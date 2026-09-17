#!/usr/bin/env python3
"""Encode the homepage hero video from the client's phone clip.

Source   assets/video/_src/slottskallan.mov  (1080p30 iPhone clip, not committed)
Output   assets/video/slottskallan-{1920,1280}.{webm,mp4} + a poster in assets/img/

The fountain at Slottskällan, handheld. The first START seconds are cut: that is
the camera being raised, with a finger at the edge of the frame.

The rest is prepared into an intermediate file first:
  1. Stabilised with vid.stab (two passes: detect, then transform). The frame
     is zoomed ZOOM percent so the compensating movement never shows an edge.
  2. Slowed to SPEED, with the missing frames synthesised by motion-compensated
     interpolation, so it stays at 30 fps. Slower, calmer water; the remaining
     sway reads as drift rather than handheld jitter.

The camera still drifts slowly downwards, so played on loop it would jump back
at the end. Instead the last FADE seconds are cross-faded into the first FADE
seconds: the output ends on its own opening frame and the loop point reads as a
soft dissolve. Audio is dropped.

WebM/VP9 for Chromium and Firefox, H.264 MP4 for Safari and anything older.
The 1280 pair is served to phones via <source media>. Foliage and fountain
spray make constant-quality encodes enormous (~20 MB), so both codecs are
two-pass to a fixed bitrate, after a light temporal denoise that strips the
phone sensor noise the encoder would otherwise spend its bits on. It all sits
under the hero scrim, so the softening is not visible.

Requires ffmpeg with libvidstab, libvpx-vp9 and libx264.
"""
import json, os, subprocess

SRC = 'assets/video/_src/slottskallan.mov'
OUT = 'assets/video'
SLUG = 'slottskallan'
START = 2.0
SPEED = 0.7
ZOOM = 4
FADE = 1.0
PREP = f'{OUT}/_src/{SLUG}-prepared.mp4'


def duration(path):
    out = subprocess.check_output(
        ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
         '-show_entries', 'stream=duration', '-of', 'json', path])
    return float(json.loads(out)['streams'][0]['duration'])


def loop_filter(width, d):
    # Trim a hair off the end: the last frame of a phone clip is often short.
    end = d - 0.05
    return (f'[0:v]split[a][b];'
            f'[a]trim={FADE}:{end},setpts=PTS-STARTPTS[main];'
            f'[b]trim=0:{FADE},setpts=PTS-STARTPTS[head];'
            f'[main][head]xfade=transition=fade:duration={FADE}:'
            f'offset={end - 2 * FADE:.3f},'
            f'hqdn3d=1.5:1.5:6:6,scale={width}:-2:flags=lanczos,format=yuv420p[v]')


def run(args, src=PREP):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, *args], check=True)


def prepare():
    """Cut, stabilise and slow the source into a near-lossless intermediate."""
    trf = f'{OUT}/_src/{SLUG}.trf'
    cut = ['ffmpeg', '-v', 'error', '-y', '-ss', str(START), '-i', SRC, '-an']
    subprocess.run([*cut, '-vf', f'vidstabdetect=shakiness=6:accuracy=15:result={trf}',
                    '-f', 'null', os.devnull], check=True)
    vf = (f'vidstabtransform=input={trf}:smoothing=45:zoom={ZOOM}:optzoom=0:'
          f'interpol=bicubic,unsharp=5:5:0.4,'
          f'setpts=PTS/{SPEED},'
          f'minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1')
    subprocess.run([*cut, '-vf', vf, '-c:v', 'libx264', '-crf', '12',
                    '-preset', 'medium', PREP], check=True)
    os.remove(trf)
    print(f'  prepared {os.path.basename(PREP)} ({duration(PREP):.1f} s)')


def main():
    os.makedirs(OUT, exist_ok=True)
    prepare()
    d = duration(PREP)
    log = f'{OUT}/_src/2pass'
    for width, kbps in ((1920, 2200), (1280, 1000)):
        fc = ['-filter_complex', loop_filter(width, d), '-map', '[v]', '-an']
        base = f'{OUT}/{SLUG}-{width}'
        rate = ['-b:v', f'{kbps}k', '-maxrate', f'{kbps * 3 // 2}k',
                '-bufsize', f'{kbps * 2}k']
        vp9 = [*fc, '-c:v', 'libvpx-vp9', *rate, '-row-mt', '1',
               '-deadline', 'good', '-passlogfile', log]
        run([*vp9, '-pass', '1', '-cpu-used', '4', '-f', 'null', os.devnull])
        run([*vp9, '-pass', '2', '-cpu-used', '1', f'{base}.webm'])
        x264 = [*fc, '-c:v', 'libx264', *rate, '-preset', 'slow',
                '-profile:v', 'high', '-passlogfile', log]
        run([*x264, '-pass', '1', '-f', 'null', os.devnull])
        run([*x264, '-pass', '2', '-movflags', '+faststart', f'{base}.mp4'])
        for ext in ('webm', 'mp4'):
            p = f'{base}.{ext}'
            print(f'  {os.path.basename(p):24} {os.path.getsize(p) // 1024:6} KB')
    for f in os.listdir(f'{OUT}/_src'):
        if f.startswith('2pass'):
            os.remove(f'{OUT}/_src/{f}')

    # Poster = the first frame of the looped output, so there is no visible
    # change when playback starts. Used as the hero <img> fallback as well.
    src = f'assets/img/_src/{SLUG}-poster.jpg'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{OUT}/{SLUG}-1920.mp4',
                    '-frames:v', '1', '-q:v', '2', src], check=True)
    print(f'  poster frame -> {src} (run build-images.py for the web variants)')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Cut and encode the homepage hero film from four AI-generated clips.

Sources  assets/video/_src/edit-{1..4}-*.mp4  (1176x784, 24 fps, not committed)
Output   assets/video/mottagningen-{1176,960}.{webm,mp4} + a poster in assets/img/_src/

The clips are slow pull-back shots, cut as a visit to the practice:
garden from the path -> house front -> meeting room -> therapy room.
Each dissolves into the next over FADE seconds, and the last one dissolves
back into the garden, so the loop has no visible seam.

The garden clip starts with the camera almost still and only reaches speed
after ~2.5 s. Opening the loop on that stretch reads as a frozen frame, so
the garden is taken from GARDEN_IN onwards. The loop tail is the 25 frames
just before GARDEN_IN: the film ends one frame before it starts.

The clips are only 1176 px wide, so the desktop encode stays at native
width (the browser scales it up under the scrim) and phones get 960.
WebM/VP9 for Chromium and Firefox, H.264 MP4 for Safari, both two-pass to a
fixed bitrate.

Requires ffmpeg with libvpx-vp9 and libx264.
"""
import os, subprocess

SRC = 'assets/video/_src'
OUT = 'assets/video'
SLUG = 'mottagningen'
FPS = 24
FADE = 1
GARDEN_IN = 108          # frame (4.5 s) where the garden camera is moving

# (file, first frame, last frame exclusive)
SHOTS = [
    ('edit-1-tradgard.mp4', GARDEN_IN, GARDEN_IN + 7 * FPS),
    ('edit-2-huset.mp4', 0, int(7.5 * FPS)),
    ('edit-3-motesrum.mp4', 0, 6 * FPS),
    ('edit-4-samtalsrum.mp4', 0, 6 * FPS),
]
TAIL = ('edit-1-tradgard.mp4', GARDEN_IN - FPS - 1, GARDEN_IN)


def edit_filter(width):
    parts, labels = [], []
    for i, (_, a, b) in enumerate(SHOTS + [TAIL]):
        parts.append(f'[{i}:v]trim=start_frame={a}:end_frame={b},'
                     f'setpts=PTS-STARTPTS,format=yuv420p[s{i}]')
        labels.append(f's{i}')
    cur, t = labels[0], 0.0
    for i, lab in enumerate(labels[1:], 1):
        _, a, b = SHOTS[i - 1]
        t += (b - a) / FPS - FADE
        out = f'x{i}'
        parts.append(f'[{cur}][{lab}]xfade=transition=fade:'
                     f'duration={FADE}:offset={t:.4f}[{out}]')
        cur = out
    parts.append(f'[{cur}]scale={width}:-2:flags=lanczos,format=yuv420p[v]')
    return ';'.join(parts)


def run(args):
    inputs = []
    for f, _, _ in SHOTS + [TAIL]:
        inputs += ['-i', f'{SRC}/{f}']
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, *args], check=True)


def main():
    log = f'{SRC}/2pass'
    for width, kbps in ((1176, 1500), (960, 900)):
        fc = ['-filter_complex', edit_filter(width), '-map', '[v]', '-an']
        base = f'{OUT}/{SLUG}-{width}'
        rate = ['-b:v', f'{kbps}k', '-maxrate', f'{kbps * 3 // 2}k',
                '-bufsize', f'{kbps * 2}k', '-g', str(2 * FPS)]
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
    for f in os.listdir(SRC):
        if f.startswith('2pass'):
            os.remove(f'{SRC}/{f}')

    # Poster = first frame of the film, so nothing jumps when playback starts.
    os.makedirs('assets/img/_src', exist_ok=True)
    poster = f'assets/img/_src/{SLUG}-poster.jpg'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{OUT}/{SLUG}-1176.mp4',
                    '-frames:v', '1', '-q:v', '2', poster], check=True)
    print(f'  poster frame -> {poster} (run build-images.py for the web variants)')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Generate responsive web variants from the source imagery.

Wide images  -> WebP at 800/1000/1600/2400px + a 1600px JPEG fallback
Portraits    -> 3:4 crop, WebP at 340/600/700/900px + a JPEG fallback

The 800 and 700 widths are for phones: a 412px screen at 1.75x density wants
~720px, which otherwise fetched the 1000/900 file at nearly twice the bytes.

Portraits are never upscaled more than 1.1x their source, so the two low-resolution
headshots (Angeli Holmstedt, Thomas Alm) emit fewer variants rather than soft ones.

Requires Pillow:  pip install Pillow
"""
import glob, os
from PIL import Image, ImageFilter, ImageOps

Image.MAX_IMAGE_PIXELS = None
OUT = 'assets/img'


# Per-width byte budgets for the full-bleed backgrounds. Detailed foliage
# encodes far larger than an interior at the same quality, so target a size
# instead of a fixed quality: the scrim hides the difference either way.
BUDGET = {2400: 300 * 1024, 1600: 165 * 1024, 1000: 80 * 1024, 800: 55 * 1024}


def variants(im, base, widths, jpg_width, quality=80, budget=False):
    made = []
    for w in widths:
        h = round(im.height * w / im.width)
        p = f'{base}-{w}.webp'
        resized = im.resize((w, h), Image.LANCZOS)
        q = quality
        resized.save(p, 'WEBP', quality=q, method=6)
        if budget:
            cap = BUDGET.get(w, 165 * 1024)
            while os.path.getsize(p) > cap and q > 42:
                q -= 7
                resized.save(p, 'WEBP', quality=q, method=6)
            # Dense foliage will not fit a sane budget on quality alone. A
            # sub-pixel blur costs nothing visually behind a scrim and cuts the
            # high-frequency detail that WebP is spending all its bytes on.
            blur = 0.0
            while os.path.getsize(p) > cap and blur < 1.6:
                blur += 0.4
                resized.filter(ImageFilter.GaussianBlur(blur)).save(
                    p, 'WEBP', quality=q, method=6)
        made.append(p)
    h = round(im.height * jpg_width / im.width)
    p = f'{base}.jpg'
    jm = im.resize((jpg_width, h), Image.LANCZOS)
    jq = min(80, quality + 8)
    jm.save(p, 'JPEG', quality=jq, optimize=True, progressive=True)
    if budget:
        while os.path.getsize(p) > 200 * 1024 and jq > 46:
            jq -= 7
            jm.save(p, 'JPEG', quality=jq, optimize=True, progressive=True)
    made.append(p)
    return made


def main():
    total = 0
    os.makedirs(f'{OUT}/team', exist_ok=True)

    # Every wide image is used as a full-bleed background under a 70-88% dark
    # scrim, so fine detail is not visible and a lower quality saves a lot of
    # weight. Detailed foliage shots in particular were several hundred KB.
    print('Wide / background images (size-budgeted; all sit under a scrim):')
    for src in sorted(glob.glob(f'{OUT}/_src/*.jpg')):
        slug = os.path.splitext(os.path.basename(src))[0]
        im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
        widths = [w for w in (2400, 1600, 1000, 800) if w <= im.width]
        made = variants(im, f'{OUT}/{slug}', widths, min(1600, im.width),
                        quality=72, budget=True)
        for p in made:
            total += os.path.getsize(p)
        kb = sum(os.path.getsize(x) for x in made) // 1024
        print(f'  {slug:14} {im.width}px -> {widths} + jpg   {kb:5} KB')

    print('\nTeam portraits (3:4):')
    for src in sorted(glob.glob('assets/team/*.jpg')):
        slug = os.path.splitext(os.path.basename(src))[0]
        im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
        target_w = min(900, int(im.width * 1.1))       # never upscale beyond 1.1x
        base = ImageOps.fit(im, (target_w, round(target_w * 4 / 3)),
                            Image.LANCZOS, centering=(0.5, 0.35))
        widths = [w for w in (900, 700, 600, 340) if w <= target_w] or [target_w]
        for p in variants(base, f'{OUT}/team/{slug}', widths,
                          min(600, target_w), quality=82):
            total += os.path.getsize(p)
        flag = '  (low-res source)' if im.width < 900 else ''
        print(f'  {slug:18} {im.width}px -> {widths} + jpg{flag}')

    build_og()
    build_brand()
    print(f'\nTotal generated: {total // 1024} KB')




# --------------------------------------------------------------------------
# Share image
#
# Link previews (Facebook, LinkedIn, Slack, iMessage) crop to 1.91:1 and are
# shown small, so the homepage gets its own 1200x630 cut rather than a hero
# variant: the castle and Gårdshuset say "Uppsala, this place" at a glance.
# --------------------------------------------------------------------------
def build_og():
    src = f'{OUT}/_src/slottet.jpg'
    if not os.path.exists(src):
        print(f'\n  skip (missing) {src}')
        return
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    og = ImageOps.fit(im, (1200, 630), Image.LANCZOS, centering=(0.5, 0.4))
    og.save(f'{OUT}/og-home.jpg', 'JPEG', quality=84, optimize=True, progressive=True)
    print(f'\nShare image:\n  og-home.jpg          {os.path.getsize(f"{OUT}/og-home.jpg") // 1024:4} KB')


# --------------------------------------------------------------------------
# Brand marks
#
# btf.jpg has no alpha, so it renders as a white box on any non-white ground.
# (The logo is now an SVG, see build-logo.py.) Key the white
# out, feathering the edge band so the mark stays smooth.
# --------------------------------------------------------------------------
def key_white(src, dest, make_white=False, floor=6, ramp=42):
    im = Image.open(src).convert('RGB')
    out = Image.new('RGBA', im.size)
    px, op = im.load(), out.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            r, g, b = px[x, y]
            d = 255 - min(r, g, b)          # 0 on pure white
            if d <= floor:
                op[x, y] = (255, 255, 255, 0)
            else:
                a = 255 if d >= ramp else int(d * 255 / ramp)
                op[x, y] = (255, 255, 255, a) if make_white else (r, g, b, a)
    out.save(dest, 'PNG', optimize=True)
    return dest


def build_brand():
    jobs = [
        ('assets/brand/btf.jpg', 'assets/brand/btf.png', False),
    ]
    print('\nBrand marks (keying out white backgrounds):')
    for src, dest, white in jobs:
        if not os.path.exists(src):
            print(f'  skip (missing) {src}')
            continue
        key_white(src, dest, make_white=white)
        print(f'  {os.path.basename(dest):20} {os.path.getsize(dest)//1024:4} KB'
              f"{'  (reversed / white)' if white else ''}")

if __name__ == '__main__':
    main()

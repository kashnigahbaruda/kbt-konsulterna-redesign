"""Build the logo files in assets/brand/ from the client's outlined lockup
(heart-source.svg): the heart mark plus "KBT Konsulterna" as glyph outlines.
The tagline group in that file is dropped, the type is re-centred on the
heart, everything is recoloured to the site's deep green, and the heart alone
is rasterised for the PNG favicons.

Not part of the normal build. Run it only when the client's file changes:

    python3 -m venv .venv && .venv/bin/pip install fonttools pillow
    .venv/bin/python tools/build-logo.py
"""
import os, re
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import SVGPath
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
BRAND = f'{PROJ}/assets/brand'
DEEP = '#1B3A38'
DEEP_RGB = (0x1B, 0x3A, 0x38)
H = 100                                   # output canvas height, logo units

src = open(f'{BRAND}/heart-source.svg').read()

# --- pull the shapes out of the client's file --------------------------------
# Layout of that file: one top-level <path> (the heart), then two <g>s of
# glyph outlines — the name, then the tagline. Only the first group is kept.
def parse(d):
    rec = RecordingPen()
    SVGPath.fromstring(f'<svg><path d="{d}"/></svg>'.encode()).draw(rec)
    return rec

def bounds(rec):
    bp = BoundsPen(None); rec.replay(bp); return bp.bounds

def to_d(rec, scale, dx=0.0, dy=0.0):
    pen = SVGPathPen(None, ntos=lambda v: f'{v:.2f}'.rstrip('0').rstrip('.'))
    rec.replay(TransformPen(pen, (scale, 0, 0, scale, dx, dy)))
    return pen.getCommands()

heart = None
groups = []
depth = 0
for tag, attrs in re.findall(r'<(g|/g|path)([^>]*)>', src):
    if tag == 'g':
        depth += 1; groups.append([])
    elif tag == '/g':
        depth -= 1
    else:
        rec = parse(re.search(r'\sd="([^"]+)"', attrs).group(1))
        if depth == 0:
            assert heart is None, 'expected a single top-level path (the heart)'
            heart = rec
        else:
            groups[-1].append(rec)
assert heart is not None and len(groups) >= 1, 'unexpected file structure'
name = groups[0]

hx0, hy0, hx1, hy1 = bounds(heart)
hw, hh = hx1 - hx0, hy1 - hy0
nb = [bounds(g) for g in name]
nx0, ny0 = min(b[0] for b in nb), min(b[1] for b in nb)
nx1, ny1 = max(b[2] for b in nb), max(b[3] for b in nb)
print(f'heart {hw:.0f}×{hh:.0f}, name {nx1-nx0:.0f}×{ny1-ny0:.0f} at x={nx0:.0f}')

# --- lockup ------------------------------------------------------------------
s = H / hh                                 # heart fills the canvas height
# Without the tagline the name sits high; centre it on the heart instead.
dy = ((hy0 + hy1) / 2 - (ny0 + ny1) / 2) * s
W = int(round(nx1 * s + 0.5))

def lockup(color):
    paths = [f'    <path d="{to_d(heart, s, -hx0 * s, -hy0 * s)}"/>']
    paths += [f'    <path d="{to_d(g, s, -hx0 * s, dy - hy0 * s)}"/>' for g in name]
    body = '\n'.join(paths)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" role="img" aria-label="KBT-Konsulterna">\n'
            f'  <g fill="{color}">\n{body}\n  </g>\n</svg>\n')

open(f'{BRAND}/logo.svg', 'w').write(lockup(DEEP))
open(f'{BRAND}/logo-white.svg', 'w').write(lockup('#FFFFFF'))

# --- mark alone, square, for the SVG favicon ---------------------------------
M = 100
ms = 84 / max(hw, hh)
mw, mh = hw * ms, hh * ms
open(f'{BRAND}/logo-mark.svg', 'w').write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {M} {M}" width="{M}" height="{M}">\n'
    f'  <path fill="{DEEP}" d="{to_d(heart, ms, (M - mw) / 2 - hx0 * ms, (M - mh) / 2 - hy0 * ms)}"/>\n'
    f'</svg>\n')

# --- raster favicons from the heart -----------------------------------------
def flatten(rec, scale, tx, ty, steps=24):
    """Contours of the heart as polygons, curves subdivided."""
    polys, cur, last = [], [], None
    P = lambda p: ((p[0] - hx0) * scale + tx, (p[1] - hy0) * scale + ty)
    for op, args in rec.value:
        if op == 'moveTo':
            if cur: polys.append(cur)
            cur, last = [P(args[0])], args[0]
        elif op == 'lineTo':
            cur.append(P(args[0])); last = args[0]
        elif op == 'curveTo':
            p0, (p1, p2, p3) = last, args
            for i in range(1, steps + 1):
                t = i / steps; u = 1 - t
                cur.append(P((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
                              u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1])))
            last = p3
        elif op == 'qCurveTo':
            p0, p1, p2 = last, args[0], args[-1]
            for i in range(1, steps + 1):
                t = i / steps; u = 1 - t
                cur.append(P((u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0],
                              u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1])))
            last = p2
        elif op in ('closePath', 'endPath'):
            if cur: polys.append(cur); cur = []
    if cur: polys.append(cur)
    return polys

def favicon(size, path):
    ss = 4; S = size * ss; pad = S * 0.08
    sc = (S - 2 * pad) / max(hw, hh)
    w, h = hw * sc, hh * sc
    mask = Image.new('L', (S, S), 0)
    d = ImageDraw.Draw(mask)
    # The heart is one outer contour followed by one inner contour (the hole).
    for i, poly in enumerate(flatten(heart, sc, (S - w) / 2, (S - h) / 2)):
        d.polygon(poly, fill=255 if i == 0 else 0)
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    img.paste(Image.new('RGBA', (S, S), DEEP_RGB + (255,)), (0, 0), mask)
    img.resize((size, size), Image.LANCZOS).save(path)

favicon(512, f'{BRAND}/icon-512.png')
favicon(180, f'{BRAND}/apple-touch-icon.png')
print(f'written logo.svg, logo-white.svg ({W}×{H}), logo-mark.svg, icon-512.png, apple-touch-icon.png')

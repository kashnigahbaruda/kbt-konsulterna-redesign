# Client photographs — committed sources

Drop the client's own photographs of the practice here as full-quality JPEGs, then run:

```bash
python3 tools/build-images.py
```

They build exactly like the stock imagery in `../_src/` — WebP at 800/1000/1600/2400px plus a
JPEG fallback — and become available to `pic_wide(base, '<filename-without-extension>', alt)`
in `tools/build-site.py`.

## Why this directory exists separately from `_src/`

`assets/img/_src/` is **gitignored**, on the grounds that everything in it is CC0 and
`tools/fetch-images.py` can re-download it on demand. Client photographs are neither CC0 nor
re-fetchable — nothing can recover them but the client — so this directory is **committed**.
That distinction is the whole reason for the split; `build-images.py` reads both and treats
them identically.

## What to put here

A cropped, web-ready JPEG at quality 90+, named for how the page will refer to it
(`rum-samtal.jpg`, not `IMG_1851.jpg`). Keep the untouched original with the client — this is
a derived file, and the crop should be recorded in `docs/IMAGE-CREDITS.md` so it can be redone.

## Two things that bit us the first time

**0. Measure the right third, not the frame.** This is the check that would have saved two
rounds. A hero candidate's average sharpness tells you nothing, because the scrim hides the left
of it; what matters is how much detail survives in the **right third** at the size the hero
actually renders (1512 × 450 from a 1440 px viewport). Under 2 is visibly soft — the CC0 stock
these replace sits around 3.4. `docs/IMAGE-CREDITS.md` has the worked comparison.

**1. The hero scrim is diagonal, not uniform.** `.hero__scrim` runs from
`rgba(19,41,40,0.88)` at the left edge to `rgba(19,41,40,0.10)` at the right. The comment in
`build-images.py` that every wide image "is used under a 70–88% dark scrim, so fine detail is
not visible" is only true of the left quarter. **The right third of every hero is very nearly
unscrimmed**, so whatever sits there is seen at full quality. Compose accordingly: put the
quiet part of the frame on the right, and anything you would rather hide on the left, where
the headline and the heavy scrim are.

**2. Anything narrower than 2400px gets upscaled.** The variant ladder stops at the source
width, so a 1700px source tops out at a 1600px variant — which the browser then upscales on
any high-density display, magnifying encoder artefacts instead of absorbing them. Sources
should be **at least 2400px on the long edge**, ideally more.

## Judging whether a photograph is good enough before wiring it in

The first September 2026 delivery failed on the resolution rule above: at 2160 px square its
crops could not feed a 2400 px variant, so the browser upscaled them and magnified the phone's
shadow smearing. The 4284 px re-delivery of the same captures fixed that by downsampling
instead — the smearing is still in the file, but it averages away rather than being enlarged.
Three of those frames are live; see `docs/IMAGE-CREDITS.md`.

So measure before blaming the encoder, and measure again before trusting a new batch:

```python
from PIL import Image, ImageChops, ImageStat

def detail(path, box, f=2):
    """How much information a region carries above 1/f resolution.
    Compare regions within one file; >3 is healthy, ~1 is smeared."""
    c = Image.open(path).convert('L').crop(box)
    w, h = c.size
    back = c.resize((w // f, h // f), Image.LANCZOS).resize((w, h), Image.LANCZOS)
    return ImageStat.Stat(ImageChops.difference(c, back)).mean[0]
```

Sample a bright region and a dark one from the same frame. **If detail tracks brightness, the
phone's noise reduction has smeared the shadows** — it does that to low-contrast fine texture
in low light, and it is baked in at capture. No encoder setting and no higher-resolution
export of that same exposure will bring it back; only a re-shoot with more light will.
`docs/IMAGE-CREDITS.md` has the worked example and the shooting notes to send the client.

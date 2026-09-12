# KBT-Konsulterna — website redesign

A redesign proposal for [kbt-konsulterna.se](https://kbt-konsulterna.se/), a private
psychology practice in central Uppsala. Static HTML and CSS — no build step, no dependencies.

> **This is a design preview, not the live practice website.** Every page carries
> `noindex, nofollow` so it cannot compete with the client's real site in search results.
> Remove that before any real launch — see [Going live](#going-live).

Locally, just **open `index.html` in a browser**. Every link resolves from `file://`, so the
whole thing can be zipped and sent on as-is.

```bash
# or serve it, if you prefer clean URLs while reviewing
python3 -m http.server 8000
```

---

## What's here

```
index.html                    Homepage
vuxna/                        Adults — treatment, couples, addiction, assessment
barn-och-ungdom/              Children & young people
organisationer/               Supervision, training, rehabilitation for employers
medarbetare/                  Team index + 7 individual bio pages
priser/                       Prices, terms, region referrals
kontakt/                      Contact, both forms, directions
om-oss/                       About, what KBT is, evidence base, online, licensing
om-oss/vanliga-fragor.html    All 16 FAQs
akut-hjalp/                   Emergency help

assets/css/site.css           The whole design system, ~660 lines
assets/js/site.js             Mobile nav + scroll reveals. Progressive enhancement only.
assets/img/                   Generated responsive WebP + JPEG
assets/team/                  The client's own photography
assets/brand/                 Logo and accreditation marks
tools/                        Scripts that generated the pages and the image set
```

17 pages, restructured from the current site's 108. The current site runs two complete
parallel content trees at once — seven page pairs are byte-identical at two indexable URLs —
and buries booking and prices inside a 12-item "OM OSS & INFO" menu. The full audit, content
inventory, proposed information architecture and redirect map are held separately from this
repo.

## The design

- **Palette "Slottskällan"** — named after where the practice actually sits, by the castle
  spring below Uppsala castle. Cool limestone ground, deep spruce-teal, a muted linden accent.
  Deliberately not the sage-green-and-blob look of the therapy category.
- **Familjen Grotesk** (a Swedish grotesque, by Letters from Sweden) for display and UI,
  **Newsreader** for long-form body. Sans headlines over serif prose — inverted from the
  professional-services norm, and the bios run to 500 words so they deserve a reading face.
- **Whitespace does all the separating.** No card borders, no rules, no shadows-as-structure.
  Sections are separated by vertical rhythm and alternating ground tone.
- **Full-bleed imagery as punctuation** — a fullscreen hero, then image bands marking the
  major transitions. Not every image is full-bleed.
- **Real SVG icons**, not font glyphs — six of them (arrow, check, plus, chevron, menu,
  close), in an inline sprite referenced with `<use>`, sized in `em` and stroked in
  `currentColor` so they always match the text beside them. Inline rather than an external
  sprite so they also resolve over `file://`.
- **Signature element: "Var ska jag börja?"** — the homepage carries a large typographic list
  written in the visitor's own words ("Jag sover inte om nätterna.") rather than clinical
  category names, each line going straight to the right page. It fixes the old site's worst
  flaw — every real problem buried three clicks deep — in one move.

### Copy

The client's existing prose is better than most agency copy: first-person, specific, warm.
**It is carried over close to verbatim**, and the seven bios and 16 FAQs are pulled
programmatically from a crawl of the current site so nothing drifted in transcription. New
copy (router lines, navigation, CTAs, headings) is written from the visitor's side of the
screen.

No testimonials — the client has deliberately chosen not to publish patient reviews because
they work under confidentiality. That decision is respected, not worked around.

## Quality

Checked across all 17 pages:

- No broken internal links or dangling anchors
- One `<h1>` per page, no skipped heading levels, every image has `alt`
- No duplicate `id`s, every form input has a label
- Skip link, real landmarks, visible keyboard focus
- `lang="sv"` — the current site declares `lang="en-US"` on entirely Swedish content
- No zoom restriction — the current site sets `maximum-scale=1.5`, which fails WCAG 1.4.4
- No horizontal overflow at 360px on any page
- **Text contrast meets WCAG AA** — 2,113 rendered text nodes measured at 1280px and 390px
  with the mobile menu open: zero failures. Getting there fixed four real bugs where a
  descendant selector was overriding a button or bold colour to invisible. Text over
  photography is excluded from that measurement and was checked by eye; it is white on a
  70–88% dark scrim.
- 215 rendered icon instances checked for minimum size and 3:1 non-text contrast
  (WCAG 1.4.11): zero failures
- Mobile menu is a fixed overlay panel below the header with its own scroll and a 44×44px
  toggle — verified the header stays pinned and the scroll position is preserved when the
  menu is opened at any scroll depth
- Responsive `<picture>` with WebP + JPEG fallback and explicit dimensions to prevent
  layout shift
- Works with JavaScript disabled — a `<noscript>` rule opens the mobile menu and hides the
  burger, and scroll reveals only hide content once JS is present. The hero load sequence is
  opt-in via `prefers-reduced-motion: no-preference`, so content is never hidden waiting on
  an animation that may not run
- Titles ≤ 70 chars, meta descriptions 50–165 chars, canonical URLs, `MedicalBusiness` and
  `FAQPage` structured data

### Weight

Homepage is about 710 KB total across 13 images at a 1440px viewport, and roughly 120 KB
before the fold. Every wide image sits under a dark scrim, so `build-images.py` encodes those
to a per-width byte budget rather than a fixed quality.

## Regenerating

The pages are plain static HTML and can be edited directly. They were *generated* from
`tools/build-site.py`, which holds the shared header, footer and navigation so 17 pages
couldn't drift apart. If you take over the HTML by hand, retire the generator rather than
running both.

```bash
python3 tools/build-site.py     # regenerate all 17 pages
python3 tools/fetch-images.py   # re-download source imagery
python3 tools/build-images.py   # regenerate responsive variants + keyed brand marks
```

`build-images.py` needs Pillow (`pip install Pillow`). Nothing else has dependencies.

Note: `build-site.py` reads the bios and FAQs from a crawl of the current site
(`research/crawl-pages.json`), which is not included in this repo. Re-running it needs that
file; the generated HTML here is complete and standalone without it.

## Going live

1. **Set `PREVIEW = False`** in `tools/build-site.py` and rebuild. That flag is what emits the
   `noindex, nofollow` tag — leaving it on would keep the real site out of Google entirely.
2. **Wire up the contact forms.** Both have `action="#"` and do nothing. They need a backend
   or a form service.
3. **Confirm the prices** — 1 500 kr / 45 min, 2 400 kr / 60 min and 1 800 kr / 45 min are
   carried over from the current site and need checking against 2026 rates.
4. **Confirm the opening hours** — Mon–Fri 09:00–17:00 comes from the current site's schema
   markup, not from any visible page copy.
5. **Confirm the right to display the accreditation marks** (Socialstyrelsen,
   Psykologförbundet, MINT, BTF). They are third-party trademarks, and Socialstyrelsen in
   particular is a government authority with rules about implying endorsement.
6. **Set up the redirects.** The current site has ~37 URLs that need to 301 to a single
   canonical target, one hop only. Nothing should 404 — some retired pages carry real content
   and external inbound links.

## Images and licensing

Team photography, the logo and the accreditation marks belong to the client and are reused
from the current site. All stock photography is **CC0 / public domain**, sourced from
Wikimedia Commons, so there is no ongoing licence obligation and no risk of a stock-photo
invoice later.

No identifiable faces appear in any stock image — on a psychology practice's site a
recognisable face invites the reader to assume they are looking at a patient. Every selection
is an empty interior, a landscape, hands only, or a figure turned away. The only faces on the
site are the seven practitioners.

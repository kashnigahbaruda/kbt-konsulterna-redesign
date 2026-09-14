# KBT-Konsulterna — website redesign

A redesign proposal for [kbt-konsulterna.se](https://kbt-konsulterna.se/), a private
psychology practice in central Uppsala. Static HTML and CSS — no build step, no dependencies.

**Live preview → https://kashnigahbaruda.github.io/kbt-konsulterna-redesign/**

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
vuxna/                        Adults — hub
  behandling/                   + 10 treatment topics (anxiety, depression, sleep …)
  utredning/                    + 3 assessment topics (adhd, autism, re-assessment)
  parterapi/ beroende/ psykiatri/
barn-och-ungdom/              Children & young people — hub
  behandling/                   + 5 treatment topics
  utredning/                    + 3 assessment topics
  stod/                         + 4 pages for the adults around the child
organisationer/               Employers — hub
  handledning/ utbildning/ rehabilitering/ skadligt-bruk/ kontakt/
medarbetare/                  Team index + 7 individual bio pages
priser/                       Prices, terms, region referrals
kontakt/                      Contact, both forms, directions
om-oss/                       About, what KBT is, evidence base, online, licensing
om-oss/vanliga-fragor.html    All 16 FAQs
akut-hjalp/                   Emergency help
sitemap.xml                   Generated — all 55 canonical URLs
robots.txt                    Generated — allows everything, points at the sitemap

assets/css/site.css           The whole design system, ~880 lines
assets/js/site.js             Mobile nav + scroll reveals. Progressive enhancement only.
assets/img/                   Generated responsive WebP + JPEG
assets/team/                  The client's own photography
assets/brand/                 Logo and accreditation marks
assets/fonts/                 Self-hosted variable fonts + their OFL licences (generated)
tools/articles.py             The topic tree: copy for all 38 sub-pages
tools/build-fonts.py          Fetches the OFL fonts and cuts Newsreader down
tools/build-site.py           Shared shell + every page builder
```

55 pages, restructured from the current site's 108. The current site runs two complete
parallel content trees at once — seven page pairs are byte-identical at two indexable URLs —
and buries booking and prices inside a 12-item "OM OSS & INFO" menu.

### The topic layer

The current site carries 38 pages in this layer — 13 section hubs and 25 small pages, one
per problem someone might search for
(`/vuxna/psykologisk-behandling-terapi/flygfobi/`, `…/sorg/`, and so on), reachable through a
sidebar navigator. The client added them for SEO, and they are the pages that rank for the
long-tail queries — "flygfobi behandling uppsala", "adhd utredning vuxen privat".

They are rebuilt here as **38 real pages** rather than folded into anchors on the hubs.
Each one carries what the originals did not:

- **A sticky sibling navigator** — the level-2 pages of the section, with the active branch's
  children nested under it. Below 62rem it moves under the article rather than disappearing.
- **Breadcrumbs** plus `BreadcrumbList` structured data.
- **A named, credentialed clinician** — `MedicalWebPage` with `author`. Search engines weight
  demonstrated expertise heavily for health content, and the old pages named nobody.
- **Related topics and prev/next**, so the articles link to each other rather than only
  upward to the hub.

A client-facing summary of all this — in Swedish, ready to send to the practice as-is —
is held with the other working documents outside this repo (`09-TILL-KUNDEN-AMNESSIDOR.md`).
It covers what changed, what the practice needs to sign off, and what to expect at launch.

The originals were thin — fourteen under 200 words, the shortest 58, and thirty of the
thirty-eight under 350 once ported. They have since been **expanded to ~500 words each**
(18,750 words across the topic layer; median 505, shortest 337). That new material is
written by us, not ported, and needs the client's clinical sign-off — see
*[Known gaps](#known-gaps)*.

## The design

- **Palette "Slottskällan"** — named after where the practice actually sits, by the castle
  spring below Uppsala castle. Cool limestone ground, deep spruce-teal, a muted linden accent.
  Deliberately not the sage-green-and-blob look of the therapy category.
- **Familjen Grotesk** (a Swedish grotesque, by Letters from Sweden) for display and UI,
  **Newsreader** for long-form body. Sans headlines over serif prose — inverted from the
  professional-services norm, and the bios run to 500 words so they deserve a reading face.
  Both are self-hosted from `assets/fonts/` rather than loaded from Google Fonts — no visitor
  IPs sent to Google, and no render-blocking stylesheet on a third-party origin. Newsreader
  is cut to weights 400–600 with its optical size pinned at 18: it is only ever set between
  17 and 34px here, and the full optical-size axis tripled the file (132 → 38 KB) for no
  visible difference at body size. Metric-adjusted Arial/Georgia fallbacks keep text from
  reflowing when the fonts swap in on a slow connection.
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

## Known gaps

### The expanded copy needs clinical review — this is the blocker

The topic pages were ported from the client's own text, then expanded. The **ported**
material asserts nothing new. The **added** material does, and a licensed psychologist at
the practice should read it before launch. Specifically, these claims are mainstream and
sourced from standard clinical guidance, but are ours and not the client's:

| Claim | Page |
|---|---|
| KBT-i is first-line for chronic insomnia, ahead of sleep medication | `vuxna/behandling/somn/` |
| Sleep restriction is not suitable for everyone and is assessed first | `vuxna/behandling/somn/` |
| *Applied tension* is used for blood/injection phobia with fainting | `vuxna/behandling/fobier/` |
| Sleep-need ranges by age (≈10–13 / 9–11 / 8–10 hours) | `barn-och-ungdom/behandling/somn/` |
| Asking a young person about suicidal thoughts does not increase risk | `barn-och-ungdom/behandling/depression/` |
| ERP is among the best-documented treatments for childhood OCD | `barn-och-ungdom/behandling/ocd/` |
| Parent work is the most effective intervention for younger children's behaviour | `barn-och-ungdom/stod/foraldrar/` |
| Placed children have markedly poorer school outcomes as a group | `barn-och-ungdom/stod/hvb-familjehem/` |
| Behavioural activation is the most-studied component in depression treatment | `vuxna/behandling/depression/` |

Two operational claims need the client's confirmation rather than a clinician's, because
they describe how the practice works:

- **"Vid gemensam vårdnad behöver båda vårdnadshavarna vanligtvis samtycka"**
  (`barn-och-ungdom/behandling/`) — legally sound, but it describes an intake rule the
  practice has to actually follow.
- **Confidentiality when an employer pays** (`organisationer/rehabilitering/` and
  `…/skadligt-bruk/`) — the pages state that the employer is told that contact exists and,
  with consent, what bears on work capacity, but never the content of sessions. Confirm
  this matches the practice's actual agreements.

### Smaller

- **No page-level `FAQPage` schema yet.** Ten topic pages carry question-form headings with
  answers — 35 questions in all, concentrated on the assessment pages, which are the highest
  commercial-intent pages on the site. Marking those up is a cheap win, but do it *after*
  sign-off: the markup has to match the visible text exactly, so it cannot be written before
  the copy is final.
- `organisationer/kontakt/` is 337 words, the shortest page. That is appropriate for a
  contact page and was left alone rather than padded.
- The client's own source pages quote the assessment conversation at **1 500 kr** on the
  adult pages and **1 400 kr** on one children's page. The children's FAQ here avoids the
  figure entirely; the adult pages carry 1 500 kr. Needs one answer.

## Quality

Checked across all 55 pages:

- No broken internal links or dangling anchors — 4 073 checked, each resolving to a real
  file rather than a directory, so the build works over `file://` as promised
- One `<h1>` per page, no skipped heading levels, every image has `alt`
- No duplicate `id`s, every form input has a label
- Skip link, real landmarks, visible keyboard focus
- `lang="sv"` — the current site declares `lang="en-US"` on entirely Swedish content
- No zoom restriction — the current site sets `maximum-scale=1.5`, which fails WCAG 1.4.4
- No horizontal overflow at 381px on any page, re-checked across all 24 expanded pages. Adding the topic layer surfaced two real
  bugs here, both now fixed: the header row (logo + "Boka samtal" + burger) overflowed by
  ~3px on every page below 27rem, and the topic cards' hover bleed ran past the gutter
- **Text contrast meets WCAG AA** — 2,113 rendered text nodes measured at 1280px and 390px
  with the mobile menu open, plus 1,115 more across the expanded topic layer (article prose,
  navigator, bylines, cards, prev/next) with translucent backgrounds properly composited:
  zero failures. Getting there fixed four real bugs where a
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
- Every one of the 55 pages has a unique `<title>`, meta description and canonical URL —
  verified, no duplicates
- `MedicalBusiness`, `FAQPage`, `BreadcrumbList`, `MedicalWebPage` and `ProfilePage`/`Person`
  structured data; every JSON-LD block parses. `BreadcrumbList` is read back out of each
  page's visible breadcrumb at build time, so the two cannot disagree
- **Lighthouse 13** (September 2026, served with gzip as any real host would, `noindex`
  stripped because Lighthouse fails the preview on it by design): accessibility, best
  practices, SEO and agentic browsing 100 on every page. Performance 100 on desktop, and on
  mobile on 52 of 55 pages; three bios score 98–99, where the LCP element is the portrait
  itself. The preview as published scores SEO 69 — that is the `noindex`, and nothing else

### Weight

Homepage is about 710 KB total across 13 images at a 1440px viewport, and roughly 120 KB
before the fold. Every wide image sits under a dark scrim, so `build-images.py` encodes those
to a per-width byte budget rather than a fixed quality. Wide images also come at 800px and
portraits at 700px, because a phone at 1.75x density wants about 720px and would otherwise
fetch the 1000/900 file at nearly twice the bytes. On heroes and bios that file is the LCP.

## Regenerating

The pages are plain static HTML and can be edited directly. They were *generated* from
`tools/build-site.py`, which holds the shared header, footer and navigation so 55 pages
couldn't drift apart. The topic copy lives in `tools/articles.py`, and the hubs link into it
from the same data, so a hub card and its page cannot disagree. If you take over the HTML by hand, retire the generator rather than
running both.

```bash
python3 tools/build-site.py     # regenerate all 55 pages + sitemap.xml
python3 tools/fetch-images.py   # re-download source imagery
python3 tools/build-images.py   # regenerate responsive variants + keyed brand marks
python3 tools/build-logo.py     # regenerate the logo SVGs + favicons from the client's file
python3 tools/build-fonts.py    # re-fetch and rebuild the self-hosted fonts
```

`build-images.py` needs Pillow (`pip install Pillow`); `build-fonts.py` needs fonttools and
brotli; `build-logo.py` needs fonttools and Pillow, and only has to run when the client's
logo file changes. Nothing else has dependencies.

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
6. **Set up the redirects.** 69 old URLs need to 301 to a single canonical target, one hop
   only — the explicit 69-row map is held with the working documents outside this repo
   (`08-REDIRECTS.md`). Wildcards will not do: seven of the
   ten treatment slugs change. Every target in that map has been verified to exist.
7. **Submit the new `sitemap.xml`** in the same release as the redirects, and retire the old
   sitemap entries at the same time.
8. **Set long cache lifetimes on the real host.** GitHub Pages sends `max-age=600` on
   everything and cannot be changed, which is why Lighthouse flags ~250 KB of short-cached
   files on the preview. On production, give `assets/fonts/`, `assets/img/`, `assets/brand/`
   and `assets/team/` a year (`Cache-Control: public, max-age=31536000, immutable`). Keep
   `site.css` and `site.js` short-cached, or add a version to their URLs first: they keep the
   same filename when they change, so a long cache would serve returning visitors stale styles.
   HTML should stay short-cached.
9. **Minify the CSS.** `site.css` is served as the commented source: 11.6 KB gzipped, 6.9 KB
   minified — a ~4.7 KB saving on a render-blocking file, which Lighthouse lists under
   "Minify CSS". Do it in `build-site.py` (write `site.min.css` and point the pages at it) so
   `site.css` stays the file you edit. It was left out of the preview on purpose: pages
   pointing at a generated file would silently ignore hand edits to `site.css` until the next
   rebuild.
10. **Re-run Lighthouse against the live domain in an incognito window.** Browser extensions
    inject scripts that Lighthouse counts — React Developer Tools shows up as ~51 KB of
    "unused JavaScript" that is not the site's. The site's only script is `site.js`, 1.5 KB.

## Images and licensing

Team photography, the logo and the accreditation marks belong to the client. The logo files
in `assets/brand/` are generated from the client's outlined lockup (`heart-source.svg`),
recoloured to the site's deep green. All stock photography is **CC0 / public domain**, sourced from
Wikimedia Commons, so there is no ongoing licence obligation and no risk of a stock-photo
invoice later.

No identifiable faces appear in any stock image — on a psychology practice's site a
recognisable face invites the reader to assume they are looking at a patient. Every selection
is an empty interior, a landscape, hands only, or a figure turned away. The only faces on the
site are the seven practitioners.

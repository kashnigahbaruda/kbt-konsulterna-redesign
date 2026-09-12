#!/usr/bin/env python3
"""Generate the static HTML for the KBT-Konsulterna redesign.

The shared shell (head, header, footer) lives here so the 18 pages cannot drift
apart. Output is plain, standalone HTML — no runtime dependency on this script.
Links use explicit index.html so the site works from file:// as well as a server;
<link rel="canonical"> carries the clean production URL.

Usage:  python3 tools/build-site.py
"""
import html as H
import os
import re

from articles import TREE

try:
    from PIL import Image
except ImportError:
    Image = None

SITE = 'https://kbt-konsulterna.se'

# True while this build is being published as a shareable preview (GitHub Pages).
# Set to False for the real launch — noindex on production would be catastrophic.
PREVIEW = True
TEL = '018 – 10 40 44'
TEL_HREF = 'tel:+4618104044'
MAIL = 'kontakt@kbt-konsulterna.se'
ADDR = 'Gårdshuset, Slottskällan, Sjukhusvägen 3, 753 09 Uppsala'
MAPS = ('https://www.google.com/maps/place/Sjukhusv%C3%A4gen+3,+753+09+Uppsala/'
        '@59.8536888,17.6380005,18z')

_dims = {}


def dim(path):
    """Real pixel dimensions, so width/height attrs prevent layout shift."""
    if path in _dims:
        return _dims[path]
    wh = (2400, 1600)
    if Image and os.path.exists(path):
        with Image.open(path) as im:
            wh = im.size
    _dims[path] = wh
    return wh


# --------------------------------------------------------------------------
# Navigation. (label, href, [children])
# --------------------------------------------------------------------------
NAV = [
    ('Vuxna', 'vuxna/index.html', [
        ('Psykologisk behandling', 'vuxna/behandling/index.html'),
        ('Parterapi', 'vuxna/parterapi/index.html'),
        ('Skadligt bruk & beroende', 'vuxna/beroende/index.html'),
        ('Utredning & bedömning', 'vuxna/utredning/index.html'),
        ('Psykiatrisk bedömning', 'vuxna/psykiatri/index.html'),
    ]),
    ('Barn & ungdom', 'barn-och-ungdom/index.html', [
        ('Psykologisk behandling', 'barn-och-ungdom/behandling/index.html'),
        ('Utredning & bedömning', 'barn-och-ungdom/utredning/index.html'),
        ('Stöd till vuxna runt barnet', 'barn-och-ungdom/stod/index.html'),
    ]),
    ('För organisationer', 'organisationer/index.html', [
        ('Handledning & coaching', 'organisationer/handledning/index.html'),
        ('Föreläsningar & utbildning', 'organisationer/utbildning/index.html'),
        ('Rehabilitering', 'organisationer/rehabilitering/index.html'),
        ('Skadligt bruk', 'organisationer/skadligt-bruk/index.html'),
        ('Kontakt för uppdrag', 'organisationer/kontakt/index.html'),
    ]),
    ('Medarbetare', 'medarbetare/index.html', []),
    ('Om oss', 'om-oss/index.html', [
        ('Vad är KBT?', 'om-oss/index.html#kbt'),
        ('Evidensbaserad praktik', 'om-oss/index.html#evidens'),
        ('Onlinesamtal', 'om-oss/index.html#online'),
        ('Vanliga frågor', 'om-oss/vanliga-fragor.html'),
    ]),
    ('Priser', 'priser/index.html', []),
    # Desktop bar omits Kontakt: the "Boka samtal" button already goes there.
    ('Kontakt', 'kontakt/index.html', [], False),
]

# --------------------------------------------------------------------------
# The team
# --------------------------------------------------------------------------
TEAM = [
    dict(slug='angeli-holmstedt', name='Angeli Holmstedt',
         role='Leg. psykolog · Leg. psykoterapeut · Handledare',
         note='Ångest, OCD och beroendeproblem, och stöd till dig som är anhörig. '
              'Utbildare i motiverande samtal och lärare i mindfulnessbaserade program.',
         lowres=True),
    dict(slug='thomas-alm', name='Thomas Alm',
         role='Leg. psykolog · Leg. psykoterapeut · Specialist i klinisk psykologi',
         note='Legitimerad psykolog sedan 1978. Missbruk och beroende, ångest och '
              'depression. Handledare inom psykiatri, primärvård och beroendevård.',
         lowres=True),
    dict(slug='karin-holmstrom', name='Karin Holmström',
         role='Leg. psykolog',
         note='Neuropsykiatriska utredningar av barn, ungdomar och vuxna. '
              'Femton år inom BUP. Arbetar även genom tolk.'),
    dict(slug='aksel-reppling', name='Aksel Reppling',
         role='Leg. psykolog',
         note='Oro och ångest, fobier och nedstämdhet. Parterapi och föräldrastöd. '
              'Tidigare BUP och Studenthälsan vid Uppsala universitet.'),
    dict(slug='elias-westerlund', name='Elias Westerlund',
         role='Leg. psykolog',
         note='Psykologisk utredning och bedömning, inklusive omprövning av '
              'tidigare ställda diagnoser.'),
    dict(slug='jens-karstrom', name='Jens Karström',
         role='Leg. psykolog · Leg. psykoterapeut · Specialist i klinisk psykologi',
         note='Trauma och traumabehandling. Prolonged exposure, schematerapi och ACT. '
              'Tar emot remisser från Regionen.'),
    dict(slug='barry-karlsson', name='Barry Karlsson',
         role='Leg. psykolog · Specialist i neuropsykologi',
         note='Kognitiva utredningar, utvecklingsbedömningar och neuropsykiatri. '
              'Forskar om förlust och komplicerad sorg.'),
]
BY_SLUG = {p['slug']: p for p in TEAM}


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def rel(base, href):
    """Resolve an app-root-relative href against a page's base prefix."""
    if href.startswith(('http', 'tel:', 'mailto:', '#')):
        return href
    return base + href


def pic_wide(base, slug, alt, sizes='100vw', cls='', eager=False):
    p = f'assets/img/{slug}.jpg'
    w, h = dim(p)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'''<picture{f' class="{cls}"' if cls else ''}>
        <source type="image/webp" sizes="{sizes}" srcset="{base}assets/img/{slug}-1000.webp 1000w, {base}assets/img/{slug}-1600.webp 1600w, {base}assets/img/{slug}-2400.webp 2400w">
        <img src="{base}assets/img/{slug}.jpg" alt="{H.escape(alt)}" width="{w}" height="{h}" decoding="async" {load}>
      </picture>'''


def pic_person(base, slug, alt, sizes='(min-width: 76rem) 20vw, (min-width: 56rem) 30vw, (min-width: 34rem) 45vw, 90vw', eager=False):
    p = f'assets/img/team/{slug}.jpg'
    w, h = dim(p)
    have = [n for n in (340, 600, 900)
            if os.path.exists(f'assets/img/team/{slug}-{n}.webp')]
    srcset = ', '.join(f'{base}assets/img/team/{slug}-{n}.webp {n}w' for n in have)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'''<picture>
        <source type="image/webp" sizes="{sizes}" srcset="{srcset}">
        <img src="{base}assets/img/team/{slug}.jpg" alt="{H.escape(alt)}" width="{w}" height="{h}" decoding="async" {load}>
      </picture>'''


def person_card(base, p, sizes=None):
    kw = {'sizes': sizes} if sizes else {}
    return f'''<a class="person" href="{base}medarbetare/{p['slug']}.html">
        <div class="person__media">{pic_person(base, p['slug'], f"{p['name']}, {p['role'].split(' · ')[0].lower()}", **kw)}</div>
        <div class="person__name">{p['name']}</div>
        <div class="person__role">{p['role']}</div>
        <p class="person__note">{p['note']}</p>
      </a>'''


def in_branch(href, current):
    """True when `current` is `href` or lives under it, so the top-level nav
    item stays marked while the reader is three levels down inside it."""
    if href == current:
        return True
    section = href.rsplit('/', 1)[0]
    return '/' in href and current.startswith(section + '/')


def nav_html(base, current):
    out = []
    for item in NAV:
        label, href = item[0], item[1]
        if len(item) > 3 and item[3] is False:
            continue
        cur = ' aria-current="page"' if in_branch(href, current) else ''
        out.append(f'<a href="{rel(base, href)}"{cur}>{label}</a>')
    return '\n        '.join(out)


def mobile_nav_html(base, current):
    out = []
    for item in NAV:
        label, href, kids = item[0], item[1], item[2]
        cur = ' aria-current="page"' if in_branch(href, current) else ''
        out.append(f'<li><a href="{rel(base, href)}"{cur}>{label}</a>')
        if kids:
            out.append('<ul class="mobile-nav__sub">')
            for klabel, khref in kids:
                out.append(f'<li><a href="{rel(base, khref)}">{klabel}</a></li>')
            out.append('</ul>')
        out.append('</li>')
    return '\n          '.join(out)


def icon(name, cls=''):
    """Inline reference into the page's SVG sprite."""
    c = f' {cls}' if cls else ''
    return (f'<svg class="icon{c}" aria-hidden="true" focusable="false">'
            f'<use href="#i-{name}"></use></svg>')


ARROW = icon('arrow-right')                       # trailing arrow on text links
ARROW_BTN = icon('arrow-right', 'btn__arrow')     # arrow inside a button
CHECK = icon('check')


def ticks(items, two=False, extra=''):
    """Checklist with real check icons rather than a CSS border triangle."""
    cls = 'ticks ticks--two' if two else 'ticks'
    style = f' style="{extra}"' if extra else ''
    lis = '\n        '.join(f'<li>{CHECK}<span>{t}</span></li>' for t in items)
    return f'<ul class="{cls}"{style}>\n        {lis}\n      </ul>'


HEAD_TPL = '''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="sv_SE">
<meta property="og:site_name" content="KBT-Konsulterna i Uppsala">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site}/assets/img/{ogimg}.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/brand/logo-mark.svg" type="image/svg+xml">
<link rel="icon" href="{base}assets/brand/icon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="{base}assets/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap">
<link rel="stylesheet" href="{base}assets/css/site.css">
<noscript><style>
  /* The burger needs JS to toggle. Without it, show the menu and hide the button
     so small screens still have navigation. The desktop rule uses !important,
     so this cannot leak above 66rem. */
  /* static, not the fixed overlay — with no JS there is no way to close it */
  .mobile-nav {{ display: block; position: static; overflow: visible; }}
  .burger {{ display: none; }}
</style></noscript>
{extra}</head>
<body>
<!-- Icon sprite, inlined once per page: a same-document fragment reference
     resolves over file:// too, where an external sprite file would be blocked.
     Stroke and size come from CSS, so every icon inherits currentColor and the
     font size of whatever it sits next to. -->
<svg class="sprite" aria-hidden="true" focusable="false" width="0" height="0"><defs>
  <symbol id="i-arrow-right" viewBox="0 0 24 24"><path d="M4 12h15"/><path d="M13 6l6 6-6 6"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path d="M4 12.5l5.5 5.5L20 6.5"/></symbol>
  <symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14"/><path d="M5 12h14"/></symbol>
  <symbol id="i-chevron-down" viewBox="0 0 24 24"><path d="M6 9.5l6 6 6-6"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path d="M3.5 7h17"/><path d="M3.5 12h17"/><path d="M3.5 17h17"/></symbol>
  <symbol id="i-close" viewBox="0 0 24 24"><path d="M6 6l12 12"/><path d="M18 6L6 18"/></symbol>
</defs></svg>

<a class="skip" href="#main">Hoppa till innehållet</a>

<header class="site-head">
  <div class="wrap site-head__inner">
    <a class="site-head__logo" href="{base}index.html">
      <img src="{base}assets/brand/logo.svg" alt="KBT-Konsulterna i Uppsala" width="{logo_w}" height="{logo_h}">
    </a>
    <nav class="nav" aria-label="Huvudmeny">
        {nav}
    </nav>
    <a class="head-akut" href="{base}akut-hjalp/index.html">Akut hjälp</a>
    <a class="head-tel" href="{tel_href}">{tel}</a>
    <a class="btn btn--primary" href="{base}kontakt/index.html">Boka samtal</a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Meny">
      <svg class="icon burger__bars" aria-hidden="true" focusable="false"><use href="#i-menu"></use></svg>
      <svg class="icon burger__x" aria-hidden="true" focusable="false"><use href="#i-close"></use></svg>
    </button>
  </div>
  <div class="mobile-nav" id="mnav" data-open="false">
    <div class="wrap">
      <ul>
          {mnav}
      </ul>
      <div class="mobile-nav__foot">
        <a class="btn btn--primary" href="{base}kontakt/index.html">Boka samtal</a>
        <a class="btn btn--ghost" href="{tel_href}">Ring {tel}</a>
        <a class="a-link" href="{base}akut-hjalp/index.html">Akut hjälp</a>
      </div>
    </div>
  </div>
</header>

<main id="main">
'''

FOOT_TPL = '''</main>

<footer class="site-foot">
  <div class="wrap">
    <div class="site-foot__grid">
      <div>
        <div class="site-foot__logo">
          <img src="{base}assets/brand/logo-white.svg" alt="KBT-Konsulterna i Uppsala" width="{logo_w}" height="{logo_h}">
        </div>
        <address class="site-foot__addr">
          {addr}<br>
          <a href="{tel_href}">{tel}</a><br>
          <a href="mailto:{mail}">{mail}</a>
        </address>
        <p class="site-foot__akut">
          Vid akuta besvär: ring <strong>112</strong>, eller se
          <a href="{base}akut-hjalp/index.html">akut hjälp</a>.
        </p>
      </div>
      <div>
        <h3>Det vi gör</h3>
        <ul>
          <li><a href="{base}vuxna/index.html">Vuxna</a></li>
          <li><a href="{base}barn-och-ungdom/index.html">Barn &amp; ungdom</a></li>
          <li><a href="{base}organisationer/index.html">För organisationer</a></li>
          <li><a href="{base}medarbetare/index.html">Medarbetare</a></li>
        </ul>
      </div>
      <div>
        <h3>Praktiskt</h3>
        <ul>
          <li><a href="{base}priser/index.html">Priser</a></li>
          <li><a href="{base}kontakt/index.html">Kontakt &amp; bokning</a></li>
          <li><a href="{base}om-oss/vanliga-fragor.html">Vanliga frågor</a></li>
          <li><a href="{base}om-oss/index.html#online">Onlinesamtal</a></li>
          <li><a href="{base}akut-hjalp/index.html">Akut hjälp</a></li>
        </ul>
      </div>
    </div>
    <div class="site-foot__base">
      <span>KBT Konsulterna, Evidensbaserad Praktik, Uppland AB</span>
      <a href="https://www.facebook.com/KBTKonsulterna/">Facebook</a>
      <span>Leg. psykologer · Tystnadsplikt</span>
    </div>
  </div>
</footer>

<script src="{base}assets/js/site.js" defer></script>
</body>
</html>
'''


def logo_size():
    """The intrinsic size of the logo SVG, so the <img> reserves the right box."""
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', open('assets/brand/logo.svg', encoding='utf-8').read())
    return m.group(1), m.group(2)
LOGO_W, LOGO_H = logo_size()


def page(path, title, desc, body, ogimg='hero-room', extra='', ogtitle=None):
    depth = path.count('/')
    base = '../' * depth
    current = path
    canonical = SITE + '/' + re.sub(r'index\.html$', '', path)
    robots = ('<meta name="robots" content="noindex, nofollow">\n'
              if PREVIEW else '')
    head = HEAD_TPL.format(
        robots=robots,
        title=H.escape(title), desc=H.escape(desc), canonical=canonical,
        ogtitle=H.escape(ogtitle or title), site=SITE, ogimg=ogimg, base=base,
        nav=nav_html(base, current), mnav=mobile_nav_html(base, current),
        tel=TEL, tel_href=TEL_HREF, extra=extra, logo_w=LOGO_W, logo_h=LOGO_H)
    foot = FOOT_TPL.format(base=base, addr=ADDR, tel=TEL, tel_href=TEL_HREF, mail=MAIL,
                           logo_w=LOGO_W, logo_h=LOGO_H)
    # A relative href ending in "/" resolves over HTTP but 404s over file://,
    # which this build promises works. Normalise them all rather than relying on
    # every hand-written link in the article copy remembering to say index.html.
    out_links = re.compile(r'(href=")((?!https?:|tel:|mailto:|#)[^"]*/)(")')
    body = out_links.sub(r'\1\2index.html\3', body)
    assert len(title) <= 70, f'{path}: title is {len(title)} chars — {title}'
    assert 50 <= len(desc) <= 165, f'{path}: description is {len(desc)} chars'
    out = head + body + foot
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    return len(out)


# ==========================================================================
# Shared content fragments
# ==========================================================================
def hero(base, slug, eyebrow, h1, lede, alt, full=False, crumb=None,
         actions=True, trust=False):
    kind = 'hero--full' if full else 'hero--page'
    crumb_html = f'<p class="crumb">{crumb}</p>' if crumb else ''
    trust_html = ('''<ul class="hero__trust">
        <li>Leg. psykologer</li>
        <li>Tystnadsplikt</li>
        <li>Mottagning i centrala Uppsala</li>
        <li>Videosamtal i hela Sverige</li>
      </ul>''' if trust else '')
    act = f'''<div class="actions">
          <a class="btn btn--on-dark" href="{base}kontakt/index.html">Boka samtal {ARROW_BTN}</a>
          <a class="hero__tel" href="{TEL_HREF}">eller ring {TEL}</a>
        </div>''' if actions else ''
    return f'''<section class="hero {kind}">
  <div class="hero__media">{pic_wide(base, slug, alt, eager=True)}</div>
  <div class="hero__scrim"></div>
  <div class="wrap hero__inner">
    <div class="hero__body">
      {crumb_html}
      <p class="hero__eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="hero__lede">{lede}</p>
      {act}
      {trust_html}
    </div>
  </div>
</section>
'''


def cta_band(base, heading='Ta första steget när du är klar för det.',
             text='Skriv eller ring. Vi hör av oss så snart vi kan, och du '
                  'behöver inte veta på förhand vad du vill ha hjälp med.'):
    return f'''<section class="bleed">
  <div class="bleed__media">{pic_wide(base, 'samtal', 'Två personer sitter mitt emot varandra med en kopp kaffe var')}</div>
  <div class="bleed__scrim"></div>
  <div class="wrap bleed__inner">
    <div class="prose--wide">
      <h2 data-reveal>{heading}</h2>
      <p class="hero__lede" style="margin-top:1.2rem">{text}</p>
      <div class="actions" style="margin-top:2rem">
        <a class="btn btn--on-dark" href="{base}kontakt/index.html">Boka samtal {ARROW_BTN}</a>
        <a class="hero__tel" href="{TEL_HREF}">eller ring {TEL}</a>
      </div>
    </div>
  </div>
</section>
'''


def marks_band(base):
    return f'''<section class="band band--tight">
  <div class="wrap">
    <p class="eyebrow">Legitimation och medlemskap</p>
    <ul class="marks">
      <li><img src="{base}assets/brand/socialstyrelsen.png" alt="Socialstyrelsen" width="280" height="58" loading="lazy"></li>
      <li><img src="{base}assets/brand/psykologforbundet.png" alt="Sveriges Psykologförbund" width="360" height="35" loading="lazy"></li>
      <li><img class="marks__tall" src="{base}assets/brand/mint.png" alt="MINT — Motivational Interviewing Network of Trainers" width="313" height="135" loading="lazy"></li>
      <li><img class="marks__tall" src="{base}assets/brand/btf.png" alt="Beteendeterapeutiska föreningen" width="360" height="129" loading="lazy"></li>
    </ul>
  </div>
</section>
'''


def akut_strip(base):
    return f'''<section class="band band--tight akut">
  <div class="wrap split">
    <div><p class="eyebrow">Akut hjälp</p></div>
    <div class="prose--wide">
      <p style="margin-bottom:0.8rem"><strong>Behöver du hjälp direkt?</strong> Vi är en
      mottagning med bokade tider och kan inte ta emot akut. Ring <strong>112</strong> vid fara
      för liv. Du kan också ringa MIND Stödlinje på <strong>90 101</strong>, eller söka
      psykakuten där du bor.</p>
      <p style="margin-bottom:0"><a class="a-link" href="{base}akut-hjalp/index.html">Se var du kan få akut hjälp {ARROW}</a></p>
    </div>
  </div>
</section>
'''


PROCESS_STEPS = [
    ('Första kontakten',
     'Du skriver eller ringer. Vi hör av oss så snart vi kan och bokar en tid. '
     'Du behöver inte ha en diagnos eller veta vad problemet heter.'),
    ('Gemensam bedömning',
     'Ett till tre samtal där vi tillsammans tar reda på vad du behöver hjälp med '
     '— och om du känner dig bekväm med oss.'),
    ('En plan',
     'Vi formulerar mål utifrån vad som är viktigt för dig, och kommer överens om '
     'metod och hur många samtal det troligen handlar om.'),
    ('Behandling och avstämning',
     'Vi arbetar mot målen och stämmer av regelbundet att behandlingen går i rätt '
     'riktning och att vi använder tiden väl.'),
]


def process_band(base, dark=True):
    items = '\n      '.join(
        f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in PROCESS_STEPS)
    cls = 'band band--deep' if dark else 'band band--hi'
    return f'''<section class="{cls}">
  <div class="wrap">
    <p class="eyebrow">Så går det till</p>
    <h2 data-reveal style="max-width:32rem;margin-bottom:clamp(2.5rem,5vw,4rem)">Fyra steg, och du bestämmer takten.</h2>
    <ol class="steps">
      {items}
    </ol>
  </div>
</section>
'''


def price_band(base, dark=False):
    cls = 'band band--sand' if not dark else 'band band--deep'
    return f'''<section class="{cls}">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Priser</p>
      <h2 data-reveal style="font-size:var(--step-2)">Vad det kostar, utan att du behöver fråga.</h2>
    </div>
    <div>
      <div class="prices">
        <div>
          <p class="price__label">Enskilt samtal</p>
          <p class="price__fig">1 500 kr <span class="price__unit">/ 45 min</span></p>
        </div>
        <div>
          <p class="price__label">Parterapi</p>
          <p class="price__fig">2 400 kr <span class="price__unit">/ 60 min</span></p>
          <p class="price__note">1 800 kr / 45 min. Ofta behövs minst 60 minuter,
          eller 2 × 45 minuter per besök.</p>
        </div>
      </div>
      <p style="margin-top:2rem;margin-bottom:0.6rem">Gäller privat finansierad terapi och
      konsultation. Moms tillkommer om arbetsgivare, försäkringsbolag eller socialtjänst
      betalar. Avbokning senare än 24 timmar före besöket debiteras i sin helhet.</p>
      <p style="margin-bottom:0"><a class="a-link" href="{base}priser/index.html">Alla priser och betalningsvillkor {ARROW}</a></p>
    </div>
  </div>
</section>
'''


# ==========================================================================
# Home
# ==========================================================================
ROUTER = [
    # Each line goes to the page that actually answers it, not to an anchor on a
    # hub the reader then has to scan. That was the whole point of the router.
    ('Jag sover inte om nätterna.', 'Sömnproblem', 'vuxna/behandling/somn/'),
    ('Jag orkar ingenting längre.', 'Stress &amp; utmattning', 'vuxna/behandling/stress-utmattning/'),
    ('Jag kan inte sluta oroa mig.', 'Oro &amp; ångest', 'vuxna/behandling/oro-angest/'),
    ('Mitt barn vägrar gå till skolan.', 'Barn &amp; ungdom', 'barn-och-ungdom/behandling/oro-angest/'),
    ('Jag dricker mer än jag vill.', 'Skadligt bruk', 'vuxna/beroende/'),
    ('Jag tror att jag har adhd eller autism.', 'Utredning', 'vuxna/utredning/'),
    ('Vi bråkar om samma sak, hela tiden.', 'Parterapi', 'vuxna/parterapi/'),
    ('Jag kan inte sluta tänka på det som hände.', 'Trauma &amp; ptsd', 'vuxna/behandling/trauma-ptsd/'),
    ('Jag vet inte var jag ska börja.', 'Hör av dig ändå', 'kontakt/index.html'),
]

HOME_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":["MedicalBusiness","Organization"],
"name":"KBT-Konsulterna i Uppsala",
"legalName":"KBT Konsulterna, Evidensbaserad Praktik, Uppland AB",
"url":"https://kbt-konsulterna.se","email":"kontakt@kbt-konsulterna.se",
"telephone":"+46181040 44",
"address":{"@type":"PostalAddress","streetAddress":"G\\u00e5rdshuset, Slottsk\\u00e4llan, Sjukhusv\\u00e4gen 3",
"addressLocality":"Uppsala","postalCode":"753 09","addressRegion":"Uppsala","addressCountry":"SE"},
"geo":{"@type":"GeoCoordinates","latitude":59.8536563,"longitude":17.6384567},
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
"dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
"opens":"09:00","closes":"17:00"}],
"sameAs":["https://www.facebook.com/KBTKonsulterna/"],
"medicalSpecialty":"Psychiatric"}
</script>
'''


def build_home():
    b = ''
    router = '\n      '.join(
        f'''<li><a class="router__row" href="{to_href(b, href)}">
        <span class="router__say">{say}</span>
        <span class="router__to">{to}{ARROW}</span>
      </a></li>''' for say, to, href in ROUTER)

    doors = [
        ('vuxna', 'Vuxna', 'Från 18 år', 'vuxna/index.html',
         'Terapi, parterapi, utredning och behandling vid skadligt bruk. '
         'För dig som är över 18.',
         'Ett ljust rum med en soffa och en fåtölj'),
        ('barn', 'Barn &amp; ungdom', 'Upp till 18 år', 'barn-och-ungdom/index.html',
         'Behandling och utredning för barn och unga — och stöd till dig som är '
         'förälder, lärare eller socialsekreterare.',
         'Ett barn som leker i snön'),
        ('foretag', 'För organisationer', 'Uppdrag &amp; utbildning',
         'organisationer/index.html',
         'Handledning, coaching, föreläsningar och utbildning för arbetsgivare, '
         'skola, vård och socialtjänst.',
         'Ett tomt, ljust mötesrum'),
    ]
    doors_html = '\n      '.join(
        f'''<a class="door" href="{b}{href}" data-reveal>
        <div class="door__media">
          {pic_wide(b, slug, alt, sizes='(min-width: 52rem) 33vw, 92vw')}
          <div class="door__scrim"></div>
          <div class="door__label">
            <span class="door__kicker">{kicker}</span>
            <h3 class="door__title">{title}</h3>
          </div>
        </div>
        <p>{text}</p>
        <span class="door__more">Läs mer{ARROW}</span>
      </a>''' for slug, title, kicker, href, text, alt in doors)

    team_html = '\n      '.join(person_card(b, p) for p in TEAM)

    body = f'''
{hero(b, 'hero-room',
      'Privat psykologmottagning i Uppsala',
      'Vi kan kognitiv beteendeterapi',
      'Sju legitimerade psykologer och psykoterapeuter i Gårdshuset vid '
      'Slottskällan, tio minuter från Uppsala C. Vi tar emot på mottagningen '
      'och online i hela Sverige.',
      'Ett varmt, ljust rum med en fåtölj vid ett stort fönster',
      full=True, trust=True)}

<section class="band">
  <div class="wrap">
    <p class="eyebrow">Medarbetare</p>
    <div class="split" style="margin-bottom:clamp(2.5rem,5vw,3.5rem)">
      <div></div>
      <div class="prose--wide">
        <h2 data-reveal style="margin-bottom:1.1rem">Hos oss väljer du en person, inte en mottagning.</h2>
        <p style="margin-bottom:0">Läs om var och en av oss och hör av dig direkt till den
        du tror passar dig. Är du osäker hjälper vi dig vidare.</p>
      </div>
    </div>
    <div class="team team--seven">
      {team_html}
    </div>
    <p style="margin-top:clamp(2.5rem,5vw,3.5rem);margin-bottom:0"><a class="a-link" href="{b}medarbetare/index.html">Osäker på vem du ska vända dig till? Se vem som arbetar med vad {ARROW}</a></p>
  </div>
</section>

<section class="band band--hi">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Vilka är vi?</p>
    </div>
    <div class="prose prose--wide">
      <h2 data-reveal style="margin-bottom:1.4rem">Legitimerade psykologer med lång och bred erfarenhet.</h2>
      <p>KBT-Konsulterna är en privat psykologmottagning i centrala Uppsala. Vi är
      legitimerade psykologer, legitimerade psykoterapeuter och specialister i kognitiv
      beteendeterapi. Flera av oss har arbetat inom psykiatrin, BUP, primärvården och
      habiliteringen, och undervisar eller handleder vid Uppsala universitet.</p>
      <p>Vi levererar en gedigen kompetens förpackad i ett varmt och professionellt
      bemötande. Varmt välkommen till oss.</p>
      {ticks(['Terapi för barn, ungdomar, vuxna och par', 'Neuropsykiatriska utredningar i alla åldrar', 'Bedömning och behandling vid skadligt bruk', 'Stöd till föräldrar och anhöriga', 'Uppdrag för företag och offentlig verksamhet', 'Handledning, kurser och utbildningar'], two=True, extra='margin-top:2rem')}
      <p style="margin-top:2rem;margin-bottom:0"><a class="a-link" href="{b}om-oss/index.html">Mer om oss och hur vi arbetar {ARROW}</a></p>
    </div>
  </div>
</section>

<section class="bleed">
  <div class="bleed__media">{pic_wide(b, 'band-forest', 'Solljus genom trädstammar i en skog')}</div>
  <div class="bleed__scrim"></div>
  <div class="wrap bleed__inner">
    <blockquote class="pull" data-reveal>
      &rdquo;Du behöver inte ha någon diagnos för att träffa mig, utan jag träffar även
      dig som befinner dig i en pågående livskris eller bara känner att du kört fast och
      hamnat i en återvändsgränd.&rdquo;
      <cite>Jens Karström, leg. psykolog och leg. psykoterapeut</cite>
    </blockquote>
  </div>
</section>

<!-- Three doors: title set on the photograph, middle door dropped a step. -->
<section class="band">
  <div class="wrap">
    <div class="split" style="margin-bottom:clamp(2.5rem,5vw,3.5rem)">
      <div>
        <p class="eyebrow">Tre ingångar</p>
      </div>
      <div class="prose--wide">
        <h2 data-reveal style="margin-bottom:1.1rem">Vem söker du hjälp för?</h2>
        <p style="margin-bottom:0">Välj den ingång som passar dig bäst. Vet du inte
        riktigt vad det handlar om? Säg det med dina egna ord här nedanför.</p>
      </div>
    </div>
    <div class="doors">
      {doors_html}
    </div>
  </div>
</section>

<!-- Signature element: the plain-language router. -->
<section class="band band--hi">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Var ska jag börja?</p>
      <p style="font-size:1rem;color:var(--muted);max-width:15rem">Säg det med dina
      egna ord. Vi visar dig vidare.</p>
    </div>
    <div>
      <ul class="router">
      {router}
      </ul>
    </div>
  </div>
</section>

{process_band(b)}
{price_band(b)}

<section class="band band--hi">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Praktiskt</p>
      <h2 data-reveal style="font-size:var(--step-2)">Var vi finns och hur vi ses.</h2>
    </div>
    <div>
      <dl class="facts">
        <div>
          <dt>Mottagning</dt>
          <dd>{ADDR}<br><a class="a-link" href="{MAPS}">Visa på karta {ARROW}</a></dd>
        </div>
        <div>
          <dt>Hitta hit</dt>
          <dd>I hjärtat av Uppsala, tio minuter från Centralstationen, i en vacker miljö
          i Gårdshuset vid Slottskällan.</dd>
        </div>
        <div>
          <dt>Öppettider</dt>
          <dd>Måndag–fredag 09–17. Vi kan erbjuda kvällstider ett par gånger per vecka,
          både digitalt och på mottagningen.</dd>
        </div>
        <div>
          <dt>Online</dt>
          <dd>Videosamtal i hela Sverige via Kaddio, med BankID och samma sekretess som
          på mottagningen. <a class="a-link" href="{b}om-oss/index.html#online">Läs mer</a></dd>
        </div>
        <div>
          <dt>Remiss och högkostnadsskydd</dt>
          <dd>Angeli Holmstedt och Jens Karström tar emot remisser från Region Uppsala.
          För övriga gäller privat taxa.</dd>
        </div>
        <div>
          <dt>Kontakt</dt>
          <dd><a href="{TEL_HREF}">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></dd>
        </div>
      </dl>
    </div>
  </div>
</section>

{cta_band(b)}
{marks_band(b)}
{akut_strip(b)}
'''
    return page('index.html',
                'KBT-Konsulterna – privat psykologmottagning i Uppsala',
                'Privat psykologmottagning i centrala Uppsala och online. Sju '
                'legitimerade psykologer. Terapi för barn, ungdomar, vuxna och par, '
                'utredning av adhd och autism.',
                body, ogimg='hero-room', extra=HOME_LD,
                ogtitle='KBT-Konsulterna – privat psykologmottagning i Uppsala')


# ==========================================================================
# Hub page scaffold
# ==========================================================================
def topics_grid(base, items, three=False):
    """Each item is (title, blurb) or (title, blurb, path). With a path the card
    becomes a link to that topic's own page — the cards used to be dead text,
    which is what made the topic layer unreachable."""
    cls = 'topics topics--three' if three else 'topics'
    out = []
    for it in items:
        t, d = it[0], it[1]
        href = it[2] if len(it) > 2 else None
        if href:
            out.append(f'<a class="topic topic--link" href="{to_href(base, href)}">'
                       f'<h3>{t}</h3><p>{d}</p>'
                       f'<span class="topic__go">Läs mer {ARROW}</span></a>')
        else:
            out.append(f'<div class="topic"><h3>{t}</h3><p>{d}</p></div>')
    inner = '\n      '.join(out)
    return f'<div class="{cls}">\n      {inner}\n    </div>'


def contents_list(base, items):
    """(label, target). A target with a slash is a page; otherwise an anchor on
    this page."""
    out = []
    for label, target in items:
        href = to_href(base, target) if '/' in target else f'#{target}'
        out.append(f'<li><a href="{href}"><span>{label}</span>{ARROW}</a></li>')
    inner = '\n      '.join(out)
    return f'<ul class="linklist linklist--two">\n      {inner}\n    </ul>'


def hub_section(anchor, eyebrow, heading, intro, content, tone='', more=None):
    """`more` is (base, path, label): the link through to this section's own
    page, so the hub summarises and the page carries the depth."""
    cls = f'band {tone}'.strip()
    more_html = ''
    if more:
        mbase, mpath, mlabel = more
        more_html = (f'\n      <p class="hub__more"><a class="a-link" '
                     f'href="{to_href(mbase, mpath)}">{mlabel} {ARROW}</a></p>')
    return f'''<section class="{cls} anchor" id="{anchor}">
  <div class="wrap split">
    <div><p class="eyebrow">{eyebrow}</p></div>
    <div>
      <h2 data-reveal style="max-width:26rem;margin-bottom:1.2rem">{heading}</h2>
      <div class="prose prose--wide" style="margin-bottom:clamp(2rem,4vw,3rem)">{intro}</div>
      {content}{more_html}
    </div>
  </div>
</section>
'''


def team_subset(base, slugs, eyebrow, heading, note):
    cards = '\n      '.join(
        person_card(base, BY_SLUG[s],
                    sizes='(min-width: 56rem) 25vw, (min-width: 34rem) 45vw, 90vw')
        for s in slugs)
    return f'''<section class="band band--hi">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <div class="split" style="margin-bottom:clamp(2.5rem,5vw,3.5rem)">
      <div></div>
      <div class="prose--wide">
        <h2 data-reveal style="margin-bottom:1.1rem">{heading}</h2>
        <p style="margin-bottom:0">{note}</p>
      </div>
    </div>
    <div class="team">
      {cards}
    </div>
    <p style="margin-top:2.5rem;margin-bottom:0"><a class="a-link" href="{base}medarbetare/index.html">Alla medarbetare {ARROW}</a></p>
  </div>
</section>
'''


# ==========================================================================
# Vuxna
# ==========================================================================
def build_vuxna():
    b = '../'
    behandling = topics_grid(b, [
        ('Oro och ångest',
         'Social ångest, panikångest, generaliserad ångest, tvångstankar och '
         'tvångshandlingar (OCD) samt fobier.', 'vuxna/behandling/oro-angest/'),
        ('Nedstämdhet och depression',
         'Från långvarig nedstämdhet till återkommande depressioner. Vi arbetar med '
         'beteendeaktivering, kognitiv terapi och återfallsprevention.',
         'vuxna/behandling/depression/'),
        ('Stress och utmattning',
         'När återhämtningen inte längre räcker till. Vi arbetar med belastning, '
         'gränser och en hållbar väg tillbaka.',
         'vuxna/behandling/stress-utmattning/'),
        ('Sömnproblem',
         'Svårt att somna, vakna mitt i natten eller sova utan att bli utvilad. '
         'KBT för insomni har starkt forskningsstöd.', 'vuxna/behandling/somn/'),
        ('Trauma och PTSD',
         'Bearbetning av svåra händelser med metoder som prolonged exposure (PE). '
         'Jens Karström har särskilt intresse för traumabehandling.',
         'vuxna/behandling/trauma-ptsd/'),
        ('Sorg',
         'Vid förlust och komplicerad sorg. Barry Karlsson forskar på området vid '
         'Uppsala universitet.', 'vuxna/behandling/sorg/'),
        ('Låg självkänsla',
         'Återkommande känslor av otillräcklighet, prestationskrav och svårt att stå '
         'upp för sig själv.', 'vuxna/behandling/sjalvkansla/'),
        ('Relationsproblem',
         'Återkommande konflikter, ensamhet i en relation, eller svårigheter som '
         'går igen från relation till relation.', 'vuxna/behandling/relationer/'),
        ('Fobier och flygfobi',
         'Specifika fobier — sprutor, blod, höjder, hissar, flygplan. '
         'Exponeringsbehandling har bland de bästa resultaten inom psykologin.',
         'vuxna/behandling/fobier/'),
        ('Neuropsykiatriska funktionsnedsättningar',
         'Behandling och anpassat stöd vid adhd och autism i vuxen ålder — med eller '
         'utan färdig diagnos.', 'vuxna/behandling/npf/'),
    ], three=True)

    utredning = topics_grid(b, [
        ('Utredning av adhd',
         'Psykologutredning med intervju, skattningsskalor och testning. Du får ett '
         'skriftligt utlåtande och konkreta rekommendationer.',
         'vuxna/utredning/adhd/'),
        ('Utredning av autism',
         'Bedömning av autismspektrumtillstånd hos vuxna, med samma noggranna '
         'återkoppling och skriftliga utlåtande.', 'vuxna/utredning/autism/'),
        ('Omprövning av diagnos',
         'Har du fått en diagnos som inte känns rätt, eller behöver den prövas på '
         'nytt? Elias Westerlund arbetar särskilt med omprövningar.',
         'vuxna/utredning/omprovning/'),
    ], three=True)

    body = f'''
{hero(b, 'vuxna', 'Vuxna',
      'Från psykisk ohälsa till ett bättre mående',
      'Terapi, parterapi, utredning och behandling vid skadligt bruk — hos '
      'legitimerade psykologer och psykoterapeuter med lång erfarenhet.',
      'Ett ljust rum med en soffa, en fåtölj och tegelvägg',
      crumb=f'<a href="{b}index.html">Hem</a><span>/</span>Vuxna')}

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Det här kan vi hjälpa med</p></div>
    <div>
      <div class="prose prose--wide" style="margin-bottom:clamp(2rem,4vw,3rem)">
        <p class="lede" style="margin-bottom:1.4rem">Att söka hjälp kan vara ett stort steg.
        Ofta finns det en längtan om att det ska ge en förändring — ett bättre mående, ett
        enklare liv.</p>
        <p>I många sammanhang finns idag en större öppenhet om psykisk ohälsa. Trots det
        upplever många en skam över att må psykiskt dåligt, att ha problem med sina barn, på
        arbetet eller med sin partner. Hos oss arbetar legitimerade psykologer och
        legitimerade psykoterapeuter med lång erfarenhet av de flesta problem vi människor
        kan drabbas av.</p>
        <p style="margin-bottom:0">Du behöver inte ha en diagnos, och du behöver inte veta
        vad problemet heter för att höra av dig.</p>
      </div>
      {contents_list(b, [
        ('Psykologisk behandling', 'vuxna/behandling/'),
        ('Parterapi', 'vuxna/parterapi/'),
        ('Skadligt bruk &amp; beroende', 'vuxna/beroende/'),
        ('Utredning &amp; bedömning', 'vuxna/utredning/'),
        ('Psykiatrisk bedömning', 'vuxna/psykiatri/'),
      ])}
    </div>
  </div>
</section>

{hub_section('behandling', 'Psykologisk behandling',
             'Samtalsterapi och KBT för vuxna.',
             '<p style="margin-bottom:0">Vi börjar med en gemensam bedömning och formulerar '
             'därefter en plan utifrån dina mål och värderingar. För det mesta arbetar vi '
             '&rdquo;här och nu&rdquo;, men om din tidigare historia påverkar hur du mår i dag '
             'finns även den med i samtalen.</p>',
             behandling, tone='band--hi',
             more=(b, 'vuxna/behandling/', 'Om psykologisk behandling'))}

{hub_section('parterapi', 'Parterapi',
             'När ni bråkar om samma sak, hela tiden.',
             '<p>Vi arbetar bland annat med IBCT (Integrative Behavioral Couple Therapy), '
             'en KBT-baserad parterapi med gott forskningsstöd. Fokus ligger på hur ni '
             'samtalar med varandra, vad konflikterna egentligen handlar om, och vad ni '
             'vill med relationen.</p>'
             '<p style="margin-bottom:0">Parterapi bokas i 60-minuterspass, eller 2 × 45 '
             'minuter. Aksel Reppling tar emot par.</p>',
             f'<p style="margin-bottom:0"><a class="a-link" href="{b}priser/index.html">'
             f'Se pris för parterapi {ARROW}</a></p>',
             more=(b, 'vuxna/parterapi/', 'Om parterapi och IBCT'))}

{hub_section('beroende', 'Skadligt bruk &amp; beroende',
             'Alkohol, läkemedel, droger och spel.',
             '<p>Många upptäcker att alkohol eller andra substanser har börjat ta en alltför '
             'stor plats i livet, och känner en längtan efter att förändra det. Vi arbetar med '
             'bedömning och behandling vid riskbruk, missbruk och beroende — inklusive '
             'spelberoende — med metoder som återfallsprevention, motiverande samtal och '
             'MBRP (mindfulnessbaserad återfallsprevention).</p>'
             '<p style="margin-bottom:0">Du är också välkommen om du är <strong>anhörig</strong> '
             'till någon som använder alkohol eller droger på ett sätt som skapar problem. '
             'Thomas Alm och Angeli Holmstedt har båda lång erfarenhet inom beroendeområdet.</p>',
             '', tone='band--hi',
             more=(b, 'vuxna/beroende/', 'Om skadligt bruk och beroende'))}

{hub_section('utredning', 'Utredning &amp; bedömning',
             'Neuropsykiatrisk utredning för vuxna.',
             '<p style="margin-bottom:0">När du kommer till oss för en utredning har vi alltid '
             'ett första bedömningssamtal där vi tillsammans går igenom dina behov, problem och '
             'förväntningar. Därefter formulerar vi en frågeställning och gör upp en plan. När '
             'utredningen är klar går vi igenom resultatet tillsammans och du får ett skriftligt '
             'utlåtande. Vi lägger stor vikt vid att identifiera dina styrkor och svårigheter, '
             'så att rekommendationerna blir konkreta — oavsett vad utredningen visar.</p>',
             utredning,
             more=(b, 'vuxna/utredning/', 'Om utredning och bedömning'))}

{hub_section('psykiatri', 'Psykiatrisk bedömning',
             'Konsultation med specialistläkare.',
             '<p style="margin-bottom:0">Vi samarbetar med en erfaren specialistläkare i '
             'psykiatri och kan erbjuda psykiatrisk bedömning och behandling som komplement '
             'till psykologisk behandling. Kontakta oss för att höra hur det kan se ut i '
             'ditt fall.</p>',
             '', tone='band--hi',
             more=(b, 'vuxna/psykiatri/', 'Om psykiatrisk bedömning'))}

{process_band(b)}
{team_subset(b, ['angeli-holmstedt', 'thomas-alm', 'jens-karstrom', 'aksel-reppling'],
             'Vem träffar du?',
             'Fyra av oss arbetar främst med vuxna.',
             'Elias Westerlund och Barry Karlsson arbetar med utredning och bedömning, '
             'och Karin Holmström med barn och unga.')}
{price_band(b)}
{cta_band(b)}
{akut_strip(b)}
'''
    return page('vuxna/index.html',
                'Psykolog för vuxna i Uppsala – terapi och utredning | KBT-Konsulterna',
                'KBT för vuxna i Uppsala och online. Behandling vid ångest, depression, '
                'stress, sömnproblem och trauma. Parterapi och utredning av adhd '
                'och autism.',
                body, ogimg='vuxna')


# ==========================================================================
# Barn & ungdom
# ==========================================================================
def build_barn():
    b = '../'
    behandling = topics_grid(b, [
        ('Oro, ängslan och ångest',
         'Oro som tar över vardagen, skolvägran, separationsångest och social ångest.',
         'barn-och-ungdom/behandling/oro-angest/'),
        ('Nedstämdhet och depression',
         'När barnet eller ungdomen drar sig undan, tappar intresse eller blir '
         'irriterad och ledsen utan tydlig anledning.',
         'barn-och-ungdom/behandling/depression/'),
        ('Tvångstankar och tvångshandlingar',
         'OCD hos barn och unga, där behandlingen görs tillsammans med föräldrarna.',
         'barn-och-ungdom/behandling/ocd/'),
        ('Sömnproblem',
         'Svårt att somna, nattliga uppvaknanden och dygnsrytm som glidit.',
         'barn-och-ungdom/behandling/somn/'),
        ('Beteenden som utmanar',
         'Utbrott, trots och aggressivitet — där vi arbetar lika mycket med de vuxna '
         'runt barnet som med barnet självt.',
         'barn-och-ungdom/behandling/beteende/'),
    ], three=True)

    utredning = topics_grid(b, [
        ('Utredning av adhd',
         'Neuropsykiatrisk utredning av barn och ungdomar, i nära samarbete med '
         'föräldrar och skola.', 'barn-och-ungdom/utredning/adhd/'),
        ('Utredning av autism',
         'Bedömning av autismspektrumtillstånd. Karin Holmström har lett ett '
         'specialiserat utredningsteam inom området.',
         'barn-och-ungdom/utredning/autism/'),
        ('Intellektuell funktion',
         'Psykologutredning av intellektuell funktion, ofta som underlag för rätt '
         'stöd i skolan.', 'barn-och-ungdom/utredning/intellektuell-funktion/'),
    ], three=True)

    stod = topics_grid(b, [
        ('Föräldrar och anhöriga',
         'Stöd och rådgivning när du känner dig osäker i föräldraskapet, eller när '
         'ditt barn inte kan eller vill gå i behandling själv.',
         'barn-och-ungdom/stod/foraldrar/'),
        ('Skola och elevhälsa',
         'Konsultation, handledning och skolpsykologiska utredningar. Vi arbetar på '
         'konsultbasis i elevhälsoteam från förskoleklass till årskurs 9.',
         'barn-och-ungdom/stod/skola/'),
        ('HVB-hem och familjehem',
         'Handledning till personalgrupper och konsultation i enskilda ärenden.',
         'barn-och-ungdom/stod/hvb-familjehem/'),
        ('Socialtjänst',
         'Utredning, bedömning och handledning som underlag för era insatser.',
         'barn-och-ungdom/stod/socialtjanst/'),
    ])

    body = f'''
{hero(b, 'barn', 'Barn &amp; ungdom',
      'Vi finns med under hela resan',
      'Behandling och utredning för barn och unga — och stöd till föräldrar, '
      'skola, HVB-hem och socialtjänst.',
      'Ett barn som leker i snön en vinterdag',
      crumb=f'<a href="{b}index.html">Hem</a><span>/</span>Barn &amp; ungdom')}

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Det här kan vi hjälpa med</p></div>
    <div>
      <div class="prose prose--wide" style="margin-bottom:clamp(2rem,4vw,3rem)">
        <p class="lede" style="margin-bottom:1.4rem">Det är svårt att veta när det är vanliga
        problem, och när det är något barnet behöver hjälp med.</p>
        <p>Psykisk ohälsa hos barn och ungdomar kan ta sig många uttryck. Barnet kan dra sig
        undan, sluta gå till skolan, tillbringa alltför mycket tid med dator eller mobil, vara
        oroligt, argt och irriterat, få utbrott eller gråta, ha svårt att sova. Även alkohol och
        droger kan komma in i en ung människas liv, med allvarliga konsekvenser.</p>
        <p style="margin-bottom:0">Våra psykologer har lång erfarenhet från BUP, skolor och
        behandlingshem — och av att arbeta med familjen och nätverket runt barnet, inte bara
        med barnet självt.</p>
      </div>
      {contents_list(b, [
        ('Psykologisk behandling', 'barn-och-ungdom/behandling/'),
        ('Utredning &amp; bedömning', 'barn-och-ungdom/utredning/'),
        ('Stöd till vuxna runt barnet', 'barn-och-ungdom/stod/'),
      ])}
    </div>
  </div>
</section>

{hub_section('behandling', 'Psykologisk behandling',
             'KBT för barn och ungdomar.',
             '<p style="margin-bottom:0">Du som förälder är en självklar del av '
             'behandlingsprocessen, antingen genom kontinuerligt föräldrastöd eller '
             'regelbundna avstämningar. Möten och samordning med skolan kan också vara '
             'en viktig pusselbit.</p>',
             behandling, tone='band--hi',
             more=(b, 'barn-och-ungdom/behandling/', 'Om psykologisk behandling'))}

{hub_section('utredning', 'Utredning &amp; bedömning',
             'Neuropsykiatrisk utredning av barn och unga.',
             '<p style="margin-bottom:0">Vi har lång erfarenhet av och hög kompetens för att '
             'utreda barn i alla åldrar. Utredningen börjar med ett bedömningssamtal, och '
             'avslutas med en genomgång av resultatet och ett skriftligt utlåtande med '
             'konkreta rekommendationer till hem och skola.</p>',
             utredning,
             more=(b, 'barn-och-ungdom/utredning/', 'Om utredning av barn och unga'))}

{hub_section('stod', 'Råd, stöd och handledning',
             'Stöd till de vuxna runt barnet.',
             '<p style="margin-bottom:0">Ofta är det de vuxna i barnets närhet som kan skapa '
             'störst förändring. Vi arbetar med föräldrar, skolpersonal, behandlingshem och '
             'socialtjänst — genom rådgivning, handledning och utbildning.</p>',
             stod, tone='band--hi',
             more=(b, 'barn-och-ungdom/stod/', 'Om råd, stöd och handledning'))}

<section class="bleed">
  <div class="bleed__media">{pic_wide(b, 'barn-play', 'Ett barn som bygger med klossar')}</div>
  <div class="bleed__scrim"></div>
  <div class="wrap bleed__inner">
    <blockquote class="pull" data-reveal>
      &rdquo;Föräldrastöd brukar vara extra hjälpsamt när ditt barn inte kan eller vill gå
      i psykologisk behandling.&rdquo;
      <cite>Jens Karström, leg. psykolog och leg. psykoterapeut</cite>
    </blockquote>
  </div>
</section>

{team_subset(b, ['karin-holmstrom', 'aksel-reppling', 'jens-karstrom', 'elias-westerlund'],
             'Vem träffar du?',
             'Fyra av oss arbetar med barn, unga och deras nätverk.',
             'Karin Holmström har femton år inom BUP och arbetar även genom tolk. '
             'Aksel Reppling och Jens Karström kommer också från BUP.')}
{price_band(b)}
{cta_band(b, heading='Osäker på om det är dags att söka hjälp?',
          text='Hör av dig ändå. Ett första samtal kostar inget mer än tiden det tar, '
               'och vi kan hjälpa dig att bedöma vad som behövs.')}
{akut_strip(b)}
'''
    return page('barn-och-ungdom/index.html',
                'Psykolog för barn och ungdomar i Uppsala | KBT-Konsulterna',
                'KBT för barn och ungdomar i Uppsala. Behandling vid oro, ångest, '
                'nedstämdhet och OCD, utredning av adhd och autism, samt stöd till '
                'föräldrar och skola.',
                body, ogimg='barn')


# ==========================================================================
# Organisationer
# ==========================================================================
def build_org():
    b = '../'
    handledning = topics_grid(b, [
        ('Verksamhetshandledning',
         'Regelbunden handledning för arbetsgrupper inom vård, skola, socialtjänst '
         'och behandlingshem — med fokus på ärenden, metod och arbetsmiljö.'),
        ('Utbildningshandledning',
         'Handledning för studenter på KBT-utbildningar och för psykologer under '
         'specialisering.'),
        ('Coaching och chefsstöd',
         'Individuell coaching för chefer och medarbetare, och stöd i svåra '
         'personalärenden.'),
    ], three=True)

    utbildning = topics_grid(b, [
        ('Föreläsningar och workshops',
         'Om stress och utmattning, oro och ångest, depression, trauma, '
         'beroendeproblematik och neuropsykiatri.'),
        ('Motiverande samtal (MI)',
         'Utbildning i MI på grund- och fördjupningsnivå. Angeli Holmstedt är '
         'medlem i MINT, det internationella nätverket av MI-utbildare.'),
        ('Mindfulnessbaserade program',
         'MBSR, MBCT och MBRP — som personalutbildning eller som insats för en '
         'grupp medarbetare.'),
    ], three=True)

    body = f'''
{hero(b, 'foretag', 'För organisationer',
      'Kompetens att låna in',
      'Handledning, coaching, föreläsningar och utbildning för arbetsgivare, '
      'skola, vård och socialtjänst. På plats hos er, hos oss eller online.',
      'Ett tomt, ljust mötesrum med stora fönster',
      crumb=f'<a href="{b}index.html">Hem</a><span>/</span>För organisationer')}

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Vilka är vi?</p></div>
    <div>
      <div class="prose prose--wide" style="margin-bottom:clamp(2rem,4vw,3rem)">
        <p class="lede" style="margin-bottom:1.4rem">En erfaren och kvalificerad grupp
        legitimerade psykologer och psykoterapeuter, vana vid uppdrag i komplexa
        verksamheter.</p>
        <p>Flera av oss har arbetat inom psykiatrin, BUP, primärvården, habiliteringen och
        universitetet. Vi har varit konsulter åt, utbildat och handlett verksamheter som
        BUP, primärvården, psykiatrin, behandlingshem och HVB, universitet, socialtjänst,
        Statens institutionsstyrelse, skolor, resurs- och specialskolor samt
        företagshälsovård.</p>
        <p style="margin-bottom:0">Vår bas är i centrala Uppsala. Vi tar emot här, arbetar
        online och kommer ut till arbetsgivare runt om i landet.</p>
      </div>
      {contents_list(b, [
        ('Handledning &amp; coaching', 'organisationer/handledning/'),
        ('Föreläsningar &amp; utbildning', 'organisationer/utbildning/'),
        ('Rehabilitering', 'organisationer/rehabilitering/'),
        ('Skadligt bruk på arbetsplatsen', 'organisationer/skadligt-bruk/'),
        ('Kontakt för uppdrag', 'organisationer/kontakt/'),
      ])}
    </div>
  </div>
</section>

{hub_section('handledning', 'Handledning &amp; coaching',
             'Handledning för personalgrupper och studenter.',
             '<p style="margin-bottom:0">Tre av oss är utbildade handledare med lång '
             'erfarenhet från psykiatri, primärvård, beroendevård, skola och företag. '
             'Barry Karlsson handleder med särskilt fokus på LSS, neuropsykiatri och '
             'kollegialt stöd.</p>',
             handledning, tone='band--hi',
             more=(b, 'organisationer/handledning/', 'Om handledning och coaching'))}

{hub_section('utbildning', 'Föreläsningar &amp; utbildning',
             'Utbildning i KBT, MI och mindfulness.',
             '<p style="margin-bottom:0">Vi håller föreläsningar, workshops och längre '
             'utbildningar, anpassade efter verksamhetens behov. Flera av oss undervisar '
             'eller har undervisat vid Uppsala universitet.</p>',
             utbildning,
             more=(b, 'organisationer/utbildning/', 'Om föreläsningar och utbildning'))}

{hub_section('rehabilitering', 'Rehabilitering',
             'Tillbaka till arbetet, hållbart.',
             '<p style="margin-bottom:0">Insatser vid stressrelaterad ohälsa och '
             'utmattning — bedömning, behandling och stöd i återgång till arbete, i '
             'samarbete med arbetsgivare och företagshälsovård. Vi arbetar med både '
             'individen och de förutsättningar som ska tas tillbaka till.</p>',
             '', tone='band--hi',
             more=(b, 'organisationer/rehabilitering/', 'Om rehabilitering'))}

{hub_section('skadligt-bruk', 'Skadligt bruk på arbetsplatsen',
             'Alkohol, läkemedel och spel i arbetslivet.',
             '<p style="margin-bottom:0">Bedömning och behandling vid riskbruk och '
             'beroende, och stöd till chefer som behöver hantera en oroande situation. '
             'Thomas Alm och Angeli Holmstedt har båda arbetat inom beroendeområdet i '
             'decennier, kliniskt och i forskning.</p>',
             '',
             more=(b, 'organisationer/skadligt-bruk/', 'Om skadligt bruk i arbetslivet'))}

<section class="band band--deep">
  <div class="wrap split">
    <div><p class="eyebrow">Kontakt för uppdrag</p></div>
    <div class="prose--wide">
      <h2 data-reveal style="margin-bottom:1.2rem">Berätta vad ni behöver.</h2>
      <p>Vi svarar på frågor om uppdrag, handledning, utbildning och samarbeten. Priser
      för handledning, utbildning och utredning lämnas på förfrågan.</p>
      <div class="actions" style="margin-top:2rem">
        <a class="btn btn--on-dark" href="{b}kontakt/index.html#foretag">Kontakta oss {ARROW_BTN}</a>
        <a class="hero__tel" href="{TEL_HREF}">eller ring {TEL}</a>
      </div>
    </div>
  </div>
</section>

{team_subset(b, ['angeli-holmstedt', 'thomas-alm', 'barry-karlsson'],
             'Handledare',
             'Tre utbildade handledare.',
             'Angeli Holmstedt är dessutom MI-utbildare via MINT och lärare i '
             'mindfulnessbaserade program.')}
{marks_band(b)}
'''
    return page('organisationer/index.html',
                'Handledning och utbildning för organisationer | KBT-Konsulterna',
                'Handledning, coaching, föreläsningar och utbildning i KBT, MI och '
                'mindfulness för arbetsgivare, skola, vård och socialtjänst.',
                body, ogimg='foretag')


# ==========================================================================
# Medarbetare — index
# ==========================================================================
ROUTING = [
    ('Oro, ångest, OCD, panik', ['angeli-holmstedt', 'aksel-reppling', 'jens-karstrom']),
    ('Nedstämdhet och depression', ['angeli-holmstedt', 'thomas-alm', 'aksel-reppling', 'jens-karstrom']),
    ('Trauma och PTSD', ['jens-karstrom', 'elias-westerlund']),
    ('Stress och utmattning', ['angeli-holmstedt', 'jens-karstrom']),
    ('Skadligt bruk, beroende, spel', ['thomas-alm', 'angeli-holmstedt']),
    ('Anhörig till någon med beroende', ['angeli-holmstedt']),
    ('Parterapi', ['aksel-reppling']),
    ('Sorg och förlust', ['barry-karlsson']),
    ('Barn och unga — behandling', ['aksel-reppling', 'jens-karstrom', 'karin-holmstrom']),
    ('Barn och unga — utredning', ['karin-holmstrom']),
    ('Vuxna — adhd- och autismutredning', ['elias-westerlund', 'barry-karlsson']),
    ('Omprövning av diagnos', ['elias-westerlund']),
    ('Kognitiv utredning, hjärnskada, LSS', ['barry-karlsson']),
    ('Föräldrastöd och skola', ['karin-holmstrom', 'aksel-reppling', 'jens-karstrom']),
    ('Handledning och utbildning', ['angeli-holmstedt', 'thomas-alm', 'barry-karlsson']),
    ('Remiss från Regionen', ['angeli-holmstedt', 'jens-karstrom']),
]


def build_medarbetare():
    b = '../'
    cards = '\n      '.join(person_card(b, p) for p in TEAM)
    rows = '\n        '.join(
        f'''<div>
          <dt>{need}</dt>
          <dd>{', '.join(f'<a class="a-link" href="{b}medarbetare/{s}.html">{BY_SLUG[s]["name"]}</a>' for s in slugs)}</dd>
        </div>''' for need, slugs in ROUTING)

    body = f'''
{hero(b, 'stillhet', 'Medarbetare',
      'Sju personer, inte en mottagning',
      'Alla legitimerade psykologer. Flera är dessutom legitimerade '
      'psykoterapeuter, specialister och handledare. Läs om var och en och '
      'hör av dig direkt.',
      'Ett fönster med en krukväxt i motljus',
      crumb=f'<a href="{b}index.html">Hem</a><span>/</span>Medarbetare')}

<section class="band">
  <div class="wrap">
    <div class="team team--seven">
      {cards}
    </div>
  </div>
</section>

<section class="band band--hi">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Vem gör vad</p>
      <p style="font-size:1rem;color:var(--muted);max-width:15rem">Är du osäker? Skriv till
      <a class="a-link" href="mailto:{MAIL}">{MAIL}</a> och vi hjälper dig vidare.</p>
    </div>
    <div>
      <h2 data-reveal style="max-width:26rem;margin-bottom:clamp(2rem,4vw,2.75rem)">Hitta rätt person direkt.</h2>
      <dl class="facts">
        {rows}
      </dl>
    </div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap split">
    <div><p class="eyebrow">Så är vi organiserade</p></div>
    <div class="prose--wide">
      <h2 data-reveal style="margin-bottom:1.2rem">Ett paraplyföretag som vi äger tillsammans.</h2>
      <p style="margin-bottom:0">KBT-Konsulterna är ett paraplyföretag som vi äger gemensamt,
      och inom ramen för det arbetar vi också i våra individuella aktiebolag. Det är vanligt
      i vår bransch. I praktiken betyder det att du har en behandlare — och en mottagning
      med kollegor att rådgöra med.</p>
    </div>
  </div>
</section>

{cta_band(b)}
{marks_band(b)}
'''
    return page('medarbetare/index.html',
                'Medarbetare – psykologer i Uppsala | KBT-Konsulterna',
                'Sju legitimerade psykologer och psykoterapeuter i Uppsala. Se vem '
                'som arbetar med vad, och hör av dig direkt.',
                body, ogimg='stillhet')


# ==========================================================================
# Medarbetare — bio pages
#
# Bio prose is read from the crawl of the client's existing site so their own
# words carry over verbatim. See docs/03-TEAM.md: these bios are the practice's
# strongest asset and are deliberately not rewritten.
# ==========================================================================
import json


def bio_paragraphs(slug):
    with open('research/crawl-pages.json', encoding='utf-8') as f:
        pages = json.load(f)
    raw = pages[f'medarbetare__{slug}']['text']
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw) if p.strip()]
    paras = [p for p in paras if not p.startswith('#')]
    paras = [p for p in paras if 'E-postadress' not in p and '@' not in p]

    # The extractor split a few sentences across block elements; rejoin any
    # fragment that does not end on sentence punctuation.
    merged = []
    for p in paras:
        p = p.replace('\n', ' ').strip()
        if merged and not re.search(r'[.!?:]$', merged[-1]):
            merged[-1] = merged[-1] + ' ' + p
        else:
            merged.append(p)
    return [H.escape(p) for p in merged if p and p != '-']


def build_bio(p):
    b = '../'
    slug, name = p['slug'], p['name']
    paras = '\n      '.join(f'<p>{t}</p>' for t in bio_paragraphs(slug))
    email = f'{slug.replace("-", ".")}@kbt-konsulterna.se'

    others = [q for q in TEAM if q['slug'] != slug][:3]
    more = '\n      '.join(
        person_card(b, q, sizes='(min-width: 56rem) 22vw, (min-width: 34rem) 45vw, 90vw')
        for q in others)

    lowres_note = ''
    body = f'''
<section class="band">
  <div class="wrap">
    <p class="crumb">
      <a class="a-link" href="{b}index.html">Hem</a><span>/</span>
      <a class="a-link" href="{b}medarbetare/index.html">Medarbetare</a><span>/</span>{name}
    </p>
    <div class="bio">
      <div class="bio__aside">
        <div class="bio__media">{pic_person(b, slug, f'{name}, {p["role"].split(" · ")[0].lower()}', sizes='(min-width: 58rem) 20rem, 92vw', eager=True)}</div>
        <div>
          <p class="price__label" style="margin-bottom:0.4rem">Kontakt</p>
          <p style="margin-bottom:0.4rem"><a class="a-link" href="mailto:{email}">{email}</a></p>
          <p style="margin-bottom:0"><a class="a-link" href="{TEL_HREF}">{TEL}</a></p>
        </div>
        <a class="btn btn--primary" href="{b}kontakt/index.html">Boka samtal {ARROW_BTN}</a>
      </div>
      <div>
        <h1 style="font-size:var(--step-4);margin-bottom:0.7rem">{name}</h1>
        <p class="person__role" style="font-size:var(--step-0);margin-bottom:2.2rem">{p['role']}</p>
        <div class="bio__prose prose">
          {paras}
        </div>
      </div>
    </div>
  </div>
</section>
{lowres_note}
<section class="band band--hi">
  <div class="wrap">
    <p class="eyebrow">Fler medarbetare</p>
    <div class="team">
      {more}
    </div>
    <p style="margin-top:2.5rem;margin-bottom:0"><a class="a-link" href="{b}medarbetare/index.html">Alla medarbetare {ARROW}</a></p>
  </div>
</section>

{cta_band(b)}
'''
    # Keep the meta description inside search-result length: first sentence of
    # the note only, trimmed if the whole thing still runs long.
    first = p['note'].split('. ')[0].rstrip('.')
    desc = f'{name}, {p["role"].split(" · ")[0].lower()} hos KBT-Konsulterna i Uppsala. {first}.'
    if len(desc) > 165:
        desc = f'{name}, {p["role"].split(" · ")[0].lower()} hos KBT-Konsulterna i Uppsala.'
    return page(f'medarbetare/{slug}.html',
                f'{name} – {p["role"].split(" · ")[0]} i Uppsala | KBT-Konsulterna',
                desc,
                body, ogimg='stillhet', ogtitle=f'{name} | KBT-Konsulterna')


# ==========================================================================
# Priser
# ==========================================================================
def build_priser():
    b = '../'
    body = f'''
{hero(b, 'bjork', 'Priser',
      'Vad det kostar',
      'Vi är en privat psykologmottagning. Här är priserna, villkoren och hur '
      'det fungerar om din arbetsgivare eller Regionen betalar.',
      'Ljus björkskog en sommardag',
      crumb=f'<a href="{b}index.html">Hem</a><span>/</span>Priser')}

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Privat finansierad terapi</p></div>
    <div>
      <div class="prices" style="margin-bottom:clamp(2.5rem,5vw,3.5rem)">
        <div>
          <p class="price__label">Enskilt samtal</p>
          <p class="price__fig">1 500 kr <span class="price__unit">/ 45 min</span></p>
        </div>
        <div>
          <p class="price__label">Parterapi</p>
          <p class="price__fig">2 400 kr <span class="price__unit">/ 60 min</span></p>
          <p class="price__note">Eller 1 800 kr / 45 min. Ofta behövs minst 60 minuter,
          eller 2 × 45 minuter per besök.</p>
        </div>
      </div>
      <div class="prose prose--wide">
        <h2 data-reveal style="font-size:var(--step-2);margin-bottom:1.1rem">Villkor</h2>
        {ticks(['Moms tillkommer om arbetsgivare, försäkringsbolag eller socialtjänst betalar.', 'Avbokning senare än 24 timmar före bokat besök debiteras i sin helhet.', 'Samtalen finansieras vanligen av privatpersoner eller arbetsgivare. I vissa fall betalar ett försäkringsbolag, behandlingshem, socialtjänsten, en skola eller annan verksamhet.'])}
      </div>
    </div>
  </div>
</section>

<section class="band band--hi">
  <div class="wrap split">
    <div><p class="eyebrow">Övriga tjänster</p></div>
    <div class="prose prose--wide">
      <h2 data-reveal style="margin-bottom:1.2rem">Handledning, utbildning och utredning</h2>
      <p>Priser för handledning, utbildning och neuropsykiatrisk utredning sätts utifrån
      uppdragets omfattning och lämnas på förfrågan. Skriv till
      <a class="a-link" href="mailto:{MAIL}">{MAIL}</a> och beskriv vad ni behöver, så
      återkommer vi med ett förslag.</p>
      <p style="margin-bottom:0"><a class="a-link" href="{b}organisationer/index.html">Mer om våra uppdrag för organisationer {ARROW}</a></p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Remiss &amp; högkostnadsskydd</p></div>
    <div class="prose prose--wide">
      <h2 data-reveal style="margin-bottom:1.2rem">Två av oss tar emot remisser från Regionen</h2>
      <p><strong>Angeli Holmstedt</strong> och <strong>Jens Karström</strong> tar emot
      patientremisser via Region Uppsala under högkostnadsskyddet.</p>
      <p>För att det ska gälla behöver du vara patient inom psykiatrin och ha blivit erbjuden
      privat psykoterapi av din remittent. Det är alltså bara den som har remiss från
      psykiatrin som kan ta del av högkostnadsskyddet — du kan inte få remiss till oss via
      vårdcentralen.</p>
      <p style="margin-bottom:0">För alla andra gäller privat taxa enligt priserna ovan.</p>
    </div>
  </div>
</section>

<section class="band band--sand">
  <div class="wrap split">
    <div><p class="eyebrow">Trygghet</p></div>
    <div>
      {ticks(['Legitimerade psykologer, med Socialstyrelsens tillsyn', 'Tystnadsplikt enligt samma lagar som inom sjukvården', 'Patientförsäkring', 'Videosamtal via Kaddio med BankID'], two=True)}
    </div>
  </div>
</section>

{process_band(b)}
{cta_band(b, heading='Osäker på vad som passar?',
          text='Skriv eller ring, och beskriv kort vad det handlar om. Vi föreslår en '
               'väg framåt och säger vad det skulle kosta.')}
{akut_strip(b)}
'''
    return page('priser/index.html',
                'Priser – psykolog och parterapi i Uppsala | KBT-Konsulterna',
                'Enskilt samtal 1 500 kr / 45 min, parterapi 2 400 kr / 60 min. '
                'Villkor, remiss och högkostnadsskydd hos KBT-Konsulterna.',
                body, ogimg='kunskap')


# ==========================================================================
# Vanliga frågor  (Q&A carried over verbatim from the client's own page)
# ==========================================================================
def faq_pairs():
    with open('research/crawl-pages.json', encoding='utf-8') as f:
        pages = json.load(f)
    raw = pages['vanliga-fragor']['text']
    chunks = re.split(r'^### ', raw, flags=re.M)[1:]
    out = []
    for c in chunks:
        lines = c.strip().split('\n')
        q = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()
        paras = [p.replace('\n', ' ').strip()
                 for p in re.split(r'\n\s*\n', body) if p.strip()]
        out.append((q, paras))
    return out


def build_faq():
    b = '../'
    items = []
    for q, paras in faq_pairs():
        ps = '\n          '.join(f'<p>{H.escape(p)}</p>' for p in paras)
        items.append(f'''<details>
        <summary><span>{H.escape(q)}</span>{icon('plus', 'faq__toggle')}</summary>
        <div>
          {ps}
        </div>
      </details>''')
    faq_html = '\n      '.join(items)

    ld = {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [
            {'@type': 'Question', 'name': q,
             'acceptedAnswer': {'@type': 'Answer', 'text': ' '.join(paras)}}
            for q, paras in faq_pairs()
        ],
    }
    extra = ('<script type="application/ld+json">'
             + json.dumps(ld, ensure_ascii=False) + '</script>\n')

    body = f'''
<section class="band">
  <div class="wrap">
    <p class="crumb">
      <a class="a-link" href="{b}index.html">Hem</a><span>/</span>
      <a class="a-link" href="{b}om-oss/index.html">Om oss</a><span>/</span>Vanliga frågor
    </p>
    <div class="split">
      <div>
        <p class="eyebrow">Vanliga frågor</p>
        <p style="font-size:1rem;color:var(--muted);max-width:15rem">Hittar du inte svaret?
        Skriv till <a class="a-link" href="mailto:{MAIL}">{MAIL}</a>.</p>
      </div>
      <div style="min-width:0">
        <h1 style="font-size:var(--step-4);max-width:28rem;margin-bottom:clamp(2rem,4vw,3rem)">Värt att veta om vår psykologverksamhet</h1>
        <div class="faq">
          {faq_html}
        </div>
      </div>
    </div>
  </div>
</section>

{price_band(b)}
{cta_band(b)}
{akut_strip(b)}
'''
    return page('om-oss/vanliga-fragor.html',
                'Vanliga frågor om vår psykologmottagning | KBT-Konsulterna',
                'Svar på vanliga frågor om väntetider, högkostnadsskydd och remiss, '
                'digitala möten, kvällstider och utredningar hos KBT-Konsulterna.',
                body, ogimg='kunskap', extra=extra)


# ==========================================================================
# Om oss
# ==========================================================================
def build_om_oss():
    b = '../'
    metoder = topics_grid(b, [
        ('Beteendeterapi och kognitiv terapi',
         'Grunderna i KBT — att förändra beteenden och att arbeta med tankar och '
         'tolkningar.'),
        ('ACT',
         'Acceptance and Commitment Therapy. Att göra plats för det svåra och '
         'samtidigt röra sig mot det som är viktigt.'),
        ('Motiverande samtal (MI)',
         'Ett samtalssätt för förändring. Angeli Holmstedt är MI-utbildare och medlem '
         'i MINT.'),
        ('Mindfulnessbaserade program',
         'MBSR, MBCT och MBRP. Socialstyrelsen rekommenderar mindfulnessbaserad '
         'behandling vid återkommande depressioner.'),
        ('Återfallsprevention',
         'Strukturerat arbete för att förebygga återfall vid missbruk och beroende.'),
        ('IBCT',
         'Integrative Behavioral Couple Therapy — KBT-baserad parterapi.'),
        ('DBT',
         'Dialektisk beteendeterapi vid emotionell instabilitet.'),
        ('PE och schematerapi',
         'Prolonged exposure vid trauma, och schematerapi vid mönster som går igen '
         'över tid.'),
    ], three=True)

    body = f'''
{hero(b, 'stillhet', 'Om oss',
      'Gedigen kompetens, varmt bemötande',
      'KBT-Konsulterna är en privat psykologmottagning i centrala Uppsala. Vi är '
      'legitimerade psykologer och psykoterapeuter, och specialister i kognitiv '
      'beteendeterapi.',
      'Ett fönster med en krukväxt i mjukt motljus',
      crumb=f'<a href="{b}index.html">Hem</a><span>/</span>Om oss')}

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Vilka är vi?</p></div>
    <div class="prose prose--wide">
      <p class="lede" style="margin-bottom:1.4rem">Vi levererar en gedigen kompetens
      förpackad i ett varmt och professionellt bemötande.</p>
      <p>Vi är sju legitimerade psykologer. Flera av oss är dessutom legitimerade
      psykoterapeuter, specialister i klinisk psykologi eller neuropsykologi, och utbildade
      handledare. Vi har arbetat inom psykiatrin, BUP, primärvården, habiliteringen,
      beroendevården, skolan och behandlingshem — och undervisar eller har undervisat vid
      Uppsala universitet.</p>
      <p>Vår mottagning ligger i Gårdshuset vid Slottskällan på Sjukhusvägen 3, tio minuter
      från Centralstationen. Vi tar emot här, och online i hela Sverige.</p>
      <p style="margin-bottom:0"><a class="a-link" href="{b}medarbetare/index.html">Läs om var och en av oss {ARROW}</a></p>
    </div>
  </div>
</section>

{hub_section('kbt', 'Vad är KBT?',
             'Ett paraply, inte en mall.',
             '<p>KBT — kognitiv beteendeterapi — har ett mångårigt och gediget '
             'forskningsstöd och är i dag ett paraplybegrepp som samlar flera olika '
             'behandlingsformer. Vi använder framför allt dem som Socialstyrelsen '
             'rekommenderar och som har starkast forskningsstöd.</p>'
             '<p style="margin-bottom:0">KBT betraktas i dag som en av de mest effektiva '
             'behandlingsformerna vid depression, ångest, sömnstörningar, problem i '
             'parrelationer och vid överdrivet användande av alkohol, droger, läkemedel '
             'och spel. Att metoderna är strukturerade betyder inte att behandlingen är '
             'det samma för alla — den utgår från dina mål och dina värderingar.</p>',
             metoder, tone='band--hi')}

{hub_section('evidens', 'Evidensbaserad praktik',
             'Det står i vårt namn.',
             '<p>Vårt företag heter KBT Konsulterna, Evidensbaserad Praktik, Uppland AB. '
             'En evidensbaserad praktik innebär att man som professionell väger samman sin '
             'samlade erfarenhet och expertis med den bästa forskningsbaserade kunskap som '
             'finns tillgänglig — och med den enskildes situation, erfarenhet och önskemål.</p>'
             '<p>Evidens kommer från vetenskapliga studier om insatsers effekter, och det '
             'krävs kunskap för att värdera dem. Att det finns forskning inom ett område '
             'betyder inte att resultatet går att lita på. Som utbildade psykologer och '
             'psykoterapeuter har vi en gedigen kompetens i att värdera forskning.</p>'
             '<p style="margin-bottom:0">Socialstyrelsens nationella riktlinjer vägleder oss '
             'inom många av de problemområden vi arbetar med.</p>',
             '')}

{hub_section('online', 'Onlinesamtal',
             'När det inte passar att ses på plats.',
             '<p>Om du inte har möjlighet att komma till mottagningen erbjuder vi samtal '
             'online via dator eller mobiltelefon. Du kan ha hela din kontakt med oss på '
             'distans, eller bara vid de tillfällen du är bortrest eller sjuk.</p>'
             '<p>För privatpersoner erbjuder vi bedömning, behandling, rådgivning och stöd '
             'online, i hela Sverige. För företag och offentlig verksamhet erbjuder vi '
             'handledning och andra insatser online.</p>'
             '<p style="margin-bottom:0"><strong>Säkerhet:</strong> vi använder Kaddios system '
             'för säkra videosamtal, som uppfyller Socialstyrelsens krav på stark '
             'autentisering. Inloggning sker med BankID. Samma lagar om sekretess och '
             'patientsäkerhet gäller som vid besök på mottagningen.</p>',
             '', tone='band--hi')}

{hub_section('legitimation', 'Vem får ge behandling?',
             'Legitimation är en skyddad titel.',
             '<p>Titlarna <strong>psykolog</strong> och <strong>psykoterapeut</strong> är '
             'skyddade i lag. En legitimerad psykolog har en femårig universitetsutbildning '
             'och ett års praktisk tjänstgöring bakom sig, och står under Socialstyrelsens '
             'tillsyn. En legitimerad psykoterapeut har därefter ytterligare en '
             'påbyggnadsutbildning.</p>'
             '<p style="margin-bottom:0">Begrepp som &rdquo;terapeut&rdquo;, '
             '&rdquo;samtalsterapeut&rdquo; eller &rdquo;coach&rdquo; är däremot inte '
             'skyddade — vem som helst får kalla sig det. Hos oss är alla legitimerade '
             'psykologer, och vi arbetar under tystnadsplikt och med patientförsäkring.</p>',
             '')}

<section class="bleed">
  <div class="bleed__media">{pic_wide(b, 'kunskap', 'Bokhyllor fyllda med böcker')}</div>
  <div class="bleed__scrim"></div>
  <div class="wrap bleed__inner">
    <blockquote class="pull" data-reveal>
      &rdquo;Vi vill inte publicera omdömen eftersom vi arbetar under sekretess. Det bästa
      betyget för oss är alla som kontaktar oss för att de blivit rekommenderade av vänner,
      anhöriga eller andra vårdinrättningar.&rdquo;
      <cite>Ur våra vanliga frågor</cite>
    </blockquote>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Mer</p></div>
    <div>
      {contents_list(b, [])}
      <ul class="linklist linklist--two">
        <li><a href="{b}om-oss/vanliga-fragor.html">Vanliga frågor</a></li>
        <li><a href="{b}medarbetare/index.html">Medarbetare</a></li>
        <li><a href="{b}priser/index.html">Priser och villkor</a></li>
        <li><a href="{b}akut-hjalp/index.html">Akut hjälp</a></li>
      </ul>
    </div>
  </div>
</section>

{cta_band(b)}
{marks_band(b)}
'''
    return page('om-oss/index.html',
                'Om KBT-Konsulterna – psykologmottagning i Uppsala | KBT-Konsulterna',
                'Om KBT-Konsulterna i Uppsala: vilka vi är, vad KBT är, vår '
                'evidensbaserade praktik och vad legitimation betyder.',
                body, ogimg='stillhet')


# ==========================================================================
# Kontakt
# ==========================================================================
SOURCE_OPTS = ['Google (sökning)', 'Google Maps', 'Rekommendation',
               'Arbetsgivare / företag', 'Kände till oss sedan tidigare',
               'Sociala medier', 'Annat / vet ej']


def source_select(idx):
    opts = '\n            '.join(
        f'<option>{o}</option>' for o in SOURCE_OPTS)
    return f'''<div class="field">
          <label for="hittade{idx}">Hur hittade du oss?</label>
          <div class="select">
            <select id="hittade{idx}" name="hittade">
              <option value="">Välj gärna ett alternativ</option>
              {opts}
            </select>
            {icon('chevron-down', 'select__caret')}
          </div>
        </div>'''


def build_kontakt():
    b = '../'
    body = f'''
{hero(b, 'samtal', 'Kontakt &amp; bokning',
      'Hör av dig',
      'Skriv eller ring. Vi återkommer så snart vi har möjlighet. Du behöver '
      'inte veta på förhand vad du vill ha hjälp med.',
      'Två personer vid ett bord med en kopp kaffe var',
      crumb=f'<a href="{b}index.html">Hem</a><span>/</span>Kontakt',
      actions=False)}

<section class="band">
  <div class="wrap split split--even">
    <div>
      <p class="eyebrow">Kontaktuppgifter</p>
      <h2 data-reveal style="font-size:var(--step-2);margin-bottom:1.6rem">Ring, mejla eller använd formuläret.</h2>
      <dl class="facts" style="grid-template-columns:1fr">
        <div>
          <dt>Telefon</dt>
          <dd><a class="a-link" href="{TEL_HREF}">{TEL}</a><br>
          Lämna ett meddelande på telefonsvararen så återkommer vi så snart vi kan.</dd>
        </div>
        <div>
          <dt>E-post</dt>
          <dd><a class="a-link" href="mailto:{MAIL}">{MAIL}</a></dd>
        </div>
        <div>
          <dt>Besöksadress</dt>
          <dd>{ADDR}<br><a class="a-link" href="{MAPS}">Visa på karta {ARROW}</a></dd>
        </div>
        <div>
          <dt>Vägbeskrivning</dt>
          <dd>Vi finns i hjärtat av Uppsala, tio minuter från Centralstationen. Mottagningen
          ligger i en vacker miljö i Gårdshuset, vid Slottskällan.</dd>
        </div>
        <div>
          <dt>Öppettider</dt>
          <dd>Måndag–fredag 09–17. Kvällstider ett par gånger per vecka, både digitalt och
          på mottagningen.</dd>
        </div>
        <div>
          <dt>Direkt till en av oss</dt>
          <dd>Alla medarbetare har egen e-post.
          <a class="a-link" href="{b}medarbetare/index.html">Se vem som arbetar med vad {ARROW}</a></dd>
        </div>
      </dl>
    </div>
    <div>
      <p class="eyebrow">Kontaktformulär</p>
      <h2 data-reveal style="font-size:var(--step-2);margin-bottom:1.6rem">Frågor eller förfrågan om tid</h2>
      <form class="form" method="post" action="#">
        <div class="field">
          <label for="namn">Namn <span class="field__req">*</span></label>
          <input id="namn" name="namn" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="epost">E-post <span class="field__req">*</span></label>
          <input id="epost" name="epost" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="telefon">Telefon</label>
          <input id="telefon" name="telefon" type="tel" autocomplete="tel">
        </div>
        <div class="field">
          <label for="meddelande">Meddelande <span class="field__req">*</span></label>
          <textarea id="meddelande" name="meddelande" required></textarea>
        </div>
        {source_select(1)}
        <button class="btn btn--primary" type="submit">Skicka {ARROW_BTN}</button>
        <p style="font-size:0.95rem;color:var(--muted);margin:0">Skriv inga känsliga uppgifter
        om din hälsa i formuläret. Vi hör av oss och tar det vidare i ett samtal.</p>
      </form>
    </div>
  </div>
</section>

<section class="band band--hi anchor" id="foretag">
  <div class="wrap split split--even">
    <div>
      <p class="eyebrow">Företag &amp; offentlig verksamhet</p>
      <h2 data-reveal style="font-size:var(--step-2);margin-bottom:1.2rem">Förfrågan om uppdrag</h2>
      <div class="prose">
        <p>Vill ni diskutera handledning, utbildning, föreläsningar eller ett samarbete?
        Beskriv kort vad ni behöver, så återkommer vi med ett förslag och en prisuppgift.</p>
        <p style="margin-bottom:0"><a class="a-link" href="{b}organisationer/index.html">Läs mer om vad vi erbjuder organisationer {ARROW}</a></p>
      </div>
    </div>
    <div>
      <form class="form" method="post" action="#">
        <div class="field">
          <label for="foretagsnamn">Företag / organisation <span class="field__req">*</span></label>
          <input id="foretagsnamn" name="foretag" type="text" autocomplete="organization" required>
        </div>
        <div class="field">
          <label for="kontaktperson">Kontaktperson <span class="field__req">*</span></label>
          <input id="kontaktperson" name="kontaktperson" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="epost2">E-post <span class="field__req">*</span></label>
          <input id="epost2" name="epost" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="telefon2">Telefon <span class="field__req">*</span></label>
          <input id="telefon2" name="telefon" type="tel" autocomplete="tel" required>
        </div>
        <div class="field">
          <label for="meddelande2">Meddelande</label>
          <textarea id="meddelande2" name="meddelande"></textarea>
        </div>
        {source_select(2)}
        <button class="btn btn--primary" type="submit">Skicka {ARROW_BTN}</button>
      </form>
    </div>
  </div>
</section>

{process_band(b)}
{akut_strip(b)}
'''
    return page('kontakt/index.html',
                'Kontakt & bokning – psykolog i Uppsala | KBT-Konsulterna',
                'Kontakta KBT-Konsulterna i Uppsala. Telefon 018 – 10 40 44. '
                'Mottagning i Gårdshuset vid Slottskällan, tio minuter från '
                'Centralstationen.',
                body, ogimg='samtal')


# ==========================================================================
# Akut hjälp
# ==========================================================================
def build_akut():
    b = '../'
    body = f'''
<section class="band akut">
  <div class="wrap">
    <p class="crumb">
      <a class="a-link" href="{b}index.html">Hem</a><span>/</span>Akut hjälp
    </p>
    <div class="split">
      <div><p class="eyebrow">Akut hjälp</p></div>
      <div class="prose--wide">
        <h1 style="font-size:var(--step-4);margin-bottom:1.2rem">Behöver du hjälp direkt?</h1>
        <p class="lede" style="color:var(--deep);margin-bottom:1.6rem">KBT-Konsulterna är en
        mottagning med bokade tider. Vi kan inte ta emot akut och har ingen jour.</p>
        <p style="margin-bottom:0">Om det uppstår akuta besvär kan du få stöd på något av
        följande sätt, dygnet runt.</p>
      </div>
    </div>
  </div>
</section>

<section class="band band--tight">
  <div class="wrap split">
    <div><p class="eyebrow">Vid fara för liv</p></div>
    <div>
      <p class="price__fig" style="margin-bottom:0.6rem">Ring 112</p>
      <p style="margin-bottom:0">Vid akut fara för liv eller hälsa.</p>
    </div>
  </div>
</section>

<section class="band band--hi">
  <div class="wrap split">
    <div><p class="eyebrow">Stödlinjer</p></div>
    <div>
      <dl class="facts">
        <div>
          <dt>MIND Stödlinje</dt>
          <dd><a class="a-link" href="tel:+4690101">90 101</a> — eller chatta via
          <a class="a-link" href="https://mind.se/">mind.se</a>.</dd>
        </div>
        <div>
          <dt>SuicideZero</dt>
          <dd>Information och stöd vid självmordstankar:
          <a class="a-link" href="https://suicidezero.se/">suicidezero.se</a></dd>
        </div>
        <div>
          <dt>1177 Vårdguiden</dt>
          <dd>Ring <a class="a-link" href="tel:+461177">1177</a> för sjukvårdsrådgivning,
          eller välj din region på <a class="a-link" href="https://www.1177.se/">1177.se</a>
          för att hitta psykakuten där du bor.</dd>
        </div>
        <div>
          <dt>Akademiska sjukhuset, Uppsala</dt>
          <dd>Växel <a class="a-link" href="tel:+46186110000">018-611 00 00</a>.
          <a class="a-link" href="https://www.akademiska.se/for-patient-och-besokare/hitta-pa-sjukhuset/a-till-o/akutmottagningen-for-vuxenpsykiatri/">Akutmottagningen för vuxenpsykiatri {ARROW}</a></dd>
        </div>
      </dl>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div><p class="eyebrow">Psykiatriska akutmottagningar</p></div>
    <div>
      {ticks(['Uppsala — akutmottagningen för vuxenpsykiatri, Akademiska sjukhuset', 'Stockholm — psykiatriska akutmottagningen', 'Västerås — akutmottagningen för psykiatri', 'Gävle — psykiatriska jourmottagningen'], two=True)}
      <p style="margin-top:1.6rem;margin-bottom:0">Bor du någon annanstans i landet hittar du
      din närmaste psykakut genom att välja region på
      <a class="a-link" href="https://www.1177.se/">1177.se</a>.</p>
    </div>
  </div>
</section>

<section class="band band--deep">
  <div class="wrap split">
    <div><p class="eyebrow">När det inte är akut</p></div>
    <div class="prose--wide">
      <h2 data-reveal style="margin-bottom:1.2rem">Vi finns här för det som inte brådskar i dag.</h2>
      <p>Vårt mål är att ge snabba tider, och för det mesta lyckas vi med det. Hör av dig
      och berätta kort vad det handlar om.</p>
      <div class="actions" style="margin-top:2rem">
        <a class="btn btn--on-dark" href="{b}kontakt/index.html">Boka samtal {ARROW_BTN}</a>
        <a class="hero__tel" href="{TEL_HREF}">eller ring {TEL}</a>
      </div>
    </div>
  </div>
</section>
'''
    return page('akut-hjalp/index.html',
                'Akut hjälp vid psykisk ohälsa | KBT-Konsulterna',
                'Vid akuta psykiska besvär: ring 112, MIND Stödlinje 90 101, eller sök '
                'psykakuten där du bor. Vi har bokade tider och ingen jour.',
                body, ogimg='stillhet')


# ==========================================================================
# ==========================================================================
# Topic tree: the level-2 hubs and level-3 articles.
#
# This is the layer the old site carried at /vuxna/psykologisk-behandling-terapi/*
# and that the first cut of the redesign collapsed into page anchors. Collapsing
# it cost 33 indexable URLs, each of which was the landing page for a distinct
# search. They come back here as real pages, with the sibling navigator the old
# site had — plus breadcrumbs, named clinicians and structured data, which it
# did not.
# ==========================================================================
def node_path(*slugs):
    """('vuxna', 'behandling', 'oro-angest') -> vuxna/behandling/oro-angest/index.html"""
    return '/'.join(slugs) + '/index.html'


def to_href(base, path):
    """Content-tree paths are written root-relative and may omit index.html."""
    if path.endswith('/'):
        path += 'index.html'
    return base + path


def side_nav(base, section, l2_slug, l3_slug=None):
    """The sibling navigator: every level-2 page in this section, with the
    active one's children nested underneath. Sticky beside the article on
    desktop; a closed <details> above it on phones."""
    items = []
    for c in section['children']:
        active2 = c['slug'] == l2_slug
        cur = ' aria-current="page"' if active2 and not l3_slug else ''
        cls = ' class="is-open"' if active2 else ''
        href = to_href(base, node_path(section['slug'], c['slug']))
        items.append(f'<li{cls}><a href="{href}"{cur}>{H.escape(c["label"])}</a>')
        kids = c.get('children') or []
        if kids and active2:
            items.append('<ul class="sidenav__sub">')
            for g in kids:
                gcur = ' aria-current="page"' if g['slug'] == l3_slug else ''
                ghref = to_href(base, node_path(section['slug'], c['slug'], g['slug']))
                items.append(
                    f'<li><a href="{ghref}"{gcur}>{H.escape(g["label"])}</a></li>')
            items.append('</ul>')
        items.append('</li>')
    inner = '\n        '.join(items)
    shref = to_href(base, section['slug'] + '/index.html')
    return f'''<nav class="sidenav" aria-label="Innehåll i {H.escape(section["label"])}">
    <details class="sidenav__box" open>
      <summary class="sidenav__head">
        <span>{H.escape(section['label'])}</span>
        {icon('chevron-down', 'sidenav__chev')}
      </summary>
      <ul class="sidenav__list">
        {inner}
      </ul>
      <p class="sidenav__all"><a href="{shref}">Översikt {H.escape(section['label'].lower())} {ARROW}</a></p>
    </details>
  </nav>'''


def crumbs(base, trail):
    """trail: [(label, path-or-None)], last item is the current page."""
    out = []
    for label, path in trail[:-1]:
        out.append(f'<a href="{to_href(base, path)}">{H.escape(label)}</a><span>/</span>')
    out.append(H.escape(trail[-1][0]))
    return ''.join(out)


def breadcrumb_ld(trail):
    items = []
    for i, (label, path) in enumerate(trail, 1):
        url = SITE + '/' + re.sub(r'index\.html$', '', path) if path else None
        item = f'"name":{json_str(label)}'
        if url:
            item += f',"item":"{url}"'
        items.append('{"@type":"ListItem","position":%d,%s}' % (i, item))
    return ('<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"BreadcrumbList",'
            '"itemListElement":[' + ','.join(items) + ']}\n</script>\n')


def article_ld(title, desc, path, people):
    """MedicalWebPage with named, credentialed authors — the E-E-A-T signal the
    old topic pages had none of. Google weights it heavily for health content."""
    url = SITE + '/' + re.sub(r'index\.html$', '', path)
    authors = ','.join(
        '{"@type":"Person","name":%s,"jobTitle":%s,"url":"%s/medarbetare/%s/"}'
        % (json_str(BY_SLUG[s]['name']), json_str(BY_SLUG[s]['role']), SITE, s)
        for s in people if s in BY_SLUG)
    a = f',"author":[{authors}]' if authors else ''
    return ('<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"MedicalWebPage",'
            f'"name":{json_str(title)},"description":{json_str(desc)},"url":"{url}",'
            '"inLanguage":"sv-SE",'
            '"publisher":{"@type":"MedicalBusiness","name":"KBT-Konsulterna i Uppsala",'
            f'"url":"{SITE}"}}{a}}}\n</script>\n')


def json_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def people_block(base, slugs):
    """Who at the practice works with this. A clinic's topic page should say."""
    if not slugs:
        return ''
    rows = '\n      '.join(
        f'''<a class="byline" href="{base}medarbetare/{s}.html">
        <span class="byline__media">{pic_person(base, s, BY_SLUG[s]["name"], sizes="120px")}</span>
        <span class="byline__text">
          <span class="byline__name">{BY_SLUG[s]["name"]}</span>
          <span class="byline__role">{BY_SLUG[s]["role"]}</span>
        </span>
      </a>''' for s in slugs if s in BY_SLUG)
    return f'''<aside class="bylines">
      <h2 class="bylines__head">Vem träffar du?</h2>
      <div class="bylines__grid">
      {rows}
      </div>
      <p class="bylines__note"><a class="a-link" href="{base}medarbetare/index.html">Alla medarbetare {ARROW}</a></p>
    </aside>'''


def also_block(base, also):
    if not also:
        return ''
    lis = '\n      '.join(
        f'<li><a href="{to_href(base, p)}"><span>{H.escape(l)}</span>{ARROW}</a></li>'
        for l, p in also)
    return f'''<nav class="alsoread" aria-label="Läs vidare">
      <h2 class="alsoread__head">Läs vidare</h2>
      <ul class="linklist">
      {lis}
    </ul>
    </nav>'''


def child_cards(base, section, parent):
    kids = parent.get('children') or []
    if not kids:
        return ''
    cards = '\n      '.join(
        f'''<a class="topiccard" href="{to_href(base, node_path(section["slug"], parent["slug"], g["slug"]))}">
        <h3>{H.escape(g['label'])}</h3>
        <p>{H.escape(g['lede'])}</p>
        <span class="topiccard__go">Läs mer {ARROW}</span>
      </a>''' for g in kids)
    return f'''<section class="childgrid">
      <h2 class="childgrid__head">{H.escape(parent['label'])} — vad vi hjälper med</h2>
      <div class="topiccards">
      {cards}
      </div>
    </section>'''


def prev_next(base, section, parent, node):
    """Sequential links across the level-3 siblings: real internal link equity
    between the articles, which a flat sidebar alone does not create."""
    kids = parent.get('children') or []
    if not kids or node is parent:
        return ''
    i = kids.index(node)
    prev = kids[i - 1] if i > 0 else None
    nxt = kids[i + 1] if i < len(kids) - 1 else None
    out = []
    if prev:
        out.append(f'''<a class="pn pn--prev" href="{to_href(base, node_path(section["slug"], parent["slug"], prev["slug"]))}">
        <span class="pn__dir">Föregående</span><span class="pn__label">{H.escape(prev['label'])}</span></a>''')
    if nxt:
        out.append(f'''<a class="pn pn--next" href="{to_href(base, node_path(section["slug"], parent["slug"], nxt["slug"]))}">
        <span class="pn__dir">Nästa</span><span class="pn__label">{H.escape(nxt['label'])}</span></a>''')
    return f'<nav class="pnav" aria-label="Fler ämnen">\n      ' + '\n      '.join(out) + '\n    </nav>'


def build_topic_page(section, parent, node=None):
    """One article. node is None for a level-2 hub, otherwise the level-3 page."""
    is_hub = node is None
    n = parent if is_hub else node
    slugs = ([section['slug'], parent['slug']] if is_hub
             else [section['slug'], parent['slug'], node['slug']])
    path = node_path(*slugs)
    base = '../' * path.count('/')

    trail = [('Hem', 'index.html'), (section['label'], section['slug'] + '/index.html')]
    if is_hub:
        trail.append((parent['label'], None))
    else:
        trail.append((parent['label'], node_path(section['slug'], parent['slug'])))
        trail.append((node['label'], None))

    body_html = n['body'].replace('{base}', base)
    extra = (breadcrumb_ld([(l, p or path) for l, p in trail])
             + article_ld(n['title'], n['desc'], path, n.get('people') or []))

    inner = f'''<article class="article">
    <p class="crumb">{crumbs(base, trail)}</p>
    <h1>{H.escape(n['h1'])}</h1>
    <p class="article__lede">{H.escape(n['lede'])}</p>
    <div class="prose article__body">{body_html}</div>
    {people_block(base, n.get('people') or [])}
    {child_cards(base, section, parent) if is_hub else ''}
    {also_block(base, n.get('also') or [])}
    {prev_next(base, section, parent, n)}
  </article>'''

    # Article before navigator in source order: a phone reader and a crawler
    # both meet the h1 first, and on mobile the sibling list falls naturally
    # below the piece it belongs to. CSS puts it back in the left column on
    # desktop.
    body = f'''<section class="band band--article">
  <div class="wrap layout-side">
    {inner}
    {side_nav(base, section, parent['slug'], None if is_hub else node['slug'])}
  </div>
</section>

{cta_band(base)}
{akut_strip(base)}
'''
    return page(path, n['title'], n['desc'], body,
                ogimg=section.get('img', 'hero-room'), extra=extra)


def build_topics():
    total = 0
    count = 0
    for section in TREE:
        for parent in section['children']:
            total += build_topic_page(section, parent)
            count += 1
            for g in parent.get('children') or []:
                total += build_topic_page(section, parent, g)
                count += 1
    print(f'  {count} topic pages')
    return total


def build_sitemap():
    """Every canonical URL, so the 38 new topic pages get discovered at launch
    rather than waiting to be crawled through the hubs."""
    urls = ['']                                   # homepage
    for path in ('vuxna/', 'barn-och-ungdom/', 'organisationer/', 'medarbetare/',
                 'priser/', 'kontakt/', 'om-oss/', 'om-oss/vanliga-fragor.html',
                 'akut-hjalp/'):
        urls.append(path)
    urls += [f'medarbetare/{p["slug"]}/' for p in TEAM]
    for section in TREE:
        for parent in section['children']:
            urls.append(f'{section["slug"]}/{parent["slug"]}/')
            for g in parent.get('children') or []:
                urls.append(f'{section["slug"]}/{parent["slug"]}/{g["slug"]}/')
    body = '\n'.join(f'  <url><loc>{SITE}/{u}</loc></url>' for u in urls)
    out = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f'{body}\n</urlset>\n')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'  sitemap.xml: {len(urls)} URLs')
    return len(out)


def main():
    total = 0
    pages = 0
    for fn in (build_home, build_vuxna, build_barn, build_org,
               build_medarbetare, build_priser, build_kontakt,
               build_om_oss, build_faq, build_akut):
        total += fn()
        pages += 1
    for p in TEAM:
        total += build_bio(p)
        pages += 1
    total += build_topics()
    build_sitemap()
    pages += sum(1 + len(c.get('children') or [])
                 for s in TREE for c in s['children'])
    print(f'Built {pages} pages, {total // 1024} KB of HTML.')


if __name__ == '__main__':
    main()

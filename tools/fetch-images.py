#!/usr/bin/env python3
"""Re-download source imagery for the KBT-Konsulterna site.

Stock photography: CC0 / public domain, from Wikimedia Commons.
Team photos + brand marks: the client's own assets, from the live site.

Originals land in assets/img/_src/ (wide images) and assets/team/ (portraits).
Run tools/build-images.py afterwards to regenerate the web variants.
"""
import os, urllib.parse, urllib.request, sys

UA = {'User-Agent': 'kbt-konsulterna-redesign/1.0 (asset fetch)'}

# CC0 stock, by Commons file name
STOCK = {
    'hero-room':   'Breather_Montreal_interior_(Unsplash).jpg',
    'band-forest': 'Forest_tree_shadows_(Unsplash).jpg',
    'vuxna':       'Budapest_Apartment_(Unsplash).jpg',
    'barn':        'Girl_in_Snow_(Unsplash).jpg',
    'barn-play':   'Playing_jenga_with_my_6_year_old_(Unsplash).jpg',
    'foretag':     'Minimalist_meeting_room_(Unsplash).jpg',
    'par':         'Seated_couple_snuggling_(Unsplash).jpg',
    'samtal':      'Coffee_Talks_(Unsplash).jpg',
    'stillhet':    'Wicker_plant_and_big_window_(Unsplash).jpg',
    'kunskap':     'Uppsala_Library_(Unsplash).jpg',
    'bjork':       'Birch_trees_in_a_grove_(Unsplash).jpg',
}

# Client's own photos, from the current WordPress uploads
BASE = 'https://kbt-konsulterna.se/wp-content/uploads'
TEAM = {
    'angeli-holmstedt': f'{BASE}/2021/09/Angeli_Holmstedt_mini_KBT-konsulterna.jpg',
    'thomas-alm':       f'{BASE}/2021/09/Thomas_Alm_mini_KBT-konsulterna.jpg',
    'karin-holmstrom':  f'{BASE}/2019/03/karin_holmstrom.jpg',
    'aksel-reppling':   f'{BASE}/2020/08/aksel_reppling.jpg',
    'elias-westerlund': f'{BASE}/2023/05/elias_westerlund-1.jpg',
    'jens-karstrom':    f'{BASE}/2024/05/Jens-rev.jpg',
    'barry-karlsson':   f'{BASE}/2024/05/Barry-ny-hemsidan.jpg',
}
BRAND = {
    'logo':              f'{BASE}/2023/12/kbt-konsulterna-logotyp.png',
    'socialstyrelsen':   f'{BASE}/2016/05/socialstyrelsen-logo20130601.png',
    'psykologforbundet': f'{BASE}/2023/03/psykologforbundet-360x35.png',
    'mint':              f'{BASE}/2023/04/mint-logo-e1682277312984.png',
    'btf':               f'{BASE}/2024/01/btf-logo-360x129.jpg',
}

def get(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 10_000:
        print(f'  skip (exists)  {dest}')
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
            data = r.read()
    except Exception as e:
        print(f'  FAILED  {dest}: {e}', file=sys.stderr)
        return
    with open(dest, 'wb') as f:
        f.write(data)
    print(f'  ok {len(data)//1024:>6} KB  {dest}')

print('CC0 stock from Wikimedia Commons (capped at 3840px):')
for slug, name in STOCK.items():
    url = ('https://commons.wikimedia.org/wiki/Special:FilePath/'
           + urllib.parse.quote(name) + '?width=2600')
    get(url, f'assets/img/_src/{slug}.jpg')

print("\nTeam photos (client's own):")
for slug, url in TEAM.items():
    get(url, f'assets/team/{slug}.jpg')

print("\nBrand + accreditation marks (client's own):")
for slug, url in BRAND.items():
    get(url, f'assets/brand/{slug}.{url.rsplit(".", 1)[-1]}')

print('\nDone. Now run: python3 tools/build-images.py')

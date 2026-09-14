#!/usr/bin/env python3
"""Build the self-hosted web fonts in assets/fonts/.

Both families are SIL OFL variable fonts, fetched from the Fontsource npm
package (the same files Google Fonts serves) and cut down for this site:

Familjen Grotesk  used as-is. Weights 400-700 are all in use and it is 19 KB.
Newsreader        weight axis limited to 400-600 (body text and <strong>), and
                  the optical-size axis pinned at 18. Newsreader is only ever
                  set between 17px (body) and 34px (.router__say, .pull), where
                  the full 6-72 opsz axis made no visible difference but tripled
                  the file: 132 KB -> 38 KB. That is the weight a phone waits on
                  before the first paint, and it cost a mobile Lighthouse point.

Sources are cached in assets/fonts/_src/ (not committed).

Requires fonttools and brotli:  pip install fonttools brotli
"""
import os
import urllib.request

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

CDN = 'https://cdn.jsdelivr.net/npm/@fontsource-variable/{pkg}@{ver}/{path}'
SRC = 'assets/fonts/_src'
OUT = 'assets/fonts'
SUBSETS = ('latin', 'latin-ext')

# (package, version, source file pattern, output name, axis limits or None)
FAMILIES = [
    ('familjen-grotesk', '5.3.0', 'familjen-grotesk-{sub}-wght-normal.woff2',
     'familjen-grotesk-{sub}.woff2', None),
    ('newsreader', '5.3.0', 'newsreader-{sub}-opsz-normal.woff2',
     'newsreader-{sub}.woff2', {'wght': (400, 600), 'opsz': 18}),
]


def fetch(pkg, ver, path, dest):
    if not os.path.exists(dest):
        url = CDN.format(pkg=pkg, ver=ver, path=path)
        with urllib.request.urlopen(url) as r, open(dest, 'wb') as f:
            f.write(r.read())
    return dest


def main():
    os.makedirs(SRC, exist_ok=True)
    for pkg, ver, pattern, out_pattern, limits in FAMILIES:
        fetch(pkg, ver, 'LICENSE', f'{OUT}/OFL-{pkg}.txt')
        for sub in SUBSETS:
            name = pattern.format(sub=sub)
            src = fetch(pkg, ver, f'files/{name}', f'{SRC}/{name}')
            font = TTFont(src)
            if limits:
                font = instancer.instantiateVariableFont(font, limits)
            font.flavor = 'woff2'
            out = f'{OUT}/{out_pattern.format(sub=sub)}'
            font.save(out)
            print(f'  {os.path.basename(out):36} {os.path.getsize(src) // 1024:4} KB -> '
                  f'{os.path.getsize(out) // 1024:4} KB')


if __name__ == '__main__':
    main()

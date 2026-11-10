#!/usr/bin/env bash
# Remove the old WordPress files from the live web root, once the new site is up.
#
#   tools/cleanup-wordpress.sh live            # list what would go, change nothing
#   tools/cleanup-wordpress.sh live --delete   # delete the WordPress files
#   tools/cleanup-wordpress.sh test            # list staging (a safe test run)
#
# Normally run by GitHub Actions (.github/workflows/cleanup-wordpress.yml) with
# the login in FTP_HOST, FTP_USER, FTP_PASS and FTP_DIR, as for tools/deploy.sh.
#
# Only names WordPress itself ships are deleted (wp-*, index.php, xmlrpc.php,
# license and readme files). Everything else is kept, and anything that is
# neither ours nor WordPress is listed for a person to look at: subdomain
# folders, .well-known (the certificate) and cgi-bin may live in the web root.
set -euo pipefail

cd "$(dirname "$0")/.."

TARGET="${1:-}" MODE="${2:-}"
usage() { echo "usage: tools/cleanup-wordpress.sh test|live [--delete]" >&2; exit 2; }
case "$TARGET" in test|live) ;; *) usage ;; esac
case "$MODE" in ''|--delete) ;; *) usage ;; esac
if [ "$MODE" = --delete ] && [ "$TARGET" != live ]; then
  echo "Deleting is only for the live site; staging never had WordPress." >&2; exit 2
fi
command -v lftp >/dev/null || { echo "lftp is missing: sudo apt install lftp" >&2; exit 1; }
: "${FTP_HOST:?}" "${FTP_USER:?}" "${FTP_PASS:?}" "${FTP_DIR:?}"

SITE=https://kbt-konsulterna.se
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

# The password goes through the environment, never on the command line.
export LFTP_PASSWORD="$FTP_PASS"
ftp() {
  lftp --env-password -u "$FTP_USER" "$FTP_HOST" <<EOF
set ftp:ssl-force true
set ftp:ssl-protect-data true
set ssl:verify-certificate true
set net:max-retries 2
set cmd:fail-exit yes
$1
EOF
}

# 1. List the web root (one name per line, folders end in "/").
ftp "cd \"$FTP_DIR\"; cls -1aF" > "$WORK/listing"

# 2. Sort every name into ours, WordPress and other.
python3 - "$WORK/listing" "$WORK/delete" <<'PY'
import sys
listing, out = sys.argv[1:3]
OURS = {'index.html', '404.html', '.htaccess', 'robots.txt', 'sitemap.xml',
        'akut-hjalp/', 'assets/', 'barn-och-ungdom/', 'kontakt/', 'medarbetare/',
        'om-oss/', 'organisationer/', 'priser/', 'vuxna/'}
WP_FILES = {'index.php', 'xmlrpc.php', 'license.txt', 'readme.html',
            'licens.html', 'licens-sv_SE.txt'}
names = []
for line in open(listing, encoding='utf-8', errors='replace'):
    name = line.rstrip('\n').rstrip('@*=|')
    if name and name not in ('./', '../', '.', '..'):
        names.append(name)

# A home folder, not a web root: deleting or uploading here would be wrong.
if 'public_html/' in names or {'etc/', 'mail/'} <= set(names):
    sys.exit("This looks like the account's home folder, not the web root "
             "(it has public_html, etc or mail). Set FTP_DIR to the web root. Stopping.")

ours = [n for n in names if n in OURS]
wp = [n for n in names if n not in OURS and (n.startswith('wp-') or n in WP_FILES)]
other = [n for n in names if n not in OURS and n not in wp]

def show(title, items):
    print(f"\n{title} ({len(items)}):")
    for n in items or ['(none)']:
        print('  ' + n)

show('The new site (kept)', ours)
show('WordPress (deleted with --delete)', wp)
show('Neither, kept: look through these by hand', other)
if 'index.html' in names and 'index.php' in names:
    print("\nNote: index.html and index.php are both there; the new .htaccess "
          "serves index.html first.")
open(out, 'w').write('\n'.join(wp) + ('\n' if wp else ''))
PY

if [ "$MODE" != --delete ]; then
  echo
  echo "Preview only, nothing was deleted."
  exit 0
fi
if [ ! -s "$WORK/delete" ]; then
  echo "No WordPress files left, nothing to delete."; exit 0
fi

# 3. Only delete once the new site is the one being served.
grep -qx 'index.html' "$WORK/listing" || { echo "The new index.html is not on the server, stopping." >&2; exit 1; }
curl -fsS "$SITE/" | grep -q 'assets/css/site.css' \
  || { echo "$SITE/ does not serve the new site yet, stopping." >&2; exit 1; }

cmds="cd \"$FTP_DIR\""
while IFS= read -r n; do
  case "$n" in
    */) cmds+="; rm -r \"${n%/}\"" ;;
    *)  cmds+="; rm \"$n\"" ;;
  esac
done < "$WORK/delete"
echo
echo "Deleting $(wc -l < "$WORK/delete") WordPress entries (wp-content can take a few minutes)..."
ftp "$cmds"

# 4. Check the result from the outside.
home=$(curl -s -o /dev/null -w '%{http_code}' "$SITE/")
login=$(curl -s -o /dev/null -w '%{http_code}' "$SITE/wp-login.php")
echo "Home page: HTTP $home. wp-login.php: HTTP $login (404 expected)."
[ "$home" = 200 ] || { echo "The home page does not answer 200, check the site now." >&2; exit 1; }
echo "Done."

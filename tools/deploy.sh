#!/usr/bin/env bash
# Build the live version of the site and upload it to Misshosting over FTP with TLS.
#
#   tools/deploy.sh test --dry-run   # list what would be uploaded, change nothing
#   tools/deploy.sh test             # upload to staging.kbt-konsulterna.se
#   tools/deploy.sh live             # upload to the live site (asks first)
#
# Needs lftp (apt install lftp) and one file per target, tools/deploy-test.env
# and tools/deploy-live.env. Neither is committed:
#
#   FTP_HOST=ftp.kbt-konsulterna.se
#   FTP_USER=[ftp-user-from-niclas]
#   FTP_PASS=[ftp-password]
#   FTP_DIR=/                        # the site's web root as that FTP account sees it
#
# The repo itself stays the GitHub Pages preview: the live version is built in
# a temporary copy with KBT_LIVE=1, so nobody has to flip PREVIEW by hand.
#
# Only uploads. Nothing on the server is deleted, so a file removed from the
# site has to be deleted on the server by hand (cPanel File Manager or FTP).
set -euo pipefail

cd "$(dirname "$0")/.."

TARGET="${1:-}"
DRY=''
case "${2:-}" in
  --dry-run) DRY='--dry-run' ;;
  '') ;;
  *) TARGET='' ;;
esac
case "$TARGET" in
  test|live) ;;
  *) echo "usage: tools/deploy.sh test|live [--dry-run]" >&2; exit 2 ;;
esac
ENV_FILE="tools/deploy-$TARGET.env"

command -v lftp >/dev/null || { echo "lftp is missing: sudo apt install lftp" >&2; exit 1; }
[ -f "$ENV_FILE" ] || { echo "$ENV_FILE is missing (see the top of this script)" >&2; exit 1; }
# shellcheck disable=SC1090
source "$ENV_FILE"
: "${FTP_HOST:?}" "${FTP_USER:?}" "${FTP_PASS:?}" "${FTP_DIR:?}"

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
BUILD="$WORK/build" STAGE="$WORK/stage"
mkdir -p "$BUILD" "$STAGE"

# 1. Build the live version in a copy of the working tree.
rsync -a --exclude='/.git/' --exclude='/tmp/' --exclude='/docs/' \
  --exclude='/assets/*/_src/' --exclude='/assets/img/_client/' --exclude='/assets/team/' \
  ./ "$BUILD/"
(cd "$BUILD" && KBT_LIVE=1 python3 tools/build-site.py >/dev/null)
if grep -rlq 'name="robots" content="noindex, nofollow"' "$BUILD/index.html"; then
  echo "live build still carries noindex, stopping" >&2; exit 1
fi
grep -q 'action="skicka.php"' "$BUILD/kontakt/index.html" || { echo "contact forms are not wired to skicka.php" >&2; exit 1; }

# 2. Copy only what the public site needs. Sources, tools, docs and the
#    client's original photos and video clips stay at home.
rsync -a \
  --include='/index.html' --include='/404.html' --include='/.htaccess' \
  --include='/robots.txt' --include='/sitemap.xml' \
  --include='/akut-hjalp/***' --include='/barn-och-ungdom/***' --include='/kontakt/***' \
  --include='/medarbetare/***' --include='/om-oss/***' --include='/organisationer/***' \
  --include='/priser/***' --include='/vuxna/***' \
  --exclude='/assets/*/_src/' --exclude='/assets/img/_client/' --exclude='/assets/team/' \
  --exclude='*.md' --exclude='.DS_Store' \
  --include='/assets/***' \
  --exclude='*' \
  "$BUILD/" "$STAGE/"
echo "Built and staged $(find "$STAGE" -type f | wc -l) files, $(du -sh "$STAGE" | cut -f1)."

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

# 3. Keep what the server has put in its own .htaccess: cPanel's password
#    protection (staging) and cPanel's PHP-version block (live). Our upload
#    replaces the file, so those lines are carried over into ours.
ftp "set cmd:fail-exit no; cd \"$FTP_DIR\"; get .htaccess -o \"$WORK/remote.htaccess\"" >/dev/null 2>&1 || true
python3 - "$WORK/remote.htaccess" "$STAGE/.htaccess" "$TARGET" <<'PY'
import os, re, sys
remote, ours, target = sys.argv[1:4]
text = open(remote, encoding='utf-8', errors='replace').read() if os.path.exists(remote) else ''
kept, inside = [], False
for line in text.splitlines():
    if re.match(r'\s*#.*BEGIN cPanel-generated', line):
        inside = True
    if inside or re.match(r'\s*(AuthType|AuthName|AuthUserFile|AuthGroupFile)\b|\s*require\s+valid-user', line, re.I):
        kept.append(line)
    if re.match(r'\s*#.*END cPanel-generated', line):
        inside = False
if target == 'test' and not any(re.match(r'\s*AuthType', l, re.I) for l in kept):
    sys.exit("Could not read the password protection from staging's .htaccess. "
             "Uploading would remove it, so stopping.")
if kept:
    body = open(ours, encoding='utf-8').read()
    with open(ours, 'w', encoding='utf-8') as f:
        f.write("# Kept from the server's own .htaccess (password protection, cPanel PHP settings).\n"
                + '\n'.join(kept) + '\n\n' + body)
print(f"Kept {len(kept)} line(s) from the server's .htaccess." if kept
      else "The server has no .htaccess lines to keep.")
PY

if [ "$TARGET" = live ] && [ -z "$DRY" ]; then
  read -r -p "Upload to the LIVE site kbt-konsulterna.se? [y/N] " ok
  [ "$ok" = y ] || { echo "Cancelled."; exit 1; }
fi

# 4. Upload new and changed files.
ftp "mirror --reverse --only-newer --no-perms --parallel=4 --verbose=1 $DRY \"$STAGE/\" \"$FTP_DIR\""

if [ -n "$DRY" ]; then
  echo "Dry run: nothing was uploaded."
else
  echo "Done. Open the $TARGET site, click through, and send a test message from /kontakt/."
fi

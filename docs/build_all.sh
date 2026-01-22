#!/usr/bin/env bash
set -euo pipefail

# Build both Chinese (zh) and English (en) HTML docs.
# Source of truth: docs/source/**/*.rst (Chinese)
# English translations: docs/locale/en/LC_MESSAGES/**/*.po (and compiled .mo)
#
# Output:
# - docs/_build/html/zh
# - docs/_build/html/en

cd "$(dirname "$0")"

command -v sphinx-build >/dev/null 2>&1 || {
  echo "[ERROR] sphinx-build not found. Install deps (pip install -r requirements.txt)." >&2
  exit 1
}

command -v sphinx-intl >/dev/null 2>&1 || {
  echo "[ERROR] sphinx-intl not found. Install it (pip install sphinx-intl)." >&2
  exit 1
}

mkdir -p _build

echo "============================================================"
echo "[1/6] Cleaning build cache (doctrees + html outputs)"
echo "============================================================"
rm -rf _build/doctrees _build/html/zh _build/html/en _build/gettext

echo "============================================================"
echo "[2/6] Build Chinese HTML -> _build/html/zh"
echo "============================================================"
sphinx-build -E -a -b html -t zh source _build/html/zh

echo "============================================================"
echo "[3/6] Extract gettext catalogs -> _build/gettext"
echo "============================================================"
sphinx-build -E -a -b gettext -t zh source _build/gettext

echo "============================================================"
echo "[4/6] Update English PO files from gettext catalogs"
echo "============================================================"
sphinx-intl update -p _build/gettext -l en

echo "============================================================"
echo "[5/6] Compile English MO files"
echo "============================================================"
sphinx-intl build -l en

echo "============================================================"
echo "[6/6] Build English HTML -> _build/html/en"
echo "============================================================"
sphinx-build -E -a -b html -t en \
  -D language=en -D html_search_language=en \
  -D project="DAOAI Video Analysis Platform User Manual" \
  -D html_title="DAOAI Video Analysis Platform User Manual" \
  source _build/html/en

echo
echo "[OK] Done."
echo "- Chinese: $(pwd)/_build/html/zh/index.html"
echo "- English: $(pwd)/_build/html/en/index.html"


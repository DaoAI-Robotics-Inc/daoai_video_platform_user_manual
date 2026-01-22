@echo off
setlocal enabledelayedexpansion

REM Build both Chinese (zh) and English (en) HTML docs.
REM - Chinese source of truth: docs/source/**/*.rst
REM - English translations:     docs/locale/en/LC_MESSAGES/**/*.po
REM - Compiled catalogs:        docs/locale/en/LC_MESSAGES/**/*.mo
REM Output:
REM - docs/_build/html/zh
REM - docs/_build/html/en

cd /d "%~dp0"

REM Basic checks
where sphinx-build >NUL 2>NUL
if errorlevel 1 (
  echo [ERROR] sphinx-build not found. Please install Sphinx (pip install -r requirements.txt)
  exit /b 1
)

where sphinx-intl >NUL 2>NUL
if errorlevel 1 (
  echo [ERROR] sphinx-intl not found. Please install sphinx-intl (pip install sphinx-intl)
  exit /b 1
)

REM Ensure build directory exists (helps when redirecting output to files)
if not exist "_build" mkdir "_build"

echo ============================================================
echo [1/6] Cleaning build cache (doctrees + html outputs)
echo ============================================================
if exist "_build\doctrees" rmdir /s /q "_build\doctrees"
if exist "_build\html\zh" rmdir /s /q "_build\html\zh"
if exist "_build\html\en" rmdir /s /q "_build\html\en"
if exist "_build\gettext" rmdir /s /q "_build\gettext"

echo ============================================================
echo [2/6] Build Chinese HTML -> _build\html\zh
echo ============================================================
sphinx-build -E -a -b html -t zh source _build\html\zh
if errorlevel 1 (
  echo [ERROR] Chinese HTML build failed.
  exit /b 1
)

echo ============================================================
echo [3/6] Extract gettext catalogs -> _build\gettext
echo ============================================================
sphinx-build -E -a -b gettext -t zh source _build\gettext
if errorlevel 1 (
  echo [ERROR] Gettext extraction failed.
  exit /b 1
)

echo ============================================================
echo [4/6] Update English PO files from gettext catalogs
echo ============================================================
sphinx-intl update -p _build\gettext -l en
if errorlevel 1 (
  echo [ERROR] sphinx-intl update failed.
  exit /b 1
)

echo ============================================================
echo [5/6] Compile English MO files
echo ============================================================
sphinx-intl build -l en
if errorlevel 1 (
  echo [ERROR] sphinx-intl build failed.
  exit /b 1
)

echo ============================================================
echo [6/6] Build English HTML -> _build\html\en
echo ============================================================
sphinx-build -E -a -b html -t en -D language=en -D html_search_language=en -D project="DAOAI Video Analysis Platform User Manual" -D html_title="DAOAI Video Analysis Platform User Manual" source _build\html\en
if errorlevel 1 (
  echo [ERROR] English HTML build failed.
  exit /b 1
)

echo.
echo [OK] Done.
echo - Chinese: %cd%\_build\html\zh\index.html
echo - English: %cd%\_build\html\en\index.html
echo.
endlocal


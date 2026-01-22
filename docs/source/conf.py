# Configuration file for the Sphinx documentation builder.
#
# This project uses the "docs/source" layout:
# - source files in docs/source
# - build output in docs/_build
# - translations in docs/locale/<lang>/LC_MESSAGES

# -- Project information -----------------------------------------------------

project = "DaoAI 天眼系统用户手册"
copyright = "2021-2025 DaoAI Robotics Inc."
author = "DaoAI"

release = "2025.5"
version = "2025.5.0"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
    "sphinxcontrib.video",
    "sphinx.ext.autosectionlabel",
    "sphinxemoji.sphinxemoji",
    "sphinx_multiversion",
    "sphinx_design",
]

templates_path = ["_templates"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_show_sourcelink = False

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

# Default (Chinese) build. Override per-build with:
#   sphinx-build ... -D language=en -D html_search_language=en
language = "zh_CN"
html_search_language = "zh"


# -- Options for EPUB output -------------------------------------------------

epub_show_urls = "footnote"


# -- Options to Support pdf build in chinese --------------------------------

latex_engine = "lualatex"
latex_elements = {
    "preamble": "\\usepackage[UTF8]{ctex}\n",
}


# -- i18n --------------------------------------------------------------------
# Translations live in docs/locale (one level above this conf.py)

locale_dirs = ["../locale"]
gettext_compact = False


# -- sphinx-multiversion -----------------------------------------------------

smv_branch_whitelist = r"^(?!chinese).*$"


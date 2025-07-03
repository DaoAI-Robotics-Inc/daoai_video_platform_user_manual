# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '天眼系统用户手册'
copyright = '2025, DaoAI'
author = 'DaoAI'
release = '2025.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs',
    'sphinxcontrib.video',
    'sphinx.ext.autosectionlabel',
    'sphinxemoji.sphinxemoji',
    "sphinx_multiversion",
]

templates_path = ['_templates']
html_css_files = [
    'css/custom.css',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
exclude_patterns = []

# -- Options for HTML output
language = 'zh_CN'
html_search_language = 'zh'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options to Support pdf build in chinese
latex_engine = 'lualatex'
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}

# sphinx-multiversion
# All branches except 'master'
smv_branch_whitelist = r'^(?!chinese).*$'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

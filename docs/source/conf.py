# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DaoAI 天眼系统用户手册'
copyright = '2021-2025 DaoAI Robotics Inc.'
author = 'DaoAI'

release = '2025.5'
version = '2025.5.0'

# -- General configuration

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

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

# -- Options for HTML output
language = 'zh_CN'
html_search_language = 'zh'

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options to Support pdf build in chinese
latex_engine = 'lualatex'
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}


html_theme = 'sphinx_rtd_theme'

latex_engine = 'lualatex'
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}
epub_show_urls = 'footnote'

templates_path = [
    "_templates",
]

# sphinx-multiversion
# All branches except 'master'
smv_branch_whitelist = r'^(?!chinese).*$'
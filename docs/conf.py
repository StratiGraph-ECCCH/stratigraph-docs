# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'StratiGraph documentation'
copyright = '2026, Emanuel Demetrescu (CNR-ISPC) and the StratiGraph consortium'
author = 'Emanuel Demetrescu'

release = '1.6'
version = '1.6.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    # the pages of the ecosystem's documentation are markdown
    'myst_parser',
]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
myst_enable_extensions = ['deflist', 'colon_fence', 'fieldlist', 'substitution']
myst_heading_anchors = 3

templates_path = ['_templates']
html_static_path = ['_static']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    # reusable RST snippets, pulled in with `.. include::`, never pages
    '_includes/**',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_title = 'StratiGraph documentation'

# The brand, vendored from `stratigraph-brand` by its own
# `docs-theme/sync-brand-docs.sh`, exactly as the apps vendor it: a manual read
# in a trench has no CDN. Without `skins.css` the manual wears the StratiGraph
# guidebook; the Extended Matrix manuals ship that file and wear EM instead.
# Light and dark follow the reader's system setting.
# EPUB non conosce il tipo di un .woff2 e, con -W, la sua lamentela
# («unknown mimetype … ignoring») ferma la pubblicazione: i caratteri del
# marchio servono alla pagina web, non al libro.
suppress_warnings = ['epub.unknown_project_files']

html_css_files = [
    'brand/stratigraph-theme.css',
    'brand/sphinx-rtd-bridge.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

numfig = True

# -- AI Act Article 50 transparency footer -----------------------------
# A short notice appended to every page via ``rst_epilog``, pointing to
# the project's AI usage policy at extendedmatrix.org/ai-usage/.
rst_epilog = """
.. include:: /_includes/ai_usage_notice.rst
"""

import sphinx_bootstrap_theme
import myst_nb
import jupytext

# import cloud_sptheme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mathpax Blog'
copyright = '2024, Karl Hoitsma'
author = 'K. Hoitsma '
# release = '0.1 '

html_logo = 'https://khoitsmahq.firstcloudit.com/images/mp_small3.png'
# html_theme = 'sphinx13'

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,
    # 'logo_only': False,
    'prev_next_buttons_location': 'top',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    'flyout_display': 'hidden',
    'version_selector': True,
    'language_selector': True,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'restructuredtext',
#     '.md': 'markdown',
# }
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.md': 'myst-nb'
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []
extensions = ['myst_nb']

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = []

nb_execution_mode = "force"
nb_execution_timeout = 60
execution_show_tb = True
myst_heading_anchors = 7

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Activate the standard theme.
# html_theme = 'alabaster'
# html_static_path = ['_static']

# Activate an alternate theme.
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Activate an alternate theme.
# html_theme = 'classic'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# html_theme = "sphinx_book_theme"

# html_theme_options = {
#     # Disable showing the sidebar. Defaults to 'false'
#     'nosidebar': False,
# }

# # Configuration file for the Sphinx documentation builder.
# #
# # For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# project = 'Example'
# copyright = 'workshop participant'
# author = 'workshop participant'
# release = '0.1'


# # -- General configuration ---------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['myst_parser']

# templates_path = ['_templates']
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# # -- Options for HTML output -------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

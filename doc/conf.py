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
author = 'K. Hoitsma'
# release = '0.1 '

html_logo = 'https://khoitsmahq.firstcloudit.com/images/mp_small3.png'
# html_theme = 'sphinx13'

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

templates_path = ['_templates']
exclude_patterns = []

jupytext --set-kernel - notebook.md

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

html_theme = "sphinx_book_theme"

html_theme_options = {
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': False,
}

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

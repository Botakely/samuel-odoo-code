# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Odoo Code'
copyright = '2022, Samuel RAMAROSELY'
author = 'Samuel RAMAROSELY'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_logo = "_static/odoo-code-icon.png"
html_favicon = "_static/odoo-code-icon.png"
html_theme_options = {
    'display_version': False,
    "style_nav_header_background": "#01939A",
}

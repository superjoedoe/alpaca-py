# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../"))

# -- Project information -----------------------------------------------------

project = "alpaca-py"
copyright = "2022, Alpaca"
author = "Alpaca"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    'sphinx_copybutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = 'python'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Furo theme - https://github.com/pradyunsg/furo
# Default css color variables used by the theme are listed below commented out.
#
html_theme = "furo"
html_favicon = 'https://files.alpaca.markets/webassets/favicon-32x32.png'
html_theme_options = {
    "light_css_variables": {
        # Fonts
        "font-stack": "'Carnas', sans-serif",
        # "font-stack--monospace": "'SFMono-Regular', Menlo, Consolas, Monaco, Liberation Mono, Lucida Console, monospace",
        
        # Base Colors
        "color-foreground-primary": "#000", # for main text and headings
        "color-foreground-secondary": "#010101", # for secondary text
        "color-foreground-muted": "#5D6065", # for muted text
        "color-foreground-border": "#878787", # for content borders
        # "color-background-primary": "white", # for content
        # "color-background-secondary": "#f8f9fb", # for navigation + ToC
        # "color-background-hover": "#efeff4ff", # for navigation-item hover
        # "color-background-hover--transparent": "#efeff400",
        # "color-background-border": "#eeebee", # for UI borders
        # "color-background-item": "#ccc", # for "background" items (eg: copybutton)

        # Announcements
        # "color-announcement-background": "#000000dd",
        # "color-announcement-text": "#eeebee",

        # Brand colors
        "color-brand-primary": "#F9D849",
        "color-brand-content": "#010101",

        # API documentation
        # "color-api-background": "var(--color-background-secondary)",
        # "color-api-background-hover": "var(--color-background-hover)",
        # "color-api-overall": "var(--color-foreground-secondary)",
        # "color-api-name": "var(--color-problematic)",
        # "color-api-pre-name": "var(--color-problematic)",
        # "color-api-paren": "var(--color-foreground-secondary)",
        # "color-api-keyword": "var(--color-foreground-primary)",
        # "color-highlight-on-target": "#ffffcc",

        # Inline code background
        # "color-inline-code-background": "var(--color-background-secondary)",
        # Highlighted text (search)
        # "color-highlighted-background": "#ddeeff",
        # "color-highlighted-text": "var(--color-foreground-primary)",

        # GUI Labels
        # "color-guilabel-background": "#ddeeff80",
        # "color-guilabel-border": "#bedaf580",
        # "color-guilabel-text": "var(--color-foreground-primary)",

        # Admonitions!
        # "color-admonition-background": "transparent",
        # "color-problematic": "#b30000",

        #
        # Everything below this should be one of:
        # - var(...)
        # - *-gradient(...)
        # - special literal values (eg: transparent, none)
        #

        # Tables
        # "color-table-header-background": "var(--color-background-secondary)",
        # "color-table-border": "var(--color-background-border)",

        # Cards
        # "color-card-border": "var(--color-background-secondary)",
        # "color-card-background": "transparent",
        # "color-card-marginals-background": "var(--color-background-secondary)",

        # Header
        # "color-header-background": "var(--color-background-primary)",
        # "color-header-border": "var(--color-background-border)",
        # "color-header-text": "var(--color-foreground-primary)",

        # Sidebar (left)
        #"color-sidebar-background": "var(--color-background-primary)",
        #"color-sidebar-background-border": "transparent",

        # "color-sidebar-brand-text": "var(--color-foreground-primary)",
        # "color-sidebar-caption-text": "var(--color-foreground-muted)",
        # "color-sidebar-link-text": "var(--color-foreground-secondary)",
        "color-sidebar-link-text--top-level": "var(--color-foreground-primary)",

        # "color-sidebar-item-background": "var(--color-sidebar-background)",
        # "color-sidebar-item-background--current": "var(--color-sidebar-item-background)",
        # "color-sidebar-item-background--hover": "linear-gradient(90deg,var(--color-background-hover--transparent) 0%,var(--color-background-hover) var(--sidebar-item-spacing-horizontal),var(--color-background-hover) 100%)",

        # "color-sidebar-item-expander-background": "transparent",
        # "color-sidebar-item-expander-background--hover": "var(--color-background-hover)",

        # "color-sidebar-search-text": "var(--color-foreground-primary)",
        # "color-sidebar-search-background": "var(--color-background-secondary)",
        # "color-sidebar-search-background--focus": "var(--color-background-primary)",
        # "color-sidebar-search-border": "var(--color-background-border)",
        # "color-sidebar-search-icon": "var(--color-foreground-muted)",

        # Table of Contents (right)
        # "color-toc-background": "var(--color-background-primary)",
        # "color-toc-title-text": "var(--color-foreground-muted)",
        # "color-toc-item-text": "var(--color-foreground-secondary)",
        # "color-toc-item-text--hover": "var(--color-foreground-primary)",
        # "color-toc-item-text--active": "var(--color-brand-primary)",

        # Actual page contents
        # "color-content-foreground": "var(--color-foreground-primary)",
        # "color-content-background": "transparent",

        # Links
        "color-link": "#0055BB",
        "color-link--hover": "#0055BB80",
        "color-link-underline": "transparent",
        "color-link-underline--hover": "#0055BB80",
    },
    "dark_css_variables": {
        # Fonts
        "font-stack": "'Carnas', sans-serif",
        # "font-stack--monospace": "'SFMono-Regular', Menlo, Consolas, Monaco, Liberation Mono, Lucida Console, monospace",
        
        # Base Colors
        "color-foreground-primary": "#ffffff", # for main text and headings
        "color-foreground-secondary": "#f7f7f7", # for secondary text
        # "color-foreground-muted": "#81868d", # for muted text
        # "color-foreground-border": "#666666", # for content borders
        # "color-background-primary": "#131416", # for content
        # "color-background-secondary": "#1a1c1e", # for navigation + ToC
        # "color-background-hover": "#1e2124ff", # for navigation-item hover
        # "color-background-hover--transparent": "#1e212400",
        # "color-background-border": "#303335", # for UI borders
        # "color-background-item": "#444", # for "background" items (eg: copybutton)

        # Announcements
        # "color-announcement-background": "#000000dd",
        # "color-announcement-text": "#eeebee",

        # Brand colors
        # "color-brand-primary": "#2b8cee",
        # "color-brand-content": "#368ce2",

        # Highlighted text (search)
        # "color-highlighted-background": "#083563",

        # GUI Labels
        # "color-guilabel-background": "#08356380",
        # "color-guilabel-border": "#13395f80",
        # API documentation
        # "color-api-keyword": "var(--color-foreground-secondary)",
        # "color-highlight-on-target": "#333300",

        # Admonitions
        # "color-admonition-background": "#18181a",
        # "color-problematic": "#ee5151",

        # Cards
        # "color-card-border": "var(--color-background-secondary)",
        # "color-card-background": "#18181a",
        # "color-card-marginals-background": "var(--color-background-hover)",

        # Links
        "color-link": "#D5C1FF",
        "color-link--hover": "#D5C1FF90",
        "color-link-underline": "transparent",
        "color-link-underline--hover": "#D5C1FF90",
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# currently unused but uncomment in the future
# html_static_path = ['_static']

pygments_style = 'monokai'
pygments_dark_style = 'monokai'

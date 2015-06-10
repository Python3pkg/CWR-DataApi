#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CWR-API documentation build configuration file.

import ast
import re
import sys
import os
from codecs import open
from os import path

# -- Version --------------------------------------------------------------

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Path to the project's root
here = path.abspath(path.dirname(__file__))

# Gets the version for the source folder __init__.py file
with open('../../cwr/__init__.py', 'rb', encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))


# -- Code location --------------------------------------------------------

sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('../../cwr'))


# -- General configuration ------------------------------------------------

# Sphinx extensions
#
# autodoc: generates documentation from docstrings
# intersphinx: generates links to other Sphinx-created docs
# viewcode: generates HTML from code sources
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# Templates.
templates_path = ['_templates']

# Only reStructuredText is accepted
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Sort members by type
autodoc_member_order = 'groupwise'

# General information about the project.
project = 'CWR-API'
copyright = '2015, WESO'
authors = ['Bernardo Martinez Garrido']

# The version info for the project.
#
# Semantic version value.
version = version_lib
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

try:
    import sphinx_bootstrap_theme
except:
    from warnings import warn

    warn("I would like to use the sphinx bootstrap theme, but can't find it.\n"
         "'pip install sphinx_bootstrap_theme' to fix.")
else:
    # Activate the theme.
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

    # Theme options.
    html_theme_options = {
        'navbar_fixed_top': 'true',
        'navbar_site_name': 'Contents',
        'bootstrap_version': '3',
        'source_link_position': 'nav',
        'bootswatch_theme': "sandstone",
    }

# Custom static files folder.
html_static_path = ['_static']

# Favicon
html_favicon = '_static/favicon.ico'

# Custom sidebars
html_sidebars = {'index': ['status.html']}

# Output file base name for HTML help builder.
htmlhelp_basename = '%s doc' % project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# List of LaTeX documents.
latex_documents = [
    (master_doc, '%s.tex' % project, '%s Documentation' % project,
     ','.join(authors), 'manual'),
]


# -- Options for manual page output ---------------------------------------

# List of manual pages.
man_pages = [
    (master_doc, project, '%s Documentation' % project,
     [','.join(authors)], 1)
]


# -- Options for Texinfo output -------------------------------------------

# List of Texinfo documents.
texinfo_documents = [
    (master_doc, project, '%s Documentation' % project,
     ','.join(authors), project, 'API library for the CWR standard format.',
     'Miscellaneous'),
]


# -- Intersphinx links ----------------------------------------------------

# Intersphinx mapping.
intersphinx_mapping = {
    'https://docs.python.org/': None,
}

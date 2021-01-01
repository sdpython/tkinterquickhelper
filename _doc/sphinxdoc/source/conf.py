# -*- coding: utf-8 -*-
"""
@file
@brief Configuration for sphinx documentation.
"""
import sys
import os
import solar_theme
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "tkinterquickhelper", "Xavier Dupré", 2021,
                     "solar_theme", solar_theme.theme_path, locals(),
                     github_repo="https://github.com/sdpython/tkinterquickhelper.git",
                     extlinks=dict(issue=(
                         'https://github.com/sdpython/tkinterquickhelper/issues/%s', 'issue {0} on GitHub')),
                     link_resolve="http://www.xavierdupre.fr/app/")

html_logo = "phdoc_static/project_ico.png"

# there is an issue with this attribute on Anaconda math_number_all
assert math_number_all or not math_number_all
blog_root = "http://www.xavierdupre.fr/app/tkinterquickhelper/helpsphinx/"

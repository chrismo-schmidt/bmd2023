#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

SITENAME = 'Bicycle & Motorcycle Dynamics 2023'

# TODO : Theme puts the author's name below the logo, should put sitename (i.e.
# it assumes this is a blog).
AUTHOR = SITENAME
SITENAME = SITENAME
SITEURL = ''
SOURCEURL = 'https://github.com/mechmotum/bmd2023'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# This sets the default pages to be top level items and articles to be under
# /news/.
INDEX_SAVE_AS = 'news/index.html'

# All news posts will have slugs that match the file name.
PATH_METADATA = '(?P<path_no_ext>.*)\..*'  # regex to grab file name without ext
ARTICLE_URL = 'news/{path_no_ext}.html'
ARTICLE_SAVE_AS = 'news/{path_no_ext}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'sortorder'

MENUITEMS = [('News', 'news/')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

try:
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file, Loader=yaml.FullLoader)
except IOError:
    THEME = ''
    PLUGIN_PATHS = ['']
else:
    THEME = config_data['THEME_PATH']
    PLUGIN_PATHS = config_data['PLUGIN_PATHS']
    if isinstance(PLUGIN_PATHS, type('')):
        PLUGIN_PATHS = [PLUGIN_PATHS]

## THEME

# Alchemy theme settings
DISQUS_SITENAME = ""
SITESUBTITLE = ('Symposium on the Dynamics and Control of Single Track Vehicles '
    '<br> 18-20 October 2023, Delft University of Technology, Delft, Netherlands')
SITEIMAGE = 'https://bmdconf.org/images/bmd-ver-logo-200x275.png'
# INSTITUTEIMAGE should bee 100px in height
#INSTITUTIONIMAGE = 'https://objects-us-east-1.dream.io/mechmotum/tu-delft-logo-233x100.png'
DESCRIPTION = ''
# pelican-alchemy removed the original theme.css, so bring it back.
THEME_CSS_OVERRIDES = ['theme/css/origtheme.css']
REPO_URL = 'https://github.com/mechmotum/bmd2023.github.io'
# TODO : Fix the template so that if this isn't declared it still builds.
EXCLUDED_CATEGORIES = []

#GOOGLE_ANALYTICS = ''
#DISQUS_SITENAME = ''

## PLUGINS

PLUGINS = ['render_math', 'extract_toc']

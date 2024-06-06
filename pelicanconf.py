#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Markus'
SITENAME = 'Blog of Markus'
# Default, do not set here something (change in publishconf.py)
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# path-specific metadata
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'}, 
    'static/CNAME': {'path': 'CNAME'},
    'static/.nojekyll': {'path': '.nojekyll'},
    }

# Static files
STATIC_PATHS = [
    'images',
    'static',
    ]

MENUITEMS = [('Home', '/'), ('Archives', '/archives.html')]

# pelican-themes
THEME = "themes/attila"

# Can set individual COVERS
#
# See site index.html (SITEURL has to be defined)
HOME_COVER = 'images/home_cover/PSX_20200814_222941.jpg'   #PSX_20200814_222941.jpg   #IMG_20211009_173919.jpg
#
#HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
#HOME_COLOR = 'green'

# https://stackoverflow.com/questions/51072113/pelican-how-can-i-render-html-pages-instead-of-markup
# But files into /markus-goller/themes/attila/templates
DIRECT_TEMPLATES = [
    'index', 'categories', 'authors', 'archives',  # (default)
    'first_map', 'map_with_luba2', 'map_ext', 'bike_tour_berlin_map'   # Other HTML template to render 
    ]

# https://stackoverflow.com/questions/18520046/how-can-i-control-the-order-of-pages-from-within-a-pelican-article-category
# https://docs.getpelican.com/en/latest/settings.html#ordering-content
ARTICLE_ORDER_BY = 'attribute'
PAGE_ORDER_BY = 'attribute'
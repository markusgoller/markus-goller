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

# https://stackoverflow.com/questions/51072113/pelican-how-can-i-render-html-pages-instead-of-markup
DIRECT_TEMPLATES = [
    'index', 'categories', 'authors', 'archives',  # (default)
    'first_map'  # other HTML template to render
    ]

# pelican-themes
THEME = "themes/attila"

# Can set individual COVERS
#
# See site index.html (SITEURL has to be defined)
HOME_COVER = 'images/home_cover/PSX_20200814_222941.jpg'   #PSX_20200814_222941.jpg   #IMG_20211009_173919.jpg
#
#HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
#HOME_COLOR = 'green'

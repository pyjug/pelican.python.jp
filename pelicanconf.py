#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'python.jp'
SITENAME = 'python.jp'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = 'ja'

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

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "theme"
FILENAME_METADATA = "(?P<slug>.*)"
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS  = '{category}/{slug}.html'

DEFAULT_CATEGORY = "news"
DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 2

PAGINATION_PATTERNS = [
    (1, '{name}{number}.html', '{name}{number}.html'),
    (2, '{name}_{number}.html', '{name}_{number}.html'),
]

STATIC_PATHS = ['images', 'images/favicon.ico', 'cgi-bin']
EXTRA_PATH_METADATA = {
        'images/favicon.ico': {'path': 'favicon.ico'},
}


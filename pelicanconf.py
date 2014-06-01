#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'python.jp maintainers'
SITENAME = 'python.jp'
SITEURL = ''

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
DEFAULT_DATE_FORMAT = '%Y-%m-%d (%a) %H:%M'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None



FILENAME_METADATA = "(?P<slug>.*)"
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS  = '{category}/{slug}.html'

DEFAULT_CATEGORY = "news"
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

THEME = "theme"

RELATIVE_URLS=True


PAGINATION_PATTERNS = [
    (1, '{name}{number}.html', '{name}{number}.html'),
    (2, '{name}_{number}.html', '{name}_{number}.html'),
]

STATIC_PATHS = ['images', 'images/favicon.ico', 'cgi-bin']
EXTRA_PATH_METADATA = {
        'images/favicon.ico': {'path': 'favicon.ico'},
}



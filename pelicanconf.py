#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'suphy'
SITENAME = u'suphy\' Blog'
#SITEURL = 'http://suphy2009.github.io'
SITEURL = 'http://localhost:8000'

GITHUB_URL = 'https://github.com/suphy2009'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
    'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_LANG = u'zh_CN'
DEFAULT_PAGINATION = 6

#使用目录名作为文章的分类名
USE_FOLDER_AS_CATEGORY = True
#DELETE_OUTPUT_DIRECTORY = True
#DEFAULT_CATEGORY = 'uncategorized'
#使用文件名作为文章或页面的slug
FILENAME_METADATA = '(?P<slug>.*)'

# feed config
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

#THEME = 'tuxlite_tbs'
#THEME = 'bootstrap2'
THEME = 'pelican-themes/tuxlite_tbs'

RELATIVE_URLS = True
#DISPLAY_CATEGORIES_ON_MENU = True

DISQUS_SITENAME = 'suphy2009'

GOOGLE_ANALYTICS = 'UA-47831467-1'

MD_EXTENSIONS = (['codehilite(css_class=highlight)', 'extra', 'fenced_code', 'tables', 'sane_lists'])

READERS = {
        'html': None,
}
#STATIC_SAVE_AS = "static/"
#拷贝静态目录 Pelican 就会将img目录拷贝到 output/static/
STATIC_PATHS = [
        'static',
        'extra',
        ]

#拷贝静态文件
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': { 'path': 'favicon.ico' },
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/googlec0086f9e29fad494.html': {'path': 'googlec0086f9e29fad494.html' },
    }

PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap", "summary"]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

LINKS =  (('Google', 'https://www.google.com/ncr'),
          ('Python', 'http://python.org/'),
          ('Pelican', 'http://docs.getpelican.com/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/suphy2009'),
          ('Facebook', 'https://www.facebook.com/profile.php?id=100003251594803'),
          ('Linkedin', 'http://www.linkedin.com/profile/view?id=273447004'),
          (u'微博', 'http://weibo.com/suphy2010'),
          (u'知乎', 'http://www.zhihu.com/people/suphy'),
          (u'豆瓣', 'http://www.douban.com/people/suphy2009'),
         )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

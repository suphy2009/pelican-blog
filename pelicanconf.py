#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'suphy'
SITENAME = u'suphy\' Blog'
SITEURL = 'http://suphy2009.github.io'
#SITEURL = 'http://localhost:8000'
#GITHUB_URL = 'https://github.com/suphy2009'

ADDRESS = 'Hangzhou.China'
MAIL = 'bww0815@gmail.com'
GOOGLEPLUS_USER='https://plus.google.com/u/0/113100105918853159511'
LINKEDIN_USER = 'http://www.linkedin.com/profile/view?id=273447004'
FACEBOOK_USER = 'https://www.facebook.com/profile.php?id=100003251594803'
ABOUT_TEXT = "About"
ABOUT_LINK = 'about.html'

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
DEFAULT_CATEGORY = 'uncategorized'
#使用文件名作为文章或页面的slug
FILENAME_METADATA = '(?P<slug>.*)'

ARCHIVES_URL = 'archives.html'
CATEGORIES_URL = 'categories.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

# feed config
#FEED_DOMAIN = SITEURL

#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

#THEME = 'pelican-themes/bootstrap2'
#THEME = 'pelican-themes/pelican-bootstrap3'
THEME = 'pelican-themes/tuxlite_tbs'
#THEME = 'pelican-themes/html5-dopetrope'
#THEME = 'pelican-themes/blueidea'
#THEME = '/Users/suphy/bak/pelican-themes/pelican-mockingbird'
#THEME = '/Users/suphy/bak/pelican-themes/pelican-simplegrey'
#MD_EXTENSIONS = (['codehilite(css_class=codehilite)', 'extra', 'fenced_code', 'tables', 'sane_lists'])

RELATIVE_URLS = True

DISQUS_SITENAME = 'suphy2009'

GOOGLE_ANALYTICS = 'UA-47831467-1'

GOOGLE_CUSTOM_SEARCH_SIDEBAR = '010153636864527898055:f3thbiahdzi'

READERS = {
        'html': None,
}
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
PLUGINS = ["sitemap", "summary", "related_posts"]

# For Related posts
RELATED_POSTS_MAX = 5

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


#################For blueidea Theme###########################
# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = True

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = True

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False

# Display the search form
DISPLAY_SEARCH_FORM =True

# Sort pages list by a given attribute
#PAGES_SORT_ATTRIBUTE = 'Title'

#################For pelican-bootstrap3 Theme###########################
PYGMENTS_STYLE = 'solarizeddark'
#Breadcrumbs
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
# NavBar
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISQUS_NO_ID = True
DISQUS_ID_PREFIX_SLUG = True
DISQUS_DISPLAY_COUNTS = True

LINKS =  (('Google', 'https://www.google.com/ncr'),
          ('Python', 'http://python.org/'),
          ('Pelican', 'http://docs.getpelican.com/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/suphy2009'),
          ('Facebook', 'https://www.facebook.com/profile.php?id=100003251594803'),
          ('Linkedin', 'http://www.linkedin.com/profile/view?id=273447004'),
          (u'微博', 'http://weibo.com/suphy2010'),
         # (u'知乎', 'http://www.zhihu.com/people/bai-wan-wei'),
         # (u'豆瓣', 'http://www.douban.com/people/suphy2009'),
         )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

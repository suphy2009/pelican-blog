Date: 2014-02-06
Title: (转) 用 Pelican 和 GitHub Pages 搭建个人博客
Category: Tech
Tags: pelican, blog, python
Slug: build_blog
Summery: 用 Pelican 和 GitHub Pages 搭建免费的个人博客

### Pelican 介绍

首先看看Pelican的一些主要特性：

   - Python实现，开放源码  
   - 输出静态页面，方便托管  
   - 支持主题，采用Jajin2模板引擎  
   - 支持代码语法高亮  
   - 支持reStructuredText、Markdown、AsciiDoc格式  
   - 支持Disqus评论  
   - 支持Atom和RSS输出  
###为什么不选择CSDN、Wordpress、Jekyll等技术

Wordpress上手容易、功能强大、插件丰富。但是在我看来，这些优点同时也是它的缺点：太笨重、太无脑、不够酷、无用功能太多、可定制的粒度不够小。我更喜欢简洁快速粗暴的博客系统。

Jekyll非常棒，可惜它基于Ruby。对于Python爱好者而言，基于Python的Pelican显然更加可口。
###Github入门指南
请参考<http://blog.csdn.net/duxinfeng2010/article/details/8654690>

###安装Pelican和Markdown
    pip install pelican
    pip install markdown

###搭建骨架
    mkdir blog
    cd blog
    pelican-quickstart

根据提示一步步输入相应的配置项，不知道如何设置的接受默认即可，后续可以通过编辑pelicanconf.py文件更改配置)

以下是生成的目录结构：
    
    blog/
    ├── content              # 存放输入的源文件
    │   └── (pages)          # 存放手工创建的静态页面
    ├── output               # 生成的输出文件
    ├── develop_server.sh    # 方便开启测试服务器
    ├── Makefile             # 方便管理博客的Makefile
    ├── pelicanconf.py       # 主配置文件
    └── publishconf.py       # 主发布文件，可删除

###开始写博文
在content目录下用Markdown语法来写一篇文章，最好选择专业的Markdown编辑器，在Mac OS X下推荐使用Mou，在Linux/Windows下请Google。

    Title: My super title
    Date: 2014-02-03 10:20
    Category: Python
    Tags: pelican, publishing
    Slug: my-super-post
    Author: Alexis Metaireau
    Summary: Short version for index and feeds
    
    This is the content of my super blog post.

写完后，执行以下命令 `make html`，现在可以在output目录下查看生成的html文件了。

###创建Github Pages
GitHub Pages分两种，一种是项目页面，可创建多个；另一种是用户页面，每个用户ID只能创建一个。两种都可以用来托管Pelican博客，这里以用户页面为例。

* 登陆Github，创建一个名为**username**.github.io或者**username**.github.com的Repository（将username替换成自己的Github账户名）。
* 点击Setting，选择一个自己喜欢的模板，最后点击发布public按钮。
* 耐心等待一段时间（不超过10分钟），登陆http://username.github.io，会发现自己的个人博客已经生成。

创建成功后，便可以把生成的页面push到github。

    cd output
    git init
    git add .
    git commit -m "first commit"
    git remote add origin https://github.com/xxx/xxx.github.io.git
    git push -u origin master

现在可以通过username.github.io或者username.github.com来访问您的博客了。

##如虎添翼
* * *
我们已经能成功地用markdown写出博文并部署到github了，但这远远不够。

###管理图片
我觉得使用云相册比本地图片要方便的多，我使用[Picasa](https://picasaweb.google.com?noredirect=1)来维护blog的所有图片。

###挑选主题
安装主题，比如bootstrap2：

    git clone https://github.com/getpelican/pelican-themes.git
    cd pelican-themes
    pelican-themes -i bootstrap2

选择主题，在pelicanconf.py中添加
    
    THEME = 'bootstrap2'

###安装第三方评论系统
在[Disqus](https://disqus.com/admin/signup)上申请一个站点，记牢Shortname。
在pelicanconf.py添加
    
    DISQUS_SITENAME = Shortname

 
###添加Google Analytics
去[Google Analytics](http://www.google.com/analytics)申请账号，记下跟踪ID。
在pelicanconf.py添加
    
    GOOGLE_ANALYTICS = 跟踪ID

###使用Google Webmasters
在[Google Webmasters](http://www.google.com/webmasters)上注册即可。

这个就是Google站长工具，使用它的目的是为了让博客被Google更好的收录，比如手动让Googlebot抓取、提交Robots、更新Sitemap等等，各方面完爆百度站长工具。

###添加插件
    git clone git://github.com/getpelican/pelican-plugins.git
比如我要使用sitemap，在pelicanconf.py里配置如下
    
    PLUGIN_PATH = u"pelican-plugins"
    PLUGINS = ["sitemap"]
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

###使用Google站内搜索
请参考<http://www.codenut.net/post/2013-06-30-cse>

###申请独立域名
* 在[Godaddy](https://www.godaddy.com)上用支付宝花购买为期一年的顶级域名，并去修改Nameservers为这两个地址：f1g1ns1.dnspod.net、f1g1ns2.dnspod.net。
* 在[Dnspod](https://www.dnspod.cn)上添加新域名，并申请一条A记录指向Github Pages的ip:207.97.227.245；
* 在Pelican主目录新建CNAME文件，添上刚刚申请的域名，如我的www.lizherui.com

##登峰造极
* * *
最后，如果感觉还不够味儿，可以参考Pelican官方文档和这个博客的完整源码。

Pelican官方文档 : <http://docs.getpelican.com/en/3.2>

Pelican文档中文版: <https://pelican-docs-chs.readthedocs.org/en/latest/>

Source Code : <https://github.com/lizherui/lizherui.github.io> 

Have fun!

[转载](http://www.lizherui.com/pages/2013/08/17/build_blog.html)






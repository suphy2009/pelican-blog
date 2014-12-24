Title: Linux curl命令
Date: 2014-03-09 17:37
Category: linux
Tags: linux
Slug: linux_main_curl

Linux curl命令是一个功能强大的网络工具，它能够通过http、ftp等方式下载文件，也能够上传文件。其实curl远不止，类似的工具还有wget。

Linux curl命令使用了libcurl库来实现，libcurl库常用在C程序中用来处理HTTP请求，curlpp是libcurl的一个C++封装，这几个东西可以用在抓取网页、网络监控等方面的开发，而curl命令可以帮助来解决开发过程中遇到的问题。

### curl命令常用参数：
```
-A或--user-agent                :随意指定自己这次访问所宣称的自己的浏览器信息
-b/--cookie <name=string/file>  :cookie字符串或文件读取位置，使用option来把上次的cookie信息追加到http request里面去。
-c/--cookie-jar <file>          :操作结束后把cookie写入到这个文件中
-C/--continue-at <offset>       :断点续转
-d/--data <data>                :HTTP POST方式传送数据
-D/--dump-header <file>         :把header信息写入到该文件中
-F/--form <name=content>        :模拟http表单提交数据
-v/--verbose                    :小写的v参数，用于打印更多信息，包括发送的请求信息，这在调试脚本是特别有用。
-m/--max-time <seconds>         :指定处理的最大时长
-H/--header <header>            :指定请求头参数
-s/--slient                     :减少输出的信息，比如进度
--connect-timeout <seconds>     :指定尝试连接的最大时长
-x/--proxy <proxyhost[:port]>   :指定代理服务器地址和端口，端口默认为1080
-T/--upload-file <file>         :指定上传文件路径
-o/--output <file>              :指定输出文件名称
--retry <num>                   :指定重试次数
-e/--referer <URL>              :指定引用地址
-I/--head                       :仅返回头部信息，使用HEAD请求
-u/--user <user[:password]>     :设置服务器的用户和密码
-O   :按照服务器上的文件名，自动存在本地
-r/--range <range>              :检索来自HTTP/1.1或FTP服务器字节范围
-T/--upload-file <file>         :上传文件
```

### 使用示例：
1. 抓取网页内容到一个文件夹
```
curl -o home.html http://www.baidu.com
```
> 将百度首页内容抓下到home.html中

2. 用-O（大写的），后面的url要具体到某个文件,支持正则表达式
```
curl -O http://www.baidu.com/img/bdlogo.gif
```

3. 模拟表单信息，模拟登录，保存cookie信息
```
curl -c ./cookie_c.txt -F log=aaaa -F pwd=****** http://www.XXXX.com/login.php
```

4. 模拟表单信息，模拟登录，保存头信息
```
curl -D ./cookie_D.txt -F log=aaaa -F pwd=****** http://www.XXXX.com/login.php
```
> -c(小写)产生的cookie和-D里面的cookie是不一样的

5. 使用cookie文件
```
curl -b ./cookie_c.txt http://www.XXXX.com/wp-admin
```

6. 断点续传，-C(大写)
```
curl -C -O http://www.baidu.com/img/bdlogo.gif
```

7. 传送数据,最好用登录页面测试，因为你传值过去后，curl回抓数据，你可以看到你传值有没有成功
```
curl -d log=aaaa http://www.XXXX.com/login.php
```

8. 显示抓取错误，下面这个例子，很清楚的表明了。
```
curl -f http://www.XXXX.com/asdf
```

9. 伪造来源地址，有的网站会判断，请求来源地址，防止盗链
```
curl -e http://localhost http://www.XXXX.com/wp-login.php
```

10. 当我们经常用curl去搞人家东西的时候，人家会把你的IP给屏蔽掉的,这个时候,我们可以用代理
```
curl -x 24.10.28.84:32779 -o home.html http://www.XXXX.com
```

11. 比较大的东西，我们可以分段下载
```
curl -r 0-100 -o img.part1 http://www.XXXX.com/wp-content/compare_varnish.jpg
curl -r 100-200 -o img.part2 http://www.XXXX.com/wp-content/compare_varnish.jpg
curl -r 200- -o img.part3 http://www.XXXX.com/wp-content/compare_varnish.jpg
```
> 用的时候把他们cat一下就OK, `cat img.part* > img.jpg`
> 

12. 模拟浏览器头
```
curl -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)" -x 123.45.67.89:1080 -o page.html -D cookie0001.txt http://www.www.baidu.com
```

13. POST请求
```
curl -d "user=nick&password=12345" http://www.yahoo.com/login.cgi
```

GET请求
```
curl http://www.yahoo.com/login.cgi?user=nick&password=12345
```

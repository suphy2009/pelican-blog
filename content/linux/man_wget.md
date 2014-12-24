Title: Linux wget命令详解
Date: 2014-03-09 16:37
Category: linux
Tags: linux
Slug: linux_main_wget

wget是一个命令行的下载工具。对于我们这些 Linux 用户来说，几乎每天都在使用它。下面为大家介绍几个有用的 wget 小技巧，可以让你更加高效而灵活的使用 wget。

```sh
wget -r -np -nd http://example.com/packages/
```

这条命令可以下载http://example.com网站上packages目录中得所有文件。其中：

- -np: 表示不遍历父目录
- -nd: 表示不在本机重新创建目录结构

```sh
wget -r -np -nd --accept=iso http://example.com/centos-5/i386/
```

与上一条命令相似，但多加一个`--accept=iso`选项，这指示wget仅下载 i386 目录中所有扩展名为 iso 的文件。你也可以指定多个扩展名，只需用逗号分隔即可。

```sh
wget -i filename.txt
```

此命令常用于批量下载的情形，把所有需要下载文件的地址放到 filename.txt 中，然后 wget 就会自动为你下载所有文件了。

```sh
wget -c http://example.com/really-big-file.iso
```

这里所指定的 -c 选项的作用为断点续传。

```sh
wget -m -k (-H) http://www.example.com/
```

该命令可用来镜像一个网站，wget 将对链接进行转换。如果网站中的图像是放在另外的站点，那么可以使用 -H 选项。



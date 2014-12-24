Title: 查看Linux系统信息命令
Date: 2014-03-09 15:37
Category: linux
Tags: linux
Slug: linux_info


Linux中查看系统信息的常用命令:

- 查看CPU信息

```
cat /proc/cpuinfo
```

- 查看内存信息  

```
cat /proc/meminfo
```

- 查看内存大小
```
grep MemTotal /proc/meminfo
```

- 查看所有PCI设备

```
$ /sbin/lspci
```

- 查看所有的usb设备

```
$ /sbin/lsusb
```

- 显示系统中所有加载的模块

```
$ /sbin/lsmod
```

- 显示当前的内存使用情况

```
free -m
```

- 查看系统各分区的使用情况（已用空间、可用空间等）

```
df -h
```

- 查看磁盘的分区及文件系统格式(需root权限)

```
fdisk -l
```

- 查看系统中CPU利用率、空闲率及各进程CPU、内存、IO等资源占用情况

```
top
```

- 另一个查看统中CPU利用率、空闲率的方法

```
vmstat 5 #5秒刷新一次
```

- 查看系统运行时间及负载情况

```
uptime
```

- 查看IDE硬盘参数

```
hdparm /dev/hda #需要root权限
```

- 查看网络接口与IP地址等信息

```
/sbin/ifconfig
```

- 查看网卡设置信息（网卡速率、连接状态等）

```
$ /sbin/ethtool eth0 #可以查看网线是否连接
```

- 查看网络连接信息

```
netstat -an
```

- 查看路由信息

```
$ route -n
```

- 查看防火墙设置

```
$iptables -L
```

- 查看当前登录用户及登录时间

```
$ w
```

- 查看登录用户历史

```
$ last
```

- 查看主机名

```
$ hostname
```

- 查看内核版本信息

```
$ uname -a
```
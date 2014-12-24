Title: Linux crontab定期执行命令
Date: 2014-03-09 18:37
Category: linux
Tags: linux
Slug: linux_main_crontab

### 什么是crond，crontab

Linux下面定期任务分为二部分，一部分是后台程序crond；另一部分是crontab往crond输入指令的接口。

crond 是linux用来定期执行程序的命令。当安装完成操作系统之后，默认便会启动此任务调度命令。crond命令每分钟会定期检查是否有要执行的工作，如果有要执行的工作便会自动执行该工作。

linux任务调度的工作主要分为以下两类：

1. 系统执行的工作：  
   系统周期性所要执行的工作，如备份系统数据、清理缓存 
2. 个人执行的工作：  
   某个用户定期要做的工作，例如每隔10分钟检查邮件服务器是否有新信，这些工作可由每个用户自行设置

Crontab是UNIX系统下的定时任务触发器，其使用者的权限记载在下列两个文件中：

| 文件 | 含义 |
| --------- | ------------- |
| /etc/cron.deny | 该文件中所列的用户不允许使用Crontab命令 |
| /etc/cron.allow | 该文件中所列的用户允许使用Crontab命令 |
| /var/spool/cron/ | 是所有用户的crontab文件 |
| /var/spool/cron/crontabs | /var/spool/cron/crontabs |

crond是linux的内置服务，但它不自动起来，可以用以下的方法启动、关闭这个服务：
 
```
/sbin/service crond start   //启动服务 
/sbin/service crond stop    //关闭服务 
/sbin/service crond restart //重启服务 
/sbin/service crond reload  //重新载入配置
```
 
-----

Crontab命令的格式为：

`crontab –l|-r|-e|-i [username]`

其参数含义如下：

|  参数名称 | 含义 | 示例 |
|----------|-----|------|
| -u | 指定用户 | crontab -u suphy -l |
| -I | 显示用户的Crontab文件的内容 | crontab -I |
| -i | 删除用户的Crontab文件前给提示 | crontab -ri |
| -r | 从Crontab目录中删除用户的Crontab文件 | crontab -r |
| -l | 查看任务列表 | crontab -l |
| -e | 编辑用户的Crontab文件 | crontab -e |
| -d | 删除任务列表 | crontab -d |

用户所建立的Crontab文件存于/var/spool/cron中，其文件名与用户名一致。 
它的格式共分为六段，前五段为时间设定段，第六段为所要执行的命令段

格式如下：`* * * * * command`

`<minute> <hour> <day> <month> <dow> <command>`

其时间段的含义如表二：

| 段 | 含义 | 取值范围 |
|----|-----|---------|
| 第一段 | 代表分钟,每分钟用\*或\*/1表示 | 0—59 |
| 第二段 | 代表小时 | 0—23 |
| 第三段 | 代表日期 | 1—31 |
| 第四段 | 代表月份 | 1—12 |
| 第五段 | 代表星期几，0代表星期日 | 0—6 |


### 示例: 每分钟都会在test.txt里输入当前时间
首先启动crond : `crond`

1. 在命令行输入： `crontab -e`
> 说明:系统默认的编辑器是VIM,如果不是请加上以下shell: 
> `$EDITOR=vi $export EDITOR`

2. 在编辑模式输入: `*/1 * * * * date >> $HOME/test.txt` ，然后保存，退出
3. 查看`crontab -l`

下面是几个具体的例子：

- 0 */2 * * * /sbin/service httpd restart  
  意思是每两个小时重启一次apache
- 50 7 * * * /sbin/service sshd start  
  意思是每天7：50开启ssh服务
- 50 22 * * * /sbin/service sshd stop  
  意思是每天22：50关闭ssh服务
- 0 0 1,15 * * fsck /home  
  每月1号和15号检查/home 磁盘
- 1 * * * * /home/bruce/backup   
  每小时的第一分执行 /home/bruce/backup这个文件
- 00 03 * * 1-5 find /home "\*.xxx" -mtime +4 -exec rm {} /;  
  每周一至周五3点钟，在目录/home中，查找文件名为*.xxx的文件，并删除4天前的文件。 
- 30 6 */10 * * ls  
  意思是每月的1、11、21、31日是的6：30执行一次ls命令



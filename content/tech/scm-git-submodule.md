Title: Git submodule的使用
Date: 2014-02-07 18:39
Category: tech
Tags: git,scm
Slug: scm-git-submodule


#关于Git Submodule的使用

### 说明:

Git的子模块(submodule)功能使得一个仓库可以用子目录的形式去包含一个外部项目的签出版本. 子模块维护它们自己的身份标记(identity); 子模块功能仅仅储存子模块仓库的位置和提交ID, 因此其他克隆父项目("superproject")的开发者可以轻松克隆所有子模块的同一版本. 对父项目的部分签出成为可能: 你可以告诉git去克隆一部分或者所有的子模块, 也可以一个都不克隆.

#### 本文介绍git submodule的常用使用方法

--------

1. 添加submodule

        git submodule add git://host/xxx.git ./output
    
2. 删除submodule
        
        git rm --cached output
        rm -rf output
        
   接着修改.gitmodules文件，去掉相对应的submodule部分
   
   再修改.git/config 中submodule部分
   
   修改完成后就删除成功了，于是commit
         
        git add .gitmodules
        git commit -m "comment"
        
   还不放心可以同步一下：
      
        git submodule sync
        
3. 更新submodule

        git submodule foreach git pull origin master
        
#### END~
 
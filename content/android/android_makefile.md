Title: Android.mk 文件的编写
Date: 2014-03-16 18:37
Category: android
Tags: NDK
Slug: android_makefile

### Android.mk 文件的编写

Android.mk 文件通常以以下两行代码作为开头：
```
LOCAL_PATH := $(call my-dir) 
 include $(CLEAR_VARS) 
```
这两行代码的作用是：

1. 设置当前模块的编译路径为当前文件夹路径。
2. 清理（可能由其他模块设置过的）编译环境中用到的变量。

为了方便模块的编译，Build 系统设置了很多的编译环境变量。要编译一个模块，只要在编译之前根据需要设置这些变量然后执行编译即可。它们包括：

- LOCAL_SRC_FILES：当前模块包含的所有源代码文件。
- LOCAL_MODULE：当前模块的名称，这个名称应当是唯一的，模块间的依赖关系就是通过这个名称来引用的。
- LOCAL_C_INCLUDES：C 或 C++ 语言需要的头文件的路径。
- LOCAL_STATIC_LIBRARIES：当前模块在静态链接时需要的库的名称。
- LOCAL_SHARED_LIBRARIES：当前模块在运行时依赖的动态库的名称。
- LOCAL_CFLAGS：提供给 C/C++ 编译器的额外编译参数。
- LOCAL_JAVA_LIBRARIES：当前模块依赖的 Java 共享库。
- LOCAL_STATIC_JAVA_LIBRARIES：当前模块依赖的 Java 静态库。
- LOCAL_PACKAGE_NAME：当前 APK 应用的名称。
- LOCAL_CERTIFICATE：签署当前应用的证书名称。
- LOCAL_MODULE_TAGS：当前模块所包含的标签，一个模块可以包含多个标签。标签的值可能是 debug, eng, user，development 或者 optional。其中，optional 是默认标签。标签是提供给编译类型使用的。不同的编译类型会安装包含不同标签的模块，

除此以外，Build 系统中还定义了一些便捷的函数以便在 Android.mk 中使用，包括：

- $(call my-dir)：获取当前文件夹路径。
- $(call all-java-files-under, <src>)：获取指定目录下的所有 Java 文件。
- $(call all-c-files-under, <src>)：获取指定目录下的所有 C 语言文件。
- $(call all-Iaidl-files-under, <src>) ：获取指定目录下的所有 AIDL 文件。
- $(call all-makefiles-under, <folder>)：获取指定目录下的所有 Make 文件。
- $(call intermediates-dir-for, <class>, <app_name>, <host or target>, <common?> )：获取 Build 输出的目标文件夹路径。



Title: AndroidManifest中属性说明
Date: 2014-06-04 14:03
Category: android
Tags: View
Slug: androidManifest

## AndroidManifest 中original-package标签

----------

@(示例笔记本)[AndroidManifest|original-package|package]

AndroidManifest.xml中:

+ <manifest>标签中package属性用于设置应用程序的进程名，即在运行时使用ddms查看到的进程名。
+ <original-package>标签用以设置应用源码包名，即Java文件所在的源码程序包层次，android工程中真实的源代码层次结构。

> <manifest>中`package`属性若与<original-package>的`android:name`值相同，配置组建时`android:name`属性值 可以使用".ClassName"形式。
> 使用<original-package>标签后，在<activity><service><receiver><provider>中的`android:name`属性需要写完整的包名，".ClassName"形式无效。
   
注意:<manifest>标签中package属性只是告诉系统应用的进程名；因此进程名（Manifest中package属性的值）与<original-package>的值可以不一样。

### 需要注意:
```xml
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.android.launcher"
    android:sharedUserId="@string/sharedUserId"
    >
```
> 这里package="com.android.launcher"，产生的R.java就会在com.android.launcher中.

`<original-package android:name="com.android.launcher2" />`
这个地方表示源码包是com.android.launcher2。
所以在代码中引用的R.java必须是import com.android.launcher.R;
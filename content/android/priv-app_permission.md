Title: Anroid4.4新增/system/priv-app/目录的权限问题
Date: 2014-12-24 20:19
Category: android
Tags: permission
Slug: android_priv-app

# Anroid4.4新增/system/priv-app/目录的权限问题

@(Android)[permission]

今天在项目中定义permission时使用了`android:protectionLevel="signatureOrSystem"`, 
`signatureOrSystem`官方解释

```
A permission that the system grants only to applications that are in the Android system image or that are signed with the same certificate as the application that declared the permission。
```

该项目设置如下并且在`/system/app/`文件中：
```
//AndroidManifest.xml
android:sharedUserId="android.uid.system"

<permission
    android:name="com.android.permission.service.HANDOFF"
    android:label="@string/perm_access_service"
    android:protectionLevel="signatureOrSystem" >
</permission>

//Android.mk
LOCAL_CERTIFICATE := platform
```

而Contacts应用需要使用到该权限的接口，存放放在`/system/app/`文件中，Contacts配置如下：
```
//Android.mk
LOCAL_PACKAGE_NAME := Contacts
LOCAL_CERTIFICATE := shared
```

由于这两个应用签名不一样，一个是`platform签名`,另外一个是`shared签名`，本以为两个应用都是`System`级别可以访问接口，可是Contacts在调用接口时crash了。

最终发现是因为Android4.4添加一个`/system/priv-app/`目录,只有存放在该目录下的应用才被看做真正的System特权应用, 才能在签名不一致的情况下使用`signatureOrSystem`权限。

加入`/system/priv-app/`目录方法：
在Android.mk中增加 `LOCAL_PRIVILEGED_MODULE := true`


`ApplicationInfo.FLAG_SYSTEM`标志表示该应用程序的apk被捆绑在/system分区。
一个新的隐藏的标志`FLAG_PRIVILEGED`已经出台，反映了访问这些权限的实际权利.
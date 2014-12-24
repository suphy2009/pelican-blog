Title: 如何在Android jni中使用Log
Date: 2014-02-18 17:37
Category: android
Tags: NDK
Slug: android_jni_log

## 打开Android C/C++文件中的Log

### 方法一：

1. 在Android.mk文件中加入：`LOCAL_LDLIBS := -llog`
2. 在要使用log的cpp文件中加入：

```c++
#include <utils/Log.h>
#define LOG_TAG "TAGNAME"
#define LOGV(...) __android_log_print(ANDROID_LOG_VERBOSE,LOG_TAG,__VA_ARGS__)
#define LOGD(...) __android_log_print(ANDROID_LOG_DEBUG, LOG_TAG, __VA_ARGS__)
#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, LOG_TAG, __VA_ARGS__)
#define LOGW(...) __android_log_print(ANDROID_LOG_WARN, LOG_TAG, __VA_ARGS__)
#define LOGE(...) __android_log_print(ANDROID_LOG_ERROR, LOG_TAG, __VA_ARGS__)

```

3. 在需要打印log的地方使用: `LOGD("************")`

> 注: 当然也可以在程序中直接使用`__android_log_print`打印log，无须定义宏；


### 方法二：

Android4.1中，log有了一些打印，具体可以参考system/core/include/cutils/log.h，该文件中定义了控制那些log输出的宏。

Android的编译参数中，加入了-DNDEBUG，也就是默认no debug；
当-DNDEBUG被打上后，默认ALOGV会被禁止; 但是我们可以使用 *LOG_NDEBUG*、*LOG_NIDEBUG*、*LOG_NDDEBUG*这三个宏控制LOG_PRI(priority, tag, ...)

可以一次打开LOGV，LOGI，LOGD，也可以分别打开：
```c++
#undef NDEBUG            //打开LOGV/LOGI/LOGD

#define LOG_NDEBUG   0   //打开LOGV
#define LOG_NIDEBUG  0   //打开LOGI
#define LOG_NDDEBUG 0    //打开LOGD
```

#### 举例：

果要看AndroidRuntime的LOGI和LOGD，可以有这样2种写法：

第一种：

NDEBUG - LOG_NDEBUG = LOG_NIDEBUG + LOG_NIDEBUG
```c++
#define LOG_TAG "AndroidRuntime"
#undef NDEBUG
#define LOG_NDEBUG 1
#include <utils/Log.h>
```

第二种：

G_NIDEBUG + LOG_NIDEBUG
```c++
#define LOG_TAG "AndroidRuntime"
#define LOG_NIDEBUG 0
#define LOG_NDDEBUG 0
#include <utils/Log.h>
```

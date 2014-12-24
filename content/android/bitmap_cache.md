Title: Android图片缓存
Date: 2014-03-11 11:37
Category: android
Tags: bitmap,cache
Slug: android_bitmap_cache

### 开源lib Universal Image Loader

1. ImageLoader根据ImageView的width，height确定图片的宽高。
2. 经常出现OutOfMemory:

    - 减少线程池数目.threadPoolSize（1 - 5 is recommended）
    - 使用.bitmapConfig(Bitmap.Config.RGB_565)减少图片占用内存数目
    - memoryCache（new WeakMemoryCache()） 及时释放内存
    - imageScaleType(ImageScaleType.IN_SAMPLE_INT)或者imageScaleType(ImageScaleType.EXACTLY)
    - 避免使用RoundedBitmapDisplayer；他会创建新的ARGB_8888格式的Bitmap对象；
    - 使用.memoryCache(new WeakMemoryCache())，不要使用.cacheInMemory();

3. 内存缓存，sd卡缓存，显示图片，可以使用已经初始化过的实现；
4. 为了避免使用list，grid，scroll，你可以使用：
```
boolean pauseOnScroll = false; // or true
boolean pauseOnFling = true; // or false
PauseOnScrollListener listener = new PauseOnScrollListener(imageLoader, pauseOnScroll, pauseOnFling);
listView.setOnScrollListener(listener);
```

### Strong Reference & WeakReference & SoftReference

1. StrongReference 是Java的默认引用实现, 它会尽可能长时间的存活于 JVM 内， 当没有任何对象指向它时 GC 执行后将会被回收
2. WeakReference，顾名思义是一个弱引用, 当所引用的对象在 JVM 内不再有强引用时, GC 后 weak reference 将会被自动回收

> WeakHashMap 使用 WeakReference 作为 key， 一旦没有指向 key 的强引用, WeakHashMap 在 GC 后将自动删除相关的 entry 

3. SoftReference 于 WeakReference 的特性基本一致， 最大的区别在于 SoftReference 会尽可能长的保留引用直到 JVM 内存不足时才会被回收(虚拟机保证), 这一特性使得 SoftReference 非常适合缓存应用

### Android 中关于内部存储的重要函数

1. context.getExternalFilesDir() 
    可以获取到 SDCard/Android/data/`packagename`/files/目录，一般放一些长时间保存的数据
2. context.getExternalCacheDir()
    可以获取到 SDCard/Android/data/`packagename`/cache/目录，一般存放临时缓存数据

如果使用上面的方法，当你的应用在被用户卸载后，SDCard/Android/data/packagename/ 这个目录下的所有文件都会被删除，不会留下垃圾信息。

3. Environment.getExternalStoragePublicDirectory(String)
    非私有的（shared）的文件应该放在目录

4. context.getCacheDir()
    返回/data/data/`packagename`/cache该目录主要用于存放缓存文件，当系统的内存存储空间紧张时，该目录下的文件会被删除掉




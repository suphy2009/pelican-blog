Title: Android关于高效显示图片的问题
Date: 2014-03-17 17:37
Category: android
Tags: bitmap
Slug: android_bitmap

## Android关于高效显示图片的问题

### Bitmap的immutable和mutable

Bitmap可以理解为Android里的画布，Canvas是画笔，Paint是画笔属性的设置，View是画图的地方；

图像（Image)有immutable(不可变的)和mutable(可变的)之分，创建自图形的Bitmap是immutable，而给定宽高以及其他一些参数创建的Bitmap是mutable.

```java
//Immutable bitmap
Bitmap temp = BitmapFactory.decodeFile("/sdcard/xxx.jpg");
Bitmap immutable = Bitmap.createBitmap(temp);

//mutable bitmap
Bitmap mutalbe = Bitmap.createBitmap(240, 320, Bitmap.Config.RGB_565);
```

在使用`Canvas canvas = new Canvas(bitmap);` 时，传入的参数只能是mutable的bitmap.

### BitmapFactory.Options.inBitmap属性

Android 3.0 (API Level 11) 引进了 BitmapFactory.Options.inBitmap 字段，如果设置了该属性，那么当使用了带有该 Options 参数的 decode 方法在加载内容时，decode 方法会尝试重用一个已经存在的位图。这就意味着位图内存已经被重用了，从而性能得到了改善，并且移除了内存的分配和解除分配。下面是一些使用 inBitmap 的注意事项：

- 重用的位图大小必须和源位图大小相同(这样才能保证它们占用相同的内存),并且位图的格式应该是 JPEG 或 PNG（无论是作为资源形式还是数据流形式）;
- 若设置了重用的位图的 Bitmap.Config 配置，则需要重写 inPreferredConfig 方法
- 你应该总是使用位图的解码方法，因为我们不能认为重用的位图是可用的（例如，若位图大小不匹配，就无法保证位图可重用）

### 使用TransitionDrawable实现两张图片的过渡效果

TransitionDrawable 可以用来实现两个Drawable直接的交错渐变的过渡效果。

```
 TransitionDrawable td = new TransitionDrawable(new Drawable[] {
                            new ColorDrawable(android.R.color.transparent),
                            drawable
                    });
// Set background to loading bitmap
imageView.setBackgroundDrawable(new BitmapDrawable(mResources, mLoadingBitmap));

imageView.setImageDrawable(td);
td.startTransition(200);
```

### Drawable Animation -- 使用多幅图片实现动画

在Andrio的中，可以使用多幅图片实现动画效果。
首先定义一个以 <animation-list>为根节点的xml文件，命名为 anim.xml 放在 res/drawable/目录下。
```
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="true">
    <item android:drawable="@drawable/image1" android:duration="200" />
    <item android:drawable="@drawable/image2" android:duration="200" />
    <item android:drawable="@drawable/image3" android:duration="200" />
</animation-list>
```
在控件中使用此资源文件
```
ImageView image = (ImageView) findViewById(R.id.rocket_image);
image.setBackgroundResource(R.drawable.rocket_thrust);
AnimationDrawable animation = (AnimationDrawable) image.getBackground(); 

animation.start();  
```


-----
### 2014.3.17 添加

Bitmap.extractAlpha()
    返回一个新的位图，该位图从源图中捕获了alpha值。
Bitmap.extractAlpha (Paint paint, int[] offsetXY)
    返回一个从源图中获取了alpha值的新位图.

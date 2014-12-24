Title: Launcher3知识总结
Date: 2014-02-17 17:37
Category: android
Tags: Launcher3
Slug: android_launcher

## 一、xml文件解析

Android解析XML文件标签的属性,获取属性的值，如：

```xml
<favorites>
...

<favorite
        launcher:packageName="com.android.dialer"
        launcher:className="com.android.dialer.DialtactsActivity"
        launcher:container="-101"
        launcher:screen="0"
        launcher:x="0"
        launcher:y="0" />
...
</favorites
```

在attrs.xml文件中定义属性：

```xml
<!-- XML attributes used by default_workspace.xml -->
    <declare-styleable name="Favorite">
        <attr name="className" format="string" />
        <attr name="packageName" format="string" />
        <attr name="container" format="string" />
        <attr name="screen" format="string" />
        <attr name="x" format="string" />
        <attr name="y" format="string" />
        <attr name="spanX" format="string" />
        <attr name="spanY" format="string" />
        <attr name="icon" format="reference" />  
        <attr name="title" format="reference" />
        <attr name="uri" format="string" />
    </declare-styleable>
```

在代码中用XmlResourceParser 方法 parser.next() 遍历xml文件到要处理的xml标签\<favorite\>位置。

```java
XmlResourceParser parser = mContext.getResources().getXml(workspaceResourceId);
AttributeSet attrs = Xml.asAttributeSet(parser);

//parser.next() 遍历xml文件到要处理的xml标签<favorite>位置

TypedArray a = mContext.obtainStyledAttributes(attrs, R.styleable.Favorite);
//使用TypedArray.getXXX()方法获取属性值
String screen = a.getString(R.styleable.Favorite_screen);

a.recycle();
```

### 二、android:stateNotNeeded=[true|false]

```xml
<activity
   android:stateNotNeeded="true"
>
</activity>
```

android:stateNotNeeded 默认为false,若设为true，则当activity重新启动时不会调用onSaveInstanceState()方法，同样onCreate()方法中的Bundle参数会用null值穿进去，也就是说Activity每次启动都跟第一次启动一样。

在某种特殊场合下，由于用户按了Home键，该属性设置为true时，不需要保存原先的状态引用，节省了空间资源，从而可以让Activity不会像默认设置那样Crash掉。

### Android布局文件中的属性

- android:ems="10" 
  设置TextView或者Edittext的宽度为10个字符的宽度。当设置该属性后，控件显示的长度就为10个字符的长度，超出的部分将不显示

- android:textAllCaps="true"
  设置TextView所有英文字母大写

- android:drawableStart
  内容显示在文字的开始

设置TextView投影：

```xml
<item name="android:shadowColor">#FF000000</item>
<item name="android:shadowDx">0.0</item>
<item name="android:shadowDy">1.0</item>
<item name="android:shadowRadius">4.0</item>
```


### Matrix
Matrix.mapPoints()应用这个matrix对这个数组中代表的2D点进行变换，变换的结果的点的信息依旧写入到这个数组中

```java
mTmpPoint[0] = ev.getX();
mTmpPoint[1] = ev.getY();
v.getMatrix().mapPoints(mTmpPoint);
```

> 应用这个matrix对这个数组中代表的2D点进行变换，变换的结果的点的信息依旧写入到这个数组中
> 使用场景： 1.计算原来一个点（0，0） 放大后的坐标。
> 
> 举例说明，有一个图片，我要在图片的某个位置上画一个正方形。当这个图片缩放后，为了使正方形依然在“某个位置”，就要用此方法来计算新的坐标。

该段代码的意思：根据event获得触摸的坐标(x,y)，再根据放大或缩小后view的Matrix获取相对应view的变换坐标



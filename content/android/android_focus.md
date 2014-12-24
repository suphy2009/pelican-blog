Title: ListView焦点问题
Date: 2014-05-29 20:03
Category: android
Tags: ListView
Slug: android_focus

## android:descendantFocusability 焦点 父控件与子控件焦点

ListView item包含ImageButton、Button、CheckBox等控件时无法获取焦点，造成点击item无响应。

可以使用android:descendantFocusability="blocksDescendants" 来解决

该属性是当一个为view获取焦点时，定义viewGroup和其子控件两者之间的关系。

属性的值有三种：

+ beforeDescendants：viewgroup会优先其子类控件而获取到焦点
+ afterDescendants：viewgroup只有当其子类控件不需要获取焦点时才获取焦点
+ blocksDescendants：viewgroup会覆盖子类控件而直接获得焦点

通常我们用到的是第三种，即在Item布局的根布局加上android:descendantFocusability=”blocksDescendants”的属性就好了


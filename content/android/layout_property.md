Title: View及TextView属性说明
Date: 2014-05-23 9:37
Category: android
Tags: View
Slug: android_view_property

## View属性说明

android:alpha  
关联方法: setAlpha(float)  
属性说明: 视图透明度，值在0-1之间。0为完全透明，1为完全不透明。  

android:background  
关联方法: setBackgroundResource(int)   
属性说明: 视图背景  

android:clickable  
关联方法: setClickable(boolean)  
属性说明: 视图是否可点击

android:contentDescription  
关联方法: setContentDescription(CharSequence)  
属性说明: 设置View的备注说明，作为一种辅助功能提供,为一些没有文字描述的View提供说明  

android:drawingCacheQuality 
关联方法: setDrawingCacheQuality(int)  
属性说明: "设置绘图时半透明质量。有可以取以下3个值 auto——默认，由框架决定 high——高质量，使用较高的颜色深度，消耗更多的内存 low——低质量，使用较低的颜色深度，但是用更少的内存" 

android:duplicateParentState  
关联方法:   
属性说明: 如果设置此属性，将直接从父容器中获取绘图状态（光标，按下等）  

android:fadeScrollbars  
关联方法: setScrollbarFadingEnabled(boolean)   
属性说明: 定义在ScrollBar没有使用时，是否褪色。  

android:fadingEdgeLength  
关联方法: getVerticalFadingEdgeLength()   
属性说明: 设置边框渐变的长度。  

android:filterTouchesWhenObscured  
关联方法: setFilterTouchesWhenObscured(boolean)   
属性说明: view所在窗口被其它可见窗口遮住时，是否过滤触摸事件。  

android:fitsSystemWindows  
关联方法: setFitsSystemWindows(boolean)   
属性说明: 设置布局调整时是否考虑系统窗口（如状态栏）  

android:focusable  
关联方法: setFocusable(boolean)   
属性说明: 设置是否获得焦点。若有requestFocus()被调用时，后者优先处理。注意在表单中想设置某一个如EditText获取焦点，光设置这个是不行的，需要将这个EditText前面的focusable都设置为false才行。在Touch模式下获取焦点需要设置focusableInTouchMode为true。  

android:focusableInTouchMode  
关联方法: setFocusableInTouchMode(boolean)   
属性说明: 设置在Touch模式下View是否能取得焦点。  

android:hapticFeedbackEnabled  
关联方法: setHapticFeedbackEnabled(boolean)   
属性说明: 是否启用触摸反馈，启用后就是在点击等操作时会有震动等反馈效果  

android:id  
关联方法: setId(int)   
属性说明: 给当前View设置一个在当前layout.xml中的唯一编号，可以通过调用View.findViewById() 或Activity.findViewById()根据这个编号查找到对应的View。不同的layout.xml之间定义相同的id不会冲突。

android:importantForAccessibility  
关联方法: setImportantForAccessibility(int)   
属性说明: 设置可达性的重要性  

android:isScrollContainer  
关联方法: setScrollContainer(boolean)   
属性说明: 设置当前View为滚动容器。这里没有测试出效果来，ListView/ GridView/ ScrollView根本就不用设置这个属性，而EdidText设置android:scrollbars也能出滚动条  

android:keepScreenOn  
关联方法: setKeepScreenOn(boolean)   
属性说明: 视图在可见的情况下是否保持唤醒状态。  

android:layerType  
关联方法: setLayerType(int,Paint)   
属性说明: "设置指定层的类型，可以取以下3个值： none——不指定 software——软件层。 hardware——硬件层。使用硬件加速。"

android:layoutDirection  
关联方法: setLayoutDirection(int)   
属性说明: 定义布局图纸的方向  

android:longClickable  
关联方法: setLongClickable(boolean)   
属性说明: 是否响应长点击事件  

android:minHeight  
关联方法: setMinimumHeight(int)   
属性说明: 设置视图最小高度  

android:minWidth  
关联方法: setMinimumWidth(int)   
属性说明: 设置视图最小宽度  

android:nextFocusDown  
关联方法: setNextFocusDownId(int)   
属性说明: 向下移动焦点时，下一个获取焦点的view的id  

android:nextFocusForward  
关联方法: setNextFocusForwardId(int)   
属性说明: 下一个获取焦点的view的id  

android:nextFocusLeft  
关联方法: setNextFocusLeftId(int)   
属性说明: 向左移动焦点时，下一个获取焦点的view的id  

android:nextFocusRight  
关联方法: setNextFocusRightId(int)   
属性说明: 向右移动焦点时，下一个获取焦点的view的id  

android:nextFocusUp  
关联方法: setNextFocusUpId(int)   
属性说明: 向上移动焦点时，下一个获取焦点的view的id  

android:onClick  
关联方法:   
属性说明: 点击时，要调用的方法的名称。  

android:padding  
关联方法: setPaddingRelative(int,int,int,int)   
属性说明: 设置上下左右的边距  

android:paddingBottom  
关联方法: setPaddingRelative(int,int,int,int)  
属性说明: 下边距  

android:paddingEnd  
关联方法: setPaddingRelative(int,int,int,int)   
属性说明: 与android:paddingRight相同  

android:paddingLeft  
关联方法: setPadding(int,int,int,int)   
属性说明: 左边距  

android:paddingRight  
关联方法: setPadding(int,int,int,int)   
属性说明: 右边距

android:paddingStart  
关联方法: setPaddingRelative(int,int,int,int)   
属性说明: android:paddingLeft相同  

android:paddingTop  
关联方法: setPaddingRelative(int,int,int,int)   
属性说明: 上边距  

android:requiresFadingEdge  
关联方法: setVerticalFadingEdgeEnabled(boolean)   
属性说明: 定义滚动时边缘是否褪色  

android:rotation  
关联方法: setRotation(float)   
属性说明: 旋转度数  

android:rotationX  
关联方法: setRotationX(float)   
属性说明: 水平旋转度数  

android:rotationY  
关联方法: setRotationY(float)   
属性说明: 竖直旋转度数  

android:saveEnabled  
关联方法: setSaveEnabled(boolean)   
属性说明: 在配置改变等情况出现时是否保存view的状态数据。如果你的view有id，那默认系统就会帮你保存。

android:scaleX  
关联方法: setScaleX(float)   
属性说明: 水平方向缩放比例

android:scaleY  
关联方法: setScaleY(float)   
属性说明: 竖直方向缩放比例  

android:scrollX  
关联方法:   
属性说明: x方向的滚动偏移。即在水平方向滚动了多少距离  

android:scrollY  
关联方法:   
属性说明: y方向的滚动偏移。即在竖直方向滚动了多少距离  

android:scrollbarAlwaysDrawHorizontalTrack  
关联方法:   
属性说明: 是否总是绘制水平滚动条的滚动轨道  

android:scrollbarAlwaysDrawVerticalTrack  
关联方法:   
属性说明: 是否总是绘制竖直滚动条的滚动轨道  

android:scrollbarDefaultDelayBeforeFade  
关联方法: setScrollBarDefaultDelayBeforeFade(int)   
属性说明: 滚动条在n毫秒后开始淡出。  

android:scrollbarFadeDuration  
关联方法: setScrollBarFadeDuration(int)   
属性说明: 滚动条用多长时间淡出完毕。  

android:scrollbarSize  
关联方法: setScrollBarSize(int)   
属性说明: 设置滚动条的尺寸。垂直滚动条的宽度、水平滚动条的高度  

android:scrollbarStyle  
关联方法: setScrollBarStyle(int)   
属性说明: "滚动条的风格。共4组值： insideOverlay——内贴图 insideInset——内插图 outsideOverlay——外贴图 outsideInset——外插图。 inside就是滚动条在绘制在padding以内；outside就是不需要绘制在padding内（即view的边界处）；Overlay是贴图，就是直接覆盖在内容的上方，这样内容可能会显示到滚动条下方去；Inset是插图，就是会在对应padding上加上滚动条的宽度，以不让内容显示到滚动条下面去。"

android:scrollbarThumbHorizontal  
关联方法:   
属性说明: 水平滚动块的drawable对象  

android:scrollbarThumbVertical  
关联方法:   
属性说明: 竖直滚动块的drawable对象  

android:scrollbarTrackHorizontal  
关联方法:   
属性说明: 水平滚动条滚动轨道的drawable对象  

android:scrollbarTrackVertical  
关联方法:   
属性说明: 竖直滚动条滚动轨道的drawable对象  

android:scrollbars  
关联方法:   
属性说明: "设置可显示的滚动条。有3个取值: none——不显示滚动条 horizontal——显示水平滚动条 vertical——显示竖直滚动条"  

android:soundEffectsEnabled  
关联方法: setSoundEffectsEnabled(boolean)   
属性说明: 点击或触摸该view时，是否需要有声音效果  

android:tag  
关联方法:   
属性说明: string标识。类似id，id是整数标识。 

android:textAlignment  
关联方法: setTextAlignment(int)   
属性说明: 设置文本的显示方式。  

android:textDirection  
关联方法: setTextDirection(int)   
属性说明: 设置文本的显示方向。  

android:transformPivotX  
关联方法: setPivotX(float)   
属性说明: 水平方向偏转量  

android:transformPivotY  
关联方法: setPivotY(float)   
属性说明: 竖直方向偏转量  

android:translationX  
关联方法: setTranslationX(float)   
属性说明: 水平方向的移动距离  

android:translationY  
关联方法: setTranslationY(float)   
属性说明: 竖直方向的移动距离  

android:visibility  
关联方法: setVisibility(int)   
属性说明: "view的可见性。有3个取值： gone——不可见，同时不占用view的空间； invisible——不可见，但占用view的空间； visible——可见"  

-----

## TextView属性说明

android:autoLink
关联方法: setAutoLinkMask(int)
属性说明: 设置是否“当文本为URL链接/email/电话号码/map时，文本显示为可点击的链接”。可选值(none/web/email/phone/map/all)

android:autoText
关联方法: setKeyListener(KeyListener)
属性说明: 如果设置，将自动执行输入值的拼写纠正。此处无效果，在显示输入法并输入的时候起作用。

android:bufferType
关联方法: setText(CharSequence,TextView.BufferType)
属性说明: 指定getText()方式取得的文本类别。选项editable 类似于StringBuilder可追加字符，也就是说getText后可调用append方法设置文本内容。

android:capitalize
关联方法: setKeyListener(KeyListener)
属性说明: 设置自动大写属性。比如设置为2，自动大写单词首字符；设置为1，自动大写每句话的首字母等等。

android:cursorVisible
关联方法: setCursorVisible(boolean)
属性说明: 设定光标为显示/隐藏，默认显示。

android:digits
关联方法: setKeyListener(KeyListener)
属性说明: 设置允许输入哪些字符。如“1234567890.+-*/%\n()”

android:drawableBottom
关联方法: setCompoundDrawablesWithIntrinsicBounds(int,int,int,int)
属性说明: 在text的下方输出一个drawable。如果指定一个颜色的话会把text的背景设为该颜色，并且同时和background使用时覆盖后者。

android:drawableEnd
关联方法: setCompoundDrawablesRelativeWithIntrinsicBounds(int,int,int,int)
属性说明: 在文本结尾处显示drawable对象。它的值可以是其它资源的引用，比如，"@[+][package:]type:name"或者"?[package:][type:]name"；也可以是颜色值，如"#rgb", "#argb", "#rrggbb", or "#aarrggbb"。

android:drawableLeft
关联方法: setCompoundDrawablesWithIntrinsicBounds(int,int,int,int)
属性说明: 在text的左边输出一个drawable。

android:drawablePadding
关联方法: setCompoundDrawablePadding(int)
属性说明: 设置text与drawable的间隔，与drawableLeft、drawableRight、drawableTop、drawableBottom一起使用，可设置为负数，单独使用没有效果。

android:drawableRight
关联方法: setCompoundDrawablesWithIntrinsicBounds(int,int,int,int)
属性说明: 在text的右边输出一个drawable。

android:drawableStart
关联方法: setCompoundDrawablesRelativeWithIntrinsicBounds(int,int,int,int)
属性说明: 在文本开始处显示drawable对象。它的值可以是其它资源的引用，比如，"@[+][package:]type:name"或者"?[package:][type:]name"；也可以是颜色值，如"#rgb", "#argb", "#rrggbb", or "#aarrggbb"。

android:drawableTop
关联方法: setCompoundDrawablesWithIntrinsicBounds(int,int,int,int)
属性说明: 在text的正上方输出一个drawable。

android:editable
关联方法: 
属性说明: 设置是否可编辑。这里无效果，在EditView中才有效果。

android:editorExtras
关联方法: setInputExtras(int)
属性说明: 设置文本的额外的输入数据。在EditView中才有效果。

android:ellipsize
关联方法: setEllipsize(TextUtils.TruncateAt)
属性说明: 设置当文字过长时,该控件该如何显示。有如下值设置：”start”—–省略号显示在开头；”end”——省略号显示在结尾；”middle”—-省略号显示在中间；”marquee” ——以跑马灯的方式显示(动画横向移动)

android:ems
关联方法: setEms(int)
属性说明: 设置TextView的宽度为N个字符的宽度。

android:fontFamily
关联方法: setTypeface(Typeface)
属性说明: 文本的字形体系。

android:freezesText
关联方法: setFreezesText(boolean)
属性说明: 设置保存文本的内容以及光标的位置。

android:gravity
关联方法: setGravity(int)
属性说明: 设置文本位置，如设置成“center”，文本将居中显示。

android:height
关联方法: setHeight(int)
属性说明: 设置文本区域的高度，支持度量单位：px(像素)/dp/sp/in/mm(毫米)

android:hint
关联方法: setHint(int)
属性说明: Text为空时显示的文字提示信息，可通过textColorHint设置提示信息的颜色。

android:imeActionId
关联方法: setImeActionLabel(CharSequence,int)
属性说明: 设置IME动作ID。

android:imeActionLabel
关联方法: setImeActionLabel(CharSequence,int)
属性说明: 设置IME动作标签。在EditView再做说明。

android:imeOptions
关联方法: setImeOptions(int)
属性说明: 附加功能，设置右下角IME动作与编辑框相关的动作，如actionDone右下角将显示一个“完成”，而不设置默认是一个回车符号。

android:includeFontPadding
关联方法: setIncludeFontPadding(boolean)
属性说明: 设置文本是否包含顶部和底部额外空白，默认为true。

android:inputMethod
关联方法: setKeyListener(KeyListener)
属性说明: 为文本指定输入法，需要完全限定名（完整的包名）。例如：com.google.android.inputmethod.pinyin，但是这里报错找不到。

android:inputType
关联方法: setRawInputType(int)
属性说明: 设置文本的类型，用于帮助输入法显示合适的键盘类型。在EditView中再详细说明，这里无效果。

android:lineSpacingExtra
关联方法: setLineSpacing(float,float)
属性说明: 设置行间距。

android:lineSpacingMultiplier
关联方法: setLineSpacing(float,float)
属性说明: 设置行间距的倍数。如”1.2”

android:lines
关联方法: setLines(int)
属性说明: 设置文本的行数，设置两行就显示两行，即使第二行没有数据。

android:linksClickable
关联方法: setLinksClickable(boolean)
属性说明: 设置链接是否点击连接，即使设置了autoLink。

android:marqueeRepeatLimit
关联方法: setMarqueeRepeatLimit(int)
属性说明: 在ellipsize指定marquee的情况下，设置重复滚动的次数，当设置为marquee_forever时表示无限次。

android:maxEms
关联方法: setMaxEms(int)
属性说明: 设置TextView的宽度为最长为N个字符的宽度。与ems同时使用时覆盖ems选项。

android:maxHeight
关联方法: setMaxHeight(int)
属性说明: 设置文本区域的最大高度

android:maxLength
关联方法: setFilters(InputFilter)
属性说明: 限制显示的文本长度，超出部分不显示。

android:maxLines
关联方法: setMaxLines(int)
属性说明: 设置文本的最大显示行数，与width或者layout_width结合使用，超出部分自动换行，超出行数将不显示。

android:maxWidth
关联方法: setMaxWidth(int)
属性说明: 设置文本区域的最大宽度

android:minEms
关联方法: setMinEms(int)
属性说明: 设置TextView的宽度为最短为N个字符的宽度。与ems同时使用时覆盖ems选项。

android:minHeight
关联方法: setMinHeight(int)
属性说明: 设置文本区域的最小高度

android:minLines
关联方法: setMinLines(int)
属性说明: 设置文本的最小行数，与lines类似。

android:minWidth
关联方法: setMinWidth(int)
属性说明: 设置文本区域的最小宽度

android:numeric
关联方法: setKeyListener(KeyListener)
属性说明: 如果被设置，该TextView有一个数字输入法。此处无用，设置后唯一效果是TextView有点击效果，此属性在EdtiView将详细说明。

android:password
关联方法: setTransformationMethod(TransformationMethod)
属性说明: 以小点”.”显示文本

android:phoneNumber
关联方法: setKeyListener(KeyListener)
属性说明: 设置为电话号码的输入方式。

android:privateImeOptions
关联方法: setPrivateImeOptions(String)
属性说明: 设置输入法选项，在EditText中才有作用。

android:scrollHorizontally
关联方法: setHorizontallyScrolling(boolean)
属性说明: 设置文本超出TextView的宽度的情况下，是否出现横拉条。

android:selectAllOnFocus
关联方法: setSelectAllOnFocus(boolean)
属性说明: 如果文本是可选择的，让他获取焦点而不是将光标移动为文本的开始位置或者末尾位置。TextView中设置后无效果。

android:shadowColor
关联方法: setShadowLayer(float,float,float,int)
属性说明: 指定文本阴影的颜色，需要与shadowRadius一起使用。

android:shadowDx
关联方法: setShadowLayer(float,float,float,int)
属性说明: 设置阴影横向坐标开始位置。

android:shadowDy
关联方法: setShadowLayer(float,float,float,int)
属性说明: 设置阴影纵向坐标开始位置。

android:shadowRadius
关联方法: setShadowLayer(float,float,float,int)
属性说明: 设置阴影的半径。设置为0.1就变成字体的颜色了，一般设置为3.0的效果比较好。

android:singleLine
关联方法: setTransformationMethod(TransformationMethod)
属性说明: 设置单行显示。如果和layout_width一起使用，当文本不能全部显示时，后面用“…”来表示。如android:text="test_ singleLine " android:singleLine="true" android:layout_width="20dp"将只显示“t…”。如果不设置singleLine或者设置为false，文本将自动换行

android:text
关联方法: setText(CharSequence,TextView.BufferType)
属性说明: 设置显示文本.

android:textAllCaps
关联方法: setAllCaps(boolean)
属性说明: 设置文本全为大写。值为"true"或"false"。

android:textAppearance
关联方法: 
属性说明: 设置文字外观。如“?android:attr/textAppearanceLargeInverse

android:textColor
关联方法: setTextColor(int)
属性说明: 设置文本颜色

android:textColorHighlight
关联方法: setHighlightColor(int)
属性说明: 被选中文字的底色，默认为蓝色

android:textColorHint
关联方法: setHintTextColor(int)
属性说明: 设置提示信息文字的颜色，默认为灰色。与hint一起使用。

android:textColorLink
关联方法: setLinkTextColor(int)
属性说明: 文字链接的颜色.

android:textIsSelectable
关联方法: isTextSelectable()
属性说明: 设置非编辑文本可否被选择。值为"true"或"false"。

android:textScaleX
关联方法: setTextScaleX(float)
属性说明: 设置文字之间间隔，默认为1.0f。

android:textSize
关联方法: setTextSize(int,float)
属性说明: 设置文字大小，推荐度量单位”sp”，如”15sp”

android:textStyle
关联方法: setTypeface(Typeface)
属性说明: 设置字形[bold(粗体) 0, italic(斜体) 1, bolditalic(又粗又斜) 2] 可以设置一个或多个，用“|”隔开

android:typeface
关联方法: setTypeface(Typeface)
属性说明: 设置文本字体，必须是以下常量值之一：normal 0, sans 1, serif 2, monospace(等宽字体) 3]

android:width
关联方法: setWidth(int)
属性说明: 设置文本区域的宽度，支持度量单位：px(像素)/dp/sp/in/mm(毫米)。
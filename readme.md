# XI GAL

XI GAL是一款基于opencv-python的galgame视觉小说引擎，以opencv的实时画图来进行界面的交互与显示。

唔......

大概是还没写完吧，而且离完成还差的很远很远





# 关于XI GAL的语法

配置文件：

包含文本框图片路径，文本框大小，文本框定位，文本框透明度，字体，字体大小，字体颜色，字体位置，窗口大小等默认使用参数

其中一些可体现在设置界面来更改默认配置的默认内容





文本

（人物，人物说的话，人物说的话的文本颜色，文本位置放在文本框的位置亦或是放到屏幕中央，此时使用的背景图，此时使用到的音乐）



@角色名

T角色将要说出的文本

L文本放置的位置，不提供位置仅提供文本则会绘制在配置文件中的位置

C角色文本的颜色，不提供颜色仅提供文本则会使用配置文件的默认颜色

M要播放的音乐

！要停止的音乐

B要作为背景的图片

I要插入融合在画面中某个位置的图片或者立绘



以上为一个分块，以一个空行来表示一个分块事件的结束
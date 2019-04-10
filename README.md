# Burp-Sqlmap
Python版的Burp-Sqlmap插件

# 效果
* 普通get注入
* post+leve2注入
* post+leve5注入
* 全自动下一步、发现注入点有提示音
[![ATnTUK.png](https://s2.ax1x.com/2019/04/10/ATnTUK.png)](https://imgchr.com/i/ATnTUK)
[![ATn5Hx.md.png](https://s2.ax1x.com/2019/04/10/ATn5Hx.md.png)](https://imgchr.com/i/ATn5Hx)
[![ATn4D1.md.png](https://s2.ax1x.com/2019/04/10/ATn4D1.md.png)](https://imgchr.com/i/ATn4D1)

# 安装
burp需要jython的支持。下载安装jython到 **C:\jython2.7.0** [jython](https://www.jython.org/downloads.html)

下载[py-sqlmap.py](https://github.com/lanpan999/Burp-Sqlmap)
将py-sqlmap.py放到sqlmap文件目录。 比如我的目录是：**C:\jython2.7.0\plung\sqlmap**
然后去burp中添加 py-sqlmap.py
[![ATnoE6.md.png](https://s2.ax1x.com/2019/04/10/ATnoE6.md.png)](https://imgchr.com/i/ATnoE6)
[![ATnhuR.png](https://s2.ax1x.com/2019/04/10/ATnhuR.png)](https://imgchr.com/i/ATnhuR)


# 需要注意的地方
因为我用的是Python双环境，如果提示Python2 不存在，把代码中83、99、115行的Python2 改成Python就行

# 如何解决 “Python" 中出现《ImportError: DLL load failed while importing win32api: 找不到指定的模块》问题

Source: https://www.jianshu.com/p/9067ea2c6cb9?ivk_sa=1024320u

[![img](a.assets/12-aeeea4bedf10f2a12c0d50d626951489.jpg)](https://www.jianshu.com/u/52bd632a3020)

[山溪旁舍鸟语香](https://www.jianshu.com/u/52bd632a3020)关注

2019.10.28 15:36:12字数 318阅读 15,413

​    1、在 ”https://github.com/mhammond/pywin32/releases“ 网站下载与自己安装的 “Python" 版本相适应的 "pywin32" 安装程序。如 "pywin32-225.win-amd64-py3.8.exe" 之类。这点很重要，如果下载的版本不匹配，就是费尽九牛二虎之力也是白费劲。

​    2、以管理员身份运行上述下载程序。

​    3、如果默认安装目录不合适的话（同时安装了几个版本的 "Python" 就会引发这种情况），"python" 脚本中有调用 “win32” 中相应模块时就会出现如文章名指出的那样的错误信息，这时可做如下处理：

​     4、用类 “python" 脚本描述处理方法如下：

​     if 同时安装了几个版本的 “Python”：

​        请将非当前使用的 “python” 安装文件夹更名

​        在当前 “python” 安装目录的 “\Scripts” 文件夹下执行 “python pywin32_postinstall.py -install” 命令。

​        将上述非当前使用的 “python” 安装文件夹正名

​    else:

​        在当前 “python” 安装目录的 “\Scripts” 文件夹下执行 “python pywin32_postinstall.py -install” 命令。



恭喜恭喜，成功了！！！
# Python GUI: cefpython3的简单分析和应用

来源：https://www.jianshu.com/p/1ca206b28e28

**内容概要：**
 一、cefpython3的浅显理解：`cefpython3是什么？ 为什么要使用它？ 如何使用？`
 二、cefpython3的简单应用：`安装使用，首先创建浏览器，然后控制浏览器，再将其嵌入到其他GUI框架。`
 三、Pyinstaller打包cefpython3应用：`首先理解Pyinstaller的是什么，为什么和怎么使用，然后以遇到问题解决问题的方式打包应用。`
 四、总结：`对文章作简要总结和说明。`

### 一、cefpython3的浅显理解

#### 1.1 是什么？

cefpython3其上游是C++开发的CEF（基于webkit、V8），CEF即(Chromium Embedder Framework)，是基于Google Chromium项目的开源Web browser控件。

**cefpython3可应用于HTML5界面软件的开发，或将其嵌入到其他GUI框架，如PyQt、wxWidgets等；或应用于web自动化测试、爬虫等，如requests、selenium等。**

#### 1.2 为什么？

cefpython3是随着cef而出现，Cpython性能不如C++，但是生成同样的应用，可能有时候我们会更倾向于更`简化且易于理解`的接口。

cefpython3并未全部实现CEF(C++)所有接口（50%左右），实现的有些接口也是待优化的状态，cefpython3虽并非一个成熟的项目，但是其也有可取之处：
 **1. 了解实现浏览器功能的过程，助于开发安全的web应用**
 **2. 通过控制浏览器，可以做一些关于web的自动化任务**
 **3. 将其嵌入到其他框架开发，减少项目开发周期**
 **4. 制作HTML5界面软件等**

#### 1.3 怎么样？

如何应用的前提是我们首先要知道它有什么？可查看github文档[API categories](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FAPI-categories.md)
 以对项目提供的API有个整体的把握！下面将其划分为五个部分来介绍：
 **1. 安装和使用**
 **2. 创建浏览器**
 **3. 控制浏览器**
 **4. 嵌入GUI框架**
 **5. cefpython3应用编译链接为shell可执行文件**

### 二、cefpython3的简单应用

> 以下内容只在Windows系统中测试通过，并不保证在Linux/Mac正常执行；为了让读者进一步学习和理解，在例子中给出了github文档中相关的链接。

#### 2.1 安装和使用

##### 2.1.1 安装



```bash
# 或你应该先创建一个虚拟环境env
pip install --user cefpython3
```

##### 2.1.2 使用



```python
# 查看是否能正常运行
from cefpython3 import cefpython as cef
print(cef.GetVersion())  
```

#### 2.2 创建浏览器

可参考github文档给出的例子[hello_world.py](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fexamples%2Fhello_world.py)

##### 2.2.1 示例代码



```python
from cefpython3 import cefpython as cef
import sys

# 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
sys.excepthook = cef.ExceptHook  

# 创建浏览器
cef.Initialize()
cef.CreateBrowserSync(url="https://www.baidu.com")

# 消息循环：监听信号和处理事件
cef.MessageLoop()

# 结束进程
cef.Shutdown()
```

##### 2.2.2 创建浏览器的示例代码说明

- 创建应用和配置

> bool cef.Initialize(settings={...},switches={...})



```python
from cefpython3 import cefpython as cef

settings = {
    "debug": True,  # 调试模式
    "log_severity": cef.LOGSEVERITY_INFO, # 日志的输出级别
    "log_file": "debug.log",  # 设置日志文件
    "user_agent": "from stonejianbu 0.0.1", 
}
switches = {
    "enable-media-stream": "",  # 取消获取媒体流（如音频、视频数据），必须以空字符串代表否！
    "proxy-server": "socks5://127.0.0.1:8888",  # 设置代理
    "disable-gpu": "",  # 设置渲染方式CPU or GPU
}

cef.Initialize(settings=settings, switches=switches)
```

关于cef应用的更多设置，可参考github文档[cef](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2Fcefpython.md)、[cef-switches](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FCommandLineSwitches.md)、[cef-settings](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FApplicationSettings.md)

- 加载浏览器和配置参数

> browser cef.CreateBrowserSync(window_info=cef.WindowInfo(), settings={..}, url="..", window_title="..")



```php
settings={
    "image_load_disabled": True,  # 设置不加载图片
}
cef.CreateBrowserSync(url="https://www.baidu.com/",
                          window_title="百度一下",
                          settings=settings)
```

关于browser的更多设置，可参考github文档[browser-settings](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FBrowserSettings.md)、[cef-WindoInfo](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FWindowInfo.md)

#### 2.3 控制浏览器

可参考github文档给出例子[tutorial.py](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fexamples%2Ftutorial.py)，但是其例子稍显复杂化，对于beginner来说是有些费解的！

##### 2.3.1 示例代码



```python
"""
创建一个浏览器加载`https://www.baidu.com`，然后通过javascript往查询框输入值并点击查询
"""
from cefpython3 import cefpython as cef
import sys


# 关于浏览器事件的客户端处理器
class LoadHandler:
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """当前页面加载状态发生变化的时候被调用"""
        print("页面正在加载....")
        if not is_loading:
            print("页面加载完成....")
            browser.ExecuteJavascript(self._jsCode())
            
    # 注意非client Handlers预定义的方法应该与自定义方法区别而在方法名前添加_
    def _jsCode(self):  
        jsCode = """
        // 通过id获取百度输入框元素
        var input_search = document.getElementById('kw');
        // 设置输入框的值为python
        input_search.value = "python";
        // 点击查询
        document.getElementById('su').click();
        """
        return jsCode


# 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
sys.excepthook = cef.ExceptHook

# 创建application: bool cef.Initialize(settings={...},switches={...})
cef.Initialize()

# 创建browser: browser cef.CreateBrowserSync(window_info=cef.WindowInfo(), settings={..}, url="..", window_title="..")
browser = cef.CreateBrowserSync(url="https://www.baidu.com")

# 添加关于浏览器事件的客户端处理器: void browser.SetClientHandler(clientHandler object)
browser.SetClientHandler(LoadHandler())

# 消息循环：监听信号和处理事件
cef.MessageLoop()

# 结束进程
cef.Shutdown()
```

##### 2.3.2 js控制浏览器的示例代码说明

- 1.捕捉事件并简单响应

cefpython3中提供了关于Chromium事件通知的接口类[Client handlers](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FAPI-categories.md%23client-handlers-interfaces)，
 如`RequestHandler`、`LoadHandler`、`RenderHandler`、`DisplayHandler`等等。我们需要做的是重写这些类及其方法，注意不是继承而是重写，然后将重写的类与browser绑定！对于这些*client handler*类有哪些方法可以重写，这需要查看相关文档！



```python
"""
添加LoadHandler以捕捉浏览器加载事件，然后提示加载完成！
"""
from cefpython3 import cefpython as cef
import sys

# 关于浏览器事件的客户端处理器
class LoadHandler:
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """当前页面加载状态发生变化的时候被调用"""
        print("页面正在加载....")
        if not is_loading:
            print("页面加载完成....")


# 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
sys.excepthook = cef.ExceptHook

# 创建application: bool cef.Initialize(settings={...},switches={...})
cef.Initialize()

# 创建browser: browser cef.CreateBrowserSync(window_info=cef.WindowInfo(), settings={..}, url="..", window_title="..")
browser = cef.CreateBrowserSync(url="https://www.baidu.com")

# 添加关于浏览器事件的客户端处理器: void browser.SetClientHandler(clientHandler object)
browser.SetClientHandler(LoadHandler())

# 消息循环：监听信号和处理事件
cef.MessageLoop()

# 结束进程
cef.Shutdown()
```

关于client handlers的更多类及其方法的使用，可参考github文档[SetGlobalClientHandler](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2Fcefpython.md%23setglobalclienthandler)、[SetClientHandler](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FBrowser.md%23setclienthandler)、[LoadHandler](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FLoadHandler.md%23loadhandler-interface)等！

- 2.绑定javaScript来控制浏览器

> browser.ExecuteJavascript(jsCode_str, scriptUrl="", startLine=1)

**javaScript可由浏览器直接解释执行，可用于web页面的动态交互**。绑定javaScript来控制浏览器，换言之，`使用python代码来将JavaScript代码交由浏览器来解释执行`，可参考github文档[browser.ExecuteJavascript](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FBrowser.md%23executejavascript)。



```python
/*javaScript代码如下，通过往百度一下的输入框中输入`python`，然后点击查询*/
JavaScript_code = """
// 通过id获取百度输入框元素
var input_search = document.getElementById('kw');
// 设置输入框的值为python
input_search.value = "python";
// 点击查询
document.getElementById('su').click();
"""
browser.ExecuteJavascript(JavaScript_code)
```

关于python与JavaScript交互的实现，可参考github文档[void browser.executeFunction(funcName,params..)](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FBrowser.md%23executefunction)、[JavascriptBindings_object cef.JavascriptBindings](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FJavascriptBindings.md)、[void browser.SetJavascriptBindings(JavascriptBindings object)](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FBrowser.md%23setjavascriptbindings)等！

#### 2.4 嵌入PyQt框架

> 在开始介绍之前，我们不妨想一想？如何将两个互不相干的东西结合在一起呢？纽带？桥梁？API？...

cefpython3和PyQt5虽互为独立，但是它们都是依托于特定的操作系统，如在windows程序中，有各种各样的资源（窗口、图标、光标等），系统在创建这些资源时会为他们分配内存，并返回标示这些资源的标示号，即[句柄](https://links.jianshu.com/go?to=https%3A%2F%2Fbaike.baidu.com%2Fitem%2Fhandle%2F2971688%3Ffr%3Daladdin)；由此，我们可以通过以Qt作为主窗口，且预留一个空位置给cef,cef通过获取Qt句柄来显示到空位置上，如此就把它们`拼接`在了一起!

可参考github文档给出的示例[qt.py](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fexamples%2Fqt.py)，给出的例子用一份代码包含了PyQt4、PyQt5和PySide在linux、windows、Mac运行的测试，由于`cef.MessageLoop()`和PyQt上的`app.exec_()`否是循环等待处理，如果使用单线程处理，似乎这是难以实现的(当然可以尝试考虑使用协程、多进程)；但是我接下来介绍的是PyQt5在windows上运行的例子，使用了多线程处理`multi_threaded_message_loop`，了解在不同系统的不同处理[Message Loop](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fdocs%2FTutorial.md%23message-loop)。 现在思路有了，那么怎么实现呢？我将上面的思路划分为3个步骤:
 `1. 将PyQt作为主窗口并预留一个空位置`
 `2. cef获取PyQt窗口控件的句柄并显示到空位置上`
 `3. 多线程处理`

##### 2.4.1 示例代码



```python
"""
将cefpython3嵌入到PyQt5中，往输入框中输入URL地址，点击查询，创建浏览器并加载HTML内容显示
"""
from PyQt5 import QtWidgets
from cefpython3 import cefpython as cef
import sys

# 浏览器内容窗口
class CefBrowser(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.browser = None
        super().__init__(parent)

    def create_browser(self, window_info, url):
        self.browser = cef.CreateBrowserSync(window_info, url=url)

    def embedBrowser(self, url):
        window_info = cef.WindowInfo()
        # void window_info.SetAsChild(int parentWindowHandle, list windowRect), windowRect~[left,top,right,bottom]
        window_info.SetAsChild(int(self.winId()), [0, 0, self.width(), self.height()])
        cef.PostTask(cef.TID_UI, self.create_browser, window_info, url)

# Qt主窗口
class BrowserWindow:
    def setUI(self, MainWindow):
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("cefpython3-PyQt5")

        # URL输入框、查询按钮、浏览器控件
        self.le_search = QtWidgets.QLineEdit()
        self.le_search.setPlaceholderText("输入网址...")
        self.btn_search = QtWidgets.QPushButton()
        self.btn_search.setText("查询")
        self.browser_widget = CefBrowser()

        # 设置布局方式：栅栏式
        self.main_layout = QtWidgets.QGridLayout(MainWindow)
        self.main_layout.addWidget(self.le_search, 0, 0, 1, 1)
        self.main_layout.addWidget(self.btn_search, 0, 1, 1, 1)
        self.main_layout.addWidget(self.browser_widget, 1, 0, 8, 2)

        # 信号和槽函数
        self.signal_slots()

    def signal_slots(self):
        # 绑定`查询`按钮的点击事件
        self.btn_search.clicked.connect(self.slot_load_url)

    def slot_load_url(self):
        """获取输入框的URL，判断是否已存在browser对象，如果存在则LoadUrl否则开始创建浏览器"""
        if self.le_search.text():
            if self.browser_widget.browser:
                self.browser_widget.browser.LoadUrl(self.le_search.text())
            else:
                self.browser_widget.embedBrowser(self.le_search.text())

    def show(self):
        """创建和显示应用窗口，循环监听处理"""
        app = QtWidgets.QApplication([])
        widget = QtWidgets.QWidget()
        main_window = BrowserWindow()
        main_window.setUI(widget)
        widget.show()
        app.exec_()


if __name__ == "__main__":
    sys.excepthook = cef.ExceptHook
    # bool cef.Initialize(settings={...},switches={...})
    cef.Initialize(settings={"multi_threaded_message_loop": True})
    BrowserWindow().show()
    cef.Shutdown()
```

##### 2.4.2 嵌入Qt框架的示例代码说明

- 1.将PyQt作为主窗口并预留一个空位置



```python
"""
创建简单浏览器窗口：输入框、查询按钮、预留的内容窗口
这里不对PyQt5的知识点作过多介绍，以下给出的例子尽可能简单
"""
from PyQt5 import QtWidgets


class BrowserWindow:
    def setUI(self, MainWindow):
        # 设置主窗口大小和标题
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("cefpython3-PyQt5")

        # URL输入框、查询按钮、浏览器控件
        self.le_search = QtWidgets.QLineEdit()
        self.le_search.setPlaceholderText("输入网址...")
        self.btn_search = QtWidgets.QPushButton()
        self.btn_search.setText("查询")
        # 将CefBrowser类实例化作为PyQt的子控件，用来显示HTML页面
        self.browser_widget = CefBrowser()    

        # 设置布局方式：栅栏式
        self.main_layout = QtWidgets.QGridLayout(MainWindow)
        self.main_layout.addWidget(self.le_search, 0, 0, 1, 1)
        self.main_layout.addWidget(self.btn_search, 0, 1, 1, 1)
        self.main_layout.addWidget(self.browser_widget, 1, 0, 8, 2)

        # 信号和槽函数
        self.signal_slots()

    def signal_slots(self):
        # 绑定`查询`按钮的点击事件
        self.btn_search.clicked.connect(self.slot_load_url)

    def slot_load_url(self):
        """获取输入框的URL，判断是否已存在browser对象，如果存在则LoadUrl否则开始创建浏览器"""
        if self.le_search.text():
            if self.browser_widget.browser:
                self.browser_widget.browser.LoadUrl(self.le_search.text())
            else:
                self.browser_widget.embedBrowser(self.le_search.text())

    def show(self):
        """创建和显示应用窗口，循环监听处理"""
        app = QtWidgets.QApplication([])
        widget = QtWidgets.QWidget()
        main_window = BrowserWindow()
        main_window.setUI(widget)
        # 显示主窗口
        widget.show()
        # 循环监听处理事件
        app.exec_()
```

- 2.cef获取PyQt窗口控件的句柄并显示到空位置上

> void window_info.SetAsChild(int parentWindowHandle, list windowRect)

首先,PyQt控件的句柄是通过`winId()`方法获取，`CefBrowser`继承于`QtWidgets.QWidget`，则获取其的句柄通过`self.winId()`；用于设置浏览器的显示方式的类[WindowInfo](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2FWindowInfo.md)。



```python
class CefBrowser(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.browser = None
        super().__init__(parent)

    def create_browser(self, window_info, url):
        self.browser = cef.CreateBrowserSync(window_info, url=url)

    def embedBrowser(self, url):
        window_info = cef.WindowInfo()
        # 设置以浏览器以子窗口显示，SetAsChild有两个参数，一个是父窗口的句柄，另一个是设置窗口位置列表[left,right,width,height]
        window_info.SetAsChild(int(self.winId()), [0, 0, self.width(), self.height()])
        
        # 设置以UI线程来创建浏览器，void cef.PostTask(线程，funcName, [params...]),传入funcName函数的参数不能是关键字
        cef.PostTask(cef.TID_UI, self.create_browser, window_info, url)
```

- 3.Windows系统中设置多线程处理

关于多线程处理和设置创建浏览器为UI线程的解释，请参考[PostTask](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fapi%2Fcefpython.md%23posttask)



```php
下面直接给出说明，其中需要修改的地方分别是：
1. 给cef添加设置：cef.Initialize(settings={"multi_threaded_message_loop": True})
2. 将UI线程作为创建浏览器的线程：cef.PostTask(cef.TID_UI, self.create_browser, window_info, url)，如之前说明
3. 不再需要手动调用：cef.MessageLoop()
```

### 三、 cefpython3应用编译链接为shell可执行文件

下面使用Pyinstaller作为打包工具，将github文档给出的例子[hello_world.py](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython%2Fblob%2Fmaster%2Fexamples%2Fhello_world.py)作为打包应用的示例。

#### 3.1 Pyinstaller的基本概念

##### 3.1.1 是什么？

Pyinstaller读取你所写的py脚本，它**递归分析**脚本主程序代码运行所需的模块、库文件以及python解释器，然后将它们都**复制**到单个目录中或编译为单个可执行文件。

##### 3.1.2 为什么？

python脚本只能由python解释器执行，若想让特定系统shell来执行则需要转换为符合特定系统所规定格式,如windows系统下的`*.com、*.exe`是直接可执行的格式；而python脚本是需要经过`编译`和`链接`。Pyinstaller作为一个高级的API，可以地轻松这一任务，而我们无需去关注如何编译?如何链接？`*.exe`具体的格式什么？

##### 3.1.3 怎么样？

如何应用？下面将从3个小步骤来说明，以一个最小化单元执行：
 `1. 简单分析说明Pyinstaller提供的接口`
 `2. 使用Pyinstaller开始打包`
 `3. 解决异常问题`
 `4. 执行最小化的完整的打包过程`

#### 3.2 Pyinstaller打包cefpython3应用

##### 3.2.1 安装和查看API



```jsx
1. 安装：pip install --user Pyinstaller
2. 查看帮助信息：Pyinstaller -h
3. 说明常用参数：-w              无console  
                -i title.ico    指定图标
                -F              打包为单个文件
                --hidden-import module_name   手动添加Pyinstaller无法获取到的必要模块
                .....
```

##### 3.2.2 开始使用



```python
import cefpython3
import subprocess
import os

# 获取cefpython3包提供的hello_world.py文件
hd_file = os.path.dirname(cefpython3.__file__) + "\\examples\\hello_world.py"
print("*******打包cefpython3应用：", hd_file)

# 相当于执行打包命令： Pyinstaller hello_world.py
subprocess.run("Pyinstaller {}".format(hd_file))
print("********打包成功!*******")

# 打包完成后，尝试启动可执行程序hello_world.exe
print("********开始执行，成功打包的应用：")
subprocess.run("./dist/hello_world/hello_world.exe")
# 如果执行后能出现标题为hell_world的弹窗，那恭喜你，否则继续往下看！
```

##### 3.2.3 解决异常问题

我将目前出现的错误归结为依赖错误，划分为两种类型的依赖问题：
 `1. 隐藏模块问题`
 `2. 其他依赖问题`

- 1. 隐藏模块问题：如`ModuleNotFoundError: No module named 'json'`错误



```python
# 对于Pyinstaller无法识别的隐藏模块，我们需要手动告诉它，如添加--hidden-import json
# 在执行以下脚本之前请先删除之前打包完成的文件和目录build、dist、hello_world.spec
import cefpython3
import subprocess
import os
    
# 获取cefpython3包提供的hello_world.py文件
hd_file = os.path.dirname(cefpython3.__file__) + "\\examples\\hello_world.py"
print("*******打包cefpython3应用：", hd_file)
    
# 相当于执行打包命令： Pyinstaller hello_world.py
subprocess.run("Pyinstaller --hidden-import json {}".format(hd_file))
print("********打包成功!*******")
    
# 打包完成后，尝试执行可执行程序hello_world.exe
print("********开始执行，成功打包的应用：")
subprocess.run("./dist/hello_world/hello_world.exe")
# 如果执行后能出现标题为hell_world!的弹窗，那恭喜你，否则继续往下看！
```

- 1. 其他依赖问题

由于cefpython3并不是由python直接编写而是由C++转换编译，其包含了`dll、pak、bin、exe、dat`等文件而目前Pyinstaller是不能够自动地将这些文件复制执行文件目录下，而使得可执行文件不能正常调用依赖文件而无法正常启动。如何解决这种问题呢？三个方法如下：
 `1. 告诉Pyinstaller让它在打包过程中帮我们把依赖文件复制过来`
 `2. 找到cefpython3包，手动复制过来一份放到可执行文件的目录`
 `3. 编写脚本代码将依赖文件复制到可执行文件的目录`



```python
"""   
下面我使用的是第三种方法，配合使用os和shutil模块完成Pyinstaller打包cefpython3应用
""" 
import os
import shutil
        
# 将一个文件夹中的指定文件复制到另一个文件夹中
def copytree(src, dst, ignores_suffix_list=None):
    os.makedirs(dst, exist_ok=True)
    names = [os.path.join(src, name) for name in os.listdir(src)]
    for name in names:
        exclude = False
        for suffix in ignores_suffix_list:
            if name.endswith(suffix):
                exclude = True
                continue
        if not exclude:
            if os.path.isdir(name):
                new_dst = os.path.join(dst, os.path.basename(name))
                shutil.copytree(name, new_dst, ignore=shutil.ignore_patterns(*ignores_suffix_list))
            else:
                shutil.copy(name, dst)
```

##### 3.2.4 完整打包示例代码



```python
import cefpython3
import subprocess
import os
import shutil


class PyinstallerCefpython:
    def __init__(self):
        self.no_suffix_script_name = "hello_world"
        # cefpython3的包目录
        self.cef_dir = os.path.dirname(cefpython3.__file__)
        # 获取cefpython3包下examples目录下的hello_world.py
        self.script_file = os.path.join(os.path.join(self.cef_dir, "examples"), "hello_world.py")

    def delete_before_generates(self):
        """删除之前打包生成的文件"""
        print("*******正在删除之前打包的生成文件....")
        try:
            shutil.rmtree("./dist")
            shutil.rmtree("./build")
            os.remove("{}.spec".format(self.no_suffix_script_name))
        except Exception as e:
            pass
        print("*******删除成功！")

    def script_to_exe(self):
        # 相当于执行打包命令： Pyinstaller hello_world.py
        print("*******开始打包cefpython3应用：", self.script_file)
        subprocess.run("Pyinstaller --hidden-import json {}".format(self.script_file))

    def copytree(self, src, dst, ignores_suffix_list=None):
        print("********正在复制将{}目录下的文件复制到{}文件夹下....".format(src, dst))
        os.makedirs(dst, exist_ok=True)
        names = [os.path.join(src, name) for name in os.listdir(src)]
        for name in names:
            exclude = False
            for suffix in ignores_suffix_list:
                if name.endswith(suffix):
                    exclude = True
                    continue
            if not exclude:
                if os.path.isdir(name):
                    new_dst = os.path.join(dst, os.path.basename(name))
                    shutil.copytree(name, new_dst, ignore=shutil.ignore_patterns(*ignores_suffix_list))
                else:
                    shutil.copy(name, dst)

    def solve_dependence(self):
        print("*******解决依赖：复制依赖文件到执行文件的目录下....")
        self.copytree(self.cef_dir, "./dist/{}".format(self.no_suffix_script_name), [".txt", ".py", ".log", "examples", ".pyd", "__"])

    def exec_application(self):
        print("*******执行成功打包的应用....")
        subprocess.run("./dist/{0}/{0}.exe".format(self.no_suffix_script_name))

    def run(self):
        self.delete_before_generates()
        self.script_to_exe()
        self.solve_dependence()
        self.exec_application()
      
    
if __name__ == "__main__":
  PyinstallerCefpython().run()
```

### 四、简单总结

本文既是个人知识点的总结，同时也为分享更多人来了解和进行cefpython3应用的开发，以上所作分析是基于**易于理解**和**了解使用方向**的目的，所有的例子都是可扩展和优化的，比如更多的cef和browser**功能设置**、`client handler`的更多操作、**控制浏览器**的复杂操作、简单浏览器的**自适应大小**和**Focus问题**和编写更通用和包含异常处理的`Pyinstaller-cefpython`接口等等。

更多的`细节`和`扩展`还需要读者自行查看[官方文档](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fcztomczak%2Fcefpython)或评论交流学习。


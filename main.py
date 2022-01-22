from cefpython3 import cefpython as cef
import sys

# 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
sys.excepthook = cef.ExceptHook

# 创建浏览器
from cefpython3 import cefpython as cef

cef.Initialize()
browser = cef.CreateBrowserSync(url="http://www.bilibili.com/")

browser.ExecuteJavascript("alert(\"Hello World!\")")

# 消息循环：监听信号和处理事件
cef.MessageLoop()

# 结束进程
cef.Shutdown()

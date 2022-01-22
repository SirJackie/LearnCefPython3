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

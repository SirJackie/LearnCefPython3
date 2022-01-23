from cefpython3 import cefpython as cef
from BrowserHelper import *


# 关于浏览器事件的客户端处理器
class LoadHandler:
    def OnLoadingStateChange(self, browser, is_loading, **_):
        # 当前页面加载状态发生变化的时候被调用
        # print("页面正在加载....")
        if not is_loading:
            # print("页面加载完成....")
            browser.ExecuteJavascript("var pyMsg = \"Hello World!\";")


browser = CreateBrowser("./HTMLSourceCodes/index.html")
browser.SetClientHandler(LoadHandler())

cef.MessageLoop()
cef.Shutdown()

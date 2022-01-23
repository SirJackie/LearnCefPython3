from cefpython3 import cefpython as cef
from BrowserHelper import *
import win32gui
import ctypes

cef.DpiAware.EnableHighDpiSupport()


# 关于浏览器事件的客户端处理器
class LoadHandler:
    def OnLoadingStateChange(self, browser, is_loading, **_):
        # When the page is loading
        if not is_loading:
            # When the page finished loading

            # Create JS Binding Object
            js = cef.JavascriptBindings()

            # Pass Variable to JS (Variable Passing)
            js.SetProperty("pyMsg", "A String from Python.")

            # Bind Python Function to JS (JS Call Python)
            js.SetFunction("PythonFunction", PythonFunction)

            browser.SetJavascriptBindings(js)

            # Python call JS
            browser.ExecuteJavascript("JSFunction()")


count = 0


def PythonFunction():
    global count
    count += 1
    print("Python received a call from JS for the", str(count) + "th time.")


browser = CreateBrowser("./HTMLSourceCodes/index.html")

# Resize the window
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
windowWidth = screensize[0] * 0.8
windowHeight = windowWidth / 16 * 9
print(windowWidth, windowHeight)

hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 0, 0, 500, 500, True)

browser.SetClientHandler(LoadHandler())

cef.MessageLoop()
cef.Shutdown()

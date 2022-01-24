from cefpython3 import cefpython as cef
from BrowserHelper import *
import win32gui
import win32api
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


def GetTaskBarHeight():
    monitorInfo = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
    monitorArea = monitorInfo.get("Monitor")
    workArea = monitorInfo.get("Work")
    taskbarHeight = monitorArea[3]-workArea[3]
    return taskbarHeight


def GetScreenSize():
    user32 = ctypes.windll.user32
    screenWidth = user32.GetSystemMetrics(0)
    screenHeight = user32.GetSystemMetrics(1)
    return screenWidth, screenHeight


def SetWindowSizeAndPos(width, height, left, top):
    hwnd = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(hwnd, left, top, width, height, True)


def GetLeftAndTopUsingWidthAndHeight(windowWidth, windowHeight):
    screenWidth, screenHeight = GetScreenSize()
    taskbarHeight = GetTaskBarHeight()

    windowLeft = int((screenWidth - windowWidth) / 2)
    windowTop = int(((screenHeight - taskbarHeight) - windowHeight) / 2)

    return windowLeft, windowTop


screenWidth, screenHeight = GetScreenSize()
taskbarHeight = GetTaskBarHeight()

windowWidth = int(screenWidth * 0.97)
windowHeight = int((screenHeight - taskbarHeight) * 0.97)
windowLeft, windowTop = GetLeftAndTopUsingWidthAndHeight(windowWidth, windowHeight)

SetWindowSizeAndPos(windowWidth, windowHeight, windowLeft, windowTop)

browser.SetClientHandler(LoadHandler())
cef.MessageLoop()
cef.Shutdown()

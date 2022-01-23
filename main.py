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

from win32api import GetMonitorInfo, MonitorFromPoint

# Get Taskbar Height
monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
taskbarHeight = monitor_area[3]-work_area[3]
print("The taskbar height is", taskbarHeight)

# Resize the window
user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
windowWidth = int(screenWidth * 0.97)
windowHeight = int((screenHeight-taskbarHeight) * 0.97)
print(windowWidth, windowHeight)

hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, int((screenWidth-windowWidth)/2), int((screenHeight-taskbarHeight-windowHeight)/2), windowWidth, windowHeight, True)

browser.SetClientHandler(LoadHandler())

cef.MessageLoop()
cef.Shutdown()

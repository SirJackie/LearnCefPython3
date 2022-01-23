from cefpython3 import cefpython as cef
from BrowserHelper import *
import ctypes

# # Query DPI Awareness (Windows 10 and 8)
# awareness = ctypes.c_int()
# errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
# print(awareness.value)

# Set DPI Awareness  (Windows 10 and 8)
# errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
# the argument is the awareness level, which can be 0, 1 or 2:
# for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)

# # Set DPI Awareness  (Windows 7 and Vista)
# success = ctypes.windll.user32.SetProcessDPIAware()

# behaviour on later OSes is undefined, although when I run it on my Windows 10 machine,
# it seems to work with effects identical to SetProcessDpiAwareness(1)

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
browser.SetClientHandler(LoadHandler())

cef.MessageLoop()
cef.Shutdown()

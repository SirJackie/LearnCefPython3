from cefpython3 import cefpython as cef
import sys
import os
import win32gui
import win32api
import ctypes


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


def EnableHighDPISupport():
    cef.DpiAware.EnableHighDpiSupport()


def LocalizeURL(URL):
    # If the URL is based on HTTP or HTTPS protocol
    if URL[0:4] == "http":
        # Just return, don't process
        return URL

    # Linuxlize the URL
    linuxlizedURL = URL.replace("\\", "/")

    # Clean the 'this folder' definition
    if linuxlizedURL[0:2] == "./":
        linuxlizedURL = linuxlizedURL[2:]

    # Get Linuxlized CWD Path
    linuxlizedCWD = os.getcwd().replace("\\", "/")

    # Merge and Generate the Target URL
    targetURL = "file:///" + linuxlizedCWD + "/" + linuxlizedURL
    return targetURL


def VariableHookee(url, name, value):
    return {
        "type": "VariableHookee",
        "url": LocalizeURL(url) if url is not None else None,
        "name": name,
        "value": value
    }


def FunctionHookee(url, name, function):
    return {
        "type": "FunctionHookee",
        "url": LocalizeURL(url) if url is not None else None,
        "name": name,
        "function": function
    }


def CodeHookee(url, jsCode):
    return {
        "type": "CodeHookee",
        "url": LocalizeURL(url) if url is not None else None,
        "jsCode": jsCode
    }


class Communicator:
    # Public Hookees
    hookees = []

    # Hooker
    @classmethod
    def OnLoadingStateChange(cls, browser, is_loading, **_):
        # When the page is loading
        if not is_loading:
            # When the page finished loading

            # Create JS Binding Object
            js = cef.JavascriptBindings()

            for hookee in cls.hookees:
                if hookee["type"] == "VariableHookee":
                    # Pass Variable to JS
                    js.SetProperty(hookee["name"], hookee["value"])
                elif hookee["type"] == "FunctionHookee":
                    # Bind Python Function to JS
                    js.SetFunction(hookee["name"], hookee["function"])
                elif hookee["type"] == "CodeHookee":
                    # Python execute JS Code (immediately)
                    browser.ExecuteJavascript(hookee["jsCode"])

            # Finish JS Binding Task
            browser.SetJavascriptBindings(js)


#
# The Browser Class
#

# You have to notice that you can't create multiple browser instances
# Due to the share of Communicator class's static property 'hookees'.
# If I want to solve this problem, I may use metaclass to produce multiple Communicator classes.
# But I don't think it is necessary as long as the Browser class is depended on single thread

class Browser:
    url = None
    browser = None

    def __init__(self, url_):
        self.Initialize(url_)
        self.AutoResizeWindow()

    def Initialize(self, url_):
        sys.excepthook = cef.ExceptHook
        EnableHighDPISupport()
        cef.Initialize(settings={}, switches={'disable-gpu': ""})
        self.url = url_
        self.browser = cef.CreateBrowserSync(url=LocalizeURL(self.url))

    @staticmethod
    def AutoResizeWindow():
        screenWidth, screenHeight = GetScreenSize()
        taskbarHeight = GetTaskBarHeight()

        windowWidth = int(screenWidth * 0.97)
        windowHeight = int((screenHeight - taskbarHeight) * 0.97)
        windowLeft, windowTop = GetLeftAndTopUsingWidthAndHeight(windowWidth, windowHeight)

        SetWindowSizeAndPos(windowWidth, windowHeight, windowLeft, windowTop)

    @staticmethod
    def AddHookee(hookee):
        Communicator.hookees.append(hookee)

    def Run(self):
        self.browser.SetClientHandler(Communicator())
        cef.MessageLoop()
        cef.Shutdown()

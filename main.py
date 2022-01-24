from cefpython3 import cefpython as cef
from BrowserHelper import *
from WindowHelper import *


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


count = 0


def PythonFunction():
    global count
    count += 1
    print("Python received a call from JS for the", str(count) + "th time.")


EnableHighDPISupport()
browser = CreateBrowser("./HTMLSourceCodes/index.html")

screenWidth, screenHeight = GetScreenSize()
taskbarHeight = GetTaskBarHeight()

windowWidth = int(screenWidth * 0.97)
windowHeight = int((screenHeight - taskbarHeight) * 0.97)
windowLeft, windowTop = GetLeftAndTopUsingWidthAndHeight(windowWidth, windowHeight)

SetWindowSizeAndPos(windowWidth, windowHeight, windowLeft, windowTop)

Communicator.hookees.append(VariableHookee(None, "pyMsg", "A String from Python."))
Communicator.hookees.append(FunctionHookee(None, "PythonFunction", PythonFunction))
Communicator.hookees.append(CodeHookee(None, "JSFunction();"))

browser.SetClientHandler(Communicator())
cef.MessageLoop()
cef.Shutdown()

# js.SetProperty("pyMsg", "A String from Python.")
# browser.ExecuteJavascript("JSFunction()")

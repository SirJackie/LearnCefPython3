from BrowserHelper import *

count = 0


def PythonFunction():
    global count
    count += 1
    print("Python received a call from JS for the", str(count) + "th time.")


browser = Browser("./HTMLSourceCodes/index.html")

browser.AddHookee(VariableHookee(None, "pyMsg", "A String from Python."))
browser.AddHookee(FunctionHookee(None, "PythonFunction", PythonFunction))
browser.AddHookee(CodeHookee(None, "JSFunction();"))
browser.Run()

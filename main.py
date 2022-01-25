from JackieBrowser import *

pythonVariable = "A String From Python"


def PythonFunction():
    print("Python received a call from JS")


browser = JackieBrowser("./HTMLSourceCodes/index.html")

browser.AddHookee(VariableHookee(None, "pyMsg", "A String from Python."))
browser.AddHookee(FunctionHookee(None, "PythonFunction", PythonFunction))
browser.AddHookee(CodeHookee(None, "JSFunction();"))
browser.Run()

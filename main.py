from JackieBrowser import *

pythonVariable = "A String From Python"


def PythonFunction():
    print("Python received a call from JS")


browser = JackieBrowser("./HTMLSourceCodes/index.html")
# browser = JackieBrowser("http://www.baidu.com/")
browser.Set("pythonVariable", pythonVariable)
browser.Add(PythonFunction)
browser.Execute("JSFunction();")
browser.Run()

from JackieBrowser import *

pythonVariable = "A String From Python"


def PythonFunction():
    print("Python received a call from JS")


browser = JackieBrowser("./HTMLSourceCodes/index.html")
# browser = JackieBrowser("http://www.baidu.com/")
# browser.Set(None, "pythonVariable", pythonVariable)
# browser.Add(None, PythonFunction)
# browser.Execute(None, "JSFunction();")
browser.Execute("https://www.baidu.com/", "alert(\"Hello World!\");")
browser.Run()

from JackieBrowser import *

pythonVariable = "A String From Python"


def PythonFunction():
    print("Python received a call from JS")


browser = JackieBrowser("./HTMLSourceCodes/index.html")
browser.Set(None, "pythonVariable", pythonVariable)
browser.Add("./HTMLSourceCodes/index.html", PythonFunction)
browser.Execute("https://www.baidu.com/", "alert(\"JS received a call from Python when accessing Baidu.\");")
browser.Run()

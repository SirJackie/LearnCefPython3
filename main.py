from cefpython3 import cefpython as cef
import sys
import os

# file:///C:/Users/Admin/Desktop/Projects/learn-cefpython3/HTMLSourceCodes/index.html

url = "HTMLSourceCodes/index.html"
cwd = "file:///" + os.getcwd().replace("\\", "/") + "/"
targetURL = cwd + url
print(targetURL)

sys.excepthook = cef.ExceptHook
cef.Initialize()
browser = cef.CreateBrowserSync(url=targetURL)
browser.ExecuteJavascript("alert(\"Hello World!\")")
cef.MessageLoop()
cef.Shutdown()

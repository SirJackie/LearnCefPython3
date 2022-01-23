from cefpython3 import cefpython as cef
from BrowserHelper import *

browser = CreateBrowser("./HTMLSourceCodes/index.html")
browser.ExecuteJavascript("alert(\"Hello World!\")")
cef.MessageLoop()
cef.Shutdown()

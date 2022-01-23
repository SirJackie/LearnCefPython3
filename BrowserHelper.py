from cefpython3 import cefpython as cef
import sys
import os


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


def CreateBrowser(URL):
    sys.excepthook = cef.ExceptHook
    cef.Initialize(settings={}, switches={'disable-gpu': ""})
    browser = cef.CreateBrowserSync(url=LocalizeURL(URL))
    return browser

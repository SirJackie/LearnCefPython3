from cefpython3 import cefpython as cef
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

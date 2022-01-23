# [How to get the height of Windows Taskbar using Python/PyQT/Win32](https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32)

Source: https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32

[Ask Question](https://stackoverflow.com/questions/ask)

Asked 11 years, 1 month ago

Active [1 year, 10 months ago](https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32?lastactivity)

Viewed 5k times



6

1

I am trying to make my GUI program align to the bottom-right of the screen on Windows. When the taskbar is not hidden, my program will just stand on top of the taskbar!

When using Python/PyQT/Win32, how can I:

1. Check if the taskbar's autohide function is on
2. Get the height of the taskbar

[python](https://stackoverflow.com/questions/tagged/python)[windows](https://stackoverflow.com/questions/tagged/windows)[winapi](https://stackoverflow.com/questions/tagged/winapi)[pyqt](https://stackoverflow.com/questions/tagged/pyqt)

[Share](https://stackoverflow.com/q/4357258)

Follow

[edited Jul 30 '18 at 19:58](https://stackoverflow.com/posts/4357258/revisions)

[![img](a.assets/jaomO.png)](https://stackoverflow.com/users/3357935/stevoisiak)

[Stevoisiak](https://stackoverflow.com/users/3357935/stevoisiak)

**18.8k**2121 gold badges102102 silver badges188188 bronze badges

asked Dec 5 '10 at 3:47

[![img](a.assets/a6c564808a2c3c9e3558fda9599c8b6c.png)](https://stackoverflow.com/users/527565/good-man)

[good man](https://stackoverflow.com/users/527565/good-man)

**329**66 silver badges1515 bronze badges

- Related: [How do I get monitor resolution in Python?](https://stackoverflow.com/q/3129322/3357935) 

[Add a comment](https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32#)



## 3 Answers

[Active](https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32?answertab=active#tab-top)[Oldest](https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32?answertab=oldest#tab-top)[Votes](https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32?answertab=votes#tab-top)





20



As [David Heffernan mentioned](https://stackoverflow.com/a/4358236/3357935), you can use [`GetMonitorInfo`](http://msdn.microsoft.com/en-us/library/dd144901.aspx) with [`pywin32`](https://pypi.org/project/pywin32/) to retrieve the monitor size. In particular, the work area will exclude the size of the taskbar.

**To get the work area size (desktop minus taskbar):**

```py
from win32api import GetMonitorInfo, MonitorFromPoint

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
print("The work area size is {}x{}.".format(work_area[2], work_area[3]))
```

> The work area size is 1366x728.

**To get the taskbar height:**

```py
from win32api import GetMonitorInfo, MonitorFromPoint

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
print("The taskbar height is {}.".format(monitor_area[3]-work_area[3]))
```

> The taskbar height is 40.

### Explanation

First, we need to create a handle referencing the primary monitor. The primary monitor [always has its upper left corner at 0,0](http://blogs.msdn.com/b/oldnewthing/archive/2007/08/09/4300545.aspx), so we can use:

```py
primary_monitor = MonitorFromPoint((0,0))
```

We retrieve information about the monitor with `GetMonitorInfo()`.

```py
monitor_info = GetMonitorInfo(primary_monitor)
# {'Monitor': (0, 0, 1366, 768), 'Work': (0, 0, 1366, 728), 'Flags': 1, 'Device': '\\\\.\\DISPLAY1'}
```

The monitor information is returned as a `dict`. The first two entries represent the monitor size and the work area size as tuples (x position, y position, height, width).

```py
work_area = monitor_info.get("Work")
# (0, 0, 1366, 728)
```



[Share](https://stackoverflow.com/a/51602236)

Follow

[edited Aug 1 '18 at 17:21](https://stackoverflow.com/posts/51602236/revisions)

answered Jul 30 '18 at 21:01

[![img](https://i.stack.imgur.com/jaomO.png?s=64&g=1)](https://stackoverflow.com/users/3357935/stevoisiak)

[Stevoisiak](https://stackoverflow.com/users/3357935/stevoisiak)

**18.8k**2121 gold badges102102 silver badges188188 bronze badges

[Add a comment](https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32#)
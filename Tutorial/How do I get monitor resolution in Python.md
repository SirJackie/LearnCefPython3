# [How do I get monitor resolution in Python?](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python)

Source: https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

[Ask Question](https://stackoverflow.com/questions/ask)

Asked 11 years, 7 months ago

Active [11 days ago](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python?lastactivity)

Viewed 233k times



161

51

What is the simplest way to get monitor resolution (preferably in a tuple)?

[python](https://stackoverflow.com/questions/tagged/python)[screen](https://stackoverflow.com/questions/tagged/screen)[resolution](https://stackoverflow.com/questions/tagged/resolution)

[Share](https://stackoverflow.com/q/3129322)

Follow

[edited May 18 '15 at 1:44](https://stackoverflow.com/posts/3129322/revisions)

[![img](a.assets/ZHHFv.jpg)](https://stackoverflow.com/users/3924118/nbro)

[nbro](https://stackoverflow.com/users/3924118/nbro)

**13.4k**2323 gold badges9393 silver badges179179 bronze badges

asked Jun 27 '10 at 23:39

[![img](a.assets/20416c585ab7b81d4d4eb9a1765a0d07.png)](https://stackoverflow.com/users/433417/rectangletangle)

[rectangletangle](https://stackoverflow.com/users/433417/rectangletangle)

**45.7k**8888 gold badges191191 silver badges270270 bronze badges

- Are you using a particular UI toolkit? (eg. GTK, wxPython, Tkinter, etc) 

- 12

  With the `Tkinter` module, you can do it [this way](http://stackoverflow.com/questions/3949844/python-calculate-the-screen-size/3949983#3949983). It's part of the standard Python library and works on most Unix and Windows platforms. 

- 1

  A good overview over different techniques for common UIs is given at [this link](https://www.blog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/) 

[Add a comment](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python#)



## 31 Answers

[Active](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python?answertab=active#tab-top)[Oldest](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python?answertab=oldest#tab-top)[Votes](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python?answertab=votes#tab-top)

1

[2](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python?page=2&tab=votes#tab-top)[Next](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python?page=2&tab=votes#tab-top)





140



In Windows, you can also use ctypes with [`GetSystemMetrics()`](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724385(v=vs.85).aspx):

```py
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
```

so that you don't need to install the pywin32 package; it doesn't need anything that doesn't come with Python itself.

For multi-monitor setups, you can retrieve the combined width and height of the virtual monitor:

```py
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
```



[Share](https://stackoverflow.com/a/3129524)

Follow

[edited Jul 31 '18 at 20:06](https://stackoverflow.com/posts/3129524/revisions)

[![img](a.assets/jaomO-1642927347467.png)](https://stackoverflow.com/users/3357935/stevoisiak)

[Stevoisiak](https://stackoverflow.com/users/3357935/stevoisiak)

**18.8k**2121 gold badges102102 silver badges188188 bronze badges

answered Jun 28 '10 at 0:54

[![img](a.assets/ab32a6cf233e27f498908c1b5a785360.jpeg)](https://stackoverflow.com/users/234287/jcao219)

[jcao219](https://stackoverflow.com/users/234287/jcao219)

**2,660**33 gold badges2020 silver badges2222 bronze badges

- 13

  Important note: the values returned may be incorrect if DPI scaling is used (ie: often the case on 4k displays), you have to call SetProcessDPIAware before initializing the GUI components (and not before calling the GetSystemMetrics function). This is true for most of the answers here (GTK, etc) on the win32 platform. 

- 1

  For multiple monitors, you may use GetSystemMetrics(78) and GetSystemMetrics(79) 

- @Derek What does `GetSystemMetrics(78)` and `GetSystemMetrics(79)` return?  

- @StevenVascellaro The width/height of the virtual screen, in pixels. [msdn.microsoft.com/en-us/library/windows/desktop/…](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724385(v=vs.85).aspx) 

[Add a comment](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python#)
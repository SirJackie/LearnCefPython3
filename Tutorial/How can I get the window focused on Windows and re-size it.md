# [How can I get the window focused on Windows and re-size it?](https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it)

Source: https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it

[Ask Question](https://stackoverflow.com/questions/ask)

Asked 11 years, 11 months ago

Active [11 years, 11 months ago](https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it?lastactivity)

Viewed 12k times



10

5

I want to get the focused window so I can resize it... how can I do it?

[python](https://stackoverflow.com/questions/tagged/python)[windows](https://stackoverflow.com/questions/tagged/windows)

[Share](https://stackoverflow.com/q/2335721)

[Improve this question](https://stackoverflow.com/posts/2335721/edit)

Follow

asked Feb 25 '10 at 16:38

[![img](a.assets/0ec16106a13b387cebbeadbd5f2d2620.png)](https://stackoverflow.com/users/281400/shady)

[Shady](https://stackoverflow.com/users/281400/shady)

**121**11 gold badge11 silver badge55 bronze badges

[Add a comment](https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it#)



## 1 Answer

[Active](https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it?answertab=active#tab-top)[Oldest](https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it?answertab=oldest#tab-top)[Votes](https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it?answertab=votes#tab-top)





16







Use the [GetForegroundWindow](http://msdn.microsoft.com/en-us/library/ms633505(VS.85).aspx) Win32 API to get the window handle.

Then use the [MoveWindow](http://msdn.microsoft.com/en-us/library/ms633534(VS.85).aspx) (or [SetWindowPos](http://msdn.microsoft.com/en-us/library/ms633545(VS.85).aspx) if you prefer) win32 API to resize the window.

Working with the Win32 API can be done directly with ctypes and working with the dlls or by using the [pywin32](http://sourceforge.net/projects/pywin32/) project.

**Edit:** Sure here is an example ([Make sure you have pywin32 installed](http://sourceforge.net/projects/pywin32/)):

```py
import win32gui
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 0, 0, 500, 500, True)
```



[Share](https://stackoverflow.com/a/2335734)

[Improve this answer](https://stackoverflow.com/posts/2335734/edit)

Follow

[edited Feb 25 '10 at 16:52](https://stackoverflow.com/posts/2335734/revisions)

answered Feb 25 '10 at 16:39

[![img](a.assets/47d8644c0ad8d89635fca422dd6d3ab5.jpeg)](https://stackoverflow.com/users/3153/brian-r-bondy)

[Brian R. Bondy](https://stackoverflow.com/users/3153/brian-r-bondy)

**323k**117117 gold badges583583 silver badges622622 bronze badges

[Add a comment](https://stackoverflow.com/questions/2335721/how-can-i-get-the-window-focused-on-windows-and-re-size-it#)
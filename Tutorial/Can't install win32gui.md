# [Can't install win32gui](https://stackoverflow.com/questions/52806906/cant-install-win32gui)

Source: https://stackoverflow.com/questions/52806906/cant-install-win32gui/57001086

[Ask Question](https://stackoverflow.com/questions/ask)

Asked 3 years, 3 months ago

Active [4 months ago](https://stackoverflow.com/questions/52806906/cant-install-win32gui/57001086?lastactivity)

Viewed 35k times



23

5

I'm trying to install win32gui with pip but I get an error:

```none
C:\Users\משתמש>pip install win32gui

Collecting win32gui
Using cached https://files.pythonhosted.org/packages/b8/75/7bed82934e51903f9d48b26b3996161bb2dce1731607b4bb7fd26003ed3e/win32gui-221.5.tar.gz
Installing build dependencies ... done
Complete output from command python setup.py egg_info:
Traceback (most recent call last):
File "<string>", line 1, in <module>
File "c:\temp\pip-install-ycidig8u\win32gui\setup.py", line 27, in <module>
from win32.distutils.gui import win32gui_build_ext
File "c:\temp\pip-install-ycidig8u\win32gui\win32\distutils\gui.py", line 6, in <module>
from .command import win32_build_ext
ModuleNotFoundError: No module named 'win32.distutils.command'
----------------------------------------

Command "python setup.py egg_info" failed with error code 1 in c:\temp\pip-install-ycidig8u\win32gui\
```

I'm using python 3.7 I've upgraded the setuptools but it is still not working...

[python](https://stackoverflow.com/questions/tagged/python)[python-3.x](https://stackoverflow.com/questions/tagged/python-3.x)

[Share](https://stackoverflow.com/q/52806906)

Follow

[edited Oct 14 '18 at 22:53](https://stackoverflow.com/posts/52806906/revisions)

[![img](a.assets/JEycE.png)](https://stackoverflow.com/users/355230/martineau)

[martineau](https://stackoverflow.com/users/355230/martineau)

**108k**2323 gold badges148148 silver badges263263 bronze badges

asked Oct 14 '18 at 20:40

[![img](a.assets/83dc1f452a433c607322dadfe6b7ab77.png)](https://stackoverflow.com/users/10504196/itaymiz)

[ItayMiz](https://stackoverflow.com/users/10504196/itaymiz)

**449**11 gold badge55 silver badges1313 bronze badges

- It may be trying to build the extension and you don't have something required to do that. I usually get a pre-built version from [Christoph Gohlke's UCI web site](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Just search for "PyWin32",  

[Add a comment](https://stackoverflow.com/questions/52806906/cant-install-win32gui/57001086#)



## 4 Answers

[Active](https://stackoverflow.com/questions/52806906/cant-install-win32gui?answertab=active#tab-top)[Oldest](https://stackoverflow.com/questions/52806906/cant-install-win32gui?answertab=oldest#tab-top)[Votes](https://stackoverflow.com/questions/52806906/cant-install-win32gui?answertab=votes#tab-top)





52







Install pywin32. That gives you win32gui.

```
pip install pywin32
```



[Share](https://stackoverflow.com/a/57001086)

Follow

answered Jul 12 '19 at 6:10

[![img](a.assets/18afb92b27771f65d19e50d390815ede.png)](https://stackoverflow.com/users/912602/bronson)

[bronson](https://stackoverflow.com/users/912602/bronson)

**4,509**11 gold badge2929 silver badges1818 bronze badges

[Add a comment](https://stackoverflow.com/questions/52806906/cant-install-win32gui/57001086#)
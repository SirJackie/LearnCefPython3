# [Can DPI scaling be enabled/disabled programmatically on a per-session basis?](https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis)

Source: https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis

[Ask Question](https://stackoverflow.com/questions/ask)

Asked 4 years, 7 months ago

Active [3 years ago](https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis?lastactivity)

Viewed 7k times



11

10

My application happens to be written in Python using pygame, which wraps SDL, but I'm imagining that this is *probably* a more-general question to do with the Windows API.

In some of my Python applications, I want pixel-for-pixel control under Windows 10 even at high resolutions. I want to be able to ensure, for example, that if my Surface Pro 3 has a native resolution of 2160x1440, then I can enter full-screen mode with those dimensions and present a full-screen image of exactly those dimensions.

The barrier to this is "DPI scaling". By default, under Windows' Settings -> Display, the value of "Change the size of text, apps, and other items" is "150% (Recommended)" and the result is that I only see 2/3 of my image. I have discovered how to fix this behaviour...

1. systemwide, by moving that slider down to 100% (but that's [undesirable](https://i.imgur.com/HFO5Rz8.png) for most other applications)
2. just for `python.exe` and `pythonw.exe`, by going to those executables' "Properties" dialogs, Compatibility tab, and clicking "Disable display scaling on high DPI settings". I can do this for me alone, or for all users. I can also automate this process by setting the appropriate keys in the registry programmatically. Or via `.exe.manifest` files (which also seems to require a global setting change, to prefer external manifests, with possible side-effects on other applications).

My question is: can I do this from *inside* my program on a per-launch basis, before I open my graphics window? I, or anyone using my software, won't necessarily want this setting enabled for *all* Python applications ever—we might want it just when running particular Python programs. I'm imagining there might be a `winapi` call (or failing that something inside SDL, wrapped by pygame) that could achieve this, but so far my research is drawing a blank.

[winapi](https://stackoverflow.com/questions/tagged/winapi)[graphics](https://stackoverflow.com/questions/tagged/graphics)[windows-10](https://stackoverflow.com/questions/tagged/windows-10)

[Share](https://stackoverflow.com/q/44398075)

[Improve this question](https://stackoverflow.com/posts/44398075/edit)

Follow

[edited Sep 13 '17 at 20:46](https://stackoverflow.com/posts/44398075/revisions)

asked Jun 6 '17 at 19:14

[![img](a.assets/download.png)](https://stackoverflow.com/users/3019689/jez)

[jez](https://stackoverflow.com/users/3019689/jez)

**13.6k**22 gold badges3232 silver badges5757 bronze badges

- 3

  [SetProcessDpiAwareness](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302122.aspx). 

- If you ever need to support Windows 7, read about adding a "manifest" resource to your EXE, as mentioned in @IInspectable's link  

- 3

  Windows 7 has a separate API call, `SetProcessDPIAware()`. You may need to do this if you are not in complete control of the manifest file (because there can only be one per executable). 

- FYI 150% is not always the default, Windows picks a default based on screen size and EDID data. 

- Take a look [this answer](https://stackoverflow.com/a/44422362/1070480)—it worked for me on Windows 10! 

[Add a comment](https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis#)



## 1 Answer

[Active](https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis?answertab=active#tab-top)[Oldest](https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis?answertab=oldest#tab-top)[Votes](https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis?answertab=votes#tab-top)





19







Here's the answer I was looking for, based on comments by IInspectable and andlabs (many thanks):

```python
  import ctypes

  # Query DPI Awareness (Windows 10 and 8)
  awareness = ctypes.c_int()
  errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
  print(awareness.value)

  # Set DPI Awareness  (Windows 10 and 8)
  errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
  # the argument is the awareness level, which can be 0, 1 or 2:
  # for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)

  # Set DPI Awareness  (Windows 7 and Vista)
  success = ctypes.windll.user32.SetProcessDPIAware()
  # behaviour on later OSes is undefined, although when I run it on my Windows 10 machine, it seems to work with effects identical to SetProcessDpiAwareness(1)
```

The awareness levels [are defined](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280512.aspx) as follows:

```c
typedef enum _PROCESS_DPI_AWARENESS { 
    PROCESS_DPI_UNAWARE = 0,
    /*  DPI unaware. This app does not scale for DPI changes and is
        always assumed to have a scale factor of 100% (96 DPI). It
        will be automatically scaled by the system on any other DPI
        setting. */

    PROCESS_SYSTEM_DPI_AWARE = 1,
    /*  System DPI aware. This app does not scale for DPI changes.
        It will query for the DPI once and use that value for the
        lifetime of the app. If the DPI changes, the app will not
        adjust to the new DPI value. It will be automatically scaled
        up or down by the system when the DPI changes from the system
        value. */

    PROCESS_PER_MONITOR_DPI_AWARE = 2
    /*  Per monitor DPI aware. This app checks for the DPI when it is
        created and adjusts the scale factor whenever the DPI changes.
        These applications are not automatically scaled by the system. */
} PROCESS_DPI_AWARENESS;
```

Level 2 sounds most appropriate for my goal although 1 will also work provided there's no change in system resolution / DPI scaling.

`SetProcessDpiAwareness` will fail with `errorCode = -2147024891 = 0x80070005 = E_ACCESSDENIED` if it has previously been called for the current process (and that includes being called by the system when the process is launched, due to a registry key or `.manifest` file)



[Share](https://stackoverflow.com/a/44422362)

[Improve this answer](https://stackoverflow.com/posts/44422362/edit)

Follow

[edited Jan 11 '19 at 21:22](https://stackoverflow.com/posts/44422362/revisions)

answered Jun 7 '17 at 20:40

[![img](https://www.gravatar.com/avatar/?s=64&d=identicon&r=PG&f=1)](https://stackoverflow.com/users/3019689/jez)

[jez](https://stackoverflow.com/users/3019689/jez)

**13.6k**22 gold badges3232 silver badges5757 bronze badges

- 1

  To make this a good, self-contained answer I would explain why you have choosen the "magic number" used as argument for `SetProcessDpiAwareness()` and propably even define named constants for the possible values in the code sample.  

- @StefanRickli thanks for suggested edit. Does `byref` also work for you? That's what I find in the latest version of the code I based on this answer. 

[Add a comment](https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis#)
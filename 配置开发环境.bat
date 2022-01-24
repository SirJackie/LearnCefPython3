@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
pip install cefpython3 -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple
pip install pywin32 -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple
echo 已完成开发环境配置，按任意键退出程序。
pause > nul
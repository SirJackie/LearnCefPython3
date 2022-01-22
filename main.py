from cefpython3 import cefpython as cef
import sys

# 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
sys.excepthook = cef.ExceptHook

# 创建浏览器
from cefpython3 import cefpython as cef

settings = {
    "debug": True,  # 调试模式
    "log_severity": cef.LOGSEVERITY_INFO, # 日志的输出级别
    "log_file": "debug.log",  # 设置日志文件
    "user_agent": "from stonejianbu 0.0.1",
}
switches = {
    "enable-media-stream": "",  # 取消获取媒体流（如音频、视频数据），必须以空字符串代表否！
    "proxy-server": "socks5://127.0.0.1:8888",  # 设置代理
    "disable-gpu": "",  # 设置渲染方式CPU or GPU
}

cef.Initialize(settings=settings, switches=switches)
cef.CreateBrowserSync(url="./src/index.html")

# 消息循环：监听信号和处理事件
cef.MessageLoop()

# 结束进程
cef.Shutdown()

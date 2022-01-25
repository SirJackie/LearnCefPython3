from BrowserHelper import *
import serial

ser = serial.Serial('COM20', 9600)  # open serial port
print(ser.name)         # check which port was really used


def LightUp(lightState):
    if lightState == 0:
        ser.write(b'0')
    elif lightState == 1:
        ser.write(b'1')


browser = Browser("./HTMLSourceCodes/index.html")

browser.AddHookee(FunctionHookee(None, "LightUp", LightUp))
browser.Run()

ser.write(b'1')     # write a string
ser.close()             # close port

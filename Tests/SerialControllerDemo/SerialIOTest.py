import serial
from time import sleep

ser = serial.Serial('COM20', 9600)  # open serial port
print(ser.name)         # check which port was really used

for i in range(0, 20):
    if i % 2 == 0:
        ser.write(b'1')
    else:
        ser.write(b'0')
    sleep(1)

ser.write(b'1')     # write a string
ser.close()             # close port

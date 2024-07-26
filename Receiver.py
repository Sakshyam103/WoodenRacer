import serial
from datetime import datetime

import os
import threading
import time

import serial

PORT = 'COM256'
port = serial.Serial(PORT, 9600, timeout= 1)
def openport():
# name of port, on linux it maight be smth like ttyUSB0
# timeout important to read empty buffer, prevents freezing
    if not port.is_open:
        port.open()


def recv(raw=0):
    if port.in_waiting:
        if raw:
            return list(port.read(100))
        else:
            return list(port.read(100))



def send(s, raw=0):
    header = b'\x00\x01\x17'  # header first 1st & 2nd bytes address 3rd "chan." (formula 420 + chan#) in our case 0x17 = 23 = 420 + 23 = 433 MHz
    if raw:
        mess = s
    else:
        mess = s
    port.write(header + mess)

# def main():
#     if not port.is_open:
#         port.open()
#     send("Hello to computer 2")
#     while True:
#         time.sleep(5)
#         x = recv()
#         print(x)
#
# if __name__ == "__main__":
#     main()

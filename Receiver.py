import serial
from datetime import datetime




def recv(port,raw=0):
    if port.in_waiting:
        if raw:
            return port.read(100), int(datetime.timestamp(datetime.now()))
        else:
            return port.read(100).decode(), int(datetime.timestamp(datetime.now()))

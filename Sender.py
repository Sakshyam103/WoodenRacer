# import serial
#
# PORT = 'COM10'
# port = serial.Serial(PORT, 9600, timeout=1)
# if not port.is_open:
#     port.open()


def send(s, port, raw=0):
    header = b'\x00\x01\x17'  # header first 1st and 2nd bytes address 3rd "chan." (formula 420 + channel) in out case 0x17 = 23 = 420 + 23 = 433 MHz
    if raw:
        mess = s
    else:
        mess = s  # sending as a byte array
    port.write(header + mess)

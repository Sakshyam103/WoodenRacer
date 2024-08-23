# import queue
# import threading
#
# import serial
import sys
import tkinter as tk
from tkinter import ttk
import random
import threading
import time

import Receiver
from flask import Flask, request, jsonify
from flask_cors import CORS


class CarControlGUI(tk.Tk):
    def __init__(self, rc):
        super().__init__()
        self.rc = rc
        self.title("Car Control Dashboard")
        self.geometry("400x400")

        # Create frames for display and input
        self.display_frame = ttk.LabelFrame(self, text="Current Values", padding="10")
        self.display_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.input_frame = ttk.LabelFrame(self, text="Set Values", padding="10")
        self.input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Initialize variables
        self.velocity = tk.StringVar(value="0")
        self.throttle = tk.StringVar(value="0")
        self.braking_force = tk.StringVar(value="0")
        self.steering_angle = tk.StringVar(value="0")
        self.slip_angle = tk.StringVar(value="0")
        self.auto_function = tk.StringVar(value="OFF")
        self.velocity1 = tk.StringVar(value="0")
        self.throttle1 = tk.StringVar(value="0")
        self.braking_force1 = tk.StringVar(value="0")
        self.steering_angle1 = tk.StringVar(value="0")
        self.slip_angle1 = tk.StringVar(value="0")
        self.auto_function1 = tk.StringVar(value="OFF")

        # Initialize input variables
        self.input_velocity = tk.StringVar(value="0")
        self.input_throttle = tk.StringVar(value="0")
        self.input_braking_force = tk.StringVar(value="0")
        self.input_steering_angle = tk.StringVar(value="0")
        self.input_slip_angle = tk.StringVar(value="0")
        self.input_auto_function = tk.StringVar(value="OFF")

        # Create display labels
        self.create_display_label("Velocity:", self.velocity, 0)
        self.create_display_label("Throttle:", self.throttle, 1)
        self.create_display_label("Braking Force:", self.braking_force, 2)
        self.create_display_label("Steering Angle:", self.steering_angle, 3)
        self.create_display_label("Slip Angle:", self.slip_angle, 4)
        self.create_display_label("Auto Function:", self.auto_function, 5)
        self.create_display_label("Velocity 1:", self.velocity1, 6)
        self.create_display_label("Throttle 1:", self.throttle1, 7)
        self.create_display_label("Braking Angle 1:", self.braking_force1, 8)
        self.create_display_label("Steering Angle 1:", self.steering_angle1, 9)
        self.create_display_label("Slip Angle 1:", self.slip_angle1, 10)
        self.create_display_label("Auto Function1:", self.auto_function1, 11)
        # Create input entries
        self.create_input_entry("Velocity:", self.input_velocity, 0)
        self.create_input_entry("Throttle:", self.input_throttle, 1)
        self.create_input_entry("Braking Force:", self.input_braking_force, 2)
        self.create_input_entry("Steering Angle:", self.input_steering_angle, 3)
        self.create_input_entry("Slip Angle:", self.input_slip_angle, 4)
        self.create_input_entry("Auto Function:", self.input_auto_function, 5)

        # Create update button
        update_button = ttk.Button(self.input_frame, text="Update", command=self.update_values)
        update_button.grid(row=6, column=1, pady=10)
        self.update_display_values()

    def create_display_label(self, text, variable, row):
        label = ttk.Label(self.display_frame, text=text)
        label.grid(row=row, column=0, sticky="e")

        value_label = ttk.Label(self.display_frame, textvariable=variable)
        value_label.grid(row=row, column=1, sticky="w")

    def create_input_entry(self, text, variable, row):
        label = ttk.Label(self.input_frame, text=text)
        label.grid(row=row, column=0, sticky="e")

        entry = ttk.Entry(self.input_frame, textvariable=variable)
        entry.grid(row=row, column=1, sticky="w")

    def update_values(self):
        # This function can be expanded to update the backend or send data to the car
        # print(f"Velocity: {self.velocity.get()}")
        # print(f"Throttle: {self.throttle.get()}")
        # print(f"Braking Force: {self.braking_force.get()}")
        # print(f"Steering Angle: {self.steering_angle.get()}")
        # print(f"Slip Angle: {self.slip_angle.get()}")
        # print(f"Auto Function: {self.auto_function.get()}")
        self.rc.setVelocity(int(self.input_velocity.get()))
        self.rc.setThrottle(int(self.input_throttle.get()))
        self.rc.setBraking(int(self.input_braking_force.get()))
        self.rc.setSteeringAngle(int(self.input_steering_angle.get()))
        self.rc.setSlipAngle(int(self.input_slip_angle.get()))
        self.rc.setAutoFunction(self.input_auto_function.get()[0])

    def update_display_values(self):
        self.velocity.set(str(self.rc.velocity))
        self.throttle.set(str(self.rc.throttle))
        self.braking_force.set(str(self.rc.braking))
        self.steering_angle.set(str(self.rc.steeringAngle))
        self.slip_angle.set(str(self.rc.slipAngle))
        self.auto_function.set(self.rc.autoFunction)
        self.velocity1.set(str(self.rc.velocity1))
        self.throttle1.set(str(self.rc.throttle1))
        self.braking_force1.set(str(self.rc.braking1))
        self.steering_angle1.set(str(self.rc.steeringAngle1))
        self.slip_angle1.set(str(self.rc.slipAngle1))
        self.auto_function1.set(self.rc.autoFunction1)
        self.after(1000, self.update_display_values)


# class SerialHandler:
#     def __init__(self, port, baudrate=9600, timeout = 1):
#         self.port = serial.Serial(port, baudrate, timeout= timeout)
#         self.send_queue = queue.Queue()
#         self.recv_queue = queue.Queue()
#         self.running = True
#         self.thread = threading.Thread(target=self.run)
#         self.thread.start()
#
#     def run(self):
#         while self.running:
#             if self.port.in_waiting:
#                 data = self.port.read(100).decode()
#                 self.recv_queue.put(data)
#
#             if not self.send_queue.empty():
#                 data = self.send_queue.get()
#                 self.port.write(data)
#
#     def recv(self):
#                 if not self.recv_queue.empty():
#                     return self.recv_queue.get()
#                 return None
#
#     def close(self):
#                 self.running = False
#                 self.thread.join()
#                 self.port.close()
#     def send(self, data):
#         self.send_queue.put(data)


# def recv(raw=0):
#     if port.in_waiting:
#         if raw:
#             return port.read(100)
#         else:
#             return port.read(100).decode()
#
#
# def send(s, raw=0):
#     header = b'\x00\x01\x17'  # header first 1st and 2nd bytes address 3rd "chan." (formula 420 + channel) in out case 0x17 = 23 = 420 + 23 = 433 MHz
#     if raw:
#         mess = s
#     else:
#         mess = s  # sending as a byte array
#     port.write(header + mess)


class RC:
    def __init__(self):
        self.id = 100
        self.velocity = 0
        self.throttle = 1
        self.braking = 1
        self.slipAngle = 1
        self.autoFunction = "n"
        self.steeringAngle = 2
        self.velocity1 = 2
        self.throttle1 = 2
        self.braking1 = 2
        self.steeringAngle1 = 2
        self.slipAngle1 = 2
        self.autoFunction1 = "n"

    def setVelocity(self, velocity1):
        self.velocity = velocity1

    def setThrottle(self, throttle1):
        self.throttle = throttle1

    def setBraking(self, braking1):
        self.braking = braking1

    def setSteeringAngle(self, steeringAngle1):
        self.steeringAngle = steeringAngle1

    def setSlipAngle(self, slipAngle1):
        self.slipAngle = slipAngle1

    def setAutoFunction(self, autoFunction1):
        self.autoFunction = autoFunction1

    def updateSensors(self, a, b, c, d, e):
        self.velocity1 = a
        self.throttle1 = b
        self.braking1 = c
        self.steeringAngle1 = d
        self.slipAngle1 = e

    # def start(self):
    #     Receiver.send(bytes([self.id, 101, self.velocity, self.throttle, self.braking, self.steeringAngle,
    #                          self.slipAngle, ord(self.autoFunction), 101, self.id, self.velocity1, self.throttle1,
    #                          self.braking1, self.steeringAngle1, self.slipAngle1, ord(self.autoFunction1)]))
    # self.av.drive(a, b, c, d, e, f, g, h, i, j, k)

    # def stop(self):
    #     Sender.send([self.id, "001", 0, 0, 0, 0, 0, "", '001', self.id, self.velocity1, self.throttle1, self.braking1,
    #                  self.steeringAngle1, self.slipAngle1, self.autoFunction1])

    def sendValues(self):
        return {'velocity': self.velocity, 'throttle': self.throttle, 'braking': self.braking,
                'steeringAngle': self.steeringAngle, 'slipAngle': self.slipAngle, 'autoFunction': self.autoFunction,
                'velocity1': self.velocity1, 'throttle1': self.throttle1, 'braking1': self.braking1,
                'steeringAngle1': self.steeringAngle1, 'slipAngle1': self.slipAngle1,
                'autoFunction1': self.autoFunction1}

    # def receiveValues(self):
    #     _, id2, velocity1, throttle1, braking1, steering1, slip1, auto1, _, _, velocity2, throttle2, braking2, steering2, slip2, auto2 = Receiver.recv()
    #     if id2 == self.id:
    #         self.velocity1 = velocity2
    #         self.throttle1 = throttle2
    #         self.braking1 = braking2
    #         self.steeringAngle1 = steering2
    #         self.slipAngle1 = slip2
    #         self.autoFunction1 = auto2
    # def updateSpeed(self, actualSpeed):
    #     self.actualSpeed = actualSpeed
    #     av.drive(self.actualSpeed, self.steeringAngle)
    #
    # def updateSteeringAngle(self, steeringAngle):
    #     self.steeringAngle = steeringAngle
    #     av.drive(self.actualSpeed, self.steeringAngle)

    # def getvalues(self):
    #     return {'velocity1': self.velocity, 'throttle1': self.throttle, 'braking1': self.braking,
    #             'steering1': self.steeringAngle, 'slip': self.slipAngle, 'autoF1': self.autoFunction}


# av = AV()
# rc = RC(av,10, 20)
# rc.start()
# print(av.actualSpeed, av.steeringAngle, av.distance_sensor)
# rc.stop()


# for now
# velocity = AV.Speed()  # send velocity to motor
# throttle = AV.Throttle()  # send throttle
# brake = AV.Brake()
# steering = AV.Steering()  # send for steering
# slip = AV.Slip()
# velocity_from_sensor = AV.SpeedSensor()
# throttle_from_sensor = AV.ThrottleSensor()
# steering_from_sensor = AV.SteeringSensor()
# slip_from_sensor = AV.SlipSensor()
# distance_sensor = AV.DistanceSensor()
# telemetry = AV.Telemetry(velocity_from_sensor, throttle_from_sensor, steering_from_sensor, slip_from_sensor)
# av = AV.AV(telemetry)
# rc1 = RC(av)  # global variable to store rc instance


rc1 = RC()  # initialize RC class


def receiveThread():
    while True:
        try:
            x = Receiver.recv()
            if x is not None:
                # packet_queue.put(x)
                # if not packet_queue.empty():
                z = list(x)
                z = z[:16]
                print(z)
            else:
                z = [101, 100, 0, 0, 0, 0, 0, 0, 0, 1, rc1.velocity, rc1.throttle, rc1.braking, rc1.steeringAngle,
                     rc1.slipAngle, 1]
            if z[1] == rc1.id:
                # rc1.setVelocity(val)
                rc1.velocity1 = z[2]
                rc1.throttle1 = z[3]
                rc1.braking1 = z[4]
                rc1.steeringAngle1 = z[5]
                rc1.slipAngle1 = z[6]
                rc1.autoFunction1 = chr(z[7])
                print(rc1.velocity1, rc1.throttle1, rc1.braking1, rc1.steeringAngle1, rc1.slipAngle1, rc1.autoFunction1)
                time.sleep(1)
        except KeyboardInterrupt or IndexError:
            print("Interrupted")
            sys.exit(0)
        # rc1.start()
        # time.sleep(1 / 2)
        # val = val + 1
        # if val == 150:
        #     val = val - 1


def sendThread(x):
    while True:
        try:
            # print(
            #     [x.id, 101, x.velocity, x.throttle, x.braking, x.steeringAngle, x.slipAngle, ord(x.autoFunction), 101, x.id,
            #      x.velocity1, x.throttle1, x.braking1, x.steeringAngle1, x.slipAngle1, ord(x.autoFunction1)])
            data = bytearray([x.id, 101, x.velocity, x.throttle, x.braking, x.steeringAngle,
                              x.slipAngle, ord(x.autoFunction), 101, x.id, x.velocity1, x.throttle1,
                              x.braking1, x.steeringAngle1, x.slipAngle1, ord(x.autoFunction1)])
            Receiver.send(data)
            time.sleep(1)
        except KeyboardInterrupt or IndexError:
            print("Keyboard Interrupt or IndexError")
            sys.exit(0)


# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'],
#      origins=['http://localhost:5174'])  # instantiate av since it does not have any parameter
#
#
# @app.route('/data', methods=['GET'])
# def getData():
#     print("received")
#     return jsonify(rc1.sendValues())
#
#
# @app.route('/start', methods=['POST'])
# def start():
#     a = request.get_json()
#     print(a)
#     rc1.setVelocity(a['velocity'])
#     rc1.setThrottle(a['throttle'])
#     rc1.setBraking(a['braking'])
#     rc1.setSteeringAngle(a['steering'])
#     rc1.setSlipAngle(a['slip'])
#     rc1.setAutoFunction(str(a['autoF']))
#     print(rc1.sendValues())
#     return jsonify(rc1.sendValues())
# av.velocity = rc1.velocity
# av.throttle = rc1.throttle
# av.brake = rc1.braking
# av.steering = rc1.steeringAngle
# av.slip = rc1.slipAngle
# av.auto = rc1.autoFunction
# rc1.start()
# print(r)
# print(r["velocity"])
# rc1.updateSensors(r['velocity1'], r['throttle1'], r['braking1'], r['steeringAngle1'], r['slipAngle1'])
# print(rc1.sendValues())
# av.get_data_from_Telemetry()
# av.sendData()
# return jsonify(rc1.sendValues())


# @app.route('/stop', methods=['GET'])
# def stop1():
#     rc1.stop()


# @app.route('/speed', methods=['POST', 'PUT'])
# def speed1():
#     a = request.get_json()
#     rc.updateSpeed(a)


# @app.route('/steering', methods=['POST'])
# def steering1():
#     b = request.get_json()
#     rc.updateSteeringAngle(b)


if __name__ == '__main__':
    Receiver.openport()
    receiveThread = threading.Thread(target=receiveThread, daemon=True)
    sendThread = threading.Thread(target=sendThread, args=(rc1,), daemon=True)
    receiveThread.start()
    sendThread.start()
    # app.run(debug=True, port=5175)
    app = CarControlGUI(rc1)
    app.mainloop()
    receiveThread.join()
    sendThread.join()
    Receiver.port.flushInput()
    Receiver.port.flushOutput()
    Receiver.port.close()

# import os
# import threading
# import time
#
# import serial
#
# PORT = 'COM256'  # name of port, on linux it maight be smth like ttyUSB0
#
# port = serial.Serial(PORT, 9600, timeout=1)  # timeout important to read empty buffer, prevents freezing
#
#
# def recv(raw=0):
#     if port.in_waiting:
#         if raw:
#             return list(port.read(100))
#         else:
#             return list(port.read(100).decode())
#
#
# def send(s, raw=0):
#     header = b'\x00\x01\x17'  # header first 1st & 2nd bytes address 3rd "chan." (formula 420 + chan#) in our case 0x17 = 23 = 420 + 23 = 433 MHz
#     if raw:
#         mess = s
#     else:
#         mess = s.encode()
#     port.write(header + mess)
#
#
# def main():
#     if not port.is_open:
#         port.open()
#     send("Hello to computer 2")
#     while True:
#         time.sleep(5)
#         x = recv()
#         print(x)


# print("Waiting")


# if __name__ == "__main__":
#     main()
#     port.close()

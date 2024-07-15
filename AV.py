import math
import time

import numpy as np

import serial
import Receiver
import Sender
import serial.tools.list_ports
from threading import Timer



PORT = 'COM10'

port = serial.Serial(PORT, 9600, timeout=1)
if not port.is_open:
    port.open()


# class Watchdog(Exception):
#     def __init__(self, timeout, userHandler=None):
#         self.timeout = timeout
#         self.handler = userHandler if userHandler is not None else self.defaultHandler
#         self.timer = Timer(self.timeout, self.handler)
#         self.timer.start()
#
#     def reset(self):
#         self.timer.cancel()
#         self.timer = Timer(self.timeout, self.handler)
#         self.timer.start()
#
#     def stop(self):
#         self.timer.cancel()
#
#     def defaultHandler(self):
#         raise self

def list_serial_ports():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        print(f"Device: {port.device}")
        print(f"Manufacturer: {port.manufacturer}")
        print(f"Description: {port.description}")
        print(f"Hardware ID: {port.hwid}")
        print(f" VID: {port.vid}")
        print(f"PID: {port.pid}")
        print(f"Serial Number: {port.serial_number}")
        print()

class Telemetry:  # receives datas from sensor
    def __init__(self, speed, throttle3, steering3, slip3):
        self.velocity = speed.getVelocity()  # get velocity from speed sensor
        self.throttle = throttle3.getThrottle()  # get throttle data from throttle sensor
        # self.braking = braking.getBraking()
        self.steering = steering3.getSteeringAngle()  # get steering angle data from steering sensor
        self.slip = slip3.getSlipAngle()  # get slip angle data from slip sensor
        self.autoFunction = 'n'  # for now just put n for normal
        self.distance = DistanceSensor().getDistance()  # get distance from distance sensor

    def sendData(self):  # send data to AV as an array
        return [self.velocity, self.throttle, self.steering, self.slip, self.autoFunction, self.distance]


class Brake:

    def __init__(self):  # initially set braking to 0
        self.braking = 0

    def actuateBrake(self, brakingForce):  # apply brake
        self.braking = brakingForce
        print("Brake Applied: ", self.braking)


class Slip:
    def __init__(self):  # initially set slip angle to 0
        self.slip = 0

    def updateSlip(self, slip):  # update slip angle
        self.slip = slip
        print('Slip Applied: ', self.slip)


class Steering:
    def __init__(self):  # initially set steering angle to 0
        self.steeringAngle = 0

    def updateSteeringAngle(self, angle):  # update the steering angle
        self.steeringAngle = angle
        print("Steering Applied: ", self.steeringAngle)


class Speed:  # sending speed to motor
    def __init__(self):  # initially set speed to 0
        self.speed = 0

    def updateSpeed(self, speed):  # update speed
        self.speed = speed
        print("Speed Applied: ", self.speed)


class Throttle:

    def __init__(self):  # initially set throttle to 0
        self.throttle = 0

    def updateThrottle(self, throttle):  # update throttle
        self.throttle = throttle
        print("Throttle Applied: ", self.throttle)


class ThrottleSensor:
    def __init__(self):  # initially set throttle to 0
        self.throttle = 0

    def getThrottle(self):  # get throttle from sensor
        self.throttle = 32  # need to fit sensor and get data
        print("Throttle Sensor data: ", self.throttle)
        return self.throttle  # return throttle


class SteeringSensor:

    def __init__(self):  # initially set steering angle to 0
        self.steering = 0

    def getSteeringAngle(self):  # give steering angle from sensor
        self.steering = 5  # need to fit steering position sensor and get data
        print("Steering position: ", self.steering)
        return self.steering  # return steering


class SpeedSensor:  # just gives speed from the sensor
    def __init__(self):  # initially set speed to 0
        self.velocity = 0

    def getVelocity(self):  # get speed from the sensor
        self.velocity = 10  # need to fit speed sensor and get data
        print("speed sensor data: ", self.velocity)
        return self.velocity  # return velocity


class SlipSensor:  # need to know if we have slip sensor or do we need to calculate for now just return 7
    def getSlipAngle(self):
        print("Slip angle sensor data: ", 7)
        return 7


class BrakeSensor:

    def getBrakePosition(self):
        print("Brake position sensor data: ", 5)
        return 5


class DistanceSensor:  # just gives distance from the sensor
    def __init__(self):  # initially set distance to infinity
        self.distance = math.inf

    def getDistance(self):  # get distance from the distance sensor
        self.distance = 5  # need to fit distance measuring sensor and get data
        print("Distance sensor data: ", self.distance)
        return self.distance  # return 10 cm for now


class AV:  # class for AV
    def __init__(self, telemetry1):
        self.telemetry = telemetry1  # need telemetry class to get the sensor's data
        self.timestamp = 0
        self.id = 1  # set id
        self.velocity = 0  # set velocity to 0
        self.throttle = 0  # set throttle to 0
        self.braking = 0  # set braking to 0
        self.steeringAngle = 0  # set steering angle to 0
        self.slipAngle = 0  # set slip angle to 0
        self.autoFunction = 'n'  # set autofunction to normal 'n'

    def drive(self, velocity4, throttle4, brake4, steering4, slip4):  # takes classes
        # self.velocity = a
        # self.throttle = b
        # self.braking = c
        # self.steeringAngle = d
        # self.slipAngle = e
        # self.autoFunction = f
        velocity4.updateSpeed(self.velocity)  # update speed
        throttle4.updateThrottle(self.throttle)  # update throttle
        brake4.actuateBrake(self.braking)  # update brake
        steering4.updateSteeringAngle(self.steeringAngle)  # update steering angle
        slip4.updateSlip(self.slipAngle)  # update slip angle
        print("Values update")

    def stop(self):
        print("Stopping")

    # def brake(self, actualSpeed):
    #     brakingForce = self.calculateBrakingForce(actualSpeed)
    #     self.brakingForce.actuateBrake(brakingForce)

    def get_data_from_Telemetry(self):  # get data from telemetry class
        a = self.telemetry.sendData()
        if a[len(a) - 1] < 5:  # check if the distance of the obstacle is less than 5
            self.braking = self.velocity  # need to stop
            print("Brake applied")
        return a

    # def calculateBrakingForce(self, actualSpeed):
    #     return actualSpeed
    #
    # def calculateThrottle(self, actualSpeed):
    #     return actualSpeed
    #
    def sendData(self):
        Sender.send(
            bytearray([self.id, 0, self.telemetry.velocity, self.telemetry.throttle, 0,
                       self.telemetry.steering, self.telemetry.slip, ord(self.telemetry.autoFunction),
                       0, self.id, self.velocity, self.throttle, self.braking,
                       self.steeringAngle, self.slipAngle, ord(self.autoFunction)]), port)
        # return {'velocity': self.velocity, 'throttle': self.throttle, 'braking': self.braking,
        #         'steeringAngle': self.steeringAngle, 'slipAngle': self.slipAngle,
        #         'velocity1': self.telemetry.velocity, 'throttle1': self.telemetry.throttle, 'braking1': 0,
        #         'steeringAngle1': self.telemetry.steering, 'slipAngle1': self.telemetry.slip}


# def myHandler():
#     print("Applying brake")


velocity = Speed()  # send velocity to motor
throttle = Throttle()  # send throttle
brake = Brake()
steering = Steering()  # send for steering
slip = Slip()
velocity_from_sensor = SpeedSensor()
throttle_from_sensor = ThrottleSensor()
steering_from_sensor = SteeringSensor()
slip_from_sensor = SlipSensor()
telemetry = Telemetry(velocity_from_sensor, throttle_from_sensor, steering_from_sensor, slip_from_sensor)
av = AV(telemetry)
list_serial_ports()
# watchdog = Watchdog(60, myHandler)
# def receiveData():
while True:
    try:
        x = Receiver.recv(port)
        if x is not None:
            (_, id2, velocity1, throttle1, braking1, steering1, slip1, auto1, _, _, velocity2, throttle2, braking2,
             steering2, slip2, auto2), datetime1 = np.array(x), x[1]
            if (datetime1 - av.timestamp) >= 1:
                av.stop()
            else:
                av.timestamp = datetime1
        else:
            (_, id2, velocity1, throttle1, braking1, steering1, slip1, auto1, _, _, velocity2, throttle2, braking2,
             steering2, slip2, auto2) = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        if id2 == av.id:
            av.velocity = velocity1
            av.throttle = throttle1
            av.brake = braking1
            av.steering = steering1
            av.slip = slip1
            av.auto = auto1
            av.drive(velocity, throttle, brake, steering, slip)
            print(av.get_data_from_Telemetry())
            av.sendData()
            time.sleep(1/2)
        # except watchdog:
        #     watchdog.stop()
        #     break

# receiveData()

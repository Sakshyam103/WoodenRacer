import numpy as np
import serial

import AV
import Receiver
import Sender
from flask import Flask, request, jsonify
from flask_cors import CORS


PORT = 'COM10'

port = serial.Serial(PORT, 9600, timeout=1)
if not port.is_open:
    port.open()


class RC:
    def __init__(self):
        self.id = 100
        self.velocity = 1
        self.throttle = 1
        self.braking = 1
        self.slipAngle = 1
        self.autoFunction = int("n")
        self.steeringAngle = 2
        self.velocity1 = 2
        self.throttle1 = 2
        self.braking1 = 2
        self.steeringAngle1 = 2
        self.slipAngle1 = 2
        self.autoFunction1 = int("n")

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

    def start(self):
        Sender.send(bytes([self.id, 101, self.velocity, self.throttle, self.braking, self.steeringAngle,
                           self.slipAngle, self.autoFunction, 101, self.id, self.velocity1, self.throttle1,
                           self.braking1, self.steeringAngle1, self.slipAngle1, self.autoFunction1]))
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

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST', 'PUT', 'DELETE'],
     origins=['http://localhost:5174'])  # instantiate av since it does not have any parameter

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
x = Receiver.recv(port)
if x is not None:
    _, id2, velocity1, throttle1, braking1, steering1, slip1, auto1, _, _, velocity2, throttle2, braking2, steering2, slip2, auto2 = np.array(x)
else:
    _, id2, velocity1, throttle1, braking1, steering1, slip1, auto1, _, _, velocity2, throttle2, braking2, steering2, slip2, auto2 = [1,0,0,0,0,0,0,0,0,1,rc1.velocity, rc1.throttle, rc1.braking, rc1.steeringAngle, rc1.slipAngle, 1]
if id2 == rc1.id:
    rc1.velocity1 = velocity1
    rc1.throttle1 = throttle1
    rc1.braking1 = braking1
    rc1.steeringAngle1 = steering1
    rc1.slipAngle1 = slip1
    rc1.autoFunction1 = auto1


@app.route('/data', methods=['GET'])
def getData():
    return jsonify(rc1.sendValues())


@app.route('/start', methods=['POST'])
def start():
    a = request.get_json()
    print(a)
    rc1.setVelocity(a['velocity'])
    rc1.setThrottle(a['throttle'])
    rc1.setBraking(a['braking'])
    rc1.setSteeringAngle(a['steering'])
    rc1.setSlipAngle(a['slip'])
    rc1.setAutoFunction(str(a['autoF']))
    print(rc1.sendValues())
    # av.velocity = rc1.velocity
    # av.throttle = rc1.throttle
    # av.brake = rc1.braking
    # av.steering = rc1.steeringAngle
    # av.slip = rc1.slipAngle
    # av.auto = rc1.autoFunction
    rc1.start()
    # print(r)
    # print(r["velocity"])
    # rc1.updateSensors(r['velocity1'], r['throttle1'], r['braking1'], r['steeringAngle1'], r['slipAngle1'])
    # print(rc1.sendValues())
    # av.get_data_from_Telemetry()
    # av.sendData()
    return jsonify(rc1.sendValues())


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
    app.run(debug=True, port=5175)

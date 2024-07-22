# import signal
# import time
# from threading import Timer
# from datetime import datetime
# import sys
#
#
# class Watchdog(Exception):
#     def __init__(self, timeout, userHandler=None):
#         self.timeout = timeout
#         self.handler = userHandler if userHandler is not None else self.defaultHandler
#         self.timer = Timer(self.timeout, self.handler)
#         self.timer.start()
#         # self.shutdown = False
#         # signal.signal(signal.SIGINT, self.shutdown_handler)
#         # signal.signal(signal.SIGTERM, self.shutdown_handler)
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
#
#     # def shutdown_handler(self, signum, frame):
#     #     self.shutdown = True
#     #     self.timer.cancel()
#     #     sys.exit(0)
#
#
# # watchdog = Watchdog(5)
# # try:
# #     print("stopped")
# # except Watchdog:
# #     watchdog.stop()
#
# def myHandler():
#     print("Watchdog expired!")
#
#
# watchdog = Watchdog(5, myHandler)
#
#
# def doSomethingRegularly():
#     while True:
#         try:
#             time.sleep(1/2)
#             print("Data received ", int(datetime.timestamp(datetime.now())))
#             watchdog.reset()
#         except Watchdog:
#             watchdog.stop()
#             break
#
#
#
# doSomethingRegularly()
import datetime


# def valuex():
#     return [1, 2, 3, 4], 23
#
#
# a, b = valuex()
# print(a)
# print(b)

# coding= utf-8

'''
    在类中使用property属性
'''

class Flight(object):

    def __init__(self,name):
        self.__flight_name = name

    def check_status(self):
        print("checking status ....")
        return 1

    @property
    def flight_status(self):
        status = self.check_status()

        if status == 0:
            print("Flight is canceled")
        elif status == 1:
            print("Flight is departed")
        else:
            print("Can't find anything about this flight")

    @flight_status.setter
    def flight_status(self,stauts):
        print("setting status ", stauts)


flight = Flight("CA998")
flight.flight_status
flight.flight_status = 2

'''
TCP 客户端
'''

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",9999))
print(s.recv(1024).decode("utf-8"))

for data in [b"Michael",b"Tracy",b"Sarah"]:
    s.send(data)
    print(s.recv(1024).decode("utf-8"))

s.send(b"exit")
s.close()
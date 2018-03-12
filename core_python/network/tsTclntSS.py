#!/usr/bin/env python

#这是一个时间戳TCP客户端，它知道如何与类似文件的SocketServer类StreamRequestHandler对象通信

from socket import *

HOST = 'localhost'
PORT = 21567
BUFF = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' %data)
    data = tcpCliSock.recv(BUFF)
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()
#!/usr/bin/env python

#这个脚本创建一个UPD客户端，它提示用户输入发送给服务器的消息，并接收服务器加入时间戳前缀的消息，然后显示给用户

from socket import *

HOST = 'localhost'
PORT = 21567
BUFF = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFF)
    if not data:
        break
    print(data)

udpCliSock.close()
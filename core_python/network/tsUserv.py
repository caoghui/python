#!/usr/bin/env python

#这个脚本创建一个UPD服务器，它接受客户端发来的消息，并将加了时间戳前缀的消息返回给客户端

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFF = 1024
ADDR = (HOST, PORT)

udpServSock = socket(AF_INET, SOCK_DGRAM)
udpServSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpServSock.recvfrom(BUFF)
    if data == 'bye':
        break
    udpServSock.sendto(b'[%s] %s' %(bytes(ctime(), 'utf-8'), data), addr)
    print('...received from and returned to:', addr)

udpServSock.close()

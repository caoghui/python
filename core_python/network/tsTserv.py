#!/usr/bin/env python

#这个脚本创建一个TCP服务器，它接受来自客户端的消息，然后将消息加上时间戳前缀并发送回客户端

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

while True:
    print('waiting for connection....')
    tcpCliSock, addr = tcpServSock.accept()
    print('connected from : ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        print(data)
        if not data:
            break
        tcpCliSock.send(b'[%s] %s' %(bytes(ctime(), 'utf-8'), data))
    tcpCliSock.close()
tcpServSock.close()
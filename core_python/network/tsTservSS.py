#!/usr/bin/env python

#通过使用SocketServer类，TCPServer和StreamRequestHandler，该脚本创建了一个时间戳TCP服务器

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write('[%s] %s' %(ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()


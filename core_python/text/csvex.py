#!/usr/bin/env python

#这个简单的脚本演示了将数据转成CSV格式写出，并再次读取

import csv
from distutils.log import warn as printf

DATA = (
    (9, 'Web Clients and Servers', 'base64, urllib'),
    (10, 'Web Programming: CGI & WSGI', 'cgi, time, wsgiref'),
    (13, 'Web Services', 'urllib, twython')
)

printf('***Writing CSV DATA')

f = open('bookdata.csv', 'w')
writer = csv.writer(f)
for record in DATA:
    writer.writerow(record)
f.close()

printf('***Review of Saved DATA')
f = open('bookdata.csv', 'r')
reader = csv.reader(f)
for chap, title, modpkgs in reader:
    printf('Chapter %s: %r (featuring %s)' % (chap, title, modpkgs))
f.close()

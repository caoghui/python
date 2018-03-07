#!/usr/bin/env python

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach', HOST)
        return
    print('***Conntected to host ', HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('***Logged in as anonymous')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot cd to ', DIRN)
        f.quit()
        return 
    print('***Changed to ', DIRN)

    try:
        f.retrbinary('RETR %s' %FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('ERROR: cannot read file ', FILE)
        os.unlink(FILE)
    else:
       print('***Downloaded ', FILE)
    f.quit()


if __name__ == '__main__':
    main()    

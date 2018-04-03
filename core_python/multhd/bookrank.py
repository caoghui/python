#!/usr/bin/env python

#该脚本通过单线程进行下载图书排名信息的调用
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib import urlopen as uopen 

REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://amazon.con/dp/'
ISBNs = {
    '0132269937' : 'Core Python Programming',
    '0132356139' : 'Python Web Development with Django',
    '0137143419' : 'Python Fundamentals',
}

def getRanking(isbn):
    page = uopen('%s%s' %(AMZN, isbn))  # or stri.format()
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print('- %r ranked %s' %(ISBNs[isbn], getRanking(isbn)))

def _main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        #_showRanking(isbn)
        Thread(target = _showRanking, args = (isbn,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()
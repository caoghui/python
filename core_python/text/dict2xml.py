#!/usr/bin/env python

#该脚本将python字典转成xml，并使用多种格式显示

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

BOOKs = {
    '0132269937':{
        'title': 'Core Python Programming',
        'edition': 2,
        'year': 2007,
    },
    '0132356139':{
        'title': 'Python Web Development with Django',
        'authors': ['Jeff Forcier', 'Paul Bissex', 'Wesley Chun'],
        'year': 2009,
    },
    '0137146419':{
        'title': 'Python Fundamentals',
        'year': 2009,
    },
}

books = Element('books')
for isbn, info in BOOKs.iteritems():
    book = SubElement(books, 'book')
    info.setdefault('authors', 'Wesley Chun')
    info.setdefault('edition', 1)
    for key, val in info.iteritems():
        SubElement(book, key).text = ', '.join(str(val).split(':'))

xml = tostring(books)
print('***Raw XML***')
print(xml)
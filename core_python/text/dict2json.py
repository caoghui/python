#!/usr/bin/env python

#该脚本将python字典转成json，并使用多种格式显示

from distutils.log import warn as printf
from json import dumps
from pprint import pprint

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

printf('***Raw Dict***')
printf(BOOKs)

printf('****Pretty_printed dict****')
pprint(BOOKs)

printf('***Raw JSON***')
printf(dumps(BOOKs))

printf('***Pretty_printed JSON')
pprint(dumps(BOOKs, indent = 4))
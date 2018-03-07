#!/usr/bin/env python

from functools import partial as pto 
from tkinter   import Tk, Button, X
#from tkMessageBox import showinfo, showwarning, showerror
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}

#回调函数
critCB = lambda : showerror('Error', 'Error Button Pressed!')
warnCB = lambda : showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda : showinfo('Info', 'Info Button Pressed!')

#主窗口
top = Tk()
top.title('Road Signs')
top.geometry('250x230')

#退出按钮
Button(top, text = 'QUIT', command = top.quit, bg = 'red', fg = 'white').pack()

#偏函数
MyButton = pto(Button, top)
CritButton = pto(MyButton, command = critCB, bg = 'white', fg = 'red')
WarnButton = pto(MyButton, command = warnCB, bg = 'goldenrod1')
ReguButton = pto(MyButton, command = infoCB, bg = 'white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text = %r%s).pack(fill=X, expand = True)' %(signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
    eval(cmd)

top.mainloop()

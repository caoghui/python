#!/usr/bin/env python

import tkinter as tk

root = tk.Tk()
root.geometry('250x150')

def resize(ev = None):
    lbl_hello.config(font = 'Helvetica -%d bold' %scale.get())



lbl_hello = tk.Label(root, text = 'Hello World', font = 'Helvetica -12 bold')
lbl_hello.pack(fill = tk.Y, expand = 1)

scale = tk.Scale(root, from_ = 10, to = 40, orient = tk.HORIZONTAL, command = resize)
scale.set(12)
scale.pack(fill = tk.X, expand = 1)

btn_quit = tk.Button(root, text = 'QUIT', command = root.quit, activebackground = 'red', activeforeground = 'white')
btn_quit.pack()

root.mainloop()
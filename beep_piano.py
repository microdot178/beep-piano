from tkinter import *
import tkinter as tk
import os

root = tk.Tk()
root.title('beep piano c:')
root.geometry('602x164')
root.resizable(False, False)

b1 = Button (text='C', width=3, height=15)
def play():
    os.system("beep -f 1500")
    print(root.geometry())
b1.config(command=play)
b1.pack()
b1.place(x=1, y=2)

b2 = Button (text='C#', width=3, height=15)
def play2 ():
    os.system('beep -f 1000')

b2.config(command=play2)
b2.pack()
b2.place(x=50, y=1)

b3 = Button (text='D', width=3, height=15)
def play3 ():
    os.system('beep -f 1000')

b3.config(command=play3)
b3.pack()
b3.place(x=100, y=1)
b4 = Button (text='D#', width=3, height=15)
def play4 ():
    os.system('beep -f 1000')

b4.config(command=play4)
b4.pack()
b4.place(x=150, y=1)

b5 = Button (text='E', width=3, height=15)
def play5 ():
    os.system('beep -f 1000')

b5.config(command=play5)
b5.pack()
b5.place(x=200, y=1)

b6 = Button (text='F', width=3, height=15)
def play6 ():
    os.system('beep -f 1000')

b6.config(command=play6)
b6.pack()
b6.place(x=250, y=1)

b7 = Button (text='F#', width=3, height=15)
def play7 ():
    os.system('beep -f 1000')

b7.config(command=play7)
b7.pack()
b7.place(x=300, y=1)

b8 = Button (text='G', width=3, height=15)
def play8 ():
    os.system('beep -f 1000')

b8.config(command=play8)
b8.pack()
b8.place(x=350, y=1)

b10 = Button (text='G#', width=3, height=15)
def play10 ():
    os.system('beep -f 1000')

b10.config(command=play10)
b10.pack()
b10.place(x=400, y=1)

b11 = Button (text='A', width=3, height=15)
def play11 ():
    os.system('beep -f 1000')

b11.config(command=play11)
b11.pack()
b11.place(x=450, y=1)

b12 = Button (text='A#', width=3, height=15)
def play12 ():
    os.system('beep -f 1000')

b12.config(command=play12)
b12.pack()
b12.place(x=500, y=1)

b13 = Button (text='B', width=3, height=15)
def play13 ():
    os.system('beep -f 1000')

b13.config(command=play13)
b13.pack()
b13.place(x=550, y=1)

root.mainloop()

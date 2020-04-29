from tkinter import *
import tkinter as tk
import os

root = tk.Tk()
root.title('beep piano c:')
root.geometry('602x164')
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file='favicon.png'))

# это все снизу клавиши 

b1 = Button (text='C', width=3, height=15)
def play():
    os.system("beep -f 261.6")
b1.config(command=play)
b1.pack()
b1.place(x=1, y=2)

b2 = Button (text='C#', width=3, height=15, background="#555",)
def play2 ():
    os.system('beep -f 277.2')

b2.config(command=play2)
b2.pack()
b2.place(x=50, y=1)

b3 = Button (text='D', width=3, height=15)
def play3 ():
    os.system('beep -f 293.7')

b3.config(command=play3)
b3.pack()
b3.place(x=100, y=1)
b4 = Button (text='D#', width=3, height=15, background="#555",)
def play4 ():
    os.system('beep -f 311.1')

b4.config(command=play4)
b4.pack()
b4.place(x=150, y=1)

b5 = Button (text='E', width=3, height=15)
def play5 ():
    os.system('beep -f 329.6')

b5.config(command=play5)
b5.pack()
b5.place(x=200, y=1)

b6 = Button (text='F', width=3, height=15)
def play6 ():
    os.system('beep -f 349.2')

b6.config(command=play6)
b6.pack()
b6.place(x=250, y=1)

b7 = Button (text='F#', width=3, height=15, background="#555",)
def play7 ():
    os.system('beep -f 370.0')

b7.config(command=play7)
b7.pack()
b7.place(x=300, y=1)

b8 = Button (text='G', width=3, height=15)
def play8 ():
    os.system('beep -f 392.0')

b8.config(command=play8)
b8.pack()
b8.place(x=350, y=1)

b9 = Button (text='G#', width=3, height=15, background="#555",)
def play9 ():
    os.system('beep -f 415.3')

b9.config(command=play9)
b9.pack()
b9.place(x=400, y=1)

b10 = Button (text='A', width=3, height=15)
def play10 ():
    os.system('beep -f 440.0')

b10.config(command=play10)
b10.pack()
b10.place(x=450, y=1)

b11 = Button (text='A#', width=3, height=15, background="#555",)
def play11 ():
    os.system('beep -f 466.2')

b11.config(command=play11)
b11.pack()
b11.place(x=500, y=1)

b12 = Button (text='B', width=3, height=15)
def play12 ():
    os.system('beep -f 493.9')

b12.config(command=play12)
b12.pack()
b12.place(x=550, y=1)

###########################################

# бинды для кнопок q,w,e,r,t,y,u,i,o,p,[,].

def bind1(event):
    root(10, bind_q, event.widget)

def bind_q(widget):
    play()

##################################

def bind2(event):
    root(10, bind_w, event.widget)

def bind_w(widget):
    play2()

##################################

def bind3(event):
    root(10, bind_e, event.widget)

def bind_e(widget):
    play3()

##################################

def bind4(event):
    root(10, bind_r, event.widget)

def bind_r(widget):
    play4()

##################################

def bind5(event):
    root(10, bind_t, event.widget)

def bind_t(widget):
    play5()

##################################

def bind6(event):
    root(10, bind_y, event.widget)

def bind_y(widget):
    play6()

##################################

def bind7(event):
    root(10, bind_u, event.widget)

def bind_u(widget):
    play7()

##################################

def bind8(event):
    root(10, bind_i, event.widget)

def bind_i(widget):
    play8()

##################################

def bind10(event):
    root(10, bind_o, event.widget)

def bind_o(widget):
    play9()

##################################

def bind11(event):
    root(10, bind_p, event.widget)

def bind_p(widget):
    play10()

##################################

def bind12(event):
    root(10, bind_12, event.widget)

def bind_12(widget):
    play11()

##################################

def bind13(event):
    root(10, bind_13, event.widget)

def bind_13(widget):
    play12()

##################################

root.bind('<q>', bind_q)
root.bind('<w>', bind_w)
root.bind('<e>', bind_e)
root.bind('<r>', bind_r)
root.bind('<t>', bind_t)
root.bind('<y>', bind_y)
root.bind('<u>', bind_u)
root.bind('<i>', bind_i)
root.bind('<o>', bind_o)
root.bind('<p>', bind_p)
root.bind('<Key-0x005b>', bind_12)
root.bind('<Key-0x005d>', bind_13)
root.mainloop()

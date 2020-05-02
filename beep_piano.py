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

def bind9(event):
    root(10, bind_o, event.widget)

def bind_o(widget):
    play9()

##################################

def bind10(event):
    root(10, bind_p, event.widget)

def bind_p(widget):
    play10()

##################################

def bind11(event):
    root(10, bind_12, event.widget)

def bind_11(widget):
    play11()

##################################

def bind12(event):
    root(10, bind_12, event.widget)

def bind_12(widget):
    play12()



#решил добавить еще однв октаву, верхнюю на копки 1,2,3,4,5,6,7,8,9,-,=

def play13():
    os.system("beep -f 523.2")

def bind13(event):
    root(10, bind_13, event.widget)

def bind_13(widget):
    play13()
##################################

def play14():
    os.system("beep -f 554.3")

def bind14(event):
    root(10, bind_14, event.widget)

def bind_14(widget):
    play14()
##################################

def play15():
    os.system("beep -f 587.3")

def bind15(event):
    root(10, bind_15, event.widget)

def bind_15(widget):
    play15()
##################################

def play16():
    os.system("beep -f 622.2")

def bind16(event):
    root(10, bind_16, event.widget)

def bind_16(widget):
    play16()
##################################

def play17():
    os.system("beep -f 659.2")

def bind17(event):
    root(10, bind_17, event.widget)

def bind_17(widget):
    play17()
##################################

def play18():
    os.system("beep -f 698.4")

def bind18(event):
    root(10, bind_18, event.widget)

def bind_18(widget):
    play18()
##################################

def play19():
    os.system("beep -f 739.9")

def bind19(event):
    root(10, bind_19, event.widget)

def bind_19(widget):
    play19()
##################################

def play20():
    os.system("beep -f 784")

def bind20(event):
    root(10, bind_20, event.widget)

def bind_20(widget):
    play20()
##################################

def play21():
    os.system("beep -f 830.6")

def bind21(event):
    root(10, bind_21, event.widget)

def bind_21(widget):
    play21()
##################################

def play22():
    os.system("beep -f 880")

def bind22(event):
    root(10, bind_22, event.widget)

def bind_22(widget):
    play22()
##################################

def play23():
    os.system("beep -f 932.3")

def bind23(event):
    root(10, bind_23, event.widget)

def bind_23(widget):
    play23()
##################################

def play24():
    os.system("beep -f 987.7")

def bind24(event):
    root(10, bind_24, event.widget)

def bind_24(widget):
    play24()
##################################




#нижняя октава

def play25():
    os.system("beep -f 130.8")

def bind25(event):
    root(10, bind_25, event.widget)

def bind_25(widget):
    play25()
##################################

def play26():
    os.system("beep -f 138.5")

def bind26(event):
    root(10, bind_26, event.widget)

def bind_26(widget):
    play26()
##################################

def play27():
    os.system("beep -f 146.8")

def bind27(event):
    root(10, bind_27, event.widget)

def bind_27(widget):
    play27()
##################################

def play28():
    os.system("beep -f 155.5")

def bind28(event):
    root(10, bind_28, event.widget)

def bind_28(widget):
    play28()
##################################

def play29():
    os.system("beep -f 164.8")

def bind29(event):
    root(10, bind_29, event.widget)

def bind_29(widget):
    play29()
##################################

def play30():
    os.system("beep -f 174.6")

def bind30(event):
    root(10, bind_30, event.widget)

def bind_30(widget):
    play30()
##################################

def play31():
    os.system("beep -f 185")

def bind31(event):
    root(10, bind_31, event.widget)

def bind_31(widget):
    play31()
##################################

def play32():
    os.system("beep -f 196")

def bind32(event):
    root(10, bind_32, event.widget)

def bind_32(widget):
    play32()
##################################

def play33():
    os.system("beep -f 207.6")

def bind33(event):
    root(10, bind_33, event.widget)

def bind_33(widget):
    play33()
##################################

def play34():
    os.system("beep -f 220")

def bind34(event):
    root(10, bind_34, event.widget)

def bind_34(widget):
    play34()
##################################

def play35():
    os.system("beep -f 233")

def bind35(event):
    root(10, bind_35, event.widget)

def bind_35(widget):
    play35()
##################################

def play36():
    os.system("beep -f 246.9")

def bind36(event):
    root(10, bind_36, event.widget)

def bind_36(widget):
    play36()
##################################

#ну это короче средняя октава
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
root.bind('<Key-0x005b>', bind_11)
root.bind('<Key-0x005d>', bind_12)

#ну а это конечно верхняя
root.bind('1', bind_13)
root.bind('2', bind_14)
root.bind('3', bind_15)
root.bind('4', bind_16)
root.bind('5', bind_17)
root.bind('6', bind_18)
root.bind('7', bind_19)
root.bind('8', bind_20)
root.bind('9', bind_21)
root.bind('0', bind_22)
root.bind('-', bind_23)
root.bind('=', bind_24)

#ну и нижняя
root.bind('a', bind_25)
root.bind('s', bind_26)
root.bind('d', bind_27)
root.bind('f', bind_28)
root.bind('g', bind_29)
root.bind('h', bind_30)
root.bind('j', bind_31)
root.bind('k', bind_32)
root.bind('l', bind_33)
root.bind('<Key- 0x003b>', bind_34)
root.bind("'", bind_35)
root.bind('<Key- 0xff0d>', bind_36)
root.mainloop()
from tkinter import *
from tkinter import font
base = Tk()
e = Entry(base, width = 50, borderwidth = 5)
base.title("Simple Calculator")
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)


m = 0


def button_add():
    x = e.get()
    m = int(x)
    e.delete(0,END)
    global t
    t = 1


def button_sub():
    x = e.get()
    m = int(x)
    e.delete(0,END)
    global t
    t = 2


def button_mul():
    x = e.get()
    m = int(x)
    e.delete(0,END)
    global t
    t = 3

def button_div():
    x = e.get()
    m = int(x)
    e.delete(0, END)
    global t
    t = 4

def button_equals():
    s = e.get()
    e.delete(0, END)
    if t == 1:
        e.insert(0, int(s) + m)
    elif t == 2:
        e.insert(0, m - int(s))
    elif t == 3:
        e.insert(0, m * int(s))
    elif t == 4:
        e.insert(0, m / int(s))
#A different font
helv36 = font.Font(family='Arial', size=20)

b0 = Button(base, padx = 55, pady = 25, text = "0", font = helv36, command = lambda: button_click(0))
b1 = Button(base, padx = 55, pady = 25, text = "1", font = helv36, command = lambda: button_click(1))
b2 = Button(base, padx = 55, pady = 25, text = "2", font = helv36, command = lambda: button_click(2))
b3 = Button(base, padx = 55, pady = 25, text = "3", font = helv36, command = lambda: button_click(3))
b4 = Button(base, padx = 55, pady = 25, text = "4", font = helv36, command = lambda: button_click(4))
b5 = Button(base, padx = 55, pady = 25, text = "5", font = helv36, command = lambda: button_click(5))
b6 = Button(base, padx = 55, pady = 25, text = "6", font = helv36, command = lambda: button_click(6))
b7 = Button(base, padx = 55, pady = 25, text = "7", font = helv36, command = lambda: button_click(7))
b8 = Button(base, padx = 55, pady = 25, text = "8", font = helv36, command = lambda: button_click(8))
b9 = Button(base, padx = 55, pady = 25, text = "9", font = helv36, command = lambda: button_click(9))
plus = Button(base, padx = 55, pady = 25, text = "+", font = helv36, command = button_add)
minus = Button(base, padx = 55, pady = 25, text = "-", font = helv36, command = button_sub)
equals = Button(base, padx = 55, pady = 25, text = "=", font = helv36, command = button_equals)
clear = Button(base, padx = 109.5, pady = 25, text = "Clear", font = helv36, command = button_clear)
mul = Button(base, padx = 55, pady = 25, text = "*", font = helv36, command = button_mul)
div = Button(base, padx = 55, pady = 25, text = "/", font = helv36, command = button_div)


b0.grid(row = 4, column = 1)
b1.grid(row = 1 , column = 0)
b2.grid(row = 1 , column = 1)
b3.grid(row = 1 , column = 2)
b4.grid(row = 2 , column = 0)
b5.grid(row = 2 , column = 1)
b6.grid(row = 2 , column = 2)
b7.grid(row = 3 , column = 0)
b8.grid(row = 3 , column = 1)
b9.grid(row = 3 , column = 2)
plus.grid(row = 4 , column = 0)
minus.grid(row = 4 , column = 2)
div.grid(row = 5, column = 1)
mul.grid(row = 5, column = 0)
clear.grid(row = 6 , columnspan = 2, column = 0)
equals.grid(row = 6 , column = 2)
base.mainloop()

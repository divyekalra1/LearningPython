from tkinter import *
from tkinter import font
base = Tk()

base.configure(bg = "#008080")

e = Entry(base, width = 50, borderwidth = 10, font = "calibri 15")

base.title("Simple Calculator")
e.grid(row = 0, column = 0, columnspan = 25, padx = 10, pady = 30)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)


m = 0


def button_add():
    x = e.get()
    global m
    m = float(x)
    e.delete(0,END)
    global t
    t = 1


def button_sub():
    x = e.get()
    global m
    m = float(x)
    e.delete(0,END)
    global t
    t = 2


def button_mul():
    x = e.get()
    global m
    m = float(x)
    e.delete(0,END)
    global t
    t = 3

def button_div():
    x = e.get()
    global m
    m = float(x)
    e.delete(0,END)
    global t
    t = 4

def button_equals():
    s = e.get()
    y = float(s)
    e.delete(0, END)
    if t == 1:
        e.insert(0, y + m)
    elif t == 2:
        e.insert(0, m - y)
    elif t == 3:
        e.insert(0, m * y)
    elif t == 4:
        e.insert(0, m / y)

def button_goback():
    f = e.get()
    length = len(f)
    e.delete(0, END)
    e.insert(0, f[0:length-1])


#A different font
helv36 = font.Font(family='Arial', size=20)

b0 = Button(base, padx = 50, pady = 25, text = "0", font = helv36, command = lambda: button_click(0), bg = "light blue")
b1 = Button(base, padx = 50, pady = 25, text = "1", font = helv36, command = lambda: button_click(1), bg = "light blue")
b2 = Button(base, padx = 50, pady = 25, text = "2", font = helv36, command = lambda: button_click(2), bg = "light blue")
b3 = Button(base, padx = 50, pady = 25, text = "3", font = helv36, command = lambda: button_click(3), bg = "light blue")
b4 = Button(base, padx = 50, pady = 25, text = "4", font = helv36, command = lambda: button_click(4), bg = "light blue")
b5 = Button(base, padx = 50, pady = 25, text = "5", font = helv36, command = lambda: button_click(5), bg = "light blue")
b6 = Button(base, padx = 50, pady = 25, text = "6", font = helv36, command = lambda: button_click(6), bg = "light blue")
b7 = Button(base, padx = 50, pady = 25, text = "7", font = helv36, command = lambda: button_click(7), bg = "light blue")
b8 = Button(base, padx = 50, pady = 25, text = "8", font = helv36, command = lambda: button_click(8), bg = "light blue")
b9 = Button(base, padx = 50, pady = 25, text = "9", font = helv36, command = lambda: button_click(9), bg = "light blue")
plus = Button(base, padx = 50, pady = 25, text = "+", font = helv36, command = button_add, bg = "black", fg = "white")
minus = Button(base, padx = 54, pady = 25, text = "-", font = helv36, command = button_sub, bg = "black", fg = "white")
equals = Button(base, padx = 50, pady = 25, text = "=", font = helv36, command = button_equals, bg = "black", fg = "white")
clear = Button(base, padx = 155, pady = 25, text = "Clear", font = helv36, command = button_clear, bg = "black", fg = "white")
mul = Button(base, padx = 53, pady = 25, text = "*", font = helv36, command = button_mul, bg = "black", fg = "white")
div = Button(base, padx = 54, pady = 25, text = "/", font = helv36, command = button_div, bg = "black", fg = "white")
decimal = Button(base, padx = 54, pady = 25, text = ".", font = helv36, command = button_div, bg = "black", fg = "white")
go_back = Button(base, padx = 35, pady = 25, text = "<---", font = helv36, command = button_goback, bg = "black", fg = "white")


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
plus.grid(row = 1 , column = 3)
minus.grid(row = 2 , column = 3)
div.grid(row = 4, column = 3)
mul.grid(row = 3, column = 3)
clear.grid(row = 5 , columnspan = 3, column = 0)
equals.grid(row = 5 , column = 3)
decimal.grid(row = 4 , column = 2)
go_back.grid(row = 4 , column = 0)

base.mainloop()

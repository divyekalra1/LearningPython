from tkinter import *

base = Tk()
def clicked():
    name = e.get()
    my_label = Label(base, text = f"Look {name}! You just clicked on a button")
    my_label.pack()

e = Entry(base, width = 50)
e.insert(0, "Enter your name here")
e.pack()

button1 = Button(base, command = clicked, text = "CLICK ME", bg = "black" , fg = "white")
button1.pack()
base.mainloop()

from tkinter import *
from PIL import ImageTk,Image
base = Tk()
base.title("Image Viewer")
base.iconbitmap("download.ico")

img1 = ImageTk.PhotoImage(Image.open("download.png"))
img2 = ImageTk.PhotoImage(Image.open("top-50-most-hilarious-Spongebob-meme-9.png"))
img3 = ImageTk.PhotoImage(Image.open("402-4024873_lick-transparent-spongebob-meme-put-you-on-the.png"))
label = Label(image = img1)
back = Button(base, text = "<<", command = lambda: go_back(0))
forward = Button(base, text = ">>", command = lambda: go_forward(2))
exit_prog = Button(base, text = "Exit Program", command = base.quit)

images = [img1, img2, img3]

def go_forward(img_number):
    global forward
    global back
    global label
    label.grid_forget()
    label = Label(image = images[img_number-1])

    if img_number == 3:
        img_number = 0
    forward = Button(base, text = ">>", command = lambda: go_forward(img_number+1))
    back = Button(base, text = "<<", command = lambda: go_back(img_number-1))
    label.grid(row = 0, column = 0, columnspan = 3)
    back.grid(row = 1, column = 0)
    forward.grid(row = 1, column = 3)
def go_back(img_number):
    global forward
    global back
    global label
    label.grid_forget()
    label = Label(image = images[img_number-1])

    if img_number == 1:
        forward = Button(base, text = ">>", command = lambda: go_forward(2))
        back = Button(base, text = "<<", command = lambda: go_back(3))


    forward = Button(base, text = ">>", command = lambda: go_forward(img_number+1))
    back = Button(base, text = "<<", command = lambda: go_back(img_number-1))
    label.grid(row = 0, column = 0, columnspan = 3)
    back.grid(row = 1, column = 0)
    forward.grid(row = 1, column = 3)
label.grid(row = 0, column = 0, columnspan = 3)
back.grid(row = 1, column = 0)
forward.grid(row = 1, column = 3)
exit_prog.grid(row = 1, column = 2)


base.mainloop()

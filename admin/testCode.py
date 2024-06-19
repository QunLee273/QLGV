from tkinter import *

def show_choice():

    label.config(text="Selected: " + var.get())

root = Tk()

var = StringVar()

radio1 = Radiobutton(root, text="Option 1", variable=var, value="Option 1")

radio1.pack()

radio2 = Radiobutton(root, text="Option 2", variable=var, value="Option 2")

radio2.pack()

button = Button(root, text="Show Choice", command=show_choice)

button.pack()

label = Label(root, text="")

label.pack()

root.mainloop()
from tkinter import *
rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Label(relief=GROOVE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.config(text='%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)

mainloop()
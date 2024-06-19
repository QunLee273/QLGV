from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("Quản lý giảng viên")
window.geometry("1280x720")

conn = sqlite3.connect("qlgv.db")
cur = conn.cursor()

tieuDe = Label(window, text="Quản lý giảng viên", font=("Arial", 24), justify="center")
tieuDe.pack()

muc1 = Label(text="Nhập thông tin:", font=("Arial", 18), justify="left")
muc1.pack(side=LEFT, padx=10)

lb_mgv = Label(text="Mgv", font=("Arial", 14))

window.mainloop()
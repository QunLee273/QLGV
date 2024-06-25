import sqlite3
import subprocess
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame, Toplevel, Listbox, Scrollbar, END


def open_register_form():
    with open('ThemTaiKhoan.py', 'r') as file:
        content = file.read()

# Hàm để đăng nhập
def login_user(username_var, password_var):
    username = username_var.get()
    password = password_var.get()

    if username and password:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                SELECT MaNguoiDung, VaiTro FROM TaiKhoan
                WHERE TenDangNhap = ? AND MatKhau = ?
            ''', (username, password))
            result = cursor.fetchone()
            if result:
                manguoidung, vaitro = result
                login_window.destroy()  # Close the login window
                if vaitro == "Quản trị viên":
                    subprocess.run(["python", "Main_AD.py"])

                elif vaitro == "Giảng viên":
                    with open("HienThi.txt", "w") as file:
                        file.write(f"{manguoidung}\n")
                    subprocess.run(["python", "main_GV.py"])

                elif vaitro == "Sinh viên":
                    with open("HienThi.txt", "w") as file:
                        file.write(f"{manguoidung}\n")
                    subprocess.run(["python", "Sinhvien.py"])

                else:
                    messagebox.showerror("Lỗi", "Vai trò không hợp lệ")
                    open_login_form()
            else:
                messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập tên đăng nhập và mật khẩu")
# Hàm để mở form Đăng nhập
def open_login_form():
    global login_window
    login_window = Tk()
    login_window.title("Đăng nhập")
    login_window.geometry("500x300")
    login_window.configure(bg='#f0f0f0')

    username_var = StringVar()
    password_var = StringVar()

    frame = Frame(login_window, bg='#ffffff', padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    Label(frame, text="Tên đăng nhập", font=("Arial", 14), bg='#ffffff').grid(row=0, column=0, pady=5, sticky='w')
    Entry(frame, textvariable=username_var, font=("Arial", 14)).grid(row=0, column=1, pady=10)

    Label(frame, text="Mật khẩu", font=("Arial", 14), bg='#ffffff').grid(row=1, column=0, pady=5, sticky='w')
    Entry(frame, textvariable=password_var, font=("Arial", 14), show='*').grid(row=1, column=1, pady=10)

    Button(frame, text="Đăng nhập", font=("Arial", 14),
           command=lambda: login_user(username_var, password_var),
           bg='#4caf50', fg='#ffffff').grid(row=2, column=0, columnspan=2, pady=10)

    Button(frame, text="thoát", font=("Arial", 14),
           command=exit,
           bg='#2196f3', fg='#ffffff').grid(row=2, column=2, columnspan=2, pady=10)

    login_window.mainloop()

# test Hàm để mở giao diện admin
def open_admin_dashboard():
    login_window.withdraw()
    subprocess.run(["python", "Main_AD.py"])

# Hàm để mở giao diện giảng viên
def open_giangvien_dashboard():
    login_window.withdraw()
    subprocess.run(["python", "main_GV.py"])
def open_sinhvien_dashbroad():
    login_window.withdraw()
    subprocess.run(["python", "Sinhvien.py"])


open_login_form()
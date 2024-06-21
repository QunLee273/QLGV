import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame, Toplevel, Listbox, Scrollbar, END

# Hàm để tạo cơ sở dữ liệu và bảng TaiKhoan nếu chưa tồn tại
def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TaiKhoan (
                TenDangNhap TEXT PRIMARY KEY,
                MatKhau TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS HocPhan (
                MaHP TEXT PRIMARY KEY,
                TenHP TEXT NOT NULL,
                SoTinChi INTEGER NOT NULL
            )
        ''')
        db.commit()

# Gọi hàm tạo cơ sở dữ liệu
create_database()
def login_user(username_var, password_var, login_window):
    username = username_var.get()
    password = password_var.get()

    if username and password:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                SELECT * FROM TaiKhoan WHERE TenDangNhap = ? AND MatKhau = ?
            ''', (username, password))
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("Thành công", "Đăng nhập thành công")
                login_window.destroy()
                open_main_dashboard()
            else:
                messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")
    else:
        messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc")
#Form Đăng nhập
login_window = Tk()
login_window.title("Đăng nhập")
login_window.geometry("400x300")
login_window.configure(bg='#f0f0f0')

username_var = StringVar()
password_var = StringVar()

frame = Frame(login_window, bg='#ffffff', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor='center')

Label(frame, text="Tên đăng nhập", font=("Arial", 14), bg='#ffffff').grid(row=0, column=0, pady=5, sticky='w')
Entry(frame, textvariable=username_var, font=("Arial", 14)).grid(row=0, column=1, pady=5)

Label(frame, text="Mật khẩu", font=("Arial", 14), bg='#ffffff').grid(row=1, column=0, pady=5, sticky='w')
Entry(frame, textvariable=password_var, font=("Arial", 14), show='*').grid(row=1, column=1, pady=5)

Button(frame, text="Đăng nhập", font=("Arial", 14), command=lambda: login_user(username_var, password_var, login_window),
    bg='#4caf50', fg='#ffffff').grid(row=2, column=0, columnspan=2, pady=10)

Button(frame, text="Đăng ký", font=("Arial", 14), bg='#2196f3', fg='#ffffff').grid(row=3, column=0, columnspan=2, pady=10)

login_window.mainloop()
import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame

def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TaiKhoan (
                TenDangNhap TEXT PRIMARY KEY,
                MatKhau TEXT NOT NULL,
                VaiTro TEXT NOT NULL,
                MaNguoiDung TEXT NOT NULL
            )
        ''')
        db.commit()

create_database()

def add_account():
    username = username_var.get()
    password = password_var.get()
    role = role_var.get()
    user_id = user_id_var.get()

    if username and password and role and user_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO TaiKhoan (TenDangNhap, MatKhau, VaiTro, MaNguoiDung)
                    VALUES (?, ?, ?, ?)
                ''', (username, password, role, user_id))
                db.commit()
                messagebox.showinfo("Thành công", "Tài khoản đã được thêm")
                clear_fields()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc")

def clear_fields():
    username_var.set("")
    password_var.set("")
    role_var.set("")
    user_id_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính
window = Tk()
window.title("Thêm tài khoản")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)
window.configure(bg='#f0f0f0')

# Biến lưu trữ giá trị nhập vào
username_var = StringVar()
password_var = StringVar()
role_var = StringVar()
user_id_var = StringVar()

# Tạo Frame để chứa các widget
frame = Frame(window, bg='#ffffff', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Tạo các nhãn và ô nhập liệu
Label(frame, text="Tên đăng nhập", font=("Arial", 16), bg='#ffffff').grid(row=0, column=0, pady=10, sticky='w')
Entry(frame, textvariable=username_var, font=("Arial", 16)).grid(row=0, column=1, pady=10)

Label(frame, text="Mật khẩu", font=("Arial", 16), bg='#ffffff').grid(row=1, column=0, pady=10, sticky='w')
Entry(frame, textvariable=password_var, show='*', font=("Arial", 16)).grid(row=1, column=1, pady=10)

Label(frame, text="Vai trò", font=("Arial", 16), bg='#ffffff').grid(row=2, column=0, pady=10, sticky='w')
Entry(frame, textvariable=role_var, font=("Arial", 16)).grid(row=2, column=1, pady=10)

Label(frame, text="Mã người dùng", font=("Arial", 16), bg='#ffffff').grid(row=3, column=0, pady=10, sticky='w')
Entry(frame, textvariable=user_id_var, font=("Arial", 16)).grid(row=3, column=1, pady=10)

# Tạo nút
Button(frame, text="Thêm tài khoản", font=("Arial", 16), command=add_account, bg='#4caf50', fg='#ffffff').grid(row=4, column=0, pady=20)
Button(frame, text="Xóa", font=("Arial", 16), command=clear_fields, bg='#f44336', fg='#ffffff').grid(row=4, column=1, pady=20)

window.mainloop()
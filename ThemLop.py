import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame

def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Lop (
                MaLop TEXT PRIMARY KEY,
                TenLop TEXT NOT NULL,
                MaGVPT TEXT NOT NULL
            )
        ''')
        db.commit()

create_database()

def add_class():
    class_id = class_id_var.get()
    class_name = class_name_var.get()
    teacher_id = teacher_id_var.get()

    if class_id and class_name and teacher_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO Lop (MaLop, TenLop, MaGVPT)
                    VALUES (?, ?, ?)
                ''', (class_id, class_name, teacher_id))
                db.commit()
                messagebox.showinfo("Thành công", "Lớp học đã được thêm")
                clear_fields()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã lớp đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc")

def clear_fields():
    class_id_var.set("")
    class_name_var.set("")
    teacher_id_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính
window = Tk()
window.title("Thêm lớp học")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)
window.configure(bg='#f0f0f0')

# Biến lưu trữ giá trị nhập vào
class_id_var = StringVar()
class_name_var = StringVar()
teacher_id_var = StringVar()

# Tạo Frame để chứa các widget
frame = Frame(window, bg='#ffffff', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Tạo các nhãn và ô nhập liệu
Label(frame, text="Mã lớp", font=("Arial", 16), bg='#ffffff').grid(row=0, column=0, pady=10, sticky='w')
Entry(frame, textvariable=class_id_var, font=("Arial", 16)).grid(row=0, column=1, pady=10)

Label(frame, text="Tên lớp", font=("Arial", 16), bg='#ffffff').grid(row=1, column=0, pady=10, sticky='w')
Entry(frame, textvariable=class_name_var, font=("Arial", 16)).grid(row=1, column=1, pady=10)

Label(frame, text="Mã GV phụ trách", font=("Arial", 16), bg='#ffffff').grid(row=2, column=0, pady=10, sticky='w')
Entry(frame, textvariable=teacher_id_var, font=("Arial", 16)).grid(row=2, column=1, pady=10)

# Tạo nút
Button(frame, text="Thêm lớp", font=("Arial", 16), command=add_class, bg='#4caf50', fg='#ffffff').grid(row=3, column=0, pady=20)
Button(frame, text="Xóa", font=("Arial", 16), command=clear_fields, bg='#f44336', fg='#ffffff').grid(row=3, column=1, pady=20)
Button(frame, text="Quay lại", font=("Arial", 16), command=exit, bg='#5662f6', fg='#ffffff').grid(row=3, column=2, pady=20)

window.mainloop()
import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame

# Hàm để tạo cơ sở dữ liệu và bảng HocPhan nếu chưa tồn tại
def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
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

# Hàm để thêm môn học vào cơ sở dữ liệu
def add_subject():
    subject_id = subject_id_var.get()
    subject_name = subject_name_var.get()
    credits = credits_var.get()

    if subject_id and subject_name and credits:
        try:
            credits = int(credits)
        except ValueError:
            messagebox.showerror("Lỗi", "Số tín chỉ phải là một số nguyên")
            return

        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO HocPhan (MaHP, TenHP, SoTinChi)
                    VALUES (?, ?, ?)
                ''', (subject_id, subject_name, credits))
                db.commit()
                messagebox.showinfo("Thành công", "Môn học đã được thêm")
                clear_fields()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã học phần đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc")

# Hàm để xóa dữ liệu đã nhập từ các ô nhập liệu
def clear_fields():
    subject_id_var.set("")
    subject_name_var.set("")
    credits_var.set("")

# Hàm để đóng chế độ toàn màn hình khi nhấn phím Escape
def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính và cấu hình giao diện
window = Tk()
window.title("Thêm môn học")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)
window.configure(bg='#f0f0f0')

# Biến lưu trữ giá trị nhập vào
subject_id_var = StringVar()
subject_name_var = StringVar()
credits_var = StringVar()

# Tạo Frame để nhóm các widget và căn chỉnh giao diện
frame = Frame(window, bg='#ffffff', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Tạo các nhãn và ô nhập liệu
Label(frame, text="Mã học phần", font=("Arial", 16), bg='#ffffff').grid(row=0, column=0, pady=10, sticky='w')
Entry(frame, textvariable=subject_id_var, font=("Arial", 16)).grid(row=0, column=1, pady=10)

Label(frame, text="Tên học phần", font=("Arial", 16), bg='#ffffff').grid(row=1, column=0, pady=10, sticky='w')
Entry(frame, textvariable=subject_name_var, font=("Arial", 16)).grid(row=1, column=1, pady=10)

Label(frame, text="Số tín chỉ", font=("Arial", 16), bg='#ffffff').grid(row=2, column=0, pady=10, sticky='w')
Entry(frame, textvariable=credits_var, font=("Arial", 16)).grid(row=2, column=1, pady=10)
# Tạo nút
Button(frame, text="Thêm môn học", font=("Arial", 16), command=add_subject, bg='#4caf50', fg='#ffffff').grid(row=3, column=0, pady=20)
Button(frame, text="Xóa", font=("Arial", 16), command=clear_fields, bg='#f44336', fg='#ffffff').grid(row=3, column=1, pady=20)
Button(frame, text="quay lại", font=("Arial", 16), command=exit, bg='#5662f6', fg='#ffffff').grid(row=3, column=2, pady=20)

window.mainloop()
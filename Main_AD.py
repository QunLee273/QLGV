import subprocess
import sys
from tkinter import Tk, Button, Frame

from PyQt5.uic.properties import QtWidgets


# Hàm mở form quản lý học phần (chưa triển khai)
def open_subject_management():
    window.withdraw()  # Hide the current window
    subprocess.run(["python", "ThemMonHoc.py"])  #
    window.deiconify()

# Hàm mở form tài khoản (chưa triển khai)
def open_account_form():
    window.withdraw()  # Hide the current window
    subprocess.run(["python", "ThemTaiKhoan.py"])  
    window.deiconify()

# Hàm mở form giảng viên (chưa triển khai)
def open_teacher_form():
    window.withdraw()  # Hide the current window
    subprocess.run(["python", "infoGV.py"])  
    window.deiconify()

# Hàm mở form sinh viên (chưa triển khai)
def open_student_form():
    window.withdraw()  # Hide the current window
    subprocess.run(["python", "Sinhvienadmin.py"])  
    window.deiconify()

# Hàm mở form lớp (chưa triển khai)
def open_class_form():
    window.withdraw()  # Hide the current window
    subprocess.run(["python", "ThemLop.py"])  
    window.deiconify()

# Hàm mở form phân công (chưa triển khai)
def open_assignment_form():
    print("Mở form phân công")

# Hàm mở form đánh giá (chưa triển khai)
def open_evaluation_form():
    print("Mở form đánh giá")
def open_baocao():
    window.withdraw()  # Hide the current window
    subprocess.run(["python", 'form.py'])
    window.deiconify()
# Hàm thoát fullscreen khi nhấn phím Esc
def exit_fullscreen(event):
    if event.keysym == 'Escape':
        window.attributes('-fullscreen', False)
        window.unbind('<Escape>')
        window.bind('<Escape>', exit_app)  # Khi ấn Esc lần thứ 2 sẽ thoát ứng dụng

# Hàm thoát ứng dụng khi nhấn Esc lần thứ 2 (đã thoát fullscreen)
def exit_app(event):
    if event.keysym == 'Escape':
        window.destroy()

# Tạo cửa sổ chính và cấu hình giao diện
window = Tk()
window.title("Main Dashboard - Admin")
window.attributes('-fullscreen', True)  # Thiết lập fullscreen
window.configure(bg='#ffffff')

# Bắt sự kiện Esc để thoát fullscreen
window.bind('<Escape>', exit_fullscreen)

# Tạo Frame để chứa các nút chức năng, đặt ở bên trái
menu_frame = Frame(window, bg='#ffffff', padx=20, pady=20)
menu_frame.pack(side='left', fill='y')

# Tạo các nút chức năng
btn_account = Button(menu_frame, text="Tài khoản", font=("Arial", 12), width=15, height=2, command=open_account_form)
btn_account.pack(fill='x', pady=10)

btn_teacher = Button(menu_frame, text="Giảng viên", font=("Arial", 12), width=15, height=2, command=open_teacher_form)
btn_teacher.pack(fill='x', pady=10)

btn_student = Button(menu_frame, text="Sinh viên", font=("Arial", 12), width=15, height=2, command=open_student_form)
btn_student.pack(fill='x', pady=10)

btn_class = Button(menu_frame, text="Lớp", font=("Arial", 12), width=15, height=2, command=open_class_form)
btn_class.pack(fill='x', pady=10)

btn_assignment = Button(menu_frame, text="Phân công", font=("Arial", 12), width=15, height=2, command=open_assignment_form)
btn_assignment.pack(fill='x', pady=10)

btn_subject = Button(menu_frame, text="Học phần", font=("Arial", 12), width=15, height=2, command=open_subject_management)
btn_subject.pack(fill='x', pady=10)

btn_evaluation = Button(menu_frame, text="Đánh giá", font=("Arial", 12), width=15, height=2, command=open_evaluation_form)
btn_evaluation.pack(fill='x', pady=10)

btn_evaluation = Button(menu_frame, text="Thống kê và báo cáo", font=("Arial", 12), width=15, height=2,command=open_baocao)
btn_evaluation.pack(fill='x', pady=10)

btn_exit = Button(menu_frame, text="Đăng xuất và thoát", font=("Arial", 12), width=15, height=2, command = exit)
btn_exit.pack(fill='x', pady=10)
# Chạy ứng dụng
window.mainloop()


def main():
    app = QtWidgets.QApplication(sys.argv)

    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())


if __name__ == "__main__":
    main()


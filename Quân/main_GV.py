from tkinter import *
import sqlite3
from tkinter import ttk

main_GV = Tk()
main_GV.title("Giảng viên")

# Kết nối DB
conn = sqlite3.connect("qlgv.db")
cur = conn.cursor()

def manHinh(event):
    main_GV.attributes("-fullscreen", not main_GV.attributes("-fullscreen"))
    main_GV.geometry("1280x720")


def ht_infor():
    # Tạo cửa sổ mới
    win_infor = Toplevel(main_GV)
    win_infor.title("Thông tin Giảng viên")

    # Tạo và cấu hình Treeview
    tree = ttk.Treeview(win_infor, columns=["mgv", "hoten", "nsinh", "gioiT", "diaC", "mail", "sdt"], show='headings')
    tree.heading("mgv", text="Mã GV")
    tree.heading("hoten", text="Họ tên")
    tree.heading("nsinh", text="Ngày sinh")
    tree.heading("gioiT", text="Giới tính")
    tree.heading("diaC", text="Địa chỉ")
    tree.heading("mail", text="Email")
    tree.heading("sdt", text="Số điện thoại")
    tree.pack()

    # Lấy dữ liệu từ database
    cur.execute("SELECT * FROM GiangVien WHERE MaGV = ?", (ten_ht,))
    rows = cur.fetchall()

    # Hiển thị dữ liệu trong Treeview
    for row in rows:
        tree.insert("", "end", values=row)

def ht_phanC():
    # Tạo cửa sổ mới
    win_phanC = Toplevel(main_GV)
    win_phanC.title("Phân công giảng dạy")

    # Tạo và cấu hình Treeview
    tree = ttk.Treeview(win_phanC, columns=["mapc", "hp", "hocKy", "nam", "lop"], show='headings')
    tree.heading("mapc", text="MaPC")
    tree.heading("hp", text="Học phần")
    tree.heading("hocKy", text="Học kỳ")
    tree.heading("nam", text="Năm học")
    tree.heading("lop", text="Lớp")
    tree.pack()

    # Lấy dữ liệu từ database
    cur.execute(
        """SELECT PhanCong.MaPC, HocPhan.TenHP, PhanCong.HocKy, PhanCong.NamHoc, Lop.TenLop 
            FROM PhanCong, HocPhan, Lop
            WHERE PhanCong.MaHP = HocPhan.MaHP AND PhanCong.MaLop = Lop.MaLop AND PhanCOng.MaGV = ?
            """, (ten_ht, ))
    rows = cur.fetchall()

    # Hiển thị dữ liệu trong Treeview
    for row in rows:
        tree.insert("", "end", values=row)

def ht_danhGia():
    # Tạo cửa sổ mới
    win_danhGia = Toplevel(main_GV)
    win_danhGia.title("Đánh giá giảng viên")

    # Tạo và cấu hình Treeview
    tree = ttk.Treeview(win_danhGia, columns=["madg", "noidung", "diem", "ngay"], show='headings')
    tree.heading("madg", text="MaDG")
    tree.heading("noidung", text="Nội dung")
    tree.heading("diem", text="Điểm số")
    tree.heading("ngay", text="Ngày đánh giá")
    tree.pack()

    # Lấy dữ liệu từ database
    cur.execute(
        """SELECT MaDG, NoiDung, DiemSo, NgayDanhGia 
            FROM DanhGia 
            WHERE MaGV = ? """, (ten_ht, ))
    rows = cur.fetchall()

    # Hiển thị dữ liệu trong Treeview
    for row in rows:
        tree.insert("", "end", values=row)


lb_GV = Label(main_GV, font=("Arial", 18, 'bold'), bd=2, relief=SOLID)
lb_GV.place(x=40, y=40, width=250, height=40)

btn_info = Button(main_GV, text="Thông tin", width=15, font=("Arial", 12, 'bold'), command=ht_infor)
btn_info.place(x=50, y=150, width=200, height=40)

btn_pC = Button(main_GV, text="Phân công", width=15, font=("Arial", 12, 'bold'), command=ht_phanC)
btn_pC.place(x=50, y=200, width=200, height=40)

btn_dg = Button(main_GV, text="Xem đánh giá", width=15, font=("Arial", 12, 'bold'), command=ht_danhGia)
btn_dg.place(x=50, y=250, width=200, height=40)

btn_dangX = Button(main_GV, text="Đăng xuất", width=15, font=("Arial", 12, 'bold'), command=exit)
btn_dangX.place(x=50, y=500, width=200, height=40)

# Hiển thị tên
with open('HienThi.txt', 'r') as f:
    ten_ht = f.read().strip()
    # Lấy dữ liệu từ database
    cur.execute(
        """SELECT Hoten 
            FROM GiangVien 
            WHERE MaGV = ? """, (ten_ht, ))
    ten = cur.fetchone()
    ten = ten[0]
    lb_GV.config(text=ten) # Cập nhật Label

# Bật/tắt toàn màn hình
main_GV.bind("<Escape>", manHinh)
main_GV.attributes("-fullscreen", True)

main_GV.mainloop()
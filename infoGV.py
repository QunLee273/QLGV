from datetime import datetime
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox

main_GV = Tk()
main_GV.title("Quản lý giảng viên")
main_GV.geometry("1920x1080")

# Kết nối DB
conn = sqlite3.connect("qlgv.db")
cur = conn.cursor()


def ht_bang():
    # Xóa dữ liệu cũ trong Treeview
    for row in bang.get_children():
        bang.delete(row)

    # Truy vấn dữ liệu từ CSDL
    cur.execute("SELECT * FROM GiangVien")
    rows = cur.fetchall()

    # Điền dữ liệu vào Treeview
    for row in rows:
        bang.insert("", END, values=row)

def kT_NgaySinh(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def them():
    # Lấy dữ liệu từ các Entry và Radiobutton
    mgv = et_mgv.get()
    ten = et_tenGV.get()
    nSinh = et_ns.get()
    gTinh = gt.get()
    dC = et_dc.get()
    mail = et_mail.get()
    sdt = et_SDT.get()

    # Kiểm tra Ngày sinh đúng dịnh dạng không
    kT_NgaySinh(nSinh)

    # Kiểm tra các trường thông tin có được điền đầy đủ không
    if mgv == '' or ten == '' or nSinh == '' or gTinh == '' or dC == '' or mail == '' or sdt == '':
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        return

    try:
        # Kiểm tra xem Mã GV đã tồn tại chưa
        cur.execute("SELECT * FROM GiangVien WHERE MaGV=?", (mgv,))
        row = cur.fetchone()
        if row:
            messagebox.showerror("Lỗi", f"Mã GV: '{mgv}' đã tồn tại. Vui lòng nhập Mã GV khác.")
            return

        # Thực hiện câu lệnh SQL để thêm dữ liệu vào CSDL
        cur.execute(
            """INSERT INTO GiangVien (MaGV, HoTen, NgaySinh, GioiTinh, DiaChi, Email, SoDienThoai) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (mgv, ten, nSinh, gTinh, dC, mail, sdt))

        # Lưu thay đổi và commit vào CSDL
        conn.commit()

        # Hiển thị thông báo khi thêm thành công
        messagebox.showinfo("Thông báo", "Thêm giảng viên thành công")

        # Cập nhật lại bảng hiển thị dữ liệu
        ht_bang()

        # Xóa dữ liệu trong các Entry sau khi thêm thành công
        et_mgv.delete(0, END)
        et_tenGV.delete(0, END)
        et_ns.delete(0, END)
        gt.set('')  # Reset Radiobutton
        et_dc.delete(0, END)
        et_mail.delete(0, END)
        et_SDT.delete(0, END)

    except Exception as e:
        # Hiển thị thông báo khi có lỗi xảy ra
        messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")


def sua():
    # Lấy dữ liệu từ các Entry và Radiobutton
    mgv = et_mgv.get()
    ten = et_tenGV.get()
    nSinh = et_ns.get()
    gTinh = gt.get()
    dC = et_dc.get()
    mail = et_mail.get()
    sdt = et_SDT.get()

    # Kiểm tra xem người dùng đã chọn giảng viên nào để sửa chưa
    chon = bang.focus()  # Lấy item được chọn trong Treeview
    if not chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn giảng viên cần sửa trong danh sách.")
        return

    # Lấy thông tin của giảng viên được chọn từ Treeview
    item = bang.item(chon, 'values')
    mgv_cu = item[0]  # Mã GV cũ của giảng viên

    # Kiểm tra xem người dùng đã nhập thông tin cần sửa chưa
    if not (mgv or ten or nSinh or gTinh or dC or mail or sdt):
        messagebox.showerror("Lỗi", "Vui lòng nhập ít nhất một trường thông tin cần sửa.")
        return

    try:
        # Bắt đầu xây dựng câu lệnh SQL để cập nhật
        sql = "UPDATE GiangVien SET "
        lst = []

        # Kiểm tra và thêm các cột cần cập nhật vào câu lệnh SQL
        if mgv:
            sql += "MaGV = ?, "
            lst.append(mgv)
        if ten:
            sql += "HoTen = ?, "
            lst.append(ten)
        if nSinh:
            sql += "NgaySinh = ?, "
            lst.append(nSinh)
        if gTinh:
            sql += "GioiTinh = ?, "
            lst.append(gTinh)
        if dC:
            sql += "DiaChi = ?, "
            lst.append(dC)
        if mail:
            sql += "Email = ?, "
            lst.append(mail)
        if sdt:
            sql += "SoDienThoai = ?, "
            lst.append(sdt)

        # Xóa ký tự ", " cuối cùng của câu lệnh SQL
        sql = sql.rstrip(", ")

        # Thêm điều kiện WHERE để chỉ cập nhật dòng có MaGV tương ứng
        sql += " WHERE MaGV = ?"
        lst.append(mgv_cu)

        # Thực hiện câu lệnh SQL để cập nhật dữ liệu vào CSDL
        cur.execute(sql, lst)

        # Lưu thay đổi và commit vào CSDL
        conn.commit()

        # Hiển thị thông báo khi sửa thành công
        messagebox.showinfo("Thông báo", "Sửa thông tin giảng viên thành công")

        # Cập nhật lại bảng hiển thị dữ liệu
        ht_bang()

        # Xóa dữ liệu trong các Entry sau khi sửa thành công
        et_mgv.delete(0, END)
        et_tenGV.delete(0, END)
        et_ns.delete(0, END)
        gt.set('')  # Reset Radiobutton
        et_dc.delete(0, END)
        et_mail.delete(0, END)
        et_SDT.delete(0, END)

    except Exception as e:
        # Hiển thị thông báo khi có lỗi xảy ra
        messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")



## Tạo form
#Label, Entry

tieuDe = Label(main_GV, text="Quản lý giảng viên", font=("Arial", 24, 'bold'), justify="center")
tieuDe.grid(column=4, row=0, padx=15, pady=15)

muc1 = Label(main_GV, text="Nhập thông tin:", font=("Arial", 18, 'bold'), justify="left")
muc1.grid(row=1, column=1, padx=5, pady=5)

et_tk = Entry(main_GV, width=50)
et_tk.grid(row=1, column=4, padx=5, pady=5, columnspan=2)

lb_mgv = Label(main_GV, text="Mã GV: ")
lb_mgv.grid(row=2, column=0, padx=5, pady=5)
et_mgv = Entry(main_GV, width=30)
et_mgv.grid(row=2, column=1, padx=5, pady=5)

lb_tenGV = Label(main_GV, text="Tên GV: ")
lb_tenGV.grid(row=3, column=0, padx=5, pady=5)
et_tenGV = Entry(main_GV, width=30)
et_tenGV.grid(row=3, column=1, padx=5, pady=5)

lb_ns = Label(main_GV, text="Ngày sinh(yyyy-mm-dd): ")
lb_ns.grid(row=4, column=0, padx=5, pady=5)
et_ns = Entry(main_GV, width=30)
et_ns.grid(row=4, column=1, padx=5, pady=5)

lb_gt = Label(main_GV, text="Giới tính: ")
lb_gt.grid(row=5, column=0, padx=5, pady=5)
gt = StringVar()
Radiobutton(main_GV, text="Nam", padx=5, variable=gt, value='Nam').place(x=170, y=230)
Radiobutton(main_GV, text="Nữ", padx =10, variable=gt, value='Nữ').place(x=230, y=230)
Radiobutton(main_GV, text="Khác", padx=15, variable=gt, value='Khác').place(x=290, y=230)

lb_dc = Label(main_GV, text="Địa chỉ: ")
lb_dc.grid(row=6, column=0, padx=5, pady=5)
et_dc = Entry(main_GV, width=30)
et_dc.grid(row=6, column=1, padx=5, pady=5)

lb_mail = Label(main_GV, text="Email: ")
lb_mail.grid(row=7, column=0, padx=5, pady=5)
et_mail = Entry(main_GV, width=30)
et_mail.grid(row=7, column=1, padx=5, pady=5)

lb_SDT = Label(main_GV, text="SĐT: ")
lb_SDT.grid(row=8, column=0, padx=5, pady=5)
et_SDT = Entry(main_GV, width=30)
et_SDT.grid(row=8, column=1, padx=5, pady=5)

# Button

btn_tk = Button(main_GV, text="Tìm kiếm:")
btn_tk.grid(row=1, column=5, padx=5, pady=5)

btn_add = Button(main_GV, text="Thêm", width=15, font=("Arial", 12, 'bold'), command=them)
btn_add.grid(row=9, column=0, padx=5, pady=5)

btn_upd = Button(main_GV, text="Sửa", width=15, font=("Arial", 12, 'bold'), command=sua)
btn_upd.grid(row=9, column=1, padx=5, pady=5)

btn_del = Button(main_GV, text="Xóa", width=15, font=("Arial", 12, 'bold'))
btn_del.grid(row=9, column=3, padx=5, pady=5)

# Treeview để hiển thị dữ liệu dưới dạng bảng
bang = ttk.Treeview(main_GV, columns=("MGV", "TenGV", "NgaySinh", "GioiTính", "DiaChỉ", "Email", "SDT"), show="headings")
bang.grid(row=2, column=4, padx=10, pady=10, rowspan=7, columnspan=4)

# Đặt tên cho các cột
bang.heading("MGV", text="Mã GV")
bang.heading("TenGV", text="Tên GV")
bang.heading("NgaySinh", text="Ngày sinh")
bang.heading("GioiTính", text="Giới tính")
bang.heading("DiaChỉ", text="Địa chỉ")
bang.heading("Email", text="Email")
bang.heading("SDT", text="SĐT")

# Đặt kích thước ô
bang.column("MGV", width=50)
bang.column("TenGV", width=120)
bang.column("NgaySinh", width=80)
bang.column("GioiTính", width=80)
bang.column("DiaChỉ", width=200)
bang.column("Email", width=200)
bang.column("SDT", width=100)

# Hiển thị dữ liệu vào bảng
ht_bang()

main_GV.mainloop()
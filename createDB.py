import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect('Quân/qlgv.db')
cur = conn.cursor()

# Tạo bảng Giảng viên
cur.execute('''
CREATE TABLE IF NOT EXISTS GiangVien (
    MaGV TEXT PRIMARY KEY,
    HoTen TEXT,
    NgaySinh DATE,
    GioiTinh TEXT,
    DiaChi TEXT,
    Email TEXT,
    SoDienThoai TEXT
)
''')

# Tạo bảng Học phần
cur.execute('''
CREATE TABLE IF NOT EXISTS HocPhan (
    MaHP TEXT PRIMARY KEY,
    TenHP TEXT,
    SoTinChi INTEGER
)
''')

# Tạo bảng Phân công giảng dạy
cur.execute('''
CREATE TABLE IF NOT EXISTS PhanCong (
    MaPC INTEGER PRIMARY KEY AUTOINCREMENT,
    MaGV TEXT,
    MaHP TEXT,
    HocKy TEXT,
    NamHoc TEXT,
    MaLop TEXT,
    FOREIGN KEY (MaGV) REFERENCES GiangVien(MaGV) ON DELETE SET NULL,
    FOREIGN KEY (MaHP) REFERENCES HocPhan(MaHP) ON DELETE SET NULL,
    FOREIGN KEY (MaLop) REFERENCES Lop(MaLop) ON DELETE SET NULL
)
''')

# Tạo bảng Sinh viên
cur.execute('''
CREATE TABLE IF NOT EXISTS SinhVien (
    MaSV TEXT PRIMARY KEY,
    HoTen TEXT,
    NgaySinh DATE,
    GioiTinh TEXT,
    DiaChi TEXT,
    Email TEXT,
    SoDienThoai TEXT,
    MaLop TEXT,
    FOREIGN KEY (MaLop) REFERENCES Lop(MaLop) ON DELETE SET NULL
)
''')

# Tạo bảng Đánh giá giảng viên
cur.execute('''
CREATE TABLE IF NOT EXISTS DanhGia (
    MaDG INTEGER PRIMARY KEY AUTOINCREMENT,
    MaGV TEXT,
    MaSV TEXT,
    NoiDung TEXT,
    DiemSo INTEGER CHECK (DiemSo >= 1 AND DiemSo <= 10),
    NgayDanhGia DATE,
    FOREIGN KEY (MaGV) REFERENCES GiangVien(MaGV) ON DELETE SET NULL,
    FOREIGN KEY (MaSV) REFERENCES SinhVien(MaSV) ON DELETE SET NULL
)
''')

# Tạo bảng Tài khoản
cur.execute('''
CREATE TABLE IF NOT EXISTS TaiKhoan (
    TenDangNhap TEXT PRIMARY KEY,
    MatKhau TEXT,
    VaiTro TEXT,
    MaNguoiDung TEXT,
    FOREIGN KEY (MaNguoiDung) REFERENCES GiangVien(MaGV) ON DELETE CASCADE,
    FOREIGN KEY (MaNguoiDung) REFERENCES SinhVien(MaSV) ON DELETE CASCADE
)
''')

# Tạo bảng Lớp
cur.execute('''
CREATE TABLE IF NOT EXISTS Lop (
    MaLop TEXT PRIMARY KEY,
    TenLop TEXT,
    MaGVPT TEXT,
    FOREIGN KEY (MaGVPT) REFERENCES GiangVien(MaGV) ON DELETE SET NULL
)
''')

# Thêm dữ liệu mẫu vào các bảng

# Thêm giảng viên
cur.executemany('''
INSERT INTO GiangVien (MaGV, HoTen, NgaySinh, GioiTinh, DiaChi, Email, SoDienThoai) VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ('GV001', 'Nguyễn Văn A', '1975-05-20', 'Nam', '123 Lê Lợi, Hà Nội', 'nguyenvana@example.com', '0123456789'),
    ('GV002', 'Trần Thị B', '1980-10-10', 'Nữ', '456 Trần Hưng Đạo, Hà Nội', 'tranthib@example.com', '0987654321')
])

# Thêm học phần
cur.executemany('''
INSERT INTO HocPhan (MaHP, TenHP, SoTinChi) VALUES (?, ?, ?)
''', [
    ('HP001', 'Lập trình C', 3),
    ('HP002', 'Cơ sở dữ liệu', 4)
])

# Thêm phân công giảng dạy
cur.executemany('''
INSERT INTO PhanCong (MaGV, MaHP, HocKy, NamHoc, MaLop) VALUES (?, ?, ?, ?, ?)
''', [
    ('GV001', 'HP001', 'HK1', '2023-2024', 'L01'),
    ('GV002', 'HP002', 'HK2', '2023-2024', 'L02')
])

# Thêm sinh viên
cur.executemany('''
INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, GioiTinh, DiaChi, Email, SoDienThoai, MaLop) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('SV001', 'Lê Văn C', '2000-08-15', 'Nam', '789 Nguyễn Trãi, Hà Nội', 'levanc@example.com', '0123456789', 'L01'),
    ('SV002', 'Phạm Thị D', '2001-12-10', 'Nữ', '123 Trần Phú, Hà Nội', 'phamthid@example.com', '0987654321', 'L02')
])

# Thêm đánh giá giảng viên
cur.executemany('''
INSERT INTO DanhGia (MaGV, MaSV, NoiDung, DiemSo, NgayDanhGia) VALUES (?, ?, ?, ?, ?)
''', [
    ('GV001', 'SV001', 'Giảng viên dạy rất tốt và nhiệt tình', 9, '2024-06-15'),
    ('GV002', 'SV002', 'Phong cách giảng dạy chưa hấp dẫn', 6, '2024-06-16')
])

# Thêm tài khoản
cur.executemany('''
INSERT INTO TaiKhoan (TenDangNhap, MatKhau, VaiTro, MaNguoiDung) VALUES (?, ?, ?, ?)
''', [
    ('admin', 'abc1', 'Quản trị viên', None),
    ('nguyenvana', 'abc1', 'Giảng viên', 'GV001'),
    ('levanc', 'abc1', 'Sinh viên', 'SV001')
])

# Thêm lớp
cur.executemany('''
INSERT INTO Lop (MaLop, TenLop, MaGVPT) VALUES (?, ?, ?)
''', [
    ('L01', 'Lớp 1', 'GV001'),
    ('L02', 'Lớp 2', 'GV002')
])

conn.commit()
conn.close()

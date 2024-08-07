# Form implementation generated from reading ui file 'giangvien_ss2.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

import pandas as pd
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class baocao(object):
    def resize_table_views(self):

        for table_view in [self.tablegiangvien, self.tablehocphan, self.tablelophoc, self.tablephancong,
                           self.tabledanhgia]:
            table_view.horizontalHeader().setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.Stretch)
            table_view.verticalHeader().setDefaultSectionSize(40)


        button_width = 120
        button_height = 40
        for button in [self.xuatgiangvien, self.xuathocphan, self.xuatlophoc, self.xuatphancong, self.xuatdanhgia]:
            button.setFixedWidth(button_width)
            button.setFixedHeight(button_height)

        button_height = 40
        button_spacing = 15

        for layout in [self.verticalLayout, self.verticalLayout_2]:
            layout.setSpacing(button_spacing)
            for button in layout.findChildren(QtWidgets.QPushButton):
                button.setFixedHeight(button_height)


    def search(self):
        keyword = self.search_input.text()


        current_index = self.stackedWidget.currentIndex()

        if current_index == 5:  # Trang giảng viên
            self.search_giangvien(keyword)
        elif current_index == 1:  # Trang học phần
            self.search_hocphan(keyword)
        elif current_index == 2:  # Trang lớp học
            self.search_lophoc(keyword)
        elif current_index == 3:  # Trang phân công
            self.search_phancong(keyword)
        elif current_index == 4:  # Trang đánh giá
            self.search_danhgia(keyword)

    def search_giangvien(self, keyword):
        model = QSqlQueryModel()
        model.setQuery(f"""
            SELECT HoTen,NgaySinh,GioiTinh,DiaChi,Email,SoDienThoai
            FROM GiangVien
            WHERE HoTen LIKE '%{keyword}%'
        """)
        self.tablegiangvien.setModel(model)

    def search_hocphan(self, keyword):
        model = QSqlQueryModel()
        model.setQuery(f"""
                SELECT hp.MaHP, hp.TenHP, hp.SoTinChi, gv.HoTen AS TenGiangVien, pc.HocKy, pc.NamHoc
                FROM HocPhan hp
                LEFT JOIN PhanCong pc ON hp.MaHP = pc.MaHP
                LEFT JOIN GiangVien gv ON pc.MaGV = gv.MaGV
                WHERE hp.TenHP LIKE '%{keyword}%' OR gv.HoTen LIKE '%{keyword}%'
            """)

        self.tablehocphan.setModel(model)  # Chỉ đặt model khi có kết quả
    def search_lophoc(self, keyword):
        model = QSqlQueryModel()
        model.setQuery(f"""
        SELECT sv.MaSV, sv.HoTen, sv.NgaySinh, sv.GioiTinh, sv.DiaChi, sv.Email, sv.SoDienThoai, l.TenLop
        FROM SinhVien sv
        JOIN Lop l ON sv.MaLop = l.MaLop 
        WHERE sv.HoTen LIKE '%{keyword}%'
    """)
        self.tablelophoc.setModel(model)
    def search_phancong(self, keyword):
        model = QSqlQueryModel()
        model.setQuery(f"""
                SELECT pc.MaPC, gv.HoTen AS GiangVien, hp.TenHP AS HocPhan, pc.HocKy, pc.NamHoc, l.TenLop AS Lop
                FROM PhanCong pc
                JOIN GiangVien gv ON pc.MaGV = gv.MaGV
                JOIN HocPhan hp ON pc.MaHP = hp.MaHP
                LEFT JOIN Lop l ON pc.MaLop = l.MaLop 
                WHERE gv.HoTen LIKE '%{keyword}%'
            """)
        self.tablephancong.setModel(model)
    def search_danhgia(self, keyword):
        model = QSqlQueryModel()
        model.setQuery(f"""
        SELECT dg.MaDG, gv.HoTen AS TenGiangVien, sv.HoTen AS TenSinhVien, dg.NoiDung, dg.DiemSo, dg.NgayDanhGia
        FROM DanhGia dg
        JOIN GiangVien gv ON dg.MaGV = gv.MaGV
        JOIN SinhVien sv ON dg.MaSV = sv.MaSV
        WHERE gv.HoTen LIKE '%{keyword}%'
    """)
        self.tabledanhgia.setModel(model)



    def load_giangvien_data(self):
        model = QSqlQueryModel()
        model.setQuery("select HoTen,NgaySinh,GioiTinh,DiaChi,Email,SoDienThoai from Giangvien")  # Giả sử bảng GiangVien tồn tại
        self.tablegiangvien.setModel(model)

    def load_hocphan_data(self):
        model = QSqlQueryModel()
        model.setQuery("""SELECT hp.MaHP, hp.TenHP, hp.SoTinChi, gv.HoTen AS TenGiangVien, pc.HocKy, pc.NamHoc
                            FROM HocPhan hp
                            JOIN PhanCong pc ON hp.MaHP = pc.MaHP
                            JOIN GiangVien gv ON pc.MaGV = gv.MaGV""")  # Giả sử bảng HocPhan tồn tại
        self.tablehocphan.setModel(model)

    def load_lophoc_data(self):
        model = QSqlQueryModel()
        model.setQuery("""SELECT sv.MaSV, sv.HoTen, sv.NgaySinh, sv.GioiTinh, sv.DiaChi, sv.Email, sv.SoDienThoai, l.TenLop
                            FROM SinhVien sv
                            JOIN Lop l ON sv.MaLop = l.MaLop""")  # Giả sử bảng LopHoc tồn tại
        self.tablelophoc.setModel(model)

    def load_phancong_data(self):
        model = QSqlQueryModel()
        model.setQuery('''
    SELECT pc.MaPC, gv.HoTen AS GiangVien, hp.TenHP AS HocPhan, pc.HocKy, pc.NamHoc, l.TenLop AS Lop
    FROM PhanCong pc
    JOIN GiangVien gv ON pc.MaGV = gv.MaGV
    JOIN HocPhan hp ON pc.MaHP = hp.MaHP
    LEFT JOIN Lop l ON pc.MaLop = l.MaLop
''')  # Giả sử bảng PhanCong tồn tại
        self.tablephancong.setModel(model)

    def load_danhgia_data(self):
        model = QSqlQueryModel()
        model.setQuery("""SELECT dg.MaDG, gv.HoTen, sv.HoTen, dg.NoiDung, dg.DiemSo, dg.NgayDanhGia
                        FROM DanhGia dg
                        JOIN GiangVien gv ON dg.MaGV = gv.MaGV
                        JOIN SinhVien sv ON dg.MaSV = sv.MaSV""")  # Giả sử bảng LichHoc tồn tại
        self.tabledanhgia.setModel(model)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 728)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(parent=self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.giangvien_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.giangvien_btn1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("mu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.giangvien_btn1.setIcon(icon)
        self.giangvien_btn1.setIconSize(QtCore.QSize(20, 20))
        self.giangvien_btn1.setCheckable(True)
        self.giangvien_btn1.setAutoExclusive(True)
        self.giangvien_btn1.setObjectName("giangvien_btn1")
        self.verticalLayout.addWidget(self.giangvien_btn1)
        self.hocphan_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.hocphan_btn1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("laptop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("laptop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.hocphan_btn1.setIcon(icon1)
        self.hocphan_btn1.setIconSize(QtCore.QSize(20, 20))
        self.hocphan_btn1.setCheckable(True)
        self.hocphan_btn1.setAutoExclusive(True)
        self.hocphan_btn1.setObjectName("hocphan_btn1")
        self.verticalLayout.addWidget(self.hocphan_btn1)
        self.lophoc_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.lophoc_btn1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("phanconggiangday.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("phanconggiangday.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.lophoc_btn1.setIcon(icon2)
        self.lophoc_btn1.setIconSize(QtCore.QSize(20, 20))
        self.lophoc_btn1.setCheckable(True)
        self.lophoc_btn1.setAutoExclusive(True)
        self.lophoc_btn1.setObjectName("lophoc_btn1")
        self.verticalLayout.addWidget(self.lophoc_btn1)
        self.phancong_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.phancong_btn1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("amduong.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap("amduong.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.phancong_btn1.setIcon(icon3)
        self.phancong_btn1.setIconSize(QtCore.QSize(20, 20))
        self.phancong_btn1.setCheckable(True)
        self.phancong_btn1.setAutoExclusive(True)
        self.phancong_btn1.setObjectName("phancong_btn1")
        self.verticalLayout.addWidget(self.phancong_btn1)
        self.danhgia_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.danhgia_btn1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("lich.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap("lich.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.danhgia_btn1.setIcon(icon4)
        self.danhgia_btn1.setIconSize(QtCore.QSize(20, 20))
        self.danhgia_btn1.setCheckable(True)
        self.danhgia_btn1.setAutoExclusive(True)
        self.danhgia_btn1.setObjectName("danhgia_btn1")
        self.verticalLayout.addWidget(self.danhgia_btn1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(parent=self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.giangvien_btn2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/home-4-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap("icon/home-4-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.giangvien_btn2.setIcon(icon6)
        self.giangvien_btn2.setIconSize(QtCore.QSize(14, 14))
        self.giangvien_btn2.setCheckable(True)
        self.giangvien_btn2.setAutoExclusive(True)
        self.giangvien_btn2.setObjectName("giangvien_btn2")
        self.verticalLayout_2.addWidget(self.giangvien_btn2)
        self.hocphan_btn2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/dashboard-5-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon7.addPixmap(QtGui.QPixmap("icon/dashboard-5-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.hocphan_btn2.setIcon(icon7)
        self.hocphan_btn2.setIconSize(QtCore.QSize(14, 14))
        self.hocphan_btn2.setCheckable(True)
        self.hocphan_btn2.setAutoExclusive(True)
        self.hocphan_btn2.setObjectName("hocphan_btn2")
        self.verticalLayout_2.addWidget(self.hocphan_btn2)
        self.lophoc_btn2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/activity-feed-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon8.addPixmap(QtGui.QPixmap("icon/activity-feed-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.lophoc_btn2.setIcon(icon8)
        self.lophoc_btn2.setIconSize(QtCore.QSize(14, 14))
        self.lophoc_btn2.setCheckable(True)
        self.lophoc_btn2.setAutoExclusive(True)
        self.lophoc_btn2.setObjectName("lophoc_btn2")
        self.verticalLayout_2.addWidget(self.lophoc_btn2)
        self.phancong_btn2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/product-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon9.addPixmap(QtGui.QPixmap("icon/product-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.phancong_btn2.setIcon(icon9)
        self.phancong_btn2.setIconSize(QtCore.QSize(14, 14))
        self.phancong_btn2.setCheckable(True)
        self.phancong_btn2.setAutoExclusive(True)
        self.phancong_btn2.setObjectName("phancong_btn2")
        self.verticalLayout_2.addWidget(self.phancong_btn2)
        self.danhgia_btn2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/group-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon10.addPixmap(QtGui.QPixmap("icon/group-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.danhgia_btn2.setIcon(icon10)
        self.danhgia_btn2.setIconSize(QtCore.QSize(14, 14))
        self.danhgia_btn2.setCheckable(True)
        self.danhgia_btn2.setAutoExclusive(True)
        self.danhgia_btn2.setObjectName("danhgia_btn2")
        self.verticalLayout_2.addWidget(self.danhgia_btn2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(parent=self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_btn = QtWidgets.QPushButton(parent=self.widget)
        self.menu_btn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon11.addPixmap(QtGui.QPixmap("menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.menu_btn.setIcon(icon11)
        self.menu_btn.setIconSize(QtCore.QSize(14, 14))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_4.addWidget(self.menu_btn)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(parent=self.widget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(parent=self.widget)
        self.search_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("timkiem.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon12.addPixmap(QtGui.QPixmap("timkiem.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.search_btn.setIcon(icon12)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.home)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.home)
        self.hocphan = QtWidgets.QWidget()
        self.hocphan.setObjectName("hocphan")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.hocphan)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.hocphan)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.tablehocphan = QtWidgets.QTableView(parent=self.hocphan)
        self.tablehocphan.setObjectName("tablehocphan")
        self.gridLayout_3.addWidget(self.tablehocphan, 0, 0, 1, 1)
        self.xuathocphan = QtWidgets.QPushButton(parent=self.hocphan)
        self.xuathocphan.setObjectName("xuathocphan")
        self.gridLayout_3.addWidget(self.xuathocphan, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.hocphan)
        self.lophoc = QtWidgets.QWidget()
        self.lophoc.setObjectName("lophoc")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.lophoc)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.xuatlophoc = QtWidgets.QPushButton(parent=self.lophoc)
        self.xuatlophoc.setObjectName("xuatlophoc")
        self.gridLayout_4.addWidget(self.xuatlophoc, 1, 0, 1, 1)
        self.tablelophoc = QtWidgets.QTableView(parent=self.lophoc)
        self.tablelophoc.setObjectName("tablelophoc")
        self.gridLayout_4.addWidget(self.tablelophoc, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.lophoc)
        self.phancong = QtWidgets.QWidget()
        self.phancong.setObjectName("phancong")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.phancong)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tablephancong = QtWidgets.QTableView(parent=self.phancong)
        self.tablephancong.setObjectName("tablephancong")
        self.gridLayout_5.addWidget(self.tablephancong, 0, 0, 1, 1)
        self.xuatphancong = QtWidgets.QPushButton(parent=self.phancong)
        self.xuatphancong.setObjectName("xuatphancong")
        self.gridLayout_5.addWidget(self.xuatphancong, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.phancong)
        self.danhgia = QtWidgets.QWidget()
        self.danhgia.setObjectName("danhgia")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.danhgia)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.xuatdanhgia = QtWidgets.QPushButton(parent=self.danhgia)
        self.xuatdanhgia.setObjectName("xuatdanhgia")
        self.gridLayout_6.addWidget(self.xuatdanhgia, 1, 0, 1, 1)
        self.tabledanhgia = QtWidgets.QTableView(parent=self.danhgia)
        self.tabledanhgia.setObjectName("tabledanhgia")
        self.gridLayout_6.addWidget(self.tabledanhgia, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.danhgia)
        self.giangvien = QtWidgets.QWidget()
        self.giangvien.setObjectName("giangvien")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.giangvien)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.xuatgiangvien = QtWidgets.QPushButton(parent=self.giangvien)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.xuatgiangvien.setFont(font)
        self.xuatgiangvien.setObjectName("xuatgiangvien")
        self.gridLayout_7.addWidget(self.xuatgiangvien, 1, 0, 1, 1)
        self.tablegiangvien = QtWidgets.QTableView(parent=self.giangvien)
        self.tablegiangvien.setObjectName("tablegiangvien")
        self.gridLayout_7.addWidget(self.tablegiangvien, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.giangvien)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        self.menu_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.menu_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.giangvien_btn1.toggled['bool'].connect(self.giangvien_btn2.setChecked) # type: ignore
        self.hocphan_btn1.toggled['bool'].connect(self.hocphan_btn2.setChecked) # type: ignore
        self.lophoc_btn1.toggled['bool'].connect(self.lophoc_btn2.setChecked) # type: ignore
        self.phancong_btn1.toggled['bool'].connect(self.phancong_btn2.setChecked) # type: ignore
        self.danhgia_btn1.toggled['bool'].connect(self.danhgia_btn2.setChecked) # type: ignore
        self.giangvien_btn2.toggled['bool'].connect(self.giangvien_btn1.setChecked) # type: ignore
        self.hocphan_btn2.toggled['bool'].connect(self.hocphan_btn1.setChecked) # type: ignore
        self.lophoc_btn2.toggled['bool'].connect(self.lophoc_btn1.setChecked) # type: ignore
        self.phancong_btn2.toggled['bool'].connect(self.phancong_btn1.setChecked) # type: ignore
        self.danhgia_btn2.toggled['bool'].connect(self.danhgia_btn1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Kết nối tín hiệu clicked của các nút với stackedWidget chính
        self.giangvien_btn1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))  # Trang giangvien
        self.hocphan_btn1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # Trang hocphan
        self.lophoc_btn1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))  # Trang lophoc
        self.phancong_btn1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))  # Trang phancong
        self.danhgia_btn1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))  # Trang danhgia
        self.giangvien_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))  # Trang giangvien
        self.hocphan_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # Trang hocphan
        self.lophoc_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))  # Trang lophoc
        self.phancong_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))  # Trang phancong
        self.danhgia_btn2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))  # Trang danhgia


        self.search_input.textChanged.connect(self.search)
        self.menu_btn.click()


        # Kết nối đến cơ sở dữ liệu
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("qlgv.db")
        if not db.open():
            print("Không thể kết nối đến cơ sở dữ liệu")
            return

        # Load dữ liệu vào table views
        self.load_giangvien_data()
        self.load_hocphan_data()
        self.load_lophoc_data()
        self.load_phancong_data()
        self.load_danhgia_data()
        self.xuatgiangvien.clicked.connect(self.xuat_giangvien_excel)
        self.xuathocphan.clicked.connect(self.xuat_hocphan_excel)
        self.xuatlophoc.clicked.connect(self.xuat_lophoc_excel)
        self.xuatphancong.clicked.connect(self.xuat_phancong_excel)
        self.xuatdanhgia.clicked.connect(self.xuat_danhgia_excel)

        self.resize_table_views()

    def export_to_excel(self, table_view, file_name):
        model = table_view.model()
        if not model:
            print("Không có dữ liệu để xuất.")
            return

        df = pd.DataFrame(
            columns=[model.headerData(i, QtCore.Qt.Orientation.Horizontal) for i in range(model.columnCount())])
        for row in range(model.rowCount()):
            df.loc[row] = [model.data(model.index(row, col)) for col in range(model.columnCount())]

        try:
            df.to_excel(file_name, index=False)
            QMessageBox.information(None, "Xuất file Excel", f"Đã xuất dữ liệu thành công vào file {file_name}")
        except Exception as e:
            QMessageBox.warning(None, "Lỗi", f"Lỗi khi xuất file Excel: {e}")

    def xuat_giangvien_excel(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file Excel", "",
                                                             "Excel (*.xlsx);;All Files (*)")
        if file_name:
            self.export_to_excel(self.tablegiangvien, file_name)

    def xuat_hocphan_excel(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file Excel", "",
                                                             "Excel (*.xlsx);;All Files (*)")
        if file_name:
            self.export_to_excel(self.tablehocphan, file_name)
        # Các phương thức xuat_lophoc_excel, xuat_phancong_excel, xuat_danhgia_excel được triển khai tương tự.

    def xuat_lophoc_excel(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file Excel", "",
                                                             "Excel (*.xlsx);;All Files (*)")
        if file_name:
            self.export_to_excel(self.tablelophoc, file_name)

    def xuat_phancong_excel(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file Excel", "",
                                                             "Excel (*.xlsx);;All Files (*)")
        if file_name:
            self.export_to_excel(self.tablephancong, file_name)

    def xuat_danhgia_excel(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file Excel", "",
                                                             "Excel (*.xlsx);;All Files (*)")
        if file_name:
            self.export_to_excel(self.tabledanhgia, file_name)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_3.setText(_translate("MainWindow", "MENU"))
        self.giangvien_btn2.setText(_translate("MainWindow", "Giảng viên"))
        self.hocphan_btn2.setText(_translate("MainWindow", "Học phần"))
        self.lophoc_btn2.setText(_translate("MainWindow", "Lớp học"))
        self.phancong_btn2.setText(_translate("MainWindow", "Phân công"))
        self.danhgia_btn2.setText(_translate("MainWindow", "Đánh giá"))
        self.exit_btn_2.setText(_translate("MainWindow", "Thoát"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.label_4.setText(_translate("MainWindow", "xin chào bạn "))
        self.xuathocphan.setText(_translate("MainWindow", "Xuất excel 📋"))
        self.xuatlophoc.setText(_translate("MainWindow", "Xuất excel 📋"))
        self.xuatphancong.setText(_translate("MainWindow", "Xuất excel 📋"))
        self.xuatdanhgia.setText(_translate("MainWindow", "Xuất excel 📋"))
        self.xuatgiangvien.setText(_translate("MainWindow", "Xuất excel 📋"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = baocao()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

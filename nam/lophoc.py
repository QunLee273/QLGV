# Form implementation generated from reading ui file 'lophoc.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import sqlite3
import subprocess
import sys
from tkinter import messagebox

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_lophoc(object):
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
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.page_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=self.page_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.page_6)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.page_8)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1021, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.stackedWidget_2.addWidget(self.page_8)
        self.gridLayout_7.addWidget(self.stackedWidget_2, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.page_6)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_7.addWidget(self.widget_2, 2, 0, 1, 1)
        self.btn_xuat = QtWidgets.QPushButton(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_xuat.setFont(font)
        self.btn_xuat.setObjectName("btn_xuat")
        self.gridLayout_7.addWidget(self.btn_xuat, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.page_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(0)
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

        MainWindow.showMaximized()

        self.search_input.textChanged.connect(self.search_database)
        self.btn_xuat.clicked.connect(self.export_table_to_excel)
        self.insert_data()

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
        self.label_4.setText(_translate("MainWindow", "Home Page"))
        self.label_5.setText(_translate("MainWindow", "Dashboard Page"))
        self.label_6.setText(_translate("MainWindow", "Orders Page"))
        self.label_7.setText(_translate("MainWindow", "Product Page"))
        self.label_8.setText(_translate("MainWindow", "Customers Page"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã sinh viên"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngày sinh"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Địa chỉ "))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Số điện thoại"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Tên lớp"))
        self.btn_xuat.setText(_translate("MainWindow", "Xuất file excel"))
        self.label_10.setText(_translate("MainWindow", "User Page"))
    def insert_data(self):
        try:
            connection = sqlite3.connect("qlgv.db")
            cursor = connection.cursor()
            sqlquery = """SELECT sv.MaSV, sv.HoTen, sv.NgaySinh, sv.GioiTinh, sv.DiaChi, sv.Email, sv.SoDienThoai, l.TenLop
                            FROM SinhVien sv
                            JOIN Lop l ON sv.MaLop = l.MaLop"""

            cursor.execute(sqlquery)
            rows = cursor.fetchall()
            col_count = len(cursor.description)

            self.tableWidget.setColumnCount(col_count)
            self.tableWidget.setRowCount(len(rows))

            for tablerow, row in enumerate(rows):
                for col in range(col_count):
                    self.tableWidget.setItem(tablerow, col, QtWidgets.QTableWidgetItem(str(row[col])))

            self.tableWidget.resizeColumnsToContents()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if connection:
                connection.close()

    def export_table_to_excel(self):
        subprocess.Popen(["python", "xuathocphan.py"])
        messagebox.showinfo("Thông báo", "Đã xuất file thành công")

    def search_database(self):
        search_text = self.search_input.text()

        conn = sqlite3.connect('qlgv.db')
        cursor = conn.cursor()
        query = "SELECT HoTen,NgaySinh,GioiTinh,DiaChi,Email,SoDienThoai FROM giangvien WHERE HoTen LIKE ?"
        cursor.execute(query, ('%' + search_text + '%',))
        results = cursor.fetchall()
        conn.close()

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

def main():
    app = QtWidgets.QApplication(sys.argv)


    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1121, 859)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(102, 255, 255); color: rgb(0, 0, 0);")  # Set background and text color
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(380, 0, 731, 851))
        self.tableWidget.setStyleSheet("background-color: rgb(165, 227, 255); color: rgb(0, 0, 0);")  # Set background and text color for table
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Set fullscreen mode
        Dialog.showFullScreen()

        self.loaddata()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Đăng nhập"))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "tên"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ngày sinh"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "giới tính"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "địa chỉ"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "số điện thoại"))

    def loaddata(self):
        connection = sqlite3.connect("test1.db")
        cursor = connection.cursor()
        sqlquery = "select * from Giangvien LIMIT 50"

        self.tableWidget.setRowCount(20)
        tablerow = 0

        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[6]))

            tablerow += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'askfor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 1101, 691))
        self.frame.setStyleSheet("border:none;     \n"
"border: 2px solid rgb(255, 255, 255);   /* 添加2px的白色框 */\n"
"width: 100px;    \n"
"height: 30px;     \n"
"\n"
"background-color: rgb(52, 52, 52);  \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 100, 71, 31))
        self.label.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"border-color:rgb(52, 52, 52);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 161, 31))
        self.lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px;\n"
"color:rgb(186,186,186);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 171, 41))
        self.label_4.setStyleSheet("font: 20pt \"微软雅黑\";\n"
"border-color:rgb(52, 52, 52)")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(1030, 10, 31, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 20pt \"微软雅黑\";\n"
"    \n"
"    background-color:  rgb(52, 52, 52);\n"
"    color: rgb(255, 255, 255);\n"
"    border-color: rgb(52, 52, 52);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    font: 20pt \"微软雅黑\";\n"
"    \n"
"    background-color:  rgb(52, 52, 52);\n"
"    color: rgb(255, 255, 255);\n"
"    border-color: rgb(52, 52, 52);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(330, 50, 751, 621))
        self.tableView.setStyleSheet("")
        self.tableView.setObjectName("tableView")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 550, 111, 41))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    font: 20pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 550, 111, 41))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    font: 20pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 71, 31))
        self.label_2.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"border-color:rgb(52, 52, 52);")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 71, 31))
        self.label_5.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"border-color:rgb(52, 52, 52);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 71, 31))
        self.label_6.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"border-color:rgb(52, 52, 52);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 71, 31))
        self.label_7.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"border-color:rgb(52, 52, 52);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 300, 71, 31))
        self.label_8.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"border-color:rgb(52, 52, 52);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 140, 161, 31))
        self.lineEdit_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px;\n"
"color:rgb(186,186,186);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 180, 161, 31))
        self.lineEdit_3.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px;\n"
"color:rgb(186,186,186);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 220, 161, 31))
        self.lineEdit_4.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px;\n"
"color:rgb(186,186,186);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 260, 161, 31))
        self.lineEdit_5.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px;\n"
"color:rgb(186,186,186);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 300, 161, 31))
        self.lineEdit_6.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px;\n"
"color:rgb(186,186,186);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 500, 111, 41))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    font: 20pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 500, 111, 41))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    font: 20pt \"微软雅黑\";\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(0,0,0);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aaff;\">请假编号</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">请假信息</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "－"))
        self.pushButton_3.setText(_translate("MainWindow", "×"))
        self.pushButton_4.setText(_translate("MainWindow", "修改"))
        self.pushButton_5.setText(_translate("MainWindow", "删除"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aaff;\">员工编号</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bababa;\">请假日期</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bababa;\">请假理由</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bababa;\">申请日期</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bababa;\">是否批准</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "查询"))
        self.pushButton_7.setText(_translate("MainWindow", "添加"))

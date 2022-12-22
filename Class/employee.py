import pymysql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.employee import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from Class import depart
from database import connect_login

class Employee_Window(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        self.depart_win = depart.Department_Window()
        super(Employee_Window,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(self.close)
        self.hidden_button.clicked.connect(self.showMinimized)
        # 设置表格
        self.model = QStandardItemModel(200,2)
        self.model.setHorizontalHeaderLabels(['员工编号', '员工名称', '所属系'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
        self.lines = 0
        # 数据库连接
        self.Mysql = connect_login.MysqlOp()
        # 查询
        self.queryE.clicked.connect(self.Query_em)
        # 插入
        self.addE.clicked.connect(self.Add_em)
        # 删除
        self.remv.clicked.connect(self.Del_em)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def Query_em(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        employee_no, employee_name = self.Eno.text(), self.Ename.text()
        id_card, phone_no = self.IDcard.text(), self.phone.text()
        depart_no = self.Dno.text()
        if not employee_no or not employee_name or not id_card or not phone_no or not depart_no:
            QMessageBox.information(self, '提示', f'⚠ 存在某一必填项为空请再次检查！')
            return
        sql = 'select emp_number, empname, dep_number from information where dep_number = {0} and empname = "{1}" and emp_number = {2}'\
            .format(int(depart_no), employee_name, int(employee_no))
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            if res:
                QMessageBox.information(self, '提示', f'查询有此人名字为{employee_name}')
                # print(res)
                item1, item2, item3 = QStandardItem(str(res[0][0])), QStandardItem(res[0][1]), QStandardItem(str(res[0][2]))
                self.model.setItem(self.lines, 0, item1)
                self.model.setItem(self.lines, 1, item2)
                self.model.setItem(self.lines, 2, item3)
                self.lines += 1
                self.Mysql.conn_employ.commit()
                cursor.close()
        except pymysql.Error as e:
            print(e)
            return

    def Add_em(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        employee_no, employee_name = self.Eno.text(), self.Ename.text()
        id_card, phone_no = self.IDcard.text(), self.phone.text()
        depart_no = self.Dno.text()
        if not employee_no or not employee_name or not id_card or not phone_no or not depart_no:
            QMessageBox.information(self, '提示', f'⚠ 存在某一必填项为空请再次检查！')
            return
        sql = 'insert into information(emp_number, empname, emp_card, emp_phone, dep_number) values({0}, "{1}", "{2}", "{3}", {4})'\
            .format(int(employee_no), employee_name, id_card, phone_no, int(depart_no))
        try:
            cursor.execute(sql)
            QMessageBox.information(self, '提示', f'插入成功')
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 存在相同主键')
            return

        item1, item2, item3 = QStandardItem(str(employee_no)), QStandardItem(employee_name), QStandardItem(str(depart_no))
        self.model.setItem(self.lines, 0, item1)
        self.model.setItem(self.lines, 1, item2)
        self.model.setItem(self.lines, 2, item3)
        self.lines += 1
        self.Mysql.conn_employ.commit()
        cursor.close()

    def Del_em(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        employee_no, employee_name = self.Eno.text(), self.Ename.text()
        id_card, phone_no = self.IDcard.text(), self.phone.text()
        depart_no = self.Dno.text()
        if not employee_no or not employee_name or not id_card or not phone_no or not depart_no:
            QMessageBox.information(self, '提示', f'⚠ 存在某一必填项为空请再次检查！')
            return
        sql = 'delete from information where emp_number = {0} and empname = "{1}"'.format(int(employee_no), employee_name)
        try:
            cursor.execute(sql)
            QMessageBox.information(self, '提示', f'删除成功')
            item1, item2, item3 = QStandardItem(str(employee_no)), QStandardItem(employee_name), QStandardItem(str(depart_no))
            self.model.setItem(self.lines, 0, item1)
            self.model.setItem(self.lines, 1, item2)
            self.model.setItem(self.lines, 2, item3)
            self.lines += 1
            self.Mysql.conn_employ.commit()
            cursor.close()
        except pymysql.Error as e:
            QMessageBox.information(self, '提示', f'⚠ 不存在对应员工')
            print(e)
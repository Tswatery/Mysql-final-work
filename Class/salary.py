import pymysql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.employee import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from Class import depart
from database import connect_login
from src.salary import *

class Salary_Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Salary_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.button_close.clicked.connect(self.close)
        self.button_hidden.clicked.connect(self.showMinimized)
        # 设置表格
        self.model = QStandardItemModel(200,3)
        self.model.setHorizontalHeaderLabels(['姓名', '基本工资', '奖金'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
        self.lines = 0
        # 数据库连接
        self.Mysql = connect_login.MysqlOp()
        # 查询
        self.Query.clicked.connect(self.query_salary)
        self.Add.clicked.connect(self.add_salary)

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

    def query_salary(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        month, eno = self.month.text(), self.eno.text()
        if not month or not eno:
            QMessageBox.information(self, '提示', f'存在必填项为空')
            return
        sql = 'select pay_number, pay_prize from salary where pay_month = {0} and emp_number = {1}'.format(int(month), int(eno))
        try:
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
            return
        res = cursor.fetchall()
        sql = 'select empname from information where emp_number = {}'.format(int(eno))
        try:
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
            return
        cnt = cursor.fetchall()
        if cnt and res:
            item_name = QStandardItem(cnt[0][0])
            item_salary = QStandardItem(str(res[0][0]))
            item_price = QStandardItem(str(res[0][1]))
            self.model.setItem(self.lines, 0, item_name)
            self.model.setItem(self.lines, 1, item_salary)
            self.model.setItem(self.lines, 2, item_price)
            self.lines += 1
            self.Mysql.conn_employ.commit()
            cursor.close()
        else:
            QMessageBox.information(self, '提示', f'⚠ 编号为{eno}的员工不存在{month}月份的工资')

    def add_salary(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        month, eno = self.month.text(), self.eno.text()
        if not month or not eno:
            QMessageBox.information(self, '提示', f'存在必填项为空')
            return
        base = self.base_salary.text()
        price = self.money_give.text()
        overtime = self.jiaban.text()
        pay_money = self.kouchu.text()

        base = int(base) if base else 0
        price = int(price) if price else 0
        overtime = int(overtime) if overtime else 0
        pay_money = int(pay_money) if pay_money else 0

        sql = 'insert into salary values({0},{1},{2},{3},{4},{5},{6})'.format(float(month), int(eno), base, price, overtime, 0, pay_money)
        try:
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
            return
        self.Mysql.conn_employ.commit()
        sql = 'select empname from information where emp_number = {0}'.format(int(eno))
        try:
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
            return
        cnt = cursor.fetchall()
        if cnt:
            item_name = QStandardItem(cnt[0][0])
            item_salary = QStandardItem(str(base))
            item_price = QStandardItem(str(price))
            self.model.setItem(self.lines, 0, item_name)
            self.model.setItem(self.lines, 1, item_salary)
            self.model.setItem(self.lines, 2, item_price)
            self.lines += 1
            self.Mysql.conn_employ.commit()
            cursor.close()
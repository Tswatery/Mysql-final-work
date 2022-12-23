import pymysql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.attendance import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from database import connect_login
from Class import choose


class Attendance_Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Attendance_Window,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(self.close)
        self.hidden_button.clicked.connect(self.showMinimized)
        # 数据库连接
        self.Mysql = connect_login.MysqlOp()
        # 图表
        self.model = QStandardItemModel(200,2)
        self.model.setHorizontalHeaderLabels(['员工名称', '出勤次数', '缺勤次数'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
        self.lines = 0
        # 查询
        self.Query.clicked.connect(self.Query_att)
        # 添加
        self.Add.clicked.connect(self.Add_att)
        # 删除
        self.rmv.clicked.connect(self.Del_att)


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

    def Query_att(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        month, employee_no = self.Month.text(), self.Eno.text()
        if not month or not employee_no:
            QMessageBox.information(self, '提示', f'⚠ 存在某一必填项为空请再次检查！')
            return
        sql = 'select att_number, abs_number from attendance where att_month = {0} and emp_number = {1}'.format(int(month), int(employee_no))
        try:
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该员工在{month}的出勤')
            return
        cnt = cursor.fetchall()
        sql = 'select empname from information where emp_number = {0}'.format(int(employee_no))
        try:
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该员工')
            return
        res = cursor.fetchall()
        print(cnt, res)
        if cnt and res:
            item_att_number, item_abs_number = QStandardItem(str(cnt[0][0])), QStandardItem(str(cnt[0][1]))
            item_name = QStandardItem(res[0][0])
            self.model.setItem(self.lines, 0, item_name)
            self.model.setItem(self.lines, 1, item_att_number)
            self.model.setItem(self.lines, 2, item_abs_number)
            self.lines += 1
            self.Mysql.conn_employ.commit()
            cursor.close()
        else:
            QMessageBox.information(self, '提示', f'⚠ 不存在该员工')
            return

    def Add_att(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        month, employee_no = self.Month.text(), self.Eno.text()
        att_number, leave_number, abs_number, late_number = self.attendace_cnt.text(), self.askfor_cnt.text(), self.notin_cnt.text(), self.late_cnt.text()
        if not month or not employee_no:
            QMessageBox.information(self, '提示', f'⚠ 存在某一必填项为空请再次检查！')
            return

        att_number = 0 if not att_number else att_number
        leave_number = 0 if not leave_number else leave_number
        abs_number = 0 if not abs_number else abs_number
        late_number = 0 if not late_number else late_number

        sql = 'insert into attendance values ({0}, {1}, 0, 0, 0, 0)'.format(int(month), int(employee_no))
        try:
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该员工！')
            return

        try:
            sql = 'select empname from information where emp_number = {0}'.format(int(employee_no))
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
            return
        res = cursor.fetchall()
        item_name, item_att_number, item_abs_number = QStandardItem(res[0][0]), QStandardItem(str(att_number)), QStandardItem(str(abs_number))
        self.model.setItem(self.lines, 0, item_name)
        self.model.setItem(self.lines, 1, item_att_number)
        self.model.setItem(self.lines, 2, item_abs_number)
        self.lines += 1
        self.Mysql.conn_employ.commit()
        cursor.close()

    def Del_att(self):
        self.Mysql.get_connect_employ()
        cursor = self.Mysql.conn_employ.cursor()
        month, employee_no = self.Month.text(), self.Eno.text()
        try:
            sql = 'select att_number, abs_number from attendance where att_month = {0} and emp_number = {1}'.format(int(month),int(employee_no))
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
            return
        res = cursor.fetchall()

        try:
            sql = 'delete from attendance where att_month = {0} and emp_number = {1}'.format(int(month), int(employee_no))
            cursor.execute(sql)
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
        sql = 'select empname from information where emp_number = {0}'.format(int(employee_no))
        cursor.execute(sql)
        cnt = cursor.fetchall()
        if res and cnt:
            item_name = QStandardItem(cnt[0][0])
            item_att_number, item_abs_number = QStandardItem(str(res[0][0])), QStandardItem(str(res[0][1]))
            self.model.setItem(self.lines, 0, item_name)
            self.model.setItem(self.lines, 1, item_att_number)
            self.model.setItem(self.lines, 2, item_abs_number)
            self.lines += 1
            self.Mysql.conn_employ.commit()
            cursor.close()
        else:
            QMessageBox.information(self, '提示', f'⚠ 不存在该编号的员工')
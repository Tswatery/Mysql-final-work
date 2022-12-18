import pymysql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.department import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from Class import choose
from database import connect_login

class Department_Window(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Department_Window,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(self.close)
        self.hidden_button.clicked.connect(self.showMinimized)
        # 查询
        self.query.clicked.connect(self.Query_depart)
        # 添加
        self.add.clicked.connect(self.Add_depart)
        # 删除
        self.remv.clicked.connect(self.Del_depart)
        # 设置表格
        self.model = QStandardItemModel(200,2)
        self.model.setHorizontalHeaderLabels(['系编号', '系名称'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
        self.lines = 0
        # 数据库连接
        self.Mysql = connect_login.MysqlOp()

    # 移动
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

    # 一些相关的操作

    def Query_depart(self):
        self.Mysql.get_connect_employ()
        departno, departname = int(self.departno.text()), self.departname.text()
        # 这是测试语句
        print(f'部门查询中，departno为{departno}, 类型为{type(departno)}, departname为{departname}')
        cursor = self.Mysql.conn_employ.cursor()
        sql = 'select * from department where dep_number = %s and dep_name = %s'
        cursor.execute(sql, (departno, departname))
        res = cursor.fetchall()
        # print(res)
        if res:
            QMessageBox.information(self, '提示', f'存在名称为{departname}，编号为{departno}的部门')
            print(res)
            item1, item2 = QStandardItem(str(res[0][0])), QStandardItem(res[0][1]) # 注意这个是元组里面套元组
            self.model.setItem(self.lines, 0, item1)
            self.model.setItem(self.lines, 1, item2)
            self.lines += 1
        else:
            QMessageBox.information(self, '提示', f'⚠ 不存在名称为{departname}，编号为{departno}的部门')

        self.Mysql.conn_employ.commit()
        cursor.close()

    def Add_depart(self):
        self.Mysql.get_connect_employ()
        departno, departname = int(self.departno.text()), self.departname.text()
        print(f'增加部门中，departno为{departno}, 类型为{type(departno)}, departname为{departname}')
        cursor = self.Mysql.conn_employ.cursor()
        sql = 'insert into department values (%s, %s)'
        try:
           cursor.execute(sql, (departno, departname))
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'添加失败 存在编号为{departno}，名称为{departname}的部门重复添加')
            return

        QMessageBox.information(self, '提示', f'添加完成 编号为{departno}，名称为{departname}')
        item1, item2 = QStandardItem(str(departno)), QStandardItem(departname)  # 注意这个是元组里面套元组
        self.model.setItem(self.lines, 0, item1)
        self.model.setItem(self.lines, 1, item2)
        self.lines += 1
        self.Mysql.conn_employ.commit()
        cursor.close()

    def Del_depart(self):
        self.Mysql.get_connect_employ()
        departno, departname = int(self.departno.text()), self.departname.text()
        print(f'删除部门中，departno为{departno}, 类型为{type(departno)}, departname为{departname}')
        cursor = self.Mysql.conn_employ.cursor()
        sql = 'delete from department where dep_name = %s and dep_number = %s'
        try:
            cursor.execute(sql, (departno, departname))
        except pymysql.Error as e:
            print(e)
            QMessageBox.information(self, '提示', f'删除失败 不存编号为{departno}，名称为{departname}的部门')
            return
        QMessageBox.information(self, '提示', f'删除成功 编号为{departno}，名称为{departname}')
        item1, item2 = QStandardItem(str(departno)), QStandardItem(departname)  # 注意这个是元组里面套元组
        self.model.setItem(self.lines, 0, item1)
        self.model.setItem(self.lines, 1, item2)
        self.lines += 1

        self.Mysql.conn_employ.commit()
        cursor.close()

    def Update_depart(self):
        pass
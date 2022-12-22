from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.choose2 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from Class import depart, employee

class ChooseWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        # 部门表
        self.depart_win = depart.Department_Window()
        # 员工表
        self.employee_win = employee.Employee_Window()
        super(ChooseWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(self.close)
        self.hidden_button.clicked.connect(self.showMinimized)
        # 部门表
        self.depart.clicked.connect(self.depart_win.show) # 点击部门表后显示部门表的样子
        self.depart.clicked.connect(self.close)#自身要关闭
        self.depart_win.close_button.clicked.connect(self.show) # 部门表关闭后要返回原来的表
        # 员工表
        self.employee.clicked.connect(self.employee_win.show)
        self.employee.clicked.connect(self.close)
        self.employee_win.close_button.clicked.connect(self.show)

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


from database import connect_login
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.login import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from Class import choose

class MainWindows(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindows,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.button_close.clicked.connect(self.close)
        self.button_hidden.clicked.connect(self.showMinimized)
        self.choose_win = choose.ChooseWindow()
        self.button_login.clicked.connect(self.is_login)
        self.choose_win.close_button.clicked.connect(self.show)

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

    def is_login(self):
        Mysql = connect_login.MysqlOp()
        Mysql.get_connect()
        user_info = Mysql.get_userinfo()
        name, pwd = self.user_lineEdit.text(), self.password_lineEdit.text()
        # 测试name和pwd是否成功读入
        print(f'name是{name}，pwd是{pwd}')
        flag_login_success = False
        for k, v in user_info:
            if k == name and v == pwd:  # 如果正确的话显示
                print('正确')
                self.choose_win.show()
                self.close()
                flag_login_success = True
                break
        if not flag_login_success:
            QMessageBox.information(self, '提示', '用户密码错误')
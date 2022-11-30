import sys
from src.login import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from database import connect_login
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src import add

class main(add.Ui_adduser, QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_pushButton.clicked.connect(self.close)
        self.hidden_pushButton.clicked.connect(self.showMinimized)

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


class MainWindows(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindows,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #按钮
        self.close_pushButton.clicked.connect(self.close)
        self.hidden_pushButton.clicked.connect(self.showMinimized)
        self.main = main()



    #窗口拖动
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
        for k, v in user_info:
            if k == name and v == pwd:  # 如果正确的话显示
                self.main.show()
                self.close()
                return
        QMessageBox.information(self, '提示', '用户密码错误')

if __name__=="__main__":
    app = QApplication(sys.argv)
    mywin = MainWindows()
    mywin.show()
    mywin.login_pushButton.clicked.connect(mywin.is_login)
    mywin.main.pushButton_2.clicked.connect(mywin.show)
    mywin.main.pushButton_2.clicked.connect(mywin.main.close)

    sys.exit(app.exec_())
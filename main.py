
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src import add, login
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from database import connect_login


class main(add.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)

class login(login.Ui_Form, QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        self.main = main()

    def is_login(self):
        Mysql = connect_login.MysqlOp()
        Mysql.get_connect()
        user_info = Mysql.get_userinfo()
        name, pwd = self.lineEdit.text(), self.lineEdit_2.text()
        for k, v in user_info:
            if k == name and v == pwd:  # 如果正确的话显示
                self.main.show()
                self.close()
                return
        QMessageBox.information(self, '提示', '用户密码错误')

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    login_window = login()
    login_window.main = main()
    login_window.show()

    Mysqltest = connect_login.MysqlOp()

    login_window.pushButton.clicked.connect(login_window.is_login) # 这个地方有问题 如果正确才显示 否则就不显示
    # login_window.pushButton.clicked.connect(main_window.show)
    # login_window.pushButton.clicked.connect(login_window.close)
    login_window.main.pushButton_2.clicked.connect(login_window.show)
    login_window.main.pushButton_2.clicked.connect(login_window.main.close)
    sys.exit(app.exec_())
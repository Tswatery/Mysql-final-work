from database import connect_login
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.login import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from src import askfor

class test_window(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(test_window,self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(self.close)
        self.hidden_button.clicked.connect(self.showMinimized)

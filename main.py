import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from database import connect_login
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Class import login

if __name__=="__main__":
    app = QApplication(sys.argv)
    mywin = login.MainWindows()
    mywin.show()

    sys.exit(app.exec_())
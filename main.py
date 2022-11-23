import login
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    UI = login.Ui_Dialog()
    UI.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
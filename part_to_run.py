import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from NetPanelAnalysis_V1_1 import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    # 窗口关闭时的二次确认消息窗体
    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.question(self,'Message',"Are you sure to quit?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
import win32gui
import os
import sys
from PySide2.QtGui import QWindow
from PySide2.QtWidgets import *


class MyFrame(MainFrame):
    def __init__(self, parent=None):
        super(MainFrame, self).__init__();
        calc_hnd = win32gui.FindWindow(None, u"计算器")
        calc_win = QWindow.fromWinId(calc_hnd)
        print(calc_hnd)
        self.layout = QVBoxLayout()
        self.button = QPushButton("please push me!")
        self.calc_wdgt = QWidget.createWindowContainer(calc_win)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.calc_wdgt)
        self.title = "test"

        self.setLayout(self.layout)
        self.setMinimumSize(800, 600)
        self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MyFrame()
    frame.show()
    sys.exit(app.exec_())

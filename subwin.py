import subprocess
import sys
import threading
import time

import win32con
import win32gui
from PySide2.QtCore import QProcess
from PySide2.QtCore import Qt
from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QMdiArea
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.p = QProcess()
        self.layout = QVBoxLayout()
        self.mdi = QMdiArea()
        self.widget = QWidget()
        self.initUI()

    def initUI(self):
        t = threading.Thread(target=self.runExe)
        t.start()

        time.sleep(2)
        # start = time.time()
        # while calc_hnd == 0:
        #     time.sleep(500)
        #     calc_hnd = win32gui.FindWindow(None, u"计算器")
        #     print(calc_hnd)
        #     end = time.time()
        #     if end - start > 5000:
        #         return

        self.setWindowTitle("测试")

        self.calc_hnd = win32gui.FindWindow(None, u"计算器")
        win32gui.SetWindowLong(self.calc_hnd, win32con.GWL_STYLE, win32con.GW_CHILD | win32con.WS_VISIBLE)

        self.calc_win = QWindow.fromWinId(self.calc_hnd)
        # self.calc_win.setWindowFlags(self.calc_win.flags() | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        # self.calc_win.setGeometry(0, 0, 640, 480)
        self.calc_wdgt = self.createWindowContainer(self.calc_win)
        self.calc_wdgt.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setCentralWidget(self.calc_wdgt)

        # 设置窗口的父子关系
        # self.calc_win.setParent(self.winId())
        # win32gui.SetParent(self.calc_hnd, self)
        # win32gui.SetParent(self.calc_wdgt, self.widget)
        self.calc_wdgt.setParent(self)
        self.setGeometry(0, 0, 640, 480)
        # self.show()

        self.show()

    @staticmethod
    def runExe():
        exePath = "C:\\Windows\\system32\\calc.exe"
        subprocess.Popen(exePath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

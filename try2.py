import sys
import subprocess
import time
import win32api, win32con, win32gui
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import QWindow
from PySide2.QtCore import Qt
from des_20190620 import Ui_MainWindow


class TestFrame(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def on_start_connect_click(self):
        subprocess.Popen("mspaint.exe")
        time.sleep(2)
        self.calc_hwnd = win32gui.FindWindow(None, "无标题 - 画图")
        self.calc_win = QWindow.fromWinId(self.calc_hwnd)
        # self.calc_win.setFlags(self.calc_win.flags() | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximized)
        print(self.calc_win)

    def on_show_connect_click(self):
        win32gui.ShowWindow(self.calc_hwnd, win32con.SW_SHOW)

    def on_hidden_conncet_click(self):
        win32gui.ShowWindow(self.calc_hwnd, win32con.SW_HIDE)

    def on_close_connect_click(self):
        win32gui.CloseWindow(self.calc_hwnd)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = TestFrame()
    test.ui.pushButton.clicked.connect(test.on_start_connect_click)
    test.ui.pushButton_2.clicked.connect(test.on_show_connect_click)
    test.ui.pushButton_3.clicked.connect(test.on_hidden_conncet_click)
    test.ui.pushButton_4.clicked.connect(test.on_close_connect_click)
    test.show()
    sys.exit(app.exec_())

import sys
import subprocess
import time
import win32api, win32con, win32gui
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QWindow
from PySide2.QtCore import Qt
from des_20190620 import Ui_MainWindow


def on_pushButton_connect_click(self):
    subprocess.Popen("mspaint.exe")
    time.sleep(2)
    calc_hwnd = win32gui.FindWindow(None, "无标题 - 画图")
    calc_win = QWindow.fromWinId(calc_hwnd)
    calc_win.setFlags(Qt.WindowTitleHint)
    calc_wdgt =
    print(calc_win)


class TestFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = TestFrame()
    test.ui.pushButton.clicked.connect(on_pushButton_connect_click)
    test.show()
    sys.exit(app.exec_())

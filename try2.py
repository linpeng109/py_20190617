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
        subprocess.Popen("D:/Program Files/GEOVIA/Surpac/69_x64/x64/bin/surpac2.exe ")
        time.sleep(60)
        self.calc_hwnd = win32gui.FindWindow(None, "GEOVIA Surpac 6.9 (x64) - D:/Workspace/py_20190617 (Profile:)")
        self.calc_win = QWindow.fromWinId(self.calc_hwnd)
        # self.calc_win.setFlags(self.calc_win.flags() | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximized)
        print(self.calc_win)

    def on_show_connect_click(self):
        win32gui.ShowWindow(self.calc_hwnd, win32con.SW_SHOW)

    def on_hidden_conncet_click(self):
        win32gui.ShowWindow(self.calc_hwnd, win32con.SW_HIDE)

    def on_close_connect_click(self):
        win32gui.PostMessage(self.calc_hwnd, win32con.WM_CLOSE)

    def on_get_connect_click(self):
        ISTYLE = win32gui.GetWindowLong(self.calc_hwnd, win32con.GWL_STYLE)
        win32gui.SetWindowLong(self.calc_hwnd, win32con.GWL_STYLE, ISTYLE & ~win32con.GW_CHILD)
        win32gui.SetWindowPos(self.calc_hwnd, None, 0, 0, 600, 400,
                              win32con.SWP_NOSIZE |
                              win32con.SWP_NOMOVE |
                              win32con.SWP_NOACTIVATE |
                              win32con.SWP_FRAMECHANGED)
        RESULT = win32gui.SetParent(self.calc_hwnd, self.winId())

        print(RESULT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = TestFrame()
    test.ui.pushButton.clicked.connect(test.on_start_connect_click)
    test.ui.pushButton_2.clicked.connect(test.on_show_connect_click)
    test.ui.pushButton_3.clicked.connect(test.on_hidden_conncet_click)
    test.ui.pushButton_4.clicked.connect(test.on_close_connect_click)
    test.ui.pushButton_5.clicked.connect(test.on_get_connect_click)
    test.show()
    sys.exit(app.exec_())

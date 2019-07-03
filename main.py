import subprocess
import sys
import time

import win32con
import win32gui
from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QApplication, QMainWindow

from MainFrame import Ui_MainWindow


class TestFrame(QMainWindow):
    calc_hwnd = 0

    calc_win = 0

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def on_start_connect_click(self):
        subprocess.Popen("C:/Program Files (x86)/GEOVIA/Surpac/69/nt_i386/bin/surpac2.exe")
        # subprocess.Popen("C:/Program Files/Microsoft Office/Office15/WINWORD.EXE")
        time.sleep(50)
        self.calc_hwnd = win32gui.FindWindow(None, "GEOVIA Surpac 6.9 - D:/Workspace/py_20190617 (Profile:)")
        # self.calc_hwnd = win32gui.FindWindow("NetUIHWND", None)
        print(self.calc_hwnd)
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
        print(self.calc_hwnd)
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
    test.ui.startSurpacBtn.clicked.connect(test.on_start_connect_click)
    # test.ui.showBtn.clicked.connect(test.on_show_connect_click)
    # test.ui.hiddenBtn.clicked.connect(test.on_hidden_conncet_click)
    # test.ui.closeAppBtn.clicked.connect(test.on_close_connect_click)
    # test.ui.stopBtn.clicked.connect(test.on_close_connect_click())
    test.ui.getWindowFormHwndBtn.clicked.connect(test.on_get_connect_click)
    test.show()
    sys.exit(app.exec_())

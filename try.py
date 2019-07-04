import os
import signal
import subprocess
import sys
import time

import win32con
import win32gui
import win32api
import win32process
from PySide2.QtWidgets import QApplication, QMainWindow

from MainFrame import Ui_MainWindow


def startProcess():
    cmd = "C:/Program Files (x86)/GEOVIA/Surpac/69/nt_i386/bin/surpac2.exe"
    pid = subprocess.Popen(cmd).pid
    return pid


def getHwndFromPid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                print(win32gui.GetWindowText(hwnd))
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def getPidsFromPName(pname):
    _result = subprocess.Popen("tasklist|findstr " + pname, shell=True, stdout=subprocess.PIPE)
    _lines = _result.stdout.readlines()
    pidList = []
    for pid in _lines:
        begin = str(pid).index('surpac2.exe') + 11
        end = str(pid).index('Console')
        pidList.append(str(pid)[begin:end].strip())
    return pidList


def on_show_connect_click(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)


def on_hidden_conncet_click(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)


def on_close_connect_click(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE)


def on_move_connect_click(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 100, 100, 600, 400, win32con.SWP_SHOWWINDOW)


def killProcess(pids):
    for pid in pids:
        _pid = int(pid)
        try:
            os.kill(_pid, signal.SIGTERM)
            print('Process(pid=%s) has be killed' % pid)
        except OSError:
            print('no such process(pid=%s)' % pid)


if __name__ == "__main__":
    # Kill all processes that named surpac
    pids = getPidsFromPName("surpac2")
    print("pidList=%s" % pids)
    killProcess(pids)

    # Startup surpac process
    pid = startProcess()
    print("pid=%s" % pid)

    # Get window's handler,but must wait a moment!
    hwnds = []
    while True:
        hwnds = getHwndFromPid(pid)
        print("hwnds.len=%s" % len(hwnds))
        if (len(hwnds) > 0):
            title = win32gui.GetWindowText(hwnds[0])
            if ("Surpac" in title):
                break
        time.sleep(1)
    # print("hwnd=%s" % hwnds[0])

    # hwnd2 = win32gui.FindWindow(None, "GEOVIA Surpac 6.9 - D:/Workspace/py_20190617 (Profile:)")
    # print("hwnd2=%s" % hwnd2)

    # Open main window
    app = QApplication()
    mainWindow = QMainWindow()
    mainFrame = Ui_MainWindow()
    mainFrame.setupUi(mainWindow)
    # mainFrame.SetSurpacWindowHideBtn.clicked.connect(on_hidden_conncet_click(hwnds[0]))
    # mainFrame.SetSurpac2WindowShowBtn.clicked.connect(on_show_connect_click(hwnds[0]))
    # pids = []
    # pids.append(pid)
    # mainFrame.KillSurpac2Btn.clicked.connect(killProcess(pids))
    mainWindow.showMaximized()

    # 隐含窗口标题栏win32con.GW_CHILD &
    ISTYLE = win32gui.GetWindowLong(hwnds[0], win32con.GWL_STYLE)
    win32gui.SetWindowLong(hwnds[0], win32con.GWL_STYLE, ISTYLE & ~win32con.WS_CAPTION)
    win32gui.SetWindowPos(hwnds[0], win32con.HWND_TOPMOST, 250, 0, 1024, 768, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
    # print(win32gui.SetForegroundWindow(hwnds[0]))
    # win32gui.SetFocus()
    # 解决子窗口获取焦点问题
    hForeWnd = win32api.GetForegroundWindow();
    dwCurID = win32process.GetCurrentThreadId();
    dwForeID = win32process.GetWindowThreadProcessId(hForeWnd, None);

    # Set surpac window as subwindows
    time.sleep(1)
    win32gui.SetParent(hwnds[0], mainWindow.winId())
    time.sleep(1)

    # exit app
    sys.exit(app.exec_())

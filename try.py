import os
import signal
import subprocess
import sys
import time

import win32con
import win32gui
import win32process
from PySide2.QtCore import QUrl
from PySide2.QtGui import QWindow
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QTreeWidgetItem

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


# 关闭列出的所有进程id号的进程
def killProcess(pids):
    for pid in pids:
        _pid = int(pid)
        try:
            os.kill(_pid, signal.SIGTERM)
            print('Process(pid=%s) has be killed' % pid)
        except OSError:
            print('no such process(pid=%s)' % pid)


def create_tab(self, webview):
    print("===================Create====================")


if __name__ == "__main__":
    # 关闭所有带有关键字surpac的进程
    pids = getPidsFromPName("surpac2")
    print("pidList=%s" % pids)
    killProcess(pids)

    # 启动surpac进程
    pid = startProcess()
    print("pid=%s" % pid)

    # 根据窗口标题关键字surpac，获取surpac主工作窗口句柄（非Logoc窗口）
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

    # 测试校验
    # hwnd2 = win32gui.FindWindow(None, "GEOVIA Surpac 6.9 - D:/Workspace/py_20190617 (Profile:)")
    # print("hwnd2=%s" % hwnd2)

    # 建立并打开主窗口
    app = QApplication(sys.argv)
    # QCoreApplication.setAttribute(Qt.AA_UseSoftwareOpenGL)
    mainWindow = QMainWindow()
    mainFrame = Ui_MainWindow()
    mainFrame.setupUi(mainWindow)
    mainWindow.setWindowTitle("中矿智信大数据集成客户端")
    mainWindow.showMaximized()

    # 显示网页tab
    webView = QWebEngineView(mainWindow)
    # webView.load(QUrl("http://www.zjky.cn/"))
    # webView.load(QUrl("http://www.sina.com.cn/"))
    webView.load(QUrl("http://localhost:8080/#/"))
    mainFrame.horizontalLayout_1.addWidget(webView)
    time.sleep(1)

    # 加入树形目录
    tree = mainFrame.treeWidget
    tree.setHeaderHidden(True)
    root = QTreeWidgetItem(tree)
    root.setText(0, '扩展命令')
    child1 = QTreeWidgetItem(root)
    child1.setText(0, '基本类')
    child11 = QTreeWidgetItem(child1)
    child11.setText(0, '清除')
    tree.addTopLevelItem(root)
    mainFrame.gridLayout.addWidget(tree, 0, 0, 1, 1)

    # 显示surpac的tab
    # 设置surpac窗口为主窗口的子窗口
    # 方法1
    # win32gui.SetParent(hwnds[0], mainWindow.winId())
    # 方法2
    native_wnd = QWindow.fromWinId(hwnds[0])
    surpacWidget = QWidget.createWindowContainer(native_wnd)
    # 方法2.1
    # mainWindow.setCentralWidget(centralWidget)
    # 方法2.2
    mainFrame.gridLayout.addWidget(surpacWidget, 0, 1, 1, 10)

    time.sleep(1)

    # 隐含窗口标题栏win32con.GW_CHILD &
    ISTYLE = win32gui.GetWindowLong(hwnds[0], win32con.GWL_STYLE)
    win32gui.SetWindowLong(hwnds[0], win32con.GWL_STYLE,
                           ISTYLE & ~win32con.WS_CAPTION & win32con.SWP_NOSIZE & win32con.SWP_NOMOVE)

    # 退出应用
    sys.exit(app.exec_())

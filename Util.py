import os
import signal
import subprocess
import time

import win32con
import win32gui
import win32process
from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QWidget


class ProcessUtil():

    # 启动执行文件返回进程pid
    def startProcess(self, cmd):
        # cmd = "C:/Program Files (x86)/GEOVIA/Surpac/69/nt_i386/bin/surpac2.exe"
        pid = subprocess.Popen(cmd).pid
        return pid

    # 从指定pid获取窗口句柄（通过回调函数）
    def getHwndFromPid(self, pid):
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

    # 从指定名称获取进程的pid数组
    def getPidsFromPName(self, pname):
        _result = subprocess.Popen("tasklist|findstr " + pname, shell=True, stdout=subprocess.PIPE)
        _lines = _result.stdout.readlines()
        pids = []
        for pid in _lines:
            begin = str(pid).index('surpac2.exe') + 11
            end = str(pid).index('Console')
            pids.append(str(pid)[begin:end].strip())
        return pids

    # 关闭列出的所有进程id号的进程
    def killProcess(self, pids):
        for pid in pids:
            _pid = int(pid)
            try:
                os.kill(_pid, signal.SIGTERM)
                print('Process(pid=%s) has be killed' % pid)
            except OSError:
                print('no such process(pid=%s)' % pid)

        # 通过pid获取包含指定窗口特征名的窗口句柄
        def GetTheMainWindow(self, pid, spTitle):
            hwnds = []
            while True:
                hwnds = self.getHwndFromPid(pid)
                if (len(hwnds) > 0):
                    _title = win32gui.GetWindowText((hwnds[0]))
                    if (spTitle in _title):
                        break
                time.sleep(1)
            return hwnds[0]


class WindowUtil():
    # 显示窗口
    def showWindow(self, hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

    # 隐含窗口
    def hiddenWindow(self, hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

    # 关闭窗口
    def closeWindow(self, hwnd):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE)

    # 设置窗口样式
    def setNoTitleWindow(self, hwnd):
        ISTYLE = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        win32gui.SetWindowLong(hwnd,
                               ISTYLE &
                               ~win32con.WS_CAPTION &
                               win32con.SWP_NOMOVE &
                               win32con.SWP_NOSIZE)

    # 将一个窗口句柄转化为一个标准Widget
    def convertWndToWidget(self, hwnd):
        native_wnd = QWindow.fromWinId(hwnd)
        return QWidget.createWindowContainer(native_wnd)

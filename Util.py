# encoding:utf-8
import datetime
import os
import signal
import socket
import subprocess
import time

import win32con
import win32gui
import win32process
from PySide2.QtCore import QUrl
from PySide2.QtGui import QWindow
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PySide2.QtWidgets import QWidget, QHBoxLayout, QTabWidget, QPushButton


class ProcessUtil:
    # 启动执行文件返回进程pid
    def startProcess(cmd):
        # cmd = "C:/Program Files (x86)/GEOVIA/Surpac/69/nt_i386/bin/surpac2.exe"
        pid = subprocess.Popen(cmd).pid
        return pid

    # 从指定pid获取窗口句柄（通过回调函数）
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

    # 从指定名称获取进程的pid数组
    def getPidsFromPName(pname):
        _result = subprocess.Popen("tasklist|findstr " + pname, shell=True, stdout=subprocess.PIPE)
        _lines = _result.stdout.readlines()
        pids = []
        for pid in _lines:
            begin = str(pid).index('surpac2.exe') + 11
            end = str(pid).index('Console')
            pids.append(str(pid)[begin:end].strip())
        return pids

    # 根据pid获取运行端口
    def getPortFromPid(pid):
        _result = subprocess.Popen("netstat -aon|findstr " + pid, shell=True, stdout=subprocess.PIPE)
        _lines = _result.stdout.readlines()
        ports = []
        for port in _lines:
            _port = str(port).replace(' ', '') \
                .replace('.', '') \
                .replace(':', '') \
                .replace("b'", '') \
                .replace("\\r\\n'", '') \
                .replace('TCP0000', '') \
                .replace(str(pid), '') \
                .replace('00000LISTENING', '')
            if len(_port) <= 10:
                ports.append(_port)
        return ports

    # 关闭列出的所有进程id号的进程
    def killProcess(pids):
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


class WindowUtil:
    # 显示窗口
    def showWindow(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

    # 隐含窗口
    def hiddenWindow(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

    # 关闭窗口
    def closeWindow(hwnd):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE)

    # 设置窗口样式
    def setNoTitleWindow(hwnd):
        ISTYLE = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        win32gui.SetWindowLong(hwnd,
                               ISTYLE &
                               ~win32con.WS_CAPTION &
                               win32con.SWP_NOMOVE &
                               win32con.SWP_NOSIZE)

    # 将一个窗口句柄转化为一个标准Widget
    def convertWndToWidget(hwnd):
        native_wnd = QWindow.fromWinId(hwnd)
        return QWidget.createWindowContainer(native_wnd)


class MyTabWidget(QTabWidget):
    def __init__(self):
        super(MyTabWidget, self).__init__()
        self.setTabsClosable(True)
        self.setDocumentMode(True)
        self.setMovable(True)
        self.tabCloseRequested.connect(self.close_Tab)
        # for i in [1, 2, 3, 4, 5]:
        #     tabItem = QWidget()
        #     layout = QHBoxLayout()
        #     layout.setSpacing(50)
        #     layout.setDirection(QHBoxLayout.LeftToRight)
        #     tabItem.setLayout(layout)
        #     for j in [1, 2, 3, 4, 5, 6]:
        #         pushBtn = QPushButton('push_' + str(i) + str(j))
        #         pushBtn.setFixedHeight(200)
        #         layout.addWidget(pushBtn)
        #     self.addTab(tabItem, '测试' + str(i))

    def create_Tab(self, widgets):
        tabItem = QWidget()
        layout = QHBoxLayout()
        layout.setSpacing(30)
        layout.setDirection(QHBoxLayout.LeftToRight)
        for widget in widgets:
            layout.addWidget(widget)
        tabItem.setLayout(layout)
        self.addTab(tabItem, '新标签')
        self.setCurrentWidget(tabItem)

    def close_Tab(self, index):
        if self.count() > 1:
            self.removeTab(index)
        else:
            self.close()


class SocketClient:

    def __init__(self, port, encode):
        self.HOST = 'localhost'
        self.BUFSIZ = 1024
        self.PORT = port
        self.ENCODE = encode
        self.ADDR = (self.HOST, port)
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpCliSock.connect(self.ADDR)

    def sendMsg(self, msg):
        self.tcpCliSock.sendall(msg.encode(self.ENCODE))
        result = self.tcpCliSock.recv(self.BUFSIZ)
        return result

    def closeSocket(self):
        self.tcpCliSock.close()


class WebEngineView(QWebEngineView):

    def __init__(self, tabWidget, parent=None):
        super(WebEngineView, self).__init__(parent)
        self.tabwidget = tabWidget
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)  # 支持视频播放
        self.page().windowCloseRequested.connect(self.on_windowCloseRequested)  # 页面关闭请求
        self.page().profile().downloadRequested.connect(self.on_downloadRequested)  # 页面下载请求

    #  支持页面关闭请求
    def on_windowCloseRequested(self):
        the_index = self.mainwindow.tabWidget.currentIndex()
        self.mainwindow.tabWidget.removeTab(the_index)

    #  支持页面下载按钮
    def on_downloadRequested(self, downloadItem):
        if downloadItem.isFinished() == False and downloadItem.state() == 0:
            # 生成文件存储地址
            the_filename = downloadItem.url().fileName()
            if len(the_filename) == 0 or "." not in the_filename:
                cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                the_filename = "下载文件" + cur_time + ".xls"
            the_sourceFile = os.path.join(os.getcwd(), the_filename)

            # 下载文件
            # downloadItem.setSavePageFormat(QWebEngineDownloadItem.CompleteHtmlSaveFormat)
            downloadItem.setPath(the_sourceFile)
            downloadItem.accept()
            downloadItem.finished.connect(self.on_downloadfinished)

    #  下载结束触发函数
    def on_downloadfinished(self):
        js_string = '''
        alert("下载成功，请到软件同目录下，查找下载文件！"); 
        '''
        self.page().runJavaScript(js_string)

    # 重载QWebEnginView的createwindow()函数
    def createWindow(self, QWebEnginePage_WebWindowType):
        print(self)
        new_webview = WebEngineView(self.tabwidget)
        self.tabwidget.create_Tab([new_webview])
        return new_webview

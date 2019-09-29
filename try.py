import os
import signal
import subprocess
import sys
import time

import win32con
import win32gui
import win32process
from PySide2.QtCore import QUrl, SIGNAL
from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QTreeWidgetItem

from MainFrame import Ui_MainWindow
from Util import WebEngineView
from socketcc import SocketClient


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
    mainWindow.setWindowTitle("奥信爆破数据集成客户端")
    mainWindow.showMaximized()

    # 显示网页tab
    # webView = QWebEngineView(mainWindow)
    webView = WebEngineView(mainWindow)
    webView.load(QUrl("http://www.sinomine.com.cn/"))
    # webView.load(QUrl("http://www.auxin-tech.com.cn/"))
    # webView.load(QUrl("http://www.zjky.cn/"))
    # webView.load(QUrl("http://www.sina.com.cn/"))
    # webView.load(QUrl("http://localhost:8080/#/"))
    # webView.load(QUrl("http://192.168.1.186:8090/"))
    tabWidget = QWidget()
    mainFrame.tabWidget.addTab(tabWidget, '新标签')
    mainFrame.tabWidget.setCurrentWidget(tabWidget)
    mainFrame.horizontalLayout_1.addWidget(webView)
    time.sleep(1)


    def onClick(self, item):
        print(item)
        socket = SocketClient(2672,'gbk')
        message = 'RCTL\n' + 'TCLSCRIPTBEGIN\n' + 'set status [ SclFunction \"EXIT GRAPHICS\" {} ]' + 'TCLSCRIPTEND\n'
        result = socket.sendMsg(message)
        print(result.decode(socket.ENCODE))
        socket.closeSocket()

        # 加入树形目录


    tree = mainFrame.treeWidget
    tree.connect(tree, SIGNAL('itemClicked(QTreeWidgetItem*, int)'), onClick)
    tree.setHeaderHidden(True)
    root = QTreeWidgetItem(tree)
    root.setText(0, '扩展命令（中矿智信）')
    child1 = QTreeWidgetItem(root)
    child1.setText(0, '露采地质')

    child11 = QTreeWidgetItem(child1)
    child11.setText(0, '创建月度炮孔数据库')
    child12 = QTreeWidgetItem(child1)
    child12.setText(0, '导入炮孔数据')
    child13 = QTreeWidgetItem(child1)
    child13.setText(0, '圈定爆堆边界')
    child14 = QTreeWidgetItem(child1)
    child14.setText(0, '圈定矿岩界线')
    child15 = QTreeWidgetItem(child1)
    child15.setText(0, '矿岩多边形算量')
    child16 = QTreeWidgetItem(child1)
    child16.setText(0, '炮孔信息处理')
    child17 = QTreeWidgetItem(child1)
    child17.setText(0, '矿岩多边形信息写入爆堆数据库')
    child18 = QTreeWidgetItem(child1)
    child18.setText(0, '当前目录矿岩多边形信息写入爆堆数据库')
    child19 = QTreeWidgetItem(child1)
    child19.setText(0, '核验爆堆数据库')
    child1a = QTreeWidgetItem(child1)
    child1a.setText(0, '数据库爆堆信息写入爆堆文件')
    child1b = QTreeWidgetItem(child1)
    child1b.setText(0, '报表统计')
    child1c = QTreeWidgetItem(child1)
    child1c.setText(0, '爆堆估值赋值')
    child1d = QTreeWidgetItem(child1)
    child1d.setText(0, '探采对比')
    child1e = QTreeWidgetItem(child1)
    child1e.setText(0, '块模型处理')
    child1f = QTreeWidgetItem(child1)
    child1f.setText(0, '在工作目录下搜索文件合并')
    child1g = QTreeWidgetItem(child1)
    child1g.setText(0, '绘制台阶潜孔取样及矿体圈定图')
    child1h = QTreeWidgetItem(child1)
    child1h.setText(0, '创建目录')
    child2 = QTreeWidgetItem(root)
    child2.setText(0, '露采测量')
    child21 = QTreeWidgetItem(child2)
    child21.setText(0, '导入现状收测数据')
    child22 = QTreeWidgetItem(child2)
    child22.setText(0, '调入已有收测范围线')
    child23 = QTreeWidgetItem(child2)
    child23.setText(0, '设置收测范围线线串好按分层号')
    child24 = QTreeWidgetItem(child2)
    child24.setText(0, '施工范围线赋属性')
    child25 = QTreeWidgetItem(child2)
    child25.setText(0, '计算填挖方量并形成汇总表')
    child26 = QTreeWidgetItem(child2)
    child26.setText(0, '图层内选择线串范围创建三维')
    child27 = QTreeWidgetItem(child2)
    child27.setText(0, '两个段之间创建三维示坡线')

    child3 = QTreeWidgetItem(root)
    child3.setText(0, '露采采矿')
    child31 = QTreeWidgetItem(child3)
    child31.setText(0, '初始化')
    child32 = QTreeWidgetItem(child3)
    child32.setText(0, '调入已有数据')
    child33 = QTreeWidgetItem(child3)
    child33.setText(0, '台阶推荐条带')
    child34 = QTreeWidgetItem(child3)
    child34.setText(0, '台阶开拓条带')
    child35 = QTreeWidgetItem(child3)
    child35.setText(0, '为采掘条带赋编号和单位')
    child36 = QTreeWidgetItem(child3)
    child36.setText(0, '删除采掘条带')
    child37 = QTreeWidgetItem(child3)
    child37.setText(0, '采掘条带算量')
    child38 = QTreeWidgetItem(child3)
    child38.setText(0, '周计划')

    child4 = QTreeWidgetItem(root)
    child4.setText(0, '地采地质')
    child41 = QTreeWidgetItem(child4)
    child41.setText(0, '数据处理')
    child42 = QTreeWidgetItem(child4)
    child42.setText(0, '品位控制模型更新')
    child43 = QTreeWidgetItem(child4)
    child43.setText(0, '回采模型更新')
    child44 = QTreeWidgetItem(child4)
    child44.setText(0, '绘图')

    child5 = QTreeWidgetItem(root)
    child5.setText(0, '地采测量')
    child51 = QTreeWidgetItem(child5)
    child51.setText(0, '数据处理')
    child52 = QTreeWidgetItem(child5)
    child52.setText(0, '品位控制模型更新')
    child53 = QTreeWidgetItem(child5)
    child53.setText(0, '回采模型更新')
    child54 = QTreeWidgetItem(child5)
    child54.setText(0, '绘图')

    child6 = QTreeWidgetItem(root)
    child6.setText(0, '地采采矿')
    child61 = QTreeWidgetItem(child6)
    child61.setText(0, '数据准备')
    child62 = QTreeWidgetItem(child6)
    child62.setText(0, '爆破准备')
    child63 = QTreeWidgetItem(child6)
    child63.setText(0, '爆破参考边界')
    child64 = QTreeWidgetItem(child6)
    child64.setText(0, '单排巷（单井或VCR）')
    child65 = QTreeWidgetItem(child6)
    child65.setText(0, '单排巷（双井或VCR）')
    child66 = QTreeWidgetItem(child6)
    child66.setText(0, '双排巷（单井或VCR）')
    child67 = QTreeWidgetItem(child6)
    child67.setText(0, '双排巷（双井或VCR）')
    child68 = QTreeWidgetItem(child6)
    child68.setText(0, '井孔编辑')
    child69 = QTreeWidgetItem(child6)
    child69.setText(0, '单体')
    child6a = QTreeWidgetItem(child6)
    child6a.setText(0, '装药')
    child6b = QTreeWidgetItem(child6)
    child6b.setText(0, '爆破实体')
    child6c = QTreeWidgetItem(child6)
    child6c.setText(0, '底部结构')

    child7 = QTreeWidgetItem(root)
    child7.setText(0, '通用插件')
    child71 = QTreeWidgetItem(child7)
    child71.setText(0, '闭合段生成实体')
    child72 = QTreeWidgetItem(child7)
    child72.setText(0, '外推矿体生成实体')
    child73 = QTreeWidgetItem(child7)
    child73.setText(0, '劈分闭合线圈')
    child74 = QTreeWidgetItem(child7)
    child74.setText(0, '求实体的质心')
    child75 = QTreeWidgetItem(child7)
    child75.setText(0, '内插过渡段')
    child76 = QTreeWidgetItem(child7)
    child76.setText(0, 'XY坐标换')
    child77 = QTreeWidgetItem(child7)
    child77.setText(0, '点击隐藏实体')
    child78 = QTreeWidgetItem(child7)
    child78.setText(0, '将DTM中每个网赋以独有的体号')
    child79 = QTreeWidgetItem(child7)
    child79.setText(0, '将DTM中所有网统一到同一体号')
    child7a = QTreeWidgetItem(child7)
    child7a.setText(0, '强制性连线')
    child7b = QTreeWidgetItem(child7)
    child7b.setText(0, '选择两个点切剖面')
    child7c = QTreeWidgetItem(child7)
    child7c.setText(0, '生成坐标网格体')
    child7d = QTreeWidgetItem(child7)
    child7d.setText(0, '沿线生成打印散点')
    child7e = QTreeWidgetItem(child7)
    child7e.setText(0, '为等高线赋Z值')
    child7f = QTreeWidgetItem(child7)
    child7f.setText(0, '坡顶坡底赋Z值（最短距离）')
    child7g = QTreeWidgetItem(child7)
    child7g.setText(0, '坡顶坡底赋Z值（手工）')
    child7h = QTreeWidgetItem(child7)
    child7h.setText(0, '按长度分割线条')
    child7i = QTreeWidgetItem(child7)
    child7i.setText(0, '生成示坡线')
    child7j = QTreeWidgetItem(child7)
    child7j.setText(0, '生成巷道断面')
    child7k = QTreeWidgetItem(child7)
    child7k.setText(0, '以面积求多边形')
    child7l = QTreeWidgetItem(child7)
    child7l.setText(0, '将2根线在交点断开')
    child7l.setData(0,)

    tree.addTopLevelItem(root)
    # root.connect(root,SIN)
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

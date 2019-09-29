import sys
import time

from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow, QPushButton
from PySide2.QtWebEngineWidgets import QWebEngineView
from Util import MyTabWidget
from Util import WebEngineView

if __name__ == "__main__":
    # 启动应用
    app = QApplication(sys.argv)

    # 生成窗口并配置
    mainWindow = QMainWindow()
    mainWindow.resize(640, 480)
    mainWindow.setWindowTitle('测试应用')

    # 生成并配置tab组件
    tabWidget = MyTabWidget()
    webView = WebEngineView(tabWidget)
    webView.load(QUrl("http://www.ifeng.com"))
    tabWidget.create_Tab([webView])

    mainWindow.setCentralWidget(tabWidget)
    mainWindow.showMaximized()

    # 退出应用
    sys.exit(app.exec_())

import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(__file__)
    print('BASE_DIR=%s' % BASE_DIR)
    app = QApplication(sys.argv)

    frame = QMainWindow()
    frame.resize(800, 600)
    frame.setWindowTitle("测试")

    webView = QWebEngineView()
    webView.load(QUrl("web_file.html"))

    sys.exit(app.exec_())

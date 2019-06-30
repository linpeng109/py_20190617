import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout

import startupProcess as StartupProcess
import getPidFromPName as GetPidFromPName
import getHwndFromPid as GetHwndFromPid


class MyMainFrame(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setupUI(self):
        self.setWindowTitle("奥信爆破客户端")
        self.resize(600, 480)
        self.layout.set
        self.layout = QVBoxLayout()

        self.pushBtn_startProcess = QPushButton('Start Surpac', self)
        self.pushBtn_startProcess.clicked.connect(self.on_pushBtn_clicked_startupProcess)
        self.layout.addWidget(self.pushBtn_startProcess)

        self.pushBtn_getPidFromPName = QPushButton('Get Surpac Pid', self)
        self.pushBtn_getPidFromPName.clicked.connect(self.on_pushBtn_clicked_getPidFromPName)
        self.layout.addWidget(self.pushBtn_getPidFromPName)


        # self.pushBtn = QPushButton('Start Surpac', self)
        # self.pushBtn.clicked.connect(self.on_pushBtn_clicked_startupProcess)
        # self.layout.addWidget(self.pushBtn)

        self.setLayout(self.layout)

    def on_pushBtn_clicked_startupProcess(self):
        print("start surpac ......")
        StartupProcess.start()

    def on_pushBtn_clicked_getPidFromPName(self):
        print("getPidFromPName ......")
        GetPidFromPName.getPids("surpac2")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_myframe = MyMainFrame()
    the_myframe.setupUI()
    the_myframe.show()

    sys.exit(app.exec_())

import sys
import time
from PySide2 import QtWidgets
from getHwndFromPid import GetHwndFromPid
from startupProcess import StartupProcess
from getPidFromPName import GetPidFromPName
from MainFrame import Ui_MainWindow


class MyMainWindow(QtWidgets.QMainWindow):
    cmd = ''
    pname = ''
    hwnds = ''

    def on_startSurpac_clicked_btn(self):
        startupProcess = StartupProcess()
        startupProcess.start()

    def on_getPidFromPName_clicked(self):
        getPidFromPName = GetPidFromPName()
        pidSet = getPidFromPName.getPids("surpac2")
        for pid in pidSet:
            # print(pid)
            self.pid = pid

    def on_getHwndFromPid_clicked(self):
        print("self.pid=%s" % self.pid)
        getHwndFromPid = GetHwndFromPid()
        getHwndFromPid.getHwnds()
        time.sleep(5)
        print(getHwndFromPid.hwnds)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.startSurpacBtn.clicked.connect(mainWindow.on_startSurpac_clicked_btn)
    ui.getPidFormPNameBtn.clicked.connect(mainWindow.on_getPidFromPName_clicked)
    ui.getHwndFromPidBtn.clicked.connect(mainWindow.on_getHwndFromPid_clicked)
    mainWindow.show()
    sys.exit(app.exec_())

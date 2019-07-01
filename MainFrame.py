# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui',
# licensing of 'MainFrame.ui' applies.
#
# Created: Mon Jul  1 11:20:34 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startSurpacBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startSurpacBtn.setObjectName("startSurpacBtn")
        self.verticalLayout.addWidget(self.startSurpacBtn)
        self.getPidFormPNameBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getPidFormPNameBtn.setObjectName("getPidFormPNameBtn")
        self.verticalLayout.addWidget(self.getPidFormPNameBtn)
        self.getHwndFromPidBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getHwndFromPidBtn.setObjectName("getHwndFromPidBtn")
        self.verticalLayout.addWidget(self.getHwndFromPidBtn)
        self.getWindowFormHwndBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getWindowFormHwndBtn.setObjectName("getWindowFormHwndBtn")
        self.verticalLayout.addWidget(self.getWindowFormHwndBtn)
        self.killProcessFormPidBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.killProcessFormPidBtn.setObjectName("killProcessFormPidBtn")
        self.verticalLayout.addWidget(self.killProcessFormPidBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.startSurpacBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Start surpac2", None, -1))
        self.getPidFormPNameBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Get Pid Form PName", None, -1))
        self.getHwndFromPidBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Get Hwnd form Pid", None, -1))
        self.getWindowFormHwndBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Get Window form Hwnd", None, -1))
        self.killProcessFormPidBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Kill Process Form Pid", None, -1))


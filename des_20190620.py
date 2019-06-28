# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des_20190620.ui',
# licensing of 'des_20190620.ui' applies.
#
# Created: Tue Jun 25 16:06:43 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 384)
        MainWindow.setWindowOpacity(4.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(10, 10, 60, 20))
        self.startBtn.setAutoRepeatInterval(90)
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(81, 10, 60, 17))
        self.stopBtn.setObjectName("stopBtn")
        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(152, 10, 60, 17))
        self.showBtn.setObjectName("showBtn")
        self.hiddenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.hiddenBtn.setGeometry(QtCore.QRect(223, 10, 60, 17))
        self.hiddenBtn.setObjectName("hiddenBtn")
        self.closeAppBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeAppBtn.setGeometry(QtCore.QRect(294, 10, 56, 17))
        self.closeAppBtn.setObjectName("closeAppBtn")
        self.getWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.getWinBtn.setGeometry(QtCore.QRect(365, 10, 81, 21))
        self.getWinBtn.setObjectName("getWinBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.startBtn.setText(QtWidgets.QApplication.translate("MainWindow", "启动Surpace2", None, -1))
        self.stopBtn.setText(QtWidgets.QApplication.translate("MainWindow", "关闭Surpace2", None, -1))
        self.showBtn.setText(QtWidgets.QApplication.translate("MainWindow", "显示Surpace2", None, -1))
        self.hiddenBtn.setText(QtWidgets.QApplication.translate("MainWindow", "隐含Surpace2", None, -1))
        self.closeAppBtn.setText(QtWidgets.QApplication.translate("MainWindow", "关闭应用", None, -1))
        self.getWinBtn.setText(QtWidgets.QApplication.translate("MainWindow", "获取窗口", None, -1))
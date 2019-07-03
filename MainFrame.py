# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui',
# licensing of 'MainFrame.ui' applies.
#
# Created: Wed Jul  3 17:14:40 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StartSurpacBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StartSurpacBtn.setObjectName("StartSurpacBtn")
        self.verticalLayout.addWidget(self.StartSurpacBtn)
        self.SetSurpacWindowHideBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SetSurpacWindowHideBtn.setObjectName("SetSurpacWindowHideBtn")
        self.verticalLayout.addWidget(self.SetSurpacWindowHideBtn)
        self.SetSurpac2WindowShowBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SetSurpac2WindowShowBtn.setObjectName("SetSurpac2WindowShowBtn")
        self.verticalLayout.addWidget(self.SetSurpac2WindowShowBtn)
        self.MoveSurpac2windowBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MoveSurpac2windowBtn.setObjectName("MoveSurpac2windowBtn")
        self.verticalLayout.addWidget(self.MoveSurpac2windowBtn)
        self.KillSurpac2Btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.KillSurpac2Btn.setObjectName("KillSurpac2Btn")
        self.verticalLayout.addWidget(self.KillSurpac2Btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.StartSurpacBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Start surpac2", None, -1))
        self.SetSurpacWindowHideBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Set Surpac2 windows Hide", None, -1))
        self.SetSurpac2WindowShowBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Set Surpac2 windows Show", None, -1))
        self.MoveSurpac2windowBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Move Surpac2 windows", None, -1))
        self.KillSurpac2Btn.setText(QtWidgets.QApplication.translate("MainWindow", "Kill Surpac2", None, -1))


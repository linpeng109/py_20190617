import os
import time
import sys
import win32gui

from subprocess import Popen
from PySide2 import QtWidgets

from PySide2.QtWidgets import QWidget

from PySide2.QtGui import QWindow

# Start win32 application calc.exe
root_path = os.environ.get("SystemRoot", r"C:\\WINDOWS")
calc_path = r'%s\\System32\\calc.exe' % root_path
Popen(calc_path)
time.sleep(500)

# Get window handle of calc window
calc_hwnd = win32gui.FindWindow(None, u"计算器")
subwin=QWindow.fromWinId(calc_hwnd)
# subwdgt=
print(calc_hwnd)

# Creat QT Application
application = QtWidgets.QApplication()
mainwin = QtWidgets.QMainWindow()

# Set QT mainwindow as parent of calc window
# mainwin.setParent(mainwin.winId(), calc_hwnd)
mainwin.createWindowContainer(QWidget(),subwin)


mainwin.showMaximized()
mainwin.show()
# Convert calc into QT widget
wgt = mainwin.find(calc_hwnd)
# XXX: following print gives "None"
print(type(wgt))
sys.exit(application.exec_())
import os, time, win32gui
from subprocess import Popen
from PySide2 import QtWidgets
from PySide2.QtGui import QWindow

root_dir = os.environ.get("SystemRoot", r"C:\\WINDOWS")
calc = r'%s\\System32\\calc.exe' % root_dir
Popen(calc)
time.sleep(1)
# Get window handle of calc window
calc_hwnd = win32gui.FindWindow(None, u"计算器")
print(calc_hwnd)
# Creat QT Application
a = QtWidgets.QApplication([])
mainwin = QtWidgets.QMainWindow()
# Set QT mainwindow as parent of calc window

win32gui.SetParent(calc_hwnd)

mainwin.showMaximized()
mainwin.show()
# Convert calc into QT widget
wgt = mainwin.find(calc_hwnd)
# XXX: following print gives "None"
print(type(wgt))
a.exec_()

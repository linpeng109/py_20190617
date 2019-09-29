#!/usr/bin/env python

import sys

from PySide2.QtCore import SIGNAL
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

from socketcc import SocketClient


class MyTreeItem(QTreeWidgetItem):

    def __init__(self, s, parent=None):
        super(MyTreeItem, self).__init__(parent, [s])


class MyTree(QTreeWidget):

    def __init__(self, parent=None):
        super(MyTree, self).__init__(parent)
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
        for s in ['清除', '其他']:
            MyTreeItem(s, self)
        self.connect(self, SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onClick)

    def onClick(self, item, column):
        print(item.text(0))
        socket = SocketClient(2672)
        message = 'TCLSCRIPTBEGIN\n' + 'set status [ SclFunction \"EXIT GRAPHICS\" {} ]' + 'TCLSCRIPTEND\n'
        result = socket.sendMsg(message)
        print(result.decode(socket.ENCODE))
        socket.closeSocket()


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.tree = MyTree(self)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()

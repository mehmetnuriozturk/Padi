#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under GPL v3
# Copyright 2013, Mehmet Nuri ÖZTÜRK <mnozturk2@gmail.com>
# Please read the COPYING file.


import sys, signal

from PyQt4 import QtCore
from PyQt4 import QtGui

from scrPadi import MainWindow
import icons_rc
def EkranOrtala(self):
     screen = QtGui.QDesktopWidget().screenGeometry()
     size =  self.geometry()
     self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtGui.QApplication(sys.argv)

    app.setApplicationName("padi")
    app.setOrganizationName("padi")
    mainWindow = MainWindow()
    mainWindow.EkranOrtala()
    mainWindow.show()
    return app.exec_()

if __name__ == "__main__":
    main()

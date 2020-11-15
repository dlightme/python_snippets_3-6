# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:53:45 2019

@author: rockhunter
"""

import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  #super returns parent object (QMainWindow)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.SetWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.show()
        
app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())      
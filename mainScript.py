#main file
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, 
                             QHBoxLayout,
                             QMainWindow,
                             QPushButton,
                             QStackedLayout,
                             QVBoxLayout,
                             QWidget)
from PyQt6 import QtWidgets, uic
from MainWindow import MainWindow

import sys

#App instance
app = QtWidgets.QApplication([])

window = MainWindow()
window.show() #dont delete that, or window will not show

app.exec()
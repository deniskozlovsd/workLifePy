from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, 
                             QHBoxLayout,
                             QMainWindow,
                             QPushButton,
                             QStackedLayout,
                             QVBoxLayout,
                             QWidget)
from PyQt6 import QtWidgets, uic
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)
        
        self.workButton.clicked.connect(self.activateWorkMode)
        self.lifeButton.clicked.connect(self.activateLifeMode)
        
       # self.m_buttonChecked = True
        #self.setWindowTitle("Work/Life")
    def activateWorkMode(self):
        self.workButton.setText("Worked")
        self.workButton.setEnabled(False)
    def activateLifeMode(self):
        self.lifeButton.setText("Lifed")
        self.lifeButton.setEnabled(False)


       
        
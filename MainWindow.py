from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, 
                             QDialog,
                             QHBoxLayout,
                             QMainWindow,
                             QPushButton,
                             QWidget)
from PyQt6 import QtWidgets, uic
from dialog import Ui_Dialog

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
        #put pop-up here
        dlg = workButtonDlg(self)
        dlg.exec()


    def activateLifeMode(self):
        self.lifeButton.setText("Lifed")
        self.lifeButton.setEnabled(False)

class workButtonDlg(QDialog):
    """work button pop up with work time setup"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


       
        
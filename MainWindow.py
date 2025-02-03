from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, 
                             QHBoxLayout,
                             QMainWindow,
                             QPushButton,
                             QStackedLayout,
                             QVBoxLayout,
                             QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_buttonChecked = True
        self.setWindowTitle("Work/Life")

        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.stackLayout = QStackedLayout()

        pageLayout.addLayout(buttonLayout)
        pageLayout.addLayout(self.stackLayout)

        self.workbtn = QPushButton("Work")
        self.workbtn.pressed.connect(self.activateWorkMode)
        buttonLayout.addWidget(self.workbtn)

        self.lifebtn = QPushButton("Life")
        self.lifebtn.pressed.connect(self.activateLifeMode)
        buttonLayout.addWidget(self.lifebtn)
       # self.stackLayout.addWidget()

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

    def activateWorkMode(self):
        self.workbtn.setText("Worked")
        self.workbtn.setEnabled(False)

    def activateLifeMode(self):
        self.lifebtn.setText("Lifed")
        self.lifebtn.setEnabled(False)



       
        
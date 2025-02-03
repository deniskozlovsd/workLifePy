#main file
from PyQt6.QtWidgets import QApplication, QWidget

import sys

#App instance
app = QApplication(sys.argv)

window = QWidget()
window.show() #dont delete that, or window will not show

app.exec()
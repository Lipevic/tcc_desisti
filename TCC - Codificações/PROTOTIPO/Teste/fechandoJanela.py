from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Close Window")
        self.l1=QLabel("Let's Close this Window")
        self.l1.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.l1)
        self.close()    #Closes the window at this point
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()
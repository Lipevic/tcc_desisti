import sys
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize 
import socket

    
app=QtWidgets.QApplication([])

ipLocall = uic.loadUi('enderecoOrigem.ui')
ipLocal = socket.gethostbyname(socket.gethostname())
ipLocall.label_4.setText(ipLocal)

ipLocall.show()
print(ipLocal)
app.exec()

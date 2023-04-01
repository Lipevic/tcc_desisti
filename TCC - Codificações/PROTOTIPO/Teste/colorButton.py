import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        button = QPushButton('Clique aqui', self)
        button.setToolTip('Este é um botão')
        button.clicked.connect(self.on_click)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Exemplo')
        self.show()

    def on_click(self):
        sender = self.sender()
        sender.setStyleSheet("background-color: red;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
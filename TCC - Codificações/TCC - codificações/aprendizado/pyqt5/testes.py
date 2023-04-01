import sys
from turtle import color
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui
class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira Janela'
        
        self.caixaTexto = QLineEdit(self)
        self.caixaTexto.move(350, 350)
        self.caixaTexto.resize(300, 25)
        botaoEnvText = QPushButton('Espresse o quão Maruto é bão ', self)
        botaoEnvText.move(350,400)
        botaoEnvText.resize(250,50)
        botaoEnvText.setStyleSheet('QPushButton {background-color: #000; color:#fff; font-size:15px; border: 3px solid transparent; border-radius: 15px;}')
        botaoEnvText.clicked.connect(self.enviarMensagem)
      
        self.mensagem = QLabel(self)
        self.mensagem.setText('Frases sobre Maruto:')
        self.mensagem.move(350,450)
        self.mensagem.setStyleSheet('QLabel {font:bold;font-size:20px;color:"black"}')
        self.mensagem.resize(400,40)

      
      
      
      
      
        botaoCliente = QPushButton('CLIENTE', self)
        botaoCliente.move(200,200)
        botaoCliente.resize(150,80)
        botaoCliente.setStyleSheet('QPushButton {background-color: #32a041; font-size:15px; border: 3px solid transparent; border-radius: 15px;}')
        botaoCliente.clicked.connect(self.botaoClienteClick)

        botaoServidor = QPushButton('SERVIDOR', self)
        botaoServidor.move(400,200)
        botaoServidor.resize(150,80)
        botaoServidor.setStyleSheet('QPushButton {background-color: #c8191e; font-size:15px; border: 3px solid transparent; border-radius: 15px;}')
        botaoServidor.clicked.connect(self.botaoServidorClick)  

        self.label = QLabel(self)
        self.label.setText('Escolha o que você deseja ser:')
        self.label.move(50, 150)
        self.label.setStyleSheet('QLabel {font:bold;font-size:20px;color:"black"}')
        self.label.resize(400,40)


    #trabalhando com  imagens 
        self.imag = QLabel(self)
        self.imag.move(50, 350)
        self.imag.setPixmap(QtGui.QPixmap('aprendizado\pyqt5\maruto1.png'))
        self.imag.resize(256, 232)




        self.carregarJanela()

    def enviarMensagem(self):
        textoRecebido = self.caixaTexto.text()
        self.mensagem.setText(textoRecebido)

    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botaoClienteClick(self):
        print('botão cliente foi clicado!')
        self.label.setText('Pronto! Você é um cliente agora!')
    
    def botaoServidorClick(self):
        print('botão Servidor foi clicado!')
        self.label.setText('Pronto! Você é um servidor agora!')
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
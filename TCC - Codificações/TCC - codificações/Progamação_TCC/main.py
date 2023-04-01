from PyQt5 import uic, QtWidgets
import socket

#CHAMADAS DO CLIENTE
def chamaCliente():
    telaCliente.show()

def chamaCabecalhoTCPCliente():
    cabecalhoTCPCliente.show()
    cabecalhoTCPCliente.label.setText('Cabeçalho TCP do Cliente')

def chamaCabecalhoIPCliente():
    cabecalhoIPCliente.show()
    cabecalhoIPCliente.label.setText('Cabeçalho IP do Cliente')
#CHAMADAS DO SERVIDOR
def chamaServidor():
    telaServidor.show()

def chamaCabecalhoIPServidor():
    cabecalhoIPServidor.show()
    cabecalhoIPServidor.label.setText('Cabeçalho IP do Servidor')

def chamaCabecalhoTCPServidor():
    cabecalhoTCPServidor.show()
    cabecalhoTCPServidor.label.setText('Cabeçalho TCP do Servidor')

#CRIANDO SOCKET
#socket cliente
"""
def socketCliente(self):
    host = 'localhost'
    porta = 54321
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))
    mensagem = 'FUNCIONOU!!!'
    cliente.sendall(str.encode(mensagem))
    data= cliente.recv(1024)
    print(data)

#socket servidor

def socketServidor(self):
    testeServer = uic.loadUi('testenoservidor.ui')
    testeServer.show()
    host = 'localhost'
    porta = 54321
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    conexao, endereco = servidor.accept()
    testeServer.label.setText(endereco)

    while True:

        data = conexao.recv(1024)
        if data:
            testeServer.label_4.setText(data)
            testeServer.label_6.setText('Fechando conexão!!')
            conexao.sendall (str.encode('|SERVIDOR|->Mensagem foi recebida'))
            conexao.close()
            break
"""

 

app=QtWidgets.QApplication([])

telaInicial = uic.loadUi('mainWindow.ui')
telaCliente = uic.loadUi('clienteWindow.ui')
telaServidor = uic.loadUi('servidorWindow.ui')
cabecalhoTCPCliente = uic.loadUi('cabecalho_TCP.ui')
cabecalhoIPCliente = uic.loadUi('cabecalho_IP.ui')
cabecalhoTCPServidor = uic.loadUi('cabecalho_TCP.ui')
cabecalhoIPServidor = uic.loadUi('cabecalho_IP.ui')

#chamando cliente ou servidor
#cliente
telaInicial.clienteBotao.clicked.connect(chamaCliente)
telaCliente.ipBotao.clicked.connect(chamaCabecalhoIPCliente)
telaCliente.tcpBotao.clicked.connect(chamaCabecalhoTCPCliente)
#servidor
telaInicial.servidorBotao.clicked.connect(chamaServidor)
telaServidor.ipBotao.clicked.connect(chamaCabecalhoIPServidor)
telaServidor.tcpBotao.clicked.connect(chamaCabecalhoTCPServidor)
#telaServidor.chamandoCliente.Clicked.connect(socketServidor)


telaInicial.show()
app.exec()
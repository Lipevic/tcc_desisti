import socket
from PyQt5 import uic, QtWidgets#, QLabel
import asyncio
def socketCliente():
    testeCliente.show()
    HOST = 'localhost'  #HOST = input ('Informe o host do servidor(IP do servidor) a qual deseja conectar:\n')
                        #tratar erro de nome para ser enviado apenas o que é desejado
       
    
    PORT = 15321    #PORT = int(input('informe a porta do servidor: \n'))
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    testeCliente.label_6.setText('Procurando Servidor')
    def clienteEnviandoMensagem():
        mensagem_cliente = 'Enviando uma mensagem ao servidor!!' #foi
        testeCliente.label_4.setText(mensagem_cliente)
        c.sendall(str.encode(mensagem_cliente))
        data= c.recv(1024)
        print('Mensagem do servidor foi: ' + mensagem_cliente)
        testeCliente.label_2.setText(data)
        c.close()
    def conectandoCliente(HOST, PORT):

        c.connect((HOST, PORT))
        clienteEnviandoMensagem()
    conectandoCliente(HOST, PORT)
    #######TENTAR FAZER POR ETAPAS primeiro(def) uma parte e por ai vai
    #mensagem_cliente = input('Informe a mensagem que sera enviada ao servidor: \n')
        
        



def socketServidor(self):
    testeServer.show()
    # input('Informe o host do servidor(IP do servidor)\n')
    def criandoSocketServer(self):
        self.HOST = '127.0.0.1'
        self.PORT = 15321  # int(input('informe a porta do servidor\n'))
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def serverOuvindo(self):
        self.s.bind((self.HOST, self.PORT))
        testeServer.label_6.setText('Aguardando conexão com o cliente e ouvindo')
        self.s.listen()
    criandoSocketServer(self)
    serverOuvindo(self)

    if self.s.accept:
        conexao, endereco = self.s.accept()
        testeServer.label.setText(endereco)
        print(endereco)
    while conexao:
        data = conexao.recv(1024)
        if data:
            testeServer.label_4.setText(data)
            testeServer.label_6.setText('Fechando conexão!!')
            conexao.sendall(str.encode('|SERVIDOR|->Mensagem foi recebida'))
            conexao.close()
            break
    

app=QtWidgets.QApplication([])

testeServer = uic.loadUi('testenoservidor.ui')
testeCliente = uic.loadUi('testecliente.ui')
telaInicial = uic.loadUi('inicial.ui')






telaInicial.cliente.clicked.connect(socketCliente)
telaInicial.servidor.clicked.connect(socketServidor)


telaInicial.show()
app.exec()
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket
import random



def duvidaIP():
    mensagemInformada = "O IP (Internet Protocol) é o principal protocolo de comunicação da Internet. Ele é o responsável por endereçar e encaminhar os pacotes que trafegam pela rede mundial de computadores. Pacotes são os blocos de informações enviados na Internet e podem ser considerados como as cartas enviadas pelo serviço de correios. (ALTERAR CONTEM PLAGIO)"
    QMessageBox.about(telaCliente, "O que é o IP", mensagemInformada)
def duvidaTCP():
   # janela = janela
    mensagemInformada = "O QUE SER O PROTOCOLO TCP"
    QMessageBox.about(telaCliente, "O que é o TCP", mensagemInformada)
###CLIENTE CHAMADOS
def chamaCliente():
    telaCliente.show()

    telaCliente.pushButton_5.clicked.connect(duvidaIP)
    telaCliente.pushButton_6.clicked.connect(duvidaTCP)#(duvidaTCP(telaCliente))
def abaoutVersao():
    QMessageBox.about(cabecalhoIPCliente.pushButton,"Versão", "EXISTE DUAS VERSÕES DE IP O IVP4 E O IPV6")
def abaoutIHM():
    QMessageBox.about(cabecalhoIPCliente.pushButton_2,"IHM", "Indica o tamanho do cabeçalho em palavras de 32 bits. O valor mínimo correto é 20")

def abaoutCompimentoTotal():
    QMessageBox.about(cabecalhoIPCliente.pushButton_5,"Comprimento Total", "Comprimento do Pacote - Este campo fornece o tamanho total do pacote em bytes, incluindo o cabeçalho e os dados.")

def abaoutTipoServico():
    QMessageBox.about(cabecalhoIPCliente.pushButton_3,"TIPOS DE SERVIÇOS","O campo Tipo de Serviço contém um valor binário de 8 bits que é usado para determinar a prioridade de cada pacote. Este Campo do caabeçalho determinará o prioridade que o datagrama receberá dos roteadores durante o percurso")
def abaoutIdentificacao():
    QMessageBox.about(cabecalhoIPCliente.pushButton_6,"IDENTIFICAÇÃO","Indica o tamanho do cabeçalho em palavras de 32 bits. O valor mínimo correto é 20(COPIA)")
#def endEndereco():
#    pass
def abaoutEnderecoOrigem():
    ipLocal = socket.gethostbyname(socket.gethostname())
    enderecoOrigem.label_4.setText(ipLocal)
    enderecoOrigem.show()
    def endEnderecoOrigem():
        enderecoOrigem.close()
    enderecoOrigem.pushButton.clicked.connect(endEnderecoOrigem)
def abaoutEnderecoDestino():
    enderecoDestino.show()
    #enderecoDestino.lineEdit.clicked.connect(enderecoDestino.lineEdit.setText(""))# tentativa de apagar no lineEdit com um click
    def enderecoServidor():
        ipServidor = enderecoDestino.lineEdit.text()
        print(ipServidor) #CADA VEZ QUE PRINTA ELE ADICIONA MAIS UMA LINHA --- ENTENDER O POR QUE!
        #COMENTAR ESSA PARTE E DEIXA O VALOR DA VARIAVEL FIXO PRA TESTE A CONTINUIDADE DO SISTEMA E VER COMUNICA !!
        #         
        
        enderecoDestino.label_5.setText(ipServidor)
        enderecoDestino.lineEdit.setText(None)
        enderecoDestino.close()

    enderecoDestino.pushButton.clicked.connect(enderecoServidor)
def abaoutFlags():
    QMessageBox.about(cabecalhoIPCliente.pushButton_7,"Flags","Flags texto")
def abaoutDeslocamentoDoFragmento():
    QMessageBox.about(cabecalhoIPCliente.pushButton_8,"Deslocamento de Fragmento","Deslocamento de Fragmento texto")    
def abaoutTempoVida():
    QMessageBox.about(cabecalhoIPCliente.pushButton_10,"Tempo de Vida","Tempo de Vida texto")
def abaoutChecksum():
    QMessageBox.about(cabecalhoIPCliente.pushButton_9,"Checksum","Checksum texto")
def abaoutProtocolo():
    QMessageBox.about(cabecalhoIPCliente.pushButton_11,"Protocolo","Protocolo texto")

def chamaCabecalhoIPCliente():
    cabecalhoIPCliente.show()
    cabecalhoIPCliente.pushButton.clicked.connect(abaoutVersao)
    cabecalhoIPCliente.pushButton_2.clicked.connect(abaoutIHM)
    cabecalhoIPCliente.pushButton_3.clicked.connect(abaoutTipoServico)
    cabecalhoIPCliente.pushButton_5.clicked.connect(abaoutCompimentoTotal)
    cabecalhoIPCliente.pushButton_6.clicked.connect(abaoutIdentificacao)
    cabecalhoIPCliente.pushButton_7.clicked.connect(abaoutFlags)
    cabecalhoIPCliente.pushButton_8.clicked.connect(abaoutDeslocamentoDoFragmento)
    cabecalhoIPCliente.pushButton_9.clicked.connect(abaoutChecksum)
    cabecalhoIPCliente.pushButton_10.clicked.connect(abaoutTempoVida)
    cabecalhoIPCliente.pushButton_11.clicked.connect(abaoutProtocolo)
    cabecalhoIPCliente.pushButton_12.clicked.connect(abaoutEnderecoOrigem)
 #   if ipServidor == False:
  #      enderecoDestino.lineEdit.textEdit("")
   #     enderecoDestino.label_5.textEdit("Não salvo Ainda")
    #ipServidor = 
    cabecalhoIPCliente.pushButton_13.clicked.connect(abaoutEnderecoDestino)  





def tcpClientePortaOrigem():
    tcpPortaOrigem.show()
    def okButton():


        portaOrigem =  tcpPortaOrigem.lineEdit.text()
        tcpPortaOrigem.lineEdit.setText(None)
        tcpPortaOrigem.label_8.setText(portaOrigem)
        tcpPortaOrigem.close()
    tcpPortaOrigem.ok.clicked.connect(okButton)

def tcpClientePortaDestino():
    tcpPortaDestino.show()   
    def okButton():
        portaDestino = tcpPortaDestino.lineEdit.text()
        tcpPortaDestino.lineEdit.setText(None)   
        tcpPortaDestino.label_8.setText(portaDestino)     
        tcpPortaDestino.close()
    tcpPortaDestino.ok.clicked.connect(okButton)
def tcpClienteNumeroSequencia():
    
    if tcpNumeroSequencia.numeroSequencia.text() == "":
        numeroSequenciaAleatorio = random.randint(0,4294967295)
        #print(numeroSequenciaAleatorio)
        tcpNumeroSequencia.numeroSequencia.setText(str(numeroSequenciaAleatorio))

    tcpNumeroSequencia.show()
    def okButton():
        tcpNumeroSequencia.close()
    tcpNumeroSequencia.ok.clicked.connect(okButton)

def tcpClienteNumeroConfirmacao():
    tcpNumeroConfirmacao.show()
    def okButton():
        tcpNumeroConfirmacao.close()
    tcpNumeroConfirmacao.ok.clicked.connect(okButton)
def abaoutTamanhoCabecalho():
    QMessageBox.about(cabecalhoTCPCliente.tamanhoCabecalho,"Tamanho Cabeçalho","""
Ele indica o comprimento do cabeçalho TCP em palavras de 32 bits, permitindo que o receptor saiba onde termina o cabeçalho e onde começa o campo de dados.
O campo tamanho do cabeçalho é representado em 4 bits, o que significa que seu valor pode variar de 0 a 15. O tamanho mínimo do cabeçalho é de 20 bytes (5 palavras de 32 bits), enquanto o tamanho máximo é de 60 bytes (15 palavras de 32 bits).
O tamanho do cabeçalho TCP é importante porque influencia diretamente no tamanho total do pacote, o que por sua vez pode afetar a eficiência da transmissão de dados. Se o cabeçalho for muito grande,
isso pode aumentar o tempo de transmissão e o número de pacotes necessários para enviar os dados. Por outro lado, um cabeçalho muito curto pode não fornecer informações suficientes para permitir que o receptor processe corretamente os dados recebidos.
Em resumo, o campo tamanho do cabeçalho no cabeçalho TCP é fundamental para permitir que o receptor entenda corretamente onde começa e onde termina o cabeçalho e para garantir a eficiência da transmissão de dados.""")

def abaoutReservado():
    QMessageBox.about(cabecalhoTCPCliente.reservado,"Reservado","""
O campo reservado do cabeçalho TCP (Transmission Control Protocol) é um campo de 6 bits que é reservado para uso futuro.
Este campo foi incluído no cabeçalho do TCP para permitir possíveis extensões do protocolo no futuro,sem a necessidade de redesenhar todo o cabeçalho.

O campo reservado é definido como zero em todas as implementações do TCP atualmente em uso,e seu uso futuro ainda não foi determinado.
No entanto, ele pode ser usado para acomodar futuras mudanças e atualizações no protocolo sem exigir uma revisão completa do cabeçalho do TCP.  
    """)
def infoFlagsTCP():
    flagsTCP.show()
    def collorButton(flag):
        if flag == "syn":
            flagsTCP.syn.setStyleSheet("background-color: #32a041;")
        elif flag == "ack":
            flagsTCP.ack.setStyleSheet("background-color: #32a041;")
        elif flag == "fin":
            flagsTCP.fin.setStyleSheet("background-color: #32a041;")
        elif flag == "rst":
            flagsTCP.rst.setStyleSheet("background-color: #32a041;")
        elif flag == "psh":
            flagsTCP.psh.setStyleSheet("background-color: #32a041;")    
        elif flag == "urg":
            flagsTCP.urg.setStyleSheet("background-color: #32a041;")           
    flagsTCP.syn.clicked.connect(lambda: collorButton("syn"))
    flagsTCP.ack.clicked.connect(lambda: collorButton("ack"))
    flagsTCP.fin.clicked.connect(lambda: collorButton("fin"))
    flagsTCP.rst.clicked.connect(lambda: collorButton("rst"))
    flagsTCP.psh.clicked.connect(lambda: collorButton("psh"))
    flagsTCP.urg.clicked.connect(lambda: collorButton("urg"))
        
def chamaCabecalhoTCPCliente():
    cabecalhoTCPCliente.show()
    cabecalhoTCPCliente.portaOrigem.clicked.connect(tcpClientePortaOrigem)
    cabecalhoTCPCliente.portaDestino.clicked.connect(tcpClientePortaDestino)
    cabecalhoTCPCliente.numeroSequencia.clicked.connect(tcpClienteNumeroSequencia)
    cabecalhoTCPCliente.numeroConfirmacao.clicked.connect(tcpClienteNumeroConfirmacao)
    cabecalhoTCPCliente.tamanhoCabecalho.clicked.connect(abaoutTamanhoCabecalho)
    cabecalhoTCPCliente.reservado.clicked.connect(abaoutReservado)
    cabecalhoTCPCliente.flags.clicked.connect(infoFlagsTCP)
###SERVIDOR CHAMADOS
def chamaServidor():
    telaServidor.show()

def chamaCabecalhoTCPServidor():
    cabecalhoTCPServidor.show()

def chamaCabecalhoIPServidor():
    cabecalhoIPServidor.show()

app=QtWidgets.QApplication([])

telaInicial = uic.loadUi('mainWindow.ui')
telaCliente = uic.loadUi('clienteWindow.ui')
telaServidor = uic.loadUi('servidorWindow.ui')
cabecalhoTCPCliente = uic.loadUi('cabecalho_TCP.ui')
cabecalhoIPCliente = uic.loadUi('cabecalho_IP.ui')
cabecalhoTCPServidor = uic.loadUi('cabecalho_TCP.ui')
cabecalhoIPServidor = uic.loadUi('cabecalho_IP.ui')
enderecoOrigem = uic.loadUi('enderecoOrigem.ui')
enderecoDestino = uic.loadUi('enderecoDestino.ui')
enderecoDestino = uic.loadUi('enderecoDestino.ui')
tcpPortaOrigem = uic.loadUi('tcpPortaOrigem.ui')
tcpPortaDestino = uic.loadUi('tcpPortaDestino.ui')
tcpNumeroSequencia = uic.loadUi('tcpNumeroSequencia.ui')
tcpNumeroConfirmacao = uic.loadUi('tcpNumeroConfirmação.ui')
flagsTCP = uic.loadUi('flagsTCP.ui')

#chamando cliente ou servidor
#cliente
telaInicial.clienteBotao.clicked.connect(chamaCliente)
telaCliente.tcpBotao.clicked.connect(chamaCabecalhoTCPCliente)
telaCliente.ipBotao.clicked.connect(chamaCabecalhoIPCliente)

#servidor
telaInicial.servidorBotao.clicked.connect(chamaServidor)
telaServidor.ipBotao.clicked.connect(chamaCabecalhoIPServidor)
telaServidor.tcpBotao.clicked.connect(chamaCabecalhoTCPServidor)






telaInicial.show()
app.exec()
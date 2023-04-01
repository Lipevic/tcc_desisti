import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input('digite qualquer coisa: \n')
while True:
    tcp.send (str.encode(msg))
    msg = input('digite qualque coisa: \n')
    if msg =='0':
        tcp.close()
        break
import socket

HOST = 'localhost'
PORT = 15321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
print('Aguardando conexão')
s.listen()

comn, ender = s.accept()

print('Conectado em {}' .format(ender))
while True:
    data = comn.recv(1024)
    if not data:
        print('fechando conexão!')
        comn.close()
        break

    comn.sendall(data)
import socket

HOST = '127.0.0.1'
PORT = 15321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('Funcionou meu chapa, parabéns!'))
data = s.recv(1024)
print('Tudo que vai volta meu mano e vou isso ai ---> {}' .format(data))
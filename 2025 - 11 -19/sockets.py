import socket
nome = socket.gethostname()
ip = socket.gethostbyname(nome)
dados = socket.gethostbyaddr(ip)

print(nome)
print(ip)
print(dados)
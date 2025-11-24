import socket

nome = socket.gethostname()  

ip = socket.gethostbyname(nome)
dados = socket.gethostbyaddr(ip)
tupallps = socket.getaddrinfo(nome, None)

print("IP:", ip)
print("Dados:", dados)
print("Todos os endereços:", tupallps)

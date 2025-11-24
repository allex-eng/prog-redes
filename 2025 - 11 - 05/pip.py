
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Nome da máquina:", hostname)
print("IP da máquina:", ip)



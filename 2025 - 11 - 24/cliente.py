# Importando a biblioteca SOCKET
import socket

# ----------------------------------------------------------------------
HOST_IP_SERVER = '10.25.1.90'    # Corrigido: removido espaço no início
HOST_PORT      = 50000           # Porta do servidor
CODE_PAGE      = 'utf-8'         # Codificação de caracteres
# ----------------------------------------------------------------------

# Criando o socket (socket.AF_INET -> IPV4 / socket.SOCK_DGRAM -> UDP)
sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('\n\nPara sair digite SAIR...\n\n')

while True:
    # Informando a mensagem a ser enviada ao servidor
    strMensagem = input('Digite a mensagem: ')

    # Saindo do cliente quando digitar "SAIR"
    if strMensagem.lower().strip() == 'sair':
        break

    # Convertendo a mensagem em bytes
    bytesMensagem = strMensagem.encode(CODE_PAGE)

    # Enviando a mensagem ao servidor
    try:
        sockUDP.sendto(bytesMensagem, (HOST_IP_SERVER, HOST_PORT))
        print("Mensagem enviada!\n")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}\n")

# Fechando o socket
sockUDP.close()

print("Cliente finalizado.")

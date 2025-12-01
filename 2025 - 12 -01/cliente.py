import socket
import constantes

# Criando o socket (IPv4 + UDP)
sockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mensagem_entr = socket.gethostbyname(socket.gethostname())
sockClient.sendto(mensagem_entr.encode(constantes.CODE_PAGE), constantes.TUPLA_SERVER)
print('\n\nPara sair digite SAIR...\n\n')

try:
    while True:
        # Informando a mensagem a ser enviada para o servidor
        strMensagem = input('Digite a mensagem: ')

        # Saindo do Cliente quando digitar SAIR
        if strMensagem.lower().strip() == 'sair':
            break

        # Enviando a mensagem ao servidor
        sockClient.sendto(strMensagem.encode(constantes.CODE_PAGE), constantes.TUPLA_SERVER)

        # Recebendo resposta do servidor
        bytesMensagemRetorno, tuplaOrigem = sockClient.recvfrom(constantes.BUFFER_SIZE)

        # Obtendo nome do host (se disponível)
        try:
            strNomeHost = socket.gethostbyaddr(tuplaOrigem[0])[0].split('.')[0].upper()
        except socket.herror:
            strNomeHost = tuplaOrigem[0]  # usa o IP se não houver nome reverso

        # Exibindo resposta
        print(f'{tuplaOrigem} -> {strNomeHost}: {bytesMensagemRetorno.decode(constantes.CODE_PAGE)}')

finally:
    sockClient.close()
    print('Servidor finalizado com sucesso.\n')

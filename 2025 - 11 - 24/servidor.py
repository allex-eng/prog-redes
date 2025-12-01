# Importando a biblioteca SOCKET
import socket

# ----------------------------------------------------------------------
HOST_IPSERVER  = '10.25.1.9'     # IP do servidor (corrigido: sem espaço no início)
HOST_PORT      = 50000            # Porta do servidor
CODE_PAGE      = 'utf-8'          # Codificação
BUFFER_SIZE    = 512              # Tamanho do buffer de recepção
# ----------------------------------------------------------------------

# Criando o socket (AF_INET -> IPv4, SOCK_DGRAM -> UDP)
sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ligando o socket à porta
sockServer.bind((HOST_IPSERVER, HOST_PORT))

# Definindo timeout de 0.5s
sockServer.settimeout(0.5)

print('\nRecebendo Mensagens...')
print('Pressione CTRL+C para encerrar o servidor...\n')
print('-' * 100 + '\n')

try:
    while True:
        try:
            # Recebendo dados do cliente
            byteMensagem, tuplaCliente = sockServer.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            continue
        else:
            ip_cliente = tuplaCliente[0]

            # Tentando obter o nome do host
            try:
                strNomeHost = socket.gethostbyaddr(ip_cliente)[0]
                strNomeHost = strNomeHost.split('.')[0].upper()
            except socket.herror:
                # Caso não consiga resolver o hostname
                strNomeHost = ip_cliente

            mensagem = byteMensagem.decode(CODE_PAGE)

            print(f'{tuplaCliente} -> {strNomeHost}: {mensagem}')

except KeyboardInterrupt:
    print('\n\nAVISO: Interrupção detectada (CTRL + C). Encerrando servidor...')

finally:
    sockServer.close()
    print('Servidor finalizado com sucesso.')

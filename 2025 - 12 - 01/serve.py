import socket
import constantes

# Criando o socket (IPv4 + UDP)
sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associando o socket ao IP e porta definidos em constantes
sockServer.bind((constantes.HOST_IP_SERVER, constantes.HOST_PORT))

# Timeout para não bloquear indefinidamente
sockServer.settimeout(0.5)

print('\nRecebendo Mensagens...')
print('Pressione CTRL+C para sair do servidor...\n')
print('-' * 100 + '\n')

try:
    while True:
        try:
            # Recebe mensagem do cliente
            byteMensagem, tuplaCliente = sockServer.recvfrom(constantes.BUFFER_SIZE)
        except socket.timeout:
            # Se não receber nada dentro do timeout, continua o loop
            continue
        else:
            # Tenta resolver o nome do host
            try:
                strNomeHost = socket.gethostbyaddr(tuplaCliente[0])[0].split('.')[0].upper()
            except socket.herror:
                strNomeHost = tuplaCliente[0]  # usa o IP se não houver nome reverso

            # Decodifica e imprime a mensagem recebida
            mensagem = byteMensagem.decode(constantes.CODE_PAGE)
            print(f'{tuplaCliente} -> {strNomeHost}: {mensagem}')

            # Opcional: responder ao cliente
            resposta = f'Servidor recebeu {len(mensagem)} caracteres'
            sockServer.sendto(resposta.encode(constantes.CODE_PAGE), tuplaCliente)

except KeyboardInterrupt:
    print('\nAVISO: CTRL+C pressionado. Encerrando servidor...\n')

finally:
    sockServer.close()
    print('Servidor finalizado com sucesso.\n')

import socket   # Biblioteca padrão para comunicação em rede (sockets)

# -------------------------------------------------------------
# CONFIGURAÇÕES DO CLIENTE
# -------------------------------------------------------------
HOST = '192.168.56.1'   # Endereço IP do servidor
PORT = 50000            # Porta em que o servidor está escutando
BUFFER_SIZE = 1024      # Quantidade máxima de bytes que será recebida por pacote
CODE_PAGE = 'utf-8'     # Codificação de texto usada para enviar e receber strings

# -------------------------------------------------------------
# CRIAÇÃO DO SOCKET UDP
# -------------------------------------------------------------
# AF_INET  -> usa IPv4
# SOCK_DGRAM -> usa UDP (não há conexão persistente como no TCP)
sockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# -------------------------------------------------------------
# LOOP PRINCIPAL
# O cliente pode pedir vários arquivos até digitar "SAIR".
# -------------------------------------------------------------
while True:
    filename = input("Digite o nome do arquivo (ou SAIR): ")

    # Se o usuário digitar SAIR, o programa termina.
    if filename.lower().strip() == "sair":
        break

    # Envia o nome do arquivo para o servidor (codificado em bytes)
    sockClient.sendto(filename.encode(CODE_PAGE), (HOST, PORT))

    # Aguarda resposta inicial do servidor
    # Essa resposta pode ser:
    #   "OK"  -> arquivo encontrado e será enviado
    #   "Arquivo não encontrado" -> servidor não encontrou o arquivo
    data, _ = sockClient.recvfrom(BUFFER_SIZE)

    # ---------------------------------------------------------
    # SE O SERVIDOR ENVIAR "OK", COMEÇA A TRANSFERÊNCIA DO ARQUIVO
    # ---------------------------------------------------------
    if data == b"OK":
        print("Servidor encontrou o arquivo. Recebendo...")

        # Cria um arquivo local para salvar os dados recebidos
        with open("recebido_" + filename, "wb") as f:

            while True:
                # Recebe um bloco (chunk) do arquivo enviado pelo servidor
                chunk, _ = sockClient.recvfrom(BUFFER_SIZE)

                # Se o chunk for "EOF", significa fim da transmissão
                if chunk == b"EOF":
                    print("Fim da transferência.")
                    break

                # Caso contrário, escreve o bloco no arquivo local
                f.write(chunk)

        print(f"Arquivo '{filename}' recebido e salvo como 'recebido_{filename}'.\n")

    # ---------------------------------------------------------
    # CASO O SERVIDOR INFORME QUE O ARQUIVO NÃO EXISTE
    # ---------------------------------------------------------
    else:
        print(data.decode(CODE_PAGE))   # Exibe a mensagem de erro
        print("Tente novamente...\n")

# -------------------------------------------------------------
# FINALIZA O SOCKET AO ENCERRAR O PROGRAMA
# -------------------------------------------------------------
sockClient.close()
print("Cliente encerrado.")

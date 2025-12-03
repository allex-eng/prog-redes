import socket   # Biblioteca usada para criar comunicação de rede (TCP/UDP)
import os       # Biblioteca usada para verificar, abrir e manipular arquivos

# -----------------------------
# CONFIGURAÇÕES DO SERVIDOR
# -----------------------------

HOST = '192.168.56.1'   # Endereço IP onde o servidor irá escutar pedidos
PORT = 50000            # Porta onde o servidor ficará aguardando requisições
BUFFER_SIZE = 1024      # Tamanho máximo de cada pacote de dados enviado/recebido
CODE_PAGE = 'utf-8'     # Codificação usada para transformar texto em bytes e vice-versa

# -----------------------------
# CRIAÇÃO DO SOCKET UDP
# -----------------------------

# socket.AF_INET  -> Usa IPv4
# socket.SOCK_DGRAM -> Cria um socket UDP (não orientado a conexão)
sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associa o socket ao IP e porta definidos (servidor passa a ouvir nessa porta)
sockServer.bind((HOST, PORT))

print("Servidor aguardando pedidos de arquivos...")

try:
    # Loop infinito para atender vários clientes enquanto o servidor estiver ligado
    while True:

        # -----------------------------------------------------------
        # 1) Recebe o nome do arquivo solicitado pelo cliente via UDP
        # -----------------------------------------------------------
        data, addr = sockServer.recvfrom(BUFFER_SIZE)  
        # 'data' contém o nome do arquivo em bytes
        # 'addr' contém o endereço (IP, porta) do cliente

        filename = data.decode(CODE_PAGE).strip()  # Converte os bytes para texto
        print(f"Cliente {addr} pediu o arquivo: {filename}")

        # -----------------------------------------------------------
        # 2) Verifica se o arquivo existe no diretório do servidor
        # -----------------------------------------------------------
        if os.path.exists(filename):

            # Envia ao cliente uma confirmação dizendo que o arquivo existe
            sockServer.sendto(b"OK", addr)

            # -----------------------------------------------------------
            # 3) Abre o arquivo e envia em blocos (chunks)
            # -----------------------------------------------------------
            with open(filename, "rb") as f:  # "rb" = leitura binária
                while True:
                    chunk = f.read(BUFFER_SIZE)  # Lê parte do arquivo
                    if not chunk:  # Se não leu mais nada, chegou ao fim
                        break
                    sockServer.sendto(chunk, addr)  # Envia esse bloco ao cliente

            # -----------------------------------------------------------
            # 4) Envia marcador "EOF" para indicar fim do arquivo
            # -----------------------------------------------------------
            sockServer.sendto(b"EOF", addr)
            print(f"Arquivo {filename} enviado com sucesso.")

        else:
            # Caso o arquivo não exista, envia mensagem de erro ao cliente
            sockServer.sendto(b"ERRO: Arquivo nao encontrado", addr)

# Permite parar o servidor usando CTRL+C sem gerar erro
except KeyboardInterrupt:
    print("\nServidor encerrado.")

finally:
    # Fecha o socket quando o servidor for finalizado
    sockServer.close()

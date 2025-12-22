import socket

SERVER = "10.25.1.171"  # ou IP do servidor
PORT = 20000
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER, PORT))
        print("Conectado ao servidor de arquivos.")
        
        while True:
            cmd = input("Digite comando (LIST, GET <arquivo>, QUIT): ")
            client.sendall(cmd.encode())
            
            if cmd.startswith("GET "):
                filename = cmd.split(" ", 1)[1]
                with open("download_" + filename, "wb") as f:
                    while True:
                        data = client.recv(BUFFER_SIZE)
                        if not data or data.endswith(b"\n"):
                            break
                        f.write(data)
                print(f"Arquivo {filename} baixado com sucesso.")
            
            else:
                data = client.recv(BUFFER_SIZE).decode()
                print("Resposta:", data)
                
                if cmd == "QUIT":
                    break

if __name__ == "__main__":
    main()

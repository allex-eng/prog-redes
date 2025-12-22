import socket
import os

HOST = "10.25.1.171"
PORT = 20000
BUFFER_SIZE = 1024

def list_files():
    return "\n".join(os.listdir("."))

def send_file(conn, filename):
    if os.path.exists(filename):
        conn.sendall(b"OK\n")
        with open(filename, "rb") as f:
            while chunk := f.read(BUFFER_SIZE):
                conn.sendall(chunk)
    else:
        conn.sendall(b"ERROR: File not found\n")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Servidor escutando em {HOST}:{PORT}...")
        
        while True:
            conn, addr = server.accept()
            print(f"Conectado por {addr}")
            with conn:
                while True:
                    data = conn.recv(BUFFER_SIZE).decode().strip()
                    if not data:
                        break
                    print(f"Comando recebido: {data}")
                    
                    if data == "LIST":
                        conn.sendall(list_files().encode())
                    elif data.startswith("GET "):
                        filename = data.split(" ", 1)[1]
                        send_file(conn, filename)
                    elif data == "QUIT":
                        conn.sendall(b"Bye!\n")
                        break
                    else:
                        conn.sendall(b"Comando invalido\n")

if __name__ == "__main__":
    main()

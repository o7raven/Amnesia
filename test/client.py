import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send_data(self, data):
        while True:
            try:
                self.client.send(bytes(data, 'utf-8'))
                print("Data sent:", data)
                response = self.client.recv(1024).decode()
                print("Server response:", response)
                break
            except (ConnectionResetError, socket.error):
                print("The connection was closed by the server. Reconnecting...")
                self.client.connect((self.host, self.port))

if __name__ == "__main__":
    host = "localhost"
    port = 8080
    data = input("some data to send to the server")
    
    client = Client(host, port)
    client.send_data(data)

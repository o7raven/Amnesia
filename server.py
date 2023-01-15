
import logging
import socket

listeningPort = 8080

class Server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('localhost', self._port))

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, new_port):
        self._port = new_port
    
    @property
    def host(self):
        return self.host

    @port.setter
    def host(self, new_host):
        self._host = new_host

    @property
    def socket(self):
        return self._socket

    
    def connect(self):
        self.socket.listen()
        print(f"\nServer listening on {self.port}")
        logging.debug("\nServer successfully initialized!")
        print("\nServer trying to establish connection")
        while True:
            connection, adress = self.socket.accept()
            print(f"\nSuccessfully established connection with {adress}")
            logging.debug(f"Server has established connection with {adress}")
            try:
                while True:
                    data = connection.recv(1024).decode()
                    if not data:
                        break
                    print(f'Received data: {data}')
                    logging.debug(data)
                    connection.send(bytes("Data received", 'utf-8'))
            except (ConnectionResetError):
                print("Client has disconnected")


 
def Start():
    server = Server('localhost', listeningPort)
    server.connect()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='activity.log', format='Time: %(asctime)s | Key: %(message)s')
    Start()
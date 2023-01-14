from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import socket


hostName = "localhost"
serverPort = 80

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

if __name__ == "__main__":
    startServer()
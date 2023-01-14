![Logo](https://i.ibb.co/znvCGpk/linkedin-banner-image-1.png)
# Amnesia

This project is a keylogger server for educational purposes only. It is not intended for any malicious use and should only be used with the proper authorization.

## Getting Started

The keylogger consists of two main files: `server.py` and `client.py`</br>
`server.py` starts a listener and creates a website that runs on the LAN, where you can download `client.py`</br> 
`client.py` connects to the listener and establishes a connection</br>
Once the connection is established, every key pressed on the client machine will be sent to the `server.py` machine

### Prerequisites

- Python 3
- The following python modules:
  - sockets
  - logging
  - http.server

### Running the keylogger
1. Clone the repository with git `git clone https://github.com/o7raven/Encryption`
2. Then enter the directory `cd Encryption`
3. Download pip requirements `pip install -r requirements`
4. Start the server by running `python server.py`. This will start the listener and create a website running on your LAN
5. You can modify the files to fit your requirements
6. Let the victim download `client.py` in an executable obfuscated form from the website created by the server
7. Run `python client.py` on the client machine. This will connect to the listener and establish a connection

### Additional files

In addition to the main files, there are also two template files for the website: `index.html` and `styles.css`. These can help you to build the page and later convert to a single-line code using [lingojam](https://lingojam.com/TexttoOneLine)

## Note

The use of keyloggers without proper authorization is illegal and can lead to severe consequences. This project is for educational purposes only and should not be used for any illegal or malicious activities.

But if you decide to use it for illegal purposes, whatever happens to you is not my fault and I am not responsible for it, keep that in mind

Please contact the developer if you have any questions or issues:

Twitter: [@o7ravenxd](https://twitter.com/o7ravenxd)

## Author

- **Raven** - [o7ravenxd](https://github.com/o7raven)

## License

This project is licensed under the MIT License.
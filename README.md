![Logo](https://i.ibb.co/znvCGpk/linkedin-banner-image-1.png)
# Amnesia

This project is a keylogger server for educational purposes only. It is not intended for any malicious use and should only be used with the proper authorization.

## Getting Started

The keylogger consists of two main files: `server.py` and `client.py`</br>
`server.py` starts a listener and creates a website that runs on the LAN, where you can download `client.py`</br> 
`client.py` connects to the listener and establishes a connection</br>
Once the connection is established, every key pressed on the client machine will be sent to the `server.py` machine

There is also one additional file called `webserver.py`. Run this file if you want to host a website on your computer. With this your victim can download the keylogger from your site

### Prerequisites

- Python 3
- The following python modules:
  - sockets
  - logging
  - http.server
  - sys
  - pynput.keyboard

### Running the keylogger
1. Clone the repository with git `git clone https://github.com/o7raven/Amnesia`
2. Then enter the directory `cd Amnesia`
3. Download pip requirements `pip install -r requirements`
4. Start the server by running `python server.py`. This will start a listener
5. Start the webserver by running `python webserver.py`. This will create a fake website from which your victim can download the malware
6. You can modify the files to fit your requirements
7. Let the victim download `amnesia.py` in an executable obfuscated form from the website created by the `webserver.py`
8. Wait until your victim runs the executable file and establishes connection with your `server.py`

### Additional info

If you want to change the appearance of a web page or create a completely new one, insert your index.html into [lingojam](https://lingojam.com/TexttoOneLine) to make it single-row</br>

Don't forget to change the `hostName` and `host` if you want to try it on other people

Antivirus will detect `amnesia.py` as a keylogger. To make it undetectable, you have to compile it into .exe. You can use tools like pyinstaller or pyarmor

If you want your victim to download the malware from your website, you have to specify the file inside the `<a href=#></a>` tag

## Note

The use of keyloggers without proper authorization is illegal and can lead to severe consequences. This project is for educational purposes only and should not be used for any illegal or malicious activities.

But if you decide to use it for illegal purposes, whatever happens to you is not my fault and I am not responsible for it, keep that in mind

You have to modify the files to make it work in your environment, so keep in mind that it won't work outside of your computer if you don't do so


Please contact the developer if you have any questions or issues:

Twitter: [@o7ravenxd](https://twitter.com/o7ravenxd)

## Author

- **Raven** - [o7ravenxd](https://github.com/o7raven)

## License

This project is licensed under the MIT License.

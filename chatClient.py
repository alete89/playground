from ChatWindow import ChatWindow
from Usuario import Usuario
import RSAKeyHandle as rsa
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def receive(windo):
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            windo.plainTextEdit.appendPlainText(msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(windo, event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = windo.lineEdit.text()
    windo.lineEdit.setText("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        quit()


# ----Now comes the sockets part----
HOST = "localhost"  # input('Enter host: ')
PORT = 33000  # input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

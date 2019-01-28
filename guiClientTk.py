"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from ChatWindow import ChatWindow
import PyQt5
import sys
from functools import partial

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            top.plainTextEdit.appendPlainText(msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.text()
    my_msg.setText("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        app.exit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.setText("{quit}")
    send()

app = PyQt5.QtWidgets.QApplication(sys.argv)
top = ChatWindow()

messages_frame = top.plainTextEdit
my_msg = top.lineEdit  # For the messages to be sent.
my_msg.setText("Type your messages here.")
# Following will contain the messages.

send_button = top.pushButton


#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)
###
send_button.clicked.connect(send)
###
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

top.show()
sys.exit(app.exec_())
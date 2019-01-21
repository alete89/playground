import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import chatClient as chat
from threading import Thread
from functools import partial



class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Enviar")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        # signals and slots
        self.pushButton.clicked.connect(partial(chat.send,self))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ChatWindow()
    window.resize(500, 480)
    window.show()
    sys.exit(app.exec_())
    receive_thread = Thread(target=chat.receive(window))
    receive_thread.start()

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from Server import usuarios  # para pruebas


class UserList(QtWidgets.QWidget):
    def __init__(self, usuariosConectados=None):
        super().__init__()
        self.usuarioSeleccionado = None
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.listView = QtWidgets.QListView(self)
        self.listWidget = QtWidgets.QListWidget(self)
        self.verticalLayout.addWidget(self.listView)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("chatear")
        self.verticalLayout.addWidget(self.pushButton)

        # listView
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        model = QtGui.QStandardItemModel(self.listView)
        for usuario in usuariosConectados:
            item = QtGui.QStandardItem(usuario)
            model.appendRow(item)

        # listWidget
        for usuario in usuariosConectados:
            self.listWidget.addItem(
                f"{usuario['username']}", userData=usuario["key"]
            )

        self.listView.setModel(model)
        # signals and slots
        self.pushButton.clicked.connect(self.abrirChat)

    def abrirChat(self):
        self.listView.selectionModel


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UserList(["pedro", "juan", "carlos"])
    window.resize(320, 480)
    window.show()
    sys.exit(app.exec_())

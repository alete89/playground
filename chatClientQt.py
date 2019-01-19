import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore


class MainWindow(QtWidgets.QWidget):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 480)
    window.show()
    sys.exit(app.exec_())

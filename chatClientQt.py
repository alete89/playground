import sys
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.vlayout = QtWidgets.QVBoxLayout()
        
        self.historial = QtWidgets.QTextEdit()
        self.vlayout.addWidget(self.historial)
        self.input = QtWidgets.QTextEdit()
        self.vlayout.addWidget(self.input)
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
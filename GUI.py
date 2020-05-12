import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from frame import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Gui definition
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        # Button clicked
        self.StartButton.clicked.connect(self.game())
        self.EndButton.clicked.connect(lambda: app.exit())

    def game(self):
        self.frame.setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
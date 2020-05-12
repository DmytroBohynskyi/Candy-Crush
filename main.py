""" Candy Crush

"""
from __future__ import barry_as_FLUFL

__version__ = '0.2'
__author__ = 'Dmytro Bohynskyi'

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt
from GUI import Ui_MainWindow
from modules import View, User

# Static variables
KEY_user_1 = {
    Qt.Key_Q: "q",
    Qt.Key_A: "a",
    Qt.Key_Z: "z",
    Qt.Key_E: "e",
    Qt.Key_D: "d",
    Qt.Key_C: "c",
    Qt.Key_S: "s",
}

KEY_user_2 = {
    Qt.Key_7: "q",
    Qt.Key_4: "a",
    Qt.Key_1: "z",
    Qt.Key_9: "e",
    Qt.Key_6: "d",
    Qt.Key_3: "c",
    Qt.Key_5: "s",
}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Gui definition
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        # definition of variables
        self.window = None  # field gor hexagon
        self.modification = True  # change of position hexagon
        self.user_1 = None  # first user
        self.user_2 = None  # second user

        # Button clicked
        self.StartButton.clicked.connect(lambda: self.game())  # start of single player mode
        self.TwoGameButton.clicked.connect(lambda: self.game(hot_sit=True))  # start of hot_sit player mode
        self.EndButton.clicked.connect(lambda: app.exit())  # closes the program

    def game(self, hot_sit=False):
        """
        this function opens game window and close start window.
        Create class object View and User
        :param hot_sit:
        :return: None
        """
        self.frame.setVisible(False)  # close start window
        self.start_frame.setVisible(True)  # open game window
        self.window = View()  # Create new windows
        self.user_1 = User()  # Create new user
        self.user_2 = User() if hot_sit else None  # Create new user
        self.print_view()  # hexagon show

    def print_view(self):
        x, y = self.window.agents.shape
        text = ""
        for y_ in range(y):
            text += "<font> .</font>" if y_ % 2 else "<font>    </font>"
            for x_, agent in enumerate(self.window.agents[:, y_]):
                if x > x_ + 1 and y > y_ + 1:
                    self.window.look_for((x_, y_))  # we are looking for three identical agents
                if self.user_1 == (x_, y_) or self.user_2 == (x_, y_):
                    text += f'<font color=#{agent.type}  >⬡</font>'  # position user_1 and user_2
                else:
                    text += f'<font color=#{agent.type}  >⬢</font>'  # hexagon
        self.textEdit.setText(text)

    def keyPressEvent(self, event):
        """

        :param event:
        :return: None
        """
        if event.key() in KEY_user_1 and self.window and self.user_1:
            p = KEY_user_1.get(event.key())  # position
            self.step(self.user_1, self.user_2, p)  # modification
        elif event.key() in KEY_user_2 and self.window and self.user_2:
            p = KEY_user_2.get(event.key())
            self.step(self.user_2, self.user_1, p)  # modification

    def step(self, user, opponent, p):
        if p == 's':
            self.modification = False
            if opponent is not None:
                opponent.act = False
        else:
            self.window.algorithm(user.position, p) if not self.modification else None
            user.algorithm(p)
            self.modification = True
            if opponent is not None:
                opponent.act = True

        self.print_view()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

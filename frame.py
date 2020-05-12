from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(533, 662)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 511, 611))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 70, 451, 421))
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"font: 48pt \"Tempus Sans ITC\";")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.StartButton = QPushButton(self.frame)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
                                       "font: 75 20pt \"Times New Roman\";")

        self.verticalLayout.addWidget(self.StartButton)

        self.NewGameButton = QPushButton(self.frame)
        self.NewGameButton.setObjectName(u"NewGameButton")
        self.NewGameButton.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
                                         "font: 75 15pt \"Times New Roman\";")

        self.verticalLayout.addWidget(self.NewGameButton)

        self.TwoGameButton = QPushButton(self.frame)
        self.TwoGameButton.setObjectName(u"TwoGameButton")
        self.TwoGameButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
                                         "font: 75 15pt \"Times New Roman\";")

        self.verticalLayout.addWidget(self.TwoGameButton)

        self.EndButton = QPushButton(self.frame)
        self.EndButton.setObjectName(u"EndButton")
        self.EndButton.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
                                     "font: 75 15pt \"Times New Roman\";")

        self.verticalLayout.addWidget(self.EndButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 533, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Candy Crush", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.NewGameButton.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.TwoGameButton.setText(QCoreApplication.translate("MainWindow", u"Hot-seat Game", None))
        self.EndButton.setText(QCoreApplication.translate("MainWindow", u"End", None))
    # retranslateUi

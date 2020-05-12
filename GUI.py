""" Candy Crush

"""
from __future__ import barry_as_FLUFL

__version__ = '0.2'
__author__ = 'Dmytro Bohynskyi'

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
        # Centralwidget Definition
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # start_frame Definition
        self.start_frame = QWidget(self.centralwidget)
        self.start_frame.setObjectName(u"start_frame")
        self.start_frame.setGeometry(QRect(-10, -10, 511, 611))
        self.start_frame.setVisible(False)

        # textEdit Definition
        self.textEdit = QTextEdit(self.start_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 170, 350, 500))
        self.textEdit.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";")
        self.textEdit.setReadOnly(True)

        # frame Definition
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 70, 451, 421))

        # verticalLayout Definition
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # label Definition
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"font: 48pt \"Tempus Sans ITC\";")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        # label_2 Definition
        self.label_2 = QLabel(self.start_frame)
        self.label_2.setGeometry(QRect(10, 10, 510, 100))
        self.label_2.setObjectName(u"label")
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setStyleSheet(u"font: 48pt \"Tempus Sans ITC\";")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        # StartButton Definition
        self.StartButton = QPushButton(self.frame)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
                                       "font: 75 20pt \"Times New Roman\";")
        self.verticalLayout.addWidget(self.StartButton)

        # NewGameButton Definition
        self.NewGameButton = QPushButton(self.frame)
        self.NewGameButton.setObjectName(u"NewGameButton")
        self.NewGameButton.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
                                         "font: 75 15pt \"Times New Roman\";")
        self.verticalLayout.addWidget(self.NewGameButton)

        # TwoGameButton Definition
        self.TwoGameButton = QPushButton(self.frame)
        self.TwoGameButton.setObjectName(u"TwoGameButton")
        self.TwoGameButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
                                         "font: 75 15pt \"Times New Roman\";")
        self.verticalLayout.addWidget(self.TwoGameButton)

        # EndButton Definition
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Candy Crush", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.NewGameButton.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.TwoGameButton.setText(QCoreApplication.translate("MainWindow", u"Hot-seat Game", None))
        self.EndButton.setText(QCoreApplication.translate("MainWindow", u"End", None))

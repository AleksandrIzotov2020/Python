# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(524, 868)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message_box = QPlainTextEdit(self.centralwidget)
        self.message_box.setObjectName(u"message_box")
        self.message_box.setReadOnly(True)

        self.verticalLayout.addWidget(self.message_box)

        self.message_input = QLineEdit(self.centralwidget)
        self.message_input.setObjectName(u"message_input")

        self.verticalLayout.addWidget(self.message_input)

        self.message_button = QPushButton(self.centralwidget)
        self.message_button.setObjectName(u"message_button")

        self.verticalLayout.addWidget(self.message_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.message_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Connecting...", None))
        self.message_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type youe message here", None))
        self.message_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi


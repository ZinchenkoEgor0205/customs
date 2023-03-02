# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QPushButton, QSizePolicy,
                               QWidget, QDialog, QDialogButtonBox, QVBoxLayout, QLabel)

class Ui_Welcome_interface(object):
    def setupUi(self, Welcome_interface):
        if not Welcome_interface.objectName():
            Welcome_interface.setObjectName(u"Welcome_interface")
        Welcome_interface.resize(375, 261)
        self.fill_btn = QPushButton(Welcome_interface)
        self.fill_btn.setObjectName(u"fill_btn")
        self.fill_btn.setEnabled(True)
        self.fill_btn.setGeometry(QRect(90, 150, 181, 31))
        self.fill_btn.setCheckable(True)
        self.form_choice = QComboBox(Welcome_interface)
        self.form_choice.addItem("")
        self.form_choice.setObjectName(u"form_choice")
        self.form_choice.setGeometry(QRect(90, 90, 181, 22))

        self.retranslateUi(Welcome_interface)

        QMetaObject.connectSlotsByName(Welcome_interface)
    # setupUi

    def retranslateUi(self, Welcome_interface):
        Welcome_interface.setWindowTitle(QCoreApplication.translate("Welcome_interface", u"Form", None))
        self.fill_btn.setText(QCoreApplication.translate("Welcome_interface", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.form_choice.setItemText(0, QCoreApplication.translate("Welcome_interface", u"18.37", None))

    # retranslateUi

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Внимание")
        self.layout = QVBoxLayout()
        self.message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(self.message)
        self.setLayout(self.layout)
        QBtn = QDialogButtonBox.Ok
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget, QDialog, QDialogButtonBox, QVBoxLayout,
                               QLabel)

class Ui_Interface(object):
    def setupUi(self, Interface):
        if not Interface.objectName():
            Interface.setObjectName(u"Interface")
        Interface.resize(497, 261)
        self.fill_btn = QPushButton(Interface)
        self.fill_btn.setObjectName(u"fill_btn")
        self.fill_btn.setEnabled(True)
        self.fill_btn.setGeometry(QRect(160, 190, 161, 31))
        self.fill_btn.setCheckable(True)

        self.retranslateUi(Interface)

        QMetaObject.connectSlotsByName(Interface)
    # setupUi

    def retranslateUi(self, Interface):
        Interface.setWindowTitle(QCoreApplication.translate("Interface", u"Form", None))
        self.fill_btn.setText(QCoreApplication.translate("Interface", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
    # retranslateUi

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Внимание")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Не все окна заполнены корректно")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
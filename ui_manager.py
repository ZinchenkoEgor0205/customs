import sys

from PySide6.QtWidgets import QApplication, QDialog
from interface import Ui_Interface
from administrative_18_37.interface_form import Ui_Form
from data import *
from administrative_18_37.ui_18_37 import Form

class Window(QDialog, Ui_Interface):
    """Main window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.fill_btn.toggled.connect(self.fill_btn_clicked)

    def fill_btn_clicked(self):
        if self.fill_btn.isChecked():
            form.show()
        else:
            form.hide()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.setWindowTitle('customs')
    w.show()
    form = Form()
    form.setWindowTitle('Форма')
    app.exec()

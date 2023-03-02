import sys

from PySide6.QtWidgets import QApplication, QDialog
from interface_welcome_screen import Ui_Welcome_interface
from administrative_18_37.ui_18_37 import Form_18_37

class Window(QDialog, Ui_Welcome_interface):
    """Main window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.fill_btn.toggled.connect(self.fill_btn_clicked)

    def fill_btn_clicked(self):
        if self.fill_btn.isChecked():
            self.form_selector().show()
        else:
            self.form_selector().hide()


    def form_selector(self):
        ARTICLES = {
            '18.37': form_18_37,
        }
        self.choice = self.form_choice.currentText()
        return ARTICLES[self.choice]






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.setWindowTitle('customs')
    main_window.show()
    form_18_37 = Form_18_37()
    form_18_37.setWindowTitle('Форма_18_37')
    app.exec()

from PySide6.QtWidgets import QApplication, QDialog
from interface import Ui_Interface, CustomDialog
from administrative_18_37.interface_form import Ui_Form
from data import *
from administrative_18_37.doc_editor_18_37 import *

class Form(QDialog, Ui_Form):

    def __init__(self):
        """Initializer."""
        super().__init__()
        self.criminal = Criminal
        self.inspector = Inspector
        self.mixed_data = MixedData
        self.setupUi(self)

        self.test(True) #Переключи на False, чтоб отключить тест

        self.process_btn.clicked.connect(self.process_btn_clicked)
        self.fill_btn.clicked.connect(self.fill_btn_clicked)

    def fill_btn_clicked(self):
        try:
            self.criminal.place_of_living = self.criminal_place_of_living_field.toPlainText()
            self.criminal.name = self.criminal_name_field.toPlainText()
            self.criminal.surname = self.criminal_surname_field.toPlainText()
            self.criminal.last_name = self.criminal_last_name_field.toPlainText()
            self.criminal.citizenship = self.criminal_citizenship_field.toPlainText()

            self.inspector.name = self.inspector_name_field.toPlainText()
            self.inspector.surname = self.inspector_surname_field.toPlainText()
            self.inspector.last_name = self.inspector_last_name_field.toPlainText()

            self.criminal.place_of_living_rp = self.criminal.place_of_living_to_rp(self.criminal)
            self.criminal.citizenship_rp = self.criminal.citizenship_to_rp(self.criminal)
            self.criminal.n_s_l_rp = self.criminal.name_surname_last_name_to_rp(self.criminal)
            self.inspector.n_s_l_rp = self.inspector.name_surname_last_name_to_rp(self.inspector)

            self.criminal_citizenship_rp_field.setText(self.criminal.citizenship_rp)
            self.criminal_n_s_l_rp_field.setText(self.criminal.n_s_l_rp)
            self.inspector_n_s_l_rp_field.setText(self.inspector.n_s_l_rp)
            # self.criminal_place_of_living_rp_field.setText(self.criminal.place_of_living_rp)
            self.mass_overload_field.setValue((self.mass_field.value() / self.max_mass_field.value() - 1) * 100)
            self.criminal_citizenship_rp_field.setEnabled(True)
            self.criminal_n_s_l_rp_field.setEnabled(True)
            self.inspector_n_s_l_rp_field.setEnabled(True)
            self.process_btn.setEnabled(True)
        except Exception as err:
            dlg = CustomDialog(self)
            dlg.exec_()

    def process_btn_clicked(self):
        self.criminal.place_of_living_rp = self.criminal_place_of_living_field.toPlainText()
        self.criminal.citizenship_rp = self.criminal_citizenship_rp_field.toPlainText()
        self.criminal.n_s_l_rp = self.criminal_n_s_l_rp_field.toPlainText()
        self.inspector.n_s_l_rp = self.inspector_n_s_l_rp_field.toPlainText()

        self.criminal.date_of_birth = self.criminal_date_of_birth_field.text()
        self.criminal.place_of_birth = self.criminal_place_of_birth_field.toPlainText()
        self.criminal.phone = self.criminal_phone_field.toPlainText()
        self.criminal.education = self.criminal_education_field.currentText()
        self.criminal.passport_n = self.criminal_passport_n_field.toPlainText()
        self.criminal.passport_date = self.criminal_passport_date_of_providing_field.text()
        self.criminal.passport_provider = self.criminal_passport_provider_field.toPlainText()
        self.criminal.passport_id = self.criminal_passport_id_field.toPlainText()
        self.criminal.firm = self.criminal_firm_name_field.toPlainText()
        self.criminal.firm_address = self.criminal_firm_address_field.toPlainText()



        self.inspector.position = self.inspector_position_field.toPlainText()
        self.inspector.department_n = self.inspector_department_field.toPlainText()
        self.mixed_data.control_date = self.date_of_control_field.text().split()[0]
        self.mixed_data.control_hour = self.date_of_control_field.text().split()[1].split(':')[0]
        self.mixed_data.control_minute = self.date_of_control_field.text().split()[1].split(':')[1]
        self.mixed_data.truck_model = self.truck_model_field.toPlainText()
        self.mixed_data.truck_n = self.truck_n_field.toPlainText()
        self.mixed_data.trailer_model = self.trailer_model_field.toPlainText()
        self.mixed_data.trailer_n = self.trailer_n_field.toPlainText()
        self.mixed_data.suspension_tp = self.truck_suspension_tp_field.toPlainText()
        self.mixed_data.shaft_n = self.shaft_n_field.currentText()
        self.mixed_data.mass = self.mass_field.text()
        self.mixed_data.max_mass = self.max_mass_field.text()
        self.mixed_data.max_road_mass = self.max_road_mass_field.text()
        self.mixed_data.mass_overload = self.mass_overload_field.text()
        self.mixed_data.weight_model = self.weight_model_field.toPlainText()
        self.mixed_data.weight_check_n = self.weight_check_n_field.toPlainText()
        self.mixed_data.weight_check_date = self.weight_check_date_field.text()
        self.mixed_data.weight_check_expiration_date = self.weight_check_date_expiration_field.text()
        self.mixed_data.protocol_n = self.protocol_n_field.toPlainText()
        self.mixed_data.good_name = self.good_name_field.toPlainText()
        self.mixed_data.departure_date = self.departure_date_field.text()
        self.mixed_data.arrival_date = self.arrival_date_field.text()
        self.mixed_data.route_name = self.route_name_field.toPlainText()

        doc_process(criminal=self.criminal, inspector=self.inspector, mixed_data=self.mixed_data)

    def test(self, flag):
        if flag:
            self.criminal_name_field.setText('Иван')
            self.criminal_surname_field.setText('Иванов')
            self.criminal_last_name_field.setText('Иванович')
            self.criminal_place_of_birth_field.setText('Республика Беларусь, г. Минск')
            self.criminal_place_of_living_field.setText('Республика Беларусь, г. Минск, ул. Ленина, д.1, кв. 50')
            self.criminal_phone_field.setText('88005553535')
            self.criminal_passport_n_field.setText('HB875212')
            self.criminal_passport_id_field.setText('1546136623287')
            self.criminal_passport_provider_field.setText('Фрунзенский РОВД г. Минска')
            self.criminal_citizenship_field.setText('Республика Беларусь')
            self.criminal_firm_name_field.setText('Grand cargo')
            self.criminal_firm_address_field.setText('Litva, Vilnus, Electriskes, 54')
            self.inspector_name_field.setText('Егор')
            self.inspector_surname_field.setText('Зинченко')
            self.inspector_last_name_field.setText('Дмитриевич')
            self.inspector_position_field.setText('Инспектор')
            self.inspector_department_field.setText('2')
            self.truck_n_field.setText('tru152')
            self.truck_model_field.setText('scania')
            self.trailer_n_field.setText('yt315')
            self.trailer_model_field.setText('schmitz')
            self.truck_suspension_tp_field.setText('пневматической повеской')
            self.weight_model_field.setText('ak64856')
            self.weight_check_n_field.setText('874653052')
            self.protocol_n_field.setText('23477565')
            self.good_name_field.setText('керамические изделия')
            self.route_name_field.setText('Лида-Бенякони-1')

import docx




def doc_process(criminal, inspector, mixed_data):
    criminal.initials = criminal.name_last_name_to_initials(criminal)
    inspector.initials = inspector.name_last_name_to_initials(inspector)
    FIELDS = {
        'FieldRPCriminalFio': criminal.n_s_l_rp,
        'FieldInitCriminalFio': criminal.initials,
        'FieldCriminalFio': f'{criminal.name} {criminal.surname} {criminal.last_name}',
        'FieldRPInspectorFio': inspector.n_s_l_rp,
        'FieldInitInspectorFio': inspector.initials,
        'FieldInspectorFio': f'{inspector.name} {inspector.surname} {inspector.last_name}',
        'FieldPosition': inspector.position,
        'FieldDepartmentN': inspector.department_n,
        'FieldDateOfBirth': criminal.date_of_birth,
        'FieldPlaceOfBirth': criminal.place_of_birth,
        'FieldPlaceOfLiving': criminal.place_of_living,
        'FieldRPPlaceOfLiving': criminal.place_of_living_rp,
        'FieldMobile': criminal.phone,
        'FieldEducation': criminal.education,
        'FieldPassportN': criminal.passport_n,
        'FieldDateOfPassportProviding': criminal.passport_date,
        'FieldTPPassportProvider': criminal.passport_provider,
        'FieldPassportID': criminal.passport_id,
        'FieldCitizenship': criminal.citizenship,
        'FieldRPCitizenship': criminal.citizenship_rp,
        'FieldFirmName': criminal.firm,
        'FieldFirmAddress': criminal.firm_address,
        'FieldDate': mixed_data.control_date,
        'FieldTimeHour': mixed_data.control_hour,
        'FieldTimeMinute': mixed_data.control_minute,
        'FieldTruckN': mixed_data.truck_n,
        'FieldTruckMark': mixed_data.truck_model,
        'FieldTrailerN': mixed_data.trailer_n,
        'FieldTrailerMark': mixed_data.trailer_model,
        'FieldShaftN': mixed_data.shaft_n,
        'FieldProtokolN': mixed_data.protocol_n,
        'FieldGoodName': mixed_data.good_name,
        'FieldMaxMass': mixed_data.max_mass,
        'FieldTravelDateStart': mixed_data.departure_date,
        'FieldTravelDateFinish': mixed_data.arrival_date,
        'FieldRouteName': mixed_data.route_name,
        'FieldTPSuspensionData': mixed_data.suspension_tp,
        'FieldMass': mixed_data.mass,
        'FieldRoadMaxMass': mixed_data.max_road_mass,
        'FieldPercentage': mixed_data.mass_overload,
        'FieldWeightModel': mixed_data.weight_model,
        'FieldCheckN': mixed_data.weight_check_n,
        'FieldCheckDate': mixed_data.weight_check_date,
        'FieldCheckExpirationDate': mixed_data.weight_check_expiration_date,

    }
    doc = docx.Document('administrative_18_37/raw_18_37.docx')
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if 'Field' in run.text:
                print(run.text)
                for key, value in FIELDS.items():
                    if key == run.text.strip() or key == run.text.strip()[:-1]:
                        run.text = run.text.replace(key, value)
                    elif len(run.text.strip().split()) >= 2:
                        for i in range(len(run.text.strip().split())):
                            if key == run.text.strip().split()[i] or key == run.text.strip().split()[:-1]:
                                run.text = run.text.replace(key, value)



    doc.save('probe_done.docx')
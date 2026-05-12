####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
Sex: Enumeration = Enumeration(
    name="Sex",
    literals={
            
    }
)

MaritalStatus: Enumeration = Enumeration(
    name="MaritalStatus",
    literals={
            
    }
)

Relationship: Enumeration = Enumeration(
    name="Relationship",
    literals={
            
    }
)

Position: Enumeration = Enumeration(
    name="Position",
    literals={
            
    }
)

TypeContract: Enumeration = Enumeration(
    name="TypeContract",
    literals={
            
    }
)

SalaryPayment: Enumeration = Enumeration(
    name="SalaryPayment",
    literals={
            
    }
)

SupplyType: Enumeration = Enumeration(
    name="SupplyType",
    literals={
            
    }
)

Administration: Enumeration = Enumeration(
    name="Administration",
    literals={
            
    }
)

# Classes
Personnel_Officer_Actor = Class(name="Personnel_Officer_Actor")
_Component = Class(name="_Component")
Staff_Actor = Class(name="Staff_Actor")
Charge_Nurse_Actor = Class(name="Charge_Nurse_Actor")
Person_Actor = Class(name="Person_Actor")
Medical_Director_Actor = Class(name="Medical_Director_Actor")
Patient_Actor = Class(name="Patient_Actor")
Person = Class(name="Person")
Patient = Class(name="Patient")
Staff = Class(name="Staff")
NextOfKind = Class(name="NextOfKind")
LocalDoctor = Class(name="LocalDoctor")
Qualification = Class(name="Qualification")
WorkExperience = Class(name="WorkExperience")
EmploymentContract = Class(name="EmploymentContract")
MedicalDirector = Class(name="MedicalDirector")
PersonnelOfficer = Class(name="PersonnelOfficer")
ChargeNurse = Class(name="ChargeNurse")
RegularDoctor = Class(name="RegularDoctor")
Ward = Class(name="Ward")
Bed = Class(name="Bed")
Requisition = Class(name="Requisition")
Supply = Class(name="Supply")
Surgical_NonSurgical = Class(name="Surgical_NonSurgical")
Pharmaceutical = Class(name="Pharmaceutical")
Supplier = Class(name="Supplier")
WaitingList = Class(name="WaitingList")
InPatient = Class(name="InPatient")
Appointment = Class(name="Appointment")
OutPatient = Class(name="OutPatient")
Medication = Class(name="Medication")
_Component1 = Class(name="_Component1")
Payee_Actor = Class(name="Payee_Actor")
Accountant_Actor = Class(name="Accountant_Actor")
Maintain_ward_s_Patients_external = Class(name="Maintain_ward_s_Patients_external")
Maintian_Patients__medication_external = Class(name="Maintian_Patients__medication_external")
of_Patients__medication_external = Class(name="of_Patients__medication_external")
of_Patients_in_wards_external = Class(name="of_Patients_in_wards_external")
of_Patients_on_waiting_list_external = Class(name="of_Patients_on_waiting_list_external")
Maintain_resources_external = Class(name="Maintain_resources_external")
Maintain_Staff_external = Class(name="Maintain_Staff_external")
Search_Staff_external = Class(name="Search_Staff_external")
of_Ward_s_Staff_external = Class(name="of_Ward_s_Staff_external")
Maintain_Patients_referred_to_the_hospital_external = Class(name="Maintain_Patients_referred_to_the_hospital_external")
Maintain_Patients_referred_to_the_out_patients_clinic_external = Class(name="Maintain_Patients_referred_to_the_out_patients_clinic_external")
of_Patients_referred_to_the_out_patient_clinic_external = Class(name="of_Patients_referred_to_the_out_patient_clinic_external")
Register_Patient_payment_external = Class(name="Register_Patient_payment_external")
of_Monthly_profit_external = Class(name="of_Monthly_profit_external")
of_Services_Improvement_external = Class(name="of_Services_Improvement_external")
Maintain_ward_s_supplies_external = Class(name="Maintain_ward_s_supplies_external")
of_ward_s_supplies_external = Class(name="of_ward_s_supplies_external")
Maintain_suppliers_external = Class(name="Maintain_suppliers_external")
Set_staff_weekly_Rota_external = Class(name="Set_staff_weekly_Rota_external")
Maintain_next_of_kind_details_external = Class(name="Maintain_next_of_kind_details_external")
Create_Patient_appointment_external = Class(name="Create_Patient_appointment_external")
Search_Patient_external = Class(name="Search_Patient_external")
Authorise_Service_Improvement_Budget_external = Class(name="Authorise_Service_Improvement_Budget_external")
Generate_Staff_s_Payroll_external = Class(name="Generate_Staff_s_Payroll_external")

# Personnel_Officer_Actor class attributes and methods

# _Component class attributes and methods

# Staff_Actor class attributes and methods

# Charge_Nurse_Actor class attributes and methods

# Person_Actor class attributes and methods

# Medical_Director_Actor class attributes and methods

# Patient_Actor class attributes and methods

# Person class attributes and methods
Person_first_name: Property = Property(name="first_name", type=StringType)
Person_last_name: Property = Property(name="last_name", type=StringType)
Person_address: Property = Property(name="address", type=StringType)
Person_telephone: Property = Property(name="telephone", type=StringType)
Person_date_of_birth: Property = Property(name="date_of_birth", type=DateType)
Person_sex: Property = Property(name="sex", type=Sex)
Person.attributes={Person_address, Person_last_name, Person_telephone, Person_date_of_birth, Person_sex, Person_first_name}

# Patient class attributes and methods
Patient_num: Property = Property(name="num", type=IntegerType)
Patient_marital_status: Property = Property(name="marital_status", type=MaritalStatus)
Patient_next_of_kind: Property = Property(name="next_of_kind", type=NextOfKind)
Patient_local_doctor: Property = Property(name="local_doctor", type=LocalDoctor)
Patient.attributes={Patient_num, Patient_next_of_kind, Patient_marital_status, Patient_local_doctor}

# Staff class attributes and methods
Staff_num: Property = Property(name="num", type=IntegerType)
Staff_nin: Property = Property(name="nin", type=IntegerType)
Staff_position: Property = Property(name="position", type=Position)
Staff_current_salary: Property = Property(name="current_salary", type=FloatType)
Staff_salary_scale: Property = Property(name="salary_scale", type=FloatType)
Staff_qualification: Property = Property(name="qualification", type=Qualification)
Staff_work_experience: Property = Property(name="work_experience", type=WorkExperience)
Staff_employment_contract: Property = Property(name="employment_contract", type=EmploymentContract)
Staff.attributes={Staff_qualification, Staff_current_salary, Staff_num, Staff_employment_contract, Staff_salary_scale, Staff_nin, Staff_work_experience, Staff_position}

# NextOfKind class attributes and methods
NextOfKind_relationship: Property = Property(name="relationship", type=Relationship)
NextOfKind.attributes={NextOfKind_relationship}

# LocalDoctor class attributes and methods
LocalDoctor_clinic_number: Property = Property(name="clinic_number", type=IntegerType)
LocalDoctor.attributes={LocalDoctor_clinic_number}

# Qualification class attributes and methods
Qualification_date: Property = Property(name="date", type=DateType)
Qualification_type: Property = Property(name="type", type=StringType)
Qualification_institution_name: Property = Property(name="institution_name", type=StringType)
Qualification.attributes={Qualification_type, Qualification_date, Qualification_institution_name}

# WorkExperience class attributes and methods
WorkExperience_organization_name: Property = Property(name="organization_name", type=StringType)
WorkExperience_position: Property = Property(name="position", type=StringType)
WorkExperience_start_date: Property = Property(name="start_date", type=DateType)
WorkExperience_finish_date: Property = Property(name="finish_date", type=DateType)
WorkExperience.attributes={WorkExperience_start_date, WorkExperience_position, WorkExperience_finish_date, WorkExperience_organization_name}

# EmploymentContract class attributes and methods
EmploymentContract_number_hours_per_week: Property = Property(name="number_hours_per_week", type=IntegerType)
EmploymentContract_type_contract: Property = Property(name="type_contract", type=TypeContract)
EmploymentContract_salary_payment: Property = Property(name="salary_payment", type=SalaryPayment)
EmploymentContract.attributes={EmploymentContract_salary_payment, EmploymentContract_number_hours_per_week, EmploymentContract_type_contract}

# MedicalDirector class attributes and methods

# PersonnelOfficer class attributes and methods

# ChargeNurse class attributes and methods

# RegularDoctor class attributes and methods

# Ward class attributes and methods
Ward_num: Property = Property(name="num", type=IntegerType)
Ward_name: Property = Property(name="name", type=StringType)
Ward_location: Property = Property(name="location", type=StringType)
Ward_telephone_extension: Property = Property(name="telephone_extension", type=IntegerType)
Ward_responsable: Property = Property(name="responsable", type=ChargeNurse)
Ward_staff: Property = Property(name="staff", type=RegularDoctor)
Ward.attributes={Ward_location, Ward_num, Ward_name, Ward_responsable, Ward_telephone_extension, Ward_staff}

# Bed class attributes and methods
Bed_num: Property = Property(name="num", type=IntegerType)
Bed.attributes={Bed_num}

# Requisition class attributes and methods
Requisition_num: Property = Property(name="num", type=IntegerType)
Requisition_responsable: Property = Property(name="responsable", type=ChargeNurse)
Requisition_ward: Property = Property(name="ward", type=Ward)
Requisition_supply: Property = Property(name="supply", type=Supply)
Requisition_quantity_required: Property = Property(name="quantity_required", type=IntegerType)
Requisition_date_ordered: Property = Property(name="date_ordered", type=DateType)
Requisition_date_delivered: Property = Property(name="date_delivered", type=DateType)
Requisition.attributes={Requisition_quantity_required, Requisition_responsable, Requisition_ward, Requisition_date_delivered, Requisition_num, Requisition_date_ordered, Requisition_supply}

# Supply class attributes and methods
Supply_num: Property = Property(name="num", type=IntegerType)
Supply_name: Property = Property(name="name", type=StringType)
Supply_description: Property = Property(name="description", type=StringType)
Supply_stock: Property = Property(name="stock", type=IntegerType)
Supply_reorder_level: Property = Property(name="reorder_level", type=IntegerType)
Supply_cost_per_unit: Property = Property(name="cost_per_unit", type=FloatType)
Supply.attributes={Supply_name, Supply_num, Supply_stock, Supply_cost_per_unit, Supply_reorder_level, Supply_description}

# Surgical_NonSurgical class attributes and methods
Surgical_NonSurgical_supply_type: Property = Property(name="supply_type", type=SupplyType)
Surgical_NonSurgical.attributes={Surgical_NonSurgical_supply_type}

# Pharmaceutical class attributes and methods
Pharmaceutical_dosage: Property = Property(name="dosage", type=StringType)
Pharmaceutical_method_of_administration: Property = Property(name="method_of_administration", type=StringType)
Pharmaceutical.attributes={Pharmaceutical_dosage, Pharmaceutical_method_of_administration}

# Supplier class attributes and methods
Supplier_num: Property = Property(name="num", type=StringType)
Supplier_fax: Property = Property(name="fax", type=StringType)
Supplier.attributes={Supplier_num, Supplier_fax}

# WaitingList class attributes and methods
WaitingList_patient: Property = Property(name="patient", type=Patient_Actor)
WaitingList_ward_required: Property = Property(name="ward_required", type=Ward)
WaitingList_date: Property = Property(name="date", type=DateType)
WaitingList.attributes={WaitingList_date, WaitingList_ward_required, WaitingList_patient}

# InPatient class attributes and methods
InPatient_patient: Property = Property(name="patient", type=Patient_Actor)
InPatient_ward_required: Property = Property(name="ward_required", type=Ward)
InPatient_duration: Property = Property(name="duration", type=IntegerType)
InPatient_date_place: Property = Property(name="date_place", type=DateType)
InPatient_date_expected_leave: Property = Property(name="date_expected_leave", type=DateType)
InPatient_date_actual_leave: Property = Property(name="date_actual_leave", type=DateType)
InPatient_bed: Property = Property(name="bed", type=Bed)
InPatient.attributes={InPatient_patient, InPatient_date_place, InPatient_bed, InPatient_date_expected_leave, InPatient_ward_required, InPatient_date_actual_leave, InPatient_duration}

# Appointment class attributes and methods
Appointment_num: Property = Property(name="num", type=IntegerType)
Appointment_patient: Property = Property(name="patient", type=Patient_Actor)
Appointment_doctor: Property = Property(name="doctor", type=RegularDoctor)
Appointment_date: Property = Property(name="date", type=DateType)
Appointment_room: Property = Property(name="room", type=StringType)
Appointment.attributes={Appointment_patient, Appointment_room, Appointment_date, Appointment_num, Appointment_doctor}

# OutPatient class attributes and methods
OutPatient_patient: Property = Property(name="patient", type=Patient_Actor)
OutPatient_date: Property = Property(name="date", type=DateType)
OutPatient_location: Property = Property(name="location", type=StringType)
OutPatient.attributes={OutPatient_date, OutPatient_location, OutPatient_patient}

# Medication class attributes and methods
Medication_patient: Property = Property(name="patient", type=Patient_Actor)
Medication_drug: Property = Property(name="drug", type=Pharmaceutical)
Medication_units_per_day: Property = Property(name="units_per_day", type=IntegerType)
Medication_administration: Property = Property(name="administration", type=Administration)
Medication_start_date: Property = Property(name="start_date", type=DateType)
Medication_finish_date: Property = Property(name="finish_date", type=DateType)
Medication.attributes={Medication_drug, Medication_start_date, Medication_patient, Medication_units_per_day, Medication_finish_date, Medication_administration}

# _Component1 class attributes and methods

# Payee_Actor class attributes and methods

# Accountant_Actor class attributes and methods

# Maintain_ward_s_Patients_external class attributes and methods

# Maintian_Patients__medication_external class attributes and methods

# of_Patients__medication_external class attributes and methods

# of_Patients_in_wards_external class attributes and methods

# of_Patients_on_waiting_list_external class attributes and methods

# Maintain_resources_external class attributes and methods

# Maintain_Staff_external class attributes and methods

# Search_Staff_external class attributes and methods

# of_Ward_s_Staff_external class attributes and methods

# Maintain_Patients_referred_to_the_hospital_external class attributes and methods

# Maintain_Patients_referred_to_the_out_patients_clinic_external class attributes and methods

# of_Patients_referred_to_the_out_patient_clinic_external class attributes and methods

# Register_Patient_payment_external class attributes and methods

# of_Monthly_profit_external class attributes and methods

# of_Services_Improvement_external class attributes and methods

# Maintain_ward_s_supplies_external class attributes and methods

# of_ward_s_supplies_external class attributes and methods

# Maintain_suppliers_external class attributes and methods

# Set_staff_weekly_Rota_external class attributes and methods

# Maintain_next_of_kind_details_external class attributes and methods

# Create_Patient_appointment_external class attributes and methods

# Search_Patient_external class attributes and methods

# Authorise_Service_Improvement_Budget_external class attributes and methods

# Generate_Staff_s_Payroll_external class attributes and methods

# Relationships
Medical_Director_Produce_Reports_of_Patients: BinaryAssociation = BinaryAssociation(
    name="Medical_Director_Produce_Reports_of_Patients",
    ends={
        Property(name="produce_Reports_of_Patients14", type=of_Patients_referred_to_the_out_patient_clinic_external, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_Director15", type=Medical_Director_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Produce_Reports_of_Patients: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Produce_Reports_of_Patients",
    ends={
        Property(name="produce_Reports_of_Patients16", type=of_Patients_referred_to_the_out_patient_clinic_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse17", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Maintain_ward_s_Patients: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Maintain_ward_s_Patients",
    ends={
        Property(name="maintain_ward_s_Patients18", type=Maintain_ward_s_Patients_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse19", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Maintian_Patients__medication: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Maintian_Patients__medication",
    ends={
        Property(name="maintian_Patients__medication20", type=Maintian_Patients__medication_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse21", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Produce_Reports_of_Patients__medication: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Produce_Reports_of_Patients__medication",
    ends={
        Property(name="produce_Reports_of_Patients__medication22", type=of_Patients__medication_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse23", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_of_ward_s_Patients: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_of_ward_s_Patients",
    ends={
        Property(name="of_ward_s_Patients24", type=of_Patients_in_wards_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse25", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medical_Director_of_ward_s_Patients: BinaryAssociation = BinaryAssociation(
    name="Medical_Director_of_ward_s_Patients",
    ends={
        Property(name="of_ward_s_Patients26", type=of_Patients_in_wards_external, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_Director27", type=Medical_Director_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_of_Patients_on_waiting_list: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_of_Patients_on_waiting_list",
    ends={
        Property(name="of_Patients_on_waiting_list28", type=of_Patients_on_waiting_list_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse29", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Maintain_resources_Medical_Director: BinaryAssociation = BinaryAssociation(
    name="Maintain_resources_Medical_Director",
    ends={
        Property(name="medical_Director0", type=Medical_Director_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="maintain_resources1", type=Maintain_resources_external, multiplicity=Multiplicity(0, 1))
    }
)
Personnel_Officer_Maintain_staff: BinaryAssociation = BinaryAssociation(
    name="Personnel_Officer_Maintain_staff",
    ends={
        Property(name="maintain_staff2", type=Maintain_Staff_external, multiplicity=Multiplicity(0, 1)),
        Property(name="personnel_Officer3", type=Personnel_Officer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Personnel_Officer__Search_staff: BinaryAssociation = BinaryAssociation(
    name="Personnel_Officer__Search_staff",
    ends={
        Property(name="Search_staff4", type=Search_Staff_external, multiplicity=Multiplicity(0, 1)),
        Property(name="personnel_Officer5", type=Personnel_Officer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Personnel_Officer_Produce_a_report: BinaryAssociation = BinaryAssociation(
    name="Personnel_Officer_Produce_a_report",
    ends={
        Property(name="produce_a_report6", type=of_Ward_s_Staff_external, multiplicity=Multiplicity(0, 1)),
        Property(name="personnel_Officer7", type=Personnel_Officer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Produce_a_report: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Produce_a_report",
    ends={
        Property(name="produce_a_report8", type=of_Ward_s_Staff_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse9", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Maintain_Patients: BinaryAssociation = BinaryAssociation(
    name="Staff_Maintain_Patients",
    ends={
        Property(name="maintain_Patients10", type=Maintain_Patients_referred_to_the_hospital_external, multiplicity=Multiplicity(0, 1)),
        Property(name="staff11", type=Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Maintain_Patients_referred_to_the_out_patients_clinic: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Maintain_Patients_referred_to_the_out_patients_clinic",
    ends={
        Property(name="maintain_Patients_referred_to_the_out_patients_clinic12", type=Maintain_Patients_referred_to_the_out_patients_clinic_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse13", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
InPatient_WaitingList: BinaryAssociation = BinaryAssociation(
    name="InPatient_WaitingList",
    ends={
        Property(name="waitingList64", type=WaitingList, multiplicity=Multiplicity(1, 1)),
        Property(name="inPatient65", type=InPatient, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Appointment: BinaryAssociation = BinaryAssociation(
    name="Patient_Appointment",
    ends={
        Property(name="appointment66", type=Appointment, multiplicity=Multiplicity(1, 9999)),
        Property(name="patient267", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
RegularDoctor_Appointment: BinaryAssociation = BinaryAssociation(
    name="RegularDoctor_Appointment",
    ends={
        Property(name="appointment68", type=Appointment, multiplicity=Multiplicity(1, 9999)),
        Property(name="regularDoctor69", type=RegularDoctor, multiplicity=Multiplicity(1, 1))
    }
)
WaitingList_Appointment: BinaryAssociation = BinaryAssociation(
    name="WaitingList_Appointment",
    ends={
        Property(name="appointment70", type=Appointment, multiplicity=Multiplicity(1, 1)),
        Property(name="waitingList71", type=WaitingList, multiplicity=Multiplicity(1, 1))
    }
)
OutPatient_Patient: BinaryAssociation = BinaryAssociation(
    name="OutPatient_Patient",
    ends={
        Property(name="patient272", type=Patient, multiplicity=Multiplicity(1, 1)),
        Property(name="outPatient73", type=OutPatient, multiplicity=Multiplicity(1, 1))
    }
)
Medication_Patient: BinaryAssociation = BinaryAssociation(
    name="Medication_Patient",
    ends={
        Property(name="patient274", type=Patient, multiplicity=Multiplicity(1, 1)),
        Property(name="medication75", type=Medication, multiplicity=Multiplicity(1, 9999))
    }
)
Medication_Pharmaceutical: BinaryAssociation = BinaryAssociation(
    name="Medication_Pharmaceutical",
    ends={
        Property(name="pharmaceutical76", type=Pharmaceutical, multiplicity=Multiplicity(1, 9999)),
        Property(name="medication77", type=Medication, multiplicity=Multiplicity(0, 9999))
    }
)
Payee_Register_patient_payment: BinaryAssociation = BinaryAssociation(
    name="Payee_Register_patient_payment",
    ends={
        Property(name="register_patient_payment78", type=Register_Patient_payment_external, multiplicity=Multiplicity(0, 1)),
        Property(name="payee79", type=Payee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payee_of_Monthly_profit: BinaryAssociation = BinaryAssociation(
    name="Payee_of_Monthly_profit",
    ends={
        Property(name="of_Monthly_profit80", type=of_Monthly_profit_external, multiplicity=Multiplicity(0, 1)),
        Property(name="payee81", type=Payee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medical_Director_of_Patients_on_waiting_list: BinaryAssociation = BinaryAssociation(
    name="Medical_Director_of_Patients_on_waiting_list",
    ends={
        Property(name="of_Patients_on_waiting_list30", type=of_Patients_on_waiting_list_external, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_Director31", type=Medical_Director_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Maintain_ward_s_supplies: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Maintain_ward_s_supplies",
    ends={
        Property(name="maintain_ward_s_supplies32", type=Maintain_ward_s_supplies_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse33", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_of_ward_s_supplies: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_of_ward_s_supplies",
    ends={
        Property(name="of_ward_s_supplies34", type=of_ward_s_supplies_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse35", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medical_Director_of_ward_s_supplies: BinaryAssociation = BinaryAssociation(
    name="Medical_Director_of_ward_s_supplies",
    ends={
        Property(name="of_ward_s_supplies36", type=of_ward_s_supplies_external, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_Director37", type=Medical_Director_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medical_Director_Maintain_suppliers: BinaryAssociation = BinaryAssociation(
    name="Medical_Director_Maintain_suppliers",
    ends={
        Property(name="maintain_suppliers38", type=Maintain_suppliers_external, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_Director39", type=Medical_Director_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Charge_Nurse_Set_staff_weekly_Rota: BinaryAssociation = BinaryAssociation(
    name="Charge_Nurse_Set_staff_weekly_Rota",
    ends={
        Property(name="set_staff_weekly_Rota40", type=Set_staff_weekly_Rota_external, multiplicity=Multiplicity(0, 1)),
        Property(name="charge_Nurse41", type=Charge_Nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Maintain_next_of_kind_details: BinaryAssociation = BinaryAssociation(
    name="Staff_Maintain_next_of_kind_details",
    ends={
        Property(name="maintain_next_of_kind_details42", type=Maintain_next_of_kind_details_external, multiplicity=Multiplicity(0, 1)),
        Property(name="staff43", type=Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Create_Patient_appointment: BinaryAssociation = BinaryAssociation(
    name="Staff_Create_Patient_appointment",
    ends={
        Property(name="create_Patient_appointment44", type=Create_Patient_appointment_external, multiplicity=Multiplicity(0, 1)),
        Property(name="staff45", type=Staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Ward_Bed: BinaryAssociation = BinaryAssociation(
    name="Ward_Bed",
    ends={
        Property(name="Ward_Bed_046", type=Bed, multiplicity=Multiplicity(1, 9999)),
        Property(name="Ward_Bed_147", type=Ward, multiplicity=Multiplicity(1, 1))
    }
)
Ward_ChargeNurse: BinaryAssociation = BinaryAssociation(
    name="Ward_ChargeNurse",
    ends={
        Property(name="Ward_ChargeNurse_048", type=ChargeNurse, multiplicity=Multiplicity(1, 1)),
        Property(name="Ward_ChargeNurse_149", type=Ward, multiplicity=Multiplicity(1, 9999))
    }
)
Ward_RegularDoctor: BinaryAssociation = BinaryAssociation(
    name="Ward_RegularDoctor",
    ends={
        Property(name="Ward_RegularDoctor_050", type=RegularDoctor, multiplicity=Multiplicity(1, 9999)),
        Property(name="Ward_RegularDoctor_151", type=Ward, multiplicity=Multiplicity(1, 9999))
    }
)
Supplier_Supply: BinaryAssociation = BinaryAssociation(
    name="Supplier_Supply",
    ends={
        Property(name="Supplier_Supply_052", type=Supply, multiplicity=Multiplicity(1, 9999)),
        Property(name="Supplier_Supply_153", type=Supplier, multiplicity=Multiplicity(1, 9999))
    }
)
Requisition_Ward: BinaryAssociation = BinaryAssociation(
    name="Requisition_Ward",
    ends={
        Property(name="Requisition_Ward_054", type=Ward, multiplicity=Multiplicity(1, 1)),
        Property(name="Requisition_Ward_155", type=Requisition, multiplicity=Multiplicity(1, 9999))
    }
)
Requisition_ChargeNurse: BinaryAssociation = BinaryAssociation(
    name="Requisition_ChargeNurse",
    ends={
        Property(name="Requisition_ChargeNurse_056", type=ChargeNurse, multiplicity=Multiplicity(1, 1)),
        Property(name="Requisition_ChargeNurse_157", type=Requisition, multiplicity=Multiplicity(1, 9999))
    }
)
Supply_Requisition: BinaryAssociation = BinaryAssociation(
    name="Supply_Requisition",
    ends={
        Property(name="Supply_Requisition_058", type=Requisition, multiplicity=Multiplicity(1, 9999)),
        Property(name="Supply_Requisition_159", type=Supply, multiplicity=Multiplicity(1, 9999))
    }
)
WaitingList_Patient: BinaryAssociation = BinaryAssociation(
    name="WaitingList_Patient",
    ends={
        Property(name="WaitingList_Patient_060", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="WaitingList_Patient_161", type=WaitingList, multiplicity=Multiplicity(1, 1))
    }
)
Ward_WaitingList: BinaryAssociation = BinaryAssociation(
    name="Ward_WaitingList",
    ends={
        Property(name="Ward_WaitingList_062", type=WaitingList, multiplicity=Multiplicity(1, 1)),
        Property(name="Ward_WaitingList_163", type=Ward, multiplicity=Multiplicity(1, 9999))
    }
)
Medical_Director_of_Services_Improvement: BinaryAssociation = BinaryAssociation(
    name="Medical_Director_of_Services_Improvement",
    ends={
        Property(name="of_Services_Improvement82", type=of_Services_Improvement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_Director83", type=Medical_Director_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payee__Search_Staff: BinaryAssociation = BinaryAssociation(
    name="Payee__Search_Staff",
    ends={
        Property(name="Search_Staff84", type=Search_Staff_external, multiplicity=Multiplicity(0, 1)),
        Property(name="payee85", type=Payee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payee_Search_Patient: BinaryAssociation = BinaryAssociation(
    name="Payee_Search_Patient",
    ends={
        Property(name="search_Patient86", type=Search_Patient_external, multiplicity=Multiplicity(0, 1)),
        Property(name="payee87", type=Payee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payee_of_Patients__medication: BinaryAssociation = BinaryAssociation(
    name="Payee_of_Patients__medication",
    ends={
        Property(name="of_Patients__medication88", type=of_Patients__medication_external, multiplicity=Multiplicity(0, 1)),
        Property(name="payee89", type=Payee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payee_of_Patients_in_wards: BinaryAssociation = BinaryAssociation(
    name="Payee_of_Patients_in_wards",
    ends={
        Property(name="of_Patients_in_wards90", type=of_Patients_in_wards_external, multiplicity=Multiplicity(0, 1)),
        Property(name="payee91", type=Payee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Payee_Maintain_ward_s_Patients: BinaryAssociation = BinaryAssociation(
    name="Payee_Maintain_ward_s_Patients",
    ends={
        Property(name="maintain_ward_s_Patients92", type=Maintain_ward_s_Patients_external, multiplicity=Multiplicity(0, 1)),
        Property(name="payee93", type=Payee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Accountant_Authorise_Service_Improvement_Budget: BinaryAssociation = BinaryAssociation(
    name="Accountant_Authorise_Service_Improvement_Budget",
    ends={
        Property(name="authorise_Service_Improvement_Budget94", type=Authorise_Service_Improvement_Budget_external, multiplicity=Multiplicity(0, 1)),
        Property(name="accountant95", type=Accountant_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Accountant__Search_Staff: BinaryAssociation = BinaryAssociation(
    name="Accountant__Search_Staff",
    ends={
        Property(name="Search_Staff96", type=Search_Staff_external, multiplicity=Multiplicity(0, 1)),
        Property(name="accountant97", type=Accountant_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Accountant_Generate_Payment_Payroll: BinaryAssociation = BinaryAssociation(
    name="Accountant_Generate_Payment_Payroll",
    ends={
        Property(name="generate_Payment_Payroll98", type=Generate_Staff_s_Payroll_external, multiplicity=Multiplicity(0, 1)),
        Property(name="accountant99", type=Accountant_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Accountant_of_Monthly_profit: BinaryAssociation = BinaryAssociation(
    name="Accountant_of_Monthly_profit",
    ends={
        Property(name="of_Monthly_profit100", type=of_Monthly_profit_external, multiplicity=Multiplicity(0, 1)),
        Property(name="accountant101", type=Accountant_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ef480fad_142e_4ef4_b993_fd2cba176f70",
    types={Personnel_Officer_Actor, _Component, Staff_Actor, Charge_Nurse_Actor, Person_Actor, Medical_Director_Actor, Patient_Actor, Person, Patient, Staff, NextOfKind, LocalDoctor, Qualification, WorkExperience, EmploymentContract, MedicalDirector, PersonnelOfficer, ChargeNurse, RegularDoctor, Ward, Bed, Requisition, Supply, Surgical_NonSurgical, Pharmaceutical, Supplier, WaitingList, InPatient, Appointment, OutPatient, Medication, _Component1, Payee_Actor, Accountant_Actor, Maintain_ward_s_Patients_external, Maintian_Patients__medication_external, of_Patients__medication_external, of_Patients_in_wards_external, of_Patients_on_waiting_list_external, Maintain_resources_external, Maintain_Staff_external, Search_Staff_external, of_Ward_s_Staff_external, Maintain_Patients_referred_to_the_hospital_external, Maintain_Patients_referred_to_the_out_patients_clinic_external, of_Patients_referred_to_the_out_patient_clinic_external, Register_Patient_payment_external, of_Monthly_profit_external, of_Services_Improvement_external, Maintain_ward_s_supplies_external, of_ward_s_supplies_external, Maintain_suppliers_external, Set_staff_weekly_Rota_external, Maintain_next_of_kind_details_external, Create_Patient_appointment_external, Search_Patient_external, Authorise_Service_Improvement_Budget_external, Generate_Staff_s_Payroll_external, Sex, MaritalStatus, Relationship, Position, TypeContract, SalaryPayment, SupplyType, Administration},
    associations={Medical_Director_Produce_Reports_of_Patients, Charge_Nurse_Produce_Reports_of_Patients, Charge_Nurse_Maintain_ward_s_Patients, Charge_Nurse_Maintian_Patients__medication, Charge_Nurse_Produce_Reports_of_Patients__medication, Charge_Nurse_of_ward_s_Patients, Medical_Director_of_ward_s_Patients, Charge_Nurse_of_Patients_on_waiting_list, Maintain_resources_Medical_Director, Personnel_Officer_Maintain_staff, Personnel_Officer__Search_staff, Personnel_Officer_Produce_a_report, Charge_Nurse_Produce_a_report, Staff_Maintain_Patients, Charge_Nurse_Maintain_Patients_referred_to_the_out_patients_clinic, InPatient_WaitingList, Patient_Appointment, RegularDoctor_Appointment, WaitingList_Appointment, OutPatient_Patient, Medication_Patient, Medication_Pharmaceutical, Payee_Register_patient_payment, Payee_of_Monthly_profit, Medical_Director_of_Patients_on_waiting_list, Charge_Nurse_Maintain_ward_s_supplies, Charge_Nurse_of_ward_s_supplies, Medical_Director_of_ward_s_supplies, Medical_Director_Maintain_suppliers, Charge_Nurse_Set_staff_weekly_Rota, Staff_Maintain_next_of_kind_details, Staff_Create_Patient_appointment, Ward_Bed, Ward_ChargeNurse, Ward_RegularDoctor, Supplier_Supply, Requisition_Ward, Requisition_ChargeNurse, Supply_Requisition, WaitingList_Patient, Ward_WaitingList, Medical_Director_of_Services_Improvement, Payee__Search_Staff, Payee_Search_Patient, Payee_of_Patients__medication, Payee_of_Patients_in_wards, Payee_Maintain_ward_s_Patients, Accountant_Authorise_Service_Improvement_Budget, Accountant__Search_Staff, Accountant_Generate_Payment_Payroll, Accountant_of_Monthly_profit},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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

# Classes
Corporation = Class(name="Corporation")
Hospitals = Class(name="Hospitals")
Disease = Class(name="Disease")
Medicine = Class(name="Medicine")
Patient_Prescription = Class(name="Patient_Prescription")
Appointment = Class(name="Appointment")
Examination = Class(name="Examination")
diagnosis = Class(name="diagnosis")
Patient_Medicines = Class(name="Patient_Medicines")
Room = Class(name="Room")
Receptionist = Class(name="Receptionist")
Bill = Class(name="Bill")
Patient = Class(name="Patient")
Personel = Class(name="Personel")
Doctor = Class(name="Doctor")

# Corporation class attributes and methods
Corporation_no: Property = Property(name="no", type=IntegerType)
Corporation_name: Property = Property(name="name", type=StringType)
Corporation_address: Property = Property(name="address", type=StringType)
Corporation.attributes={Corporation_address, Corporation_no, Corporation_name}

# Hospitals class attributes and methods
Hospitals_no: Property = Property(name="no", type=IntegerType)
Hospitals_type: Property = Property(name="type", type=StringType)
Hospitals_address: Property = Property(name="address", type=StringType)
Hospitals_name: Property = Property(name="name", type=StringType)
Hospitals.attributes={Hospitals_name, Hospitals_no, Hospitals_type, Hospitals_address}

# Disease class attributes and methods
Disease_code: Property = Property(name="code", type=IntegerType)
Disease_name: Property = Property(name="name", type=StringType)
Disease_type: Property = Property(name="type", type=StringType)
Disease.attributes={Disease_name, Disease_code, Disease_type}

# Medicine class attributes and methods
Medicine_code: Property = Property(name="code", type=IntegerType)
Medicine_name: Property = Property(name="name", type=StringType)
Medicine_price: Property = Property(name="price", type=StringType)
Medicine_type: Property = Property(name="type", type=StringType)
Medicine.attributes={Medicine_price, Medicine_name, Medicine_code, Medicine_type}

# Patient_Prescription class attributes and methods
Patient_Prescription_code: Property = Property(name="code", type=IntegerType)
Patient_Prescription_code1: Property = Property(name="code1", type=IntegerType)
Patient_Prescription_patientid: Property = Property(name="patientid", type=IntegerType)
Patient_Prescription_diseaseid: Property = Property(name="diseaseid", type=IntegerType)
Patient_Prescription_date: Property = Property(name="date", type=StringType)
Patient_Prescription_medicineid: Property = Property(name="medicineid", type=IntegerType)
Patient_Prescription.attributes={Patient_Prescription_patientid, Patient_Prescription_diseaseid, Patient_Prescription_code1, Patient_Prescription_medicineid, Patient_Prescription_date, Patient_Prescription_code}

# Appointment class attributes and methods
Appointment_no: Property = Property(name="no", type=StringType)
Appointment_doctoradi: Property = Property(name="doctoradi", type=IntegerType)
Appointment_date: Property = Property(name="date", type=StringType)
Appointment_time: Property = Property(name="time", type=StringType)
Appointment_room: Property = Property(name="room", type=IntegerType)
Appointment_attribute: Property = Property(name="attribute", type=StringType)
Appointment.attributes={Appointment_time, Appointment_date, Appointment_room, Appointment_attribute, Appointment_doctoradi, Appointment_no}

# Examination class attributes and methods
Examination_no: Property = Property(name="no", type=IntegerType)
Examination_attribute: Property = Property(name="attribute", type=StringType)
Examination_Appointmentid: Property = Property(name="Appointmentid", type=IntegerType)
Examination_diagnosisid: Property = Property(name="diagnosisid", type=IntegerType)
Examination.attributes={Examination_no, Examination_attribute, Examination_Appointmentid, Examination_diagnosisid}

# diagnosis class attributes and methods
diagnosis_id: Property = Property(name="id", type=IntegerType)
diagnosis_diagnoses: Property = Property(name="diagnoses", type=StringType)
diagnosis.attributes={diagnosis_diagnoses, diagnosis_id}

# Patient_Medicines class attributes and methods
Patient_Medicines_no: Property = Property(name="no", type=IntegerType)
Patient_Medicines_patientno: Property = Property(name="patientno", type=StringType)
Patient_Medicines_medicines: Property = Property(name="medicines", type=StringType)
Patient_Medicines_quantities: Property = Property(name="quantities", type=IntegerType)
Patient_Medicines.attributes={Patient_Medicines_patientno, Patient_Medicines_medicines, Patient_Medicines_quantities, Patient_Medicines_no}

# Room class attributes and methods
Room_no: Property = Property(name="no", type=IntegerType)
Room_floor: Property = Property(name="floor", type=IntegerType)
Room_buildingname: Property = Property(name="buildingname", type=StringType)
Room.attributes={Room_no, Room_buildingname, Room_floor}

# Receptionist class attributes and methods
Receptionist_no: Property = Property(name="no", type=IntegerType)
Receptionist_checkroom: Property = Property(name="checkroom", type=StringType)
Receptionist.attributes={Receptionist_no, Receptionist_checkroom}

# Bill class attributes and methods
Bill_no: Property = Property(name="no", type=IntegerType)
Bill_patientno: Property = Property(name="patientno", type=IntegerType)
Bill_amount: Property = Property(name="amount", type=StringType)
Bill.attributes={Bill_patientno, Bill_no, Bill_amount}

# Patient class attributes and methods
Patient_name: Property = Property(name="name", type=StringType)
Patient_telno: Property = Property(name="telno", type=StringType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_birth: Property = Property(name="birth", type=StringType)
Patient_gender: Property = Property(name="gender", type=StringType)
Patient_tcno: Property = Property(name="tcno", type=StringType)
Patient_tcno1: Property = Property(name="tcno1", type=StringType)
Patient_name1: Property = Property(name="name1", type=StringType)
Patient_telno1: Property = Property(name="telno1", type=StringType)
Patient_address1: Property = Property(name="address1", type=StringType)
Patient_birth1: Property = Property(name="birth1", type=StringType)
Patient_gender1: Property = Property(name="gender1", type=StringType)
Patient_attribute: Property = Property(name="attribute", type=StringType)
Patient.attributes={Patient_gender1, Patient_tcno1, Patient_attribute, Patient_name, Patient_tcno, Patient_telno1, Patient_address, Patient_gender, Patient_birth1, Patient_telno, Patient_address1, Patient_name1, Patient_birth}

# Personel class attributes and methods
Personel_tcno: Property = Property(name="tcno", type=StringType)
Personel_name: Property = Property(name="name", type=StringType)
Personel_attribute: Property = Property(name="attribute", type=StringType)
Personel_registerno: Property = Property(name="registerno", type=StringType)
Personel_tcno1: Property = Property(name="tcno1", type=StringType)
Personel_name1: Property = Property(name="name1", type=StringType)
Personel_gender: Property = Property(name="gender", type=StringType)
Personel_position: Property = Property(name="position", type=StringType)
Personel_corporation: Property = Property(name="corporation", type=StringType)
Personel_attribute7: Property = Property(name="attribute7", type=StringType)
Personel.attributes={Personel_tcno1, Personel_position, Personel_registerno, Personel_gender, Personel_corporation, Personel_tcno, Personel_attribute, Personel_attribute7, Personel_name1, Personel_name}

# Doctor class attributes and methods
Doctor_registorno: Property = Property(name="registorno", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_corporation: Property = Property(name="corporation", type=StringType)
Doctor.attributes={Doctor_corporation, Doctor_specialization, Doctor_registorno}

# Relationships
Hospitals_Personel: BinaryAssociation = BinaryAssociation(
    name="Hospitals_Personel",
    ends={
        Property(name="personel14", type=Personel, multiplicity=Multiplicity(1, 9999)),
        Property(name="hospitals15", type=Hospitals, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Appointment: BinaryAssociation = BinaryAssociation(
    name="Patient_Appointment",
    ends={
        Property(name="appointment16", type=Appointment, multiplicity=Multiplicity(1, 9999)),
        Property(name="patient17", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Appointment: BinaryAssociation = BinaryAssociation(
    name="Doctor_Appointment",
    ends={
        Property(name="appointment18", type=Appointment, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor19", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Examination_Appointment: BinaryAssociation = BinaryAssociation(
    name="Examination_Appointment",
    ends={
        Property(name="appointment20", type=Appointment, multiplicity=Multiplicity(1, 1)),
        Property(name="examination21", type=Examination, multiplicity=Multiplicity(0, 1))
    }
)
Room_Appointment: BinaryAssociation = BinaryAssociation(
    name="Room_Appointment",
    ends={
        Property(name="appointment22", type=Appointment, multiplicity=Multiplicity(1, 1)),
        Property(name="room23", type=Room, multiplicity=Multiplicity(1, 1))
    }
)
Examination_diagnosis: BinaryAssociation = BinaryAssociation(
    name="Examination_diagnosis",
    ends={
        Property(name="diagnosis24", type=diagnosis, multiplicity=Multiplicity(1, 9999)),
        Property(name="examination25", type=Examination, multiplicity=Multiplicity(1, 1))
    }
)
Patient_Patient_Medicines: BinaryAssociation = BinaryAssociation(
    name="Patient_Patient_Medicines",
    ends={
        Property(name="patient_Medicines26", type=Patient_Medicines, multiplicity=Multiplicity(0, 1)),
        Property(name="patient27", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Doctor: BinaryAssociation = BinaryAssociation(
    name="Patient_Doctor",
    ends={
        Property(name="doctor0", type=Personel, multiplicity=Multiplicity(0, 1)),
        Property(name="patient1", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Doctor2: BinaryAssociation = BinaryAssociation(
    name="Patient_Doctor2",
    ends={
        Property(name="doctor2", type=Personel, multiplicity=Multiplicity(0, 1)),
        Property(name="patient3", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Personel: BinaryAssociation = BinaryAssociation(
    name="Doctor_Personel",
    ends={
        Property(name="personel4", type=Personel, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor5", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Personel_Corporation: BinaryAssociation = BinaryAssociation(
    name="Personel_Corporation",
    ends={
        Property(name="corporation26", type=Corporation, multiplicity=Multiplicity(0, 1)),
        Property(name="personel7", type=Personel, multiplicity=Multiplicity(1, 9999))
    }
)
Personel_Hospitals: BinaryAssociation = BinaryAssociation(
    name="Personel_Hospitals",
    ends={
        Property(name="hospitals8", type=Hospitals, multiplicity=Multiplicity(0, 1)),
        Property(name="personel9", type=Personel, multiplicity=Multiplicity(0, 1))
    }
)
Personel_Doctor: BinaryAssociation = BinaryAssociation(
    name="Personel_Doctor",
    ends={
        Property(name="doctor10", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="personel11", type=Personel, multiplicity=Multiplicity(1, 1))
    }
)
Corporation_Personel: BinaryAssociation = BinaryAssociation(
    name="Corporation_Personel",
    ends={
        Property(name="personel12", type=Personel, multiplicity=Multiplicity(1, 9999)),
        Property(name="corporation13", type=Corporation, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Patient_Prescription: BinaryAssociation = BinaryAssociation(
    name="Patient_Patient_Prescription",
    ends={
        Property(name="patient_Prescription28", type=Patient_Prescription, multiplicity=Multiplicity(0, 1)),
        Property(name="patient29", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
Patient_Prescription_Disease: BinaryAssociation = BinaryAssociation(
    name="Patient_Prescription_Disease",
    ends={
        Property(name="disease30", type=Disease, multiplicity=Multiplicity(0, 1)),
        Property(name="patient_Prescription31", type=Patient_Prescription, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Prescription_Patient_Medicines: BinaryAssociation = BinaryAssociation(
    name="Patient_Prescription_Patient_Medicines",
    ends={
        Property(name="patient_Medicines32", type=Patient_Medicines, multiplicity=Multiplicity(1, 1)),
        Property(name="patient_Prescription33", type=Patient_Prescription, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Medicines_Medicine: BinaryAssociation = BinaryAssociation(
    name="Patient_Medicines_Medicine",
    ends={
        Property(name="medicine34", type=Medicine, multiplicity=Multiplicity(1, 9999)),
        Property(name="patient_Medicines35", type=Patient_Medicines, multiplicity=Multiplicity(1, 1))
    }
)
diagnosis_Disease: BinaryAssociation = BinaryAssociation(
    name="diagnosis_Disease",
    ends={
        Property(name="disease36", type=Disease, multiplicity=Multiplicity(1, 9999)),
        Property(name="diagnosis37", type=diagnosis, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_Personel: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Personel",
    ends={
        Property(name="personel38", type=Personel, multiplicity=Multiplicity(1, 1)),
        Property(name="receptionist39", type=Receptionist, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Patient: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Patient",
    ends={
        Property(name="patient40", type=Patient, multiplicity=Multiplicity(1, 1)),
        Property(name="receptionist41", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)
Personel_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Personel_Receptionist",
    ends={
        Property(name="receptionist42", type=Receptionist, multiplicity=Multiplicity(0, 1)),
        Property(name="personel43", type=Personel, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kzQPIHleEemeYMb8Sxp8Zg",
    types={Corporation, Hospitals, Disease, Medicine, Patient_Prescription, Appointment, Examination, diagnosis, Patient_Medicines, Room, Receptionist, Bill, Patient, Personel, Doctor},
    associations={Hospitals_Personel, Patient_Appointment, Doctor_Appointment, Examination_Appointment, Room_Appointment, Examination_diagnosis, Patient_Patient_Medicines, Patient_Doctor, Patient_Doctor2, Doctor_Personel, Personel_Corporation, Personel_Hospitals, Personel_Doctor, Corporation_Personel, Patient_Patient_Prescription, Patient_Prescription_Disease, Patient_Prescription_Patient_Medicines, Patient_Medicines_Medicine, diagnosis_Disease, Receptionist_Personel, Receptionist_Patient, Personel_Receptionist},
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
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
Hospital = Class(name="Hospital")
Doctor = Class(name="Doctor")
Patients = Class(name="Patients")
Receptionist = Class(name="Receptionist")
Appointment = Class(name="Appointment")
DoctorDatabase = Class(name="DoctorDatabase")
PatientProfile = Class(name="PatientProfile")
Assistant = Class(name="Assistant")
Prescription = Class(name="Prescription")
BloodBank = Class(name="BloodBank")
Billing_Report = Class(name="Billing_Report")

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_address: Property = Property(name="address", type=StringType)
Hospital_phone: Property = Property(name="phone", type=IntegerType)
Hospital.attributes={Hospital_name, Hospital_phone, Hospital_address}

# Doctor class attributes and methods
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_specilization: Property = Property(name="specilization", type=StringType)
Doctor_timing: Property = Property(name="timing", type=StringType)
Doctor_privateConsultancy: Property = Property(name="privateConsultancy", type=BooleanType)
Doctor.attributes={Doctor_privateConsultancy, Doctor_timing, Doctor_name, Doctor_specilization}

# Patients class attributes and methods
Patients_name: Property = Property(name="name", type=StringType)
Patients_weight: Property = Property(name="weight", type=IntegerType)
Patients_BP: Property = Property(name="BP", type=IntegerType)
Patients_History: Property = Property(name="History", type=StringType)
Patients_Symptoms: Property = Property(name="Symptoms", type=StringType)
Patients.attributes={Patients_BP, Patients_weight, Patients_Symptoms, Patients_name, Patients_History}

# Receptionist class attributes and methods
Receptionist_name: Property = Property(name="name", type=StringType)
Receptionist_CNIC: Property = Property(name="CNIC", type=StringType)
Receptionist.attributes={Receptionist_name, Receptionist_CNIC}

# Appointment class attributes and methods
Appointment_Time: Property = Property(name="Time", type=StringType)
Appointment_Patient: Property = Property(name="Patient", type=StringType)
Appointment_Doctor: Property = Property(name="Doctor", type=StringType)
Appointment.attributes={Appointment_Doctor, Appointment_Patient, Appointment_Time}

# DoctorDatabase class attributes and methods
DoctorDatabase_doctorName: Property = Property(name="doctorName", type=StringType)
DoctorDatabase_Specialization: Property = Property(name="Specialization", type=StringType)
DoctorDatabase.attributes={DoctorDatabase_Specialization, DoctorDatabase_doctorName}

# PatientProfile class attributes and methods
PatientProfile_appointment: Property = Property(name="appointment", type=StringType)
PatientProfile_name: Property = Property(name="name", type=StringType)
PatientProfile.attributes={PatientProfile_appointment, PatientProfile_name}

# Assistant class attributes and methods
Assistant_name: Property = Property(name="name", type=StringType)
Assistant_CNIC: Property = Property(name="CNIC", type=StringType)
Assistant.attributes={Assistant_CNIC, Assistant_name}

# Prescription class attributes and methods
Prescription_medicines: Property = Property(name="medicines", type=StringType)
Prescription_tests: Property = Property(name="tests", type=StringType)
Prescription.attributes={Prescription_tests, Prescription_medicines}

# BloodBank class attributes and methods
BloodBank_bloodGroup: Property = Property(name="bloodGroup", type=StringType)
BloodBank_phone: Property = Property(name="phone", type=StringType)
BloodBank.attributes={BloodBank_bloodGroup, BloodBank_phone}

# Billing_Report class attributes and methods
Billing_Report_serviceCharges: Property = Property(name="serviceCharges", type=StringType)
Billing_Report_testCharges: Property = Property(name="testCharges", type=StringType)
Billing_Report.attributes={Billing_Report_serviceCharges, Billing_Report_testCharges}

# Relationships
Hospital_Doctor: BinaryAssociation = BinaryAssociation(
    name="Hospital_Doctor",
    ends={
        Property(name="has0", type=Doctor, multiplicity=Multiplicity(0, 9999)),
        Property(name="Hospital_Doctor_11", type=Hospital, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Patients: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patients",
    ends={
        Property(name="Doctor_Patients_02", type=Patients, multiplicity=Multiplicity(1, 9999)),
        Property(name="Checks_up3", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Patients_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patients_Receptionist",
    ends={
        Property(name="calls_query4", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="Patients_Receptionist_15", type=Patients, multiplicity=Multiplicity(0, 9999))
    }
)
Patients_Hospital: BinaryAssociation = BinaryAssociation(
    name="Patients_Hospital",
    ends={
        Property(name="Visit6", type=Hospital, multiplicity=Multiplicity(1, 1)),
        Property(name="Patients_Hospital_17", type=Patients, multiplicity=Multiplicity(0, 9999))
    }
)
Receptionist_Appointment: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Appointment",
    ends={
        Property(name="give8", type=Appointment, multiplicity=Multiplicity(0, 9999)),
        Property(name="Receptionist_Appointment_19", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)
Patients_Appointment: BinaryAssociation = BinaryAssociation(
    name="Patients_Appointment",
    ends={
        Property(name="Patients_Appointment_010", type=Appointment, multiplicity=Multiplicity(1, 1)),
        Property(name="requests11", type=Patients, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_DoctorDatabase: BinaryAssociation = BinaryAssociation(
    name="Receptionist_DoctorDatabase",
    ends={
        Property(name="Receptionist_DoctorDatabase_012", type=DoctorDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="check13", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_PatientProfile: BinaryAssociation = BinaryAssociation(
    name="Receptionist_PatientProfile",
    ends={
        Property(name="create_update14", type=PatientProfile, multiplicity=Multiplicity(0, 9999)),
        Property(name="Receptionist_PatientProfile_115", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)
Assistant_Appointment: BinaryAssociation = BinaryAssociation(
    name="Assistant_Appointment",
    ends={
        Property(name="Assistant_Appointment_016", type=Appointment, multiplicity=Multiplicity(0, 9999)),
        Property(name="check_details17", type=Assistant, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Prescription: BinaryAssociation = BinaryAssociation(
    name="Doctor_Prescription",
    ends={
        Property(name="Doctor_Prescription_018", type=Prescription, multiplicity=Multiplicity(0, 9999)),
        Property(name="writes19", type=Doctor, multiplicity=Multiplicity(0, 9999))
    }
)
Patients_Assistant: BinaryAssociation = BinaryAssociation(
    name="Patients_Assistant",
    ends={
        Property(name="record_history20", type=Assistant, multiplicity=Multiplicity(1, 1)),
        Property(name="Patients_Assistant_121", type=Patients, multiplicity=Multiplicity(0, 9999))
    }
)
Doctor_Assistant: BinaryAssociation = BinaryAssociation(
    name="Doctor_Assistant",
    ends={
        Property(name="forward_patient_history22", type=Assistant, multiplicity=Multiplicity(1, 1)),
        Property(name="Doctor_Assistant_123", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Hospital_BloodBank: BinaryAssociation = BinaryAssociation(
    name="Hospital_BloodBank",
    ends={
        Property(name="has24", type=BloodBank, multiplicity=Multiplicity(1, 1)),
        Property(name="Hospital_BloodBank_125", type=Hospital, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_Billing_Report: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Billing_Report",
    ends={
        Property(name="generate26", type=Billing_Report, multiplicity=Multiplicity(0, 9999)),
        Property(name="Receptionist_Billing_Report_127", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_74vroGdMEeiTTuxWefFgMg",
    types={Hospital, Doctor, Patients, Receptionist, Appointment, DoctorDatabase, PatientProfile, Assistant, Prescription, BloodBank, Billing_Report},
    associations={Hospital_Doctor, Doctor_Patients, Patients_Receptionist, Patients_Hospital, Receptionist_Appointment, Patients_Appointment, Receptionist_DoctorDatabase, Receptionist_PatientProfile, Assistant_Appointment, Doctor_Prescription, Patients_Assistant, Doctor_Assistant, Hospital_BloodBank, Receptionist_Billing_Report},
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
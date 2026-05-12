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
Employee_Actor = Class(name="Employee_Actor")
Nurse_Actor = Class(name="Nurse_Actor")
Doctor_Actor = Class(name="Doctor_Actor")
Patient_Actor = Class(name="Patient_Actor")
Logging_into_system_UseCase = Class(name="Logging_into_system_UseCase")
Appointment_management_UseCase = Class(name="Appointment_management_UseCase")
New_appointment_UseCase = Class(name="New_appointment_UseCase")
Remove_appointment_UseCase = Class(name="Remove_appointment_UseCase")
Diagnose_UseCase = Class(name="Diagnose_UseCase")
Billing_UseCase = Class(name="Billing_UseCase")
Authorization_UseCase = Class(name="Authorization_UseCase")
Employee = Class(name="Employee")
Doctor = Class(name="Doctor")
Nurse = Class(name="Nurse")
Patient = Class(name="Patient")
Schedule = Class(name="Schedule")
Diagnose = Class(name="Diagnose")
TreatmentList = Class(name="TreatmentList")
Create_new_patient_account_UseCase = Class(name="Create_new_patient_account_UseCase")
Logging_as_existing_user_UseCase = Class(name="Logging_as_existing_user_UseCase")
Bill = Class(name="Bill")
Appointment_external = Class(name="Appointment_external")
AppointmentDiagnose_external = Class(name="AppointmentDiagnose_external")

# Employee_Actor class attributes and methods

# Nurse_Actor class attributes and methods

# Doctor_Actor class attributes and methods

# Patient_Actor class attributes and methods

# Logging_into_system_UseCase class attributes and methods

# Appointment_management_UseCase class attributes and methods

# New_appointment_UseCase class attributes and methods

# Remove_appointment_UseCase class attributes and methods

# Diagnose_UseCase class attributes and methods

# Billing_UseCase class attributes and methods

# Authorization_UseCase class attributes and methods

# Employee class attributes and methods
Employee_employeeID: Property = Property(name="employeeID", type=IntegerType)
Employee_employeeName: Property = Property(name="employeeName", type=StringType)
Employee_employeeSurname: Property = Property(name="employeeSurname", type=StringType)
Employee_employeeAddress: Property = Property(name="employeeAddress", type=StringType)
Employee_employeeMobile: Property = Property(name="employeeMobile", type=StringType)
Employee_employeeEmail: Property = Property(name="employeeEmail", type=StringType)
Employee_employeeUsername: Property = Property(name="employeeUsername", type=StringType)
Employee_employeePassword: Property = Property(name="employeePassword", type=StringType)
Employee.attributes={Employee_employeeSurname, Employee_employeeAddress, Employee_employeeUsername, Employee_employeeID, Employee_employeePassword, Employee_employeeMobile, Employee_employeeName, Employee_employeeEmail}

# Doctor class attributes and methods
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor.attributes={Doctor_specialization}

# Nurse class attributes and methods
Nurse_experience: Property = Property(name="experience", type=StringType)
Nurse.attributes={Nurse_experience}

# Patient class attributes and methods
Patient_coupon: Property = Property(name="coupon", type=FloatType)
Patient_patientID: Property = Property(name="patientID", type=IntegerType)
Patient_patientName: Property = Property(name="patientName", type=StringType)
Patient_patientSurname: Property = Property(name="patientSurname", type=StringType)
Patient_patientMobile: Property = Property(name="patientMobile", type=StringType)
Patient_patientEmail: Property = Property(name="patientEmail", type=StringType)
Patient_patientAddress: Property = Property(name="patientAddress", type=StringType)
Patient.attributes={Patient_patientSurname, Patient_coupon, Patient_patientName, Patient_patientMobile, Patient_patientEmail, Patient_patientID, Patient_patientAddress}

# Schedule class attributes and methods
Schedule_scheduleID: Property = Property(name="scheduleID", type=IntegerType)
Schedule_startTime: Property = Property(name="startTime", type=StringType)
Schedule_endTime: Property = Property(name="endTime", type=StringType)
Schedule_date: Property = Property(name="date", type=StringType)
Schedule_available: Property = Property(name="available", type=BooleanType)
Schedule.attributes={Schedule_startTime, Schedule_endTime, Schedule_scheduleID, Schedule_date, Schedule_available}

# Diagnose class attributes and methods
Diagnose_diagnoseID: Property = Property(name="diagnoseID", type=IntegerType)
Diagnose_symptomps: Property = Property(name="symptomps", type=StringType)
Diagnose_medication: Property = Property(name="medication", type=StringType)
Diagnose.attributes={Diagnose_symptomps, Diagnose_diagnoseID, Diagnose_medication}

# TreatmentList class attributes and methods
TreatmentList_treatmentID: Property = Property(name="treatmentID", type=IntegerType)
TreatmentList_treatmentName: Property = Property(name="treatmentName", type=StringType)
TreatmentList_treatmentPrice: Property = Property(name="treatmentPrice", type=FloatType)
TreatmentList.attributes={TreatmentList_treatmentPrice, TreatmentList_treatmentName, TreatmentList_treatmentID}

# Create_new_patient_account_UseCase class attributes and methods

# Logging_as_existing_user_UseCase class attributes and methods

# Bill class attributes and methods
Bill_billID: Property = Property(name="billID", type=StringType)
Bill_date: Property = Property(name="date", type=StringType)
Bill_ammount: Property = Property(name="ammount", type=FloatType)
Bill.attributes={Bill_date, Bill_ammount, Bill_billID}

# Appointment_external class attributes and methods

# AppointmentDiagnose_external class attributes and methods

# Relationships
Employee_Logging_into_system: BinaryAssociation = BinaryAssociation(
    name="Employee_Logging_into_system",
    ends={
        Property(name="logging_into_system0", type=Logging_into_system_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employee1", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Create_appointment: BinaryAssociation = BinaryAssociation(
    name="Patient_Create_appointment",
    ends={
        Property(name="create_appointment2", type=Appointment_management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patient3", type=Patient_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Billing: BinaryAssociation = BinaryAssociation(
    name="Patient_Billing",
    ends={
        Property(name="billing4", type=Billing_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patient5", type=Patient_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Logging_into_system: BinaryAssociation = BinaryAssociation(
    name="Patient_Logging_into_system",
    ends={
        Property(name="logging_into_system6", type=Logging_into_system_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patient7", type=Patient_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_DoctorSchedule: BinaryAssociation = BinaryAssociation(
    name="Patient_DoctorSchedule",
    ends={
        Property(name="patient8", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="appointment9", type=Appointment_external, multiplicity=Multiplicity(0, 9999))
    }
)
TreatmentList_AppointmentDiagnose: BinaryAssociation = BinaryAssociation(
    name="TreatmentList_AppointmentDiagnose",
    ends={
        Property(name="treatmentList10", type=TreatmentList, multiplicity=Multiplicity(1, 1)),
        Property(name="appointmentDiagnose11", type=AppointmentDiagnose_external, multiplicity=Multiplicity(0, 9999))
    }
)
Appointment_Bill: BinaryAssociation = BinaryAssociation(
    name="Appointment_Bill",
    ends={
        Property(name="appointment12", type=Appointment_external, multiplicity=Multiplicity(1, 1)),
        Property(name="bill13", type=Bill, multiplicity=Multiplicity(0, 1))
    }
)
Nurse_Bill: BinaryAssociation = BinaryAssociation(
    name="Nurse_Bill",
    ends={
        Property(name="nurse14", type=Nurse, multiplicity=Multiplicity(1, 1)),
        Property(name="bill15", type=Bill, multiplicity=Multiplicity(0, 9999))
    }
)
Doctor_Diagnose: BinaryAssociation = BinaryAssociation(
    name="Doctor_Diagnose",
    ends={
        Property(name="doctor16", type=Doctor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="diagnose17", type=Diagnose_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Nurse_Billing: BinaryAssociation = BinaryAssociation(
    name="Nurse_Billing",
    ends={
        Property(name="nurse18", type=Nurse_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="billing19", type=Billing_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_79t5IGqZEeqghpCovSsunw",
    types={Employee_Actor, Nurse_Actor, Doctor_Actor, Patient_Actor, Logging_into_system_UseCase, Appointment_management_UseCase, New_appointment_UseCase, Remove_appointment_UseCase, Diagnose_UseCase, Billing_UseCase, Authorization_UseCase, Employee, Doctor, Nurse, Patient, Schedule, Diagnose, TreatmentList, Create_new_patient_account_UseCase, Logging_as_existing_user_UseCase, Bill, Appointment_external, AppointmentDiagnose_external},
    associations={Employee_Logging_into_system, Patient_Create_appointment, Patient_Billing, Patient_Logging_into_system, Patient_DoctorSchedule, TreatmentList_AppointmentDiagnose, Appointment_Bill, Nurse_Bill, Doctor_Diagnose, Nurse_Billing},
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
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
Person = Class(name="Person")
Staff = Class(name="Staff")
Nurse = Class(name="Nurse")
Doctor = Class(name="Doctor")
Technician = Class(name="Technician")
Medicine = Class(name="Medicine")
Patient = Class(name="Patient")
Appointment = Class(name="Appointment")
Sickness = Class(name="Sickness")
Health_Records = Class(name="Health_Records")

# Person class attributes and methods
Person_name: Property = Property(name="name", type=StringType)
Person_id: Property = Property(name="id", type=IntegerType)
Person_email: Property = Property(name="email", type=StringType)
Person_job: Property = Property(name="job", type=StringType)
Person.attributes={Person_email, Person_id, Person_job, Person_name}

# Staff class attributes and methods
Staff_name: Property = Property(name="name", type=StringType)
Staff_job: Property = Property(name="job", type=StringType)
Staff.attributes={Staff_job, Staff_name}

# Nurse class attributes and methods
Nurse_name: Property = Property(name="name", type=StringType)
Nurse_id: Property = Property(name="id", type=IntegerType)
Nurse.attributes={Nurse_name, Nurse_id}

# Doctor class attributes and methods
Doctor_speciality: Property = Property(name="speciality", type=StringType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_id: Property = Property(name="id", type=IntegerType)
Doctor.attributes={Doctor_name, Doctor_speciality, Doctor_id}

# Technician class attributes and methods
Technician_name: Property = Property(name="name", type=StringType)
Technician_id: Property = Property(name="id", type=IntegerType)
Technician.attributes={Technician_id, Technician_name}

# Medicine class attributes and methods
Medicine_name: Property = Property(name="name", type=StringType)
Medicine_code: Property = Property(name="code", type=IntegerType)
Medicine_price: Property = Property(name="price", type=StringType)
Medicine_amount: Property = Property(name="amount", type=IntegerType)
Medicine.attributes={Medicine_amount, Medicine_price, Medicine_code, Medicine_name}

# Patient class attributes and methods
Patient_healthrecords: Property = Property(name="healthrecords", type=StringType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_id: Property = Property(name="id", type=IntegerType)
Patient.attributes={Patient_healthrecords, Patient_name, Patient_id}

# Appointment class attributes and methods
Appointment_date: Property = Property(name="date", type=StringType)
Appointment_time: Property = Property(name="time", type=IntegerType)
Appointment_location: Property = Property(name="location", type=StringType)
Appointment.attributes={Appointment_date, Appointment_location, Appointment_time}

# Sickness class attributes and methods
Sickness_symptoms: Property = Property(name="symptoms", type=StringType)
Sickness_recommendations: Property = Property(name="recommendations", type=StringType)
Sickness_prescription: Property = Property(name="prescription", type=StringType)
Sickness.attributes={Sickness_prescription, Sickness_recommendations, Sickness_symptoms}

# Health_Records class attributes and methods
Health_Records_healthhistory: Property = Property(name="healthhistory", type=StringType)
Health_Records.attributes={Health_Records_healthhistory}

# Relationships
Appointment_Patient: BinaryAssociation = BinaryAssociation(
    name="Appointment_Patient",
    ends={
        Property(name="appointment15", type=Appointment, multiplicity=Multiplicity(0, 1)),
        Property(name="patient14", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Sickness_Patient: BinaryAssociation = BinaryAssociation(
    name="Sickness_Patient",
    ends={
        Property(name="patient16", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="sickness17", type=Sickness, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Health_Records: BinaryAssociation = BinaryAssociation(
    name="Doctor_Health_Records",
    ends={
        Property(name="health_Records18", type=Health_Records, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor19", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Health_Records_Patient: BinaryAssociation = BinaryAssociation(
    name="Health_Records_Patient",
    ends={
        Property(name="patient20", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="health_Records21", type=Health_Records, multiplicity=Multiplicity(0, 1))
    }
)
Person_Staff: BinaryAssociation = BinaryAssociation(
    name="Person_Staff",
    ends={
        Property(name="staff0", type=Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="person1", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Nurse: BinaryAssociation = BinaryAssociation(
    name="Staff_Nurse",
    ends={
        Property(name="nurse2", type=Nurse, multiplicity=Multiplicity(0, 1)),
        Property(name="staff3", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Doctor: BinaryAssociation = BinaryAssociation(
    name="Staff_Doctor",
    ends={
        Property(name="doctor4", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="staff5", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Technician: BinaryAssociation = BinaryAssociation(
    name="Staff_Technician",
    ends={
        Property(name="technician6", type=Technician, multiplicity=Multiplicity(0, 1)),
        Property(name="staff7", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Medicine: BinaryAssociation = BinaryAssociation(
    name="Doctor_Medicine",
    ends={
        Property(name="medicine8", type=Medicine, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor9", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Person_Patient: BinaryAssociation = BinaryAssociation(
    name="Person_Patient",
    ends={
        Property(name="patient10", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="person11", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
Appointment_Doctor: BinaryAssociation = BinaryAssociation(
    name="Appointment_Doctor",
    ends={
        Property(name="doctor12", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="appointment13", type=Appointment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2c952d14_083b_4ecc_8c26_ad2766562a0b",
    types={Person, Staff, Nurse, Doctor, Technician, Medicine, Patient, Appointment, Sickness, Health_Records},
    associations={Appointment_Patient, Sickness_Patient, Doctor_Health_Records, Health_Records_Patient, Person_Staff, Staff_Nurse, Staff_Doctor, Staff_Technician, Doctor_Medicine, Person_Patient, Appointment_Doctor},
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
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
Patient = Class(name="Patient")
Hospital = Class(name="Hospital")
Staff = Class(name="Staff")
Doctor = Class(name="Doctor")
Department = Class(name="Department")
Operations_Staff = Class(name="Operations_Staff")
Administrative_Staff = Class(name="Administrative_Staff")
Technical_Staff = Class(name="Technical_Staff")
Nurse = Class(name="Nurse")
Front_Desk_Staff = Class(name="Front_Desk_Staff")
Technician = Class(name="Technician")
Technologist = Class(name="Technologist")
Receptionist = Class(name="Receptionist")

# Person class attributes and methods
Person_title: Property = Property(name="title", type=StringType)
Person_givenName: Property = Property(name="givenName", type=StringType)
Person_middleName: Property = Property(name="middleName", type=StringType)
Person_familyName: Property = Property(name="familyName", type=StringType)
Person_name: Property = Property(name="name", type=StringType)
Person_birthDate: Property = Property(name="birthDate", type=StringType)
Person_gender: Property = Property(name="gender", type=StringType)
Person_homeAddress: Property = Property(name="homeAddress", type=StringType)
Person_phone: Property = Property(name="phone", type=StringType)
Person.attributes={Person_phone, Person_middleName, Person_gender, Person_title, Person_name, Person_homeAddress, Person_givenName, Person_familyName, Person_birthDate}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=StringType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_gender: Property = Property(name="gender", type=StringType)
Patient_birthDate: Property = Property(name="birthDate", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_accepted: Property = Property(name="accepted", type=StringType)
Patient_sickness: Property = Property(name="sickness", type=StringType)
Patient_prescriptions: Property = Property(name="prescriptions", type=StringType)
Patient_allergies: Property = Property(name="allergies", type=StringType)
Patient_specialReqs: Property = Property(name="specialReqs", type=StringType)
Patient.attributes={Patient_gender, Patient_prescriptions, Patient_accepted, Patient_birthDate, Patient_age, Patient_sickness, Patient_name, Patient_id, Patient_allergies, Patient_specialReqs}

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_address: Property = Property(name="address", type=StringType)
Hospital_phone: Property = Property(name="phone", type=StringType)
Hospital.attributes={Hospital_address, Hospital_name, Hospital_phone}

# Staff class attributes and methods
Staff_joined: Property = Property(name="joined", type=StringType)
Staff_education: Property = Property(name="education", type=StringType)
Staff_certification: Property = Property(name="certification", type=StringType)
Staff_languages: Property = Property(name="languages", type=StringType)
Staff_UserName: Property = Property(name="UserName", type=StringType)
Staff_Password: Property = Property(name="Password", type=StringType)
Staff.attributes={Staff_joined, Staff_certification, Staff_education, Staff_UserName, Staff_languages, Staff_Password}

# Doctor class attributes and methods
Doctor_specialty: Property = Property(name="specialty", type=StringType)
Doctor_locations: Property = Property(name="locations", type=StringType)
Doctor.attributes={Doctor_locations, Doctor_specialty}

# Department class attributes and methods

# Operations_Staff class attributes and methods

# Administrative_Staff class attributes and methods

# Technical_Staff class attributes and methods

# Nurse class attributes and methods

# Front_Desk_Staff class attributes and methods

# Technician class attributes and methods

# Technologist class attributes and methods

# Receptionist class attributes and methods

# Relationships
Person_Hospital: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital",
    ends={
        Property(name="hospital0", type=Hospital, multiplicity=Multiplicity(0, 9999)),
        Property(name="person1", type=Person, multiplicity=Multiplicity(0, 9999))
    }
)
Hospital_Department: BinaryAssociation = BinaryAssociation(
    name="Hospital_Department",
    ends={
        Property(name="department2", type=Department, multiplicity=Multiplicity(0, 9999)),
        Property(name="hospital3", type=Hospital, multiplicity=Multiplicity(1, 1))
    }
)
Department_Staff: BinaryAssociation = BinaryAssociation(
    name="Department_Staff",
    ends={
        Property(name="staff4", type=Staff, multiplicity=Multiplicity(0, 9999)),
        Property(name="department5", type=Department, multiplicity=Multiplicity(1, 1))
    }
)
Patient_Operations_Staff: BinaryAssociation = BinaryAssociation(
    name="Patient_Operations_Staff",
    ends={
        Property(name="operations_Staff6", type=Operations_Staff, multiplicity=Multiplicity(0, 9999)),
        Property(name="patient7", type=Patient, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c23de5b8_380a_4c6e_a282_a78811ce08e3",
    types={Person, Patient, Hospital, Staff, Doctor, Department, Operations_Staff, Administrative_Staff, Technical_Staff, Nurse, Front_Desk_Staff, Technician, Technologist, Receptionist},
    associations={Person_Hospital, Hospital_Department, Department_Staff, Patient_Operations_Staff},
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
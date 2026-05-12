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
Person = Class(name="Person")
Patient = Class(name="Patient")
Department = Class(name="Department")
Staff = Class(name="Staff")
Operation_Staff = Class(name="Operation_Staff")
Administrative_Staff = Class(name="Administrative_Staff")
Technical_Staff = Class(name="Technical_Staff")
Doctor = Class(name="Doctor")
Nurse = Class(name="Nurse")
Surgeon = Class(name="Surgeon")
Receptionist = Class(name="Receptionist")

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_Address: Property = Property(name="Address", type=StringType)
Hospital_phone_no: Property = Property(name="phone_no", type=StringType)
Hospital.attributes={Hospital_phone_no, Hospital_Address, Hospital_name}

# Person class attributes and methods
Person_name: Property = Property(name="name", type=StringType)
Person_father_s_name: Property = Property(name="father_s_name", type=StringType)
Person_Birth_date: Property = Property(name="Birth_date", type=StringType)
Person_Age: Property = Property(name="Age", type=IntegerType)
Person_Gender: Property = Property(name="Gender", type=StringType)
Person.attributes={Person_name, Person_Birth_date, Person_Age, Person_Gender, Person_father_s_name}

# Patient class attributes and methods
Patient_name: Property = Property(name="name", type=StringType)
Patient_Sickness: Property = Property(name="Sickness", type=StringType)
Patient_Prescription: Property = Property(name="Prescription", type=StringType)
Patient_Allergy: Property = Property(name="Allergy", type=StringType)
Patient.attributes={Patient_Prescription, Patient_Sickness, Patient_name, Patient_Allergy}

# Department class attributes and methods

# Staff class attributes and methods
Staff_Education: Property = Property(name="Education", type=StringType)
Staff_Certification: Property = Property(name="Certification", type=StringType)
Staff_Languages: Property = Property(name="Languages", type=StringType)
Staff.attributes={Staff_Certification, Staff_Education, Staff_Languages}

# Operation_Staff class attributes and methods

# Administrative_Staff class attributes and methods

# Technical_Staff class attributes and methods

# Doctor class attributes and methods
Doctor_Speciality: Property = Property(name="Speciality", type=StringType)
Doctor_Location: Property = Property(name="Location", type=StringType)
Doctor.attributes={Doctor_Location, Doctor_Speciality}

# Nurse class attributes and methods

# Surgeon class attributes and methods

# Receptionist class attributes and methods

# Relationships
Hospital_Department: BinaryAssociation = BinaryAssociation(
    name="Hospital_Department",
    ends={
        Property(name="department0", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="hospital1", type=Hospital, multiplicity=Multiplicity(1, 9999))
    }
)
Department_Staff: BinaryAssociation = BinaryAssociation(
    name="Department_Staff",
    ends={
        Property(name="staff2", type=Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="department3", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Person_Hospital: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital",
    ends={
        Property(name="hospital4", type=Hospital, multiplicity=Multiplicity(0, 1)),
        Property(name="person5", type=Person, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3AEQUMMJEemzkdgWIUToCg",
    types={Hospital, Person, Patient, Department, Staff, Operation_Staff, Administrative_Staff, Technical_Staff, Doctor, Nurse, Surgeon, Receptionist},
    associations={Hospital_Department, Department_Staff, Person_Hospital},
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
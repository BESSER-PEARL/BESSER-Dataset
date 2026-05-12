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
Hospital = Class(name="Hospital")
Patient = Class(name="Patient")
Staff = Class(name="Staff")
Operation_Staff = Class(name="Operation_Staff")
Administrative_Staff = Class(name="Administrative_Staff")
Techinal_Staff = Class(name="Techinal_Staff")

# Person class attributes and methods
Person_Title: Property = Property(name="Title", type=StringType)
Person_FirstName: Property = Property(name="FirstName", type=StringType)
Person_MiddleName: Property = Property(name="MiddleName", type=StringType)
Person_LastName: Property = Property(name="LastName", type=StringType)
Person_PersonHospitalId: Property = Property(name="PersonHospitalId", type=IntegerType)
Person_BirthDate: Property = Property(name="BirthDate", type=StringType)
Person_Gender: Property = Property(name="Gender", type=StringType)
Person_Address: Property = Property(name="Address", type=StringType)
Person_Phone: Property = Property(name="Phone", type=IntegerType)
Person_PersonPatientId: Property = Property(name="PersonPatientId", type=IntegerType)
Person.attributes={Person_Phone, Person_PersonHospitalId, Person_Address, Person_Title, Person_BirthDate, Person_LastName, Person_MiddleName, Person_Gender, Person_PersonPatientId, Person_FirstName}

# Hospital class attributes and methods
Hospital_Address: Property = Property(name="Address", type=StringType)
Hospital_Phone: Property = Property(name="Phone", type=IntegerType)
Hospital_HospitalId: Property = Property(name="HospitalId", type=IntegerType)
Hospital_Name: Property = Property(name="Name", type=StringType)
Hospital.attributes={Hospital_Address, Hospital_Phone, Hospital_HospitalId, Hospital_Name}

# Patient class attributes and methods
Patient_PatientId: Property = Property(name="PatientId", type=IntegerType)
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_Gender: Property = Property(name="Gender", type=StringType)
Patient_Birthdate: Property = Property(name="Birthdate", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_DateOfEntry: Property = Property(name="DateOfEntry", type=StringType)
Patient_Sickness: Property = Property(name="Sickness", type=StringType)
Patient.attributes={Patient_Name, Patient_Age, Patient_PatientId, Patient_Gender, Patient_Sickness, Patient_DateOfEntry, Patient_Birthdate}

# Staff class attributes and methods
Staff_Joined: Property = Property(name="Joined", type=StringType)
Staff_Education: Property = Property(name="Education", type=StringType)
Staff_Certification: Property = Property(name="Certification", type=StringType)
Staff_Languages: Property = Property(name="Languages", type=StringType)
Staff.attributes={Staff_Education, Staff_Joined, Staff_Languages, Staff_Certification}

# Operation_Staff class attributes and methods
Operation_Staff_DoctorSpeciality: Property = Property(name="DoctorSpeciality", type=StringType)
Operation_Staff_DoctorLocation: Property = Property(name="DoctorLocation", type=StringType)
Operation_Staff_NurseName: Property = Property(name="NurseName", type=StringType)
Operation_Staff.attributes={Operation_Staff_NurseName, Operation_Staff_DoctorSpeciality, Operation_Staff_DoctorLocation}

# Administrative_Staff class attributes and methods
Administrative_Staff_FrontDeskStaffName: Property = Property(name="FrontDeskStaffName", type=StringType)
Administrative_Staff_ReceptionistName: Property = Property(name="ReceptionistName", type=StringType)
Administrative_Staff.attributes={Administrative_Staff_FrontDeskStaffName, Administrative_Staff_ReceptionistName}

# Techinal_Staff class attributes and methods
Techinal_Staff_Technician: Property = Property(name="Technician", type=StringType)
Techinal_Staff_Technologist: Property = Property(name="Technologist", type=StringType)
Techinal_Staff.attributes={Techinal_Staff_Technologist, Techinal_Staff_Technician}

# Relationships
Person_Hospital: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital",
    ends={
        Property(name="hospital0", type=Hospital, multiplicity=Multiplicity(0, 9999)),
        Property(name="person1", type=Person, multiplicity=Multiplicity(0, 9999))
    }
)
Staff_Hospital: BinaryAssociation = BinaryAssociation(
    name="Staff_Hospital",
    ends={
        Property(name="hospital2", type=Hospital, multiplicity=Multiplicity(0, 9999)),
        Property(name="staff3", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
Operation_Staff_Patient: BinaryAssociation = BinaryAssociation(
    name="Operation_Staff_Patient",
    ends={
        Property(name="patient4", type=Patient, multiplicity=Multiplicity(0, 9999)),
        Property(name="operation_Staff5", type=Operation_Staff, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_SxnJ4AaQEeqFfO0RhT_ZfA",
    types={Person, Hospital, Patient, Staff, Operation_Staff, Administrative_Staff, Techinal_Staff},
    associations={Person_Hospital, Staff_Hospital, Operation_Staff_Patient},
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
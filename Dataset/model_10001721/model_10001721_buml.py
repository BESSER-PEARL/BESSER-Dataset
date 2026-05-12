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
Staff = Class(name="Staff")
Person = Class(name="Person")
Patient = Class(name="Patient")
Doctor = Class(name="Doctor")
SystemAdministrator = Class(name="SystemAdministrator")
HospitalSystem = Class(name="HospitalSystem")

# Staff class attributes and methods
Staff_Status: Property = Property(name="Status", type=StringType)
Staff_Joined: Property = Property(name="Joined", type=StringType)
Staff_Education: Property = Property(name="Education", type=StringType)
Staff_Certification: Property = Property(name="Certification", type=StringType)
Staff_Languages: Property = Property(name="Languages", type=StringType)
Staff.attributes={Staff_Joined, Staff_Certification, Staff_Education, Staff_Status, Staff_Languages}

# Person class attributes and methods
Person_FullName: Property = Property(name="FullName", type=StringType)
Person_BirthDate: Property = Property(name="BirthDate", type=StringType)
Person_Gender: Property = Property(name="Gender", type=StringType)
Person_ID: Property = Property(name="ID", type=IntegerType)
Person_AccessLevel: Property = Property(name="AccessLevel", type=StringType)
Person.attributes={Person_FullName, Person_ID, Person_BirthDate, Person_AccessLevel, Person_Gender}

# Patient class attributes and methods
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Phone: Property = Property(name="Phone", type=StringType)
Patient_DiseaseHistory: Property = Property(name="DiseaseHistory", type=StringType)
Patient_Prescriptions: Property = Property(name="Prescriptions", type=StringType)
Patient.attributes={Patient_Address, Patient_Prescriptions, Patient_Phone, Patient_Age, Patient_DiseaseHistory}

# Doctor class attributes and methods
Doctor_Shedule: Property = Property(name="Shedule", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor.attributes={Doctor_Shedule, Doctor_Specialization}

# SystemAdministrator class attributes and methods
SystemAdministrator_Patients: Property = Property(name="Patients", type=StringType)
SystemAdministrator_Doctors: Property = Property(name="Doctors", type=StringType)
SystemAdministrator.attributes={SystemAdministrator_Patients, SystemAdministrator_Doctors}

# HospitalSystem class attributes and methods
HospitalSystem_Patients: Property = Property(name="Patients", type=StringType)
HospitalSystem_Doctors: Property = Property(name="Doctors", type=StringType)
HospitalSystem_admin: Property = Property(name="admin", type=SystemAdministrator)
HospitalSystem.attributes={HospitalSystem_Patients, HospitalSystem_admin, HospitalSystem_Doctors}

# Relationships
HospitalSystem_SystemAdministrator: BinaryAssociation = BinaryAssociation(
    name="HospitalSystem_SystemAdministrator",
    ends={
        Property(name="systemAdministrator0", type=SystemAdministrator, multiplicity=Multiplicity(0, 1)),
        Property(name="hospitalSystem1", type=HospitalSystem, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_QoNUwNnpEeeQi8PFukjNiw",
    types={Staff, Person, Patient, Doctor, SystemAdministrator, HospitalSystem},
    associations={HospitalSystem_SystemAdministrator},
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
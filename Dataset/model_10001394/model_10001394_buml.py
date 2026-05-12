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
Hospital_Patients = Class(name="Hospital_Patients")
Hospital = Class(name="Hospital")
Hospital__Receptionist = Class(name="Hospital__Receptionist")
Hospital_Doctor = Class(name="Hospital_Doctor")

# Hospital_Patients class attributes and methods
Hospital_Patients_Patient_s_Name: Property = Property(name="Patient_s_Name", type=StringType)
Hospital_Patients_NIC_Number: Property = Property(name="NIC_Number", type=IntegerType)
Hospital_Patients_Sickness: Property = Property(name="Sickness", type=StringType)
Hospital_Patients_Phone_Number: Property = Property(name="Phone_Number", type=IntegerType)
Hospital_Patients.attributes={Hospital_Patients_Sickness, Hospital_Patients_Patient_s_Name, Hospital_Patients_NIC_Number, Hospital_Patients_Phone_Number}

# Hospital class attributes and methods
Hospital_HR: Property = Property(name="HR", type=StringType)
Hospital_Operation_Theater: Property = Property(name="Operation_Theater", type=StringType)
Hospital_Cancer_Center: Property = Property(name="Cancer_Center", type=StringType)
Hospital_Cardiology: Property = Property(name="Cardiology", type=StringType)
Hospital.attributes={Hospital_Operation_Theater, Hospital_Cardiology, Hospital_Cancer_Center, Hospital_HR}

# Hospital__Receptionist class attributes and methods
Hospital__Receptionist_Employee_ID: Property = Property(name="Employee_ID", type=IntegerType)
Hospital__Receptionist_Name: Property = Property(name="Name", type=StringType)
Hospital__Receptionist.attributes={Hospital__Receptionist_Name, Hospital__Receptionist_Employee_ID}

# Hospital_Doctor class attributes and methods
Hospital_Doctor_ID: Property = Property(name="ID", type=IntegerType)
Hospital_Doctor_Name: Property = Property(name="Name", type=StringType)
Hospital_Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Hospital_Doctor_Rank: Property = Property(name="Rank", type=StringType)
Hospital_Doctor_Salary: Property = Property(name="Salary", type=IntegerType)
Hospital_Doctor.attributes={Hospital_Doctor_Salary, Hospital_Doctor_Specialization, Hospital_Doctor_ID, Hospital_Doctor_Rank, Hospital_Doctor_Name}

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient0", type=Hospital_Patients, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor1", type=Hospital_Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Patients__Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patients__Receptionist",
    ends={
        Property(name="Receptionist2", type=Hospital__Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="patients3", type=Hospital_Patients, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4GwVEKhMEeeEQN1ZyOr__g",
    types={Hospital_Patients, Hospital, Hospital__Receptionist, Hospital_Doctor},
    associations={Doctor_Patient, Patients__Receptionist},
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
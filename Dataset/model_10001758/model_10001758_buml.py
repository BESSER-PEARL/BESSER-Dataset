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
Employee = Class(name="Employee")
Nurse = Class(name="Nurse")
Doctor = Class(name="Doctor")
patient = Class(name="patient")
Room = Class(name="Room")
Receiptionist = Class(name="Receiptionist")

# Employee class attributes and methods
Employee_Emp_ID: Property = Property(name="Emp_ID", type=IntegerType)
Employee_Emp_Name: Property = Property(name="Emp_Name", type=StringType)
Employee_Contact_NO: Property = Property(name="Contact_NO", type=IntegerType)
Employee_Address: Property = Property(name="Address", type=StringType)
Employee_Salary: Property = Property(name="Salary", type=StringType)
Employee_Designation: Property = Property(name="Designation", type=StringType)
Employee_Joindate: Property = Property(name="Joindate", type=StringType)
Employee.attributes={Employee_Emp_Name, Employee_Address, Employee_Designation, Employee_Emp_ID, Employee_Joindate, Employee_Salary, Employee_Contact_NO}

# Nurse class attributes and methods

# Doctor class attributes and methods

# patient class attributes and methods
patient_Patient_ID: Property = Property(name="Patient_ID", type=IntegerType)
patient_Patient_Name: Property = Property(name="Patient_Name", type=StringType)
patient_Patient_Address: Property = Property(name="Patient_Address", type=StringType)
patient_Patient_Contact_NO: Property = Property(name="Patient_Contact_NO", type=IntegerType)
patient_DOB: Property = Property(name="DOB", type=StringType)
patient_Sex: Property = Property(name="Sex", type=StringType)
patient_Status: Property = Property(name="Status", type=StringType)
patient.attributes={patient_Patient_Name, patient_Status, patient_Sex, patient_Patient_Address, patient_DOB, patient_Patient_Contact_NO, patient_Patient_ID}

# Room class attributes and methods
Room_Room_Rent: Property = Property(name="Room_Rent", type=StringType)
Room_Room_NO: Property = Property(name="Room_NO", type=IntegerType)
Room_Room_TYPE: Property = Property(name="Room_TYPE", type=StringType)
Room.attributes={Room_Room_TYPE, Room_Room_NO, Room_Room_Rent}

# Receiptionist class attributes and methods

# Relationships
Doctor_patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_patient",
    ends={
        Property(name="patient0", type=patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Receiptionist_patient: BinaryAssociation = BinaryAssociation(
    name="Receiptionist_patient",
    ends={
        Property(name="patient2", type=patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="receiptionist3", type=Receiptionist, multiplicity=Multiplicity(1, 9999))
    }
)
patient_Room: BinaryAssociation = BinaryAssociation(
    name="patient_Room",
    ends={
        Property(name="room4", type=Room, multiplicity=Multiplicity(1, 9999)),
        Property(name="patient5", type=patient, multiplicity=Multiplicity(1, 9999))
    }
)
Nurse_Room: BinaryAssociation = BinaryAssociation(
    name="Nurse_Room",
    ends={
        Property(name="room6", type=Room, multiplicity=Multiplicity(1, 9999)),
        Property(name="nurse7", type=Nurse, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_TVsYEMZIEeeWu_SLkciAbg",
    types={Employee, Nurse, Doctor, patient, Room, Receiptionist},
    associations={Doctor_patient, Receiptionist_patient, patient_Room, Nurse_Room},
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
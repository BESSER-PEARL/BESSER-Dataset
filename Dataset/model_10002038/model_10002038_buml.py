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
Doctor = Class(name="Doctor")
Bill = Class(name="Bill")
Patient = Class(name="Patient")
Nurse = Class(name="Nurse")

# Doctor class attributes and methods
Doctor_DoctorID: Property = Property(name="DoctorID", type=IntegerType)
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_DepartmentID: Property = Property(name="DepartmentID", type=IntegerType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor_attribute: Property = Property(name="attribute", type=StringType)
Doctor_PhoneNo: Property = Property(name="PhoneNo", type=StringType)
Doctor_Address: Property = Property(name="Address", type=StringType)
Doctor.attributes={Doctor_attribute, Doctor_DepartmentID, Doctor_Specialization, Doctor_Address, Doctor_PhoneNo, Doctor_Name, Doctor_DoctorID}

# Bill class attributes and methods
Bill_PatientName: Property = Property(name="PatientName", type=StringType)
Bill_Amount: Property = Property(name="Amount", type=StringType)
Bill.attributes={Bill_PatientName, Bill_Amount}

# Patient class attributes and methods
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_PatientID: Property = Property(name="PatientID", type=IntegerType)
Patient_TelephoneNo: Property = Property(name="TelephoneNo", type=StringType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_Sex: Property = Property(name="Sex", type=StringType)
Patient_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Patient.attributes={Patient_Name, Patient_Age, Patient_Sex, Patient_TelephoneNo, Patient_PatientID, Patient_Address, Patient_RoomNo}

# Nurse class attributes and methods
Nurse_ID: Property = Property(name="ID", type=IntegerType)
Nurse_Name: Property = Property(name="Name", type=StringType)
Nurse.attributes={Nurse_ID, Nurse_Name}

# Relationships
Nurse_Patient: BinaryAssociation = BinaryAssociation(
    name="Nurse_Patient",
    ends={
        Property(name="patient6", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="nurse7", type=Nurse, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient0", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_bill: BinaryAssociation = BinaryAssociation(
    name="Patient_bill",
    ends={
        Property(name="bill2", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="patient3", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Nurse_Doctor: BinaryAssociation = BinaryAssociation(
    name="Nurse_Doctor",
    ends={
        Property(name="doctor4", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="nurse5", type=Nurse, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kuzu4NTAEeehRMl7r1_c5g",
    types={Doctor, Bill, Patient, Nurse},
    associations={Nurse_Patient, Doctor_Patient, Patient_bill, Nurse_Doctor},
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
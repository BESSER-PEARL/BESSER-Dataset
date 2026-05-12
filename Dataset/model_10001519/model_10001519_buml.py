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
Patient = Class(name="Patient")
Ward = Class(name="Ward")
Department = Class(name="Department")
Bill = Class(name="Bill")
Receptionist = Class(name="Receptionist")

# Doctor class attributes and methods
Doctor_DocID: Property = Property(name="DocID", type=StringType)
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_Department: Property = Property(name="Department", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=IntegerType)
Doctor_PhoneNumber: Property = Property(name="PhoneNumber", type=IntegerType)
Doctor_Address: Property = Property(name="Address", type=StringType)
Doctor.attributes={Doctor_Address, Doctor_Name, Doctor_Department, Doctor_PhoneNumber, Doctor_DocID, Doctor_Specialization}

# Patient class attributes and methods
Patient_PatientID: Property = Property(name="PatientID", type=IntegerType)
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=StringType)
Patient_WardNo: Property = Property(name="WardNo", type=IntegerType)
Patient_Gender: Property = Property(name="Gender", type=StringType)
Patient.attributes={Patient_WardNo, Patient_Gender, Patient_PatientID, Patient_Age, Patient_Address, Patient_Name}

# Ward class attributes and methods
Ward_wardNo: Property = Property(name="wardNo", type=IntegerType)
Ward_Location: Property = Property(name="Location", type=StringType)
Ward.attributes={Ward_Location, Ward_wardNo}

# Department class attributes and methods
Department_deptID: Property = Property(name="deptID", type=StringType)
Department_Name: Property = Property(name="Name", type=StringType)
Department_DocID: Property = Property(name="DocID", type=StringType)
Department.attributes={Department_Name, Department_deptID, Department_DocID}

# Bill class attributes and methods
Bill_BillNo: Property = Property(name="BillNo", type=IntegerType)
Bill_patientName: Property = Property(name="patientName", type=StringType)
Bill_amount: Property = Property(name="amount", type=IntegerType)
Bill.attributes={Bill_patientName, Bill_BillNo, Bill_amount}

# Receptionist class attributes and methods

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="checks0", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Department: BinaryAssociation = BinaryAssociation(
    name="Doctor_Department",
    ends={
        Property(name="department2", type=Department, multiplicity=Multiplicity(1, 1)),
        Property(name="belongs_to3", type=Doctor, multiplicity=Multiplicity(0, 9999))
    }
)
Patient_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patient_Receptionist",
    ends={
        Property(name="give_appointment4", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="patient5", type=Patient, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Ward: BinaryAssociation = BinaryAssociation(
    name="Patient_Ward",
    ends={
        Property(name="alloted_to6", type=Ward, multiplicity=Multiplicity(1, 1)),
        Property(name="patient7", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="pays_bill8", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="patient9", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_Bill: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Bill",
    ends={
        Property(name="bill10", type=Bill, multiplicity=Multiplicity(0, 9999)),
        Property(name="generates_bill11", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_DEPWUAcrEeeoBvzX9wJhsQ",
    types={Doctor, Patient, Ward, Department, Bill, Receptionist},
    associations={Doctor_Patient, Doctor_Department, Patient_Receptionist, Patient_Ward, Patient_Bill, Receptionist_Bill},
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
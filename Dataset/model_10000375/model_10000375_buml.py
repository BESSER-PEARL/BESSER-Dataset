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
Receptionist = Class(name="Receptionist")
Bill = Class(name="Bill")
Room = Class(name="Room")

# Doctor class attributes and methods
Doctor_DocId_: Property = Property(name="DocId_", type=IntegerType)
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_Department: Property = Property(name="Department", type=StringType)
Doctor_Address: Property = Property(name="Address", type=StringType)
Doctor_Email: Property = Property(name="Email", type=StringType)
Doctor.attributes={Doctor_Address, Doctor_DocId_, Doctor_Department, Doctor_Email, Doctor_Name}

# Patient class attributes and methods
Patient_Id: Property = Property(name="Id", type=IntegerType)
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_PhNo_: Property = Property(name="PhNo_", type=IntegerType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_WardNo: Property = Property(name="WardNo", type=IntegerType)
Patient.attributes={Patient_Age, Patient_Address, Patient_PhNo_, Patient_Name, Patient_Id, Patient_WardNo}

# Receptionist class attributes and methods
Receptionist_Id: Property = Property(name="Id", type=IntegerType)
Receptionist_Name: Property = Property(name="Name", type=StringType)
Receptionist_Email: Property = Property(name="Email", type=StringType)
Receptionist.attributes={Receptionist_Email, Receptionist_Name, Receptionist_Id}

# Bill class attributes and methods
Bill_BillNo: Property = Property(name="BillNo", type=StringType)
Bill_Patient_Id: Property = Property(name="Patient_Id", type=IntegerType)
Bill_Amount: Property = Property(name="Amount", type=StringType)
Bill.attributes={Bill_BillNo, Bill_Amount, Bill_Patient_Id}

# Room class attributes and methods
Room_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Room_RoomType: Property = Property(name="RoomType", type=StringType)
Room.attributes={Room_RoomType, Room_RoomNo}

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient0", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patient_Receptionist",
    ends={
        Property(name="receptionist2", type=Receptionist, multiplicity=Multiplicity(0, 1)),
        Property(name="patient3", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Bill: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Bill",
    ends={
        Property(name="bill4", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist5", type=Receptionist, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="bill6", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="patient7", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Rooms: BinaryAssociation = BinaryAssociation(
    name="Patient_Rooms",
    ends={
        Property(name="rooms8", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="patient9", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2f088655_b2c6_4385_8999_29494b86d9cd",
    types={Doctor, Patient, Receptionist, Bill, Room},
    associations={Doctor_Patient, Patient_Receptionist, Receptionist_Bill, Patient_Bill, Patient_Rooms},
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
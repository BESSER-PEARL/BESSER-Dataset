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
Receptionist = Class(name="Receptionist")
Patient = Class(name="Patient")
Doctor = Class(name="Doctor")
Bill = Class(name="Bill")
Department = Class(name="Department")
Rooms = Class(name="Rooms")
Staff = Class(name="Staff")
char_Interface = Class(name="char_Interface")

# Receptionist class attributes and methods
Receptionist_Rid: Property = Property(name="Rid", type=StringType)
Receptionist_Rname: Property = Property(name="Rname", type=StringType)
Receptionist.attributes={Receptionist_Rid, Receptionist_Rname}

# Patient class attributes and methods
Patient_Pid: Property = Property(name="Pid", type=IntegerType)
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_TelNO: Property = Property(name="TelNO", type=IntegerType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_Sex: Property = Property(name="Sex", type=IntegerType)
Patient_RoomNo_: Property = Property(name="RoomNo_", type=IntegerType)
Patient.attributes={Patient_TelNO, Patient_Pid, Patient_RoomNo_, Patient_Age, Patient_Sex, Patient_Name, Patient_Address}

# Doctor class attributes and methods
Doctor_DocID: Property = Property(name="DocID", type=IntegerType)
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_Department: Property = Property(name="Department", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor_PhNo: Property = Property(name="PhNo", type=IntegerType)
Doctor_Address: Property = Property(name="Address", type=StringType)
Doctor.attributes={Doctor_Department, Doctor_Name, Doctor_Address, Doctor_Specialization, Doctor_PhNo, Doctor_DocID}

# Bill class attributes and methods
Bill_Bill_No: Property = Property(name="Bill_No", type=StringType)
Bill_Patient_Name: Property = Property(name="Patient_Name", type=StringType)
Bill_Amount: Property = Property(name="Amount", type=StringType)
Bill.attributes={Bill_Patient_Name, Bill_Bill_No, Bill_Amount}

# Department class attributes and methods
Department_ID: Property = Property(name="ID", type=IntegerType)
Department_Name: Property = Property(name="Name", type=StringType)
Department_Doctor_ID: Property = Property(name="Doctor_ID", type=IntegerType)
Department.attributes={Department_Doctor_ID, Department_ID, Department_Name}

# Rooms class attributes and methods
Rooms_Room_No: Property = Property(name="Room_No", type=IntegerType)
Rooms_Location: Property = Property(name="Location", type=StringType)
Rooms.attributes={Rooms_Location, Rooms_Room_No}

# Staff class attributes and methods
Staff_ID: Property = Property(name="ID", type=IntegerType)
Staff_Name: Property = Property(name="Name", type=StringType)
Staff_Type: Property = Property(name="Type", type=StringType)
Staff.attributes={Staff_Type, Staff_Name, Staff_ID}

# char_Interface class attributes and methods

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="Doctor_Patient_00", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="Doctor_Patient_11", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patient_Receptionist",
    ends={
        Property(name="Patient_Receptionist_02", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="Patient_Receptionist_13", type=Patient, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="Patient_Bill_04", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="patient5", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_Bill2: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Bill2",
    ends={
        Property(name="bill6", type=Bill, multiplicity=Multiplicity(1, 9999)),
        Property(name="receptionist7", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)
Patient_Rooms: BinaryAssociation = BinaryAssociation(
    name="Patient_Rooms",
    ends={
        Property(name="Patient_Rooms_08", type=Rooms, multiplicity=Multiplicity(1, 9999)),
        Property(name="Patient_Rooms_19", type=Patient, multiplicity=Multiplicity(1, 9999))
    }
)
Doctor_Department: BinaryAssociation = BinaryAssociation(
    name="Doctor_Department",
    ends={
        Property(name="Doctor_Department_010", type=Department, multiplicity=Multiplicity(1, 1)),
        Property(name="Doctor_Department_111", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Rooms_Staff: BinaryAssociation = BinaryAssociation(
    name="Rooms_Staff",
    ends={
        Property(name="staff12", type=Staff, multiplicity=Multiplicity(1, 9999)),
        Property(name="Rooms_Staff_113", type=Rooms, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_1veKUJkGEeexEbmG8xrwVA",
    types={Receptionist, Patient, Doctor, Bill, Department, Rooms, Staff, char_Interface},
    associations={Doctor_Patient, Patient_Receptionist, Patient_Bill, Receptionist_Bill2, Patient_Rooms, Doctor_Department, Rooms_Staff},
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
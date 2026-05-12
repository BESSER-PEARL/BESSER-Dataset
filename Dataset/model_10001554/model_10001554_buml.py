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
ReceptionList = Class(name="ReceptionList")
Bill = Class(name="Bill")
Rooms = Class(name="Rooms")
Dept = Class(name="Dept")
Float = Class(name="Float")
system_Component = Class(name="system_Component")

# Doctor class attributes and methods
Doctor_docId: Property = Property(name="docId", type=IntegerType)
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_Dept: Property = Property(name="Dept", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor_PhoneNo: Property = Property(name="PhoneNo", type=IntegerType)
Doctor_Location: Property = Property(name="Location", type=StringType)
Doctor.attributes={Doctor_Location, Doctor_Dept, Doctor_docId, Doctor_Specialization, Doctor_PhoneNo, Doctor_Name}

# Patient class attributes and methods
Patient_PatientId: Property = Property(name="PatientId", type=IntegerType)
Patient_PatientName: Property = Property(name="PatientName", type=StringType)
Patient_PhoneNo: Property = Property(name="PhoneNo", type=IntegerType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_Sex: Property = Property(name="Sex", type=StringType)
Patient_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Patient.attributes={Patient_PatientId, Patient_Age, Patient_PhoneNo, Patient_Sex, Patient_PatientName, Patient_Address, Patient_RoomNo}

# ReceptionList class attributes and methods
ReceptionList_RepId: Property = Property(name="RepId", type=IntegerType)
ReceptionList_name: Property = Property(name="name", type=StringType)
ReceptionList.attributes={ReceptionList_name, ReceptionList_RepId}

# Bill class attributes and methods
Bill_BillId: Property = Property(name="BillId", type=IntegerType)
Bill_PatientName: Property = Property(name="PatientName", type=StringType)
Bill_Amount: Property = Property(name="Amount", type=Float)
Bill.attributes={Bill_Amount, Bill_BillId, Bill_PatientName}

# Rooms class attributes and methods
Rooms_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Rooms_Location: Property = Property(name="Location", type=StringType)
Rooms.attributes={Rooms_Location, Rooms_RoomNo}

# Dept class attributes and methods
Dept_Id: Property = Property(name="Id", type=IntegerType)
Dept_Name: Property = Property(name="Name", type=StringType)
Dept_DocId: Property = Property(name="DocId", type=IntegerType)
Dept.attributes={Dept_DocId, Dept_Id, Dept_Name}

# Float class attributes and methods

# system_Component class attributes and methods

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient0", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_ReceptionList: BinaryAssociation = BinaryAssociation(
    name="Patient_ReceptionList",
    ends={
        Property(name="receptionList2", type=ReceptionList, multiplicity=Multiplicity(1, 1)),
        Property(name="patient3", type=Patient, multiplicity=Multiplicity(1, 9999))
    }
)
Bill_Patient: BinaryAssociation = BinaryAssociation(
    name="Bill_Patient",
    ends={
        Property(name="patient4", type=Patient, multiplicity=Multiplicity(1, 1)),
        Property(name="bill5", type=Bill, multiplicity=Multiplicity(1, 1))
    }
)
Bill_ReceptionList: BinaryAssociation = BinaryAssociation(
    name="Bill_ReceptionList",
    ends={
        Property(name="receptionList6", type=ReceptionList, multiplicity=Multiplicity(1, 1)),
        Property(name="bill7", type=Bill, multiplicity=Multiplicity(0, 9999))
    }
)
Rooms_Patient: BinaryAssociation = BinaryAssociation(
    name="Rooms_Patient",
    ends={
        Property(name="patient8", type=Patient, multiplicity=Multiplicity(1, 1)),
        Property(name="rooms9", type=Rooms, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Dept: BinaryAssociation = BinaryAssociation(
    name="Doctor_Dept",
    ends={
        Property(name="dept10", type=Dept, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor11", type=Doctor, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_FPUYkAG3EeiLEbIzy5aHfg",
    types={Doctor, Patient, ReceptionList, Bill, Rooms, Dept, Float, system_Component},
    associations={Doctor_Patient, Patient_ReceptionList, Bill_Patient, Bill_ReceptionList, Rooms_Patient, Doctor_Dept},
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
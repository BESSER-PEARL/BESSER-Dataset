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
Rooms = Class(name="Rooms")
Bill = Class(name="Bill")
Dept = Class(name="Dept")
e = Class(name="e")
ff = Class(name="ff")

# Doctor class attributes and methods
Doctor_Docid: Property = Property(name="Docid", type=IntegerType)
Doctor_DocName: Property = Property(name="DocName", type=StringType)
Doctor_Dept: Property = Property(name="Dept", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor_Phoneno: Property = Property(name="Phoneno", type=StringType)
Doctor_Location: Property = Property(name="Location", type=StringType)
Doctor.attributes={Doctor_Location, Doctor_Phoneno, Doctor_Specialization, Doctor_DocName, Doctor_Docid, Doctor_Dept}

# Patient class attributes and methods
Patient_Patientid: Property = Property(name="Patientid", type=IntegerType)
Patient_PatientName: Property = Property(name="PatientName", type=StringType)
Patient_PhoneNo: Property = Property(name="PhoneNo", type=IntegerType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_Sex: Property = Property(name="Sex", type=StringType)
Patient_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Patient.attributes={Patient_Patientid, Patient_Age, Patient_PatientName, Patient_Address, Patient_PhoneNo, Patient_RoomNo, Patient_Sex}

# Receptionist class attributes and methods
Receptionist_Receptionid: Property = Property(name="Receptionid", type=IntegerType)
Receptionist_RecName: Property = Property(name="RecName", type=StringType)
Receptionist.attributes={Receptionist_RecName, Receptionist_Receptionid}

# Rooms class attributes and methods
Rooms_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Rooms_Location: Property = Property(name="Location", type=StringType)
Rooms.attributes={Rooms_Location, Rooms_RoomNo}

# Bill class attributes and methods
Bill_BillNo: Property = Property(name="BillNo", type=StringType)
Bill_PatientName: Property = Property(name="PatientName", type=StringType)
Bill_Amt: Property = Property(name="Amt", type=StringType)
Bill.attributes={Bill_Amt, Bill_PatientName, Bill_BillNo}

# Dept class attributes and methods
Dept_id: Property = Property(name="id", type=IntegerType)
Dept_DeptName: Property = Property(name="DeptName", type=StringType)
Dept_Docid: Property = Property(name="Docid", type=IntegerType)
Dept.attributes={Dept_id, Dept_DeptName, Dept_Docid}

# e class attributes and methods
e_ee: Property = Property(name="ee", type=IntegerType)
e.attributes={e_ee}

# ff class attributes and methods
ff_fd: Property = Property(name="fd", type=IntegerType)
ff.attributes={ff_fd}

# Relationships
Patient_Rooms: BinaryAssociation = BinaryAssociation(
    name="Patient_Rooms",
    ends={
        Property(name="rooms8", type=Rooms, multiplicity=Multiplicity(1, 1)),
        Property(name="Patient_Rooms_19", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="Patient_Bill_010", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="patient11", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
e_ff: BinaryAssociation = BinaryAssociation(
    name="e_ff",
    ends={
        Property(name="ff12", type=ff, multiplicity=Multiplicity(0, 1)),
        Property(name="e13", type=e, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient0", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Patient_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patient_Receptionist",
    ends={
        Property(name="receptionist2", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="patient3", type=Patient, multiplicity=Multiplicity(1, 9999))
    }
)
Receptionist_Bill: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Bill",
    ends={
        Property(name="bill4", type=Bill, multiplicity=Multiplicity(1, 9999)),
        Property(name="receptionist5", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Dept: BinaryAssociation = BinaryAssociation(
    name="Doctor_Dept",
    ends={
        Property(name="dept6", type=Dept, multiplicity=Multiplicity(1, 1)),
        Property(name="Doctor_Dept_17", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_eL5SIK3JEee6S77dw3LIvQ",
    types={Doctor, Patient, Receptionist, Rooms, Bill, Dept, e, ff},
    associations={Patient_Rooms, Patient_Bill, e_ff, Doctor_Patient, Patient_Receptionist, Receptionist_Bill, Doctor_Dept},
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
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
Rooms = Class(name="Rooms")
Doctor = Class(name="Doctor")
Dept = Class(name="Dept")
Bill = Class(name="Bill")
Patient = Class(name="Patient")
Staff = Class(name="Staff")

# Receptionist class attributes and methods
Receptionist_Receptional_id: Property = Property(name="Receptional_id", type=IntegerType)
Receptionist_Name: Property = Property(name="Name", type=StringType)
Receptionist.attributes={Receptionist_Name, Receptionist_Receptional_id}

# Rooms class attributes and methods
Rooms_Roomno_: Property = Property(name="Roomno_", type=IntegerType)
Rooms_Location: Property = Property(name="Location", type=StringType)
Rooms.attributes={Rooms_Roomno_, Rooms_Location}

# Doctor class attributes and methods
Doctor_Doct_id: Property = Property(name="Doct_id", type=IntegerType)
Doctor_DocName: Property = Property(name="DocName", type=StringType)
Doctor_Dept: Property = Property(name="Dept", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor_PhoneNo_: Property = Property(name="PhoneNo_", type=IntegerType)
Doctor_Location: Property = Property(name="Location", type=StringType)
Doctor.attributes={Doctor_DocName, Doctor_PhoneNo_, Doctor_Dept, Doctor_Location, Doctor_Doct_id, Doctor_Specialization}

# Dept class attributes and methods
Dept_Id: Property = Property(name="Id", type=IntegerType)
Dept_Name: Property = Property(name="Name", type=StringType)
Dept_Doc_id: Property = Property(name="Doc_id", type=IntegerType)
Dept.attributes={Dept_Name, Dept_Id, Dept_Doc_id}

# Bill class attributes and methods
Bill_BillNo_: Property = Property(name="BillNo_", type=StringType)
Bill_PatientName: Property = Property(name="PatientName", type=StringType)
Bill_Amount: Property = Property(name="Amount", type=IntegerType)
Bill.attributes={Bill_Amount, Bill_PatientName, Bill_BillNo_}

# Patient class attributes and methods
Patient_PhoneNo_: Property = Property(name="PhoneNo_", type=IntegerType)
Patient_Patient_id: Property = Property(name="Patient_id", type=IntegerType)
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_Sex: Property = Property(name="Sex", type=StringType)
Patient_RoomNo_: Property = Property(name="RoomNo_", type=IntegerType)
Patient.attributes={Patient_Age, Patient_Name, Patient_Patient_id, Patient_Sex, Patient_PhoneNo_, Patient_RoomNo_, Patient_Address}

# Staff class attributes and methods
Staff_Type: Property = Property(name="Type", type=StringType)
Staff_Id: Property = Property(name="Id", type=IntegerType)
Staff_Staff_name: Property = Property(name="Staff_name", type=StringType)
Staff.attributes={Staff_Staff_name, Staff_Type, Staff_Id}

# Relationships
Class_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Class_Receptionist",
    ends={
        Property(name="receptionist0", type=Receptionist, multiplicity=Multiplicity(0, 1)),
        Property(name="Class_Receptionist_11", type=Bill, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Patient: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Patient",
    ends={
        Property(name="patient2", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist3", type=Receptionist, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Doctor: BinaryAssociation = BinaryAssociation(
    name="Patient_Doctor",
    ends={
        Property(name="doctor4", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="patient5", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Dept: BinaryAssociation = BinaryAssociation(
    name="Doctor_Dept",
    ends={
        Property(name="dept6", type=Dept, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor7", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Rooms: BinaryAssociation = BinaryAssociation(
    name="Patient_Rooms",
    ends={
        Property(name="rooms8", type=Rooms, multiplicity=Multiplicity(0, 1)),
        Property(name="patient9", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="bill10", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="patient11", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Rooms_Staff: BinaryAssociation = BinaryAssociation(
    name="Rooms_Staff",
    ends={
        Property(name="staff12", type=Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="rooms13", type=Rooms, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vv_XwAZtEeipbtix_oa2Dg",
    types={Receptionist, Rooms, Doctor, Dept, Bill, Patient, Staff},
    associations={Class_Receptionist, Receptionist_Patient, Patient_Doctor, Doctor_Dept, Patient_Rooms, Patient_Bill, Rooms_Staff},
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
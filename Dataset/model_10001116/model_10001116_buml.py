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
Receptionsit = Class(name="Receptionsit")
Deparment = Class(name="Deparment")
Bill = Class(name="Bill")
Rooms = Class(name="Rooms")
Staff = Class(name="Staff")

# Doctor class attributes and methods
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_DocId: Property = Property(name="DocId", type=IntegerType)
Doctor_Department: Property = Property(name="Department", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor_PhNo: Property = Property(name="PhNo", type=IntegerType)
Doctor.attributes={Doctor_Department, Doctor_DocId, Doctor_Specialization, Doctor_PhNo, Doctor_Name}

# Patient class attributes and methods
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_PatientId: Property = Property(name="PatientId", type=IntegerType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient.attributes={Patient_Name, Patient_PatientId, Patient_age}

# Receptionsit class attributes and methods
Receptionsit_Name: Property = Property(name="Name", type=StringType)
Receptionsit_Id: Property = Property(name="Id", type=IntegerType)
Receptionsit.attributes={Receptionsit_Id, Receptionsit_Name}

# Deparment class attributes and methods
Deparment_Name: Property = Property(name="Name", type=StringType)
Deparment_Id: Property = Property(name="Id", type=IntegerType)
Deparment_PhNo: Property = Property(name="PhNo", type=IntegerType)
Deparment.attributes={Deparment_PhNo, Deparment_Id, Deparment_Name}

# Bill class attributes and methods
Bill_BillNo: Property = Property(name="BillNo", type=StringType)
Bill_PatientName: Property = Property(name="PatientName", type=StringType)
Bill_Amount: Property = Property(name="Amount", type=StringType)
Bill.attributes={Bill_PatientName, Bill_BillNo, Bill_Amount}

# Rooms class attributes and methods
Rooms_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Rooms_WardNo: Property = Property(name="WardNo", type=StringType)
Rooms.attributes={Rooms_RoomNo, Rooms_WardNo}

# Staff class attributes and methods
Staff_Name: Property = Property(name="Name", type=StringType)
Staff_Id: Property = Property(name="Id", type=IntegerType)
Staff_Type: Property = Property(name="Type", type=StringType)
Staff.attributes={Staff_Name, Staff_Type, Staff_Id}

# Relationships
Patient_Receptionsit: BinaryAssociation = BinaryAssociation(
    name="Patient_Receptionsit",
    ends={
        Property(name="patient3", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="Give_Appointment2", type=Receptionsit, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="Pay_Bill4", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="patient5", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Receptionsit_Bill: BinaryAssociation = BinaryAssociation(
    name="Receptionsit_Bill",
    ends={
        Property(name="Generate_Bills6", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionsit7", type=Receptionsit, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Deparment: BinaryAssociation = BinaryAssociation(
    name="Doctor_Deparment",
    ends={
        Property(name="Belongs_To8", type=Deparment, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor9", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Rooms: BinaryAssociation = BinaryAssociation(
    name="Patient_Rooms",
    ends={
        Property(name="Alloted_To10", type=Rooms, multiplicity=Multiplicity(0, 1)),
        Property(name="patient11", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Staff: BinaryAssociation = BinaryAssociation(
    name="Patient_Staff",
    ends={
        Property(name="staff12", type=Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="Do_Cleaning13", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="Checks0", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_87548082_5ccd_449b_ab02_102e7e1d3499",
    types={Doctor, Patient, Receptionsit, Deparment, Bill, Rooms, Staff},
    associations={Patient_Receptionsit, Patient_Bill, Receptionsit_Bill, Doctor_Deparment, Patient_Rooms, Patient_Staff, Doctor_Patient},
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
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
Department = Class(name="Department")
Patient = Class(name="Patient")
Room = Class(name="Room")
Receptionist = Class(name="Receptionist")
Person = Class(name="Person", is_abstract=True)
Bill = Class(name="Bill")
Staff = Class(name="Staff")
Nurse = Class(name="Nurse")

# Doctor class attributes and methods
Doctor_docid: Property = Property(name="docid", type=IntegerType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_department: Property = Property(name="department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=IntegerType)
Doctor_address: Property = Property(name="address", type=StringType)
Doctor.attributes={Doctor_address, Doctor_phno, Doctor_department, Doctor_docid, Doctor_specialization, Doctor_name}

# Department class attributes and methods
Department_id: Property = Property(name="id", type=IntegerType)
Department_name: Property = Property(name="name", type=StringType)
Department_doctorid: Property = Property(name="doctorid", type=IntegerType)
Department.attributes={Department_name, Department_doctorid, Department_id}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_telno: Property = Property(name="telno", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient_roomno: Property = Property(name="roomno", type=IntegerType)
Patient.attributes={Patient_roomno, Patient_age, Patient_address, Patient_telno, Patient_id, Patient_name, Patient_sex}

# Room class attributes and methods
Room_roomno: Property = Property(name="roomno", type=IntegerType)
Room_location: Property = Property(name="location", type=StringType)
Room.attributes={Room_roomno, Room_location}

# Receptionist class attributes and methods
Receptionist_id: Property = Property(name="id", type=IntegerType)
Receptionist_attribute2: Property = Property(name="attribute2", type=StringType)
Receptionist.attributes={Receptionist_id, Receptionist_attribute2}

# Person class attributes and methods
Person_id: Property = Property(name="id", type=IntegerType)
Person_name: Property = Property(name="name", type=StringType)
Person_type: Property = Property(name="type", type=StringType)
Person.attributes={Person_name, Person_type, Person_id}

# Bill class attributes and methods
Bill_billno: Property = Property(name="billno", type=StringType)
Bill_patientname: Property = Property(name="patientname", type=StringType)
Bill_amount: Property = Property(name="amount", type=FloatType)
Bill.attributes={Bill_amount, Bill_patientname, Bill_billno}

# Staff class attributes and methods

# Nurse class attributes and methods

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patients0", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctors1", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Doctor_Department: BinaryAssociation = BinaryAssociation(
    name="Doctor_Department",
    ends={
        Property(name="depmt2", type=Department, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor3", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Room: BinaryAssociation = BinaryAssociation(
    name="Patient_Room",
    ends={
        Property(name="room4", type=Room, multiplicity=Multiplicity(1, 1)),
        Property(name="patient5", type=Patient, multiplicity=Multiplicity(1, 9999))
    }
)
Room_Staff: BinaryAssociation = BinaryAssociation(
    name="Room_Staff",
    ends={
        Property(name="staff6", type=Staff, multiplicity=Multiplicity(0, 9999)),
        Property(name="room7", type=Room, multiplicity=Multiplicity(0, 9999))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="bill8", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="pat9", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
receptions: BinaryAssociation = BinaryAssociation(
    name="receptions",
    ends={
        Property(name="receptionist10", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="p11", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
manages: BinaryAssociation = BinaryAssociation(
    name="manages",
    ends={
        Property(name="sbill12", type=Bill, multiplicity=Multiplicity(0, 9999)),
        Property(name="receptionist13", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b202a006_e9dc_4cd5_af2c_ea250c57c63e",
    types={Doctor, Department, Patient, Room, Receptionist, Person, Bill, Staff, Nurse},
    associations={Doctor_Patient, Doctor_Department, Patient_Room, Room_Staff, Patient_Bill, receptions, manages},
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
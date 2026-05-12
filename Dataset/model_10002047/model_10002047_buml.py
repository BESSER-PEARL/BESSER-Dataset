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
Nurse = Class(name="Nurse")
Patient = Class(name="Patient")
Room = Class(name="Room")
Staff = Class(name="Staff")
Person = Class(name="Person", is_abstract=True)
Hospital = Class(name="Hospital")
Bill = Class(name="Bill")
Staff1 = Class(name="Staff1")
Nurse1 = Class(name="Nurse1")
Department = Class(name="Department")
Operations_staff = Class(name="Operations_staff")
Administrative_staff = Class(name="Administrative_staff")
Technical_staff = Class(name="Technical_staff")

# Doctor class attributes and methods
Doctor_docid: Property = Property(name="docid", type=IntegerType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_department: Property = Property(name="department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=IntegerType)
Doctor_address: Property = Property(name="address", type=StringType)
Doctor.attributes={Doctor_docid, Doctor_address, Doctor_department, Doctor_specialization, Doctor_phno, Doctor_name}

# Nurse class attributes and methods
Nurse_id: Property = Property(name="id", type=IntegerType)
Nurse_name: Property = Property(name="name", type=StringType)
Nurse_doctorid: Property = Property(name="doctorid", type=IntegerType)
Nurse.attributes={Nurse_name, Nurse_id, Nurse_doctorid}

# Patient class attributes and methods
Patient_accepted: Property = Property(name="accepted", type=DateType)
Patient_sickness: Property = Property(name="sickness", type=StringType)
Patient_telno: Property = Property(name="telno", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient_roomno: Property = Property(name="roomno", type=IntegerType)
Patient.attributes={Patient_age, Patient_sex, Patient_sickness, Patient_telno, Patient_roomno, Patient_accepted, Patient_address}

# Room class attributes and methods
Room_roomno: Property = Property(name="roomno", type=IntegerType)
Room_location: Property = Property(name="location", type=StringType)
Room.attributes={Room_location, Room_roomno}

# Staff class attributes and methods
Staff_joined: Property = Property(name="joined", type=DateType)
Staff_education: Property = Property(name="education", type=StringType)
Staff.attributes={Staff_education, Staff_joined}

# Person class attributes and methods
Person_Name: Property = Property(name="Name", type=StringType)
Person_Title: Property = Property(name="Title", type=StringType)
Person_Gender: Property = Property(name="Gender", type=StringType)
Person_birthDate: Property = Property(name="birthDate", type=DateType)
Person_address: Property = Property(name="address", type=StringType)
Person_phone: Property = Property(name="phone", type=IntegerType)
Person.attributes={Person_Title, Person_phone, Person_address, Person_Name, Person_birthDate, Person_Gender}

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_address: Property = Property(name="address", type=StringType)
Hospital_phone: Property = Property(name="phone", type=IntegerType)
Hospital.attributes={Hospital_name, Hospital_phone, Hospital_address}

# Bill class attributes and methods
Bill_billno: Property = Property(name="billno", type=StringType)
Bill_patientname: Property = Property(name="patientname", type=StringType)
Bill_amount: Property = Property(name="amount", type=FloatType)
Bill.attributes={Bill_billno, Bill_amount, Bill_patientname}

# Staff1 class attributes and methods

# Nurse1 class attributes and methods

# Department class attributes and methods

# Operations_staff class attributes and methods

# Administrative_staff class attributes and methods

# Technical_staff class attributes and methods

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
        Property(name="depmt2", type=Nurse, multiplicity=Multiplicity(1, 1)),
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
        Property(name="staff6", type=Staff1, multiplicity=Multiplicity(0, 9999)),
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
        Property(name="receptionist10", type=Staff, multiplicity=Multiplicity(1, 1)),
        Property(name="p11", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
manages: BinaryAssociation = BinaryAssociation(
    name="manages",
    ends={
        Property(name="sbill12", type=Bill, multiplicity=Multiplicity(0, 9999)),
        Property(name="receptionist13", type=Staff, multiplicity=Multiplicity(1, 1))
    }
)
Person_Hospital: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital",
    ends={
        Property(name="person14", type=Person, multiplicity=Multiplicity(0, 1)),
        Property(name="hospital15", type=Hospital, multiplicity=Multiplicity(0, 1))
    }
)
Person_Hospital2: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital2",
    ends={
        Property(name="person16", type=Person, multiplicity=Multiplicity(0, 9999)),
        Property(name="Person_Hospital2_117", type=Hospital, multiplicity=Multiplicity(0, 9999))
    }
)
Hospital_Department: BinaryAssociation = BinaryAssociation(
    name="Hospital_Department",
    ends={
        Property(name="hospital18", type=Hospital, multiplicity=Multiplicity(1, 1)),
        Property(name="department19", type=Department, multiplicity=Multiplicity(0, 9999))
    }
)
Department_Staff: BinaryAssociation = BinaryAssociation(
    name="Department_Staff",
    ends={
        Property(name="department20", type=Department, multiplicity=Multiplicity(1, 1)),
        Property(name="staff21", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
Patient_Operations_staff: BinaryAssociation = BinaryAssociation(
    name="Patient_Operations_staff",
    ends={
        Property(name="patient22", type=Patient, multiplicity=Multiplicity(0, 9999)),
        Property(name="operations_staff23", type=Operations_staff, multiplicity=Multiplicity(0, 9999))
    }
)
Person_Hospital3: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital3",
    ends={
        Property(name="person24", type=Person, multiplicity=Multiplicity(0, 9999)),
        Property(name="hospital25", type=Hospital, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lHBVMHQQEeqHBZyMlFJVZw",
    types={Doctor, Nurse, Patient, Room, Staff, Person, Hospital, Bill, Staff1, Nurse1, Department, Operations_staff, Administrative_staff, Technical_staff},
    associations={Doctor_Patient, Doctor_Department, Patient_Room, Room_Staff, Patient_Bill, receptions, manages, Person_Hospital, Person_Hospital2, Hospital_Department, Department_Staff, Patient_Operations_staff, Person_Hospital3},
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
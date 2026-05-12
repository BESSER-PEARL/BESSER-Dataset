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
Patient = Class(name="Patient")
Receptionist = Class(name="Receptionist")
Departmnt = Class(name="Departmnt")
Rooms = Class(name="Rooms")
Staff = Class(name="Staff")
Patient_Actor = Class(name="Patient_Actor")
Doctor_Actor = Class(name="Doctor_Actor")
Takes_Appt_UseCase = Class(name="Takes_Appt_UseCase")
Consult_the_doctor_UseCase = Class(name="Consult_the_doctor_UseCase")
Follow_doc_instrn_UseCase = Class(name="Follow_doc_instrn_UseCase")
pay_bills_UseCase = Class(name="pay_bills_UseCase")
Doctor = Class(name="Doctor")

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_Sex: Property = Property(name="Sex", type=StringType)
Patient_Name: Property = Property(name="Name", type=IntegerType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_TelNo: Property = Property(name="TelNo", type=IntegerType)
Patient_Rno: Property = Property(name="Rno", type=IntegerType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient.attributes={Patient_Address, Patient_TelNo, Patient_Rno, Patient_Sex, Patient_Name, Patient_id, Patient_Age}

# Receptionist class attributes and methods
Receptionist_id: Property = Property(name="id", type=IntegerType)
Receptionist_Name: Property = Property(name="Name", type=StringType)
Receptionist.attributes={Receptionist_Name, Receptionist_id}

# Departmnt class attributes and methods
Departmnt_id: Property = Property(name="id", type=IntegerType)
Departmnt_name: Property = Property(name="name", type=StringType)
Departmnt_docid: Property = Property(name="docid", type=IntegerType)
Departmnt.attributes={Departmnt_name, Departmnt_id, Departmnt_docid}

# Rooms class attributes and methods
Rooms_Roomno: Property = Property(name="Roomno", type=IntegerType)
Rooms_location: Property = Property(name="location", type=StringType)
Rooms.attributes={Rooms_location, Rooms_Roomno}

# Staff class attributes and methods
Staff_id: Property = Property(name="id", type=IntegerType)
Staff_Name: Property = Property(name="Name", type=StringType)
Staff_type: Property = Property(name="type", type=StringType)
Staff.attributes={Staff_Name, Staff_type, Staff_id}

# Patient_Actor class attributes and methods

# Doctor_Actor class attributes and methods

# Takes_Appt_UseCase class attributes and methods

# Consult_the_doctor_UseCase class attributes and methods

# Follow_doc_instrn_UseCase class attributes and methods

# pay_bills_UseCase class attributes and methods

# Doctor class attributes and methods
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_Department: Property = Property(name="Department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=StringType)
Doctor_Docid: Property = Property(name="Docid", type=IntegerType)
Doctor.attributes={Doctor_Department, Doctor_Docid, Doctor_phno, Doctor_Name, Doctor_specialization}

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
Doctor_Departmnt: BinaryAssociation = BinaryAssociation(
    name="Doctor_Departmnt",
    ends={
        Property(name="departmnt4", type=Departmnt, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor5", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Rooms_Staff: BinaryAssociation = BinaryAssociation(
    name="Rooms_Staff",
    ends={
        Property(name="staff6", type=Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="rooms7", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Rooms_Patient: BinaryAssociation = BinaryAssociation(
    name="Rooms_Patient",
    ends={
        Property(name="patient8", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="rooms9", type=Rooms, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6a08a8f0_b912_4989_9183_e22aa2ad28c8",
    types={Patient, Receptionist, Departmnt, Rooms, Staff, Patient_Actor, Doctor_Actor, Takes_Appt_UseCase, Consult_the_doctor_UseCase, Follow_doc_instrn_UseCase, pay_bills_UseCase, Doctor},
    associations={Doctor_Patient, Patient_Receptionist, Doctor_Departmnt, Rooms_Staff, Rooms_Patient},
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
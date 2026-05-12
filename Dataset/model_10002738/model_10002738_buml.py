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
Admin = Class(name="Admin")
Patient = Class(name="Patient")
Login_Component = Class(name="Login_Component")
Availability_Component = Class(name="Availability_Component")
DataBase_Component = Class(name="DataBase_Component")

# Doctor class attributes and methods
Doctor_docid: Property = Property(name="docid", type=IntegerType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_department: Property = Property(name="department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=IntegerType)
Doctor_address: Property = Property(name="address", type=StringType)
Doctor.attributes={Doctor_name, Doctor_department, Doctor_docid, Doctor_phno, Doctor_address, Doctor_specialization}

# Admin class attributes and methods
Admin_id: Property = Property(name="id", type=IntegerType)
Admin_name: Property = Property(name="name", type=StringType)
Admin_doctorid: Property = Property(name="doctorid", type=IntegerType)
Admin.attributes={Admin_doctorid, Admin_name, Admin_id}

# Patient class attributes and methods
Patient_roomno: Property = Property(name="roomno", type=IntegerType)
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_telno: Property = Property(name="telno", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient.attributes={Patient_roomno, Patient_age, Patient_sex, Patient_name, Patient_address, Patient_telno, Patient_id}

# Login_Component class attributes and methods

# Availability_Component class attributes and methods

# DataBase_Component class attributes and methods

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
        Property(name="depmt2", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor3", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Department_Patient: BinaryAssociation = BinaryAssociation(
    name="Department_Patient",
    ends={
        Property(name="patient4", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="department5", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="d4bba546_0a94_4722_96ed_a8a8806fa9d5",
    types={Doctor, Admin, Patient, Login_Component, Availability_Component, DataBase_Component},
    associations={Doctor_Patient, Doctor_Department, Department_Patient},
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
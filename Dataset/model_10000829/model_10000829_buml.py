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

# Doctor class attributes and methods
Doctor_docid: Property = Property(name="docid", type=IntegerType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_department: Property = Property(name="department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=IntegerType)
Doctor_address: Property = Property(name="address", type=StringType)
Doctor.attributes={Doctor_specialization, Doctor_name, Doctor_phno, Doctor_department, Doctor_docid, Doctor_address}

# Admin class attributes and methods
Admin_User_Name: Property = Property(name="User_Name", type=Admin)
Admin_name: Property = Property(name="name", type=StringType)
Admin_Password: Property = Property(name="Password", type=StringType)
Admin.attributes={Admin_User_Name, Admin_name, Admin_Password}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_telno: Property = Property(name="telno", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient.attributes={Patient_name, Patient_address, Patient_sex, Patient_telno, Patient_age, Patient_id}

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

# Domain Model
domain_model = DomainModel(
    name="_65b5a010_4334_440f_88dc_5378029bf0af",
    types={Doctor, Admin, Patient},
    associations={Doctor_Patient, Doctor_Department},
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
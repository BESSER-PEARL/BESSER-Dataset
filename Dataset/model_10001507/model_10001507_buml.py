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
System_Admin = Class(name="System_Admin")
Patient = Class(name="Patient")
Nurse = Class(name="Nurse")

# Doctor class attributes and methods
Doctor_docid: Property = Property(name="docid", type=IntegerType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_department: Property = Property(name="department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=IntegerType)
Doctor_address: Property = Property(name="address", type=StringType)
Doctor.attributes={Doctor_department, Doctor_specialization, Doctor_name, Doctor_address, Doctor_phno, Doctor_docid}

# System_Admin class attributes and methods
System_Admin_id: Property = Property(name="id", type=IntegerType)
System_Admin_name: Property = Property(name="name", type=StringType)
System_Admin_adminid: Property = Property(name="adminid", type=IntegerType)
System_Admin.attributes={System_Admin_adminid, System_Admin_id, System_Admin_name}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_telno: Property = Property(name="telno", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient.attributes={Patient_telno, Patient_name, Patient_address, Patient_age, Patient_id, Patient_sex}

# Nurse class attributes and methods
Nurse_id: Property = Property(name="id", type=IntegerType)
Nurse_attribute2: Property = Property(name="attribute2", type=StringType)
Nurse.attributes={Nurse_attribute2, Nurse_id}

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
        Property(name="admin2", type=System_Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor3", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
receptions: BinaryAssociation = BinaryAssociation(
    name="receptions",
    ends={
        Property(name="Nurse4", type=Nurse, multiplicity=Multiplicity(1, 1)),
        Property(name="p5", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_BkUEwF3iEeqK2M3E1LfZ7Q",
    types={Doctor, System_Admin, Patient, Nurse},
    associations={Doctor_Patient, Doctor_Department, receptions},
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
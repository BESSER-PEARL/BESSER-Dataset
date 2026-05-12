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
Hospital_Management_System = Class(name="Hospital_Management_System")

# Doctor class attributes and methods
Doctor_DocID: Property = Property(name="DocID", type=IntegerType)
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_Department: Property = Property(name="Department", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor_Phone: Property = Property(name="Phone", type=IntegerType)
Doctor_Address: Property = Property(name="Address", type=StringType)
Doctor.attributes={Doctor_Name, Doctor_Department, Doctor_Phone, Doctor_DocID, Doctor_Specialization, Doctor_Address}

# Patient class attributes and methods
Patient_PatID: Property = Property(name="PatID", type=IntegerType)
Patient_Name: Property = Property(name="Name", type=StringType)
Patient_TelNo: Property = Property(name="TelNo", type=IntegerType)
Patient_Address: Property = Property(name="Address", type=StringType)
Patient_Age: Property = Property(name="Age", type=IntegerType)
Patient_Gender: Property = Property(name="Gender", type=StringType)
Patient_RoomNo: Property = Property(name="RoomNo", type=IntegerType)
Patient.attributes={Patient_PatID, Patient_RoomNo, Patient_Age, Patient_Address, Patient_Gender, Patient_TelNo, Patient_Name}

# Receptionist class attributes and methods
Receptionist_ID: Property = Property(name="ID", type=IntegerType)
Receptionist_Name: Property = Property(name="Name", type=StringType)
Receptionist.attributes={Receptionist_Name, Receptionist_ID}

# Hospital_Management_System class attributes and methods
Hospital_Management_System_Name: Property = Property(name="Name", type=StringType)
Hospital_Management_System_Address: Property = Property(name="Address", type=StringType)
Hospital_Management_System_Code: Property = Property(name="Code", type=StringType)
Hospital_Management_System.attributes={Hospital_Management_System_Name, Hospital_Management_System_Address, Hospital_Management_System_Code}

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient0", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor1", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Patient: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Patient",
    ends={
        Property(name="patient2", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist3", type=Receptionist, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Doctor: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Doctor",
    ends={
        Property(name="doctor4", type=Doctor, multiplicity=Multiplicity(1, 9999)),
        Property(name="receptionist5", type=Receptionist, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JXVvQKhREeeEQN1ZyOr__g",
    types={Doctor, Patient, Receptionist, Hospital_Management_System},
    associations={Doctor_Patient, Receptionist_Patient, Receptionist_Doctor},
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
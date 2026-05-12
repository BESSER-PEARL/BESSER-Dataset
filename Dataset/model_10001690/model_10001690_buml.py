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
Take_Appointment_external = Class(name="Take_Appointment_external")
Give_Prescription_external = Class(name="Give_Prescription_external")
Check_Patient_external = Class(name="Check_Patient_external")
Person = Class(name="Person")
Patient = Class(name="Patient")
prescription = Class(name="prescription")
Doctor = Class(name="Doctor")
Admin_Office_Component = Class(name="Admin_Office_Component")
Patient_Actor = Class(name="Patient_Actor")
Doctor_Actor = Class(name="Doctor_Actor")
Show_to_Doctor_external = Class(name="Show_to_Doctor_external")

# Take_Appointment_external class attributes and methods

# Give_Prescription_external class attributes and methods

# Check_Patient_external class attributes and methods

# Person class attributes and methods
Person_Name: Property = Property(name="Name", type=StringType)
Person_Phone_no: Property = Property(name="Phone_no", type=StringType)
Person_Name1: Property = Property(name="Name1", type=StringType)
Person_Id: Property = Property(name="Id", type=StringType)
Person_Gender: Property = Property(name="Gender", type=StringType)
Person_Birth_date: Property = Property(name="Birth_date", type=StringType)
Person_Age: Property = Property(name="Age", type=IntegerType)
Person.attributes={Person_Name1, Person_Name, Person_Birth_date, Person_Phone_no, Person_Gender, Person_Age, Person_Id}

# Patient class attributes and methods
Patient_Patient_id: Property = Property(name="Patient_id", type=IntegerType)
Patient_Admit_date: Property = Property(name="Admit_date", type=StringType)
Patient_Sickness: Property = Property(name="Sickness", type=StringType)
Patient.attributes={Patient_Admit_date, Patient_Patient_id, Patient_Sickness}

# prescription class attributes and methods

# Doctor class attributes and methods
Doctor_Doctor_id: Property = Property(name="Doctor_id", type=IntegerType)
Doctor_Dept: Property = Property(name="Dept", type=StringType)
Doctor_Specialization: Property = Property(name="Specialization", type=StringType)
Doctor.attributes={Doctor_Dept, Doctor_Doctor_id, Doctor_Specialization}

# Admin_Office_Component class attributes and methods

# Patient_Actor class attributes and methods

# Doctor_Actor class attributes and methods

# Show_to_Doctor_external class attributes and methods

# Relationships
Patient_Take_Appointment: BinaryAssociation = BinaryAssociation(
    name="Patient_Take_Appointment",
    ends={
        Property(name="take_Appointment2", type=Take_Appointment_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patient3", type=Patient_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Give_Prescription: BinaryAssociation = BinaryAssociation(
    name="Doctor_Give_Prescription",
    ends={
        Property(name="give_Prescription4", type=Give_Prescription_external, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor5", type=Doctor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Check_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Check_Patient",
    ends={
        Property(name="check_Patient6", type=Check_Patient_external, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor7", type=Doctor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Show_to_Doctor: BinaryAssociation = BinaryAssociation(
    name="Patient_Show_to_Doctor",
    ends={
        Property(name="show_to_Doctor0", type=Show_to_Doctor_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patient1", type=Patient_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_P5FbIAZuEeipbtix_oa2Dg",
    types={Take_Appointment_external, Give_Prescription_external, Check_Patient_external, Person, Patient, prescription, Doctor, Admin_Office_Component, Patient_Actor, Doctor_Actor, Show_to_Doctor_external},
    associations={Patient_Take_Appointment, Doctor_Give_Prescription, Doctor_Check_Patient, Patient_Show_to_Doctor},
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
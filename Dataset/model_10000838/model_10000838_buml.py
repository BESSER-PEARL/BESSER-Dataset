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
Receptionist_Actor = Class(name="Receptionist_Actor")
System_Component = Class(name="System_Component")
Check_for_Appointments_UseCase = Class(name="Check_for_Appointments_UseCase")
Handle_Medical_Reports_UseCase = Class(name="Handle_Medical_Reports_UseCase")
Patient_Actor = Class(name="Patient_Actor")
Doctor_Actor = Class(name="Doctor_Actor")
Accounts_Section_Actor = Class(name="Accounts_Section_Actor")
Class_ = Class(name="Class")
Patient_Information_external = Class(name="Patient_Information_external")
Schedule_Patient_Appointments_external = Class(name="Schedule_Patient_Appointments_external")
Bed_Allotment_external = Class(name="Bed_Allotment_external")
Generate_Bill_external = Class(name="Generate_Bill_external")
Draw_Salary_external = Class(name="Draw_Salary_external")
Patient_Hospital_Registration_external = Class(name="Patient_Hospital_Registration_external")

# Receptionist_Actor class attributes and methods

# System_Component class attributes and methods

# Check_for_Appointments_UseCase class attributes and methods

# Handle_Medical_Reports_UseCase class attributes and methods

# Patient_Actor class attributes and methods

# Doctor_Actor class attributes and methods

# Accounts_Section_Actor class attributes and methods

# Class class attributes and methods

# Patient_Information_external class attributes and methods

# Schedule_Patient_Appointments_external class attributes and methods

# Bed_Allotment_external class attributes and methods

# Generate_Bill_external class attributes and methods

# Draw_Salary_external class attributes and methods

# Patient_Hospital_Registration_external class attributes and methods

# Relationships
Receptionist_Generate_Bill: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Generate_Bill",
    ends={
        Property(name="generate_Bill26", type=Generate_Bill_external, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist27", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Draw_Salary: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Draw_Salary",
    ends={
        Property(name="draw_Salary28", type=Draw_Salary_external, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist29", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Information_Doctor: BinaryAssociation = BinaryAssociation(
    name="Patient_Information_Doctor",
    ends={
        Property(name="doctor0", type=Doctor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="patient_Information1", type=Patient_Information_external, multiplicity=Multiplicity(0, 1))
    }
)
Handle_Medical_Reports_Doctor: BinaryAssociation = BinaryAssociation(
    name="Handle_Medical_Reports_Doctor",
    ends={
        Property(name="doctor2", type=Doctor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="handle_Medical_Reports3", type=Handle_Medical_Reports_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Schedule_Patient_Appointments__Patient: BinaryAssociation = BinaryAssociation(
    name="Schedule_Patient_Appointments__Patient",
    ends={
        Property(name="patient4", type=Patient_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="schedule_Patient_Appointments5", type=Schedule_Patient_Appointments_external, multiplicity=Multiplicity(0, 1))
    }
)
Schedule_Patient_Appointments__Doctor: BinaryAssociation = BinaryAssociation(
    name="Schedule_Patient_Appointments__Doctor",
    ends={
        Property(name="doctor6", type=Doctor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="schedule_Patient_Appointments7", type=Schedule_Patient_Appointments_external, multiplicity=Multiplicity(0, 1))
    }
)
Bed_Allotment_Patient: BinaryAssociation = BinaryAssociation(
    name="Bed_Allotment_Patient",
    ends={
        Property(name="patient8", type=Patient_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="bed_Allotment9", type=Bed_Allotment_external, multiplicity=Multiplicity(0, 1))
    }
)
Generate_Bill_Patient: BinaryAssociation = BinaryAssociation(
    name="Generate_Bill_Patient",
    ends={
        Property(name="patient10", type=Patient_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generate_Bill11", type=Generate_Bill_external, multiplicity=Multiplicity(0, 1))
    }
)
Generate_Bill_Accounts_Section: BinaryAssociation = BinaryAssociation(
    name="Generate_Bill_Accounts_Section",
    ends={
        Property(name="accounts_Section12", type=Accounts_Section_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generate_Bill13", type=Generate_Bill_external, multiplicity=Multiplicity(0, 1))
    }
)
Draw_Salary_Accounts_Section: BinaryAssociation = BinaryAssociation(
    name="Draw_Salary_Accounts_Section",
    ends={
        Property(name="accounts_Section14", type=Accounts_Section_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="draw_Salary15", type=Draw_Salary_external, multiplicity=Multiplicity(0, 1))
    }
)
Check_for_Appointments_Patient: BinaryAssociation = BinaryAssociation(
    name="Check_for_Appointments_Patient",
    ends={
        Property(name="patient16", type=Patient_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_for_Appointments17", type=Check_for_Appointments_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Patient_Hospital_Registration: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Patient_Hospital_Registration",
    ends={
        Property(name="patient_Hospital_Registration18", type=Patient_Hospital_Registration_external, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist19", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Patient_Information: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Patient_Information",
    ends={
        Property(name="patient_Information20", type=Patient_Information_external, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist21", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Handle_Medical_Reports: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Handle_Medical_Reports",
    ends={
        Property(name="handle_Medical_Reports22", type=Handle_Medical_Reports_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist23", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Check_for_Appointments: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Check_for_Appointments",
    ends={
        Property(name="check_for_Appointments24", type=Check_for_Appointments_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist25", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6701637f_cfb8_4ccb_8e97_9fba45c30835",
    types={Receptionist_Actor, System_Component, Check_for_Appointments_UseCase, Handle_Medical_Reports_UseCase, Patient_Actor, Doctor_Actor, Accounts_Section_Actor, Class_, Patient_Information_external, Schedule_Patient_Appointments_external, Bed_Allotment_external, Generate_Bill_external, Draw_Salary_external, Patient_Hospital_Registration_external},
    associations={Receptionist_Generate_Bill, Receptionist_Draw_Salary, Patient_Information_Doctor, Handle_Medical_Reports_Doctor, Schedule_Patient_Appointments__Patient, Schedule_Patient_Appointments__Doctor, Bed_Allotment_Patient, Generate_Bill_Patient, Generate_Bill_Accounts_Section, Draw_Salary_Accounts_Section, Check_for_Appointments_Patient, Receptionist_Patient_Hospital_Registration, Receptionist_Patient_Information, Receptionist_Handle_Medical_Reports, Receptionist_Check_for_Appointments},
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
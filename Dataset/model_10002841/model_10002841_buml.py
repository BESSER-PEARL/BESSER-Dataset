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
Patient_Check_In_aNurse = Class(name="Patient_Check_In_aNurse")
Patient_Check_In__aReceptionist = Class(name="Patient_Check_In__aReceptionist")
Patient_Check_In_aDoctor = Class(name="Patient_Check_In_aDoctor")
Patient_Check_In_aPatient = Class(name="Patient_Check_In_aPatient")

# Patient_Check_In_aNurse class attributes and methods
Patient_Check_In_aNurse_ID: Property = Property(name="ID", type=IntegerType)
Patient_Check_In_aNurse_Name: Property = Property(name="Name", type=StringType)
Patient_Check_In_aNurse_Ranking: Property = Property(name="Ranking", type=StringType)
Patient_Check_In_aNurse.attributes={Patient_Check_In_aNurse_Ranking, Patient_Check_In_aNurse_ID, Patient_Check_In_aNurse_Name}

# Patient_Check_In__aReceptionist class attributes and methods
Patient_Check_In__aReceptionist_Employee_ID: Property = Property(name="Employee_ID", type=IntegerType)
Patient_Check_In__aReceptionist_Name: Property = Property(name="Name", type=StringType)
Patient_Check_In__aReceptionist.attributes={Patient_Check_In__aReceptionist_Name, Patient_Check_In__aReceptionist_Employee_ID}

# Patient_Check_In_aDoctor class attributes and methods
Patient_Check_In_aDoctor_ID: Property = Property(name="ID", type=IntegerType)
Patient_Check_In_aDoctor_Name: Property = Property(name="Name", type=StringType)
Patient_Check_In_aDoctor_Specialization: Property = Property(name="Specialization", type=StringType)
Patient_Check_In_aDoctor_Rank: Property = Property(name="Rank", type=StringType)
Patient_Check_In_aDoctor.attributes={Patient_Check_In_aDoctor_Rank, Patient_Check_In_aDoctor_Specialization, Patient_Check_In_aDoctor_Name, Patient_Check_In_aDoctor_ID}

# Patient_Check_In_aPatient class attributes and methods
Patient_Check_In_aPatient_Patient_s_Name: Property = Property(name="Patient_s_Name", type=StringType)
Patient_Check_In_aPatient_MRN_Number: Property = Property(name="MRN_Number", type=IntegerType)
Patient_Check_In_aPatient_Symptoms: Property = Property(name="Symptoms", type=StringType)
Patient_Check_In_aPatient_Phone_Number: Property = Property(name="Phone_Number", type=IntegerType)
Patient_Check_In_aPatient.attributes={Patient_Check_In_aPatient_MRN_Number, Patient_Check_In_aPatient_Phone_Number, Patient_Check_In_aPatient_Patient_s_Name, Patient_Check_In_aPatient_Symptoms}

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient0", type=Patient_Check_In_aPatient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor1", type=Patient_Check_In_aDoctor, multiplicity=Multiplicity(0, 1))
    }
)
Patients__Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patients__Receptionist",
    ends={
        Property(name="Receptionist2", type=Patient_Check_In__aReceptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="patients3", type=Patient_Check_In_aPatient, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e1cf4f61_dbfd_4aab_851e_733c624ef8a0",
    types={Patient_Check_In_aNurse, Patient_Check_In__aReceptionist, Patient_Check_In_aDoctor, Patient_Check_In_aPatient},
    associations={Doctor_Patient, Patients__Receptionist},
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
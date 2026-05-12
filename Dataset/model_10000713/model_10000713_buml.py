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
Person = Class(name="Person")
Diagnosis = Class(name="Diagnosis")
Signs = Class(name="Signs")
Medical_test = Class(name="Medical_test")
Instructions = Class(name="Instructions")
Symptoms = Class(name="Symptoms")
Medicine = Class(name="Medicine")
Patient = Class(name="Patient")

# Person class attributes and methods
Person_Name: Property = Property(name="Name", type=StringType)
Person_Email: Property = Property(name="Email", type=StringType)
Person_Password: Property = Property(name="Password", type=StringType)
Person_ID: Property = Property(name="ID", type=IntegerType)
Person_Ssn: Property = Property(name="Ssn", type=StringType)
Person_Image: Property = Property(name="Image", type=StringType)
Person_PhoneNumeber: Property = Property(name="PhoneNumeber", type=StringType)
Person_InsuranceNumber: Property = Property(name="InsuranceNumber", type=StringType)
Person_Gender: Property = Property(name="Gender", type=IntegerType)
Person_Last_Seen: Property = Property(name="Last_Seen", type=StringType)
Person_Balance: Property = Property(name="Balance", type=StringType)
Person_Lat: Property = Property(name="Lat", type=StringType)
Person_Long: Property = Property(name="Long", type=StringType)
Person.attributes={Person_Image, Person_PhoneNumeber, Person_Name, Person_Lat, Person_Balance, Person_Email, Person_Ssn, Person_Long, Person_ID, Person_InsuranceNumber, Person_Password, Person_Gender, Person_Last_Seen}

# Diagnosis class attributes and methods
Diagnosis_ID: Property = Property(name="ID", type=IntegerType)
Diagnosis_Patient_Id: Property = Property(name="Patient_Id", type=IntegerType)
Diagnosis_Doctor_Id: Property = Property(name="Doctor_Id", type=IntegerType)
Diagnosis_Date: Property = Property(name="Date", type=StringType)
Diagnosis_Condition: Property = Property(name="Condition", type=StringType)
Diagnosis_LIst_of_Diagnosis: Property = Property(name="LIst_of_Diagnosis", type=StringType)
Diagnosis_LIst_of_Medical_Test: Property = Property(name="LIst_of_Medical_Test", type=StringType)
Diagnosis_LIst_of_Instructions: Property = Property(name="LIst_of_Instructions", type=StringType)
Diagnosis_LIst_of_Symptoms: Property = Property(name="LIst_of_Symptoms", type=StringType)
Diagnosis_LIst_of_Medicine: Property = Property(name="LIst_of_Medicine", type=StringType)
Diagnosis.attributes={Diagnosis_LIst_of_Medicine, Diagnosis_LIst_of_Symptoms, Diagnosis_Doctor_Id, Diagnosis_LIst_of_Medical_Test, Diagnosis_Condition, Diagnosis_Date, Diagnosis_LIst_of_Instructions, Diagnosis_LIst_of_Diagnosis, Diagnosis_Patient_Id, Diagnosis_ID}

# Signs class attributes and methods
Signs_name: Property = Property(name="name", type=StringType)
Signs_ID: Property = Property(name="ID", type=IntegerType)
Signs.attributes={Signs_ID, Signs_name}

# Medical_test class attributes and methods
Medical_test_Date: Property = Property(name="Date", type=StringType)
Medical_test_ID: Property = Property(name="ID", type=IntegerType)
Medical_test_name: Property = Property(name="name", type=StringType)
Medical_test_Image: Property = Property(name="Image", type=StringType)
Medical_test_Lab: Property = Property(name="Lab", type=StringType)
Medical_test.attributes={Medical_test_name, Medical_test_ID, Medical_test_Date, Medical_test_Image, Medical_test_Lab}

# Instructions class attributes and methods
Instructions_name: Property = Property(name="name", type=StringType)
Instructions_ID: Property = Property(name="ID", type=IntegerType)
Instructions_descriptions: Property = Property(name="descriptions", type=StringType)
Instructions.attributes={Instructions_descriptions, Instructions_ID, Instructions_name}

# Symptoms class attributes and methods
Symptoms_name: Property = Property(name="name", type=StringType)
Symptoms_ID: Property = Property(name="ID", type=IntegerType)
Symptoms.attributes={Symptoms_ID, Symptoms_name}

# Medicine class attributes and methods
Medicine_ID: Property = Property(name="ID", type=IntegerType)
Medicine_name: Property = Property(name="name", type=StringType)
Medicine_Price: Property = Property(name="Price", type=StringType)
Medicine_ActiveIngredient: Property = Property(name="ActiveIngredient", type=StringType)
Medicine_Type: Property = Property(name="Type", type=StringType)
Medicine.attributes={Medicine_ActiveIngredient, Medicine_Type, Medicine_name, Medicine_ID, Medicine_Price}

# Patient class attributes and methods
Patient_weight: Property = Property(name="weight", type=FloatType)
Patient_Height: Property = Property(name="Height", type=FloatType)
Patient_Allergies: Property = Property(name="Allergies", type=StringType)
Patient_DiagnosisList: Property = Property(name="DiagnosisList", type=StringType)
Patient_Surgeries: Property = Property(name="Surgeries", type=StringType)
Patient_Medicine: Property = Property(name="Medicine", type=StringType)
Patient_MedicalTest: Property = Property(name="MedicalTest", type=StringType)
Patient.attributes={Patient_weight, Patient_MedicalTest, Patient_Surgeries, Patient_Medicine, Patient_Allergies, Patient_DiagnosisList, Patient_Height}

# Relationships
Diagnosis_Medicine: BinaryAssociation = BinaryAssociation(
    name="Diagnosis_Medicine",
    ends={
        Property(name="medicine0", type=Medicine, multiplicity=Multiplicity(0, 9999)),
        Property(name="diagnosis1", type=Diagnosis, multiplicity=Multiplicity(1, 1))
    }
)
Diagnosis_Symptoms: BinaryAssociation = BinaryAssociation(
    name="Diagnosis_Symptoms",
    ends={
        Property(name="symptoms2", type=Symptoms, multiplicity=Multiplicity(0, 9999)),
        Property(name="diagnosis3", type=Diagnosis, multiplicity=Multiplicity(1, 1))
    }
)
Diagnosis_Signs: BinaryAssociation = BinaryAssociation(
    name="Diagnosis_Signs",
    ends={
        Property(name="signs4", type=Signs, multiplicity=Multiplicity(0, 9999)),
        Property(name="diagnosis5", type=Diagnosis, multiplicity=Multiplicity(1, 1))
    }
)
Diagnosis_Instructions: BinaryAssociation = BinaryAssociation(
    name="Diagnosis_Instructions",
    ends={
        Property(name="instructions6", type=Instructions, multiplicity=Multiplicity(0, 9999)),
        Property(name="diagnosis7", type=Diagnosis, multiplicity=Multiplicity(1, 1))
    }
)
Diagnosis_Medical_test: BinaryAssociation = BinaryAssociation(
    name="Diagnosis_Medical_test",
    ends={
        Property(name="medical_test8", type=Medical_test, multiplicity=Multiplicity(0, 9999)),
        Property(name="diagnosis9", type=Diagnosis, multiplicity=Multiplicity(1, 1))
    }
)
Patient__Diagnosis: BinaryAssociation = BinaryAssociation(
    name="Patient__Diagnosis",
    ends={
        Property(name="diagnosis10", type=Diagnosis, multiplicity=Multiplicity(0, 9999)),
        Property(name="patient11", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_581f9358_bf71_4952_89d8_8d0c1cf059a4",
    types={Person, Diagnosis, Signs, Medical_test, Instructions, Symptoms, Medicine, Patient},
    associations={Diagnosis_Medicine, Diagnosis_Symptoms, Diagnosis_Signs, Diagnosis_Instructions, Diagnosis_Medical_test, Patient__Diagnosis},
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
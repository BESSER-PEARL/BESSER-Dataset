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
Decision_support_system_Input_heart_disease_symptoms_UseCase = Class(name="Decision_support_system_Input_heart_disease_symptoms_UseCase")
Decision_support_system_Generate_heart_disease_diagnosis_UseCase = Class(name="Decision_support_system_Generate_heart_disease_diagnosis_UseCase")
Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase = Class(name="Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase")
Patient_Actor = Class(name="Patient_Actor")
Medical_staff_Actor = Class(name="Medical_staff_Actor")
user = Class(name="user")
Input_Data = Class(name="Input_Data")
Model = Class(name="Model")
Treatment = Class(name="Treatment")
Patient = Class(name="Patient")
Doctor = Class(name="Doctor")

# Decision_support_system_Input_heart_disease_symptoms_UseCase class attributes and methods

# Decision_support_system_Generate_heart_disease_diagnosis_UseCase class attributes and methods

# Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase class attributes and methods

# Patient_Actor class attributes and methods

# Medical_staff_Actor class attributes and methods

# user class attributes and methods
user_name: Property = Property(name="name", type=StringType)
user_id: Property = Property(name="id", type=StringType)
user.attributes={user_id, user_name}

# Input_Data class attributes and methods
Input_Data_id: Property = Property(name="id", type=StringType)
Input_Data_Symptoms_list: Property = Property(name="Symptoms_list", type=StringType)
Input_Data.attributes={Input_Data_id, Input_Data_Symptoms_list}

# Model class attributes and methods

# Treatment class attributes and methods
Treatment_id: Property = Property(name="id", type=StringType)
Treatment_disease: Property = Property(name="disease", type=StringType)
Treatment.attributes={Treatment_disease, Treatment_id}

# Patient class attributes and methods
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_phone: Property = Property(name="phone", type=StringType)
Patient.attributes={Patient_phone, Patient_age, Patient_address}

# Doctor class attributes and methods
Doctor_qualification: Property = Property(name="qualification", type=StringType)
Doctor.attributes={Doctor_qualification}

# Relationships
Patient_Input_symptoms: BinaryAssociation = BinaryAssociation(
    name="Patient_Input_symptoms",
    ends={
        Property(name="input_symptoms0", type=Decision_support_system_Input_heart_disease_symptoms_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patient1", type=Patient_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medical_staff_Input_symptoms: BinaryAssociation = BinaryAssociation(
    name="Medical_staff_Input_symptoms",
    ends={
        Property(name="input_symptoms2", type=Decision_support_system_Input_heart_disease_symptoms_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_staff3", type=Medical_staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medical_staff_Generate_diagnosis: BinaryAssociation = BinaryAssociation(
    name="Medical_staff_Generate_diagnosis",
    ends={
        Property(name="generate_diagnosis4", type=Decision_support_system_Generate_heart_disease_diagnosis_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_staff5", type=Medical_staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medical_staff_Check_treatment_recommendation: BinaryAssociation = BinaryAssociation(
    name="Medical_staff_Check_treatment_recommendation",
    ends={
        Property(name="check_treatment_recommendation6", type=Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_staff7", type=Medical_staff_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_Input_Data: BinaryAssociation = BinaryAssociation(
    name="user_Input_Data",
    ends={
        Property(name="input_Data8", type=Input_Data, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=user, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Model: BinaryAssociation = BinaryAssociation(
    name="Doctor_Model",
    ends={
        Property(name="model10", type=Model, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor11", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Treatment: BinaryAssociation = BinaryAssociation(
    name="Doctor_Treatment",
    ends={
        Property(name="treatment12", type=Treatment, multiplicity=Multiplicity(0, 9999)),
        Property(name="doctor13", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_fCkkYMleEeiZ3fREAmKE6g",
    types={Decision_support_system_Input_heart_disease_symptoms_UseCase, Decision_support_system_Generate_heart_disease_diagnosis_UseCase, Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase, Patient_Actor, Medical_staff_Actor, user, Input_Data, Model, Treatment, Patient, Doctor},
    associations={Patient_Input_symptoms, Medical_staff_Input_symptoms, Medical_staff_Generate_diagnosis, Medical_staff_Check_treatment_recommendation, user_Input_Data, Doctor_Model, Doctor_Treatment},
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
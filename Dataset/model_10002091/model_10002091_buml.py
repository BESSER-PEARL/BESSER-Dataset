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
Class1 = Class(name="Class1")
doctor = Class(name="doctor")
Hospital = Class(name="Hospital")
ward = Class(name="ward")
consultant_doctor = Class(name="consultant_doctor")
junior_doctor = Class(name="junior_doctor")
team = Class(name="team")
patient = Class(name="patient")

# Class1 class attributes and methods

# doctor class attributes and methods
doctor_name: Property = Property(name="name", type=StringType)
doctor_grade: Property = Property(name="grade", type=StringType)
doctor_address: Property = Property(name="address", type=StringType)
doctor.attributes={doctor_name, doctor_address, doctor_grade}

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_totalwards: Property = Property(name="totalwards", type=IntegerType)
Hospital.attributes={Hospital_totalwards, Hospital_name}

# ward class attributes and methods
ward_ward_id: Property = Property(name="ward_id", type=IntegerType)
ward_no_of_patients: Property = Property(name="no_of_patients", type=StringType)
ward.attributes={ward_ward_id, ward_no_of_patients}

# consultant_doctor class attributes and methods

# junior_doctor class attributes and methods

# team class attributes and methods

# patient class attributes and methods

# Relationships
Hospital_ward: BinaryAssociation = BinaryAssociation(
    name="Hospital_ward",
    ends={
        Property(name="ward0", type=ward, multiplicity=Multiplicity(1, 9999)),
        Property(name="hospital1", type=Hospital, multiplicity=Multiplicity(1, 1))
    }
)
doctor_consultant_doctor: BinaryAssociation = BinaryAssociation(
    name="doctor_consultant_doctor",
    ends={
        Property(name="consultant_doctor2", type=consultant_doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor3", type=doctor, multiplicity=Multiplicity(0, 1))
    }
)
doctor_junior_doctor: BinaryAssociation = BinaryAssociation(
    name="doctor_junior_doctor",
    ends={
        Property(name="junior_doctor4", type=junior_doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor5", type=doctor, multiplicity=Multiplicity(0, 1))
    }
)
doctor_team: BinaryAssociation = BinaryAssociation(
    name="doctor_team",
    ends={
        Property(name="team6", type=team, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor7", type=doctor, multiplicity=Multiplicity(0, 1))
    }
)
patient_team: BinaryAssociation = BinaryAssociation(
    name="patient_team",
    ends={
        Property(name="team8", type=team, multiplicity=Multiplicity(1, 1)),
        Property(name="patient9", type=patient, multiplicity=Multiplicity(1, 1))
    }
)
consultant_doctor_patient: BinaryAssociation = BinaryAssociation(
    name="consultant_doctor_patient",
    ends={
        Property(name="patient10", type=patient, multiplicity=Multiplicity(1, 1)),
        Property(name="consultant_doctor11", type=consultant_doctor, multiplicity=Multiplicity(1, 1))
    }
)
patient_junior_doctor: BinaryAssociation = BinaryAssociation(
    name="patient_junior_doctor",
    ends={
        Property(name="junior_doctor12", type=junior_doctor, multiplicity=Multiplicity(1, 9999)),
        Property(name="patient13", type=patient, multiplicity=Multiplicity(1, 1))
    }
)
team_consultant_doctor: BinaryAssociation = BinaryAssociation(
    name="team_consultant_doctor",
    ends={
        Property(name="consultant_doctor14", type=consultant_doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="team15", type=team, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_no56YFYvEemzqJd_lyYV1Q",
    types={Class1, doctor, Hospital, ward, consultant_doctor, junior_doctor, team, patient},
    associations={Hospital_ward, doctor_consultant_doctor, doctor_junior_doctor, doctor_team, patient_team, consultant_doctor_patient, patient_junior_doctor, team_consultant_doctor},
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
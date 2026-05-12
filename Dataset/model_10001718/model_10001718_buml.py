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

# Enumerations
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            
    }
)

# Classes
Hospital = Class(name="Hospital")
Team = Class(name="Team")
Ward = Class(name="Ward")
Patient = Class(name="Patient")
Doctor = Class(name="Doctor")
ConsultantDoctor = Class(name="ConsultantDoctor")
JuniorDoctor = Class(name="JuniorDoctor")
Person = Class(name="Person")

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_address: Property = Property(name="address", type=StringType)
Hospital_phone: Property = Property(name="phone", type=StringType)
Hospital.attributes={Hospital_address, Hospital_phone, Hospital_name}

# Team class attributes and methods
Team_name: Property = Property(name="name", type=StringType)
Team.attributes={Team_name}

# Ward class attributes and methods
Ward_name: Property = Property(name="name", type=StringType)
Ward_capacity: Property = Property(name="capacity", type=IntegerType)
Ward.attributes={Ward_name, Ward_capacity}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_sickness: Property = Property(name="sickness", type=StringType)
Patient_prescriptions: Property = Property(name="prescriptions", type=StringType)
Patient_allergies: Property = Property(name="allergies", type=StringType)
Patient_specialReqs: Property = Property(name="specialReqs", type=StringType)
Patient.attributes={Patient_id, Patient_allergies, Patient_specialReqs, Patient_sickness, Patient_prescriptions}

# Doctor class attributes and methods
Doctor_specialty: Property = Property(name="specialty", type=StringType)
Doctor_locations: Property = Property(name="locations", type=StringType)
Doctor.attributes={Doctor_locations, Doctor_specialty}

# ConsultantDoctor class attributes and methods

# JuniorDoctor class attributes and methods

# Person class attributes and methods
Person_gender: Property = Property(name="gender", type=Gender)
Person_age: Property = Property(name="age", type=IntegerType)
Person_address: Property = Property(name="address", type=StringType)
Person_phone: Property = Property(name="phone", type=StringType)
Person.attributes={Person_age, Person_gender, Person_address, Person_phone}

# Relationships
Hospital_Ward: BinaryAssociation = BinaryAssociation(
    name="Hospital_Ward",
    ends={
        Property(name="ward0", type=Ward, multiplicity=Multiplicity(0, 9999)),
        Property(name="hospital1", type=Hospital, multiplicity=Multiplicity(1, 1))
    }
)
Hospital_Team: BinaryAssociation = BinaryAssociation(
    name="Hospital_Team",
    ends={
        Property(name="team2", type=Team, multiplicity=Multiplicity(1, 9999)),
        Property(name="hospital3", type=Hospital, multiplicity=Multiplicity(1, 1))
    }
)
Team_Doctor: BinaryAssociation = BinaryAssociation(
    name="Team_Doctor",
    ends={
        Property(name="doctor4", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="team5", type=Team, multiplicity=Multiplicity(0, 9999))
    }
)
Patient_Ward: BinaryAssociation = BinaryAssociation(
    name="Patient_Ward",
    ends={
        Property(name="ward6", type=Ward, multiplicity=Multiplicity(1, 1)),
        Property(name="patient7", type=Patient, multiplicity=Multiplicity(0, 9999))
    }
)
ConsultantDoctor_Team: BinaryAssociation = BinaryAssociation(
    name="ConsultantDoctor_Team",
    ends={
        Property(name="team8", type=Team, multiplicity=Multiplicity(0, 1)),
        Property(name="consultantDoctor9", type=ConsultantDoctor, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patient10", type=Patient, multiplicity=Multiplicity(0, 9999)),
        Property(name="doctor11", type=Doctor, multiplicity=Multiplicity(0, 9999))
    }
)
ConsultantDoctor_Patient: BinaryAssociation = BinaryAssociation(
    name="ConsultantDoctor_Patient",
    ends={
        Property(name="patient12", type=Patient, multiplicity=Multiplicity(0, 9999)),
        Property(name="consultantDoctor13", type=ConsultantDoctor, multiplicity=Multiplicity(1, 1))
    }
)
ConsultantDoctor_JuniorDoctor: BinaryAssociation = BinaryAssociation(
    name="ConsultantDoctor_JuniorDoctor",
    ends={
        Property(name="juniorDoctor14", type=JuniorDoctor, multiplicity=Multiplicity(0, 9999)),
        Property(name="consultantDoctor15", type=ConsultantDoctor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_QV6ykP0iEeeyruBoe7_QtQ",
    types={Hospital, Team, Ward, Patient, Doctor, ConsultantDoctor, JuniorDoctor, Person, Gender},
    associations={Hospital_Ward, Hospital_Team, Team_Doctor, Patient_Ward, ConsultantDoctor_Team, Doctor_Patient, ConsultantDoctor_Patient, ConsultantDoctor_JuniorDoctor},
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
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
Admin_Actor = Class(name="Admin_Actor")
Class_ = Class(name="Class")
Dashboard_UseCase = Class(name="Dashboard_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
Add_Subject_UseCase = Class(name="Add_Subject_UseCase")
Enroll_Student_UseCase = Class(name="Enroll_Student_UseCase")
Enroll_Teacher_UseCase = Class(name="Enroll_Teacher_UseCase")
Add_Department_UseCase = Class(name="Add_Department_UseCase")
Add_Class_UseCase = Class(name="Add_Class_UseCase")
_UseCase = Class(name="_UseCase")
UseCase2_UseCase = Class(name="UseCase2_UseCase")
UseCase3_UseCase = Class(name="UseCase3_UseCase")
UseCase4_UseCase = Class(name="UseCase4_UseCase")
UseCase5_UseCase = Class(name="UseCase5_UseCase")
UseCase6_UseCase = Class(name="UseCase6_UseCase")
UseCase7_UseCase = Class(name="UseCase7_UseCase")
UseCase8_UseCase = Class(name="UseCase8_UseCase")
Kind_of_Adjectives_UseCase = Class(name="Kind_of_Adjectives_UseCase")
Possessive_Adjectives__UseCase = Class(name="Possessive_Adjectives__UseCase")
Demonstrative_Adjectives__UseCase = Class(name="Demonstrative_Adjectives__UseCase")
Numbers_Adjectives__UseCase = Class(name="Numbers_Adjectives__UseCase")
Interrogative_Adjectives__UseCase = Class(name="Interrogative_Adjectives__UseCase")
Indefinite_Adjectives__UseCase = Class(name="Indefinite_Adjectives__UseCase")
Attributive_Adjectives__UseCase = Class(name="Attributive_Adjectives__UseCase")

# Admin_Actor class attributes and methods

# Class class attributes and methods

# Dashboard_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# Add_Subject_UseCase class attributes and methods

# Enroll_Student_UseCase class attributes and methods

# Enroll_Teacher_UseCase class attributes and methods

# Add_Department_UseCase class attributes and methods

# Add_Class_UseCase class attributes and methods

# _UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# UseCase3_UseCase class attributes and methods

# UseCase4_UseCase class attributes and methods

# UseCase5_UseCase class attributes and methods

# UseCase6_UseCase class attributes and methods

# UseCase7_UseCase class attributes and methods

# UseCase8_UseCase class attributes and methods

# Kind_of_Adjectives_UseCase class attributes and methods

# Possessive_Adjectives__UseCase class attributes and methods

# Demonstrative_Adjectives__UseCase class attributes and methods

# Numbers_Adjectives__UseCase class attributes and methods

# Interrogative_Adjectives__UseCase class attributes and methods

# Indefinite_Adjectives__UseCase class attributes and methods

# Attributive_Adjectives__UseCase class attributes and methods

# Relationships
Admin_Enroll_Student: BinaryAssociation = BinaryAssociation(
    name="Admin_Enroll_Student",
    ends={
        Property(name="enroll_Student0", type=Enroll_Student_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Enroll_Teacher: BinaryAssociation = BinaryAssociation(
    name="Admin_Enroll_Teacher",
    ends={
        Property(name="enroll_Teacher2", type=Enroll_Teacher_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin3", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Add_Department: BinaryAssociation = BinaryAssociation(
    name="Admin_Add_Department",
    ends={
        Property(name="add_Department4", type=Add_Department_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin5", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Add_Class: BinaryAssociation = BinaryAssociation(
    name="Admin_Add_Class",
    ends={
        Property(name="add_Class6", type=Add_Class_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="zunair7", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase5: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase5",
    ends={
        Property(name="useCase58", type=UseCase5_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin9", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase6: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase6",
    ends={
        Property(name="useCase610", type=UseCase6_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin11", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
association: BinaryAssociation = BinaryAssociation(
    name="association",
    ends={
        Property(name="association_012", type=_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase2",
    ends={
        Property(name="useCase214", type=UseCase2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase3: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase3",
    ends={
        Property(name="useCase316", type=UseCase3_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase4: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase4",
    ends={
        Property(name="useCase418", type=UseCase4_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin19", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase7: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase7",
    ends={
        Property(name="useCase720", type=UseCase7_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin21", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase8: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase8",
    ends={
        Property(name="useCase822", type=UseCase8_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin23", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Indefinite_Adjectives__Kind_of_Adjectives: BinaryAssociation = BinaryAssociation(
    name="Indefinite_Adjectives__Kind_of_Adjectives",
    ends={
        Property(name="kind_of_Adjectives24", type=Kind_of_Adjectives_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="indefinite_Adjectives_25", type=Indefinite_Adjectives__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Attributive_Adjectives__Kind_of_Adjectives: BinaryAssociation = BinaryAssociation(
    name="Attributive_Adjectives__Kind_of_Adjectives",
    ends={
        Property(name="kind_of_Adjectives26", type=Kind_of_Adjectives_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="attributive_Adjectives_27", type=Attributive_Adjectives__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Demonstrative_Adjectives__Kind_of_Adjectives: BinaryAssociation = BinaryAssociation(
    name="Demonstrative_Adjectives__Kind_of_Adjectives",
    ends={
        Property(name="kind_of_Adjectives28", type=Kind_of_Adjectives_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="demonstrative_Adjectives_29", type=Demonstrative_Adjectives__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Numbers_Adjectives__Kind_of_Adjectives: BinaryAssociation = BinaryAssociation(
    name="Numbers_Adjectives__Kind_of_Adjectives",
    ends={
        Property(name="kind_of_Adjectives30", type=Kind_of_Adjectives_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="numbers_Adjectives_31", type=Numbers_Adjectives__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Interrogative_Adjectives__Kind_of_Adjectives: BinaryAssociation = BinaryAssociation(
    name="Interrogative_Adjectives__Kind_of_Adjectives",
    ends={
        Property(name="kind_of_Adjectives32", type=Kind_of_Adjectives_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="interrogative_Adjectives_33", type=Interrogative_Adjectives__UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Possessive_Adjectives__Kind_of_Adjectives: BinaryAssociation = BinaryAssociation(
    name="Possessive_Adjectives__Kind_of_Adjectives",
    ends={
        Property(name="kind_of_Adjectives34", type=Kind_of_Adjectives_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="possessive_Adjectives_35", type=Possessive_Adjectives__UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9c65767e_d6b9_42a8_bc7e_af2b7ef67e0e",
    types={Admin_Actor, Class_, Dashboard_UseCase, UseCase_UseCase, Add_Subject_UseCase, Enroll_Student_UseCase, Enroll_Teacher_UseCase, Add_Department_UseCase, Add_Class_UseCase, _UseCase, UseCase2_UseCase, UseCase3_UseCase, UseCase4_UseCase, UseCase5_UseCase, UseCase6_UseCase, UseCase7_UseCase, UseCase8_UseCase, Kind_of_Adjectives_UseCase, Possessive_Adjectives__UseCase, Demonstrative_Adjectives__UseCase, Numbers_Adjectives__UseCase, Interrogative_Adjectives__UseCase, Indefinite_Adjectives__UseCase, Attributive_Adjectives__UseCase},
    associations={Admin_Enroll_Student, Admin_Enroll_Teacher, Admin_Add_Department, Admin_Add_Class, Admin_UseCase5, Admin_UseCase6, association, Admin_UseCase2, Admin_UseCase3, Admin_UseCase4, Admin_UseCase7, Admin_UseCase8, Indefinite_Adjectives__Kind_of_Adjectives, Attributive_Adjectives__Kind_of_Adjectives, Demonstrative_Adjectives__Kind_of_Adjectives, Numbers_Adjectives__Kind_of_Adjectives, Interrogative_Adjectives__Kind_of_Adjectives, Possessive_Adjectives__Kind_of_Adjectives},
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
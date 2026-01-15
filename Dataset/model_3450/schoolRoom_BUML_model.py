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
School_School = Class(name="School::School")
School_SchoolRoom = Class(name="School::SchoolRoom")
School_Clock = Class(name="School::Clock")
School_Buzzer = Class(name="School::Buzzer")

# School_School class attributes and methods

# School_SchoolRoom class attributes and methods

# School_Clock class attributes and methods

# School_Buzzer class attributes and methods

# Relationships
room0: BinaryAssociation = BinaryAssociation(
    name="room0",
    ends={
        Property(name="School_SchoolRoom", type=School_School, multiplicity=Multiplicity(1, 1)),
        Property(name="School_School", type=School_SchoolRoom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clock1: BinaryAssociation = BinaryAssociation(
    name="clock1",
    ends={
        Property(name="School_Clock", type=School_School, multiplicity=Multiplicity(1, 1)),
        Property(name="School_School2", type=School_Clock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
buzzer3: BinaryAssociation = BinaryAssociation(
    name="buzzer3",
    ends={
        Property(name="School_Buzzer", type=School_SchoolRoom, multiplicity=Multiplicity(1, 1)),
        Property(name="School_SchoolRoom4", type=School_Buzzer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ring5: BinaryAssociation = BinaryAssociation(
    name="ring5",
    ends={
        Property(name="Clock", type=School_Buzzer, multiplicity=Multiplicity(1, 1)),
        Property(name="alarm", type=School_Clock, multiplicity=Multiplicity(1, 1))
    }
)
alarm6: BinaryAssociation = BinaryAssociation(
    name="alarm6",
    ends={
        Property(name="Buzzer", type=School_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="ring", type=School_Buzzer, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="School",
    types={School_School, School_SchoolRoom, School_Clock, School_Buzzer},
    associations={room0, clock1, buzzer3, ring5, alarm6},
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
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
example_Player = Class(name="example::Player")
example_MP3 = Class(name="example::MP3")

# example_Player class attributes and methods

# example_MP3 class attributes and methods

# Relationships
mp3s0: BinaryAssociation = BinaryAssociation(
    name="mp3s0",
    ends={
        Property(name="MP3", type=example_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="player", type=example_MP3, multiplicity=Multiplicity(0, 9999))
    }
)
player1: BinaryAssociation = BinaryAssociation(
    name="player1",
    ends={
        Property(name="Player", type=example_MP3, multiplicity=Multiplicity(1, 1)),
        Property(name="mp3s", type=example_Player, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example",
    types={example_Player, example_MP3},
    associations={mp3s0, player1},
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
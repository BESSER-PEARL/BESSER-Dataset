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
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="example_MP3", type=example_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="example_Player", type=example_MP3, multiplicity=Multiplicity(0, 9999))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="example_MP33", type=example_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="example_Player2", type=example_MP3, multiplicity=Multiplicity(0, 1))
    }
)
b4: BinaryAssociation = BinaryAssociation(
    name="b4",
    ends={
        Property(name="example_Player6", type=example_MP3, multiplicity=Multiplicity(1, 1)),
        Property(name="example_MP35", type=example_Player, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example",
    types={example_Player, example_MP3},
    associations={a0, c1, b4},
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
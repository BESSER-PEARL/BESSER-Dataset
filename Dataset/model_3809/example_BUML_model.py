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
example_Codec = Class(name="example::Codec")
example_Player = Class(name="example::Player")

# example_Codec class attributes and methods

# example_Player class attributes and methods
example_Player_compression1: Property = Property(name="compression1", type=StringType)
example_Player.attributes={example_Player_compression1}

# Relationships
compression20: BinaryAssociation = BinaryAssociation(
    name="compression20",
    ends={
        Property(name="example_Codec", type=example_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="example_Player", type=example_Codec, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example",
    types={example_Codec, example_Player},
    associations={compression20},
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
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
Basic_C = Class(name="Basic::C")

# Basic_C class attributes and methods
Basic_C_a: Property = Property(name="a", type=IntegerType)
Basic_C_b: Property = Property(name="b", type=IntegerType)
Basic_C.attributes={Basic_C_b, Basic_C_a}

# Domain Model
domain_model = DomainModel(
    name="Basic",
    types={Basic_C},
    associations={},
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
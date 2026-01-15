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
Basic2_C = Class(name="Basic2::C")

# Basic2_C class attributes and methods
Basic2_C_a: Property = Property(name="a", type=IntegerType)
Basic2_C_b: Property = Property(name="b", type=IntegerType)
Basic2_C_c: Property = Property(name="c", type=IntegerType)
Basic2_C.attributes={Basic2_C_a, Basic2_C_b, Basic2_C_c}

# Domain Model
domain_model = DomainModel(
    name="Basic2",
    types={Basic2_C},
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
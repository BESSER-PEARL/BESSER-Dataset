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
Basic4_C = Class(name="Basic4::C")

# Basic4_C class attributes and methods
Basic4_C_a: Property = Property(name="a", type=BooleanType)
Basic4_C_b: Property = Property(name="b", type=BooleanType)
Basic4_C_c: Property = Property(name="c", type=BooleanType)
Basic4_C_d: Property = Property(name="d", type=BooleanType)
Basic4_C.attributes={Basic4_C_b, Basic4_C_d, Basic4_C_c, Basic4_C_a}

# Domain Model
domain_model = DomainModel(
    name="Basic4",
    types={Basic4_C},
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
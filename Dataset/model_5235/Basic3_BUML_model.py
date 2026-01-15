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
Basic3_C = Class(name="Basic3::C")

# Basic3_C class attributes and methods
Basic3_C_a: Property = Property(name="a", type=BooleanType)
Basic3_C_b: Property = Property(name="b", type=BooleanType)
Basic3_C_c: Property = Property(name="c", type=BooleanType)
Basic3_C_d: Property = Property(name="d", type=BooleanType)
Basic3_C.attributes={Basic3_C_b, Basic3_C_a, Basic3_C_c, Basic3_C_d}

# Domain Model
domain_model = DomainModel(
    name="Basic3",
    types={Basic3_C},
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
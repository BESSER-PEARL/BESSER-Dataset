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
in_x_X = Class(name="in::x::X")
in_A = Class(name="in::A")
B = Class(name="B")
C = Class(name="C")
in_B = Class(name="in::B")
in_C = Class(name="in::C")

# in_x_X class attributes and methods

# in_A class attributes and methods

# B class attributes and methods

# C class attributes and methods

# in_B class attributes and methods

# in_C class attributes and methods

# Generalizations
gen_in_A_B = Generalization(general=B, specific=in_A)
gen_in_A_C = Generalization(general=C, specific=in_A)

# Domain Model
domain_model = DomainModel(
    name="in",
    types={in_x_X, in_A, B, C, in_B, in_C},
    associations={},
    generalizations={gen_in_A_B, gen_in_A_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
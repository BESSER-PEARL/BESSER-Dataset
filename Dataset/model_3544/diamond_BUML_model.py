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
diamond_A = Class(name="diamond::A")
diamond_B = Class(name="diamond::B")
A = Class(name="A")
diamond_C = Class(name="diamond::C")
diamond_D = Class(name="diamond::D")
B = Class(name="B")
C = Class(name="C")

# diamond_A class attributes and methods

# diamond_B class attributes and methods

# A class attributes and methods

# diamond_C class attributes and methods

# diamond_D class attributes and methods

# B class attributes and methods

# C class attributes and methods

# Generalizations
gen_diamond_B_A = Generalization(general=A, specific=diamond_B)
gen_diamond_C_A = Generalization(general=A, specific=diamond_C)
gen_diamond_D_B = Generalization(general=B, specific=diamond_D)
gen_diamond_D_C = Generalization(general=C, specific=diamond_D)

# Domain Model
domain_model = DomainModel(
    name="diamond",
    types={diamond_A, diamond_B, A, diamond_C, diamond_D, B, C},
    associations={},
    generalizations={gen_diamond_B_A, gen_diamond_C_A, gen_diamond_D_B, gen_diamond_D_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
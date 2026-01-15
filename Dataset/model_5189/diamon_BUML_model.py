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
diamon_A = Class(name="diamon::A")
diamon_B = Class(name="diamon::B")
A = Class(name="A")
diamon_C = Class(name="diamon::C")
diamon_D = Class(name="diamon::D")
B = Class(name="B")
C = Class(name="C")

# diamon_A class attributes and methods

# diamon_B class attributes and methods

# A class attributes and methods

# diamon_C class attributes and methods

# diamon_D class attributes and methods

# B class attributes and methods

# C class attributes and methods

# Generalizations
gen_diamon_B_A = Generalization(general=A, specific=diamon_B)
gen_diamon_C_A = Generalization(general=A, specific=diamon_C)
gen_diamon_D_B = Generalization(general=B, specific=diamon_D)
gen_diamon_D_C = Generalization(general=C, specific=diamon_D)

# Domain Model
domain_model = DomainModel(
    name="diamon",
    types={diamon_A, diamon_B, A, diamon_C, diamon_D, B, C},
    associations={},
    generalizations={gen_diamon_B_A, gen_diamon_C_A, gen_diamon_D_B, gen_diamon_D_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
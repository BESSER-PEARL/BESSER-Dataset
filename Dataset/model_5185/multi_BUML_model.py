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
multi_A = Class(name="multi::A")
multi_B = Class(name="multi::B")
multi_C = Class(name="multi::C")
A = Class(name="A")
B = Class(name="B")

# multi_A class attributes and methods

# multi_B class attributes and methods

# multi_C class attributes and methods

# A class attributes and methods

# B class attributes and methods

# Generalizations
gen_multi_C_A = Generalization(general=A, specific=multi_C)
gen_multi_C_B = Generalization(general=B, specific=multi_C)

# Domain Model
domain_model = DomainModel(
    name="multi",
    types={multi_A, multi_B, multi_C, A, B},
    associations={},
    generalizations={gen_multi_C_A, gen_multi_C_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
p_A = Class(name="p::A")
B = Class(name="B")
p_B = Class(name="p::B")

# p_A class attributes and methods

# B class attributes and methods

# p_B class attributes and methods

# Generalizations
gen_p_A_B = Generalization(general=B, specific=p_A)

# Domain Model
domain_model = DomainModel(
    name="p",
    types={p_A, B, p_B},
    associations={},
    generalizations={gen_p_A_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
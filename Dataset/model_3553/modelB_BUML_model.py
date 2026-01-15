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
modelB_A = Class(name="modelB::A")
A = Class(name="A")
B = Class(name="B")

# modelB_A class attributes and methods

# A class attributes and methods

# B class attributes and methods

# Generalizations
gen_modelB_A_A = Generalization(general=A, specific=modelB_A)
gen_modelB_A_B = Generalization(general=B, specific=modelB_A)

# Domain Model
domain_model = DomainModel(
    name="modelB",
    types={modelB_A, A, B},
    associations={},
    generalizations={gen_modelB_A_A, gen_modelB_A_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
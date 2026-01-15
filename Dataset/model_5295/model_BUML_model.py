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
model_A = Class(name="model::A", is_abstract=True)
model_B = Class(name="model::B")
A = Class(name="A")

# model_A class attributes and methods

# model_B class attributes and methods

# A class attributes and methods

# Generalizations
gen_model_B_A = Generalization(general=A, specific=model_B)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_A, model_B, A},
    associations={},
    generalizations={gen_model_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
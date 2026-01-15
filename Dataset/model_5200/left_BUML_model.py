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
model_A = Class(name="model::A")
model_B = Class(name="model::B")
model_C = Class(name="model::C")
model_D = Class(name="model::D")

# model_A class attributes and methods

# model_B class attributes and methods

# model_C class attributes and methods

# model_D class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_A, model_B, model_C, model_D},
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
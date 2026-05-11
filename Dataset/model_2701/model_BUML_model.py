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
model_Model = Class(name="model_Model")
model_A = Class(name="model_A")
model_B = Class(name="model_B")
model_C = Class(name="model_C")

# model_Model class attributes and methods

# model_A class attributes and methods

# model_B class attributes and methods

# model_C class attributes and methods

# Relationships
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="model_A", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model", type=model_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="model_B", type=model_A, multiplicity=Multiplicity(1, 1)),
        Property(name="model_A2", type=model_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="model_C", type=model_B, multiplicity=Multiplicity(1, 1)),
        Property(name="model_B4", type=model_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Model, model_A, model_B, model_C},
    associations={a0, b1, c3},
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
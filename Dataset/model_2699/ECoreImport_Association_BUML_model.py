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

# model_A class attributes and methods

# model_B class attributes and methods

# model_C class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="B", type=model_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=model_B, multiplicity=Multiplicity(1, 9999))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="model_C", type=model_B, multiplicity=Multiplicity(1, 1)),
        Property(name="model_B", type=model_C, multiplicity=Multiplicity(0, 9999))
    }
)
a2: BinaryAssociation = BinaryAssociation(
    name="a2",
    ends={
        Property(name="A", type=model_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=model_A, multiplicity=Multiplicity(1, 5))
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_A, model_B, model_C},
    associations={b0, c1, a2},
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
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
x_A = Class(name="x::A")
x_C = Class(name="x::C")
x_B = Class(name="x::B")

# x_A class attributes and methods

# x_C class attributes and methods

# x_B class attributes and methods

# Relationships
c0: BinaryAssociation = BinaryAssociation(
    name="c0",
    ends={
        Property(name="x_C", type=x_A, multiplicity=Multiplicity(1, 1)),
        Property(name="x_A", type=x_C, multiplicity=Multiplicity(0, 1))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="x_C2", type=x_B, multiplicity=Multiplicity(1, 1)),
        Property(name="x_B", type=x_C, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="x",
    types={x_A, x_C, x_B},
    associations={c0, c1},
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
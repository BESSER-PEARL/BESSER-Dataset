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
b_B = Class(name="b::B")
b_A = Class(name="b::A")
b_C = Class(name="b::C")

# b_B class attributes and methods

# b_A class attributes and methods

# b_C class attributes and methods

# Relationships
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="b_A", type=b_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b_B", type=b_A, multiplicity=Multiplicity(0, 1))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="b_C", type=b_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b_B2", type=b_C, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b",
    types={b_B, b_A, b_C},
    associations={a0, c1},
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
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
input_A = Class(name="input::A")

# input_A class attributes and methods

# Relationships
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="input_A", type=input_A, multiplicity=Multiplicity(1, 1)),
        Property(name="input_A0", type=input_A, multiplicity=Multiplicity(0, 1))
    }
)
b3: BinaryAssociation = BinaryAssociation(
    name="b3",
    ends={
        Property(name="input_A4", type=input_A, multiplicity=Multiplicity(1, 1)),
        Property(name="input_A2", type=input_A, multiplicity=Multiplicity(0, 1))
    }
)
c6: BinaryAssociation = BinaryAssociation(
    name="c6",
    ends={
        Property(name="input_A7", type=input_A, multiplicity=Multiplicity(1, 1)),
        Property(name="input_A5", type=input_A, multiplicity=Multiplicity(0, 1))
    }
)
d9: BinaryAssociation = BinaryAssociation(
    name="d9",
    ends={
        Property(name="input_A10", type=input_A, multiplicity=Multiplicity(1, 1)),
        Property(name="input_A8", type=input_A, multiplicity=Multiplicity(0, 1))
    }
)
e12: BinaryAssociation = BinaryAssociation(
    name="e12",
    ends={
        Property(name="input_A13", type=input_A, multiplicity=Multiplicity(1, 1)),
        Property(name="input_A11", type=input_A, multiplicity=Multiplicity(0, 1))
    }
)
f15: BinaryAssociation = BinaryAssociation(
    name="f15",
    ends={
        Property(name="input_A16", type=input_A, multiplicity=Multiplicity(1, 1)),
        Property(name="input_A14", type=input_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="input",
    types={input_A},
    associations={a1, b3, c6, d9, e12, f15},
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
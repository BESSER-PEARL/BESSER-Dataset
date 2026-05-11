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
reference_A = Class(name="reference_A")
reference_B = Class(name="reference_B")
reference_X = Class(name="reference_X")
reference_Y = Class(name="reference_Y")
reference_C = Class(name="reference_C")

# reference_A class attributes and methods

# reference_B class attributes and methods

# reference_X class attributes and methods

# reference_Y class attributes and methods

# reference_C class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="reference_B", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_A", type=reference_B, multiplicity=Multiplicity(0, 1))
    }
)
x1: BinaryAssociation = BinaryAssociation(
    name="x1",
    ends={
        Property(name="X", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=reference_X, multiplicity=Multiplicity(0, 1))
    }
)
y2: BinaryAssociation = BinaryAssociation(
    name="y2",
    ends={
        Property(name="Y", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a3", type=reference_Y, multiplicity=Multiplicity(0, 1))
    }
)
c4: BinaryAssociation = BinaryAssociation(
    name="c4",
    ends={
        Property(name="reference_C", type=reference_B, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_B5", type=reference_C, multiplicity=Multiplicity(0, 1))
    }
)
a6: BinaryAssociation = BinaryAssociation(
    name="a6",
    ends={
        Property(name="A", type=reference_X, multiplicity=Multiplicity(1, 1)),
        Property(name="x", type=reference_A, multiplicity=Multiplicity(0, 1))
    }
)
a7: BinaryAssociation = BinaryAssociation(
    name="a7",
    ends={
        Property(name="A8", type=reference_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="y", type=reference_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="reference",
    types={reference_A, reference_B, reference_X, reference_Y, reference_C},
    associations={b0, x1, y2, c4, a6, a7},
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
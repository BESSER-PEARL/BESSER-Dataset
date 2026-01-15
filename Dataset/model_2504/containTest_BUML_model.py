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
A_B = Class(name="A::B")
A_A = Class(name="A::A")
A_C = Class(name="A::C")
A_D = Class(name="A::D")
A_E = Class(name="A::E")

# A_B class attributes and methods

# A_A class attributes and methods

# A_C class attributes and methods

# A_D class attributes and methods

# A_E class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="A_B", type=A_A, multiplicity=Multiplicity(1, 1)),
        Property(name="A_A", type=A_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="A_C", type=A_B, multiplicity=Multiplicity(1, 1)),
        Property(name="A_B2", type=A_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d3: BinaryAssociation = BinaryAssociation(
    name="d3",
    ends={
        Property(name="A_D", type=A_B, multiplicity=Multiplicity(1, 1)),
        Property(name="A_B4", type=A_D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b6: BinaryAssociation = BinaryAssociation(
    name="b6",
    ends={
        Property(name="A_B7", type=A_B, multiplicity=Multiplicity(1, 1)),
        Property(name="A_B5", type=A_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e8: BinaryAssociation = BinaryAssociation(
    name="e8",
    ends={
        Property(name="A_E", type=A_C, multiplicity=Multiplicity(1, 1)),
        Property(name="A_C9", type=A_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="A",
    types={A_B, A_A, A_C, A_D, A_E},
    associations={b0, c1, d3, b6, e8},
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
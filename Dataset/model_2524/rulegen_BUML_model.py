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
rulegen_Context = Class(name="rulegen::Context")
rulegen_A = Class(name="rulegen::A")
rulegen_B = Class(name="rulegen::B")
rulegen_C = Class(name="rulegen::C")
rulegen_D = Class(name="rulegen::D")

# rulegen_Context class attributes and methods

# rulegen_A class attributes and methods

# rulegen_B class attributes and methods

# rulegen_C class attributes and methods

# rulegen_D class attributes and methods

# Relationships
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="rulegen_A", type=rulegen_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="rulegen_Context", type=rulegen_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="rulegen_B", type=rulegen_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="rulegen_Context2", type=rulegen_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="rulegen_C", type=rulegen_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="rulegen_Context4", type=rulegen_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
d5: BinaryAssociation = BinaryAssociation(
    name="d5",
    ends={
        Property(name="rulegen_D", type=rulegen_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="rulegen_Context6", type=rulegen_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeAB7: BinaryAssociation = BinaryAssociation(
    name="edgeAB7",
    ends={
        Property(name="B", type=rulegen_A, multiplicity=Multiplicity(1, 1)),
        Property(name="edgeBA", type=rulegen_B, multiplicity=Multiplicity(0, 9999))
    }
)
edgeBA8: BinaryAssociation = BinaryAssociation(
    name="edgeBA8",
    ends={
        Property(name="A", type=rulegen_B, multiplicity=Multiplicity(1, 1)),
        Property(name="edgeAB", type=rulegen_A, multiplicity=Multiplicity(0, 9999))
    }
)
edgeBC9: BinaryAssociation = BinaryAssociation(
    name="edgeBC9",
    ends={
        Property(name="C", type=rulegen_B, multiplicity=Multiplicity(1, 1)),
        Property(name="edgeCB", type=rulegen_C, multiplicity=Multiplicity(0, 9999))
    }
)
edgeCB10: BinaryAssociation = BinaryAssociation(
    name="edgeCB10",
    ends={
        Property(name="B11", type=rulegen_C, multiplicity=Multiplicity(1, 1)),
        Property(name="edgeBC", type=rulegen_B, multiplicity=Multiplicity(0, 9999))
    }
)
edgeDC12: BinaryAssociation = BinaryAssociation(
    name="edgeDC12",
    ends={
        Property(name="rulegen_C14", type=rulegen_D, multiplicity=Multiplicity(1, 1)),
        Property(name="rulegen_D13", type=rulegen_C, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="rulegen",
    types={rulegen_Context, rulegen_A, rulegen_B, rulegen_C, rulegen_D},
    associations={a0, b1, c3, d5, edgeAB7, edgeBA8, edgeBC9, edgeCB10, edgeDC12},
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
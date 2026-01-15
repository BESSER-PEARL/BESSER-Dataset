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
test_A = Class(name="test::A")
test_B = Class(name="test::B")
test_C = Class(name="test::C")
test_E = Class(name="test::E")
test_I = Class(name="test::I")
test_D = Class(name="test::D")
test_G = Class(name="test::G")
test_F = Class(name="test::F")
test_H = Class(name="test::H")

# test_A class attributes and methods

# test_B class attributes and methods

# test_C class attributes and methods

# test_E class attributes and methods

# test_I class attributes and methods

# test_D class attributes and methods

# test_G class attributes and methods

# test_F class attributes and methods

# test_H class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="test_B", type=test_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test_A", type=test_B, multiplicity=Multiplicity(0, 1))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="test_C", type=test_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test_A2", type=test_C, multiplicity=Multiplicity(0, 1))
    }
)
e3: BinaryAssociation = BinaryAssociation(
    name="e3",
    ends={
        Property(name="test_E", type=test_B, multiplicity=Multiplicity(1, 1)),
        Property(name="test_B4", type=test_E, multiplicity=Multiplicity(0, 1))
    }
)
i5: BinaryAssociation = BinaryAssociation(
    name="i5",
    ends={
        Property(name="test_I", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test_C6", type=test_I, multiplicity=Multiplicity(0, 1))
    }
)
d11: BinaryAssociation = BinaryAssociation(
    name="d11",
    ends={
        Property(name="D", type=test_E, multiplicity=Multiplicity(1, 1)),
        Property(name="e", type=test_D, multiplicity=Multiplicity(0, 1))
    }
)
g12: BinaryAssociation = BinaryAssociation(
    name="g12",
    ends={
        Property(name="test_G", type=test_I, multiplicity=Multiplicity(1, 1)),
        Property(name="test_I13", type=test_G, multiplicity=Multiplicity(0, 1))
    }
)
f7: BinaryAssociation = BinaryAssociation(
    name="f7",
    ends={
        Property(name="test_F", type=test_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_D", type=test_F, multiplicity=Multiplicity(0, 1))
    }
)
h8: BinaryAssociation = BinaryAssociation(
    name="h8",
    ends={
        Property(name="test_H", type=test_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test_D9", type=test_H, multiplicity=Multiplicity(0, 1))
    }
)
e10: BinaryAssociation = BinaryAssociation(
    name="e10",
    ends={
        Property(name="E", type=test_D, multiplicity=Multiplicity(1, 1)),
        Property(name="d", type=test_E, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_A, test_B, test_C, test_E, test_I, test_D, test_G, test_F, test_H},
    associations={b0, c1, e3, i5, d11, g12, f7, h8, e10},
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
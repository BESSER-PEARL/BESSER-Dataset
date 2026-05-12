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
R = Class(name="R")
A = Class(name="A")
B = Class(name="B")
Y = Class(name="Y")
z = Class(name="z")
c = Class(name="c")
c2 = Class(name="c2")
c3 = Class(name="c3")
MyClass9 = Class(name="MyClass9")

# R class attributes and methods

# A class attributes and methods

# B class attributes and methods

# Y class attributes and methods

# z class attributes and methods

# c class attributes and methods

# c2 class attributes and methods

# c3 class attributes and methods

# MyClass9 class attributes and methods

# Relationships
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a0", type=A, multiplicity=Multiplicity(0, 1)),
        Property(name="r1", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(8, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_c: BinaryAssociation = BinaryAssociation(
    name="B_c",
    ends={
        Property(name="c4", type=c, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=B, multiplicity=Multiplicity(0, 1))
    }
)
c2_z: BinaryAssociation = BinaryAssociation(
    name="c2_z",
    ends={
        Property(name="z6", type=z, multiplicity=Multiplicity(0, 1)),
        Property(name="c27", type=c2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_PCuPsLsTEeedTfUoC_GfaA",
    types={R, A, B, Y, z, c, c2, c3, MyClass9},
    associations={R_A, A_B, B_c, c2_z},
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
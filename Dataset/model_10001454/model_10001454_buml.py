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
A = Class(name="A")
B = Class(name="B")
C = Class(name="C", is_abstract=True)
C2 = Class(name="C2")
Z = Class(name="Z")
Y = Class(name="Y")
C3 = Class(name="C3")
R = Class(name="R")

# A class attributes and methods
A_a: Property = Property(name="a", type=StringType)
A.attributes={A_a}

# B class attributes and methods
B_b: Property = Property(name="b", type=IntegerType)
B.attributes={B_b}

# C class attributes and methods
C_c: Property = Property(name="c", type=IntegerType)
C_d: Property = Property(name="d", type=BooleanType)
C.attributes={C_c, C_d}

# C2 class attributes and methods

# Z class attributes and methods

# Y class attributes and methods
Y_Y: Property = Property(name="Y", type=StringType)
Y.attributes={Y_Y}

# C3 class attributes and methods

# R class attributes and methods

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a4", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7hovYPeoEeiqn80yrzdh8w",
    types={A, B, C, C2, Z, Y, C3, R},
    associations={B_C, A_B, R_A},
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
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
C3 = Class(name="C3")
Class_ = Class(name="Class")
A1 = Class(name="A1")
A2 = Class(name="A2")
A3 = Class(name="A3")
B1 = Class(name="B1")
B2 = Class(name="B2")
A = Class(name="A")
B = Class(name="B")
C = Class(name="C")
R = Class(name="R")
Z = Class(name="Z")
Y = Class(name="Y")
C2 = Class(name="C2")

# C3 class attributes and methods

# Class class attributes and methods

# A1 class attributes and methods
A1_b: Property = Property(name="b", type=BooleanType)
A1_d: Property = Property(name="d", type=IntegerType)
A1.attributes={A1_b, A1_d}

# A2 class attributes and methods

# A3 class attributes and methods

# B1 class attributes and methods

# B2 class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC2, C_attC1}

# R class attributes and methods

# Z class attributes and methods

# Y class attributes and methods

# C2 class attributes and methods

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 1)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR2", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r3", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b4", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="c6", type=B1, multiplicity=Multiplicity(1, 1)),
        Property(name="a7", type=A1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_OJPskMUwEeeWu_SLkciAbg",
    types={C3, Class_, A1, A2, A3, B1, B2, A, B, C, R, Z, Y, C2},
    associations={B_C, R_A, A_B, A_B2},
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
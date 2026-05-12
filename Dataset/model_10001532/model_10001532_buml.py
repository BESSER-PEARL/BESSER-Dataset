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
y = Class(name="y")
A = Class(name="A")
Z = Class(name="Z")
B = Class(name="B")
C = Class(name="C")
C1 = Class(name="C1")
C2 = Class(name="C2")

# R class attributes and methods

# y class attributes and methods
y_attY: Property = Property(name="attY", type=StringType)
y.attributes={y_attY}

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Z class attributes and methods

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# C1 class attributes and methods

# C2 class attributes and methods

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
        Property(name="b2", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c4", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=B, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_E6T1wPJVEei0SKJPiR2ViA",
    types={R, y, A, Z, B, C, C1, C2},
    associations={R_A, A_B, B_C},
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
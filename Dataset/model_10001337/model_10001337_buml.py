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
A1 = Class(name="A1")
B1 = Class(name="B1")
C1 = Class(name="C1")
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
B = Class(name="B")
C = Class(name="C")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# B1 class attributes and methods
B1_attB: Property = Property(name="attB", type=IntegerType)
B1.attributes={B1_attB}

# C1 class attributes and methods
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1.attributes={C1_attC2, C1_attC1}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC2, C_attC1}

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
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b4", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR6", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r7", type=R, multiplicity=Multiplicity(0, 1))
    }
)
C_B: BinaryAssociation = BinaryAssociation(
    name="C_B",
    ends={
        Property(name="b8", type=B1, multiplicity=Multiplicity(0, 1)),
        Property(name="c9", type=C1, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0kZuAPbYEeiqn80yrzdh8w",
    types={A, A1, B1, C1, Y, R, Z, C2, C3, B, C},
    associations={B_C, A_B, A_B2, R_A, C_B},
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
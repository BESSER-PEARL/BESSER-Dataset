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
C = Class(name="C")
A2 = Class(name="A2")
B2 = Class(name="B2")
C2 = Class(name="C2")
A1 = Class(name="A1", is_abstract=True)
B1 = Class(name="B1")
C1 = Class(name="C1", is_abstract=True)
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
C21 = Class(name="C21")
C3 = Class(name="C3")

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

# A2 class attributes and methods
A2_attA: Property = Property(name="attA", type=StringType)
A2.attributes={A2_attA}

# B2 class attributes and methods
B2_attB: Property = Property(name="attB", type=IntegerType)
B2.attributes={B2_attB}

# C2 class attributes and methods
C2_attC1: Property = Property(name="attC1", type=IntegerType)
C2_attC2: Property = Property(name="attC2", type=BooleanType)
C2.attributes={C2_attC1, C2_attC2}

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# B1 class attributes and methods
B1_attB: Property = Property(name="attB", type=IntegerType)
B1.attributes={B1_attB}

# C1 class attributes and methods
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1.attributes={C1_attC1, C1_attC2}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Z class attributes and methods

# C21 class attributes and methods

# C3 class attributes and methods

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
C_B: BinaryAssociation = BinaryAssociation(
    name="C_B",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="c3", type=C, multiplicity=Multiplicity(0, 9999))
    }
)
C_B2: BinaryAssociation = BinaryAssociation(
    name="C_B2",
    ends={
        Property(name="b4", type=B2, multiplicity=Multiplicity(0, 1)),
        Property(name="c5", type=C2, multiplicity=Multiplicity(0, 9999))
    }
)
C_B3: BinaryAssociation = BinaryAssociation(
    name="C_B3",
    ends={
        Property(name="b6", type=B1, multiplicity=Multiplicity(0, 1)),
        Property(name="c7", type=C1, multiplicity=Multiplicity(0, 9999))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR8", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r9", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b10", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a11", type=A1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_AH4m4Om1EeiV94kHgjpOMg",
    types={A, B, C, A2, B2, C2, A1, B1, C1, Y, R, Z, C21, C3},
    associations={A_B, C_B, C_B2, C_B3, R_A, A_B2},
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
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
Y = Class(name="Y")
R = Class(name="R")
B = Class(name="B")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
C = Class(name="C")
A2 = Class(name="A2")
A3 = Class(name="A3")
A1 = Class(name="A1")
B1 = Class(name="B1")
B2 = Class(name="B2")
cxw = Class(name="cxw")
dz_aklm = Class(name="dz_aklm")
A4 = Class(name="A4")
A5 = Class(name="A5")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# A2 class attributes and methods

# A3 class attributes and methods

# A1 class attributes and methods
A1_b: Property = Property(name="b", type=BooleanType)
A1_d: Property = Property(name="d", type=IntegerType)
A1.attributes={A1_b, A1_d}

# B1 class attributes and methods

# B2 class attributes and methods

# cxw class attributes and methods

# dz_aklm class attributes and methods

# A4 class attributes and methods

# A5 class attributes and methods

# Relationships
C2_C: BinaryAssociation = BinaryAssociation(
    name="C2_C",
    ends={
        Property(name="c21", type=C2, multiplicity=Multiplicity(0, 1)),
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR4", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c6", type=C, multiplicity=Multiplicity(0, 1)),
        Property(name="b7", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="c8", type=B1, multiplicity=Multiplicity(0, 1)),
        Property(name="c9", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
A_A: BinaryAssociation = BinaryAssociation(
    name="A_A",
    ends={
        Property(name="a10", type=A1, multiplicity=Multiplicity(0, 1)),
        Property(name="a11", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
A3_A3: BinaryAssociation = BinaryAssociation(
    name="A3_A3",
    ends={
        Property(name="a312", type=A3, multiplicity=Multiplicity(0, 1)),
        Property(name="a313", type=A3, multiplicity=Multiplicity(0, 1))
    }
)
A3_A: BinaryAssociation = BinaryAssociation(
    name="A3_A",
    ends={
        Property(name="a14", type=A1, multiplicity=Multiplicity(0, 1)),
        Property(name="a315", type=A3, multiplicity=Multiplicity(0, 1))
    }
)
A3_A32: BinaryAssociation = BinaryAssociation(
    name="A3_A32",
    ends={
        Property(name="a316", type=A3, multiplicity=Multiplicity(0, 1)),
        Property(name="a317", type=A3, multiplicity=Multiplicity(0, 1))
    }
)
A3_A33: BinaryAssociation = BinaryAssociation(
    name="A3_A33",
    ends={
        Property(name="a318", type=A3, multiplicity=Multiplicity(0, 1)),
        Property(name="a319", type=A3, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EPZngAeqEeqFfO0RhT_ZfA",
    types={A, Y, R, B, Z, C2, C3, C, A2, A3, A1, B1, B2, cxw, dz_aklm, A4, A5},
    associations={C2_C, A_B2, R_A, B_C2, A_B, A_A, A3_A3, A3_A, A3_A32, A3_A33},
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
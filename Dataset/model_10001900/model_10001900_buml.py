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
Y = Class(name="Y")
B = Class(name="B")
Z = Class(name="Z")
R = Class(name="R")
C2 = Class(name="C2")
C3 = Class(name="C3")
A = Class(name="A")
Y2 = Class(name="Y2")
R2 = Class(name="R2")
A2 = Class(name="A2")
Z2 = Class(name="Z2")
B2 = Class(name="B2")
C4 = Class(name="C4")
C22 = Class(name="C22")
C32 = Class(name="C32")

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# Z class attributes and methods

# R class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Y2 class attributes and methods
Y2_attY: Property = Property(name="attY", type=StringType)
Y2.attributes={Y2_attY}

# R2 class attributes and methods

# A2 class attributes and methods
A2_attA: Property = Property(name="attA", type=StringType)
A2.attributes={A2_attA}

# Z2 class attributes and methods

# B2 class attributes and methods
B2_attB: Property = Property(name="attB", type=IntegerType)
B2.attributes={B2_attB}

# C4 class attributes and methods
C4_attC: Property = Property(name="attC", type=BooleanType)
C4_attC2: Property = Property(name="attC2", type=IntegerType)
C4.attributes={C4_attC2, C4_attC}

# C22 class attributes and methods

# C32 class attributes and methods

# Relationships
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a0", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r1", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
R_A2: BinaryAssociation = BinaryAssociation(
    name="R_A2",
    ends={
        Property(name="a4", type=A2, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R2, multiplicity=Multiplicity(0, 1))
    }
)
A_B22: BinaryAssociation = BinaryAssociation(
    name="A_B22",
    ends={
        Property(name="b6", type=B2, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=A2, multiplicity=Multiplicity(0, 1))
    }
)
B_C22: BinaryAssociation = BinaryAssociation(
    name="B_C22",
    ends={
        Property(name="c8", type=C4, multiplicity=Multiplicity(0, 9999)),
        Property(name="b9", type=B2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_cCnuEOmiEeiV94kHgjpOMg",
    types={Y, B, Z, R, C2, C3, A, Y2, R2, A2, Z2, B2, C4, C22, C32},
    associations={R_A, A_B2, R_A2, A_B22, B_C22},
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
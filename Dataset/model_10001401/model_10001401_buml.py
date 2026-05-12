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
C2 = Class(name="C2")
C3 = Class(name="C3")
C = Class(name="C", is_abstract=True)
Z = Class(name="Z")
A = Class(name="A", is_abstract=True)
B = Class(name="B")
R = Class(name="R")
Y = Class(name="Y")
C22 = Class(name="C22")
C32 = Class(name="C32")
C4 = Class(name="C4", is_abstract=True)
Z2 = Class(name="Z2")
A2 = Class(name="A2", is_abstract=True)
B2 = Class(name="B2")
R2 = Class(name="R2")
Y2 = Class(name="Y2")

# C2 class attributes and methods

# C3 class attributes and methods

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# Z class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# R class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# C22 class attributes and methods

# C32 class attributes and methods

# C4 class attributes and methods
C4_attC1: Property = Property(name="attC1", type=IntegerType)
C4_attC2: Property = Property(name="attC2", type=BooleanType)
C4.attributes={C4_attC1, C4_attC2}

# Z2 class attributes and methods

# A2 class attributes and methods
A2_attA: Property = Property(name="attA", type=StringType)
A2.attributes={A2_attA}

# B2 class attributes and methods
B2_attB: Property = Property(name="attB", type=IntegerType)
B2.attributes={B2_attB}

# R2 class attributes and methods

# Y2 class attributes and methods
Y2_attY: Property = Property(name="attY", type=StringType)
Y2.attributes={Y2_attY}

# Relationships
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
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 9999))
    }
)
B_C22: BinaryAssociation = BinaryAssociation(
    name="B_C22",
    ends={
        Property(name="c6", type=C4, multiplicity=Multiplicity(0, 9999)),
        Property(name="b7", type=B2, multiplicity=Multiplicity(0, 9999))
    }
)
A_B22: BinaryAssociation = BinaryAssociation(
    name="A_B22",
    ends={
        Property(name="b8", type=B2, multiplicity=Multiplicity(1, 9999)),
        Property(name="a9", type=A2, multiplicity=Multiplicity(0, 1))
    }
)
R_A2: BinaryAssociation = BinaryAssociation(
    name="R_A2",
    ends={
        Property(name="aR10", type=A2, multiplicity=Multiplicity(0, 9999)),
        Property(name="r11", type=R2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4VILsM7BEeeMV96X50GAvA",
    types={C2, C3, C, Z, A, B, R, Y, C22, C32, C4, Z2, A2, B2, R2, Y2},
    associations={A_B2, R_A, B_C2, B_C22, A_B22, R_A2},
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
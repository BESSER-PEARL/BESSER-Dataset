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
A = Class(name="A", is_abstract=True)
B = Class(name="B", is_abstract=True)
C = Class(name="C")
Z = Class(name="Z")
R = Class(name="R")
Y = Class(name="Y")
C2 = Class(name="C2")
C3 = Class(name="C3")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_AttC2: Property = Property(name="AttC2", type=BooleanType)
C.attributes={C_attC1, C_AttC2}

# Z class attributes and methods

# R class attributes and methods

# Y class attributes and methods
Y_atty: Property = Property(name="atty", type=StringType)
Y.attributes={Y_atty}

# C2 class attributes and methods

# C3 class attributes and methods

# Relationships
C3_C: BinaryAssociation = BinaryAssociation(
    name="C3_C",
    ends={
        Property(name="c4", type=C, multiplicity=Multiplicity(0, 1)),
        Property(name="c35", type=C3, multiplicity=Multiplicity(0, 1))
    }
)
C2_C: BinaryAssociation = BinaryAssociation(
    name="C2_C",
    ends={
        Property(name="c6", type=C, multiplicity=Multiplicity(0, 1)),
        Property(name="c27", type=C2, multiplicity=Multiplicity(0, 1))
    }
)
Z_A: BinaryAssociation = BinaryAssociation(
    name="Z_A",
    ends={
        Property(name="a8", type=A, multiplicity=Multiplicity(0, 1)),
        Property(name="z9", type=Z, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR10", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r11", type=R, multiplicity=Multiplicity(0, 1))
    }
)
Y_A: BinaryAssociation = BinaryAssociation(
    name="Y_A",
    ends={
        Property(name="a12", type=A, multiplicity=Multiplicity(0, 1)),
        Property(name="y13", type=Y, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_h85FwM6_EeeMV96X50GAvA",
    types={A, B, C, Z, R, Y, C2, C3},
    associations={C3_C, C2_C, Z_A, R_A, Y_A, A_B, B_C},
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
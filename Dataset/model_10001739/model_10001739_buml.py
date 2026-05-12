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
B = Class(name="B")
C = Class(name="C", is_abstract=True)
C2 = Class(name="C2")
C3 = Class(name="C3")
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
A1 = Class(name="A1")
B1 = Class(name="B1")
A2 = Class(name="A2")
A3 = Class(name="A3")
B2 = Class(name="B2")

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

# C2 class attributes and methods

# C3 class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Z class attributes and methods

# A1 class attributes and methods
A1_b: Property = Property(name="b", type=BooleanType)
A1_d: Property = Property(name="d", type=IntegerType)
A1.attributes={A1_d, A1_b}

# B1 class attributes and methods

# A2 class attributes and methods

# A3 class attributes and methods

# B2 class attributes and methods

# Relationships
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1)),
        Property(name="aR4", type=A, multiplicity=Multiplicity(0, 9999))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="c6", type=B1, multiplicity=Multiplicity(0, 1)),
        Property(name="a7", type=A1, multiplicity=Multiplicity(0, 9999))
    }
)
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

# Domain Model
domain_model = DomainModel(
    name="_SE1dMLsQEeedTfUoC_GfaA",
    types={A, B, C, C2, C3, Y, R, Z, A1, B1, A2, A3, B2},
    associations={R_A, A_B2, B_C, A_B},
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
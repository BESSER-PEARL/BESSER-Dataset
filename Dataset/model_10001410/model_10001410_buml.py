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
T = Class(name="T")
Z = Class(name="Z")
R = Class(name="R")
N = Class(name="N")
W = Class(name="W")
C2 = Class(name="C2")
C3 = Class(name="C3")
M = Class(name="M")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# T class attributes and methods
T_attY: Property = Property(name="attY", type=StringType)
T.attributes={T_attY}

# Z class attributes and methods

# R class attributes and methods

# N class attributes and methods
N_attB: Property = Property(name="attB", type=IntegerType)
N.attributes={N_attB}

# W class attributes and methods
W_attC1: Property = Property(name="attC1", type=IntegerType)
W_attC2: Property = Property(name="attC2", type=BooleanType)
W.attributes={W_attC2, W_attC1}

# C2 class attributes and methods

# C3 class attributes and methods

# M class attributes and methods
M_attA: Property = Property(name="attA", type=StringType)
M.attributes={M_attA}

# Relationships
c_Class7: BinaryAssociation = BinaryAssociation(
    name="c_Class7",
    ends={
        Property(name="aR8", type=M, multiplicity=Multiplicity(0, 1)),
        Property(name="c9", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=C, multiplicity=Multiplicity(0, 1)),
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
    }
)
Class7_Class3: BinaryAssociation = BinaryAssociation(
    name="Class7_Class3",
    ends={
        Property(name="b4", type=N, multiplicity=Multiplicity(0, 1)),
        Property(name="a5", type=M, multiplicity=Multiplicity(0, 1))
    }
)
Class3_Class4: BinaryAssociation = BinaryAssociation(
    name="Class3_Class4",
    ends={
        Property(name="class46", type=W, multiplicity=Multiplicity(0, 1)),
        Property(name="class37", type=N, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5IsCgBCfEeimSO_GhE8jew",
    types={A, B, C, T, Z, R, N, W, C2, C3, M},
    associations={c_Class7, A_B, B_C, Class7_Class3, Class3_Class4},
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
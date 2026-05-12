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
B = Class(name="B")
C = Class(name="C", is_abstract=True)
R = Class(name="R")
Y = Class(name="Y")
C1 = Class(name="C1")
C2 = Class(name="C2")
Z = Class(name="Z")
A = Class(name="A", is_abstract=True)

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC2, C_attC1}

# R class attributes and methods

# Y class attributes and methods

# C1 class attributes and methods

# C2 class attributes and methods

# Z class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
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

# Domain Model
domain_model = DomainModel(
    name="_W9_PMOmlEeiV94kHgjpOMg",
    types={B, C, R, Y, C1, C2, Z, A},
    associations={B_C, R_A, A_B},
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
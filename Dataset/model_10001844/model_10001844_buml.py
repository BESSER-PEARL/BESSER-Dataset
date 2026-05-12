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
A = Class(name="A", is_abstract=True)
Y = Class(name="Y")
Z = Class(name="Z")
B = Class(name="B")
C2 = Class(name="C2")
C = Class(name="C", is_abstract=True)
C3 = Class(name="C3")
B1 = Class(name="B1")
A3 = Class(name="A3")
B2 = Class(name="B2")
A1 = Class(name="A1")
A2 = Class(name="A2")

# R class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# Z class attributes and methods

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C2 class attributes and methods

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# C3 class attributes and methods

# B1 class attributes and methods

# A3 class attributes and methods

# B2 class attributes and methods

# A1 class attributes and methods
A1_b: Property = Property(name="b", type=BooleanType)
A1_c: Property = Property(name="c", type=B1)
A1_d: Property = Property(name="d", type=IntegerType)
A1.attributes={A1_b, A1_c, A1_d}

# A2 class attributes and methods

# Relationships
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a0", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r1", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c4", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A1_B1: BinaryAssociation = BinaryAssociation(
    name="A1_B1",
    ends={
        Property(name="b16", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a17", type=A1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ZuZlEMUgEeeWu_SLkciAbg",
    types={R, A, Y, Z, B, C2, C, C3, B1, A3, B2, A1, A2},
    associations={R_A, A_B, B_C, A1_B1},
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
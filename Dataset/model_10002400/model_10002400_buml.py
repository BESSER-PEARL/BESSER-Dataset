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
C = Class(name="C")
B = Class(name="B")
A1 = Class(name="A1", is_abstract=True)
B1 = Class(name="B1")
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
C1 = Class(name="C1", is_abstract=True)
C2 = Class(name="C2")
C21 = Class(name="C21")
A = Class(name="A")

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attrC2: Property = Property(name="attrC2", type=BooleanType)
C.attributes={C_attC1, C_attrC2}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=StringType)
B.attributes={B_attB}

# A1 class attributes and methods
A1_attrA: Property = Property(name="attrA", type=StringType)
A1.attributes={A1_attrA}

# B1 class attributes and methods
B1_attrB: Property = Property(name="attrB", type=IntegerType)
B1.attributes={B1_attrB}

# Y class attributes and methods
Y_attry: Property = Property(name="attry", type=StringType)
Y.attributes={Y_attry}

# R class attributes and methods

# Z class attributes and methods

# C1 class attributes and methods
C1_attrC1: Property = Property(name="attrC1", type=IntegerType)
C1_attrC2: Property = Property(name="attrC2", type=BooleanType)
C1.attributes={C1_attrC2, C1_attrC1}

# C2 class attributes and methods

# C21 class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Relationships
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
        Property(name="b3", type=B, multiplicity=Multiplicity(1, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR4", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b6", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c8", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="B_C2_19", type=B1, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="af4b2ebc_4ed5_4b7c_b82e_0d7a913781e1",
    types={C, B, A1, B1, Y, R, Z, C1, C2, C21, A},
    associations={A_B, B_C, R_A, A_B2, B_C2},
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
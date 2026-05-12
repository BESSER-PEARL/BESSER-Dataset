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
A1 = Class(name="A1", is_abstract=True)
B1 = Class(name="B1")
C1 = Class(name="C1", is_abstract=True)
R = Class(name="R")
Z = Class(name="Z")
Y = Class(name="Y")
C2 = Class(name="C2")
C3 = Class(name="C3")
A2 = Class(name="A2", is_abstract=True)
B2 = Class(name="B2")
C4 = Class(name="C4", is_abstract=True)
R2 = Class(name="R2")
Z2 = Class(name="Z2")
Y2 = Class(name="Y2")
C22 = Class(name="C22")
C32 = Class(name="C32")

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

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# B1 class attributes and methods
B1_attB: Property = Property(name="attB", type=IntegerType)
B1.attributes={B1_attB}

# C1 class attributes and methods
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1.attributes={C1_attC2, C1_attC1}

# R class attributes and methods

# Z class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# C2 class attributes and methods

# C3 class attributes and methods

# A2 class attributes and methods
A2_attA: Property = Property(name="attA", type=StringType)
A2.attributes={A2_attA}

# B2 class attributes and methods
B2_attB: Property = Property(name="attB", type=IntegerType)
B2.attributes={B2_attB}

# C4 class attributes and methods
C4_attC1: Property = Property(name="attC1", type=IntegerType)
C4_attC2: Property = Property(name="attC2", type=BooleanType)
C4.attributes={C4_attC2, C4_attC1}

# R2 class attributes and methods

# Z2 class attributes and methods

# Y2 class attributes and methods
Y2_attY: Property = Property(name="attY", type=StringType)
Y2.attributes={Y2_attY}

# C22 class attributes and methods

# C32 class attributes and methods

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
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
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
        Property(name="b9", type=B1, multiplicity=Multiplicity(0, 1))
    }
)
R_A2: BinaryAssociation = BinaryAssociation(
    name="R_A2",
    ends={
        Property(name="aR10", type=A2, multiplicity=Multiplicity(0, 9999)),
        Property(name="r11", type=R2, multiplicity=Multiplicity(0, 1))
    }
)
A_B22: BinaryAssociation = BinaryAssociation(
    name="A_B22",
    ends={
        Property(name="b12", type=B2, multiplicity=Multiplicity(1, 9999)),
        Property(name="a13", type=A2, multiplicity=Multiplicity(0, 1))
    }
)
B_C22: BinaryAssociation = BinaryAssociation(
    name="B_C22",
    ends={
        Property(name="c14", type=C4, multiplicity=Multiplicity(0, 9999)),
        Property(name="b15", type=B2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_tQL6oC_EEeifBcOeQWIjJw",
    types={A, B, C, A1, B1, C1, R, Z, Y, C2, C3, A2, B2, C4, R2, Z2, Y2, C22, C32},
    associations={A_B, B_C, R_A, A_B2, B_C2, R_A2, A_B22, B_C22},
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
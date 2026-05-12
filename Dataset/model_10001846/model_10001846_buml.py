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
A1 = Class(name="A1")
B1 = Class(name="B1")
C1 = Class(name="C1")
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
A12 = Class(name="A12", is_abstract=True)
B12 = Class(name="B12")
C12 = Class(name="C12")
Y2 = Class(name="Y2")
R2 = Class(name="R2")
Z2 = Class(name="Z2")
C22 = Class(name="C22")
C32 = Class(name="C32")

# A1 class attributes and methods
A1_altA: Property = Property(name="altA", type=StringType)
A1.attributes={A1_altA}

# B1 class attributes and methods
B1_altB1: Property = Property(name="altB1", type=IntegerType)
B1.attributes={B1_altB1}

# C1 class attributes and methods
C1_altC1: Property = Property(name="altC1", type=IntegerType)
C1_altc2: Property = Property(name="altc2", type=BooleanType)
C1.attributes={C1_altC1, C1_altc2}

# Y class attributes and methods
Y_alty: Property = Property(name="alty", type=StringType)
Y.attributes={Y_alty}

# R class attributes and methods

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# A12 class attributes and methods
A12_altA: Property = Property(name="altA", type=StringType)
A12.attributes={A12_altA}

# B12 class attributes and methods
B12_altB1: Property = Property(name="altB1", type=IntegerType)
B12.attributes={B12_altB1}

# C12 class attributes and methods
C12_altC1: Property = Property(name="altC1", type=IntegerType)
C12_altc2: Property = Property(name="altc2", type=BooleanType)
C12.attributes={C12_altC1, C12_altc2}

# Y2 class attributes and methods
Y2_alty: Property = Property(name="alty", type=StringType)
Y2.attributes={Y2_alty}

# R2 class attributes and methods

# Z2 class attributes and methods

# C22 class attributes and methods

# C32 class attributes and methods

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR2", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r3", type=R, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c4", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=B1, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b6", type=B12, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=A12, multiplicity=Multiplicity(0, 1))
    }
)
R_A2: BinaryAssociation = BinaryAssociation(
    name="R_A2",
    ends={
        Property(name="aR8", type=A12, multiplicity=Multiplicity(0, 9999)),
        Property(name="r9", type=R2, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c10", type=C12, multiplicity=Multiplicity(0, 9999)),
        Property(name="b11", type=B12, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__1eBMOm0EeiV94kHgjpOMg",
    types={A1, B1, C1, Y, R, Z, C2, C3, A12, B12, C12, Y2, R2, Z2, C22, C32},
    associations={A_B, R_A, B_C, A_B2, R_A2, B_C2},
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
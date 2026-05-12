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
Y = Class(name="Y")
R = Class(name="R")
A1 = Class(name="A1")
Z = Class(name="Z")
B1 = Class(name="B1")
c = Class(name="c")
c2 = Class(name="c2")
c3 = Class(name="c3")

# A class attributes and methods
A_atta: Property = Property(name="atta", type=StringType)
A.attributes={A_atta}

# B class attributes and methods
B_attb: Property = Property(name="attb", type=IntegerType)
B.attributes={B_attb}

# C class attributes and methods
C_att1: Property = Property(name="att1", type=IntegerType)
C_att2: Property = Property(name="att2", type=BooleanType)
C.attributes={C_att1, C_att2}

# Y class attributes and methods
Y_atty: Property = Property(name="atty", type=StringType)
Y.attributes={Y_atty}

# R class attributes and methods

# A1 class attributes and methods
A1_atta: Property = Property(name="atta", type=StringType)
A1.attributes={A1_atta}

# Z class attributes and methods

# B1 class attributes and methods
B1_attb: Property = Property(name="attb", type=IntegerType)
B1.attributes={B1_attb}

# c class attributes and methods
c_att1: Property = Property(name="att1", type=IntegerType)
c_att2: Property = Property(name="att2", type=BooleanType)
c.attributes={c_att1, c_att2}

# c2 class attributes and methods

# c3 class attributes and methods

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
        Property(name="b3", type=B, multiplicity=Multiplicity(1, 9999))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b4", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR6", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r7", type=R, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_NBtKcLskEeedTfUoC_GfaA",
    types={A, B, C, Y, R, A1, Z, B1, c, c2, c3},
    associations={A_B, B_C, A_B2, R_A},
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
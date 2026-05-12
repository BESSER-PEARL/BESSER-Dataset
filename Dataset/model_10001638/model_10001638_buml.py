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
A = Class(name="A")
B = Class(name="B")
R = Class(name="R")
Y = Class(name="Y")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
Z1 = Class(name="Z1")

# C class attributes and methods
C_altC1: Property = Property(name="altC1", type=IntegerType)
C_altC2: Property = Property(name="altC2", type=BooleanType)
C.attributes={C_altC2, C_altC1}

# A class attributes and methods
A_altA: Property = Property(name="altA", type=StringType)
A.attributes={A_altA}

# B class attributes and methods
B_altB: Property = Property(name="altB", type=StringType)
B.attributes={B_altB}

# R class attributes and methods

# Y class attributes and methods

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# Z1 class attributes and methods

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 9999))
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
        Property(name="b4", type=B, multiplicity=Multiplicity(0, 9999)),
        Property(name="a5", type=A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_LAF4MM7REeeLcIicqHdTUQ",
    types={C, A, B, R, Y, Z, C2, C3, Z1},
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
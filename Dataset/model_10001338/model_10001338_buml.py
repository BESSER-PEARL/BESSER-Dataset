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
B1 = Class(name="B1")
A1 = Class(name="A1")
C1 = Class(name="C1")
C3 = Class(name="C3")
C2 = Class(name="C2")
R = Class(name="R")
Z = Class(name="Z")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=StringType)
B.attributes={B_attB}

# C class attributes and methods
C_attC: Property = Property(name="attC", type=StringType)
C.attributes={C_attC}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# B1 class attributes and methods
B1_attB: Property = Property(name="attB", type=StringType)
B1.attributes={B1_attB}

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# C1 class attributes and methods
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1.attributes={C1_attC1, C1_attC2}

# C3 class attributes and methods

# C2 class attributes and methods

# R class attributes and methods

# Z class attributes and methods

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
Class3_Class2: BinaryAssociation = BinaryAssociation(
    name="Class3_Class2",
    ends={
        Property(name="b4", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
aR: BinaryAssociation = BinaryAssociation(
    name="aR",
    ends={
        Property(name="class36", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="class77", type=R, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c8", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b9", type=B1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0km_EAIUEeifsJ80ec9hDw",
    types={A, B, C, Y, B1, A1, C1, C3, C2, R, Z},
    associations={A_B, B_C, Class3_Class2, aR, B_C2},
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
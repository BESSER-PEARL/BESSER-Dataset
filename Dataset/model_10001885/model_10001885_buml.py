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
A1 = Class(name="A1")
B1 = Class(name="B1")
C1 = Class(name="C1")
C2 = Class(name="C2")
C3 = Class(name="C3")

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
C1.attributes={C1_attC1, C1_attC2}

# C2 class attributes and methods

# C3 class attributes and methods

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
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c4", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=B1, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b6", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=A1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_bEhHEOmiEeiV94kHgjpOMg",
    types={A, B, C, A1, B1, C1, C2, C3},
    associations={A_B, B_C, B_C2, A_B2},
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
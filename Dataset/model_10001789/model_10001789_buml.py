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
R = Class(name="R")
Y = Class(name="Y")
Z = Class(name="Z")
C6 = Class(name="C6")
C5 = Class(name="C5")
C4 = Class(name="C4", is_abstract=True)
A4 = Class(name="A4", is_abstract=True)
B4 = Class(name="B4")
Personne = Class(name="Personne")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC2, C_attC1}

# R class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# Z class attributes and methods

# C6 class attributes and methods

# C5 class attributes and methods

# C4 class attributes and methods
C4_attC1: Property = Property(name="attC1", type=IntegerType)
C4_attC2: Property = Property(name="attC2", type=BooleanType)
C4.attributes={C4_attC1, C4_attC2}

# A4 class attributes and methods
A4_attA: Property = Property(name="attA", type=StringType)
A4.attributes={A4_attA}

# B4 class attributes and methods
B4_attB: Property = Property(name="attB", type=IntegerType)
B4.attributes={B4_attB}

# Personne class attributes and methods

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
B_C4: BinaryAssociation = BinaryAssociation(
    name="B_C4",
    ends={
        Property(name="c4", type=C4, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=B4, multiplicity=Multiplicity(1, 1))
    }
)
R_A4: BinaryAssociation = BinaryAssociation(
    name="R_A4",
    ends={
        Property(name="aR6", type=A4, multiplicity=Multiplicity(0, 9999)),
        Property(name="r7", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A4_B4: BinaryAssociation = BinaryAssociation(
    name="A4_B4",
    ends={
        Property(name="b8", type=B4, multiplicity=Multiplicity(1, 9999)),
        Property(name="a9", type=A4, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_V_82cOmhEeiV94kHgjpOMg",
    types={A, B, C, R, Y, Z, C6, C5, C4, A4, B4, Personne},
    associations={A_B, B_C, B_C4, R_A4, A4_B4},
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
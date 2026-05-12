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
Aa = Class(name="Aa")
Bb = Class(name="Bb")
Cc = Class(name="Cc")
A = Class(name="A", is_abstract=True)
Y = Class(name="Y")
R = Class(name="R")
B = Class(name="B")
Z = Class(name="Z")
C = Class(name="C", is_abstract=True)
C2 = Class(name="C2")
C3 = Class(name="C3")

# Aa class attributes and methods
Aa_attA: Property = Property(name="attA", type=StringType)
Aa.attributes={Aa_attA}

# Bb class attributes and methods
Bb_attB: Property = Property(name="attB", type=IntegerType)
Bb.attributes={Bb_attB}

# Cc class attributes and methods
Cc_attC1: Property = Property(name="attC1", type=IntegerType)
Cc_attC2: Property = Property(name="attC2", type=BooleanType)
Cc.attributes={Cc_attC1, Cc_attC2}

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# Z class attributes and methods

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# C2 class attributes and methods

# C3 class attributes and methods

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=Bb, multiplicity=Multiplicity(0, 1)),
        Property(name="a1", type=Aa, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=Cc, multiplicity=Multiplicity(0, 1)),
        Property(name="b3", type=Bb, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a4", type=A, multiplicity=Multiplicity(0, 1)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b6", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="a7", type=A, multiplicity=Multiplicity(0, 1))
    }
)
C_B: BinaryAssociation = BinaryAssociation(
    name="C_B",
    ends={
        Property(name="b8", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="c9", type=C, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Hr0oEMUuEeeWu_SLkciAbg",
    types={Aa, Bb, Cc, A, Y, R, B, Z, C, C2, C3},
    associations={A_B, B_C, R_A, A_B2, C_B},
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
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
Y = Class(name="Y")
R = Class(name="R")
A = Class(name="A", is_abstract=True)
B = Class(name="B")
Z = Class(name="Z")
C = Class(name="C")
C2 = Class(name="C2")
C3 = Class(name="C3")

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

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
Class4_Class6: BinaryAssociation = BinaryAssociation(
    name="Class4_Class6",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="class41", type=B, multiplicity=Multiplicity(0, 1))
    }
)
Class2_Class3: BinaryAssociation = BinaryAssociation(
    name="Class2_Class3",
    ends={
        Property(name="aR2", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r3", type=R, multiplicity=Multiplicity(0, 1))
    }
)
Class3_Class4: BinaryAssociation = BinaryAssociation(
    name="Class3_Class4",
    ends={
        Property(name="b4", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_DMsRIOm0EeiV94kHgjpOMg",
    types={Y, R, A, B, Z, C, C2, C3},
    associations={Class4_Class6, Class2_Class3, Class3_Class4},
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
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
A1 = Class(name="A1", is_abstract=True)
R = Class(name="R")
Z = Class(name="Z")
B1 = Class(name="B1")
C1 = Class(name="C1", is_abstract=True)
C2 = Class(name="C2")
C3 = Class(name="C3")

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# R class attributes and methods

# Z class attributes and methods

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
A_B22222: BinaryAssociation = BinaryAssociation(
    name="A_B22222",
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
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c4", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=B1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Gf5R0Om1EeiV94kHgjpOMg",
    types={Y, A1, R, Z, B1, C1, C2, C3},
    associations={A_B22222, R_A, B_C2},
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
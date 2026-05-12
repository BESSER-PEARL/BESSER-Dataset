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

# A class attributes and methods
A_attrA1: Property = Property(name="attrA1", type=IntegerType)
A_attrA2: Property = Property(name="attrA2", type=StringType)
A.attributes={A_attrA1, A_attrA2}

# B class attributes and methods
B_attrB1: Property = Property(name="attrB1", type=IntegerType)
B_attrB2: Property = Property(name="attrB2", type=StringType)
B.attributes={B_attrB2, B_attrB1}

# C class attributes and methods
C_attrC1: Property = Property(name="attrC1", type=IntegerType)
C_attrC2: Property = Property(name="attrC2", type=StringType)
C.attributes={C_attrC1, C_attrC2}

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
C_B: BinaryAssociation = BinaryAssociation(
    name="C_B",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(0, 9999)),
        Property(name="c3", type=C, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Xh3SoPJIEei0SKJPiR2ViA",
    types={A, B, C},
    associations={A_B, C_B},
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
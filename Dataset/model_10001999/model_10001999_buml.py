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
A_attrA: Property = Property(name="attrA", type=StringType)
A.attributes={A_attrA}

# B class attributes and methods
B_attrB: Property = Property(name="attrB", type=StringType)
B.attributes={B_attrB}

# C class attributes and methods
C_attrCA: Property = Property(name="attrCA", type=IntegerType)
C_attrC2: Property = Property(name="attrC2", type=BooleanType)
C.attributes={C_attrCA, C_attrC2}

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=C, multiplicity=Multiplicity(0, 1)),
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_iahzsCPTEeisAYMSV00L2Q",
    types={A, B, C},
    associations={A_B, B_C},
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
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
y = Class(name="y")
r = Class(name="r")
A = Class(name="A", is_abstract=True)
B = Class(name="B")
Z = Class(name="Z")
C = Class(name="C", is_abstract=True)
C2 = Class(name="C2")
C3 = Class(name="C3")

# y class attributes and methods
y_attY: Property = Property(name="attY", type=StringType)
y.attributes={y_attY}

# r class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attb: Property = Property(name="attb", type=IntegerType)
B.attributes={B_attb}

# Z class attributes and methods

# C class attributes and methods
C_attc1: Property = Property(name="attc1", type=IntegerType)
C_attc2: Property = Property(name="attc2", type=BooleanType)
C.attributes={C_attc1, C_attc2}

# C2 class attributes and methods

# C3 class attributes and methods

# Relationships
r__A: BinaryAssociation = BinaryAssociation(
    name="r__A",
    ends={
        Property(name="aR0", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r1", type=r, multiplicity=Multiplicity(0, 1))
    }
)
A__B: BinaryAssociation = BinaryAssociation(
    name="A__B",
    ends={
        Property(name="B2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="A3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c4", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="B5", type=B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_axMp8M9UEeeLcIicqHdTUQ",
    types={y, r, A, B, Z, C, C2, C3},
    associations={r__A, A__B, B_C},
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
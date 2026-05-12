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
C = Class(name="C")
B = Class(name="B")
r = Class(name="r")
z = Class(name="z")
y = Class(name="y")
c1 = Class(name="c1")
c2 = Class(name="c2")

# A class attributes and methods
A_atta: Property = Property(name="atta", type=StringType)
A.attributes={A_atta}

# C class attributes and methods
C_attc1: Property = Property(name="attc1", type=IntegerType)
C_attc2: Property = Property(name="attc2", type=BooleanType)
C.attributes={C_attc1, C_attc2}

# B class attributes and methods
B_attb: Property = Property(name="attb", type=StringType)
B.attributes={B_attb}

# r class attributes and methods

# z class attributes and methods

# y class attributes and methods
y_atty: Property = Property(name="atty", type=StringType)
y.attributes={y_atty}

# c1 class attributes and methods

# c2 class attributes and methods

# Relationships
Class_A: BinaryAssociation = BinaryAssociation(
    name="Class_A",
    ends={
        Property(name="ar4", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=r, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_QrpskPbZEeiqn80yrzdh8w",
    types={A, C, B, r, z, y, c1, c2},
    associations={Class_A, B_C, A_B2},
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
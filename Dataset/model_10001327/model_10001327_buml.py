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
C3 = Class(name="C3")
C2 = Class(name="C2")
Z = Class(name="Z")
R = Class(name="R")
Y = Class(name="Y")
A = Class(name="A")
B = Class(name="B")
A2 = Class(name="A2")
A3 = Class(name="A3")
B2 = Class(name="B2")
E = Class(name="E")
F = Class(name="F")
G = Class(name="G")

# C3 class attributes and methods

# C2 class attributes and methods

# Z class attributes and methods

# R class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# A class attributes and methods
A_b: Property = Property(name="b", type=BooleanType)
A_d: Property = Property(name="d", type=IntegerType)
A.attributes={A_b, A_d}

# B class attributes and methods

# A2 class attributes and methods

# A3 class attributes and methods

# B2 class attributes and methods

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# G class attributes and methods

# Relationships
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="c0", type=B, multiplicity=Multiplicity(0, 1)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
G_E: BinaryAssociation = BinaryAssociation(
    name="G_E",
    ends={
        Property(name="e2", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g3", type=G, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_00_WUOm0EeiV94kHgjpOMg",
    types={C3, C2, Z, R, Y, A, B, A2, A3, B2, E, F, G},
    associations={A_B2, G_E},
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
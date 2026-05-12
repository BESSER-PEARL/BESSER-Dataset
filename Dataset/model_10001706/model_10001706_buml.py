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
B = Class(name="B")
C = Class(name="C", is_abstract=True)
A = Class(name="A", is_abstract=True)
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
E = Class(name="E")
F = Class(name="F")
G = Class(name="G")

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_atC1: Property = Property(name="atC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_atC1, C_attC2}

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# G class attributes and methods

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR4", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
G_E: BinaryAssociation = BinaryAssociation(
    name="G_E",
    ends={
        Property(name="e6", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g7", type=G, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_PkgXoNWtEeehRMl7r1_c5g",
    types={B, C, A, Y, R, Z, C2, C3, E, F, G},
    associations={B_C, A_B, R_A, G_E},
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
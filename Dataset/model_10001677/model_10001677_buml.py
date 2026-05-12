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
Y = Class(name="Y")
R = Class(name="R")
AA = Class(name="AA")
BB = Class(name="BB")
Z = Class(name="Z")
CC = Class(name="CC")
C2 = Class(name="C2")
C3 = Class(name="C3")
Personne = Class(name="Personne")
union = Class(name="union")
Mariage = Class(name="Mariage")
PACS = Class(name="PACS")

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

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# AA class attributes and methods
AA_attA: Property = Property(name="attA", type=StringType)
AA.attributes={AA_attA}

# BB class attributes and methods
BB_attB: Property = Property(name="attB", type=IntegerType)
BB.attributes={BB_attB}

# Z class attributes and methods

# CC class attributes and methods
CC_attC1: Property = Property(name="attC1", type=IntegerType)
CC_attC2: Property = Property(name="attC2", type=BooleanType)
CC.attributes={CC_attC1, CC_attC2}

# C2 class attributes and methods

# C3 class attributes and methods

# Personne class attributes and methods

# union class attributes and methods

# Mariage class attributes and methods

# PACS class attributes and methods

# Relationships
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="personne14", type=Personne, multiplicity=Multiplicity(0, 9999)),
        Property(name="enfants15", type=Personne, multiplicity=Multiplicity(0, 2))
    }
)
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
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a4", type=AA, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b6", type=BB, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=AA, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c8", type=CC, multiplicity=Multiplicity(0, 9999)),
        Property(name="b9", type=BB, multiplicity=Multiplicity(0, 1))
    }
)
Personne_union: BinaryAssociation = BinaryAssociation(
    name="Personne_union",
    ends={
        Property(name="union10", type=union, multiplicity=Multiplicity(0, 9999)),
        Property(name="per11", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_union2: BinaryAssociation = BinaryAssociation(
    name="Personne_union2",
    ends={
        Property(name="unionActuelle12", type=union, multiplicity=Multiplicity(0, 1)),
        Property(name="personne13", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_OIVZoPJXEei0SKJPiR2ViA",
    types={A, B, C, Y, R, AA, BB, Z, CC, C2, C3, Personne, union, Mariage, PACS},
    associations={Personne_Personne, A_B, B_C, R_A, A_B2, B_C2, Personne_union, Personne_union2},
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
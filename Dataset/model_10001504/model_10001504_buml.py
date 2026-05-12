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
A = Class(name="A")
Z = Class(name="Z")
C1 = Class(name="C1")
B = Class(name="B")
C = Class(name="C")
C2 = Class(name="C2")
Personne = Class(name="Personne")
Union = Class(name="Union")
Mariage = Class(name="Mariage")
PACS = Class(name="PACS")

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# Z class attributes and methods

# C1 class attributes and methods

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# C2 class attributes and methods

# Personne class attributes and methods

# Union class attributes and methods
Union_dateUnion: Property = Property(name="dateUnion", type=IntegerType)
Union.attributes={Union_dateUnion}

# Mariage class attributes and methods

# PACS class attributes and methods

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 1))
    }
)
Y_B: BinaryAssociation = BinaryAssociation(
    name="Y_B",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="y3", type=Y, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR4", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents6", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants7", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Union: BinaryAssociation = BinaryAssociation(
    name="Personne_Union",
    ends={
        Property(name="union8", type=Union, multiplicity=Multiplicity(0, 9999)),
        Property(name="pers9", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Union2: BinaryAssociation = BinaryAssociation(
    name="Personne_Union2",
    ends={
        Property(name="unionActuelle10", type=Union, multiplicity=Multiplicity(0, 1)),
        Property(name="personne11", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_BYFEIPJgEei0SKJPiR2ViA",
    types={Y, R, A, Z, C1, B, C, C2, Personne, Union, Mariage, PACS},
    associations={B_C, Y_B, R_A, Personne_Personne, Personne_Union, Personne_Union2},
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
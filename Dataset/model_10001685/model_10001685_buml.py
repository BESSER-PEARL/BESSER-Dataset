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
A2 = Class(name="A2")
B2 = Class(name="B2")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
C4 = Class(name="C4")
Personne = Class(name="Personne")
Union = Class(name="Union")
Mariage = Class(name="Mariage")
PACs = Class(name="PACs")
E = Class(name="E")
F = Class(name="F")
G = Class(name="G")

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

# A2 class attributes and methods
A2_attA: Property = Property(name="attA", type=StringType)
A2.attributes={A2_attA}

# B2 class attributes and methods
B2_attB: Property = Property(name="attB", type=IntegerType)
B2.attributes={B2_attB}

# Z class attributes and methods

# C2 class attributes and methods
C2_attC1: Property = Property(name="attC1", type=IntegerType)
C2_attC2: Property = Property(name="attC2", type=IntegerType)
C2.attributes={C2_attC1, C2_attC2}

# C3 class attributes and methods

# C4 class attributes and methods

# Personne class attributes and methods

# Union class attributes and methods
Union_dateUnion: Property = Property(name="dateUnion", type=StringType)
Union.attributes={Union_dateUnion}

# Mariage class attributes and methods

# PACs class attributes and methods

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# G class attributes and methods

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a4", type=A2, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b6", type=B2, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=A2, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c8", type=C2, multiplicity=Multiplicity(0, 9999)),
        Property(name="b9", type=B2, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents10", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants11", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Union: BinaryAssociation = BinaryAssociation(
    name="Personne_Union",
    ends={
        Property(name="union12", type=Union, multiplicity=Multiplicity(0, 9999)),
        Property(name="pers13", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Union2: BinaryAssociation = BinaryAssociation(
    name="Personne_Union2",
    ends={
        Property(name="unionActuelles14", type=Union, multiplicity=Multiplicity(0, 1)),
        Property(name="personnes15", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
G_E: BinaryAssociation = BinaryAssociation(
    name="G_E",
    ends={
        Property(name="e16", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g17", type=G, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_OPGDkO_TEeiH57IZcqf8WA",
    types={A, B, C, Y, R, A2, B2, Z, C2, C3, C4, Personne, Union, Mariage, PACs, E, F, G},
    associations={A_B, B_C, R_A, A_B2, B_C2, Personne_Personne, Personne_Union, Personne_Union2, G_E},
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
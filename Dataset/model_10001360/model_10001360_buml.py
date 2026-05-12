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
C2 = Class(name="C2")
C3 = Class(name="C3")
Z = Class(name="Z")
Union = Class(name="Union")
Personne = Class(name="Personne")
Mariage = Class(name="Mariage")
PACS = Class(name="PACS")
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
C_attc1: Property = Property(name="attc1", type=IntegerType)
C_attc2: Property = Property(name="attc2", type=BooleanType)
C.attributes={C_attc2, C_attc1}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# Z class attributes and methods

# Union class attributes and methods
Union_dateUnion: Property = Property(name="dateUnion", type=Union)
Union.attributes={Union_dateUnion}

# Personne class attributes and methods

# Mariage class attributes and methods

# PACS class attributes and methods

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# G class attributes and methods

# Relationships
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR4", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Union: BinaryAssociation = BinaryAssociation(
    name="Personne_Union",
    ends={
        Property(name="union6", type=Union, multiplicity=Multiplicity(0, 9999)),
        Property(name="pers7", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Union_Personne: BinaryAssociation = BinaryAssociation(
    name="Union_Personne",
    ends={
        Property(name="personnes8", type=Personne, multiplicity=Multiplicity(2, 2)),
        Property(name="unionActuelle9", type=Union, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents10", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfant11", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
G_E: BinaryAssociation = BinaryAssociation(
    name="G_E",
    ends={
        Property(name="e12", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g13", type=G, multiplicity=Multiplicity(0, 1))
    }
)
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

# Domain Model
domain_model = DomainModel(
    name="_27wI0PJXEei0SKJPiR2ViA",
    types={A, B, C, Y, R, C2, C3, Z, Union, Personne, Mariage, PACS, E, F, G},
    associations={R_A, Personne_Union, Union_Personne, Personne_Personne, G_E, B_C, A_B},
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
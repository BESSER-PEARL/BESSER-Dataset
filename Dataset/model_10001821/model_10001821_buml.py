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
A = Class(name="A", is_abstract=True)
B = Class(name="B")
C = Class(name="C")
Y = Class(name="Y")
Z = Class(name="Z")
R = Class(name="R")
C2 = Class(name="C2")
C3 = Class(name="C3")
Union = Class(name="Union")
Personne = Class(name="Personne")
Mariage = Class(name="Mariage")
PACS = Class(name="PACS")
F = Class(name="F")
E = Class(name="E")
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

# Z class attributes and methods

# R class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# Union class attributes and methods
Union_dateUnion: Property = Property(name="dateUnion", type=StringType)
Union.attributes={Union_dateUnion}

# Personne class attributes and methods

# Mariage class attributes and methods

# PACS class attributes and methods

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# G class attributes and methods

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR2", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r3", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b4", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A, multiplicity=Multiplicity(0, 1))
    }
)
Union_Personne: BinaryAssociation = BinaryAssociation(
    name="Union_Personne",
    ends={
        Property(name="pers6", type=Personne, multiplicity=Multiplicity(2, 2)),
        Property(name="union7", type=Union, multiplicity=Multiplicity(0, 9999))
    }
)
Union_Personne2: BinaryAssociation = BinaryAssociation(
    name="Union_Personne2",
    ends={
        Property(name="personne8", type=Personne, multiplicity=Multiplicity(0, 9999)),
        Property(name="unionActuelle9", type=Union, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents10", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants11", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
G_F: BinaryAssociation = BinaryAssociation(
    name="G_F",
    ends={
        Property(name="e12", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g13", type=G, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Y6EXAOdYEeiDGLvZhbPYyA",
    types={A, B, C, Y, Z, R, C2, C3, Union, Personne, Mariage, PACS, F, E, G},
    associations={B_C, R_A, A_B, Union_Personne, Union_Personne2, Personne_Personne, G_F},
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
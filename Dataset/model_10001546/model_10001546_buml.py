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
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
Personne = Class(name="Personne")
Union = Class(name="Union")
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
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC2, C_attC1}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# Personne class attributes and methods

# Union class attributes and methods
Union_dateUnion: Property = Property(name="dateUnion", type=StringType)
Union.attributes={Union_dateUnion}

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
        Property(name="a0", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r1", type=R, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b4", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A, multiplicity=Multiplicity(0, 1))
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
G_E: BinaryAssociation = BinaryAssociation(
    name="G_E",
    ends={
        Property(name="e12", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g13", type=G, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EwAzIOm2EeiV94kHgjpOMg",
    types={A, B, C, Y, R, Z, C2, C3, Personne, Union, Mariage, PACS, E, F, G},
    associations={R_A, B_C, A_B2, Personne_Personne, Personne_Union, Personne_Union2, G_E},
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
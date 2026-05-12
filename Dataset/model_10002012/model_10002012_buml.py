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
A1 = Class(name="A1")
Z = Class(name="Z")
B1 = Class(name="B1")
C1 = Class(name="C1")
C2 = Class(name="C2")
C3 = Class(name="C3")
A2 = Class(name="A2")
A21 = Class(name="A21")
A3 = Class(name="A3")
B2 = Class(name="B2")
B21 = Class(name="B21")
Personne = Class(name="Personne")
Union = Class(name="Union")
PACS = Class(name="PACS")
Mariage = Class(name="Mariage")
E = Class(name="E")
F = Class(name="F")
G = Class(name="G")
Y3 = Class(name="Y3")
R3 = Class(name="R3")
A4 = Class(name="A4")
Z3 = Class(name="Z3")
B4 = Class(name="B4")
C5 = Class(name="C5")
C23 = Class(name="C23")
C33 = Class(name="C33")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# Z class attributes and methods

# B1 class attributes and methods
B1_attB: Property = Property(name="attB", type=IntegerType)
B1.attributes={B1_attB}

# C1 class attributes and methods
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1.attributes={C1_attC2, C1_attC1}

# C2 class attributes and methods

# C3 class attributes and methods

# A2 class attributes and methods
A2_d: Property = Property(name="d", type=IntegerType)
A2.attributes={A2_d}

# A21 class attributes and methods
A21_b: Property = Property(name="b", type=BooleanType)
A21.attributes={A21_b}

# A3 class attributes and methods

# B2 class attributes and methods

# B21 class attributes and methods

# Personne class attributes and methods

# Union class attributes and methods
Union_dateUnion: Property = Property(name="dateUnion", type=StringType)
Union.attributes={Union_dateUnion}

# PACS class attributes and methods

# Mariage class attributes and methods

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# G class attributes and methods

# Y3 class attributes and methods
Y3_attY: Property = Property(name="attY", type=StringType)
Y3.attributes={Y3_attY}

# R3 class attributes and methods

# A4 class attributes and methods
A4_attA: Property = Property(name="attA", type=StringType)
A4.attributes={A4_attA}

# Z3 class attributes and methods

# B4 class attributes and methods
B4_attB: Property = Property(name="attB", type=IntegerType)
B4.attributes={B4_attB}

# C5 class attributes and methods
C5_attC1: Property = Property(name="attC1", type=IntegerType)
C5_attC2: Property = Property(name="attC2", type=BooleanType)
C5.attributes={C5_attC1, C5_attC2}

# C23 class attributes and methods

# C33 class attributes and methods

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
        Property(name="aR4", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b6", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c8", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b9", type=B1, multiplicity=Multiplicity(0, 1))
    }
)
A_B3: BinaryAssociation = BinaryAssociation(
    name="A_B3",
    ends={
        Property(name="c10", type=B2, multiplicity=Multiplicity(0, 1)),
        Property(name="A_B3_111", type=A2, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents12", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants13", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Union: BinaryAssociation = BinaryAssociation(
    name="Personne_Union",
    ends={
        Property(name="union14", type=Union, multiplicity=Multiplicity(0, 9999)),
        Property(name="personnes15", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Union2: BinaryAssociation = BinaryAssociation(
    name="Personne_Union2",
    ends={
        Property(name="unionActuelle16", type=Union, multiplicity=Multiplicity(0, 1)),
        Property(name="personnes17", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
G_E: BinaryAssociation = BinaryAssociation(
    name="G_E",
    ends={
        Property(name="e18", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g19", type=G, multiplicity=Multiplicity(0, 1))
    }
)
R_A3: BinaryAssociation = BinaryAssociation(
    name="R_A3",
    ends={
        Property(name="aR20", type=A4, multiplicity=Multiplicity(0, 9999)),
        Property(name="r21", type=R3, multiplicity=Multiplicity(0, 1))
    }
)
A_B4: BinaryAssociation = BinaryAssociation(
    name="A_B4",
    ends={
        Property(name="b22", type=B4, multiplicity=Multiplicity(1, 9999)),
        Property(name="a23", type=A4, multiplicity=Multiplicity(0, 1))
    }
)
B_C4: BinaryAssociation = BinaryAssociation(
    name="B_C4",
    ends={
        Property(name="c24", type=C5, multiplicity=Multiplicity(0, 9999)),
        Property(name="b25", type=B4, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jTs_wBD6EeqDmNBP3mfLQg",
    types={A, B, C, Y, R, A1, Z, B1, C1, C2, C3, A2, A21, A3, B2, B21, Personne, Union, PACS, Mariage, E, F, G, Y3, R3, A4, Z3, B4, C5, C23, C33},
    associations={A_B, B_C, R_A, A_B2, B_C2, A_B3, Personne_Personne, Personne_Union, Personne_Union2, G_E, R_A3, A_B4, B_C4},
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
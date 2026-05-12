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
C = Class(name="C")
A1 = Class(name="A1", is_abstract=True)
R = Class(name="R")
Y = Class(name="Y")
Z = Class(name="Z")
C1 = Class(name="C1", is_abstract=True)
C11 = Class(name="C11")
C2 = Class(name="C2")
B1 = Class(name="B1")
B2 = Class(name="B2")
A2 = Class(name="A2", is_abstract=True)
A21 = Class(name="A21")
A3 = Class(name="A3")
B21 = Class(name="B21")
Personne = Class(name="Personne")
Union = Class(name="Union")
Mariage = Class(name="Mariage")
PACS = Class(name="PACS")
Date = Class(name="Date")
E = Class(name="E")
F = Class(name="F")
G = Class(name="G")
A = Class(name="A")

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC2, C_attC1}

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# R class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# Z class attributes and methods

# C1 class attributes and methods
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1.attributes={C1_attC2, C1_attC1}

# C11 class attributes and methods

# C2 class attributes and methods

# B1 class attributes and methods
B1_attB: Property = Property(name="attB", type=IntegerType)
B1.attributes={B1_attB}

# B2 class attributes and methods

# A2 class attributes and methods
A2_d: Property = Property(name="d", type=IntegerType)
A2.attributes={A2_d}

# A21 class attributes and methods
A21_b: Property = Property(name="b", type=BooleanType)
A21.attributes={A21_b}

# A3 class attributes and methods

# B21 class attributes and methods

# Personne class attributes and methods

# Union class attributes and methods
Union_dateUnion: Property = Property(name="dateUnion", type=Date)
Union.attributes={Union_dateUnion}

# Mariage class attributes and methods

# PACS class attributes and methods

# Date class attributes and methods

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# G class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

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
        Property(name="b3", type=B, multiplicity=Multiplicity(1, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1)),
        Property(name="aR4", type=A1, multiplicity=Multiplicity(0, 9999))
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
        Property(name="c8", type=C1, multiplicity=Multiplicity(0, 1)),
        Property(name="b9", type=B1, multiplicity=Multiplicity(0, 1))
    }
)
B_C3: BinaryAssociation = BinaryAssociation(
    name="B_C3",
    ends={
        Property(name="c10", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b11", type=B1, multiplicity=Multiplicity(0, 1))
    }
)
A_B3: BinaryAssociation = BinaryAssociation(
    name="A_B3",
    ends={
        Property(name="c12", type=B2, multiplicity=Multiplicity(0, 1)),
        Property(name="a13", type=A2, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents14", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants15", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Union: BinaryAssociation = BinaryAssociation(
    name="Personne_Union",
    ends={
        Property(name="union16", type=Union, multiplicity=Multiplicity(0, 9999)),
        Property(name="pers17", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Union2: BinaryAssociation = BinaryAssociation(
    name="Personne_Union2",
    ends={
        Property(name="unionActuelle18", type=Union, multiplicity=Multiplicity(0, 1)),
        Property(name="personnes19", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
G_E: BinaryAssociation = BinaryAssociation(
    name="G_E",
    ends={
        Property(name="e20", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g21", type=G, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_dnWmgAnUEeqB3a4sRh_tuQ",
    types={B, C, A1, R, Y, Z, C1, C11, C2, B1, B2, A2, A21, A3, B21, Personne, Union, Mariage, PACS, Date, E, F, G, A},
    associations={A_B, B_C, R_A, A_B2, B_C2, B_C3, A_B3, Personne_Personne, Personne_Union, Personne_Union2, G_E},
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
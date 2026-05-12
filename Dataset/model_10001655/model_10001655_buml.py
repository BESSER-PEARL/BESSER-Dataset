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
A1 = Class(name="A1", is_abstract=True)
B1 = Class(name="B1")
C1 = Class(name="C1", is_abstract=True)
C2 = Class(name="C2")
C3 = Class(name="C3")
Z = Class(name="Z")
Y = Class(name="Y")
R = Class(name="R")
Class_ = Class(name="Class")
Personne = Class(name="Personne")
Union = Class(name="Union")
Mariage = Class(name="Mariage")
PACS = Class(name="PACS")
E = Class(name="E")
F = Class(name="F")

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

# A1 class attributes and methods
A1_attA: Property = Property(name="attA", type=StringType)
A1.attributes={A1_attA}

# B1 class attributes and methods
B1_attB: Property = Property(name="attB", type=IntegerType)
B1.attributes={B1_attB}

# C1 class attributes and methods
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1.attributes={C1_attC2, C1_attC1}

# C2 class attributes and methods

# C3 class attributes and methods

# Z class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Class class attributes and methods

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

# Relationships
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
        Property(name="b4", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c6", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b7", type=B1, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR8", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r9", type=R, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Union: BinaryAssociation = BinaryAssociation(
    name="Personne_Union",
    ends={
        Property(name="union10", type=Union, multiplicity=Multiplicity(0, 9999)),
        Property(name="pers11", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Union2: BinaryAssociation = BinaryAssociation(
    name="Personne_Union2",
    ends={
        Property(name="unionActuelle12", type=Union, multiplicity=Multiplicity(0, 1)),
        Property(name="personnes13", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents14", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants15", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_MO_AwOmjEeiV94kHgjpOMg",
    types={A, B, C, A1, B1, C1, C2, C3, Z, Y, R, Class_, Personne, Union, Mariage, PACS, E, F},
    associations={B_C, A_B2, B_C2, R_A, Personne_Union, Personne_Union2, Personne_Personne, A_B},
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
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
Interface_Interface = Class(name="Interface_Interface")
A2 = Class(name="A2")
B2 = Class(name="B2")
C2 = Class(name="C2")
A1 = Class(name="A1")
B1 = Class(name="B1")
C1 = Class(name="C1")
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
C21 = Class(name="C21")
C3 = Class(name="C3")
A3 = Class(name="A3")
B3 = Class(name="B3")
C4 = Class(name="C4")
B21 = Class(name="B21")
A21 = Class(name="A21")
A31 = Class(name="A31")
PACS = Class(name="PACS")
Mariage = Class(name="Mariage")
Union = Class(name="Union")
Personne = Class(name="Personne")
Mariage1 = Class(name="Mariage1")
A5 = Class(name="A5")
B5 = Class(name="B5")
C5 = Class(name="C5")
Union1 = Class(name="Union1")

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

# Interface_Interface class attributes and methods

# A2 class attributes and methods
A2_attA: Property = Property(name="attA", type=StringType)
A2.attributes={A2_attA}

# B2 class attributes and methods
B2_attB: Property = Property(name="attB", type=IntegerType)
B2.attributes={B2_attB}

# C2 class attributes and methods
C2_attC1: Property = Property(name="attC1", type=IntegerType)
C2_attC2: Property = Property(name="attC2", type=BooleanType)
C2.attributes={C2_attC2, C2_attC1}

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

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Z class attributes and methods

# C21 class attributes and methods

# C3 class attributes and methods

# A3 class attributes and methods
A3_b: Property = Property(name="b", type=BooleanType)
A3_c: Property = Property(name="c", type=B)
A3_d: Property = Property(name="d", type=IntegerType)
A3.attributes={A3_d, A3_b, A3_c}

# B3 class attributes and methods

# C4 class attributes and methods

# B21 class attributes and methods

# A21 class attributes and methods

# A31 class attributes and methods

# PACS class attributes and methods

# Mariage class attributes and methods

# Union class attributes and methods

# Personne class attributes and methods

# Mariage1 class attributes and methods

# A5 class attributes and methods
A5_attA: Property = Property(name="attA", type=StringType)
A5.attributes={A5_attA}

# B5 class attributes and methods
B5_attB: Property = Property(name="attB", type=IntegerType)
B5.attributes={B5_attB}

# C5 class attributes and methods
C5_attC1: Property = Property(name="attC1", type=IntegerType)
C5_attC2: Property = Property(name="attC2", type=BooleanType)
C5.attributes={C5_attC1, C5_attC2}

# Union1 class attributes and methods
Union1_dateUnion: Property = Property(name="dateUnion", type=StringType)
Union1.attributes={Union1_dateUnion}

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b0", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c2", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A_B2: BinaryAssociation = BinaryAssociation(
    name="A_B2",
    ends={
        Property(name="b4", type=B2, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A2, multiplicity=Multiplicity(0, 1))
    }
)
B_C22: BinaryAssociation = BinaryAssociation(
    name="B_C22",
    ends={
        Property(name="c6", type=C2, multiplicity=Multiplicity(0, 9999)),
        Property(name="b7", type=B2, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR12", type=A1, multiplicity=Multiplicity(0, 9999)),
        Property(name="r13", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B4: BinaryAssociation = BinaryAssociation(
    name="A_B4",
    ends={
        Property(name="b14", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a15", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
A_B5: BinaryAssociation = BinaryAssociation(
    name="A_B5",
    ends={
        Property(name="c16", type=B3, multiplicity=Multiplicity(0, 1)),
        Property(name="a17", type=A3, multiplicity=Multiplicity(0, 1))
    }
)
A2_A: BinaryAssociation = BinaryAssociation(
    name="A2_A",
    ends={
        Property(name="a18", type=A3, multiplicity=Multiplicity(0, 1)),
        Property(name="a219", type=A21, multiplicity=Multiplicity(0, 1))
    }
)
Mariage_Union: BinaryAssociation = BinaryAssociation(
    name="Mariage_Union",
    ends={
        Property(name="union20", type=Union, multiplicity=Multiplicity(0, 1)),
        Property(name="mariage21", type=Mariage, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Union: BinaryAssociation = BinaryAssociation(
    name="Personne_Union",
    ends={
        Property(name="union22", type=Union, multiplicity=Multiplicity(2, 2)),
        Property(name="personne23", type=Personne, multiplicity=Multiplicity(1, 1))
    }
)
A_B51: BinaryAssociation = BinaryAssociation(
    name="A_B51",
    ends={
        Property(name="b24", type=B5, multiplicity=Multiplicity(1, 9999)),
        Property(name="a25", type=A5, multiplicity=Multiplicity(0, 1))
    }
)
B_C25: BinaryAssociation = BinaryAssociation(
    name="B_C25",
    ends={
        Property(name="c26", type=C5, multiplicity=Multiplicity(0, 9999)),
        Property(name="b27", type=B5, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Union2: BinaryAssociation = BinaryAssociation(
    name="Personne_Union2",
    ends={
        Property(name="unions28", type=Union1, multiplicity=Multiplicity(0, 9999)),
        Property(name="pers29", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Union3: BinaryAssociation = BinaryAssociation(
    name="Personne_Union3",
    ends={
        Property(name="unionActuelle30", type=Union1, multiplicity=Multiplicity(0, 1)),
        Property(name="personne31", type=Personne, multiplicity=Multiplicity(2, 2))
    }
)
Personne_Personne: BinaryAssociation = BinaryAssociation(
    name="Personne_Personne",
    ends={
        Property(name="parents32", type=Personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants33", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
A_B3: BinaryAssociation = BinaryAssociation(
    name="A_B3",
    ends={
        Property(name="b8", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a9", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
B_C23: BinaryAssociation = BinaryAssociation(
    name="B_C23",
    ends={
        Property(name="c10", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b11", type=B1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_p2Z6gAepEeqFfO0RhT_ZfA",
    types={A, B, C, Interface_Interface, A2, B2, C2, A1, B1, C1, Y, R, Z, C21, C3, A3, B3, C4, B21, A21, A31, PACS, Mariage, Union, Personne, Mariage1, A5, B5, C5, Union1},
    associations={A_B, B_C2, A_B2, B_C22, R_A, A_B4, A_B5, A2_A, Mariage_Union, Personne_Union, A_B51, B_C25, Personne_Union2, Personne_Union3, Personne_Personne, A_B3, B_C23},
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
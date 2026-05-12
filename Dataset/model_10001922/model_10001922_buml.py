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
R = Class(name="R")
Y = Class(name="Y")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
personne = Class(name="personne")
mariage = Class(name="mariage")
pacs = Class(name="pacs")
union = Class(name="union")
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

# R class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# personne class attributes and methods

# mariage class attributes and methods

# pacs class attributes and methods

# union class attributes and methods

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
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR4", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r5", type=R, multiplicity=Multiplicity(0, 1))
    }
)
personne_union: BinaryAssociation = BinaryAssociation(
    name="personne_union",
    ends={
        Property(name="union6", type=union, multiplicity=Multiplicity(0, 9999)),
        Property(name="pers7", type=personne, multiplicity=Multiplicity(2, 2))
    }
)
personne_personne: BinaryAssociation = BinaryAssociation(
    name="personne_personne",
    ends={
        Property(name="parents8", type=personne, multiplicity=Multiplicity(0, 2)),
        Property(name="enfants9", type=personne, multiplicity=Multiplicity(0, 9999))
    }
)
personne_union2: BinaryAssociation = BinaryAssociation(
    name="personne_union2",
    ends={
        Property(name="unionActuelle10", type=union, multiplicity=Multiplicity(0, 1)),
        Property(name="personnes11", type=personne, multiplicity=Multiplicity(2, 2))
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
    name="_dV5T0OwTEei9dNtZPq67hQ",
    types={B, C, R, Y, Z, C2, C3, personne, mariage, pacs, union, E, F, G, A},
    associations={B_C, A_B, R_A, personne_union, personne_personne, personne_union2, G_E},
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
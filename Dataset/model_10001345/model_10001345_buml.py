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
model2_C1 = Class(name="model2_C1")
model2_C2 = Class(name="model2_C2")
model2_C = Class(name="model2_C")
model2_Z = Class(name="model2_Z")
model2_A = Class(name="model2_A")
model2_Y = Class(name="model2_Y")
model2_B = Class(name="model2_B")
model2_R = Class(name="model2_R")
exo6_Polygone = Class(name="exo6_Polygone")
exo6_Point = Class(name="exo6_Point")
exo6_Triangle = Class(name="exo6_Triangle")
Class_ = Class(name="Class")

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

# model2_C1 class attributes and methods

# model2_C2 class attributes and methods

# model2_C class attributes and methods
model2_C_attC1: Property = Property(name="attC1", type=IntegerType)
model2_C_attC2: Property = Property(name="attC2", type=BooleanType)
model2_C.attributes={model2_C_attC2, model2_C_attC1}

# model2_Z class attributes and methods

# model2_A class attributes and methods
model2_A_attA: Property = Property(name="attA", type=StringType)
model2_A.attributes={model2_A_attA}

# model2_Y class attributes and methods
model2_Y_attY: Property = Property(name="attY", type=StringType)
model2_Y.attributes={model2_Y_attY}

# model2_B class attributes and methods
model2_B_attB: Property = Property(name="attB", type=IntegerType)
model2_B.attributes={model2_B_attB}

# model2_R class attributes and methods

# exo6_Polygone class attributes and methods
exo6_Polygone_sommets: Property = Property(name="sommets", type=model2_C)
exo6_Polygone.attributes={exo6_Polygone_sommets}

# exo6_Point class attributes and methods
exo6_Point_abcisse: Property = Property(name="abcisse", type=C)
exo6_Point_ordonnee: Property = Property(name="ordonnee", type=C)
exo6_Point.attributes={exo6_Point_abcisse, exo6_Point_ordonnee}

# exo6_Triangle class attributes and methods

# Class class attributes and methods

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
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c4", type=model2_C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b5", type=model2_B, multiplicity=Multiplicity(0, 1))
    }
)
A_R: BinaryAssociation = BinaryAssociation(
    name="A_R",
    ends={
        Property(name="r6", type=model2_R, multiplicity=Multiplicity(0, 1)),
        Property(name="aR7", type=model2_A, multiplicity=Multiplicity(0, 9999))
    }
)
B_A: BinaryAssociation = BinaryAssociation(
    name="B_A",
    ends={
        Property(name="a8", type=model2_A, multiplicity=Multiplicity(0, 1)),
        Property(name="b9", type=model2_B, multiplicity=Multiplicity(1, 9999))
    }
)
Polygone_Point: BinaryAssociation = BinaryAssociation(
    name="Polygone_Point",
    ends={
        Property(name="point10", type=exo6_Point, multiplicity=Multiplicity(0, 1)),
        Property(name="polygone11", type=exo6_Polygone, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_1CA8QLTbEeiOktH6zvsQYA",
    types={A, B, C, model2_C1, model2_C2, model2_C, model2_Z, model2_A, model2_Y, model2_B, model2_R, exo6_Polygone, exo6_Point, exo6_Triangle, Class_},
    associations={A_B, B_C, B_C2, A_R, B_A, Polygone_Point},
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
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
PERSONNEL = Class(name="PERSONNEL")
PERMIS = Class(name="PERMIS")
CHAUFFEUR = Class(name="CHAUFFEUR")
RESERVATION = Class(name="RESERVATION")
A = Class(name="A")
B = Class(name="B")
C = Class(name="C")
Y = Class(name="Y")
R = Class(name="R")
A1 = Class(name="A1")
Z = Class(name="Z")
B1 = Class(name="B1")
C1 = Class(name="C1")
C11 = Class(name="C11")
C2 = Class(name="C2")

# PERSONNEL class attributes and methods
PERSONNEL_nomPersonnel: Property = Property(name="nomPersonnel", type=StringType)
PERSONNEL_prenomPersonnel: Property = Property(name="prenomPersonnel", type=StringType)
PERSONNEL_unPrivate: Property = Property(name="unPrivate", type=BooleanType)
PERSONNEL.attributes={PERSONNEL_nomPersonnel, PERSONNEL_unPrivate, PERSONNEL_prenomPersonnel}

# PERMIS class attributes and methods
PERMIS_libPermis: Property = Property(name="libPermis", type=StringType)
PERMIS.attributes={PERMIS_libPermis}

# CHAUFFEUR class attributes and methods
CHAUFFEUR_nomPersonnel: Property = Property(name="nomPersonnel", type=StringType)
CHAUFFEUR_prenomPersonnel: Property = Property(name="prenomPersonnel", type=StringType)
CHAUFFEUR.attributes={CHAUFFEUR_nomPersonnel, CHAUFFEUR_prenomPersonnel}

# RESERVATION class attributes and methods

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
C1_attC2: Property = Property(name="attC2", type=BooleanType)
C1_attC1: Property = Property(name="attC1", type=IntegerType)
C1.attributes={C1_attC1, C1_attC2}

# C11 class attributes and methods

# C2 class attributes and methods

# Relationships
CHAUFFEUR_PERMIS: BinaryAssociation = BinaryAssociation(
    name="CHAUFFEUR_PERMIS",
    ends={
        Property(name="pERMIS0", type=PERMIS, multiplicity=Multiplicity(1, 9999)),
        Property(name="cHAUFFEUR1", type=CHAUFFEUR, multiplicity=Multiplicity(0, 1))
    }
)
PERSONNEL_RESERVATION: BinaryAssociation = BinaryAssociation(
    name="PERSONNEL_RESERVATION",
    ends={
        Property(name="rESERVATION2", type=RESERVATION, multiplicity=Multiplicity(1, 9999)),
        Property(name="pERSONNEL3", type=PERSONNEL, multiplicity=Multiplicity(0, 1))
    }
)
CHAUFFEUR_RESERVATION: BinaryAssociation = BinaryAssociation(
    name="CHAUFFEUR_RESERVATION",
    ends={
        Property(name="rESERVATION4", type=RESERVATION, multiplicity=Multiplicity(0, 9999)),
        Property(name="cHAUFFEUR5", type=CHAUFFEUR, multiplicity=Multiplicity(1, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b6", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a7", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c8", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b9", type=B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_XhxOMPJXEei0SKJPiR2ViA",
    types={PERSONNEL, PERMIS, CHAUFFEUR, RESERVATION, A, B, C, Y, R, A1, Z, B1, C1, C11, C2},
    associations={CHAUFFEUR_PERMIS, PERSONNEL_RESERVATION, CHAUFFEUR_RESERVATION, A_B, B_C},
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
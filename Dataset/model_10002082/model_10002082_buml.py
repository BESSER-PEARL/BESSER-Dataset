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
Z = Class(name="Z")
R = Class(name="R")
C2 = Class(name="C2")
C3 = Class(name="C3")
Personne = Class(name="Personne")
Sport = Class(name="Sport")
Lieu = Class(name="Lieu")

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

# Z class attributes and methods

# R class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# Personne class attributes and methods
Personne_id: Property = Property(name="id", type=IntegerType)
Personne_nom: Property = Property(name="nom", type=StringType)
Personne_prenom: Property = Property(name="prenom", type=StringType)
Personne.attributes={Personne_prenom, Personne_nom, Personne_id}

# Sport class attributes and methods
Sport_id: Property = Property(name="id", type=IntegerType)
Sport_nom: Property = Property(name="nom", type=StringType)
Sport.attributes={Sport_id, Sport_nom}

# Lieu class attributes and methods

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
        Property(name="a2", type=A, multiplicity=Multiplicity(0, 9999)),
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
Personne_Sport: BinaryAssociation = BinaryAssociation(
    name="Personne_Sport",
    ends={
        Property(name="sport6", type=Sport, multiplicity=Multiplicity(0, 9999)),
        Property(name="personne7", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Lieu_Personne: BinaryAssociation = BinaryAssociation(
    name="Lieu_Personne",
    ends={
        Property(name="personne8", type=Personne, multiplicity=Multiplicity(0, 9999)),
        Property(name="lieu9", type=Lieu, multiplicity=Multiplicity(0, 9999))
    }
)
Sport_Lieu: BinaryAssociation = BinaryAssociation(
    name="Sport_Lieu",
    ends={
        Property(name="lieu10", type=Lieu, multiplicity=Multiplicity(0, 9999)),
        Property(name="sport11", type=Sport, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_nX1B8G_QEeSQQ4inw3dTxQ",
    types={A, B, C, Y, Z, R, C2, C3, Personne, Sport, Lieu},
    associations={B_C, R_A, A_B, Personne_Sport, Lieu_Personne, Sport_Lieu},
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
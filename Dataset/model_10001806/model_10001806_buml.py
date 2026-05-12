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
C = Class(name="C", is_abstract=True)
A = Class(name="A", is_abstract=True)
R = Class(name="R")
Y = Class(name="Y")
C2 = Class(name="C2")
C1 = Class(name="C1")
B = Class(name="B")
Z = Class(name="Z")
Client = Class(name="Client")
Chauffeur = Class(name="Chauffeur")
Groupe = Class(name="Groupe")
Reservation = Class(name="Reservation")
Permis = Class(name="Permis")
Vehicule = Class(name="Vehicule")
E = Class(name="E")
F = Class(name="F")
G = Class(name="G")

# C class attributes and methods
C_attc1: Property = Property(name="attc1", type=IntegerType)
C_attc2: Property = Property(name="attc2", type=BooleanType)
C.attributes={C_attc2, C_attc1}

# A class attributes and methods
A_atta: Property = Property(name="atta", type=StringType)
A.attributes={A_atta}

# R class attributes and methods

# Y class attributes and methods
Y_atty: Property = Property(name="atty", type=StringType)
Y.attributes={Y_atty}

# C2 class attributes and methods

# C1 class attributes and methods

# B class attributes and methods
B_attb: Property = Property(name="attb", type=StringType)
B.attributes={B_attb}

# Z class attributes and methods

# Client class attributes and methods
Client_fonction: Property = Property(name="fonction", type=StringType)
Client_nom: Property = Property(name="nom", type=StringType)
Client.attributes={Client_nom, Client_fonction}

# Chauffeur class attributes and methods
Chauffeur_position: Property = Property(name="position", type=StringType)
Chauffeur.attributes={Chauffeur_position}

# Groupe class attributes and methods
Groupe_rang: Property = Property(name="rang", type=StringType)
Groupe.attributes={Groupe_rang}

# Reservation class attributes and methods

# Permis class attributes and methods

# Vehicule class attributes and methods
Vehicule_rang: Property = Property(name="rang", type=IntegerType)
Vehicule_standing: Property = Property(name="standing", type=StringType)
Vehicule.attributes={Vehicule_standing, Vehicule_rang}

# E class attributes and methods
E_attE: Property = Property(name="attE", type=StringType)
E.attributes={E_attE}

# F class attributes and methods
F_attF: Property = Property(name="attF", type=StringType)
F.attributes={F_attF}

# G class attributes and methods

# Relationships
Groupe_Reservation: BinaryAssociation = BinaryAssociation(
    name="Groupe_Reservation",
    ends={
        Property(name="reservation8", type=Reservation, multiplicity=Multiplicity(0, 1)),
        Property(name="groupe9", type=Groupe, multiplicity=Multiplicity(0, 1))
    }
)
Chauffeur_Permis: BinaryAssociation = BinaryAssociation(
    name="Chauffeur_Permis",
    ends={
        Property(name="permis10", type=Permis, multiplicity=Multiplicity(0, 1)),
        Property(name="chauffeur11", type=Chauffeur, multiplicity=Multiplicity(0, 1))
    }
)
B__C: BinaryAssociation = BinaryAssociation(
    name="B__C",
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
Client_Groupe: BinaryAssociation = BinaryAssociation(
    name="Client_Groupe",
    ends={
        Property(name="groupe6", type=Groupe, multiplicity=Multiplicity(0, 9999)),
        Property(name="client7", type=Client, multiplicity=Multiplicity(0, 9999))
    }
)
Vehicule_Chauffeur: BinaryAssociation = BinaryAssociation(
    name="Vehicule_Chauffeur",
    ends={
        Property(name="chauffeur12", type=Chauffeur, multiplicity=Multiplicity(0, 1)),
        Property(name="vehicule13", type=Vehicule, multiplicity=Multiplicity(0, 1))
    }
)
Reservation_Vehicule: BinaryAssociation = BinaryAssociation(
    name="Reservation_Vehicule",
    ends={
        Property(name="vehicule14", type=Vehicule, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation15", type=Reservation, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass",
    ends={
        Property(name="e16", type=E, multiplicity=Multiplicity(0, 1)),
        Property(name="g17", type=G, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_X1iQ4MUeEeeWu_SLkciAbg",
    types={C, A, R, Y, C2, C1, B, Z, Client, Chauffeur, Groupe, Reservation, Permis, Vehicule, E, F, G},
    associations={Groupe_Reservation, Chauffeur_Permis, B__C, A_B, R_A, Client_Groupe, Vehicule_Chauffeur, Reservation_Vehicule, MyClass3_MyClass},
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
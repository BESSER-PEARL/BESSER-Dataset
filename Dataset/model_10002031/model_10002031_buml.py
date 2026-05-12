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
Employ_ = Class(name="Employ_")
administrateur = Class(name="administrateur")
salari_ = Class(name="salari_")
typeEmploy_ = Class(name="typeEmploy_")
Conge = Class(name="Conge")
typecong_ = Class(name="typecong_")
EtatConge = Class(name="EtatConge")
reduire = Class(name="reduire")
abs = Class(name="abs")
retard = Class(name="retard")

# Employ_ class attributes and methods
Employ__ID: Property = Property(name="ID", type=IntegerType)
Employ__nom: Property = Property(name="nom", type=StringType)
Employ__prenom: Property = Property(name="prenom", type=StringType)
Employ__poste: Property = Property(name="poste", type=StringType)
Employ__adresse: Property = Property(name="adresse", type=StringType)
Employ_.attributes={Employ__poste, Employ__nom, Employ__prenom, Employ__adresse, Employ__ID}

# administrateur class attributes and methods
administrateur_secteur: Property = Property(name="secteur", type=StringType)
administrateur.attributes={administrateur_secteur}

# salari_ class attributes and methods
salari__departement: Property = Property(name="departement", type=StringType)
salari_.attributes={salari__departement}

# typeEmploy_ class attributes and methods
typeEmploy__id: Property = Property(name="id", type=StringType)
typeEmploy_.attributes={typeEmploy__id}

# Conge class attributes and methods
Conge_id: Property = Property(name="id", type=IntegerType)
Conge_datedebut: Property = Property(name="datedebut", type=StringType)
Conge_datefin: Property = Property(name="datefin", type=StringType)
Conge_adresse: Property = Property(name="adresse", type=StringType)
Conge.attributes={Conge_datefin, Conge_adresse, Conge_datedebut, Conge_id}

# typecong_ class attributes and methods
typecong__idconge: Property = Property(name="idconge", type=IntegerType)
typecong_.attributes={typecong__idconge}

# EtatConge class attributes and methods
EtatConge_idEtat: Property = Property(name="idEtat", type=IntegerType)
EtatConge_nom: Property = Property(name="nom", type=StringType)
EtatConge.attributes={EtatConge_nom, EtatConge_idEtat}

# reduire class attributes and methods

# abs class attributes and methods
abs_idab: Property = Property(name="idab", type=IntegerType)
abs_nbrjr: Property = Property(name="nbrjr", type=IntegerType)
abs_motif: Property = Property(name="motif", type=StringType)
abs.attributes={abs_motif, abs_idab, abs_nbrjr}

# retard class attributes and methods
retard_motif: Property = Property(name="motif", type=StringType)
retard_idretad: Property = Property(name="idretad", type=IntegerType)
retard_nbrminute: Property = Property(name="nbrminute", type=IntegerType)
retard.attributes={retard_motif, retard_nbrminute, retard_idretad}

# Relationships
Employ__typeEmploy_: BinaryAssociation = BinaryAssociation(
    name="Employ__typeEmploy_",
    ends={
        Property(name="typeEmploy_0", type=typeEmploy_, multiplicity=Multiplicity(1, 1)),
        Property(name="employ_1", type=Employ_, multiplicity=Multiplicity(0, 9999))
    }
)
Employ__Conge: BinaryAssociation = BinaryAssociation(
    name="Employ__Conge",
    ends={
        Property(name="conge2", type=Conge, multiplicity=Multiplicity(0, 1)),
        Property(name="employ_3", type=Employ_, multiplicity=Multiplicity(0, 9999))
    }
)
salari__Conge: BinaryAssociation = BinaryAssociation(
    name="salari__Conge",
    ends={
        Property(name="conge4", type=Conge, multiplicity=Multiplicity(0, 1)),
        Property(name="salari_5", type=salari_, multiplicity=Multiplicity(0, 9999))
    }
)
Conge_typecong_: BinaryAssociation = BinaryAssociation(
    name="Conge_typecong_",
    ends={
        Property(name="typecong_6", type=typecong_, multiplicity=Multiplicity(0, 1)),
        Property(name="conge7", type=Conge, multiplicity=Multiplicity(0, 9999))
    }
)
Conge_EtatConge: BinaryAssociation = BinaryAssociation(
    name="Conge_EtatConge",
    ends={
        Property(name="etatConge8", type=EtatConge, multiplicity=Multiplicity(0, 1)),
        Property(name="conge9", type=Conge, multiplicity=Multiplicity(0, 9999))
    }
)
abs_Employ_: BinaryAssociation = BinaryAssociation(
    name="abs_Employ_",
    ends={
        Property(name="employ_10", type=Employ_, multiplicity=Multiplicity(0, 1)),
        Property(name="abs11", type=abs, multiplicity=Multiplicity(0, 9999))
    }
)
retard_Employ_: BinaryAssociation = BinaryAssociation(
    name="retard_Employ_",
    ends={
        Property(name="employ_12", type=Employ_, multiplicity=Multiplicity(0, 1)),
        Property(name="retard13", type=retard, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kivRELy_EeedTfUoC_GfaA",
    types={Employ_, administrateur, salari_, typeEmploy_, Conge, typecong_, EtatConge, reduire, abs, retard},
    associations={Employ__typeEmploy_, Employ__Conge, salari__Conge, Conge_typecong_, Conge_EtatConge, abs_Employ_, retard_Employ_},
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
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
droneDSL_Model = Class(name="droneDSL::Model")
droneDSL_Import = Class(name="droneDSL::Import")
droneDSL_Prologue = Class(name="droneDSL::Prologue")
droneDSL_Main = Class(name="droneDSL::Main")
droneDSL_FonctionDecl = Class(name="droneDSL::FonctionDecl")
droneDSL_Pourcent_vitesse_hauteur_max = Class(name="droneDSL::Pourcent::vitesse::hauteur::max")
droneDSL_PourcentConst = Class(name="droneDSL::PourcentConst")
droneDSL_Pourcent_vitesse_deplacement_max = Class(name="droneDSL::Pourcent::vitesse::deplacement::max")
droneDSL_Pourcent_vitesse_rotation_max = Class(name="droneDSL::Pourcent::vitesse::rotation::max")
droneDSL_Hauteur_max = Class(name="droneDSL::Hauteur::max")
droneDSL_SecondeConst = Class(name="droneDSL::SecondeConst")
droneDSL_Eloignement_max = Class(name="droneDSL::Eloignement::max")
SecondeExp = Class(name="SecondeExp")
PourcentExp = Class(name="PourcentExp")
droneDSL_SecondeDecl = Class(name="droneDSL::SecondeDecl")
VarDecl = Class(name="VarDecl")
droneDSL_PourcentDecl = Class(name="droneDSL::PourcentDecl")
droneDSL_VarDecl = Class(name="droneDSL::VarDecl")
droneDSL_RefSecondeVar = Class(name="droneDSL::RefSecondeVar")
droneDSL_RefPourcentVar = Class(name="droneDSL::RefPourcentVar")
droneDSL_PourcentExp = Class(name="droneDSL::PourcentExp")
droneDSL_SecondeExp = Class(name="droneDSL::SecondeExp")
droneDSL_Decoller = Class(name="droneDSL::Decoller")
DecollerAtterrir = Class(name="DecollerAtterrir")
droneDSL_Atterrir = Class(name="droneDSL::Atterrir")
droneDSL_Monter = Class(name="droneDSL::Monter")
Mouvement = Class(name="Mouvement")
CommandeBasique = Class(name="CommandeBasique")
MD = Class(name="MD")
droneDSL_Descendre = Class(name="droneDSL::Descendre")
droneDSL_Avancer = Class(name="droneDSL::Avancer")
AR = Class(name="AR")
droneDSL_Reculer = Class(name="droneDSL::Reculer")
droneDSL_Gauche = Class(name="droneDSL::Gauche")
GDr = Class(name="GDr")
droneDSL_Droite = Class(name="droneDSL::Droite")
droneDSL_RotationGauche = Class(name="droneDSL::RotationGauche")
RGRD = Class(name="RGRD")
droneDSL_RotationDroite = Class(name="droneDSL::RotationDroite")
droneDSL_Pause = Class(name="droneDSL::Pause")
droneDSL_Mouvement = Class(name="droneDSL::Mouvement")
droneDSL_DecollerAtterrir = Class(name="droneDSL::DecollerAtterrir")
droneDSL_CommandeBasique = Class(name="droneDSL::CommandeBasique")
droneDSL_EObject = Class(name="droneDSL::EObject")
droneDSL_FinDeMain = Class(name="droneDSL::FinDeMain")
droneDSL_FonctionCall = Class(name="droneDSL::FonctionCall")
droneDSL_FonctionCallInterne = Class(name="droneDSL::FonctionCallInterne")
FonctionCall = Class(name="FonctionCall")
droneDSL_FonctionCallExterne = Class(name="droneDSL::FonctionCallExterne")
droneDSL_MD = Class(name="droneDSL::MD")
droneDSL_GDr = Class(name="droneDSL::GDr")
droneDSL_RGRD = Class(name="droneDSL::RGRD")
droneDSL_AR = Class(name="droneDSL::AR")
droneDSL_Parallele = Class(name="droneDSL::Parallele")
droneDSL_Parallele2 = Class(name="droneDSL::Parallele2")
Parallele = Class(name="Parallele")
droneDSL_Parallele3 = Class(name="droneDSL::Parallele3")
droneDSL_Parallele4 = Class(name="droneDSL::Parallele4")

# droneDSL_Model class attributes and methods

# droneDSL_Import class attributes and methods
droneDSL_Import_name: Property = Property(name="name", type=StringType)
droneDSL_Import.attributes={droneDSL_Import_name}

# droneDSL_Prologue class attributes and methods

# droneDSL_Main class attributes and methods

# droneDSL_FonctionDecl class attributes and methods
droneDSL_FonctionDecl_name: Property = Property(name="name", type=StringType)
droneDSL_FonctionDecl.attributes={droneDSL_FonctionDecl_name}

# droneDSL_Pourcent_vitesse_hauteur_max class attributes and methods

# droneDSL_PourcentConst class attributes and methods
droneDSL_PourcentConst_val: Property = Property(name="val", type=StringType)
droneDSL_PourcentConst.attributes={droneDSL_PourcentConst_val}

# droneDSL_Pourcent_vitesse_deplacement_max class attributes and methods

# droneDSL_Pourcent_vitesse_rotation_max class attributes and methods

# droneDSL_Hauteur_max class attributes and methods

# droneDSL_SecondeConst class attributes and methods
droneDSL_SecondeConst_val: Property = Property(name="val", type=StringType)
droneDSL_SecondeConst.attributes={droneDSL_SecondeConst_val}

# droneDSL_Eloignement_max class attributes and methods

# SecondeExp class attributes and methods

# PourcentExp class attributes and methods

# droneDSL_SecondeDecl class attributes and methods

# VarDecl class attributes and methods

# droneDSL_PourcentDecl class attributes and methods

# droneDSL_VarDecl class attributes and methods
droneDSL_VarDecl_name: Property = Property(name="name", type=StringType)
droneDSL_VarDecl.attributes={droneDSL_VarDecl_name}

# droneDSL_RefSecondeVar class attributes and methods

# droneDSL_RefPourcentVar class attributes and methods

# droneDSL_PourcentExp class attributes and methods

# droneDSL_SecondeExp class attributes and methods

# droneDSL_Decoller class attributes and methods

# DecollerAtterrir class attributes and methods

# droneDSL_Atterrir class attributes and methods

# droneDSL_Monter class attributes and methods

# Mouvement class attributes and methods

# CommandeBasique class attributes and methods

# MD class attributes and methods

# droneDSL_Descendre class attributes and methods

# droneDSL_Avancer class attributes and methods

# AR class attributes and methods

# droneDSL_Reculer class attributes and methods

# droneDSL_Gauche class attributes and methods

# GDr class attributes and methods

# droneDSL_Droite class attributes and methods

# droneDSL_RotationGauche class attributes and methods

# RGRD class attributes and methods

# droneDSL_RotationDroite class attributes and methods

# droneDSL_Pause class attributes and methods

# droneDSL_Mouvement class attributes and methods

# droneDSL_DecollerAtterrir class attributes and methods
droneDSL_DecollerAtterrir_str: Property = Property(name="str", type=StringType)
droneDSL_DecollerAtterrir.attributes={droneDSL_DecollerAtterrir_str}

# droneDSL_CommandeBasique class attributes and methods

# droneDSL_EObject class attributes and methods

# droneDSL_FinDeMain class attributes and methods
droneDSL_FinDeMain_accolade: Property = Property(name="accolade", type=StringType)
droneDSL_FinDeMain.attributes={droneDSL_FinDeMain_accolade}

# droneDSL_FonctionCall class attributes and methods

# droneDSL_FonctionCallInterne class attributes and methods

# FonctionCall class attributes and methods

# droneDSL_FonctionCallExterne class attributes and methods
droneDSL_FonctionCallExterne_name: Property = Property(name="name", type=StringType)
droneDSL_FonctionCallExterne.attributes={droneDSL_FonctionCallExterne_name}

# droneDSL_MD class attributes and methods

# droneDSL_GDr class attributes and methods

# droneDSL_RGRD class attributes and methods

# droneDSL_AR class attributes and methods

# droneDSL_Parallele class attributes and methods

# droneDSL_Parallele2 class attributes and methods

# Parallele class attributes and methods

# droneDSL_Parallele3 class attributes and methods

# droneDSL_Parallele4 class attributes and methods

# Relationships
eloignement27: BinaryAssociation = BinaryAssociation(
    name="eloignement27",
    ends={
        Property(name="droneDSL_Eloignement_max29", type=droneDSL_Prologue, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Prologue28", type=droneDSL_Eloignement_max, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="droneDSL_Import", type=droneDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Model", type=droneDSL_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prologue1: BinaryAssociation = BinaryAssociation(
    name="prologue1",
    ends={
        Property(name="droneDSL_Prologue", type=droneDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Model2", type=droneDSL_Prologue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
m3: BinaryAssociation = BinaryAssociation(
    name="m3",
    ends={
        Property(name="droneDSL_Main", type=droneDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Model4", type=droneDSL_Main, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fonctions5: BinaryAssociation = BinaryAssociation(
    name="fonctions5",
    ends={
        Property(name="droneDSL_FonctionDecl", type=droneDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Model6", type=droneDSL_FonctionDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vitesse_verticale7: BinaryAssociation = BinaryAssociation(
    name="vitesse_verticale7",
    ends={
        Property(name="droneDSL_PourcentConst", type=droneDSL_Pourcent_vitesse_hauteur_max, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Pourcent_vitesse_hauteur_max", type=droneDSL_PourcentConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse_deplacement8: BinaryAssociation = BinaryAssociation(
    name="vitesse_deplacement8",
    ends={
        Property(name="droneDSL_PourcentConst9", type=droneDSL_Pourcent_vitesse_deplacement_max, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Pourcent_vitesse_deplacement_max", type=droneDSL_PourcentConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse_rotation10: BinaryAssociation = BinaryAssociation(
    name="vitesse_rotation10",
    ends={
        Property(name="droneDSL_PourcentConst11", type=droneDSL_Pourcent_vitesse_rotation_max, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Pourcent_vitesse_rotation_max", type=droneDSL_PourcentConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hauteur_max12: BinaryAssociation = BinaryAssociation(
    name="hauteur_max12",
    ends={
        Property(name="droneDSL_SecondeConst", type=droneDSL_Hauteur_max, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Hauteur_max", type=droneDSL_SecondeConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eloignement_max13: BinaryAssociation = BinaryAssociation(
    name="eloignement_max13",
    ends={
        Property(name="droneDSL_SecondeConst14", type=droneDSL_Eloignement_max, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Eloignement_max", type=droneDSL_SecondeConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse_verticale15: BinaryAssociation = BinaryAssociation(
    name="vitesse_verticale15",
    ends={
        Property(name="droneDSL_Pourcent_vitesse_hauteur_max17", type=droneDSL_Prologue, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Prologue16", type=droneDSL_Pourcent_vitesse_hauteur_max, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse_deplacement18: BinaryAssociation = BinaryAssociation(
    name="vitesse_deplacement18",
    ends={
        Property(name="droneDSL_Pourcent_vitesse_deplacement_max20", type=droneDSL_Prologue, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Prologue19", type=droneDSL_Pourcent_vitesse_deplacement_max, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse_rotation21: BinaryAssociation = BinaryAssociation(
    name="vitesse_rotation21",
    ends={
        Property(name="droneDSL_Pourcent_vitesse_rotation_max23", type=droneDSL_Prologue, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Prologue22", type=droneDSL_Pourcent_vitesse_rotation_max, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hauteur24: BinaryAssociation = BinaryAssociation(
    name="hauteur24",
    ends={
        Property(name="droneDSL_Hauteur_max26", type=droneDSL_Prologue, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Prologue25", type=droneDSL_Hauteur_max, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse48: BinaryAssociation = BinaryAssociation(
    name="vitesse48",
    ends={
        Property(name="droneDSL_PourcentExp50", type=droneDSL_Avancer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Avancer49", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val30: BinaryAssociation = BinaryAssociation(
    name="val30",
    ends={
        Property(name="droneDSL_SecondeConst31", type=droneDSL_SecondeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_SecondeDecl", type=droneDSL_SecondeConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val32: BinaryAssociation = BinaryAssociation(
    name="val32",
    ends={
        Property(name="droneDSL_PourcentConst33", type=droneDSL_PourcentDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_PourcentDecl", type=droneDSL_PourcentConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var34: BinaryAssociation = BinaryAssociation(
    name="var34",
    ends={
        Property(name="droneDSL_SecondeDecl35", type=droneDSL_RefSecondeVar, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_RefSecondeVar", type=droneDSL_SecondeDecl, multiplicity=Multiplicity(0, 1))
    }
)
var36: BinaryAssociation = BinaryAssociation(
    name="var36",
    ends={
        Property(name="droneDSL_PourcentDecl37", type=droneDSL_RefPourcentVar, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_RefPourcentVar", type=droneDSL_PourcentDecl, multiplicity=Multiplicity(0, 1))
    }
)
duree38: BinaryAssociation = BinaryAssociation(
    name="duree38",
    ends={
        Property(name="droneDSL_SecondeExp", type=droneDSL_Monter, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Monter", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse39: BinaryAssociation = BinaryAssociation(
    name="vitesse39",
    ends={
        Property(name="droneDSL_PourcentExp", type=droneDSL_Monter, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Monter40", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree41: BinaryAssociation = BinaryAssociation(
    name="duree41",
    ends={
        Property(name="droneDSL_SecondeExp42", type=droneDSL_Descendre, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Descendre", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse43: BinaryAssociation = BinaryAssociation(
    name="vitesse43",
    ends={
        Property(name="droneDSL_PourcentExp45", type=droneDSL_Descendre, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Descendre44", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree46: BinaryAssociation = BinaryAssociation(
    name="duree46",
    ends={
        Property(name="droneDSL_SecondeExp47", type=droneDSL_Avancer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Avancer", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree51: BinaryAssociation = BinaryAssociation(
    name="duree51",
    ends={
        Property(name="droneDSL_SecondeExp52", type=droneDSL_Reculer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Reculer", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse53: BinaryAssociation = BinaryAssociation(
    name="vitesse53",
    ends={
        Property(name="droneDSL_PourcentExp55", type=droneDSL_Reculer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Reculer54", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree56: BinaryAssociation = BinaryAssociation(
    name="duree56",
    ends={
        Property(name="droneDSL_SecondeExp57", type=droneDSL_Gauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Gauche", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse58: BinaryAssociation = BinaryAssociation(
    name="vitesse58",
    ends={
        Property(name="droneDSL_PourcentExp60", type=droneDSL_Gauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Gauche59", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree61: BinaryAssociation = BinaryAssociation(
    name="duree61",
    ends={
        Property(name="droneDSL_SecondeExp62", type=droneDSL_Droite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Droite", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse63: BinaryAssociation = BinaryAssociation(
    name="vitesse63",
    ends={
        Property(name="droneDSL_PourcentExp65", type=droneDSL_Droite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Droite64", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree66: BinaryAssociation = BinaryAssociation(
    name="duree66",
    ends={
        Property(name="droneDSL_SecondeExp67", type=droneDSL_RotationGauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_RotationGauche", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse68: BinaryAssociation = BinaryAssociation(
    name="vitesse68",
    ends={
        Property(name="droneDSL_PourcentExp70", type=droneDSL_RotationGauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_RotationGauche69", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree71: BinaryAssociation = BinaryAssociation(
    name="duree71",
    ends={
        Property(name="droneDSL_SecondeExp72", type=droneDSL_RotationDroite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_RotationDroite", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse73: BinaryAssociation = BinaryAssociation(
    name="vitesse73",
    ends={
        Property(name="droneDSL_PourcentExp75", type=droneDSL_RotationDroite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_RotationDroite74", type=droneDSL_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree76: BinaryAssociation = BinaryAssociation(
    name="duree76",
    ends={
        Property(name="droneDSL_SecondeExp77", type=droneDSL_Pause, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Pause", type=droneDSL_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d104: BinaryAssociation = BinaryAssociation(
    name="d104",
    ends={
        Property(name="droneDSL_EObject106", type=droneDSL_Parallele4, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Parallele4105", type=droneDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body78: BinaryAssociation = BinaryAssociation(
    name="body78",
    ends={
        Property(name="droneDSL_EObject", type=droneDSL_FonctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_FonctionDecl79", type=droneDSL_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref80: BinaryAssociation = BinaryAssociation(
    name="ref80",
    ends={
        Property(name="droneDSL_FonctionDecl81", type=droneDSL_FonctionCallInterne, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_FonctionCallInterne", type=droneDSL_FonctionDecl, multiplicity=Multiplicity(0, 1))
    }
)
file82: BinaryAssociation = BinaryAssociation(
    name="file82",
    ends={
        Property(name="droneDSL_Import83", type=droneDSL_FonctionCallExterne, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_FonctionCallExterne", type=droneDSL_Import, multiplicity=Multiplicity(0, 1))
    }
)
decollage84: BinaryAssociation = BinaryAssociation(
    name="decollage84",
    ends={
        Property(name="droneDSL_Decoller", type=droneDSL_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Main85", type=droneDSL_Decoller, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mainbody86: BinaryAssociation = BinaryAssociation(
    name="mainbody86",
    ends={
        Property(name="droneDSL_EObject88", type=droneDSL_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Main87", type=droneDSL_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atterrissage89: BinaryAssociation = BinaryAssociation(
    name="atterrissage89",
    ends={
        Property(name="droneDSL_Atterrir", type=droneDSL_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Main90", type=droneDSL_Atterrir, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fdm91: BinaryAssociation = BinaryAssociation(
    name="fdm91",
    ends={
        Property(name="droneDSL_FinDeMain", type=droneDSL_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Main92", type=droneDSL_FinDeMain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a93: BinaryAssociation = BinaryAssociation(
    name="a93",
    ends={
        Property(name="droneDSL_EObject94", type=droneDSL_Parallele, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Parallele", type=droneDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b95: BinaryAssociation = BinaryAssociation(
    name="b95",
    ends={
        Property(name="droneDSL_EObject97", type=droneDSL_Parallele, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Parallele96", type=droneDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t98: BinaryAssociation = BinaryAssociation(
    name="t98",
    ends={
        Property(name="droneDSL_EObject99", type=droneDSL_Parallele2, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Parallele2", type=droneDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c100: BinaryAssociation = BinaryAssociation(
    name="c100",
    ends={
        Property(name="droneDSL_EObject101", type=droneDSL_Parallele3, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Parallele3", type=droneDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c102: BinaryAssociation = BinaryAssociation(
    name="c102",
    ends={
        Property(name="droneDSL_EObject103", type=droneDSL_Parallele4, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSL_Parallele4", type=droneDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_droneDSL_SecondeConst_SecondeExp = Generalization(general=SecondeExp, specific=droneDSL_SecondeConst)
gen_droneDSL_PourcentConst_PourcentExp = Generalization(general=PourcentExp, specific=droneDSL_PourcentConst)
gen_droneDSL_SecondeDecl_VarDecl = Generalization(general=VarDecl, specific=droneDSL_SecondeDecl)
gen_droneDSL_PourcentDecl_VarDecl = Generalization(general=VarDecl, specific=droneDSL_PourcentDecl)
gen_droneDSL_RefSecondeVar_SecondeExp = Generalization(general=SecondeExp, specific=droneDSL_RefSecondeVar)
gen_droneDSL_RefPourcentVar_PourcentExp = Generalization(general=PourcentExp, specific=droneDSL_RefPourcentVar)
gen_droneDSL_Decoller_DecollerAtterrir = Generalization(general=DecollerAtterrir, specific=droneDSL_Decoller)
gen_droneDSL_Atterrir_DecollerAtterrir = Generalization(general=DecollerAtterrir, specific=droneDSL_Atterrir)
gen_droneDSL_Monter_Mouvement = Generalization(general=Mouvement, specific=droneDSL_Monter)
gen_droneDSL_Monter_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_Monter)
gen_droneDSL_Monter_MD = Generalization(general=MD, specific=droneDSL_Monter)
gen_droneDSL_Descendre_Mouvement = Generalization(general=Mouvement, specific=droneDSL_Descendre)
gen_droneDSL_Descendre_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_Descendre)
gen_droneDSL_Descendre_MD = Generalization(general=MD, specific=droneDSL_Descendre)
gen_droneDSL_Avancer_Mouvement = Generalization(general=Mouvement, specific=droneDSL_Avancer)
gen_droneDSL_Avancer_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_Avancer)
gen_droneDSL_Avancer_AR = Generalization(general=AR, specific=droneDSL_Avancer)
gen_droneDSL_Reculer_Mouvement = Generalization(general=Mouvement, specific=droneDSL_Reculer)
gen_droneDSL_Reculer_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_Reculer)
gen_droneDSL_Reculer_AR = Generalization(general=AR, specific=droneDSL_Reculer)
gen_droneDSL_Gauche_Mouvement = Generalization(general=Mouvement, specific=droneDSL_Gauche)
gen_droneDSL_Gauche_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_Gauche)
gen_droneDSL_Gauche_GDr = Generalization(general=GDr, specific=droneDSL_Gauche)
gen_droneDSL_Droite_Mouvement = Generalization(general=Mouvement, specific=droneDSL_Droite)
gen_droneDSL_Droite_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_Droite)
gen_droneDSL_Droite_GDr = Generalization(general=GDr, specific=droneDSL_Droite)
gen_droneDSL_RotationGauche_Mouvement = Generalization(general=Mouvement, specific=droneDSL_RotationGauche)
gen_droneDSL_RotationGauche_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_RotationGauche)
gen_droneDSL_RotationGauche_RGRD = Generalization(general=RGRD, specific=droneDSL_RotationGauche)
gen_droneDSL_RotationDroite_Mouvement = Generalization(general=Mouvement, specific=droneDSL_RotationDroite)
gen_droneDSL_RotationDroite_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_RotationDroite)
gen_droneDSL_RotationDroite_RGRD = Generalization(general=RGRD, specific=droneDSL_RotationDroite)
gen_droneDSL_Pause_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSL_Pause)
gen_droneDSL_FonctionCallInterne_FonctionCall = Generalization(general=FonctionCall, specific=droneDSL_FonctionCallInterne)
gen_droneDSL_FonctionCallExterne_FonctionCall = Generalization(general=FonctionCall, specific=droneDSL_FonctionCallExterne)
gen_droneDSL_Parallele_Mouvement = Generalization(general=Mouvement, specific=droneDSL_Parallele)
gen_droneDSL_Parallele2_Parallele = Generalization(general=Parallele, specific=droneDSL_Parallele2)
gen_droneDSL_Parallele3_Parallele = Generalization(general=Parallele, specific=droneDSL_Parallele3)
gen_droneDSL_Parallele4_Parallele = Generalization(general=Parallele, specific=droneDSL_Parallele4)

# Domain Model
domain_model = DomainModel(
    name="droneDSL",
    types={droneDSL_Model, droneDSL_Import, droneDSL_Prologue, droneDSL_Main, droneDSL_FonctionDecl, droneDSL_Pourcent_vitesse_hauteur_max, droneDSL_PourcentConst, droneDSL_Pourcent_vitesse_deplacement_max, droneDSL_Pourcent_vitesse_rotation_max, droneDSL_Hauteur_max, droneDSL_SecondeConst, droneDSL_Eloignement_max, SecondeExp, PourcentExp, droneDSL_SecondeDecl, VarDecl, droneDSL_PourcentDecl, droneDSL_VarDecl, droneDSL_RefSecondeVar, droneDSL_RefPourcentVar, droneDSL_PourcentExp, droneDSL_SecondeExp, droneDSL_Decoller, DecollerAtterrir, droneDSL_Atterrir, droneDSL_Monter, Mouvement, CommandeBasique, MD, droneDSL_Descendre, droneDSL_Avancer, AR, droneDSL_Reculer, droneDSL_Gauche, GDr, droneDSL_Droite, droneDSL_RotationGauche, RGRD, droneDSL_RotationDroite, droneDSL_Pause, droneDSL_Mouvement, droneDSL_DecollerAtterrir, droneDSL_CommandeBasique, droneDSL_EObject, droneDSL_FinDeMain, droneDSL_FonctionCall, droneDSL_FonctionCallInterne, FonctionCall, droneDSL_FonctionCallExterne, droneDSL_MD, droneDSL_GDr, droneDSL_RGRD, droneDSL_AR, droneDSL_Parallele, droneDSL_Parallele2, Parallele, droneDSL_Parallele3, droneDSL_Parallele4},
    associations={eloignement27, imports0, prologue1, m3, fonctions5, vitesse_verticale7, vitesse_deplacement8, vitesse_rotation10, hauteur_max12, eloignement_max13, vitesse_verticale15, vitesse_deplacement18, vitesse_rotation21, hauteur24, vitesse48, val30, val32, var34, var36, duree38, vitesse39, duree41, vitesse43, duree46, duree51, vitesse53, duree56, vitesse58, duree61, vitesse63, duree66, vitesse68, duree71, vitesse73, duree76, d104, body78, ref80, file82, decollage84, mainbody86, atterrissage89, fdm91, a93, b95, t98, c100, c102},
    generalizations={gen_droneDSL_SecondeConst_SecondeExp, gen_droneDSL_PourcentConst_PourcentExp, gen_droneDSL_SecondeDecl_VarDecl, gen_droneDSL_PourcentDecl_VarDecl, gen_droneDSL_RefSecondeVar_SecondeExp, gen_droneDSL_RefPourcentVar_PourcentExp, gen_droneDSL_Decoller_DecollerAtterrir, gen_droneDSL_Atterrir_DecollerAtterrir, gen_droneDSL_Monter_Mouvement, gen_droneDSL_Monter_CommandeBasique, gen_droneDSL_Monter_MD, gen_droneDSL_Descendre_Mouvement, gen_droneDSL_Descendre_CommandeBasique, gen_droneDSL_Descendre_MD, gen_droneDSL_Avancer_Mouvement, gen_droneDSL_Avancer_CommandeBasique, gen_droneDSL_Avancer_AR, gen_droneDSL_Reculer_Mouvement, gen_droneDSL_Reculer_CommandeBasique, gen_droneDSL_Reculer_AR, gen_droneDSL_Gauche_Mouvement, gen_droneDSL_Gauche_CommandeBasique, gen_droneDSL_Gauche_GDr, gen_droneDSL_Droite_Mouvement, gen_droneDSL_Droite_CommandeBasique, gen_droneDSL_Droite_GDr, gen_droneDSL_RotationGauche_Mouvement, gen_droneDSL_RotationGauche_CommandeBasique, gen_droneDSL_RotationGauche_RGRD, gen_droneDSL_RotationDroite_Mouvement, gen_droneDSL_RotationDroite_CommandeBasique, gen_droneDSL_RotationDroite_RGRD, gen_droneDSL_Pause_CommandeBasique, gen_droneDSL_FonctionCallInterne_FonctionCall, gen_droneDSL_FonctionCallExterne_FonctionCall, gen_droneDSL_Parallele_Mouvement, gen_droneDSL_Parallele2_Parallele, gen_droneDSL_Parallele3_Parallele, gen_droneDSL_Parallele4_Parallele},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
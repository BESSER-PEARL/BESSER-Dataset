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
droneDSLLib_Model = Class(name="droneDSLLib::Model")
droneDSLLib_FonctionDecl = Class(name="droneDSLLib::FonctionDecl")
droneDSLLib_SecondeConst = Class(name="droneDSLLib::SecondeConst")
SecondeExp = Class(name="SecondeExp")
droneDSLLib_PourcentConst = Class(name="droneDSLLib::PourcentConst")
PourcentExp = Class(name="PourcentExp")
droneDSLLib_VarDecl = Class(name="droneDSLLib::VarDecl")
droneDSLLib_RefSecondeVar = Class(name="droneDSLLib::RefSecondeVar")
droneDSLLib_RefPourcentVar = Class(name="droneDSLLib::RefPourcentVar")
droneDSLLib_PourcentExp = Class(name="droneDSLLib::PourcentExp")
droneDSLLib_SecondeExp = Class(name="droneDSLLib::SecondeExp")
droneDSLLib_Decoller = Class(name="droneDSLLib::Decoller")
DecollerAtterrir = Class(name="DecollerAtterrir")
droneDSLLib_Atterrir = Class(name="droneDSLLib::Atterrir")
droneDSLLib_Monter = Class(name="droneDSLLib::Monter")
Mouvement = Class(name="Mouvement")
CommandeBasique = Class(name="CommandeBasique")
MD = Class(name="MD")
droneDSLLib_Descendre = Class(name="droneDSLLib::Descendre")
droneDSLLib_Avancer = Class(name="droneDSLLib::Avancer")
AR = Class(name="AR")
droneDSLLib_SecondeDecl = Class(name="droneDSLLib::SecondeDecl")
VarDecl = Class(name="VarDecl")
droneDSLLib_PourcentDecl = Class(name="droneDSLLib::PourcentDecl")
droneDSLLib_Gauche = Class(name="droneDSLLib::Gauche")
GDr = Class(name="GDr")
droneDSLLib_Droite = Class(name="droneDSLLib::Droite")
droneDSLLib_RotationGauche = Class(name="droneDSLLib::RotationGauche")
RGRD = Class(name="RGRD")
droneDSLLib_RotationDroite = Class(name="droneDSLLib::RotationDroite")
droneDSLLib_Pause = Class(name="droneDSLLib::Pause")
droneDSLLib_Reculer = Class(name="droneDSLLib::Reculer")
droneDSLLib_EObject = Class(name="droneDSLLib::EObject")
droneDSLLib_FonctionCall = Class(name="droneDSLLib::FonctionCall")
droneDSLLib_FonctionCallInterne = Class(name="droneDSLLib::FonctionCallInterne")
FonctionCall = Class(name="FonctionCall")
droneDSLLib_MD = Class(name="droneDSLLib::MD")
droneDSLLib_GDr = Class(name="droneDSLLib::GDr")
droneDSLLib_RGRD = Class(name="droneDSLLib::RGRD")
droneDSLLib_AR = Class(name="droneDSLLib::AR")
droneDSLLib_Parallele = Class(name="droneDSLLib::Parallele")
droneDSLLib_Parallele2 = Class(name="droneDSLLib::Parallele2")
Parallele = Class(name="Parallele")
droneDSLLib_Parallele3 = Class(name="droneDSLLib::Parallele3")
droneDSLLib_Parallele4 = Class(name="droneDSLLib::Parallele4")
droneDSLLib_Mouvement = Class(name="droneDSLLib::Mouvement")
droneDSLLib_DecollerAtterrir = Class(name="droneDSLLib::DecollerAtterrir")
droneDSLLib_CommandeBasique = Class(name="droneDSLLib::CommandeBasique")

# droneDSLLib_Model class attributes and methods

# droneDSLLib_FonctionDecl class attributes and methods
droneDSLLib_FonctionDecl_name: Property = Property(name="name", type=StringType)
droneDSLLib_FonctionDecl.attributes={droneDSLLib_FonctionDecl_name}

# droneDSLLib_SecondeConst class attributes and methods
droneDSLLib_SecondeConst_val: Property = Property(name="val", type=StringType)
droneDSLLib_SecondeConst.attributes={droneDSLLib_SecondeConst_val}

# SecondeExp class attributes and methods

# droneDSLLib_PourcentConst class attributes and methods
droneDSLLib_PourcentConst_val: Property = Property(name="val", type=StringType)
droneDSLLib_PourcentConst.attributes={droneDSLLib_PourcentConst_val}

# PourcentExp class attributes and methods

# droneDSLLib_VarDecl class attributes and methods
droneDSLLib_VarDecl_name: Property = Property(name="name", type=StringType)
droneDSLLib_VarDecl.attributes={droneDSLLib_VarDecl_name}

# droneDSLLib_RefSecondeVar class attributes and methods

# droneDSLLib_RefPourcentVar class attributes and methods

# droneDSLLib_PourcentExp class attributes and methods

# droneDSLLib_SecondeExp class attributes and methods

# droneDSLLib_Decoller class attributes and methods

# DecollerAtterrir class attributes and methods

# droneDSLLib_Atterrir class attributes and methods

# droneDSLLib_Monter class attributes and methods

# Mouvement class attributes and methods

# CommandeBasique class attributes and methods

# MD class attributes and methods

# droneDSLLib_Descendre class attributes and methods

# droneDSLLib_Avancer class attributes and methods

# AR class attributes and methods

# droneDSLLib_SecondeDecl class attributes and methods

# VarDecl class attributes and methods

# droneDSLLib_PourcentDecl class attributes and methods

# droneDSLLib_Gauche class attributes and methods

# GDr class attributes and methods

# droneDSLLib_Droite class attributes and methods

# droneDSLLib_RotationGauche class attributes and methods

# RGRD class attributes and methods

# droneDSLLib_RotationDroite class attributes and methods

# droneDSLLib_Pause class attributes and methods

# droneDSLLib_Reculer class attributes and methods

# droneDSLLib_EObject class attributes and methods

# droneDSLLib_FonctionCall class attributes and methods

# droneDSLLib_FonctionCallInterne class attributes and methods

# FonctionCall class attributes and methods

# droneDSLLib_MD class attributes and methods

# droneDSLLib_GDr class attributes and methods

# droneDSLLib_RGRD class attributes and methods

# droneDSLLib_AR class attributes and methods

# droneDSLLib_Parallele class attributes and methods

# droneDSLLib_Parallele2 class attributes and methods

# Parallele class attributes and methods

# droneDSLLib_Parallele3 class attributes and methods

# droneDSLLib_Parallele4 class attributes and methods

# droneDSLLib_Mouvement class attributes and methods

# droneDSLLib_DecollerAtterrir class attributes and methods
droneDSLLib_DecollerAtterrir_str: Property = Property(name="str", type=StringType)
droneDSLLib_DecollerAtterrir.attributes={droneDSLLib_DecollerAtterrir_str}

# droneDSLLib_CommandeBasique class attributes and methods

# Relationships
fonctions0: BinaryAssociation = BinaryAssociation(
    name="fonctions0",
    ends={
        Property(name="droneDSLLib_FonctionDecl", type=droneDSLLib_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Model", type=droneDSLLib_FonctionDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
val2: BinaryAssociation = BinaryAssociation(
    name="val2",
    ends={
        Property(name="droneDSLLib_PourcentDecl", type=droneDSLLib_PourcentConst, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="droneDSLLib_PourcentConst", type=droneDSLLib_PourcentDecl, multiplicity=Multiplicity(1, 1))
    }
)
var3: BinaryAssociation = BinaryAssociation(
    name="var3",
    ends={
        Property(name="droneDSLLib_SecondeDecl4", type=droneDSLLib_RefSecondeVar, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_RefSecondeVar", type=droneDSLLib_SecondeDecl, multiplicity=Multiplicity(0, 1))
    }
)
var5: BinaryAssociation = BinaryAssociation(
    name="var5",
    ends={
        Property(name="droneDSLLib_PourcentDecl6", type=droneDSLLib_RefPourcentVar, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_RefPourcentVar", type=droneDSLLib_PourcentDecl, multiplicity=Multiplicity(0, 1))
    }
)
duree7: BinaryAssociation = BinaryAssociation(
    name="duree7",
    ends={
        Property(name="droneDSLLib_SecondeExp", type=droneDSLLib_Monter, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Monter", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse8: BinaryAssociation = BinaryAssociation(
    name="vitesse8",
    ends={
        Property(name="droneDSLLib_PourcentExp", type=droneDSLLib_Monter, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Monter9", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree10: BinaryAssociation = BinaryAssociation(
    name="duree10",
    ends={
        Property(name="droneDSLLib_SecondeExp11", type=droneDSLLib_Descendre, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Descendre", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse12: BinaryAssociation = BinaryAssociation(
    name="vitesse12",
    ends={
        Property(name="droneDSLLib_PourcentExp14", type=droneDSLLib_Descendre, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Descendre13", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree15: BinaryAssociation = BinaryAssociation(
    name="duree15",
    ends={
        Property(name="droneDSLLib_SecondeExp16", type=droneDSLLib_Avancer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Avancer", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse17: BinaryAssociation = BinaryAssociation(
    name="vitesse17",
    ends={
        Property(name="droneDSLLib_PourcentExp19", type=droneDSLLib_Avancer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Avancer18", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val1: BinaryAssociation = BinaryAssociation(
    name="val1",
    ends={
        Property(name="droneDSLLib_SecondeConst", type=droneDSLLib_SecondeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_SecondeDecl", type=droneDSLLib_SecondeConst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse22: BinaryAssociation = BinaryAssociation(
    name="vitesse22",
    ends={
        Property(name="droneDSLLib_PourcentExp24", type=droneDSLLib_Reculer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Reculer23", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree25: BinaryAssociation = BinaryAssociation(
    name="duree25",
    ends={
        Property(name="droneDSLLib_SecondeExp26", type=droneDSLLib_Gauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Gauche", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse27: BinaryAssociation = BinaryAssociation(
    name="vitesse27",
    ends={
        Property(name="droneDSLLib_PourcentExp29", type=droneDSLLib_Gauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Gauche28", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree30: BinaryAssociation = BinaryAssociation(
    name="duree30",
    ends={
        Property(name="droneDSLLib_SecondeExp31", type=droneDSLLib_Droite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Droite", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse32: BinaryAssociation = BinaryAssociation(
    name="vitesse32",
    ends={
        Property(name="droneDSLLib_PourcentExp34", type=droneDSLLib_Droite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Droite33", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree35: BinaryAssociation = BinaryAssociation(
    name="duree35",
    ends={
        Property(name="droneDSLLib_SecondeExp36", type=droneDSLLib_RotationGauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_RotationGauche", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse37: BinaryAssociation = BinaryAssociation(
    name="vitesse37",
    ends={
        Property(name="droneDSLLib_PourcentExp39", type=droneDSLLib_RotationGauche, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_RotationGauche38", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree40: BinaryAssociation = BinaryAssociation(
    name="duree40",
    ends={
        Property(name="droneDSLLib_SecondeExp41", type=droneDSLLib_RotationDroite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_RotationDroite", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vitesse42: BinaryAssociation = BinaryAssociation(
    name="vitesse42",
    ends={
        Property(name="droneDSLLib_PourcentExp44", type=droneDSLLib_RotationDroite, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_RotationDroite43", type=droneDSLLib_PourcentExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree20: BinaryAssociation = BinaryAssociation(
    name="duree20",
    ends={
        Property(name="droneDSLLib_SecondeExp21", type=droneDSLLib_Reculer, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Reculer", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="droneDSLLib_EObject", type=droneDSLLib_FonctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_FonctionDecl48", type=droneDSLLib_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref49: BinaryAssociation = BinaryAssociation(
    name="ref49",
    ends={
        Property(name="droneDSLLib_FonctionDecl50", type=droneDSLLib_FonctionCallInterne, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_FonctionCallInterne", type=droneDSLLib_FonctionDecl, multiplicity=Multiplicity(0, 1))
    }
)
a51: BinaryAssociation = BinaryAssociation(
    name="a51",
    ends={
        Property(name="droneDSLLib_EObject52", type=droneDSLLib_Parallele, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Parallele", type=droneDSLLib_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b53: BinaryAssociation = BinaryAssociation(
    name="b53",
    ends={
        Property(name="droneDSLLib_EObject55", type=droneDSLLib_Parallele, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Parallele54", type=droneDSLLib_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t56: BinaryAssociation = BinaryAssociation(
    name="t56",
    ends={
        Property(name="droneDSLLib_EObject57", type=droneDSLLib_Parallele2, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Parallele2", type=droneDSLLib_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c58: BinaryAssociation = BinaryAssociation(
    name="c58",
    ends={
        Property(name="droneDSLLib_EObject59", type=droneDSLLib_Parallele3, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Parallele3", type=droneDSLLib_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c60: BinaryAssociation = BinaryAssociation(
    name="c60",
    ends={
        Property(name="droneDSLLib_EObject61", type=droneDSLLib_Parallele4, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Parallele4", type=droneDSLLib_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d62: BinaryAssociation = BinaryAssociation(
    name="d62",
    ends={
        Property(name="droneDSLLib_EObject64", type=droneDSLLib_Parallele4, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Parallele463", type=droneDSLLib_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duree45: BinaryAssociation = BinaryAssociation(
    name="duree45",
    ends={
        Property(name="droneDSLLib_SecondeExp46", type=droneDSLLib_Pause, multiplicity=Multiplicity(1, 1)),
        Property(name="droneDSLLib_Pause", type=droneDSLLib_SecondeExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_droneDSLLib_SecondeConst_SecondeExp = Generalization(general=SecondeExp, specific=droneDSLLib_SecondeConst)
gen_droneDSLLib_PourcentConst_PourcentExp = Generalization(general=PourcentExp, specific=droneDSLLib_PourcentConst)
gen_droneDSLLib_RefSecondeVar_SecondeExp = Generalization(general=SecondeExp, specific=droneDSLLib_RefSecondeVar)
gen_droneDSLLib_RefPourcentVar_PourcentExp = Generalization(general=PourcentExp, specific=droneDSLLib_RefPourcentVar)
gen_droneDSLLib_Decoller_DecollerAtterrir = Generalization(general=DecollerAtterrir, specific=droneDSLLib_Decoller)
gen_droneDSLLib_Atterrir_DecollerAtterrir = Generalization(general=DecollerAtterrir, specific=droneDSLLib_Atterrir)
gen_droneDSLLib_Monter_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_Monter)
gen_droneDSLLib_Monter_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_Monter)
gen_droneDSLLib_Monter_MD = Generalization(general=MD, specific=droneDSLLib_Monter)
gen_droneDSLLib_Descendre_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_Descendre)
gen_droneDSLLib_Descendre_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_Descendre)
gen_droneDSLLib_Descendre_MD = Generalization(general=MD, specific=droneDSLLib_Descendre)
gen_droneDSLLib_Avancer_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_Avancer)
gen_droneDSLLib_Avancer_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_Avancer)
gen_droneDSLLib_Avancer_AR = Generalization(general=AR, specific=droneDSLLib_Avancer)
gen_droneDSLLib_SecondeDecl_VarDecl = Generalization(general=VarDecl, specific=droneDSLLib_SecondeDecl)
gen_droneDSLLib_PourcentDecl_VarDecl = Generalization(general=VarDecl, specific=droneDSLLib_PourcentDecl)
gen_droneDSLLib_Gauche_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_Gauche)
gen_droneDSLLib_Gauche_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_Gauche)
gen_droneDSLLib_Gauche_GDr = Generalization(general=GDr, specific=droneDSLLib_Gauche)
gen_droneDSLLib_Droite_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_Droite)
gen_droneDSLLib_Droite_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_Droite)
gen_droneDSLLib_Droite_GDr = Generalization(general=GDr, specific=droneDSLLib_Droite)
gen_droneDSLLib_RotationGauche_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_RotationGauche)
gen_droneDSLLib_RotationGauche_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_RotationGauche)
gen_droneDSLLib_RotationGauche_RGRD = Generalization(general=RGRD, specific=droneDSLLib_RotationGauche)
gen_droneDSLLib_RotationDroite_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_RotationDroite)
gen_droneDSLLib_RotationDroite_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_RotationDroite)
gen_droneDSLLib_RotationDroite_RGRD = Generalization(general=RGRD, specific=droneDSLLib_RotationDroite)
gen_droneDSLLib_Pause_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_Pause)
gen_droneDSLLib_Reculer_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_Reculer)
gen_droneDSLLib_Reculer_CommandeBasique = Generalization(general=CommandeBasique, specific=droneDSLLib_Reculer)
gen_droneDSLLib_Reculer_AR = Generalization(general=AR, specific=droneDSLLib_Reculer)
gen_droneDSLLib_FonctionCallInterne_FonctionCall = Generalization(general=FonctionCall, specific=droneDSLLib_FonctionCallInterne)
gen_droneDSLLib_Parallele_Mouvement = Generalization(general=Mouvement, specific=droneDSLLib_Parallele)
gen_droneDSLLib_Parallele2_Parallele = Generalization(general=Parallele, specific=droneDSLLib_Parallele2)
gen_droneDSLLib_Parallele3_Parallele = Generalization(general=Parallele, specific=droneDSLLib_Parallele3)
gen_droneDSLLib_Parallele4_Parallele = Generalization(general=Parallele, specific=droneDSLLib_Parallele4)

# Domain Model
domain_model = DomainModel(
    name="droneDSLLib",
    types={droneDSLLib_Model, droneDSLLib_FonctionDecl, droneDSLLib_SecondeConst, SecondeExp, droneDSLLib_PourcentConst, PourcentExp, droneDSLLib_VarDecl, droneDSLLib_RefSecondeVar, droneDSLLib_RefPourcentVar, droneDSLLib_PourcentExp, droneDSLLib_SecondeExp, droneDSLLib_Decoller, DecollerAtterrir, droneDSLLib_Atterrir, droneDSLLib_Monter, Mouvement, CommandeBasique, MD, droneDSLLib_Descendre, droneDSLLib_Avancer, AR, droneDSLLib_SecondeDecl, VarDecl, droneDSLLib_PourcentDecl, droneDSLLib_Gauche, GDr, droneDSLLib_Droite, droneDSLLib_RotationGauche, RGRD, droneDSLLib_RotationDroite, droneDSLLib_Pause, droneDSLLib_Reculer, droneDSLLib_EObject, droneDSLLib_FonctionCall, droneDSLLib_FonctionCallInterne, FonctionCall, droneDSLLib_MD, droneDSLLib_GDr, droneDSLLib_RGRD, droneDSLLib_AR, droneDSLLib_Parallele, droneDSLLib_Parallele2, Parallele, droneDSLLib_Parallele3, droneDSLLib_Parallele4, droneDSLLib_Mouvement, droneDSLLib_DecollerAtterrir, droneDSLLib_CommandeBasique},
    associations={fonctions0, val2, var3, var5, duree7, vitesse8, duree10, vitesse12, duree15, vitesse17, val1, vitesse22, duree25, vitesse27, duree30, vitesse32, duree35, vitesse37, duree40, vitesse42, duree20, body47, ref49, a51, b53, t56, c58, c60, d62, duree45},
    generalizations={gen_droneDSLLib_SecondeConst_SecondeExp, gen_droneDSLLib_PourcentConst_PourcentExp, gen_droneDSLLib_RefSecondeVar_SecondeExp, gen_droneDSLLib_RefPourcentVar_PourcentExp, gen_droneDSLLib_Decoller_DecollerAtterrir, gen_droneDSLLib_Atterrir_DecollerAtterrir, gen_droneDSLLib_Monter_Mouvement, gen_droneDSLLib_Monter_CommandeBasique, gen_droneDSLLib_Monter_MD, gen_droneDSLLib_Descendre_Mouvement, gen_droneDSLLib_Descendre_CommandeBasique, gen_droneDSLLib_Descendre_MD, gen_droneDSLLib_Avancer_Mouvement, gen_droneDSLLib_Avancer_CommandeBasique, gen_droneDSLLib_Avancer_AR, gen_droneDSLLib_SecondeDecl_VarDecl, gen_droneDSLLib_PourcentDecl_VarDecl, gen_droneDSLLib_Gauche_Mouvement, gen_droneDSLLib_Gauche_CommandeBasique, gen_droneDSLLib_Gauche_GDr, gen_droneDSLLib_Droite_Mouvement, gen_droneDSLLib_Droite_CommandeBasique, gen_droneDSLLib_Droite_GDr, gen_droneDSLLib_RotationGauche_Mouvement, gen_droneDSLLib_RotationGauche_CommandeBasique, gen_droneDSLLib_RotationGauche_RGRD, gen_droneDSLLib_RotationDroite_Mouvement, gen_droneDSLLib_RotationDroite_CommandeBasique, gen_droneDSLLib_RotationDroite_RGRD, gen_droneDSLLib_Pause_CommandeBasique, gen_droneDSLLib_Reculer_Mouvement, gen_droneDSLLib_Reculer_CommandeBasique, gen_droneDSLLib_Reculer_AR, gen_droneDSLLib_FonctionCallInterne_FonctionCall, gen_droneDSLLib_Parallele_Mouvement, gen_droneDSLLib_Parallele2_Parallele, gen_droneDSLLib_Parallele3_Parallele, gen_droneDSLLib_Parallele4_Parallele},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
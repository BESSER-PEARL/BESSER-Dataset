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
ActionListener_Interface = Class(name="ActionListener_Interface")
Vue_VueCommande = Class(name="Vue_VueCommande")
Vue_VueGrille = Class(name="Vue_VueGrille")
Vue_CVue = Class(name="Vue_CVue")
Modele_CModele = Class(name="Modele_CModele")
Modele_Cellule = Class(name="Modele_Cellule")
Modele_Joueur = Class(name="Modele_Joueur")
Modele_Participants = Class(name="Modele_Participants")
Observer_Interface = Class(name="Observer_Interface")
Observable = Class(name="Observable", is_abstract=True)
Controleur_Controleur = Class(name="Controleur_Controleur")
JPanel = Class(name="JPanel")
Graphics_Interface = Class(name="Graphics_Interface")
Class_ = Class(name="Class")
ActionEvent2_Interface = Class(name="ActionEvent2_Interface")

# ActionListener_Interface class attributes and methods

# Vue_VueCommande class attributes and methods
Vue_VueCommande_modele: Property = Property(name="modele", type=Modele_CModele)
Vue_VueCommande.attributes={Vue_VueCommande_modele}

# Vue_VueGrille class attributes and methods
Vue_VueGrille_modele: Property = Property(name="modele", type=Modele_CModele)
Vue_VueGrille_TAILLE: Property = Property(name="TAILLE", type=IntegerType)
Vue_VueGrille_update: Property = Property(name="update", type=StringType)
Vue_VueGrille.attributes={Vue_VueGrille_TAILLE, Vue_VueGrille_update, Vue_VueGrille_modele}

# Vue_CVue class attributes and methods
Vue_CVue_frame: Property = Property(name="frame", type=StringType)
Vue_CVue_grille: Property = Property(name="grille", type=Vue_VueGrille)
Vue_CVue_commande: Property = Property(name="commande", type=Vue_VueCommande)
Vue_CVue.attributes={Vue_CVue_grille, Vue_CVue_frame, Vue_CVue_commande}

# Modele_CModele class attributes and methods
Modele_CModele_hauteur: Property = Property(name="hauteur", type=IntegerType)
Modele_CModele_largeur: Property = Property(name="largeur", type=IntegerType)
Modele_CModele_attribute: Property = Property(name="attribute", type=Modele_Cellule)
Modele_CModele.attributes={Modele_CModele_largeur, Modele_CModele_hauteur, Modele_CModele_attribute}

# Modele_Cellule class attributes and methods
Modele_Cellule_modele: Property = Property(name="modele", type=Modele_CModele)
Modele_Cellule_etat: Property = Property(name="etat", type=BooleanType)
Modele_Cellule_x: Property = Property(name="x", type=IntegerType)
Modele_Cellule_prochaineEtat: Property = Property(name="prochaineEtat", type=BooleanType)
Modele_Cellule_y: Property = Property(name="y", type=IntegerType)
Modele_Cellule.attributes={Modele_Cellule_prochaineEtat, Modele_Cellule_modele, Modele_Cellule_y, Modele_Cellule_x, Modele_Cellule_etat}

# Modele_Joueur class attributes and methods
Modele_Joueur_cles: Property = Property(name="cles", type=IntegerType)
Modele_Joueur_x: Property = Property(name="x", type=IntegerType)
Modele_Joueur_y: Property = Property(name="y", type=IntegerType)
Modele_Joueur_artefacts: Property = Property(name="artefacts", type=StringType)
Modele_Joueur_vivant: Property = Property(name="vivant", type=BooleanType)
Modele_Joueur.attributes={Modele_Joueur_artefacts, Modele_Joueur_cles, Modele_Joueur_vivant, Modele_Joueur_y, Modele_Joueur_x}

# Modele_Participants class attributes and methods
Modele_Participants_NOMBRE: Property = Property(name="NOMBRE", type=IntegerType)
Modele_Participants_attribute: Property = Property(name="attribute", type=StringType)
Modele_Participants.attributes={Modele_Participants_NOMBRE, Modele_Participants_attribute}

# Observer_Interface class attributes and methods

# Observable class attributes and methods

# Controleur_Controleur class attributes and methods
Controleur_Controleur_modele: Property = Property(name="modele", type=Modele_CModele)
Controleur_Controleur.attributes={Controleur_Controleur_modele}

# JPanel class attributes and methods

# Graphics_Interface class attributes and methods

# Class class attributes and methods

# ActionEvent2_Interface class attributes and methods

# Relationships
VueGrille_CVue: BinaryAssociation = BinaryAssociation(
    name="VueGrille_CVue",
    ends={
        Property(name="VueGrille_CVue_00", type=Vue_CVue, multiplicity=Multiplicity(0, 9999)),
        Property(name="VueGrille_CVue_11", type=Vue_VueGrille, multiplicity=Multiplicity(1, 1))
    }
)
VueGrille_CModele: BinaryAssociation = BinaryAssociation(
    name="VueGrille_CModele",
    ends={
        Property(name="VueGrille_CModele_02", type=Modele_CModele, multiplicity=Multiplicity(1, 1)),
        Property(name="VueGrille_CModele_13", type=Vue_VueGrille, multiplicity=Multiplicity(0, 9999))
    }
)
CVue_VueCommande: BinaryAssociation = BinaryAssociation(
    name="CVue_VueCommande",
    ends={
        Property(name="CVue_VueCommande_04", type=Vue_VueCommande, multiplicity=Multiplicity(1, 1)),
        Property(name="CVue_VueCommande_15", type=Vue_CVue, multiplicity=Multiplicity(0, 9999))
    }
)
VueCommande_CModele: BinaryAssociation = BinaryAssociation(
    name="VueCommande_CModele",
    ends={
        Property(name="VueCommande_CModele_06", type=Modele_CModele, multiplicity=Multiplicity(1, 1)),
        Property(name="VueCommande_CModele_17", type=Vue_VueCommande, multiplicity=Multiplicity(0, 9999))
    }
)
CModele_Cellule: BinaryAssociation = BinaryAssociation(
    name="CModele_Cellule",
    ends={
        Property(name="Cellule8", type=Modele_Cellule, multiplicity=Multiplicity(0, 9999)),
        Property(name="CModele9", type=Modele_CModele, multiplicity=Multiplicity(1, 1))
    }
)
CModele_Controleur: BinaryAssociation = BinaryAssociation(
    name="CModele_Controleur",
    ends={
        Property(name="CModele_Controleur_010", type=Controleur_Controleur, multiplicity=Multiplicity(0, 9999)),
        Property(name="Controleur11", type=Modele_CModele, multiplicity=Multiplicity(1, 1))
    }
)
Participants_Joueur: BinaryAssociation = BinaryAssociation(
    name="Participants_Joueur",
    ends={
        Property(name="Joueur12", type=Modele_Joueur, multiplicity=Multiplicity(0, 9999)),
        Property(name="Participants13", type=Modele_Participants, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2b7c6301_1860_4b56_93cc_48eecf0de43e",
    types={ActionListener_Interface, Vue_VueCommande, Vue_VueGrille, Vue_CVue, Modele_CModele, Modele_Cellule, Modele_Joueur, Modele_Participants, Observer_Interface, Observable, Controleur_Controleur, JPanel, Graphics_Interface, Class_, ActionEvent2_Interface},
    associations={VueGrille_CVue, VueGrille_CModele, CVue_VueCommande, VueCommande_CModele, CModele_Cellule, CModele_Controleur, Participants_Joueur},
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
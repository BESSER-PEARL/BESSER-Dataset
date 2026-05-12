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

# Enumerations
Information: Enumeration = Enumeration(
    name="Information",
    literals={
            
    }
)

IHM: Enumeration = Enumeration(
    name="IHM",
    literals={
            
    }
)

# Classes
Analyse_Fast_Food = Class(name="Analyse_Fast_Food")
Analyse_Review = Class(name="Analyse_Review")
Analyse_Utilisateur = Class(name="Analyse_Utilisateur")
Analyse_Compte = Class(name="Analyse_Compte")
Analyse_Criteres = Class(name="Analyse_Criteres")
Analyse_Moderateurs = Class(name="Analyse_Moderateurs")
FicheRestaurant = Class(name="FicheRestaurant")
AvisGlobal = Class(name="AvisGlobal")
Commentaire = Class(name="Commentaire")
Photo = Class(name="Photo")
Pr_sentation = Class(name="Pr_sentation")
Analyse2_Fast_Food = Class(name="Analyse2_Fast_Food")
Analyse2_Review = Class(name="Analyse2_Review")
Analyse2_Utilisateur = Class(name="Analyse2_Utilisateur")
Analyse2_Compte = Class(name="Analyse2_Compte")
Analyse2_Criteres = Class(name="Analyse2_Criteres")
Analyse2_Moderateurs = Class(name="Analyse2_Moderateurs")
Analyse2_AvisGlobal = Class(name="Analyse2_AvisGlobal")
Controlleur_Actor = Class(name="Controlleur_Actor")

# Analyse_Fast_Food class attributes and methods
Analyse_Fast_Food_Adresse: Property = Property(name="Adresse", type=StringType)
Analyse_Fast_Food_Ville: Property = Property(name="Ville", type=StringType)
Analyse_Fast_Food_nbPlaces: Property = Property(name="nbPlaces", type=IntegerType)
Analyse_Fast_Food_nom: Property = Property(name="nom", type=StringType)
Analyse_Fast_Food_prixMax: Property = Property(name="prixMax", type=IntegerType)
Analyse_Fast_Food_prixMin: Property = Property(name="prixMin", type=IntegerType)
Analyse_Fast_Food_numeroTel: Property = Property(name="numeroTel", type=StringType)
Analyse_Fast_Food_horaires: Property = Property(name="horaires", type=StringType)
Analyse_Fast_Food_proprietaire: Property = Property(name="proprietaire", type=StringType)
Analyse_Fast_Food_notes: Property = Property(name="notes", type=StringType)
Analyse_Fast_Food_photos: Property = Property(name="photos", type=StringType)
Analyse_Fast_Food.attributes={Analyse_Fast_Food_notes, Analyse_Fast_Food_nom, Analyse_Fast_Food_prixMin, Analyse_Fast_Food_numeroTel, Analyse_Fast_Food_horaires, Analyse_Fast_Food_Ville, Analyse_Fast_Food_photos, Analyse_Fast_Food_Adresse, Analyse_Fast_Food_proprietaire, Analyse_Fast_Food_prixMax, Analyse_Fast_Food_nbPlaces}

# Analyse_Review class attributes and methods
Analyse_Review_NoteGlobale: Property = Property(name="NoteGlobale", type=IntegerType)
Analyse_Review_lesNotes: Property = Property(name="lesNotes", type=StringType)
Analyse_Review_Commentaire: Property = Property(name="Commentaire", type=StringType)
Analyse_Review.attributes={Analyse_Review_Commentaire, Analyse_Review_lesNotes, Analyse_Review_NoteGlobale}

# Analyse_Utilisateur class attributes and methods

# Analyse_Compte class attributes and methods
Analyse_Compte_login: Property = Property(name="login", type=StringType)
Analyse_Compte_motdepasse: Property = Property(name="motdepasse", type=StringType)
Analyse_Compte.attributes={Analyse_Compte_motdepasse, Analyse_Compte_login}

# Analyse_Criteres class attributes and methods
Analyse_Criteres_rapportQualitePrix: Property = Property(name="rapportQualitePrix", type=IntegerType)
Analyse_Criteres_rapidite: Property = Property(name="rapidite", type=IntegerType)
Analyse_Criteres_qualit_: Property = Property(name="qualit_", type=IntegerType)
Analyse_Criteres_respectHoraires: Property = Property(name="respectHoraires", type=IntegerType)
Analyse_Criteres_amabilite: Property = Property(name="amabilite", type=IntegerType)
Analyse_Criteres.attributes={Analyse_Criteres_amabilite, Analyse_Criteres_rapportQualitePrix, Analyse_Criteres_rapidite, Analyse_Criteres_respectHoraires, Analyse_Criteres_qualit_}

# Analyse_Moderateurs class attributes and methods

# FicheRestaurant class attributes and methods
FicheRestaurant_nom: Property = Property(name="nom", type=StringType)
FicheRestaurant.attributes={FicheRestaurant_nom}

# AvisGlobal class attributes and methods
AvisGlobal_note: Property = Property(name="note", type=StringType)
AvisGlobal_nbAvis: Property = Property(name="nbAvis", type=IntegerType)
AvisGlobal_diagramme: Property = Property(name="diagramme", type=StringType)
AvisGlobal_Commentaires: Property = Property(name="Commentaires", type=StringType)
AvisGlobal.attributes={AvisGlobal_note, AvisGlobal_Commentaires, AvisGlobal_nbAvis, AvisGlobal_diagramme}

# Commentaire class attributes and methods
Commentaire_auteur: Property = Property(name="auteur", type=Analyse_Compte)
Commentaire_commentaire: Property = Property(name="commentaire", type=StringType)
Commentaire.attributes={Commentaire_auteur, Commentaire_commentaire}

# Photo class attributes and methods

# Pr_sentation class attributes and methods
Pr_sentation_numTel: Property = Property(name="numTel", type=StringType)
Pr_sentation_siteDeCommande: Property = Property(name="siteDeCommande", type=StringType)
Pr_sentation_ouverture: Property = Property(name="ouverture", type=StringType)
Pr_sentation_description: Property = Property(name="description", type=StringType)
Pr_sentation_adresse: Property = Property(name="adresse", type=StringType)
Pr_sentation.attributes={Pr_sentation_ouverture, Pr_sentation_siteDeCommande, Pr_sentation_numTel, Pr_sentation_adresse, Pr_sentation_description}

# Analyse2_Fast_Food class attributes and methods
Analyse2_Fast_Food_nom: Property = Property(name="nom", type=StringType)
Analyse2_Fast_Food_numeroTel: Property = Property(name="numeroTel", type=StringType)
Analyse2_Fast_Food_siteDeCommande: Property = Property(name="siteDeCommande", type=StringType)
Analyse2_Fast_Food_description: Property = Property(name="description", type=StringType)
Analyse2_Fast_Food_horaires: Property = Property(name="horaires", type=StringType)
Analyse2_Fast_Food_Adresse: Property = Property(name="Adresse", type=StringType)
Analyse2_Fast_Food_Ville: Property = Property(name="Ville", type=StringType)
Analyse2_Fast_Food_nbPlaces: Property = Property(name="nbPlaces", type=IntegerType)
Analyse2_Fast_Food_prixMax: Property = Property(name="prixMax", type=IntegerType)
Analyse2_Fast_Food_prixMin: Property = Property(name="prixMin", type=IntegerType)
Analyse2_Fast_Food_proprietaire: Property = Property(name="proprietaire", type=StringType)
Analyse2_Fast_Food_reviews: Property = Property(name="reviews", type=StringType)
Analyse2_Fast_Food_photos: Property = Property(name="photos", type=StringType)
Analyse2_Fast_Food.attributes={Analyse2_Fast_Food_siteDeCommande, Analyse2_Fast_Food_description, Analyse2_Fast_Food_numeroTel, Analyse2_Fast_Food_proprietaire, Analyse2_Fast_Food_reviews, Analyse2_Fast_Food_photos, Analyse2_Fast_Food_nom, Analyse2_Fast_Food_Ville, Analyse2_Fast_Food_horaires, Analyse2_Fast_Food_nbPlaces, Analyse2_Fast_Food_prixMax, Analyse2_Fast_Food_Adresse, Analyse2_Fast_Food_prixMin}

# Analyse2_Review class attributes and methods
Analyse2_Review_utilite: Property = Property(name="utilite", type=StringType)
Analyse2_Review_lesNotes: Property = Property(name="lesNotes", type=StringType)
Analyse2_Review_Commentaire: Property = Property(name="Commentaire", type=StringType)
Analyse2_Review.attributes={Analyse2_Review_utilite, Analyse2_Review_Commentaire, Analyse2_Review_lesNotes}

# Analyse2_Utilisateur class attributes and methods

# Analyse2_Compte class attributes and methods
Analyse2_Compte_login: Property = Property(name="login", type=StringType)
Analyse2_Compte_motdepasse: Property = Property(name="motdepasse", type=StringType)
Analyse2_Compte.attributes={Analyse2_Compte_login, Analyse2_Compte_motdepasse}

# Analyse2_Criteres class attributes and methods
Analyse2_Criteres_rapportQualitePrix: Property = Property(name="rapportQualitePrix", type=IntegerType)
Analyse2_Criteres_rapidite: Property = Property(name="rapidite", type=IntegerType)
Analyse2_Criteres_qualit_: Property = Property(name="qualit_", type=IntegerType)
Analyse2_Criteres_respectHoraires: Property = Property(name="respectHoraires", type=IntegerType)
Analyse2_Criteres_amabilite: Property = Property(name="amabilite", type=IntegerType)
Analyse2_Criteres.attributes={Analyse2_Criteres_qualit_, Analyse2_Criteres_respectHoraires, Analyse2_Criteres_amabilite, Analyse2_Criteres_rapidite, Analyse2_Criteres_rapportQualitePrix}

# Analyse2_Moderateurs class attributes and methods

# Analyse2_AvisGlobal class attributes and methods
Analyse2_AvisGlobal_notes: Property = Property(name="notes", type=StringType)
Analyse2_AvisGlobal_nbAvis: Property = Property(name="nbAvis", type=IntegerType)
Analyse2_AvisGlobal_Commentaires: Property = Property(name="Commentaires", type=StringType)
Analyse2_AvisGlobal.attributes={Analyse2_AvisGlobal_notes, Analyse2_AvisGlobal_Commentaires, Analyse2_AvisGlobal_nbAvis}

# Controlleur_Actor class attributes and methods

# Relationships
Review_Fast_Food: BinaryAssociation = BinaryAssociation(
    name="Review_Fast_Food",
    ends={
        Property(name="caract_rise0", type=Analyse_Fast_Food, multiplicity=Multiplicity(1, 1)),
        Property(name="poss_de1", type=Analyse_Review, multiplicity=Multiplicity(0, 9999))
    }
)
Compte_Utilisateur: BinaryAssociation = BinaryAssociation(
    name="Compte_Utilisateur",
    ends={
        Property(name="est_associ_2", type=Analyse_Utilisateur, multiplicity=Multiplicity(1, 1)),
        Property(name="poss_de3", type=Analyse_Compte, multiplicity=Multiplicity(0, 1))
    }
)
Compte_Review: BinaryAssociation = BinaryAssociation(
    name="Compte_Review",
    ends={
        Property(name="poss_de4", type=Analyse_Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="est__crite5", type=Analyse_Compte, multiplicity=Multiplicity(1, 1))
    }
)
Criteres_Review: BinaryAssociation = BinaryAssociation(
    name="Criteres_Review",
    ends={
        Property(name="sont_associ_s6", type=Analyse_Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="note7", type=Analyse_Criteres, multiplicity=Multiplicity(0, 9999))
    }
)
Moderateurs_Compte: BinaryAssociation = BinaryAssociation(
    name="Moderateurs_Compte",
    ends={
        Property(name="poss_de8", type=Analyse_Compte, multiplicity=Multiplicity(1, 1)),
        Property(name="est_associ_9", type=Analyse_Moderateurs, multiplicity=Multiplicity(1, 1))
    }
)
Commentaire_AvisGlobal: BinaryAssociation = BinaryAssociation(
    name="Commentaire_AvisGlobal",
    ends={
        Property(name="avisGlobal10", type=AvisGlobal, multiplicity=Multiplicity(1, 1)),
        Property(name="commentaire11", type=Commentaire, multiplicity=Multiplicity(0, 9999))
    }
)
AvisGlobal_FicheRestaurant: BinaryAssociation = BinaryAssociation(
    name="AvisGlobal_FicheRestaurant",
    ends={
        Property(name="d_finit12", type=FicheRestaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="poss_de13", type=AvisGlobal, multiplicity=Multiplicity(1, 1))
    }
)
FicheRestaurant_Photo: BinaryAssociation = BinaryAssociation(
    name="FicheRestaurant_Photo",
    ends={
        Property(name="poss_de14", type=Photo, multiplicity=Multiplicity(0, 9999)),
        Property(name="repr_sente15", type=FicheRestaurant, multiplicity=Multiplicity(1, 1))
    }
)
Pr_sentation_FicheRestaurant: BinaryAssociation = BinaryAssociation(
    name="Pr_sentation_FicheRestaurant",
    ends={
        Property(name="repr_sente16", type=FicheRestaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="poss_de17", type=Pr_sentation, multiplicity=Multiplicity(1, 1))
    }
)
Review_Fast_Food1: BinaryAssociation = BinaryAssociation(
    name="Review_Fast_Food1",
    ends={
        Property(name="caract_rise18", type=Analyse2_Fast_Food, multiplicity=Multiplicity(1, 1)),
        Property(name="poss_de19", type=Analyse2_Review, multiplicity=Multiplicity(0, 9999))
    }
)
Compte_Utilisateur1: BinaryAssociation = BinaryAssociation(
    name="Compte_Utilisateur1",
    ends={
        Property(name="est_associ_20", type=Analyse2_Utilisateur, multiplicity=Multiplicity(1, 1)),
        Property(name="poss_de21", type=Analyse2_Compte, multiplicity=Multiplicity(0, 1))
    }
)
Compte_Review1: BinaryAssociation = BinaryAssociation(
    name="Compte_Review1",
    ends={
        Property(name="poss_de22", type=Analyse2_Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="est__crite23", type=Analyse2_Compte, multiplicity=Multiplicity(1, 1))
    }
)
Criteres_Review1: BinaryAssociation = BinaryAssociation(
    name="Criteres_Review1",
    ends={
        Property(name="sont_associ_s24", type=Analyse2_Review, multiplicity=Multiplicity(0, 9999)),
        Property(name="note25", type=Analyse2_Criteres, multiplicity=Multiplicity(0, 9999))
    }
)
Moderateurs_Compte1: BinaryAssociation = BinaryAssociation(
    name="Moderateurs_Compte1",
    ends={
        Property(name="poss_de26", type=Analyse2_Compte, multiplicity=Multiplicity(1, 1)),
        Property(name="est_associ_27", type=Analyse2_Moderateurs, multiplicity=Multiplicity(1, 1))
    }
)
AvisGlobal_Fast_Food: BinaryAssociation = BinaryAssociation(
    name="AvisGlobal_Fast_Food",
    ends={
        Property(name="fast_Food28", type=Analyse2_Fast_Food, multiplicity=Multiplicity(1, 1)),
        Property(name="avisGlobal29", type=Analyse2_AvisGlobal, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6g9DgEGsEemokbRu9Ld3Pw",
    types={Analyse_Fast_Food, Analyse_Review, Analyse_Utilisateur, Analyse_Compte, Analyse_Criteres, Analyse_Moderateurs, FicheRestaurant, AvisGlobal, Commentaire, Photo, Pr_sentation, Analyse2_Fast_Food, Analyse2_Review, Analyse2_Utilisateur, Analyse2_Compte, Analyse2_Criteres, Analyse2_Moderateurs, Analyse2_AvisGlobal, Controlleur_Actor, Information, IHM},
    associations={Review_Fast_Food, Compte_Utilisateur, Compte_Review, Criteres_Review, Moderateurs_Compte, Commentaire_AvisGlobal, AvisGlobal_FicheRestaurant, FicheRestaurant_Photo, Pr_sentation_FicheRestaurant, Review_Fast_Food1, Compte_Utilisateur1, Compte_Review1, Criteres_Review1, Moderateurs_Compte1, AvisGlobal_Fast_Food},
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
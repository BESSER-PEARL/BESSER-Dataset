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
Personne2: Enumeration = Enumeration(
    name="Personne2",
    literals={
            
    }
)

# Classes
Class_ = Class(name="Class")
Personne = Class(name="Personne")
Avis = Class(name="Avis")
Utilisateur = Class(name="Utilisateur")
Avis1 = Class(name="Avis1")
Voiture = Class(name="Voiture")
Trajet = Class(name="Trajet")
Trajet1 = Class(name="Trajet1")
Utilisateur1 = Class(name="Utilisateur1")
V_hicule = Class(name="V_hicule")
Lieu = Class(name="Lieu")
Conducteur = Class(name="Conducteur")
Passager = Class(name="Passager")
Chemin_Interface = Class(name="Chemin_Interface")
Trajet2 = Class(name="Trajet2")
Utilisateur2 = Class(name="Utilisateur2")
V_hicule1 = Class(name="V_hicule1")
Conducteur1 = Class(name="Conducteur1")
Passager1 = Class(name="Passager1")
Avis2 = Class(name="Avis2")
Lieu1 = Class(name="Lieu1")

# Class class attributes and methods

# Personne class attributes and methods

# Avis class attributes and methods

# Utilisateur class attributes and methods
Utilisateur_photoDeProfil: Property = Property(name="photoDeProfil", type=StringType)
Utilisateur_nom: Property = Property(name="nom", type=StringType)
Utilisateur_score: Property = Property(name="score", type=StringType)
Utilisateur_nbAvis: Property = Property(name="nbAvis", type=IntegerType)
Utilisateur.attributes={Utilisateur_photoDeProfil, Utilisateur_nbAvis, Utilisateur_score, Utilisateur_nom}

# Avis1 class attributes and methods
Avis1_note: Property = Property(name="note", type=IntegerType)
Avis1_description: Property = Property(name="description", type=StringType)
Avis1.attributes={Avis1_description, Avis1_note}

# Voiture class attributes and methods
Voiture_places: Property = Property(name="places", type=IntegerType)
Voiture.attributes={Voiture_places}

# Trajet class attributes and methods
Trajet_date: Property = Property(name="date", type=StringType)
Trajet_prix: Property = Property(name="prix", type=IntegerType)
Trajet_depart: Property = Property(name="depart", type=Lieu)
Trajet_destination: Property = Property(name="destination", type=Lieu)
Trajet_placesRestantes: Property = Property(name="placesRestantes", type=IntegerType)
Trajet_description: Property = Property(name="description", type=StringType)
Trajet.attributes={Trajet_destination, Trajet_description, Trajet_date, Trajet_depart, Trajet_placesRestantes, Trajet_prix}

# Trajet1 class attributes and methods
Trajet1_lieudebut: Property = Property(name="lieudebut", type=Lieu)
Trajet1_lieuFin: Property = Property(name="lieuFin", type=Lieu)
Trajet1_datedebut: Property = Property(name="datedebut", type=StringType)
Trajet1_dateFin: Property = Property(name="dateFin", type=StringType)
Trajet1.attributes={Trajet1_dateFin, Trajet1_lieuFin, Trajet1_lieudebut, Trajet1_datedebut}

# Utilisateur1 class attributes and methods
Utilisateur1_nom: Property = Property(name="nom", type=StringType)
Utilisateur1_age: Property = Property(name="age", type=IntegerType)
Utilisateur1_adresse: Property = Property(name="adresse", type=StringType)
Utilisateur1.attributes={Utilisateur1_nom, Utilisateur1_adresse, Utilisateur1_age}

# V_hicule class attributes and methods
V_hicule_imatriculation: Property = Property(name="imatriculation", type=StringType)
V_hicule_modele: Property = Property(name="modele", type=StringType)
V_hicule_marque: Property = Property(name="marque", type=StringType)
V_hicule_propri_taire: Property = Property(name="propri_taire", type=Conducteur)
V_hicule.attributes={V_hicule_modele, V_hicule_marque, V_hicule_propri_taire, V_hicule_imatriculation}

# Lieu class attributes and methods

# Conducteur class attributes and methods

# Passager class attributes and methods

# Chemin_Interface class attributes and methods

# Trajet2 class attributes and methods
Trajet2_lieudebut: Property = Property(name="lieudebut", type=Lieu)
Trajet2_lieuFin: Property = Property(name="lieuFin", type=Lieu)
Trajet2_datedebut: Property = Property(name="datedebut", type=StringType)
Trajet2_dateFin: Property = Property(name="dateFin", type=StringType)
Trajet2_prix: Property = Property(name="prix", type=IntegerType)
Trajet2_placesRestantes: Property = Property(name="placesRestantes", type=IntegerType)
Trajet2_description: Property = Property(name="description", type=StringType)
Trajet2.attributes={Trajet2_datedebut, Trajet2_description, Trajet2_prix, Trajet2_dateFin, Trajet2_placesRestantes, Trajet2_lieuFin, Trajet2_lieudebut}

# Utilisateur2 class attributes and methods
Utilisateur2_nom: Property = Property(name="nom", type=StringType)
Utilisateur2_age: Property = Property(name="age", type=IntegerType)
Utilisateur2_adresse: Property = Property(name="adresse", type=StringType)
Utilisateur2_photoDeProfil: Property = Property(name="photoDeProfil", type=StringType)
Utilisateur2_nbAvis: Property = Property(name="nbAvis", type=IntegerType)
Utilisateur2.attributes={Utilisateur2_adresse, Utilisateur2_age, Utilisateur2_nbAvis, Utilisateur2_nom, Utilisateur2_photoDeProfil}

# V_hicule1 class attributes and methods
V_hicule1_imatriculation: Property = Property(name="imatriculation", type=StringType)
V_hicule1_modele: Property = Property(name="modele", type=StringType)
V_hicule1_marque: Property = Property(name="marque", type=StringType)
V_hicule1_propri_taire: Property = Property(name="propri_taire", type=Conducteur1)
V_hicule1_nbPlaces: Property = Property(name="nbPlaces", type=IntegerType)
V_hicule1.attributes={V_hicule1_propri_taire, V_hicule1_marque, V_hicule1_modele, V_hicule1_nbPlaces, V_hicule1_imatriculation}

# Conducteur1 class attributes and methods

# Passager1 class attributes and methods

# Avis2 class attributes and methods
Avis2_note: Property = Property(name="note", type=IntegerType)
Avis2_description: Property = Property(name="description", type=StringType)
Avis2.attributes={Avis2_note, Avis2_description}

# Lieu1 class attributes and methods

# Relationships
Personne_Avis: BinaryAssociation = BinaryAssociation(
    name="Personne_Avis",
    ends={
        Property(name="avis0", type=Avis1, multiplicity=Multiplicity(0, 9999)),
        Property(name="Utilisateur1", type=Utilisateur, multiplicity=Multiplicity(1, 1))
    }
)
Trajet_Passager: BinaryAssociation = BinaryAssociation(
    name="Trajet_Passager",
    ends={
        Property(name="passager2", type=Passager, multiplicity=Multiplicity(1, 9999)),
        Property(name="trajet3", type=Trajet1, multiplicity=Multiplicity(1, 1))
    }
)
V_hicule_Conducteur: BinaryAssociation = BinaryAssociation(
    name="V_hicule_Conducteur",
    ends={
        Property(name="conducteur4", type=Conducteur, multiplicity=Multiplicity(1, 1)),
        Property(name="v_hicule5", type=V_hicule, multiplicity=Multiplicity(1, 9999))
    }
)
Trajet_Conducteur: BinaryAssociation = BinaryAssociation(
    name="Trajet_Conducteur",
    ends={
        Property(name="conducteur6", type=Conducteur, multiplicity=Multiplicity(1, 1)),
        Property(name="trajet7", type=Trajet1, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Trajet: BinaryAssociation = BinaryAssociation(
    name="Personne_Trajet",
    ends={
        Property(name="trajet8", type=Trajet, multiplicity=Multiplicity(0, 9999)),
        Property(name="Utilisateur9", type=Utilisateur, multiplicity=Multiplicity(1, 1))
    }
)
Personne_Voiture: BinaryAssociation = BinaryAssociation(
    name="Personne_Voiture",
    ends={
        Property(name="voiture10", type=Voiture, multiplicity=Multiplicity(0, 9999)),
        Property(name="Utilisateur11", type=Utilisateur, multiplicity=Multiplicity(1, 1))
    }
)
Utilisateur_Avis: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Avis",
    ends={
        Property(name="avis12", type=Avis2, multiplicity=Multiplicity(0, 9999)),
        Property(name="utilisateur13", type=Utilisateur2, multiplicity=Multiplicity(1, 1))
    }
)
Conducteur_V_hicule: BinaryAssociation = BinaryAssociation(
    name="Conducteur_V_hicule",
    ends={
        Property(name="v_hicule14", type=V_hicule1, multiplicity=Multiplicity(0, 9999)),
        Property(name="conducteur15", type=Conducteur1, multiplicity=Multiplicity(1, 1))
    }
)
Conducteur_Trajet: BinaryAssociation = BinaryAssociation(
    name="Conducteur_Trajet",
    ends={
        Property(name="trajet16", type=Trajet2, multiplicity=Multiplicity(0, 9999)),
        Property(name="conducteur17", type=Conducteur1, multiplicity=Multiplicity(1, 1))
    }
)
Passager_Trajet: BinaryAssociation = BinaryAssociation(
    name="Passager_Trajet",
    ends={
        Property(name="trajet18", type=Trajet2, multiplicity=Multiplicity(1, 1)),
        Property(name="passager19", type=Passager1, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f441a1ff_f110_40c3_bea6_508edb95649e",
    types={Class_, Personne, Avis, Utilisateur, Avis1, Voiture, Trajet, Trajet1, Utilisateur1, V_hicule, Lieu, Conducteur, Passager, Chemin_Interface, Trajet2, Utilisateur2, V_hicule1, Conducteur1, Passager1, Avis2, Lieu1, Personne2},
    associations={Personne_Avis, Trajet_Passager, V_hicule_Conducteur, Trajet_Conducteur, Personne_Trajet, Personne_Voiture, Utilisateur_Avis, Conducteur_V_hicule, Conducteur_Trajet, Passager_Trajet},
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
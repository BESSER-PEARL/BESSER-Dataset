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

# Class class attributes and methods

# Personne class attributes and methods

# Avis class attributes and methods

# Utilisateur class attributes and methods
Utilisateur_nom: Property = Property(name="nom", type=StringType)
Utilisateur_score: Property = Property(name="score", type=StringType)
Utilisateur_nbAvis: Property = Property(name="nbAvis", type=IntegerType)
Utilisateur_photoDeProfil: Property = Property(name="photoDeProfil", type=StringType)
Utilisateur.attributes={Utilisateur_score, Utilisateur_photoDeProfil, Utilisateur_nbAvis, Utilisateur_nom}

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
Trajet.attributes={Trajet_depart, Trajet_date, Trajet_placesRestantes, Trajet_destination, Trajet_prix, Trajet_description}

# Trajet1 class attributes and methods
Trajet1_lieudebut: Property = Property(name="lieudebut", type=Lieu)
Trajet1_lieuFin: Property = Property(name="lieuFin", type=Lieu)
Trajet1_datedebut: Property = Property(name="datedebut", type=StringType)
Trajet1_dateFin: Property = Property(name="dateFin", type=StringType)
Trajet1.attributes={Trajet1_dateFin, Trajet1_lieudebut, Trajet1_lieuFin, Trajet1_datedebut}

# Utilisateur1 class attributes and methods
Utilisateur1_nom: Property = Property(name="nom", type=StringType)
Utilisateur1_age: Property = Property(name="age", type=IntegerType)
Utilisateur1_adresse: Property = Property(name="adresse", type=StringType)
Utilisateur1.attributes={Utilisateur1_adresse, Utilisateur1_age, Utilisateur1_nom}

# V_hicule class attributes and methods
V_hicule_imatriculation: Property = Property(name="imatriculation", type=StringType)
V_hicule_modele: Property = Property(name="modele", type=StringType)
V_hicule_marque: Property = Property(name="marque", type=StringType)
V_hicule_propri_taire: Property = Property(name="propri_taire", type=Conducteur)
V_hicule.attributes={V_hicule_modele, V_hicule_marque, V_hicule_imatriculation, V_hicule_propri_taire}

# Lieu class attributes and methods

# Conducteur class attributes and methods

# Passager class attributes and methods

# Chemin_Interface class attributes and methods

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

# Domain Model
domain_model = DomainModel(
    name="_2465ef00_8115_453b_99a5_436541400c81",
    types={Class_, Personne, Avis, Utilisateur, Avis1, Voiture, Trajet, Trajet1, Utilisateur1, V_hicule, Lieu, Conducteur, Passager, Chemin_Interface, Personne2},
    associations={Personne_Avis, Trajet_Passager, V_hicule_Conducteur, Trajet_Conducteur, Personne_Trajet, Personne_Voiture},
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
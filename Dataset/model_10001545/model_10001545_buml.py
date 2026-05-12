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
Role = Class(name="Role")
ihm_Actor = Class(name="ihm_Actor")
Acteur_Actor = Class(name="Acteur_Actor")
Contr_leur_Actor = Class(name="Contr_leur_Actor")
Persistance_Actor = Class(name="Persistance_Actor")
ihm = Class(name="ihm")
Contr_leur = Class(name="Contr_leur")
Persistance = Class(name="Persistance")

# Class class attributes and methods

# Personne class attributes and methods

# Avis class attributes and methods

# Utilisateur class attributes and methods
Utilisateur_nom: Property = Property(name="nom", type=StringType)
Utilisateur_score: Property = Property(name="score", type=StringType)
Utilisateur_nbAvis: Property = Property(name="nbAvis", type=IntegerType)
Utilisateur_photoDeProfil: Property = Property(name="photoDeProfil", type=StringType)
Utilisateur.attributes={Utilisateur_nbAvis, Utilisateur_photoDeProfil, Utilisateur_score, Utilisateur_nom}

# Avis1 class attributes and methods
Avis1_note: Property = Property(name="note", type=IntegerType)
Avis1_description: Property = Property(name="description", type=StringType)
Avis1.attributes={Avis1_note, Avis1_description}

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
Trajet.attributes={Trajet_date, Trajet_prix, Trajet_placesRestantes, Trajet_destination, Trajet_depart, Trajet_description}

# Trajet1 class attributes and methods
Trajet1_datedebut: Property = Property(name="datedebut", type=StringType)
Trajet1_dateFin: Property = Property(name="dateFin", type=StringType)
Trajet1_lieudebut: Property = Property(name="lieudebut", type=Lieu)
Trajet1_lieuFin: Property = Property(name="lieuFin", type=Lieu)
Trajet1.attributes={Trajet1_dateFin, Trajet1_lieudebut, Trajet1_datedebut, Trajet1_lieuFin}

# Utilisateur1 class attributes and methods
Utilisateur1_nom: Property = Property(name="nom", type=StringType)
Utilisateur1_age: Property = Property(name="age", type=IntegerType)
Utilisateur1_adresse: Property = Property(name="adresse", type=StringType)
Utilisateur1.attributes={Utilisateur1_nom, Utilisateur1_age, Utilisateur1_adresse}

# V_hicule class attributes and methods
V_hicule_imatriculation: Property = Property(name="imatriculation", type=StringType)
V_hicule_modele: Property = Property(name="modele", type=StringType)
V_hicule_marque: Property = Property(name="marque", type=StringType)
V_hicule_propri_taire: Property = Property(name="propri_taire", type=Conducteur)
V_hicule.attributes={V_hicule_propri_taire, V_hicule_modele, V_hicule_marque, V_hicule_imatriculation}

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
Trajet2.attributes={Trajet2_prix, Trajet2_placesRestantes, Trajet2_dateFin, Trajet2_lieuFin, Trajet2_datedebut, Trajet2_lieudebut, Trajet2_description}

# Utilisateur2 class attributes and methods
Utilisateur2_nom: Property = Property(name="nom", type=StringType)
Utilisateur2_age: Property = Property(name="age", type=IntegerType)
Utilisateur2_adresse: Property = Property(name="adresse", type=StringType)
Utilisateur2_photoDeProfil: Property = Property(name="photoDeProfil", type=StringType)
Utilisateur2.attributes={Utilisateur2_adresse, Utilisateur2_age, Utilisateur2_photoDeProfil, Utilisateur2_nom}

# V_hicule1 class attributes and methods
V_hicule1_imatriculation: Property = Property(name="imatriculation", type=StringType)
V_hicule1_modele: Property = Property(name="modele", type=StringType)
V_hicule1_marque: Property = Property(name="marque", type=StringType)
V_hicule1_propri_taire: Property = Property(name="propri_taire", type=Conducteur1)
V_hicule1_nbPlaces: Property = Property(name="nbPlaces", type=IntegerType)
V_hicule1.attributes={V_hicule1_imatriculation, V_hicule1_modele, V_hicule1_propri_taire, V_hicule1_marque, V_hicule1_nbPlaces}

# Conducteur1 class attributes and methods

# Passager1 class attributes and methods

# Avis2 class attributes and methods
Avis2_note: Property = Property(name="note", type=IntegerType)
Avis2_description: Property = Property(name="description", type=StringType)
Avis2.attributes={Avis2_note, Avis2_description}

# Lieu1 class attributes and methods

# Role class attributes and methods
Role_nbAvis: Property = Property(name="nbAvis", type=IntegerType)
Role.attributes={Role_nbAvis}

# ihm_Actor class attributes and methods

# Acteur_Actor class attributes and methods

# Contr_leur_Actor class attributes and methods

# Persistance_Actor class attributes and methods

# ihm class attributes and methods

# Contr_leur class attributes and methods

# Persistance class attributes and methods

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
Conducteur_V_hicule: BinaryAssociation = BinaryAssociation(
    name="Conducteur_V_hicule",
    ends={
        Property(name="v_hicule12", type=V_hicule1, multiplicity=Multiplicity(0, 9999)),
        Property(name="conducteur13", type=Conducteur1, multiplicity=Multiplicity(1, 1))
    }
)
Conducteur_Trajet: BinaryAssociation = BinaryAssociation(
    name="Conducteur_Trajet",
    ends={
        Property(name="trajet14", type=Trajet2, multiplicity=Multiplicity(0, 9999)),
        Property(name="conducteur15", type=Conducteur1, multiplicity=Multiplicity(1, 1))
    }
)
Utilisateur_Role: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Role",
    ends={
        Property(name="role16", type=Role, multiplicity=Multiplicity(1, 2)),
        Property(name="utilisateur17", type=Utilisateur2, multiplicity=Multiplicity(1, 1))
    }
)
Role_Avis: BinaryAssociation = BinaryAssociation(
    name="Role_Avis",
    ends={
        Property(name="avis18", type=Avis2, multiplicity=Multiplicity(0, 9999)),
        Property(name="role19", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
Lieu_Trajet: BinaryAssociation = BinaryAssociation(
    name="Lieu_Trajet",
    ends={
        Property(name="Arrivee20", type=Trajet2, multiplicity=Multiplicity(0, 9999)),
        Property(name="lieu21", type=Lieu1, multiplicity=Multiplicity(1, 1))
    }
)
Lieu_Trajet2: BinaryAssociation = BinaryAssociation(
    name="Lieu_Trajet2",
    ends={
        Property(name="Depart22", type=Trajet2, multiplicity=Multiplicity(0, 9999)),
        Property(name="lieu23", type=Lieu1, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EvAy8EGtEemokbRu9Ld3Pw",
    types={Class_, Personne, Avis, Utilisateur, Avis1, Voiture, Trajet, Trajet1, Utilisateur1, V_hicule, Lieu, Conducteur, Passager, Chemin_Interface, Trajet2, Utilisateur2, V_hicule1, Conducteur1, Passager1, Avis2, Lieu1, Role, ihm_Actor, Acteur_Actor, Contr_leur_Actor, Persistance_Actor, ihm, Contr_leur, Persistance, Personne2},
    associations={Personne_Avis, Trajet_Passager, V_hicule_Conducteur, Trajet_Conducteur, Personne_Trajet, Personne_Voiture, Conducteur_V_hicule, Conducteur_Trajet, Utilisateur_Role, Role_Avis, Lieu_Trajet, Lieu_Trajet2},
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
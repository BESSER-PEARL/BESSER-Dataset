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
domain_Role: Enumeration = Enumeration(
    name="domain_Role",
    literals={
            
    }
)

# Classes
domain_Profil = Class(name="domain_Profil")
domain_Voiture = Class(name="domain_Voiture")
domain_Authentification = Class(name="domain_Authentification")
domain_Trajet = Class(name="domain_Trajet")
domain_Ville = Class(name="domain_Ville")
domain_Avis = Class(name="domain_Avis")
domain_Reservation = Class(name="domain_Reservation")

# domain_Profil class attributes and methods
domain_Profil_id: Property = Property(name="id", type=IntegerType)
domain_Profil_nom: Property = Property(name="nom", type=StringType)
domain_Profil_prenom: Property = Property(name="prenom", type=StringType)
domain_Profil_tel: Property = Property(name="tel", type=StringType)
domain_Profil_mail: Property = Property(name="mail", type=StringType)
domain_Profil_role: Property = Property(name="role", type=domain_Role)
domain_Profil.attributes={domain_Profil_prenom, domain_Profil_mail, domain_Profil_role, domain_Profil_tel, domain_Profil_id, domain_Profil_nom}

# domain_Voiture class attributes and methods
domain_Voiture_id: Property = Property(name="id", type=IntegerType)
domain_Voiture_model: Property = Property(name="model", type=StringType)
domain_Voiture_marque: Property = Property(name="marque", type=StringType)
domain_Voiture_confort: Property = Property(name="confort", type=StringType)
domain_Voiture_nbPlaces: Property = Property(name="nbPlaces", type=IntegerType)
domain_Voiture_categorie: Property = Property(name="categorie", type=StringType)
domain_Voiture.attributes={domain_Voiture_confort, domain_Voiture_id, domain_Voiture_model, domain_Voiture_marque, domain_Voiture_categorie, domain_Voiture_nbPlaces}

# domain_Authentification class attributes and methods
domain_Authentification_id: Property = Property(name="id", type=StringType)
domain_Authentification_password: Property = Property(name="password", type=StringType)
domain_Authentification.attributes={domain_Authentification_password, domain_Authentification_id}

# domain_Trajet class attributes and methods
domain_Trajet_id: Property = Property(name="id", type=IntegerType)
domain_Trajet_date: Property = Property(name="date", type=DateType)
domain_Trajet_depart: Property = Property(name="depart", type=domain_Ville)
domain_Trajet_destination: Property = Property(name="destination", type=domain_Ville)
domain_Trajet_prix: Property = Property(name="prix", type=IntegerType)
domain_Trajet.attributes={domain_Trajet_depart, domain_Trajet_prix, domain_Trajet_id, domain_Trajet_destination, domain_Trajet_date}

# domain_Ville class attributes and methods
domain_Ville_id: Property = Property(name="id", type=IntegerType)
domain_Ville_nom: Property = Property(name="nom", type=StringType)
domain_Ville_cp: Property = Property(name="cp", type=IntegerType)
domain_Ville.attributes={domain_Ville_nom, domain_Ville_cp, domain_Ville_id}

# domain_Avis class attributes and methods
domain_Avis_commentaire: Property = Property(name="commentaire", type=StringType)
domain_Avis_note: Property = Property(name="note", type=IntegerType)
domain_Avis_id: Property = Property(name="id", type=IntegerType)
domain_Avis.attributes={domain_Avis_commentaire, domain_Avis_id, domain_Avis_note}

# domain_Reservation class attributes and methods
domain_Reservation_id2: Property = Property(name="id2", type=IntegerType)
domain_Reservation_id: Property = Property(name="id", type=IntegerType)
domain_Reservation_dateReservation: Property = Property(name="dateReservation", type=DateType)
domain_Reservation.attributes={domain_Reservation_id2, domain_Reservation_dateReservation, domain_Reservation_id}

# Relationships
Personne_Preferences: BinaryAssociation = BinaryAssociation(
    name="Personne_Preferences",
    ends={
        Property(name="Cr_e0", type=domain_Authentification, multiplicity=Multiplicity(1, 9999)),
        Property(name="personne1", type=domain_Profil, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Evenement: BinaryAssociation = BinaryAssociation(
    name="Personne_Evenement",
    ends={
        Property(name="events2", type=domain_Trajet, multiplicity=Multiplicity(0, 9999)),
        Property(name="participants3", type=domain_Profil, multiplicity=Multiplicity(1, 9999))
    }
)
Avis_Personne: BinaryAssociation = BinaryAssociation(
    name="Avis_Personne",
    ends={
        Property(name="personne4", type=domain_Profil, multiplicity=Multiplicity(0, 1)),
        Property(name="avis5", type=domain_Avis, multiplicity=Multiplicity(0, 9999))
    }
)
Avis_Evenement: BinaryAssociation = BinaryAssociation(
    name="Avis_Evenement",
    ends={
        Property(name="evenement6", type=domain_Trajet, multiplicity=Multiplicity(0, 1)),
        Property(name="avis7", type=domain_Avis, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Ville: BinaryAssociation = BinaryAssociation(
    name="Personne_Ville",
    ends={
        Property(name="adresse8", type=domain_Ville, multiplicity=Multiplicity(0, 1)),
        Property(name="personnes9", type=domain_Profil, multiplicity=Multiplicity(0, 9999))
    }
)
Ville_Trajet: BinaryAssociation = BinaryAssociation(
    name="Ville_Trajet",
    ends={
        Property(name="ville10", type=domain_Ville, multiplicity=Multiplicity(1, 1)),
        Property(name="trajet11", type=domain_Trajet, multiplicity=Multiplicity(1, 1))
    }
)
Profil_Reservation: BinaryAssociation = BinaryAssociation(
    name="Profil_Reservation",
    ends={
        Property(name="profil12", type=domain_Profil, multiplicity=Multiplicity(1, 9999)),
        Property(name="reservation13", type=domain_Reservation, multiplicity=Multiplicity(0, 1))
    }
)
Trajet_Reservation: BinaryAssociation = BinaryAssociation(
    name="Trajet_Reservation",
    ends={
        Property(name="trajet14", type=domain_Trajet, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation15", type=domain_Reservation, multiplicity=Multiplicity(1, 9999))
    }
)
Voiture_Passager: BinaryAssociation = BinaryAssociation(
    name="Voiture_Passager",
    ends={
        Property(name="voiture16", type=domain_Voiture, multiplicity=Multiplicity(0, 1)),
        Property(name="Profil17", type=domain_Profil, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_PTJYQI4yEeqwvcm2LAkYWA",
    types={domain_Profil, domain_Voiture, domain_Authentification, domain_Trajet, domain_Ville, domain_Avis, domain_Reservation, domain_Role},
    associations={Personne_Preferences, Personne_Evenement, Avis_Personne, Avis_Evenement, Personne_Ville, Ville_Trajet, Profil_Reservation, Trajet_Reservation, Voiture_Passager},
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
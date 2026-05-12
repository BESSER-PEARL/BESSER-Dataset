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
Covoiturage_Passager = Class(name="Covoiturage_Passager")
Covoiturage_Voiture = Class(name="Covoiturage_Voiture")
Covoiturage_Authentification = Class(name="Covoiturage_Authentification")
Covoiturage_Trajet = Class(name="Covoiturage_Trajet")
Covoiturage_Ville = Class(name="Covoiturage_Ville")
Covoiturage_Avis = Class(name="Covoiturage_Avis")
Covoiturage_Reservation = Class(name="Covoiturage_Reservation")
Covoiturage_Conducteur = Class(name="Covoiturage_Conducteur")
Covoiturage_Message = Class(name="Covoiturage_Message")

# Covoiturage_Passager class attributes and methods
Covoiturage_Passager_id: Property = Property(name="id", type=IntegerType)
Covoiturage_Passager_nom: Property = Property(name="nom", type=StringType)
Covoiturage_Passager_prenom: Property = Property(name="prenom", type=StringType)
Covoiturage_Passager_tel: Property = Property(name="tel", type=IntegerType)
Covoiturage_Passager_mail: Property = Property(name="mail", type=StringType)
Covoiturage_Passager.attributes={Covoiturage_Passager_mail, Covoiturage_Passager_id, Covoiturage_Passager_prenom, Covoiturage_Passager_nom, Covoiturage_Passager_tel}

# Covoiturage_Voiture class attributes and methods
Covoiturage_Voiture_id: Property = Property(name="id", type=IntegerType)
Covoiturage_Voiture_model: Property = Property(name="model", type=StringType)
Covoiturage_Voiture_marque: Property = Property(name="marque", type=StringType)
Covoiturage_Voiture_confort: Property = Property(name="confort", type=StringType)
Covoiturage_Voiture_nbPlaces: Property = Property(name="nbPlaces", type=IntegerType)
Covoiturage_Voiture_categorie: Property = Property(name="categorie", type=StringType)
Covoiturage_Voiture_attribute: Property = Property(name="attribute", type=StringType)
Covoiturage_Voiture.attributes={Covoiturage_Voiture_marque, Covoiturage_Voiture_categorie, Covoiturage_Voiture_confort, Covoiturage_Voiture_model, Covoiturage_Voiture_nbPlaces, Covoiturage_Voiture_id, Covoiturage_Voiture_attribute}

# Covoiturage_Authentification class attributes and methods
Covoiturage_Authentification_id: Property = Property(name="id", type=StringType)
Covoiturage_Authentification_password: Property = Property(name="password", type=StringType)
Covoiturage_Authentification.attributes={Covoiturage_Authentification_password, Covoiturage_Authentification_id}

# Covoiturage_Trajet class attributes and methods
Covoiturage_Trajet_id: Property = Property(name="id", type=IntegerType)
Covoiturage_Trajet_date: Property = Property(name="date", type=DateType)
Covoiturage_Trajet_depart: Property = Property(name="depart", type=Covoiturage_Ville)
Covoiturage_Trajet_destination: Property = Property(name="destination", type=Covoiturage_Ville)
Covoiturage_Trajet_prix: Property = Property(name="prix", type=IntegerType)
Covoiturage_Trajet_etat: Property = Property(name="etat", type=BooleanType)
Covoiturage_Trajet.attributes={Covoiturage_Trajet_destination, Covoiturage_Trajet_depart, Covoiturage_Trajet_id, Covoiturage_Trajet_prix, Covoiturage_Trajet_date, Covoiturage_Trajet_etat}

# Covoiturage_Ville class attributes and methods
Covoiturage_Ville_id: Property = Property(name="id", type=IntegerType)
Covoiturage_Ville_nom: Property = Property(name="nom", type=StringType)
Covoiturage_Ville_cp: Property = Property(name="cp", type=IntegerType)
Covoiturage_Ville.attributes={Covoiturage_Ville_cp, Covoiturage_Ville_id, Covoiturage_Ville_nom}

# Covoiturage_Avis class attributes and methods
Covoiturage_Avis_id: Property = Property(name="id", type=IntegerType)
Covoiturage_Avis_commentaire: Property = Property(name="commentaire", type=StringType)
Covoiturage_Avis_note: Property = Property(name="note", type=IntegerType)
Covoiturage_Avis.attributes={Covoiturage_Avis_id, Covoiturage_Avis_note, Covoiturage_Avis_commentaire}

# Covoiturage_Reservation class attributes and methods
Covoiturage_Reservation_id2: Property = Property(name="id2", type=IntegerType)
Covoiturage_Reservation_id: Property = Property(name="id", type=IntegerType)
Covoiturage_Reservation_dateReservation: Property = Property(name="dateReservation", type=DateType)
Covoiturage_Reservation_etat: Property = Property(name="etat", type=BooleanType)
Covoiturage_Reservation.attributes={Covoiturage_Reservation_id, Covoiturage_Reservation_etat, Covoiturage_Reservation_dateReservation, Covoiturage_Reservation_id2}

# Covoiturage_Conducteur class attributes and methods
Covoiturage_Conducteur_datePermi: Property = Property(name="datePermi", type=StringType)
Covoiturage_Conducteur.attributes={Covoiturage_Conducteur_datePermi}

# Covoiturage_Message class attributes and methods
Covoiturage_Message_Id: Property = Property(name="Id", type=StringType)
Covoiturage_Message_Value: Property = Property(name="Value", type=StringType)
Covoiturage_Message.attributes={Covoiturage_Message_Value, Covoiturage_Message_Id}

# Relationships
Personne_Preferences: BinaryAssociation = BinaryAssociation(
    name="Personne_Preferences",
    ends={
        Property(name="s_authentifi_0", type=Covoiturage_Authentification, multiplicity=Multiplicity(1, 1)),
        Property(name="personne1", type=Covoiturage_Passager, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Evenement: BinaryAssociation = BinaryAssociation(
    name="Personne_Evenement",
    ends={
        Property(name="trajet2", type=Covoiturage_Trajet, multiplicity=Multiplicity(0, 9999)),
        Property(name="participants3", type=Covoiturage_Conducteur, multiplicity=Multiplicity(1, 1))
    }
)
Avis_Personne: BinaryAssociation = BinaryAssociation(
    name="Avis_Personne",
    ends={
        Property(name="personne4", type=Covoiturage_Passager, multiplicity=Multiplicity(0, 1)),
        Property(name="avis5", type=Covoiturage_Avis, multiplicity=Multiplicity(0, 9999))
    }
)
Avis_Evenement: BinaryAssociation = BinaryAssociation(
    name="Avis_Evenement",
    ends={
        Property(name="evenement6", type=Covoiturage_Trajet, multiplicity=Multiplicity(0, 1)),
        Property(name="avis7", type=Covoiturage_Avis, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Ville: BinaryAssociation = BinaryAssociation(
    name="Personne_Ville",
    ends={
        Property(name="adresse8", type=Covoiturage_Ville, multiplicity=Multiplicity(1, 1)),
        Property(name="personnes9", type=Covoiturage_Passager, multiplicity=Multiplicity(0, 9999))
    }
)
Ville_Trajet: BinaryAssociation = BinaryAssociation(
    name="Ville_Trajet",
    ends={
        Property(name="ville10", type=Covoiturage_Ville, multiplicity=Multiplicity(1, 1)),
        Property(name="trajet11", type=Covoiturage_Trajet, multiplicity=Multiplicity(1, 9999))
    }
)
Profil_Reservation: BinaryAssociation = BinaryAssociation(
    name="Profil_Reservation",
    ends={
        Property(name="profil12", type=Covoiturage_Passager, multiplicity=Multiplicity(1, 9999)),
        Property(name="reservation13", type=Covoiturage_Reservation, multiplicity=Multiplicity(0, 1))
    }
)
Trajet_Reservation: BinaryAssociation = BinaryAssociation(
    name="Trajet_Reservation",
    ends={
        Property(name="trajet14", type=Covoiturage_Trajet, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation15", type=Covoiturage_Reservation, multiplicity=Multiplicity(1, 9999))
    }
)
Voiture_Passager: BinaryAssociation = BinaryAssociation(
    name="Voiture_Passager",
    ends={
        Property(name="voiture16", type=Covoiturage_Voiture, multiplicity=Multiplicity(1, 1)),
        Property(name="Profil17", type=Covoiturage_Conducteur, multiplicity=Multiplicity(1, 1))
    }
)
Passager_Message: BinaryAssociation = BinaryAssociation(
    name="Passager_Message",
    ends={
        Property(name="passager18", type=Covoiturage_Passager, multiplicity=Multiplicity(1, 1)),
        Property(name="message19", type=Covoiturage_Message, multiplicity=Multiplicity(0, 9999))
    }
)
Voiture_Trajet: BinaryAssociation = BinaryAssociation(
    name="Voiture_Trajet",
    ends={
        Property(name="voiture20", type=Covoiturage_Voiture, multiplicity=Multiplicity(1, 1)),
        Property(name="trajet21", type=Covoiturage_Trajet, multiplicity=Multiplicity(1, 9999))
    }
)
Trajet_Passager: BinaryAssociation = BinaryAssociation(
    name="Trajet_Passager",
    ends={
        Property(name="trajet22", type=Covoiturage_Trajet, multiplicity=Multiplicity(0, 9999)),
        Property(name="passager23", type=Covoiturage_Passager, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6xWGII5HEeqwvcm2LAkYWA",
    types={Covoiturage_Passager, Covoiturage_Voiture, Covoiturage_Authentification, Covoiturage_Trajet, Covoiturage_Ville, Covoiturage_Avis, Covoiturage_Reservation, Covoiturage_Conducteur, Covoiturage_Message},
    associations={Personne_Preferences, Personne_Evenement, Avis_Personne, Avis_Evenement, Personne_Ville, Ville_Trajet, Profil_Reservation, Trajet_Reservation, Voiture_Passager, Passager_Message, Voiture_Trajet, Trajet_Passager},
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
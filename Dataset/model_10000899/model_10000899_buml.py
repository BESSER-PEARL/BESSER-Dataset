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
covoiturage_Personne = Class(name="covoiturage_Personne")
covoiturage_Voiture = Class(name="covoiturage_Voiture")
covoiturage_Preferences = Class(name="covoiturage_Preferences")
covoiturage_Reservations = Class(name="covoiturage_Reservations")
covoiturage_Ville = Class(name="covoiturage_Ville")
covoiturage_Avis = Class(name="covoiturage_Avis")
Admin_Admin_Actor = Class(name="Admin_Admin_Actor")
Admin_consulter_liste_utilis_UseCase = Class(name="Admin_consulter_liste_utilis_UseCase")
Admin_modifier_utilis_UseCase = Class(name="Admin_modifier_utilis_UseCase")
Admin_suppr_utils_UseCase = Class(name="Admin_suppr_utils_UseCase")
Admin_consulter_trajets_UseCase = Class(name="Admin_consulter_trajets_UseCase")
Admin_UseCase5_UseCase = Class(name="Admin_UseCase5_UseCase")
Admin_s_inscrire_UseCase = Class(name="Admin_s_inscrire_UseCase")
Admin_Passager___conducteur_Actor = Class(name="Admin_Passager___conducteur_Actor")
Admin_add_trajet_UseCase = Class(name="Admin_add_trajet_UseCase")

# covoiturage_Personne class attributes and methods
covoiturage_Personne_id: Property = Property(name="id", type=IntegerType)
covoiturage_Personne_nom: Property = Property(name="nom", type=StringType)
covoiturage_Personne_prenom: Property = Property(name="prenom", type=StringType)
covoiturage_Personne_tel: Property = Property(name="tel", type=StringType)
covoiturage_Personne_mail: Property = Property(name="mail", type=StringType)
covoiturage_Personne.attributes={covoiturage_Personne_mail, covoiturage_Personne_tel, covoiturage_Personne_prenom, covoiturage_Personne_id, covoiturage_Personne_nom}

# covoiturage_Voiture class attributes and methods
covoiturage_Voiture_id: Property = Property(name="id", type=IntegerType)
covoiturage_Voiture_categorie: Property = Property(name="categorie", type=StringType)
covoiturage_Voiture_marque: Property = Property(name="marque", type=StringType)
covoiturage_Voiture_model: Property = Property(name="model", type=StringType)
covoiturage_Voiture_confort: Property = Property(name="confort", type=StringType)
covoiturage_Voiture_couleur: Property = Property(name="couleur", type=StringType)
covoiturage_Voiture_nbPlaces: Property = Property(name="nbPlaces", type=IntegerType)
covoiturage_Voiture_climatiseur: Property = Property(name="climatiseur", type=BooleanType)
covoiturage_Voiture_tabac: Property = Property(name="tabac", type=BooleanType)
covoiturage_Voiture.attributes={covoiturage_Voiture_confort, covoiturage_Voiture_couleur, covoiturage_Voiture_nbPlaces, covoiturage_Voiture_climatiseur, covoiturage_Voiture_marque, covoiturage_Voiture_id, covoiturage_Voiture_model, covoiturage_Voiture_tabac, covoiturage_Voiture_categorie}

# covoiturage_Preferences class attributes and methods
covoiturage_Preferences_id: Property = Property(name="id", type=IntegerType)
covoiturage_Preferences_nomPref: Property = Property(name="nomPref", type=StringType)
covoiturage_Preferences_valeur: Property = Property(name="valeur", type=StringType)
covoiturage_Preferences.attributes={covoiturage_Preferences_id, covoiturage_Preferences_nomPref, covoiturage_Preferences_valeur}

# covoiturage_Reservations class attributes and methods
covoiturage_Reservations_id: Property = Property(name="id", type=IntegerType)
covoiturage_Reservations_date: Property = Property(name="date", type=DateType)
covoiturage_Reservations_lieuDeDepose: Property = Property(name="lieuDeDepose", type=StringType)
covoiturage_Reservations_prix: Property = Property(name="prix", type=IntegerType)
covoiturage_Reservations.attributes={covoiturage_Reservations_date, covoiturage_Reservations_prix, covoiturage_Reservations_id, covoiturage_Reservations_lieuDeDepose}

# covoiturage_Ville class attributes and methods
covoiturage_Ville_id: Property = Property(name="id", type=IntegerType)
covoiturage_Ville_nom: Property = Property(name="nom", type=StringType)
covoiturage_Ville_cp: Property = Property(name="cp", type=StringType)
covoiturage_Ville.attributes={covoiturage_Ville_nom, covoiturage_Ville_cp, covoiturage_Ville_id}

# covoiturage_Avis class attributes and methods
covoiturage_Avis_id: Property = Property(name="id", type=IntegerType)
covoiturage_Avis_commentaire: Property = Property(name="commentaire", type=StringType)
covoiturage_Avis_note: Property = Property(name="note", type=IntegerType)
covoiturage_Avis.attributes={covoiturage_Avis_id, covoiturage_Avis_commentaire, covoiturage_Avis_note}

# Admin_Admin_Actor class attributes and methods

# Admin_consulter_liste_utilis_UseCase class attributes and methods

# Admin_modifier_utilis_UseCase class attributes and methods

# Admin_suppr_utils_UseCase class attributes and methods

# Admin_consulter_trajets_UseCase class attributes and methods

# Admin_UseCase5_UseCase class attributes and methods

# Admin_s_inscrire_UseCase class attributes and methods

# Admin_Passager___conducteur_Actor class attributes and methods

# Admin_add_trajet_UseCase class attributes and methods

# Relationships
Personne_Voiture: BinaryAssociation = BinaryAssociation(
    name="Personne_Voiture",
    ends={
        Property(name="voiture0", type=covoiturage_Voiture, multiplicity=Multiplicity(0, 1)),
        Property(name="personne1", type=covoiturage_Personne, multiplicity=Multiplicity(1, 1))
    }
)
Personne_Preferences: BinaryAssociation = BinaryAssociation(
    name="Personne_Preferences",
    ends={
        Property(name="preferences2", type=covoiturage_Preferences, multiplicity=Multiplicity(1, 9999)),
        Property(name="personne3", type=covoiturage_Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Evenement_Ville: BinaryAssociation = BinaryAssociation(
    name="Evenement_Ville",
    ends={
        Property(name="villes4", type=covoiturage_Ville, multiplicity=Multiplicity(1, 9999)),
        Property(name="evenement5", type=covoiturage_Reservations, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Evenement: BinaryAssociation = BinaryAssociation(
    name="Personne_Evenement",
    ends={
        Property(name="events6", type=covoiturage_Reservations, multiplicity=Multiplicity(0, 9999)),
        Property(name="participants7", type=covoiturage_Personne, multiplicity=Multiplicity(1, 9999))
    }
)
Avis_Personne: BinaryAssociation = BinaryAssociation(
    name="Avis_Personne",
    ends={
        Property(name="personne8", type=covoiturage_Personne, multiplicity=Multiplicity(0, 1)),
        Property(name="avis9", type=covoiturage_Avis, multiplicity=Multiplicity(0, 9999))
    }
)
Avis_Evenement: BinaryAssociation = BinaryAssociation(
    name="Avis_Evenement",
    ends={
        Property(name="evenement10", type=covoiturage_Reservations, multiplicity=Multiplicity(0, 1)),
        Property(name="avis11", type=covoiturage_Avis, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Ville: BinaryAssociation = BinaryAssociation(
    name="Personne_Ville",
    ends={
        Property(name="adresse12", type=covoiturage_Ville, multiplicity=Multiplicity(0, 1)),
        Property(name="personnes13", type=covoiturage_Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase14", type=Admin_consulter_liste_utilis_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor15", type=Admin_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase2: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase2",
    ends={
        Property(name="useCase216", type=Admin_modifier_utilis_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor17", type=Admin_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase3: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase3",
    ends={
        Property(name="useCase318", type=Admin_suppr_utils_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor19", type=Admin_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase4: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase4",
    ends={
        Property(name="useCase420", type=Admin_consulter_trajets_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor21", type=Admin_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Actor_UseCase5: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase5",
    ends={
        Property(name="useCase522", type=Admin_UseCase5_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor23", type=Admin_Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
UseCase6_Actor2: BinaryAssociation = BinaryAssociation(
    name="UseCase6_Actor2",
    ends={
        Property(name="actor224", type=Admin_Passager___conducteur_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="useCase625", type=Admin_s_inscrire_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6d314461_b8d2_460d_aa88_2cfe13181116",
    types={covoiturage_Personne, covoiturage_Voiture, covoiturage_Preferences, covoiturage_Reservations, covoiturage_Ville, covoiturage_Avis, Admin_Admin_Actor, Admin_consulter_liste_utilis_UseCase, Admin_modifier_utilis_UseCase, Admin_suppr_utils_UseCase, Admin_consulter_trajets_UseCase, Admin_UseCase5_UseCase, Admin_s_inscrire_UseCase, Admin_Passager___conducteur_Actor, Admin_add_trajet_UseCase},
    associations={Personne_Voiture, Personne_Preferences, Evenement_Ville, Personne_Evenement, Avis_Personne, Avis_Evenement, Personne_Ville, Actor_UseCase, Actor_UseCase2, Actor_UseCase3, Actor_UseCase4, Actor_UseCase5, UseCase6_Actor2},
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
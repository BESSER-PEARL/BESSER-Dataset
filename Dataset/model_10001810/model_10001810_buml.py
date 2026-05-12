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
Utilisateur = Class(name="Utilisateur")
Class_ = Class(name="Class")
Commande = Class(name="Commande")
Etat = Class(name="Etat")
Adresse = Class(name="Adresse")
Livraison = Class(name="Livraison")
Stock = Class(name="Stock")
Ingr_dient = Class(name="Ingr_dient")
Cat_gorie = Class(name="Cat_gorie")
Recette = Class(name="Recette")
Produit = Class(name="Produit")
R_le = Class(name="R_le")
Pizzeria = Class(name="Pizzeria")

# Utilisateur class attributes and methods
Utilisateur_id: Property = Property(name="id", type=IntegerType)
Utilisateur_nom: Property = Property(name="nom", type=StringType)
Utilisateur_prenom: Property = Property(name="prenom", type=StringType)
Utilisateur_civilit_: Property = Property(name="civilit_", type=StringType)
Utilisateur_date_naissance: Property = Property(name="date_naissance", type=StringType)
Utilisateur_email: Property = Property(name="email", type=StringType)
Utilisateur_mot_de_passe: Property = Property(name="mot_de_passe", type=StringType)
Utilisateur_role_id: Property = Property(name="role_id", type=IntegerType)
Utilisateur_pizzeria_id: Property = Property(name="pizzeria_id", type=IntegerType)
Utilisateur.attributes={Utilisateur_id, Utilisateur_prenom, Utilisateur_email, Utilisateur_date_naissance, Utilisateur_mot_de_passe, Utilisateur_nom, Utilisateur_role_id, Utilisateur_pizzeria_id, Utilisateur_civilit_}

# Class class attributes and methods

# Commande class attributes and methods
Commande_id: Property = Property(name="id", type=IntegerType)
Commande_utilisateur_id: Property = Property(name="utilisateur_id", type=IntegerType)
Commande_date: Property = Property(name="date", type=IntegerType)
Commande_paiement: Property = Property(name="paiement", type=StringType)
Commande__tat: Property = Property(name="_tat", type=IntegerType)
Commande.attributes={Commande_id, Commande_date, Commande__tat, Commande_paiement, Commande_utilisateur_id}

# Etat class attributes and methods
Etat_id: Property = Property(name="id", type=IntegerType)
Etat_nom: Property = Property(name="nom", type=StringType)
Etat_verrouillage: Property = Property(name="verrouillage", type=BooleanType)
Etat.attributes={Etat_nom, Etat_id, Etat_verrouillage}

# Adresse class attributes and methods
Adresse_id: Property = Property(name="id", type=IntegerType)
Adresse_utilisateur_id: Property = Property(name="utilisateur_id", type=IntegerType)
Adresse_voie: Property = Property(name="voie", type=StringType)
Adresse_num_ro: Property = Property(name="num_ro", type=IntegerType)
Adresse_ville: Property = Property(name="ville", type=StringType)
Adresse_code_postal: Property = Property(name="code_postal", type=IntegerType)
Adresse_t_l_phone: Property = Property(name="t_l_phone", type=StringType)
Adresse_geocode: Property = Property(name="geocode", type=StringType)
Adresse.attributes={Adresse_t_l_phone, Adresse_voie, Adresse_id, Adresse_utilisateur_id, Adresse_num_ro, Adresse_geocode, Adresse_ville, Adresse_code_postal}

# Livraison class attributes and methods
Livraison_id: Property = Property(name="id", type=IntegerType)
Livraison_commande_id: Property = Property(name="commande_id", type=IntegerType)
Livraison_livreur_id: Property = Property(name="livreur_id", type=IntegerType)
Livraison_client_id: Property = Property(name="client_id", type=IntegerType)
Livraison_geocode: Property = Property(name="geocode", type=StringType)
Livraison.attributes={Livraison_geocode, Livraison_id, Livraison_livreur_id, Livraison_commande_id, Livraison_client_id}

# Stock class attributes and methods
Stock_ingredient_id: Property = Property(name="ingredient_id", type=IntegerType)
Stock_quantit_: Property = Property(name="quantit_", type=IntegerType)
Stock_date_modification: Property = Property(name="date_modification", type=IntegerType)
Stock_disponibilit_: Property = Property(name="disponibilit_", type=BooleanType)
Stock.attributes={Stock_ingredient_id, Stock_date_modification, Stock_disponibilit_, Stock_quantit_}

# Ingr_dient class attributes and methods
Ingr_dient_id: Property = Property(name="id", type=IntegerType)
Ingr_dient_nom: Property = Property(name="nom", type=StringType)
Ingr_dient_poids: Property = Property(name="poids", type=StringType)
Ingr_dient_unit_: Property = Property(name="unit_", type=StringType)
Ingr_dient.attributes={Ingr_dient_poids, Ingr_dient_nom, Ingr_dient_id, Ingr_dient_unit_}

# Cat_gorie class attributes and methods
Cat_gorie_id: Property = Property(name="id", type=IntegerType)
Cat_gorie_nom: Property = Property(name="nom", type=StringType)
Cat_gorie.attributes={Cat_gorie_nom, Cat_gorie_id}

# Recette class attributes and methods
Recette_id: Property = Property(name="id", type=IntegerType)
Recette_produit_id: Property = Property(name="produit_id", type=IntegerType)
Recette.attributes={Recette_produit_id, Recette_id}

# Produit class attributes and methods
Produit_id: Property = Property(name="id", type=IntegerType)
Produit_nom: Property = Property(name="nom", type=StringType)
Produit_categorie_id: Property = Property(name="categorie_id", type=IntegerType)
Produit_prix: Property = Property(name="prix", type=StringType)
Produit.attributes={Produit_categorie_id, Produit_id, Produit_prix, Produit_nom}

# R_le class attributes and methods
R_le_id: Property = Property(name="id", type=IntegerType)
R_le_type: Property = Property(name="type", type=StringType)
R_le.attributes={R_le_id, R_le_type}

# Pizzeria class attributes and methods
Pizzeria_id: Property = Property(name="id", type=IntegerType)
Pizzeria_adresse_id: Property = Property(name="adresse_id", type=IntegerType)
Pizzeria_nom: Property = Property(name="nom", type=StringType)
Pizzeria.attributes={Pizzeria_nom, Pizzeria_adresse_id, Pizzeria_id}

# Relationships
Utilisateur_R_le: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_R_le",
    ends={
        Property(name="Utilisateur_R_le_00", type=R_le, multiplicity=Multiplicity(1, 1)),
        Property(name="Utilisateur_R_le_11", type=Utilisateur, multiplicity=Multiplicity(1, 9999))
    }
)
Produit_Recette: BinaryAssociation = BinaryAssociation(
    name="Produit_Recette",
    ends={
        Property(name="Produit_Recette_02", type=Recette, multiplicity=Multiplicity(1, 1)),
        Property(name="Produit_Recette_13", type=Produit, multiplicity=Multiplicity(1, 1))
    }
)
Produit_Cat_gorie: BinaryAssociation = BinaryAssociation(
    name="Produit_Cat_gorie",
    ends={
        Property(name="Produit_Cat_gorie_04", type=Cat_gorie, multiplicity=Multiplicity(1, 1)),
        Property(name="Produit_Cat_gorie_15", type=Produit, multiplicity=Multiplicity(1, 9999))
    }
)
Commande_Utilisateur: BinaryAssociation = BinaryAssociation(
    name="Commande_Utilisateur",
    ends={
        Property(name="Commande_Utilisateur_06", type=Utilisateur, multiplicity=Multiplicity(0, 1)),
        Property(name="Commande_Utilisateur_17", type=Commande, multiplicity=Multiplicity(0, 1))
    }
)
Stock_Ingr_dient: BinaryAssociation = BinaryAssociation(
    name="Stock_Ingr_dient",
    ends={
        Property(name="Stock_Ingr_dient_08", type=Ingr_dient, multiplicity=Multiplicity(1, 1)),
        Property(name="Stock_Ingr_dient_19", type=Stock, multiplicity=Multiplicity(1, 1))
    }
)
Pizzeria_Adresse: BinaryAssociation = BinaryAssociation(
    name="Pizzeria_Adresse",
    ends={
        Property(name="Pizzeria_Adresse_018", type=Adresse, multiplicity=Multiplicity(1, 1)),
        Property(name="Pizzeria_Adresse_119", type=Pizzeria, multiplicity=Multiplicity(1, 1))
    }
)
Livraison_Utilisateur2: BinaryAssociation = BinaryAssociation(
    name="Livraison_Utilisateur2",
    ends={
        Property(name="Livraison_Utilisateur2_020", type=Utilisateur, multiplicity=Multiplicity(1, 1)),
        Property(name="client21", type=Livraison, multiplicity=Multiplicity(1, 9999))
    }
)
Etat_Commande: BinaryAssociation = BinaryAssociation(
    name="Etat_Commande",
    ends={
        Property(name="Etat_Commande_010", type=Commande, multiplicity=Multiplicity(0, 1)),
        Property(name="Etat_Commande_111", type=Etat, multiplicity=Multiplicity(0, 1))
    }
)
Livraison_Utilisateur: BinaryAssociation = BinaryAssociation(
    name="Livraison_Utilisateur",
    ends={
        Property(name="Livraison_Utilisateur_012", type=Utilisateur, multiplicity=Multiplicity(1, 1)),
        Property(name="livreur13", type=Livraison, multiplicity=Multiplicity(1, 9999))
    }
)
Livraison_Commande: BinaryAssociation = BinaryAssociation(
    name="Livraison_Commande",
    ends={
        Property(name="Livraison_Commande_014", type=Commande, multiplicity=Multiplicity(0, 1)),
        Property(name="Livraison_Commande_115", type=Livraison, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_Pizzeria: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Pizzeria",
    ends={
        Property(name="Utilisateur_Pizzeria_016", type=Pizzeria, multiplicity=Multiplicity(0, 1)),
        Property(name="Utilisateur_Pizzeria_117", type=Utilisateur, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_XMgioP1JEeiqaPjcVWadXw",
    types={Utilisateur, Class_, Commande, Etat, Adresse, Livraison, Stock, Ingr_dient, Cat_gorie, Recette, Produit, R_le, Pizzeria},
    associations={Utilisateur_R_le, Produit_Recette, Produit_Cat_gorie, Commande_Utilisateur, Stock_Ingr_dient, Pizzeria_Adresse, Livraison_Utilisateur2, Etat_Commande, Livraison_Utilisateur, Livraison_Commande, Utilisateur_Pizzeria},
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
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
Date_trajet = Class(name="Date_trajet")
Utilisateur_anonyme_Actor = Class(name="Utilisateur_anonyme_Actor")
Proposition_de_voyage_UseCase = Class(name="Proposition_de_voyage_UseCase")
Administrateur_Actor = Class(name="Administrateur_Actor")
S_enregistre_UseCase = Class(name="S_enregistre_UseCase")
Passager__Actor = Class(name="Passager__Actor")
Conducteur_Actor = Class(name="Conducteur_Actor")
Enregistre_son_vehicule_UseCase = Class(name="Enregistre_son_vehicule_UseCase")
S_authentifier_UseCase = Class(name="S_authentifier_UseCase")
Choisi_un_voyage_UseCase = Class(name="Choisi_un_voyage_UseCase")
Administre_UseCase = Class(name="Administre_UseCase")
Reserve_voyage_UseCase = Class(name="Reserve_voyage_UseCase")
confirme_voyage_UseCase = Class(name="confirme_voyage_UseCase")
Valide_embarquement_UseCase = Class(name="Valide_embarquement_UseCase")
Valide_arriv__UseCase = Class(name="Valide_arriv__UseCase")
Effectue_un_paiement_UseCase = Class(name="Effectue_un_paiement_UseCase")

# Utilisateur class attributes and methods
Utilisateur_id_utilisateur: Property = Property(name="id_utilisateur", type=IntegerType)
Utilisateur_Nom: Property = Property(name="Nom", type=StringType)
Utilisateur_Pr_nom: Property = Property(name="Pr_nom", type=StringType)
Utilisateur_Login: Property = Property(name="Login", type=StringType)
Utilisateur_Password: Property = Property(name="Password", type=StringType)
Utilisateur_Mail: Property = Property(name="Mail", type=StringType)
Utilisateur_Telephone: Property = Property(name="Telephone", type=StringType)
Utilisateur.attributes={Utilisateur_Login, Utilisateur_Pr_nom, Utilisateur_Telephone, Utilisateur_id_utilisateur, Utilisateur_Mail, Utilisateur_Nom, Utilisateur_Password}

# Date_trajet class attributes and methods
Date_trajet_id_date: Property = Property(name="id_date", type=IntegerType)
Date_trajet_Jour: Property = Property(name="Jour", type=StringType)
Date_trajet_Type_date: Property = Property(name="Type_date", type=StringType)
Date_trajet_Date___heure__minute: Property = Property(name="Date___heure__minute", type=StringType)
Date_trajet.attributes={Date_trajet_Type_date, Date_trajet_Date___heure__minute, Date_trajet_id_date, Date_trajet_Jour}

# Utilisateur_anonyme_Actor class attributes and methods

# Proposition_de_voyage_UseCase class attributes and methods

# Administrateur_Actor class attributes and methods

# S_enregistre_UseCase class attributes and methods

# Passager__Actor class attributes and methods

# Conducteur_Actor class attributes and methods

# Enregistre_son_vehicule_UseCase class attributes and methods

# S_authentifier_UseCase class attributes and methods

# Choisi_un_voyage_UseCase class attributes and methods

# Administre_UseCase class attributes and methods

# Reserve_voyage_UseCase class attributes and methods

# confirme_voyage_UseCase class attributes and methods

# Valide_embarquement_UseCase class attributes and methods

# Valide_arriv__UseCase class attributes and methods

# Effectue_un_paiement_UseCase class attributes and methods

# Relationships
Utilisateur_S_enregistre: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_S_enregistre",
    ends={
        Property(name="s_enregistre0", type=S_enregistre_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="utilisateur1", type=Utilisateur_anonyme_Actor, multiplicity=Multiplicity(0, 1))
    }
)
S_enregistre_Passager: BinaryAssociation = BinaryAssociation(
    name="S_enregistre_Passager",
    ends={
        Property(name="passager2", type=Passager__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="s_enregistre3", type=S_enregistre_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
S_enregistre_Conducteur: BinaryAssociation = BinaryAssociation(
    name="S_enregistre_Conducteur",
    ends={
        Property(name="conducteur4", type=Conducteur_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="s_enregistre5", type=S_enregistre_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Conducteur_Proposition_de_voyage: BinaryAssociation = BinaryAssociation(
    name="Conducteur_Proposition_de_voyage",
    ends={
        Property(name="proposition_de_voyage6", type=Proposition_de_voyage_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="conducteur7", type=Conducteur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Conducteur_Enregistre_son_vehicule: BinaryAssociation = BinaryAssociation(
    name="Conducteur_Enregistre_son_vehicule",
    ends={
        Property(name="enregistre_son_vehicule8", type=Enregistre_son_vehicule_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="conducteur9", type=Conducteur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_anonyme_S_authentifier: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_anonyme_S_authentifier",
    ends={
        Property(name="s_authentifier10", type=S_authentifier_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="utilisateur_anonyme11", type=Utilisateur_anonyme_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passager__Choisi_un_voyage: BinaryAssociation = BinaryAssociation(
    name="Passager__Choisi_un_voyage",
    ends={
        Property(name="choisi_un_voyage12", type=Choisi_un_voyage_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="passager13", type=Passager__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrateur_Administre: BinaryAssociation = BinaryAssociation(
    name="Administrateur_Administre",
    ends={
        Property(name="administre14", type=Administre_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrateur15", type=Administrateur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passager__Reserve_voyage: BinaryAssociation = BinaryAssociation(
    name="Passager__Reserve_voyage",
    ends={
        Property(name="reserve_voyage16", type=Reserve_voyage_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="passager17", type=Passager__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Conducteur_confirme_voyage: BinaryAssociation = BinaryAssociation(
    name="Conducteur_confirme_voyage",
    ends={
        Property(name="confirme_voyage18", type=confirme_voyage_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="conducteur19", type=Conducteur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Conducteur_Valide_embarquement: BinaryAssociation = BinaryAssociation(
    name="Conducteur_Valide_embarquement",
    ends={
        Property(name="valide_embarquement20", type=Valide_embarquement_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="conducteur21", type=Conducteur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passager__Effectue_un_paiement: BinaryAssociation = BinaryAssociation(
    name="Passager__Effectue_un_paiement",
    ends={
        Property(name="effectue_un_paiement22", type=Effectue_un_paiement_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="passager23", type=Passager__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Conducteur_Valide_arriv_: BinaryAssociation = BinaryAssociation(
    name="Conducteur_Valide_arriv_",
    ends={
        Property(name="valide_arriv_24", type=Valide_arriv__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="conducteur25", type=Conducteur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passager__Valide_arriv_: BinaryAssociation = BinaryAssociation(
    name="Passager__Valide_arriv_",
    ends={
        Property(name="valide_arriv_26", type=Valide_arriv__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="passager27", type=Passager__Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JzatQFqhEemzpo5ZYvX8TA",
    types={Utilisateur, Date_trajet, Utilisateur_anonyme_Actor, Proposition_de_voyage_UseCase, Administrateur_Actor, S_enregistre_UseCase, Passager__Actor, Conducteur_Actor, Enregistre_son_vehicule_UseCase, S_authentifier_UseCase, Choisi_un_voyage_UseCase, Administre_UseCase, Reserve_voyage_UseCase, confirme_voyage_UseCase, Valide_embarquement_UseCase, Valide_arriv__UseCase, Effectue_un_paiement_UseCase},
    associations={Utilisateur_S_enregistre, S_enregistre_Passager, S_enregistre_Conducteur, Conducteur_Proposition_de_voyage, Conducteur_Enregistre_son_vehicule, Utilisateur_anonyme_S_authentifier, Passager__Choisi_un_voyage, Administrateur_Administre, Passager__Reserve_voyage, Conducteur_confirme_voyage, Conducteur_Valide_embarquement, Passager__Effectue_un_paiement, Conducteur_Valide_arriv_, Passager__Valide_arriv_},
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
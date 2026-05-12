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
Client = Class(name="Client")
Formation = Class(name="Formation")
DevisEntete = Class(name="DevisEntete")
Facture = Class(name="Facture")
Convention = Class(name="Convention")
Type = Class(name="Type")
Prestation = Class(name="Prestation")
Formateur = Class(name="Formateur")
Participant = Class(name="Participant")

# Client class attributes and methods
Client_nom: Property = Property(name="nom", type=StringType)
Client_adresse: Property = Property(name="adresse", type=StringType)
Client_codePostal: Property = Property(name="codePostal", type=StringType)
Client_ville: Property = Property(name="ville", type=StringType)
Client_contact: Property = Property(name="contact", type=StringType)
Client_tel: Property = Property(name="tel", type=StringType)
Client.attributes={Client_contact, Client_codePostal, Client_ville, Client_nom, Client_tel, Client_adresse}

# Formation class attributes and methods
Formation_libelle: Property = Property(name="libelle", type=StringType)
Formation_cout_unitaire: Property = Property(name="cout_unitaire", type=IntegerType)
Formation_objectif: Property = Property(name="objectif", type=StringType)
Formation.attributes={Formation_cout_unitaire, Formation_libelle, Formation_objectif}

# DevisEntete class attributes and methods
DevisEntete_numero: Property = Property(name="numero", type=StringType)
DevisEntete_id_session: Property = Property(name="id_session", type=IntegerType)
DevisEntete.attributes={DevisEntete_numero, DevisEntete_id_session}

# Facture class attributes and methods
Facture_numero: Property = Property(name="numero", type=StringType)
Facture_id_devis: Property = Property(name="id_devis", type=IntegerType)
Facture_paye: Property = Property(name="paye", type=BooleanType)
Facture.attributes={Facture_paye, Facture_id_devis, Facture_numero}

# Convention class attributes and methods
Convention_numero: Property = Property(name="numero", type=StringType)
Convention_id_convention: Property = Property(name="id_convention", type=IntegerType)
Convention.attributes={Convention_numero, Convention_id_convention}

# Type class attributes and methods
Type_type: Property = Property(name="type", type=StringType)
Type.attributes={Type_type}

# Prestation class attributes and methods
Prestation_id_client: Property = Property(name="id_client", type=IntegerType)
Prestation_id_formation: Property = Property(name="id_formation", type=IntegerType)
Prestation_id_formateur: Property = Property(name="id_formateur", type=IntegerType)
Prestation_id_type: Property = Property(name="id_type", type=IntegerType)
Prestation_date_debut: Property = Property(name="date_debut", type=StringType)
Prestation_date_fin: Property = Property(name="date_fin", type=StringType)
Prestation_duree: Property = Property(name="duree", type=StringType)
Prestation_horaires: Property = Property(name="horaires", type=StringType)
Prestation_lieu: Property = Property(name="lieu", type=BooleanType)
Prestation_nb_stagiaires: Property = Property(name="nb_stagiaires", type=IntegerType)
Prestation.attributes={Prestation_horaires, Prestation_id_client, Prestation_id_formateur, Prestation_nb_stagiaires, Prestation_duree, Prestation_id_type, Prestation_date_fin, Prestation_date_debut, Prestation_lieu, Prestation_id_formation}

# Formateur class attributes and methods
Formateur_Nom: Property = Property(name="Nom", type=StringType)
Formateur_Prenom: Property = Property(name="Prenom", type=StringType)
Formateur.attributes={Formateur_Nom, Formateur_Prenom}

# Participant class attributes and methods
Participant_id_session: Property = Property(name="id_session", type=IntegerType)
Participant_nom: Property = Property(name="nom", type=StringType)
Participant_prenom: Property = Property(name="prenom", type=StringType)
Participant_date_naissance: Property = Property(name="date_naissance", type=StringType)
Participant.attributes={Participant_id_session, Participant_nom, Participant_date_naissance, Participant_prenom}

# Relationships
Sessions_Participants: BinaryAssociation = BinaryAssociation(
    name="Sessions_Participants",
    ends={
        Property(name="participants0", type=Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="sessions1", type=Prestation, multiplicity=Multiplicity(0, 9999))
    }
)
Formateurs_Sessions: BinaryAssociation = BinaryAssociation(
    name="Formateurs_Sessions",
    ends={
        Property(name="sessions2", type=Prestation, multiplicity=Multiplicity(0, 1)),
        Property(name="formateurs3", type=Formateur, multiplicity=Multiplicity(0, 1))
    }
)
DevisEntete_Session: BinaryAssociation = BinaryAssociation(
    name="DevisEntete_Session",
    ends={
        Property(name="session4", type=Prestation, multiplicity=Multiplicity(0, 1)),
        Property(name="devisEntete5", type=DevisEntete, multiplicity=Multiplicity(0, 1))
    }
)
Client_Session: BinaryAssociation = BinaryAssociation(
    name="Client_Session",
    ends={
        Property(name="session6", type=Prestation, multiplicity=Multiplicity(0, 1)),
        Property(name="client7", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
Formation_Session: BinaryAssociation = BinaryAssociation(
    name="Formation_Session",
    ends={
        Property(name="session8", type=Prestation, multiplicity=Multiplicity(0, 1)),
        Property(name="formation9", type=Formation, multiplicity=Multiplicity(0, 1))
    }
)
Type_Prestation: BinaryAssociation = BinaryAssociation(
    name="Type_Prestation",
    ends={
        Property(name="prestation10", type=Prestation, multiplicity=Multiplicity(0, 1)),
        Property(name="type11", type=Type, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_xxwCoJSgEeiilJ4tAEXZQQ",
    types={Client, Formation, DevisEntete, Facture, Convention, Type, Prestation, Formateur, Participant},
    associations={Sessions_Participants, Formateurs_Sessions, DevisEntete_Session, Client_Session, Formation_Session, Type_Prestation},
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
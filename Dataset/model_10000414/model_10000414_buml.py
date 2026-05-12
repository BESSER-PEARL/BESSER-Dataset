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
BankAccount = Class(name="BankAccount")
ClassA = Class(name="ClassA")
ClassB = Class(name="ClassB")
ClassC = Class(name="ClassC")
ClassD = Class(name="ClassD")
ClassE = Class(name="ClassE")
ClassF = Class(name="ClassF")
ClassG = Class(name="ClassG")
ClassJ = Class(name="ClassJ")
ClassH = Class(name="ClassH")
ClassK = Class(name="ClassK")
ClassL = Class(name="ClassL")
ClassM = Class(name="ClassM")
ClassN = Class(name="ClassN")
ClassP = Class(name="ClassP")
InterfaceO_Interface = Class(name="InterfaceO_Interface")
ClassQ = Class(name="ClassQ")
ClassR = Class(name="ClassR")
ClassS = Class(name="ClassS")
ClassT = Class(name="ClassT")
ClassU = Class(name="ClassU")
ClassV = Class(name="ClassV")
Personne = Class(name="Personne")
Etudiant = Class(name="Etudiant")
Formateur = Class(name="Formateur")
Direction = Class(name="Direction")
Administrateur = Class(name="Administrateur")
Session = Class(name="Session")
Formation = Class(name="Formation")
Document = Class(name="Document")
CCP = Class(name="CCP")

# BankAccount class attributes and methods
BankAccount_ownerName: Property = Property(name="ownerName", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount.attributes={BankAccount_balance, BankAccount_ownerName}

# ClassA class attributes and methods
ClassA_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassA_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassA_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassA_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassA.attributes={ClassA_publicAttribute, ClassA_privateAttribute, ClassA_packageAttribute, ClassA_protectedAttribute}

# ClassB class attributes and methods

# ClassC class attributes and methods
ClassC_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassC_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassC_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassC_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassC.attributes={ClassC_packageAttribute, ClassC_publicAttribute, ClassC_privateAttribute, ClassC_protectedAttribute}

# ClassD class attributes and methods

# ClassE class attributes and methods

# ClassF class attributes and methods

# ClassG class attributes and methods

# ClassJ class attributes and methods

# ClassH class attributes and methods

# ClassK class attributes and methods

# ClassL class attributes and methods

# ClassM class attributes and methods

# ClassN class attributes and methods

# ClassP class attributes and methods

# InterfaceO_Interface class attributes and methods

# ClassQ class attributes and methods

# ClassR class attributes and methods

# ClassS class attributes and methods

# ClassT class attributes and methods

# ClassU class attributes and methods

# ClassV class attributes and methods

# Personne class attributes and methods
Personne_id: Property = Property(name="id", type=IntegerType)
Personne_nom: Property = Property(name="nom", type=StringType)
Personne_prenom: Property = Property(name="prenom", type=StringType)
Personne_naissance: Property = Property(name="naissance", type=DateType)
Personne_telephone: Property = Property(name="telephone", type=StringType)
Personne_mail: Property = Property(name="mail", type=StringType)
Personne_photo: Property = Property(name="photo", type=StringType)
Personne.attributes={Personne_telephone, Personne_prenom, Personne_mail, Personne_naissance, Personne_id, Personne_photo, Personne_nom}

# Etudiant class attributes and methods
Etudiant_id_etudiant: Property = Property(name="id_etudiant", type=IntegerType)
Etudiant_list_notes: Property = Property(name="list_notes", type=FloatType)
Etudiant_list_commentaire: Property = Property(name="list_commentaire", type=StringType)
Etudiant_cv: Property = Property(name="cv", type=StringType)
Etudiant_actif: Property = Property(name="actif", type=BooleanType)
Etudiant.attributes={Etudiant_id_etudiant, Etudiant_actif, Etudiant_list_commentaire, Etudiant_cv, Etudiant_list_notes}

# Formateur class attributes and methods
Formateur_id_formateur: Property = Property(name="id_formateur", type=IntegerType)
Formateur_actif: Property = Property(name="actif", type=BooleanType)
Formateur.attributes={Formateur_actif, Formateur_id_formateur}

# Direction class attributes and methods
Direction_id_direction: Property = Property(name="id_direction", type=IntegerType)
Direction_actif: Property = Property(name="actif", type=BooleanType)
Direction.attributes={Direction_actif, Direction_id_direction}

# Administrateur class attributes and methods
Administrateur_id_administrateur: Property = Property(name="id_administrateur", type=IntegerType)
Administrateur_actif: Property = Property(name="actif", type=BooleanType)
Administrateur.attributes={Administrateur_actif, Administrateur_id_administrateur}

# Session class attributes and methods
Session_id_session: Property = Property(name="id_session", type=IntegerType)
Session_label: Property = Property(name="label", type=StringType)
Session_adresse: Property = Property(name="adresse", type=StringType)
Session_date_debut: Property = Property(name="date_debut", type=DateType)
Session_date_fin: Property = Property(name="date_fin", type=DateType)
Session.attributes={Session_date_debut, Session_adresse, Session_date_fin, Session_id_session, Session_label}

# Formation class attributes and methods
Formation_id_formation: Property = Property(name="id_formation", type=IntegerType)
Formation_label: Property = Property(name="label", type=StringType)
Formation_descriptif: Property = Property(name="descriptif", type=StringType)
Formation.attributes={Formation_label, Formation_id_formation, Formation_descriptif}

# Document class attributes and methods
Document_id_document: Property = Property(name="id_document", type=IntegerType)
Document_label: Property = Property(name="label", type=StringType)
Document_descriptif: Property = Property(name="descriptif", type=StringType)
Document_url: Property = Property(name="url", type=StringType)
Document_cours: Property = Property(name="cours", type=BooleanType)
Document.attributes={Document_cours, Document_url, Document_descriptif, Document_id_document, Document_label}

# CCP class attributes and methods
CCP_id_ccp: Property = Property(name="id_ccp", type=IntegerType)
CCP_label: Property = Property(name="label", type=StringType)
CCP_description: Property = Property(name="description", type=StringType)
CCP.attributes={CCP_id_ccp, CCP_description, CCP_label}

# Relationships
ClassD_ClassE: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassE",
    ends={
        Property(name="classE0", type=ClassE, multiplicity=Multiplicity(0, 1)),
        Property(name="classD1", type=ClassD, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopy",
    ends={
        Property(name="classG2", type=ClassG, multiplicity=Multiplicity(0, 1)),
        Property(name="classF3", type=ClassF, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopyCopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopyCopy",
    ends={
        Property(name="classG4", type=ClassJ, multiplicity=Multiplicity(0, 1)),
        Property(name="classF5", type=ClassH, multiplicity=Multiplicity(0, 1))
    }
)
Personne_Etudiant: BinaryAssociation = BinaryAssociation(
    name="Personne_Etudiant",
    ends={
        Property(name="etudiant6", type=Etudiant, multiplicity=Multiplicity(0, 1)),
        Property(name="personne7", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Formateur: BinaryAssociation = BinaryAssociation(
    name="Personne_Formateur",
    ends={
        Property(name="formateur8", type=Formateur, multiplicity=Multiplicity(0, 1)),
        Property(name="personne9", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Direction: BinaryAssociation = BinaryAssociation(
    name="Personne_Direction",
    ends={
        Property(name="direction10", type=Direction, multiplicity=Multiplicity(0, 1)),
        Property(name="personne11", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Personne_Administrateur: BinaryAssociation = BinaryAssociation(
    name="Personne_Administrateur",
    ends={
        Property(name="administrateur12", type=Administrateur, multiplicity=Multiplicity(0, 1)),
        Property(name="personne13", type=Personne, multiplicity=Multiplicity(0, 9999))
    }
)
Session_Formateur: BinaryAssociation = BinaryAssociation(
    name="Session_Formateur",
    ends={
        Property(name="formateur14", type=Formateur, multiplicity=Multiplicity(1, 9999)),
        Property(name="session15", type=Session, multiplicity=Multiplicity(1, 9999))
    }
)
Formation_Session: BinaryAssociation = BinaryAssociation(
    name="Formation_Session",
    ends={
        Property(name="session16", type=Session, multiplicity=Multiplicity(0, 9999)),
        Property(name="formation17", type=Formation, multiplicity=Multiplicity(1, 1))
    }
)
Formation_CCP: BinaryAssociation = BinaryAssociation(
    name="Formation_CCP",
    ends={
        Property(name="cCP18", type=CCP, multiplicity=Multiplicity(0, 9999)),
        Property(name="formation19", type=Formation, multiplicity=Multiplicity(0, 9999))
    }
)
Document_Session: BinaryAssociation = BinaryAssociation(
    name="Document_Session",
    ends={
        Property(name="session20", type=Session, multiplicity=Multiplicity(0, 9999)),
        Property(name="document21", type=Document, multiplicity=Multiplicity(0, 9999))
    }
)
Etudiant_Session: BinaryAssociation = BinaryAssociation(
    name="Etudiant_Session",
    ends={
        Property(name="session22", type=Session, multiplicity=Multiplicity(1, 9999)),
        Property(name="etudiant23", type=Etudiant, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_348cf966_a42e_438a_91b6_9396329db506",
    types={BankAccount, ClassA, ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassJ, ClassH, ClassK, ClassL, ClassM, ClassN, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV, Personne, Etudiant, Formateur, Direction, Administrateur, Session, Formation, Document, CCP},
    associations={ClassD_ClassE, ClassD_ClassECopy, ClassD_ClassECopyCopy, Personne_Etudiant, Personne_Formateur, Personne_Direction, Personne_Administrateur, Session_Formateur, Formation_Session, Formation_CCP, Document_Session, Etudiant_Session},
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
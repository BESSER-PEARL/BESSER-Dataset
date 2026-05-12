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
Personne = Class(name="Personne")
Utilisateur = Class(name="Utilisateur")
Voiture = Class(name="Voiture")
cours = Class(name="cours")
Examen = Class(name="Examen")
Professeur = Class(name="Professeur")
Candidat = Class(name="Candidat")
Groupe = Class(name="Groupe")
CoursConduite = Class(name="CoursConduite")
CoursCode = Class(name="CoursCode")

# Personne class attributes and methods
Personne_id: Property = Property(name="id", type=IntegerType)
Personne_nom: Property = Property(name="nom", type=StringType)
Personne_prenom: Property = Property(name="prenom", type=StringType)
Personne_adresse: Property = Property(name="adresse", type=StringType)
Personne_telephone: Property = Property(name="telephone", type=StringType)
Personne_email: Property = Property(name="email", type=StringType)
Personne_dateNaissance: Property = Property(name="dateNaissance", type=StringType)
Personne_lieuNaissance: Property = Property(name="lieuNaissance", type=StringType)
Personne_numeroCIN: Property = Property(name="numeroCIN", type=IntegerType)
Personne.attributes={Personne_dateNaissance, Personne_adresse, Personne_prenom, Personne_id, Personne_lieuNaissance, Personne_nom, Personne_numeroCIN, Personne_telephone, Personne_email}

# Utilisateur class attributes and methods
Utilisateur_login: Property = Property(name="login", type=StringType)
Utilisateur_mdp: Property = Property(name="mdp", type=StringType)
Utilisateur.attributes={Utilisateur_login, Utilisateur_mdp}

# Voiture class attributes and methods
Voiture_id: Property = Property(name="id", type=IntegerType)
Voiture_immatriculation: Property = Property(name="immatriculation", type=StringType)
Voiture_marque: Property = Property(name="marque", type=StringType)
Voiture_modele: Property = Property(name="modele", type=StringType)
Voiture.attributes={Voiture_immatriculation, Voiture_id, Voiture_marque, Voiture_modele}

# cours class attributes and methods
cours_id: Property = Property(name="id", type=IntegerType)
cours_dateCours: Property = Property(name="dateCours", type=StringType)
cours_heureD: Property = Property(name="heureD", type=StringType)
cours_heureF: Property = Property(name="heureF", type=StringType)
cours.attributes={cours_dateCours, cours_id, cours_heureF, cours_heureD}

# Examen class attributes and methods
Examen_id: Property = Property(name="id", type=IntegerType)
Examen_dateExamen: Property = Property(name="dateExamen", type=StringType)
Examen_heureD: Property = Property(name="heureD", type=StringType)
Examen_heureF: Property = Property(name="heureF", type=StringType)
Examen_typeExamen: Property = Property(name="typeExamen", type=StringType)
Examen.attributes={Examen_heureF, Examen_typeExamen, Examen_dateExamen, Examen_heureD, Examen_id}

# Professeur class attributes and methods
Professeur_dateEmbauche: Property = Property(name="dateEmbauche", type=StringType)
Professeur.attributes={Professeur_dateEmbauche}

# Candidat class attributes and methods

# Groupe class attributes and methods
Groupe_id: Property = Property(name="id", type=IntegerType)
Groupe_numeroGroupe: Property = Property(name="numeroGroupe", type=IntegerType)
Groupe_libelle: Property = Property(name="libelle", type=StringType)
Groupe.attributes={Groupe_id, Groupe_numeroGroupe, Groupe_libelle}

# CoursConduite class attributes and methods

# CoursCode class attributes and methods

# Relationships
professeur_coursCode: BinaryAssociation = BinaryAssociation(
    name="professeur_coursCode",
    ends={
        Property(name="professeur5", type=Professeur, multiplicity=Multiplicity(1, 1)),
        Property(name="donner4", type=CoursCode, multiplicity=Multiplicity(0, 9999))
    }
)
professeur_coursConduite: BinaryAssociation = BinaryAssociation(
    name="professeur_coursConduite",
    ends={
        Property(name="dispenser6", type=CoursConduite, multiplicity=Multiplicity(0, 9999)),
        Property(name="professeur7", type=Professeur, multiplicity=Multiplicity(1, 1))
    }
)
groupe_coursCode: BinaryAssociation = BinaryAssociation(
    name="groupe_coursCode",
    ends={
        Property(name="suivre8", type=CoursCode, multiplicity=Multiplicity(1, 9999)),
        Property(name="groupe9", type=Groupe, multiplicity=Multiplicity(1, 1))
    }
)
coursConduite_candidat: BinaryAssociation = BinaryAssociation(
    name="coursConduite_candidat",
    ends={
        Property(name="faire10", type=Candidat, multiplicity=Multiplicity(1, 1)),
        Property(name="coursConduite11", type=CoursConduite, multiplicity=Multiplicity(0, 9999))
    }
)
coursConduite_voiture: BinaryAssociation = BinaryAssociation(
    name="coursConduite_voiture",
    ends={
        Property(name="concerner0", type=Voiture, multiplicity=Multiplicity(1, 1)),
        Property(name="coursConduite1", type=CoursConduite, multiplicity=Multiplicity(0, 9999))
    }
)
candidat_groupe: BinaryAssociation = BinaryAssociation(
    name="candidat_groupe",
    ends={
        Property(name="appartenir2", type=Groupe, multiplicity=Multiplicity(1, 1)),
        Property(name="candidat3", type=Candidat, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_f6nG8KNoEemlGeJsLESUmg",
    types={Personne, Utilisateur, Voiture, cours, Examen, Professeur, Candidat, Groupe, CoursConduite, CoursCode},
    associations={professeur_coursCode, professeur_coursConduite, groupe_coursCode, coursConduite_candidat, coursConduite_voiture, candidat_groupe},
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
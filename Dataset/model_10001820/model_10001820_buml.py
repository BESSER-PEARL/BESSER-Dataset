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
Club_de_lecture_Habitant_Actor = Class(name="Club_de_lecture_Habitant_Actor")
Club_de_lecture_S_inscrire_UseCase = Class(name="Club_de_lecture_S_inscrire_UseCase")
Club_de_lecture_Consulter_p_riodiques___livres_UseCase = Class(name="Club_de_lecture_Consulter_p_riodiques___livres_UseCase")
Club_de_lecture_Utilisateur_inscrit_Actor = Class(name="Club_de_lecture_Utilisateur_inscrit_Actor")
Club_de_lecture_Emprunter_livres_UseCase = Class(name="Club_de_lecture_Emprunter_livres_UseCase")
Club_de_lecture_Emprunter_DVD_UseCase = Class(name="Club_de_lecture_Emprunter_DVD_UseCase")
Club_de_lecture_Emprunter_livre_num_rique_UseCase = Class(name="Club_de_lecture_Emprunter_livre_num_rique_UseCase")
Etudiant = Class(name="Etudiant")
Responsable_CL = Class(name="Responsable_CL")
Animal = Class(name="Animal")
Habitant = Class(name="Habitant")
Utilisateur_Inscrit = Class(name="Utilisateur_Inscrit")
Utilisateur_Inscrit1 = Class(name="Utilisateur_Inscrit1")
Media_physique = Class(name="Media_physique")
Livre = Class(name="Livre")
CD = Class(name="CD")
Livre_num_rique = Class(name="Livre_num_rique")
Informations = Class(name="Informations")
Club_de_lecture_Emprunter_UseCase = Class(name="Club_de_lecture_Emprunter_UseCase")
Club_de_lecture_Faire_proposition_UseCase = Class(name="Club_de_lecture_Faire_proposition_UseCase")

# Club_de_lecture_Habitant_Actor class attributes and methods

# Club_de_lecture_S_inscrire_UseCase class attributes and methods

# Club_de_lecture_Consulter_p_riodiques___livres_UseCase class attributes and methods

# Club_de_lecture_Utilisateur_inscrit_Actor class attributes and methods

# Club_de_lecture_Emprunter_livres_UseCase class attributes and methods

# Club_de_lecture_Emprunter_DVD_UseCase class attributes and methods

# Club_de_lecture_Emprunter_livre_num_rique_UseCase class attributes and methods

# Etudiant class attributes and methods

# Responsable_CL class attributes and methods

# Animal class attributes and methods
Animal_Age: Property = Property(name="Age", type=StringType)
Animal.attributes={Animal_Age}

# Habitant class attributes and methods

# Utilisateur_Inscrit class attributes and methods

# Utilisateur_Inscrit1 class attributes and methods
Utilisateur_Inscrit1_noCarte: Property = Property(name="noCarte", type=StringType)
Utilisateur_Inscrit1.attributes={Utilisateur_Inscrit1_noCarte}

# Media_physique class attributes and methods

# Livre class attributes and methods

# CD class attributes and methods

# Livre_num_rique class attributes and methods

# Informations class attributes and methods

# Club_de_lecture_Emprunter_UseCase class attributes and methods

# Club_de_lecture_Faire_proposition_UseCase class attributes and methods

# Relationships
Habtitant_S_inscrire: BinaryAssociation = BinaryAssociation(
    name="Habtitant_S_inscrire",
    ends={
        Property(name="s_inscrire0", type=Club_de_lecture_S_inscrire_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="habtitant1", type=Club_de_lecture_Habitant_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Habtitant_Consulter_p_riodiques___livres: BinaryAssociation = BinaryAssociation(
    name="Habtitant_Consulter_p_riodiques___livres",
    ends={
        Property(name="consulter_p_riodiques___livres2", type=Club_de_lecture_Consulter_p_riodiques___livres_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="habtitant3", type=Club_de_lecture_Habitant_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_inscrit_Emprunter: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_inscrit_Emprunter",
    ends={
        Property(name="emprunter4", type=Club_de_lecture_Emprunter_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="utilisateur_inscrit5", type=Club_de_lecture_Utilisateur_inscrit_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_inscrit_Faire_proposition: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_inscrit_Faire_proposition",
    ends={
        Property(name="faire_proposition6", type=Club_de_lecture_Faire_proposition_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="utilisateur_inscrit7", type=Club_de_lecture_Utilisateur_inscrit_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_Inscrit_Livre: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Inscrit_Livre",
    ends={
        Property(name="empruntLivre8", type=Livre, multiplicity=Multiplicity(0, 5)),
        Property(name="emprunter_9", type=Utilisateur_Inscrit1, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_Inscrit_CD: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Inscrit_CD",
    ends={
        Property(name="cD10", type=CD, multiplicity=Multiplicity(0, 1)),
        Property(name="utilisateur_Inscrit11", type=Utilisateur_Inscrit1, multiplicity=Multiplicity(0, 1))
    }
)
Utilisateur_Inscrit_Livre_num_rique: BinaryAssociation = BinaryAssociation(
    name="Utilisateur_Inscrit_Livre_num_rique",
    ends={
        Property(name="livre_num_rique12", type=Livre_num_rique, multiplicity=Multiplicity(0, 5)),
        Property(name="utilisateur_Inscrit13", type=Utilisateur_Inscrit1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Y2Pk4DkcEeqTDpmqRhKD9Q",
    types={Club_de_lecture_Habitant_Actor, Club_de_lecture_S_inscrire_UseCase, Club_de_lecture_Consulter_p_riodiques___livres_UseCase, Club_de_lecture_Utilisateur_inscrit_Actor, Club_de_lecture_Emprunter_livres_UseCase, Club_de_lecture_Emprunter_DVD_UseCase, Club_de_lecture_Emprunter_livre_num_rique_UseCase, Etudiant, Responsable_CL, Animal, Habitant, Utilisateur_Inscrit, Utilisateur_Inscrit1, Media_physique, Livre, CD, Livre_num_rique, Informations, Club_de_lecture_Emprunter_UseCase, Club_de_lecture_Faire_proposition_UseCase},
    associations={Habtitant_S_inscrire, Habtitant_Consulter_p_riodiques___livres, Utilisateur_inscrit_Emprunter, Utilisateur_inscrit_Faire_proposition, Utilisateur_Inscrit_Livre, Utilisateur_Inscrit_CD, Utilisateur_Inscrit_Livre_num_rique},
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
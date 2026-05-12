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
Membre = Class(name="Membre")
Association = Class(name="Association")
Service = Class(name="Service")
Membre1 = Class(name="Membre1")
Recherche_Avanc_e = Class(name="Recherche_Avanc_e")
Resultat_Recherche = Class(name="Resultat_Recherche")
Recherche_Rapide = Class(name="Recherche_Rapide")
Acteurs = Class(name="Acteurs")
Systeme = Class(name="Systeme")
RechercheDAssociations = Class(name="RechercheDAssociations")
Resultat = Class(name="Resultat")
Utilisateur = Class(name="Utilisateur")
CompteDeLUtilisateur = Class(name="CompteDeLUtilisateur")
PropositionDeService = Class(name="PropositionDeService")
DemandeDeService = Class(name="DemandeDeService")
RecherchePropositions = Class(name="RecherchePropositions")
RechercheDemandes = Class(name="RechercheDemandes")
Utilisateur1 = Class(name="Utilisateur1")
CompteDeLUtilisateur1 = Class(name="CompteDeLUtilisateur1")
PropositionDeService1 = Class(name="PropositionDeService1")
DemandeDeService1 = Class(name="DemandeDeService1")
CritereDeRecherche = Class(name="CritereDeRecherche")
AffichageResultats = Class(name="AffichageResultats")
SelectionnerUnResultat = Class(name="SelectionnerUnResultat")
AffichageDetailleResultat = Class(name="AffichageDetailleResultat")
Contacter = Class(name="Contacter")
RechercheRapide = Class(name="RechercheRapide")
RechercheAvancee = Class(name="RechercheAvancee")
AffichageAccueil = Class(name="AffichageAccueil")
__table___T_CompteDeLUtilisateur = Class(name="__table___T_CompteDeLUtilisateur")
__table___T_Services = Class(name="__table___T_Services")

# Membre class attributes and methods
Membre_nom___salim_talout: Property = Property(name="nom___salim_talout", type=StringType)
Membre.attributes={Membre_nom___salim_talout}

# Association class attributes and methods
Association_nom___unicef: Property = Property(name="nom___unicef", type=StringType)
Association.attributes={Association_nom___unicef}

# Service class attributes and methods
Service_description: Property = Property(name="description", type=StringType)
Service.attributes={Service_description}

# Membre1 class attributes and methods

# Recherche_Avanc_e class attributes and methods
Recherche_Avanc_e_Titre: Property = Property(name="Titre", type=StringType)
Recherche_Avanc_e_Association: Property = Property(name="Association", type=Association)
Recherche_Avanc_e_Pays: Property = Property(name="Pays", type=StringType)
Recherche_Avanc_e_NbParticipants: Property = Property(name="NbParticipants", type=IntegerType)
Recherche_Avanc_e_Date: Property = Property(name="Date", type=DateType)
Recherche_Avanc_e.attributes={Recherche_Avanc_e_Pays, Recherche_Avanc_e_Titre, Recherche_Avanc_e_Association, Recherche_Avanc_e_Date, Recherche_Avanc_e_NbParticipants}

# Resultat_Recherche class attributes and methods

# Recherche_Rapide class attributes and methods
Recherche_Rapide_MotsCles: Property = Property(name="MotsCles", type=StringType)
Recherche_Rapide.attributes={Recherche_Rapide_MotsCles}

# Acteurs class attributes and methods

# Systeme class attributes and methods

# RechercheDAssociations class attributes and methods
RechercheDAssociations_criteres: Property = Property(name="criteres", type=StringType)
RechercheDAssociations.attributes={RechercheDAssociations_criteres}

# Resultat class attributes and methods
Resultat_Liste: Property = Property(name="Liste", type=Resultat_Recherche)
Resultat.attributes={Resultat_Liste}

# Utilisateur class attributes and methods

# CompteDeLUtilisateur class attributes and methods
CompteDeLUtilisateur_peudo: Property = Property(name="peudo", type=StringType)
CompteDeLUtilisateur_adresseMail: Property = Property(name="adresseMail", type=StringType)
CompteDeLUtilisateur_motDePasse: Property = Property(name="motDePasse", type=StringType)
CompteDeLUtilisateur_Type: Property = Property(name="Type", type=StringType)
CompteDeLUtilisateur.attributes={CompteDeLUtilisateur_peudo, CompteDeLUtilisateur_adresseMail, CompteDeLUtilisateur_motDePasse, CompteDeLUtilisateur_Type}

# PropositionDeService class attributes and methods

# DemandeDeService class attributes and methods

# RecherchePropositions class attributes and methods
RecherchePropositions_criteres: Property = Property(name="criteres", type=StringType)
RecherchePropositions.attributes={RecherchePropositions_criteres}

# RechercheDemandes class attributes and methods
RechercheDemandes_criteres: Property = Property(name="criteres", type=StringType)
RechercheDemandes.attributes={RechercheDemandes_criteres}

# Utilisateur1 class attributes and methods

# CompteDeLUtilisateur1 class attributes and methods
CompteDeLUtilisateur1_peudo: Property = Property(name="peudo", type=StringType)
CompteDeLUtilisateur1_adresseMail: Property = Property(name="adresseMail", type=StringType)
CompteDeLUtilisateur1_motDePasse: Property = Property(name="motDePasse", type=StringType)
CompteDeLUtilisateur1_Type: Property = Property(name="Type", type=StringType)
CompteDeLUtilisateur1.attributes={CompteDeLUtilisateur1_peudo, CompteDeLUtilisateur1_Type, CompteDeLUtilisateur1_adresseMail, CompteDeLUtilisateur1_motDePasse}

# PropositionDeService1 class attributes and methods

# DemandeDeService1 class attributes and methods

# CritereDeRecherche class attributes and methods
CritereDeRecherche_critere: Property = Property(name="critere", type=StringType)
CritereDeRecherche.attributes={CritereDeRecherche_critere}

# AffichageResultats class attributes and methods

# SelectionnerUnResultat class attributes and methods

# AffichageDetailleResultat class attributes and methods

# Contacter class attributes and methods
Contacter_personne: Property = Property(name="personne", type=Utilisateur)
Contacter.attributes={Contacter_personne}

# RechercheRapide class attributes and methods
RechercheRapide_MotsCles: Property = Property(name="MotsCles", type=StringType)
RechercheRapide.attributes={RechercheRapide_MotsCles}

# RechercheAvancee class attributes and methods
RechercheAvancee_Titre: Property = Property(name="Titre", type=StringType)
RechercheAvancee_Association: Property = Property(name="Association", type=Association)
RechercheAvancee_GenreService: Property = Property(name="GenreService", type=Service)
RechercheAvancee_NbParticipants: Property = Property(name="NbParticipants", type=IntegerType)
RechercheAvancee_Date: Property = Property(name="Date", type=DateType)
RechercheAvancee.attributes={RechercheAvancee_NbParticipants, RechercheAvancee_GenreService, RechercheAvancee_Date, RechercheAvancee_Association, RechercheAvancee_Titre}

# AffichageAccueil class attributes and methods

# __table___T_CompteDeLUtilisateur class attributes and methods
__table___T_CompteDeLUtilisateur_numeroUtilisateur: Property = Property(name="numeroUtilisateur", type=IntegerType)
__table___T_CompteDeLUtilisateur_pseudo: Property = Property(name="pseudo", type=StringType)
__table___T_CompteDeLUtilisateur_adresseMail: Property = Property(name="adresseMail", type=StringType)
__table___T_CompteDeLUtilisateur_motDePasse: Property = Property(name="motDePasse", type=StringType)
__table___T_CompteDeLUtilisateur_type: Property = Property(name="type", type=StringType)
__table___T_CompteDeLUtilisateur.attributes={__table___T_CompteDeLUtilisateur_pseudo, __table___T_CompteDeLUtilisateur_adresseMail, __table___T_CompteDeLUtilisateur_numeroUtilisateur, __table___T_CompteDeLUtilisateur_motDePasse, __table___T_CompteDeLUtilisateur_type}

# __table___T_Services class attributes and methods
__table___T_Services_numeroService: Property = Property(name="numeroService", type=IntegerType)
__table___T_Services_numeroUtilisateur: Property = Property(name="numeroUtilisateur", type=IntegerType)
__table___T_Services_type: Property = Property(name="type", type=StringType)
__table___T_Services_titre: Property = Property(name="titre", type=StringType)
__table___T_Services_description: Property = Property(name="description", type=StringType)
__table___T_Services_nbParticipants: Property = Property(name="nbParticipants", type=IntegerType)
__table___T_Services_date: Property = Property(name="date", type=DateType)
__table___T_Services.attributes={__table___T_Services_numeroService, __table___T_Services_titre, __table___T_Services_date, __table___T_Services_nbParticipants, __table___T_Services_type, __table___T_Services_numeroUtilisateur, __table___T_Services_description}

# Relationships
Association_Membre: BinaryAssociation = BinaryAssociation(
    name="Association_Membre",
    ends={
        Property(name="membre0", type=Membre, multiplicity=Multiplicity(0, 9999)),
        Property(name="association1", type=Association, multiplicity=Multiplicity(1, 9999))
    }
)
Service_Association: BinaryAssociation = BinaryAssociation(
    name="Service_Association",
    ends={
        Property(name="association2", type=Association, multiplicity=Multiplicity(1, 1)),
        Property(name="service3", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
Service_Membre: BinaryAssociation = BinaryAssociation(
    name="Service_Membre",
    ends={
        Property(name="membre4", type=Membre, multiplicity=Multiplicity(0, 9999)),
        Property(name="service5", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Tsj1kAWNEeeUMouUWv9oWw",
    types={Membre, Association, Service, Membre1, Recherche_Avanc_e, Resultat_Recherche, Recherche_Rapide, Acteurs, Systeme, RechercheDAssociations, Resultat, Utilisateur, CompteDeLUtilisateur, PropositionDeService, DemandeDeService, RecherchePropositions, RechercheDemandes, Utilisateur1, CompteDeLUtilisateur1, PropositionDeService1, DemandeDeService1, CritereDeRecherche, AffichageResultats, SelectionnerUnResultat, AffichageDetailleResultat, Contacter, RechercheRapide, RechercheAvancee, AffichageAccueil, __table___T_CompteDeLUtilisateur, __table___T_Services},
    associations={Association_Membre, Service_Association, Service_Membre},
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
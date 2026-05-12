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
FormatWebEnum: Enumeration = Enumeration(
    name="FormatWebEnum",
    literals={
            EnumerationLiteral(name="XML"),
			EnumerationLiteral(name="HTML"),
			EnumerationLiteral(name="HTM")
    }
)

DateVisibleEnum: Enumeration = Enumeration(
    name="DateVisibleEnum",
    literals={
            EnumerationLiteral(name="15J"),
			EnumerationLiteral(name="1M"),
			EnumerationLiteral(name="3M"),
			EnumerationLiteral(name="1A"),
			EnumerationLiteral(name="2A"),
			EnumerationLiteral(name="JAMAIS")
    }
)

FormatEnum: Enumeration = Enumeration(
    name="FormatEnum",
    literals={
            EnumerationLiteral(name="ANNEX"),
			EnumerationLiteral(name="PDF"),
			EnumerationLiteral(name="TEX"),
			EnumerationLiteral(name="DOC"),
			EnumerationLiteral(name="RTF"),
			EnumerationLiteral(name="TXT"),
			EnumerationLiteral(name="PS")
    }
)

# Classes
Entry = Class(name="Entry")
HAL_Connexion = Class(name="HAL_Connexion")
HAL_HAL = Class(name="HAL_HAL")
Connexion = Class(name="Connexion")
TamponType = Class(name="TamponType")
HAL_Article = Class(name="HAL_Article", is_abstract=True)
HAL_Entry = Class(name="HAL_Entry", is_abstract=True)
AutLabType = Class(name="AutLabType")
AbstractDepot = Class(name="AbstractDepot")
HAL_Notice = Class(name="HAL_Notice")
MetaArtNoticeType = Class(name="MetaArtNoticeType")
MetaArtType = Class(name="MetaArtType")
HAL_ArticleRecent = Class(name="HAL_ArticleRecent")
Article = Class(name="Article")
DepotsType = Class(name="DepotsType")
HAL_ArticleRetro = Class(name="HAL_ArticleRetro")
HAL_WorkshopType = Class(name="HAL_WorkshopType", is_abstract=True)
HAL_ReferenceBiblioType = Class(name="HAL_ReferenceBiblioType", is_abstract=True)
HAL_ArtRevueType = Class(name="HAL_ArtRevueType", is_abstract=True)
ReferenceBiblioType = Class(name="ReferenceBiblioType")
HAL_ArtOuvrageType = Class(name="HAL_ArtOuvrageType", is_abstract=True)
HAL_TheseType = Class(name="HAL_TheseType", is_abstract=True)
HAL_OuvrageType = Class(name="HAL_OuvrageType", is_abstract=True)
HAL_AutreType = Class(name="HAL_AutreType", is_abstract=True)
HAL_BrevetType = Class(name="HAL_BrevetType", is_abstract=True)
HAL_ArtRevue = Class(name="HAL_ArtRevue")
ArtRevueType = Class(name="ArtRevueType")
HAL_ArtJournal = Class(name="HAL_ArtJournal")
HAL_Workshop = Class(name="HAL_Workshop")
WorkshopType = Class(name="WorkshopType")
HAL_Communication = Class(name="HAL_Communication")
HAL_Conference = Class(name="HAL_Conference")
HAL_ArtOuvrage = Class(name="HAL_ArtOuvrage")
ArtOuvrageType = Class(name="ArtOuvrageType")
HAL_Ouvrage = Class(name="HAL_Ouvrage")
OuvrageType = Class(name="OuvrageType")
HAL_Brevet = Class(name="HAL_Brevet")
BrevetType = Class(name="BrevetType")
HAL_Autre = Class(name="HAL_Autre")
AutreType = Class(name="AutreType")
HAL_These = Class(name="HAL_These")
TheseType = Class(name="TheseType")
HAL_MetaType = Class(name="HAL_MetaType", is_abstract=True)
HAL_AutLabType = Class(name="HAL_AutLabType")
Auteur = Class(name="Auteur")
Laboratoire = Class(name="Laboratoire")
HAL_Auteur = Class(name="HAL_Auteur")
HAL_MetaArtType = Class(name="HAL_MetaArtType")
MetaType = Class(name="MetaType")
HAL_MetaArtNoticeType = Class(name="HAL_MetaArtNoticeType")
HAL_MetaLab = Class(name="HAL_MetaLab")
HAL_AffiliationType = Class(name="HAL_AffiliationType")
HAL_TamponType = Class(name="HAL_TamponType")
HAL_Laboratoire = Class(name="HAL_Laboratoire")
AbstractMetaLab = Class(name="AbstractMetaLab")
HAL_AbstractMetaLab = Class(name="HAL_AbstractMetaLab", is_abstract=True)
HAL_DepotWeb = Class(name="HAL_DepotWeb")
HAL_AbstractDepotType = Class(name="HAL_AbstractDepotType", is_abstract=True)
HAL_DepotsType = Class(name="HAL_DepotsType")
AbstractDepotType = Class(name="AbstractDepotType")
HAL_AbstractDepot = Class(name="HAL_AbstractDepot", is_abstract=True)
HAL_Depot = Class(name="HAL_Depot")
HAL_WebLink = Class(name="HAL_WebLink")
Server = Class(name="Server")
HAL_Server = Class(name="HAL_Server")

# Entry class attributes and methods

# HAL_Connexion class attributes and methods
HAL_Connexion_login: Property = Property(name="login", type=StringType)
HAL_Connexion_password: Property = Property(name="password", type=StringType)
HAL_Connexion.attributes={HAL_Connexion_password, HAL_Connexion_login}

# HAL_HAL class attributes and methods

# Connexion class attributes and methods

# TamponType class attributes and methods

# HAL_Article class attributes and methods

# HAL_Entry class attributes and methods

# AutLabType class attributes and methods

# AbstractDepot class attributes and methods

# HAL_Notice class attributes and methods

# MetaArtNoticeType class attributes and methods

# MetaArtType class attributes and methods

# HAL_ArticleRecent class attributes and methods

# Article class attributes and methods

# DepotsType class attributes and methods

# HAL_ArticleRetro class attributes and methods
HAL_ArticleRetro_dateRedaction: Property = Property(name="dateRedaction", type=StringType)
HAL_ArticleRetro.attributes={HAL_ArticleRetro_dateRedaction}

# HAL_WorkshopType class attributes and methods
HAL_WorkshopType_serie: Property = Property(name="serie", type=StringType)
HAL_WorkshopType_urldoi: Property = Property(name="urldoi", type=StringType)
HAL_WorkshopType_titconf: Property = Property(name="titconf", type=StringType)
HAL_WorkshopType_ville: Property = Property(name="ville", type=StringType)
HAL_WorkshopType_pays: Property = Property(name="pays", type=StringType)
HAL_WorkshopType_edcom: Property = Property(name="edcom", type=StringType)
HAL_WorkshopType_annee: Property = Property(name="annee", type=StringType)
HAL_WorkshopType_page: Property = Property(name="page", type=StringType)
HAL_WorkshopType_edsci: Property = Property(name="edsci", type=StringType)
HAL_WorkshopType.attributes={HAL_WorkshopType_pays, HAL_WorkshopType_titconf, HAL_WorkshopType_annee, HAL_WorkshopType_urldoi, HAL_WorkshopType_page, HAL_WorkshopType_ville, HAL_WorkshopType_edcom, HAL_WorkshopType_edsci, HAL_WorkshopType_serie}

# HAL_ReferenceBiblioType class attributes and methods

# HAL_ArtRevueType class attributes and methods
HAL_ArtRevueType_page: Property = Property(name="page", type=StringType)
HAL_ArtRevueType_annee: Property = Property(name="annee", type=StringType)
HAL_ArtRevueType_urldoi: Property = Property(name="urldoi", type=StringType)
HAL_ArtRevueType_journal: Property = Property(name="journal", type=StringType)
HAL_ArtRevueType_volume: Property = Property(name="volume", type=StringType)
HAL_ArtRevueType.attributes={HAL_ArtRevueType_journal, HAL_ArtRevueType_urldoi, HAL_ArtRevueType_page, HAL_ArtRevueType_volume, HAL_ArtRevueType_annee}

# ReferenceBiblioType class attributes and methods

# HAL_ArtOuvrageType class attributes and methods
HAL_ArtOuvrageType_urldoi: Property = Property(name="urldoi", type=StringType)
HAL_ArtOuvrageType_titouv: Property = Property(name="titouv", type=StringType)
HAL_ArtOuvrageType_edcom: Property = Property(name="edcom", type=StringType)
HAL_ArtOuvrageType_annee: Property = Property(name="annee", type=StringType)
HAL_ArtOuvrageType_edsci: Property = Property(name="edsci", type=StringType)
HAL_ArtOuvrageType_serie: Property = Property(name="serie", type=StringType)
HAL_ArtOuvrageType.attributes={HAL_ArtOuvrageType_annee, HAL_ArtOuvrageType_serie, HAL_ArtOuvrageType_edcom, HAL_ArtOuvrageType_urldoi, HAL_ArtOuvrageType_edsci, HAL_ArtOuvrageType_titouv}

# HAL_TheseType class attributes and methods
HAL_TheseType_orgthe: Property = Property(name="orgthe", type=StringType)
HAL_TheseType_niveau: Property = Property(name="niveau", type=StringType)
HAL_TheseType_defencedate: Property = Property(name="defencedate", type=StringType)
HAL_TheseType_directeur: Property = Property(name="directeur", type=StringType)
HAL_TheseType_codirecteur: Property = Property(name="codirecteur", type=StringType)
HAL_TheseType.attributes={HAL_TheseType_orgthe, HAL_TheseType_codirecteur, HAL_TheseType_directeur, HAL_TheseType_niveau, HAL_TheseType_defencedate}

# HAL_OuvrageType class attributes and methods
HAL_OuvrageType_edcom: Property = Property(name="edcom", type=StringType)
HAL_OuvrageType_annee: Property = Property(name="annee", type=StringType)
HAL_OuvrageType_page: Property = Property(name="page", type=StringType)
HAL_OuvrageType_urldoi: Property = Property(name="urldoi", type=StringType)
HAL_OuvrageType.attributes={HAL_OuvrageType_edcom, HAL_OuvrageType_page, HAL_OuvrageType_urldoi, HAL_OuvrageType_annee}

# HAL_AutreType class attributes and methods
HAL_AutreType_urldoi: Property = Property(name="urldoi", type=StringType)
HAL_AutreType_annee: Property = Property(name="annee", type=StringType)
HAL_AutreType_description: Property = Property(name="description", type=StringType)
HAL_AutreType.attributes={HAL_AutreType_description, HAL_AutreType_urldoi, HAL_AutreType_annee}

# HAL_BrevetType class attributes and methods
HAL_BrevetType_numbrevet: Property = Property(name="numbrevet", type=StringType)
HAL_BrevetType_page: Property = Property(name="page", type=StringType)
HAL_BrevetType_pays: Property = Property(name="pays", type=StringType)
HAL_BrevetType_datebrevet: Property = Property(name="datebrevet", type=StringType)
HAL_BrevetType.attributes={HAL_BrevetType_datebrevet, HAL_BrevetType_page, HAL_BrevetType_numbrevet, HAL_BrevetType_pays}

# HAL_ArtRevue class attributes and methods

# ArtRevueType class attributes and methods

# HAL_ArtJournal class attributes and methods

# HAL_Workshop class attributes and methods

# WorkshopType class attributes and methods

# HAL_Communication class attributes and methods

# HAL_Conference class attributes and methods

# HAL_ArtOuvrage class attributes and methods

# ArtOuvrageType class attributes and methods

# HAL_Ouvrage class attributes and methods

# OuvrageType class attributes and methods

# HAL_Brevet class attributes and methods

# BrevetType class attributes and methods

# HAL_Autre class attributes and methods

# AutreType class attributes and methods

# HAL_These class attributes and methods

# TheseType class attributes and methods

# HAL_MetaType class attributes and methods
HAL_MetaType_langue: Property = Property(name="langue", type=StringType)
HAL_MetaType_title: Property = Property(name="title", type=StringType)
HAL_MetaType_comment: Property = Property(name="comment", type=StringType)
HAL_MetaType_refInterne: Property = Property(name="refInterne", type=StringType)
HAL_MetaType_idext: Property = Property(name="idext", type=StringType)
HAL_MetaType_isEpj: Property = Property(name="isEpj", type=StringType)
HAL_MetaType_isEpl: Property = Property(name="isEpl", type=StringType)
HAL_MetaType_classification: Property = Property(name="classification", type=StringType)
HAL_MetaType_collaboration: Property = Property(name="collaboration", type=StringType)
HAL_MetaType_keyword: Property = Property(name="keyword", type=StringType)
HAL_MetaType_datevisible: Property = Property(name="datevisible", type=StringType)
HAL_MetaType_financement: Property = Property(name="financement", type=StringType)
HAL_MetaType_researchteam: Property = Property(name="researchteam", type=StringType)
HAL_MetaType.attributes={HAL_MetaType_datevisible, HAL_MetaType_comment, HAL_MetaType_collaboration, HAL_MetaType_title, HAL_MetaType_isEpj, HAL_MetaType_classification, HAL_MetaType_keyword, HAL_MetaType_isEpl, HAL_MetaType_financement, HAL_MetaType_langue, HAL_MetaType_researchteam, HAL_MetaType_refInterne, HAL_MetaType_idext}

# HAL_AutLabType class attributes and methods

# Auteur class attributes and methods

# Laboratoire class attributes and methods

# HAL_Auteur class attributes and methods
HAL_Auteur_nom: Property = Property(name="nom", type=StringType)
HAL_Auteur_prenom: Property = Property(name="prenom", type=StringType)
HAL_Auteur_autrePrenom: Property = Property(name="autrePrenom", type=StringType)
HAL_Auteur_email: Property = Property(name="email", type=StringType)
HAL_Auteur_urlPerso: Property = Property(name="urlPerso", type=StringType)
HAL_Auteur.attributes={HAL_Auteur_email, HAL_Auteur_prenom, HAL_Auteur_nom, HAL_Auteur_autrePrenom, HAL_Auteur_urlPerso}

# HAL_MetaArtType class attributes and methods
HAL_MetaArtType_domain: Property = Property(name="domain", type=StringType)
HAL_MetaArtType_abstract: Property = Property(name="abstract", type=StringType)
HAL_MetaArtType.attributes={HAL_MetaArtType_domain, HAL_MetaArtType_abstract}

# MetaType class attributes and methods

# HAL_MetaArtNoticeType class attributes and methods
HAL_MetaArtNoticeType_domain: Property = Property(name="domain", type=StringType)
HAL_MetaArtNoticeType_abstract: Property = Property(name="abstract", type=StringType)
HAL_MetaArtNoticeType.attributes={HAL_MetaArtNoticeType_domain, HAL_MetaArtNoticeType_abstract}

# HAL_MetaLab class attributes and methods
HAL_MetaLab_id: Property = Property(name="id", type=StringType)
HAL_MetaLab.attributes={HAL_MetaLab_id}

# HAL_AffiliationType class attributes and methods
HAL_AffiliationType_institution: Property = Property(name="institution", type=StringType)
HAL_AffiliationType_prive: Property = Property(name="prive", type=StringType)
HAL_AffiliationType_ecole: Property = Property(name="ecole", type=StringType)
HAL_AffiliationType_universite: Property = Property(name="universite", type=StringType)
HAL_AffiliationType.attributes={HAL_AffiliationType_institution, HAL_AffiliationType_universite, HAL_AffiliationType_ecole, HAL_AffiliationType_prive}

# HAL_TamponType class attributes and methods
HAL_TamponType_id: Property = Property(name="id", type=StringType)
HAL_TamponType.attributes={HAL_TamponType_id}

# HAL_Laboratoire class attributes and methods
HAL_Laboratoire_id: Property = Property(name="id", type=StringType)
HAL_Laboratoire.attributes={HAL_Laboratoire_id}

# AbstractMetaLab class attributes and methods

# HAL_AbstractMetaLab class attributes and methods

# HAL_DepotWeb class attributes and methods
HAL_DepotWeb_format: Property = Property(name="format", type=StringType)
HAL_DepotWeb.attributes={HAL_DepotWeb_format}

# HAL_AbstractDepotType class attributes and methods

# HAL_DepotsType class attributes and methods

# AbstractDepotType class attributes and methods

# HAL_AbstractDepot class attributes and methods
HAL_AbstractDepot_nom: Property = Property(name="nom", type=StringType)
HAL_AbstractDepot.attributes={HAL_AbstractDepot_nom}

# HAL_Depot class attributes and methods
HAL_Depot_format: Property = Property(name="format", type=StringType)
HAL_Depot.attributes={HAL_Depot_format}

# HAL_WebLink class attributes and methods
HAL_WebLink_identifiant: Property = Property(name="identifiant", type=StringType)
HAL_WebLink.attributes={HAL_WebLink_identifiant}

# Server class attributes and methods

# HAL_Server class attributes and methods

# Relationships
contents1: BinaryAssociation = BinaryAssociation(
    name="contents1",
    ends={
        Property(name="Entry", type=HAL_HAL, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_HAL2", type=Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connexion0: BinaryAssociation = BinaryAssociation(
    name="connexion0",
    ends={
        Property(name="Connexion", type=HAL_HAL, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_HAL", type=Connexion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tampons4: BinaryAssociation = BinaryAssociation(
    name="tampons4",
    ends={
        Property(name="TamponType", type=HAL_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_Entry5", type=TamponType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
autLab3: BinaryAssociation = BinaryAssociation(
    name="autLab3",
    ends={
        Property(name="AutLabType", type=HAL_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_Entry", type=AutLabType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fichiers8: BinaryAssociation = BinaryAssociation(
    name="fichiers8",
    ends={
        Property(name="AbstractDepot", type=HAL_ArticleRetro, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_ArticleRetro", type=AbstractDepot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaArtNotice9: BinaryAssociation = BinaryAssociation(
    name="metaArtNotice9",
    ends={
        Property(name="MetaArtNoticeType", type=HAL_Notice, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_Notice", type=MetaArtNoticeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaArt6: BinaryAssociation = BinaryAssociation(
    name="metaArt6",
    ends={
        Property(name="MetaArtType", type=HAL_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_Article", type=MetaArtType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fichiers7: BinaryAssociation = BinaryAssociation(
    name="fichiers7",
    ends={
        Property(name="DepotsType", type=HAL_ArticleRecent, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_ArticleRecent", type=DepotsType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referenceBiblio11: BinaryAssociation = BinaryAssociation(
    name="referenceBiblio11",
    ends={
        Property(name="ReferenceBiblioType12", type=HAL_MetaArtNoticeType, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_MetaArtNoticeType", type=ReferenceBiblioType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
auteurs13: BinaryAssociation = BinaryAssociation(
    name="auteurs13",
    ends={
        Property(name="Auteur", type=HAL_AutLabType, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_AutLabType", type=Auteur, multiplicity=Multiplicity(1, 9999))
    }
)
laboratoires14: BinaryAssociation = BinaryAssociation(
    name="laboratoires14",
    ends={
        Property(name="Laboratoire", type=HAL_AutLabType, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_AutLabType15", type=Laboratoire, multiplicity=Multiplicity(1, 9999))
    }
)
referenceBiblio10: BinaryAssociation = BinaryAssociation(
    name="referenceBiblio10",
    ends={
        Property(name="ReferenceBiblioType", type=HAL_MetaArtType, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_MetaArtType", type=ReferenceBiblioType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lab16: BinaryAssociation = BinaryAssociation(
    name="lab16",
    ends={
        Property(name="Laboratoire17", type=HAL_Auteur, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_Auteur", type=Laboratoire, multiplicity=Multiplicity(0, 1))
    }
)
metas18: BinaryAssociation = BinaryAssociation(
    name="metas18",
    ends={
        Property(name="AbstractMetaLab", type=HAL_Laboratoire, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_Laboratoire", type=AbstractMetaLab, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
depots19: BinaryAssociation = BinaryAssociation(
    name="depots19",
    ends={
        Property(name="AbstractDepot20", type=HAL_DepotsType, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_DepotsType", type=AbstractDepot, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
server21: BinaryAssociation = BinaryAssociation(
    name="server21",
    ends={
        Property(name="Server", type=HAL_WebLink, multiplicity=Multiplicity(1, 1)),
        Property(name="HAL_WebLink", type=Server, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_HAL_Article_Entry = Generalization(general=Entry, specific=HAL_Article)
gen_HAL_Notice_Entry = Generalization(general=Entry, specific=HAL_Notice)
gen_HAL_ArticleRecent_Article = Generalization(general=Article, specific=HAL_ArticleRecent)
gen_HAL_ArticleRetro_Article = Generalization(general=Article, specific=HAL_ArticleRetro)
gen_HAL_WorkshopType_ReferenceBiblioType = Generalization(general=ReferenceBiblioType, specific=HAL_WorkshopType)
gen_HAL_ArtRevueType_ReferenceBiblioType = Generalization(general=ReferenceBiblioType, specific=HAL_ArtRevueType)
gen_HAL_ArtOuvrageType_ReferenceBiblioType = Generalization(general=ReferenceBiblioType, specific=HAL_ArtOuvrageType)
gen_HAL_TheseType_ReferenceBiblioType = Generalization(general=ReferenceBiblioType, specific=HAL_TheseType)
gen_HAL_OuvrageType_ReferenceBiblioType = Generalization(general=ReferenceBiblioType, specific=HAL_OuvrageType)
gen_HAL_AutreType_ReferenceBiblioType = Generalization(general=ReferenceBiblioType, specific=HAL_AutreType)
gen_HAL_BrevetType_ReferenceBiblioType = Generalization(general=ReferenceBiblioType, specific=HAL_BrevetType)
gen_HAL_ArtRevue_ArtRevueType = Generalization(general=ArtRevueType, specific=HAL_ArtRevue)
gen_HAL_ArtJournal_ArtRevueType = Generalization(general=ArtRevueType, specific=HAL_ArtJournal)
gen_HAL_Workshop_WorkshopType = Generalization(general=WorkshopType, specific=HAL_Workshop)
gen_HAL_Communication_WorkshopType = Generalization(general=WorkshopType, specific=HAL_Communication)
gen_HAL_Conference_WorkshopType = Generalization(general=WorkshopType, specific=HAL_Conference)
gen_HAL_ArtOuvrage_ArtOuvrageType = Generalization(general=ArtOuvrageType, specific=HAL_ArtOuvrage)
gen_HAL_Ouvrage_OuvrageType = Generalization(general=OuvrageType, specific=HAL_Ouvrage)
gen_HAL_Brevet_BrevetType = Generalization(general=BrevetType, specific=HAL_Brevet)
gen_HAL_Autre_AutreType = Generalization(general=AutreType, specific=HAL_Autre)
gen_HAL_These_TheseType = Generalization(general=TheseType, specific=HAL_These)
gen_HAL_MetaArtType_MetaType = Generalization(general=MetaType, specific=HAL_MetaArtType)
gen_HAL_MetaArtNoticeType_MetaType = Generalization(general=MetaType, specific=HAL_MetaArtNoticeType)
gen_HAL_MetaLab_AbstractMetaLab = Generalization(general=AbstractMetaLab, specific=HAL_MetaLab)
gen_HAL_DepotWeb_AbstractDepot = Generalization(general=AbstractDepot, specific=HAL_DepotWeb)
gen_HAL_DepotsType_AbstractDepotType = Generalization(general=AbstractDepotType, specific=HAL_DepotsType)
gen_HAL_Depot_AbstractDepot = Generalization(general=AbstractDepot, specific=HAL_Depot)
gen_HAL_WebLink_AbstractDepotType = Generalization(general=AbstractDepotType, specific=HAL_WebLink)

# Domain Model
domain_model = DomainModel(
    name="HAL",
    types={Entry, HAL_Connexion, HAL_HAL, Connexion, TamponType, HAL_Article, HAL_Entry, AutLabType, AbstractDepot, HAL_Notice, MetaArtNoticeType, MetaArtType, HAL_ArticleRecent, Article, DepotsType, HAL_ArticleRetro, HAL_WorkshopType, HAL_ReferenceBiblioType, HAL_ArtRevueType, ReferenceBiblioType, HAL_ArtOuvrageType, HAL_TheseType, HAL_OuvrageType, HAL_AutreType, HAL_BrevetType, HAL_ArtRevue, ArtRevueType, HAL_ArtJournal, HAL_Workshop, WorkshopType, HAL_Communication, HAL_Conference, HAL_ArtOuvrage, ArtOuvrageType, HAL_Ouvrage, OuvrageType, HAL_Brevet, BrevetType, HAL_Autre, AutreType, HAL_These, TheseType, HAL_MetaType, HAL_AutLabType, Auteur, Laboratoire, HAL_Auteur, HAL_MetaArtType, MetaType, HAL_MetaArtNoticeType, HAL_MetaLab, HAL_AffiliationType, HAL_TamponType, HAL_Laboratoire, AbstractMetaLab, HAL_AbstractMetaLab, HAL_DepotWeb, HAL_AbstractDepotType, HAL_DepotsType, AbstractDepotType, HAL_AbstractDepot, HAL_Depot, HAL_WebLink, Server, HAL_Server, FormatWebEnum, DateVisibleEnum, FormatEnum},
    associations={contents1, connexion0, tampons4, autLab3, fichiers8, metaArtNotice9, metaArt6, fichiers7, referenceBiblio11, auteurs13, laboratoires14, referenceBiblio10, lab16, metas18, depots19, server21},
    generalizations={gen_HAL_Article_Entry, gen_HAL_Notice_Entry, gen_HAL_ArticleRecent_Article, gen_HAL_ArticleRetro_Article, gen_HAL_WorkshopType_ReferenceBiblioType, gen_HAL_ArtRevueType_ReferenceBiblioType, gen_HAL_ArtOuvrageType_ReferenceBiblioType, gen_HAL_TheseType_ReferenceBiblioType, gen_HAL_OuvrageType_ReferenceBiblioType, gen_HAL_AutreType_ReferenceBiblioType, gen_HAL_BrevetType_ReferenceBiblioType, gen_HAL_ArtRevue_ArtRevueType, gen_HAL_ArtJournal_ArtRevueType, gen_HAL_Workshop_WorkshopType, gen_HAL_Communication_WorkshopType, gen_HAL_Conference_WorkshopType, gen_HAL_ArtOuvrage_ArtOuvrageType, gen_HAL_Ouvrage_OuvrageType, gen_HAL_Brevet_BrevetType, gen_HAL_Autre_AutreType, gen_HAL_These_TheseType, gen_HAL_MetaArtType_MetaType, gen_HAL_MetaArtNoticeType_MetaType, gen_HAL_MetaLab_AbstractMetaLab, gen_HAL_DepotWeb_AbstractDepot, gen_HAL_DepotsType_AbstractDepotType, gen_HAL_Depot_AbstractDepot, gen_HAL_WebLink_AbstractDepotType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
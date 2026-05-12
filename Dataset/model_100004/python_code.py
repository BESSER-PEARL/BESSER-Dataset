from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DateVisibleEnum(Enum):
    _15J = "15J"
    _1M = "1M"
    _3M = "3M"
    _1A = "1A"
    _2A = "2A"
    JAMAIS = "JAMAIS"
class FormatWebEnum(Enum):
    XML = "XML"
    HTML = "HTML"
    HTM = "HTM"
class FormatEnum(Enum):
    ANNEX = "ANNEX"
    PDF = "PDF"
    TEX = "TEX"
    DOC = "DOC"
    RTF = "RTF"
    TXT = "TXT"
    PS = "PS"


############################################
# Definition of Classes
############################################

class HAL_Server:

    pass
class Server:

    pass
class HAL_AbstractDepot(ABC):

    def __init__(self, nom: str):
        self.nom = nom
        
        pass
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom


class AbstractDepotType:

    pass
class HAL_WebLink(AbstractDepotType):

    def __init__(self, identifiant: str, HAL_WebLink: "Server" = None):
        self.identifiant = identifiant
        self.HAL_WebLink = HAL_WebLink
        
        pass
    @property
    def identifiant(self):
        return self.__identifiant

    @identifiant.setter
    def identifiant(self, identifiant: str):
        self.__identifiant = identifiant


    @property
    def HAL_WebLink(self):
        return self.__HAL_WebLink

    @HAL_WebLink.setter
    def HAL_WebLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HAL_WebLink__HAL_WebLink", None)
        self.__HAL_WebLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Server"):
                opp_val = getattr(old_value, "Server", None)
                if opp_val == self:
                    setattr(old_value, "Server", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Server"):
                opp_val = getattr(value, "Server", None)
                setattr(value, "Server", self)

class HAL_DepotsType(AbstractDepotType):

    pass
class HAL_AbstractDepotType(ABC):

    pass
class HAL_AbstractMetaLab(ABC):

    pass
class AbstractMetaLab:

    pass
class HAL_Laboratoire:

    def __init__(self, id: str, HAL_Laboratoire: "AbstractMetaLab" = None):
        self.id = id
        self.HAL_Laboratoire = HAL_Laboratoire
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def HAL_Laboratoire(self):
        return self.__HAL_Laboratoire

    @HAL_Laboratoire.setter
    def HAL_Laboratoire(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HAL_Laboratoire__HAL_Laboratoire", None)
        self.__HAL_Laboratoire = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractMetaLab"):
                opp_val = getattr(old_value, "AbstractMetaLab", None)
                if opp_val == self:
                    setattr(old_value, "AbstractMetaLab", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractMetaLab"):
                opp_val = getattr(value, "AbstractMetaLab", None)
                setattr(value, "AbstractMetaLab", self)

class HAL_TamponType:

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class HAL_AffiliationType:

    def __init__(self, institution: str, prive: str, ecole: str, universite: str):
        self.institution = institution
        self.prive = prive
        self.ecole = ecole
        self.universite = universite
        
        pass
    @property
    def institution(self):
        return self.__institution

    @institution.setter
    def institution(self, institution: str):
        self.__institution = institution


    @property
    def prive(self):
        return self.__prive

    @prive.setter
    def prive(self, prive: str):
        self.__prive = prive


    @property
    def universite(self):
        return self.__universite

    @universite.setter
    def universite(self, universite: str):
        self.__universite = universite


    @property
    def ecole(self):
        return self.__ecole

    @ecole.setter
    def ecole(self, ecole: str):
        self.__ecole = ecole


class HAL_MetaLab(AbstractMetaLab):

    def __init__(self, id: str, AbstractMetaLab: "HAL_Laboratoire" = None):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class MetaType:

    pass
class HAL_MetaArtNoticeType(MetaType):

    def __init__(self, domain: str, abstract: str, HAL_MetaArtNoticeType: "ReferenceBiblioType" = None):
        self.domain = domain
        self.abstract = abstract
        self.HAL_MetaArtNoticeType = HAL_MetaArtNoticeType
        
        pass
    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def HAL_MetaArtNoticeType(self):
        return self.__HAL_MetaArtNoticeType

    @HAL_MetaArtNoticeType.setter
    def HAL_MetaArtNoticeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HAL_MetaArtNoticeType__HAL_MetaArtNoticeType", None)
        self.__HAL_MetaArtNoticeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReferenceBiblioType12"):
                opp_val = getattr(old_value, "ReferenceBiblioType12", None)
                if opp_val == self:
                    setattr(old_value, "ReferenceBiblioType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReferenceBiblioType12"):
                opp_val = getattr(value, "ReferenceBiblioType12", None)
                setattr(value, "ReferenceBiblioType12", self)

class HAL_MetaArtType(MetaType):

    def __init__(self, domain: str, abstract: str, HAL_MetaArtType: "ReferenceBiblioType" = None):
        self.domain = domain
        self.abstract = abstract
        self.HAL_MetaArtType = HAL_MetaArtType
        
        pass
    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def HAL_MetaArtType(self):
        return self.__HAL_MetaArtType

    @HAL_MetaArtType.setter
    def HAL_MetaArtType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HAL_MetaArtType__HAL_MetaArtType", None)
        self.__HAL_MetaArtType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReferenceBiblioType"):
                opp_val = getattr(old_value, "ReferenceBiblioType", None)
                if opp_val == self:
                    setattr(old_value, "ReferenceBiblioType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReferenceBiblioType"):
                opp_val = getattr(value, "ReferenceBiblioType", None)
                setattr(value, "ReferenceBiblioType", self)

class HAL_Auteur:

    def __init__(self, nom: str, prenom: str, autrePrenom: str, email: str, urlPerso: str, HAL_Auteur: "Laboratoire" = None):
        self.nom = nom
        self.prenom = prenom
        self.autrePrenom = autrePrenom
        self.email = email
        self.urlPerso = urlPerso
        self.HAL_Auteur = HAL_Auteur
        
        pass
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def urlPerso(self):
        return self.__urlPerso

    @urlPerso.setter
    def urlPerso(self, urlPerso: str):
        self.__urlPerso = urlPerso


    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom


    @property
    def autrePrenom(self):
        return self.__autrePrenom

    @autrePrenom.setter
    def autrePrenom(self, autrePrenom: str):
        self.__autrePrenom = autrePrenom


    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom


    @property
    def HAL_Auteur(self):
        return self.__HAL_Auteur

    @HAL_Auteur.setter
    def HAL_Auteur(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HAL_Auteur__HAL_Auteur", None)
        self.__HAL_Auteur = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Laboratoire17"):
                opp_val = getattr(old_value, "Laboratoire17", None)
                if opp_val == self:
                    setattr(old_value, "Laboratoire17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Laboratoire17"):
                opp_val = getattr(value, "Laboratoire17", None)
                setattr(value, "Laboratoire17", self)

class Laboratoire:

    pass
class Auteur:

    pass
class HAL_AutLabType:

    pass
class HAL_MetaType(ABC):

    def __init__(self, langue: str, title: str, comment: str, refInterne: str, idext: str, isEpj: str, isEpl: str, classification: str, collaboration: str, keyword: str, datevisible: str, financement: str, researchteam: str):
        self.langue = langue
        self.title = title
        self.comment = comment
        self.refInterne = refInterne
        self.idext = idext
        self.isEpj = isEpj
        self.isEpl = isEpl
        self.classification = classification
        self.collaboration = collaboration
        self.keyword = keyword
        self.datevisible = datevisible
        self.financement = financement
        self.researchteam = researchteam
        
        pass
    @property
    def datevisible(self):
        return self.__datevisible

    @datevisible.setter
    def datevisible(self, datevisible: str):
        self.__datevisible = datevisible


    @property
    def idext(self):
        return self.__idext

    @idext.setter
    def idext(self, idext: str):
        self.__idext = idext


    @property
    def isEpl(self):
        return self.__isEpl

    @isEpl.setter
    def isEpl(self, isEpl: str):
        self.__isEpl = isEpl


    @property
    def classification(self):
        return self.__classification

    @classification.setter
    def classification(self, classification: str):
        self.__classification = classification


    @property
    def collaboration(self):
        return self.__collaboration

    @collaboration.setter
    def collaboration(self, collaboration: str):
        self.__collaboration = collaboration


    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def langue(self):
        return self.__langue

    @langue.setter
    def langue(self, langue: str):
        self.__langue = langue


    @property
    def refInterne(self):
        return self.__refInterne

    @refInterne.setter
    def refInterne(self, refInterne: str):
        self.__refInterne = refInterne


    @property
    def researchteam(self):
        return self.__researchteam

    @researchteam.setter
    def researchteam(self, researchteam: str):
        self.__researchteam = researchteam


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def financement(self):
        return self.__financement

    @financement.setter
    def financement(self, financement: str):
        self.__financement = financement


    @property
    def isEpj(self):
        return self.__isEpj

    @isEpj.setter
    def isEpj(self, isEpj: str):
        self.__isEpj = isEpj


class TheseType:

    pass
class HAL_These(TheseType):

    pass
class AutreType:

    pass
class HAL_Autre(AutreType):

    pass
class BrevetType:

    pass
class HAL_Brevet(BrevetType):

    pass
class OuvrageType:

    pass
class HAL_Ouvrage(OuvrageType):

    pass
class ArtOuvrageType:

    pass
class HAL_ArtOuvrage(ArtOuvrageType):

    pass
class WorkshopType:

    pass
class HAL_Conference(WorkshopType):

    pass
class HAL_Communication(WorkshopType):

    pass
class HAL_Workshop(WorkshopType):

    pass
class ArtRevueType:

    pass
class HAL_ArtJournal(ArtRevueType):

    pass
class HAL_ArtRevue(ArtRevueType):

    pass
class ReferenceBiblioType:

    pass
class HAL_BrevetType(ReferenceBiblioType):

    def __init__(self, numbrevet: str, page: str, pays: str, datebrevet: str, ReferenceBiblioType: "HAL_MetaArtType" = None, ReferenceBiblioType12: "HAL_MetaArtNoticeType" = None):
        self.numbrevet = numbrevet
        self.page = page
        self.pays = pays
        self.datebrevet = datebrevet
        
        pass
    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page: str):
        self.__page = page


    @property
    def datebrevet(self):
        return self.__datebrevet

    @datebrevet.setter
    def datebrevet(self, datebrevet: str):
        self.__datebrevet = datebrevet


    @property
    def pays(self):
        return self.__pays

    @pays.setter
    def pays(self, pays: str):
        self.__pays = pays


    @property
    def numbrevet(self):
        return self.__numbrevet

    @numbrevet.setter
    def numbrevet(self, numbrevet: str):
        self.__numbrevet = numbrevet


class HAL_TheseType(ReferenceBiblioType):

    def __init__(self, orgthe: str, niveau: str, defencedate: str, directeur: str, codirecteur: str, ReferenceBiblioType: "HAL_MetaArtType" = None, ReferenceBiblioType12: "HAL_MetaArtNoticeType" = None):
        self.orgthe = orgthe
        self.niveau = niveau
        self.defencedate = defencedate
        self.directeur = directeur
        self.codirecteur = codirecteur
        
        pass
    @property
    def codirecteur(self):
        return self.__codirecteur

    @codirecteur.setter
    def codirecteur(self, codirecteur: str):
        self.__codirecteur = codirecteur


    @property
    def directeur(self):
        return self.__directeur

    @directeur.setter
    def directeur(self, directeur: str):
        self.__directeur = directeur


    @property
    def niveau(self):
        return self.__niveau

    @niveau.setter
    def niveau(self, niveau: str):
        self.__niveau = niveau


    @property
    def defencedate(self):
        return self.__defencedate

    @defencedate.setter
    def defencedate(self, defencedate: str):
        self.__defencedate = defencedate


    @property
    def orgthe(self):
        return self.__orgthe

    @orgthe.setter
    def orgthe(self, orgthe: str):
        self.__orgthe = orgthe


class HAL_AutreType(ReferenceBiblioType):

    def __init__(self, urldoi: str, annee: str, description: str, ReferenceBiblioType: "HAL_MetaArtType" = None, ReferenceBiblioType12: "HAL_MetaArtNoticeType" = None):
        self.urldoi = urldoi
        self.annee = annee
        self.description = description
        
        pass
    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, annee: str):
        self.__annee = annee


    @property
    def urldoi(self):
        return self.__urldoi

    @urldoi.setter
    def urldoi(self, urldoi: str):
        self.__urldoi = urldoi


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class HAL_ArtOuvrageType(ReferenceBiblioType):

    def __init__(self, serie: str, urldoi: str, titouv: str, edcom: str, annee: str, edsci: str, ReferenceBiblioType: "HAL_MetaArtType" = None, ReferenceBiblioType12: "HAL_MetaArtNoticeType" = None):
        self.serie = serie
        self.urldoi = urldoi
        self.titouv = titouv
        self.edcom = edcom
        self.annee = annee
        self.edsci = edsci
        
        pass
    @property
    def edsci(self):
        return self.__edsci

    @edsci.setter
    def edsci(self, edsci: str):
        self.__edsci = edsci


    @property
    def edcom(self):
        return self.__edcom

    @edcom.setter
    def edcom(self, edcom: str):
        self.__edcom = edcom


    @property
    def urldoi(self):
        return self.__urldoi

    @urldoi.setter
    def urldoi(self, urldoi: str):
        self.__urldoi = urldoi


    @property
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, serie: str):
        self.__serie = serie


    @property
    def titouv(self):
        return self.__titouv

    @titouv.setter
    def titouv(self, titouv: str):
        self.__titouv = titouv


    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, annee: str):
        self.__annee = annee


class HAL_OuvrageType(ReferenceBiblioType):

    def __init__(self, edcom: str, annee: str, page: str, urldoi: str, ReferenceBiblioType: "HAL_MetaArtType" = None, ReferenceBiblioType12: "HAL_MetaArtNoticeType" = None):
        self.edcom = edcom
        self.annee = annee
        self.page = page
        self.urldoi = urldoi
        
        pass
    @property
    def urldoi(self):
        return self.__urldoi

    @urldoi.setter
    def urldoi(self, urldoi: str):
        self.__urldoi = urldoi


    @property
    def edcom(self):
        return self.__edcom

    @edcom.setter
    def edcom(self, edcom: str):
        self.__edcom = edcom


    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, annee: str):
        self.__annee = annee


    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page: str):
        self.__page = page


class HAL_ArtRevueType(ReferenceBiblioType):

    def __init__(self, page: str, annee: str, urldoi: str, journal: str, volume: str, ReferenceBiblioType: "HAL_MetaArtType" = None, ReferenceBiblioType12: "HAL_MetaArtNoticeType" = None):
        self.page = page
        self.annee = annee
        self.urldoi = urldoi
        self.journal = journal
        self.volume = volume
        
        pass
    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, annee: str):
        self.__annee = annee


    @property
    def urldoi(self):
        return self.__urldoi

    @urldoi.setter
    def urldoi(self, urldoi: str):
        self.__urldoi = urldoi


    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page: str):
        self.__page = page


    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal


class HAL_ReferenceBiblioType(ABC):

    pass
class HAL_WorkshopType(ReferenceBiblioType):

    def __init__(self, serie: str, urldoi: str, titconf: str, ville: str, pays: str, edcom: str, annee: str, page: str, edsci: str, ReferenceBiblioType: "HAL_MetaArtType" = None, ReferenceBiblioType12: "HAL_MetaArtNoticeType" = None):
        self.serie = serie
        self.urldoi = urldoi
        self.titconf = titconf
        self.ville = ville
        self.pays = pays
        self.edcom = edcom
        self.annee = annee
        self.page = page
        self.edsci = edsci
        
        pass
    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, annee: str):
        self.__annee = annee


    @property
    def urldoi(self):
        return self.__urldoi

    @urldoi.setter
    def urldoi(self, urldoi: str):
        self.__urldoi = urldoi


    @property
    def titconf(self):
        return self.__titconf

    @titconf.setter
    def titconf(self, titconf: str):
        self.__titconf = titconf


    @property
    def edcom(self):
        return self.__edcom

    @edcom.setter
    def edcom(self, edcom: str):
        self.__edcom = edcom


    @property
    def ville(self):
        return self.__ville

    @ville.setter
    def ville(self, ville: str):
        self.__ville = ville


    @property
    def edsci(self):
        return self.__edsci

    @edsci.setter
    def edsci(self, edsci: str):
        self.__edsci = edsci


    @property
    def pays(self):
        return self.__pays

    @pays.setter
    def pays(self, pays: str):
        self.__pays = pays


    @property
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, serie: str):
        self.__serie = serie


    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page: str):
        self.__page = page


class DepotsType:

    pass
class Article:

    pass
class HAL_ArticleRetro(Article):

    def __init__(self, dateRedaction: str, HAL_ArticleRetro: "AbstractDepot" = None):
        self.dateRedaction = dateRedaction
        self.HAL_ArticleRetro = HAL_ArticleRetro
        
        pass
    @property
    def dateRedaction(self):
        return self.__dateRedaction

    @dateRedaction.setter
    def dateRedaction(self, dateRedaction: str):
        self.__dateRedaction = dateRedaction


    @property
    def HAL_ArticleRetro(self):
        return self.__HAL_ArticleRetro

    @HAL_ArticleRetro.setter
    def HAL_ArticleRetro(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HAL_ArticleRetro__HAL_ArticleRetro", None)
        self.__HAL_ArticleRetro = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractDepot"):
                opp_val = getattr(old_value, "AbstractDepot", None)
                if opp_val == self:
                    setattr(old_value, "AbstractDepot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractDepot"):
                opp_val = getattr(value, "AbstractDepot", None)
                setattr(value, "AbstractDepot", self)

class HAL_ArticleRecent(Article):

    pass
class MetaArtType:

    pass
class MetaArtNoticeType:

    pass
class AbstractDepot:

    pass
class HAL_Depot(AbstractDepot):

    def __init__(self, format: str, AbstractDepot: "HAL_ArticleRetro" = None, AbstractDepot20: "HAL_DepotsType" = None):
        self.format = format
        
        pass
    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format


class HAL_DepotWeb(AbstractDepot):

    def __init__(self, format: str, AbstractDepot: "HAL_ArticleRetro" = None, AbstractDepot20: "HAL_DepotsType" = None):
        self.format = format
        
        pass
    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format


class AutLabType:

    pass
class HAL_Entry(ABC):

    pass
class TamponType:

    pass
class Connexion:

    pass
class HAL_HAL:

    pass
class HAL_Connexion:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login


class Entry:

    pass
class HAL_Article(Entry):

    pass
class HAL_Notice(Entry):

    pass
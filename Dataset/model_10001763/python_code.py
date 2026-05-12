from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class __table___T_Services:

    def __init__(self, numeroService: int, numeroUtilisateur: int, type: str, titre: str, description: str, nbParticipants: int, date: date):
        self.numeroService = numeroService
        self.numeroUtilisateur = numeroUtilisateur
        self.type = type
        self.titre = titre
        self.description = description
        self.nbParticipants = nbParticipants
        self.date = date
        
        pass
    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, titre: str):
        self.__titre = titre

    @property
    def numeroUtilisateur(self):
        return self.__numeroUtilisateur
    @numeroUtilisateur.setter
    def numeroUtilisateur(self, numeroUtilisateur: int):
        self.__numeroUtilisateur = numeroUtilisateur

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def numeroService(self):
        return self.__numeroService
    @numeroService.setter
    def numeroService(self, numeroService: int):
        self.__numeroService = numeroService

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def nbParticipants(self):
        return self.__nbParticipants
    @nbParticipants.setter
    def nbParticipants(self, nbParticipants: int):
        self.__nbParticipants = nbParticipants



class __table___T_CompteDeLUtilisateur:

    def __init__(self, numeroUtilisateur: int, pseudo: str, adresseMail: str, motDePasse: str, type: str):
        self.numeroUtilisateur = numeroUtilisateur
        self.pseudo = pseudo
        self.adresseMail = adresseMail
        self.motDePasse = motDePasse
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def numeroUtilisateur(self):
        return self.__numeroUtilisateur
    @numeroUtilisateur.setter
    def numeroUtilisateur(self, numeroUtilisateur: int):
        self.__numeroUtilisateur = numeroUtilisateur

    @property
    def motDePasse(self):
        return self.__motDePasse
    @motDePasse.setter
    def motDePasse(self, motDePasse: str):
        self.__motDePasse = motDePasse

    @property
    def pseudo(self):
        return self.__pseudo
    @pseudo.setter
    def pseudo(self, pseudo: str):
        self.__pseudo = pseudo

    @property
    def adresseMail(self):
        return self.__adresseMail
    @adresseMail.setter
    def adresseMail(self, adresseMail: str):
        self.__adresseMail = adresseMail



class AffichageAccueil:

    pass


class RechercheAvancee:

    def __init__(self, Titre: str, Association: Association, GenreService: Service, NbParticipants: int, Date: date):
        self.Titre = Titre
        self.Association = Association
        self.GenreService = GenreService
        self.NbParticipants = NbParticipants
        self.Date = Date
        
        pass
    @property
    def Titre(self):
        return self.__Titre
    @Titre.setter
    def Titre(self, Titre: str):
        self.__Titre = Titre

    @property
    def Association(self):
        return self.__Association
    @Association.setter
    def Association(self, Association: Association):
        self.__Association = Association

    @property
    def GenreService(self):
        return self.__GenreService
    @GenreService.setter
    def GenreService(self, GenreService: Service):
        self.__GenreService = GenreService

    @property
    def NbParticipants(self):
        return self.__NbParticipants
    @NbParticipants.setter
    def NbParticipants(self, NbParticipants: int):
        self.__NbParticipants = NbParticipants

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date



class RechercheRapide:

    def __init__(self, MotsCles: str):
        self.MotsCles = MotsCles
        
        pass
    @property
    def MotsCles(self):
        return self.__MotsCles
    @MotsCles.setter
    def MotsCles(self, MotsCles: str):
        self.__MotsCles = MotsCles



class Contacter:

    def __init__(self, personne: Utilisateur):
        self.personne = personne
        
        pass
    @property
    def personne(self):
        return self.__personne
    @personne.setter
    def personne(self, personne: Utilisateur):
        self.__personne = personne



class AffichageDetailleResultat:

    pass


class SelectionnerUnResultat:

    pass


class AffichageResultats:

    pass


class CritereDeRecherche:

    def __init__(self, critere: str):
        self.critere = critere
        
        pass
    @property
    def critere(self):
        return self.__critere
    @critere.setter
    def critere(self, critere: str):
        self.__critere = critere



class DemandeDeService1:

    pass


class PropositionDeService1:

    pass


class CompteDeLUtilisateur1:

    def __init__(self, peudo: str, adresseMail: str, motDePasse: str, Type: str):
        self.peudo = peudo
        self.adresseMail = adresseMail
        self.motDePasse = motDePasse
        self.Type = Type
        
        pass
    @property
    def motDePasse(self):
        return self.__motDePasse
    @motDePasse.setter
    def motDePasse(self, motDePasse: str):
        self.__motDePasse = motDePasse

    @property
    def adresseMail(self):
        return self.__adresseMail
    @adresseMail.setter
    def adresseMail(self, adresseMail: str):
        self.__adresseMail = adresseMail

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def peudo(self):
        return self.__peudo
    @peudo.setter
    def peudo(self, peudo: str):
        self.__peudo = peudo



class Utilisateur1:

    pass


class RechercheDemandes:

    def __init__(self, criteres: str):
        self.criteres = criteres
        
        pass
    @property
    def criteres(self):
        return self.__criteres
    @criteres.setter
    def criteres(self, criteres: str):
        self.__criteres = criteres



class RecherchePropositions:

    def __init__(self, criteres: str):
        self.criteres = criteres
        
        pass
    @property
    def criteres(self):
        return self.__criteres
    @criteres.setter
    def criteres(self, criteres: str):
        self.__criteres = criteres



class DemandeDeService:

    pass


class PropositionDeService:

    pass


class CompteDeLUtilisateur:

    def __init__(self, peudo: str, adresseMail: str, motDePasse: str, Type: str):
        self.peudo = peudo
        self.adresseMail = adresseMail
        self.motDePasse = motDePasse
        self.Type = Type
        
        pass
    @property
    def motDePasse(self):
        return self.__motDePasse
    @motDePasse.setter
    def motDePasse(self, motDePasse: str):
        self.__motDePasse = motDePasse

    @property
    def peudo(self):
        return self.__peudo
    @peudo.setter
    def peudo(self, peudo: str):
        self.__peudo = peudo

    @property
    def adresseMail(self):
        return self.__adresseMail
    @adresseMail.setter
    def adresseMail(self, adresseMail: str):
        self.__adresseMail = adresseMail

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type



class Utilisateur:

    pass


class Resultat:

    def __init__(self, Liste: Resultat_Recherche):
        self.Liste = Liste
        
        pass
    @property
    def Liste(self):
        return self.__Liste
    @Liste.setter
    def Liste(self, Liste: Resultat_Recherche):
        self.__Liste = Liste



class RechercheDAssociations:

    def __init__(self, criteres: str):
        self.criteres = criteres
        
        pass
    @property
    def criteres(self):
        return self.__criteres
    @criteres.setter
    def criteres(self, criteres: str):
        self.__criteres = criteres



class Systeme:

    pass


class Acteurs:

    pass


class Recherche_Rapide:

    def __init__(self, MotsCles: str):
        self.MotsCles = MotsCles
        
        pass
    @property
    def MotsCles(self):
        return self.__MotsCles
    @MotsCles.setter
    def MotsCles(self, MotsCles: str):
        self.__MotsCles = MotsCles



class Resultat_Recherche:

    pass


class Recherche_Avanc_e:

    def __init__(self, Titre: str, Association: Association, Pays: str, NbParticipants: int, Date: date):
        self.Titre = Titre
        self.Association = Association
        self.Pays = Pays
        self.NbParticipants = NbParticipants
        self.Date = Date
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def Pays(self):
        return self.__Pays
    @Pays.setter
    def Pays(self, Pays: str):
        self.__Pays = Pays

    @property
    def NbParticipants(self):
        return self.__NbParticipants
    @NbParticipants.setter
    def NbParticipants(self, NbParticipants: int):
        self.__NbParticipants = NbParticipants

    @property
    def Titre(self):
        return self.__Titre
    @Titre.setter
    def Titre(self, Titre: str):
        self.__Titre = Titre

    @property
    def Association(self):
        return self.__Association
    @Association.setter
    def Association(self, Association: Association):
        self.__Association = Association



class Membre1:

    pass


class Service:

    def __init__(self, description: str, association2: "Association" = None, membre4: set["Membre"] = None):
        self.description = description
        self.association2 = association2
        self.membre4 = membre4 if membre4 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def membre4(self):
        return self.__membre4
    @membre4.setter
    def membre4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__membre4", None)
        self.__membre4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service5"):
                    opp_val = getattr(item, "service5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service5"):
                    opp_val = getattr(item, "service5", None)
                    
                    if opp_val is None:
                        setattr(item, "service5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def association2(self):
        return self.__association2
    @association2.setter
    def association2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__association2", None)
        self.__association2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service3"):
                opp_val = getattr(old_value, "service3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service3"):
                opp_val = getattr(value, "service3", None)
                if opp_val is None:
                    setattr(value, "service3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Association:

    def __init__(self, nom___unicef: str, membre0: set["Membre"] = None, service3: set["Service"] = None):
        self.nom___unicef = nom___unicef
        self.membre0 = membre0 if membre0 is not None else set()
        self.service3 = service3 if service3 is not None else set()
        
        pass
    @property
    def nom___unicef(self):
        return self.__nom___unicef
    @nom___unicef.setter
    def nom___unicef(self, nom___unicef: str):
        self.__nom___unicef = nom___unicef

    @property
    def service3(self):
        return self.__service3
    @service3.setter
    def service3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Association__service3", None)
        self.__service3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "association2"):
                    opp_val = getattr(item, "association2", None)
                    
                    if opp_val == self:
                        setattr(item, "association2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "association2"):
                    opp_val = getattr(item, "association2", None)
                    
                    setattr(item, "association2", self)
                    

    @property
    def membre0(self):
        return self.__membre0
    @membre0.setter
    def membre0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Association__membre0", None)
        self.__membre0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "association1"):
                    opp_val = getattr(item, "association1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "association1"):
                    opp_val = getattr(item, "association1", None)
                    
                    if opp_val is None:
                        setattr(item, "association1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Membre:

    def __init__(self, nom___salim_talout: str, association1: set["Association"] = None, service5: set["Service"] = None):
        self.nom___salim_talout = nom___salim_talout
        self.association1 = association1 if association1 is not None else set()
        self.service5 = service5 if service5 is not None else set()
        
        pass
    @property
    def nom___salim_talout(self):
        return self.__nom___salim_talout
    @nom___salim_talout.setter
    def nom___salim_talout(self, nom___salim_talout: str):
        self.__nom___salim_talout = nom___salim_talout

    @property
    def service5(self):
        return self.__service5
    @service5.setter
    def service5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Membre__service5", None)
        self.__service5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "membre4"):
                    opp_val = getattr(item, "membre4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "membre4"):
                    opp_val = getattr(item, "membre4", None)
                    
                    if opp_val is None:
                        setattr(item, "membre4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def association1(self):
        return self.__association1
    @association1.setter
    def association1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Membre__association1", None)
        self.__association1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "membre0"):
                    opp_val = getattr(item, "membre0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "membre0"):
                    opp_val = getattr(item, "membre0", None)
                    
                    if opp_val is None:
                        setattr(item, "membre0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    


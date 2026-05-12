from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class domain_Role(Enum):
    pass

############################################
# Definition of Classes
############################################










class domain_Reservation:

    def __init__(self, id2: int, id: int, dateReservation: date, profil12: set["domain_Profil"] = None, trajet14: "domain_Trajet" = None):
        self.id2 = id2
        self.id = id
        self.dateReservation = dateReservation
        self.profil12 = profil12 if profil12 is not None else set()
        self.trajet14 = trajet14
        
        pass
    @property
    def dateReservation(self):
        return self.__dateReservation
    @dateReservation.setter
    def dateReservation(self, dateReservation: date):
        self.__dateReservation = dateReservation

    @property
    def id2(self):
        return self.__id2
    @id2.setter
    def id2(self, id2: int):
        self.__id2 = id2

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def trajet14(self):
        return self.__trajet14
    @trajet14.setter
    def trajet14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Reservation__trajet14", None)
        self.__trajet14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservation15"):
                opp_val = getattr(old_value, "reservation15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservation15"):
                opp_val = getattr(value, "reservation15", None)
                if opp_val is None:
                    setattr(value, "reservation15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def profil12(self):
        return self.__profil12
    @profil12.setter
    def profil12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Reservation__profil12", None)
        self.__profil12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservation13"):
                    opp_val = getattr(item, "reservation13", None)
                    
                    if opp_val == self:
                        setattr(item, "reservation13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservation13"):
                    opp_val = getattr(item, "reservation13", None)
                    
                    setattr(item, "reservation13", self)
                    



class domain_Avis:

    def __init__(self, commentaire: str, note: int, id: int, personne4: "domain_Profil" = None, evenement6: "domain_Trajet" = None):
        self.commentaire = commentaire
        self.note = note
        self.id = id
        self.personne4 = personne4
        self.evenement6 = evenement6
        
        pass
    @property
    def commentaire(self):
        return self.__commentaire
    @commentaire.setter
    def commentaire(self, commentaire: str):
        self.__commentaire = commentaire

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note: int):
        self.__note = note

    @property
    def personne4(self):
        return self.__personne4
    @personne4.setter
    def personne4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Avis__personne4", None)
        self.__personne4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avis5"):
                opp_val = getattr(old_value, "avis5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avis5"):
                opp_val = getattr(value, "avis5", None)
                if opp_val is None:
                    setattr(value, "avis5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def evenement6(self):
        return self.__evenement6
    @evenement6.setter
    def evenement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Avis__evenement6", None)
        self.__evenement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avis7"):
                opp_val = getattr(old_value, "avis7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avis7"):
                opp_val = getattr(value, "avis7", None)
                if opp_val is None:
                    setattr(value, "avis7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class domain_Ville:

    def __init__(self, id: int, nom: str, cp: int, personnes9: set["domain_Profil"] = None, trajet11: "domain_Trajet" = None):
        self.id = id
        self.nom = nom
        self.cp = cp
        self.personnes9 = personnes9 if personnes9 is not None else set()
        self.trajet11 = trajet11
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def cp(self):
        return self.__cp
    @cp.setter
    def cp(self, cp: int):
        self.__cp = cp

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def personnes9(self):
        return self.__personnes9
    @personnes9.setter
    def personnes9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Ville__personnes9", None)
        self.__personnes9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adresse8"):
                    opp_val = getattr(item, "adresse8", None)
                    
                    if opp_val == self:
                        setattr(item, "adresse8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adresse8"):
                    opp_val = getattr(item, "adresse8", None)
                    
                    setattr(item, "adresse8", self)
                    

    @property
    def trajet11(self):
        return self.__trajet11
    @trajet11.setter
    def trajet11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Ville__trajet11", None)
        self.__trajet11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ville10"):
                opp_val = getattr(old_value, "ville10", None)
                if opp_val == self:
                    setattr(old_value, "ville10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ville10"):
                opp_val = getattr(value, "ville10", None)
                setattr(value, "ville10", self)



class domain_Trajet:

    def __init__(self, id: int, date: date, depart: domain_Ville, destination: domain_Ville, prix: int, participants3: set["domain_Profil"] = None, avis7: set["domain_Avis"] = None, ville10: "domain_Ville" = None, reservation15: set["domain_Reservation"] = None):
        self.id = id
        self.date = date
        self.depart = depart
        self.destination = destination
        self.prix = prix
        self.participants3 = participants3 if participants3 is not None else set()
        self.avis7 = avis7 if avis7 is not None else set()
        self.ville10 = ville10
        self.reservation15 = reservation15 if reservation15 is not None else set()
        
        pass
    @property
    def depart(self):
        return self.__depart
    @depart.setter
    def depart(self, depart: domain_Ville):
        self.__depart = depart

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix: int):
        self.__prix = prix

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: domain_Ville):
        self.__destination = destination

    @property
    def ville10(self):
        return self.__ville10
    @ville10.setter
    def ville10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Trajet__ville10", None)
        self.__ville10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet11"):
                opp_val = getattr(old_value, "trajet11", None)
                if opp_val == self:
                    setattr(old_value, "trajet11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet11"):
                opp_val = getattr(value, "trajet11", None)
                setattr(value, "trajet11", self)

    @property
    def participants3(self):
        return self.__participants3
    @participants3.setter
    def participants3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Trajet__participants3", None)
        self.__participants3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events2"):
                    opp_val = getattr(item, "events2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events2"):
                    opp_val = getattr(item, "events2", None)
                    
                    if opp_val is None:
                        setattr(item, "events2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def avis7(self):
        return self.__avis7
    @avis7.setter
    def avis7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Trajet__avis7", None)
        self.__avis7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "evenement6"):
                    opp_val = getattr(item, "evenement6", None)
                    
                    if opp_val == self:
                        setattr(item, "evenement6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "evenement6"):
                    opp_val = getattr(item, "evenement6", None)
                    
                    setattr(item, "evenement6", self)
                    

    @property
    def reservation15(self):
        return self.__reservation15
    @reservation15.setter
    def reservation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Trajet__reservation15", None)
        self.__reservation15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trajet14"):
                    opp_val = getattr(item, "trajet14", None)
                    
                    if opp_val == self:
                        setattr(item, "trajet14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trajet14"):
                    opp_val = getattr(item, "trajet14", None)
                    
                    setattr(item, "trajet14", self)
                    



class domain_Authentification:

    def __init__(self, id: str, password: str, personne1: set["domain_Profil"] = None):
        self.id = id
        self.password = password
        self.personne1 = personne1 if personne1 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def personne1(self):
        return self.__personne1
    @personne1.setter
    def personne1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Authentification__personne1", None)
        self.__personne1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cr_e0"):
                    opp_val = getattr(item, "Cr_e0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cr_e0"):
                    opp_val = getattr(item, "Cr_e0", None)
                    
                    if opp_val is None:
                        setattr(item, "Cr_e0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class domain_Voiture:

    def __init__(self, id: int, model: str, marque: str, confort: str, nbPlaces: int, categorie: str, Profil17: "domain_Profil" = None):
        self.id = id
        self.model = model
        self.marque = marque
        self.confort = confort
        self.nbPlaces = nbPlaces
        self.categorie = categorie
        self.Profil17 = Profil17
        
        pass
    @property
    def categorie(self):
        return self.__categorie
    @categorie.setter
    def categorie(self, categorie: str):
        self.__categorie = categorie

    @property
    def confort(self):
        return self.__confort
    @confort.setter
    def confort(self, confort: str):
        self.__confort = confort

    @property
    def nbPlaces(self):
        return self.__nbPlaces
    @nbPlaces.setter
    def nbPlaces(self, nbPlaces: int):
        self.__nbPlaces = nbPlaces

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self, marque: str):
        self.__marque = marque

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Profil17(self):
        return self.__Profil17
    @Profil17.setter
    def Profil17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Voiture__Profil17", None)
        self.__Profil17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voiture16"):
                opp_val = getattr(old_value, "voiture16", None)
                if opp_val == self:
                    setattr(old_value, "voiture16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voiture16"):
                opp_val = getattr(value, "voiture16", None)
                setattr(value, "voiture16", self)



class domain_Profil:

    def __init__(self, id: int, nom: str, prenom: str, tel: str, mail: str, role: domain_Role, Cr_e0: set["domain_Authentification"] = None, events2: set["domain_Trajet"] = None, avis5: set["domain_Avis"] = None, adresse8: "domain_Ville" = None, reservation13: "domain_Reservation" = None, voiture16: "domain_Voiture" = None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail
        self.role = role
        self.Cr_e0 = Cr_e0 if Cr_e0 is not None else set()
        self.events2 = events2 if events2 is not None else set()
        self.avis5 = avis5 if avis5 is not None else set()
        self.adresse8 = adresse8
        self.reservation13 = reservation13
        self.voiture16 = voiture16
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self, tel: str):
        self.__tel = tel

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role: domain_Role):
        self.__role = role

    @property
    def Cr_e0(self):
        return self.__Cr_e0
    @Cr_e0.setter
    def Cr_e0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Profil__Cr_e0", None)
        self.__Cr_e0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "personne1"):
                    opp_val = getattr(item, "personne1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "personne1"):
                    opp_val = getattr(item, "personne1", None)
                    
                    if opp_val is None:
                        setattr(item, "personne1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def voiture16(self):
        return self.__voiture16
    @voiture16.setter
    def voiture16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Profil__voiture16", None)
        self.__voiture16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Profil17"):
                opp_val = getattr(old_value, "Profil17", None)
                if opp_val == self:
                    setattr(old_value, "Profil17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Profil17"):
                opp_val = getattr(value, "Profil17", None)
                setattr(value, "Profil17", self)

    @property
    def avis5(self):
        return self.__avis5
    @avis5.setter
    def avis5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Profil__avis5", None)
        self.__avis5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "personne4"):
                    opp_val = getattr(item, "personne4", None)
                    
                    if opp_val == self:
                        setattr(item, "personne4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "personne4"):
                    opp_val = getattr(item, "personne4", None)
                    
                    setattr(item, "personne4", self)
                    

    @property
    def adresse8(self):
        return self.__adresse8
    @adresse8.setter
    def adresse8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Profil__adresse8", None)
        self.__adresse8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personnes9"):
                opp_val = getattr(old_value, "personnes9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personnes9"):
                opp_val = getattr(value, "personnes9", None)
                if opp_val is None:
                    setattr(value, "personnes9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reservation13(self):
        return self.__reservation13
    @reservation13.setter
    def reservation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Profil__reservation13", None)
        self.__reservation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profil12"):
                opp_val = getattr(old_value, "profil12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profil12"):
                opp_val = getattr(value, "profil12", None)
                if opp_val is None:
                    setattr(value, "profil12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def events2(self):
        return self.__events2
    @events2.setter
    def events2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domain_Profil__events2", None)
        self.__events2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "participants3"):
                    opp_val = getattr(item, "participants3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "participants3"):
                    opp_val = getattr(item, "participants3", None)
                    
                    if opp_val is None:
                        setattr(item, "participants3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    


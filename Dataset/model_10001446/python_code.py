from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Covoiturage_Trajet:

    def __init__(self, id: int, date: date, depart: Covoiturage_Ville, destination: Covoiturage_Ville, prix: int, etat: bool, participants3: "Covoiturage_Conducteur" = None, avis7: set["Covoiturage_Avis"] = None, ville10: "Covoiturage_Ville" = None, reservation15: set["Covoiturage_Reservation"] = None, voiture20: "Covoiturage_Voiture" = None, passager23: set["Covoiturage_Passager"] = None):
        self.id = id
        self.date = date
        self.depart = depart
        self.destination = destination
        self.prix = prix
        self.etat = etat
        self.participants3 = participants3
        self.avis7 = avis7 if avis7 is not None else set()
        self.ville10 = ville10
        self.reservation15 = reservation15 if reservation15 is not None else set()
        self.voiture20 = voiture20
        self.passager23 = passager23 if passager23 is not None else set()
        
        pass
    @property
    def etat(self):
        return self.__etat
    @etat.setter
    def etat(self, etat: bool):
        self.__etat = etat

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
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def depart(self):
        return self.__depart
    @depart.setter
    def depart(self, depart: Covoiturage_Ville):
        self.__depart = depart

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: Covoiturage_Ville):
        self.__destination = destination

    @property
    def ville10(self):
        return self.__ville10
    @ville10.setter
    def ville10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Trajet__ville10", None)
        self.__ville10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet11"):
                opp_val = getattr(old_value, "trajet11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet11"):
                opp_val = getattr(value, "trajet11", None)
                if opp_val is None:
                    setattr(value, "trajet11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def passager23(self):
        return self.__passager23
    @passager23.setter
    def passager23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Trajet__passager23", None)
        self.__passager23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trajet22"):
                    opp_val = getattr(item, "trajet22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trajet22"):
                    opp_val = getattr(item, "trajet22", None)
                    
                    if opp_val is None:
                        setattr(item, "trajet22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def voiture20(self):
        return self.__voiture20
    @voiture20.setter
    def voiture20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Trajet__voiture20", None)
        self.__voiture20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet21"):
                opp_val = getattr(old_value, "trajet21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet21"):
                opp_val = getattr(value, "trajet21", None)
                if opp_val is None:
                    setattr(value, "trajet21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def participants3(self):
        return self.__participants3
    @participants3.setter
    def participants3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Trajet__participants3", None)
        self.__participants3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet2"):
                opp_val = getattr(old_value, "trajet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet2"):
                opp_val = getattr(value, "trajet2", None)
                if opp_val is None:
                    setattr(value, "trajet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avis7(self):
        return self.__avis7
    @avis7.setter
    def avis7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Trajet__avis7", None)
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
        old_value = getattr(self, f"_Covoiturage_Trajet__reservation15", None)
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
                    



class Covoiturage_Authentification:

    def __init__(self, id: str, password: str, personne1: set["Covoiturage_Passager"] = None):
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
        old_value = getattr(self, f"_Covoiturage_Authentification__personne1", None)
        self.__personne1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "s_authentifi_0"):
                    opp_val = getattr(item, "s_authentifi_0", None)
                    
                    if opp_val == self:
                        setattr(item, "s_authentifi_0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "s_authentifi_0"):
                    opp_val = getattr(item, "s_authentifi_0", None)
                    
                    setattr(item, "s_authentifi_0", self)
                    



class Covoiturage_Voiture:

    def __init__(self, id: int, model: str, marque: str, confort: str, nbPlaces: int, categorie: str, attribute: str, Profil17: "Covoiturage_Conducteur" = None, trajet21: set["Covoiturage_Trajet"] = None):
        self.id = id
        self.model = model
        self.marque = marque
        self.confort = confort
        self.nbPlaces = nbPlaces
        self.categorie = categorie
        self.attribute = attribute
        self.Profil17 = Profil17
        self.trajet21 = trajet21 if trajet21 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def categorie(self):
        return self.__categorie
    @categorie.setter
    def categorie(self, categorie: str):
        self.__categorie = categorie

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self, marque: str):
        self.__marque = marque

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
    def confort(self):
        return self.__confort
    @confort.setter
    def confort(self, confort: str):
        self.__confort = confort

    @property
    def Profil17(self):
        return self.__Profil17
    @Profil17.setter
    def Profil17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Voiture__Profil17", None)
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

    @property
    def trajet21(self):
        return self.__trajet21
    @trajet21.setter
    def trajet21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Voiture__trajet21", None)
        self.__trajet21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "voiture20"):
                    opp_val = getattr(item, "voiture20", None)
                    
                    if opp_val == self:
                        setattr(item, "voiture20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "voiture20"):
                    opp_val = getattr(item, "voiture20", None)
                    
                    setattr(item, "voiture20", self)
                    



class Covoiturage_Passager:

    def __init__(self, id: int, nom: str, prenom: str, tel: int, mail: str, s_authentifi_0: "Covoiturage_Authentification" = None, avis5: set["Covoiturage_Avis"] = None, adresse8: "Covoiturage_Ville" = None, reservation13: "Covoiturage_Reservation" = None, message19: set["Covoiturage_Message"] = None, trajet22: set["Covoiturage_Trajet"] = None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail
        self.s_authentifi_0 = s_authentifi_0
        self.avis5 = avis5 if avis5 is not None else set()
        self.adresse8 = adresse8
        self.reservation13 = reservation13
        self.message19 = message19 if message19 is not None else set()
        self.trajet22 = trajet22 if trajet22 is not None else set()
        
        pass
    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self, tel: int):
        self.__tel = tel

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

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
    def s_authentifi_0(self):
        return self.__s_authentifi_0
    @s_authentifi_0.setter
    def s_authentifi_0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Passager__s_authentifi_0", None)
        self.__s_authentifi_0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personne1"):
                opp_val = getattr(old_value, "personne1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personne1"):
                opp_val = getattr(value, "personne1", None)
                if opp_val is None:
                    setattr(value, "personne1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avis5(self):
        return self.__avis5
    @avis5.setter
    def avis5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Passager__avis5", None)
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
    def trajet22(self):
        return self.__trajet22
    @trajet22.setter
    def trajet22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Passager__trajet22", None)
        self.__trajet22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "passager23"):
                    opp_val = getattr(item, "passager23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "passager23"):
                    opp_val = getattr(item, "passager23", None)
                    
                    if opp_val is None:
                        setattr(item, "passager23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def message19(self):
        return self.__message19
    @message19.setter
    def message19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Passager__message19", None)
        self.__message19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "passager18"):
                    opp_val = getattr(item, "passager18", None)
                    
                    if opp_val == self:
                        setattr(item, "passager18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "passager18"):
                    opp_val = getattr(item, "passager18", None)
                    
                    setattr(item, "passager18", self)
                    

    @property
    def reservation13(self):
        return self.__reservation13
    @reservation13.setter
    def reservation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Passager__reservation13", None)
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
    def adresse8(self):
        return self.__adresse8
    @adresse8.setter
    def adresse8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Passager__adresse8", None)
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



class Covoiturage_Message:

    def __init__(self, Id: str, Value: str, passager18: "Covoiturage_Passager" = None):
        self.Id = Id
        self.Value = Value
        self.passager18 = passager18
        
        pass
    @property
    def Value(self):
        return self.__Value
    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def passager18(self):
        return self.__passager18
    @passager18.setter
    def passager18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Message__passager18", None)
        self.__passager18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message19"):
                opp_val = getattr(old_value, "message19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message19"):
                opp_val = getattr(value, "message19", None)
                if opp_val is None:
                    setattr(value, "message19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Covoiturage_Conducteur:

    def __init__(self, datePermi: str, trajet2: set["Covoiturage_Trajet"] = None, voiture16: "Covoiturage_Voiture" = None):
        self.datePermi = datePermi
        self.trajet2 = trajet2 if trajet2 is not None else set()
        self.voiture16 = voiture16
        
        pass
    @property
    def datePermi(self):
        return self.__datePermi
    @datePermi.setter
    def datePermi(self, datePermi: str):
        self.__datePermi = datePermi

    @property
    def voiture16(self):
        return self.__voiture16
    @voiture16.setter
    def voiture16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Conducteur__voiture16", None)
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
    def trajet2(self):
        return self.__trajet2
    @trajet2.setter
    def trajet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Conducteur__trajet2", None)
        self.__trajet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "participants3"):
                    opp_val = getattr(item, "participants3", None)
                    
                    if opp_val == self:
                        setattr(item, "participants3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "participants3"):
                    opp_val = getattr(item, "participants3", None)
                    
                    setattr(item, "participants3", self)
                    



class Covoiturage_Reservation:

    def __init__(self, id2: int, id: int, dateReservation: date, etat: bool, profil12: set["Covoiturage_Passager"] = None, trajet14: "Covoiturage_Trajet" = None):
        self.id2 = id2
        self.id = id
        self.dateReservation = dateReservation
        self.etat = etat
        self.profil12 = profil12 if profil12 is not None else set()
        self.trajet14 = trajet14
        
        pass
    @property
    def id2(self):
        return self.__id2
    @id2.setter
    def id2(self, id2: int):
        self.__id2 = id2

    @property
    def dateReservation(self):
        return self.__dateReservation
    @dateReservation.setter
    def dateReservation(self, dateReservation: date):
        self.__dateReservation = dateReservation

    @property
    def etat(self):
        return self.__etat
    @etat.setter
    def etat(self, etat: bool):
        self.__etat = etat

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def profil12(self):
        return self.__profil12
    @profil12.setter
    def profil12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Reservation__profil12", None)
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
                    

    @property
    def trajet14(self):
        return self.__trajet14
    @trajet14.setter
    def trajet14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Reservation__trajet14", None)
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



class Covoiturage_Avis:

    def __init__(self, id: int, commentaire: str, note: int, personne4: "Covoiturage_Passager" = None, evenement6: "Covoiturage_Trajet" = None):
        self.id = id
        self.commentaire = commentaire
        self.note = note
        self.personne4 = personne4
        self.evenement6 = evenement6
        
        pass
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
    def commentaire(self):
        return self.__commentaire
    @commentaire.setter
    def commentaire(self, commentaire: str):
        self.__commentaire = commentaire

    @property
    def evenement6(self):
        return self.__evenement6
    @evenement6.setter
    def evenement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Avis__evenement6", None)
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

    @property
    def personne4(self):
        return self.__personne4
    @personne4.setter
    def personne4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Avis__personne4", None)
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



class Covoiturage_Ville:

    def __init__(self, id: int, nom: str, cp: int, personnes9: set["Covoiturage_Passager"] = None, trajet11: set["Covoiturage_Trajet"] = None):
        self.id = id
        self.nom = nom
        self.cp = cp
        self.personnes9 = personnes9 if personnes9 is not None else set()
        self.trajet11 = trajet11 if trajet11 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def cp(self):
        return self.__cp
    @cp.setter
    def cp(self, cp: int):
        self.__cp = cp

    @property
    def personnes9(self):
        return self.__personnes9
    @personnes9.setter
    def personnes9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Covoiturage_Ville__personnes9", None)
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
        old_value = getattr(self, f"_Covoiturage_Ville__trajet11", None)
        self.__trajet11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ville10"):
                    opp_val = getattr(item, "ville10", None)
                    
                    if opp_val == self:
                        setattr(item, "ville10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ville10"):
                    opp_val = getattr(item, "ville10", None)
                    
                    setattr(item, "ville10", self)
                    


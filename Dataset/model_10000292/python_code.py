from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Personne2(Enum):
    pass

############################################
# Definition of Classes
############################################










class Chemin_Interface:

    pass


class Passager:

    pass


class Conducteur:

    pass


class Lieu:

    pass


class V_hicule:

    def __init__(self, imatriculation: str, modele: str, marque: str, propri_taire: Conducteur, conducteur4: "Conducteur" = None):
        self.imatriculation = imatriculation
        self.modele = modele
        self.marque = marque
        self.propri_taire = propri_taire
        self.conducteur4 = conducteur4
        
        pass
    @property
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self, marque: str):
        self.__marque = marque

    @property
    def propri_taire(self):
        return self.__propri_taire
    @propri_taire.setter
    def propri_taire(self, propri_taire: Conducteur):
        self.__propri_taire = propri_taire

    @property
    def imatriculation(self):
        return self.__imatriculation
    @imatriculation.setter
    def imatriculation(self, imatriculation: str):
        self.__imatriculation = imatriculation

    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: str):
        self.__modele = modele

    @property
    def conducteur4(self):
        return self.__conducteur4
    @conducteur4.setter
    def conducteur4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_V_hicule__conducteur4", None)
        self.__conducteur4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "v_hicule5"):
                opp_val = getattr(old_value, "v_hicule5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "v_hicule5"):
                opp_val = getattr(value, "v_hicule5", None)
                if opp_val is None:
                    setattr(value, "v_hicule5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Utilisateur1:

    def __init__(self, nom: str, age: int, adresse: str):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        
        pass
    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age



class Trajet1:

    def __init__(self, lieudebut: Lieu, lieuFin: Lieu, datedebut: str, dateFin: str, passager2: set["Passager"] = None, conducteur6: "Conducteur" = None):
        self.lieudebut = lieudebut
        self.lieuFin = lieuFin
        self.datedebut = datedebut
        self.dateFin = dateFin
        self.passager2 = passager2 if passager2 is not None else set()
        self.conducteur6 = conducteur6
        
        pass
    @property
    def dateFin(self):
        return self.__dateFin
    @dateFin.setter
    def dateFin(self, dateFin: str):
        self.__dateFin = dateFin

    @property
    def datedebut(self):
        return self.__datedebut
    @datedebut.setter
    def datedebut(self, datedebut: str):
        self.__datedebut = datedebut

    @property
    def lieudebut(self):
        return self.__lieudebut
    @lieudebut.setter
    def lieudebut(self, lieudebut: Lieu):
        self.__lieudebut = lieudebut

    @property
    def lieuFin(self):
        return self.__lieuFin
    @lieuFin.setter
    def lieuFin(self, lieuFin: Lieu):
        self.__lieuFin = lieuFin

    @property
    def passager2(self):
        return self.__passager2
    @passager2.setter
    def passager2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trajet1__passager2", None)
        self.__passager2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trajet3"):
                    opp_val = getattr(item, "trajet3", None)
                    
                    if opp_val == self:
                        setattr(item, "trajet3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trajet3"):
                    opp_val = getattr(item, "trajet3", None)
                    
                    setattr(item, "trajet3", self)
                    

    @property
    def conducteur6(self):
        return self.__conducteur6
    @conducteur6.setter
    def conducteur6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trajet1__conducteur6", None)
        self.__conducteur6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet7"):
                opp_val = getattr(old_value, "trajet7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet7"):
                opp_val = getattr(value, "trajet7", None)
                if opp_val is None:
                    setattr(value, "trajet7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Trajet:

    def __init__(self, date: str, prix: int, depart: Lieu, destination: Lieu, placesRestantes: int, description: str, Utilisateur9: "Utilisateur" = None):
        self.date = date
        self.prix = prix
        self.depart = depart
        self.destination = destination
        self.placesRestantes = placesRestantes
        self.description = description
        self.Utilisateur9 = Utilisateur9
        
        pass
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix: int):
        self.__prix = prix

    @property
    def placesRestantes(self):
        return self.__placesRestantes
    @placesRestantes.setter
    def placesRestantes(self, placesRestantes: int):
        self.__placesRestantes = placesRestantes

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: Lieu):
        self.__destination = destination

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def depart(self):
        return self.__depart
    @depart.setter
    def depart(self, depart: Lieu):
        self.__depart = depart

    @property
    def Utilisateur9(self):
        return self.__Utilisateur9
    @Utilisateur9.setter
    def Utilisateur9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trajet__Utilisateur9", None)
        self.__Utilisateur9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet8"):
                opp_val = getattr(old_value, "trajet8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet8"):
                opp_val = getattr(value, "trajet8", None)
                if opp_val is None:
                    setattr(value, "trajet8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Voiture:

    def __init__(self, places: int, Utilisateur11: "Utilisateur" = None):
        self.places = places
        self.Utilisateur11 = Utilisateur11
        
        pass
    @property
    def places(self):
        return self.__places
    @places.setter
    def places(self, places: int):
        self.__places = places

    @property
    def Utilisateur11(self):
        return self.__Utilisateur11
    @Utilisateur11.setter
    def Utilisateur11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Voiture__Utilisateur11", None)
        self.__Utilisateur11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voiture10"):
                opp_val = getattr(old_value, "voiture10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voiture10"):
                opp_val = getattr(value, "voiture10", None)
                if opp_val is None:
                    setattr(value, "voiture10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Avis1:

    def __init__(self, note: int, description: str, Utilisateur1: "Utilisateur" = None):
        self.note = note
        self.description = description
        self.Utilisateur1 = Utilisateur1
        
        pass
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note: int):
        self.__note = note

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Utilisateur1(self):
        return self.__Utilisateur1
    @Utilisateur1.setter
    def Utilisateur1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Avis1__Utilisateur1", None)
        self.__Utilisateur1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avis0"):
                opp_val = getattr(old_value, "avis0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avis0"):
                opp_val = getattr(value, "avis0", None)
                if opp_val is None:
                    setattr(value, "avis0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Utilisateur:

    def __init__(self, nom: str, score: str, nbAvis: int, photoDeProfil: str, avis0: set["Avis1"] = None, trajet8: set["Trajet"] = None, voiture10: set["Voiture"] = None):
        self.nom = nom
        self.score = score
        self.nbAvis = nbAvis
        self.photoDeProfil = photoDeProfil
        self.avis0 = avis0 if avis0 is not None else set()
        self.trajet8 = trajet8 if trajet8 is not None else set()
        self.voiture10 = voiture10 if voiture10 is not None else set()
        
        pass
    @property
    def photoDeProfil(self):
        return self.__photoDeProfil
    @photoDeProfil.setter
    def photoDeProfil(self, photoDeProfil: str):
        self.__photoDeProfil = photoDeProfil

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: str):
        self.__score = score

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def nbAvis(self):
        return self.__nbAvis
    @nbAvis.setter
    def nbAvis(self, nbAvis: int):
        self.__nbAvis = nbAvis

    @property
    def avis0(self):
        return self.__avis0
    @avis0.setter
    def avis0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__avis0", None)
        self.__avis0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Utilisateur1"):
                    opp_val = getattr(item, "Utilisateur1", None)
                    
                    if opp_val == self:
                        setattr(item, "Utilisateur1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Utilisateur1"):
                    opp_val = getattr(item, "Utilisateur1", None)
                    
                    setattr(item, "Utilisateur1", self)
                    

    @property
    def voiture10(self):
        return self.__voiture10
    @voiture10.setter
    def voiture10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__voiture10", None)
        self.__voiture10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Utilisateur11"):
                    opp_val = getattr(item, "Utilisateur11", None)
                    
                    if opp_val == self:
                        setattr(item, "Utilisateur11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Utilisateur11"):
                    opp_val = getattr(item, "Utilisateur11", None)
                    
                    setattr(item, "Utilisateur11", self)
                    

    @property
    def trajet8(self):
        return self.__trajet8
    @trajet8.setter
    def trajet8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__trajet8", None)
        self.__trajet8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Utilisateur9"):
                    opp_val = getattr(item, "Utilisateur9", None)
                    
                    if opp_val == self:
                        setattr(item, "Utilisateur9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Utilisateur9"):
                    opp_val = getattr(item, "Utilisateur9", None)
                    
                    setattr(item, "Utilisateur9", self)
                    



class Avis:

    pass


class Personne:

    pass


class Class:

    pass

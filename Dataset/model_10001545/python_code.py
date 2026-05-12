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







class Persistance_Actor:

    pass


class Contr_leur_Actor:

    pass


class Acteur_Actor:

    pass


class ihm_Actor:

    pass





class Persistance:

    pass


class Contr_leur:

    pass


class ihm:

    pass


class Role:

    def __init__(self, nbAvis: int, utilisateur17: "Utilisateur2" = None, avis18: set["Avis2"] = None):
        self.nbAvis = nbAvis
        self.utilisateur17 = utilisateur17
        self.avis18 = avis18 if avis18 is not None else set()
        
        pass
    @property
    def nbAvis(self):
        return self.__nbAvis
    @nbAvis.setter
    def nbAvis(self, nbAvis: int):
        self.__nbAvis = nbAvis

    @property
    def utilisateur17(self):
        return self.__utilisateur17
    @utilisateur17.setter
    def utilisateur17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Role__utilisateur17", None)
        self.__utilisateur17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role16"):
                opp_val = getattr(old_value, "role16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role16"):
                opp_val = getattr(value, "role16", None)
                if opp_val is None:
                    setattr(value, "role16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avis18(self):
        return self.__avis18
    @avis18.setter
    def avis18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Role__avis18", None)
        self.__avis18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "role19"):
                    opp_val = getattr(item, "role19", None)
                    
                    if opp_val == self:
                        setattr(item, "role19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "role19"):
                    opp_val = getattr(item, "role19", None)
                    
                    setattr(item, "role19", self)
                    



class Lieu1:

    pass


class Avis2:

    def __init__(self, note: int, description: str, role19: "Role" = None):
        self.note = note
        self.description = description
        self.role19 = role19
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note: int):
        self.__note = note

    @property
    def role19(self):
        return self.__role19
    @role19.setter
    def role19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Avis2__role19", None)
        self.__role19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avis18"):
                opp_val = getattr(old_value, "avis18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avis18"):
                opp_val = getattr(value, "avis18", None)
                if opp_val is None:
                    setattr(value, "avis18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Passager1:

    pass


class Conducteur1:

    pass


class V_hicule1:

    def __init__(self, imatriculation: str, modele: str, marque: str, propri_taire: Conducteur1, nbPlaces: int, conducteur13: "Conducteur1" = None):
        self.imatriculation = imatriculation
        self.modele = modele
        self.marque = marque
        self.propri_taire = propri_taire
        self.nbPlaces = nbPlaces
        self.conducteur13 = conducteur13
        
        pass
    @property
    def imatriculation(self):
        return self.__imatriculation
    @imatriculation.setter
    def imatriculation(self, imatriculation: str):
        self.__imatriculation = imatriculation

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
    def propri_taire(self):
        return self.__propri_taire
    @propri_taire.setter
    def propri_taire(self, propri_taire: Conducteur1):
        self.__propri_taire = propri_taire

    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: str):
        self.__modele = modele

    @property
    def conducteur13(self):
        return self.__conducteur13
    @conducteur13.setter
    def conducteur13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_V_hicule1__conducteur13", None)
        self.__conducteur13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "v_hicule12"):
                opp_val = getattr(old_value, "v_hicule12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "v_hicule12"):
                opp_val = getattr(value, "v_hicule12", None)
                if opp_val is None:
                    setattr(value, "v_hicule12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Utilisateur2:

    def __init__(self, nom: str, age: int, adresse: str, photoDeProfil: str, role16: set["Role"] = None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.photoDeProfil = photoDeProfil
        self.role16 = role16 if role16 is not None else set()
        
        pass
    @property
    def photoDeProfil(self):
        return self.__photoDeProfil
    @photoDeProfil.setter
    def photoDeProfil(self, photoDeProfil: str):
        self.__photoDeProfil = photoDeProfil

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

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def role16(self):
        return self.__role16
    @role16.setter
    def role16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur2__role16", None)
        self.__role16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "utilisateur17"):
                    opp_val = getattr(item, "utilisateur17", None)
                    
                    if opp_val == self:
                        setattr(item, "utilisateur17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "utilisateur17"):
                    opp_val = getattr(item, "utilisateur17", None)
                    
                    setattr(item, "utilisateur17", self)
                    



class Trajet2:

    def __init__(self, lieudebut: Lieu, lieuFin: Lieu, datedebut: str, dateFin: str, prix: int, placesRestantes: int, description: str, conducteur15: "Conducteur1" = None, lieu21: "Lieu1" = None, lieu23: "Lieu1" = None):
        self.lieudebut = lieudebut
        self.lieuFin = lieuFin
        self.datedebut = datedebut
        self.dateFin = dateFin
        self.prix = prix
        self.placesRestantes = placesRestantes
        self.description = description
        self.conducteur15 = conducteur15
        self.lieu21 = lieu21
        self.lieu23 = lieu23
        
        pass
    @property
    def placesRestantes(self):
        return self.__placesRestantes
    @placesRestantes.setter
    def placesRestantes(self, placesRestantes: int):
        self.__placesRestantes = placesRestantes

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix: int):
        self.__prix = prix

    @property
    def dateFin(self):
        return self.__dateFin
    @dateFin.setter
    def dateFin(self, dateFin: str):
        self.__dateFin = dateFin

    @property
    def lieuFin(self):
        return self.__lieuFin
    @lieuFin.setter
    def lieuFin(self, lieuFin: Lieu):
        self.__lieuFin = lieuFin

    @property
    def lieudebut(self):
        return self.__lieudebut
    @lieudebut.setter
    def lieudebut(self, lieudebut: Lieu):
        self.__lieudebut = lieudebut

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def datedebut(self):
        return self.__datedebut
    @datedebut.setter
    def datedebut(self, datedebut: str):
        self.__datedebut = datedebut

    @property
    def lieu21(self):
        return self.__lieu21
    @lieu21.setter
    def lieu21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trajet2__lieu21", None)
        self.__lieu21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arrivee20"):
                opp_val = getattr(old_value, "Arrivee20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arrivee20"):
                opp_val = getattr(value, "Arrivee20", None)
                if opp_val is None:
                    setattr(value, "Arrivee20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conducteur15(self):
        return self.__conducteur15
    @conducteur15.setter
    def conducteur15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trajet2__conducteur15", None)
        self.__conducteur15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet14"):
                opp_val = getattr(old_value, "trajet14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet14"):
                opp_val = getattr(value, "trajet14", None)
                if opp_val is None:
                    setattr(value, "trajet14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lieu23(self):
        return self.__lieu23
    @lieu23.setter
    def lieu23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trajet2__lieu23", None)
        self.__lieu23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Depart22"):
                opp_val = getattr(old_value, "Depart22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Depart22"):
                opp_val = getattr(value, "Depart22", None)
                if opp_val is None:
                    setattr(value, "Depart22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



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
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self, marque: str):
        self.__marque = marque

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

    def __init__(self, datedebut: str, dateFin: str, lieudebut: Lieu, lieuFin: Lieu, conducteur6: "Conducteur" = None, passager2: set["Passager"] = None):
        self.datedebut = datedebut
        self.dateFin = dateFin
        self.lieudebut = lieudebut
        self.lieuFin = lieuFin
        self.conducteur6 = conducteur6
        self.passager2 = passager2 if passager2 is not None else set()
        
        pass
    @property
    def lieudebut(self):
        return self.__lieudebut
    @lieudebut.setter
    def lieudebut(self, lieudebut: Lieu):
        self.__lieudebut = lieudebut

    @property
    def datedebut(self):
        return self.__datedebut
    @datedebut.setter
    def datedebut(self, datedebut: str):
        self.__datedebut = datedebut

    @property
    def dateFin(self):
        return self.__dateFin
    @dateFin.setter
    def dateFin(self, dateFin: str):
        self.__dateFin = dateFin

    @property
    def lieuFin(self):
        return self.__lieuFin
    @lieuFin.setter
    def lieuFin(self, lieuFin: Lieu):
        self.__lieuFin = lieuFin

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
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix: int):
        self.__prix = prix

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: Lieu):
        self.__destination = destination

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
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note: int):
        self.__note = note

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

    def __init__(self, nom: str, score: str, nbAvis: int, photoDeProfil: str, trajet8: set["Trajet"] = None, voiture10: set["Voiture"] = None, avis0: set["Avis1"] = None):
        self.nom = nom
        self.score = score
        self.nbAvis = nbAvis
        self.photoDeProfil = photoDeProfil
        self.trajet8 = trajet8 if trajet8 is not None else set()
        self.voiture10 = voiture10 if voiture10 is not None else set()
        self.avis0 = avis0 if avis0 is not None else set()
        
        pass
    @property
    def nbAvis(self):
        return self.__nbAvis
    @nbAvis.setter
    def nbAvis(self, nbAvis: int):
        self.__nbAvis = nbAvis

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: str):
        self.__score = score

    @property
    def photoDeProfil(self):
        return self.__photoDeProfil
    @photoDeProfil.setter
    def photoDeProfil(self, photoDeProfil: str):
        self.__photoDeProfil = photoDeProfil

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
                    



class Avis:

    pass


class Personne:

    pass


class Class:

    pass

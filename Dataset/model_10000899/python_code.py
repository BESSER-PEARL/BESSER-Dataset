from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Admin_add_trajet_UseCase:

    pass


class Admin_Passager___conducteur_Actor:

    pass


class Admin_s_inscrire_UseCase:

    pass


class Admin_UseCase5_UseCase:

    pass


class Admin_consulter_trajets_UseCase:

    pass


class Admin_suppr_utils_UseCase:

    pass


class Admin_modifier_utilis_UseCase:

    pass


class Admin_consulter_liste_utilis_UseCase:

    pass


class Admin_Admin_Actor:

    pass





class covoiturage_Avis:

    def __init__(self, id: int, commentaire: str, note: int, personne8: "covoiturage_Personne" = None, evenement10: "covoiturage_Reservations" = None):
        self.id = id
        self.commentaire = commentaire
        self.note = note
        self.personne8 = personne8
        self.evenement10 = evenement10
        
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
    def evenement10(self):
        return self.__evenement10
    @evenement10.setter
    def evenement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Avis__evenement10", None)
        self.__evenement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avis11"):
                opp_val = getattr(old_value, "avis11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avis11"):
                opp_val = getattr(value, "avis11", None)
                if opp_val is None:
                    setattr(value, "avis11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def personne8(self):
        return self.__personne8
    @personne8.setter
    def personne8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Avis__personne8", None)
        self.__personne8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avis9"):
                opp_val = getattr(old_value, "avis9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avis9"):
                opp_val = getattr(value, "avis9", None)
                if opp_val is None:
                    setattr(value, "avis9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class covoiturage_Ville:

    def __init__(self, id: int, nom: str, cp: str, evenement5: "covoiturage_Reservations" = None, personnes13: set["covoiturage_Personne"] = None):
        self.id = id
        self.nom = nom
        self.cp = cp
        self.evenement5 = evenement5
        self.personnes13 = personnes13 if personnes13 is not None else set()
        
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
    def cp(self, cp: str):
        self.__cp = cp

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def evenement5(self):
        return self.__evenement5
    @evenement5.setter
    def evenement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Ville__evenement5", None)
        self.__evenement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "villes4"):
                opp_val = getattr(old_value, "villes4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "villes4"):
                opp_val = getattr(value, "villes4", None)
                if opp_val is None:
                    setattr(value, "villes4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def personnes13(self):
        return self.__personnes13
    @personnes13.setter
    def personnes13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Ville__personnes13", None)
        self.__personnes13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adresse12"):
                    opp_val = getattr(item, "adresse12", None)
                    
                    if opp_val == self:
                        setattr(item, "adresse12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adresse12"):
                    opp_val = getattr(item, "adresse12", None)
                    
                    setattr(item, "adresse12", self)
                    



class covoiturage_Reservations:

    def __init__(self, id: int, date: date, lieuDeDepose: str, prix: int, villes4: set["covoiturage_Ville"] = None, participants7: set["covoiturage_Personne"] = None, avis11: set["covoiturage_Avis"] = None):
        self.id = id
        self.date = date
        self.lieuDeDepose = lieuDeDepose
        self.prix = prix
        self.villes4 = villes4 if villes4 is not None else set()
        self.participants7 = participants7 if participants7 is not None else set()
        self.avis11 = avis11 if avis11 is not None else set()
        
        pass
    @property
    def lieuDeDepose(self):
        return self.__lieuDeDepose
    @lieuDeDepose.setter
    def lieuDeDepose(self, lieuDeDepose: str):
        self.__lieuDeDepose = lieuDeDepose

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix: int):
        self.__prix = prix

    @property
    def villes4(self):
        return self.__villes4
    @villes4.setter
    def villes4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Reservations__villes4", None)
        self.__villes4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "evenement5"):
                    opp_val = getattr(item, "evenement5", None)
                    
                    if opp_val == self:
                        setattr(item, "evenement5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "evenement5"):
                    opp_val = getattr(item, "evenement5", None)
                    
                    setattr(item, "evenement5", self)
                    

    @property
    def participants7(self):
        return self.__participants7
    @participants7.setter
    def participants7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Reservations__participants7", None)
        self.__participants7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events6"):
                    opp_val = getattr(item, "events6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events6"):
                    opp_val = getattr(item, "events6", None)
                    
                    if opp_val is None:
                        setattr(item, "events6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def avis11(self):
        return self.__avis11
    @avis11.setter
    def avis11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Reservations__avis11", None)
        self.__avis11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "evenement10"):
                    opp_val = getattr(item, "evenement10", None)
                    
                    if opp_val == self:
                        setattr(item, "evenement10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "evenement10"):
                    opp_val = getattr(item, "evenement10", None)
                    
                    setattr(item, "evenement10", self)
                    



class covoiturage_Preferences:

    def __init__(self, id: int, nomPref: str, valeur: str, personne3: set["covoiturage_Personne"] = None):
        self.id = id
        self.nomPref = nomPref
        self.valeur = valeur
        self.personne3 = personne3 if personne3 is not None else set()
        
        pass
    @property
    def nomPref(self):
        return self.__nomPref
    @nomPref.setter
    def nomPref(self, nomPref: str):
        self.__nomPref = nomPref

    @property
    def valeur(self):
        return self.__valeur
    @valeur.setter
    def valeur(self, valeur: str):
        self.__valeur = valeur

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def personne3(self):
        return self.__personne3
    @personne3.setter
    def personne3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Preferences__personne3", None)
        self.__personne3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "preferences2"):
                    opp_val = getattr(item, "preferences2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "preferences2"):
                    opp_val = getattr(item, "preferences2", None)
                    
                    if opp_val is None:
                        setattr(item, "preferences2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class covoiturage_Voiture:

    def __init__(self, id: int, categorie: str, marque: str, model: str, confort: str, couleur: str, nbPlaces: int, climatiseur: bool, tabac: bool, personne1: "covoiturage_Personne" = None):
        self.id = id
        self.categorie = categorie
        self.marque = marque
        self.model = model
        self.confort = confort
        self.couleur = couleur
        self.nbPlaces = nbPlaces
        self.climatiseur = climatiseur
        self.tabac = tabac
        self.personne1 = personne1
        
        pass
    @property
    def tabac(self):
        return self.__tabac
    @tabac.setter
    def tabac(self, tabac: bool):
        self.__tabac = tabac

    @property
    def confort(self):
        return self.__confort
    @confort.setter
    def confort(self, confort: str):
        self.__confort = confort

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def categorie(self):
        return self.__categorie
    @categorie.setter
    def categorie(self, categorie: str):
        self.__categorie = categorie

    @property
    def couleur(self):
        return self.__couleur
    @couleur.setter
    def couleur(self, couleur: str):
        self.__couleur = couleur

    @property
    def nbPlaces(self):
        return self.__nbPlaces
    @nbPlaces.setter
    def nbPlaces(self, nbPlaces: int):
        self.__nbPlaces = nbPlaces

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self, marque: str):
        self.__marque = marque

    @property
    def climatiseur(self):
        return self.__climatiseur
    @climatiseur.setter
    def climatiseur(self, climatiseur: bool):
        self.__climatiseur = climatiseur

    @property
    def personne1(self):
        return self.__personne1
    @personne1.setter
    def personne1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Voiture__personne1", None)
        self.__personne1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voiture0"):
                opp_val = getattr(old_value, "voiture0", None)
                if opp_val == self:
                    setattr(old_value, "voiture0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voiture0"):
                opp_val = getattr(value, "voiture0", None)
                setattr(value, "voiture0", self)



class covoiturage_Personne:

    def __init__(self, id: int, nom: str, prenom: str, tel: str, mail: str, events6: set["covoiturage_Reservations"] = None, avis9: set["covoiturage_Avis"] = None, adresse12: "covoiturage_Ville" = None, voiture0: "covoiturage_Voiture" = None, preferences2: set["covoiturage_Preferences"] = None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail
        self.events6 = events6 if events6 is not None else set()
        self.avis9 = avis9 if avis9 is not None else set()
        self.adresse12 = adresse12
        self.voiture0 = voiture0
        self.preferences2 = preferences2 if preferences2 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self, tel: str):
        self.__tel = tel

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def preferences2(self):
        return self.__preferences2
    @preferences2.setter
    def preferences2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Personne__preferences2", None)
        self.__preferences2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "personne3"):
                    opp_val = getattr(item, "personne3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "personne3"):
                    opp_val = getattr(item, "personne3", None)
                    
                    if opp_val is None:
                        setattr(item, "personne3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def events6(self):
        return self.__events6
    @events6.setter
    def events6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Personne__events6", None)
        self.__events6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "participants7"):
                    opp_val = getattr(item, "participants7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "participants7"):
                    opp_val = getattr(item, "participants7", None)
                    
                    if opp_val is None:
                        setattr(item, "participants7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def avis9(self):
        return self.__avis9
    @avis9.setter
    def avis9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Personne__avis9", None)
        self.__avis9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "personne8"):
                    opp_val = getattr(item, "personne8", None)
                    
                    if opp_val == self:
                        setattr(item, "personne8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "personne8"):
                    opp_val = getattr(item, "personne8", None)
                    
                    setattr(item, "personne8", self)
                    

    @property
    def adresse12(self):
        return self.__adresse12
    @adresse12.setter
    def adresse12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Personne__adresse12", None)
        self.__adresse12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personnes13"):
                opp_val = getattr(old_value, "personnes13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personnes13"):
                opp_val = getattr(value, "personnes13", None)
                if opp_val is None:
                    setattr(value, "personnes13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def voiture0(self):
        return self.__voiture0
    @voiture0.setter
    def voiture0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_covoiturage_Personne__voiture0", None)
        self.__voiture0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personne1"):
                opp_val = getattr(old_value, "personne1", None)
                if opp_val == self:
                    setattr(old_value, "personne1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personne1"):
                opp_val = getattr(value, "personne1", None)
                setattr(value, "personne1", self)


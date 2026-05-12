from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CoursCode:

    pass


class CoursConduite:

    pass


class Groupe:

    def __init__(self, id: int, numeroGroupe: int, libelle: str, suivre8: set["CoursCode"] = None, candidat3: set["Candidat"] = None):
        self.id = id
        self.numeroGroupe = numeroGroupe
        self.libelle = libelle
        self.suivre8 = suivre8 if suivre8 is not None else set()
        self.candidat3 = candidat3 if candidat3 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def numeroGroupe(self):
        return self.__numeroGroupe
    @numeroGroupe.setter
    def numeroGroupe(self, numeroGroupe: int):
        self.__numeroGroupe = numeroGroupe

    @property
    def libelle(self):
        return self.__libelle
    @libelle.setter
    def libelle(self, libelle: str):
        self.__libelle = libelle

    @property
    def suivre8(self):
        return self.__suivre8
    @suivre8.setter
    def suivre8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Groupe__suivre8", None)
        self.__suivre8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "groupe9"):
                    opp_val = getattr(item, "groupe9", None)
                    
                    if opp_val == self:
                        setattr(item, "groupe9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "groupe9"):
                    opp_val = getattr(item, "groupe9", None)
                    
                    setattr(item, "groupe9", self)
                    

    @property
    def candidat3(self):
        return self.__candidat3
    @candidat3.setter
    def candidat3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Groupe__candidat3", None)
        self.__candidat3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "appartenir2"):
                    opp_val = getattr(item, "appartenir2", None)
                    
                    if opp_val == self:
                        setattr(item, "appartenir2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "appartenir2"):
                    opp_val = getattr(item, "appartenir2", None)
                    
                    setattr(item, "appartenir2", self)
                    



class Candidat:

    pass


class Professeur:

    def __init__(self, dateEmbauche: str, donner4: set["CoursCode"] = None, dispenser6: set["CoursConduite"] = None):
        self.dateEmbauche = dateEmbauche
        self.donner4 = donner4 if donner4 is not None else set()
        self.dispenser6 = dispenser6 if dispenser6 is not None else set()
        
        pass
    @property
    def dateEmbauche(self):
        return self.__dateEmbauche
    @dateEmbauche.setter
    def dateEmbauche(self, dateEmbauche: str):
        self.__dateEmbauche = dateEmbauche

    @property
    def dispenser6(self):
        return self.__dispenser6
    @dispenser6.setter
    def dispenser6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Professeur__dispenser6", None)
        self.__dispenser6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "professeur7"):
                    opp_val = getattr(item, "professeur7", None)
                    
                    if opp_val == self:
                        setattr(item, "professeur7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "professeur7"):
                    opp_val = getattr(item, "professeur7", None)
                    
                    setattr(item, "professeur7", self)
                    

    @property
    def donner4(self):
        return self.__donner4
    @donner4.setter
    def donner4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Professeur__donner4", None)
        self.__donner4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "professeur5"):
                    opp_val = getattr(item, "professeur5", None)
                    
                    if opp_val == self:
                        setattr(item, "professeur5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "professeur5"):
                    opp_val = getattr(item, "professeur5", None)
                    
                    setattr(item, "professeur5", self)
                    



class Examen:

    def __init__(self, id: int, dateExamen: str, heureD: str, heureF: str, typeExamen: str):
        self.id = id
        self.dateExamen = dateExamen
        self.heureD = heureD
        self.heureF = heureF
        self.typeExamen = typeExamen
        
        pass
    @property
    def heureF(self):
        return self.__heureF
    @heureF.setter
    def heureF(self, heureF: str):
        self.__heureF = heureF

    @property
    def dateExamen(self):
        return self.__dateExamen
    @dateExamen.setter
    def dateExamen(self, dateExamen: str):
        self.__dateExamen = dateExamen

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def heureD(self):
        return self.__heureD
    @heureD.setter
    def heureD(self, heureD: str):
        self.__heureD = heureD

    @property
    def typeExamen(self):
        return self.__typeExamen
    @typeExamen.setter
    def typeExamen(self, typeExamen: str):
        self.__typeExamen = typeExamen



class cours:

    def __init__(self, id: int, dateCours: str, heureD: str, heureF: str):
        self.id = id
        self.dateCours = dateCours
        self.heureD = heureD
        self.heureF = heureF
        
        pass
    @property
    def dateCours(self):
        return self.__dateCours
    @dateCours.setter
    def dateCours(self, dateCours: str):
        self.__dateCours = dateCours

    @property
    def heureF(self):
        return self.__heureF
    @heureF.setter
    def heureF(self, heureF: str):
        self.__heureF = heureF

    @property
    def heureD(self):
        return self.__heureD
    @heureD.setter
    def heureD(self, heureD: str):
        self.__heureD = heureD

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Voiture:

    def __init__(self, id: int, immatriculation: str, marque: str, modele: str, coursConduite1: set["CoursConduite"] = None):
        self.id = id
        self.immatriculation = immatriculation
        self.marque = marque
        self.modele = modele
        self.coursConduite1 = coursConduite1 if coursConduite1 is not None else set()
        
        pass
    @property
    def immatriculation(self):
        return self.__immatriculation
    @immatriculation.setter
    def immatriculation(self, immatriculation: str):
        self.__immatriculation = immatriculation

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
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele: str):
        self.__modele = modele

    @property
    def coursConduite1(self):
        return self.__coursConduite1
    @coursConduite1.setter
    def coursConduite1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Voiture__coursConduite1", None)
        self.__coursConduite1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "concerner0"):
                    opp_val = getattr(item, "concerner0", None)
                    
                    if opp_val == self:
                        setattr(item, "concerner0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "concerner0"):
                    opp_val = getattr(item, "concerner0", None)
                    
                    setattr(item, "concerner0", self)
                    



class Utilisateur:

    def __init__(self, login: str, mdp: str):
        self.login = login
        self.mdp = mdp
        
        pass
    @property
    def mdp(self):
        return self.__mdp
    @mdp.setter
    def mdp(self, mdp: str):
        self.__mdp = mdp

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login



class Personne:

    def __init__(self, id: int, nom: str, prenom: str, adresse: str, telephone: str, email: str, dateNaissance: str, lieuNaissance: str, numeroCIN: int):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.dateNaissance = dateNaissance
        self.lieuNaissance = lieuNaissance
        self.numeroCIN = numeroCIN
        
        pass
    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def dateNaissance(self):
        return self.__dateNaissance
    @dateNaissance.setter
    def dateNaissance(self, dateNaissance: str):
        self.__dateNaissance = dateNaissance

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
    def numeroCIN(self):
        return self.__numeroCIN
    @numeroCIN.setter
    def numeroCIN(self, numeroCIN: int):
        self.__numeroCIN = numeroCIN

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone: str):
        self.__telephone = telephone

    @property
    def lieuNaissance(self):
        return self.__lieuNaissance
    @lieuNaissance.setter
    def lieuNaissance(self, lieuNaissance: str):
        self.__lieuNaissance = lieuNaissance

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom


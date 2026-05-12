from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Test:

    def __init__(self, Prenom: str):
        self.Prenom = Prenom
        
        pass
    @property
    def Prenom(self):
        return self.__Prenom
    @Prenom.setter
    def Prenom(self, Prenom: str):
        self.__Prenom = Prenom



class Compte:

    def __init__(self, login: str, password: str, typeCompte: str, employe5: "Employe" = None, patient11: "Patient" = None):
        self.login = login
        self.password = password
        self.typeCompte = typeCompte
        self.employe5 = employe5
        self.patient11 = patient11
        
        pass
    @property
    def typeCompte(self):
        return self.__typeCompte
    @typeCompte.setter
    def typeCompte(self, typeCompte: str):
        self.__typeCompte = typeCompte

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def employe5(self):
        return self.__employe5
    @employe5.setter
    def employe5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Compte__employe5", None)
        self.__employe5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compte4"):
                opp_val = getattr(old_value, "compte4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compte4"):
                opp_val = getattr(value, "compte4", None)
                if opp_val is None:
                    setattr(value, "compte4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient11(self):
        return self.__patient11
    @patient11.setter
    def patient11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Compte__patient11", None)
        self.__patient11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compte10"):
                opp_val = getattr(old_value, "compte10", None)
                if opp_val == self:
                    setattr(old_value, "compte10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compte10"):
                opp_val = getattr(value, "compte10", None)
                setattr(value, "compte10", self)



class Patient:

    def __init__(self, antecedent: str, traitement: str, allergies: str, rDV13: set["RDV"] = None, medecin15: "Medecin" = None, compte10: "Compte" = None):
        self.antecedent = antecedent
        self.traitement = traitement
        self.allergies = allergies
        self.rDV13 = rDV13 if rDV13 is not None else set()
        self.medecin15 = medecin15
        self.compte10 = compte10
        
        pass
    @property
    def allergies(self):
        return self.__allergies
    @allergies.setter
    def allergies(self, allergies: str):
        self.__allergies = allergies

    @property
    def antecedent(self):
        return self.__antecedent
    @antecedent.setter
    def antecedent(self, antecedent: str):
        self.__antecedent = antecedent

    @property
    def traitement(self):
        return self.__traitement
    @traitement.setter
    def traitement(self, traitement: str):
        self.__traitement = traitement

    @property
    def medecin15(self):
        return self.__medecin15
    @medecin15.setter
    def medecin15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__medecin15", None)
        self.__medecin15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient14"):
                opp_val = getattr(old_value, "patient14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient14"):
                opp_val = getattr(value, "patient14", None)
                if opp_val is None:
                    setattr(value, "patient14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rDV13(self):
        return self.__rDV13
    @rDV13.setter
    def rDV13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__rDV13", None)
        self.__rDV13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient12"):
                    opp_val = getattr(item, "patient12", None)
                    
                    if opp_val == self:
                        setattr(item, "patient12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient12"):
                    opp_val = getattr(item, "patient12", None)
                    
                    setattr(item, "patient12", self)
                    

    @property
    def compte10(self):
        return self.__compte10
    @compte10.setter
    def compte10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__compte10", None)
        self.__compte10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient11"):
                opp_val = getattr(old_value, "patient11", None)
                if opp_val == self:
                    setattr(old_value, "patient11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient11"):
                opp_val = getattr(value, "patient11", None)
                setattr(value, "patient11", self)



class Agenda:

    def __init__(self, annee: str, rDV0: set["RDV"] = None, agendaPartage3: "AgendaPartage" = None, medecin7: "Medecin" = None):
        self.annee = annee
        self.rDV0 = rDV0 if rDV0 is not None else set()
        self.agendaPartage3 = agendaPartage3
        self.medecin7 = medecin7
        
        pass
    @property
    def annee(self):
        return self.__annee
    @annee.setter
    def annee(self, annee: str):
        self.__annee = annee

    @property
    def medecin7(self):
        return self.__medecin7
    @medecin7.setter
    def medecin7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agenda__medecin7", None)
        self.__medecin7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agenda6"):
                opp_val = getattr(old_value, "agenda6", None)
                if opp_val == self:
                    setattr(old_value, "agenda6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agenda6"):
                opp_val = getattr(value, "agenda6", None)
                setattr(value, "agenda6", self)

    @property
    def rDV0(self):
        return self.__rDV0
    @rDV0.setter
    def rDV0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agenda__rDV0", None)
        self.__rDV0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "agenda1"):
                    opp_val = getattr(item, "agenda1", None)
                    
                    if opp_val == self:
                        setattr(item, "agenda1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "agenda1"):
                    opp_val = getattr(item, "agenda1", None)
                    
                    setattr(item, "agenda1", self)
                    

    @property
    def agendaPartage3(self):
        return self.__agendaPartage3
    @agendaPartage3.setter
    def agendaPartage3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agenda__agendaPartage3", None)
        self.__agendaPartage3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agenda2"):
                opp_val = getattr(old_value, "agenda2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agenda2"):
                opp_val = getattr(value, "agenda2", None)
                if opp_val is None:
                    setattr(value, "agenda2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class AgendaPartage:

    pass


class RDV:

    def __init__(self, date: str, heure: str, duree: int, employeAdministratif17: set["EmployeAdministratif"] = None, agenda1: "Agenda" = None, patient12: "Patient" = None):
        self.date = date
        self.heure = heure
        self.duree = duree
        self.employeAdministratif17 = employeAdministratif17 if employeAdministratif17 is not None else set()
        self.agenda1 = agenda1
        self.patient12 = patient12
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def heure(self):
        return self.__heure
    @heure.setter
    def heure(self, heure: str):
        self.__heure = heure

    @property
    def duree(self):
        return self.__duree
    @duree.setter
    def duree(self, duree: int):
        self.__duree = duree

    @property
    def patient12(self):
        return self.__patient12
    @patient12.setter
    def patient12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDV__patient12", None)
        self.__patient12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rDV13"):
                opp_val = getattr(old_value, "rDV13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rDV13"):
                opp_val = getattr(value, "rDV13", None)
                if opp_val is None:
                    setattr(value, "rDV13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def agenda1(self):
        return self.__agenda1
    @agenda1.setter
    def agenda1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDV__agenda1", None)
        self.__agenda1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rDV0"):
                opp_val = getattr(old_value, "rDV0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rDV0"):
                opp_val = getattr(value, "rDV0", None)
                if opp_val is None:
                    setattr(value, "rDV0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employeAdministratif17(self):
        return self.__employeAdministratif17
    @employeAdministratif17.setter
    def employeAdministratif17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDV__employeAdministratif17", None)
        self.__employeAdministratif17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rDV16"):
                    opp_val = getattr(item, "rDV16", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rDV16"):
                    opp_val = getattr(item, "rDV16", None)
                    
                    if opp_val is None:
                        setattr(item, "rDV16", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Medecin:

    def __init__(self, specialisation: str, patient14: set["Patient"] = None, agenda6: "Agenda" = None):
        self.specialisation = specialisation
        self.patient14 = patient14 if patient14 is not None else set()
        self.agenda6 = agenda6
        
        pass
    @property
    def specialisation(self):
        return self.__specialisation
    @specialisation.setter
    def specialisation(self, specialisation: str):
        self.__specialisation = specialisation

    @property
    def patient14(self):
        return self.__patient14
    @patient14.setter
    def patient14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medecin__patient14", None)
        self.__patient14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "medecin15"):
                    opp_val = getattr(item, "medecin15", None)
                    
                    if opp_val == self:
                        setattr(item, "medecin15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "medecin15"):
                    opp_val = getattr(item, "medecin15", None)
                    
                    setattr(item, "medecin15", self)
                    

    @property
    def agenda6(self):
        return self.__agenda6
    @agenda6.setter
    def agenda6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medecin__agenda6", None)
        self.__agenda6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medecin7"):
                opp_val = getattr(old_value, "medecin7", None)
                if opp_val == self:
                    setattr(old_value, "medecin7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medecin7"):
                opp_val = getattr(value, "medecin7", None)
                setattr(value, "medecin7", self)



class EmployeAdministratif:

    def __init__(self, formation: str, rDV16: set["RDV"] = None, agendaPartage8: "AgendaPartage" = None):
        self.formation = formation
        self.rDV16 = rDV16 if rDV16 is not None else set()
        self.agendaPartage8 = agendaPartage8
        
        pass
    @property
    def formation(self):
        return self.__formation
    @formation.setter
    def formation(self, formation: str):
        self.__formation = formation

    @property
    def rDV16(self):
        return self.__rDV16
    @rDV16.setter
    def rDV16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmployeAdministratif__rDV16", None)
        self.__rDV16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employeAdministratif17"):
                    opp_val = getattr(item, "employeAdministratif17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employeAdministratif17"):
                    opp_val = getattr(item, "employeAdministratif17", None)
                    
                    if opp_val is None:
                        setattr(item, "employeAdministratif17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def agendaPartage8(self):
        return self.__agendaPartage8
    @agendaPartage8.setter
    def agendaPartage8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmployeAdministratif__agendaPartage8", None)
        self.__agendaPartage8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employeAdministratif9"):
                opp_val = getattr(old_value, "employeAdministratif9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employeAdministratif9"):
                opp_val = getattr(value, "employeAdministratif9", None)
                if opp_val is None:
                    setattr(value, "employeAdministratif9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Employe(ABC):

    def __init__(self, salaire: int, dateDebut: str, dateFin: str, joursVacance: int, compte4: set["Compte"] = None):
        self.salaire = salaire
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.joursVacance = joursVacance
        self.compte4 = compte4 if compte4 is not None else set()
        
        pass
    @property
    def salaire(self):
        return self.__salaire
    @salaire.setter
    def salaire(self, salaire: int):
        self.__salaire = salaire

    @property
    def joursVacance(self):
        return self.__joursVacance
    @joursVacance.setter
    def joursVacance(self, joursVacance: int):
        self.__joursVacance = joursVacance

    @property
    def dateDebut(self):
        return self.__dateDebut
    @dateDebut.setter
    def dateDebut(self, dateDebut: str):
        self.__dateDebut = dateDebut

    @property
    def dateFin(self):
        return self.__dateFin
    @dateFin.setter
    def dateFin(self, dateFin: str):
        self.__dateFin = dateFin

    @property
    def compte4(self):
        return self.__compte4
    @compte4.setter
    def compte4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employe__compte4", None)
        self.__compte4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employe5"):
                    opp_val = getattr(item, "employe5", None)
                    
                    if opp_val == self:
                        setattr(item, "employe5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employe5"):
                    opp_val = getattr(item, "employe5", None)
                    
                    setattr(item, "employe5", self)
                    



class Personne(ABC):

    def __init__(self, nom: str, prenom: str, adresse: str, email: str, telPrive: str, dateNaissance: str):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.telPrive = telPrive
        self.dateNaissance = dateNaissance
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

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
    def dateNaissance(self):
        return self.__dateNaissance
    @dateNaissance.setter
    def dateNaissance(self, dateNaissance: str):
        self.__dateNaissance = dateNaissance

    @property
    def telPrive(self):
        return self.__telPrive
    @telPrive.setter
    def telPrive(self, telPrive: str):
        self.__telPrive = telPrive

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse


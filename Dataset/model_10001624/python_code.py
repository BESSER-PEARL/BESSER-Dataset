from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Effectue_un_paiement_UseCase:

    pass


class Valide_arriv__UseCase:

    pass


class Valide_embarquement_UseCase:

    pass


class confirme_voyage_UseCase:

    pass


class Reserve_voyage_UseCase:

    pass


class Administre_UseCase:

    pass


class Choisi_un_voyage_UseCase:

    pass


class S_authentifier_UseCase:

    pass


class Enregistre_son_vehicule_UseCase:

    pass


class Conducteur_Actor:

    pass


class Passager__Actor:

    pass


class S_enregistre_UseCase:

    pass


class Administrateur_Actor:

    pass


class Proposition_de_voyage_UseCase:

    pass


class Utilisateur_anonyme_Actor:

    pass





class Date_trajet:

    def __init__(self, id_date: int, Jour: str, Type_date: str, Date___heure__minute: str):
        self.id_date = id_date
        self.Jour = Jour
        self.Type_date = Type_date
        self.Date___heure__minute = Date___heure__minute
        
        pass
    @property
    def Date___heure__minute(self):
        return self.__Date___heure__minute
    @Date___heure__minute.setter
    def Date___heure__minute(self, Date___heure__minute: str):
        self.__Date___heure__minute = Date___heure__minute

    @property
    def Jour(self):
        return self.__Jour
    @Jour.setter
    def Jour(self, Jour: str):
        self.__Jour = Jour

    @property
    def id_date(self):
        return self.__id_date
    @id_date.setter
    def id_date(self, id_date: int):
        self.__id_date = id_date

    @property
    def Type_date(self):
        return self.__Type_date
    @Type_date.setter
    def Type_date(self, Type_date: str):
        self.__Type_date = Type_date



class Utilisateur:

    def __init__(self, id_utilisateur: int, Nom: str, Pr_nom: str, Login: str, Password: str, Mail: str, Telephone: str):
        self.id_utilisateur = id_utilisateur
        self.Nom = Nom
        self.Pr_nom = Pr_nom
        self.Login = Login
        self.Password = Password
        self.Mail = Mail
        self.Telephone = Telephone
        
        pass
    @property
    def Login(self):
        return self.__Login
    @Login.setter
    def Login(self, Login: str):
        self.__Login = Login

    @property
    def Mail(self):
        return self.__Mail
    @Mail.setter
    def Mail(self, Mail: str):
        self.__Mail = Mail

    @property
    def Nom(self):
        return self.__Nom
    @Nom.setter
    def Nom(self, Nom: str):
        self.__Nom = Nom

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Telephone(self):
        return self.__Telephone
    @Telephone.setter
    def Telephone(self, Telephone: str):
        self.__Telephone = Telephone

    @property
    def id_utilisateur(self):
        return self.__id_utilisateur
    @id_utilisateur.setter
    def id_utilisateur(self, id_utilisateur: int):
        self.__id_utilisateur = id_utilisateur

    @property
    def Pr_nom(self):
        return self.__Pr_nom
    @Pr_nom.setter
    def Pr_nom(self, Pr_nom: str):
        self.__Pr_nom = Pr_nom


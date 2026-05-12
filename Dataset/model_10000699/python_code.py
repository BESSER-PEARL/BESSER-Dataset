from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ClassF:

    pass


class ClassE:

    pass


class ClassD:

    pass


class Commentaires:

    def __init__(self, idComm: float, privateAttribute: int, protectedAttribute: str, packageAttribute: str):
        self.idComm = idComm
        self.privateAttribute = privateAttribute
        self.protectedAttribute = protectedAttribute
        self.packageAttribute = packageAttribute
        
        pass
    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute

    @property
    def privateAttribute(self):
        return self.__privateAttribute
    @privateAttribute.setter
    def privateAttribute(self, privateAttribute: int):
        self.__privateAttribute = privateAttribute

    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute

    @property
    def idComm(self):
        return self.__idComm
    @idComm.setter
    def idComm(self, idComm: float):
        self.__idComm = idComm



class Cours:

    pass


class Membres:

    def __init__(self, idM: str, nom: str, prenom: str, email: str, telephone: int, mdp: str):
        self.idM = idM
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.mdp = mdp
        
        pass
    @property
    def idM(self):
        return self.__idM
    @idM.setter
    def idM(self, idM: str):
        self.__idM = idM

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def mdp(self):
        return self.__mdp
    @mdp.setter
    def mdp(self, mdp: str):
        self.__mdp = mdp

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone: int):
        self.__telephone = telephone



class Quizz:

    def __init__(self, ownerName: str, balance: float):
        self.ownerName = ownerName
        self.balance = balance
        
        pass
    @property
    def ownerName(self):
        return self.__ownerName
    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance



class MyClass:

    pass


class ClassL:

    pass


class ClassK:

    pass


class ClassH:

    pass


class ClassJ:

    pass


class ClassG:

    pass

from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Worker(ABC):

    def __init__(self, Cook: str, Waitor: str, Cashier: str):
        self.Cook = Cook
        self.Waitor = Waitor
        self.Cashier = Cashier
        
        pass
    @property
    def Cook(self):
        return self.__Cook
    @Cook.setter
    def Cook(self, Cook: str):
        self.__Cook = Cook

    @property
    def Cashier(self):
        return self.__Cashier
    @Cashier.setter
    def Cashier(self, Cashier: str):
        self.__Cashier = Cashier

    @property
    def Waitor(self):
        return self.__Waitor
    @Waitor.setter
    def Waitor(self, Waitor: str):
        self.__Waitor = Waitor



class Cashier:

    pass


class Waiter:

    pass


class Cook:

    pass


class Customer:

    pass


class People(ABC):

    def __init__(self, name: str, Custumer_: str, Worker: str):
        self.name = name
        self.Custumer_ = Custumer_
        self.Worker = Worker
        
        pass
    @property
    def Worker(self):
        return self.__Worker
    @Worker.setter
    def Worker(self, Worker: str):
        self.__Worker = Worker

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Custumer_(self):
        return self.__Custumer_
    @Custumer_.setter
    def Custumer_(self, Custumer_: str):
        self.__Custumer_ = Custumer_


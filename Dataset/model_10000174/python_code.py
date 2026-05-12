from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################







class Actor_Actor:

    pass





class Cashier:

    pass


class Waiter:

    pass


class Cook:

    pass


class Customer:

    pass


class People(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Worker(ABC):

    pass

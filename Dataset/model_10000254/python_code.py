from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Cashier:

    pass


class Waiter:

    pass


class Cook:

    pass


class Customer:

    pass


class Event(ABC):

    def __init__(self, created_at: float, entity: str):
        self.created_at = created_at
        self.entity = entity
        
        pass
    @property
    def entity(self):
        return self.__entity
    @entity.setter
    def entity(self, entity: str):
        self.__entity = entity

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: float):
        self.__created_at = created_at



class Worker(ABC):

    pass

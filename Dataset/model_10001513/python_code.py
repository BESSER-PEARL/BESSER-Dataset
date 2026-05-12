from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Interface_Interface:

    pass


class Class4:

    pass


class Class3:

    pass


class Class2:

    pass


class Class:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



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

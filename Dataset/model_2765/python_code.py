from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class tests_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Named:

    pass
class tests_Root(Named):

    pass
class tests_TypeB(Named):

    pass
class tests_TypeA(Named):

    pass
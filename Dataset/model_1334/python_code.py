from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class classescs_RootCS:

    pass
class classescs_PathNameCS:

    pass
class NamedElementCS:

    pass
class classescs_ClassCS(NamedElementCS):

    pass
class classescs_PathElementCS(NamedElementCS):

    pass
class classescs_PackageCS(NamedElementCS):

    pass
class classescs_NamedElementCS(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

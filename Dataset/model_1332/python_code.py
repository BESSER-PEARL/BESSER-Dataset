from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElementCS:

    pass
class classescs_PathElementCS(NamedElementCS):

    pass
class classescs_ClassCS(NamedElementCS):

    pass
class classescs_PackageCS(NamedElementCS):

    pass
class ElementCS:

    pass
class classescs_RootCS(ElementCS):

    pass
class classescs_PathNameCS(ElementCS):

    pass
class classescs_NamedElementCS(ElementCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class classescs_Element:

    pass
class classescs_ElementCS(ABC):

    pass
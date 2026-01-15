from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Namespace:

    pass
class NamedElement:

    pass
class classes_Class(NamedElement):

    pass
class classes_Package(Namespace, NamedElement):

    pass
class Element:

    pass
class classes_Root(Element):

    pass
class classes_Namespace(Element):

    pass
class classes_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class classes_Element(ABC):

    pass
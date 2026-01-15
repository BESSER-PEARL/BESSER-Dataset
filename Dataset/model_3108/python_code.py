from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class uml_UMLSpecification(NamedElement):

    pass
class uml_Class(NamedElement):

    pass
class uml_Attribute(NamedElement):

    pass
class uml_Association(NamedElement):

    pass
from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class entity_Namespace(NamedElement):

    pass
class entity_Type(NamedElement):

    pass
class entity_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class entity_Attribute(NamedElement):

    pass
class entity_Reference(NamedElement):

    pass
class Type:

    pass
class entity_Datatype(Type):

    pass
class entity_Entity(Type):

    pass
from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractComponent:

    pass
class Type:

    pass
class Interface:

    pass
class adl_Type(Interface):

    def __init__(self, signature: str):
        self.signature = signature
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

class adl_NamedElement(ABC):

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
class adl_Binding(NamedElement):

    pass
class adl_Component(NamedElement, AbstractComponent):

    pass
class adl_Interface(NamedElement):

    pass
class adl_Provided(Type):

    pass
class adl_Required(Type):

    pass
class adl_AbstractComponent(ABC):

    pass
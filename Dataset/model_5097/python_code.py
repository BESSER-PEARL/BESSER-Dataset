from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Interface:

    pass
class adl_Type(Interface):

    def __init__(self, signature: str):
        self.signature = signature
        
        pass
    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


class adl_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class adl_Interface(NamedElement):

    pass
class AbstractComponent:

    pass
class adl_Component(AbstractComponent, NamedElement):

    pass
class adl_AbstractComponent(ABC):

    pass
class Type:

    pass
class adl_Required(Type):

    pass
class adl_Provided(Type):

    pass
class adl_Binding(NamedElement):

    pass
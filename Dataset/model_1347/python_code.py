from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class classes_Visitable(ABC):

    pass
class CallExp:

    pass
class classes_OperationCallExp(CallExp):

    pass
class classes_PropertyCallExp(CallExp):

    pass
class Namespace:

    pass
class NamedElement:

    pass
class classes_Class(NamedElement):

    pass
class classes_Parameter(NamedElement):

    pass
class classes_Argument(NamedElement):

    pass
class classes_Package(Namespace, NamedElement):

    pass
class TypedElement:

    pass
class classes_Property(TypedElement, NamedElement):

    pass
class classes_Operation(TypedElement, NamedElement):

    pass
class classes_CallExp(TypedElement):

    pass
class Element:

    pass
class classes_TypedElement(Element):

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

class Visitable:

    pass
class classes_Element(Visitable):

    pass
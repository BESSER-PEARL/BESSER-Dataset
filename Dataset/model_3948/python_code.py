from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PathExp_Bool_attrElement(ABC):

    def __init__(self, bool_attr: bool):
        self.bool_attr = bool_attr
        
    @property
    def bool_attr(self) -> bool:
        return self.__bool_attr

    @bool_attr.setter
    def bool_attr(self, bool_attr: bool):
        self.__bool_attr = bool_attr

class Bool_attrElement:

    pass
class PathExp:

    pass
class PathExp_State(ABC):

    pass
class Transition:

    pass
class State:

    pass
class PathExp_Initial(State, Bool_attrElement):

    pass
class PathExp_Internal(State):

    def __init__(self, attr: int, #13: "PathExp_Transition", #16: "PathExp_Transition", #: "PathExp_PathExp"):
        self.attr = attr
        
    @property
    def attr(self) -> int:
        return self.__attr

    @attr.setter
    def attr(self, attr: int):
        self.__attr = attr

class PathExp_Final(Bool_attrElement, State):

    pass
class Element:

    pass
class PathExp_Transition(Element):

    pass
class PathExp_PathExp(Element):

    pass
class PathExp_Element(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

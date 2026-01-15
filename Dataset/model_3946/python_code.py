from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PathExp:

    pass
class PathExp_State(ABC):

    pass
class Transition:

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

class State:

    pass
class PathExp_Final(State):

    pass
class PathExp_Internal(State):

    def __init__(self, attr: int, #: "PathExp_PathExp", #13: "PathExp_Transition", #16: "PathExp_Transition"):
        self.attr = attr
        
    @property
    def attr(self) -> int:
        return self.__attr

    @attr.setter
    def attr(self, attr: int):
        self.__attr = attr

class PathExp_Initial(State):

    pass
class Element:

    pass
class PathExp_Transition(Element):

    pass
class PathExp_PathExp(Element):

    pass
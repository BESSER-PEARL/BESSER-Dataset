from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class PathExp_Internal(State):

    def __init__(self, attr: int, State10: "PathExp_Transition" = None, State8: "PathExp_Transition" = None, State: "PathExp_PathExp" = None):
        self.attr = attr
        
        pass
    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, attr: int):
        self.__attr = attr


class PathExp_Final(State):

    pass
class PathExp_Initial(State):

    pass
class PathExp:

    pass
class PathExp_State(ABC):

    pass
class Transition:

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
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


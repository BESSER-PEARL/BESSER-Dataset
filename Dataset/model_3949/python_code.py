from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Bool_attrElement:

    pass
class PathExp_Bool_attrElement(ABC):

    def __init__(self, bool_attr: bool):
        self.bool_attr = bool_attr
        
        pass
    @property
    def bool_attr(self):
        return self.__bool_attr

    @bool_attr.setter
    def bool_attr(self, bool_attr: bool):
        self.__bool_attr = bool_attr


class PathExp:

    pass
class PathExp_State(ABC):

    pass
class Transition:

    pass
class State:

    pass
class PathExp_Final(Bool_attrElement, State):

    pass
class PathExp_Internal(State):

    def __init__(self, attr: int, State: "PathExp_PathExp" = None, State10: "PathExp_Transition" = None, State8: "PathExp_Transition" = None):
        self.attr = attr
        
        pass
    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, attr: int):
        self.__attr = attr


class PathExp_Initial(Bool_attrElement, State):

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


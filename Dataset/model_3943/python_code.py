from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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


class PathExp_State:

    pass
class Transition:

    pass
class State:

    pass
class Element:

    pass
class PathExp_Transition(Element):

    pass
class PathExp_PathExp(Element):

    pass
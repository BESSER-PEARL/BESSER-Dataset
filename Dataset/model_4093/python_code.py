from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class automaton_NamedElement(ABC):

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
class automaton_Input(NamedElement):

    pass
class automaton_Automaton(NamedElement):

    pass
class automaton_Output(NamedElement):

    pass
class automaton_Transition(NamedElement):

    pass
class automaton_State(NamedElement):

    pass
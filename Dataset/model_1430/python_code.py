from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"


############################################
# Definition of Classes
############################################

class Constraint:

    pass
class State:

    pass
class statemachines_almostuml_Pseudostate(State):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class statemachines_almostuml_FinalState(State):

    pass
class statemachines_almostuml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class statemachines_almostuml_Constraint(ABC):

    pass
class Behavior:

    pass
class almostuml_Vertex:

    pass
class almostuml_NamedElement:

    pass
class statemachines_almostuml_State(almostuml_NamedElement, almostuml_Vertex):

    pass
class Trigger:

    pass
class StateMachine:

    pass
class statemachines_CustomSystem:

    pass
class Transition:

    pass
class Vertex:

    pass
class Region:

    pass
class NamedElement:

    pass
class statemachines_almostuml_Event(NamedElement):

    pass
class statemachines_almostuml_Behavior(NamedElement):

    pass
class statemachines_almostuml_Trigger(NamedElement):

    pass
class statemachines_almostuml_Region(NamedElement):

    pass
class statemachines_almostuml_Transition(NamedElement):

    pass
class statemachines_almostuml_Vertex(NamedElement):

    pass
class statemachines_almostuml_StateMachine(NamedElement):

    pass
class Event:

    pass
class statemachines_CustomEvent(Event):

    pass
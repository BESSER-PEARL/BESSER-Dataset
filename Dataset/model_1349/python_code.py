from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class statemachine_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class AbstractState:

    pass
class statemachine_State(AbstractState):

    pass
class statemachine_Initial(AbstractState):

    pass
class Named:

    pass
class statemachine_Transition(Named):

    pass
class statemachine_AbstractState(Named):

    pass
class statemachine_StateMachine:

    pass
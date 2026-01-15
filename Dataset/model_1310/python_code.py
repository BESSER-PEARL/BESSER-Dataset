from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class stateMachine_OutputState:

    pass
class stateMachine_InputState:

    pass
class ex_stateMachine_StandardState(stateMachine_OutputState, stateMachine_InputState):

    pass
class ex_stateMachine_State(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class InputState:

    pass
class ex_stateMachine_TerminalState(InputState):

    pass
class OutputState:

    pass
class ex_stateMachine_InitState(OutputState):

    pass
class ex_stateMachine_Transition:

    pass
class Transition:

    pass
class InitState:

    pass
class ex_stateMachine_StateMachine:

    pass
class State:

    pass
class ex_stateMachine_InputState(State):

    pass
class ex_stateMachine_OutputState(State):

    pass
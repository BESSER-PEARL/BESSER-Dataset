from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsmProv_Trigger:

    def __init__(self, expression: str):
        self.expression = expression
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    def evalTrigger(self, fsmProv_events) :
        # TODO: Implement evalTrigger method
        pass

class fsmProv_Transition:

    pass
class fsmProv_State:

    pass
class fsmProv_AbstractState(ABC):

    pass
class fsmProv_Region:

    pass
class fsmProv_StateMachine:

    pass
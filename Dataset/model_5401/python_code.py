from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    out = "out"
    return = "return"
    in = "in"
    inout = "inout"


############################################
# Definition of Classes
############################################

class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class UML2_Behavior:

    pass
class UML2_OpaqueExpression:

    pass
class UML2_ParameterSet:

    pass
class Behavior:

    pass
class UML2_Interaction(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Activity(Behavior):

    pass
class UML2_Parameter:

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
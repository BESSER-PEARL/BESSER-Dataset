from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"
    return_ = "return_"


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
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
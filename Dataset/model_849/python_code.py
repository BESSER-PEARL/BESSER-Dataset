from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, input: str, output: str, leavingTransitions: "fsm_State" = None, Transition: "fsm_State" = None, fsm_Transition: "fsm_State" = None):
        self.input = input
        self.output = output
        self.leavingTransitions = leavingTransitions
        self.Transition = Transition
        self.fsm_Transition = fsm_Transition
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def leavingTransitions(self):
        return self.__leavingTransitions

    @leavingTransitions.setter
    def leavingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__leavingTransitions", None)
        self.__leavingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State9"):
                opp_val = getattr(old_value, "State9", None)
                if opp_val == self:
                    setattr(old_value, "State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State9"):
                opp_val = getattr(value, "State9", None)
                setattr(value, "State9", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State7"):
                opp_val = getattr(old_value, "fsm_State7", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State7"):
                opp_val = getattr(value, "fsm_State7", None)
                setattr(value, "fsm_State7", self)

class fsm_NamedElement(ABC):

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
class fsm_State(NamedElement):

    pass
class fsm_FiniteStateMachine(NamedElement):

    pass
class fsm_Model(NamedElement):

    pass
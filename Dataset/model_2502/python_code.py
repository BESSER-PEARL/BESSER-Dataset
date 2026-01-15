from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class InitialState:

    pass
class TimedState:

    pass
class tfsm_TimedInitialState(InitialState, TimedState):

    pass
class FinalState:

    pass
class BinaryClockConstraint:

    pass
class tfsm_OrClockConstraint(BinaryClockConstraint):

    pass
class tfsm_AndClockConstraint(BinaryClockConstraint):

    pass
class tfsm_TimedFinalState(TimedState, FinalState):

    pass
class ClockConstraint:

    pass
class tfsm_LowerEqualClockConstraint(ClockConstraint):

    pass
class tfsm_LowerClockConstraint(ClockConstraint):

    pass
class tfsm_UpperEqualClockConstraint(ClockConstraint):

    pass
class tfsm_UpperClockConstraint(ClockConstraint):

    pass
class tfsm_ClockReset:

    pass
class ClockConstraintOperation:

    pass
class tfsm_ClockConstraint(ClockConstraintOperation):

    def __init__(self, threshold: int, tfsm_ClockConstraint: "tfsm_Clock" = None):
        self.threshold = threshold
        self.tfsm_ClockConstraint = tfsm_ClockConstraint
        
    @property
    def threshold(self) -> int:
        return self.__threshold

    @threshold.setter
    def threshold(self, threshold: int):
        self.__threshold = threshold

    @property
    def tfsm_ClockConstraint(self):
        return self.__tfsm_ClockConstraint

    @tfsm_ClockConstraint.setter
    def tfsm_ClockConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_ClockConstraint__tfsm_ClockConstraint", None)
        self.__tfsm_ClockConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_Clock7"):
                opp_val = getattr(old_value, "tfsm_Clock7", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_Clock7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_Clock7"):
                opp_val = getattr(value, "tfsm_Clock7", None)
                setattr(value, "tfsm_Clock7", self)

class tfsm_BinaryClockConstraint(ClockConstraintOperation):

    pass
class FSM:

    pass
class tfsm_TimedFSM(FSM):

    pass
class Transition:

    pass
class tfsm_TimedTransition(Transition):

    pass
class tfsm_ClockConstraintOperation(ABC):

    pass
class State:

    pass
class tfsm_TimedState(State):

    pass
class tfsm_Clock:

    def __init__(self, name: str, tick: int, tfsm_Clock: "tfsm_TimedFSM" = None, tfsm_Clock7: "tfsm_ClockConstraint" = None, tfsm_Clock10: "tfsm_ClockReset" = None):
        self.name = name
        self.tick = tick
        self.tfsm_Clock = tfsm_Clock
        self.tfsm_Clock7 = tfsm_Clock7
        self.tfsm_Clock10 = tfsm_Clock10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tick(self) -> int:
        return self.__tick

    @tick.setter
    def tick(self, tick: int):
        self.__tick = tick

    @property
    def tfsm_Clock10(self):
        return self.__tfsm_Clock10

    @tfsm_Clock10.setter
    def tfsm_Clock10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Clock__tfsm_Clock10", None)
        self.__tfsm_Clock10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_ClockReset9"):
                opp_val = getattr(old_value, "tfsm_ClockReset9", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_ClockReset9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_ClockReset9"):
                opp_val = getattr(value, "tfsm_ClockReset9", None)
                setattr(value, "tfsm_ClockReset9", self)

    @property
    def tfsm_Clock(self):
        return self.__tfsm_Clock

    @tfsm_Clock.setter
    def tfsm_Clock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Clock__tfsm_Clock", None)
        self.__tfsm_Clock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TimedFSM"):
                opp_val = getattr(old_value, "tfsm_TimedFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TimedFSM"):
                opp_val = getattr(value, "tfsm_TimedFSM", None)
                if opp_val is None:
                    setattr(value, "tfsm_TimedFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_Clock7(self):
        return self.__tfsm_Clock7

    @tfsm_Clock7.setter
    def tfsm_Clock7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Clock__tfsm_Clock7", None)
        self.__tfsm_Clock7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_ClockConstraint"):
                opp_val = getattr(old_value, "tfsm_ClockConstraint", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_ClockConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_ClockConstraint"):
                opp_val = getattr(value, "tfsm_ClockConstraint", None)
                setattr(value, "tfsm_ClockConstraint", self)

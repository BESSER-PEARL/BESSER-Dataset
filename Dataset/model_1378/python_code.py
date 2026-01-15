from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class tsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tsm_TimeEvent:

    def __init__(self, time: int, tsm_TimeEvent: "tsm_Transition" = None):
        self.time = time
        self.tsm_TimeEvent = tsm_TimeEvent
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def tsm_TimeEvent(self):
        return self.__tsm_TimeEvent

    @tsm_TimeEvent.setter
    def tsm_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tsm_TimeEvent__tsm_TimeEvent", None)
        self.__tsm_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tsm_Transition10"):
                opp_val = getattr(old_value, "tsm_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "tsm_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tsm_Transition10"):
                opp_val = getattr(value, "tsm_Transition10", None)
                setattr(value, "tsm_Transition10", self)

class NamedElement:

    pass
class tsm_Transition(NamedElement):

    pass
class tsm_State(NamedElement):

    pass
class tsm_StateMachine(NamedElement):

    pass
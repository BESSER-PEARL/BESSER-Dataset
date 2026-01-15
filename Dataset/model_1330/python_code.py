from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class states_ActionExecution:

    pass
class states_Event:

    def __init__(self, qualifiedName: str, states_Event: "states_Transition" = None, states_Event16: "states_ActionExecution" = None):
        self.qualifiedName = qualifiedName
        self.states_Event = states_Event
        self.states_Event16 = states_Event16
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def states_Event(self):
        return self.__states_Event

    @states_Event.setter
    def states_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Event__states_Event", None)
        self.__states_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_Transition14"):
                opp_val = getattr(old_value, "states_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "states_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_Transition14"):
                opp_val = getattr(value, "states_Transition14", None)
                setattr(value, "states_Transition14", self)

    @property
    def states_Event16(self):
        return self.__states_Event16

    @states_Event16.setter
    def states_Event16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Event__states_Event16", None)
        self.__states_Event16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_ActionExecution"):
                opp_val = getattr(old_value, "states_ActionExecution", None)
                if opp_val == self:
                    setattr(old_value, "states_ActionExecution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_ActionExecution"):
                opp_val = getattr(value, "states_ActionExecution", None)
                setattr(value, "states_ActionExecution", self)

class states_EObject:

    pass
class states_Trace:

    pass
class states_Transition:

    pass
class states_State:

    pass
class states_StateSystem:

    pass
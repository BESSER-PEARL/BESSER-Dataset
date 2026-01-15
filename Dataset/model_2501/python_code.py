from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tfsm_Guard:

    def __init__(self, time: int, tfsm_Guard: "tfsm_Transition" = None):
        self.time = time
        self.tfsm_Guard = tfsm_Guard
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def tfsm_Guard(self):
        return self.__tfsm_Guard

    @tfsm_Guard.setter
    def tfsm_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Guard__tfsm_Guard", None)
        self.__tfsm_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_Transition"):
                opp_val = getattr(old_value, "tfsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_Transition"):
                opp_val = getattr(value, "tfsm_Transition", None)
                setattr(value, "tfsm_Transition", self)

class Transition:

    pass
class tfsm_Transition(Transition):

    pass
class State:

    pass
class tfsm_State(State):

    def __init__(self, time: int, tfsm_State: "tfsm_FSM" = None):
        self.time = time
        self.tfsm_State = tfsm_State
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def tfsm_State(self):
        return self.__tfsm_State

    @tfsm_State.setter
    def tfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__tfsm_State", None)
        self.__tfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSM"):
                opp_val = getattr(old_value, "tfsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSM"):
                opp_val = getattr(value, "tfsm_FSM", None)
                setattr(value, "tfsm_FSM", self)

class FSM:

    pass
class tfsm_FSM(FSM):

    pass
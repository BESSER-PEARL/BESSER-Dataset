from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class HSM_StateMachine:

    pass
class State:

    pass
class HSM_FinalState(State):

    pass
class HSM_InitialState(State):

    pass
class HSM_CompositeState(State):

    pass
class HSM_State:

    def __init__(self, name: str, HSM_State: "HSM_StateMachine" = None):
        self.name = name
        self.HSM_State = HSM_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HSM_State(self):
        return self.__HSM_State

    @HSM_State.setter
    def HSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State", None)
        self.__HSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_StateMachine"):
                opp_val = getattr(old_value, "HSM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_StateMachine"):
                opp_val = getattr(value, "HSM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "HSM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

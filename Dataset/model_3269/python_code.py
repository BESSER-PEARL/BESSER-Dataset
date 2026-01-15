from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class SM_FinalState(State):

    pass
class SM_InitialState(State):

    pass
class SM_State:

    def __init__(self, name: str, SM_State: "SM_StateMachine" = None):
        self.name = name
        self.SM_State = SM_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SM_State(self):
        return self.__SM_State

    @SM_State.setter
    def SM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_State__SM_State", None)
        self.__SM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SM_StateMachine"):
                opp_val = getattr(old_value, "SM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SM_StateMachine"):
                opp_val = getattr(value, "SM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "SM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SM_StateMachine:

    pass
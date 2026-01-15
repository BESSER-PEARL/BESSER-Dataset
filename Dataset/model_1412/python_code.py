from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NHSM_Transition:

    pass
class NHSM_State:

    def __init__(self, name: str, NHSM_State: "NHSM_StateMachine" = None, NHSM_State5: "NHSM_Transition" = None, NHSM_State8: "NHSM_Transition" = None):
        self.name = name
        self.NHSM_State = NHSM_State
        self.NHSM_State5 = NHSM_State5
        self.NHSM_State8 = NHSM_State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def NHSM_State5(self):
        return self.__NHSM_State5

    @NHSM_State5.setter
    def NHSM_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__NHSM_State5", None)
        self.__NHSM_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_Transition4"):
                opp_val = getattr(old_value, "NHSM_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_Transition4"):
                opp_val = getattr(value, "NHSM_Transition4", None)
                setattr(value, "NHSM_Transition4", self)

    @property
    def NHSM_State8(self):
        return self.__NHSM_State8

    @NHSM_State8.setter
    def NHSM_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__NHSM_State8", None)
        self.__NHSM_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_Transition7"):
                opp_val = getattr(old_value, "NHSM_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_Transition7"):
                opp_val = getattr(value, "NHSM_Transition7", None)
                setattr(value, "NHSM_Transition7", self)

    @property
    def NHSM_State(self):
        return self.__NHSM_State

    @NHSM_State.setter
    def NHSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__NHSM_State", None)
        self.__NHSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_StateMachine"):
                opp_val = getattr(old_value, "NHSM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_StateMachine"):
                opp_val = getattr(value, "NHSM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "NHSM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NHSM_StateMachine:

    pass
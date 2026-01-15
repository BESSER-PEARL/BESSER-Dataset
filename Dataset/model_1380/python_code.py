from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class statemachine_Final(State):

    pass
class statemachine_Initial(State):

    pass
class statemachine_Transition:

    pass
class statemachine_State:

    def __init__(self, time: str, statemachine_State: "statemachine_FSM" = None, statemachine_State5: "statemachine_FSM" = None, statemachine_State11: "statemachine_Transition" = None, statemachine_State14: "statemachine_Transition" = None, statemachine_State8: "statemachine_State" = None, statemachine_State6: set["statemachine_State"] = None):
        self.time = time
        self.statemachine_State = statemachine_State
        self.statemachine_State5 = statemachine_State5
        self.statemachine_State11 = statemachine_State11
        self.statemachine_State14 = statemachine_State14
        self.statemachine_State8 = statemachine_State8
        self.statemachine_State6 = statemachine_State6 if statemachine_State6 is not None else set()
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def statemachine_State6(self):
        return self.__statemachine_State6

    @statemachine_State6.setter
    def statemachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State6", None)
        self.__statemachine_State6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State8"):
                    opp_val = getattr(item, "statemachine_State8", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State8"):
                    opp_val = getattr(item, "statemachine_State8", None)
                    
                    setattr(item, "statemachine_State8", self)
                    

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_FSM"):
                opp_val = getattr(old_value, "statemachine_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_FSM"):
                opp_val = getattr(value, "statemachine_FSM", None)
                if opp_val is None:
                    setattr(value, "statemachine_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State11(self):
        return self.__statemachine_State11

    @statemachine_State11.setter
    def statemachine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State11", None)
        self.__statemachine_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition10"):
                opp_val = getattr(old_value, "statemachine_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition10"):
                opp_val = getattr(value, "statemachine_Transition10", None)
                setattr(value, "statemachine_Transition10", self)

    @property
    def statemachine_State5(self):
        return self.__statemachine_State5

    @statemachine_State5.setter
    def statemachine_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State5", None)
        self.__statemachine_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_FSM4"):
                opp_val = getattr(old_value, "statemachine_FSM4", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_FSM4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_FSM4"):
                opp_val = getattr(value, "statemachine_FSM4", None)
                setattr(value, "statemachine_FSM4", self)

    @property
    def statemachine_State8(self):
        return self.__statemachine_State8

    @statemachine_State8.setter
    def statemachine_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State8", None)
        self.__statemachine_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State6"):
                opp_val = getattr(old_value, "statemachine_State6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State6"):
                opp_val = getattr(value, "statemachine_State6", None)
                if opp_val is None:
                    setattr(value, "statemachine_State6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State14(self):
        return self.__statemachine_State14

    @statemachine_State14.setter
    def statemachine_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State14", None)
        self.__statemachine_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition13"):
                opp_val = getattr(old_value, "statemachine_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition13"):
                opp_val = getattr(value, "statemachine_Transition13", None)
                setattr(value, "statemachine_Transition13", self)

class statemachine_FSM:

    pass
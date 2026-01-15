from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class fsm_FinalState(State):

    pass
class fsm_InitialState(State):

    pass
class fsm_Transition:

    pass
class fsm_State:

    def __init__(self, name: str, fsm_State: "fsm_FSM" = None, fsm_State7: "fsm_Transition" = None, fsm_State10: "fsm_Transition" = None):
        self.name = name
        self.fsm_State = fsm_State
        self.fsm_State7 = fsm_State7
        self.fsm_State10 = fsm_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_State10(self):
        return self.__fsm_State10

    @fsm_State10.setter
    def fsm_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State10", None)
        self.__fsm_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition9"):
                opp_val = getattr(old_value, "fsm_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition9"):
                opp_val = getattr(value, "fsm_Transition9", None)
                setattr(value, "fsm_Transition9", self)

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM"):
                opp_val = getattr(old_value, "fsm_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM"):
                opp_val = getattr(value, "fsm_FSM", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State7(self):
        return self.__fsm_State7

    @fsm_State7.setter
    def fsm_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State7", None)
        self.__fsm_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition6"):
                opp_val = getattr(old_value, "fsm_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition6"):
                opp_val = getattr(value, "fsm_Transition6", None)
                setattr(value, "fsm_Transition6", self)

class fsm_FSM:

    def __init__(self, name: str, fsm_FSM: set["fsm_State"] = None, fsm_FSM2: set["fsm_Transition"] = None, fsm_FSM4: "fsm_InitialState" = None):
        self.name = name
        self.fsm_FSM = fsm_FSM if fsm_FSM is not None else set()
        self.fsm_FSM2 = fsm_FSM2 if fsm_FSM2 is not None else set()
        self.fsm_FSM4 = fsm_FSM4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_FSM4(self):
        return self.__fsm_FSM4

    @fsm_FSM4.setter
    def fsm_FSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM4", None)
        self.__fsm_FSM4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_InitialState"):
                opp_val = getattr(old_value, "fsm_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "fsm_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_InitialState"):
                opp_val = getattr(value, "fsm_InitialState", None)
                setattr(value, "fsm_InitialState", self)

    @property
    def fsm_FSM2(self):
        return self.__fsm_FSM2

    @fsm_FSM2.setter
    def fsm_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM2", None)
        self.__fsm_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    setattr(item, "fsm_Transition", self)
                    

    @property
    def fsm_FSM(self):
        return self.__fsm_FSM

    @fsm_FSM.setter
    def fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM", None)
        self.__fsm_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    setattr(item, "fsm_State", self)
                    

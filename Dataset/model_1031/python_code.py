from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, name: str, trigger: str, fsm_Transition4: set["fsm_State"] = None, fsm_Transition: "fsm_FSM" = None):
        self.name = name
        self.trigger = trigger
        self.fsm_Transition4 = fsm_Transition4 if fsm_Transition4 is not None else set()
        self.fsm_Transition = fsm_Transition
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "fsm_FSM2"):
                opp_val = getattr(old_value, "fsm_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM2"):
                opp_val = getattr(value, "fsm_FSM2", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition4(self):
        return self.__fsm_Transition4

    @fsm_Transition4.setter
    def fsm_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition4", None)
        self.__fsm_Transition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State5"):
                    opp_val = getattr(item, "fsm_State5", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State5"):
                    opp_val = getattr(item, "fsm_State5", None)
                    
                    setattr(item, "fsm_State5", self)
                    

class fsm_State:

    def __init__(self, name: str, fsm_State5: "fsm_Transition" = None, fsm_State: "fsm_FSM" = None):
        self.name = name
        self.fsm_State5 = fsm_State5
        self.fsm_State = fsm_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_State5(self):
        return self.__fsm_State5

    @fsm_State5.setter
    def fsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State5", None)
        self.__fsm_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition4"):
                opp_val = getattr(old_value, "fsm_Transition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition4"):
                opp_val = getattr(value, "fsm_Transition4", None)
                if opp_val is None:
                    setattr(value, "fsm_Transition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class fsm_FSM:

    def __init__(self, name: str, fsm_FSM: set["fsm_State"] = None, fsm_FSM2: set["fsm_Transition"] = None):
        self.name = name
        self.fsm_FSM = fsm_FSM if fsm_FSM is not None else set()
        self.fsm_FSM2 = fsm_FSM2 if fsm_FSM2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

class State:

    pass
class fsm_Final(State):

    pass
class fsm_Initial(State):

    pass
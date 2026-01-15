from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class fsm_tp_InitialState(State):

    pass
class fsm_tp_Transition:

    def __init__(self, name: str, trigger: str, fsm_tp_Transition: "fsm_tp_FSM" = None, fsm_tp_Transition6: "fsm_tp_State" = None, fsm_tp_Transition9: "fsm_tp_State" = None):
        self.name = name
        self.trigger = trigger
        self.fsm_tp_Transition = fsm_tp_Transition
        self.fsm_tp_Transition6 = fsm_tp_Transition6
        self.fsm_tp_Transition9 = fsm_tp_Transition9
        
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
    def fsm_tp_Transition9(self):
        return self.__fsm_tp_Transition9

    @fsm_tp_Transition9.setter
    def fsm_tp_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_Transition__fsm_tp_Transition9", None)
        self.__fsm_tp_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_tp_State10"):
                opp_val = getattr(old_value, "fsm_tp_State10", None)
                if opp_val == self:
                    setattr(old_value, "fsm_tp_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_tp_State10"):
                opp_val = getattr(value, "fsm_tp_State10", None)
                setattr(value, "fsm_tp_State10", self)

    @property
    def fsm_tp_Transition(self):
        return self.__fsm_tp_Transition

    @fsm_tp_Transition.setter
    def fsm_tp_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_Transition__fsm_tp_Transition", None)
        self.__fsm_tp_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_tp_FSM2"):
                opp_val = getattr(old_value, "fsm_tp_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_tp_FSM2"):
                opp_val = getattr(value, "fsm_tp_FSM2", None)
                if opp_val is None:
                    setattr(value, "fsm_tp_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_tp_Transition6(self):
        return self.__fsm_tp_Transition6

    @fsm_tp_Transition6.setter
    def fsm_tp_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_Transition__fsm_tp_Transition6", None)
        self.__fsm_tp_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_tp_State7"):
                opp_val = getattr(old_value, "fsm_tp_State7", None)
                if opp_val == self:
                    setattr(old_value, "fsm_tp_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_tp_State7"):
                opp_val = getattr(value, "fsm_tp_State7", None)
                setattr(value, "fsm_tp_State7", self)

class fsm_tp_State:

    def __init__(self, name: str, isFinal: bool, fsm_tp_State: "fsm_tp_FSM" = None, fsm_tp_State7: "fsm_tp_Transition" = None, fsm_tp_State10: "fsm_tp_Transition" = None):
        self.name = name
        self.isFinal = isFinal
        self.fsm_tp_State = fsm_tp_State
        self.fsm_tp_State7 = fsm_tp_State7
        self.fsm_tp_State10 = fsm_tp_State10
        
    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_tp_State7(self):
        return self.__fsm_tp_State7

    @fsm_tp_State7.setter
    def fsm_tp_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_State__fsm_tp_State7", None)
        self.__fsm_tp_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_tp_Transition6"):
                opp_val = getattr(old_value, "fsm_tp_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "fsm_tp_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_tp_Transition6"):
                opp_val = getattr(value, "fsm_tp_Transition6", None)
                setattr(value, "fsm_tp_Transition6", self)

    @property
    def fsm_tp_State10(self):
        return self.__fsm_tp_State10

    @fsm_tp_State10.setter
    def fsm_tp_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_State__fsm_tp_State10", None)
        self.__fsm_tp_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_tp_Transition9"):
                opp_val = getattr(old_value, "fsm_tp_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "fsm_tp_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_tp_Transition9"):
                opp_val = getattr(value, "fsm_tp_Transition9", None)
                setattr(value, "fsm_tp_Transition9", self)

    @property
    def fsm_tp_State(self):
        return self.__fsm_tp_State

    @fsm_tp_State.setter
    def fsm_tp_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_State__fsm_tp_State", None)
        self.__fsm_tp_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_tp_FSM"):
                opp_val = getattr(old_value, "fsm_tp_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_tp_FSM"):
                opp_val = getattr(value, "fsm_tp_FSM", None)
                if opp_val is None:
                    setattr(value, "fsm_tp_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_tp_FSM:

    def __init__(self, name: str, fsm_tp_FSM: set["fsm_tp_State"] = None, fsm_tp_FSM2: set["fsm_tp_Transition"] = None, fsm_tp_FSM4: "fsm_tp_InitialState" = None):
        self.name = name
        self.fsm_tp_FSM = fsm_tp_FSM if fsm_tp_FSM is not None else set()
        self.fsm_tp_FSM2 = fsm_tp_FSM2 if fsm_tp_FSM2 is not None else set()
        self.fsm_tp_FSM4 = fsm_tp_FSM4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_tp_FSM4(self):
        return self.__fsm_tp_FSM4

    @fsm_tp_FSM4.setter
    def fsm_tp_FSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_FSM__fsm_tp_FSM4", None)
        self.__fsm_tp_FSM4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_tp_InitialState"):
                opp_val = getattr(old_value, "fsm_tp_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "fsm_tp_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_tp_InitialState"):
                opp_val = getattr(value, "fsm_tp_InitialState", None)
                setattr(value, "fsm_tp_InitialState", self)

    @property
    def fsm_tp_FSM(self):
        return self.__fsm_tp_FSM

    @fsm_tp_FSM.setter
    def fsm_tp_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_FSM__fsm_tp_FSM", None)
        self.__fsm_tp_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_tp_State"):
                    opp_val = getattr(item, "fsm_tp_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_tp_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_tp_State"):
                    opp_val = getattr(item, "fsm_tp_State", None)
                    
                    setattr(item, "fsm_tp_State", self)
                    

    @property
    def fsm_tp_FSM2(self):
        return self.__fsm_tp_FSM2

    @fsm_tp_FSM2.setter
    def fsm_tp_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_tp_FSM__fsm_tp_FSM2", None)
        self.__fsm_tp_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_tp_Transition"):
                    opp_val = getattr(item, "fsm_tp_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_tp_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_tp_Transition"):
                    opp_val = getattr(item, "fsm_tp_Transition", None)
                    
                    setattr(item, "fsm_tp_Transition", self)
                    

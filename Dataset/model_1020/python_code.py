from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class fsm_Initial(State):

    pass
class fsm_Final(State):

    pass
class fsm_FSM:

    def __init__(self, name: str, fsm_FSM: set["fsm_State"] = None, fsm_FSM7: set["fsm_Transition"] = None):
        self.name = name
        self.fsm_FSM = fsm_FSM if fsm_FSM is not None else set()
        self.fsm_FSM7 = fsm_FSM7 if fsm_FSM7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

    @property
    def fsm_FSM7(self):
        return self.__fsm_FSM7

    @fsm_FSM7.setter
    def fsm_FSM7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM7", None)
        self.__fsm_FSM7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition8"):
                    opp_val = getattr(item, "fsm_Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition8"):
                    opp_val = getattr(item, "fsm_Transition8", None)
                    
                    setattr(item, "fsm_Transition8", self)
                    

class fsm_State:

    def __init__(self, name: str, fsm_State: "fsm_Transition" = None, fsm_State3: "fsm_Transition" = None, fsm_State5: "fsm_FSM" = None):
        self.name = name
        self.fsm_State = fsm_State
        self.fsm_State3 = fsm_State3
        self.fsm_State5 = fsm_State5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_State3(self):
        return self.__fsm_State3

    @fsm_State3.setter
    def fsm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State3", None)
        self.__fsm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition2"):
                opp_val = getattr(old_value, "fsm_Transition2", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition2"):
                opp_val = getattr(value, "fsm_Transition2", None)
                setattr(value, "fsm_Transition2", self)

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
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition"):
                opp_val = getattr(old_value, "fsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition"):
                opp_val = getattr(value, "fsm_Transition", None)
                setattr(value, "fsm_Transition", self)

class fsm_Transition:

    def __init__(self, name: str, fsm_Transition: "fsm_State" = None, fsm_Transition2: "fsm_State" = None, fsm_Transition8: "fsm_FSM" = None):
        self.name = name
        self.fsm_Transition = fsm_Transition
        self.fsm_Transition2 = fsm_Transition2
        self.fsm_Transition8 = fsm_Transition8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Transition8(self):
        return self.__fsm_Transition8

    @fsm_Transition8.setter
    def fsm_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition8", None)
        self.__fsm_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM7"):
                opp_val = getattr(old_value, "fsm_FSM7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM7"):
                opp_val = getattr(value, "fsm_FSM7", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "fsm_State"):
                opp_val = getattr(old_value, "fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State"):
                opp_val = getattr(value, "fsm_State", None)
                setattr(value, "fsm_State", self)

    @property
    def fsm_Transition2(self):
        return self.__fsm_Transition2

    @fsm_Transition2.setter
    def fsm_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition2", None)
        self.__fsm_Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State3"):
                opp_val = getattr(old_value, "fsm_State3", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State3"):
                opp_val = getattr(value, "fsm_State3", None)
                setattr(value, "fsm_State3", self)

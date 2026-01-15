from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tp01_Transition:

    def __init__(self, name: str, tp01_Transition4: "tp01_State" = None, tp01_Transition7: "tp01_State" = None, tp01_Transition: "tp01_FSM" = None):
        self.name = name
        self.tp01_Transition4 = tp01_Transition4
        self.tp01_Transition7 = tp01_Transition7
        self.tp01_Transition = tp01_Transition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp01_Transition4(self):
        return self.__tp01_Transition4

    @tp01_Transition4.setter
    def tp01_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_Transition__tp01_Transition4", None)
        self.__tp01_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp01_State5"):
                opp_val = getattr(old_value, "tp01_State5", None)
                if opp_val == self:
                    setattr(old_value, "tp01_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp01_State5"):
                opp_val = getattr(value, "tp01_State5", None)
                setattr(value, "tp01_State5", self)

    @property
    def tp01_Transition(self):
        return self.__tp01_Transition

    @tp01_Transition.setter
    def tp01_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_Transition__tp01_Transition", None)
        self.__tp01_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp01_FSM2"):
                opp_val = getattr(old_value, "tp01_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp01_FSM2"):
                opp_val = getattr(value, "tp01_FSM2", None)
                if opp_val is None:
                    setattr(value, "tp01_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp01_Transition7(self):
        return self.__tp01_Transition7

    @tp01_Transition7.setter
    def tp01_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_Transition__tp01_Transition7", None)
        self.__tp01_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp01_State8"):
                opp_val = getattr(old_value, "tp01_State8", None)
                if opp_val == self:
                    setattr(old_value, "tp01_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp01_State8"):
                opp_val = getattr(value, "tp01_State8", None)
                setattr(value, "tp01_State8", self)

class tp01_State:

    def __init__(self, name: str, tp01_State5: "tp01_Transition" = None, tp01_State8: "tp01_Transition" = None, tp01_State: "tp01_FSM" = None):
        self.name = name
        self.tp01_State5 = tp01_State5
        self.tp01_State8 = tp01_State8
        self.tp01_State = tp01_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp01_State8(self):
        return self.__tp01_State8

    @tp01_State8.setter
    def tp01_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_State__tp01_State8", None)
        self.__tp01_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp01_Transition7"):
                opp_val = getattr(old_value, "tp01_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "tp01_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp01_Transition7"):
                opp_val = getattr(value, "tp01_Transition7", None)
                setattr(value, "tp01_Transition7", self)

    @property
    def tp01_State(self):
        return self.__tp01_State

    @tp01_State.setter
    def tp01_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_State__tp01_State", None)
        self.__tp01_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp01_FSM"):
                opp_val = getattr(old_value, "tp01_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp01_FSM"):
                opp_val = getattr(value, "tp01_FSM", None)
                if opp_val is None:
                    setattr(value, "tp01_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp01_State5(self):
        return self.__tp01_State5

    @tp01_State5.setter
    def tp01_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_State__tp01_State5", None)
        self.__tp01_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp01_Transition4"):
                opp_val = getattr(old_value, "tp01_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "tp01_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp01_Transition4"):
                opp_val = getattr(value, "tp01_Transition4", None)
                setattr(value, "tp01_Transition4", self)

class State:

    pass
class tp01_FinalState(State):

    pass
class tp01_StartState(State):

    pass
class tp01_FSM:

    def __init__(self, name: str, tp01_FSM: set["tp01_State"] = None, tp01_FSM2: set["tp01_Transition"] = None):
        self.name = name
        self.tp01_FSM = tp01_FSM if tp01_FSM is not None else set()
        self.tp01_FSM2 = tp01_FSM2 if tp01_FSM2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp01_FSM(self):
        return self.__tp01_FSM

    @tp01_FSM.setter
    def tp01_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_FSM__tp01_FSM", None)
        self.__tp01_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp01_State"):
                    opp_val = getattr(item, "tp01_State", None)
                    
                    if opp_val == self:
                        setattr(item, "tp01_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp01_State"):
                    opp_val = getattr(item, "tp01_State", None)
                    
                    setattr(item, "tp01_State", self)
                    

    @property
    def tp01_FSM2(self):
        return self.__tp01_FSM2

    @tp01_FSM2.setter
    def tp01_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp01_FSM__tp01_FSM2", None)
        self.__tp01_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp01_Transition"):
                    opp_val = getattr(item, "tp01_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tp01_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp01_Transition"):
                    opp_val = getattr(item, "tp01_Transition", None)
                    
                    setattr(item, "tp01_Transition", self)
                    

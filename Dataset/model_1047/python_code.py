from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fMS_Transition:

    def __init__(self, name: str, fMS_Transition: "fMS_FSM" = None, fMS_Transition4: "fMS_State" = None, fMS_Transition7: "fMS_State" = None):
        self.name = name
        self.fMS_Transition = fMS_Transition
        self.fMS_Transition4 = fMS_Transition4
        self.fMS_Transition7 = fMS_Transition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fMS_Transition4(self):
        return self.__fMS_Transition4

    @fMS_Transition4.setter
    def fMS_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_Transition__fMS_Transition4", None)
        self.__fMS_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fMS_State5"):
                opp_val = getattr(old_value, "fMS_State5", None)
                if opp_val == self:
                    setattr(old_value, "fMS_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fMS_State5"):
                opp_val = getattr(value, "fMS_State5", None)
                setattr(value, "fMS_State5", self)

    @property
    def fMS_Transition7(self):
        return self.__fMS_Transition7

    @fMS_Transition7.setter
    def fMS_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_Transition__fMS_Transition7", None)
        self.__fMS_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fMS_State8"):
                opp_val = getattr(old_value, "fMS_State8", None)
                if opp_val == self:
                    setattr(old_value, "fMS_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fMS_State8"):
                opp_val = getattr(value, "fMS_State8", None)
                setattr(value, "fMS_State8", self)

    @property
    def fMS_Transition(self):
        return self.__fMS_Transition

    @fMS_Transition.setter
    def fMS_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_Transition__fMS_Transition", None)
        self.__fMS_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fMS_FSM2"):
                opp_val = getattr(old_value, "fMS_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fMS_FSM2"):
                opp_val = getattr(value, "fMS_FSM2", None)
                if opp_val is None:
                    setattr(value, "fMS_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fMS_State:

    def __init__(self, name: str, fMS_State5: "fMS_Transition" = None, fMS_State8: "fMS_Transition" = None, fMS_State: "fMS_FSM" = None):
        self.name = name
        self.fMS_State5 = fMS_State5
        self.fMS_State8 = fMS_State8
        self.fMS_State = fMS_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fMS_State8(self):
        return self.__fMS_State8

    @fMS_State8.setter
    def fMS_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_State__fMS_State8", None)
        self.__fMS_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fMS_Transition7"):
                opp_val = getattr(old_value, "fMS_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "fMS_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fMS_Transition7"):
                opp_val = getattr(value, "fMS_Transition7", None)
                setattr(value, "fMS_Transition7", self)

    @property
    def fMS_State(self):
        return self.__fMS_State

    @fMS_State.setter
    def fMS_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_State__fMS_State", None)
        self.__fMS_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fMS_FSM"):
                opp_val = getattr(old_value, "fMS_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fMS_FSM"):
                opp_val = getattr(value, "fMS_FSM", None)
                if opp_val is None:
                    setattr(value, "fMS_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fMS_State5(self):
        return self.__fMS_State5

    @fMS_State5.setter
    def fMS_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_State__fMS_State5", None)
        self.__fMS_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fMS_Transition4"):
                opp_val = getattr(old_value, "fMS_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "fMS_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fMS_Transition4"):
                opp_val = getattr(value, "fMS_Transition4", None)
                setattr(value, "fMS_Transition4", self)

class fMS_FSM:

    def __init__(self, name: str, fMS_FSM2: set["fMS_Transition"] = None, fMS_FSM: set["fMS_State"] = None):
        self.name = name
        self.fMS_FSM2 = fMS_FSM2 if fMS_FSM2 is not None else set()
        self.fMS_FSM = fMS_FSM if fMS_FSM is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fMS_FSM(self):
        return self.__fMS_FSM

    @fMS_FSM.setter
    def fMS_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_FSM__fMS_FSM", None)
        self.__fMS_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fMS_State"):
                    opp_val = getattr(item, "fMS_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fMS_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fMS_State"):
                    opp_val = getattr(item, "fMS_State", None)
                    
                    setattr(item, "fMS_State", self)
                    

    @property
    def fMS_FSM2(self):
        return self.__fMS_FSM2

    @fMS_FSM2.setter
    def fMS_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fMS_FSM__fMS_FSM2", None)
        self.__fMS_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fMS_Transition"):
                    opp_val = getattr(item, "fMS_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fMS_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fMS_Transition"):
                    opp_val = getattr(item, "fMS_Transition", None)
                    
                    setattr(item, "fMS_Transition", self)
                    

class State:

    pass
class fMS_FinalState(State):

    pass
class fMS_InitState(State):

    pass
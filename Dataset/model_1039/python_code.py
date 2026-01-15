from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, name: str, fsm_Transition: "fsm_State" = None, fsm_Transition7: "fsm_State" = None):
        self.name = name
        self.fsm_Transition = fsm_Transition
        self.fsm_Transition7 = fsm_Transition7
        
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
            if hasattr(old_value, "fsm_State5"):
                opp_val = getattr(old_value, "fsm_State5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State5"):
                opp_val = getattr(value, "fsm_State5", None)
                if opp_val is None:
                    setattr(value, "fsm_State5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition7(self):
        return self.__fsm_Transition7

    @fsm_Transition7.setter
    def fsm_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition7", None)
        self.__fsm_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State8"):
                opp_val = getattr(old_value, "fsm_State8", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State8"):
                opp_val = getattr(value, "fsm_State8", None)
                setattr(value, "fsm_State8", self)

class fsm_State:

    def __init__(self, name: str, fsm_State: "fsm_Fsm" = None, fsm_State3: "fsm_Fsm" = None, fsm_State5: set["fsm_Transition"] = None, fsm_State8: "fsm_Transition" = None):
        self.name = name
        self.fsm_State = fsm_State
        self.fsm_State3 = fsm_State3
        self.fsm_State5 = fsm_State5 if fsm_State5 is not None else set()
        self.fsm_State8 = fsm_State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_State8(self):
        return self.__fsm_State8

    @fsm_State8.setter
    def fsm_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State8", None)
        self.__fsm_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition7"):
                opp_val = getattr(old_value, "fsm_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition7"):
                opp_val = getattr(value, "fsm_Transition7", None)
                setattr(value, "fsm_Transition7", self)

    @property
    def fsm_State5(self):
        return self.__fsm_State5

    @fsm_State5.setter
    def fsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State5", None)
        self.__fsm_State5 = value if value is not None else set()
        
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
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Fsm"):
                opp_val = getattr(old_value, "fsm_Fsm", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Fsm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Fsm"):
                opp_val = getattr(value, "fsm_Fsm", None)
                setattr(value, "fsm_Fsm", self)

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
            if hasattr(old_value, "fsm_Fsm2"):
                opp_val = getattr(old_value, "fsm_Fsm2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Fsm2"):
                opp_val = getattr(value, "fsm_Fsm2", None)
                if opp_val is None:
                    setattr(value, "fsm_Fsm2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_Fsm:

    def __init__(self, name: str, fsm_Fsm: "fsm_State" = None, fsm_Fsm2: set["fsm_State"] = None):
        self.name = name
        self.fsm_Fsm = fsm_Fsm
        self.fsm_Fsm2 = fsm_Fsm2 if fsm_Fsm2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Fsm2(self):
        return self.__fsm_Fsm2

    @fsm_Fsm2.setter
    def fsm_Fsm2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Fsm__fsm_Fsm2", None)
        self.__fsm_Fsm2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State3"):
                    opp_val = getattr(item, "fsm_State3", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State3"):
                    opp_val = getattr(item, "fsm_State3", None)
                    
                    setattr(item, "fsm_State3", self)
                    

    @property
    def fsm_Fsm(self):
        return self.__fsm_Fsm

    @fsm_Fsm.setter
    def fsm_Fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Fsm__fsm_Fsm", None)
        self.__fsm_Fsm = value
        
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

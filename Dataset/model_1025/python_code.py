from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class nicoLang_FinalState(State):

    pass
class nicoLang_InitState(State):

    pass
class nicoLang_State:

    def __init__(self, name: str, nicoLang_State: "nicoLang_FSM" = None, nicoLang_State5: "nicoLang_Transition" = None, nicoLang_State8: "nicoLang_Transition" = None):
        self.name = name
        self.nicoLang_State = nicoLang_State
        self.nicoLang_State5 = nicoLang_State5
        self.nicoLang_State8 = nicoLang_State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nicoLang_State8(self):
        return self.__nicoLang_State8

    @nicoLang_State8.setter
    def nicoLang_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_State__nicoLang_State8", None)
        self.__nicoLang_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nicoLang_Transition7"):
                opp_val = getattr(old_value, "nicoLang_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "nicoLang_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nicoLang_Transition7"):
                opp_val = getattr(value, "nicoLang_Transition7", None)
                setattr(value, "nicoLang_Transition7", self)

    @property
    def nicoLang_State5(self):
        return self.__nicoLang_State5

    @nicoLang_State5.setter
    def nicoLang_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_State__nicoLang_State5", None)
        self.__nicoLang_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nicoLang_Transition4"):
                opp_val = getattr(old_value, "nicoLang_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "nicoLang_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nicoLang_Transition4"):
                opp_val = getattr(value, "nicoLang_Transition4", None)
                setattr(value, "nicoLang_Transition4", self)

    @property
    def nicoLang_State(self):
        return self.__nicoLang_State

    @nicoLang_State.setter
    def nicoLang_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_State__nicoLang_State", None)
        self.__nicoLang_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nicoLang_FSM2"):
                opp_val = getattr(old_value, "nicoLang_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nicoLang_FSM2"):
                opp_val = getattr(value, "nicoLang_FSM2", None)
                if opp_val is None:
                    setattr(value, "nicoLang_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nicoLang_Transition:

    def __init__(self, name: str, trigger: str, nicoLang_Transition: "nicoLang_FSM" = None, nicoLang_Transition4: "nicoLang_State" = None, nicoLang_Transition7: "nicoLang_State" = None):
        self.name = name
        self.trigger = trigger
        self.nicoLang_Transition = nicoLang_Transition
        self.nicoLang_Transition4 = nicoLang_Transition4
        self.nicoLang_Transition7 = nicoLang_Transition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def nicoLang_Transition7(self):
        return self.__nicoLang_Transition7

    @nicoLang_Transition7.setter
    def nicoLang_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_Transition__nicoLang_Transition7", None)
        self.__nicoLang_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nicoLang_State8"):
                opp_val = getattr(old_value, "nicoLang_State8", None)
                if opp_val == self:
                    setattr(old_value, "nicoLang_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nicoLang_State8"):
                opp_val = getattr(value, "nicoLang_State8", None)
                setattr(value, "nicoLang_State8", self)

    @property
    def nicoLang_Transition(self):
        return self.__nicoLang_Transition

    @nicoLang_Transition.setter
    def nicoLang_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_Transition__nicoLang_Transition", None)
        self.__nicoLang_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nicoLang_FSM"):
                opp_val = getattr(old_value, "nicoLang_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nicoLang_FSM"):
                opp_val = getattr(value, "nicoLang_FSM", None)
                if opp_val is None:
                    setattr(value, "nicoLang_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nicoLang_Transition4(self):
        return self.__nicoLang_Transition4

    @nicoLang_Transition4.setter
    def nicoLang_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_Transition__nicoLang_Transition4", None)
        self.__nicoLang_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nicoLang_State5"):
                opp_val = getattr(old_value, "nicoLang_State5", None)
                if opp_val == self:
                    setattr(old_value, "nicoLang_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nicoLang_State5"):
                opp_val = getattr(value, "nicoLang_State5", None)
                setattr(value, "nicoLang_State5", self)

class nicoLang_FSM:

    def __init__(self, name: str, nicoLang_FSM: set["nicoLang_Transition"] = None, nicoLang_FSM2: set["nicoLang_State"] = None):
        self.name = name
        self.nicoLang_FSM = nicoLang_FSM if nicoLang_FSM is not None else set()
        self.nicoLang_FSM2 = nicoLang_FSM2 if nicoLang_FSM2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nicoLang_FSM2(self):
        return self.__nicoLang_FSM2

    @nicoLang_FSM2.setter
    def nicoLang_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_FSM__nicoLang_FSM2", None)
        self.__nicoLang_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nicoLang_State"):
                    opp_val = getattr(item, "nicoLang_State", None)
                    
                    if opp_val == self:
                        setattr(item, "nicoLang_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nicoLang_State"):
                    opp_val = getattr(item, "nicoLang_State", None)
                    
                    setattr(item, "nicoLang_State", self)
                    

    @property
    def nicoLang_FSM(self):
        return self.__nicoLang_FSM

    @nicoLang_FSM.setter
    def nicoLang_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nicoLang_FSM__nicoLang_FSM", None)
        self.__nicoLang_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nicoLang_Transition"):
                    opp_val = getattr(item, "nicoLang_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "nicoLang_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nicoLang_Transition"):
                    opp_val = getattr(item, "nicoLang_Transition", None)
                    
                    setattr(item, "nicoLang_Transition", self)
                    

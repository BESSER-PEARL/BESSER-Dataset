from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Guard:

    pass
class tfsm_EventGuard(Guard):

    pass
class tfsm_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class tfsm_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, tfsm_TemporalGuard: "tfsm_FSMClock" = None):
        self.afterDuration = afterDuration
        self.tfsm_TemporalGuard = tfsm_TemporalGuard
        
    @property
    def afterDuration(self) -> int:
        return self.__afterDuration

    @afterDuration.setter
    def afterDuration(self, afterDuration: int):
        self.__afterDuration = afterDuration

    @property
    def tfsm_TemporalGuard(self):
        return self.__tfsm_TemporalGuard

    @tfsm_TemporalGuard.setter
    def tfsm_TemporalGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TemporalGuard__tfsm_TemporalGuard", None)
        self.__tfsm_TemporalGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSMClock30"):
                opp_val = getattr(old_value, "tfsm_FSMClock30", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSMClock30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMClock30"):
                opp_val = getattr(value, "tfsm_FSMClock30", None)
                setattr(value, "tfsm_FSMClock30", self)

class tfsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class tfsm_Guard(NamedElement):

    pass
class tfsm_TimedSystem(NamedElement):

    pass
class tfsm_Transition(NamedElement):

    def __init__(self, action: str, 14: "tfsm_State" = None, 17: "tfsm_State" = None, 19: "tfsm_State" = None, 22: "tfsm_State" = None, tfsm_Transition25: "tfsm_Guard" = None, tfsm_Transition27: set["tfsm_FSMEvent"] = None, tfsm_Transition: "tfsm_TFSM" = None, tfsm_Transition35: "tfsm_FSMEvent" = None):
        self.action = action
        self.14 = 14
        self.17 = 17
        self.19 = 19
        self.22 = 22
        self.tfsm_Transition25 = tfsm_Transition25
        self.tfsm_Transition27 = tfsm_Transition27 if tfsm_Transition27 is not None else set()
        self.tfsm_Transition = tfsm_Transition
        self.tfsm_Transition35 = tfsm_Transition35
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def tfsm_Transition35(self):
        return self.__tfsm_Transition35

    @tfsm_Transition35.setter
    def tfsm_Transition35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition35", None)
        self.__tfsm_Transition35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSMEvent34"):
                opp_val = getattr(old_value, "tfsm_FSMEvent34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMEvent34"):
                opp_val = getattr(value, "tfsm_FSMEvent34", None)
                if opp_val is None:
                    setattr(value, "tfsm_FSMEvent34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_Transition(self):
        return self.__tfsm_Transition

    @tfsm_Transition.setter
    def tfsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition", None)
        self.__tfsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TFSM8"):
                opp_val = getattr(old_value, "tfsm_TFSM8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TFSM8"):
                opp_val = getattr(value, "tfsm_TFSM8", None)
                if opp_val is None:
                    setattr(value, "tfsm_TFSM8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                if opp_val is None:
                    setattr(value, "13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_Transition25(self):
        return self.__tfsm_Transition25

    @tfsm_Transition25.setter
    def tfsm_Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition25", None)
        self.__tfsm_Transition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_Guard"):
                opp_val = getattr(old_value, "tfsm_Guard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_Guard"):
                opp_val = getattr(value, "tfsm_Guard", None)
                setattr(value, "tfsm_Guard", self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__22", None)
        self.__22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "23"):
                opp_val = getattr(old_value, "23", None)
                if opp_val == self:
                    setattr(old_value, "23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "23"):
                opp_val = getattr(value, "23", None)
                setattr(value, "23", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                if opp_val is None:
                    setattr(value, "16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_Transition27(self):
        return self.__tfsm_Transition27

    @tfsm_Transition27.setter
    def tfsm_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition27", None)
        self.__tfsm_Transition27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_FSMEvent28"):
                    opp_val = getattr(item, "tfsm_FSMEvent28", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMEvent28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMEvent28"):
                    opp_val = getattr(item, "tfsm_FSMEvent28", None)
                    
                    setattr(item, "tfsm_FSMEvent28", self)
                    

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__19", None)
        self.__19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "20"):
                opp_val = getattr(old_value, "20", None)
                if opp_val == self:
                    setattr(old_value, "20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "20"):
                opp_val = getattr(value, "20", None)
                setattr(value, "20", self)

class tfsm_FSMClock(NamedElement):

    pass
class tfsm_State(NamedElement):

    pass
class tfsm_FSMEvent(NamedElement):

    pass
class tfsm_TFSM(NamedElement):

    pass
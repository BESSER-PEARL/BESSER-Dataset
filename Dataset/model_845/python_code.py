from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Guard:

    pass
class tfsm_plaink3_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class tfsm_plaink3_EventGuard(Guard):

    def __init__(self, tfsm_plaink3_EventGuard: "tfsm_plaink3_FSMEvent" = None):
        self.tfsm_plaink3_EventGuard = tfsm_plaink3_EventGuard
        
    @property
    def tfsm_plaink3_EventGuard(self):
        return self.__tfsm_plaink3_EventGuard

    @tfsm_plaink3_EventGuard.setter
    def tfsm_plaink3_EventGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_EventGuard__tfsm_plaink3_EventGuard", None)
        self.__tfsm_plaink3_EventGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_FSMEvent35"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMEvent35", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_FSMEvent35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMEvent35"):
                opp_val = getattr(value, "tfsm_plaink3_FSMEvent35", None)
                setattr(value, "tfsm_plaink3_FSMEvent35", self)

    def visit(self):
        # TODO: Implement visit method
        pass

class tfsm_plaink3_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, tfsm_plaink3_TemporalGuard: "tfsm_plaink3_FSMClock" = None):
        self.afterDuration = afterDuration
        self.tfsm_plaink3_TemporalGuard = tfsm_plaink3_TemporalGuard
        
    @property
    def afterDuration(self) -> int:
        return self.__afterDuration

    @afterDuration.setter
    def afterDuration(self, afterDuration: int):
        self.__afterDuration = afterDuration

    @property
    def tfsm_plaink3_TemporalGuard(self):
        return self.__tfsm_plaink3_TemporalGuard

    @tfsm_plaink3_TemporalGuard.setter
    def tfsm_plaink3_TemporalGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TemporalGuard__tfsm_plaink3_TemporalGuard", None)
        self.__tfsm_plaink3_TemporalGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_FSMClock33"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMClock33", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_FSMClock33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMClock33"):
                opp_val = getattr(value, "tfsm_plaink3_FSMClock33", None)
                setattr(value, "tfsm_plaink3_FSMClock33", self)

    def visit(self):
        # TODO: Implement visit method
        pass

class tfsm_plaink3_NamedElement(ABC):

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
class tfsm_plaink3_Guard(NamedElement):

    def __init__(self, tfsm_plaink3_Guard: "tfsm_plaink3_Transition" = None):
        self.tfsm_plaink3_Guard = tfsm_plaink3_Guard
        
    @property
    def tfsm_plaink3_Guard(self):
        return self.__tfsm_plaink3_Guard

    @tfsm_plaink3_Guard.setter
    def tfsm_plaink3_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Guard__tfsm_plaink3_Guard", None)
        self.__tfsm_plaink3_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_Transition28"):
                opp_val = getattr(old_value, "tfsm_plaink3_Transition28", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_Transition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_Transition28"):
                opp_val = getattr(value, "tfsm_plaink3_Transition28", None)
                setattr(value, "tfsm_plaink3_Transition28", self)

    def visit(self):
        # TODO: Implement visit method
        pass

class tfsm_plaink3_FSMClock(NamedElement):

    def __init__(self, numberOfTicks: str, tfsm_plaink3_FSMClock: "tfsm_plaink3_TFSM" = None, tfsm_plaink3_FSMClock33: "tfsm_plaink3_TemporalGuard" = None, tfsm_plaink3_FSMClock43: "tfsm_plaink3_TimedSystem" = None):
        self.numberOfTicks = numberOfTicks
        self.tfsm_plaink3_FSMClock = tfsm_plaink3_FSMClock
        self.tfsm_plaink3_FSMClock33 = tfsm_plaink3_FSMClock33
        self.tfsm_plaink3_FSMClock43 = tfsm_plaink3_FSMClock43
        
    @property
    def numberOfTicks(self) -> str:
        return self.__numberOfTicks

    @numberOfTicks.setter
    def numberOfTicks(self, numberOfTicks: str):
        self.__numberOfTicks = numberOfTicks

    @property
    def tfsm_plaink3_FSMClock43(self):
        return self.__tfsm_plaink3_FSMClock43

    @tfsm_plaink3_FSMClock43.setter
    def tfsm_plaink3_FSMClock43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMClock__tfsm_plaink3_FSMClock43", None)
        self.__tfsm_plaink3_FSMClock43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TimedSystem42"):
                opp_val = getattr(old_value, "tfsm_plaink3_TimedSystem42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TimedSystem42"):
                opp_val = getattr(value, "tfsm_plaink3_TimedSystem42", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TimedSystem42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_FSMClock(self):
        return self.__tfsm_plaink3_FSMClock

    @tfsm_plaink3_FSMClock.setter
    def tfsm_plaink3_FSMClock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMClock__tfsm_plaink3_FSMClock", None)
        self.__tfsm_plaink3_FSMClock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM6"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM6", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_TFSM6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM6"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM6", None)
                setattr(value, "tfsm_plaink3_TFSM6", self)

    @property
    def tfsm_plaink3_FSMClock33(self):
        return self.__tfsm_plaink3_FSMClock33

    @tfsm_plaink3_FSMClock33.setter
    def tfsm_plaink3_FSMClock33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMClock__tfsm_plaink3_FSMClock33", None)
        self.__tfsm_plaink3_FSMClock33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TemporalGuard"):
                opp_val = getattr(old_value, "tfsm_plaink3_TemporalGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_TemporalGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TemporalGuard"):
                opp_val = getattr(value, "tfsm_plaink3_TemporalGuard", None)
                setattr(value, "tfsm_plaink3_TemporalGuard", self)

    def visit(self):
        # TODO: Implement visit method
        pass

    def ticks(self):
        # TODO: Implement ticks method
        pass

class tfsm_plaink3_TimedSystem(NamedElement):

    def __init__(self, tfsm_plaink3_TimedSystem: set["tfsm_plaink3_TFSM"] = None, tfsm_plaink3_TimedSystem42: set["tfsm_plaink3_FSMClock"] = None, tfsm_plaink3_TimedSystem45: set["tfsm_plaink3_FSMEvent"] = None):
        self.tfsm_plaink3_TimedSystem = tfsm_plaink3_TimedSystem if tfsm_plaink3_TimedSystem is not None else set()
        self.tfsm_plaink3_TimedSystem42 = tfsm_plaink3_TimedSystem42 if tfsm_plaink3_TimedSystem42 is not None else set()
        self.tfsm_plaink3_TimedSystem45 = tfsm_plaink3_TimedSystem45 if tfsm_plaink3_TimedSystem45 is not None else set()
        
    @property
    def tfsm_plaink3_TimedSystem45(self):
        return self.__tfsm_plaink3_TimedSystem45

    @tfsm_plaink3_TimedSystem45.setter
    def tfsm_plaink3_TimedSystem45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TimedSystem__tfsm_plaink3_TimedSystem45", None)
        self.__tfsm_plaink3_TimedSystem45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_FSMEvent46"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent46", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_FSMEvent46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_FSMEvent46"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent46", None)
                    
                    setattr(item, "tfsm_plaink3_FSMEvent46", self)
                    

    @property
    def tfsm_plaink3_TimedSystem42(self):
        return self.__tfsm_plaink3_TimedSystem42

    @tfsm_plaink3_TimedSystem42.setter
    def tfsm_plaink3_TimedSystem42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TimedSystem__tfsm_plaink3_TimedSystem42", None)
        self.__tfsm_plaink3_TimedSystem42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_FSMClock43"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMClock43", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_FSMClock43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_FSMClock43"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMClock43", None)
                    
                    setattr(item, "tfsm_plaink3_FSMClock43", self)
                    

    @property
    def tfsm_plaink3_TimedSystem(self):
        return self.__tfsm_plaink3_TimedSystem

    @tfsm_plaink3_TimedSystem.setter
    def tfsm_plaink3_TimedSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TimedSystem__tfsm_plaink3_TimedSystem", None)
        self.__tfsm_plaink3_TimedSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_TFSM40"):
                    opp_val = getattr(item, "tfsm_plaink3_TFSM40", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_TFSM40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_TFSM40"):
                    opp_val = getattr(item, "tfsm_plaink3_TFSM40", None)
                    
                    setattr(item, "tfsm_plaink3_TFSM40", self)
                    

    def main(self):
        # TODO: Implement main method
        pass

    def initializeModel(self, args: str):
        # TODO: Implement initializeModel method
        pass

    def visit(self):
        # TODO: Implement visit method
        pass

class tfsm_plaink3_FSMEvent(NamedElement):

    def __init__(self, isTriggered: str, tfsm_plaink3_FSMEvent: "tfsm_plaink3_TFSM" = None, tfsm_plaink3_FSMEvent31: "tfsm_plaink3_Transition" = None, tfsm_plaink3_FSMEvent35: "tfsm_plaink3_EventGuard" = None, tfsm_plaink3_FSMEvent37: set["tfsm_plaink3_Transition"] = None, tfsm_plaink3_FSMEvent46: "tfsm_plaink3_TimedSystem" = None):
        self.isTriggered = isTriggered
        self.tfsm_plaink3_FSMEvent = tfsm_plaink3_FSMEvent
        self.tfsm_plaink3_FSMEvent31 = tfsm_plaink3_FSMEvent31
        self.tfsm_plaink3_FSMEvent35 = tfsm_plaink3_FSMEvent35
        self.tfsm_plaink3_FSMEvent37 = tfsm_plaink3_FSMEvent37 if tfsm_plaink3_FSMEvent37 is not None else set()
        self.tfsm_plaink3_FSMEvent46 = tfsm_plaink3_FSMEvent46
        
    @property
    def isTriggered(self) -> str:
        return self.__isTriggered

    @isTriggered.setter
    def isTriggered(self, isTriggered: str):
        self.__isTriggered = isTriggered

    @property
    def tfsm_plaink3_FSMEvent46(self):
        return self.__tfsm_plaink3_FSMEvent46

    @tfsm_plaink3_FSMEvent46.setter
    def tfsm_plaink3_FSMEvent46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent46", None)
        self.__tfsm_plaink3_FSMEvent46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TimedSystem45"):
                opp_val = getattr(old_value, "tfsm_plaink3_TimedSystem45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TimedSystem45"):
                opp_val = getattr(value, "tfsm_plaink3_TimedSystem45", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TimedSystem45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_FSMEvent31(self):
        return self.__tfsm_plaink3_FSMEvent31

    @tfsm_plaink3_FSMEvent31.setter
    def tfsm_plaink3_FSMEvent31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent31", None)
        self.__tfsm_plaink3_FSMEvent31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_Transition30"):
                opp_val = getattr(old_value, "tfsm_plaink3_Transition30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_Transition30"):
                opp_val = getattr(value, "tfsm_plaink3_Transition30", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_Transition30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_FSMEvent35(self):
        return self.__tfsm_plaink3_FSMEvent35

    @tfsm_plaink3_FSMEvent35.setter
    def tfsm_plaink3_FSMEvent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent35", None)
        self.__tfsm_plaink3_FSMEvent35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_EventGuard"):
                opp_val = getattr(old_value, "tfsm_plaink3_EventGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_EventGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_EventGuard"):
                opp_val = getattr(value, "tfsm_plaink3_EventGuard", None)
                setattr(value, "tfsm_plaink3_EventGuard", self)

    @property
    def tfsm_plaink3_FSMEvent37(self):
        return self.__tfsm_plaink3_FSMEvent37

    @tfsm_plaink3_FSMEvent37.setter
    def tfsm_plaink3_FSMEvent37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent37", None)
        self.__tfsm_plaink3_FSMEvent37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_Transition38"):
                    opp_val = getattr(item, "tfsm_plaink3_Transition38", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_Transition38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_Transition38"):
                    opp_val = getattr(item, "tfsm_plaink3_Transition38", None)
                    
                    setattr(item, "tfsm_plaink3_Transition38", self)
                    

    @property
    def tfsm_plaink3_FSMEvent(self):
        return self.__tfsm_plaink3_FSMEvent

    @tfsm_plaink3_FSMEvent.setter
    def tfsm_plaink3_FSMEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent", None)
        self.__tfsm_plaink3_FSMEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM4"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM4"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM4", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TFSM4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def trigger(self):
        # TODO: Implement trigger method
        pass

    def unTrigger(self):
        # TODO: Implement unTrigger method
        pass

class tfsm_plaink3_Transition(NamedElement):

    def __init__(self, action: str, tfsm_plaink3_Transition: "tfsm_plaink3_TFSM" = None, 17: "tfsm_plaink3_State" = None, 20: "tfsm_plaink3_State" = None, 25: "tfsm_plaink3_State" = None, tfsm_plaink3_Transition28: "tfsm_plaink3_Guard" = None, tfsm_plaink3_Transition30: set["tfsm_plaink3_FSMEvent"] = None, tfsm_plaink3_Transition38: "tfsm_plaink3_FSMEvent" = None, 22: "tfsm_plaink3_State" = None):
        self.action = action
        self.tfsm_plaink3_Transition = tfsm_plaink3_Transition
        self.17 = 17
        self.20 = 20
        self.25 = 25
        self.tfsm_plaink3_Transition28 = tfsm_plaink3_Transition28
        self.tfsm_plaink3_Transition30 = tfsm_plaink3_Transition30 if tfsm_plaink3_Transition30 is not None else set()
        self.tfsm_plaink3_Transition38 = tfsm_plaink3_Transition38
        self.22 = 22
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__22", None)
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
    def tfsm_plaink3_Transition30(self):
        return self.__tfsm_plaink3_Transition30

    @tfsm_plaink3_Transition30.setter
    def tfsm_plaink3_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition30", None)
        self.__tfsm_plaink3_Transition30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_FSMEvent31"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent31", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_FSMEvent31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_FSMEvent31"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent31", None)
                    
                    setattr(item, "tfsm_plaink3_FSMEvent31", self)
                    

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "19"):
                opp_val = getattr(old_value, "19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "19"):
                opp_val = getattr(value, "19", None)
                if opp_val is None:
                    setattr(value, "19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_Transition38(self):
        return self.__tfsm_plaink3_Transition38

    @tfsm_plaink3_Transition38.setter
    def tfsm_plaink3_Transition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition38", None)
        self.__tfsm_plaink3_Transition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_FSMEvent37"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMEvent37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMEvent37"):
                opp_val = getattr(value, "tfsm_plaink3_FSMEvent37", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_FSMEvent37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_Transition28(self):
        return self.__tfsm_plaink3_Transition28

    @tfsm_plaink3_Transition28.setter
    def tfsm_plaink3_Transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition28", None)
        self.__tfsm_plaink3_Transition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_Guard"):
                opp_val = getattr(old_value, "tfsm_plaink3_Guard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_Guard"):
                opp_val = getattr(value, "tfsm_plaink3_Guard", None)
                setattr(value, "tfsm_plaink3_Guard", self)

    @property
    def 25(self):
        return self.__25

    @25.setter
    def 25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__25", None)
        self.__25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "26"):
                opp_val = getattr(old_value, "26", None)
                if opp_val == self:
                    setattr(old_value, "26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "26"):
                opp_val = getattr(value, "26", None)
                setattr(value, "26", self)

    @property
    def tfsm_plaink3_Transition(self):
        return self.__tfsm_plaink3_Transition

    @tfsm_plaink3_Transition.setter
    def tfsm_plaink3_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition", None)
        self.__tfsm_plaink3_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM8"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM8"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM8", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TFSM8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__17", None)
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

    def visit(self):
        # TODO: Implement visit method
        pass

    def fire(self):
        # TODO: Implement fire method
        pass

class tfsm_plaink3_TFSM(NamedElement):

    def __init__(self, stepNumber: int, lastStateChangeStepNumber: int, : set["tfsm_plaink3_State"] = None, tfsm_plaink3_TFSM: "tfsm_plaink3_State" = None, tfsm_plaink3_TFSM4: set["tfsm_plaink3_FSMEvent"] = None, tfsm_plaink3_TFSM6: "tfsm_plaink3_FSMClock" = None, tfsm_plaink3_TFSM8: set["tfsm_plaink3_Transition"] = None, tfsm_plaink3_TFSM10: "tfsm_plaink3_State" = None, 14: "tfsm_plaink3_State" = None, tfsm_plaink3_TFSM40: "tfsm_plaink3_TimedSystem" = None):
        self.stepNumber = stepNumber
        self.lastStateChangeStepNumber = lastStateChangeStepNumber
        self. =  if  is not None else set()
        self.tfsm_plaink3_TFSM = tfsm_plaink3_TFSM
        self.tfsm_plaink3_TFSM4 = tfsm_plaink3_TFSM4 if tfsm_plaink3_TFSM4 is not None else set()
        self.tfsm_plaink3_TFSM6 = tfsm_plaink3_TFSM6
        self.tfsm_plaink3_TFSM8 = tfsm_plaink3_TFSM8 if tfsm_plaink3_TFSM8 is not None else set()
        self.tfsm_plaink3_TFSM10 = tfsm_plaink3_TFSM10
        self.14 = 14
        self.tfsm_plaink3_TFSM40 = tfsm_plaink3_TFSM40
        
    @property
    def lastStateChangeStepNumber(self) -> int:
        return self.__lastStateChangeStepNumber

    @lastStateChangeStepNumber.setter
    def lastStateChangeStepNumber(self, lastStateChangeStepNumber: int):
        self.__lastStateChangeStepNumber = lastStateChangeStepNumber

    @property
    def stepNumber(self) -> int:
        return self.__stepNumber

    @stepNumber.setter
    def stepNumber(self, stepNumber: int):
        self.__stepNumber = stepNumber

    @property
    def tfsm_plaink3_TFSM6(self):
        return self.__tfsm_plaink3_TFSM6

    @tfsm_plaink3_TFSM6.setter
    def tfsm_plaink3_TFSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__tfsm_plaink3_TFSM6", None)
        self.__tfsm_plaink3_TFSM6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_FSMClock"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMClock", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_FSMClock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMClock"):
                opp_val = getattr(value, "tfsm_plaink3_FSMClock", None)
                setattr(value, "tfsm_plaink3_FSMClock", self)

    @property
    def tfsm_plaink3_TFSM10(self):
        return self.__tfsm_plaink3_TFSM10

    @tfsm_plaink3_TFSM10.setter
    def tfsm_plaink3_TFSM10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__tfsm_plaink3_TFSM10", None)
        self.__tfsm_plaink3_TFSM10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_State11"):
                opp_val = getattr(old_value, "tfsm_plaink3_State11", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_State11"):
                opp_val = getattr(value, "tfsm_plaink3_State11", None)
                setattr(value, "tfsm_plaink3_State11", self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    @property
    def tfsm_plaink3_TFSM8(self):
        return self.__tfsm_plaink3_TFSM8

    @tfsm_plaink3_TFSM8.setter
    def tfsm_plaink3_TFSM8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__tfsm_plaink3_TFSM8", None)
        self.__tfsm_plaink3_TFSM8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_Transition"):
                    opp_val = getattr(item, "tfsm_plaink3_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_Transition"):
                    opp_val = getattr(item, "tfsm_plaink3_Transition", None)
                    
                    setattr(item, "tfsm_plaink3_Transition", self)
                    

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

    @property
    def tfsm_plaink3_TFSM4(self):
        return self.__tfsm_plaink3_TFSM4

    @tfsm_plaink3_TFSM4.setter
    def tfsm_plaink3_TFSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__tfsm_plaink3_TFSM4", None)
        self.__tfsm_plaink3_TFSM4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_FSMEvent"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_FSMEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_FSMEvent"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent", None)
                    
                    setattr(item, "tfsm_plaink3_FSMEvent", self)
                    

    @property
    def tfsm_plaink3_TFSM40(self):
        return self.__tfsm_plaink3_TFSM40

    @tfsm_plaink3_TFSM40.setter
    def tfsm_plaink3_TFSM40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__tfsm_plaink3_TFSM40", None)
        self.__tfsm_plaink3_TFSM40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TimedSystem"):
                opp_val = getattr(old_value, "tfsm_plaink3_TimedSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TimedSystem"):
                opp_val = getattr(value, "tfsm_plaink3_TimedSystem", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TimedSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_TFSM(self):
        return self.__tfsm_plaink3_TFSM

    @tfsm_plaink3_TFSM.setter
    def tfsm_plaink3_TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TFSM__tfsm_plaink3_TFSM", None)
        self.__tfsm_plaink3_TFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_State"):
                opp_val = getattr(old_value, "tfsm_plaink3_State", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_State"):
                opp_val = getattr(value, "tfsm_plaink3_State", None)
                setattr(value, "tfsm_plaink3_State", self)

    def visit(self):
        # TODO: Implement visit method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class tfsm_plaink3_State(NamedElement):

    def __init__(self, 1: "tfsm_plaink3_TFSM" = None, tfsm_plaink3_State: "tfsm_plaink3_TFSM" = None, tfsm_plaink3_State11: "tfsm_plaink3_TFSM" = None, 13: "tfsm_plaink3_TFSM" = None, 16: set["tfsm_plaink3_Transition"] = None, 26: "tfsm_plaink3_Transition" = None, 19: set["tfsm_plaink3_Transition"] = None, 23: "tfsm_plaink3_Transition" = None):
        self.1 = 1
        self.tfsm_plaink3_State = tfsm_plaink3_State
        self.tfsm_plaink3_State11 = tfsm_plaink3_State11
        self.13 = 13
        self.16 = 16 if 16 is not None else set()
        self.26 = 26
        self.19 = 19 if 19 is not None else set()
        self.23 = 23
        
    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__19", None)
        self.__19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    if opp_val == self:
                        setattr(item, "20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    setattr(item, "20", self)
                    

    @property
    def tfsm_plaink3_State(self):
        return self.__tfsm_plaink3_State

    @tfsm_plaink3_State.setter
    def tfsm_plaink3_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__tfsm_plaink3_State", None)
        self.__tfsm_plaink3_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_TFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM", None)
                setattr(value, "tfsm_plaink3_TFSM", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if opp_val == self:
                    setattr(old_value, "14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                setattr(value, "14", self)

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__16", None)
        self.__16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    if opp_val == self:
                        setattr(item, "17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    setattr(item, "17", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 26(self):
        return self.__26

    @26.setter
    def 26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__26", None)
        self.__26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "25"):
                opp_val = getattr(old_value, "25", None)
                if opp_val == self:
                    setattr(old_value, "25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "25"):
                opp_val = getattr(value, "25", None)
                setattr(value, "25", self)

    @property
    def 23(self):
        return self.__23

    @23.setter
    def 23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__23", None)
        self.__23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "22"):
                opp_val = getattr(old_value, "22", None)
                if opp_val == self:
                    setattr(old_value, "22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "22"):
                opp_val = getattr(value, "22", None)
                setattr(value, "22", self)

    @property
    def tfsm_plaink3_State11(self):
        return self.__tfsm_plaink3_State11

    @tfsm_plaink3_State11.setter
    def tfsm_plaink3_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_State__tfsm_plaink3_State11", None)
        self.__tfsm_plaink3_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM10"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM10", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_TFSM10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM10"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM10", None)
                setattr(value, "tfsm_plaink3_TFSM10", self)

    def visit(self):
        # TODO: Implement visit method
        pass

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

    def onLeave(self):
        # TODO: Implement onLeave method
        pass

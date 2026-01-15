from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Event:

    pass
class rtsc_VariableAssignmentEvent(Event):

    def __init__(self, value: str, rtsc_VariableAssignmentEvent: "rtsc_Variable" = None):
        self.value = value
        self.rtsc_VariableAssignmentEvent = rtsc_VariableAssignmentEvent
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def rtsc_VariableAssignmentEvent(self):
        return self.__rtsc_VariableAssignmentEvent

    @rtsc_VariableAssignmentEvent.setter
    def rtsc_VariableAssignmentEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_VariableAssignmentEvent__rtsc_VariableAssignmentEvent", None)
        self.__rtsc_VariableAssignmentEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Variable98"):
                opp_val = getattr(old_value, "rtsc_Variable98", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Variable98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Variable98"):
                opp_val = getattr(value, "rtsc_Variable98", None)
                setattr(value, "rtsc_Variable98", self)

class rtsc_ClockResetEvent(Event):

    pass
class rtsc_MessageEvent(Event):

    pass
class rtsc_MessageTypeRepository:

    pass
class rtsc_System:

    pass
class rtsc_Message:

    pass
class rtsc_Connector:

    pass
class rtsc_MessageBuffer:

    pass
class BehavioralElement:

    pass
class rtsc_Port(BehavioralElement):

    pass
class rtsc_ClockConstraint:

    def __init__(self, bound: int, rtsc_ClockConstraint: "rtsc_Transition" = None, rtsc_ClockConstraint55: "rtsc_Clock" = None):
        self.bound = bound
        self.rtsc_ClockConstraint = rtsc_ClockConstraint
        self.rtsc_ClockConstraint55 = rtsc_ClockConstraint55
        
    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def rtsc_ClockConstraint(self):
        return self.__rtsc_ClockConstraint

    @rtsc_ClockConstraint.setter
    def rtsc_ClockConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_ClockConstraint__rtsc_ClockConstraint", None)
        self.__rtsc_ClockConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Transition43"):
                opp_val = getattr(old_value, "rtsc_Transition43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Transition43"):
                opp_val = getattr(value, "rtsc_Transition43", None)
                if opp_val is None:
                    setattr(value, "rtsc_Transition43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_ClockConstraint55(self):
        return self.__rtsc_ClockConstraint55

    @rtsc_ClockConstraint55.setter
    def rtsc_ClockConstraint55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_ClockConstraint__rtsc_ClockConstraint55", None)
        self.__rtsc_ClockConstraint55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Clock"):
                opp_val = getattr(old_value, "rtsc_Clock", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Clock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Clock"):
                opp_val = getattr(value, "rtsc_Clock", None)
                setattr(value, "rtsc_Clock", self)

class rtsc_Guard:

    def __init__(self, value: str, rtsc_Guard: "rtsc_Transition" = None, rtsc_Guard53: "rtsc_Variable" = None):
        self.value = value
        self.rtsc_Guard = rtsc_Guard
        self.rtsc_Guard53 = rtsc_Guard53
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def rtsc_Guard53(self):
        return self.__rtsc_Guard53

    @rtsc_Guard53.setter
    def rtsc_Guard53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Guard__rtsc_Guard53", None)
        self.__rtsc_Guard53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Variable"):
                opp_val = getattr(old_value, "rtsc_Variable", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Variable"):
                opp_val = getattr(value, "rtsc_Variable", None)
                setattr(value, "rtsc_Variable", self)

    @property
    def rtsc_Guard(self):
        return self.__rtsc_Guard

    @rtsc_Guard.setter
    def rtsc_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Guard__rtsc_Guard", None)
        self.__rtsc_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Transition"):
                opp_val = getattr(old_value, "rtsc_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Transition"):
                opp_val = getattr(value, "rtsc_Transition", None)
                if opp_val is None:
                    setattr(value, "rtsc_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rtsc_Event(ABC):

    pass
class rtsc_Vertex(ABC):

    pass
class rtsc_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Vertex:

    pass
class Behavior:

    pass
class NamedElement:

    pass
class rtsc_CoordinationProtocol(NamedElement):

    pass
class rtsc_Variable(NamedElement):

    def __init__(self, initialValue: str, 14: "rtsc_Realtimestatechart" = None, rtsc_Variable: "rtsc_Guard" = None, 57: "rtsc_Realtimestatechart" = None, rtsc_Variable98: "rtsc_VariableAssignmentEvent" = None):
        self.initialValue = initialValue
        self.14 = 14
        self.rtsc_Variable = rtsc_Variable
        self.57 = 57
        self.rtsc_Variable98 = rtsc_Variable98
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def 57(self):
        return self.__57

    @57.setter
    def 57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__57", None)
        self.__57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "58"):
                opp_val = getattr(old_value, "58", None)
                if opp_val == self:
                    setattr(old_value, "58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "58"):
                opp_val = getattr(value, "58", None)
                setattr(value, "58", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__14", None)
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
    def rtsc_Variable(self):
        return self.__rtsc_Variable

    @rtsc_Variable.setter
    def rtsc_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__rtsc_Variable", None)
        self.__rtsc_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Guard53"):
                opp_val = getattr(old_value, "rtsc_Guard53", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Guard53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Guard53"):
                opp_val = getattr(value, "rtsc_Guard53", None)
                setattr(value, "rtsc_Guard53", self)

    @property
    def rtsc_Variable98(self):
        return self.__rtsc_Variable98

    @rtsc_Variable98.setter
    def rtsc_Variable98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__rtsc_Variable98", None)
        self.__rtsc_Variable98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_VariableAssignmentEvent"):
                opp_val = getattr(old_value, "rtsc_VariableAssignmentEvent", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_VariableAssignmentEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_VariableAssignmentEvent"):
                opp_val = getattr(value, "rtsc_VariableAssignmentEvent", None)
                setattr(value, "rtsc_VariableAssignmentEvent", self)

class rtsc_MessageType(NamedElement):

    pass
class rtsc_Realtimestatechart(Behavior, NamedElement):

    pass
class rtsc_Transition(NamedElement):

    pass
class rtsc_Clock(NamedElement):

    pass
class rtsc_State(NamedElement, Vertex):

    def __init__(self, initial: bool, final: bool, rtsc_State19: set["rtsc_Realtimestatechart"] = None, 10: "rtsc_Realtimestatechart" = None, rtsc_State: "rtsc_Realtimestatechart" = None, 22: "rtsc_Realtimestatechart" = None, 25: set["rtsc_Transition"] = None, 28: set["rtsc_Transition"] = None, rtsc_State31: set["rtsc_Event"] = None, rtsc_State33: set["rtsc_Event"] = None, 37: "rtsc_Transition" = None, 40: "rtsc_Transition" = None):
        self.initial = initial
        self.final = final
        self.rtsc_State19 = rtsc_State19 if rtsc_State19 is not None else set()
        self.10 = 10
        self.rtsc_State = rtsc_State
        self.22 = 22
        self.25 = 25 if 25 is not None else set()
        self.28 = 28 if 28 is not None else set()
        self.rtsc_State31 = rtsc_State31 if rtsc_State31 is not None else set()
        self.rtsc_State33 = rtsc_State33 if rtsc_State33 is not None else set()
        self.37 = 37
        self.40 = 40
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def 28(self):
        return self.__28

    @28.setter
    def 28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__28", None)
        self.__28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "29"):
                    opp_val = getattr(item, "29", None)
                    
                    if opp_val == self:
                        setattr(item, "29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "29"):
                    opp_val = getattr(item, "29", None)
                    
                    setattr(item, "29", self)
                    

    @property
    def 37(self):
        return self.__37

    @37.setter
    def 37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__37", None)
        self.__37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "36"):
                opp_val = getattr(old_value, "36", None)
                if opp_val == self:
                    setattr(old_value, "36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "36"):
                opp_val = getattr(value, "36", None)
                setattr(value, "36", self)

    @property
    def 40(self):
        return self.__40

    @40.setter
    def 40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__40", None)
        self.__40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "39"):
                opp_val = getattr(old_value, "39", None)
                if opp_val == self:
                    setattr(old_value, "39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "39"):
                opp_val = getattr(value, "39", None)
                setattr(value, "39", self)

    @property
    def rtsc_State33(self):
        return self.__rtsc_State33

    @rtsc_State33.setter
    def rtsc_State33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State33", None)
        self.__rtsc_State33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Event34"):
                    opp_val = getattr(item, "rtsc_Event34", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Event34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Event34"):
                    opp_val = getattr(item, "rtsc_Event34", None)
                    
                    setattr(item, "rtsc_Event34", self)
                    

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                if opp_val is None:
                    setattr(value, "9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_State(self):
        return self.__rtsc_State

    @rtsc_State.setter
    def rtsc_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State", None)
        self.__rtsc_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Realtimestatechart"):
                opp_val = getattr(old_value, "rtsc_Realtimestatechart", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Realtimestatechart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Realtimestatechart"):
                opp_val = getattr(value, "rtsc_Realtimestatechart", None)
                setattr(value, "rtsc_Realtimestatechart", self)

    @property
    def 25(self):
        return self.__25

    @25.setter
    def 25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__25", None)
        self.__25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "26"):
                    opp_val = getattr(item, "26", None)
                    
                    if opp_val == self:
                        setattr(item, "26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "26"):
                    opp_val = getattr(item, "26", None)
                    
                    setattr(item, "26", self)
                    

    @property
    def rtsc_State31(self):
        return self.__rtsc_State31

    @rtsc_State31.setter
    def rtsc_State31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State31", None)
        self.__rtsc_State31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Event"):
                    opp_val = getattr(item, "rtsc_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Event"):
                    opp_val = getattr(item, "rtsc_Event", None)
                    
                    setattr(item, "rtsc_Event", self)
                    

    @property
    def rtsc_State19(self):
        return self.__rtsc_State19

    @rtsc_State19.setter
    def rtsc_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State19", None)
        self.__rtsc_State19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Realtimestatechart20"):
                    opp_val = getattr(item, "rtsc_Realtimestatechart20", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Realtimestatechart20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Realtimestatechart20"):
                    opp_val = getattr(item, "rtsc_Realtimestatechart20", None)
                    
                    setattr(item, "rtsc_Realtimestatechart20", self)
                    

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__22", None)
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

class rtsc_BehavioralElement(NamedElement):

    pass
class rtsc_Behavior(ABC):

    pass
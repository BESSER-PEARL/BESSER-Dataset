from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rtsc_MessageTypeRepository:

    pass
class rtsc_System:

    pass
class Event:

    pass
class rtsc_ClockResetEvent(Event):

    def __init__(self, rtsc_ClockResetEvent: "rtsc_Clock" = None):
        self.rtsc_ClockResetEvent = rtsc_ClockResetEvent
        
    @property
    def rtsc_ClockResetEvent(self):
        return self.__rtsc_ClockResetEvent

    @rtsc_ClockResetEvent.setter
    def rtsc_ClockResetEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_ClockResetEvent__rtsc_ClockResetEvent", None)
        self.__rtsc_ClockResetEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Clock102"):
                opp_val = getattr(old_value, "rtsc_Clock102", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Clock102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Clock102"):
                opp_val = getattr(value, "rtsc_Clock102", None)
                setattr(value, "rtsc_Clock102", self)

    def execute(self):
        # TODO: Implement execute method
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
            if hasattr(old_value, "rtsc_Variable104"):
                opp_val = getattr(old_value, "rtsc_Variable104", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Variable104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Variable104"):
                opp_val = getattr(value, "rtsc_Variable104", None)
                setattr(value, "rtsc_Variable104", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class rtsc_MessageEvent(Event):

    def __init__(self, rtsc_MessageEvent: "rtsc_MessageType" = None):
        self.rtsc_MessageEvent = rtsc_MessageEvent
        
    @property
    def rtsc_MessageEvent(self):
        return self.__rtsc_MessageEvent

    @rtsc_MessageEvent.setter
    def rtsc_MessageEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageEvent__rtsc_MessageEvent", None)
        self.__rtsc_MessageEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_MessageType100"):
                opp_val = getattr(old_value, "rtsc_MessageType100", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_MessageType100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_MessageType100"):
                opp_val = getattr(value, "rtsc_MessageType100", None)
                setattr(value, "rtsc_MessageType100", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class rtsc_Connector:

    pass
class rtsc_MessageBuffer:

    def __init__(self, 73: "rtsc_Port" = None, rtsc_MessageBuffer: set["rtsc_MessageType"] = None, rtsc_MessageBuffer78: set["rtsc_Message"] = None, 68: "rtsc_Port" = None):
        self.73 = 73
        self.rtsc_MessageBuffer = rtsc_MessageBuffer if rtsc_MessageBuffer is not None else set()
        self.rtsc_MessageBuffer78 = rtsc_MessageBuffer78 if rtsc_MessageBuffer78 is not None else set()
        self.68 = 68
        
    @property
    def 68(self):
        return self.__68

    @68.setter
    def 68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageBuffer__68", None)
        self.__68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "67"):
                opp_val = getattr(old_value, "67", None)
                if opp_val == self:
                    setattr(old_value, "67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "67"):
                opp_val = getattr(value, "67", None)
                setattr(value, "67", self)

    @property
    def rtsc_MessageBuffer(self):
        return self.__rtsc_MessageBuffer

    @rtsc_MessageBuffer.setter
    def rtsc_MessageBuffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageBuffer__rtsc_MessageBuffer", None)
        self.__rtsc_MessageBuffer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_MessageType76"):
                    opp_val = getattr(item, "rtsc_MessageType76", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_MessageType76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_MessageType76"):
                    opp_val = getattr(item, "rtsc_MessageType76", None)
                    
                    setattr(item, "rtsc_MessageType76", self)
                    

    @property
    def 73(self):
        return self.__73

    @73.setter
    def 73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageBuffer__73", None)
        self.__73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "74"):
                opp_val = getattr(old_value, "74", None)
                if opp_val == self:
                    setattr(old_value, "74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "74"):
                opp_val = getattr(value, "74", None)
                setattr(value, "74", self)

    @property
    def rtsc_MessageBuffer78(self):
        return self.__rtsc_MessageBuffer78

    @rtsc_MessageBuffer78.setter
    def rtsc_MessageBuffer78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageBuffer__rtsc_MessageBuffer78", None)
        self.__rtsc_MessageBuffer78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Message"):
                    opp_val = getattr(item, "rtsc_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Message"):
                    opp_val = getattr(item, "rtsc_Message", None)
                    
                    setattr(item, "rtsc_Message", self)
                    

    def hasMessage(self, type: str):
        # TODO: Implement hasMessage method
        pass

    def addMessage(self, message: str):
        # TODO: Implement addMessage method
        pass

    def getMessage(self, type: str) -> str:
        # TODO: Implement getMessage method
        pass

class BehavioralElement:

    pass
class rtsc_Port(BehavioralElement):

    pass
class rtsc_Message:

    pass
class rtsc_Vertex:

    def __init__(self, active: bool):
        self.active = active
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

class rtsc_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class rtsc_ClockConstraint:

    def __init__(self, bound: int, rtsc_ClockConstraint: "rtsc_Transition" = None, rtsc_ClockConstraint58: "rtsc_Clock" = None):
        self.bound = bound
        self.rtsc_ClockConstraint = rtsc_ClockConstraint
        self.rtsc_ClockConstraint58 = rtsc_ClockConstraint58
        
    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def rtsc_ClockConstraint58(self):
        return self.__rtsc_ClockConstraint58

    @rtsc_ClockConstraint58.setter
    def rtsc_ClockConstraint58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_ClockConstraint__rtsc_ClockConstraint58", None)
        self.__rtsc_ClockConstraint58 = value
        
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
            if hasattr(old_value, "rtsc_Transition46"):
                opp_val = getattr(old_value, "rtsc_Transition46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Transition46"):
                opp_val = getattr(value, "rtsc_Transition46", None)
                if opp_val is None:
                    setattr(value, "rtsc_Transition46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def evaluate(self, checkFederation: str):
        # TODO: Implement evaluate method
        pass

    def apply(self, federation: str):
        # TODO: Implement apply method
        pass

class rtsc_Guard:

    def __init__(self, value: bool, rtsc_Guard: "rtsc_Transition" = None, rtsc_Guard56: "rtsc_Variable" = None):
        self.value = value
        self.rtsc_Guard = rtsc_Guard
        self.rtsc_Guard56 = rtsc_Guard56
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

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
            if hasattr(old_value, "rtsc_Transition44"):
                opp_val = getattr(old_value, "rtsc_Transition44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Transition44"):
                opp_val = getattr(value, "rtsc_Transition44", None)
                if opp_val is None:
                    setattr(value, "rtsc_Transition44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Guard56(self):
        return self.__rtsc_Guard56

    @rtsc_Guard56.setter
    def rtsc_Guard56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Guard__rtsc_Guard56", None)
        self.__rtsc_Guard56 = value
        
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

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class rtsc_Event(ABC):

    def __init__(self, rtsc_Event: "rtsc_State" = None, rtsc_Event36: "rtsc_State" = None, rtsc_Event54: "rtsc_Transition" = None):
        self.rtsc_Event = rtsc_Event
        self.rtsc_Event36 = rtsc_Event36
        self.rtsc_Event54 = rtsc_Event54
        
    @property
    def rtsc_Event(self):
        return self.__rtsc_Event

    @rtsc_Event.setter
    def rtsc_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Event__rtsc_Event", None)
        self.__rtsc_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_State33"):
                opp_val = getattr(old_value, "rtsc_State33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_State33"):
                opp_val = getattr(value, "rtsc_State33", None)
                if opp_val is None:
                    setattr(value, "rtsc_State33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Event36(self):
        return self.__rtsc_Event36

    @rtsc_Event36.setter
    def rtsc_Event36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Event__rtsc_Event36", None)
        self.__rtsc_Event36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_State35"):
                opp_val = getattr(old_value, "rtsc_State35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_State35"):
                opp_val = getattr(value, "rtsc_State35", None)
                if opp_val is None:
                    setattr(value, "rtsc_State35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Event54(self):
        return self.__rtsc_Event54

    @rtsc_Event54.setter
    def rtsc_Event54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Event__rtsc_Event54", None)
        self.__rtsc_Event54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Transition53"):
                opp_val = getattr(old_value, "rtsc_Transition53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Transition53"):
                opp_val = getattr(value, "rtsc_Transition53", None)
                if opp_val is None:
                    setattr(value, "rtsc_Transition53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self):
        # TODO: Implement execute method
        pass

class Behavior:

    pass
class Vertex:

    pass
class NamedElement:

    pass
class rtsc_Realtimestatechart(Behavior, NamedElement):

    def __init__(self, rounds: int, 16: set["rtsc_Clock"] = None, rtsc_Realtimestatechart19: set["rtsc_Transition"] = None, rtsc_Realtimestatechart22: "rtsc_State" = None, 6: set["rtsc_Transition"] = None, 9: set["rtsc_State"] = None, rtsc_Realtimestatechart: "rtsc_State" = None, 13: set["rtsc_Variable"] = None, 25: "rtsc_State" = None, 61: "rtsc_Variable" = None, 49: "rtsc_Transition" = None, 64: "rtsc_Clock" = None, rtsc_Realtimestatechart90: "rtsc_System" = None):
        self.rounds = rounds
        self.16 = 16 if 16 is not None else set()
        self.rtsc_Realtimestatechart19 = rtsc_Realtimestatechart19 if rtsc_Realtimestatechart19 is not None else set()
        self.rtsc_Realtimestatechart22 = rtsc_Realtimestatechart22
        self.6 = 6 if 6 is not None else set()
        self.9 = 9 if 9 is not None else set()
        self.rtsc_Realtimestatechart = rtsc_Realtimestatechart
        self.13 = 13 if 13 is not None else set()
        self.25 = 25
        self.61 = 61
        self.49 = 49
        self.64 = 64
        self.rtsc_Realtimestatechart90 = rtsc_Realtimestatechart90
        
    @property
    def rounds(self) -> int:
        return self.__rounds

    @rounds.setter
    def rounds(self, rounds: int):
        self.__rounds = rounds

    @property
    def 64(self):
        return self.__64

    @64.setter
    def 64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__64", None)
        self.__64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "63"):
                opp_val = getattr(old_value, "63", None)
                if opp_val == self:
                    setattr(old_value, "63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "63"):
                opp_val = getattr(value, "63", None)
                setattr(value, "63", self)

    @property
    def rtsc_Realtimestatechart22(self):
        return self.__rtsc_Realtimestatechart22

    @rtsc_Realtimestatechart22.setter
    def rtsc_Realtimestatechart22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__rtsc_Realtimestatechart22", None)
        self.__rtsc_Realtimestatechart22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_State21"):
                opp_val = getattr(old_value, "rtsc_State21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_State21"):
                opp_val = getattr(value, "rtsc_State21", None)
                if opp_val is None:
                    setattr(value, "rtsc_State21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__9", None)
        self.__9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    if opp_val == self:
                        setattr(item, "10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    setattr(item, "10", self)
                    

    @property
    def 49(self):
        return self.__49

    @49.setter
    def 49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__49", None)
        self.__49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "48"):
                opp_val = getattr(old_value, "48", None)
                if opp_val == self:
                    setattr(old_value, "48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "48"):
                opp_val = getattr(value, "48", None)
                setattr(value, "48", self)

    @property
    def 25(self):
        return self.__25

    @25.setter
    def 25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__25", None)
        self.__25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "24"):
                opp_val = getattr(old_value, "24", None)
                if opp_val == self:
                    setattr(old_value, "24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "24"):
                opp_val = getattr(value, "24", None)
                setattr(value, "24", self)

    @property
    def rtsc_Realtimestatechart(self):
        return self.__rtsc_Realtimestatechart

    @rtsc_Realtimestatechart.setter
    def rtsc_Realtimestatechart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__rtsc_Realtimestatechart", None)
        self.__rtsc_Realtimestatechart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_State"):
                opp_val = getattr(old_value, "rtsc_State", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_State"):
                opp_val = getattr(value, "rtsc_State", None)
                setattr(value, "rtsc_State", self)

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__16", None)
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
    def rtsc_Realtimestatechart19(self):
        return self.__rtsc_Realtimestatechart19

    @rtsc_Realtimestatechart19.setter
    def rtsc_Realtimestatechart19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__rtsc_Realtimestatechart19", None)
        self.__rtsc_Realtimestatechart19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Transition"):
                    opp_val = getattr(item, "rtsc_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Transition"):
                    opp_val = getattr(item, "rtsc_Transition", None)
                    
                    setattr(item, "rtsc_Transition", self)
                    

    @property
    def rtsc_Realtimestatechart90(self):
        return self.__rtsc_Realtimestatechart90

    @rtsc_Realtimestatechart90.setter
    def rtsc_Realtimestatechart90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__rtsc_Realtimestatechart90", None)
        self.__rtsc_Realtimestatechart90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_System"):
                opp_val = getattr(old_value, "rtsc_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_System"):
                opp_val = getattr(value, "rtsc_System", None)
                if opp_val is None:
                    setattr(value, "rtsc_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 61(self):
        return self.__61

    @61.setter
    def 61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__61", None)
        self.__61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "60"):
                opp_val = getattr(old_value, "60", None)
                if opp_val == self:
                    setattr(old_value, "60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "60"):
                opp_val = getattr(value, "60", None)
                setattr(value, "60", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__13", None)
        self.__13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    if opp_val == self:
                        setattr(item, "14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    setattr(item, "14", self)
                    

    def initialize(self, args: str):
        # TODO: Implement initialize method
        pass

    def main(self):
        # TODO: Implement main method
        pass

    def step(self):
        # TODO: Implement step method
        pass

    def sequentialStep(self):
        # TODO: Implement sequentialStep method
        pass

class rtsc_Clock(NamedElement):

    def __init__(self, uClock: bool, 17: "rtsc_Realtimestatechart" = None, rtsc_Clock: "rtsc_ClockConstraint" = None, 63: "rtsc_Realtimestatechart" = None, rtsc_Clock102: "rtsc_ClockResetEvent" = None):
        self.uClock = uClock
        self.17 = 17
        self.rtsc_Clock = rtsc_Clock
        self.63 = 63
        self.rtsc_Clock102 = rtsc_Clock102
        
    @property
    def uClock(self) -> bool:
        return self.__uClock

    @uClock.setter
    def uClock(self, uClock: bool):
        self.__uClock = uClock

    @property
    def 63(self):
        return self.__63

    @63.setter
    def 63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Clock__63", None)
        self.__63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "64"):
                opp_val = getattr(old_value, "64", None)
                if opp_val == self:
                    setattr(old_value, "64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "64"):
                opp_val = getattr(value, "64", None)
                setattr(value, "64", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Clock__17", None)
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
    def rtsc_Clock(self):
        return self.__rtsc_Clock

    @rtsc_Clock.setter
    def rtsc_Clock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Clock__rtsc_Clock", None)
        self.__rtsc_Clock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_ClockConstraint58"):
                opp_val = getattr(old_value, "rtsc_ClockConstraint58", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_ClockConstraint58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_ClockConstraint58"):
                opp_val = getattr(value, "rtsc_ClockConstraint58", None)
                setattr(value, "rtsc_ClockConstraint58", self)

    @property
    def rtsc_Clock102(self):
        return self.__rtsc_Clock102

    @rtsc_Clock102.setter
    def rtsc_Clock102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Clock__rtsc_Clock102", None)
        self.__rtsc_Clock102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_ClockResetEvent"):
                opp_val = getattr(old_value, "rtsc_ClockResetEvent", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_ClockResetEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_ClockResetEvent"):
                opp_val = getattr(value, "rtsc_ClockResetEvent", None)
                setattr(value, "rtsc_ClockResetEvent", self)

    def reset(self):
        # TODO: Implement reset method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

    def printValue(self):
        # TODO: Implement printValue method
        pass

class rtsc_State(Vertex, NamedElement):

    def __init__(self, initial: bool, final: bool, rtsc_State21: set["rtsc_Realtimestatechart"] = None, 10: "rtsc_Realtimestatechart" = None, rtsc_State: "rtsc_Realtimestatechart" = None, 24: "rtsc_Realtimestatechart" = None, 27: set["rtsc_Transition"] = None, 30: set["rtsc_Transition"] = None, rtsc_State33: set["rtsc_Event"] = None, rtsc_State35: set["rtsc_Event"] = None, 39: "rtsc_Transition" = None, 42: "rtsc_Transition" = None):
        self.initial = initial
        self.final = final
        self.rtsc_State21 = rtsc_State21 if rtsc_State21 is not None else set()
        self.10 = 10
        self.rtsc_State = rtsc_State
        self.24 = 24
        self.27 = 27 if 27 is not None else set()
        self.30 = 30 if 30 is not None else set()
        self.rtsc_State33 = rtsc_State33 if rtsc_State33 is not None else set()
        self.rtsc_State35 = rtsc_State35 if rtsc_State35 is not None else set()
        self.39 = 39
        self.42 = 42
        
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
    def 24(self):
        return self.__24

    @24.setter
    def 24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__24", None)
        self.__24 = value
        
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
    def 27(self):
        return self.__27

    @27.setter
    def 27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__27", None)
        self.__27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "28"):
                    opp_val = getattr(item, "28", None)
                    
                    if opp_val == self:
                        setattr(item, "28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "28"):
                    opp_val = getattr(item, "28", None)
                    
                    setattr(item, "28", self)
                    

    @property
    def rtsc_State35(self):
        return self.__rtsc_State35

    @rtsc_State35.setter
    def rtsc_State35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State35", None)
        self.__rtsc_State35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Event36"):
                    opp_val = getattr(item, "rtsc_Event36", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Event36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Event36"):
                    opp_val = getattr(item, "rtsc_Event36", None)
                    
                    setattr(item, "rtsc_Event36", self)
                    

    @property
    def 30(self):
        return self.__30

    @30.setter
    def 30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__30", None)
        self.__30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "31"):
                    opp_val = getattr(item, "31", None)
                    
                    if opp_val == self:
                        setattr(item, "31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "31"):
                    opp_val = getattr(item, "31", None)
                    
                    setattr(item, "31", self)
                    

    @property
    def rtsc_State21(self):
        return self.__rtsc_State21

    @rtsc_State21.setter
    def rtsc_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State21", None)
        self.__rtsc_State21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Realtimestatechart22"):
                    opp_val = getattr(item, "rtsc_Realtimestatechart22", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Realtimestatechart22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Realtimestatechart22"):
                    opp_val = getattr(item, "rtsc_Realtimestatechart22", None)
                    
                    setattr(item, "rtsc_Realtimestatechart22", self)
                    

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
    def 42(self):
        return self.__42

    @42.setter
    def 42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__42", None)
        self.__42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "41"):
                opp_val = getattr(old_value, "41", None)
                if opp_val == self:
                    setattr(old_value, "41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "41"):
                opp_val = getattr(value, "41", None)
                setattr(value, "41", self)

    @property
    def 39(self):
        return self.__39

    @39.setter
    def 39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__39", None)
        self.__39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "38"):
                opp_val = getattr(old_value, "38", None)
                if opp_val == self:
                    setattr(old_value, "38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "38"):
                opp_val = getattr(value, "38", None)
                setattr(value, "38", self)

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

    def entry(self):
        # TODO: Implement entry method
        pass

    def exit(self):
        # TODO: Implement exit method
        pass

class rtsc_MessageType(NamedElement):

    pass
class rtsc_CoordinationProtocol(NamedElement):

    def __init__(self, rtsc_CoordinationProtocol: set["rtsc_Port"] = None, rtsc_CoordinationProtocol85: "rtsc_Connector" = None, rtsc_CoordinationProtocol93: "rtsc_System" = None):
        self.rtsc_CoordinationProtocol = rtsc_CoordinationProtocol if rtsc_CoordinationProtocol is not None else set()
        self.rtsc_CoordinationProtocol85 = rtsc_CoordinationProtocol85
        self.rtsc_CoordinationProtocol93 = rtsc_CoordinationProtocol93
        
    @property
    def rtsc_CoordinationProtocol(self):
        return self.__rtsc_CoordinationProtocol

    @rtsc_CoordinationProtocol.setter
    def rtsc_CoordinationProtocol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_CoordinationProtocol__rtsc_CoordinationProtocol", None)
        self.__rtsc_CoordinationProtocol = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Port83"):
                    opp_val = getattr(item, "rtsc_Port83", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Port83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Port83"):
                    opp_val = getattr(item, "rtsc_Port83", None)
                    
                    setattr(item, "rtsc_Port83", self)
                    

    @property
    def rtsc_CoordinationProtocol93(self):
        return self.__rtsc_CoordinationProtocol93

    @rtsc_CoordinationProtocol93.setter
    def rtsc_CoordinationProtocol93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_CoordinationProtocol__rtsc_CoordinationProtocol93", None)
        self.__rtsc_CoordinationProtocol93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_System92"):
                opp_val = getattr(old_value, "rtsc_System92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_System92"):
                opp_val = getattr(value, "rtsc_System92", None)
                if opp_val is None:
                    setattr(value, "rtsc_System92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_CoordinationProtocol85(self):
        return self.__rtsc_CoordinationProtocol85

    @rtsc_CoordinationProtocol85.setter
    def rtsc_CoordinationProtocol85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_CoordinationProtocol__rtsc_CoordinationProtocol85", None)
        self.__rtsc_CoordinationProtocol85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Connector"):
                opp_val = getattr(old_value, "rtsc_Connector", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Connector"):
                opp_val = getattr(value, "rtsc_Connector", None)
                setattr(value, "rtsc_Connector", self)

    def initialize(self, arguments: str):
        # TODO: Implement initialize method
        pass

    def step(self):
        # TODO: Implement step method
        pass

    def main(self):
        # TODO: Implement main method
        pass

class rtsc_Transition(NamedElement):

    def __init__(self, hitCount: int, rtsc_Transition: "rtsc_Realtimestatechart" = None, 7: "rtsc_Realtimestatechart" = None, 28: "rtsc_State" = None, 31: "rtsc_State" = None, 38: "rtsc_State" = None, 41: "rtsc_State" = None, rtsc_Transition44: set["rtsc_Guard"] = None, rtsc_Transition46: set["rtsc_ClockConstraint"] = None, 48: "rtsc_Realtimestatechart" = None, rtsc_Transition51: set["rtsc_MessageType"] = None, rtsc_Transition53: set["rtsc_Event"] = None):
        self.hitCount = hitCount
        self.rtsc_Transition = rtsc_Transition
        self.7 = 7
        self.28 = 28
        self.31 = 31
        self.38 = 38
        self.41 = 41
        self.rtsc_Transition44 = rtsc_Transition44 if rtsc_Transition44 is not None else set()
        self.rtsc_Transition46 = rtsc_Transition46 if rtsc_Transition46 is not None else set()
        self.48 = 48
        self.rtsc_Transition51 = rtsc_Transition51 if rtsc_Transition51 is not None else set()
        self.rtsc_Transition53 = rtsc_Transition53 if rtsc_Transition53 is not None else set()
        
    @property
    def hitCount(self) -> int:
        return self.__hitCount

    @hitCount.setter
    def hitCount(self, hitCount: int):
        self.__hitCount = hitCount

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                if opp_val is None:
                    setattr(value, "6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Transition(self):
        return self.__rtsc_Transition

    @rtsc_Transition.setter
    def rtsc_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition", None)
        self.__rtsc_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Realtimestatechart19"):
                opp_val = getattr(old_value, "rtsc_Realtimestatechart19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Realtimestatechart19"):
                opp_val = getattr(value, "rtsc_Realtimestatechart19", None)
                if opp_val is None:
                    setattr(value, "rtsc_Realtimestatechart19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 38(self):
        return self.__38

    @38.setter
    def 38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__38", None)
        self.__38 = value
        
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
    def rtsc_Transition44(self):
        return self.__rtsc_Transition44

    @rtsc_Transition44.setter
    def rtsc_Transition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition44", None)
        self.__rtsc_Transition44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Guard"):
                    opp_val = getattr(item, "rtsc_Guard", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Guard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Guard"):
                    opp_val = getattr(item, "rtsc_Guard", None)
                    
                    setattr(item, "rtsc_Guard", self)
                    

    @property
    def rtsc_Transition51(self):
        return self.__rtsc_Transition51

    @rtsc_Transition51.setter
    def rtsc_Transition51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition51", None)
        self.__rtsc_Transition51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_MessageType"):
                    opp_val = getattr(item, "rtsc_MessageType", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_MessageType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_MessageType"):
                    opp_val = getattr(item, "rtsc_MessageType", None)
                    
                    setattr(item, "rtsc_MessageType", self)
                    

    @property
    def 41(self):
        return self.__41

    @41.setter
    def 41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__41", None)
        self.__41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "42"):
                opp_val = getattr(old_value, "42", None)
                if opp_val == self:
                    setattr(old_value, "42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "42"):
                opp_val = getattr(value, "42", None)
                setattr(value, "42", self)

    @property
    def rtsc_Transition46(self):
        return self.__rtsc_Transition46

    @rtsc_Transition46.setter
    def rtsc_Transition46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition46", None)
        self.__rtsc_Transition46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_ClockConstraint"):
                    opp_val = getattr(item, "rtsc_ClockConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_ClockConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_ClockConstraint"):
                    opp_val = getattr(item, "rtsc_ClockConstraint", None)
                    
                    setattr(item, "rtsc_ClockConstraint", self)
                    

    @property
    def 28(self):
        return self.__28

    @28.setter
    def 28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__28", None)
        self.__28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "27"):
                opp_val = getattr(old_value, "27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "27"):
                opp_val = getattr(value, "27", None)
                if opp_val is None:
                    setattr(value, "27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 48(self):
        return self.__48

    @48.setter
    def 48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__48", None)
        self.__48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "49"):
                opp_val = getattr(old_value, "49", None)
                if opp_val == self:
                    setattr(old_value, "49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "49"):
                opp_val = getattr(value, "49", None)
                setattr(value, "49", self)

    @property
    def 31(self):
        return self.__31

    @31.setter
    def 31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__31", None)
        self.__31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "30"):
                opp_val = getattr(old_value, "30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "30"):
                opp_val = getattr(value, "30", None)
                if opp_val is None:
                    setattr(value, "30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Transition53(self):
        return self.__rtsc_Transition53

    @rtsc_Transition53.setter
    def rtsc_Transition53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition53", None)
        self.__rtsc_Transition53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Event54"):
                    opp_val = getattr(item, "rtsc_Event54", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Event54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Event54"):
                    opp_val = getattr(item, "rtsc_Event54", None)
                    
                    setattr(item, "rtsc_Event54", self)
                    

    def consumeMessages(self):
        # TODO: Implement consumeMessages method
        pass

    def fire(self) -> Vertex:
        # TODO: Implement fire method
        pass

    def canFire(self):
        # TODO: Implement canFire method
        pass

    def checkMessages(self):
        # TODO: Implement checkMessages method
        pass

    def guardsHold(self):
        # TODO: Implement guardsHold method
        pass

    def clocksHold(self):
        # TODO: Implement clocksHold method
        pass

class rtsc_Variable(NamedElement):

    def __init__(self, initialValue: str, runtimeValue: str, 14: "rtsc_Realtimestatechart" = None, 60: "rtsc_Realtimestatechart" = None, rtsc_Variable: "rtsc_Guard" = None, rtsc_Variable104: "rtsc_VariableAssignmentEvent" = None):
        self.initialValue = initialValue
        self.runtimeValue = runtimeValue
        self.14 = 14
        self.60 = 60
        self.rtsc_Variable = rtsc_Variable
        self.rtsc_Variable104 = rtsc_Variable104
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def runtimeValue(self) -> str:
        return self.__runtimeValue

    @runtimeValue.setter
    def runtimeValue(self, runtimeValue: str):
        self.__runtimeValue = runtimeValue

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
            if hasattr(old_value, "rtsc_Guard56"):
                opp_val = getattr(old_value, "rtsc_Guard56", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Guard56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Guard56"):
                opp_val = getattr(value, "rtsc_Guard56", None)
                setattr(value, "rtsc_Guard56", self)

    @property
    def 60(self):
        return self.__60

    @60.setter
    def 60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__60", None)
        self.__60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "61"):
                opp_val = getattr(old_value, "61", None)
                if opp_val == self:
                    setattr(old_value, "61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "61"):
                opp_val = getattr(value, "61", None)
                setattr(value, "61", self)

    @property
    def rtsc_Variable104(self):
        return self.__rtsc_Variable104

    @rtsc_Variable104.setter
    def rtsc_Variable104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__rtsc_Variable104", None)
        self.__rtsc_Variable104 = value
        
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

class rtsc_BehavioralElement(NamedElement):

    pass
class rtsc_Behavior(ABC):

    pass
from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rtsc_MessageTypeRepository:

    pass
class rtsc_System:

    pass
class rtsc_Message:

    pass
class Event:

    pass
class rtsc_VariableAssignmentEvent(Event):

    def __init__(self, value: str, rtsc_VariableAssignmentEvent: "rtsc_Variable" = None):
        self.value = value
        self.rtsc_VariableAssignmentEvent = rtsc_VariableAssignmentEvent
        
        pass
    @property
    def value(self):
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
            if hasattr(old_value, "rtsc_Variable76"):
                opp_val = getattr(old_value, "rtsc_Variable76", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Variable76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Variable76"):
                opp_val = getattr(value, "rtsc_Variable76", None)
                setattr(value, "rtsc_Variable76", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class rtsc_ClockResetEvent(Event):

    def __init__(self, rtsc_ClockResetEvent: "rtsc_Clock" = None):
        self.rtsc_ClockResetEvent = rtsc_ClockResetEvent
        
        pass
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
            if hasattr(old_value, "rtsc_Clock74"):
                opp_val = getattr(old_value, "rtsc_Clock74", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Clock74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Clock74"):
                opp_val = getattr(value, "rtsc_Clock74", None)
                setattr(value, "rtsc_Clock74", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class rtsc_MessageEvent(Event):

    def __init__(self, rtsc_MessageEvent: "rtsc_MessageType" = None):
        self.rtsc_MessageEvent = rtsc_MessageEvent
        
        pass
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
            if hasattr(old_value, "rtsc_MessageType72"):
                opp_val = getattr(old_value, "rtsc_MessageType72", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_MessageType72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_MessageType72"):
                opp_val = getattr(value, "rtsc_MessageType72", None)
                setattr(value, "rtsc_MessageType72", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class rtsc_Connector:

    pass
class rtsc_MessageBuffer:

    def __init__(self, MessageBuffer: "rtsc_Port" = None, incomingBuffer: "rtsc_Port" = None, rtsc_MessageBuffer: set["rtsc_MessageType"] = None, rtsc_MessageBuffer51: set["rtsc_Message"] = None):
        self.MessageBuffer = MessageBuffer
        self.incomingBuffer = incomingBuffer
        self.rtsc_MessageBuffer = rtsc_MessageBuffer if rtsc_MessageBuffer is not None else set()
        self.rtsc_MessageBuffer51 = rtsc_MessageBuffer51 if rtsc_MessageBuffer51 is not None else set()
        
        pass
    @property
    def incomingBuffer(self):
        return self.__incomingBuffer

    @incomingBuffer.setter
    def incomingBuffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageBuffer__incomingBuffer", None)
        self.__incomingBuffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Port"):
                opp_val = getattr(old_value, "Port", None)
                if opp_val == self:
                    setattr(old_value, "Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Port"):
                opp_val = getattr(value, "Port", None)
                setattr(value, "Port", self)

    @property
    def MessageBuffer(self):
        return self.__MessageBuffer

    @MessageBuffer.setter
    def MessageBuffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageBuffer__MessageBuffer", None)
        self.__MessageBuffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "port"):
                opp_val = getattr(old_value, "port", None)
                if opp_val == self:
                    setattr(old_value, "port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "port"):
                opp_val = getattr(value, "port", None)
                setattr(value, "port", self)

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
                if hasattr(item, "rtsc_MessageType49"):
                    opp_val = getattr(item, "rtsc_MessageType49", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_MessageType49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_MessageType49"):
                    opp_val = getattr(item, "rtsc_MessageType49", None)
                    
                    setattr(item, "rtsc_MessageType49", self)
                    

    @property
    def rtsc_MessageBuffer51(self):
        return self.__rtsc_MessageBuffer51

    @rtsc_MessageBuffer51.setter
    def rtsc_MessageBuffer51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_MessageBuffer__rtsc_MessageBuffer51", None)
        self.__rtsc_MessageBuffer51 = value if value is not None else set()
        
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
                    

    def getMessage(self, rtsc_type) :
        # TODO: Implement getMessage method
        pass

    def addMessage(self, rtsc_message):
        # TODO: Implement addMessage method
        pass

    def hasMessage(self, rtsc_type):
        # TODO: Implement hasMessage method
        pass

class BehavioralElement:

    pass
class rtsc_Port(BehavioralElement):

    pass
class rtsc_Event(ABC):

    def __init__(self, rtsc_Event35: "rtsc_Transition" = None, rtsc_Event: "rtsc_State" = None, rtsc_Event21: "rtsc_State" = None):
        self.rtsc_Event35 = rtsc_Event35
        self.rtsc_Event = rtsc_Event
        self.rtsc_Event21 = rtsc_Event21
        
        pass
    @property
    def rtsc_Event35(self):
        return self.__rtsc_Event35

    @rtsc_Event35.setter
    def rtsc_Event35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Event__rtsc_Event35", None)
        self.__rtsc_Event35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_Transition34"):
                opp_val = getattr(old_value, "rtsc_Transition34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Transition34"):
                opp_val = getattr(value, "rtsc_Transition34", None)
                if opp_val is None:
                    setattr(value, "rtsc_Transition34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Event21(self):
        return self.__rtsc_Event21

    @rtsc_Event21.setter
    def rtsc_Event21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Event__rtsc_Event21", None)
        self.__rtsc_Event21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_State20"):
                opp_val = getattr(old_value, "rtsc_State20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_State20"):
                opp_val = getattr(value, "rtsc_State20", None)
                if opp_val is None:
                    setattr(value, "rtsc_State20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "rtsc_State18"):
                opp_val = getattr(old_value, "rtsc_State18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_State18"):
                opp_val = getattr(value, "rtsc_State18", None)
                if opp_val is None:
                    setattr(value, "rtsc_State18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self):
        # TODO: Implement execute method
        pass

class rtsc_Vertex:

    def __init__(self, active: bool):
        self.active = active
        
        pass
    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


class rtsc_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class rtsc_ClockConstraint:

    def __init__(self, bound: int, rtsc_ClockConstraint: "rtsc_Transition" = None, rtsc_ClockConstraint39: "rtsc_Clock" = None):
        self.bound = bound
        self.rtsc_ClockConstraint = rtsc_ClockConstraint
        self.rtsc_ClockConstraint39 = rtsc_ClockConstraint39
        
        pass
    @property
    def bound(self):
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
            if hasattr(old_value, "rtsc_Transition28"):
                opp_val = getattr(old_value, "rtsc_Transition28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Transition28"):
                opp_val = getattr(value, "rtsc_Transition28", None)
                if opp_val is None:
                    setattr(value, "rtsc_Transition28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_ClockConstraint39(self):
        return self.__rtsc_ClockConstraint39

    @rtsc_ClockConstraint39.setter
    def rtsc_ClockConstraint39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_ClockConstraint__rtsc_ClockConstraint39", None)
        self.__rtsc_ClockConstraint39 = value
        
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

    def apply(self, rtsc_federation):
        # TODO: Implement apply method
        pass

    def evaluate(self, rtsc_checkFederation):
        # TODO: Implement evaluate method
        pass

class rtsc_Guard:

    def __init__(self, value: bool, rtsc_Guard: "rtsc_Transition" = None, rtsc_Guard37: "rtsc_Variable" = None):
        self.value = value
        self.rtsc_Guard = rtsc_Guard
        self.rtsc_Guard37 = rtsc_Guard37
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


    @property
    def rtsc_Guard37(self):
        return self.__rtsc_Guard37

    @rtsc_Guard37.setter
    def rtsc_Guard37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Guard__rtsc_Guard37", None)
        self.__rtsc_Guard37 = value
        
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

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class Behavior:

    pass
class NamedElement:

    pass
class rtsc_MessageType(NamedElement):

    pass
class rtsc_CoordinationProtocol(NamedElement):

    def __init__(self, rtsc_CoordinationProtocol: set["rtsc_Port"] = None, rtsc_CoordinationProtocol57: "rtsc_Connector" = None, rtsc_CoordinationProtocol65: "rtsc_System" = None):
        self.rtsc_CoordinationProtocol = rtsc_CoordinationProtocol if rtsc_CoordinationProtocol is not None else set()
        self.rtsc_CoordinationProtocol57 = rtsc_CoordinationProtocol57
        self.rtsc_CoordinationProtocol65 = rtsc_CoordinationProtocol65
        
        pass
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
                if hasattr(item, "rtsc_Port55"):
                    opp_val = getattr(item, "rtsc_Port55", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Port55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Port55"):
                    opp_val = getattr(item, "rtsc_Port55", None)
                    
                    setattr(item, "rtsc_Port55", self)
                    

    @property
    def rtsc_CoordinationProtocol65(self):
        return self.__rtsc_CoordinationProtocol65

    @rtsc_CoordinationProtocol65.setter
    def rtsc_CoordinationProtocol65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_CoordinationProtocol__rtsc_CoordinationProtocol65", None)
        self.__rtsc_CoordinationProtocol65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_System64"):
                opp_val = getattr(old_value, "rtsc_System64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_System64"):
                opp_val = getattr(value, "rtsc_System64", None)
                if opp_val is None:
                    setattr(value, "rtsc_System64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_CoordinationProtocol57(self):
        return self.__rtsc_CoordinationProtocol57

    @rtsc_CoordinationProtocol57.setter
    def rtsc_CoordinationProtocol57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_CoordinationProtocol__rtsc_CoordinationProtocol57", None)
        self.__rtsc_CoordinationProtocol57 = value
        
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

    def main(self):
        # TODO: Implement main method
        pass

    def initialize(self, rtsc_arguments):
        # TODO: Implement initialize method
        pass

class rtsc_Realtimestatechart(NamedElement, Behavior):

    def __init__(self, rounds: int, rtsc_Realtimestatechart: "rtsc_State" = None, statechart6: set["rtsc_Variable"] = None, statechart8: set["rtsc_Clock"] = None, rtsc_Realtimestatechart11: "rtsc_State" = None, Realtimestatechart: "rtsc_State" = None, Realtimestatechart30: "rtsc_Transition" = None, statechart: set["rtsc_Transition"] = None, owningRTSC: set["rtsc_State"] = None, Realtimestatechart43: "rtsc_Clock" = None, Realtimestatechart41: "rtsc_Variable" = None, rtsc_Realtimestatechart62: "rtsc_System" = None):
        self.rounds = rounds
        self.rtsc_Realtimestatechart = rtsc_Realtimestatechart
        self.statechart6 = statechart6 if statechart6 is not None else set()
        self.statechart8 = statechart8 if statechart8 is not None else set()
        self.rtsc_Realtimestatechart11 = rtsc_Realtimestatechart11
        self.Realtimestatechart = Realtimestatechart
        self.Realtimestatechart30 = Realtimestatechart30
        self.statechart = statechart if statechart is not None else set()
        self.owningRTSC = owningRTSC if owningRTSC is not None else set()
        self.Realtimestatechart43 = Realtimestatechart43
        self.Realtimestatechart41 = Realtimestatechart41
        self.rtsc_Realtimestatechart62 = rtsc_Realtimestatechart62
        
        pass
    @property
    def rounds(self):
        return self.__rounds

    @rounds.setter
    def rounds(self, rounds: int):
        self.__rounds = rounds


    @property
    def rtsc_Realtimestatechart11(self):
        return self.__rtsc_Realtimestatechart11

    @rtsc_Realtimestatechart11.setter
    def rtsc_Realtimestatechart11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__rtsc_Realtimestatechart11", None)
        self.__rtsc_Realtimestatechart11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rtsc_State10"):
                opp_val = getattr(old_value, "rtsc_State10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_State10"):
                opp_val = getattr(value, "rtsc_State10", None)
                if opp_val is None:
                    setattr(value, "rtsc_State10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statechart8(self):
        return self.__statechart8

    @statechart8.setter
    def statechart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__statechart8", None)
        self.__statechart8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clock"):
                    opp_val = getattr(item, "Clock", None)
                    
                    if opp_val == self:
                        setattr(item, "Clock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clock"):
                    opp_val = getattr(item, "Clock", None)
                    
                    setattr(item, "Clock", self)
                    

    @property
    def statechart(self):
        return self.__statechart

    @statechart.setter
    def statechart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__statechart", None)
        self.__statechart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def owningRTSC(self):
        return self.__owningRTSC

    @owningRTSC.setter
    def owningRTSC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__owningRTSC", None)
        self.__owningRTSC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

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
    def statechart6(self):
        return self.__statechart6

    @statechart6.setter
    def statechart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__statechart6", None)
        self.__statechart6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def rtsc_Realtimestatechart62(self):
        return self.__rtsc_Realtimestatechart62

    @rtsc_Realtimestatechart62.setter
    def rtsc_Realtimestatechart62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__rtsc_Realtimestatechart62", None)
        self.__rtsc_Realtimestatechart62 = value
        
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
    def Realtimestatechart(self):
        return self.__Realtimestatechart

    @Realtimestatechart.setter
    def Realtimestatechart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__Realtimestatechart", None)
        self.__Realtimestatechart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def Realtimestatechart43(self):
        return self.__Realtimestatechart43

    @Realtimestatechart43.setter
    def Realtimestatechart43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__Realtimestatechart43", None)
        self.__Realtimestatechart43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clocks"):
                opp_val = getattr(old_value, "clocks", None)
                if opp_val == self:
                    setattr(old_value, "clocks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clocks"):
                opp_val = getattr(value, "clocks", None)
                setattr(value, "clocks", self)

    @property
    def Realtimestatechart41(self):
        return self.__Realtimestatechart41

    @Realtimestatechart41.setter
    def Realtimestatechart41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__Realtimestatechart41", None)
        self.__Realtimestatechart41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variables"):
                opp_val = getattr(old_value, "variables", None)
                if opp_val == self:
                    setattr(old_value, "variables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variables"):
                opp_val = getattr(value, "variables", None)
                setattr(value, "variables", self)

    @property
    def Realtimestatechart30(self):
        return self.__Realtimestatechart30

    @Realtimestatechart30.setter
    def Realtimestatechart30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Realtimestatechart__Realtimestatechart30", None)
        self.__Realtimestatechart30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    def step(self):
        # TODO: Implement step method
        pass

    def initialize(self, rtsc_args):
        # TODO: Implement initialize method
        pass

    def main(self):
        # TODO: Implement main method
        pass

    def sequentialStep(self):
        # TODO: Implement sequentialStep method
        pass

class rtsc_BehavioralElement(NamedElement):

    pass
class rtsc_Behavior(ABC):

    pass
class Vertex:

    pass
class rtsc_Clock(NamedElement):

    def __init__(self, uClock: bool, Clock: "rtsc_Realtimestatechart" = None, clocks: "rtsc_Realtimestatechart" = None, rtsc_Clock: "rtsc_ClockConstraint" = None, rtsc_Clock74: "rtsc_ClockResetEvent" = None):
        self.uClock = uClock
        self.Clock = Clock
        self.clocks = clocks
        self.rtsc_Clock = rtsc_Clock
        self.rtsc_Clock74 = rtsc_Clock74
        
        pass
    @property
    def uClock(self):
        return self.__uClock

    @uClock.setter
    def uClock(self, uClock: bool):
        self.__uClock = uClock


    @property
    def rtsc_Clock74(self):
        return self.__rtsc_Clock74

    @rtsc_Clock74.setter
    def rtsc_Clock74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Clock__rtsc_Clock74", None)
        self.__rtsc_Clock74 = value
        
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

    @property
    def clocks(self):
        return self.__clocks

    @clocks.setter
    def clocks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Clock__clocks", None)
        self.__clocks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Realtimestatechart43"):
                opp_val = getattr(old_value, "Realtimestatechart43", None)
                if opp_val == self:
                    setattr(old_value, "Realtimestatechart43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Realtimestatechart43"):
                opp_val = getattr(value, "Realtimestatechart43", None)
                setattr(value, "Realtimestatechart43", self)

    @property
    def Clock(self):
        return self.__Clock

    @Clock.setter
    def Clock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Clock__Clock", None)
        self.__Clock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart8"):
                opp_val = getattr(old_value, "statechart8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart8"):
                opp_val = getattr(value, "statechart8", None)
                if opp_val is None:
                    setattr(value, "statechart8", set([self]))
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
            if hasattr(old_value, "rtsc_ClockConstraint39"):
                opp_val = getattr(old_value, "rtsc_ClockConstraint39", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_ClockConstraint39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_ClockConstraint39"):
                opp_val = getattr(value, "rtsc_ClockConstraint39", None)
                setattr(value, "rtsc_ClockConstraint39", self)

    def reset(self):
        # TODO: Implement reset method
        pass

    def printValue(self):
        # TODO: Implement printValue method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

class rtsc_Variable(NamedElement):

    def __init__(self, initialValue: str, runtimeValue: str, Variable: "rtsc_Realtimestatechart" = None, rtsc_Variable: "rtsc_Guard" = None, variables: "rtsc_Realtimestatechart" = None, rtsc_Variable76: "rtsc_VariableAssignmentEvent" = None):
        self.initialValue = initialValue
        self.runtimeValue = runtimeValue
        self.Variable = Variable
        self.rtsc_Variable = rtsc_Variable
        self.variables = variables
        self.rtsc_Variable76 = rtsc_Variable76
        
        pass
    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue


    @property
    def runtimeValue(self):
        return self.__runtimeValue

    @runtimeValue.setter
    def runtimeValue(self, runtimeValue: str):
        self.__runtimeValue = runtimeValue


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
            if hasattr(old_value, "rtsc_Guard37"):
                opp_val = getattr(old_value, "rtsc_Guard37", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Guard37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Guard37"):
                opp_val = getattr(value, "rtsc_Guard37", None)
                setattr(value, "rtsc_Guard37", self)

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__variables", None)
        self.__variables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Realtimestatechart41"):
                opp_val = getattr(old_value, "Realtimestatechart41", None)
                if opp_val == self:
                    setattr(old_value, "Realtimestatechart41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Realtimestatechart41"):
                opp_val = getattr(value, "Realtimestatechart41", None)
                setattr(value, "Realtimestatechart41", self)

    @property
    def rtsc_Variable76(self):
        return self.__rtsc_Variable76

    @rtsc_Variable76.setter
    def rtsc_Variable76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__rtsc_Variable76", None)
        self.__rtsc_Variable76 = value
        
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

    @property
    def Variable(self):
        return self.__Variable

    @Variable.setter
    def Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__Variable", None)
        self.__Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart6"):
                opp_val = getattr(old_value, "statechart6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart6"):
                opp_val = getattr(value, "statechart6", None)
                if opp_val is None:
                    setattr(value, "statechart6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rtsc_State(NamedElement, Vertex):

    def __init__(self, initial: bool, final: bool, rtsc_State: "rtsc_Realtimestatechart" = None, rtsc_State10: set["rtsc_Realtimestatechart"] = None, states: "rtsc_Realtimestatechart" = None, target: set["rtsc_Transition"] = None, State25: "rtsc_Transition" = None, State: "rtsc_Realtimestatechart" = None, source: set["rtsc_Transition"] = None, rtsc_State18: set["rtsc_Event"] = None, rtsc_State20: set["rtsc_Event"] = None, State23: "rtsc_Transition" = None):
        self.initial = initial
        self.final = final
        self.rtsc_State = rtsc_State
        self.rtsc_State10 = rtsc_State10 if rtsc_State10 is not None else set()
        self.states = states
        self.target = target if target is not None else set()
        self.State25 = State25
        self.State = State
        self.source = source if source is not None else set()
        self.rtsc_State18 = rtsc_State18 if rtsc_State18 is not None else set()
        self.rtsc_State20 = rtsc_State20 if rtsc_State20 is not None else set()
        self.State23 = State23
        
        pass
    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def initial(self):
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial


    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningRTSC"):
                opp_val = getattr(old_value, "owningRTSC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningRTSC"):
                opp_val = getattr(value, "owningRTSC", None)
                if opp_val is None:
                    setattr(value, "owningRTSC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition14"):
                    opp_val = getattr(item, "Transition14", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition14"):
                    opp_val = getattr(item, "Transition14", None)
                    
                    setattr(item, "Transition14", self)
                    

    @property
    def State23(self):
        return self.__State23

    @State23.setter
    def State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__State23", None)
        self.__State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition16"):
                    opp_val = getattr(item, "Transition16", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition16"):
                    opp_val = getattr(item, "Transition16", None)
                    
                    setattr(item, "Transition16", self)
                    

    @property
    def State25(self):
        return self.__State25

    @State25.setter
    def State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__State25", None)
        self.__State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

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
    def rtsc_State20(self):
        return self.__rtsc_State20

    @rtsc_State20.setter
    def rtsc_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State20", None)
        self.__rtsc_State20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Event21"):
                    opp_val = getattr(item, "rtsc_Event21", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Event21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Event21"):
                    opp_val = getattr(item, "rtsc_Event21", None)
                    
                    setattr(item, "rtsc_Event21", self)
                    

    @property
    def rtsc_State18(self):
        return self.__rtsc_State18

    @rtsc_State18.setter
    def rtsc_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State18", None)
        self.__rtsc_State18 = value if value is not None else set()
        
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
    def rtsc_State10(self):
        return self.__rtsc_State10

    @rtsc_State10.setter
    def rtsc_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__rtsc_State10", None)
        self.__rtsc_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Realtimestatechart11"):
                    opp_val = getattr(item, "rtsc_Realtimestatechart11", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Realtimestatechart11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Realtimestatechart11"):
                    opp_val = getattr(item, "rtsc_Realtimestatechart11", None)
                    
                    setattr(item, "rtsc_Realtimestatechart11", self)
                    

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Realtimestatechart"):
                opp_val = getattr(old_value, "Realtimestatechart", None)
                if opp_val == self:
                    setattr(old_value, "Realtimestatechart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Realtimestatechart"):
                opp_val = getattr(value, "Realtimestatechart", None)
                setattr(value, "Realtimestatechart", self)

    def exit(self):
        # TODO: Implement exit method
        pass

    def entry(self):
        # TODO: Implement entry method
        pass

class rtsc_Transition(NamedElement):

    def __init__(self, hitCount: int, Transition14: "rtsc_State" = None, incomingTransitions: "rtsc_State" = None, rtsc_Transition: set["rtsc_Guard"] = None, rtsc_Transition28: set["rtsc_ClockConstraint"] = None, transitions: "rtsc_Realtimestatechart" = None, Transition: "rtsc_Realtimestatechart" = None, rtsc_Transition32: set["rtsc_MessageType"] = None, rtsc_Transition34: set["rtsc_Event"] = None, Transition16: "rtsc_State" = None, outgoingTransitions: "rtsc_State" = None):
        self.hitCount = hitCount
        self.Transition14 = Transition14
        self.incomingTransitions = incomingTransitions
        self.rtsc_Transition = rtsc_Transition if rtsc_Transition is not None else set()
        self.rtsc_Transition28 = rtsc_Transition28 if rtsc_Transition28 is not None else set()
        self.transitions = transitions
        self.Transition = Transition
        self.rtsc_Transition32 = rtsc_Transition32 if rtsc_Transition32 is not None else set()
        self.rtsc_Transition34 = rtsc_Transition34 if rtsc_Transition34 is not None else set()
        self.Transition16 = Transition16
        self.outgoingTransitions = outgoingTransitions
        
        pass
    @property
    def hitCount(self):
        return self.__hitCount

    @hitCount.setter
    def hitCount(self, hitCount: int):
        self.__hitCount = hitCount


    @property
    def rtsc_Transition(self):
        return self.__rtsc_Transition

    @rtsc_Transition.setter
    def rtsc_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition", None)
        self.__rtsc_Transition = value if value is not None else set()
        
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
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State23"):
                opp_val = getattr(old_value, "State23", None)
                if opp_val == self:
                    setattr(old_value, "State23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State23"):
                opp_val = getattr(value, "State23", None)
                setattr(value, "State23", self)

    @property
    def Transition14(self):
        return self.__Transition14

    @Transition14.setter
    def Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__Transition14", None)
        self.__Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition16(self):
        return self.__Transition16

    @Transition16.setter
    def Transition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__Transition16", None)
        self.__Transition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Transition32(self):
        return self.__rtsc_Transition32

    @rtsc_Transition32.setter
    def rtsc_Transition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition32", None)
        self.__rtsc_Transition32 = value if value is not None else set()
        
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
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Realtimestatechart30"):
                opp_val = getattr(old_value, "Realtimestatechart30", None)
                if opp_val == self:
                    setattr(old_value, "Realtimestatechart30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Realtimestatechart30"):
                opp_val = getattr(value, "Realtimestatechart30", None)
                setattr(value, "Realtimestatechart30", self)

    @property
    def rtsc_Transition34(self):
        return self.__rtsc_Transition34

    @rtsc_Transition34.setter
    def rtsc_Transition34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition34", None)
        self.__rtsc_Transition34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rtsc_Event35"):
                    opp_val = getattr(item, "rtsc_Event35", None)
                    
                    if opp_val == self:
                        setattr(item, "rtsc_Event35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rtsc_Event35"):
                    opp_val = getattr(item, "rtsc_Event35", None)
                    
                    setattr(item, "rtsc_Event35", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart"):
                opp_val = getattr(old_value, "statechart", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart"):
                opp_val = getattr(value, "statechart", None)
                if opp_val is None:
                    setattr(value, "statechart", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rtsc_Transition28(self):
        return self.__rtsc_Transition28

    @rtsc_Transition28.setter
    def rtsc_Transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__rtsc_Transition28", None)
        self.__rtsc_Transition28 = value if value is not None else set()
        
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
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State25"):
                opp_val = getattr(old_value, "State25", None)
                if opp_val == self:
                    setattr(old_value, "State25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State25"):
                opp_val = getattr(value, "State25", None)
                setattr(value, "State25", self)

    def canFire(self):
        # TODO: Implement canFire method
        pass

    def fire(self) :
        # TODO: Implement fire method
        pass

    def clocksHold(self):
        # TODO: Implement clocksHold method
        pass

    def consumeMessages(self):
        # TODO: Implement consumeMessages method
        pass

    def guardsHold(self):
        # TODO: Implement guardsHold method
        pass

    def checkMessages(self):
        # TODO: Implement checkMessages method
        pass

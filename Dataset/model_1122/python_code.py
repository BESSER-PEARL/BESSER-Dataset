from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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

class rtsc_Guard:

    def __init__(self, value: str, rtsc_Guard: "rtsc_Transition" = None, rtsc_Guard37: "rtsc_Variable" = None):
        self.value = value
        self.rtsc_Guard = rtsc_Guard
        self.rtsc_Guard37 = rtsc_Guard37
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
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

class rtsc_Event(ABC):

    pass
class Vertex:

    pass
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


class rtsc_Behavior(ABC):

    pass
class Behavior:

    pass
class NamedElement:

    pass
class rtsc_Clock(NamedElement):

    pass
class rtsc_MessageType(NamedElement):

    pass
class rtsc_State(NamedElement, Vertex):

    def __init__(self, initial: bool, final: bool, State: "rtsc_Realtimestatechart" = None, rtsc_State: "rtsc_Realtimestatechart" = None, rtsc_State10: set["rtsc_Realtimestatechart"] = None, states: "rtsc_Realtimestatechart" = None, target: set["rtsc_Transition"] = None, source: set["rtsc_Transition"] = None, rtsc_State18: set["rtsc_Event"] = None, rtsc_State20: set["rtsc_Event"] = None, State23: "rtsc_Transition" = None, State25: "rtsc_Transition" = None):
        self.initial = initial
        self.final = final
        self.State = State
        self.rtsc_State = rtsc_State
        self.rtsc_State10 = rtsc_State10 if rtsc_State10 is not None else set()
        self.states = states
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.rtsc_State18 = rtsc_State18 if rtsc_State18 is not None else set()
        self.rtsc_State20 = rtsc_State20 if rtsc_State20 is not None else set()
        self.State23 = State23
        self.State25 = State25
        
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

class rtsc_Variable(NamedElement):

    def __init__(self, initialValue: str, Variable: "rtsc_Realtimestatechart" = None, rtsc_Variable: "rtsc_Guard" = None, variables: "rtsc_Realtimestatechart" = None, rtsc_Variable73: "rtsc_VariableAssignmentEvent" = None):
        self.initialValue = initialValue
        self.Variable = Variable
        self.rtsc_Variable = rtsc_Variable
        self.variables = variables
        self.rtsc_Variable73 = rtsc_Variable73
        
        pass
    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue


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
    def rtsc_Variable73(self):
        return self.__rtsc_Variable73

    @rtsc_Variable73.setter
    def rtsc_Variable73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rtsc_Variable__rtsc_Variable73", None)
        self.__rtsc_Variable73 = value
        
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

class rtsc_BehavioralElement(NamedElement):

    pass
class rtsc_Transition(NamedElement):

    pass
class rtsc_Realtimestatechart(NamedElement, Behavior):

    pass
class Event:

    pass
class rtsc_ClockResetEvent(Event):

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
            if hasattr(old_value, "rtsc_Variable73"):
                opp_val = getattr(old_value, "rtsc_Variable73", None)
                if opp_val == self:
                    setattr(old_value, "rtsc_Variable73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rtsc_Variable73"):
                opp_val = getattr(value, "rtsc_Variable73", None)
                setattr(value, "rtsc_Variable73", self)

class rtsc_MessageEvent(Event):

    pass
class rtsc_MessageTypeRepository:

    pass
class rtsc_CoordinationProtocol(NamedElement):

    pass
class rtsc_Connector:

    pass
class rtsc_MessageBuffer:

    pass
class BehavioralElement:

    pass
class rtsc_Port(BehavioralElement):

    pass
class rtsc_Vertex(ABC):

    pass
class rtsc_System:

    pass
class rtsc_Message:

    pass
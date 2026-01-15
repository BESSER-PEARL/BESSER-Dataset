from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Gate:

    pass
class fault_tree_XOR(Gate):

    pass
class fault_tree_AND(Gate):

    pass
class fault_tree_Inhibit(Gate):

    pass
class fault_tree_PriorAND(Gate):

    pass
class fault_tree_OR(Gate):

    pass
class IDBase:

    pass
class fault_tree_FailureType(IDBase):

    def __init__(self, name: str, type: set["fault_tree_FailureInstance"] = None, failure_type: "fault_tree_FaultTree" = None, FailureType: "fault_tree_FailureInstance" = None, FailureType61: "fault_tree_FaultTree" = None):
        self.name = name
        self.type = type if type is not None else set()
        self.failure_type = failure_type
        self.FailureType = FailureType
        self.FailureType61 = FailureType61
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureType__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FailureInstance23"):
                    opp_val = getattr(item, "FailureInstance23", None)
                    
                    if opp_val == self:
                        setattr(item, "FailureInstance23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FailureInstance23"):
                    opp_val = getattr(item, "FailureInstance23", None)
                    
                    setattr(item, "FailureInstance23", self)
                    

    @property
    def FailureType(self):
        return self.__FailureType

    @FailureType.setter
    def FailureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureType__FailureType", None)
        self.__FailureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instance"):
                opp_val = getattr(old_value, "instance", None)
                if opp_val == self:
                    setattr(old_value, "instance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instance"):
                opp_val = getattr(value, "instance", None)
                setattr(value, "instance", self)

    @property
    def failure_type(self):
        return self.__failure_type

    @failure_type.setter
    def failure_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureType__failure_type", None)
        self.__failure_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree25"):
                opp_val = getattr(old_value, "FaultTree25", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree25"):
                opp_val = getattr(value, "FaultTree25", None)
                setattr(value, "FaultTree25", self)

    @property
    def FailureType61(self):
        return self.__FailureType61

    @FailureType61.setter
    def FailureType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureType__FailureType61", None)
        self.__FailureType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root60"):
                opp_val = getattr(old_value, "root60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root60"):
                opp_val = getattr(value, "root60", None)
                if opp_val is None:
                    setattr(value, "root60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fault_tree_FaultTree(IDBase):

    pass
class fault_tree_ErrorType(IDBase):

    def __init__(self, name: str, error_type: "fault_tree_FaultTree" = None, ErrorType: "fault_tree_ErrorInstance" = None, type39: set["fault_tree_ErrorInstance"] = None, ErrorType67: "fault_tree_FaultTree" = None):
        self.name = name
        self.error_type = error_type
        self.ErrorType = ErrorType
        self.type39 = type39 if type39 is not None else set()
        self.ErrorType67 = ErrorType67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ErrorType67(self):
        return self.__ErrorType67

    @ErrorType67.setter
    def ErrorType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorType__ErrorType67", None)
        self.__ErrorType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root66"):
                opp_val = getattr(old_value, "root66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root66"):
                opp_val = getattr(value, "root66", None)
                if opp_val is None:
                    setattr(value, "root66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def type39(self):
        return self.__type39

    @type39.setter
    def type39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorType__type39", None)
        self.__type39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ErrorInstance40"):
                    opp_val = getattr(item, "ErrorInstance40", None)
                    
                    if opp_val == self:
                        setattr(item, "ErrorInstance40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ErrorInstance40"):
                    opp_val = getattr(item, "ErrorInstance40", None)
                    
                    setattr(item, "ErrorInstance40", self)
                    

    @property
    def ErrorType(self):
        return self.__ErrorType

    @ErrorType.setter
    def ErrorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorType__ErrorType", None)
        self.__ErrorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error46"):
                opp_val = getattr(old_value, "error46", None)
                if opp_val == self:
                    setattr(old_value, "error46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error46"):
                opp_val = getattr(value, "error46", None)
                setattr(value, "error46", self)

    @property
    def error_type(self):
        return self.__error_type

    @error_type.setter
    def error_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorType__error_type", None)
        self.__error_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree42"):
                opp_val = getattr(old_value, "FaultTree42", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree42"):
                opp_val = getattr(value, "FaultTree42", None)
                setattr(value, "FaultTree42", self)

class fault_tree_Event(IDBase):

    def __init__(self, description: str, name: str, fault_tree_Event: "fault_tree_IntermediateEvent" = None, fault_tree_Event21: "fault_tree_IntermediateEvent" = None, Event: "fault_tree_Gate" = None, Event8: "fault_tree_Gate" = None, outputEvent: "fault_tree_Gate" = None, inputEvents: "fault_tree_Gate" = None, event: "fault_tree_FaultTree" = None, Event55: "fault_tree_FaultTree" = None):
        self.description = description
        self.name = name
        self.fault_tree_Event = fault_tree_Event
        self.fault_tree_Event21 = fault_tree_Event21
        self.Event = Event
        self.Event8 = Event8
        self.outputEvent = outputEvent
        self.inputEvents = inputEvents
        self.event = event
        self.Event55 = Event55
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fault_tree_Event21(self):
        return self.__fault_tree_Event21

    @fault_tree_Event21.setter
    def fault_tree_Event21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__fault_tree_Event21", None)
        self.__fault_tree_Event21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fault_tree_IntermediateEvent20"):
                opp_val = getattr(old_value, "fault_tree_IntermediateEvent20", None)
                if opp_val == self:
                    setattr(old_value, "fault_tree_IntermediateEvent20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fault_tree_IntermediateEvent20"):
                opp_val = getattr(value, "fault_tree_IntermediateEvent20", None)
                setattr(value, "fault_tree_IntermediateEvent20", self)

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputGate"):
                opp_val = getattr(old_value, "outputGate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputGate"):
                opp_val = getattr(value, "outputGate", None)
                if opp_val is None:
                    setattr(value, "outputGate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fault_tree_Event(self):
        return self.__fault_tree_Event

    @fault_tree_Event.setter
    def fault_tree_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__fault_tree_Event", None)
        self.__fault_tree_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fault_tree_IntermediateEvent18"):
                opp_val = getattr(old_value, "fault_tree_IntermediateEvent18", None)
                if opp_val == self:
                    setattr(old_value, "fault_tree_IntermediateEvent18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fault_tree_IntermediateEvent18"):
                opp_val = getattr(value, "fault_tree_IntermediateEvent18", None)
                setattr(value, "fault_tree_IntermediateEvent18", self)

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__event", None)
        self.__event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree14"):
                opp_val = getattr(old_value, "FaultTree14", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree14"):
                opp_val = getattr(value, "FaultTree14", None)
                setattr(value, "FaultTree14", self)

    @property
    def Event55(self):
        return self.__Event55

    @Event55.setter
    def Event55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__Event55", None)
        self.__Event55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root54"):
                opp_val = getattr(old_value, "root54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root54"):
                opp_val = getattr(value, "root54", None)
                if opp_val is None:
                    setattr(value, "root54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outputEvent(self):
        return self.__outputEvent

    @outputEvent.setter
    def outputEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__outputEvent", None)
        self.__outputEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Gate"):
                opp_val = getattr(old_value, "Gate", None)
                if opp_val == self:
                    setattr(old_value, "Gate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Gate"):
                opp_val = getattr(value, "Gate", None)
                setattr(value, "Gate", self)

    @property
    def Event8(self):
        return self.__Event8

    @Event8.setter
    def Event8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__Event8", None)
        self.__Event8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputGate"):
                opp_val = getattr(old_value, "inputGate", None)
                if opp_val == self:
                    setattr(old_value, "inputGate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputGate"):
                opp_val = getattr(value, "inputGate", None)
                setattr(value, "inputGate", self)

    @property
    def inputEvents(self):
        return self.__inputEvents

    @inputEvents.setter
    def inputEvents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_Event__inputEvents", None)
        self.__inputEvents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Gate12"):
                opp_val = getattr(old_value, "Gate12", None)
                if opp_val == self:
                    setattr(old_value, "Gate12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Gate12"):
                opp_val = getattr(value, "Gate12", None)
                setattr(value, "Gate12", self)

class fault_tree_ErrorInstance(IDBase):

    def __init__(self, name: str, instance44: "fault_tree_BasicEvent" = None, error46: "fault_tree_ErrorType" = None, error_instance: "fault_tree_FaultTree" = None, fault_tree_ErrorInstance: "fault_tree_FailureInstance" = None, ErrorInstance: "fault_tree_BasicEvent" = None, ErrorInstance40: "fault_tree_ErrorType" = None, ErrorInstance64: "fault_tree_FaultTree" = None):
        self.name = name
        self.instance44 = instance44
        self.error46 = error46
        self.error_instance = error_instance
        self.fault_tree_ErrorInstance = fault_tree_ErrorInstance
        self.ErrorInstance = ErrorInstance
        self.ErrorInstance40 = ErrorInstance40
        self.ErrorInstance64 = ErrorInstance64
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ErrorInstance40(self):
        return self.__ErrorInstance40

    @ErrorInstance40.setter
    def ErrorInstance40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorInstance__ErrorInstance40", None)
        self.__ErrorInstance40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type39"):
                opp_val = getattr(old_value, "type39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type39"):
                opp_val = getattr(value, "type39", None)
                if opp_val is None:
                    setattr(value, "type39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fault_tree_ErrorInstance(self):
        return self.__fault_tree_ErrorInstance

    @fault_tree_ErrorInstance.setter
    def fault_tree_ErrorInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorInstance__fault_tree_ErrorInstance", None)
        self.__fault_tree_ErrorInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fault_tree_FailureInstance32"):
                opp_val = getattr(old_value, "fault_tree_FailureInstance32", None)
                if opp_val == self:
                    setattr(old_value, "fault_tree_FailureInstance32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fault_tree_FailureInstance32"):
                opp_val = getattr(value, "fault_tree_FailureInstance32", None)
                setattr(value, "fault_tree_FailureInstance32", self)

    @property
    def ErrorInstance64(self):
        return self.__ErrorInstance64

    @ErrorInstance64.setter
    def ErrorInstance64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorInstance__ErrorInstance64", None)
        self.__ErrorInstance64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root63"):
                opp_val = getattr(old_value, "root63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root63"):
                opp_val = getattr(value, "root63", None)
                if opp_val is None:
                    setattr(value, "root63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def error46(self):
        return self.__error46

    @error46.setter
    def error46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorInstance__error46", None)
        self.__error46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ErrorType"):
                opp_val = getattr(old_value, "ErrorType", None)
                if opp_val == self:
                    setattr(old_value, "ErrorType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ErrorType"):
                opp_val = getattr(value, "ErrorType", None)
                setattr(value, "ErrorType", self)

    @property
    def ErrorInstance(self):
        return self.__ErrorInstance

    @ErrorInstance.setter
    def ErrorInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorInstance__ErrorInstance", None)
        self.__ErrorInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error"):
                opp_val = getattr(old_value, "error", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error"):
                opp_val = getattr(value, "error", None)
                if opp_val is None:
                    setattr(value, "error", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def error_instance(self):
        return self.__error_instance

    @error_instance.setter
    def error_instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorInstance__error_instance", None)
        self.__error_instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree48"):
                opp_val = getattr(old_value, "FaultTree48", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree48"):
                opp_val = getattr(value, "FaultTree48", None)
                setattr(value, "FaultTree48", self)

    @property
    def instance44(self):
        return self.__instance44

    @instance44.setter
    def instance44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_ErrorInstance__instance44", None)
        self.__instance44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicEvent"):
                opp_val = getattr(old_value, "BasicEvent", None)
                if opp_val == self:
                    setattr(old_value, "BasicEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicEvent"):
                opp_val = getattr(value, "BasicEvent", None)
                setattr(value, "BasicEvent", self)

class fault_tree_FailureInstance(IDBase):

    def __init__(self, name: str, FailureInstance: "fault_tree_IntermediateEvent" = None, FailureInstance23: "fault_tree_FailureType" = None, instance: "fault_tree_FailureType" = None, failure_instance: "fault_tree_FaultTree" = None, fault_tree_FailureInstance: "fault_tree_FailureInstance" = None, fault_tree_FailureInstance29: "fault_tree_FailureInstance" = None, fault_tree_FailureInstance32: "fault_tree_ErrorInstance" = None, instance34: "fault_tree_IntermediateEvent" = None, FailureInstance58: "fault_tree_FaultTree" = None):
        self.name = name
        self.FailureInstance = FailureInstance
        self.FailureInstance23 = FailureInstance23
        self.instance = instance
        self.failure_instance = failure_instance
        self.fault_tree_FailureInstance = fault_tree_FailureInstance
        self.fault_tree_FailureInstance29 = fault_tree_FailureInstance29
        self.fault_tree_FailureInstance32 = fault_tree_FailureInstance32
        self.instance34 = instance34
        self.FailureInstance58 = FailureInstance58
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def instance34(self):
        return self.__instance34

    @instance34.setter
    def instance34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__instance34", None)
        self.__instance34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntermediateEvent"):
                opp_val = getattr(old_value, "IntermediateEvent", None)
                if opp_val == self:
                    setattr(old_value, "IntermediateEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntermediateEvent"):
                opp_val = getattr(value, "IntermediateEvent", None)
                setattr(value, "IntermediateEvent", self)

    @property
    def FailureInstance(self):
        return self.__FailureInstance

    @FailureInstance.setter
    def FailureInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__FailureInstance", None)
        self.__FailureInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event16"):
                opp_val = getattr(old_value, "event16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event16"):
                opp_val = getattr(value, "event16", None)
                if opp_val is None:
                    setattr(value, "event16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fault_tree_FailureInstance32(self):
        return self.__fault_tree_FailureInstance32

    @fault_tree_FailureInstance32.setter
    def fault_tree_FailureInstance32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__fault_tree_FailureInstance32", None)
        self.__fault_tree_FailureInstance32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fault_tree_ErrorInstance"):
                opp_val = getattr(old_value, "fault_tree_ErrorInstance", None)
                if opp_val == self:
                    setattr(old_value, "fault_tree_ErrorInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fault_tree_ErrorInstance"):
                opp_val = getattr(value, "fault_tree_ErrorInstance", None)
                setattr(value, "fault_tree_ErrorInstance", self)

    @property
    def failure_instance(self):
        return self.__failure_instance

    @failure_instance.setter
    def failure_instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__failure_instance", None)
        self.__failure_instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree28"):
                opp_val = getattr(old_value, "FaultTree28", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree28"):
                opp_val = getattr(value, "FaultTree28", None)
                setattr(value, "FaultTree28", self)

    @property
    def fault_tree_FailureInstance29(self):
        return self.__fault_tree_FailureInstance29

    @fault_tree_FailureInstance29.setter
    def fault_tree_FailureInstance29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__fault_tree_FailureInstance29", None)
        self.__fault_tree_FailureInstance29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fault_tree_FailureInstance"):
                opp_val = getattr(old_value, "fault_tree_FailureInstance", None)
                if opp_val == self:
                    setattr(old_value, "fault_tree_FailureInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fault_tree_FailureInstance"):
                opp_val = getattr(value, "fault_tree_FailureInstance", None)
                setattr(value, "fault_tree_FailureInstance", self)

    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__instance", None)
        self.__instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FailureType"):
                opp_val = getattr(old_value, "FailureType", None)
                if opp_val == self:
                    setattr(old_value, "FailureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FailureType"):
                opp_val = getattr(value, "FailureType", None)
                setattr(value, "FailureType", self)

    @property
    def FailureInstance58(self):
        return self.__FailureInstance58

    @FailureInstance58.setter
    def FailureInstance58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__FailureInstance58", None)
        self.__FailureInstance58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root57"):
                opp_val = getattr(old_value, "root57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root57"):
                opp_val = getattr(value, "root57", None)
                if opp_val is None:
                    setattr(value, "root57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fault_tree_FailureInstance(self):
        return self.__fault_tree_FailureInstance

    @fault_tree_FailureInstance.setter
    def fault_tree_FailureInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__fault_tree_FailureInstance", None)
        self.__fault_tree_FailureInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fault_tree_FailureInstance29"):
                opp_val = getattr(old_value, "fault_tree_FailureInstance29", None)
                if opp_val == self:
                    setattr(old_value, "fault_tree_FailureInstance29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fault_tree_FailureInstance29"):
                opp_val = getattr(value, "fault_tree_FailureInstance29", None)
                setattr(value, "fault_tree_FailureInstance29", self)

    @property
    def FailureInstance23(self):
        return self.__FailureInstance23

    @FailureInstance23.setter
    def FailureInstance23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_FailureInstance__FailureInstance23", None)
        self.__FailureInstance23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fault_tree_Gate(IDBase):

    pass
class Event:

    pass
class fault_tree_IntermediateEvent(Event):

    pass
class fault_tree_UndevelopedEvent(Event):

    pass
class fault_tree_BasicEvent(Event):

    def __init__(self, probability: float, BasicEvent: "fault_tree_ErrorInstance" = None, error: set["fault_tree_ErrorInstance"] = None, fault_tree_BasicEvent: "fault_tree_IntermediateEvent" = None):
        self.probability = probability
        self.BasicEvent = BasicEvent
        self.error = error if error is not None else set()
        self.fault_tree_BasicEvent = fault_tree_BasicEvent
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_BasicEvent__error", None)
        self.__error = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ErrorInstance"):
                    opp_val = getattr(item, "ErrorInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "ErrorInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ErrorInstance"):
                    opp_val = getattr(item, "ErrorInstance", None)
                    
                    setattr(item, "ErrorInstance", self)
                    

    @property
    def BasicEvent(self):
        return self.__BasicEvent

    @BasicEvent.setter
    def BasicEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_BasicEvent__BasicEvent", None)
        self.__BasicEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instance44"):
                opp_val = getattr(old_value, "instance44", None)
                if opp_val == self:
                    setattr(old_value, "instance44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instance44"):
                opp_val = getattr(value, "instance44", None)
                setattr(value, "instance44", self)

    @property
    def fault_tree_BasicEvent(self):
        return self.__fault_tree_BasicEvent

    @fault_tree_BasicEvent.setter
    def fault_tree_BasicEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fault_tree_BasicEvent__fault_tree_BasicEvent", None)
        self.__fault_tree_BasicEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fault_tree_IntermediateEvent37"):
                opp_val = getattr(old_value, "fault_tree_IntermediateEvent37", None)
                if opp_val == self:
                    setattr(old_value, "fault_tree_IntermediateEvent37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fault_tree_IntermediateEvent37"):
                opp_val = getattr(value, "fault_tree_IntermediateEvent37", None)
                setattr(value, "fault_tree_IntermediateEvent37", self)

class fault_tree_Hazard(Event):

    pass
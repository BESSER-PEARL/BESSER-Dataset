from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimaryEventType(Enum):
    BASIC = "BASIC"
    UNDEVELOPED = "UNDEVELOPED"
    EXTERNAL = "EXTERNAL"
class GateType(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
    PAND = "PAND"
    INHIBIT = "INHIBIT"


############################################
# Definition of Classes
############################################

class Transfer:

    pass
class Event:

    pass
class faultTree_Transfer(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class faultTree_TransferIn(Transfer):

    pass
class faultTree_TransferOut(Transfer):

    pass
class faultTree_ConditioningEvent(Event):

    def __init__(self, condition: str, faultTree_ConditioningEvent: "faultTree_FaultTree" = None):
        self.condition = condition
        self.faultTree_ConditioningEvent = faultTree_ConditioningEvent
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def faultTree_ConditioningEvent(self):
        return self.__faultTree_ConditioningEvent

    @faultTree_ConditioningEvent.setter
    def faultTree_ConditioningEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_ConditioningEvent__faultTree_ConditioningEvent", None)
        self.__faultTree_ConditioningEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_FaultTree7"):
                opp_val = getattr(old_value, "faultTree_FaultTree7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_FaultTree7"):
                opp_val = getattr(value, "faultTree_FaultTree7", None)
                if opp_val is None:
                    setattr(value, "faultTree_FaultTree7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class faultTree_PrimaryEvent(Event):

    def __init__(self, type: str, probability: float, faultTree_PrimaryEvent: "faultTree_FaultTree" = None):
        self.type = type
        self.probability = probability
        self.faultTree_PrimaryEvent = faultTree_PrimaryEvent
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def faultTree_PrimaryEvent(self):
        return self.__faultTree_PrimaryEvent

    @faultTree_PrimaryEvent.setter
    def faultTree_PrimaryEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_PrimaryEvent__faultTree_PrimaryEvent", None)
        self.__faultTree_PrimaryEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_FaultTree5"):
                opp_val = getattr(old_value, "faultTree_FaultTree5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_FaultTree5"):
                opp_val = getattr(value, "faultTree_FaultTree5", None)
                if opp_val is None:
                    setattr(value, "faultTree_FaultTree5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class faultTree_IntermediateEvent(Event):

    def __init__(self, probability: float, faultTree_IntermediateEvent: "faultTree_FaultTree" = None, faultTree_IntermediateEvent14: "faultTree_FaultTree" = None, IntermediateEvent: "faultTree_Gate" = None, IntermediateEvent41: "faultTree_TransferOut" = None, output: "faultTree_Gate" = None, IntermediateEvent27: "faultTree_IntermediateEvent" = None, bottomEvent: "faultTree_IntermediateEvent" = None, IntermediateEvent30: "faultTree_IntermediateEvent" = None, topEvent: "faultTree_IntermediateEvent" = None, event: "faultTree_TransferIn" = None, event34: "faultTree_TransferOut" = None, IntermediateEvent37: "faultTree_TransferIn" = None):
        self.probability = probability
        self.faultTree_IntermediateEvent = faultTree_IntermediateEvent
        self.faultTree_IntermediateEvent14 = faultTree_IntermediateEvent14
        self.IntermediateEvent = IntermediateEvent
        self.IntermediateEvent41 = IntermediateEvent41
        self.output = output
        self.IntermediateEvent27 = IntermediateEvent27
        self.bottomEvent = bottomEvent
        self.IntermediateEvent30 = IntermediateEvent30
        self.topEvent = topEvent
        self.event = event
        self.event34 = event34
        self.IntermediateEvent37 = IntermediateEvent37
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def topEvent(self):
        return self.__topEvent

    @topEvent.setter
    def topEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__topEvent", None)
        self.__topEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntermediateEvent30"):
                opp_val = getattr(old_value, "IntermediateEvent30", None)
                if opp_val == self:
                    setattr(old_value, "IntermediateEvent30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntermediateEvent30"):
                opp_val = getattr(value, "IntermediateEvent30", None)
                setattr(value, "IntermediateEvent30", self)

    @property
    def event34(self):
        return self.__event34

    @event34.setter
    def event34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__event34", None)
        self.__event34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransferOut35"):
                opp_val = getattr(old_value, "TransferOut35", None)
                if opp_val == self:
                    setattr(old_value, "TransferOut35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransferOut35"):
                opp_val = getattr(value, "TransferOut35", None)
                setattr(value, "TransferOut35", self)

    @property
    def bottomEvent(self):
        return self.__bottomEvent

    @bottomEvent.setter
    def bottomEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__bottomEvent", None)
        self.__bottomEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntermediateEvent27"):
                opp_val = getattr(old_value, "IntermediateEvent27", None)
                if opp_val == self:
                    setattr(old_value, "IntermediateEvent27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntermediateEvent27"):
                opp_val = getattr(value, "IntermediateEvent27", None)
                setattr(value, "IntermediateEvent27", self)

    @property
    def IntermediateEvent27(self):
        return self.__IntermediateEvent27

    @IntermediateEvent27.setter
    def IntermediateEvent27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__IntermediateEvent27", None)
        self.__IntermediateEvent27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottomEvent"):
                opp_val = getattr(old_value, "bottomEvent", None)
                if opp_val == self:
                    setattr(old_value, "bottomEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottomEvent"):
                opp_val = getattr(value, "bottomEvent", None)
                setattr(value, "bottomEvent", self)

    @property
    def IntermediateEvent30(self):
        return self.__IntermediateEvent30

    @IntermediateEvent30.setter
    def IntermediateEvent30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__IntermediateEvent30", None)
        self.__IntermediateEvent30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "topEvent"):
                opp_val = getattr(old_value, "topEvent", None)
                if opp_val == self:
                    setattr(old_value, "topEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "topEvent"):
                opp_val = getattr(value, "topEvent", None)
                setattr(value, "topEvent", self)

    @property
    def IntermediateEvent37(self):
        return self.__IntermediateEvent37

    @IntermediateEvent37.setter
    def IntermediateEvent37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__IntermediateEvent37", None)
        self.__IntermediateEvent37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transferIn"):
                opp_val = getattr(old_value, "transferIn", None)
                if opp_val == self:
                    setattr(old_value, "transferIn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transferIn"):
                opp_val = getattr(value, "transferIn", None)
                setattr(value, "transferIn", self)

    @property
    def IntermediateEvent41(self):
        return self.__IntermediateEvent41

    @IntermediateEvent41.setter
    def IntermediateEvent41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__IntermediateEvent41", None)
        self.__IntermediateEvent41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transferOut"):
                opp_val = getattr(old_value, "transferOut", None)
                if opp_val == self:
                    setattr(old_value, "transferOut", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transferOut"):
                opp_val = getattr(value, "transferOut", None)
                setattr(value, "transferOut", self)

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__output", None)
        self.__output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Gate24"):
                opp_val = getattr(old_value, "Gate24", None)
                if opp_val == self:
                    setattr(old_value, "Gate24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Gate24"):
                opp_val = getattr(value, "Gate24", None)
                setattr(value, "Gate24", self)

    @property
    def faultTree_IntermediateEvent14(self):
        return self.__faultTree_IntermediateEvent14

    @faultTree_IntermediateEvent14.setter
    def faultTree_IntermediateEvent14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__faultTree_IntermediateEvent14", None)
        self.__faultTree_IntermediateEvent14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_FaultTree13"):
                opp_val = getattr(old_value, "faultTree_FaultTree13", None)
                if opp_val == self:
                    setattr(old_value, "faultTree_FaultTree13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_FaultTree13"):
                opp_val = getattr(value, "faultTree_FaultTree13", None)
                setattr(value, "faultTree_FaultTree13", self)

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__event", None)
        self.__event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransferIn32"):
                opp_val = getattr(old_value, "TransferIn32", None)
                if opp_val == self:
                    setattr(old_value, "TransferIn32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransferIn32"):
                opp_val = getattr(value, "TransferIn32", None)
                setattr(value, "TransferIn32", self)

    @property
    def IntermediateEvent(self):
        return self.__IntermediateEvent

    @IntermediateEvent.setter
    def IntermediateEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__IntermediateEvent", None)
        self.__IntermediateEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottomGate"):
                opp_val = getattr(old_value, "bottomGate", None)
                if opp_val == self:
                    setattr(old_value, "bottomGate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottomGate"):
                opp_val = getattr(value, "bottomGate", None)
                setattr(value, "bottomGate", self)

    @property
    def faultTree_IntermediateEvent(self):
        return self.__faultTree_IntermediateEvent

    @faultTree_IntermediateEvent.setter
    def faultTree_IntermediateEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_IntermediateEvent__faultTree_IntermediateEvent", None)
        self.__faultTree_IntermediateEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_FaultTree3"):
                opp_val = getattr(old_value, "faultTree_FaultTree3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_FaultTree3"):
                opp_val = getattr(value, "faultTree_FaultTree3", None)
                if opp_val is None:
                    setattr(value, "faultTree_FaultTree3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class faultTree_Event(ABC):

    def __init__(self, name: str, description: str, inputs: set["faultTree_Gate"] = None, faultTree_Event21: "faultTree_FaultTree" = None, faultTree_Event: "faultTree_FaultTree" = None, Event: "faultTree_Gate" = None):
        self.name = name
        self.description = description
        self.inputs = inputs if inputs is not None else set()
        self.faultTree_Event21 = faultTree_Event21
        self.faultTree_Event = faultTree_Event
        self.Event = Event
        
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
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "topGates"):
                opp_val = getattr(old_value, "topGates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "topGates"):
                opp_val = getattr(value, "topGates", None)
                if opp_val is None:
                    setattr(value, "topGates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def faultTree_Event21(self):
        return self.__faultTree_Event21

    @faultTree_Event21.setter
    def faultTree_Event21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Event__faultTree_Event21", None)
        self.__faultTree_Event21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_FaultTree22"):
                opp_val = getattr(old_value, "faultTree_FaultTree22", None)
                if opp_val == self:
                    setattr(old_value, "faultTree_FaultTree22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_FaultTree22"):
                opp_val = getattr(value, "faultTree_FaultTree22", None)
                setattr(value, "faultTree_FaultTree22", self)

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Event__inputs", None)
        self.__inputs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Gate19"):
                    opp_val = getattr(item, "Gate19", None)
                    
                    if opp_val == self:
                        setattr(item, "Gate19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Gate19"):
                    opp_val = getattr(item, "Gate19", None)
                    
                    setattr(item, "Gate19", self)
                    

    @property
    def faultTree_Event(self):
        return self.__faultTree_Event

    @faultTree_Event.setter
    def faultTree_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Event__faultTree_Event", None)
        self.__faultTree_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_FaultTree"):
                opp_val = getattr(old_value, "faultTree_FaultTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_FaultTree"):
                opp_val = getattr(value, "faultTree_FaultTree", None)
                if opp_val is None:
                    setattr(value, "faultTree_FaultTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class faultTree_Gate:

    def __init__(self, type: str, probability: float, name: str, Gate: "faultTree_FaultTree" = None, Gate19: "faultTree_Event" = None, topGates: set["faultTree_Event"] = None, bottomGate: "faultTree_IntermediateEvent" = None, gates: "faultTree_FaultTree" = None, Gate24: "faultTree_IntermediateEvent" = None):
        self.type = type
        self.probability = probability
        self.name = name
        self.Gate = Gate
        self.Gate19 = Gate19
        self.topGates = topGates if topGates is not None else set()
        self.bottomGate = bottomGate
        self.gates = gates
        self.Gate24 = Gate24
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Gate(self):
        return self.__Gate

    @Gate.setter
    def Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Gate__Gate", None)
        self.__Gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree"):
                opp_val = getattr(old_value, "faultTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree"):
                opp_val = getattr(value, "faultTree", None)
                if opp_val is None:
                    setattr(value, "faultTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Gate19(self):
        return self.__Gate19

    @Gate19.setter
    def Gate19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Gate__Gate19", None)
        self.__Gate19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputs"):
                opp_val = getattr(old_value, "inputs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputs"):
                opp_val = getattr(value, "inputs", None)
                if opp_val is None:
                    setattr(value, "inputs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gates(self):
        return self.__gates

    @gates.setter
    def gates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Gate__gates", None)
        self.__gates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree"):
                opp_val = getattr(old_value, "FaultTree", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree"):
                opp_val = getattr(value, "FaultTree", None)
                setattr(value, "FaultTree", self)

    @property
    def bottomGate(self):
        return self.__bottomGate

    @bottomGate.setter
    def bottomGate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Gate__bottomGate", None)
        self.__bottomGate = value
        
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
    def topGates(self):
        return self.__topGates

    @topGates.setter
    def topGates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Gate__topGates", None)
        self.__topGates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def Gate24(self):
        return self.__Gate24

    @Gate24.setter
    def Gate24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_Gate__Gate24", None)
        self.__Gate24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "output"):
                opp_val = getattr(old_value, "output", None)
                if opp_val == self:
                    setattr(old_value, "output", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "output"):
                opp_val = getattr(value, "output", None)
                setattr(value, "output", self)

class faultTree_FaultTree:

    def __init__(self, name: str, faultTree: set["faultTree_Gate"] = None, faultTree_FaultTree22: "faultTree_Event" = None, faultTree_FaultTree: set["faultTree_Event"] = None, faultTree_FaultTree3: set["faultTree_IntermediateEvent"] = None, faultTree_FaultTree5: set["faultTree_PrimaryEvent"] = None, faultTree_FaultTree7: set["faultTree_ConditioningEvent"] = None, faultTree9: "faultTree_TransferOut" = None, faultTree11: set["faultTree_TransferIn"] = None, faultTree_FaultTree13: "faultTree_IntermediateEvent" = None, FaultTree: "faultTree_Gate" = None, FaultTree39: "faultTree_TransferIn" = None, FaultTree44: "faultTree_TransferOut" = None):
        self.name = name
        self.faultTree = faultTree if faultTree is not None else set()
        self.faultTree_FaultTree22 = faultTree_FaultTree22
        self.faultTree_FaultTree = faultTree_FaultTree if faultTree_FaultTree is not None else set()
        self.faultTree_FaultTree3 = faultTree_FaultTree3 if faultTree_FaultTree3 is not None else set()
        self.faultTree_FaultTree5 = faultTree_FaultTree5 if faultTree_FaultTree5 is not None else set()
        self.faultTree_FaultTree7 = faultTree_FaultTree7 if faultTree_FaultTree7 is not None else set()
        self.faultTree9 = faultTree9
        self.faultTree11 = faultTree11 if faultTree11 is not None else set()
        self.faultTree_FaultTree13 = faultTree_FaultTree13
        self.FaultTree = FaultTree
        self.FaultTree39 = FaultTree39
        self.FaultTree44 = FaultTree44
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FaultTree(self):
        return self.__FaultTree

    @FaultTree.setter
    def FaultTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__FaultTree", None)
        self.__FaultTree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gates"):
                opp_val = getattr(old_value, "gates", None)
                if opp_val == self:
                    setattr(old_value, "gates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gates"):
                opp_val = getattr(value, "gates", None)
                setattr(value, "gates", self)

    @property
    def faultTree_FaultTree(self):
        return self.__faultTree_FaultTree

    @faultTree_FaultTree.setter
    def faultTree_FaultTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree_FaultTree", None)
        self.__faultTree_FaultTree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "faultTree_Event"):
                    opp_val = getattr(item, "faultTree_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "faultTree_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "faultTree_Event"):
                    opp_val = getattr(item, "faultTree_Event", None)
                    
                    setattr(item, "faultTree_Event", self)
                    

    @property
    def faultTree(self):
        return self.__faultTree

    @faultTree.setter
    def faultTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree", None)
        self.__faultTree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Gate"):
                    opp_val = getattr(item, "Gate", None)
                    
                    if opp_val == self:
                        setattr(item, "Gate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Gate"):
                    opp_val = getattr(item, "Gate", None)
                    
                    setattr(item, "Gate", self)
                    

    @property
    def FaultTree44(self):
        return self.__FaultTree44

    @FaultTree44.setter
    def FaultTree44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__FaultTree44", None)
        self.__FaultTree44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transferOut43"):
                opp_val = getattr(old_value, "transferOut43", None)
                if opp_val == self:
                    setattr(old_value, "transferOut43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transferOut43"):
                opp_val = getattr(value, "transferOut43", None)
                setattr(value, "transferOut43", self)

    @property
    def FaultTree39(self):
        return self.__FaultTree39

    @FaultTree39.setter
    def FaultTree39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__FaultTree39", None)
        self.__FaultTree39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transferIns"):
                opp_val = getattr(old_value, "transferIns", None)
                if opp_val == self:
                    setattr(old_value, "transferIns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transferIns"):
                opp_val = getattr(value, "transferIns", None)
                setattr(value, "transferIns", self)

    @property
    def faultTree_FaultTree7(self):
        return self.__faultTree_FaultTree7

    @faultTree_FaultTree7.setter
    def faultTree_FaultTree7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree_FaultTree7", None)
        self.__faultTree_FaultTree7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "faultTree_ConditioningEvent"):
                    opp_val = getattr(item, "faultTree_ConditioningEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "faultTree_ConditioningEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "faultTree_ConditioningEvent"):
                    opp_val = getattr(item, "faultTree_ConditioningEvent", None)
                    
                    setattr(item, "faultTree_ConditioningEvent", self)
                    

    @property
    def faultTree_FaultTree22(self):
        return self.__faultTree_FaultTree22

    @faultTree_FaultTree22.setter
    def faultTree_FaultTree22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree_FaultTree22", None)
        self.__faultTree_FaultTree22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_Event21"):
                opp_val = getattr(old_value, "faultTree_Event21", None)
                if opp_val == self:
                    setattr(old_value, "faultTree_Event21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_Event21"):
                opp_val = getattr(value, "faultTree_Event21", None)
                setattr(value, "faultTree_Event21", self)

    @property
    def faultTree_FaultTree3(self):
        return self.__faultTree_FaultTree3

    @faultTree_FaultTree3.setter
    def faultTree_FaultTree3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree_FaultTree3", None)
        self.__faultTree_FaultTree3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "faultTree_IntermediateEvent"):
                    opp_val = getattr(item, "faultTree_IntermediateEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "faultTree_IntermediateEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "faultTree_IntermediateEvent"):
                    opp_val = getattr(item, "faultTree_IntermediateEvent", None)
                    
                    setattr(item, "faultTree_IntermediateEvent", self)
                    

    @property
    def faultTree11(self):
        return self.__faultTree11

    @faultTree11.setter
    def faultTree11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree11", None)
        self.__faultTree11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransferIn"):
                    opp_val = getattr(item, "TransferIn", None)
                    
                    if opp_val == self:
                        setattr(item, "TransferIn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransferIn"):
                    opp_val = getattr(item, "TransferIn", None)
                    
                    setattr(item, "TransferIn", self)
                    

    @property
    def faultTree9(self):
        return self.__faultTree9

    @faultTree9.setter
    def faultTree9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree9", None)
        self.__faultTree9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransferOut"):
                opp_val = getattr(old_value, "TransferOut", None)
                if opp_val == self:
                    setattr(old_value, "TransferOut", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransferOut"):
                opp_val = getattr(value, "TransferOut", None)
                setattr(value, "TransferOut", self)

    @property
    def faultTree_FaultTree13(self):
        return self.__faultTree_FaultTree13

    @faultTree_FaultTree13.setter
    def faultTree_FaultTree13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree_FaultTree13", None)
        self.__faultTree_FaultTree13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faultTree_IntermediateEvent14"):
                opp_val = getattr(old_value, "faultTree_IntermediateEvent14", None)
                if opp_val == self:
                    setattr(old_value, "faultTree_IntermediateEvent14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faultTree_IntermediateEvent14"):
                opp_val = getattr(value, "faultTree_IntermediateEvent14", None)
                setattr(value, "faultTree_IntermediateEvent14", self)

    @property
    def faultTree_FaultTree5(self):
        return self.__faultTree_FaultTree5

    @faultTree_FaultTree5.setter
    def faultTree_FaultTree5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_faultTree_FaultTree__faultTree_FaultTree5", None)
        self.__faultTree_FaultTree5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "faultTree_PrimaryEvent"):
                    opp_val = getattr(item, "faultTree_PrimaryEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "faultTree_PrimaryEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "faultTree_PrimaryEvent"):
                    opp_val = getattr(item, "faultTree_PrimaryEvent", None)
                    
                    setattr(item, "faultTree_PrimaryEvent", self)
                    

from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ControlNode:

    pass
class activitydiagram_ForkNode(ControlNode):

    pass
class activitydiagram_JoinNode(ControlNode):

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_InitialNode(ControlNode):

    pass
class ActivityNode:

    pass
class activitydiagram_ControlNode(ActivityNode):

    pass
class activitydiagram_SignalNode(ActivityNode):

    def __init__(self, signalId: str):
        self.signalId = signalId
        
    @property
    def signalId(self) -> str:
        return self.__signalId

    @signalId.setter
    def signalId(self, signalId: str):
        self.__signalId = signalId

class activitydiagram_ObjectNode(ActivityNode):

    pass
class activitydiagram_ActionNode(ActivityNode):

    pass
class ObjectNode:

    pass
class activitydiagram_Pin(ObjectNode):

    pass
class activitydiagram_ExpansionNode(ObjectNode):

    pass
class activitydiagram_DataStoreNode(ObjectNode):

    pass
class activitydiagram_ActivityParameterNode(ObjectNode):

    def __init__(self, parameter: str):
        self.parameter = parameter
        
    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

class FinalNode:

    pass
class activitydiagram_FlowFinalNode(FinalNode):

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    pass
class activitydiagram_TimeEventNode(ActivityNode):

    def __init__(self, cycle: str):
        self.cycle = cycle
        
    @property
    def cycle(self) -> str:
        return self.__cycle

    @cycle.setter
    def cycle(self, cycle: str):
        self.__cycle = cycle

class activitydiagram_AcceptSignalNode(ActivityNode):

    def __init__(self, signalId: str):
        self.signalId = signalId
        
    @property
    def signalId(self) -> str:
        return self.__signalId

    @signalId.setter
    def signalId(self, signalId: str):
        self.__signalId = signalId

class activitydiagram_DecisionNode(ControlNode):

    pass
class activitydiagram_MergeNode(ControlNode):

    pass
class activitydiagram_ADElement(ABC):

    def __init__(self, name: str, ADElement: "activitydiagram_Activity" = None, contains: "activitydiagram_Activity" = None):
        self.name = name
        self.ADElement = ADElement
        self.contains = contains
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contains(self):
        return self.__contains

    @contains.setter
    def contains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ADElement__contains", None)
        self.__contains = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

    @property
    def ADElement(self):
        return self.__ADElement

    @ADElement.setter
    def ADElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ADElement__ADElement", None)
        self.__ADElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityDiag"):
                opp_val = getattr(old_value, "activityDiag", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityDiag"):
                opp_val = getattr(value, "activityDiag", None)
                if opp_val is None:
                    setattr(value, "activityDiag", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ADElement:

    pass
class activitydiagram_ActivityNode(ADElement):

    def __init__(self, current: bool, source: set["activitydiagram_ActivityEdge"] = None, target: set["activitydiagram_ActivityEdge"] = None, ActivityNode: "activitydiagram_ActivityEdge" = None, ActivityNode7: "activitydiagram_ActivityEdge" = None):
        self.current = current
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.ActivityNode = ActivityNode
        self.ActivityNode7 = ActivityNode7
        
    @property
    def current(self) -> bool:
        return self.__current

    @current.setter
    def current(self, current: bool):
        self.__current = current

    @property
    def ActivityNode(self):
        return self.__ActivityNode

    @ActivityNode.setter
    def ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode", None)
        self.__ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sedges"):
                opp_val = getattr(old_value, "sedges", None)
                if opp_val == self:
                    setattr(old_value, "sedges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sedges"):
                opp_val = getattr(value, "sedges", None)
                setattr(value, "sedges", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge4"):
                    opp_val = getattr(item, "ActivityEdge4", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge4"):
                    opp_val = getattr(item, "ActivityEdge4", None)
                    
                    setattr(item, "ActivityEdge4", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    @property
    def ActivityNode7(self):
        return self.__ActivityNode7

    @ActivityNode7.setter
    def ActivityNode7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode7", None)
        self.__ActivityNode7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tedges"):
                opp_val = getattr(old_value, "tedges", None)
                if opp_val == self:
                    setattr(old_value, "tedges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tedges"):
                opp_val = getattr(value, "tedges", None)
                setattr(value, "tedges", self)

class activitydiagram_ActivityEdge(ADElement):

    def __init__(self, guard: bool, ActivityEdge: "activitydiagram_ActivityNode" = None, ActivityEdge4: "activitydiagram_ActivityNode" = None, sedges: "activitydiagram_ActivityNode" = None, tedges: "activitydiagram_ActivityNode" = None):
        self.guard = guard
        self.ActivityEdge = ActivityEdge
        self.ActivityEdge4 = ActivityEdge4
        self.sedges = sedges
        self.tedges = tedges
        
    @property
    def guard(self) -> bool:
        return self.__guard

    @guard.setter
    def guard(self, guard: bool):
        self.__guard = guard

    @property
    def tedges(self):
        return self.__tedges

    @tedges.setter
    def tedges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__tedges", None)
        self.__tedges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode7"):
                opp_val = getattr(old_value, "ActivityNode7", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode7"):
                opp_val = getattr(value, "ActivityNode7", None)
                setattr(value, "ActivityNode7", self)

    @property
    def sedges(self):
        return self.__sedges

    @sedges.setter
    def sedges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__sedges", None)
        self.__sedges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode"):
                opp_val = getattr(old_value, "ActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode"):
                opp_val = getattr(value, "ActivityNode", None)
                setattr(value, "ActivityNode", self)

    @property
    def ActivityEdge(self):
        return self.__ActivityEdge

    @ActivityEdge.setter
    def ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__ActivityEdge", None)
        self.__ActivityEdge = value
        
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
    def ActivityEdge4(self):
        return self.__ActivityEdge4

    @ActivityEdge4.setter
    def ActivityEdge4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__ActivityEdge4", None)
        self.__ActivityEdge4 = value
        
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

class activitydiagram_Activity(ADElement):

    pass
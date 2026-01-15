from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ObjectNode:

    pass
class activity_Object(ObjectNode):

    pass
class activity_Pin(ObjectNode):

    pass
class Pin:

    pass
class activity_InputPin(Pin):

    pass
class activity_OutputPin(Pin):

    pass
class ExecutableNode:

    pass
class activity_AcceptEventAction(ExecutableNode):

    pass
class activity_SendSignalAction(ExecutableNode):

    pass
class activity_AcceptTimeEventAction(ExecutableNode):

    pass
class activity_Action(ExecutableNode):

    pass
class FinalNode:

    pass
class activity_ActivityFinalNode(FinalNode):

    pass
class activity_FlowFinalNode(FinalNode):

    pass
class ActivityEdge:

    pass
class activity_InterruptEdge(ActivityEdge):

    pass
class activity_ObjectFlow(ActivityEdge):

    pass
class activity_ControlFlow(ActivityEdge):

    pass
class activity_DataStoreNode(ObjectNode):

    pass
class activity_CentralBufferNode(ObjectNode):

    pass
class NamedElement:

    pass
class Activity:

    pass
class activity_ActivityGroup(Activity):

    def __init__(self, name: str, activity_ActivityGroup: "activity_Activity" = None):
        self.name = name
        self.activity_ActivityGroup = activity_ActivityGroup
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activity_ActivityGroup(self):
        return self.__activity_ActivityGroup

    @activity_ActivityGroup.setter
    def activity_ActivityGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityGroup__activity_ActivityGroup", None)
        self.__activity_ActivityGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_Activity8"):
                opp_val = getattr(old_value, "activity_Activity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_Activity8"):
                opp_val = getattr(value, "activity_Activity8", None)
                if opp_val is None:
                    setattr(value, "activity_Activity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class activity_ActivityParameterNode(Activity):

    def __init__(self, name: str, activity_ActivityParameterNode: "activity_Activity" = None, activity_ActivityParameterNode10: set["activity_ActivityNode"] = None):
        self.name = name
        self.activity_ActivityParameterNode = activity_ActivityParameterNode
        self.activity_ActivityParameterNode10 = activity_ActivityParameterNode10 if activity_ActivityParameterNode10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activity_ActivityParameterNode10(self):
        return self.__activity_ActivityParameterNode10

    @activity_ActivityParameterNode10.setter
    def activity_ActivityParameterNode10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityParameterNode__activity_ActivityParameterNode10", None)
        self.__activity_ActivityParameterNode10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activity_ActivityNode11"):
                    opp_val = getattr(item, "activity_ActivityNode11", None)
                    
                    if opp_val == self:
                        setattr(item, "activity_ActivityNode11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activity_ActivityNode11"):
                    opp_val = getattr(item, "activity_ActivityNode11", None)
                    
                    setattr(item, "activity_ActivityNode11", self)
                    

    @property
    def activity_ActivityParameterNode(self):
        return self.__activity_ActivityParameterNode

    @activity_ActivityParameterNode.setter
    def activity_ActivityParameterNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activity_ActivityParameterNode__activity_ActivityParameterNode", None)
        self.__activity_ActivityParameterNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity_Activity4"):
                opp_val = getattr(old_value, "activity_Activity4", None)
                if opp_val == self:
                    setattr(old_value, "activity_Activity4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity_Activity4"):
                opp_val = getattr(value, "activity_Activity4", None)
                setattr(value, "activity_Activity4", self)

class ControlNode:

    pass
class activity_Connector(ControlNode):

    pass
class activity_JoinNode(ControlNode):

    pass
class activity_FinalNode(ControlNode):

    pass
class activity_MergeNode(ControlNode):

    pass
class activity_DecisionNode(ControlNode):

    pass
class activity_ForkNode(ControlNode):

    pass
class activity_InitialNode(ControlNode):

    pass
class ActivityNode:

    pass
class activity_ExecutableNode(ActivityNode):

    pass
class activity_ObjectNode(ActivityNode):

    pass
class activity_ControlNode(ActivityNode):

    pass
class activity_NamedElement(ABC):

    def __init__(self, qualifiedName: str, Name: str):
        self.qualifiedName = qualifiedName
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class ActivityGroup:

    pass
class activity_ActivityPartition(ActivityGroup):

    pass
class activity_InterruptibleActivityRegion(ActivityGroup):

    pass
class activity_ActivityNode(NamedElement):

    pass
class activity_ActivityEdge(NamedElement):

    pass
class activity_Activity:

    pass
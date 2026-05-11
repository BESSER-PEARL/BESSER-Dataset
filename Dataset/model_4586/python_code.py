from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class ObjectNodeOrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
    FIFO = "FIFO"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"


############################################
# Definition of Classes
############################################

class ExpansionRegion:

    pass
class ExpansionNode:

    pass
class Activities_ExtraStructuredActivities_Classifier(ABC):

    pass
class Classifier:

    pass
class Activities_CompleteStructuredActivities_InputPin:

    pass
class ExecutableNode:

    pass
class Clause:

    pass
class Activities_StructuredActivities_MultiplicityElement(ABC):

    pass
class Activities_StructuredActivities_OutputPin:

    pass
class StructuredActivities_MultiplicityElement:

    pass
class ExceptionHandler:

    pass
class IntermediateActivities_Feature:

    pass
class FundamentalActivities_Namespace:

    pass
class Activities_IntermediateActivities_BehavioralFeature(FundamentalActivities_Namespace, IntermediateActivities_Feature):

    pass
class CentralBufferNode:

    pass
class Activities_IntermediateActivities_DataStoreNode(CentralBufferNode):

    pass
class Activities_IntermediateActivities_State:

    pass
class Activities_IntermediateActivities_Constraint:

    pass
class Activities_IntermediateActivities_Element(ABC):

    pass
class FundamentalActivities_Action:

    pass
class FundamentalActivities_ActivityGroup:

    pass
class StructuredActivities_ExecutableNode:

    pass
class Activities_StructuredActivities_StructuredActivityNode(FundamentalActivities_Namespace, FundamentalActivities_ActivityGroup, FundamentalActivities_Action, StructuredActivities_ExecutableNode):

    def __init__(self, mustIsolate: bool, structuredNode: "Activity" = None, Activities_StructuredActivities_StructuredActivityNode: set["Variable"] = None, inStructuredNode: set["ActivityNode"] = None, Activities_StructuredActivities_StructuredActivityNode106: set["InputPin"] = None, inStructuredNode109: set["ActivityEdge"] = None, Activities_StructuredActivities_StructuredActivityNode112: set["OutputPin"] = None):
        self.mustIsolate = mustIsolate
        self.structuredNode = structuredNode
        self.Activities_StructuredActivities_StructuredActivityNode = Activities_StructuredActivities_StructuredActivityNode if Activities_StructuredActivities_StructuredActivityNode is not None else set()
        self.inStructuredNode = inStructuredNode if inStructuredNode is not None else set()
        self.Activities_StructuredActivities_StructuredActivityNode106 = Activities_StructuredActivities_StructuredActivityNode106 if Activities_StructuredActivities_StructuredActivityNode106 is not None else set()
        self.inStructuredNode109 = inStructuredNode109 if inStructuredNode109 is not None else set()
        self.Activities_StructuredActivities_StructuredActivityNode112 = Activities_StructuredActivities_StructuredActivityNode112 if Activities_StructuredActivities_StructuredActivityNode112 is not None else set()
        
        pass
    @property
    def mustIsolate(self):
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate


    @property
    def Activities_StructuredActivities_StructuredActivityNode112(self):
        return self.__Activities_StructuredActivities_StructuredActivityNode112

    @Activities_StructuredActivities_StructuredActivityNode112.setter
    def Activities_StructuredActivities_StructuredActivityNode112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__Activities_StructuredActivities_StructuredActivityNode112", None)
        self.__Activities_StructuredActivities_StructuredActivityNode112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin113"):
                    opp_val = getattr(item, "OutputPin113", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin113"):
                    opp_val = getattr(item, "OutputPin113", None)
                    
                    setattr(item, "OutputPin113", self)
                    

    @property
    def Activities_StructuredActivities_StructuredActivityNode(self):
        return self.__Activities_StructuredActivities_StructuredActivityNode

    @Activities_StructuredActivities_StructuredActivityNode.setter
    def Activities_StructuredActivities_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__Activities_StructuredActivities_StructuredActivityNode", None)
        self.__Activities_StructuredActivities_StructuredActivityNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable102"):
                    opp_val = getattr(item, "Variable102", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable102"):
                    opp_val = getattr(item, "Variable102", None)
                    
                    setattr(item, "Variable102", self)
                    

    @property
    def Activities_StructuredActivities_StructuredActivityNode106(self):
        return self.__Activities_StructuredActivities_StructuredActivityNode106

    @Activities_StructuredActivities_StructuredActivityNode106.setter
    def Activities_StructuredActivities_StructuredActivityNode106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__Activities_StructuredActivities_StructuredActivityNode106", None)
        self.__Activities_StructuredActivities_StructuredActivityNode106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPin107"):
                    opp_val = getattr(item, "InputPin107", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPin107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPin107"):
                    opp_val = getattr(item, "InputPin107", None)
                    
                    setattr(item, "InputPin107", self)
                    

    @property
    def inStructuredNode(self):
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__inStructuredNode", None)
        self.__inStructuredNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode104"):
                    opp_val = getattr(item, "ActivityNode104", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode104"):
                    opp_val = getattr(item, "ActivityNode104", None)
                    
                    setattr(item, "ActivityNode104", self)
                    

    @property
    def structuredNode(self):
        return self.__structuredNode

    @structuredNode.setter
    def structuredNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__structuredNode", None)
        self.__structuredNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity100"):
                opp_val = getattr(old_value, "Activity100", None)
                if opp_val == self:
                    setattr(old_value, "Activity100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity100"):
                opp_val = getattr(value, "Activity100", None)
                setattr(value, "Activity100", self)

    @property
    def inStructuredNode109(self):
        return self.__inStructuredNode109

    @inStructuredNode109.setter
    def inStructuredNode109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__inStructuredNode109", None)
        self.__inStructuredNode109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge110"):
                    opp_val = getattr(item, "ActivityEdge110", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge110"):
                    opp_val = getattr(item, "ActivityEdge110", None)
                    
                    setattr(item, "ActivityEdge110", self)
                    

class Activities_IntermediateActivities_Class:

    pass
class Activities_IntermediateActivities_Feature(ABC):

    pass
class FinalNode:

    pass
class Activities_IntermediateActivities_FlowFinalNode(FinalNode):

    pass
class State:

    pass
class Element:

    pass
class Activities_ExtraStructuredActivities_ExceptionHandler(Element):

    pass
class Activities_StructuredActivities_Clause(Element):

    pass
class Activities_IntermediateActivities_ValueSpecification(ABC):

    pass
class ObjectFlow:

    pass
class ControlNode:

    pass
class Activities_IntermediateActivities_FinalNode(ControlNode):

    pass
class Activities_IntermediateActivities_DecisionNode(ControlNode):

    pass
class Activities_IntermediateActivities_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: bool, Activities_IntermediateActivities_JoinNode: "ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.Activities_IntermediateActivities_JoinNode = Activities_IntermediateActivities_JoinNode
        
        pass
    @property
    def isCombineDuplicate(self):
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: bool):
        self.__isCombineDuplicate = isCombineDuplicate


    @property
    def Activities_IntermediateActivities_JoinNode(self):
        return self.__Activities_IntermediateActivities_JoinNode

    @Activities_IntermediateActivities_JoinNode.setter
    def Activities_IntermediateActivities_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_IntermediateActivities_JoinNode__Activities_IntermediateActivities_JoinNode", None)
        self.__Activities_IntermediateActivities_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification74"):
                opp_val = getattr(old_value, "ValueSpecification74", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification74"):
                opp_val = getattr(value, "ValueSpecification74", None)
                setattr(value, "ValueSpecification74", self)

class Activities_IntermediateActivities_ForkNode(ControlNode):

    pass
class Activities_IntermediateActivities_MergeNode(ControlNode):

    pass
class Activities_BasicActivities_InitialNode(ControlNode):

    pass
class IntermediateActivities_FinalNode:

    pass
class BasicActivities_ControlNode:

    pass
class Activities_BasicActivities_ActivityFinalNode(BasicActivities_ControlNode, IntermediateActivities_FinalNode):

    pass
class Activities_BasicActivities_Parameter:

    def __init__(self, isException: bool, isStream: bool, effect: str, parameter: set["ParameterSet"] = None):
        self.isException = isException
        self.isStream = isStream
        self.effect = effect
        self.parameter = parameter if parameter is not None else set()
        
        pass
    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def isException(self):
        return self.__isException

    @isException.setter
    def isException(self, isException: bool):
        self.__isException = isException


    @property
    def isStream(self):
        return self.__isStream

    @isStream.setter
    def isStream(self, isStream: bool):
        self.__isStream = isStream


    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_Parameter__parameter", None)
        self.__parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterSet46"):
                    opp_val = getattr(item, "ParameterSet46", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterSet46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterSet46"):
                    opp_val = getattr(item, "ParameterSet46", None)
                    
                    setattr(item, "ParameterSet46", self)
                    

class Parameter:

    pass
class ObjectNode:

    pass
class Activities_IntermediateActivities_CentralBufferNode(ObjectNode):

    pass
class Activities_ExtraStructuredActivities_ExpansionNode(ObjectNode):

    pass
class Activities_BasicActivities_ActivityParameterNode(ObjectNode):

    pass
class Activities_BasicActivities_Pin(ObjectNode):

    def __init__(self, isControl: bool, ObjectNode: "Activities_ExtraStructuredActivities_ExceptionHandler" = None):
        self.isControl = isControl
        
        pass
    @property
    def isControl(self):
        return self.__isControl

    @isControl.setter
    def isControl(self, isControl: bool):
        self.__isControl = isControl


class Activities_BasicActivities_TypedElement:

    pass
class BasicActivities_TypedElement:

    pass
class Activities_StructuredActivities_Variable(BasicActivities_TypedElement, StructuredActivities_MultiplicityElement):

    pass
class ValueSpecification:

    pass
class OutputPin:

    pass
class InputPin:

    pass
class Constraint:

    pass
class InterruptibleActivityRegion:

    pass
class FundamentalActivities_ActivityNode:

    pass
class Activities_BasicActivities_ObjectNode(BasicActivities_TypedElement, FundamentalActivities_ActivityNode):

    pass
class RedefinableElement:

    pass
class Activities_BasicActivities_ActivityEdge(RedefinableElement):

    pass
class Activities_BasicActivities_RedefinableElement(ABC):

    pass
class Activities_FundamentalActivities_Namespace(ABC):

    pass
class Activity:

    pass
class NamedElement:

    pass
class Activities_IntermediateActivities_ParameterSet(NamedElement):

    pass
class Activities_FundamentalActivities_ActivityGroup(NamedElement):

    pass
class ActivityPartition:

    pass
class ActivityEdge:

    pass
class Activities_BasicActivities_ControlFlow(ActivityEdge):

    pass
class Activities_BasicActivities_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool, ordering: str, isControlType: bool, Activities_BasicActivities_ObjectFlow: "Behavior" = None, Activities_BasicActivities_ObjectFlow69: "Behavior" = None, Activities_BasicActivities_ObjectFlow72: set["State"] = None, ActivityEdge110: "Activities_StructuredActivities_StructuredActivityNode" = None, ActivityEdge52: "Activities_BasicActivities_ActivityEdge" = None, ActivityEdge17: "Activities_FundamentalActivities_ActivityNode" = None, ActivityEdge42: "Activities_FundamentalActivities_ActivityGroup" = None, ActivityEdge: "Activities_FundamentalActivities_Activity" = None, ActivityEdge15: "Activities_FundamentalActivities_ActivityNode" = None, ActivityEdge80: "Activities_IntermediateActivities_ActivityPartition" = None, ActivityEdge96: "Activities_IntermediateActivities_InterruptibleActivityRegion" = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.ordering = ordering
        self.isControlType = isControlType
        self.Activities_BasicActivities_ObjectFlow = Activities_BasicActivities_ObjectFlow
        self.Activities_BasicActivities_ObjectFlow69 = Activities_BasicActivities_ObjectFlow69
        self.Activities_BasicActivities_ObjectFlow72 = Activities_BasicActivities_ObjectFlow72 if Activities_BasicActivities_ObjectFlow72 is not None else set()
        
        pass
    @property
    def isControlType(self):
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: bool):
        self.__isControlType = isControlType


    @property
    def isMultireceive(self):
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: bool):
        self.__isMultireceive = isMultireceive


    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def isMulticast(self):
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: bool):
        self.__isMulticast = isMulticast


    @property
    def Activities_BasicActivities_ObjectFlow69(self):
        return self.__Activities_BasicActivities_ObjectFlow69

    @Activities_BasicActivities_ObjectFlow69.setter
    def Activities_BasicActivities_ObjectFlow69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_ObjectFlow__Activities_BasicActivities_ObjectFlow69", None)
        self.__Activities_BasicActivities_ObjectFlow69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior70"):
                opp_val = getattr(old_value, "Behavior70", None)
                if opp_val == self:
                    setattr(old_value, "Behavior70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior70"):
                opp_val = getattr(value, "Behavior70", None)
                setattr(value, "Behavior70", self)

    @property
    def Activities_BasicActivities_ObjectFlow(self):
        return self.__Activities_BasicActivities_ObjectFlow

    @Activities_BasicActivities_ObjectFlow.setter
    def Activities_BasicActivities_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_ObjectFlow__Activities_BasicActivities_ObjectFlow", None)
        self.__Activities_BasicActivities_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior"):
                opp_val = getattr(old_value, "Behavior", None)
                if opp_val == self:
                    setattr(old_value, "Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior"):
                opp_val = getattr(value, "Behavior", None)
                setattr(value, "Behavior", self)

    @property
    def Activities_BasicActivities_ObjectFlow72(self):
        return self.__Activities_BasicActivities_ObjectFlow72

    @Activities_BasicActivities_ObjectFlow72.setter
    def Activities_BasicActivities_ObjectFlow72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_ObjectFlow__Activities_BasicActivities_ObjectFlow72", None)
        self.__Activities_BasicActivities_ObjectFlow72 = value if value is not None else set()
        
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
                    

class ActivityGroup:

    pass
class Activities_IntermediateActivities_ActivityPartition(ActivityGroup):

    pass
class Activities_IntermediateActivities_InterruptibleActivityRegion(ActivityGroup):

    pass
class ActivityNode:

    pass
class Activities_FundamentalActivities_Action(ActivityNode):

    def __init__(self, isLocallyReentrant: bool, Activities_FundamentalActivities_Action: set["Constraint"] = None, Activities_FundamentalActivities_Action27: set["Constraint"] = None, Activities_FundamentalActivities_Action30: set["InputPin"] = None, Activities_FundamentalActivities_Action32: set["OutputPin"] = None, ActivityNode: "Activities_FundamentalActivities_Activity" = None, ActivityNode98: "Activities_IntermediateActivities_InterruptibleActivityRegion" = None, ActivityNode104: "Activities_StructuredActivities_StructuredActivityNode" = None, ActivityNode88: "Activities_IntermediateActivities_ActivityPartition" = None, ActivityNode39: "Activities_FundamentalActivities_ActivityGroup" = None, ActivityNode48: "Activities_BasicActivities_ActivityEdge" = None, ActivityNode50: "Activities_BasicActivities_ActivityEdge" = None, ActivityNode13: "Activities_FundamentalActivities_ActivityNode" = None):
        self.isLocallyReentrant = isLocallyReentrant
        self.Activities_FundamentalActivities_Action = Activities_FundamentalActivities_Action if Activities_FundamentalActivities_Action is not None else set()
        self.Activities_FundamentalActivities_Action27 = Activities_FundamentalActivities_Action27 if Activities_FundamentalActivities_Action27 is not None else set()
        self.Activities_FundamentalActivities_Action30 = Activities_FundamentalActivities_Action30 if Activities_FundamentalActivities_Action30 is not None else set()
        self.Activities_FundamentalActivities_Action32 = Activities_FundamentalActivities_Action32 if Activities_FundamentalActivities_Action32 is not None else set()
        
        pass
    @property
    def isLocallyReentrant(self):
        return self.__isLocallyReentrant

    @isLocallyReentrant.setter
    def isLocallyReentrant(self, isLocallyReentrant: bool):
        self.__isLocallyReentrant = isLocallyReentrant


    @property
    def Activities_FundamentalActivities_Action30(self):
        return self.__Activities_FundamentalActivities_Action30

    @Activities_FundamentalActivities_Action30.setter
    def Activities_FundamentalActivities_Action30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action30", None)
        self.__Activities_FundamentalActivities_Action30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPin"):
                    opp_val = getattr(item, "InputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPin"):
                    opp_val = getattr(item, "InputPin", None)
                    
                    setattr(item, "InputPin", self)
                    

    @property
    def Activities_FundamentalActivities_Action(self):
        return self.__Activities_FundamentalActivities_Action

    @Activities_FundamentalActivities_Action.setter
    def Activities_FundamentalActivities_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action", None)
        self.__Activities_FundamentalActivities_Action = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def Activities_FundamentalActivities_Action32(self):
        return self.__Activities_FundamentalActivities_Action32

    @Activities_FundamentalActivities_Action32.setter
    def Activities_FundamentalActivities_Action32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action32", None)
        self.__Activities_FundamentalActivities_Action32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin"):
                    opp_val = getattr(item, "OutputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin"):
                    opp_val = getattr(item, "OutputPin", None)
                    
                    setattr(item, "OutputPin", self)
                    

    @property
    def Activities_FundamentalActivities_Action27(self):
        return self.__Activities_FundamentalActivities_Action27

    @Activities_FundamentalActivities_Action27.setter
    def Activities_FundamentalActivities_Action27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action27", None)
        self.__Activities_FundamentalActivities_Action27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint28"):
                    opp_val = getattr(item, "Constraint28", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint28"):
                    opp_val = getattr(item, "Constraint28", None)
                    
                    setattr(item, "Constraint28", self)
                    

class Activities_BasicActivities_ControlNode(ActivityNode):

    pass
class Activities_StructuredActivities_ExecutableNode(ActivityNode):

    pass
class Behavior:

    pass
class Activities_FundamentalActivities_Activity(Behavior):

    def __init__(self, isSingleExecution: bool, isReadOnly: bool, Activities_FundamentalActivities_Activity: set["ActivityNode"] = None, inActivity: set["ActivityGroup"] = None, Activities_FundamentalActivities_Activity3: set["ActivityEdge"] = None, Activities_FundamentalActivities_Activity5: set["ActivityPartition"] = None, activity: set["StructuredActivityNode"] = None, Activities_FundamentalActivities_Activity8: set["Variable"] = None, Behavior78: "Activities_IntermediateActivities_DecisionNode" = None, Behavior70: "Activities_BasicActivities_ObjectFlow" = None, Behavior: "Activities_BasicActivities_ObjectFlow" = None):
        self.isSingleExecution = isSingleExecution
        self.isReadOnly = isReadOnly
        self.Activities_FundamentalActivities_Activity = Activities_FundamentalActivities_Activity if Activities_FundamentalActivities_Activity is not None else set()
        self.inActivity = inActivity if inActivity is not None else set()
        self.Activities_FundamentalActivities_Activity3 = Activities_FundamentalActivities_Activity3 if Activities_FundamentalActivities_Activity3 is not None else set()
        self.Activities_FundamentalActivities_Activity5 = Activities_FundamentalActivities_Activity5 if Activities_FundamentalActivities_Activity5 is not None else set()
        self.activity = activity if activity is not None else set()
        self.Activities_FundamentalActivities_Activity8 = Activities_FundamentalActivities_Activity8 if Activities_FundamentalActivities_Activity8 is not None else set()
        
        pass
    @property
    def isSingleExecution(self):
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly


    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuredActivityNode"):
                    opp_val = getattr(item, "StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuredActivityNode"):
                    opp_val = getattr(item, "StructuredActivityNode", None)
                    
                    setattr(item, "StructuredActivityNode", self)
                    

    @property
    def Activities_FundamentalActivities_Activity8(self):
        return self.__Activities_FundamentalActivities_Activity8

    @Activities_FundamentalActivities_Activity8.setter
    def Activities_FundamentalActivities_Activity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity8", None)
        self.__Activities_FundamentalActivities_Activity8 = value if value is not None else set()
        
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
    def Activities_FundamentalActivities_Activity3(self):
        return self.__Activities_FundamentalActivities_Activity3

    @Activities_FundamentalActivities_Activity3.setter
    def Activities_FundamentalActivities_Activity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity3", None)
        self.__Activities_FundamentalActivities_Activity3 = value if value is not None else set()
        
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
    def inActivity(self):
        return self.__inActivity

    @inActivity.setter
    def inActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__inActivity", None)
        self.__inActivity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityGroup"):
                    opp_val = getattr(item, "ActivityGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityGroup"):
                    opp_val = getattr(item, "ActivityGroup", None)
                    
                    setattr(item, "ActivityGroup", self)
                    

    @property
    def Activities_FundamentalActivities_Activity5(self):
        return self.__Activities_FundamentalActivities_Activity5

    @Activities_FundamentalActivities_Activity5.setter
    def Activities_FundamentalActivities_Activity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity5", None)
        self.__Activities_FundamentalActivities_Activity5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityPartition"):
                    opp_val = getattr(item, "ActivityPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityPartition"):
                    opp_val = getattr(item, "ActivityPartition", None)
                    
                    setattr(item, "ActivityPartition", self)
                    

    @property
    def Activities_FundamentalActivities_Activity(self):
        return self.__Activities_FundamentalActivities_Activity

    @Activities_FundamentalActivities_Activity.setter
    def Activities_FundamentalActivities_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity", None)
        self.__Activities_FundamentalActivities_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    setattr(item, "ActivityNode", self)
                    

class BasicActivities_RedefinableElement:

    pass
class FundamentalActivities_NamedElement:

    pass
class Activities_FundamentalActivities_ActivityNode(FundamentalActivities_NamedElement, BasicActivities_RedefinableElement):

    pass
class Activities_FundamentalActivities_NamedElement(ABC):

    pass
class ParameterSet:

    pass
class Class:

    pass
class Activities_FundamentalActivities_Behavior(Class):

    pass
class Variable:

    pass
class StructuredActivityNode:

    pass
class Activities_ExtraStructuredActivities_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, regionAsInput: set["ExpansionNode"] = None, regionAsOutput: set["ExpansionNode"] = None, StructuredActivityNode66: "Activities_BasicActivities_ActivityEdge" = None, StructuredActivityNode: "Activities_FundamentalActivities_Activity" = None, StructuredActivityNode24: "Activities_FundamentalActivities_ActivityNode" = None):
        self.mode = mode
        self.regionAsInput = regionAsInput if regionAsInput is not None else set()
        self.regionAsOutput = regionAsOutput if regionAsOutput is not None else set()
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def regionAsOutput(self):
        return self.__regionAsOutput

    @regionAsOutput.setter
    def regionAsOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_ExtraStructuredActivities_ExpansionRegion__regionAsOutput", None)
        self.__regionAsOutput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpansionNode165"):
                    opp_val = getattr(item, "ExpansionNode165", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode165"):
                    opp_val = getattr(item, "ExpansionNode165", None)
                    
                    setattr(item, "ExpansionNode165", self)
                    

    @property
    def regionAsInput(self):
        return self.__regionAsInput

    @regionAsInput.setter
    def regionAsInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_ExtraStructuredActivities_ExpansionRegion__regionAsInput", None)
        self.__regionAsInput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpansionNode"):
                    opp_val = getattr(item, "ExpansionNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode"):
                    opp_val = getattr(item, "ExpansionNode", None)
                    
                    setattr(item, "ExpansionNode", self)
                    

class Activities_StructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: bool, isAssumed: bool, Activities_StructuredActivities_ConditionalNode: set["Clause"] = None, Activities_StructuredActivities_ConditionalNode139: set["ExecutableNode"] = None, Activities_StructuredActivities_ConditionalNode142: set["ExecutableNode"] = None, Activities_StructuredActivities_ConditionalNode145: set["OutputPin"] = None, StructuredActivityNode66: "Activities_BasicActivities_ActivityEdge" = None, StructuredActivityNode: "Activities_FundamentalActivities_Activity" = None, StructuredActivityNode24: "Activities_FundamentalActivities_ActivityNode" = None):
        self.isDeterminate = isDeterminate
        self.isAssumed = isAssumed
        self.Activities_StructuredActivities_ConditionalNode = Activities_StructuredActivities_ConditionalNode if Activities_StructuredActivities_ConditionalNode is not None else set()
        self.Activities_StructuredActivities_ConditionalNode139 = Activities_StructuredActivities_ConditionalNode139 if Activities_StructuredActivities_ConditionalNode139 is not None else set()
        self.Activities_StructuredActivities_ConditionalNode142 = Activities_StructuredActivities_ConditionalNode142 if Activities_StructuredActivities_ConditionalNode142 is not None else set()
        self.Activities_StructuredActivities_ConditionalNode145 = Activities_StructuredActivities_ConditionalNode145 if Activities_StructuredActivities_ConditionalNode145 is not None else set()
        
        pass
    @property
    def isDeterminate(self):
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: bool):
        self.__isDeterminate = isDeterminate


    @property
    def isAssumed(self):
        return self.__isAssumed

    @isAssumed.setter
    def isAssumed(self, isAssumed: bool):
        self.__isAssumed = isAssumed


    @property
    def Activities_StructuredActivities_ConditionalNode139(self):
        return self.__Activities_StructuredActivities_ConditionalNode139

    @Activities_StructuredActivities_ConditionalNode139.setter
    def Activities_StructuredActivities_ConditionalNode139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode139", None)
        self.__Activities_StructuredActivities_ConditionalNode139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode140"):
                    opp_val = getattr(item, "ExecutableNode140", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode140"):
                    opp_val = getattr(item, "ExecutableNode140", None)
                    
                    setattr(item, "ExecutableNode140", self)
                    

    @property
    def Activities_StructuredActivities_ConditionalNode142(self):
        return self.__Activities_StructuredActivities_ConditionalNode142

    @Activities_StructuredActivities_ConditionalNode142.setter
    def Activities_StructuredActivities_ConditionalNode142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode142", None)
        self.__Activities_StructuredActivities_ConditionalNode142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode143"):
                    opp_val = getattr(item, "ExecutableNode143", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode143"):
                    opp_val = getattr(item, "ExecutableNode143", None)
                    
                    setattr(item, "ExecutableNode143", self)
                    

    @property
    def Activities_StructuredActivities_ConditionalNode145(self):
        return self.__Activities_StructuredActivities_ConditionalNode145

    @Activities_StructuredActivities_ConditionalNode145.setter
    def Activities_StructuredActivities_ConditionalNode145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode145", None)
        self.__Activities_StructuredActivities_ConditionalNode145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin146"):
                    opp_val = getattr(item, "OutputPin146", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin146"):
                    opp_val = getattr(item, "OutputPin146", None)
                    
                    setattr(item, "OutputPin146", self)
                    

    @property
    def Activities_StructuredActivities_ConditionalNode(self):
        return self.__Activities_StructuredActivities_ConditionalNode

    @Activities_StructuredActivities_ConditionalNode.setter
    def Activities_StructuredActivities_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode", None)
        self.__Activities_StructuredActivities_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clause"):
                    opp_val = getattr(item, "Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clause"):
                    opp_val = getattr(item, "Clause", None)
                    
                    setattr(item, "Clause", self)
                    

class Activities_StructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: bool, Activities_StructuredActivities_LoopNode117: set["ExecutableNode"] = None, Activities_StructuredActivities_LoopNode120: set["ExecutableNode"] = None, Activities_StructuredActivities_LoopNode123: "OutputPin" = None, Activities_StructuredActivities_LoopNode126: set["InputPin"] = None, Activities_StructuredActivities_LoopNode129: set["OutputPin"] = None, Activities_StructuredActivities_LoopNode132: set["OutputPin"] = None, Activities_StructuredActivities_LoopNode135: set["OutputPin"] = None, Activities_StructuredActivities_LoopNode: set["ExecutableNode"] = None, StructuredActivityNode66: "Activities_BasicActivities_ActivityEdge" = None, StructuredActivityNode: "Activities_FundamentalActivities_Activity" = None, StructuredActivityNode24: "Activities_FundamentalActivities_ActivityNode" = None):
        self.isTestedFirst = isTestedFirst
        self.Activities_StructuredActivities_LoopNode117 = Activities_StructuredActivities_LoopNode117 if Activities_StructuredActivities_LoopNode117 is not None else set()
        self.Activities_StructuredActivities_LoopNode120 = Activities_StructuredActivities_LoopNode120 if Activities_StructuredActivities_LoopNode120 is not None else set()
        self.Activities_StructuredActivities_LoopNode123 = Activities_StructuredActivities_LoopNode123
        self.Activities_StructuredActivities_LoopNode126 = Activities_StructuredActivities_LoopNode126 if Activities_StructuredActivities_LoopNode126 is not None else set()
        self.Activities_StructuredActivities_LoopNode129 = Activities_StructuredActivities_LoopNode129 if Activities_StructuredActivities_LoopNode129 is not None else set()
        self.Activities_StructuredActivities_LoopNode132 = Activities_StructuredActivities_LoopNode132 if Activities_StructuredActivities_LoopNode132 is not None else set()
        self.Activities_StructuredActivities_LoopNode135 = Activities_StructuredActivities_LoopNode135 if Activities_StructuredActivities_LoopNode135 is not None else set()
        self.Activities_StructuredActivities_LoopNode = Activities_StructuredActivities_LoopNode if Activities_StructuredActivities_LoopNode is not None else set()
        
        pass
    @property
    def isTestedFirst(self):
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: bool):
        self.__isTestedFirst = isTestedFirst


    @property
    def Activities_StructuredActivities_LoopNode135(self):
        return self.__Activities_StructuredActivities_LoopNode135

    @Activities_StructuredActivities_LoopNode135.setter
    def Activities_StructuredActivities_LoopNode135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode135", None)
        self.__Activities_StructuredActivities_LoopNode135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin136"):
                    opp_val = getattr(item, "OutputPin136", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin136"):
                    opp_val = getattr(item, "OutputPin136", None)
                    
                    setattr(item, "OutputPin136", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode126(self):
        return self.__Activities_StructuredActivities_LoopNode126

    @Activities_StructuredActivities_LoopNode126.setter
    def Activities_StructuredActivities_LoopNode126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode126", None)
        self.__Activities_StructuredActivities_LoopNode126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPin127"):
                    opp_val = getattr(item, "InputPin127", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPin127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPin127"):
                    opp_val = getattr(item, "InputPin127", None)
                    
                    setattr(item, "InputPin127", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode120(self):
        return self.__Activities_StructuredActivities_LoopNode120

    @Activities_StructuredActivities_LoopNode120.setter
    def Activities_StructuredActivities_LoopNode120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode120", None)
        self.__Activities_StructuredActivities_LoopNode120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode121"):
                    opp_val = getattr(item, "ExecutableNode121", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode121"):
                    opp_val = getattr(item, "ExecutableNode121", None)
                    
                    setattr(item, "ExecutableNode121", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode129(self):
        return self.__Activities_StructuredActivities_LoopNode129

    @Activities_StructuredActivities_LoopNode129.setter
    def Activities_StructuredActivities_LoopNode129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode129", None)
        self.__Activities_StructuredActivities_LoopNode129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin130"):
                    opp_val = getattr(item, "OutputPin130", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin130"):
                    opp_val = getattr(item, "OutputPin130", None)
                    
                    setattr(item, "OutputPin130", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode117(self):
        return self.__Activities_StructuredActivities_LoopNode117

    @Activities_StructuredActivities_LoopNode117.setter
    def Activities_StructuredActivities_LoopNode117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode117", None)
        self.__Activities_StructuredActivities_LoopNode117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode118"):
                    opp_val = getattr(item, "ExecutableNode118", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode118"):
                    opp_val = getattr(item, "ExecutableNode118", None)
                    
                    setattr(item, "ExecutableNode118", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode123(self):
        return self.__Activities_StructuredActivities_LoopNode123

    @Activities_StructuredActivities_LoopNode123.setter
    def Activities_StructuredActivities_LoopNode123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode123", None)
        self.__Activities_StructuredActivities_LoopNode123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputPin124"):
                opp_val = getattr(old_value, "OutputPin124", None)
                if opp_val == self:
                    setattr(old_value, "OutputPin124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputPin124"):
                opp_val = getattr(value, "OutputPin124", None)
                setattr(value, "OutputPin124", self)

    @property
    def Activities_StructuredActivities_LoopNode(self):
        return self.__Activities_StructuredActivities_LoopNode

    @Activities_StructuredActivities_LoopNode.setter
    def Activities_StructuredActivities_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode", None)
        self.__Activities_StructuredActivities_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode"):
                    opp_val = getattr(item, "ExecutableNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode"):
                    opp_val = getattr(item, "ExecutableNode", None)
                    
                    setattr(item, "ExecutableNode", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode132(self):
        return self.__Activities_StructuredActivities_LoopNode132

    @Activities_StructuredActivities_LoopNode132.setter
    def Activities_StructuredActivities_LoopNode132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode132", None)
        self.__Activities_StructuredActivities_LoopNode132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin133"):
                    opp_val = getattr(item, "OutputPin133", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin133"):
                    opp_val = getattr(item, "OutputPin133", None)
                    
                    setattr(item, "OutputPin133", self)
                    

class Activities_StructuredActivities_SequenceNode(StructuredActivityNode):

    pass
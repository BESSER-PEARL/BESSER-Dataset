from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class InteractionOperatorKind(Enum):
    seq = "seq"
    alt = "alt"
    opt = "opt"
    break = "break"
    par = "par"
    strict = "strict"
    loop = "loop"
    critical = "critical"
    neg = "neg"
    assert = "assert"
    ignore = "ignore"
    consider = "consider"
class MessageKind(Enum):
    complete = "complete"
    lost = "lost"
    found = "found"
    unknown = "unknown"
class ConnectorKind(Enum):
    assembly = "assembly"
    delegation = "delegation"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class MessageSort(Enum):
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class ObjectNodeOrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
    FIFO = "FIFO"
class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"


############################################
# Definition of Classes
############################################

class Transition:

    pass
class uml_ProtocolTransition(Transition):

    pass
class CentralBufferNode:

    pass
class uml_DataStoreNode(CentralBufferNode):

    pass
class AcceptEventAction:

    pass
class uml_AcceptCallAction(AcceptEventAction):

    pass
class CreateLinkAction:

    pass
class uml_CreateLinkObjectAction(CreateLinkAction):

    pass
class WriteVariableAction:

    pass
class uml_RemoveVariableValueAction(WriteVariableAction):

    def __init__(self, isRemoveDuplicates: str, uml_RemoveVariableValueAction: "uml_InputPin" = None):
        self.isRemoveDuplicates = isRemoveDuplicates
        self.uml_RemoveVariableValueAction = uml_RemoveVariableValueAction
        
    @property
    def isRemoveDuplicates(self) -> str:
        return self.__isRemoveDuplicates

    @isRemoveDuplicates.setter
    def isRemoveDuplicates(self, isRemoveDuplicates: str):
        self.__isRemoveDuplicates = isRemoveDuplicates

    @property
    def uml_RemoveVariableValueAction(self):
        return self.__uml_RemoveVariableValueAction

    @uml_RemoveVariableValueAction.setter
    def uml_RemoveVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_RemoveVariableValueAction__uml_RemoveVariableValueAction", None)
        self.__uml_RemoveVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin897"):
                opp_val = getattr(old_value, "uml_InputPin897", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin897", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin897"):
                opp_val = getattr(value, "uml_InputPin897", None)
                setattr(value, "uml_InputPin897", self)

class uml_AddVariableValueAction(WriteVariableAction):

    def __init__(self, isReplaceAll: str, uml_AddVariableValueAction: "uml_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.uml_AddVariableValueAction = uml_AddVariableValueAction
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml_AddVariableValueAction(self):
        return self.__uml_AddVariableValueAction

    @uml_AddVariableValueAction.setter
    def uml_AddVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_AddVariableValueAction__uml_AddVariableValueAction", None)
        self.__uml_AddVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin895"):
                opp_val = getattr(old_value, "uml_InputPin895", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin895", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin895"):
                opp_val = getattr(value, "uml_InputPin895", None)
                setattr(value, "uml_InputPin895", self)

class State:

    pass
class uml_FinalState(State):

    pass
class Observation:

    pass
class uml_DurationObservation(Observation):

    def __init__(self, firstEvent: str, uml_DurationObservation: set["uml_NamedElement"] = None):
        self.firstEvent = firstEvent
        self.uml_DurationObservation = uml_DurationObservation if uml_DurationObservation is not None else set()
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

    @property
    def uml_DurationObservation(self):
        return self.__uml_DurationObservation

    @uml_DurationObservation.setter
    def uml_DurationObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DurationObservation__uml_DurationObservation", None)
        self.__uml_DurationObservation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_NamedElement886"):
                    opp_val = getattr(item, "uml_NamedElement886", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_NamedElement886", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_NamedElement886"):
                    opp_val = getattr(item, "uml_NamedElement886", None)
                    
                    setattr(item, "uml_NamedElement886", self)
                    

class uml_TimeObservation(Observation):

    def __init__(self, firstEvent: str, uml_TimeObservation: "uml_NamedElement" = None):
        self.firstEvent = firstEvent
        self.uml_TimeObservation = uml_TimeObservation
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

    @property
    def uml_TimeObservation(self):
        return self.__uml_TimeObservation

    @uml_TimeObservation.setter
    def uml_TimeObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_TimeObservation__uml_TimeObservation", None)
        self.__uml_TimeObservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_NamedElement884"):
                opp_val = getattr(old_value, "uml_NamedElement884", None)
                if opp_val == self:
                    setattr(old_value, "uml_NamedElement884", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_NamedElement884"):
                opp_val = getattr(value, "uml_NamedElement884", None)
                setattr(value, "uml_NamedElement884", self)

class IntervalConstraint:

    pass
class uml_DurationConstraint(IntervalConstraint):

    def __init__(self, firstEvent: str):
        self.firstEvent = firstEvent
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

class uml_TimeConstraint(IntervalConstraint):

    def __init__(self, firstEvent: str):
        self.firstEvent = firstEvent
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

class VariableAction:

    pass
class uml_ClearVariableAction(VariableAction):

    pass
class uml_WriteVariableAction(VariableAction):

    pass
class uml_ReadVariableAction(VariableAction):

    pass
class Interval:

    pass
class uml_TimeInterval(Interval):

    pass
class uml_DurationInterval(Interval):

    pass
class WriteLinkAction:

    pass
class uml_DestroyLinkAction(WriteLinkAction):

    pass
class uml_CreateLinkAction(WriteLinkAction):

    pass
class LinkEndData:

    pass
class uml_LinkEndDestructionData(LinkEndData):

    def __init__(self, isDestroyDuplicates: str, uml_LinkEndDestructionData: "uml_InputPin" = None):
        self.isDestroyDuplicates = isDestroyDuplicates
        self.uml_LinkEndDestructionData = uml_LinkEndDestructionData
        
    @property
    def isDestroyDuplicates(self) -> str:
        return self.__isDestroyDuplicates

    @isDestroyDuplicates.setter
    def isDestroyDuplicates(self, isDestroyDuplicates: str):
        self.__isDestroyDuplicates = isDestroyDuplicates

    @property
    def uml_LinkEndDestructionData(self):
        return self.__uml_LinkEndDestructionData

    @uml_LinkEndDestructionData.setter
    def uml_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LinkEndDestructionData__uml_LinkEndDestructionData", None)
        self.__uml_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin851"):
                opp_val = getattr(old_value, "uml_InputPin851", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin851", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin851"):
                opp_val = getattr(value, "uml_InputPin851", None)
                setattr(value, "uml_InputPin851", self)

class uml_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: str, uml_LinkEndCreationData: "uml_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.uml_LinkEndCreationData = uml_LinkEndCreationData
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml_LinkEndCreationData(self):
        return self.__uml_LinkEndCreationData

    @uml_LinkEndCreationData.setter
    def uml_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LinkEndCreationData__uml_LinkEndCreationData", None)
        self.__uml_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin849"):
                opp_val = getattr(old_value, "uml_InputPin849", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin849", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin849"):
                opp_val = getattr(value, "uml_InputPin849", None)
                setattr(value, "uml_InputPin849", self)

class LinkAction:

    pass
class uml_WriteLinkAction(LinkAction):

    pass
class uml_ReadLinkAction(LinkAction):

    pass
class StructuralFeatureAction:

    pass
class uml_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class uml_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class WriteStructuralFeatureAction:

    pass
class uml_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isReplaceAll: str, uml_AddStructuralFeatureValueAction: "uml_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.uml_AddStructuralFeatureValueAction = uml_AddStructuralFeatureValueAction
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml_AddStructuralFeatureValueAction(self):
        return self.__uml_AddStructuralFeatureValueAction

    @uml_AddStructuralFeatureValueAction.setter
    def uml_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_AddStructuralFeatureValueAction__uml_AddStructuralFeatureValueAction", None)
        self.__uml_AddStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin827"):
                opp_val = getattr(old_value, "uml_InputPin827", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin827", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin827"):
                opp_val = getattr(value, "uml_InputPin827", None)
                setattr(value, "uml_InputPin827", self)

class uml_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isRemoveDuplicates: str, uml_RemoveStructuralFeatureValueAction: "uml_InputPin" = None):
        self.isRemoveDuplicates = isRemoveDuplicates
        self.uml_RemoveStructuralFeatureValueAction = uml_RemoveStructuralFeatureValueAction
        
    @property
    def isRemoveDuplicates(self) -> str:
        return self.__isRemoveDuplicates

    @isRemoveDuplicates.setter
    def isRemoveDuplicates(self, isRemoveDuplicates: str):
        self.__isRemoveDuplicates = isRemoveDuplicates

    @property
    def uml_RemoveStructuralFeatureValueAction(self):
        return self.__uml_RemoveStructuralFeatureValueAction

    @uml_RemoveStructuralFeatureValueAction.setter
    def uml_RemoveStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_RemoveStructuralFeatureValueAction__uml_RemoveStructuralFeatureValueAction", None)
        self.__uml_RemoveStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin825"):
                opp_val = getattr(old_value, "uml_InputPin825", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin825", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin825"):
                opp_val = getattr(value, "uml_InputPin825", None)
                setattr(value, "uml_InputPin825", self)

class uml_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class CombinedFragment:

    pass
class uml_ConsiderIgnoreFragment(CombinedFragment):

    pass
class Node:

    pass
class uml_ExecutionEnvironment(Node):

    pass
class uml_Device(Node):

    pass
class FinalNode:

    pass
class uml_ActivityFinalNode(FinalNode):

    pass
class uml_FlowFinalNode(FinalNode):

    pass
class Event:

    pass
class uml_TimeEvent(Event):

    def __init__(self, isRelative: str, uml_TimeEvent: "uml_TimeExpression" = None):
        self.isRelative = isRelative
        self.uml_TimeEvent = uml_TimeEvent
        
    @property
    def isRelative(self) -> str:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: str):
        self.__isRelative = isRelative

    @property
    def uml_TimeEvent(self):
        return self.__uml_TimeEvent

    @uml_TimeEvent.setter
    def uml_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_TimeEvent__uml_TimeEvent", None)
        self.__uml_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_TimeExpression888"):
                opp_val = getattr(old_value, "uml_TimeExpression888", None)
                if opp_val == self:
                    setattr(old_value, "uml_TimeExpression888", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_TimeExpression888"):
                opp_val = getattr(value, "uml_TimeExpression888", None)
                setattr(value, "uml_TimeExpression888", self)

class uml_ChangeEvent(Event):

    pass
class uml_ExecutionEvent(Event):

    pass
class ExecutionSpecification:

    pass
class uml_BehaviorExecutionSpecification(ExecutionSpecification):

    pass
class uml_ActionExecutionSpecification(ExecutionSpecification):

    pass
class OccurrenceSpecification:

    pass
class uml_ExecutionOccurrenceSpecification(OccurrenceSpecification):

    pass
class uml_MessageEvent(Event):

    pass
class MessageEvent:

    pass
class uml_CallEvent(MessageEvent):

    pass
class uml_AnyReceiveEvent(MessageEvent):

    pass
class uml_ReceiveOperationEvent(MessageEvent):

    pass
class uml_SignalEvent(MessageEvent):

    pass
class uml_SendSignalEvent(MessageEvent):

    pass
class uml_ReceiveSignalEvent(MessageEvent):

    pass
class uml_SendOperationEvent(MessageEvent):

    pass
class uml_DestructionEvent(Event):

    pass
class uml_CreationEvent(Event):

    pass
class MessageEnd:

    pass
class uml_MessageOccurrenceSpecification(OccurrenceSpecification, MessageEnd):

    pass
class Constraint:

    pass
class uml_IntervalConstraint(Constraint):

    pass
class uml_InteractionConstraint(Constraint):

    pass
class InteractionUse:

    pass
class uml_PartDecomposition(InteractionUse):

    pass
class uml_Gate(MessageEnd):

    pass
class InteractionFragment:

    pass
class uml_InteractionUse(InteractionFragment):

    pass
class uml_CombinedFragment(InteractionFragment):

    def __init__(self, interactionOperator: str, uml_CombinedFragment: set["uml_InteractionOperand"] = None, uml_CombinedFragment789: set["uml_Gate"] = None):
        self.interactionOperator = interactionOperator
        self.uml_CombinedFragment = uml_CombinedFragment if uml_CombinedFragment is not None else set()
        self.uml_CombinedFragment789 = uml_CombinedFragment789 if uml_CombinedFragment789 is not None else set()
        
    @property
    def interactionOperator(self) -> str:
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator

    @property
    def uml_CombinedFragment789(self):
        return self.__uml_CombinedFragment789

    @uml_CombinedFragment789.setter
    def uml_CombinedFragment789(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_CombinedFragment__uml_CombinedFragment789", None)
        self.__uml_CombinedFragment789 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Gate790"):
                    opp_val = getattr(item, "uml_Gate790", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Gate790", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Gate790"):
                    opp_val = getattr(item, "uml_Gate790", None)
                    
                    setattr(item, "uml_Gate790", self)
                    

    @property
    def uml_CombinedFragment(self):
        return self.__uml_CombinedFragment

    @uml_CombinedFragment.setter
    def uml_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_CombinedFragment__uml_CombinedFragment", None)
        self.__uml_CombinedFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_InteractionOperand787"):
                    opp_val = getattr(item, "uml_InteractionOperand787", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_InteractionOperand787", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_InteractionOperand787"):
                    opp_val = getattr(item, "uml_InteractionOperand787", None)
                    
                    setattr(item, "uml_InteractionOperand787", self)
                    

class uml_StateInvariant(InteractionFragment):

    pass
class uml_Continuation(InteractionFragment):

    def __init__(self, setting: str):
        self.setting = setting
        
    @property
    def setting(self) -> str:
        return self.__setting

    @setting.setter
    def setting(self, setting: str):
        self.__setting = setting

class uml_ExecutionSpecification(InteractionFragment):

    pass
class uml_OccurrenceSpecification(InteractionFragment):

    pass
class CallAction:

    pass
class uml_CallBehaviorAction(CallAction):

    pass
class uml_StartObjectBehaviorAction(CallAction):

    pass
class uml_CallOperationAction(CallAction):

    pass
class InputPin:

    pass
class uml_ActionInputPin(InputPin):

    pass
class uml_ValuePin(InputPin):

    pass
class ControlNode:

    pass
class uml_MergeNode(ControlNode):

    pass
class uml_ForkNode(ControlNode):

    pass
class uml_FinalNode(ControlNode):

    pass
class uml_DecisionNode(ControlNode):

    pass
class uml_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: str, uml_JoinNode: "uml_ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.uml_JoinNode = uml_JoinNode
        
    @property
    def isCombineDuplicate(self) -> str:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: str):
        self.__isCombineDuplicate = isCombineDuplicate

    @property
    def uml_JoinNode(self):
        return self.__uml_JoinNode

    @uml_JoinNode.setter
    def uml_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_JoinNode__uml_JoinNode", None)
        self.__uml_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ValueSpecification999"):
                opp_val = getattr(old_value, "uml_ValueSpecification999", None)
                if opp_val == self:
                    setattr(old_value, "uml_ValueSpecification999", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ValueSpecification999"):
                opp_val = getattr(value, "uml_ValueSpecification999", None)
                setattr(value, "uml_ValueSpecification999", self)

class uml_InitialNode(ControlNode):

    pass
class ActivityEdge:

    pass
class uml_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: str, isMultireceive: str, uml_ObjectFlow: "uml_DecisionNode" = None, uml_ObjectFlow767: "uml_Behavior" = None, uml_ObjectFlow770: "uml_Behavior" = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.uml_ObjectFlow = uml_ObjectFlow
        self.uml_ObjectFlow767 = uml_ObjectFlow767
        self.uml_ObjectFlow770 = uml_ObjectFlow770
        
    @property
    def isMultireceive(self) -> str:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: str):
        self.__isMultireceive = isMultireceive

    @property
    def isMulticast(self) -> str:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: str):
        self.__isMulticast = isMulticast

    @property
    def uml_ObjectFlow(self):
        return self.__uml_ObjectFlow

    @uml_ObjectFlow.setter
    def uml_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ObjectFlow__uml_ObjectFlow", None)
        self.__uml_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DecisionNode765"):
                opp_val = getattr(old_value, "uml_DecisionNode765", None)
                if opp_val == self:
                    setattr(old_value, "uml_DecisionNode765", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DecisionNode765"):
                opp_val = getattr(value, "uml_DecisionNode765", None)
                setattr(value, "uml_DecisionNode765", self)

    @property
    def uml_ObjectFlow767(self):
        return self.__uml_ObjectFlow767

    @uml_ObjectFlow767.setter
    def uml_ObjectFlow767(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ObjectFlow__uml_ObjectFlow767", None)
        self.__uml_ObjectFlow767 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior768"):
                opp_val = getattr(old_value, "uml_Behavior768", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior768", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior768"):
                opp_val = getattr(value, "uml_Behavior768", None)
                setattr(value, "uml_Behavior768", self)

    @property
    def uml_ObjectFlow770(self):
        return self.__uml_ObjectFlow770

    @uml_ObjectFlow770.setter
    def uml_ObjectFlow770(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ObjectFlow__uml_ObjectFlow770", None)
        self.__uml_ObjectFlow770 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior771"):
                opp_val = getattr(old_value, "uml_Behavior771", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior771", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior771"):
                opp_val = getattr(value, "uml_Behavior771", None)
                setattr(value, "uml_Behavior771", self)

class uml_ControlFlow(ActivityEdge):

    pass
class StructuredActivityNode:

    pass
class uml_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: str, uml_LoopNode1024: set["uml_ExecutableNode"] = None, uml_LoopNode1027: "uml_OutputPin" = None, uml_LoopNode: set["uml_ExecutableNode"] = None, uml_LoopNode1030: set["uml_ExecutableNode"] = None, uml_LoopNode1033: set["uml_OutputPin"] = None, uml_LoopNode1036: set["uml_OutputPin"] = None, uml_LoopNode1039: set["uml_OutputPin"] = None, uml_LoopNode1042: set["uml_InputPin"] = None):
        self.isTestedFirst = isTestedFirst
        self.uml_LoopNode1024 = uml_LoopNode1024 if uml_LoopNode1024 is not None else set()
        self.uml_LoopNode1027 = uml_LoopNode1027
        self.uml_LoopNode = uml_LoopNode if uml_LoopNode is not None else set()
        self.uml_LoopNode1030 = uml_LoopNode1030 if uml_LoopNode1030 is not None else set()
        self.uml_LoopNode1033 = uml_LoopNode1033 if uml_LoopNode1033 is not None else set()
        self.uml_LoopNode1036 = uml_LoopNode1036 if uml_LoopNode1036 is not None else set()
        self.uml_LoopNode1039 = uml_LoopNode1039 if uml_LoopNode1039 is not None else set()
        self.uml_LoopNode1042 = uml_LoopNode1042 if uml_LoopNode1042 is not None else set()
        
    @property
    def isTestedFirst(self) -> str:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: str):
        self.__isTestedFirst = isTestedFirst

    @property
    def uml_LoopNode1039(self):
        return self.__uml_LoopNode1039

    @uml_LoopNode1039.setter
    def uml_LoopNode1039(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode1039", None)
        self.__uml_LoopNode1039 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_OutputPin1040"):
                    opp_val = getattr(item, "uml_OutputPin1040", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_OutputPin1040", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_OutputPin1040"):
                    opp_val = getattr(item, "uml_OutputPin1040", None)
                    
                    setattr(item, "uml_OutputPin1040", self)
                    

    @property
    def uml_LoopNode1033(self):
        return self.__uml_LoopNode1033

    @uml_LoopNode1033.setter
    def uml_LoopNode1033(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode1033", None)
        self.__uml_LoopNode1033 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_OutputPin1034"):
                    opp_val = getattr(item, "uml_OutputPin1034", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_OutputPin1034", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_OutputPin1034"):
                    opp_val = getattr(item, "uml_OutputPin1034", None)
                    
                    setattr(item, "uml_OutputPin1034", self)
                    

    @property
    def uml_LoopNode1036(self):
        return self.__uml_LoopNode1036

    @uml_LoopNode1036.setter
    def uml_LoopNode1036(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode1036", None)
        self.__uml_LoopNode1036 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_OutputPin1037"):
                    opp_val = getattr(item, "uml_OutputPin1037", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_OutputPin1037", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_OutputPin1037"):
                    opp_val = getattr(item, "uml_OutputPin1037", None)
                    
                    setattr(item, "uml_OutputPin1037", self)
                    

    @property
    def uml_LoopNode1027(self):
        return self.__uml_LoopNode1027

    @uml_LoopNode1027.setter
    def uml_LoopNode1027(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode1027", None)
        self.__uml_LoopNode1027 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_OutputPin1028"):
                opp_val = getattr(old_value, "uml_OutputPin1028", None)
                if opp_val == self:
                    setattr(old_value, "uml_OutputPin1028", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_OutputPin1028"):
                opp_val = getattr(value, "uml_OutputPin1028", None)
                setattr(value, "uml_OutputPin1028", self)

    @property
    def uml_LoopNode1024(self):
        return self.__uml_LoopNode1024

    @uml_LoopNode1024.setter
    def uml_LoopNode1024(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode1024", None)
        self.__uml_LoopNode1024 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ExecutableNode1025"):
                    opp_val = getattr(item, "uml_ExecutableNode1025", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ExecutableNode1025", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ExecutableNode1025"):
                    opp_val = getattr(item, "uml_ExecutableNode1025", None)
                    
                    setattr(item, "uml_ExecutableNode1025", self)
                    

    @property
    def uml_LoopNode1030(self):
        return self.__uml_LoopNode1030

    @uml_LoopNode1030.setter
    def uml_LoopNode1030(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode1030", None)
        self.__uml_LoopNode1030 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ExecutableNode1031"):
                    opp_val = getattr(item, "uml_ExecutableNode1031", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ExecutableNode1031", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ExecutableNode1031"):
                    opp_val = getattr(item, "uml_ExecutableNode1031", None)
                    
                    setattr(item, "uml_ExecutableNode1031", self)
                    

    @property
    def uml_LoopNode(self):
        return self.__uml_LoopNode

    @uml_LoopNode.setter
    def uml_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode", None)
        self.__uml_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ExecutableNode1022"):
                    opp_val = getattr(item, "uml_ExecutableNode1022", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ExecutableNode1022", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ExecutableNode1022"):
                    opp_val = getattr(item, "uml_ExecutableNode1022", None)
                    
                    setattr(item, "uml_ExecutableNode1022", self)
                    

    @property
    def uml_LoopNode1042(self):
        return self.__uml_LoopNode1042

    @uml_LoopNode1042.setter
    def uml_LoopNode1042(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_LoopNode__uml_LoopNode1042", None)
        self.__uml_LoopNode1042 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_InputPin1043"):
                    opp_val = getattr(item, "uml_InputPin1043", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_InputPin1043", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_InputPin1043"):
                    opp_val = getattr(item, "uml_InputPin1043", None)
                    
                    setattr(item, "uml_InputPin1043", self)
                    

class uml_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: str, isAssured: str, uml_ConditionalNode: set["uml_Clause"] = None, uml_ConditionalNode1002: set["uml_OutputPin"] = None):
        self.isDeterminate = isDeterminate
        self.isAssured = isAssured
        self.uml_ConditionalNode = uml_ConditionalNode if uml_ConditionalNode is not None else set()
        self.uml_ConditionalNode1002 = uml_ConditionalNode1002 if uml_ConditionalNode1002 is not None else set()
        
    @property
    def isDeterminate(self) -> str:
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: str):
        self.__isDeterminate = isDeterminate

    @property
    def isAssured(self) -> str:
        return self.__isAssured

    @isAssured.setter
    def isAssured(self, isAssured: str):
        self.__isAssured = isAssured

    @property
    def uml_ConditionalNode(self):
        return self.__uml_ConditionalNode

    @uml_ConditionalNode.setter
    def uml_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ConditionalNode__uml_ConditionalNode", None)
        self.__uml_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Clause"):
                    opp_val = getattr(item, "uml_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Clause"):
                    opp_val = getattr(item, "uml_Clause", None)
                    
                    setattr(item, "uml_Clause", self)
                    

    @property
    def uml_ConditionalNode1002(self):
        return self.__uml_ConditionalNode1002

    @uml_ConditionalNode1002.setter
    def uml_ConditionalNode1002(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ConditionalNode__uml_ConditionalNode1002", None)
        self.__uml_ConditionalNode1002 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_OutputPin1003"):
                    opp_val = getattr(item, "uml_OutputPin1003", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_OutputPin1003", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_OutputPin1003"):
                    opp_val = getattr(item, "uml_OutputPin1003", None)
                    
                    setattr(item, "uml_OutputPin1003", self)
                    

class uml_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, ExpansionRegion: "uml_ExpansionNode" = None, ExpansionRegion1046: "uml_ExpansionNode" = None, regionAsInput: set["uml_ExpansionNode"] = None, regionAsOutput: set["uml_ExpansionNode"] = None):
        self.mode = mode
        self.ExpansionRegion = ExpansionRegion
        self.ExpansionRegion1046 = ExpansionRegion1046
        self.regionAsInput = regionAsInput if regionAsInput is not None else set()
        self.regionAsOutput = regionAsOutput if regionAsOutput is not None else set()
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def ExpansionRegion1046(self):
        return self.__ExpansionRegion1046

    @ExpansionRegion1046.setter
    def ExpansionRegion1046(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ExpansionRegion__ExpansionRegion1046", None)
        self.__ExpansionRegion1046 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputElement"):
                opp_val = getattr(old_value, "inputElement", None)
                if opp_val == self:
                    setattr(old_value, "inputElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputElement"):
                opp_val = getattr(value, "inputElement", None)
                setattr(value, "inputElement", self)

    @property
    def ExpansionRegion(self):
        return self.__ExpansionRegion

    @ExpansionRegion.setter
    def ExpansionRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ExpansionRegion__ExpansionRegion", None)
        self.__ExpansionRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputElement"):
                opp_val = getattr(old_value, "outputElement", None)
                if opp_val == self:
                    setattr(old_value, "outputElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputElement"):
                opp_val = getattr(value, "outputElement", None)
                setattr(value, "outputElement", self)

    @property
    def regionAsOutput(self):
        return self.__regionAsOutput

    @regionAsOutput.setter
    def regionAsOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ExpansionRegion__regionAsOutput", None)
        self.__regionAsOutput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpansionNode1049"):
                    opp_val = getattr(item, "ExpansionNode1049", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode1049", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode1049"):
                    opp_val = getattr(item, "ExpansionNode1049", None)
                    
                    setattr(item, "ExpansionNode1049", self)
                    

    @property
    def regionAsInput(self):
        return self.__regionAsInput

    @regionAsInput.setter
    def regionAsInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ExpansionRegion__regionAsInput", None)
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
                    

class uml_SequenceNode(StructuredActivityNode):

    pass
class InvocationAction:

    pass
class uml_SendSignalAction(InvocationAction):

    pass
class uml_SendObjectAction(InvocationAction):

    pass
class uml_BroadcastSignalAction(InvocationAction):

    pass
class uml_CallAction(InvocationAction):

    def __init__(self, isSynchronous: str, uml_CallAction: set["uml_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.uml_CallAction = uml_CallAction if uml_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> str:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: str):
        self.__isSynchronous = isSynchronous

    @property
    def uml_CallAction(self):
        return self.__uml_CallAction

    @uml_CallAction.setter
    def uml_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_CallAction__uml_CallAction", None)
        self.__uml_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_OutputPin643"):
                    opp_val = getattr(item, "uml_OutputPin643", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_OutputPin643", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_OutputPin643"):
                    opp_val = getattr(item, "uml_OutputPin643", None)
                    
                    setattr(item, "uml_OutputPin643", self)
                    

class ObjectNode:

    pass
class uml_CentralBufferNode(ObjectNode):

    pass
class uml_ActivityParameterNode(ObjectNode):

    pass
class uml_ExpansionNode(ObjectNode):

    pass
class Pin:

    pass
class ActivityGroup:

    pass
class ExecutableNode:

    pass
class uml_Action(ExecutableNode):

    pass
class uml_InterruptibleActivityRegion(ActivityGroup):

    pass
class ActivityNode:

    pass
class uml_ControlNode(ActivityNode):

    pass
class uml_ExecutableNode(ActivityNode):

    pass
class LiteralSpecification:

    pass
class uml_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class uml_LiteralInteger(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class uml_OutputPin(Pin):

    pass
class uml_InputPin(Pin):

    pass
class Action:

    pass
class uml_RaiseExceptionAction(Action):

    pass
class uml_TestIdentityAction(Action):

    pass
class uml_AcceptEventAction(Action):

    def __init__(self, isUnmarshall: str, uml_AcceptEventAction: set["uml_OutputPin"] = None, uml_AcceptEventAction968: set["uml_Trigger"] = None):
        self.isUnmarshall = isUnmarshall
        self.uml_AcceptEventAction = uml_AcceptEventAction if uml_AcceptEventAction is not None else set()
        self.uml_AcceptEventAction968 = uml_AcceptEventAction968 if uml_AcceptEventAction968 is not None else set()
        
    @property
    def isUnmarshall(self) -> str:
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: str):
        self.__isUnmarshall = isUnmarshall

    @property
    def uml_AcceptEventAction(self):
        return self.__uml_AcceptEventAction

    @uml_AcceptEventAction.setter
    def uml_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_AcceptEventAction__uml_AcceptEventAction", None)
        self.__uml_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_OutputPin966"):
                    opp_val = getattr(item, "uml_OutputPin966", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_OutputPin966", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_OutputPin966"):
                    opp_val = getattr(item, "uml_OutputPin966", None)
                    
                    setattr(item, "uml_OutputPin966", self)
                    

    @property
    def uml_AcceptEventAction968(self):
        return self.__uml_AcceptEventAction968

    @uml_AcceptEventAction968.setter
    def uml_AcceptEventAction968(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_AcceptEventAction__uml_AcceptEventAction968", None)
        self.__uml_AcceptEventAction968 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Trigger969"):
                    opp_val = getattr(item, "uml_Trigger969", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Trigger969", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Trigger969"):
                    opp_val = getattr(item, "uml_Trigger969", None)
                    
                    setattr(item, "uml_Trigger969", self)
                    

class uml_CreateObjectAction(Action):

    pass
class uml_ValueSpecificationAction(Action):

    pass
class uml_InvocationAction(Action):

    pass
class uml_ReadLinkObjectEndQualifierAction(Action):

    pass
class uml_DestroyObjectAction(Action):

    def __init__(self, isDestroyLinks: str, isDestroyOwnedObjects: str, uml_DestroyObjectAction: "uml_InputPin" = None):
        self.isDestroyLinks = isDestroyLinks
        self.isDestroyOwnedObjects = isDestroyOwnedObjects
        self.uml_DestroyObjectAction = uml_DestroyObjectAction
        
    @property
    def isDestroyOwnedObjects(self) -> str:
        return self.__isDestroyOwnedObjects

    @isDestroyOwnedObjects.setter
    def isDestroyOwnedObjects(self, isDestroyOwnedObjects: str):
        self.__isDestroyOwnedObjects = isDestroyOwnedObjects

    @property
    def isDestroyLinks(self) -> str:
        return self.__isDestroyLinks

    @isDestroyLinks.setter
    def isDestroyLinks(self, isDestroyLinks: str):
        self.__isDestroyLinks = isDestroyLinks

    @property
    def uml_DestroyObjectAction(self):
        return self.__uml_DestroyObjectAction

    @uml_DestroyObjectAction.setter
    def uml_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DestroyObjectAction__uml_DestroyObjectAction", None)
        self.__uml_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin799"):
                opp_val = getattr(old_value, "uml_InputPin799", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin799", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin799"):
                opp_val = getattr(value, "uml_InputPin799", None)
                setattr(value, "uml_InputPin799", self)

class uml_StartClassifierBehaviorAction(Action):

    pass
class uml_ClearAssociationAction(Action):

    pass
class uml_ReadSelfAction(Action):

    pass
class uml_StructuralFeatureAction(Action):

    pass
class uml_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: str, uml_ReclassifyObjectAction: set["uml_Classifier"] = None, uml_ReclassifyObjectAction932: set["uml_Classifier"] = None, uml_ReclassifyObjectAction935: "uml_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.uml_ReclassifyObjectAction = uml_ReclassifyObjectAction if uml_ReclassifyObjectAction is not None else set()
        self.uml_ReclassifyObjectAction932 = uml_ReclassifyObjectAction932 if uml_ReclassifyObjectAction932 is not None else set()
        self.uml_ReclassifyObjectAction935 = uml_ReclassifyObjectAction935
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml_ReclassifyObjectAction935(self):
        return self.__uml_ReclassifyObjectAction935

    @uml_ReclassifyObjectAction935.setter
    def uml_ReclassifyObjectAction935(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReclassifyObjectAction__uml_ReclassifyObjectAction935", None)
        self.__uml_ReclassifyObjectAction935 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin936"):
                opp_val = getattr(old_value, "uml_InputPin936", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin936", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin936"):
                opp_val = getattr(value, "uml_InputPin936", None)
                setattr(value, "uml_InputPin936", self)

    @property
    def uml_ReclassifyObjectAction932(self):
        return self.__uml_ReclassifyObjectAction932

    @uml_ReclassifyObjectAction932.setter
    def uml_ReclassifyObjectAction932(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReclassifyObjectAction__uml_ReclassifyObjectAction932", None)
        self.__uml_ReclassifyObjectAction932 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier933"):
                    opp_val = getattr(item, "uml_Classifier933", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier933", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier933"):
                    opp_val = getattr(item, "uml_Classifier933", None)
                    
                    setattr(item, "uml_Classifier933", self)
                    

    @property
    def uml_ReclassifyObjectAction(self):
        return self.__uml_ReclassifyObjectAction

    @uml_ReclassifyObjectAction.setter
    def uml_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReclassifyObjectAction__uml_ReclassifyObjectAction", None)
        self.__uml_ReclassifyObjectAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier930"):
                    opp_val = getattr(item, "uml_Classifier930", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier930", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier930"):
                    opp_val = getattr(item, "uml_Classifier930", None)
                    
                    setattr(item, "uml_Classifier930", self)
                    

class uml_ReadExtentAction(Action):

    pass
class uml_LinkAction(Action):

    pass
class uml_ReadIsClassifiedObjectAction(Action):

    def __init__(self, isDirect: str, uml_ReadIsClassifiedObjectAction: "uml_Classifier" = None, uml_ReadIsClassifiedObjectAction940: "uml_OutputPin" = None, uml_ReadIsClassifiedObjectAction943: "uml_InputPin" = None):
        self.isDirect = isDirect
        self.uml_ReadIsClassifiedObjectAction = uml_ReadIsClassifiedObjectAction
        self.uml_ReadIsClassifiedObjectAction940 = uml_ReadIsClassifiedObjectAction940
        self.uml_ReadIsClassifiedObjectAction943 = uml_ReadIsClassifiedObjectAction943
        
    @property
    def isDirect(self) -> str:
        return self.__isDirect

    @isDirect.setter
    def isDirect(self, isDirect: str):
        self.__isDirect = isDirect

    @property
    def uml_ReadIsClassifiedObjectAction940(self):
        return self.__uml_ReadIsClassifiedObjectAction940

    @uml_ReadIsClassifiedObjectAction940.setter
    def uml_ReadIsClassifiedObjectAction940(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReadIsClassifiedObjectAction__uml_ReadIsClassifiedObjectAction940", None)
        self.__uml_ReadIsClassifiedObjectAction940 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_OutputPin941"):
                opp_val = getattr(old_value, "uml_OutputPin941", None)
                if opp_val == self:
                    setattr(old_value, "uml_OutputPin941", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_OutputPin941"):
                opp_val = getattr(value, "uml_OutputPin941", None)
                setattr(value, "uml_OutputPin941", self)

    @property
    def uml_ReadIsClassifiedObjectAction943(self):
        return self.__uml_ReadIsClassifiedObjectAction943

    @uml_ReadIsClassifiedObjectAction943.setter
    def uml_ReadIsClassifiedObjectAction943(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReadIsClassifiedObjectAction__uml_ReadIsClassifiedObjectAction943", None)
        self.__uml_ReadIsClassifiedObjectAction943 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin944"):
                opp_val = getattr(old_value, "uml_InputPin944", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin944", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin944"):
                opp_val = getattr(value, "uml_InputPin944", None)
                setattr(value, "uml_InputPin944", self)

    @property
    def uml_ReadIsClassifiedObjectAction(self):
        return self.__uml_ReadIsClassifiedObjectAction

    @uml_ReadIsClassifiedObjectAction.setter
    def uml_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReadIsClassifiedObjectAction__uml_ReadIsClassifiedObjectAction", None)
        self.__uml_ReadIsClassifiedObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier938"):
                opp_val = getattr(old_value, "uml_Classifier938", None)
                if opp_val == self:
                    setattr(old_value, "uml_Classifier938", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier938"):
                opp_val = getattr(value, "uml_Classifier938", None)
                setattr(value, "uml_Classifier938", self)

class uml_ReduceAction(Action):

    def __init__(self, isOrdered: str, uml_ReduceAction: "uml_Behavior" = None, uml_ReduceAction991: "uml_OutputPin" = None, uml_ReduceAction994: "uml_InputPin" = None):
        self.isOrdered = isOrdered
        self.uml_ReduceAction = uml_ReduceAction
        self.uml_ReduceAction991 = uml_ReduceAction991
        self.uml_ReduceAction994 = uml_ReduceAction994
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def uml_ReduceAction994(self):
        return self.__uml_ReduceAction994

    @uml_ReduceAction994.setter
    def uml_ReduceAction994(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReduceAction__uml_ReduceAction994", None)
        self.__uml_ReduceAction994 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InputPin995"):
                opp_val = getattr(old_value, "uml_InputPin995", None)
                if opp_val == self:
                    setattr(old_value, "uml_InputPin995", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InputPin995"):
                opp_val = getattr(value, "uml_InputPin995", None)
                setattr(value, "uml_InputPin995", self)

    @property
    def uml_ReduceAction(self):
        return self.__uml_ReduceAction

    @uml_ReduceAction.setter
    def uml_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReduceAction__uml_ReduceAction", None)
        self.__uml_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior989"):
                opp_val = getattr(old_value, "uml_Behavior989", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior989", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior989"):
                opp_val = getattr(value, "uml_Behavior989", None)
                setattr(value, "uml_Behavior989", self)

    @property
    def uml_ReduceAction991(self):
        return self.__uml_ReduceAction991

    @uml_ReduceAction991.setter
    def uml_ReduceAction991(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ReduceAction__uml_ReduceAction991", None)
        self.__uml_ReduceAction991 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_OutputPin992"):
                opp_val = getattr(old_value, "uml_OutputPin992", None)
                if opp_val == self:
                    setattr(old_value, "uml_OutputPin992", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_OutputPin992"):
                opp_val = getattr(value, "uml_OutputPin992", None)
                setattr(value, "uml_OutputPin992", self)

class uml_ReadLinkObjectEndAction(Action):

    pass
class uml_ReplyAction(Action):

    pass
class uml_VariableAction(Action):

    pass
class uml_UnmarshallAction(Action):

    pass
class uml_OpaqueAction(Action):

    def __init__(self, body: str, language: str, uml_OpaqueAction: set["uml_InputPin"] = None, uml_OpaqueAction520: set["uml_OutputPin"] = None):
        self.body = body
        self.language = language
        self.uml_OpaqueAction = uml_OpaqueAction if uml_OpaqueAction is not None else set()
        self.uml_OpaqueAction520 = uml_OpaqueAction520 if uml_OpaqueAction520 is not None else set()
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def uml_OpaqueAction520(self):
        return self.__uml_OpaqueAction520

    @uml_OpaqueAction520.setter
    def uml_OpaqueAction520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_OpaqueAction__uml_OpaqueAction520", None)
        self.__uml_OpaqueAction520 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_OutputPin"):
                    opp_val = getattr(item, "uml_OutputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_OutputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_OutputPin"):
                    opp_val = getattr(item, "uml_OutputPin", None)
                    
                    setattr(item, "uml_OutputPin", self)
                    

    @property
    def uml_OpaqueAction(self):
        return self.__uml_OpaqueAction

    @uml_OpaqueAction.setter
    def uml_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_OpaqueAction__uml_OpaqueAction", None)
        self.__uml_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_InputPin"):
                    opp_val = getattr(item, "uml_InputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_InputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_InputPin"):
                    opp_val = getattr(item, "uml_InputPin", None)
                    
                    setattr(item, "uml_InputPin", self)
                    

class OpaqueBehavior:

    pass
class uml_FunctionBehavior(OpaqueBehavior):

    pass
class uml_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class uml_LiteralNull(LiteralSpecification):

    pass
class uml_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class InstanceSpecification:

    pass
class uml_EnumerationLiteral(InstanceSpecification):

    pass
class DataType:

    pass
class uml_PrimitiveType(DataType):

    pass
class uml_Enumeration(DataType):

    pass
class TemplateSignature:

    pass
class Expression:

    pass
class Package:

    pass
class uml_Model(Package):

    def __init__(self, viewpoint: str):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> str:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: str):
        self.__viewpoint = viewpoint

class uml_Profile(Package):

    pass
class TemplateParameter:

    pass
class uml_ClassifierTemplateParameter(TemplateParameter):

    def __init__(self, allowSubstitutable: str, uml_ClassifierTemplateParameter: set["uml_Classifier"] = None):
        self.allowSubstitutable = allowSubstitutable
        self.uml_ClassifierTemplateParameter = uml_ClassifierTemplateParameter if uml_ClassifierTemplateParameter is not None else set()
        
    @property
    def allowSubstitutable(self) -> str:
        return self.__allowSubstitutable

    @allowSubstitutable.setter
    def allowSubstitutable(self, allowSubstitutable: str):
        self.__allowSubstitutable = allowSubstitutable

    @property
    def uml_ClassifierTemplateParameter(self):
        return self.__uml_ClassifierTemplateParameter

    @uml_ClassifierTemplateParameter.setter
    def uml_ClassifierTemplateParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ClassifierTemplateParameter__uml_ClassifierTemplateParameter", None)
        self.__uml_ClassifierTemplateParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier487"):
                    opp_val = getattr(item, "uml_Classifier487", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier487", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier487"):
                    opp_val = getattr(item, "uml_Classifier487", None)
                    
                    setattr(item, "uml_Classifier487", self)
                    

class uml_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class uml_OperationTemplateParameter(TemplateParameter):

    pass
class Association:

    pass
class uml_CommunicationPath(Association):

    pass
class StructuredClassifier:

    pass
class uml_EncapsulatedClassifier(StructuredClassifier):

    pass
class Vertex:

    pass
class uml_ConnectionPointReference(Vertex):

    pass
class Property:

    pass
class uml_ExtensionEnd(Property):

    pass
class uml_Port(Property):

    def __init__(self, isBehavior: str, isService: str, uml_Port: "uml_Trigger" = None, uml_Port353: set["uml_Interface"] = None, uml_Port357: "uml_Port" = None, uml_Port355: set["uml_Port"] = None, uml_Port359: set["uml_Interface"] = None, uml_Port362: "uml_ProtocolStateMachine" = None, uml_Port405: "uml_EncapsulatedClassifier" = None, uml_Port648: "uml_InvocationAction" = None):
        self.isBehavior = isBehavior
        self.isService = isService
        self.uml_Port = uml_Port
        self.uml_Port353 = uml_Port353 if uml_Port353 is not None else set()
        self.uml_Port357 = uml_Port357
        self.uml_Port355 = uml_Port355 if uml_Port355 is not None else set()
        self.uml_Port359 = uml_Port359 if uml_Port359 is not None else set()
        self.uml_Port362 = uml_Port362
        self.uml_Port405 = uml_Port405
        self.uml_Port648 = uml_Port648
        
    @property
    def isBehavior(self) -> str:
        return self.__isBehavior

    @isBehavior.setter
    def isBehavior(self, isBehavior: str):
        self.__isBehavior = isBehavior

    @property
    def isService(self) -> str:
        return self.__isService

    @isService.setter
    def isService(self, isService: str):
        self.__isService = isService

    @property
    def uml_Port355(self):
        return self.__uml_Port355

    @uml_Port355.setter
    def uml_Port355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port355", None)
        self.__uml_Port355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Port357"):
                    opp_val = getattr(item, "uml_Port357", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Port357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Port357"):
                    opp_val = getattr(item, "uml_Port357", None)
                    
                    setattr(item, "uml_Port357", self)
                    

    @property
    def uml_Port357(self):
        return self.__uml_Port357

    @uml_Port357.setter
    def uml_Port357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port357", None)
        self.__uml_Port357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Port355"):
                opp_val = getattr(old_value, "uml_Port355", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Port355"):
                opp_val = getattr(value, "uml_Port355", None)
                if opp_val is None:
                    setattr(value, "uml_Port355", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Port648(self):
        return self.__uml_Port648

    @uml_Port648.setter
    def uml_Port648(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port648", None)
        self.__uml_Port648 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InvocationAction647"):
                opp_val = getattr(old_value, "uml_InvocationAction647", None)
                if opp_val == self:
                    setattr(old_value, "uml_InvocationAction647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InvocationAction647"):
                opp_val = getattr(value, "uml_InvocationAction647", None)
                setattr(value, "uml_InvocationAction647", self)

    @property
    def uml_Port405(self):
        return self.__uml_Port405

    @uml_Port405.setter
    def uml_Port405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port405", None)
        self.__uml_Port405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_EncapsulatedClassifier"):
                opp_val = getattr(old_value, "uml_EncapsulatedClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_EncapsulatedClassifier"):
                opp_val = getattr(value, "uml_EncapsulatedClassifier", None)
                if opp_val is None:
                    setattr(value, "uml_EncapsulatedClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Port362(self):
        return self.__uml_Port362

    @uml_Port362.setter
    def uml_Port362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port362", None)
        self.__uml_Port362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ProtocolStateMachine363"):
                opp_val = getattr(old_value, "uml_ProtocolStateMachine363", None)
                if opp_val == self:
                    setattr(old_value, "uml_ProtocolStateMachine363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ProtocolStateMachine363"):
                opp_val = getattr(value, "uml_ProtocolStateMachine363", None)
                setattr(value, "uml_ProtocolStateMachine363", self)

    @property
    def uml_Port(self):
        return self.__uml_Port

    @uml_Port.setter
    def uml_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port", None)
        self.__uml_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Trigger351"):
                opp_val = getattr(old_value, "uml_Trigger351", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Trigger351"):
                opp_val = getattr(value, "uml_Trigger351", None)
                if opp_val is None:
                    setattr(value, "uml_Trigger351", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Port353(self):
        return self.__uml_Port353

    @uml_Port353.setter
    def uml_Port353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port353", None)
        self.__uml_Port353 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Interface354"):
                    opp_val = getattr(item, "uml_Interface354", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Interface354", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Interface354"):
                    opp_val = getattr(item, "uml_Interface354", None)
                    
                    setattr(item, "uml_Interface354", self)
                    

    @property
    def uml_Port359(self):
        return self.__uml_Port359

    @uml_Port359.setter
    def uml_Port359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Port__uml_Port359", None)
        self.__uml_Port359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Interface360"):
                    opp_val = getattr(item, "uml_Interface360", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Interface360", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Interface360"):
                    opp_val = getattr(item, "uml_Interface360", None)
                    
                    setattr(item, "uml_Interface360", self)
                    

class uml_Pseudostate(Vertex):

    def __init__(self, kind: str, Pseudostate: "uml_StateMachine" = None, Pseudostate369: "uml_State" = None, connectionPoint: "uml_StateMachine" = None, connectionPoint399: "uml_State" = None, uml_Pseudostate: "uml_ConnectionPointReference" = None, uml_Pseudostate393: "uml_ConnectionPointReference" = None):
        self.kind = kind
        self.Pseudostate = Pseudostate
        self.Pseudostate369 = Pseudostate369
        self.connectionPoint = connectionPoint
        self.connectionPoint399 = connectionPoint399
        self.uml_Pseudostate = uml_Pseudostate
        self.uml_Pseudostate393 = uml_Pseudostate393
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def uml_Pseudostate393(self):
        return self.__uml_Pseudostate393

    @uml_Pseudostate393.setter
    def uml_Pseudostate393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Pseudostate__uml_Pseudostate393", None)
        self.__uml_Pseudostate393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ConnectionPointReference392"):
                opp_val = getattr(old_value, "uml_ConnectionPointReference392", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ConnectionPointReference392"):
                opp_val = getattr(value, "uml_ConnectionPointReference392", None)
                if opp_val is None:
                    setattr(value, "uml_ConnectionPointReference392", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Pseudostate(self):
        return self.__uml_Pseudostate

    @uml_Pseudostate.setter
    def uml_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Pseudostate__uml_Pseudostate", None)
        self.__uml_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ConnectionPointReference"):
                opp_val = getattr(old_value, "uml_ConnectionPointReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ConnectionPointReference"):
                opp_val = getattr(value, "uml_ConnectionPointReference", None)
                if opp_val is None:
                    setattr(value, "uml_ConnectionPointReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Pseudostate369(self):
        return self.__Pseudostate369

    @Pseudostate369.setter
    def Pseudostate369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Pseudostate__Pseudostate369", None)
        self.__Pseudostate369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state368"):
                opp_val = getattr(old_value, "state368", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state368"):
                opp_val = getattr(value, "state368", None)
                if opp_val is None:
                    setattr(value, "state368", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connectionPoint(self):
        return self.__connectionPoint

    @connectionPoint.setter
    def connectionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Pseudostate__connectionPoint", None)
        self.__connectionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine397"):
                opp_val = getattr(old_value, "StateMachine397", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine397"):
                opp_val = getattr(value, "StateMachine397", None)
                setattr(value, "StateMachine397", self)

    @property
    def Pseudostate(self):
        return self.__Pseudostate

    @Pseudostate.setter
    def Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Pseudostate__Pseudostate", None)
        self.__Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine310"):
                opp_val = getattr(old_value, "stateMachine310", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine310"):
                opp_val = getattr(value, "stateMachine310", None)
                if opp_val is None:
                    setattr(value, "stateMachine310", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connectionPoint399(self):
        return self.__connectionPoint399

    @connectionPoint399.setter
    def connectionPoint399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Pseudostate__connectionPoint399", None)
        self.__connectionPoint399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State400"):
                opp_val = getattr(old_value, "State400", None)
                if opp_val == self:
                    setattr(old_value, "State400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State400"):
                opp_val = getattr(value, "State400", None)
                setattr(value, "State400", self)

class Behavior:

    pass
class uml_Interaction(InteractionFragment, Behavior):

    pass
class uml_Activity(Behavior):

    def __init__(self, isReadOnly: str, isSingleExecution: str, Activity: "uml_ActivityNode" = None, Activity561: "uml_ActivityGroup" = None, uml_Activity: set["uml_StructuredActivityNode"] = None, inActivity: set["uml_ActivityGroup"] = None, Activity583: "uml_Variable" = None, activityScope: set["uml_Variable"] = None, activity: set["uml_ActivityNode"] = None, activity573: set["uml_ActivityEdge"] = None, uml_Activity576: set["uml_ActivityPartition"] = None, Activity607: "uml_ActivityEdge" = None):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.Activity = Activity
        self.Activity561 = Activity561
        self.uml_Activity = uml_Activity if uml_Activity is not None else set()
        self.inActivity = inActivity if inActivity is not None else set()
        self.Activity583 = Activity583
        self.activityScope = activityScope if activityScope is not None else set()
        self.activity = activity if activity is not None else set()
        self.activity573 = activity573 if activity573 is not None else set()
        self.uml_Activity576 = uml_Activity576 if uml_Activity576 is not None else set()
        self.Activity607 = Activity607
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def isSingleExecution(self) -> str:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: str):
        self.__isSingleExecution = isSingleExecution

    @property
    def uml_Activity(self):
        return self.__uml_Activity

    @uml_Activity.setter
    def uml_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__uml_Activity", None)
        self.__uml_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_StructuredActivityNode"):
                    opp_val = getattr(item, "uml_StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_StructuredActivityNode"):
                    opp_val = getattr(item, "uml_StructuredActivityNode", None)
                    
                    setattr(item, "uml_StructuredActivityNode", self)
                    

    @property
    def inActivity(self):
        return self.__inActivity

    @inActivity.setter
    def inActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__inActivity", None)
        self.__inActivity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityGroup578"):
                    opp_val = getattr(item, "ActivityGroup578", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityGroup578", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityGroup578"):
                    opp_val = getattr(item, "ActivityGroup578", None)
                    
                    setattr(item, "ActivityGroup578", self)
                    

    @property
    def activity573(self):
        return self.__activity573

    @activity573.setter
    def activity573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__activity573", None)
        self.__activity573 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge574"):
                    opp_val = getattr(item, "ActivityEdge574", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge574", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge574"):
                    opp_val = getattr(item, "ActivityEdge574", None)
                    
                    setattr(item, "ActivityEdge574", self)
                    

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node538"):
                opp_val = getattr(old_value, "node538", None)
                if opp_val == self:
                    setattr(old_value, "node538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node538"):
                opp_val = getattr(value, "node538", None)
                setattr(value, "node538", self)

    @property
    def Activity583(self):
        return self.__Activity583

    @Activity583.setter
    def Activity583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__Activity583", None)
        self.__Activity583 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variable582"):
                opp_val = getattr(old_value, "variable582", None)
                if opp_val == self:
                    setattr(old_value, "variable582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variable582"):
                opp_val = getattr(value, "variable582", None)
                setattr(value, "variable582", self)

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode571"):
                    opp_val = getattr(item, "ActivityNode571", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode571", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode571"):
                    opp_val = getattr(item, "ActivityNode571", None)
                    
                    setattr(item, "ActivityNode571", self)
                    

    @property
    def uml_Activity576(self):
        return self.__uml_Activity576

    @uml_Activity576.setter
    def uml_Activity576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__uml_Activity576", None)
        self.__uml_Activity576 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ActivityPartition"):
                    opp_val = getattr(item, "uml_ActivityPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ActivityPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ActivityPartition"):
                    opp_val = getattr(item, "uml_ActivityPartition", None)
                    
                    setattr(item, "uml_ActivityPartition", self)
                    

    @property
    def Activity561(self):
        return self.__Activity561

    @Activity561.setter
    def Activity561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__Activity561", None)
        self.__Activity561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group"):
                opp_val = getattr(old_value, "group", None)
                if opp_val == self:
                    setattr(old_value, "group", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group"):
                opp_val = getattr(value, "group", None)
                setattr(value, "group", self)

    @property
    def activityScope(self):
        return self.__activityScope

    @activityScope.setter
    def activityScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__activityScope", None)
        self.__activityScope = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable569"):
                    opp_val = getattr(item, "Variable569", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable569", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable569"):
                    opp_val = getattr(item, "Variable569", None)
                    
                    setattr(item, "Variable569", self)
                    

    @property
    def Activity607(self):
        return self.__Activity607

    @Activity607.setter
    def Activity607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Activity__Activity607", None)
        self.__Activity607 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edge606"):
                opp_val = getattr(old_value, "edge606", None)
                if opp_val == self:
                    setattr(old_value, "edge606", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edge606"):
                opp_val = getattr(value, "edge606", None)
                setattr(value, "edge606", self)

class uml_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class uml_StateMachine(Behavior):

    pass
class StateMachine:

    pass
class uml_ProtocolStateMachine(StateMachine):

    pass
class uml_Extension(Association):

    def __init__(self, isRequired: str, Extension: "uml_Class" = None, extension: "uml_Class" = None):
        self.isRequired = isRequired
        self.Extension = Extension
        self.extension = extension
        
    @property
    def isRequired(self) -> str:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: str):
        self.__isRequired = isRequired

    @property
    def Extension(self):
        return self.__Extension

    @Extension.setter
    def Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Extension__Extension", None)
        self.__Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaclass"):
                opp_val = getattr(old_value, "metaclass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaclass"):
                opp_val = getattr(value, "metaclass", None)
                if opp_val is None:
                    setattr(value, "metaclass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Extension__extension", None)
        self.__extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class429"):
                opp_val = getattr(old_value, "Class429", None)
                if opp_val == self:
                    setattr(old_value, "Class429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class429"):
                opp_val = getattr(value, "Class429", None)
                setattr(value, "Class429", self)

class BehavioredClassifier:

    pass
class uml_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class uml_Actor(BehavioredClassifier):

    pass
class EncapsulatedClassifier:

    pass
class Feature:

    pass
class uml_Connector(Feature):

    def __init__(self, kind: str, uml_Connector421: "uml_Connector" = None, uml_Connector419: set["uml_Connector"] = None, uml_Connector423: set["uml_ConnectorEnd"] = None, uml_Connector426: set["uml_Behavior"] = None, uml_Connector: "uml_StructuredClassifier" = None, uml_Connector417: "uml_Association" = None, uml_Connector673: "uml_Message" = None, uml_Connector920: "uml_InformationFlow" = None):
        self.kind = kind
        self.uml_Connector421 = uml_Connector421
        self.uml_Connector419 = uml_Connector419 if uml_Connector419 is not None else set()
        self.uml_Connector423 = uml_Connector423 if uml_Connector423 is not None else set()
        self.uml_Connector426 = uml_Connector426 if uml_Connector426 is not None else set()
        self.uml_Connector = uml_Connector
        self.uml_Connector417 = uml_Connector417
        self.uml_Connector673 = uml_Connector673
        self.uml_Connector920 = uml_Connector920
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def uml_Connector421(self):
        return self.__uml_Connector421

    @uml_Connector421.setter
    def uml_Connector421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector421", None)
        self.__uml_Connector421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Connector419"):
                opp_val = getattr(old_value, "uml_Connector419", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Connector419"):
                opp_val = getattr(value, "uml_Connector419", None)
                if opp_val is None:
                    setattr(value, "uml_Connector419", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Connector(self):
        return self.__uml_Connector

    @uml_Connector.setter
    def uml_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector", None)
        self.__uml_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_StructuredClassifier415"):
                opp_val = getattr(old_value, "uml_StructuredClassifier415", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_StructuredClassifier415"):
                opp_val = getattr(value, "uml_StructuredClassifier415", None)
                if opp_val is None:
                    setattr(value, "uml_StructuredClassifier415", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Connector419(self):
        return self.__uml_Connector419

    @uml_Connector419.setter
    def uml_Connector419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector419", None)
        self.__uml_Connector419 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Connector421"):
                    opp_val = getattr(item, "uml_Connector421", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Connector421", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Connector421"):
                    opp_val = getattr(item, "uml_Connector421", None)
                    
                    setattr(item, "uml_Connector421", self)
                    

    @property
    def uml_Connector920(self):
        return self.__uml_Connector920

    @uml_Connector920.setter
    def uml_Connector920(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector920", None)
        self.__uml_Connector920 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InformationFlow919"):
                opp_val = getattr(old_value, "uml_InformationFlow919", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InformationFlow919"):
                opp_val = getattr(value, "uml_InformationFlow919", None)
                if opp_val is None:
                    setattr(value, "uml_InformationFlow919", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Connector423(self):
        return self.__uml_Connector423

    @uml_Connector423.setter
    def uml_Connector423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector423", None)
        self.__uml_Connector423 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ConnectorEnd424"):
                    opp_val = getattr(item, "uml_ConnectorEnd424", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ConnectorEnd424", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ConnectorEnd424"):
                    opp_val = getattr(item, "uml_ConnectorEnd424", None)
                    
                    setattr(item, "uml_ConnectorEnd424", self)
                    

    @property
    def uml_Connector426(self):
        return self.__uml_Connector426

    @uml_Connector426.setter
    def uml_Connector426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector426", None)
        self.__uml_Connector426 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Behavior427"):
                    opp_val = getattr(item, "uml_Behavior427", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Behavior427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Behavior427"):
                    opp_val = getattr(item, "uml_Behavior427", None)
                    
                    setattr(item, "uml_Behavior427", self)
                    

    @property
    def uml_Connector417(self):
        return self.__uml_Connector417

    @uml_Connector417.setter
    def uml_Connector417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector417", None)
        self.__uml_Connector417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Association418"):
                opp_val = getattr(old_value, "uml_Association418", None)
                if opp_val == self:
                    setattr(old_value, "uml_Association418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Association418"):
                opp_val = getattr(value, "uml_Association418", None)
                setattr(value, "uml_Association418", self)

    @property
    def uml_Connector673(self):
        return self.__uml_Connector673

    @uml_Connector673.setter
    def uml_Connector673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Connector__uml_Connector673", None)
        self.__uml_Connector673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Message672"):
                opp_val = getattr(old_value, "uml_Message672", None)
                if opp_val == self:
                    setattr(old_value, "uml_Message672", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Message672"):
                opp_val = getattr(value, "uml_Message672", None)
                setattr(value, "uml_Message672", self)

class Class:

    pass
class uml_Component(Class):

    def __init__(self, isIndirectlyInstantiated: str, uml_Component781: set["uml_PackageableElement"] = None, abstraction: set["uml_ComponentRealization"] = None, Component: "uml_ComponentRealization" = None, uml_Component: set["uml_Interface"] = None, uml_Component778: set["uml_Interface"] = None):
        self.isIndirectlyInstantiated = isIndirectlyInstantiated
        self.uml_Component781 = uml_Component781 if uml_Component781 is not None else set()
        self.abstraction = abstraction if abstraction is not None else set()
        self.Component = Component
        self.uml_Component = uml_Component if uml_Component is not None else set()
        self.uml_Component778 = uml_Component778 if uml_Component778 is not None else set()
        
    @property
    def isIndirectlyInstantiated(self) -> str:
        return self.__isIndirectlyInstantiated

    @isIndirectlyInstantiated.setter
    def isIndirectlyInstantiated(self, isIndirectlyInstantiated: str):
        self.__isIndirectlyInstantiated = isIndirectlyInstantiated

    @property
    def uml_Component778(self):
        return self.__uml_Component778

    @uml_Component778.setter
    def uml_Component778(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Component__uml_Component778", None)
        self.__uml_Component778 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Interface779"):
                    opp_val = getattr(item, "uml_Interface779", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Interface779", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Interface779"):
                    opp_val = getattr(item, "uml_Interface779", None)
                    
                    setattr(item, "uml_Interface779", self)
                    

    @property
    def abstraction(self):
        return self.__abstraction

    @abstraction.setter
    def abstraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Component__abstraction", None)
        self.__abstraction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComponentRealization"):
                    opp_val = getattr(item, "ComponentRealization", None)
                    
                    if opp_val == self:
                        setattr(item, "ComponentRealization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComponentRealization"):
                    opp_val = getattr(item, "ComponentRealization", None)
                    
                    setattr(item, "ComponentRealization", self)
                    

    @property
    def uml_Component781(self):
        return self.__uml_Component781

    @uml_Component781.setter
    def uml_Component781(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Component__uml_Component781", None)
        self.__uml_Component781 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_PackageableElement782"):
                    opp_val = getattr(item, "uml_PackageableElement782", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_PackageableElement782", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_PackageableElement782"):
                    opp_val = getattr(item, "uml_PackageableElement782", None)
                    
                    setattr(item, "uml_PackageableElement782", self)
                    

    @property
    def uml_Component(self):
        return self.__uml_Component

    @uml_Component.setter
    def uml_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Component__uml_Component", None)
        self.__uml_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Interface776"):
                    opp_val = getattr(item, "uml_Interface776", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Interface776", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Interface776"):
                    opp_val = getattr(item, "uml_Interface776", None)
                    
                    setattr(item, "uml_Interface776", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realization"):
                opp_val = getattr(old_value, "realization", None)
                if opp_val == self:
                    setattr(old_value, "realization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realization"):
                opp_val = getattr(value, "realization", None)
                setattr(value, "realization", self)

class uml_AssociationClass(Class, Association):

    pass
class uml_Stereotype(Class):

    pass
class BehavioralFeature:

    pass
class uml_Reception(BehavioralFeature):

    pass
class DeployedArtifact:

    pass
class Artifact:

    pass
class uml_DeploymentSpecification(Artifact):

    def __init__(self, deploymentLocation: str, executionLocation: str, configuration: "uml_Deployment" = None, DeploymentSpecification: "uml_Deployment" = None):
        self.deploymentLocation = deploymentLocation
        self.executionLocation = executionLocation
        self.configuration = configuration
        self.DeploymentSpecification = DeploymentSpecification
        
    @property
    def deploymentLocation(self) -> str:
        return self.__deploymentLocation

    @deploymentLocation.setter
    def deploymentLocation(self, deploymentLocation: str):
        self.__deploymentLocation = deploymentLocation

    @property
    def executionLocation(self) -> str:
        return self.__executionLocation

    @executionLocation.setter
    def executionLocation(self, executionLocation: str):
        self.__executionLocation = executionLocation

    @property
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DeploymentSpecification__configuration", None)
        self.__configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Deployment203"):
                opp_val = getattr(old_value, "Deployment203", None)
                if opp_val == self:
                    setattr(old_value, "Deployment203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Deployment203"):
                opp_val = getattr(value, "Deployment203", None)
                setattr(value, "Deployment203", self)

    @property
    def DeploymentSpecification(self):
        return self.__DeploymentSpecification

    @DeploymentSpecification.setter
    def DeploymentSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DeploymentSpecification__DeploymentSpecification", None)
        self.__DeploymentSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deployment"):
                opp_val = getattr(old_value, "deployment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deployment"):
                opp_val = getattr(value, "deployment", None)
                if opp_val is None:
                    setattr(value, "deployment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Class(BehavioredClassifier, EncapsulatedClassifier):

    def __init__(self, isActive: str, uml_Class: "uml_Property" = None, Class: "uml_Operation" = None, uml_Class265: set["uml_Classifier"] = None, class: set["uml_Operation"] = None, uml_Class270: "uml_Class" = None, uml_Class268: set["uml_Class"] = None, uml_Class272: set["uml_Reception"] = None, metaclass: set["uml_Extension"] = None, Class429: "uml_Extension" = None):
        self.isActive = isActive
        self.uml_Class = uml_Class
        self.Class = Class
        self.uml_Class265 = uml_Class265 if uml_Class265 is not None else set()
        self.class = class if class is not None else set()
        self.uml_Class270 = uml_Class270
        self.uml_Class268 = uml_Class268 if uml_Class268 is not None else set()
        self.uml_Class272 = uml_Class272 if uml_Class272 is not None else set()
        self.metaclass = metaclass if metaclass is not None else set()
        self.Class429 = Class429
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def uml_Class265(self):
        return self.__uml_Class265

    @uml_Class265.setter
    def uml_Class265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class265", None)
        self.__uml_Class265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier266"):
                    opp_val = getattr(item, "uml_Classifier266", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier266"):
                    opp_val = getattr(item, "uml_Classifier266", None)
                    
                    setattr(item, "uml_Classifier266", self)
                    

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def uml_Class270(self):
        return self.__uml_Class270

    @uml_Class270.setter
    def uml_Class270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class270", None)
        self.__uml_Class270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class268"):
                opp_val = getattr(old_value, "uml_Class268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class268"):
                opp_val = getattr(value, "uml_Class268", None)
                if opp_val is None:
                    setattr(value, "uml_Class268", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperation219"):
                opp_val = getattr(old_value, "ownedOperation219", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperation219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperation219"):
                opp_val = getattr(value, "ownedOperation219", None)
                setattr(value, "ownedOperation219", self)

    @property
    def uml_Class272(self):
        return self.__uml_Class272

    @uml_Class272.setter
    def uml_Class272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class272", None)
        self.__uml_Class272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Reception"):
                    opp_val = getattr(item, "uml_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Reception"):
                    opp_val = getattr(item, "uml_Reception", None)
                    
                    setattr(item, "uml_Reception", self)
                    

    @property
    def metaclass(self):
        return self.__metaclass

    @metaclass.setter
    def metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__metaclass", None)
        self.__metaclass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Extension"):
                    opp_val = getattr(item, "Extension", None)
                    
                    if opp_val == self:
                        setattr(item, "Extension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extension"):
                    opp_val = getattr(item, "Extension", None)
                    
                    setattr(item, "Extension", self)
                    

    @property
    def uml_Class268(self):
        return self.__uml_Class268

    @uml_Class268.setter
    def uml_Class268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class268", None)
        self.__uml_Class268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Class270"):
                    opp_val = getattr(item, "uml_Class270", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Class270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Class270"):
                    opp_val = getattr(item, "uml_Class270", None)
                    
                    setattr(item, "uml_Class270", self)
                    

    @property
    def uml_Class(self):
        return self.__uml_Class

    @uml_Class.setter
    def uml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__uml_Class", None)
        self.__uml_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Property172"):
                opp_val = getattr(old_value, "uml_Property172", None)
                if opp_val == self:
                    setattr(old_value, "uml_Property172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Property172"):
                opp_val = getattr(value, "uml_Property172", None)
                setattr(value, "uml_Property172", self)

    @property
    def Class429(self):
        return self.__Class429

    @Class429.setter
    def Class429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Class__Class429", None)
        self.__Class429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extension"):
                opp_val = getattr(old_value, "extension", None)
                if opp_val == self:
                    setattr(old_value, "extension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extension"):
                opp_val = getattr(value, "extension", None)
                setattr(value, "extension", self)

class DeploymentTarget:

    pass
class uml_Node(Class, DeploymentTarget):

    pass
class StructuralFeature:

    pass
class MultiplicityElement:

    pass
class uml_ConnectorEnd(MultiplicityElement):

    pass
class uml_Pin(ObjectNode, MultiplicityElement):

    def __init__(self, isControl: str):
        self.isControl = isControl
        
    @property
    def isControl(self) -> str:
        return self.__isControl

    @isControl.setter
    def isControl(self, isControl: str):
        self.__isControl = isControl

class ConnectableElement:

    pass
class uml_Variable(MultiplicityElement, ConnectableElement):

    pass
class uml_Behavior(Class):

    def __init__(self, isReentrant: str, uml_Behavior: "uml_OpaqueExpression" = None, uml_Behavior248: "uml_Behavior" = None, uml_Behavior246: set["uml_Behavior"] = None, uml_Behavior250: set["uml_Parameter"] = None, uml_Behavior253: "uml_BehavioredClassifier" = None, Behavior: "uml_BehavioralFeature" = None, method: "uml_BehavioralFeature" = None, uml_Behavior255: set["uml_Constraint"] = None, uml_Behavior258: set["uml_Constraint"] = None, uml_Behavior261: set["uml_ParameterSet"] = None, uml_Behavior276: "uml_BehavioredClassifier" = None, uml_Behavior279: "uml_BehavioredClassifier" = None, uml_Behavior344: "uml_Transition" = None, uml_Behavior377: "uml_State" = None, uml_Behavior380: "uml_State" = None, uml_Behavior383: "uml_State" = None, uml_Behavior427: "uml_Connector" = None, uml_Behavior641: "uml_ObjectNode" = None, uml_Behavior660: "uml_CallBehaviorAction" = None, uml_Behavior745: "uml_BehaviorExecutionSpecification" = None, uml_Behavior763: "uml_DecisionNode" = None, uml_Behavior768: "uml_ObjectFlow" = None, uml_Behavior771: "uml_ObjectFlow" = None, uml_Behavior989: "uml_ReduceAction" = None):
        self.isReentrant = isReentrant
        self.uml_Behavior = uml_Behavior
        self.uml_Behavior248 = uml_Behavior248
        self.uml_Behavior246 = uml_Behavior246 if uml_Behavior246 is not None else set()
        self.uml_Behavior250 = uml_Behavior250 if uml_Behavior250 is not None else set()
        self.uml_Behavior253 = uml_Behavior253
        self.Behavior = Behavior
        self.method = method
        self.uml_Behavior255 = uml_Behavior255 if uml_Behavior255 is not None else set()
        self.uml_Behavior258 = uml_Behavior258 if uml_Behavior258 is not None else set()
        self.uml_Behavior261 = uml_Behavior261 if uml_Behavior261 is not None else set()
        self.uml_Behavior276 = uml_Behavior276
        self.uml_Behavior279 = uml_Behavior279
        self.uml_Behavior344 = uml_Behavior344
        self.uml_Behavior377 = uml_Behavior377
        self.uml_Behavior380 = uml_Behavior380
        self.uml_Behavior383 = uml_Behavior383
        self.uml_Behavior427 = uml_Behavior427
        self.uml_Behavior641 = uml_Behavior641
        self.uml_Behavior660 = uml_Behavior660
        self.uml_Behavior745 = uml_Behavior745
        self.uml_Behavior763 = uml_Behavior763
        self.uml_Behavior768 = uml_Behavior768
        self.uml_Behavior771 = uml_Behavior771
        self.uml_Behavior989 = uml_Behavior989
        
    @property
    def isReentrant(self) -> str:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: str):
        self.__isReentrant = isReentrant

    @property
    def uml_Behavior989(self):
        return self.__uml_Behavior989

    @uml_Behavior989.setter
    def uml_Behavior989(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior989", None)
        self.__uml_Behavior989 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReduceAction"):
                opp_val = getattr(old_value, "uml_ReduceAction", None)
                if opp_val == self:
                    setattr(old_value, "uml_ReduceAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReduceAction"):
                opp_val = getattr(value, "uml_ReduceAction", None)
                setattr(value, "uml_ReduceAction", self)

    @property
    def uml_Behavior253(self):
        return self.__uml_Behavior253

    @uml_Behavior253.setter
    def uml_Behavior253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior253", None)
        self.__uml_Behavior253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_BehavioredClassifier"):
                opp_val = getattr(old_value, "uml_BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "uml_BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_BehavioredClassifier"):
                opp_val = getattr(value, "uml_BehavioredClassifier", None)
                setattr(value, "uml_BehavioredClassifier", self)

    @property
    def uml_Behavior246(self):
        return self.__uml_Behavior246

    @uml_Behavior246.setter
    def uml_Behavior246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior246", None)
        self.__uml_Behavior246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Behavior248"):
                    opp_val = getattr(item, "uml_Behavior248", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Behavior248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Behavior248"):
                    opp_val = getattr(item, "uml_Behavior248", None)
                    
                    setattr(item, "uml_Behavior248", self)
                    

    @property
    def uml_Behavior279(self):
        return self.__uml_Behavior279

    @uml_Behavior279.setter
    def uml_Behavior279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior279", None)
        self.__uml_Behavior279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_BehavioredClassifier278"):
                opp_val = getattr(old_value, "uml_BehavioredClassifier278", None)
                if opp_val == self:
                    setattr(old_value, "uml_BehavioredClassifier278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_BehavioredClassifier278"):
                opp_val = getattr(value, "uml_BehavioredClassifier278", None)
                setattr(value, "uml_BehavioredClassifier278", self)

    @property
    def uml_Behavior380(self):
        return self.__uml_Behavior380

    @uml_Behavior380.setter
    def uml_Behavior380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior380", None)
        self.__uml_Behavior380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State379"):
                opp_val = getattr(old_value, "uml_State379", None)
                if opp_val == self:
                    setattr(old_value, "uml_State379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State379"):
                opp_val = getattr(value, "uml_State379", None)
                setattr(value, "uml_State379", self)

    @property
    def uml_Behavior344(self):
        return self.__uml_Behavior344

    @uml_Behavior344.setter
    def uml_Behavior344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior344", None)
        self.__uml_Behavior344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Transition343"):
                opp_val = getattr(old_value, "uml_Transition343", None)
                if opp_val == self:
                    setattr(old_value, "uml_Transition343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Transition343"):
                opp_val = getattr(value, "uml_Transition343", None)
                setattr(value, "uml_Transition343", self)

    @property
    def uml_Behavior427(self):
        return self.__uml_Behavior427

    @uml_Behavior427.setter
    def uml_Behavior427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior427", None)
        self.__uml_Behavior427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Connector426"):
                opp_val = getattr(old_value, "uml_Connector426", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Connector426"):
                opp_val = getattr(value, "uml_Connector426", None)
                if opp_val is None:
                    setattr(value, "uml_Connector426", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Behavior768(self):
        return self.__uml_Behavior768

    @uml_Behavior768.setter
    def uml_Behavior768(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior768", None)
        self.__uml_Behavior768 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ObjectFlow767"):
                opp_val = getattr(old_value, "uml_ObjectFlow767", None)
                if opp_val == self:
                    setattr(old_value, "uml_ObjectFlow767", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ObjectFlow767"):
                opp_val = getattr(value, "uml_ObjectFlow767", None)
                setattr(value, "uml_ObjectFlow767", self)

    @property
    def uml_Behavior763(self):
        return self.__uml_Behavior763

    @uml_Behavior763.setter
    def uml_Behavior763(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior763", None)
        self.__uml_Behavior763 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DecisionNode"):
                opp_val = getattr(old_value, "uml_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "uml_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DecisionNode"):
                opp_val = getattr(value, "uml_DecisionNode", None)
                setattr(value, "uml_DecisionNode", self)

    @property
    def uml_Behavior276(self):
        return self.__uml_Behavior276

    @uml_Behavior276.setter
    def uml_Behavior276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior276", None)
        self.__uml_Behavior276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_BehavioredClassifier275"):
                opp_val = getattr(old_value, "uml_BehavioredClassifier275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_BehavioredClassifier275"):
                opp_val = getattr(value, "uml_BehavioredClassifier275", None)
                if opp_val is None:
                    setattr(value, "uml_BehavioredClassifier275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Behavior641(self):
        return self.__uml_Behavior641

    @uml_Behavior641.setter
    def uml_Behavior641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior641", None)
        self.__uml_Behavior641 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ObjectNode640"):
                opp_val = getattr(old_value, "uml_ObjectNode640", None)
                if opp_val == self:
                    setattr(old_value, "uml_ObjectNode640", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ObjectNode640"):
                opp_val = getattr(value, "uml_ObjectNode640", None)
                setattr(value, "uml_ObjectNode640", self)

    @property
    def uml_Behavior377(self):
        return self.__uml_Behavior377

    @uml_Behavior377.setter
    def uml_Behavior377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior377", None)
        self.__uml_Behavior377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State376"):
                opp_val = getattr(old_value, "uml_State376", None)
                if opp_val == self:
                    setattr(old_value, "uml_State376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State376"):
                opp_val = getattr(value, "uml_State376", None)
                setattr(value, "uml_State376", self)

    @property
    def uml_Behavior258(self):
        return self.__uml_Behavior258

    @uml_Behavior258.setter
    def uml_Behavior258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior258", None)
        self.__uml_Behavior258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Constraint259"):
                    opp_val = getattr(item, "uml_Constraint259", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Constraint259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Constraint259"):
                    opp_val = getattr(item, "uml_Constraint259", None)
                    
                    setattr(item, "uml_Constraint259", self)
                    

    @property
    def Behavior(self):
        return self.__Behavior

    @Behavior.setter
    def Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__Behavior", None)
        self.__Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specification"):
                opp_val = getattr(old_value, "specification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specification"):
                opp_val = getattr(value, "specification", None)
                if opp_val is None:
                    setattr(value, "specification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Behavior(self):
        return self.__uml_Behavior

    @uml_Behavior.setter
    def uml_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior", None)
        self.__uml_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_OpaqueExpression149"):
                opp_val = getattr(old_value, "uml_OpaqueExpression149", None)
                if opp_val == self:
                    setattr(old_value, "uml_OpaqueExpression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_OpaqueExpression149"):
                opp_val = getattr(value, "uml_OpaqueExpression149", None)
                setattr(value, "uml_OpaqueExpression149", self)

    @property
    def uml_Behavior383(self):
        return self.__uml_Behavior383

    @uml_Behavior383.setter
    def uml_Behavior383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior383", None)
        self.__uml_Behavior383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State382"):
                opp_val = getattr(old_value, "uml_State382", None)
                if opp_val == self:
                    setattr(old_value, "uml_State382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State382"):
                opp_val = getattr(value, "uml_State382", None)
                setattr(value, "uml_State382", self)

    @property
    def uml_Behavior771(self):
        return self.__uml_Behavior771

    @uml_Behavior771.setter
    def uml_Behavior771(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior771", None)
        self.__uml_Behavior771 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ObjectFlow770"):
                opp_val = getattr(old_value, "uml_ObjectFlow770", None)
                if opp_val == self:
                    setattr(old_value, "uml_ObjectFlow770", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ObjectFlow770"):
                opp_val = getattr(value, "uml_ObjectFlow770", None)
                setattr(value, "uml_ObjectFlow770", self)

    @property
    def uml_Behavior660(self):
        return self.__uml_Behavior660

    @uml_Behavior660.setter
    def uml_Behavior660(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior660", None)
        self.__uml_Behavior660 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_CallBehaviorAction"):
                opp_val = getattr(old_value, "uml_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "uml_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_CallBehaviorAction"):
                opp_val = getattr(value, "uml_CallBehaviorAction", None)
                setattr(value, "uml_CallBehaviorAction", self)

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__method", None)
        self.__method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioralFeature"):
                opp_val = getattr(old_value, "BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioralFeature"):
                opp_val = getattr(value, "BehavioralFeature", None)
                setattr(value, "BehavioralFeature", self)

    @property
    def uml_Behavior745(self):
        return self.__uml_Behavior745

    @uml_Behavior745.setter
    def uml_Behavior745(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior745", None)
        self.__uml_Behavior745 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_BehaviorExecutionSpecification"):
                opp_val = getattr(old_value, "uml_BehaviorExecutionSpecification", None)
                if opp_val == self:
                    setattr(old_value, "uml_BehaviorExecutionSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_BehaviorExecutionSpecification"):
                opp_val = getattr(value, "uml_BehaviorExecutionSpecification", None)
                setattr(value, "uml_BehaviorExecutionSpecification", self)

    @property
    def uml_Behavior255(self):
        return self.__uml_Behavior255

    @uml_Behavior255.setter
    def uml_Behavior255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior255", None)
        self.__uml_Behavior255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Constraint256"):
                    opp_val = getattr(item, "uml_Constraint256", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Constraint256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Constraint256"):
                    opp_val = getattr(item, "uml_Constraint256", None)
                    
                    setattr(item, "uml_Constraint256", self)
                    

    @property
    def uml_Behavior250(self):
        return self.__uml_Behavior250

    @uml_Behavior250.setter
    def uml_Behavior250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior250", None)
        self.__uml_Behavior250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Parameter251"):
                    opp_val = getattr(item, "uml_Parameter251", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Parameter251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Parameter251"):
                    opp_val = getattr(item, "uml_Parameter251", None)
                    
                    setattr(item, "uml_Parameter251", self)
                    

    @property
    def uml_Behavior261(self):
        return self.__uml_Behavior261

    @uml_Behavior261.setter
    def uml_Behavior261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior261", None)
        self.__uml_Behavior261 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ParameterSet262"):
                    opp_val = getattr(item, "uml_ParameterSet262", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ParameterSet262", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ParameterSet262"):
                    opp_val = getattr(item, "uml_ParameterSet262", None)
                    
                    setattr(item, "uml_ParameterSet262", self)
                    

    @property
    def uml_Behavior248(self):
        return self.__uml_Behavior248

    @uml_Behavior248.setter
    def uml_Behavior248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior248", None)
        self.__uml_Behavior248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior246"):
                opp_val = getattr(old_value, "uml_Behavior246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior246"):
                opp_val = getattr(value, "uml_Behavior246", None)
                if opp_val is None:
                    setattr(value, "uml_Behavior246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Parameter(MultiplicityElement, ConnectableElement):

    def __init__(self, direction: str, default: str, isException: str, isStream: str, effect: str, uml_Parameter152: "uml_Operation" = None, uml_Parameter154: "uml_ValueSpecification" = None, uml_Parameter: "uml_OpaqueExpression" = None, parameter: set["uml_ParameterSet"] = None, uml_Parameter251: "uml_Behavior" = None, uml_Parameter239: "uml_BehavioralFeature" = None, Parameter: "uml_ParameterSet" = None, uml_Parameter664: "uml_ActivityParameterNode" = None):
        self.direction = direction
        self.default = default
        self.isException = isException
        self.isStream = isStream
        self.effect = effect
        self.uml_Parameter152 = uml_Parameter152
        self.uml_Parameter154 = uml_Parameter154
        self.uml_Parameter = uml_Parameter
        self.parameter = parameter if parameter is not None else set()
        self.uml_Parameter251 = uml_Parameter251
        self.uml_Parameter239 = uml_Parameter239
        self.Parameter = Parameter
        self.uml_Parameter664 = uml_Parameter664
        
    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def isStream(self) -> str:
        return self.__isStream

    @isStream.setter
    def isStream(self, isStream: str):
        self.__isStream = isStream

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def isException(self) -> str:
        return self.__isException

    @isException.setter
    def isException(self, isException: str):
        self.__isException = isException

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def uml_Parameter664(self):
        return self.__uml_Parameter664

    @uml_Parameter664.setter
    def uml_Parameter664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter664", None)
        self.__uml_Parameter664 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ActivityParameterNode"):
                opp_val = getattr(old_value, "uml_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "uml_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ActivityParameterNode"):
                opp_val = getattr(value, "uml_ActivityParameterNode", None)
                setattr(value, "uml_ActivityParameterNode", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__parameter", None)
        self.__parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterSet"):
                    opp_val = getattr(item, "ParameterSet", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterSet"):
                    opp_val = getattr(item, "ParameterSet", None)
                    
                    setattr(item, "ParameterSet", self)
                    

    @property
    def uml_Parameter251(self):
        return self.__uml_Parameter251

    @uml_Parameter251.setter
    def uml_Parameter251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter251", None)
        self.__uml_Parameter251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior250"):
                opp_val = getattr(old_value, "uml_Behavior250", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior250"):
                opp_val = getattr(value, "uml_Behavior250", None)
                if opp_val is None:
                    setattr(value, "uml_Behavior250", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Parameter154(self):
        return self.__uml_Parameter154

    @uml_Parameter154.setter
    def uml_Parameter154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter154", None)
        self.__uml_Parameter154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ValueSpecification155"):
                opp_val = getattr(old_value, "uml_ValueSpecification155", None)
                if opp_val == self:
                    setattr(old_value, "uml_ValueSpecification155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ValueSpecification155"):
                opp_val = getattr(value, "uml_ValueSpecification155", None)
                setattr(value, "uml_ValueSpecification155", self)

    @property
    def uml_Parameter152(self):
        return self.__uml_Parameter152

    @uml_Parameter152.setter
    def uml_Parameter152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter152", None)
        self.__uml_Parameter152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Operation"):
                opp_val = getattr(old_value, "uml_Operation", None)
                if opp_val == self:
                    setattr(old_value, "uml_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Operation"):
                opp_val = getattr(value, "uml_Operation", None)
                setattr(value, "uml_Operation", self)

    @property
    def uml_Parameter239(self):
        return self.__uml_Parameter239

    @uml_Parameter239.setter
    def uml_Parameter239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter239", None)
        self.__uml_Parameter239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_BehavioralFeature"):
                opp_val = getattr(old_value, "uml_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_BehavioralFeature"):
                opp_val = getattr(value, "uml_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "uml_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterSet"):
                opp_val = getattr(old_value, "parameterSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterSet"):
                opp_val = getattr(value, "parameterSet", None)
                if opp_val is None:
                    setattr(value, "parameterSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Parameter(self):
        return self.__uml_Parameter

    @uml_Parameter.setter
    def uml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Parameter__uml_Parameter", None)
        self.__uml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_OpaqueExpression147"):
                opp_val = getattr(old_value, "uml_OpaqueExpression147", None)
                if opp_val == self:
                    setattr(old_value, "uml_OpaqueExpression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_OpaqueExpression147"):
                opp_val = getattr(value, "uml_OpaqueExpression147", None)
                setattr(value, "uml_OpaqueExpression147", self)

class Realization:

    pass
class uml_ComponentRealization(Realization):

    pass
class uml_InterfaceRealization(Realization):

    pass
class ValueSpecification:

    pass
class uml_TimeExpression(ValueSpecification):

    pass
class uml_Interval(ValueSpecification):

    pass
class uml_Duration(ValueSpecification):

    pass
class uml_LiteralSpecification(ValueSpecification):

    pass
class uml_Expression(ValueSpecification):

    def __init__(self, symbol: str, uml_Expression: set["uml_ValueSpecification"] = None):
        self.symbol = symbol
        self.uml_Expression = uml_Expression if uml_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def uml_Expression(self):
        return self.__uml_Expression

    @uml_Expression.setter
    def uml_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Expression__uml_Expression", None)
        self.__uml_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ValueSpecification494"):
                    opp_val = getattr(item, "uml_ValueSpecification494", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ValueSpecification494", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ValueSpecification494"):
                    opp_val = getattr(item, "uml_ValueSpecification494", None)
                    
                    setattr(item, "uml_ValueSpecification494", self)
                    

class uml_InstanceValue(ValueSpecification):

    pass
class uml_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, uml_OpaqueExpression: "uml_Abstraction" = None, uml_OpaqueExpression147: "uml_Parameter" = None, uml_OpaqueExpression149: "uml_Behavior" = None):
        self.body = body
        self.language = language
        self.uml_OpaqueExpression = uml_OpaqueExpression
        self.uml_OpaqueExpression147 = uml_OpaqueExpression147
        self.uml_OpaqueExpression149 = uml_OpaqueExpression149
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def uml_OpaqueExpression147(self):
        return self.__uml_OpaqueExpression147

    @uml_OpaqueExpression147.setter
    def uml_OpaqueExpression147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_OpaqueExpression__uml_OpaqueExpression147", None)
        self.__uml_OpaqueExpression147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Parameter"):
                opp_val = getattr(old_value, "uml_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "uml_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Parameter"):
                opp_val = getattr(value, "uml_Parameter", None)
                setattr(value, "uml_Parameter", self)

    @property
    def uml_OpaqueExpression(self):
        return self.__uml_OpaqueExpression

    @uml_OpaqueExpression.setter
    def uml_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_OpaqueExpression__uml_OpaqueExpression", None)
        self.__uml_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Abstraction"):
                opp_val = getattr(old_value, "uml_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "uml_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Abstraction"):
                opp_val = getattr(value, "uml_Abstraction", None)
                setattr(value, "uml_Abstraction", self)

    @property
    def uml_OpaqueExpression149(self):
        return self.__uml_OpaqueExpression149

    @uml_OpaqueExpression149.setter
    def uml_OpaqueExpression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_OpaqueExpression__uml_OpaqueExpression149", None)
        self.__uml_OpaqueExpression149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior"):
                opp_val = getattr(old_value, "uml_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior"):
                opp_val = getattr(value, "uml_Behavior", None)
                setattr(value, "uml_Behavior", self)

class Dependency:

    pass
class uml_Usage(Dependency):

    pass
class uml_Deployment(Dependency):

    pass
class uml_Abstraction(Dependency):

    pass
class Abstraction:

    pass
class uml_Manifestation(Abstraction):

    pass
class uml_Realization(Abstraction):

    pass
class uml_UseCase(BehavioredClassifier):

    pass
class uml_Property(DeploymentTarget, StructuralFeature, ConnectableElement):

    def __init__(self, isDerived: str, isDerivedUnion: str, default: str, aggregation: str, isComposite: str, uml_Property: "uml_Association" = None, Property: "uml_Association" = None, Property61: "uml_Association" = None, uml_Property80: "uml_Classifier" = None, uml_Property164: "uml_ConnectorEnd" = None, ownedAttribute: "uml_DataType" = None, uml_Property176: "uml_Property" = None, uml_Property174: set["uml_Property"] = None, uml_Property170: "uml_ConnectorEnd" = None, uml_Property172: "uml_Class" = None, uml_Property184: set["uml_Property"] = None, memberEnd: "uml_Association" = None, Property191: "uml_Property" = None, associationEnd: set["uml_Property"] = None, Property194: "uml_Property" = None, qualifier: "uml_Property" = None, ownedEnd: "uml_Association" = None, uml_Property179: "uml_ValueSpecification" = None, uml_Property183: "uml_Property" = None, uml_Property181: "uml_Property" = None, uml_Property186: "uml_Property" = None, uml_Property213: "uml_Artifact" = None, uml_Property305: "uml_Signal" = None, uml_Property287: "uml_Interface" = None, uml_Property407: "uml_StructuredClassifier" = None, uml_Property410: "uml_StructuredClassifier" = None, Property444: "uml_DataType" = None, uml_Property842: "uml_QualifierValue" = None, uml_Property837: "uml_LinkEndData" = None, uml_Property951: "uml_ReadLinkObjectEndAction" = None, uml_Property962: "uml_ReadLinkObjectEndQualifierAction" = None):
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.aggregation = aggregation
        self.isComposite = isComposite
        self.uml_Property = uml_Property
        self.Property = Property
        self.Property61 = Property61
        self.uml_Property80 = uml_Property80
        self.uml_Property164 = uml_Property164
        self.ownedAttribute = ownedAttribute
        self.uml_Property176 = uml_Property176
        self.uml_Property174 = uml_Property174 if uml_Property174 is not None else set()
        self.uml_Property170 = uml_Property170
        self.uml_Property172 = uml_Property172
        self.uml_Property184 = uml_Property184 if uml_Property184 is not None else set()
        self.memberEnd = memberEnd
        self.Property191 = Property191
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.Property194 = Property194
        self.qualifier = qualifier
        self.ownedEnd = ownedEnd
        self.uml_Property179 = uml_Property179
        self.uml_Property183 = uml_Property183
        self.uml_Property181 = uml_Property181
        self.uml_Property186 = uml_Property186
        self.uml_Property213 = uml_Property213
        self.uml_Property305 = uml_Property305
        self.uml_Property287 = uml_Property287
        self.uml_Property407 = uml_Property407
        self.uml_Property410 = uml_Property410
        self.Property444 = Property444
        self.uml_Property842 = uml_Property842
        self.uml_Property837 = uml_Property837
        self.uml_Property951 = uml_Property951
        self.uml_Property962 = uml_Property962
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isDerivedUnion(self) -> str:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: str):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def uml_Property183(self):
        return self.__uml_Property183

    @uml_Property183.setter
    def uml_Property183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property183", None)
        self.__uml_Property183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Property181"):
                opp_val = getattr(old_value, "uml_Property181", None)
                if opp_val == self:
                    setattr(old_value, "uml_Property181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Property181"):
                opp_val = getattr(value, "uml_Property181", None)
                setattr(value, "uml_Property181", self)

    @property
    def uml_Property186(self):
        return self.__uml_Property186

    @uml_Property186.setter
    def uml_Property186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property186", None)
        self.__uml_Property186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Property184"):
                opp_val = getattr(old_value, "uml_Property184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Property184"):
                opp_val = getattr(value, "uml_Property184", None)
                if opp_val is None:
                    setattr(value, "uml_Property184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property407(self):
        return self.__uml_Property407

    @uml_Property407.setter
    def uml_Property407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property407", None)
        self.__uml_Property407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_StructuredClassifier"):
                opp_val = getattr(old_value, "uml_StructuredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_StructuredClassifier"):
                opp_val = getattr(value, "uml_StructuredClassifier", None)
                if opp_val is None:
                    setattr(value, "uml_StructuredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property(self):
        return self.__uml_Property

    @uml_Property.setter
    def uml_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property", None)
        self.__uml_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Association65"):
                opp_val = getattr(old_value, "uml_Association65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Association65"):
                opp_val = getattr(value, "uml_Association65", None)
                if opp_val is None:
                    setattr(value, "uml_Association65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property174(self):
        return self.__uml_Property174

    @uml_Property174.setter
    def uml_Property174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property174", None)
        self.__uml_Property174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property176"):
                    opp_val = getattr(item, "uml_Property176", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property176"):
                    opp_val = getattr(item, "uml_Property176", None)
                    
                    setattr(item, "uml_Property176", self)
                    

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__ownedEnd", None)
        self.__ownedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def uml_Property170(self):
        return self.__uml_Property170

    @uml_Property170.setter
    def uml_Property170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property170", None)
        self.__uml_Property170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ConnectorEnd169"):
                opp_val = getattr(old_value, "uml_ConnectorEnd169", None)
                if opp_val == self:
                    setattr(old_value, "uml_ConnectorEnd169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ConnectorEnd169"):
                opp_val = getattr(value, "uml_ConnectorEnd169", None)
                setattr(value, "uml_ConnectorEnd169", self)

    @property
    def uml_Property176(self):
        return self.__uml_Property176

    @uml_Property176.setter
    def uml_Property176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property176", None)
        self.__uml_Property176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Property174"):
                opp_val = getattr(old_value, "uml_Property174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Property174"):
                opp_val = getattr(value, "uml_Property174", None)
                if opp_val is None:
                    setattr(value, "uml_Property174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property842(self):
        return self.__uml_Property842

    @uml_Property842.setter
    def uml_Property842(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property842", None)
        self.__uml_Property842 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_QualifierValue841"):
                opp_val = getattr(old_value, "uml_QualifierValue841", None)
                if opp_val == self:
                    setattr(old_value, "uml_QualifierValue841", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_QualifierValue841"):
                opp_val = getattr(value, "uml_QualifierValue841", None)
                setattr(value, "uml_QualifierValue841", self)

    @property
    def Property444(self):
        return self.__Property444

    @Property444.setter
    def Property444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__Property444", None)
        self.__Property444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype"):
                opp_val = getattr(old_value, "datatype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype"):
                opp_val = getattr(value, "datatype", None)
                if opp_val is None:
                    setattr(value, "datatype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property184(self):
        return self.__uml_Property184

    @uml_Property184.setter
    def uml_Property184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property184", None)
        self.__uml_Property184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property186"):
                    opp_val = getattr(item, "uml_Property186", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property186"):
                    opp_val = getattr(item, "uml_Property186", None)
                    
                    setattr(item, "uml_Property186", self)
                    

    @property
    def uml_Property951(self):
        return self.__uml_Property951

    @uml_Property951.setter
    def uml_Property951(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property951", None)
        self.__uml_Property951 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReadLinkObjectEndAction950"):
                opp_val = getattr(old_value, "uml_ReadLinkObjectEndAction950", None)
                if opp_val == self:
                    setattr(old_value, "uml_ReadLinkObjectEndAction950", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReadLinkObjectEndAction950"):
                opp_val = getattr(value, "uml_ReadLinkObjectEndAction950", None)
                setattr(value, "uml_ReadLinkObjectEndAction950", self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association188"):
                opp_val = getattr(old_value, "Association188", None)
                if opp_val == self:
                    setattr(old_value, "Association188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association188"):
                opp_val = getattr(value, "Association188", None)
                setattr(value, "Association188", self)

    @property
    def uml_Property80(self):
        return self.__uml_Property80

    @uml_Property80.setter
    def uml_Property80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property80", None)
        self.__uml_Property80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier79"):
                opp_val = getattr(old_value, "uml_Classifier79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier79"):
                opp_val = getattr(value, "uml_Classifier79", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property962(self):
        return self.__uml_Property962

    @uml_Property962.setter
    def uml_Property962(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property962", None)
        self.__uml_Property962 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReadLinkObjectEndQualifierAction961"):
                opp_val = getattr(old_value, "uml_ReadLinkObjectEndQualifierAction961", None)
                if opp_val == self:
                    setattr(old_value, "uml_ReadLinkObjectEndQualifierAction961", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReadLinkObjectEndQualifierAction961"):
                opp_val = getattr(value, "uml_ReadLinkObjectEndQualifierAction961", None)
                setattr(value, "uml_ReadLinkObjectEndQualifierAction961", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__associationEnd", None)
        self.__associationEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property191"):
                    opp_val = getattr(item, "Property191", None)
                    
                    if opp_val == self:
                        setattr(item, "Property191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property191"):
                    opp_val = getattr(item, "Property191", None)
                    
                    setattr(item, "Property191", self)
                    

    @property
    def uml_Property164(self):
        return self.__uml_Property164

    @uml_Property164.setter
    def uml_Property164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property164", None)
        self.__uml_Property164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ConnectorEnd163"):
                opp_val = getattr(old_value, "uml_ConnectorEnd163", None)
                if opp_val == self:
                    setattr(old_value, "uml_ConnectorEnd163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ConnectorEnd163"):
                opp_val = getattr(value, "uml_ConnectorEnd163", None)
                setattr(value, "uml_ConnectorEnd163", self)

    @property
    def uml_Property181(self):
        return self.__uml_Property181

    @uml_Property181.setter
    def uml_Property181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property181", None)
        self.__uml_Property181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Property183"):
                opp_val = getattr(old_value, "uml_Property183", None)
                if opp_val == self:
                    setattr(old_value, "uml_Property183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Property183"):
                opp_val = getattr(value, "uml_Property183", None)
                setattr(value, "uml_Property183", self)

    @property
    def uml_Property305(self):
        return self.__uml_Property305

    @uml_Property305.setter
    def uml_Property305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property305", None)
        self.__uml_Property305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Signal304"):
                opp_val = getattr(old_value, "uml_Signal304", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Signal304"):
                opp_val = getattr(value, "uml_Signal304", None)
                if opp_val is None:
                    setattr(value, "uml_Signal304", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property191(self):
        return self.__Property191

    @Property191.setter
    def Property191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__Property191", None)
        self.__Property191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationEnd"):
                opp_val = getattr(old_value, "associationEnd", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationEnd"):
                opp_val = getattr(value, "associationEnd", None)
                if opp_val is None:
                    setattr(value, "associationEnd", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property61(self):
        return self.__Property61

    @Property61.setter
    def Property61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__Property61", None)
        self.__Property61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__qualifier", None)
        self.__qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property194"):
                opp_val = getattr(old_value, "Property194", None)
                if opp_val == self:
                    setattr(old_value, "Property194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property194"):
                opp_val = getattr(value, "Property194", None)
                setattr(value, "Property194", self)

    @property
    def uml_Property287(self):
        return self.__uml_Property287

    @uml_Property287.setter
    def uml_Property287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property287", None)
        self.__uml_Property287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Interface286"):
                opp_val = getattr(old_value, "uml_Interface286", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Interface286"):
                opp_val = getattr(value, "uml_Interface286", None)
                if opp_val is None:
                    setattr(value, "uml_Interface286", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property179(self):
        return self.__uml_Property179

    @uml_Property179.setter
    def uml_Property179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property179", None)
        self.__uml_Property179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ValueSpecification180"):
                opp_val = getattr(old_value, "uml_ValueSpecification180", None)
                if opp_val == self:
                    setattr(old_value, "uml_ValueSpecification180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ValueSpecification180"):
                opp_val = getattr(value, "uml_ValueSpecification180", None)
                setattr(value, "uml_ValueSpecification180", self)

    @property
    def uml_Property837(self):
        return self.__uml_Property837

    @uml_Property837.setter
    def uml_Property837(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property837", None)
        self.__uml_Property837 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_LinkEndData836"):
                opp_val = getattr(old_value, "uml_LinkEndData836", None)
                if opp_val == self:
                    setattr(old_value, "uml_LinkEndData836", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_LinkEndData836"):
                opp_val = getattr(value, "uml_LinkEndData836", None)
                setattr(value, "uml_LinkEndData836", self)

    @property
    def uml_Property172(self):
        return self.__uml_Property172

    @uml_Property172.setter
    def uml_Property172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property172", None)
        self.__uml_Property172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class"):
                opp_val = getattr(old_value, "uml_Class", None)
                if opp_val == self:
                    setattr(old_value, "uml_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class"):
                opp_val = getattr(value, "uml_Class", None)
                setattr(value, "uml_Class", self)

    @property
    def Property194(self):
        return self.__Property194

    @Property194.setter
    def Property194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__Property194", None)
        self.__Property194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifier"):
                opp_val = getattr(old_value, "qualifier", None)
                if opp_val == self:
                    setattr(old_value, "qualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifier"):
                opp_val = getattr(value, "qualifier", None)
                setattr(value, "qualifier", self)

    @property
    def uml_Property410(self):
        return self.__uml_Property410

    @uml_Property410.setter
    def uml_Property410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property410", None)
        self.__uml_Property410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_StructuredClassifier409"):
                opp_val = getattr(old_value, "uml_StructuredClassifier409", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_StructuredClassifier409"):
                opp_val = getattr(value, "uml_StructuredClassifier409", None)
                if opp_val is None:
                    setattr(value, "uml_StructuredClassifier409", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Property213(self):
        return self.__uml_Property213

    @uml_Property213.setter
    def uml_Property213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__uml_Property213", None)
        self.__uml_Property213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Artifact212"):
                opp_val = getattr(old_value, "uml_Artifact212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Artifact212"):
                opp_val = getattr(value, "uml_Artifact212", None)
                if opp_val is None:
                    setattr(value, "uml_Artifact212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningAssociation"):
                opp_val = getattr(old_value, "owningAssociation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningAssociation"):
                opp_val = getattr(value, "owningAssociation", None)
                if opp_val is None:
                    setattr(value, "owningAssociation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Classifier:

    pass
class uml_Interface(Classifier):

    pass
class uml_StructuredClassifier(Classifier):

    pass
class uml_InformationItem(Classifier):

    pass
class uml_BehavioredClassifier(Classifier):

    pass
class uml_DataType(Classifier):

    pass
class uml_Signal(Classifier):

    pass
class uml_Artifact(Classifier, DeployedArtifact):

    def __init__(self, fileName: str, uml_Artifact212: set["uml_Property"] = None, uml_Artifact: "uml_Artifact" = None, uml_Artifact204: set["uml_Artifact"] = None, uml_Artifact207: set["uml_Manifestation"] = None, uml_Artifact209: set["uml_Operation"] = None):
        self.fileName = fileName
        self.uml_Artifact212 = uml_Artifact212 if uml_Artifact212 is not None else set()
        self.uml_Artifact = uml_Artifact
        self.uml_Artifact204 = uml_Artifact204 if uml_Artifact204 is not None else set()
        self.uml_Artifact207 = uml_Artifact207 if uml_Artifact207 is not None else set()
        self.uml_Artifact209 = uml_Artifact209 if uml_Artifact209 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def uml_Artifact207(self):
        return self.__uml_Artifact207

    @uml_Artifact207.setter
    def uml_Artifact207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Artifact__uml_Artifact207", None)
        self.__uml_Artifact207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Manifestation"):
                    opp_val = getattr(item, "uml_Manifestation", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Manifestation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Manifestation"):
                    opp_val = getattr(item, "uml_Manifestation", None)
                    
                    setattr(item, "uml_Manifestation", self)
                    

    @property
    def uml_Artifact209(self):
        return self.__uml_Artifact209

    @uml_Artifact209.setter
    def uml_Artifact209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Artifact__uml_Artifact209", None)
        self.__uml_Artifact209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Operation210"):
                    opp_val = getattr(item, "uml_Operation210", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Operation210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Operation210"):
                    opp_val = getattr(item, "uml_Operation210", None)
                    
                    setattr(item, "uml_Operation210", self)
                    

    @property
    def uml_Artifact212(self):
        return self.__uml_Artifact212

    @uml_Artifact212.setter
    def uml_Artifact212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Artifact__uml_Artifact212", None)
        self.__uml_Artifact212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property213"):
                    opp_val = getattr(item, "uml_Property213", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property213"):
                    opp_val = getattr(item, "uml_Property213", None)
                    
                    setattr(item, "uml_Property213", self)
                    

    @property
    def uml_Artifact204(self):
        return self.__uml_Artifact204

    @uml_Artifact204.setter
    def uml_Artifact204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Artifact__uml_Artifact204", None)
        self.__uml_Artifact204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Artifact"):
                    opp_val = getattr(item, "uml_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Artifact"):
                    opp_val = getattr(item, "uml_Artifact", None)
                    
                    setattr(item, "uml_Artifact", self)
                    

    @property
    def uml_Artifact(self):
        return self.__uml_Artifact

    @uml_Artifact.setter
    def uml_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Artifact__uml_Artifact", None)
        self.__uml_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Artifact204"):
                opp_val = getattr(old_value, "uml_Artifact204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Artifact204"):
                opp_val = getattr(value, "uml_Artifact204", None)
                if opp_val is None:
                    setattr(value, "uml_Artifact204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Substitution(Realization):

    pass
class Type:

    pass
class RedefinableElement:

    pass
class uml_ExtensionPoint(RedefinableElement):

    pass
class uml_ActivityEdge(RedefinableElement):

    pass
class uml_ActivityNode(RedefinableElement):

    pass
class uml_RedefinableTemplateSignature(TemplateSignature, RedefinableElement):

    pass
class uml_Feature(RedefinableElement):

    def __init__(self, isStatic: str, Feature: "uml_Classifier" = None, feature: set["uml_Classifier"] = None):
        self.isStatic = isStatic
        self.Feature = Feature
        self.feature = feature if feature is not None else set()
        
    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier140"):
                    opp_val = getattr(item, "Classifier140", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier140"):
                    opp_val = getattr(item, "Classifier140", None)
                    
                    setattr(item, "Classifier140", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuringClassifier"):
                opp_val = getattr(old_value, "featuringClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuringClassifier"):
                opp_val = getattr(value, "featuringClassifier", None)
                if opp_val is None:
                    setattr(value, "featuringClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypedElement:

    pass
class uml_ObjectNode(TypedElement, ActivityNode):

    def __init__(self, ordering: str, isControlType: str, uml_ObjectNode: "uml_ExceptionHandler" = None, uml_ObjectNode640: "uml_Behavior" = None, uml_ObjectNode634: "uml_ValueSpecification" = None, uml_ObjectNode637: set["uml_State"] = None):
        self.ordering = ordering
        self.isControlType = isControlType
        self.uml_ObjectNode = uml_ObjectNode
        self.uml_ObjectNode640 = uml_ObjectNode640
        self.uml_ObjectNode634 = uml_ObjectNode634
        self.uml_ObjectNode637 = uml_ObjectNode637 if uml_ObjectNode637 is not None else set()
        
    @property
    def isControlType(self) -> str:
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: str):
        self.__isControlType = isControlType

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def uml_ObjectNode(self):
        return self.__uml_ObjectNode

    @uml_ObjectNode.setter
    def uml_ObjectNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ObjectNode__uml_ObjectNode", None)
        self.__uml_ObjectNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ExceptionHandler628"):
                opp_val = getattr(old_value, "uml_ExceptionHandler628", None)
                if opp_val == self:
                    setattr(old_value, "uml_ExceptionHandler628", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ExceptionHandler628"):
                opp_val = getattr(value, "uml_ExceptionHandler628", None)
                setattr(value, "uml_ExceptionHandler628", self)

    @property
    def uml_ObjectNode640(self):
        return self.__uml_ObjectNode640

    @uml_ObjectNode640.setter
    def uml_ObjectNode640(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ObjectNode__uml_ObjectNode640", None)
        self.__uml_ObjectNode640 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior641"):
                opp_val = getattr(old_value, "uml_Behavior641", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior641", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior641"):
                opp_val = getattr(value, "uml_Behavior641", None)
                setattr(value, "uml_Behavior641", self)

    @property
    def uml_ObjectNode637(self):
        return self.__uml_ObjectNode637

    @uml_ObjectNode637.setter
    def uml_ObjectNode637(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ObjectNode__uml_ObjectNode637", None)
        self.__uml_ObjectNode637 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_State638"):
                    opp_val = getattr(item, "uml_State638", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_State638", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_State638"):
                    opp_val = getattr(item, "uml_State638", None)
                    
                    setattr(item, "uml_State638", self)
                    

    @property
    def uml_ObjectNode634(self):
        return self.__uml_ObjectNode634

    @uml_ObjectNode634.setter
    def uml_ObjectNode634(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ObjectNode__uml_ObjectNode634", None)
        self.__uml_ObjectNode634 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ValueSpecification635"):
                opp_val = getattr(old_value, "uml_ValueSpecification635", None)
                if opp_val == self:
                    setattr(old_value, "uml_ValueSpecification635", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ValueSpecification635"):
                opp_val = getattr(value, "uml_ValueSpecification635", None)
                setattr(value, "uml_ValueSpecification635", self)

class uml_StructuralFeature(Feature, TypedElement, MultiplicityElement):

    def __init__(self, isReadOnly: str, uml_StructuralFeature: "uml_Slot" = None, uml_StructuralFeature811: "uml_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.uml_StructuralFeature = uml_StructuralFeature
        self.uml_StructuralFeature811 = uml_StructuralFeature811
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def uml_StructuralFeature(self):
        return self.__uml_StructuralFeature

    @uml_StructuralFeature.setter
    def uml_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuralFeature__uml_StructuralFeature", None)
        self.__uml_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Slot"):
                opp_val = getattr(old_value, "uml_Slot", None)
                if opp_val == self:
                    setattr(old_value, "uml_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Slot"):
                opp_val = getattr(value, "uml_Slot", None)
                setattr(value, "uml_Slot", self)

    @property
    def uml_StructuralFeature811(self):
        return self.__uml_StructuralFeature811

    @uml_StructuralFeature811.setter
    def uml_StructuralFeature811(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuralFeature__uml_StructuralFeature811", None)
        self.__uml_StructuralFeature811 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_StructuralFeatureAction"):
                opp_val = getattr(old_value, "uml_StructuralFeatureAction", None)
                if opp_val == self:
                    setattr(old_value, "uml_StructuralFeatureAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_StructuralFeatureAction"):
                opp_val = getattr(value, "uml_StructuralFeatureAction", None)
                setattr(value, "uml_StructuralFeatureAction", self)

class Relationship:

    pass
class uml_Association(Classifier, Relationship):

    def __init__(self, isDerived: str, uml_Association65: set["uml_Property"] = None, owningAssociation: set["uml_Property"] = None, association: set["uml_Property"] = None, uml_Association: set["uml_Type"] = None, Association188: "uml_Property" = None, Association: "uml_Property" = None, uml_Association418: "uml_Connector" = None, uml_Association856: "uml_ClearAssociationAction" = None):
        self.isDerived = isDerived
        self.uml_Association65 = uml_Association65 if uml_Association65 is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.association = association if association is not None else set()
        self.uml_Association = uml_Association if uml_Association is not None else set()
        self.Association188 = Association188
        self.Association = Association
        self.uml_Association418 = uml_Association418
        self.uml_Association856 = uml_Association856
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def uml_Association856(self):
        return self.__uml_Association856

    @uml_Association856.setter
    def uml_Association856(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association856", None)
        self.__uml_Association856 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ClearAssociationAction855"):
                opp_val = getattr(old_value, "uml_ClearAssociationAction855", None)
                if opp_val == self:
                    setattr(old_value, "uml_ClearAssociationAction855", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ClearAssociationAction855"):
                opp_val = getattr(value, "uml_ClearAssociationAction855", None)
                setattr(value, "uml_ClearAssociationAction855", self)

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property61"):
                    opp_val = getattr(item, "Property61", None)
                    
                    if opp_val == self:
                        setattr(item, "Property61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property61"):
                    opp_val = getattr(item, "Property61", None)
                    
                    setattr(item, "Property61", self)
                    

    @property
    def uml_Association(self):
        return self.__uml_Association

    @uml_Association.setter
    def uml_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association", None)
        self.__uml_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Type63"):
                    opp_val = getattr(item, "uml_Type63", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Type63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Type63"):
                    opp_val = getattr(item, "uml_Type63", None)
                    
                    setattr(item, "uml_Type63", self)
                    

    @property
    def uml_Association418(self):
        return self.__uml_Association418

    @uml_Association418.setter
    def uml_Association418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association418", None)
        self.__uml_Association418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Connector417"):
                opp_val = getattr(old_value, "uml_Connector417", None)
                if opp_val == self:
                    setattr(old_value, "uml_Connector417", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Connector417"):
                opp_val = getattr(value, "uml_Connector417", None)
                setattr(value, "uml_Connector417", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedEnd"):
                opp_val = getattr(old_value, "ownedEnd", None)
                if opp_val == self:
                    setattr(old_value, "ownedEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedEnd"):
                opp_val = getattr(value, "ownedEnd", None)
                setattr(value, "ownedEnd", self)

    @property
    def uml_Association65(self):
        return self.__uml_Association65

    @uml_Association65.setter
    def uml_Association65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__uml_Association65", None)
        self.__uml_Association65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property"):
                    opp_val = getattr(item, "uml_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property"):
                    opp_val = getattr(item, "uml_Property", None)
                    
                    setattr(item, "uml_Property", self)
                    

    @property
    def Association188(self):
        return self.__Association188

    @Association188.setter
    def Association188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Association__Association188", None)
        self.__Association188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "memberEnd"):
                opp_val = getattr(old_value, "memberEnd", None)
                if opp_val == self:
                    setattr(old_value, "memberEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "memberEnd"):
                opp_val = getattr(value, "memberEnd", None)
                setattr(value, "memberEnd", self)

class uml_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class uml_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: str, Generalization: "uml_Classifier" = None, generalization134: "uml_Classifier" = None, Generalization138: "uml_GeneralizationSet" = None, uml_Generalization: "uml_Classifier" = None, generalization: set["uml_GeneralizationSet"] = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.generalization134 = generalization134
        self.Generalization138 = Generalization138
        self.uml_Generalization = uml_Generalization
        self.generalization = generalization if generalization is not None else set()
        
    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def uml_Generalization(self):
        return self.__uml_Generalization

    @uml_Generalization.setter
    def uml_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__uml_Generalization", None)
        self.__uml_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier130"):
                opp_val = getattr(old_value, "uml_Classifier130", None)
                if opp_val == self:
                    setattr(old_value, "uml_Classifier130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier130"):
                opp_val = getattr(value, "uml_Classifier130", None)
                setattr(value, "uml_Classifier130", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__generalization", None)
        self.__generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet132"):
                    opp_val = getattr(item, "GeneralizationSet132", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet132"):
                    opp_val = getattr(item, "GeneralizationSet132", None)
                    
                    setattr(item, "GeneralizationSet132", self)
                    

    @property
    def generalization134(self):
        return self.__generalization134

    @generalization134.setter
    def generalization134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__generalization134", None)
        self.__generalization134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

    @property
    def Generalization138(self):
        return self.__Generalization138

    @Generalization138.setter
    def Generalization138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__Generalization138", None)
        self.__Generalization138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalizationSet"):
                opp_val = getattr(old_value, "generalizationSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalizationSet"):
                opp_val = getattr(value, "generalizationSet", None)
                if opp_val is None:
                    setattr(value, "generalizationSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Generalization__Generalization", None)
        self.__Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specific"):
                opp_val = getattr(old_value, "specific", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specific"):
                opp_val = getattr(value, "specific", None)
                if opp_val is None:
                    setattr(value, "specific", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_ElementImport(DirectedRelationship):

    def __init__(self, alias: str, visibility: str, ElementImport: "uml_Namespace" = None, uml_ElementImport: "uml_PackageableElement" = None, elementImport: "uml_Namespace" = None, uml_ElementImport435: "uml_Profile" = None):
        self.alias = alias
        self.visibility = visibility
        self.ElementImport = ElementImport
        self.uml_ElementImport = uml_ElementImport
        self.elementImport = elementImport
        self.uml_ElementImport435 = uml_ElementImport435
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace45"):
                opp_val = getattr(old_value, "Namespace45", None)
                if opp_val == self:
                    setattr(old_value, "Namespace45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace45"):
                opp_val = getattr(value, "Namespace45", None)
                setattr(value, "Namespace45", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ElementImport__ElementImport", None)
        self.__ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace"):
                opp_val = getattr(old_value, "importingNamespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace"):
                opp_val = getattr(value, "importingNamespace", None)
                if opp_val is None:
                    setattr(value, "importingNamespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_ElementImport435(self):
        return self.__uml_ElementImport435

    @uml_ElementImport435.setter
    def uml_ElementImport435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ElementImport__uml_ElementImport435", None)
        self.__uml_ElementImport435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Profile434"):
                opp_val = getattr(old_value, "uml_Profile434", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Profile434"):
                opp_val = getattr(value, "uml_Profile434", None)
                if opp_val is None:
                    setattr(value, "uml_Profile434", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_ElementImport(self):
        return self.__uml_ElementImport

    @uml_ElementImport.setter
    def uml_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ElementImport__uml_ElementImport", None)
        self.__uml_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_PackageableElement43"):
                opp_val = getattr(old_value, "uml_PackageableElement43", None)
                if opp_val == self:
                    setattr(old_value, "uml_PackageableElement43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_PackageableElement43"):
                opp_val = getattr(value, "uml_PackageableElement43", None)
                setattr(value, "uml_PackageableElement43", self)

class uml_TemplateBinding(DirectedRelationship):

    pass
class uml_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "uml_Namespace" = None, uml_PackageImport: "uml_Package" = None, packageImport: "uml_Namespace" = None, uml_PackageImport438: "uml_Profile" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.uml_PackageImport = uml_PackageImport
        self.packageImport = packageImport
        self.uml_PackageImport438 = uml_PackageImport438
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def uml_PackageImport438(self):
        return self.__uml_PackageImport438

    @uml_PackageImport438.setter
    def uml_PackageImport438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_PackageImport__uml_PackageImport438", None)
        self.__uml_PackageImport438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Profile437"):
                opp_val = getattr(old_value, "uml_Profile437", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Profile437"):
                opp_val = getattr(value, "uml_Profile437", None)
                if opp_val is None:
                    setattr(value, "uml_Profile437", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_PackageImport(self):
        return self.__uml_PackageImport

    @uml_PackageImport.setter
    def uml_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_PackageImport__uml_PackageImport", None)
        self.__uml_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Package47"):
                opp_val = getattr(old_value, "uml_Package47", None)
                if opp_val == self:
                    setattr(old_value, "uml_Package47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Package47"):
                opp_val = getattr(value, "uml_Package47", None)
                setattr(value, "uml_Package47", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace33"):
                opp_val = getattr(old_value, "importingNamespace33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace33"):
                opp_val = getattr(value, "importingNamespace33", None)
                if opp_val is None:
                    setattr(value, "importingNamespace33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace49"):
                opp_val = getattr(old_value, "Namespace49", None)
                if opp_val == self:
                    setattr(old_value, "Namespace49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace49"):
                opp_val = getattr(value, "Namespace49", None)
                setattr(value, "Namespace49", self)

class uml_ProtocolConformance(DirectedRelationship):

    pass
class PackageableElement:

    pass
class uml_Observation(PackageableElement):

    pass
class uml_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: str, isDisjoint: str, GeneralizationSet: "uml_Classifier" = None, powertypeExtent: "uml_Classifier" = None, generalizationSet: set["uml_Generalization"] = None, GeneralizationSet132: "uml_Generalization" = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.GeneralizationSet = GeneralizationSet
        self.powertypeExtent = powertypeExtent
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        self.GeneralizationSet132 = GeneralizationSet132
        
    @property
    def isDisjoint(self) -> str:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: str):
        self.__isDisjoint = isDisjoint

    @property
    def isCovering(self) -> str:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: str):
        self.__isCovering = isCovering

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_GeneralizationSet__generalizationSet", None)
        self.__generalizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization138"):
                    opp_val = getattr(item, "Generalization138", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization138"):
                    opp_val = getattr(item, "Generalization138", None)
                    
                    setattr(item, "Generalization138", self)
                    

    @property
    def GeneralizationSet132(self):
        return self.__GeneralizationSet132

    @GeneralizationSet132.setter
    def GeneralizationSet132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_GeneralizationSet__GeneralizationSet132", None)
        self.__GeneralizationSet132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                if opp_val is None:
                    setattr(value, "generalization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_GeneralizationSet__GeneralizationSet", None)
        self.__GeneralizationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "powertype"):
                opp_val = getattr(old_value, "powertype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "powertype"):
                opp_val = getattr(value, "powertype", None)
                if opp_val is None:
                    setattr(value, "powertype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_GeneralizationSet__powertypeExtent", None)
        self.__powertypeExtent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier136"):
                opp_val = getattr(old_value, "Classifier136", None)
                if opp_val == self:
                    setattr(old_value, "Classifier136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier136"):
                opp_val = getattr(value, "Classifier136", None)
                setattr(value, "Classifier136", self)

class uml_InstanceSpecification(PackageableElement, DeploymentTarget, DeployedArtifact):

    pass
class uml_ValueSpecification(TypedElement, PackageableElement):

    pass
class uml_Event(PackageableElement):

    pass
class uml_Dependency(DirectedRelationship, PackageableElement):

    pass
class uml_InformationFlow(DirectedRelationship, PackageableElement):

    pass
class uml_Constraint(PackageableElement):

    pass
class Namespace:

    pass
class uml_State(Vertex, Namespace, RedefinableElement):

    def __init__(self, isComposite: str, isOrthogonal: str, isSimple: str, isSubmachineState: str, State317: "uml_Region" = None, State: "uml_StateMachine" = None, submachineState: "uml_StateMachine" = None, state: set["uml_ConnectionPointReference"] = None, state368: set["uml_Pseudostate"] = None, uml_State: "uml_State" = None, uml_State370: "uml_State" = None, uml_State373: "uml_Constraint" = None, uml_State376: "uml_Behavior" = None, uml_State379: "uml_Behavior" = None, uml_State382: "uml_Behavior" = None, uml_State385: set["uml_Trigger"] = None, State400: "uml_Pseudostate" = None, state388: set["uml_Region"] = None, State395: "uml_ConnectionPointReference" = None, uml_State638: "uml_ObjectNode" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.State317 = State317
        self.State = State
        self.submachineState = submachineState
        self.state = state if state is not None else set()
        self.state368 = state368 if state368 is not None else set()
        self.uml_State = uml_State
        self.uml_State370 = uml_State370
        self.uml_State373 = uml_State373
        self.uml_State376 = uml_State376
        self.uml_State379 = uml_State379
        self.uml_State382 = uml_State382
        self.uml_State385 = uml_State385 if uml_State385 is not None else set()
        self.State400 = State400
        self.state388 = state388 if state388 is not None else set()
        self.State395 = State395
        self.uml_State638 = uml_State638
        
    @property
    def isOrthogonal(self) -> str:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: str):
        self.__isOrthogonal = isOrthogonal

    @property
    def isSubmachineState(self) -> str:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: str):
        self.__isSubmachineState = isSubmachineState

    @property
    def isSimple(self) -> str:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: str):
        self.__isSimple = isSimple

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def uml_State379(self):
        return self.__uml_State379

    @uml_State379.setter
    def uml_State379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State379", None)
        self.__uml_State379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior380"):
                opp_val = getattr(old_value, "uml_Behavior380", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior380"):
                opp_val = getattr(value, "uml_Behavior380", None)
                setattr(value, "uml_Behavior380", self)

    @property
    def submachineState(self):
        return self.__submachineState

    @submachineState.setter
    def submachineState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__submachineState", None)
        self.__submachineState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine365"):
                opp_val = getattr(old_value, "StateMachine365", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine365"):
                opp_val = getattr(value, "StateMachine365", None)
                setattr(value, "StateMachine365", self)

    @property
    def uml_State385(self):
        return self.__uml_State385

    @uml_State385.setter
    def uml_State385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State385", None)
        self.__uml_State385 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Trigger386"):
                    opp_val = getattr(item, "uml_Trigger386", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Trigger386", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Trigger386"):
                    opp_val = getattr(item, "uml_Trigger386", None)
                    
                    setattr(item, "uml_Trigger386", self)
                    

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectionPointReference"):
                    opp_val = getattr(item, "ConnectionPointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectionPointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectionPointReference"):
                    opp_val = getattr(item, "ConnectionPointReference", None)
                    
                    setattr(item, "ConnectionPointReference", self)
                    

    @property
    def uml_State373(self):
        return self.__uml_State373

    @uml_State373.setter
    def uml_State373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State373", None)
        self.__uml_State373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Constraint374"):
                opp_val = getattr(old_value, "uml_Constraint374", None)
                if opp_val == self:
                    setattr(old_value, "uml_Constraint374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Constraint374"):
                opp_val = getattr(value, "uml_Constraint374", None)
                setattr(value, "uml_Constraint374", self)

    @property
    def uml_State376(self):
        return self.__uml_State376

    @uml_State376.setter
    def uml_State376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State376", None)
        self.__uml_State376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior377"):
                opp_val = getattr(old_value, "uml_Behavior377", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior377"):
                opp_val = getattr(value, "uml_Behavior377", None)
                setattr(value, "uml_Behavior377", self)

    @property
    def State317(self):
        return self.__State317

    @State317.setter
    def State317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__State317", None)
        self.__State317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region"):
                opp_val = getattr(old_value, "region", None)
                if opp_val == self:
                    setattr(old_value, "region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region"):
                opp_val = getattr(value, "region", None)
                setattr(value, "region", self)

    @property
    def state368(self):
        return self.__state368

    @state368.setter
    def state368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__state368", None)
        self.__state368 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Pseudostate369"):
                    opp_val = getattr(item, "Pseudostate369", None)
                    
                    if opp_val == self:
                        setattr(item, "Pseudostate369", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Pseudostate369"):
                    opp_val = getattr(item, "Pseudostate369", None)
                    
                    setattr(item, "Pseudostate369", self)
                    

    @property
    def state388(self):
        return self.__state388

    @state388.setter
    def state388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__state388", None)
        self.__state388 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region389"):
                    opp_val = getattr(item, "Region389", None)
                    
                    if opp_val == self:
                        setattr(item, "Region389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region389"):
                    opp_val = getattr(item, "Region389", None)
                    
                    setattr(item, "Region389", self)
                    

    @property
    def State400(self):
        return self.__State400

    @State400.setter
    def State400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__State400", None)
        self.__State400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectionPoint399"):
                opp_val = getattr(old_value, "connectionPoint399", None)
                if opp_val == self:
                    setattr(old_value, "connectionPoint399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectionPoint399"):
                opp_val = getattr(value, "connectionPoint399", None)
                setattr(value, "connectionPoint399", self)

    @property
    def uml_State370(self):
        return self.__uml_State370

    @uml_State370.setter
    def uml_State370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State370", None)
        self.__uml_State370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State"):
                opp_val = getattr(old_value, "uml_State", None)
                if opp_val == self:
                    setattr(old_value, "uml_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State"):
                opp_val = getattr(value, "uml_State", None)
                setattr(value, "uml_State", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "submachine"):
                opp_val = getattr(old_value, "submachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "submachine"):
                opp_val = getattr(value, "submachine", None)
                if opp_val is None:
                    setattr(value, "submachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_State638(self):
        return self.__uml_State638

    @uml_State638.setter
    def uml_State638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State638", None)
        self.__uml_State638 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ObjectNode637"):
                opp_val = getattr(old_value, "uml_ObjectNode637", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ObjectNode637"):
                opp_val = getattr(value, "uml_ObjectNode637", None)
                if opp_val is None:
                    setattr(value, "uml_ObjectNode637", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_State382(self):
        return self.__uml_State382

    @uml_State382.setter
    def uml_State382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State382", None)
        self.__uml_State382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior383"):
                opp_val = getattr(old_value, "uml_Behavior383", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior383"):
                opp_val = getattr(value, "uml_Behavior383", None)
                setattr(value, "uml_Behavior383", self)

    @property
    def State395(self):
        return self.__State395

    @State395.setter
    def State395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__State395", None)
        self.__State395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection"):
                opp_val = getattr(old_value, "connection", None)
                if opp_val == self:
                    setattr(old_value, "connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection"):
                opp_val = getattr(value, "connection", None)
                setattr(value, "connection", self)

    @property
    def uml_State(self):
        return self.__uml_State

    @uml_State.setter
    def uml_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_State__uml_State", None)
        self.__uml_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State370"):
                opp_val = getattr(old_value, "uml_State370", None)
                if opp_val == self:
                    setattr(old_value, "uml_State370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State370"):
                opp_val = getattr(value, "uml_State370", None)
                setattr(value, "uml_State370", self)

class uml_Region(Namespace, RedefinableElement):

    pass
class uml_BehavioralFeature(Feature, Namespace):

    def __init__(self, isAbstract: str, concurrency: str, uml_BehavioralFeature242: set["uml_Type"] = None, uml_BehavioralFeature245: set["uml_ParameterSet"] = None, uml_BehavioralFeature: set["uml_Parameter"] = None, specification: set["uml_Behavior"] = None, BehavioralFeature: "uml_Behavior" = None):
        self.isAbstract = isAbstract
        self.concurrency = concurrency
        self.uml_BehavioralFeature242 = uml_BehavioralFeature242 if uml_BehavioralFeature242 is not None else set()
        self.uml_BehavioralFeature245 = uml_BehavioralFeature245 if uml_BehavioralFeature245 is not None else set()
        self.uml_BehavioralFeature = uml_BehavioralFeature if uml_BehavioralFeature is not None else set()
        self.specification = specification if specification is not None else set()
        self.BehavioralFeature = BehavioralFeature
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_BehavioralFeature__specification", None)
        self.__specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Behavior"):
                    opp_val = getattr(item, "Behavior", None)
                    
                    if opp_val == self:
                        setattr(item, "Behavior", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Behavior"):
                    opp_val = getattr(item, "Behavior", None)
                    
                    setattr(item, "Behavior", self)
                    

    @property
    def uml_BehavioralFeature245(self):
        return self.__uml_BehavioralFeature245

    @uml_BehavioralFeature245.setter
    def uml_BehavioralFeature245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_BehavioralFeature__uml_BehavioralFeature245", None)
        self.__uml_BehavioralFeature245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ParameterSet"):
                    opp_val = getattr(item, "uml_ParameterSet", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ParameterSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ParameterSet"):
                    opp_val = getattr(item, "uml_ParameterSet", None)
                    
                    setattr(item, "uml_ParameterSet", self)
                    

    @property
    def uml_BehavioralFeature(self):
        return self.__uml_BehavioralFeature

    @uml_BehavioralFeature.setter
    def uml_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_BehavioralFeature__uml_BehavioralFeature", None)
        self.__uml_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Parameter239"):
                    opp_val = getattr(item, "uml_Parameter239", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Parameter239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Parameter239"):
                    opp_val = getattr(item, "uml_Parameter239", None)
                    
                    setattr(item, "uml_Parameter239", self)
                    

    @property
    def BehavioralFeature(self):
        return self.__BehavioralFeature

    @BehavioralFeature.setter
    def BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_BehavioralFeature__BehavioralFeature", None)
        self.__BehavioralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "method"):
                opp_val = getattr(old_value, "method", None)
                if opp_val == self:
                    setattr(old_value, "method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "method"):
                opp_val = getattr(value, "method", None)
                setattr(value, "method", self)

    @property
    def uml_BehavioralFeature242(self):
        return self.__uml_BehavioralFeature242

    @uml_BehavioralFeature242.setter
    def uml_BehavioralFeature242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_BehavioralFeature__uml_BehavioralFeature242", None)
        self.__uml_BehavioralFeature242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Type243"):
                    opp_val = getattr(item, "uml_Type243", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Type243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Type243"):
                    opp_val = getattr(item, "uml_Type243", None)
                    
                    setattr(item, "uml_Type243", self)
                    

class uml_InteractionOperand(InteractionFragment, Namespace):

    pass
class uml_StructuredActivityNode(ActivityGroup, Namespace, Action):

    def __init__(self, mustIsolate: str, StructuredActivityNode: "uml_ActivityNode" = None, inStructuredNode: set["uml_ActivityEdge"] = None, inStructuredNode553: set["uml_ActivityNode"] = None, uml_StructuredActivityNode: "uml_Activity" = None, scope: set["uml_Variable"] = None, StructuredActivityNode580: "uml_Variable" = None, StructuredActivityNode602: "uml_ActivityEdge" = None):
        self.mustIsolate = mustIsolate
        self.StructuredActivityNode = StructuredActivityNode
        self.inStructuredNode = inStructuredNode if inStructuredNode is not None else set()
        self.inStructuredNode553 = inStructuredNode553 if inStructuredNode553 is not None else set()
        self.uml_StructuredActivityNode = uml_StructuredActivityNode
        self.scope = scope if scope is not None else set()
        self.StructuredActivityNode580 = StructuredActivityNode580
        self.StructuredActivityNode602 = StructuredActivityNode602
        
    @property
    def mustIsolate(self) -> str:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: str):
        self.__mustIsolate = mustIsolate

    @property
    def inStructuredNode553(self):
        return self.__inStructuredNode553

    @inStructuredNode553.setter
    def inStructuredNode553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuredActivityNode__inStructuredNode553", None)
        self.__inStructuredNode553 = value if value is not None else set()
        
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
                    

    @property
    def uml_StructuredActivityNode(self):
        return self.__uml_StructuredActivityNode

    @uml_StructuredActivityNode.setter
    def uml_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuredActivityNode__uml_StructuredActivityNode", None)
        self.__uml_StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Activity"):
                opp_val = getattr(old_value, "uml_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Activity"):
                opp_val = getattr(value, "uml_Activity", None)
                if opp_val is None:
                    setattr(value, "uml_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inStructuredNode(self):
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuredActivityNode__inStructuredNode", None)
        self.__inStructuredNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge551"):
                    opp_val = getattr(item, "ActivityEdge551", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge551", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge551"):
                    opp_val = getattr(item, "ActivityEdge551", None)
                    
                    setattr(item, "ActivityEdge551", self)
                    

    @property
    def StructuredActivityNode(self):
        return self.__StructuredActivityNode

    @StructuredActivityNode.setter
    def StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuredActivityNode__StructuredActivityNode", None)
        self.__StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if opp_val == self:
                    setattr(old_value, "node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                setattr(value, "node", self)

    @property
    def StructuredActivityNode580(self):
        return self.__StructuredActivityNode580

    @StructuredActivityNode580.setter
    def StructuredActivityNode580(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuredActivityNode__StructuredActivityNode580", None)
        self.__StructuredActivityNode580 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variable"):
                opp_val = getattr(old_value, "variable", None)
                if opp_val == self:
                    setattr(old_value, "variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variable"):
                opp_val = getattr(value, "variable", None)
                setattr(value, "variable", self)

    @property
    def StructuredActivityNode602(self):
        return self.__StructuredActivityNode602

    @StructuredActivityNode602.setter
    def StructuredActivityNode602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuredActivityNode__StructuredActivityNode602", None)
        self.__StructuredActivityNode602 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edge601"):
                opp_val = getattr(old_value, "edge601", None)
                if opp_val == self:
                    setattr(old_value, "edge601", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edge601"):
                opp_val = getattr(value, "edge601", None)
                setattr(value, "edge601", self)

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_StructuredActivityNode__scope", None)
        self.__scope = value if value is not None else set()
        
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
                    

class uml_Transition(Namespace, RedefinableElement):

    def __init__(self, kind: str, Transition: "uml_Region" = None, uml_Transition: "uml_Vertex" = None, uml_Transition325: "uml_Vertex" = None, uml_Transition346: set["uml_Trigger"] = None, transition: "uml_Region" = None, uml_Transition331: "uml_Vertex" = None, uml_Transition334: "uml_Vertex" = None, uml_Transition338: "uml_Transition" = None, uml_Transition336: "uml_Transition" = None, uml_Transition340: "uml_Constraint" = None, uml_Transition343: "uml_Behavior" = None):
        self.kind = kind
        self.Transition = Transition
        self.uml_Transition = uml_Transition
        self.uml_Transition325 = uml_Transition325
        self.uml_Transition346 = uml_Transition346 if uml_Transition346 is not None else set()
        self.transition = transition
        self.uml_Transition331 = uml_Transition331
        self.uml_Transition334 = uml_Transition334
        self.uml_Transition338 = uml_Transition338
        self.uml_Transition336 = uml_Transition336
        self.uml_Transition340 = uml_Transition340
        self.uml_Transition343 = uml_Transition343
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def uml_Transition343(self):
        return self.__uml_Transition343

    @uml_Transition343.setter
    def uml_Transition343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition343", None)
        self.__uml_Transition343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior344"):
                opp_val = getattr(old_value, "uml_Behavior344", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior344"):
                opp_val = getattr(value, "uml_Behavior344", None)
                setattr(value, "uml_Behavior344", self)

    @property
    def uml_Transition(self):
        return self.__uml_Transition

    @uml_Transition.setter
    def uml_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition", None)
        self.__uml_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Vertex"):
                opp_val = getattr(old_value, "uml_Vertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Vertex"):
                opp_val = getattr(value, "uml_Vertex", None)
                if opp_val is None:
                    setattr(value, "uml_Vertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Transition336(self):
        return self.__uml_Transition336

    @uml_Transition336.setter
    def uml_Transition336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition336", None)
        self.__uml_Transition336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Transition338"):
                opp_val = getattr(old_value, "uml_Transition338", None)
                if opp_val == self:
                    setattr(old_value, "uml_Transition338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Transition338"):
                opp_val = getattr(value, "uml_Transition338", None)
                setattr(value, "uml_Transition338", self)

    @property
    def uml_Transition340(self):
        return self.__uml_Transition340

    @uml_Transition340.setter
    def uml_Transition340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition340", None)
        self.__uml_Transition340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Constraint341"):
                opp_val = getattr(old_value, "uml_Constraint341", None)
                if opp_val == self:
                    setattr(old_value, "uml_Constraint341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Constraint341"):
                opp_val = getattr(value, "uml_Constraint341", None)
                setattr(value, "uml_Constraint341", self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region329"):
                opp_val = getattr(old_value, "Region329", None)
                if opp_val == self:
                    setattr(old_value, "Region329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region329"):
                opp_val = getattr(value, "Region329", None)
                setattr(value, "Region329", self)

    @property
    def uml_Transition346(self):
        return self.__uml_Transition346

    @uml_Transition346.setter
    def uml_Transition346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition346", None)
        self.__uml_Transition346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Trigger347"):
                    opp_val = getattr(item, "uml_Trigger347", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Trigger347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Trigger347"):
                    opp_val = getattr(item, "uml_Trigger347", None)
                    
                    setattr(item, "uml_Trigger347", self)
                    

    @property
    def uml_Transition338(self):
        return self.__uml_Transition338

    @uml_Transition338.setter
    def uml_Transition338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition338", None)
        self.__uml_Transition338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Transition336"):
                opp_val = getattr(old_value, "uml_Transition336", None)
                if opp_val == self:
                    setattr(old_value, "uml_Transition336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Transition336"):
                opp_val = getattr(value, "uml_Transition336", None)
                setattr(value, "uml_Transition336", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container315"):
                opp_val = getattr(old_value, "container315", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container315"):
                opp_val = getattr(value, "container315", None)
                if opp_val is None:
                    setattr(value, "container315", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Transition334(self):
        return self.__uml_Transition334

    @uml_Transition334.setter
    def uml_Transition334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition334", None)
        self.__uml_Transition334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Vertex335"):
                opp_val = getattr(old_value, "uml_Vertex335", None)
                if opp_val == self:
                    setattr(old_value, "uml_Vertex335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Vertex335"):
                opp_val = getattr(value, "uml_Vertex335", None)
                setattr(value, "uml_Vertex335", self)

    @property
    def uml_Transition325(self):
        return self.__uml_Transition325

    @uml_Transition325.setter
    def uml_Transition325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition325", None)
        self.__uml_Transition325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Vertex324"):
                opp_val = getattr(old_value, "uml_Vertex324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Vertex324"):
                opp_val = getattr(value, "uml_Vertex324", None)
                if opp_val is None:
                    setattr(value, "uml_Vertex324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Transition331(self):
        return self.__uml_Transition331

    @uml_Transition331.setter
    def uml_Transition331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition331", None)
        self.__uml_Transition331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Vertex332"):
                opp_val = getattr(old_value, "uml_Vertex332", None)
                if opp_val == self:
                    setattr(old_value, "uml_Vertex332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Vertex332"):
                opp_val = getattr(value, "uml_Vertex332", None)
                setattr(value, "uml_Vertex332", self)

class EModelElement:

    pass
class uml_Element(EModelElement):

    pass
class ParameterableElement:

    pass
class uml_ConnectableElement(TypedElement, ParameterableElement):

    pass
class NamedElement:

    pass
class uml_ParameterSet(NamedElement):

    pass
class uml_GeneralOrdering(NamedElement):

    pass
class uml_InteractionFragment(NamedElement):

    pass
class uml_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str, uml_RedefinableElement: "uml_RedefinableElement" = None, uml_RedefinableElement89: set["uml_RedefinableElement"] = None, uml_RedefinableElement92: set["uml_Classifier"] = None):
        self.isLeaf = isLeaf
        self.uml_RedefinableElement = uml_RedefinableElement
        self.uml_RedefinableElement89 = uml_RedefinableElement89 if uml_RedefinableElement89 is not None else set()
        self.uml_RedefinableElement92 = uml_RedefinableElement92 if uml_RedefinableElement92 is not None else set()
        
    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def uml_RedefinableElement89(self):
        return self.__uml_RedefinableElement89

    @uml_RedefinableElement89.setter
    def uml_RedefinableElement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_RedefinableElement__uml_RedefinableElement89", None)
        self.__uml_RedefinableElement89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_RedefinableElement"):
                    opp_val = getattr(item, "uml_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_RedefinableElement"):
                    opp_val = getattr(item, "uml_RedefinableElement", None)
                    
                    setattr(item, "uml_RedefinableElement", self)
                    

    @property
    def uml_RedefinableElement(self):
        return self.__uml_RedefinableElement

    @uml_RedefinableElement.setter
    def uml_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_RedefinableElement__uml_RedefinableElement", None)
        self.__uml_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_RedefinableElement89"):
                opp_val = getattr(old_value, "uml_RedefinableElement89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_RedefinableElement89"):
                opp_val = getattr(value, "uml_RedefinableElement89", None)
                if opp_val is None:
                    setattr(value, "uml_RedefinableElement89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_RedefinableElement92(self):
        return self.__uml_RedefinableElement92

    @uml_RedefinableElement92.setter
    def uml_RedefinableElement92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_RedefinableElement__uml_RedefinableElement92", None)
        self.__uml_RedefinableElement92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier93"):
                    opp_val = getattr(item, "uml_Classifier93", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier93"):
                    opp_val = getattr(item, "uml_Classifier93", None)
                    
                    setattr(item, "uml_Classifier93", self)
                    

class uml_Namespace(NamedElement):

    pass
class uml_CollaborationUse(NamedElement):

    pass
class uml_Extend(DirectedRelationship, NamedElement):

    pass
class uml_Vertex(NamedElement):

    pass
class uml_DeployedArtifact(NamedElement):

    pass
class uml_ActivityPartition(ActivityGroup, NamedElement):

    def __init__(self, isDimension: str, isExternal: str, ActivityPartition: "uml_ActivityNode" = None, ActivityPartition591: "uml_ActivityEdge" = None, uml_ActivityPartition: "uml_Activity" = None, ActivityPartition615: "uml_ActivityPartition" = None, subpartition: "uml_ActivityPartition" = None, uml_ActivityPartition617: "uml_Element" = None, inPartition620: set["uml_ActivityEdge"] = None, inPartition: set["uml_ActivityNode"] = None, ActivityPartition612: "uml_ActivityPartition" = None, superPartition: set["uml_ActivityPartition"] = None):
        self.isDimension = isDimension
        self.isExternal = isExternal
        self.ActivityPartition = ActivityPartition
        self.ActivityPartition591 = ActivityPartition591
        self.uml_ActivityPartition = uml_ActivityPartition
        self.ActivityPartition615 = ActivityPartition615
        self.subpartition = subpartition
        self.uml_ActivityPartition617 = uml_ActivityPartition617
        self.inPartition620 = inPartition620 if inPartition620 is not None else set()
        self.inPartition = inPartition if inPartition is not None else set()
        self.ActivityPartition612 = ActivityPartition612
        self.superPartition = superPartition if superPartition is not None else set()
        
    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def isDimension(self) -> str:
        return self.__isDimension

    @isDimension.setter
    def isDimension(self, isDimension: str):
        self.__isDimension = isDimension

    @property
    def subpartition(self):
        return self.__subpartition

    @subpartition.setter
    def subpartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__subpartition", None)
        self.__subpartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityPartition615"):
                opp_val = getattr(old_value, "ActivityPartition615", None)
                if opp_val == self:
                    setattr(old_value, "ActivityPartition615", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityPartition615"):
                opp_val = getattr(value, "ActivityPartition615", None)
                setattr(value, "ActivityPartition615", self)

    @property
    def uml_ActivityPartition617(self):
        return self.__uml_ActivityPartition617

    @uml_ActivityPartition617.setter
    def uml_ActivityPartition617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__uml_ActivityPartition617", None)
        self.__uml_ActivityPartition617 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Element618"):
                opp_val = getattr(old_value, "uml_Element618", None)
                if opp_val == self:
                    setattr(old_value, "uml_Element618", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Element618"):
                opp_val = getattr(value, "uml_Element618", None)
                setattr(value, "uml_Element618", self)

    @property
    def superPartition(self):
        return self.__superPartition

    @superPartition.setter
    def superPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__superPartition", None)
        self.__superPartition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityPartition612"):
                    opp_val = getattr(item, "ActivityPartition612", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityPartition612", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityPartition612"):
                    opp_val = getattr(item, "ActivityPartition612", None)
                    
                    setattr(item, "ActivityPartition612", self)
                    

    @property
    def ActivityPartition591(self):
        return self.__ActivityPartition591

    @ActivityPartition591.setter
    def ActivityPartition591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__ActivityPartition591", None)
        self.__ActivityPartition591 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edge"):
                opp_val = getattr(old_value, "edge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edge"):
                opp_val = getattr(value, "edge", None)
                if opp_val is None:
                    setattr(value, "edge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityPartition(self):
        return self.__ActivityPartition

    @ActivityPartition.setter
    def ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__ActivityPartition", None)
        self.__ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node543"):
                opp_val = getattr(old_value, "node543", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node543"):
                opp_val = getattr(value, "node543", None)
                if opp_val is None:
                    setattr(value, "node543", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityPartition612(self):
        return self.__ActivityPartition612

    @ActivityPartition612.setter
    def ActivityPartition612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__ActivityPartition612", None)
        self.__ActivityPartition612 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superPartition"):
                opp_val = getattr(old_value, "superPartition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superPartition"):
                opp_val = getattr(value, "superPartition", None)
                if opp_val is None:
                    setattr(value, "superPartition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inPartition620(self):
        return self.__inPartition620

    @inPartition620.setter
    def inPartition620(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__inPartition620", None)
        self.__inPartition620 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge621"):
                    opp_val = getattr(item, "ActivityEdge621", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge621", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge621"):
                    opp_val = getattr(item, "ActivityEdge621", None)
                    
                    setattr(item, "ActivityEdge621", self)
                    

    @property
    def inPartition(self):
        return self.__inPartition

    @inPartition.setter
    def inPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__inPartition", None)
        self.__inPartition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode609"):
                    opp_val = getattr(item, "ActivityNode609", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode609", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode609"):
                    opp_val = getattr(item, "ActivityNode609", None)
                    
                    setattr(item, "ActivityNode609", self)
                    

    @property
    def uml_ActivityPartition(self):
        return self.__uml_ActivityPartition

    @uml_ActivityPartition.setter
    def uml_ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__uml_ActivityPartition", None)
        self.__uml_ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Activity576"):
                opp_val = getattr(old_value, "uml_Activity576", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Activity576"):
                opp_val = getattr(value, "uml_Activity576", None)
                if opp_val is None:
                    setattr(value, "uml_Activity576", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityPartition615(self):
        return self.__ActivityPartition615

    @ActivityPartition615.setter
    def ActivityPartition615(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ActivityPartition__ActivityPartition615", None)
        self.__ActivityPartition615 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subpartition"):
                opp_val = getattr(old_value, "subpartition", None)
                if opp_val == self:
                    setattr(old_value, "subpartition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subpartition"):
                opp_val = getattr(value, "subpartition", None)
                setattr(value, "subpartition", self)

class uml_MessageEnd(NamedElement):

    pass
class uml_Trigger(NamedElement):

    pass
class uml_Message(NamedElement):

    def __init__(self, messageKind: str, messageSort: str, uml_Message683: "uml_MessageEnd" = None, uml_Message: "uml_MessageEnd" = None, uml_Message669: "uml_MessageEnd" = None, uml_Message672: "uml_Connector" = None, message: "uml_Interaction" = None, uml_Message676: set["uml_ValueSpecification"] = None, uml_Message679: "uml_NamedElement" = None, Message: "uml_Interaction" = None, uml_Message923: "uml_InformationFlow" = None):
        self.messageKind = messageKind
        self.messageSort = messageSort
        self.uml_Message683 = uml_Message683
        self.uml_Message = uml_Message
        self.uml_Message669 = uml_Message669
        self.uml_Message672 = uml_Message672
        self.message = message
        self.uml_Message676 = uml_Message676 if uml_Message676 is not None else set()
        self.uml_Message679 = uml_Message679
        self.Message = Message
        self.uml_Message923 = uml_Message923
        
    @property
    def messageSort(self) -> str:
        return self.__messageSort

    @messageSort.setter
    def messageSort(self, messageSort: str):
        self.__messageSort = messageSort

    @property
    def messageKind(self) -> str:
        return self.__messageKind

    @messageKind.setter
    def messageKind(self, messageKind: str):
        self.__messageKind = messageKind

    @property
    def uml_Message669(self):
        return self.__uml_Message669

    @uml_Message669.setter
    def uml_Message669(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__uml_Message669", None)
        self.__uml_Message669 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_MessageEnd670"):
                opp_val = getattr(old_value, "uml_MessageEnd670", None)
                if opp_val == self:
                    setattr(old_value, "uml_MessageEnd670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_MessageEnd670"):
                opp_val = getattr(value, "uml_MessageEnd670", None)
                setattr(value, "uml_MessageEnd670", self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__message", None)
        self.__message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interaction"):
                opp_val = getattr(old_value, "Interaction", None)
                if opp_val == self:
                    setattr(old_value, "Interaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interaction"):
                opp_val = getattr(value, "Interaction", None)
                setattr(value, "Interaction", self)

    @property
    def uml_Message672(self):
        return self.__uml_Message672

    @uml_Message672.setter
    def uml_Message672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__uml_Message672", None)
        self.__uml_Message672 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Connector673"):
                opp_val = getattr(old_value, "uml_Connector673", None)
                if opp_val == self:
                    setattr(old_value, "uml_Connector673", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Connector673"):
                opp_val = getattr(value, "uml_Connector673", None)
                setattr(value, "uml_Connector673", self)

    @property
    def uml_Message676(self):
        return self.__uml_Message676

    @uml_Message676.setter
    def uml_Message676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__uml_Message676", None)
        self.__uml_Message676 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ValueSpecification677"):
                    opp_val = getattr(item, "uml_ValueSpecification677", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ValueSpecification677", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ValueSpecification677"):
                    opp_val = getattr(item, "uml_ValueSpecification677", None)
                    
                    setattr(item, "uml_ValueSpecification677", self)
                    

    @property
    def uml_Message683(self):
        return self.__uml_Message683

    @uml_Message683.setter
    def uml_Message683(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__uml_Message683", None)
        self.__uml_Message683 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_MessageEnd682"):
                opp_val = getattr(old_value, "uml_MessageEnd682", None)
                if opp_val == self:
                    setattr(old_value, "uml_MessageEnd682", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_MessageEnd682"):
                opp_val = getattr(value, "uml_MessageEnd682", None)
                setattr(value, "uml_MessageEnd682", self)

    @property
    def uml_Message679(self):
        return self.__uml_Message679

    @uml_Message679.setter
    def uml_Message679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__uml_Message679", None)
        self.__uml_Message679 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_NamedElement680"):
                opp_val = getattr(old_value, "uml_NamedElement680", None)
                if opp_val == self:
                    setattr(old_value, "uml_NamedElement680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_NamedElement680"):
                opp_val = getattr(value, "uml_NamedElement680", None)
                setattr(value, "uml_NamedElement680", self)

    @property
    def uml_Message923(self):
        return self.__uml_Message923

    @uml_Message923.setter
    def uml_Message923(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__uml_Message923", None)
        self.__uml_Message923 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InformationFlow922"):
                opp_val = getattr(old_value, "uml_InformationFlow922", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InformationFlow922"):
                opp_val = getattr(value, "uml_InformationFlow922", None)
                if opp_val is None:
                    setattr(value, "uml_InformationFlow922", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Message(self):
        return self.__uml_Message

    @uml_Message.setter
    def uml_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__uml_Message", None)
        self.__uml_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_MessageEnd"):
                opp_val = getattr(old_value, "uml_MessageEnd", None)
                if opp_val == self:
                    setattr(old_value, "uml_MessageEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_MessageEnd"):
                opp_val = getattr(value, "uml_MessageEnd", None)
                setattr(value, "uml_MessageEnd", self)

    @property
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Message__Message", None)
        self.__Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction691"):
                opp_val = getattr(old_value, "interaction691", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction691"):
                opp_val = getattr(value, "interaction691", None)
                if opp_val is None:
                    setattr(value, "interaction691", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Lifeline(NamedElement):

    pass
class uml_TypedElement(NamedElement):

    pass
class uml_DeploymentTarget(NamedElement):

    pass
class uml_Include(DirectedRelationship, NamedElement):

    pass
class uml_ProfileApplication(DirectedRelationship):

    def __init__(self, isStrict: str, ProfileApplication: "uml_Package" = None, uml_ProfileApplication: "uml_Profile" = None, profileApplication: "uml_Package" = None):
        self.isStrict = isStrict
        self.ProfileApplication = ProfileApplication
        self.uml_ProfileApplication = uml_ProfileApplication
        self.profileApplication = profileApplication
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

    @property
    def profileApplication(self):
        return self.__profileApplication

    @profileApplication.setter
    def profileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ProfileApplication__profileApplication", None)
        self.__profileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package502"):
                opp_val = getattr(old_value, "Package502", None)
                if opp_val == self:
                    setattr(old_value, "Package502", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package502"):
                opp_val = getattr(value, "Package502", None)
                setattr(value, "Package502", self)

    @property
    def ProfileApplication(self):
        return self.__ProfileApplication

    @ProfileApplication.setter
    def ProfileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ProfileApplication__ProfileApplication", None)
        self.__ProfileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applyingPackage"):
                opp_val = getattr(old_value, "applyingPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applyingPackage"):
                opp_val = getattr(value, "applyingPackage", None)
                if opp_val is None:
                    setattr(value, "applyingPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_ProfileApplication(self):
        return self.__uml_ProfileApplication

    @uml_ProfileApplication.setter
    def uml_ProfileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_ProfileApplication__uml_ProfileApplication", None)
        self.__uml_ProfileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Profile500"):
                opp_val = getattr(old_value, "uml_Profile500", None)
                if opp_val == self:
                    setattr(old_value, "uml_Profile500", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Profile500"):
                opp_val = getattr(value, "uml_Profile500", None)
                setattr(value, "uml_Profile500", self)

class uml_PackageableElement(NamedElement, ParameterableElement):

    pass
class uml_PackageMerge(DirectedRelationship):

    pass
class uml_Type(PackageableElement):

    pass
class TemplateableElement:

    pass
class uml_StringExpression(TemplateableElement, Expression):

    pass
class uml_Operation(BehavioralFeature, TemplateableElement, ParameterableElement):

    def __init__(self, isQuery: str, isOrdered: str, isUnique: str, lower: str, upper: str, uml_Operation: "uml_Parameter" = None, ownedOperation: "uml_Interface" = None, ownedOperation219: "uml_Class" = None, uml_Operation210: "uml_Artifact" = None, uml_Operation224: set["uml_Constraint"] = None, uml_Operation228: "uml_Operation" = None, uml_Operation226: set["uml_Operation"] = None, ownedOperation230: "uml_DataType" = None, uml_Operation233: "uml_Constraint" = None, uml_Operation236: "uml_Type" = None, uml_Operation221: set["uml_Constraint"] = None, Operation: "uml_Class" = None, Operation289: "uml_Interface" = None, Operation447: "uml_DataType" = None, uml_Operation655: "uml_CallOperationAction" = None, uml_Operation747: "uml_SendOperationEvent" = None, uml_Operation753: "uml_ReceiveOperationEvent" = None, uml_Operation757: "uml_CallEvent" = None, uml_Operation1054: "uml_ProtocolTransition" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.uml_Operation = uml_Operation
        self.ownedOperation = ownedOperation
        self.ownedOperation219 = ownedOperation219
        self.uml_Operation210 = uml_Operation210
        self.uml_Operation224 = uml_Operation224 if uml_Operation224 is not None else set()
        self.uml_Operation228 = uml_Operation228
        self.uml_Operation226 = uml_Operation226 if uml_Operation226 is not None else set()
        self.ownedOperation230 = ownedOperation230
        self.uml_Operation233 = uml_Operation233
        self.uml_Operation236 = uml_Operation236
        self.uml_Operation221 = uml_Operation221 if uml_Operation221 is not None else set()
        self.Operation = Operation
        self.Operation289 = Operation289
        self.Operation447 = Operation447
        self.uml_Operation655 = uml_Operation655
        self.uml_Operation747 = uml_Operation747
        self.uml_Operation753 = uml_Operation753
        self.uml_Operation757 = uml_Operation757
        self.uml_Operation1054 = uml_Operation1054
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def uml_Operation1054(self):
        return self.__uml_Operation1054

    @uml_Operation1054.setter
    def uml_Operation1054(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation1054", None)
        self.__uml_Operation1054 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ProtocolTransition1053"):
                opp_val = getattr(old_value, "uml_ProtocolTransition1053", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ProtocolTransition1053"):
                opp_val = getattr(value, "uml_ProtocolTransition1053", None)
                if opp_val is None:
                    setattr(value, "uml_ProtocolTransition1053", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Operation(self):
        return self.__uml_Operation

    @uml_Operation.setter
    def uml_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation", None)
        self.__uml_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Parameter152"):
                opp_val = getattr(old_value, "uml_Parameter152", None)
                if opp_val == self:
                    setattr(old_value, "uml_Parameter152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Parameter152"):
                opp_val = getattr(value, "uml_Parameter152", None)
                setattr(value, "uml_Parameter152", self)

    @property
    def uml_Operation210(self):
        return self.__uml_Operation210

    @uml_Operation210.setter
    def uml_Operation210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation210", None)
        self.__uml_Operation210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Artifact209"):
                opp_val = getattr(old_value, "uml_Artifact209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Artifact209"):
                opp_val = getattr(value, "uml_Artifact209", None)
                if opp_val is None:
                    setattr(value, "uml_Artifact209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Operation757(self):
        return self.__uml_Operation757

    @uml_Operation757.setter
    def uml_Operation757(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation757", None)
        self.__uml_Operation757 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_CallEvent"):
                opp_val = getattr(old_value, "uml_CallEvent", None)
                if opp_val == self:
                    setattr(old_value, "uml_CallEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_CallEvent"):
                opp_val = getattr(value, "uml_CallEvent", None)
                setattr(value, "uml_CallEvent", self)

    @property
    def Operation447(self):
        return self.__Operation447

    @Operation447.setter
    def Operation447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__Operation447", None)
        self.__Operation447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype446"):
                opp_val = getattr(old_value, "datatype446", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype446"):
                opp_val = getattr(value, "datatype446", None)
                if opp_val is None:
                    setattr(value, "datatype446", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Operation224(self):
        return self.__uml_Operation224

    @uml_Operation224.setter
    def uml_Operation224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation224", None)
        self.__uml_Operation224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Constraint225"):
                    opp_val = getattr(item, "uml_Constraint225", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Constraint225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Constraint225"):
                    opp_val = getattr(item, "uml_Constraint225", None)
                    
                    setattr(item, "uml_Constraint225", self)
                    

    @property
    def uml_Operation226(self):
        return self.__uml_Operation226

    @uml_Operation226.setter
    def uml_Operation226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation226", None)
        self.__uml_Operation226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Operation228"):
                    opp_val = getattr(item, "uml_Operation228", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Operation228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Operation228"):
                    opp_val = getattr(item, "uml_Operation228", None)
                    
                    setattr(item, "uml_Operation228", self)
                    

    @property
    def uml_Operation753(self):
        return self.__uml_Operation753

    @uml_Operation753.setter
    def uml_Operation753(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation753", None)
        self.__uml_Operation753 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReceiveOperationEvent"):
                opp_val = getattr(old_value, "uml_ReceiveOperationEvent", None)
                if opp_val == self:
                    setattr(old_value, "uml_ReceiveOperationEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReceiveOperationEvent"):
                opp_val = getattr(value, "uml_ReceiveOperationEvent", None)
                setattr(value, "uml_ReceiveOperationEvent", self)

    @property
    def uml_Operation233(self):
        return self.__uml_Operation233

    @uml_Operation233.setter
    def uml_Operation233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation233", None)
        self.__uml_Operation233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Constraint234"):
                opp_val = getattr(old_value, "uml_Constraint234", None)
                if opp_val == self:
                    setattr(old_value, "uml_Constraint234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Constraint234"):
                opp_val = getattr(value, "uml_Constraint234", None)
                setattr(value, "uml_Constraint234", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Operation655(self):
        return self.__uml_Operation655

    @uml_Operation655.setter
    def uml_Operation655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation655", None)
        self.__uml_Operation655 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_CallOperationAction"):
                opp_val = getattr(old_value, "uml_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "uml_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_CallOperationAction"):
                opp_val = getattr(value, "uml_CallOperationAction", None)
                setattr(value, "uml_CallOperationAction", self)

    @property
    def ownedOperation219(self):
        return self.__ownedOperation219

    @ownedOperation219.setter
    def ownedOperation219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__ownedOperation219", None)
        self.__ownedOperation219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def uml_Operation747(self):
        return self.__uml_Operation747

    @uml_Operation747.setter
    def uml_Operation747(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation747", None)
        self.__uml_Operation747 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_SendOperationEvent"):
                opp_val = getattr(old_value, "uml_SendOperationEvent", None)
                if opp_val == self:
                    setattr(old_value, "uml_SendOperationEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_SendOperationEvent"):
                opp_val = getattr(value, "uml_SendOperationEvent", None)
                setattr(value, "uml_SendOperationEvent", self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface"):
                opp_val = getattr(old_value, "Interface", None)
                if opp_val == self:
                    setattr(old_value, "Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface"):
                opp_val = getattr(value, "Interface", None)
                setattr(value, "Interface", self)

    @property
    def Operation289(self):
        return self.__Operation289

    @Operation289.setter
    def Operation289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__Operation289", None)
        self.__Operation289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interface"):
                opp_val = getattr(old_value, "interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interface"):
                opp_val = getattr(value, "interface", None)
                if opp_val is None:
                    setattr(value, "interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedOperation230(self):
        return self.__ownedOperation230

    @ownedOperation230.setter
    def ownedOperation230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__ownedOperation230", None)
        self.__ownedOperation230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType231"):
                opp_val = getattr(old_value, "DataType231", None)
                if opp_val == self:
                    setattr(old_value, "DataType231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType231"):
                opp_val = getattr(value, "DataType231", None)
                setattr(value, "DataType231", self)

    @property
    def uml_Operation236(self):
        return self.__uml_Operation236

    @uml_Operation236.setter
    def uml_Operation236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation236", None)
        self.__uml_Operation236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Type237"):
                opp_val = getattr(old_value, "uml_Type237", None)
                if opp_val == self:
                    setattr(old_value, "uml_Type237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Type237"):
                opp_val = getattr(value, "uml_Type237", None)
                setattr(value, "uml_Type237", self)

    @property
    def uml_Operation221(self):
        return self.__uml_Operation221

    @uml_Operation221.setter
    def uml_Operation221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation221", None)
        self.__uml_Operation221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Constraint222"):
                    opp_val = getattr(item, "uml_Constraint222", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Constraint222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Constraint222"):
                    opp_val = getattr(item, "uml_Constraint222", None)
                    
                    setattr(item, "uml_Constraint222", self)
                    

    @property
    def uml_Operation228(self):
        return self.__uml_Operation228

    @uml_Operation228.setter
    def uml_Operation228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Operation__uml_Operation228", None)
        self.__uml_Operation228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Operation226"):
                opp_val = getattr(old_value, "uml_Operation226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Operation226"):
                opp_val = getattr(value, "uml_Operation226", None)
                if opp_val is None:
                    setattr(value, "uml_Operation226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Package(TemplateableElement, PackageableElement, Namespace):

    pass
class uml_Classifier(Type, TemplateableElement, Namespace, RedefinableElement):

    def __init__(self, isAbstract: str, specific: set["uml_Generalization"] = None, powertype: set["uml_GeneralizationSet"] = None, featuringClassifier: set["uml_Feature"] = None, uml_Classifier: set["uml_NamedElement"] = None, uml_Classifier73: "uml_Classifier" = None, uml_Classifier71: set["uml_Classifier"] = None, uml_Classifier76: "uml_Classifier" = None, uml_Classifier74: set["uml_Classifier"] = None, substitutingClassifier: set["uml_Substitution"] = None, uml_Classifier82: "uml_CollaborationUse" = None, uml_Classifier84: set["uml_CollaborationUse"] = None, uml_Classifier87: set["uml_UseCase"] = None, subject: set["uml_UseCase"] = None, uml_Classifier79: set["uml_Property"] = None, uml_Classifier93: "uml_RedefinableElement" = None, Classifier: "uml_Generalization" = None, Classifier136: "uml_GeneralizationSet" = None, uml_Classifier130: "uml_Generalization" = None, Classifier144: "uml_Substitution" = None, Classifier140: "uml_Feature" = None, uml_Classifier142: "uml_Substitution" = None, uml_Classifier266: "uml_Class" = None, uml_Classifier292: "uml_Interface" = None, Classifier462: "uml_UseCase" = None, uml_Classifier485: "uml_RedefinableTemplateSignature" = None, uml_Classifier487: "uml_ClassifierTemplateParameter" = None, uml_Classifier506: "uml_InstanceSpecification" = None, uml_Classifier528: "uml_Action" = None, uml_Classifier631: "uml_ExceptionHandler" = None, uml_Classifier774: "uml_ComponentRealization" = None, uml_Classifier794: "uml_CreateObjectAction" = None, uml_Classifier928: "uml_ReadExtentAction" = None, uml_Classifier903: "uml_InformationItem" = None, uml_Classifier908: "uml_InformationFlow" = None, uml_Classifier930: "uml_ReclassifyObjectAction" = None, uml_Classifier933: "uml_ReclassifyObjectAction" = None, uml_Classifier938: "uml_ReadIsClassifiedObjectAction" = None, uml_Classifier984: "uml_UnmarshallAction" = None):
        self.isAbstract = isAbstract
        self.specific = specific if specific is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.uml_Classifier = uml_Classifier if uml_Classifier is not None else set()
        self.uml_Classifier73 = uml_Classifier73
        self.uml_Classifier71 = uml_Classifier71 if uml_Classifier71 is not None else set()
        self.uml_Classifier76 = uml_Classifier76
        self.uml_Classifier74 = uml_Classifier74 if uml_Classifier74 is not None else set()
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        self.uml_Classifier82 = uml_Classifier82
        self.uml_Classifier84 = uml_Classifier84 if uml_Classifier84 is not None else set()
        self.uml_Classifier87 = uml_Classifier87 if uml_Classifier87 is not None else set()
        self.subject = subject if subject is not None else set()
        self.uml_Classifier79 = uml_Classifier79 if uml_Classifier79 is not None else set()
        self.uml_Classifier93 = uml_Classifier93
        self.Classifier = Classifier
        self.Classifier136 = Classifier136
        self.uml_Classifier130 = uml_Classifier130
        self.Classifier144 = Classifier144
        self.Classifier140 = Classifier140
        self.uml_Classifier142 = uml_Classifier142
        self.uml_Classifier266 = uml_Classifier266
        self.uml_Classifier292 = uml_Classifier292
        self.Classifier462 = Classifier462
        self.uml_Classifier485 = uml_Classifier485
        self.uml_Classifier487 = uml_Classifier487
        self.uml_Classifier506 = uml_Classifier506
        self.uml_Classifier528 = uml_Classifier528
        self.uml_Classifier631 = uml_Classifier631
        self.uml_Classifier774 = uml_Classifier774
        self.uml_Classifier794 = uml_Classifier794
        self.uml_Classifier928 = uml_Classifier928
        self.uml_Classifier903 = uml_Classifier903
        self.uml_Classifier908 = uml_Classifier908
        self.uml_Classifier930 = uml_Classifier930
        self.uml_Classifier933 = uml_Classifier933
        self.uml_Classifier938 = uml_Classifier938
        self.uml_Classifier984 = uml_Classifier984
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__powertype", None)
        self.__powertype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet"):
                    opp_val = getattr(item, "GeneralizationSet", None)
                    
                    setattr(item, "GeneralizationSet", self)
                    

    @property
    def uml_Classifier87(self):
        return self.__uml_Classifier87

    @uml_Classifier87.setter
    def uml_Classifier87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier87", None)
        self.__uml_Classifier87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_UseCase"):
                    opp_val = getattr(item, "uml_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_UseCase"):
                    opp_val = getattr(item, "uml_UseCase", None)
                    
                    setattr(item, "uml_UseCase", self)
                    

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization134"):
                opp_val = getattr(old_value, "generalization134", None)
                if opp_val == self:
                    setattr(old_value, "generalization134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization134"):
                opp_val = getattr(value, "generalization134", None)
                setattr(value, "generalization134", self)

    @property
    def uml_Classifier487(self):
        return self.__uml_Classifier487

    @uml_Classifier487.setter
    def uml_Classifier487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier487", None)
        self.__uml_Classifier487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ClassifierTemplateParameter"):
                opp_val = getattr(old_value, "uml_ClassifierTemplateParameter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ClassifierTemplateParameter"):
                opp_val = getattr(value, "uml_ClassifierTemplateParameter", None)
                if opp_val is None:
                    setattr(value, "uml_ClassifierTemplateParameter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier266(self):
        return self.__uml_Classifier266

    @uml_Classifier266.setter
    def uml_Classifier266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier266", None)
        self.__uml_Classifier266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class265"):
                opp_val = getattr(old_value, "uml_Class265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class265"):
                opp_val = getattr(value, "uml_Class265", None)
                if opp_val is None:
                    setattr(value, "uml_Class265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier506(self):
        return self.__uml_Classifier506

    @uml_Classifier506.setter
    def uml_Classifier506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier506", None)
        self.__uml_Classifier506 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InstanceSpecification"):
                opp_val = getattr(old_value, "uml_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InstanceSpecification"):
                opp_val = getattr(value, "uml_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "uml_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier84(self):
        return self.__uml_Classifier84

    @uml_Classifier84.setter
    def uml_Classifier84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier84", None)
        self.__uml_Classifier84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_CollaborationUse85"):
                    opp_val = getattr(item, "uml_CollaborationUse85", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_CollaborationUse85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_CollaborationUse85"):
                    opp_val = getattr(item, "uml_CollaborationUse85", None)
                    
                    setattr(item, "uml_CollaborationUse85", self)
                    

    @property
    def uml_Classifier908(self):
        return self.__uml_Classifier908

    @uml_Classifier908.setter
    def uml_Classifier908(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier908", None)
        self.__uml_Classifier908 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InformationFlow907"):
                opp_val = getattr(old_value, "uml_InformationFlow907", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InformationFlow907"):
                opp_val = getattr(value, "uml_InformationFlow907", None)
                if opp_val is None:
                    setattr(value, "uml_InformationFlow907", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier76(self):
        return self.__uml_Classifier76

    @uml_Classifier76.setter
    def uml_Classifier76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier76", None)
        self.__uml_Classifier76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier74"):
                opp_val = getattr(old_value, "uml_Classifier74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier74"):
                opp_val = getattr(value, "uml_Classifier74", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__specific", None)
        self.__specific = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    setattr(item, "Generalization", self)
                    

    @property
    def uml_Classifier485(self):
        return self.__uml_Classifier485

    @uml_Classifier485.setter
    def uml_Classifier485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier485", None)
        self.__uml_Classifier485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_RedefinableTemplateSignature484"):
                opp_val = getattr(old_value, "uml_RedefinableTemplateSignature484", None)
                if opp_val == self:
                    setattr(old_value, "uml_RedefinableTemplateSignature484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_RedefinableTemplateSignature484"):
                opp_val = getattr(value, "uml_RedefinableTemplateSignature484", None)
                setattr(value, "uml_RedefinableTemplateSignature484", self)

    @property
    def uml_Classifier82(self):
        return self.__uml_Classifier82

    @uml_Classifier82.setter
    def uml_Classifier82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier82", None)
        self.__uml_Classifier82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_CollaborationUse"):
                opp_val = getattr(old_value, "uml_CollaborationUse", None)
                if opp_val == self:
                    setattr(old_value, "uml_CollaborationUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_CollaborationUse"):
                opp_val = getattr(value, "uml_CollaborationUse", None)
                setattr(value, "uml_CollaborationUse", self)

    @property
    def uml_Classifier142(self):
        return self.__uml_Classifier142

    @uml_Classifier142.setter
    def uml_Classifier142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier142", None)
        self.__uml_Classifier142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Substitution"):
                opp_val = getattr(old_value, "uml_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "uml_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Substitution"):
                opp_val = getattr(value, "uml_Substitution", None)
                setattr(value, "uml_Substitution", self)

    @property
    def uml_Classifier631(self):
        return self.__uml_Classifier631

    @uml_Classifier631.setter
    def uml_Classifier631(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier631", None)
        self.__uml_Classifier631 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ExceptionHandler630"):
                opp_val = getattr(old_value, "uml_ExceptionHandler630", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ExceptionHandler630"):
                opp_val = getattr(value, "uml_ExceptionHandler630", None)
                if opp_val is None:
                    setattr(value, "uml_ExceptionHandler630", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier71(self):
        return self.__uml_Classifier71

    @uml_Classifier71.setter
    def uml_Classifier71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier71", None)
        self.__uml_Classifier71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier73"):
                    opp_val = getattr(item, "uml_Classifier73", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier73"):
                    opp_val = getattr(item, "uml_Classifier73", None)
                    
                    setattr(item, "uml_Classifier73", self)
                    

    @property
    def uml_Classifier903(self):
        return self.__uml_Classifier903

    @uml_Classifier903.setter
    def uml_Classifier903(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier903", None)
        self.__uml_Classifier903 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InformationItem"):
                opp_val = getattr(old_value, "uml_InformationItem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InformationItem"):
                opp_val = getattr(value, "uml_InformationItem", None)
                if opp_val is None:
                    setattr(value, "uml_InformationItem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier74(self):
        return self.__uml_Classifier74

    @uml_Classifier74.setter
    def uml_Classifier74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier74", None)
        self.__uml_Classifier74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Classifier76"):
                    opp_val = getattr(item, "uml_Classifier76", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Classifier76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Classifier76"):
                    opp_val = getattr(item, "uml_Classifier76", None)
                    
                    setattr(item, "uml_Classifier76", self)
                    

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__subject", None)
        self.__subject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCase"):
                    opp_val = getattr(item, "UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCase"):
                    opp_val = getattr(item, "UseCase", None)
                    
                    setattr(item, "UseCase", self)
                    

    @property
    def uml_Classifier130(self):
        return self.__uml_Classifier130

    @uml_Classifier130.setter
    def uml_Classifier130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier130", None)
        self.__uml_Classifier130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Generalization"):
                opp_val = getattr(old_value, "uml_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "uml_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Generalization"):
                opp_val = getattr(value, "uml_Generalization", None)
                setattr(value, "uml_Generalization", self)

    @property
    def uml_Classifier79(self):
        return self.__uml_Classifier79

    @uml_Classifier79.setter
    def uml_Classifier79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier79", None)
        self.__uml_Classifier79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Property80"):
                    opp_val = getattr(item, "uml_Property80", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Property80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Property80"):
                    opp_val = getattr(item, "uml_Property80", None)
                    
                    setattr(item, "uml_Property80", self)
                    

    @property
    def uml_Classifier933(self):
        return self.__uml_Classifier933

    @uml_Classifier933.setter
    def uml_Classifier933(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier933", None)
        self.__uml_Classifier933 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReclassifyObjectAction932"):
                opp_val = getattr(old_value, "uml_ReclassifyObjectAction932", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReclassifyObjectAction932"):
                opp_val = getattr(value, "uml_ReclassifyObjectAction932", None)
                if opp_val is None:
                    setattr(value, "uml_ReclassifyObjectAction932", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier928(self):
        return self.__uml_Classifier928

    @uml_Classifier928.setter
    def uml_Classifier928(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier928", None)
        self.__uml_Classifier928 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReadExtentAction927"):
                opp_val = getattr(old_value, "uml_ReadExtentAction927", None)
                if opp_val == self:
                    setattr(old_value, "uml_ReadExtentAction927", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReadExtentAction927"):
                opp_val = getattr(value, "uml_ReadExtentAction927", None)
                setattr(value, "uml_ReadExtentAction927", self)

    @property
    def uml_Classifier774(self):
        return self.__uml_Classifier774

    @uml_Classifier774.setter
    def uml_Classifier774(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier774", None)
        self.__uml_Classifier774 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ComponentRealization"):
                opp_val = getattr(old_value, "uml_ComponentRealization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ComponentRealization"):
                opp_val = getattr(value, "uml_ComponentRealization", None)
                if opp_val is None:
                    setattr(value, "uml_ComponentRealization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier140(self):
        return self.__Classifier140

    @Classifier140.setter
    def Classifier140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier140", None)
        self.__Classifier140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier(self):
        return self.__uml_Classifier

    @uml_Classifier.setter
    def uml_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier", None)
        self.__uml_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_NamedElement70"):
                    opp_val = getattr(item, "uml_NamedElement70", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_NamedElement70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_NamedElement70"):
                    opp_val = getattr(item, "uml_NamedElement70", None)
                    
                    setattr(item, "uml_NamedElement70", self)
                    

    @property
    def Classifier136(self):
        return self.__Classifier136

    @Classifier136.setter
    def Classifier136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier136", None)
        self.__Classifier136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "powertypeExtent"):
                opp_val = getattr(old_value, "powertypeExtent", None)
                if opp_val == self:
                    setattr(old_value, "powertypeExtent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "powertypeExtent"):
                opp_val = getattr(value, "powertypeExtent", None)
                setattr(value, "powertypeExtent", self)

    @property
    def Classifier462(self):
        return self.__Classifier462

    @Classifier462.setter
    def Classifier462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier462", None)
        self.__Classifier462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase461"):
                opp_val = getattr(old_value, "useCase461", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase461"):
                opp_val = getattr(value, "useCase461", None)
                if opp_val is None:
                    setattr(value, "useCase461", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier938(self):
        return self.__uml_Classifier938

    @uml_Classifier938.setter
    def uml_Classifier938(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier938", None)
        self.__uml_Classifier938 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReadIsClassifiedObjectAction"):
                opp_val = getattr(old_value, "uml_ReadIsClassifiedObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "uml_ReadIsClassifiedObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReadIsClassifiedObjectAction"):
                opp_val = getattr(value, "uml_ReadIsClassifiedObjectAction", None)
                setattr(value, "uml_ReadIsClassifiedObjectAction", self)

    @property
    def uml_Classifier73(self):
        return self.__uml_Classifier73

    @uml_Classifier73.setter
    def uml_Classifier73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier73", None)
        self.__uml_Classifier73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier71"):
                opp_val = getattr(old_value, "uml_Classifier71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier71"):
                opp_val = getattr(value, "uml_Classifier71", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__featuringClassifier", None)
        self.__featuringClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def uml_Classifier794(self):
        return self.__uml_Classifier794

    @uml_Classifier794.setter
    def uml_Classifier794(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier794", None)
        self.__uml_Classifier794 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_CreateObjectAction"):
                opp_val = getattr(old_value, "uml_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "uml_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_CreateObjectAction"):
                opp_val = getattr(value, "uml_CreateObjectAction", None)
                setattr(value, "uml_CreateObjectAction", self)

    @property
    def uml_Classifier292(self):
        return self.__uml_Classifier292

    @uml_Classifier292.setter
    def uml_Classifier292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier292", None)
        self.__uml_Classifier292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Interface291"):
                opp_val = getattr(old_value, "uml_Interface291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Interface291"):
                opp_val = getattr(value, "uml_Interface291", None)
                if opp_val is None:
                    setattr(value, "uml_Interface291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier930(self):
        return self.__uml_Classifier930

    @uml_Classifier930.setter
    def uml_Classifier930(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier930", None)
        self.__uml_Classifier930 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ReclassifyObjectAction"):
                opp_val = getattr(old_value, "uml_ReclassifyObjectAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ReclassifyObjectAction"):
                opp_val = getattr(value, "uml_ReclassifyObjectAction", None)
                if opp_val is None:
                    setattr(value, "uml_ReclassifyObjectAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier93(self):
        return self.__uml_Classifier93

    @uml_Classifier93.setter
    def uml_Classifier93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier93", None)
        self.__uml_Classifier93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_RedefinableElement92"):
                opp_val = getattr(old_value, "uml_RedefinableElement92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_RedefinableElement92"):
                opp_val = getattr(value, "uml_RedefinableElement92", None)
                if opp_val is None:
                    setattr(value, "uml_RedefinableElement92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Classifier528(self):
        return self.__uml_Classifier528

    @uml_Classifier528.setter
    def uml_Classifier528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier528", None)
        self.__uml_Classifier528 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Action527"):
                opp_val = getattr(old_value, "uml_Action527", None)
                if opp_val == self:
                    setattr(old_value, "uml_Action527", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Action527"):
                opp_val = getattr(value, "uml_Action527", None)
                setattr(value, "uml_Action527", self)

    @property
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__substitutingClassifier", None)
        self.__substitutingClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    if opp_val == self:
                        setattr(item, "Substitution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Substitution"):
                    opp_val = getattr(item, "Substitution", None)
                    
                    setattr(item, "Substitution", self)
                    

    @property
    def uml_Classifier984(self):
        return self.__uml_Classifier984

    @uml_Classifier984.setter
    def uml_Classifier984(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier984", None)
        self.__uml_Classifier984 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_UnmarshallAction983"):
                opp_val = getattr(old_value, "uml_UnmarshallAction983", None)
                if opp_val == self:
                    setattr(old_value, "uml_UnmarshallAction983", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_UnmarshallAction983"):
                opp_val = getattr(value, "uml_UnmarshallAction983", None)
                setattr(value, "uml_UnmarshallAction983", self)

    @property
    def Classifier144(self):
        return self.__Classifier144

    @Classifier144.setter
    def Classifier144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier144", None)
        self.__Classifier144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "substitution"):
                opp_val = getattr(old_value, "substitution", None)
                if opp_val == self:
                    setattr(old_value, "substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "substitution"):
                opp_val = getattr(value, "substitution", None)
                setattr(value, "substitution", self)

class Element:

    pass
class uml_TemplateParameterSubstitution(Element):

    pass
class uml_TemplateSignature(Element):

    pass
class uml_LinkEndData(Element):

    pass
class uml_Clause(Element):

    pass
class uml_ExceptionHandler(Element):

    pass
class uml_TemplateParameter(Element):

    pass
class uml_QualifierValue(Element):

    pass
class uml_ParameterableElement(Element):

    pass
class uml_ActivityGroup(Element):

    pass
class uml_Relationship(Element):

    pass
class uml_Image(Element):

    def __init__(self, content: str, location: str, format: str, uml_Image: "uml_Stereotype" = None):
        self.content = content
        self.location = location
        self.format = format
        self.uml_Image = uml_Image
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def uml_Image(self):
        return self.__uml_Image

    @uml_Image.setter
    def uml_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Image__uml_Image", None)
        self.__uml_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Stereotype"):
                opp_val = getattr(old_value, "uml_Stereotype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Stereotype"):
                opp_val = getattr(value, "uml_Stereotype", None)
                if opp_val is None:
                    setattr(value, "uml_Stereotype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, uml_NamedElement22: "uml_Dependency" = None, NamedElement: "uml_Dependency" = None, client: set["uml_Dependency"] = None, ownedMember: "uml_Namespace" = None, uml_NamedElement: "uml_StringExpression" = None, uml_NamedElement36: "uml_Namespace" = None, NamedElement41: "uml_Namespace" = None, uml_NamedElement70: "uml_Classifier" = None, uml_NamedElement680: "uml_Message" = None, uml_NamedElement792: "uml_ConsiderIgnoreFragment" = None, uml_NamedElement884: "uml_TimeObservation" = None, uml_NamedElement886: "uml_DurationObservation" = None, uml_NamedElement911: "uml_InformationFlow" = None, uml_NamedElement914: "uml_InformationFlow" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.uml_NamedElement22 = uml_NamedElement22
        self.NamedElement = NamedElement
        self.client = client if client is not None else set()
        self.ownedMember = ownedMember
        self.uml_NamedElement = uml_NamedElement
        self.uml_NamedElement36 = uml_NamedElement36
        self.NamedElement41 = NamedElement41
        self.uml_NamedElement70 = uml_NamedElement70
        self.uml_NamedElement680 = uml_NamedElement680
        self.uml_NamedElement792 = uml_NamedElement792
        self.uml_NamedElement884 = uml_NamedElement884
        self.uml_NamedElement886 = uml_NamedElement886
        self.uml_NamedElement911 = uml_NamedElement911
        self.uml_NamedElement914 = uml_NamedElement914
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clientDependency"):
                opp_val = getattr(old_value, "clientDependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clientDependency"):
                opp_val = getattr(value, "clientDependency", None)
                if opp_val is None:
                    setattr(value, "clientDependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement884(self):
        return self.__uml_NamedElement884

    @uml_NamedElement884.setter
    def uml_NamedElement884(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement884", None)
        self.__uml_NamedElement884 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_TimeObservation"):
                opp_val = getattr(old_value, "uml_TimeObservation", None)
                if opp_val == self:
                    setattr(old_value, "uml_TimeObservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_TimeObservation"):
                opp_val = getattr(value, "uml_TimeObservation", None)
                setattr(value, "uml_TimeObservation", self)

    @property
    def uml_NamedElement914(self):
        return self.__uml_NamedElement914

    @uml_NamedElement914.setter
    def uml_NamedElement914(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement914", None)
        self.__uml_NamedElement914 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InformationFlow913"):
                opp_val = getattr(old_value, "uml_InformationFlow913", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InformationFlow913"):
                opp_val = getattr(value, "uml_InformationFlow913", None)
                if opp_val is None:
                    setattr(value, "uml_InformationFlow913", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement41(self):
        return self.__NamedElement41

    @NamedElement41.setter
    def NamedElement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__NamedElement41", None)
        self.__NamedElement41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                if opp_val is None:
                    setattr(value, "namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement680(self):
        return self.__uml_NamedElement680

    @uml_NamedElement680.setter
    def uml_NamedElement680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement680", None)
        self.__uml_NamedElement680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Message679"):
                opp_val = getattr(old_value, "uml_Message679", None)
                if opp_val == self:
                    setattr(old_value, "uml_Message679", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Message679"):
                opp_val = getattr(value, "uml_Message679", None)
                setattr(value, "uml_Message679", self)

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__client", None)
        self.__client = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    setattr(item, "Dependency", self)
                    

    @property
    def uml_NamedElement70(self):
        return self.__uml_NamedElement70

    @uml_NamedElement70.setter
    def uml_NamedElement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement70", None)
        self.__uml_NamedElement70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Classifier"):
                opp_val = getattr(old_value, "uml_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Classifier"):
                opp_val = getattr(value, "uml_Classifier", None)
                if opp_val is None:
                    setattr(value, "uml_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement(self):
        return self.__uml_NamedElement

    @uml_NamedElement.setter
    def uml_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement", None)
        self.__uml_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_StringExpression"):
                opp_val = getattr(old_value, "uml_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "uml_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_StringExpression"):
                opp_val = getattr(value, "uml_StringExpression", None)
                setattr(value, "uml_StringExpression", self)

    @property
    def uml_NamedElement22(self):
        return self.__uml_NamedElement22

    @uml_NamedElement22.setter
    def uml_NamedElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement22", None)
        self.__uml_NamedElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Dependency"):
                opp_val = getattr(old_value, "uml_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Dependency"):
                opp_val = getattr(value, "uml_Dependency", None)
                if opp_val is None:
                    setattr(value, "uml_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement792(self):
        return self.__uml_NamedElement792

    @uml_NamedElement792.setter
    def uml_NamedElement792(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement792", None)
        self.__uml_NamedElement792 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ConsiderIgnoreFragment"):
                opp_val = getattr(old_value, "uml_ConsiderIgnoreFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ConsiderIgnoreFragment"):
                opp_val = getattr(value, "uml_ConsiderIgnoreFragment", None)
                if opp_val is None:
                    setattr(value, "uml_ConsiderIgnoreFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement36(self):
        return self.__uml_NamedElement36

    @uml_NamedElement36.setter
    def uml_NamedElement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement36", None)
        self.__uml_NamedElement36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Namespace"):
                opp_val = getattr(old_value, "uml_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Namespace"):
                opp_val = getattr(value, "uml_Namespace", None)
                if opp_val is None:
                    setattr(value, "uml_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__ownedMember", None)
        self.__ownedMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

    @property
    def uml_NamedElement911(self):
        return self.__uml_NamedElement911

    @uml_NamedElement911.setter
    def uml_NamedElement911(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement911", None)
        self.__uml_NamedElement911 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_InformationFlow910"):
                opp_val = getattr(old_value, "uml_InformationFlow910", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_InformationFlow910"):
                opp_val = getattr(value, "uml_InformationFlow910", None)
                if opp_val is None:
                    setattr(value, "uml_InformationFlow910", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_NamedElement886(self):
        return self.__uml_NamedElement886

    @uml_NamedElement886.setter
    def uml_NamedElement886(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement886", None)
        self.__uml_NamedElement886 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DurationObservation"):
                opp_val = getattr(old_value, "uml_DurationObservation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DurationObservation"):
                opp_val = getattr(value, "uml_DurationObservation", None)
                if opp_val is None:
                    setattr(value, "uml_DurationObservation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_MultiplicityElement(Element):

    def __init__(self, isOrdered: str, isUnique: str, upper: str, lower: str, uml_MultiplicityElement: "uml_ValueSpecification" = None, uml_MultiplicityElement159: "uml_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.uml_MultiplicityElement = uml_MultiplicityElement
        self.uml_MultiplicityElement159 = uml_MultiplicityElement159
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def uml_MultiplicityElement(self):
        return self.__uml_MultiplicityElement

    @uml_MultiplicityElement.setter
    def uml_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_MultiplicityElement__uml_MultiplicityElement", None)
        self.__uml_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ValueSpecification157"):
                opp_val = getattr(old_value, "uml_ValueSpecification157", None)
                if opp_val == self:
                    setattr(old_value, "uml_ValueSpecification157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ValueSpecification157"):
                opp_val = getattr(value, "uml_ValueSpecification157", None)
                setattr(value, "uml_ValueSpecification157", self)

    @property
    def uml_MultiplicityElement159(self):
        return self.__uml_MultiplicityElement159

    @uml_MultiplicityElement159.setter
    def uml_MultiplicityElement159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_MultiplicityElement__uml_MultiplicityElement159", None)
        self.__uml_MultiplicityElement159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ValueSpecification160"):
                opp_val = getattr(old_value, "uml_ValueSpecification160", None)
                if opp_val == self:
                    setattr(old_value, "uml_ValueSpecification160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ValueSpecification160"):
                opp_val = getattr(value, "uml_ValueSpecification160", None)
                setattr(value, "uml_ValueSpecification160", self)

class uml_TemplateableElement(Element):

    pass
class uml_Slot(Element):

    pass
class uml_Comment(Element):

    def __init__(self, body: str, uml_Comment: set["uml_Element"] = None, uml_Comment8: "uml_Element" = None):
        self.body = body
        self.uml_Comment = uml_Comment if uml_Comment is not None else set()
        self.uml_Comment8 = uml_Comment8
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def uml_Comment8(self):
        return self.__uml_Comment8

    @uml_Comment8.setter
    def uml_Comment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Comment__uml_Comment8", None)
        self.__uml_Comment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Element7"):
                opp_val = getattr(old_value, "uml_Element7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Element7"):
                opp_val = getattr(value, "uml_Element7", None)
                if opp_val is None:
                    setattr(value, "uml_Element7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Comment(self):
        return self.__uml_Comment

    @uml_Comment.setter
    def uml_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Comment__uml_Comment", None)
        self.__uml_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Element"):
                    opp_val = getattr(item, "uml_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Element"):
                    opp_val = getattr(item, "uml_Element", None)
                    
                    setattr(item, "uml_Element", self)
                    

from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
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
class ConnectorKind(Enum):
    assembly = "assembly"
    delegation = "delegation"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class MessageKind(Enum):
    found = "found"
    unknown = "unknown"
    complete = "complete"
    lost = "lost"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class ObjectNodeOrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
    FIFO = "FIFO"
class MessageSort(Enum):
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"


############################################
# Definition of Classes
############################################

class Transition:

    pass
class uml3_0_0_ProtocolTransition(Transition):

    pass
class CentralBufferNode:

    pass
class uml3_0_0_DataStoreNode(CentralBufferNode):

    pass
class AcceptEventAction:

    pass
class uml3_0_0_AcceptCallAction(AcceptEventAction):

    pass
class CreateLinkAction:

    pass
class uml3_0_0_CreateLinkObjectAction(CreateLinkAction):

    pass
class VariableAction:

    pass
class uml3_0_0_ReadVariableAction(VariableAction):

    pass
class WriteVariableAction:

    pass
class uml3_0_0_RemoveVariableValueAction(WriteVariableAction):

    def __init__(self, isRemoveDuplicates: str, uml3_0_0_RemoveVariableValueAction: "uml3_0_0_InputPin" = None):
        self.isRemoveDuplicates = isRemoveDuplicates
        self.uml3_0_0_RemoveVariableValueAction = uml3_0_0_RemoveVariableValueAction
        
    @property
    def isRemoveDuplicates(self) -> str:
        return self.__isRemoveDuplicates

    @isRemoveDuplicates.setter
    def isRemoveDuplicates(self, isRemoveDuplicates: str):
        self.__isRemoveDuplicates = isRemoveDuplicates

    @property
    def uml3_0_0_RemoveVariableValueAction(self):
        return self.__uml3_0_0_RemoveVariableValueAction

    @uml3_0_0_RemoveVariableValueAction.setter
    def uml3_0_0_RemoveVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_RemoveVariableValueAction__uml3_0_0_RemoveVariableValueAction", None)
        self.__uml3_0_0_RemoveVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin897"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin897", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin897", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin897"):
                opp_val = getattr(value, "uml3_0_0_InputPin897", None)
                setattr(value, "uml3_0_0_InputPin897", self)

class uml3_0_0_AddVariableValueAction(WriteVariableAction):

    def __init__(self, isReplaceAll: str, uml3_0_0_AddVariableValueAction: "uml3_0_0_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.uml3_0_0_AddVariableValueAction = uml3_0_0_AddVariableValueAction
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml3_0_0_AddVariableValueAction(self):
        return self.__uml3_0_0_AddVariableValueAction

    @uml3_0_0_AddVariableValueAction.setter
    def uml3_0_0_AddVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_AddVariableValueAction__uml3_0_0_AddVariableValueAction", None)
        self.__uml3_0_0_AddVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin895"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin895", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin895", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin895"):
                opp_val = getattr(value, "uml3_0_0_InputPin895", None)
                setattr(value, "uml3_0_0_InputPin895", self)

class uml3_0_0_ClearVariableAction(VariableAction):

    pass
class uml3_0_0_WriteVariableAction(VariableAction):

    pass
class State:

    pass
class uml3_0_0_FinalState(State):

    pass
class Observation:

    pass
class uml3_0_0_DurationObservation(Observation):

    def __init__(self, firstEvent: str, uml3_0_0_DurationObservation: set["uml3_0_0_NamedElement"] = None):
        self.firstEvent = firstEvent
        self.uml3_0_0_DurationObservation = uml3_0_0_DurationObservation if uml3_0_0_DurationObservation is not None else set()
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

    @property
    def uml3_0_0_DurationObservation(self):
        return self.__uml3_0_0_DurationObservation

    @uml3_0_0_DurationObservation.setter
    def uml3_0_0_DurationObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_DurationObservation__uml3_0_0_DurationObservation", None)
        self.__uml3_0_0_DurationObservation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_NamedElement886"):
                    opp_val = getattr(item, "uml3_0_0_NamedElement886", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_NamedElement886", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_NamedElement886"):
                    opp_val = getattr(item, "uml3_0_0_NamedElement886", None)
                    
                    setattr(item, "uml3_0_0_NamedElement886", self)
                    

class uml3_0_0_TimeObservation(Observation):

    def __init__(self, firstEvent: str, uml3_0_0_TimeObservation: "uml3_0_0_NamedElement" = None):
        self.firstEvent = firstEvent
        self.uml3_0_0_TimeObservation = uml3_0_0_TimeObservation
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

    @property
    def uml3_0_0_TimeObservation(self):
        return self.__uml3_0_0_TimeObservation

    @uml3_0_0_TimeObservation.setter
    def uml3_0_0_TimeObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_TimeObservation__uml3_0_0_TimeObservation", None)
        self.__uml3_0_0_TimeObservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_NamedElement884"):
                opp_val = getattr(old_value, "uml3_0_0_NamedElement884", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_NamedElement884", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_NamedElement884"):
                opp_val = getattr(value, "uml3_0_0_NamedElement884", None)
                setattr(value, "uml3_0_0_NamedElement884", self)

class IntervalConstraint:

    pass
class uml3_0_0_DurationConstraint(IntervalConstraint):

    def __init__(self, firstEvent: str):
        self.firstEvent = firstEvent
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

class uml3_0_0_TimeConstraint(IntervalConstraint):

    def __init__(self, firstEvent: str):
        self.firstEvent = firstEvent
        
    @property
    def firstEvent(self) -> str:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: str):
        self.__firstEvent = firstEvent

class Interval:

    pass
class uml3_0_0_TimeInterval(Interval):

    pass
class uml3_0_0_DurationInterval(Interval):

    pass
class WriteLinkAction:

    pass
class uml3_0_0_DestroyLinkAction(WriteLinkAction):

    pass
class uml3_0_0_CreateLinkAction(WriteLinkAction):

    pass
class LinkEndData:

    pass
class uml3_0_0_LinkEndDestructionData(LinkEndData):

    def __init__(self, isDestroyDuplicates: str, uml3_0_0_LinkEndDestructionData: "uml3_0_0_InputPin" = None):
        self.isDestroyDuplicates = isDestroyDuplicates
        self.uml3_0_0_LinkEndDestructionData = uml3_0_0_LinkEndDestructionData
        
    @property
    def isDestroyDuplicates(self) -> str:
        return self.__isDestroyDuplicates

    @isDestroyDuplicates.setter
    def isDestroyDuplicates(self, isDestroyDuplicates: str):
        self.__isDestroyDuplicates = isDestroyDuplicates

    @property
    def uml3_0_0_LinkEndDestructionData(self):
        return self.__uml3_0_0_LinkEndDestructionData

    @uml3_0_0_LinkEndDestructionData.setter
    def uml3_0_0_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LinkEndDestructionData__uml3_0_0_LinkEndDestructionData", None)
        self.__uml3_0_0_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin851"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin851", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin851", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin851"):
                opp_val = getattr(value, "uml3_0_0_InputPin851", None)
                setattr(value, "uml3_0_0_InputPin851", self)

class uml3_0_0_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: str, uml3_0_0_LinkEndCreationData: "uml3_0_0_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.uml3_0_0_LinkEndCreationData = uml3_0_0_LinkEndCreationData
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml3_0_0_LinkEndCreationData(self):
        return self.__uml3_0_0_LinkEndCreationData

    @uml3_0_0_LinkEndCreationData.setter
    def uml3_0_0_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LinkEndCreationData__uml3_0_0_LinkEndCreationData", None)
        self.__uml3_0_0_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin849"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin849", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin849", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin849"):
                opp_val = getattr(value, "uml3_0_0_InputPin849", None)
                setattr(value, "uml3_0_0_InputPin849", self)

class LinkAction:

    pass
class uml3_0_0_WriteLinkAction(LinkAction):

    pass
class uml3_0_0_ReadLinkAction(LinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class uml3_0_0_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isReplaceAll: str, uml3_0_0_AddStructuralFeatureValueAction: "uml3_0_0_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.uml3_0_0_AddStructuralFeatureValueAction = uml3_0_0_AddStructuralFeatureValueAction
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml3_0_0_AddStructuralFeatureValueAction(self):
        return self.__uml3_0_0_AddStructuralFeatureValueAction

    @uml3_0_0_AddStructuralFeatureValueAction.setter
    def uml3_0_0_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_AddStructuralFeatureValueAction__uml3_0_0_AddStructuralFeatureValueAction", None)
        self.__uml3_0_0_AddStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin827"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin827", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin827", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin827"):
                opp_val = getattr(value, "uml3_0_0_InputPin827", None)
                setattr(value, "uml3_0_0_InputPin827", self)

class uml3_0_0_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isRemoveDuplicates: str, uml3_0_0_RemoveStructuralFeatureValueAction: "uml3_0_0_InputPin" = None):
        self.isRemoveDuplicates = isRemoveDuplicates
        self.uml3_0_0_RemoveStructuralFeatureValueAction = uml3_0_0_RemoveStructuralFeatureValueAction
        
    @property
    def isRemoveDuplicates(self) -> str:
        return self.__isRemoveDuplicates

    @isRemoveDuplicates.setter
    def isRemoveDuplicates(self, isRemoveDuplicates: str):
        self.__isRemoveDuplicates = isRemoveDuplicates

    @property
    def uml3_0_0_RemoveStructuralFeatureValueAction(self):
        return self.__uml3_0_0_RemoveStructuralFeatureValueAction

    @uml3_0_0_RemoveStructuralFeatureValueAction.setter
    def uml3_0_0_RemoveStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_RemoveStructuralFeatureValueAction__uml3_0_0_RemoveStructuralFeatureValueAction", None)
        self.__uml3_0_0_RemoveStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin825"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin825", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin825", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin825"):
                opp_val = getattr(value, "uml3_0_0_InputPin825", None)
                setattr(value, "uml3_0_0_InputPin825", self)

class StructuralFeatureAction:

    pass
class uml3_0_0_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class uml3_0_0_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class uml3_0_0_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class CombinedFragment:

    pass
class uml3_0_0_ConsiderIgnoreFragment(CombinedFragment):

    pass
class Node:

    pass
class uml3_0_0_ExecutionEnvironment(Node):

    pass
class uml3_0_0_Device(Node):

    pass
class FinalNode:

    pass
class uml3_0_0_ActivityFinalNode(FinalNode):

    pass
class uml3_0_0_FlowFinalNode(FinalNode):

    pass
class OccurrenceSpecification:

    pass
class uml3_0_0_ExecutionOccurrenceSpecification(OccurrenceSpecification):

    pass
class MessageEvent:

    pass
class uml3_0_0_ReceiveSignalEvent(MessageEvent):

    pass
class uml3_0_0_AnyReceiveEvent(MessageEvent):

    pass
class uml3_0_0_CallEvent(MessageEvent):

    pass
class uml3_0_0_ReceiveOperationEvent(MessageEvent):

    pass
class uml3_0_0_SendSignalEvent(MessageEvent):

    pass
class uml3_0_0_SignalEvent(MessageEvent):

    pass
class uml3_0_0_SendOperationEvent(MessageEvent):

    pass
class Event:

    pass
class uml3_0_0_MessageEvent(Event):

    pass
class uml3_0_0_TimeEvent(Event):

    def __init__(self, isRelative: str, uml3_0_0_TimeEvent: "uml3_0_0_TimeExpression" = None):
        self.isRelative = isRelative
        self.uml3_0_0_TimeEvent = uml3_0_0_TimeEvent
        
    @property
    def isRelative(self) -> str:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: str):
        self.__isRelative = isRelative

    @property
    def uml3_0_0_TimeEvent(self):
        return self.__uml3_0_0_TimeEvent

    @uml3_0_0_TimeEvent.setter
    def uml3_0_0_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_TimeEvent__uml3_0_0_TimeEvent", None)
        self.__uml3_0_0_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_TimeExpression888"):
                opp_val = getattr(old_value, "uml3_0_0_TimeExpression888", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_TimeExpression888", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_TimeExpression888"):
                opp_val = getattr(value, "uml3_0_0_TimeExpression888", None)
                setattr(value, "uml3_0_0_TimeExpression888", self)

class uml3_0_0_CreationEvent(Event):

    pass
class uml3_0_0_DestructionEvent(Event):

    pass
class uml3_0_0_ChangeEvent(Event):

    pass
class uml3_0_0_ExecutionEvent(Event):

    pass
class ExecutionSpecification:

    pass
class uml3_0_0_BehaviorExecutionSpecification(ExecutionSpecification):

    pass
class uml3_0_0_ActionExecutionSpecification(ExecutionSpecification):

    pass
class Constraint:

    pass
class uml3_0_0_IntervalConstraint(Constraint):

    pass
class uml3_0_0_InteractionConstraint(Constraint):

    pass
class MessageEnd:

    pass
class uml3_0_0_MessageOccurrenceSpecification(OccurrenceSpecification, MessageEnd):

    pass
class InteractionUse:

    pass
class uml3_0_0_PartDecomposition(InteractionUse):

    pass
class uml3_0_0_Gate(MessageEnd):

    pass
class InteractionFragment:

    pass
class uml3_0_0_StateInvariant(InteractionFragment):

    pass
class uml3_0_0_CombinedFragment(InteractionFragment):

    def __init__(self, interactionOperator: str, uml3_0_0_CombinedFragment789: set["uml3_0_0_Gate"] = None, uml3_0_0_CombinedFragment: set["uml3_0_0_InteractionOperand"] = None):
        self.interactionOperator = interactionOperator
        self.uml3_0_0_CombinedFragment789 = uml3_0_0_CombinedFragment789 if uml3_0_0_CombinedFragment789 is not None else set()
        self.uml3_0_0_CombinedFragment = uml3_0_0_CombinedFragment if uml3_0_0_CombinedFragment is not None else set()
        
    @property
    def interactionOperator(self) -> str:
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator

    @property
    def uml3_0_0_CombinedFragment(self):
        return self.__uml3_0_0_CombinedFragment

    @uml3_0_0_CombinedFragment.setter
    def uml3_0_0_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_CombinedFragment__uml3_0_0_CombinedFragment", None)
        self.__uml3_0_0_CombinedFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_InteractionOperand787"):
                    opp_val = getattr(item, "uml3_0_0_InteractionOperand787", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_InteractionOperand787", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_InteractionOperand787"):
                    opp_val = getattr(item, "uml3_0_0_InteractionOperand787", None)
                    
                    setattr(item, "uml3_0_0_InteractionOperand787", self)
                    

    @property
    def uml3_0_0_CombinedFragment789(self):
        return self.__uml3_0_0_CombinedFragment789

    @uml3_0_0_CombinedFragment789.setter
    def uml3_0_0_CombinedFragment789(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_CombinedFragment__uml3_0_0_CombinedFragment789", None)
        self.__uml3_0_0_CombinedFragment789 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Gate790"):
                    opp_val = getattr(item, "uml3_0_0_Gate790", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Gate790", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Gate790"):
                    opp_val = getattr(item, "uml3_0_0_Gate790", None)
                    
                    setattr(item, "uml3_0_0_Gate790", self)
                    

class uml3_0_0_OccurrenceSpecification(InteractionFragment):

    pass
class uml3_0_0_InteractionUse(InteractionFragment):

    pass
class uml3_0_0_Continuation(InteractionFragment):

    def __init__(self, setting: str):
        self.setting = setting
        
    @property
    def setting(self) -> str:
        return self.__setting

    @setting.setter
    def setting(self, setting: str):
        self.__setting = setting

class uml3_0_0_ExecutionSpecification(InteractionFragment):

    pass
class StructuredActivityNode:

    pass
class uml3_0_0_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: str, uml3_0_0_LoopNode1039: set["uml3_0_0_OutputPin"] = None, uml3_0_0_LoopNode1042: set["uml3_0_0_InputPin"] = None, uml3_0_0_LoopNode: set["uml3_0_0_ExecutableNode"] = None, uml3_0_0_LoopNode1024: set["uml3_0_0_ExecutableNode"] = None, uml3_0_0_LoopNode1027: "uml3_0_0_OutputPin" = None, uml3_0_0_LoopNode1030: set["uml3_0_0_ExecutableNode"] = None, uml3_0_0_LoopNode1033: set["uml3_0_0_OutputPin"] = None, uml3_0_0_LoopNode1036: set["uml3_0_0_OutputPin"] = None):
        self.isTestedFirst = isTestedFirst
        self.uml3_0_0_LoopNode1039 = uml3_0_0_LoopNode1039 if uml3_0_0_LoopNode1039 is not None else set()
        self.uml3_0_0_LoopNode1042 = uml3_0_0_LoopNode1042 if uml3_0_0_LoopNode1042 is not None else set()
        self.uml3_0_0_LoopNode = uml3_0_0_LoopNode if uml3_0_0_LoopNode is not None else set()
        self.uml3_0_0_LoopNode1024 = uml3_0_0_LoopNode1024 if uml3_0_0_LoopNode1024 is not None else set()
        self.uml3_0_0_LoopNode1027 = uml3_0_0_LoopNode1027
        self.uml3_0_0_LoopNode1030 = uml3_0_0_LoopNode1030 if uml3_0_0_LoopNode1030 is not None else set()
        self.uml3_0_0_LoopNode1033 = uml3_0_0_LoopNode1033 if uml3_0_0_LoopNode1033 is not None else set()
        self.uml3_0_0_LoopNode1036 = uml3_0_0_LoopNode1036 if uml3_0_0_LoopNode1036 is not None else set()
        
    @property
    def isTestedFirst(self) -> str:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: str):
        self.__isTestedFirst = isTestedFirst

    @property
    def uml3_0_0_LoopNode1024(self):
        return self.__uml3_0_0_LoopNode1024

    @uml3_0_0_LoopNode1024.setter
    def uml3_0_0_LoopNode1024(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode1024", None)
        self.__uml3_0_0_LoopNode1024 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ExecutableNode1025"):
                    opp_val = getattr(item, "uml3_0_0_ExecutableNode1025", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ExecutableNode1025", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ExecutableNode1025"):
                    opp_val = getattr(item, "uml3_0_0_ExecutableNode1025", None)
                    
                    setattr(item, "uml3_0_0_ExecutableNode1025", self)
                    

    @property
    def uml3_0_0_LoopNode1036(self):
        return self.__uml3_0_0_LoopNode1036

    @uml3_0_0_LoopNode1036.setter
    def uml3_0_0_LoopNode1036(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode1036", None)
        self.__uml3_0_0_LoopNode1036 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_OutputPin1037"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1037", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_OutputPin1037", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_OutputPin1037"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1037", None)
                    
                    setattr(item, "uml3_0_0_OutputPin1037", self)
                    

    @property
    def uml3_0_0_LoopNode1039(self):
        return self.__uml3_0_0_LoopNode1039

    @uml3_0_0_LoopNode1039.setter
    def uml3_0_0_LoopNode1039(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode1039", None)
        self.__uml3_0_0_LoopNode1039 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_OutputPin1040"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1040", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_OutputPin1040", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_OutputPin1040"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1040", None)
                    
                    setattr(item, "uml3_0_0_OutputPin1040", self)
                    

    @property
    def uml3_0_0_LoopNode1033(self):
        return self.__uml3_0_0_LoopNode1033

    @uml3_0_0_LoopNode1033.setter
    def uml3_0_0_LoopNode1033(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode1033", None)
        self.__uml3_0_0_LoopNode1033 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_OutputPin1034"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1034", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_OutputPin1034", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_OutputPin1034"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1034", None)
                    
                    setattr(item, "uml3_0_0_OutputPin1034", self)
                    

    @property
    def uml3_0_0_LoopNode(self):
        return self.__uml3_0_0_LoopNode

    @uml3_0_0_LoopNode.setter
    def uml3_0_0_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode", None)
        self.__uml3_0_0_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ExecutableNode1022"):
                    opp_val = getattr(item, "uml3_0_0_ExecutableNode1022", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ExecutableNode1022", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ExecutableNode1022"):
                    opp_val = getattr(item, "uml3_0_0_ExecutableNode1022", None)
                    
                    setattr(item, "uml3_0_0_ExecutableNode1022", self)
                    

    @property
    def uml3_0_0_LoopNode1027(self):
        return self.__uml3_0_0_LoopNode1027

    @uml3_0_0_LoopNode1027.setter
    def uml3_0_0_LoopNode1027(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode1027", None)
        self.__uml3_0_0_LoopNode1027 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_OutputPin1028"):
                opp_val = getattr(old_value, "uml3_0_0_OutputPin1028", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_OutputPin1028", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_OutputPin1028"):
                opp_val = getattr(value, "uml3_0_0_OutputPin1028", None)
                setattr(value, "uml3_0_0_OutputPin1028", self)

    @property
    def uml3_0_0_LoopNode1042(self):
        return self.__uml3_0_0_LoopNode1042

    @uml3_0_0_LoopNode1042.setter
    def uml3_0_0_LoopNode1042(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode1042", None)
        self.__uml3_0_0_LoopNode1042 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_InputPin1043"):
                    opp_val = getattr(item, "uml3_0_0_InputPin1043", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_InputPin1043", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_InputPin1043"):
                    opp_val = getattr(item, "uml3_0_0_InputPin1043", None)
                    
                    setattr(item, "uml3_0_0_InputPin1043", self)
                    

    @property
    def uml3_0_0_LoopNode1030(self):
        return self.__uml3_0_0_LoopNode1030

    @uml3_0_0_LoopNode1030.setter
    def uml3_0_0_LoopNode1030(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_LoopNode__uml3_0_0_LoopNode1030", None)
        self.__uml3_0_0_LoopNode1030 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ExecutableNode1031"):
                    opp_val = getattr(item, "uml3_0_0_ExecutableNode1031", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ExecutableNode1031", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ExecutableNode1031"):
                    opp_val = getattr(item, "uml3_0_0_ExecutableNode1031", None)
                    
                    setattr(item, "uml3_0_0_ExecutableNode1031", self)
                    

class uml3_0_0_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: str, isAssured: str, uml3_0_0_ConditionalNode1002: set["uml3_0_0_OutputPin"] = None, uml3_0_0_ConditionalNode: set["uml3_0_0_Clause"] = None):
        self.isDeterminate = isDeterminate
        self.isAssured = isAssured
        self.uml3_0_0_ConditionalNode1002 = uml3_0_0_ConditionalNode1002 if uml3_0_0_ConditionalNode1002 is not None else set()
        self.uml3_0_0_ConditionalNode = uml3_0_0_ConditionalNode if uml3_0_0_ConditionalNode is not None else set()
        
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
    def uml3_0_0_ConditionalNode1002(self):
        return self.__uml3_0_0_ConditionalNode1002

    @uml3_0_0_ConditionalNode1002.setter
    def uml3_0_0_ConditionalNode1002(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ConditionalNode__uml3_0_0_ConditionalNode1002", None)
        self.__uml3_0_0_ConditionalNode1002 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_OutputPin1003"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1003", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_OutputPin1003", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_OutputPin1003"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin1003", None)
                    
                    setattr(item, "uml3_0_0_OutputPin1003", self)
                    

    @property
    def uml3_0_0_ConditionalNode(self):
        return self.__uml3_0_0_ConditionalNode

    @uml3_0_0_ConditionalNode.setter
    def uml3_0_0_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ConditionalNode__uml3_0_0_ConditionalNode", None)
        self.__uml3_0_0_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Clause"):
                    opp_val = getattr(item, "uml3_0_0_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Clause"):
                    opp_val = getattr(item, "uml3_0_0_Clause", None)
                    
                    setattr(item, "uml3_0_0_Clause", self)
                    

class uml3_0_0_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, ExpansionRegion: "uml3_0_0_ExpansionNode" = None, ExpansionRegion1046: "uml3_0_0_ExpansionNode" = None, regionAsInput: set["uml3_0_0_ExpansionNode"] = None, regionAsOutput: set["uml3_0_0_ExpansionNode"] = None):
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
    def regionAsInput(self):
        return self.__regionAsInput

    @regionAsInput.setter
    def regionAsInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ExpansionRegion__regionAsInput", None)
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
                    

    @property
    def ExpansionRegion(self):
        return self.__ExpansionRegion

    @ExpansionRegion.setter
    def ExpansionRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ExpansionRegion__ExpansionRegion", None)
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
    def ExpansionRegion1046(self):
        return self.__ExpansionRegion1046

    @ExpansionRegion1046.setter
    def ExpansionRegion1046(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ExpansionRegion__ExpansionRegion1046", None)
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
    def regionAsOutput(self):
        return self.__regionAsOutput

    @regionAsOutput.setter
    def regionAsOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ExpansionRegion__regionAsOutput", None)
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
                    

class uml3_0_0_SequenceNode(StructuredActivityNode):

    pass
class InputPin:

    pass
class uml3_0_0_ActionInputPin(InputPin):

    pass
class uml3_0_0_ValuePin(InputPin):

    pass
class ControlNode:

    pass
class uml3_0_0_DecisionNode(ControlNode):

    pass
class uml3_0_0_FinalNode(ControlNode):

    pass
class uml3_0_0_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: str, uml3_0_0_JoinNode: "uml3_0_0_ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.uml3_0_0_JoinNode = uml3_0_0_JoinNode
        
    @property
    def isCombineDuplicate(self) -> str:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: str):
        self.__isCombineDuplicate = isCombineDuplicate

    @property
    def uml3_0_0_JoinNode(self):
        return self.__uml3_0_0_JoinNode

    @uml3_0_0_JoinNode.setter
    def uml3_0_0_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_JoinNode__uml3_0_0_JoinNode", None)
        self.__uml3_0_0_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ValueSpecification999"):
                opp_val = getattr(old_value, "uml3_0_0_ValueSpecification999", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ValueSpecification999", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ValueSpecification999"):
                opp_val = getattr(value, "uml3_0_0_ValueSpecification999", None)
                setattr(value, "uml3_0_0_ValueSpecification999", self)

class uml3_0_0_ForkNode(ControlNode):

    pass
class uml3_0_0_MergeNode(ControlNode):

    pass
class uml3_0_0_InitialNode(ControlNode):

    pass
class ActivityEdge:

    pass
class uml3_0_0_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: str, isMultireceive: str, uml3_0_0_ObjectFlow: "uml3_0_0_DecisionNode" = None, uml3_0_0_ObjectFlow767: "uml3_0_0_Behavior" = None, uml3_0_0_ObjectFlow770: "uml3_0_0_Behavior" = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.uml3_0_0_ObjectFlow = uml3_0_0_ObjectFlow
        self.uml3_0_0_ObjectFlow767 = uml3_0_0_ObjectFlow767
        self.uml3_0_0_ObjectFlow770 = uml3_0_0_ObjectFlow770
        
    @property
    def isMulticast(self) -> str:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: str):
        self.__isMulticast = isMulticast

    @property
    def isMultireceive(self) -> str:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: str):
        self.__isMultireceive = isMultireceive

    @property
    def uml3_0_0_ObjectFlow770(self):
        return self.__uml3_0_0_ObjectFlow770

    @uml3_0_0_ObjectFlow770.setter
    def uml3_0_0_ObjectFlow770(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ObjectFlow__uml3_0_0_ObjectFlow770", None)
        self.__uml3_0_0_ObjectFlow770 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior771"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior771", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior771", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior771"):
                opp_val = getattr(value, "uml3_0_0_Behavior771", None)
                setattr(value, "uml3_0_0_Behavior771", self)

    @property
    def uml3_0_0_ObjectFlow(self):
        return self.__uml3_0_0_ObjectFlow

    @uml3_0_0_ObjectFlow.setter
    def uml3_0_0_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ObjectFlow__uml3_0_0_ObjectFlow", None)
        self.__uml3_0_0_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_DecisionNode765"):
                opp_val = getattr(old_value, "uml3_0_0_DecisionNode765", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_DecisionNode765", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_DecisionNode765"):
                opp_val = getattr(value, "uml3_0_0_DecisionNode765", None)
                setattr(value, "uml3_0_0_DecisionNode765", self)

    @property
    def uml3_0_0_ObjectFlow767(self):
        return self.__uml3_0_0_ObjectFlow767

    @uml3_0_0_ObjectFlow767.setter
    def uml3_0_0_ObjectFlow767(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ObjectFlow__uml3_0_0_ObjectFlow767", None)
        self.__uml3_0_0_ObjectFlow767 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior768"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior768", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior768", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior768"):
                opp_val = getattr(value, "uml3_0_0_Behavior768", None)
                setattr(value, "uml3_0_0_Behavior768", self)

class uml3_0_0_ControlFlow(ActivityEdge):

    pass
class CallAction:

    pass
class uml3_0_0_CallBehaviorAction(CallAction):

    pass
class uml3_0_0_StartObjectBehaviorAction(CallAction):

    pass
class uml3_0_0_CallOperationAction(CallAction):

    pass
class InvocationAction:

    pass
class uml3_0_0_BroadcastSignalAction(InvocationAction):

    pass
class uml3_0_0_SendObjectAction(InvocationAction):

    pass
class uml3_0_0_SendSignalAction(InvocationAction):

    pass
class uml3_0_0_CallAction(InvocationAction):

    def __init__(self, isSynchronous: str, uml3_0_0_CallAction: set["uml3_0_0_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.uml3_0_0_CallAction = uml3_0_0_CallAction if uml3_0_0_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> str:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: str):
        self.__isSynchronous = isSynchronous

    @property
    def uml3_0_0_CallAction(self):
        return self.__uml3_0_0_CallAction

    @uml3_0_0_CallAction.setter
    def uml3_0_0_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_CallAction__uml3_0_0_CallAction", None)
        self.__uml3_0_0_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_OutputPin643"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin643", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_OutputPin643", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_OutputPin643"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin643", None)
                    
                    setattr(item, "uml3_0_0_OutputPin643", self)
                    

class ObjectNode:

    pass
class uml3_0_0_ExpansionNode(ObjectNode):

    pass
class uml3_0_0_CentralBufferNode(ObjectNode):

    pass
class uml3_0_0_ActivityParameterNode(ObjectNode):

    pass
class Pin:

    pass
class ActivityGroup:

    pass
class uml3_0_0_InterruptibleActivityRegion(ActivityGroup):

    pass
class ActivityNode:

    pass
class uml3_0_0_ControlNode(ActivityNode):

    pass
class uml3_0_0_ExecutableNode(ActivityNode):

    pass
class ExecutableNode:

    pass
class uml3_0_0_Action(ExecutableNode):

    pass
class uml3_0_0_OutputPin(Pin):

    pass
class uml3_0_0_InputPin(Pin):

    pass
class Action:

    pass
class uml3_0_0_UnmarshallAction(Action):

    pass
class uml3_0_0_StructuralFeatureAction(Action):

    pass
class uml3_0_0_ValueSpecificationAction(Action):

    pass
class uml3_0_0_InvocationAction(Action):

    pass
class uml3_0_0_ReadLinkObjectEndQualifierAction(Action):

    pass
class uml3_0_0_ClearAssociationAction(Action):

    pass
class uml3_0_0_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: str, uml3_0_0_ReclassifyObjectAction: set["uml3_0_0_Classifier"] = None, uml3_0_0_ReclassifyObjectAction935: "uml3_0_0_InputPin" = None, uml3_0_0_ReclassifyObjectAction932: set["uml3_0_0_Classifier"] = None):
        self.isReplaceAll = isReplaceAll
        self.uml3_0_0_ReclassifyObjectAction = uml3_0_0_ReclassifyObjectAction if uml3_0_0_ReclassifyObjectAction is not None else set()
        self.uml3_0_0_ReclassifyObjectAction935 = uml3_0_0_ReclassifyObjectAction935
        self.uml3_0_0_ReclassifyObjectAction932 = uml3_0_0_ReclassifyObjectAction932 if uml3_0_0_ReclassifyObjectAction932 is not None else set()
        
    @property
    def isReplaceAll(self) -> str:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: str):
        self.__isReplaceAll = isReplaceAll

    @property
    def uml3_0_0_ReclassifyObjectAction932(self):
        return self.__uml3_0_0_ReclassifyObjectAction932

    @uml3_0_0_ReclassifyObjectAction932.setter
    def uml3_0_0_ReclassifyObjectAction932(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReclassifyObjectAction__uml3_0_0_ReclassifyObjectAction932", None)
        self.__uml3_0_0_ReclassifyObjectAction932 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Classifier933"):
                    opp_val = getattr(item, "uml3_0_0_Classifier933", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Classifier933", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Classifier933"):
                    opp_val = getattr(item, "uml3_0_0_Classifier933", None)
                    
                    setattr(item, "uml3_0_0_Classifier933", self)
                    

    @property
    def uml3_0_0_ReclassifyObjectAction935(self):
        return self.__uml3_0_0_ReclassifyObjectAction935

    @uml3_0_0_ReclassifyObjectAction935.setter
    def uml3_0_0_ReclassifyObjectAction935(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReclassifyObjectAction__uml3_0_0_ReclassifyObjectAction935", None)
        self.__uml3_0_0_ReclassifyObjectAction935 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin936"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin936", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin936", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin936"):
                opp_val = getattr(value, "uml3_0_0_InputPin936", None)
                setattr(value, "uml3_0_0_InputPin936", self)

    @property
    def uml3_0_0_ReclassifyObjectAction(self):
        return self.__uml3_0_0_ReclassifyObjectAction

    @uml3_0_0_ReclassifyObjectAction.setter
    def uml3_0_0_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReclassifyObjectAction__uml3_0_0_ReclassifyObjectAction", None)
        self.__uml3_0_0_ReclassifyObjectAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Classifier930"):
                    opp_val = getattr(item, "uml3_0_0_Classifier930", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Classifier930", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Classifier930"):
                    opp_val = getattr(item, "uml3_0_0_Classifier930", None)
                    
                    setattr(item, "uml3_0_0_Classifier930", self)
                    

class uml3_0_0_TestIdentityAction(Action):

    pass
class uml3_0_0_CreateObjectAction(Action):

    pass
class uml3_0_0_LinkAction(Action):

    pass
class uml3_0_0_ReduceAction(Action):

    def __init__(self, isOrdered: str, uml3_0_0_ReduceAction: "uml3_0_0_Behavior" = None, uml3_0_0_ReduceAction991: "uml3_0_0_OutputPin" = None, uml3_0_0_ReduceAction994: "uml3_0_0_InputPin" = None):
        self.isOrdered = isOrdered
        self.uml3_0_0_ReduceAction = uml3_0_0_ReduceAction
        self.uml3_0_0_ReduceAction991 = uml3_0_0_ReduceAction991
        self.uml3_0_0_ReduceAction994 = uml3_0_0_ReduceAction994
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def uml3_0_0_ReduceAction991(self):
        return self.__uml3_0_0_ReduceAction991

    @uml3_0_0_ReduceAction991.setter
    def uml3_0_0_ReduceAction991(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReduceAction__uml3_0_0_ReduceAction991", None)
        self.__uml3_0_0_ReduceAction991 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_OutputPin992"):
                opp_val = getattr(old_value, "uml3_0_0_OutputPin992", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_OutputPin992", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_OutputPin992"):
                opp_val = getattr(value, "uml3_0_0_OutputPin992", None)
                setattr(value, "uml3_0_0_OutputPin992", self)

    @property
    def uml3_0_0_ReduceAction994(self):
        return self.__uml3_0_0_ReduceAction994

    @uml3_0_0_ReduceAction994.setter
    def uml3_0_0_ReduceAction994(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReduceAction__uml3_0_0_ReduceAction994", None)
        self.__uml3_0_0_ReduceAction994 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin995"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin995", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin995", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin995"):
                opp_val = getattr(value, "uml3_0_0_InputPin995", None)
                setattr(value, "uml3_0_0_InputPin995", self)

    @property
    def uml3_0_0_ReduceAction(self):
        return self.__uml3_0_0_ReduceAction

    @uml3_0_0_ReduceAction.setter
    def uml3_0_0_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReduceAction__uml3_0_0_ReduceAction", None)
        self.__uml3_0_0_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior989"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior989", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior989", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior989"):
                opp_val = getattr(value, "uml3_0_0_Behavior989", None)
                setattr(value, "uml3_0_0_Behavior989", self)

class uml3_0_0_ReadIsClassifiedObjectAction(Action):

    def __init__(self, isDirect: str, uml3_0_0_ReadIsClassifiedObjectAction: "uml3_0_0_Classifier" = None, uml3_0_0_ReadIsClassifiedObjectAction940: "uml3_0_0_OutputPin" = None, uml3_0_0_ReadIsClassifiedObjectAction943: "uml3_0_0_InputPin" = None):
        self.isDirect = isDirect
        self.uml3_0_0_ReadIsClassifiedObjectAction = uml3_0_0_ReadIsClassifiedObjectAction
        self.uml3_0_0_ReadIsClassifiedObjectAction940 = uml3_0_0_ReadIsClassifiedObjectAction940
        self.uml3_0_0_ReadIsClassifiedObjectAction943 = uml3_0_0_ReadIsClassifiedObjectAction943
        
    @property
    def isDirect(self) -> str:
        return self.__isDirect

    @isDirect.setter
    def isDirect(self, isDirect: str):
        self.__isDirect = isDirect

    @property
    def uml3_0_0_ReadIsClassifiedObjectAction940(self):
        return self.__uml3_0_0_ReadIsClassifiedObjectAction940

    @uml3_0_0_ReadIsClassifiedObjectAction940.setter
    def uml3_0_0_ReadIsClassifiedObjectAction940(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReadIsClassifiedObjectAction__uml3_0_0_ReadIsClassifiedObjectAction940", None)
        self.__uml3_0_0_ReadIsClassifiedObjectAction940 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_OutputPin941"):
                opp_val = getattr(old_value, "uml3_0_0_OutputPin941", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_OutputPin941", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_OutputPin941"):
                opp_val = getattr(value, "uml3_0_0_OutputPin941", None)
                setattr(value, "uml3_0_0_OutputPin941", self)

    @property
    def uml3_0_0_ReadIsClassifiedObjectAction943(self):
        return self.__uml3_0_0_ReadIsClassifiedObjectAction943

    @uml3_0_0_ReadIsClassifiedObjectAction943.setter
    def uml3_0_0_ReadIsClassifiedObjectAction943(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReadIsClassifiedObjectAction__uml3_0_0_ReadIsClassifiedObjectAction943", None)
        self.__uml3_0_0_ReadIsClassifiedObjectAction943 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin944"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin944", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin944", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin944"):
                opp_val = getattr(value, "uml3_0_0_InputPin944", None)
                setattr(value, "uml3_0_0_InputPin944", self)

    @property
    def uml3_0_0_ReadIsClassifiedObjectAction(self):
        return self.__uml3_0_0_ReadIsClassifiedObjectAction

    @uml3_0_0_ReadIsClassifiedObjectAction.setter
    def uml3_0_0_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ReadIsClassifiedObjectAction__uml3_0_0_ReadIsClassifiedObjectAction", None)
        self.__uml3_0_0_ReadIsClassifiedObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Classifier938"):
                opp_val = getattr(old_value, "uml3_0_0_Classifier938", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Classifier938", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Classifier938"):
                opp_val = getattr(value, "uml3_0_0_Classifier938", None)
                setattr(value, "uml3_0_0_Classifier938", self)

class uml3_0_0_AcceptEventAction(Action):

    def __init__(self, isUnmarshall: str, uml3_0_0_AcceptEventAction: set["uml3_0_0_OutputPin"] = None, uml3_0_0_AcceptEventAction968: set["uml3_0_0_Trigger"] = None):
        self.isUnmarshall = isUnmarshall
        self.uml3_0_0_AcceptEventAction = uml3_0_0_AcceptEventAction if uml3_0_0_AcceptEventAction is not None else set()
        self.uml3_0_0_AcceptEventAction968 = uml3_0_0_AcceptEventAction968 if uml3_0_0_AcceptEventAction968 is not None else set()
        
    @property
    def isUnmarshall(self) -> str:
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: str):
        self.__isUnmarshall = isUnmarshall

    @property
    def uml3_0_0_AcceptEventAction(self):
        return self.__uml3_0_0_AcceptEventAction

    @uml3_0_0_AcceptEventAction.setter
    def uml3_0_0_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_AcceptEventAction__uml3_0_0_AcceptEventAction", None)
        self.__uml3_0_0_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_OutputPin966"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin966", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_OutputPin966", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_OutputPin966"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin966", None)
                    
                    setattr(item, "uml3_0_0_OutputPin966", self)
                    

    @property
    def uml3_0_0_AcceptEventAction968(self):
        return self.__uml3_0_0_AcceptEventAction968

    @uml3_0_0_AcceptEventAction968.setter
    def uml3_0_0_AcceptEventAction968(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_AcceptEventAction__uml3_0_0_AcceptEventAction968", None)
        self.__uml3_0_0_AcceptEventAction968 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Trigger969"):
                    opp_val = getattr(item, "uml3_0_0_Trigger969", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Trigger969", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Trigger969"):
                    opp_val = getattr(item, "uml3_0_0_Trigger969", None)
                    
                    setattr(item, "uml3_0_0_Trigger969", self)
                    

class uml3_0_0_ReadLinkObjectEndAction(Action):

    pass
class uml3_0_0_ReplyAction(Action):

    pass
class uml3_0_0_ReadExtentAction(Action):

    pass
class uml3_0_0_DestroyObjectAction(Action):

    def __init__(self, isDestroyLinks: str, isDestroyOwnedObjects: str, uml3_0_0_DestroyObjectAction: "uml3_0_0_InputPin" = None):
        self.isDestroyLinks = isDestroyLinks
        self.isDestroyOwnedObjects = isDestroyOwnedObjects
        self.uml3_0_0_DestroyObjectAction = uml3_0_0_DestroyObjectAction
        
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
    def uml3_0_0_DestroyObjectAction(self):
        return self.__uml3_0_0_DestroyObjectAction

    @uml3_0_0_DestroyObjectAction.setter
    def uml3_0_0_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_DestroyObjectAction__uml3_0_0_DestroyObjectAction", None)
        self.__uml3_0_0_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InputPin799"):
                opp_val = getattr(old_value, "uml3_0_0_InputPin799", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InputPin799", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InputPin799"):
                opp_val = getattr(value, "uml3_0_0_InputPin799", None)
                setattr(value, "uml3_0_0_InputPin799", self)

class uml3_0_0_ReadSelfAction(Action):

    pass
class uml3_0_0_RaiseExceptionAction(Action):

    pass
class uml3_0_0_StartClassifierBehaviorAction(Action):

    pass
class uml3_0_0_VariableAction(Action):

    pass
class uml3_0_0_OpaqueAction(Action):

    def __init__(self, body: str, language: str, uml3_0_0_OpaqueAction: set["uml3_0_0_InputPin"] = None, uml3_0_0_OpaqueAction520: set["uml3_0_0_OutputPin"] = None):
        self.body = body
        self.language = language
        self.uml3_0_0_OpaqueAction = uml3_0_0_OpaqueAction if uml3_0_0_OpaqueAction is not None else set()
        self.uml3_0_0_OpaqueAction520 = uml3_0_0_OpaqueAction520 if uml3_0_0_OpaqueAction520 is not None else set()
        
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
    def uml3_0_0_OpaqueAction(self):
        return self.__uml3_0_0_OpaqueAction

    @uml3_0_0_OpaqueAction.setter
    def uml3_0_0_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_OpaqueAction__uml3_0_0_OpaqueAction", None)
        self.__uml3_0_0_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_InputPin"):
                    opp_val = getattr(item, "uml3_0_0_InputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_InputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_InputPin"):
                    opp_val = getattr(item, "uml3_0_0_InputPin", None)
                    
                    setattr(item, "uml3_0_0_InputPin", self)
                    

    @property
    def uml3_0_0_OpaqueAction520(self):
        return self.__uml3_0_0_OpaqueAction520

    @uml3_0_0_OpaqueAction520.setter
    def uml3_0_0_OpaqueAction520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_OpaqueAction__uml3_0_0_OpaqueAction520", None)
        self.__uml3_0_0_OpaqueAction520 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_OutputPin"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_OutputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_OutputPin"):
                    opp_val = getattr(item, "uml3_0_0_OutputPin", None)
                    
                    setattr(item, "uml3_0_0_OutputPin", self)
                    

class OpaqueBehavior:

    pass
class uml3_0_0_FunctionBehavior(OpaqueBehavior):

    pass
class LiteralSpecification:

    pass
class uml3_0_0_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class uml3_0_0_LiteralNull(LiteralSpecification):

    pass
class uml3_0_0_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class uml3_0_0_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class uml3_0_0_LiteralInteger(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Expression:

    pass
class InstanceSpecification:

    pass
class uml3_0_0_EnumerationLiteral(InstanceSpecification):

    pass
class DataType:

    pass
class uml3_0_0_PrimitiveType(DataType):

    pass
class uml3_0_0_Enumeration(DataType):

    pass
class TemplateSignature:

    pass
class TemplateParameter:

    pass
class uml3_0_0_ClassifierTemplateParameter(TemplateParameter):

    def __init__(self, allowSubstitutable: str, uml3_0_0_ClassifierTemplateParameter: set["uml3_0_0_Classifier"] = None):
        self.allowSubstitutable = allowSubstitutable
        self.uml3_0_0_ClassifierTemplateParameter = uml3_0_0_ClassifierTemplateParameter if uml3_0_0_ClassifierTemplateParameter is not None else set()
        
    @property
    def allowSubstitutable(self) -> str:
        return self.__allowSubstitutable

    @allowSubstitutable.setter
    def allowSubstitutable(self, allowSubstitutable: str):
        self.__allowSubstitutable = allowSubstitutable

    @property
    def uml3_0_0_ClassifierTemplateParameter(self):
        return self.__uml3_0_0_ClassifierTemplateParameter

    @uml3_0_0_ClassifierTemplateParameter.setter
    def uml3_0_0_ClassifierTemplateParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ClassifierTemplateParameter__uml3_0_0_ClassifierTemplateParameter", None)
        self.__uml3_0_0_ClassifierTemplateParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Classifier487"):
                    opp_val = getattr(item, "uml3_0_0_Classifier487", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Classifier487", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Classifier487"):
                    opp_val = getattr(item, "uml3_0_0_Classifier487", None)
                    
                    setattr(item, "uml3_0_0_Classifier487", self)
                    

class uml3_0_0_OperationTemplateParameter(TemplateParameter):

    pass
class uml3_0_0_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class Package:

    pass
class uml3_0_0_Model(Package):

    def __init__(self, viewpoint: str):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> str:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: str):
        self.__viewpoint = viewpoint

class uml3_0_0_Profile(Package):

    pass
class StructuredClassifier:

    pass
class uml3_0_0_EncapsulatedClassifier(StructuredClassifier):

    pass
class Association:

    pass
class uml3_0_0_CommunicationPath(Association):

    pass
class Vertex:

    pass
class uml3_0_0_ConnectionPointReference(Vertex):

    pass
class Property:

    pass
class uml3_0_0_ExtensionEnd(Property):

    pass
class uml3_0_0_Port(Property):

    def __init__(self, isBehavior: str, isService: str, uml3_0_0_Port: "uml3_0_0_Trigger" = None, uml3_0_0_Port353: set["uml3_0_0_Interface"] = None, uml3_0_0_Port357: "uml3_0_0_Port" = None, uml3_0_0_Port355: set["uml3_0_0_Port"] = None, uml3_0_0_Port359: set["uml3_0_0_Interface"] = None, uml3_0_0_Port362: "uml3_0_0_ProtocolStateMachine" = None, uml3_0_0_Port405: "uml3_0_0_EncapsulatedClassifier" = None, uml3_0_0_Port648: "uml3_0_0_InvocationAction" = None):
        self.isBehavior = isBehavior
        self.isService = isService
        self.uml3_0_0_Port = uml3_0_0_Port
        self.uml3_0_0_Port353 = uml3_0_0_Port353 if uml3_0_0_Port353 is not None else set()
        self.uml3_0_0_Port357 = uml3_0_0_Port357
        self.uml3_0_0_Port355 = uml3_0_0_Port355 if uml3_0_0_Port355 is not None else set()
        self.uml3_0_0_Port359 = uml3_0_0_Port359 if uml3_0_0_Port359 is not None else set()
        self.uml3_0_0_Port362 = uml3_0_0_Port362
        self.uml3_0_0_Port405 = uml3_0_0_Port405
        self.uml3_0_0_Port648 = uml3_0_0_Port648
        
    @property
    def isService(self) -> str:
        return self.__isService

    @isService.setter
    def isService(self, isService: str):
        self.__isService = isService

    @property
    def isBehavior(self) -> str:
        return self.__isBehavior

    @isBehavior.setter
    def isBehavior(self, isBehavior: str):
        self.__isBehavior = isBehavior

    @property
    def uml3_0_0_Port355(self):
        return self.__uml3_0_0_Port355

    @uml3_0_0_Port355.setter
    def uml3_0_0_Port355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port355", None)
        self.__uml3_0_0_Port355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Port357"):
                    opp_val = getattr(item, "uml3_0_0_Port357", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Port357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Port357"):
                    opp_val = getattr(item, "uml3_0_0_Port357", None)
                    
                    setattr(item, "uml3_0_0_Port357", self)
                    

    @property
    def uml3_0_0_Port405(self):
        return self.__uml3_0_0_Port405

    @uml3_0_0_Port405.setter
    def uml3_0_0_Port405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port405", None)
        self.__uml3_0_0_Port405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_EncapsulatedClassifier"):
                opp_val = getattr(old_value, "uml3_0_0_EncapsulatedClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_EncapsulatedClassifier"):
                opp_val = getattr(value, "uml3_0_0_EncapsulatedClassifier", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_EncapsulatedClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Port(self):
        return self.__uml3_0_0_Port

    @uml3_0_0_Port.setter
    def uml3_0_0_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port", None)
        self.__uml3_0_0_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Trigger351"):
                opp_val = getattr(old_value, "uml3_0_0_Trigger351", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Trigger351"):
                opp_val = getattr(value, "uml3_0_0_Trigger351", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Trigger351", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Port648(self):
        return self.__uml3_0_0_Port648

    @uml3_0_0_Port648.setter
    def uml3_0_0_Port648(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port648", None)
        self.__uml3_0_0_Port648 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InvocationAction647"):
                opp_val = getattr(old_value, "uml3_0_0_InvocationAction647", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_InvocationAction647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InvocationAction647"):
                opp_val = getattr(value, "uml3_0_0_InvocationAction647", None)
                setattr(value, "uml3_0_0_InvocationAction647", self)

    @property
    def uml3_0_0_Port357(self):
        return self.__uml3_0_0_Port357

    @uml3_0_0_Port357.setter
    def uml3_0_0_Port357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port357", None)
        self.__uml3_0_0_Port357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Port355"):
                opp_val = getattr(old_value, "uml3_0_0_Port355", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Port355"):
                opp_val = getattr(value, "uml3_0_0_Port355", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Port355", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Port353(self):
        return self.__uml3_0_0_Port353

    @uml3_0_0_Port353.setter
    def uml3_0_0_Port353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port353", None)
        self.__uml3_0_0_Port353 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Interface354"):
                    opp_val = getattr(item, "uml3_0_0_Interface354", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Interface354", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Interface354"):
                    opp_val = getattr(item, "uml3_0_0_Interface354", None)
                    
                    setattr(item, "uml3_0_0_Interface354", self)
                    

    @property
    def uml3_0_0_Port359(self):
        return self.__uml3_0_0_Port359

    @uml3_0_0_Port359.setter
    def uml3_0_0_Port359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port359", None)
        self.__uml3_0_0_Port359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Interface360"):
                    opp_val = getattr(item, "uml3_0_0_Interface360", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Interface360", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Interface360"):
                    opp_val = getattr(item, "uml3_0_0_Interface360", None)
                    
                    setattr(item, "uml3_0_0_Interface360", self)
                    

    @property
    def uml3_0_0_Port362(self):
        return self.__uml3_0_0_Port362

    @uml3_0_0_Port362.setter
    def uml3_0_0_Port362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Port__uml3_0_0_Port362", None)
        self.__uml3_0_0_Port362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ProtocolStateMachine363"):
                opp_val = getattr(old_value, "uml3_0_0_ProtocolStateMachine363", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ProtocolStateMachine363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ProtocolStateMachine363"):
                opp_val = getattr(value, "uml3_0_0_ProtocolStateMachine363", None)
                setattr(value, "uml3_0_0_ProtocolStateMachine363", self)

class Behavior:

    pass
class uml3_0_0_Activity(Behavior):

    def __init__(self, isReadOnly: str, isSingleExecution: str, Activity: "uml3_0_0_ActivityNode" = None, uml3_0_0_Activity: set["uml3_0_0_StructuredActivityNode"] = None, activityScope: set["uml3_0_0_Variable"] = None, activity: set["uml3_0_0_ActivityNode"] = None, activity573: set["uml3_0_0_ActivityEdge"] = None, uml3_0_0_Activity576: set["uml3_0_0_ActivityPartition"] = None, inActivity: set["uml3_0_0_ActivityGroup"] = None, Activity583: "uml3_0_0_Variable" = None, Activity561: "uml3_0_0_ActivityGroup" = None, Activity607: "uml3_0_0_ActivityEdge" = None):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.Activity = Activity
        self.uml3_0_0_Activity = uml3_0_0_Activity if uml3_0_0_Activity is not None else set()
        self.activityScope = activityScope if activityScope is not None else set()
        self.activity = activity if activity is not None else set()
        self.activity573 = activity573 if activity573 is not None else set()
        self.uml3_0_0_Activity576 = uml3_0_0_Activity576 if uml3_0_0_Activity576 is not None else set()
        self.inActivity = inActivity if inActivity is not None else set()
        self.Activity583 = Activity583
        self.Activity561 = Activity561
        self.Activity607 = Activity607
        
    @property
    def isSingleExecution(self) -> str:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: str):
        self.__isSingleExecution = isSingleExecution

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def Activity561(self):
        return self.__Activity561

    @Activity561.setter
    def Activity561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__Activity561", None)
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
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__activity", None)
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
    def Activity583(self):
        return self.__Activity583

    @Activity583.setter
    def Activity583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__Activity583", None)
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
    def uml3_0_0_Activity576(self):
        return self.__uml3_0_0_Activity576

    @uml3_0_0_Activity576.setter
    def uml3_0_0_Activity576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__uml3_0_0_Activity576", None)
        self.__uml3_0_0_Activity576 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ActivityPartition"):
                    opp_val = getattr(item, "uml3_0_0_ActivityPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ActivityPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ActivityPartition"):
                    opp_val = getattr(item, "uml3_0_0_ActivityPartition", None)
                    
                    setattr(item, "uml3_0_0_ActivityPartition", self)
                    

    @property
    def activityScope(self):
        return self.__activityScope

    @activityScope.setter
    def activityScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__activityScope", None)
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
    def uml3_0_0_Activity(self):
        return self.__uml3_0_0_Activity

    @uml3_0_0_Activity.setter
    def uml3_0_0_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__uml3_0_0_Activity", None)
        self.__uml3_0_0_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_StructuredActivityNode"):
                    opp_val = getattr(item, "uml3_0_0_StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_StructuredActivityNode"):
                    opp_val = getattr(item, "uml3_0_0_StructuredActivityNode", None)
                    
                    setattr(item, "uml3_0_0_StructuredActivityNode", self)
                    

    @property
    def Activity607(self):
        return self.__Activity607

    @Activity607.setter
    def Activity607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__Activity607", None)
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

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__Activity", None)
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
    def activity573(self):
        return self.__activity573

    @activity573.setter
    def activity573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__activity573", None)
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
    def inActivity(self):
        return self.__inActivity

    @inActivity.setter
    def inActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Activity__inActivity", None)
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
                    

class uml3_0_0_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
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

class uml3_0_0_Interaction(Behavior, InteractionFragment):

    pass
class uml3_0_0_StateMachine(Behavior):

    pass
class uml3_0_0_Pseudostate(Vertex):

    def __init__(self, kind: str, Pseudostate: "uml3_0_0_StateMachine" = None, Pseudostate369: "uml3_0_0_State" = None, uml3_0_0_Pseudostate: "uml3_0_0_ConnectionPointReference" = None, uml3_0_0_Pseudostate393: "uml3_0_0_ConnectionPointReference" = None, connectionPoint: "uml3_0_0_StateMachine" = None, connectionPoint399: "uml3_0_0_State" = None):
        self.kind = kind
        self.Pseudostate = Pseudostate
        self.Pseudostate369 = Pseudostate369
        self.uml3_0_0_Pseudostate = uml3_0_0_Pseudostate
        self.uml3_0_0_Pseudostate393 = uml3_0_0_Pseudostate393
        self.connectionPoint = connectionPoint
        self.connectionPoint399 = connectionPoint399
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Pseudostate369(self):
        return self.__Pseudostate369

    @Pseudostate369.setter
    def Pseudostate369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Pseudostate__Pseudostate369", None)
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
    def uml3_0_0_Pseudostate(self):
        return self.__uml3_0_0_Pseudostate

    @uml3_0_0_Pseudostate.setter
    def uml3_0_0_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Pseudostate__uml3_0_0_Pseudostate", None)
        self.__uml3_0_0_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ConnectionPointReference"):
                opp_val = getattr(old_value, "uml3_0_0_ConnectionPointReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ConnectionPointReference"):
                opp_val = getattr(value, "uml3_0_0_ConnectionPointReference", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ConnectionPointReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connectionPoint(self):
        return self.__connectionPoint

    @connectionPoint.setter
    def connectionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Pseudostate__connectionPoint", None)
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
    def connectionPoint399(self):
        return self.__connectionPoint399

    @connectionPoint399.setter
    def connectionPoint399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Pseudostate__connectionPoint399", None)
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

    @property
    def uml3_0_0_Pseudostate393(self):
        return self.__uml3_0_0_Pseudostate393

    @uml3_0_0_Pseudostate393.setter
    def uml3_0_0_Pseudostate393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Pseudostate__uml3_0_0_Pseudostate393", None)
        self.__uml3_0_0_Pseudostate393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ConnectionPointReference392"):
                opp_val = getattr(old_value, "uml3_0_0_ConnectionPointReference392", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ConnectionPointReference392"):
                opp_val = getattr(value, "uml3_0_0_ConnectionPointReference392", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ConnectionPointReference392", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Pseudostate(self):
        return self.__Pseudostate

    @Pseudostate.setter
    def Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Pseudostate__Pseudostate", None)
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

class StateMachine:

    pass
class uml3_0_0_ProtocolStateMachine(StateMachine):

    pass
class uml3_0_0_Extension(Association):

    def __init__(self, isRequired: str, Extension: "uml3_0_0_Class" = None, extension: "uml3_0_0_Class" = None):
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
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Extension__extension", None)
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

    @property
    def Extension(self):
        return self.__Extension

    @Extension.setter
    def Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Extension__Extension", None)
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

class BehavioredClassifier:

    pass
class uml3_0_0_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class uml3_0_0_Actor(BehavioredClassifier):

    pass
class EncapsulatedClassifier:

    pass
class Class:

    pass
class uml3_0_0_Stereotype(Class):

    pass
class uml3_0_0_AssociationClass(Association, Class):

    pass
class uml3_0_0_Component(Class):

    def __init__(self, isIndirectlyInstantiated: str, Component: "uml3_0_0_ComponentRealization" = None, uml3_0_0_Component: set["uml3_0_0_Interface"] = None, uml3_0_0_Component778: set["uml3_0_0_Interface"] = None, uml3_0_0_Component781: set["uml3_0_0_PackageableElement"] = None, abstraction: set["uml3_0_0_ComponentRealization"] = None):
        self.isIndirectlyInstantiated = isIndirectlyInstantiated
        self.Component = Component
        self.uml3_0_0_Component = uml3_0_0_Component if uml3_0_0_Component is not None else set()
        self.uml3_0_0_Component778 = uml3_0_0_Component778 if uml3_0_0_Component778 is not None else set()
        self.uml3_0_0_Component781 = uml3_0_0_Component781 if uml3_0_0_Component781 is not None else set()
        self.abstraction = abstraction if abstraction is not None else set()
        
    @property
    def isIndirectlyInstantiated(self) -> str:
        return self.__isIndirectlyInstantiated

    @isIndirectlyInstantiated.setter
    def isIndirectlyInstantiated(self, isIndirectlyInstantiated: str):
        self.__isIndirectlyInstantiated = isIndirectlyInstantiated

    @property
    def uml3_0_0_Component(self):
        return self.__uml3_0_0_Component

    @uml3_0_0_Component.setter
    def uml3_0_0_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Component__uml3_0_0_Component", None)
        self.__uml3_0_0_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Interface776"):
                    opp_val = getattr(item, "uml3_0_0_Interface776", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Interface776", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Interface776"):
                    opp_val = getattr(item, "uml3_0_0_Interface776", None)
                    
                    setattr(item, "uml3_0_0_Interface776", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Component__Component", None)
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

    @property
    def abstraction(self):
        return self.__abstraction

    @abstraction.setter
    def abstraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Component__abstraction", None)
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
    def uml3_0_0_Component781(self):
        return self.__uml3_0_0_Component781

    @uml3_0_0_Component781.setter
    def uml3_0_0_Component781(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Component__uml3_0_0_Component781", None)
        self.__uml3_0_0_Component781 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_PackageableElement782"):
                    opp_val = getattr(item, "uml3_0_0_PackageableElement782", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_PackageableElement782", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_PackageableElement782"):
                    opp_val = getattr(item, "uml3_0_0_PackageableElement782", None)
                    
                    setattr(item, "uml3_0_0_PackageableElement782", self)
                    

    @property
    def uml3_0_0_Component778(self):
        return self.__uml3_0_0_Component778

    @uml3_0_0_Component778.setter
    def uml3_0_0_Component778(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Component__uml3_0_0_Component778", None)
        self.__uml3_0_0_Component778 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Interface779"):
                    opp_val = getattr(item, "uml3_0_0_Interface779", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Interface779", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Interface779"):
                    opp_val = getattr(item, "uml3_0_0_Interface779", None)
                    
                    setattr(item, "uml3_0_0_Interface779", self)
                    

class Feature:

    pass
class uml3_0_0_Connector(Feature):

    def __init__(self, kind: str, uml3_0_0_Connector: "uml3_0_0_StructuredClassifier" = None, uml3_0_0_Connector417: "uml3_0_0_Association" = None, uml3_0_0_Connector421: "uml3_0_0_Connector" = None, uml3_0_0_Connector419: set["uml3_0_0_Connector"] = None, uml3_0_0_Connector423: set["uml3_0_0_ConnectorEnd"] = None, uml3_0_0_Connector426: set["uml3_0_0_Behavior"] = None, uml3_0_0_Connector673: "uml3_0_0_Message" = None, uml3_0_0_Connector920: "uml3_0_0_InformationFlow" = None):
        self.kind = kind
        self.uml3_0_0_Connector = uml3_0_0_Connector
        self.uml3_0_0_Connector417 = uml3_0_0_Connector417
        self.uml3_0_0_Connector421 = uml3_0_0_Connector421
        self.uml3_0_0_Connector419 = uml3_0_0_Connector419 if uml3_0_0_Connector419 is not None else set()
        self.uml3_0_0_Connector423 = uml3_0_0_Connector423 if uml3_0_0_Connector423 is not None else set()
        self.uml3_0_0_Connector426 = uml3_0_0_Connector426 if uml3_0_0_Connector426 is not None else set()
        self.uml3_0_0_Connector673 = uml3_0_0_Connector673
        self.uml3_0_0_Connector920 = uml3_0_0_Connector920
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def uml3_0_0_Connector417(self):
        return self.__uml3_0_0_Connector417

    @uml3_0_0_Connector417.setter
    def uml3_0_0_Connector417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector417", None)
        self.__uml3_0_0_Connector417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Association418"):
                opp_val = getattr(old_value, "uml3_0_0_Association418", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Association418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Association418"):
                opp_val = getattr(value, "uml3_0_0_Association418", None)
                setattr(value, "uml3_0_0_Association418", self)

    @property
    def uml3_0_0_Connector673(self):
        return self.__uml3_0_0_Connector673

    @uml3_0_0_Connector673.setter
    def uml3_0_0_Connector673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector673", None)
        self.__uml3_0_0_Connector673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Message672"):
                opp_val = getattr(old_value, "uml3_0_0_Message672", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Message672", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Message672"):
                opp_val = getattr(value, "uml3_0_0_Message672", None)
                setattr(value, "uml3_0_0_Message672", self)

    @property
    def uml3_0_0_Connector(self):
        return self.__uml3_0_0_Connector

    @uml3_0_0_Connector.setter
    def uml3_0_0_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector", None)
        self.__uml3_0_0_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_StructuredClassifier415"):
                opp_val = getattr(old_value, "uml3_0_0_StructuredClassifier415", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_StructuredClassifier415"):
                opp_val = getattr(value, "uml3_0_0_StructuredClassifier415", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_StructuredClassifier415", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Connector920(self):
        return self.__uml3_0_0_Connector920

    @uml3_0_0_Connector920.setter
    def uml3_0_0_Connector920(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector920", None)
        self.__uml3_0_0_Connector920 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InformationFlow919"):
                opp_val = getattr(old_value, "uml3_0_0_InformationFlow919", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InformationFlow919"):
                opp_val = getattr(value, "uml3_0_0_InformationFlow919", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_InformationFlow919", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Connector423(self):
        return self.__uml3_0_0_Connector423

    @uml3_0_0_Connector423.setter
    def uml3_0_0_Connector423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector423", None)
        self.__uml3_0_0_Connector423 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ConnectorEnd424"):
                    opp_val = getattr(item, "uml3_0_0_ConnectorEnd424", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ConnectorEnd424", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ConnectorEnd424"):
                    opp_val = getattr(item, "uml3_0_0_ConnectorEnd424", None)
                    
                    setattr(item, "uml3_0_0_ConnectorEnd424", self)
                    

    @property
    def uml3_0_0_Connector421(self):
        return self.__uml3_0_0_Connector421

    @uml3_0_0_Connector421.setter
    def uml3_0_0_Connector421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector421", None)
        self.__uml3_0_0_Connector421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Connector419"):
                opp_val = getattr(old_value, "uml3_0_0_Connector419", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Connector419"):
                opp_val = getattr(value, "uml3_0_0_Connector419", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Connector419", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Connector426(self):
        return self.__uml3_0_0_Connector426

    @uml3_0_0_Connector426.setter
    def uml3_0_0_Connector426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector426", None)
        self.__uml3_0_0_Connector426 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Behavior427"):
                    opp_val = getattr(item, "uml3_0_0_Behavior427", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Behavior427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Behavior427"):
                    opp_val = getattr(item, "uml3_0_0_Behavior427", None)
                    
                    setattr(item, "uml3_0_0_Behavior427", self)
                    

    @property
    def uml3_0_0_Connector419(self):
        return self.__uml3_0_0_Connector419

    @uml3_0_0_Connector419.setter
    def uml3_0_0_Connector419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Connector__uml3_0_0_Connector419", None)
        self.__uml3_0_0_Connector419 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Connector421"):
                    opp_val = getattr(item, "uml3_0_0_Connector421", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Connector421", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Connector421"):
                    opp_val = getattr(item, "uml3_0_0_Connector421", None)
                    
                    setattr(item, "uml3_0_0_Connector421", self)
                    

class BehavioralFeature:

    pass
class uml3_0_0_Reception(BehavioralFeature):

    pass
class DeployedArtifact:

    pass
class Artifact:

    pass
class uml3_0_0_DeploymentSpecification(Artifact):

    def __init__(self, deploymentLocation: str, executionLocation: str, DeploymentSpecification: "uml3_0_0_Deployment" = None, configuration: "uml3_0_0_Deployment" = None):
        self.deploymentLocation = deploymentLocation
        self.executionLocation = executionLocation
        self.DeploymentSpecification = DeploymentSpecification
        self.configuration = configuration
        
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
    def DeploymentSpecification(self):
        return self.__DeploymentSpecification

    @DeploymentSpecification.setter
    def DeploymentSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_DeploymentSpecification__DeploymentSpecification", None)
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

    @property
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_DeploymentSpecification__configuration", None)
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

class uml3_0_0_Class(BehavioredClassifier, EncapsulatedClassifier):

    def __init__(self, isActive: str, uml3_0_0_Class: "uml3_0_0_Property" = None, Class: "uml3_0_0_Operation" = None, uml3_0_0_Class265: set["uml3_0_0_Classifier"] = None, class: set["uml3_0_0_Operation"] = None, uml3_0_0_Class270: "uml3_0_0_Class" = None, uml3_0_0_Class268: set["uml3_0_0_Class"] = None, uml3_0_0_Class272: set["uml3_0_0_Reception"] = None, metaclass: set["uml3_0_0_Extension"] = None, Class429: "uml3_0_0_Extension" = None):
        self.isActive = isActive
        self.uml3_0_0_Class = uml3_0_0_Class
        self.Class = Class
        self.uml3_0_0_Class265 = uml3_0_0_Class265 if uml3_0_0_Class265 is not None else set()
        self.class = class if class is not None else set()
        self.uml3_0_0_Class270 = uml3_0_0_Class270
        self.uml3_0_0_Class268 = uml3_0_0_Class268 if uml3_0_0_Class268 is not None else set()
        self.uml3_0_0_Class272 = uml3_0_0_Class272 if uml3_0_0_Class272 is not None else set()
        self.metaclass = metaclass if metaclass is not None else set()
        self.Class429 = Class429
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def uml3_0_0_Class265(self):
        return self.__uml3_0_0_Class265

    @uml3_0_0_Class265.setter
    def uml3_0_0_Class265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__uml3_0_0_Class265", None)
        self.__uml3_0_0_Class265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Classifier266"):
                    opp_val = getattr(item, "uml3_0_0_Classifier266", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Classifier266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Classifier266"):
                    opp_val = getattr(item, "uml3_0_0_Classifier266", None)
                    
                    setattr(item, "uml3_0_0_Classifier266", self)
                    

    @property
    def metaclass(self):
        return self.__metaclass

    @metaclass.setter
    def metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__metaclass", None)
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
    def Class429(self):
        return self.__Class429

    @Class429.setter
    def Class429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__Class429", None)
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

    @property
    def uml3_0_0_Class268(self):
        return self.__uml3_0_0_Class268

    @uml3_0_0_Class268.setter
    def uml3_0_0_Class268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__uml3_0_0_Class268", None)
        self.__uml3_0_0_Class268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Class270"):
                    opp_val = getattr(item, "uml3_0_0_Class270", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Class270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Class270"):
                    opp_val = getattr(item, "uml3_0_0_Class270", None)
                    
                    setattr(item, "uml3_0_0_Class270", self)
                    

    @property
    def uml3_0_0_Class272(self):
        return self.__uml3_0_0_Class272

    @uml3_0_0_Class272.setter
    def uml3_0_0_Class272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__uml3_0_0_Class272", None)
        self.__uml3_0_0_Class272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Reception"):
                    opp_val = getattr(item, "uml3_0_0_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Reception"):
                    opp_val = getattr(item, "uml3_0_0_Reception", None)
                    
                    setattr(item, "uml3_0_0_Reception", self)
                    

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__class", None)
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
    def uml3_0_0_Class(self):
        return self.__uml3_0_0_Class

    @uml3_0_0_Class.setter
    def uml3_0_0_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__uml3_0_0_Class", None)
        self.__uml3_0_0_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Property172"):
                opp_val = getattr(old_value, "uml3_0_0_Property172", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Property172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Property172"):
                opp_val = getattr(value, "uml3_0_0_Property172", None)
                setattr(value, "uml3_0_0_Property172", self)

    @property
    def uml3_0_0_Class270(self):
        return self.__uml3_0_0_Class270

    @uml3_0_0_Class270.setter
    def uml3_0_0_Class270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__uml3_0_0_Class270", None)
        self.__uml3_0_0_Class270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Class268"):
                opp_val = getattr(old_value, "uml3_0_0_Class268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Class268"):
                opp_val = getattr(value, "uml3_0_0_Class268", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Class268", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Class__Class", None)
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

class DeploymentTarget:

    pass
class uml3_0_0_Node(DeploymentTarget, Class):

    pass
class StructuralFeature:

    pass
class uml3_0_0_Behavior(Class):

    def __init__(self, isReentrant: str, uml3_0_0_Behavior: "uml3_0_0_OpaqueExpression" = None, Behavior: "uml3_0_0_BehavioralFeature" = None, uml3_0_0_Behavior248: "uml3_0_0_Behavior" = None, uml3_0_0_Behavior246: set["uml3_0_0_Behavior"] = None, uml3_0_0_Behavior250: set["uml3_0_0_Parameter"] = None, uml3_0_0_Behavior253: "uml3_0_0_BehavioredClassifier" = None, uml3_0_0_Behavior255: set["uml3_0_0_Constraint"] = None, uml3_0_0_Behavior258: set["uml3_0_0_Constraint"] = None, uml3_0_0_Behavior261: set["uml3_0_0_ParameterSet"] = None, method: "uml3_0_0_BehavioralFeature" = None, uml3_0_0_Behavior276: "uml3_0_0_BehavioredClassifier" = None, uml3_0_0_Behavior279: "uml3_0_0_BehavioredClassifier" = None, uml3_0_0_Behavior344: "uml3_0_0_Transition" = None, uml3_0_0_Behavior377: "uml3_0_0_State" = None, uml3_0_0_Behavior380: "uml3_0_0_State" = None, uml3_0_0_Behavior383: "uml3_0_0_State" = None, uml3_0_0_Behavior427: "uml3_0_0_Connector" = None, uml3_0_0_Behavior660: "uml3_0_0_CallBehaviorAction" = None, uml3_0_0_Behavior641: "uml3_0_0_ObjectNode" = None, uml3_0_0_Behavior745: "uml3_0_0_BehaviorExecutionSpecification" = None, uml3_0_0_Behavior763: "uml3_0_0_DecisionNode" = None, uml3_0_0_Behavior768: "uml3_0_0_ObjectFlow" = None, uml3_0_0_Behavior771: "uml3_0_0_ObjectFlow" = None, uml3_0_0_Behavior989: "uml3_0_0_ReduceAction" = None):
        self.isReentrant = isReentrant
        self.uml3_0_0_Behavior = uml3_0_0_Behavior
        self.Behavior = Behavior
        self.uml3_0_0_Behavior248 = uml3_0_0_Behavior248
        self.uml3_0_0_Behavior246 = uml3_0_0_Behavior246 if uml3_0_0_Behavior246 is not None else set()
        self.uml3_0_0_Behavior250 = uml3_0_0_Behavior250 if uml3_0_0_Behavior250 is not None else set()
        self.uml3_0_0_Behavior253 = uml3_0_0_Behavior253
        self.uml3_0_0_Behavior255 = uml3_0_0_Behavior255 if uml3_0_0_Behavior255 is not None else set()
        self.uml3_0_0_Behavior258 = uml3_0_0_Behavior258 if uml3_0_0_Behavior258 is not None else set()
        self.uml3_0_0_Behavior261 = uml3_0_0_Behavior261 if uml3_0_0_Behavior261 is not None else set()
        self.method = method
        self.uml3_0_0_Behavior276 = uml3_0_0_Behavior276
        self.uml3_0_0_Behavior279 = uml3_0_0_Behavior279
        self.uml3_0_0_Behavior344 = uml3_0_0_Behavior344
        self.uml3_0_0_Behavior377 = uml3_0_0_Behavior377
        self.uml3_0_0_Behavior380 = uml3_0_0_Behavior380
        self.uml3_0_0_Behavior383 = uml3_0_0_Behavior383
        self.uml3_0_0_Behavior427 = uml3_0_0_Behavior427
        self.uml3_0_0_Behavior660 = uml3_0_0_Behavior660
        self.uml3_0_0_Behavior641 = uml3_0_0_Behavior641
        self.uml3_0_0_Behavior745 = uml3_0_0_Behavior745
        self.uml3_0_0_Behavior763 = uml3_0_0_Behavior763
        self.uml3_0_0_Behavior768 = uml3_0_0_Behavior768
        self.uml3_0_0_Behavior771 = uml3_0_0_Behavior771
        self.uml3_0_0_Behavior989 = uml3_0_0_Behavior989
        
    @property
    def isReentrant(self) -> str:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: str):
        self.__isReentrant = isReentrant

    @property
    def uml3_0_0_Behavior279(self):
        return self.__uml3_0_0_Behavior279

    @uml3_0_0_Behavior279.setter
    def uml3_0_0_Behavior279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior279", None)
        self.__uml3_0_0_Behavior279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_BehavioredClassifier278"):
                opp_val = getattr(old_value, "uml3_0_0_BehavioredClassifier278", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_BehavioredClassifier278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_BehavioredClassifier278"):
                opp_val = getattr(value, "uml3_0_0_BehavioredClassifier278", None)
                setattr(value, "uml3_0_0_BehavioredClassifier278", self)

    @property
    def uml3_0_0_Behavior377(self):
        return self.__uml3_0_0_Behavior377

    @uml3_0_0_Behavior377.setter
    def uml3_0_0_Behavior377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior377", None)
        self.__uml3_0_0_Behavior377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_State376"):
                opp_val = getattr(old_value, "uml3_0_0_State376", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_State376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_State376"):
                opp_val = getattr(value, "uml3_0_0_State376", None)
                setattr(value, "uml3_0_0_State376", self)

    @property
    def uml3_0_0_Behavior383(self):
        return self.__uml3_0_0_Behavior383

    @uml3_0_0_Behavior383.setter
    def uml3_0_0_Behavior383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior383", None)
        self.__uml3_0_0_Behavior383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_State382"):
                opp_val = getattr(old_value, "uml3_0_0_State382", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_State382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_State382"):
                opp_val = getattr(value, "uml3_0_0_State382", None)
                setattr(value, "uml3_0_0_State382", self)

    @property
    def uml3_0_0_Behavior660(self):
        return self.__uml3_0_0_Behavior660

    @uml3_0_0_Behavior660.setter
    def uml3_0_0_Behavior660(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior660", None)
        self.__uml3_0_0_Behavior660 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_CallBehaviorAction"):
                opp_val = getattr(old_value, "uml3_0_0_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_CallBehaviorAction"):
                opp_val = getattr(value, "uml3_0_0_CallBehaviorAction", None)
                setattr(value, "uml3_0_0_CallBehaviorAction", self)

    @property
    def uml3_0_0_Behavior246(self):
        return self.__uml3_0_0_Behavior246

    @uml3_0_0_Behavior246.setter
    def uml3_0_0_Behavior246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior246", None)
        self.__uml3_0_0_Behavior246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Behavior248"):
                    opp_val = getattr(item, "uml3_0_0_Behavior248", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Behavior248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Behavior248"):
                    opp_val = getattr(item, "uml3_0_0_Behavior248", None)
                    
                    setattr(item, "uml3_0_0_Behavior248", self)
                    

    @property
    def uml3_0_0_Behavior763(self):
        return self.__uml3_0_0_Behavior763

    @uml3_0_0_Behavior763.setter
    def uml3_0_0_Behavior763(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior763", None)
        self.__uml3_0_0_Behavior763 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_DecisionNode"):
                opp_val = getattr(old_value, "uml3_0_0_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_DecisionNode"):
                opp_val = getattr(value, "uml3_0_0_DecisionNode", None)
                setattr(value, "uml3_0_0_DecisionNode", self)

    @property
    def uml3_0_0_Behavior771(self):
        return self.__uml3_0_0_Behavior771

    @uml3_0_0_Behavior771.setter
    def uml3_0_0_Behavior771(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior771", None)
        self.__uml3_0_0_Behavior771 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ObjectFlow770"):
                opp_val = getattr(old_value, "uml3_0_0_ObjectFlow770", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ObjectFlow770", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ObjectFlow770"):
                opp_val = getattr(value, "uml3_0_0_ObjectFlow770", None)
                setattr(value, "uml3_0_0_ObjectFlow770", self)

    @property
    def uml3_0_0_Behavior641(self):
        return self.__uml3_0_0_Behavior641

    @uml3_0_0_Behavior641.setter
    def uml3_0_0_Behavior641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior641", None)
        self.__uml3_0_0_Behavior641 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ObjectNode640"):
                opp_val = getattr(old_value, "uml3_0_0_ObjectNode640", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ObjectNode640", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ObjectNode640"):
                opp_val = getattr(value, "uml3_0_0_ObjectNode640", None)
                setattr(value, "uml3_0_0_ObjectNode640", self)

    @property
    def uml3_0_0_Behavior989(self):
        return self.__uml3_0_0_Behavior989

    @uml3_0_0_Behavior989.setter
    def uml3_0_0_Behavior989(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior989", None)
        self.__uml3_0_0_Behavior989 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReduceAction"):
                opp_val = getattr(old_value, "uml3_0_0_ReduceAction", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ReduceAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReduceAction"):
                opp_val = getattr(value, "uml3_0_0_ReduceAction", None)
                setattr(value, "uml3_0_0_ReduceAction", self)

    @property
    def uml3_0_0_Behavior380(self):
        return self.__uml3_0_0_Behavior380

    @uml3_0_0_Behavior380.setter
    def uml3_0_0_Behavior380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior380", None)
        self.__uml3_0_0_Behavior380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_State379"):
                opp_val = getattr(old_value, "uml3_0_0_State379", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_State379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_State379"):
                opp_val = getattr(value, "uml3_0_0_State379", None)
                setattr(value, "uml3_0_0_State379", self)

    @property
    def uml3_0_0_Behavior261(self):
        return self.__uml3_0_0_Behavior261

    @uml3_0_0_Behavior261.setter
    def uml3_0_0_Behavior261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior261", None)
        self.__uml3_0_0_Behavior261 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ParameterSet262"):
                    opp_val = getattr(item, "uml3_0_0_ParameterSet262", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ParameterSet262", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ParameterSet262"):
                    opp_val = getattr(item, "uml3_0_0_ParameterSet262", None)
                    
                    setattr(item, "uml3_0_0_ParameterSet262", self)
                    

    @property
    def uml3_0_0_Behavior(self):
        return self.__uml3_0_0_Behavior

    @uml3_0_0_Behavior.setter
    def uml3_0_0_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior", None)
        self.__uml3_0_0_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_OpaqueExpression149"):
                opp_val = getattr(old_value, "uml3_0_0_OpaqueExpression149", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_OpaqueExpression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_OpaqueExpression149"):
                opp_val = getattr(value, "uml3_0_0_OpaqueExpression149", None)
                setattr(value, "uml3_0_0_OpaqueExpression149", self)

    @property
    def uml3_0_0_Behavior255(self):
        return self.__uml3_0_0_Behavior255

    @uml3_0_0_Behavior255.setter
    def uml3_0_0_Behavior255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior255", None)
        self.__uml3_0_0_Behavior255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Constraint256"):
                    opp_val = getattr(item, "uml3_0_0_Constraint256", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Constraint256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Constraint256"):
                    opp_val = getattr(item, "uml3_0_0_Constraint256", None)
                    
                    setattr(item, "uml3_0_0_Constraint256", self)
                    

    @property
    def uml3_0_0_Behavior344(self):
        return self.__uml3_0_0_Behavior344

    @uml3_0_0_Behavior344.setter
    def uml3_0_0_Behavior344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior344", None)
        self.__uml3_0_0_Behavior344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Transition343"):
                opp_val = getattr(old_value, "uml3_0_0_Transition343", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Transition343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Transition343"):
                opp_val = getattr(value, "uml3_0_0_Transition343", None)
                setattr(value, "uml3_0_0_Transition343", self)

    @property
    def uml3_0_0_Behavior768(self):
        return self.__uml3_0_0_Behavior768

    @uml3_0_0_Behavior768.setter
    def uml3_0_0_Behavior768(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior768", None)
        self.__uml3_0_0_Behavior768 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ObjectFlow767"):
                opp_val = getattr(old_value, "uml3_0_0_ObjectFlow767", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ObjectFlow767", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ObjectFlow767"):
                opp_val = getattr(value, "uml3_0_0_ObjectFlow767", None)
                setattr(value, "uml3_0_0_ObjectFlow767", self)

    @property
    def uml3_0_0_Behavior248(self):
        return self.__uml3_0_0_Behavior248

    @uml3_0_0_Behavior248.setter
    def uml3_0_0_Behavior248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior248", None)
        self.__uml3_0_0_Behavior248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior246"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior246"):
                opp_val = getattr(value, "uml3_0_0_Behavior246", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Behavior246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Behavior258(self):
        return self.__uml3_0_0_Behavior258

    @uml3_0_0_Behavior258.setter
    def uml3_0_0_Behavior258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior258", None)
        self.__uml3_0_0_Behavior258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Constraint259"):
                    opp_val = getattr(item, "uml3_0_0_Constraint259", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Constraint259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Constraint259"):
                    opp_val = getattr(item, "uml3_0_0_Constraint259", None)
                    
                    setattr(item, "uml3_0_0_Constraint259", self)
                    

    @property
    def uml3_0_0_Behavior276(self):
        return self.__uml3_0_0_Behavior276

    @uml3_0_0_Behavior276.setter
    def uml3_0_0_Behavior276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior276", None)
        self.__uml3_0_0_Behavior276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_BehavioredClassifier275"):
                opp_val = getattr(old_value, "uml3_0_0_BehavioredClassifier275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_BehavioredClassifier275"):
                opp_val = getattr(value, "uml3_0_0_BehavioredClassifier275", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_BehavioredClassifier275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Behavior253(self):
        return self.__uml3_0_0_Behavior253

    @uml3_0_0_Behavior253.setter
    def uml3_0_0_Behavior253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior253", None)
        self.__uml3_0_0_Behavior253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_BehavioredClassifier"):
                opp_val = getattr(old_value, "uml3_0_0_BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_BehavioredClassifier"):
                opp_val = getattr(value, "uml3_0_0_BehavioredClassifier", None)
                setattr(value, "uml3_0_0_BehavioredClassifier", self)

    @property
    def uml3_0_0_Behavior250(self):
        return self.__uml3_0_0_Behavior250

    @uml3_0_0_Behavior250.setter
    def uml3_0_0_Behavior250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior250", None)
        self.__uml3_0_0_Behavior250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Parameter251"):
                    opp_val = getattr(item, "uml3_0_0_Parameter251", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Parameter251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Parameter251"):
                    opp_val = getattr(item, "uml3_0_0_Parameter251", None)
                    
                    setattr(item, "uml3_0_0_Parameter251", self)
                    

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__method", None)
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
    def uml3_0_0_Behavior745(self):
        return self.__uml3_0_0_Behavior745

    @uml3_0_0_Behavior745.setter
    def uml3_0_0_Behavior745(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior745", None)
        self.__uml3_0_0_Behavior745 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_BehaviorExecutionSpecification"):
                opp_val = getattr(old_value, "uml3_0_0_BehaviorExecutionSpecification", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_BehaviorExecutionSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_BehaviorExecutionSpecification"):
                opp_val = getattr(value, "uml3_0_0_BehaviorExecutionSpecification", None)
                setattr(value, "uml3_0_0_BehaviorExecutionSpecification", self)

    @property
    def uml3_0_0_Behavior427(self):
        return self.__uml3_0_0_Behavior427

    @uml3_0_0_Behavior427.setter
    def uml3_0_0_Behavior427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__uml3_0_0_Behavior427", None)
        self.__uml3_0_0_Behavior427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Connector426"):
                opp_val = getattr(old_value, "uml3_0_0_Connector426", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Connector426"):
                opp_val = getattr(value, "uml3_0_0_Connector426", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Connector426", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Behavior(self):
        return self.__Behavior

    @Behavior.setter
    def Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Behavior__Behavior", None)
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

class ValueSpecification:

    pass
class uml3_0_0_Expression(ValueSpecification):

    def __init__(self, symbol: str, uml3_0_0_Expression: set["uml3_0_0_ValueSpecification"] = None):
        self.symbol = symbol
        self.uml3_0_0_Expression = uml3_0_0_Expression if uml3_0_0_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def uml3_0_0_Expression(self):
        return self.__uml3_0_0_Expression

    @uml3_0_0_Expression.setter
    def uml3_0_0_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Expression__uml3_0_0_Expression", None)
        self.__uml3_0_0_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ValueSpecification494"):
                    opp_val = getattr(item, "uml3_0_0_ValueSpecification494", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ValueSpecification494", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ValueSpecification494"):
                    opp_val = getattr(item, "uml3_0_0_ValueSpecification494", None)
                    
                    setattr(item, "uml3_0_0_ValueSpecification494", self)
                    

class uml3_0_0_Duration(ValueSpecification):

    pass
class uml3_0_0_LiteralSpecification(ValueSpecification):

    pass
class uml3_0_0_Interval(ValueSpecification):

    pass
class uml3_0_0_TimeExpression(ValueSpecification):

    pass
class uml3_0_0_InstanceValue(ValueSpecification):

    pass
class uml3_0_0_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, uml3_0_0_OpaqueExpression: "uml3_0_0_Abstraction" = None, uml3_0_0_OpaqueExpression147: "uml3_0_0_Parameter" = None, uml3_0_0_OpaqueExpression149: "uml3_0_0_Behavior" = None):
        self.body = body
        self.language = language
        self.uml3_0_0_OpaqueExpression = uml3_0_0_OpaqueExpression
        self.uml3_0_0_OpaqueExpression147 = uml3_0_0_OpaqueExpression147
        self.uml3_0_0_OpaqueExpression149 = uml3_0_0_OpaqueExpression149
        
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
    def uml3_0_0_OpaqueExpression(self):
        return self.__uml3_0_0_OpaqueExpression

    @uml3_0_0_OpaqueExpression.setter
    def uml3_0_0_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_OpaqueExpression__uml3_0_0_OpaqueExpression", None)
        self.__uml3_0_0_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Abstraction"):
                opp_val = getattr(old_value, "uml3_0_0_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Abstraction"):
                opp_val = getattr(value, "uml3_0_0_Abstraction", None)
                setattr(value, "uml3_0_0_Abstraction", self)

    @property
    def uml3_0_0_OpaqueExpression149(self):
        return self.__uml3_0_0_OpaqueExpression149

    @uml3_0_0_OpaqueExpression149.setter
    def uml3_0_0_OpaqueExpression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_OpaqueExpression__uml3_0_0_OpaqueExpression149", None)
        self.__uml3_0_0_OpaqueExpression149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior"):
                opp_val = getattr(value, "uml3_0_0_Behavior", None)
                setattr(value, "uml3_0_0_Behavior", self)

    @property
    def uml3_0_0_OpaqueExpression147(self):
        return self.__uml3_0_0_OpaqueExpression147

    @uml3_0_0_OpaqueExpression147.setter
    def uml3_0_0_OpaqueExpression147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_OpaqueExpression__uml3_0_0_OpaqueExpression147", None)
        self.__uml3_0_0_OpaqueExpression147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Parameter"):
                opp_val = getattr(old_value, "uml3_0_0_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Parameter"):
                opp_val = getattr(value, "uml3_0_0_Parameter", None)
                setattr(value, "uml3_0_0_Parameter", self)

class Dependency:

    pass
class uml3_0_0_Deployment(Dependency):

    pass
class uml3_0_0_Usage(Dependency):

    pass
class uml3_0_0_Abstraction(Dependency):

    pass
class Abstraction:

    pass
class uml3_0_0_Manifestation(Abstraction):

    pass
class uml3_0_0_Realization(Abstraction):

    pass
class MultiplicityElement:

    pass
class uml3_0_0_Pin(MultiplicityElement, ObjectNode):

    def __init__(self, isControl: str):
        self.isControl = isControl
        
    @property
    def isControl(self) -> str:
        return self.__isControl

    @isControl.setter
    def isControl(self, isControl: str):
        self.__isControl = isControl

class uml3_0_0_ConnectorEnd(MultiplicityElement):

    pass
class ConnectableElement:

    pass
class uml3_0_0_Variable(MultiplicityElement, ConnectableElement):

    pass
class uml3_0_0_Parameter(MultiplicityElement, ConnectableElement):

    def __init__(self, direction: str, default: str, isException: str, isStream: str, effect: str, parameter: set["uml3_0_0_ParameterSet"] = None, uml3_0_0_Parameter152: "uml3_0_0_Operation" = None, uml3_0_0_Parameter154: "uml3_0_0_ValueSpecification" = None, uml3_0_0_Parameter: "uml3_0_0_OpaqueExpression" = None, uml3_0_0_Parameter239: "uml3_0_0_BehavioralFeature" = None, uml3_0_0_Parameter251: "uml3_0_0_Behavior" = None, Parameter: "uml3_0_0_ParameterSet" = None, uml3_0_0_Parameter664: "uml3_0_0_ActivityParameterNode" = None):
        self.direction = direction
        self.default = default
        self.isException = isException
        self.isStream = isStream
        self.effect = effect
        self.parameter = parameter if parameter is not None else set()
        self.uml3_0_0_Parameter152 = uml3_0_0_Parameter152
        self.uml3_0_0_Parameter154 = uml3_0_0_Parameter154
        self.uml3_0_0_Parameter = uml3_0_0_Parameter
        self.uml3_0_0_Parameter239 = uml3_0_0_Parameter239
        self.uml3_0_0_Parameter251 = uml3_0_0_Parameter251
        self.Parameter = Parameter
        self.uml3_0_0_Parameter664 = uml3_0_0_Parameter664
        
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
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

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
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__parameter", None)
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
    def uml3_0_0_Parameter239(self):
        return self.__uml3_0_0_Parameter239

    @uml3_0_0_Parameter239.setter
    def uml3_0_0_Parameter239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__uml3_0_0_Parameter239", None)
        self.__uml3_0_0_Parameter239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_BehavioralFeature"):
                opp_val = getattr(old_value, "uml3_0_0_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_BehavioralFeature"):
                opp_val = getattr(value, "uml3_0_0_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Parameter251(self):
        return self.__uml3_0_0_Parameter251

    @uml3_0_0_Parameter251.setter
    def uml3_0_0_Parameter251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__uml3_0_0_Parameter251", None)
        self.__uml3_0_0_Parameter251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior250"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior250", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior250"):
                opp_val = getattr(value, "uml3_0_0_Behavior250", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Behavior250", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__Parameter", None)
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
    def uml3_0_0_Parameter(self):
        return self.__uml3_0_0_Parameter

    @uml3_0_0_Parameter.setter
    def uml3_0_0_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__uml3_0_0_Parameter", None)
        self.__uml3_0_0_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_OpaqueExpression147"):
                opp_val = getattr(old_value, "uml3_0_0_OpaqueExpression147", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_OpaqueExpression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_OpaqueExpression147"):
                opp_val = getattr(value, "uml3_0_0_OpaqueExpression147", None)
                setattr(value, "uml3_0_0_OpaqueExpression147", self)

    @property
    def uml3_0_0_Parameter664(self):
        return self.__uml3_0_0_Parameter664

    @uml3_0_0_Parameter664.setter
    def uml3_0_0_Parameter664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__uml3_0_0_Parameter664", None)
        self.__uml3_0_0_Parameter664 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ActivityParameterNode"):
                opp_val = getattr(old_value, "uml3_0_0_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ActivityParameterNode"):
                opp_val = getattr(value, "uml3_0_0_ActivityParameterNode", None)
                setattr(value, "uml3_0_0_ActivityParameterNode", self)

    @property
    def uml3_0_0_Parameter154(self):
        return self.__uml3_0_0_Parameter154

    @uml3_0_0_Parameter154.setter
    def uml3_0_0_Parameter154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__uml3_0_0_Parameter154", None)
        self.__uml3_0_0_Parameter154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ValueSpecification155"):
                opp_val = getattr(old_value, "uml3_0_0_ValueSpecification155", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ValueSpecification155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ValueSpecification155"):
                opp_val = getattr(value, "uml3_0_0_ValueSpecification155", None)
                setattr(value, "uml3_0_0_ValueSpecification155", self)

    @property
    def uml3_0_0_Parameter152(self):
        return self.__uml3_0_0_Parameter152

    @uml3_0_0_Parameter152.setter
    def uml3_0_0_Parameter152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Parameter__uml3_0_0_Parameter152", None)
        self.__uml3_0_0_Parameter152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Operation"):
                opp_val = getattr(old_value, "uml3_0_0_Operation", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Operation"):
                opp_val = getattr(value, "uml3_0_0_Operation", None)
                setattr(value, "uml3_0_0_Operation", self)

class Realization:

    pass
class uml3_0_0_ComponentRealization(Realization):

    pass
class uml3_0_0_InterfaceRealization(Realization):

    pass
class uml3_0_0_Substitution(Realization):

    pass
class uml3_0_0_UseCase(BehavioredClassifier):

    pass
class TypedElement:

    pass
class uml3_0_0_ObjectNode(TypedElement, ActivityNode):

    def __init__(self, ordering: str, isControlType: str, uml3_0_0_ObjectNode: "uml3_0_0_ExceptionHandler" = None, uml3_0_0_ObjectNode634: "uml3_0_0_ValueSpecification" = None, uml3_0_0_ObjectNode637: set["uml3_0_0_State"] = None, uml3_0_0_ObjectNode640: "uml3_0_0_Behavior" = None):
        self.ordering = ordering
        self.isControlType = isControlType
        self.uml3_0_0_ObjectNode = uml3_0_0_ObjectNode
        self.uml3_0_0_ObjectNode634 = uml3_0_0_ObjectNode634
        self.uml3_0_0_ObjectNode637 = uml3_0_0_ObjectNode637 if uml3_0_0_ObjectNode637 is not None else set()
        self.uml3_0_0_ObjectNode640 = uml3_0_0_ObjectNode640
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def isControlType(self) -> str:
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: str):
        self.__isControlType = isControlType

    @property
    def uml3_0_0_ObjectNode(self):
        return self.__uml3_0_0_ObjectNode

    @uml3_0_0_ObjectNode.setter
    def uml3_0_0_ObjectNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ObjectNode__uml3_0_0_ObjectNode", None)
        self.__uml3_0_0_ObjectNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ExceptionHandler628"):
                opp_val = getattr(old_value, "uml3_0_0_ExceptionHandler628", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ExceptionHandler628", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ExceptionHandler628"):
                opp_val = getattr(value, "uml3_0_0_ExceptionHandler628", None)
                setattr(value, "uml3_0_0_ExceptionHandler628", self)

    @property
    def uml3_0_0_ObjectNode637(self):
        return self.__uml3_0_0_ObjectNode637

    @uml3_0_0_ObjectNode637.setter
    def uml3_0_0_ObjectNode637(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ObjectNode__uml3_0_0_ObjectNode637", None)
        self.__uml3_0_0_ObjectNode637 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_State638"):
                    opp_val = getattr(item, "uml3_0_0_State638", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_State638", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_State638"):
                    opp_val = getattr(item, "uml3_0_0_State638", None)
                    
                    setattr(item, "uml3_0_0_State638", self)
                    

    @property
    def uml3_0_0_ObjectNode634(self):
        return self.__uml3_0_0_ObjectNode634

    @uml3_0_0_ObjectNode634.setter
    def uml3_0_0_ObjectNode634(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ObjectNode__uml3_0_0_ObjectNode634", None)
        self.__uml3_0_0_ObjectNode634 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ValueSpecification635"):
                opp_val = getattr(old_value, "uml3_0_0_ValueSpecification635", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ValueSpecification635", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ValueSpecification635"):
                opp_val = getattr(value, "uml3_0_0_ValueSpecification635", None)
                setattr(value, "uml3_0_0_ValueSpecification635", self)

    @property
    def uml3_0_0_ObjectNode640(self):
        return self.__uml3_0_0_ObjectNode640

    @uml3_0_0_ObjectNode640.setter
    def uml3_0_0_ObjectNode640(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ObjectNode__uml3_0_0_ObjectNode640", None)
        self.__uml3_0_0_ObjectNode640 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior641"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior641", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior641", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior641"):
                opp_val = getattr(value, "uml3_0_0_Behavior641", None)
                setattr(value, "uml3_0_0_Behavior641", self)

class uml3_0_0_StructuralFeature(TypedElement, MultiplicityElement, Feature):

    def __init__(self, isReadOnly: str, uml3_0_0_StructuralFeature: "uml3_0_0_Slot" = None, uml3_0_0_StructuralFeature811: "uml3_0_0_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.uml3_0_0_StructuralFeature = uml3_0_0_StructuralFeature
        self.uml3_0_0_StructuralFeature811 = uml3_0_0_StructuralFeature811
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def uml3_0_0_StructuralFeature811(self):
        return self.__uml3_0_0_StructuralFeature811

    @uml3_0_0_StructuralFeature811.setter
    def uml3_0_0_StructuralFeature811(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuralFeature__uml3_0_0_StructuralFeature811", None)
        self.__uml3_0_0_StructuralFeature811 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_StructuralFeatureAction"):
                opp_val = getattr(old_value, "uml3_0_0_StructuralFeatureAction", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_StructuralFeatureAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_StructuralFeatureAction"):
                opp_val = getattr(value, "uml3_0_0_StructuralFeatureAction", None)
                setattr(value, "uml3_0_0_StructuralFeatureAction", self)

    @property
    def uml3_0_0_StructuralFeature(self):
        return self.__uml3_0_0_StructuralFeature

    @uml3_0_0_StructuralFeature.setter
    def uml3_0_0_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuralFeature__uml3_0_0_StructuralFeature", None)
        self.__uml3_0_0_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Slot"):
                opp_val = getattr(old_value, "uml3_0_0_Slot", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Slot"):
                opp_val = getattr(value, "uml3_0_0_Slot", None)
                setattr(value, "uml3_0_0_Slot", self)

class Type:

    pass
class RedefinableElement:

    pass
class uml3_0_0_RedefinableTemplateSignature(TemplateSignature, RedefinableElement):

    pass
class uml3_0_0_ActivityNode(RedefinableElement):

    pass
class uml3_0_0_ExtensionPoint(RedefinableElement):

    pass
class uml3_0_0_Feature(RedefinableElement):

    def __init__(self, isStatic: str, Feature: "uml3_0_0_Classifier" = None, feature: set["uml3_0_0_Classifier"] = None):
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
        old_value = getattr(self, f"_uml3_0_0_Feature__feature", None)
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
        old_value = getattr(self, f"_uml3_0_0_Feature__Feature", None)
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

class uml3_0_0_ActivityEdge(RedefinableElement):

    pass
class uml3_0_0_Property(StructuralFeature, ConnectableElement, DeploymentTarget):

    def __init__(self, isDerived: str, aggregation: str, isComposite: str, isDerivedUnion: str, default: str, Property: "uml3_0_0_Association" = None, Property61: "uml3_0_0_Association" = None, uml3_0_0_Property: "uml3_0_0_Association" = None, uml3_0_0_Property80: "uml3_0_0_Classifier" = None, uml3_0_0_Property164: "uml3_0_0_ConnectorEnd" = None, uml3_0_0_Property170: "uml3_0_0_ConnectorEnd" = None, uml3_0_0_Property172: "uml3_0_0_Class" = None, ownedAttribute: "uml3_0_0_DataType" = None, uml3_0_0_Property176: "uml3_0_0_Property" = None, uml3_0_0_Property174: set["uml3_0_0_Property"] = None, ownedEnd: "uml3_0_0_Association" = None, uml3_0_0_Property179: "uml3_0_0_ValueSpecification" = None, uml3_0_0_Property183: "uml3_0_0_Property" = None, uml3_0_0_Property181: "uml3_0_0_Property" = None, uml3_0_0_Property186: "uml3_0_0_Property" = None, uml3_0_0_Property184: set["uml3_0_0_Property"] = None, memberEnd: "uml3_0_0_Association" = None, Property194: "uml3_0_0_Property" = None, qualifier: "uml3_0_0_Property" = None, Property191: "uml3_0_0_Property" = None, associationEnd: set["uml3_0_0_Property"] = None, uml3_0_0_Property213: "uml3_0_0_Artifact" = None, uml3_0_0_Property287: "uml3_0_0_Interface" = None, uml3_0_0_Property305: "uml3_0_0_Signal" = None, uml3_0_0_Property407: "uml3_0_0_StructuredClassifier" = None, uml3_0_0_Property410: "uml3_0_0_StructuredClassifier" = None, Property444: "uml3_0_0_DataType" = None, uml3_0_0_Property842: "uml3_0_0_QualifierValue" = None, uml3_0_0_Property837: "uml3_0_0_LinkEndData" = None, uml3_0_0_Property951: "uml3_0_0_ReadLinkObjectEndAction" = None, uml3_0_0_Property962: "uml3_0_0_ReadLinkObjectEndQualifierAction" = None):
        self.isDerived = isDerived
        self.aggregation = aggregation
        self.isComposite = isComposite
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.Property = Property
        self.Property61 = Property61
        self.uml3_0_0_Property = uml3_0_0_Property
        self.uml3_0_0_Property80 = uml3_0_0_Property80
        self.uml3_0_0_Property164 = uml3_0_0_Property164
        self.uml3_0_0_Property170 = uml3_0_0_Property170
        self.uml3_0_0_Property172 = uml3_0_0_Property172
        self.ownedAttribute = ownedAttribute
        self.uml3_0_0_Property176 = uml3_0_0_Property176
        self.uml3_0_0_Property174 = uml3_0_0_Property174 if uml3_0_0_Property174 is not None else set()
        self.ownedEnd = ownedEnd
        self.uml3_0_0_Property179 = uml3_0_0_Property179
        self.uml3_0_0_Property183 = uml3_0_0_Property183
        self.uml3_0_0_Property181 = uml3_0_0_Property181
        self.uml3_0_0_Property186 = uml3_0_0_Property186
        self.uml3_0_0_Property184 = uml3_0_0_Property184 if uml3_0_0_Property184 is not None else set()
        self.memberEnd = memberEnd
        self.Property194 = Property194
        self.qualifier = qualifier
        self.Property191 = Property191
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.uml3_0_0_Property213 = uml3_0_0_Property213
        self.uml3_0_0_Property287 = uml3_0_0_Property287
        self.uml3_0_0_Property305 = uml3_0_0_Property305
        self.uml3_0_0_Property407 = uml3_0_0_Property407
        self.uml3_0_0_Property410 = uml3_0_0_Property410
        self.Property444 = Property444
        self.uml3_0_0_Property842 = uml3_0_0_Property842
        self.uml3_0_0_Property837 = uml3_0_0_Property837
        self.uml3_0_0_Property951 = uml3_0_0_Property951
        self.uml3_0_0_Property962 = uml3_0_0_Property962
        
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
    def uml3_0_0_Property213(self):
        return self.__uml3_0_0_Property213

    @uml3_0_0_Property213.setter
    def uml3_0_0_Property213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property213", None)
        self.__uml3_0_0_Property213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Artifact212"):
                opp_val = getattr(old_value, "uml3_0_0_Artifact212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Artifact212"):
                opp_val = getattr(value, "uml3_0_0_Artifact212", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Artifact212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property407(self):
        return self.__uml3_0_0_Property407

    @uml3_0_0_Property407.setter
    def uml3_0_0_Property407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property407", None)
        self.__uml3_0_0_Property407 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_StructuredClassifier"):
                opp_val = getattr(old_value, "uml3_0_0_StructuredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_StructuredClassifier"):
                opp_val = getattr(value, "uml3_0_0_StructuredClassifier", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_StructuredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property842(self):
        return self.__uml3_0_0_Property842

    @uml3_0_0_Property842.setter
    def uml3_0_0_Property842(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property842", None)
        self.__uml3_0_0_Property842 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_QualifierValue841"):
                opp_val = getattr(old_value, "uml3_0_0_QualifierValue841", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_QualifierValue841", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_QualifierValue841"):
                opp_val = getattr(value, "uml3_0_0_QualifierValue841", None)
                setattr(value, "uml3_0_0_QualifierValue841", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__ownedAttribute", None)
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
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__ownedEnd", None)
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
    def uml3_0_0_Property174(self):
        return self.__uml3_0_0_Property174

    @uml3_0_0_Property174.setter
    def uml3_0_0_Property174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property174", None)
        self.__uml3_0_0_Property174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Property176"):
                    opp_val = getattr(item, "uml3_0_0_Property176", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Property176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Property176"):
                    opp_val = getattr(item, "uml3_0_0_Property176", None)
                    
                    setattr(item, "uml3_0_0_Property176", self)
                    

    @property
    def Property61(self):
        return self.__Property61

    @Property61.setter
    def Property61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__Property61", None)
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
    def Property194(self):
        return self.__Property194

    @Property194.setter
    def Property194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__Property194", None)
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
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__qualifier", None)
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
    def uml3_0_0_Property164(self):
        return self.__uml3_0_0_Property164

    @uml3_0_0_Property164.setter
    def uml3_0_0_Property164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property164", None)
        self.__uml3_0_0_Property164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ConnectorEnd163"):
                opp_val = getattr(old_value, "uml3_0_0_ConnectorEnd163", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ConnectorEnd163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ConnectorEnd163"):
                opp_val = getattr(value, "uml3_0_0_ConnectorEnd163", None)
                setattr(value, "uml3_0_0_ConnectorEnd163", self)

    @property
    def uml3_0_0_Property287(self):
        return self.__uml3_0_0_Property287

    @uml3_0_0_Property287.setter
    def uml3_0_0_Property287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property287", None)
        self.__uml3_0_0_Property287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Interface286"):
                opp_val = getattr(old_value, "uml3_0_0_Interface286", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Interface286"):
                opp_val = getattr(value, "uml3_0_0_Interface286", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Interface286", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property176(self):
        return self.__uml3_0_0_Property176

    @uml3_0_0_Property176.setter
    def uml3_0_0_Property176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property176", None)
        self.__uml3_0_0_Property176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Property174"):
                opp_val = getattr(old_value, "uml3_0_0_Property174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Property174"):
                opp_val = getattr(value, "uml3_0_0_Property174", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Property174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property183(self):
        return self.__uml3_0_0_Property183

    @uml3_0_0_Property183.setter
    def uml3_0_0_Property183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property183", None)
        self.__uml3_0_0_Property183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Property181"):
                opp_val = getattr(old_value, "uml3_0_0_Property181", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Property181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Property181"):
                opp_val = getattr(value, "uml3_0_0_Property181", None)
                setattr(value, "uml3_0_0_Property181", self)

    @property
    def uml3_0_0_Property410(self):
        return self.__uml3_0_0_Property410

    @uml3_0_0_Property410.setter
    def uml3_0_0_Property410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property410", None)
        self.__uml3_0_0_Property410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_StructuredClassifier409"):
                opp_val = getattr(old_value, "uml3_0_0_StructuredClassifier409", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_StructuredClassifier409"):
                opp_val = getattr(value, "uml3_0_0_StructuredClassifier409", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_StructuredClassifier409", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property191(self):
        return self.__Property191

    @Property191.setter
    def Property191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__Property191", None)
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
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__associationEnd", None)
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
    def uml3_0_0_Property(self):
        return self.__uml3_0_0_Property

    @uml3_0_0_Property.setter
    def uml3_0_0_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property", None)
        self.__uml3_0_0_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Association65"):
                opp_val = getattr(old_value, "uml3_0_0_Association65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Association65"):
                opp_val = getattr(value, "uml3_0_0_Association65", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Association65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property181(self):
        return self.__uml3_0_0_Property181

    @uml3_0_0_Property181.setter
    def uml3_0_0_Property181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property181", None)
        self.__uml3_0_0_Property181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Property183"):
                opp_val = getattr(old_value, "uml3_0_0_Property183", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Property183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Property183"):
                opp_val = getattr(value, "uml3_0_0_Property183", None)
                setattr(value, "uml3_0_0_Property183", self)

    @property
    def uml3_0_0_Property170(self):
        return self.__uml3_0_0_Property170

    @uml3_0_0_Property170.setter
    def uml3_0_0_Property170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property170", None)
        self.__uml3_0_0_Property170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ConnectorEnd169"):
                opp_val = getattr(old_value, "uml3_0_0_ConnectorEnd169", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ConnectorEnd169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ConnectorEnd169"):
                opp_val = getattr(value, "uml3_0_0_ConnectorEnd169", None)
                setattr(value, "uml3_0_0_ConnectorEnd169", self)

    @property
    def uml3_0_0_Property80(self):
        return self.__uml3_0_0_Property80

    @uml3_0_0_Property80.setter
    def uml3_0_0_Property80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property80", None)
        self.__uml3_0_0_Property80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Classifier79"):
                opp_val = getattr(old_value, "uml3_0_0_Classifier79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Classifier79"):
                opp_val = getattr(value, "uml3_0_0_Classifier79", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Classifier79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property172(self):
        return self.__uml3_0_0_Property172

    @uml3_0_0_Property172.setter
    def uml3_0_0_Property172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property172", None)
        self.__uml3_0_0_Property172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Class"):
                opp_val = getattr(old_value, "uml3_0_0_Class", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Class"):
                opp_val = getattr(value, "uml3_0_0_Class", None)
                setattr(value, "uml3_0_0_Class", self)

    @property
    def uml3_0_0_Property951(self):
        return self.__uml3_0_0_Property951

    @uml3_0_0_Property951.setter
    def uml3_0_0_Property951(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property951", None)
        self.__uml3_0_0_Property951 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReadLinkObjectEndAction950"):
                opp_val = getattr(old_value, "uml3_0_0_ReadLinkObjectEndAction950", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ReadLinkObjectEndAction950", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReadLinkObjectEndAction950"):
                opp_val = getattr(value, "uml3_0_0_ReadLinkObjectEndAction950", None)
                setattr(value, "uml3_0_0_ReadLinkObjectEndAction950", self)

    @property
    def uml3_0_0_Property179(self):
        return self.__uml3_0_0_Property179

    @uml3_0_0_Property179.setter
    def uml3_0_0_Property179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property179", None)
        self.__uml3_0_0_Property179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ValueSpecification180"):
                opp_val = getattr(old_value, "uml3_0_0_ValueSpecification180", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ValueSpecification180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ValueSpecification180"):
                opp_val = getattr(value, "uml3_0_0_ValueSpecification180", None)
                setattr(value, "uml3_0_0_ValueSpecification180", self)

    @property
    def uml3_0_0_Property184(self):
        return self.__uml3_0_0_Property184

    @uml3_0_0_Property184.setter
    def uml3_0_0_Property184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property184", None)
        self.__uml3_0_0_Property184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Property186"):
                    opp_val = getattr(item, "uml3_0_0_Property186", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Property186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Property186"):
                    opp_val = getattr(item, "uml3_0_0_Property186", None)
                    
                    setattr(item, "uml3_0_0_Property186", self)
                    

    @property
    def uml3_0_0_Property186(self):
        return self.__uml3_0_0_Property186

    @uml3_0_0_Property186.setter
    def uml3_0_0_Property186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property186", None)
        self.__uml3_0_0_Property186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Property184"):
                opp_val = getattr(old_value, "uml3_0_0_Property184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Property184"):
                opp_val = getattr(value, "uml3_0_0_Property184", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Property184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property305(self):
        return self.__uml3_0_0_Property305

    @uml3_0_0_Property305.setter
    def uml3_0_0_Property305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property305", None)
        self.__uml3_0_0_Property305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Signal304"):
                opp_val = getattr(old_value, "uml3_0_0_Signal304", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Signal304"):
                opp_val = getattr(value, "uml3_0_0_Signal304", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Signal304", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Property837(self):
        return self.__uml3_0_0_Property837

    @uml3_0_0_Property837.setter
    def uml3_0_0_Property837(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property837", None)
        self.__uml3_0_0_Property837 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_LinkEndData836"):
                opp_val = getattr(old_value, "uml3_0_0_LinkEndData836", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_LinkEndData836", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_LinkEndData836"):
                opp_val = getattr(value, "uml3_0_0_LinkEndData836", None)
                setattr(value, "uml3_0_0_LinkEndData836", self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__memberEnd", None)
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
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__Property", None)
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

    @property
    def Property444(self):
        return self.__Property444

    @Property444.setter
    def Property444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__Property444", None)
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
    def uml3_0_0_Property962(self):
        return self.__uml3_0_0_Property962

    @uml3_0_0_Property962.setter
    def uml3_0_0_Property962(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Property__uml3_0_0_Property962", None)
        self.__uml3_0_0_Property962 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReadLinkObjectEndQualifierAction961"):
                opp_val = getattr(old_value, "uml3_0_0_ReadLinkObjectEndQualifierAction961", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ReadLinkObjectEndQualifierAction961", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReadLinkObjectEndQualifierAction961"):
                opp_val = getattr(value, "uml3_0_0_ReadLinkObjectEndQualifierAction961", None)
                setattr(value, "uml3_0_0_ReadLinkObjectEndQualifierAction961", self)

class Classifier:

    pass
class uml3_0_0_Signal(Classifier):

    pass
class uml3_0_0_DataType(Classifier):

    pass
class uml3_0_0_BehavioredClassifier(Classifier):

    pass
class uml3_0_0_Artifact(DeployedArtifact, Classifier):

    def __init__(self, fileName: str, uml3_0_0_Artifact: "uml3_0_0_Artifact" = None, uml3_0_0_Artifact204: set["uml3_0_0_Artifact"] = None, uml3_0_0_Artifact207: set["uml3_0_0_Manifestation"] = None, uml3_0_0_Artifact209: set["uml3_0_0_Operation"] = None, uml3_0_0_Artifact212: set["uml3_0_0_Property"] = None):
        self.fileName = fileName
        self.uml3_0_0_Artifact = uml3_0_0_Artifact
        self.uml3_0_0_Artifact204 = uml3_0_0_Artifact204 if uml3_0_0_Artifact204 is not None else set()
        self.uml3_0_0_Artifact207 = uml3_0_0_Artifact207 if uml3_0_0_Artifact207 is not None else set()
        self.uml3_0_0_Artifact209 = uml3_0_0_Artifact209 if uml3_0_0_Artifact209 is not None else set()
        self.uml3_0_0_Artifact212 = uml3_0_0_Artifact212 if uml3_0_0_Artifact212 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def uml3_0_0_Artifact(self):
        return self.__uml3_0_0_Artifact

    @uml3_0_0_Artifact.setter
    def uml3_0_0_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Artifact__uml3_0_0_Artifact", None)
        self.__uml3_0_0_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Artifact204"):
                opp_val = getattr(old_value, "uml3_0_0_Artifact204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Artifact204"):
                opp_val = getattr(value, "uml3_0_0_Artifact204", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Artifact204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Artifact204(self):
        return self.__uml3_0_0_Artifact204

    @uml3_0_0_Artifact204.setter
    def uml3_0_0_Artifact204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Artifact__uml3_0_0_Artifact204", None)
        self.__uml3_0_0_Artifact204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Artifact"):
                    opp_val = getattr(item, "uml3_0_0_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Artifact"):
                    opp_val = getattr(item, "uml3_0_0_Artifact", None)
                    
                    setattr(item, "uml3_0_0_Artifact", self)
                    

    @property
    def uml3_0_0_Artifact212(self):
        return self.__uml3_0_0_Artifact212

    @uml3_0_0_Artifact212.setter
    def uml3_0_0_Artifact212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Artifact__uml3_0_0_Artifact212", None)
        self.__uml3_0_0_Artifact212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Property213"):
                    opp_val = getattr(item, "uml3_0_0_Property213", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Property213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Property213"):
                    opp_val = getattr(item, "uml3_0_0_Property213", None)
                    
                    setattr(item, "uml3_0_0_Property213", self)
                    

    @property
    def uml3_0_0_Artifact209(self):
        return self.__uml3_0_0_Artifact209

    @uml3_0_0_Artifact209.setter
    def uml3_0_0_Artifact209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Artifact__uml3_0_0_Artifact209", None)
        self.__uml3_0_0_Artifact209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Operation210"):
                    opp_val = getattr(item, "uml3_0_0_Operation210", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Operation210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Operation210"):
                    opp_val = getattr(item, "uml3_0_0_Operation210", None)
                    
                    setattr(item, "uml3_0_0_Operation210", self)
                    

    @property
    def uml3_0_0_Artifact207(self):
        return self.__uml3_0_0_Artifact207

    @uml3_0_0_Artifact207.setter
    def uml3_0_0_Artifact207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Artifact__uml3_0_0_Artifact207", None)
        self.__uml3_0_0_Artifact207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Manifestation"):
                    opp_val = getattr(item, "uml3_0_0_Manifestation", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Manifestation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Manifestation"):
                    opp_val = getattr(item, "uml3_0_0_Manifestation", None)
                    
                    setattr(item, "uml3_0_0_Manifestation", self)
                    

class uml3_0_0_Interface(Classifier):

    pass
class uml3_0_0_StructuredClassifier(Classifier):

    pass
class uml3_0_0_InformationItem(Classifier):

    pass
class ParameterableElement:

    pass
class uml3_0_0_ConnectableElement(TypedElement, ParameterableElement):

    pass
class NamedElement:

    pass
class uml3_0_0_MessageEnd(NamedElement):

    pass
class uml3_0_0_Lifeline(NamedElement):

    pass
class uml3_0_0_Message(NamedElement):

    def __init__(self, messageKind: str, messageSort: str, uml3_0_0_Message: "uml3_0_0_MessageEnd" = None, uml3_0_0_Message669: "uml3_0_0_MessageEnd" = None, uml3_0_0_Message672: "uml3_0_0_Connector" = None, message: "uml3_0_0_Interaction" = None, uml3_0_0_Message676: set["uml3_0_0_ValueSpecification"] = None, uml3_0_0_Message679: "uml3_0_0_NamedElement" = None, uml3_0_0_Message683: "uml3_0_0_MessageEnd" = None, Message: "uml3_0_0_Interaction" = None, uml3_0_0_Message923: "uml3_0_0_InformationFlow" = None):
        self.messageKind = messageKind
        self.messageSort = messageSort
        self.uml3_0_0_Message = uml3_0_0_Message
        self.uml3_0_0_Message669 = uml3_0_0_Message669
        self.uml3_0_0_Message672 = uml3_0_0_Message672
        self.message = message
        self.uml3_0_0_Message676 = uml3_0_0_Message676 if uml3_0_0_Message676 is not None else set()
        self.uml3_0_0_Message679 = uml3_0_0_Message679
        self.uml3_0_0_Message683 = uml3_0_0_Message683
        self.Message = Message
        self.uml3_0_0_Message923 = uml3_0_0_Message923
        
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
    def uml3_0_0_Message923(self):
        return self.__uml3_0_0_Message923

    @uml3_0_0_Message923.setter
    def uml3_0_0_Message923(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__uml3_0_0_Message923", None)
        self.__uml3_0_0_Message923 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InformationFlow922"):
                opp_val = getattr(old_value, "uml3_0_0_InformationFlow922", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InformationFlow922"):
                opp_val = getattr(value, "uml3_0_0_InformationFlow922", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_InformationFlow922", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Message(self):
        return self.__uml3_0_0_Message

    @uml3_0_0_Message.setter
    def uml3_0_0_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__uml3_0_0_Message", None)
        self.__uml3_0_0_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_MessageEnd"):
                opp_val = getattr(old_value, "uml3_0_0_MessageEnd", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_MessageEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_MessageEnd"):
                opp_val = getattr(value, "uml3_0_0_MessageEnd", None)
                setattr(value, "uml3_0_0_MessageEnd", self)

    @property
    def uml3_0_0_Message683(self):
        return self.__uml3_0_0_Message683

    @uml3_0_0_Message683.setter
    def uml3_0_0_Message683(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__uml3_0_0_Message683", None)
        self.__uml3_0_0_Message683 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_MessageEnd682"):
                opp_val = getattr(old_value, "uml3_0_0_MessageEnd682", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_MessageEnd682", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_MessageEnd682"):
                opp_val = getattr(value, "uml3_0_0_MessageEnd682", None)
                setattr(value, "uml3_0_0_MessageEnd682", self)

    @property
    def uml3_0_0_Message676(self):
        return self.__uml3_0_0_Message676

    @uml3_0_0_Message676.setter
    def uml3_0_0_Message676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__uml3_0_0_Message676", None)
        self.__uml3_0_0_Message676 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ValueSpecification677"):
                    opp_val = getattr(item, "uml3_0_0_ValueSpecification677", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ValueSpecification677", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ValueSpecification677"):
                    opp_val = getattr(item, "uml3_0_0_ValueSpecification677", None)
                    
                    setattr(item, "uml3_0_0_ValueSpecification677", self)
                    

    @property
    def uml3_0_0_Message669(self):
        return self.__uml3_0_0_Message669

    @uml3_0_0_Message669.setter
    def uml3_0_0_Message669(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__uml3_0_0_Message669", None)
        self.__uml3_0_0_Message669 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_MessageEnd670"):
                opp_val = getattr(old_value, "uml3_0_0_MessageEnd670", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_MessageEnd670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_MessageEnd670"):
                opp_val = getattr(value, "uml3_0_0_MessageEnd670", None)
                setattr(value, "uml3_0_0_MessageEnd670", self)

    @property
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__Message", None)
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

    @property
    def uml3_0_0_Message679(self):
        return self.__uml3_0_0_Message679

    @uml3_0_0_Message679.setter
    def uml3_0_0_Message679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__uml3_0_0_Message679", None)
        self.__uml3_0_0_Message679 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_NamedElement680"):
                opp_val = getattr(old_value, "uml3_0_0_NamedElement680", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_NamedElement680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_NamedElement680"):
                opp_val = getattr(value, "uml3_0_0_NamedElement680", None)
                setattr(value, "uml3_0_0_NamedElement680", self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__message", None)
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
    def uml3_0_0_Message672(self):
        return self.__uml3_0_0_Message672

    @uml3_0_0_Message672.setter
    def uml3_0_0_Message672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Message__uml3_0_0_Message672", None)
        self.__uml3_0_0_Message672 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Connector673"):
                opp_val = getattr(old_value, "uml3_0_0_Connector673", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Connector673", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Connector673"):
                opp_val = getattr(value, "uml3_0_0_Connector673", None)
                setattr(value, "uml3_0_0_Connector673", self)

class uml3_0_0_Trigger(NamedElement):

    pass
class uml3_0_0_InteractionFragment(NamedElement):

    pass
class uml3_0_0_ParameterSet(NamedElement):

    pass
class uml3_0_0_DeploymentTarget(NamedElement):

    pass
class uml3_0_0_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: str, uml3_0_0_RedefinableElement: "uml3_0_0_RedefinableElement" = None, uml3_0_0_RedefinableElement89: set["uml3_0_0_RedefinableElement"] = None, uml3_0_0_RedefinableElement92: set["uml3_0_0_Classifier"] = None):
        self.isLeaf = isLeaf
        self.uml3_0_0_RedefinableElement = uml3_0_0_RedefinableElement
        self.uml3_0_0_RedefinableElement89 = uml3_0_0_RedefinableElement89 if uml3_0_0_RedefinableElement89 is not None else set()
        self.uml3_0_0_RedefinableElement92 = uml3_0_0_RedefinableElement92 if uml3_0_0_RedefinableElement92 is not None else set()
        
    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def uml3_0_0_RedefinableElement92(self):
        return self.__uml3_0_0_RedefinableElement92

    @uml3_0_0_RedefinableElement92.setter
    def uml3_0_0_RedefinableElement92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_RedefinableElement__uml3_0_0_RedefinableElement92", None)
        self.__uml3_0_0_RedefinableElement92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Classifier93"):
                    opp_val = getattr(item, "uml3_0_0_Classifier93", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Classifier93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Classifier93"):
                    opp_val = getattr(item, "uml3_0_0_Classifier93", None)
                    
                    setattr(item, "uml3_0_0_Classifier93", self)
                    

    @property
    def uml3_0_0_RedefinableElement(self):
        return self.__uml3_0_0_RedefinableElement

    @uml3_0_0_RedefinableElement.setter
    def uml3_0_0_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_RedefinableElement__uml3_0_0_RedefinableElement", None)
        self.__uml3_0_0_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_RedefinableElement89"):
                opp_val = getattr(old_value, "uml3_0_0_RedefinableElement89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_RedefinableElement89"):
                opp_val = getattr(value, "uml3_0_0_RedefinableElement89", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_RedefinableElement89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_RedefinableElement89(self):
        return self.__uml3_0_0_RedefinableElement89

    @uml3_0_0_RedefinableElement89.setter
    def uml3_0_0_RedefinableElement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_RedefinableElement__uml3_0_0_RedefinableElement89", None)
        self.__uml3_0_0_RedefinableElement89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_RedefinableElement"):
                    opp_val = getattr(item, "uml3_0_0_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_RedefinableElement"):
                    opp_val = getattr(item, "uml3_0_0_RedefinableElement", None)
                    
                    setattr(item, "uml3_0_0_RedefinableElement", self)
                    

class uml3_0_0_Vertex(NamedElement):

    pass
class uml3_0_0_ActivityPartition(ActivityGroup, NamedElement):

    def __init__(self, isDimension: str, isExternal: str, ActivityPartition: "uml3_0_0_ActivityNode" = None, uml3_0_0_ActivityPartition: "uml3_0_0_Activity" = None, ActivityPartition591: "uml3_0_0_ActivityEdge" = None, inPartition: set["uml3_0_0_ActivityNode"] = None, ActivityPartition612: "uml3_0_0_ActivityPartition" = None, superPartition: set["uml3_0_0_ActivityPartition"] = None, uml3_0_0_ActivityPartition617: "uml3_0_0_Element" = None, inPartition620: set["uml3_0_0_ActivityEdge"] = None, ActivityPartition615: "uml3_0_0_ActivityPartition" = None, subpartition: "uml3_0_0_ActivityPartition" = None):
        self.isDimension = isDimension
        self.isExternal = isExternal
        self.ActivityPartition = ActivityPartition
        self.uml3_0_0_ActivityPartition = uml3_0_0_ActivityPartition
        self.ActivityPartition591 = ActivityPartition591
        self.inPartition = inPartition if inPartition is not None else set()
        self.ActivityPartition612 = ActivityPartition612
        self.superPartition = superPartition if superPartition is not None else set()
        self.uml3_0_0_ActivityPartition617 = uml3_0_0_ActivityPartition617
        self.inPartition620 = inPartition620 if inPartition620 is not None else set()
        self.ActivityPartition615 = ActivityPartition615
        self.subpartition = subpartition
        
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
    def ActivityPartition615(self):
        return self.__ActivityPartition615

    @ActivityPartition615.setter
    def ActivityPartition615(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__ActivityPartition615", None)
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

    @property
    def superPartition(self):
        return self.__superPartition

    @superPartition.setter
    def superPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__superPartition", None)
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
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__ActivityPartition591", None)
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
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__ActivityPartition", None)
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
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__ActivityPartition612", None)
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
    def subpartition(self):
        return self.__subpartition

    @subpartition.setter
    def subpartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__subpartition", None)
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
    def inPartition620(self):
        return self.__inPartition620

    @inPartition620.setter
    def inPartition620(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__inPartition620", None)
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
    def uml3_0_0_ActivityPartition(self):
        return self.__uml3_0_0_ActivityPartition

    @uml3_0_0_ActivityPartition.setter
    def uml3_0_0_ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__uml3_0_0_ActivityPartition", None)
        self.__uml3_0_0_ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Activity576"):
                opp_val = getattr(old_value, "uml3_0_0_Activity576", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Activity576"):
                opp_val = getattr(value, "uml3_0_0_Activity576", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Activity576", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inPartition(self):
        return self.__inPartition

    @inPartition.setter
    def inPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__inPartition", None)
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
    def uml3_0_0_ActivityPartition617(self):
        return self.__uml3_0_0_ActivityPartition617

    @uml3_0_0_ActivityPartition617.setter
    def uml3_0_0_ActivityPartition617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ActivityPartition__uml3_0_0_ActivityPartition617", None)
        self.__uml3_0_0_ActivityPartition617 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Element618"):
                opp_val = getattr(old_value, "uml3_0_0_Element618", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Element618", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Element618"):
                opp_val = getattr(value, "uml3_0_0_Element618", None)
                setattr(value, "uml3_0_0_Element618", self)

class uml3_0_0_TypedElement(NamedElement):

    pass
class uml3_0_0_GeneralOrdering(NamedElement):

    pass
class uml3_0_0_DeployedArtifact(NamedElement):

    pass
class uml3_0_0_CollaborationUse(NamedElement):

    pass
class Relationship:

    pass
class uml3_0_0_Association(Classifier, Relationship):

    def __init__(self, isDerived: str, owningAssociation: set["uml3_0_0_Property"] = None, association: set["uml3_0_0_Property"] = None, uml3_0_0_Association: set["uml3_0_0_Type"] = None, uml3_0_0_Association65: set["uml3_0_0_Property"] = None, Association: "uml3_0_0_Property" = None, Association188: "uml3_0_0_Property" = None, uml3_0_0_Association418: "uml3_0_0_Connector" = None, uml3_0_0_Association856: "uml3_0_0_ClearAssociationAction" = None):
        self.isDerived = isDerived
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.association = association if association is not None else set()
        self.uml3_0_0_Association = uml3_0_0_Association if uml3_0_0_Association is not None else set()
        self.uml3_0_0_Association65 = uml3_0_0_Association65 if uml3_0_0_Association65 is not None else set()
        self.Association = Association
        self.Association188 = Association188
        self.uml3_0_0_Association418 = uml3_0_0_Association418
        self.uml3_0_0_Association856 = uml3_0_0_Association856
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__association", None)
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
    def uml3_0_0_Association418(self):
        return self.__uml3_0_0_Association418

    @uml3_0_0_Association418.setter
    def uml3_0_0_Association418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__uml3_0_0_Association418", None)
        self.__uml3_0_0_Association418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Connector417"):
                opp_val = getattr(old_value, "uml3_0_0_Connector417", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Connector417", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Connector417"):
                opp_val = getattr(value, "uml3_0_0_Connector417", None)
                setattr(value, "uml3_0_0_Connector417", self)

    @property
    def Association188(self):
        return self.__Association188

    @Association188.setter
    def Association188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__Association188", None)
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

    @property
    def uml3_0_0_Association856(self):
        return self.__uml3_0_0_Association856

    @uml3_0_0_Association856.setter
    def uml3_0_0_Association856(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__uml3_0_0_Association856", None)
        self.__uml3_0_0_Association856 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ClearAssociationAction855"):
                opp_val = getattr(old_value, "uml3_0_0_ClearAssociationAction855", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ClearAssociationAction855", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ClearAssociationAction855"):
                opp_val = getattr(value, "uml3_0_0_ClearAssociationAction855", None)
                setattr(value, "uml3_0_0_ClearAssociationAction855", self)

    @property
    def uml3_0_0_Association(self):
        return self.__uml3_0_0_Association

    @uml3_0_0_Association.setter
    def uml3_0_0_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__uml3_0_0_Association", None)
        self.__uml3_0_0_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Type63"):
                    opp_val = getattr(item, "uml3_0_0_Type63", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Type63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Type63"):
                    opp_val = getattr(item, "uml3_0_0_Type63", None)
                    
                    setattr(item, "uml3_0_0_Type63", self)
                    

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__owningAssociation", None)
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
    def uml3_0_0_Association65(self):
        return self.__uml3_0_0_Association65

    @uml3_0_0_Association65.setter
    def uml3_0_0_Association65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__uml3_0_0_Association65", None)
        self.__uml3_0_0_Association65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Property"):
                    opp_val = getattr(item, "uml3_0_0_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Property"):
                    opp_val = getattr(item, "uml3_0_0_Property", None)
                    
                    setattr(item, "uml3_0_0_Property", self)
                    

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Association__Association", None)
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

class uml3_0_0_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class uml3_0_0_Extend(DirectedRelationship, NamedElement):

    pass
class uml3_0_0_ProfileApplication(DirectedRelationship):

    def __init__(self, isStrict: str, ProfileApplication: "uml3_0_0_Package" = None, uml3_0_0_ProfileApplication: "uml3_0_0_Profile" = None, profileApplication: "uml3_0_0_Package" = None):
        self.isStrict = isStrict
        self.ProfileApplication = ProfileApplication
        self.uml3_0_0_ProfileApplication = uml3_0_0_ProfileApplication
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
        old_value = getattr(self, f"_uml3_0_0_ProfileApplication__profileApplication", None)
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
    def uml3_0_0_ProfileApplication(self):
        return self.__uml3_0_0_ProfileApplication

    @uml3_0_0_ProfileApplication.setter
    def uml3_0_0_ProfileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ProfileApplication__uml3_0_0_ProfileApplication", None)
        self.__uml3_0_0_ProfileApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Profile500"):
                opp_val = getattr(old_value, "uml3_0_0_Profile500", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Profile500", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Profile500"):
                opp_val = getattr(value, "uml3_0_0_Profile500", None)
                setattr(value, "uml3_0_0_Profile500", self)

    @property
    def ProfileApplication(self):
        return self.__ProfileApplication

    @ProfileApplication.setter
    def ProfileApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ProfileApplication__ProfileApplication", None)
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

class uml3_0_0_TemplateBinding(DirectedRelationship):

    pass
class uml3_0_0_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, uml3_0_0_PackageImport: "uml3_0_0_Package" = None, packageImport: "uml3_0_0_Namespace" = None, PackageImport: "uml3_0_0_Namespace" = None, uml3_0_0_PackageImport438: "uml3_0_0_Profile" = None):
        self.visibility = visibility
        self.uml3_0_0_PackageImport = uml3_0_0_PackageImport
        self.packageImport = packageImport
        self.PackageImport = PackageImport
        self.uml3_0_0_PackageImport438 = uml3_0_0_PackageImport438
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def uml3_0_0_PackageImport(self):
        return self.__uml3_0_0_PackageImport

    @uml3_0_0_PackageImport.setter
    def uml3_0_0_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_PackageImport__uml3_0_0_PackageImport", None)
        self.__uml3_0_0_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Package47"):
                opp_val = getattr(old_value, "uml3_0_0_Package47", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Package47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Package47"):
                opp_val = getattr(value, "uml3_0_0_Package47", None)
                setattr(value, "uml3_0_0_Package47", self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_PackageImport__packageImport", None)
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

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_PackageImport__PackageImport", None)
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
    def uml3_0_0_PackageImport438(self):
        return self.__uml3_0_0_PackageImport438

    @uml3_0_0_PackageImport438.setter
    def uml3_0_0_PackageImport438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_PackageImport__uml3_0_0_PackageImport438", None)
        self.__uml3_0_0_PackageImport438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Profile437"):
                opp_val = getattr(old_value, "uml3_0_0_Profile437", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Profile437"):
                opp_val = getattr(value, "uml3_0_0_Profile437", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Profile437", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml3_0_0_Include(DirectedRelationship, NamedElement):

    pass
class uml3_0_0_ProtocolConformance(DirectedRelationship):

    pass
class uml3_0_0_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: str, Generalization: "uml3_0_0_Classifier" = None, generalization: set["uml3_0_0_GeneralizationSet"] = None, generalization134: "uml3_0_0_Classifier" = None, Generalization138: "uml3_0_0_GeneralizationSet" = None, uml3_0_0_Generalization: "uml3_0_0_Classifier" = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.generalization = generalization if generalization is not None else set()
        self.generalization134 = generalization134
        self.Generalization138 = Generalization138
        self.uml3_0_0_Generalization = uml3_0_0_Generalization
        
    @property
    def isSubstitutable(self) -> str:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: str):
        self.__isSubstitutable = isSubstitutable

    @property
    def uml3_0_0_Generalization(self):
        return self.__uml3_0_0_Generalization

    @uml3_0_0_Generalization.setter
    def uml3_0_0_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Generalization__uml3_0_0_Generalization", None)
        self.__uml3_0_0_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Classifier130"):
                opp_val = getattr(old_value, "uml3_0_0_Classifier130", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Classifier130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Classifier130"):
                opp_val = getattr(value, "uml3_0_0_Classifier130", None)
                setattr(value, "uml3_0_0_Classifier130", self)

    @property
    def Generalization138(self):
        return self.__Generalization138

    @Generalization138.setter
    def Generalization138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Generalization__Generalization138", None)
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
        old_value = getattr(self, f"_uml3_0_0_Generalization__Generalization", None)
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

    @property
    def generalization134(self):
        return self.__generalization134

    @generalization134.setter
    def generalization134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Generalization__generalization134", None)
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
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Generalization__generalization", None)
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
                    

class uml3_0_0_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, uml3_0_0_ElementImport: "uml3_0_0_PackageableElement" = None, elementImport: "uml3_0_0_Namespace" = None, ElementImport: "uml3_0_0_Namespace" = None, uml3_0_0_ElementImport435: "uml3_0_0_Profile" = None):
        self.visibility = visibility
        self.alias = alias
        self.uml3_0_0_ElementImport = uml3_0_0_ElementImport
        self.elementImport = elementImport
        self.ElementImport = ElementImport
        self.uml3_0_0_ElementImport435 = uml3_0_0_ElementImport435
        
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
        old_value = getattr(self, f"_uml3_0_0_ElementImport__elementImport", None)
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
    def uml3_0_0_ElementImport(self):
        return self.__uml3_0_0_ElementImport

    @uml3_0_0_ElementImport.setter
    def uml3_0_0_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ElementImport__uml3_0_0_ElementImport", None)
        self.__uml3_0_0_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_PackageableElement43"):
                opp_val = getattr(old_value, "uml3_0_0_PackageableElement43", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_PackageableElement43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_PackageableElement43"):
                opp_val = getattr(value, "uml3_0_0_PackageableElement43", None)
                setattr(value, "uml3_0_0_PackageableElement43", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ElementImport__ElementImport", None)
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
    def uml3_0_0_ElementImport435(self):
        return self.__uml3_0_0_ElementImport435

    @uml3_0_0_ElementImport435.setter
    def uml3_0_0_ElementImport435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_ElementImport__uml3_0_0_ElementImport435", None)
        self.__uml3_0_0_ElementImport435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Profile434"):
                opp_val = getattr(old_value, "uml3_0_0_Profile434", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Profile434"):
                opp_val = getattr(value, "uml3_0_0_Profile434", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Profile434", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml3_0_0_Namespace(NamedElement):

    pass
class EModelElement:

    pass
class uml3_0_0_Element(EModelElement):

    pass
class Element:

    pass
class uml3_0_0_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, ownedMember: "uml3_0_0_Namespace" = None, uml3_0_0_NamedElement: "uml3_0_0_StringExpression" = None, uml3_0_0_NamedElement22: "uml3_0_0_Dependency" = None, NamedElement: "uml3_0_0_Dependency" = None, client: set["uml3_0_0_Dependency"] = None, NamedElement41: "uml3_0_0_Namespace" = None, uml3_0_0_NamedElement36: "uml3_0_0_Namespace" = None, uml3_0_0_NamedElement70: "uml3_0_0_Classifier" = None, uml3_0_0_NamedElement680: "uml3_0_0_Message" = None, uml3_0_0_NamedElement792: "uml3_0_0_ConsiderIgnoreFragment" = None, uml3_0_0_NamedElement884: "uml3_0_0_TimeObservation" = None, uml3_0_0_NamedElement886: "uml3_0_0_DurationObservation" = None, uml3_0_0_NamedElement911: "uml3_0_0_InformationFlow" = None, uml3_0_0_NamedElement914: "uml3_0_0_InformationFlow" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.ownedMember = ownedMember
        self.uml3_0_0_NamedElement = uml3_0_0_NamedElement
        self.uml3_0_0_NamedElement22 = uml3_0_0_NamedElement22
        self.NamedElement = NamedElement
        self.client = client if client is not None else set()
        self.NamedElement41 = NamedElement41
        self.uml3_0_0_NamedElement36 = uml3_0_0_NamedElement36
        self.uml3_0_0_NamedElement70 = uml3_0_0_NamedElement70
        self.uml3_0_0_NamedElement680 = uml3_0_0_NamedElement680
        self.uml3_0_0_NamedElement792 = uml3_0_0_NamedElement792
        self.uml3_0_0_NamedElement884 = uml3_0_0_NamedElement884
        self.uml3_0_0_NamedElement886 = uml3_0_0_NamedElement886
        self.uml3_0_0_NamedElement911 = uml3_0_0_NamedElement911
        self.uml3_0_0_NamedElement914 = uml3_0_0_NamedElement914
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml3_0_0_NamedElement914(self):
        return self.__uml3_0_0_NamedElement914

    @uml3_0_0_NamedElement914.setter
    def uml3_0_0_NamedElement914(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement914", None)
        self.__uml3_0_0_NamedElement914 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InformationFlow913"):
                opp_val = getattr(old_value, "uml3_0_0_InformationFlow913", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InformationFlow913"):
                opp_val = getattr(value, "uml3_0_0_InformationFlow913", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_InformationFlow913", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_NamedElement22(self):
        return self.__uml3_0_0_NamedElement22

    @uml3_0_0_NamedElement22.setter
    def uml3_0_0_NamedElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement22", None)
        self.__uml3_0_0_NamedElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Dependency"):
                opp_val = getattr(old_value, "uml3_0_0_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Dependency"):
                opp_val = getattr(value, "uml3_0_0_Dependency", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_NamedElement792(self):
        return self.__uml3_0_0_NamedElement792

    @uml3_0_0_NamedElement792.setter
    def uml3_0_0_NamedElement792(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement792", None)
        self.__uml3_0_0_NamedElement792 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ConsiderIgnoreFragment"):
                opp_val = getattr(old_value, "uml3_0_0_ConsiderIgnoreFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ConsiderIgnoreFragment"):
                opp_val = getattr(value, "uml3_0_0_ConsiderIgnoreFragment", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ConsiderIgnoreFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_NamedElement(self):
        return self.__uml3_0_0_NamedElement

    @uml3_0_0_NamedElement.setter
    def uml3_0_0_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement", None)
        self.__uml3_0_0_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_StringExpression"):
                opp_val = getattr(old_value, "uml3_0_0_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_StringExpression"):
                opp_val = getattr(value, "uml3_0_0_StringExpression", None)
                setattr(value, "uml3_0_0_StringExpression", self)

    @property
    def uml3_0_0_NamedElement70(self):
        return self.__uml3_0_0_NamedElement70

    @uml3_0_0_NamedElement70.setter
    def uml3_0_0_NamedElement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement70", None)
        self.__uml3_0_0_NamedElement70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Classifier"):
                opp_val = getattr(old_value, "uml3_0_0_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Classifier"):
                opp_val = getattr(value, "uml3_0_0_Classifier", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__ownedMember", None)
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
    def uml3_0_0_NamedElement884(self):
        return self.__uml3_0_0_NamedElement884

    @uml3_0_0_NamedElement884.setter
    def uml3_0_0_NamedElement884(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement884", None)
        self.__uml3_0_0_NamedElement884 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_TimeObservation"):
                opp_val = getattr(old_value, "uml3_0_0_TimeObservation", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_TimeObservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_TimeObservation"):
                opp_val = getattr(value, "uml3_0_0_TimeObservation", None)
                setattr(value, "uml3_0_0_TimeObservation", self)

    @property
    def uml3_0_0_NamedElement36(self):
        return self.__uml3_0_0_NamedElement36

    @uml3_0_0_NamedElement36.setter
    def uml3_0_0_NamedElement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement36", None)
        self.__uml3_0_0_NamedElement36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Namespace"):
                opp_val = getattr(old_value, "uml3_0_0_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Namespace"):
                opp_val = getattr(value, "uml3_0_0_Namespace", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__NamedElement", None)
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
    def uml3_0_0_NamedElement911(self):
        return self.__uml3_0_0_NamedElement911

    @uml3_0_0_NamedElement911.setter
    def uml3_0_0_NamedElement911(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement911", None)
        self.__uml3_0_0_NamedElement911 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InformationFlow910"):
                opp_val = getattr(old_value, "uml3_0_0_InformationFlow910", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InformationFlow910"):
                opp_val = getattr(value, "uml3_0_0_InformationFlow910", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_InformationFlow910", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_NamedElement886(self):
        return self.__uml3_0_0_NamedElement886

    @uml3_0_0_NamedElement886.setter
    def uml3_0_0_NamedElement886(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement886", None)
        self.__uml3_0_0_NamedElement886 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_DurationObservation"):
                opp_val = getattr(old_value, "uml3_0_0_DurationObservation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_DurationObservation"):
                opp_val = getattr(value, "uml3_0_0_DurationObservation", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_DurationObservation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__client", None)
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
    def uml3_0_0_NamedElement680(self):
        return self.__uml3_0_0_NamedElement680

    @uml3_0_0_NamedElement680.setter
    def uml3_0_0_NamedElement680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__uml3_0_0_NamedElement680", None)
        self.__uml3_0_0_NamedElement680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Message679"):
                opp_val = getattr(old_value, "uml3_0_0_Message679", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Message679", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Message679"):
                opp_val = getattr(value, "uml3_0_0_Message679", None)
                setattr(value, "uml3_0_0_Message679", self)

    @property
    def NamedElement41(self):
        return self.__NamedElement41

    @NamedElement41.setter
    def NamedElement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_NamedElement__NamedElement41", None)
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

class uml3_0_0_QualifierValue(Element):

    pass
class uml3_0_0_TemplateSignature(Element):

    pass
class uml3_0_0_Slot(Element):

    pass
class uml3_0_0_ActivityGroup(Element):

    pass
class uml3_0_0_Image(Element):

    def __init__(self, content: str, location: str, format: str, uml3_0_0_Image: "uml3_0_0_Stereotype" = None):
        self.content = content
        self.location = location
        self.format = format
        self.uml3_0_0_Image = uml3_0_0_Image
        
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
    def uml3_0_0_Image(self):
        return self.__uml3_0_0_Image

    @uml3_0_0_Image.setter
    def uml3_0_0_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Image__uml3_0_0_Image", None)
        self.__uml3_0_0_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Stereotype"):
                opp_val = getattr(old_value, "uml3_0_0_Stereotype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Stereotype"):
                opp_val = getattr(value, "uml3_0_0_Stereotype", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Stereotype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml3_0_0_TemplateableElement(Element):

    pass
class uml3_0_0_TemplateParameter(Element):

    pass
class uml3_0_0_Clause(Element):

    pass
class uml3_0_0_ExceptionHandler(Element):

    pass
class uml3_0_0_MultiplicityElement(Element):

    def __init__(self, isOrdered: str, isUnique: str, upper: str, lower: str, uml3_0_0_MultiplicityElement: "uml3_0_0_ValueSpecification" = None, uml3_0_0_MultiplicityElement159: "uml3_0_0_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.uml3_0_0_MultiplicityElement = uml3_0_0_MultiplicityElement
        self.uml3_0_0_MultiplicityElement159 = uml3_0_0_MultiplicityElement159
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def uml3_0_0_MultiplicityElement(self):
        return self.__uml3_0_0_MultiplicityElement

    @uml3_0_0_MultiplicityElement.setter
    def uml3_0_0_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_MultiplicityElement__uml3_0_0_MultiplicityElement", None)
        self.__uml3_0_0_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ValueSpecification157"):
                opp_val = getattr(old_value, "uml3_0_0_ValueSpecification157", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ValueSpecification157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ValueSpecification157"):
                opp_val = getattr(value, "uml3_0_0_ValueSpecification157", None)
                setattr(value, "uml3_0_0_ValueSpecification157", self)

    @property
    def uml3_0_0_MultiplicityElement159(self):
        return self.__uml3_0_0_MultiplicityElement159

    @uml3_0_0_MultiplicityElement159.setter
    def uml3_0_0_MultiplicityElement159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_MultiplicityElement__uml3_0_0_MultiplicityElement159", None)
        self.__uml3_0_0_MultiplicityElement159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ValueSpecification160"):
                opp_val = getattr(old_value, "uml3_0_0_ValueSpecification160", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ValueSpecification160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ValueSpecification160"):
                opp_val = getattr(value, "uml3_0_0_ValueSpecification160", None)
                setattr(value, "uml3_0_0_ValueSpecification160", self)

class uml3_0_0_TemplateParameterSubstitution(Element):

    pass
class uml3_0_0_LinkEndData(Element):

    pass
class uml3_0_0_Relationship(Element):

    pass
class uml3_0_0_ParameterableElement(Element):

    pass
class uml3_0_0_Comment(Element):

    def __init__(self, body: str, uml3_0_0_Comment8: "uml3_0_0_Element" = None, uml3_0_0_Comment: set["uml3_0_0_Element"] = None):
        self.body = body
        self.uml3_0_0_Comment8 = uml3_0_0_Comment8
        self.uml3_0_0_Comment = uml3_0_0_Comment if uml3_0_0_Comment is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def uml3_0_0_Comment(self):
        return self.__uml3_0_0_Comment

    @uml3_0_0_Comment.setter
    def uml3_0_0_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Comment__uml3_0_0_Comment", None)
        self.__uml3_0_0_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Element"):
                    opp_val = getattr(item, "uml3_0_0_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Element"):
                    opp_val = getattr(item, "uml3_0_0_Element", None)
                    
                    setattr(item, "uml3_0_0_Element", self)
                    

    @property
    def uml3_0_0_Comment8(self):
        return self.__uml3_0_0_Comment8

    @uml3_0_0_Comment8.setter
    def uml3_0_0_Comment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Comment__uml3_0_0_Comment8", None)
        self.__uml3_0_0_Comment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Element7"):
                opp_val = getattr(old_value, "uml3_0_0_Element7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Element7"):
                opp_val = getattr(value, "uml3_0_0_Element7", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Element7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml3_0_0_PackageableElement(ParameterableElement, NamedElement):

    pass
class uml3_0_0_PackageMerge(DirectedRelationship):

    pass
class TemplateableElement:

    pass
class uml3_0_0_StringExpression(TemplateableElement, Expression):

    pass
class uml3_0_0_Operation(TemplateableElement, ParameterableElement, BehavioralFeature):

    def __init__(self, isQuery: str, isOrdered: str, isUnique: str, lower: str, upper: str, uml3_0_0_Operation: "uml3_0_0_Parameter" = None, uml3_0_0_Operation210: "uml3_0_0_Artifact" = None, ownedOperation: "uml3_0_0_Interface" = None, ownedOperation219: "uml3_0_0_Class" = None, uml3_0_0_Operation221: set["uml3_0_0_Constraint"] = None, uml3_0_0_Operation224: set["uml3_0_0_Constraint"] = None, ownedOperation230: "uml3_0_0_DataType" = None, uml3_0_0_Operation233: "uml3_0_0_Constraint" = None, uml3_0_0_Operation236: "uml3_0_0_Type" = None, uml3_0_0_Operation228: "uml3_0_0_Operation" = None, uml3_0_0_Operation226: set["uml3_0_0_Operation"] = None, Operation: "uml3_0_0_Class" = None, Operation289: "uml3_0_0_Interface" = None, Operation447: "uml3_0_0_DataType" = None, uml3_0_0_Operation655: "uml3_0_0_CallOperationAction" = None, uml3_0_0_Operation747: "uml3_0_0_SendOperationEvent" = None, uml3_0_0_Operation753: "uml3_0_0_ReceiveOperationEvent" = None, uml3_0_0_Operation757: "uml3_0_0_CallEvent" = None, uml3_0_0_Operation1054: "uml3_0_0_ProtocolTransition" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.uml3_0_0_Operation = uml3_0_0_Operation
        self.uml3_0_0_Operation210 = uml3_0_0_Operation210
        self.ownedOperation = ownedOperation
        self.ownedOperation219 = ownedOperation219
        self.uml3_0_0_Operation221 = uml3_0_0_Operation221 if uml3_0_0_Operation221 is not None else set()
        self.uml3_0_0_Operation224 = uml3_0_0_Operation224 if uml3_0_0_Operation224 is not None else set()
        self.ownedOperation230 = ownedOperation230
        self.uml3_0_0_Operation233 = uml3_0_0_Operation233
        self.uml3_0_0_Operation236 = uml3_0_0_Operation236
        self.uml3_0_0_Operation228 = uml3_0_0_Operation228
        self.uml3_0_0_Operation226 = uml3_0_0_Operation226 if uml3_0_0_Operation226 is not None else set()
        self.Operation = Operation
        self.Operation289 = Operation289
        self.Operation447 = Operation447
        self.uml3_0_0_Operation655 = uml3_0_0_Operation655
        self.uml3_0_0_Operation747 = uml3_0_0_Operation747
        self.uml3_0_0_Operation753 = uml3_0_0_Operation753
        self.uml3_0_0_Operation757 = uml3_0_0_Operation757
        self.uml3_0_0_Operation1054 = uml3_0_0_Operation1054
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

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
    def ownedOperation219(self):
        return self.__ownedOperation219

    @ownedOperation219.setter
    def ownedOperation219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__ownedOperation219", None)
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
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__ownedOperation", None)
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
    def uml3_0_0_Operation(self):
        return self.__uml3_0_0_Operation

    @uml3_0_0_Operation.setter
    def uml3_0_0_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation", None)
        self.__uml3_0_0_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Parameter152"):
                opp_val = getattr(old_value, "uml3_0_0_Parameter152", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Parameter152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Parameter152"):
                opp_val = getattr(value, "uml3_0_0_Parameter152", None)
                setattr(value, "uml3_0_0_Parameter152", self)

    @property
    def uml3_0_0_Operation757(self):
        return self.__uml3_0_0_Operation757

    @uml3_0_0_Operation757.setter
    def uml3_0_0_Operation757(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation757", None)
        self.__uml3_0_0_Operation757 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_CallEvent"):
                opp_val = getattr(old_value, "uml3_0_0_CallEvent", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_CallEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_CallEvent"):
                opp_val = getattr(value, "uml3_0_0_CallEvent", None)
                setattr(value, "uml3_0_0_CallEvent", self)

    @property
    def uml3_0_0_Operation228(self):
        return self.__uml3_0_0_Operation228

    @uml3_0_0_Operation228.setter
    def uml3_0_0_Operation228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation228", None)
        self.__uml3_0_0_Operation228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Operation226"):
                opp_val = getattr(old_value, "uml3_0_0_Operation226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Operation226"):
                opp_val = getattr(value, "uml3_0_0_Operation226", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Operation226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Operation210(self):
        return self.__uml3_0_0_Operation210

    @uml3_0_0_Operation210.setter
    def uml3_0_0_Operation210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation210", None)
        self.__uml3_0_0_Operation210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Artifact209"):
                opp_val = getattr(old_value, "uml3_0_0_Artifact209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Artifact209"):
                opp_val = getattr(value, "uml3_0_0_Artifact209", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Artifact209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Operation753(self):
        return self.__uml3_0_0_Operation753

    @uml3_0_0_Operation753.setter
    def uml3_0_0_Operation753(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation753", None)
        self.__uml3_0_0_Operation753 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReceiveOperationEvent"):
                opp_val = getattr(old_value, "uml3_0_0_ReceiveOperationEvent", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ReceiveOperationEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReceiveOperationEvent"):
                opp_val = getattr(value, "uml3_0_0_ReceiveOperationEvent", None)
                setattr(value, "uml3_0_0_ReceiveOperationEvent", self)

    @property
    def uml3_0_0_Operation221(self):
        return self.__uml3_0_0_Operation221

    @uml3_0_0_Operation221.setter
    def uml3_0_0_Operation221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation221", None)
        self.__uml3_0_0_Operation221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Constraint222"):
                    opp_val = getattr(item, "uml3_0_0_Constraint222", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Constraint222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Constraint222"):
                    opp_val = getattr(item, "uml3_0_0_Constraint222", None)
                    
                    setattr(item, "uml3_0_0_Constraint222", self)
                    

    @property
    def uml3_0_0_Operation747(self):
        return self.__uml3_0_0_Operation747

    @uml3_0_0_Operation747.setter
    def uml3_0_0_Operation747(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation747", None)
        self.__uml3_0_0_Operation747 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_SendOperationEvent"):
                opp_val = getattr(old_value, "uml3_0_0_SendOperationEvent", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_SendOperationEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_SendOperationEvent"):
                opp_val = getattr(value, "uml3_0_0_SendOperationEvent", None)
                setattr(value, "uml3_0_0_SendOperationEvent", self)

    @property
    def uml3_0_0_Operation655(self):
        return self.__uml3_0_0_Operation655

    @uml3_0_0_Operation655.setter
    def uml3_0_0_Operation655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation655", None)
        self.__uml3_0_0_Operation655 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_CallOperationAction"):
                opp_val = getattr(old_value, "uml3_0_0_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_CallOperationAction"):
                opp_val = getattr(value, "uml3_0_0_CallOperationAction", None)
                setattr(value, "uml3_0_0_CallOperationAction", self)

    @property
    def Operation289(self):
        return self.__Operation289

    @Operation289.setter
    def Operation289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__Operation289", None)
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
    def Operation447(self):
        return self.__Operation447

    @Operation447.setter
    def Operation447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__Operation447", None)
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
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__Operation", None)
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
    def uml3_0_0_Operation1054(self):
        return self.__uml3_0_0_Operation1054

    @uml3_0_0_Operation1054.setter
    def uml3_0_0_Operation1054(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation1054", None)
        self.__uml3_0_0_Operation1054 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ProtocolTransition1053"):
                opp_val = getattr(old_value, "uml3_0_0_ProtocolTransition1053", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ProtocolTransition1053"):
                opp_val = getattr(value, "uml3_0_0_ProtocolTransition1053", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ProtocolTransition1053", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Operation224(self):
        return self.__uml3_0_0_Operation224

    @uml3_0_0_Operation224.setter
    def uml3_0_0_Operation224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation224", None)
        self.__uml3_0_0_Operation224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Constraint225"):
                    opp_val = getattr(item, "uml3_0_0_Constraint225", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Constraint225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Constraint225"):
                    opp_val = getattr(item, "uml3_0_0_Constraint225", None)
                    
                    setattr(item, "uml3_0_0_Constraint225", self)
                    

    @property
    def uml3_0_0_Operation236(self):
        return self.__uml3_0_0_Operation236

    @uml3_0_0_Operation236.setter
    def uml3_0_0_Operation236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation236", None)
        self.__uml3_0_0_Operation236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Type237"):
                opp_val = getattr(old_value, "uml3_0_0_Type237", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Type237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Type237"):
                opp_val = getattr(value, "uml3_0_0_Type237", None)
                setattr(value, "uml3_0_0_Type237", self)

    @property
    def uml3_0_0_Operation226(self):
        return self.__uml3_0_0_Operation226

    @uml3_0_0_Operation226.setter
    def uml3_0_0_Operation226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation226", None)
        self.__uml3_0_0_Operation226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Operation228"):
                    opp_val = getattr(item, "uml3_0_0_Operation228", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Operation228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Operation228"):
                    opp_val = getattr(item, "uml3_0_0_Operation228", None)
                    
                    setattr(item, "uml3_0_0_Operation228", self)
                    

    @property
    def ownedOperation230(self):
        return self.__ownedOperation230

    @ownedOperation230.setter
    def ownedOperation230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__ownedOperation230", None)
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
    def uml3_0_0_Operation233(self):
        return self.__uml3_0_0_Operation233

    @uml3_0_0_Operation233.setter
    def uml3_0_0_Operation233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Operation__uml3_0_0_Operation233", None)
        self.__uml3_0_0_Operation233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Constraint234"):
                opp_val = getattr(old_value, "uml3_0_0_Constraint234", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Constraint234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Constraint234"):
                opp_val = getattr(value, "uml3_0_0_Constraint234", None)
                setattr(value, "uml3_0_0_Constraint234", self)

class PackageableElement:

    pass
class uml3_0_0_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: str, isDisjoint: str, GeneralizationSet: "uml3_0_0_Classifier" = None, powertypeExtent: "uml3_0_0_Classifier" = None, generalizationSet: set["uml3_0_0_Generalization"] = None, GeneralizationSet132: "uml3_0_0_Generalization" = None):
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
    def GeneralizationSet132(self):
        return self.__GeneralizationSet132

    @GeneralizationSet132.setter
    def GeneralizationSet132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_GeneralizationSet__GeneralizationSet132", None)
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
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_GeneralizationSet__powertypeExtent", None)
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

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_GeneralizationSet__generalizationSet", None)
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
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_GeneralizationSet__GeneralizationSet", None)
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

class uml3_0_0_Observation(PackageableElement):

    pass
class uml3_0_0_InstanceSpecification(DeployedArtifact, DeploymentTarget, PackageableElement):

    pass
class uml3_0_0_Constraint(PackageableElement):

    pass
class uml3_0_0_Event(PackageableElement):

    pass
class uml3_0_0_InformationFlow(DirectedRelationship, PackageableElement):

    pass
class uml3_0_0_Type(PackageableElement):

    pass
class uml3_0_0_Dependency(DirectedRelationship, PackageableElement):

    pass
class uml3_0_0_ValueSpecification(TypedElement, PackageableElement):

    pass
class Namespace:

    pass
class uml3_0_0_Region(RedefinableElement, Namespace):

    pass
class uml3_0_0_Transition(RedefinableElement, Namespace):

    def __init__(self, kind: str, Transition: "uml3_0_0_Region" = None, uml3_0_0_Transition: "uml3_0_0_Vertex" = None, uml3_0_0_Transition325: "uml3_0_0_Vertex" = None, transition: "uml3_0_0_Region" = None, uml3_0_0_Transition331: "uml3_0_0_Vertex" = None, uml3_0_0_Transition334: "uml3_0_0_Vertex" = None, uml3_0_0_Transition340: "uml3_0_0_Constraint" = None, uml3_0_0_Transition343: "uml3_0_0_Behavior" = None, uml3_0_0_Transition346: set["uml3_0_0_Trigger"] = None, uml3_0_0_Transition338: "uml3_0_0_Transition" = None, uml3_0_0_Transition336: "uml3_0_0_Transition" = None):
        self.kind = kind
        self.Transition = Transition
        self.uml3_0_0_Transition = uml3_0_0_Transition
        self.uml3_0_0_Transition325 = uml3_0_0_Transition325
        self.transition = transition
        self.uml3_0_0_Transition331 = uml3_0_0_Transition331
        self.uml3_0_0_Transition334 = uml3_0_0_Transition334
        self.uml3_0_0_Transition340 = uml3_0_0_Transition340
        self.uml3_0_0_Transition343 = uml3_0_0_Transition343
        self.uml3_0_0_Transition346 = uml3_0_0_Transition346 if uml3_0_0_Transition346 is not None else set()
        self.uml3_0_0_Transition338 = uml3_0_0_Transition338
        self.uml3_0_0_Transition336 = uml3_0_0_Transition336
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def uml3_0_0_Transition331(self):
        return self.__uml3_0_0_Transition331

    @uml3_0_0_Transition331.setter
    def uml3_0_0_Transition331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition331", None)
        self.__uml3_0_0_Transition331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Vertex332"):
                opp_val = getattr(old_value, "uml3_0_0_Vertex332", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Vertex332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Vertex332"):
                opp_val = getattr(value, "uml3_0_0_Vertex332", None)
                setattr(value, "uml3_0_0_Vertex332", self)

    @property
    def uml3_0_0_Transition334(self):
        return self.__uml3_0_0_Transition334

    @uml3_0_0_Transition334.setter
    def uml3_0_0_Transition334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition334", None)
        self.__uml3_0_0_Transition334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Vertex335"):
                opp_val = getattr(old_value, "uml3_0_0_Vertex335", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Vertex335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Vertex335"):
                opp_val = getattr(value, "uml3_0_0_Vertex335", None)
                setattr(value, "uml3_0_0_Vertex335", self)

    @property
    def uml3_0_0_Transition340(self):
        return self.__uml3_0_0_Transition340

    @uml3_0_0_Transition340.setter
    def uml3_0_0_Transition340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition340", None)
        self.__uml3_0_0_Transition340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Constraint341"):
                opp_val = getattr(old_value, "uml3_0_0_Constraint341", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Constraint341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Constraint341"):
                opp_val = getattr(value, "uml3_0_0_Constraint341", None)
                setattr(value, "uml3_0_0_Constraint341", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__Transition", None)
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
    def uml3_0_0_Transition325(self):
        return self.__uml3_0_0_Transition325

    @uml3_0_0_Transition325.setter
    def uml3_0_0_Transition325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition325", None)
        self.__uml3_0_0_Transition325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Vertex324"):
                opp_val = getattr(old_value, "uml3_0_0_Vertex324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Vertex324"):
                opp_val = getattr(value, "uml3_0_0_Vertex324", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Vertex324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Transition(self):
        return self.__uml3_0_0_Transition

    @uml3_0_0_Transition.setter
    def uml3_0_0_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition", None)
        self.__uml3_0_0_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Vertex"):
                opp_val = getattr(old_value, "uml3_0_0_Vertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Vertex"):
                opp_val = getattr(value, "uml3_0_0_Vertex", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Vertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__transition", None)
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
    def uml3_0_0_Transition343(self):
        return self.__uml3_0_0_Transition343

    @uml3_0_0_Transition343.setter
    def uml3_0_0_Transition343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition343", None)
        self.__uml3_0_0_Transition343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior344"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior344", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior344"):
                opp_val = getattr(value, "uml3_0_0_Behavior344", None)
                setattr(value, "uml3_0_0_Behavior344", self)

    @property
    def uml3_0_0_Transition336(self):
        return self.__uml3_0_0_Transition336

    @uml3_0_0_Transition336.setter
    def uml3_0_0_Transition336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition336", None)
        self.__uml3_0_0_Transition336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Transition338"):
                opp_val = getattr(old_value, "uml3_0_0_Transition338", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Transition338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Transition338"):
                opp_val = getattr(value, "uml3_0_0_Transition338", None)
                setattr(value, "uml3_0_0_Transition338", self)

    @property
    def uml3_0_0_Transition346(self):
        return self.__uml3_0_0_Transition346

    @uml3_0_0_Transition346.setter
    def uml3_0_0_Transition346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition346", None)
        self.__uml3_0_0_Transition346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Trigger347"):
                    opp_val = getattr(item, "uml3_0_0_Trigger347", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Trigger347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Trigger347"):
                    opp_val = getattr(item, "uml3_0_0_Trigger347", None)
                    
                    setattr(item, "uml3_0_0_Trigger347", self)
                    

    @property
    def uml3_0_0_Transition338(self):
        return self.__uml3_0_0_Transition338

    @uml3_0_0_Transition338.setter
    def uml3_0_0_Transition338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Transition__uml3_0_0_Transition338", None)
        self.__uml3_0_0_Transition338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Transition336"):
                opp_val = getattr(old_value, "uml3_0_0_Transition336", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Transition336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Transition336"):
                opp_val = getattr(value, "uml3_0_0_Transition336", None)
                setattr(value, "uml3_0_0_Transition336", self)

class uml3_0_0_InteractionOperand(InteractionFragment, Namespace):

    pass
class uml3_0_0_StructuredActivityNode(ActivityGroup, Action, Namespace):

    def __init__(self, mustIsolate: str, scope: set["uml3_0_0_Variable"] = None, inStructuredNode: set["uml3_0_0_ActivityEdge"] = None, inStructuredNode553: set["uml3_0_0_ActivityNode"] = None, StructuredActivityNode: "uml3_0_0_ActivityNode" = None, uml3_0_0_StructuredActivityNode: "uml3_0_0_Activity" = None, StructuredActivityNode580: "uml3_0_0_Variable" = None, StructuredActivityNode602: "uml3_0_0_ActivityEdge" = None):
        self.mustIsolate = mustIsolate
        self.scope = scope if scope is not None else set()
        self.inStructuredNode = inStructuredNode if inStructuredNode is not None else set()
        self.inStructuredNode553 = inStructuredNode553 if inStructuredNode553 is not None else set()
        self.StructuredActivityNode = StructuredActivityNode
        self.uml3_0_0_StructuredActivityNode = uml3_0_0_StructuredActivityNode
        self.StructuredActivityNode580 = StructuredActivityNode580
        self.StructuredActivityNode602 = StructuredActivityNode602
        
    @property
    def mustIsolate(self) -> str:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: str):
        self.__mustIsolate = mustIsolate

    @property
    def inStructuredNode(self):
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuredActivityNode__inStructuredNode", None)
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
    def inStructuredNode553(self):
        return self.__inStructuredNode553

    @inStructuredNode553.setter
    def inStructuredNode553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuredActivityNode__inStructuredNode553", None)
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
    def StructuredActivityNode602(self):
        return self.__StructuredActivityNode602

    @StructuredActivityNode602.setter
    def StructuredActivityNode602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuredActivityNode__StructuredActivityNode602", None)
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
    def StructuredActivityNode(self):
        return self.__StructuredActivityNode

    @StructuredActivityNode.setter
    def StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuredActivityNode__StructuredActivityNode", None)
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
        old_value = getattr(self, f"_uml3_0_0_StructuredActivityNode__StructuredActivityNode580", None)
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
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuredActivityNode__scope", None)
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
                    

    @property
    def uml3_0_0_StructuredActivityNode(self):
        return self.__uml3_0_0_StructuredActivityNode

    @uml3_0_0_StructuredActivityNode.setter
    def uml3_0_0_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_StructuredActivityNode__uml3_0_0_StructuredActivityNode", None)
        self.__uml3_0_0_StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Activity"):
                opp_val = getattr(old_value, "uml3_0_0_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Activity"):
                opp_val = getattr(value, "uml3_0_0_Activity", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml3_0_0_Classifier(TemplateableElement, Type, RedefinableElement, Namespace):

    def __init__(self, isAbstract: str, specific: set["uml3_0_0_Generalization"] = None, powertype: set["uml3_0_0_GeneralizationSet"] = None, featuringClassifier: set["uml3_0_0_Feature"] = None, uml3_0_0_Classifier82: "uml3_0_0_CollaborationUse" = None, uml3_0_0_Classifier84: set["uml3_0_0_CollaborationUse"] = None, uml3_0_0_Classifier87: set["uml3_0_0_UseCase"] = None, subject: set["uml3_0_0_UseCase"] = None, uml3_0_0_Classifier93: "uml3_0_0_RedefinableElement" = None, uml3_0_0_Classifier: set["uml3_0_0_NamedElement"] = None, uml3_0_0_Classifier73: "uml3_0_0_Classifier" = None, uml3_0_0_Classifier71: set["uml3_0_0_Classifier"] = None, uml3_0_0_Classifier76: "uml3_0_0_Classifier" = None, uml3_0_0_Classifier74: set["uml3_0_0_Classifier"] = None, substitutingClassifier: set["uml3_0_0_Substitution"] = None, uml3_0_0_Classifier79: set["uml3_0_0_Property"] = None, Classifier: "uml3_0_0_Generalization" = None, Classifier136: "uml3_0_0_GeneralizationSet" = None, Classifier140: "uml3_0_0_Feature" = None, uml3_0_0_Classifier142: "uml3_0_0_Substitution" = None, Classifier144: "uml3_0_0_Substitution" = None, uml3_0_0_Classifier130: "uml3_0_0_Generalization" = None, uml3_0_0_Classifier266: "uml3_0_0_Class" = None, uml3_0_0_Classifier292: "uml3_0_0_Interface" = None, Classifier462: "uml3_0_0_UseCase" = None, uml3_0_0_Classifier485: "uml3_0_0_RedefinableTemplateSignature" = None, uml3_0_0_Classifier487: "uml3_0_0_ClassifierTemplateParameter" = None, uml3_0_0_Classifier506: "uml3_0_0_InstanceSpecification" = None, uml3_0_0_Classifier528: "uml3_0_0_Action" = None, uml3_0_0_Classifier631: "uml3_0_0_ExceptionHandler" = None, uml3_0_0_Classifier774: "uml3_0_0_ComponentRealization" = None, uml3_0_0_Classifier794: "uml3_0_0_CreateObjectAction" = None, uml3_0_0_Classifier903: "uml3_0_0_InformationItem" = None, uml3_0_0_Classifier908: "uml3_0_0_InformationFlow" = None, uml3_0_0_Classifier928: "uml3_0_0_ReadExtentAction" = None, uml3_0_0_Classifier930: "uml3_0_0_ReclassifyObjectAction" = None, uml3_0_0_Classifier938: "uml3_0_0_ReadIsClassifiedObjectAction" = None, uml3_0_0_Classifier933: "uml3_0_0_ReclassifyObjectAction" = None, uml3_0_0_Classifier984: "uml3_0_0_UnmarshallAction" = None):
        self.isAbstract = isAbstract
        self.specific = specific if specific is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.uml3_0_0_Classifier82 = uml3_0_0_Classifier82
        self.uml3_0_0_Classifier84 = uml3_0_0_Classifier84 if uml3_0_0_Classifier84 is not None else set()
        self.uml3_0_0_Classifier87 = uml3_0_0_Classifier87 if uml3_0_0_Classifier87 is not None else set()
        self.subject = subject if subject is not None else set()
        self.uml3_0_0_Classifier93 = uml3_0_0_Classifier93
        self.uml3_0_0_Classifier = uml3_0_0_Classifier if uml3_0_0_Classifier is not None else set()
        self.uml3_0_0_Classifier73 = uml3_0_0_Classifier73
        self.uml3_0_0_Classifier71 = uml3_0_0_Classifier71 if uml3_0_0_Classifier71 is not None else set()
        self.uml3_0_0_Classifier76 = uml3_0_0_Classifier76
        self.uml3_0_0_Classifier74 = uml3_0_0_Classifier74 if uml3_0_0_Classifier74 is not None else set()
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        self.uml3_0_0_Classifier79 = uml3_0_0_Classifier79 if uml3_0_0_Classifier79 is not None else set()
        self.Classifier = Classifier
        self.Classifier136 = Classifier136
        self.Classifier140 = Classifier140
        self.uml3_0_0_Classifier142 = uml3_0_0_Classifier142
        self.Classifier144 = Classifier144
        self.uml3_0_0_Classifier130 = uml3_0_0_Classifier130
        self.uml3_0_0_Classifier266 = uml3_0_0_Classifier266
        self.uml3_0_0_Classifier292 = uml3_0_0_Classifier292
        self.Classifier462 = Classifier462
        self.uml3_0_0_Classifier485 = uml3_0_0_Classifier485
        self.uml3_0_0_Classifier487 = uml3_0_0_Classifier487
        self.uml3_0_0_Classifier506 = uml3_0_0_Classifier506
        self.uml3_0_0_Classifier528 = uml3_0_0_Classifier528
        self.uml3_0_0_Classifier631 = uml3_0_0_Classifier631
        self.uml3_0_0_Classifier774 = uml3_0_0_Classifier774
        self.uml3_0_0_Classifier794 = uml3_0_0_Classifier794
        self.uml3_0_0_Classifier903 = uml3_0_0_Classifier903
        self.uml3_0_0_Classifier908 = uml3_0_0_Classifier908
        self.uml3_0_0_Classifier928 = uml3_0_0_Classifier928
        self.uml3_0_0_Classifier930 = uml3_0_0_Classifier930
        self.uml3_0_0_Classifier938 = uml3_0_0_Classifier938
        self.uml3_0_0_Classifier933 = uml3_0_0_Classifier933
        self.uml3_0_0_Classifier984 = uml3_0_0_Classifier984
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def uml3_0_0_Classifier(self):
        return self.__uml3_0_0_Classifier

    @uml3_0_0_Classifier.setter
    def uml3_0_0_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier", None)
        self.__uml3_0_0_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_NamedElement70"):
                    opp_val = getattr(item, "uml3_0_0_NamedElement70", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_NamedElement70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_NamedElement70"):
                    opp_val = getattr(item, "uml3_0_0_NamedElement70", None)
                    
                    setattr(item, "uml3_0_0_NamedElement70", self)
                    

    @property
    def uml3_0_0_Classifier79(self):
        return self.__uml3_0_0_Classifier79

    @uml3_0_0_Classifier79.setter
    def uml3_0_0_Classifier79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier79", None)
        self.__uml3_0_0_Classifier79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Property80"):
                    opp_val = getattr(item, "uml3_0_0_Property80", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Property80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Property80"):
                    opp_val = getattr(item, "uml3_0_0_Property80", None)
                    
                    setattr(item, "uml3_0_0_Property80", self)
                    

    @property
    def uml3_0_0_Classifier933(self):
        return self.__uml3_0_0_Classifier933

    @uml3_0_0_Classifier933.setter
    def uml3_0_0_Classifier933(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier933", None)
        self.__uml3_0_0_Classifier933 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReclassifyObjectAction932"):
                opp_val = getattr(old_value, "uml3_0_0_ReclassifyObjectAction932", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReclassifyObjectAction932"):
                opp_val = getattr(value, "uml3_0_0_ReclassifyObjectAction932", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ReclassifyObjectAction932", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier84(self):
        return self.__uml3_0_0_Classifier84

    @uml3_0_0_Classifier84.setter
    def uml3_0_0_Classifier84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier84", None)
        self.__uml3_0_0_Classifier84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_CollaborationUse85"):
                    opp_val = getattr(item, "uml3_0_0_CollaborationUse85", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_CollaborationUse85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_CollaborationUse85"):
                    opp_val = getattr(item, "uml3_0_0_CollaborationUse85", None)
                    
                    setattr(item, "uml3_0_0_CollaborationUse85", self)
                    

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__featuringClassifier", None)
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
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__Classifier", None)
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
    def uml3_0_0_Classifier130(self):
        return self.__uml3_0_0_Classifier130

    @uml3_0_0_Classifier130.setter
    def uml3_0_0_Classifier130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier130", None)
        self.__uml3_0_0_Classifier130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Generalization"):
                opp_val = getattr(old_value, "uml3_0_0_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Generalization"):
                opp_val = getattr(value, "uml3_0_0_Generalization", None)
                setattr(value, "uml3_0_0_Generalization", self)

    @property
    def uml3_0_0_Classifier903(self):
        return self.__uml3_0_0_Classifier903

    @uml3_0_0_Classifier903.setter
    def uml3_0_0_Classifier903(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier903", None)
        self.__uml3_0_0_Classifier903 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InformationItem"):
                opp_val = getattr(old_value, "uml3_0_0_InformationItem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InformationItem"):
                opp_val = getattr(value, "uml3_0_0_InformationItem", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_InformationItem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier82(self):
        return self.__uml3_0_0_Classifier82

    @uml3_0_0_Classifier82.setter
    def uml3_0_0_Classifier82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier82", None)
        self.__uml3_0_0_Classifier82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_CollaborationUse"):
                opp_val = getattr(old_value, "uml3_0_0_CollaborationUse", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_CollaborationUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_CollaborationUse"):
                opp_val = getattr(value, "uml3_0_0_CollaborationUse", None)
                setattr(value, "uml3_0_0_CollaborationUse", self)

    @property
    def uml3_0_0_Classifier87(self):
        return self.__uml3_0_0_Classifier87

    @uml3_0_0_Classifier87.setter
    def uml3_0_0_Classifier87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier87", None)
        self.__uml3_0_0_Classifier87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_UseCase"):
                    opp_val = getattr(item, "uml3_0_0_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_UseCase"):
                    opp_val = getattr(item, "uml3_0_0_UseCase", None)
                    
                    setattr(item, "uml3_0_0_UseCase", self)
                    

    @property
    def uml3_0_0_Classifier74(self):
        return self.__uml3_0_0_Classifier74

    @uml3_0_0_Classifier74.setter
    def uml3_0_0_Classifier74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier74", None)
        self.__uml3_0_0_Classifier74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Classifier76"):
                    opp_val = getattr(item, "uml3_0_0_Classifier76", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Classifier76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Classifier76"):
                    opp_val = getattr(item, "uml3_0_0_Classifier76", None)
                    
                    setattr(item, "uml3_0_0_Classifier76", self)
                    

    @property
    def uml3_0_0_Classifier930(self):
        return self.__uml3_0_0_Classifier930

    @uml3_0_0_Classifier930.setter
    def uml3_0_0_Classifier930(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier930", None)
        self.__uml3_0_0_Classifier930 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReclassifyObjectAction"):
                opp_val = getattr(old_value, "uml3_0_0_ReclassifyObjectAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReclassifyObjectAction"):
                opp_val = getattr(value, "uml3_0_0_ReclassifyObjectAction", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ReclassifyObjectAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier144(self):
        return self.__Classifier144

    @Classifier144.setter
    def Classifier144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__Classifier144", None)
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

    @property
    def uml3_0_0_Classifier485(self):
        return self.__uml3_0_0_Classifier485

    @uml3_0_0_Classifier485.setter
    def uml3_0_0_Classifier485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier485", None)
        self.__uml3_0_0_Classifier485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_RedefinableTemplateSignature484"):
                opp_val = getattr(old_value, "uml3_0_0_RedefinableTemplateSignature484", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_RedefinableTemplateSignature484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_RedefinableTemplateSignature484"):
                opp_val = getattr(value, "uml3_0_0_RedefinableTemplateSignature484", None)
                setattr(value, "uml3_0_0_RedefinableTemplateSignature484", self)

    @property
    def uml3_0_0_Classifier506(self):
        return self.__uml3_0_0_Classifier506

    @uml3_0_0_Classifier506.setter
    def uml3_0_0_Classifier506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier506", None)
        self.__uml3_0_0_Classifier506 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InstanceSpecification"):
                opp_val = getattr(old_value, "uml3_0_0_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InstanceSpecification"):
                opp_val = getattr(value, "uml3_0_0_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier76(self):
        return self.__uml3_0_0_Classifier76

    @uml3_0_0_Classifier76.setter
    def uml3_0_0_Classifier76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier76", None)
        self.__uml3_0_0_Classifier76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Classifier74"):
                opp_val = getattr(old_value, "uml3_0_0_Classifier74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Classifier74"):
                opp_val = getattr(value, "uml3_0_0_Classifier74", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Classifier74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__subject", None)
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
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__powertype", None)
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
    def uml3_0_0_Classifier774(self):
        return self.__uml3_0_0_Classifier774

    @uml3_0_0_Classifier774.setter
    def uml3_0_0_Classifier774(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier774", None)
        self.__uml3_0_0_Classifier774 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ComponentRealization"):
                opp_val = getattr(old_value, "uml3_0_0_ComponentRealization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ComponentRealization"):
                opp_val = getattr(value, "uml3_0_0_ComponentRealization", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ComponentRealization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier93(self):
        return self.__uml3_0_0_Classifier93

    @uml3_0_0_Classifier93.setter
    def uml3_0_0_Classifier93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier93", None)
        self.__uml3_0_0_Classifier93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_RedefinableElement92"):
                opp_val = getattr(old_value, "uml3_0_0_RedefinableElement92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_RedefinableElement92"):
                opp_val = getattr(value, "uml3_0_0_RedefinableElement92", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_RedefinableElement92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier908(self):
        return self.__uml3_0_0_Classifier908

    @uml3_0_0_Classifier908.setter
    def uml3_0_0_Classifier908(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier908", None)
        self.__uml3_0_0_Classifier908 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_InformationFlow907"):
                opp_val = getattr(old_value, "uml3_0_0_InformationFlow907", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_InformationFlow907"):
                opp_val = getattr(value, "uml3_0_0_InformationFlow907", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_InformationFlow907", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__specific", None)
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
    def uml3_0_0_Classifier142(self):
        return self.__uml3_0_0_Classifier142

    @uml3_0_0_Classifier142.setter
    def uml3_0_0_Classifier142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier142", None)
        self.__uml3_0_0_Classifier142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Substitution"):
                opp_val = getattr(old_value, "uml3_0_0_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Substitution"):
                opp_val = getattr(value, "uml3_0_0_Substitution", None)
                setattr(value, "uml3_0_0_Substitution", self)

    @property
    def Classifier140(self):
        return self.__Classifier140

    @Classifier140.setter
    def Classifier140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__Classifier140", None)
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
    def uml3_0_0_Classifier73(self):
        return self.__uml3_0_0_Classifier73

    @uml3_0_0_Classifier73.setter
    def uml3_0_0_Classifier73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier73", None)
        self.__uml3_0_0_Classifier73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Classifier71"):
                opp_val = getattr(old_value, "uml3_0_0_Classifier71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Classifier71"):
                opp_val = getattr(value, "uml3_0_0_Classifier71", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Classifier71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier631(self):
        return self.__uml3_0_0_Classifier631

    @uml3_0_0_Classifier631.setter
    def uml3_0_0_Classifier631(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier631", None)
        self.__uml3_0_0_Classifier631 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ExceptionHandler630"):
                opp_val = getattr(old_value, "uml3_0_0_ExceptionHandler630", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ExceptionHandler630"):
                opp_val = getattr(value, "uml3_0_0_ExceptionHandler630", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ExceptionHandler630", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier984(self):
        return self.__uml3_0_0_Classifier984

    @uml3_0_0_Classifier984.setter
    def uml3_0_0_Classifier984(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier984", None)
        self.__uml3_0_0_Classifier984 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_UnmarshallAction983"):
                opp_val = getattr(old_value, "uml3_0_0_UnmarshallAction983", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_UnmarshallAction983", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_UnmarshallAction983"):
                opp_val = getattr(value, "uml3_0_0_UnmarshallAction983", None)
                setattr(value, "uml3_0_0_UnmarshallAction983", self)

    @property
    def Classifier462(self):
        return self.__Classifier462

    @Classifier462.setter
    def Classifier462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__Classifier462", None)
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
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__substitutingClassifier", None)
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
    def uml3_0_0_Classifier292(self):
        return self.__uml3_0_0_Classifier292

    @uml3_0_0_Classifier292.setter
    def uml3_0_0_Classifier292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier292", None)
        self.__uml3_0_0_Classifier292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Interface291"):
                opp_val = getattr(old_value, "uml3_0_0_Interface291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Interface291"):
                opp_val = getattr(value, "uml3_0_0_Interface291", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Interface291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier794(self):
        return self.__uml3_0_0_Classifier794

    @uml3_0_0_Classifier794.setter
    def uml3_0_0_Classifier794(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier794", None)
        self.__uml3_0_0_Classifier794 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_CreateObjectAction"):
                opp_val = getattr(old_value, "uml3_0_0_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_CreateObjectAction"):
                opp_val = getattr(value, "uml3_0_0_CreateObjectAction", None)
                setattr(value, "uml3_0_0_CreateObjectAction", self)

    @property
    def Classifier136(self):
        return self.__Classifier136

    @Classifier136.setter
    def Classifier136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__Classifier136", None)
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
    def uml3_0_0_Classifier71(self):
        return self.__uml3_0_0_Classifier71

    @uml3_0_0_Classifier71.setter
    def uml3_0_0_Classifier71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier71", None)
        self.__uml3_0_0_Classifier71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Classifier73"):
                    opp_val = getattr(item, "uml3_0_0_Classifier73", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Classifier73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Classifier73"):
                    opp_val = getattr(item, "uml3_0_0_Classifier73", None)
                    
                    setattr(item, "uml3_0_0_Classifier73", self)
                    

    @property
    def uml3_0_0_Classifier266(self):
        return self.__uml3_0_0_Classifier266

    @uml3_0_0_Classifier266.setter
    def uml3_0_0_Classifier266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier266", None)
        self.__uml3_0_0_Classifier266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Class265"):
                opp_val = getattr(old_value, "uml3_0_0_Class265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Class265"):
                opp_val = getattr(value, "uml3_0_0_Class265", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_Class265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml3_0_0_Classifier528(self):
        return self.__uml3_0_0_Classifier528

    @uml3_0_0_Classifier528.setter
    def uml3_0_0_Classifier528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier528", None)
        self.__uml3_0_0_Classifier528 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Action527"):
                opp_val = getattr(old_value, "uml3_0_0_Action527", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Action527", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Action527"):
                opp_val = getattr(value, "uml3_0_0_Action527", None)
                setattr(value, "uml3_0_0_Action527", self)

    @property
    def uml3_0_0_Classifier938(self):
        return self.__uml3_0_0_Classifier938

    @uml3_0_0_Classifier938.setter
    def uml3_0_0_Classifier938(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier938", None)
        self.__uml3_0_0_Classifier938 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReadIsClassifiedObjectAction"):
                opp_val = getattr(old_value, "uml3_0_0_ReadIsClassifiedObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ReadIsClassifiedObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReadIsClassifiedObjectAction"):
                opp_val = getattr(value, "uml3_0_0_ReadIsClassifiedObjectAction", None)
                setattr(value, "uml3_0_0_ReadIsClassifiedObjectAction", self)

    @property
    def uml3_0_0_Classifier928(self):
        return self.__uml3_0_0_Classifier928

    @uml3_0_0_Classifier928.setter
    def uml3_0_0_Classifier928(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier928", None)
        self.__uml3_0_0_Classifier928 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ReadExtentAction927"):
                opp_val = getattr(old_value, "uml3_0_0_ReadExtentAction927", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_ReadExtentAction927", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ReadExtentAction927"):
                opp_val = getattr(value, "uml3_0_0_ReadExtentAction927", None)
                setattr(value, "uml3_0_0_ReadExtentAction927", self)

    @property
    def uml3_0_0_Classifier487(self):
        return self.__uml3_0_0_Classifier487

    @uml3_0_0_Classifier487.setter
    def uml3_0_0_Classifier487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_Classifier__uml3_0_0_Classifier487", None)
        self.__uml3_0_0_Classifier487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ClassifierTemplateParameter"):
                opp_val = getattr(old_value, "uml3_0_0_ClassifierTemplateParameter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ClassifierTemplateParameter"):
                opp_val = getattr(value, "uml3_0_0_ClassifierTemplateParameter", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ClassifierTemplateParameter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml3_0_0_BehavioralFeature(Namespace, Feature):

    def __init__(self, isAbstract: str, concurrency: str, uml3_0_0_BehavioralFeature: set["uml3_0_0_Parameter"] = None, specification: set["uml3_0_0_Behavior"] = None, uml3_0_0_BehavioralFeature242: set["uml3_0_0_Type"] = None, BehavioralFeature: "uml3_0_0_Behavior" = None, uml3_0_0_BehavioralFeature245: set["uml3_0_0_ParameterSet"] = None):
        self.isAbstract = isAbstract
        self.concurrency = concurrency
        self.uml3_0_0_BehavioralFeature = uml3_0_0_BehavioralFeature if uml3_0_0_BehavioralFeature is not None else set()
        self.specification = specification if specification is not None else set()
        self.uml3_0_0_BehavioralFeature242 = uml3_0_0_BehavioralFeature242 if uml3_0_0_BehavioralFeature242 is not None else set()
        self.BehavioralFeature = BehavioralFeature
        self.uml3_0_0_BehavioralFeature245 = uml3_0_0_BehavioralFeature245 if uml3_0_0_BehavioralFeature245 is not None else set()
        
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
    def uml3_0_0_BehavioralFeature(self):
        return self.__uml3_0_0_BehavioralFeature

    @uml3_0_0_BehavioralFeature.setter
    def uml3_0_0_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_BehavioralFeature__uml3_0_0_BehavioralFeature", None)
        self.__uml3_0_0_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Parameter239"):
                    opp_val = getattr(item, "uml3_0_0_Parameter239", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Parameter239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Parameter239"):
                    opp_val = getattr(item, "uml3_0_0_Parameter239", None)
                    
                    setattr(item, "uml3_0_0_Parameter239", self)
                    

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_BehavioralFeature__specification", None)
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
    def uml3_0_0_BehavioralFeature242(self):
        return self.__uml3_0_0_BehavioralFeature242

    @uml3_0_0_BehavioralFeature242.setter
    def uml3_0_0_BehavioralFeature242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_BehavioralFeature__uml3_0_0_BehavioralFeature242", None)
        self.__uml3_0_0_BehavioralFeature242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Type243"):
                    opp_val = getattr(item, "uml3_0_0_Type243", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Type243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Type243"):
                    opp_val = getattr(item, "uml3_0_0_Type243", None)
                    
                    setattr(item, "uml3_0_0_Type243", self)
                    

    @property
    def uml3_0_0_BehavioralFeature245(self):
        return self.__uml3_0_0_BehavioralFeature245

    @uml3_0_0_BehavioralFeature245.setter
    def uml3_0_0_BehavioralFeature245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_BehavioralFeature__uml3_0_0_BehavioralFeature245", None)
        self.__uml3_0_0_BehavioralFeature245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_ParameterSet"):
                    opp_val = getattr(item, "uml3_0_0_ParameterSet", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_ParameterSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_ParameterSet"):
                    opp_val = getattr(item, "uml3_0_0_ParameterSet", None)
                    
                    setattr(item, "uml3_0_0_ParameterSet", self)
                    

    @property
    def BehavioralFeature(self):
        return self.__BehavioralFeature

    @BehavioralFeature.setter
    def BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_BehavioralFeature__BehavioralFeature", None)
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

class uml3_0_0_State(Vertex, Namespace, RedefinableElement):

    def __init__(self, isComposite: str, isOrthogonal: str, isSimple: str, isSubmachineState: str, State: "uml3_0_0_StateMachine" = None, State317: "uml3_0_0_Region" = None, state: set["uml3_0_0_ConnectionPointReference"] = None, state368: set["uml3_0_0_Pseudostate"] = None, uml3_0_0_State: "uml3_0_0_State" = None, uml3_0_0_State370: "uml3_0_0_State" = None, uml3_0_0_State373: "uml3_0_0_Constraint" = None, uml3_0_0_State376: "uml3_0_0_Behavior" = None, uml3_0_0_State379: "uml3_0_0_Behavior" = None, uml3_0_0_State382: "uml3_0_0_Behavior" = None, submachineState: "uml3_0_0_StateMachine" = None, state388: set["uml3_0_0_Region"] = None, State395: "uml3_0_0_ConnectionPointReference" = None, State400: "uml3_0_0_Pseudostate" = None, uml3_0_0_State385: set["uml3_0_0_Trigger"] = None, uml3_0_0_State638: "uml3_0_0_ObjectNode" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.State = State
        self.State317 = State317
        self.state = state if state is not None else set()
        self.state368 = state368 if state368 is not None else set()
        self.uml3_0_0_State = uml3_0_0_State
        self.uml3_0_0_State370 = uml3_0_0_State370
        self.uml3_0_0_State373 = uml3_0_0_State373
        self.uml3_0_0_State376 = uml3_0_0_State376
        self.uml3_0_0_State379 = uml3_0_0_State379
        self.uml3_0_0_State382 = uml3_0_0_State382
        self.submachineState = submachineState
        self.state388 = state388 if state388 is not None else set()
        self.State395 = State395
        self.State400 = State400
        self.uml3_0_0_State385 = uml3_0_0_State385 if uml3_0_0_State385 is not None else set()
        self.uml3_0_0_State638 = uml3_0_0_State638
        
    @property
    def isOrthogonal(self) -> str:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: str):
        self.__isOrthogonal = isOrthogonal

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
    def isSubmachineState(self) -> str:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: str):
        self.__isSubmachineState = isSubmachineState

    @property
    def uml3_0_0_State379(self):
        return self.__uml3_0_0_State379

    @uml3_0_0_State379.setter
    def uml3_0_0_State379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State379", None)
        self.__uml3_0_0_State379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior380"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior380", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior380"):
                opp_val = getattr(value, "uml3_0_0_Behavior380", None)
                setattr(value, "uml3_0_0_Behavior380", self)

    @property
    def State395(self):
        return self.__State395

    @State395.setter
    def State395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__State395", None)
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
    def uml3_0_0_State370(self):
        return self.__uml3_0_0_State370

    @uml3_0_0_State370.setter
    def uml3_0_0_State370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State370", None)
        self.__uml3_0_0_State370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_State"):
                opp_val = getattr(old_value, "uml3_0_0_State", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_State"):
                opp_val = getattr(value, "uml3_0_0_State", None)
                setattr(value, "uml3_0_0_State", self)

    @property
    def uml3_0_0_State373(self):
        return self.__uml3_0_0_State373

    @uml3_0_0_State373.setter
    def uml3_0_0_State373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State373", None)
        self.__uml3_0_0_State373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Constraint374"):
                opp_val = getattr(old_value, "uml3_0_0_Constraint374", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Constraint374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Constraint374"):
                opp_val = getattr(value, "uml3_0_0_Constraint374", None)
                setattr(value, "uml3_0_0_Constraint374", self)

    @property
    def State400(self):
        return self.__State400

    @State400.setter
    def State400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__State400", None)
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
    def uml3_0_0_State385(self):
        return self.__uml3_0_0_State385

    @uml3_0_0_State385.setter
    def uml3_0_0_State385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State385", None)
        self.__uml3_0_0_State385 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml3_0_0_Trigger386"):
                    opp_val = getattr(item, "uml3_0_0_Trigger386", None)
                    
                    if opp_val == self:
                        setattr(item, "uml3_0_0_Trigger386", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml3_0_0_Trigger386"):
                    opp_val = getattr(item, "uml3_0_0_Trigger386", None)
                    
                    setattr(item, "uml3_0_0_Trigger386", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__State", None)
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
    def uml3_0_0_State638(self):
        return self.__uml3_0_0_State638

    @uml3_0_0_State638.setter
    def uml3_0_0_State638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State638", None)
        self.__uml3_0_0_State638 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_ObjectNode637"):
                opp_val = getattr(old_value, "uml3_0_0_ObjectNode637", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_ObjectNode637"):
                opp_val = getattr(value, "uml3_0_0_ObjectNode637", None)
                if opp_val is None:
                    setattr(value, "uml3_0_0_ObjectNode637", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State317(self):
        return self.__State317

    @State317.setter
    def State317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__State317", None)
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
    def state388(self):
        return self.__state388

    @state388.setter
    def state388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__state388", None)
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
    def uml3_0_0_State382(self):
        return self.__uml3_0_0_State382

    @uml3_0_0_State382.setter
    def uml3_0_0_State382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State382", None)
        self.__uml3_0_0_State382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior383"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior383", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior383"):
                opp_val = getattr(value, "uml3_0_0_Behavior383", None)
                setattr(value, "uml3_0_0_Behavior383", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__state", None)
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
    def uml3_0_0_State376(self):
        return self.__uml3_0_0_State376

    @uml3_0_0_State376.setter
    def uml3_0_0_State376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State376", None)
        self.__uml3_0_0_State376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_Behavior377"):
                opp_val = getattr(old_value, "uml3_0_0_Behavior377", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_Behavior377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_Behavior377"):
                opp_val = getattr(value, "uml3_0_0_Behavior377", None)
                setattr(value, "uml3_0_0_Behavior377", self)

    @property
    def submachineState(self):
        return self.__submachineState

    @submachineState.setter
    def submachineState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__submachineState", None)
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
    def uml3_0_0_State(self):
        return self.__uml3_0_0_State

    @uml3_0_0_State.setter
    def uml3_0_0_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__uml3_0_0_State", None)
        self.__uml3_0_0_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml3_0_0_State370"):
                opp_val = getattr(old_value, "uml3_0_0_State370", None)
                if opp_val == self:
                    setattr(old_value, "uml3_0_0_State370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml3_0_0_State370"):
                opp_val = getattr(value, "uml3_0_0_State370", None)
                setattr(value, "uml3_0_0_State370", self)

    @property
    def state368(self):
        return self.__state368

    @state368.setter
    def state368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml3_0_0_State__state368", None)
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
                    

class uml3_0_0_Package(TemplateableElement, PackageableElement, Namespace):

    pass
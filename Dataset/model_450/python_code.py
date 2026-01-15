from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CallConcurrencyKind(Enum):
    guarded = "guarded"
    concurrent = "concurrent"
    sequential = "sequential"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class ObjectNodeOrderingKind(Enum):
    FIFO = "FIFO"
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
class ConnectorKind(Enum):
    delegation = "delegation"
    assembly = "assembly"
class ParameterEffectKind(Enum):
    update = "update"
    read = "read"
    delete = "delete"
    create = "create"
class AggregationKind(Enum):
    composite = "composite"
    none = "none"
    shared = "shared"
class MessageKind(Enum):
    unknown = "unknown"
    complete = "complete"
    found = "found"
    lost = "lost"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class MessageSort(Enum):
    synchSignal = "synchSignal"
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
class PseudostateKind(Enum):
    shallowHistory = "shallowHistory"
    choice = "choice"
    join = "join"
    exitPoint = "exitPoint"
    terminate = "terminate"
    fork = "fork"
    junction = "junction"
    initial = "initial"
    entryPoint = "entryPoint"
    deepHistory = "deepHistory"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class InteractionOperator(Enum):
    loop = "loop"
    alt = "alt"
    break = "break"
    assert = "assert"
    strict = "strict"
    seq = "seq"
    ignore = "ignore"
    neg = "neg"
    critical = "critical"
    consider = "consider"
    par = "par"
    opt = "opt"
class VisibilityKind(Enum):
    package = "package"
    private = "private"
    protected = "protected"
    public = "public"


############################################
# Definition of Classes
############################################

class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class Artifact:

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class StateMachine:

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class UML2_DeploymentSpecification(Artifact):

    def __init__(self, deploymentLocation: str, executionLocation: str, UML2_DeploymentSpecification: "UML2_Deployment" = None):
        self.deploymentLocation = deploymentLocation
        self.executionLocation = executionLocation
        self.UML2_DeploymentSpecification = UML2_DeploymentSpecification
        
    @property
    def executionLocation(self) -> str:
        return self.__executionLocation

    @executionLocation.setter
    def executionLocation(self, executionLocation: str):
        self.__executionLocation = executionLocation

    @property
    def deploymentLocation(self) -> str:
        return self.__deploymentLocation

    @deploymentLocation.setter
    def deploymentLocation(self, deploymentLocation: str):
        self.__deploymentLocation = deploymentLocation

    @property
    def UML2_DeploymentSpecification(self):
        return self.__UML2_DeploymentSpecification

    @UML2_DeploymentSpecification.setter
    def UML2_DeploymentSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_DeploymentSpecification__UML2_DeploymentSpecification", None)
        self.__UML2_DeploymentSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Deployment868"):
                opp_val = getattr(old_value, "UML2_Deployment868", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Deployment868"):
                opp_val = getattr(value, "UML2_Deployment868", None)
                if opp_val is None:
                    setattr(value, "UML2_Deployment868", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IntervalConstraint:

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class Interval:

    pass
class UML2_DurationInterval(Interval):

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class UML2_TimeInterval(Interval):

    pass
class CallAction:

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class UML2_CallOperationAction(CallAction):

    pass
class WriteVariableAction:

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    def __init__(self, isReplaceAll: bool, UML2_AddVariableValueAction: "UML2_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2_AddVariableValueAction = UML2_AddVariableValueAction
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2_AddVariableValueAction(self):
        return self.__UML2_AddVariableValueAction

    @UML2_AddVariableValueAction.setter
    def UML2_AddVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_AddVariableValueAction__UML2_AddVariableValueAction", None)
        self.__UML2_AddVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InputPin800"):
                opp_val = getattr(old_value, "UML2_InputPin800", None)
                if opp_val == self:
                    setattr(old_value, "UML2_InputPin800", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InputPin800"):
                opp_val = getattr(value, "UML2_InputPin800", None)
                setattr(value, "UML2_InputPin800", self)

class VariableAction:

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class InvocationAction:

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_CallAction(InvocationAction):

    def __init__(self, isSynchronous: bool, UML2_CallAction: set["UML2_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.UML2_CallAction = UML2_CallAction if UML2_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> bool:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: bool):
        self.__isSynchronous = isSynchronous

    @property
    def UML2_CallAction(self):
        return self.__UML2_CallAction

    @UML2_CallAction.setter
    def UML2_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_CallAction__UML2_CallAction", None)
        self.__UML2_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_OutputPin809"):
                    opp_val = getattr(item, "UML2_OutputPin809", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_OutputPin809", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_OutputPin809"):
                    opp_val = getattr(item, "UML2_OutputPin809", None)
                    
                    setattr(item, "UML2_OutputPin809", self)
                    

class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class WriteLinkAction:

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class LinkEndData:

    pass
class UML2_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: bool, UML2_LinkEndCreationData: "UML2_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2_LinkEndCreationData = UML2_LinkEndCreationData
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2_LinkEndCreationData(self):
        return self.__UML2_LinkEndCreationData

    @UML2_LinkEndCreationData.setter
    def UML2_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LinkEndCreationData__UML2_LinkEndCreationData", None)
        self.__UML2_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InputPin788"):
                opp_val = getattr(old_value, "UML2_InputPin788", None)
                if opp_val == self:
                    setattr(old_value, "UML2_InputPin788", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InputPin788"):
                opp_val = getattr(value, "UML2_InputPin788", None)
                setattr(value, "UML2_InputPin788", self)

class LinkAction:

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isReplaceAll: bool, UML2_AddStructuralFeatureValueAction: "UML2_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2_AddStructuralFeatureValueAction = UML2_AddStructuralFeatureValueAction
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2_AddStructuralFeatureValueAction(self):
        return self.__UML2_AddStructuralFeatureValueAction

    @UML2_AddStructuralFeatureValueAction.setter
    def UML2_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_AddStructuralFeatureValueAction__UML2_AddStructuralFeatureValueAction", None)
        self.__UML2_AddStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InputPin775"):
                opp_val = getattr(old_value, "UML2_InputPin775", None)
                if opp_val == self:
                    setattr(old_value, "UML2_InputPin775", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InputPin775"):
                opp_val = getattr(value, "UML2_InputPin775", None)
                setattr(value, "UML2_InputPin775", self)

class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class StructuralFeatureAction:

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class State:

    pass
class UML2_FinalState(State):

    pass
class Vertex:

    pass
class UML2_ConnectionPointReference(Vertex):

    pass
class Constraint:

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class UML2_Pseudostate(Vertex):

    def __init__(self, kind: str, UML2_Pseudostate: "UML2_StateMachine" = None, UML2_Pseudostate725: "UML2_ConnectionPointReference" = None, UML2_Pseudostate728: "UML2_ConnectionPointReference" = None):
        self.kind = kind
        self.UML2_Pseudostate = UML2_Pseudostate
        self.UML2_Pseudostate725 = UML2_Pseudostate725
        self.UML2_Pseudostate728 = UML2_Pseudostate728
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def UML2_Pseudostate(self):
        return self.__UML2_Pseudostate

    @UML2_Pseudostate.setter
    def UML2_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Pseudostate__UML2_Pseudostate", None)
        self.__UML2_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StateMachine"):
                opp_val = getattr(old_value, "UML2_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StateMachine"):
                opp_val = getattr(value, "UML2_StateMachine", None)
                if opp_val is None:
                    setattr(value, "UML2_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Pseudostate725(self):
        return self.__UML2_Pseudostate725

    @UML2_Pseudostate725.setter
    def UML2_Pseudostate725(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Pseudostate__UML2_Pseudostate725", None)
        self.__UML2_Pseudostate725 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ConnectionPointReference724"):
                opp_val = getattr(old_value, "UML2_ConnectionPointReference724", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ConnectionPointReference724"):
                opp_val = getattr(value, "UML2_ConnectionPointReference724", None)
                if opp_val is None:
                    setattr(value, "UML2_ConnectionPointReference724", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Pseudostate728(self):
        return self.__UML2_Pseudostate728

    @UML2_Pseudostate728.setter
    def UML2_Pseudostate728(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Pseudostate__UML2_Pseudostate728", None)
        self.__UML2_Pseudostate728 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ConnectionPointReference727"):
                opp_val = getattr(old_value, "UML2_ConnectionPointReference727", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ConnectionPointReference727"):
                opp_val = getattr(value, "UML2_ConnectionPointReference727", None)
                if opp_val is None:
                    setattr(value, "UML2_ConnectionPointReference727", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_InteractionConstraint(Constraint):

    pass
class InteractionOccurrence:

    pass
class TemplateSignature:

    pass
class TemplateParameter:

    pass
class UML2_ClassifierTemplateParameter(TemplateParameter):

    def __init__(self, allowSubstitutable: bool):
        self.allowSubstitutable = allowSubstitutable
        
    @property
    def allowSubstitutable(self) -> bool:
        return self.__allowSubstitutable

    @allowSubstitutable.setter
    def allowSubstitutable(self, allowSubstitutable: bool):
        self.__allowSubstitutable = allowSubstitutable

class UML2_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class UML2_OperationTemplateParameter(TemplateParameter):

    pass
class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class MessageEnd:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class UML2_Gate(MessageEnd):

    pass
class InteractionFragment:

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class UML2_Continuation(InteractionFragment):

    def __init__(self, setting: bool):
        self.setting = setting
        
    @property
    def setting(self) -> bool:
        return self.__setting

    @setting.setter
    def setting(self, setting: bool):
        self.__setting = setting

class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_CombinedFragment(InteractionFragment):

    def __init__(self, interactionOperator: str, UML2_CombinedFragment: set["UML2_InteractionOperand"] = None, UML2_CombinedFragment672: set["UML2_Gate"] = None):
        self.interactionOperator = interactionOperator
        self.UML2_CombinedFragment = UML2_CombinedFragment if UML2_CombinedFragment is not None else set()
        self.UML2_CombinedFragment672 = UML2_CombinedFragment672 if UML2_CombinedFragment672 is not None else set()
        
    @property
    def interactionOperator(self) -> str:
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator

    @property
    def UML2_CombinedFragment672(self):
        return self.__UML2_CombinedFragment672

    @UML2_CombinedFragment672.setter
    def UML2_CombinedFragment672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_CombinedFragment__UML2_CombinedFragment672", None)
        self.__UML2_CombinedFragment672 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Gate673"):
                    opp_val = getattr(item, "UML2_Gate673", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Gate673", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Gate673"):
                    opp_val = getattr(item, "UML2_Gate673", None)
                    
                    setattr(item, "UML2_Gate673", self)
                    

    @property
    def UML2_CombinedFragment(self):
        return self.__UML2_CombinedFragment

    @UML2_CombinedFragment.setter
    def UML2_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_CombinedFragment__UML2_CombinedFragment", None)
        self.__UML2_CombinedFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_InteractionOperand670"):
                    opp_val = getattr(item, "UML2_InteractionOperand670", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_InteractionOperand670", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_InteractionOperand670"):
                    opp_val = getattr(item, "UML2_InteractionOperand670", None)
                    
                    setattr(item, "UML2_InteractionOperand670", self)
                    

class UML2_StateInvariant(InteractionFragment):

    pass
class UML2_EventOccurrence(InteractionFragment, MessageEnd):

    pass
class StructuredActivityNode:

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, ExpansionRegion: "UML2_ExpansionNode" = None, ExpansionRegion640: "UML2_ExpansionNode" = None, regionAsOutput: set["UML2_ExpansionNode"] = None, regionAsInput: set["UML2_ExpansionNode"] = None):
        self.mode = mode
        self.ExpansionRegion = ExpansionRegion
        self.ExpansionRegion640 = ExpansionRegion640
        self.regionAsOutput = regionAsOutput if regionAsOutput is not None else set()
        self.regionAsInput = regionAsInput if regionAsInput is not None else set()
        
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
        old_value = getattr(self, f"_UML2_ExpansionRegion__regionAsInput", None)
        self.__regionAsInput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpansionNode643"):
                    opp_val = getattr(item, "ExpansionNode643", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode643", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode643"):
                    opp_val = getattr(item, "ExpansionNode643", None)
                    
                    setattr(item, "ExpansionNode643", self)
                    

    @property
    def ExpansionRegion(self):
        return self.__ExpansionRegion

    @ExpansionRegion.setter
    def ExpansionRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ExpansionRegion__ExpansionRegion", None)
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
    def ExpansionRegion640(self):
        return self.__ExpansionRegion640

    @ExpansionRegion640.setter
    def ExpansionRegion640(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ExpansionRegion__ExpansionRegion640", None)
        self.__ExpansionRegion640 = value
        
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
        old_value = getattr(self, f"_UML2_ExpansionRegion__regionAsOutput", None)
        self.__regionAsOutput = value if value is not None else set()
        
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
                    

class UML2_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: bool, isAssured: bool, UML2_ConditionalNode: set["UML2_Clause"] = None, UML2_ConditionalNode478: set["UML2_OutputPin"] = None):
        self.isDeterminate = isDeterminate
        self.isAssured = isAssured
        self.UML2_ConditionalNode = UML2_ConditionalNode if UML2_ConditionalNode is not None else set()
        self.UML2_ConditionalNode478 = UML2_ConditionalNode478 if UML2_ConditionalNode478 is not None else set()
        
    @property
    def isDeterminate(self) -> bool:
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: bool):
        self.__isDeterminate = isDeterminate

    @property
    def isAssured(self) -> bool:
        return self.__isAssured

    @isAssured.setter
    def isAssured(self, isAssured: bool):
        self.__isAssured = isAssured

    @property
    def UML2_ConditionalNode(self):
        return self.__UML2_ConditionalNode

    @UML2_ConditionalNode.setter
    def UML2_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ConditionalNode__UML2_ConditionalNode", None)
        self.__UML2_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Clause"):
                    opp_val = getattr(item, "UML2_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Clause"):
                    opp_val = getattr(item, "UML2_Clause", None)
                    
                    setattr(item, "UML2_Clause", self)
                    

    @property
    def UML2_ConditionalNode478(self):
        return self.__UML2_ConditionalNode478

    @UML2_ConditionalNode478.setter
    def UML2_ConditionalNode478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ConditionalNode__UML2_ConditionalNode478", None)
        self.__UML2_ConditionalNode478 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_OutputPin479"):
                    opp_val = getattr(item, "UML2_OutputPin479", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_OutputPin479", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_OutputPin479"):
                    opp_val = getattr(item, "UML2_OutputPin479", None)
                    
                    setattr(item, "UML2_OutputPin479", self)
                    

class UML2_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: bool, UML2_LoopNode: set["UML2_ActivityNode"] = None, UML2_LoopNode500: set["UML2_ActivityNode"] = None, UML2_LoopNode515: set["UML2_OutputPin"] = None, UML2_LoopNode518: set["UML2_InputPin"] = None, UML2_LoopNode503: "UML2_OutputPin" = None, UML2_LoopNode506: set["UML2_ActivityNode"] = None, UML2_LoopNode509: set["UML2_OutputPin"] = None, UML2_LoopNode512: set["UML2_OutputPin"] = None):
        self.isTestedFirst = isTestedFirst
        self.UML2_LoopNode = UML2_LoopNode if UML2_LoopNode is not None else set()
        self.UML2_LoopNode500 = UML2_LoopNode500 if UML2_LoopNode500 is not None else set()
        self.UML2_LoopNode515 = UML2_LoopNode515 if UML2_LoopNode515 is not None else set()
        self.UML2_LoopNode518 = UML2_LoopNode518 if UML2_LoopNode518 is not None else set()
        self.UML2_LoopNode503 = UML2_LoopNode503
        self.UML2_LoopNode506 = UML2_LoopNode506 if UML2_LoopNode506 is not None else set()
        self.UML2_LoopNode509 = UML2_LoopNode509 if UML2_LoopNode509 is not None else set()
        self.UML2_LoopNode512 = UML2_LoopNode512 if UML2_LoopNode512 is not None else set()
        
    @property
    def isTestedFirst(self) -> bool:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: bool):
        self.__isTestedFirst = isTestedFirst

    @property
    def UML2_LoopNode509(self):
        return self.__UML2_LoopNode509

    @UML2_LoopNode509.setter
    def UML2_LoopNode509(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode509", None)
        self.__UML2_LoopNode509 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_OutputPin510"):
                    opp_val = getattr(item, "UML2_OutputPin510", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_OutputPin510", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_OutputPin510"):
                    opp_val = getattr(item, "UML2_OutputPin510", None)
                    
                    setattr(item, "UML2_OutputPin510", self)
                    

    @property
    def UML2_LoopNode515(self):
        return self.__UML2_LoopNode515

    @UML2_LoopNode515.setter
    def UML2_LoopNode515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode515", None)
        self.__UML2_LoopNode515 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_OutputPin516"):
                    opp_val = getattr(item, "UML2_OutputPin516", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_OutputPin516", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_OutputPin516"):
                    opp_val = getattr(item, "UML2_OutputPin516", None)
                    
                    setattr(item, "UML2_OutputPin516", self)
                    

    @property
    def UML2_LoopNode(self):
        return self.__UML2_LoopNode

    @UML2_LoopNode.setter
    def UML2_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode", None)
        self.__UML2_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ActivityNode498"):
                    opp_val = getattr(item, "UML2_ActivityNode498", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ActivityNode498", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ActivityNode498"):
                    opp_val = getattr(item, "UML2_ActivityNode498", None)
                    
                    setattr(item, "UML2_ActivityNode498", self)
                    

    @property
    def UML2_LoopNode506(self):
        return self.__UML2_LoopNode506

    @UML2_LoopNode506.setter
    def UML2_LoopNode506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode506", None)
        self.__UML2_LoopNode506 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ActivityNode507"):
                    opp_val = getattr(item, "UML2_ActivityNode507", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ActivityNode507", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ActivityNode507"):
                    opp_val = getattr(item, "UML2_ActivityNode507", None)
                    
                    setattr(item, "UML2_ActivityNode507", self)
                    

    @property
    def UML2_LoopNode503(self):
        return self.__UML2_LoopNode503

    @UML2_LoopNode503.setter
    def UML2_LoopNode503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode503", None)
        self.__UML2_LoopNode503 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_OutputPin504"):
                opp_val = getattr(old_value, "UML2_OutputPin504", None)
                if opp_val == self:
                    setattr(old_value, "UML2_OutputPin504", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_OutputPin504"):
                opp_val = getattr(value, "UML2_OutputPin504", None)
                setattr(value, "UML2_OutputPin504", self)

    @property
    def UML2_LoopNode512(self):
        return self.__UML2_LoopNode512

    @UML2_LoopNode512.setter
    def UML2_LoopNode512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode512", None)
        self.__UML2_LoopNode512 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_OutputPin513"):
                    opp_val = getattr(item, "UML2_OutputPin513", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_OutputPin513", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_OutputPin513"):
                    opp_val = getattr(item, "UML2_OutputPin513", None)
                    
                    setattr(item, "UML2_OutputPin513", self)
                    

    @property
    def UML2_LoopNode500(self):
        return self.__UML2_LoopNode500

    @UML2_LoopNode500.setter
    def UML2_LoopNode500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode500", None)
        self.__UML2_LoopNode500 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ActivityNode501"):
                    opp_val = getattr(item, "UML2_ActivityNode501", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ActivityNode501", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ActivityNode501"):
                    opp_val = getattr(item, "UML2_ActivityNode501", None)
                    
                    setattr(item, "UML2_ActivityNode501", self)
                    

    @property
    def UML2_LoopNode518(self):
        return self.__UML2_LoopNode518

    @UML2_LoopNode518.setter
    def UML2_LoopNode518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_LoopNode__UML2_LoopNode518", None)
        self.__UML2_LoopNode518 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_InputPin519"):
                    opp_val = getattr(item, "UML2_InputPin519", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_InputPin519", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_InputPin519"):
                    opp_val = getattr(item, "UML2_InputPin519", None)
                    
                    setattr(item, "UML2_InputPin519", self)
                    

class ActivityGroup:

    pass
class Action:

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    def __init__(self, isDestroyLinks: bool, isDestroyOwnedObjects: bool, UML2_DestroyObjectAction: "UML2_InputPin" = None):
        self.isDestroyLinks = isDestroyLinks
        self.isDestroyOwnedObjects = isDestroyOwnedObjects
        self.UML2_DestroyObjectAction = UML2_DestroyObjectAction
        
    @property
    def isDestroyOwnedObjects(self) -> bool:
        return self.__isDestroyOwnedObjects

    @isDestroyOwnedObjects.setter
    def isDestroyOwnedObjects(self, isDestroyOwnedObjects: bool):
        self.__isDestroyOwnedObjects = isDestroyOwnedObjects

    @property
    def isDestroyLinks(self) -> bool:
        return self.__isDestroyLinks

    @isDestroyLinks.setter
    def isDestroyLinks(self, isDestroyLinks: bool):
        self.__isDestroyLinks = isDestroyLinks

    @property
    def UML2_DestroyObjectAction(self):
        return self.__UML2_DestroyObjectAction

    @UML2_DestroyObjectAction.setter
    def UML2_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_DestroyObjectAction__UML2_DestroyObjectAction", None)
        self.__UML2_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InputPin754"):
                opp_val = getattr(old_value, "UML2_InputPin754", None)
                if opp_val == self:
                    setattr(old_value, "UML2_InputPin754", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InputPin754"):
                opp_val = getattr(value, "UML2_InputPin754", None)
                setattr(value, "UML2_InputPin754", self)

class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    def __init__(self, isDirect: bool, UML2_ReadIsClassifiedObjectAction: "UML2_Classifier" = None, UML2_ReadIsClassifiedObjectAction902: "UML2_OutputPin" = None, UML2_ReadIsClassifiedObjectAction905: "UML2_InputPin" = None):
        self.isDirect = isDirect
        self.UML2_ReadIsClassifiedObjectAction = UML2_ReadIsClassifiedObjectAction
        self.UML2_ReadIsClassifiedObjectAction902 = UML2_ReadIsClassifiedObjectAction902
        self.UML2_ReadIsClassifiedObjectAction905 = UML2_ReadIsClassifiedObjectAction905
        
    @property
    def isDirect(self) -> bool:
        return self.__isDirect

    @isDirect.setter
    def isDirect(self, isDirect: bool):
        self.__isDirect = isDirect

    @property
    def UML2_ReadIsClassifiedObjectAction(self):
        return self.__UML2_ReadIsClassifiedObjectAction

    @UML2_ReadIsClassifiedObjectAction.setter
    def UML2_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ReadIsClassifiedObjectAction__UML2_ReadIsClassifiedObjectAction", None)
        self.__UML2_ReadIsClassifiedObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier900"):
                opp_val = getattr(old_value, "UML2_Classifier900", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Classifier900", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier900"):
                opp_val = getattr(value, "UML2_Classifier900", None)
                setattr(value, "UML2_Classifier900", self)

    @property
    def UML2_ReadIsClassifiedObjectAction905(self):
        return self.__UML2_ReadIsClassifiedObjectAction905

    @UML2_ReadIsClassifiedObjectAction905.setter
    def UML2_ReadIsClassifiedObjectAction905(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ReadIsClassifiedObjectAction__UML2_ReadIsClassifiedObjectAction905", None)
        self.__UML2_ReadIsClassifiedObjectAction905 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InputPin906"):
                opp_val = getattr(old_value, "UML2_InputPin906", None)
                if opp_val == self:
                    setattr(old_value, "UML2_InputPin906", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InputPin906"):
                opp_val = getattr(value, "UML2_InputPin906", None)
                setattr(value, "UML2_InputPin906", self)

    @property
    def UML2_ReadIsClassifiedObjectAction902(self):
        return self.__UML2_ReadIsClassifiedObjectAction902

    @UML2_ReadIsClassifiedObjectAction902.setter
    def UML2_ReadIsClassifiedObjectAction902(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ReadIsClassifiedObjectAction__UML2_ReadIsClassifiedObjectAction902", None)
        self.__UML2_ReadIsClassifiedObjectAction902 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_OutputPin903"):
                opp_val = getattr(old_value, "UML2_OutputPin903", None)
                if opp_val == self:
                    setattr(old_value, "UML2_OutputPin903", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_OutputPin903"):
                opp_val = getattr(value, "UML2_OutputPin903", None)
                setattr(value, "UML2_OutputPin903", self)

class UML2_RaiseExceptionAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: bool, UML2_ReclassifyObjectAction: set["UML2_Classifier"] = None, UML2_ReclassifyObjectAction894: set["UML2_Classifier"] = None, UML2_ReclassifyObjectAction897: "UML2_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2_ReclassifyObjectAction = UML2_ReclassifyObjectAction if UML2_ReclassifyObjectAction is not None else set()
        self.UML2_ReclassifyObjectAction894 = UML2_ReclassifyObjectAction894 if UML2_ReclassifyObjectAction894 is not None else set()
        self.UML2_ReclassifyObjectAction897 = UML2_ReclassifyObjectAction897
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2_ReclassifyObjectAction894(self):
        return self.__UML2_ReclassifyObjectAction894

    @UML2_ReclassifyObjectAction894.setter
    def UML2_ReclassifyObjectAction894(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ReclassifyObjectAction__UML2_ReclassifyObjectAction894", None)
        self.__UML2_ReclassifyObjectAction894 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier895"):
                    opp_val = getattr(item, "UML2_Classifier895", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier895", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier895"):
                    opp_val = getattr(item, "UML2_Classifier895", None)
                    
                    setattr(item, "UML2_Classifier895", self)
                    

    @property
    def UML2_ReclassifyObjectAction(self):
        return self.__UML2_ReclassifyObjectAction

    @UML2_ReclassifyObjectAction.setter
    def UML2_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ReclassifyObjectAction__UML2_ReclassifyObjectAction", None)
        self.__UML2_ReclassifyObjectAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier892"):
                    opp_val = getattr(item, "UML2_Classifier892", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier892", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier892"):
                    opp_val = getattr(item, "UML2_Classifier892", None)
                    
                    setattr(item, "UML2_Classifier892", self)
                    

    @property
    def UML2_ReclassifyObjectAction897(self):
        return self.__UML2_ReclassifyObjectAction897

    @UML2_ReclassifyObjectAction897.setter
    def UML2_ReclassifyObjectAction897(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ReclassifyObjectAction__UML2_ReclassifyObjectAction897", None)
        self.__UML2_ReclassifyObjectAction897 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InputPin898"):
                opp_val = getattr(old_value, "UML2_InputPin898", None)
                if opp_val == self:
                    setattr(old_value, "UML2_InputPin898", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InputPin898"):
                opp_val = getattr(value, "UML2_InputPin898", None)
                setattr(value, "UML2_InputPin898", self)

class UML2_ApplyFunctionAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class Trigger:

    pass
class UML2_ChangeTrigger(Trigger):

    pass
class UML2_TimeTrigger(Trigger):

    def __init__(self, isRelative: bool, UML2_TimeTrigger: "UML2_ValueSpecification" = None):
        self.isRelative = isRelative
        self.UML2_TimeTrigger = UML2_TimeTrigger
        
    @property
    def isRelative(self) -> bool:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: bool):
        self.__isRelative = isRelative

    @property
    def UML2_TimeTrigger(self):
        return self.__UML2_TimeTrigger

    @UML2_TimeTrigger.setter
    def UML2_TimeTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_TimeTrigger__UML2_TimeTrigger", None)
        self.__UML2_TimeTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ValueSpecification467"):
                opp_val = getattr(old_value, "UML2_ValueSpecification467", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ValueSpecification467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ValueSpecification467"):
                opp_val = getattr(value, "UML2_ValueSpecification467", None)
                setattr(value, "UML2_ValueSpecification467", self)

class UML2_MessageTrigger(Trigger):

    pass
class MessageTrigger:

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class ActivityNode:

    pass
class ObjectNode:

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class Pin:

    pass
class UML2_ExecutableNode(ActivityNode):

    pass
class FinalNode:

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class UML2_ForkNode(ControlNode):

    pass
class UML2_DecisionNode(ControlNode):

    pass
class UML2_MergeNode(ControlNode):

    pass
class UML2_FinalNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: bool, UML2_JoinNode: "UML2_ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.UML2_JoinNode = UML2_JoinNode
        
    @property
    def isCombineDuplicate(self) -> bool:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: bool):
        self.__isCombineDuplicate = isCombineDuplicate

    @property
    def UML2_JoinNode(self):
        return self.__UML2_JoinNode

    @UML2_JoinNode.setter
    def UML2_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_JoinNode__UML2_JoinNode", None)
        self.__UML2_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ValueSpecification624"):
                opp_val = getattr(old_value, "UML2_ValueSpecification624", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ValueSpecification624", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ValueSpecification624"):
                opp_val = getattr(value, "UML2_ValueSpecification624", None)
                setattr(value, "UML2_ValueSpecification624", self)

class UML2_InitialNode(ControlNode):

    pass
class ActivityEdge:

    pass
class UML2_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool, UML2_ObjectFlow: "UML2_Behavior" = None, UML2_ObjectFlow367: "UML2_Behavior" = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.UML2_ObjectFlow = UML2_ObjectFlow
        self.UML2_ObjectFlow367 = UML2_ObjectFlow367
        
    @property
    def isMultireceive(self) -> bool:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: bool):
        self.__isMultireceive = isMultireceive

    @property
    def isMulticast(self) -> bool:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: bool):
        self.__isMulticast = isMulticast

    @property
    def UML2_ObjectFlow367(self):
        return self.__UML2_ObjectFlow367

    @UML2_ObjectFlow367.setter
    def UML2_ObjectFlow367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ObjectFlow__UML2_ObjectFlow367", None)
        self.__UML2_ObjectFlow367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior368"):
                opp_val = getattr(old_value, "UML2_Behavior368", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Behavior368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior368"):
                opp_val = getattr(value, "UML2_Behavior368", None)
                setattr(value, "UML2_Behavior368", self)

    @property
    def UML2_ObjectFlow(self):
        return self.__UML2_ObjectFlow

    @UML2_ObjectFlow.setter
    def UML2_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ObjectFlow__UML2_ObjectFlow", None)
        self.__UML2_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior365"):
                opp_val = getattr(old_value, "UML2_Behavior365", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Behavior365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior365"):
                opp_val = getattr(value, "UML2_Behavior365", None)
                setattr(value, "UML2_Behavior365", self)

class UML2_ControlFlow(ActivityEdge):

    pass
class UML2_ControlNode(ActivityNode):

    pass
class UML2_InputPin(Pin):

    pass
class UML2_OutputPin(Pin):

    pass
class ExecutableNode:

    pass
class UML2_InterruptibleActivityRegion(ActivityGroup):

    pass
class Realization:

    pass
class Abstraction:

    pass
class UML2_Manifestation(Abstraction):

    pass
class UML2_Realization(Abstraction):

    pass
class UML2_Implementation(Realization):

    pass
class Dependency:

    pass
class UML2_Deployment(Dependency):

    pass
class UML2_Usage(Dependency):

    pass
class UML2_Abstraction(Dependency):

    pass
class UML2_Permission(Dependency):

    pass
class UML2_Action(ExecutableNode):

    def __init__(self, effect: str, UML2_Action: "UML2_Activity" = None, UML2_Action345: set["UML2_OutputPin"] = None, UML2_Action347: set["UML2_InputPin"] = None, UML2_Action349: "UML2_Classifier" = None, UML2_Action352: set["UML2_Constraint"] = None, UML2_Action355: set["UML2_Constraint"] = None):
        self.effect = effect
        self.UML2_Action = UML2_Action
        self.UML2_Action345 = UML2_Action345 if UML2_Action345 is not None else set()
        self.UML2_Action347 = UML2_Action347 if UML2_Action347 is not None else set()
        self.UML2_Action349 = UML2_Action349
        self.UML2_Action352 = UML2_Action352 if UML2_Action352 is not None else set()
        self.UML2_Action355 = UML2_Action355 if UML2_Action355 is not None else set()
        
    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def UML2_Action347(self):
        return self.__UML2_Action347

    @UML2_Action347.setter
    def UML2_Action347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Action__UML2_Action347", None)
        self.__UML2_Action347 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_InputPin"):
                    opp_val = getattr(item, "UML2_InputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_InputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_InputPin"):
                    opp_val = getattr(item, "UML2_InputPin", None)
                    
                    setattr(item, "UML2_InputPin", self)
                    

    @property
    def UML2_Action349(self):
        return self.__UML2_Action349

    @UML2_Action349.setter
    def UML2_Action349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Action__UML2_Action349", None)
        self.__UML2_Action349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier350"):
                opp_val = getattr(old_value, "UML2_Classifier350", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Classifier350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier350"):
                opp_val = getattr(value, "UML2_Classifier350", None)
                setattr(value, "UML2_Classifier350", self)

    @property
    def UML2_Action352(self):
        return self.__UML2_Action352

    @UML2_Action352.setter
    def UML2_Action352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Action__UML2_Action352", None)
        self.__UML2_Action352 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Constraint353"):
                    opp_val = getattr(item, "UML2_Constraint353", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Constraint353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Constraint353"):
                    opp_val = getattr(item, "UML2_Constraint353", None)
                    
                    setattr(item, "UML2_Constraint353", self)
                    

    @property
    def UML2_Action345(self):
        return self.__UML2_Action345

    @UML2_Action345.setter
    def UML2_Action345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Action__UML2_Action345", None)
        self.__UML2_Action345 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_OutputPin"):
                    opp_val = getattr(item, "UML2_OutputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_OutputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_OutputPin"):
                    opp_val = getattr(item, "UML2_OutputPin", None)
                    
                    setattr(item, "UML2_OutputPin", self)
                    

    @property
    def UML2_Action(self):
        return self.__UML2_Action

    @UML2_Action.setter
    def UML2_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Action__UML2_Action", None)
        self.__UML2_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Activity"):
                opp_val = getattr(old_value, "UML2_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Activity"):
                opp_val = getattr(value, "UML2_Activity", None)
                if opp_val is None:
                    setattr(value, "UML2_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Action355(self):
        return self.__UML2_Action355

    @UML2_Action355.setter
    def UML2_Action355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Action__UML2_Action355", None)
        self.__UML2_Action355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Constraint356"):
                    opp_val = getattr(item, "UML2_Constraint356", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Constraint356", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Constraint356"):
                    opp_val = getattr(item, "UML2_Constraint356", None)
                    
                    setattr(item, "UML2_Constraint356", self)
                    

class Behavior:

    pass
class UML2_Interaction(Behavior, InteractionFragment):

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Activity(Behavior):

    def __init__(self, body: str, language: str, isSingleExecution: bool, isReadOnly: bool, activity: set["UML2_ActivityEdge"] = None, activityGroup_activity: set["UML2_ActivityGroup"] = None, activity246: set["UML2_ActivityNode"] = None, UML2_Activity: set["UML2_Action"] = None, UML2_Activity249: set["UML2_StructuredActivityNode"] = None, Activity: "UML2_ActivityEdge" = None, Activity332: "UML2_ActivityNode" = None, Activity324: "UML2_ActivityGroup" = None, UML2_Activity705: "UML2_State" = None, UML2_Activity708: "UML2_State" = None, UML2_Activity711: "UML2_State" = None, UML2_Activity747: "UML2_Transition" = None):
        self.body = body
        self.language = language
        self.isSingleExecution = isSingleExecution
        self.isReadOnly = isReadOnly
        self.activity = activity if activity is not None else set()
        self.activityGroup_activity = activityGroup_activity if activityGroup_activity is not None else set()
        self.activity246 = activity246 if activity246 is not None else set()
        self.UML2_Activity = UML2_Activity if UML2_Activity is not None else set()
        self.UML2_Activity249 = UML2_Activity249 if UML2_Activity249 is not None else set()
        self.Activity = Activity
        self.Activity332 = Activity332
        self.Activity324 = Activity324
        self.UML2_Activity705 = UML2_Activity705
        self.UML2_Activity708 = UML2_Activity708
        self.UML2_Activity711 = UML2_Activity711
        self.UML2_Activity747 = UML2_Activity747
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def isSingleExecution(self) -> bool:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edge"):
                opp_val = getattr(old_value, "edge", None)
                if opp_val == self:
                    setattr(old_value, "edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edge"):
                opp_val = getattr(value, "edge", None)
                setattr(value, "edge", self)

    @property
    def UML2_Activity249(self):
        return self.__UML2_Activity249

    @UML2_Activity249.setter
    def UML2_Activity249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__UML2_Activity249", None)
        self.__UML2_Activity249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_StructuredActivityNode"):
                    opp_val = getattr(item, "UML2_StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_StructuredActivityNode"):
                    opp_val = getattr(item, "UML2_StructuredActivityNode", None)
                    
                    setattr(item, "UML2_StructuredActivityNode", self)
                    

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
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
    def UML2_Activity708(self):
        return self.__UML2_Activity708

    @UML2_Activity708.setter
    def UML2_Activity708(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__UML2_Activity708", None)
        self.__UML2_Activity708 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_State707"):
                opp_val = getattr(old_value, "UML2_State707", None)
                if opp_val == self:
                    setattr(old_value, "UML2_State707", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_State707"):
                opp_val = getattr(value, "UML2_State707", None)
                setattr(value, "UML2_State707", self)

    @property
    def Activity324(self):
        return self.__Activity324

    @Activity324.setter
    def Activity324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__Activity324", None)
        self.__Activity324 = value
        
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
    def UML2_Activity705(self):
        return self.__UML2_Activity705

    @UML2_Activity705.setter
    def UML2_Activity705(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__UML2_Activity705", None)
        self.__UML2_Activity705 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_State704"):
                opp_val = getattr(old_value, "UML2_State704", None)
                if opp_val == self:
                    setattr(old_value, "UML2_State704", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_State704"):
                opp_val = getattr(value, "UML2_State704", None)
                setattr(value, "UML2_State704", self)

    @property
    def Activity332(self):
        return self.__Activity332

    @Activity332.setter
    def Activity332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__Activity332", None)
        self.__Activity332 = value
        
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
    def UML2_Activity747(self):
        return self.__UML2_Activity747

    @UML2_Activity747.setter
    def UML2_Activity747(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__UML2_Activity747", None)
        self.__UML2_Activity747 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Transition746"):
                opp_val = getattr(old_value, "UML2_Transition746", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Transition746", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Transition746"):
                opp_val = getattr(value, "UML2_Transition746", None)
                setattr(value, "UML2_Transition746", self)

    @property
    def UML2_Activity711(self):
        return self.__UML2_Activity711

    @UML2_Activity711.setter
    def UML2_Activity711(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__UML2_Activity711", None)
        self.__UML2_Activity711 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_State710"):
                opp_val = getattr(old_value, "UML2_State710", None)
                if opp_val == self:
                    setattr(old_value, "UML2_State710", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_State710"):
                opp_val = getattr(value, "UML2_State710", None)
                setattr(value, "UML2_State710", self)

    @property
    def activity246(self):
        return self.__activity246

    @activity246.setter
    def activity246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__activity246", None)
        self.__activity246 = value if value is not None else set()
        
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
    def UML2_Activity(self):
        return self.__UML2_Activity

    @UML2_Activity.setter
    def UML2_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__UML2_Activity", None)
        self.__UML2_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Action"):
                    opp_val = getattr(item, "UML2_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Action"):
                    opp_val = getattr(item, "UML2_Action", None)
                    
                    setattr(item, "UML2_Action", self)
                    

    @property
    def activityGroup_activity(self):
        return self.__activityGroup_activity

    @activityGroup_activity.setter
    def activityGroup_activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Activity__activityGroup_activity", None)
        self.__activityGroup_activity = value if value is not None else set()
        
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
                    

class Property:

    pass
class UML2_Port(Property):

    def __init__(self, isBehavior: bool, isService: bool, UML2_Port: set["UML2_Interface"] = None, UML2_Port443: "UML2_Port" = None, UML2_Port441: set["UML2_Port"] = None, UML2_Port445: set["UML2_Interface"] = None, UML2_Port448: "UML2_ProtocolStateMachine" = None, UML2_Port451: "UML2_EncapsulatedClassifier" = None, UML2_Port458: "UML2_Trigger" = None, UML2_Port814: "UML2_InvocationAction" = None):
        self.isBehavior = isBehavior
        self.isService = isService
        self.UML2_Port = UML2_Port if UML2_Port is not None else set()
        self.UML2_Port443 = UML2_Port443
        self.UML2_Port441 = UML2_Port441 if UML2_Port441 is not None else set()
        self.UML2_Port445 = UML2_Port445 if UML2_Port445 is not None else set()
        self.UML2_Port448 = UML2_Port448
        self.UML2_Port451 = UML2_Port451
        self.UML2_Port458 = UML2_Port458
        self.UML2_Port814 = UML2_Port814
        
    @property
    def isService(self) -> bool:
        return self.__isService

    @isService.setter
    def isService(self, isService: bool):
        self.__isService = isService

    @property
    def isBehavior(self) -> bool:
        return self.__isBehavior

    @isBehavior.setter
    def isBehavior(self, isBehavior: bool):
        self.__isBehavior = isBehavior

    @property
    def UML2_Port451(self):
        return self.__UML2_Port451

    @UML2_Port451.setter
    def UML2_Port451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port451", None)
        self.__UML2_Port451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_EncapsulatedClassifier"):
                opp_val = getattr(old_value, "UML2_EncapsulatedClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_EncapsulatedClassifier"):
                opp_val = getattr(value, "UML2_EncapsulatedClassifier", None)
                if opp_val is None:
                    setattr(value, "UML2_EncapsulatedClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Port458(self):
        return self.__UML2_Port458

    @UML2_Port458.setter
    def UML2_Port458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port458", None)
        self.__UML2_Port458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Trigger457"):
                opp_val = getattr(old_value, "UML2_Trigger457", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Trigger457"):
                opp_val = getattr(value, "UML2_Trigger457", None)
                if opp_val is None:
                    setattr(value, "UML2_Trigger457", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Port448(self):
        return self.__UML2_Port448

    @UML2_Port448.setter
    def UML2_Port448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port448", None)
        self.__UML2_Port448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ProtocolStateMachine449"):
                opp_val = getattr(old_value, "UML2_ProtocolStateMachine449", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ProtocolStateMachine449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ProtocolStateMachine449"):
                opp_val = getattr(value, "UML2_ProtocolStateMachine449", None)
                setattr(value, "UML2_ProtocolStateMachine449", self)

    @property
    def UML2_Port814(self):
        return self.__UML2_Port814

    @UML2_Port814.setter
    def UML2_Port814(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port814", None)
        self.__UML2_Port814 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InvocationAction813"):
                opp_val = getattr(old_value, "UML2_InvocationAction813", None)
                if opp_val == self:
                    setattr(old_value, "UML2_InvocationAction813", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InvocationAction813"):
                opp_val = getattr(value, "UML2_InvocationAction813", None)
                setattr(value, "UML2_InvocationAction813", self)

    @property
    def UML2_Port(self):
        return self.__UML2_Port

    @UML2_Port.setter
    def UML2_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port", None)
        self.__UML2_Port = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Interface440"):
                    opp_val = getattr(item, "UML2_Interface440", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Interface440", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Interface440"):
                    opp_val = getattr(item, "UML2_Interface440", None)
                    
                    setattr(item, "UML2_Interface440", self)
                    

    @property
    def UML2_Port445(self):
        return self.__UML2_Port445

    @UML2_Port445.setter
    def UML2_Port445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port445", None)
        self.__UML2_Port445 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Interface446"):
                    opp_val = getattr(item, "UML2_Interface446", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Interface446", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Interface446"):
                    opp_val = getattr(item, "UML2_Interface446", None)
                    
                    setattr(item, "UML2_Interface446", self)
                    

    @property
    def UML2_Port441(self):
        return self.__UML2_Port441

    @UML2_Port441.setter
    def UML2_Port441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port441", None)
        self.__UML2_Port441 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Port443"):
                    opp_val = getattr(item, "UML2_Port443", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Port443", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Port443"):
                    opp_val = getattr(item, "UML2_Port443", None)
                    
                    setattr(item, "UML2_Port443", self)
                    

    @property
    def UML2_Port443(self):
        return self.__UML2_Port443

    @UML2_Port443.setter
    def UML2_Port443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Port__UML2_Port443", None)
        self.__UML2_Port443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Port441"):
                opp_val = getattr(old_value, "UML2_Port441", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Port441"):
                opp_val = getattr(value, "UML2_Port441", None)
                if opp_val is None:
                    setattr(value, "UML2_Port441", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_ExtensionEnd(Property):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class PackageImport:

    pass
class Package:

    pass
class UML2_Model(Package):

    def __init__(self, viewpoint: str):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> str:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: str):
        self.__viewpoint = viewpoint

class UML2_Profile(Package):

    pass
class Class:

    pass
class UML2_Component(Class):

    def __init__(self, isIndirectlyInstantiated: bool, Component: "UML2_Realization" = None, UML2_Component863: set["UML2_PackageableElement"] = None, UML2_Component: set["UML2_Interface"] = None, UML2_Component859: set["UML2_Interface"] = None, abstraction: set["UML2_Realization"] = None):
        self.isIndirectlyInstantiated = isIndirectlyInstantiated
        self.Component = Component
        self.UML2_Component863 = UML2_Component863 if UML2_Component863 is not None else set()
        self.UML2_Component = UML2_Component if UML2_Component is not None else set()
        self.UML2_Component859 = UML2_Component859 if UML2_Component859 is not None else set()
        self.abstraction = abstraction if abstraction is not None else set()
        
    @property
    def isIndirectlyInstantiated(self) -> bool:
        return self.__isIndirectlyInstantiated

    @isIndirectlyInstantiated.setter
    def isIndirectlyInstantiated(self, isIndirectlyInstantiated: bool):
        self.__isIndirectlyInstantiated = isIndirectlyInstantiated

    @property
    def abstraction(self):
        return self.__abstraction

    @abstraction.setter
    def abstraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Component__abstraction", None)
        self.__abstraction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Realization"):
                    opp_val = getattr(item, "Realization", None)
                    
                    if opp_val == self:
                        setattr(item, "Realization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Realization"):
                    opp_val = getattr(item, "Realization", None)
                    
                    setattr(item, "Realization", self)
                    

    @property
    def UML2_Component859(self):
        return self.__UML2_Component859

    @UML2_Component859.setter
    def UML2_Component859(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Component__UML2_Component859", None)
        self.__UML2_Component859 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Interface860"):
                    opp_val = getattr(item, "UML2_Interface860", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Interface860", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Interface860"):
                    opp_val = getattr(item, "UML2_Interface860", None)
                    
                    setattr(item, "UML2_Interface860", self)
                    

    @property
    def UML2_Component863(self):
        return self.__UML2_Component863

    @UML2_Component863.setter
    def UML2_Component863(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Component__UML2_Component863", None)
        self.__UML2_Component863 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_PackageableElement864"):
                    opp_val = getattr(item, "UML2_PackageableElement864", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_PackageableElement864", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_PackageableElement864"):
                    opp_val = getattr(item, "UML2_PackageableElement864", None)
                    
                    setattr(item, "UML2_PackageableElement864", self)
                    

    @property
    def UML2_Component(self):
        return self.__UML2_Component

    @UML2_Component.setter
    def UML2_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Component__UML2_Component", None)
        self.__UML2_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Interface857"):
                    opp_val = getattr(item, "UML2_Interface857", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Interface857", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Interface857"):
                    opp_val = getattr(item, "UML2_Interface857", None)
                    
                    setattr(item, "UML2_Interface857", self)
                    

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Component__Component", None)
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

class UML2_AssociationClass(Association, Class):

    pass
class UML2_Stereotype(Class):

    pass
class DirectedRelationship:

    pass
class UML2_ProtocolConformance(DirectedRelationship):

    pass
class UML2_TemplateBinding(DirectedRelationship):

    pass
class DeployedArtifact:

    pass
class Feature:

    pass
class UML2_Connector(Feature):

    def __init__(self, kind: str, UML2_Connector: "UML2_Association" = None, UML2_Connector284: "UML2_Connector" = None, UML2_Connector282: set["UML2_Connector"] = None, UML2_Connector286: set["UML2_ConnectorEnd"] = None, UML2_Connector289: set["UML2_Behavior"] = None, UML2_Connector300: "UML2_StructuredClassifier" = None, UML2_Connector546: "UML2_Message" = None):
        self.kind = kind
        self.UML2_Connector = UML2_Connector
        self.UML2_Connector284 = UML2_Connector284
        self.UML2_Connector282 = UML2_Connector282 if UML2_Connector282 is not None else set()
        self.UML2_Connector286 = UML2_Connector286 if UML2_Connector286 is not None else set()
        self.UML2_Connector289 = UML2_Connector289 if UML2_Connector289 is not None else set()
        self.UML2_Connector300 = UML2_Connector300
        self.UML2_Connector546 = UML2_Connector546
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def UML2_Connector282(self):
        return self.__UML2_Connector282

    @UML2_Connector282.setter
    def UML2_Connector282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Connector__UML2_Connector282", None)
        self.__UML2_Connector282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Connector284"):
                    opp_val = getattr(item, "UML2_Connector284", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Connector284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Connector284"):
                    opp_val = getattr(item, "UML2_Connector284", None)
                    
                    setattr(item, "UML2_Connector284", self)
                    

    @property
    def UML2_Connector300(self):
        return self.__UML2_Connector300

    @UML2_Connector300.setter
    def UML2_Connector300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Connector__UML2_Connector300", None)
        self.__UML2_Connector300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StructuredClassifier299"):
                opp_val = getattr(old_value, "UML2_StructuredClassifier299", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StructuredClassifier299"):
                opp_val = getattr(value, "UML2_StructuredClassifier299", None)
                if opp_val is None:
                    setattr(value, "UML2_StructuredClassifier299", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Connector(self):
        return self.__UML2_Connector

    @UML2_Connector.setter
    def UML2_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Connector__UML2_Connector", None)
        self.__UML2_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association281"):
                opp_val = getattr(old_value, "UML2_Association281", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Association281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association281"):
                opp_val = getattr(value, "UML2_Association281", None)
                setattr(value, "UML2_Association281", self)

    @property
    def UML2_Connector546(self):
        return self.__UML2_Connector546

    @UML2_Connector546.setter
    def UML2_Connector546(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Connector__UML2_Connector546", None)
        self.__UML2_Connector546 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Message"):
                opp_val = getattr(old_value, "UML2_Message", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Message", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Message"):
                opp_val = getattr(value, "UML2_Message", None)
                setattr(value, "UML2_Message", self)

    @property
    def UML2_Connector286(self):
        return self.__UML2_Connector286

    @UML2_Connector286.setter
    def UML2_Connector286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Connector__UML2_Connector286", None)
        self.__UML2_Connector286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ConnectorEnd287"):
                    opp_val = getattr(item, "UML2_ConnectorEnd287", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ConnectorEnd287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ConnectorEnd287"):
                    opp_val = getattr(item, "UML2_ConnectorEnd287", None)
                    
                    setattr(item, "UML2_ConnectorEnd287", self)
                    

    @property
    def UML2_Connector289(self):
        return self.__UML2_Connector289

    @UML2_Connector289.setter
    def UML2_Connector289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Connector__UML2_Connector289", None)
        self.__UML2_Connector289 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Behavior290"):
                    opp_val = getattr(item, "UML2_Behavior290", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Behavior290", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Behavior290"):
                    opp_val = getattr(item, "UML2_Behavior290", None)
                    
                    setattr(item, "UML2_Behavior290", self)
                    

    @property
    def UML2_Connector284(self):
        return self.__UML2_Connector284

    @UML2_Connector284.setter
    def UML2_Connector284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Connector__UML2_Connector284", None)
        self.__UML2_Connector284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Connector282"):
                opp_val = getattr(old_value, "UML2_Connector282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Connector282"):
                opp_val = getattr(value, "UML2_Connector282", None)
                if opp_val is None:
                    setattr(value, "UML2_Connector282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LiteralSpecification:

    pass
class UML2_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UML2_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class UML2_Substitution(Realization):

    pass
class UML2_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: bool, Generalization: "UML2_Classifier" = None, generalization: "UML2_Classifier" = None, UML2_Generalization: "UML2_Classifier" = None, generalization180: set["UML2_GeneralizationSet"] = None, Generalization265: "UML2_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.generalization = generalization
        self.UML2_Generalization = UML2_Generalization
        self.generalization180 = generalization180 if generalization180 is not None else set()
        self.Generalization265 = Generalization265
        
    @property
    def isSubstitutable(self) -> bool:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Generalization__generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier176"):
                opp_val = getattr(old_value, "Classifier176", None)
                if opp_val == self:
                    setattr(old_value, "Classifier176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier176"):
                opp_val = getattr(value, "Classifier176", None)
                setattr(value, "Classifier176", self)

    @property
    def generalization180(self):
        return self.__generalization180

    @generalization180.setter
    def generalization180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Generalization__generalization180", None)
        self.__generalization180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeneralizationSet181"):
                    opp_val = getattr(item, "GeneralizationSet181", None)
                    
                    if opp_val == self:
                        setattr(item, "GeneralizationSet181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeneralizationSet181"):
                    opp_val = getattr(item, "GeneralizationSet181", None)
                    
                    setattr(item, "GeneralizationSet181", self)
                    

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Generalization__Generalization", None)
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
    def UML2_Generalization(self):
        return self.__UML2_Generalization

    @UML2_Generalization.setter
    def UML2_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Generalization__UML2_Generalization", None)
        self.__UML2_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier178"):
                opp_val = getattr(old_value, "UML2_Classifier178", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Classifier178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier178"):
                opp_val = getattr(value, "UML2_Classifier178", None)
                setattr(value, "UML2_Classifier178", self)

    @property
    def Generalization265(self):
        return self.__Generalization265

    @Generalization265.setter
    def Generalization265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Generalization__Generalization265", None)
        self.__Generalization265 = value
        
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

class RedefinableElement:

    pass
class UML2_ActivityNode(RedefinableElement):

    pass
class UML2_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, Feature: "UML2_Classifier" = None, feature: set["UML2_Classifier"] = None):
        self.isStatic = isStatic
        self.Feature = Feature
        self.feature = feature if feature is not None else set()
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    setattr(item, "Classifier", self)
                    

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__Feature", None)
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

class UML2_RedefinableTemplateSignature(RedefinableElement, TemplateSignature):

    pass
class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class UML2_Transition(RedefinableElement):

    def __init__(self, kind: str, Transition: "UML2_Region" = None, Transition719: "UML2_Vertex" = None, Transition722: "UML2_Vertex" = None, transition: "UML2_Region" = None, outgoing732: "UML2_Vertex" = None, incoming735: "UML2_Vertex" = None, UML2_Transition: "UML2_Transition" = None, UML2_Transition737: "UML2_Transition" = None, UML2_Transition740: set["UML2_Trigger"] = None, UML2_Transition743: "UML2_Constraint" = None, UML2_Transition746: "UML2_Activity" = None):
        self.kind = kind
        self.Transition = Transition
        self.Transition719 = Transition719
        self.Transition722 = Transition722
        self.transition = transition
        self.outgoing732 = outgoing732
        self.incoming735 = incoming735
        self.UML2_Transition = UML2_Transition
        self.UML2_Transition737 = UML2_Transition737
        self.UML2_Transition740 = UML2_Transition740 if UML2_Transition740 is not None else set()
        self.UML2_Transition743 = UML2_Transition743
        self.UML2_Transition746 = UML2_Transition746
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region730"):
                opp_val = getattr(old_value, "Region730", None)
                if opp_val == self:
                    setattr(old_value, "Region730", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region730"):
                opp_val = getattr(value, "Region730", None)
                setattr(value, "Region730", self)

    @property
    def UML2_Transition(self):
        return self.__UML2_Transition

    @UML2_Transition.setter
    def UML2_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__UML2_Transition", None)
        self.__UML2_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Transition737"):
                opp_val = getattr(old_value, "UML2_Transition737", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Transition737", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Transition737"):
                opp_val = getattr(value, "UML2_Transition737", None)
                setattr(value, "UML2_Transition737", self)

    @property
    def UML2_Transition737(self):
        return self.__UML2_Transition737

    @UML2_Transition737.setter
    def UML2_Transition737(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__UML2_Transition737", None)
        self.__UML2_Transition737 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Transition"):
                opp_val = getattr(old_value, "UML2_Transition", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Transition"):
                opp_val = getattr(value, "UML2_Transition", None)
                setattr(value, "UML2_Transition", self)

    @property
    def UML2_Transition746(self):
        return self.__UML2_Transition746

    @UML2_Transition746.setter
    def UML2_Transition746(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__UML2_Transition746", None)
        self.__UML2_Transition746 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Activity747"):
                opp_val = getattr(old_value, "UML2_Activity747", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Activity747", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Activity747"):
                opp_val = getattr(value, "UML2_Activity747", None)
                setattr(value, "UML2_Activity747", self)

    @property
    def Transition719(self):
        return self.__Transition719

    @Transition719.setter
    def Transition719(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__Transition719", None)
        self.__Transition719 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source718"):
                opp_val = getattr(old_value, "source718", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source718"):
                opp_val = getattr(value, "source718", None)
                if opp_val is None:
                    setattr(value, "source718", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming735(self):
        return self.__incoming735

    @incoming735.setter
    def incoming735(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__incoming735", None)
        self.__incoming735 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex736"):
                opp_val = getattr(old_value, "Vertex736", None)
                if opp_val == self:
                    setattr(old_value, "Vertex736", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex736"):
                opp_val = getattr(value, "Vertex736", None)
                setattr(value, "Vertex736", self)

    @property
    def UML2_Transition743(self):
        return self.__UML2_Transition743

    @UML2_Transition743.setter
    def UML2_Transition743(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__UML2_Transition743", None)
        self.__UML2_Transition743 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Constraint744"):
                opp_val = getattr(old_value, "UML2_Constraint744", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Constraint744", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Constraint744"):
                opp_val = getattr(value, "UML2_Constraint744", None)
                setattr(value, "UML2_Constraint744", self)

    @property
    def UML2_Transition740(self):
        return self.__UML2_Transition740

    @UML2_Transition740.setter
    def UML2_Transition740(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__UML2_Transition740", None)
        self.__UML2_Transition740 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Trigger741"):
                    opp_val = getattr(item, "UML2_Trigger741", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Trigger741", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Trigger741"):
                    opp_val = getattr(item, "UML2_Trigger741", None)
                    
                    setattr(item, "UML2_Trigger741", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container683"):
                opp_val = getattr(old_value, "container683", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container683"):
                opp_val = getattr(value, "container683", None)
                if opp_val is None:
                    setattr(value, "container683", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition722(self):
        return self.__Transition722

    @Transition722.setter
    def Transition722(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__Transition722", None)
        self.__Transition722 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target721"):
                opp_val = getattr(old_value, "target721", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target721"):
                opp_val = getattr(value, "target721", None)
                if opp_val is None:
                    setattr(value, "target721", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing732(self):
        return self.__outgoing732

    @outgoing732.setter
    def outgoing732(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Transition__outgoing732", None)
        self.__outgoing732 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex733"):
                opp_val = getattr(old_value, "Vertex733", None)
                if opp_val == self:
                    setattr(old_value, "Vertex733", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex733"):
                opp_val = getattr(value, "Vertex733", None)
                setattr(value, "Vertex733", self)

class Type:

    pass
class InstanceSpecification:

    pass
class Classifier:

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    def __init__(self, fileName: str, UML2_Artifact: "UML2_Artifact" = None, UML2_Artifact396: set["UML2_Artifact"] = None, UML2_Artifact399: set["UML2_Manifestation"] = None, UML2_Artifact401: set["UML2_Operation"] = None, UML2_Artifact404: set["UML2_Property"] = None):
        self.fileName = fileName
        self.UML2_Artifact = UML2_Artifact
        self.UML2_Artifact396 = UML2_Artifact396 if UML2_Artifact396 is not None else set()
        self.UML2_Artifact399 = UML2_Artifact399 if UML2_Artifact399 is not None else set()
        self.UML2_Artifact401 = UML2_Artifact401 if UML2_Artifact401 is not None else set()
        self.UML2_Artifact404 = UML2_Artifact404 if UML2_Artifact404 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def UML2_Artifact(self):
        return self.__UML2_Artifact

    @UML2_Artifact.setter
    def UML2_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Artifact__UML2_Artifact", None)
        self.__UML2_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Artifact396"):
                opp_val = getattr(old_value, "UML2_Artifact396", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Artifact396"):
                opp_val = getattr(value, "UML2_Artifact396", None)
                if opp_val is None:
                    setattr(value, "UML2_Artifact396", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Artifact399(self):
        return self.__UML2_Artifact399

    @UML2_Artifact399.setter
    def UML2_Artifact399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Artifact__UML2_Artifact399", None)
        self.__UML2_Artifact399 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Manifestation"):
                    opp_val = getattr(item, "UML2_Manifestation", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Manifestation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Manifestation"):
                    opp_val = getattr(item, "UML2_Manifestation", None)
                    
                    setattr(item, "UML2_Manifestation", self)
                    

    @property
    def UML2_Artifact404(self):
        return self.__UML2_Artifact404

    @UML2_Artifact404.setter
    def UML2_Artifact404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Artifact__UML2_Artifact404", None)
        self.__UML2_Artifact404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property405"):
                    opp_val = getattr(item, "UML2_Property405", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property405", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property405"):
                    opp_val = getattr(item, "UML2_Property405", None)
                    
                    setattr(item, "UML2_Property405", self)
                    

    @property
    def UML2_Artifact396(self):
        return self.__UML2_Artifact396

    @UML2_Artifact396.setter
    def UML2_Artifact396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Artifact__UML2_Artifact396", None)
        self.__UML2_Artifact396 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Artifact"):
                    opp_val = getattr(item, "UML2_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Artifact"):
                    opp_val = getattr(item, "UML2_Artifact", None)
                    
                    setattr(item, "UML2_Artifact", self)
                    

    @property
    def UML2_Artifact401(self):
        return self.__UML2_Artifact401

    @UML2_Artifact401.setter
    def UML2_Artifact401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Artifact__UML2_Artifact401", None)
        self.__UML2_Artifact401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Operation402"):
                    opp_val = getattr(item, "UML2_Operation402", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Operation402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Operation402"):
                    opp_val = getattr(item, "UML2_Operation402", None)
                    
                    setattr(item, "UML2_Operation402", self)
                    

class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_ProfileApplication(PackageImport):

    pass
class UML2_PackageMerge(DirectedRelationship):

    pass
class Namespace:

    pass
class UML2_Region(RedefinableElement, Namespace):

    pass
class UML2_StructuredActivityNode(ActivityGroup, Action, Namespace):

    def __init__(self, mustIsolate: bool, UML2_StructuredActivityNode: "UML2_Activity" = None, StructuredActivityNode: "UML2_ActivityEdge" = None, StructuredActivityNode337: "UML2_ActivityNode" = None, StructuredActivityNode469: "UML2_Variable" = None, scope: set["UML2_Variable"] = None, inStructuredNode: set["UML2_ActivityNode"] = None, inStructuredNode474: set["UML2_ActivityEdge"] = None):
        self.mustIsolate = mustIsolate
        self.UML2_StructuredActivityNode = UML2_StructuredActivityNode
        self.StructuredActivityNode = StructuredActivityNode
        self.StructuredActivityNode337 = StructuredActivityNode337
        self.StructuredActivityNode469 = StructuredActivityNode469
        self.scope = scope if scope is not None else set()
        self.inStructuredNode = inStructuredNode if inStructuredNode is not None else set()
        self.inStructuredNode474 = inStructuredNode474 if inStructuredNode474 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def inStructuredNode(self):
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuredActivityNode__inStructuredNode", None)
        self.__inStructuredNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode472"):
                    opp_val = getattr(item, "ActivityNode472", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode472", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode472"):
                    opp_val = getattr(item, "ActivityNode472", None)
                    
                    setattr(item, "ActivityNode472", self)
                    

    @property
    def StructuredActivityNode337(self):
        return self.__StructuredActivityNode337

    @StructuredActivityNode337.setter
    def StructuredActivityNode337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuredActivityNode__StructuredActivityNode337", None)
        self.__StructuredActivityNode337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedNode"):
                opp_val = getattr(old_value, "containedNode", None)
                if opp_val == self:
                    setattr(old_value, "containedNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedNode"):
                opp_val = getattr(value, "containedNode", None)
                setattr(value, "containedNode", self)

    @property
    def UML2_StructuredActivityNode(self):
        return self.__UML2_StructuredActivityNode

    @UML2_StructuredActivityNode.setter
    def UML2_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuredActivityNode__UML2_StructuredActivityNode", None)
        self.__UML2_StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Activity249"):
                opp_val = getattr(old_value, "UML2_Activity249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Activity249"):
                opp_val = getattr(value, "UML2_Activity249", None)
                if opp_val is None:
                    setattr(value, "UML2_Activity249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inStructuredNode474(self):
        return self.__inStructuredNode474

    @inStructuredNode474.setter
    def inStructuredNode474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuredActivityNode__inStructuredNode474", None)
        self.__inStructuredNode474 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge475"):
                    opp_val = getattr(item, "ActivityEdge475", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge475", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge475"):
                    opp_val = getattr(item, "ActivityEdge475", None)
                    
                    setattr(item, "ActivityEdge475", self)
                    

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuredActivityNode__scope", None)
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
    def StructuredActivityNode(self):
        return self.__StructuredActivityNode

    @StructuredActivityNode.setter
    def StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuredActivityNode__StructuredActivityNode", None)
        self.__StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedEdge"):
                opp_val = getattr(old_value, "containedEdge", None)
                if opp_val == self:
                    setattr(old_value, "containedEdge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedEdge"):
                opp_val = getattr(value, "containedEdge", None)
                setattr(value, "containedEdge", self)

    @property
    def StructuredActivityNode469(self):
        return self.__StructuredActivityNode469

    @StructuredActivityNode469.setter
    def StructuredActivityNode469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuredActivityNode__StructuredActivityNode469", None)
        self.__StructuredActivityNode469 = value
        
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

class UML2_InteractionOperand(InteractionFragment, Namespace):

    pass
class UML2_BehavioralFeature(Feature, Namespace):

    def __init__(self, isAbstract: bool, concurrency: str, UML2_BehavioralFeature: set["UML2_Parameter"] = None, UML2_BehavioralFeature151: set["UML2_Parameter"] = None, UML2_BehavioralFeature154: set["UML2_Parameter"] = None, UML2_BehavioralFeature157: set["UML2_Type"] = None, specification: set["UML2_Behavior"] = None, BehavioralFeature: "UML2_Behavior" = None):
        self.isAbstract = isAbstract
        self.concurrency = concurrency
        self.UML2_BehavioralFeature = UML2_BehavioralFeature if UML2_BehavioralFeature is not None else set()
        self.UML2_BehavioralFeature151 = UML2_BehavioralFeature151 if UML2_BehavioralFeature151 is not None else set()
        self.UML2_BehavioralFeature154 = UML2_BehavioralFeature154 if UML2_BehavioralFeature154 is not None else set()
        self.UML2_BehavioralFeature157 = UML2_BehavioralFeature157 if UML2_BehavioralFeature157 is not None else set()
        self.specification = specification if specification is not None else set()
        self.BehavioralFeature = BehavioralFeature
        
    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_BehavioralFeature154(self):
        return self.__UML2_BehavioralFeature154

    @UML2_BehavioralFeature154.setter
    def UML2_BehavioralFeature154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_BehavioralFeature__UML2_BehavioralFeature154", None)
        self.__UML2_BehavioralFeature154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Parameter155"):
                    opp_val = getattr(item, "UML2_Parameter155", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Parameter155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Parameter155"):
                    opp_val = getattr(item, "UML2_Parameter155", None)
                    
                    setattr(item, "UML2_Parameter155", self)
                    

    @property
    def BehavioralFeature(self):
        return self.__BehavioralFeature

    @BehavioralFeature.setter
    def BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_BehavioralFeature__BehavioralFeature", None)
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
    def UML2_BehavioralFeature157(self):
        return self.__UML2_BehavioralFeature157

    @UML2_BehavioralFeature157.setter
    def UML2_BehavioralFeature157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_BehavioralFeature__UML2_BehavioralFeature157", None)
        self.__UML2_BehavioralFeature157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Type158"):
                    opp_val = getattr(item, "UML2_Type158", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Type158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Type158"):
                    opp_val = getattr(item, "UML2_Type158", None)
                    
                    setattr(item, "UML2_Type158", self)
                    

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_BehavioralFeature__specification", None)
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
    def UML2_BehavioralFeature151(self):
        return self.__UML2_BehavioralFeature151

    @UML2_BehavioralFeature151.setter
    def UML2_BehavioralFeature151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_BehavioralFeature__UML2_BehavioralFeature151", None)
        self.__UML2_BehavioralFeature151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Parameter152"):
                    opp_val = getattr(item, "UML2_Parameter152", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Parameter152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Parameter152"):
                    opp_val = getattr(item, "UML2_Parameter152", None)
                    
                    setattr(item, "UML2_Parameter152", self)
                    

    @property
    def UML2_BehavioralFeature(self):
        return self.__UML2_BehavioralFeature

    @UML2_BehavioralFeature.setter
    def UML2_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_BehavioralFeature__UML2_BehavioralFeature", None)
        self.__UML2_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Parameter149"):
                    opp_val = getattr(item, "UML2_Parameter149", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Parameter149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Parameter149"):
                    opp_val = getattr(item, "UML2_Parameter149", None)
                    
                    setattr(item, "UML2_Parameter149", self)
                    

class UML2_State(RedefinableElement, Vertex, Namespace):

    def __init__(self, isComposite: bool, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, UML2_State: "UML2_ObjectNode" = None, State: "UML2_Region" = None, UML2_State691: "UML2_StateMachine" = None, UML2_State694: set["UML2_ConnectionPointReference"] = None, UML2_State697: "UML2_State" = None, UML2_State695: "UML2_State" = None, UML2_State699: set["UML2_Trigger"] = None, state: set["UML2_Region"] = None, UML2_State704: "UML2_Activity" = None, UML2_State707: "UML2_Activity" = None, UML2_State710: "UML2_Activity" = None, UML2_State713: "UML2_Constraint" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.UML2_State = UML2_State
        self.State = State
        self.UML2_State691 = UML2_State691
        self.UML2_State694 = UML2_State694 if UML2_State694 is not None else set()
        self.UML2_State697 = UML2_State697
        self.UML2_State695 = UML2_State695
        self.UML2_State699 = UML2_State699 if UML2_State699 is not None else set()
        self.state = state if state is not None else set()
        self.UML2_State704 = UML2_State704
        self.UML2_State707 = UML2_State707
        self.UML2_State710 = UML2_State710
        self.UML2_State713 = UML2_State713
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isOrthogonal(self) -> bool:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal

    @property
    def isSubmachineState(self) -> bool:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState

    @property
    def isSimple(self) -> bool:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple

    @property
    def UML2_State704(self):
        return self.__UML2_State704

    @UML2_State704.setter
    def UML2_State704(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State704", None)
        self.__UML2_State704 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Activity705"):
                opp_val = getattr(old_value, "UML2_Activity705", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Activity705", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Activity705"):
                opp_val = getattr(value, "UML2_Activity705", None)
                setattr(value, "UML2_Activity705", self)

    @property
    def UML2_State(self):
        return self.__UML2_State

    @UML2_State.setter
    def UML2_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State", None)
        self.__UML2_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ObjectNode360"):
                opp_val = getattr(old_value, "UML2_ObjectNode360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ObjectNode360"):
                opp_val = getattr(value, "UML2_ObjectNode360", None)
                if opp_val is None:
                    setattr(value, "UML2_ObjectNode360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_State694(self):
        return self.__UML2_State694

    @UML2_State694.setter
    def UML2_State694(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State694", None)
        self.__UML2_State694 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ConnectionPointReference"):
                    opp_val = getattr(item, "UML2_ConnectionPointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ConnectionPointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ConnectionPointReference"):
                    opp_val = getattr(item, "UML2_ConnectionPointReference", None)
                    
                    setattr(item, "UML2_ConnectionPointReference", self)
                    

    @property
    def UML2_State713(self):
        return self.__UML2_State713

    @UML2_State713.setter
    def UML2_State713(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State713", None)
        self.__UML2_State713 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Constraint714"):
                opp_val = getattr(old_value, "UML2_Constraint714", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Constraint714", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Constraint714"):
                opp_val = getattr(value, "UML2_Constraint714", None)
                setattr(value, "UML2_Constraint714", self)

    @property
    def UML2_State697(self):
        return self.__UML2_State697

    @UML2_State697.setter
    def UML2_State697(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State697", None)
        self.__UML2_State697 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_State695"):
                opp_val = getattr(old_value, "UML2_State695", None)
                if opp_val == self:
                    setattr(old_value, "UML2_State695", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_State695"):
                opp_val = getattr(value, "UML2_State695", None)
                setattr(value, "UML2_State695", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__state", None)
        self.__state = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region702"):
                    opp_val = getattr(item, "Region702", None)
                    
                    if opp_val == self:
                        setattr(item, "Region702", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region702"):
                    opp_val = getattr(item, "Region702", None)
                    
                    setattr(item, "Region702", self)
                    

    @property
    def UML2_State695(self):
        return self.__UML2_State695

    @UML2_State695.setter
    def UML2_State695(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State695", None)
        self.__UML2_State695 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_State697"):
                opp_val = getattr(old_value, "UML2_State697", None)
                if opp_val == self:
                    setattr(old_value, "UML2_State697", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_State697"):
                opp_val = getattr(value, "UML2_State697", None)
                setattr(value, "UML2_State697", self)

    @property
    def UML2_State699(self):
        return self.__UML2_State699

    @UML2_State699.setter
    def UML2_State699(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State699", None)
        self.__UML2_State699 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Trigger700"):
                    opp_val = getattr(item, "UML2_Trigger700", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Trigger700", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Trigger700"):
                    opp_val = getattr(item, "UML2_Trigger700", None)
                    
                    setattr(item, "UML2_Trigger700", self)
                    

    @property
    def UML2_State707(self):
        return self.__UML2_State707

    @UML2_State707.setter
    def UML2_State707(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State707", None)
        self.__UML2_State707 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Activity708"):
                opp_val = getattr(old_value, "UML2_Activity708", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Activity708", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Activity708"):
                opp_val = getattr(value, "UML2_Activity708", None)
                setattr(value, "UML2_Activity708", self)

    @property
    def UML2_State710(self):
        return self.__UML2_State710

    @UML2_State710.setter
    def UML2_State710(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State710", None)
        self.__UML2_State710 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Activity711"):
                opp_val = getattr(old_value, "UML2_Activity711", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Activity711", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Activity711"):
                opp_val = getattr(value, "UML2_Activity711", None)
                setattr(value, "UML2_Activity711", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region687"):
                opp_val = getattr(old_value, "region687", None)
                if opp_val == self:
                    setattr(old_value, "region687", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region687"):
                opp_val = getattr(value, "region687", None)
                setattr(value, "region687", self)

    @property
    def UML2_State691(self):
        return self.__UML2_State691

    @UML2_State691.setter
    def UML2_State691(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_State__UML2_State691", None)
        self.__UML2_State691 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StateMachine692"):
                opp_val = getattr(old_value, "UML2_StateMachine692", None)
                if opp_val == self:
                    setattr(old_value, "UML2_StateMachine692", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StateMachine692"):
                opp_val = getattr(value, "UML2_StateMachine692", None)
                setattr(value, "UML2_StateMachine692", self)

class MultiplicityElement:

    pass
class UML2_Pin(MultiplicityElement, ObjectNode):

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class BehavioralFeature:

    pass
class UML2_DataType(Classifier):

    pass
class DeploymentTarget:

    pass
class UML2_Node(DeploymentTarget, Class):

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class UML2_Property(DeploymentTarget, ConnectableElement, StructuralFeature):

    def __init__(self, default: str, isComposite: bool, isDerived: bool, isDerivedUnion: bool, aggregation: str, UML2_Property53: set["UML2_Property"] = None, UML2_Property: "UML2_Class" = None, UML2_Property51: "UML2_Property" = None, UML2_Property49: "UML2_Property" = None, ownedEnd: "UML2_Association" = None, UML2_Property55: "UML2_Property" = None, UML2_Property58: "UML2_Property" = None, UML2_Property56: set["UML2_Property"] = None, ownedAttribute: "UML2_DataType" = None, memberEnd: "UML2_Association" = None, UML2_Property63: "UML2_ValueSpecification" = None, Property: "UML2_Property" = None, associationEnd: set["UML2_Property"] = None, Property69: "UML2_Property" = None, qualifier: "UML2_Property" = None, Property108: "UML2_DataType" = None, UML2_Property123: "UML2_Classifier" = None, Property195: "UML2_Association" = None, Property191: "UML2_Association" = None, UML2_Property292: "UML2_StructuredClassifier" = None, UML2_Property295: "UML2_StructuredClassifier" = None, UML2_Property274: "UML2_ConnectorEnd" = None, UML2_Property278: "UML2_ConnectorEnd" = None, UML2_Property377: "UML2_Interface" = None, UML2_Property405: "UML2_Artifact" = None, UML2_Property463: "UML2_Signal" = None, UML2_Property782: "UML2_LinkEndData" = None, UML2_Property911: "UML2_QualifierValue" = None, UML2_Property919: "UML2_ReadLinkObjectEndAction" = None, UML2_Property930: "UML2_ReadLinkObjectEndQualifierAction" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.aggregation = aggregation
        self.UML2_Property53 = UML2_Property53 if UML2_Property53 is not None else set()
        self.UML2_Property = UML2_Property
        self.UML2_Property51 = UML2_Property51
        self.UML2_Property49 = UML2_Property49
        self.ownedEnd = ownedEnd
        self.UML2_Property55 = UML2_Property55
        self.UML2_Property58 = UML2_Property58
        self.UML2_Property56 = UML2_Property56 if UML2_Property56 is not None else set()
        self.ownedAttribute = ownedAttribute
        self.memberEnd = memberEnd
        self.UML2_Property63 = UML2_Property63
        self.Property = Property
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.Property69 = Property69
        self.qualifier = qualifier
        self.Property108 = Property108
        self.UML2_Property123 = UML2_Property123
        self.Property195 = Property195
        self.Property191 = Property191
        self.UML2_Property292 = UML2_Property292
        self.UML2_Property295 = UML2_Property295
        self.UML2_Property274 = UML2_Property274
        self.UML2_Property278 = UML2_Property278
        self.UML2_Property377 = UML2_Property377
        self.UML2_Property405 = UML2_Property405
        self.UML2_Property463 = UML2_Property463
        self.UML2_Property782 = UML2_Property782
        self.UML2_Property911 = UML2_Property911
        self.UML2_Property919 = UML2_Property919
        self.UML2_Property930 = UML2_Property930
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

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
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def Property69(self):
        return self.__Property69

    @Property69.setter
    def Property69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__Property69", None)
        self.__Property69 = value
        
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
    def UML2_Property292(self):
        return self.__UML2_Property292

    @UML2_Property292.setter
    def UML2_Property292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property292", None)
        self.__UML2_Property292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StructuredClassifier"):
                opp_val = getattr(old_value, "UML2_StructuredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StructuredClassifier"):
                opp_val = getattr(value, "UML2_StructuredClassifier", None)
                if opp_val is None:
                    setattr(value, "UML2_StructuredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property782(self):
        return self.__UML2_Property782

    @UML2_Property782.setter
    def UML2_Property782(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property782", None)
        self.__UML2_Property782 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_LinkEndData781"):
                opp_val = getattr(old_value, "UML2_LinkEndData781", None)
                if opp_val == self:
                    setattr(old_value, "UML2_LinkEndData781", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_LinkEndData781"):
                opp_val = getattr(value, "UML2_LinkEndData781", None)
                setattr(value, "UML2_LinkEndData781", self)

    @property
    def UML2_Property919(self):
        return self.__UML2_Property919

    @UML2_Property919.setter
    def UML2_Property919(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property919", None)
        self.__UML2_Property919 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ReadLinkObjectEndAction918"):
                opp_val = getattr(old_value, "UML2_ReadLinkObjectEndAction918", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ReadLinkObjectEndAction918", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ReadLinkObjectEndAction918"):
                opp_val = getattr(value, "UML2_ReadLinkObjectEndAction918", None)
                setattr(value, "UML2_ReadLinkObjectEndAction918", self)

    @property
    def UML2_Property55(self):
        return self.__UML2_Property55

    @UML2_Property55.setter
    def UML2_Property55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property55", None)
        self.__UML2_Property55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property53"):
                opp_val = getattr(old_value, "UML2_Property53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property53"):
                opp_val = getattr(value, "UML2_Property53", None)
                if opp_val is None:
                    setattr(value, "UML2_Property53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property278(self):
        return self.__UML2_Property278

    @UML2_Property278.setter
    def UML2_Property278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property278", None)
        self.__UML2_Property278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ConnectorEnd277"):
                opp_val = getattr(old_value, "UML2_ConnectorEnd277", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ConnectorEnd277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ConnectorEnd277"):
                opp_val = getattr(value, "UML2_ConnectorEnd277", None)
                setattr(value, "UML2_ConnectorEnd277", self)

    @property
    def UML2_Property56(self):
        return self.__UML2_Property56

    @UML2_Property56.setter
    def UML2_Property56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property56", None)
        self.__UML2_Property56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property58"):
                    opp_val = getattr(item, "UML2_Property58", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property58"):
                    opp_val = getattr(item, "UML2_Property58", None)
                    
                    setattr(item, "UML2_Property58", self)
                    

    @property
    def UML2_Property930(self):
        return self.__UML2_Property930

    @UML2_Property930.setter
    def UML2_Property930(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property930", None)
        self.__UML2_Property930 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ReadLinkObjectEndQualifierAction929"):
                opp_val = getattr(old_value, "UML2_ReadLinkObjectEndQualifierAction929", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ReadLinkObjectEndQualifierAction929", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ReadLinkObjectEndQualifierAction929"):
                opp_val = getattr(value, "UML2_ReadLinkObjectEndQualifierAction929", None)
                setattr(value, "UML2_ReadLinkObjectEndQualifierAction929", self)

    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__qualifier", None)
        self.__qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property69"):
                opp_val = getattr(old_value, "Property69", None)
                if opp_val == self:
                    setattr(old_value, "Property69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property69"):
                opp_val = getattr(value, "Property69", None)
                setattr(value, "Property69", self)

    @property
    def UML2_Property405(self):
        return self.__UML2_Property405

    @UML2_Property405.setter
    def UML2_Property405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property405", None)
        self.__UML2_Property405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Artifact404"):
                opp_val = getattr(old_value, "UML2_Artifact404", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Artifact404"):
                opp_val = getattr(value, "UML2_Artifact404", None)
                if opp_val is None:
                    setattr(value, "UML2_Artifact404", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property377(self):
        return self.__UML2_Property377

    @UML2_Property377.setter
    def UML2_Property377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property377", None)
        self.__UML2_Property377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Interface"):
                opp_val = getattr(old_value, "UML2_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Interface"):
                opp_val = getattr(value, "UML2_Interface", None)
                if opp_val is None:
                    setattr(value, "UML2_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property911(self):
        return self.__UML2_Property911

    @UML2_Property911.setter
    def UML2_Property911(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property911", None)
        self.__UML2_Property911 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_QualifierValue910"):
                opp_val = getattr(old_value, "UML2_QualifierValue910", None)
                if opp_val == self:
                    setattr(old_value, "UML2_QualifierValue910", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_QualifierValue910"):
                opp_val = getattr(value, "UML2_QualifierValue910", None)
                setattr(value, "UML2_QualifierValue910", self)

    @property
    def UML2_Property463(self):
        return self.__UML2_Property463

    @UML2_Property463.setter
    def UML2_Property463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property463", None)
        self.__UML2_Property463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Signal462"):
                opp_val = getattr(old_value, "UML2_Signal462", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Signal462"):
                opp_val = getattr(value, "UML2_Signal462", None)
                if opp_val is None:
                    setattr(value, "UML2_Signal462", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property53(self):
        return self.__UML2_Property53

    @UML2_Property53.setter
    def UML2_Property53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property53", None)
        self.__UML2_Property53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property55"):
                    opp_val = getattr(item, "UML2_Property55", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property55"):
                    opp_val = getattr(item, "UML2_Property55", None)
                    
                    setattr(item, "UML2_Property55", self)
                    

    @property
    def UML2_Property63(self):
        return self.__UML2_Property63

    @UML2_Property63.setter
    def UML2_Property63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property63", None)
        self.__UML2_Property63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ValueSpecification64"):
                opp_val = getattr(old_value, "UML2_ValueSpecification64", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ValueSpecification64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ValueSpecification64"):
                opp_val = getattr(value, "UML2_ValueSpecification64", None)
                setattr(value, "UML2_ValueSpecification64", self)

    @property
    def UML2_Property274(self):
        return self.__UML2_Property274

    @UML2_Property274.setter
    def UML2_Property274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property274", None)
        self.__UML2_Property274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ConnectorEnd"):
                opp_val = getattr(old_value, "UML2_ConnectorEnd", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ConnectorEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ConnectorEnd"):
                opp_val = getattr(value, "UML2_ConnectorEnd", None)
                setattr(value, "UML2_ConnectorEnd", self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__Property", None)
        self.__Property = value
        
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
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__ownedAttribute", None)
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
    def UML2_Property51(self):
        return self.__UML2_Property51

    @UML2_Property51.setter
    def UML2_Property51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property51", None)
        self.__UML2_Property51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property49"):
                opp_val = getattr(old_value, "UML2_Property49", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Property49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property49"):
                opp_val = getattr(value, "UML2_Property49", None)
                setattr(value, "UML2_Property49", self)

    @property
    def Property191(self):
        return self.__Property191

    @Property191.setter
    def Property191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__Property191", None)
        self.__Property191 = value
        
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
    def Property108(self):
        return self.__Property108

    @Property108.setter
    def Property108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__Property108", None)
        self.__Property108 = value
        
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
    def UML2_Property(self):
        return self.__UML2_Property

    @UML2_Property.setter
    def UML2_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property", None)
        self.__UML2_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Class48"):
                opp_val = getattr(old_value, "UML2_Class48", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Class48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Class48"):
                opp_val = getattr(value, "UML2_Class48", None)
                setattr(value, "UML2_Class48", self)

    @property
    def UML2_Property58(self):
        return self.__UML2_Property58

    @UML2_Property58.setter
    def UML2_Property58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property58", None)
        self.__UML2_Property58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property56"):
                opp_val = getattr(old_value, "UML2_Property56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property56"):
                opp_val = getattr(value, "UML2_Property56", None)
                if opp_val is None:
                    setattr(value, "UML2_Property56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property123(self):
        return self.__UML2_Property123

    @UML2_Property123.setter
    def UML2_Property123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property123", None)
        self.__UML2_Property123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier122"):
                opp_val = getattr(old_value, "UML2_Classifier122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier122"):
                opp_val = getattr(value, "UML2_Classifier122", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__ownedEnd", None)
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
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__associationEnd", None)
        self.__associationEnd = value if value is not None else set()
        
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
    def UML2_Property49(self):
        return self.__UML2_Property49

    @UML2_Property49.setter
    def UML2_Property49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property49", None)
        self.__UML2_Property49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property51"):
                opp_val = getattr(old_value, "UML2_Property51", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Property51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property51"):
                opp_val = getattr(value, "UML2_Property51", None)
                setattr(value, "UML2_Property51", self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association61"):
                opp_val = getattr(old_value, "Association61", None)
                if opp_val == self:
                    setattr(old_value, "Association61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association61"):
                opp_val = getattr(value, "Association61", None)
                setattr(value, "Association61", self)

    @property
    def Property195(self):
        return self.__Property195

    @Property195.setter
    def Property195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__Property195", None)
        self.__Property195 = value
        
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
    def UML2_Property295(self):
        return self.__UML2_Property295

    @UML2_Property295.setter
    def UML2_Property295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property295", None)
        self.__UML2_Property295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StructuredClassifier294"):
                opp_val = getattr(old_value, "UML2_StructuredClassifier294", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StructuredClassifier294"):
                opp_val = getattr(value, "UML2_StructuredClassifier294", None)
                if opp_val is None:
                    setattr(value, "UML2_StructuredClassifier294", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PackageableElement:

    pass
class UML2_InformationFlow(PackageableElement, DirectedRelationship):

    pass
class UML2_PrimitiveFunction(PackageableElement):

    def __init__(self, body: str, language: str, UML2_PrimitiveFunction: "UML2_ApplyFunctionAction" = None):
        self.body = body
        self.language = language
        self.UML2_PrimitiveFunction = UML2_PrimitiveFunction
        
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
    def UML2_PrimitiveFunction(self):
        return self.__UML2_PrimitiveFunction

    @UML2_PrimitiveFunction.setter
    def UML2_PrimitiveFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PrimitiveFunction__UML2_PrimitiveFunction", None)
        self.__UML2_PrimitiveFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ApplyFunctionAction"):
                opp_val = getattr(old_value, "UML2_ApplyFunctionAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ApplyFunctionAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ApplyFunctionAction"):
                opp_val = getattr(value, "UML2_ApplyFunctionAction", None)
                setattr(value, "UML2_ApplyFunctionAction", self)

class UML2_Package(PackageableElement, Namespace):

    pass
class UML2_InstanceSpecification(DeploymentTarget, PackageableElement, DeployedArtifact):

    pass
class UML2_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: bool, isDisjoint: bool, GeneralizationSet: "UML2_Classifier" = None, GeneralizationSet181: "UML2_Generalization" = None, powertypeExtent: "UML2_Classifier" = None, generalizationSet: set["UML2_Generalization"] = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.GeneralizationSet = GeneralizationSet
        self.GeneralizationSet181 = GeneralizationSet181
        self.powertypeExtent = powertypeExtent
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        
    @property
    def isDisjoint(self) -> bool:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint

    @property
    def isCovering(self) -> bool:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering

    @property
    def GeneralizationSet181(self):
        return self.__GeneralizationSet181

    @GeneralizationSet181.setter
    def GeneralizationSet181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_GeneralizationSet__GeneralizationSet181", None)
        self.__GeneralizationSet181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization180"):
                opp_val = getattr(old_value, "generalization180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization180"):
                opp_val = getattr(value, "generalization180", None)
                if opp_val is None:
                    setattr(value, "generalization180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_GeneralizationSet__GeneralizationSet", None)
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
        old_value = getattr(self, f"_UML2_GeneralizationSet__powertypeExtent", None)
        self.__powertypeExtent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier263"):
                opp_val = getattr(old_value, "Classifier263", None)
                if opp_val == self:
                    setattr(old_value, "Classifier263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier263"):
                opp_val = getattr(value, "Classifier263", None)
                setattr(value, "Classifier263", self)

    @property
    def generalizationSet(self):
        return self.__generalizationSet

    @generalizationSet.setter
    def generalizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_GeneralizationSet__generalizationSet", None)
        self.__generalizationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization265"):
                    opp_val = getattr(item, "Generalization265", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization265"):
                    opp_val = getattr(item, "Generalization265", None)
                    
                    setattr(item, "Generalization265", self)
                    

class UML2_Type(PackageableElement):

    pass
class UML2_Reception(BehavioralFeature):

    pass
class UML2_Classifier(RedefinableElement, Type, Namespace):

    def __init__(self, isAbstract: bool, UML2_Classifier: "UML2_Class" = None, UML2_Classifier133: "UML2_CollaborationOccurrence" = None, featuringClassifier: set["UML2_Feature"] = None, UML2_Classifier115: set["UML2_NamedElement"] = None, UML2_Classifier119: "UML2_Classifier" = None, UML2_Classifier117: set["UML2_Classifier"] = None, specific: set["UML2_Generalization"] = None, UML2_Classifier122: set["UML2_Property"] = None, UML2_Classifier126: "UML2_Classifier" = None, UML2_Classifier124: set["UML2_Classifier"] = None, substitutingClassifier: set["UML2_Substitution"] = None, powertype: set["UML2_GeneralizationSet"] = None, UML2_Classifier130: set["UML2_UseCase"] = None, subject: set["UML2_UseCase"] = None, UML2_Classifier135: set["UML2_CollaborationOccurrence"] = None, Classifier: "UML2_Feature" = None, UML2_Classifier162: "UML2_InstanceSpecification" = None, UML2_Classifier174: "UML2_RedefinableElement" = None, Classifier176: "UML2_Generalization" = None, UML2_Classifier178: "UML2_Generalization" = None, UML2_Classifier259: "UML2_Substitution" = None, Classifier261: "UML2_Substitution" = None, Classifier263: "UML2_GeneralizationSet" = None, UML2_Classifier267: "UML2_InformationItem" = None, UML2_Classifier272: "UML2_InformationFlow" = None, UML2_Classifier257: "UML2_Realization" = None, UML2_Classifier350: "UML2_Action" = None, UML2_Classifier386: "UML2_Interface" = None, Classifier424: "UML2_UseCase" = None, UML2_Classifier651: "UML2_ExceptionHandler" = None, UML2_Classifier749: "UML2_CreateObjectAction" = None, UML2_Classifier890: "UML2_ReadExtentAction" = None, UML2_Classifier892: "UML2_ReclassifyObjectAction" = None, UML2_Classifier895: "UML2_ReclassifyObjectAction" = None, UML2_Classifier900: "UML2_ReadIsClassifiedObjectAction" = None):
        self.isAbstract = isAbstract
        self.UML2_Classifier = UML2_Classifier
        self.UML2_Classifier133 = UML2_Classifier133
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.UML2_Classifier115 = UML2_Classifier115 if UML2_Classifier115 is not None else set()
        self.UML2_Classifier119 = UML2_Classifier119
        self.UML2_Classifier117 = UML2_Classifier117 if UML2_Classifier117 is not None else set()
        self.specific = specific if specific is not None else set()
        self.UML2_Classifier122 = UML2_Classifier122 if UML2_Classifier122 is not None else set()
        self.UML2_Classifier126 = UML2_Classifier126
        self.UML2_Classifier124 = UML2_Classifier124 if UML2_Classifier124 is not None else set()
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.UML2_Classifier130 = UML2_Classifier130 if UML2_Classifier130 is not None else set()
        self.subject = subject if subject is not None else set()
        self.UML2_Classifier135 = UML2_Classifier135 if UML2_Classifier135 is not None else set()
        self.Classifier = Classifier
        self.UML2_Classifier162 = UML2_Classifier162
        self.UML2_Classifier174 = UML2_Classifier174
        self.Classifier176 = Classifier176
        self.UML2_Classifier178 = UML2_Classifier178
        self.UML2_Classifier259 = UML2_Classifier259
        self.Classifier261 = Classifier261
        self.Classifier263 = Classifier263
        self.UML2_Classifier267 = UML2_Classifier267
        self.UML2_Classifier272 = UML2_Classifier272
        self.UML2_Classifier257 = UML2_Classifier257
        self.UML2_Classifier350 = UML2_Classifier350
        self.UML2_Classifier386 = UML2_Classifier386
        self.Classifier424 = Classifier424
        self.UML2_Classifier651 = UML2_Classifier651
        self.UML2_Classifier749 = UML2_Classifier749
        self.UML2_Classifier890 = UML2_Classifier890
        self.UML2_Classifier892 = UML2_Classifier892
        self.UML2_Classifier895 = UML2_Classifier895
        self.UML2_Classifier900 = UML2_Classifier900
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_Classifier135(self):
        return self.__UML2_Classifier135

    @UML2_Classifier135.setter
    def UML2_Classifier135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier135", None)
        self.__UML2_Classifier135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_CollaborationOccurrence136"):
                    opp_val = getattr(item, "UML2_CollaborationOccurrence136", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_CollaborationOccurrence136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_CollaborationOccurrence136"):
                    opp_val = getattr(item, "UML2_CollaborationOccurrence136", None)
                    
                    setattr(item, "UML2_CollaborationOccurrence136", self)
                    

    @property
    def UML2_Classifier133(self):
        return self.__UML2_Classifier133

    @UML2_Classifier133.setter
    def UML2_Classifier133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier133", None)
        self.__UML2_Classifier133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_CollaborationOccurrence"):
                opp_val = getattr(old_value, "UML2_CollaborationOccurrence", None)
                if opp_val == self:
                    setattr(old_value, "UML2_CollaborationOccurrence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_CollaborationOccurrence"):
                opp_val = getattr(value, "UML2_CollaborationOccurrence", None)
                setattr(value, "UML2_CollaborationOccurrence", self)

    @property
    def UML2_Classifier174(self):
        return self.__UML2_Classifier174

    @UML2_Classifier174.setter
    def UML2_Classifier174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier174", None)
        self.__UML2_Classifier174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_RedefinableElement"):
                opp_val = getattr(old_value, "UML2_RedefinableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_RedefinableElement"):
                opp_val = getattr(value, "UML2_RedefinableElement", None)
                if opp_val is None:
                    setattr(value, "UML2_RedefinableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier130(self):
        return self.__UML2_Classifier130

    @UML2_Classifier130.setter
    def UML2_Classifier130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier130", None)
        self.__UML2_Classifier130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_UseCase"):
                    opp_val = getattr(item, "UML2_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_UseCase"):
                    opp_val = getattr(item, "UML2_UseCase", None)
                    
                    setattr(item, "UML2_UseCase", self)
                    

    @property
    def UML2_Classifier272(self):
        return self.__UML2_Classifier272

    @UML2_Classifier272.setter
    def UML2_Classifier272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier272", None)
        self.__UML2_Classifier272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InformationFlow271"):
                opp_val = getattr(old_value, "UML2_InformationFlow271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InformationFlow271"):
                opp_val = getattr(value, "UML2_InformationFlow271", None)
                if opp_val is None:
                    setattr(value, "UML2_InformationFlow271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__substitutingClassifier", None)
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
    def UML2_Classifier119(self):
        return self.__UML2_Classifier119

    @UML2_Classifier119.setter
    def UML2_Classifier119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier119", None)
        self.__UML2_Classifier119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier117"):
                opp_val = getattr(old_value, "UML2_Classifier117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier117"):
                opp_val = getattr(value, "UML2_Classifier117", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier386(self):
        return self.__UML2_Classifier386

    @UML2_Classifier386.setter
    def UML2_Classifier386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier386", None)
        self.__UML2_Classifier386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Interface385"):
                opp_val = getattr(old_value, "UML2_Interface385", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Interface385"):
                opp_val = getattr(value, "UML2_Interface385", None)
                if opp_val is None:
                    setattr(value, "UML2_Interface385", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier900(self):
        return self.__UML2_Classifier900

    @UML2_Classifier900.setter
    def UML2_Classifier900(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier900", None)
        self.__UML2_Classifier900 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ReadIsClassifiedObjectAction"):
                opp_val = getattr(old_value, "UML2_ReadIsClassifiedObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ReadIsClassifiedObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ReadIsClassifiedObjectAction"):
                opp_val = getattr(value, "UML2_ReadIsClassifiedObjectAction", None)
                setattr(value, "UML2_ReadIsClassifiedObjectAction", self)

    @property
    def UML2_Classifier115(self):
        return self.__UML2_Classifier115

    @UML2_Classifier115.setter
    def UML2_Classifier115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier115", None)
        self.__UML2_Classifier115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_NamedElement116"):
                    opp_val = getattr(item, "UML2_NamedElement116", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_NamedElement116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_NamedElement116"):
                    opp_val = getattr(item, "UML2_NamedElement116", None)
                    
                    setattr(item, "UML2_NamedElement116", self)
                    

    @property
    def UML2_Classifier350(self):
        return self.__UML2_Classifier350

    @UML2_Classifier350.setter
    def UML2_Classifier350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier350", None)
        self.__UML2_Classifier350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Action349"):
                opp_val = getattr(old_value, "UML2_Action349", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Action349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Action349"):
                opp_val = getattr(value, "UML2_Action349", None)
                setattr(value, "UML2_Action349", self)

    @property
    def Classifier176(self):
        return self.__Classifier176

    @Classifier176.setter
    def Classifier176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__Classifier176", None)
        self.__Classifier176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if opp_val == self:
                    setattr(old_value, "generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                setattr(value, "generalization", self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__featuringClassifier", None)
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
    def UML2_Classifier267(self):
        return self.__UML2_Classifier267

    @UML2_Classifier267.setter
    def UML2_Classifier267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier267", None)
        self.__UML2_Classifier267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InformationItem"):
                opp_val = getattr(old_value, "UML2_InformationItem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InformationItem"):
                opp_val = getattr(value, "UML2_InformationItem", None)
                if opp_val is None:
                    setattr(value, "UML2_InformationItem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier117(self):
        return self.__UML2_Classifier117

    @UML2_Classifier117.setter
    def UML2_Classifier117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier117", None)
        self.__UML2_Classifier117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier119"):
                    opp_val = getattr(item, "UML2_Classifier119", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier119"):
                    opp_val = getattr(item, "UML2_Classifier119", None)
                    
                    setattr(item, "UML2_Classifier119", self)
                    

    @property
    def UML2_Classifier178(self):
        return self.__UML2_Classifier178

    @UML2_Classifier178.setter
    def UML2_Classifier178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier178", None)
        self.__UML2_Classifier178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Generalization"):
                opp_val = getattr(old_value, "UML2_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Generalization"):
                opp_val = getattr(value, "UML2_Generalization", None)
                setattr(value, "UML2_Generalization", self)

    @property
    def UML2_Classifier651(self):
        return self.__UML2_Classifier651

    @UML2_Classifier651.setter
    def UML2_Classifier651(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier651", None)
        self.__UML2_Classifier651 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ExceptionHandler650"):
                opp_val = getattr(old_value, "UML2_ExceptionHandler650", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ExceptionHandler650"):
                opp_val = getattr(value, "UML2_ExceptionHandler650", None)
                if opp_val is None:
                    setattr(value, "UML2_ExceptionHandler650", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier892(self):
        return self.__UML2_Classifier892

    @UML2_Classifier892.setter
    def UML2_Classifier892(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier892", None)
        self.__UML2_Classifier892 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ReclassifyObjectAction"):
                opp_val = getattr(old_value, "UML2_ReclassifyObjectAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ReclassifyObjectAction"):
                opp_val = getattr(value, "UML2_ReclassifyObjectAction", None)
                if opp_val is None:
                    setattr(value, "UML2_ReclassifyObjectAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier162(self):
        return self.__UML2_Classifier162

    @UML2_Classifier162.setter
    def UML2_Classifier162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier162", None)
        self.__UML2_Classifier162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InstanceSpecification"):
                opp_val = getattr(old_value, "UML2_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InstanceSpecification"):
                opp_val = getattr(value, "UML2_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "UML2_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier895(self):
        return self.__UML2_Classifier895

    @UML2_Classifier895.setter
    def UML2_Classifier895(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier895", None)
        self.__UML2_Classifier895 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ReclassifyObjectAction894"):
                opp_val = getattr(old_value, "UML2_ReclassifyObjectAction894", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ReclassifyObjectAction894"):
                opp_val = getattr(value, "UML2_ReclassifyObjectAction894", None)
                if opp_val is None:
                    setattr(value, "UML2_ReclassifyObjectAction894", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier126(self):
        return self.__UML2_Classifier126

    @UML2_Classifier126.setter
    def UML2_Classifier126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier126", None)
        self.__UML2_Classifier126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier124"):
                opp_val = getattr(old_value, "UML2_Classifier124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier124"):
                opp_val = getattr(value, "UML2_Classifier124", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier122(self):
        return self.__UML2_Classifier122

    @UML2_Classifier122.setter
    def UML2_Classifier122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier122", None)
        self.__UML2_Classifier122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property123"):
                    opp_val = getattr(item, "UML2_Property123", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property123"):
                    opp_val = getattr(item, "UML2_Property123", None)
                    
                    setattr(item, "UML2_Property123", self)
                    

    @property
    def UML2_Classifier(self):
        return self.__UML2_Classifier

    @UML2_Classifier.setter
    def UML2_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier", None)
        self.__UML2_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Class43"):
                opp_val = getattr(old_value, "UML2_Class43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Class43"):
                opp_val = getattr(value, "UML2_Class43", None)
                if opp_val is None:
                    setattr(value, "UML2_Class43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier261(self):
        return self.__Classifier261

    @Classifier261.setter
    def Classifier261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__Classifier261", None)
        self.__Classifier261 = value
        
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
    def Classifier424(self):
        return self.__Classifier424

    @Classifier424.setter
    def Classifier424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__Classifier424", None)
        self.__Classifier424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCase423"):
                opp_val = getattr(old_value, "useCase423", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCase423"):
                opp_val = getattr(value, "useCase423", None)
                if opp_val is None:
                    setattr(value, "useCase423", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__Classifier", None)
        self.__Classifier = value
        
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
    def UML2_Classifier259(self):
        return self.__UML2_Classifier259

    @UML2_Classifier259.setter
    def UML2_Classifier259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier259", None)
        self.__UML2_Classifier259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Substitution"):
                opp_val = getattr(old_value, "UML2_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Substitution"):
                opp_val = getattr(value, "UML2_Substitution", None)
                setattr(value, "UML2_Substitution", self)

    @property
    def UML2_Classifier749(self):
        return self.__UML2_Classifier749

    @UML2_Classifier749.setter
    def UML2_Classifier749(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier749", None)
        self.__UML2_Classifier749 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_CreateObjectAction"):
                opp_val = getattr(old_value, "UML2_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_CreateObjectAction"):
                opp_val = getattr(value, "UML2_CreateObjectAction", None)
                setattr(value, "UML2_CreateObjectAction", self)

    @property
    def UML2_Classifier890(self):
        return self.__UML2_Classifier890

    @UML2_Classifier890.setter
    def UML2_Classifier890(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier890", None)
        self.__UML2_Classifier890 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ReadExtentAction889"):
                opp_val = getattr(old_value, "UML2_ReadExtentAction889", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ReadExtentAction889", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ReadExtentAction889"):
                opp_val = getattr(value, "UML2_ReadExtentAction889", None)
                setattr(value, "UML2_ReadExtentAction889", self)

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__subject", None)
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
    def UML2_Classifier257(self):
        return self.__UML2_Classifier257

    @UML2_Classifier257.setter
    def UML2_Classifier257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier257", None)
        self.__UML2_Classifier257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Realization"):
                opp_val = getattr(old_value, "UML2_Realization", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Realization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Realization"):
                opp_val = getattr(value, "UML2_Realization", None)
                setattr(value, "UML2_Realization", self)

    @property
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__powertype", None)
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
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__specific", None)
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
    def Classifier263(self):
        return self.__Classifier263

    @Classifier263.setter
    def Classifier263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__Classifier263", None)
        self.__Classifier263 = value
        
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
    def UML2_Classifier124(self):
        return self.__UML2_Classifier124

    @UML2_Classifier124.setter
    def UML2_Classifier124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier124", None)
        self.__UML2_Classifier124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier126"):
                    opp_val = getattr(item, "UML2_Classifier126", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier126"):
                    opp_val = getattr(item, "UML2_Classifier126", None)
                    
                    setattr(item, "UML2_Classifier126", self)
                    

class UML2_Extension(Association):

    def __init__(self, isRequired: bool, Extension: "UML2_Class" = None, extension: "UML2_Class" = None):
        self.isRequired = isRequired
        self.Extension = Extension
        self.extension = extension
        
    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def Extension(self):
        return self.__Extension

    @Extension.setter
    def Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Extension__Extension", None)
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
        old_value = getattr(self, f"_UML2_Extension__extension", None)
        self.__extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class212"):
                opp_val = getattr(old_value, "Class212", None)
                if opp_val == self:
                    setattr(old_value, "Class212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class212"):
                opp_val = getattr(value, "Class212", None)
                setattr(value, "Class212", self)

class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    def __init__(self, isActive: bool, class_: set["UML2_Operation"] = None, UML2_Class: "UML2_Class" = None, UML2_Class39: set["UML2_Class"] = None, metaclass: set["UML2_Extension"] = None, UML2_Class43: set["UML2_Classifier"] = None, UML2_Class45: set["UML2_Reception"] = None, UML2_Class48: "UML2_Property" = None, Class: "UML2_Operation" = None, Class212: "UML2_Extension" = None):
        self.isActive = isActive
        self.class_ = class_ if class_ is not None else set()
        self.UML2_Class = UML2_Class
        self.UML2_Class39 = UML2_Class39 if UML2_Class39 is not None else set()
        self.metaclass = metaclass if metaclass is not None else set()
        self.UML2_Class43 = UML2_Class43 if UML2_Class43 is not None else set()
        self.UML2_Class45 = UML2_Class45 if UML2_Class45 is not None else set()
        self.UML2_Class48 = UML2_Class48
        self.Class = Class
        self.Class212 = Class212
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def UML2_Class39(self):
        return self.__UML2_Class39

    @UML2_Class39.setter
    def UML2_Class39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class39", None)
        self.__UML2_Class39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Class"):
                    opp_val = getattr(item, "UML2_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Class"):
                    opp_val = getattr(item, "UML2_Class", None)
                    
                    setattr(item, "UML2_Class", self)
                    

    @property
    def UML2_Class(self):
        return self.__UML2_Class

    @UML2_Class.setter
    def UML2_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class", None)
        self.__UML2_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Class39"):
                opp_val = getattr(old_value, "UML2_Class39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Class39"):
                opp_val = getattr(value, "UML2_Class39", None)
                if opp_val is None:
                    setattr(value, "UML2_Class39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__class_", None)
        self.__class_ = value if value is not None else set()
        
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
    def UML2_Class43(self):
        return self.__UML2_Class43

    @UML2_Class43.setter
    def UML2_Class43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class43", None)
        self.__UML2_Class43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier"):
                    opp_val = getattr(item, "UML2_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier"):
                    opp_val = getattr(item, "UML2_Classifier", None)
                    
                    setattr(item, "UML2_Classifier", self)
                    

    @property
    def metaclass(self):
        return self.__metaclass

    @metaclass.setter
    def metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__metaclass", None)
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
    def UML2_Class48(self):
        return self.__UML2_Class48

    @UML2_Class48.setter
    def UML2_Class48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class48", None)
        self.__UML2_Class48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property"):
                opp_val = getattr(old_value, "UML2_Property", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property"):
                opp_val = getattr(value, "UML2_Property", None)
                setattr(value, "UML2_Property", self)

    @property
    def Class212(self):
        return self.__Class212

    @Class212.setter
    def Class212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__Class212", None)
        self.__Class212 = value
        
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
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperation"):
                opp_val = getattr(old_value, "ownedOperation", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperation"):
                opp_val = getattr(value, "ownedOperation", None)
                setattr(value, "ownedOperation", self)

    @property
    def UML2_Class45(self):
        return self.__UML2_Class45

    @UML2_Class45.setter
    def UML2_Class45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class45", None)
        self.__UML2_Class45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Reception"):
                    opp_val = getattr(item, "UML2_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Reception"):
                    opp_val = getattr(item, "UML2_Reception", None)
                    
                    setattr(item, "UML2_Reception", self)
                    

class Relationship:

    pass
class UML2_Association(Classifier, Relationship):

    def __init__(self, isDerived: bool, Association: "UML2_Property" = None, Association61: "UML2_Property" = None, UML2_Association: set["UML2_Type"] = None, association: set["UML2_Property"] = None, owningAssociation: set["UML2_Property"] = None, UML2_Association281: "UML2_Connector" = None, UML2_Association793: "UML2_ClearAssociationAction" = None):
        self.isDerived = isDerived
        self.Association = Association
        self.Association61 = Association61
        self.UML2_Association = UML2_Association if UML2_Association is not None else set()
        self.association = association if association is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.UML2_Association281 = UML2_Association281
        self.UML2_Association793 = UML2_Association793
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def UML2_Association(self):
        return self.__UML2_Association

    @UML2_Association.setter
    def UML2_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Association__UML2_Association", None)
        self.__UML2_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Type193"):
                    opp_val = getattr(item, "UML2_Type193", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Type193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Type193"):
                    opp_val = getattr(item, "UML2_Type193", None)
                    
                    setattr(item, "UML2_Type193", self)
                    

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Association__Association", None)
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
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property195"):
                    opp_val = getattr(item, "Property195", None)
                    
                    if opp_val == self:
                        setattr(item, "Property195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property195"):
                    opp_val = getattr(item, "Property195", None)
                    
                    setattr(item, "Property195", self)
                    

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
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
    def UML2_Association793(self):
        return self.__UML2_Association793

    @UML2_Association793.setter
    def UML2_Association793(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Association__UML2_Association793", None)
        self.__UML2_Association793 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ClearAssociationAction792"):
                opp_val = getattr(old_value, "UML2_ClearAssociationAction792", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ClearAssociationAction792", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ClearAssociationAction792"):
                opp_val = getattr(value, "UML2_ClearAssociationAction792", None)
                setattr(value, "UML2_ClearAssociationAction792", self)

    @property
    def UML2_Association281(self):
        return self.__UML2_Association281

    @UML2_Association281.setter
    def UML2_Association281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Association__UML2_Association281", None)
        self.__UML2_Association281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Connector"):
                opp_val = getattr(old_value, "UML2_Connector", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Connector"):
                opp_val = getattr(value, "UML2_Connector", None)
                setattr(value, "UML2_Connector", self)

    @property
    def Association61(self):
        return self.__Association61

    @Association61.setter
    def Association61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Association__Association61", None)
        self.__Association61 = value
        
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

class UML2_DirectedRelationship(Relationship):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    def __init__(self, symbol: str, UML2_Expression: set["UML2_ValueSpecification"] = None):
        self.symbol = symbol
        self.UML2_Expression = UML2_Expression if UML2_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def UML2_Expression(self):
        return self.__UML2_Expression

    @UML2_Expression.setter
    def UML2_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Expression__UML2_Expression", None)
        self.__UML2_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ValueSpecification24"):
                    opp_val = getattr(item, "UML2_ValueSpecification24", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ValueSpecification24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ValueSpecification24"):
                    opp_val = getattr(item, "UML2_ValueSpecification24", None)
                    
                    setattr(item, "UML2_ValueSpecification24", self)
                    

class ParameterableElement:

    pass
class TypedElement:

    pass
class UML2_Variable(MultiplicityElement, TypedElement, ConnectableElement):

    pass
class UML2_Operation(MultiplicityElement, TypedElement, BehavioralFeature, ParameterableElement):

    def __init__(self, isQuery: bool, Operation: "UML2_Class" = None, operation: set["UML2_Parameter"] = None, ownedOperation: "UML2_Class" = None, ownedOperation73: "UML2_DataType" = None, UML2_Operation: set["UML2_Constraint"] = None, UML2_Operation77: set["UML2_Constraint"] = None, UML2_Operation81: "UML2_Operation" = None, UML2_Operation79: set["UML2_Operation"] = None, UML2_Operation83: "UML2_Constraint" = None, Operation87: "UML2_Parameter" = None, Operation111: "UML2_DataType" = None, UML2_Operation380: "UML2_Interface" = None, UML2_Operation402: "UML2_Artifact" = None, UML2_Operation453: "UML2_CallTrigger" = None, UML2_Operation828: "UML2_CallOperationAction" = None, UML2_Operation882: "UML2_ProtocolTransition" = None):
        self.isQuery = isQuery
        self.Operation = Operation
        self.operation = operation if operation is not None else set()
        self.ownedOperation = ownedOperation
        self.ownedOperation73 = ownedOperation73
        self.UML2_Operation = UML2_Operation if UML2_Operation is not None else set()
        self.UML2_Operation77 = UML2_Operation77 if UML2_Operation77 is not None else set()
        self.UML2_Operation81 = UML2_Operation81
        self.UML2_Operation79 = UML2_Operation79 if UML2_Operation79 is not None else set()
        self.UML2_Operation83 = UML2_Operation83
        self.Operation87 = Operation87
        self.Operation111 = Operation111
        self.UML2_Operation380 = UML2_Operation380
        self.UML2_Operation402 = UML2_Operation402
        self.UML2_Operation453 = UML2_Operation453
        self.UML2_Operation828 = UML2_Operation828
        self.UML2_Operation882 = UML2_Operation882
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
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
    def UML2_Operation453(self):
        return self.__UML2_Operation453

    @UML2_Operation453.setter
    def UML2_Operation453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation453", None)
        self.__UML2_Operation453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_CallTrigger"):
                opp_val = getattr(old_value, "UML2_CallTrigger", None)
                if opp_val == self:
                    setattr(old_value, "UML2_CallTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_CallTrigger"):
                opp_val = getattr(value, "UML2_CallTrigger", None)
                setattr(value, "UML2_CallTrigger", self)

    @property
    def UML2_Operation81(self):
        return self.__UML2_Operation81

    @UML2_Operation81.setter
    def UML2_Operation81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation81", None)
        self.__UML2_Operation81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Operation79"):
                opp_val = getattr(old_value, "UML2_Operation79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Operation79"):
                opp_val = getattr(value, "UML2_Operation79", None)
                if opp_val is None:
                    setattr(value, "UML2_Operation79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Operation83(self):
        return self.__UML2_Operation83

    @UML2_Operation83.setter
    def UML2_Operation83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation83", None)
        self.__UML2_Operation83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Constraint84"):
                opp_val = getattr(old_value, "UML2_Constraint84", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Constraint84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Constraint84"):
                opp_val = getattr(value, "UML2_Constraint84", None)
                setattr(value, "UML2_Constraint84", self)

    @property
    def Operation111(self):
        return self.__Operation111

    @Operation111.setter
    def Operation111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__Operation111", None)
        self.__Operation111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype110"):
                opp_val = getattr(old_value, "datatype110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype110"):
                opp_val = getattr(value, "datatype110", None)
                if opp_val is None:
                    setattr(value, "datatype110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Operation77(self):
        return self.__UML2_Operation77

    @UML2_Operation77.setter
    def UML2_Operation77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation77", None)
        self.__UML2_Operation77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Constraint78"):
                    opp_val = getattr(item, "UML2_Constraint78", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Constraint78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Constraint78"):
                    opp_val = getattr(item, "UML2_Constraint78", None)
                    
                    setattr(item, "UML2_Constraint78", self)
                    

    @property
    def UML2_Operation79(self):
        return self.__UML2_Operation79

    @UML2_Operation79.setter
    def UML2_Operation79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation79", None)
        self.__UML2_Operation79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Operation81"):
                    opp_val = getattr(item, "UML2_Operation81", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Operation81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Operation81"):
                    opp_val = getattr(item, "UML2_Operation81", None)
                    
                    setattr(item, "UML2_Operation81", self)
                    

    @property
    def UML2_Operation(self):
        return self.__UML2_Operation

    @UML2_Operation.setter
    def UML2_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation", None)
        self.__UML2_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Constraint"):
                    opp_val = getattr(item, "UML2_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Constraint"):
                    opp_val = getattr(item, "UML2_Constraint", None)
                    
                    setattr(item, "UML2_Constraint", self)
                    

    @property
    def ownedOperation73(self):
        return self.__ownedOperation73

    @ownedOperation73.setter
    def ownedOperation73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__ownedOperation73", None)
        self.__ownedOperation73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType74"):
                opp_val = getattr(old_value, "DataType74", None)
                if opp_val == self:
                    setattr(old_value, "DataType74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType74"):
                opp_val = getattr(value, "DataType74", None)
                setattr(value, "DataType74", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_"):
                opp_val = getattr(old_value, "class_", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_"):
                opp_val = getattr(value, "class_", None)
                if opp_val is None:
                    setattr(value, "class_", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Operation402(self):
        return self.__UML2_Operation402

    @UML2_Operation402.setter
    def UML2_Operation402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation402", None)
        self.__UML2_Operation402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Artifact401"):
                opp_val = getattr(old_value, "UML2_Artifact401", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Artifact401"):
                opp_val = getattr(value, "UML2_Artifact401", None)
                if opp_val is None:
                    setattr(value, "UML2_Artifact401", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def UML2_Operation380(self):
        return self.__UML2_Operation380

    @UML2_Operation380.setter
    def UML2_Operation380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation380", None)
        self.__UML2_Operation380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Interface379"):
                opp_val = getattr(old_value, "UML2_Interface379", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Interface379"):
                opp_val = getattr(value, "UML2_Interface379", None)
                if opp_val is None:
                    setattr(value, "UML2_Interface379", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Operation828(self):
        return self.__UML2_Operation828

    @UML2_Operation828.setter
    def UML2_Operation828(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation828", None)
        self.__UML2_Operation828 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_CallOperationAction"):
                opp_val = getattr(old_value, "UML2_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_CallOperationAction"):
                opp_val = getattr(value, "UML2_CallOperationAction", None)
                setattr(value, "UML2_CallOperationAction", self)

    @property
    def Operation87(self):
        return self.__Operation87

    @Operation87.setter
    def Operation87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__Operation87", None)
        self.__Operation87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedParameter"):
                opp_val = getattr(old_value, "ownedParameter", None)
                if opp_val == self:
                    setattr(old_value, "ownedParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedParameter"):
                opp_val = getattr(value, "ownedParameter", None)
                setattr(value, "ownedParameter", self)

    @property
    def UML2_Operation882(self):
        return self.__UML2_Operation882

    @UML2_Operation882.setter
    def UML2_Operation882(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation882", None)
        self.__UML2_Operation882 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ProtocolTransition881"):
                opp_val = getattr(old_value, "UML2_ProtocolTransition881", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ProtocolTransition881"):
                opp_val = getattr(value, "UML2_ProtocolTransition881", None)
                if opp_val is None:
                    setattr(value, "UML2_ProtocolTransition881", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_StructuralFeature(MultiplicityElement, TypedElement, Feature):

    def __init__(self, isReadOnly: bool, UML2_StructuralFeature: "UML2_Slot" = None, UML2_StructuralFeature766: "UML2_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.UML2_StructuralFeature = UML2_StructuralFeature
        self.UML2_StructuralFeature766 = UML2_StructuralFeature766
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def UML2_StructuralFeature(self):
        return self.__UML2_StructuralFeature

    @UML2_StructuralFeature.setter
    def UML2_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature", None)
        self.__UML2_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Slot170"):
                opp_val = getattr(old_value, "UML2_Slot170", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Slot170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Slot170"):
                opp_val = getattr(value, "UML2_Slot170", None)
                setattr(value, "UML2_Slot170", self)

    @property
    def UML2_StructuralFeature766(self):
        return self.__UML2_StructuralFeature766

    @UML2_StructuralFeature766.setter
    def UML2_StructuralFeature766(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature766", None)
        self.__UML2_StructuralFeature766 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StructuralFeatureAction"):
                opp_val = getattr(old_value, "UML2_StructuralFeatureAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_StructuralFeatureAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StructuralFeatureAction"):
                opp_val = getattr(value, "UML2_StructuralFeatureAction", None)
                setattr(value, "UML2_StructuralFeatureAction", self)

class UML2_ObjectNode(TypedElement, ActivityNode):

    def __init__(self, ordering: str, UML2_ObjectNode: "UML2_ValueSpecification" = None, UML2_ObjectNode360: set["UML2_State"] = None, UML2_ObjectNode362: "UML2_Behavior" = None, UML2_ObjectNode648: "UML2_ExceptionHandler" = None):
        self.ordering = ordering
        self.UML2_ObjectNode = UML2_ObjectNode
        self.UML2_ObjectNode360 = UML2_ObjectNode360 if UML2_ObjectNode360 is not None else set()
        self.UML2_ObjectNode362 = UML2_ObjectNode362
        self.UML2_ObjectNode648 = UML2_ObjectNode648
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def UML2_ObjectNode(self):
        return self.__UML2_ObjectNode

    @UML2_ObjectNode.setter
    def UML2_ObjectNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ObjectNode__UML2_ObjectNode", None)
        self.__UML2_ObjectNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ValueSpecification358"):
                opp_val = getattr(old_value, "UML2_ValueSpecification358", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ValueSpecification358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ValueSpecification358"):
                opp_val = getattr(value, "UML2_ValueSpecification358", None)
                setattr(value, "UML2_ValueSpecification358", self)

    @property
    def UML2_ObjectNode648(self):
        return self.__UML2_ObjectNode648

    @UML2_ObjectNode648.setter
    def UML2_ObjectNode648(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ObjectNode__UML2_ObjectNode648", None)
        self.__UML2_ObjectNode648 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ExceptionHandler647"):
                opp_val = getattr(old_value, "UML2_ExceptionHandler647", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ExceptionHandler647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ExceptionHandler647"):
                opp_val = getattr(value, "UML2_ExceptionHandler647", None)
                setattr(value, "UML2_ExceptionHandler647", self)

    @property
    def UML2_ObjectNode362(self):
        return self.__UML2_ObjectNode362

    @UML2_ObjectNode362.setter
    def UML2_ObjectNode362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ObjectNode__UML2_ObjectNode362", None)
        self.__UML2_ObjectNode362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior363"):
                opp_val = getattr(old_value, "UML2_Behavior363", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Behavior363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior363"):
                opp_val = getattr(value, "UML2_Behavior363", None)
                setattr(value, "UML2_Behavior363", self)

    @property
    def UML2_ObjectNode360(self):
        return self.__UML2_ObjectNode360

    @UML2_ObjectNode360.setter
    def UML2_ObjectNode360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ObjectNode__UML2_ObjectNode360", None)
        self.__UML2_ObjectNode360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_State"):
                    opp_val = getattr(item, "UML2_State", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_State"):
                    opp_val = getattr(item, "UML2_State", None)
                    
                    setattr(item, "UML2_State", self)
                    

class UML2_Behavior(Class):

    def __init__(self, isReentrant: bool, UML2_Behavior: "UML2_OpaqueExpression" = None, Behavior: "UML2_BehavioralFeature" = None, ownedBehavior: "UML2_BehavioredClassifier" = None, UML2_Behavior216: "UML2_Behavior" = None, UML2_Behavior214: set["UML2_Behavior"] = None, method: "UML2_BehavioralFeature" = None, UML2_Behavior219: set["UML2_Parameter"] = None, UML2_Behavior222: set["UML2_Parameter"] = None, UML2_Behavior225: set["UML2_Parameter"] = None, UML2_Behavior228: set["UML2_Constraint"] = None, UML2_Behavior231: set["UML2_Constraint"] = None, UML2_Behavior234: set["UML2_ParameterSet"] = None, Behavior236: "UML2_BehavioredClassifier" = None, UML2_Behavior238: "UML2_BehavioredClassifier" = None, UML2_Behavior290: "UML2_Connector" = None, UML2_Behavior365: "UML2_ObjectFlow" = None, UML2_Behavior368: "UML2_ObjectFlow" = None, UML2_Behavior370: "UML2_DecisionNode" = None, UML2_Behavior363: "UML2_ObjectNode" = None, UML2_Behavior573: "UML2_ExecutionOccurrence" = None, UML2_Behavior833: "UML2_CallBehaviorAction" = None):
        self.isReentrant = isReentrant
        self.UML2_Behavior = UML2_Behavior
        self.Behavior = Behavior
        self.ownedBehavior = ownedBehavior
        self.UML2_Behavior216 = UML2_Behavior216
        self.UML2_Behavior214 = UML2_Behavior214 if UML2_Behavior214 is not None else set()
        self.method = method
        self.UML2_Behavior219 = UML2_Behavior219 if UML2_Behavior219 is not None else set()
        self.UML2_Behavior222 = UML2_Behavior222 if UML2_Behavior222 is not None else set()
        self.UML2_Behavior225 = UML2_Behavior225 if UML2_Behavior225 is not None else set()
        self.UML2_Behavior228 = UML2_Behavior228 if UML2_Behavior228 is not None else set()
        self.UML2_Behavior231 = UML2_Behavior231 if UML2_Behavior231 is not None else set()
        self.UML2_Behavior234 = UML2_Behavior234 if UML2_Behavior234 is not None else set()
        self.Behavior236 = Behavior236
        self.UML2_Behavior238 = UML2_Behavior238
        self.UML2_Behavior290 = UML2_Behavior290
        self.UML2_Behavior365 = UML2_Behavior365
        self.UML2_Behavior368 = UML2_Behavior368
        self.UML2_Behavior370 = UML2_Behavior370
        self.UML2_Behavior363 = UML2_Behavior363
        self.UML2_Behavior573 = UML2_Behavior573
        self.UML2_Behavior833 = UML2_Behavior833
        
    @property
    def isReentrant(self) -> bool:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: bool):
        self.__isReentrant = isReentrant

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__method", None)
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
    def UML2_Behavior573(self):
        return self.__UML2_Behavior573

    @UML2_Behavior573.setter
    def UML2_Behavior573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior573", None)
        self.__UML2_Behavior573 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ExecutionOccurrence"):
                opp_val = getattr(old_value, "UML2_ExecutionOccurrence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ExecutionOccurrence"):
                opp_val = getattr(value, "UML2_ExecutionOccurrence", None)
                if opp_val is None:
                    setattr(value, "UML2_ExecutionOccurrence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Behavior833(self):
        return self.__UML2_Behavior833

    @UML2_Behavior833.setter
    def UML2_Behavior833(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior833", None)
        self.__UML2_Behavior833 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_CallBehaviorAction"):
                opp_val = getattr(old_value, "UML2_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_CallBehaviorAction"):
                opp_val = getattr(value, "UML2_CallBehaviorAction", None)
                setattr(value, "UML2_CallBehaviorAction", self)

    @property
    def UML2_Behavior(self):
        return self.__UML2_Behavior

    @UML2_Behavior.setter
    def UML2_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior", None)
        self.__UML2_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_OpaqueExpression22"):
                opp_val = getattr(old_value, "UML2_OpaqueExpression22", None)
                if opp_val == self:
                    setattr(old_value, "UML2_OpaqueExpression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_OpaqueExpression22"):
                opp_val = getattr(value, "UML2_OpaqueExpression22", None)
                setattr(value, "UML2_OpaqueExpression22", self)

    @property
    def UML2_Behavior214(self):
        return self.__UML2_Behavior214

    @UML2_Behavior214.setter
    def UML2_Behavior214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior214", None)
        self.__UML2_Behavior214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Behavior216"):
                    opp_val = getattr(item, "UML2_Behavior216", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Behavior216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Behavior216"):
                    opp_val = getattr(item, "UML2_Behavior216", None)
                    
                    setattr(item, "UML2_Behavior216", self)
                    

    @property
    def Behavior236(self):
        return self.__Behavior236

    @Behavior236.setter
    def Behavior236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__Behavior236", None)
        self.__Behavior236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "context"):
                opp_val = getattr(old_value, "context", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "context"):
                opp_val = getattr(value, "context", None)
                if opp_val is None:
                    setattr(value, "context", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Behavior219(self):
        return self.__UML2_Behavior219

    @UML2_Behavior219.setter
    def UML2_Behavior219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior219", None)
        self.__UML2_Behavior219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Parameter220"):
                    opp_val = getattr(item, "UML2_Parameter220", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Parameter220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Parameter220"):
                    opp_val = getattr(item, "UML2_Parameter220", None)
                    
                    setattr(item, "UML2_Parameter220", self)
                    

    @property
    def UML2_Behavior363(self):
        return self.__UML2_Behavior363

    @UML2_Behavior363.setter
    def UML2_Behavior363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior363", None)
        self.__UML2_Behavior363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ObjectNode362"):
                opp_val = getattr(old_value, "UML2_ObjectNode362", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ObjectNode362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ObjectNode362"):
                opp_val = getattr(value, "UML2_ObjectNode362", None)
                setattr(value, "UML2_ObjectNode362", self)

    @property
    def UML2_Behavior370(self):
        return self.__UML2_Behavior370

    @UML2_Behavior370.setter
    def UML2_Behavior370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior370", None)
        self.__UML2_Behavior370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_DecisionNode"):
                opp_val = getattr(old_value, "UML2_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "UML2_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_DecisionNode"):
                opp_val = getattr(value, "UML2_DecisionNode", None)
                setattr(value, "UML2_DecisionNode", self)

    @property
    def UML2_Behavior290(self):
        return self.__UML2_Behavior290

    @UML2_Behavior290.setter
    def UML2_Behavior290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior290", None)
        self.__UML2_Behavior290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Connector289"):
                opp_val = getattr(old_value, "UML2_Connector289", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Connector289"):
                opp_val = getattr(value, "UML2_Connector289", None)
                if opp_val is None:
                    setattr(value, "UML2_Connector289", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Behavior231(self):
        return self.__UML2_Behavior231

    @UML2_Behavior231.setter
    def UML2_Behavior231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior231", None)
        self.__UML2_Behavior231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Constraint232"):
                    opp_val = getattr(item, "UML2_Constraint232", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Constraint232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Constraint232"):
                    opp_val = getattr(item, "UML2_Constraint232", None)
                    
                    setattr(item, "UML2_Constraint232", self)
                    

    @property
    def UML2_Behavior238(self):
        return self.__UML2_Behavior238

    @UML2_Behavior238.setter
    def UML2_Behavior238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior238", None)
        self.__UML2_Behavior238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_BehavioredClassifier"):
                opp_val = getattr(old_value, "UML2_BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "UML2_BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_BehavioredClassifier"):
                opp_val = getattr(value, "UML2_BehavioredClassifier", None)
                setattr(value, "UML2_BehavioredClassifier", self)

    @property
    def UML2_Behavior368(self):
        return self.__UML2_Behavior368

    @UML2_Behavior368.setter
    def UML2_Behavior368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior368", None)
        self.__UML2_Behavior368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ObjectFlow367"):
                opp_val = getattr(old_value, "UML2_ObjectFlow367", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ObjectFlow367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ObjectFlow367"):
                opp_val = getattr(value, "UML2_ObjectFlow367", None)
                setattr(value, "UML2_ObjectFlow367", self)

    @property
    def UML2_Behavior228(self):
        return self.__UML2_Behavior228

    @UML2_Behavior228.setter
    def UML2_Behavior228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior228", None)
        self.__UML2_Behavior228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Constraint229"):
                    opp_val = getattr(item, "UML2_Constraint229", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Constraint229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Constraint229"):
                    opp_val = getattr(item, "UML2_Constraint229", None)
                    
                    setattr(item, "UML2_Constraint229", self)
                    

    @property
    def Behavior(self):
        return self.__Behavior

    @Behavior.setter
    def Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__Behavior", None)
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
    def UML2_Behavior216(self):
        return self.__UML2_Behavior216

    @UML2_Behavior216.setter
    def UML2_Behavior216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior216", None)
        self.__UML2_Behavior216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior214"):
                opp_val = getattr(old_value, "UML2_Behavior214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior214"):
                opp_val = getattr(value, "UML2_Behavior214", None)
                if opp_val is None:
                    setattr(value, "UML2_Behavior214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Behavior234(self):
        return self.__UML2_Behavior234

    @UML2_Behavior234.setter
    def UML2_Behavior234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior234", None)
        self.__UML2_Behavior234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ParameterSet"):
                    opp_val = getattr(item, "UML2_ParameterSet", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ParameterSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ParameterSet"):
                    opp_val = getattr(item, "UML2_ParameterSet", None)
                    
                    setattr(item, "UML2_ParameterSet", self)
                    

    @property
    def UML2_Behavior365(self):
        return self.__UML2_Behavior365

    @UML2_Behavior365.setter
    def UML2_Behavior365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior365", None)
        self.__UML2_Behavior365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ObjectFlow"):
                opp_val = getattr(old_value, "UML2_ObjectFlow", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ObjectFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ObjectFlow"):
                opp_val = getattr(value, "UML2_ObjectFlow", None)
                setattr(value, "UML2_ObjectFlow", self)

    @property
    def UML2_Behavior225(self):
        return self.__UML2_Behavior225

    @UML2_Behavior225.setter
    def UML2_Behavior225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior225", None)
        self.__UML2_Behavior225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Parameter226"):
                    opp_val = getattr(item, "UML2_Parameter226", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Parameter226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Parameter226"):
                    opp_val = getattr(item, "UML2_Parameter226", None)
                    
                    setattr(item, "UML2_Parameter226", self)
                    

    @property
    def ownedBehavior(self):
        return self.__ownedBehavior

    @ownedBehavior.setter
    def ownedBehavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__ownedBehavior", None)
        self.__ownedBehavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioredClassifier"):
                opp_val = getattr(old_value, "BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioredClassifier"):
                opp_val = getattr(value, "BehavioredClassifier", None)
                setattr(value, "BehavioredClassifier", self)

    @property
    def UML2_Behavior222(self):
        return self.__UML2_Behavior222

    @UML2_Behavior222.setter
    def UML2_Behavior222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Behavior__UML2_Behavior222", None)
        self.__UML2_Behavior222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Parameter223"):
                    opp_val = getattr(item, "UML2_Parameter223", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Parameter223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Parameter223"):
                    opp_val = getattr(item, "UML2_Parameter223", None)
                    
                    setattr(item, "UML2_Parameter223", self)
                    

class UML2_Parameter(MultiplicityElement, TypedElement, ConnectableElement):

    def __init__(self, default: str, direction: str, isException: bool, isStream: bool, effect: str, UML2_Parameter: "UML2_OpaqueExpression" = None, Parameter: "UML2_Operation" = None, ownedParameter: "UML2_Operation" = None, UML2_Parameter89: "UML2_ValueSpecification" = None, parameter: set["UML2_ParameterSet"] = None, UML2_Parameter149: "UML2_BehavioralFeature" = None, UML2_Parameter152: "UML2_BehavioralFeature" = None, UML2_Parameter155: "UML2_BehavioralFeature" = None, UML2_Parameter220: "UML2_Behavior" = None, UML2_Parameter223: "UML2_Behavior" = None, UML2_Parameter226: "UML2_Behavior" = None, UML2_Parameter373: "UML2_ActivityParameterNode" = None, Parameter852: "UML2_ParameterSet" = None):
        self.default = default
        self.direction = direction
        self.isException = isException
        self.isStream = isStream
        self.effect = effect
        self.UML2_Parameter = UML2_Parameter
        self.Parameter = Parameter
        self.ownedParameter = ownedParameter
        self.UML2_Parameter89 = UML2_Parameter89
        self.parameter = parameter if parameter is not None else set()
        self.UML2_Parameter149 = UML2_Parameter149
        self.UML2_Parameter152 = UML2_Parameter152
        self.UML2_Parameter155 = UML2_Parameter155
        self.UML2_Parameter220 = UML2_Parameter220
        self.UML2_Parameter223 = UML2_Parameter223
        self.UML2_Parameter226 = UML2_Parameter226
        self.UML2_Parameter373 = UML2_Parameter373
        self.Parameter852 = Parameter852
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def isException(self) -> bool:
        return self.__isException

    @isException.setter
    def isException(self, isException: bool):
        self.__isException = isException

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def isStream(self) -> bool:
        return self.__isStream

    @isStream.setter
    def isStream(self, isStream: bool):
        self.__isStream = isStream

    @property
    def UML2_Parameter220(self):
        return self.__UML2_Parameter220

    @UML2_Parameter220.setter
    def UML2_Parameter220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter220", None)
        self.__UML2_Parameter220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior219"):
                opp_val = getattr(old_value, "UML2_Behavior219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior219"):
                opp_val = getattr(value, "UML2_Behavior219", None)
                if opp_val is None:
                    setattr(value, "UML2_Behavior219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedParameter(self):
        return self.__ownedParameter

    @ownedParameter.setter
    def ownedParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__ownedParameter", None)
        self.__ownedParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation87"):
                opp_val = getattr(old_value, "Operation87", None)
                if opp_val == self:
                    setattr(old_value, "Operation87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation87"):
                opp_val = getattr(value, "Operation87", None)
                setattr(value, "Operation87", self)

    @property
    def UML2_Parameter89(self):
        return self.__UML2_Parameter89

    @UML2_Parameter89.setter
    def UML2_Parameter89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter89", None)
        self.__UML2_Parameter89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ValueSpecification90"):
                opp_val = getattr(old_value, "UML2_ValueSpecification90", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ValueSpecification90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ValueSpecification90"):
                opp_val = getattr(value, "UML2_ValueSpecification90", None)
                setattr(value, "UML2_ValueSpecification90", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__parameter", None)
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
    def UML2_Parameter155(self):
        return self.__UML2_Parameter155

    @UML2_Parameter155.setter
    def UML2_Parameter155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter155", None)
        self.__UML2_Parameter155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_BehavioralFeature154"):
                opp_val = getattr(old_value, "UML2_BehavioralFeature154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_BehavioralFeature154"):
                opp_val = getattr(value, "UML2_BehavioralFeature154", None)
                if opp_val is None:
                    setattr(value, "UML2_BehavioralFeature154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Parameter(self):
        return self.__UML2_Parameter

    @UML2_Parameter.setter
    def UML2_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter", None)
        self.__UML2_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_OpaqueExpression"):
                opp_val = getattr(old_value, "UML2_OpaqueExpression", None)
                if opp_val == self:
                    setattr(old_value, "UML2_OpaqueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_OpaqueExpression"):
                opp_val = getattr(value, "UML2_OpaqueExpression", None)
                setattr(value, "UML2_OpaqueExpression", self)

    @property
    def UML2_Parameter152(self):
        return self.__UML2_Parameter152

    @UML2_Parameter152.setter
    def UML2_Parameter152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter152", None)
        self.__UML2_Parameter152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_BehavioralFeature151"):
                opp_val = getattr(old_value, "UML2_BehavioralFeature151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_BehavioralFeature151"):
                opp_val = getattr(value, "UML2_BehavioralFeature151", None)
                if opp_val is None:
                    setattr(value, "UML2_BehavioralFeature151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Parameter373(self):
        return self.__UML2_Parameter373

    @UML2_Parameter373.setter
    def UML2_Parameter373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter373", None)
        self.__UML2_Parameter373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ActivityParameterNode"):
                opp_val = getattr(old_value, "UML2_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ActivityParameterNode"):
                opp_val = getattr(value, "UML2_ActivityParameterNode", None)
                setattr(value, "UML2_ActivityParameterNode", self)

    @property
    def UML2_Parameter223(self):
        return self.__UML2_Parameter223

    @UML2_Parameter223.setter
    def UML2_Parameter223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter223", None)
        self.__UML2_Parameter223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior222"):
                opp_val = getattr(old_value, "UML2_Behavior222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior222"):
                opp_val = getattr(value, "UML2_Behavior222", None)
                if opp_val is None:
                    setattr(value, "UML2_Behavior222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Parameter149(self):
        return self.__UML2_Parameter149

    @UML2_Parameter149.setter
    def UML2_Parameter149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter149", None)
        self.__UML2_Parameter149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_BehavioralFeature"):
                opp_val = getattr(old_value, "UML2_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_BehavioralFeature"):
                opp_val = getattr(value, "UML2_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "UML2_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation"):
                opp_val = getattr(old_value, "operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation"):
                opp_val = getattr(value, "operation", None)
                if opp_val is None:
                    setattr(value, "operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Parameter226(self):
        return self.__UML2_Parameter226

    @UML2_Parameter226.setter
    def UML2_Parameter226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter226", None)
        self.__UML2_Parameter226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior225"):
                opp_val = getattr(old_value, "UML2_Behavior225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior225"):
                opp_val = getattr(value, "UML2_Behavior225", None)
                if opp_val is None:
                    setattr(value, "UML2_Behavior225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameter852(self):
        return self.__Parameter852

    @Parameter852.setter
    def Parameter852(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__Parameter852", None)
        self.__Parameter852 = value
        
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

class ValueSpecification:

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_Duration(ValueSpecification):

    def __init__(self, firstTime: bool, UML2_Duration: set["UML2_NamedElement"] = None, UML2_Duration846: "UML2_DurationObservationAction" = None):
        self.firstTime = firstTime
        self.UML2_Duration = UML2_Duration if UML2_Duration is not None else set()
        self.UML2_Duration846 = UML2_Duration846
        
    @property
    def firstTime(self) -> bool:
        return self.__firstTime

    @firstTime.setter
    def firstTime(self, firstTime: bool):
        self.__firstTime = firstTime

    @property
    def UML2_Duration(self):
        return self.__UML2_Duration

    @UML2_Duration.setter
    def UML2_Duration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Duration__UML2_Duration", None)
        self.__UML2_Duration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_NamedElement837"):
                    opp_val = getattr(item, "UML2_NamedElement837", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_NamedElement837", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_NamedElement837"):
                    opp_val = getattr(item, "UML2_NamedElement837", None)
                    
                    setattr(item, "UML2_NamedElement837", self)
                    

    @property
    def UML2_Duration846(self):
        return self.__UML2_Duration846

    @UML2_Duration846.setter
    def UML2_Duration846(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Duration__UML2_Duration846", None)
        self.__UML2_Duration846 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_DurationObservationAction"):
                opp_val = getattr(old_value, "UML2_DurationObservationAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_DurationObservationAction"):
                opp_val = getattr(value, "UML2_DurationObservationAction", None)
                if opp_val is None:
                    setattr(value, "UML2_DurationObservationAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_TimeExpression(ValueSpecification):

    def __init__(self, firstTime: bool, UML2_TimeExpression: "UML2_NamedElement" = None, UML2_TimeExpression839: "UML2_TimeObservationAction" = None):
        self.firstTime = firstTime
        self.UML2_TimeExpression = UML2_TimeExpression
        self.UML2_TimeExpression839 = UML2_TimeExpression839
        
    @property
    def firstTime(self) -> bool:
        return self.__firstTime

    @firstTime.setter
    def firstTime(self, firstTime: bool):
        self.__firstTime = firstTime

    @property
    def UML2_TimeExpression(self):
        return self.__UML2_TimeExpression

    @UML2_TimeExpression.setter
    def UML2_TimeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_TimeExpression__UML2_TimeExpression", None)
        self.__UML2_TimeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_NamedElement835"):
                opp_val = getattr(old_value, "UML2_NamedElement835", None)
                if opp_val == self:
                    setattr(old_value, "UML2_NamedElement835", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_NamedElement835"):
                opp_val = getattr(value, "UML2_NamedElement835", None)
                setattr(value, "UML2_NamedElement835", self)

    @property
    def UML2_TimeExpression839(self):
        return self.__UML2_TimeExpression839

    @UML2_TimeExpression839.setter
    def UML2_TimeExpression839(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_TimeExpression__UML2_TimeExpression839", None)
        self.__UML2_TimeExpression839 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_TimeObservationAction"):
                opp_val = getattr(old_value, "UML2_TimeObservationAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_TimeObservationAction"):
                opp_val = getattr(value, "UML2_TimeObservationAction", None)
                if opp_val is None:
                    setattr(value, "UML2_TimeObservationAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    def __init__(self, bodies: str, language: str, UML2_OpaqueExpression: "UML2_Parameter" = None, UML2_OpaqueExpression22: "UML2_Behavior" = None, UML2_OpaqueExpression254: "UML2_Abstraction" = None, UML2_OpaqueExpression539: "UML2_Lifeline" = None):
        self.bodies = bodies
        self.language = language
        self.UML2_OpaqueExpression = UML2_OpaqueExpression
        self.UML2_OpaqueExpression22 = UML2_OpaqueExpression22
        self.UML2_OpaqueExpression254 = UML2_OpaqueExpression254
        self.UML2_OpaqueExpression539 = UML2_OpaqueExpression539
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def bodies(self) -> str:
        return self.__bodies

    @bodies.setter
    def bodies(self, bodies: str):
        self.__bodies = bodies

    @property
    def UML2_OpaqueExpression(self):
        return self.__UML2_OpaqueExpression

    @UML2_OpaqueExpression.setter
    def UML2_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_OpaqueExpression__UML2_OpaqueExpression", None)
        self.__UML2_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Parameter"):
                opp_val = getattr(old_value, "UML2_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Parameter"):
                opp_val = getattr(value, "UML2_Parameter", None)
                setattr(value, "UML2_Parameter", self)

    @property
    def UML2_OpaqueExpression539(self):
        return self.__UML2_OpaqueExpression539

    @UML2_OpaqueExpression539.setter
    def UML2_OpaqueExpression539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_OpaqueExpression__UML2_OpaqueExpression539", None)
        self.__UML2_OpaqueExpression539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Lifeline538"):
                opp_val = getattr(old_value, "UML2_Lifeline538", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Lifeline538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Lifeline538"):
                opp_val = getattr(value, "UML2_Lifeline538", None)
                setattr(value, "UML2_Lifeline538", self)

    @property
    def UML2_OpaqueExpression254(self):
        return self.__UML2_OpaqueExpression254

    @UML2_OpaqueExpression254.setter
    def UML2_OpaqueExpression254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_OpaqueExpression__UML2_OpaqueExpression254", None)
        self.__UML2_OpaqueExpression254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Abstraction"):
                opp_val = getattr(old_value, "UML2_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Abstraction"):
                opp_val = getattr(value, "UML2_Abstraction", None)
                setattr(value, "UML2_Abstraction", self)

    @property
    def UML2_OpaqueExpression22(self):
        return self.__UML2_OpaqueExpression22

    @UML2_OpaqueExpression22.setter
    def UML2_OpaqueExpression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_OpaqueExpression__UML2_OpaqueExpression22", None)
        self.__UML2_OpaqueExpression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior"):
                opp_val = getattr(old_value, "UML2_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior"):
                opp_val = getattr(value, "UML2_Behavior", None)
                setattr(value, "UML2_Behavior", self)

class UML2_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "UML2_Namespace" = None, UML2_PackageImport207: "UML2_Profile" = None, UML2_PackageImport: "UML2_Package" = None, packageImport: "UML2_Namespace" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.UML2_PackageImport207 = UML2_PackageImport207
        self.UML2_PackageImport = UML2_PackageImport
        self.packageImport = packageImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def UML2_PackageImport(self):
        return self.__UML2_PackageImport

    @UML2_PackageImport.setter
    def UML2_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageImport__UML2_PackageImport", None)
        self.__UML2_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Package187"):
                opp_val = getattr(old_value, "UML2_Package187", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Package187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Package187"):
                opp_val = getattr(value, "UML2_Package187", None)
                setattr(value, "UML2_Package187", self)

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageImport__PackageImport", None)
        self.__PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "importingNamespace19"):
                opp_val = getattr(old_value, "importingNamespace19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "importingNamespace19"):
                opp_val = getattr(value, "importingNamespace19", None)
                if opp_val is None:
                    setattr(value, "importingNamespace19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace189"):
                opp_val = getattr(old_value, "Namespace189", None)
                if opp_val == self:
                    setattr(old_value, "Namespace189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace189"):
                opp_val = getattr(value, "Namespace189", None)
                setattr(value, "Namespace189", self)

    @property
    def UML2_PackageImport207(self):
        return self.__UML2_PackageImport207

    @UML2_PackageImport207.setter
    def UML2_PackageImport207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageImport__UML2_PackageImport207", None)
        self.__UML2_PackageImport207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Profile206"):
                opp_val = getattr(old_value, "UML2_Profile206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Profile206"):
                opp_val = getattr(value, "UML2_Profile206", None)
                if opp_val is None:
                    setattr(value, "UML2_Profile206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, ElementImport: "UML2_Namespace" = None, UML2_ElementImport: "UML2_PackageableElement" = None, elementImport: "UML2_Namespace" = None, UML2_ElementImport204: "UML2_Profile" = None):
        self.visibility = visibility
        self.alias = alias
        self.ElementImport = ElementImport
        self.UML2_ElementImport = UML2_ElementImport
        self.elementImport = elementImport
        self.UML2_ElementImport204 = UML2_ElementImport204
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def UML2_ElementImport204(self):
        return self.__UML2_ElementImport204

    @UML2_ElementImport204.setter
    def UML2_ElementImport204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ElementImport__UML2_ElementImport204", None)
        self.__UML2_ElementImport204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Profile203"):
                opp_val = getattr(old_value, "UML2_Profile203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Profile203"):
                opp_val = getattr(value, "UML2_Profile203", None)
                if opp_val is None:
                    setattr(value, "UML2_Profile203", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_ElementImport(self):
        return self.__UML2_ElementImport

    @UML2_ElementImport.setter
    def UML2_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ElementImport__UML2_ElementImport", None)
        self.__UML2_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_PackageableElement183"):
                opp_val = getattr(old_value, "UML2_PackageableElement183", None)
                if opp_val == self:
                    setattr(old_value, "UML2_PackageableElement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_PackageableElement183"):
                opp_val = getattr(value, "UML2_PackageableElement183", None)
                setattr(value, "UML2_PackageableElement183", self)

    @property
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace185"):
                opp_val = getattr(old_value, "Namespace185", None)
                if opp_val == self:
                    setattr(old_value, "Namespace185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace185"):
                opp_val = getattr(value, "Namespace185", None)
                setattr(value, "Namespace185", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ElementImport__ElementImport", None)
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

class UML2_Constraint(PackageableElement):

    pass
class NamedElement:

    pass
class UML2_Extend(DirectedRelationship, NamedElement):

    pass
class UML2_Message(NamedElement):

    def __init__(self, messageKind: str, messageSort: str, Message: "UML2_Interaction" = None, sendMessage: "UML2_MessageEnd" = None, UML2_Message: "UML2_Connector" = None, message: "UML2_Interaction" = None, UML2_Message550: "UML2_NamedElement" = None, UML2_Message553: set["UML2_ValueSpecification"] = None, receiveMessage: "UML2_MessageEnd" = None, Message559: "UML2_MessageEnd" = None, Message561: "UML2_MessageEnd" = None):
        self.messageKind = messageKind
        self.messageSort = messageSort
        self.Message = Message
        self.sendMessage = sendMessage
        self.UML2_Message = UML2_Message
        self.message = message
        self.UML2_Message550 = UML2_Message550
        self.UML2_Message553 = UML2_Message553 if UML2_Message553 is not None else set()
        self.receiveMessage = receiveMessage
        self.Message559 = Message559
        self.Message561 = Message561
        
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
    def receiveMessage(self):
        return self.__receiveMessage

    @receiveMessage.setter
    def receiveMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__receiveMessage", None)
        self.__receiveMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageEnd"):
                opp_val = getattr(old_value, "MessageEnd", None)
                if opp_val == self:
                    setattr(old_value, "MessageEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageEnd"):
                opp_val = getattr(value, "MessageEnd", None)
                setattr(value, "MessageEnd", self)

    @property
    def Message559(self):
        return self.__Message559

    @Message559.setter
    def Message559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__Message559", None)
        self.__Message559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receiveEvent"):
                opp_val = getattr(old_value, "receiveEvent", None)
                if opp_val == self:
                    setattr(old_value, "receiveEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receiveEvent"):
                opp_val = getattr(value, "receiveEvent", None)
                setattr(value, "receiveEvent", self)

    @property
    def Message561(self):
        return self.__Message561

    @Message561.setter
    def Message561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__Message561", None)
        self.__Message561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sendEvent"):
                opp_val = getattr(old_value, "sendEvent", None)
                if opp_val == self:
                    setattr(old_value, "sendEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sendEvent"):
                opp_val = getattr(value, "sendEvent", None)
                setattr(value, "sendEvent", self)

    @property
    def UML2_Message553(self):
        return self.__UML2_Message553

    @UML2_Message553.setter
    def UML2_Message553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__UML2_Message553", None)
        self.__UML2_Message553 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_ValueSpecification554"):
                    opp_val = getattr(item, "UML2_ValueSpecification554", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_ValueSpecification554", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_ValueSpecification554"):
                    opp_val = getattr(item, "UML2_ValueSpecification554", None)
                    
                    setattr(item, "UML2_ValueSpecification554", self)
                    

    @property
    def sendMessage(self):
        return self.__sendMessage

    @sendMessage.setter
    def sendMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__sendMessage", None)
        self.__sendMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageEnd544"):
                opp_val = getattr(old_value, "MessageEnd544", None)
                if opp_val == self:
                    setattr(old_value, "MessageEnd544", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageEnd544"):
                opp_val = getattr(value, "MessageEnd544", None)
                setattr(value, "MessageEnd544", self)

    @property
    def UML2_Message550(self):
        return self.__UML2_Message550

    @UML2_Message550.setter
    def UML2_Message550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__UML2_Message550", None)
        self.__UML2_Message550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_NamedElement551"):
                opp_val = getattr(old_value, "UML2_NamedElement551", None)
                if opp_val == self:
                    setattr(old_value, "UML2_NamedElement551", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_NamedElement551"):
                opp_val = getattr(value, "UML2_NamedElement551", None)
                setattr(value, "UML2_NamedElement551", self)

    @property
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__Message", None)
        self.__Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction522"):
                opp_val = getattr(old_value, "interaction522", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction522"):
                opp_val = getattr(value, "interaction522", None)
                if opp_val is None:
                    setattr(value, "interaction522", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Message(self):
        return self.__UML2_Message

    @UML2_Message.setter
    def UML2_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__UML2_Message", None)
        self.__UML2_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Connector546"):
                opp_val = getattr(old_value, "UML2_Connector546", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Connector546", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Connector546"):
                opp_val = getattr(value, "UML2_Connector546", None)
                setattr(value, "UML2_Connector546", self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Message__message", None)
        self.__message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interaction548"):
                opp_val = getattr(old_value, "Interaction548", None)
                if opp_val == self:
                    setattr(old_value, "Interaction548", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interaction548"):
                opp_val = getattr(value, "Interaction548", None)
                setattr(value, "Interaction548", self)

class UML2_TypedElement(NamedElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_ActivityPartition(ActivityGroup, NamedElement):

    def __init__(self, isDimension: bool, isExternal: bool, ActivityPartition: "UML2_ActivityEdge" = None, ActivityPartition340: "UML2_ActivityNode" = None, inPartition: set["UML2_ActivityEdge"] = None, inPartition628: set["UML2_ActivityNode"] = None, ActivityPartition632: "UML2_ActivityPartition" = None, superPartition: set["UML2_ActivityPartition"] = None, ActivityPartition635: "UML2_ActivityPartition" = None, subgroup: "UML2_ActivityPartition" = None, UML2_ActivityPartition: "UML2_Element" = None):
        self.isDimension = isDimension
        self.isExternal = isExternal
        self.ActivityPartition = ActivityPartition
        self.ActivityPartition340 = ActivityPartition340
        self.inPartition = inPartition if inPartition is not None else set()
        self.inPartition628 = inPartition628 if inPartition628 is not None else set()
        self.ActivityPartition632 = ActivityPartition632
        self.superPartition = superPartition if superPartition is not None else set()
        self.ActivityPartition635 = ActivityPartition635
        self.subgroup = subgroup
        self.UML2_ActivityPartition = UML2_ActivityPartition
        
    @property
    def isDimension(self) -> bool:
        return self.__isDimension

    @isDimension.setter
    def isDimension(self, isDimension: bool):
        self.__isDimension = isDimension

    @property
    def isExternal(self) -> bool:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: bool):
        self.__isExternal = isExternal

    @property
    def ActivityPartition632(self):
        return self.__ActivityPartition632

    @ActivityPartition632.setter
    def ActivityPartition632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__ActivityPartition632", None)
        self.__ActivityPartition632 = value
        
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
    def inPartition(self):
        return self.__inPartition

    @inPartition.setter
    def inPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__inPartition", None)
        self.__inPartition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge626"):
                    opp_val = getattr(item, "ActivityEdge626", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge626", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge626"):
                    opp_val = getattr(item, "ActivityEdge626", None)
                    
                    setattr(item, "ActivityEdge626", self)
                    

    @property
    def ActivityPartition(self):
        return self.__ActivityPartition

    @ActivityPartition.setter
    def ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__ActivityPartition", None)
        self.__ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedEdge315"):
                opp_val = getattr(old_value, "containedEdge315", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedEdge315"):
                opp_val = getattr(value, "containedEdge315", None)
                if opp_val is None:
                    setattr(value, "containedEdge315", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityPartition340(self):
        return self.__ActivityPartition340

    @ActivityPartition340.setter
    def ActivityPartition340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__ActivityPartition340", None)
        self.__ActivityPartition340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedNode339"):
                opp_val = getattr(old_value, "containedNode339", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedNode339"):
                opp_val = getattr(value, "containedNode339", None)
                if opp_val is None:
                    setattr(value, "containedNode339", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subgroup(self):
        return self.__subgroup

    @subgroup.setter
    def subgroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__subgroup", None)
        self.__subgroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityPartition635"):
                opp_val = getattr(old_value, "ActivityPartition635", None)
                if opp_val == self:
                    setattr(old_value, "ActivityPartition635", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityPartition635"):
                opp_val = getattr(value, "ActivityPartition635", None)
                setattr(value, "ActivityPartition635", self)

    @property
    def UML2_ActivityPartition(self):
        return self.__UML2_ActivityPartition

    @UML2_ActivityPartition.setter
    def UML2_ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__UML2_ActivityPartition", None)
        self.__UML2_ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Element637"):
                opp_val = getattr(old_value, "UML2_Element637", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Element637", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Element637"):
                opp_val = getattr(value, "UML2_Element637", None)
                setattr(value, "UML2_Element637", self)

    @property
    def inPartition628(self):
        return self.__inPartition628

    @inPartition628.setter
    def inPartition628(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__inPartition628", None)
        self.__inPartition628 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode629"):
                    opp_val = getattr(item, "ActivityNode629", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode629", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode629"):
                    opp_val = getattr(item, "ActivityNode629", None)
                    
                    setattr(item, "ActivityNode629", self)
                    

    @property
    def ActivityPartition635(self):
        return self.__ActivityPartition635

    @ActivityPartition635.setter
    def ActivityPartition635(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__ActivityPartition635", None)
        self.__ActivityPartition635 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subgroup"):
                opp_val = getattr(old_value, "subgroup", None)
                if opp_val == self:
                    setattr(old_value, "subgroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subgroup"):
                opp_val = getattr(value, "subgroup", None)
                setattr(value, "subgroup", self)

    @property
    def superPartition(self):
        return self.__superPartition

    @superPartition.setter
    def superPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ActivityPartition__superPartition", None)
        self.__superPartition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityPartition632"):
                    opp_val = getattr(item, "ActivityPartition632", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityPartition632", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityPartition632"):
                    opp_val = getattr(item, "ActivityPartition632", None)
                    
                    setattr(item, "ActivityPartition632", self)
                    

class UML2_Trigger(NamedElement):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool, UML2_RedefinableElement: set["UML2_Classifier"] = None):
        self.isLeaf = isLeaf
        self.UML2_RedefinableElement = UML2_RedefinableElement if UML2_RedefinableElement is not None else set()
        
    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

    @property
    def UML2_RedefinableElement(self):
        return self.__UML2_RedefinableElement

    @UML2_RedefinableElement.setter
    def UML2_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_RedefinableElement__UML2_RedefinableElement", None)
        self.__UML2_RedefinableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier174"):
                    opp_val = getattr(item, "UML2_Classifier174", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier174"):
                    opp_val = getattr(item, "UML2_Classifier174", None)
                    
                    setattr(item, "UML2_Classifier174", self)
                    

class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Include(DirectedRelationship, NamedElement):

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class UML2_PackageableElement(NamedElement, ParameterableElement):

    def __init__(self, packageableElement_visibility: str, UML2_PackageableElement: "UML2_Namespace" = None, UML2_PackageableElement100: "UML2_Package" = None, UML2_PackageableElement183: "UML2_ElementImport" = None, UML2_PackageableElement408: "UML2_Manifestation" = None, UML2_PackageableElement864: "UML2_Component" = None, UML2_PackageableElement871: "UML2_DeploymentTarget" = None):
        self.packageableElement_visibility = packageableElement_visibility
        self.UML2_PackageableElement = UML2_PackageableElement
        self.UML2_PackageableElement100 = UML2_PackageableElement100
        self.UML2_PackageableElement183 = UML2_PackageableElement183
        self.UML2_PackageableElement408 = UML2_PackageableElement408
        self.UML2_PackageableElement864 = UML2_PackageableElement864
        self.UML2_PackageableElement871 = UML2_PackageableElement871
        
    @property
    def packageableElement_visibility(self) -> str:
        return self.__packageableElement_visibility

    @packageableElement_visibility.setter
    def packageableElement_visibility(self, packageableElement_visibility: str):
        self.__packageableElement_visibility = packageableElement_visibility

    @property
    def UML2_PackageableElement(self):
        return self.__UML2_PackageableElement

    @UML2_PackageableElement.setter
    def UML2_PackageableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageableElement__UML2_PackageableElement", None)
        self.__UML2_PackageableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Namespace16"):
                opp_val = getattr(old_value, "UML2_Namespace16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Namespace16"):
                opp_val = getattr(value, "UML2_Namespace16", None)
                if opp_val is None:
                    setattr(value, "UML2_Namespace16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_PackageableElement408(self):
        return self.__UML2_PackageableElement408

    @UML2_PackageableElement408.setter
    def UML2_PackageableElement408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageableElement__UML2_PackageableElement408", None)
        self.__UML2_PackageableElement408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Manifestation407"):
                opp_val = getattr(old_value, "UML2_Manifestation407", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Manifestation407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Manifestation407"):
                opp_val = getattr(value, "UML2_Manifestation407", None)
                setattr(value, "UML2_Manifestation407", self)

    @property
    def UML2_PackageableElement100(self):
        return self.__UML2_PackageableElement100

    @UML2_PackageableElement100.setter
    def UML2_PackageableElement100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageableElement__UML2_PackageableElement100", None)
        self.__UML2_PackageableElement100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Package"):
                opp_val = getattr(old_value, "UML2_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Package"):
                opp_val = getattr(value, "UML2_Package", None)
                if opp_val is None:
                    setattr(value, "UML2_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_PackageableElement183(self):
        return self.__UML2_PackageableElement183

    @UML2_PackageableElement183.setter
    def UML2_PackageableElement183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageableElement__UML2_PackageableElement183", None)
        self.__UML2_PackageableElement183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ElementImport"):
                opp_val = getattr(old_value, "UML2_ElementImport", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ElementImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ElementImport"):
                opp_val = getattr(value, "UML2_ElementImport", None)
                setattr(value, "UML2_ElementImport", self)

    @property
    def UML2_PackageableElement864(self):
        return self.__UML2_PackageableElement864

    @UML2_PackageableElement864.setter
    def UML2_PackageableElement864(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageableElement__UML2_PackageableElement864", None)
        self.__UML2_PackageableElement864 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Component863"):
                opp_val = getattr(old_value, "UML2_Component863", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Component863"):
                opp_val = getattr(value, "UML2_Component863", None)
                if opp_val is None:
                    setattr(value, "UML2_Component863", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_PackageableElement871(self):
        return self.__UML2_PackageableElement871

    @UML2_PackageableElement871.setter
    def UML2_PackageableElement871(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_PackageableElement__UML2_PackageableElement871", None)
        self.__UML2_PackageableElement871 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_DeploymentTarget"):
                opp_val = getattr(old_value, "UML2_DeploymentTarget", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_DeploymentTarget"):
                opp_val = getattr(value, "UML2_DeploymentTarget", None)
                if opp_val is None:
                    setattr(value, "UML2_DeploymentTarget", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_ConnectableElement(NamedElement, ParameterableElement):

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_Dependency(PackageableElement, DirectedRelationship):

    pass
class TemplateableElement:

    pass
class UML2_StringExpression(TemplateableElement):

    pass
class UML2_NamedElement(TemplateableElement):

    def __init__(self, name: str, qualifiedName: str, visibility: str, UML2_NamedElement13: "UML2_Namespace" = None, client: set["UML2_Dependency"] = None, UML2_NamedElement: "UML2_StringExpression" = None, UML2_NamedElement116: "UML2_Classifier" = None, NamedElement: "UML2_Dependency" = None, UML2_NamedElement252: "UML2_Dependency" = None, UML2_NamedElement551: "UML2_Message" = None, UML2_NamedElement835: "UML2_TimeExpression" = None, UML2_NamedElement837: "UML2_Duration" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.visibility = visibility
        self.UML2_NamedElement13 = UML2_NamedElement13
        self.client = client if client is not None else set()
        self.UML2_NamedElement = UML2_NamedElement
        self.UML2_NamedElement116 = UML2_NamedElement116
        self.NamedElement = NamedElement
        self.UML2_NamedElement252 = UML2_NamedElement252
        self.UML2_NamedElement551 = UML2_NamedElement551
        self.UML2_NamedElement835 = UML2_NamedElement835
        self.UML2_NamedElement837 = UML2_NamedElement837
        
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
    def UML2_NamedElement835(self):
        return self.__UML2_NamedElement835

    @UML2_NamedElement835.setter
    def UML2_NamedElement835(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement835", None)
        self.__UML2_NamedElement835 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_TimeExpression"):
                opp_val = getattr(old_value, "UML2_TimeExpression", None)
                if opp_val == self:
                    setattr(old_value, "UML2_TimeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_TimeExpression"):
                opp_val = getattr(value, "UML2_TimeExpression", None)
                setattr(value, "UML2_TimeExpression", self)

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__client", None)
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
    def UML2_NamedElement837(self):
        return self.__UML2_NamedElement837

    @UML2_NamedElement837.setter
    def UML2_NamedElement837(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement837", None)
        self.__UML2_NamedElement837 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Duration"):
                opp_val = getattr(old_value, "UML2_Duration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Duration"):
                opp_val = getattr(value, "UML2_Duration", None)
                if opp_val is None:
                    setattr(value, "UML2_Duration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__NamedElement", None)
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
    def UML2_NamedElement116(self):
        return self.__UML2_NamedElement116

    @UML2_NamedElement116.setter
    def UML2_NamedElement116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement116", None)
        self.__UML2_NamedElement116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier115"):
                opp_val = getattr(old_value, "UML2_Classifier115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier115"):
                opp_val = getattr(value, "UML2_Classifier115", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_NamedElement13(self):
        return self.__UML2_NamedElement13

    @UML2_NamedElement13.setter
    def UML2_NamedElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement13", None)
        self.__UML2_NamedElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Namespace"):
                opp_val = getattr(old_value, "UML2_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Namespace"):
                opp_val = getattr(value, "UML2_Namespace", None)
                if opp_val is None:
                    setattr(value, "UML2_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_NamedElement(self):
        return self.__UML2_NamedElement

    @UML2_NamedElement.setter
    def UML2_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement", None)
        self.__UML2_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StringExpression"):
                opp_val = getattr(old_value, "UML2_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "UML2_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StringExpression"):
                opp_val = getattr(value, "UML2_StringExpression", None)
                setattr(value, "UML2_StringExpression", self)

    @property
    def UML2_NamedElement252(self):
        return self.__UML2_NamedElement252

    @UML2_NamedElement252.setter
    def UML2_NamedElement252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement252", None)
        self.__UML2_NamedElement252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Dependency"):
                opp_val = getattr(old_value, "UML2_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Dependency"):
                opp_val = getattr(value, "UML2_Dependency", None)
                if opp_val is None:
                    setattr(value, "UML2_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_NamedElement551(self):
        return self.__UML2_NamedElement551

    @UML2_NamedElement551.setter
    def UML2_NamedElement551(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement551", None)
        self.__UML2_NamedElement551 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Message550"):
                opp_val = getattr(old_value, "UML2_Message550", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Message550", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Message550"):
                opp_val = getattr(value, "UML2_Message550", None)
                setattr(value, "UML2_Message550", self)

class UML2_ValueSpecification(TypedElement, ParameterableElement):

    pass
class Element:

    pass
class UML2_Slot(Element):

    pass
class UML2_Clause(Element):

    pass
class UML2_ParameterableElement(Element):

    pass
class UML2_TemplateableElement(Element):

    pass
class UML2_LinkEndData(Element):

    pass
class UML2_ExceptionHandler(Element):

    pass
class UML2_TemplateParameterSubstitution(Element):

    pass
class UML2_TemplateSignature(Element):

    pass
class UML2_TemplateParameter(Element):

    pass
class UML2_Relationship(Element):

    pass
class UML2_ActivityGroup(Element):

    pass
class UML2_QualifierValue(Element):

    pass
class UML2_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, lower: int, upper: str, UML2_MultiplicityElement: "UML2_ValueSpecification" = None, UML2_MultiplicityElement8: "UML2_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.UML2_MultiplicityElement = UML2_MultiplicityElement
        self.UML2_MultiplicityElement8 = UML2_MultiplicityElement8
        
    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def UML2_MultiplicityElement(self):
        return self.__UML2_MultiplicityElement

    @UML2_MultiplicityElement.setter
    def UML2_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_MultiplicityElement__UML2_MultiplicityElement", None)
        self.__UML2_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ValueSpecification"):
                opp_val = getattr(old_value, "UML2_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ValueSpecification"):
                opp_val = getattr(value, "UML2_ValueSpecification", None)
                setattr(value, "UML2_ValueSpecification", self)

    @property
    def UML2_MultiplicityElement8(self):
        return self.__UML2_MultiplicityElement8

    @UML2_MultiplicityElement8.setter
    def UML2_MultiplicityElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_MultiplicityElement__UML2_MultiplicityElement8", None)
        self.__UML2_MultiplicityElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_ValueSpecification9"):
                opp_val = getattr(old_value, "UML2_ValueSpecification9", None)
                if opp_val == self:
                    setattr(old_value, "UML2_ValueSpecification9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_ValueSpecification9"):
                opp_val = getattr(value, "UML2_ValueSpecification9", None)
                setattr(value, "UML2_ValueSpecification9", self)

class UML2_Comment(TemplateableElement):

    def __init__(self, body: str, UML2_Comment: "UML2_Element" = None, UML2_Comment26: set["UML2_Element"] = None, UML2_Comment29: "UML2_StringExpression" = None):
        self.body = body
        self.UML2_Comment = UML2_Comment
        self.UML2_Comment26 = UML2_Comment26 if UML2_Comment26 is not None else set()
        self.UML2_Comment29 = UML2_Comment29
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def UML2_Comment29(self):
        return self.__UML2_Comment29

    @UML2_Comment29.setter
    def UML2_Comment29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Comment__UML2_Comment29", None)
        self.__UML2_Comment29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StringExpression30"):
                opp_val = getattr(old_value, "UML2_StringExpression30", None)
                if opp_val == self:
                    setattr(old_value, "UML2_StringExpression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StringExpression30"):
                opp_val = getattr(value, "UML2_StringExpression30", None)
                setattr(value, "UML2_StringExpression30", self)

    @property
    def UML2_Comment(self):
        return self.__UML2_Comment

    @UML2_Comment.setter
    def UML2_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Comment__UML2_Comment", None)
        self.__UML2_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Element"):
                opp_val = getattr(old_value, "UML2_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Element"):
                opp_val = getattr(value, "UML2_Element", None)
                if opp_val is None:
                    setattr(value, "UML2_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Comment26(self):
        return self.__UML2_Comment26

    @UML2_Comment26.setter
    def UML2_Comment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Comment__UML2_Comment26", None)
        self.__UML2_Comment26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Element27"):
                    opp_val = getattr(item, "UML2_Element27", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Element27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Element27"):
                    opp_val = getattr(item, "UML2_Element27", None)
                    
                    setattr(item, "UML2_Element27", self)
                    

class UML2_Element(ABC):

    pass
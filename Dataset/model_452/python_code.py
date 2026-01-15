from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterEffectKind(Enum):
    update = "update"
    read = "read"
    delete = "delete"
    create = "create"
class MessageKind(Enum):
    found = "found"
    lost = "lost"
    unknown = "unknown"
    complete = "complete"
class ExpansionKind(Enum):
    stream = "stream"
    parallel = "parallel"
    iterative = "iterative"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class ConnectorKind(Enum):
    delegation = "delegation"
    assembly = "assembly"
class CallConcurrencyKind(Enum):
    guarded = "guarded"
    concurrent = "concurrent"
    sequential = "sequential"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class InteractionOperator(Enum):
    ignore = "ignore"
    neg = "neg"
    critical = "critical"
    consider = "consider"
    par = "par"
    opt = "opt"
    loop = "loop"
    alt = "alt"
    break = "break"
    assert = "assert"
    strict = "strict"
    seq = "seq"
class PseudostateKind(Enum):
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    choice = "choice"
    join = "join"
    exitPoint = "exitPoint"
    terminate = "terminate"
    fork = "fork"
    junction = "junction"
    initial = "initial"
    entryPoint = "entryPoint"
class ObjectNodeOrderingKind(Enum):
    FIFO = "FIFO"
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
class VisibilityKind(Enum):
    package = "package"
    private = "private"
    protected = "protected"
    public = "public"
class MessageSort(Enum):
    synchSignal = "synchSignal"
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
class AggregationKind(Enum):
    composite = "composite"
    none = "none"
    shared = "shared"


############################################
# Definition of Classes
############################################

class Artifact:

    pass
class CreateLinkAction:

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction):

    pass
class AcceptEventAction:

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction):

    pass
class Node:

    pass
class UML2WithID_ExecutionEnvironment(Node):

    pass
class UML2WithID_Device(Node):

    pass
class UML2WithID_DeploymentSpecification(Artifact):

    def __init__(self, deploymentLocation: str, executionLocation: str, UML2WithID_DeploymentSpecification: "UML2WithID_Deployment" = None):
        self.deploymentLocation = deploymentLocation
        self.executionLocation = executionLocation
        self.UML2WithID_DeploymentSpecification = UML2WithID_DeploymentSpecification
        
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
    def UML2WithID_DeploymentSpecification(self):
        return self.__UML2WithID_DeploymentSpecification

    @UML2WithID_DeploymentSpecification.setter
    def UML2WithID_DeploymentSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_DeploymentSpecification__UML2WithID_DeploymentSpecification", None)
        self.__UML2WithID_DeploymentSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Deployment868"):
                opp_val = getattr(old_value, "UML2WithID_Deployment868", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Deployment868"):
                opp_val = getattr(value, "UML2WithID_Deployment868", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Deployment868", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transition:

    pass
class UML2WithID_ProtocolTransition(Transition):

    pass
class StateMachine:

    pass
class CentralBufferNode:

    pass
class UML2WithID_DataStoreNode(CentralBufferNode):

    pass
class CallAction:

    pass
class UML2WithID_CallBehaviorAction(CallAction):

    pass
class UML2WithID_CallOperationAction(CallAction):

    pass
class IntervalConstraint:

    pass
class UML2WithID_DurationConstraint(IntervalConstraint):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint):

    pass
class Interval:

    pass
class UML2WithID_TimeInterval(Interval):

    pass
class UML2WithID_DurationInterval(Interval):

    pass
class WriteVariableAction:

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction):

    def __init__(self, isReplaceAll: bool, UML2WithID_AddVariableValueAction: "UML2WithID_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2WithID_AddVariableValueAction = UML2WithID_AddVariableValueAction
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2WithID_AddVariableValueAction(self):
        return self.__UML2WithID_AddVariableValueAction

    @UML2WithID_AddVariableValueAction.setter
    def UML2WithID_AddVariableValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_AddVariableValueAction__UML2WithID_AddVariableValueAction", None)
        self.__UML2WithID_AddVariableValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InputPin800"):
                opp_val = getattr(old_value, "UML2WithID_InputPin800", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_InputPin800", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InputPin800"):
                opp_val = getattr(value, "UML2WithID_InputPin800", None)
                setattr(value, "UML2WithID_InputPin800", self)

class InvocationAction:

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction):

    pass
class UML2WithID_SendObjectAction(InvocationAction):

    pass
class UML2WithID_SendSignalAction(InvocationAction):

    pass
class UML2WithID_CallAction(InvocationAction):

    def __init__(self, isSynchronous: bool, UML2WithID_CallAction: set["UML2WithID_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.UML2WithID_CallAction = UML2WithID_CallAction if UML2WithID_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> bool:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: bool):
        self.__isSynchronous = isSynchronous

    @property
    def UML2WithID_CallAction(self):
        return self.__UML2WithID_CallAction

    @UML2WithID_CallAction.setter
    def UML2WithID_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_CallAction__UML2WithID_CallAction", None)
        self.__UML2WithID_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_OutputPin809"):
                    opp_val = getattr(item, "UML2WithID_OutputPin809", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_OutputPin809", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_OutputPin809"):
                    opp_val = getattr(item, "UML2WithID_OutputPin809", None)
                    
                    setattr(item, "UML2WithID_OutputPin809", self)
                    

class LinkAction:

    pass
class UML2WithID_ReadLinkAction(LinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, isReplaceAll: bool, UML2WithID_AddStructuralFeatureValueAction: "UML2WithID_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2WithID_AddStructuralFeatureValueAction = UML2WithID_AddStructuralFeatureValueAction
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2WithID_AddStructuralFeatureValueAction(self):
        return self.__UML2WithID_AddStructuralFeatureValueAction

    @UML2WithID_AddStructuralFeatureValueAction.setter
    def UML2WithID_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_AddStructuralFeatureValueAction__UML2WithID_AddStructuralFeatureValueAction", None)
        self.__UML2WithID_AddStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InputPin775"):
                opp_val = getattr(old_value, "UML2WithID_InputPin775", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_InputPin775", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InputPin775"):
                opp_val = getattr(value, "UML2WithID_InputPin775", None)
                setattr(value, "UML2WithID_InputPin775", self)

class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class VariableAction:

    pass
class UML2WithID_ClearVariableAction(VariableAction):

    pass
class UML2WithID_WriteVariableAction(VariableAction):

    pass
class UML2WithID_ReadVariableAction(VariableAction):

    pass
class UML2WithID_WriteLinkAction(LinkAction):

    pass
class WriteLinkAction:

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction):

    pass
class LinkEndData:

    pass
class UML2WithID_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: bool, UML2WithID_LinkEndCreationData: "UML2WithID_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2WithID_LinkEndCreationData = UML2WithID_LinkEndCreationData
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2WithID_LinkEndCreationData(self):
        return self.__UML2WithID_LinkEndCreationData

    @UML2WithID_LinkEndCreationData.setter
    def UML2WithID_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LinkEndCreationData__UML2WithID_LinkEndCreationData", None)
        self.__UML2WithID_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InputPin788"):
                opp_val = getattr(old_value, "UML2WithID_InputPin788", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_InputPin788", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InputPin788"):
                opp_val = getattr(value, "UML2WithID_InputPin788", None)
                setattr(value, "UML2WithID_InputPin788", self)

class State:

    pass
class UML2WithID_FinalState(State):

    pass
class StructuralFeatureAction:

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class Vertex:

    pass
class UML2WithID_ConnectionPointReference(Vertex):

    pass
class Constraint:

    pass
class UML2WithID_IntervalConstraint(Constraint):

    pass
class UML2WithID_InteractionConstraint(Constraint):

    pass
class InteractionOccurrence:

    pass
class UML2WithID_Pseudostate(Vertex):

    def __init__(self, kind: str, UML2WithID_Pseudostate: "UML2WithID_StateMachine" = None, UML2WithID_Pseudostate725: "UML2WithID_ConnectionPointReference" = None, UML2WithID_Pseudostate728: "UML2WithID_ConnectionPointReference" = None):
        self.kind = kind
        self.UML2WithID_Pseudostate = UML2WithID_Pseudostate
        self.UML2WithID_Pseudostate725 = UML2WithID_Pseudostate725
        self.UML2WithID_Pseudostate728 = UML2WithID_Pseudostate728
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def UML2WithID_Pseudostate(self):
        return self.__UML2WithID_Pseudostate

    @UML2WithID_Pseudostate.setter
    def UML2WithID_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Pseudostate__UML2WithID_Pseudostate", None)
        self.__UML2WithID_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StateMachine"):
                opp_val = getattr(old_value, "UML2WithID_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StateMachine"):
                opp_val = getattr(value, "UML2WithID_StateMachine", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Pseudostate728(self):
        return self.__UML2WithID_Pseudostate728

    @UML2WithID_Pseudostate728.setter
    def UML2WithID_Pseudostate728(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Pseudostate__UML2WithID_Pseudostate728", None)
        self.__UML2WithID_Pseudostate728 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ConnectionPointReference727"):
                opp_val = getattr(old_value, "UML2WithID_ConnectionPointReference727", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ConnectionPointReference727"):
                opp_val = getattr(value, "UML2WithID_ConnectionPointReference727", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ConnectionPointReference727", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Pseudostate725(self):
        return self.__UML2WithID_Pseudostate725

    @UML2WithID_Pseudostate725.setter
    def UML2WithID_Pseudostate725(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Pseudostate__UML2WithID_Pseudostate725", None)
        self.__UML2WithID_Pseudostate725 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ConnectionPointReference724"):
                opp_val = getattr(old_value, "UML2WithID_ConnectionPointReference724", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ConnectionPointReference724"):
                opp_val = getattr(value, "UML2WithID_ConnectionPointReference724", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ConnectionPointReference724", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TemplateSignature:

    pass
class TemplateParameter:

    pass
class UML2WithID_ClassifierTemplateParameter(TemplateParameter):

    def __init__(self, allowSubstitutable: bool):
        self.allowSubstitutable = allowSubstitutable
        
    @property
    def allowSubstitutable(self) -> bool:
        return self.__allowSubstitutable

    @allowSubstitutable.setter
    def allowSubstitutable(self, allowSubstitutable: bool):
        self.__allowSubstitutable = allowSubstitutable

class UML2WithID_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class UML2WithID_OperationTemplateParameter(TemplateParameter):

    pass
class MessageEnd:

    pass
class EventOccurrence:

    pass
class UML2WithID_Stop(EventOccurrence):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence):

    pass
class InteractionFragment:

    pass
class UML2WithID_Continuation(InteractionFragment):

    def __init__(self, setting: bool):
        self.setting = setting
        
    @property
    def setting(self) -> bool:
        return self.__setting

    @setting.setter
    def setting(self, setting: bool):
        self.__setting = setting

class UML2WithID_ExecutionOccurrence(InteractionFragment):

    pass
class UML2WithID_StateInvariant(InteractionFragment):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment):

    pass
class UML2WithID_CombinedFragment(InteractionFragment):

    def __init__(self, interactionOperator: str, UML2WithID_CombinedFragment: set["UML2WithID_InteractionOperand"] = None, UML2WithID_CombinedFragment672: set["UML2WithID_Gate"] = None):
        self.interactionOperator = interactionOperator
        self.UML2WithID_CombinedFragment = UML2WithID_CombinedFragment if UML2WithID_CombinedFragment is not None else set()
        self.UML2WithID_CombinedFragment672 = UML2WithID_CombinedFragment672 if UML2WithID_CombinedFragment672 is not None else set()
        
    @property
    def interactionOperator(self) -> str:
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator

    @property
    def UML2WithID_CombinedFragment672(self):
        return self.__UML2WithID_CombinedFragment672

    @UML2WithID_CombinedFragment672.setter
    def UML2WithID_CombinedFragment672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_CombinedFragment__UML2WithID_CombinedFragment672", None)
        self.__UML2WithID_CombinedFragment672 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Gate673"):
                    opp_val = getattr(item, "UML2WithID_Gate673", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Gate673", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Gate673"):
                    opp_val = getattr(item, "UML2WithID_Gate673", None)
                    
                    setattr(item, "UML2WithID_Gate673", self)
                    

    @property
    def UML2WithID_CombinedFragment(self):
        return self.__UML2WithID_CombinedFragment

    @UML2WithID_CombinedFragment.setter
    def UML2WithID_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_CombinedFragment__UML2WithID_CombinedFragment", None)
        self.__UML2WithID_CombinedFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_InteractionOperand670"):
                    opp_val = getattr(item, "UML2WithID_InteractionOperand670", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_InteractionOperand670", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_InteractionOperand670"):
                    opp_val = getattr(item, "UML2WithID_InteractionOperand670", None)
                    
                    setattr(item, "UML2WithID_InteractionOperand670", self)
                    

class UML2WithID_EventOccurrence(InteractionFragment, MessageEnd):

    pass
class UML2WithID_Gate(MessageEnd):

    pass
class StructuredActivityNode:

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, ExpansionRegion: "UML2WithID_ExpansionNode" = None, ExpansionRegion640: "UML2WithID_ExpansionNode" = None, regionAsOutput: set["UML2WithID_ExpansionNode"] = None, regionAsInput: set["UML2WithID_ExpansionNode"] = None):
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
    def regionAsOutput(self):
        return self.__regionAsOutput

    @regionAsOutput.setter
    def regionAsOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ExpansionRegion__regionAsOutput", None)
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
                    

    @property
    def ExpansionRegion(self):
        return self.__ExpansionRegion

    @ExpansionRegion.setter
    def ExpansionRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ExpansionRegion__ExpansionRegion", None)
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
    def regionAsInput(self):
        return self.__regionAsInput

    @regionAsInput.setter
    def regionAsInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ExpansionRegion__regionAsInput", None)
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
    def ExpansionRegion640(self):
        return self.__ExpansionRegion640

    @ExpansionRegion640.setter
    def ExpansionRegion640(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ExpansionRegion__ExpansionRegion640", None)
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

class UML2WithID_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: bool, isAssured: bool, UML2WithID_ConditionalNode478: set["UML2WithID_OutputPin"] = None, UML2WithID_ConditionalNode: set["UML2WithID_Clause"] = None):
        self.isDeterminate = isDeterminate
        self.isAssured = isAssured
        self.UML2WithID_ConditionalNode478 = UML2WithID_ConditionalNode478 if UML2WithID_ConditionalNode478 is not None else set()
        self.UML2WithID_ConditionalNode = UML2WithID_ConditionalNode if UML2WithID_ConditionalNode is not None else set()
        
    @property
    def isAssured(self) -> bool:
        return self.__isAssured

    @isAssured.setter
    def isAssured(self, isAssured: bool):
        self.__isAssured = isAssured

    @property
    def isDeterminate(self) -> bool:
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: bool):
        self.__isDeterminate = isDeterminate

    @property
    def UML2WithID_ConditionalNode478(self):
        return self.__UML2WithID_ConditionalNode478

    @UML2WithID_ConditionalNode478.setter
    def UML2WithID_ConditionalNode478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ConditionalNode__UML2WithID_ConditionalNode478", None)
        self.__UML2WithID_ConditionalNode478 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_OutputPin479"):
                    opp_val = getattr(item, "UML2WithID_OutputPin479", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_OutputPin479", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_OutputPin479"):
                    opp_val = getattr(item, "UML2WithID_OutputPin479", None)
                    
                    setattr(item, "UML2WithID_OutputPin479", self)
                    

    @property
    def UML2WithID_ConditionalNode(self):
        return self.__UML2WithID_ConditionalNode

    @UML2WithID_ConditionalNode.setter
    def UML2WithID_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ConditionalNode__UML2WithID_ConditionalNode", None)
        self.__UML2WithID_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Clause"):
                    opp_val = getattr(item, "UML2WithID_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Clause"):
                    opp_val = getattr(item, "UML2WithID_Clause", None)
                    
                    setattr(item, "UML2WithID_Clause", self)
                    

class ActivityGroup:

    pass
class Action:

    pass
class UML2WithID_ReadSelfAction(Action):

    pass
class UML2WithID_InvocationAction(Action):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action):

    pass
class UML2WithID_ClearAssociationAction(Action):

    pass
class UML2WithID_RaiseExceptionAction(Action):

    pass
class UML2WithID_ReplyAction(Action):

    pass
class UML2WithID_CreateObjectAction(Action):

    pass
class UML2WithID_ApplyFunctionAction(Action):

    pass
class UML2WithID_TestIdentityAction(Action):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action):

    pass
class UML2WithID_LinkAction(Action):

    pass
class UML2WithID_StructuralFeatureAction(Action):

    pass
class UML2WithID_DestroyObjectAction(Action):

    def __init__(self, isDestroyLinks: bool, isDestroyOwnedObjects: bool, UML2WithID_DestroyObjectAction: "UML2WithID_InputPin" = None):
        self.isDestroyLinks = isDestroyLinks
        self.isDestroyOwnedObjects = isDestroyOwnedObjects
        self.UML2WithID_DestroyObjectAction = UML2WithID_DestroyObjectAction
        
    @property
    def isDestroyLinks(self) -> bool:
        return self.__isDestroyLinks

    @isDestroyLinks.setter
    def isDestroyLinks(self, isDestroyLinks: bool):
        self.__isDestroyLinks = isDestroyLinks

    @property
    def isDestroyOwnedObjects(self) -> bool:
        return self.__isDestroyOwnedObjects

    @isDestroyOwnedObjects.setter
    def isDestroyOwnedObjects(self, isDestroyOwnedObjects: bool):
        self.__isDestroyOwnedObjects = isDestroyOwnedObjects

    @property
    def UML2WithID_DestroyObjectAction(self):
        return self.__UML2WithID_DestroyObjectAction

    @UML2WithID_DestroyObjectAction.setter
    def UML2WithID_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_DestroyObjectAction__UML2WithID_DestroyObjectAction", None)
        self.__UML2WithID_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InputPin754"):
                opp_val = getattr(old_value, "UML2WithID_InputPin754", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_InputPin754", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InputPin754"):
                opp_val = getattr(value, "UML2WithID_InputPin754", None)
                setattr(value, "UML2WithID_InputPin754", self)

class UML2WithID_ReadExtentAction(Action):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action):

    def __init__(self, isDirect: bool, UML2WithID_ReadIsClassifiedObjectAction: "UML2WithID_Classifier" = None, UML2WithID_ReadIsClassifiedObjectAction902: "UML2WithID_OutputPin" = None, UML2WithID_ReadIsClassifiedObjectAction905: "UML2WithID_InputPin" = None):
        self.isDirect = isDirect
        self.UML2WithID_ReadIsClassifiedObjectAction = UML2WithID_ReadIsClassifiedObjectAction
        self.UML2WithID_ReadIsClassifiedObjectAction902 = UML2WithID_ReadIsClassifiedObjectAction902
        self.UML2WithID_ReadIsClassifiedObjectAction905 = UML2WithID_ReadIsClassifiedObjectAction905
        
    @property
    def isDirect(self) -> bool:
        return self.__isDirect

    @isDirect.setter
    def isDirect(self, isDirect: bool):
        self.__isDirect = isDirect

    @property
    def UML2WithID_ReadIsClassifiedObjectAction905(self):
        return self.__UML2WithID_ReadIsClassifiedObjectAction905

    @UML2WithID_ReadIsClassifiedObjectAction905.setter
    def UML2WithID_ReadIsClassifiedObjectAction905(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ReadIsClassifiedObjectAction__UML2WithID_ReadIsClassifiedObjectAction905", None)
        self.__UML2WithID_ReadIsClassifiedObjectAction905 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InputPin906"):
                opp_val = getattr(old_value, "UML2WithID_InputPin906", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_InputPin906", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InputPin906"):
                opp_val = getattr(value, "UML2WithID_InputPin906", None)
                setattr(value, "UML2WithID_InputPin906", self)

    @property
    def UML2WithID_ReadIsClassifiedObjectAction902(self):
        return self.__UML2WithID_ReadIsClassifiedObjectAction902

    @UML2WithID_ReadIsClassifiedObjectAction902.setter
    def UML2WithID_ReadIsClassifiedObjectAction902(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ReadIsClassifiedObjectAction__UML2WithID_ReadIsClassifiedObjectAction902", None)
        self.__UML2WithID_ReadIsClassifiedObjectAction902 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_OutputPin903"):
                opp_val = getattr(old_value, "UML2WithID_OutputPin903", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_OutputPin903", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_OutputPin903"):
                opp_val = getattr(value, "UML2WithID_OutputPin903", None)
                setattr(value, "UML2WithID_OutputPin903", self)

    @property
    def UML2WithID_ReadIsClassifiedObjectAction(self):
        return self.__UML2WithID_ReadIsClassifiedObjectAction

    @UML2WithID_ReadIsClassifiedObjectAction.setter
    def UML2WithID_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ReadIsClassifiedObjectAction__UML2WithID_ReadIsClassifiedObjectAction", None)
        self.__UML2WithID_ReadIsClassifiedObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Classifier900"):
                opp_val = getattr(old_value, "UML2WithID_Classifier900", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Classifier900", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Classifier900"):
                opp_val = getattr(value, "UML2WithID_Classifier900", None)
                setattr(value, "UML2WithID_Classifier900", self)

class UML2WithID_VariableAction(Action):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2WithID_AcceptEventAction(Action):

    pass
class UML2WithID_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: bool, UML2WithID_ReclassifyObjectAction: set["UML2WithID_Classifier"] = None, UML2WithID_ReclassifyObjectAction894: set["UML2WithID_Classifier"] = None, UML2WithID_ReclassifyObjectAction897: "UML2WithID_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.UML2WithID_ReclassifyObjectAction = UML2WithID_ReclassifyObjectAction if UML2WithID_ReclassifyObjectAction is not None else set()
        self.UML2WithID_ReclassifyObjectAction894 = UML2WithID_ReclassifyObjectAction894 if UML2WithID_ReclassifyObjectAction894 is not None else set()
        self.UML2WithID_ReclassifyObjectAction897 = UML2WithID_ReclassifyObjectAction897
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def UML2WithID_ReclassifyObjectAction(self):
        return self.__UML2WithID_ReclassifyObjectAction

    @UML2WithID_ReclassifyObjectAction.setter
    def UML2WithID_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ReclassifyObjectAction__UML2WithID_ReclassifyObjectAction", None)
        self.__UML2WithID_ReclassifyObjectAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Classifier892"):
                    opp_val = getattr(item, "UML2WithID_Classifier892", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Classifier892", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Classifier892"):
                    opp_val = getattr(item, "UML2WithID_Classifier892", None)
                    
                    setattr(item, "UML2WithID_Classifier892", self)
                    

    @property
    def UML2WithID_ReclassifyObjectAction897(self):
        return self.__UML2WithID_ReclassifyObjectAction897

    @UML2WithID_ReclassifyObjectAction897.setter
    def UML2WithID_ReclassifyObjectAction897(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ReclassifyObjectAction__UML2WithID_ReclassifyObjectAction897", None)
        self.__UML2WithID_ReclassifyObjectAction897 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InputPin898"):
                opp_val = getattr(old_value, "UML2WithID_InputPin898", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_InputPin898", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InputPin898"):
                opp_val = getattr(value, "UML2WithID_InputPin898", None)
                setattr(value, "UML2WithID_InputPin898", self)

    @property
    def UML2WithID_ReclassifyObjectAction894(self):
        return self.__UML2WithID_ReclassifyObjectAction894

    @UML2WithID_ReclassifyObjectAction894.setter
    def UML2WithID_ReclassifyObjectAction894(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ReclassifyObjectAction__UML2WithID_ReclassifyObjectAction894", None)
        self.__UML2WithID_ReclassifyObjectAction894 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Classifier895"):
                    opp_val = getattr(item, "UML2WithID_Classifier895", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Classifier895", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Classifier895"):
                    opp_val = getattr(item, "UML2WithID_Classifier895", None)
                    
                    setattr(item, "UML2WithID_Classifier895", self)
                    

class UML2WithID_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: bool, UML2WithID_LoopNode: set["UML2WithID_ActivityNode"] = None, UML2WithID_LoopNode500: set["UML2WithID_ActivityNode"] = None, UML2WithID_LoopNode503: "UML2WithID_OutputPin" = None, UML2WithID_LoopNode506: set["UML2WithID_ActivityNode"] = None, UML2WithID_LoopNode509: set["UML2WithID_OutputPin"] = None, UML2WithID_LoopNode512: set["UML2WithID_OutputPin"] = None, UML2WithID_LoopNode515: set["UML2WithID_OutputPin"] = None, UML2WithID_LoopNode518: set["UML2WithID_InputPin"] = None):
        self.isTestedFirst = isTestedFirst
        self.UML2WithID_LoopNode = UML2WithID_LoopNode if UML2WithID_LoopNode is not None else set()
        self.UML2WithID_LoopNode500 = UML2WithID_LoopNode500 if UML2WithID_LoopNode500 is not None else set()
        self.UML2WithID_LoopNode503 = UML2WithID_LoopNode503
        self.UML2WithID_LoopNode506 = UML2WithID_LoopNode506 if UML2WithID_LoopNode506 is not None else set()
        self.UML2WithID_LoopNode509 = UML2WithID_LoopNode509 if UML2WithID_LoopNode509 is not None else set()
        self.UML2WithID_LoopNode512 = UML2WithID_LoopNode512 if UML2WithID_LoopNode512 is not None else set()
        self.UML2WithID_LoopNode515 = UML2WithID_LoopNode515 if UML2WithID_LoopNode515 is not None else set()
        self.UML2WithID_LoopNode518 = UML2WithID_LoopNode518 if UML2WithID_LoopNode518 is not None else set()
        
    @property
    def isTestedFirst(self) -> bool:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: bool):
        self.__isTestedFirst = isTestedFirst

    @property
    def UML2WithID_LoopNode503(self):
        return self.__UML2WithID_LoopNode503

    @UML2WithID_LoopNode503.setter
    def UML2WithID_LoopNode503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode503", None)
        self.__UML2WithID_LoopNode503 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_OutputPin504"):
                opp_val = getattr(old_value, "UML2WithID_OutputPin504", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_OutputPin504", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_OutputPin504"):
                opp_val = getattr(value, "UML2WithID_OutputPin504", None)
                setattr(value, "UML2WithID_OutputPin504", self)

    @property
    def UML2WithID_LoopNode518(self):
        return self.__UML2WithID_LoopNode518

    @UML2WithID_LoopNode518.setter
    def UML2WithID_LoopNode518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode518", None)
        self.__UML2WithID_LoopNode518 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_InputPin519"):
                    opp_val = getattr(item, "UML2WithID_InputPin519", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_InputPin519", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_InputPin519"):
                    opp_val = getattr(item, "UML2WithID_InputPin519", None)
                    
                    setattr(item, "UML2WithID_InputPin519", self)
                    

    @property
    def UML2WithID_LoopNode506(self):
        return self.__UML2WithID_LoopNode506

    @UML2WithID_LoopNode506.setter
    def UML2WithID_LoopNode506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode506", None)
        self.__UML2WithID_LoopNode506 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ActivityNode507"):
                    opp_val = getattr(item, "UML2WithID_ActivityNode507", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ActivityNode507", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ActivityNode507"):
                    opp_val = getattr(item, "UML2WithID_ActivityNode507", None)
                    
                    setattr(item, "UML2WithID_ActivityNode507", self)
                    

    @property
    def UML2WithID_LoopNode500(self):
        return self.__UML2WithID_LoopNode500

    @UML2WithID_LoopNode500.setter
    def UML2WithID_LoopNode500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode500", None)
        self.__UML2WithID_LoopNode500 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ActivityNode501"):
                    opp_val = getattr(item, "UML2WithID_ActivityNode501", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ActivityNode501", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ActivityNode501"):
                    opp_val = getattr(item, "UML2WithID_ActivityNode501", None)
                    
                    setattr(item, "UML2WithID_ActivityNode501", self)
                    

    @property
    def UML2WithID_LoopNode515(self):
        return self.__UML2WithID_LoopNode515

    @UML2WithID_LoopNode515.setter
    def UML2WithID_LoopNode515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode515", None)
        self.__UML2WithID_LoopNode515 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_OutputPin516"):
                    opp_val = getattr(item, "UML2WithID_OutputPin516", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_OutputPin516", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_OutputPin516"):
                    opp_val = getattr(item, "UML2WithID_OutputPin516", None)
                    
                    setattr(item, "UML2WithID_OutputPin516", self)
                    

    @property
    def UML2WithID_LoopNode(self):
        return self.__UML2WithID_LoopNode

    @UML2WithID_LoopNode.setter
    def UML2WithID_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode", None)
        self.__UML2WithID_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ActivityNode498"):
                    opp_val = getattr(item, "UML2WithID_ActivityNode498", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ActivityNode498", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ActivityNode498"):
                    opp_val = getattr(item, "UML2WithID_ActivityNode498", None)
                    
                    setattr(item, "UML2WithID_ActivityNode498", self)
                    

    @property
    def UML2WithID_LoopNode512(self):
        return self.__UML2WithID_LoopNode512

    @UML2WithID_LoopNode512.setter
    def UML2WithID_LoopNode512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode512", None)
        self.__UML2WithID_LoopNode512 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_OutputPin513"):
                    opp_val = getattr(item, "UML2WithID_OutputPin513", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_OutputPin513", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_OutputPin513"):
                    opp_val = getattr(item, "UML2WithID_OutputPin513", None)
                    
                    setattr(item, "UML2WithID_OutputPin513", self)
                    

    @property
    def UML2WithID_LoopNode509(self):
        return self.__UML2WithID_LoopNode509

    @UML2WithID_LoopNode509.setter
    def UML2WithID_LoopNode509(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_LoopNode__UML2WithID_LoopNode509", None)
        self.__UML2WithID_LoopNode509 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_OutputPin510"):
                    opp_val = getattr(item, "UML2WithID_OutputPin510", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_OutputPin510", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_OutputPin510"):
                    opp_val = getattr(item, "UML2WithID_OutputPin510", None)
                    
                    setattr(item, "UML2WithID_OutputPin510", self)
                    

class Trigger:

    pass
class UML2WithID_ChangeTrigger(Trigger):

    pass
class UML2WithID_MessageTrigger(Trigger):

    pass
class MessageTrigger:

    pass
class UML2WithID_AnyTrigger(MessageTrigger):

    pass
class UML2WithID_CallTrigger(MessageTrigger):

    pass
class UML2WithID_TimeTrigger(Trigger):

    def __init__(self, isRelative: bool, UML2WithID_TimeTrigger: "UML2WithID_ValueSpecification" = None):
        self.isRelative = isRelative
        self.UML2WithID_TimeTrigger = UML2WithID_TimeTrigger
        
    @property
    def isRelative(self) -> bool:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: bool):
        self.__isRelative = isRelative

    @property
    def UML2WithID_TimeTrigger(self):
        return self.__UML2WithID_TimeTrigger

    @UML2WithID_TimeTrigger.setter
    def UML2WithID_TimeTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_TimeTrigger__UML2WithID_TimeTrigger", None)
        self.__UML2WithID_TimeTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ValueSpecification467"):
                opp_val = getattr(old_value, "UML2WithID_ValueSpecification467", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ValueSpecification467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ValueSpecification467"):
                opp_val = getattr(value, "UML2WithID_ValueSpecification467", None)
                setattr(value, "UML2WithID_ValueSpecification467", self)

class UML2WithID_SignalTrigger(MessageTrigger):

    pass
class StructuredClassifier:

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine):

    pass
class InputPin:

    pass
class UML2WithID_ValuePin(InputPin):

    pass
class ObjectNode:

    pass
class UML2WithID_ActivityParameterNode(ObjectNode):

    pass
class UML2WithID_CentralBufferNode(ObjectNode):

    pass
class UML2WithID_ExpansionNode(ObjectNode):

    pass
class ActivityEdge:

    pass
class UML2WithID_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool, UML2WithID_ObjectFlow: "UML2WithID_Behavior" = None, UML2WithID_ObjectFlow367: "UML2WithID_Behavior" = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.UML2WithID_ObjectFlow = UML2WithID_ObjectFlow
        self.UML2WithID_ObjectFlow367 = UML2WithID_ObjectFlow367
        
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
    def UML2WithID_ObjectFlow(self):
        return self.__UML2WithID_ObjectFlow

    @UML2WithID_ObjectFlow.setter
    def UML2WithID_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ObjectFlow__UML2WithID_ObjectFlow", None)
        self.__UML2WithID_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior365"):
                opp_val = getattr(old_value, "UML2WithID_Behavior365", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Behavior365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior365"):
                opp_val = getattr(value, "UML2WithID_Behavior365", None)
                setattr(value, "UML2WithID_Behavior365", self)

    @property
    def UML2WithID_ObjectFlow367(self):
        return self.__UML2WithID_ObjectFlow367

    @UML2WithID_ObjectFlow367.setter
    def UML2WithID_ObjectFlow367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ObjectFlow__UML2WithID_ObjectFlow367", None)
        self.__UML2WithID_ObjectFlow367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior368"):
                opp_val = getattr(old_value, "UML2WithID_Behavior368", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Behavior368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior368"):
                opp_val = getattr(value, "UML2WithID_Behavior368", None)
                setattr(value, "UML2WithID_Behavior368", self)

class UML2WithID_ControlFlow(ActivityEdge):

    pass
class ActivityNode:

    pass
class UML2WithID_ControlNode(ActivityNode):

    pass
class Pin:

    pass
class UML2WithID_InputPin(Pin):

    pass
class UML2WithID_ExecutableNode(ActivityNode):

    pass
class FinalNode:

    pass
class UML2WithID_FlowFinalNode(FinalNode):

    pass
class UML2WithID_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class UML2WithID_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: bool, UML2WithID_JoinNode: "UML2WithID_ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.UML2WithID_JoinNode = UML2WithID_JoinNode
        
    @property
    def isCombineDuplicate(self) -> bool:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: bool):
        self.__isCombineDuplicate = isCombineDuplicate

    @property
    def UML2WithID_JoinNode(self):
        return self.__UML2WithID_JoinNode

    @UML2WithID_JoinNode.setter
    def UML2WithID_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_JoinNode__UML2WithID_JoinNode", None)
        self.__UML2WithID_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ValueSpecification624"):
                opp_val = getattr(old_value, "UML2WithID_ValueSpecification624", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ValueSpecification624", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ValueSpecification624"):
                opp_val = getattr(value, "UML2WithID_ValueSpecification624", None)
                setattr(value, "UML2WithID_ValueSpecification624", self)

class UML2WithID_MergeNode(ControlNode):

    pass
class UML2WithID_DecisionNode(ControlNode):

    pass
class UML2WithID_ForkNode(ControlNode):

    pass
class UML2WithID_FinalNode(ControlNode):

    pass
class UML2WithID_InitialNode(ControlNode):

    pass
class UML2WithID_InterruptibleActivityRegion(ActivityGroup):

    pass
class UML2WithID_OutputPin(Pin):

    pass
class ExecutableNode:

    pass
class Realization:

    pass
class Abstraction:

    pass
class UML2WithID_Manifestation(Abstraction):

    pass
class UML2WithID_Realization(Abstraction):

    pass
class Behavior:

    pass
class UML2WithID_Interaction(InteractionFragment, Behavior):

    pass
class UML2WithID_Activity(Behavior):

    def __init__(self, isSingleExecution: bool, isReadOnly: bool, body: str, language: str, UML2WithID_Activity: set["UML2WithID_Action"] = None, UML2WithID_Activity249: set["UML2WithID_StructuredActivityNode"] = None, activity: set["UML2WithID_ActivityEdge"] = None, activityGroup_activity: set["UML2WithID_ActivityGroup"] = None, activity246: set["UML2WithID_ActivityNode"] = None, Activity: "UML2WithID_ActivityEdge" = None, Activity332: "UML2WithID_ActivityNode" = None, Activity324: "UML2WithID_ActivityGroup" = None, UML2WithID_Activity705: "UML2WithID_State" = None, UML2WithID_Activity708: "UML2WithID_State" = None, UML2WithID_Activity747: "UML2WithID_Transition" = None, UML2WithID_Activity711: "UML2WithID_State" = None):
        self.isSingleExecution = isSingleExecution
        self.isReadOnly = isReadOnly
        self.body = body
        self.language = language
        self.UML2WithID_Activity = UML2WithID_Activity if UML2WithID_Activity is not None else set()
        self.UML2WithID_Activity249 = UML2WithID_Activity249 if UML2WithID_Activity249 is not None else set()
        self.activity = activity if activity is not None else set()
        self.activityGroup_activity = activityGroup_activity if activityGroup_activity is not None else set()
        self.activity246 = activity246 if activity246 is not None else set()
        self.Activity = Activity
        self.Activity332 = Activity332
        self.Activity324 = Activity324
        self.UML2WithID_Activity705 = UML2WithID_Activity705
        self.UML2WithID_Activity708 = UML2WithID_Activity708
        self.UML2WithID_Activity747 = UML2WithID_Activity747
        self.UML2WithID_Activity711 = UML2WithID_Activity711
        
    @property
    def isSingleExecution(self) -> bool:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution

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
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def activity246(self):
        return self.__activity246

    @activity246.setter
    def activity246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__activity246", None)
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
    def Activity324(self):
        return self.__Activity324

    @Activity324.setter
    def Activity324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__Activity324", None)
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
    def UML2WithID_Activity705(self):
        return self.__UML2WithID_Activity705

    @UML2WithID_Activity705.setter
    def UML2WithID_Activity705(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__UML2WithID_Activity705", None)
        self.__UML2WithID_Activity705 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_State704"):
                opp_val = getattr(old_value, "UML2WithID_State704", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_State704", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_State704"):
                opp_val = getattr(value, "UML2WithID_State704", None)
                setattr(value, "UML2WithID_State704", self)

    @property
    def UML2WithID_Activity708(self):
        return self.__UML2WithID_Activity708

    @UML2WithID_Activity708.setter
    def UML2WithID_Activity708(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__UML2WithID_Activity708", None)
        self.__UML2WithID_Activity708 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_State707"):
                opp_val = getattr(old_value, "UML2WithID_State707", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_State707", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_State707"):
                opp_val = getattr(value, "UML2WithID_State707", None)
                setattr(value, "UML2WithID_State707", self)

    @property
    def UML2WithID_Activity747(self):
        return self.__UML2WithID_Activity747

    @UML2WithID_Activity747.setter
    def UML2WithID_Activity747(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__UML2WithID_Activity747", None)
        self.__UML2WithID_Activity747 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Transition746"):
                opp_val = getattr(old_value, "UML2WithID_Transition746", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Transition746", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Transition746"):
                opp_val = getattr(value, "UML2WithID_Transition746", None)
                setattr(value, "UML2WithID_Transition746", self)

    @property
    def UML2WithID_Activity249(self):
        return self.__UML2WithID_Activity249

    @UML2WithID_Activity249.setter
    def UML2WithID_Activity249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__UML2WithID_Activity249", None)
        self.__UML2WithID_Activity249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_StructuredActivityNode"):
                    opp_val = getattr(item, "UML2WithID_StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_StructuredActivityNode"):
                    opp_val = getattr(item, "UML2WithID_StructuredActivityNode", None)
                    
                    setattr(item, "UML2WithID_StructuredActivityNode", self)
                    

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__Activity", None)
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
    def Activity332(self):
        return self.__Activity332

    @Activity332.setter
    def Activity332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__Activity332", None)
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
    def UML2WithID_Activity(self):
        return self.__UML2WithID_Activity

    @UML2WithID_Activity.setter
    def UML2WithID_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__UML2WithID_Activity", None)
        self.__UML2WithID_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Action"):
                    opp_val = getattr(item, "UML2WithID_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Action"):
                    opp_val = getattr(item, "UML2WithID_Action", None)
                    
                    setattr(item, "UML2WithID_Action", self)
                    

    @property
    def UML2WithID_Activity711(self):
        return self.__UML2WithID_Activity711

    @UML2WithID_Activity711.setter
    def UML2WithID_Activity711(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__UML2WithID_Activity711", None)
        self.__UML2WithID_Activity711 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_State710"):
                opp_val = getattr(old_value, "UML2WithID_State710", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_State710", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_State710"):
                opp_val = getattr(value, "UML2WithID_State710", None)
                setattr(value, "UML2WithID_State710", self)

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__activity", None)
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
    def activityGroup_activity(self):
        return self.__activityGroup_activity

    @activityGroup_activity.setter
    def activityGroup_activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Activity__activityGroup_activity", None)
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
                    

class UML2WithID_StateMachine(Behavior):

    pass
class UML2WithID_Implementation(Realization):

    pass
class Dependency:

    pass
class UML2WithID_Deployment(Dependency):

    pass
class UML2WithID_Abstraction(Dependency):

    pass
class UML2WithID_Usage(Dependency):

    pass
class UML2WithID_Permission(Dependency):

    pass
class UML2WithID_Action(ExecutableNode):

    def __init__(self, effect: str, UML2WithID_Action: "UML2WithID_Activity" = None, UML2WithID_Action345: set["UML2WithID_OutputPin"] = None, UML2WithID_Action347: set["UML2WithID_InputPin"] = None, UML2WithID_Action349: "UML2WithID_Classifier" = None, UML2WithID_Action352: set["UML2WithID_Constraint"] = None, UML2WithID_Action355: set["UML2WithID_Constraint"] = None):
        self.effect = effect
        self.UML2WithID_Action = UML2WithID_Action
        self.UML2WithID_Action345 = UML2WithID_Action345 if UML2WithID_Action345 is not None else set()
        self.UML2WithID_Action347 = UML2WithID_Action347 if UML2WithID_Action347 is not None else set()
        self.UML2WithID_Action349 = UML2WithID_Action349
        self.UML2WithID_Action352 = UML2WithID_Action352 if UML2WithID_Action352 is not None else set()
        self.UML2WithID_Action355 = UML2WithID_Action355 if UML2WithID_Action355 is not None else set()
        
    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def UML2WithID_Action355(self):
        return self.__UML2WithID_Action355

    @UML2WithID_Action355.setter
    def UML2WithID_Action355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Action__UML2WithID_Action355", None)
        self.__UML2WithID_Action355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Constraint356"):
                    opp_val = getattr(item, "UML2WithID_Constraint356", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Constraint356", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Constraint356"):
                    opp_val = getattr(item, "UML2WithID_Constraint356", None)
                    
                    setattr(item, "UML2WithID_Constraint356", self)
                    

    @property
    def UML2WithID_Action352(self):
        return self.__UML2WithID_Action352

    @UML2WithID_Action352.setter
    def UML2WithID_Action352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Action__UML2WithID_Action352", None)
        self.__UML2WithID_Action352 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Constraint353"):
                    opp_val = getattr(item, "UML2WithID_Constraint353", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Constraint353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Constraint353"):
                    opp_val = getattr(item, "UML2WithID_Constraint353", None)
                    
                    setattr(item, "UML2WithID_Constraint353", self)
                    

    @property
    def UML2WithID_Action(self):
        return self.__UML2WithID_Action

    @UML2WithID_Action.setter
    def UML2WithID_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Action__UML2WithID_Action", None)
        self.__UML2WithID_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Activity"):
                opp_val = getattr(old_value, "UML2WithID_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Activity"):
                opp_val = getattr(value, "UML2WithID_Activity", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Action349(self):
        return self.__UML2WithID_Action349

    @UML2WithID_Action349.setter
    def UML2WithID_Action349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Action__UML2WithID_Action349", None)
        self.__UML2WithID_Action349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Classifier350"):
                opp_val = getattr(old_value, "UML2WithID_Classifier350", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Classifier350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Classifier350"):
                opp_val = getattr(value, "UML2WithID_Classifier350", None)
                setattr(value, "UML2WithID_Classifier350", self)

    @property
    def UML2WithID_Action345(self):
        return self.__UML2WithID_Action345

    @UML2WithID_Action345.setter
    def UML2WithID_Action345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Action__UML2WithID_Action345", None)
        self.__UML2WithID_Action345 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_OutputPin"):
                    opp_val = getattr(item, "UML2WithID_OutputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_OutputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_OutputPin"):
                    opp_val = getattr(item, "UML2WithID_OutputPin", None)
                    
                    setattr(item, "UML2WithID_OutputPin", self)
                    

    @property
    def UML2WithID_Action347(self):
        return self.__UML2WithID_Action347

    @UML2WithID_Action347.setter
    def UML2WithID_Action347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Action__UML2WithID_Action347", None)
        self.__UML2WithID_Action347 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_InputPin"):
                    opp_val = getattr(item, "UML2WithID_InputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_InputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_InputPin"):
                    opp_val = getattr(item, "UML2WithID_InputPin", None)
                    
                    setattr(item, "UML2WithID_InputPin", self)
                    

class Property:

    pass
class UML2WithID_Port(Property):

    def __init__(self, isBehavior: bool, isService: bool, UML2WithID_Port458: "UML2WithID_Trigger" = None, UML2WithID_Port: set["UML2WithID_Interface"] = None, UML2WithID_Port443: "UML2WithID_Port" = None, UML2WithID_Port441: set["UML2WithID_Port"] = None, UML2WithID_Port445: set["UML2WithID_Interface"] = None, UML2WithID_Port448: "UML2WithID_ProtocolStateMachine" = None, UML2WithID_Port451: "UML2WithID_EncapsulatedClassifier" = None, UML2WithID_Port814: "UML2WithID_InvocationAction" = None):
        self.isBehavior = isBehavior
        self.isService = isService
        self.UML2WithID_Port458 = UML2WithID_Port458
        self.UML2WithID_Port = UML2WithID_Port if UML2WithID_Port is not None else set()
        self.UML2WithID_Port443 = UML2WithID_Port443
        self.UML2WithID_Port441 = UML2WithID_Port441 if UML2WithID_Port441 is not None else set()
        self.UML2WithID_Port445 = UML2WithID_Port445 if UML2WithID_Port445 is not None else set()
        self.UML2WithID_Port448 = UML2WithID_Port448
        self.UML2WithID_Port451 = UML2WithID_Port451
        self.UML2WithID_Port814 = UML2WithID_Port814
        
    @property
    def isBehavior(self) -> bool:
        return self.__isBehavior

    @isBehavior.setter
    def isBehavior(self, isBehavior: bool):
        self.__isBehavior = isBehavior

    @property
    def isService(self) -> bool:
        return self.__isService

    @isService.setter
    def isService(self, isService: bool):
        self.__isService = isService

    @property
    def UML2WithID_Port441(self):
        return self.__UML2WithID_Port441

    @UML2WithID_Port441.setter
    def UML2WithID_Port441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port441", None)
        self.__UML2WithID_Port441 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Port443"):
                    opp_val = getattr(item, "UML2WithID_Port443", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Port443", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Port443"):
                    opp_val = getattr(item, "UML2WithID_Port443", None)
                    
                    setattr(item, "UML2WithID_Port443", self)
                    

    @property
    def UML2WithID_Port(self):
        return self.__UML2WithID_Port

    @UML2WithID_Port.setter
    def UML2WithID_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port", None)
        self.__UML2WithID_Port = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Interface440"):
                    opp_val = getattr(item, "UML2WithID_Interface440", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Interface440", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Interface440"):
                    opp_val = getattr(item, "UML2WithID_Interface440", None)
                    
                    setattr(item, "UML2WithID_Interface440", self)
                    

    @property
    def UML2WithID_Port458(self):
        return self.__UML2WithID_Port458

    @UML2WithID_Port458.setter
    def UML2WithID_Port458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port458", None)
        self.__UML2WithID_Port458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Trigger457"):
                opp_val = getattr(old_value, "UML2WithID_Trigger457", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Trigger457"):
                opp_val = getattr(value, "UML2WithID_Trigger457", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Trigger457", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Port814(self):
        return self.__UML2WithID_Port814

    @UML2WithID_Port814.setter
    def UML2WithID_Port814(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port814", None)
        self.__UML2WithID_Port814 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InvocationAction813"):
                opp_val = getattr(old_value, "UML2WithID_InvocationAction813", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_InvocationAction813", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InvocationAction813"):
                opp_val = getattr(value, "UML2WithID_InvocationAction813", None)
                setattr(value, "UML2WithID_InvocationAction813", self)

    @property
    def UML2WithID_Port448(self):
        return self.__UML2WithID_Port448

    @UML2WithID_Port448.setter
    def UML2WithID_Port448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port448", None)
        self.__UML2WithID_Port448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ProtocolStateMachine449"):
                opp_val = getattr(old_value, "UML2WithID_ProtocolStateMachine449", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ProtocolStateMachine449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ProtocolStateMachine449"):
                opp_val = getattr(value, "UML2WithID_ProtocolStateMachine449", None)
                setattr(value, "UML2WithID_ProtocolStateMachine449", self)

    @property
    def UML2WithID_Port451(self):
        return self.__UML2WithID_Port451

    @UML2WithID_Port451.setter
    def UML2WithID_Port451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port451", None)
        self.__UML2WithID_Port451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_EncapsulatedClassifier"):
                opp_val = getattr(old_value, "UML2WithID_EncapsulatedClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_EncapsulatedClassifier"):
                opp_val = getattr(value, "UML2WithID_EncapsulatedClassifier", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_EncapsulatedClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Port445(self):
        return self.__UML2WithID_Port445

    @UML2WithID_Port445.setter
    def UML2WithID_Port445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port445", None)
        self.__UML2WithID_Port445 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Interface446"):
                    opp_val = getattr(item, "UML2WithID_Interface446", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Interface446", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Interface446"):
                    opp_val = getattr(item, "UML2WithID_Interface446", None)
                    
                    setattr(item, "UML2WithID_Interface446", self)
                    

    @property
    def UML2WithID_Port443(self):
        return self.__UML2WithID_Port443

    @UML2WithID_Port443.setter
    def UML2WithID_Port443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Port__UML2WithID_Port443", None)
        self.__UML2WithID_Port443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Port441"):
                opp_val = getattr(old_value, "UML2WithID_Port441", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Port441"):
                opp_val = getattr(value, "UML2WithID_Port441", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Port441", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2WithID_ExtensionEnd(Property):

    pass
class Association:

    pass
class UML2WithID_CommunicationPath(Association):

    pass
class PackageImport:

    pass
class Package:

    pass
class UML2WithID_Model(Package):

    def __init__(self, viewpoint: str):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> str:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: str):
        self.__viewpoint = viewpoint

class UML2WithID_Profile(Package):

    pass
class Class:

    pass
class UML2WithID_Component(Class):

    def __init__(self, isIndirectlyInstantiated: bool, Component: "UML2WithID_Realization" = None, UML2WithID_Component: set["UML2WithID_Interface"] = None, UML2WithID_Component859: set["UML2WithID_Interface"] = None, abstraction: set["UML2WithID_Realization"] = None, UML2WithID_Component863: set["UML2WithID_PackageableElement"] = None):
        self.isIndirectlyInstantiated = isIndirectlyInstantiated
        self.Component = Component
        self.UML2WithID_Component = UML2WithID_Component if UML2WithID_Component is not None else set()
        self.UML2WithID_Component859 = UML2WithID_Component859 if UML2WithID_Component859 is not None else set()
        self.abstraction = abstraction if abstraction is not None else set()
        self.UML2WithID_Component863 = UML2WithID_Component863 if UML2WithID_Component863 is not None else set()
        
    @property
    def isIndirectlyInstantiated(self) -> bool:
        return self.__isIndirectlyInstantiated

    @isIndirectlyInstantiated.setter
    def isIndirectlyInstantiated(self, isIndirectlyInstantiated: bool):
        self.__isIndirectlyInstantiated = isIndirectlyInstantiated

    @property
    def UML2WithID_Component859(self):
        return self.__UML2WithID_Component859

    @UML2WithID_Component859.setter
    def UML2WithID_Component859(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Component__UML2WithID_Component859", None)
        self.__UML2WithID_Component859 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Interface860"):
                    opp_val = getattr(item, "UML2WithID_Interface860", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Interface860", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Interface860"):
                    opp_val = getattr(item, "UML2WithID_Interface860", None)
                    
                    setattr(item, "UML2WithID_Interface860", self)
                    

    @property
    def UML2WithID_Component863(self):
        return self.__UML2WithID_Component863

    @UML2WithID_Component863.setter
    def UML2WithID_Component863(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Component__UML2WithID_Component863", None)
        self.__UML2WithID_Component863 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_PackageableElement864"):
                    opp_val = getattr(item, "UML2WithID_PackageableElement864", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_PackageableElement864", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_PackageableElement864"):
                    opp_val = getattr(item, "UML2WithID_PackageableElement864", None)
                    
                    setattr(item, "UML2WithID_PackageableElement864", self)
                    

    @property
    def UML2WithID_Component(self):
        return self.__UML2WithID_Component

    @UML2WithID_Component.setter
    def UML2WithID_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Component__UML2WithID_Component", None)
        self.__UML2WithID_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Interface857"):
                    opp_val = getattr(item, "UML2WithID_Interface857", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Interface857", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Interface857"):
                    opp_val = getattr(item, "UML2WithID_Interface857", None)
                    
                    setattr(item, "UML2WithID_Interface857", self)
                    

    @property
    def abstraction(self):
        return self.__abstraction

    @abstraction.setter
    def abstraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Component__abstraction", None)
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
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Component__Component", None)
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

class UML2WithID_AssociationClass(Class, Association):

    pass
class UML2WithID_Stereotype(Class):

    pass
class DirectedRelationship:

    pass
class UML2WithID_ProtocolConformance(DirectedRelationship):

    pass
class UML2WithID_TemplateBinding(DirectedRelationship):

    pass
class DeployedArtifact:

    pass
class Feature:

    pass
class UML2WithID_Connector(Feature):

    def __init__(self, kind: str, UML2WithID_Connector300: "UML2WithID_StructuredClassifier" = None, UML2WithID_Connector: "UML2WithID_Association" = None, UML2WithID_Connector284: "UML2WithID_Connector" = None, UML2WithID_Connector282: set["UML2WithID_Connector"] = None, UML2WithID_Connector286: set["UML2WithID_ConnectorEnd"] = None, UML2WithID_Connector289: set["UML2WithID_Behavior"] = None, UML2WithID_Connector546: "UML2WithID_Message" = None):
        self.kind = kind
        self.UML2WithID_Connector300 = UML2WithID_Connector300
        self.UML2WithID_Connector = UML2WithID_Connector
        self.UML2WithID_Connector284 = UML2WithID_Connector284
        self.UML2WithID_Connector282 = UML2WithID_Connector282 if UML2WithID_Connector282 is not None else set()
        self.UML2WithID_Connector286 = UML2WithID_Connector286 if UML2WithID_Connector286 is not None else set()
        self.UML2WithID_Connector289 = UML2WithID_Connector289 if UML2WithID_Connector289 is not None else set()
        self.UML2WithID_Connector546 = UML2WithID_Connector546
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def UML2WithID_Connector284(self):
        return self.__UML2WithID_Connector284

    @UML2WithID_Connector284.setter
    def UML2WithID_Connector284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Connector__UML2WithID_Connector284", None)
        self.__UML2WithID_Connector284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Connector282"):
                opp_val = getattr(old_value, "UML2WithID_Connector282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Connector282"):
                opp_val = getattr(value, "UML2WithID_Connector282", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Connector282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Connector286(self):
        return self.__UML2WithID_Connector286

    @UML2WithID_Connector286.setter
    def UML2WithID_Connector286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Connector__UML2WithID_Connector286", None)
        self.__UML2WithID_Connector286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ConnectorEnd287"):
                    opp_val = getattr(item, "UML2WithID_ConnectorEnd287", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ConnectorEnd287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ConnectorEnd287"):
                    opp_val = getattr(item, "UML2WithID_ConnectorEnd287", None)
                    
                    setattr(item, "UML2WithID_ConnectorEnd287", self)
                    

    @property
    def UML2WithID_Connector289(self):
        return self.__UML2WithID_Connector289

    @UML2WithID_Connector289.setter
    def UML2WithID_Connector289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Connector__UML2WithID_Connector289", None)
        self.__UML2WithID_Connector289 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Behavior290"):
                    opp_val = getattr(item, "UML2WithID_Behavior290", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Behavior290", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Behavior290"):
                    opp_val = getattr(item, "UML2WithID_Behavior290", None)
                    
                    setattr(item, "UML2WithID_Behavior290", self)
                    

    @property
    def UML2WithID_Connector282(self):
        return self.__UML2WithID_Connector282

    @UML2WithID_Connector282.setter
    def UML2WithID_Connector282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Connector__UML2WithID_Connector282", None)
        self.__UML2WithID_Connector282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Connector284"):
                    opp_val = getattr(item, "UML2WithID_Connector284", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Connector284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Connector284"):
                    opp_val = getattr(item, "UML2WithID_Connector284", None)
                    
                    setattr(item, "UML2WithID_Connector284", self)
                    

    @property
    def UML2WithID_Connector546(self):
        return self.__UML2WithID_Connector546

    @UML2WithID_Connector546.setter
    def UML2WithID_Connector546(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Connector__UML2WithID_Connector546", None)
        self.__UML2WithID_Connector546 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Message"):
                opp_val = getattr(old_value, "UML2WithID_Message", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Message", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Message"):
                opp_val = getattr(value, "UML2WithID_Message", None)
                setattr(value, "UML2WithID_Message", self)

    @property
    def UML2WithID_Connector(self):
        return self.__UML2WithID_Connector

    @UML2WithID_Connector.setter
    def UML2WithID_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Connector__UML2WithID_Connector", None)
        self.__UML2WithID_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Association281"):
                opp_val = getattr(old_value, "UML2WithID_Association281", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Association281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Association281"):
                opp_val = getattr(value, "UML2WithID_Association281", None)
                setattr(value, "UML2WithID_Association281", self)

    @property
    def UML2WithID_Connector300(self):
        return self.__UML2WithID_Connector300

    @UML2WithID_Connector300.setter
    def UML2WithID_Connector300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Connector__UML2WithID_Connector300", None)
        self.__UML2WithID_Connector300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StructuredClassifier299"):
                opp_val = getattr(old_value, "UML2WithID_StructuredClassifier299", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StructuredClassifier299"):
                opp_val = getattr(value, "UML2WithID_StructuredClassifier299", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_StructuredClassifier299", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LiteralSpecification:

    pass
class UML2WithID_LiteralNull(LiteralSpecification):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class UML2WithID_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class UML2WithID_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class UML2WithID_Substitution(Realization):

    pass
class UML2WithID_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: bool, Generalization: "UML2WithID_Classifier" = None, generalization: "UML2WithID_Classifier" = None, UML2WithID_Generalization: "UML2WithID_Classifier" = None, generalization180: set["UML2WithID_GeneralizationSet"] = None, Generalization265: "UML2WithID_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.Generalization = Generalization
        self.generalization = generalization
        self.UML2WithID_Generalization = UML2WithID_Generalization
        self.generalization180 = generalization180 if generalization180 is not None else set()
        self.Generalization265 = Generalization265
        
    @property
    def isSubstitutable(self) -> bool:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable

    @property
    def UML2WithID_Generalization(self):
        return self.__UML2WithID_Generalization

    @UML2WithID_Generalization.setter
    def UML2WithID_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Generalization__UML2WithID_Generalization", None)
        self.__UML2WithID_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Classifier178"):
                opp_val = getattr(old_value, "UML2WithID_Classifier178", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Classifier178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Classifier178"):
                opp_val = getattr(value, "UML2WithID_Classifier178", None)
                setattr(value, "UML2WithID_Classifier178", self)

    @property
    def Generalization265(self):
        return self.__Generalization265

    @Generalization265.setter
    def Generalization265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Generalization__Generalization265", None)
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

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Generalization__Generalization", None)
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
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Generalization__generalization", None)
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
        old_value = getattr(self, f"_UML2WithID_Generalization__generalization180", None)
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
                    

class RedefinableElement:

    pass
class UML2WithID_ExtensionPoint(RedefinableElement):

    pass
class UML2WithID_ActivityNode(RedefinableElement):

    pass
class UML2WithID_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, Feature: "UML2WithID_Classifier" = None, feature: set["UML2WithID_Classifier"] = None):
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
        old_value = getattr(self, f"_UML2WithID_Feature__feature", None)
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
        old_value = getattr(self, f"_UML2WithID_Feature__Feature", None)
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

class UML2WithID_Transition(RedefinableElement):

    def __init__(self, kind: str, Transition: "UML2WithID_Region" = None, transition: "UML2WithID_Region" = None, outgoing732: "UML2WithID_Vertex" = None, incoming735: "UML2WithID_Vertex" = None, UML2WithID_Transition: "UML2WithID_Transition" = None, UML2WithID_Transition737: "UML2WithID_Transition" = None, UML2WithID_Transition740: set["UML2WithID_Trigger"] = None, UML2WithID_Transition743: "UML2WithID_Constraint" = None, UML2WithID_Transition746: "UML2WithID_Activity" = None, Transition719: "UML2WithID_Vertex" = None, Transition722: "UML2WithID_Vertex" = None):
        self.kind = kind
        self.Transition = Transition
        self.transition = transition
        self.outgoing732 = outgoing732
        self.incoming735 = incoming735
        self.UML2WithID_Transition = UML2WithID_Transition
        self.UML2WithID_Transition737 = UML2WithID_Transition737
        self.UML2WithID_Transition740 = UML2WithID_Transition740 if UML2WithID_Transition740 is not None else set()
        self.UML2WithID_Transition743 = UML2WithID_Transition743
        self.UML2WithID_Transition746 = UML2WithID_Transition746
        self.Transition719 = Transition719
        self.Transition722 = Transition722
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Transition722(self):
        return self.__Transition722

    @Transition722.setter
    def Transition722(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__Transition722", None)
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
    def incoming735(self):
        return self.__incoming735

    @incoming735.setter
    def incoming735(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__incoming735", None)
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
    def outgoing732(self):
        return self.__outgoing732

    @outgoing732.setter
    def outgoing732(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__outgoing732", None)
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

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__Transition", None)
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
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__transition", None)
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
    def UML2WithID_Transition746(self):
        return self.__UML2WithID_Transition746

    @UML2WithID_Transition746.setter
    def UML2WithID_Transition746(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__UML2WithID_Transition746", None)
        self.__UML2WithID_Transition746 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Activity747"):
                opp_val = getattr(old_value, "UML2WithID_Activity747", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Activity747", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Activity747"):
                opp_val = getattr(value, "UML2WithID_Activity747", None)
                setattr(value, "UML2WithID_Activity747", self)

    @property
    def UML2WithID_Transition743(self):
        return self.__UML2WithID_Transition743

    @UML2WithID_Transition743.setter
    def UML2WithID_Transition743(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__UML2WithID_Transition743", None)
        self.__UML2WithID_Transition743 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Constraint744"):
                opp_val = getattr(old_value, "UML2WithID_Constraint744", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Constraint744", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Constraint744"):
                opp_val = getattr(value, "UML2WithID_Constraint744", None)
                setattr(value, "UML2WithID_Constraint744", self)

    @property
    def UML2WithID_Transition(self):
        return self.__UML2WithID_Transition

    @UML2WithID_Transition.setter
    def UML2WithID_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__UML2WithID_Transition", None)
        self.__UML2WithID_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Transition737"):
                opp_val = getattr(old_value, "UML2WithID_Transition737", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Transition737", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Transition737"):
                opp_val = getattr(value, "UML2WithID_Transition737", None)
                setattr(value, "UML2WithID_Transition737", self)

    @property
    def UML2WithID_Transition740(self):
        return self.__UML2WithID_Transition740

    @UML2WithID_Transition740.setter
    def UML2WithID_Transition740(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__UML2WithID_Transition740", None)
        self.__UML2WithID_Transition740 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Trigger741"):
                    opp_val = getattr(item, "UML2WithID_Trigger741", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Trigger741", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Trigger741"):
                    opp_val = getattr(item, "UML2WithID_Trigger741", None)
                    
                    setattr(item, "UML2WithID_Trigger741", self)
                    

    @property
    def UML2WithID_Transition737(self):
        return self.__UML2WithID_Transition737

    @UML2WithID_Transition737.setter
    def UML2WithID_Transition737(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__UML2WithID_Transition737", None)
        self.__UML2WithID_Transition737 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Transition"):
                opp_val = getattr(old_value, "UML2WithID_Transition", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Transition"):
                opp_val = getattr(value, "UML2WithID_Transition", None)
                setattr(value, "UML2WithID_Transition", self)

    @property
    def Transition719(self):
        return self.__Transition719

    @Transition719.setter
    def Transition719(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Transition__Transition719", None)
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

class UML2WithID_RedefinableTemplateSignature(TemplateSignature, RedefinableElement):

    pass
class UML2WithID_ActivityEdge(RedefinableElement):

    pass
class Type:

    pass
class InstanceSpecification:

    pass
class Classifier:

    pass
class UML2WithID_ParameterableClassifier(Classifier):

    pass
class UML2WithID_Artifact(Classifier, DeployedArtifact):

    def __init__(self, fileName: str, UML2WithID_Artifact: "UML2WithID_Artifact" = None, UML2WithID_Artifact396: set["UML2WithID_Artifact"] = None, UML2WithID_Artifact399: set["UML2WithID_Manifestation"] = None, UML2WithID_Artifact401: set["UML2WithID_Operation"] = None, UML2WithID_Artifact404: set["UML2WithID_Property"] = None):
        self.fileName = fileName
        self.UML2WithID_Artifact = UML2WithID_Artifact
        self.UML2WithID_Artifact396 = UML2WithID_Artifact396 if UML2WithID_Artifact396 is not None else set()
        self.UML2WithID_Artifact399 = UML2WithID_Artifact399 if UML2WithID_Artifact399 is not None else set()
        self.UML2WithID_Artifact401 = UML2WithID_Artifact401 if UML2WithID_Artifact401 is not None else set()
        self.UML2WithID_Artifact404 = UML2WithID_Artifact404 if UML2WithID_Artifact404 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def UML2WithID_Artifact401(self):
        return self.__UML2WithID_Artifact401

    @UML2WithID_Artifact401.setter
    def UML2WithID_Artifact401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Artifact__UML2WithID_Artifact401", None)
        self.__UML2WithID_Artifact401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Operation402"):
                    opp_val = getattr(item, "UML2WithID_Operation402", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Operation402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Operation402"):
                    opp_val = getattr(item, "UML2WithID_Operation402", None)
                    
                    setattr(item, "UML2WithID_Operation402", self)
                    

    @property
    def UML2WithID_Artifact404(self):
        return self.__UML2WithID_Artifact404

    @UML2WithID_Artifact404.setter
    def UML2WithID_Artifact404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Artifact__UML2WithID_Artifact404", None)
        self.__UML2WithID_Artifact404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Property405"):
                    opp_val = getattr(item, "UML2WithID_Property405", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Property405", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Property405"):
                    opp_val = getattr(item, "UML2WithID_Property405", None)
                    
                    setattr(item, "UML2WithID_Property405", self)
                    

    @property
    def UML2WithID_Artifact(self):
        return self.__UML2WithID_Artifact

    @UML2WithID_Artifact.setter
    def UML2WithID_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Artifact__UML2WithID_Artifact", None)
        self.__UML2WithID_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Artifact396"):
                opp_val = getattr(old_value, "UML2WithID_Artifact396", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Artifact396"):
                opp_val = getattr(value, "UML2WithID_Artifact396", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Artifact396", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Artifact399(self):
        return self.__UML2WithID_Artifact399

    @UML2WithID_Artifact399.setter
    def UML2WithID_Artifact399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Artifact__UML2WithID_Artifact399", None)
        self.__UML2WithID_Artifact399 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Manifestation"):
                    opp_val = getattr(item, "UML2WithID_Manifestation", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Manifestation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Manifestation"):
                    opp_val = getattr(item, "UML2WithID_Manifestation", None)
                    
                    setattr(item, "UML2WithID_Manifestation", self)
                    

    @property
    def UML2WithID_Artifact396(self):
        return self.__UML2WithID_Artifact396

    @UML2WithID_Artifact396.setter
    def UML2WithID_Artifact396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Artifact__UML2WithID_Artifact396", None)
        self.__UML2WithID_Artifact396 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Artifact"):
                    opp_val = getattr(item, "UML2WithID_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Artifact"):
                    opp_val = getattr(item, "UML2WithID_Artifact", None)
                    
                    setattr(item, "UML2WithID_Artifact", self)
                    

class UML2WithID_TemplateableClassifier(Classifier):

    pass
class UML2WithID_Interface(Classifier):

    pass
class UML2WithID_Actor(Classifier):

    pass
class UML2WithID_Signal(Classifier):

    pass
class UML2WithID_BehavioredClassifier(Classifier):

    pass
class UML2WithID_InformationItem(Classifier):

    pass
class UML2WithID_StructuredClassifier(Classifier):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification):

    pass
class DataType:

    pass
class UML2WithID_PrimitiveType(DataType):

    pass
class UML2WithID_Enumeration(DataType):

    pass
class UML2WithID_ProfileApplication(PackageImport):

    pass
class UML2WithID_PackageMerge(DirectedRelationship):

    pass
class Namespace:

    pass
class UML2WithID_InteractionOperand(InteractionFragment, Namespace):

    pass
class UML2WithID_State(Namespace, Vertex, RedefinableElement):

    def __init__(self, isComposite: bool, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, UML2WithID_State: "UML2WithID_ObjectNode" = None, UML2WithID_State691: "UML2WithID_StateMachine" = None, UML2WithID_State694: set["UML2WithID_ConnectionPointReference"] = None, UML2WithID_State697: "UML2WithID_State" = None, UML2WithID_State695: "UML2WithID_State" = None, UML2WithID_State699: set["UML2WithID_Trigger"] = None, state: set["UML2WithID_Region"] = None, UML2WithID_State704: "UML2WithID_Activity" = None, UML2WithID_State707: "UML2WithID_Activity" = None, State: "UML2WithID_Region" = None, UML2WithID_State710: "UML2WithID_Activity" = None, UML2WithID_State713: "UML2WithID_Constraint" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.UML2WithID_State = UML2WithID_State
        self.UML2WithID_State691 = UML2WithID_State691
        self.UML2WithID_State694 = UML2WithID_State694 if UML2WithID_State694 is not None else set()
        self.UML2WithID_State697 = UML2WithID_State697
        self.UML2WithID_State695 = UML2WithID_State695
        self.UML2WithID_State699 = UML2WithID_State699 if UML2WithID_State699 is not None else set()
        self.state = state if state is not None else set()
        self.UML2WithID_State704 = UML2WithID_State704
        self.UML2WithID_State707 = UML2WithID_State707
        self.State = State
        self.UML2WithID_State710 = UML2WithID_State710
        self.UML2WithID_State713 = UML2WithID_State713
        
    @property
    def isSubmachineState(self) -> bool:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isSimple(self) -> bool:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple

    @property
    def isOrthogonal(self) -> bool:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal

    @property
    def UML2WithID_State694(self):
        return self.__UML2WithID_State694

    @UML2WithID_State694.setter
    def UML2WithID_State694(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State694", None)
        self.__UML2WithID_State694 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ConnectionPointReference"):
                    opp_val = getattr(item, "UML2WithID_ConnectionPointReference", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ConnectionPointReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ConnectionPointReference"):
                    opp_val = getattr(item, "UML2WithID_ConnectionPointReference", None)
                    
                    setattr(item, "UML2WithID_ConnectionPointReference", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__State", None)
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
    def UML2WithID_State707(self):
        return self.__UML2WithID_State707

    @UML2WithID_State707.setter
    def UML2WithID_State707(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State707", None)
        self.__UML2WithID_State707 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Activity708"):
                opp_val = getattr(old_value, "UML2WithID_Activity708", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Activity708", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Activity708"):
                opp_val = getattr(value, "UML2WithID_Activity708", None)
                setattr(value, "UML2WithID_Activity708", self)

    @property
    def UML2WithID_State704(self):
        return self.__UML2WithID_State704

    @UML2WithID_State704.setter
    def UML2WithID_State704(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State704", None)
        self.__UML2WithID_State704 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Activity705"):
                opp_val = getattr(old_value, "UML2WithID_Activity705", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Activity705", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Activity705"):
                opp_val = getattr(value, "UML2WithID_Activity705", None)
                setattr(value, "UML2WithID_Activity705", self)

    @property
    def UML2WithID_State699(self):
        return self.__UML2WithID_State699

    @UML2WithID_State699.setter
    def UML2WithID_State699(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State699", None)
        self.__UML2WithID_State699 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Trigger700"):
                    opp_val = getattr(item, "UML2WithID_Trigger700", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Trigger700", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Trigger700"):
                    opp_val = getattr(item, "UML2WithID_Trigger700", None)
                    
                    setattr(item, "UML2WithID_Trigger700", self)
                    

    @property
    def UML2WithID_State691(self):
        return self.__UML2WithID_State691

    @UML2WithID_State691.setter
    def UML2WithID_State691(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State691", None)
        self.__UML2WithID_State691 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StateMachine692"):
                opp_val = getattr(old_value, "UML2WithID_StateMachine692", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_StateMachine692", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StateMachine692"):
                opp_val = getattr(value, "UML2WithID_StateMachine692", None)
                setattr(value, "UML2WithID_StateMachine692", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__state", None)
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
    def UML2WithID_State695(self):
        return self.__UML2WithID_State695

    @UML2WithID_State695.setter
    def UML2WithID_State695(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State695", None)
        self.__UML2WithID_State695 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_State697"):
                opp_val = getattr(old_value, "UML2WithID_State697", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_State697", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_State697"):
                opp_val = getattr(value, "UML2WithID_State697", None)
                setattr(value, "UML2WithID_State697", self)

    @property
    def UML2WithID_State697(self):
        return self.__UML2WithID_State697

    @UML2WithID_State697.setter
    def UML2WithID_State697(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State697", None)
        self.__UML2WithID_State697 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_State695"):
                opp_val = getattr(old_value, "UML2WithID_State695", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_State695", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_State695"):
                opp_val = getattr(value, "UML2WithID_State695", None)
                setattr(value, "UML2WithID_State695", self)

    @property
    def UML2WithID_State713(self):
        return self.__UML2WithID_State713

    @UML2WithID_State713.setter
    def UML2WithID_State713(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State713", None)
        self.__UML2WithID_State713 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Constraint714"):
                opp_val = getattr(old_value, "UML2WithID_Constraint714", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Constraint714", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Constraint714"):
                opp_val = getattr(value, "UML2WithID_Constraint714", None)
                setattr(value, "UML2WithID_Constraint714", self)

    @property
    def UML2WithID_State(self):
        return self.__UML2WithID_State

    @UML2WithID_State.setter
    def UML2WithID_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State", None)
        self.__UML2WithID_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ObjectNode360"):
                opp_val = getattr(old_value, "UML2WithID_ObjectNode360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ObjectNode360"):
                opp_val = getattr(value, "UML2WithID_ObjectNode360", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ObjectNode360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_State710(self):
        return self.__UML2WithID_State710

    @UML2WithID_State710.setter
    def UML2WithID_State710(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_State__UML2WithID_State710", None)
        self.__UML2WithID_State710 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Activity711"):
                opp_val = getattr(old_value, "UML2WithID_Activity711", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Activity711", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Activity711"):
                opp_val = getattr(value, "UML2WithID_Activity711", None)
                setattr(value, "UML2WithID_Activity711", self)

class UML2WithID_StructuredActivityNode(Namespace, Action, ActivityGroup):

    def __init__(self, mustIsolate: bool, UML2WithID_StructuredActivityNode: "UML2WithID_Activity" = None, StructuredActivityNode337: "UML2WithID_ActivityNode" = None, StructuredActivityNode: "UML2WithID_ActivityEdge" = None, StructuredActivityNode469: "UML2WithID_Variable" = None, scope: set["UML2WithID_Variable"] = None, inStructuredNode: set["UML2WithID_ActivityNode"] = None, inStructuredNode474: set["UML2WithID_ActivityEdge"] = None):
        self.mustIsolate = mustIsolate
        self.UML2WithID_StructuredActivityNode = UML2WithID_StructuredActivityNode
        self.StructuredActivityNode337 = StructuredActivityNode337
        self.StructuredActivityNode = StructuredActivityNode
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
        old_value = getattr(self, f"_UML2WithID_StructuredActivityNode__inStructuredNode", None)
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
    def StructuredActivityNode(self):
        return self.__StructuredActivityNode

    @StructuredActivityNode.setter
    def StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuredActivityNode__StructuredActivityNode", None)
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
    def StructuredActivityNode337(self):
        return self.__StructuredActivityNode337

    @StructuredActivityNode337.setter
    def StructuredActivityNode337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuredActivityNode__StructuredActivityNode337", None)
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
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuredActivityNode__scope", None)
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
    def UML2WithID_StructuredActivityNode(self):
        return self.__UML2WithID_StructuredActivityNode

    @UML2WithID_StructuredActivityNode.setter
    def UML2WithID_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuredActivityNode__UML2WithID_StructuredActivityNode", None)
        self.__UML2WithID_StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Activity249"):
                opp_val = getattr(old_value, "UML2WithID_Activity249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Activity249"):
                opp_val = getattr(value, "UML2WithID_Activity249", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Activity249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StructuredActivityNode469(self):
        return self.__StructuredActivityNode469

    @StructuredActivityNode469.setter
    def StructuredActivityNode469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuredActivityNode__StructuredActivityNode469", None)
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

    @property
    def inStructuredNode474(self):
        return self.__inStructuredNode474

    @inStructuredNode474.setter
    def inStructuredNode474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuredActivityNode__inStructuredNode474", None)
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
                    

class UML2WithID_Region(Namespace, RedefinableElement):

    pass
class UML2WithID_BehavioralFeature(Namespace, Feature):

    def __init__(self, isAbstract: bool, concurrency: str, UML2WithID_BehavioralFeature: set["UML2WithID_Parameter"] = None, UML2WithID_BehavioralFeature151: set["UML2WithID_Parameter"] = None, UML2WithID_BehavioralFeature154: set["UML2WithID_Parameter"] = None, UML2WithID_BehavioralFeature157: set["UML2WithID_Type"] = None, specification: set["UML2WithID_Behavior"] = None, BehavioralFeature: "UML2WithID_Behavior" = None):
        self.isAbstract = isAbstract
        self.concurrency = concurrency
        self.UML2WithID_BehavioralFeature = UML2WithID_BehavioralFeature if UML2WithID_BehavioralFeature is not None else set()
        self.UML2WithID_BehavioralFeature151 = UML2WithID_BehavioralFeature151 if UML2WithID_BehavioralFeature151 is not None else set()
        self.UML2WithID_BehavioralFeature154 = UML2WithID_BehavioralFeature154 if UML2WithID_BehavioralFeature154 is not None else set()
        self.UML2WithID_BehavioralFeature157 = UML2WithID_BehavioralFeature157 if UML2WithID_BehavioralFeature157 is not None else set()
        self.specification = specification if specification is not None else set()
        self.BehavioralFeature = BehavioralFeature
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def UML2WithID_BehavioralFeature(self):
        return self.__UML2WithID_BehavioralFeature

    @UML2WithID_BehavioralFeature.setter
    def UML2WithID_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_BehavioralFeature__UML2WithID_BehavioralFeature", None)
        self.__UML2WithID_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Parameter149"):
                    opp_val = getattr(item, "UML2WithID_Parameter149", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Parameter149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Parameter149"):
                    opp_val = getattr(item, "UML2WithID_Parameter149", None)
                    
                    setattr(item, "UML2WithID_Parameter149", self)
                    

    @property
    def UML2WithID_BehavioralFeature157(self):
        return self.__UML2WithID_BehavioralFeature157

    @UML2WithID_BehavioralFeature157.setter
    def UML2WithID_BehavioralFeature157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_BehavioralFeature__UML2WithID_BehavioralFeature157", None)
        self.__UML2WithID_BehavioralFeature157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Type158"):
                    opp_val = getattr(item, "UML2WithID_Type158", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Type158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Type158"):
                    opp_val = getattr(item, "UML2WithID_Type158", None)
                    
                    setattr(item, "UML2WithID_Type158", self)
                    

    @property
    def UML2WithID_BehavioralFeature154(self):
        return self.__UML2WithID_BehavioralFeature154

    @UML2WithID_BehavioralFeature154.setter
    def UML2WithID_BehavioralFeature154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_BehavioralFeature__UML2WithID_BehavioralFeature154", None)
        self.__UML2WithID_BehavioralFeature154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Parameter155"):
                    opp_val = getattr(item, "UML2WithID_Parameter155", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Parameter155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Parameter155"):
                    opp_val = getattr(item, "UML2WithID_Parameter155", None)
                    
                    setattr(item, "UML2WithID_Parameter155", self)
                    

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_BehavioralFeature__specification", None)
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
    def UML2WithID_BehavioralFeature151(self):
        return self.__UML2WithID_BehavioralFeature151

    @UML2WithID_BehavioralFeature151.setter
    def UML2WithID_BehavioralFeature151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_BehavioralFeature__UML2WithID_BehavioralFeature151", None)
        self.__UML2WithID_BehavioralFeature151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Parameter152"):
                    opp_val = getattr(item, "UML2WithID_Parameter152", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Parameter152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Parameter152"):
                    opp_val = getattr(item, "UML2WithID_Parameter152", None)
                    
                    setattr(item, "UML2WithID_Parameter152", self)
                    

    @property
    def BehavioralFeature(self):
        return self.__BehavioralFeature

    @BehavioralFeature.setter
    def BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_BehavioralFeature__BehavioralFeature", None)
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

class MultiplicityElement:

    pass
class UML2WithID_ConnectorEnd(MultiplicityElement):

    pass
class UML2WithID_Pin(ObjectNode, MultiplicityElement):

    pass
class BehavioralFeature:

    pass
class UML2WithID_DataType(Classifier):

    pass
class DeploymentTarget:

    pass
class UML2WithID_Node(Class, DeploymentTarget):

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class UML2WithID_Property(StructuralFeature, DeploymentTarget, ConnectableElement):

    def __init__(self, default: str, isComposite: bool, isDerived: bool, isDerivedUnion: bool, aggregation: str, UML2WithID_Property: "UML2WithID_Class" = None, UML2WithID_Property51: "UML2WithID_Property" = None, UML2WithID_Property49: "UML2WithID_Property" = None, ownedEnd: "UML2WithID_Association" = None, UML2WithID_Property55: "UML2WithID_Property" = None, UML2WithID_Property53: set["UML2WithID_Property"] = None, UML2WithID_Property58: "UML2WithID_Property" = None, UML2WithID_Property56: set["UML2WithID_Property"] = None, ownedAttribute: "UML2WithID_DataType" = None, memberEnd: "UML2WithID_Association" = None, UML2WithID_Property63: "UML2WithID_ValueSpecification" = None, Property: "UML2WithID_Property" = None, associationEnd: set["UML2WithID_Property"] = None, Property69: "UML2WithID_Property" = None, qualifier: "UML2WithID_Property" = None, Property108: "UML2WithID_DataType" = None, UML2WithID_Property123: "UML2WithID_Classifier" = None, Property191: "UML2WithID_Association" = None, Property195: "UML2WithID_Association" = None, UML2WithID_Property274: "UML2WithID_ConnectorEnd" = None, UML2WithID_Property278: "UML2WithID_ConnectorEnd" = None, UML2WithID_Property292: "UML2WithID_StructuredClassifier" = None, UML2WithID_Property295: "UML2WithID_StructuredClassifier" = None, UML2WithID_Property405: "UML2WithID_Artifact" = None, UML2WithID_Property377: "UML2WithID_Interface" = None, UML2WithID_Property463: "UML2WithID_Signal" = None, UML2WithID_Property782: "UML2WithID_LinkEndData" = None, UML2WithID_Property911: "UML2WithID_QualifierValue" = None, UML2WithID_Property919: "UML2WithID_ReadLinkObjectEndAction" = None, UML2WithID_Property930: "UML2WithID_ReadLinkObjectEndQualifierAction" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.aggregation = aggregation
        self.UML2WithID_Property = UML2WithID_Property
        self.UML2WithID_Property51 = UML2WithID_Property51
        self.UML2WithID_Property49 = UML2WithID_Property49
        self.ownedEnd = ownedEnd
        self.UML2WithID_Property55 = UML2WithID_Property55
        self.UML2WithID_Property53 = UML2WithID_Property53 if UML2WithID_Property53 is not None else set()
        self.UML2WithID_Property58 = UML2WithID_Property58
        self.UML2WithID_Property56 = UML2WithID_Property56 if UML2WithID_Property56 is not None else set()
        self.ownedAttribute = ownedAttribute
        self.memberEnd = memberEnd
        self.UML2WithID_Property63 = UML2WithID_Property63
        self.Property = Property
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.Property69 = Property69
        self.qualifier = qualifier
        self.Property108 = Property108
        self.UML2WithID_Property123 = UML2WithID_Property123
        self.Property191 = Property191
        self.Property195 = Property195
        self.UML2WithID_Property274 = UML2WithID_Property274
        self.UML2WithID_Property278 = UML2WithID_Property278
        self.UML2WithID_Property292 = UML2WithID_Property292
        self.UML2WithID_Property295 = UML2WithID_Property295
        self.UML2WithID_Property405 = UML2WithID_Property405
        self.UML2WithID_Property377 = UML2WithID_Property377
        self.UML2WithID_Property463 = UML2WithID_Property463
        self.UML2WithID_Property782 = UML2WithID_Property782
        self.UML2WithID_Property911 = UML2WithID_Property911
        self.UML2WithID_Property919 = UML2WithID_Property919
        self.UML2WithID_Property930 = UML2WithID_Property930
        
    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

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
    def UML2WithID_Property405(self):
        return self.__UML2WithID_Property405

    @UML2WithID_Property405.setter
    def UML2WithID_Property405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property405", None)
        self.__UML2WithID_Property405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Artifact404"):
                opp_val = getattr(old_value, "UML2WithID_Artifact404", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Artifact404"):
                opp_val = getattr(value, "UML2WithID_Artifact404", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Artifact404", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Property(self):
        return self.__UML2WithID_Property

    @UML2WithID_Property.setter
    def UML2WithID_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property", None)
        self.__UML2WithID_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Class48"):
                opp_val = getattr(old_value, "UML2WithID_Class48", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Class48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Class48"):
                opp_val = getattr(value, "UML2WithID_Class48", None)
                setattr(value, "UML2WithID_Class48", self)

    @property
    def UML2WithID_Property274(self):
        return self.__UML2WithID_Property274

    @UML2WithID_Property274.setter
    def UML2WithID_Property274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property274", None)
        self.__UML2WithID_Property274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ConnectorEnd"):
                opp_val = getattr(old_value, "UML2WithID_ConnectorEnd", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ConnectorEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ConnectorEnd"):
                opp_val = getattr(value, "UML2WithID_ConnectorEnd", None)
                setattr(value, "UML2WithID_ConnectorEnd", self)

    @property
    def UML2WithID_Property919(self):
        return self.__UML2WithID_Property919

    @UML2WithID_Property919.setter
    def UML2WithID_Property919(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property919", None)
        self.__UML2WithID_Property919 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ReadLinkObjectEndAction918"):
                opp_val = getattr(old_value, "UML2WithID_ReadLinkObjectEndAction918", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ReadLinkObjectEndAction918", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ReadLinkObjectEndAction918"):
                opp_val = getattr(value, "UML2WithID_ReadLinkObjectEndAction918", None)
                setattr(value, "UML2WithID_ReadLinkObjectEndAction918", self)

    @property
    def UML2WithID_Property377(self):
        return self.__UML2WithID_Property377

    @UML2WithID_Property377.setter
    def UML2WithID_Property377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property377", None)
        self.__UML2WithID_Property377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Interface"):
                opp_val = getattr(old_value, "UML2WithID_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Interface"):
                opp_val = getattr(value, "UML2WithID_Interface", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Property123(self):
        return self.__UML2WithID_Property123

    @UML2WithID_Property123.setter
    def UML2WithID_Property123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property123", None)
        self.__UML2WithID_Property123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Classifier122"):
                opp_val = getattr(old_value, "UML2WithID_Classifier122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Classifier122"):
                opp_val = getattr(value, "UML2WithID_Classifier122", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Classifier122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Property930(self):
        return self.__UML2WithID_Property930

    @UML2WithID_Property930.setter
    def UML2WithID_Property930(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property930", None)
        self.__UML2WithID_Property930 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ReadLinkObjectEndQualifierAction929"):
                opp_val = getattr(old_value, "UML2WithID_ReadLinkObjectEndQualifierAction929", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ReadLinkObjectEndQualifierAction929", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ReadLinkObjectEndQualifierAction929"):
                opp_val = getattr(value, "UML2WithID_ReadLinkObjectEndQualifierAction929", None)
                setattr(value, "UML2WithID_ReadLinkObjectEndQualifierAction929", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__ownedAttribute", None)
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
    def UML2WithID_Property63(self):
        return self.__UML2WithID_Property63

    @UML2WithID_Property63.setter
    def UML2WithID_Property63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property63", None)
        self.__UML2WithID_Property63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ValueSpecification64"):
                opp_val = getattr(old_value, "UML2WithID_ValueSpecification64", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ValueSpecification64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ValueSpecification64"):
                opp_val = getattr(value, "UML2WithID_ValueSpecification64", None)
                setattr(value, "UML2WithID_ValueSpecification64", self)

    @property
    def qualifier(self):
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__qualifier", None)
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
    def UML2WithID_Property295(self):
        return self.__UML2WithID_Property295

    @UML2WithID_Property295.setter
    def UML2WithID_Property295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property295", None)
        self.__UML2WithID_Property295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StructuredClassifier294"):
                opp_val = getattr(old_value, "UML2WithID_StructuredClassifier294", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StructuredClassifier294"):
                opp_val = getattr(value, "UML2WithID_StructuredClassifier294", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_StructuredClassifier294", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Property278(self):
        return self.__UML2WithID_Property278

    @UML2WithID_Property278.setter
    def UML2WithID_Property278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property278", None)
        self.__UML2WithID_Property278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ConnectorEnd277"):
                opp_val = getattr(old_value, "UML2WithID_ConnectorEnd277", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ConnectorEnd277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ConnectorEnd277"):
                opp_val = getattr(value, "UML2WithID_ConnectorEnd277", None)
                setattr(value, "UML2WithID_ConnectorEnd277", self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__memberEnd", None)
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
    def UML2WithID_Property53(self):
        return self.__UML2WithID_Property53

    @UML2WithID_Property53.setter
    def UML2WithID_Property53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property53", None)
        self.__UML2WithID_Property53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Property55"):
                    opp_val = getattr(item, "UML2WithID_Property55", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Property55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Property55"):
                    opp_val = getattr(item, "UML2WithID_Property55", None)
                    
                    setattr(item, "UML2WithID_Property55", self)
                    

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__ownedEnd", None)
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
    def UML2WithID_Property58(self):
        return self.__UML2WithID_Property58

    @UML2WithID_Property58.setter
    def UML2WithID_Property58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property58", None)
        self.__UML2WithID_Property58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Property56"):
                opp_val = getattr(old_value, "UML2WithID_Property56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Property56"):
                opp_val = getattr(value, "UML2WithID_Property56", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Property56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Property49(self):
        return self.__UML2WithID_Property49

    @UML2WithID_Property49.setter
    def UML2WithID_Property49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property49", None)
        self.__UML2WithID_Property49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Property51"):
                opp_val = getattr(old_value, "UML2WithID_Property51", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Property51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Property51"):
                opp_val = getattr(value, "UML2WithID_Property51", None)
                setattr(value, "UML2WithID_Property51", self)

    @property
    def UML2WithID_Property55(self):
        return self.__UML2WithID_Property55

    @UML2WithID_Property55.setter
    def UML2WithID_Property55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property55", None)
        self.__UML2WithID_Property55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Property53"):
                opp_val = getattr(old_value, "UML2WithID_Property53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Property53"):
                opp_val = getattr(value, "UML2WithID_Property53", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Property53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Property463(self):
        return self.__UML2WithID_Property463

    @UML2WithID_Property463.setter
    def UML2WithID_Property463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property463", None)
        self.__UML2WithID_Property463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Signal462"):
                opp_val = getattr(old_value, "UML2WithID_Signal462", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Signal462"):
                opp_val = getattr(value, "UML2WithID_Signal462", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Signal462", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property108(self):
        return self.__Property108

    @Property108.setter
    def Property108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__Property108", None)
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
    def UML2WithID_Property911(self):
        return self.__UML2WithID_Property911

    @UML2WithID_Property911.setter
    def UML2WithID_Property911(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property911", None)
        self.__UML2WithID_Property911 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_QualifierValue910"):
                opp_val = getattr(old_value, "UML2WithID_QualifierValue910", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_QualifierValue910", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_QualifierValue910"):
                opp_val = getattr(value, "UML2WithID_QualifierValue910", None)
                setattr(value, "UML2WithID_QualifierValue910", self)

    @property
    def Property195(self):
        return self.__Property195

    @Property195.setter
    def Property195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__Property195", None)
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
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__Property", None)
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
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__associationEnd", None)
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
    def UML2WithID_Property292(self):
        return self.__UML2WithID_Property292

    @UML2WithID_Property292.setter
    def UML2WithID_Property292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property292", None)
        self.__UML2WithID_Property292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StructuredClassifier"):
                opp_val = getattr(old_value, "UML2WithID_StructuredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StructuredClassifier"):
                opp_val = getattr(value, "UML2WithID_StructuredClassifier", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_StructuredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Property51(self):
        return self.__UML2WithID_Property51

    @UML2WithID_Property51.setter
    def UML2WithID_Property51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property51", None)
        self.__UML2WithID_Property51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Property49"):
                opp_val = getattr(old_value, "UML2WithID_Property49", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Property49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Property49"):
                opp_val = getattr(value, "UML2WithID_Property49", None)
                setattr(value, "UML2WithID_Property49", self)

    @property
    def UML2WithID_Property56(self):
        return self.__UML2WithID_Property56

    @UML2WithID_Property56.setter
    def UML2WithID_Property56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property56", None)
        self.__UML2WithID_Property56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Property58"):
                    opp_val = getattr(item, "UML2WithID_Property58", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Property58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Property58"):
                    opp_val = getattr(item, "UML2WithID_Property58", None)
                    
                    setattr(item, "UML2WithID_Property58", self)
                    

    @property
    def UML2WithID_Property782(self):
        return self.__UML2WithID_Property782

    @UML2WithID_Property782.setter
    def UML2WithID_Property782(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property782", None)
        self.__UML2WithID_Property782 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_LinkEndData781"):
                opp_val = getattr(old_value, "UML2WithID_LinkEndData781", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_LinkEndData781", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_LinkEndData781"):
                opp_val = getattr(value, "UML2WithID_LinkEndData781", None)
                setattr(value, "UML2WithID_LinkEndData781", self)

    @property
    def Property69(self):
        return self.__Property69

    @Property69.setter
    def Property69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__Property69", None)
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
    def Property191(self):
        return self.__Property191

    @Property191.setter
    def Property191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__Property191", None)
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

class PackageableElement:

    pass
class UML2WithID_PrimitiveFunction(PackageableElement):

    def __init__(self, body: str, language: str, UML2WithID_PrimitiveFunction: "UML2WithID_ApplyFunctionAction" = None):
        self.body = body
        self.language = language
        self.UML2WithID_PrimitiveFunction = UML2WithID_PrimitiveFunction
        
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
    def UML2WithID_PrimitiveFunction(self):
        return self.__UML2WithID_PrimitiveFunction

    @UML2WithID_PrimitiveFunction.setter
    def UML2WithID_PrimitiveFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PrimitiveFunction__UML2WithID_PrimitiveFunction", None)
        self.__UML2WithID_PrimitiveFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ApplyFunctionAction"):
                opp_val = getattr(old_value, "UML2WithID_ApplyFunctionAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ApplyFunctionAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ApplyFunctionAction"):
                opp_val = getattr(value, "UML2WithID_ApplyFunctionAction", None)
                setattr(value, "UML2WithID_ApplyFunctionAction", self)

class UML2WithID_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: bool, isDisjoint: bool, GeneralizationSet: "UML2WithID_Classifier" = None, GeneralizationSet181: "UML2WithID_Generalization" = None, powertypeExtent: "UML2WithID_Classifier" = None, generalizationSet: set["UML2WithID_Generalization"] = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.GeneralizationSet = GeneralizationSet
        self.GeneralizationSet181 = GeneralizationSet181
        self.powertypeExtent = powertypeExtent
        self.generalizationSet = generalizationSet if generalizationSet is not None else set()
        
    @property
    def isCovering(self) -> bool:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering

    @property
    def isDisjoint(self) -> bool:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint

    @property
    def powertypeExtent(self):
        return self.__powertypeExtent

    @powertypeExtent.setter
    def powertypeExtent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_GeneralizationSet__powertypeExtent", None)
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
        old_value = getattr(self, f"_UML2WithID_GeneralizationSet__generalizationSet", None)
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
                    

    @property
    def GeneralizationSet(self):
        return self.__GeneralizationSet

    @GeneralizationSet.setter
    def GeneralizationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_GeneralizationSet__GeneralizationSet", None)
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
    def GeneralizationSet181(self):
        return self.__GeneralizationSet181

    @GeneralizationSet181.setter
    def GeneralizationSet181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_GeneralizationSet__GeneralizationSet181", None)
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

class UML2WithID_Package(Namespace, PackageableElement):

    pass
class UML2WithID_InformationFlow(PackageableElement, DirectedRelationship):

    pass
class UML2WithID_InstanceSpecification(PackageableElement, DeploymentTarget, DeployedArtifact):

    pass
class UML2WithID_Type(PackageableElement):

    pass
class UML2WithID_Reception(BehavioralFeature):

    pass
class UML2WithID_Classifier(Namespace, RedefinableElement, Type):

    def __init__(self, isAbstract: bool, UML2WithID_Classifier: "UML2WithID_Class" = None, featuringClassifier: set["UML2WithID_Feature"] = None, UML2WithID_Classifier115: set["UML2WithID_NamedElement"] = None, UML2WithID_Classifier119: "UML2WithID_Classifier" = None, UML2WithID_Classifier117: set["UML2WithID_Classifier"] = None, specific: set["UML2WithID_Generalization"] = None, UML2WithID_Classifier122: set["UML2WithID_Property"] = None, UML2WithID_Classifier126: "UML2WithID_Classifier" = None, UML2WithID_Classifier124: set["UML2WithID_Classifier"] = None, substitutingClassifier: set["UML2WithID_Substitution"] = None, powertype: set["UML2WithID_GeneralizationSet"] = None, UML2WithID_Classifier130: set["UML2WithID_UseCase"] = None, subject: set["UML2WithID_UseCase"] = None, UML2WithID_Classifier133: "UML2WithID_CollaborationOccurrence" = None, UML2WithID_Classifier135: set["UML2WithID_CollaborationOccurrence"] = None, Classifier: "UML2WithID_Feature" = None, UML2WithID_Classifier174: "UML2WithID_RedefinableElement" = None, UML2WithID_Classifier162: "UML2WithID_InstanceSpecification" = None, Classifier176: "UML2WithID_Generalization" = None, UML2WithID_Classifier178: "UML2WithID_Generalization" = None, UML2WithID_Classifier267: "UML2WithID_InformationItem" = None, UML2WithID_Classifier272: "UML2WithID_InformationFlow" = None, UML2WithID_Classifier257: "UML2WithID_Realization" = None, UML2WithID_Classifier259: "UML2WithID_Substitution" = None, Classifier261: "UML2WithID_Substitution" = None, Classifier263: "UML2WithID_GeneralizationSet" = None, UML2WithID_Classifier350: "UML2WithID_Action" = None, UML2WithID_Classifier386: "UML2WithID_Interface" = None, Classifier424: "UML2WithID_UseCase" = None, UML2WithID_Classifier651: "UML2WithID_ExceptionHandler" = None, UML2WithID_Classifier749: "UML2WithID_CreateObjectAction" = None, UML2WithID_Classifier900: "UML2WithID_ReadIsClassifiedObjectAction" = None, UML2WithID_Classifier890: "UML2WithID_ReadExtentAction" = None, UML2WithID_Classifier892: "UML2WithID_ReclassifyObjectAction" = None, UML2WithID_Classifier895: "UML2WithID_ReclassifyObjectAction" = None):
        self.isAbstract = isAbstract
        self.UML2WithID_Classifier = UML2WithID_Classifier
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.UML2WithID_Classifier115 = UML2WithID_Classifier115 if UML2WithID_Classifier115 is not None else set()
        self.UML2WithID_Classifier119 = UML2WithID_Classifier119
        self.UML2WithID_Classifier117 = UML2WithID_Classifier117 if UML2WithID_Classifier117 is not None else set()
        self.specific = specific if specific is not None else set()
        self.UML2WithID_Classifier122 = UML2WithID_Classifier122 if UML2WithID_Classifier122 is not None else set()
        self.UML2WithID_Classifier126 = UML2WithID_Classifier126
        self.UML2WithID_Classifier124 = UML2WithID_Classifier124 if UML2WithID_Classifier124 is not None else set()
        self.substitutingClassifier = substitutingClassifier if substitutingClassifier is not None else set()
        self.powertype = powertype if powertype is not None else set()
        self.UML2WithID_Classifier130 = UML2WithID_Classifier130 if UML2WithID_Classifier130 is not None else set()
        self.subject = subject if subject is not None else set()
        self.UML2WithID_Classifier133 = UML2WithID_Classifier133
        self.UML2WithID_Classifier135 = UML2WithID_Classifier135 if UML2WithID_Classifier135 is not None else set()
        self.Classifier = Classifier
        self.UML2WithID_Classifier174 = UML2WithID_Classifier174
        self.UML2WithID_Classifier162 = UML2WithID_Classifier162
        self.Classifier176 = Classifier176
        self.UML2WithID_Classifier178 = UML2WithID_Classifier178
        self.UML2WithID_Classifier267 = UML2WithID_Classifier267
        self.UML2WithID_Classifier272 = UML2WithID_Classifier272
        self.UML2WithID_Classifier257 = UML2WithID_Classifier257
        self.UML2WithID_Classifier259 = UML2WithID_Classifier259
        self.Classifier261 = Classifier261
        self.Classifier263 = Classifier263
        self.UML2WithID_Classifier350 = UML2WithID_Classifier350
        self.UML2WithID_Classifier386 = UML2WithID_Classifier386
        self.Classifier424 = Classifier424
        self.UML2WithID_Classifier651 = UML2WithID_Classifier651
        self.UML2WithID_Classifier749 = UML2WithID_Classifier749
        self.UML2WithID_Classifier900 = UML2WithID_Classifier900
        self.UML2WithID_Classifier890 = UML2WithID_Classifier890
        self.UML2WithID_Classifier892 = UML2WithID_Classifier892
        self.UML2WithID_Classifier895 = UML2WithID_Classifier895
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2WithID_Classifier651(self):
        return self.__UML2WithID_Classifier651

    @UML2WithID_Classifier651.setter
    def UML2WithID_Classifier651(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier651", None)
        self.__UML2WithID_Classifier651 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ExceptionHandler650"):
                opp_val = getattr(old_value, "UML2WithID_ExceptionHandler650", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ExceptionHandler650"):
                opp_val = getattr(value, "UML2WithID_ExceptionHandler650", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ExceptionHandler650", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Classifier259(self):
        return self.__UML2WithID_Classifier259

    @UML2WithID_Classifier259.setter
    def UML2WithID_Classifier259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier259", None)
        self.__UML2WithID_Classifier259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Substitution"):
                opp_val = getattr(old_value, "UML2WithID_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Substitution"):
                opp_val = getattr(value, "UML2WithID_Substitution", None)
                setattr(value, "UML2WithID_Substitution", self)

    @property
    def UML2WithID_Classifier130(self):
        return self.__UML2WithID_Classifier130

    @UML2WithID_Classifier130.setter
    def UML2WithID_Classifier130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier130", None)
        self.__UML2WithID_Classifier130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_UseCase"):
                    opp_val = getattr(item, "UML2WithID_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_UseCase"):
                    opp_val = getattr(item, "UML2WithID_UseCase", None)
                    
                    setattr(item, "UML2WithID_UseCase", self)
                    

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__specific", None)
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
    def UML2WithID_Classifier115(self):
        return self.__UML2WithID_Classifier115

    @UML2WithID_Classifier115.setter
    def UML2WithID_Classifier115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier115", None)
        self.__UML2WithID_Classifier115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_NamedElement116"):
                    opp_val = getattr(item, "UML2WithID_NamedElement116", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_NamedElement116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_NamedElement116"):
                    opp_val = getattr(item, "UML2WithID_NamedElement116", None)
                    
                    setattr(item, "UML2WithID_NamedElement116", self)
                    

    @property
    def UML2WithID_Classifier895(self):
        return self.__UML2WithID_Classifier895

    @UML2WithID_Classifier895.setter
    def UML2WithID_Classifier895(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier895", None)
        self.__UML2WithID_Classifier895 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ReclassifyObjectAction894"):
                opp_val = getattr(old_value, "UML2WithID_ReclassifyObjectAction894", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ReclassifyObjectAction894"):
                opp_val = getattr(value, "UML2WithID_ReclassifyObjectAction894", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ReclassifyObjectAction894", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier176(self):
        return self.__Classifier176

    @Classifier176.setter
    def Classifier176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__Classifier176", None)
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
    def UML2WithID_Classifier892(self):
        return self.__UML2WithID_Classifier892

    @UML2WithID_Classifier892.setter
    def UML2WithID_Classifier892(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier892", None)
        self.__UML2WithID_Classifier892 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ReclassifyObjectAction"):
                opp_val = getattr(old_value, "UML2WithID_ReclassifyObjectAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ReclassifyObjectAction"):
                opp_val = getattr(value, "UML2WithID_ReclassifyObjectAction", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ReclassifyObjectAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Classifier267(self):
        return self.__UML2WithID_Classifier267

    @UML2WithID_Classifier267.setter
    def UML2WithID_Classifier267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier267", None)
        self.__UML2WithID_Classifier267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InformationItem"):
                opp_val = getattr(old_value, "UML2WithID_InformationItem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InformationItem"):
                opp_val = getattr(value, "UML2WithID_InformationItem", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_InformationItem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Classifier126(self):
        return self.__UML2WithID_Classifier126

    @UML2WithID_Classifier126.setter
    def UML2WithID_Classifier126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier126", None)
        self.__UML2WithID_Classifier126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Classifier124"):
                opp_val = getattr(old_value, "UML2WithID_Classifier124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Classifier124"):
                opp_val = getattr(value, "UML2WithID_Classifier124", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Classifier124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Classifier174(self):
        return self.__UML2WithID_Classifier174

    @UML2WithID_Classifier174.setter
    def UML2WithID_Classifier174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier174", None)
        self.__UML2WithID_Classifier174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_RedefinableElement"):
                opp_val = getattr(old_value, "UML2WithID_RedefinableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_RedefinableElement"):
                opp_val = getattr(value, "UML2WithID_RedefinableElement", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_RedefinableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier261(self):
        return self.__Classifier261

    @Classifier261.setter
    def Classifier261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__Classifier261", None)
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
    def Classifier263(self):
        return self.__Classifier263

    @Classifier263.setter
    def Classifier263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__Classifier263", None)
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
    def UML2WithID_Classifier133(self):
        return self.__UML2WithID_Classifier133

    @UML2WithID_Classifier133.setter
    def UML2WithID_Classifier133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier133", None)
        self.__UML2WithID_Classifier133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_CollaborationOccurrence"):
                opp_val = getattr(old_value, "UML2WithID_CollaborationOccurrence", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_CollaborationOccurrence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_CollaborationOccurrence"):
                opp_val = getattr(value, "UML2WithID_CollaborationOccurrence", None)
                setattr(value, "UML2WithID_CollaborationOccurrence", self)

    @property
    def UML2WithID_Classifier749(self):
        return self.__UML2WithID_Classifier749

    @UML2WithID_Classifier749.setter
    def UML2WithID_Classifier749(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier749", None)
        self.__UML2WithID_Classifier749 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_CreateObjectAction"):
                opp_val = getattr(old_value, "UML2WithID_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_CreateObjectAction"):
                opp_val = getattr(value, "UML2WithID_CreateObjectAction", None)
                setattr(value, "UML2WithID_CreateObjectAction", self)

    @property
    def Classifier424(self):
        return self.__Classifier424

    @Classifier424.setter
    def Classifier424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__Classifier424", None)
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
    def UML2WithID_Classifier135(self):
        return self.__UML2WithID_Classifier135

    @UML2WithID_Classifier135.setter
    def UML2WithID_Classifier135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier135", None)
        self.__UML2WithID_Classifier135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_CollaborationOccurrence136"):
                    opp_val = getattr(item, "UML2WithID_CollaborationOccurrence136", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_CollaborationOccurrence136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_CollaborationOccurrence136"):
                    opp_val = getattr(item, "UML2WithID_CollaborationOccurrence136", None)
                    
                    setattr(item, "UML2WithID_CollaborationOccurrence136", self)
                    

    @property
    def UML2WithID_Classifier178(self):
        return self.__UML2WithID_Classifier178

    @UML2WithID_Classifier178.setter
    def UML2WithID_Classifier178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier178", None)
        self.__UML2WithID_Classifier178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Generalization"):
                opp_val = getattr(old_value, "UML2WithID_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Generalization"):
                opp_val = getattr(value, "UML2WithID_Generalization", None)
                setattr(value, "UML2WithID_Generalization", self)

    @property
    def powertype(self):
        return self.__powertype

    @powertype.setter
    def powertype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__powertype", None)
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
    def UML2WithID_Classifier117(self):
        return self.__UML2WithID_Classifier117

    @UML2WithID_Classifier117.setter
    def UML2WithID_Classifier117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier117", None)
        self.__UML2WithID_Classifier117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Classifier119"):
                    opp_val = getattr(item, "UML2WithID_Classifier119", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Classifier119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Classifier119"):
                    opp_val = getattr(item, "UML2WithID_Classifier119", None)
                    
                    setattr(item, "UML2WithID_Classifier119", self)
                    

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__subject", None)
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
    def UML2WithID_Classifier386(self):
        return self.__UML2WithID_Classifier386

    @UML2WithID_Classifier386.setter
    def UML2WithID_Classifier386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier386", None)
        self.__UML2WithID_Classifier386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Interface385"):
                opp_val = getattr(old_value, "UML2WithID_Interface385", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Interface385"):
                opp_val = getattr(value, "UML2WithID_Interface385", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Interface385", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def substitutingClassifier(self):
        return self.__substitutingClassifier

    @substitutingClassifier.setter
    def substitutingClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__substitutingClassifier", None)
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
    def UML2WithID_Classifier122(self):
        return self.__UML2WithID_Classifier122

    @UML2WithID_Classifier122.setter
    def UML2WithID_Classifier122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier122", None)
        self.__UML2WithID_Classifier122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Property123"):
                    opp_val = getattr(item, "UML2WithID_Property123", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Property123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Property123"):
                    opp_val = getattr(item, "UML2WithID_Property123", None)
                    
                    setattr(item, "UML2WithID_Property123", self)
                    

    @property
    def UML2WithID_Classifier119(self):
        return self.__UML2WithID_Classifier119

    @UML2WithID_Classifier119.setter
    def UML2WithID_Classifier119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier119", None)
        self.__UML2WithID_Classifier119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Classifier117"):
                opp_val = getattr(old_value, "UML2WithID_Classifier117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Classifier117"):
                opp_val = getattr(value, "UML2WithID_Classifier117", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Classifier117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Classifier124(self):
        return self.__UML2WithID_Classifier124

    @UML2WithID_Classifier124.setter
    def UML2WithID_Classifier124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier124", None)
        self.__UML2WithID_Classifier124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Classifier126"):
                    opp_val = getattr(item, "UML2WithID_Classifier126", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Classifier126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Classifier126"):
                    opp_val = getattr(item, "UML2WithID_Classifier126", None)
                    
                    setattr(item, "UML2WithID_Classifier126", self)
                    

    @property
    def UML2WithID_Classifier890(self):
        return self.__UML2WithID_Classifier890

    @UML2WithID_Classifier890.setter
    def UML2WithID_Classifier890(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier890", None)
        self.__UML2WithID_Classifier890 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ReadExtentAction889"):
                opp_val = getattr(old_value, "UML2WithID_ReadExtentAction889", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ReadExtentAction889", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ReadExtentAction889"):
                opp_val = getattr(value, "UML2WithID_ReadExtentAction889", None)
                setattr(value, "UML2WithID_ReadExtentAction889", self)

    @property
    def UML2WithID_Classifier272(self):
        return self.__UML2WithID_Classifier272

    @UML2WithID_Classifier272.setter
    def UML2WithID_Classifier272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier272", None)
        self.__UML2WithID_Classifier272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InformationFlow271"):
                opp_val = getattr(old_value, "UML2WithID_InformationFlow271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InformationFlow271"):
                opp_val = getattr(value, "UML2WithID_InformationFlow271", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_InformationFlow271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Classifier257(self):
        return self.__UML2WithID_Classifier257

    @UML2WithID_Classifier257.setter
    def UML2WithID_Classifier257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier257", None)
        self.__UML2WithID_Classifier257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Realization"):
                opp_val = getattr(old_value, "UML2WithID_Realization", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Realization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Realization"):
                opp_val = getattr(value, "UML2WithID_Realization", None)
                setattr(value, "UML2WithID_Realization", self)

    @property
    def UML2WithID_Classifier350(self):
        return self.__UML2WithID_Classifier350

    @UML2WithID_Classifier350.setter
    def UML2WithID_Classifier350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier350", None)
        self.__UML2WithID_Classifier350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Action349"):
                opp_val = getattr(old_value, "UML2WithID_Action349", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Action349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Action349"):
                opp_val = getattr(value, "UML2WithID_Action349", None)
                setattr(value, "UML2WithID_Action349", self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__Classifier", None)
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
    def UML2WithID_Classifier900(self):
        return self.__UML2WithID_Classifier900

    @UML2WithID_Classifier900.setter
    def UML2WithID_Classifier900(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier900", None)
        self.__UML2WithID_Classifier900 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ReadIsClassifiedObjectAction"):
                opp_val = getattr(old_value, "UML2WithID_ReadIsClassifiedObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ReadIsClassifiedObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ReadIsClassifiedObjectAction"):
                opp_val = getattr(value, "UML2WithID_ReadIsClassifiedObjectAction", None)
                setattr(value, "UML2WithID_ReadIsClassifiedObjectAction", self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__featuringClassifier", None)
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
    def UML2WithID_Classifier162(self):
        return self.__UML2WithID_Classifier162

    @UML2WithID_Classifier162.setter
    def UML2WithID_Classifier162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier162", None)
        self.__UML2WithID_Classifier162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_InstanceSpecification"):
                opp_val = getattr(old_value, "UML2WithID_InstanceSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_InstanceSpecification"):
                opp_val = getattr(value, "UML2WithID_InstanceSpecification", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_InstanceSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Classifier(self):
        return self.__UML2WithID_Classifier

    @UML2WithID_Classifier.setter
    def UML2WithID_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Classifier__UML2WithID_Classifier", None)
        self.__UML2WithID_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Class43"):
                opp_val = getattr(old_value, "UML2WithID_Class43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Class43"):
                opp_val = getattr(value, "UML2WithID_Class43", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Class43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2WithID_Extension(Association):

    def __init__(self, isRequired: bool, Extension: "UML2WithID_Class" = None, extension: "UML2WithID_Class" = None):
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
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Extension__extension", None)
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

    @property
    def Extension(self):
        return self.__Extension

    @Extension.setter
    def Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Extension__Extension", None)
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

class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2WithID_UseCase(BehavioredClassifier):

    pass
class UML2WithID_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2WithID_Class(EncapsulatedClassifier, BehavioredClassifier):

    def __init__(self, isActive: bool, class_: set["UML2WithID_Operation"] = None, UML2WithID_Class: "UML2WithID_Class" = None, UML2WithID_Class39: set["UML2WithID_Class"] = None, metaclass: set["UML2WithID_Extension"] = None, UML2WithID_Class43: set["UML2WithID_Classifier"] = None, UML2WithID_Class45: set["UML2WithID_Reception"] = None, UML2WithID_Class48: "UML2WithID_Property" = None, Class: "UML2WithID_Operation" = None, Class212: "UML2WithID_Extension" = None):
        self.isActive = isActive
        self.class_ = class_ if class_ is not None else set()
        self.UML2WithID_Class = UML2WithID_Class
        self.UML2WithID_Class39 = UML2WithID_Class39 if UML2WithID_Class39 is not None else set()
        self.metaclass = metaclass if metaclass is not None else set()
        self.UML2WithID_Class43 = UML2WithID_Class43 if UML2WithID_Class43 is not None else set()
        self.UML2WithID_Class45 = UML2WithID_Class45 if UML2WithID_Class45 is not None else set()
        self.UML2WithID_Class48 = UML2WithID_Class48
        self.Class = Class
        self.Class212 = Class212
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def UML2WithID_Class45(self):
        return self.__UML2WithID_Class45

    @UML2WithID_Class45.setter
    def UML2WithID_Class45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__UML2WithID_Class45", None)
        self.__UML2WithID_Class45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Reception"):
                    opp_val = getattr(item, "UML2WithID_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Reception"):
                    opp_val = getattr(item, "UML2WithID_Reception", None)
                    
                    setattr(item, "UML2WithID_Reception", self)
                    

    @property
    def UML2WithID_Class(self):
        return self.__UML2WithID_Class

    @UML2WithID_Class.setter
    def UML2WithID_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__UML2WithID_Class", None)
        self.__UML2WithID_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Class39"):
                opp_val = getattr(old_value, "UML2WithID_Class39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Class39"):
                opp_val = getattr(value, "UML2WithID_Class39", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Class39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Class43(self):
        return self.__UML2WithID_Class43

    @UML2WithID_Class43.setter
    def UML2WithID_Class43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__UML2WithID_Class43", None)
        self.__UML2WithID_Class43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Classifier"):
                    opp_val = getattr(item, "UML2WithID_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Classifier"):
                    opp_val = getattr(item, "UML2WithID_Classifier", None)
                    
                    setattr(item, "UML2WithID_Classifier", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__Class", None)
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
    def Class212(self):
        return self.__Class212

    @Class212.setter
    def Class212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__Class212", None)
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
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__class_", None)
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
    def UML2WithID_Class48(self):
        return self.__UML2WithID_Class48

    @UML2WithID_Class48.setter
    def UML2WithID_Class48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__UML2WithID_Class48", None)
        self.__UML2WithID_Class48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Property"):
                opp_val = getattr(old_value, "UML2WithID_Property", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Property"):
                opp_val = getattr(value, "UML2WithID_Property", None)
                setattr(value, "UML2WithID_Property", self)

    @property
    def metaclass(self):
        return self.__metaclass

    @metaclass.setter
    def metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__metaclass", None)
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
    def UML2WithID_Class39(self):
        return self.__UML2WithID_Class39

    @UML2WithID_Class39.setter
    def UML2WithID_Class39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Class__UML2WithID_Class39", None)
        self.__UML2WithID_Class39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Class"):
                    opp_val = getattr(item, "UML2WithID_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Class"):
                    opp_val = getattr(item, "UML2WithID_Class", None)
                    
                    setattr(item, "UML2WithID_Class", self)
                    

class Relationship:

    pass
class UML2WithID_Association(Classifier, Relationship):

    def __init__(self, isDerived: bool, Association: "UML2WithID_Property" = None, Association61: "UML2WithID_Property" = None, owningAssociation: set["UML2WithID_Property"] = None, UML2WithID_Association: set["UML2WithID_Type"] = None, association: set["UML2WithID_Property"] = None, UML2WithID_Association281: "UML2WithID_Connector" = None, UML2WithID_Association793: "UML2WithID_ClearAssociationAction" = None):
        self.isDerived = isDerived
        self.Association = Association
        self.Association61 = Association61
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        self.UML2WithID_Association = UML2WithID_Association if UML2WithID_Association is not None else set()
        self.association = association if association is not None else set()
        self.UML2WithID_Association281 = UML2WithID_Association281
        self.UML2WithID_Association793 = UML2WithID_Association793
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def UML2WithID_Association(self):
        return self.__UML2WithID_Association

    @UML2WithID_Association.setter
    def UML2WithID_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Association__UML2WithID_Association", None)
        self.__UML2WithID_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Type193"):
                    opp_val = getattr(item, "UML2WithID_Type193", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Type193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Type193"):
                    opp_val = getattr(item, "UML2WithID_Type193", None)
                    
                    setattr(item, "UML2WithID_Type193", self)
                    

    @property
    def UML2WithID_Association281(self):
        return self.__UML2WithID_Association281

    @UML2WithID_Association281.setter
    def UML2WithID_Association281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Association__UML2WithID_Association281", None)
        self.__UML2WithID_Association281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Connector"):
                opp_val = getattr(old_value, "UML2WithID_Connector", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Connector"):
                opp_val = getattr(value, "UML2WithID_Connector", None)
                setattr(value, "UML2WithID_Connector", self)

    @property
    def UML2WithID_Association793(self):
        return self.__UML2WithID_Association793

    @UML2WithID_Association793.setter
    def UML2WithID_Association793(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Association__UML2WithID_Association793", None)
        self.__UML2WithID_Association793 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ClearAssociationAction792"):
                opp_val = getattr(old_value, "UML2WithID_ClearAssociationAction792", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ClearAssociationAction792", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ClearAssociationAction792"):
                opp_val = getattr(value, "UML2WithID_ClearAssociationAction792", None)
                setattr(value, "UML2WithID_ClearAssociationAction792", self)

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Association__association", None)
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
        old_value = getattr(self, f"_UML2WithID_Association__owningAssociation", None)
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
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Association__Association", None)
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
    def Association61(self):
        return self.__Association61

    @Association61.setter
    def Association61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Association__Association61", None)
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

class UML2WithID_DirectedRelationship(Relationship):

    pass
class OpaqueExpression:

    pass
class UML2WithID_Expression(OpaqueExpression):

    def __init__(self, symbol: str, UML2WithID_Expression: set["UML2WithID_ValueSpecification"] = None):
        self.symbol = symbol
        self.UML2WithID_Expression = UML2WithID_Expression if UML2WithID_Expression is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def UML2WithID_Expression(self):
        return self.__UML2WithID_Expression

    @UML2WithID_Expression.setter
    def UML2WithID_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Expression__UML2WithID_Expression", None)
        self.__UML2WithID_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ValueSpecification24"):
                    opp_val = getattr(item, "UML2WithID_ValueSpecification24", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ValueSpecification24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ValueSpecification24"):
                    opp_val = getattr(item, "UML2WithID_ValueSpecification24", None)
                    
                    setattr(item, "UML2WithID_ValueSpecification24", self)
                    

class ParameterableElement:

    pass
class TypedElement:

    pass
class UML2WithID_Operation(TypedElement, ParameterableElement, BehavioralFeature, MultiplicityElement):

    def __init__(self, isQuery: bool, Operation: "UML2WithID_Class" = None, operation: set["UML2WithID_Parameter"] = None, ownedOperation: "UML2WithID_Class" = None, ownedOperation73: "UML2WithID_DataType" = None, UML2WithID_Operation: set["UML2WithID_Constraint"] = None, UML2WithID_Operation77: set["UML2WithID_Constraint"] = None, UML2WithID_Operation81: "UML2WithID_Operation" = None, UML2WithID_Operation79: set["UML2WithID_Operation"] = None, UML2WithID_Operation83: "UML2WithID_Constraint" = None, Operation87: "UML2WithID_Parameter" = None, Operation111: "UML2WithID_DataType" = None, UML2WithID_Operation402: "UML2WithID_Artifact" = None, UML2WithID_Operation380: "UML2WithID_Interface" = None, UML2WithID_Operation453: "UML2WithID_CallTrigger" = None, UML2WithID_Operation828: "UML2WithID_CallOperationAction" = None, UML2WithID_Operation882: "UML2WithID_ProtocolTransition" = None):
        self.isQuery = isQuery
        self.Operation = Operation
        self.operation = operation if operation is not None else set()
        self.ownedOperation = ownedOperation
        self.ownedOperation73 = ownedOperation73
        self.UML2WithID_Operation = UML2WithID_Operation if UML2WithID_Operation is not None else set()
        self.UML2WithID_Operation77 = UML2WithID_Operation77 if UML2WithID_Operation77 is not None else set()
        self.UML2WithID_Operation81 = UML2WithID_Operation81
        self.UML2WithID_Operation79 = UML2WithID_Operation79 if UML2WithID_Operation79 is not None else set()
        self.UML2WithID_Operation83 = UML2WithID_Operation83
        self.Operation87 = Operation87
        self.Operation111 = Operation111
        self.UML2WithID_Operation402 = UML2WithID_Operation402
        self.UML2WithID_Operation380 = UML2WithID_Operation380
        self.UML2WithID_Operation453 = UML2WithID_Operation453
        self.UML2WithID_Operation828 = UML2WithID_Operation828
        self.UML2WithID_Operation882 = UML2WithID_Operation882
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def UML2WithID_Operation79(self):
        return self.__UML2WithID_Operation79

    @UML2WithID_Operation79.setter
    def UML2WithID_Operation79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation79", None)
        self.__UML2WithID_Operation79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Operation81"):
                    opp_val = getattr(item, "UML2WithID_Operation81", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Operation81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Operation81"):
                    opp_val = getattr(item, "UML2WithID_Operation81", None)
                    
                    setattr(item, "UML2WithID_Operation81", self)
                    

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__Operation", None)
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
    def Operation111(self):
        return self.__Operation111

    @Operation111.setter
    def Operation111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__Operation111", None)
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
    def ownedOperation73(self):
        return self.__ownedOperation73

    @ownedOperation73.setter
    def ownedOperation73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__ownedOperation73", None)
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
    def UML2WithID_Operation81(self):
        return self.__UML2WithID_Operation81

    @UML2WithID_Operation81.setter
    def UML2WithID_Operation81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation81", None)
        self.__UML2WithID_Operation81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Operation79"):
                opp_val = getattr(old_value, "UML2WithID_Operation79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Operation79"):
                opp_val = getattr(value, "UML2WithID_Operation79", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Operation79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Operation380(self):
        return self.__UML2WithID_Operation380

    @UML2WithID_Operation380.setter
    def UML2WithID_Operation380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation380", None)
        self.__UML2WithID_Operation380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Interface379"):
                opp_val = getattr(old_value, "UML2WithID_Interface379", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Interface379"):
                opp_val = getattr(value, "UML2WithID_Interface379", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Interface379", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Operation453(self):
        return self.__UML2WithID_Operation453

    @UML2WithID_Operation453.setter
    def UML2WithID_Operation453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation453", None)
        self.__UML2WithID_Operation453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_CallTrigger"):
                opp_val = getattr(old_value, "UML2WithID_CallTrigger", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_CallTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_CallTrigger"):
                opp_val = getattr(value, "UML2WithID_CallTrigger", None)
                setattr(value, "UML2WithID_CallTrigger", self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__ownedOperation", None)
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
    def UML2WithID_Operation882(self):
        return self.__UML2WithID_Operation882

    @UML2WithID_Operation882.setter
    def UML2WithID_Operation882(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation882", None)
        self.__UML2WithID_Operation882 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ProtocolTransition881"):
                opp_val = getattr(old_value, "UML2WithID_ProtocolTransition881", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ProtocolTransition881"):
                opp_val = getattr(value, "UML2WithID_ProtocolTransition881", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ProtocolTransition881", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Operation83(self):
        return self.__UML2WithID_Operation83

    @UML2WithID_Operation83.setter
    def UML2WithID_Operation83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation83", None)
        self.__UML2WithID_Operation83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Constraint84"):
                opp_val = getattr(old_value, "UML2WithID_Constraint84", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Constraint84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Constraint84"):
                opp_val = getattr(value, "UML2WithID_Constraint84", None)
                setattr(value, "UML2WithID_Constraint84", self)

    @property
    def Operation87(self):
        return self.__Operation87

    @Operation87.setter
    def Operation87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__Operation87", None)
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
    def UML2WithID_Operation(self):
        return self.__UML2WithID_Operation

    @UML2WithID_Operation.setter
    def UML2WithID_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation", None)
        self.__UML2WithID_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Constraint"):
                    opp_val = getattr(item, "UML2WithID_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Constraint"):
                    opp_val = getattr(item, "UML2WithID_Constraint", None)
                    
                    setattr(item, "UML2WithID_Constraint", self)
                    

    @property
    def UML2WithID_Operation402(self):
        return self.__UML2WithID_Operation402

    @UML2WithID_Operation402.setter
    def UML2WithID_Operation402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation402", None)
        self.__UML2WithID_Operation402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Artifact401"):
                opp_val = getattr(old_value, "UML2WithID_Artifact401", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Artifact401"):
                opp_val = getattr(value, "UML2WithID_Artifact401", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Artifact401", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Operation77(self):
        return self.__UML2WithID_Operation77

    @UML2WithID_Operation77.setter
    def UML2WithID_Operation77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation77", None)
        self.__UML2WithID_Operation77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Constraint78"):
                    opp_val = getattr(item, "UML2WithID_Constraint78", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Constraint78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Constraint78"):
                    opp_val = getattr(item, "UML2WithID_Constraint78", None)
                    
                    setattr(item, "UML2WithID_Constraint78", self)
                    

    @property
    def UML2WithID_Operation828(self):
        return self.__UML2WithID_Operation828

    @UML2WithID_Operation828.setter
    def UML2WithID_Operation828(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__UML2WithID_Operation828", None)
        self.__UML2WithID_Operation828 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_CallOperationAction"):
                opp_val = getattr(old_value, "UML2WithID_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_CallOperationAction"):
                opp_val = getattr(value, "UML2WithID_CallOperationAction", None)
                setattr(value, "UML2WithID_CallOperationAction", self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Operation__operation", None)
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
                    

class UML2WithID_Variable(TypedElement, MultiplicityElement, ConnectableElement):

    pass
class UML2WithID_ObjectNode(TypedElement, ActivityNode):

    def __init__(self, ordering: str, UML2WithID_ObjectNode: "UML2WithID_ValueSpecification" = None, UML2WithID_ObjectNode360: set["UML2WithID_State"] = None, UML2WithID_ObjectNode362: "UML2WithID_Behavior" = None, UML2WithID_ObjectNode648: "UML2WithID_ExceptionHandler" = None):
        self.ordering = ordering
        self.UML2WithID_ObjectNode = UML2WithID_ObjectNode
        self.UML2WithID_ObjectNode360 = UML2WithID_ObjectNode360 if UML2WithID_ObjectNode360 is not None else set()
        self.UML2WithID_ObjectNode362 = UML2WithID_ObjectNode362
        self.UML2WithID_ObjectNode648 = UML2WithID_ObjectNode648
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def UML2WithID_ObjectNode(self):
        return self.__UML2WithID_ObjectNode

    @UML2WithID_ObjectNode.setter
    def UML2WithID_ObjectNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ObjectNode__UML2WithID_ObjectNode", None)
        self.__UML2WithID_ObjectNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ValueSpecification358"):
                opp_val = getattr(old_value, "UML2WithID_ValueSpecification358", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ValueSpecification358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ValueSpecification358"):
                opp_val = getattr(value, "UML2WithID_ValueSpecification358", None)
                setattr(value, "UML2WithID_ValueSpecification358", self)

    @property
    def UML2WithID_ObjectNode360(self):
        return self.__UML2WithID_ObjectNode360

    @UML2WithID_ObjectNode360.setter
    def UML2WithID_ObjectNode360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ObjectNode__UML2WithID_ObjectNode360", None)
        self.__UML2WithID_ObjectNode360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_State"):
                    opp_val = getattr(item, "UML2WithID_State", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_State"):
                    opp_val = getattr(item, "UML2WithID_State", None)
                    
                    setattr(item, "UML2WithID_State", self)
                    

    @property
    def UML2WithID_ObjectNode362(self):
        return self.__UML2WithID_ObjectNode362

    @UML2WithID_ObjectNode362.setter
    def UML2WithID_ObjectNode362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ObjectNode__UML2WithID_ObjectNode362", None)
        self.__UML2WithID_ObjectNode362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior363"):
                opp_val = getattr(old_value, "UML2WithID_Behavior363", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Behavior363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior363"):
                opp_val = getattr(value, "UML2WithID_Behavior363", None)
                setattr(value, "UML2WithID_Behavior363", self)

    @property
    def UML2WithID_ObjectNode648(self):
        return self.__UML2WithID_ObjectNode648

    @UML2WithID_ObjectNode648.setter
    def UML2WithID_ObjectNode648(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ObjectNode__UML2WithID_ObjectNode648", None)
        self.__UML2WithID_ObjectNode648 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ExceptionHandler647"):
                opp_val = getattr(old_value, "UML2WithID_ExceptionHandler647", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ExceptionHandler647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ExceptionHandler647"):
                opp_val = getattr(value, "UML2WithID_ExceptionHandler647", None)
                setattr(value, "UML2WithID_ExceptionHandler647", self)

class UML2WithID_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    def __init__(self, isReadOnly: bool, UML2WithID_StructuralFeature: "UML2WithID_Slot" = None, UML2WithID_StructuralFeature766: "UML2WithID_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.UML2WithID_StructuralFeature = UML2WithID_StructuralFeature
        self.UML2WithID_StructuralFeature766 = UML2WithID_StructuralFeature766
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def UML2WithID_StructuralFeature(self):
        return self.__UML2WithID_StructuralFeature

    @UML2WithID_StructuralFeature.setter
    def UML2WithID_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuralFeature__UML2WithID_StructuralFeature", None)
        self.__UML2WithID_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Slot170"):
                opp_val = getattr(old_value, "UML2WithID_Slot170", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Slot170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Slot170"):
                opp_val = getattr(value, "UML2WithID_Slot170", None)
                setattr(value, "UML2WithID_Slot170", self)

    @property
    def UML2WithID_StructuralFeature766(self):
        return self.__UML2WithID_StructuralFeature766

    @UML2WithID_StructuralFeature766.setter
    def UML2WithID_StructuralFeature766(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_StructuralFeature__UML2WithID_StructuralFeature766", None)
        self.__UML2WithID_StructuralFeature766 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StructuralFeatureAction"):
                opp_val = getattr(old_value, "UML2WithID_StructuralFeatureAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_StructuralFeatureAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StructuralFeatureAction"):
                opp_val = getattr(value, "UML2WithID_StructuralFeatureAction", None)
                setattr(value, "UML2WithID_StructuralFeatureAction", self)

class UML2WithID_Behavior(Class):

    def __init__(self, isReentrant: bool, UML2WithID_Behavior: "UML2WithID_OpaqueExpression" = None, Behavior: "UML2WithID_BehavioralFeature" = None, UML2WithID_Behavior216: "UML2WithID_Behavior" = None, UML2WithID_Behavior214: set["UML2WithID_Behavior"] = None, method: "UML2WithID_BehavioralFeature" = None, UML2WithID_Behavior219: set["UML2WithID_Parameter"] = None, UML2WithID_Behavior222: set["UML2WithID_Parameter"] = None, UML2WithID_Behavior225: set["UML2WithID_Parameter"] = None, UML2WithID_Behavior228: set["UML2WithID_Constraint"] = None, UML2WithID_Behavior231: set["UML2WithID_Constraint"] = None, ownedBehavior: "UML2WithID_BehavioredClassifier" = None, UML2WithID_Behavior234: set["UML2WithID_ParameterSet"] = None, Behavior236: "UML2WithID_BehavioredClassifier" = None, UML2WithID_Behavior238: "UML2WithID_BehavioredClassifier" = None, UML2WithID_Behavior290: "UML2WithID_Connector" = None, UML2WithID_Behavior365: "UML2WithID_ObjectFlow" = None, UML2WithID_Behavior368: "UML2WithID_ObjectFlow" = None, UML2WithID_Behavior370: "UML2WithID_DecisionNode" = None, UML2WithID_Behavior363: "UML2WithID_ObjectNode" = None, UML2WithID_Behavior573: "UML2WithID_ExecutionOccurrence" = None, UML2WithID_Behavior833: "UML2WithID_CallBehaviorAction" = None):
        self.isReentrant = isReentrant
        self.UML2WithID_Behavior = UML2WithID_Behavior
        self.Behavior = Behavior
        self.UML2WithID_Behavior216 = UML2WithID_Behavior216
        self.UML2WithID_Behavior214 = UML2WithID_Behavior214 if UML2WithID_Behavior214 is not None else set()
        self.method = method
        self.UML2WithID_Behavior219 = UML2WithID_Behavior219 if UML2WithID_Behavior219 is not None else set()
        self.UML2WithID_Behavior222 = UML2WithID_Behavior222 if UML2WithID_Behavior222 is not None else set()
        self.UML2WithID_Behavior225 = UML2WithID_Behavior225 if UML2WithID_Behavior225 is not None else set()
        self.UML2WithID_Behavior228 = UML2WithID_Behavior228 if UML2WithID_Behavior228 is not None else set()
        self.UML2WithID_Behavior231 = UML2WithID_Behavior231 if UML2WithID_Behavior231 is not None else set()
        self.ownedBehavior = ownedBehavior
        self.UML2WithID_Behavior234 = UML2WithID_Behavior234 if UML2WithID_Behavior234 is not None else set()
        self.Behavior236 = Behavior236
        self.UML2WithID_Behavior238 = UML2WithID_Behavior238
        self.UML2WithID_Behavior290 = UML2WithID_Behavior290
        self.UML2WithID_Behavior365 = UML2WithID_Behavior365
        self.UML2WithID_Behavior368 = UML2WithID_Behavior368
        self.UML2WithID_Behavior370 = UML2WithID_Behavior370
        self.UML2WithID_Behavior363 = UML2WithID_Behavior363
        self.UML2WithID_Behavior573 = UML2WithID_Behavior573
        self.UML2WithID_Behavior833 = UML2WithID_Behavior833
        
    @property
    def isReentrant(self) -> bool:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: bool):
        self.__isReentrant = isReentrant

    @property
    def Behavior236(self):
        return self.__Behavior236

    @Behavior236.setter
    def Behavior236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__Behavior236", None)
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
    def UML2WithID_Behavior365(self):
        return self.__UML2WithID_Behavior365

    @UML2WithID_Behavior365.setter
    def UML2WithID_Behavior365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior365", None)
        self.__UML2WithID_Behavior365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ObjectFlow"):
                opp_val = getattr(old_value, "UML2WithID_ObjectFlow", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ObjectFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ObjectFlow"):
                opp_val = getattr(value, "UML2WithID_ObjectFlow", None)
                setattr(value, "UML2WithID_ObjectFlow", self)

    @property
    def UML2WithID_Behavior368(self):
        return self.__UML2WithID_Behavior368

    @UML2WithID_Behavior368.setter
    def UML2WithID_Behavior368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior368", None)
        self.__UML2WithID_Behavior368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ObjectFlow367"):
                opp_val = getattr(old_value, "UML2WithID_ObjectFlow367", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ObjectFlow367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ObjectFlow367"):
                opp_val = getattr(value, "UML2WithID_ObjectFlow367", None)
                setattr(value, "UML2WithID_ObjectFlow367", self)

    @property
    def UML2WithID_Behavior231(self):
        return self.__UML2WithID_Behavior231

    @UML2WithID_Behavior231.setter
    def UML2WithID_Behavior231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior231", None)
        self.__UML2WithID_Behavior231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Constraint232"):
                    opp_val = getattr(item, "UML2WithID_Constraint232", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Constraint232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Constraint232"):
                    opp_val = getattr(item, "UML2WithID_Constraint232", None)
                    
                    setattr(item, "UML2WithID_Constraint232", self)
                    

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__method", None)
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
    def UML2WithID_Behavior225(self):
        return self.__UML2WithID_Behavior225

    @UML2WithID_Behavior225.setter
    def UML2WithID_Behavior225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior225", None)
        self.__UML2WithID_Behavior225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Parameter226"):
                    opp_val = getattr(item, "UML2WithID_Parameter226", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Parameter226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Parameter226"):
                    opp_val = getattr(item, "UML2WithID_Parameter226", None)
                    
                    setattr(item, "UML2WithID_Parameter226", self)
                    

    @property
    def UML2WithID_Behavior363(self):
        return self.__UML2WithID_Behavior363

    @UML2WithID_Behavior363.setter
    def UML2WithID_Behavior363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior363", None)
        self.__UML2WithID_Behavior363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ObjectNode362"):
                opp_val = getattr(old_value, "UML2WithID_ObjectNode362", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ObjectNode362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ObjectNode362"):
                opp_val = getattr(value, "UML2WithID_ObjectNode362", None)
                setattr(value, "UML2WithID_ObjectNode362", self)

    @property
    def UML2WithID_Behavior(self):
        return self.__UML2WithID_Behavior

    @UML2WithID_Behavior.setter
    def UML2WithID_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior", None)
        self.__UML2WithID_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_OpaqueExpression22"):
                opp_val = getattr(old_value, "UML2WithID_OpaqueExpression22", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_OpaqueExpression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_OpaqueExpression22"):
                opp_val = getattr(value, "UML2WithID_OpaqueExpression22", None)
                setattr(value, "UML2WithID_OpaqueExpression22", self)

    @property
    def UML2WithID_Behavior833(self):
        return self.__UML2WithID_Behavior833

    @UML2WithID_Behavior833.setter
    def UML2WithID_Behavior833(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior833", None)
        self.__UML2WithID_Behavior833 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_CallBehaviorAction"):
                opp_val = getattr(old_value, "UML2WithID_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_CallBehaviorAction"):
                opp_val = getattr(value, "UML2WithID_CallBehaviorAction", None)
                setattr(value, "UML2WithID_CallBehaviorAction", self)

    @property
    def ownedBehavior(self):
        return self.__ownedBehavior

    @ownedBehavior.setter
    def ownedBehavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__ownedBehavior", None)
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
    def UML2WithID_Behavior370(self):
        return self.__UML2WithID_Behavior370

    @UML2WithID_Behavior370.setter
    def UML2WithID_Behavior370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior370", None)
        self.__UML2WithID_Behavior370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_DecisionNode"):
                opp_val = getattr(old_value, "UML2WithID_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_DecisionNode"):
                opp_val = getattr(value, "UML2WithID_DecisionNode", None)
                setattr(value, "UML2WithID_DecisionNode", self)

    @property
    def UML2WithID_Behavior290(self):
        return self.__UML2WithID_Behavior290

    @UML2WithID_Behavior290.setter
    def UML2WithID_Behavior290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior290", None)
        self.__UML2WithID_Behavior290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Connector289"):
                opp_val = getattr(old_value, "UML2WithID_Connector289", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Connector289"):
                opp_val = getattr(value, "UML2WithID_Connector289", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Connector289", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Behavior(self):
        return self.__Behavior

    @Behavior.setter
    def Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__Behavior", None)
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
    def UML2WithID_Behavior234(self):
        return self.__UML2WithID_Behavior234

    @UML2WithID_Behavior234.setter
    def UML2WithID_Behavior234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior234", None)
        self.__UML2WithID_Behavior234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ParameterSet"):
                    opp_val = getattr(item, "UML2WithID_ParameterSet", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ParameterSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ParameterSet"):
                    opp_val = getattr(item, "UML2WithID_ParameterSet", None)
                    
                    setattr(item, "UML2WithID_ParameterSet", self)
                    

    @property
    def UML2WithID_Behavior219(self):
        return self.__UML2WithID_Behavior219

    @UML2WithID_Behavior219.setter
    def UML2WithID_Behavior219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior219", None)
        self.__UML2WithID_Behavior219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Parameter220"):
                    opp_val = getattr(item, "UML2WithID_Parameter220", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Parameter220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Parameter220"):
                    opp_val = getattr(item, "UML2WithID_Parameter220", None)
                    
                    setattr(item, "UML2WithID_Parameter220", self)
                    

    @property
    def UML2WithID_Behavior573(self):
        return self.__UML2WithID_Behavior573

    @UML2WithID_Behavior573.setter
    def UML2WithID_Behavior573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior573", None)
        self.__UML2WithID_Behavior573 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ExecutionOccurrence"):
                opp_val = getattr(old_value, "UML2WithID_ExecutionOccurrence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ExecutionOccurrence"):
                opp_val = getattr(value, "UML2WithID_ExecutionOccurrence", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_ExecutionOccurrence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Behavior228(self):
        return self.__UML2WithID_Behavior228

    @UML2WithID_Behavior228.setter
    def UML2WithID_Behavior228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior228", None)
        self.__UML2WithID_Behavior228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Constraint229"):
                    opp_val = getattr(item, "UML2WithID_Constraint229", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Constraint229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Constraint229"):
                    opp_val = getattr(item, "UML2WithID_Constraint229", None)
                    
                    setattr(item, "UML2WithID_Constraint229", self)
                    

    @property
    def UML2WithID_Behavior216(self):
        return self.__UML2WithID_Behavior216

    @UML2WithID_Behavior216.setter
    def UML2WithID_Behavior216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior216", None)
        self.__UML2WithID_Behavior216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior214"):
                opp_val = getattr(old_value, "UML2WithID_Behavior214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior214"):
                opp_val = getattr(value, "UML2WithID_Behavior214", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Behavior214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Behavior214(self):
        return self.__UML2WithID_Behavior214

    @UML2WithID_Behavior214.setter
    def UML2WithID_Behavior214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior214", None)
        self.__UML2WithID_Behavior214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Behavior216"):
                    opp_val = getattr(item, "UML2WithID_Behavior216", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Behavior216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Behavior216"):
                    opp_val = getattr(item, "UML2WithID_Behavior216", None)
                    
                    setattr(item, "UML2WithID_Behavior216", self)
                    

    @property
    def UML2WithID_Behavior238(self):
        return self.__UML2WithID_Behavior238

    @UML2WithID_Behavior238.setter
    def UML2WithID_Behavior238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior238", None)
        self.__UML2WithID_Behavior238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_BehavioredClassifier"):
                opp_val = getattr(old_value, "UML2WithID_BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_BehavioredClassifier"):
                opp_val = getattr(value, "UML2WithID_BehavioredClassifier", None)
                setattr(value, "UML2WithID_BehavioredClassifier", self)

    @property
    def UML2WithID_Behavior222(self):
        return self.__UML2WithID_Behavior222

    @UML2WithID_Behavior222.setter
    def UML2WithID_Behavior222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Behavior__UML2WithID_Behavior222", None)
        self.__UML2WithID_Behavior222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Parameter223"):
                    opp_val = getattr(item, "UML2WithID_Parameter223", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Parameter223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Parameter223"):
                    opp_val = getattr(item, "UML2WithID_Parameter223", None)
                    
                    setattr(item, "UML2WithID_Parameter223", self)
                    

class UML2WithID_Parameter(TypedElement, MultiplicityElement, ConnectableElement):

    def __init__(self, default: str, direction: str, isException: bool, isStream: bool, effect: str, UML2WithID_Parameter: "UML2WithID_OpaqueExpression" = None, Parameter: "UML2WithID_Operation" = None, ownedParameter: "UML2WithID_Operation" = None, UML2WithID_Parameter89: "UML2WithID_ValueSpecification" = None, parameter: set["UML2WithID_ParameterSet"] = None, UML2WithID_Parameter149: "UML2WithID_BehavioralFeature" = None, UML2WithID_Parameter152: "UML2WithID_BehavioralFeature" = None, UML2WithID_Parameter155: "UML2WithID_BehavioralFeature" = None, UML2WithID_Parameter220: "UML2WithID_Behavior" = None, UML2WithID_Parameter223: "UML2WithID_Behavior" = None, UML2WithID_Parameter226: "UML2WithID_Behavior" = None, UML2WithID_Parameter373: "UML2WithID_ActivityParameterNode" = None, Parameter852: "UML2WithID_ParameterSet" = None):
        self.default = default
        self.direction = direction
        self.isException = isException
        self.isStream = isStream
        self.effect = effect
        self.UML2WithID_Parameter = UML2WithID_Parameter
        self.Parameter = Parameter
        self.ownedParameter = ownedParameter
        self.UML2WithID_Parameter89 = UML2WithID_Parameter89
        self.parameter = parameter if parameter is not None else set()
        self.UML2WithID_Parameter149 = UML2WithID_Parameter149
        self.UML2WithID_Parameter152 = UML2WithID_Parameter152
        self.UML2WithID_Parameter155 = UML2WithID_Parameter155
        self.UML2WithID_Parameter220 = UML2WithID_Parameter220
        self.UML2WithID_Parameter223 = UML2WithID_Parameter223
        self.UML2WithID_Parameter226 = UML2WithID_Parameter226
        self.UML2WithID_Parameter373 = UML2WithID_Parameter373
        self.Parameter852 = Parameter852
        
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
    def isException(self) -> bool:
        return self.__isException

    @isException.setter
    def isException(self, isException: bool):
        self.__isException = isException

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__parameter", None)
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
    def UML2WithID_Parameter220(self):
        return self.__UML2WithID_Parameter220

    @UML2WithID_Parameter220.setter
    def UML2WithID_Parameter220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter220", None)
        self.__UML2WithID_Parameter220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior219"):
                opp_val = getattr(old_value, "UML2WithID_Behavior219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior219"):
                opp_val = getattr(value, "UML2WithID_Behavior219", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Behavior219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameter852(self):
        return self.__Parameter852

    @Parameter852.setter
    def Parameter852(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__Parameter852", None)
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

    @property
    def UML2WithID_Parameter(self):
        return self.__UML2WithID_Parameter

    @UML2WithID_Parameter.setter
    def UML2WithID_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter", None)
        self.__UML2WithID_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_OpaqueExpression"):
                opp_val = getattr(old_value, "UML2WithID_OpaqueExpression", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_OpaqueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_OpaqueExpression"):
                opp_val = getattr(value, "UML2WithID_OpaqueExpression", None)
                setattr(value, "UML2WithID_OpaqueExpression", self)

    @property
    def UML2WithID_Parameter226(self):
        return self.__UML2WithID_Parameter226

    @UML2WithID_Parameter226.setter
    def UML2WithID_Parameter226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter226", None)
        self.__UML2WithID_Parameter226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior225"):
                opp_val = getattr(old_value, "UML2WithID_Behavior225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior225"):
                opp_val = getattr(value, "UML2WithID_Behavior225", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Behavior225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__Parameter", None)
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
    def UML2WithID_Parameter155(self):
        return self.__UML2WithID_Parameter155

    @UML2WithID_Parameter155.setter
    def UML2WithID_Parameter155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter155", None)
        self.__UML2WithID_Parameter155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_BehavioralFeature154"):
                opp_val = getattr(old_value, "UML2WithID_BehavioralFeature154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_BehavioralFeature154"):
                opp_val = getattr(value, "UML2WithID_BehavioralFeature154", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_BehavioralFeature154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedParameter(self):
        return self.__ownedParameter

    @ownedParameter.setter
    def ownedParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__ownedParameter", None)
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
    def UML2WithID_Parameter149(self):
        return self.__UML2WithID_Parameter149

    @UML2WithID_Parameter149.setter
    def UML2WithID_Parameter149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter149", None)
        self.__UML2WithID_Parameter149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_BehavioralFeature"):
                opp_val = getattr(old_value, "UML2WithID_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_BehavioralFeature"):
                opp_val = getattr(value, "UML2WithID_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Parameter223(self):
        return self.__UML2WithID_Parameter223

    @UML2WithID_Parameter223.setter
    def UML2WithID_Parameter223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter223", None)
        self.__UML2WithID_Parameter223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior222"):
                opp_val = getattr(old_value, "UML2WithID_Behavior222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior222"):
                opp_val = getattr(value, "UML2WithID_Behavior222", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Behavior222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Parameter89(self):
        return self.__UML2WithID_Parameter89

    @UML2WithID_Parameter89.setter
    def UML2WithID_Parameter89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter89", None)
        self.__UML2WithID_Parameter89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ValueSpecification90"):
                opp_val = getattr(old_value, "UML2WithID_ValueSpecification90", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ValueSpecification90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ValueSpecification90"):
                opp_val = getattr(value, "UML2WithID_ValueSpecification90", None)
                setattr(value, "UML2WithID_ValueSpecification90", self)

    @property
    def UML2WithID_Parameter373(self):
        return self.__UML2WithID_Parameter373

    @UML2WithID_Parameter373.setter
    def UML2WithID_Parameter373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter373", None)
        self.__UML2WithID_Parameter373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ActivityParameterNode"):
                opp_val = getattr(old_value, "UML2WithID_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ActivityParameterNode"):
                opp_val = getattr(value, "UML2WithID_ActivityParameterNode", None)
                setattr(value, "UML2WithID_ActivityParameterNode", self)

    @property
    def UML2WithID_Parameter152(self):
        return self.__UML2WithID_Parameter152

    @UML2WithID_Parameter152.setter
    def UML2WithID_Parameter152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Parameter__UML2WithID_Parameter152", None)
        self.__UML2WithID_Parameter152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_BehavioralFeature151"):
                opp_val = getattr(old_value, "UML2WithID_BehavioralFeature151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_BehavioralFeature151"):
                opp_val = getattr(value, "UML2WithID_BehavioralFeature151", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_BehavioralFeature151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ValueSpecification:

    pass
class UML2WithID_LiteralSpecification(ValueSpecification):

    pass
class UML2WithID_InstanceValue(ValueSpecification):

    pass
class UML2WithID_Duration(ValueSpecification):

    def __init__(self, firstTime: bool, UML2WithID_Duration: set["UML2WithID_NamedElement"] = None, UML2WithID_Duration846: "UML2WithID_DurationObservationAction" = None):
        self.firstTime = firstTime
        self.UML2WithID_Duration = UML2WithID_Duration if UML2WithID_Duration is not None else set()
        self.UML2WithID_Duration846 = UML2WithID_Duration846
        
    @property
    def firstTime(self) -> bool:
        return self.__firstTime

    @firstTime.setter
    def firstTime(self, firstTime: bool):
        self.__firstTime = firstTime

    @property
    def UML2WithID_Duration(self):
        return self.__UML2WithID_Duration

    @UML2WithID_Duration.setter
    def UML2WithID_Duration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Duration__UML2WithID_Duration", None)
        self.__UML2WithID_Duration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_NamedElement837"):
                    opp_val = getattr(item, "UML2WithID_NamedElement837", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_NamedElement837", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_NamedElement837"):
                    opp_val = getattr(item, "UML2WithID_NamedElement837", None)
                    
                    setattr(item, "UML2WithID_NamedElement837", self)
                    

    @property
    def UML2WithID_Duration846(self):
        return self.__UML2WithID_Duration846

    @UML2WithID_Duration846.setter
    def UML2WithID_Duration846(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Duration__UML2WithID_Duration846", None)
        self.__UML2WithID_Duration846 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_DurationObservationAction"):
                opp_val = getattr(old_value, "UML2WithID_DurationObservationAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_DurationObservationAction"):
                opp_val = getattr(value, "UML2WithID_DurationObservationAction", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_DurationObservationAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2WithID_Interval(ValueSpecification):

    pass
class UML2WithID_TimeExpression(ValueSpecification):

    def __init__(self, firstTime: bool, UML2WithID_TimeExpression: "UML2WithID_NamedElement" = None, UML2WithID_TimeExpression839: "UML2WithID_TimeObservationAction" = None):
        self.firstTime = firstTime
        self.UML2WithID_TimeExpression = UML2WithID_TimeExpression
        self.UML2WithID_TimeExpression839 = UML2WithID_TimeExpression839
        
    @property
    def firstTime(self) -> bool:
        return self.__firstTime

    @firstTime.setter
    def firstTime(self, firstTime: bool):
        self.__firstTime = firstTime

    @property
    def UML2WithID_TimeExpression(self):
        return self.__UML2WithID_TimeExpression

    @UML2WithID_TimeExpression.setter
    def UML2WithID_TimeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_TimeExpression__UML2WithID_TimeExpression", None)
        self.__UML2WithID_TimeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_NamedElement835"):
                opp_val = getattr(old_value, "UML2WithID_NamedElement835", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_NamedElement835", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_NamedElement835"):
                opp_val = getattr(value, "UML2WithID_NamedElement835", None)
                setattr(value, "UML2WithID_NamedElement835", self)

    @property
    def UML2WithID_TimeExpression839(self):
        return self.__UML2WithID_TimeExpression839

    @UML2WithID_TimeExpression839.setter
    def UML2WithID_TimeExpression839(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_TimeExpression__UML2WithID_TimeExpression839", None)
        self.__UML2WithID_TimeExpression839 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_TimeObservationAction"):
                opp_val = getattr(old_value, "UML2WithID_TimeObservationAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_TimeObservationAction"):
                opp_val = getattr(value, "UML2WithID_TimeObservationAction", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_TimeObservationAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2WithID_OpaqueExpression(ValueSpecification):

    def __init__(self, bodies: str, language: str, UML2WithID_OpaqueExpression: "UML2WithID_Parameter" = None, UML2WithID_OpaqueExpression22: "UML2WithID_Behavior" = None, UML2WithID_OpaqueExpression254: "UML2WithID_Abstraction" = None, UML2WithID_OpaqueExpression539: "UML2WithID_Lifeline" = None):
        self.bodies = bodies
        self.language = language
        self.UML2WithID_OpaqueExpression = UML2WithID_OpaqueExpression
        self.UML2WithID_OpaqueExpression22 = UML2WithID_OpaqueExpression22
        self.UML2WithID_OpaqueExpression254 = UML2WithID_OpaqueExpression254
        self.UML2WithID_OpaqueExpression539 = UML2WithID_OpaqueExpression539
        
    @property
    def bodies(self) -> str:
        return self.__bodies

    @bodies.setter
    def bodies(self, bodies: str):
        self.__bodies = bodies

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def UML2WithID_OpaqueExpression(self):
        return self.__UML2WithID_OpaqueExpression

    @UML2WithID_OpaqueExpression.setter
    def UML2WithID_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_OpaqueExpression__UML2WithID_OpaqueExpression", None)
        self.__UML2WithID_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Parameter"):
                opp_val = getattr(old_value, "UML2WithID_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Parameter"):
                opp_val = getattr(value, "UML2WithID_Parameter", None)
                setattr(value, "UML2WithID_Parameter", self)

    @property
    def UML2WithID_OpaqueExpression22(self):
        return self.__UML2WithID_OpaqueExpression22

    @UML2WithID_OpaqueExpression22.setter
    def UML2WithID_OpaqueExpression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_OpaqueExpression__UML2WithID_OpaqueExpression22", None)
        self.__UML2WithID_OpaqueExpression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Behavior"):
                opp_val = getattr(old_value, "UML2WithID_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Behavior"):
                opp_val = getattr(value, "UML2WithID_Behavior", None)
                setattr(value, "UML2WithID_Behavior", self)

    @property
    def UML2WithID_OpaqueExpression539(self):
        return self.__UML2WithID_OpaqueExpression539

    @UML2WithID_OpaqueExpression539.setter
    def UML2WithID_OpaqueExpression539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_OpaqueExpression__UML2WithID_OpaqueExpression539", None)
        self.__UML2WithID_OpaqueExpression539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Lifeline538"):
                opp_val = getattr(old_value, "UML2WithID_Lifeline538", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Lifeline538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Lifeline538"):
                opp_val = getattr(value, "UML2WithID_Lifeline538", None)
                setattr(value, "UML2WithID_Lifeline538", self)

    @property
    def UML2WithID_OpaqueExpression254(self):
        return self.__UML2WithID_OpaqueExpression254

    @UML2WithID_OpaqueExpression254.setter
    def UML2WithID_OpaqueExpression254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_OpaqueExpression__UML2WithID_OpaqueExpression254", None)
        self.__UML2WithID_OpaqueExpression254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Abstraction"):
                opp_val = getattr(old_value, "UML2WithID_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Abstraction"):
                opp_val = getattr(value, "UML2WithID_Abstraction", None)
                setattr(value, "UML2WithID_Abstraction", self)

class UML2WithID_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, PackageImport: "UML2WithID_Namespace" = None, UML2WithID_PackageImport: "UML2WithID_Package" = None, packageImport: "UML2WithID_Namespace" = None, UML2WithID_PackageImport207: "UML2WithID_Profile" = None):
        self.visibility = visibility
        self.PackageImport = PackageImport
        self.UML2WithID_PackageImport = UML2WithID_PackageImport
        self.packageImport = packageImport
        self.UML2WithID_PackageImport207 = UML2WithID_PackageImport207
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def PackageImport(self):
        return self.__PackageImport

    @PackageImport.setter
    def PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageImport__PackageImport", None)
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
    def UML2WithID_PackageImport(self):
        return self.__UML2WithID_PackageImport

    @UML2WithID_PackageImport.setter
    def UML2WithID_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageImport__UML2WithID_PackageImport", None)
        self.__UML2WithID_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Package187"):
                opp_val = getattr(old_value, "UML2WithID_Package187", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Package187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Package187"):
                opp_val = getattr(value, "UML2WithID_Package187", None)
                setattr(value, "UML2WithID_Package187", self)

    @property
    def UML2WithID_PackageImport207(self):
        return self.__UML2WithID_PackageImport207

    @UML2WithID_PackageImport207.setter
    def UML2WithID_PackageImport207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageImport__UML2WithID_PackageImport207", None)
        self.__UML2WithID_PackageImport207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Profile206"):
                opp_val = getattr(old_value, "UML2WithID_Profile206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Profile206"):
                opp_val = getattr(value, "UML2WithID_Profile206", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Profile206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageImport__packageImport", None)
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

class UML2WithID_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, ElementImport: "UML2WithID_Namespace" = None, UML2WithID_ElementImport: "UML2WithID_PackageableElement" = None, elementImport: "UML2WithID_Namespace" = None, UML2WithID_ElementImport204: "UML2WithID_Profile" = None):
        self.visibility = visibility
        self.alias = alias
        self.ElementImport = ElementImport
        self.UML2WithID_ElementImport = UML2WithID_ElementImport
        self.elementImport = elementImport
        self.UML2WithID_ElementImport204 = UML2WithID_ElementImport204
        
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
    def UML2WithID_ElementImport204(self):
        return self.__UML2WithID_ElementImport204

    @UML2WithID_ElementImport204.setter
    def UML2WithID_ElementImport204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ElementImport__UML2WithID_ElementImport204", None)
        self.__UML2WithID_ElementImport204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Profile203"):
                opp_val = getattr(old_value, "UML2WithID_Profile203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Profile203"):
                opp_val = getattr(value, "UML2WithID_Profile203", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Profile203", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_ElementImport(self):
        return self.__UML2WithID_ElementImport

    @UML2WithID_ElementImport.setter
    def UML2WithID_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ElementImport__UML2WithID_ElementImport", None)
        self.__UML2WithID_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_PackageableElement183"):
                opp_val = getattr(old_value, "UML2WithID_PackageableElement183", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_PackageableElement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_PackageableElement183"):
                opp_val = getattr(value, "UML2WithID_PackageableElement183", None)
                setattr(value, "UML2WithID_PackageableElement183", self)

    @property
    def ElementImport(self):
        return self.__ElementImport

    @ElementImport.setter
    def ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ElementImport__ElementImport", None)
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
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ElementImport__elementImport", None)
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

class UML2WithID_Constraint(PackageableElement):

    pass
class NamedElement:

    pass
class UML2WithID_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool, UML2WithID_RedefinableElement: set["UML2WithID_Classifier"] = None):
        self.isLeaf = isLeaf
        self.UML2WithID_RedefinableElement = UML2WithID_RedefinableElement if UML2WithID_RedefinableElement is not None else set()
        
    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

    @property
    def UML2WithID_RedefinableElement(self):
        return self.__UML2WithID_RedefinableElement

    @UML2WithID_RedefinableElement.setter
    def UML2WithID_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_RedefinableElement__UML2WithID_RedefinableElement", None)
        self.__UML2WithID_RedefinableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Classifier174"):
                    opp_val = getattr(item, "UML2WithID_Classifier174", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Classifier174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Classifier174"):
                    opp_val = getattr(item, "UML2WithID_Classifier174", None)
                    
                    setattr(item, "UML2WithID_Classifier174", self)
                    

class UML2WithID_ParameterSet(NamedElement):

    pass
class UML2WithID_PackageableElement(ParameterableElement, NamedElement):

    def __init__(self, packageableElement_visibility: str, UML2WithID_PackageableElement: "UML2WithID_Namespace" = None, UML2WithID_PackageableElement100: "UML2WithID_Package" = None, UML2WithID_PackageableElement183: "UML2WithID_ElementImport" = None, UML2WithID_PackageableElement408: "UML2WithID_Manifestation" = None, UML2WithID_PackageableElement864: "UML2WithID_Component" = None, UML2WithID_PackageableElement871: "UML2WithID_DeploymentTarget" = None):
        self.packageableElement_visibility = packageableElement_visibility
        self.UML2WithID_PackageableElement = UML2WithID_PackageableElement
        self.UML2WithID_PackageableElement100 = UML2WithID_PackageableElement100
        self.UML2WithID_PackageableElement183 = UML2WithID_PackageableElement183
        self.UML2WithID_PackageableElement408 = UML2WithID_PackageableElement408
        self.UML2WithID_PackageableElement864 = UML2WithID_PackageableElement864
        self.UML2WithID_PackageableElement871 = UML2WithID_PackageableElement871
        
    @property
    def packageableElement_visibility(self) -> str:
        return self.__packageableElement_visibility

    @packageableElement_visibility.setter
    def packageableElement_visibility(self, packageableElement_visibility: str):
        self.__packageableElement_visibility = packageableElement_visibility

    @property
    def UML2WithID_PackageableElement(self):
        return self.__UML2WithID_PackageableElement

    @UML2WithID_PackageableElement.setter
    def UML2WithID_PackageableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageableElement__UML2WithID_PackageableElement", None)
        self.__UML2WithID_PackageableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Namespace16"):
                opp_val = getattr(old_value, "UML2WithID_Namespace16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Namespace16"):
                opp_val = getattr(value, "UML2WithID_Namespace16", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Namespace16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_PackageableElement100(self):
        return self.__UML2WithID_PackageableElement100

    @UML2WithID_PackageableElement100.setter
    def UML2WithID_PackageableElement100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageableElement__UML2WithID_PackageableElement100", None)
        self.__UML2WithID_PackageableElement100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Package"):
                opp_val = getattr(old_value, "UML2WithID_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Package"):
                opp_val = getattr(value, "UML2WithID_Package", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_PackageableElement864(self):
        return self.__UML2WithID_PackageableElement864

    @UML2WithID_PackageableElement864.setter
    def UML2WithID_PackageableElement864(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageableElement__UML2WithID_PackageableElement864", None)
        self.__UML2WithID_PackageableElement864 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Component863"):
                opp_val = getattr(old_value, "UML2WithID_Component863", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Component863"):
                opp_val = getattr(value, "UML2WithID_Component863", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Component863", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_PackageableElement408(self):
        return self.__UML2WithID_PackageableElement408

    @UML2WithID_PackageableElement408.setter
    def UML2WithID_PackageableElement408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageableElement__UML2WithID_PackageableElement408", None)
        self.__UML2WithID_PackageableElement408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Manifestation407"):
                opp_val = getattr(old_value, "UML2WithID_Manifestation407", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Manifestation407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Manifestation407"):
                opp_val = getattr(value, "UML2WithID_Manifestation407", None)
                setattr(value, "UML2WithID_Manifestation407", self)

    @property
    def UML2WithID_PackageableElement871(self):
        return self.__UML2WithID_PackageableElement871

    @UML2WithID_PackageableElement871.setter
    def UML2WithID_PackageableElement871(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageableElement__UML2WithID_PackageableElement871", None)
        self.__UML2WithID_PackageableElement871 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_DeploymentTarget"):
                opp_val = getattr(old_value, "UML2WithID_DeploymentTarget", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_DeploymentTarget"):
                opp_val = getattr(value, "UML2WithID_DeploymentTarget", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_DeploymentTarget", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_PackageableElement183(self):
        return self.__UML2WithID_PackageableElement183

    @UML2WithID_PackageableElement183.setter
    def UML2WithID_PackageableElement183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_PackageableElement__UML2WithID_PackageableElement183", None)
        self.__UML2WithID_PackageableElement183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ElementImport"):
                opp_val = getattr(old_value, "UML2WithID_ElementImport", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ElementImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ElementImport"):
                opp_val = getattr(value, "UML2WithID_ElementImport", None)
                setattr(value, "UML2WithID_ElementImport", self)

class UML2WithID_GeneralOrdering(NamedElement):

    pass
class UML2WithID_Include(NamedElement, DirectedRelationship):

    pass
class UML2WithID_MessageEnd(NamedElement):

    pass
class UML2WithID_InteractionFragment(NamedElement):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement):

    pass
class UML2WithID_TypedElement(NamedElement):

    pass
class UML2WithID_Extend(NamedElement, DirectedRelationship):

    pass
class UML2WithID_ConnectableElement(ParameterableElement, NamedElement):

    pass
class UML2WithID_Message(NamedElement):

    def __init__(self, messageKind: str, messageSort: str, Message: "UML2WithID_Interaction" = None, UML2WithID_Message553: set["UML2WithID_ValueSpecification"] = None, Message559: "UML2WithID_MessageEnd" = None, receiveMessage: "UML2WithID_MessageEnd" = None, sendMessage: "UML2WithID_MessageEnd" = None, UML2WithID_Message: "UML2WithID_Connector" = None, message: "UML2WithID_Interaction" = None, UML2WithID_Message550: "UML2WithID_NamedElement" = None, Message561: "UML2WithID_MessageEnd" = None):
        self.messageKind = messageKind
        self.messageSort = messageSort
        self.Message = Message
        self.UML2WithID_Message553 = UML2WithID_Message553 if UML2WithID_Message553 is not None else set()
        self.Message559 = Message559
        self.receiveMessage = receiveMessage
        self.sendMessage = sendMessage
        self.UML2WithID_Message = UML2WithID_Message
        self.message = message
        self.UML2WithID_Message550 = UML2WithID_Message550
        self.Message561 = Message561
        
    @property
    def messageKind(self) -> str:
        return self.__messageKind

    @messageKind.setter
    def messageKind(self, messageKind: str):
        self.__messageKind = messageKind

    @property
    def messageSort(self) -> str:
        return self.__messageSort

    @messageSort.setter
    def messageSort(self, messageSort: str):
        self.__messageSort = messageSort

    @property
    def sendMessage(self):
        return self.__sendMessage

    @sendMessage.setter
    def sendMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__sendMessage", None)
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
    def Message559(self):
        return self.__Message559

    @Message559.setter
    def Message559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__Message559", None)
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
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__Message", None)
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
    def receiveMessage(self):
        return self.__receiveMessage

    @receiveMessage.setter
    def receiveMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__receiveMessage", None)
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
    def UML2WithID_Message553(self):
        return self.__UML2WithID_Message553

    @UML2WithID_Message553.setter
    def UML2WithID_Message553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__UML2WithID_Message553", None)
        self.__UML2WithID_Message553 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_ValueSpecification554"):
                    opp_val = getattr(item, "UML2WithID_ValueSpecification554", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_ValueSpecification554", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_ValueSpecification554"):
                    opp_val = getattr(item, "UML2WithID_ValueSpecification554", None)
                    
                    setattr(item, "UML2WithID_ValueSpecification554", self)
                    

    @property
    def UML2WithID_Message550(self):
        return self.__UML2WithID_Message550

    @UML2WithID_Message550.setter
    def UML2WithID_Message550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__UML2WithID_Message550", None)
        self.__UML2WithID_Message550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_NamedElement551"):
                opp_val = getattr(old_value, "UML2WithID_NamedElement551", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_NamedElement551", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_NamedElement551"):
                opp_val = getattr(value, "UML2WithID_NamedElement551", None)
                setattr(value, "UML2WithID_NamedElement551", self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__message", None)
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

    @property
    def Message561(self):
        return self.__Message561

    @Message561.setter
    def Message561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__Message561", None)
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
    def UML2WithID_Message(self):
        return self.__UML2WithID_Message

    @UML2WithID_Message.setter
    def UML2WithID_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Message__UML2WithID_Message", None)
        self.__UML2WithID_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Connector546"):
                opp_val = getattr(old_value, "UML2WithID_Connector546", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Connector546", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Connector546"):
                opp_val = getattr(value, "UML2WithID_Connector546", None)
                setattr(value, "UML2WithID_Connector546", self)

class UML2WithID_Trigger(NamedElement):

    pass
class UML2WithID_Vertex(NamedElement):

    pass
class UML2WithID_DeploymentTarget(NamedElement):

    pass
class UML2WithID_ActivityPartition(ActivityGroup, NamedElement):

    def __init__(self, isDimension: bool, isExternal: bool, ActivityPartition340: "UML2WithID_ActivityNode" = None, ActivityPartition: "UML2WithID_ActivityEdge" = None, ActivityPartition632: "UML2WithID_ActivityPartition" = None, superPartition: set["UML2WithID_ActivityPartition"] = None, ActivityPartition635: "UML2WithID_ActivityPartition" = None, subgroup: "UML2WithID_ActivityPartition" = None, UML2WithID_ActivityPartition: "UML2WithID_Element" = None, inPartition: set["UML2WithID_ActivityEdge"] = None, inPartition628: set["UML2WithID_ActivityNode"] = None):
        self.isDimension = isDimension
        self.isExternal = isExternal
        self.ActivityPartition340 = ActivityPartition340
        self.ActivityPartition = ActivityPartition
        self.ActivityPartition632 = ActivityPartition632
        self.superPartition = superPartition if superPartition is not None else set()
        self.ActivityPartition635 = ActivityPartition635
        self.subgroup = subgroup
        self.UML2WithID_ActivityPartition = UML2WithID_ActivityPartition
        self.inPartition = inPartition if inPartition is not None else set()
        self.inPartition628 = inPartition628 if inPartition628 is not None else set()
        
    @property
    def isExternal(self) -> bool:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: bool):
        self.__isExternal = isExternal

    @property
    def isDimension(self) -> bool:
        return self.__isDimension

    @isDimension.setter
    def isDimension(self, isDimension: bool):
        self.__isDimension = isDimension

    @property
    def ActivityPartition340(self):
        return self.__ActivityPartition340

    @ActivityPartition340.setter
    def ActivityPartition340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__ActivityPartition340", None)
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
    def ActivityPartition635(self):
        return self.__ActivityPartition635

    @ActivityPartition635.setter
    def ActivityPartition635(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__ActivityPartition635", None)
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
    def inPartition(self):
        return self.__inPartition

    @inPartition.setter
    def inPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__inPartition", None)
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
    def ActivityPartition632(self):
        return self.__ActivityPartition632

    @ActivityPartition632.setter
    def ActivityPartition632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__ActivityPartition632", None)
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
    def inPartition628(self):
        return self.__inPartition628

    @inPartition628.setter
    def inPartition628(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__inPartition628", None)
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
    def superPartition(self):
        return self.__superPartition

    @superPartition.setter
    def superPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__superPartition", None)
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
                    

    @property
    def UML2WithID_ActivityPartition(self):
        return self.__UML2WithID_ActivityPartition

    @UML2WithID_ActivityPartition.setter
    def UML2WithID_ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__UML2WithID_ActivityPartition", None)
        self.__UML2WithID_ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Element637"):
                opp_val = getattr(old_value, "UML2WithID_Element637", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Element637", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Element637"):
                opp_val = getattr(value, "UML2WithID_Element637", None)
                setattr(value, "UML2WithID_Element637", self)

    @property
    def ActivityPartition(self):
        return self.__ActivityPartition

    @ActivityPartition.setter
    def ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__ActivityPartition", None)
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
    def subgroup(self):
        return self.__subgroup

    @subgroup.setter
    def subgroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_ActivityPartition__subgroup", None)
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

class UML2WithID_Lifeline(NamedElement):

    pass
class UML2WithID_DeployedArtifact(NamedElement):

    pass
class UML2WithID_Namespace(NamedElement):

    pass
class UML2WithID_Dependency(PackageableElement, DirectedRelationship):

    pass
class TemplateableElement:

    pass
class UML2WithID_StringExpression(TemplateableElement):

    pass
class UML2WithID_NamedElement(TemplateableElement):

    def __init__(self, name: str, qualifiedName: str, visibility: str, client: set["UML2WithID_Dependency"] = None, UML2WithID_NamedElement: "UML2WithID_StringExpression" = None, UML2WithID_NamedElement13: "UML2WithID_Namespace" = None, UML2WithID_NamedElement116: "UML2WithID_Classifier" = None, NamedElement: "UML2WithID_Dependency" = None, UML2WithID_NamedElement252: "UML2WithID_Dependency" = None, UML2WithID_NamedElement551: "UML2WithID_Message" = None, UML2WithID_NamedElement835: "UML2WithID_TimeExpression" = None, UML2WithID_NamedElement837: "UML2WithID_Duration" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.visibility = visibility
        self.client = client if client is not None else set()
        self.UML2WithID_NamedElement = UML2WithID_NamedElement
        self.UML2WithID_NamedElement13 = UML2WithID_NamedElement13
        self.UML2WithID_NamedElement116 = UML2WithID_NamedElement116
        self.NamedElement = NamedElement
        self.UML2WithID_NamedElement252 = UML2WithID_NamedElement252
        self.UML2WithID_NamedElement551 = UML2WithID_NamedElement551
        self.UML2WithID_NamedElement835 = UML2WithID_NamedElement835
        self.UML2WithID_NamedElement837 = UML2WithID_NamedElement837
        
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
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def UML2WithID_NamedElement116(self):
        return self.__UML2WithID_NamedElement116

    @UML2WithID_NamedElement116.setter
    def UML2WithID_NamedElement116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement116", None)
        self.__UML2WithID_NamedElement116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Classifier115"):
                opp_val = getattr(old_value, "UML2WithID_Classifier115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Classifier115"):
                opp_val = getattr(value, "UML2WithID_Classifier115", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Classifier115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__client", None)
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
    def UML2WithID_NamedElement835(self):
        return self.__UML2WithID_NamedElement835

    @UML2WithID_NamedElement835.setter
    def UML2WithID_NamedElement835(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement835", None)
        self.__UML2WithID_NamedElement835 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_TimeExpression"):
                opp_val = getattr(old_value, "UML2WithID_TimeExpression", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_TimeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_TimeExpression"):
                opp_val = getattr(value, "UML2WithID_TimeExpression", None)
                setattr(value, "UML2WithID_TimeExpression", self)

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__NamedElement", None)
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
    def UML2WithID_NamedElement13(self):
        return self.__UML2WithID_NamedElement13

    @UML2WithID_NamedElement13.setter
    def UML2WithID_NamedElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement13", None)
        self.__UML2WithID_NamedElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Namespace"):
                opp_val = getattr(old_value, "UML2WithID_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Namespace"):
                opp_val = getattr(value, "UML2WithID_Namespace", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_NamedElement837(self):
        return self.__UML2WithID_NamedElement837

    @UML2WithID_NamedElement837.setter
    def UML2WithID_NamedElement837(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement837", None)
        self.__UML2WithID_NamedElement837 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Duration"):
                opp_val = getattr(old_value, "UML2WithID_Duration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Duration"):
                opp_val = getattr(value, "UML2WithID_Duration", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Duration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_NamedElement551(self):
        return self.__UML2WithID_NamedElement551

    @UML2WithID_NamedElement551.setter
    def UML2WithID_NamedElement551(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement551", None)
        self.__UML2WithID_NamedElement551 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Message550"):
                opp_val = getattr(old_value, "UML2WithID_Message550", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Message550", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Message550"):
                opp_val = getattr(value, "UML2WithID_Message550", None)
                setattr(value, "UML2WithID_Message550", self)

    @property
    def UML2WithID_NamedElement252(self):
        return self.__UML2WithID_NamedElement252

    @UML2WithID_NamedElement252.setter
    def UML2WithID_NamedElement252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement252", None)
        self.__UML2WithID_NamedElement252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Dependency"):
                opp_val = getattr(old_value, "UML2WithID_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Dependency"):
                opp_val = getattr(value, "UML2WithID_Dependency", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_NamedElement(self):
        return self.__UML2WithID_NamedElement

    @UML2WithID_NamedElement.setter
    def UML2WithID_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement", None)
        self.__UML2WithID_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StringExpression"):
                opp_val = getattr(old_value, "UML2WithID_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StringExpression"):
                opp_val = getattr(value, "UML2WithID_StringExpression", None)
                setattr(value, "UML2WithID_StringExpression", self)

class UML2WithID_ValueSpecification(TypedElement, ParameterableElement):

    pass
class Element:

    pass
class UML2WithID_ActivityGroup(Element):

    pass
class UML2WithID_LinkEndData(Element):

    pass
class UML2WithID_TemplateParameterSubstitution(Element):

    pass
class UML2WithID_TemplateSignature(Element):

    pass
class UML2WithID_QualifierValue(Element):

    pass
class UML2WithID_ParameterableElement(Element):

    pass
class UML2WithID_Slot(Element):

    pass
class UML2WithID_ExceptionHandler(Element):

    pass
class UML2WithID_Clause(Element):

    pass
class UML2WithID_TemplateableElement(Element):

    pass
class UML2WithID_Relationship(Element):

    pass
class UML2WithID_TemplateParameter(Element):

    pass
class UML2WithID_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, lower: int, upper: str, UML2WithID_MultiplicityElement: "UML2WithID_ValueSpecification" = None, UML2WithID_MultiplicityElement8: "UML2WithID_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        self.UML2WithID_MultiplicityElement = UML2WithID_MultiplicityElement
        self.UML2WithID_MultiplicityElement8 = UML2WithID_MultiplicityElement8
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def UML2WithID_MultiplicityElement8(self):
        return self.__UML2WithID_MultiplicityElement8

    @UML2WithID_MultiplicityElement8.setter
    def UML2WithID_MultiplicityElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_MultiplicityElement__UML2WithID_MultiplicityElement8", None)
        self.__UML2WithID_MultiplicityElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ValueSpecification9"):
                opp_val = getattr(old_value, "UML2WithID_ValueSpecification9", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ValueSpecification9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ValueSpecification9"):
                opp_val = getattr(value, "UML2WithID_ValueSpecification9", None)
                setattr(value, "UML2WithID_ValueSpecification9", self)

    @property
    def UML2WithID_MultiplicityElement(self):
        return self.__UML2WithID_MultiplicityElement

    @UML2WithID_MultiplicityElement.setter
    def UML2WithID_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_MultiplicityElement__UML2WithID_MultiplicityElement", None)
        self.__UML2WithID_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ValueSpecification"):
                opp_val = getattr(old_value, "UML2WithID_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ValueSpecification"):
                opp_val = getattr(value, "UML2WithID_ValueSpecification", None)
                setattr(value, "UML2WithID_ValueSpecification", self)

class UML2WithID_Comment(TemplateableElement):

    def __init__(self, body: str, UML2WithID_Comment: "UML2WithID_Element" = None, UML2WithID_Comment26: set["UML2WithID_Element"] = None, UML2WithID_Comment29: "UML2WithID_StringExpression" = None):
        self.body = body
        self.UML2WithID_Comment = UML2WithID_Comment
        self.UML2WithID_Comment26 = UML2WithID_Comment26 if UML2WithID_Comment26 is not None else set()
        self.UML2WithID_Comment29 = UML2WithID_Comment29
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def UML2WithID_Comment(self):
        return self.__UML2WithID_Comment

    @UML2WithID_Comment.setter
    def UML2WithID_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Comment__UML2WithID_Comment", None)
        self.__UML2WithID_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Element"):
                opp_val = getattr(old_value, "UML2WithID_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Element"):
                opp_val = getattr(value, "UML2WithID_Element", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Comment26(self):
        return self.__UML2WithID_Comment26

    @UML2WithID_Comment26.setter
    def UML2WithID_Comment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Comment__UML2WithID_Comment26", None)
        self.__UML2WithID_Comment26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Element27"):
                    opp_val = getattr(item, "UML2WithID_Element27", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Element27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Element27"):
                    opp_val = getattr(item, "UML2WithID_Element27", None)
                    
                    setattr(item, "UML2WithID_Element27", self)
                    

    @property
    def UML2WithID_Comment29(self):
        return self.__UML2WithID_Comment29

    @UML2WithID_Comment29.setter
    def UML2WithID_Comment29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Comment__UML2WithID_Comment29", None)
        self.__UML2WithID_Comment29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_StringExpression30"):
                opp_val = getattr(old_value, "UML2WithID_StringExpression30", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_StringExpression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_StringExpression30"):
                opp_val = getattr(value, "UML2WithID_StringExpression30", None)
                setattr(value, "UML2WithID_StringExpression30", self)

class UML2WithID_Element(ABC):

    def __init__(self, ID: str, Element: "UML2WithID_Element" = None, owner: set["UML2WithID_Element"] = None, Element4: "UML2WithID_Element" = None, ownedElement: "UML2WithID_Element" = None, UML2WithID_Element: set["UML2WithID_Comment"] = None, UML2WithID_Element27: "UML2WithID_Comment" = None, UML2WithID_Element32: "UML2WithID_DirectedRelationship" = None, UML2WithID_Element35: "UML2WithID_DirectedRelationship" = None, UML2WithID_Element37: "UML2WithID_Relationship" = None, UML2WithID_Element147: "UML2WithID_Constraint" = None, UML2WithID_Element637: "UML2WithID_ActivityPartition" = None):
        self.ID = ID
        self.Element = Element
        self.owner = owner if owner is not None else set()
        self.Element4 = Element4
        self.ownedElement = ownedElement
        self.UML2WithID_Element = UML2WithID_Element if UML2WithID_Element is not None else set()
        self.UML2WithID_Element27 = UML2WithID_Element27
        self.UML2WithID_Element32 = UML2WithID_Element32
        self.UML2WithID_Element35 = UML2WithID_Element35
        self.UML2WithID_Element37 = UML2WithID_Element37
        self.UML2WithID_Element147 = UML2WithID_Element147
        self.UML2WithID_Element637 = UML2WithID_Element637
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def UML2WithID_Element32(self):
        return self.__UML2WithID_Element32

    @UML2WithID_Element32.setter
    def UML2WithID_Element32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element32", None)
        self.__UML2WithID_Element32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_DirectedRelationship"):
                opp_val = getattr(old_value, "UML2WithID_DirectedRelationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_DirectedRelationship"):
                opp_val = getattr(value, "UML2WithID_DirectedRelationship", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_DirectedRelationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Element(self):
        return self.__UML2WithID_Element

    @UML2WithID_Element.setter
    def UML2WithID_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element", None)
        self.__UML2WithID_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2WithID_Comment"):
                    opp_val = getattr(item, "UML2WithID_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2WithID_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2WithID_Comment"):
                    opp_val = getattr(item, "UML2WithID_Comment", None)
                    
                    setattr(item, "UML2WithID_Comment", self)
                    

    @property
    def Element4(self):
        return self.__Element4

    @Element4.setter
    def Element4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__Element4", None)
        self.__Element4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElement"):
                opp_val = getattr(old_value, "ownedElement", None)
                if opp_val == self:
                    setattr(old_value, "ownedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElement"):
                opp_val = getattr(value, "ownedElement", None)
                setattr(value, "ownedElement", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element4"):
                opp_val = getattr(old_value, "Element4", None)
                if opp_val == self:
                    setattr(old_value, "Element4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element4"):
                opp_val = getattr(value, "Element4", None)
                setattr(value, "Element4", self)

    @property
    def UML2WithID_Element637(self):
        return self.__UML2WithID_Element637

    @UML2WithID_Element637.setter
    def UML2WithID_Element637(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element637", None)
        self.__UML2WithID_Element637 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_ActivityPartition"):
                opp_val = getattr(old_value, "UML2WithID_ActivityPartition", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_ActivityPartition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_ActivityPartition"):
                opp_val = getattr(value, "UML2WithID_ActivityPartition", None)
                setattr(value, "UML2WithID_ActivityPartition", self)

    @property
    def UML2WithID_Element27(self):
        return self.__UML2WithID_Element27

    @UML2WithID_Element27.setter
    def UML2WithID_Element27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element27", None)
        self.__UML2WithID_Element27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Comment26"):
                opp_val = getattr(old_value, "UML2WithID_Comment26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Comment26"):
                opp_val = getattr(value, "UML2WithID_Comment26", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Comment26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Element35(self):
        return self.__UML2WithID_Element35

    @UML2WithID_Element35.setter
    def UML2WithID_Element35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element35", None)
        self.__UML2WithID_Element35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_DirectedRelationship34"):
                opp_val = getattr(old_value, "UML2WithID_DirectedRelationship34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_DirectedRelationship34"):
                opp_val = getattr(value, "UML2WithID_DirectedRelationship34", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_DirectedRelationship34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__Element", None)
        self.__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Element147(self):
        return self.__UML2WithID_Element147

    @UML2WithID_Element147.setter
    def UML2WithID_Element147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element147", None)
        self.__UML2WithID_Element147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Constraint146"):
                opp_val = getattr(old_value, "UML2WithID_Constraint146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Constraint146"):
                opp_val = getattr(value, "UML2WithID_Constraint146", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Constraint146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2WithID_Element37(self):
        return self.__UML2WithID_Element37

    @UML2WithID_Element37.setter
    def UML2WithID_Element37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element37", None)
        self.__UML2WithID_Element37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Relationship"):
                opp_val = getattr(old_value, "UML2WithID_Relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Relationship"):
                opp_val = getattr(value, "UML2WithID_Relationship", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

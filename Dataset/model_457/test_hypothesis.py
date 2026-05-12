import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ActivityNode,
    Transition,
    CompleteDSLPckg_ProtocolTransition,
    StateMachine,
    CompleteDSLPckg_ProtocolStateMachine,
    State,
    CompleteDSLPckg_FinalState,
    Vertex,
    CompleteDSLPckg_ConnectionPointReference,
    WriteVariableAction,
    CompleteDSLPckg_RemoveVariableValueAction,
    CompleteDSLPckg_AddVariableValueAction,
    VariableAction,
    CompleteDSLPckg_ClearVariableAction,
    CompleteDSLPckg_WriteVariableAction,
    CompleteDSLPckg_ReadVariableAction,
    CompleteDSLPckg_Pseudostate,
    CreateLinkAction,
    CompleteDSLPckg_CreateLinkObjectAction,
    CompleteDSLPckg_ReadlsClassifiedObjectAction,
    AcceptEventAction,
    CompleteDSLPckg_AcceptCallAction,
    LinkAction,
    CompleteDSLPckg_WriteLinkAction,
    CompleteDSLPckg_ReadLinkAction,
    WriteStructuralFeatureAction,
    CompleteDSLPckg_RemoveStructuralFeatureValueAction,
    CompleteDSLPckg_AddStructuralFeatureValueAction,
    LinkEndData,
    CompleteDSLPckg_LinkEndDestructionData,
    CompleteDSLPckg_LinkEndCreationData,
    InteractionUse,
    MessageEnd,
    CombinedFragment,
    CompleteDSLPckg_ConsiderIgnoreFragment,
    CompleteDSLPckg_CombinedFragment,
    CompleteDSLPckg_PartDecomposition,
    ExecutionSpecification,
    CompleteDSLPckg_ActionExecutionSpecification,
    CompleteDSLPckg_BehaviorExecutionSpecification,
    MessageOccurrenceSpecification,
    CompleteDSLPckg_DestructionOccurrenceSpecification,
    OccurenceSpecification,
    CompleteDSLPckg_MessageOccurrenceSpecification,
    CompleteDSLPckg_ExecutionOccurrenceSpecification,
    InteractionFragment,
    CompleteDSLPckg_Continuation,
    CompleteDSLPckg_InteractionUse,
    CompleteDSLPckg_OccurenceSpecification,
    CompleteDSLPckg_StateInvariant,
    CompleteDSLPckg_ExecutionSpecification,
    CompleteDSLPckg_Gate,
    ExecutableNode,
    CentralBufferNode,
    CompleteDSLPckg_DataStoreNode,
    StructuredActivityNode,
    CompleteDSLPckg_ConditionalNode,
    CompleteDSLPckg_ExpansionRegion,
    CompleteDSLPckg_SequenceNode,
    CompleteDSLPckg_LoopNode,
    CompleteDSLPckg_ExecutableNode,
    ActivityEdge,
    CompleteDSLPckg_ObjectFlow,
    CompleteDSLPckg_ControlFlow,
    ActivityGroup,
    CompleteDSLPckg_InterruptibleActivityRegion,
    CompleteDSLPckg_ActivityPartition,
    FinalNode,
    CompleteDSLPckg_FlowFinalNode,
    ControlNode,
    CompleteDSLPckg_JoinNode,
    CompleteDSLPckg_DecisionNode,
    CompleteDSLPckg_FinalNode,
    CompleteDSLPckg_ForkNode,
    CompleteDSLPckg_InitialNode,
    CompleteDSLPckg_MergeNode,
    CompleteDSLPckg_ActivityFinalNode,
    CompleteDSLPckg_ControlNode,
    ObjectNode,
    CompleteDSLPckg_ExpansionNode,
    CompleteDSLPckg_CentralBufferNode,
    CompleteDSLPckg_ActivityParameterNode,
    WriteLinkAction,
    CompleteDSLPckg_DestroyLinkAction,
    CompleteDSLPckg_CreateLinkAction,
    StructuralFeatureAction,
    CompleteDSLPckg_ClearStructuralFeatureAction,
    CompleteDSLPckg_WriteStructuralFeatureAction,
    CompleteDSLPckg_ReadStructuralFeatureAction,
    CompleteDSLPckg_CallOperationAction,
    CallAction,
    CompleteDSLPckg_StartObjectBehaviorAction,
    CompleteDSLPckg_CallBehaviorAction,
    InvocationAction,
    CompleteDSLPckg_SendSignalAction,
    CompleteDSLPckg_BroadcastSignalAction,
    CompleteDSLPckg_CallAction,
    InputPin,
    CompleteDSLPckg_ActionInputPin,
    CompleteDSLPckg_ValuePin,
    Pin,
    Action,
    CompleteDSLPckg_DestroyObjectAction,
    CompleteDSLPckg_ReclassifyObjectAction,
    CompleteDSLPckg_TestIdentityAction,
    CompleteDSLPckg_ReadSelfAction,
    CompleteDSLPckg_ValueSpecificationAction,
    CompleteDSLPckg_VariableAction,
    CompleteDSLPckg_ReduceAction,
    CompleteDSLPckg_StructuralFeatureAction,
    CompleteDSLPckg_ReadLinkObjectEndAction,
    CompleteDSLPckg_RaiseExceptionAction,
    CompleteDSLPckg_ReplyAction,
    CompleteDSLPckg_ReadLinkObjectEndQualifierAction,
    CompleteDSLPckg_CreateObjectAction,
    CompleteDSLPckg_StartClassifierBehaviorAction,
    CompleteDSLPckg_LinkAction,
    CompleteDSLPckg_UnmarshallAction,
    CompleteDSLPckg_AcceptEventAction,
    CompleteDSLPckg_ReadExtendAction,
    CompleteDSLPckg_OpaqueAction,
    CompleteDSLPckg_SendObjectAction,
    CompleteDSLPckg_InputPin,
    Artifact,
    CompleteDSLPckg_DeploymentSpecification,
    Node,
    CompleteDSLPckg_ExecutionEnvironment,
    CompleteDSLPckg_Device,
    CompleteDSLPckg_OutputPin,
    DeployedArtifact,
    CompleteDSLPckg_InvocationAction,
    CompleteDSLPckg_ConnectorEnd,
    Property,
    CompleteDSLPckg_Port,
    IntervalConstraint,
    CompleteDSLPckg_DurationConstraint,
    CompleteDSLPckg_TimeConstraint,
    Constraint,
    CompleteDSLPckg_InteractionConstraint,
    CompleteDSLPckg_IntervalConstraint,
    Interval,
    CompleteDSLPckg_DurationInterval,
    CompleteDSLPckg_TimeInterval,
    Observation,
    CompleteDSLPckg_DurationObservation,
    CompleteDSLPckg_TimeObservation,
    CompleteDSLPckg_TimeEvent,
    MessageEvent,
    CompleteDSLPckg_SignalEvent,
    CompleteDSLPckg_CallEvent,
    CompleteDSLPckg_AnyReceiveEvent,
    Event,
    CompleteDSLPckg_ChangeEvent,
    CompleteDSLPckg_MessageEvent,
    OpaqueBehavior,
    CompleteDSLPckg_FunctionBehavior,
    Behavior,
    CompleteDSLPckg_Interaction,
    CompleteDSLPckg_StateMachine,
    CompleteDSLPckg_Activity,
    CompleteDSLPckg_OpaqueBehavior,
    Association,
    CompleteDSLPckg_CommunicationPath,
    Class,
    CompleteDSLPckg_AssociationClass,
    Realization,
    CompleteDSLPckg_InterfaceRealization,
    CompleteDSLPckg_ComponentRealization,
    Abstraction,
    CompleteDSLPckg_Manifestation,
    CompleteDSLPckg_Realization,
    Dependency,
    CompleteDSLPckg_Abstraction,
    CompleteDSLPckg_Deployment,
    CompleteDSLPckg_Usage,
    InstanceSpecification,
    CompleteDSLPckg_EnumerationLiteral,
    DataType,
    CompleteDSLPckg_Enumeration,
    CompleteDSLPckg_PrimitiveType,
    EncapsulatedClassifier,
    StructuredClassifier,
    CompleteDSLPckg_EncapsulatedClassifier,
    BehavioredClassifier,
    CompleteDSLPckg_UseCase,
    CompleteDSLPckg_Actor,
    CompleteDSLPckg_Collaboration,
    Classifier,
    CompleteDSLPckg_Signal,
    CompleteDSLPckg_StructuredClassifier,
    CompleteDSLPckg_BehavioredClassifier,
    BehavioralFeature,
    CompleteDSLPckg_Reception,
    CompleteDSLPckg_Operation,
    CompleteDSLPckg_Interface,
    CompleteDSLPckg_DataType,
    CompleteDSLPckg_Class,
    DeploymentTarget,
    CompleteDSLPckg_Node,
    ConnectableElement,
    StructuralFeature,
    MultiplicityElement,
    Feature,
    CompleteDSLPckg_Connector,
    CompleteDSLPckg_Substitution,
    CompleteDSLPckg_Property,
    Type,
    RedefinableElement,
    CompleteDSLPckg_Feature,
    CompleteDSLPckg_ExtensionPoint,
    CompleteDSLPckg_ActivityEdge,
    CompleteDSLPckg_InstanceValue,
    LiteralSpecification,
    CompleteDSLPckg_LiteralString,
    CompleteDSLPckg_LiteralUnilimitedNatural,
    CompleteDSLPckg_LiteralBoolean,
    CompleteDSLPckg_LiteralReal,
    CompleteDSLPckg_LiteralInteger,
    CompleteDSLPckg_LiteralNull,
    CompleteDSLPckg_Behavior,
    ValueSpecification,
    CompleteDSLPckg_Duration,
    CompleteDSLPckg_TimeExpression,
    CompleteDSLPckg_LiteralSpecification,
    CompleteDSLPckg_Interval,
    CompleteDSLPckg_OpaqueExpression,
    CompleteDSLPckg_Expression,
    TypedElement,
    CompleteDSLPckg_Parameter,
    CompleteDSLPckg_Variable,
    CompleteDSLPckg_ObjectNode,
    CompleteDSLPckg_Pin,
    CompleteDSLPckg_ConnectableElement,
    CompleteDSLPckg_StructuralFeature,
    Relationship,
    CompleteDSLPckg_Association,
    CompleteDSLPckg_DirectedRelationship,
    PackageableElement,
    CompleteDSLPckg_InstanceSpecification,
    CompleteDSLPckg_GeneralizationSet,
    CompleteDSLPckg_Observation,
    CompleteDSLPckg_Type,
    CompleteDSLPckg_Event,
    CompleteDSLPckg_ValueSpecification,
    Namespace,
    CompleteDSLPckg_State,
    CompleteDSLPckg_Classifier,
    CompleteDSLPckg_Region,
    CompleteDSLPckg_Transition,
    CompleteDSLPckg_InteractionOperand,
    CompleteDSLPckg_StructuredActivityNode,
    CompleteDSLPckg_BehavioralFeature,
    CompleteDSLPckg_Package,
    DirectedRelationship,
    CompleteDSLPckg_Generalization,
    CompleteDSLPckg_ProtocolConformance,
    CompleteDSLPckg_PackageMerge,
    CompleteDSLPckg_Constraint,
    CompleteDSLPckg_PackageImport,
    CompleteDSLPckg_ElementImport,
    CompleteDSLPckg_Dependency,
    Element,
    CompleteDSLPckg_MultiplicityElement,
    CompleteDSLPckg_Slot,
    CompleteDSLPckg_LinkEndData,
    CompleteDSLPckg_QualifierValue,
    CompleteDSLPckg_Clause,
    CompleteDSLPckg_Relationship,
    CompleteDSLPckg_ExceptionHandler,
    CompleteDSLPckg_NamedElement,
    CompleteDSLPckg_Comment,
    CompleteDSLPckg_Element,
    NamedElement,
    CompleteDSLPckg_TypedElement,
    CompleteDSLPckg_MessageEnd,
    CompleteDSLPckg_Message,
    CompleteDSLPckg_Lifeline,
    CompleteDSLPckg_GeneralOrdering,
    CompleteDSLPckg_Component,
    CompleteDSLPckg_Namespace,
    CompleteDSLPckg_CollaborationUse,
    CompleteDSLPckg_Vertex,
    CompleteDSLPckg_RedefinableElement,
    CompleteDSLPckg_PackageableElement,
    CompleteDSLPckg_DeploymentTarget,
    CompleteDSLPckg_ParameterSet,
    CompleteDSLPckg_InteractionFragment,
    CompleteDSLPckg_DeployedArtifact,
    CompleteDSLPckg_Extend,
    CompleteDSLPckg_Artifact,
    CompleteDSLPckg_ActivityGroup,
    CompleteDSLPckg_ActivityNode,
    CompleteDSLPckg_Trigger,
    CompleteDSLPckg_Action,
    CompleteDSLPckg_Include,
    InteractionOperandKind,
    TransitionKind,
    VisibilityKind,
    ExpansionKind,
    ParameterEffectKind,
    AggregationKind,
    MessageSort,
    ConnectorKind,
    ObjectNodeOrderingKind,
    CallConcurrencyFeature,
    MessageKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ProtocolTransition)


def test_completedslpckg_protocoltransition_constructor_exists():
    assert callable(CompleteDSLPckg_ProtocolTransition.__init__)


def test_completedslpckg_protocoltransition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ProtocolStateMachine)


def test_completedslpckg_protocolstatemachine_constructor_exists():
    assert callable(CompleteDSLPckg_ProtocolStateMachine.__init__)


def test_completedslpckg_protocolstatemachine_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_finalstate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FinalState)


def test_completedslpckg_finalstate_constructor_exists():
    assert callable(CompleteDSLPckg_FinalState.__init__)


def test_completedslpckg_finalstate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConnectionPointReference)


def test_completedslpckg_connectionpointreference_constructor_exists():
    assert callable(CompleteDSLPckg_ConnectionPointReference.__init__)


def test_completedslpckg_connectionpointreference_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RemoveVariableValueAction)


def test_completedslpckg_removevariablevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_RemoveVariableValueAction.__init__)


def test_completedslpckg_removevariablevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AddVariableValueAction)


def test_completedslpckg_addvariablevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_AddVariableValueAction.__init__)


def test_completedslpckg_addvariablevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ClearVariableAction)


def test_completedslpckg_clearvariableaction_constructor_exists():
    assert callable(CompleteDSLPckg_ClearVariableAction.__init__)


def test_completedslpckg_clearvariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_WriteVariableAction)


def test_completedslpckg_writevariableaction_constructor_exists():
    assert callable(CompleteDSLPckg_WriteVariableAction.__init__)


def test_completedslpckg_writevariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadVariableAction)


def test_completedslpckg_readvariableaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadVariableAction.__init__)


def test_completedslpckg_readvariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_pseudostate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Pseudostate)


def test_completedslpckg_pseudostate_constructor_exists():
    assert callable(CompleteDSLPckg_Pseudostate.__init__)


def test_completedslpckg_pseudostate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CreateLinkObjectAction)


def test_completedslpckg_createlinkobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_CreateLinkObjectAction.__init__)


def test_completedslpckg_createlinkobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_readlsclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadlsClassifiedObjectAction)


def test_completedslpckg_readlsclassifiedobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadlsClassifiedObjectAction.__init__)


def test_completedslpckg_readlsclassifiedobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadlsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AcceptCallAction)


def test_completedslpckg_acceptcallaction_constructor_exists():
    assert callable(CompleteDSLPckg_AcceptCallAction.__init__)


def test_completedslpckg_acceptcallaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_WriteLinkAction)


def test_completedslpckg_writelinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_WriteLinkAction.__init__)


def test_completedslpckg_writelinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadLinkAction)


def test_completedslpckg_readlinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadLinkAction.__init__)


def test_completedslpckg_readlinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RemoveStructuralFeatureValueAction)


def test_completedslpckg_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_RemoveStructuralFeatureValueAction.__init__)


def test_completedslpckg_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AddStructuralFeatureValueAction)


def test_completedslpckg_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg_AddStructuralFeatureValueAction.__init__)


def test_completedslpckg_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkEndDestructionData)


def test_completedslpckg_linkenddestructiondata_constructor_exists():
    assert callable(CompleteDSLPckg_LinkEndDestructionData.__init__)


def test_completedslpckg_linkenddestructiondata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_completedslpckg_linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(CompleteDSLPckg_LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in CompleteDSLPckg_LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkEndCreationData)


def test_completedslpckg_linkendcreationdata_constructor_exists():
    assert callable(CompleteDSLPckg_LinkEndCreationData.__init__)


def test_completedslpckg_linkendcreationdata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_completedslpckg_linkendcreationdata_has_isReplaceAll():
    assert hasattr(CompleteDSLPckg_LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in CompleteDSLPckg_LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_interactionuse_is_not_abstract():
    assert not inspect.isabstract(InteractionUse)


def test_interactionuse_constructor_exists():
    assert callable(InteractionUse.__init__)


def test_interactionuse_constructor_args():
    sig = inspect.signature(InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConsiderIgnoreFragment)


def test_completedslpckg_considerignorefragment_constructor_exists():
    assert callable(CompleteDSLPckg_ConsiderIgnoreFragment.__init__)


def test_completedslpckg_considerignorefragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CombinedFragment)


def test_completedslpckg_combinedfragment_constructor_exists():
    assert callable(CompleteDSLPckg_CombinedFragment.__init__)


def test_completedslpckg_combinedfragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_completedslpckg_combinedfragment_has_interactionOperator():
    assert hasattr(CompleteDSLPckg_CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in CompleteDSLPckg_CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_partdecomposition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PartDecomposition)


def test_completedslpckg_partdecomposition_constructor_exists():
    assert callable(CompleteDSLPckg_PartDecomposition.__init__)


def test_completedslpckg_partdecomposition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActionExecutionSpecification)


def test_completedslpckg_actionexecutionspecification_constructor_exists():
    assert callable(CompleteDSLPckg_ActionExecutionSpecification.__init__)


def test_completedslpckg_actionexecutionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BehaviorExecutionSpecification)


def test_completedslpckg_behaviorexecutionspecification_constructor_exists():
    assert callable(CompleteDSLPckg_BehaviorExecutionSpecification.__init__)


def test_completedslpckg_behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(MessageOccurrenceSpecification)


def test_messageoccurrencespecification_constructor_exists():
    assert callable(MessageOccurrenceSpecification.__init__)


def test_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_destructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DestructionOccurrenceSpecification)


def test_completedslpckg_destructionoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_DestructionOccurrenceSpecification.__init__)


def test_completedslpckg_destructionoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_occurencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurenceSpecification)


def test_occurencespecification_constructor_exists():
    assert callable(OccurenceSpecification.__init__)


def test_occurencespecification_constructor_args():
    sig = inspect.signature(OccurenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MessageOccurrenceSpecification)


def test_completedslpckg_messageoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_MessageOccurrenceSpecification.__init__)


def test_completedslpckg_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutionOccurrenceSpecification)


def test_completedslpckg_executionoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutionOccurrenceSpecification.__init__)


def test_completedslpckg_executionoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_continuation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Continuation)


def test_completedslpckg_continuation_constructor_exists():
    assert callable(CompleteDSLPckg_Continuation.__init__)


def test_completedslpckg_continuation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_completedslpckg_continuation_has_setting():
    assert hasattr(CompleteDSLPckg_Continuation, "setting")
    descriptor = None
    for klass in CompleteDSLPckg_Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_interactionuse_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionUse)


def test_completedslpckg_interactionuse_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionUse.__init__)


def test_completedslpckg_interactionuse_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_occurencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OccurenceSpecification)


def test_completedslpckg_occurencespecification_constructor_exists():
    assert callable(CompleteDSLPckg_OccurenceSpecification.__init__)


def test_completedslpckg_occurencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OccurenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StateInvariant)


def test_completedslpckg_stateinvariant_constructor_exists():
    assert callable(CompleteDSLPckg_StateInvariant.__init__)


def test_completedslpckg_stateinvariant_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_executionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutionSpecification)


def test_completedslpckg_executionspecification_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutionSpecification.__init__)


def test_completedslpckg_executionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_gate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Gate)


def test_completedslpckg_gate_constructor_exists():
    assert callable(CompleteDSLPckg_Gate.__init__)


def test_completedslpckg_gate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Gate.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_datastorenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DataStoreNode)


def test_completedslpckg_datastorenode_constructor_exists():
    assert callable(CompleteDSLPckg_DataStoreNode.__init__)


def test_completedslpckg_datastorenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConditionalNode)


def test_completedslpckg_conditionalnode_constructor_exists():
    assert callable(CompleteDSLPckg_ConditionalNode.__init__)


def test_completedslpckg_conditionalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssumed" in params, "Missing parameter 'isAssumed'"

def test_completedslpckg_conditionalnode_has_isDeterminate():
    assert hasattr(CompleteDSLPckg_ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in CompleteDSLPckg_ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_conditionalnode_has_isAssumed():
    assert hasattr(CompleteDSLPckg_ConditionalNode, "isAssumed")
    descriptor = None
    for klass in CompleteDSLPckg_ConditionalNode.__mro__:
        if "isAssumed" in klass.__dict__:
            descriptor = klass.__dict__["isAssumed"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_expansionregion_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExpansionRegion)


def test_completedslpckg_expansionregion_constructor_exists():
    assert callable(CompleteDSLPckg_ExpansionRegion.__init__)


def test_completedslpckg_expansionregion_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_completedslpckg_expansionregion_has_mode():
    assert hasattr(CompleteDSLPckg_ExpansionRegion, "mode")
    descriptor = None
    for klass in CompleteDSLPckg_ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_sequencenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SequenceNode)


def test_completedslpckg_sequencenode_constructor_exists():
    assert callable(CompleteDSLPckg_SequenceNode.__init__)


def test_completedslpckg_sequencenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_loopnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LoopNode)


def test_completedslpckg_loopnode_constructor_exists():
    assert callable(CompleteDSLPckg_LoopNode.__init__)


def test_completedslpckg_loopnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_completedslpckg_loopnode_has_isTestedFirst():
    assert hasattr(CompleteDSLPckg_LoopNode, "isTestedFirst")
    descriptor = None
    for klass in CompleteDSLPckg_LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_executablenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutableNode)


def test_completedslpckg_executablenode_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutableNode.__init__)


def test_completedslpckg_executablenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_objectflow_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ObjectFlow)


def test_completedslpckg_objectflow_constructor_exists():
    assert callable(CompleteDSLPckg_ObjectFlow.__init__)


def test_completedslpckg_objectflow_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"

def test_completedslpckg_objectflow_has_ordering():
    assert hasattr(CompleteDSLPckg_ObjectFlow, "ordering")
    descriptor = None
    for klass in CompleteDSLPckg_ObjectFlow.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_objectflow_has_isControlType():
    assert hasattr(CompleteDSLPckg_ObjectFlow, "isControlType")
    descriptor = None
    for klass in CompleteDSLPckg_ObjectFlow.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_objectflow_has_isMultireceive():
    assert hasattr(CompleteDSLPckg_ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in CompleteDSLPckg_ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_objectflow_has_isMulticast():
    assert hasattr(CompleteDSLPckg_ObjectFlow, "isMulticast")
    descriptor = None
    for klass in CompleteDSLPckg_ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_controlflow_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ControlFlow)


def test_completedslpckg_controlflow_constructor_exists():
    assert callable(CompleteDSLPckg_ControlFlow.__init__)


def test_completedslpckg_controlflow_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InterruptibleActivityRegion)


def test_completedslpckg_interruptibleactivityregion_constructor_exists():
    assert callable(CompleteDSLPckg_InterruptibleActivityRegion.__init__)


def test_completedslpckg_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_activitypartition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityPartition)


def test_completedslpckg_activitypartition_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityPartition.__init__)


def test_completedslpckg_activitypartition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FlowFinalNode)


def test_completedslpckg_flowfinalnode_constructor_exists():
    assert callable(CompleteDSLPckg_FlowFinalNode.__init__)


def test_completedslpckg_flowfinalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_joinnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_JoinNode)


def test_completedslpckg_joinnode_constructor_exists():
    assert callable(CompleteDSLPckg_JoinNode.__init__)


def test_completedslpckg_joinnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_completedslpckg_joinnode_has_isCombineDuplicate():
    assert hasattr(CompleteDSLPckg_JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in CompleteDSLPckg_JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_decisionnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DecisionNode)


def test_completedslpckg_decisionnode_constructor_exists():
    assert callable(CompleteDSLPckg_DecisionNode.__init__)


def test_completedslpckg_decisionnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_finalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FinalNode)


def test_completedslpckg_finalnode_constructor_exists():
    assert callable(CompleteDSLPckg_FinalNode.__init__)


def test_completedslpckg_finalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_forknode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ForkNode)


def test_completedslpckg_forknode_constructor_exists():
    assert callable(CompleteDSLPckg_ForkNode.__init__)


def test_completedslpckg_forknode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_initialnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InitialNode)


def test_completedslpckg_initialnode_constructor_exists():
    assert callable(CompleteDSLPckg_InitialNode.__init__)


def test_completedslpckg_initialnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_mergenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MergeNode)


def test_completedslpckg_mergenode_constructor_exists():
    assert callable(CompleteDSLPckg_MergeNode.__init__)


def test_completedslpckg_mergenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityFinalNode)


def test_completedslpckg_activityfinalnode_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityFinalNode.__init__)


def test_completedslpckg_activityfinalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_controlnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ControlNode)


def test_completedslpckg_controlnode_constructor_exists():
    assert callable(CompleteDSLPckg_ControlNode.__init__)


def test_completedslpckg_controlnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_expansionnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExpansionNode)


def test_completedslpckg_expansionnode_constructor_exists():
    assert callable(CompleteDSLPckg_ExpansionNode.__init__)


def test_completedslpckg_expansionnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CentralBufferNode)


def test_completedslpckg_centralbuffernode_constructor_exists():
    assert callable(CompleteDSLPckg_CentralBufferNode.__init__)


def test_completedslpckg_centralbuffernode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityParameterNode)


def test_completedslpckg_activityparameternode_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityParameterNode.__init__)


def test_completedslpckg_activityparameternode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DestroyLinkAction)


def test_completedslpckg_destroylinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_DestroyLinkAction.__init__)


def test_completedslpckg_destroylinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CreateLinkAction)


def test_completedslpckg_createlinkaction_constructor_exists():
    assert callable(CompleteDSLPckg_CreateLinkAction.__init__)


def test_completedslpckg_createlinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ClearStructuralFeatureAction)


def test_completedslpckg_clearstructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_ClearStructuralFeatureAction.__init__)


def test_completedslpckg_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_WriteStructuralFeatureAction)


def test_completedslpckg_writestructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_WriteStructuralFeatureAction.__init__)


def test_completedslpckg_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadStructuralFeatureAction)


def test_completedslpckg_readstructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadStructuralFeatureAction.__init__)


def test_completedslpckg_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallOperationAction)


def test_completedslpckg_calloperationaction_constructor_exists():
    assert callable(CompleteDSLPckg_CallOperationAction.__init__)


def test_completedslpckg_calloperationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StartObjectBehaviorAction)


def test_completedslpckg_startobjectbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg_StartObjectBehaviorAction.__init__)


def test_completedslpckg_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallBehaviorAction)


def test_completedslpckg_callbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg_CallBehaviorAction.__init__)


def test_completedslpckg_callbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SendSignalAction)


def test_completedslpckg_sendsignalaction_constructor_exists():
    assert callable(CompleteDSLPckg_SendSignalAction.__init__)


def test_completedslpckg_sendsignalaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BroadcastSignalAction)


def test_completedslpckg_broadcastsignalaction_constructor_exists():
    assert callable(CompleteDSLPckg_BroadcastSignalAction.__init__)


def test_completedslpckg_broadcastsignalaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_callaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallAction)


def test_completedslpckg_callaction_constructor_exists():
    assert callable(CompleteDSLPckg_CallAction.__init__)


def test_completedslpckg_callaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_completedslpckg_callaction_has_isSynchronous():
    assert hasattr(CompleteDSLPckg_CallAction, "isSynchronous")
    descriptor = None
    for klass in CompleteDSLPckg_CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_actioninputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActionInputPin)


def test_completedslpckg_actioninputpin_constructor_exists():
    assert callable(CompleteDSLPckg_ActionInputPin.__init__)


def test_completedslpckg_actioninputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_valuepin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ValuePin)


def test_completedslpckg_valuepin_constructor_exists():
    assert callable(CompleteDSLPckg_ValuePin.__init__)


def test_completedslpckg_valuepin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DestroyObjectAction)


def test_completedslpckg_destroyobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_DestroyObjectAction.__init__)


def test_completedslpckg_destroyobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReclassifyObjectAction)


def test_completedslpckg_reclassifyobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReclassifyObjectAction.__init__)


def test_completedslpckg_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_completedslpckg_reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(CompleteDSLPckg_ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in CompleteDSLPckg_ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TestIdentityAction)


def test_completedslpckg_testidentityaction_constructor_exists():
    assert callable(CompleteDSLPckg_TestIdentityAction.__init__)


def test_completedslpckg_testidentityaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_readselfaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadSelfAction)


def test_completedslpckg_readselfaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadSelfAction.__init__)


def test_completedslpckg_readselfaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ValueSpecificationAction)


def test_completedslpckg_valuespecificationaction_constructor_exists():
    assert callable(CompleteDSLPckg_ValueSpecificationAction.__init__)


def test_completedslpckg_valuespecificationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_variableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_VariableAction)


def test_completedslpckg_variableaction_constructor_exists():
    assert callable(CompleteDSLPckg_VariableAction.__init__)


def test_completedslpckg_variableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_reduceaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReduceAction)


def test_completedslpckg_reduceaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReduceAction.__init__)


def test_completedslpckg_reduceaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_completedslpckg_reduceaction_has_isOrdered():
    assert hasattr(CompleteDSLPckg_ReduceAction, "isOrdered")
    descriptor = None
    for klass in CompleteDSLPckg_ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuralFeatureAction)


def test_completedslpckg_structuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg_StructuralFeatureAction.__init__)


def test_completedslpckg_structuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadLinkObjectEndAction)


def test_completedslpckg_readlinkobjectendaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadLinkObjectEndAction.__init__)


def test_completedslpckg_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RaiseExceptionAction)


def test_completedslpckg_raiseexceptionaction_constructor_exists():
    assert callable(CompleteDSLPckg_RaiseExceptionAction.__init__)


def test_completedslpckg_raiseexceptionaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_replyaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReplyAction)


def test_completedslpckg_replyaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReplyAction.__init__)


def test_completedslpckg_replyaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadLinkObjectEndQualifierAction)


def test_completedslpckg_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadLinkObjectEndQualifierAction.__init__)


def test_completedslpckg_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CreateObjectAction)


def test_completedslpckg_createobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_CreateObjectAction.__init__)


def test_completedslpckg_createobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StartClassifierBehaviorAction)


def test_completedslpckg_startclassifierbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg_StartClassifierBehaviorAction.__init__)


def test_completedslpckg_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_linkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkAction)


def test_completedslpckg_linkaction_constructor_exists():
    assert callable(CompleteDSLPckg_LinkAction.__init__)


def test_completedslpckg_linkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_UnmarshallAction)


def test_completedslpckg_unmarshallaction_constructor_exists():
    assert callable(CompleteDSLPckg_UnmarshallAction.__init__)


def test_completedslpckg_unmarshallaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AcceptEventAction)


def test_completedslpckg_accepteventaction_constructor_exists():
    assert callable(CompleteDSLPckg_AcceptEventAction.__init__)


def test_completedslpckg_accepteventaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_completedslpckg_accepteventaction_has_isUnmarshall():
    assert hasattr(CompleteDSLPckg_AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in CompleteDSLPckg_AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_readextendaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ReadExtendAction)


def test_completedslpckg_readextendaction_constructor_exists():
    assert callable(CompleteDSLPckg_ReadExtendAction.__init__)


def test_completedslpckg_readextendaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ReadExtendAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OpaqueAction)


def test_completedslpckg_opaqueaction_constructor_exists():
    assert callable(CompleteDSLPckg_OpaqueAction.__init__)


def test_completedslpckg_opaqueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_completedslpckg_opaqueaction_has_body():
    assert hasattr(CompleteDSLPckg_OpaqueAction, "body")
    descriptor = None
    for klass in CompleteDSLPckg_OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_opaqueaction_has_language():
    assert hasattr(CompleteDSLPckg_OpaqueAction, "language")
    descriptor = None
    for klass in CompleteDSLPckg_OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SendObjectAction)


def test_completedslpckg_sendobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg_SendObjectAction.__init__)


def test_completedslpckg_sendobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_inputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InputPin)


def test_completedslpckg_inputpin_constructor_exists():
    assert callable(CompleteDSLPckg_InputPin.__init__)


def test_completedslpckg_inputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DeploymentSpecification)


def test_completedslpckg_deploymentspecification_constructor_exists():
    assert callable(CompleteDSLPckg_DeploymentSpecification.__init__)


def test_completedslpckg_deploymentspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"

def test_completedslpckg_deploymentspecification_has_executionLocation():
    assert hasattr(CompleteDSLPckg_DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in CompleteDSLPckg_DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_deploymentspecification_has_deploymentLocation():
    assert hasattr(CompleteDSLPckg_DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in CompleteDSLPckg_DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExecutionEnvironment)


def test_completedslpckg_executionenvironment_constructor_exists():
    assert callable(CompleteDSLPckg_ExecutionEnvironment.__init__)


def test_completedslpckg_executionenvironment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_device_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Device)


def test_completedslpckg_device_constructor_exists():
    assert callable(CompleteDSLPckg_Device.__init__)


def test_completedslpckg_device_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Device.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_outputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OutputPin)


def test_completedslpckg_outputpin_constructor_exists():
    assert callable(CompleteDSLPckg_OutputPin.__init__)


def test_completedslpckg_outputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_invocationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InvocationAction)


def test_completedslpckg_invocationaction_constructor_exists():
    assert callable(CompleteDSLPckg_InvocationAction.__init__)


def test_completedslpckg_invocationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_connectorend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConnectorEnd)


def test_completedslpckg_connectorend_constructor_exists():
    assert callable(CompleteDSLPckg_ConnectorEnd.__init__)


def test_completedslpckg_connectorend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_port_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Port)


def test_completedslpckg_port_constructor_exists():
    assert callable(CompleteDSLPckg_Port.__init__)


def test_completedslpckg_port_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Port.__init__)
    params = list(sig.parameters.keys())
    assert "isConjugated" in params, "Missing parameter 'isConjugated'"
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"
    assert "isService" in params, "Missing parameter 'isService'"

def test_completedslpckg_port_has_isConjugated():
    assert hasattr(CompleteDSLPckg_Port, "isConjugated")
    descriptor = None
    for klass in CompleteDSLPckg_Port.__mro__:
        if "isConjugated" in klass.__dict__:
            descriptor = klass.__dict__["isConjugated"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_port_has_isBehavior():
    assert hasattr(CompleteDSLPckg_Port, "isBehavior")
    descriptor = None
    for klass in CompleteDSLPckg_Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_port_has_isService():
    assert hasattr(CompleteDSLPckg_Port, "isService")
    descriptor = None
    for klass in CompleteDSLPckg_Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DurationConstraint)


def test_completedslpckg_durationconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_DurationConstraint.__init__)


def test_completedslpckg_durationconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg_durationconstraint_has_firstEvent():
    assert hasattr(CompleteDSLPckg_DurationConstraint, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg_DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeConstraint)


def test_completedslpckg_timeconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_TimeConstraint.__init__)


def test_completedslpckg_timeconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg_timeconstraint_has_firstEvent():
    assert hasattr(CompleteDSLPckg_TimeConstraint, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg_TimeConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionConstraint)


def test_completedslpckg_interactionconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionConstraint.__init__)


def test_completedslpckg_interactionconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_IntervalConstraint)


def test_completedslpckg_intervalconstraint_constructor_exists():
    assert callable(CompleteDSLPckg_IntervalConstraint.__init__)


def test_completedslpckg_intervalconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_durationinterval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DurationInterval)


def test_completedslpckg_durationinterval_constructor_exists():
    assert callable(CompleteDSLPckg_DurationInterval.__init__)


def test_completedslpckg_durationinterval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_timeinterval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeInterval)


def test_completedslpckg_timeinterval_constructor_exists():
    assert callable(CompleteDSLPckg_TimeInterval.__init__)


def test_completedslpckg_timeinterval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_durationobservation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DurationObservation)


def test_completedslpckg_durationobservation_constructor_exists():
    assert callable(CompleteDSLPckg_DurationObservation.__init__)


def test_completedslpckg_durationobservation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg_durationobservation_has_firstEvent():
    assert hasattr(CompleteDSLPckg_DurationObservation, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg_DurationObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_timeobservation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeObservation)


def test_completedslpckg_timeobservation_constructor_exists():
    assert callable(CompleteDSLPckg_TimeObservation.__init__)


def test_completedslpckg_timeobservation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg_timeobservation_has_firstEvent():
    assert hasattr(CompleteDSLPckg_TimeObservation, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg_TimeObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_timeevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeEvent)


def test_completedslpckg_timeevent_constructor_exists():
    assert callable(CompleteDSLPckg_TimeEvent.__init__)


def test_completedslpckg_timeevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_completedslpckg_timeevent_has_isRelative():
    assert hasattr(CompleteDSLPckg_TimeEvent, "isRelative")
    descriptor = None
    for klass in CompleteDSLPckg_TimeEvent.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_signalevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_SignalEvent)


def test_completedslpckg_signalevent_constructor_exists():
    assert callable(CompleteDSLPckg_SignalEvent.__init__)


def test_completedslpckg_signalevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_callevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CallEvent)


def test_completedslpckg_callevent_constructor_exists():
    assert callable(CompleteDSLPckg_CallEvent.__init__)


def test_completedslpckg_callevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AnyReceiveEvent)


def test_completedslpckg_anyreceiveevent_constructor_exists():
    assert callable(CompleteDSLPckg_AnyReceiveEvent.__init__)


def test_completedslpckg_anyreceiveevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_changeevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ChangeEvent)


def test_completedslpckg_changeevent_constructor_exists():
    assert callable(CompleteDSLPckg_ChangeEvent.__init__)


def test_completedslpckg_changeevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_messageevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MessageEvent)


def test_completedslpckg_messageevent_constructor_exists():
    assert callable(CompleteDSLPckg_MessageEvent.__init__)


def test_completedslpckg_messageevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_FunctionBehavior)


def test_completedslpckg_functionbehavior_constructor_exists():
    assert callable(CompleteDSLPckg_FunctionBehavior.__init__)


def test_completedslpckg_functionbehavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_interaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Interaction)


def test_completedslpckg_interaction_constructor_exists():
    assert callable(CompleteDSLPckg_Interaction.__init__)


def test_completedslpckg_interaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_statemachine_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StateMachine)


def test_completedslpckg_statemachine_constructor_exists():
    assert callable(CompleteDSLPckg_StateMachine.__init__)


def test_completedslpckg_statemachine_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_activity_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Activity)


def test_completedslpckg_activity_constructor_exists():
    assert callable(CompleteDSLPckg_Activity.__init__)


def test_completedslpckg_activity_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_completedslpckg_activity_has_isSingleExecution():
    assert hasattr(CompleteDSLPckg_Activity, "isSingleExecution")
    descriptor = None
    for klass in CompleteDSLPckg_Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_activity_has_isReadOnly():
    assert hasattr(CompleteDSLPckg_Activity, "isReadOnly")
    descriptor = None
    for klass in CompleteDSLPckg_Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OpaqueBehavior)


def test_completedslpckg_opaquebehavior_constructor_exists():
    assert callable(CompleteDSLPckg_OpaqueBehavior.__init__)


def test_completedslpckg_opaquebehavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_completedslpckg_opaquebehavior_has_language():
    assert hasattr(CompleteDSLPckg_OpaqueBehavior, "language")
    descriptor = None
    for klass in CompleteDSLPckg_OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_opaquebehavior_has_body():
    assert hasattr(CompleteDSLPckg_OpaqueBehavior, "body")
    descriptor = None
    for klass in CompleteDSLPckg_OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_communicationpath_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CommunicationPath)


def test_completedslpckg_communicationpath_constructor_exists():
    assert callable(CompleteDSLPckg_CommunicationPath.__init__)


def test_completedslpckg_communicationpath_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_associationclass_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_AssociationClass)


def test_completedslpckg_associationclass_constructor_exists():
    assert callable(CompleteDSLPckg_AssociationClass.__init__)


def test_completedslpckg_associationclass_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_interfacerealization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InterfaceRealization)


def test_completedslpckg_interfacerealization_constructor_exists():
    assert callable(CompleteDSLPckg_InterfaceRealization.__init__)


def test_completedslpckg_interfacerealization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_componentrealization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ComponentRealization)


def test_completedslpckg_componentrealization_constructor_exists():
    assert callable(CompleteDSLPckg_ComponentRealization.__init__)


def test_completedslpckg_componentrealization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_manifestation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Manifestation)


def test_completedslpckg_manifestation_constructor_exists():
    assert callable(CompleteDSLPckg_Manifestation.__init__)


def test_completedslpckg_manifestation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_realization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Realization)


def test_completedslpckg_realization_constructor_exists():
    assert callable(CompleteDSLPckg_Realization.__init__)


def test_completedslpckg_realization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Realization.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_abstraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Abstraction)


def test_completedslpckg_abstraction_constructor_exists():
    assert callable(CompleteDSLPckg_Abstraction.__init__)


def test_completedslpckg_abstraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_deployment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Deployment)


def test_completedslpckg_deployment_constructor_exists():
    assert callable(CompleteDSLPckg_Deployment.__init__)


def test_completedslpckg_deployment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Deployment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_usage_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Usage)


def test_completedslpckg_usage_constructor_exists():
    assert callable(CompleteDSLPckg_Usage.__init__)


def test_completedslpckg_usage_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Usage.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_EnumerationLiteral)


def test_completedslpckg_enumerationliteral_constructor_exists():
    assert callable(CompleteDSLPckg_EnumerationLiteral.__init__)


def test_completedslpckg_enumerationliteral_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_enumeration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Enumeration)


def test_completedslpckg_enumeration_constructor_exists():
    assert callable(CompleteDSLPckg_Enumeration.__init__)


def test_completedslpckg_enumeration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_primitivetype_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PrimitiveType)


def test_completedslpckg_primitivetype_constructor_exists():
    assert callable(CompleteDSLPckg_PrimitiveType.__init__)


def test_completedslpckg_primitivetype_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_EncapsulatedClassifier)


def test_completedslpckg_encapsulatedclassifier_constructor_exists():
    assert callable(CompleteDSLPckg_EncapsulatedClassifier.__init__)


def test_completedslpckg_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_usecase_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_UseCase)


def test_completedslpckg_usecase_constructor_exists():
    assert callable(CompleteDSLPckg_UseCase.__init__)


def test_completedslpckg_usecase_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_actor_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Actor)


def test_completedslpckg_actor_constructor_exists():
    assert callable(CompleteDSLPckg_Actor.__init__)


def test_completedslpckg_actor_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Actor.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_collaboration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Collaboration)


def test_completedslpckg_collaboration_constructor_exists():
    assert callable(CompleteDSLPckg_Collaboration.__init__)


def test_completedslpckg_collaboration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_signal_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Signal)


def test_completedslpckg_signal_constructor_exists():
    assert callable(CompleteDSLPckg_Signal.__init__)


def test_completedslpckg_signal_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Signal.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuredClassifier)


def test_completedslpckg_structuredclassifier_constructor_exists():
    assert callable(CompleteDSLPckg_StructuredClassifier.__init__)


def test_completedslpckg_structuredclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BehavioredClassifier)


def test_completedslpckg_behavioredclassifier_constructor_exists():
    assert callable(CompleteDSLPckg_BehavioredClassifier.__init__)


def test_completedslpckg_behavioredclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_reception_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Reception)


def test_completedslpckg_reception_constructor_exists():
    assert callable(CompleteDSLPckg_Reception.__init__)


def test_completedslpckg_reception_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Reception.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_operation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Operation)


def test_completedslpckg_operation_constructor_exists():
    assert callable(CompleteDSLPckg_Operation.__init__)


def test_completedslpckg_operation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_completedslpckg_operation_has_upper():
    assert hasattr(CompleteDSLPckg_Operation, "upper")
    descriptor = None
    for klass in CompleteDSLPckg_Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_operation_has_isUnique():
    assert hasattr(CompleteDSLPckg_Operation, "isUnique")
    descriptor = None
    for klass in CompleteDSLPckg_Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_operation_has_isOrdered():
    assert hasattr(CompleteDSLPckg_Operation, "isOrdered")
    descriptor = None
    for klass in CompleteDSLPckg_Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_operation_has_lower():
    assert hasattr(CompleteDSLPckg_Operation, "lower")
    descriptor = None
    for klass in CompleteDSLPckg_Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_operation_has_isQuery():
    assert hasattr(CompleteDSLPckg_Operation, "isQuery")
    descriptor = None
    for klass in CompleteDSLPckg_Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_interface_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Interface)


def test_completedslpckg_interface_constructor_exists():
    assert callable(CompleteDSLPckg_Interface.__init__)


def test_completedslpckg_interface_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Interface.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_datatype_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DataType)


def test_completedslpckg_datatype_constructor_exists():
    assert callable(CompleteDSLPckg_DataType.__init__)


def test_completedslpckg_datatype_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DataType.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_class_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Class)


def test_completedslpckg_class_constructor_exists():
    assert callable(CompleteDSLPckg_Class.__init__)


def test_completedslpckg_class_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Class.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_node_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Node)


def test_completedslpckg_node_constructor_exists():
    assert callable(CompleteDSLPckg_Node.__init__)


def test_completedslpckg_node_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Node.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_connector_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Connector)


def test_completedslpckg_connector_constructor_exists():
    assert callable(CompleteDSLPckg_Connector.__init__)


def test_completedslpckg_connector_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_completedslpckg_connector_has_kind():
    assert hasattr(CompleteDSLPckg_Connector, "kind")
    descriptor = None
    for klass in CompleteDSLPckg_Connector.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_substitution_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Substitution)


def test_completedslpckg_substitution_constructor_exists():
    assert callable(CompleteDSLPckg_Substitution.__init__)


def test_completedslpckg_substitution_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Substitution.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_property_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Property)


def test_completedslpckg_property_constructor_exists():
    assert callable(CompleteDSLPckg_Property.__init__)


def test_completedslpckg_property_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "default" in params, "Missing parameter 'default'"

def test_completedslpckg_property_has_isID():
    assert hasattr(CompleteDSLPckg_Property, "isID")
    descriptor = None
    for klass in CompleteDSLPckg_Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_property_has_isComposite():
    assert hasattr(CompleteDSLPckg_Property, "isComposite")
    descriptor = None
    for klass in CompleteDSLPckg_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_property_has_isDerivedUnion():
    assert hasattr(CompleteDSLPckg_Property, "isDerivedUnion")
    descriptor = None
    for klass in CompleteDSLPckg_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_property_has_isDerived():
    assert hasattr(CompleteDSLPckg_Property, "isDerived")
    descriptor = None
    for klass in CompleteDSLPckg_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_property_has_aggregation():
    assert hasattr(CompleteDSLPckg_Property, "aggregation")
    descriptor = None
    for klass in CompleteDSLPckg_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_property_has_default():
    assert hasattr(CompleteDSLPckg_Property, "default")
    descriptor = None
    for klass in CompleteDSLPckg_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_feature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Feature)


def test_completedslpckg_feature_constructor_exists():
    assert callable(CompleteDSLPckg_Feature.__init__)


def test_completedslpckg_feature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_completedslpckg_feature_has_isStatic():
    assert hasattr(CompleteDSLPckg_Feature, "isStatic")
    descriptor = None
    for klass in CompleteDSLPckg_Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExtensionPoint)


def test_completedslpckg_extensionpoint_constructor_exists():
    assert callable(CompleteDSLPckg_ExtensionPoint.__init__)


def test_completedslpckg_extensionpoint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_activityedge_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityEdge)


def test_completedslpckg_activityedge_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityEdge.__init__)


def test_completedslpckg_activityedge_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_instancevalue_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InstanceValue)


def test_completedslpckg_instancevalue_constructor_exists():
    assert callable(CompleteDSLPckg_InstanceValue.__init__)


def test_completedslpckg_instancevalue_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_literalstring_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralString)


def test_completedslpckg_literalstring_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralString.__init__)


def test_completedslpckg_literalstring_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_literalunilimitednatural_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralUnilimitedNatural)


def test_completedslpckg_literalunilimitednatural_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralUnilimitedNatural.__init__)


def test_completedslpckg_literalunilimitednatural_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralUnilimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_literalboolean_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralBoolean)


def test_completedslpckg_literalboolean_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralBoolean.__init__)


def test_completedslpckg_literalboolean_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_literalreal_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralReal)


def test_completedslpckg_literalreal_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralReal.__init__)


def test_completedslpckg_literalreal_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_literalinteger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralInteger)


def test_completedslpckg_literalinteger_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralInteger.__init__)


def test_completedslpckg_literalinteger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_literalnull_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralNull)


def test_completedslpckg_literalnull_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralNull.__init__)


def test_completedslpckg_literalnull_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_behavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Behavior)


def test_completedslpckg_behavior_constructor_exists():
    assert callable(CompleteDSLPckg_Behavior.__init__)


def test_completedslpckg_behavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_completedslpckg_behavior_has_isReentrant():
    assert hasattr(CompleteDSLPckg_Behavior, "isReentrant")
    descriptor = None
    for klass in CompleteDSLPckg_Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_duration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Duration)


def test_completedslpckg_duration_constructor_exists():
    assert callable(CompleteDSLPckg_Duration.__init__)


def test_completedslpckg_duration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Duration.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_timeexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TimeExpression)


def test_completedslpckg_timeexpression_constructor_exists():
    assert callable(CompleteDSLPckg_TimeExpression.__init__)


def test_completedslpckg_timeexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_literalspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LiteralSpecification)


def test_completedslpckg_literalspecification_constructor_exists():
    assert callable(CompleteDSLPckg_LiteralSpecification.__init__)


def test_completedslpckg_literalspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_interval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Interval)


def test_completedslpckg_interval_constructor_exists():
    assert callable(CompleteDSLPckg_Interval.__init__)


def test_completedslpckg_interval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Interval.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_OpaqueExpression)


def test_completedslpckg_opaqueexpression_constructor_exists():
    assert callable(CompleteDSLPckg_OpaqueExpression.__init__)


def test_completedslpckg_opaqueexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_completedslpckg_opaqueexpression_has_body():
    assert hasattr(CompleteDSLPckg_OpaqueExpression, "body")
    descriptor = None
    for klass in CompleteDSLPckg_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_opaqueexpression_has_language():
    assert hasattr(CompleteDSLPckg_OpaqueExpression, "language")
    descriptor = None
    for klass in CompleteDSLPckg_OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_expression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Expression)


def test_completedslpckg_expression_constructor_exists():
    assert callable(CompleteDSLPckg_Expression.__init__)


def test_completedslpckg_expression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_completedslpckg_expression_has_symbol():
    assert hasattr(CompleteDSLPckg_Expression, "symbol")
    descriptor = None
    for klass in CompleteDSLPckg_Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_parameter_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Parameter)


def test_completedslpckg_parameter_constructor_exists():
    assert callable(CompleteDSLPckg_Parameter.__init__)


def test_completedslpckg_parameter_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_completedslpckg_parameter_has_default():
    assert hasattr(CompleteDSLPckg_Parameter, "default")
    descriptor = None
    for klass in CompleteDSLPckg_Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_variable_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Variable)


def test_completedslpckg_variable_constructor_exists():
    assert callable(CompleteDSLPckg_Variable.__init__)


def test_completedslpckg_variable_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Variable.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_objectnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ObjectNode)


def test_completedslpckg_objectnode_constructor_exists():
    assert callable(CompleteDSLPckg_ObjectNode.__init__)


def test_completedslpckg_objectnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_pin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Pin)


def test_completedslpckg_pin_constructor_exists():
    assert callable(CompleteDSLPckg_Pin.__init__)


def test_completedslpckg_pin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Pin.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_connectableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ConnectableElement)


def test_completedslpckg_connectableelement_constructor_exists():
    assert callable(CompleteDSLPckg_ConnectableElement.__init__)


def test_completedslpckg_connectableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuralFeature)


def test_completedslpckg_structuralfeature_constructor_exists():
    assert callable(CompleteDSLPckg_StructuralFeature.__init__)


def test_completedslpckg_structuralfeature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_completedslpckg_structuralfeature_has_isReadOnly():
    assert hasattr(CompleteDSLPckg_StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in CompleteDSLPckg_StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_association_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Association)


def test_completedslpckg_association_constructor_exists():
    assert callable(CompleteDSLPckg_Association.__init__)


def test_completedslpckg_association_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_completedslpckg_association_has_isDerived():
    assert hasattr(CompleteDSLPckg_Association, "isDerived")
    descriptor = None
    for klass in CompleteDSLPckg_Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DirectedRelationship)


def test_completedslpckg_directedrelationship_constructor_exists():
    assert callable(CompleteDSLPckg_DirectedRelationship.__init__)


def test_completedslpckg_directedrelationship_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_instancespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InstanceSpecification)


def test_completedslpckg_instancespecification_constructor_exists():
    assert callable(CompleteDSLPckg_InstanceSpecification.__init__)


def test_completedslpckg_instancespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_generalizationset_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_GeneralizationSet)


def test_completedslpckg_generalizationset_constructor_exists():
    assert callable(CompleteDSLPckg_GeneralizationSet.__init__)


def test_completedslpckg_generalizationset_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"

def test_completedslpckg_generalizationset_has_isCovering():
    assert hasattr(CompleteDSLPckg_GeneralizationSet, "isCovering")
    descriptor = None
    for klass in CompleteDSLPckg_GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_generalizationset_has_isDisjoint():
    assert hasattr(CompleteDSLPckg_GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in CompleteDSLPckg_GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_observation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Observation)


def test_completedslpckg_observation_constructor_exists():
    assert callable(CompleteDSLPckg_Observation.__init__)


def test_completedslpckg_observation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Observation.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_type_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Type)


def test_completedslpckg_type_constructor_exists():
    assert callable(CompleteDSLPckg_Type.__init__)


def test_completedslpckg_type_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Type.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_event_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Event)


def test_completedslpckg_event_constructor_exists():
    assert callable(CompleteDSLPckg_Event.__init__)


def test_completedslpckg_event_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Event.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_valuespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ValueSpecification)


def test_completedslpckg_valuespecification_constructor_exists():
    assert callable(CompleteDSLPckg_ValueSpecification.__init__)


def test_completedslpckg_valuespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_state_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_State)


def test_completedslpckg_state_constructor_exists():
    assert callable(CompleteDSLPckg_State.__init__)


def test_completedslpckg_state_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_State.__init__)
    params = list(sig.parameters.keys())
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"

def test_completedslpckg_state_has_isOrthogonal():
    assert hasattr(CompleteDSLPckg_State, "isOrthogonal")
    descriptor = None
    for klass in CompleteDSLPckg_State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_state_has_isSimple():
    assert hasattr(CompleteDSLPckg_State, "isSimple")
    descriptor = None
    for klass in CompleteDSLPckg_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_state_has_isComposite():
    assert hasattr(CompleteDSLPckg_State, "isComposite")
    descriptor = None
    for klass in CompleteDSLPckg_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_state_has_isSubmachineState():
    assert hasattr(CompleteDSLPckg_State, "isSubmachineState")
    descriptor = None
    for klass in CompleteDSLPckg_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_classifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Classifier)


def test_completedslpckg_classifier_constructor_exists():
    assert callable(CompleteDSLPckg_Classifier.__init__)


def test_completedslpckg_classifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isFinalSpecialization" in params, "Missing parameter 'isFinalSpecialization'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_completedslpckg_classifier_has_isFinalSpecialization():
    assert hasattr(CompleteDSLPckg_Classifier, "isFinalSpecialization")
    descriptor = None
    for klass in CompleteDSLPckg_Classifier.__mro__:
        if "isFinalSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["isFinalSpecialization"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_classifier_has_isAbstract():
    assert hasattr(CompleteDSLPckg_Classifier, "isAbstract")
    descriptor = None
    for klass in CompleteDSLPckg_Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_region_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Region)


def test_completedslpckg_region_constructor_exists():
    assert callable(CompleteDSLPckg_Region.__init__)


def test_completedslpckg_region_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Region.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_transition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Transition)


def test_completedslpckg_transition_constructor_exists():
    assert callable(CompleteDSLPckg_Transition.__init__)


def test_completedslpckg_transition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_completedslpckg_transition_has_kind():
    assert hasattr(CompleteDSLPckg_Transition, "kind")
    descriptor = None
    for klass in CompleteDSLPckg_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionOperand)


def test_completedslpckg_interactionoperand_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionOperand.__init__)


def test_completedslpckg_interactionoperand_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_StructuredActivityNode)


def test_completedslpckg_structuredactivitynode_constructor_exists():
    assert callable(CompleteDSLPckg_StructuredActivityNode.__init__)


def test_completedslpckg_structuredactivitynode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_completedslpckg_structuredactivitynode_has_mustIsolate():
    assert hasattr(CompleteDSLPckg_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in CompleteDSLPckg_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_BehavioralFeature)


def test_completedslpckg_behavioralfeature_constructor_exists():
    assert callable(CompleteDSLPckg_BehavioralFeature.__init__)


def test_completedslpckg_behavioralfeature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_package_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Package)


def test_completedslpckg_package_constructor_exists():
    assert callable(CompleteDSLPckg_Package.__init__)


def test_completedslpckg_package_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Package.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"

def test_completedslpckg_package_has_URI():
    assert hasattr(CompleteDSLPckg_Package, "URI")
    descriptor = None
    for klass in CompleteDSLPckg_Package.__mro__:
        if "URI" in klass.__dict__:
            descriptor = klass.__dict__["URI"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_generalization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Generalization)


def test_completedslpckg_generalization_constructor_exists():
    assert callable(CompleteDSLPckg_Generalization.__init__)


def test_completedslpckg_generalization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_completedslpckg_generalization_has_isSubstitutable():
    assert hasattr(CompleteDSLPckg_Generalization, "isSubstitutable")
    descriptor = None
    for klass in CompleteDSLPckg_Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ProtocolConformance)


def test_completedslpckg_protocolconformance_constructor_exists():
    assert callable(CompleteDSLPckg_ProtocolConformance.__init__)


def test_completedslpckg_protocolconformance_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_packagemerge_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PackageMerge)


def test_completedslpckg_packagemerge_constructor_exists():
    assert callable(CompleteDSLPckg_PackageMerge.__init__)


def test_completedslpckg_packagemerge_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_constraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Constraint)


def test_completedslpckg_constraint_constructor_exists():
    assert callable(CompleteDSLPckg_Constraint.__init__)


def test_completedslpckg_constraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_packageimport_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PackageImport)


def test_completedslpckg_packageimport_constructor_exists():
    assert callable(CompleteDSLPckg_PackageImport.__init__)


def test_completedslpckg_packageimport_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_completedslpckg_packageimport_has_visibility():
    assert hasattr(CompleteDSLPckg_PackageImport, "visibility")
    descriptor = None
    for klass in CompleteDSLPckg_PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_elementimport_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ElementImport)


def test_completedslpckg_elementimport_constructor_exists():
    assert callable(CompleteDSLPckg_ElementImport.__init__)


def test_completedslpckg_elementimport_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_completedslpckg_elementimport_has_visibility():
    assert hasattr(CompleteDSLPckg_ElementImport, "visibility")
    descriptor = None
    for klass in CompleteDSLPckg_ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_elementimport_has_alias():
    assert hasattr(CompleteDSLPckg_ElementImport, "alias")
    descriptor = None
    for klass in CompleteDSLPckg_ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_dependency_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Dependency)


def test_completedslpckg_dependency_constructor_exists():
    assert callable(CompleteDSLPckg_Dependency.__init__)


def test_completedslpckg_dependency_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MultiplicityElement)


def test_completedslpckg_multiplicityelement_constructor_exists():
    assert callable(CompleteDSLPckg_MultiplicityElement.__init__)


def test_completedslpckg_multiplicityelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_completedslpckg_multiplicityelement_has_lower():
    assert hasattr(CompleteDSLPckg_MultiplicityElement, "lower")
    descriptor = None
    for klass in CompleteDSLPckg_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_multiplicityelement_has_isOrdered():
    assert hasattr(CompleteDSLPckg_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in CompleteDSLPckg_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_multiplicityelement_has_isUnique():
    assert hasattr(CompleteDSLPckg_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in CompleteDSLPckg_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_multiplicityelement_has_upper():
    assert hasattr(CompleteDSLPckg_MultiplicityElement, "upper")
    descriptor = None
    for klass in CompleteDSLPckg_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_slot_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Slot)


def test_completedslpckg_slot_constructor_exists():
    assert callable(CompleteDSLPckg_Slot.__init__)


def test_completedslpckg_slot_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Slot.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_linkenddata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_LinkEndData)


def test_completedslpckg_linkenddata_constructor_exists():
    assert callable(CompleteDSLPckg_LinkEndData.__init__)


def test_completedslpckg_linkenddata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_QualifierValue)


def test_completedslpckg_qualifiervalue_constructor_exists():
    assert callable(CompleteDSLPckg_QualifierValue.__init__)


def test_completedslpckg_qualifiervalue_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_clause_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Clause)


def test_completedslpckg_clause_constructor_exists():
    assert callable(CompleteDSLPckg_Clause.__init__)


def test_completedslpckg_clause_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Clause.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_relationship_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Relationship)


def test_completedslpckg_relationship_constructor_exists():
    assert callable(CompleteDSLPckg_Relationship.__init__)


def test_completedslpckg_relationship_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ExceptionHandler)


def test_completedslpckg_exceptionhandler_constructor_exists():
    assert callable(CompleteDSLPckg_ExceptionHandler.__init__)


def test_completedslpckg_exceptionhandler_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_namedelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_NamedElement)


def test_completedslpckg_namedelement_constructor_exists():
    assert callable(CompleteDSLPckg_NamedElement.__init__)


def test_completedslpckg_namedelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_completedslpckg_namedelement_has_qualifiedName():
    assert hasattr(CompleteDSLPckg_NamedElement, "qualifiedName")
    descriptor = None
    for klass in CompleteDSLPckg_NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_namedelement_has_visibility():
    assert hasattr(CompleteDSLPckg_NamedElement, "visibility")
    descriptor = None
    for klass in CompleteDSLPckg_NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_namedelement_has_name():
    assert hasattr(CompleteDSLPckg_NamedElement, "name")
    descriptor = None
    for klass in CompleteDSLPckg_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_comment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Comment)


def test_completedslpckg_comment_constructor_exists():
    assert callable(CompleteDSLPckg_Comment.__init__)


def test_completedslpckg_comment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_completedslpckg_comment_has_body():
    assert hasattr(CompleteDSLPckg_Comment, "body")
    descriptor = None
    for klass in CompleteDSLPckg_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_element_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Element)


def test_completedslpckg_element_constructor_exists():
    assert callable(CompleteDSLPckg_Element.__init__)


def test_completedslpckg_element_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Element.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_typedelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_TypedElement)


def test_completedslpckg_typedelement_constructor_exists():
    assert callable(CompleteDSLPckg_TypedElement.__init__)


def test_completedslpckg_typedelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_messageend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_MessageEnd)


def test_completedslpckg_messageend_constructor_exists():
    assert callable(CompleteDSLPckg_MessageEnd.__init__)


def test_completedslpckg_messageend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_message_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Message)


def test_completedslpckg_message_constructor_exists():
    assert callable(CompleteDSLPckg_Message.__init__)


def test_completedslpckg_message_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageKind" in params, "Missing parameter 'messageKind'"
    assert "messageSort" in params, "Missing parameter 'messageSort'"

def test_completedslpckg_message_has_messageKind():
    assert hasattr(CompleteDSLPckg_Message, "messageKind")
    descriptor = None
    for klass in CompleteDSLPckg_Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg_message_has_messageSort():
    assert hasattr(CompleteDSLPckg_Message, "messageSort")
    descriptor = None
    for klass in CompleteDSLPckg_Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_lifeline_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Lifeline)


def test_completedslpckg_lifeline_constructor_exists():
    assert callable(CompleteDSLPckg_Lifeline.__init__)


def test_completedslpckg_lifeline_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_generalordering_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_GeneralOrdering)


def test_completedslpckg_generalordering_constructor_exists():
    assert callable(CompleteDSLPckg_GeneralOrdering.__init__)


def test_completedslpckg_generalordering_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_component_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Component)


def test_completedslpckg_component_constructor_exists():
    assert callable(CompleteDSLPckg_Component.__init__)


def test_completedslpckg_component_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"

def test_completedslpckg_component_has_isIndirectlyInstantiated():
    assert hasattr(CompleteDSLPckg_Component, "isIndirectlyInstantiated")
    descriptor = None
    for klass in CompleteDSLPckg_Component.__mro__:
        if "isIndirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["isIndirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_namespace_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Namespace)


def test_completedslpckg_namespace_constructor_exists():
    assert callable(CompleteDSLPckg_Namespace.__init__)


def test_completedslpckg_namespace_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_collaborationuse_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_CollaborationUse)


def test_completedslpckg_collaborationuse_constructor_exists():
    assert callable(CompleteDSLPckg_CollaborationUse.__init__)


def test_completedslpckg_collaborationuse_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_vertex_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Vertex)


def test_completedslpckg_vertex_constructor_exists():
    assert callable(CompleteDSLPckg_Vertex.__init__)


def test_completedslpckg_vertex_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_RedefinableElement)


def test_completedslpckg_redefinableelement_constructor_exists():
    assert callable(CompleteDSLPckg_RedefinableElement.__init__)


def test_completedslpckg_redefinableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_completedslpckg_redefinableelement_has_isLeaf():
    assert hasattr(CompleteDSLPckg_RedefinableElement, "isLeaf")
    descriptor = None
    for klass in CompleteDSLPckg_RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_packageableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_PackageableElement)


def test_completedslpckg_packageableelement_constructor_exists():
    assert callable(CompleteDSLPckg_PackageableElement.__init__)


def test_completedslpckg_packageableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DeploymentTarget)


def test_completedslpckg_deploymenttarget_constructor_exists():
    assert callable(CompleteDSLPckg_DeploymentTarget.__init__)


def test_completedslpckg_deploymenttarget_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_parameterset_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ParameterSet)


def test_completedslpckg_parameterset_constructor_exists():
    assert callable(CompleteDSLPckg_ParameterSet.__init__)


def test_completedslpckg_parameterset_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_InteractionFragment)


def test_completedslpckg_interactionfragment_constructor_exists():
    assert callable(CompleteDSLPckg_InteractionFragment.__init__)


def test_completedslpckg_interactionfragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_DeployedArtifact)


def test_completedslpckg_deployedartifact_constructor_exists():
    assert callable(CompleteDSLPckg_DeployedArtifact.__init__)


def test_completedslpckg_deployedartifact_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_extend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Extend)


def test_completedslpckg_extend_constructor_exists():
    assert callable(CompleteDSLPckg_Extend.__init__)


def test_completedslpckg_extend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Extend.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_artifact_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Artifact)


def test_completedslpckg_artifact_constructor_exists():
    assert callable(CompleteDSLPckg_Artifact.__init__)


def test_completedslpckg_artifact_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_completedslpckg_artifact_has_fileName():
    assert hasattr(CompleteDSLPckg_Artifact, "fileName")
    descriptor = None
    for klass in CompleteDSLPckg_Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg_activitygroup_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityGroup)


def test_completedslpckg_activitygroup_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityGroup.__init__)


def test_completedslpckg_activitygroup_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_activitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_ActivityNode)


def test_completedslpckg_activitynode_constructor_exists():
    assert callable(CompleteDSLPckg_ActivityNode.__init__)


def test_completedslpckg_activitynode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_trigger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Trigger)


def test_completedslpckg_trigger_constructor_exists():
    assert callable(CompleteDSLPckg_Trigger.__init__)


def test_completedslpckg_trigger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_action_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Action)


def test_completedslpckg_action_constructor_exists():
    assert callable(CompleteDSLPckg_Action.__init__)


def test_completedslpckg_action_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Action.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg_include_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg_Include)


def test_completedslpckg_include_constructor_exists():
    assert callable(CompleteDSLPckg_Include.__init__)


def test_completedslpckg_include_constructor_args():
    sig = inspect.signature(CompleteDSLPckg_Include.__init__)
    params = list(sig.parameters.keys())

def test_interactionoperandkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperandKind is not None

def test_interactionoperandkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperandKind]
    expected_literals = [
        "neg",
        "par",
        "loop",
        "critical",
        "alt",
        "consider",
        "break_",
        "assert_",
        "opt",
        "seq",
        "strict",
        "ignore",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperandKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "external",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "public",
        "protected",
        "package",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "iterative",
        "parallel",
        "stream",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "create",
        "read",
        "update",
        "delete",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "none",
        "composite",
        "shared",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "asynchCall",
        "createMessage",
        "deleteMessage",
        "asynchSignal",
        "synchCall",
        "reply",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_connectorkind_exists():
    # Check that the Enumeration exists
    assert ConnectorKind is not None

def test_connectorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectorKind]
    expected_literals = [
        "delegation",
        "assembly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectorKind"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "LIFO",
        "FIFO",
        "unordered",
        "ordered",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

def test_callconcurrencyfeature_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyFeature is not None

def test_callconcurrencyfeature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyFeature]
    expected_literals = [
        "guarded",
        "concurrent",
        "sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyFeature"

def test_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "lost",
        "unknown",
        "complete",
        "found",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
ActivityNode_strategy = st.builds(
    ActivityNode,
)
Transition_strategy = st.builds(
    Transition,
)
CompleteDSLPckg_ProtocolTransition_strategy = st.builds(
    CompleteDSLPckg_ProtocolTransition,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
CompleteDSLPckg_ProtocolStateMachine_strategy = st.builds(
    CompleteDSLPckg_ProtocolStateMachine,
)
State_strategy = st.builds(
    State,
)
CompleteDSLPckg_FinalState_strategy = st.builds(
    CompleteDSLPckg_FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
CompleteDSLPckg_ConnectionPointReference_strategy = st.builds(
    CompleteDSLPckg_ConnectionPointReference,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
CompleteDSLPckg_RemoveVariableValueAction_strategy = st.builds(
    CompleteDSLPckg_RemoveVariableValueAction,
)
CompleteDSLPckg_AddVariableValueAction_strategy = st.builds(
    CompleteDSLPckg_AddVariableValueAction,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
CompleteDSLPckg_ClearVariableAction_strategy = st.builds(
    CompleteDSLPckg_ClearVariableAction,
)
CompleteDSLPckg_WriteVariableAction_strategy = st.builds(
    CompleteDSLPckg_WriteVariableAction,
)
CompleteDSLPckg_ReadVariableAction_strategy = st.builds(
    CompleteDSLPckg_ReadVariableAction,
)
CompleteDSLPckg_Pseudostate_strategy = st.builds(
    CompleteDSLPckg_Pseudostate,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
CompleteDSLPckg_CreateLinkObjectAction_strategy = st.builds(
    CompleteDSLPckg_CreateLinkObjectAction,
)
CompleteDSLPckg_ReadlsClassifiedObjectAction_strategy = st.builds(
    CompleteDSLPckg_ReadlsClassifiedObjectAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
CompleteDSLPckg_AcceptCallAction_strategy = st.builds(
    CompleteDSLPckg_AcceptCallAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
CompleteDSLPckg_WriteLinkAction_strategy = st.builds(
    CompleteDSLPckg_WriteLinkAction,
)
CompleteDSLPckg_ReadLinkAction_strategy = st.builds(
    CompleteDSLPckg_ReadLinkAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
CompleteDSLPckg_RemoveStructuralFeatureValueAction_strategy = st.builds(
    CompleteDSLPckg_RemoveStructuralFeatureValueAction,
)
CompleteDSLPckg_AddStructuralFeatureValueAction_strategy = st.builds(
    CompleteDSLPckg_AddStructuralFeatureValueAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
CompleteDSLPckg_LinkEndDestructionData_strategy = st.builds(
    CompleteDSLPckg_LinkEndDestructionData,
    isDestroyDuplicates=
        st.booleans()
)
CompleteDSLPckg_LinkEndCreationData_strategy = st.builds(
    CompleteDSLPckg_LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
CompleteDSLPckg_ConsiderIgnoreFragment_strategy = st.builds(
    CompleteDSLPckg_ConsiderIgnoreFragment,
)
CompleteDSLPckg_CombinedFragment_strategy = st.builds(
    CompleteDSLPckg_CombinedFragment,
    interactionOperator=
        safe_text
)
CompleteDSLPckg_PartDecomposition_strategy = st.builds(
    CompleteDSLPckg_PartDecomposition,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
CompleteDSLPckg_ActionExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg_ActionExecutionSpecification,
)
CompleteDSLPckg_BehaviorExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg_BehaviorExecutionSpecification,
)
MessageOccurrenceSpecification_strategy = st.builds(
    MessageOccurrenceSpecification,
)
CompleteDSLPckg_DestructionOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg_DestructionOccurrenceSpecification,
)
OccurenceSpecification_strategy = st.builds(
    OccurenceSpecification,
)
CompleteDSLPckg_MessageOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg_MessageOccurrenceSpecification,
)
CompleteDSLPckg_ExecutionOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg_ExecutionOccurrenceSpecification,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
CompleteDSLPckg_Continuation_strategy = st.builds(
    CompleteDSLPckg_Continuation,
    setting=
        st.booleans()
)
CompleteDSLPckg_InteractionUse_strategy = st.builds(
    CompleteDSLPckg_InteractionUse,
)
CompleteDSLPckg_OccurenceSpecification_strategy = st.builds(
    CompleteDSLPckg_OccurenceSpecification,
)
CompleteDSLPckg_StateInvariant_strategy = st.builds(
    CompleteDSLPckg_StateInvariant,
)
CompleteDSLPckg_ExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg_ExecutionSpecification,
)
CompleteDSLPckg_Gate_strategy = st.builds(
    CompleteDSLPckg_Gate,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
CompleteDSLPckg_DataStoreNode_strategy = st.builds(
    CompleteDSLPckg_DataStoreNode,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
CompleteDSLPckg_ConditionalNode_strategy = st.builds(
    CompleteDSLPckg_ConditionalNode,
    isDeterminate=
        st.booleans(),
    isAssumed=
        st.booleans()
)
CompleteDSLPckg_ExpansionRegion_strategy = st.builds(
    CompleteDSLPckg_ExpansionRegion,
    mode=
        safe_text
)
CompleteDSLPckg_SequenceNode_strategy = st.builds(
    CompleteDSLPckg_SequenceNode,
)
CompleteDSLPckg_LoopNode_strategy = st.builds(
    CompleteDSLPckg_LoopNode,
    isTestedFirst=
        st.booleans()
)
CompleteDSLPckg_ExecutableNode_strategy = st.builds(
    CompleteDSLPckg_ExecutableNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
CompleteDSLPckg_ObjectFlow_strategy = st.builds(
    CompleteDSLPckg_ObjectFlow,
    ordering=
        safe_text,
    isControlType=
        st.booleans(),
    isMultireceive=
        st.booleans(),
    isMulticast=
        st.booleans()
)
CompleteDSLPckg_ControlFlow_strategy = st.builds(
    CompleteDSLPckg_ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
CompleteDSLPckg_InterruptibleActivityRegion_strategy = st.builds(
    CompleteDSLPckg_InterruptibleActivityRegion,
)
CompleteDSLPckg_ActivityPartition_strategy = st.builds(
    CompleteDSLPckg_ActivityPartition,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
CompleteDSLPckg_FlowFinalNode_strategy = st.builds(
    CompleteDSLPckg_FlowFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
CompleteDSLPckg_JoinNode_strategy = st.builds(
    CompleteDSLPckg_JoinNode,
    isCombineDuplicate=
        st.booleans()
)
CompleteDSLPckg_DecisionNode_strategy = st.builds(
    CompleteDSLPckg_DecisionNode,
)
CompleteDSLPckg_FinalNode_strategy = st.builds(
    CompleteDSLPckg_FinalNode,
)
CompleteDSLPckg_ForkNode_strategy = st.builds(
    CompleteDSLPckg_ForkNode,
)
CompleteDSLPckg_InitialNode_strategy = st.builds(
    CompleteDSLPckg_InitialNode,
)
CompleteDSLPckg_MergeNode_strategy = st.builds(
    CompleteDSLPckg_MergeNode,
)
CompleteDSLPckg_ActivityFinalNode_strategy = st.builds(
    CompleteDSLPckg_ActivityFinalNode,
)
CompleteDSLPckg_ControlNode_strategy = st.builds(
    CompleteDSLPckg_ControlNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
CompleteDSLPckg_ExpansionNode_strategy = st.builds(
    CompleteDSLPckg_ExpansionNode,
)
CompleteDSLPckg_CentralBufferNode_strategy = st.builds(
    CompleteDSLPckg_CentralBufferNode,
)
CompleteDSLPckg_ActivityParameterNode_strategy = st.builds(
    CompleteDSLPckg_ActivityParameterNode,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
CompleteDSLPckg_DestroyLinkAction_strategy = st.builds(
    CompleteDSLPckg_DestroyLinkAction,
)
CompleteDSLPckg_CreateLinkAction_strategy = st.builds(
    CompleteDSLPckg_CreateLinkAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
CompleteDSLPckg_ClearStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_ClearStructuralFeatureAction,
)
CompleteDSLPckg_WriteStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_WriteStructuralFeatureAction,
)
CompleteDSLPckg_ReadStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_ReadStructuralFeatureAction,
)
CompleteDSLPckg_CallOperationAction_strategy = st.builds(
    CompleteDSLPckg_CallOperationAction,
)
CallAction_strategy = st.builds(
    CallAction,
)
CompleteDSLPckg_StartObjectBehaviorAction_strategy = st.builds(
    CompleteDSLPckg_StartObjectBehaviorAction,
)
CompleteDSLPckg_CallBehaviorAction_strategy = st.builds(
    CompleteDSLPckg_CallBehaviorAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
CompleteDSLPckg_SendSignalAction_strategy = st.builds(
    CompleteDSLPckg_SendSignalAction,
)
CompleteDSLPckg_BroadcastSignalAction_strategy = st.builds(
    CompleteDSLPckg_BroadcastSignalAction,
)
CompleteDSLPckg_CallAction_strategy = st.builds(
    CompleteDSLPckg_CallAction,
    isSynchronous=
        st.booleans()
)
InputPin_strategy = st.builds(
    InputPin,
)
CompleteDSLPckg_ActionInputPin_strategy = st.builds(
    CompleteDSLPckg_ActionInputPin,
)
CompleteDSLPckg_ValuePin_strategy = st.builds(
    CompleteDSLPckg_ValuePin,
)
Pin_strategy = st.builds(
    Pin,
)
Action_strategy = st.builds(
    Action,
)
CompleteDSLPckg_DestroyObjectAction_strategy = st.builds(
    CompleteDSLPckg_DestroyObjectAction,
)
CompleteDSLPckg_ReclassifyObjectAction_strategy = st.builds(
    CompleteDSLPckg_ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
CompleteDSLPckg_TestIdentityAction_strategy = st.builds(
    CompleteDSLPckg_TestIdentityAction,
)
CompleteDSLPckg_ReadSelfAction_strategy = st.builds(
    CompleteDSLPckg_ReadSelfAction,
)
CompleteDSLPckg_ValueSpecificationAction_strategy = st.builds(
    CompleteDSLPckg_ValueSpecificationAction,
)
CompleteDSLPckg_VariableAction_strategy = st.builds(
    CompleteDSLPckg_VariableAction,
)
CompleteDSLPckg_ReduceAction_strategy = st.builds(
    CompleteDSLPckg_ReduceAction,
    isOrdered=
        st.booleans()
)
CompleteDSLPckg_StructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg_StructuralFeatureAction,
)
CompleteDSLPckg_ReadLinkObjectEndAction_strategy = st.builds(
    CompleteDSLPckg_ReadLinkObjectEndAction,
)
CompleteDSLPckg_RaiseExceptionAction_strategy = st.builds(
    CompleteDSLPckg_RaiseExceptionAction,
)
CompleteDSLPckg_ReplyAction_strategy = st.builds(
    CompleteDSLPckg_ReplyAction,
)
CompleteDSLPckg_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    CompleteDSLPckg_ReadLinkObjectEndQualifierAction,
)
CompleteDSLPckg_CreateObjectAction_strategy = st.builds(
    CompleteDSLPckg_CreateObjectAction,
)
CompleteDSLPckg_StartClassifierBehaviorAction_strategy = st.builds(
    CompleteDSLPckg_StartClassifierBehaviorAction,
)
CompleteDSLPckg_LinkAction_strategy = st.builds(
    CompleteDSLPckg_LinkAction,
)
CompleteDSLPckg_UnmarshallAction_strategy = st.builds(
    CompleteDSLPckg_UnmarshallAction,
)
CompleteDSLPckg_AcceptEventAction_strategy = st.builds(
    CompleteDSLPckg_AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
CompleteDSLPckg_ReadExtendAction_strategy = st.builds(
    CompleteDSLPckg_ReadExtendAction,
)
CompleteDSLPckg_OpaqueAction_strategy = st.builds(
    CompleteDSLPckg_OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
CompleteDSLPckg_SendObjectAction_strategy = st.builds(
    CompleteDSLPckg_SendObjectAction,
)
CompleteDSLPckg_InputPin_strategy = st.builds(
    CompleteDSLPckg_InputPin,
)
Artifact_strategy = st.builds(
    Artifact,
)
CompleteDSLPckg_DeploymentSpecification_strategy = st.builds(
    CompleteDSLPckg_DeploymentSpecification,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
CompleteDSLPckg_ExecutionEnvironment_strategy = st.builds(
    CompleteDSLPckg_ExecutionEnvironment,
)
CompleteDSLPckg_Device_strategy = st.builds(
    CompleteDSLPckg_Device,
)
CompleteDSLPckg_OutputPin_strategy = st.builds(
    CompleteDSLPckg_OutputPin,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
CompleteDSLPckg_InvocationAction_strategy = st.builds(
    CompleteDSLPckg_InvocationAction,
)
CompleteDSLPckg_ConnectorEnd_strategy = st.builds(
    CompleteDSLPckg_ConnectorEnd,
)
Property_strategy = st.builds(
    Property,
)
CompleteDSLPckg_Port_strategy = st.builds(
    CompleteDSLPckg_Port,
    isConjugated=
        st.booleans(),
    isBehavior=
        st.booleans(),
    isService=
        st.booleans()
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
CompleteDSLPckg_DurationConstraint_strategy = st.builds(
    CompleteDSLPckg_DurationConstraint,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg_TimeConstraint_strategy = st.builds(
    CompleteDSLPckg_TimeConstraint,
    firstEvent=
        st.booleans()
)
Constraint_strategy = st.builds(
    Constraint,
)
CompleteDSLPckg_InteractionConstraint_strategy = st.builds(
    CompleteDSLPckg_InteractionConstraint,
)
CompleteDSLPckg_IntervalConstraint_strategy = st.builds(
    CompleteDSLPckg_IntervalConstraint,
)
Interval_strategy = st.builds(
    Interval,
)
CompleteDSLPckg_DurationInterval_strategy = st.builds(
    CompleteDSLPckg_DurationInterval,
)
CompleteDSLPckg_TimeInterval_strategy = st.builds(
    CompleteDSLPckg_TimeInterval,
)
Observation_strategy = st.builds(
    Observation,
)
CompleteDSLPckg_DurationObservation_strategy = st.builds(
    CompleteDSLPckg_DurationObservation,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg_TimeObservation_strategy = st.builds(
    CompleteDSLPckg_TimeObservation,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg_TimeEvent_strategy = st.builds(
    CompleteDSLPckg_TimeEvent,
    isRelative=
        st.booleans()
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
CompleteDSLPckg_SignalEvent_strategy = st.builds(
    CompleteDSLPckg_SignalEvent,
)
CompleteDSLPckg_CallEvent_strategy = st.builds(
    CompleteDSLPckg_CallEvent,
)
CompleteDSLPckg_AnyReceiveEvent_strategy = st.builds(
    CompleteDSLPckg_AnyReceiveEvent,
)
Event_strategy = st.builds(
    Event,
)
CompleteDSLPckg_ChangeEvent_strategy = st.builds(
    CompleteDSLPckg_ChangeEvent,
)
CompleteDSLPckg_MessageEvent_strategy = st.builds(
    CompleteDSLPckg_MessageEvent,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
CompleteDSLPckg_FunctionBehavior_strategy = st.builds(
    CompleteDSLPckg_FunctionBehavior,
)
Behavior_strategy = st.builds(
    Behavior,
)
CompleteDSLPckg_Interaction_strategy = st.builds(
    CompleteDSLPckg_Interaction,
)
CompleteDSLPckg_StateMachine_strategy = st.builds(
    CompleteDSLPckg_StateMachine,
)
CompleteDSLPckg_Activity_strategy = st.builds(
    CompleteDSLPckg_Activity,
    isSingleExecution=
        st.booleans(),
    isReadOnly=
        st.booleans()
)
CompleteDSLPckg_OpaqueBehavior_strategy = st.builds(
    CompleteDSLPckg_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
CompleteDSLPckg_CommunicationPath_strategy = st.builds(
    CompleteDSLPckg_CommunicationPath,
)
Class_strategy = st.builds(
    Class,
)
CompleteDSLPckg_AssociationClass_strategy = st.builds(
    CompleteDSLPckg_AssociationClass,
)
Realization_strategy = st.builds(
    Realization,
)
CompleteDSLPckg_InterfaceRealization_strategy = st.builds(
    CompleteDSLPckg_InterfaceRealization,
)
CompleteDSLPckg_ComponentRealization_strategy = st.builds(
    CompleteDSLPckg_ComponentRealization,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
CompleteDSLPckg_Manifestation_strategy = st.builds(
    CompleteDSLPckg_Manifestation,
)
CompleteDSLPckg_Realization_strategy = st.builds(
    CompleteDSLPckg_Realization,
)
Dependency_strategy = st.builds(
    Dependency,
)
CompleteDSLPckg_Abstraction_strategy = st.builds(
    CompleteDSLPckg_Abstraction,
)
CompleteDSLPckg_Deployment_strategy = st.builds(
    CompleteDSLPckg_Deployment,
)
CompleteDSLPckg_Usage_strategy = st.builds(
    CompleteDSLPckg_Usage,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
CompleteDSLPckg_EnumerationLiteral_strategy = st.builds(
    CompleteDSLPckg_EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
CompleteDSLPckg_Enumeration_strategy = st.builds(
    CompleteDSLPckg_Enumeration,
)
CompleteDSLPckg_PrimitiveType_strategy = st.builds(
    CompleteDSLPckg_PrimitiveType,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
CompleteDSLPckg_EncapsulatedClassifier_strategy = st.builds(
    CompleteDSLPckg_EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
CompleteDSLPckg_UseCase_strategy = st.builds(
    CompleteDSLPckg_UseCase,
)
CompleteDSLPckg_Actor_strategy = st.builds(
    CompleteDSLPckg_Actor,
)
CompleteDSLPckg_Collaboration_strategy = st.builds(
    CompleteDSLPckg_Collaboration,
)
Classifier_strategy = st.builds(
    Classifier,
)
CompleteDSLPckg_Signal_strategy = st.builds(
    CompleteDSLPckg_Signal,
)
CompleteDSLPckg_StructuredClassifier_strategy = st.builds(
    CompleteDSLPckg_StructuredClassifier,
)
CompleteDSLPckg_BehavioredClassifier_strategy = st.builds(
    CompleteDSLPckg_BehavioredClassifier,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
CompleteDSLPckg_Reception_strategy = st.builds(
    CompleteDSLPckg_Reception,
)
CompleteDSLPckg_Operation_strategy = st.builds(
    CompleteDSLPckg_Operation,
    upper=
        st.integers(),
    isUnique=
        st.booleans(),
    isOrdered=
        st.booleans(),
    lower=
        st.integers(),
    isQuery=
        st.booleans()
)
CompleteDSLPckg_Interface_strategy = st.builds(
    CompleteDSLPckg_Interface,
)
CompleteDSLPckg_DataType_strategy = st.builds(
    CompleteDSLPckg_DataType,
)
CompleteDSLPckg_Class_strategy = st.builds(
    CompleteDSLPckg_Class,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
CompleteDSLPckg_Node_strategy = st.builds(
    CompleteDSLPckg_Node,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
Feature_strategy = st.builds(
    Feature,
)
CompleteDSLPckg_Connector_strategy = st.builds(
    CompleteDSLPckg_Connector,
    kind=
        safe_text
)
CompleteDSLPckg_Substitution_strategy = st.builds(
    CompleteDSLPckg_Substitution,
)
CompleteDSLPckg_Property_strategy = st.builds(
    CompleteDSLPckg_Property,
    isID=
        st.booleans(),
    isComposite=
        st.booleans(),
    isDerivedUnion=
        st.booleans(),
    isDerived=
        st.booleans(),
    aggregation=
        safe_text,
    default=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
CompleteDSLPckg_Feature_strategy = st.builds(
    CompleteDSLPckg_Feature,
    isStatic=
        st.booleans()
)
CompleteDSLPckg_ExtensionPoint_strategy = st.builds(
    CompleteDSLPckg_ExtensionPoint,
)
CompleteDSLPckg_ActivityEdge_strategy = st.builds(
    CompleteDSLPckg_ActivityEdge,
)
CompleteDSLPckg_InstanceValue_strategy = st.builds(
    CompleteDSLPckg_InstanceValue,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
CompleteDSLPckg_LiteralString_strategy = st.builds(
    CompleteDSLPckg_LiteralString,
)
CompleteDSLPckg_LiteralUnilimitedNatural_strategy = st.builds(
    CompleteDSLPckg_LiteralUnilimitedNatural,
)
CompleteDSLPckg_LiteralBoolean_strategy = st.builds(
    CompleteDSLPckg_LiteralBoolean,
)
CompleteDSLPckg_LiteralReal_strategy = st.builds(
    CompleteDSLPckg_LiteralReal,
)
CompleteDSLPckg_LiteralInteger_strategy = st.builds(
    CompleteDSLPckg_LiteralInteger,
)
CompleteDSLPckg_LiteralNull_strategy = st.builds(
    CompleteDSLPckg_LiteralNull,
)
CompleteDSLPckg_Behavior_strategy = st.builds(
    CompleteDSLPckg_Behavior,
    isReentrant=
        st.booleans()
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
CompleteDSLPckg_Duration_strategy = st.builds(
    CompleteDSLPckg_Duration,
)
CompleteDSLPckg_TimeExpression_strategy = st.builds(
    CompleteDSLPckg_TimeExpression,
)
CompleteDSLPckg_LiteralSpecification_strategy = st.builds(
    CompleteDSLPckg_LiteralSpecification,
)
CompleteDSLPckg_Interval_strategy = st.builds(
    CompleteDSLPckg_Interval,
)
CompleteDSLPckg_OpaqueExpression_strategy = st.builds(
    CompleteDSLPckg_OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
CompleteDSLPckg_Expression_strategy = st.builds(
    CompleteDSLPckg_Expression,
    symbol=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
CompleteDSLPckg_Parameter_strategy = st.builds(
    CompleteDSLPckg_Parameter,
    default=
        safe_text
)
CompleteDSLPckg_Variable_strategy = st.builds(
    CompleteDSLPckg_Variable,
)
CompleteDSLPckg_ObjectNode_strategy = st.builds(
    CompleteDSLPckg_ObjectNode,
)
CompleteDSLPckg_Pin_strategy = st.builds(
    CompleteDSLPckg_Pin,
)
CompleteDSLPckg_ConnectableElement_strategy = st.builds(
    CompleteDSLPckg_ConnectableElement,
)
CompleteDSLPckg_StructuralFeature_strategy = st.builds(
    CompleteDSLPckg_StructuralFeature,
    isReadOnly=
        st.booleans()
)
Relationship_strategy = st.builds(
    Relationship,
)
CompleteDSLPckg_Association_strategy = st.builds(
    CompleteDSLPckg_Association,
    isDerived=
        st.booleans()
)
CompleteDSLPckg_DirectedRelationship_strategy = st.builds(
    CompleteDSLPckg_DirectedRelationship,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
CompleteDSLPckg_InstanceSpecification_strategy = st.builds(
    CompleteDSLPckg_InstanceSpecification,
)
CompleteDSLPckg_GeneralizationSet_strategy = st.builds(
    CompleteDSLPckg_GeneralizationSet,
    isCovering=
        st.booleans(),
    isDisjoint=
        st.booleans()
)
CompleteDSLPckg_Observation_strategy = st.builds(
    CompleteDSLPckg_Observation,
)
CompleteDSLPckg_Type_strategy = st.builds(
    CompleteDSLPckg_Type,
)
CompleteDSLPckg_Event_strategy = st.builds(
    CompleteDSLPckg_Event,
)
CompleteDSLPckg_ValueSpecification_strategy = st.builds(
    CompleteDSLPckg_ValueSpecification,
)
Namespace_strategy = st.builds(
    Namespace,
)
CompleteDSLPckg_State_strategy = st.builds(
    CompleteDSLPckg_State,
    isOrthogonal=
        st.booleans(),
    isSimple=
        st.booleans(),
    isComposite=
        st.booleans(),
    isSubmachineState=
        st.booleans()
)
CompleteDSLPckg_Classifier_strategy = st.builds(
    CompleteDSLPckg_Classifier,
    isFinalSpecialization=
        st.booleans(),
    isAbstract=
        st.booleans()
)
CompleteDSLPckg_Region_strategy = st.builds(
    CompleteDSLPckg_Region,
)
CompleteDSLPckg_Transition_strategy = st.builds(
    CompleteDSLPckg_Transition,
    kind=
        safe_text
)
CompleteDSLPckg_InteractionOperand_strategy = st.builds(
    CompleteDSLPckg_InteractionOperand,
)
CompleteDSLPckg_StructuredActivityNode_strategy = st.builds(
    CompleteDSLPckg_StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
CompleteDSLPckg_BehavioralFeature_strategy = st.builds(
    CompleteDSLPckg_BehavioralFeature,
)
CompleteDSLPckg_Package_strategy = st.builds(
    CompleteDSLPckg_Package,
    URI=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
CompleteDSLPckg_Generalization_strategy = st.builds(
    CompleteDSLPckg_Generalization,
    isSubstitutable=
        st.booleans()
)
CompleteDSLPckg_ProtocolConformance_strategy = st.builds(
    CompleteDSLPckg_ProtocolConformance,
)
CompleteDSLPckg_PackageMerge_strategy = st.builds(
    CompleteDSLPckg_PackageMerge,
)
CompleteDSLPckg_Constraint_strategy = st.builds(
    CompleteDSLPckg_Constraint,
)
CompleteDSLPckg_PackageImport_strategy = st.builds(
    CompleteDSLPckg_PackageImport,
    visibility=
        safe_text
)
CompleteDSLPckg_ElementImport_strategy = st.builds(
    CompleteDSLPckg_ElementImport,
    visibility=
        safe_text,
    alias=
        safe_text
)
CompleteDSLPckg_Dependency_strategy = st.builds(
    CompleteDSLPckg_Dependency,
)
Element_strategy = st.builds(
    Element,
)
CompleteDSLPckg_MultiplicityElement_strategy = st.builds(
    CompleteDSLPckg_MultiplicityElement,
    lower=
        st.integers(),
    isOrdered=
        st.booleans(),
    isUnique=
        st.booleans(),
    upper=
        st.integers()
)
CompleteDSLPckg_Slot_strategy = st.builds(
    CompleteDSLPckg_Slot,
)
CompleteDSLPckg_LinkEndData_strategy = st.builds(
    CompleteDSLPckg_LinkEndData,
)
CompleteDSLPckg_QualifierValue_strategy = st.builds(
    CompleteDSLPckg_QualifierValue,
)
CompleteDSLPckg_Clause_strategy = st.builds(
    CompleteDSLPckg_Clause,
)
CompleteDSLPckg_Relationship_strategy = st.builds(
    CompleteDSLPckg_Relationship,
)
CompleteDSLPckg_ExceptionHandler_strategy = st.builds(
    CompleteDSLPckg_ExceptionHandler,
)
CompleteDSLPckg_NamedElement_strategy = st.builds(
    CompleteDSLPckg_NamedElement,
    qualifiedName=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
CompleteDSLPckg_Comment_strategy = st.builds(
    CompleteDSLPckg_Comment,
    body=
        safe_text
)
CompleteDSLPckg_Element_strategy = st.builds(
    CompleteDSLPckg_Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
CompleteDSLPckg_TypedElement_strategy = st.builds(
    CompleteDSLPckg_TypedElement,
)
CompleteDSLPckg_MessageEnd_strategy = st.builds(
    CompleteDSLPckg_MessageEnd,
)
CompleteDSLPckg_Message_strategy = st.builds(
    CompleteDSLPckg_Message,
    messageKind=
        safe_text,
    messageSort=
        safe_text
)
CompleteDSLPckg_Lifeline_strategy = st.builds(
    CompleteDSLPckg_Lifeline,
)
CompleteDSLPckg_GeneralOrdering_strategy = st.builds(
    CompleteDSLPckg_GeneralOrdering,
)
CompleteDSLPckg_Component_strategy = st.builds(
    CompleteDSLPckg_Component,
    isIndirectlyInstantiated=
        st.booleans()
)
CompleteDSLPckg_Namespace_strategy = st.builds(
    CompleteDSLPckg_Namespace,
)
CompleteDSLPckg_CollaborationUse_strategy = st.builds(
    CompleteDSLPckg_CollaborationUse,
)
CompleteDSLPckg_Vertex_strategy = st.builds(
    CompleteDSLPckg_Vertex,
)
CompleteDSLPckg_RedefinableElement_strategy = st.builds(
    CompleteDSLPckg_RedefinableElement,
    isLeaf=
        st.booleans()
)
CompleteDSLPckg_PackageableElement_strategy = st.builds(
    CompleteDSLPckg_PackageableElement,
)
CompleteDSLPckg_DeploymentTarget_strategy = st.builds(
    CompleteDSLPckg_DeploymentTarget,
)
CompleteDSLPckg_ParameterSet_strategy = st.builds(
    CompleteDSLPckg_ParameterSet,
)
CompleteDSLPckg_InteractionFragment_strategy = st.builds(
    CompleteDSLPckg_InteractionFragment,
)
CompleteDSLPckg_DeployedArtifact_strategy = st.builds(
    CompleteDSLPckg_DeployedArtifact,
)
CompleteDSLPckg_Extend_strategy = st.builds(
    CompleteDSLPckg_Extend,
)
CompleteDSLPckg_Artifact_strategy = st.builds(
    CompleteDSLPckg_Artifact,
    fileName=
        safe_text
)
CompleteDSLPckg_ActivityGroup_strategy = st.builds(
    CompleteDSLPckg_ActivityGroup,
)
CompleteDSLPckg_ActivityNode_strategy = st.builds(
    CompleteDSLPckg_ActivityNode,
)
CompleteDSLPckg_Trigger_strategy = st.builds(
    CompleteDSLPckg_Trigger,
)
CompleteDSLPckg_Action_strategy = st.builds(
    CompleteDSLPckg_Action,
)
CompleteDSLPckg_Include_strategy = st.builds(
    CompleteDSLPckg_Include,
)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=CompleteDSLPckg_ProtocolTransition_strategy)
@settings(max_examples=50)
def test_completedslpckg_protocoltransition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ProtocolTransition)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=CompleteDSLPckg_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_completedslpckg_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ProtocolStateMachine)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=CompleteDSLPckg_FinalState_strategy)
@settings(max_examples=50)
def test_completedslpckg_finalstate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FinalState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=CompleteDSLPckg_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_completedslpckg_connectionpointreference_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConnectionPointReference)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=CompleteDSLPckg_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RemoveVariableValueAction)

@given(instance=CompleteDSLPckg_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AddVariableValueAction)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=CompleteDSLPckg_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_clearvariableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ClearVariableAction)

@given(instance=CompleteDSLPckg_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_writevariableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_WriteVariableAction)

@given(instance=CompleteDSLPckg_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readvariableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadVariableAction)

@given(instance=CompleteDSLPckg_Pseudostate_strategy)
@settings(max_examples=50)
def test_completedslpckg_pseudostate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Pseudostate)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=CompleteDSLPckg_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CreateLinkObjectAction)

@given(instance=CompleteDSLPckg_ReadlsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readlsclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadlsClassifiedObjectAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=CompleteDSLPckg_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_acceptcallaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AcceptCallAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=CompleteDSLPckg_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_writelinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_WriteLinkAction)

@given(instance=CompleteDSLPckg_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readlinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadLinkAction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=CompleteDSLPckg_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RemoveStructuralFeatureValueAction)

@given(instance=CompleteDSLPckg_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AddStructuralFeatureValueAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=CompleteDSLPckg_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_completedslpckg_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkEndDestructionData)



@given(instance=CompleteDSLPckg_LinkEndDestructionData_strategy)
def test_completedslpckg_linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=CompleteDSLPckg_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_completedslpckg_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkEndCreationData)



@given(instance=CompleteDSLPckg_LinkEndCreationData_strategy)
def test_completedslpckg_linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=InteractionUse_strategy)
@settings(max_examples=50)
def test_interactionuse_instantiation(instance):
    assert isinstance(instance, InteractionUse)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=CombinedFragment_strategy)
@settings(max_examples=50)
def test_combinedfragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)

@given(instance=CompleteDSLPckg_ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_completedslpckg_considerignorefragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConsiderIgnoreFragment)

@given(instance=CompleteDSLPckg_CombinedFragment_strategy)
@settings(max_examples=50)
def test_completedslpckg_combinedfragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CombinedFragment)



@given(instance=CompleteDSLPckg_CombinedFragment_strategy)
def test_completedslpckg_combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=CompleteDSLPckg_PartDecomposition_strategy)
@settings(max_examples=50)
def test_completedslpckg_partdecomposition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PartDecomposition)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=CompleteDSLPckg_ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActionExecutionSpecification)

@given(instance=CompleteDSLPckg_BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BehaviorExecutionSpecification)

@given(instance=MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, MessageOccurrenceSpecification)

@given(instance=CompleteDSLPckg_DestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_destructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DestructionOccurrenceSpecification)

@given(instance=OccurenceSpecification_strategy)
@settings(max_examples=50)
def test_occurencespecification_instantiation(instance):
    assert isinstance(instance, OccurenceSpecification)

@given(instance=CompleteDSLPckg_MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MessageOccurrenceSpecification)

@given(instance=CompleteDSLPckg_ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutionOccurrenceSpecification)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=CompleteDSLPckg_Continuation_strategy)
@settings(max_examples=50)
def test_completedslpckg_continuation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Continuation)



@given(instance=CompleteDSLPckg_Continuation_strategy)
def test_completedslpckg_continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=CompleteDSLPckg_InteractionUse_strategy)
@settings(max_examples=50)
def test_completedslpckg_interactionuse_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionUse)

@given(instance=CompleteDSLPckg_OccurenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_occurencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OccurenceSpecification)

@given(instance=CompleteDSLPckg_StateInvariant_strategy)
@settings(max_examples=50)
def test_completedslpckg_stateinvariant_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StateInvariant)

@given(instance=CompleteDSLPckg_ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_executionspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutionSpecification)

@given(instance=CompleteDSLPckg_Gate_strategy)
@settings(max_examples=50)
def test_completedslpckg_gate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Gate)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=CompleteDSLPckg_DataStoreNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_datastorenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DataStoreNode)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=CompleteDSLPckg_ConditionalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_conditionalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConditionalNode)



@given(instance=CompleteDSLPckg_ConditionalNode_strategy)
def test_completedslpckg_conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original



@given(instance=CompleteDSLPckg_ConditionalNode_strategy)
def test_completedslpckg_conditionalnode_isAssumed_setter(instance):
    original = instance.isAssumed
    instance.isAssumed = original
    assert instance.isAssumed == original

@given(instance=CompleteDSLPckg_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_completedslpckg_expansionregion_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExpansionRegion)



@given(instance=CompleteDSLPckg_ExpansionRegion_strategy)
def test_completedslpckg_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=CompleteDSLPckg_SequenceNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_sequencenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SequenceNode)

@given(instance=CompleteDSLPckg_LoopNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_loopnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LoopNode)



@given(instance=CompleteDSLPckg_LoopNode_strategy)
def test_completedslpckg_loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=CompleteDSLPckg_ExecutableNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_executablenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutableNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
@settings(max_examples=50)
def test_completedslpckg_objectflow_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ObjectFlow)



@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_completedslpckg_objectflow_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_completedslpckg_objectflow_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original



@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_completedslpckg_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original



@given(instance=CompleteDSLPckg_ObjectFlow_strategy)
def test_completedslpckg_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=CompleteDSLPckg_ControlFlow_strategy)
@settings(max_examples=50)
def test_completedslpckg_controlflow_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ControlFlow)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=CompleteDSLPckg_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_completedslpckg_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InterruptibleActivityRegion)

@given(instance=CompleteDSLPckg_ActivityPartition_strategy)
@settings(max_examples=50)
def test_completedslpckg_activitypartition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityPartition)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=CompleteDSLPckg_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_flowfinalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FlowFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=CompleteDSLPckg_JoinNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_joinnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_JoinNode)



@given(instance=CompleteDSLPckg_JoinNode_strategy)
def test_completedslpckg_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=CompleteDSLPckg_DecisionNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_decisionnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DecisionNode)

@given(instance=CompleteDSLPckg_FinalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_finalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FinalNode)

@given(instance=CompleteDSLPckg_ForkNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_forknode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ForkNode)

@given(instance=CompleteDSLPckg_InitialNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_initialnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InitialNode)

@given(instance=CompleteDSLPckg_MergeNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_mergenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MergeNode)

@given(instance=CompleteDSLPckg_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_activityfinalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityFinalNode)

@given(instance=CompleteDSLPckg_ControlNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_controlnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ControlNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=CompleteDSLPckg_ExpansionNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_expansionnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExpansionNode)

@given(instance=CompleteDSLPckg_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CentralBufferNode)

@given(instance=CompleteDSLPckg_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_activityparameternode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityParameterNode)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=CompleteDSLPckg_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_destroylinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DestroyLinkAction)

@given(instance=CompleteDSLPckg_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_createlinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CreateLinkAction)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=CompleteDSLPckg_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ClearStructuralFeatureAction)

@given(instance=CompleteDSLPckg_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_WriteStructuralFeatureAction)

@given(instance=CompleteDSLPckg_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadStructuralFeatureAction)

@given(instance=CompleteDSLPckg_CallOperationAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_calloperationaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallOperationAction)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=CompleteDSLPckg_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StartObjectBehaviorAction)

@given(instance=CompleteDSLPckg_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_callbehavioraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallBehaviorAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=CompleteDSLPckg_SendSignalAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_sendsignalaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SendSignalAction)

@given(instance=CompleteDSLPckg_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BroadcastSignalAction)

@given(instance=CompleteDSLPckg_CallAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_callaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallAction)



@given(instance=CompleteDSLPckg_CallAction_strategy)
def test_completedslpckg_callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=CompleteDSLPckg_ActionInputPin_strategy)
@settings(max_examples=50)
def test_completedslpckg_actioninputpin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActionInputPin)

@given(instance=CompleteDSLPckg_ValuePin_strategy)
@settings(max_examples=50)
def test_completedslpckg_valuepin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ValuePin)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=CompleteDSLPckg_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DestroyObjectAction)

@given(instance=CompleteDSLPckg_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReclassifyObjectAction)



@given(instance=CompleteDSLPckg_ReclassifyObjectAction_strategy)
def test_completedslpckg_reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=CompleteDSLPckg_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_testidentityaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TestIdentityAction)

@given(instance=CompleteDSLPckg_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readselfaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadSelfAction)

@given(instance=CompleteDSLPckg_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ValueSpecificationAction)

@given(instance=CompleteDSLPckg_VariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_variableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_VariableAction)

@given(instance=CompleteDSLPckg_ReduceAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_reduceaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReduceAction)



@given(instance=CompleteDSLPckg_ReduceAction_strategy)
def test_completedslpckg_reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=CompleteDSLPckg_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuralFeatureAction)

@given(instance=CompleteDSLPckg_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadLinkObjectEndAction)

@given(instance=CompleteDSLPckg_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RaiseExceptionAction)

@given(instance=CompleteDSLPckg_ReplyAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_replyaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReplyAction)

@given(instance=CompleteDSLPckg_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadLinkObjectEndQualifierAction)

@given(instance=CompleteDSLPckg_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_createobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CreateObjectAction)

@given(instance=CompleteDSLPckg_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StartClassifierBehaviorAction)

@given(instance=CompleteDSLPckg_LinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_linkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkAction)

@given(instance=CompleteDSLPckg_UnmarshallAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_unmarshallaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_UnmarshallAction)

@given(instance=CompleteDSLPckg_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_accepteventaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AcceptEventAction)



@given(instance=CompleteDSLPckg_AcceptEventAction_strategy)
def test_completedslpckg_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=CompleteDSLPckg_ReadExtendAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_readextendaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ReadExtendAction)

@given(instance=CompleteDSLPckg_OpaqueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_opaqueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OpaqueAction)



@given(instance=CompleteDSLPckg_OpaqueAction_strategy)
def test_completedslpckg_opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=CompleteDSLPckg_OpaqueAction_strategy)
def test_completedslpckg_opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=CompleteDSLPckg_SendObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_sendobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SendObjectAction)

@given(instance=CompleteDSLPckg_InputPin_strategy)
@settings(max_examples=50)
def test_completedslpckg_inputpin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InputPin)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=CompleteDSLPckg_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_deploymentspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DeploymentSpecification)



@given(instance=CompleteDSLPckg_DeploymentSpecification_strategy)
def test_completedslpckg_deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original



@given(instance=CompleteDSLPckg_DeploymentSpecification_strategy)
def test_completedslpckg_deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=CompleteDSLPckg_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_completedslpckg_executionenvironment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExecutionEnvironment)

@given(instance=CompleteDSLPckg_Device_strategy)
@settings(max_examples=50)
def test_completedslpckg_device_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Device)

@given(instance=CompleteDSLPckg_OutputPin_strategy)
@settings(max_examples=50)
def test_completedslpckg_outputpin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OutputPin)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=CompleteDSLPckg_InvocationAction_strategy)
@settings(max_examples=50)
def test_completedslpckg_invocationaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InvocationAction)

@given(instance=CompleteDSLPckg_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_completedslpckg_connectorend_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConnectorEnd)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=CompleteDSLPckg_Port_strategy)
@settings(max_examples=50)
def test_completedslpckg_port_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Port)



@given(instance=CompleteDSLPckg_Port_strategy)
def test_completedslpckg_port_isConjugated_setter(instance):
    original = instance.isConjugated
    instance.isConjugated = original
    assert instance.isConjugated == original



@given(instance=CompleteDSLPckg_Port_strategy)
def test_completedslpckg_port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original



@given(instance=CompleteDSLPckg_Port_strategy)
def test_completedslpckg_port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=CompleteDSLPckg_DurationConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg_durationconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DurationConstraint)



@given(instance=CompleteDSLPckg_DurationConstraint_strategy)
def test_completedslpckg_durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=CompleteDSLPckg_TimeConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg_timeconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeConstraint)



@given(instance=CompleteDSLPckg_TimeConstraint_strategy)
def test_completedslpckg_timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=CompleteDSLPckg_InteractionConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg_interactionconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionConstraint)

@given(instance=CompleteDSLPckg_IntervalConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg_intervalconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_IntervalConstraint)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=CompleteDSLPckg_DurationInterval_strategy)
@settings(max_examples=50)
def test_completedslpckg_durationinterval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DurationInterval)

@given(instance=CompleteDSLPckg_TimeInterval_strategy)
@settings(max_examples=50)
def test_completedslpckg_timeinterval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeInterval)

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=CompleteDSLPckg_DurationObservation_strategy)
@settings(max_examples=50)
def test_completedslpckg_durationobservation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DurationObservation)



@given(instance=CompleteDSLPckg_DurationObservation_strategy)
def test_completedslpckg_durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=CompleteDSLPckg_TimeObservation_strategy)
@settings(max_examples=50)
def test_completedslpckg_timeobservation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeObservation)



@given(instance=CompleteDSLPckg_TimeObservation_strategy)
def test_completedslpckg_timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=CompleteDSLPckg_TimeEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg_timeevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeEvent)



@given(instance=CompleteDSLPckg_TimeEvent_strategy)
def test_completedslpckg_timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=CompleteDSLPckg_SignalEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg_signalevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_SignalEvent)

@given(instance=CompleteDSLPckg_CallEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg_callevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CallEvent)

@given(instance=CompleteDSLPckg_AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg_anyreceiveevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AnyReceiveEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=CompleteDSLPckg_ChangeEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg_changeevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ChangeEvent)

@given(instance=CompleteDSLPckg_MessageEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg_messageevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MessageEvent)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=CompleteDSLPckg_FunctionBehavior_strategy)
@settings(max_examples=50)
def test_completedslpckg_functionbehavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_FunctionBehavior)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=CompleteDSLPckg_Interaction_strategy)
@settings(max_examples=50)
def test_completedslpckg_interaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Interaction)

@given(instance=CompleteDSLPckg_StateMachine_strategy)
@settings(max_examples=50)
def test_completedslpckg_statemachine_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StateMachine)

@given(instance=CompleteDSLPckg_Activity_strategy)
@settings(max_examples=50)
def test_completedslpckg_activity_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Activity)



@given(instance=CompleteDSLPckg_Activity_strategy)
def test_completedslpckg_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original



@given(instance=CompleteDSLPckg_Activity_strategy)
def test_completedslpckg_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=CompleteDSLPckg_OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_completedslpckg_opaquebehavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OpaqueBehavior)



@given(instance=CompleteDSLPckg_OpaqueBehavior_strategy)
def test_completedslpckg_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=CompleteDSLPckg_OpaqueBehavior_strategy)
def test_completedslpckg_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=CompleteDSLPckg_CommunicationPath_strategy)
@settings(max_examples=50)
def test_completedslpckg_communicationpath_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CommunicationPath)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=CompleteDSLPckg_AssociationClass_strategy)
@settings(max_examples=50)
def test_completedslpckg_associationclass_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_AssociationClass)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=CompleteDSLPckg_InterfaceRealization_strategy)
@settings(max_examples=50)
def test_completedslpckg_interfacerealization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InterfaceRealization)

@given(instance=CompleteDSLPckg_ComponentRealization_strategy)
@settings(max_examples=50)
def test_completedslpckg_componentrealization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ComponentRealization)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=CompleteDSLPckg_Manifestation_strategy)
@settings(max_examples=50)
def test_completedslpckg_manifestation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Manifestation)

@given(instance=CompleteDSLPckg_Realization_strategy)
@settings(max_examples=50)
def test_completedslpckg_realization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Realization)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=CompleteDSLPckg_Abstraction_strategy)
@settings(max_examples=50)
def test_completedslpckg_abstraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Abstraction)

@given(instance=CompleteDSLPckg_Deployment_strategy)
@settings(max_examples=50)
def test_completedslpckg_deployment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Deployment)

@given(instance=CompleteDSLPckg_Usage_strategy)
@settings(max_examples=50)
def test_completedslpckg_usage_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Usage)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=CompleteDSLPckg_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_completedslpckg_enumerationliteral_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=CompleteDSLPckg_Enumeration_strategy)
@settings(max_examples=50)
def test_completedslpckg_enumeration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Enumeration)

@given(instance=CompleteDSLPckg_PrimitiveType_strategy)
@settings(max_examples=50)
def test_completedslpckg_primitivetype_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PrimitiveType)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=CompleteDSLPckg_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_completedslpckg_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_EncapsulatedClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=CompleteDSLPckg_UseCase_strategy)
@settings(max_examples=50)
def test_completedslpckg_usecase_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_UseCase)

@given(instance=CompleteDSLPckg_Actor_strategy)
@settings(max_examples=50)
def test_completedslpckg_actor_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Actor)

@given(instance=CompleteDSLPckg_Collaboration_strategy)
@settings(max_examples=50)
def test_completedslpckg_collaboration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Collaboration)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=CompleteDSLPckg_Signal_strategy)
@settings(max_examples=50)
def test_completedslpckg_signal_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Signal)

@given(instance=CompleteDSLPckg_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_completedslpckg_structuredclassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuredClassifier)

@given(instance=CompleteDSLPckg_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_completedslpckg_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BehavioredClassifier)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=CompleteDSLPckg_Reception_strategy)
@settings(max_examples=50)
def test_completedslpckg_reception_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Reception)

@given(instance=CompleteDSLPckg_Operation_strategy)
@settings(max_examples=50)
def test_completedslpckg_operation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Operation)



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_completedslpckg_operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_completedslpckg_operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_completedslpckg_operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_completedslpckg_operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=CompleteDSLPckg_Operation_strategy)
def test_completedslpckg_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=CompleteDSLPckg_Interface_strategy)
@settings(max_examples=50)
def test_completedslpckg_interface_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Interface)

@given(instance=CompleteDSLPckg_DataType_strategy)
@settings(max_examples=50)
def test_completedslpckg_datatype_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DataType)

@given(instance=CompleteDSLPckg_Class_strategy)
@settings(max_examples=50)
def test_completedslpckg_class_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Class)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=CompleteDSLPckg_Node_strategy)
@settings(max_examples=50)
def test_completedslpckg_node_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Node)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=CompleteDSLPckg_Connector_strategy)
@settings(max_examples=50)
def test_completedslpckg_connector_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Connector)



@given(instance=CompleteDSLPckg_Connector_strategy)
def test_completedslpckg_connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CompleteDSLPckg_Substitution_strategy)
@settings(max_examples=50)
def test_completedslpckg_substitution_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Substitution)

@given(instance=CompleteDSLPckg_Property_strategy)
@settings(max_examples=50)
def test_completedslpckg_property_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Property)



@given(instance=CompleteDSLPckg_Property_strategy)
def test_completedslpckg_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_completedslpckg_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_completedslpckg_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_completedslpckg_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_completedslpckg_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=CompleteDSLPckg_Property_strategy)
def test_completedslpckg_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=CompleteDSLPckg_Feature_strategy)
@settings(max_examples=50)
def test_completedslpckg_feature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Feature)



@given(instance=CompleteDSLPckg_Feature_strategy)
def test_completedslpckg_feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=CompleteDSLPckg_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_completedslpckg_extensionpoint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExtensionPoint)

@given(instance=CompleteDSLPckg_ActivityEdge_strategy)
@settings(max_examples=50)
def test_completedslpckg_activityedge_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityEdge)

@given(instance=CompleteDSLPckg_InstanceValue_strategy)
@settings(max_examples=50)
def test_completedslpckg_instancevalue_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InstanceValue)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=CompleteDSLPckg_LiteralString_strategy)
@settings(max_examples=50)
def test_completedslpckg_literalstring_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralString)

@given(instance=CompleteDSLPckg_LiteralUnilimitedNatural_strategy)
@settings(max_examples=50)
def test_completedslpckg_literalunilimitednatural_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralUnilimitedNatural)

@given(instance=CompleteDSLPckg_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_completedslpckg_literalboolean_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralBoolean)

@given(instance=CompleteDSLPckg_LiteralReal_strategy)
@settings(max_examples=50)
def test_completedslpckg_literalreal_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralReal)

@given(instance=CompleteDSLPckg_LiteralInteger_strategy)
@settings(max_examples=50)
def test_completedslpckg_literalinteger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralInteger)

@given(instance=CompleteDSLPckg_LiteralNull_strategy)
@settings(max_examples=50)
def test_completedslpckg_literalnull_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralNull)

@given(instance=CompleteDSLPckg_Behavior_strategy)
@settings(max_examples=50)
def test_completedslpckg_behavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Behavior)



@given(instance=CompleteDSLPckg_Behavior_strategy)
def test_completedslpckg_behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=CompleteDSLPckg_Duration_strategy)
@settings(max_examples=50)
def test_completedslpckg_duration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Duration)

@given(instance=CompleteDSLPckg_TimeExpression_strategy)
@settings(max_examples=50)
def test_completedslpckg_timeexpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TimeExpression)

@given(instance=CompleteDSLPckg_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_literalspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LiteralSpecification)

@given(instance=CompleteDSLPckg_Interval_strategy)
@settings(max_examples=50)
def test_completedslpckg_interval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Interval)

@given(instance=CompleteDSLPckg_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_completedslpckg_opaqueexpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_OpaqueExpression)



@given(instance=CompleteDSLPckg_OpaqueExpression_strategy)
def test_completedslpckg_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=CompleteDSLPckg_OpaqueExpression_strategy)
def test_completedslpckg_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=CompleteDSLPckg_Expression_strategy)
@settings(max_examples=50)
def test_completedslpckg_expression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Expression)



@given(instance=CompleteDSLPckg_Expression_strategy)
def test_completedslpckg_expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=CompleteDSLPckg_Parameter_strategy)
@settings(max_examples=50)
def test_completedslpckg_parameter_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Parameter)



@given(instance=CompleteDSLPckg_Parameter_strategy)
def test_completedslpckg_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CompleteDSLPckg_Variable_strategy)
@settings(max_examples=50)
def test_completedslpckg_variable_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Variable)

@given(instance=CompleteDSLPckg_ObjectNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_objectnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ObjectNode)

@given(instance=CompleteDSLPckg_Pin_strategy)
@settings(max_examples=50)
def test_completedslpckg_pin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Pin)

@given(instance=CompleteDSLPckg_ConnectableElement_strategy)
@settings(max_examples=50)
def test_completedslpckg_connectableelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ConnectableElement)

@given(instance=CompleteDSLPckg_StructuralFeature_strategy)
@settings(max_examples=50)
def test_completedslpckg_structuralfeature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuralFeature)



@given(instance=CompleteDSLPckg_StructuralFeature_strategy)
def test_completedslpckg_structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=CompleteDSLPckg_Association_strategy)
@settings(max_examples=50)
def test_completedslpckg_association_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Association)



@given(instance=CompleteDSLPckg_Association_strategy)
def test_completedslpckg_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=CompleteDSLPckg_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_completedslpckg_directedrelationship_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DirectedRelationship)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=CompleteDSLPckg_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_instancespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InstanceSpecification)

@given(instance=CompleteDSLPckg_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_completedslpckg_generalizationset_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_GeneralizationSet)



@given(instance=CompleteDSLPckg_GeneralizationSet_strategy)
def test_completedslpckg_generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original



@given(instance=CompleteDSLPckg_GeneralizationSet_strategy)
def test_completedslpckg_generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=CompleteDSLPckg_Observation_strategy)
@settings(max_examples=50)
def test_completedslpckg_observation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Observation)

@given(instance=CompleteDSLPckg_Type_strategy)
@settings(max_examples=50)
def test_completedslpckg_type_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Type)

@given(instance=CompleteDSLPckg_Event_strategy)
@settings(max_examples=50)
def test_completedslpckg_event_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Event)

@given(instance=CompleteDSLPckg_ValueSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg_valuespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ValueSpecification)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=CompleteDSLPckg_State_strategy)
@settings(max_examples=50)
def test_completedslpckg_state_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_State)



@given(instance=CompleteDSLPckg_State_strategy)
def test_completedslpckg_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original



@given(instance=CompleteDSLPckg_State_strategy)
def test_completedslpckg_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=CompleteDSLPckg_State_strategy)
def test_completedslpckg_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=CompleteDSLPckg_State_strategy)
def test_completedslpckg_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=CompleteDSLPckg_Classifier_strategy)
@settings(max_examples=50)
def test_completedslpckg_classifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Classifier)



@given(instance=CompleteDSLPckg_Classifier_strategy)
def test_completedslpckg_classifier_isFinalSpecialization_setter(instance):
    original = instance.isFinalSpecialization
    instance.isFinalSpecialization = original
    assert instance.isFinalSpecialization == original



@given(instance=CompleteDSLPckg_Classifier_strategy)
def test_completedslpckg_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=CompleteDSLPckg_Region_strategy)
@settings(max_examples=50)
def test_completedslpckg_region_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Region)

@given(instance=CompleteDSLPckg_Transition_strategy)
@settings(max_examples=50)
def test_completedslpckg_transition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Transition)



@given(instance=CompleteDSLPckg_Transition_strategy)
def test_completedslpckg_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CompleteDSLPckg_InteractionOperand_strategy)
@settings(max_examples=50)
def test_completedslpckg_interactionoperand_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionOperand)

@given(instance=CompleteDSLPckg_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_StructuredActivityNode)



@given(instance=CompleteDSLPckg_StructuredActivityNode_strategy)
def test_completedslpckg_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=CompleteDSLPckg_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_completedslpckg_behavioralfeature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_BehavioralFeature)

@given(instance=CompleteDSLPckg_Package_strategy)
@settings(max_examples=50)
def test_completedslpckg_package_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Package)



@given(instance=CompleteDSLPckg_Package_strategy)
def test_completedslpckg_package_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=CompleteDSLPckg_Generalization_strategy)
@settings(max_examples=50)
def test_completedslpckg_generalization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Generalization)



@given(instance=CompleteDSLPckg_Generalization_strategy)
def test_completedslpckg_generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=CompleteDSLPckg_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_completedslpckg_protocolconformance_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ProtocolConformance)

@given(instance=CompleteDSLPckg_PackageMerge_strategy)
@settings(max_examples=50)
def test_completedslpckg_packagemerge_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PackageMerge)

@given(instance=CompleteDSLPckg_Constraint_strategy)
@settings(max_examples=50)
def test_completedslpckg_constraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Constraint)

@given(instance=CompleteDSLPckg_PackageImport_strategy)
@settings(max_examples=50)
def test_completedslpckg_packageimport_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PackageImport)



@given(instance=CompleteDSLPckg_PackageImport_strategy)
def test_completedslpckg_packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=CompleteDSLPckg_ElementImport_strategy)
@settings(max_examples=50)
def test_completedslpckg_elementimport_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ElementImport)



@given(instance=CompleteDSLPckg_ElementImport_strategy)
def test_completedslpckg_elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=CompleteDSLPckg_ElementImport_strategy)
def test_completedslpckg_elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=CompleteDSLPckg_Dependency_strategy)
@settings(max_examples=50)
def test_completedslpckg_dependency_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Dependency)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_completedslpckg_multiplicityelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MultiplicityElement)



@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_completedslpckg_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_completedslpckg_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_completedslpckg_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=CompleteDSLPckg_MultiplicityElement_strategy)
def test_completedslpckg_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=CompleteDSLPckg_Slot_strategy)
@settings(max_examples=50)
def test_completedslpckg_slot_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Slot)

@given(instance=CompleteDSLPckg_LinkEndData_strategy)
@settings(max_examples=50)
def test_completedslpckg_linkenddata_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_LinkEndData)

@given(instance=CompleteDSLPckg_QualifierValue_strategy)
@settings(max_examples=50)
def test_completedslpckg_qualifiervalue_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_QualifierValue)

@given(instance=CompleteDSLPckg_Clause_strategy)
@settings(max_examples=50)
def test_completedslpckg_clause_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Clause)

@given(instance=CompleteDSLPckg_Relationship_strategy)
@settings(max_examples=50)
def test_completedslpckg_relationship_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Relationship)

@given(instance=CompleteDSLPckg_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_completedslpckg_exceptionhandler_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ExceptionHandler)

@given(instance=CompleteDSLPckg_NamedElement_strategy)
@settings(max_examples=50)
def test_completedslpckg_namedelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_NamedElement)



@given(instance=CompleteDSLPckg_NamedElement_strategy)
def test_completedslpckg_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=CompleteDSLPckg_NamedElement_strategy)
def test_completedslpckg_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=CompleteDSLPckg_NamedElement_strategy)
def test_completedslpckg_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompleteDSLPckg_Comment_strategy)
@settings(max_examples=50)
def test_completedslpckg_comment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Comment)



@given(instance=CompleteDSLPckg_Comment_strategy)
def test_completedslpckg_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=CompleteDSLPckg_Element_strategy)
@settings(max_examples=50)
def test_completedslpckg_element_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Element)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=CompleteDSLPckg_TypedElement_strategy)
@settings(max_examples=50)
def test_completedslpckg_typedelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_TypedElement)

@given(instance=CompleteDSLPckg_MessageEnd_strategy)
@settings(max_examples=50)
def test_completedslpckg_messageend_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_MessageEnd)

@given(instance=CompleteDSLPckg_Message_strategy)
@settings(max_examples=50)
def test_completedslpckg_message_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Message)



@given(instance=CompleteDSLPckg_Message_strategy)
def test_completedslpckg_message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original



@given(instance=CompleteDSLPckg_Message_strategy)
def test_completedslpckg_message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original

@given(instance=CompleteDSLPckg_Lifeline_strategy)
@settings(max_examples=50)
def test_completedslpckg_lifeline_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Lifeline)

@given(instance=CompleteDSLPckg_GeneralOrdering_strategy)
@settings(max_examples=50)
def test_completedslpckg_generalordering_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_GeneralOrdering)

@given(instance=CompleteDSLPckg_Component_strategy)
@settings(max_examples=50)
def test_completedslpckg_component_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Component)



@given(instance=CompleteDSLPckg_Component_strategy)
def test_completedslpckg_component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original

@given(instance=CompleteDSLPckg_Namespace_strategy)
@settings(max_examples=50)
def test_completedslpckg_namespace_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Namespace)

@given(instance=CompleteDSLPckg_CollaborationUse_strategy)
@settings(max_examples=50)
def test_completedslpckg_collaborationuse_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_CollaborationUse)

@given(instance=CompleteDSLPckg_Vertex_strategy)
@settings(max_examples=50)
def test_completedslpckg_vertex_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Vertex)

@given(instance=CompleteDSLPckg_RedefinableElement_strategy)
@settings(max_examples=50)
def test_completedslpckg_redefinableelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_RedefinableElement)



@given(instance=CompleteDSLPckg_RedefinableElement_strategy)
def test_completedslpckg_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=CompleteDSLPckg_PackageableElement_strategy)
@settings(max_examples=50)
def test_completedslpckg_packageableelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_PackageableElement)

@given(instance=CompleteDSLPckg_DeploymentTarget_strategy)
@settings(max_examples=50)
def test_completedslpckg_deploymenttarget_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DeploymentTarget)

@given(instance=CompleteDSLPckg_ParameterSet_strategy)
@settings(max_examples=50)
def test_completedslpckg_parameterset_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ParameterSet)

@given(instance=CompleteDSLPckg_InteractionFragment_strategy)
@settings(max_examples=50)
def test_completedslpckg_interactionfragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_InteractionFragment)

@given(instance=CompleteDSLPckg_DeployedArtifact_strategy)
@settings(max_examples=50)
def test_completedslpckg_deployedartifact_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_DeployedArtifact)

@given(instance=CompleteDSLPckg_Extend_strategy)
@settings(max_examples=50)
def test_completedslpckg_extend_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Extend)

@given(instance=CompleteDSLPckg_Artifact_strategy)
@settings(max_examples=50)
def test_completedslpckg_artifact_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Artifact)



@given(instance=CompleteDSLPckg_Artifact_strategy)
def test_completedslpckg_artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=CompleteDSLPckg_ActivityGroup_strategy)
@settings(max_examples=50)
def test_completedslpckg_activitygroup_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityGroup)

@given(instance=CompleteDSLPckg_ActivityNode_strategy)
@settings(max_examples=50)
def test_completedslpckg_activitynode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_ActivityNode)

@given(instance=CompleteDSLPckg_Trigger_strategy)
@settings(max_examples=50)
def test_completedslpckg_trigger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Trigger)

@given(instance=CompleteDSLPckg_Action_strategy)
@settings(max_examples=50)
def test_completedslpckg_action_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Action)

@given(instance=CompleteDSLPckg_Include_strategy)
@settings(max_examples=50)
def test_completedslpckg_include_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg_Include)

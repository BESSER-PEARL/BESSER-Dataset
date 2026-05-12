import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    uml3_0_0_ProtocolTransition,
    CentralBufferNode,
    uml3_0_0_DataStoreNode,
    AcceptEventAction,
    uml3_0_0_AcceptCallAction,
    CreateLinkAction,
    uml3_0_0_CreateLinkObjectAction,
    WriteVariableAction,
    uml3_0_0_AddVariableValueAction,
    VariableAction,
    uml3_0_0_WriteVariableAction,
    uml3_0_0_ClearVariableAction,
    uml3_0_0_ReadVariableAction,
    uml3_0_0_RemoveVariableValueAction,
    State,
    uml3_0_0_FinalState,
    Observation,
    uml3_0_0_DurationObservation,
    uml3_0_0_TimeObservation,
    IntervalConstraint,
    uml3_0_0_DurationConstraint,
    uml3_0_0_TimeConstraint,
    Interval,
    uml3_0_0_TimeInterval,
    uml3_0_0_DurationInterval,
    WriteLinkAction,
    uml3_0_0_CreateLinkAction,
    LinkEndData,
    uml3_0_0_LinkEndCreationData,
    uml3_0_0_LinkEndDestructionData,
    uml3_0_0_DestroyLinkAction,
    LinkAction,
    uml3_0_0_WriteLinkAction,
    uml3_0_0_ReadLinkAction,
    WriteStructuralFeatureAction,
    uml3_0_0_AddStructuralFeatureValueAction,
    uml3_0_0_RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    uml3_0_0_ClearStructuralFeatureAction,
    uml3_0_0_WriteStructuralFeatureAction,
    uml3_0_0_ReadStructuralFeatureAction,
    CombinedFragment,
    uml3_0_0_ConsiderIgnoreFragment,
    Node,
    uml3_0_0_ExecutionEnvironment,
    uml3_0_0_Device,
    FinalNode,
    uml3_0_0_ActivityFinalNode,
    uml3_0_0_FlowFinalNode,
    OccurrenceSpecification,
    uml3_0_0_ExecutionOccurrenceSpecification,
    MessageEvent,
    uml3_0_0_CallEvent,
    uml3_0_0_SendSignalEvent,
    uml3_0_0_ReceiveSignalEvent,
    uml3_0_0_AnyReceiveEvent,
    uml3_0_0_ReceiveOperationEvent,
    uml3_0_0_SignalEvent,
    ExecutionSpecification,
    uml3_0_0_ActionExecutionSpecification,
    InteractionUse,
    Constraint,
    uml3_0_0_IntervalConstraint,
    uml3_0_0_PartDecomposition,
    uml3_0_0_InteractionConstraint,
    MessageEnd,
    uml3_0_0_MessageOccurrenceSpecification,
    InteractionFragment,
    uml3_0_0_CombinedFragment,
    uml3_0_0_OccurrenceSpecification,
    uml3_0_0_StateInvariant,
    uml3_0_0_InteractionUse,
    uml3_0_0_Continuation,
    uml3_0_0_ExecutionSpecification,
    uml3_0_0_Gate,
    InputPin,
    uml3_0_0_ActionInputPin,
    uml3_0_0_ValuePin,
    ControlNode,
    uml3_0_0_FinalNode,
    uml3_0_0_MergeNode,
    uml3_0_0_JoinNode,
    uml3_0_0_ForkNode,
    uml3_0_0_DecisionNode,
    uml3_0_0_InitialNode,
    ActivityEdge,
    uml3_0_0_ObjectFlow,
    uml3_0_0_ControlFlow,
    StructuredActivityNode,
    uml3_0_0_ConditionalNode,
    uml3_0_0_ExpansionRegion,
    uml3_0_0_LoopNode,
    uml3_0_0_SequenceNode,
    CallAction,
    uml3_0_0_CallBehaviorAction,
    uml3_0_0_StartObjectBehaviorAction,
    uml3_0_0_CallOperationAction,
    InvocationAction,
    uml3_0_0_BroadcastSignalAction,
    uml3_0_0_SendObjectAction,
    uml3_0_0_SendSignalAction,
    uml3_0_0_CallAction,
    ObjectNode,
    uml3_0_0_ActivityParameterNode,
    uml3_0_0_ExpansionNode,
    uml3_0_0_CentralBufferNode,
    Pin,
    ActivityGroup,
    uml3_0_0_InterruptibleActivityRegion,
    ActivityNode,
    uml3_0_0_ControlNode,
    uml3_0_0_ExecutableNode,
    ExecutableNode,
    uml3_0_0_Action,
    uml3_0_0_OutputPin,
    uml3_0_0_InputPin,
    Action,
    uml3_0_0_ReadSelfAction,
    uml3_0_0_CreateObjectAction,
    uml3_0_0_ReplyAction,
    uml3_0_0_RaiseExceptionAction,
    uml3_0_0_VariableAction,
    uml3_0_0_ReadExtentAction,
    uml3_0_0_AcceptEventAction,
    uml3_0_0_ReadLinkObjectEndAction,
    uml3_0_0_ReclassifyObjectAction,
    uml3_0_0_UnmarshallAction,
    uml3_0_0_LinkAction,
    uml3_0_0_InvocationAction,
    uml3_0_0_ReadLinkObjectEndQualifierAction,
    uml3_0_0_StartClassifierBehaviorAction,
    uml3_0_0_ReduceAction,
    uml3_0_0_ReadIsClassifiedObjectAction,
    uml3_0_0_ClearAssociationAction,
    uml3_0_0_ValueSpecificationAction,
    uml3_0_0_DestroyObjectAction,
    uml3_0_0_StructuralFeatureAction,
    uml3_0_0_TestIdentityAction,
    uml3_0_0_OpaqueAction,
    OpaqueBehavior,
    uml3_0_0_FunctionBehavior,
    LiteralSpecification,
    uml3_0_0_LiteralString,
    uml3_0_0_LiteralUnlimitedNatural,
    uml3_0_0_LiteralNull,
    uml3_0_0_LiteralBoolean,
    uml3_0_0_LiteralInteger,
    InstanceSpecification,
    uml3_0_0_EnumerationLiteral,
    DataType,
    uml3_0_0_PrimitiveType,
    uml3_0_0_Enumeration,
    Expression,
    TemplateSignature,
    TemplateParameter,
    uml3_0_0_ClassifierTemplateParameter,
    uml3_0_0_ConnectableElementTemplateParameter,
    uml3_0_0_OperationTemplateParameter,
    StructuredClassifier,
    uml3_0_0_EncapsulatedClassifier,
    Package,
    uml3_0_0_Model,
    uml3_0_0_Profile,
    Association,
    uml3_0_0_CommunicationPath,
    Vertex,
    uml3_0_0_ConnectionPointReference,
    Property,
    uml3_0_0_ExtensionEnd,
    uml3_0_0_Port,
    uml3_0_0_Pseudostate,
    Behavior,
    uml3_0_0_OpaqueBehavior,
    uml3_0_0_Interaction,
    uml3_0_0_Activity,
    uml3_0_0_StateMachine,
    StateMachine,
    uml3_0_0_ProtocolStateMachine,
    uml3_0_0_Extension,
    BehavioredClassifier,
    uml3_0_0_Actor,
    uml3_0_0_Collaboration,
    EncapsulatedClassifier,
    Class,
    uml3_0_0_AssociationClass,
    uml3_0_0_Stereotype,
    uml3_0_0_Component,
    Feature,
    uml3_0_0_Connector,
    BehavioralFeature,
    uml3_0_0_Reception,
    DeployedArtifact,
    Artifact,
    uml3_0_0_DeploymentSpecification,
    uml3_0_0_Class,
    DeploymentTarget,
    uml3_0_0_Node,
    StructuralFeature,
    ValueSpecification,
    uml3_0_0_LiteralSpecification,
    uml3_0_0_Interval,
    uml3_0_0_TimeExpression,
    uml3_0_0_Duration,
    uml3_0_0_Expression,
    uml3_0_0_InstanceValue,
    uml3_0_0_OpaqueExpression,
    Dependency,
    uml3_0_0_Deployment,
    uml3_0_0_Usage,
    uml3_0_0_Abstraction,
    Abstraction,
    uml3_0_0_Manifestation,
    uml3_0_0_Realization,
    uml3_0_0_SendOperationEvent,
    MultiplicityElement,
    uml3_0_0_Pin,
    uml3_0_0_ConnectorEnd,
    Event,
    uml3_0_0_TimeEvent,
    uml3_0_0_ChangeEvent,
    uml3_0_0_DestructionEvent,
    uml3_0_0_MessageEvent,
    uml3_0_0_CreationEvent,
    ConnectableElement,
    uml3_0_0_Variable,
    uml3_0_0_ExecutionEvent,
    uml3_0_0_Behavior,
    uml3_0_0_BehaviorExecutionSpecification,
    uml3_0_0_Parameter,
    Realization,
    uml3_0_0_ComponentRealization,
    uml3_0_0_InterfaceRealization,
    uml3_0_0_Property,
    Classifier,
    uml3_0_0_BehavioredClassifier,
    uml3_0_0_InformationItem,
    uml3_0_0_StructuredClassifier,
    uml3_0_0_DataType,
    uml3_0_0_Interface,
    uml3_0_0_Signal,
    uml3_0_0_Artifact,
    uml3_0_0_UseCase,
    uml3_0_0_Substitution,
    Type,
    RedefinableElement,
    uml3_0_0_ExtensionPoint,
    uml3_0_0_ActivityNode,
    uml3_0_0_RedefinableTemplateSignature,
    uml3_0_0_ActivityEdge,
    uml3_0_0_Feature,
    TypedElement,
    uml3_0_0_ObjectNode,
    uml3_0_0_StructuralFeature,
    DirectedRelationship,
    uml3_0_0_Generalization,
    uml3_0_0_TemplateBinding,
    uml3_0_0_ProtocolConformance,
    uml3_0_0_PackageImport,
    uml3_0_0_ElementImport,
    Relationship,
    uml3_0_0_Association,
    uml3_0_0_DirectedRelationship,
    EModelElement,
    ParameterableElement,
    uml3_0_0_ConnectableElement,
    NamedElement,
    uml3_0_0_CollaborationUse,
    uml3_0_0_ActivityPartition,
    uml3_0_0_GeneralOrdering,
    uml3_0_0_Vertex,
    uml3_0_0_TypedElement,
    uml3_0_0_Extend,
    uml3_0_0_RedefinableElement,
    uml3_0_0_DeploymentTarget,
    uml3_0_0_ParameterSet,
    uml3_0_0_DeployedArtifact,
    uml3_0_0_InteractionFragment,
    uml3_0_0_MessageEnd,
    uml3_0_0_Trigger,
    uml3_0_0_Message,
    uml3_0_0_Namespace,
    uml3_0_0_Lifeline,
    uml3_0_0_Include,
    uml3_0_0_ProfileApplication,
    uml3_0_0_PackageableElement,
    uml3_0_0_PackageMerge,
    TemplateableElement,
    uml3_0_0_StringExpression,
    uml3_0_0_Operation,
    PackageableElement,
    uml3_0_0_Type,
    uml3_0_0_Observation,
    uml3_0_0_InformationFlow,
    uml3_0_0_InstanceSpecification,
    uml3_0_0_Event,
    uml3_0_0_Dependency,
    uml3_0_0_ValueSpecification,
    uml3_0_0_Constraint,
    uml3_0_0_GeneralizationSet,
    Namespace,
    uml3_0_0_Transition,
    uml3_0_0_InteractionOperand,
    uml3_0_0_StructuredActivityNode,
    uml3_0_0_State,
    uml3_0_0_BehavioralFeature,
    uml3_0_0_Region,
    uml3_0_0_Classifier,
    uml3_0_0_Package,
    uml3_0_0_Element,
    Element,
    uml3_0_0_Relationship,
    uml3_0_0_Clause,
    uml3_0_0_LinkEndData,
    uml3_0_0_ParameterableElement,
    uml3_0_0_QualifierValue,
    uml3_0_0_Image,
    uml3_0_0_NamedElement,
    uml3_0_0_ExceptionHandler,
    uml3_0_0_MultiplicityElement,
    uml3_0_0_ActivityGroup,
    uml3_0_0_TemplateSignature,
    uml3_0_0_TemplateableElement,
    uml3_0_0_TemplateParameterSubstitution,
    uml3_0_0_Slot,
    uml3_0_0_TemplateParameter,
    uml3_0_0_Comment,
    ParameterEffectKind,
    ExpansionKind,
    PseudostateKind,
    AggregationKind,
    TransitionKind,
    ConnectorKind,
    ObjectNodeOrderingKind,
    MessageKind,
    VisibilityKind,
    InteractionOperatorKind,
    CallConcurrencyKind,
    ParameterDirectionKind,
    MessageSort,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ProtocolTransition)


def test_uml3_0_0_protocoltransition_constructor_exists():
    assert callable(uml3_0_0_ProtocolTransition.__init__)


def test_uml3_0_0_protocoltransition_constructor_args():
    sig = inspect.signature(uml3_0_0_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_datastorenode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DataStoreNode)


def test_uml3_0_0_datastorenode_constructor_exists():
    assert callable(uml3_0_0_DataStoreNode.__init__)


def test_uml3_0_0_datastorenode_constructor_args():
    sig = inspect.signature(uml3_0_0_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_AcceptCallAction)


def test_uml3_0_0_acceptcallaction_constructor_exists():
    assert callable(uml3_0_0_AcceptCallAction.__init__)


def test_uml3_0_0_acceptcallaction_constructor_args():
    sig = inspect.signature(uml3_0_0_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CreateLinkObjectAction)


def test_uml3_0_0_createlinkobjectaction_constructor_exists():
    assert callable(uml3_0_0_CreateLinkObjectAction.__init__)


def test_uml3_0_0_createlinkobjectaction_constructor_args():
    sig = inspect.signature(uml3_0_0_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_AddVariableValueAction)


def test_uml3_0_0_addvariablevalueaction_constructor_exists():
    assert callable(uml3_0_0_AddVariableValueAction.__init__)


def test_uml3_0_0_addvariablevalueaction_constructor_args():
    sig = inspect.signature(uml3_0_0_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3_0_0_addvariablevalueaction_has_isReplaceAll():
    assert hasattr(uml3_0_0_AddVariableValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml3_0_0_AddVariableValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_WriteVariableAction)


def test_uml3_0_0_writevariableaction_constructor_exists():
    assert callable(uml3_0_0_WriteVariableAction.__init__)


def test_uml3_0_0_writevariableaction_constructor_args():
    sig = inspect.signature(uml3_0_0_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ClearVariableAction)


def test_uml3_0_0_clearvariableaction_constructor_exists():
    assert callable(uml3_0_0_ClearVariableAction.__init__)


def test_uml3_0_0_clearvariableaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadVariableAction)


def test_uml3_0_0_readvariableaction_constructor_exists():
    assert callable(uml3_0_0_ReadVariableAction.__init__)


def test_uml3_0_0_readvariableaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_RemoveVariableValueAction)


def test_uml3_0_0_removevariablevalueaction_constructor_exists():
    assert callable(uml3_0_0_RemoveVariableValueAction.__init__)


def test_uml3_0_0_removevariablevalueaction_constructor_args():
    sig = inspect.signature(uml3_0_0_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml3_0_0_removevariablevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml3_0_0_RemoveVariableValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml3_0_0_RemoveVariableValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_finalstate_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_FinalState)


def test_uml3_0_0_finalstate_constructor_exists():
    assert callable(uml3_0_0_FinalState.__init__)


def test_uml3_0_0_finalstate_constructor_args():
    sig = inspect.signature(uml3_0_0_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_durationobservation_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DurationObservation)


def test_uml3_0_0_durationobservation_constructor_exists():
    assert callable(uml3_0_0_DurationObservation.__init__)


def test_uml3_0_0_durationobservation_constructor_args():
    sig = inspect.signature(uml3_0_0_DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3_0_0_durationobservation_has_firstEvent():
    assert hasattr(uml3_0_0_DurationObservation, "firstEvent")
    descriptor = None
    for klass in uml3_0_0_DurationObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_timeobservation_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TimeObservation)


def test_uml3_0_0_timeobservation_constructor_exists():
    assert callable(uml3_0_0_TimeObservation.__init__)


def test_uml3_0_0_timeobservation_constructor_args():
    sig = inspect.signature(uml3_0_0_TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3_0_0_timeobservation_has_firstEvent():
    assert hasattr(uml3_0_0_TimeObservation, "firstEvent")
    descriptor = None
    for klass in uml3_0_0_TimeObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DurationConstraint)


def test_uml3_0_0_durationconstraint_constructor_exists():
    assert callable(uml3_0_0_DurationConstraint.__init__)


def test_uml3_0_0_durationconstraint_constructor_args():
    sig = inspect.signature(uml3_0_0_DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3_0_0_durationconstraint_has_firstEvent():
    assert hasattr(uml3_0_0_DurationConstraint, "firstEvent")
    descriptor = None
    for klass in uml3_0_0_DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TimeConstraint)


def test_uml3_0_0_timeconstraint_constructor_exists():
    assert callable(uml3_0_0_TimeConstraint.__init__)


def test_uml3_0_0_timeconstraint_constructor_args():
    sig = inspect.signature(uml3_0_0_TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3_0_0_timeconstraint_has_firstEvent():
    assert hasattr(uml3_0_0_TimeConstraint, "firstEvent")
    descriptor = None
    for klass in uml3_0_0_TimeConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_timeinterval_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TimeInterval)


def test_uml3_0_0_timeinterval_constructor_exists():
    assert callable(uml3_0_0_TimeInterval.__init__)


def test_uml3_0_0_timeinterval_constructor_args():
    sig = inspect.signature(uml3_0_0_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_durationinterval_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DurationInterval)


def test_uml3_0_0_durationinterval_constructor_exists():
    assert callable(uml3_0_0_DurationInterval.__init__)


def test_uml3_0_0_durationinterval_constructor_args():
    sig = inspect.signature(uml3_0_0_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CreateLinkAction)


def test_uml3_0_0_createlinkaction_constructor_exists():
    assert callable(uml3_0_0_CreateLinkAction.__init__)


def test_uml3_0_0_createlinkaction_constructor_args():
    sig = inspect.signature(uml3_0_0_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LinkEndCreationData)


def test_uml3_0_0_linkendcreationdata_constructor_exists():
    assert callable(uml3_0_0_LinkEndCreationData.__init__)


def test_uml3_0_0_linkendcreationdata_constructor_args():
    sig = inspect.signature(uml3_0_0_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3_0_0_linkendcreationdata_has_isReplaceAll():
    assert hasattr(uml3_0_0_LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in uml3_0_0_LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LinkEndDestructionData)


def test_uml3_0_0_linkenddestructiondata_constructor_exists():
    assert callable(uml3_0_0_LinkEndDestructionData.__init__)


def test_uml3_0_0_linkenddestructiondata_constructor_args():
    sig = inspect.signature(uml3_0_0_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_uml3_0_0_linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(uml3_0_0_LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in uml3_0_0_LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DestroyLinkAction)


def test_uml3_0_0_destroylinkaction_constructor_exists():
    assert callable(uml3_0_0_DestroyLinkAction.__init__)


def test_uml3_0_0_destroylinkaction_constructor_args():
    sig = inspect.signature(uml3_0_0_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_WriteLinkAction)


def test_uml3_0_0_writelinkaction_constructor_exists():
    assert callable(uml3_0_0_WriteLinkAction.__init__)


def test_uml3_0_0_writelinkaction_constructor_args():
    sig = inspect.signature(uml3_0_0_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadLinkAction)


def test_uml3_0_0_readlinkaction_constructor_exists():
    assert callable(uml3_0_0_ReadLinkAction.__init__)


def test_uml3_0_0_readlinkaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_AddStructuralFeatureValueAction)


def test_uml3_0_0_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml3_0_0_AddStructuralFeatureValueAction.__init__)


def test_uml3_0_0_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml3_0_0_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3_0_0_addstructuralfeaturevalueaction_has_isReplaceAll():
    assert hasattr(uml3_0_0_AddStructuralFeatureValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml3_0_0_AddStructuralFeatureValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_RemoveStructuralFeatureValueAction)


def test_uml3_0_0_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml3_0_0_RemoveStructuralFeatureValueAction.__init__)


def test_uml3_0_0_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml3_0_0_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml3_0_0_removestructuralfeaturevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml3_0_0_RemoveStructuralFeatureValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml3_0_0_RemoveStructuralFeatureValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ClearStructuralFeatureAction)


def test_uml3_0_0_clearstructuralfeatureaction_constructor_exists():
    assert callable(uml3_0_0_ClearStructuralFeatureAction.__init__)


def test_uml3_0_0_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_WriteStructuralFeatureAction)


def test_uml3_0_0_writestructuralfeatureaction_constructor_exists():
    assert callable(uml3_0_0_WriteStructuralFeatureAction.__init__)


def test_uml3_0_0_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3_0_0_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadStructuralFeatureAction)


def test_uml3_0_0_readstructuralfeatureaction_constructor_exists():
    assert callable(uml3_0_0_ReadStructuralFeatureAction.__init__)


def test_uml3_0_0_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ConsiderIgnoreFragment)


def test_uml3_0_0_considerignorefragment_constructor_exists():
    assert callable(uml3_0_0_ConsiderIgnoreFragment.__init__)


def test_uml3_0_0_considerignorefragment_constructor_args():
    sig = inspect.signature(uml3_0_0_ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExecutionEnvironment)


def test_uml3_0_0_executionenvironment_constructor_exists():
    assert callable(uml3_0_0_ExecutionEnvironment.__init__)


def test_uml3_0_0_executionenvironment_constructor_args():
    sig = inspect.signature(uml3_0_0_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_device_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Device)


def test_uml3_0_0_device_constructor_exists():
    assert callable(uml3_0_0_Device.__init__)


def test_uml3_0_0_device_constructor_args():
    sig = inspect.signature(uml3_0_0_Device.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActivityFinalNode)


def test_uml3_0_0_activityfinalnode_constructor_exists():
    assert callable(uml3_0_0_ActivityFinalNode.__init__)


def test_uml3_0_0_activityfinalnode_constructor_args():
    sig = inspect.signature(uml3_0_0_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_FlowFinalNode)


def test_uml3_0_0_flowfinalnode_constructor_exists():
    assert callable(uml3_0_0_FlowFinalNode.__init__)


def test_uml3_0_0_flowfinalnode_constructor_args():
    sig = inspect.signature(uml3_0_0_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExecutionOccurrenceSpecification)


def test_uml3_0_0_executionoccurrencespecification_constructor_exists():
    assert callable(uml3_0_0_ExecutionOccurrenceSpecification.__init__)


def test_uml3_0_0_executionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml3_0_0_ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_callevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CallEvent)


def test_uml3_0_0_callevent_constructor_exists():
    assert callable(uml3_0_0_CallEvent.__init__)


def test_uml3_0_0_callevent_constructor_args():
    sig = inspect.signature(uml3_0_0_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_sendsignalevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_SendSignalEvent)


def test_uml3_0_0_sendsignalevent_constructor_exists():
    assert callable(uml3_0_0_SendSignalEvent.__init__)


def test_uml3_0_0_sendsignalevent_constructor_args():
    sig = inspect.signature(uml3_0_0_SendSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_receivesignalevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReceiveSignalEvent)


def test_uml3_0_0_receivesignalevent_constructor_exists():
    assert callable(uml3_0_0_ReceiveSignalEvent.__init__)


def test_uml3_0_0_receivesignalevent_constructor_args():
    sig = inspect.signature(uml3_0_0_ReceiveSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_AnyReceiveEvent)


def test_uml3_0_0_anyreceiveevent_constructor_exists():
    assert callable(uml3_0_0_AnyReceiveEvent.__init__)


def test_uml3_0_0_anyreceiveevent_constructor_args():
    sig = inspect.signature(uml3_0_0_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_receiveoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReceiveOperationEvent)


def test_uml3_0_0_receiveoperationevent_constructor_exists():
    assert callable(uml3_0_0_ReceiveOperationEvent.__init__)


def test_uml3_0_0_receiveoperationevent_constructor_args():
    sig = inspect.signature(uml3_0_0_ReceiveOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_signalevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_SignalEvent)


def test_uml3_0_0_signalevent_constructor_exists():
    assert callable(uml3_0_0_SignalEvent.__init__)


def test_uml3_0_0_signalevent_constructor_args():
    sig = inspect.signature(uml3_0_0_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActionExecutionSpecification)


def test_uml3_0_0_actionexecutionspecification_constructor_exists():
    assert callable(uml3_0_0_ActionExecutionSpecification.__init__)


def test_uml3_0_0_actionexecutionspecification_constructor_args():
    sig = inspect.signature(uml3_0_0_ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionuse_is_not_abstract():
    assert not inspect.isabstract(InteractionUse)


def test_interactionuse_constructor_exists():
    assert callable(InteractionUse.__init__)


def test_interactionuse_constructor_args():
    sig = inspect.signature(InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_IntervalConstraint)


def test_uml3_0_0_intervalconstraint_constructor_exists():
    assert callable(uml3_0_0_IntervalConstraint.__init__)


def test_uml3_0_0_intervalconstraint_constructor_args():
    sig = inspect.signature(uml3_0_0_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_partdecomposition_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_PartDecomposition)


def test_uml3_0_0_partdecomposition_constructor_exists():
    assert callable(uml3_0_0_PartDecomposition.__init__)


def test_uml3_0_0_partdecomposition_constructor_args():
    sig = inspect.signature(uml3_0_0_PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InteractionConstraint)


def test_uml3_0_0_interactionconstraint_constructor_exists():
    assert callable(uml3_0_0_InteractionConstraint.__init__)


def test_uml3_0_0_interactionconstraint_constructor_args():
    sig = inspect.signature(uml3_0_0_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_MessageOccurrenceSpecification)


def test_uml3_0_0_messageoccurrencespecification_constructor_exists():
    assert callable(uml3_0_0_MessageOccurrenceSpecification.__init__)


def test_uml3_0_0_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(uml3_0_0_MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CombinedFragment)


def test_uml3_0_0_combinedfragment_constructor_exists():
    assert callable(uml3_0_0_CombinedFragment.__init__)


def test_uml3_0_0_combinedfragment_constructor_args():
    sig = inspect.signature(uml3_0_0_CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_uml3_0_0_combinedfragment_has_interactionOperator():
    assert hasattr(uml3_0_0_CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in uml3_0_0_CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_OccurrenceSpecification)


def test_uml3_0_0_occurrencespecification_constructor_exists():
    assert callable(uml3_0_0_OccurrenceSpecification.__init__)


def test_uml3_0_0_occurrencespecification_constructor_args():
    sig = inspect.signature(uml3_0_0_OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StateInvariant)


def test_uml3_0_0_stateinvariant_constructor_exists():
    assert callable(uml3_0_0_StateInvariant.__init__)


def test_uml3_0_0_stateinvariant_constructor_args():
    sig = inspect.signature(uml3_0_0_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_interactionuse_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InteractionUse)


def test_uml3_0_0_interactionuse_constructor_exists():
    assert callable(uml3_0_0_InteractionUse.__init__)


def test_uml3_0_0_interactionuse_constructor_args():
    sig = inspect.signature(uml3_0_0_InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_continuation_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Continuation)


def test_uml3_0_0_continuation_constructor_exists():
    assert callable(uml3_0_0_Continuation.__init__)


def test_uml3_0_0_continuation_constructor_args():
    sig = inspect.signature(uml3_0_0_Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_uml3_0_0_continuation_has_setting():
    assert hasattr(uml3_0_0_Continuation, "setting")
    descriptor = None
    for klass in uml3_0_0_Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_executionspecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExecutionSpecification)


def test_uml3_0_0_executionspecification_constructor_exists():
    assert callable(uml3_0_0_ExecutionSpecification.__init__)


def test_uml3_0_0_executionspecification_constructor_args():
    sig = inspect.signature(uml3_0_0_ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_gate_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Gate)


def test_uml3_0_0_gate_constructor_exists():
    assert callable(uml3_0_0_Gate.__init__)


def test_uml3_0_0_gate_constructor_args():
    sig = inspect.signature(uml3_0_0_Gate.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_actioninputpin_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActionInputPin)


def test_uml3_0_0_actioninputpin_constructor_exists():
    assert callable(uml3_0_0_ActionInputPin.__init__)


def test_uml3_0_0_actioninputpin_constructor_args():
    sig = inspect.signature(uml3_0_0_ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_valuepin_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ValuePin)


def test_uml3_0_0_valuepin_constructor_exists():
    assert callable(uml3_0_0_ValuePin.__init__)


def test_uml3_0_0_valuepin_constructor_args():
    sig = inspect.signature(uml3_0_0_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_finalnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_FinalNode)


def test_uml3_0_0_finalnode_constructor_exists():
    assert callable(uml3_0_0_FinalNode.__init__)


def test_uml3_0_0_finalnode_constructor_args():
    sig = inspect.signature(uml3_0_0_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_mergenode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_MergeNode)


def test_uml3_0_0_mergenode_constructor_exists():
    assert callable(uml3_0_0_MergeNode.__init__)


def test_uml3_0_0_mergenode_constructor_args():
    sig = inspect.signature(uml3_0_0_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_joinnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_JoinNode)


def test_uml3_0_0_joinnode_constructor_exists():
    assert callable(uml3_0_0_JoinNode.__init__)


def test_uml3_0_0_joinnode_constructor_args():
    sig = inspect.signature(uml3_0_0_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_uml3_0_0_joinnode_has_isCombineDuplicate():
    assert hasattr(uml3_0_0_JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in uml3_0_0_JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_forknode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ForkNode)


def test_uml3_0_0_forknode_constructor_exists():
    assert callable(uml3_0_0_ForkNode.__init__)


def test_uml3_0_0_forknode_constructor_args():
    sig = inspect.signature(uml3_0_0_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_decisionnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DecisionNode)


def test_uml3_0_0_decisionnode_constructor_exists():
    assert callable(uml3_0_0_DecisionNode.__init__)


def test_uml3_0_0_decisionnode_constructor_args():
    sig = inspect.signature(uml3_0_0_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_initialnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InitialNode)


def test_uml3_0_0_initialnode_constructor_exists():
    assert callable(uml3_0_0_InitialNode.__init__)


def test_uml3_0_0_initialnode_constructor_args():
    sig = inspect.signature(uml3_0_0_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_objectflow_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ObjectFlow)


def test_uml3_0_0_objectflow_constructor_exists():
    assert callable(uml3_0_0_ObjectFlow.__init__)


def test_uml3_0_0_objectflow_constructor_args():
    sig = inspect.signature(uml3_0_0_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"

def test_uml3_0_0_objectflow_has_isMulticast():
    assert hasattr(uml3_0_0_ObjectFlow, "isMulticast")
    descriptor = None
    for klass in uml3_0_0_ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_objectflow_has_isMultireceive():
    assert hasattr(uml3_0_0_ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in uml3_0_0_ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_controlflow_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ControlFlow)


def test_uml3_0_0_controlflow_constructor_exists():
    assert callable(uml3_0_0_ControlFlow.__init__)


def test_uml3_0_0_controlflow_constructor_args():
    sig = inspect.signature(uml3_0_0_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ConditionalNode)


def test_uml3_0_0_conditionalnode_constructor_exists():
    assert callable(uml3_0_0_ConditionalNode.__init__)


def test_uml3_0_0_conditionalnode_constructor_args():
    sig = inspect.signature(uml3_0_0_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssured" in params, "Missing parameter 'isAssured'"

def test_uml3_0_0_conditionalnode_has_isDeterminate():
    assert hasattr(uml3_0_0_ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in uml3_0_0_ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_conditionalnode_has_isAssured():
    assert hasattr(uml3_0_0_ConditionalNode, "isAssured")
    descriptor = None
    for klass in uml3_0_0_ConditionalNode.__mro__:
        if "isAssured" in klass.__dict__:
            descriptor = klass.__dict__["isAssured"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_expansionregion_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExpansionRegion)


def test_uml3_0_0_expansionregion_constructor_exists():
    assert callable(uml3_0_0_ExpansionRegion.__init__)


def test_uml3_0_0_expansionregion_constructor_args():
    sig = inspect.signature(uml3_0_0_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_uml3_0_0_expansionregion_has_mode():
    assert hasattr(uml3_0_0_ExpansionRegion, "mode")
    descriptor = None
    for klass in uml3_0_0_ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_loopnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LoopNode)


def test_uml3_0_0_loopnode_constructor_exists():
    assert callable(uml3_0_0_LoopNode.__init__)


def test_uml3_0_0_loopnode_constructor_args():
    sig = inspect.signature(uml3_0_0_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_uml3_0_0_loopnode_has_isTestedFirst():
    assert hasattr(uml3_0_0_LoopNode, "isTestedFirst")
    descriptor = None
    for klass in uml3_0_0_LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_sequencenode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_SequenceNode)


def test_uml3_0_0_sequencenode_constructor_exists():
    assert callable(uml3_0_0_SequenceNode.__init__)


def test_uml3_0_0_sequencenode_constructor_args():
    sig = inspect.signature(uml3_0_0_SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CallBehaviorAction)


def test_uml3_0_0_callbehavioraction_constructor_exists():
    assert callable(uml3_0_0_CallBehaviorAction.__init__)


def test_uml3_0_0_callbehavioraction_constructor_args():
    sig = inspect.signature(uml3_0_0_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StartObjectBehaviorAction)


def test_uml3_0_0_startobjectbehavioraction_constructor_exists():
    assert callable(uml3_0_0_StartObjectBehaviorAction.__init__)


def test_uml3_0_0_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml3_0_0_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CallOperationAction)


def test_uml3_0_0_calloperationaction_constructor_exists():
    assert callable(uml3_0_0_CallOperationAction.__init__)


def test_uml3_0_0_calloperationaction_constructor_args():
    sig = inspect.signature(uml3_0_0_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_BroadcastSignalAction)


def test_uml3_0_0_broadcastsignalaction_constructor_exists():
    assert callable(uml3_0_0_BroadcastSignalAction.__init__)


def test_uml3_0_0_broadcastsignalaction_constructor_args():
    sig = inspect.signature(uml3_0_0_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_SendObjectAction)


def test_uml3_0_0_sendobjectaction_constructor_exists():
    assert callable(uml3_0_0_SendObjectAction.__init__)


def test_uml3_0_0_sendobjectaction_constructor_args():
    sig = inspect.signature(uml3_0_0_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_SendSignalAction)


def test_uml3_0_0_sendsignalaction_constructor_exists():
    assert callable(uml3_0_0_SendSignalAction.__init__)


def test_uml3_0_0_sendsignalaction_constructor_args():
    sig = inspect.signature(uml3_0_0_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_callaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CallAction)


def test_uml3_0_0_callaction_constructor_exists():
    assert callable(uml3_0_0_CallAction.__init__)


def test_uml3_0_0_callaction_constructor_args():
    sig = inspect.signature(uml3_0_0_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_uml3_0_0_callaction_has_isSynchronous():
    assert hasattr(uml3_0_0_CallAction, "isSynchronous")
    descriptor = None
    for klass in uml3_0_0_CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActivityParameterNode)


def test_uml3_0_0_activityparameternode_constructor_exists():
    assert callable(uml3_0_0_ActivityParameterNode.__init__)


def test_uml3_0_0_activityparameternode_constructor_args():
    sig = inspect.signature(uml3_0_0_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_expansionnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExpansionNode)


def test_uml3_0_0_expansionnode_constructor_exists():
    assert callable(uml3_0_0_ExpansionNode.__init__)


def test_uml3_0_0_expansionnode_constructor_args():
    sig = inspect.signature(uml3_0_0_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CentralBufferNode)


def test_uml3_0_0_centralbuffernode_constructor_exists():
    assert callable(uml3_0_0_CentralBufferNode.__init__)


def test_uml3_0_0_centralbuffernode_constructor_args():
    sig = inspect.signature(uml3_0_0_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InterruptibleActivityRegion)


def test_uml3_0_0_interruptibleactivityregion_constructor_exists():
    assert callable(uml3_0_0_InterruptibleActivityRegion.__init__)


def test_uml3_0_0_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml3_0_0_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_controlnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ControlNode)


def test_uml3_0_0_controlnode_constructor_exists():
    assert callable(uml3_0_0_ControlNode.__init__)


def test_uml3_0_0_controlnode_constructor_args():
    sig = inspect.signature(uml3_0_0_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_executablenode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExecutableNode)


def test_uml3_0_0_executablenode_constructor_exists():
    assert callable(uml3_0_0_ExecutableNode.__init__)


def test_uml3_0_0_executablenode_constructor_args():
    sig = inspect.signature(uml3_0_0_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_action_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Action)


def test_uml3_0_0_action_constructor_exists():
    assert callable(uml3_0_0_Action.__init__)


def test_uml3_0_0_action_constructor_args():
    sig = inspect.signature(uml3_0_0_Action.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_outputpin_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_OutputPin)


def test_uml3_0_0_outputpin_constructor_exists():
    assert callable(uml3_0_0_OutputPin.__init__)


def test_uml3_0_0_outputpin_constructor_args():
    sig = inspect.signature(uml3_0_0_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_inputpin_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InputPin)


def test_uml3_0_0_inputpin_constructor_exists():
    assert callable(uml3_0_0_InputPin.__init__)


def test_uml3_0_0_inputpin_constructor_args():
    sig = inspect.signature(uml3_0_0_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_readselfaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadSelfAction)


def test_uml3_0_0_readselfaction_constructor_exists():
    assert callable(uml3_0_0_ReadSelfAction.__init__)


def test_uml3_0_0_readselfaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CreateObjectAction)


def test_uml3_0_0_createobjectaction_constructor_exists():
    assert callable(uml3_0_0_CreateObjectAction.__init__)


def test_uml3_0_0_createobjectaction_constructor_args():
    sig = inspect.signature(uml3_0_0_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_replyaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReplyAction)


def test_uml3_0_0_replyaction_constructor_exists():
    assert callable(uml3_0_0_ReplyAction.__init__)


def test_uml3_0_0_replyaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_RaiseExceptionAction)


def test_uml3_0_0_raiseexceptionaction_constructor_exists():
    assert callable(uml3_0_0_RaiseExceptionAction.__init__)


def test_uml3_0_0_raiseexceptionaction_constructor_args():
    sig = inspect.signature(uml3_0_0_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_variableaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_VariableAction)


def test_uml3_0_0_variableaction_constructor_exists():
    assert callable(uml3_0_0_VariableAction.__init__)


def test_uml3_0_0_variableaction_constructor_args():
    sig = inspect.signature(uml3_0_0_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_readextentaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadExtentAction)


def test_uml3_0_0_readextentaction_constructor_exists():
    assert callable(uml3_0_0_ReadExtentAction.__init__)


def test_uml3_0_0_readextentaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_AcceptEventAction)


def test_uml3_0_0_accepteventaction_constructor_exists():
    assert callable(uml3_0_0_AcceptEventAction.__init__)


def test_uml3_0_0_accepteventaction_constructor_args():
    sig = inspect.signature(uml3_0_0_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_uml3_0_0_accepteventaction_has_isUnmarshall():
    assert hasattr(uml3_0_0_AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in uml3_0_0_AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadLinkObjectEndAction)


def test_uml3_0_0_readlinkobjectendaction_constructor_exists():
    assert callable(uml3_0_0_ReadLinkObjectEndAction.__init__)


def test_uml3_0_0_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReclassifyObjectAction)


def test_uml3_0_0_reclassifyobjectaction_constructor_exists():
    assert callable(uml3_0_0_ReclassifyObjectAction.__init__)


def test_uml3_0_0_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3_0_0_reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(uml3_0_0_ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in uml3_0_0_ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_UnmarshallAction)


def test_uml3_0_0_unmarshallaction_constructor_exists():
    assert callable(uml3_0_0_UnmarshallAction.__init__)


def test_uml3_0_0_unmarshallaction_constructor_args():
    sig = inspect.signature(uml3_0_0_UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_linkaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LinkAction)


def test_uml3_0_0_linkaction_constructor_exists():
    assert callable(uml3_0_0_LinkAction.__init__)


def test_uml3_0_0_linkaction_constructor_args():
    sig = inspect.signature(uml3_0_0_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_invocationaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InvocationAction)


def test_uml3_0_0_invocationaction_constructor_exists():
    assert callable(uml3_0_0_InvocationAction.__init__)


def test_uml3_0_0_invocationaction_constructor_args():
    sig = inspect.signature(uml3_0_0_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadLinkObjectEndQualifierAction)


def test_uml3_0_0_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml3_0_0_ReadLinkObjectEndQualifierAction.__init__)


def test_uml3_0_0_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StartClassifierBehaviorAction)


def test_uml3_0_0_startclassifierbehavioraction_constructor_exists():
    assert callable(uml3_0_0_StartClassifierBehaviorAction.__init__)


def test_uml3_0_0_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml3_0_0_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_reduceaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReduceAction)


def test_uml3_0_0_reduceaction_constructor_exists():
    assert callable(uml3_0_0_ReduceAction.__init__)


def test_uml3_0_0_reduceaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_uml3_0_0_reduceaction_has_isOrdered():
    assert hasattr(uml3_0_0_ReduceAction, "isOrdered")
    descriptor = None
    for klass in uml3_0_0_ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ReadIsClassifiedObjectAction)


def test_uml3_0_0_readisclassifiedobjectaction_constructor_exists():
    assert callable(uml3_0_0_ReadIsClassifiedObjectAction.__init__)


def test_uml3_0_0_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDirect" in params, "Missing parameter 'isDirect'"

def test_uml3_0_0_readisclassifiedobjectaction_has_isDirect():
    assert hasattr(uml3_0_0_ReadIsClassifiedObjectAction, "isDirect")
    descriptor = None
    for klass in uml3_0_0_ReadIsClassifiedObjectAction.__mro__:
        if "isDirect" in klass.__dict__:
            descriptor = klass.__dict__["isDirect"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ClearAssociationAction)


def test_uml3_0_0_clearassociationaction_constructor_exists():
    assert callable(uml3_0_0_ClearAssociationAction.__init__)


def test_uml3_0_0_clearassociationaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ValueSpecificationAction)


def test_uml3_0_0_valuespecificationaction_constructor_exists():
    assert callable(uml3_0_0_ValueSpecificationAction.__init__)


def test_uml3_0_0_valuespecificationaction_constructor_args():
    sig = inspect.signature(uml3_0_0_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DestroyObjectAction)


def test_uml3_0_0_destroyobjectaction_constructor_exists():
    assert callable(uml3_0_0_DestroyObjectAction.__init__)


def test_uml3_0_0_destroyobjectaction_constructor_args():
    sig = inspect.signature(uml3_0_0_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyLinks" in params, "Missing parameter 'isDestroyLinks'"
    assert "isDestroyOwnedObjects" in params, "Missing parameter 'isDestroyOwnedObjects'"

def test_uml3_0_0_destroyobjectaction_has_isDestroyLinks():
    assert hasattr(uml3_0_0_DestroyObjectAction, "isDestroyLinks")
    descriptor = None
    for klass in uml3_0_0_DestroyObjectAction.__mro__:
        if "isDestroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyLinks"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_destroyobjectaction_has_isDestroyOwnedObjects():
    assert hasattr(uml3_0_0_DestroyObjectAction, "isDestroyOwnedObjects")
    descriptor = None
    for klass in uml3_0_0_DestroyObjectAction.__mro__:
        if "isDestroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StructuralFeatureAction)


def test_uml3_0_0_structuralfeatureaction_constructor_exists():
    assert callable(uml3_0_0_StructuralFeatureAction.__init__)


def test_uml3_0_0_structuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3_0_0_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TestIdentityAction)


def test_uml3_0_0_testidentityaction_constructor_exists():
    assert callable(uml3_0_0_TestIdentityAction.__init__)


def test_uml3_0_0_testidentityaction_constructor_args():
    sig = inspect.signature(uml3_0_0_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_OpaqueAction)


def test_uml3_0_0_opaqueaction_constructor_exists():
    assert callable(uml3_0_0_OpaqueAction.__init__)


def test_uml3_0_0_opaqueaction_constructor_args():
    sig = inspect.signature(uml3_0_0_OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_uml3_0_0_opaqueaction_has_language():
    assert hasattr(uml3_0_0_OpaqueAction, "language")
    descriptor = None
    for klass in uml3_0_0_OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_opaqueaction_has_body():
    assert hasattr(uml3_0_0_OpaqueAction, "body")
    descriptor = None
    for klass in uml3_0_0_OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_FunctionBehavior)


def test_uml3_0_0_functionbehavior_constructor_exists():
    assert callable(uml3_0_0_FunctionBehavior.__init__)


def test_uml3_0_0_functionbehavior_constructor_args():
    sig = inspect.signature(uml3_0_0_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_literalstring_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LiteralString)


def test_uml3_0_0_literalstring_constructor_exists():
    assert callable(uml3_0_0_LiteralString.__init__)


def test_uml3_0_0_literalstring_constructor_args():
    sig = inspect.signature(uml3_0_0_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3_0_0_literalstring_has_value():
    assert hasattr(uml3_0_0_LiteralString, "value")
    descriptor = None
    for klass in uml3_0_0_LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LiteralUnlimitedNatural)


def test_uml3_0_0_literalunlimitednatural_constructor_exists():
    assert callable(uml3_0_0_LiteralUnlimitedNatural.__init__)


def test_uml3_0_0_literalunlimitednatural_constructor_args():
    sig = inspect.signature(uml3_0_0_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3_0_0_literalunlimitednatural_has_value():
    assert hasattr(uml3_0_0_LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in uml3_0_0_LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_literalnull_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LiteralNull)


def test_uml3_0_0_literalnull_constructor_exists():
    assert callable(uml3_0_0_LiteralNull.__init__)


def test_uml3_0_0_literalnull_constructor_args():
    sig = inspect.signature(uml3_0_0_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_literalboolean_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LiteralBoolean)


def test_uml3_0_0_literalboolean_constructor_exists():
    assert callable(uml3_0_0_LiteralBoolean.__init__)


def test_uml3_0_0_literalboolean_constructor_args():
    sig = inspect.signature(uml3_0_0_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3_0_0_literalboolean_has_value():
    assert hasattr(uml3_0_0_LiteralBoolean, "value")
    descriptor = None
    for klass in uml3_0_0_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_literalinteger_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LiteralInteger)


def test_uml3_0_0_literalinteger_constructor_exists():
    assert callable(uml3_0_0_LiteralInteger.__init__)


def test_uml3_0_0_literalinteger_constructor_args():
    sig = inspect.signature(uml3_0_0_LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3_0_0_literalinteger_has_value():
    assert hasattr(uml3_0_0_LiteralInteger, "value")
    descriptor = None
    for klass in uml3_0_0_LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_EnumerationLiteral)


def test_uml3_0_0_enumerationliteral_constructor_exists():
    assert callable(uml3_0_0_EnumerationLiteral.__init__)


def test_uml3_0_0_enumerationliteral_constructor_args():
    sig = inspect.signature(uml3_0_0_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_primitivetype_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_PrimitiveType)


def test_uml3_0_0_primitivetype_constructor_exists():
    assert callable(uml3_0_0_PrimitiveType.__init__)


def test_uml3_0_0_primitivetype_constructor_args():
    sig = inspect.signature(uml3_0_0_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_enumeration_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Enumeration)


def test_uml3_0_0_enumeration_constructor_exists():
    assert callable(uml3_0_0_Enumeration.__init__)


def test_uml3_0_0_enumeration_constructor_args():
    sig = inspect.signature(uml3_0_0_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_templatesignature_is_not_abstract():
    assert not inspect.isabstract(TemplateSignature)


def test_templatesignature_constructor_exists():
    assert callable(TemplateSignature.__init__)


def test_templatesignature_constructor_args():
    sig = inspect.signature(TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ClassifierTemplateParameter)


def test_uml3_0_0_classifiertemplateparameter_constructor_exists():
    assert callable(uml3_0_0_ClassifierTemplateParameter.__init__)


def test_uml3_0_0_classifiertemplateparameter_constructor_args():
    sig = inspect.signature(uml3_0_0_ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"

def test_uml3_0_0_classifiertemplateparameter_has_allowSubstitutable():
    assert hasattr(uml3_0_0_ClassifierTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in uml3_0_0_ClassifierTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ConnectableElementTemplateParameter)


def test_uml3_0_0_connectableelementtemplateparameter_constructor_exists():
    assert callable(uml3_0_0_ConnectableElementTemplateParameter.__init__)


def test_uml3_0_0_connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(uml3_0_0_ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_OperationTemplateParameter)


def test_uml3_0_0_operationtemplateparameter_constructor_exists():
    assert callable(uml3_0_0_OperationTemplateParameter.__init__)


def test_uml3_0_0_operationtemplateparameter_constructor_args():
    sig = inspect.signature(uml3_0_0_OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_EncapsulatedClassifier)


def test_uml3_0_0_encapsulatedclassifier_constructor_exists():
    assert callable(uml3_0_0_EncapsulatedClassifier.__init__)


def test_uml3_0_0_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml3_0_0_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_model_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Model)


def test_uml3_0_0_model_constructor_exists():
    assert callable(uml3_0_0_Model.__init__)


def test_uml3_0_0_model_constructor_args():
    sig = inspect.signature(uml3_0_0_Model.__init__)
    params = list(sig.parameters.keys())
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"

def test_uml3_0_0_model_has_viewpoint():
    assert hasattr(uml3_0_0_Model, "viewpoint")
    descriptor = None
    for klass in uml3_0_0_Model.__mro__:
        if "viewpoint" in klass.__dict__:
            descriptor = klass.__dict__["viewpoint"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_profile_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Profile)


def test_uml3_0_0_profile_constructor_exists():
    assert callable(uml3_0_0_Profile.__init__)


def test_uml3_0_0_profile_constructor_args():
    sig = inspect.signature(uml3_0_0_Profile.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_communicationpath_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CommunicationPath)


def test_uml3_0_0_communicationpath_constructor_exists():
    assert callable(uml3_0_0_CommunicationPath.__init__)


def test_uml3_0_0_communicationpath_constructor_args():
    sig = inspect.signature(uml3_0_0_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ConnectionPointReference)


def test_uml3_0_0_connectionpointreference_constructor_exists():
    assert callable(uml3_0_0_ConnectionPointReference.__init__)


def test_uml3_0_0_connectionpointreference_constructor_args():
    sig = inspect.signature(uml3_0_0_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_extensionend_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExtensionEnd)


def test_uml3_0_0_extensionend_constructor_exists():
    assert callable(uml3_0_0_ExtensionEnd.__init__)


def test_uml3_0_0_extensionend_constructor_args():
    sig = inspect.signature(uml3_0_0_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_port_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Port)


def test_uml3_0_0_port_constructor_exists():
    assert callable(uml3_0_0_Port.__init__)


def test_uml3_0_0_port_constructor_args():
    sig = inspect.signature(uml3_0_0_Port.__init__)
    params = list(sig.parameters.keys())
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"
    assert "isService" in params, "Missing parameter 'isService'"

def test_uml3_0_0_port_has_isBehavior():
    assert hasattr(uml3_0_0_Port, "isBehavior")
    descriptor = None
    for klass in uml3_0_0_Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_port_has_isService():
    assert hasattr(uml3_0_0_Port, "isService")
    descriptor = None
    for klass in uml3_0_0_Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_pseudostate_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Pseudostate)


def test_uml3_0_0_pseudostate_constructor_exists():
    assert callable(uml3_0_0_Pseudostate.__init__)


def test_uml3_0_0_pseudostate_constructor_args():
    sig = inspect.signature(uml3_0_0_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml3_0_0_pseudostate_has_kind():
    assert hasattr(uml3_0_0_Pseudostate, "kind")
    descriptor = None
    for klass in uml3_0_0_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_OpaqueBehavior)


def test_uml3_0_0_opaquebehavior_constructor_exists():
    assert callable(uml3_0_0_OpaqueBehavior.__init__)


def test_uml3_0_0_opaquebehavior_constructor_args():
    sig = inspect.signature(uml3_0_0_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_uml3_0_0_opaquebehavior_has_language():
    assert hasattr(uml3_0_0_OpaqueBehavior, "language")
    descriptor = None
    for klass in uml3_0_0_OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_opaquebehavior_has_body():
    assert hasattr(uml3_0_0_OpaqueBehavior, "body")
    descriptor = None
    for klass in uml3_0_0_OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_interaction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Interaction)


def test_uml3_0_0_interaction_constructor_exists():
    assert callable(uml3_0_0_Interaction.__init__)


def test_uml3_0_0_interaction_constructor_args():
    sig = inspect.signature(uml3_0_0_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_activity_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Activity)


def test_uml3_0_0_activity_constructor_exists():
    assert callable(uml3_0_0_Activity.__init__)


def test_uml3_0_0_activity_constructor_args():
    sig = inspect.signature(uml3_0_0_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml3_0_0_activity_has_isSingleExecution():
    assert hasattr(uml3_0_0_Activity, "isSingleExecution")
    descriptor = None
    for klass in uml3_0_0_Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_activity_has_isReadOnly():
    assert hasattr(uml3_0_0_Activity, "isReadOnly")
    descriptor = None
    for klass in uml3_0_0_Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_statemachine_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StateMachine)


def test_uml3_0_0_statemachine_constructor_exists():
    assert callable(uml3_0_0_StateMachine.__init__)


def test_uml3_0_0_statemachine_constructor_args():
    sig = inspect.signature(uml3_0_0_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ProtocolStateMachine)


def test_uml3_0_0_protocolstatemachine_constructor_exists():
    assert callable(uml3_0_0_ProtocolStateMachine.__init__)


def test_uml3_0_0_protocolstatemachine_constructor_args():
    sig = inspect.signature(uml3_0_0_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_extension_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Extension)


def test_uml3_0_0_extension_constructor_exists():
    assert callable(uml3_0_0_Extension.__init__)


def test_uml3_0_0_extension_constructor_args():
    sig = inspect.signature(uml3_0_0_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_uml3_0_0_extension_has_isRequired():
    assert hasattr(uml3_0_0_Extension, "isRequired")
    descriptor = None
    for klass in uml3_0_0_Extension.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_actor_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Actor)


def test_uml3_0_0_actor_constructor_exists():
    assert callable(uml3_0_0_Actor.__init__)


def test_uml3_0_0_actor_constructor_args():
    sig = inspect.signature(uml3_0_0_Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_collaboration_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Collaboration)


def test_uml3_0_0_collaboration_constructor_exists():
    assert callable(uml3_0_0_Collaboration.__init__)


def test_uml3_0_0_collaboration_constructor_args():
    sig = inspect.signature(uml3_0_0_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_associationclass_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_AssociationClass)


def test_uml3_0_0_associationclass_constructor_exists():
    assert callable(uml3_0_0_AssociationClass.__init__)


def test_uml3_0_0_associationclass_constructor_args():
    sig = inspect.signature(uml3_0_0_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_stereotype_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Stereotype)


def test_uml3_0_0_stereotype_constructor_exists():
    assert callable(uml3_0_0_Stereotype.__init__)


def test_uml3_0_0_stereotype_constructor_args():
    sig = inspect.signature(uml3_0_0_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_component_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Component)


def test_uml3_0_0_component_constructor_exists():
    assert callable(uml3_0_0_Component.__init__)


def test_uml3_0_0_component_constructor_args():
    sig = inspect.signature(uml3_0_0_Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"

def test_uml3_0_0_component_has_isIndirectlyInstantiated():
    assert hasattr(uml3_0_0_Component, "isIndirectlyInstantiated")
    descriptor = None
    for klass in uml3_0_0_Component.__mro__:
        if "isIndirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["isIndirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_connector_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Connector)


def test_uml3_0_0_connector_constructor_exists():
    assert callable(uml3_0_0_Connector.__init__)


def test_uml3_0_0_connector_constructor_args():
    sig = inspect.signature(uml3_0_0_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml3_0_0_connector_has_kind():
    assert hasattr(uml3_0_0_Connector, "kind")
    descriptor = None
    for klass in uml3_0_0_Connector.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_reception_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Reception)


def test_uml3_0_0_reception_constructor_exists():
    assert callable(uml3_0_0_Reception.__init__)


def test_uml3_0_0_reception_constructor_args():
    sig = inspect.signature(uml3_0_0_Reception.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DeploymentSpecification)


def test_uml3_0_0_deploymentspecification_constructor_exists():
    assert callable(uml3_0_0_DeploymentSpecification.__init__)


def test_uml3_0_0_deploymentspecification_constructor_args():
    sig = inspect.signature(uml3_0_0_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"

def test_uml3_0_0_deploymentspecification_has_executionLocation():
    assert hasattr(uml3_0_0_DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in uml3_0_0_DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_deploymentspecification_has_deploymentLocation():
    assert hasattr(uml3_0_0_DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in uml3_0_0_DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_class_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Class)


def test_uml3_0_0_class_constructor_exists():
    assert callable(uml3_0_0_Class.__init__)


def test_uml3_0_0_class_constructor_args():
    sig = inspect.signature(uml3_0_0_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml3_0_0_class_has_isActive():
    assert hasattr(uml3_0_0_Class, "isActive")
    descriptor = None
    for klass in uml3_0_0_Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_node_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Node)


def test_uml3_0_0_node_constructor_exists():
    assert callable(uml3_0_0_Node.__init__)


def test_uml3_0_0_node_constructor_args():
    sig = inspect.signature(uml3_0_0_Node.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_literalspecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LiteralSpecification)


def test_uml3_0_0_literalspecification_constructor_exists():
    assert callable(uml3_0_0_LiteralSpecification.__init__)


def test_uml3_0_0_literalspecification_constructor_args():
    sig = inspect.signature(uml3_0_0_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_interval_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Interval)


def test_uml3_0_0_interval_constructor_exists():
    assert callable(uml3_0_0_Interval.__init__)


def test_uml3_0_0_interval_constructor_args():
    sig = inspect.signature(uml3_0_0_Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_timeexpression_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TimeExpression)


def test_uml3_0_0_timeexpression_constructor_exists():
    assert callable(uml3_0_0_TimeExpression.__init__)


def test_uml3_0_0_timeexpression_constructor_args():
    sig = inspect.signature(uml3_0_0_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_duration_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Duration)


def test_uml3_0_0_duration_constructor_exists():
    assert callable(uml3_0_0_Duration.__init__)


def test_uml3_0_0_duration_constructor_args():
    sig = inspect.signature(uml3_0_0_Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_expression_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Expression)


def test_uml3_0_0_expression_constructor_exists():
    assert callable(uml3_0_0_Expression.__init__)


def test_uml3_0_0_expression_constructor_args():
    sig = inspect.signature(uml3_0_0_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_uml3_0_0_expression_has_symbol():
    assert hasattr(uml3_0_0_Expression, "symbol")
    descriptor = None
    for klass in uml3_0_0_Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_instancevalue_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InstanceValue)


def test_uml3_0_0_instancevalue_constructor_exists():
    assert callable(uml3_0_0_InstanceValue.__init__)


def test_uml3_0_0_instancevalue_constructor_args():
    sig = inspect.signature(uml3_0_0_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_OpaqueExpression)


def test_uml3_0_0_opaqueexpression_constructor_exists():
    assert callable(uml3_0_0_OpaqueExpression.__init__)


def test_uml3_0_0_opaqueexpression_constructor_args():
    sig = inspect.signature(uml3_0_0_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml3_0_0_opaqueexpression_has_body():
    assert hasattr(uml3_0_0_OpaqueExpression, "body")
    descriptor = None
    for klass in uml3_0_0_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_opaqueexpression_has_language():
    assert hasattr(uml3_0_0_OpaqueExpression, "language")
    descriptor = None
    for klass in uml3_0_0_OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_deployment_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Deployment)


def test_uml3_0_0_deployment_constructor_exists():
    assert callable(uml3_0_0_Deployment.__init__)


def test_uml3_0_0_deployment_constructor_args():
    sig = inspect.signature(uml3_0_0_Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_usage_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Usage)


def test_uml3_0_0_usage_constructor_exists():
    assert callable(uml3_0_0_Usage.__init__)


def test_uml3_0_0_usage_constructor_args():
    sig = inspect.signature(uml3_0_0_Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_abstraction_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Abstraction)


def test_uml3_0_0_abstraction_constructor_exists():
    assert callable(uml3_0_0_Abstraction.__init__)


def test_uml3_0_0_abstraction_constructor_args():
    sig = inspect.signature(uml3_0_0_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_manifestation_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Manifestation)


def test_uml3_0_0_manifestation_constructor_exists():
    assert callable(uml3_0_0_Manifestation.__init__)


def test_uml3_0_0_manifestation_constructor_args():
    sig = inspect.signature(uml3_0_0_Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_realization_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Realization)


def test_uml3_0_0_realization_constructor_exists():
    assert callable(uml3_0_0_Realization.__init__)


def test_uml3_0_0_realization_constructor_args():
    sig = inspect.signature(uml3_0_0_Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_sendoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_SendOperationEvent)


def test_uml3_0_0_sendoperationevent_constructor_exists():
    assert callable(uml3_0_0_SendOperationEvent.__init__)


def test_uml3_0_0_sendoperationevent_constructor_args():
    sig = inspect.signature(uml3_0_0_SendOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_pin_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Pin)


def test_uml3_0_0_pin_constructor_exists():
    assert callable(uml3_0_0_Pin.__init__)


def test_uml3_0_0_pin_constructor_args():
    sig = inspect.signature(uml3_0_0_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_uml3_0_0_pin_has_isControl():
    assert hasattr(uml3_0_0_Pin, "isControl")
    descriptor = None
    for klass in uml3_0_0_Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_connectorend_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ConnectorEnd)


def test_uml3_0_0_connectorend_constructor_exists():
    assert callable(uml3_0_0_ConnectorEnd.__init__)


def test_uml3_0_0_connectorend_constructor_args():
    sig = inspect.signature(uml3_0_0_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_timeevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TimeEvent)


def test_uml3_0_0_timeevent_constructor_exists():
    assert callable(uml3_0_0_TimeEvent.__init__)


def test_uml3_0_0_timeevent_constructor_args():
    sig = inspect.signature(uml3_0_0_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_uml3_0_0_timeevent_has_isRelative():
    assert hasattr(uml3_0_0_TimeEvent, "isRelative")
    descriptor = None
    for klass in uml3_0_0_TimeEvent.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_changeevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ChangeEvent)


def test_uml3_0_0_changeevent_constructor_exists():
    assert callable(uml3_0_0_ChangeEvent.__init__)


def test_uml3_0_0_changeevent_constructor_args():
    sig = inspect.signature(uml3_0_0_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_destructionevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DestructionEvent)


def test_uml3_0_0_destructionevent_constructor_exists():
    assert callable(uml3_0_0_DestructionEvent.__init__)


def test_uml3_0_0_destructionevent_constructor_args():
    sig = inspect.signature(uml3_0_0_DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_messageevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_MessageEvent)


def test_uml3_0_0_messageevent_constructor_exists():
    assert callable(uml3_0_0_MessageEvent.__init__)


def test_uml3_0_0_messageevent_constructor_args():
    sig = inspect.signature(uml3_0_0_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_creationevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CreationEvent)


def test_uml3_0_0_creationevent_constructor_exists():
    assert callable(uml3_0_0_CreationEvent.__init__)


def test_uml3_0_0_creationevent_constructor_args():
    sig = inspect.signature(uml3_0_0_CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_variable_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Variable)


def test_uml3_0_0_variable_constructor_exists():
    assert callable(uml3_0_0_Variable.__init__)


def test_uml3_0_0_variable_constructor_args():
    sig = inspect.signature(uml3_0_0_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_executionevent_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExecutionEvent)


def test_uml3_0_0_executionevent_constructor_exists():
    assert callable(uml3_0_0_ExecutionEvent.__init__)


def test_uml3_0_0_executionevent_constructor_args():
    sig = inspect.signature(uml3_0_0_ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_behavior_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Behavior)


def test_uml3_0_0_behavior_constructor_exists():
    assert callable(uml3_0_0_Behavior.__init__)


def test_uml3_0_0_behavior_constructor_args():
    sig = inspect.signature(uml3_0_0_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_uml3_0_0_behavior_has_isReentrant():
    assert hasattr(uml3_0_0_Behavior, "isReentrant")
    descriptor = None
    for klass in uml3_0_0_Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_BehaviorExecutionSpecification)


def test_uml3_0_0_behaviorexecutionspecification_constructor_exists():
    assert callable(uml3_0_0_BehaviorExecutionSpecification.__init__)


def test_uml3_0_0_behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml3_0_0_BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_parameter_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Parameter)


def test_uml3_0_0_parameter_constructor_exists():
    assert callable(uml3_0_0_Parameter.__init__)


def test_uml3_0_0_parameter_constructor_args():
    sig = inspect.signature(uml3_0_0_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isStream" in params, "Missing parameter 'isStream'"

def test_uml3_0_0_parameter_has_default():
    assert hasattr(uml3_0_0_Parameter, "default")
    descriptor = None
    for klass in uml3_0_0_Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_parameter_has_effect():
    assert hasattr(uml3_0_0_Parameter, "effect")
    descriptor = None
    for klass in uml3_0_0_Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_parameter_has_isException():
    assert hasattr(uml3_0_0_Parameter, "isException")
    descriptor = None
    for klass in uml3_0_0_Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_parameter_has_direction():
    assert hasattr(uml3_0_0_Parameter, "direction")
    descriptor = None
    for klass in uml3_0_0_Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_parameter_has_isStream():
    assert hasattr(uml3_0_0_Parameter, "isStream")
    descriptor = None
    for klass in uml3_0_0_Parameter.__mro__:
        if "isStream" in klass.__dict__:
            descriptor = klass.__dict__["isStream"]
            break
    assert isinstance(descriptor, property)



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_componentrealization_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ComponentRealization)


def test_uml3_0_0_componentrealization_constructor_exists():
    assert callable(uml3_0_0_ComponentRealization.__init__)


def test_uml3_0_0_componentrealization_constructor_args():
    sig = inspect.signature(uml3_0_0_ComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_interfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InterfaceRealization)


def test_uml3_0_0_interfacerealization_constructor_exists():
    assert callable(uml3_0_0_InterfaceRealization.__init__)


def test_uml3_0_0_interfacerealization_constructor_args():
    sig = inspect.signature(uml3_0_0_InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_property_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Property)


def test_uml3_0_0_property_constructor_exists():
    assert callable(uml3_0_0_Property.__init__)


def test_uml3_0_0_property_constructor_args():
    sig = inspect.signature(uml3_0_0_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_uml3_0_0_property_has_isComposite():
    assert hasattr(uml3_0_0_Property, "isComposite")
    descriptor = None
    for klass in uml3_0_0_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_property_has_default():
    assert hasattr(uml3_0_0_Property, "default")
    descriptor = None
    for klass in uml3_0_0_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_property_has_isDerivedUnion():
    assert hasattr(uml3_0_0_Property, "isDerivedUnion")
    descriptor = None
    for klass in uml3_0_0_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_property_has_isDerived():
    assert hasattr(uml3_0_0_Property, "isDerived")
    descriptor = None
    for klass in uml3_0_0_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_property_has_aggregation():
    assert hasattr(uml3_0_0_Property, "aggregation")
    descriptor = None
    for klass in uml3_0_0_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_BehavioredClassifier)


def test_uml3_0_0_behavioredclassifier_constructor_exists():
    assert callable(uml3_0_0_BehavioredClassifier.__init__)


def test_uml3_0_0_behavioredclassifier_constructor_args():
    sig = inspect.signature(uml3_0_0_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_informationitem_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InformationItem)


def test_uml3_0_0_informationitem_constructor_exists():
    assert callable(uml3_0_0_InformationItem.__init__)


def test_uml3_0_0_informationitem_constructor_args():
    sig = inspect.signature(uml3_0_0_InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StructuredClassifier)


def test_uml3_0_0_structuredclassifier_constructor_exists():
    assert callable(uml3_0_0_StructuredClassifier.__init__)


def test_uml3_0_0_structuredclassifier_constructor_args():
    sig = inspect.signature(uml3_0_0_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_datatype_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DataType)


def test_uml3_0_0_datatype_constructor_exists():
    assert callable(uml3_0_0_DataType.__init__)


def test_uml3_0_0_datatype_constructor_args():
    sig = inspect.signature(uml3_0_0_DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_interface_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Interface)


def test_uml3_0_0_interface_constructor_exists():
    assert callable(uml3_0_0_Interface.__init__)


def test_uml3_0_0_interface_constructor_args():
    sig = inspect.signature(uml3_0_0_Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_signal_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Signal)


def test_uml3_0_0_signal_constructor_exists():
    assert callable(uml3_0_0_Signal.__init__)


def test_uml3_0_0_signal_constructor_args():
    sig = inspect.signature(uml3_0_0_Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_artifact_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Artifact)


def test_uml3_0_0_artifact_constructor_exists():
    assert callable(uml3_0_0_Artifact.__init__)


def test_uml3_0_0_artifact_constructor_args():
    sig = inspect.signature(uml3_0_0_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_uml3_0_0_artifact_has_fileName():
    assert hasattr(uml3_0_0_Artifact, "fileName")
    descriptor = None
    for klass in uml3_0_0_Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_usecase_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_UseCase)


def test_uml3_0_0_usecase_constructor_exists():
    assert callable(uml3_0_0_UseCase.__init__)


def test_uml3_0_0_usecase_constructor_args():
    sig = inspect.signature(uml3_0_0_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_substitution_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Substitution)


def test_uml3_0_0_substitution_constructor_exists():
    assert callable(uml3_0_0_Substitution.__init__)


def test_uml3_0_0_substitution_constructor_args():
    sig = inspect.signature(uml3_0_0_Substitution.__init__)
    params = list(sig.parameters.keys())



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



def test_uml3_0_0_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExtensionPoint)


def test_uml3_0_0_extensionpoint_constructor_exists():
    assert callable(uml3_0_0_ExtensionPoint.__init__)


def test_uml3_0_0_extensionpoint_constructor_args():
    sig = inspect.signature(uml3_0_0_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_activitynode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActivityNode)


def test_uml3_0_0_activitynode_constructor_exists():
    assert callable(uml3_0_0_ActivityNode.__init__)


def test_uml3_0_0_activitynode_constructor_args():
    sig = inspect.signature(uml3_0_0_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_RedefinableTemplateSignature)


def test_uml3_0_0_redefinabletemplatesignature_constructor_exists():
    assert callable(uml3_0_0_RedefinableTemplateSignature.__init__)


def test_uml3_0_0_redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(uml3_0_0_RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_activityedge_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActivityEdge)


def test_uml3_0_0_activityedge_constructor_exists():
    assert callable(uml3_0_0_ActivityEdge.__init__)


def test_uml3_0_0_activityedge_constructor_args():
    sig = inspect.signature(uml3_0_0_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_feature_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Feature)


def test_uml3_0_0_feature_constructor_exists():
    assert callable(uml3_0_0_Feature.__init__)


def test_uml3_0_0_feature_constructor_args():
    sig = inspect.signature(uml3_0_0_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml3_0_0_feature_has_isStatic():
    assert hasattr(uml3_0_0_Feature, "isStatic")
    descriptor = None
    for klass in uml3_0_0_Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_objectnode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ObjectNode)


def test_uml3_0_0_objectnode_constructor_exists():
    assert callable(uml3_0_0_ObjectNode.__init__)


def test_uml3_0_0_objectnode_constructor_args():
    sig = inspect.signature(uml3_0_0_ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"

def test_uml3_0_0_objectnode_has_ordering():
    assert hasattr(uml3_0_0_ObjectNode, "ordering")
    descriptor = None
    for klass in uml3_0_0_ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_objectnode_has_isControlType():
    assert hasattr(uml3_0_0_ObjectNode, "isControlType")
    descriptor = None
    for klass in uml3_0_0_ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StructuralFeature)


def test_uml3_0_0_structuralfeature_constructor_exists():
    assert callable(uml3_0_0_StructuralFeature.__init__)


def test_uml3_0_0_structuralfeature_constructor_args():
    sig = inspect.signature(uml3_0_0_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml3_0_0_structuralfeature_has_isReadOnly():
    assert hasattr(uml3_0_0_StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in uml3_0_0_StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_generalization_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Generalization)


def test_uml3_0_0_generalization_constructor_exists():
    assert callable(uml3_0_0_Generalization.__init__)


def test_uml3_0_0_generalization_constructor_args():
    sig = inspect.signature(uml3_0_0_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_uml3_0_0_generalization_has_isSubstitutable():
    assert hasattr(uml3_0_0_Generalization, "isSubstitutable")
    descriptor = None
    for klass in uml3_0_0_Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_templatebinding_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TemplateBinding)


def test_uml3_0_0_templatebinding_constructor_exists():
    assert callable(uml3_0_0_TemplateBinding.__init__)


def test_uml3_0_0_templatebinding_constructor_args():
    sig = inspect.signature(uml3_0_0_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ProtocolConformance)


def test_uml3_0_0_protocolconformance_constructor_exists():
    assert callable(uml3_0_0_ProtocolConformance.__init__)


def test_uml3_0_0_protocolconformance_constructor_args():
    sig = inspect.signature(uml3_0_0_ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_packageimport_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_PackageImport)


def test_uml3_0_0_packageimport_constructor_exists():
    assert callable(uml3_0_0_PackageImport.__init__)


def test_uml3_0_0_packageimport_constructor_args():
    sig = inspect.signature(uml3_0_0_PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml3_0_0_packageimport_has_visibility():
    assert hasattr(uml3_0_0_PackageImport, "visibility")
    descriptor = None
    for klass in uml3_0_0_PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_elementimport_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ElementImport)


def test_uml3_0_0_elementimport_constructor_exists():
    assert callable(uml3_0_0_ElementImport.__init__)


def test_uml3_0_0_elementimport_constructor_args():
    sig = inspect.signature(uml3_0_0_ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml3_0_0_elementimport_has_alias():
    assert hasattr(uml3_0_0_ElementImport, "alias")
    descriptor = None
    for klass in uml3_0_0_ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_elementimport_has_visibility():
    assert hasattr(uml3_0_0_ElementImport, "visibility")
    descriptor = None
    for klass in uml3_0_0_ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_association_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Association)


def test_uml3_0_0_association_constructor_exists():
    assert callable(uml3_0_0_Association.__init__)


def test_uml3_0_0_association_constructor_args():
    sig = inspect.signature(uml3_0_0_Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml3_0_0_association_has_isDerived():
    assert hasattr(uml3_0_0_Association, "isDerived")
    descriptor = None
    for klass in uml3_0_0_Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DirectedRelationship)


def test_uml3_0_0_directedrelationship_constructor_exists():
    assert callable(uml3_0_0_DirectedRelationship.__init__)


def test_uml3_0_0_directedrelationship_constructor_args():
    sig = inspect.signature(uml3_0_0_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_connectableelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ConnectableElement)


def test_uml3_0_0_connectableelement_constructor_exists():
    assert callable(uml3_0_0_ConnectableElement.__init__)


def test_uml3_0_0_connectableelement_constructor_args():
    sig = inspect.signature(uml3_0_0_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_collaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_CollaborationUse)


def test_uml3_0_0_collaborationuse_constructor_exists():
    assert callable(uml3_0_0_CollaborationUse.__init__)


def test_uml3_0_0_collaborationuse_constructor_args():
    sig = inspect.signature(uml3_0_0_CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_activitypartition_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActivityPartition)


def test_uml3_0_0_activitypartition_constructor_exists():
    assert callable(uml3_0_0_ActivityPartition.__init__)


def test_uml3_0_0_activitypartition_constructor_args():
    sig = inspect.signature(uml3_0_0_ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "isDimension" in params, "Missing parameter 'isDimension'"

def test_uml3_0_0_activitypartition_has_isExternal():
    assert hasattr(uml3_0_0_ActivityPartition, "isExternal")
    descriptor = None
    for klass in uml3_0_0_ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_activitypartition_has_isDimension():
    assert hasattr(uml3_0_0_ActivityPartition, "isDimension")
    descriptor = None
    for klass in uml3_0_0_ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_generalordering_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_GeneralOrdering)


def test_uml3_0_0_generalordering_constructor_exists():
    assert callable(uml3_0_0_GeneralOrdering.__init__)


def test_uml3_0_0_generalordering_constructor_args():
    sig = inspect.signature(uml3_0_0_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_vertex_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Vertex)


def test_uml3_0_0_vertex_constructor_exists():
    assert callable(uml3_0_0_Vertex.__init__)


def test_uml3_0_0_vertex_constructor_args():
    sig = inspect.signature(uml3_0_0_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_typedelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TypedElement)


def test_uml3_0_0_typedelement_constructor_exists():
    assert callable(uml3_0_0_TypedElement.__init__)


def test_uml3_0_0_typedelement_constructor_args():
    sig = inspect.signature(uml3_0_0_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_extend_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Extend)


def test_uml3_0_0_extend_constructor_exists():
    assert callable(uml3_0_0_Extend.__init__)


def test_uml3_0_0_extend_constructor_args():
    sig = inspect.signature(uml3_0_0_Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_RedefinableElement)


def test_uml3_0_0_redefinableelement_constructor_exists():
    assert callable(uml3_0_0_RedefinableElement.__init__)


def test_uml3_0_0_redefinableelement_constructor_args():
    sig = inspect.signature(uml3_0_0_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_uml3_0_0_redefinableelement_has_isLeaf():
    assert hasattr(uml3_0_0_RedefinableElement, "isLeaf")
    descriptor = None
    for klass in uml3_0_0_RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DeploymentTarget)


def test_uml3_0_0_deploymenttarget_constructor_exists():
    assert callable(uml3_0_0_DeploymentTarget.__init__)


def test_uml3_0_0_deploymenttarget_constructor_args():
    sig = inspect.signature(uml3_0_0_DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_parameterset_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ParameterSet)


def test_uml3_0_0_parameterset_constructor_exists():
    assert callable(uml3_0_0_ParameterSet.__init__)


def test_uml3_0_0_parameterset_constructor_args():
    sig = inspect.signature(uml3_0_0_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_DeployedArtifact)


def test_uml3_0_0_deployedartifact_constructor_exists():
    assert callable(uml3_0_0_DeployedArtifact.__init__)


def test_uml3_0_0_deployedartifact_constructor_args():
    sig = inspect.signature(uml3_0_0_DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InteractionFragment)


def test_uml3_0_0_interactionfragment_constructor_exists():
    assert callable(uml3_0_0_InteractionFragment.__init__)


def test_uml3_0_0_interactionfragment_constructor_args():
    sig = inspect.signature(uml3_0_0_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_messageend_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_MessageEnd)


def test_uml3_0_0_messageend_constructor_exists():
    assert callable(uml3_0_0_MessageEnd.__init__)


def test_uml3_0_0_messageend_constructor_args():
    sig = inspect.signature(uml3_0_0_MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_trigger_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Trigger)


def test_uml3_0_0_trigger_constructor_exists():
    assert callable(uml3_0_0_Trigger.__init__)


def test_uml3_0_0_trigger_constructor_args():
    sig = inspect.signature(uml3_0_0_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_message_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Message)


def test_uml3_0_0_message_constructor_exists():
    assert callable(uml3_0_0_Message.__init__)


def test_uml3_0_0_message_constructor_args():
    sig = inspect.signature(uml3_0_0_Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageSort" in params, "Missing parameter 'messageSort'"
    assert "messageKind" in params, "Missing parameter 'messageKind'"

def test_uml3_0_0_message_has_messageSort():
    assert hasattr(uml3_0_0_Message, "messageSort")
    descriptor = None
    for klass in uml3_0_0_Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_message_has_messageKind():
    assert hasattr(uml3_0_0_Message, "messageKind")
    descriptor = None
    for klass in uml3_0_0_Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_namespace_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Namespace)


def test_uml3_0_0_namespace_constructor_exists():
    assert callable(uml3_0_0_Namespace.__init__)


def test_uml3_0_0_namespace_constructor_args():
    sig = inspect.signature(uml3_0_0_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_lifeline_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Lifeline)


def test_uml3_0_0_lifeline_constructor_exists():
    assert callable(uml3_0_0_Lifeline.__init__)


def test_uml3_0_0_lifeline_constructor_args():
    sig = inspect.signature(uml3_0_0_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_include_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Include)


def test_uml3_0_0_include_constructor_exists():
    assert callable(uml3_0_0_Include.__init__)


def test_uml3_0_0_include_constructor_args():
    sig = inspect.signature(uml3_0_0_Include.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_profileapplication_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ProfileApplication)


def test_uml3_0_0_profileapplication_constructor_exists():
    assert callable(uml3_0_0_ProfileApplication.__init__)


def test_uml3_0_0_profileapplication_constructor_args():
    sig = inspect.signature(uml3_0_0_ProfileApplication.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_uml3_0_0_profileapplication_has_isStrict():
    assert hasattr(uml3_0_0_ProfileApplication, "isStrict")
    descriptor = None
    for klass in uml3_0_0_ProfileApplication.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_PackageableElement)


def test_uml3_0_0_packageableelement_constructor_exists():
    assert callable(uml3_0_0_PackageableElement.__init__)


def test_uml3_0_0_packageableelement_constructor_args():
    sig = inspect.signature(uml3_0_0_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_packagemerge_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_PackageMerge)


def test_uml3_0_0_packagemerge_constructor_exists():
    assert callable(uml3_0_0_PackageMerge.__init__)


def test_uml3_0_0_packagemerge_constructor_args():
    sig = inspect.signature(uml3_0_0_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_stringexpression_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StringExpression)


def test_uml3_0_0_stringexpression_constructor_exists():
    assert callable(uml3_0_0_StringExpression.__init__)


def test_uml3_0_0_stringexpression_constructor_args():
    sig = inspect.signature(uml3_0_0_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_operation_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Operation)


def test_uml3_0_0_operation_constructor_exists():
    assert callable(uml3_0_0_Operation.__init__)


def test_uml3_0_0_operation_constructor_args():
    sig = inspect.signature(uml3_0_0_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_uml3_0_0_operation_has_lower():
    assert hasattr(uml3_0_0_Operation, "lower")
    descriptor = None
    for klass in uml3_0_0_Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_operation_has_upper():
    assert hasattr(uml3_0_0_Operation, "upper")
    descriptor = None
    for klass in uml3_0_0_Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_operation_has_isQuery():
    assert hasattr(uml3_0_0_Operation, "isQuery")
    descriptor = None
    for klass in uml3_0_0_Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_operation_has_isOrdered():
    assert hasattr(uml3_0_0_Operation, "isOrdered")
    descriptor = None
    for klass in uml3_0_0_Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_operation_has_isUnique():
    assert hasattr(uml3_0_0_Operation, "isUnique")
    descriptor = None
    for klass in uml3_0_0_Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_type_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Type)


def test_uml3_0_0_type_constructor_exists():
    assert callable(uml3_0_0_Type.__init__)


def test_uml3_0_0_type_constructor_args():
    sig = inspect.signature(uml3_0_0_Type.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_observation_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Observation)


def test_uml3_0_0_observation_constructor_exists():
    assert callable(uml3_0_0_Observation.__init__)


def test_uml3_0_0_observation_constructor_args():
    sig = inspect.signature(uml3_0_0_Observation.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_informationflow_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InformationFlow)


def test_uml3_0_0_informationflow_constructor_exists():
    assert callable(uml3_0_0_InformationFlow.__init__)


def test_uml3_0_0_informationflow_constructor_args():
    sig = inspect.signature(uml3_0_0_InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_instancespecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InstanceSpecification)


def test_uml3_0_0_instancespecification_constructor_exists():
    assert callable(uml3_0_0_InstanceSpecification.__init__)


def test_uml3_0_0_instancespecification_constructor_args():
    sig = inspect.signature(uml3_0_0_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_event_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Event)


def test_uml3_0_0_event_constructor_exists():
    assert callable(uml3_0_0_Event.__init__)


def test_uml3_0_0_event_constructor_args():
    sig = inspect.signature(uml3_0_0_Event.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_dependency_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Dependency)


def test_uml3_0_0_dependency_constructor_exists():
    assert callable(uml3_0_0_Dependency.__init__)


def test_uml3_0_0_dependency_constructor_args():
    sig = inspect.signature(uml3_0_0_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_valuespecification_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ValueSpecification)


def test_uml3_0_0_valuespecification_constructor_exists():
    assert callable(uml3_0_0_ValueSpecification.__init__)


def test_uml3_0_0_valuespecification_constructor_args():
    sig = inspect.signature(uml3_0_0_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_constraint_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Constraint)


def test_uml3_0_0_constraint_constructor_exists():
    assert callable(uml3_0_0_Constraint.__init__)


def test_uml3_0_0_constraint_constructor_args():
    sig = inspect.signature(uml3_0_0_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_generalizationset_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_GeneralizationSet)


def test_uml3_0_0_generalizationset_constructor_exists():
    assert callable(uml3_0_0_GeneralizationSet.__init__)


def test_uml3_0_0_generalizationset_constructor_args():
    sig = inspect.signature(uml3_0_0_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"
    assert "isCovering" in params, "Missing parameter 'isCovering'"

def test_uml3_0_0_generalizationset_has_isDisjoint():
    assert hasattr(uml3_0_0_GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in uml3_0_0_GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_generalizationset_has_isCovering():
    assert hasattr(uml3_0_0_GeneralizationSet, "isCovering")
    descriptor = None
    for klass in uml3_0_0_GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_transition_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Transition)


def test_uml3_0_0_transition_constructor_exists():
    assert callable(uml3_0_0_Transition.__init__)


def test_uml3_0_0_transition_constructor_args():
    sig = inspect.signature(uml3_0_0_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml3_0_0_transition_has_kind():
    assert hasattr(uml3_0_0_Transition, "kind")
    descriptor = None
    for klass in uml3_0_0_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_InteractionOperand)


def test_uml3_0_0_interactionoperand_constructor_exists():
    assert callable(uml3_0_0_InteractionOperand.__init__)


def test_uml3_0_0_interactionoperand_constructor_args():
    sig = inspect.signature(uml3_0_0_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_StructuredActivityNode)


def test_uml3_0_0_structuredactivitynode_constructor_exists():
    assert callable(uml3_0_0_StructuredActivityNode.__init__)


def test_uml3_0_0_structuredactivitynode_constructor_args():
    sig = inspect.signature(uml3_0_0_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_uml3_0_0_structuredactivitynode_has_mustIsolate():
    assert hasattr(uml3_0_0_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in uml3_0_0_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_state_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_State)


def test_uml3_0_0_state_constructor_exists():
    assert callable(uml3_0_0_State.__init__)


def test_uml3_0_0_state_constructor_args():
    sig = inspect.signature(uml3_0_0_State.__init__)
    params = list(sig.parameters.keys())
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"

def test_uml3_0_0_state_has_isOrthogonal():
    assert hasattr(uml3_0_0_State, "isOrthogonal")
    descriptor = None
    for klass in uml3_0_0_State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_state_has_isSimple():
    assert hasattr(uml3_0_0_State, "isSimple")
    descriptor = None
    for klass in uml3_0_0_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_state_has_isComposite():
    assert hasattr(uml3_0_0_State, "isComposite")
    descriptor = None
    for klass in uml3_0_0_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_state_has_isSubmachineState():
    assert hasattr(uml3_0_0_State, "isSubmachineState")
    descriptor = None
    for klass in uml3_0_0_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_BehavioralFeature)


def test_uml3_0_0_behavioralfeature_constructor_exists():
    assert callable(uml3_0_0_BehavioralFeature.__init__)


def test_uml3_0_0_behavioralfeature_constructor_args():
    sig = inspect.signature(uml3_0_0_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml3_0_0_behavioralfeature_has_concurrency():
    assert hasattr(uml3_0_0_BehavioralFeature, "concurrency")
    descriptor = None
    for klass in uml3_0_0_BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_behavioralfeature_has_isAbstract():
    assert hasattr(uml3_0_0_BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in uml3_0_0_BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_region_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Region)


def test_uml3_0_0_region_constructor_exists():
    assert callable(uml3_0_0_Region.__init__)


def test_uml3_0_0_region_constructor_args():
    sig = inspect.signature(uml3_0_0_Region.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_classifier_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Classifier)


def test_uml3_0_0_classifier_constructor_exists():
    assert callable(uml3_0_0_Classifier.__init__)


def test_uml3_0_0_classifier_constructor_args():
    sig = inspect.signature(uml3_0_0_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml3_0_0_classifier_has_isAbstract():
    assert hasattr(uml3_0_0_Classifier, "isAbstract")
    descriptor = None
    for klass in uml3_0_0_Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_package_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Package)


def test_uml3_0_0_package_constructor_exists():
    assert callable(uml3_0_0_Package.__init__)


def test_uml3_0_0_package_constructor_args():
    sig = inspect.signature(uml3_0_0_Package.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_element_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Element)


def test_uml3_0_0_element_constructor_exists():
    assert callable(uml3_0_0_Element.__init__)


def test_uml3_0_0_element_constructor_args():
    sig = inspect.signature(uml3_0_0_Element.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_relationship_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Relationship)


def test_uml3_0_0_relationship_constructor_exists():
    assert callable(uml3_0_0_Relationship.__init__)


def test_uml3_0_0_relationship_constructor_args():
    sig = inspect.signature(uml3_0_0_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_clause_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Clause)


def test_uml3_0_0_clause_constructor_exists():
    assert callable(uml3_0_0_Clause.__init__)


def test_uml3_0_0_clause_constructor_args():
    sig = inspect.signature(uml3_0_0_Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_linkenddata_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_LinkEndData)


def test_uml3_0_0_linkenddata_constructor_exists():
    assert callable(uml3_0_0_LinkEndData.__init__)


def test_uml3_0_0_linkenddata_constructor_args():
    sig = inspect.signature(uml3_0_0_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ParameterableElement)


def test_uml3_0_0_parameterableelement_constructor_exists():
    assert callable(uml3_0_0_ParameterableElement.__init__)


def test_uml3_0_0_parameterableelement_constructor_args():
    sig = inspect.signature(uml3_0_0_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_QualifierValue)


def test_uml3_0_0_qualifiervalue_constructor_exists():
    assert callable(uml3_0_0_QualifierValue.__init__)


def test_uml3_0_0_qualifiervalue_constructor_args():
    sig = inspect.signature(uml3_0_0_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_image_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Image)


def test_uml3_0_0_image_constructor_exists():
    assert callable(uml3_0_0_Image.__init__)


def test_uml3_0_0_image_constructor_args():
    sig = inspect.signature(uml3_0_0_Image.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "content" in params, "Missing parameter 'content'"
    assert "location" in params, "Missing parameter 'location'"

def test_uml3_0_0_image_has_format():
    assert hasattr(uml3_0_0_Image, "format")
    descriptor = None
    for klass in uml3_0_0_Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_image_has_content():
    assert hasattr(uml3_0_0_Image, "content")
    descriptor = None
    for klass in uml3_0_0_Image.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_image_has_location():
    assert hasattr(uml3_0_0_Image, "location")
    descriptor = None
    for klass in uml3_0_0_Image.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_namedelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_NamedElement)


def test_uml3_0_0_namedelement_constructor_exists():
    assert callable(uml3_0_0_NamedElement.__init__)


def test_uml3_0_0_namedelement_constructor_args():
    sig = inspect.signature(uml3_0_0_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_uml3_0_0_namedelement_has_qualifiedName():
    assert hasattr(uml3_0_0_NamedElement, "qualifiedName")
    descriptor = None
    for klass in uml3_0_0_NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_namedelement_has_visibility():
    assert hasattr(uml3_0_0_NamedElement, "visibility")
    descriptor = None
    for klass in uml3_0_0_NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_namedelement_has_name():
    assert hasattr(uml3_0_0_NamedElement, "name")
    descriptor = None
    for klass in uml3_0_0_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ExceptionHandler)


def test_uml3_0_0_exceptionhandler_constructor_exists():
    assert callable(uml3_0_0_ExceptionHandler.__init__)


def test_uml3_0_0_exceptionhandler_constructor_args():
    sig = inspect.signature(uml3_0_0_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_MultiplicityElement)


def test_uml3_0_0_multiplicityelement_constructor_exists():
    assert callable(uml3_0_0_MultiplicityElement.__init__)


def test_uml3_0_0_multiplicityelement_constructor_args():
    sig = inspect.signature(uml3_0_0_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_uml3_0_0_multiplicityelement_has_isUnique():
    assert hasattr(uml3_0_0_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in uml3_0_0_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_multiplicityelement_has_isOrdered():
    assert hasattr(uml3_0_0_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in uml3_0_0_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_multiplicityelement_has_upper():
    assert hasattr(uml3_0_0_MultiplicityElement, "upper")
    descriptor = None
    for klass in uml3_0_0_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml3_0_0_multiplicityelement_has_lower():
    assert hasattr(uml3_0_0_MultiplicityElement, "lower")
    descriptor = None
    for klass in uml3_0_0_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_uml3_0_0_activitygroup_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_ActivityGroup)


def test_uml3_0_0_activitygroup_constructor_exists():
    assert callable(uml3_0_0_ActivityGroup.__init__)


def test_uml3_0_0_activitygroup_constructor_args():
    sig = inspect.signature(uml3_0_0_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_templatesignature_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TemplateSignature)


def test_uml3_0_0_templatesignature_constructor_exists():
    assert callable(uml3_0_0_TemplateSignature.__init__)


def test_uml3_0_0_templatesignature_constructor_args():
    sig = inspect.signature(uml3_0_0_TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_templateableelement_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TemplateableElement)


def test_uml3_0_0_templateableelement_constructor_exists():
    assert callable(uml3_0_0_TemplateableElement.__init__)


def test_uml3_0_0_templateableelement_constructor_args():
    sig = inspect.signature(uml3_0_0_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TemplateParameterSubstitution)


def test_uml3_0_0_templateparametersubstitution_constructor_exists():
    assert callable(uml3_0_0_TemplateParameterSubstitution.__init__)


def test_uml3_0_0_templateparametersubstitution_constructor_args():
    sig = inspect.signature(uml3_0_0_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_slot_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Slot)


def test_uml3_0_0_slot_constructor_exists():
    assert callable(uml3_0_0_Slot.__init__)


def test_uml3_0_0_slot_constructor_args():
    sig = inspect.signature(uml3_0_0_Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_templateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_TemplateParameter)


def test_uml3_0_0_templateparameter_constructor_exists():
    assert callable(uml3_0_0_TemplateParameter.__init__)


def test_uml3_0_0_templateparameter_constructor_args():
    sig = inspect.signature(uml3_0_0_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml3_0_0_comment_is_not_abstract():
    assert not inspect.isabstract(uml3_0_0_Comment)


def test_uml3_0_0_comment_constructor_exists():
    assert callable(uml3_0_0_Comment.__init__)


def test_uml3_0_0_comment_constructor_args():
    sig = inspect.signature(uml3_0_0_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uml3_0_0_comment_has_body():
    assert hasattr(uml3_0_0_Comment, "body")
    descriptor = None
    for klass in uml3_0_0_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "update",
        "create",
        "delete",
        "read",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "parallel",
        "stream",
        "iterative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "deepHistory",
        "fork",
        "exitPoint",
        "initial",
        "entryPoint",
        "terminate",
        "choice",
        "junction",
        "shallowHistory",
        "join",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "shared",
        "none",
        "composite",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "local",
        "internal",
        "external",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

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
        "ordered",
        "unordered",
        "LIFO",
        "FIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

def test_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "unknown",
        "lost",
        "found",
        "complete",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "public",
        "package",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "assert_",
        "par",
        "strict",
        "neg",
        "ignore",
        "alt",
        "loop",
        "consider",
        "seq",
        "critical",
        "break_",
        "opt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "guarded",
        "sequential",
        "concurrent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "out",
        "inout",
        "return_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "synchCall",
        "deleteMessage",
        "reply",
        "asynchSignal",
        "createMessage",
        "asynchCall",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"


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
Transition_strategy = st.builds(
    Transition,
)
uml3_0_0_ProtocolTransition_strategy = st.builds(
    uml3_0_0_ProtocolTransition,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
uml3_0_0_DataStoreNode_strategy = st.builds(
    uml3_0_0_DataStoreNode,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
uml3_0_0_AcceptCallAction_strategy = st.builds(
    uml3_0_0_AcceptCallAction,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
uml3_0_0_CreateLinkObjectAction_strategy = st.builds(
    uml3_0_0_CreateLinkObjectAction,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
uml3_0_0_AddVariableValueAction_strategy = st.builds(
    uml3_0_0_AddVariableValueAction,
    isReplaceAll=
        safe_text
)
VariableAction_strategy = st.builds(
    VariableAction,
)
uml3_0_0_WriteVariableAction_strategy = st.builds(
    uml3_0_0_WriteVariableAction,
)
uml3_0_0_ClearVariableAction_strategy = st.builds(
    uml3_0_0_ClearVariableAction,
)
uml3_0_0_ReadVariableAction_strategy = st.builds(
    uml3_0_0_ReadVariableAction,
)
uml3_0_0_RemoveVariableValueAction_strategy = st.builds(
    uml3_0_0_RemoveVariableValueAction,
    isRemoveDuplicates=
        safe_text
)
State_strategy = st.builds(
    State,
)
uml3_0_0_FinalState_strategy = st.builds(
    uml3_0_0_FinalState,
)
Observation_strategy = st.builds(
    Observation,
)
uml3_0_0_DurationObservation_strategy = st.builds(
    uml3_0_0_DurationObservation,
    firstEvent=
        safe_text
)
uml3_0_0_TimeObservation_strategy = st.builds(
    uml3_0_0_TimeObservation,
    firstEvent=
        safe_text
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
uml3_0_0_DurationConstraint_strategy = st.builds(
    uml3_0_0_DurationConstraint,
    firstEvent=
        safe_text
)
uml3_0_0_TimeConstraint_strategy = st.builds(
    uml3_0_0_TimeConstraint,
    firstEvent=
        safe_text
)
Interval_strategy = st.builds(
    Interval,
)
uml3_0_0_TimeInterval_strategy = st.builds(
    uml3_0_0_TimeInterval,
)
uml3_0_0_DurationInterval_strategy = st.builds(
    uml3_0_0_DurationInterval,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
uml3_0_0_CreateLinkAction_strategy = st.builds(
    uml3_0_0_CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
uml3_0_0_LinkEndCreationData_strategy = st.builds(
    uml3_0_0_LinkEndCreationData,
    isReplaceAll=
        safe_text
)
uml3_0_0_LinkEndDestructionData_strategy = st.builds(
    uml3_0_0_LinkEndDestructionData,
    isDestroyDuplicates=
        safe_text
)
uml3_0_0_DestroyLinkAction_strategy = st.builds(
    uml3_0_0_DestroyLinkAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
uml3_0_0_WriteLinkAction_strategy = st.builds(
    uml3_0_0_WriteLinkAction,
)
uml3_0_0_ReadLinkAction_strategy = st.builds(
    uml3_0_0_ReadLinkAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
uml3_0_0_AddStructuralFeatureValueAction_strategy = st.builds(
    uml3_0_0_AddStructuralFeatureValueAction,
    isReplaceAll=
        safe_text
)
uml3_0_0_RemoveStructuralFeatureValueAction_strategy = st.builds(
    uml3_0_0_RemoveStructuralFeatureValueAction,
    isRemoveDuplicates=
        safe_text
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
uml3_0_0_ClearStructuralFeatureAction_strategy = st.builds(
    uml3_0_0_ClearStructuralFeatureAction,
)
uml3_0_0_WriteStructuralFeatureAction_strategy = st.builds(
    uml3_0_0_WriteStructuralFeatureAction,
)
uml3_0_0_ReadStructuralFeatureAction_strategy = st.builds(
    uml3_0_0_ReadStructuralFeatureAction,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
uml3_0_0_ConsiderIgnoreFragment_strategy = st.builds(
    uml3_0_0_ConsiderIgnoreFragment,
)
Node_strategy = st.builds(
    Node,
)
uml3_0_0_ExecutionEnvironment_strategy = st.builds(
    uml3_0_0_ExecutionEnvironment,
)
uml3_0_0_Device_strategy = st.builds(
    uml3_0_0_Device,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
uml3_0_0_ActivityFinalNode_strategy = st.builds(
    uml3_0_0_ActivityFinalNode,
)
uml3_0_0_FlowFinalNode_strategy = st.builds(
    uml3_0_0_FlowFinalNode,
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
uml3_0_0_ExecutionOccurrenceSpecification_strategy = st.builds(
    uml3_0_0_ExecutionOccurrenceSpecification,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
uml3_0_0_CallEvent_strategy = st.builds(
    uml3_0_0_CallEvent,
)
uml3_0_0_SendSignalEvent_strategy = st.builds(
    uml3_0_0_SendSignalEvent,
)
uml3_0_0_ReceiveSignalEvent_strategy = st.builds(
    uml3_0_0_ReceiveSignalEvent,
)
uml3_0_0_AnyReceiveEvent_strategy = st.builds(
    uml3_0_0_AnyReceiveEvent,
)
uml3_0_0_ReceiveOperationEvent_strategy = st.builds(
    uml3_0_0_ReceiveOperationEvent,
)
uml3_0_0_SignalEvent_strategy = st.builds(
    uml3_0_0_SignalEvent,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
uml3_0_0_ActionExecutionSpecification_strategy = st.builds(
    uml3_0_0_ActionExecutionSpecification,
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
Constraint_strategy = st.builds(
    Constraint,
)
uml3_0_0_IntervalConstraint_strategy = st.builds(
    uml3_0_0_IntervalConstraint,
)
uml3_0_0_PartDecomposition_strategy = st.builds(
    uml3_0_0_PartDecomposition,
)
uml3_0_0_InteractionConstraint_strategy = st.builds(
    uml3_0_0_InteractionConstraint,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
uml3_0_0_MessageOccurrenceSpecification_strategy = st.builds(
    uml3_0_0_MessageOccurrenceSpecification,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
uml3_0_0_CombinedFragment_strategy = st.builds(
    uml3_0_0_CombinedFragment,
    interactionOperator=
        safe_text
)
uml3_0_0_OccurrenceSpecification_strategy = st.builds(
    uml3_0_0_OccurrenceSpecification,
)
uml3_0_0_StateInvariant_strategy = st.builds(
    uml3_0_0_StateInvariant,
)
uml3_0_0_InteractionUse_strategy = st.builds(
    uml3_0_0_InteractionUse,
)
uml3_0_0_Continuation_strategy = st.builds(
    uml3_0_0_Continuation,
    setting=
        safe_text
)
uml3_0_0_ExecutionSpecification_strategy = st.builds(
    uml3_0_0_ExecutionSpecification,
)
uml3_0_0_Gate_strategy = st.builds(
    uml3_0_0_Gate,
)
InputPin_strategy = st.builds(
    InputPin,
)
uml3_0_0_ActionInputPin_strategy = st.builds(
    uml3_0_0_ActionInputPin,
)
uml3_0_0_ValuePin_strategy = st.builds(
    uml3_0_0_ValuePin,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
uml3_0_0_FinalNode_strategy = st.builds(
    uml3_0_0_FinalNode,
)
uml3_0_0_MergeNode_strategy = st.builds(
    uml3_0_0_MergeNode,
)
uml3_0_0_JoinNode_strategy = st.builds(
    uml3_0_0_JoinNode,
    isCombineDuplicate=
        safe_text
)
uml3_0_0_ForkNode_strategy = st.builds(
    uml3_0_0_ForkNode,
)
uml3_0_0_DecisionNode_strategy = st.builds(
    uml3_0_0_DecisionNode,
)
uml3_0_0_InitialNode_strategy = st.builds(
    uml3_0_0_InitialNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
uml3_0_0_ObjectFlow_strategy = st.builds(
    uml3_0_0_ObjectFlow,
    isMulticast=
        safe_text,
    isMultireceive=
        safe_text
)
uml3_0_0_ControlFlow_strategy = st.builds(
    uml3_0_0_ControlFlow,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
uml3_0_0_ConditionalNode_strategy = st.builds(
    uml3_0_0_ConditionalNode,
    isDeterminate=
        safe_text,
    isAssured=
        safe_text
)
uml3_0_0_ExpansionRegion_strategy = st.builds(
    uml3_0_0_ExpansionRegion,
    mode=
        safe_text
)
uml3_0_0_LoopNode_strategy = st.builds(
    uml3_0_0_LoopNode,
    isTestedFirst=
        safe_text
)
uml3_0_0_SequenceNode_strategy = st.builds(
    uml3_0_0_SequenceNode,
)
CallAction_strategy = st.builds(
    CallAction,
)
uml3_0_0_CallBehaviorAction_strategy = st.builds(
    uml3_0_0_CallBehaviorAction,
)
uml3_0_0_StartObjectBehaviorAction_strategy = st.builds(
    uml3_0_0_StartObjectBehaviorAction,
)
uml3_0_0_CallOperationAction_strategy = st.builds(
    uml3_0_0_CallOperationAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
uml3_0_0_BroadcastSignalAction_strategy = st.builds(
    uml3_0_0_BroadcastSignalAction,
)
uml3_0_0_SendObjectAction_strategy = st.builds(
    uml3_0_0_SendObjectAction,
)
uml3_0_0_SendSignalAction_strategy = st.builds(
    uml3_0_0_SendSignalAction,
)
uml3_0_0_CallAction_strategy = st.builds(
    uml3_0_0_CallAction,
    isSynchronous=
        safe_text
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
uml3_0_0_ActivityParameterNode_strategy = st.builds(
    uml3_0_0_ActivityParameterNode,
)
uml3_0_0_ExpansionNode_strategy = st.builds(
    uml3_0_0_ExpansionNode,
)
uml3_0_0_CentralBufferNode_strategy = st.builds(
    uml3_0_0_CentralBufferNode,
)
Pin_strategy = st.builds(
    Pin,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
uml3_0_0_InterruptibleActivityRegion_strategy = st.builds(
    uml3_0_0_InterruptibleActivityRegion,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
uml3_0_0_ControlNode_strategy = st.builds(
    uml3_0_0_ControlNode,
)
uml3_0_0_ExecutableNode_strategy = st.builds(
    uml3_0_0_ExecutableNode,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
uml3_0_0_Action_strategy = st.builds(
    uml3_0_0_Action,
)
uml3_0_0_OutputPin_strategy = st.builds(
    uml3_0_0_OutputPin,
)
uml3_0_0_InputPin_strategy = st.builds(
    uml3_0_0_InputPin,
)
Action_strategy = st.builds(
    Action,
)
uml3_0_0_ReadSelfAction_strategy = st.builds(
    uml3_0_0_ReadSelfAction,
)
uml3_0_0_CreateObjectAction_strategy = st.builds(
    uml3_0_0_CreateObjectAction,
)
uml3_0_0_ReplyAction_strategy = st.builds(
    uml3_0_0_ReplyAction,
)
uml3_0_0_RaiseExceptionAction_strategy = st.builds(
    uml3_0_0_RaiseExceptionAction,
)
uml3_0_0_VariableAction_strategy = st.builds(
    uml3_0_0_VariableAction,
)
uml3_0_0_ReadExtentAction_strategy = st.builds(
    uml3_0_0_ReadExtentAction,
)
uml3_0_0_AcceptEventAction_strategy = st.builds(
    uml3_0_0_AcceptEventAction,
    isUnmarshall=
        safe_text
)
uml3_0_0_ReadLinkObjectEndAction_strategy = st.builds(
    uml3_0_0_ReadLinkObjectEndAction,
)
uml3_0_0_ReclassifyObjectAction_strategy = st.builds(
    uml3_0_0_ReclassifyObjectAction,
    isReplaceAll=
        safe_text
)
uml3_0_0_UnmarshallAction_strategy = st.builds(
    uml3_0_0_UnmarshallAction,
)
uml3_0_0_LinkAction_strategy = st.builds(
    uml3_0_0_LinkAction,
)
uml3_0_0_InvocationAction_strategy = st.builds(
    uml3_0_0_InvocationAction,
)
uml3_0_0_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml3_0_0_ReadLinkObjectEndQualifierAction,
)
uml3_0_0_StartClassifierBehaviorAction_strategy = st.builds(
    uml3_0_0_StartClassifierBehaviorAction,
)
uml3_0_0_ReduceAction_strategy = st.builds(
    uml3_0_0_ReduceAction,
    isOrdered=
        safe_text
)
uml3_0_0_ReadIsClassifiedObjectAction_strategy = st.builds(
    uml3_0_0_ReadIsClassifiedObjectAction,
    isDirect=
        safe_text
)
uml3_0_0_ClearAssociationAction_strategy = st.builds(
    uml3_0_0_ClearAssociationAction,
)
uml3_0_0_ValueSpecificationAction_strategy = st.builds(
    uml3_0_0_ValueSpecificationAction,
)
uml3_0_0_DestroyObjectAction_strategy = st.builds(
    uml3_0_0_DestroyObjectAction,
    isDestroyLinks=
        safe_text,
    isDestroyOwnedObjects=
        safe_text
)
uml3_0_0_StructuralFeatureAction_strategy = st.builds(
    uml3_0_0_StructuralFeatureAction,
)
uml3_0_0_TestIdentityAction_strategy = st.builds(
    uml3_0_0_TestIdentityAction,
)
uml3_0_0_OpaqueAction_strategy = st.builds(
    uml3_0_0_OpaqueAction,
    language=
        safe_text,
    body=
        safe_text
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
uml3_0_0_FunctionBehavior_strategy = st.builds(
    uml3_0_0_FunctionBehavior,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
uml3_0_0_LiteralString_strategy = st.builds(
    uml3_0_0_LiteralString,
    value=
        safe_text
)
uml3_0_0_LiteralUnlimitedNatural_strategy = st.builds(
    uml3_0_0_LiteralUnlimitedNatural,
    value=
        safe_text
)
uml3_0_0_LiteralNull_strategy = st.builds(
    uml3_0_0_LiteralNull,
)
uml3_0_0_LiteralBoolean_strategy = st.builds(
    uml3_0_0_LiteralBoolean,
    value=
        safe_text
)
uml3_0_0_LiteralInteger_strategy = st.builds(
    uml3_0_0_LiteralInteger,
    value=
        safe_text
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
uml3_0_0_EnumerationLiteral_strategy = st.builds(
    uml3_0_0_EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
uml3_0_0_PrimitiveType_strategy = st.builds(
    uml3_0_0_PrimitiveType,
)
uml3_0_0_Enumeration_strategy = st.builds(
    uml3_0_0_Enumeration,
)
Expression_strategy = st.builds(
    Expression,
)
TemplateSignature_strategy = st.builds(
    TemplateSignature,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
uml3_0_0_ClassifierTemplateParameter_strategy = st.builds(
    uml3_0_0_ClassifierTemplateParameter,
    allowSubstitutable=
        safe_text
)
uml3_0_0_ConnectableElementTemplateParameter_strategy = st.builds(
    uml3_0_0_ConnectableElementTemplateParameter,
)
uml3_0_0_OperationTemplateParameter_strategy = st.builds(
    uml3_0_0_OperationTemplateParameter,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
uml3_0_0_EncapsulatedClassifier_strategy = st.builds(
    uml3_0_0_EncapsulatedClassifier,
)
Package_strategy = st.builds(
    Package,
)
uml3_0_0_Model_strategy = st.builds(
    uml3_0_0_Model,
    viewpoint=
        safe_text
)
uml3_0_0_Profile_strategy = st.builds(
    uml3_0_0_Profile,
)
Association_strategy = st.builds(
    Association,
)
uml3_0_0_CommunicationPath_strategy = st.builds(
    uml3_0_0_CommunicationPath,
)
Vertex_strategy = st.builds(
    Vertex,
)
uml3_0_0_ConnectionPointReference_strategy = st.builds(
    uml3_0_0_ConnectionPointReference,
)
Property_strategy = st.builds(
    Property,
)
uml3_0_0_ExtensionEnd_strategy = st.builds(
    uml3_0_0_ExtensionEnd,
)
uml3_0_0_Port_strategy = st.builds(
    uml3_0_0_Port,
    isBehavior=
        safe_text,
    isService=
        safe_text
)
uml3_0_0_Pseudostate_strategy = st.builds(
    uml3_0_0_Pseudostate,
    kind=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
uml3_0_0_OpaqueBehavior_strategy = st.builds(
    uml3_0_0_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
uml3_0_0_Interaction_strategy = st.builds(
    uml3_0_0_Interaction,
)
uml3_0_0_Activity_strategy = st.builds(
    uml3_0_0_Activity,
    isSingleExecution=
        safe_text,
    isReadOnly=
        safe_text
)
uml3_0_0_StateMachine_strategy = st.builds(
    uml3_0_0_StateMachine,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
uml3_0_0_ProtocolStateMachine_strategy = st.builds(
    uml3_0_0_ProtocolStateMachine,
)
uml3_0_0_Extension_strategy = st.builds(
    uml3_0_0_Extension,
    isRequired=
        safe_text
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
uml3_0_0_Actor_strategy = st.builds(
    uml3_0_0_Actor,
)
uml3_0_0_Collaboration_strategy = st.builds(
    uml3_0_0_Collaboration,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
Class_strategy = st.builds(
    Class,
)
uml3_0_0_AssociationClass_strategy = st.builds(
    uml3_0_0_AssociationClass,
)
uml3_0_0_Stereotype_strategy = st.builds(
    uml3_0_0_Stereotype,
)
uml3_0_0_Component_strategy = st.builds(
    uml3_0_0_Component,
    isIndirectlyInstantiated=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
uml3_0_0_Connector_strategy = st.builds(
    uml3_0_0_Connector,
    kind=
        safe_text
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
uml3_0_0_Reception_strategy = st.builds(
    uml3_0_0_Reception,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
Artifact_strategy = st.builds(
    Artifact,
)
uml3_0_0_DeploymentSpecification_strategy = st.builds(
    uml3_0_0_DeploymentSpecification,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text
)
uml3_0_0_Class_strategy = st.builds(
    uml3_0_0_Class,
    isActive=
        safe_text
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
uml3_0_0_Node_strategy = st.builds(
    uml3_0_0_Node,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
uml3_0_0_LiteralSpecification_strategy = st.builds(
    uml3_0_0_LiteralSpecification,
)
uml3_0_0_Interval_strategy = st.builds(
    uml3_0_0_Interval,
)
uml3_0_0_TimeExpression_strategy = st.builds(
    uml3_0_0_TimeExpression,
)
uml3_0_0_Duration_strategy = st.builds(
    uml3_0_0_Duration,
)
uml3_0_0_Expression_strategy = st.builds(
    uml3_0_0_Expression,
    symbol=
        safe_text
)
uml3_0_0_InstanceValue_strategy = st.builds(
    uml3_0_0_InstanceValue,
)
uml3_0_0_OpaqueExpression_strategy = st.builds(
    uml3_0_0_OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
Dependency_strategy = st.builds(
    Dependency,
)
uml3_0_0_Deployment_strategy = st.builds(
    uml3_0_0_Deployment,
)
uml3_0_0_Usage_strategy = st.builds(
    uml3_0_0_Usage,
)
uml3_0_0_Abstraction_strategy = st.builds(
    uml3_0_0_Abstraction,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
uml3_0_0_Manifestation_strategy = st.builds(
    uml3_0_0_Manifestation,
)
uml3_0_0_Realization_strategy = st.builds(
    uml3_0_0_Realization,
)
uml3_0_0_SendOperationEvent_strategy = st.builds(
    uml3_0_0_SendOperationEvent,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
uml3_0_0_Pin_strategy = st.builds(
    uml3_0_0_Pin,
    isControl=
        safe_text
)
uml3_0_0_ConnectorEnd_strategy = st.builds(
    uml3_0_0_ConnectorEnd,
)
Event_strategy = st.builds(
    Event,
)
uml3_0_0_TimeEvent_strategy = st.builds(
    uml3_0_0_TimeEvent,
    isRelative=
        safe_text
)
uml3_0_0_ChangeEvent_strategy = st.builds(
    uml3_0_0_ChangeEvent,
)
uml3_0_0_DestructionEvent_strategy = st.builds(
    uml3_0_0_DestructionEvent,
)
uml3_0_0_MessageEvent_strategy = st.builds(
    uml3_0_0_MessageEvent,
)
uml3_0_0_CreationEvent_strategy = st.builds(
    uml3_0_0_CreationEvent,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
uml3_0_0_Variable_strategy = st.builds(
    uml3_0_0_Variable,
)
uml3_0_0_ExecutionEvent_strategy = st.builds(
    uml3_0_0_ExecutionEvent,
)
uml3_0_0_Behavior_strategy = st.builds(
    uml3_0_0_Behavior,
    isReentrant=
        safe_text
)
uml3_0_0_BehaviorExecutionSpecification_strategy = st.builds(
    uml3_0_0_BehaviorExecutionSpecification,
)
uml3_0_0_Parameter_strategy = st.builds(
    uml3_0_0_Parameter,
    default=
        safe_text,
    effect=
        safe_text,
    isException=
        safe_text,
    direction=
        safe_text,
    isStream=
        safe_text
)
Realization_strategy = st.builds(
    Realization,
)
uml3_0_0_ComponentRealization_strategy = st.builds(
    uml3_0_0_ComponentRealization,
)
uml3_0_0_InterfaceRealization_strategy = st.builds(
    uml3_0_0_InterfaceRealization,
)
uml3_0_0_Property_strategy = st.builds(
    uml3_0_0_Property,
    isComposite=
        safe_text,
    default=
        safe_text,
    isDerivedUnion=
        safe_text,
    isDerived=
        safe_text,
    aggregation=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uml3_0_0_BehavioredClassifier_strategy = st.builds(
    uml3_0_0_BehavioredClassifier,
)
uml3_0_0_InformationItem_strategy = st.builds(
    uml3_0_0_InformationItem,
)
uml3_0_0_StructuredClassifier_strategy = st.builds(
    uml3_0_0_StructuredClassifier,
)
uml3_0_0_DataType_strategy = st.builds(
    uml3_0_0_DataType,
)
uml3_0_0_Interface_strategy = st.builds(
    uml3_0_0_Interface,
)
uml3_0_0_Signal_strategy = st.builds(
    uml3_0_0_Signal,
)
uml3_0_0_Artifact_strategy = st.builds(
    uml3_0_0_Artifact,
    fileName=
        safe_text
)
uml3_0_0_UseCase_strategy = st.builds(
    uml3_0_0_UseCase,
)
uml3_0_0_Substitution_strategy = st.builds(
    uml3_0_0_Substitution,
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
uml3_0_0_ExtensionPoint_strategy = st.builds(
    uml3_0_0_ExtensionPoint,
)
uml3_0_0_ActivityNode_strategy = st.builds(
    uml3_0_0_ActivityNode,
)
uml3_0_0_RedefinableTemplateSignature_strategy = st.builds(
    uml3_0_0_RedefinableTemplateSignature,
)
uml3_0_0_ActivityEdge_strategy = st.builds(
    uml3_0_0_ActivityEdge,
)
uml3_0_0_Feature_strategy = st.builds(
    uml3_0_0_Feature,
    isStatic=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uml3_0_0_ObjectNode_strategy = st.builds(
    uml3_0_0_ObjectNode,
    ordering=
        safe_text,
    isControlType=
        safe_text
)
uml3_0_0_StructuralFeature_strategy = st.builds(
    uml3_0_0_StructuralFeature,
    isReadOnly=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
uml3_0_0_Generalization_strategy = st.builds(
    uml3_0_0_Generalization,
    isSubstitutable=
        safe_text
)
uml3_0_0_TemplateBinding_strategy = st.builds(
    uml3_0_0_TemplateBinding,
)
uml3_0_0_ProtocolConformance_strategy = st.builds(
    uml3_0_0_ProtocolConformance,
)
uml3_0_0_PackageImport_strategy = st.builds(
    uml3_0_0_PackageImport,
    visibility=
        safe_text
)
uml3_0_0_ElementImport_strategy = st.builds(
    uml3_0_0_ElementImport,
    alias=
        safe_text,
    visibility=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
uml3_0_0_Association_strategy = st.builds(
    uml3_0_0_Association,
    isDerived=
        safe_text
)
uml3_0_0_DirectedRelationship_strategy = st.builds(
    uml3_0_0_DirectedRelationship,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
uml3_0_0_ConnectableElement_strategy = st.builds(
    uml3_0_0_ConnectableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml3_0_0_CollaborationUse_strategy = st.builds(
    uml3_0_0_CollaborationUse,
)
uml3_0_0_ActivityPartition_strategy = st.builds(
    uml3_0_0_ActivityPartition,
    isExternal=
        safe_text,
    isDimension=
        safe_text
)
uml3_0_0_GeneralOrdering_strategy = st.builds(
    uml3_0_0_GeneralOrdering,
)
uml3_0_0_Vertex_strategy = st.builds(
    uml3_0_0_Vertex,
)
uml3_0_0_TypedElement_strategy = st.builds(
    uml3_0_0_TypedElement,
)
uml3_0_0_Extend_strategy = st.builds(
    uml3_0_0_Extend,
)
uml3_0_0_RedefinableElement_strategy = st.builds(
    uml3_0_0_RedefinableElement,
    isLeaf=
        safe_text
)
uml3_0_0_DeploymentTarget_strategy = st.builds(
    uml3_0_0_DeploymentTarget,
)
uml3_0_0_ParameterSet_strategy = st.builds(
    uml3_0_0_ParameterSet,
)
uml3_0_0_DeployedArtifact_strategy = st.builds(
    uml3_0_0_DeployedArtifact,
)
uml3_0_0_InteractionFragment_strategy = st.builds(
    uml3_0_0_InteractionFragment,
)
uml3_0_0_MessageEnd_strategy = st.builds(
    uml3_0_0_MessageEnd,
)
uml3_0_0_Trigger_strategy = st.builds(
    uml3_0_0_Trigger,
)
uml3_0_0_Message_strategy = st.builds(
    uml3_0_0_Message,
    messageSort=
        safe_text,
    messageKind=
        safe_text
)
uml3_0_0_Namespace_strategy = st.builds(
    uml3_0_0_Namespace,
)
uml3_0_0_Lifeline_strategy = st.builds(
    uml3_0_0_Lifeline,
)
uml3_0_0_Include_strategy = st.builds(
    uml3_0_0_Include,
)
uml3_0_0_ProfileApplication_strategy = st.builds(
    uml3_0_0_ProfileApplication,
    isStrict=
        safe_text
)
uml3_0_0_PackageableElement_strategy = st.builds(
    uml3_0_0_PackageableElement,
)
uml3_0_0_PackageMerge_strategy = st.builds(
    uml3_0_0_PackageMerge,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
uml3_0_0_StringExpression_strategy = st.builds(
    uml3_0_0_StringExpression,
)
uml3_0_0_Operation_strategy = st.builds(
    uml3_0_0_Operation,
    lower=
        safe_text,
    upper=
        safe_text,
    isQuery=
        safe_text,
    isOrdered=
        safe_text,
    isUnique=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml3_0_0_Type_strategy = st.builds(
    uml3_0_0_Type,
)
uml3_0_0_Observation_strategy = st.builds(
    uml3_0_0_Observation,
)
uml3_0_0_InformationFlow_strategy = st.builds(
    uml3_0_0_InformationFlow,
)
uml3_0_0_InstanceSpecification_strategy = st.builds(
    uml3_0_0_InstanceSpecification,
)
uml3_0_0_Event_strategy = st.builds(
    uml3_0_0_Event,
)
uml3_0_0_Dependency_strategy = st.builds(
    uml3_0_0_Dependency,
)
uml3_0_0_ValueSpecification_strategy = st.builds(
    uml3_0_0_ValueSpecification,
)
uml3_0_0_Constraint_strategy = st.builds(
    uml3_0_0_Constraint,
)
uml3_0_0_GeneralizationSet_strategy = st.builds(
    uml3_0_0_GeneralizationSet,
    isDisjoint=
        safe_text,
    isCovering=
        safe_text
)
Namespace_strategy = st.builds(
    Namespace,
)
uml3_0_0_Transition_strategy = st.builds(
    uml3_0_0_Transition,
    kind=
        safe_text
)
uml3_0_0_InteractionOperand_strategy = st.builds(
    uml3_0_0_InteractionOperand,
)
uml3_0_0_StructuredActivityNode_strategy = st.builds(
    uml3_0_0_StructuredActivityNode,
    mustIsolate=
        safe_text
)
uml3_0_0_State_strategy = st.builds(
    uml3_0_0_State,
    isOrthogonal=
        safe_text,
    isSimple=
        safe_text,
    isComposite=
        safe_text,
    isSubmachineState=
        safe_text
)
uml3_0_0_BehavioralFeature_strategy = st.builds(
    uml3_0_0_BehavioralFeature,
    concurrency=
        safe_text,
    isAbstract=
        safe_text
)
uml3_0_0_Region_strategy = st.builds(
    uml3_0_0_Region,
)
uml3_0_0_Classifier_strategy = st.builds(
    uml3_0_0_Classifier,
    isAbstract=
        safe_text
)
uml3_0_0_Package_strategy = st.builds(
    uml3_0_0_Package,
)
uml3_0_0_Element_strategy = st.builds(
    uml3_0_0_Element,
)
Element_strategy = st.builds(
    Element,
)
uml3_0_0_Relationship_strategy = st.builds(
    uml3_0_0_Relationship,
)
uml3_0_0_Clause_strategy = st.builds(
    uml3_0_0_Clause,
)
uml3_0_0_LinkEndData_strategy = st.builds(
    uml3_0_0_LinkEndData,
)
uml3_0_0_ParameterableElement_strategy = st.builds(
    uml3_0_0_ParameterableElement,
)
uml3_0_0_QualifierValue_strategy = st.builds(
    uml3_0_0_QualifierValue,
)
uml3_0_0_Image_strategy = st.builds(
    uml3_0_0_Image,
    format=
        safe_text,
    content=
        safe_text,
    location=
        safe_text
)
uml3_0_0_NamedElement_strategy = st.builds(
    uml3_0_0_NamedElement,
    qualifiedName=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
uml3_0_0_ExceptionHandler_strategy = st.builds(
    uml3_0_0_ExceptionHandler,
)
uml3_0_0_MultiplicityElement_strategy = st.builds(
    uml3_0_0_MultiplicityElement,
    isUnique=
        safe_text,
    isOrdered=
        safe_text,
    upper=
        safe_text,
    lower=
        safe_text
)
uml3_0_0_ActivityGroup_strategy = st.builds(
    uml3_0_0_ActivityGroup,
)
uml3_0_0_TemplateSignature_strategy = st.builds(
    uml3_0_0_TemplateSignature,
)
uml3_0_0_TemplateableElement_strategy = st.builds(
    uml3_0_0_TemplateableElement,
)
uml3_0_0_TemplateParameterSubstitution_strategy = st.builds(
    uml3_0_0_TemplateParameterSubstitution,
)
uml3_0_0_Slot_strategy = st.builds(
    uml3_0_0_Slot,
)
uml3_0_0_TemplateParameter_strategy = st.builds(
    uml3_0_0_TemplateParameter,
)
uml3_0_0_Comment_strategy = st.builds(
    uml3_0_0_Comment,
    body=
        safe_text
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=uml3_0_0_ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml3_0_0_protocoltransition_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ProtocolTransition)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=uml3_0_0_DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_datastorenode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DataStoreNode)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=uml3_0_0_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_acceptcallaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_AcceptCallAction)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=uml3_0_0_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CreateLinkObjectAction)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=uml3_0_0_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_AddVariableValueAction)



@given(instance=uml3_0_0_AddVariableValueAction_strategy)
def test_uml3_0_0_addvariablevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=uml3_0_0_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_writevariableaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_WriteVariableAction)

@given(instance=uml3_0_0_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_clearvariableaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ClearVariableAction)

@given(instance=uml3_0_0_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readvariableaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadVariableAction)

@given(instance=uml3_0_0_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_RemoveVariableValueAction)



@given(instance=uml3_0_0_RemoveVariableValueAction_strategy)
def test_uml3_0_0_removevariablevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=uml3_0_0_FinalState_strategy)
@settings(max_examples=50)
def test_uml3_0_0_finalstate_instantiation(instance):
    assert isinstance(instance, uml3_0_0_FinalState)

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=uml3_0_0_DurationObservation_strategy)
@settings(max_examples=50)
def test_uml3_0_0_durationobservation_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DurationObservation)



@given(instance=uml3_0_0_DurationObservation_strategy)
def test_uml3_0_0_durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml3_0_0_TimeObservation_strategy)
@settings(max_examples=50)
def test_uml3_0_0_timeobservation_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TimeObservation)



@given(instance=uml3_0_0_TimeObservation_strategy)
def test_uml3_0_0_timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=uml3_0_0_DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml3_0_0_durationconstraint_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DurationConstraint)



@given(instance=uml3_0_0_DurationConstraint_strategy)
def test_uml3_0_0_durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml3_0_0_TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml3_0_0_timeconstraint_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TimeConstraint)



@given(instance=uml3_0_0_TimeConstraint_strategy)
def test_uml3_0_0_timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=uml3_0_0_TimeInterval_strategy)
@settings(max_examples=50)
def test_uml3_0_0_timeinterval_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TimeInterval)

@given(instance=uml3_0_0_DurationInterval_strategy)
@settings(max_examples=50)
def test_uml3_0_0_durationinterval_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DurationInterval)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=uml3_0_0_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_createlinkaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CreateLinkAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=uml3_0_0_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml3_0_0_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LinkEndCreationData)



@given(instance=uml3_0_0_LinkEndCreationData_strategy)
def test_uml3_0_0_linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml3_0_0_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_uml3_0_0_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LinkEndDestructionData)



@given(instance=uml3_0_0_LinkEndDestructionData_strategy)
def test_uml3_0_0_linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=uml3_0_0_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_destroylinkaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DestroyLinkAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=uml3_0_0_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_writelinkaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_WriteLinkAction)

@given(instance=uml3_0_0_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readlinkaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadLinkAction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=uml3_0_0_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_AddStructuralFeatureValueAction)



@given(instance=uml3_0_0_AddStructuralFeatureValueAction_strategy)
def test_uml3_0_0_addstructuralfeaturevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml3_0_0_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_RemoveStructuralFeatureValueAction)



@given(instance=uml3_0_0_RemoveStructuralFeatureValueAction_strategy)
def test_uml3_0_0_removestructuralfeaturevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=uml3_0_0_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ClearStructuralFeatureAction)

@given(instance=uml3_0_0_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_WriteStructuralFeatureAction)

@given(instance=uml3_0_0_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadStructuralFeatureAction)

@given(instance=CombinedFragment_strategy)
@settings(max_examples=50)
def test_combinedfragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)

@given(instance=uml3_0_0_ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_uml3_0_0_considerignorefragment_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ConsiderIgnoreFragment)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=uml3_0_0_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml3_0_0_executionenvironment_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExecutionEnvironment)

@given(instance=uml3_0_0_Device_strategy)
@settings(max_examples=50)
def test_uml3_0_0_device_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Device)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=uml3_0_0_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_activityfinalnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActivityFinalNode)

@given(instance=uml3_0_0_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_flowfinalnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_FlowFinalNode)

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=uml3_0_0_ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExecutionOccurrenceSpecification)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=uml3_0_0_CallEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_callevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CallEvent)

@given(instance=uml3_0_0_SendSignalEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_sendsignalevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_SendSignalEvent)

@given(instance=uml3_0_0_ReceiveSignalEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_receivesignalevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReceiveSignalEvent)

@given(instance=uml3_0_0_AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_anyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_AnyReceiveEvent)

@given(instance=uml3_0_0_ReceiveOperationEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_receiveoperationevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReceiveOperationEvent)

@given(instance=uml3_0_0_SignalEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_signalevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_SignalEvent)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=uml3_0_0_ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActionExecutionSpecification)

@given(instance=InteractionUse_strategy)
@settings(max_examples=50)
def test_interactionuse_instantiation(instance):
    assert isinstance(instance, InteractionUse)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=uml3_0_0_IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml3_0_0_intervalconstraint_instantiation(instance):
    assert isinstance(instance, uml3_0_0_IntervalConstraint)

@given(instance=uml3_0_0_PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml3_0_0_partdecomposition_instantiation(instance):
    assert isinstance(instance, uml3_0_0_PartDecomposition)

@given(instance=uml3_0_0_InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interactionconstraint_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InteractionConstraint)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=uml3_0_0_MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_MessageOccurrenceSpecification)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=uml3_0_0_CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml3_0_0_combinedfragment_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CombinedFragment)



@given(instance=uml3_0_0_CombinedFragment_strategy)
def test_uml3_0_0_combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=uml3_0_0_OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_occurrencespecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_OccurrenceSpecification)

@given(instance=uml3_0_0_StateInvariant_strategy)
@settings(max_examples=50)
def test_uml3_0_0_stateinvariant_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StateInvariant)

@given(instance=uml3_0_0_InteractionUse_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interactionuse_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InteractionUse)

@given(instance=uml3_0_0_Continuation_strategy)
@settings(max_examples=50)
def test_uml3_0_0_continuation_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Continuation)



@given(instance=uml3_0_0_Continuation_strategy)
def test_uml3_0_0_continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=uml3_0_0_ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_executionspecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExecutionSpecification)

@given(instance=uml3_0_0_Gate_strategy)
@settings(max_examples=50)
def test_uml3_0_0_gate_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Gate)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=uml3_0_0_ActionInputPin_strategy)
@settings(max_examples=50)
def test_uml3_0_0_actioninputpin_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActionInputPin)

@given(instance=uml3_0_0_ValuePin_strategy)
@settings(max_examples=50)
def test_uml3_0_0_valuepin_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ValuePin)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=uml3_0_0_FinalNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_finalnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_FinalNode)

@given(instance=uml3_0_0_MergeNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_mergenode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_MergeNode)

@given(instance=uml3_0_0_JoinNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_joinnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_JoinNode)



@given(instance=uml3_0_0_JoinNode_strategy)
def test_uml3_0_0_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=uml3_0_0_ForkNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_forknode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ForkNode)

@given(instance=uml3_0_0_DecisionNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_decisionnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DecisionNode)

@given(instance=uml3_0_0_InitialNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_initialnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InitialNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=uml3_0_0_ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml3_0_0_objectflow_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ObjectFlow)



@given(instance=uml3_0_0_ObjectFlow_strategy)
def test_uml3_0_0_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original



@given(instance=uml3_0_0_ObjectFlow_strategy)
def test_uml3_0_0_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=uml3_0_0_ControlFlow_strategy)
@settings(max_examples=50)
def test_uml3_0_0_controlflow_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ControlFlow)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=uml3_0_0_ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_conditionalnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ConditionalNode)



@given(instance=uml3_0_0_ConditionalNode_strategy)
def test_uml3_0_0_conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original



@given(instance=uml3_0_0_ConditionalNode_strategy)
def test_uml3_0_0_conditionalnode_isAssured_setter(instance):
    original = instance.isAssured
    instance.isAssured = original
    assert instance.isAssured == original

@given(instance=uml3_0_0_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml3_0_0_expansionregion_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExpansionRegion)



@given(instance=uml3_0_0_ExpansionRegion_strategy)
def test_uml3_0_0_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=uml3_0_0_LoopNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_loopnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LoopNode)



@given(instance=uml3_0_0_LoopNode_strategy)
def test_uml3_0_0_loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=uml3_0_0_SequenceNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_sequencenode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_SequenceNode)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=uml3_0_0_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_callbehavioraction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CallBehaviorAction)

@given(instance=uml3_0_0_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StartObjectBehaviorAction)

@given(instance=uml3_0_0_CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_calloperationaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CallOperationAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=uml3_0_0_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_BroadcastSignalAction)

@given(instance=uml3_0_0_SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_sendobjectaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_SendObjectAction)

@given(instance=uml3_0_0_SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_sendsignalaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_SendSignalAction)

@given(instance=uml3_0_0_CallAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_callaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CallAction)



@given(instance=uml3_0_0_CallAction_strategy)
def test_uml3_0_0_callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=uml3_0_0_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_activityparameternode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActivityParameterNode)

@given(instance=uml3_0_0_ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_expansionnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExpansionNode)

@given(instance=uml3_0_0_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_centralbuffernode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CentralBufferNode)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=uml3_0_0_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InterruptibleActivityRegion)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=uml3_0_0_ControlNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_controlnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ControlNode)

@given(instance=uml3_0_0_ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_executablenode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExecutableNode)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=uml3_0_0_Action_strategy)
@settings(max_examples=50)
def test_uml3_0_0_action_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Action)

@given(instance=uml3_0_0_OutputPin_strategy)
@settings(max_examples=50)
def test_uml3_0_0_outputpin_instantiation(instance):
    assert isinstance(instance, uml3_0_0_OutputPin)

@given(instance=uml3_0_0_InputPin_strategy)
@settings(max_examples=50)
def test_uml3_0_0_inputpin_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=uml3_0_0_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readselfaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadSelfAction)

@given(instance=uml3_0_0_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_createobjectaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CreateObjectAction)

@given(instance=uml3_0_0_ReplyAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_replyaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReplyAction)

@given(instance=uml3_0_0_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_RaiseExceptionAction)

@given(instance=uml3_0_0_VariableAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_variableaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_VariableAction)

@given(instance=uml3_0_0_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readextentaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadExtentAction)

@given(instance=uml3_0_0_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_accepteventaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_AcceptEventAction)



@given(instance=uml3_0_0_AcceptEventAction_strategy)
def test_uml3_0_0_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=uml3_0_0_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadLinkObjectEndAction)

@given(instance=uml3_0_0_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReclassifyObjectAction)



@given(instance=uml3_0_0_ReclassifyObjectAction_strategy)
def test_uml3_0_0_reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml3_0_0_UnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_unmarshallaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_UnmarshallAction)

@given(instance=uml3_0_0_LinkAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_linkaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LinkAction)

@given(instance=uml3_0_0_InvocationAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_invocationaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InvocationAction)

@given(instance=uml3_0_0_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadLinkObjectEndQualifierAction)

@given(instance=uml3_0_0_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StartClassifierBehaviorAction)

@given(instance=uml3_0_0_ReduceAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_reduceaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReduceAction)



@given(instance=uml3_0_0_ReduceAction_strategy)
def test_uml3_0_0_reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml3_0_0_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ReadIsClassifiedObjectAction)



@given(instance=uml3_0_0_ReadIsClassifiedObjectAction_strategy)
def test_uml3_0_0_readisclassifiedobjectaction_isDirect_setter(instance):
    original = instance.isDirect
    instance.isDirect = original
    assert instance.isDirect == original

@given(instance=uml3_0_0_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_clearassociationaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ClearAssociationAction)

@given(instance=uml3_0_0_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ValueSpecificationAction)

@given(instance=uml3_0_0_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DestroyObjectAction)



@given(instance=uml3_0_0_DestroyObjectAction_strategy)
def test_uml3_0_0_destroyobjectaction_isDestroyLinks_setter(instance):
    original = instance.isDestroyLinks
    instance.isDestroyLinks = original
    assert instance.isDestroyLinks == original



@given(instance=uml3_0_0_DestroyObjectAction_strategy)
def test_uml3_0_0_destroyobjectaction_isDestroyOwnedObjects_setter(instance):
    original = instance.isDestroyOwnedObjects
    instance.isDestroyOwnedObjects = original
    assert instance.isDestroyOwnedObjects == original

@given(instance=uml3_0_0_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StructuralFeatureAction)

@given(instance=uml3_0_0_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_testidentityaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TestIdentityAction)

@given(instance=uml3_0_0_OpaqueAction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_opaqueaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_OpaqueAction)



@given(instance=uml3_0_0_OpaqueAction_strategy)
def test_uml3_0_0_opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=uml3_0_0_OpaqueAction_strategy)
def test_uml3_0_0_opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=uml3_0_0_FunctionBehavior_strategy)
@settings(max_examples=50)
def test_uml3_0_0_functionbehavior_instantiation(instance):
    assert isinstance(instance, uml3_0_0_FunctionBehavior)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=uml3_0_0_LiteralString_strategy)
@settings(max_examples=50)
def test_uml3_0_0_literalstring_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LiteralString)



@given(instance=uml3_0_0_LiteralString_strategy)
def test_uml3_0_0_literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml3_0_0_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml3_0_0_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LiteralUnlimitedNatural)



@given(instance=uml3_0_0_LiteralUnlimitedNatural_strategy)
def test_uml3_0_0_literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml3_0_0_LiteralNull_strategy)
@settings(max_examples=50)
def test_uml3_0_0_literalnull_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LiteralNull)

@given(instance=uml3_0_0_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml3_0_0_literalboolean_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LiteralBoolean)



@given(instance=uml3_0_0_LiteralBoolean_strategy)
def test_uml3_0_0_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml3_0_0_LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml3_0_0_literalinteger_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LiteralInteger)



@given(instance=uml3_0_0_LiteralInteger_strategy)
def test_uml3_0_0_literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=uml3_0_0_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml3_0_0_enumerationliteral_instantiation(instance):
    assert isinstance(instance, uml3_0_0_EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=uml3_0_0_PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml3_0_0_primitivetype_instantiation(instance):
    assert isinstance(instance, uml3_0_0_PrimitiveType)

@given(instance=uml3_0_0_Enumeration_strategy)
@settings(max_examples=50)
def test_uml3_0_0_enumeration_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Enumeration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=TemplateSignature_strategy)
@settings(max_examples=50)
def test_templatesignature_instantiation(instance):
    assert isinstance(instance, TemplateSignature)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=uml3_0_0_ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3_0_0_classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ClassifierTemplateParameter)



@given(instance=uml3_0_0_ClassifierTemplateParameter_strategy)
def test_uml3_0_0_classifiertemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=uml3_0_0_ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3_0_0_connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ConnectableElementTemplateParameter)

@given(instance=uml3_0_0_OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3_0_0_operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml3_0_0_OperationTemplateParameter)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=uml3_0_0_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml3_0_0_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, uml3_0_0_EncapsulatedClassifier)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=uml3_0_0_Model_strategy)
@settings(max_examples=50)
def test_uml3_0_0_model_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Model)



@given(instance=uml3_0_0_Model_strategy)
def test_uml3_0_0_model_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original

@given(instance=uml3_0_0_Profile_strategy)
@settings(max_examples=50)
def test_uml3_0_0_profile_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Profile)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=uml3_0_0_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml3_0_0_communicationpath_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CommunicationPath)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=uml3_0_0_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml3_0_0_connectionpointreference_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ConnectionPointReference)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=uml3_0_0_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml3_0_0_extensionend_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExtensionEnd)

@given(instance=uml3_0_0_Port_strategy)
@settings(max_examples=50)
def test_uml3_0_0_port_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Port)



@given(instance=uml3_0_0_Port_strategy)
def test_uml3_0_0_port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original



@given(instance=uml3_0_0_Port_strategy)
def test_uml3_0_0_port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original

@given(instance=uml3_0_0_Pseudostate_strategy)
@settings(max_examples=50)
def test_uml3_0_0_pseudostate_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Pseudostate)



@given(instance=uml3_0_0_Pseudostate_strategy)
def test_uml3_0_0_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=uml3_0_0_OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_uml3_0_0_opaquebehavior_instantiation(instance):
    assert isinstance(instance, uml3_0_0_OpaqueBehavior)



@given(instance=uml3_0_0_OpaqueBehavior_strategy)
def test_uml3_0_0_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=uml3_0_0_OpaqueBehavior_strategy)
def test_uml3_0_0_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml3_0_0_Interaction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interaction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Interaction)

@given(instance=uml3_0_0_Activity_strategy)
@settings(max_examples=50)
def test_uml3_0_0_activity_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Activity)



@given(instance=uml3_0_0_Activity_strategy)
def test_uml3_0_0_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original



@given(instance=uml3_0_0_Activity_strategy)
def test_uml3_0_0_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=uml3_0_0_StateMachine_strategy)
@settings(max_examples=50)
def test_uml3_0_0_statemachine_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StateMachine)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=uml3_0_0_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml3_0_0_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ProtocolStateMachine)

@given(instance=uml3_0_0_Extension_strategy)
@settings(max_examples=50)
def test_uml3_0_0_extension_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Extension)



@given(instance=uml3_0_0_Extension_strategy)
def test_uml3_0_0_extension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=uml3_0_0_Actor_strategy)
@settings(max_examples=50)
def test_uml3_0_0_actor_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Actor)

@given(instance=uml3_0_0_Collaboration_strategy)
@settings(max_examples=50)
def test_uml3_0_0_collaboration_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Collaboration)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=uml3_0_0_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml3_0_0_associationclass_instantiation(instance):
    assert isinstance(instance, uml3_0_0_AssociationClass)

@given(instance=uml3_0_0_Stereotype_strategy)
@settings(max_examples=50)
def test_uml3_0_0_stereotype_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Stereotype)

@given(instance=uml3_0_0_Component_strategy)
@settings(max_examples=50)
def test_uml3_0_0_component_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Component)



@given(instance=uml3_0_0_Component_strategy)
def test_uml3_0_0_component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=uml3_0_0_Connector_strategy)
@settings(max_examples=50)
def test_uml3_0_0_connector_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Connector)



@given(instance=uml3_0_0_Connector_strategy)
def test_uml3_0_0_connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=uml3_0_0_Reception_strategy)
@settings(max_examples=50)
def test_uml3_0_0_reception_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Reception)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=uml3_0_0_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_deploymentspecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DeploymentSpecification)



@given(instance=uml3_0_0_DeploymentSpecification_strategy)
def test_uml3_0_0_deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original



@given(instance=uml3_0_0_DeploymentSpecification_strategy)
def test_uml3_0_0_deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=uml3_0_0_Class_strategy)
@settings(max_examples=50)
def test_uml3_0_0_class_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Class)



@given(instance=uml3_0_0_Class_strategy)
def test_uml3_0_0_class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=uml3_0_0_Node_strategy)
@settings(max_examples=50)
def test_uml3_0_0_node_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Node)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=uml3_0_0_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_literalspecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LiteralSpecification)

@given(instance=uml3_0_0_Interval_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interval_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Interval)

@given(instance=uml3_0_0_TimeExpression_strategy)
@settings(max_examples=50)
def test_uml3_0_0_timeexpression_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TimeExpression)

@given(instance=uml3_0_0_Duration_strategy)
@settings(max_examples=50)
def test_uml3_0_0_duration_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Duration)

@given(instance=uml3_0_0_Expression_strategy)
@settings(max_examples=50)
def test_uml3_0_0_expression_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Expression)



@given(instance=uml3_0_0_Expression_strategy)
def test_uml3_0_0_expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=uml3_0_0_InstanceValue_strategy)
@settings(max_examples=50)
def test_uml3_0_0_instancevalue_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InstanceValue)

@given(instance=uml3_0_0_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml3_0_0_opaqueexpression_instantiation(instance):
    assert isinstance(instance, uml3_0_0_OpaqueExpression)



@given(instance=uml3_0_0_OpaqueExpression_strategy)
def test_uml3_0_0_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=uml3_0_0_OpaqueExpression_strategy)
def test_uml3_0_0_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=uml3_0_0_Deployment_strategy)
@settings(max_examples=50)
def test_uml3_0_0_deployment_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Deployment)

@given(instance=uml3_0_0_Usage_strategy)
@settings(max_examples=50)
def test_uml3_0_0_usage_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Usage)

@given(instance=uml3_0_0_Abstraction_strategy)
@settings(max_examples=50)
def test_uml3_0_0_abstraction_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Abstraction)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=uml3_0_0_Manifestation_strategy)
@settings(max_examples=50)
def test_uml3_0_0_manifestation_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Manifestation)

@given(instance=uml3_0_0_Realization_strategy)
@settings(max_examples=50)
def test_uml3_0_0_realization_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Realization)

@given(instance=uml3_0_0_SendOperationEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_sendoperationevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_SendOperationEvent)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=uml3_0_0_Pin_strategy)
@settings(max_examples=50)
def test_uml3_0_0_pin_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Pin)



@given(instance=uml3_0_0_Pin_strategy)
def test_uml3_0_0_pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=uml3_0_0_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml3_0_0_connectorend_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ConnectorEnd)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=uml3_0_0_TimeEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_timeevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TimeEvent)



@given(instance=uml3_0_0_TimeEvent_strategy)
def test_uml3_0_0_timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=uml3_0_0_ChangeEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_changeevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ChangeEvent)

@given(instance=uml3_0_0_DestructionEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_destructionevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DestructionEvent)

@given(instance=uml3_0_0_MessageEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_messageevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_MessageEvent)

@given(instance=uml3_0_0_CreationEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_creationevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CreationEvent)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=uml3_0_0_Variable_strategy)
@settings(max_examples=50)
def test_uml3_0_0_variable_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Variable)

@given(instance=uml3_0_0_ExecutionEvent_strategy)
@settings(max_examples=50)
def test_uml3_0_0_executionevent_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExecutionEvent)

@given(instance=uml3_0_0_Behavior_strategy)
@settings(max_examples=50)
def test_uml3_0_0_behavior_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Behavior)



@given(instance=uml3_0_0_Behavior_strategy)
def test_uml3_0_0_behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=uml3_0_0_BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_BehaviorExecutionSpecification)

@given(instance=uml3_0_0_Parameter_strategy)
@settings(max_examples=50)
def test_uml3_0_0_parameter_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Parameter)



@given(instance=uml3_0_0_Parameter_strategy)
def test_uml3_0_0_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=uml3_0_0_Parameter_strategy)
def test_uml3_0_0_parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=uml3_0_0_Parameter_strategy)
def test_uml3_0_0_parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original



@given(instance=uml3_0_0_Parameter_strategy)
def test_uml3_0_0_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=uml3_0_0_Parameter_strategy)
def test_uml3_0_0_parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=uml3_0_0_ComponentRealization_strategy)
@settings(max_examples=50)
def test_uml3_0_0_componentrealization_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ComponentRealization)

@given(instance=uml3_0_0_InterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interfacerealization_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InterfaceRealization)

@given(instance=uml3_0_0_Property_strategy)
@settings(max_examples=50)
def test_uml3_0_0_property_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Property)



@given(instance=uml3_0_0_Property_strategy)
def test_uml3_0_0_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=uml3_0_0_Property_strategy)
def test_uml3_0_0_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=uml3_0_0_Property_strategy)
def test_uml3_0_0_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=uml3_0_0_Property_strategy)
def test_uml3_0_0_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=uml3_0_0_Property_strategy)
def test_uml3_0_0_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml3_0_0_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml3_0_0_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml3_0_0_BehavioredClassifier)

@given(instance=uml3_0_0_InformationItem_strategy)
@settings(max_examples=50)
def test_uml3_0_0_informationitem_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InformationItem)

@given(instance=uml3_0_0_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml3_0_0_structuredclassifier_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StructuredClassifier)

@given(instance=uml3_0_0_DataType_strategy)
@settings(max_examples=50)
def test_uml3_0_0_datatype_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DataType)

@given(instance=uml3_0_0_Interface_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interface_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Interface)

@given(instance=uml3_0_0_Signal_strategy)
@settings(max_examples=50)
def test_uml3_0_0_signal_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Signal)

@given(instance=uml3_0_0_Artifact_strategy)
@settings(max_examples=50)
def test_uml3_0_0_artifact_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Artifact)



@given(instance=uml3_0_0_Artifact_strategy)
def test_uml3_0_0_artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=uml3_0_0_UseCase_strategy)
@settings(max_examples=50)
def test_uml3_0_0_usecase_instantiation(instance):
    assert isinstance(instance, uml3_0_0_UseCase)

@given(instance=uml3_0_0_Substitution_strategy)
@settings(max_examples=50)
def test_uml3_0_0_substitution_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Substitution)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=uml3_0_0_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml3_0_0_extensionpoint_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExtensionPoint)

@given(instance=uml3_0_0_ActivityNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_activitynode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActivityNode)

@given(instance=uml3_0_0_RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml3_0_0_redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, uml3_0_0_RedefinableTemplateSignature)

@given(instance=uml3_0_0_ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml3_0_0_activityedge_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActivityEdge)

@given(instance=uml3_0_0_Feature_strategy)
@settings(max_examples=50)
def test_uml3_0_0_feature_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Feature)



@given(instance=uml3_0_0_Feature_strategy)
def test_uml3_0_0_feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=uml3_0_0_ObjectNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_objectnode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ObjectNode)



@given(instance=uml3_0_0_ObjectNode_strategy)
def test_uml3_0_0_objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=uml3_0_0_ObjectNode_strategy)
def test_uml3_0_0_objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=uml3_0_0_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml3_0_0_structuralfeature_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StructuralFeature)



@given(instance=uml3_0_0_StructuralFeature_strategy)
def test_uml3_0_0_structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=uml3_0_0_Generalization_strategy)
@settings(max_examples=50)
def test_uml3_0_0_generalization_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Generalization)



@given(instance=uml3_0_0_Generalization_strategy)
def test_uml3_0_0_generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=uml3_0_0_TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml3_0_0_templatebinding_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TemplateBinding)

@given(instance=uml3_0_0_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml3_0_0_protocolconformance_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ProtocolConformance)

@given(instance=uml3_0_0_PackageImport_strategy)
@settings(max_examples=50)
def test_uml3_0_0_packageimport_instantiation(instance):
    assert isinstance(instance, uml3_0_0_PackageImport)



@given(instance=uml3_0_0_PackageImport_strategy)
def test_uml3_0_0_packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml3_0_0_ElementImport_strategy)
@settings(max_examples=50)
def test_uml3_0_0_elementimport_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ElementImport)



@given(instance=uml3_0_0_ElementImport_strategy)
def test_uml3_0_0_elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=uml3_0_0_ElementImport_strategy)
def test_uml3_0_0_elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=uml3_0_0_Association_strategy)
@settings(max_examples=50)
def test_uml3_0_0_association_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Association)



@given(instance=uml3_0_0_Association_strategy)
def test_uml3_0_0_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml3_0_0_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml3_0_0_directedrelationship_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DirectedRelationship)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=uml3_0_0_ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_connectableelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ConnectableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml3_0_0_CollaborationUse_strategy)
@settings(max_examples=50)
def test_uml3_0_0_collaborationuse_instantiation(instance):
    assert isinstance(instance, uml3_0_0_CollaborationUse)

@given(instance=uml3_0_0_ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml3_0_0_activitypartition_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActivityPartition)



@given(instance=uml3_0_0_ActivityPartition_strategy)
def test_uml3_0_0_activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original



@given(instance=uml3_0_0_ActivityPartition_strategy)
def test_uml3_0_0_activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=uml3_0_0_GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml3_0_0_generalordering_instantiation(instance):
    assert isinstance(instance, uml3_0_0_GeneralOrdering)

@given(instance=uml3_0_0_Vertex_strategy)
@settings(max_examples=50)
def test_uml3_0_0_vertex_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Vertex)

@given(instance=uml3_0_0_TypedElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_typedelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TypedElement)

@given(instance=uml3_0_0_Extend_strategy)
@settings(max_examples=50)
def test_uml3_0_0_extend_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Extend)

@given(instance=uml3_0_0_RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_redefinableelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_RedefinableElement)



@given(instance=uml3_0_0_RedefinableElement_strategy)
def test_uml3_0_0_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=uml3_0_0_DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml3_0_0_deploymenttarget_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DeploymentTarget)

@given(instance=uml3_0_0_ParameterSet_strategy)
@settings(max_examples=50)
def test_uml3_0_0_parameterset_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ParameterSet)

@given(instance=uml3_0_0_DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml3_0_0_deployedartifact_instantiation(instance):
    assert isinstance(instance, uml3_0_0_DeployedArtifact)

@given(instance=uml3_0_0_InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interactionfragment_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InteractionFragment)

@given(instance=uml3_0_0_MessageEnd_strategy)
@settings(max_examples=50)
def test_uml3_0_0_messageend_instantiation(instance):
    assert isinstance(instance, uml3_0_0_MessageEnd)

@given(instance=uml3_0_0_Trigger_strategy)
@settings(max_examples=50)
def test_uml3_0_0_trigger_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Trigger)

@given(instance=uml3_0_0_Message_strategy)
@settings(max_examples=50)
def test_uml3_0_0_message_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Message)



@given(instance=uml3_0_0_Message_strategy)
def test_uml3_0_0_message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original



@given(instance=uml3_0_0_Message_strategy)
def test_uml3_0_0_message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original

@given(instance=uml3_0_0_Namespace_strategy)
@settings(max_examples=50)
def test_uml3_0_0_namespace_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Namespace)

@given(instance=uml3_0_0_Lifeline_strategy)
@settings(max_examples=50)
def test_uml3_0_0_lifeline_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Lifeline)

@given(instance=uml3_0_0_Include_strategy)
@settings(max_examples=50)
def test_uml3_0_0_include_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Include)

@given(instance=uml3_0_0_ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml3_0_0_profileapplication_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ProfileApplication)



@given(instance=uml3_0_0_ProfileApplication_strategy)
def test_uml3_0_0_profileapplication_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=uml3_0_0_PackageableElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_packageableelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_PackageableElement)

@given(instance=uml3_0_0_PackageMerge_strategy)
@settings(max_examples=50)
def test_uml3_0_0_packagemerge_instantiation(instance):
    assert isinstance(instance, uml3_0_0_PackageMerge)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=uml3_0_0_StringExpression_strategy)
@settings(max_examples=50)
def test_uml3_0_0_stringexpression_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StringExpression)

@given(instance=uml3_0_0_Operation_strategy)
@settings(max_examples=50)
def test_uml3_0_0_operation_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Operation)



@given(instance=uml3_0_0_Operation_strategy)
def test_uml3_0_0_operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=uml3_0_0_Operation_strategy)
def test_uml3_0_0_operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=uml3_0_0_Operation_strategy)
def test_uml3_0_0_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original



@given(instance=uml3_0_0_Operation_strategy)
def test_uml3_0_0_operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=uml3_0_0_Operation_strategy)
def test_uml3_0_0_operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uml3_0_0_Type_strategy)
@settings(max_examples=50)
def test_uml3_0_0_type_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Type)

@given(instance=uml3_0_0_Observation_strategy)
@settings(max_examples=50)
def test_uml3_0_0_observation_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Observation)

@given(instance=uml3_0_0_InformationFlow_strategy)
@settings(max_examples=50)
def test_uml3_0_0_informationflow_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InformationFlow)

@given(instance=uml3_0_0_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_instancespecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InstanceSpecification)

@given(instance=uml3_0_0_Event_strategy)
@settings(max_examples=50)
def test_uml3_0_0_event_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Event)

@given(instance=uml3_0_0_Dependency_strategy)
@settings(max_examples=50)
def test_uml3_0_0_dependency_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Dependency)

@given(instance=uml3_0_0_ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml3_0_0_valuespecification_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ValueSpecification)

@given(instance=uml3_0_0_Constraint_strategy)
@settings(max_examples=50)
def test_uml3_0_0_constraint_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Constraint)

@given(instance=uml3_0_0_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml3_0_0_generalizationset_instantiation(instance):
    assert isinstance(instance, uml3_0_0_GeneralizationSet)



@given(instance=uml3_0_0_GeneralizationSet_strategy)
def test_uml3_0_0_generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original



@given(instance=uml3_0_0_GeneralizationSet_strategy)
def test_uml3_0_0_generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=uml3_0_0_Transition_strategy)
@settings(max_examples=50)
def test_uml3_0_0_transition_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Transition)



@given(instance=uml3_0_0_Transition_strategy)
def test_uml3_0_0_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uml3_0_0_InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml3_0_0_interactionoperand_instantiation(instance):
    assert isinstance(instance, uml3_0_0_InteractionOperand)

@given(instance=uml3_0_0_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml3_0_0_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml3_0_0_StructuredActivityNode)



@given(instance=uml3_0_0_StructuredActivityNode_strategy)
def test_uml3_0_0_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=uml3_0_0_State_strategy)
@settings(max_examples=50)
def test_uml3_0_0_state_instantiation(instance):
    assert isinstance(instance, uml3_0_0_State)



@given(instance=uml3_0_0_State_strategy)
def test_uml3_0_0_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original



@given(instance=uml3_0_0_State_strategy)
def test_uml3_0_0_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=uml3_0_0_State_strategy)
def test_uml3_0_0_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=uml3_0_0_State_strategy)
def test_uml3_0_0_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=uml3_0_0_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml3_0_0_behavioralfeature_instantiation(instance):
    assert isinstance(instance, uml3_0_0_BehavioralFeature)



@given(instance=uml3_0_0_BehavioralFeature_strategy)
def test_uml3_0_0_behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original



@given(instance=uml3_0_0_BehavioralFeature_strategy)
def test_uml3_0_0_behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml3_0_0_Region_strategy)
@settings(max_examples=50)
def test_uml3_0_0_region_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Region)

@given(instance=uml3_0_0_Classifier_strategy)
@settings(max_examples=50)
def test_uml3_0_0_classifier_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Classifier)



@given(instance=uml3_0_0_Classifier_strategy)
def test_uml3_0_0_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml3_0_0_Package_strategy)
@settings(max_examples=50)
def test_uml3_0_0_package_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Package)

@given(instance=uml3_0_0_Element_strategy)
@settings(max_examples=50)
def test_uml3_0_0_element_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Element)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uml3_0_0_Relationship_strategy)
@settings(max_examples=50)
def test_uml3_0_0_relationship_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Relationship)

@given(instance=uml3_0_0_Clause_strategy)
@settings(max_examples=50)
def test_uml3_0_0_clause_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Clause)

@given(instance=uml3_0_0_LinkEndData_strategy)
@settings(max_examples=50)
def test_uml3_0_0_linkenddata_instantiation(instance):
    assert isinstance(instance, uml3_0_0_LinkEndData)

@given(instance=uml3_0_0_ParameterableElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_parameterableelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ParameterableElement)

@given(instance=uml3_0_0_QualifierValue_strategy)
@settings(max_examples=50)
def test_uml3_0_0_qualifiervalue_instantiation(instance):
    assert isinstance(instance, uml3_0_0_QualifierValue)

@given(instance=uml3_0_0_Image_strategy)
@settings(max_examples=50)
def test_uml3_0_0_image_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Image)



@given(instance=uml3_0_0_Image_strategy)
def test_uml3_0_0_image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=uml3_0_0_Image_strategy)
def test_uml3_0_0_image_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=uml3_0_0_Image_strategy)
def test_uml3_0_0_image_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=uml3_0_0_NamedElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_namedelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_NamedElement)



@given(instance=uml3_0_0_NamedElement_strategy)
def test_uml3_0_0_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=uml3_0_0_NamedElement_strategy)
def test_uml3_0_0_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=uml3_0_0_NamedElement_strategy)
def test_uml3_0_0_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml3_0_0_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml3_0_0_exceptionhandler_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ExceptionHandler)

@given(instance=uml3_0_0_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_multiplicityelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_MultiplicityElement)



@given(instance=uml3_0_0_MultiplicityElement_strategy)
def test_uml3_0_0_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=uml3_0_0_MultiplicityElement_strategy)
def test_uml3_0_0_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=uml3_0_0_MultiplicityElement_strategy)
def test_uml3_0_0_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=uml3_0_0_MultiplicityElement_strategy)
def test_uml3_0_0_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=uml3_0_0_ActivityGroup_strategy)
@settings(max_examples=50)
def test_uml3_0_0_activitygroup_instantiation(instance):
    assert isinstance(instance, uml3_0_0_ActivityGroup)

@given(instance=uml3_0_0_TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml3_0_0_templatesignature_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TemplateSignature)

@given(instance=uml3_0_0_TemplateableElement_strategy)
@settings(max_examples=50)
def test_uml3_0_0_templateableelement_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TemplateableElement)

@given(instance=uml3_0_0_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml3_0_0_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TemplateParameterSubstitution)

@given(instance=uml3_0_0_Slot_strategy)
@settings(max_examples=50)
def test_uml3_0_0_slot_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Slot)

@given(instance=uml3_0_0_TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3_0_0_templateparameter_instantiation(instance):
    assert isinstance(instance, uml3_0_0_TemplateParameter)

@given(instance=uml3_0_0_Comment_strategy)
@settings(max_examples=50)
def test_uml3_0_0_comment_instantiation(instance):
    assert isinstance(instance, uml3_0_0_Comment)



@given(instance=uml3_0_0_Comment_strategy)
def test_uml3_0_0_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

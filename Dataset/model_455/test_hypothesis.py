import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StructuralFeatureAction,
    uml_WriteStructuralFeatureAction,
    uml_ClearStructuralFeatureAction,
    uml_ReadStructuralFeatureAction,
    WriteStructuralFeatureAction,
    uml_RemoveStructuralFeatureValueAction,
    Node,
    uml_ExecutionEnvironment,
    uml_Device,
    CombinedFragment,
    uml_ConsiderIgnoreFragment,
    FinalNode,
    uml_ActivityFinalNode,
    uml_FlowFinalNode,
    MessageEvent,
    uml_ReceiveOperationEvent,
    uml_SendSignalEvent,
    uml_AnyReceiveEvent,
    uml_ReceiveSignalEvent,
    uml_CallEvent,
    uml_SignalEvent,
    uml_SendOperationEvent,
    Event,
    uml_CreationEvent,
    uml_DestructionEvent,
    uml_MessageEvent,
    uml_ChangeEvent,
    uml_ExecutionEvent,
    ExecutionSpecification,
    uml_BehaviorExecutionSpecification,
    uml_ActionExecutionSpecification,
    Constraint,
    uml_InteractionConstraint,
    OccurrenceSpecification,
    uml_ExecutionOccurrenceSpecification,
    MessageEnd,
    uml_MessageOccurrenceSpecification,
    InteractionUse,
    uml_PartDecomposition,
    InteractionFragment,
    uml_CombinedFragment,
    uml_ExecutionSpecification,
    uml_Continuation,
    uml_StateInvariant,
    uml_InteractionUse,
    uml_OccurrenceSpecification,
    InputPin,
    uml_ValuePin,
    uml_Gate,
    StructuredActivityNode,
    uml_SequenceNode,
    CallAction,
    uml_CallBehaviorAction,
    uml_CallOperationAction,
    InvocationAction,
    uml_SendSignalAction,
    uml_CallAction,
    ObjectNode,
    uml_CentralBufferNode,
    Pin,
    uml_ActivityParameterNode,
    ControlNode,
    uml_FinalNode,
    uml_ForkNode,
    uml_DecisionNode,
    uml_MergeNode,
    uml_InitialNode,
    ActivityEdge,
    uml_ObjectFlow,
    uml_ControlFlow,
    ActivityGroup,
    uml_InterruptibleActivityRegion,
    ActivityNode,
    uml_ControlNode,
    uml_ExecutableNode,
    ExecutableNode,
    uml_Action,
    uml_OutputPin,
    uml_InputPin,
    Action,
    uml_StructuralFeatureAction,
    uml_InvocationAction,
    uml_CreateObjectAction,
    uml_TestIdentityAction,
    uml_DestroyObjectAction,
    uml_ReadSelfAction,
    uml_OpaqueAction,
    OpaqueBehavior,
    uml_FunctionBehavior,
    InstanceSpecification,
    LiteralSpecification,
    uml_LiteralUnlimitedNatural,
    uml_LiteralString,
    uml_LiteralNull,
    uml_LiteralBoolean,
    uml_LiteralInteger,
    uml_EnumerationLiteral,
    DataType,
    uml_PrimitiveType,
    uml_Enumeration,
    Transition,
    uml_ProtocolTransition,
    uml_ExpansionRegion,
    uml_ExpansionNode,
    uml_LoopNode,
    uml_ConditionalNode,
    CentralBufferNode,
    uml_DataStoreNode,
    uml_JoinNode,
    uml_StartObjectBehaviorAction,
    uml_ReduceAction,
    uml_UnmarshallAction,
    uml_ReplyAction,
    AcceptEventAction,
    uml_AcceptCallAction,
    uml_AcceptEventAction,
    CreateLinkAction,
    uml_CreateLinkObjectAction,
    uml_ReadLinkObjectEndQualifierAction,
    uml_StartClassifierBehaviorAction,
    uml_ReadIsClassifiedObjectAction,
    uml_ReclassifyObjectAction,
    uml_ReadLinkObjectEndAction,
    uml_ReadExtentAction,
    uml_ActionInputPin,
    uml_RaiseExceptionAction,
    WriteVariableAction,
    uml_RemoveVariableValueAction,
    uml_AddVariableValueAction,
    VariableAction,
    uml_ClearVariableAction,
    uml_WriteVariableAction,
    uml_ReadVariableAction,
    uml_VariableAction,
    uml_TimeEvent,
    State,
    uml_FinalState,
    Observation,
    uml_DurationObservation,
    uml_TimeObservation,
    uml_IntervalConstraint,
    IntervalConstraint,
    uml_DurationConstraint,
    uml_TimeConstraint,
    Interval,
    uml_TimeInterval,
    uml_DurationInterval,
    uml_ValueSpecificationAction,
    uml_SendObjectAction,
    uml_BroadcastSignalAction,
    uml_ClearAssociationAction,
    WriteLinkAction,
    uml_DestroyLinkAction,
    uml_CreateLinkAction,
    LinkEndData,
    uml_LinkEndDestructionData,
    uml_LinkEndCreationData,
    LinkAction,
    uml_WriteLinkAction,
    uml_ReadLinkAction,
    uml_LinkAction,
    uml_AddStructuralFeatureValueAction,
    TemplateSignature,
    Expression,
    TemplateParameter,
    uml_ConnectableElementTemplateParameter,
    uml_ClassifierTemplateParameter,
    uml_OperationTemplateParameter,
    Association,
    uml_CommunicationPath,
    Package,
    uml_Model,
    uml_Profile,
    StructuredClassifier,
    uml_EncapsulatedClassifier,
    Vertex,
    Property,
    uml_ExtensionEnd,
    uml_Port,
    uml_ConnectionPointReference,
    uml_Pseudostate,
    Behavior,
    uml_Activity,
    uml_OpaqueBehavior,
    uml_Interaction,
    uml_StateMachine,
    StateMachine,
    uml_ProtocolStateMachine,
    Class,
    uml_Component,
    uml_AssociationClass,
    uml_Stereotype,
    uml_Extension,
    BehavioredClassifier,
    uml_Collaboration,
    uml_Actor,
    EncapsulatedClassifier,
    BehavioralFeature,
    uml_Reception,
    Feature,
    uml_Connector,
    DeployedArtifact,
    Artifact,
    uml_DeploymentSpecification,
    uml_Class,
    DeploymentTarget,
    uml_Node,
    StructuralFeature,
    Realization,
    uml_InterfaceRealization,
    uml_ComponentRealization,
    MultiplicityElement,
    uml_Pin,
    uml_ConnectorEnd,
    ConnectableElement,
    uml_Variable,
    uml_Behavior,
    uml_Parameter,
    ValueSpecification,
    uml_LiteralSpecification,
    uml_Interval,
    uml_TimeExpression,
    uml_InstanceValue,
    uml_Expression,
    uml_Duration,
    uml_OpaqueExpression,
    Dependency,
    uml_Usage,
    uml_Deployment,
    uml_Abstraction,
    Abstraction,
    uml_Manifestation,
    uml_Realization,
    uml_UseCase,
    uml_Substitution,
    uml_Property,
    Classifier,
    uml_InformationItem,
    uml_Signal,
    uml_Interface,
    uml_Artifact,
    uml_DataType,
    uml_StructuredClassifier,
    uml_BehavioredClassifier,
    TypedElement,
    uml_ObjectNode,
    uml_StructuralFeature,
    Type,
    RedefinableElement,
    uml_Feature,
    uml_ExtensionPoint,
    uml_ActivityNode,
    uml_RedefinableTemplateSignature,
    uml_ActivityEdge,
    ParameterableElement,
    uml_ConnectableElement,
    NamedElement,
    uml_GeneralOrdering,
    uml_CollaborationUse,
    uml_MessageEnd,
    uml_Message,
    uml_ActivityPartition,
    uml_Lifeline,
    uml_Trigger,
    uml_TypedElement,
    uml_Vertex,
    uml_ParameterSet,
    uml_DeploymentTarget,
    uml_Namespace,
    uml_InteractionFragment,
    uml_DeployedArtifact,
    uml_RedefinableElement,
    uml_PackageableElement,
    TemplateableElement,
    uml_Operation,
    PackageableElement,
    uml_GeneralizationSet,
    uml_Constraint,
    uml_Event,
    uml_ValueSpecification,
    uml_Type,
    uml_InstanceSpecification,
    uml_Observation,
    Namespace,
    uml_InteractionOperand,
    uml_Transition,
    uml_Region,
    uml_StructuredActivityNode,
    uml_BehavioralFeature,
    uml_State,
    uml_Classifier,
    uml_Package,
    Relationship,
    uml_Association,
    uml_DirectedRelationship,
    DirectedRelationship,
    uml_Generalization,
    uml_ProtocolConformance,
    uml_PackageImport,
    uml_InformationFlow,
    uml_TemplateBinding,
    uml_ElementImport,
    uml_Extend,
    uml_PackageMerge,
    uml_ProfileApplication,
    uml_Include,
    uml_Dependency,
    uml_StringExpression,
    Element,
    uml_TemplateSignature,
    uml_Image,
    uml_TemplateParameterSubstitution,
    uml_ParameterableElement,
    uml_TemplateParameter,
    uml_MultiplicityElement,
    uml_TemplateableElement,
    uml_ExceptionHandler,
    uml_Clause,
    uml_Relationship,
    uml_NamedElement,
    uml_ActivityGroup,
    uml_QualifierValue,
    uml_Slot,
    uml_LinkEndData,
    uml_Comment,
    EModelElement,
    uml_Element,
    ParameterEffectKind,
    MessageSort,
    ObjectNodeOrderingKind,
    InteractionOperatorKind,
    AggregationKind,
    ExpansionKind,
    ParameterDirectionKind,
    VisibilityKind,
    PseudostateKind,
    CallConcurrencyKind,
    ConnectorKind,
    TransitionKind,
    MessageKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_WriteStructuralFeatureAction)


def test_uml_writestructuralfeatureaction_constructor_exists():
    assert callable(uml_WriteStructuralFeatureAction.__init__)


def test_uml_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_ClearStructuralFeatureAction)


def test_uml_clearstructuralfeatureaction_constructor_exists():
    assert callable(uml_ClearStructuralFeatureAction.__init__)


def test_uml_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadStructuralFeatureAction)


def test_uml_readstructuralfeatureaction_constructor_exists():
    assert callable(uml_ReadStructuralFeatureAction.__init__)


def test_uml_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_RemoveStructuralFeatureValueAction)


def test_uml_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_RemoveStructuralFeatureValueAction.__init__)


def test_uml_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml_removestructuralfeaturevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml_RemoveStructuralFeatureValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml_RemoveStructuralFeatureValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(uml_ExecutionEnvironment)


def test_uml_executionenvironment_constructor_exists():
    assert callable(uml_ExecutionEnvironment.__init__)


def test_uml_executionenvironment_constructor_args():
    sig = inspect.signature(uml_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml_device_is_not_abstract():
    assert not inspect.isabstract(uml_Device)


def test_uml_device_constructor_exists():
    assert callable(uml_Device.__init__)


def test_uml_device_constructor_args():
    sig = inspect.signature(uml_Device.__init__)
    params = list(sig.parameters.keys())



def test_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(uml_ConsiderIgnoreFragment)


def test_uml_considerignorefragment_constructor_exists():
    assert callable(uml_ConsiderIgnoreFragment.__init__)


def test_uml_considerignorefragment_constructor_args():
    sig = inspect.signature(uml_ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityFinalNode)


def test_uml_activityfinalnode_constructor_exists():
    assert callable(uml_ActivityFinalNode.__init__)


def test_uml_activityfinalnode_constructor_args():
    sig = inspect.signature(uml_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_FlowFinalNode)


def test_uml_flowfinalnode_constructor_exists():
    assert callable(uml_FlowFinalNode.__init__)


def test_uml_flowfinalnode_constructor_args():
    sig = inspect.signature(uml_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_receiveoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml_ReceiveOperationEvent)


def test_uml_receiveoperationevent_constructor_exists():
    assert callable(uml_ReceiveOperationEvent.__init__)


def test_uml_receiveoperationevent_constructor_args():
    sig = inspect.signature(uml_ReceiveOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_sendsignalevent_is_not_abstract():
    assert not inspect.isabstract(uml_SendSignalEvent)


def test_uml_sendsignalevent_constructor_exists():
    assert callable(uml_SendSignalEvent.__init__)


def test_uml_sendsignalevent_constructor_args():
    sig = inspect.signature(uml_SendSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml_AnyReceiveEvent)


def test_uml_anyreceiveevent_constructor_exists():
    assert callable(uml_AnyReceiveEvent.__init__)


def test_uml_anyreceiveevent_constructor_args():
    sig = inspect.signature(uml_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_receivesignalevent_is_not_abstract():
    assert not inspect.isabstract(uml_ReceiveSignalEvent)


def test_uml_receivesignalevent_constructor_exists():
    assert callable(uml_ReceiveSignalEvent.__init__)


def test_uml_receivesignalevent_constructor_args():
    sig = inspect.signature(uml_ReceiveSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_callevent_is_not_abstract():
    assert not inspect.isabstract(uml_CallEvent)


def test_uml_callevent_constructor_exists():
    assert callable(uml_CallEvent.__init__)


def test_uml_callevent_constructor_args():
    sig = inspect.signature(uml_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_signalevent_is_not_abstract():
    assert not inspect.isabstract(uml_SignalEvent)


def test_uml_signalevent_constructor_exists():
    assert callable(uml_SignalEvent.__init__)


def test_uml_signalevent_constructor_args():
    sig = inspect.signature(uml_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_sendoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml_SendOperationEvent)


def test_uml_sendoperationevent_constructor_exists():
    assert callable(uml_SendOperationEvent.__init__)


def test_uml_sendoperationevent_constructor_args():
    sig = inspect.signature(uml_SendOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_uml_creationevent_is_not_abstract():
    assert not inspect.isabstract(uml_CreationEvent)


def test_uml_creationevent_constructor_exists():
    assert callable(uml_CreationEvent.__init__)


def test_uml_creationevent_constructor_args():
    sig = inspect.signature(uml_CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_destructionevent_is_not_abstract():
    assert not inspect.isabstract(uml_DestructionEvent)


def test_uml_destructionevent_constructor_exists():
    assert callable(uml_DestructionEvent.__init__)


def test_uml_destructionevent_constructor_args():
    sig = inspect.signature(uml_DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_messageevent_is_not_abstract():
    assert not inspect.isabstract(uml_MessageEvent)


def test_uml_messageevent_constructor_exists():
    assert callable(uml_MessageEvent.__init__)


def test_uml_messageevent_constructor_args():
    sig = inspect.signature(uml_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_changeevent_is_not_abstract():
    assert not inspect.isabstract(uml_ChangeEvent)


def test_uml_changeevent_constructor_exists():
    assert callable(uml_ChangeEvent.__init__)


def test_uml_changeevent_constructor_args():
    sig = inspect.signature(uml_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_executionevent_is_not_abstract():
    assert not inspect.isabstract(uml_ExecutionEvent)


def test_uml_executionevent_constructor_exists():
    assert callable(uml_ExecutionEvent.__init__)


def test_uml_executionevent_constructor_args():
    sig = inspect.signature(uml_ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_BehaviorExecutionSpecification)


def test_uml_behaviorexecutionspecification_constructor_exists():
    assert callable(uml_BehaviorExecutionSpecification.__init__)


def test_uml_behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml_BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_ActionExecutionSpecification)


def test_uml_actionexecutionspecification_constructor_exists():
    assert callable(uml_ActionExecutionSpecification.__init__)


def test_uml_actionexecutionspecification_constructor_args():
    sig = inspect.signature(uml_ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_InteractionConstraint)


def test_uml_interactionconstraint_constructor_exists():
    assert callable(uml_InteractionConstraint.__init__)


def test_uml_interactionconstraint_constructor_args():
    sig = inspect.signature(uml_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_ExecutionOccurrenceSpecification)


def test_uml_executionoccurrencespecification_constructor_exists():
    assert callable(uml_ExecutionOccurrenceSpecification.__init__)


def test_uml_executionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_MessageOccurrenceSpecification)


def test_uml_messageoccurrencespecification_constructor_exists():
    assert callable(uml_MessageOccurrenceSpecification.__init__)


def test_uml_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionuse_is_not_abstract():
    assert not inspect.isabstract(InteractionUse)


def test_interactionuse_constructor_exists():
    assert callable(InteractionUse.__init__)


def test_interactionuse_constructor_args():
    sig = inspect.signature(InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml_partdecomposition_is_not_abstract():
    assert not inspect.isabstract(uml_PartDecomposition)


def test_uml_partdecomposition_constructor_exists():
    assert callable(uml_PartDecomposition.__init__)


def test_uml_partdecomposition_constructor_args():
    sig = inspect.signature(uml_PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml_CombinedFragment)


def test_uml_combinedfragment_constructor_exists():
    assert callable(uml_CombinedFragment.__init__)


def test_uml_combinedfragment_constructor_args():
    sig = inspect.signature(uml_CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_uml_combinedfragment_has_interactionOperator():
    assert hasattr(uml_CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in uml_CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_uml_executionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_ExecutionSpecification)


def test_uml_executionspecification_constructor_exists():
    assert callable(uml_ExecutionSpecification.__init__)


def test_uml_executionspecification_constructor_args():
    sig = inspect.signature(uml_ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_continuation_is_not_abstract():
    assert not inspect.isabstract(uml_Continuation)


def test_uml_continuation_constructor_exists():
    assert callable(uml_Continuation.__init__)


def test_uml_continuation_constructor_args():
    sig = inspect.signature(uml_Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_uml_continuation_has_setting():
    assert hasattr(uml_Continuation, "setting")
    descriptor = None
    for klass in uml_Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_uml_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml_StateInvariant)


def test_uml_stateinvariant_constructor_exists():
    assert callable(uml_StateInvariant.__init__)


def test_uml_stateinvariant_constructor_args():
    sig = inspect.signature(uml_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml_interactionuse_is_not_abstract():
    assert not inspect.isabstract(uml_InteractionUse)


def test_uml_interactionuse_constructor_exists():
    assert callable(uml_InteractionUse.__init__)


def test_uml_interactionuse_constructor_args():
    sig = inspect.signature(uml_InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_OccurrenceSpecification)


def test_uml_occurrencespecification_constructor_exists():
    assert callable(uml_OccurrenceSpecification.__init__)


def test_uml_occurrencespecification_constructor_args():
    sig = inspect.signature(uml_OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_valuepin_is_not_abstract():
    assert not inspect.isabstract(uml_ValuePin)


def test_uml_valuepin_constructor_exists():
    assert callable(uml_ValuePin.__init__)


def test_uml_valuepin_constructor_args():
    sig = inspect.signature(uml_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml_gate_is_not_abstract():
    assert not inspect.isabstract(uml_Gate)


def test_uml_gate_constructor_exists():
    assert callable(uml_Gate.__init__)


def test_uml_gate_constructor_args():
    sig = inspect.signature(uml_Gate.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_sequencenode_is_not_abstract():
    assert not inspect.isabstract(uml_SequenceNode)


def test_uml_sequencenode_constructor_exists():
    assert callable(uml_SequenceNode.__init__)


def test_uml_sequencenode_constructor_args():
    sig = inspect.signature(uml_SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_CallBehaviorAction)


def test_uml_callbehavioraction_constructor_exists():
    assert callable(uml_CallBehaviorAction.__init__)


def test_uml_callbehavioraction_constructor_args():
    sig = inspect.signature(uml_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml_CallOperationAction)


def test_uml_calloperationaction_constructor_exists():
    assert callable(uml_CallOperationAction.__init__)


def test_uml_calloperationaction_constructor_args():
    sig = inspect.signature(uml_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_SendSignalAction)


def test_uml_sendsignalaction_constructor_exists():
    assert callable(uml_SendSignalAction.__init__)


def test_uml_sendsignalaction_constructor_args():
    sig = inspect.signature(uml_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_callaction_is_not_abstract():
    assert not inspect.isabstract(uml_CallAction)


def test_uml_callaction_constructor_exists():
    assert callable(uml_CallAction.__init__)


def test_uml_callaction_constructor_args():
    sig = inspect.signature(uml_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_uml_callaction_has_isSynchronous():
    assert hasattr(uml_CallAction, "isSynchronous")
    descriptor = None
    for klass in uml_CallAction.__mro__:
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



def test_uml_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml_CentralBufferNode)


def test_uml_centralbuffernode_constructor_exists():
    assert callable(uml_CentralBufferNode.__init__)


def test_uml_centralbuffernode_constructor_args():
    sig = inspect.signature(uml_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityParameterNode)


def test_uml_activityparameternode_constructor_exists():
    assert callable(uml_ActivityParameterNode.__init__)


def test_uml_activityparameternode_constructor_args():
    sig = inspect.signature(uml_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_finalnode_is_not_abstract():
    assert not inspect.isabstract(uml_FinalNode)


def test_uml_finalnode_constructor_exists():
    assert callable(uml_FinalNode.__init__)


def test_uml_finalnode_constructor_args():
    sig = inspect.signature(uml_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_forknode_is_not_abstract():
    assert not inspect.isabstract(uml_ForkNode)


def test_uml_forknode_constructor_exists():
    assert callable(uml_ForkNode.__init__)


def test_uml_forknode_constructor_args():
    sig = inspect.signature(uml_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_decisionnode_is_not_abstract():
    assert not inspect.isabstract(uml_DecisionNode)


def test_uml_decisionnode_constructor_exists():
    assert callable(uml_DecisionNode.__init__)


def test_uml_decisionnode_constructor_args():
    sig = inspect.signature(uml_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_mergenode_is_not_abstract():
    assert not inspect.isabstract(uml_MergeNode)


def test_uml_mergenode_constructor_exists():
    assert callable(uml_MergeNode.__init__)


def test_uml_mergenode_constructor_args():
    sig = inspect.signature(uml_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_initialnode_is_not_abstract():
    assert not inspect.isabstract(uml_InitialNode)


def test_uml_initialnode_constructor_exists():
    assert callable(uml_InitialNode.__init__)


def test_uml_initialnode_constructor_args():
    sig = inspect.signature(uml_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml_objectflow_is_not_abstract():
    assert not inspect.isabstract(uml_ObjectFlow)


def test_uml_objectflow_constructor_exists():
    assert callable(uml_ObjectFlow.__init__)


def test_uml_objectflow_constructor_args():
    sig = inspect.signature(uml_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"

def test_uml_objectflow_has_isMulticast():
    assert hasattr(uml_ObjectFlow, "isMulticast")
    descriptor = None
    for klass in uml_ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_uml_objectflow_has_isMultireceive():
    assert hasattr(uml_ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in uml_ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)



def test_uml_controlflow_is_not_abstract():
    assert not inspect.isabstract(uml_ControlFlow)


def test_uml_controlflow_constructor_exists():
    assert callable(uml_ControlFlow.__init__)


def test_uml_controlflow_constructor_args():
    sig = inspect.signature(uml_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml_InterruptibleActivityRegion)


def test_uml_interruptibleactivityregion_constructor_exists():
    assert callable(uml_InterruptibleActivityRegion.__init__)


def test_uml_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_controlnode_is_not_abstract():
    assert not inspect.isabstract(uml_ControlNode)


def test_uml_controlnode_constructor_exists():
    assert callable(uml_ControlNode.__init__)


def test_uml_controlnode_constructor_args():
    sig = inspect.signature(uml_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_executablenode_is_not_abstract():
    assert not inspect.isabstract(uml_ExecutableNode)


def test_uml_executablenode_constructor_exists():
    assert callable(uml_ExecutableNode.__init__)


def test_uml_executablenode_constructor_args():
    sig = inspect.signature(uml_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_action_is_not_abstract():
    assert not inspect.isabstract(uml_Action)


def test_uml_action_constructor_exists():
    assert callable(uml_Action.__init__)


def test_uml_action_constructor_args():
    sig = inspect.signature(uml_Action.__init__)
    params = list(sig.parameters.keys())



def test_uml_outputpin_is_not_abstract():
    assert not inspect.isabstract(uml_OutputPin)


def test_uml_outputpin_constructor_exists():
    assert callable(uml_OutputPin.__init__)


def test_uml_outputpin_constructor_args():
    sig = inspect.signature(uml_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_inputpin_is_not_abstract():
    assert not inspect.isabstract(uml_InputPin)


def test_uml_inputpin_constructor_exists():
    assert callable(uml_InputPin.__init__)


def test_uml_inputpin_constructor_args():
    sig = inspect.signature(uml_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_StructuralFeatureAction)


def test_uml_structuralfeatureaction_constructor_exists():
    assert callable(uml_StructuralFeatureAction.__init__)


def test_uml_structuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_invocationaction_is_not_abstract():
    assert not inspect.isabstract(uml_InvocationAction)


def test_uml_invocationaction_constructor_exists():
    assert callable(uml_InvocationAction.__init__)


def test_uml_invocationaction_constructor_args():
    sig = inspect.signature(uml_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_CreateObjectAction)


def test_uml_createobjectaction_constructor_exists():
    assert callable(uml_CreateObjectAction.__init__)


def test_uml_createobjectaction_constructor_args():
    sig = inspect.signature(uml_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml_TestIdentityAction)


def test_uml_testidentityaction_constructor_exists():
    assert callable(uml_TestIdentityAction.__init__)


def test_uml_testidentityaction_constructor_args():
    sig = inspect.signature(uml_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_DestroyObjectAction)


def test_uml_destroyobjectaction_constructor_exists():
    assert callable(uml_DestroyObjectAction.__init__)


def test_uml_destroyobjectaction_constructor_args():
    sig = inspect.signature(uml_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyOwnedObjects" in params, "Missing parameter 'isDestroyOwnedObjects'"
    assert "isDestroyLinks" in params, "Missing parameter 'isDestroyLinks'"

def test_uml_destroyobjectaction_has_isDestroyOwnedObjects():
    assert hasattr(uml_DestroyObjectAction, "isDestroyOwnedObjects")
    descriptor = None
    for klass in uml_DestroyObjectAction.__mro__:
        if "isDestroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)

def test_uml_destroyobjectaction_has_isDestroyLinks():
    assert hasattr(uml_DestroyObjectAction, "isDestroyLinks")
    descriptor = None
    for klass in uml_DestroyObjectAction.__mro__:
        if "isDestroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyLinks"]
            break
    assert isinstance(descriptor, property)



def test_uml_readselfaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadSelfAction)


def test_uml_readselfaction_constructor_exists():
    assert callable(uml_ReadSelfAction.__init__)


def test_uml_readselfaction_constructor_args():
    sig = inspect.signature(uml_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml_OpaqueAction)


def test_uml_opaqueaction_constructor_exists():
    assert callable(uml_OpaqueAction.__init__)


def test_uml_opaqueaction_constructor_args():
    sig = inspect.signature(uml_OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml_opaqueaction_has_body():
    assert hasattr(uml_OpaqueAction, "body")
    descriptor = None
    for klass in uml_OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml_opaqueaction_has_language():
    assert hasattr(uml_OpaqueAction, "language")
    descriptor = None
    for klass in uml_OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(uml_FunctionBehavior)


def test_uml_functionbehavior_constructor_exists():
    assert callable(uml_FunctionBehavior.__init__)


def test_uml_functionbehavior_constructor_args():
    sig = inspect.signature(uml_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml_LiteralUnlimitedNatural)


def test_uml_literalunlimitednatural_constructor_exists():
    assert callable(uml_LiteralUnlimitedNatural.__init__)


def test_uml_literalunlimitednatural_constructor_args():
    sig = inspect.signature(uml_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml_literalunlimitednatural_has_value():
    assert hasattr(uml_LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in uml_LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml_literalstring_is_not_abstract():
    assert not inspect.isabstract(uml_LiteralString)


def test_uml_literalstring_constructor_exists():
    assert callable(uml_LiteralString.__init__)


def test_uml_literalstring_constructor_args():
    sig = inspect.signature(uml_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml_literalstring_has_value():
    assert hasattr(uml_LiteralString, "value")
    descriptor = None
    for klass in uml_LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml_literalnull_is_not_abstract():
    assert not inspect.isabstract(uml_LiteralNull)


def test_uml_literalnull_constructor_exists():
    assert callable(uml_LiteralNull.__init__)


def test_uml_literalnull_constructor_args():
    sig = inspect.signature(uml_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml_literalboolean_is_not_abstract():
    assert not inspect.isabstract(uml_LiteralBoolean)


def test_uml_literalboolean_constructor_exists():
    assert callable(uml_LiteralBoolean.__init__)


def test_uml_literalboolean_constructor_args():
    sig = inspect.signature(uml_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml_literalboolean_has_value():
    assert hasattr(uml_LiteralBoolean, "value")
    descriptor = None
    for klass in uml_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml_literalinteger_is_not_abstract():
    assert not inspect.isabstract(uml_LiteralInteger)


def test_uml_literalinteger_constructor_exists():
    assert callable(uml_LiteralInteger.__init__)


def test_uml_literalinteger_constructor_args():
    sig = inspect.signature(uml_LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml_literalinteger_has_value():
    assert hasattr(uml_LiteralInteger, "value")
    descriptor = None
    for klass in uml_LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml_EnumerationLiteral)


def test_uml_enumerationliteral_constructor_exists():
    assert callable(uml_EnumerationLiteral.__init__)


def test_uml_enumerationliteral_constructor_args():
    sig = inspect.signature(uml_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml_primitivetype_is_not_abstract():
    assert not inspect.isabstract(uml_PrimitiveType)


def test_uml_primitivetype_constructor_exists():
    assert callable(uml_PrimitiveType.__init__)


def test_uml_primitivetype_constructor_args():
    sig = inspect.signature(uml_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml_enumeration_is_not_abstract():
    assert not inspect.isabstract(uml_Enumeration)


def test_uml_enumeration_constructor_exists():
    assert callable(uml_Enumeration.__init__)


def test_uml_enumeration_constructor_args():
    sig = inspect.signature(uml_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(uml_ProtocolTransition)


def test_uml_protocoltransition_constructor_exists():
    assert callable(uml_ProtocolTransition.__init__)


def test_uml_protocoltransition_constructor_args():
    sig = inspect.signature(uml_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml_expansionregion_is_not_abstract():
    assert not inspect.isabstract(uml_ExpansionRegion)


def test_uml_expansionregion_constructor_exists():
    assert callable(uml_ExpansionRegion.__init__)


def test_uml_expansionregion_constructor_args():
    sig = inspect.signature(uml_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_uml_expansionregion_has_mode():
    assert hasattr(uml_ExpansionRegion, "mode")
    descriptor = None
    for klass in uml_ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_uml_expansionnode_is_not_abstract():
    assert not inspect.isabstract(uml_ExpansionNode)


def test_uml_expansionnode_constructor_exists():
    assert callable(uml_ExpansionNode.__init__)


def test_uml_expansionnode_constructor_args():
    sig = inspect.signature(uml_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_loopnode_is_not_abstract():
    assert not inspect.isabstract(uml_LoopNode)


def test_uml_loopnode_constructor_exists():
    assert callable(uml_LoopNode.__init__)


def test_uml_loopnode_constructor_args():
    sig = inspect.signature(uml_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_uml_loopnode_has_isTestedFirst():
    assert hasattr(uml_LoopNode, "isTestedFirst")
    descriptor = None
    for klass in uml_LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_uml_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(uml_ConditionalNode)


def test_uml_conditionalnode_constructor_exists():
    assert callable(uml_ConditionalNode.__init__)


def test_uml_conditionalnode_constructor_args():
    sig = inspect.signature(uml_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssured" in params, "Missing parameter 'isAssured'"

def test_uml_conditionalnode_has_isDeterminate():
    assert hasattr(uml_ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in uml_ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_uml_conditionalnode_has_isAssured():
    assert hasattr(uml_ConditionalNode, "isAssured")
    descriptor = None
    for klass in uml_ConditionalNode.__mro__:
        if "isAssured" in klass.__dict__:
            descriptor = klass.__dict__["isAssured"]
            break
    assert isinstance(descriptor, property)



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_datastorenode_is_not_abstract():
    assert not inspect.isabstract(uml_DataStoreNode)


def test_uml_datastorenode_constructor_exists():
    assert callable(uml_DataStoreNode.__init__)


def test_uml_datastorenode_constructor_args():
    sig = inspect.signature(uml_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_joinnode_is_not_abstract():
    assert not inspect.isabstract(uml_JoinNode)


def test_uml_joinnode_constructor_exists():
    assert callable(uml_JoinNode.__init__)


def test_uml_joinnode_constructor_args():
    sig = inspect.signature(uml_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_uml_joinnode_has_isCombineDuplicate():
    assert hasattr(uml_JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in uml_JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_uml_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_StartObjectBehaviorAction)


def test_uml_startobjectbehavioraction_constructor_exists():
    assert callable(uml_StartObjectBehaviorAction.__init__)


def test_uml_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_reduceaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReduceAction)


def test_uml_reduceaction_constructor_exists():
    assert callable(uml_ReduceAction.__init__)


def test_uml_reduceaction_constructor_args():
    sig = inspect.signature(uml_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_uml_reduceaction_has_isOrdered():
    assert hasattr(uml_ReduceAction, "isOrdered")
    descriptor = None
    for klass in uml_ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_uml_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml_UnmarshallAction)


def test_uml_unmarshallaction_constructor_exists():
    assert callable(uml_UnmarshallAction.__init__)


def test_uml_unmarshallaction_constructor_args():
    sig = inspect.signature(uml_UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_replyaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReplyAction)


def test_uml_replyaction_constructor_exists():
    assert callable(uml_ReplyAction.__init__)


def test_uml_replyaction_constructor_args():
    sig = inspect.signature(uml_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(uml_AcceptCallAction)


def test_uml_acceptcallaction_constructor_exists():
    assert callable(uml_AcceptCallAction.__init__)


def test_uml_acceptcallaction_constructor_args():
    sig = inspect.signature(uml_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml_AcceptEventAction)


def test_uml_accepteventaction_constructor_exists():
    assert callable(uml_AcceptEventAction.__init__)


def test_uml_accepteventaction_constructor_args():
    sig = inspect.signature(uml_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_uml_accepteventaction_has_isUnmarshall():
    assert hasattr(uml_AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in uml_AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_CreateLinkObjectAction)


def test_uml_createlinkobjectaction_constructor_exists():
    assert callable(uml_CreateLinkObjectAction.__init__)


def test_uml_createlinkobjectaction_constructor_args():
    sig = inspect.signature(uml_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadLinkObjectEndQualifierAction)


def test_uml_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml_ReadLinkObjectEndQualifierAction.__init__)


def test_uml_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_StartClassifierBehaviorAction)


def test_uml_startclassifierbehavioraction_constructor_exists():
    assert callable(uml_StartClassifierBehaviorAction.__init__)


def test_uml_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadIsClassifiedObjectAction)


def test_uml_readisclassifiedobjectaction_constructor_exists():
    assert callable(uml_ReadIsClassifiedObjectAction.__init__)


def test_uml_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDirect" in params, "Missing parameter 'isDirect'"

def test_uml_readisclassifiedobjectaction_has_isDirect():
    assert hasattr(uml_ReadIsClassifiedObjectAction, "isDirect")
    descriptor = None
    for klass in uml_ReadIsClassifiedObjectAction.__mro__:
        if "isDirect" in klass.__dict__:
            descriptor = klass.__dict__["isDirect"]
            break
    assert isinstance(descriptor, property)



def test_uml_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReclassifyObjectAction)


def test_uml_reclassifyobjectaction_constructor_exists():
    assert callable(uml_ReclassifyObjectAction.__init__)


def test_uml_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml_reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(uml_ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in uml_ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadLinkObjectEndAction)


def test_uml_readlinkobjectendaction_constructor_exists():
    assert callable(uml_ReadLinkObjectEndAction.__init__)


def test_uml_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_readextentaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadExtentAction)


def test_uml_readextentaction_constructor_exists():
    assert callable(uml_ReadExtentAction.__init__)


def test_uml_readextentaction_constructor_args():
    sig = inspect.signature(uml_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_actioninputpin_is_not_abstract():
    assert not inspect.isabstract(uml_ActionInputPin)


def test_uml_actioninputpin_constructor_exists():
    assert callable(uml_ActionInputPin.__init__)


def test_uml_actioninputpin_constructor_args():
    sig = inspect.signature(uml_ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml_RaiseExceptionAction)


def test_uml_raiseexceptionaction_constructor_exists():
    assert callable(uml_RaiseExceptionAction.__init__)


def test_uml_raiseexceptionaction_constructor_args():
    sig = inspect.signature(uml_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_RemoveVariableValueAction)


def test_uml_removevariablevalueaction_constructor_exists():
    assert callable(uml_RemoveVariableValueAction.__init__)


def test_uml_removevariablevalueaction_constructor_args():
    sig = inspect.signature(uml_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml_removevariablevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml_RemoveVariableValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml_RemoveVariableValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_uml_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_AddVariableValueAction)


def test_uml_addvariablevalueaction_constructor_exists():
    assert callable(uml_AddVariableValueAction.__init__)


def test_uml_addvariablevalueaction_constructor_args():
    sig = inspect.signature(uml_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml_addvariablevalueaction_has_isReplaceAll():
    assert hasattr(uml_AddVariableValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml_AddVariableValueAction.__mro__:
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



def test_uml_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_ClearVariableAction)


def test_uml_clearvariableaction_constructor_exists():
    assert callable(uml_ClearVariableAction.__init__)


def test_uml_clearvariableaction_constructor_args():
    sig = inspect.signature(uml_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_WriteVariableAction)


def test_uml_writevariableaction_constructor_exists():
    assert callable(uml_WriteVariableAction.__init__)


def test_uml_writevariableaction_constructor_args():
    sig = inspect.signature(uml_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadVariableAction)


def test_uml_readvariableaction_constructor_exists():
    assert callable(uml_ReadVariableAction.__init__)


def test_uml_readvariableaction_constructor_args():
    sig = inspect.signature(uml_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_variableaction_is_not_abstract():
    assert not inspect.isabstract(uml_VariableAction)


def test_uml_variableaction_constructor_exists():
    assert callable(uml_VariableAction.__init__)


def test_uml_variableaction_constructor_args():
    sig = inspect.signature(uml_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_timeevent_is_not_abstract():
    assert not inspect.isabstract(uml_TimeEvent)


def test_uml_timeevent_constructor_exists():
    assert callable(uml_TimeEvent.__init__)


def test_uml_timeevent_constructor_args():
    sig = inspect.signature(uml_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_uml_timeevent_has_isRelative():
    assert hasattr(uml_TimeEvent, "isRelative")
    descriptor = None
    for klass in uml_TimeEvent.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_uml_finalstate_is_not_abstract():
    assert not inspect.isabstract(uml_FinalState)


def test_uml_finalstate_constructor_exists():
    assert callable(uml_FinalState.__init__)


def test_uml_finalstate_constructor_args():
    sig = inspect.signature(uml_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_uml_durationobservation_is_not_abstract():
    assert not inspect.isabstract(uml_DurationObservation)


def test_uml_durationobservation_constructor_exists():
    assert callable(uml_DurationObservation.__init__)


def test_uml_durationobservation_constructor_args():
    sig = inspect.signature(uml_DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml_durationobservation_has_firstEvent():
    assert hasattr(uml_DurationObservation, "firstEvent")
    descriptor = None
    for klass in uml_DurationObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml_timeobservation_is_not_abstract():
    assert not inspect.isabstract(uml_TimeObservation)


def test_uml_timeobservation_constructor_exists():
    assert callable(uml_TimeObservation.__init__)


def test_uml_timeobservation_constructor_args():
    sig = inspect.signature(uml_TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml_timeobservation_has_firstEvent():
    assert hasattr(uml_TimeObservation, "firstEvent")
    descriptor = None
    for klass in uml_TimeObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_IntervalConstraint)


def test_uml_intervalconstraint_constructor_exists():
    assert callable(uml_IntervalConstraint.__init__)


def test_uml_intervalconstraint_constructor_args():
    sig = inspect.signature(uml_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_DurationConstraint)


def test_uml_durationconstraint_constructor_exists():
    assert callable(uml_DurationConstraint.__init__)


def test_uml_durationconstraint_constructor_args():
    sig = inspect.signature(uml_DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml_durationconstraint_has_firstEvent():
    assert hasattr(uml_DurationConstraint, "firstEvent")
    descriptor = None
    for klass in uml_DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TimeConstraint)


def test_uml_timeconstraint_constructor_exists():
    assert callable(uml_TimeConstraint.__init__)


def test_uml_timeconstraint_constructor_args():
    sig = inspect.signature(uml_TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml_timeconstraint_has_firstEvent():
    assert hasattr(uml_TimeConstraint, "firstEvent")
    descriptor = None
    for klass in uml_TimeConstraint.__mro__:
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



def test_uml_timeinterval_is_not_abstract():
    assert not inspect.isabstract(uml_TimeInterval)


def test_uml_timeinterval_constructor_exists():
    assert callable(uml_TimeInterval.__init__)


def test_uml_timeinterval_constructor_args():
    sig = inspect.signature(uml_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_durationinterval_is_not_abstract():
    assert not inspect.isabstract(uml_DurationInterval)


def test_uml_durationinterval_constructor_exists():
    assert callable(uml_DurationInterval.__init__)


def test_uml_durationinterval_constructor_args():
    sig = inspect.signature(uml_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml_ValueSpecificationAction)


def test_uml_valuespecificationaction_constructor_exists():
    assert callable(uml_ValueSpecificationAction.__init__)


def test_uml_valuespecificationaction_constructor_args():
    sig = inspect.signature(uml_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_SendObjectAction)


def test_uml_sendobjectaction_constructor_exists():
    assert callable(uml_SendObjectAction.__init__)


def test_uml_sendobjectaction_constructor_args():
    sig = inspect.signature(uml_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_BroadcastSignalAction)


def test_uml_broadcastsignalaction_constructor_exists():
    assert callable(uml_BroadcastSignalAction.__init__)


def test_uml_broadcastsignalaction_constructor_args():
    sig = inspect.signature(uml_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml_ClearAssociationAction)


def test_uml_clearassociationaction_constructor_exists():
    assert callable(uml_ClearAssociationAction.__init__)


def test_uml_clearassociationaction_constructor_args():
    sig = inspect.signature(uml_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_DestroyLinkAction)


def test_uml_destroylinkaction_constructor_exists():
    assert callable(uml_DestroyLinkAction.__init__)


def test_uml_destroylinkaction_constructor_args():
    sig = inspect.signature(uml_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_CreateLinkAction)


def test_uml_createlinkaction_constructor_exists():
    assert callable(uml_CreateLinkAction.__init__)


def test_uml_createlinkaction_constructor_args():
    sig = inspect.signature(uml_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(uml_LinkEndDestructionData)


def test_uml_linkenddestructiondata_constructor_exists():
    assert callable(uml_LinkEndDestructionData.__init__)


def test_uml_linkenddestructiondata_constructor_args():
    sig = inspect.signature(uml_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_uml_linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(uml_LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in uml_LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_uml_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(uml_LinkEndCreationData)


def test_uml_linkendcreationdata_constructor_exists():
    assert callable(uml_LinkEndCreationData.__init__)


def test_uml_linkendcreationdata_constructor_args():
    sig = inspect.signature(uml_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml_linkendcreationdata_has_isReplaceAll():
    assert hasattr(uml_LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in uml_LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_WriteLinkAction)


def test_uml_writelinkaction_constructor_exists():
    assert callable(uml_WriteLinkAction.__init__)


def test_uml_writelinkaction_constructor_args():
    sig = inspect.signature(uml_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_ReadLinkAction)


def test_uml_readlinkaction_constructor_exists():
    assert callable(uml_ReadLinkAction.__init__)


def test_uml_readlinkaction_constructor_args():
    sig = inspect.signature(uml_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_linkaction_is_not_abstract():
    assert not inspect.isabstract(uml_LinkAction)


def test_uml_linkaction_constructor_exists():
    assert callable(uml_LinkAction.__init__)


def test_uml_linkaction_constructor_args():
    sig = inspect.signature(uml_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_AddStructuralFeatureValueAction)


def test_uml_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_AddStructuralFeatureValueAction.__init__)


def test_uml_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml_addstructuralfeaturevalueaction_has_isReplaceAll():
    assert hasattr(uml_AddStructuralFeatureValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml_AddStructuralFeatureValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_templatesignature_is_not_abstract():
    assert not inspect.isabstract(TemplateSignature)


def test_templatesignature_constructor_exists():
    assert callable(TemplateSignature.__init__)


def test_templatesignature_constructor_args():
    sig = inspect.signature(TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_ConnectableElementTemplateParameter)


def test_uml_connectableelementtemplateparameter_constructor_exists():
    assert callable(uml_ConnectableElementTemplateParameter.__init__)


def test_uml_connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(uml_ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_ClassifierTemplateParameter)


def test_uml_classifiertemplateparameter_constructor_exists():
    assert callable(uml_ClassifierTemplateParameter.__init__)


def test_uml_classifiertemplateparameter_constructor_args():
    sig = inspect.signature(uml_ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"

def test_uml_classifiertemplateparameter_has_allowSubstitutable():
    assert hasattr(uml_ClassifierTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in uml_ClassifierTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml_operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_OperationTemplateParameter)


def test_uml_operationtemplateparameter_constructor_exists():
    assert callable(uml_OperationTemplateParameter.__init__)


def test_uml_operationtemplateparameter_constructor_args():
    sig = inspect.signature(uml_OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml_communicationpath_is_not_abstract():
    assert not inspect.isabstract(uml_CommunicationPath)


def test_uml_communicationpath_constructor_exists():
    assert callable(uml_CommunicationPath.__init__)


def test_uml_communicationpath_constructor_args():
    sig = inspect.signature(uml_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml_model_is_not_abstract():
    assert not inspect.isabstract(uml_Model)


def test_uml_model_constructor_exists():
    assert callable(uml_Model.__init__)


def test_uml_model_constructor_args():
    sig = inspect.signature(uml_Model.__init__)
    params = list(sig.parameters.keys())
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"

def test_uml_model_has_viewpoint():
    assert hasattr(uml_Model, "viewpoint")
    descriptor = None
    for klass in uml_Model.__mro__:
        if "viewpoint" in klass.__dict__:
            descriptor = klass.__dict__["viewpoint"]
            break
    assert isinstance(descriptor, property)



def test_uml_profile_is_not_abstract():
    assert not inspect.isabstract(uml_Profile)


def test_uml_profile_constructor_exists():
    assert callable(uml_Profile.__init__)


def test_uml_profile_constructor_args():
    sig = inspect.signature(uml_Profile.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_EncapsulatedClassifier)


def test_uml_encapsulatedclassifier_constructor_exists():
    assert callable(uml_EncapsulatedClassifier.__init__)


def test_uml_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml_extensionend_is_not_abstract():
    assert not inspect.isabstract(uml_ExtensionEnd)


def test_uml_extensionend_constructor_exists():
    assert callable(uml_ExtensionEnd.__init__)


def test_uml_extensionend_constructor_args():
    sig = inspect.signature(uml_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_port_is_not_abstract():
    assert not inspect.isabstract(uml_Port)


def test_uml_port_constructor_exists():
    assert callable(uml_Port.__init__)


def test_uml_port_constructor_args():
    sig = inspect.signature(uml_Port.__init__)
    params = list(sig.parameters.keys())
    assert "isService" in params, "Missing parameter 'isService'"
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"

def test_uml_port_has_isService():
    assert hasattr(uml_Port, "isService")
    descriptor = None
    for klass in uml_Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)

def test_uml_port_has_isBehavior():
    assert hasattr(uml_Port, "isBehavior")
    descriptor = None
    for klass in uml_Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)



def test_uml_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml_ConnectionPointReference)


def test_uml_connectionpointreference_constructor_exists():
    assert callable(uml_ConnectionPointReference.__init__)


def test_uml_connectionpointreference_constructor_args():
    sig = inspect.signature(uml_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml_pseudostate_is_not_abstract():
    assert not inspect.isabstract(uml_Pseudostate)


def test_uml_pseudostate_constructor_exists():
    assert callable(uml_Pseudostate.__init__)


def test_uml_pseudostate_constructor_args():
    sig = inspect.signature(uml_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml_pseudostate_has_kind():
    assert hasattr(uml_Pseudostate, "kind")
    descriptor = None
    for klass in uml_Pseudostate.__mro__:
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



def test_uml_activity_is_not_abstract():
    assert not inspect.isabstract(uml_Activity)


def test_uml_activity_constructor_exists():
    assert callable(uml_Activity.__init__)


def test_uml_activity_constructor_args():
    sig = inspect.signature(uml_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_uml_activity_has_isReadOnly():
    assert hasattr(uml_Activity, "isReadOnly")
    descriptor = None
    for klass in uml_Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_uml_activity_has_isSingleExecution():
    assert hasattr(uml_Activity, "isSingleExecution")
    descriptor = None
    for klass in uml_Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)



def test_uml_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(uml_OpaqueBehavior)


def test_uml_opaquebehavior_constructor_exists():
    assert callable(uml_OpaqueBehavior.__init__)


def test_uml_opaquebehavior_constructor_args():
    sig = inspect.signature(uml_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_uml_opaquebehavior_has_language():
    assert hasattr(uml_OpaqueBehavior, "language")
    descriptor = None
    for klass in uml_OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml_opaquebehavior_has_body():
    assert hasattr(uml_OpaqueBehavior, "body")
    descriptor = None
    for klass in uml_OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uml_interaction_is_not_abstract():
    assert not inspect.isabstract(uml_Interaction)


def test_uml_interaction_constructor_exists():
    assert callable(uml_Interaction.__init__)


def test_uml_interaction_constructor_args():
    sig = inspect.signature(uml_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml_statemachine_is_not_abstract():
    assert not inspect.isabstract(uml_StateMachine)


def test_uml_statemachine_constructor_exists():
    assert callable(uml_StateMachine.__init__)


def test_uml_statemachine_constructor_args():
    sig = inspect.signature(uml_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml_ProtocolStateMachine)


def test_uml_protocolstatemachine_constructor_exists():
    assert callable(uml_ProtocolStateMachine.__init__)


def test_uml_protocolstatemachine_constructor_args():
    sig = inspect.signature(uml_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml_component_is_not_abstract():
    assert not inspect.isabstract(uml_Component)


def test_uml_component_constructor_exists():
    assert callable(uml_Component.__init__)


def test_uml_component_constructor_args():
    sig = inspect.signature(uml_Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"

def test_uml_component_has_isIndirectlyInstantiated():
    assert hasattr(uml_Component, "isIndirectlyInstantiated")
    descriptor = None
    for klass in uml_Component.__mro__:
        if "isIndirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["isIndirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)



def test_uml_associationclass_is_not_abstract():
    assert not inspect.isabstract(uml_AssociationClass)


def test_uml_associationclass_constructor_exists():
    assert callable(uml_AssociationClass.__init__)


def test_uml_associationclass_constructor_args():
    sig = inspect.signature(uml_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml_stereotype_is_not_abstract():
    assert not inspect.isabstract(uml_Stereotype)


def test_uml_stereotype_constructor_exists():
    assert callable(uml_Stereotype.__init__)


def test_uml_stereotype_constructor_args():
    sig = inspect.signature(uml_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml_extension_is_not_abstract():
    assert not inspect.isabstract(uml_Extension)


def test_uml_extension_constructor_exists():
    assert callable(uml_Extension.__init__)


def test_uml_extension_constructor_args():
    sig = inspect.signature(uml_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_uml_extension_has_isRequired():
    assert hasattr(uml_Extension, "isRequired")
    descriptor = None
    for klass in uml_Extension.__mro__:
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



def test_uml_collaboration_is_not_abstract():
    assert not inspect.isabstract(uml_Collaboration)


def test_uml_collaboration_constructor_exists():
    assert callable(uml_Collaboration.__init__)


def test_uml_collaboration_constructor_args():
    sig = inspect.signature(uml_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml_actor_is_not_abstract():
    assert not inspect.isabstract(uml_Actor)


def test_uml_actor_constructor_exists():
    assert callable(uml_Actor.__init__)


def test_uml_actor_constructor_args():
    sig = inspect.signature(uml_Actor.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml_reception_is_not_abstract():
    assert not inspect.isabstract(uml_Reception)


def test_uml_reception_constructor_exists():
    assert callable(uml_Reception.__init__)


def test_uml_reception_constructor_args():
    sig = inspect.signature(uml_Reception.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml_connector_is_not_abstract():
    assert not inspect.isabstract(uml_Connector)


def test_uml_connector_constructor_exists():
    assert callable(uml_Connector.__init__)


def test_uml_connector_constructor_args():
    sig = inspect.signature(uml_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml_connector_has_kind():
    assert hasattr(uml_Connector, "kind")
    descriptor = None
    for klass in uml_Connector.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



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



def test_uml_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(uml_DeploymentSpecification)


def test_uml_deploymentspecification_constructor_exists():
    assert callable(uml_DeploymentSpecification.__init__)


def test_uml_deploymentspecification_constructor_args():
    sig = inspect.signature(uml_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"

def test_uml_deploymentspecification_has_deploymentLocation():
    assert hasattr(uml_DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in uml_DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)

def test_uml_deploymentspecification_has_executionLocation():
    assert hasattr(uml_DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in uml_DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)



def test_uml_class_is_not_abstract():
    assert not inspect.isabstract(uml_Class)


def test_uml_class_constructor_exists():
    assert callable(uml_Class.__init__)


def test_uml_class_constructor_args():
    sig = inspect.signature(uml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml_class_has_isActive():
    assert hasattr(uml_Class, "isActive")
    descriptor = None
    for klass in uml_Class.__mro__:
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



def test_uml_node_is_not_abstract():
    assert not inspect.isabstract(uml_Node)


def test_uml_node_constructor_exists():
    assert callable(uml_Node.__init__)


def test_uml_node_constructor_args():
    sig = inspect.signature(uml_Node.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml_interfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml_InterfaceRealization)


def test_uml_interfacerealization_constructor_exists():
    assert callable(uml_InterfaceRealization.__init__)


def test_uml_interfacerealization_constructor_args():
    sig = inspect.signature(uml_InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml_componentrealization_is_not_abstract():
    assert not inspect.isabstract(uml_ComponentRealization)


def test_uml_componentrealization_constructor_exists():
    assert callable(uml_ComponentRealization.__init__)


def test_uml_componentrealization_constructor_args():
    sig = inspect.signature(uml_ComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_pin_is_not_abstract():
    assert not inspect.isabstract(uml_Pin)


def test_uml_pin_constructor_exists():
    assert callable(uml_Pin.__init__)


def test_uml_pin_constructor_args():
    sig = inspect.signature(uml_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_uml_pin_has_isControl():
    assert hasattr(uml_Pin, "isControl")
    descriptor = None
    for klass in uml_Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_uml_connectorend_is_not_abstract():
    assert not inspect.isabstract(uml_ConnectorEnd)


def test_uml_connectorend_constructor_exists():
    assert callable(uml_ConnectorEnd.__init__)


def test_uml_connectorend_constructor_args():
    sig = inspect.signature(uml_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_variable_is_not_abstract():
    assert not inspect.isabstract(uml_Variable)


def test_uml_variable_constructor_exists():
    assert callable(uml_Variable.__init__)


def test_uml_variable_constructor_args():
    sig = inspect.signature(uml_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml_behavior_is_not_abstract():
    assert not inspect.isabstract(uml_Behavior)


def test_uml_behavior_constructor_exists():
    assert callable(uml_Behavior.__init__)


def test_uml_behavior_constructor_args():
    sig = inspect.signature(uml_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_uml_behavior_has_isReentrant():
    assert hasattr(uml_Behavior, "isReentrant")
    descriptor = None
    for klass in uml_Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_uml_parameter_is_not_abstract():
    assert not inspect.isabstract(uml_Parameter)


def test_uml_parameter_constructor_exists():
    assert callable(uml_Parameter.__init__)


def test_uml_parameter_constructor_args():
    sig = inspect.signature(uml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "isStream" in params, "Missing parameter 'isStream'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "default" in params, "Missing parameter 'default'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_uml_parameter_has_isStream():
    assert hasattr(uml_Parameter, "isStream")
    descriptor = None
    for klass in uml_Parameter.__mro__:
        if "isStream" in klass.__dict__:
            descriptor = klass.__dict__["isStream"]
            break
    assert isinstance(descriptor, property)

def test_uml_parameter_has_isException():
    assert hasattr(uml_Parameter, "isException")
    descriptor = None
    for klass in uml_Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_uml_parameter_has_default():
    assert hasattr(uml_Parameter, "default")
    descriptor = None
    for klass in uml_Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml_parameter_has_effect():
    assert hasattr(uml_Parameter, "effect")
    descriptor = None
    for klass in uml_Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_uml_parameter_has_direction():
    assert hasattr(uml_Parameter, "direction")
    descriptor = None
    for klass in uml_Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_literalspecification_is_not_abstract():
    assert not inspect.isabstract(uml_LiteralSpecification)


def test_uml_literalspecification_constructor_exists():
    assert callable(uml_LiteralSpecification.__init__)


def test_uml_literalspecification_constructor_args():
    sig = inspect.signature(uml_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_interval_is_not_abstract():
    assert not inspect.isabstract(uml_Interval)


def test_uml_interval_constructor_exists():
    assert callable(uml_Interval.__init__)


def test_uml_interval_constructor_args():
    sig = inspect.signature(uml_Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml_timeexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TimeExpression)


def test_uml_timeexpression_constructor_exists():
    assert callable(uml_TimeExpression.__init__)


def test_uml_timeexpression_constructor_args():
    sig = inspect.signature(uml_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_instancevalue_is_not_abstract():
    assert not inspect.isabstract(uml_InstanceValue)


def test_uml_instancevalue_constructor_exists():
    assert callable(uml_InstanceValue.__init__)


def test_uml_instancevalue_constructor_args():
    sig = inspect.signature(uml_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_expression_is_not_abstract():
    assert not inspect.isabstract(uml_Expression)


def test_uml_expression_constructor_exists():
    assert callable(uml_Expression.__init__)


def test_uml_expression_constructor_args():
    sig = inspect.signature(uml_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_uml_expression_has_symbol():
    assert hasattr(uml_Expression, "symbol")
    descriptor = None
    for klass in uml_Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_uml_duration_is_not_abstract():
    assert not inspect.isabstract(uml_Duration)


def test_uml_duration_constructor_exists():
    assert callable(uml_Duration.__init__)


def test_uml_duration_constructor_args():
    sig = inspect.signature(uml_Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml_OpaqueExpression)


def test_uml_opaqueexpression_constructor_exists():
    assert callable(uml_OpaqueExpression.__init__)


def test_uml_opaqueexpression_constructor_args():
    sig = inspect.signature(uml_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml_opaqueexpression_has_body():
    assert hasattr(uml_OpaqueExpression, "body")
    descriptor = None
    for klass in uml_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml_opaqueexpression_has_language():
    assert hasattr(uml_OpaqueExpression, "language")
    descriptor = None
    for klass in uml_OpaqueExpression.__mro__:
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



def test_uml_usage_is_not_abstract():
    assert not inspect.isabstract(uml_Usage)


def test_uml_usage_constructor_exists():
    assert callable(uml_Usage.__init__)


def test_uml_usage_constructor_args():
    sig = inspect.signature(uml_Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml_deployment_is_not_abstract():
    assert not inspect.isabstract(uml_Deployment)


def test_uml_deployment_constructor_exists():
    assert callable(uml_Deployment.__init__)


def test_uml_deployment_constructor_args():
    sig = inspect.signature(uml_Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml_abstraction_is_not_abstract():
    assert not inspect.isabstract(uml_Abstraction)


def test_uml_abstraction_constructor_exists():
    assert callable(uml_Abstraction.__init__)


def test_uml_abstraction_constructor_args():
    sig = inspect.signature(uml_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml_manifestation_is_not_abstract():
    assert not inspect.isabstract(uml_Manifestation)


def test_uml_manifestation_constructor_exists():
    assert callable(uml_Manifestation.__init__)


def test_uml_manifestation_constructor_args():
    sig = inspect.signature(uml_Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml_realization_is_not_abstract():
    assert not inspect.isabstract(uml_Realization)


def test_uml_realization_constructor_exists():
    assert callable(uml_Realization.__init__)


def test_uml_realization_constructor_args():
    sig = inspect.signature(uml_Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml_usecase_is_not_abstract():
    assert not inspect.isabstract(uml_UseCase)


def test_uml_usecase_constructor_exists():
    assert callable(uml_UseCase.__init__)


def test_uml_usecase_constructor_args():
    sig = inspect.signature(uml_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml_substitution_is_not_abstract():
    assert not inspect.isabstract(uml_Substitution)


def test_uml_substitution_constructor_exists():
    assert callable(uml_Substitution.__init__)


def test_uml_substitution_constructor_args():
    sig = inspect.signature(uml_Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml_property_is_not_abstract():
    assert not inspect.isabstract(uml_Property)


def test_uml_property_constructor_exists():
    assert callable(uml_Property.__init__)


def test_uml_property_constructor_args():
    sig = inspect.signature(uml_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"

def test_uml_property_has_isComposite():
    assert hasattr(uml_Property, "isComposite")
    descriptor = None
    for klass in uml_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml_property_has_isDerivedUnion():
    assert hasattr(uml_Property, "isDerivedUnion")
    descriptor = None
    for klass in uml_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_uml_property_has_aggregation():
    assert hasattr(uml_Property, "aggregation")
    descriptor = None
    for klass in uml_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_uml_property_has_isDerived():
    assert hasattr(uml_Property, "isDerived")
    descriptor = None
    for klass in uml_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_uml_property_has_default():
    assert hasattr(uml_Property, "default")
    descriptor = None
    for klass in uml_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_informationitem_is_not_abstract():
    assert not inspect.isabstract(uml_InformationItem)


def test_uml_informationitem_constructor_exists():
    assert callable(uml_InformationItem.__init__)


def test_uml_informationitem_constructor_args():
    sig = inspect.signature(uml_InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml_signal_is_not_abstract():
    assert not inspect.isabstract(uml_Signal)


def test_uml_signal_constructor_exists():
    assert callable(uml_Signal.__init__)


def test_uml_signal_constructor_args():
    sig = inspect.signature(uml_Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml_interface_is_not_abstract():
    assert not inspect.isabstract(uml_Interface)


def test_uml_interface_constructor_exists():
    assert callable(uml_Interface.__init__)


def test_uml_interface_constructor_args():
    sig = inspect.signature(uml_Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml_artifact_is_not_abstract():
    assert not inspect.isabstract(uml_Artifact)


def test_uml_artifact_constructor_exists():
    assert callable(uml_Artifact.__init__)


def test_uml_artifact_constructor_args():
    sig = inspect.signature(uml_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_uml_artifact_has_fileName():
    assert hasattr(uml_Artifact, "fileName")
    descriptor = None
    for klass in uml_Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_uml_datatype_is_not_abstract():
    assert not inspect.isabstract(uml_DataType)


def test_uml_datatype_constructor_exists():
    assert callable(uml_DataType.__init__)


def test_uml_datatype_constructor_args():
    sig = inspect.signature(uml_DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_StructuredClassifier)


def test_uml_structuredclassifier_constructor_exists():
    assert callable(uml_StructuredClassifier.__init__)


def test_uml_structuredclassifier_constructor_args():
    sig = inspect.signature(uml_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_BehavioredClassifier)


def test_uml_behavioredclassifier_constructor_exists():
    assert callable(uml_BehavioredClassifier.__init__)


def test_uml_behavioredclassifier_constructor_args():
    sig = inspect.signature(uml_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_objectnode_is_not_abstract():
    assert not inspect.isabstract(uml_ObjectNode)


def test_uml_objectnode_constructor_exists():
    assert callable(uml_ObjectNode.__init__)


def test_uml_objectnode_constructor_args():
    sig = inspect.signature(uml_ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"

def test_uml_objectnode_has_ordering():
    assert hasattr(uml_ObjectNode, "ordering")
    descriptor = None
    for klass in uml_ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_uml_objectnode_has_isControlType():
    assert hasattr(uml_ObjectNode, "isControlType")
    descriptor = None
    for klass in uml_ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)



def test_uml_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml_StructuralFeature)


def test_uml_structuralfeature_constructor_exists():
    assert callable(uml_StructuralFeature.__init__)


def test_uml_structuralfeature_constructor_args():
    sig = inspect.signature(uml_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml_structuralfeature_has_isReadOnly():
    assert hasattr(uml_StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in uml_StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
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



def test_uml_feature_is_not_abstract():
    assert not inspect.isabstract(uml_Feature)


def test_uml_feature_constructor_exists():
    assert callable(uml_Feature.__init__)


def test_uml_feature_constructor_args():
    sig = inspect.signature(uml_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml_feature_has_isStatic():
    assert hasattr(uml_Feature, "isStatic")
    descriptor = None
    for klass in uml_Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_uml_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml_ExtensionPoint)


def test_uml_extensionpoint_constructor_exists():
    assert callable(uml_ExtensionPoint.__init__)


def test_uml_extensionpoint_constructor_args():
    sig = inspect.signature(uml_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml_activitynode_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityNode)


def test_uml_activitynode_constructor_exists():
    assert callable(uml_ActivityNode.__init__)


def test_uml_activitynode_constructor_args():
    sig = inspect.signature(uml_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml_RedefinableTemplateSignature)


def test_uml_redefinabletemplatesignature_constructor_exists():
    assert callable(uml_RedefinableTemplateSignature.__init__)


def test_uml_redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(uml_RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml_activityedge_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityEdge)


def test_uml_activityedge_constructor_exists():
    assert callable(uml_ActivityEdge.__init__)


def test_uml_activityedge_constructor_args():
    sig = inspect.signature(uml_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_connectableelement_is_not_abstract():
    assert not inspect.isabstract(uml_ConnectableElement)


def test_uml_connectableelement_constructor_exists():
    assert callable(uml_ConnectableElement.__init__)


def test_uml_connectableelement_constructor_args():
    sig = inspect.signature(uml_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_generalordering_is_not_abstract():
    assert not inspect.isabstract(uml_GeneralOrdering)


def test_uml_generalordering_constructor_exists():
    assert callable(uml_GeneralOrdering.__init__)


def test_uml_generalordering_constructor_args():
    sig = inspect.signature(uml_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml_collaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml_CollaborationUse)


def test_uml_collaborationuse_constructor_exists():
    assert callable(uml_CollaborationUse.__init__)


def test_uml_collaborationuse_constructor_args():
    sig = inspect.signature(uml_CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_uml_messageend_is_not_abstract():
    assert not inspect.isabstract(uml_MessageEnd)


def test_uml_messageend_constructor_exists():
    assert callable(uml_MessageEnd.__init__)


def test_uml_messageend_constructor_args():
    sig = inspect.signature(uml_MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_message_is_not_abstract():
    assert not inspect.isabstract(uml_Message)


def test_uml_message_constructor_exists():
    assert callable(uml_Message.__init__)


def test_uml_message_constructor_args():
    sig = inspect.signature(uml_Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageSort" in params, "Missing parameter 'messageSort'"
    assert "messageKind" in params, "Missing parameter 'messageKind'"

def test_uml_message_has_messageSort():
    assert hasattr(uml_Message, "messageSort")
    descriptor = None
    for klass in uml_Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)

def test_uml_message_has_messageKind():
    assert hasattr(uml_Message, "messageKind")
    descriptor = None
    for klass in uml_Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)



def test_uml_activitypartition_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityPartition)


def test_uml_activitypartition_constructor_exists():
    assert callable(uml_ActivityPartition.__init__)


def test_uml_activitypartition_constructor_args():
    sig = inspect.signature(uml_ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isDimension" in params, "Missing parameter 'isDimension'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_uml_activitypartition_has_isDimension():
    assert hasattr(uml_ActivityPartition, "isDimension")
    descriptor = None
    for klass in uml_ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)

def test_uml_activitypartition_has_isExternal():
    assert hasattr(uml_ActivityPartition, "isExternal")
    descriptor = None
    for klass in uml_ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)



def test_uml_lifeline_is_not_abstract():
    assert not inspect.isabstract(uml_Lifeline)


def test_uml_lifeline_constructor_exists():
    assert callable(uml_Lifeline.__init__)


def test_uml_lifeline_constructor_args():
    sig = inspect.signature(uml_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml_trigger_is_not_abstract():
    assert not inspect.isabstract(uml_Trigger)


def test_uml_trigger_constructor_exists():
    assert callable(uml_Trigger.__init__)


def test_uml_trigger_constructor_args():
    sig = inspect.signature(uml_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml_typedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TypedElement)


def test_uml_typedelement_constructor_exists():
    assert callable(uml_TypedElement.__init__)


def test_uml_typedelement_constructor_args():
    sig = inspect.signature(uml_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_vertex_is_not_abstract():
    assert not inspect.isabstract(uml_Vertex)


def test_uml_vertex_constructor_exists():
    assert callable(uml_Vertex.__init__)


def test_uml_vertex_constructor_args():
    sig = inspect.signature(uml_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml_parameterset_is_not_abstract():
    assert not inspect.isabstract(uml_ParameterSet)


def test_uml_parameterset_constructor_exists():
    assert callable(uml_ParameterSet.__init__)


def test_uml_parameterset_constructor_args():
    sig = inspect.signature(uml_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(uml_DeploymentTarget)


def test_uml_deploymenttarget_constructor_exists():
    assert callable(uml_DeploymentTarget.__init__)


def test_uml_deploymenttarget_constructor_args():
    sig = inspect.signature(uml_DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml_namespace_is_not_abstract():
    assert not inspect.isabstract(uml_Namespace)


def test_uml_namespace_constructor_exists():
    assert callable(uml_Namespace.__init__)


def test_uml_namespace_constructor_args():
    sig = inspect.signature(uml_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(uml_InteractionFragment)


def test_uml_interactionfragment_constructor_exists():
    assert callable(uml_InteractionFragment.__init__)


def test_uml_interactionfragment_constructor_args():
    sig = inspect.signature(uml_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(uml_DeployedArtifact)


def test_uml_deployedartifact_constructor_exists():
    assert callable(uml_DeployedArtifact.__init__)


def test_uml_deployedartifact_constructor_args():
    sig = inspect.signature(uml_DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml_RedefinableElement)


def test_uml_redefinableelement_constructor_exists():
    assert callable(uml_RedefinableElement.__init__)


def test_uml_redefinableelement_constructor_args():
    sig = inspect.signature(uml_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_uml_redefinableelement_has_isLeaf():
    assert hasattr(uml_RedefinableElement, "isLeaf")
    descriptor = None
    for klass in uml_RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_uml_packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml_PackageableElement)


def test_uml_packageableelement_constructor_exists():
    assert callable(uml_PackageableElement.__init__)


def test_uml_packageableelement_constructor_args():
    sig = inspect.signature(uml_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_operation_is_not_abstract():
    assert not inspect.isabstract(uml_Operation)


def test_uml_operation_constructor_exists():
    assert callable(uml_Operation.__init__)


def test_uml_operation_constructor_args():
    sig = inspect.signature(uml_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_uml_operation_has_isOrdered():
    assert hasattr(uml_Operation, "isOrdered")
    descriptor = None
    for klass in uml_Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml_operation_has_lower():
    assert hasattr(uml_Operation, "lower")
    descriptor = None
    for klass in uml_Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml_operation_has_isQuery():
    assert hasattr(uml_Operation, "isQuery")
    descriptor = None
    for klass in uml_Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_uml_operation_has_upper():
    assert hasattr(uml_Operation, "upper")
    descriptor = None
    for klass in uml_Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml_operation_has_isUnique():
    assert hasattr(uml_Operation, "isUnique")
    descriptor = None
    for klass in uml_Operation.__mro__:
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



def test_uml_generalizationset_is_not_abstract():
    assert not inspect.isabstract(uml_GeneralizationSet)


def test_uml_generalizationset_constructor_exists():
    assert callable(uml_GeneralizationSet.__init__)


def test_uml_generalizationset_constructor_args():
    sig = inspect.signature(uml_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"
    assert "isCovering" in params, "Missing parameter 'isCovering'"

def test_uml_generalizationset_has_isDisjoint():
    assert hasattr(uml_GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in uml_GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)

def test_uml_generalizationset_has_isCovering():
    assert hasattr(uml_GeneralizationSet, "isCovering")
    descriptor = None
    for klass in uml_GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)



def test_uml_constraint_is_not_abstract():
    assert not inspect.isabstract(uml_Constraint)


def test_uml_constraint_constructor_exists():
    assert callable(uml_Constraint.__init__)


def test_uml_constraint_constructor_args():
    sig = inspect.signature(uml_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_event_is_not_abstract():
    assert not inspect.isabstract(uml_Event)


def test_uml_event_constructor_exists():
    assert callable(uml_Event.__init__)


def test_uml_event_constructor_args():
    sig = inspect.signature(uml_Event.__init__)
    params = list(sig.parameters.keys())



def test_uml_valuespecification_is_not_abstract():
    assert not inspect.isabstract(uml_ValueSpecification)


def test_uml_valuespecification_constructor_exists():
    assert callable(uml_ValueSpecification.__init__)


def test_uml_valuespecification_constructor_args():
    sig = inspect.signature(uml_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_type_is_not_abstract():
    assert not inspect.isabstract(uml_Type)


def test_uml_type_constructor_exists():
    assert callable(uml_Type.__init__)


def test_uml_type_constructor_args():
    sig = inspect.signature(uml_Type.__init__)
    params = list(sig.parameters.keys())



def test_uml_instancespecification_is_not_abstract():
    assert not inspect.isabstract(uml_InstanceSpecification)


def test_uml_instancespecification_constructor_exists():
    assert callable(uml_InstanceSpecification.__init__)


def test_uml_instancespecification_constructor_args():
    sig = inspect.signature(uml_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_observation_is_not_abstract():
    assert not inspect.isabstract(uml_Observation)


def test_uml_observation_constructor_exists():
    assert callable(uml_Observation.__init__)


def test_uml_observation_constructor_args():
    sig = inspect.signature(uml_Observation.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(uml_InteractionOperand)


def test_uml_interactionoperand_constructor_exists():
    assert callable(uml_InteractionOperand.__init__)


def test_uml_interactionoperand_constructor_args():
    sig = inspect.signature(uml_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml_transition_is_not_abstract():
    assert not inspect.isabstract(uml_Transition)


def test_uml_transition_constructor_exists():
    assert callable(uml_Transition.__init__)


def test_uml_transition_constructor_args():
    sig = inspect.signature(uml_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml_transition_has_kind():
    assert hasattr(uml_Transition, "kind")
    descriptor = None
    for klass in uml_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml_region_is_not_abstract():
    assert not inspect.isabstract(uml_Region)


def test_uml_region_constructor_exists():
    assert callable(uml_Region.__init__)


def test_uml_region_constructor_args():
    sig = inspect.signature(uml_Region.__init__)
    params = list(sig.parameters.keys())



def test_uml_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml_StructuredActivityNode)


def test_uml_structuredactivitynode_constructor_exists():
    assert callable(uml_StructuredActivityNode.__init__)


def test_uml_structuredactivitynode_constructor_args():
    sig = inspect.signature(uml_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_uml_structuredactivitynode_has_mustIsolate():
    assert hasattr(uml_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in uml_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_uml_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml_BehavioralFeature)


def test_uml_behavioralfeature_constructor_exists():
    assert callable(uml_BehavioralFeature.__init__)


def test_uml_behavioralfeature_constructor_args():
    sig = inspect.signature(uml_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "concurrency" in params, "Missing parameter 'concurrency'"

def test_uml_behavioralfeature_has_isAbstract():
    assert hasattr(uml_BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in uml_BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_uml_behavioralfeature_has_concurrency():
    assert hasattr(uml_BehavioralFeature, "concurrency")
    descriptor = None
    for klass in uml_BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)



def test_uml_state_is_not_abstract():
    assert not inspect.isabstract(uml_State)


def test_uml_state_constructor_exists():
    assert callable(uml_State.__init__)


def test_uml_state_constructor_args():
    sig = inspect.signature(uml_State.__init__)
    params = list(sig.parameters.keys())
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"

def test_uml_state_has_isSimple():
    assert hasattr(uml_State, "isSimple")
    descriptor = None
    for klass in uml_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_uml_state_has_isComposite():
    assert hasattr(uml_State, "isComposite")
    descriptor = None
    for klass in uml_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml_state_has_isOrthogonal():
    assert hasattr(uml_State, "isOrthogonal")
    descriptor = None
    for klass in uml_State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_uml_state_has_isSubmachineState():
    assert hasattr(uml_State, "isSubmachineState")
    descriptor = None
    for klass in uml_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)



def test_uml_classifier_is_not_abstract():
    assert not inspect.isabstract(uml_Classifier)


def test_uml_classifier_constructor_exists():
    assert callable(uml_Classifier.__init__)


def test_uml_classifier_constructor_args():
    sig = inspect.signature(uml_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml_classifier_has_isAbstract():
    assert hasattr(uml_Classifier, "isAbstract")
    descriptor = None
    for klass in uml_Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml_package_is_not_abstract():
    assert not inspect.isabstract(uml_Package)


def test_uml_package_constructor_exists():
    assert callable(uml_Package.__init__)


def test_uml_package_constructor_args():
    sig = inspect.signature(uml_Package.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml_association_is_not_abstract():
    assert not inspect.isabstract(uml_Association)


def test_uml_association_constructor_exists():
    assert callable(uml_Association.__init__)


def test_uml_association_constructor_args():
    sig = inspect.signature(uml_Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml_association_has_isDerived():
    assert hasattr(uml_Association, "isDerived")
    descriptor = None
    for klass in uml_Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_uml_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml_DirectedRelationship)


def test_uml_directedrelationship_constructor_exists():
    assert callable(uml_DirectedRelationship.__init__)


def test_uml_directedrelationship_constructor_args():
    sig = inspect.signature(uml_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_uml_generalization_is_not_abstract():
    assert not inspect.isabstract(uml_Generalization)


def test_uml_generalization_constructor_exists():
    assert callable(uml_Generalization.__init__)


def test_uml_generalization_constructor_args():
    sig = inspect.signature(uml_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_uml_generalization_has_isSubstitutable():
    assert hasattr(uml_Generalization, "isSubstitutable")
    descriptor = None
    for klass in uml_Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml_ProtocolConformance)


def test_uml_protocolconformance_constructor_exists():
    assert callable(uml_ProtocolConformance.__init__)


def test_uml_protocolconformance_constructor_args():
    sig = inspect.signature(uml_ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml_packageimport_is_not_abstract():
    assert not inspect.isabstract(uml_PackageImport)


def test_uml_packageimport_constructor_exists():
    assert callable(uml_PackageImport.__init__)


def test_uml_packageimport_constructor_args():
    sig = inspect.signature(uml_PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml_packageimport_has_visibility():
    assert hasattr(uml_PackageImport, "visibility")
    descriptor = None
    for klass in uml_PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml_informationflow_is_not_abstract():
    assert not inspect.isabstract(uml_InformationFlow)


def test_uml_informationflow_constructor_exists():
    assert callable(uml_InformationFlow.__init__)


def test_uml_informationflow_constructor_args():
    sig = inspect.signature(uml_InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_templatebinding_is_not_abstract():
    assert not inspect.isabstract(uml_TemplateBinding)


def test_uml_templatebinding_constructor_exists():
    assert callable(uml_TemplateBinding.__init__)


def test_uml_templatebinding_constructor_args():
    sig = inspect.signature(uml_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_uml_elementimport_is_not_abstract():
    assert not inspect.isabstract(uml_ElementImport)


def test_uml_elementimport_constructor_exists():
    assert callable(uml_ElementImport.__init__)


def test_uml_elementimport_constructor_args():
    sig = inspect.signature(uml_ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml_elementimport_has_alias():
    assert hasattr(uml_ElementImport, "alias")
    descriptor = None
    for klass in uml_ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_uml_elementimport_has_visibility():
    assert hasattr(uml_ElementImport, "visibility")
    descriptor = None
    for klass in uml_ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml_extend_is_not_abstract():
    assert not inspect.isabstract(uml_Extend)


def test_uml_extend_constructor_exists():
    assert callable(uml_Extend.__init__)


def test_uml_extend_constructor_args():
    sig = inspect.signature(uml_Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml_packagemerge_is_not_abstract():
    assert not inspect.isabstract(uml_PackageMerge)


def test_uml_packagemerge_constructor_exists():
    assert callable(uml_PackageMerge.__init__)


def test_uml_packagemerge_constructor_args():
    sig = inspect.signature(uml_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml_profileapplication_is_not_abstract():
    assert not inspect.isabstract(uml_ProfileApplication)


def test_uml_profileapplication_constructor_exists():
    assert callable(uml_ProfileApplication.__init__)


def test_uml_profileapplication_constructor_args():
    sig = inspect.signature(uml_ProfileApplication.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_uml_profileapplication_has_isStrict():
    assert hasattr(uml_ProfileApplication, "isStrict")
    descriptor = None
    for klass in uml_ProfileApplication.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_uml_include_is_not_abstract():
    assert not inspect.isabstract(uml_Include)


def test_uml_include_constructor_exists():
    assert callable(uml_Include.__init__)


def test_uml_include_constructor_args():
    sig = inspect.signature(uml_Include.__init__)
    params = list(sig.parameters.keys())



def test_uml_dependency_is_not_abstract():
    assert not inspect.isabstract(uml_Dependency)


def test_uml_dependency_constructor_exists():
    assert callable(uml_Dependency.__init__)


def test_uml_dependency_constructor_args():
    sig = inspect.signature(uml_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml_stringexpression_is_not_abstract():
    assert not inspect.isabstract(uml_StringExpression)


def test_uml_stringexpression_constructor_exists():
    assert callable(uml_StringExpression.__init__)


def test_uml_stringexpression_constructor_args():
    sig = inspect.signature(uml_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml_templatesignature_is_not_abstract():
    assert not inspect.isabstract(uml_TemplateSignature)


def test_uml_templatesignature_constructor_exists():
    assert callable(uml_TemplateSignature.__init__)


def test_uml_templatesignature_constructor_args():
    sig = inspect.signature(uml_TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml_image_is_not_abstract():
    assert not inspect.isabstract(uml_Image)


def test_uml_image_constructor_exists():
    assert callable(uml_Image.__init__)


def test_uml_image_constructor_args():
    sig = inspect.signature(uml_Image.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "content" in params, "Missing parameter 'content'"
    assert "location" in params, "Missing parameter 'location'"

def test_uml_image_has_format():
    assert hasattr(uml_Image, "format")
    descriptor = None
    for klass in uml_Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_uml_image_has_content():
    assert hasattr(uml_Image, "content")
    descriptor = None
    for klass in uml_Image.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_uml_image_has_location():
    assert hasattr(uml_Image, "location")
    descriptor = None
    for klass in uml_Image.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_uml_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml_TemplateParameterSubstitution)


def test_uml_templateparametersubstitution_constructor_exists():
    assert callable(uml_TemplateParameterSubstitution.__init__)


def test_uml_templateparametersubstitution_constructor_args():
    sig = inspect.signature(uml_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml_ParameterableElement)


def test_uml_parameterableelement_constructor_exists():
    assert callable(uml_ParameterableElement.__init__)


def test_uml_parameterableelement_constructor_args():
    sig = inspect.signature(uml_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_templateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TemplateParameter)


def test_uml_templateparameter_constructor_exists():
    assert callable(uml_TemplateParameter.__init__)


def test_uml_templateparameter_constructor_args():
    sig = inspect.signature(uml_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(uml_MultiplicityElement)


def test_uml_multiplicityelement_constructor_exists():
    assert callable(uml_MultiplicityElement.__init__)


def test_uml_multiplicityelement_constructor_args():
    sig = inspect.signature(uml_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_uml_multiplicityelement_has_isUnique():
    assert hasattr(uml_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in uml_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_uml_multiplicityelement_has_lower():
    assert hasattr(uml_MultiplicityElement, "lower")
    descriptor = None
    for klass in uml_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml_multiplicityelement_has_upper():
    assert hasattr(uml_MultiplicityElement, "upper")
    descriptor = None
    for klass in uml_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml_multiplicityelement_has_isOrdered():
    assert hasattr(uml_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in uml_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_uml_templateableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TemplateableElement)


def test_uml_templateableelement_constructor_exists():
    assert callable(uml_TemplateableElement.__init__)


def test_uml_templateableelement_constructor_args():
    sig = inspect.signature(uml_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml_ExceptionHandler)


def test_uml_exceptionhandler_constructor_exists():
    assert callable(uml_ExceptionHandler.__init__)


def test_uml_exceptionhandler_constructor_args():
    sig = inspect.signature(uml_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml_clause_is_not_abstract():
    assert not inspect.isabstract(uml_Clause)


def test_uml_clause_constructor_exists():
    assert callable(uml_Clause.__init__)


def test_uml_clause_constructor_args():
    sig = inspect.signature(uml_Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml_relationship_is_not_abstract():
    assert not inspect.isabstract(uml_Relationship)


def test_uml_relationship_constructor_exists():
    assert callable(uml_Relationship.__init__)


def test_uml_relationship_constructor_args():
    sig = inspect.signature(uml_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml_namedelement_is_not_abstract():
    assert not inspect.isabstract(uml_NamedElement)


def test_uml_namedelement_constructor_exists():
    assert callable(uml_NamedElement.__init__)


def test_uml_namedelement_constructor_args():
    sig = inspect.signature(uml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_uml_namedelement_has_visibility():
    assert hasattr(uml_NamedElement, "visibility")
    descriptor = None
    for klass in uml_NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml_namedelement_has_name():
    assert hasattr(uml_NamedElement, "name")
    descriptor = None
    for klass in uml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uml_namedelement_has_qualifiedName():
    assert hasattr(uml_NamedElement, "qualifiedName")
    descriptor = None
    for klass in uml_NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_uml_activitygroup_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityGroup)


def test_uml_activitygroup_constructor_exists():
    assert callable(uml_ActivityGroup.__init__)


def test_uml_activitygroup_constructor_args():
    sig = inspect.signature(uml_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml_QualifierValue)


def test_uml_qualifiervalue_constructor_exists():
    assert callable(uml_QualifierValue.__init__)


def test_uml_qualifiervalue_constructor_args():
    sig = inspect.signature(uml_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_slot_is_not_abstract():
    assert not inspect.isabstract(uml_Slot)


def test_uml_slot_constructor_exists():
    assert callable(uml_Slot.__init__)


def test_uml_slot_constructor_args():
    sig = inspect.signature(uml_Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml_linkenddata_is_not_abstract():
    assert not inspect.isabstract(uml_LinkEndData)


def test_uml_linkenddata_constructor_exists():
    assert callable(uml_LinkEndData.__init__)


def test_uml_linkenddata_constructor_args():
    sig = inspect.signature(uml_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml_comment_is_not_abstract():
    assert not inspect.isabstract(uml_Comment)


def test_uml_comment_constructor_exists():
    assert callable(uml_Comment.__init__)


def test_uml_comment_constructor_args():
    sig = inspect.signature(uml_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uml_comment_has_body():
    assert hasattr(uml_Comment, "body")
    descriptor = None
    for klass in uml_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_element_is_not_abstract():
    assert not inspect.isabstract(uml_Element)


def test_uml_element_constructor_exists():
    assert callable(uml_Element.__init__)


def test_uml_element_constructor_args():
    sig = inspect.signature(uml_Element.__init__)
    params = list(sig.parameters.keys())

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

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "synchCall",
        "createMessage",
        "reply",
        "asynchSignal",
        "asynchCall",
        "deleteMessage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "LIFO",
        "unordered",
        "ordered",
        "FIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "par",
        "critical",
        "alt",
        "ignore",
        "assert_",
        "break_",
        "consider",
        "opt",
        "neg",
        "strict",
        "loop",
        "seq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "composite",
        "shared",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"

def test_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "stream",
        "iterative",
        "parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "out",
        "return_",
        "inout",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

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

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "fork",
        "choice",
        "initial",
        "join",
        "shallowHistory",
        "junction",
        "deepHistory",
        "entryPoint",
        "terminate",
        "exitPoint",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "sequential",
        "concurrent",
        "guarded",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

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

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "internal",
        "local",
        "external",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

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
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
uml_WriteStructuralFeatureAction_strategy = st.builds(
    uml_WriteStructuralFeatureAction,
)
uml_ClearStructuralFeatureAction_strategy = st.builds(
    uml_ClearStructuralFeatureAction,
)
uml_ReadStructuralFeatureAction_strategy = st.builds(
    uml_ReadStructuralFeatureAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
uml_RemoveStructuralFeatureValueAction_strategy = st.builds(
    uml_RemoveStructuralFeatureValueAction,
    isRemoveDuplicates=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
uml_ExecutionEnvironment_strategy = st.builds(
    uml_ExecutionEnvironment,
)
uml_Device_strategy = st.builds(
    uml_Device,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
uml_ConsiderIgnoreFragment_strategy = st.builds(
    uml_ConsiderIgnoreFragment,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
uml_ActivityFinalNode_strategy = st.builds(
    uml_ActivityFinalNode,
)
uml_FlowFinalNode_strategy = st.builds(
    uml_FlowFinalNode,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
uml_ReceiveOperationEvent_strategy = st.builds(
    uml_ReceiveOperationEvent,
)
uml_SendSignalEvent_strategy = st.builds(
    uml_SendSignalEvent,
)
uml_AnyReceiveEvent_strategy = st.builds(
    uml_AnyReceiveEvent,
)
uml_ReceiveSignalEvent_strategy = st.builds(
    uml_ReceiveSignalEvent,
)
uml_CallEvent_strategy = st.builds(
    uml_CallEvent,
)
uml_SignalEvent_strategy = st.builds(
    uml_SignalEvent,
)
uml_SendOperationEvent_strategy = st.builds(
    uml_SendOperationEvent,
)
Event_strategy = st.builds(
    Event,
)
uml_CreationEvent_strategy = st.builds(
    uml_CreationEvent,
)
uml_DestructionEvent_strategy = st.builds(
    uml_DestructionEvent,
)
uml_MessageEvent_strategy = st.builds(
    uml_MessageEvent,
)
uml_ChangeEvent_strategy = st.builds(
    uml_ChangeEvent,
)
uml_ExecutionEvent_strategy = st.builds(
    uml_ExecutionEvent,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
uml_BehaviorExecutionSpecification_strategy = st.builds(
    uml_BehaviorExecutionSpecification,
)
uml_ActionExecutionSpecification_strategy = st.builds(
    uml_ActionExecutionSpecification,
)
Constraint_strategy = st.builds(
    Constraint,
)
uml_InteractionConstraint_strategy = st.builds(
    uml_InteractionConstraint,
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
uml_ExecutionOccurrenceSpecification_strategy = st.builds(
    uml_ExecutionOccurrenceSpecification,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
uml_MessageOccurrenceSpecification_strategy = st.builds(
    uml_MessageOccurrenceSpecification,
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
uml_PartDecomposition_strategy = st.builds(
    uml_PartDecomposition,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
uml_CombinedFragment_strategy = st.builds(
    uml_CombinedFragment,
    interactionOperator=
        safe_text
)
uml_ExecutionSpecification_strategy = st.builds(
    uml_ExecutionSpecification,
)
uml_Continuation_strategy = st.builds(
    uml_Continuation,
    setting=
        safe_text
)
uml_StateInvariant_strategy = st.builds(
    uml_StateInvariant,
)
uml_InteractionUse_strategy = st.builds(
    uml_InteractionUse,
)
uml_OccurrenceSpecification_strategy = st.builds(
    uml_OccurrenceSpecification,
)
InputPin_strategy = st.builds(
    InputPin,
)
uml_ValuePin_strategy = st.builds(
    uml_ValuePin,
)
uml_Gate_strategy = st.builds(
    uml_Gate,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
uml_SequenceNode_strategy = st.builds(
    uml_SequenceNode,
)
CallAction_strategy = st.builds(
    CallAction,
)
uml_CallBehaviorAction_strategy = st.builds(
    uml_CallBehaviorAction,
)
uml_CallOperationAction_strategy = st.builds(
    uml_CallOperationAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
uml_SendSignalAction_strategy = st.builds(
    uml_SendSignalAction,
)
uml_CallAction_strategy = st.builds(
    uml_CallAction,
    isSynchronous=
        safe_text
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
uml_CentralBufferNode_strategy = st.builds(
    uml_CentralBufferNode,
)
Pin_strategy = st.builds(
    Pin,
)
uml_ActivityParameterNode_strategy = st.builds(
    uml_ActivityParameterNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
uml_FinalNode_strategy = st.builds(
    uml_FinalNode,
)
uml_ForkNode_strategy = st.builds(
    uml_ForkNode,
)
uml_DecisionNode_strategy = st.builds(
    uml_DecisionNode,
)
uml_MergeNode_strategy = st.builds(
    uml_MergeNode,
)
uml_InitialNode_strategy = st.builds(
    uml_InitialNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
uml_ObjectFlow_strategy = st.builds(
    uml_ObjectFlow,
    isMulticast=
        safe_text,
    isMultireceive=
        safe_text
)
uml_ControlFlow_strategy = st.builds(
    uml_ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
uml_InterruptibleActivityRegion_strategy = st.builds(
    uml_InterruptibleActivityRegion,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
uml_ControlNode_strategy = st.builds(
    uml_ControlNode,
)
uml_ExecutableNode_strategy = st.builds(
    uml_ExecutableNode,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
uml_Action_strategy = st.builds(
    uml_Action,
)
uml_OutputPin_strategy = st.builds(
    uml_OutputPin,
)
uml_InputPin_strategy = st.builds(
    uml_InputPin,
)
Action_strategy = st.builds(
    Action,
)
uml_StructuralFeatureAction_strategy = st.builds(
    uml_StructuralFeatureAction,
)
uml_InvocationAction_strategy = st.builds(
    uml_InvocationAction,
)
uml_CreateObjectAction_strategy = st.builds(
    uml_CreateObjectAction,
)
uml_TestIdentityAction_strategy = st.builds(
    uml_TestIdentityAction,
)
uml_DestroyObjectAction_strategy = st.builds(
    uml_DestroyObjectAction,
    isDestroyOwnedObjects=
        safe_text,
    isDestroyLinks=
        safe_text
)
uml_ReadSelfAction_strategy = st.builds(
    uml_ReadSelfAction,
)
uml_OpaqueAction_strategy = st.builds(
    uml_OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
uml_FunctionBehavior_strategy = st.builds(
    uml_FunctionBehavior,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
uml_LiteralUnlimitedNatural_strategy = st.builds(
    uml_LiteralUnlimitedNatural,
    value=
        safe_text
)
uml_LiteralString_strategy = st.builds(
    uml_LiteralString,
    value=
        safe_text
)
uml_LiteralNull_strategy = st.builds(
    uml_LiteralNull,
)
uml_LiteralBoolean_strategy = st.builds(
    uml_LiteralBoolean,
    value=
        safe_text
)
uml_LiteralInteger_strategy = st.builds(
    uml_LiteralInteger,
    value=
        safe_text
)
uml_EnumerationLiteral_strategy = st.builds(
    uml_EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
uml_PrimitiveType_strategy = st.builds(
    uml_PrimitiveType,
)
uml_Enumeration_strategy = st.builds(
    uml_Enumeration,
)
Transition_strategy = st.builds(
    Transition,
)
uml_ProtocolTransition_strategy = st.builds(
    uml_ProtocolTransition,
)
uml_ExpansionRegion_strategy = st.builds(
    uml_ExpansionRegion,
    mode=
        safe_text
)
uml_ExpansionNode_strategy = st.builds(
    uml_ExpansionNode,
)
uml_LoopNode_strategy = st.builds(
    uml_LoopNode,
    isTestedFirst=
        safe_text
)
uml_ConditionalNode_strategy = st.builds(
    uml_ConditionalNode,
    isDeterminate=
        safe_text,
    isAssured=
        safe_text
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
uml_DataStoreNode_strategy = st.builds(
    uml_DataStoreNode,
)
uml_JoinNode_strategy = st.builds(
    uml_JoinNode,
    isCombineDuplicate=
        safe_text
)
uml_StartObjectBehaviorAction_strategy = st.builds(
    uml_StartObjectBehaviorAction,
)
uml_ReduceAction_strategy = st.builds(
    uml_ReduceAction,
    isOrdered=
        safe_text
)
uml_UnmarshallAction_strategy = st.builds(
    uml_UnmarshallAction,
)
uml_ReplyAction_strategy = st.builds(
    uml_ReplyAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
uml_AcceptCallAction_strategy = st.builds(
    uml_AcceptCallAction,
)
uml_AcceptEventAction_strategy = st.builds(
    uml_AcceptEventAction,
    isUnmarshall=
        safe_text
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
uml_CreateLinkObjectAction_strategy = st.builds(
    uml_CreateLinkObjectAction,
)
uml_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml_ReadLinkObjectEndQualifierAction,
)
uml_StartClassifierBehaviorAction_strategy = st.builds(
    uml_StartClassifierBehaviorAction,
)
uml_ReadIsClassifiedObjectAction_strategy = st.builds(
    uml_ReadIsClassifiedObjectAction,
    isDirect=
        safe_text
)
uml_ReclassifyObjectAction_strategy = st.builds(
    uml_ReclassifyObjectAction,
    isReplaceAll=
        safe_text
)
uml_ReadLinkObjectEndAction_strategy = st.builds(
    uml_ReadLinkObjectEndAction,
)
uml_ReadExtentAction_strategy = st.builds(
    uml_ReadExtentAction,
)
uml_ActionInputPin_strategy = st.builds(
    uml_ActionInputPin,
)
uml_RaiseExceptionAction_strategy = st.builds(
    uml_RaiseExceptionAction,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
uml_RemoveVariableValueAction_strategy = st.builds(
    uml_RemoveVariableValueAction,
    isRemoveDuplicates=
        safe_text
)
uml_AddVariableValueAction_strategy = st.builds(
    uml_AddVariableValueAction,
    isReplaceAll=
        safe_text
)
VariableAction_strategy = st.builds(
    VariableAction,
)
uml_ClearVariableAction_strategy = st.builds(
    uml_ClearVariableAction,
)
uml_WriteVariableAction_strategy = st.builds(
    uml_WriteVariableAction,
)
uml_ReadVariableAction_strategy = st.builds(
    uml_ReadVariableAction,
)
uml_VariableAction_strategy = st.builds(
    uml_VariableAction,
)
uml_TimeEvent_strategy = st.builds(
    uml_TimeEvent,
    isRelative=
        safe_text
)
State_strategy = st.builds(
    State,
)
uml_FinalState_strategy = st.builds(
    uml_FinalState,
)
Observation_strategy = st.builds(
    Observation,
)
uml_DurationObservation_strategy = st.builds(
    uml_DurationObservation,
    firstEvent=
        safe_text
)
uml_TimeObservation_strategy = st.builds(
    uml_TimeObservation,
    firstEvent=
        safe_text
)
uml_IntervalConstraint_strategy = st.builds(
    uml_IntervalConstraint,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
uml_DurationConstraint_strategy = st.builds(
    uml_DurationConstraint,
    firstEvent=
        safe_text
)
uml_TimeConstraint_strategy = st.builds(
    uml_TimeConstraint,
    firstEvent=
        safe_text
)
Interval_strategy = st.builds(
    Interval,
)
uml_TimeInterval_strategy = st.builds(
    uml_TimeInterval,
)
uml_DurationInterval_strategy = st.builds(
    uml_DurationInterval,
)
uml_ValueSpecificationAction_strategy = st.builds(
    uml_ValueSpecificationAction,
)
uml_SendObjectAction_strategy = st.builds(
    uml_SendObjectAction,
)
uml_BroadcastSignalAction_strategy = st.builds(
    uml_BroadcastSignalAction,
)
uml_ClearAssociationAction_strategy = st.builds(
    uml_ClearAssociationAction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
uml_DestroyLinkAction_strategy = st.builds(
    uml_DestroyLinkAction,
)
uml_CreateLinkAction_strategy = st.builds(
    uml_CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
uml_LinkEndDestructionData_strategy = st.builds(
    uml_LinkEndDestructionData,
    isDestroyDuplicates=
        safe_text
)
uml_LinkEndCreationData_strategy = st.builds(
    uml_LinkEndCreationData,
    isReplaceAll=
        safe_text
)
LinkAction_strategy = st.builds(
    LinkAction,
)
uml_WriteLinkAction_strategy = st.builds(
    uml_WriteLinkAction,
)
uml_ReadLinkAction_strategy = st.builds(
    uml_ReadLinkAction,
)
uml_LinkAction_strategy = st.builds(
    uml_LinkAction,
)
uml_AddStructuralFeatureValueAction_strategy = st.builds(
    uml_AddStructuralFeatureValueAction,
    isReplaceAll=
        safe_text
)
TemplateSignature_strategy = st.builds(
    TemplateSignature,
)
Expression_strategy = st.builds(
    Expression,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
uml_ConnectableElementTemplateParameter_strategy = st.builds(
    uml_ConnectableElementTemplateParameter,
)
uml_ClassifierTemplateParameter_strategy = st.builds(
    uml_ClassifierTemplateParameter,
    allowSubstitutable=
        safe_text
)
uml_OperationTemplateParameter_strategy = st.builds(
    uml_OperationTemplateParameter,
)
Association_strategy = st.builds(
    Association,
)
uml_CommunicationPath_strategy = st.builds(
    uml_CommunicationPath,
)
Package_strategy = st.builds(
    Package,
)
uml_Model_strategy = st.builds(
    uml_Model,
    viewpoint=
        safe_text
)
uml_Profile_strategy = st.builds(
    uml_Profile,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
uml_EncapsulatedClassifier_strategy = st.builds(
    uml_EncapsulatedClassifier,
)
Vertex_strategy = st.builds(
    Vertex,
)
Property_strategy = st.builds(
    Property,
)
uml_ExtensionEnd_strategy = st.builds(
    uml_ExtensionEnd,
)
uml_Port_strategy = st.builds(
    uml_Port,
    isService=
        safe_text,
    isBehavior=
        safe_text
)
uml_ConnectionPointReference_strategy = st.builds(
    uml_ConnectionPointReference,
)
uml_Pseudostate_strategy = st.builds(
    uml_Pseudostate,
    kind=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
uml_Activity_strategy = st.builds(
    uml_Activity,
    isReadOnly=
        safe_text,
    isSingleExecution=
        safe_text
)
uml_OpaqueBehavior_strategy = st.builds(
    uml_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
uml_Interaction_strategy = st.builds(
    uml_Interaction,
)
uml_StateMachine_strategy = st.builds(
    uml_StateMachine,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
uml_ProtocolStateMachine_strategy = st.builds(
    uml_ProtocolStateMachine,
)
Class_strategy = st.builds(
    Class,
)
uml_Component_strategy = st.builds(
    uml_Component,
    isIndirectlyInstantiated=
        safe_text
)
uml_AssociationClass_strategy = st.builds(
    uml_AssociationClass,
)
uml_Stereotype_strategy = st.builds(
    uml_Stereotype,
)
uml_Extension_strategy = st.builds(
    uml_Extension,
    isRequired=
        safe_text
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
uml_Collaboration_strategy = st.builds(
    uml_Collaboration,
)
uml_Actor_strategy = st.builds(
    uml_Actor,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
uml_Reception_strategy = st.builds(
    uml_Reception,
)
Feature_strategy = st.builds(
    Feature,
)
uml_Connector_strategy = st.builds(
    uml_Connector,
    kind=
        safe_text
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
Artifact_strategy = st.builds(
    Artifact,
)
uml_DeploymentSpecification_strategy = st.builds(
    uml_DeploymentSpecification,
    deploymentLocation=
        safe_text,
    executionLocation=
        safe_text
)
uml_Class_strategy = st.builds(
    uml_Class,
    isActive=
        safe_text
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
uml_Node_strategy = st.builds(
    uml_Node,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
Realization_strategy = st.builds(
    Realization,
)
uml_InterfaceRealization_strategy = st.builds(
    uml_InterfaceRealization,
)
uml_ComponentRealization_strategy = st.builds(
    uml_ComponentRealization,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
uml_Pin_strategy = st.builds(
    uml_Pin,
    isControl=
        safe_text
)
uml_ConnectorEnd_strategy = st.builds(
    uml_ConnectorEnd,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
uml_Variable_strategy = st.builds(
    uml_Variable,
)
uml_Behavior_strategy = st.builds(
    uml_Behavior,
    isReentrant=
        safe_text
)
uml_Parameter_strategy = st.builds(
    uml_Parameter,
    isStream=
        safe_text,
    isException=
        safe_text,
    default=
        safe_text,
    effect=
        safe_text,
    direction=
        safe_text
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
uml_LiteralSpecification_strategy = st.builds(
    uml_LiteralSpecification,
)
uml_Interval_strategy = st.builds(
    uml_Interval,
)
uml_TimeExpression_strategy = st.builds(
    uml_TimeExpression,
)
uml_InstanceValue_strategy = st.builds(
    uml_InstanceValue,
)
uml_Expression_strategy = st.builds(
    uml_Expression,
    symbol=
        safe_text
)
uml_Duration_strategy = st.builds(
    uml_Duration,
)
uml_OpaqueExpression_strategy = st.builds(
    uml_OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
Dependency_strategy = st.builds(
    Dependency,
)
uml_Usage_strategy = st.builds(
    uml_Usage,
)
uml_Deployment_strategy = st.builds(
    uml_Deployment,
)
uml_Abstraction_strategy = st.builds(
    uml_Abstraction,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
uml_Manifestation_strategy = st.builds(
    uml_Manifestation,
)
uml_Realization_strategy = st.builds(
    uml_Realization,
)
uml_UseCase_strategy = st.builds(
    uml_UseCase,
)
uml_Substitution_strategy = st.builds(
    uml_Substitution,
)
uml_Property_strategy = st.builds(
    uml_Property,
    isComposite=
        safe_text,
    isDerivedUnion=
        safe_text,
    aggregation=
        safe_text,
    isDerived=
        safe_text,
    default=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uml_InformationItem_strategy = st.builds(
    uml_InformationItem,
)
uml_Signal_strategy = st.builds(
    uml_Signal,
)
uml_Interface_strategy = st.builds(
    uml_Interface,
)
uml_Artifact_strategy = st.builds(
    uml_Artifact,
    fileName=
        safe_text
)
uml_DataType_strategy = st.builds(
    uml_DataType,
)
uml_StructuredClassifier_strategy = st.builds(
    uml_StructuredClassifier,
)
uml_BehavioredClassifier_strategy = st.builds(
    uml_BehavioredClassifier,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uml_ObjectNode_strategy = st.builds(
    uml_ObjectNode,
    ordering=
        safe_text,
    isControlType=
        safe_text
)
uml_StructuralFeature_strategy = st.builds(
    uml_StructuralFeature,
    isReadOnly=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
uml_Feature_strategy = st.builds(
    uml_Feature,
    isStatic=
        safe_text
)
uml_ExtensionPoint_strategy = st.builds(
    uml_ExtensionPoint,
)
uml_ActivityNode_strategy = st.builds(
    uml_ActivityNode,
)
uml_RedefinableTemplateSignature_strategy = st.builds(
    uml_RedefinableTemplateSignature,
)
uml_ActivityEdge_strategy = st.builds(
    uml_ActivityEdge,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
uml_ConnectableElement_strategy = st.builds(
    uml_ConnectableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml_GeneralOrdering_strategy = st.builds(
    uml_GeneralOrdering,
)
uml_CollaborationUse_strategy = st.builds(
    uml_CollaborationUse,
)
uml_MessageEnd_strategy = st.builds(
    uml_MessageEnd,
)
uml_Message_strategy = st.builds(
    uml_Message,
    messageSort=
        safe_text,
    messageKind=
        safe_text
)
uml_ActivityPartition_strategy = st.builds(
    uml_ActivityPartition,
    isDimension=
        safe_text,
    isExternal=
        safe_text
)
uml_Lifeline_strategy = st.builds(
    uml_Lifeline,
)
uml_Trigger_strategy = st.builds(
    uml_Trigger,
)
uml_TypedElement_strategy = st.builds(
    uml_TypedElement,
)
uml_Vertex_strategy = st.builds(
    uml_Vertex,
)
uml_ParameterSet_strategy = st.builds(
    uml_ParameterSet,
)
uml_DeploymentTarget_strategy = st.builds(
    uml_DeploymentTarget,
)
uml_Namespace_strategy = st.builds(
    uml_Namespace,
)
uml_InteractionFragment_strategy = st.builds(
    uml_InteractionFragment,
)
uml_DeployedArtifact_strategy = st.builds(
    uml_DeployedArtifact,
)
uml_RedefinableElement_strategy = st.builds(
    uml_RedefinableElement,
    isLeaf=
        safe_text
)
uml_PackageableElement_strategy = st.builds(
    uml_PackageableElement,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
uml_Operation_strategy = st.builds(
    uml_Operation,
    isOrdered=
        safe_text,
    lower=
        safe_text,
    isQuery=
        safe_text,
    upper=
        safe_text,
    isUnique=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml_GeneralizationSet_strategy = st.builds(
    uml_GeneralizationSet,
    isDisjoint=
        safe_text,
    isCovering=
        safe_text
)
uml_Constraint_strategy = st.builds(
    uml_Constraint,
)
uml_Event_strategy = st.builds(
    uml_Event,
)
uml_ValueSpecification_strategy = st.builds(
    uml_ValueSpecification,
)
uml_Type_strategy = st.builds(
    uml_Type,
)
uml_InstanceSpecification_strategy = st.builds(
    uml_InstanceSpecification,
)
uml_Observation_strategy = st.builds(
    uml_Observation,
)
Namespace_strategy = st.builds(
    Namespace,
)
uml_InteractionOperand_strategy = st.builds(
    uml_InteractionOperand,
)
uml_Transition_strategy = st.builds(
    uml_Transition,
    kind=
        safe_text
)
uml_Region_strategy = st.builds(
    uml_Region,
)
uml_StructuredActivityNode_strategy = st.builds(
    uml_StructuredActivityNode,
    mustIsolate=
        safe_text
)
uml_BehavioralFeature_strategy = st.builds(
    uml_BehavioralFeature,
    isAbstract=
        safe_text,
    concurrency=
        safe_text
)
uml_State_strategy = st.builds(
    uml_State,
    isSimple=
        safe_text,
    isComposite=
        safe_text,
    isOrthogonal=
        safe_text,
    isSubmachineState=
        safe_text
)
uml_Classifier_strategy = st.builds(
    uml_Classifier,
    isAbstract=
        safe_text
)
uml_Package_strategy = st.builds(
    uml_Package,
)
Relationship_strategy = st.builds(
    Relationship,
)
uml_Association_strategy = st.builds(
    uml_Association,
    isDerived=
        safe_text
)
uml_DirectedRelationship_strategy = st.builds(
    uml_DirectedRelationship,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
uml_Generalization_strategy = st.builds(
    uml_Generalization,
    isSubstitutable=
        safe_text
)
uml_ProtocolConformance_strategy = st.builds(
    uml_ProtocolConformance,
)
uml_PackageImport_strategy = st.builds(
    uml_PackageImport,
    visibility=
        safe_text
)
uml_InformationFlow_strategy = st.builds(
    uml_InformationFlow,
)
uml_TemplateBinding_strategy = st.builds(
    uml_TemplateBinding,
)
uml_ElementImport_strategy = st.builds(
    uml_ElementImport,
    alias=
        safe_text,
    visibility=
        safe_text
)
uml_Extend_strategy = st.builds(
    uml_Extend,
)
uml_PackageMerge_strategy = st.builds(
    uml_PackageMerge,
)
uml_ProfileApplication_strategy = st.builds(
    uml_ProfileApplication,
    isStrict=
        safe_text
)
uml_Include_strategy = st.builds(
    uml_Include,
)
uml_Dependency_strategy = st.builds(
    uml_Dependency,
)
uml_StringExpression_strategy = st.builds(
    uml_StringExpression,
)
Element_strategy = st.builds(
    Element,
)
uml_TemplateSignature_strategy = st.builds(
    uml_TemplateSignature,
)
uml_Image_strategy = st.builds(
    uml_Image,
    format=
        safe_text,
    content=
        safe_text,
    location=
        safe_text
)
uml_TemplateParameterSubstitution_strategy = st.builds(
    uml_TemplateParameterSubstitution,
)
uml_ParameterableElement_strategy = st.builds(
    uml_ParameterableElement,
)
uml_TemplateParameter_strategy = st.builds(
    uml_TemplateParameter,
)
uml_MultiplicityElement_strategy = st.builds(
    uml_MultiplicityElement,
    isUnique=
        safe_text,
    lower=
        safe_text,
    upper=
        safe_text,
    isOrdered=
        safe_text
)
uml_TemplateableElement_strategy = st.builds(
    uml_TemplateableElement,
)
uml_ExceptionHandler_strategy = st.builds(
    uml_ExceptionHandler,
)
uml_Clause_strategy = st.builds(
    uml_Clause,
)
uml_Relationship_strategy = st.builds(
    uml_Relationship,
)
uml_NamedElement_strategy = st.builds(
    uml_NamedElement,
    visibility=
        safe_text,
    name=
        safe_text,
    qualifiedName=
        safe_text
)
uml_ActivityGroup_strategy = st.builds(
    uml_ActivityGroup,
)
uml_QualifierValue_strategy = st.builds(
    uml_QualifierValue,
)
uml_Slot_strategy = st.builds(
    uml_Slot,
)
uml_LinkEndData_strategy = st.builds(
    uml_LinkEndData,
)
uml_Comment_strategy = st.builds(
    uml_Comment,
    body=
        safe_text
)
EModelElement_strategy = st.builds(
    EModelElement,
)
uml_Element_strategy = st.builds(
    uml_Element,
)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=uml_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_WriteStructuralFeatureAction)

@given(instance=uml_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_ClearStructuralFeatureAction)

@given(instance=uml_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_ReadStructuralFeatureAction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=uml_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_RemoveStructuralFeatureValueAction)



@given(instance=uml_RemoveStructuralFeatureValueAction_strategy)
def test_uml_removestructuralfeaturevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=uml_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml_executionenvironment_instantiation(instance):
    assert isinstance(instance, uml_ExecutionEnvironment)

@given(instance=uml_Device_strategy)
@settings(max_examples=50)
def test_uml_device_instantiation(instance):
    assert isinstance(instance, uml_Device)

@given(instance=CombinedFragment_strategy)
@settings(max_examples=50)
def test_combinedfragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)

@given(instance=uml_ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_uml_considerignorefragment_instantiation(instance):
    assert isinstance(instance, uml_ConsiderIgnoreFragment)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=uml_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml_activityfinalnode_instantiation(instance):
    assert isinstance(instance, uml_ActivityFinalNode)

@given(instance=uml_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml_flowfinalnode_instantiation(instance):
    assert isinstance(instance, uml_FlowFinalNode)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=uml_ReceiveOperationEvent_strategy)
@settings(max_examples=50)
def test_uml_receiveoperationevent_instantiation(instance):
    assert isinstance(instance, uml_ReceiveOperationEvent)

@given(instance=uml_SendSignalEvent_strategy)
@settings(max_examples=50)
def test_uml_sendsignalevent_instantiation(instance):
    assert isinstance(instance, uml_SendSignalEvent)

@given(instance=uml_AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml_anyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml_AnyReceiveEvent)

@given(instance=uml_ReceiveSignalEvent_strategy)
@settings(max_examples=50)
def test_uml_receivesignalevent_instantiation(instance):
    assert isinstance(instance, uml_ReceiveSignalEvent)

@given(instance=uml_CallEvent_strategy)
@settings(max_examples=50)
def test_uml_callevent_instantiation(instance):
    assert isinstance(instance, uml_CallEvent)

@given(instance=uml_SignalEvent_strategy)
@settings(max_examples=50)
def test_uml_signalevent_instantiation(instance):
    assert isinstance(instance, uml_SignalEvent)

@given(instance=uml_SendOperationEvent_strategy)
@settings(max_examples=50)
def test_uml_sendoperationevent_instantiation(instance):
    assert isinstance(instance, uml_SendOperationEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=uml_CreationEvent_strategy)
@settings(max_examples=50)
def test_uml_creationevent_instantiation(instance):
    assert isinstance(instance, uml_CreationEvent)

@given(instance=uml_DestructionEvent_strategy)
@settings(max_examples=50)
def test_uml_destructionevent_instantiation(instance):
    assert isinstance(instance, uml_DestructionEvent)

@given(instance=uml_MessageEvent_strategy)
@settings(max_examples=50)
def test_uml_messageevent_instantiation(instance):
    assert isinstance(instance, uml_MessageEvent)

@given(instance=uml_ChangeEvent_strategy)
@settings(max_examples=50)
def test_uml_changeevent_instantiation(instance):
    assert isinstance(instance, uml_ChangeEvent)

@given(instance=uml_ExecutionEvent_strategy)
@settings(max_examples=50)
def test_uml_executionevent_instantiation(instance):
    assert isinstance(instance, uml_ExecutionEvent)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=uml_BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_BehaviorExecutionSpecification)

@given(instance=uml_ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_ActionExecutionSpecification)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=uml_InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml_interactionconstraint_instantiation(instance):
    assert isinstance(instance, uml_InteractionConstraint)

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=uml_ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_ExecutionOccurrenceSpecification)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=uml_MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_MessageOccurrenceSpecification)

@given(instance=InteractionUse_strategy)
@settings(max_examples=50)
def test_interactionuse_instantiation(instance):
    assert isinstance(instance, InteractionUse)

@given(instance=uml_PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml_partdecomposition_instantiation(instance):
    assert isinstance(instance, uml_PartDecomposition)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=uml_CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml_combinedfragment_instantiation(instance):
    assert isinstance(instance, uml_CombinedFragment)



@given(instance=uml_CombinedFragment_strategy)
def test_uml_combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=uml_ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_executionspecification_instantiation(instance):
    assert isinstance(instance, uml_ExecutionSpecification)

@given(instance=uml_Continuation_strategy)
@settings(max_examples=50)
def test_uml_continuation_instantiation(instance):
    assert isinstance(instance, uml_Continuation)



@given(instance=uml_Continuation_strategy)
def test_uml_continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=uml_StateInvariant_strategy)
@settings(max_examples=50)
def test_uml_stateinvariant_instantiation(instance):
    assert isinstance(instance, uml_StateInvariant)

@given(instance=uml_InteractionUse_strategy)
@settings(max_examples=50)
def test_uml_interactionuse_instantiation(instance):
    assert isinstance(instance, uml_InteractionUse)

@given(instance=uml_OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_occurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_OccurrenceSpecification)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=uml_ValuePin_strategy)
@settings(max_examples=50)
def test_uml_valuepin_instantiation(instance):
    assert isinstance(instance, uml_ValuePin)

@given(instance=uml_Gate_strategy)
@settings(max_examples=50)
def test_uml_gate_instantiation(instance):
    assert isinstance(instance, uml_Gate)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=uml_SequenceNode_strategy)
@settings(max_examples=50)
def test_uml_sequencenode_instantiation(instance):
    assert isinstance(instance, uml_SequenceNode)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=uml_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_callbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_CallBehaviorAction)

@given(instance=uml_CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml_calloperationaction_instantiation(instance):
    assert isinstance(instance, uml_CallOperationAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=uml_SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml_sendsignalaction_instantiation(instance):
    assert isinstance(instance, uml_SendSignalAction)

@given(instance=uml_CallAction_strategy)
@settings(max_examples=50)
def test_uml_callaction_instantiation(instance):
    assert isinstance(instance, uml_CallAction)



@given(instance=uml_CallAction_strategy)
def test_uml_callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=uml_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml_centralbuffernode_instantiation(instance):
    assert isinstance(instance, uml_CentralBufferNode)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=uml_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml_activityparameternode_instantiation(instance):
    assert isinstance(instance, uml_ActivityParameterNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=uml_FinalNode_strategy)
@settings(max_examples=50)
def test_uml_finalnode_instantiation(instance):
    assert isinstance(instance, uml_FinalNode)

@given(instance=uml_ForkNode_strategy)
@settings(max_examples=50)
def test_uml_forknode_instantiation(instance):
    assert isinstance(instance, uml_ForkNode)

@given(instance=uml_DecisionNode_strategy)
@settings(max_examples=50)
def test_uml_decisionnode_instantiation(instance):
    assert isinstance(instance, uml_DecisionNode)

@given(instance=uml_MergeNode_strategy)
@settings(max_examples=50)
def test_uml_mergenode_instantiation(instance):
    assert isinstance(instance, uml_MergeNode)

@given(instance=uml_InitialNode_strategy)
@settings(max_examples=50)
def test_uml_initialnode_instantiation(instance):
    assert isinstance(instance, uml_InitialNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=uml_ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml_objectflow_instantiation(instance):
    assert isinstance(instance, uml_ObjectFlow)



@given(instance=uml_ObjectFlow_strategy)
def test_uml_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original



@given(instance=uml_ObjectFlow_strategy)
def test_uml_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=uml_ControlFlow_strategy)
@settings(max_examples=50)
def test_uml_controlflow_instantiation(instance):
    assert isinstance(instance, uml_ControlFlow)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=uml_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml_InterruptibleActivityRegion)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=uml_ControlNode_strategy)
@settings(max_examples=50)
def test_uml_controlnode_instantiation(instance):
    assert isinstance(instance, uml_ControlNode)

@given(instance=uml_ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml_executablenode_instantiation(instance):
    assert isinstance(instance, uml_ExecutableNode)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=uml_Action_strategy)
@settings(max_examples=50)
def test_uml_action_instantiation(instance):
    assert isinstance(instance, uml_Action)

@given(instance=uml_OutputPin_strategy)
@settings(max_examples=50)
def test_uml_outputpin_instantiation(instance):
    assert isinstance(instance, uml_OutputPin)

@given(instance=uml_InputPin_strategy)
@settings(max_examples=50)
def test_uml_inputpin_instantiation(instance):
    assert isinstance(instance, uml_InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=uml_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_StructuralFeatureAction)

@given(instance=uml_InvocationAction_strategy)
@settings(max_examples=50)
def test_uml_invocationaction_instantiation(instance):
    assert isinstance(instance, uml_InvocationAction)

@given(instance=uml_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml_createobjectaction_instantiation(instance):
    assert isinstance(instance, uml_CreateObjectAction)

@given(instance=uml_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml_testidentityaction_instantiation(instance):
    assert isinstance(instance, uml_TestIdentityAction)

@given(instance=uml_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_DestroyObjectAction)



@given(instance=uml_DestroyObjectAction_strategy)
def test_uml_destroyobjectaction_isDestroyOwnedObjects_setter(instance):
    original = instance.isDestroyOwnedObjects
    instance.isDestroyOwnedObjects = original
    assert instance.isDestroyOwnedObjects == original



@given(instance=uml_DestroyObjectAction_strategy)
def test_uml_destroyobjectaction_isDestroyLinks_setter(instance):
    original = instance.isDestroyLinks
    instance.isDestroyLinks = original
    assert instance.isDestroyLinks == original

@given(instance=uml_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml_readselfaction_instantiation(instance):
    assert isinstance(instance, uml_ReadSelfAction)

@given(instance=uml_OpaqueAction_strategy)
@settings(max_examples=50)
def test_uml_opaqueaction_instantiation(instance):
    assert isinstance(instance, uml_OpaqueAction)



@given(instance=uml_OpaqueAction_strategy)
def test_uml_opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=uml_OpaqueAction_strategy)
def test_uml_opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=uml_FunctionBehavior_strategy)
@settings(max_examples=50)
def test_uml_functionbehavior_instantiation(instance):
    assert isinstance(instance, uml_FunctionBehavior)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=uml_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml_LiteralUnlimitedNatural)



@given(instance=uml_LiteralUnlimitedNatural_strategy)
def test_uml_literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml_LiteralString_strategy)
@settings(max_examples=50)
def test_uml_literalstring_instantiation(instance):
    assert isinstance(instance, uml_LiteralString)



@given(instance=uml_LiteralString_strategy)
def test_uml_literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml_LiteralNull_strategy)
@settings(max_examples=50)
def test_uml_literalnull_instantiation(instance):
    assert isinstance(instance, uml_LiteralNull)

@given(instance=uml_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml_literalboolean_instantiation(instance):
    assert isinstance(instance, uml_LiteralBoolean)



@given(instance=uml_LiteralBoolean_strategy)
def test_uml_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml_LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml_literalinteger_instantiation(instance):
    assert isinstance(instance, uml_LiteralInteger)



@given(instance=uml_LiteralInteger_strategy)
def test_uml_literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml_enumerationliteral_instantiation(instance):
    assert isinstance(instance, uml_EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=uml_PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml_primitivetype_instantiation(instance):
    assert isinstance(instance, uml_PrimitiveType)

@given(instance=uml_Enumeration_strategy)
@settings(max_examples=50)
def test_uml_enumeration_instantiation(instance):
    assert isinstance(instance, uml_Enumeration)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=uml_ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml_protocoltransition_instantiation(instance):
    assert isinstance(instance, uml_ProtocolTransition)

@given(instance=uml_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml_expansionregion_instantiation(instance):
    assert isinstance(instance, uml_ExpansionRegion)



@given(instance=uml_ExpansionRegion_strategy)
def test_uml_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=uml_ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml_expansionnode_instantiation(instance):
    assert isinstance(instance, uml_ExpansionNode)

@given(instance=uml_LoopNode_strategy)
@settings(max_examples=50)
def test_uml_loopnode_instantiation(instance):
    assert isinstance(instance, uml_LoopNode)



@given(instance=uml_LoopNode_strategy)
def test_uml_loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=uml_ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml_conditionalnode_instantiation(instance):
    assert isinstance(instance, uml_ConditionalNode)



@given(instance=uml_ConditionalNode_strategy)
def test_uml_conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original



@given(instance=uml_ConditionalNode_strategy)
def test_uml_conditionalnode_isAssured_setter(instance):
    original = instance.isAssured
    instance.isAssured = original
    assert instance.isAssured == original

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=uml_DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml_datastorenode_instantiation(instance):
    assert isinstance(instance, uml_DataStoreNode)

@given(instance=uml_JoinNode_strategy)
@settings(max_examples=50)
def test_uml_joinnode_instantiation(instance):
    assert isinstance(instance, uml_JoinNode)



@given(instance=uml_JoinNode_strategy)
def test_uml_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=uml_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_StartObjectBehaviorAction)

@given(instance=uml_ReduceAction_strategy)
@settings(max_examples=50)
def test_uml_reduceaction_instantiation(instance):
    assert isinstance(instance, uml_ReduceAction)



@given(instance=uml_ReduceAction_strategy)
def test_uml_reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml_UnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml_unmarshallaction_instantiation(instance):
    assert isinstance(instance, uml_UnmarshallAction)

@given(instance=uml_ReplyAction_strategy)
@settings(max_examples=50)
def test_uml_replyaction_instantiation(instance):
    assert isinstance(instance, uml_ReplyAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=uml_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml_acceptcallaction_instantiation(instance):
    assert isinstance(instance, uml_AcceptCallAction)

@given(instance=uml_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml_accepteventaction_instantiation(instance):
    assert isinstance(instance, uml_AcceptEventAction)



@given(instance=uml_AcceptEventAction_strategy)
def test_uml_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=uml_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, uml_CreateLinkObjectAction)

@given(instance=uml_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml_ReadLinkObjectEndQualifierAction)

@given(instance=uml_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_StartClassifierBehaviorAction)

@given(instance=uml_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml_ReadIsClassifiedObjectAction)



@given(instance=uml_ReadIsClassifiedObjectAction_strategy)
def test_uml_readisclassifiedobjectaction_isDirect_setter(instance):
    original = instance.isDirect
    instance.isDirect = original
    assert instance.isDirect == original

@given(instance=uml_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_ReclassifyObjectAction)



@given(instance=uml_ReclassifyObjectAction_strategy)
def test_uml_reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml_ReadLinkObjectEndAction)

@given(instance=uml_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml_readextentaction_instantiation(instance):
    assert isinstance(instance, uml_ReadExtentAction)

@given(instance=uml_ActionInputPin_strategy)
@settings(max_examples=50)
def test_uml_actioninputpin_instantiation(instance):
    assert isinstance(instance, uml_ActionInputPin)

@given(instance=uml_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml_RaiseExceptionAction)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=uml_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_RemoveVariableValueAction)



@given(instance=uml_RemoveVariableValueAction_strategy)
def test_uml_removevariablevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=uml_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_AddVariableValueAction)



@given(instance=uml_AddVariableValueAction_strategy)
def test_uml_addvariablevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=uml_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml_clearvariableaction_instantiation(instance):
    assert isinstance(instance, uml_ClearVariableAction)

@given(instance=uml_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml_writevariableaction_instantiation(instance):
    assert isinstance(instance, uml_WriteVariableAction)

@given(instance=uml_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml_readvariableaction_instantiation(instance):
    assert isinstance(instance, uml_ReadVariableAction)

@given(instance=uml_VariableAction_strategy)
@settings(max_examples=50)
def test_uml_variableaction_instantiation(instance):
    assert isinstance(instance, uml_VariableAction)

@given(instance=uml_TimeEvent_strategy)
@settings(max_examples=50)
def test_uml_timeevent_instantiation(instance):
    assert isinstance(instance, uml_TimeEvent)



@given(instance=uml_TimeEvent_strategy)
def test_uml_timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=uml_FinalState_strategy)
@settings(max_examples=50)
def test_uml_finalstate_instantiation(instance):
    assert isinstance(instance, uml_FinalState)

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=uml_DurationObservation_strategy)
@settings(max_examples=50)
def test_uml_durationobservation_instantiation(instance):
    assert isinstance(instance, uml_DurationObservation)



@given(instance=uml_DurationObservation_strategy)
def test_uml_durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml_TimeObservation_strategy)
@settings(max_examples=50)
def test_uml_timeobservation_instantiation(instance):
    assert isinstance(instance, uml_TimeObservation)



@given(instance=uml_TimeObservation_strategy)
def test_uml_timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml_IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml_intervalconstraint_instantiation(instance):
    assert isinstance(instance, uml_IntervalConstraint)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=uml_DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml_durationconstraint_instantiation(instance):
    assert isinstance(instance, uml_DurationConstraint)



@given(instance=uml_DurationConstraint_strategy)
def test_uml_durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml_TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml_timeconstraint_instantiation(instance):
    assert isinstance(instance, uml_TimeConstraint)



@given(instance=uml_TimeConstraint_strategy)
def test_uml_timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=uml_TimeInterval_strategy)
@settings(max_examples=50)
def test_uml_timeinterval_instantiation(instance):
    assert isinstance(instance, uml_TimeInterval)

@given(instance=uml_DurationInterval_strategy)
@settings(max_examples=50)
def test_uml_durationinterval_instantiation(instance):
    assert isinstance(instance, uml_DurationInterval)

@given(instance=uml_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, uml_ValueSpecificationAction)

@given(instance=uml_SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml_sendobjectaction_instantiation(instance):
    assert isinstance(instance, uml_SendObjectAction)

@given(instance=uml_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml_BroadcastSignalAction)

@given(instance=uml_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml_clearassociationaction_instantiation(instance):
    assert isinstance(instance, uml_ClearAssociationAction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=uml_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml_destroylinkaction_instantiation(instance):
    assert isinstance(instance, uml_DestroyLinkAction)

@given(instance=uml_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml_createlinkaction_instantiation(instance):
    assert isinstance(instance, uml_CreateLinkAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=uml_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_uml_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, uml_LinkEndDestructionData)



@given(instance=uml_LinkEndDestructionData_strategy)
def test_uml_linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=uml_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, uml_LinkEndCreationData)



@given(instance=uml_LinkEndCreationData_strategy)
def test_uml_linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=uml_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml_writelinkaction_instantiation(instance):
    assert isinstance(instance, uml_WriteLinkAction)

@given(instance=uml_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml_readlinkaction_instantiation(instance):
    assert isinstance(instance, uml_ReadLinkAction)

@given(instance=uml_LinkAction_strategy)
@settings(max_examples=50)
def test_uml_linkaction_instantiation(instance):
    assert isinstance(instance, uml_LinkAction)

@given(instance=uml_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_AddStructuralFeatureValueAction)



@given(instance=uml_AddStructuralFeatureValueAction_strategy)
def test_uml_addstructuralfeaturevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=TemplateSignature_strategy)
@settings(max_examples=50)
def test_templatesignature_instantiation(instance):
    assert isinstance(instance, TemplateSignature)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=uml_ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_ConnectableElementTemplateParameter)

@given(instance=uml_ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_ClassifierTemplateParameter)



@given(instance=uml_ClassifierTemplateParameter_strategy)
def test_uml_classifiertemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=uml_OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_OperationTemplateParameter)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=uml_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml_communicationpath_instantiation(instance):
    assert isinstance(instance, uml_CommunicationPath)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=uml_Model_strategy)
@settings(max_examples=50)
def test_uml_model_instantiation(instance):
    assert isinstance(instance, uml_Model)



@given(instance=uml_Model_strategy)
def test_uml_model_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original

@given(instance=uml_Profile_strategy)
@settings(max_examples=50)
def test_uml_profile_instantiation(instance):
    assert isinstance(instance, uml_Profile)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=uml_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, uml_EncapsulatedClassifier)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=uml_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml_extensionend_instantiation(instance):
    assert isinstance(instance, uml_ExtensionEnd)

@given(instance=uml_Port_strategy)
@settings(max_examples=50)
def test_uml_port_instantiation(instance):
    assert isinstance(instance, uml_Port)



@given(instance=uml_Port_strategy)
def test_uml_port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original



@given(instance=uml_Port_strategy)
def test_uml_port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original

@given(instance=uml_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml_connectionpointreference_instantiation(instance):
    assert isinstance(instance, uml_ConnectionPointReference)

@given(instance=uml_Pseudostate_strategy)
@settings(max_examples=50)
def test_uml_pseudostate_instantiation(instance):
    assert isinstance(instance, uml_Pseudostate)



@given(instance=uml_Pseudostate_strategy)
def test_uml_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=uml_Activity_strategy)
@settings(max_examples=50)
def test_uml_activity_instantiation(instance):
    assert isinstance(instance, uml_Activity)



@given(instance=uml_Activity_strategy)
def test_uml_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=uml_Activity_strategy)
def test_uml_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=uml_OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_uml_opaquebehavior_instantiation(instance):
    assert isinstance(instance, uml_OpaqueBehavior)



@given(instance=uml_OpaqueBehavior_strategy)
def test_uml_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=uml_OpaqueBehavior_strategy)
def test_uml_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml_Interaction_strategy)
@settings(max_examples=50)
def test_uml_interaction_instantiation(instance):
    assert isinstance(instance, uml_Interaction)

@given(instance=uml_StateMachine_strategy)
@settings(max_examples=50)
def test_uml_statemachine_instantiation(instance):
    assert isinstance(instance, uml_StateMachine)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=uml_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, uml_ProtocolStateMachine)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=uml_Component_strategy)
@settings(max_examples=50)
def test_uml_component_instantiation(instance):
    assert isinstance(instance, uml_Component)



@given(instance=uml_Component_strategy)
def test_uml_component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original

@given(instance=uml_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml_associationclass_instantiation(instance):
    assert isinstance(instance, uml_AssociationClass)

@given(instance=uml_Stereotype_strategy)
@settings(max_examples=50)
def test_uml_stereotype_instantiation(instance):
    assert isinstance(instance, uml_Stereotype)

@given(instance=uml_Extension_strategy)
@settings(max_examples=50)
def test_uml_extension_instantiation(instance):
    assert isinstance(instance, uml_Extension)



@given(instance=uml_Extension_strategy)
def test_uml_extension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=uml_Collaboration_strategy)
@settings(max_examples=50)
def test_uml_collaboration_instantiation(instance):
    assert isinstance(instance, uml_Collaboration)

@given(instance=uml_Actor_strategy)
@settings(max_examples=50)
def test_uml_actor_instantiation(instance):
    assert isinstance(instance, uml_Actor)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=uml_Reception_strategy)
@settings(max_examples=50)
def test_uml_reception_instantiation(instance):
    assert isinstance(instance, uml_Reception)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=uml_Connector_strategy)
@settings(max_examples=50)
def test_uml_connector_instantiation(instance):
    assert isinstance(instance, uml_Connector)



@given(instance=uml_Connector_strategy)
def test_uml_connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=uml_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml_deploymentspecification_instantiation(instance):
    assert isinstance(instance, uml_DeploymentSpecification)



@given(instance=uml_DeploymentSpecification_strategy)
def test_uml_deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original



@given(instance=uml_DeploymentSpecification_strategy)
def test_uml_deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original

@given(instance=uml_Class_strategy)
@settings(max_examples=50)
def test_uml_class_instantiation(instance):
    assert isinstance(instance, uml_Class)



@given(instance=uml_Class_strategy)
def test_uml_class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=uml_Node_strategy)
@settings(max_examples=50)
def test_uml_node_instantiation(instance):
    assert isinstance(instance, uml_Node)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=uml_InterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml_interfacerealization_instantiation(instance):
    assert isinstance(instance, uml_InterfaceRealization)

@given(instance=uml_ComponentRealization_strategy)
@settings(max_examples=50)
def test_uml_componentrealization_instantiation(instance):
    assert isinstance(instance, uml_ComponentRealization)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=uml_Pin_strategy)
@settings(max_examples=50)
def test_uml_pin_instantiation(instance):
    assert isinstance(instance, uml_Pin)



@given(instance=uml_Pin_strategy)
def test_uml_pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=uml_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml_connectorend_instantiation(instance):
    assert isinstance(instance, uml_ConnectorEnd)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=uml_Variable_strategy)
@settings(max_examples=50)
def test_uml_variable_instantiation(instance):
    assert isinstance(instance, uml_Variable)

@given(instance=uml_Behavior_strategy)
@settings(max_examples=50)
def test_uml_behavior_instantiation(instance):
    assert isinstance(instance, uml_Behavior)



@given(instance=uml_Behavior_strategy)
def test_uml_behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=uml_Parameter_strategy)
@settings(max_examples=50)
def test_uml_parameter_instantiation(instance):
    assert isinstance(instance, uml_Parameter)



@given(instance=uml_Parameter_strategy)
def test_uml_parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original



@given(instance=uml_Parameter_strategy)
def test_uml_parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original



@given(instance=uml_Parameter_strategy)
def test_uml_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=uml_Parameter_strategy)
def test_uml_parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=uml_Parameter_strategy)
def test_uml_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=uml_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml_literalspecification_instantiation(instance):
    assert isinstance(instance, uml_LiteralSpecification)

@given(instance=uml_Interval_strategy)
@settings(max_examples=50)
def test_uml_interval_instantiation(instance):
    assert isinstance(instance, uml_Interval)

@given(instance=uml_TimeExpression_strategy)
@settings(max_examples=50)
def test_uml_timeexpression_instantiation(instance):
    assert isinstance(instance, uml_TimeExpression)

@given(instance=uml_InstanceValue_strategy)
@settings(max_examples=50)
def test_uml_instancevalue_instantiation(instance):
    assert isinstance(instance, uml_InstanceValue)

@given(instance=uml_Expression_strategy)
@settings(max_examples=50)
def test_uml_expression_instantiation(instance):
    assert isinstance(instance, uml_Expression)



@given(instance=uml_Expression_strategy)
def test_uml_expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=uml_Duration_strategy)
@settings(max_examples=50)
def test_uml_duration_instantiation(instance):
    assert isinstance(instance, uml_Duration)

@given(instance=uml_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml_opaqueexpression_instantiation(instance):
    assert isinstance(instance, uml_OpaqueExpression)



@given(instance=uml_OpaqueExpression_strategy)
def test_uml_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=uml_OpaqueExpression_strategy)
def test_uml_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=uml_Usage_strategy)
@settings(max_examples=50)
def test_uml_usage_instantiation(instance):
    assert isinstance(instance, uml_Usage)

@given(instance=uml_Deployment_strategy)
@settings(max_examples=50)
def test_uml_deployment_instantiation(instance):
    assert isinstance(instance, uml_Deployment)

@given(instance=uml_Abstraction_strategy)
@settings(max_examples=50)
def test_uml_abstraction_instantiation(instance):
    assert isinstance(instance, uml_Abstraction)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=uml_Manifestation_strategy)
@settings(max_examples=50)
def test_uml_manifestation_instantiation(instance):
    assert isinstance(instance, uml_Manifestation)

@given(instance=uml_Realization_strategy)
@settings(max_examples=50)
def test_uml_realization_instantiation(instance):
    assert isinstance(instance, uml_Realization)

@given(instance=uml_UseCase_strategy)
@settings(max_examples=50)
def test_uml_usecase_instantiation(instance):
    assert isinstance(instance, uml_UseCase)

@given(instance=uml_Substitution_strategy)
@settings(max_examples=50)
def test_uml_substitution_instantiation(instance):
    assert isinstance(instance, uml_Substitution)

@given(instance=uml_Property_strategy)
@settings(max_examples=50)
def test_uml_property_instantiation(instance):
    assert isinstance(instance, uml_Property)



@given(instance=uml_Property_strategy)
def test_uml_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=uml_Property_strategy)
def test_uml_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=uml_Property_strategy)
def test_uml_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=uml_Property_strategy)
def test_uml_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=uml_Property_strategy)
def test_uml_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml_InformationItem_strategy)
@settings(max_examples=50)
def test_uml_informationitem_instantiation(instance):
    assert isinstance(instance, uml_InformationItem)

@given(instance=uml_Signal_strategy)
@settings(max_examples=50)
def test_uml_signal_instantiation(instance):
    assert isinstance(instance, uml_Signal)

@given(instance=uml_Interface_strategy)
@settings(max_examples=50)
def test_uml_interface_instantiation(instance):
    assert isinstance(instance, uml_Interface)

@given(instance=uml_Artifact_strategy)
@settings(max_examples=50)
def test_uml_artifact_instantiation(instance):
    assert isinstance(instance, uml_Artifact)



@given(instance=uml_Artifact_strategy)
def test_uml_artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=uml_DataType_strategy)
@settings(max_examples=50)
def test_uml_datatype_instantiation(instance):
    assert isinstance(instance, uml_DataType)

@given(instance=uml_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml_structuredclassifier_instantiation(instance):
    assert isinstance(instance, uml_StructuredClassifier)

@given(instance=uml_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml_BehavioredClassifier)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=uml_ObjectNode_strategy)
@settings(max_examples=50)
def test_uml_objectnode_instantiation(instance):
    assert isinstance(instance, uml_ObjectNode)



@given(instance=uml_ObjectNode_strategy)
def test_uml_objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=uml_ObjectNode_strategy)
def test_uml_objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=uml_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml_structuralfeature_instantiation(instance):
    assert isinstance(instance, uml_StructuralFeature)



@given(instance=uml_StructuralFeature_strategy)
def test_uml_structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=uml_Feature_strategy)
@settings(max_examples=50)
def test_uml_feature_instantiation(instance):
    assert isinstance(instance, uml_Feature)



@given(instance=uml_Feature_strategy)
def test_uml_feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=uml_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml_extensionpoint_instantiation(instance):
    assert isinstance(instance, uml_ExtensionPoint)

@given(instance=uml_ActivityNode_strategy)
@settings(max_examples=50)
def test_uml_activitynode_instantiation(instance):
    assert isinstance(instance, uml_ActivityNode)

@given(instance=uml_RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml_redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, uml_RedefinableTemplateSignature)

@given(instance=uml_ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml_activityedge_instantiation(instance):
    assert isinstance(instance, uml_ActivityEdge)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=uml_ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml_connectableelement_instantiation(instance):
    assert isinstance(instance, uml_ConnectableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml_GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml_generalordering_instantiation(instance):
    assert isinstance(instance, uml_GeneralOrdering)

@given(instance=uml_CollaborationUse_strategy)
@settings(max_examples=50)
def test_uml_collaborationuse_instantiation(instance):
    assert isinstance(instance, uml_CollaborationUse)

@given(instance=uml_MessageEnd_strategy)
@settings(max_examples=50)
def test_uml_messageend_instantiation(instance):
    assert isinstance(instance, uml_MessageEnd)

@given(instance=uml_Message_strategy)
@settings(max_examples=50)
def test_uml_message_instantiation(instance):
    assert isinstance(instance, uml_Message)



@given(instance=uml_Message_strategy)
def test_uml_message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original



@given(instance=uml_Message_strategy)
def test_uml_message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original

@given(instance=uml_ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml_activitypartition_instantiation(instance):
    assert isinstance(instance, uml_ActivityPartition)



@given(instance=uml_ActivityPartition_strategy)
def test_uml_activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original



@given(instance=uml_ActivityPartition_strategy)
def test_uml_activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=uml_Lifeline_strategy)
@settings(max_examples=50)
def test_uml_lifeline_instantiation(instance):
    assert isinstance(instance, uml_Lifeline)

@given(instance=uml_Trigger_strategy)
@settings(max_examples=50)
def test_uml_trigger_instantiation(instance):
    assert isinstance(instance, uml_Trigger)

@given(instance=uml_TypedElement_strategy)
@settings(max_examples=50)
def test_uml_typedelement_instantiation(instance):
    assert isinstance(instance, uml_TypedElement)

@given(instance=uml_Vertex_strategy)
@settings(max_examples=50)
def test_uml_vertex_instantiation(instance):
    assert isinstance(instance, uml_Vertex)

@given(instance=uml_ParameterSet_strategy)
@settings(max_examples=50)
def test_uml_parameterset_instantiation(instance):
    assert isinstance(instance, uml_ParameterSet)

@given(instance=uml_DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml_deploymenttarget_instantiation(instance):
    assert isinstance(instance, uml_DeploymentTarget)

@given(instance=uml_Namespace_strategy)
@settings(max_examples=50)
def test_uml_namespace_instantiation(instance):
    assert isinstance(instance, uml_Namespace)

@given(instance=uml_InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml_interactionfragment_instantiation(instance):
    assert isinstance(instance, uml_InteractionFragment)

@given(instance=uml_DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml_deployedartifact_instantiation(instance):
    assert isinstance(instance, uml_DeployedArtifact)

@given(instance=uml_RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml_redefinableelement_instantiation(instance):
    assert isinstance(instance, uml_RedefinableElement)



@given(instance=uml_RedefinableElement_strategy)
def test_uml_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=uml_PackageableElement_strategy)
@settings(max_examples=50)
def test_uml_packageableelement_instantiation(instance):
    assert isinstance(instance, uml_PackageableElement)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=uml_Operation_strategy)
@settings(max_examples=50)
def test_uml_operation_instantiation(instance):
    assert isinstance(instance, uml_Operation)



@given(instance=uml_Operation_strategy)
def test_uml_operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=uml_Operation_strategy)
def test_uml_operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=uml_Operation_strategy)
def test_uml_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original



@given(instance=uml_Operation_strategy)
def test_uml_operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=uml_Operation_strategy)
def test_uml_operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uml_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml_generalizationset_instantiation(instance):
    assert isinstance(instance, uml_GeneralizationSet)



@given(instance=uml_GeneralizationSet_strategy)
def test_uml_generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original



@given(instance=uml_GeneralizationSet_strategy)
def test_uml_generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=uml_Constraint_strategy)
@settings(max_examples=50)
def test_uml_constraint_instantiation(instance):
    assert isinstance(instance, uml_Constraint)

@given(instance=uml_Event_strategy)
@settings(max_examples=50)
def test_uml_event_instantiation(instance):
    assert isinstance(instance, uml_Event)

@given(instance=uml_ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml_valuespecification_instantiation(instance):
    assert isinstance(instance, uml_ValueSpecification)

@given(instance=uml_Type_strategy)
@settings(max_examples=50)
def test_uml_type_instantiation(instance):
    assert isinstance(instance, uml_Type)

@given(instance=uml_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml_instancespecification_instantiation(instance):
    assert isinstance(instance, uml_InstanceSpecification)

@given(instance=uml_Observation_strategy)
@settings(max_examples=50)
def test_uml_observation_instantiation(instance):
    assert isinstance(instance, uml_Observation)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=uml_InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml_interactionoperand_instantiation(instance):
    assert isinstance(instance, uml_InteractionOperand)

@given(instance=uml_Transition_strategy)
@settings(max_examples=50)
def test_uml_transition_instantiation(instance):
    assert isinstance(instance, uml_Transition)



@given(instance=uml_Transition_strategy)
def test_uml_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uml_Region_strategy)
@settings(max_examples=50)
def test_uml_region_instantiation(instance):
    assert isinstance(instance, uml_Region)

@given(instance=uml_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml_StructuredActivityNode)



@given(instance=uml_StructuredActivityNode_strategy)
def test_uml_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=uml_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml_behavioralfeature_instantiation(instance):
    assert isinstance(instance, uml_BehavioralFeature)



@given(instance=uml_BehavioralFeature_strategy)
def test_uml_behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=uml_BehavioralFeature_strategy)
def test_uml_behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=uml_State_strategy)
@settings(max_examples=50)
def test_uml_state_instantiation(instance):
    assert isinstance(instance, uml_State)



@given(instance=uml_State_strategy)
def test_uml_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=uml_State_strategy)
def test_uml_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=uml_State_strategy)
def test_uml_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original



@given(instance=uml_State_strategy)
def test_uml_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=uml_Classifier_strategy)
@settings(max_examples=50)
def test_uml_classifier_instantiation(instance):
    assert isinstance(instance, uml_Classifier)



@given(instance=uml_Classifier_strategy)
def test_uml_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml_Package_strategy)
@settings(max_examples=50)
def test_uml_package_instantiation(instance):
    assert isinstance(instance, uml_Package)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=uml_Association_strategy)
@settings(max_examples=50)
def test_uml_association_instantiation(instance):
    assert isinstance(instance, uml_Association)



@given(instance=uml_Association_strategy)
def test_uml_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml_directedrelationship_instantiation(instance):
    assert isinstance(instance, uml_DirectedRelationship)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=uml_Generalization_strategy)
@settings(max_examples=50)
def test_uml_generalization_instantiation(instance):
    assert isinstance(instance, uml_Generalization)



@given(instance=uml_Generalization_strategy)
def test_uml_generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=uml_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml_protocolconformance_instantiation(instance):
    assert isinstance(instance, uml_ProtocolConformance)

@given(instance=uml_PackageImport_strategy)
@settings(max_examples=50)
def test_uml_packageimport_instantiation(instance):
    assert isinstance(instance, uml_PackageImport)



@given(instance=uml_PackageImport_strategy)
def test_uml_packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml_InformationFlow_strategy)
@settings(max_examples=50)
def test_uml_informationflow_instantiation(instance):
    assert isinstance(instance, uml_InformationFlow)

@given(instance=uml_TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml_templatebinding_instantiation(instance):
    assert isinstance(instance, uml_TemplateBinding)

@given(instance=uml_ElementImport_strategy)
@settings(max_examples=50)
def test_uml_elementimport_instantiation(instance):
    assert isinstance(instance, uml_ElementImport)



@given(instance=uml_ElementImport_strategy)
def test_uml_elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=uml_ElementImport_strategy)
def test_uml_elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml_Extend_strategy)
@settings(max_examples=50)
def test_uml_extend_instantiation(instance):
    assert isinstance(instance, uml_Extend)

@given(instance=uml_PackageMerge_strategy)
@settings(max_examples=50)
def test_uml_packagemerge_instantiation(instance):
    assert isinstance(instance, uml_PackageMerge)

@given(instance=uml_ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml_profileapplication_instantiation(instance):
    assert isinstance(instance, uml_ProfileApplication)



@given(instance=uml_ProfileApplication_strategy)
def test_uml_profileapplication_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=uml_Include_strategy)
@settings(max_examples=50)
def test_uml_include_instantiation(instance):
    assert isinstance(instance, uml_Include)

@given(instance=uml_Dependency_strategy)
@settings(max_examples=50)
def test_uml_dependency_instantiation(instance):
    assert isinstance(instance, uml_Dependency)

@given(instance=uml_StringExpression_strategy)
@settings(max_examples=50)
def test_uml_stringexpression_instantiation(instance):
    assert isinstance(instance, uml_StringExpression)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uml_TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml_templatesignature_instantiation(instance):
    assert isinstance(instance, uml_TemplateSignature)

@given(instance=uml_Image_strategy)
@settings(max_examples=50)
def test_uml_image_instantiation(instance):
    assert isinstance(instance, uml_Image)



@given(instance=uml_Image_strategy)
def test_uml_image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=uml_Image_strategy)
def test_uml_image_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=uml_Image_strategy)
def test_uml_image_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=uml_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml_TemplateParameterSubstitution)

@given(instance=uml_ParameterableElement_strategy)
@settings(max_examples=50)
def test_uml_parameterableelement_instantiation(instance):
    assert isinstance(instance, uml_ParameterableElement)

@given(instance=uml_TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_templateparameter_instantiation(instance):
    assert isinstance(instance, uml_TemplateParameter)

@given(instance=uml_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml_multiplicityelement_instantiation(instance):
    assert isinstance(instance, uml_MultiplicityElement)



@given(instance=uml_MultiplicityElement_strategy)
def test_uml_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=uml_MultiplicityElement_strategy)
def test_uml_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=uml_MultiplicityElement_strategy)
def test_uml_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=uml_MultiplicityElement_strategy)
def test_uml_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml_TemplateableElement_strategy)
@settings(max_examples=50)
def test_uml_templateableelement_instantiation(instance):
    assert isinstance(instance, uml_TemplateableElement)

@given(instance=uml_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml_exceptionhandler_instantiation(instance):
    assert isinstance(instance, uml_ExceptionHandler)

@given(instance=uml_Clause_strategy)
@settings(max_examples=50)
def test_uml_clause_instantiation(instance):
    assert isinstance(instance, uml_Clause)

@given(instance=uml_Relationship_strategy)
@settings(max_examples=50)
def test_uml_relationship_instantiation(instance):
    assert isinstance(instance, uml_Relationship)

@given(instance=uml_NamedElement_strategy)
@settings(max_examples=50)
def test_uml_namedelement_instantiation(instance):
    assert isinstance(instance, uml_NamedElement)



@given(instance=uml_NamedElement_strategy)
def test_uml_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=uml_NamedElement_strategy)
def test_uml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=uml_NamedElement_strategy)
def test_uml_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=uml_ActivityGroup_strategy)
@settings(max_examples=50)
def test_uml_activitygroup_instantiation(instance):
    assert isinstance(instance, uml_ActivityGroup)

@given(instance=uml_QualifierValue_strategy)
@settings(max_examples=50)
def test_uml_qualifiervalue_instantiation(instance):
    assert isinstance(instance, uml_QualifierValue)

@given(instance=uml_Slot_strategy)
@settings(max_examples=50)
def test_uml_slot_instantiation(instance):
    assert isinstance(instance, uml_Slot)

@given(instance=uml_LinkEndData_strategy)
@settings(max_examples=50)
def test_uml_linkenddata_instantiation(instance):
    assert isinstance(instance, uml_LinkEndData)

@given(instance=uml_Comment_strategy)
@settings(max_examples=50)
def test_uml_comment_instantiation(instance):
    assert isinstance(instance, uml_Comment)



@given(instance=uml_Comment_strategy)
def test_uml_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=uml_Element_strategy)
@settings(max_examples=50)
def test_uml_element_instantiation(instance):
    assert isinstance(instance, uml_Element)

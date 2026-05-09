import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    InteractionUse,
    MessageEnd,
    CombinedFragment,
    CompleteDSLPckg::ConsiderIgnoreFragment,
    CompleteDSLPckg::CombinedFragment,
    CompleteDSLPckg::PartDecomposition,
    ExecutionSpecification,
    CompleteDSLPckg::ActionExecutionSpecification,
    CompleteDSLPckg::BehaviorExecutionSpecification,
    MessageOccurrenceSpecification,
    CompleteDSLPckg::DestructionOccurrenceSpecification,
    OccurenceSpecification,
    CompleteDSLPckg::MessageOccurrenceSpecification,
    CompleteDSLPckg::ExecutionOccurrenceSpecification,
    InteractionFragment,
    CompleteDSLPckg::Continuation,
    CompleteDSLPckg::InteractionUse,
    CompleteDSLPckg::OccurenceSpecification,
    CompleteDSLPckg::StateInvariant,
    CompleteDSLPckg::ExecutionSpecification,
    CompleteDSLPckg::Gate,
    ExecutableNode,
    CentralBufferNode,
    CompleteDSLPckg::DataStoreNode,
    StructuredActivityNode,
    CompleteDSLPckg::ExpansionRegion,
    CompleteDSLPckg::ConditionalNode,
    CompleteDSLPckg::SequenceNode,
    CompleteDSLPckg::LoopNode,
    ActivityEdge,
    CompleteDSLPckg::ObjectFlow,
    CompleteDSLPckg::ControlFlow,
    ActivityGroup,
    FinalNode,
    CompleteDSLPckg::FlowFinalNode,
    ControlNode,
    CompleteDSLPckg::FinalNode,
    CompleteDSLPckg::MergeNode,
    CompleteDSLPckg::DecisionNode,
    CompleteDSLPckg::InitialNode,
    CompleteDSLPckg::JoinNode,
    CompleteDSLPckg::ForkNode,
    CompleteDSLPckg::ActivityFinalNode,
    ObjectNode,
    CompleteDSLPckg::CentralBufferNode,
    CompleteDSLPckg::ExpansionNode,
    CompleteDSLPckg::ActivityParameterNode,
    ActivityNode,
    CompleteDSLPckg::ControlNode,
    CompleteDSLPckg::ExecutableNode,
    CompleteDSLPckg::ActivityPartition,
    Transition,
    CompleteDSLPckg::ProtocolTransition,
    CompleteDSLPckg::InterruptibleActivityRegion,
    StateMachine,
    CompleteDSLPckg::ProtocolStateMachine,
    State,
    CompleteDSLPckg::FinalState,
    Vertex,
    CompleteDSLPckg::ConnectionPointReference,
    WriteVariableAction,
    CompleteDSLPckg::RemoveVariableValueAction,
    CompleteDSLPckg::AddVariableValueAction,
    VariableAction,
    CompleteDSLPckg::ClearVariableAction,
    CompleteDSLPckg::WriteVariableAction,
    CompleteDSLPckg::ReadVariableAction,
    CompleteDSLPckg::Pseudostate,
    CreateLinkAction,
    CompleteDSLPckg::CreateLinkObjectAction,
    CompleteDSLPckg::ReadlsClassifiedObjectAction,
    CompleteDSLPckg::InstanceValue,
    LiteralSpecification,
    CompleteDSLPckg::LiteralUnilimitedNatural,
    CompleteDSLPckg::LiteralInteger,
    CompleteDSLPckg::LiteralString,
    CompleteDSLPckg::LiteralBoolean,
    CompleteDSLPckg::LiteralReal,
    CompleteDSLPckg::LiteralNull,
    ValueSpecification,
    CompleteDSLPckg::LiteralSpecification,
    CompleteDSLPckg::OpaqueExpression,
    CompleteDSLPckg::Expression,
    TypedElement,
    CompleteDSLPckg::Parameter,
    CompleteDSLPckg::ObjectNode,
    Relationship,
    CompleteDSLPckg::DirectedRelationship,
    PackageableElement,
    CompleteDSLPckg::ValueSpecification,
    CompleteDSLPckg::Type,
    CompleteDSLPckg::InstanceSpecification,
    Namespace,
    CompleteDSLPckg::InteractionOperand,
    CompleteDSLPckg::Package,
    DirectedRelationship,
    CompleteDSLPckg::ProtocolConformance,
    CompleteDSLPckg::PackageMerge,
    CompleteDSLPckg::Constraint,
    CompleteDSLPckg::PackageImport,
    CompleteDSLPckg::ElementImport,
    CompleteDSLPckg::Dependency,
    Element,
    CompleteDSLPckg::Clause,
    CompleteDSLPckg::Relationship,
    CompleteDSLPckg::MultiplicityElement,
    CompleteDSLPckg::Slot,
    CompleteDSLPckg::ExceptionHandler,
    CompleteDSLPckg::NamedElement,
    CompleteDSLPckg::Comment,
    CompleteDSLPckg::Element,
    NamedElement,
    CompleteDSLPckg::Lifeline,
    CompleteDSLPckg::Include,
    CompleteDSLPckg::GeneralOrdering,
    CompleteDSLPckg::Namespace,
    CompleteDSLPckg::ActivityGroup,
    CompleteDSLPckg::TypedElement,
    CompleteDSLPckg::Message,
    CompleteDSLPckg::ParameterSet,
    CompleteDSLPckg::RedefinableElement,
    CompleteDSLPckg::InteractionFragment,
    CompleteDSLPckg::Vertex,
    CompleteDSLPckg::MessageEnd,
    CompleteDSLPckg::PackageableElement,
    CompleteDSLPckg::Extend,
    AcceptEventAction,
    CompleteDSLPckg::AcceptCallAction,
    LinkAction,
    CompleteDSLPckg::WriteLinkAction,
    CompleteDSLPckg::ReadLinkAction,
    CompleteDSLPckg::QualifierValue,
    CompleteDSLPckg::LinkEndData,
    WriteStructuralFeatureAction,
    CompleteDSLPckg::RemoveStructuralFeatureValueAction,
    CompleteDSLPckg::AddStructuralFeatureValueAction,
    LinkEndData,
    CompleteDSLPckg::LinkEndDestructionData,
    CompleteDSLPckg::LinkEndCreationData,
    WriteLinkAction,
    CompleteDSLPckg::DestroyLinkAction,
    CompleteDSLPckg::CreateLinkAction,
    StructuralFeatureAction,
    CompleteDSLPckg::WriteStructuralFeatureAction,
    CompleteDSLPckg::ClearStructuralFeatureAction,
    CompleteDSLPckg::ReadStructuralFeatureAction,
    CompleteDSLPckg::CallOperationAction,
    CallAction,
    CompleteDSLPckg::StartObjectBehaviorAction,
    CompleteDSLPckg::CallBehaviorAction,
    InvocationAction,
    CompleteDSLPckg::BroadcastSignalAction,
    CompleteDSLPckg::SendSignalAction,
    CompleteDSLPckg::CallAction,
    InputPin,
    CompleteDSLPckg::ActionInputPin,
    CompleteDSLPckg::ValuePin,
    Pin,
    Action,
    CompleteDSLPckg::TestIdentityAction,
    CompleteDSLPckg::ReadSelfAction,
    CompleteDSLPckg::UnmarshallAction,
    CompleteDSLPckg::ReadLinkObjectEndQualifierAction,
    CompleteDSLPckg::CreateObjectAction,
    CompleteDSLPckg::ReadLinkObjectEndAction,
    CompleteDSLPckg::LinkAction,
    CompleteDSLPckg::ReplyAction,
    CompleteDSLPckg::VariableAction,
    CompleteDSLPckg::ValueSpecificationAction,
    CompleteDSLPckg::DestroyObjectAction,
    CompleteDSLPckg::StartClassifierBehaviorAction,
    CompleteDSLPckg::ReadExtendAction,
    CompleteDSLPckg::AcceptEventAction,
    CompleteDSLPckg::StructuredActivityNode,
    CompleteDSLPckg::RaiseExceptionAction,
    CompleteDSLPckg::ReduceAction,
    CompleteDSLPckg::ReclassifyObjectAction,
    CompleteDSLPckg::StructuralFeatureAction,
    CompleteDSLPckg::OpaqueAction,
    CompleteDSLPckg::SendObjectAction,
    CompleteDSLPckg::InputPin,
    CompleteDSLPckg::Action,
    Artifact,
    CompleteDSLPckg::DeploymentSpecification,
    CompleteDSLPckg::DeployedArtifact,
    CompleteDSLPckg::DeploymentTarget,
    Node,
    CompleteDSLPckg::ExecutionEnvironment,
    CompleteDSLPckg::Device,
    CompleteDSLPckg::OutputPin,
    DeployedArtifact,
    CompleteDSLPckg::InvocationAction,
    CompleteDSLPckg::ConnectableElement,
    CompleteDSLPckg::ConnectorEnd,
    Property,
    CompleteDSLPckg::Port,
    IntervalConstraint,
    CompleteDSLPckg::DurationConstraint,
    CompleteDSLPckg::TimeConstraint,
    Constraint,
    CompleteDSLPckg::InteractionConstraint,
    CompleteDSLPckg::IntervalConstraint,
    Interval,
    CompleteDSLPckg::DurationInterval,
    CompleteDSLPckg::TimeInterval,
    CompleteDSLPckg::Duration,
    Observation,
    CompleteDSLPckg::DurationObservation,
    CompleteDSLPckg::TimeObservation,
    CompleteDSLPckg::Observation,
    CompleteDSLPckg::TimeExpression,
    CompleteDSLPckg::TimeEvent,
    MessageEvent,
    CompleteDSLPckg::CallEvent,
    CompleteDSLPckg::SignalEvent,
    CompleteDSLPckg::AnyReceiveEvent,
    Event,
    CompleteDSLPckg::ChangeEvent,
    CompleteDSLPckg::MessageEvent,
    CompleteDSLPckg::Interval,
    CompleteDSLPckg::Trigger,
    OpaqueBehavior,
    CompleteDSLPckg::FunctionBehavior,
    Behavior,
    CompleteDSLPckg::StateMachine,
    CompleteDSLPckg::Activity,
    CompleteDSLPckg::Interaction,
    CompleteDSLPckg::OpaqueBehavior,
    CompleteDSLPckg::Event,
    Association,
    CompleteDSLPckg::CommunicationPath,
    Class,
    CompleteDSLPckg::Behavior,
    CompleteDSLPckg::Component,
    CompleteDSLPckg::AssociationClass,
    Realization,
    CompleteDSLPckg::ComponentRealization,
    CompleteDSLPckg::InterfaceRealization,
    Abstraction,
    CompleteDSLPckg::Manifestation,
    CompleteDSLPckg::Realization,
    Dependency,
    CompleteDSLPckg::Deployment,
    CompleteDSLPckg::Abstraction,
    CompleteDSLPckg::Usage,
    InstanceSpecification,
    CompleteDSLPckg::EnumerationLiteral,
    DataType,
    CompleteDSLPckg::Enumeration,
    CompleteDSLPckg::PrimitiveType,
    EncapsulatedClassifier,
    StructuredClassifier,
    CompleteDSLPckg::EncapsulatedClassifier,
    BehavioredClassifier,
    CompleteDSLPckg::UseCase,
    CompleteDSLPckg::Actor,
    CompleteDSLPckg::Collaboration,
    Classifier,
    CompleteDSLPckg::BehavioredClassifier,
    CompleteDSLPckg::StructuredClassifier,
    CompleteDSLPckg::Artifact,
    CompleteDSLPckg::Signal,
    BehavioralFeature,
    CompleteDSLPckg::Reception,
    CompleteDSLPckg::Operation,
    CompleteDSLPckg::Interface,
    CompleteDSLPckg::DataType,
    CompleteDSLPckg::Association,
    CompleteDSLPckg::Class,
    DeploymentTarget,
    CompleteDSLPckg::Node,
    ConnectableElement,
    StructuralFeature,
    MultiplicityElement,
    CompleteDSLPckg::Variable,
    CompleteDSLPckg::Pin,
    Feature,
    CompleteDSLPckg::StructuralFeature,
    CompleteDSLPckg::Connector,
    CompleteDSLPckg::BehavioralFeature,
    CompleteDSLPckg::CollaborationUse,
    CompleteDSLPckg::GeneralizationSet,
    CompleteDSLPckg::Substitution,
    CompleteDSLPckg::Generalization,
    CompleteDSLPckg::Property,
    Type,
    RedefinableElement,
    CompleteDSLPckg::Classifier,
    CompleteDSLPckg::State,
    CompleteDSLPckg::Feature,
    CompleteDSLPckg::ExtensionPoint,
    CompleteDSLPckg::ActivityEdge,
    CompleteDSLPckg::Transition,
    CompleteDSLPckg::Region,
    CompleteDSLPckg::ActivityNode,
    ConnectorKind,
    ObjectNodeOrderingKind,
    ParameterEffectKind,
    ExpansionKind,
    MessageSort,
    VisibilityKind,
    AggregationKind,
    TransitionKind,
    InteractionOperandKind,
    CallConcurrencyFeature,
    MessageKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_completedslpckg::considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ConsiderIgnoreFragment)


def test_completedslpckg::considerignorefragment_constructor_exists():
    assert callable(CompleteDSLPckg::ConsiderIgnoreFragment.__init__)


def test_completedslpckg::considerignorefragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CombinedFragment)


def test_completedslpckg::combinedfragment_constructor_exists():
    assert callable(CompleteDSLPckg::CombinedFragment.__init__)


def test_completedslpckg::combinedfragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_completedslpckg::combinedfragment_has_interactionOperator():
    assert hasattr(CompleteDSLPckg::CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in CompleteDSLPckg::CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::partdecomposition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::PartDecomposition)


def test_completedslpckg::partdecomposition_constructor_exists():
    assert callable(CompleteDSLPckg::PartDecomposition.__init__)


def test_completedslpckg::partdecomposition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActionExecutionSpecification)


def test_completedslpckg::actionexecutionspecification_constructor_exists():
    assert callable(CompleteDSLPckg::ActionExecutionSpecification.__init__)


def test_completedslpckg::actionexecutionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::BehaviorExecutionSpecification)


def test_completedslpckg::behaviorexecutionspecification_constructor_exists():
    assert callable(CompleteDSLPckg::BehaviorExecutionSpecification.__init__)


def test_completedslpckg::behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(MessageOccurrenceSpecification)


def test_messageoccurrencespecification_constructor_exists():
    assert callable(MessageOccurrenceSpecification.__init__)


def test_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::destructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DestructionOccurrenceSpecification)


def test_completedslpckg::destructionoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg::DestructionOccurrenceSpecification.__init__)


def test_completedslpckg::destructionoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_occurencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurenceSpecification)


def test_occurencespecification_constructor_exists():
    assert callable(OccurenceSpecification.__init__)


def test_occurencespecification_constructor_args():
    sig = inspect.signature(OccurenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::MessageOccurrenceSpecification)


def test_completedslpckg::messageoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg::MessageOccurrenceSpecification.__init__)


def test_completedslpckg::messageoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExecutionOccurrenceSpecification)


def test_completedslpckg::executionoccurrencespecification_constructor_exists():
    assert callable(CompleteDSLPckg::ExecutionOccurrenceSpecification.__init__)


def test_completedslpckg::executionoccurrencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::continuation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Continuation)


def test_completedslpckg::continuation_constructor_exists():
    assert callable(CompleteDSLPckg::Continuation.__init__)


def test_completedslpckg::continuation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_completedslpckg::continuation_has_setting():
    assert hasattr(CompleteDSLPckg::Continuation, "setting")
    descriptor = None
    for klass in CompleteDSLPckg::Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::interactionuse_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InteractionUse)


def test_completedslpckg::interactionuse_constructor_exists():
    assert callable(CompleteDSLPckg::InteractionUse.__init__)


def test_completedslpckg::interactionuse_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::occurencespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::OccurenceSpecification)


def test_completedslpckg::occurencespecification_constructor_exists():
    assert callable(CompleteDSLPckg::OccurenceSpecification.__init__)


def test_completedslpckg::occurencespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::OccurenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::stateinvariant_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StateInvariant)


def test_completedslpckg::stateinvariant_constructor_exists():
    assert callable(CompleteDSLPckg::StateInvariant.__init__)


def test_completedslpckg::stateinvariant_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::executionspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExecutionSpecification)


def test_completedslpckg::executionspecification_constructor_exists():
    assert callable(CompleteDSLPckg::ExecutionSpecification.__init__)


def test_completedslpckg::executionspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::gate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Gate)


def test_completedslpckg::gate_constructor_exists():
    assert callable(CompleteDSLPckg::Gate.__init__)


def test_completedslpckg::gate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Gate.__init__)
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



def test_completedslpckg::datastorenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DataStoreNode)


def test_completedslpckg::datastorenode_constructor_exists():
    assert callable(CompleteDSLPckg::DataStoreNode.__init__)


def test_completedslpckg::datastorenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::expansionregion_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExpansionRegion)


def test_completedslpckg::expansionregion_constructor_exists():
    assert callable(CompleteDSLPckg::ExpansionRegion.__init__)


def test_completedslpckg::expansionregion_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_completedslpckg::expansionregion_has_mode():
    assert hasattr(CompleteDSLPckg::ExpansionRegion, "mode")
    descriptor = None
    for klass in CompleteDSLPckg::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ConditionalNode)


def test_completedslpckg::conditionalnode_constructor_exists():
    assert callable(CompleteDSLPckg::ConditionalNode.__init__)


def test_completedslpckg::conditionalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssumed" in params, "Missing parameter 'isAssumed'"

def test_completedslpckg::conditionalnode_has_isDeterminate():
    assert hasattr(CompleteDSLPckg::ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in CompleteDSLPckg::ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::conditionalnode_has_isAssumed():
    assert hasattr(CompleteDSLPckg::ConditionalNode, "isAssumed")
    descriptor = None
    for klass in CompleteDSLPckg::ConditionalNode.__mro__:
        if "isAssumed" in klass.__dict__:
            descriptor = klass.__dict__["isAssumed"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::sequencenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::SequenceNode)


def test_completedslpckg::sequencenode_constructor_exists():
    assert callable(CompleteDSLPckg::SequenceNode.__init__)


def test_completedslpckg::sequencenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::loopnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LoopNode)


def test_completedslpckg::loopnode_constructor_exists():
    assert callable(CompleteDSLPckg::LoopNode.__init__)


def test_completedslpckg::loopnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_completedslpckg::loopnode_has_isTestedFirst():
    assert hasattr(CompleteDSLPckg::LoopNode, "isTestedFirst")
    descriptor = None
    for klass in CompleteDSLPckg::LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::objectflow_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ObjectFlow)


def test_completedslpckg::objectflow_constructor_exists():
    assert callable(CompleteDSLPckg::ObjectFlow.__init__)


def test_completedslpckg::objectflow_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"

def test_completedslpckg::objectflow_has_isMultireceive():
    assert hasattr(CompleteDSLPckg::ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in CompleteDSLPckg::ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::objectflow_has_ordering():
    assert hasattr(CompleteDSLPckg::ObjectFlow, "ordering")
    descriptor = None
    for klass in CompleteDSLPckg::ObjectFlow.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::objectflow_has_isMulticast():
    assert hasattr(CompleteDSLPckg::ObjectFlow, "isMulticast")
    descriptor = None
    for klass in CompleteDSLPckg::ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::objectflow_has_isControlType():
    assert hasattr(CompleteDSLPckg::ObjectFlow, "isControlType")
    descriptor = None
    for klass in CompleteDSLPckg::ObjectFlow.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::controlflow_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ControlFlow)


def test_completedslpckg::controlflow_constructor_exists():
    assert callable(CompleteDSLPckg::ControlFlow.__init__)


def test_completedslpckg::controlflow_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::FlowFinalNode)


def test_completedslpckg::flowfinalnode_constructor_exists():
    assert callable(CompleteDSLPckg::FlowFinalNode.__init__)


def test_completedslpckg::flowfinalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::finalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::FinalNode)


def test_completedslpckg::finalnode_constructor_exists():
    assert callable(CompleteDSLPckg::FinalNode.__init__)


def test_completedslpckg::finalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::mergenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::MergeNode)


def test_completedslpckg::mergenode_constructor_exists():
    assert callable(CompleteDSLPckg::MergeNode.__init__)


def test_completedslpckg::mergenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::decisionnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DecisionNode)


def test_completedslpckg::decisionnode_constructor_exists():
    assert callable(CompleteDSLPckg::DecisionNode.__init__)


def test_completedslpckg::decisionnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::initialnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InitialNode)


def test_completedslpckg::initialnode_constructor_exists():
    assert callable(CompleteDSLPckg::InitialNode.__init__)


def test_completedslpckg::initialnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::joinnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::JoinNode)


def test_completedslpckg::joinnode_constructor_exists():
    assert callable(CompleteDSLPckg::JoinNode.__init__)


def test_completedslpckg::joinnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_completedslpckg::joinnode_has_isCombineDuplicate():
    assert hasattr(CompleteDSLPckg::JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in CompleteDSLPckg::JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::forknode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ForkNode)


def test_completedslpckg::forknode_constructor_exists():
    assert callable(CompleteDSLPckg::ForkNode.__init__)


def test_completedslpckg::forknode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActivityFinalNode)


def test_completedslpckg::activityfinalnode_constructor_exists():
    assert callable(CompleteDSLPckg::ActivityFinalNode.__init__)


def test_completedslpckg::activityfinalnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CentralBufferNode)


def test_completedslpckg::centralbuffernode_constructor_exists():
    assert callable(CompleteDSLPckg::CentralBufferNode.__init__)


def test_completedslpckg::centralbuffernode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::expansionnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExpansionNode)


def test_completedslpckg::expansionnode_constructor_exists():
    assert callable(CompleteDSLPckg::ExpansionNode.__init__)


def test_completedslpckg::expansionnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActivityParameterNode)


def test_completedslpckg::activityparameternode_constructor_exists():
    assert callable(CompleteDSLPckg::ActivityParameterNode.__init__)


def test_completedslpckg::activityparameternode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::controlnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ControlNode)


def test_completedslpckg::controlnode_constructor_exists():
    assert callable(CompleteDSLPckg::ControlNode.__init__)


def test_completedslpckg::controlnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::executablenode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExecutableNode)


def test_completedslpckg::executablenode_constructor_exists():
    assert callable(CompleteDSLPckg::ExecutableNode.__init__)


def test_completedslpckg::executablenode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::activitypartition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActivityPartition)


def test_completedslpckg::activitypartition_constructor_exists():
    assert callable(CompleteDSLPckg::ActivityPartition.__init__)


def test_completedslpckg::activitypartition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ProtocolTransition)


def test_completedslpckg::protocoltransition_constructor_exists():
    assert callable(CompleteDSLPckg::ProtocolTransition.__init__)


def test_completedslpckg::protocoltransition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InterruptibleActivityRegion)


def test_completedslpckg::interruptibleactivityregion_constructor_exists():
    assert callable(CompleteDSLPckg::InterruptibleActivityRegion.__init__)


def test_completedslpckg::interruptibleactivityregion_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ProtocolStateMachine)


def test_completedslpckg::protocolstatemachine_constructor_exists():
    assert callable(CompleteDSLPckg::ProtocolStateMachine.__init__)


def test_completedslpckg::protocolstatemachine_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::finalstate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::FinalState)


def test_completedslpckg::finalstate_constructor_exists():
    assert callable(CompleteDSLPckg::FinalState.__init__)


def test_completedslpckg::finalstate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ConnectionPointReference)


def test_completedslpckg::connectionpointreference_constructor_exists():
    assert callable(CompleteDSLPckg::ConnectionPointReference.__init__)


def test_completedslpckg::connectionpointreference_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::RemoveVariableValueAction)


def test_completedslpckg::removevariablevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg::RemoveVariableValueAction.__init__)


def test_completedslpckg::removevariablevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AddVariableValueAction)


def test_completedslpckg::addvariablevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg::AddVariableValueAction.__init__)


def test_completedslpckg::addvariablevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ClearVariableAction)


def test_completedslpckg::clearvariableaction_constructor_exists():
    assert callable(CompleteDSLPckg::ClearVariableAction.__init__)


def test_completedslpckg::clearvariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::WriteVariableAction)


def test_completedslpckg::writevariableaction_constructor_exists():
    assert callable(CompleteDSLPckg::WriteVariableAction.__init__)


def test_completedslpckg::writevariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadVariableAction)


def test_completedslpckg::readvariableaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadVariableAction.__init__)


def test_completedslpckg::readvariableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::pseudostate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Pseudostate)


def test_completedslpckg::pseudostate_constructor_exists():
    assert callable(CompleteDSLPckg::Pseudostate.__init__)


def test_completedslpckg::pseudostate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CreateLinkObjectAction)


def test_completedslpckg::createlinkobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg::CreateLinkObjectAction.__init__)


def test_completedslpckg::createlinkobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readlsclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadlsClassifiedObjectAction)


def test_completedslpckg::readlsclassifiedobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadlsClassifiedObjectAction.__init__)


def test_completedslpckg::readlsclassifiedobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadlsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::instancevalue_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InstanceValue)


def test_completedslpckg::instancevalue_constructor_exists():
    assert callable(CompleteDSLPckg::InstanceValue.__init__)


def test_completedslpckg::instancevalue_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::literalunilimitednatural_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LiteralUnilimitedNatural)


def test_completedslpckg::literalunilimitednatural_constructor_exists():
    assert callable(CompleteDSLPckg::LiteralUnilimitedNatural.__init__)


def test_completedslpckg::literalunilimitednatural_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LiteralUnilimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::literalinteger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LiteralInteger)


def test_completedslpckg::literalinteger_constructor_exists():
    assert callable(CompleteDSLPckg::LiteralInteger.__init__)


def test_completedslpckg::literalinteger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::literalstring_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LiteralString)


def test_completedslpckg::literalstring_constructor_exists():
    assert callable(CompleteDSLPckg::LiteralString.__init__)


def test_completedslpckg::literalstring_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::literalboolean_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LiteralBoolean)


def test_completedslpckg::literalboolean_constructor_exists():
    assert callable(CompleteDSLPckg::LiteralBoolean.__init__)


def test_completedslpckg::literalboolean_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::literalreal_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LiteralReal)


def test_completedslpckg::literalreal_constructor_exists():
    assert callable(CompleteDSLPckg::LiteralReal.__init__)


def test_completedslpckg::literalreal_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::literalnull_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LiteralNull)


def test_completedslpckg::literalnull_constructor_exists():
    assert callable(CompleteDSLPckg::LiteralNull.__init__)


def test_completedslpckg::literalnull_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::literalspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LiteralSpecification)


def test_completedslpckg::literalspecification_constructor_exists():
    assert callable(CompleteDSLPckg::LiteralSpecification.__init__)


def test_completedslpckg::literalspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::OpaqueExpression)


def test_completedslpckg::opaqueexpression_constructor_exists():
    assert callable(CompleteDSLPckg::OpaqueExpression.__init__)


def test_completedslpckg::opaqueexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_completedslpckg::opaqueexpression_has_language():
    assert hasattr(CompleteDSLPckg::OpaqueExpression, "language")
    descriptor = None
    for klass in CompleteDSLPckg::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::opaqueexpression_has_body():
    assert hasattr(CompleteDSLPckg::OpaqueExpression, "body")
    descriptor = None
    for klass in CompleteDSLPckg::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::expression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Expression)


def test_completedslpckg::expression_constructor_exists():
    assert callable(CompleteDSLPckg::Expression.__init__)


def test_completedslpckg::expression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_completedslpckg::expression_has_symbol():
    assert hasattr(CompleteDSLPckg::Expression, "symbol")
    descriptor = None
    for klass in CompleteDSLPckg::Expression.__mro__:
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



def test_completedslpckg::parameter_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Parameter)


def test_completedslpckg::parameter_constructor_exists():
    assert callable(CompleteDSLPckg::Parameter.__init__)


def test_completedslpckg::parameter_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_completedslpckg::parameter_has_default():
    assert hasattr(CompleteDSLPckg::Parameter, "default")
    descriptor = None
    for klass in CompleteDSLPckg::Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::objectnode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ObjectNode)


def test_completedslpckg::objectnode_constructor_exists():
    assert callable(CompleteDSLPckg::ObjectNode.__init__)


def test_completedslpckg::objectnode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DirectedRelationship)


def test_completedslpckg::directedrelationship_constructor_exists():
    assert callable(CompleteDSLPckg::DirectedRelationship.__init__)


def test_completedslpckg::directedrelationship_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::valuespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ValueSpecification)


def test_completedslpckg::valuespecification_constructor_exists():
    assert callable(CompleteDSLPckg::ValueSpecification.__init__)


def test_completedslpckg::valuespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::type_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Type)


def test_completedslpckg::type_constructor_exists():
    assert callable(CompleteDSLPckg::Type.__init__)


def test_completedslpckg::type_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Type.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::instancespecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InstanceSpecification)


def test_completedslpckg::instancespecification_constructor_exists():
    assert callable(CompleteDSLPckg::InstanceSpecification.__init__)


def test_completedslpckg::instancespecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InteractionOperand)


def test_completedslpckg::interactionoperand_constructor_exists():
    assert callable(CompleteDSLPckg::InteractionOperand.__init__)


def test_completedslpckg::interactionoperand_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::package_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Package)


def test_completedslpckg::package_constructor_exists():
    assert callable(CompleteDSLPckg::Package.__init__)


def test_completedslpckg::package_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Package.__init__)
    params = list(sig.parameters.keys())
    assert "URI" in params, "Missing parameter 'URI'"

def test_completedslpckg::package_has_URI():
    assert hasattr(CompleteDSLPckg::Package, "URI")
    descriptor = None
    for klass in CompleteDSLPckg::Package.__mro__:
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



def test_completedslpckg::protocolconformance_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ProtocolConformance)


def test_completedslpckg::protocolconformance_constructor_exists():
    assert callable(CompleteDSLPckg::ProtocolConformance.__init__)


def test_completedslpckg::protocolconformance_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::packagemerge_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::PackageMerge)


def test_completedslpckg::packagemerge_constructor_exists():
    assert callable(CompleteDSLPckg::PackageMerge.__init__)


def test_completedslpckg::packagemerge_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::constraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Constraint)


def test_completedslpckg::constraint_constructor_exists():
    assert callable(CompleteDSLPckg::Constraint.__init__)


def test_completedslpckg::constraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::packageimport_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::PackageImport)


def test_completedslpckg::packageimport_constructor_exists():
    assert callable(CompleteDSLPckg::PackageImport.__init__)


def test_completedslpckg::packageimport_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_completedslpckg::packageimport_has_visibility():
    assert hasattr(CompleteDSLPckg::PackageImport, "visibility")
    descriptor = None
    for klass in CompleteDSLPckg::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::elementimport_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ElementImport)


def test_completedslpckg::elementimport_constructor_exists():
    assert callable(CompleteDSLPckg::ElementImport.__init__)


def test_completedslpckg::elementimport_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_completedslpckg::elementimport_has_alias():
    assert hasattr(CompleteDSLPckg::ElementImport, "alias")
    descriptor = None
    for klass in CompleteDSLPckg::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::elementimport_has_visibility():
    assert hasattr(CompleteDSLPckg::ElementImport, "visibility")
    descriptor = None
    for klass in CompleteDSLPckg::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::dependency_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Dependency)


def test_completedslpckg::dependency_constructor_exists():
    assert callable(CompleteDSLPckg::Dependency.__init__)


def test_completedslpckg::dependency_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::clause_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Clause)


def test_completedslpckg::clause_constructor_exists():
    assert callable(CompleteDSLPckg::Clause.__init__)


def test_completedslpckg::clause_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Clause.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::relationship_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Relationship)


def test_completedslpckg::relationship_constructor_exists():
    assert callable(CompleteDSLPckg::Relationship.__init__)


def test_completedslpckg::relationship_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::MultiplicityElement)


def test_completedslpckg::multiplicityelement_constructor_exists():
    assert callable(CompleteDSLPckg::MultiplicityElement.__init__)


def test_completedslpckg::multiplicityelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_completedslpckg::multiplicityelement_has_isUnique():
    assert hasattr(CompleteDSLPckg::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in CompleteDSLPckg::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::multiplicityelement_has_isOrdered():
    assert hasattr(CompleteDSLPckg::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in CompleteDSLPckg::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::multiplicityelement_has_lower():
    assert hasattr(CompleteDSLPckg::MultiplicityElement, "lower")
    descriptor = None
    for klass in CompleteDSLPckg::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::multiplicityelement_has_upper():
    assert hasattr(CompleteDSLPckg::MultiplicityElement, "upper")
    descriptor = None
    for klass in CompleteDSLPckg::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::slot_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Slot)


def test_completedslpckg::slot_constructor_exists():
    assert callable(CompleteDSLPckg::Slot.__init__)


def test_completedslpckg::slot_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Slot.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExceptionHandler)


def test_completedslpckg::exceptionhandler_constructor_exists():
    assert callable(CompleteDSLPckg::ExceptionHandler.__init__)


def test_completedslpckg::exceptionhandler_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::namedelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::NamedElement)


def test_completedslpckg::namedelement_constructor_exists():
    assert callable(CompleteDSLPckg::NamedElement.__init__)


def test_completedslpckg::namedelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_completedslpckg::namedelement_has_name():
    assert hasattr(CompleteDSLPckg::NamedElement, "name")
    descriptor = None
    for klass in CompleteDSLPckg::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::namedelement_has_qualifiedName():
    assert hasattr(CompleteDSLPckg::NamedElement, "qualifiedName")
    descriptor = None
    for klass in CompleteDSLPckg::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::namedelement_has_visibility():
    assert hasattr(CompleteDSLPckg::NamedElement, "visibility")
    descriptor = None
    for klass in CompleteDSLPckg::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::comment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Comment)


def test_completedslpckg::comment_constructor_exists():
    assert callable(CompleteDSLPckg::Comment.__init__)


def test_completedslpckg::comment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_completedslpckg::comment_has_body():
    assert hasattr(CompleteDSLPckg::Comment, "body")
    descriptor = None
    for klass in CompleteDSLPckg::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::element_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Element)


def test_completedslpckg::element_constructor_exists():
    assert callable(CompleteDSLPckg::Element.__init__)


def test_completedslpckg::element_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Element.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::lifeline_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Lifeline)


def test_completedslpckg::lifeline_constructor_exists():
    assert callable(CompleteDSLPckg::Lifeline.__init__)


def test_completedslpckg::lifeline_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::include_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Include)


def test_completedslpckg::include_constructor_exists():
    assert callable(CompleteDSLPckg::Include.__init__)


def test_completedslpckg::include_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Include.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::generalordering_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::GeneralOrdering)


def test_completedslpckg::generalordering_constructor_exists():
    assert callable(CompleteDSLPckg::GeneralOrdering.__init__)


def test_completedslpckg::generalordering_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::namespace_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Namespace)


def test_completedslpckg::namespace_constructor_exists():
    assert callable(CompleteDSLPckg::Namespace.__init__)


def test_completedslpckg::namespace_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::activitygroup_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActivityGroup)


def test_completedslpckg::activitygroup_constructor_exists():
    assert callable(CompleteDSLPckg::ActivityGroup.__init__)


def test_completedslpckg::activitygroup_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::typedelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::TypedElement)


def test_completedslpckg::typedelement_constructor_exists():
    assert callable(CompleteDSLPckg::TypedElement.__init__)


def test_completedslpckg::typedelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::message_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Message)


def test_completedslpckg::message_constructor_exists():
    assert callable(CompleteDSLPckg::Message.__init__)


def test_completedslpckg::message_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageKind" in params, "Missing parameter 'messageKind'"
    assert "messageSort" in params, "Missing parameter 'messageSort'"

def test_completedslpckg::message_has_messageKind():
    assert hasattr(CompleteDSLPckg::Message, "messageKind")
    descriptor = None
    for klass in CompleteDSLPckg::Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::message_has_messageSort():
    assert hasattr(CompleteDSLPckg::Message, "messageSort")
    descriptor = None
    for klass in CompleteDSLPckg::Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::parameterset_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ParameterSet)


def test_completedslpckg::parameterset_constructor_exists():
    assert callable(CompleteDSLPckg::ParameterSet.__init__)


def test_completedslpckg::parameterset_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::RedefinableElement)


def test_completedslpckg::redefinableelement_constructor_exists():
    assert callable(CompleteDSLPckg::RedefinableElement.__init__)


def test_completedslpckg::redefinableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_completedslpckg::redefinableelement_has_isLeaf():
    assert hasattr(CompleteDSLPckg::RedefinableElement, "isLeaf")
    descriptor = None
    for klass in CompleteDSLPckg::RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InteractionFragment)


def test_completedslpckg::interactionfragment_constructor_exists():
    assert callable(CompleteDSLPckg::InteractionFragment.__init__)


def test_completedslpckg::interactionfragment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::vertex_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Vertex)


def test_completedslpckg::vertex_constructor_exists():
    assert callable(CompleteDSLPckg::Vertex.__init__)


def test_completedslpckg::vertex_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::messageend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::MessageEnd)


def test_completedslpckg::messageend_constructor_exists():
    assert callable(CompleteDSLPckg::MessageEnd.__init__)


def test_completedslpckg::messageend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::packageableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::PackageableElement)


def test_completedslpckg::packageableelement_constructor_exists():
    assert callable(CompleteDSLPckg::PackageableElement.__init__)


def test_completedslpckg::packageableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::extend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Extend)


def test_completedslpckg::extend_constructor_exists():
    assert callable(CompleteDSLPckg::Extend.__init__)


def test_completedslpckg::extend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Extend.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AcceptCallAction)


def test_completedslpckg::acceptcallaction_constructor_exists():
    assert callable(CompleteDSLPckg::AcceptCallAction.__init__)


def test_completedslpckg::acceptcallaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::WriteLinkAction)


def test_completedslpckg::writelinkaction_constructor_exists():
    assert callable(CompleteDSLPckg::WriteLinkAction.__init__)


def test_completedslpckg::writelinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadLinkAction)


def test_completedslpckg::readlinkaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadLinkAction.__init__)


def test_completedslpckg::readlinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::QualifierValue)


def test_completedslpckg::qualifiervalue_constructor_exists():
    assert callable(CompleteDSLPckg::QualifierValue.__init__)


def test_completedslpckg::qualifiervalue_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::linkenddata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LinkEndData)


def test_completedslpckg::linkenddata_constructor_exists():
    assert callable(CompleteDSLPckg::LinkEndData.__init__)


def test_completedslpckg::linkenddata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::RemoveStructuralFeatureValueAction)


def test_completedslpckg::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg::RemoveStructuralFeatureValueAction.__init__)


def test_completedslpckg::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AddStructuralFeatureValueAction)


def test_completedslpckg::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(CompleteDSLPckg::AddStructuralFeatureValueAction.__init__)


def test_completedslpckg::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LinkEndDestructionData)


def test_completedslpckg::linkenddestructiondata_constructor_exists():
    assert callable(CompleteDSLPckg::LinkEndDestructionData.__init__)


def test_completedslpckg::linkenddestructiondata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_completedslpckg::linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(CompleteDSLPckg::LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in CompleteDSLPckg::LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LinkEndCreationData)


def test_completedslpckg::linkendcreationdata_constructor_exists():
    assert callable(CompleteDSLPckg::LinkEndCreationData.__init__)


def test_completedslpckg::linkendcreationdata_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_completedslpckg::linkendcreationdata_has_isReplaceAll():
    assert hasattr(CompleteDSLPckg::LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in CompleteDSLPckg::LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DestroyLinkAction)


def test_completedslpckg::destroylinkaction_constructor_exists():
    assert callable(CompleteDSLPckg::DestroyLinkAction.__init__)


def test_completedslpckg::destroylinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CreateLinkAction)


def test_completedslpckg::createlinkaction_constructor_exists():
    assert callable(CompleteDSLPckg::CreateLinkAction.__init__)


def test_completedslpckg::createlinkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::WriteStructuralFeatureAction)


def test_completedslpckg::writestructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg::WriteStructuralFeatureAction.__init__)


def test_completedslpckg::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ClearStructuralFeatureAction)


def test_completedslpckg::clearstructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg::ClearStructuralFeatureAction.__init__)


def test_completedslpckg::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadStructuralFeatureAction)


def test_completedslpckg::readstructuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadStructuralFeatureAction.__init__)


def test_completedslpckg::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CallOperationAction)


def test_completedslpckg::calloperationaction_constructor_exists():
    assert callable(CompleteDSLPckg::CallOperationAction.__init__)


def test_completedslpckg::calloperationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StartObjectBehaviorAction)


def test_completedslpckg::startobjectbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg::StartObjectBehaviorAction.__init__)


def test_completedslpckg::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CallBehaviorAction)


def test_completedslpckg::callbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg::CallBehaviorAction.__init__)


def test_completedslpckg::callbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::BroadcastSignalAction)


def test_completedslpckg::broadcastsignalaction_constructor_exists():
    assert callable(CompleteDSLPckg::BroadcastSignalAction.__init__)


def test_completedslpckg::broadcastsignalaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::SendSignalAction)


def test_completedslpckg::sendsignalaction_constructor_exists():
    assert callable(CompleteDSLPckg::SendSignalAction.__init__)


def test_completedslpckg::sendsignalaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::callaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CallAction)


def test_completedslpckg::callaction_constructor_exists():
    assert callable(CompleteDSLPckg::CallAction.__init__)


def test_completedslpckg::callaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_completedslpckg::callaction_has_isSynchronous():
    assert hasattr(CompleteDSLPckg::CallAction, "isSynchronous")
    descriptor = None
    for klass in CompleteDSLPckg::CallAction.__mro__:
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



def test_completedslpckg::actioninputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActionInputPin)


def test_completedslpckg::actioninputpin_constructor_exists():
    assert callable(CompleteDSLPckg::ActionInputPin.__init__)


def test_completedslpckg::actioninputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::valuepin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ValuePin)


def test_completedslpckg::valuepin_constructor_exists():
    assert callable(CompleteDSLPckg::ValuePin.__init__)


def test_completedslpckg::valuepin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ValuePin.__init__)
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



def test_completedslpckg::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::TestIdentityAction)


def test_completedslpckg::testidentityaction_constructor_exists():
    assert callable(CompleteDSLPckg::TestIdentityAction.__init__)


def test_completedslpckg::testidentityaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readselfaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadSelfAction)


def test_completedslpckg::readselfaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadSelfAction.__init__)


def test_completedslpckg::readselfaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::UnmarshallAction)


def test_completedslpckg::unmarshallaction_constructor_exists():
    assert callable(CompleteDSLPckg::UnmarshallAction.__init__)


def test_completedslpckg::unmarshallaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadLinkObjectEndQualifierAction)


def test_completedslpckg::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadLinkObjectEndQualifierAction.__init__)


def test_completedslpckg::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CreateObjectAction)


def test_completedslpckg::createobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg::CreateObjectAction.__init__)


def test_completedslpckg::createobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadLinkObjectEndAction)


def test_completedslpckg::readlinkobjectendaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadLinkObjectEndAction.__init__)


def test_completedslpckg::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::linkaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::LinkAction)


def test_completedslpckg::linkaction_constructor_exists():
    assert callable(CompleteDSLPckg::LinkAction.__init__)


def test_completedslpckg::linkaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::replyaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReplyAction)


def test_completedslpckg::replyaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReplyAction.__init__)


def test_completedslpckg::replyaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::variableaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::VariableAction)


def test_completedslpckg::variableaction_constructor_exists():
    assert callable(CompleteDSLPckg::VariableAction.__init__)


def test_completedslpckg::variableaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ValueSpecificationAction)


def test_completedslpckg::valuespecificationaction_constructor_exists():
    assert callable(CompleteDSLPckg::ValueSpecificationAction.__init__)


def test_completedslpckg::valuespecificationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DestroyObjectAction)


def test_completedslpckg::destroyobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg::DestroyObjectAction.__init__)


def test_completedslpckg::destroyobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StartClassifierBehaviorAction)


def test_completedslpckg::startclassifierbehavioraction_constructor_exists():
    assert callable(CompleteDSLPckg::StartClassifierBehaviorAction.__init__)


def test_completedslpckg::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::readextendaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReadExtendAction)


def test_completedslpckg::readextendaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReadExtendAction.__init__)


def test_completedslpckg::readextendaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReadExtendAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AcceptEventAction)


def test_completedslpckg::accepteventaction_constructor_exists():
    assert callable(CompleteDSLPckg::AcceptEventAction.__init__)


def test_completedslpckg::accepteventaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_completedslpckg::accepteventaction_has_isUnmarshall():
    assert hasattr(CompleteDSLPckg::AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in CompleteDSLPckg::AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StructuredActivityNode)


def test_completedslpckg::structuredactivitynode_constructor_exists():
    assert callable(CompleteDSLPckg::StructuredActivityNode.__init__)


def test_completedslpckg::structuredactivitynode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_completedslpckg::structuredactivitynode_has_mustIsolate():
    assert hasattr(CompleteDSLPckg::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in CompleteDSLPckg::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::RaiseExceptionAction)


def test_completedslpckg::raiseexceptionaction_constructor_exists():
    assert callable(CompleteDSLPckg::RaiseExceptionAction.__init__)


def test_completedslpckg::raiseexceptionaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::reduceaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReduceAction)


def test_completedslpckg::reduceaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReduceAction.__init__)


def test_completedslpckg::reduceaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_completedslpckg::reduceaction_has_isOrdered():
    assert hasattr(CompleteDSLPckg::ReduceAction, "isOrdered")
    descriptor = None
    for klass in CompleteDSLPckg::ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ReclassifyObjectAction)


def test_completedslpckg::reclassifyobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg::ReclassifyObjectAction.__init__)


def test_completedslpckg::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_completedslpckg::reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(CompleteDSLPckg::ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in CompleteDSLPckg::ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StructuralFeatureAction)


def test_completedslpckg::structuralfeatureaction_constructor_exists():
    assert callable(CompleteDSLPckg::StructuralFeatureAction.__init__)


def test_completedslpckg::structuralfeatureaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::OpaqueAction)


def test_completedslpckg::opaqueaction_constructor_exists():
    assert callable(CompleteDSLPckg::OpaqueAction.__init__)


def test_completedslpckg::opaqueaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_completedslpckg::opaqueaction_has_body():
    assert hasattr(CompleteDSLPckg::OpaqueAction, "body")
    descriptor = None
    for klass in CompleteDSLPckg::OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::opaqueaction_has_language():
    assert hasattr(CompleteDSLPckg::OpaqueAction, "language")
    descriptor = None
    for klass in CompleteDSLPckg::OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::SendObjectAction)


def test_completedslpckg::sendobjectaction_constructor_exists():
    assert callable(CompleteDSLPckg::SendObjectAction.__init__)


def test_completedslpckg::sendobjectaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::inputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InputPin)


def test_completedslpckg::inputpin_constructor_exists():
    assert callable(CompleteDSLPckg::InputPin.__init__)


def test_completedslpckg::inputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::action_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Action)


def test_completedslpckg::action_constructor_exists():
    assert callable(CompleteDSLPckg::Action.__init__)


def test_completedslpckg::action_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Action.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DeploymentSpecification)


def test_completedslpckg::deploymentspecification_constructor_exists():
    assert callable(CompleteDSLPckg::DeploymentSpecification.__init__)


def test_completedslpckg::deploymentspecification_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"

def test_completedslpckg::deploymentspecification_has_executionLocation():
    assert hasattr(CompleteDSLPckg::DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in CompleteDSLPckg::DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::deploymentspecification_has_deploymentLocation():
    assert hasattr(CompleteDSLPckg::DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in CompleteDSLPckg::DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::deployedartifact_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DeployedArtifact)


def test_completedslpckg::deployedartifact_constructor_exists():
    assert callable(CompleteDSLPckg::DeployedArtifact.__init__)


def test_completedslpckg::deployedartifact_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DeploymentTarget)


def test_completedslpckg::deploymenttarget_constructor_exists():
    assert callable(CompleteDSLPckg::DeploymentTarget.__init__)


def test_completedslpckg::deploymenttarget_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExecutionEnvironment)


def test_completedslpckg::executionenvironment_constructor_exists():
    assert callable(CompleteDSLPckg::ExecutionEnvironment.__init__)


def test_completedslpckg::executionenvironment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::device_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Device)


def test_completedslpckg::device_constructor_exists():
    assert callable(CompleteDSLPckg::Device.__init__)


def test_completedslpckg::device_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Device.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::outputpin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::OutputPin)


def test_completedslpckg::outputpin_constructor_exists():
    assert callable(CompleteDSLPckg::OutputPin.__init__)


def test_completedslpckg::outputpin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::invocationaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InvocationAction)


def test_completedslpckg::invocationaction_constructor_exists():
    assert callable(CompleteDSLPckg::InvocationAction.__init__)


def test_completedslpckg::invocationaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::connectableelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ConnectableElement)


def test_completedslpckg::connectableelement_constructor_exists():
    assert callable(CompleteDSLPckg::ConnectableElement.__init__)


def test_completedslpckg::connectableelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::connectorend_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ConnectorEnd)


def test_completedslpckg::connectorend_constructor_exists():
    assert callable(CompleteDSLPckg::ConnectorEnd.__init__)


def test_completedslpckg::connectorend_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::port_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Port)


def test_completedslpckg::port_constructor_exists():
    assert callable(CompleteDSLPckg::Port.__init__)


def test_completedslpckg::port_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Port.__init__)
    params = list(sig.parameters.keys())
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"
    assert "isConjugated" in params, "Missing parameter 'isConjugated'"
    assert "isService" in params, "Missing parameter 'isService'"

def test_completedslpckg::port_has_isBehavior():
    assert hasattr(CompleteDSLPckg::Port, "isBehavior")
    descriptor = None
    for klass in CompleteDSLPckg::Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::port_has_isConjugated():
    assert hasattr(CompleteDSLPckg::Port, "isConjugated")
    descriptor = None
    for klass in CompleteDSLPckg::Port.__mro__:
        if "isConjugated" in klass.__dict__:
            descriptor = klass.__dict__["isConjugated"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::port_has_isService():
    assert hasattr(CompleteDSLPckg::Port, "isService")
    descriptor = None
    for klass in CompleteDSLPckg::Port.__mro__:
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



def test_completedslpckg::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DurationConstraint)


def test_completedslpckg::durationconstraint_constructor_exists():
    assert callable(CompleteDSLPckg::DurationConstraint.__init__)


def test_completedslpckg::durationconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg::durationconstraint_has_firstEvent():
    assert hasattr(CompleteDSLPckg::DurationConstraint, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg::DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::TimeConstraint)


def test_completedslpckg::timeconstraint_constructor_exists():
    assert callable(CompleteDSLPckg::TimeConstraint.__init__)


def test_completedslpckg::timeconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg::timeconstraint_has_firstEvent():
    assert hasattr(CompleteDSLPckg::TimeConstraint, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg::TimeConstraint.__mro__:
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



def test_completedslpckg::interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InteractionConstraint)


def test_completedslpckg::interactionconstraint_constructor_exists():
    assert callable(CompleteDSLPckg::InteractionConstraint.__init__)


def test_completedslpckg::interactionconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::IntervalConstraint)


def test_completedslpckg::intervalconstraint_constructor_exists():
    assert callable(CompleteDSLPckg::IntervalConstraint.__init__)


def test_completedslpckg::intervalconstraint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::durationinterval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DurationInterval)


def test_completedslpckg::durationinterval_constructor_exists():
    assert callable(CompleteDSLPckg::DurationInterval.__init__)


def test_completedslpckg::durationinterval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::timeinterval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::TimeInterval)


def test_completedslpckg::timeinterval_constructor_exists():
    assert callable(CompleteDSLPckg::TimeInterval.__init__)


def test_completedslpckg::timeinterval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::duration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Duration)


def test_completedslpckg::duration_constructor_exists():
    assert callable(CompleteDSLPckg::Duration.__init__)


def test_completedslpckg::duration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Duration.__init__)
    params = list(sig.parameters.keys())



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::durationobservation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DurationObservation)


def test_completedslpckg::durationobservation_constructor_exists():
    assert callable(CompleteDSLPckg::DurationObservation.__init__)


def test_completedslpckg::durationobservation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg::durationobservation_has_firstEvent():
    assert hasattr(CompleteDSLPckg::DurationObservation, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg::DurationObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::timeobservation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::TimeObservation)


def test_completedslpckg::timeobservation_constructor_exists():
    assert callable(CompleteDSLPckg::TimeObservation.__init__)


def test_completedslpckg::timeobservation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_completedslpckg::timeobservation_has_firstEvent():
    assert hasattr(CompleteDSLPckg::TimeObservation, "firstEvent")
    descriptor = None
    for klass in CompleteDSLPckg::TimeObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::observation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Observation)


def test_completedslpckg::observation_constructor_exists():
    assert callable(CompleteDSLPckg::Observation.__init__)


def test_completedslpckg::observation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Observation.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::timeexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::TimeExpression)


def test_completedslpckg::timeexpression_constructor_exists():
    assert callable(CompleteDSLPckg::TimeExpression.__init__)


def test_completedslpckg::timeexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::timeevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::TimeEvent)


def test_completedslpckg::timeevent_constructor_exists():
    assert callable(CompleteDSLPckg::TimeEvent.__init__)


def test_completedslpckg::timeevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_completedslpckg::timeevent_has_isRelative():
    assert hasattr(CompleteDSLPckg::TimeEvent, "isRelative")
    descriptor = None
    for klass in CompleteDSLPckg::TimeEvent.__mro__:
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



def test_completedslpckg::callevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CallEvent)


def test_completedslpckg::callevent_constructor_exists():
    assert callable(CompleteDSLPckg::CallEvent.__init__)


def test_completedslpckg::callevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::signalevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::SignalEvent)


def test_completedslpckg::signalevent_constructor_exists():
    assert callable(CompleteDSLPckg::SignalEvent.__init__)


def test_completedslpckg::signalevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AnyReceiveEvent)


def test_completedslpckg::anyreceiveevent_constructor_exists():
    assert callable(CompleteDSLPckg::AnyReceiveEvent.__init__)


def test_completedslpckg::anyreceiveevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::changeevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ChangeEvent)


def test_completedslpckg::changeevent_constructor_exists():
    assert callable(CompleteDSLPckg::ChangeEvent.__init__)


def test_completedslpckg::changeevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::messageevent_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::MessageEvent)


def test_completedslpckg::messageevent_constructor_exists():
    assert callable(CompleteDSLPckg::MessageEvent.__init__)


def test_completedslpckg::messageevent_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::interval_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Interval)


def test_completedslpckg::interval_constructor_exists():
    assert callable(CompleteDSLPckg::Interval.__init__)


def test_completedslpckg::interval_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Interval.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::trigger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Trigger)


def test_completedslpckg::trigger_constructor_exists():
    assert callable(CompleteDSLPckg::Trigger.__init__)


def test_completedslpckg::trigger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::functionbehavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::FunctionBehavior)


def test_completedslpckg::functionbehavior_constructor_exists():
    assert callable(CompleteDSLPckg::FunctionBehavior.__init__)


def test_completedslpckg::functionbehavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::statemachine_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StateMachine)


def test_completedslpckg::statemachine_constructor_exists():
    assert callable(CompleteDSLPckg::StateMachine.__init__)


def test_completedslpckg::statemachine_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::activity_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Activity)


def test_completedslpckg::activity_constructor_exists():
    assert callable(CompleteDSLPckg::Activity.__init__)


def test_completedslpckg::activity_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_completedslpckg::activity_has_isSingleExecution():
    assert hasattr(CompleteDSLPckg::Activity, "isSingleExecution")
    descriptor = None
    for klass in CompleteDSLPckg::Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::activity_has_isReadOnly():
    assert hasattr(CompleteDSLPckg::Activity, "isReadOnly")
    descriptor = None
    for klass in CompleteDSLPckg::Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::interaction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Interaction)


def test_completedslpckg::interaction_constructor_exists():
    assert callable(CompleteDSLPckg::Interaction.__init__)


def test_completedslpckg::interaction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::OpaqueBehavior)


def test_completedslpckg::opaquebehavior_constructor_exists():
    assert callable(CompleteDSLPckg::OpaqueBehavior.__init__)


def test_completedslpckg::opaquebehavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_completedslpckg::opaquebehavior_has_language():
    assert hasattr(CompleteDSLPckg::OpaqueBehavior, "language")
    descriptor = None
    for klass in CompleteDSLPckg::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::opaquebehavior_has_body():
    assert hasattr(CompleteDSLPckg::OpaqueBehavior, "body")
    descriptor = None
    for klass in CompleteDSLPckg::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::event_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Event)


def test_completedslpckg::event_constructor_exists():
    assert callable(CompleteDSLPckg::Event.__init__)


def test_completedslpckg::event_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Event.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::communicationpath_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CommunicationPath)


def test_completedslpckg::communicationpath_constructor_exists():
    assert callable(CompleteDSLPckg::CommunicationPath.__init__)


def test_completedslpckg::communicationpath_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::behavior_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Behavior)


def test_completedslpckg::behavior_constructor_exists():
    assert callable(CompleteDSLPckg::Behavior.__init__)


def test_completedslpckg::behavior_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_completedslpckg::behavior_has_isReentrant():
    assert hasattr(CompleteDSLPckg::Behavior, "isReentrant")
    descriptor = None
    for klass in CompleteDSLPckg::Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::component_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Component)


def test_completedslpckg::component_constructor_exists():
    assert callable(CompleteDSLPckg::Component.__init__)


def test_completedslpckg::component_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"

def test_completedslpckg::component_has_isIndirectlyInstantiated():
    assert hasattr(CompleteDSLPckg::Component, "isIndirectlyInstantiated")
    descriptor = None
    for klass in CompleteDSLPckg::Component.__mro__:
        if "isIndirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["isIndirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::associationclass_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AssociationClass)


def test_completedslpckg::associationclass_constructor_exists():
    assert callable(CompleteDSLPckg::AssociationClass.__init__)


def test_completedslpckg::associationclass_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::componentrealization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ComponentRealization)


def test_completedslpckg::componentrealization_constructor_exists():
    assert callable(CompleteDSLPckg::ComponentRealization.__init__)


def test_completedslpckg::componentrealization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::interfacerealization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InterfaceRealization)


def test_completedslpckg::interfacerealization_constructor_exists():
    assert callable(CompleteDSLPckg::InterfaceRealization.__init__)


def test_completedslpckg::interfacerealization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::manifestation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Manifestation)


def test_completedslpckg::manifestation_constructor_exists():
    assert callable(CompleteDSLPckg::Manifestation.__init__)


def test_completedslpckg::manifestation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::realization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Realization)


def test_completedslpckg::realization_constructor_exists():
    assert callable(CompleteDSLPckg::Realization.__init__)


def test_completedslpckg::realization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Realization.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::deployment_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Deployment)


def test_completedslpckg::deployment_constructor_exists():
    assert callable(CompleteDSLPckg::Deployment.__init__)


def test_completedslpckg::deployment_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Deployment.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::abstraction_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Abstraction)


def test_completedslpckg::abstraction_constructor_exists():
    assert callable(CompleteDSLPckg::Abstraction.__init__)


def test_completedslpckg::abstraction_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::usage_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Usage)


def test_completedslpckg::usage_constructor_exists():
    assert callable(CompleteDSLPckg::Usage.__init__)


def test_completedslpckg::usage_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Usage.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::EnumerationLiteral)


def test_completedslpckg::enumerationliteral_constructor_exists():
    assert callable(CompleteDSLPckg::EnumerationLiteral.__init__)


def test_completedslpckg::enumerationliteral_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::enumeration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Enumeration)


def test_completedslpckg::enumeration_constructor_exists():
    assert callable(CompleteDSLPckg::Enumeration.__init__)


def test_completedslpckg::enumeration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::primitivetype_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::PrimitiveType)


def test_completedslpckg::primitivetype_constructor_exists():
    assert callable(CompleteDSLPckg::PrimitiveType.__init__)


def test_completedslpckg::primitivetype_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::PrimitiveType.__init__)
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



def test_completedslpckg::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::EncapsulatedClassifier)


def test_completedslpckg::encapsulatedclassifier_constructor_exists():
    assert callable(CompleteDSLPckg::EncapsulatedClassifier.__init__)


def test_completedslpckg::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::usecase_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::UseCase)


def test_completedslpckg::usecase_constructor_exists():
    assert callable(CompleteDSLPckg::UseCase.__init__)


def test_completedslpckg::usecase_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::actor_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Actor)


def test_completedslpckg::actor_constructor_exists():
    assert callable(CompleteDSLPckg::Actor.__init__)


def test_completedslpckg::actor_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Actor.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::collaboration_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Collaboration)


def test_completedslpckg::collaboration_constructor_exists():
    assert callable(CompleteDSLPckg::Collaboration.__init__)


def test_completedslpckg::collaboration_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::BehavioredClassifier)


def test_completedslpckg::behavioredclassifier_constructor_exists():
    assert callable(CompleteDSLPckg::BehavioredClassifier.__init__)


def test_completedslpckg::behavioredclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StructuredClassifier)


def test_completedslpckg::structuredclassifier_constructor_exists():
    assert callable(CompleteDSLPckg::StructuredClassifier.__init__)


def test_completedslpckg::structuredclassifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::artifact_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Artifact)


def test_completedslpckg::artifact_constructor_exists():
    assert callable(CompleteDSLPckg::Artifact.__init__)


def test_completedslpckg::artifact_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_completedslpckg::artifact_has_fileName():
    assert hasattr(CompleteDSLPckg::Artifact, "fileName")
    descriptor = None
    for klass in CompleteDSLPckg::Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::signal_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Signal)


def test_completedslpckg::signal_constructor_exists():
    assert callable(CompleteDSLPckg::Signal.__init__)


def test_completedslpckg::signal_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Signal.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::reception_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Reception)


def test_completedslpckg::reception_constructor_exists():
    assert callable(CompleteDSLPckg::Reception.__init__)


def test_completedslpckg::reception_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Reception.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::operation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Operation)


def test_completedslpckg::operation_constructor_exists():
    assert callable(CompleteDSLPckg::Operation.__init__)


def test_completedslpckg::operation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_completedslpckg::operation_has_lower():
    assert hasattr(CompleteDSLPckg::Operation, "lower")
    descriptor = None
    for klass in CompleteDSLPckg::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::operation_has_isOrdered():
    assert hasattr(CompleteDSLPckg::Operation, "isOrdered")
    descriptor = None
    for klass in CompleteDSLPckg::Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::operation_has_isUnique():
    assert hasattr(CompleteDSLPckg::Operation, "isUnique")
    descriptor = None
    for klass in CompleteDSLPckg::Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::operation_has_isQuery():
    assert hasattr(CompleteDSLPckg::Operation, "isQuery")
    descriptor = None
    for klass in CompleteDSLPckg::Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::operation_has_upper():
    assert hasattr(CompleteDSLPckg::Operation, "upper")
    descriptor = None
    for klass in CompleteDSLPckg::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::interface_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Interface)


def test_completedslpckg::interface_constructor_exists():
    assert callable(CompleteDSLPckg::Interface.__init__)


def test_completedslpckg::interface_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Interface.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::datatype_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::DataType)


def test_completedslpckg::datatype_constructor_exists():
    assert callable(CompleteDSLPckg::DataType.__init__)


def test_completedslpckg::datatype_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::DataType.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::association_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Association)


def test_completedslpckg::association_constructor_exists():
    assert callable(CompleteDSLPckg::Association.__init__)


def test_completedslpckg::association_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_completedslpckg::association_has_isDerived():
    assert hasattr(CompleteDSLPckg::Association, "isDerived")
    descriptor = None
    for klass in CompleteDSLPckg::Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::class_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Class)


def test_completedslpckg::class_constructor_exists():
    assert callable(CompleteDSLPckg::Class.__init__)


def test_completedslpckg::class_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Class.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::node_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Node)


def test_completedslpckg::node_constructor_exists():
    assert callable(CompleteDSLPckg::Node.__init__)


def test_completedslpckg::node_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Node.__init__)
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



def test_completedslpckg::variable_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Variable)


def test_completedslpckg::variable_constructor_exists():
    assert callable(CompleteDSLPckg::Variable.__init__)


def test_completedslpckg::variable_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Variable.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::pin_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Pin)


def test_completedslpckg::pin_constructor_exists():
    assert callable(CompleteDSLPckg::Pin.__init__)


def test_completedslpckg::pin_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Pin.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StructuralFeature)


def test_completedslpckg::structuralfeature_constructor_exists():
    assert callable(CompleteDSLPckg::StructuralFeature.__init__)


def test_completedslpckg::structuralfeature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_completedslpckg::structuralfeature_has_isReadOnly():
    assert hasattr(CompleteDSLPckg::StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in CompleteDSLPckg::StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::connector_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Connector)


def test_completedslpckg::connector_constructor_exists():
    assert callable(CompleteDSLPckg::Connector.__init__)


def test_completedslpckg::connector_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_completedslpckg::connector_has_kind():
    assert hasattr(CompleteDSLPckg::Connector, "kind")
    descriptor = None
    for klass in CompleteDSLPckg::Connector.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::BehavioralFeature)


def test_completedslpckg::behavioralfeature_constructor_exists():
    assert callable(CompleteDSLPckg::BehavioralFeature.__init__)


def test_completedslpckg::behavioralfeature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::collaborationuse_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::CollaborationUse)


def test_completedslpckg::collaborationuse_constructor_exists():
    assert callable(CompleteDSLPckg::CollaborationUse.__init__)


def test_completedslpckg::collaborationuse_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::generalizationset_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::GeneralizationSet)


def test_completedslpckg::generalizationset_constructor_exists():
    assert callable(CompleteDSLPckg::GeneralizationSet.__init__)


def test_completedslpckg::generalizationset_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"
    assert "isCovering" in params, "Missing parameter 'isCovering'"

def test_completedslpckg::generalizationset_has_isDisjoint():
    assert hasattr(CompleteDSLPckg::GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in CompleteDSLPckg::GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::generalizationset_has_isCovering():
    assert hasattr(CompleteDSLPckg::GeneralizationSet, "isCovering")
    descriptor = None
    for klass in CompleteDSLPckg::GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::substitution_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Substitution)


def test_completedslpckg::substitution_constructor_exists():
    assert callable(CompleteDSLPckg::Substitution.__init__)


def test_completedslpckg::substitution_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::generalization_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Generalization)


def test_completedslpckg::generalization_constructor_exists():
    assert callable(CompleteDSLPckg::Generalization.__init__)


def test_completedslpckg::generalization_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_completedslpckg::generalization_has_isSubstitutable():
    assert hasattr(CompleteDSLPckg::Generalization, "isSubstitutable")
    descriptor = None
    for klass in CompleteDSLPckg::Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::property_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Property)


def test_completedslpckg::property_constructor_exists():
    assert callable(CompleteDSLPckg::Property.__init__)


def test_completedslpckg::property_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_completedslpckg::property_has_isDerived():
    assert hasattr(CompleteDSLPckg::Property, "isDerived")
    descriptor = None
    for klass in CompleteDSLPckg::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::property_has_default():
    assert hasattr(CompleteDSLPckg::Property, "default")
    descriptor = None
    for klass in CompleteDSLPckg::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::property_has_isID():
    assert hasattr(CompleteDSLPckg::Property, "isID")
    descriptor = None
    for klass in CompleteDSLPckg::Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::property_has_isComposite():
    assert hasattr(CompleteDSLPckg::Property, "isComposite")
    descriptor = None
    for klass in CompleteDSLPckg::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::property_has_isDerivedUnion():
    assert hasattr(CompleteDSLPckg::Property, "isDerivedUnion")
    descriptor = None
    for klass in CompleteDSLPckg::Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::property_has_aggregation():
    assert hasattr(CompleteDSLPckg::Property, "aggregation")
    descriptor = None
    for klass in CompleteDSLPckg::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
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



def test_completedslpckg::classifier_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Classifier)


def test_completedslpckg::classifier_constructor_exists():
    assert callable(CompleteDSLPckg::Classifier.__init__)


def test_completedslpckg::classifier_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isFinalSpecialization" in params, "Missing parameter 'isFinalSpecialization'"

def test_completedslpckg::classifier_has_isAbstract():
    assert hasattr(CompleteDSLPckg::Classifier, "isAbstract")
    descriptor = None
    for klass in CompleteDSLPckg::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::classifier_has_isFinalSpecialization():
    assert hasattr(CompleteDSLPckg::Classifier, "isFinalSpecialization")
    descriptor = None
    for klass in CompleteDSLPckg::Classifier.__mro__:
        if "isFinalSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["isFinalSpecialization"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::state_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::State)


def test_completedslpckg::state_constructor_exists():
    assert callable(CompleteDSLPckg::State.__init__)


def test_completedslpckg::state_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"

def test_completedslpckg::state_has_isComposite():
    assert hasattr(CompleteDSLPckg::State, "isComposite")
    descriptor = None
    for klass in CompleteDSLPckg::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::state_has_isSubmachineState():
    assert hasattr(CompleteDSLPckg::State, "isSubmachineState")
    descriptor = None
    for klass in CompleteDSLPckg::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::state_has_isSimple():
    assert hasattr(CompleteDSLPckg::State, "isSimple")
    descriptor = None
    for klass in CompleteDSLPckg::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_completedslpckg::state_has_isOrthogonal():
    assert hasattr(CompleteDSLPckg::State, "isOrthogonal")
    descriptor = None
    for klass in CompleteDSLPckg::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::feature_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Feature)


def test_completedslpckg::feature_constructor_exists():
    assert callable(CompleteDSLPckg::Feature.__init__)


def test_completedslpckg::feature_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_completedslpckg::feature_has_isStatic():
    assert hasattr(CompleteDSLPckg::Feature, "isStatic")
    descriptor = None
    for klass in CompleteDSLPckg::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ExtensionPoint)


def test_completedslpckg::extensionpoint_constructor_exists():
    assert callable(CompleteDSLPckg::ExtensionPoint.__init__)


def test_completedslpckg::extensionpoint_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::activityedge_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActivityEdge)


def test_completedslpckg::activityedge_constructor_exists():
    assert callable(CompleteDSLPckg::ActivityEdge.__init__)


def test_completedslpckg::activityedge_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::transition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Transition)


def test_completedslpckg::transition_constructor_exists():
    assert callable(CompleteDSLPckg::Transition.__init__)


def test_completedslpckg::transition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_completedslpckg::transition_has_kind():
    assert hasattr(CompleteDSLPckg::Transition, "kind")
    descriptor = None
    for klass in CompleteDSLPckg::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::region_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Region)


def test_completedslpckg::region_constructor_exists():
    assert callable(CompleteDSLPckg::Region.__init__)


def test_completedslpckg::region_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Region.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::activitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ActivityNode)


def test_completedslpckg::activitynode_constructor_exists():
    assert callable(CompleteDSLPckg::ActivityNode.__init__)


def test_completedslpckg::activitynode_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ActivityNode.__init__)
    params = list(sig.parameters.keys())

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

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "read",
        "create",
        "update",
        "delete",
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
        "stream",
        "parallel",
        "iterative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "asynchCall",
        "asynchSignal",
        "createMessage",
        "synchCall",
        "deleteMessage",
        "reply",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "protected",
        "private",
        "public",
        "package",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "shared",
        "composite",
        "none",
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
        "internal",
        "external",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_interactionoperandkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperandKind is not None

def test_interactionoperandkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperandKind]
    expected_literals = [
        "opt",
        "loop",
        "neg",
        "ignore",
        "consider",
        "seq",
        "assert_",
        "critical",
        "alt",
        "strict",
        "par",
        "break_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperandKind"

def test_callconcurrencyfeature_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyFeature is not None

def test_callconcurrencyfeature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyFeature]
    expected_literals = [
        "sequential",
        "concurrent",
        "guarded",
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
        "complete",
        "found",
        "unknown",
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
InteractionUse_strategy = st.builds(
    InteractionUse,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
CompleteDSLPckg::ConsiderIgnoreFragment_strategy = st.builds(
    CompleteDSLPckg::ConsiderIgnoreFragment,
)
CompleteDSLPckg::CombinedFragment_strategy = st.builds(
    CompleteDSLPckg::CombinedFragment,
    interactionOperator=
        safe_text
)
CompleteDSLPckg::PartDecomposition_strategy = st.builds(
    CompleteDSLPckg::PartDecomposition,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
CompleteDSLPckg::ActionExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg::ActionExecutionSpecification,
)
CompleteDSLPckg::BehaviorExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg::BehaviorExecutionSpecification,
)
MessageOccurrenceSpecification_strategy = st.builds(
    MessageOccurrenceSpecification,
)
CompleteDSLPckg::DestructionOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg::DestructionOccurrenceSpecification,
)
OccurenceSpecification_strategy = st.builds(
    OccurenceSpecification,
)
CompleteDSLPckg::MessageOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg::MessageOccurrenceSpecification,
)
CompleteDSLPckg::ExecutionOccurrenceSpecification_strategy = st.builds(
    CompleteDSLPckg::ExecutionOccurrenceSpecification,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
CompleteDSLPckg::Continuation_strategy = st.builds(
    CompleteDSLPckg::Continuation,
    setting=
        st.booleans()
)
CompleteDSLPckg::InteractionUse_strategy = st.builds(
    CompleteDSLPckg::InteractionUse,
)
CompleteDSLPckg::OccurenceSpecification_strategy = st.builds(
    CompleteDSLPckg::OccurenceSpecification,
)
CompleteDSLPckg::StateInvariant_strategy = st.builds(
    CompleteDSLPckg::StateInvariant,
)
CompleteDSLPckg::ExecutionSpecification_strategy = st.builds(
    CompleteDSLPckg::ExecutionSpecification,
)
CompleteDSLPckg::Gate_strategy = st.builds(
    CompleteDSLPckg::Gate,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
CompleteDSLPckg::DataStoreNode_strategy = st.builds(
    CompleteDSLPckg::DataStoreNode,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
CompleteDSLPckg::ExpansionRegion_strategy = st.builds(
    CompleteDSLPckg::ExpansionRegion,
    mode=
        safe_text
)
CompleteDSLPckg::ConditionalNode_strategy = st.builds(
    CompleteDSLPckg::ConditionalNode,
    isDeterminate=
        st.booleans(),
    isAssumed=
        st.booleans()
)
CompleteDSLPckg::SequenceNode_strategy = st.builds(
    CompleteDSLPckg::SequenceNode,
)
CompleteDSLPckg::LoopNode_strategy = st.builds(
    CompleteDSLPckg::LoopNode,
    isTestedFirst=
        st.booleans()
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
CompleteDSLPckg::ObjectFlow_strategy = st.builds(
    CompleteDSLPckg::ObjectFlow,
    isMultireceive=
        st.booleans(),
    ordering=
        safe_text,
    isMulticast=
        st.booleans(),
    isControlType=
        st.booleans()
)
CompleteDSLPckg::ControlFlow_strategy = st.builds(
    CompleteDSLPckg::ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
CompleteDSLPckg::FlowFinalNode_strategy = st.builds(
    CompleteDSLPckg::FlowFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
CompleteDSLPckg::FinalNode_strategy = st.builds(
    CompleteDSLPckg::FinalNode,
)
CompleteDSLPckg::MergeNode_strategy = st.builds(
    CompleteDSLPckg::MergeNode,
)
CompleteDSLPckg::DecisionNode_strategy = st.builds(
    CompleteDSLPckg::DecisionNode,
)
CompleteDSLPckg::InitialNode_strategy = st.builds(
    CompleteDSLPckg::InitialNode,
)
CompleteDSLPckg::JoinNode_strategy = st.builds(
    CompleteDSLPckg::JoinNode,
    isCombineDuplicate=
        st.booleans()
)
CompleteDSLPckg::ForkNode_strategy = st.builds(
    CompleteDSLPckg::ForkNode,
)
CompleteDSLPckg::ActivityFinalNode_strategy = st.builds(
    CompleteDSLPckg::ActivityFinalNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
CompleteDSLPckg::CentralBufferNode_strategy = st.builds(
    CompleteDSLPckg::CentralBufferNode,
)
CompleteDSLPckg::ExpansionNode_strategy = st.builds(
    CompleteDSLPckg::ExpansionNode,
)
CompleteDSLPckg::ActivityParameterNode_strategy = st.builds(
    CompleteDSLPckg::ActivityParameterNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
CompleteDSLPckg::ControlNode_strategy = st.builds(
    CompleteDSLPckg::ControlNode,
)
CompleteDSLPckg::ExecutableNode_strategy = st.builds(
    CompleteDSLPckg::ExecutableNode,
)
CompleteDSLPckg::ActivityPartition_strategy = st.builds(
    CompleteDSLPckg::ActivityPartition,
)
Transition_strategy = st.builds(
    Transition,
)
CompleteDSLPckg::ProtocolTransition_strategy = st.builds(
    CompleteDSLPckg::ProtocolTransition,
)
CompleteDSLPckg::InterruptibleActivityRegion_strategy = st.builds(
    CompleteDSLPckg::InterruptibleActivityRegion,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
CompleteDSLPckg::ProtocolStateMachine_strategy = st.builds(
    CompleteDSLPckg::ProtocolStateMachine,
)
State_strategy = st.builds(
    State,
)
CompleteDSLPckg::FinalState_strategy = st.builds(
    CompleteDSLPckg::FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
CompleteDSLPckg::ConnectionPointReference_strategy = st.builds(
    CompleteDSLPckg::ConnectionPointReference,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
CompleteDSLPckg::RemoveVariableValueAction_strategy = st.builds(
    CompleteDSLPckg::RemoveVariableValueAction,
)
CompleteDSLPckg::AddVariableValueAction_strategy = st.builds(
    CompleteDSLPckg::AddVariableValueAction,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
CompleteDSLPckg::ClearVariableAction_strategy = st.builds(
    CompleteDSLPckg::ClearVariableAction,
)
CompleteDSLPckg::WriteVariableAction_strategy = st.builds(
    CompleteDSLPckg::WriteVariableAction,
)
CompleteDSLPckg::ReadVariableAction_strategy = st.builds(
    CompleteDSLPckg::ReadVariableAction,
)
CompleteDSLPckg::Pseudostate_strategy = st.builds(
    CompleteDSLPckg::Pseudostate,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
CompleteDSLPckg::CreateLinkObjectAction_strategy = st.builds(
    CompleteDSLPckg::CreateLinkObjectAction,
)
CompleteDSLPckg::ReadlsClassifiedObjectAction_strategy = st.builds(
    CompleteDSLPckg::ReadlsClassifiedObjectAction,
)
CompleteDSLPckg::InstanceValue_strategy = st.builds(
    CompleteDSLPckg::InstanceValue,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
CompleteDSLPckg::LiteralUnilimitedNatural_strategy = st.builds(
    CompleteDSLPckg::LiteralUnilimitedNatural,
)
CompleteDSLPckg::LiteralInteger_strategy = st.builds(
    CompleteDSLPckg::LiteralInteger,
)
CompleteDSLPckg::LiteralString_strategy = st.builds(
    CompleteDSLPckg::LiteralString,
)
CompleteDSLPckg::LiteralBoolean_strategy = st.builds(
    CompleteDSLPckg::LiteralBoolean,
)
CompleteDSLPckg::LiteralReal_strategy = st.builds(
    CompleteDSLPckg::LiteralReal,
)
CompleteDSLPckg::LiteralNull_strategy = st.builds(
    CompleteDSLPckg::LiteralNull,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
CompleteDSLPckg::LiteralSpecification_strategy = st.builds(
    CompleteDSLPckg::LiteralSpecification,
)
CompleteDSLPckg::OpaqueExpression_strategy = st.builds(
    CompleteDSLPckg::OpaqueExpression,
    language=
        safe_text,
    body=
        safe_text
)
CompleteDSLPckg::Expression_strategy = st.builds(
    CompleteDSLPckg::Expression,
    symbol=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
CompleteDSLPckg::Parameter_strategy = st.builds(
    CompleteDSLPckg::Parameter,
    default=
        safe_text
)
CompleteDSLPckg::ObjectNode_strategy = st.builds(
    CompleteDSLPckg::ObjectNode,
)
Relationship_strategy = st.builds(
    Relationship,
)
CompleteDSLPckg::DirectedRelationship_strategy = st.builds(
    CompleteDSLPckg::DirectedRelationship,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
CompleteDSLPckg::ValueSpecification_strategy = st.builds(
    CompleteDSLPckg::ValueSpecification,
)
CompleteDSLPckg::Type_strategy = st.builds(
    CompleteDSLPckg::Type,
)
CompleteDSLPckg::InstanceSpecification_strategy = st.builds(
    CompleteDSLPckg::InstanceSpecification,
)
Namespace_strategy = st.builds(
    Namespace,
)
CompleteDSLPckg::InteractionOperand_strategy = st.builds(
    CompleteDSLPckg::InteractionOperand,
)
CompleteDSLPckg::Package_strategy = st.builds(
    CompleteDSLPckg::Package,
    URI=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
CompleteDSLPckg::ProtocolConformance_strategy = st.builds(
    CompleteDSLPckg::ProtocolConformance,
)
CompleteDSLPckg::PackageMerge_strategy = st.builds(
    CompleteDSLPckg::PackageMerge,
)
CompleteDSLPckg::Constraint_strategy = st.builds(
    CompleteDSLPckg::Constraint,
)
CompleteDSLPckg::PackageImport_strategy = st.builds(
    CompleteDSLPckg::PackageImport,
    visibility=
        safe_text
)
CompleteDSLPckg::ElementImport_strategy = st.builds(
    CompleteDSLPckg::ElementImport,
    alias=
        safe_text,
    visibility=
        safe_text
)
CompleteDSLPckg::Dependency_strategy = st.builds(
    CompleteDSLPckg::Dependency,
)
Element_strategy = st.builds(
    Element,
)
CompleteDSLPckg::Clause_strategy = st.builds(
    CompleteDSLPckg::Clause,
)
CompleteDSLPckg::Relationship_strategy = st.builds(
    CompleteDSLPckg::Relationship,
)
CompleteDSLPckg::MultiplicityElement_strategy = st.builds(
    CompleteDSLPckg::MultiplicityElement,
    isUnique=
        st.booleans(),
    isOrdered=
        st.booleans(),
    lower=
        st.integers(),
    upper=
        st.integers()
)
CompleteDSLPckg::Slot_strategy = st.builds(
    CompleteDSLPckg::Slot,
)
CompleteDSLPckg::ExceptionHandler_strategy = st.builds(
    CompleteDSLPckg::ExceptionHandler,
)
CompleteDSLPckg::NamedElement_strategy = st.builds(
    CompleteDSLPckg::NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text,
    visibility=
        safe_text
)
CompleteDSLPckg::Comment_strategy = st.builds(
    CompleteDSLPckg::Comment,
    body=
        safe_text
)
CompleteDSLPckg::Element_strategy = st.builds(
    CompleteDSLPckg::Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
CompleteDSLPckg::Lifeline_strategy = st.builds(
    CompleteDSLPckg::Lifeline,
)
CompleteDSLPckg::Include_strategy = st.builds(
    CompleteDSLPckg::Include,
)
CompleteDSLPckg::GeneralOrdering_strategy = st.builds(
    CompleteDSLPckg::GeneralOrdering,
)
CompleteDSLPckg::Namespace_strategy = st.builds(
    CompleteDSLPckg::Namespace,
)
CompleteDSLPckg::ActivityGroup_strategy = st.builds(
    CompleteDSLPckg::ActivityGroup,
)
CompleteDSLPckg::TypedElement_strategy = st.builds(
    CompleteDSLPckg::TypedElement,
)
CompleteDSLPckg::Message_strategy = st.builds(
    CompleteDSLPckg::Message,
    messageKind=
        safe_text,
    messageSort=
        safe_text
)
CompleteDSLPckg::ParameterSet_strategy = st.builds(
    CompleteDSLPckg::ParameterSet,
)
CompleteDSLPckg::RedefinableElement_strategy = st.builds(
    CompleteDSLPckg::RedefinableElement,
    isLeaf=
        st.booleans()
)
CompleteDSLPckg::InteractionFragment_strategy = st.builds(
    CompleteDSLPckg::InteractionFragment,
)
CompleteDSLPckg::Vertex_strategy = st.builds(
    CompleteDSLPckg::Vertex,
)
CompleteDSLPckg::MessageEnd_strategy = st.builds(
    CompleteDSLPckg::MessageEnd,
)
CompleteDSLPckg::PackageableElement_strategy = st.builds(
    CompleteDSLPckg::PackageableElement,
)
CompleteDSLPckg::Extend_strategy = st.builds(
    CompleteDSLPckg::Extend,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
CompleteDSLPckg::AcceptCallAction_strategy = st.builds(
    CompleteDSLPckg::AcceptCallAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
CompleteDSLPckg::WriteLinkAction_strategy = st.builds(
    CompleteDSLPckg::WriteLinkAction,
)
CompleteDSLPckg::ReadLinkAction_strategy = st.builds(
    CompleteDSLPckg::ReadLinkAction,
)
CompleteDSLPckg::QualifierValue_strategy = st.builds(
    CompleteDSLPckg::QualifierValue,
)
CompleteDSLPckg::LinkEndData_strategy = st.builds(
    CompleteDSLPckg::LinkEndData,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
CompleteDSLPckg::RemoveStructuralFeatureValueAction_strategy = st.builds(
    CompleteDSLPckg::RemoveStructuralFeatureValueAction,
)
CompleteDSLPckg::AddStructuralFeatureValueAction_strategy = st.builds(
    CompleteDSLPckg::AddStructuralFeatureValueAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
CompleteDSLPckg::LinkEndDestructionData_strategy = st.builds(
    CompleteDSLPckg::LinkEndDestructionData,
    isDestroyDuplicates=
        st.booleans()
)
CompleteDSLPckg::LinkEndCreationData_strategy = st.builds(
    CompleteDSLPckg::LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
CompleteDSLPckg::DestroyLinkAction_strategy = st.builds(
    CompleteDSLPckg::DestroyLinkAction,
)
CompleteDSLPckg::CreateLinkAction_strategy = st.builds(
    CompleteDSLPckg::CreateLinkAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
CompleteDSLPckg::WriteStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg::WriteStructuralFeatureAction,
)
CompleteDSLPckg::ClearStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg::ClearStructuralFeatureAction,
)
CompleteDSLPckg::ReadStructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg::ReadStructuralFeatureAction,
)
CompleteDSLPckg::CallOperationAction_strategy = st.builds(
    CompleteDSLPckg::CallOperationAction,
)
CallAction_strategy = st.builds(
    CallAction,
)
CompleteDSLPckg::StartObjectBehaviorAction_strategy = st.builds(
    CompleteDSLPckg::StartObjectBehaviorAction,
)
CompleteDSLPckg::CallBehaviorAction_strategy = st.builds(
    CompleteDSLPckg::CallBehaviorAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
CompleteDSLPckg::BroadcastSignalAction_strategy = st.builds(
    CompleteDSLPckg::BroadcastSignalAction,
)
CompleteDSLPckg::SendSignalAction_strategy = st.builds(
    CompleteDSLPckg::SendSignalAction,
)
CompleteDSLPckg::CallAction_strategy = st.builds(
    CompleteDSLPckg::CallAction,
    isSynchronous=
        st.booleans()
)
InputPin_strategy = st.builds(
    InputPin,
)
CompleteDSLPckg::ActionInputPin_strategy = st.builds(
    CompleteDSLPckg::ActionInputPin,
)
CompleteDSLPckg::ValuePin_strategy = st.builds(
    CompleteDSLPckg::ValuePin,
)
Pin_strategy = st.builds(
    Pin,
)
Action_strategy = st.builds(
    Action,
)
CompleteDSLPckg::TestIdentityAction_strategy = st.builds(
    CompleteDSLPckg::TestIdentityAction,
)
CompleteDSLPckg::ReadSelfAction_strategy = st.builds(
    CompleteDSLPckg::ReadSelfAction,
)
CompleteDSLPckg::UnmarshallAction_strategy = st.builds(
    CompleteDSLPckg::UnmarshallAction,
)
CompleteDSLPckg::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    CompleteDSLPckg::ReadLinkObjectEndQualifierAction,
)
CompleteDSLPckg::CreateObjectAction_strategy = st.builds(
    CompleteDSLPckg::CreateObjectAction,
)
CompleteDSLPckg::ReadLinkObjectEndAction_strategy = st.builds(
    CompleteDSLPckg::ReadLinkObjectEndAction,
)
CompleteDSLPckg::LinkAction_strategy = st.builds(
    CompleteDSLPckg::LinkAction,
)
CompleteDSLPckg::ReplyAction_strategy = st.builds(
    CompleteDSLPckg::ReplyAction,
)
CompleteDSLPckg::VariableAction_strategy = st.builds(
    CompleteDSLPckg::VariableAction,
)
CompleteDSLPckg::ValueSpecificationAction_strategy = st.builds(
    CompleteDSLPckg::ValueSpecificationAction,
)
CompleteDSLPckg::DestroyObjectAction_strategy = st.builds(
    CompleteDSLPckg::DestroyObjectAction,
)
CompleteDSLPckg::StartClassifierBehaviorAction_strategy = st.builds(
    CompleteDSLPckg::StartClassifierBehaviorAction,
)
CompleteDSLPckg::ReadExtendAction_strategy = st.builds(
    CompleteDSLPckg::ReadExtendAction,
)
CompleteDSLPckg::AcceptEventAction_strategy = st.builds(
    CompleteDSLPckg::AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
CompleteDSLPckg::StructuredActivityNode_strategy = st.builds(
    CompleteDSLPckg::StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
CompleteDSLPckg::RaiseExceptionAction_strategy = st.builds(
    CompleteDSLPckg::RaiseExceptionAction,
)
CompleteDSLPckg::ReduceAction_strategy = st.builds(
    CompleteDSLPckg::ReduceAction,
    isOrdered=
        st.booleans()
)
CompleteDSLPckg::ReclassifyObjectAction_strategy = st.builds(
    CompleteDSLPckg::ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
CompleteDSLPckg::StructuralFeatureAction_strategy = st.builds(
    CompleteDSLPckg::StructuralFeatureAction,
)
CompleteDSLPckg::OpaqueAction_strategy = st.builds(
    CompleteDSLPckg::OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
CompleteDSLPckg::SendObjectAction_strategy = st.builds(
    CompleteDSLPckg::SendObjectAction,
)
CompleteDSLPckg::InputPin_strategy = st.builds(
    CompleteDSLPckg::InputPin,
)
CompleteDSLPckg::Action_strategy = st.builds(
    CompleteDSLPckg::Action,
)
Artifact_strategy = st.builds(
    Artifact,
)
CompleteDSLPckg::DeploymentSpecification_strategy = st.builds(
    CompleteDSLPckg::DeploymentSpecification,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text
)
CompleteDSLPckg::DeployedArtifact_strategy = st.builds(
    CompleteDSLPckg::DeployedArtifact,
)
CompleteDSLPckg::DeploymentTarget_strategy = st.builds(
    CompleteDSLPckg::DeploymentTarget,
)
Node_strategy = st.builds(
    Node,
)
CompleteDSLPckg::ExecutionEnvironment_strategy = st.builds(
    CompleteDSLPckg::ExecutionEnvironment,
)
CompleteDSLPckg::Device_strategy = st.builds(
    CompleteDSLPckg::Device,
)
CompleteDSLPckg::OutputPin_strategy = st.builds(
    CompleteDSLPckg::OutputPin,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
CompleteDSLPckg::InvocationAction_strategy = st.builds(
    CompleteDSLPckg::InvocationAction,
)
CompleteDSLPckg::ConnectableElement_strategy = st.builds(
    CompleteDSLPckg::ConnectableElement,
)
CompleteDSLPckg::ConnectorEnd_strategy = st.builds(
    CompleteDSLPckg::ConnectorEnd,
)
Property_strategy = st.builds(
    Property,
)
CompleteDSLPckg::Port_strategy = st.builds(
    CompleteDSLPckg::Port,
    isBehavior=
        st.booleans(),
    isConjugated=
        st.booleans(),
    isService=
        st.booleans()
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
CompleteDSLPckg::DurationConstraint_strategy = st.builds(
    CompleteDSLPckg::DurationConstraint,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg::TimeConstraint_strategy = st.builds(
    CompleteDSLPckg::TimeConstraint,
    firstEvent=
        st.booleans()
)
Constraint_strategy = st.builds(
    Constraint,
)
CompleteDSLPckg::InteractionConstraint_strategy = st.builds(
    CompleteDSLPckg::InteractionConstraint,
)
CompleteDSLPckg::IntervalConstraint_strategy = st.builds(
    CompleteDSLPckg::IntervalConstraint,
)
Interval_strategy = st.builds(
    Interval,
)
CompleteDSLPckg::DurationInterval_strategy = st.builds(
    CompleteDSLPckg::DurationInterval,
)
CompleteDSLPckg::TimeInterval_strategy = st.builds(
    CompleteDSLPckg::TimeInterval,
)
CompleteDSLPckg::Duration_strategy = st.builds(
    CompleteDSLPckg::Duration,
)
Observation_strategy = st.builds(
    Observation,
)
CompleteDSLPckg::DurationObservation_strategy = st.builds(
    CompleteDSLPckg::DurationObservation,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg::TimeObservation_strategy = st.builds(
    CompleteDSLPckg::TimeObservation,
    firstEvent=
        st.booleans()
)
CompleteDSLPckg::Observation_strategy = st.builds(
    CompleteDSLPckg::Observation,
)
CompleteDSLPckg::TimeExpression_strategy = st.builds(
    CompleteDSLPckg::TimeExpression,
)
CompleteDSLPckg::TimeEvent_strategy = st.builds(
    CompleteDSLPckg::TimeEvent,
    isRelative=
        st.booleans()
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
CompleteDSLPckg::CallEvent_strategy = st.builds(
    CompleteDSLPckg::CallEvent,
)
CompleteDSLPckg::SignalEvent_strategy = st.builds(
    CompleteDSLPckg::SignalEvent,
)
CompleteDSLPckg::AnyReceiveEvent_strategy = st.builds(
    CompleteDSLPckg::AnyReceiveEvent,
)
Event_strategy = st.builds(
    Event,
)
CompleteDSLPckg::ChangeEvent_strategy = st.builds(
    CompleteDSLPckg::ChangeEvent,
)
CompleteDSLPckg::MessageEvent_strategy = st.builds(
    CompleteDSLPckg::MessageEvent,
)
CompleteDSLPckg::Interval_strategy = st.builds(
    CompleteDSLPckg::Interval,
)
CompleteDSLPckg::Trigger_strategy = st.builds(
    CompleteDSLPckg::Trigger,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
CompleteDSLPckg::FunctionBehavior_strategy = st.builds(
    CompleteDSLPckg::FunctionBehavior,
)
Behavior_strategy = st.builds(
    Behavior,
)
CompleteDSLPckg::StateMachine_strategy = st.builds(
    CompleteDSLPckg::StateMachine,
)
CompleteDSLPckg::Activity_strategy = st.builds(
    CompleteDSLPckg::Activity,
    isSingleExecution=
        st.booleans(),
    isReadOnly=
        st.booleans()
)
CompleteDSLPckg::Interaction_strategy = st.builds(
    CompleteDSLPckg::Interaction,
)
CompleteDSLPckg::OpaqueBehavior_strategy = st.builds(
    CompleteDSLPckg::OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
CompleteDSLPckg::Event_strategy = st.builds(
    CompleteDSLPckg::Event,
)
Association_strategy = st.builds(
    Association,
)
CompleteDSLPckg::CommunicationPath_strategy = st.builds(
    CompleteDSLPckg::CommunicationPath,
)
Class_strategy = st.builds(
    Class,
)
CompleteDSLPckg::Behavior_strategy = st.builds(
    CompleteDSLPckg::Behavior,
    isReentrant=
        st.booleans()
)
CompleteDSLPckg::Component_strategy = st.builds(
    CompleteDSLPckg::Component,
    isIndirectlyInstantiated=
        st.booleans()
)
CompleteDSLPckg::AssociationClass_strategy = st.builds(
    CompleteDSLPckg::AssociationClass,
)
Realization_strategy = st.builds(
    Realization,
)
CompleteDSLPckg::ComponentRealization_strategy = st.builds(
    CompleteDSLPckg::ComponentRealization,
)
CompleteDSLPckg::InterfaceRealization_strategy = st.builds(
    CompleteDSLPckg::InterfaceRealization,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
CompleteDSLPckg::Manifestation_strategy = st.builds(
    CompleteDSLPckg::Manifestation,
)
CompleteDSLPckg::Realization_strategy = st.builds(
    CompleteDSLPckg::Realization,
)
Dependency_strategy = st.builds(
    Dependency,
)
CompleteDSLPckg::Deployment_strategy = st.builds(
    CompleteDSLPckg::Deployment,
)
CompleteDSLPckg::Abstraction_strategy = st.builds(
    CompleteDSLPckg::Abstraction,
)
CompleteDSLPckg::Usage_strategy = st.builds(
    CompleteDSLPckg::Usage,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
CompleteDSLPckg::EnumerationLiteral_strategy = st.builds(
    CompleteDSLPckg::EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
CompleteDSLPckg::Enumeration_strategy = st.builds(
    CompleteDSLPckg::Enumeration,
)
CompleteDSLPckg::PrimitiveType_strategy = st.builds(
    CompleteDSLPckg::PrimitiveType,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
CompleteDSLPckg::EncapsulatedClassifier_strategy = st.builds(
    CompleteDSLPckg::EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
CompleteDSLPckg::UseCase_strategy = st.builds(
    CompleteDSLPckg::UseCase,
)
CompleteDSLPckg::Actor_strategy = st.builds(
    CompleteDSLPckg::Actor,
)
CompleteDSLPckg::Collaboration_strategy = st.builds(
    CompleteDSLPckg::Collaboration,
)
Classifier_strategy = st.builds(
    Classifier,
)
CompleteDSLPckg::BehavioredClassifier_strategy = st.builds(
    CompleteDSLPckg::BehavioredClassifier,
)
CompleteDSLPckg::StructuredClassifier_strategy = st.builds(
    CompleteDSLPckg::StructuredClassifier,
)
CompleteDSLPckg::Artifact_strategy = st.builds(
    CompleteDSLPckg::Artifact,
    fileName=
        safe_text
)
CompleteDSLPckg::Signal_strategy = st.builds(
    CompleteDSLPckg::Signal,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
CompleteDSLPckg::Reception_strategy = st.builds(
    CompleteDSLPckg::Reception,
)
CompleteDSLPckg::Operation_strategy = st.builds(
    CompleteDSLPckg::Operation,
    lower=
        st.integers(),
    isOrdered=
        st.booleans(),
    isUnique=
        st.booleans(),
    isQuery=
        st.booleans(),
    upper=
        st.integers()
)
CompleteDSLPckg::Interface_strategy = st.builds(
    CompleteDSLPckg::Interface,
)
CompleteDSLPckg::DataType_strategy = st.builds(
    CompleteDSLPckg::DataType,
)
CompleteDSLPckg::Association_strategy = st.builds(
    CompleteDSLPckg::Association,
    isDerived=
        st.booleans()
)
CompleteDSLPckg::Class_strategy = st.builds(
    CompleteDSLPckg::Class,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
CompleteDSLPckg::Node_strategy = st.builds(
    CompleteDSLPckg::Node,
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
CompleteDSLPckg::Variable_strategy = st.builds(
    CompleteDSLPckg::Variable,
)
CompleteDSLPckg::Pin_strategy = st.builds(
    CompleteDSLPckg::Pin,
)
Feature_strategy = st.builds(
    Feature,
)
CompleteDSLPckg::StructuralFeature_strategy = st.builds(
    CompleteDSLPckg::StructuralFeature,
    isReadOnly=
        st.booleans()
)
CompleteDSLPckg::Connector_strategy = st.builds(
    CompleteDSLPckg::Connector,
    kind=
        safe_text
)
CompleteDSLPckg::BehavioralFeature_strategy = st.builds(
    CompleteDSLPckg::BehavioralFeature,
)
CompleteDSLPckg::CollaborationUse_strategy = st.builds(
    CompleteDSLPckg::CollaborationUse,
)
CompleteDSLPckg::GeneralizationSet_strategy = st.builds(
    CompleteDSLPckg::GeneralizationSet,
    isDisjoint=
        st.booleans(),
    isCovering=
        st.booleans()
)
CompleteDSLPckg::Substitution_strategy = st.builds(
    CompleteDSLPckg::Substitution,
)
CompleteDSLPckg::Generalization_strategy = st.builds(
    CompleteDSLPckg::Generalization,
    isSubstitutable=
        st.booleans()
)
CompleteDSLPckg::Property_strategy = st.builds(
    CompleteDSLPckg::Property,
    isDerived=
        st.booleans(),
    default=
        safe_text,
    isID=
        st.booleans(),
    isComposite=
        st.booleans(),
    isDerivedUnion=
        st.booleans(),
    aggregation=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
CompleteDSLPckg::Classifier_strategy = st.builds(
    CompleteDSLPckg::Classifier,
    isAbstract=
        st.booleans(),
    isFinalSpecialization=
        st.booleans()
)
CompleteDSLPckg::State_strategy = st.builds(
    CompleteDSLPckg::State,
    isComposite=
        st.booleans(),
    isSubmachineState=
        st.booleans(),
    isSimple=
        st.booleans(),
    isOrthogonal=
        st.booleans()
)
CompleteDSLPckg::Feature_strategy = st.builds(
    CompleteDSLPckg::Feature,
    isStatic=
        st.booleans()
)
CompleteDSLPckg::ExtensionPoint_strategy = st.builds(
    CompleteDSLPckg::ExtensionPoint,
)
CompleteDSLPckg::ActivityEdge_strategy = st.builds(
    CompleteDSLPckg::ActivityEdge,
)
CompleteDSLPckg::Transition_strategy = st.builds(
    CompleteDSLPckg::Transition,
    kind=
        safe_text
)
CompleteDSLPckg::Region_strategy = st.builds(
    CompleteDSLPckg::Region,
)
CompleteDSLPckg::ActivityNode_strategy = st.builds(
    CompleteDSLPckg::ActivityNode,
)

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

@given(instance=CompleteDSLPckg::ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_completedslpckg::considerignorefragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ConsiderIgnoreFragment)

@given(instance=CompleteDSLPckg::CombinedFragment_strategy)
@settings(max_examples=50)
def test_completedslpckg::combinedfragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CombinedFragment)

@given(instance=CompleteDSLPckg::CombinedFragment_strategy)
def test_completedslpckg::combinedfragment_interactionOperator_type(instance):
    assert isinstance(instance.interactionOperator, str)


@given(instance=CompleteDSLPckg::CombinedFragment_strategy)
def test_completedslpckg::combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=CompleteDSLPckg::PartDecomposition_strategy)
@settings(max_examples=50)
def test_completedslpckg::partdecomposition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::PartDecomposition)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=CompleteDSLPckg::ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActionExecutionSpecification)

@given(instance=CompleteDSLPckg::BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::BehaviorExecutionSpecification)

@given(instance=MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, MessageOccurrenceSpecification)

@given(instance=CompleteDSLPckg::DestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::destructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DestructionOccurrenceSpecification)

@given(instance=OccurenceSpecification_strategy)
@settings(max_examples=50)
def test_occurencespecification_instantiation(instance):
    assert isinstance(instance, OccurenceSpecification)

@given(instance=CompleteDSLPckg::MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::MessageOccurrenceSpecification)

@given(instance=CompleteDSLPckg::ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExecutionOccurrenceSpecification)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=CompleteDSLPckg::Continuation_strategy)
@settings(max_examples=50)
def test_completedslpckg::continuation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Continuation)

@given(instance=CompleteDSLPckg::Continuation_strategy)
def test_completedslpckg::continuation_setting_type(instance):
    assert isinstance(instance.setting, bool)


@given(instance=CompleteDSLPckg::Continuation_strategy)
def test_completedslpckg::continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=CompleteDSLPckg::InteractionUse_strategy)
@settings(max_examples=50)
def test_completedslpckg::interactionuse_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InteractionUse)

@given(instance=CompleteDSLPckg::OccurenceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::occurencespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::OccurenceSpecification)

@given(instance=CompleteDSLPckg::StateInvariant_strategy)
@settings(max_examples=50)
def test_completedslpckg::stateinvariant_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StateInvariant)

@given(instance=CompleteDSLPckg::ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::executionspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExecutionSpecification)

@given(instance=CompleteDSLPckg::Gate_strategy)
@settings(max_examples=50)
def test_completedslpckg::gate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Gate)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=CompleteDSLPckg::DataStoreNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::datastorenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DataStoreNode)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=CompleteDSLPckg::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_completedslpckg::expansionregion_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExpansionRegion)

@given(instance=CompleteDSLPckg::ExpansionRegion_strategy)
def test_completedslpckg::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=CompleteDSLPckg::ExpansionRegion_strategy)
def test_completedslpckg::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=CompleteDSLPckg::ConditionalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::conditionalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ConditionalNode)

@given(instance=CompleteDSLPckg::ConditionalNode_strategy)
def test_completedslpckg::conditionalnode_isDeterminate_type(instance):
    assert isinstance(instance.isDeterminate, bool)


@given(instance=CompleteDSLPckg::ConditionalNode_strategy)
def test_completedslpckg::conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original

@given(instance=CompleteDSLPckg::ConditionalNode_strategy)
def test_completedslpckg::conditionalnode_isAssumed_type(instance):
    assert isinstance(instance.isAssumed, bool)


@given(instance=CompleteDSLPckg::ConditionalNode_strategy)
def test_completedslpckg::conditionalnode_isAssumed_setter(instance):
    original = instance.isAssumed
    instance.isAssumed = original
    assert instance.isAssumed == original

@given(instance=CompleteDSLPckg::SequenceNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::sequencenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::SequenceNode)

@given(instance=CompleteDSLPckg::LoopNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::loopnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LoopNode)

@given(instance=CompleteDSLPckg::LoopNode_strategy)
def test_completedslpckg::loopnode_isTestedFirst_type(instance):
    assert isinstance(instance.isTestedFirst, bool)


@given(instance=CompleteDSLPckg::LoopNode_strategy)
def test_completedslpckg::loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
@settings(max_examples=50)
def test_completedslpckg::objectflow_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ObjectFlow)

@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_isMultireceive_type(instance):
    assert isinstance(instance.isMultireceive, bool)


@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_isMulticast_type(instance):
    assert isinstance(instance.isMulticast, bool)


@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_isControlType_type(instance):
    assert isinstance(instance.isControlType, bool)


@given(instance=CompleteDSLPckg::ObjectFlow_strategy)
def test_completedslpckg::objectflow_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=CompleteDSLPckg::ControlFlow_strategy)
@settings(max_examples=50)
def test_completedslpckg::controlflow_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ControlFlow)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=CompleteDSLPckg::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::flowfinalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::FlowFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=CompleteDSLPckg::FinalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::finalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::FinalNode)

@given(instance=CompleteDSLPckg::MergeNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::mergenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::MergeNode)

@given(instance=CompleteDSLPckg::DecisionNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::decisionnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DecisionNode)

@given(instance=CompleteDSLPckg::InitialNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::initialnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InitialNode)

@given(instance=CompleteDSLPckg::JoinNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::joinnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::JoinNode)

@given(instance=CompleteDSLPckg::JoinNode_strategy)
def test_completedslpckg::joinnode_isCombineDuplicate_type(instance):
    assert isinstance(instance.isCombineDuplicate, bool)


@given(instance=CompleteDSLPckg::JoinNode_strategy)
def test_completedslpckg::joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=CompleteDSLPckg::ForkNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::forknode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ForkNode)

@given(instance=CompleteDSLPckg::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::activityfinalnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActivityFinalNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=CompleteDSLPckg::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::centralbuffernode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CentralBufferNode)

@given(instance=CompleteDSLPckg::ExpansionNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::expansionnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExpansionNode)

@given(instance=CompleteDSLPckg::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::activityparameternode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActivityParameterNode)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=CompleteDSLPckg::ControlNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::controlnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ControlNode)

@given(instance=CompleteDSLPckg::ExecutableNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::executablenode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExecutableNode)

@given(instance=CompleteDSLPckg::ActivityPartition_strategy)
@settings(max_examples=50)
def test_completedslpckg::activitypartition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActivityPartition)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=CompleteDSLPckg::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_completedslpckg::protocoltransition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ProtocolTransition)

@given(instance=CompleteDSLPckg::InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_completedslpckg::interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InterruptibleActivityRegion)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=CompleteDSLPckg::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_completedslpckg::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ProtocolStateMachine)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=CompleteDSLPckg::FinalState_strategy)
@settings(max_examples=50)
def test_completedslpckg::finalstate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::FinalState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=CompleteDSLPckg::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_completedslpckg::connectionpointreference_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ConnectionPointReference)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=CompleteDSLPckg::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::RemoveVariableValueAction)

@given(instance=CompleteDSLPckg::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AddVariableValueAction)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=CompleteDSLPckg::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::clearvariableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ClearVariableAction)

@given(instance=CompleteDSLPckg::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::writevariableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::WriteVariableAction)

@given(instance=CompleteDSLPckg::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readvariableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadVariableAction)

@given(instance=CompleteDSLPckg::Pseudostate_strategy)
@settings(max_examples=50)
def test_completedslpckg::pseudostate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Pseudostate)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=CompleteDSLPckg::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CreateLinkObjectAction)

@given(instance=CompleteDSLPckg::ReadlsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readlsclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadlsClassifiedObjectAction)

@given(instance=CompleteDSLPckg::InstanceValue_strategy)
@settings(max_examples=50)
def test_completedslpckg::instancevalue_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InstanceValue)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=CompleteDSLPckg::LiteralUnilimitedNatural_strategy)
@settings(max_examples=50)
def test_completedslpckg::literalunilimitednatural_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LiteralUnilimitedNatural)

@given(instance=CompleteDSLPckg::LiteralInteger_strategy)
@settings(max_examples=50)
def test_completedslpckg::literalinteger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LiteralInteger)

@given(instance=CompleteDSLPckg::LiteralString_strategy)
@settings(max_examples=50)
def test_completedslpckg::literalstring_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LiteralString)

@given(instance=CompleteDSLPckg::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_completedslpckg::literalboolean_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LiteralBoolean)

@given(instance=CompleteDSLPckg::LiteralReal_strategy)
@settings(max_examples=50)
def test_completedslpckg::literalreal_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LiteralReal)

@given(instance=CompleteDSLPckg::LiteralNull_strategy)
@settings(max_examples=50)
def test_completedslpckg::literalnull_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LiteralNull)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=CompleteDSLPckg::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::literalspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LiteralSpecification)

@given(instance=CompleteDSLPckg::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_completedslpckg::opaqueexpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::OpaqueExpression)

@given(instance=CompleteDSLPckg::OpaqueExpression_strategy)
def test_completedslpckg::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=CompleteDSLPckg::OpaqueExpression_strategy)
def test_completedslpckg::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=CompleteDSLPckg::OpaqueExpression_strategy)
def test_completedslpckg::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=CompleteDSLPckg::OpaqueExpression_strategy)
def test_completedslpckg::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=CompleteDSLPckg::Expression_strategy)
@settings(max_examples=50)
def test_completedslpckg::expression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Expression)

@given(instance=CompleteDSLPckg::Expression_strategy)
def test_completedslpckg::expression_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=CompleteDSLPckg::Expression_strategy)
def test_completedslpckg::expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=CompleteDSLPckg::Parameter_strategy)
@settings(max_examples=50)
def test_completedslpckg::parameter_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Parameter)

@given(instance=CompleteDSLPckg::Parameter_strategy)
def test_completedslpckg::parameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=CompleteDSLPckg::Parameter_strategy)
def test_completedslpckg::parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CompleteDSLPckg::ObjectNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::objectnode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ObjectNode)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=CompleteDSLPckg::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_completedslpckg::directedrelationship_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DirectedRelationship)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=CompleteDSLPckg::ValueSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::valuespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ValueSpecification)

@given(instance=CompleteDSLPckg::Type_strategy)
@settings(max_examples=50)
def test_completedslpckg::type_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Type)

@given(instance=CompleteDSLPckg::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::instancespecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InstanceSpecification)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=CompleteDSLPckg::InteractionOperand_strategy)
@settings(max_examples=50)
def test_completedslpckg::interactionoperand_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InteractionOperand)

@given(instance=CompleteDSLPckg::Package_strategy)
@settings(max_examples=50)
def test_completedslpckg::package_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Package)

@given(instance=CompleteDSLPckg::Package_strategy)
def test_completedslpckg::package_URI_type(instance):
    assert isinstance(instance.URI, str)


@given(instance=CompleteDSLPckg::Package_strategy)
def test_completedslpckg::package_URI_setter(instance):
    original = instance.URI
    instance.URI = original
    assert instance.URI == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=CompleteDSLPckg::ProtocolConformance_strategy)
@settings(max_examples=50)
def test_completedslpckg::protocolconformance_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ProtocolConformance)

@given(instance=CompleteDSLPckg::PackageMerge_strategy)
@settings(max_examples=50)
def test_completedslpckg::packagemerge_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::PackageMerge)

@given(instance=CompleteDSLPckg::Constraint_strategy)
@settings(max_examples=50)
def test_completedslpckg::constraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Constraint)

@given(instance=CompleteDSLPckg::PackageImport_strategy)
@settings(max_examples=50)
def test_completedslpckg::packageimport_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::PackageImport)

@given(instance=CompleteDSLPckg::PackageImport_strategy)
def test_completedslpckg::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=CompleteDSLPckg::PackageImport_strategy)
def test_completedslpckg::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=CompleteDSLPckg::ElementImport_strategy)
@settings(max_examples=50)
def test_completedslpckg::elementimport_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ElementImport)

@given(instance=CompleteDSLPckg::ElementImport_strategy)
def test_completedslpckg::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=CompleteDSLPckg::ElementImport_strategy)
def test_completedslpckg::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=CompleteDSLPckg::ElementImport_strategy)
def test_completedslpckg::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=CompleteDSLPckg::ElementImport_strategy)
def test_completedslpckg::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=CompleteDSLPckg::Dependency_strategy)
@settings(max_examples=50)
def test_completedslpckg::dependency_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Dependency)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=CompleteDSLPckg::Clause_strategy)
@settings(max_examples=50)
def test_completedslpckg::clause_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Clause)

@given(instance=CompleteDSLPckg::Relationship_strategy)
@settings(max_examples=50)
def test_completedslpckg::relationship_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Relationship)

@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_completedslpckg::multiplicityelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::MultiplicityElement)

@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=CompleteDSLPckg::MultiplicityElement_strategy)
def test_completedslpckg::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=CompleteDSLPckg::Slot_strategy)
@settings(max_examples=50)
def test_completedslpckg::slot_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Slot)

@given(instance=CompleteDSLPckg::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_completedslpckg::exceptionhandler_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExceptionHandler)

@given(instance=CompleteDSLPckg::NamedElement_strategy)
@settings(max_examples=50)
def test_completedslpckg::namedelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::NamedElement)

@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=CompleteDSLPckg::Comment_strategy)
@settings(max_examples=50)
def test_completedslpckg::comment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Comment)

@given(instance=CompleteDSLPckg::Comment_strategy)
def test_completedslpckg::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=CompleteDSLPckg::Comment_strategy)
def test_completedslpckg::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=CompleteDSLPckg::Element_strategy)
@settings(max_examples=50)
def test_completedslpckg::element_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Element)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=CompleteDSLPckg::Lifeline_strategy)
@settings(max_examples=50)
def test_completedslpckg::lifeline_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Lifeline)

@given(instance=CompleteDSLPckg::Include_strategy)
@settings(max_examples=50)
def test_completedslpckg::include_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Include)

@given(instance=CompleteDSLPckg::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_completedslpckg::generalordering_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::GeneralOrdering)

@given(instance=CompleteDSLPckg::Namespace_strategy)
@settings(max_examples=50)
def test_completedslpckg::namespace_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Namespace)

@given(instance=CompleteDSLPckg::ActivityGroup_strategy)
@settings(max_examples=50)
def test_completedslpckg::activitygroup_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActivityGroup)

@given(instance=CompleteDSLPckg::TypedElement_strategy)
@settings(max_examples=50)
def test_completedslpckg::typedelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::TypedElement)

@given(instance=CompleteDSLPckg::Message_strategy)
@settings(max_examples=50)
def test_completedslpckg::message_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Message)

@given(instance=CompleteDSLPckg::Message_strategy)
def test_completedslpckg::message_messageKind_type(instance):
    assert isinstance(instance.messageKind, str)


@given(instance=CompleteDSLPckg::Message_strategy)
def test_completedslpckg::message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original

@given(instance=CompleteDSLPckg::Message_strategy)
def test_completedslpckg::message_messageSort_type(instance):
    assert isinstance(instance.messageSort, str)


@given(instance=CompleteDSLPckg::Message_strategy)
def test_completedslpckg::message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original

@given(instance=CompleteDSLPckg::ParameterSet_strategy)
@settings(max_examples=50)
def test_completedslpckg::parameterset_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ParameterSet)

@given(instance=CompleteDSLPckg::RedefinableElement_strategy)
@settings(max_examples=50)
def test_completedslpckg::redefinableelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::RedefinableElement)

@given(instance=CompleteDSLPckg::RedefinableElement_strategy)
def test_completedslpckg::redefinableelement_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, bool)


@given(instance=CompleteDSLPckg::RedefinableElement_strategy)
def test_completedslpckg::redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=CompleteDSLPckg::InteractionFragment_strategy)
@settings(max_examples=50)
def test_completedslpckg::interactionfragment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InteractionFragment)

@given(instance=CompleteDSLPckg::Vertex_strategy)
@settings(max_examples=50)
def test_completedslpckg::vertex_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Vertex)

@given(instance=CompleteDSLPckg::MessageEnd_strategy)
@settings(max_examples=50)
def test_completedslpckg::messageend_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::MessageEnd)

@given(instance=CompleteDSLPckg::PackageableElement_strategy)
@settings(max_examples=50)
def test_completedslpckg::packageableelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::PackageableElement)

@given(instance=CompleteDSLPckg::Extend_strategy)
@settings(max_examples=50)
def test_completedslpckg::extend_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Extend)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=CompleteDSLPckg::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::acceptcallaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AcceptCallAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=CompleteDSLPckg::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::writelinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::WriteLinkAction)

@given(instance=CompleteDSLPckg::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readlinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadLinkAction)

@given(instance=CompleteDSLPckg::QualifierValue_strategy)
@settings(max_examples=50)
def test_completedslpckg::qualifiervalue_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::QualifierValue)

@given(instance=CompleteDSLPckg::LinkEndData_strategy)
@settings(max_examples=50)
def test_completedslpckg::linkenddata_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LinkEndData)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=CompleteDSLPckg::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::RemoveStructuralFeatureValueAction)

@given(instance=CompleteDSLPckg::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AddStructuralFeatureValueAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=CompleteDSLPckg::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_completedslpckg::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LinkEndDestructionData)

@given(instance=CompleteDSLPckg::LinkEndDestructionData_strategy)
def test_completedslpckg::linkenddestructiondata_isDestroyDuplicates_type(instance):
    assert isinstance(instance.isDestroyDuplicates, bool)


@given(instance=CompleteDSLPckg::LinkEndDestructionData_strategy)
def test_completedslpckg::linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=CompleteDSLPckg::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_completedslpckg::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LinkEndCreationData)

@given(instance=CompleteDSLPckg::LinkEndCreationData_strategy)
def test_completedslpckg::linkendcreationdata_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=CompleteDSLPckg::LinkEndCreationData_strategy)
def test_completedslpckg::linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=CompleteDSLPckg::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::destroylinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DestroyLinkAction)

@given(instance=CompleteDSLPckg::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::createlinkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CreateLinkAction)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=CompleteDSLPckg::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::WriteStructuralFeatureAction)

@given(instance=CompleteDSLPckg::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ClearStructuralFeatureAction)

@given(instance=CompleteDSLPckg::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadStructuralFeatureAction)

@given(instance=CompleteDSLPckg::CallOperationAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::calloperationaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CallOperationAction)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=CompleteDSLPckg::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StartObjectBehaviorAction)

@given(instance=CompleteDSLPckg::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::callbehavioraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CallBehaviorAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=CompleteDSLPckg::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::BroadcastSignalAction)

@given(instance=CompleteDSLPckg::SendSignalAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::sendsignalaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::SendSignalAction)

@given(instance=CompleteDSLPckg::CallAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::callaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CallAction)

@given(instance=CompleteDSLPckg::CallAction_strategy)
def test_completedslpckg::callaction_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, bool)


@given(instance=CompleteDSLPckg::CallAction_strategy)
def test_completedslpckg::callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=CompleteDSLPckg::ActionInputPin_strategy)
@settings(max_examples=50)
def test_completedslpckg::actioninputpin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActionInputPin)

@given(instance=CompleteDSLPckg::ValuePin_strategy)
@settings(max_examples=50)
def test_completedslpckg::valuepin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ValuePin)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=CompleteDSLPckg::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::testidentityaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::TestIdentityAction)

@given(instance=CompleteDSLPckg::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readselfaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadSelfAction)

@given(instance=CompleteDSLPckg::UnmarshallAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::unmarshallaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::UnmarshallAction)

@given(instance=CompleteDSLPckg::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadLinkObjectEndQualifierAction)

@given(instance=CompleteDSLPckg::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::createobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CreateObjectAction)

@given(instance=CompleteDSLPckg::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadLinkObjectEndAction)

@given(instance=CompleteDSLPckg::LinkAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::linkaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::LinkAction)

@given(instance=CompleteDSLPckg::ReplyAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::replyaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReplyAction)

@given(instance=CompleteDSLPckg::VariableAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::variableaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::VariableAction)

@given(instance=CompleteDSLPckg::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ValueSpecificationAction)

@given(instance=CompleteDSLPckg::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DestroyObjectAction)

@given(instance=CompleteDSLPckg::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StartClassifierBehaviorAction)

@given(instance=CompleteDSLPckg::ReadExtendAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::readextendaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReadExtendAction)

@given(instance=CompleteDSLPckg::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::accepteventaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AcceptEventAction)

@given(instance=CompleteDSLPckg::AcceptEventAction_strategy)
def test_completedslpckg::accepteventaction_isUnmarshall_type(instance):
    assert isinstance(instance.isUnmarshall, bool)


@given(instance=CompleteDSLPckg::AcceptEventAction_strategy)
def test_completedslpckg::accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=CompleteDSLPckg::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StructuredActivityNode)

@given(instance=CompleteDSLPckg::StructuredActivityNode_strategy)
def test_completedslpckg::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, bool)


@given(instance=CompleteDSLPckg::StructuredActivityNode_strategy)
def test_completedslpckg::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=CompleteDSLPckg::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::RaiseExceptionAction)

@given(instance=CompleteDSLPckg::ReduceAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::reduceaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReduceAction)

@given(instance=CompleteDSLPckg::ReduceAction_strategy)
def test_completedslpckg::reduceaction_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=CompleteDSLPckg::ReduceAction_strategy)
def test_completedslpckg::reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=CompleteDSLPckg::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ReclassifyObjectAction)

@given(instance=CompleteDSLPckg::ReclassifyObjectAction_strategy)
def test_completedslpckg::reclassifyobjectaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=CompleteDSLPckg::ReclassifyObjectAction_strategy)
def test_completedslpckg::reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=CompleteDSLPckg::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StructuralFeatureAction)

@given(instance=CompleteDSLPckg::OpaqueAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::opaqueaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::OpaqueAction)

@given(instance=CompleteDSLPckg::OpaqueAction_strategy)
def test_completedslpckg::opaqueaction_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=CompleteDSLPckg::OpaqueAction_strategy)
def test_completedslpckg::opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=CompleteDSLPckg::OpaqueAction_strategy)
def test_completedslpckg::opaqueaction_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=CompleteDSLPckg::OpaqueAction_strategy)
def test_completedslpckg::opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=CompleteDSLPckg::SendObjectAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::sendobjectaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::SendObjectAction)

@given(instance=CompleteDSLPckg::InputPin_strategy)
@settings(max_examples=50)
def test_completedslpckg::inputpin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InputPin)

@given(instance=CompleteDSLPckg::Action_strategy)
@settings(max_examples=50)
def test_completedslpckg::action_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Action)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=CompleteDSLPckg::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_completedslpckg::deploymentspecification_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DeploymentSpecification)

@given(instance=CompleteDSLPckg::DeploymentSpecification_strategy)
def test_completedslpckg::deploymentspecification_executionLocation_type(instance):
    assert isinstance(instance.executionLocation, str)


@given(instance=CompleteDSLPckg::DeploymentSpecification_strategy)
def test_completedslpckg::deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original

@given(instance=CompleteDSLPckg::DeploymentSpecification_strategy)
def test_completedslpckg::deploymentspecification_deploymentLocation_type(instance):
    assert isinstance(instance.deploymentLocation, str)


@given(instance=CompleteDSLPckg::DeploymentSpecification_strategy)
def test_completedslpckg::deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=CompleteDSLPckg::DeployedArtifact_strategy)
@settings(max_examples=50)
def test_completedslpckg::deployedartifact_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DeployedArtifact)

@given(instance=CompleteDSLPckg::DeploymentTarget_strategy)
@settings(max_examples=50)
def test_completedslpckg::deploymenttarget_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DeploymentTarget)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=CompleteDSLPckg::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_completedslpckg::executionenvironment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExecutionEnvironment)

@given(instance=CompleteDSLPckg::Device_strategy)
@settings(max_examples=50)
def test_completedslpckg::device_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Device)

@given(instance=CompleteDSLPckg::OutputPin_strategy)
@settings(max_examples=50)
def test_completedslpckg::outputpin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::OutputPin)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=CompleteDSLPckg::InvocationAction_strategy)
@settings(max_examples=50)
def test_completedslpckg::invocationaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InvocationAction)

@given(instance=CompleteDSLPckg::ConnectableElement_strategy)
@settings(max_examples=50)
def test_completedslpckg::connectableelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ConnectableElement)

@given(instance=CompleteDSLPckg::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_completedslpckg::connectorend_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ConnectorEnd)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=CompleteDSLPckg::Port_strategy)
@settings(max_examples=50)
def test_completedslpckg::port_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Port)

@given(instance=CompleteDSLPckg::Port_strategy)
def test_completedslpckg::port_isBehavior_type(instance):
    assert isinstance(instance.isBehavior, bool)


@given(instance=CompleteDSLPckg::Port_strategy)
def test_completedslpckg::port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original

@given(instance=CompleteDSLPckg::Port_strategy)
def test_completedslpckg::port_isConjugated_type(instance):
    assert isinstance(instance.isConjugated, bool)


@given(instance=CompleteDSLPckg::Port_strategy)
def test_completedslpckg::port_isConjugated_setter(instance):
    original = instance.isConjugated
    instance.isConjugated = original
    assert instance.isConjugated == original

@given(instance=CompleteDSLPckg::Port_strategy)
def test_completedslpckg::port_isService_type(instance):
    assert isinstance(instance.isService, bool)


@given(instance=CompleteDSLPckg::Port_strategy)
def test_completedslpckg::port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=CompleteDSLPckg::DurationConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg::durationconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DurationConstraint)

@given(instance=CompleteDSLPckg::DurationConstraint_strategy)
def test_completedslpckg::durationconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, bool)


@given(instance=CompleteDSLPckg::DurationConstraint_strategy)
def test_completedslpckg::durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=CompleteDSLPckg::TimeConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg::timeconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::TimeConstraint)

@given(instance=CompleteDSLPckg::TimeConstraint_strategy)
def test_completedslpckg::timeconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, bool)


@given(instance=CompleteDSLPckg::TimeConstraint_strategy)
def test_completedslpckg::timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=CompleteDSLPckg::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg::interactionconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InteractionConstraint)

@given(instance=CompleteDSLPckg::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_completedslpckg::intervalconstraint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::IntervalConstraint)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=CompleteDSLPckg::DurationInterval_strategy)
@settings(max_examples=50)
def test_completedslpckg::durationinterval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DurationInterval)

@given(instance=CompleteDSLPckg::TimeInterval_strategy)
@settings(max_examples=50)
def test_completedslpckg::timeinterval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::TimeInterval)

@given(instance=CompleteDSLPckg::Duration_strategy)
@settings(max_examples=50)
def test_completedslpckg::duration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Duration)

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=CompleteDSLPckg::DurationObservation_strategy)
@settings(max_examples=50)
def test_completedslpckg::durationobservation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DurationObservation)

@given(instance=CompleteDSLPckg::DurationObservation_strategy)
def test_completedslpckg::durationobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, bool)


@given(instance=CompleteDSLPckg::DurationObservation_strategy)
def test_completedslpckg::durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=CompleteDSLPckg::TimeObservation_strategy)
@settings(max_examples=50)
def test_completedslpckg::timeobservation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::TimeObservation)

@given(instance=CompleteDSLPckg::TimeObservation_strategy)
def test_completedslpckg::timeobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, bool)


@given(instance=CompleteDSLPckg::TimeObservation_strategy)
def test_completedslpckg::timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=CompleteDSLPckg::Observation_strategy)
@settings(max_examples=50)
def test_completedslpckg::observation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Observation)

@given(instance=CompleteDSLPckg::TimeExpression_strategy)
@settings(max_examples=50)
def test_completedslpckg::timeexpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::TimeExpression)

@given(instance=CompleteDSLPckg::TimeEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg::timeevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::TimeEvent)

@given(instance=CompleteDSLPckg::TimeEvent_strategy)
def test_completedslpckg::timeevent_isRelative_type(instance):
    assert isinstance(instance.isRelative, bool)


@given(instance=CompleteDSLPckg::TimeEvent_strategy)
def test_completedslpckg::timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=CompleteDSLPckg::CallEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg::callevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CallEvent)

@given(instance=CompleteDSLPckg::SignalEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg::signalevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::SignalEvent)

@given(instance=CompleteDSLPckg::AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg::anyreceiveevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AnyReceiveEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=CompleteDSLPckg::ChangeEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg::changeevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ChangeEvent)

@given(instance=CompleteDSLPckg::MessageEvent_strategy)
@settings(max_examples=50)
def test_completedslpckg::messageevent_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::MessageEvent)

@given(instance=CompleteDSLPckg::Interval_strategy)
@settings(max_examples=50)
def test_completedslpckg::interval_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Interval)

@given(instance=CompleteDSLPckg::Trigger_strategy)
@settings(max_examples=50)
def test_completedslpckg::trigger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Trigger)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=CompleteDSLPckg::FunctionBehavior_strategy)
@settings(max_examples=50)
def test_completedslpckg::functionbehavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::FunctionBehavior)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=CompleteDSLPckg::StateMachine_strategy)
@settings(max_examples=50)
def test_completedslpckg::statemachine_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StateMachine)

@given(instance=CompleteDSLPckg::Activity_strategy)
@settings(max_examples=50)
def test_completedslpckg::activity_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Activity)

@given(instance=CompleteDSLPckg::Activity_strategy)
def test_completedslpckg::activity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, bool)


@given(instance=CompleteDSLPckg::Activity_strategy)
def test_completedslpckg::activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=CompleteDSLPckg::Activity_strategy)
def test_completedslpckg::activity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=CompleteDSLPckg::Activity_strategy)
def test_completedslpckg::activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=CompleteDSLPckg::Interaction_strategy)
@settings(max_examples=50)
def test_completedslpckg::interaction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Interaction)

@given(instance=CompleteDSLPckg::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_completedslpckg::opaquebehavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::OpaqueBehavior)

@given(instance=CompleteDSLPckg::OpaqueBehavior_strategy)
def test_completedslpckg::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=CompleteDSLPckg::OpaqueBehavior_strategy)
def test_completedslpckg::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=CompleteDSLPckg::OpaqueBehavior_strategy)
def test_completedslpckg::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=CompleteDSLPckg::OpaqueBehavior_strategy)
def test_completedslpckg::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=CompleteDSLPckg::Event_strategy)
@settings(max_examples=50)
def test_completedslpckg::event_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Event)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=CompleteDSLPckg::CommunicationPath_strategy)
@settings(max_examples=50)
def test_completedslpckg::communicationpath_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CommunicationPath)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=CompleteDSLPckg::Behavior_strategy)
@settings(max_examples=50)
def test_completedslpckg::behavior_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Behavior)

@given(instance=CompleteDSLPckg::Behavior_strategy)
def test_completedslpckg::behavior_isReentrant_type(instance):
    assert isinstance(instance.isReentrant, bool)


@given(instance=CompleteDSLPckg::Behavior_strategy)
def test_completedslpckg::behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=CompleteDSLPckg::Component_strategy)
@settings(max_examples=50)
def test_completedslpckg::component_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Component)

@given(instance=CompleteDSLPckg::Component_strategy)
def test_completedslpckg::component_isIndirectlyInstantiated_type(instance):
    assert isinstance(instance.isIndirectlyInstantiated, bool)


@given(instance=CompleteDSLPckg::Component_strategy)
def test_completedslpckg::component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original

@given(instance=CompleteDSLPckg::AssociationClass_strategy)
@settings(max_examples=50)
def test_completedslpckg::associationclass_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AssociationClass)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=CompleteDSLPckg::ComponentRealization_strategy)
@settings(max_examples=50)
def test_completedslpckg::componentrealization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ComponentRealization)

@given(instance=CompleteDSLPckg::InterfaceRealization_strategy)
@settings(max_examples=50)
def test_completedslpckg::interfacerealization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InterfaceRealization)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=CompleteDSLPckg::Manifestation_strategy)
@settings(max_examples=50)
def test_completedslpckg::manifestation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Manifestation)

@given(instance=CompleteDSLPckg::Realization_strategy)
@settings(max_examples=50)
def test_completedslpckg::realization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Realization)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=CompleteDSLPckg::Deployment_strategy)
@settings(max_examples=50)
def test_completedslpckg::deployment_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Deployment)

@given(instance=CompleteDSLPckg::Abstraction_strategy)
@settings(max_examples=50)
def test_completedslpckg::abstraction_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Abstraction)

@given(instance=CompleteDSLPckg::Usage_strategy)
@settings(max_examples=50)
def test_completedslpckg::usage_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Usage)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=CompleteDSLPckg::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_completedslpckg::enumerationliteral_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=CompleteDSLPckg::Enumeration_strategy)
@settings(max_examples=50)
def test_completedslpckg::enumeration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Enumeration)

@given(instance=CompleteDSLPckg::PrimitiveType_strategy)
@settings(max_examples=50)
def test_completedslpckg::primitivetype_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::PrimitiveType)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=CompleteDSLPckg::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_completedslpckg::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::EncapsulatedClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=CompleteDSLPckg::UseCase_strategy)
@settings(max_examples=50)
def test_completedslpckg::usecase_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::UseCase)

@given(instance=CompleteDSLPckg::Actor_strategy)
@settings(max_examples=50)
def test_completedslpckg::actor_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Actor)

@given(instance=CompleteDSLPckg::Collaboration_strategy)
@settings(max_examples=50)
def test_completedslpckg::collaboration_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Collaboration)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=CompleteDSLPckg::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_completedslpckg::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::BehavioredClassifier)

@given(instance=CompleteDSLPckg::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_completedslpckg::structuredclassifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StructuredClassifier)

@given(instance=CompleteDSLPckg::Artifact_strategy)
@settings(max_examples=50)
def test_completedslpckg::artifact_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Artifact)

@given(instance=CompleteDSLPckg::Artifact_strategy)
def test_completedslpckg::artifact_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=CompleteDSLPckg::Artifact_strategy)
def test_completedslpckg::artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=CompleteDSLPckg::Signal_strategy)
@settings(max_examples=50)
def test_completedslpckg::signal_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Signal)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=CompleteDSLPckg::Reception_strategy)
@settings(max_examples=50)
def test_completedslpckg::reception_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Reception)

@given(instance=CompleteDSLPckg::Operation_strategy)
@settings(max_examples=50)
def test_completedslpckg::operation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Operation)

@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, bool)


@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=CompleteDSLPckg::Operation_strategy)
def test_completedslpckg::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=CompleteDSLPckg::Interface_strategy)
@settings(max_examples=50)
def test_completedslpckg::interface_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Interface)

@given(instance=CompleteDSLPckg::DataType_strategy)
@settings(max_examples=50)
def test_completedslpckg::datatype_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::DataType)

@given(instance=CompleteDSLPckg::Association_strategy)
@settings(max_examples=50)
def test_completedslpckg::association_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Association)

@given(instance=CompleteDSLPckg::Association_strategy)
def test_completedslpckg::association_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=CompleteDSLPckg::Association_strategy)
def test_completedslpckg::association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=CompleteDSLPckg::Class_strategy)
@settings(max_examples=50)
def test_completedslpckg::class_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Class)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=CompleteDSLPckg::Node_strategy)
@settings(max_examples=50)
def test_completedslpckg::node_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Node)

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

@given(instance=CompleteDSLPckg::Variable_strategy)
@settings(max_examples=50)
def test_completedslpckg::variable_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Variable)

@given(instance=CompleteDSLPckg::Pin_strategy)
@settings(max_examples=50)
def test_completedslpckg::pin_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Pin)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=CompleteDSLPckg::StructuralFeature_strategy)
@settings(max_examples=50)
def test_completedslpckg::structuralfeature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StructuralFeature)

@given(instance=CompleteDSLPckg::StructuralFeature_strategy)
def test_completedslpckg::structuralfeature_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=CompleteDSLPckg::StructuralFeature_strategy)
def test_completedslpckg::structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=CompleteDSLPckg::Connector_strategy)
@settings(max_examples=50)
def test_completedslpckg::connector_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Connector)

@given(instance=CompleteDSLPckg::Connector_strategy)
def test_completedslpckg::connector_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=CompleteDSLPckg::Connector_strategy)
def test_completedslpckg::connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CompleteDSLPckg::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_completedslpckg::behavioralfeature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::BehavioralFeature)

@given(instance=CompleteDSLPckg::CollaborationUse_strategy)
@settings(max_examples=50)
def test_completedslpckg::collaborationuse_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::CollaborationUse)

@given(instance=CompleteDSLPckg::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_completedslpckg::generalizationset_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::GeneralizationSet)

@given(instance=CompleteDSLPckg::GeneralizationSet_strategy)
def test_completedslpckg::generalizationset_isDisjoint_type(instance):
    assert isinstance(instance.isDisjoint, bool)


@given(instance=CompleteDSLPckg::GeneralizationSet_strategy)
def test_completedslpckg::generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=CompleteDSLPckg::GeneralizationSet_strategy)
def test_completedslpckg::generalizationset_isCovering_type(instance):
    assert isinstance(instance.isCovering, bool)


@given(instance=CompleteDSLPckg::GeneralizationSet_strategy)
def test_completedslpckg::generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=CompleteDSLPckg::Substitution_strategy)
@settings(max_examples=50)
def test_completedslpckg::substitution_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Substitution)

@given(instance=CompleteDSLPckg::Generalization_strategy)
@settings(max_examples=50)
def test_completedslpckg::generalization_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Generalization)

@given(instance=CompleteDSLPckg::Generalization_strategy)
def test_completedslpckg::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, bool)


@given(instance=CompleteDSLPckg::Generalization_strategy)
def test_completedslpckg::generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=CompleteDSLPckg::Property_strategy)
@settings(max_examples=50)
def test_completedslpckg::property_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Property)

@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isID_type(instance):
    assert isinstance(instance.isID, bool)


@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original

@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isDerivedUnion_type(instance):
    assert isinstance(instance.isDerivedUnion, bool)


@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original

@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=CompleteDSLPckg::Property_strategy)
def test_completedslpckg::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=CompleteDSLPckg::Classifier_strategy)
@settings(max_examples=50)
def test_completedslpckg::classifier_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Classifier)

@given(instance=CompleteDSLPckg::Classifier_strategy)
def test_completedslpckg::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=CompleteDSLPckg::Classifier_strategy)
def test_completedslpckg::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=CompleteDSLPckg::Classifier_strategy)
def test_completedslpckg::classifier_isFinalSpecialization_type(instance):
    assert isinstance(instance.isFinalSpecialization, bool)


@given(instance=CompleteDSLPckg::Classifier_strategy)
def test_completedslpckg::classifier_isFinalSpecialization_setter(instance):
    original = instance.isFinalSpecialization
    instance.isFinalSpecialization = original
    assert instance.isFinalSpecialization == original

@given(instance=CompleteDSLPckg::State_strategy)
@settings(max_examples=50)
def test_completedslpckg::state_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::State)

@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, bool)


@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, bool)


@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, bool)


@given(instance=CompleteDSLPckg::State_strategy)
def test_completedslpckg::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=CompleteDSLPckg::Feature_strategy)
@settings(max_examples=50)
def test_completedslpckg::feature_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Feature)

@given(instance=CompleteDSLPckg::Feature_strategy)
def test_completedslpckg::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=CompleteDSLPckg::Feature_strategy)
def test_completedslpckg::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=CompleteDSLPckg::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_completedslpckg::extensionpoint_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ExtensionPoint)

@given(instance=CompleteDSLPckg::ActivityEdge_strategy)
@settings(max_examples=50)
def test_completedslpckg::activityedge_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActivityEdge)

@given(instance=CompleteDSLPckg::Transition_strategy)
@settings(max_examples=50)
def test_completedslpckg::transition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Transition)

@given(instance=CompleteDSLPckg::Transition_strategy)
def test_completedslpckg::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=CompleteDSLPckg::Transition_strategy)
def test_completedslpckg::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CompleteDSLPckg::Region_strategy)
@settings(max_examples=50)
def test_completedslpckg::region_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Region)

@given(instance=CompleteDSLPckg::ActivityNode_strategy)
@settings(max_examples=50)
def test_completedslpckg::activitynode_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ActivityNode)

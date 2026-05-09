import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transition,
    uml3::0::0::ProtocolTransition,
    VariableAction,
    uml3::0::0::WriteVariableAction,
    uml3::0::0::ClearVariableAction,
    uml3::0::0::ReadVariableAction,
    State,
    uml3::0::0::FinalState,
    Observation,
    uml3::0::0::DurationObservation,
    uml3::0::0::TimeObservation,
    IntervalConstraint,
    uml3::0::0::DurationConstraint,
    uml3::0::0::TimeConstraint,
    Interval,
    uml3::0::0::TimeInterval,
    uml3::0::0::DurationInterval,
    WriteLinkAction,
    uml3::0::0::CreateLinkAction,
    LinkEndData,
    uml3::0::0::LinkEndCreationData,
    uml3::0::0::LinkEndDestructionData,
    uml3::0::0::DestroyLinkAction,
    LinkAction,
    uml3::0::0::WriteLinkAction,
    uml3::0::0::ReadLinkAction,
    WriteStructuralFeatureAction,
    uml3::0::0::AddStructuralFeatureValueAction,
    uml3::0::0::RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    uml3::0::0::WriteStructuralFeatureAction,
    uml3::0::0::ClearStructuralFeatureAction,
    uml3::0::0::ReadStructuralFeatureAction,
    CombinedFragment,
    uml3::0::0::ConsiderIgnoreFragment,
    Node,
    uml3::0::0::ExecutionEnvironment,
    uml3::0::0::Device,
    FinalNode,
    uml3::0::0::ActivityFinalNode,
    uml3::0::0::FlowFinalNode,
    OccurrenceSpecification,
    uml3::0::0::ExecutionOccurrenceSpecification,
    MessageEvent,
    uml3::0::0::SignalEvent,
    uml3::0::0::SendSignalEvent,
    uml3::0::0::CallEvent,
    uml3::0::0::ReceiveOperationEvent,
    uml3::0::0::AnyReceiveEvent,
    uml3::0::0::ReceiveSignalEvent,
    uml3::0::0::SendOperationEvent,
    Event,
    uml3::0::0::CreationEvent,
    uml3::0::0::ChangeEvent,
    uml3::0::0::TimeEvent,
    uml3::0::0::DestructionEvent,
    uml3::0::0::MessageEvent,
    uml3::0::0::ExecutionEvent,
    ExecutionSpecification,
    uml3::0::0::BehaviorExecutionSpecification,
    uml3::0::0::ActionExecutionSpecification,
    InteractionUse,
    Constraint,
    uml3::0::0::IntervalConstraint,
    uml3::0::0::PartDecomposition,
    uml3::0::0::InteractionConstraint,
    MessageEnd,
    uml3::0::0::MessageOccurrenceSpecification,
    InteractionFragment,
    uml3::0::0::StateInvariant,
    uml3::0::0::Continuation,
    uml3::0::0::InteractionUse,
    uml3::0::0::OccurrenceSpecification,
    uml3::0::0::CombinedFragment,
    uml3::0::0::ExecutionSpecification,
    uml3::0::0::Gate,
    InputPin,
    uml3::0::0::ActionInputPin,
    uml3::0::0::ValuePin,
    ControlNode,
    uml3::0::0::FinalNode,
    uml3::0::0::ForkNode,
    uml3::0::0::DecisionNode,
    uml3::0::0::MergeNode,
    uml3::0::0::InitialNode,
    ActivityEdge,
    uml3::0::0::ObjectFlow,
    uml3::0::0::ControlFlow,
    StructuredActivityNode,
    uml3::0::0::ExpansionRegion,
    uml3::0::0::LoopNode,
    uml3::0::0::SequenceNode,
    CallAction,
    uml3::0::0::CallBehaviorAction,
    uml3::0::0::CallOperationAction,
    InvocationAction,
    uml3::0::0::SendObjectAction,
    uml3::0::0::BroadcastSignalAction,
    uml3::0::0::SendSignalAction,
    uml3::0::0::CallAction,
    ObjectNode,
    uml3::0::0::CentralBufferNode,
    uml3::0::0::ExpansionNode,
    uml3::0::0::ActivityParameterNode,
    Pin,
    ActivityGroup,
    uml3::0::0::InterruptibleActivityRegion,
    ActivityNode,
    uml3::0::0::ControlNode,
    uml3::0::0::ExecutableNode,
    ExecutableNode,
    uml3::0::0::Action,
    uml3::0::0::OutputPin,
    uml3::0::0::InputPin,
    Action,
    uml3::0::0::ReadSelfAction,
    uml3::0::0::VariableAction,
    uml3::0::0::ClearAssociationAction,
    uml3::0::0::ValueSpecificationAction,
    uml3::0::0::TestIdentityAction,
    uml3::0::0::StructuralFeatureAction,
    uml3::0::0::DestroyObjectAction,
    uml3::0::0::CreateObjectAction,
    uml3::0::0::RaiseExceptionAction,
    uml3::0::0::InvocationAction,
    uml3::0::0::LinkAction,
    uml3::0::0::OpaqueAction,
    OpaqueBehavior,
    uml3::0::0::FunctionBehavior,
    LiteralSpecification,
    uml3::0::0::LiteralUnlimitedNatural,
    uml3::0::0::LiteralBoolean,
    uml3::0::0::LiteralString,
    uml3::0::0::LiteralNull,
    uml3::0::0::LiteralInteger,
    InstanceSpecification,
    uml3::0::0::EnumerationLiteral,
    DataType,
    uml3::0::0::PrimitiveType,
    uml3::0::0::Enumeration,
    Expression,
    TemplateSignature,
    TemplateParameter,
    uml3::0::0::ConnectableElementTemplateParameter,
    uml3::0::0::ClassifierTemplateParameter,
    uml3::0::0::OperationTemplateParameter,
    StructuredClassifier,
    uml3::0::0::EncapsulatedClassifier,
    Package,
    uml3::0::0::Model,
    uml3::0::0::Profile,
    Association,
    uml3::0::0::CommunicationPath,
    Vertex,
    uml3::0::0::ConnectionPointReference,
    Property,
    uml3::0::0::ExtensionEnd,
    uml3::0::0::Port,
    uml3::0::0::Pseudostate,
    Behavior,
    uml3::0::0::Interaction,
    uml3::0::0::OpaqueBehavior,
    uml3::0::0::Activity,
    uml3::0::0::StateMachine,
    StateMachine,
    uml3::0::0::ProtocolStateMachine,
    uml3::0::0::Extension,
    BehavioredClassifier,
    uml3::0::0::Actor,
    uml3::0::0::Collaboration,
    EncapsulatedClassifier,
    Class,
    uml3::0::0::Component,
    uml3::0::0::Stereotype,
    uml3::0::0::AssociationClass,
    Feature,
    uml3::0::0::Connector,
    BehavioralFeature,
    uml3::0::0::Reception,
    DeployedArtifact,
    Artifact,
    uml3::0::0::DeploymentSpecification,
    uml3::0::0::Class,
    DeploymentTarget,
    uml3::0::0::Node,
    StructuralFeature,
    ValueSpecification,
    uml3::0::0::TimeExpression,
    uml3::0::0::InstanceValue,
    uml3::0::0::Duration,
    uml3::0::0::LiteralSpecification,
    uml3::0::0::Expression,
    uml3::0::0::Interval,
    uml3::0::0::OpaqueExpression,
    Dependency,
    uml3::0::0::Usage,
    uml3::0::0::Deployment,
    uml3::0::0::Abstraction,
    Abstraction,
    uml3::0::0::Manifestation,
    uml3::0::0::Realization,
    MultiplicityElement,
    uml3::0::0::Pin,
    uml3::0::0::ConnectorEnd,
    ConnectableElement,
    uml3::0::0::Variable,
    uml3::0::0::ConditionalNode,
    CentralBufferNode,
    uml3::0::0::DataStoreNode,
    uml3::0::0::JoinNode,
    uml3::0::0::StartObjectBehaviorAction,
    uml3::0::0::ReduceAction,
    uml3::0::0::UnmarshallAction,
    uml3::0::0::ReplyAction,
    AcceptEventAction,
    uml3::0::0::AcceptCallAction,
    uml3::0::0::ReadLinkObjectEndAction,
    uml3::0::0::AcceptEventAction,
    CreateLinkAction,
    uml3::0::0::CreateLinkObjectAction,
    uml3::0::0::ReadLinkObjectEndQualifierAction,
    uml3::0::0::StartClassifierBehaviorAction,
    uml3::0::0::ReadIsClassifiedObjectAction,
    uml3::0::0::ReclassifyObjectAction,
    uml3::0::0::ReadExtentAction,
    WriteVariableAction,
    uml3::0::0::RemoveVariableValueAction,
    uml3::0::0::AddVariableValueAction,
    DirectedRelationship,
    uml3::0::0::ProtocolConformance,
    uml3::0::0::PackageImport,
    uml3::0::0::ElementImport,
    Relationship,
    uml3::0::0::DirectedRelationship,
    EModelElement,
    ParameterableElement,
    NamedElement,
    uml3::0::0::MessageEnd,
    uml3::0::0::Namespace,
    uml3::0::0::DeploymentTarget,
    uml3::0::0::ActivityPartition,
    uml3::0::0::Lifeline,
    uml3::0::0::Include,
    uml3::0::0::Message,
    uml3::0::0::InteractionFragment,
    uml3::0::0::ParameterSet,
    uml3::0::0::GeneralOrdering,
    uml3::0::0::DeployedArtifact,
    uml3::0::0::Vertex,
    uml3::0::0::Trigger,
    uml3::0::0::Extend,
    uml3::0::0::ProfileApplication,
    uml3::0::0::PackageableElement,
    uml3::0::0::PackageMerge,
    TemplateableElement,
    uml3::0::0::StringExpression,
    uml3::0::0::Operation,
    PackageableElement,
    uml3::0::0::InformationFlow,
    uml3::0::0::InstanceSpecification,
    uml3::0::0::Constraint,
    uml3::0::0::Observation,
    uml3::0::0::Event,
    uml3::0::0::Type,
    uml3::0::0::Dependency,
    Namespace,
    uml3::0::0::InteractionOperand,
    uml3::0::0::BehavioralFeature,
    uml3::0::0::StructuredActivityNode,
    uml3::0::0::Package,
    uml3::0::0::Element,
    Element,
    uml3::0::0::Relationship,
    uml3::0::0::ActivityGroup,
    uml3::0::0::Image,
    uml3::0::0::LinkEndData,
    uml3::0::0::NamedElement,
    uml3::0::0::Slot,
    uml3::0::0::Clause,
    uml3::0::0::ExceptionHandler,
    uml3::0::0::QualifierValue,
    uml3::0::0::MultiplicityElement,
    uml3::0::0::Comment,
    uml3::0::0::Behavior,
    uml3::0::0::Parameter,
    Realization,
    uml3::0::0::ComponentRealization,
    uml3::0::0::InterfaceRealization,
    uml3::0::0::RedefinableElement,
    uml3::0::0::ParameterableElement,
    uml3::0::0::TemplateParameter,
    uml3::0::0::TemplateParameterSubstitution,
    uml3::0::0::TemplateSignature,
    uml3::0::0::TemplateBinding,
    uml3::0::0::TemplateableElement,
    uml3::0::0::Property,
    Classifier,
    uml3::0::0::InformationItem,
    uml3::0::0::Signal,
    uml3::0::0::DataType,
    uml3::0::0::Artifact,
    uml3::0::0::Interface,
    uml3::0::0::StructuredClassifier,
    uml3::0::0::BehavioredClassifier,
    uml3::0::0::Association,
    uml3::0::0::UseCase,
    uml3::0::0::CollaborationUse,
    uml3::0::0::Substitution,
    uml3::0::0::GeneralizationSet,
    uml3::0::0::Generalization,
    Type,
    RedefinableElement,
    uml3::0::0::ActivityEdge,
    uml3::0::0::Region,
    uml3::0::0::ActivityNode,
    uml3::0::0::RedefinableTemplateSignature,
    uml3::0::0::State,
    uml3::0::0::Transition,
    uml3::0::0::ExtensionPoint,
    uml3::0::0::Feature,
    uml3::0::0::Classifier,
    uml3::0::0::TypedElement,
    TypedElement,
    uml3::0::0::ObjectNode,
    uml3::0::0::StructuralFeature,
    uml3::0::0::ConnectableElement,
    uml3::0::0::ValueSpecification,
    ParameterDirectionKind,
    ParameterEffectKind,
    ExpansionKind,
    CallConcurrencyKind,
    InteractionOperatorKind,
    MessageSort,
    ConnectorKind,
    TransitionKind,
    ObjectNodeOrderingKind,
    VisibilityKind,
    MessageKind,
    AggregationKind,
    PseudostateKind,
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



def test_uml3::0::0::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ProtocolTransition)


def test_uml3::0::0::protocoltransition_constructor_exists():
    assert callable(uml3::0::0::ProtocolTransition.__init__)


def test_uml3::0::0::protocoltransition_constructor_args():
    sig = inspect.signature(uml3::0::0::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::WriteVariableAction)


def test_uml3::0::0::writevariableaction_constructor_exists():
    assert callable(uml3::0::0::WriteVariableAction.__init__)


def test_uml3::0::0::writevariableaction_constructor_args():
    sig = inspect.signature(uml3::0::0::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ClearVariableAction)


def test_uml3::0::0::clearvariableaction_constructor_exists():
    assert callable(uml3::0::0::ClearVariableAction.__init__)


def test_uml3::0::0::clearvariableaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadVariableAction)


def test_uml3::0::0::readvariableaction_constructor_exists():
    assert callable(uml3::0::0::ReadVariableAction.__init__)


def test_uml3::0::0::readvariableaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::finalstate_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::FinalState)


def test_uml3::0::0::finalstate_constructor_exists():
    assert callable(uml3::0::0::FinalState.__init__)


def test_uml3::0::0::finalstate_constructor_args():
    sig = inspect.signature(uml3::0::0::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::durationobservation_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DurationObservation)


def test_uml3::0::0::durationobservation_constructor_exists():
    assert callable(uml3::0::0::DurationObservation.__init__)


def test_uml3::0::0::durationobservation_constructor_args():
    sig = inspect.signature(uml3::0::0::DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3::0::0::durationobservation_has_firstEvent():
    assert hasattr(uml3::0::0::DurationObservation, "firstEvent")
    descriptor = None
    for klass in uml3::0::0::DurationObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::timeobservation_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TimeObservation)


def test_uml3::0::0::timeobservation_constructor_exists():
    assert callable(uml3::0::0::TimeObservation.__init__)


def test_uml3::0::0::timeobservation_constructor_args():
    sig = inspect.signature(uml3::0::0::TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3::0::0::timeobservation_has_firstEvent():
    assert hasattr(uml3::0::0::TimeObservation, "firstEvent")
    descriptor = None
    for klass in uml3::0::0::TimeObservation.__mro__:
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



def test_uml3::0::0::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DurationConstraint)


def test_uml3::0::0::durationconstraint_constructor_exists():
    assert callable(uml3::0::0::DurationConstraint.__init__)


def test_uml3::0::0::durationconstraint_constructor_args():
    sig = inspect.signature(uml3::0::0::DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3::0::0::durationconstraint_has_firstEvent():
    assert hasattr(uml3::0::0::DurationConstraint, "firstEvent")
    descriptor = None
    for klass in uml3::0::0::DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TimeConstraint)


def test_uml3::0::0::timeconstraint_constructor_exists():
    assert callable(uml3::0::0::TimeConstraint.__init__)


def test_uml3::0::0::timeconstraint_constructor_args():
    sig = inspect.signature(uml3::0::0::TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml3::0::0::timeconstraint_has_firstEvent():
    assert hasattr(uml3::0::0::TimeConstraint, "firstEvent")
    descriptor = None
    for klass in uml3::0::0::TimeConstraint.__mro__:
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



def test_uml3::0::0::timeinterval_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TimeInterval)


def test_uml3::0::0::timeinterval_constructor_exists():
    assert callable(uml3::0::0::TimeInterval.__init__)


def test_uml3::0::0::timeinterval_constructor_args():
    sig = inspect.signature(uml3::0::0::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::durationinterval_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DurationInterval)


def test_uml3::0::0::durationinterval_constructor_exists():
    assert callable(uml3::0::0::DurationInterval.__init__)


def test_uml3::0::0::durationinterval_constructor_args():
    sig = inspect.signature(uml3::0::0::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CreateLinkAction)


def test_uml3::0::0::createlinkaction_constructor_exists():
    assert callable(uml3::0::0::CreateLinkAction.__init__)


def test_uml3::0::0::createlinkaction_constructor_args():
    sig = inspect.signature(uml3::0::0::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LinkEndCreationData)


def test_uml3::0::0::linkendcreationdata_constructor_exists():
    assert callable(uml3::0::0::LinkEndCreationData.__init__)


def test_uml3::0::0::linkendcreationdata_constructor_args():
    sig = inspect.signature(uml3::0::0::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3::0::0::linkendcreationdata_has_isReplaceAll():
    assert hasattr(uml3::0::0::LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in uml3::0::0::LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LinkEndDestructionData)


def test_uml3::0::0::linkenddestructiondata_constructor_exists():
    assert callable(uml3::0::0::LinkEndDestructionData.__init__)


def test_uml3::0::0::linkenddestructiondata_constructor_args():
    sig = inspect.signature(uml3::0::0::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_uml3::0::0::linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(uml3::0::0::LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in uml3::0::0::LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DestroyLinkAction)


def test_uml3::0::0::destroylinkaction_constructor_exists():
    assert callable(uml3::0::0::DestroyLinkAction.__init__)


def test_uml3::0::0::destroylinkaction_constructor_args():
    sig = inspect.signature(uml3::0::0::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::WriteLinkAction)


def test_uml3::0::0::writelinkaction_constructor_exists():
    assert callable(uml3::0::0::WriteLinkAction.__init__)


def test_uml3::0::0::writelinkaction_constructor_args():
    sig = inspect.signature(uml3::0::0::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadLinkAction)


def test_uml3::0::0::readlinkaction_constructor_exists():
    assert callable(uml3::0::0::ReadLinkAction.__init__)


def test_uml3::0::0::readlinkaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::AddStructuralFeatureValueAction)


def test_uml3::0::0::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml3::0::0::AddStructuralFeatureValueAction.__init__)


def test_uml3::0::0::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml3::0::0::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3::0::0::addstructuralfeaturevalueaction_has_isReplaceAll():
    assert hasattr(uml3::0::0::AddStructuralFeatureValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml3::0::0::AddStructuralFeatureValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::RemoveStructuralFeatureValueAction)


def test_uml3::0::0::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml3::0::0::RemoveStructuralFeatureValueAction.__init__)


def test_uml3::0::0::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml3::0::0::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml3::0::0::removestructuralfeaturevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml3::0::0::RemoveStructuralFeatureValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml3::0::0::RemoveStructuralFeatureValueAction.__mro__:
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



def test_uml3::0::0::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::WriteStructuralFeatureAction)


def test_uml3::0::0::writestructuralfeatureaction_constructor_exists():
    assert callable(uml3::0::0::WriteStructuralFeatureAction.__init__)


def test_uml3::0::0::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3::0::0::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ClearStructuralFeatureAction)


def test_uml3::0::0::clearstructuralfeatureaction_constructor_exists():
    assert callable(uml3::0::0::ClearStructuralFeatureAction.__init__)


def test_uml3::0::0::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadStructuralFeatureAction)


def test_uml3::0::0::readstructuralfeatureaction_constructor_exists():
    assert callable(uml3::0::0::ReadStructuralFeatureAction.__init__)


def test_uml3::0::0::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ConsiderIgnoreFragment)


def test_uml3::0::0::considerignorefragment_constructor_exists():
    assert callable(uml3::0::0::ConsiderIgnoreFragment.__init__)


def test_uml3::0::0::considerignorefragment_constructor_args():
    sig = inspect.signature(uml3::0::0::ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExecutionEnvironment)


def test_uml3::0::0::executionenvironment_constructor_exists():
    assert callable(uml3::0::0::ExecutionEnvironment.__init__)


def test_uml3::0::0::executionenvironment_constructor_args():
    sig = inspect.signature(uml3::0::0::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::device_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Device)


def test_uml3::0::0::device_constructor_exists():
    assert callable(uml3::0::0::Device.__init__)


def test_uml3::0::0::device_constructor_args():
    sig = inspect.signature(uml3::0::0::Device.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActivityFinalNode)


def test_uml3::0::0::activityfinalnode_constructor_exists():
    assert callable(uml3::0::0::ActivityFinalNode.__init__)


def test_uml3::0::0::activityfinalnode_constructor_args():
    sig = inspect.signature(uml3::0::0::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::FlowFinalNode)


def test_uml3::0::0::flowfinalnode_constructor_exists():
    assert callable(uml3::0::0::FlowFinalNode.__init__)


def test_uml3::0::0::flowfinalnode_constructor_args():
    sig = inspect.signature(uml3::0::0::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExecutionOccurrenceSpecification)


def test_uml3::0::0::executionoccurrencespecification_constructor_exists():
    assert callable(uml3::0::0::ExecutionOccurrenceSpecification.__init__)


def test_uml3::0::0::executionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml3::0::0::ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::signalevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::SignalEvent)


def test_uml3::0::0::signalevent_constructor_exists():
    assert callable(uml3::0::0::SignalEvent.__init__)


def test_uml3::0::0::signalevent_constructor_args():
    sig = inspect.signature(uml3::0::0::SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::sendsignalevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::SendSignalEvent)


def test_uml3::0::0::sendsignalevent_constructor_exists():
    assert callable(uml3::0::0::SendSignalEvent.__init__)


def test_uml3::0::0::sendsignalevent_constructor_args():
    sig = inspect.signature(uml3::0::0::SendSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::callevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CallEvent)


def test_uml3::0::0::callevent_constructor_exists():
    assert callable(uml3::0::0::CallEvent.__init__)


def test_uml3::0::0::callevent_constructor_args():
    sig = inspect.signature(uml3::0::0::CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::receiveoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReceiveOperationEvent)


def test_uml3::0::0::receiveoperationevent_constructor_exists():
    assert callable(uml3::0::0::ReceiveOperationEvent.__init__)


def test_uml3::0::0::receiveoperationevent_constructor_args():
    sig = inspect.signature(uml3::0::0::ReceiveOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::AnyReceiveEvent)


def test_uml3::0::0::anyreceiveevent_constructor_exists():
    assert callable(uml3::0::0::AnyReceiveEvent.__init__)


def test_uml3::0::0::anyreceiveevent_constructor_args():
    sig = inspect.signature(uml3::0::0::AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::receivesignalevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReceiveSignalEvent)


def test_uml3::0::0::receivesignalevent_constructor_exists():
    assert callable(uml3::0::0::ReceiveSignalEvent.__init__)


def test_uml3::0::0::receivesignalevent_constructor_args():
    sig = inspect.signature(uml3::0::0::ReceiveSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::sendoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::SendOperationEvent)


def test_uml3::0::0::sendoperationevent_constructor_exists():
    assert callable(uml3::0::0::SendOperationEvent.__init__)


def test_uml3::0::0::sendoperationevent_constructor_args():
    sig = inspect.signature(uml3::0::0::SendOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::creationevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CreationEvent)


def test_uml3::0::0::creationevent_constructor_exists():
    assert callable(uml3::0::0::CreationEvent.__init__)


def test_uml3::0::0::creationevent_constructor_args():
    sig = inspect.signature(uml3::0::0::CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::changeevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ChangeEvent)


def test_uml3::0::0::changeevent_constructor_exists():
    assert callable(uml3::0::0::ChangeEvent.__init__)


def test_uml3::0::0::changeevent_constructor_args():
    sig = inspect.signature(uml3::0::0::ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::timeevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TimeEvent)


def test_uml3::0::0::timeevent_constructor_exists():
    assert callable(uml3::0::0::TimeEvent.__init__)


def test_uml3::0::0::timeevent_constructor_args():
    sig = inspect.signature(uml3::0::0::TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_uml3::0::0::timeevent_has_isRelative():
    assert hasattr(uml3::0::0::TimeEvent, "isRelative")
    descriptor = None
    for klass in uml3::0::0::TimeEvent.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::destructionevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DestructionEvent)


def test_uml3::0::0::destructionevent_constructor_exists():
    assert callable(uml3::0::0::DestructionEvent.__init__)


def test_uml3::0::0::destructionevent_constructor_args():
    sig = inspect.signature(uml3::0::0::DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::messageevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::MessageEvent)


def test_uml3::0::0::messageevent_constructor_exists():
    assert callable(uml3::0::0::MessageEvent.__init__)


def test_uml3::0::0::messageevent_constructor_args():
    sig = inspect.signature(uml3::0::0::MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::executionevent_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExecutionEvent)


def test_uml3::0::0::executionevent_constructor_exists():
    assert callable(uml3::0::0::ExecutionEvent.__init__)


def test_uml3::0::0::executionevent_constructor_args():
    sig = inspect.signature(uml3::0::0::ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::BehaviorExecutionSpecification)


def test_uml3::0::0::behaviorexecutionspecification_constructor_exists():
    assert callable(uml3::0::0::BehaviorExecutionSpecification.__init__)


def test_uml3::0::0::behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml3::0::0::BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActionExecutionSpecification)


def test_uml3::0::0::actionexecutionspecification_constructor_exists():
    assert callable(uml3::0::0::ActionExecutionSpecification.__init__)


def test_uml3::0::0::actionexecutionspecification_constructor_args():
    sig = inspect.signature(uml3::0::0::ActionExecutionSpecification.__init__)
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



def test_uml3::0::0::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::IntervalConstraint)


def test_uml3::0::0::intervalconstraint_constructor_exists():
    assert callable(uml3::0::0::IntervalConstraint.__init__)


def test_uml3::0::0::intervalconstraint_constructor_args():
    sig = inspect.signature(uml3::0::0::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::partdecomposition_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::PartDecomposition)


def test_uml3::0::0::partdecomposition_constructor_exists():
    assert callable(uml3::0::0::PartDecomposition.__init__)


def test_uml3::0::0::partdecomposition_constructor_args():
    sig = inspect.signature(uml3::0::0::PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InteractionConstraint)


def test_uml3::0::0::interactionconstraint_constructor_exists():
    assert callable(uml3::0::0::InteractionConstraint.__init__)


def test_uml3::0::0::interactionconstraint_constructor_args():
    sig = inspect.signature(uml3::0::0::InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::MessageOccurrenceSpecification)


def test_uml3::0::0::messageoccurrencespecification_constructor_exists():
    assert callable(uml3::0::0::MessageOccurrenceSpecification.__init__)


def test_uml3::0::0::messageoccurrencespecification_constructor_args():
    sig = inspect.signature(uml3::0::0::MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::stateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StateInvariant)


def test_uml3::0::0::stateinvariant_constructor_exists():
    assert callable(uml3::0::0::StateInvariant.__init__)


def test_uml3::0::0::stateinvariant_constructor_args():
    sig = inspect.signature(uml3::0::0::StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::continuation_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Continuation)


def test_uml3::0::0::continuation_constructor_exists():
    assert callable(uml3::0::0::Continuation.__init__)


def test_uml3::0::0::continuation_constructor_args():
    sig = inspect.signature(uml3::0::0::Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_uml3::0::0::continuation_has_setting():
    assert hasattr(uml3::0::0::Continuation, "setting")
    descriptor = None
    for klass in uml3::0::0::Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::interactionuse_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InteractionUse)


def test_uml3::0::0::interactionuse_constructor_exists():
    assert callable(uml3::0::0::InteractionUse.__init__)


def test_uml3::0::0::interactionuse_constructor_args():
    sig = inspect.signature(uml3::0::0::InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::OccurrenceSpecification)


def test_uml3::0::0::occurrencespecification_constructor_exists():
    assert callable(uml3::0::0::OccurrenceSpecification.__init__)


def test_uml3::0::0::occurrencespecification_constructor_args():
    sig = inspect.signature(uml3::0::0::OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CombinedFragment)


def test_uml3::0::0::combinedfragment_constructor_exists():
    assert callable(uml3::0::0::CombinedFragment.__init__)


def test_uml3::0::0::combinedfragment_constructor_args():
    sig = inspect.signature(uml3::0::0::CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_uml3::0::0::combinedfragment_has_interactionOperator():
    assert hasattr(uml3::0::0::CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in uml3::0::0::CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::executionspecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExecutionSpecification)


def test_uml3::0::0::executionspecification_constructor_exists():
    assert callable(uml3::0::0::ExecutionSpecification.__init__)


def test_uml3::0::0::executionspecification_constructor_args():
    sig = inspect.signature(uml3::0::0::ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::gate_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Gate)


def test_uml3::0::0::gate_constructor_exists():
    assert callable(uml3::0::0::Gate.__init__)


def test_uml3::0::0::gate_constructor_args():
    sig = inspect.signature(uml3::0::0::Gate.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::actioninputpin_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActionInputPin)


def test_uml3::0::0::actioninputpin_constructor_exists():
    assert callable(uml3::0::0::ActionInputPin.__init__)


def test_uml3::0::0::actioninputpin_constructor_args():
    sig = inspect.signature(uml3::0::0::ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::valuepin_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ValuePin)


def test_uml3::0::0::valuepin_constructor_exists():
    assert callable(uml3::0::0::ValuePin.__init__)


def test_uml3::0::0::valuepin_constructor_args():
    sig = inspect.signature(uml3::0::0::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::finalnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::FinalNode)


def test_uml3::0::0::finalnode_constructor_exists():
    assert callable(uml3::0::0::FinalNode.__init__)


def test_uml3::0::0::finalnode_constructor_args():
    sig = inspect.signature(uml3::0::0::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::forknode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ForkNode)


def test_uml3::0::0::forknode_constructor_exists():
    assert callable(uml3::0::0::ForkNode.__init__)


def test_uml3::0::0::forknode_constructor_args():
    sig = inspect.signature(uml3::0::0::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::decisionnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DecisionNode)


def test_uml3::0::0::decisionnode_constructor_exists():
    assert callable(uml3::0::0::DecisionNode.__init__)


def test_uml3::0::0::decisionnode_constructor_args():
    sig = inspect.signature(uml3::0::0::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::mergenode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::MergeNode)


def test_uml3::0::0::mergenode_constructor_exists():
    assert callable(uml3::0::0::MergeNode.__init__)


def test_uml3::0::0::mergenode_constructor_args():
    sig = inspect.signature(uml3::0::0::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::initialnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InitialNode)


def test_uml3::0::0::initialnode_constructor_exists():
    assert callable(uml3::0::0::InitialNode.__init__)


def test_uml3::0::0::initialnode_constructor_args():
    sig = inspect.signature(uml3::0::0::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::objectflow_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ObjectFlow)


def test_uml3::0::0::objectflow_constructor_exists():
    assert callable(uml3::0::0::ObjectFlow.__init__)


def test_uml3::0::0::objectflow_constructor_args():
    sig = inspect.signature(uml3::0::0::ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"

def test_uml3::0::0::objectflow_has_isMulticast():
    assert hasattr(uml3::0::0::ObjectFlow, "isMulticast")
    descriptor = None
    for klass in uml3::0::0::ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::objectflow_has_isMultireceive():
    assert hasattr(uml3::0::0::ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in uml3::0::0::ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::controlflow_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ControlFlow)


def test_uml3::0::0::controlflow_constructor_exists():
    assert callable(uml3::0::0::ControlFlow.__init__)


def test_uml3::0::0::controlflow_constructor_args():
    sig = inspect.signature(uml3::0::0::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::expansionregion_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExpansionRegion)


def test_uml3::0::0::expansionregion_constructor_exists():
    assert callable(uml3::0::0::ExpansionRegion.__init__)


def test_uml3::0::0::expansionregion_constructor_args():
    sig = inspect.signature(uml3::0::0::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_uml3::0::0::expansionregion_has_mode():
    assert hasattr(uml3::0::0::ExpansionRegion, "mode")
    descriptor = None
    for klass in uml3::0::0::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::loopnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LoopNode)


def test_uml3::0::0::loopnode_constructor_exists():
    assert callable(uml3::0::0::LoopNode.__init__)


def test_uml3::0::0::loopnode_constructor_args():
    sig = inspect.signature(uml3::0::0::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_uml3::0::0::loopnode_has_isTestedFirst():
    assert hasattr(uml3::0::0::LoopNode, "isTestedFirst")
    descriptor = None
    for klass in uml3::0::0::LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::sequencenode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::SequenceNode)


def test_uml3::0::0::sequencenode_constructor_exists():
    assert callable(uml3::0::0::SequenceNode.__init__)


def test_uml3::0::0::sequencenode_constructor_args():
    sig = inspect.signature(uml3::0::0::SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CallBehaviorAction)


def test_uml3::0::0::callbehavioraction_constructor_exists():
    assert callable(uml3::0::0::CallBehaviorAction.__init__)


def test_uml3::0::0::callbehavioraction_constructor_args():
    sig = inspect.signature(uml3::0::0::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CallOperationAction)


def test_uml3::0::0::calloperationaction_constructor_exists():
    assert callable(uml3::0::0::CallOperationAction.__init__)


def test_uml3::0::0::calloperationaction_constructor_args():
    sig = inspect.signature(uml3::0::0::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::SendObjectAction)


def test_uml3::0::0::sendobjectaction_constructor_exists():
    assert callable(uml3::0::0::SendObjectAction.__init__)


def test_uml3::0::0::sendobjectaction_constructor_args():
    sig = inspect.signature(uml3::0::0::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::BroadcastSignalAction)


def test_uml3::0::0::broadcastsignalaction_constructor_exists():
    assert callable(uml3::0::0::BroadcastSignalAction.__init__)


def test_uml3::0::0::broadcastsignalaction_constructor_args():
    sig = inspect.signature(uml3::0::0::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::SendSignalAction)


def test_uml3::0::0::sendsignalaction_constructor_exists():
    assert callable(uml3::0::0::SendSignalAction.__init__)


def test_uml3::0::0::sendsignalaction_constructor_args():
    sig = inspect.signature(uml3::0::0::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::callaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CallAction)


def test_uml3::0::0::callaction_constructor_exists():
    assert callable(uml3::0::0::CallAction.__init__)


def test_uml3::0::0::callaction_constructor_args():
    sig = inspect.signature(uml3::0::0::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_uml3::0::0::callaction_has_isSynchronous():
    assert hasattr(uml3::0::0::CallAction, "isSynchronous")
    descriptor = None
    for klass in uml3::0::0::CallAction.__mro__:
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



def test_uml3::0::0::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CentralBufferNode)


def test_uml3::0::0::centralbuffernode_constructor_exists():
    assert callable(uml3::0::0::CentralBufferNode.__init__)


def test_uml3::0::0::centralbuffernode_constructor_args():
    sig = inspect.signature(uml3::0::0::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::expansionnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExpansionNode)


def test_uml3::0::0::expansionnode_constructor_exists():
    assert callable(uml3::0::0::ExpansionNode.__init__)


def test_uml3::0::0::expansionnode_constructor_args():
    sig = inspect.signature(uml3::0::0::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActivityParameterNode)


def test_uml3::0::0::activityparameternode_constructor_exists():
    assert callable(uml3::0::0::ActivityParameterNode.__init__)


def test_uml3::0::0::activityparameternode_constructor_args():
    sig = inspect.signature(uml3::0::0::ActivityParameterNode.__init__)
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



def test_uml3::0::0::interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InterruptibleActivityRegion)


def test_uml3::0::0::interruptibleactivityregion_constructor_exists():
    assert callable(uml3::0::0::InterruptibleActivityRegion.__init__)


def test_uml3::0::0::interruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml3::0::0::InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::controlnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ControlNode)


def test_uml3::0::0::controlnode_constructor_exists():
    assert callable(uml3::0::0::ControlNode.__init__)


def test_uml3::0::0::controlnode_constructor_args():
    sig = inspect.signature(uml3::0::0::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::executablenode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExecutableNode)


def test_uml3::0::0::executablenode_constructor_exists():
    assert callable(uml3::0::0::ExecutableNode.__init__)


def test_uml3::0::0::executablenode_constructor_args():
    sig = inspect.signature(uml3::0::0::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::action_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Action)


def test_uml3::0::0::action_constructor_exists():
    assert callable(uml3::0::0::Action.__init__)


def test_uml3::0::0::action_constructor_args():
    sig = inspect.signature(uml3::0::0::Action.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::outputpin_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::OutputPin)


def test_uml3::0::0::outputpin_constructor_exists():
    assert callable(uml3::0::0::OutputPin.__init__)


def test_uml3::0::0::outputpin_constructor_args():
    sig = inspect.signature(uml3::0::0::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::inputpin_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InputPin)


def test_uml3::0::0::inputpin_constructor_exists():
    assert callable(uml3::0::0::InputPin.__init__)


def test_uml3::0::0::inputpin_constructor_args():
    sig = inspect.signature(uml3::0::0::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::readselfaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadSelfAction)


def test_uml3::0::0::readselfaction_constructor_exists():
    assert callable(uml3::0::0::ReadSelfAction.__init__)


def test_uml3::0::0::readselfaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::variableaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::VariableAction)


def test_uml3::0::0::variableaction_constructor_exists():
    assert callable(uml3::0::0::VariableAction.__init__)


def test_uml3::0::0::variableaction_constructor_args():
    sig = inspect.signature(uml3::0::0::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ClearAssociationAction)


def test_uml3::0::0::clearassociationaction_constructor_exists():
    assert callable(uml3::0::0::ClearAssociationAction.__init__)


def test_uml3::0::0::clearassociationaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ValueSpecificationAction)


def test_uml3::0::0::valuespecificationaction_constructor_exists():
    assert callable(uml3::0::0::ValueSpecificationAction.__init__)


def test_uml3::0::0::valuespecificationaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TestIdentityAction)


def test_uml3::0::0::testidentityaction_constructor_exists():
    assert callable(uml3::0::0::TestIdentityAction.__init__)


def test_uml3::0::0::testidentityaction_constructor_args():
    sig = inspect.signature(uml3::0::0::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StructuralFeatureAction)


def test_uml3::0::0::structuralfeatureaction_constructor_exists():
    assert callable(uml3::0::0::StructuralFeatureAction.__init__)


def test_uml3::0::0::structuralfeatureaction_constructor_args():
    sig = inspect.signature(uml3::0::0::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DestroyObjectAction)


def test_uml3::0::0::destroyobjectaction_constructor_exists():
    assert callable(uml3::0::0::DestroyObjectAction.__init__)


def test_uml3::0::0::destroyobjectaction_constructor_args():
    sig = inspect.signature(uml3::0::0::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyOwnedObjects" in params, "Missing parameter 'isDestroyOwnedObjects'"
    assert "isDestroyLinks" in params, "Missing parameter 'isDestroyLinks'"

def test_uml3::0::0::destroyobjectaction_has_isDestroyOwnedObjects():
    assert hasattr(uml3::0::0::DestroyObjectAction, "isDestroyOwnedObjects")
    descriptor = None
    for klass in uml3::0::0::DestroyObjectAction.__mro__:
        if "isDestroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::destroyobjectaction_has_isDestroyLinks():
    assert hasattr(uml3::0::0::DestroyObjectAction, "isDestroyLinks")
    descriptor = None
    for klass in uml3::0::0::DestroyObjectAction.__mro__:
        if "isDestroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyLinks"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CreateObjectAction)


def test_uml3::0::0::createobjectaction_constructor_exists():
    assert callable(uml3::0::0::CreateObjectAction.__init__)


def test_uml3::0::0::createobjectaction_constructor_args():
    sig = inspect.signature(uml3::0::0::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::RaiseExceptionAction)


def test_uml3::0::0::raiseexceptionaction_constructor_exists():
    assert callable(uml3::0::0::RaiseExceptionAction.__init__)


def test_uml3::0::0::raiseexceptionaction_constructor_args():
    sig = inspect.signature(uml3::0::0::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::invocationaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InvocationAction)


def test_uml3::0::0::invocationaction_constructor_exists():
    assert callable(uml3::0::0::InvocationAction.__init__)


def test_uml3::0::0::invocationaction_constructor_args():
    sig = inspect.signature(uml3::0::0::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::linkaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LinkAction)


def test_uml3::0::0::linkaction_constructor_exists():
    assert callable(uml3::0::0::LinkAction.__init__)


def test_uml3::0::0::linkaction_constructor_args():
    sig = inspect.signature(uml3::0::0::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::OpaqueAction)


def test_uml3::0::0::opaqueaction_constructor_exists():
    assert callable(uml3::0::0::OpaqueAction.__init__)


def test_uml3::0::0::opaqueaction_constructor_args():
    sig = inspect.signature(uml3::0::0::OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml3::0::0::opaqueaction_has_body():
    assert hasattr(uml3::0::0::OpaqueAction, "body")
    descriptor = None
    for klass in uml3::0::0::OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::opaqueaction_has_language():
    assert hasattr(uml3::0::0::OpaqueAction, "language")
    descriptor = None
    for klass in uml3::0::0::OpaqueAction.__mro__:
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



def test_uml3::0::0::functionbehavior_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::FunctionBehavior)


def test_uml3::0::0::functionbehavior_constructor_exists():
    assert callable(uml3::0::0::FunctionBehavior.__init__)


def test_uml3::0::0::functionbehavior_constructor_args():
    sig = inspect.signature(uml3::0::0::FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LiteralUnlimitedNatural)


def test_uml3::0::0::literalunlimitednatural_constructor_exists():
    assert callable(uml3::0::0::LiteralUnlimitedNatural.__init__)


def test_uml3::0::0::literalunlimitednatural_constructor_args():
    sig = inspect.signature(uml3::0::0::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3::0::0::literalunlimitednatural_has_value():
    assert hasattr(uml3::0::0::LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in uml3::0::0::LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::literalboolean_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LiteralBoolean)


def test_uml3::0::0::literalboolean_constructor_exists():
    assert callable(uml3::0::0::LiteralBoolean.__init__)


def test_uml3::0::0::literalboolean_constructor_args():
    sig = inspect.signature(uml3::0::0::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3::0::0::literalboolean_has_value():
    assert hasattr(uml3::0::0::LiteralBoolean, "value")
    descriptor = None
    for klass in uml3::0::0::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::literalstring_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LiteralString)


def test_uml3::0::0::literalstring_constructor_exists():
    assert callable(uml3::0::0::LiteralString.__init__)


def test_uml3::0::0::literalstring_constructor_args():
    sig = inspect.signature(uml3::0::0::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3::0::0::literalstring_has_value():
    assert hasattr(uml3::0::0::LiteralString, "value")
    descriptor = None
    for klass in uml3::0::0::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::literalnull_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LiteralNull)


def test_uml3::0::0::literalnull_constructor_exists():
    assert callable(uml3::0::0::LiteralNull.__init__)


def test_uml3::0::0::literalnull_constructor_args():
    sig = inspect.signature(uml3::0::0::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::literalinteger_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LiteralInteger)


def test_uml3::0::0::literalinteger_constructor_exists():
    assert callable(uml3::0::0::LiteralInteger.__init__)


def test_uml3::0::0::literalinteger_constructor_args():
    sig = inspect.signature(uml3::0::0::LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml3::0::0::literalinteger_has_value():
    assert hasattr(uml3::0::0::LiteralInteger, "value")
    descriptor = None
    for klass in uml3::0::0::LiteralInteger.__mro__:
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



def test_uml3::0::0::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::EnumerationLiteral)


def test_uml3::0::0::enumerationliteral_constructor_exists():
    assert callable(uml3::0::0::EnumerationLiteral.__init__)


def test_uml3::0::0::enumerationliteral_constructor_args():
    sig = inspect.signature(uml3::0::0::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::primitivetype_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::PrimitiveType)


def test_uml3::0::0::primitivetype_constructor_exists():
    assert callable(uml3::0::0::PrimitiveType.__init__)


def test_uml3::0::0::primitivetype_constructor_args():
    sig = inspect.signature(uml3::0::0::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::enumeration_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Enumeration)


def test_uml3::0::0::enumeration_constructor_exists():
    assert callable(uml3::0::0::Enumeration.__init__)


def test_uml3::0::0::enumeration_constructor_args():
    sig = inspect.signature(uml3::0::0::Enumeration.__init__)
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



def test_uml3::0::0::connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ConnectableElementTemplateParameter)


def test_uml3::0::0::connectableelementtemplateparameter_constructor_exists():
    assert callable(uml3::0::0::ConnectableElementTemplateParameter.__init__)


def test_uml3::0::0::connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(uml3::0::0::ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ClassifierTemplateParameter)


def test_uml3::0::0::classifiertemplateparameter_constructor_exists():
    assert callable(uml3::0::0::ClassifierTemplateParameter.__init__)


def test_uml3::0::0::classifiertemplateparameter_constructor_args():
    sig = inspect.signature(uml3::0::0::ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"

def test_uml3::0::0::classifiertemplateparameter_has_allowSubstitutable():
    assert hasattr(uml3::0::0::ClassifierTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in uml3::0::0::ClassifierTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::OperationTemplateParameter)


def test_uml3::0::0::operationtemplateparameter_constructor_exists():
    assert callable(uml3::0::0::OperationTemplateParameter.__init__)


def test_uml3::0::0::operationtemplateparameter_constructor_args():
    sig = inspect.signature(uml3::0::0::OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::EncapsulatedClassifier)


def test_uml3::0::0::encapsulatedclassifier_constructor_exists():
    assert callable(uml3::0::0::EncapsulatedClassifier.__init__)


def test_uml3::0::0::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml3::0::0::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::model_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Model)


def test_uml3::0::0::model_constructor_exists():
    assert callable(uml3::0::0::Model.__init__)


def test_uml3::0::0::model_constructor_args():
    sig = inspect.signature(uml3::0::0::Model.__init__)
    params = list(sig.parameters.keys())
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"

def test_uml3::0::0::model_has_viewpoint():
    assert hasattr(uml3::0::0::Model, "viewpoint")
    descriptor = None
    for klass in uml3::0::0::Model.__mro__:
        if "viewpoint" in klass.__dict__:
            descriptor = klass.__dict__["viewpoint"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::profile_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Profile)


def test_uml3::0::0::profile_constructor_exists():
    assert callable(uml3::0::0::Profile.__init__)


def test_uml3::0::0::profile_constructor_args():
    sig = inspect.signature(uml3::0::0::Profile.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::communicationpath_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CommunicationPath)


def test_uml3::0::0::communicationpath_constructor_exists():
    assert callable(uml3::0::0::CommunicationPath.__init__)


def test_uml3::0::0::communicationpath_constructor_args():
    sig = inspect.signature(uml3::0::0::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ConnectionPointReference)


def test_uml3::0::0::connectionpointreference_constructor_exists():
    assert callable(uml3::0::0::ConnectionPointReference.__init__)


def test_uml3::0::0::connectionpointreference_constructor_args():
    sig = inspect.signature(uml3::0::0::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::extensionend_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExtensionEnd)


def test_uml3::0::0::extensionend_constructor_exists():
    assert callable(uml3::0::0::ExtensionEnd.__init__)


def test_uml3::0::0::extensionend_constructor_args():
    sig = inspect.signature(uml3::0::0::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::port_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Port)


def test_uml3::0::0::port_constructor_exists():
    assert callable(uml3::0::0::Port.__init__)


def test_uml3::0::0::port_constructor_args():
    sig = inspect.signature(uml3::0::0::Port.__init__)
    params = list(sig.parameters.keys())
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"
    assert "isService" in params, "Missing parameter 'isService'"

def test_uml3::0::0::port_has_isBehavior():
    assert hasattr(uml3::0::0::Port, "isBehavior")
    descriptor = None
    for klass in uml3::0::0::Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::port_has_isService():
    assert hasattr(uml3::0::0::Port, "isService")
    descriptor = None
    for klass in uml3::0::0::Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::pseudostate_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Pseudostate)


def test_uml3::0::0::pseudostate_constructor_exists():
    assert callable(uml3::0::0::Pseudostate.__init__)


def test_uml3::0::0::pseudostate_constructor_args():
    sig = inspect.signature(uml3::0::0::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml3::0::0::pseudostate_has_kind():
    assert hasattr(uml3::0::0::Pseudostate, "kind")
    descriptor = None
    for klass in uml3::0::0::Pseudostate.__mro__:
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



def test_uml3::0::0::interaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Interaction)


def test_uml3::0::0::interaction_constructor_exists():
    assert callable(uml3::0::0::Interaction.__init__)


def test_uml3::0::0::interaction_constructor_args():
    sig = inspect.signature(uml3::0::0::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::OpaqueBehavior)


def test_uml3::0::0::opaquebehavior_constructor_exists():
    assert callable(uml3::0::0::OpaqueBehavior.__init__)


def test_uml3::0::0::opaquebehavior_constructor_args():
    sig = inspect.signature(uml3::0::0::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml3::0::0::opaquebehavior_has_body():
    assert hasattr(uml3::0::0::OpaqueBehavior, "body")
    descriptor = None
    for klass in uml3::0::0::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::opaquebehavior_has_language():
    assert hasattr(uml3::0::0::OpaqueBehavior, "language")
    descriptor = None
    for klass in uml3::0::0::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::activity_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Activity)


def test_uml3::0::0::activity_constructor_exists():
    assert callable(uml3::0::0::Activity.__init__)


def test_uml3::0::0::activity_constructor_args():
    sig = inspect.signature(uml3::0::0::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_uml3::0::0::activity_has_isReadOnly():
    assert hasattr(uml3::0::0::Activity, "isReadOnly")
    descriptor = None
    for klass in uml3::0::0::Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::activity_has_isSingleExecution():
    assert hasattr(uml3::0::0::Activity, "isSingleExecution")
    descriptor = None
    for klass in uml3::0::0::Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::statemachine_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StateMachine)


def test_uml3::0::0::statemachine_constructor_exists():
    assert callable(uml3::0::0::StateMachine.__init__)


def test_uml3::0::0::statemachine_constructor_args():
    sig = inspect.signature(uml3::0::0::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ProtocolStateMachine)


def test_uml3::0::0::protocolstatemachine_constructor_exists():
    assert callable(uml3::0::0::ProtocolStateMachine.__init__)


def test_uml3::0::0::protocolstatemachine_constructor_args():
    sig = inspect.signature(uml3::0::0::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::extension_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Extension)


def test_uml3::0::0::extension_constructor_exists():
    assert callable(uml3::0::0::Extension.__init__)


def test_uml3::0::0::extension_constructor_args():
    sig = inspect.signature(uml3::0::0::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_uml3::0::0::extension_has_isRequired():
    assert hasattr(uml3::0::0::Extension, "isRequired")
    descriptor = None
    for klass in uml3::0::0::Extension.__mro__:
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



def test_uml3::0::0::actor_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Actor)


def test_uml3::0::0::actor_constructor_exists():
    assert callable(uml3::0::0::Actor.__init__)


def test_uml3::0::0::actor_constructor_args():
    sig = inspect.signature(uml3::0::0::Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::collaboration_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Collaboration)


def test_uml3::0::0::collaboration_constructor_exists():
    assert callable(uml3::0::0::Collaboration.__init__)


def test_uml3::0::0::collaboration_constructor_args():
    sig = inspect.signature(uml3::0::0::Collaboration.__init__)
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



def test_uml3::0::0::component_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Component)


def test_uml3::0::0::component_constructor_exists():
    assert callable(uml3::0::0::Component.__init__)


def test_uml3::0::0::component_constructor_args():
    sig = inspect.signature(uml3::0::0::Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"

def test_uml3::0::0::component_has_isIndirectlyInstantiated():
    assert hasattr(uml3::0::0::Component, "isIndirectlyInstantiated")
    descriptor = None
    for klass in uml3::0::0::Component.__mro__:
        if "isIndirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["isIndirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::stereotype_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Stereotype)


def test_uml3::0::0::stereotype_constructor_exists():
    assert callable(uml3::0::0::Stereotype.__init__)


def test_uml3::0::0::stereotype_constructor_args():
    sig = inspect.signature(uml3::0::0::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::associationclass_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::AssociationClass)


def test_uml3::0::0::associationclass_constructor_exists():
    assert callable(uml3::0::0::AssociationClass.__init__)


def test_uml3::0::0::associationclass_constructor_args():
    sig = inspect.signature(uml3::0::0::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::connector_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Connector)


def test_uml3::0::0::connector_constructor_exists():
    assert callable(uml3::0::0::Connector.__init__)


def test_uml3::0::0::connector_constructor_args():
    sig = inspect.signature(uml3::0::0::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml3::0::0::connector_has_kind():
    assert hasattr(uml3::0::0::Connector, "kind")
    descriptor = None
    for klass in uml3::0::0::Connector.__mro__:
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



def test_uml3::0::0::reception_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Reception)


def test_uml3::0::0::reception_constructor_exists():
    assert callable(uml3::0::0::Reception.__init__)


def test_uml3::0::0::reception_constructor_args():
    sig = inspect.signature(uml3::0::0::Reception.__init__)
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



def test_uml3::0::0::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DeploymentSpecification)


def test_uml3::0::0::deploymentspecification_constructor_exists():
    assert callable(uml3::0::0::DeploymentSpecification.__init__)


def test_uml3::0::0::deploymentspecification_constructor_args():
    sig = inspect.signature(uml3::0::0::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"

def test_uml3::0::0::deploymentspecification_has_deploymentLocation():
    assert hasattr(uml3::0::0::DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in uml3::0::0::DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::deploymentspecification_has_executionLocation():
    assert hasattr(uml3::0::0::DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in uml3::0::0::DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::class_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Class)


def test_uml3::0::0::class_constructor_exists():
    assert callable(uml3::0::0::Class.__init__)


def test_uml3::0::0::class_constructor_args():
    sig = inspect.signature(uml3::0::0::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml3::0::0::class_has_isActive():
    assert hasattr(uml3::0::0::Class, "isActive")
    descriptor = None
    for klass in uml3::0::0::Class.__mro__:
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



def test_uml3::0::0::node_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Node)


def test_uml3::0::0::node_constructor_exists():
    assert callable(uml3::0::0::Node.__init__)


def test_uml3::0::0::node_constructor_args():
    sig = inspect.signature(uml3::0::0::Node.__init__)
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



def test_uml3::0::0::timeexpression_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TimeExpression)


def test_uml3::0::0::timeexpression_constructor_exists():
    assert callable(uml3::0::0::TimeExpression.__init__)


def test_uml3::0::0::timeexpression_constructor_args():
    sig = inspect.signature(uml3::0::0::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::instancevalue_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InstanceValue)


def test_uml3::0::0::instancevalue_constructor_exists():
    assert callable(uml3::0::0::InstanceValue.__init__)


def test_uml3::0::0::instancevalue_constructor_args():
    sig = inspect.signature(uml3::0::0::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::duration_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Duration)


def test_uml3::0::0::duration_constructor_exists():
    assert callable(uml3::0::0::Duration.__init__)


def test_uml3::0::0::duration_constructor_args():
    sig = inspect.signature(uml3::0::0::Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::literalspecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LiteralSpecification)


def test_uml3::0::0::literalspecification_constructor_exists():
    assert callable(uml3::0::0::LiteralSpecification.__init__)


def test_uml3::0::0::literalspecification_constructor_args():
    sig = inspect.signature(uml3::0::0::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::expression_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Expression)


def test_uml3::0::0::expression_constructor_exists():
    assert callable(uml3::0::0::Expression.__init__)


def test_uml3::0::0::expression_constructor_args():
    sig = inspect.signature(uml3::0::0::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_uml3::0::0::expression_has_symbol():
    assert hasattr(uml3::0::0::Expression, "symbol")
    descriptor = None
    for klass in uml3::0::0::Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::interval_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Interval)


def test_uml3::0::0::interval_constructor_exists():
    assert callable(uml3::0::0::Interval.__init__)


def test_uml3::0::0::interval_constructor_args():
    sig = inspect.signature(uml3::0::0::Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::OpaqueExpression)


def test_uml3::0::0::opaqueexpression_constructor_exists():
    assert callable(uml3::0::0::OpaqueExpression.__init__)


def test_uml3::0::0::opaqueexpression_constructor_args():
    sig = inspect.signature(uml3::0::0::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml3::0::0::opaqueexpression_has_body():
    assert hasattr(uml3::0::0::OpaqueExpression, "body")
    descriptor = None
    for klass in uml3::0::0::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::opaqueexpression_has_language():
    assert hasattr(uml3::0::0::OpaqueExpression, "language")
    descriptor = None
    for klass in uml3::0::0::OpaqueExpression.__mro__:
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



def test_uml3::0::0::usage_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Usage)


def test_uml3::0::0::usage_constructor_exists():
    assert callable(uml3::0::0::Usage.__init__)


def test_uml3::0::0::usage_constructor_args():
    sig = inspect.signature(uml3::0::0::Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::deployment_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Deployment)


def test_uml3::0::0::deployment_constructor_exists():
    assert callable(uml3::0::0::Deployment.__init__)


def test_uml3::0::0::deployment_constructor_args():
    sig = inspect.signature(uml3::0::0::Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::abstraction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Abstraction)


def test_uml3::0::0::abstraction_constructor_exists():
    assert callable(uml3::0::0::Abstraction.__init__)


def test_uml3::0::0::abstraction_constructor_args():
    sig = inspect.signature(uml3::0::0::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::manifestation_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Manifestation)


def test_uml3::0::0::manifestation_constructor_exists():
    assert callable(uml3::0::0::Manifestation.__init__)


def test_uml3::0::0::manifestation_constructor_args():
    sig = inspect.signature(uml3::0::0::Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::realization_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Realization)


def test_uml3::0::0::realization_constructor_exists():
    assert callable(uml3::0::0::Realization.__init__)


def test_uml3::0::0::realization_constructor_args():
    sig = inspect.signature(uml3::0::0::Realization.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::pin_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Pin)


def test_uml3::0::0::pin_constructor_exists():
    assert callable(uml3::0::0::Pin.__init__)


def test_uml3::0::0::pin_constructor_args():
    sig = inspect.signature(uml3::0::0::Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_uml3::0::0::pin_has_isControl():
    assert hasattr(uml3::0::0::Pin, "isControl")
    descriptor = None
    for klass in uml3::0::0::Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::connectorend_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ConnectorEnd)


def test_uml3::0::0::connectorend_constructor_exists():
    assert callable(uml3::0::0::ConnectorEnd.__init__)


def test_uml3::0::0::connectorend_constructor_args():
    sig = inspect.signature(uml3::0::0::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::variable_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Variable)


def test_uml3::0::0::variable_constructor_exists():
    assert callable(uml3::0::0::Variable.__init__)


def test_uml3::0::0::variable_constructor_args():
    sig = inspect.signature(uml3::0::0::Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ConditionalNode)


def test_uml3::0::0::conditionalnode_constructor_exists():
    assert callable(uml3::0::0::ConditionalNode.__init__)


def test_uml3::0::0::conditionalnode_constructor_args():
    sig = inspect.signature(uml3::0::0::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssured" in params, "Missing parameter 'isAssured'"

def test_uml3::0::0::conditionalnode_has_isDeterminate():
    assert hasattr(uml3::0::0::ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in uml3::0::0::ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::conditionalnode_has_isAssured():
    assert hasattr(uml3::0::0::ConditionalNode, "isAssured")
    descriptor = None
    for klass in uml3::0::0::ConditionalNode.__mro__:
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



def test_uml3::0::0::datastorenode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DataStoreNode)


def test_uml3::0::0::datastorenode_constructor_exists():
    assert callable(uml3::0::0::DataStoreNode.__init__)


def test_uml3::0::0::datastorenode_constructor_args():
    sig = inspect.signature(uml3::0::0::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::joinnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::JoinNode)


def test_uml3::0::0::joinnode_constructor_exists():
    assert callable(uml3::0::0::JoinNode.__init__)


def test_uml3::0::0::joinnode_constructor_args():
    sig = inspect.signature(uml3::0::0::JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_uml3::0::0::joinnode_has_isCombineDuplicate():
    assert hasattr(uml3::0::0::JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in uml3::0::0::JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StartObjectBehaviorAction)


def test_uml3::0::0::startobjectbehavioraction_constructor_exists():
    assert callable(uml3::0::0::StartObjectBehaviorAction.__init__)


def test_uml3::0::0::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml3::0::0::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::reduceaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReduceAction)


def test_uml3::0::0::reduceaction_constructor_exists():
    assert callable(uml3::0::0::ReduceAction.__init__)


def test_uml3::0::0::reduceaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_uml3::0::0::reduceaction_has_isOrdered():
    assert hasattr(uml3::0::0::ReduceAction, "isOrdered")
    descriptor = None
    for klass in uml3::0::0::ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::UnmarshallAction)


def test_uml3::0::0::unmarshallaction_constructor_exists():
    assert callable(uml3::0::0::UnmarshallAction.__init__)


def test_uml3::0::0::unmarshallaction_constructor_args():
    sig = inspect.signature(uml3::0::0::UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::replyaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReplyAction)


def test_uml3::0::0::replyaction_constructor_exists():
    assert callable(uml3::0::0::ReplyAction.__init__)


def test_uml3::0::0::replyaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::AcceptCallAction)


def test_uml3::0::0::acceptcallaction_constructor_exists():
    assert callable(uml3::0::0::AcceptCallAction.__init__)


def test_uml3::0::0::acceptcallaction_constructor_args():
    sig = inspect.signature(uml3::0::0::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadLinkObjectEndAction)


def test_uml3::0::0::readlinkobjectendaction_constructor_exists():
    assert callable(uml3::0::0::ReadLinkObjectEndAction.__init__)


def test_uml3::0::0::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::AcceptEventAction)


def test_uml3::0::0::accepteventaction_constructor_exists():
    assert callable(uml3::0::0::AcceptEventAction.__init__)


def test_uml3::0::0::accepteventaction_constructor_args():
    sig = inspect.signature(uml3::0::0::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_uml3::0::0::accepteventaction_has_isUnmarshall():
    assert hasattr(uml3::0::0::AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in uml3::0::0::AcceptEventAction.__mro__:
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



def test_uml3::0::0::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CreateLinkObjectAction)


def test_uml3::0::0::createlinkobjectaction_constructor_exists():
    assert callable(uml3::0::0::CreateLinkObjectAction.__init__)


def test_uml3::0::0::createlinkobjectaction_constructor_args():
    sig = inspect.signature(uml3::0::0::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadLinkObjectEndQualifierAction)


def test_uml3::0::0::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml3::0::0::ReadLinkObjectEndQualifierAction.__init__)


def test_uml3::0::0::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StartClassifierBehaviorAction)


def test_uml3::0::0::startclassifierbehavioraction_constructor_exists():
    assert callable(uml3::0::0::StartClassifierBehaviorAction.__init__)


def test_uml3::0::0::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml3::0::0::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadIsClassifiedObjectAction)


def test_uml3::0::0::readisclassifiedobjectaction_constructor_exists():
    assert callable(uml3::0::0::ReadIsClassifiedObjectAction.__init__)


def test_uml3::0::0::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDirect" in params, "Missing parameter 'isDirect'"

def test_uml3::0::0::readisclassifiedobjectaction_has_isDirect():
    assert hasattr(uml3::0::0::ReadIsClassifiedObjectAction, "isDirect")
    descriptor = None
    for klass in uml3::0::0::ReadIsClassifiedObjectAction.__mro__:
        if "isDirect" in klass.__dict__:
            descriptor = klass.__dict__["isDirect"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReclassifyObjectAction)


def test_uml3::0::0::reclassifyobjectaction_constructor_exists():
    assert callable(uml3::0::0::ReclassifyObjectAction.__init__)


def test_uml3::0::0::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3::0::0::reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(uml3::0::0::ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in uml3::0::0::ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::readextentaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ReadExtentAction)


def test_uml3::0::0::readextentaction_constructor_exists():
    assert callable(uml3::0::0::ReadExtentAction.__init__)


def test_uml3::0::0::readextentaction_constructor_args():
    sig = inspect.signature(uml3::0::0::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::RemoveVariableValueAction)


def test_uml3::0::0::removevariablevalueaction_constructor_exists():
    assert callable(uml3::0::0::RemoveVariableValueAction.__init__)


def test_uml3::0::0::removevariablevalueaction_constructor_args():
    sig = inspect.signature(uml3::0::0::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml3::0::0::removevariablevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml3::0::0::RemoveVariableValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml3::0::0::RemoveVariableValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::AddVariableValueAction)


def test_uml3::0::0::addvariablevalueaction_constructor_exists():
    assert callable(uml3::0::0::AddVariableValueAction.__init__)


def test_uml3::0::0::addvariablevalueaction_constructor_args():
    sig = inspect.signature(uml3::0::0::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml3::0::0::addvariablevalueaction_has_isReplaceAll():
    assert hasattr(uml3::0::0::AddVariableValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml3::0::0::AddVariableValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::protocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ProtocolConformance)


def test_uml3::0::0::protocolconformance_constructor_exists():
    assert callable(uml3::0::0::ProtocolConformance.__init__)


def test_uml3::0::0::protocolconformance_constructor_args():
    sig = inspect.signature(uml3::0::0::ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::packageimport_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::PackageImport)


def test_uml3::0::0::packageimport_constructor_exists():
    assert callable(uml3::0::0::PackageImport.__init__)


def test_uml3::0::0::packageimport_constructor_args():
    sig = inspect.signature(uml3::0::0::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml3::0::0::packageimport_has_visibility():
    assert hasattr(uml3::0::0::PackageImport, "visibility")
    descriptor = None
    for klass in uml3::0::0::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::elementimport_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ElementImport)


def test_uml3::0::0::elementimport_constructor_exists():
    assert callable(uml3::0::0::ElementImport.__init__)


def test_uml3::0::0::elementimport_constructor_args():
    sig = inspect.signature(uml3::0::0::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_uml3::0::0::elementimport_has_visibility():
    assert hasattr(uml3::0::0::ElementImport, "visibility")
    descriptor = None
    for klass in uml3::0::0::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::elementimport_has_alias():
    assert hasattr(uml3::0::0::ElementImport, "alias")
    descriptor = None
    for klass in uml3::0::0::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DirectedRelationship)


def test_uml3::0::0::directedrelationship_constructor_exists():
    assert callable(uml3::0::0::DirectedRelationship.__init__)


def test_uml3::0::0::directedrelationship_constructor_args():
    sig = inspect.signature(uml3::0::0::DirectedRelationship.__init__)
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



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::messageend_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::MessageEnd)


def test_uml3::0::0::messageend_constructor_exists():
    assert callable(uml3::0::0::MessageEnd.__init__)


def test_uml3::0::0::messageend_constructor_args():
    sig = inspect.signature(uml3::0::0::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::namespace_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Namespace)


def test_uml3::0::0::namespace_constructor_exists():
    assert callable(uml3::0::0::Namespace.__init__)


def test_uml3::0::0::namespace_constructor_args():
    sig = inspect.signature(uml3::0::0::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DeploymentTarget)


def test_uml3::0::0::deploymenttarget_constructor_exists():
    assert callable(uml3::0::0::DeploymentTarget.__init__)


def test_uml3::0::0::deploymenttarget_constructor_args():
    sig = inspect.signature(uml3::0::0::DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::activitypartition_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActivityPartition)


def test_uml3::0::0::activitypartition_constructor_exists():
    assert callable(uml3::0::0::ActivityPartition.__init__)


def test_uml3::0::0::activitypartition_constructor_args():
    sig = inspect.signature(uml3::0::0::ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isDimension" in params, "Missing parameter 'isDimension'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_uml3::0::0::activitypartition_has_isDimension():
    assert hasattr(uml3::0::0::ActivityPartition, "isDimension")
    descriptor = None
    for klass in uml3::0::0::ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::activitypartition_has_isExternal():
    assert hasattr(uml3::0::0::ActivityPartition, "isExternal")
    descriptor = None
    for klass in uml3::0::0::ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::lifeline_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Lifeline)


def test_uml3::0::0::lifeline_constructor_exists():
    assert callable(uml3::0::0::Lifeline.__init__)


def test_uml3::0::0::lifeline_constructor_args():
    sig = inspect.signature(uml3::0::0::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::include_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Include)


def test_uml3::0::0::include_constructor_exists():
    assert callable(uml3::0::0::Include.__init__)


def test_uml3::0::0::include_constructor_args():
    sig = inspect.signature(uml3::0::0::Include.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::message_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Message)


def test_uml3::0::0::message_constructor_exists():
    assert callable(uml3::0::0::Message.__init__)


def test_uml3::0::0::message_constructor_args():
    sig = inspect.signature(uml3::0::0::Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageSort" in params, "Missing parameter 'messageSort'"
    assert "messageKind" in params, "Missing parameter 'messageKind'"

def test_uml3::0::0::message_has_messageSort():
    assert hasattr(uml3::0::0::Message, "messageSort")
    descriptor = None
    for klass in uml3::0::0::Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::message_has_messageKind():
    assert hasattr(uml3::0::0::Message, "messageKind")
    descriptor = None
    for klass in uml3::0::0::Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InteractionFragment)


def test_uml3::0::0::interactionfragment_constructor_exists():
    assert callable(uml3::0::0::InteractionFragment.__init__)


def test_uml3::0::0::interactionfragment_constructor_args():
    sig = inspect.signature(uml3::0::0::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::parameterset_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ParameterSet)


def test_uml3::0::0::parameterset_constructor_exists():
    assert callable(uml3::0::0::ParameterSet.__init__)


def test_uml3::0::0::parameterset_constructor_args():
    sig = inspect.signature(uml3::0::0::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::generalordering_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::GeneralOrdering)


def test_uml3::0::0::generalordering_constructor_exists():
    assert callable(uml3::0::0::GeneralOrdering.__init__)


def test_uml3::0::0::generalordering_constructor_args():
    sig = inspect.signature(uml3::0::0::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::deployedartifact_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DeployedArtifact)


def test_uml3::0::0::deployedartifact_constructor_exists():
    assert callable(uml3::0::0::DeployedArtifact.__init__)


def test_uml3::0::0::deployedartifact_constructor_args():
    sig = inspect.signature(uml3::0::0::DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::vertex_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Vertex)


def test_uml3::0::0::vertex_constructor_exists():
    assert callable(uml3::0::0::Vertex.__init__)


def test_uml3::0::0::vertex_constructor_args():
    sig = inspect.signature(uml3::0::0::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::trigger_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Trigger)


def test_uml3::0::0::trigger_constructor_exists():
    assert callable(uml3::0::0::Trigger.__init__)


def test_uml3::0::0::trigger_constructor_args():
    sig = inspect.signature(uml3::0::0::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::extend_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Extend)


def test_uml3::0::0::extend_constructor_exists():
    assert callable(uml3::0::0::Extend.__init__)


def test_uml3::0::0::extend_constructor_args():
    sig = inspect.signature(uml3::0::0::Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::profileapplication_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ProfileApplication)


def test_uml3::0::0::profileapplication_constructor_exists():
    assert callable(uml3::0::0::ProfileApplication.__init__)


def test_uml3::0::0::profileapplication_constructor_args():
    sig = inspect.signature(uml3::0::0::ProfileApplication.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_uml3::0::0::profileapplication_has_isStrict():
    assert hasattr(uml3::0::0::ProfileApplication, "isStrict")
    descriptor = None
    for klass in uml3::0::0::ProfileApplication.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::PackageableElement)


def test_uml3::0::0::packageableelement_constructor_exists():
    assert callable(uml3::0::0::PackageableElement.__init__)


def test_uml3::0::0::packageableelement_constructor_args():
    sig = inspect.signature(uml3::0::0::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::packagemerge_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::PackageMerge)


def test_uml3::0::0::packagemerge_constructor_exists():
    assert callable(uml3::0::0::PackageMerge.__init__)


def test_uml3::0::0::packagemerge_constructor_args():
    sig = inspect.signature(uml3::0::0::PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::stringexpression_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StringExpression)


def test_uml3::0::0::stringexpression_constructor_exists():
    assert callable(uml3::0::0::StringExpression.__init__)


def test_uml3::0::0::stringexpression_constructor_args():
    sig = inspect.signature(uml3::0::0::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::operation_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Operation)


def test_uml3::0::0::operation_constructor_exists():
    assert callable(uml3::0::0::Operation.__init__)


def test_uml3::0::0::operation_constructor_args():
    sig = inspect.signature(uml3::0::0::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_uml3::0::0::operation_has_isQuery():
    assert hasattr(uml3::0::0::Operation, "isQuery")
    descriptor = None
    for klass in uml3::0::0::Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::operation_has_upper():
    assert hasattr(uml3::0::0::Operation, "upper")
    descriptor = None
    for klass in uml3::0::0::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::operation_has_lower():
    assert hasattr(uml3::0::0::Operation, "lower")
    descriptor = None
    for klass in uml3::0::0::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::operation_has_isOrdered():
    assert hasattr(uml3::0::0::Operation, "isOrdered")
    descriptor = None
    for klass in uml3::0::0::Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::operation_has_isUnique():
    assert hasattr(uml3::0::0::Operation, "isUnique")
    descriptor = None
    for klass in uml3::0::0::Operation.__mro__:
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



def test_uml3::0::0::informationflow_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InformationFlow)


def test_uml3::0::0::informationflow_constructor_exists():
    assert callable(uml3::0::0::InformationFlow.__init__)


def test_uml3::0::0::informationflow_constructor_args():
    sig = inspect.signature(uml3::0::0::InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::instancespecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InstanceSpecification)


def test_uml3::0::0::instancespecification_constructor_exists():
    assert callable(uml3::0::0::InstanceSpecification.__init__)


def test_uml3::0::0::instancespecification_constructor_args():
    sig = inspect.signature(uml3::0::0::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::constraint_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Constraint)


def test_uml3::0::0::constraint_constructor_exists():
    assert callable(uml3::0::0::Constraint.__init__)


def test_uml3::0::0::constraint_constructor_args():
    sig = inspect.signature(uml3::0::0::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::observation_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Observation)


def test_uml3::0::0::observation_constructor_exists():
    assert callable(uml3::0::0::Observation.__init__)


def test_uml3::0::0::observation_constructor_args():
    sig = inspect.signature(uml3::0::0::Observation.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::event_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Event)


def test_uml3::0::0::event_constructor_exists():
    assert callable(uml3::0::0::Event.__init__)


def test_uml3::0::0::event_constructor_args():
    sig = inspect.signature(uml3::0::0::Event.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::type_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Type)


def test_uml3::0::0::type_constructor_exists():
    assert callable(uml3::0::0::Type.__init__)


def test_uml3::0::0::type_constructor_args():
    sig = inspect.signature(uml3::0::0::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::dependency_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Dependency)


def test_uml3::0::0::dependency_constructor_exists():
    assert callable(uml3::0::0::Dependency.__init__)


def test_uml3::0::0::dependency_constructor_args():
    sig = inspect.signature(uml3::0::0::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InteractionOperand)


def test_uml3::0::0::interactionoperand_constructor_exists():
    assert callable(uml3::0::0::InteractionOperand.__init__)


def test_uml3::0::0::interactionoperand_constructor_args():
    sig = inspect.signature(uml3::0::0::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::BehavioralFeature)


def test_uml3::0::0::behavioralfeature_constructor_exists():
    assert callable(uml3::0::0::BehavioralFeature.__init__)


def test_uml3::0::0::behavioralfeature_constructor_args():
    sig = inspect.signature(uml3::0::0::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml3::0::0::behavioralfeature_has_concurrency():
    assert hasattr(uml3::0::0::BehavioralFeature, "concurrency")
    descriptor = None
    for klass in uml3::0::0::BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::behavioralfeature_has_isAbstract():
    assert hasattr(uml3::0::0::BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in uml3::0::0::BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StructuredActivityNode)


def test_uml3::0::0::structuredactivitynode_constructor_exists():
    assert callable(uml3::0::0::StructuredActivityNode.__init__)


def test_uml3::0::0::structuredactivitynode_constructor_args():
    sig = inspect.signature(uml3::0::0::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_uml3::0::0::structuredactivitynode_has_mustIsolate():
    assert hasattr(uml3::0::0::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in uml3::0::0::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::package_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Package)


def test_uml3::0::0::package_constructor_exists():
    assert callable(uml3::0::0::Package.__init__)


def test_uml3::0::0::package_constructor_args():
    sig = inspect.signature(uml3::0::0::Package.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::element_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Element)


def test_uml3::0::0::element_constructor_exists():
    assert callable(uml3::0::0::Element.__init__)


def test_uml3::0::0::element_constructor_args():
    sig = inspect.signature(uml3::0::0::Element.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::relationship_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Relationship)


def test_uml3::0::0::relationship_constructor_exists():
    assert callable(uml3::0::0::Relationship.__init__)


def test_uml3::0::0::relationship_constructor_args():
    sig = inspect.signature(uml3::0::0::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::activitygroup_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActivityGroup)


def test_uml3::0::0::activitygroup_constructor_exists():
    assert callable(uml3::0::0::ActivityGroup.__init__)


def test_uml3::0::0::activitygroup_constructor_args():
    sig = inspect.signature(uml3::0::0::ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::image_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Image)


def test_uml3::0::0::image_constructor_exists():
    assert callable(uml3::0::0::Image.__init__)


def test_uml3::0::0::image_constructor_args():
    sig = inspect.signature(uml3::0::0::Image.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "location" in params, "Missing parameter 'location'"
    assert "content" in params, "Missing parameter 'content'"

def test_uml3::0::0::image_has_format():
    assert hasattr(uml3::0::0::Image, "format")
    descriptor = None
    for klass in uml3::0::0::Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::image_has_location():
    assert hasattr(uml3::0::0::Image, "location")
    descriptor = None
    for klass in uml3::0::0::Image.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::image_has_content():
    assert hasattr(uml3::0::0::Image, "content")
    descriptor = None
    for klass in uml3::0::0::Image.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::linkenddata_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::LinkEndData)


def test_uml3::0::0::linkenddata_constructor_exists():
    assert callable(uml3::0::0::LinkEndData.__init__)


def test_uml3::0::0::linkenddata_constructor_args():
    sig = inspect.signature(uml3::0::0::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::namedelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::NamedElement)


def test_uml3::0::0::namedelement_constructor_exists():
    assert callable(uml3::0::0::NamedElement.__init__)


def test_uml3::0::0::namedelement_constructor_args():
    sig = inspect.signature(uml3::0::0::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "name" in params, "Missing parameter 'name'"

def test_uml3::0::0::namedelement_has_visibility():
    assert hasattr(uml3::0::0::NamedElement, "visibility")
    descriptor = None
    for klass in uml3::0::0::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::namedelement_has_qualifiedName():
    assert hasattr(uml3::0::0::NamedElement, "qualifiedName")
    descriptor = None
    for klass in uml3::0::0::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::namedelement_has_name():
    assert hasattr(uml3::0::0::NamedElement, "name")
    descriptor = None
    for klass in uml3::0::0::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::slot_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Slot)


def test_uml3::0::0::slot_constructor_exists():
    assert callable(uml3::0::0::Slot.__init__)


def test_uml3::0::0::slot_constructor_args():
    sig = inspect.signature(uml3::0::0::Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::clause_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Clause)


def test_uml3::0::0::clause_constructor_exists():
    assert callable(uml3::0::0::Clause.__init__)


def test_uml3::0::0::clause_constructor_args():
    sig = inspect.signature(uml3::0::0::Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExceptionHandler)


def test_uml3::0::0::exceptionhandler_constructor_exists():
    assert callable(uml3::0::0::ExceptionHandler.__init__)


def test_uml3::0::0::exceptionhandler_constructor_args():
    sig = inspect.signature(uml3::0::0::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::QualifierValue)


def test_uml3::0::0::qualifiervalue_constructor_exists():
    assert callable(uml3::0::0::QualifierValue.__init__)


def test_uml3::0::0::qualifiervalue_constructor_args():
    sig = inspect.signature(uml3::0::0::QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::MultiplicityElement)


def test_uml3::0::0::multiplicityelement_constructor_exists():
    assert callable(uml3::0::0::MultiplicityElement.__init__)


def test_uml3::0::0::multiplicityelement_constructor_args():
    sig = inspect.signature(uml3::0::0::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_uml3::0::0::multiplicityelement_has_upper():
    assert hasattr(uml3::0::0::MultiplicityElement, "upper")
    descriptor = None
    for klass in uml3::0::0::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::multiplicityelement_has_isOrdered():
    assert hasattr(uml3::0::0::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in uml3::0::0::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::multiplicityelement_has_isUnique():
    assert hasattr(uml3::0::0::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in uml3::0::0::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::multiplicityelement_has_lower():
    assert hasattr(uml3::0::0::MultiplicityElement, "lower")
    descriptor = None
    for klass in uml3::0::0::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::comment_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Comment)


def test_uml3::0::0::comment_constructor_exists():
    assert callable(uml3::0::0::Comment.__init__)


def test_uml3::0::0::comment_constructor_args():
    sig = inspect.signature(uml3::0::0::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uml3::0::0::comment_has_body():
    assert hasattr(uml3::0::0::Comment, "body")
    descriptor = None
    for klass in uml3::0::0::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::behavior_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Behavior)


def test_uml3::0::0::behavior_constructor_exists():
    assert callable(uml3::0::0::Behavior.__init__)


def test_uml3::0::0::behavior_constructor_args():
    sig = inspect.signature(uml3::0::0::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_uml3::0::0::behavior_has_isReentrant():
    assert hasattr(uml3::0::0::Behavior, "isReentrant")
    descriptor = None
    for klass in uml3::0::0::Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::parameter_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Parameter)


def test_uml3::0::0::parameter_constructor_exists():
    assert callable(uml3::0::0::Parameter.__init__)


def test_uml3::0::0::parameter_constructor_args():
    sig = inspect.signature(uml3::0::0::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isStream" in params, "Missing parameter 'isStream'"

def test_uml3::0::0::parameter_has_direction():
    assert hasattr(uml3::0::0::Parameter, "direction")
    descriptor = None
    for klass in uml3::0::0::Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::parameter_has_effect():
    assert hasattr(uml3::0::0::Parameter, "effect")
    descriptor = None
    for klass in uml3::0::0::Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::parameter_has_isException():
    assert hasattr(uml3::0::0::Parameter, "isException")
    descriptor = None
    for klass in uml3::0::0::Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::parameter_has_default():
    assert hasattr(uml3::0::0::Parameter, "default")
    descriptor = None
    for klass in uml3::0::0::Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::parameter_has_isStream():
    assert hasattr(uml3::0::0::Parameter, "isStream")
    descriptor = None
    for klass in uml3::0::0::Parameter.__mro__:
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



def test_uml3::0::0::componentrealization_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ComponentRealization)


def test_uml3::0::0::componentrealization_constructor_exists():
    assert callable(uml3::0::0::ComponentRealization.__init__)


def test_uml3::0::0::componentrealization_constructor_args():
    sig = inspect.signature(uml3::0::0::ComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::interfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InterfaceRealization)


def test_uml3::0::0::interfacerealization_constructor_exists():
    assert callable(uml3::0::0::InterfaceRealization.__init__)


def test_uml3::0::0::interfacerealization_constructor_args():
    sig = inspect.signature(uml3::0::0::InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::RedefinableElement)


def test_uml3::0::0::redefinableelement_constructor_exists():
    assert callable(uml3::0::0::RedefinableElement.__init__)


def test_uml3::0::0::redefinableelement_constructor_args():
    sig = inspect.signature(uml3::0::0::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_uml3::0::0::redefinableelement_has_isLeaf():
    assert hasattr(uml3::0::0::RedefinableElement, "isLeaf")
    descriptor = None
    for klass in uml3::0::0::RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::parameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ParameterableElement)


def test_uml3::0::0::parameterableelement_constructor_exists():
    assert callable(uml3::0::0::ParameterableElement.__init__)


def test_uml3::0::0::parameterableelement_constructor_args():
    sig = inspect.signature(uml3::0::0::ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::templateparameter_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TemplateParameter)


def test_uml3::0::0::templateparameter_constructor_exists():
    assert callable(uml3::0::0::TemplateParameter.__init__)


def test_uml3::0::0::templateparameter_constructor_args():
    sig = inspect.signature(uml3::0::0::TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TemplateParameterSubstitution)


def test_uml3::0::0::templateparametersubstitution_constructor_exists():
    assert callable(uml3::0::0::TemplateParameterSubstitution.__init__)


def test_uml3::0::0::templateparametersubstitution_constructor_args():
    sig = inspect.signature(uml3::0::0::TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::templatesignature_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TemplateSignature)


def test_uml3::0::0::templatesignature_constructor_exists():
    assert callable(uml3::0::0::TemplateSignature.__init__)


def test_uml3::0::0::templatesignature_constructor_args():
    sig = inspect.signature(uml3::0::0::TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::templatebinding_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TemplateBinding)


def test_uml3::0::0::templatebinding_constructor_exists():
    assert callable(uml3::0::0::TemplateBinding.__init__)


def test_uml3::0::0::templatebinding_constructor_args():
    sig = inspect.signature(uml3::0::0::TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::templateableelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TemplateableElement)


def test_uml3::0::0::templateableelement_constructor_exists():
    assert callable(uml3::0::0::TemplateableElement.__init__)


def test_uml3::0::0::templateableelement_constructor_args():
    sig = inspect.signature(uml3::0::0::TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::property_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Property)


def test_uml3::0::0::property_constructor_exists():
    assert callable(uml3::0::0::Property.__init__)


def test_uml3::0::0::property_constructor_args():
    sig = inspect.signature(uml3::0::0::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_uml3::0::0::property_has_isDerivedUnion():
    assert hasattr(uml3::0::0::Property, "isDerivedUnion")
    descriptor = None
    for klass in uml3::0::0::Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::property_has_aggregation():
    assert hasattr(uml3::0::0::Property, "aggregation")
    descriptor = None
    for klass in uml3::0::0::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::property_has_default():
    assert hasattr(uml3::0::0::Property, "default")
    descriptor = None
    for klass in uml3::0::0::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::property_has_isDerived():
    assert hasattr(uml3::0::0::Property, "isDerived")
    descriptor = None
    for klass in uml3::0::0::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::property_has_isComposite():
    assert hasattr(uml3::0::0::Property, "isComposite")
    descriptor = None
    for klass in uml3::0::0::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::informationitem_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::InformationItem)


def test_uml3::0::0::informationitem_constructor_exists():
    assert callable(uml3::0::0::InformationItem.__init__)


def test_uml3::0::0::informationitem_constructor_args():
    sig = inspect.signature(uml3::0::0::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::signal_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Signal)


def test_uml3::0::0::signal_constructor_exists():
    assert callable(uml3::0::0::Signal.__init__)


def test_uml3::0::0::signal_constructor_args():
    sig = inspect.signature(uml3::0::0::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::datatype_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::DataType)


def test_uml3::0::0::datatype_constructor_exists():
    assert callable(uml3::0::0::DataType.__init__)


def test_uml3::0::0::datatype_constructor_args():
    sig = inspect.signature(uml3::0::0::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::artifact_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Artifact)


def test_uml3::0::0::artifact_constructor_exists():
    assert callable(uml3::0::0::Artifact.__init__)


def test_uml3::0::0::artifact_constructor_args():
    sig = inspect.signature(uml3::0::0::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_uml3::0::0::artifact_has_fileName():
    assert hasattr(uml3::0::0::Artifact, "fileName")
    descriptor = None
    for klass in uml3::0::0::Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::interface_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Interface)


def test_uml3::0::0::interface_constructor_exists():
    assert callable(uml3::0::0::Interface.__init__)


def test_uml3::0::0::interface_constructor_args():
    sig = inspect.signature(uml3::0::0::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StructuredClassifier)


def test_uml3::0::0::structuredclassifier_constructor_exists():
    assert callable(uml3::0::0::StructuredClassifier.__init__)


def test_uml3::0::0::structuredclassifier_constructor_args():
    sig = inspect.signature(uml3::0::0::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::BehavioredClassifier)


def test_uml3::0::0::behavioredclassifier_constructor_exists():
    assert callable(uml3::0::0::BehavioredClassifier.__init__)


def test_uml3::0::0::behavioredclassifier_constructor_args():
    sig = inspect.signature(uml3::0::0::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::association_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Association)


def test_uml3::0::0::association_constructor_exists():
    assert callable(uml3::0::0::Association.__init__)


def test_uml3::0::0::association_constructor_args():
    sig = inspect.signature(uml3::0::0::Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml3::0::0::association_has_isDerived():
    assert hasattr(uml3::0::0::Association, "isDerived")
    descriptor = None
    for klass in uml3::0::0::Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::usecase_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::UseCase)


def test_uml3::0::0::usecase_constructor_exists():
    assert callable(uml3::0::0::UseCase.__init__)


def test_uml3::0::0::usecase_constructor_args():
    sig = inspect.signature(uml3::0::0::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::collaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::CollaborationUse)


def test_uml3::0::0::collaborationuse_constructor_exists():
    assert callable(uml3::0::0::CollaborationUse.__init__)


def test_uml3::0::0::collaborationuse_constructor_args():
    sig = inspect.signature(uml3::0::0::CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::substitution_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Substitution)


def test_uml3::0::0::substitution_constructor_exists():
    assert callable(uml3::0::0::Substitution.__init__)


def test_uml3::0::0::substitution_constructor_args():
    sig = inspect.signature(uml3::0::0::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::generalizationset_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::GeneralizationSet)


def test_uml3::0::0::generalizationset_constructor_exists():
    assert callable(uml3::0::0::GeneralizationSet.__init__)


def test_uml3::0::0::generalizationset_constructor_args():
    sig = inspect.signature(uml3::0::0::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"
    assert "isCovering" in params, "Missing parameter 'isCovering'"

def test_uml3::0::0::generalizationset_has_isDisjoint():
    assert hasattr(uml3::0::0::GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in uml3::0::0::GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::generalizationset_has_isCovering():
    assert hasattr(uml3::0::0::GeneralizationSet, "isCovering")
    descriptor = None
    for klass in uml3::0::0::GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::generalization_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Generalization)


def test_uml3::0::0::generalization_constructor_exists():
    assert callable(uml3::0::0::Generalization.__init__)


def test_uml3::0::0::generalization_constructor_args():
    sig = inspect.signature(uml3::0::0::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_uml3::0::0::generalization_has_isSubstitutable():
    assert hasattr(uml3::0::0::Generalization, "isSubstitutable")
    descriptor = None
    for klass in uml3::0::0::Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
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



def test_uml3::0::0::activityedge_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActivityEdge)


def test_uml3::0::0::activityedge_constructor_exists():
    assert callable(uml3::0::0::ActivityEdge.__init__)


def test_uml3::0::0::activityedge_constructor_args():
    sig = inspect.signature(uml3::0::0::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::region_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Region)


def test_uml3::0::0::region_constructor_exists():
    assert callable(uml3::0::0::Region.__init__)


def test_uml3::0::0::region_constructor_args():
    sig = inspect.signature(uml3::0::0::Region.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::activitynode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ActivityNode)


def test_uml3::0::0::activitynode_constructor_exists():
    assert callable(uml3::0::0::ActivityNode.__init__)


def test_uml3::0::0::activitynode_constructor_args():
    sig = inspect.signature(uml3::0::0::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::RedefinableTemplateSignature)


def test_uml3::0::0::redefinabletemplatesignature_constructor_exists():
    assert callable(uml3::0::0::RedefinableTemplateSignature.__init__)


def test_uml3::0::0::redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(uml3::0::0::RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::state_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::State)


def test_uml3::0::0::state_constructor_exists():
    assert callable(uml3::0::0::State.__init__)


def test_uml3::0::0::state_constructor_args():
    sig = inspect.signature(uml3::0::0::State.__init__)
    params = list(sig.parameters.keys())
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"

def test_uml3::0::0::state_has_isSubmachineState():
    assert hasattr(uml3::0::0::State, "isSubmachineState")
    descriptor = None
    for klass in uml3::0::0::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::state_has_isComposite():
    assert hasattr(uml3::0::0::State, "isComposite")
    descriptor = None
    for klass in uml3::0::0::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::state_has_isSimple():
    assert hasattr(uml3::0::0::State, "isSimple")
    descriptor = None
    for klass in uml3::0::0::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::state_has_isOrthogonal():
    assert hasattr(uml3::0::0::State, "isOrthogonal")
    descriptor = None
    for klass in uml3::0::0::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::transition_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Transition)


def test_uml3::0::0::transition_constructor_exists():
    assert callable(uml3::0::0::Transition.__init__)


def test_uml3::0::0::transition_constructor_args():
    sig = inspect.signature(uml3::0::0::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml3::0::0::transition_has_kind():
    assert hasattr(uml3::0::0::Transition, "kind")
    descriptor = None
    for klass in uml3::0::0::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ExtensionPoint)


def test_uml3::0::0::extensionpoint_constructor_exists():
    assert callable(uml3::0::0::ExtensionPoint.__init__)


def test_uml3::0::0::extensionpoint_constructor_args():
    sig = inspect.signature(uml3::0::0::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::feature_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Feature)


def test_uml3::0::0::feature_constructor_exists():
    assert callable(uml3::0::0::Feature.__init__)


def test_uml3::0::0::feature_constructor_args():
    sig = inspect.signature(uml3::0::0::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml3::0::0::feature_has_isStatic():
    assert hasattr(uml3::0::0::Feature, "isStatic")
    descriptor = None
    for klass in uml3::0::0::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::classifier_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::Classifier)


def test_uml3::0::0::classifier_constructor_exists():
    assert callable(uml3::0::0::Classifier.__init__)


def test_uml3::0::0::classifier_constructor_args():
    sig = inspect.signature(uml3::0::0::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml3::0::0::classifier_has_isAbstract():
    assert hasattr(uml3::0::0::Classifier, "isAbstract")
    descriptor = None
    for klass in uml3::0::0::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::typedelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::TypedElement)


def test_uml3::0::0::typedelement_constructor_exists():
    assert callable(uml3::0::0::TypedElement.__init__)


def test_uml3::0::0::typedelement_constructor_args():
    sig = inspect.signature(uml3::0::0::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::objectnode_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ObjectNode)


def test_uml3::0::0::objectnode_constructor_exists():
    assert callable(uml3::0::0::ObjectNode.__init__)


def test_uml3::0::0::objectnode_constructor_args():
    sig = inspect.signature(uml3::0::0::ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"

def test_uml3::0::0::objectnode_has_ordering():
    assert hasattr(uml3::0::0::ObjectNode, "ordering")
    descriptor = None
    for klass in uml3::0::0::ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_uml3::0::0::objectnode_has_isControlType():
    assert hasattr(uml3::0::0::ObjectNode, "isControlType")
    descriptor = None
    for klass in uml3::0::0::ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::StructuralFeature)


def test_uml3::0::0::structuralfeature_constructor_exists():
    assert callable(uml3::0::0::StructuralFeature.__init__)


def test_uml3::0::0::structuralfeature_constructor_args():
    sig = inspect.signature(uml3::0::0::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml3::0::0::structuralfeature_has_isReadOnly():
    assert hasattr(uml3::0::0::StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in uml3::0::0::StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_uml3::0::0::connectableelement_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ConnectableElement)


def test_uml3::0::0::connectableelement_constructor_exists():
    assert callable(uml3::0::0::ConnectableElement.__init__)


def test_uml3::0::0::connectableelement_constructor_args():
    sig = inspect.signature(uml3::0::0::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml3::0::0::valuespecification_is_not_abstract():
    assert not inspect.isabstract(uml3::0::0::ValueSpecification)


def test_uml3::0::0::valuespecification_constructor_exists():
    assert callable(uml3::0::0::ValueSpecification.__init__)


def test_uml3::0::0::valuespecification_constructor_args():
    sig = inspect.signature(uml3::0::0::ValueSpecification.__init__)
    params = list(sig.parameters.keys())

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

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "read",
        "update",
        "delete",
        "create",
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
        "iterative",
        "parallel",
        "stream",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

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

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "seq",
        "break_",
        "ignore",
        "strict",
        "neg",
        "consider",
        "opt",
        "alt",
        "assert_",
        "critical",
        "par",
        "loop",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "createMessage",
        "reply",
        "synchCall",
        "asynchCall",
        "asynchSignal",
        "deleteMessage",
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

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "external",
        "internal",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "ordered",
        "FIFO",
        "unordered",
        "LIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

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

def test_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "complete",
        "unknown",
        "lost",
        "found",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"

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

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "fork",
        "junction",
        "entryPoint",
        "join",
        "exitPoint",
        "initial",
        "terminate",
        "choice",
        "shallowHistory",
        "deepHistory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"


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
uml3::0::0::ProtocolTransition_strategy = st.builds(
    uml3::0::0::ProtocolTransition,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
uml3::0::0::WriteVariableAction_strategy = st.builds(
    uml3::0::0::WriteVariableAction,
)
uml3::0::0::ClearVariableAction_strategy = st.builds(
    uml3::0::0::ClearVariableAction,
)
uml3::0::0::ReadVariableAction_strategy = st.builds(
    uml3::0::0::ReadVariableAction,
)
State_strategy = st.builds(
    State,
)
uml3::0::0::FinalState_strategy = st.builds(
    uml3::0::0::FinalState,
)
Observation_strategy = st.builds(
    Observation,
)
uml3::0::0::DurationObservation_strategy = st.builds(
    uml3::0::0::DurationObservation,
    firstEvent=
        safe_text
)
uml3::0::0::TimeObservation_strategy = st.builds(
    uml3::0::0::TimeObservation,
    firstEvent=
        safe_text
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
uml3::0::0::DurationConstraint_strategy = st.builds(
    uml3::0::0::DurationConstraint,
    firstEvent=
        safe_text
)
uml3::0::0::TimeConstraint_strategy = st.builds(
    uml3::0::0::TimeConstraint,
    firstEvent=
        safe_text
)
Interval_strategy = st.builds(
    Interval,
)
uml3::0::0::TimeInterval_strategy = st.builds(
    uml3::0::0::TimeInterval,
)
uml3::0::0::DurationInterval_strategy = st.builds(
    uml3::0::0::DurationInterval,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
uml3::0::0::CreateLinkAction_strategy = st.builds(
    uml3::0::0::CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
uml3::0::0::LinkEndCreationData_strategy = st.builds(
    uml3::0::0::LinkEndCreationData,
    isReplaceAll=
        safe_text
)
uml3::0::0::LinkEndDestructionData_strategy = st.builds(
    uml3::0::0::LinkEndDestructionData,
    isDestroyDuplicates=
        safe_text
)
uml3::0::0::DestroyLinkAction_strategy = st.builds(
    uml3::0::0::DestroyLinkAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
uml3::0::0::WriteLinkAction_strategy = st.builds(
    uml3::0::0::WriteLinkAction,
)
uml3::0::0::ReadLinkAction_strategy = st.builds(
    uml3::0::0::ReadLinkAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
uml3::0::0::AddStructuralFeatureValueAction_strategy = st.builds(
    uml3::0::0::AddStructuralFeatureValueAction,
    isReplaceAll=
        safe_text
)
uml3::0::0::RemoveStructuralFeatureValueAction_strategy = st.builds(
    uml3::0::0::RemoveStructuralFeatureValueAction,
    isRemoveDuplicates=
        safe_text
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
uml3::0::0::WriteStructuralFeatureAction_strategy = st.builds(
    uml3::0::0::WriteStructuralFeatureAction,
)
uml3::0::0::ClearStructuralFeatureAction_strategy = st.builds(
    uml3::0::0::ClearStructuralFeatureAction,
)
uml3::0::0::ReadStructuralFeatureAction_strategy = st.builds(
    uml3::0::0::ReadStructuralFeatureAction,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
uml3::0::0::ConsiderIgnoreFragment_strategy = st.builds(
    uml3::0::0::ConsiderIgnoreFragment,
)
Node_strategy = st.builds(
    Node,
)
uml3::0::0::ExecutionEnvironment_strategy = st.builds(
    uml3::0::0::ExecutionEnvironment,
)
uml3::0::0::Device_strategy = st.builds(
    uml3::0::0::Device,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
uml3::0::0::ActivityFinalNode_strategy = st.builds(
    uml3::0::0::ActivityFinalNode,
)
uml3::0::0::FlowFinalNode_strategy = st.builds(
    uml3::0::0::FlowFinalNode,
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
uml3::0::0::ExecutionOccurrenceSpecification_strategy = st.builds(
    uml3::0::0::ExecutionOccurrenceSpecification,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
uml3::0::0::SignalEvent_strategy = st.builds(
    uml3::0::0::SignalEvent,
)
uml3::0::0::SendSignalEvent_strategy = st.builds(
    uml3::0::0::SendSignalEvent,
)
uml3::0::0::CallEvent_strategy = st.builds(
    uml3::0::0::CallEvent,
)
uml3::0::0::ReceiveOperationEvent_strategy = st.builds(
    uml3::0::0::ReceiveOperationEvent,
)
uml3::0::0::AnyReceiveEvent_strategy = st.builds(
    uml3::0::0::AnyReceiveEvent,
)
uml3::0::0::ReceiveSignalEvent_strategy = st.builds(
    uml3::0::0::ReceiveSignalEvent,
)
uml3::0::0::SendOperationEvent_strategy = st.builds(
    uml3::0::0::SendOperationEvent,
)
Event_strategy = st.builds(
    Event,
)
uml3::0::0::CreationEvent_strategy = st.builds(
    uml3::0::0::CreationEvent,
)
uml3::0::0::ChangeEvent_strategy = st.builds(
    uml3::0::0::ChangeEvent,
)
uml3::0::0::TimeEvent_strategy = st.builds(
    uml3::0::0::TimeEvent,
    isRelative=
        safe_text
)
uml3::0::0::DestructionEvent_strategy = st.builds(
    uml3::0::0::DestructionEvent,
)
uml3::0::0::MessageEvent_strategy = st.builds(
    uml3::0::0::MessageEvent,
)
uml3::0::0::ExecutionEvent_strategy = st.builds(
    uml3::0::0::ExecutionEvent,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
uml3::0::0::BehaviorExecutionSpecification_strategy = st.builds(
    uml3::0::0::BehaviorExecutionSpecification,
)
uml3::0::0::ActionExecutionSpecification_strategy = st.builds(
    uml3::0::0::ActionExecutionSpecification,
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
Constraint_strategy = st.builds(
    Constraint,
)
uml3::0::0::IntervalConstraint_strategy = st.builds(
    uml3::0::0::IntervalConstraint,
)
uml3::0::0::PartDecomposition_strategy = st.builds(
    uml3::0::0::PartDecomposition,
)
uml3::0::0::InteractionConstraint_strategy = st.builds(
    uml3::0::0::InteractionConstraint,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
uml3::0::0::MessageOccurrenceSpecification_strategy = st.builds(
    uml3::0::0::MessageOccurrenceSpecification,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
uml3::0::0::StateInvariant_strategy = st.builds(
    uml3::0::0::StateInvariant,
)
uml3::0::0::Continuation_strategy = st.builds(
    uml3::0::0::Continuation,
    setting=
        safe_text
)
uml3::0::0::InteractionUse_strategy = st.builds(
    uml3::0::0::InteractionUse,
)
uml3::0::0::OccurrenceSpecification_strategy = st.builds(
    uml3::0::0::OccurrenceSpecification,
)
uml3::0::0::CombinedFragment_strategy = st.builds(
    uml3::0::0::CombinedFragment,
    interactionOperator=
        safe_text
)
uml3::0::0::ExecutionSpecification_strategy = st.builds(
    uml3::0::0::ExecutionSpecification,
)
uml3::0::0::Gate_strategy = st.builds(
    uml3::0::0::Gate,
)
InputPin_strategy = st.builds(
    InputPin,
)
uml3::0::0::ActionInputPin_strategy = st.builds(
    uml3::0::0::ActionInputPin,
)
uml3::0::0::ValuePin_strategy = st.builds(
    uml3::0::0::ValuePin,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
uml3::0::0::FinalNode_strategy = st.builds(
    uml3::0::0::FinalNode,
)
uml3::0::0::ForkNode_strategy = st.builds(
    uml3::0::0::ForkNode,
)
uml3::0::0::DecisionNode_strategy = st.builds(
    uml3::0::0::DecisionNode,
)
uml3::0::0::MergeNode_strategy = st.builds(
    uml3::0::0::MergeNode,
)
uml3::0::0::InitialNode_strategy = st.builds(
    uml3::0::0::InitialNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
uml3::0::0::ObjectFlow_strategy = st.builds(
    uml3::0::0::ObjectFlow,
    isMulticast=
        safe_text,
    isMultireceive=
        safe_text
)
uml3::0::0::ControlFlow_strategy = st.builds(
    uml3::0::0::ControlFlow,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
uml3::0::0::ExpansionRegion_strategy = st.builds(
    uml3::0::0::ExpansionRegion,
    mode=
        safe_text
)
uml3::0::0::LoopNode_strategy = st.builds(
    uml3::0::0::LoopNode,
    isTestedFirst=
        safe_text
)
uml3::0::0::SequenceNode_strategy = st.builds(
    uml3::0::0::SequenceNode,
)
CallAction_strategy = st.builds(
    CallAction,
)
uml3::0::0::CallBehaviorAction_strategy = st.builds(
    uml3::0::0::CallBehaviorAction,
)
uml3::0::0::CallOperationAction_strategy = st.builds(
    uml3::0::0::CallOperationAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
uml3::0::0::SendObjectAction_strategy = st.builds(
    uml3::0::0::SendObjectAction,
)
uml3::0::0::BroadcastSignalAction_strategy = st.builds(
    uml3::0::0::BroadcastSignalAction,
)
uml3::0::0::SendSignalAction_strategy = st.builds(
    uml3::0::0::SendSignalAction,
)
uml3::0::0::CallAction_strategy = st.builds(
    uml3::0::0::CallAction,
    isSynchronous=
        safe_text
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
uml3::0::0::CentralBufferNode_strategy = st.builds(
    uml3::0::0::CentralBufferNode,
)
uml3::0::0::ExpansionNode_strategy = st.builds(
    uml3::0::0::ExpansionNode,
)
uml3::0::0::ActivityParameterNode_strategy = st.builds(
    uml3::0::0::ActivityParameterNode,
)
Pin_strategy = st.builds(
    Pin,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
uml3::0::0::InterruptibleActivityRegion_strategy = st.builds(
    uml3::0::0::InterruptibleActivityRegion,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
uml3::0::0::ControlNode_strategy = st.builds(
    uml3::0::0::ControlNode,
)
uml3::0::0::ExecutableNode_strategy = st.builds(
    uml3::0::0::ExecutableNode,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
uml3::0::0::Action_strategy = st.builds(
    uml3::0::0::Action,
)
uml3::0::0::OutputPin_strategy = st.builds(
    uml3::0::0::OutputPin,
)
uml3::0::0::InputPin_strategy = st.builds(
    uml3::0::0::InputPin,
)
Action_strategy = st.builds(
    Action,
)
uml3::0::0::ReadSelfAction_strategy = st.builds(
    uml3::0::0::ReadSelfAction,
)
uml3::0::0::VariableAction_strategy = st.builds(
    uml3::0::0::VariableAction,
)
uml3::0::0::ClearAssociationAction_strategy = st.builds(
    uml3::0::0::ClearAssociationAction,
)
uml3::0::0::ValueSpecificationAction_strategy = st.builds(
    uml3::0::0::ValueSpecificationAction,
)
uml3::0::0::TestIdentityAction_strategy = st.builds(
    uml3::0::0::TestIdentityAction,
)
uml3::0::0::StructuralFeatureAction_strategy = st.builds(
    uml3::0::0::StructuralFeatureAction,
)
uml3::0::0::DestroyObjectAction_strategy = st.builds(
    uml3::0::0::DestroyObjectAction,
    isDestroyOwnedObjects=
        safe_text,
    isDestroyLinks=
        safe_text
)
uml3::0::0::CreateObjectAction_strategy = st.builds(
    uml3::0::0::CreateObjectAction,
)
uml3::0::0::RaiseExceptionAction_strategy = st.builds(
    uml3::0::0::RaiseExceptionAction,
)
uml3::0::0::InvocationAction_strategy = st.builds(
    uml3::0::0::InvocationAction,
)
uml3::0::0::LinkAction_strategy = st.builds(
    uml3::0::0::LinkAction,
)
uml3::0::0::OpaqueAction_strategy = st.builds(
    uml3::0::0::OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
uml3::0::0::FunctionBehavior_strategy = st.builds(
    uml3::0::0::FunctionBehavior,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
uml3::0::0::LiteralUnlimitedNatural_strategy = st.builds(
    uml3::0::0::LiteralUnlimitedNatural,
    value=
        safe_text
)
uml3::0::0::LiteralBoolean_strategy = st.builds(
    uml3::0::0::LiteralBoolean,
    value=
        safe_text
)
uml3::0::0::LiteralString_strategy = st.builds(
    uml3::0::0::LiteralString,
    value=
        safe_text
)
uml3::0::0::LiteralNull_strategy = st.builds(
    uml3::0::0::LiteralNull,
)
uml3::0::0::LiteralInteger_strategy = st.builds(
    uml3::0::0::LiteralInteger,
    value=
        safe_text
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
uml3::0::0::EnumerationLiteral_strategy = st.builds(
    uml3::0::0::EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
uml3::0::0::PrimitiveType_strategy = st.builds(
    uml3::0::0::PrimitiveType,
)
uml3::0::0::Enumeration_strategy = st.builds(
    uml3::0::0::Enumeration,
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
uml3::0::0::ConnectableElementTemplateParameter_strategy = st.builds(
    uml3::0::0::ConnectableElementTemplateParameter,
)
uml3::0::0::ClassifierTemplateParameter_strategy = st.builds(
    uml3::0::0::ClassifierTemplateParameter,
    allowSubstitutable=
        safe_text
)
uml3::0::0::OperationTemplateParameter_strategy = st.builds(
    uml3::0::0::OperationTemplateParameter,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
uml3::0::0::EncapsulatedClassifier_strategy = st.builds(
    uml3::0::0::EncapsulatedClassifier,
)
Package_strategy = st.builds(
    Package,
)
uml3::0::0::Model_strategy = st.builds(
    uml3::0::0::Model,
    viewpoint=
        safe_text
)
uml3::0::0::Profile_strategy = st.builds(
    uml3::0::0::Profile,
)
Association_strategy = st.builds(
    Association,
)
uml3::0::0::CommunicationPath_strategy = st.builds(
    uml3::0::0::CommunicationPath,
)
Vertex_strategy = st.builds(
    Vertex,
)
uml3::0::0::ConnectionPointReference_strategy = st.builds(
    uml3::0::0::ConnectionPointReference,
)
Property_strategy = st.builds(
    Property,
)
uml3::0::0::ExtensionEnd_strategy = st.builds(
    uml3::0::0::ExtensionEnd,
)
uml3::0::0::Port_strategy = st.builds(
    uml3::0::0::Port,
    isBehavior=
        safe_text,
    isService=
        safe_text
)
uml3::0::0::Pseudostate_strategy = st.builds(
    uml3::0::0::Pseudostate,
    kind=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
uml3::0::0::Interaction_strategy = st.builds(
    uml3::0::0::Interaction,
)
uml3::0::0::OpaqueBehavior_strategy = st.builds(
    uml3::0::0::OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)
uml3::0::0::Activity_strategy = st.builds(
    uml3::0::0::Activity,
    isReadOnly=
        safe_text,
    isSingleExecution=
        safe_text
)
uml3::0::0::StateMachine_strategy = st.builds(
    uml3::0::0::StateMachine,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
uml3::0::0::ProtocolStateMachine_strategy = st.builds(
    uml3::0::0::ProtocolStateMachine,
)
uml3::0::0::Extension_strategy = st.builds(
    uml3::0::0::Extension,
    isRequired=
        safe_text
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
uml3::0::0::Actor_strategy = st.builds(
    uml3::0::0::Actor,
)
uml3::0::0::Collaboration_strategy = st.builds(
    uml3::0::0::Collaboration,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
Class_strategy = st.builds(
    Class,
)
uml3::0::0::Component_strategy = st.builds(
    uml3::0::0::Component,
    isIndirectlyInstantiated=
        safe_text
)
uml3::0::0::Stereotype_strategy = st.builds(
    uml3::0::0::Stereotype,
)
uml3::0::0::AssociationClass_strategy = st.builds(
    uml3::0::0::AssociationClass,
)
Feature_strategy = st.builds(
    Feature,
)
uml3::0::0::Connector_strategy = st.builds(
    uml3::0::0::Connector,
    kind=
        safe_text
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
uml3::0::0::Reception_strategy = st.builds(
    uml3::0::0::Reception,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
Artifact_strategy = st.builds(
    Artifact,
)
uml3::0::0::DeploymentSpecification_strategy = st.builds(
    uml3::0::0::DeploymentSpecification,
    deploymentLocation=
        safe_text,
    executionLocation=
        safe_text
)
uml3::0::0::Class_strategy = st.builds(
    uml3::0::0::Class,
    isActive=
        safe_text
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
uml3::0::0::Node_strategy = st.builds(
    uml3::0::0::Node,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
uml3::0::0::TimeExpression_strategy = st.builds(
    uml3::0::0::TimeExpression,
)
uml3::0::0::InstanceValue_strategy = st.builds(
    uml3::0::0::InstanceValue,
)
uml3::0::0::Duration_strategy = st.builds(
    uml3::0::0::Duration,
)
uml3::0::0::LiteralSpecification_strategy = st.builds(
    uml3::0::0::LiteralSpecification,
)
uml3::0::0::Expression_strategy = st.builds(
    uml3::0::0::Expression,
    symbol=
        safe_text
)
uml3::0::0::Interval_strategy = st.builds(
    uml3::0::0::Interval,
)
uml3::0::0::OpaqueExpression_strategy = st.builds(
    uml3::0::0::OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
Dependency_strategy = st.builds(
    Dependency,
)
uml3::0::0::Usage_strategy = st.builds(
    uml3::0::0::Usage,
)
uml3::0::0::Deployment_strategy = st.builds(
    uml3::0::0::Deployment,
)
uml3::0::0::Abstraction_strategy = st.builds(
    uml3::0::0::Abstraction,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
uml3::0::0::Manifestation_strategy = st.builds(
    uml3::0::0::Manifestation,
)
uml3::0::0::Realization_strategy = st.builds(
    uml3::0::0::Realization,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
uml3::0::0::Pin_strategy = st.builds(
    uml3::0::0::Pin,
    isControl=
        safe_text
)
uml3::0::0::ConnectorEnd_strategy = st.builds(
    uml3::0::0::ConnectorEnd,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
uml3::0::0::Variable_strategy = st.builds(
    uml3::0::0::Variable,
)
uml3::0::0::ConditionalNode_strategy = st.builds(
    uml3::0::0::ConditionalNode,
    isDeterminate=
        safe_text,
    isAssured=
        safe_text
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
uml3::0::0::DataStoreNode_strategy = st.builds(
    uml3::0::0::DataStoreNode,
)
uml3::0::0::JoinNode_strategy = st.builds(
    uml3::0::0::JoinNode,
    isCombineDuplicate=
        safe_text
)
uml3::0::0::StartObjectBehaviorAction_strategy = st.builds(
    uml3::0::0::StartObjectBehaviorAction,
)
uml3::0::0::ReduceAction_strategy = st.builds(
    uml3::0::0::ReduceAction,
    isOrdered=
        safe_text
)
uml3::0::0::UnmarshallAction_strategy = st.builds(
    uml3::0::0::UnmarshallAction,
)
uml3::0::0::ReplyAction_strategy = st.builds(
    uml3::0::0::ReplyAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
uml3::0::0::AcceptCallAction_strategy = st.builds(
    uml3::0::0::AcceptCallAction,
)
uml3::0::0::ReadLinkObjectEndAction_strategy = st.builds(
    uml3::0::0::ReadLinkObjectEndAction,
)
uml3::0::0::AcceptEventAction_strategy = st.builds(
    uml3::0::0::AcceptEventAction,
    isUnmarshall=
        safe_text
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
uml3::0::0::CreateLinkObjectAction_strategy = st.builds(
    uml3::0::0::CreateLinkObjectAction,
)
uml3::0::0::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml3::0::0::ReadLinkObjectEndQualifierAction,
)
uml3::0::0::StartClassifierBehaviorAction_strategy = st.builds(
    uml3::0::0::StartClassifierBehaviorAction,
)
uml3::0::0::ReadIsClassifiedObjectAction_strategy = st.builds(
    uml3::0::0::ReadIsClassifiedObjectAction,
    isDirect=
        safe_text
)
uml3::0::0::ReclassifyObjectAction_strategy = st.builds(
    uml3::0::0::ReclassifyObjectAction,
    isReplaceAll=
        safe_text
)
uml3::0::0::ReadExtentAction_strategy = st.builds(
    uml3::0::0::ReadExtentAction,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
uml3::0::0::RemoveVariableValueAction_strategy = st.builds(
    uml3::0::0::RemoveVariableValueAction,
    isRemoveDuplicates=
        safe_text
)
uml3::0::0::AddVariableValueAction_strategy = st.builds(
    uml3::0::0::AddVariableValueAction,
    isReplaceAll=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
uml3::0::0::ProtocolConformance_strategy = st.builds(
    uml3::0::0::ProtocolConformance,
)
uml3::0::0::PackageImport_strategy = st.builds(
    uml3::0::0::PackageImport,
    visibility=
        safe_text
)
uml3::0::0::ElementImport_strategy = st.builds(
    uml3::0::0::ElementImport,
    visibility=
        safe_text,
    alias=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
uml3::0::0::DirectedRelationship_strategy = st.builds(
    uml3::0::0::DirectedRelationship,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml3::0::0::MessageEnd_strategy = st.builds(
    uml3::0::0::MessageEnd,
)
uml3::0::0::Namespace_strategy = st.builds(
    uml3::0::0::Namespace,
)
uml3::0::0::DeploymentTarget_strategy = st.builds(
    uml3::0::0::DeploymentTarget,
)
uml3::0::0::ActivityPartition_strategy = st.builds(
    uml3::0::0::ActivityPartition,
    isDimension=
        safe_text,
    isExternal=
        safe_text
)
uml3::0::0::Lifeline_strategy = st.builds(
    uml3::0::0::Lifeline,
)
uml3::0::0::Include_strategy = st.builds(
    uml3::0::0::Include,
)
uml3::0::0::Message_strategy = st.builds(
    uml3::0::0::Message,
    messageSort=
        safe_text,
    messageKind=
        safe_text
)
uml3::0::0::InteractionFragment_strategy = st.builds(
    uml3::0::0::InteractionFragment,
)
uml3::0::0::ParameterSet_strategy = st.builds(
    uml3::0::0::ParameterSet,
)
uml3::0::0::GeneralOrdering_strategy = st.builds(
    uml3::0::0::GeneralOrdering,
)
uml3::0::0::DeployedArtifact_strategy = st.builds(
    uml3::0::0::DeployedArtifact,
)
uml3::0::0::Vertex_strategy = st.builds(
    uml3::0::0::Vertex,
)
uml3::0::0::Trigger_strategy = st.builds(
    uml3::0::0::Trigger,
)
uml3::0::0::Extend_strategy = st.builds(
    uml3::0::0::Extend,
)
uml3::0::0::ProfileApplication_strategy = st.builds(
    uml3::0::0::ProfileApplication,
    isStrict=
        safe_text
)
uml3::0::0::PackageableElement_strategy = st.builds(
    uml3::0::0::PackageableElement,
)
uml3::0::0::PackageMerge_strategy = st.builds(
    uml3::0::0::PackageMerge,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
uml3::0::0::StringExpression_strategy = st.builds(
    uml3::0::0::StringExpression,
)
uml3::0::0::Operation_strategy = st.builds(
    uml3::0::0::Operation,
    isQuery=
        safe_text,
    upper=
        safe_text,
    lower=
        safe_text,
    isOrdered=
        safe_text,
    isUnique=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml3::0::0::InformationFlow_strategy = st.builds(
    uml3::0::0::InformationFlow,
)
uml3::0::0::InstanceSpecification_strategy = st.builds(
    uml3::0::0::InstanceSpecification,
)
uml3::0::0::Constraint_strategy = st.builds(
    uml3::0::0::Constraint,
)
uml3::0::0::Observation_strategy = st.builds(
    uml3::0::0::Observation,
)
uml3::0::0::Event_strategy = st.builds(
    uml3::0::0::Event,
)
uml3::0::0::Type_strategy = st.builds(
    uml3::0::0::Type,
)
uml3::0::0::Dependency_strategy = st.builds(
    uml3::0::0::Dependency,
)
Namespace_strategy = st.builds(
    Namespace,
)
uml3::0::0::InteractionOperand_strategy = st.builds(
    uml3::0::0::InteractionOperand,
)
uml3::0::0::BehavioralFeature_strategy = st.builds(
    uml3::0::0::BehavioralFeature,
    concurrency=
        safe_text,
    isAbstract=
        safe_text
)
uml3::0::0::StructuredActivityNode_strategy = st.builds(
    uml3::0::0::StructuredActivityNode,
    mustIsolate=
        safe_text
)
uml3::0::0::Package_strategy = st.builds(
    uml3::0::0::Package,
)
uml3::0::0::Element_strategy = st.builds(
    uml3::0::0::Element,
)
Element_strategy = st.builds(
    Element,
)
uml3::0::0::Relationship_strategy = st.builds(
    uml3::0::0::Relationship,
)
uml3::0::0::ActivityGroup_strategy = st.builds(
    uml3::0::0::ActivityGroup,
)
uml3::0::0::Image_strategy = st.builds(
    uml3::0::0::Image,
    format=
        safe_text,
    location=
        safe_text,
    content=
        safe_text
)
uml3::0::0::LinkEndData_strategy = st.builds(
    uml3::0::0::LinkEndData,
)
uml3::0::0::NamedElement_strategy = st.builds(
    uml3::0::0::NamedElement,
    visibility=
        safe_text,
    qualifiedName=
        safe_text,
    name=
        safe_text
)
uml3::0::0::Slot_strategy = st.builds(
    uml3::0::0::Slot,
)
uml3::0::0::Clause_strategy = st.builds(
    uml3::0::0::Clause,
)
uml3::0::0::ExceptionHandler_strategy = st.builds(
    uml3::0::0::ExceptionHandler,
)
uml3::0::0::QualifierValue_strategy = st.builds(
    uml3::0::0::QualifierValue,
)
uml3::0::0::MultiplicityElement_strategy = st.builds(
    uml3::0::0::MultiplicityElement,
    upper=
        safe_text,
    isOrdered=
        safe_text,
    isUnique=
        safe_text,
    lower=
        safe_text
)
uml3::0::0::Comment_strategy = st.builds(
    uml3::0::0::Comment,
    body=
        safe_text
)
uml3::0::0::Behavior_strategy = st.builds(
    uml3::0::0::Behavior,
    isReentrant=
        safe_text
)
uml3::0::0::Parameter_strategy = st.builds(
    uml3::0::0::Parameter,
    direction=
        safe_text,
    effect=
        safe_text,
    isException=
        safe_text,
    default=
        safe_text,
    isStream=
        safe_text
)
Realization_strategy = st.builds(
    Realization,
)
uml3::0::0::ComponentRealization_strategy = st.builds(
    uml3::0::0::ComponentRealization,
)
uml3::0::0::InterfaceRealization_strategy = st.builds(
    uml3::0::0::InterfaceRealization,
)
uml3::0::0::RedefinableElement_strategy = st.builds(
    uml3::0::0::RedefinableElement,
    isLeaf=
        safe_text
)
uml3::0::0::ParameterableElement_strategy = st.builds(
    uml3::0::0::ParameterableElement,
)
uml3::0::0::TemplateParameter_strategy = st.builds(
    uml3::0::0::TemplateParameter,
)
uml3::0::0::TemplateParameterSubstitution_strategy = st.builds(
    uml3::0::0::TemplateParameterSubstitution,
)
uml3::0::0::TemplateSignature_strategy = st.builds(
    uml3::0::0::TemplateSignature,
)
uml3::0::0::TemplateBinding_strategy = st.builds(
    uml3::0::0::TemplateBinding,
)
uml3::0::0::TemplateableElement_strategy = st.builds(
    uml3::0::0::TemplateableElement,
)
uml3::0::0::Property_strategy = st.builds(
    uml3::0::0::Property,
    isDerivedUnion=
        safe_text,
    aggregation=
        safe_text,
    default=
        safe_text,
    isDerived=
        safe_text,
    isComposite=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uml3::0::0::InformationItem_strategy = st.builds(
    uml3::0::0::InformationItem,
)
uml3::0::0::Signal_strategy = st.builds(
    uml3::0::0::Signal,
)
uml3::0::0::DataType_strategy = st.builds(
    uml3::0::0::DataType,
)
uml3::0::0::Artifact_strategy = st.builds(
    uml3::0::0::Artifact,
    fileName=
        safe_text
)
uml3::0::0::Interface_strategy = st.builds(
    uml3::0::0::Interface,
)
uml3::0::0::StructuredClassifier_strategy = st.builds(
    uml3::0::0::StructuredClassifier,
)
uml3::0::0::BehavioredClassifier_strategy = st.builds(
    uml3::0::0::BehavioredClassifier,
)
uml3::0::0::Association_strategy = st.builds(
    uml3::0::0::Association,
    isDerived=
        safe_text
)
uml3::0::0::UseCase_strategy = st.builds(
    uml3::0::0::UseCase,
)
uml3::0::0::CollaborationUse_strategy = st.builds(
    uml3::0::0::CollaborationUse,
)
uml3::0::0::Substitution_strategy = st.builds(
    uml3::0::0::Substitution,
)
uml3::0::0::GeneralizationSet_strategy = st.builds(
    uml3::0::0::GeneralizationSet,
    isDisjoint=
        safe_text,
    isCovering=
        safe_text
)
uml3::0::0::Generalization_strategy = st.builds(
    uml3::0::0::Generalization,
    isSubstitutable=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
uml3::0::0::ActivityEdge_strategy = st.builds(
    uml3::0::0::ActivityEdge,
)
uml3::0::0::Region_strategy = st.builds(
    uml3::0::0::Region,
)
uml3::0::0::ActivityNode_strategy = st.builds(
    uml3::0::0::ActivityNode,
)
uml3::0::0::RedefinableTemplateSignature_strategy = st.builds(
    uml3::0::0::RedefinableTemplateSignature,
)
uml3::0::0::State_strategy = st.builds(
    uml3::0::0::State,
    isSubmachineState=
        safe_text,
    isComposite=
        safe_text,
    isSimple=
        safe_text,
    isOrthogonal=
        safe_text
)
uml3::0::0::Transition_strategy = st.builds(
    uml3::0::0::Transition,
    kind=
        safe_text
)
uml3::0::0::ExtensionPoint_strategy = st.builds(
    uml3::0::0::ExtensionPoint,
)
uml3::0::0::Feature_strategy = st.builds(
    uml3::0::0::Feature,
    isStatic=
        safe_text
)
uml3::0::0::Classifier_strategy = st.builds(
    uml3::0::0::Classifier,
    isAbstract=
        safe_text
)
uml3::0::0::TypedElement_strategy = st.builds(
    uml3::0::0::TypedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uml3::0::0::ObjectNode_strategy = st.builds(
    uml3::0::0::ObjectNode,
    ordering=
        safe_text,
    isControlType=
        safe_text
)
uml3::0::0::StructuralFeature_strategy = st.builds(
    uml3::0::0::StructuralFeature,
    isReadOnly=
        safe_text
)
uml3::0::0::ConnectableElement_strategy = st.builds(
    uml3::0::0::ConnectableElement,
)
uml3::0::0::ValueSpecification_strategy = st.builds(
    uml3::0::0::ValueSpecification,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=uml3::0::0::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml3::0::0::protocoltransition_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ProtocolTransition)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=uml3::0::0::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::writevariableaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::WriteVariableAction)

@given(instance=uml3::0::0::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::clearvariableaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ClearVariableAction)

@given(instance=uml3::0::0::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readvariableaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadVariableAction)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=uml3::0::0::FinalState_strategy)
@settings(max_examples=50)
def test_uml3::0::0::finalstate_instantiation(instance):
    assert isinstance(instance, uml3::0::0::FinalState)

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=uml3::0::0::DurationObservation_strategy)
@settings(max_examples=50)
def test_uml3::0::0::durationobservation_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DurationObservation)

@given(instance=uml3::0::0::DurationObservation_strategy)
def test_uml3::0::0::durationobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml3::0::0::DurationObservation_strategy)
def test_uml3::0::0::durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml3::0::0::TimeObservation_strategy)
@settings(max_examples=50)
def test_uml3::0::0::timeobservation_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TimeObservation)

@given(instance=uml3::0::0::TimeObservation_strategy)
def test_uml3::0::0::timeobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml3::0::0::TimeObservation_strategy)
def test_uml3::0::0::timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=uml3::0::0::DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml3::0::0::durationconstraint_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DurationConstraint)

@given(instance=uml3::0::0::DurationConstraint_strategy)
def test_uml3::0::0::durationconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml3::0::0::DurationConstraint_strategy)
def test_uml3::0::0::durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml3::0::0::TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml3::0::0::timeconstraint_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TimeConstraint)

@given(instance=uml3::0::0::TimeConstraint_strategy)
def test_uml3::0::0::timeconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml3::0::0::TimeConstraint_strategy)
def test_uml3::0::0::timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=uml3::0::0::TimeInterval_strategy)
@settings(max_examples=50)
def test_uml3::0::0::timeinterval_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TimeInterval)

@given(instance=uml3::0::0::DurationInterval_strategy)
@settings(max_examples=50)
def test_uml3::0::0::durationinterval_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DurationInterval)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=uml3::0::0::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::createlinkaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CreateLinkAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=uml3::0::0::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml3::0::0::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LinkEndCreationData)

@given(instance=uml3::0::0::LinkEndCreationData_strategy)
def test_uml3::0::0::linkendcreationdata_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml3::0::0::LinkEndCreationData_strategy)
def test_uml3::0::0::linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml3::0::0::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_uml3::0::0::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LinkEndDestructionData)

@given(instance=uml3::0::0::LinkEndDestructionData_strategy)
def test_uml3::0::0::linkenddestructiondata_isDestroyDuplicates_type(instance):
    assert isinstance(instance.isDestroyDuplicates, str)


@given(instance=uml3::0::0::LinkEndDestructionData_strategy)
def test_uml3::0::0::linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=uml3::0::0::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::destroylinkaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DestroyLinkAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=uml3::0::0::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::writelinkaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::WriteLinkAction)

@given(instance=uml3::0::0::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readlinkaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadLinkAction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=uml3::0::0::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::AddStructuralFeatureValueAction)

@given(instance=uml3::0::0::AddStructuralFeatureValueAction_strategy)
def test_uml3::0::0::addstructuralfeaturevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml3::0::0::AddStructuralFeatureValueAction_strategy)
def test_uml3::0::0::addstructuralfeaturevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml3::0::0::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::RemoveStructuralFeatureValueAction)

@given(instance=uml3::0::0::RemoveStructuralFeatureValueAction_strategy)
def test_uml3::0::0::removestructuralfeaturevalueaction_isRemoveDuplicates_type(instance):
    assert isinstance(instance.isRemoveDuplicates, str)


@given(instance=uml3::0::0::RemoveStructuralFeatureValueAction_strategy)
def test_uml3::0::0::removestructuralfeaturevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=uml3::0::0::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::WriteStructuralFeatureAction)

@given(instance=uml3::0::0::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ClearStructuralFeatureAction)

@given(instance=uml3::0::0::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadStructuralFeatureAction)

@given(instance=CombinedFragment_strategy)
@settings(max_examples=50)
def test_combinedfragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)

@given(instance=uml3::0::0::ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_uml3::0::0::considerignorefragment_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ConsiderIgnoreFragment)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=uml3::0::0::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml3::0::0::executionenvironment_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExecutionEnvironment)

@given(instance=uml3::0::0::Device_strategy)
@settings(max_examples=50)
def test_uml3::0::0::device_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Device)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=uml3::0::0::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::activityfinalnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActivityFinalNode)

@given(instance=uml3::0::0::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::flowfinalnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::FlowFinalNode)

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=uml3::0::0::ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExecutionOccurrenceSpecification)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=uml3::0::0::SignalEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::signalevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::SignalEvent)

@given(instance=uml3::0::0::SendSignalEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::sendsignalevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::SendSignalEvent)

@given(instance=uml3::0::0::CallEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::callevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CallEvent)

@given(instance=uml3::0::0::ReceiveOperationEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::receiveoperationevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReceiveOperationEvent)

@given(instance=uml3::0::0::AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::anyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::AnyReceiveEvent)

@given(instance=uml3::0::0::ReceiveSignalEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::receivesignalevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReceiveSignalEvent)

@given(instance=uml3::0::0::SendOperationEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::sendoperationevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::SendOperationEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=uml3::0::0::CreationEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::creationevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CreationEvent)

@given(instance=uml3::0::0::ChangeEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::changeevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ChangeEvent)

@given(instance=uml3::0::0::TimeEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::timeevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TimeEvent)

@given(instance=uml3::0::0::TimeEvent_strategy)
def test_uml3::0::0::timeevent_isRelative_type(instance):
    assert isinstance(instance.isRelative, str)


@given(instance=uml3::0::0::TimeEvent_strategy)
def test_uml3::0::0::timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=uml3::0::0::DestructionEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::destructionevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DestructionEvent)

@given(instance=uml3::0::0::MessageEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::messageevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::MessageEvent)

@given(instance=uml3::0::0::ExecutionEvent_strategy)
@settings(max_examples=50)
def test_uml3::0::0::executionevent_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExecutionEvent)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=uml3::0::0::BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::BehaviorExecutionSpecification)

@given(instance=uml3::0::0::ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActionExecutionSpecification)

@given(instance=InteractionUse_strategy)
@settings(max_examples=50)
def test_interactionuse_instantiation(instance):
    assert isinstance(instance, InteractionUse)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=uml3::0::0::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml3::0::0::intervalconstraint_instantiation(instance):
    assert isinstance(instance, uml3::0::0::IntervalConstraint)

@given(instance=uml3::0::0::PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml3::0::0::partdecomposition_instantiation(instance):
    assert isinstance(instance, uml3::0::0::PartDecomposition)

@given(instance=uml3::0::0::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interactionconstraint_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InteractionConstraint)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=uml3::0::0::MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::MessageOccurrenceSpecification)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=uml3::0::0::StateInvariant_strategy)
@settings(max_examples=50)
def test_uml3::0::0::stateinvariant_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StateInvariant)

@given(instance=uml3::0::0::Continuation_strategy)
@settings(max_examples=50)
def test_uml3::0::0::continuation_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Continuation)

@given(instance=uml3::0::0::Continuation_strategy)
def test_uml3::0::0::continuation_setting_type(instance):
    assert isinstance(instance.setting, str)


@given(instance=uml3::0::0::Continuation_strategy)
def test_uml3::0::0::continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=uml3::0::0::InteractionUse_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interactionuse_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InteractionUse)

@given(instance=uml3::0::0::OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::occurrencespecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::OccurrenceSpecification)

@given(instance=uml3::0::0::CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml3::0::0::combinedfragment_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CombinedFragment)

@given(instance=uml3::0::0::CombinedFragment_strategy)
def test_uml3::0::0::combinedfragment_interactionOperator_type(instance):
    assert isinstance(instance.interactionOperator, str)


@given(instance=uml3::0::0::CombinedFragment_strategy)
def test_uml3::0::0::combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=uml3::0::0::ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::executionspecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExecutionSpecification)

@given(instance=uml3::0::0::Gate_strategy)
@settings(max_examples=50)
def test_uml3::0::0::gate_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Gate)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=uml3::0::0::ActionInputPin_strategy)
@settings(max_examples=50)
def test_uml3::0::0::actioninputpin_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActionInputPin)

@given(instance=uml3::0::0::ValuePin_strategy)
@settings(max_examples=50)
def test_uml3::0::0::valuepin_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ValuePin)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=uml3::0::0::FinalNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::finalnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::FinalNode)

@given(instance=uml3::0::0::ForkNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::forknode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ForkNode)

@given(instance=uml3::0::0::DecisionNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::decisionnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DecisionNode)

@given(instance=uml3::0::0::MergeNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::mergenode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::MergeNode)

@given(instance=uml3::0::0::InitialNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::initialnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InitialNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=uml3::0::0::ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml3::0::0::objectflow_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ObjectFlow)

@given(instance=uml3::0::0::ObjectFlow_strategy)
def test_uml3::0::0::objectflow_isMulticast_type(instance):
    assert isinstance(instance.isMulticast, str)


@given(instance=uml3::0::0::ObjectFlow_strategy)
def test_uml3::0::0::objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=uml3::0::0::ObjectFlow_strategy)
def test_uml3::0::0::objectflow_isMultireceive_type(instance):
    assert isinstance(instance.isMultireceive, str)


@given(instance=uml3::0::0::ObjectFlow_strategy)
def test_uml3::0::0::objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=uml3::0::0::ControlFlow_strategy)
@settings(max_examples=50)
def test_uml3::0::0::controlflow_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ControlFlow)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=uml3::0::0::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml3::0::0::expansionregion_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExpansionRegion)

@given(instance=uml3::0::0::ExpansionRegion_strategy)
def test_uml3::0::0::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=uml3::0::0::ExpansionRegion_strategy)
def test_uml3::0::0::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=uml3::0::0::LoopNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::loopnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LoopNode)

@given(instance=uml3::0::0::LoopNode_strategy)
def test_uml3::0::0::loopnode_isTestedFirst_type(instance):
    assert isinstance(instance.isTestedFirst, str)


@given(instance=uml3::0::0::LoopNode_strategy)
def test_uml3::0::0::loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=uml3::0::0::SequenceNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::sequencenode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::SequenceNode)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=uml3::0::0::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::callbehavioraction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CallBehaviorAction)

@given(instance=uml3::0::0::CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::calloperationaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CallOperationAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=uml3::0::0::SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::sendobjectaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::SendObjectAction)

@given(instance=uml3::0::0::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::BroadcastSignalAction)

@given(instance=uml3::0::0::SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::sendsignalaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::SendSignalAction)

@given(instance=uml3::0::0::CallAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::callaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CallAction)

@given(instance=uml3::0::0::CallAction_strategy)
def test_uml3::0::0::callaction_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, str)


@given(instance=uml3::0::0::CallAction_strategy)
def test_uml3::0::0::callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=uml3::0::0::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::centralbuffernode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CentralBufferNode)

@given(instance=uml3::0::0::ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::expansionnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExpansionNode)

@given(instance=uml3::0::0::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::activityparameternode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActivityParameterNode)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=uml3::0::0::InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InterruptibleActivityRegion)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=uml3::0::0::ControlNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::controlnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ControlNode)

@given(instance=uml3::0::0::ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::executablenode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExecutableNode)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=uml3::0::0::Action_strategy)
@settings(max_examples=50)
def test_uml3::0::0::action_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Action)

@given(instance=uml3::0::0::OutputPin_strategy)
@settings(max_examples=50)
def test_uml3::0::0::outputpin_instantiation(instance):
    assert isinstance(instance, uml3::0::0::OutputPin)

@given(instance=uml3::0::0::InputPin_strategy)
@settings(max_examples=50)
def test_uml3::0::0::inputpin_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=uml3::0::0::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readselfaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadSelfAction)

@given(instance=uml3::0::0::VariableAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::variableaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::VariableAction)

@given(instance=uml3::0::0::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::clearassociationaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ClearAssociationAction)

@given(instance=uml3::0::0::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ValueSpecificationAction)

@given(instance=uml3::0::0::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::testidentityaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TestIdentityAction)

@given(instance=uml3::0::0::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StructuralFeatureAction)

@given(instance=uml3::0::0::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DestroyObjectAction)

@given(instance=uml3::0::0::DestroyObjectAction_strategy)
def test_uml3::0::0::destroyobjectaction_isDestroyOwnedObjects_type(instance):
    assert isinstance(instance.isDestroyOwnedObjects, str)


@given(instance=uml3::0::0::DestroyObjectAction_strategy)
def test_uml3::0::0::destroyobjectaction_isDestroyOwnedObjects_setter(instance):
    original = instance.isDestroyOwnedObjects
    instance.isDestroyOwnedObjects = original
    assert instance.isDestroyOwnedObjects == original

@given(instance=uml3::0::0::DestroyObjectAction_strategy)
def test_uml3::0::0::destroyobjectaction_isDestroyLinks_type(instance):
    assert isinstance(instance.isDestroyLinks, str)


@given(instance=uml3::0::0::DestroyObjectAction_strategy)
def test_uml3::0::0::destroyobjectaction_isDestroyLinks_setter(instance):
    original = instance.isDestroyLinks
    instance.isDestroyLinks = original
    assert instance.isDestroyLinks == original

@given(instance=uml3::0::0::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::createobjectaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CreateObjectAction)

@given(instance=uml3::0::0::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::RaiseExceptionAction)

@given(instance=uml3::0::0::InvocationAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::invocationaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InvocationAction)

@given(instance=uml3::0::0::LinkAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::linkaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LinkAction)

@given(instance=uml3::0::0::OpaqueAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::opaqueaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::OpaqueAction)

@given(instance=uml3::0::0::OpaqueAction_strategy)
def test_uml3::0::0::opaqueaction_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml3::0::0::OpaqueAction_strategy)
def test_uml3::0::0::opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml3::0::0::OpaqueAction_strategy)
def test_uml3::0::0::opaqueaction_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=uml3::0::0::OpaqueAction_strategy)
def test_uml3::0::0::opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=uml3::0::0::FunctionBehavior_strategy)
@settings(max_examples=50)
def test_uml3::0::0::functionbehavior_instantiation(instance):
    assert isinstance(instance, uml3::0::0::FunctionBehavior)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=uml3::0::0::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml3::0::0::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LiteralUnlimitedNatural)

@given(instance=uml3::0::0::LiteralUnlimitedNatural_strategy)
def test_uml3::0::0::literalunlimitednatural_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml3::0::0::LiteralUnlimitedNatural_strategy)
def test_uml3::0::0::literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml3::0::0::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml3::0::0::literalboolean_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LiteralBoolean)

@given(instance=uml3::0::0::LiteralBoolean_strategy)
def test_uml3::0::0::literalboolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml3::0::0::LiteralBoolean_strategy)
def test_uml3::0::0::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml3::0::0::LiteralString_strategy)
@settings(max_examples=50)
def test_uml3::0::0::literalstring_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LiteralString)

@given(instance=uml3::0::0::LiteralString_strategy)
def test_uml3::0::0::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml3::0::0::LiteralString_strategy)
def test_uml3::0::0::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml3::0::0::LiteralNull_strategy)
@settings(max_examples=50)
def test_uml3::0::0::literalnull_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LiteralNull)

@given(instance=uml3::0::0::LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml3::0::0::literalinteger_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LiteralInteger)

@given(instance=uml3::0::0::LiteralInteger_strategy)
def test_uml3::0::0::literalinteger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml3::0::0::LiteralInteger_strategy)
def test_uml3::0::0::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=uml3::0::0::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml3::0::0::enumerationliteral_instantiation(instance):
    assert isinstance(instance, uml3::0::0::EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=uml3::0::0::PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml3::0::0::primitivetype_instantiation(instance):
    assert isinstance(instance, uml3::0::0::PrimitiveType)

@given(instance=uml3::0::0::Enumeration_strategy)
@settings(max_examples=50)
def test_uml3::0::0::enumeration_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Enumeration)

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

@given(instance=uml3::0::0::ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3::0::0::connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ConnectableElementTemplateParameter)

@given(instance=uml3::0::0::ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3::0::0::classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ClassifierTemplateParameter)

@given(instance=uml3::0::0::ClassifierTemplateParameter_strategy)
def test_uml3::0::0::classifiertemplateparameter_allowSubstitutable_type(instance):
    assert isinstance(instance.allowSubstitutable, str)


@given(instance=uml3::0::0::ClassifierTemplateParameter_strategy)
def test_uml3::0::0::classifiertemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=uml3::0::0::OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3::0::0::operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml3::0::0::OperationTemplateParameter)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=uml3::0::0::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml3::0::0::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, uml3::0::0::EncapsulatedClassifier)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=uml3::0::0::Model_strategy)
@settings(max_examples=50)
def test_uml3::0::0::model_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Model)

@given(instance=uml3::0::0::Model_strategy)
def test_uml3::0::0::model_viewpoint_type(instance):
    assert isinstance(instance.viewpoint, str)


@given(instance=uml3::0::0::Model_strategy)
def test_uml3::0::0::model_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original

@given(instance=uml3::0::0::Profile_strategy)
@settings(max_examples=50)
def test_uml3::0::0::profile_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Profile)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=uml3::0::0::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml3::0::0::communicationpath_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CommunicationPath)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=uml3::0::0::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml3::0::0::connectionpointreference_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ConnectionPointReference)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=uml3::0::0::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml3::0::0::extensionend_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExtensionEnd)

@given(instance=uml3::0::0::Port_strategy)
@settings(max_examples=50)
def test_uml3::0::0::port_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Port)

@given(instance=uml3::0::0::Port_strategy)
def test_uml3::0::0::port_isBehavior_type(instance):
    assert isinstance(instance.isBehavior, str)


@given(instance=uml3::0::0::Port_strategy)
def test_uml3::0::0::port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original

@given(instance=uml3::0::0::Port_strategy)
def test_uml3::0::0::port_isService_type(instance):
    assert isinstance(instance.isService, str)


@given(instance=uml3::0::0::Port_strategy)
def test_uml3::0::0::port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original

@given(instance=uml3::0::0::Pseudostate_strategy)
@settings(max_examples=50)
def test_uml3::0::0::pseudostate_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Pseudostate)

@given(instance=uml3::0::0::Pseudostate_strategy)
def test_uml3::0::0::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml3::0::0::Pseudostate_strategy)
def test_uml3::0::0::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=uml3::0::0::Interaction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Interaction)

@given(instance=uml3::0::0::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_uml3::0::0::opaquebehavior_instantiation(instance):
    assert isinstance(instance, uml3::0::0::OpaqueBehavior)

@given(instance=uml3::0::0::OpaqueBehavior_strategy)
def test_uml3::0::0::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml3::0::0::OpaqueBehavior_strategy)
def test_uml3::0::0::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml3::0::0::OpaqueBehavior_strategy)
def test_uml3::0::0::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=uml3::0::0::OpaqueBehavior_strategy)
def test_uml3::0::0::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=uml3::0::0::Activity_strategy)
@settings(max_examples=50)
def test_uml3::0::0::activity_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Activity)

@given(instance=uml3::0::0::Activity_strategy)
def test_uml3::0::0::activity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=uml3::0::0::Activity_strategy)
def test_uml3::0::0::activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=uml3::0::0::Activity_strategy)
def test_uml3::0::0::activity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, str)


@given(instance=uml3::0::0::Activity_strategy)
def test_uml3::0::0::activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=uml3::0::0::StateMachine_strategy)
@settings(max_examples=50)
def test_uml3::0::0::statemachine_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StateMachine)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=uml3::0::0::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml3::0::0::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ProtocolStateMachine)

@given(instance=uml3::0::0::Extension_strategy)
@settings(max_examples=50)
def test_uml3::0::0::extension_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Extension)

@given(instance=uml3::0::0::Extension_strategy)
def test_uml3::0::0::extension_isRequired_type(instance):
    assert isinstance(instance.isRequired, str)


@given(instance=uml3::0::0::Extension_strategy)
def test_uml3::0::0::extension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=uml3::0::0::Actor_strategy)
@settings(max_examples=50)
def test_uml3::0::0::actor_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Actor)

@given(instance=uml3::0::0::Collaboration_strategy)
@settings(max_examples=50)
def test_uml3::0::0::collaboration_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Collaboration)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=uml3::0::0::Component_strategy)
@settings(max_examples=50)
def test_uml3::0::0::component_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Component)

@given(instance=uml3::0::0::Component_strategy)
def test_uml3::0::0::component_isIndirectlyInstantiated_type(instance):
    assert isinstance(instance.isIndirectlyInstantiated, str)


@given(instance=uml3::0::0::Component_strategy)
def test_uml3::0::0::component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original

@given(instance=uml3::0::0::Stereotype_strategy)
@settings(max_examples=50)
def test_uml3::0::0::stereotype_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Stereotype)

@given(instance=uml3::0::0::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml3::0::0::associationclass_instantiation(instance):
    assert isinstance(instance, uml3::0::0::AssociationClass)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=uml3::0::0::Connector_strategy)
@settings(max_examples=50)
def test_uml3::0::0::connector_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Connector)

@given(instance=uml3::0::0::Connector_strategy)
def test_uml3::0::0::connector_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml3::0::0::Connector_strategy)
def test_uml3::0::0::connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=uml3::0::0::Reception_strategy)
@settings(max_examples=50)
def test_uml3::0::0::reception_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Reception)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=uml3::0::0::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::deploymentspecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DeploymentSpecification)

@given(instance=uml3::0::0::DeploymentSpecification_strategy)
def test_uml3::0::0::deploymentspecification_deploymentLocation_type(instance):
    assert isinstance(instance.deploymentLocation, str)


@given(instance=uml3::0::0::DeploymentSpecification_strategy)
def test_uml3::0::0::deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=uml3::0::0::DeploymentSpecification_strategy)
def test_uml3::0::0::deploymentspecification_executionLocation_type(instance):
    assert isinstance(instance.executionLocation, str)


@given(instance=uml3::0::0::DeploymentSpecification_strategy)
def test_uml3::0::0::deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original

@given(instance=uml3::0::0::Class_strategy)
@settings(max_examples=50)
def test_uml3::0::0::class_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Class)

@given(instance=uml3::0::0::Class_strategy)
def test_uml3::0::0::class_isActive_type(instance):
    assert isinstance(instance.isActive, str)


@given(instance=uml3::0::0::Class_strategy)
def test_uml3::0::0::class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=uml3::0::0::Node_strategy)
@settings(max_examples=50)
def test_uml3::0::0::node_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Node)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=uml3::0::0::TimeExpression_strategy)
@settings(max_examples=50)
def test_uml3::0::0::timeexpression_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TimeExpression)

@given(instance=uml3::0::0::InstanceValue_strategy)
@settings(max_examples=50)
def test_uml3::0::0::instancevalue_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InstanceValue)

@given(instance=uml3::0::0::Duration_strategy)
@settings(max_examples=50)
def test_uml3::0::0::duration_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Duration)

@given(instance=uml3::0::0::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::literalspecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LiteralSpecification)

@given(instance=uml3::0::0::Expression_strategy)
@settings(max_examples=50)
def test_uml3::0::0::expression_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Expression)

@given(instance=uml3::0::0::Expression_strategy)
def test_uml3::0::0::expression_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=uml3::0::0::Expression_strategy)
def test_uml3::0::0::expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=uml3::0::0::Interval_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interval_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Interval)

@given(instance=uml3::0::0::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml3::0::0::opaqueexpression_instantiation(instance):
    assert isinstance(instance, uml3::0::0::OpaqueExpression)

@given(instance=uml3::0::0::OpaqueExpression_strategy)
def test_uml3::0::0::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml3::0::0::OpaqueExpression_strategy)
def test_uml3::0::0::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml3::0::0::OpaqueExpression_strategy)
def test_uml3::0::0::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=uml3::0::0::OpaqueExpression_strategy)
def test_uml3::0::0::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=uml3::0::0::Usage_strategy)
@settings(max_examples=50)
def test_uml3::0::0::usage_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Usage)

@given(instance=uml3::0::0::Deployment_strategy)
@settings(max_examples=50)
def test_uml3::0::0::deployment_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Deployment)

@given(instance=uml3::0::0::Abstraction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::abstraction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Abstraction)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=uml3::0::0::Manifestation_strategy)
@settings(max_examples=50)
def test_uml3::0::0::manifestation_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Manifestation)

@given(instance=uml3::0::0::Realization_strategy)
@settings(max_examples=50)
def test_uml3::0::0::realization_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Realization)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=uml3::0::0::Pin_strategy)
@settings(max_examples=50)
def test_uml3::0::0::pin_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Pin)

@given(instance=uml3::0::0::Pin_strategy)
def test_uml3::0::0::pin_isControl_type(instance):
    assert isinstance(instance.isControl, str)


@given(instance=uml3::0::0::Pin_strategy)
def test_uml3::0::0::pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=uml3::0::0::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml3::0::0::connectorend_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ConnectorEnd)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=uml3::0::0::Variable_strategy)
@settings(max_examples=50)
def test_uml3::0::0::variable_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Variable)

@given(instance=uml3::0::0::ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::conditionalnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ConditionalNode)

@given(instance=uml3::0::0::ConditionalNode_strategy)
def test_uml3::0::0::conditionalnode_isDeterminate_type(instance):
    assert isinstance(instance.isDeterminate, str)


@given(instance=uml3::0::0::ConditionalNode_strategy)
def test_uml3::0::0::conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original

@given(instance=uml3::0::0::ConditionalNode_strategy)
def test_uml3::0::0::conditionalnode_isAssured_type(instance):
    assert isinstance(instance.isAssured, str)


@given(instance=uml3::0::0::ConditionalNode_strategy)
def test_uml3::0::0::conditionalnode_isAssured_setter(instance):
    original = instance.isAssured
    instance.isAssured = original
    assert instance.isAssured == original

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=uml3::0::0::DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::datastorenode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DataStoreNode)

@given(instance=uml3::0::0::JoinNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::joinnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::JoinNode)

@given(instance=uml3::0::0::JoinNode_strategy)
def test_uml3::0::0::joinnode_isCombineDuplicate_type(instance):
    assert isinstance(instance.isCombineDuplicate, str)


@given(instance=uml3::0::0::JoinNode_strategy)
def test_uml3::0::0::joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=uml3::0::0::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StartObjectBehaviorAction)

@given(instance=uml3::0::0::ReduceAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::reduceaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReduceAction)

@given(instance=uml3::0::0::ReduceAction_strategy)
def test_uml3::0::0::reduceaction_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=uml3::0::0::ReduceAction_strategy)
def test_uml3::0::0::reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml3::0::0::UnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::unmarshallaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::UnmarshallAction)

@given(instance=uml3::0::0::ReplyAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::replyaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReplyAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=uml3::0::0::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::acceptcallaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::AcceptCallAction)

@given(instance=uml3::0::0::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadLinkObjectEndAction)

@given(instance=uml3::0::0::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::accepteventaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::AcceptEventAction)

@given(instance=uml3::0::0::AcceptEventAction_strategy)
def test_uml3::0::0::accepteventaction_isUnmarshall_type(instance):
    assert isinstance(instance.isUnmarshall, str)


@given(instance=uml3::0::0::AcceptEventAction_strategy)
def test_uml3::0::0::accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=uml3::0::0::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CreateLinkObjectAction)

@given(instance=uml3::0::0::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadLinkObjectEndQualifierAction)

@given(instance=uml3::0::0::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StartClassifierBehaviorAction)

@given(instance=uml3::0::0::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadIsClassifiedObjectAction)

@given(instance=uml3::0::0::ReadIsClassifiedObjectAction_strategy)
def test_uml3::0::0::readisclassifiedobjectaction_isDirect_type(instance):
    assert isinstance(instance.isDirect, str)


@given(instance=uml3::0::0::ReadIsClassifiedObjectAction_strategy)
def test_uml3::0::0::readisclassifiedobjectaction_isDirect_setter(instance):
    original = instance.isDirect
    instance.isDirect = original
    assert instance.isDirect == original

@given(instance=uml3::0::0::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReclassifyObjectAction)

@given(instance=uml3::0::0::ReclassifyObjectAction_strategy)
def test_uml3::0::0::reclassifyobjectaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml3::0::0::ReclassifyObjectAction_strategy)
def test_uml3::0::0::reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml3::0::0::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::readextentaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ReadExtentAction)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=uml3::0::0::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::RemoveVariableValueAction)

@given(instance=uml3::0::0::RemoveVariableValueAction_strategy)
def test_uml3::0::0::removevariablevalueaction_isRemoveDuplicates_type(instance):
    assert isinstance(instance.isRemoveDuplicates, str)


@given(instance=uml3::0::0::RemoveVariableValueAction_strategy)
def test_uml3::0::0::removevariablevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=uml3::0::0::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml3::0::0::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml3::0::0::AddVariableValueAction)

@given(instance=uml3::0::0::AddVariableValueAction_strategy)
def test_uml3::0::0::addvariablevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml3::0::0::AddVariableValueAction_strategy)
def test_uml3::0::0::addvariablevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=uml3::0::0::ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml3::0::0::protocolconformance_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ProtocolConformance)

@given(instance=uml3::0::0::PackageImport_strategy)
@settings(max_examples=50)
def test_uml3::0::0::packageimport_instantiation(instance):
    assert isinstance(instance, uml3::0::0::PackageImport)

@given(instance=uml3::0::0::PackageImport_strategy)
def test_uml3::0::0::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml3::0::0::PackageImport_strategy)
def test_uml3::0::0::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml3::0::0::ElementImport_strategy)
@settings(max_examples=50)
def test_uml3::0::0::elementimport_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ElementImport)

@given(instance=uml3::0::0::ElementImport_strategy)
def test_uml3::0::0::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml3::0::0::ElementImport_strategy)
def test_uml3::0::0::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml3::0::0::ElementImport_strategy)
def test_uml3::0::0::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=uml3::0::0::ElementImport_strategy)
def test_uml3::0::0::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=uml3::0::0::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml3::0::0::directedrelationship_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DirectedRelationship)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml3::0::0::MessageEnd_strategy)
@settings(max_examples=50)
def test_uml3::0::0::messageend_instantiation(instance):
    assert isinstance(instance, uml3::0::0::MessageEnd)

@given(instance=uml3::0::0::Namespace_strategy)
@settings(max_examples=50)
def test_uml3::0::0::namespace_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Namespace)

@given(instance=uml3::0::0::DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml3::0::0::deploymenttarget_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DeploymentTarget)

@given(instance=uml3::0::0::ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml3::0::0::activitypartition_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActivityPartition)

@given(instance=uml3::0::0::ActivityPartition_strategy)
def test_uml3::0::0::activitypartition_isDimension_type(instance):
    assert isinstance(instance.isDimension, str)


@given(instance=uml3::0::0::ActivityPartition_strategy)
def test_uml3::0::0::activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=uml3::0::0::ActivityPartition_strategy)
def test_uml3::0::0::activitypartition_isExternal_type(instance):
    assert isinstance(instance.isExternal, str)


@given(instance=uml3::0::0::ActivityPartition_strategy)
def test_uml3::0::0::activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=uml3::0::0::Lifeline_strategy)
@settings(max_examples=50)
def test_uml3::0::0::lifeline_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Lifeline)

@given(instance=uml3::0::0::Include_strategy)
@settings(max_examples=50)
def test_uml3::0::0::include_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Include)

@given(instance=uml3::0::0::Message_strategy)
@settings(max_examples=50)
def test_uml3::0::0::message_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Message)

@given(instance=uml3::0::0::Message_strategy)
def test_uml3::0::0::message_messageSort_type(instance):
    assert isinstance(instance.messageSort, str)


@given(instance=uml3::0::0::Message_strategy)
def test_uml3::0::0::message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original

@given(instance=uml3::0::0::Message_strategy)
def test_uml3::0::0::message_messageKind_type(instance):
    assert isinstance(instance.messageKind, str)


@given(instance=uml3::0::0::Message_strategy)
def test_uml3::0::0::message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original

@given(instance=uml3::0::0::InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interactionfragment_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InteractionFragment)

@given(instance=uml3::0::0::ParameterSet_strategy)
@settings(max_examples=50)
def test_uml3::0::0::parameterset_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ParameterSet)

@given(instance=uml3::0::0::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml3::0::0::generalordering_instantiation(instance):
    assert isinstance(instance, uml3::0::0::GeneralOrdering)

@given(instance=uml3::0::0::DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml3::0::0::deployedartifact_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DeployedArtifact)

@given(instance=uml3::0::0::Vertex_strategy)
@settings(max_examples=50)
def test_uml3::0::0::vertex_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Vertex)

@given(instance=uml3::0::0::Trigger_strategy)
@settings(max_examples=50)
def test_uml3::0::0::trigger_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Trigger)

@given(instance=uml3::0::0::Extend_strategy)
@settings(max_examples=50)
def test_uml3::0::0::extend_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Extend)

@given(instance=uml3::0::0::ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml3::0::0::profileapplication_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ProfileApplication)

@given(instance=uml3::0::0::ProfileApplication_strategy)
def test_uml3::0::0::profileapplication_isStrict_type(instance):
    assert isinstance(instance.isStrict, str)


@given(instance=uml3::0::0::ProfileApplication_strategy)
def test_uml3::0::0::profileapplication_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=uml3::0::0::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::packageableelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::PackageableElement)

@given(instance=uml3::0::0::PackageMerge_strategy)
@settings(max_examples=50)
def test_uml3::0::0::packagemerge_instantiation(instance):
    assert isinstance(instance, uml3::0::0::PackageMerge)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=uml3::0::0::StringExpression_strategy)
@settings(max_examples=50)
def test_uml3::0::0::stringexpression_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StringExpression)

@given(instance=uml3::0::0::Operation_strategy)
@settings(max_examples=50)
def test_uml3::0::0::operation_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Operation)

@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, str)


@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=uml3::0::0::Operation_strategy)
def test_uml3::0::0::operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uml3::0::0::InformationFlow_strategy)
@settings(max_examples=50)
def test_uml3::0::0::informationflow_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InformationFlow)

@given(instance=uml3::0::0::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::instancespecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InstanceSpecification)

@given(instance=uml3::0::0::Constraint_strategy)
@settings(max_examples=50)
def test_uml3::0::0::constraint_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Constraint)

@given(instance=uml3::0::0::Observation_strategy)
@settings(max_examples=50)
def test_uml3::0::0::observation_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Observation)

@given(instance=uml3::0::0::Event_strategy)
@settings(max_examples=50)
def test_uml3::0::0::event_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Event)

@given(instance=uml3::0::0::Type_strategy)
@settings(max_examples=50)
def test_uml3::0::0::type_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Type)

@given(instance=uml3::0::0::Dependency_strategy)
@settings(max_examples=50)
def test_uml3::0::0::dependency_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Dependency)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=uml3::0::0::InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interactionoperand_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InteractionOperand)

@given(instance=uml3::0::0::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml3::0::0::behavioralfeature_instantiation(instance):
    assert isinstance(instance, uml3::0::0::BehavioralFeature)

@given(instance=uml3::0::0::BehavioralFeature_strategy)
def test_uml3::0::0::behavioralfeature_concurrency_type(instance):
    assert isinstance(instance.concurrency, str)


@given(instance=uml3::0::0::BehavioralFeature_strategy)
def test_uml3::0::0::behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=uml3::0::0::BehavioralFeature_strategy)
def test_uml3::0::0::behavioralfeature_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uml3::0::0::BehavioralFeature_strategy)
def test_uml3::0::0::behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml3::0::0::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StructuredActivityNode)

@given(instance=uml3::0::0::StructuredActivityNode_strategy)
def test_uml3::0::0::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, str)


@given(instance=uml3::0::0::StructuredActivityNode_strategy)
def test_uml3::0::0::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=uml3::0::0::Package_strategy)
@settings(max_examples=50)
def test_uml3::0::0::package_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Package)

@given(instance=uml3::0::0::Element_strategy)
@settings(max_examples=50)
def test_uml3::0::0::element_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Element)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uml3::0::0::Relationship_strategy)
@settings(max_examples=50)
def test_uml3::0::0::relationship_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Relationship)

@given(instance=uml3::0::0::ActivityGroup_strategy)
@settings(max_examples=50)
def test_uml3::0::0::activitygroup_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActivityGroup)

@given(instance=uml3::0::0::Image_strategy)
@settings(max_examples=50)
def test_uml3::0::0::image_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Image)

@given(instance=uml3::0::0::Image_strategy)
def test_uml3::0::0::image_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=uml3::0::0::Image_strategy)
def test_uml3::0::0::image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=uml3::0::0::Image_strategy)
def test_uml3::0::0::image_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=uml3::0::0::Image_strategy)
def test_uml3::0::0::image_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=uml3::0::0::Image_strategy)
def test_uml3::0::0::image_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=uml3::0::0::Image_strategy)
def test_uml3::0::0::image_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=uml3::0::0::LinkEndData_strategy)
@settings(max_examples=50)
def test_uml3::0::0::linkenddata_instantiation(instance):
    assert isinstance(instance, uml3::0::0::LinkEndData)

@given(instance=uml3::0::0::NamedElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::namedelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::NamedElement)

@given(instance=uml3::0::0::NamedElement_strategy)
def test_uml3::0::0::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml3::0::0::NamedElement_strategy)
def test_uml3::0::0::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml3::0::0::NamedElement_strategy)
def test_uml3::0::0::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=uml3::0::0::NamedElement_strategy)
def test_uml3::0::0::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=uml3::0::0::NamedElement_strategy)
def test_uml3::0::0::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml3::0::0::NamedElement_strategy)
def test_uml3::0::0::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml3::0::0::Slot_strategy)
@settings(max_examples=50)
def test_uml3::0::0::slot_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Slot)

@given(instance=uml3::0::0::Clause_strategy)
@settings(max_examples=50)
def test_uml3::0::0::clause_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Clause)

@given(instance=uml3::0::0::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml3::0::0::exceptionhandler_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExceptionHandler)

@given(instance=uml3::0::0::QualifierValue_strategy)
@settings(max_examples=50)
def test_uml3::0::0::qualifiervalue_instantiation(instance):
    assert isinstance(instance, uml3::0::0::QualifierValue)

@given(instance=uml3::0::0::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::multiplicityelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::MultiplicityElement)

@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=uml3::0::0::MultiplicityElement_strategy)
def test_uml3::0::0::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=uml3::0::0::Comment_strategy)
@settings(max_examples=50)
def test_uml3::0::0::comment_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Comment)

@given(instance=uml3::0::0::Comment_strategy)
def test_uml3::0::0::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml3::0::0::Comment_strategy)
def test_uml3::0::0::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml3::0::0::Behavior_strategy)
@settings(max_examples=50)
def test_uml3::0::0::behavior_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Behavior)

@given(instance=uml3::0::0::Behavior_strategy)
def test_uml3::0::0::behavior_isReentrant_type(instance):
    assert isinstance(instance.isReentrant, str)


@given(instance=uml3::0::0::Behavior_strategy)
def test_uml3::0::0::behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=uml3::0::0::Parameter_strategy)
@settings(max_examples=50)
def test_uml3::0::0::parameter_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Parameter)

@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_isException_type(instance):
    assert isinstance(instance.isException, str)


@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original

@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_isStream_type(instance):
    assert isinstance(instance.isStream, str)


@given(instance=uml3::0::0::Parameter_strategy)
def test_uml3::0::0::parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=uml3::0::0::ComponentRealization_strategy)
@settings(max_examples=50)
def test_uml3::0::0::componentrealization_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ComponentRealization)

@given(instance=uml3::0::0::InterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interfacerealization_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InterfaceRealization)

@given(instance=uml3::0::0::RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::redefinableelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::RedefinableElement)

@given(instance=uml3::0::0::RedefinableElement_strategy)
def test_uml3::0::0::redefinableelement_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, str)


@given(instance=uml3::0::0::RedefinableElement_strategy)
def test_uml3::0::0::redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=uml3::0::0::ParameterableElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::parameterableelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ParameterableElement)

@given(instance=uml3::0::0::TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml3::0::0::templateparameter_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TemplateParameter)

@given(instance=uml3::0::0::TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml3::0::0::templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TemplateParameterSubstitution)

@given(instance=uml3::0::0::TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml3::0::0::templatesignature_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TemplateSignature)

@given(instance=uml3::0::0::TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml3::0::0::templatebinding_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TemplateBinding)

@given(instance=uml3::0::0::TemplateableElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::templateableelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TemplateableElement)

@given(instance=uml3::0::0::Property_strategy)
@settings(max_examples=50)
def test_uml3::0::0::property_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Property)

@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_isDerivedUnion_type(instance):
    assert isinstance(instance.isDerivedUnion, str)


@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original

@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=uml3::0::0::Property_strategy)
def test_uml3::0::0::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml3::0::0::InformationItem_strategy)
@settings(max_examples=50)
def test_uml3::0::0::informationitem_instantiation(instance):
    assert isinstance(instance, uml3::0::0::InformationItem)

@given(instance=uml3::0::0::Signal_strategy)
@settings(max_examples=50)
def test_uml3::0::0::signal_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Signal)

@given(instance=uml3::0::0::DataType_strategy)
@settings(max_examples=50)
def test_uml3::0::0::datatype_instantiation(instance):
    assert isinstance(instance, uml3::0::0::DataType)

@given(instance=uml3::0::0::Artifact_strategy)
@settings(max_examples=50)
def test_uml3::0::0::artifact_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Artifact)

@given(instance=uml3::0::0::Artifact_strategy)
def test_uml3::0::0::artifact_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=uml3::0::0::Artifact_strategy)
def test_uml3::0::0::artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=uml3::0::0::Interface_strategy)
@settings(max_examples=50)
def test_uml3::0::0::interface_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Interface)

@given(instance=uml3::0::0::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml3::0::0::structuredclassifier_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StructuredClassifier)

@given(instance=uml3::0::0::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml3::0::0::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml3::0::0::BehavioredClassifier)

@given(instance=uml3::0::0::Association_strategy)
@settings(max_examples=50)
def test_uml3::0::0::association_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Association)

@given(instance=uml3::0::0::Association_strategy)
def test_uml3::0::0::association_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=uml3::0::0::Association_strategy)
def test_uml3::0::0::association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml3::0::0::UseCase_strategy)
@settings(max_examples=50)
def test_uml3::0::0::usecase_instantiation(instance):
    assert isinstance(instance, uml3::0::0::UseCase)

@given(instance=uml3::0::0::CollaborationUse_strategy)
@settings(max_examples=50)
def test_uml3::0::0::collaborationuse_instantiation(instance):
    assert isinstance(instance, uml3::0::0::CollaborationUse)

@given(instance=uml3::0::0::Substitution_strategy)
@settings(max_examples=50)
def test_uml3::0::0::substitution_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Substitution)

@given(instance=uml3::0::0::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml3::0::0::generalizationset_instantiation(instance):
    assert isinstance(instance, uml3::0::0::GeneralizationSet)

@given(instance=uml3::0::0::GeneralizationSet_strategy)
def test_uml3::0::0::generalizationset_isDisjoint_type(instance):
    assert isinstance(instance.isDisjoint, str)


@given(instance=uml3::0::0::GeneralizationSet_strategy)
def test_uml3::0::0::generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=uml3::0::0::GeneralizationSet_strategy)
def test_uml3::0::0::generalizationset_isCovering_type(instance):
    assert isinstance(instance.isCovering, str)


@given(instance=uml3::0::0::GeneralizationSet_strategy)
def test_uml3::0::0::generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=uml3::0::0::Generalization_strategy)
@settings(max_examples=50)
def test_uml3::0::0::generalization_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Generalization)

@given(instance=uml3::0::0::Generalization_strategy)
def test_uml3::0::0::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, str)


@given(instance=uml3::0::0::Generalization_strategy)
def test_uml3::0::0::generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=uml3::0::0::ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml3::0::0::activityedge_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActivityEdge)

@given(instance=uml3::0::0::Region_strategy)
@settings(max_examples=50)
def test_uml3::0::0::region_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Region)

@given(instance=uml3::0::0::ActivityNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::activitynode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ActivityNode)

@given(instance=uml3::0::0::RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml3::0::0::redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, uml3::0::0::RedefinableTemplateSignature)

@given(instance=uml3::0::0::State_strategy)
@settings(max_examples=50)
def test_uml3::0::0::state_instantiation(instance):
    assert isinstance(instance, uml3::0::0::State)

@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, str)


@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, str)


@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, str)


@given(instance=uml3::0::0::State_strategy)
def test_uml3::0::0::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=uml3::0::0::Transition_strategy)
@settings(max_examples=50)
def test_uml3::0::0::transition_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Transition)

@given(instance=uml3::0::0::Transition_strategy)
def test_uml3::0::0::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml3::0::0::Transition_strategy)
def test_uml3::0::0::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uml3::0::0::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml3::0::0::extensionpoint_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ExtensionPoint)

@given(instance=uml3::0::0::Feature_strategy)
@settings(max_examples=50)
def test_uml3::0::0::feature_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Feature)

@given(instance=uml3::0::0::Feature_strategy)
def test_uml3::0::0::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=uml3::0::0::Feature_strategy)
def test_uml3::0::0::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=uml3::0::0::Classifier_strategy)
@settings(max_examples=50)
def test_uml3::0::0::classifier_instantiation(instance):
    assert isinstance(instance, uml3::0::0::Classifier)

@given(instance=uml3::0::0::Classifier_strategy)
def test_uml3::0::0::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uml3::0::0::Classifier_strategy)
def test_uml3::0::0::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml3::0::0::TypedElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::typedelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::TypedElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=uml3::0::0::ObjectNode_strategy)
@settings(max_examples=50)
def test_uml3::0::0::objectnode_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ObjectNode)

@given(instance=uml3::0::0::ObjectNode_strategy)
def test_uml3::0::0::objectnode_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=uml3::0::0::ObjectNode_strategy)
def test_uml3::0::0::objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=uml3::0::0::ObjectNode_strategy)
def test_uml3::0::0::objectnode_isControlType_type(instance):
    assert isinstance(instance.isControlType, str)


@given(instance=uml3::0::0::ObjectNode_strategy)
def test_uml3::0::0::objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=uml3::0::0::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml3::0::0::structuralfeature_instantiation(instance):
    assert isinstance(instance, uml3::0::0::StructuralFeature)

@given(instance=uml3::0::0::StructuralFeature_strategy)
def test_uml3::0::0::structuralfeature_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=uml3::0::0::StructuralFeature_strategy)
def test_uml3::0::0::structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=uml3::0::0::ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml3::0::0::connectableelement_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ConnectableElement)

@given(instance=uml3::0::0::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml3::0::0::valuespecification_instantiation(instance):
    assert isinstance(instance, uml3::0::0::ValueSpecification)

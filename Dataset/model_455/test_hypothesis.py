import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    uml::FinalState,
    Observation,
    uml::DurationObservation,
    uml::TimeObservation,
    IntervalConstraint,
    uml::DurationConstraint,
    uml::TimeConstraint,
    Interval,
    uml::TimeInterval,
    uml::DurationInterval,
    WriteLinkAction,
    uml::DestroyLinkAction,
    uml::CreateLinkAction,
    LinkEndData,
    uml::LinkEndDestructionData,
    uml::LinkEndCreationData,
    LinkAction,
    uml::WriteLinkAction,
    uml::ReadLinkAction,
    StructuralFeatureAction,
    uml::WriteStructuralFeatureAction,
    uml::ClearStructuralFeatureAction,
    uml::ReadStructuralFeatureAction,
    WriteStructuralFeatureAction,
    uml::AddStructuralFeatureValueAction,
    uml::RemoveStructuralFeatureValueAction,
    Node,
    uml::ExecutionEnvironment,
    uml::Device,
    CombinedFragment,
    uml::ConsiderIgnoreFragment,
    FinalNode,
    uml::ActivityFinalNode,
    uml::FlowFinalNode,
    MessageEvent,
    uml::CallEvent,
    uml::ReceiveSignalEvent,
    uml::SignalEvent,
    uml::ReceiveOperationEvent,
    uml::AnyReceiveEvent,
    uml::SendSignalEvent,
    uml::SendOperationEvent,
    Event,
    uml::ChangeEvent,
    uml::DestructionEvent,
    uml::MessageEvent,
    uml::TimeEvent,
    uml::CreationEvent,
    uml::ExecutionEvent,
    ExecutionSpecification,
    uml::BehaviorExecutionSpecification,
    uml::ActionExecutionSpecification,
    Constraint,
    uml::IntervalConstraint,
    uml::InteractionConstraint,
    OccurrenceSpecification,
    uml::ExecutionOccurrenceSpecification,
    MessageEnd,
    uml::MessageOccurrenceSpecification,
    InteractionUse,
    uml::PartDecomposition,
    InteractionFragment,
    uml::StateInvariant,
    uml::OccurrenceSpecification,
    uml::Continuation,
    uml::ExecutionSpecification,
    uml::InteractionUse,
    uml::CombinedFragment,
    InputPin,
    uml::ValuePin,
    uml::Gate,
    StructuredActivityNode,
    uml::SequenceNode,
    CallAction,
    uml::CallBehaviorAction,
    uml::CallOperationAction,
    InvocationAction,
    uml::BroadcastSignalAction,
    uml::SendSignalAction,
    uml::SendObjectAction,
    uml::CallAction,
    ObjectNode,
    uml::CentralBufferNode,
    Pin,
    uml::ActivityParameterNode,
    ControlNode,
    uml::MergeNode,
    uml::FinalNode,
    uml::DecisionNode,
    uml::ForkNode,
    uml::InitialNode,
    ActivityEdge,
    uml::ObjectFlow,
    uml::ControlFlow,
    ActivityGroup,
    uml::InterruptibleActivityRegion,
    ActivityNode,
    uml::ControlNode,
    uml::ExecutableNode,
    ExecutableNode,
    uml::Action,
    uml::OutputPin,
    uml::InputPin,
    Action,
    uml::InvocationAction,
    uml::ValueSpecificationAction,
    uml::ReadSelfAction,
    uml::StructuralFeatureAction,
    uml::DestroyObjectAction,
    uml::CreateObjectAction,
    uml::LinkAction,
    uml::TestIdentityAction,
    uml::ClearAssociationAction,
    uml::OpaqueAction,
    OpaqueBehavior,
    uml::FunctionBehavior,
    InstanceSpecification,
    LiteralSpecification,
    uml::LiteralUnlimitedNatural,
    uml::LiteralNull,
    uml::LiteralString,
    uml::LiteralBoolean,
    uml::LiteralInteger,
    uml::EnumerationLiteral,
    DataType,
    uml::PrimitiveType,
    uml::Enumeration,
    TemplateSignature,
    Expression,
    TemplateParameter,
    uml::ClassifierTemplateParameter,
    uml::ConnectableElementTemplateParameter,
    uml::OperationTemplateParameter,
    Association,
    uml::CommunicationPath,
    Package,
    uml::Model,
    uml::Profile,
    StructuredClassifier,
    uml::EncapsulatedClassifier,
    Vertex,
    Property,
    uml::ExtensionEnd,
    uml::Port,
    uml::ConnectionPointReference,
    uml::Pseudostate,
    Behavior,
    uml::Interaction,
    uml::OpaqueBehavior,
    uml::Activity,
    uml::StateMachine,
    StateMachine,
    uml::ProtocolStateMachine,
    Class,
    uml::Stereotype,
    uml::Component,
    uml::Extension,
    BehavioredClassifier,
    uml::Actor,
    uml::Collaboration,
    EncapsulatedClassifier,
    BehavioralFeature,
    uml::Reception,
    Feature,
    uml::Connector,
    DeployedArtifact,
    Artifact,
    uml::DeploymentSpecification,
    uml::Class,
    DeploymentTarget,
    uml::Node,
    StructuralFeature,
    Realization,
    uml::InterfaceRealization,
    uml::ComponentRealization,
    uml::AssociationClass,
    Transition,
    uml::ProtocolTransition,
    uml::ExpansionRegion,
    uml::ExpansionNode,
    uml::LoopNode,
    uml::ConditionalNode,
    CentralBufferNode,
    uml::DataStoreNode,
    uml::JoinNode,
    uml::StartObjectBehaviorAction,
    uml::ReduceAction,
    uml::UnmarshallAction,
    uml::ReplyAction,
    AcceptEventAction,
    uml::AcceptCallAction,
    uml::AcceptEventAction,
    CreateLinkAction,
    uml::CreateLinkObjectAction,
    uml::ReadLinkObjectEndQualifierAction,
    uml::StartClassifierBehaviorAction,
    uml::ReadIsClassifiedObjectAction,
    uml::ReclassifyObjectAction,
    uml::ReadLinkObjectEndAction,
    uml::ReadExtentAction,
    uml::ActionInputPin,
    uml::RaiseExceptionAction,
    WriteVariableAction,
    uml::RemoveVariableValueAction,
    uml::AddVariableValueAction,
    DirectedRelationship,
    uml::ProtocolConformance,
    VariableAction,
    uml::ClearVariableAction,
    uml::WriteVariableAction,
    Element,
    uml::QualifierValue,
    uml::LinkEndData,
    uml::ActivityGroup,
    uml::Slot,
    uml::Image,
    uml::MultiplicityElement,
    uml::Clause,
    uml::ExceptionHandler,
    uml::ReadVariableAction,
    uml::Comment,
    uml::VariableAction,
    EModelElement,
    uml::Element,
    MultiplicityElement,
    uml::Pin,
    uml::ConnectorEnd,
    ConnectableElement,
    uml::Variable,
    uml::Behavior,
    uml::Parameter,
    ValueSpecification,
    uml::LiteralSpecification,
    uml::TimeExpression,
    uml::Duration,
    uml::Interval,
    uml::InstanceValue,
    uml::Expression,
    uml::OpaqueExpression,
    Dependency,
    uml::Deployment,
    uml::Usage,
    uml::Abstraction,
    Abstraction,
    uml::Manifestation,
    uml::Realization,
    uml::ParameterableElement,
    uml::UseCase,
    uml::Substitution,
    uml::TemplateParameter,
    uml::TemplateParameterSubstitution,
    uml::TemplateSignature,
    uml::TemplateBinding,
    uml::TemplateableElement,
    uml::Property,
    Classifier,
    uml::Signal,
    uml::StructuredClassifier,
    uml::BehavioredClassifier,
    uml::Interface,
    uml::DataType,
    uml::InformationItem,
    uml::Artifact,
    TypedElement,
    uml::StructuralFeature,
    uml::ObjectNode,
    uml::Generalization,
    Type,
    RedefinableElement,
    uml::Feature,
    uml::ExtensionPoint,
    uml::ActivityEdge,
    uml::RedefinableTemplateSignature,
    uml::ActivityNode,
    uml::PackageImport,
    uml::ElementImport,
    uml::Relationship,
    uml::NamedElement,
    ParameterableElement,
    uml::ConnectableElement,
    NamedElement,
    uml::InteractionFragment,
    uml::MessageEnd,
    uml::CollaborationUse,
    uml::GeneralOrdering,
    uml::Extend,
    uml::TypedElement,
    uml::Include,
    uml::Vertex,
    uml::Message,
    uml::DeployedArtifact,
    uml::DeploymentTarget,
    uml::Trigger,
    uml::Namespace,
    uml::RedefinableElement,
    uml::ActivityPartition,
    uml::ParameterSet,
    uml::Lifeline,
    uml::ProfileApplication,
    uml::PackageableElement,
    uml::PackageMerge,
    TemplateableElement,
    uml::StringExpression,
    uml::Operation,
    PackageableElement,
    uml::Type,
    uml::Dependency,
    uml::ValueSpecification,
    uml::InstanceSpecification,
    uml::GeneralizationSet,
    uml::Observation,
    uml::InformationFlow,
    uml::Event,
    uml::Constraint,
    Namespace,
    uml::Classifier,
    uml::Region,
    uml::BehavioralFeature,
    uml::State,
    uml::StructuredActivityNode,
    uml::Transition,
    uml::InteractionOperand,
    uml::Package,
    Relationship,
    uml::Association,
    uml::DirectedRelationship,
    ObjectNodeOrderingKind,
    ExpansionKind,
    ParameterEffectKind,
    MessageKind,
    AggregationKind,
    TransitionKind,
    CallConcurrencyKind,
    VisibilityKind,
    ConnectorKind,
    ParameterDirectionKind,
    MessageSort,
    InteractionOperatorKind,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_uml::finalstate_is_not_abstract():
    assert not inspect.isabstract(uml::FinalState)


def test_uml::finalstate_constructor_exists():
    assert callable(uml::FinalState.__init__)


def test_uml::finalstate_constructor_args():
    sig = inspect.signature(uml::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_uml::durationobservation_is_not_abstract():
    assert not inspect.isabstract(uml::DurationObservation)


def test_uml::durationobservation_constructor_exists():
    assert callable(uml::DurationObservation.__init__)


def test_uml::durationobservation_constructor_args():
    sig = inspect.signature(uml::DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml::durationobservation_has_firstEvent():
    assert hasattr(uml::DurationObservation, "firstEvent")
    descriptor = None
    for klass in uml::DurationObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml::timeobservation_is_not_abstract():
    assert not inspect.isabstract(uml::TimeObservation)


def test_uml::timeobservation_constructor_exists():
    assert callable(uml::TimeObservation.__init__)


def test_uml::timeobservation_constructor_args():
    sig = inspect.signature(uml::TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml::timeobservation_has_firstEvent():
    assert hasattr(uml::TimeObservation, "firstEvent")
    descriptor = None
    for klass in uml::TimeObservation.__mro__:
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



def test_uml::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::DurationConstraint)


def test_uml::durationconstraint_constructor_exists():
    assert callable(uml::DurationConstraint.__init__)


def test_uml::durationconstraint_constructor_args():
    sig = inspect.signature(uml::DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml::durationconstraint_has_firstEvent():
    assert hasattr(uml::DurationConstraint, "firstEvent")
    descriptor = None
    for klass in uml::DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_uml::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::TimeConstraint)


def test_uml::timeconstraint_constructor_exists():
    assert callable(uml::TimeConstraint.__init__)


def test_uml::timeconstraint_constructor_args():
    sig = inspect.signature(uml::TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_uml::timeconstraint_has_firstEvent():
    assert hasattr(uml::TimeConstraint, "firstEvent")
    descriptor = None
    for klass in uml::TimeConstraint.__mro__:
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



def test_uml::timeinterval_is_not_abstract():
    assert not inspect.isabstract(uml::TimeInterval)


def test_uml::timeinterval_constructor_exists():
    assert callable(uml::TimeInterval.__init__)


def test_uml::timeinterval_constructor_args():
    sig = inspect.signature(uml::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml::durationinterval_is_not_abstract():
    assert not inspect.isabstract(uml::DurationInterval)


def test_uml::durationinterval_constructor_exists():
    assert callable(uml::DurationInterval.__init__)


def test_uml::durationinterval_constructor_args():
    sig = inspect.signature(uml::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml::DestroyLinkAction)


def test_uml::destroylinkaction_constructor_exists():
    assert callable(uml::DestroyLinkAction.__init__)


def test_uml::destroylinkaction_constructor_args():
    sig = inspect.signature(uml::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml::CreateLinkAction)


def test_uml::createlinkaction_constructor_exists():
    assert callable(uml::CreateLinkAction.__init__)


def test_uml::createlinkaction_constructor_args():
    sig = inspect.signature(uml::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(uml::LinkEndDestructionData)


def test_uml::linkenddestructiondata_constructor_exists():
    assert callable(uml::LinkEndDestructionData.__init__)


def test_uml::linkenddestructiondata_constructor_args():
    sig = inspect.signature(uml::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_uml::linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(uml::LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in uml::LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_uml::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(uml::LinkEndCreationData)


def test_uml::linkendcreationdata_constructor_exists():
    assert callable(uml::LinkEndCreationData.__init__)


def test_uml::linkendcreationdata_constructor_args():
    sig = inspect.signature(uml::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml::linkendcreationdata_has_isReplaceAll():
    assert hasattr(uml::LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in uml::LinkEndCreationData.__mro__:
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



def test_uml::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(uml::WriteLinkAction)


def test_uml::writelinkaction_constructor_exists():
    assert callable(uml::WriteLinkAction.__init__)


def test_uml::writelinkaction_constructor_args():
    sig = inspect.signature(uml::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadLinkAction)


def test_uml::readlinkaction_constructor_exists():
    assert callable(uml::ReadLinkAction.__init__)


def test_uml::readlinkaction_constructor_args():
    sig = inspect.signature(uml::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml::WriteStructuralFeatureAction)


def test_uml::writestructuralfeatureaction_constructor_exists():
    assert callable(uml::WriteStructuralFeatureAction.__init__)


def test_uml::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml::ClearStructuralFeatureAction)


def test_uml::clearstructuralfeatureaction_constructor_exists():
    assert callable(uml::ClearStructuralFeatureAction.__init__)


def test_uml::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadStructuralFeatureAction)


def test_uml::readstructuralfeatureaction_constructor_exists():
    assert callable(uml::ReadStructuralFeatureAction.__init__)


def test_uml::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::AddStructuralFeatureValueAction)


def test_uml::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml::AddStructuralFeatureValueAction.__init__)


def test_uml::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml::addstructuralfeaturevalueaction_has_isReplaceAll():
    assert hasattr(uml::AddStructuralFeatureValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml::AddStructuralFeatureValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::RemoveStructuralFeatureValueAction)


def test_uml::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml::RemoveStructuralFeatureValueAction.__init__)


def test_uml::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml::removestructuralfeaturevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml::RemoveStructuralFeatureValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml::RemoveStructuralFeatureValueAction.__mro__:
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



def test_uml::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(uml::ExecutionEnvironment)


def test_uml::executionenvironment_constructor_exists():
    assert callable(uml::ExecutionEnvironment.__init__)


def test_uml::executionenvironment_constructor_args():
    sig = inspect.signature(uml::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml::device_is_not_abstract():
    assert not inspect.isabstract(uml::Device)


def test_uml::device_constructor_exists():
    assert callable(uml::Device.__init__)


def test_uml::device_constructor_args():
    sig = inspect.signature(uml::Device.__init__)
    params = list(sig.parameters.keys())



def test_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml::considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(uml::ConsiderIgnoreFragment)


def test_uml::considerignorefragment_constructor_exists():
    assert callable(uml::ConsiderIgnoreFragment.__init__)


def test_uml::considerignorefragment_constructor_args():
    sig = inspect.signature(uml::ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml::ActivityFinalNode)


def test_uml::activityfinalnode_constructor_exists():
    assert callable(uml::ActivityFinalNode.__init__)


def test_uml::activityfinalnode_constructor_args():
    sig = inspect.signature(uml::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml::FlowFinalNode)


def test_uml::flowfinalnode_constructor_exists():
    assert callable(uml::FlowFinalNode.__init__)


def test_uml::flowfinalnode_constructor_args():
    sig = inspect.signature(uml::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::callevent_is_not_abstract():
    assert not inspect.isabstract(uml::CallEvent)


def test_uml::callevent_constructor_exists():
    assert callable(uml::CallEvent.__init__)


def test_uml::callevent_constructor_args():
    sig = inspect.signature(uml::CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::receivesignalevent_is_not_abstract():
    assert not inspect.isabstract(uml::ReceiveSignalEvent)


def test_uml::receivesignalevent_constructor_exists():
    assert callable(uml::ReceiveSignalEvent.__init__)


def test_uml::receivesignalevent_constructor_args():
    sig = inspect.signature(uml::ReceiveSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::signalevent_is_not_abstract():
    assert not inspect.isabstract(uml::SignalEvent)


def test_uml::signalevent_constructor_exists():
    assert callable(uml::SignalEvent.__init__)


def test_uml::signalevent_constructor_args():
    sig = inspect.signature(uml::SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::receiveoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml::ReceiveOperationEvent)


def test_uml::receiveoperationevent_constructor_exists():
    assert callable(uml::ReceiveOperationEvent.__init__)


def test_uml::receiveoperationevent_constructor_args():
    sig = inspect.signature(uml::ReceiveOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml::AnyReceiveEvent)


def test_uml::anyreceiveevent_constructor_exists():
    assert callable(uml::AnyReceiveEvent.__init__)


def test_uml::anyreceiveevent_constructor_args():
    sig = inspect.signature(uml::AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::sendsignalevent_is_not_abstract():
    assert not inspect.isabstract(uml::SendSignalEvent)


def test_uml::sendsignalevent_constructor_exists():
    assert callable(uml::SendSignalEvent.__init__)


def test_uml::sendsignalevent_constructor_args():
    sig = inspect.signature(uml::SendSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::sendoperationevent_is_not_abstract():
    assert not inspect.isabstract(uml::SendOperationEvent)


def test_uml::sendoperationevent_constructor_exists():
    assert callable(uml::SendOperationEvent.__init__)


def test_uml::sendoperationevent_constructor_args():
    sig = inspect.signature(uml::SendOperationEvent.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_uml::changeevent_is_not_abstract():
    assert not inspect.isabstract(uml::ChangeEvent)


def test_uml::changeevent_constructor_exists():
    assert callable(uml::ChangeEvent.__init__)


def test_uml::changeevent_constructor_args():
    sig = inspect.signature(uml::ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::destructionevent_is_not_abstract():
    assert not inspect.isabstract(uml::DestructionEvent)


def test_uml::destructionevent_constructor_exists():
    assert callable(uml::DestructionEvent.__init__)


def test_uml::destructionevent_constructor_args():
    sig = inspect.signature(uml::DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::messageevent_is_not_abstract():
    assert not inspect.isabstract(uml::MessageEvent)


def test_uml::messageevent_constructor_exists():
    assert callable(uml::MessageEvent.__init__)


def test_uml::messageevent_constructor_args():
    sig = inspect.signature(uml::MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::timeevent_is_not_abstract():
    assert not inspect.isabstract(uml::TimeEvent)


def test_uml::timeevent_constructor_exists():
    assert callable(uml::TimeEvent.__init__)


def test_uml::timeevent_constructor_args():
    sig = inspect.signature(uml::TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_uml::timeevent_has_isRelative():
    assert hasattr(uml::TimeEvent, "isRelative")
    descriptor = None
    for klass in uml::TimeEvent.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_uml::creationevent_is_not_abstract():
    assert not inspect.isabstract(uml::CreationEvent)


def test_uml::creationevent_constructor_exists():
    assert callable(uml::CreationEvent.__init__)


def test_uml::creationevent_constructor_args():
    sig = inspect.signature(uml::CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::executionevent_is_not_abstract():
    assert not inspect.isabstract(uml::ExecutionEvent)


def test_uml::executionevent_constructor_exists():
    assert callable(uml::ExecutionEvent.__init__)


def test_uml::executionevent_constructor_args():
    sig = inspect.signature(uml::ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml::BehaviorExecutionSpecification)


def test_uml::behaviorexecutionspecification_constructor_exists():
    assert callable(uml::BehaviorExecutionSpecification.__init__)


def test_uml::behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml::BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml::ActionExecutionSpecification)


def test_uml::actionexecutionspecification_constructor_exists():
    assert callable(uml::ActionExecutionSpecification.__init__)


def test_uml::actionexecutionspecification_constructor_args():
    sig = inspect.signature(uml::ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::IntervalConstraint)


def test_uml::intervalconstraint_constructor_exists():
    assert callable(uml::IntervalConstraint.__init__)


def test_uml::intervalconstraint_constructor_args():
    sig = inspect.signature(uml::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::InteractionConstraint)


def test_uml::interactionconstraint_constructor_exists():
    assert callable(uml::InteractionConstraint.__init__)


def test_uml::interactionconstraint_constructor_args():
    sig = inspect.signature(uml::InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml::ExecutionOccurrenceSpecification)


def test_uml::executionoccurrencespecification_constructor_exists():
    assert callable(uml::ExecutionOccurrenceSpecification.__init__)


def test_uml::executionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml::ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml::messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml::MessageOccurrenceSpecification)


def test_uml::messageoccurrencespecification_constructor_exists():
    assert callable(uml::MessageOccurrenceSpecification.__init__)


def test_uml::messageoccurrencespecification_constructor_args():
    sig = inspect.signature(uml::MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionuse_is_not_abstract():
    assert not inspect.isabstract(InteractionUse)


def test_interactionuse_constructor_exists():
    assert callable(InteractionUse.__init__)


def test_interactionuse_constructor_args():
    sig = inspect.signature(InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml::partdecomposition_is_not_abstract():
    assert not inspect.isabstract(uml::PartDecomposition)


def test_uml::partdecomposition_constructor_exists():
    assert callable(uml::PartDecomposition.__init__)


def test_uml::partdecomposition_constructor_args():
    sig = inspect.signature(uml::PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml::stateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml::StateInvariant)


def test_uml::stateinvariant_constructor_exists():
    assert callable(uml::StateInvariant.__init__)


def test_uml::stateinvariant_constructor_args():
    sig = inspect.signature(uml::StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml::occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml::OccurrenceSpecification)


def test_uml::occurrencespecification_constructor_exists():
    assert callable(uml::OccurrenceSpecification.__init__)


def test_uml::occurrencespecification_constructor_args():
    sig = inspect.signature(uml::OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::continuation_is_not_abstract():
    assert not inspect.isabstract(uml::Continuation)


def test_uml::continuation_constructor_exists():
    assert callable(uml::Continuation.__init__)


def test_uml::continuation_constructor_args():
    sig = inspect.signature(uml::Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_uml::continuation_has_setting():
    assert hasattr(uml::Continuation, "setting")
    descriptor = None
    for klass in uml::Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_uml::executionspecification_is_not_abstract():
    assert not inspect.isabstract(uml::ExecutionSpecification)


def test_uml::executionspecification_constructor_exists():
    assert callable(uml::ExecutionSpecification.__init__)


def test_uml::executionspecification_constructor_args():
    sig = inspect.signature(uml::ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::interactionuse_is_not_abstract():
    assert not inspect.isabstract(uml::InteractionUse)


def test_uml::interactionuse_constructor_exists():
    assert callable(uml::InteractionUse.__init__)


def test_uml::interactionuse_constructor_args():
    sig = inspect.signature(uml::InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml::CombinedFragment)


def test_uml::combinedfragment_constructor_exists():
    assert callable(uml::CombinedFragment.__init__)


def test_uml::combinedfragment_constructor_args():
    sig = inspect.signature(uml::CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_uml::combinedfragment_has_interactionOperator():
    assert hasattr(uml::CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in uml::CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml::valuepin_is_not_abstract():
    assert not inspect.isabstract(uml::ValuePin)


def test_uml::valuepin_constructor_exists():
    assert callable(uml::ValuePin.__init__)


def test_uml::valuepin_constructor_args():
    sig = inspect.signature(uml::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml::gate_is_not_abstract():
    assert not inspect.isabstract(uml::Gate)


def test_uml::gate_constructor_exists():
    assert callable(uml::Gate.__init__)


def test_uml::gate_constructor_args():
    sig = inspect.signature(uml::Gate.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::sequencenode_is_not_abstract():
    assert not inspect.isabstract(uml::SequenceNode)


def test_uml::sequencenode_constructor_exists():
    assert callable(uml::SequenceNode.__init__)


def test_uml::sequencenode_constructor_args():
    sig = inspect.signature(uml::SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml::CallBehaviorAction)


def test_uml::callbehavioraction_constructor_exists():
    assert callable(uml::CallBehaviorAction.__init__)


def test_uml::callbehavioraction_constructor_args():
    sig = inspect.signature(uml::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml::CallOperationAction)


def test_uml::calloperationaction_constructor_exists():
    assert callable(uml::CallOperationAction.__init__)


def test_uml::calloperationaction_constructor_args():
    sig = inspect.signature(uml::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml::BroadcastSignalAction)


def test_uml::broadcastsignalaction_constructor_exists():
    assert callable(uml::BroadcastSignalAction.__init__)


def test_uml::broadcastsignalaction_constructor_args():
    sig = inspect.signature(uml::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml::SendSignalAction)


def test_uml::sendsignalaction_constructor_exists():
    assert callable(uml::SendSignalAction.__init__)


def test_uml::sendsignalaction_constructor_args():
    sig = inspect.signature(uml::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::SendObjectAction)


def test_uml::sendobjectaction_constructor_exists():
    assert callable(uml::SendObjectAction.__init__)


def test_uml::sendobjectaction_constructor_args():
    sig = inspect.signature(uml::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::callaction_is_not_abstract():
    assert not inspect.isabstract(uml::CallAction)


def test_uml::callaction_constructor_exists():
    assert callable(uml::CallAction.__init__)


def test_uml::callaction_constructor_args():
    sig = inspect.signature(uml::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_uml::callaction_has_isSynchronous():
    assert hasattr(uml::CallAction, "isSynchronous")
    descriptor = None
    for klass in uml::CallAction.__mro__:
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



def test_uml::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml::CentralBufferNode)


def test_uml::centralbuffernode_constructor_exists():
    assert callable(uml::CentralBufferNode.__init__)


def test_uml::centralbuffernode_constructor_args():
    sig = inspect.signature(uml::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml::ActivityParameterNode)


def test_uml::activityparameternode_constructor_exists():
    assert callable(uml::ActivityParameterNode.__init__)


def test_uml::activityparameternode_constructor_args():
    sig = inspect.signature(uml::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::mergenode_is_not_abstract():
    assert not inspect.isabstract(uml::MergeNode)


def test_uml::mergenode_constructor_exists():
    assert callable(uml::MergeNode.__init__)


def test_uml::mergenode_constructor_args():
    sig = inspect.signature(uml::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::finalnode_is_not_abstract():
    assert not inspect.isabstract(uml::FinalNode)


def test_uml::finalnode_constructor_exists():
    assert callable(uml::FinalNode.__init__)


def test_uml::finalnode_constructor_args():
    sig = inspect.signature(uml::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::decisionnode_is_not_abstract():
    assert not inspect.isabstract(uml::DecisionNode)


def test_uml::decisionnode_constructor_exists():
    assert callable(uml::DecisionNode.__init__)


def test_uml::decisionnode_constructor_args():
    sig = inspect.signature(uml::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::forknode_is_not_abstract():
    assert not inspect.isabstract(uml::ForkNode)


def test_uml::forknode_constructor_exists():
    assert callable(uml::ForkNode.__init__)


def test_uml::forknode_constructor_args():
    sig = inspect.signature(uml::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::initialnode_is_not_abstract():
    assert not inspect.isabstract(uml::InitialNode)


def test_uml::initialnode_constructor_exists():
    assert callable(uml::InitialNode.__init__)


def test_uml::initialnode_constructor_args():
    sig = inspect.signature(uml::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml::objectflow_is_not_abstract():
    assert not inspect.isabstract(uml::ObjectFlow)


def test_uml::objectflow_constructor_exists():
    assert callable(uml::ObjectFlow.__init__)


def test_uml::objectflow_constructor_args():
    sig = inspect.signature(uml::ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"

def test_uml::objectflow_has_isMultireceive():
    assert hasattr(uml::ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in uml::ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_uml::objectflow_has_isMulticast():
    assert hasattr(uml::ObjectFlow, "isMulticast")
    descriptor = None
    for klass in uml::ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)



def test_uml::controlflow_is_not_abstract():
    assert not inspect.isabstract(uml::ControlFlow)


def test_uml::controlflow_constructor_exists():
    assert callable(uml::ControlFlow.__init__)


def test_uml::controlflow_constructor_args():
    sig = inspect.signature(uml::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml::interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml::InterruptibleActivityRegion)


def test_uml::interruptibleactivityregion_constructor_exists():
    assert callable(uml::InterruptibleActivityRegion.__init__)


def test_uml::interruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml::InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::controlnode_is_not_abstract():
    assert not inspect.isabstract(uml::ControlNode)


def test_uml::controlnode_constructor_exists():
    assert callable(uml::ControlNode.__init__)


def test_uml::controlnode_constructor_args():
    sig = inspect.signature(uml::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::executablenode_is_not_abstract():
    assert not inspect.isabstract(uml::ExecutableNode)


def test_uml::executablenode_constructor_exists():
    assert callable(uml::ExecutableNode.__init__)


def test_uml::executablenode_constructor_args():
    sig = inspect.signature(uml::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::action_is_not_abstract():
    assert not inspect.isabstract(uml::Action)


def test_uml::action_constructor_exists():
    assert callable(uml::Action.__init__)


def test_uml::action_constructor_args():
    sig = inspect.signature(uml::Action.__init__)
    params = list(sig.parameters.keys())



def test_uml::outputpin_is_not_abstract():
    assert not inspect.isabstract(uml::OutputPin)


def test_uml::outputpin_constructor_exists():
    assert callable(uml::OutputPin.__init__)


def test_uml::outputpin_constructor_args():
    sig = inspect.signature(uml::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml::inputpin_is_not_abstract():
    assert not inspect.isabstract(uml::InputPin)


def test_uml::inputpin_constructor_exists():
    assert callable(uml::InputPin.__init__)


def test_uml::inputpin_constructor_args():
    sig = inspect.signature(uml::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml::invocationaction_is_not_abstract():
    assert not inspect.isabstract(uml::InvocationAction)


def test_uml::invocationaction_constructor_exists():
    assert callable(uml::InvocationAction.__init__)


def test_uml::invocationaction_constructor_args():
    sig = inspect.signature(uml::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml::ValueSpecificationAction)


def test_uml::valuespecificationaction_constructor_exists():
    assert callable(uml::ValueSpecificationAction.__init__)


def test_uml::valuespecificationaction_constructor_args():
    sig = inspect.signature(uml::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::readselfaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadSelfAction)


def test_uml::readselfaction_constructor_exists():
    assert callable(uml::ReadSelfAction.__init__)


def test_uml::readselfaction_constructor_args():
    sig = inspect.signature(uml::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml::StructuralFeatureAction)


def test_uml::structuralfeatureaction_constructor_exists():
    assert callable(uml::StructuralFeatureAction.__init__)


def test_uml::structuralfeatureaction_constructor_args():
    sig = inspect.signature(uml::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::DestroyObjectAction)


def test_uml::destroyobjectaction_constructor_exists():
    assert callable(uml::DestroyObjectAction.__init__)


def test_uml::destroyobjectaction_constructor_args():
    sig = inspect.signature(uml::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyOwnedObjects" in params, "Missing parameter 'isDestroyOwnedObjects'"
    assert "isDestroyLinks" in params, "Missing parameter 'isDestroyLinks'"

def test_uml::destroyobjectaction_has_isDestroyOwnedObjects():
    assert hasattr(uml::DestroyObjectAction, "isDestroyOwnedObjects")
    descriptor = None
    for klass in uml::DestroyObjectAction.__mro__:
        if "isDestroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)

def test_uml::destroyobjectaction_has_isDestroyLinks():
    assert hasattr(uml::DestroyObjectAction, "isDestroyLinks")
    descriptor = None
    for klass in uml::DestroyObjectAction.__mro__:
        if "isDestroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyLinks"]
            break
    assert isinstance(descriptor, property)



def test_uml::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::CreateObjectAction)


def test_uml::createobjectaction_constructor_exists():
    assert callable(uml::CreateObjectAction.__init__)


def test_uml::createobjectaction_constructor_args():
    sig = inspect.signature(uml::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::linkaction_is_not_abstract():
    assert not inspect.isabstract(uml::LinkAction)


def test_uml::linkaction_constructor_exists():
    assert callable(uml::LinkAction.__init__)


def test_uml::linkaction_constructor_args():
    sig = inspect.signature(uml::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml::TestIdentityAction)


def test_uml::testidentityaction_constructor_exists():
    assert callable(uml::TestIdentityAction.__init__)


def test_uml::testidentityaction_constructor_args():
    sig = inspect.signature(uml::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml::ClearAssociationAction)


def test_uml::clearassociationaction_constructor_exists():
    assert callable(uml::ClearAssociationAction.__init__)


def test_uml::clearassociationaction_constructor_args():
    sig = inspect.signature(uml::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml::OpaqueAction)


def test_uml::opaqueaction_constructor_exists():
    assert callable(uml::OpaqueAction.__init__)


def test_uml::opaqueaction_constructor_args():
    sig = inspect.signature(uml::OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_uml::opaqueaction_has_language():
    assert hasattr(uml::OpaqueAction, "language")
    descriptor = None
    for klass in uml::OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml::opaqueaction_has_body():
    assert hasattr(uml::OpaqueAction, "body")
    descriptor = None
    for klass in uml::OpaqueAction.__mro__:
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



def test_uml::functionbehavior_is_not_abstract():
    assert not inspect.isabstract(uml::FunctionBehavior)


def test_uml::functionbehavior_constructor_exists():
    assert callable(uml::FunctionBehavior.__init__)


def test_uml::functionbehavior_constructor_args():
    sig = inspect.signature(uml::FunctionBehavior.__init__)
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



def test_uml::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml::LiteralUnlimitedNatural)


def test_uml::literalunlimitednatural_constructor_exists():
    assert callable(uml::LiteralUnlimitedNatural.__init__)


def test_uml::literalunlimitednatural_constructor_args():
    sig = inspect.signature(uml::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml::literalunlimitednatural_has_value():
    assert hasattr(uml::LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in uml::LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml::literalnull_is_not_abstract():
    assert not inspect.isabstract(uml::LiteralNull)


def test_uml::literalnull_constructor_exists():
    assert callable(uml::LiteralNull.__init__)


def test_uml::literalnull_constructor_args():
    sig = inspect.signature(uml::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml::literalstring_is_not_abstract():
    assert not inspect.isabstract(uml::LiteralString)


def test_uml::literalstring_constructor_exists():
    assert callable(uml::LiteralString.__init__)


def test_uml::literalstring_constructor_args():
    sig = inspect.signature(uml::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml::literalstring_has_value():
    assert hasattr(uml::LiteralString, "value")
    descriptor = None
    for klass in uml::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml::literalboolean_is_not_abstract():
    assert not inspect.isabstract(uml::LiteralBoolean)


def test_uml::literalboolean_constructor_exists():
    assert callable(uml::LiteralBoolean.__init__)


def test_uml::literalboolean_constructor_args():
    sig = inspect.signature(uml::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml::literalboolean_has_value():
    assert hasattr(uml::LiteralBoolean, "value")
    descriptor = None
    for klass in uml::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml::literalinteger_is_not_abstract():
    assert not inspect.isabstract(uml::LiteralInteger)


def test_uml::literalinteger_constructor_exists():
    assert callable(uml::LiteralInteger.__init__)


def test_uml::literalinteger_constructor_args():
    sig = inspect.signature(uml::LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml::literalinteger_has_value():
    assert hasattr(uml::LiteralInteger, "value")
    descriptor = None
    for klass in uml::LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml::EnumerationLiteral)


def test_uml::enumerationliteral_constructor_exists():
    assert callable(uml::EnumerationLiteral.__init__)


def test_uml::enumerationliteral_constructor_args():
    sig = inspect.signature(uml::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml::primitivetype_is_not_abstract():
    assert not inspect.isabstract(uml::PrimitiveType)


def test_uml::primitivetype_constructor_exists():
    assert callable(uml::PrimitiveType.__init__)


def test_uml::primitivetype_constructor_args():
    sig = inspect.signature(uml::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml::enumeration_is_not_abstract():
    assert not inspect.isabstract(uml::Enumeration)


def test_uml::enumeration_constructor_exists():
    assert callable(uml::Enumeration.__init__)


def test_uml::enumeration_constructor_args():
    sig = inspect.signature(uml::Enumeration.__init__)
    params = list(sig.parameters.keys())



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



def test_uml::classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::ClassifierTemplateParameter)


def test_uml::classifiertemplateparameter_constructor_exists():
    assert callable(uml::ClassifierTemplateParameter.__init__)


def test_uml::classifiertemplateparameter_constructor_args():
    sig = inspect.signature(uml::ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"

def test_uml::classifiertemplateparameter_has_allowSubstitutable():
    assert hasattr(uml::ClassifierTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in uml::ClassifierTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml::connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::ConnectableElementTemplateParameter)


def test_uml::connectableelementtemplateparameter_constructor_exists():
    assert callable(uml::ConnectableElementTemplateParameter.__init__)


def test_uml::connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(uml::ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml::operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::OperationTemplateParameter)


def test_uml::operationtemplateparameter_constructor_exists():
    assert callable(uml::OperationTemplateParameter.__init__)


def test_uml::operationtemplateparameter_constructor_args():
    sig = inspect.signature(uml::OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml::communicationpath_is_not_abstract():
    assert not inspect.isabstract(uml::CommunicationPath)


def test_uml::communicationpath_constructor_exists():
    assert callable(uml::CommunicationPath.__init__)


def test_uml::communicationpath_constructor_args():
    sig = inspect.signature(uml::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml::model_is_not_abstract():
    assert not inspect.isabstract(uml::Model)


def test_uml::model_constructor_exists():
    assert callable(uml::Model.__init__)


def test_uml::model_constructor_args():
    sig = inspect.signature(uml::Model.__init__)
    params = list(sig.parameters.keys())
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"

def test_uml::model_has_viewpoint():
    assert hasattr(uml::Model, "viewpoint")
    descriptor = None
    for klass in uml::Model.__mro__:
        if "viewpoint" in klass.__dict__:
            descriptor = klass.__dict__["viewpoint"]
            break
    assert isinstance(descriptor, property)



def test_uml::profile_is_not_abstract():
    assert not inspect.isabstract(uml::Profile)


def test_uml::profile_constructor_exists():
    assert callable(uml::Profile.__init__)


def test_uml::profile_constructor_args():
    sig = inspect.signature(uml::Profile.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::EncapsulatedClassifier)


def test_uml::encapsulatedclassifier_constructor_exists():
    assert callable(uml::EncapsulatedClassifier.__init__)


def test_uml::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml::EncapsulatedClassifier.__init__)
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



def test_uml::extensionend_is_not_abstract():
    assert not inspect.isabstract(uml::ExtensionEnd)


def test_uml::extensionend_constructor_exists():
    assert callable(uml::ExtensionEnd.__init__)


def test_uml::extensionend_constructor_args():
    sig = inspect.signature(uml::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml::port_is_not_abstract():
    assert not inspect.isabstract(uml::Port)


def test_uml::port_constructor_exists():
    assert callable(uml::Port.__init__)


def test_uml::port_constructor_args():
    sig = inspect.signature(uml::Port.__init__)
    params = list(sig.parameters.keys())
    assert "isService" in params, "Missing parameter 'isService'"
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"

def test_uml::port_has_isService():
    assert hasattr(uml::Port, "isService")
    descriptor = None
    for klass in uml::Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)

def test_uml::port_has_isBehavior():
    assert hasattr(uml::Port, "isBehavior")
    descriptor = None
    for klass in uml::Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)



def test_uml::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml::ConnectionPointReference)


def test_uml::connectionpointreference_constructor_exists():
    assert callable(uml::ConnectionPointReference.__init__)


def test_uml::connectionpointreference_constructor_args():
    sig = inspect.signature(uml::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml::pseudostate_is_not_abstract():
    assert not inspect.isabstract(uml::Pseudostate)


def test_uml::pseudostate_constructor_exists():
    assert callable(uml::Pseudostate.__init__)


def test_uml::pseudostate_constructor_args():
    sig = inspect.signature(uml::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml::pseudostate_has_kind():
    assert hasattr(uml::Pseudostate, "kind")
    descriptor = None
    for klass in uml::Pseudostate.__mro__:
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



def test_uml::interaction_is_not_abstract():
    assert not inspect.isabstract(uml::Interaction)


def test_uml::interaction_constructor_exists():
    assert callable(uml::Interaction.__init__)


def test_uml::interaction_constructor_args():
    sig = inspect.signature(uml::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(uml::OpaqueBehavior)


def test_uml::opaquebehavior_constructor_exists():
    assert callable(uml::OpaqueBehavior.__init__)


def test_uml::opaquebehavior_constructor_args():
    sig = inspect.signature(uml::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml::opaquebehavior_has_body():
    assert hasattr(uml::OpaqueBehavior, "body")
    descriptor = None
    for klass in uml::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml::opaquebehavior_has_language():
    assert hasattr(uml::OpaqueBehavior, "language")
    descriptor = None
    for klass in uml::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_uml::activity_is_not_abstract():
    assert not inspect.isabstract(uml::Activity)


def test_uml::activity_constructor_exists():
    assert callable(uml::Activity.__init__)


def test_uml::activity_constructor_args():
    sig = inspect.signature(uml::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_uml::activity_has_isReadOnly():
    assert hasattr(uml::Activity, "isReadOnly")
    descriptor = None
    for klass in uml::Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_uml::activity_has_isSingleExecution():
    assert hasattr(uml::Activity, "isSingleExecution")
    descriptor = None
    for klass in uml::Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)



def test_uml::statemachine_is_not_abstract():
    assert not inspect.isabstract(uml::StateMachine)


def test_uml::statemachine_constructor_exists():
    assert callable(uml::StateMachine.__init__)


def test_uml::statemachine_constructor_args():
    sig = inspect.signature(uml::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml::ProtocolStateMachine)


def test_uml::protocolstatemachine_constructor_exists():
    assert callable(uml::ProtocolStateMachine.__init__)


def test_uml::protocolstatemachine_constructor_args():
    sig = inspect.signature(uml::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml::stereotype_is_not_abstract():
    assert not inspect.isabstract(uml::Stereotype)


def test_uml::stereotype_constructor_exists():
    assert callable(uml::Stereotype.__init__)


def test_uml::stereotype_constructor_args():
    sig = inspect.signature(uml::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml::component_is_not_abstract():
    assert not inspect.isabstract(uml::Component)


def test_uml::component_constructor_exists():
    assert callable(uml::Component.__init__)


def test_uml::component_constructor_args():
    sig = inspect.signature(uml::Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"

def test_uml::component_has_isIndirectlyInstantiated():
    assert hasattr(uml::Component, "isIndirectlyInstantiated")
    descriptor = None
    for klass in uml::Component.__mro__:
        if "isIndirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["isIndirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)



def test_uml::extension_is_not_abstract():
    assert not inspect.isabstract(uml::Extension)


def test_uml::extension_constructor_exists():
    assert callable(uml::Extension.__init__)


def test_uml::extension_constructor_args():
    sig = inspect.signature(uml::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_uml::extension_has_isRequired():
    assert hasattr(uml::Extension, "isRequired")
    descriptor = None
    for klass in uml::Extension.__mro__:
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



def test_uml::actor_is_not_abstract():
    assert not inspect.isabstract(uml::Actor)


def test_uml::actor_constructor_exists():
    assert callable(uml::Actor.__init__)


def test_uml::actor_constructor_args():
    sig = inspect.signature(uml::Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml::collaboration_is_not_abstract():
    assert not inspect.isabstract(uml::Collaboration)


def test_uml::collaboration_constructor_exists():
    assert callable(uml::Collaboration.__init__)


def test_uml::collaboration_constructor_args():
    sig = inspect.signature(uml::Collaboration.__init__)
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



def test_uml::reception_is_not_abstract():
    assert not inspect.isabstract(uml::Reception)


def test_uml::reception_constructor_exists():
    assert callable(uml::Reception.__init__)


def test_uml::reception_constructor_args():
    sig = inspect.signature(uml::Reception.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml::connector_is_not_abstract():
    assert not inspect.isabstract(uml::Connector)


def test_uml::connector_constructor_exists():
    assert callable(uml::Connector.__init__)


def test_uml::connector_constructor_args():
    sig = inspect.signature(uml::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml::connector_has_kind():
    assert hasattr(uml::Connector, "kind")
    descriptor = None
    for klass in uml::Connector.__mro__:
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



def test_uml::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(uml::DeploymentSpecification)


def test_uml::deploymentspecification_constructor_exists():
    assert callable(uml::DeploymentSpecification.__init__)


def test_uml::deploymentspecification_constructor_args():
    sig = inspect.signature(uml::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"

def test_uml::deploymentspecification_has_executionLocation():
    assert hasattr(uml::DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in uml::DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)

def test_uml::deploymentspecification_has_deploymentLocation():
    assert hasattr(uml::DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in uml::DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)



def test_uml::class_is_not_abstract():
    assert not inspect.isabstract(uml::Class)


def test_uml::class_constructor_exists():
    assert callable(uml::Class.__init__)


def test_uml::class_constructor_args():
    sig = inspect.signature(uml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml::class_has_isActive():
    assert hasattr(uml::Class, "isActive")
    descriptor = None
    for klass in uml::Class.__mro__:
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



def test_uml::node_is_not_abstract():
    assert not inspect.isabstract(uml::Node)


def test_uml::node_constructor_exists():
    assert callable(uml::Node.__init__)


def test_uml::node_constructor_args():
    sig = inspect.signature(uml::Node.__init__)
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



def test_uml::interfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml::InterfaceRealization)


def test_uml::interfacerealization_constructor_exists():
    assert callable(uml::InterfaceRealization.__init__)


def test_uml::interfacerealization_constructor_args():
    sig = inspect.signature(uml::InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml::componentrealization_is_not_abstract():
    assert not inspect.isabstract(uml::ComponentRealization)


def test_uml::componentrealization_constructor_exists():
    assert callable(uml::ComponentRealization.__init__)


def test_uml::componentrealization_constructor_args():
    sig = inspect.signature(uml::ComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml::associationclass_is_not_abstract():
    assert not inspect.isabstract(uml::AssociationClass)


def test_uml::associationclass_constructor_exists():
    assert callable(uml::AssociationClass.__init__)


def test_uml::associationclass_constructor_args():
    sig = inspect.signature(uml::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(uml::ProtocolTransition)


def test_uml::protocoltransition_constructor_exists():
    assert callable(uml::ProtocolTransition.__init__)


def test_uml::protocoltransition_constructor_args():
    sig = inspect.signature(uml::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml::expansionregion_is_not_abstract():
    assert not inspect.isabstract(uml::ExpansionRegion)


def test_uml::expansionregion_constructor_exists():
    assert callable(uml::ExpansionRegion.__init__)


def test_uml::expansionregion_constructor_args():
    sig = inspect.signature(uml::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_uml::expansionregion_has_mode():
    assert hasattr(uml::ExpansionRegion, "mode")
    descriptor = None
    for klass in uml::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_uml::expansionnode_is_not_abstract():
    assert not inspect.isabstract(uml::ExpansionNode)


def test_uml::expansionnode_constructor_exists():
    assert callable(uml::ExpansionNode.__init__)


def test_uml::expansionnode_constructor_args():
    sig = inspect.signature(uml::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::loopnode_is_not_abstract():
    assert not inspect.isabstract(uml::LoopNode)


def test_uml::loopnode_constructor_exists():
    assert callable(uml::LoopNode.__init__)


def test_uml::loopnode_constructor_args():
    sig = inspect.signature(uml::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_uml::loopnode_has_isTestedFirst():
    assert hasattr(uml::LoopNode, "isTestedFirst")
    descriptor = None
    for klass in uml::LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_uml::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(uml::ConditionalNode)


def test_uml::conditionalnode_constructor_exists():
    assert callable(uml::ConditionalNode.__init__)


def test_uml::conditionalnode_constructor_args():
    sig = inspect.signature(uml::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isAssured" in params, "Missing parameter 'isAssured'"
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"

def test_uml::conditionalnode_has_isAssured():
    assert hasattr(uml::ConditionalNode, "isAssured")
    descriptor = None
    for klass in uml::ConditionalNode.__mro__:
        if "isAssured" in klass.__dict__:
            descriptor = klass.__dict__["isAssured"]
            break
    assert isinstance(descriptor, property)

def test_uml::conditionalnode_has_isDeterminate():
    assert hasattr(uml::ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in uml::ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::datastorenode_is_not_abstract():
    assert not inspect.isabstract(uml::DataStoreNode)


def test_uml::datastorenode_constructor_exists():
    assert callable(uml::DataStoreNode.__init__)


def test_uml::datastorenode_constructor_args():
    sig = inspect.signature(uml::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::joinnode_is_not_abstract():
    assert not inspect.isabstract(uml::JoinNode)


def test_uml::joinnode_constructor_exists():
    assert callable(uml::JoinNode.__init__)


def test_uml::joinnode_constructor_args():
    sig = inspect.signature(uml::JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_uml::joinnode_has_isCombineDuplicate():
    assert hasattr(uml::JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in uml::JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_uml::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml::StartObjectBehaviorAction)


def test_uml::startobjectbehavioraction_constructor_exists():
    assert callable(uml::StartObjectBehaviorAction.__init__)


def test_uml::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::reduceaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReduceAction)


def test_uml::reduceaction_constructor_exists():
    assert callable(uml::ReduceAction.__init__)


def test_uml::reduceaction_constructor_args():
    sig = inspect.signature(uml::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_uml::reduceaction_has_isOrdered():
    assert hasattr(uml::ReduceAction, "isOrdered")
    descriptor = None
    for klass in uml::ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_uml::unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml::UnmarshallAction)


def test_uml::unmarshallaction_constructor_exists():
    assert callable(uml::UnmarshallAction.__init__)


def test_uml::unmarshallaction_constructor_args():
    sig = inspect.signature(uml::UnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::replyaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReplyAction)


def test_uml::replyaction_constructor_exists():
    assert callable(uml::ReplyAction.__init__)


def test_uml::replyaction_constructor_args():
    sig = inspect.signature(uml::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(uml::AcceptCallAction)


def test_uml::acceptcallaction_constructor_exists():
    assert callable(uml::AcceptCallAction.__init__)


def test_uml::acceptcallaction_constructor_args():
    sig = inspect.signature(uml::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml::AcceptEventAction)


def test_uml::accepteventaction_constructor_exists():
    assert callable(uml::AcceptEventAction.__init__)


def test_uml::accepteventaction_constructor_args():
    sig = inspect.signature(uml::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_uml::accepteventaction_has_isUnmarshall():
    assert hasattr(uml::AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in uml::AcceptEventAction.__mro__:
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



def test_uml::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::CreateLinkObjectAction)


def test_uml::createlinkobjectaction_constructor_exists():
    assert callable(uml::CreateLinkObjectAction.__init__)


def test_uml::createlinkobjectaction_constructor_args():
    sig = inspect.signature(uml::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadLinkObjectEndQualifierAction)


def test_uml::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml::ReadLinkObjectEndQualifierAction.__init__)


def test_uml::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml::StartClassifierBehaviorAction)


def test_uml::startclassifierbehavioraction_constructor_exists():
    assert callable(uml::StartClassifierBehaviorAction.__init__)


def test_uml::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadIsClassifiedObjectAction)


def test_uml::readisclassifiedobjectaction_constructor_exists():
    assert callable(uml::ReadIsClassifiedObjectAction.__init__)


def test_uml::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDirect" in params, "Missing parameter 'isDirect'"

def test_uml::readisclassifiedobjectaction_has_isDirect():
    assert hasattr(uml::ReadIsClassifiedObjectAction, "isDirect")
    descriptor = None
    for klass in uml::ReadIsClassifiedObjectAction.__mro__:
        if "isDirect" in klass.__dict__:
            descriptor = klass.__dict__["isDirect"]
            break
    assert isinstance(descriptor, property)



def test_uml::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReclassifyObjectAction)


def test_uml::reclassifyobjectaction_constructor_exists():
    assert callable(uml::ReclassifyObjectAction.__init__)


def test_uml::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml::reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(uml::ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in uml::ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadLinkObjectEndAction)


def test_uml::readlinkobjectendaction_constructor_exists():
    assert callable(uml::ReadLinkObjectEndAction.__init__)


def test_uml::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::readextentaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadExtentAction)


def test_uml::readextentaction_constructor_exists():
    assert callable(uml::ReadExtentAction.__init__)


def test_uml::readextentaction_constructor_args():
    sig = inspect.signature(uml::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::actioninputpin_is_not_abstract():
    assert not inspect.isabstract(uml::ActionInputPin)


def test_uml::actioninputpin_constructor_exists():
    assert callable(uml::ActionInputPin.__init__)


def test_uml::actioninputpin_constructor_args():
    sig = inspect.signature(uml::ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml::RaiseExceptionAction)


def test_uml::raiseexceptionaction_constructor_exists():
    assert callable(uml::RaiseExceptionAction.__init__)


def test_uml::raiseexceptionaction_constructor_args():
    sig = inspect.signature(uml::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::RemoveVariableValueAction)


def test_uml::removevariablevalueaction_constructor_exists():
    assert callable(uml::RemoveVariableValueAction.__init__)


def test_uml::removevariablevalueaction_constructor_args():
    sig = inspect.signature(uml::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_uml::removevariablevalueaction_has_isRemoveDuplicates():
    assert hasattr(uml::RemoveVariableValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in uml::RemoveVariableValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_uml::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::AddVariableValueAction)


def test_uml::addvariablevalueaction_constructor_exists():
    assert callable(uml::AddVariableValueAction.__init__)


def test_uml::addvariablevalueaction_constructor_args():
    sig = inspect.signature(uml::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml::addvariablevalueaction_has_isReplaceAll():
    assert hasattr(uml::AddVariableValueAction, "isReplaceAll")
    descriptor = None
    for klass in uml::AddVariableValueAction.__mro__:
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



def test_uml::protocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml::ProtocolConformance)


def test_uml::protocolconformance_constructor_exists():
    assert callable(uml::ProtocolConformance.__init__)


def test_uml::protocolconformance_constructor_args():
    sig = inspect.signature(uml::ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml::ClearVariableAction)


def test_uml::clearvariableaction_constructor_exists():
    assert callable(uml::ClearVariableAction.__init__)


def test_uml::clearvariableaction_constructor_args():
    sig = inspect.signature(uml::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(uml::WriteVariableAction)


def test_uml::writevariableaction_constructor_exists():
    assert callable(uml::WriteVariableAction.__init__)


def test_uml::writevariableaction_constructor_args():
    sig = inspect.signature(uml::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml::QualifierValue)


def test_uml::qualifiervalue_constructor_exists():
    assert callable(uml::QualifierValue.__init__)


def test_uml::qualifiervalue_constructor_args():
    sig = inspect.signature(uml::QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml::linkenddata_is_not_abstract():
    assert not inspect.isabstract(uml::LinkEndData)


def test_uml::linkenddata_constructor_exists():
    assert callable(uml::LinkEndData.__init__)


def test_uml::linkenddata_constructor_args():
    sig = inspect.signature(uml::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml::activitygroup_is_not_abstract():
    assert not inspect.isabstract(uml::ActivityGroup)


def test_uml::activitygroup_constructor_exists():
    assert callable(uml::ActivityGroup.__init__)


def test_uml::activitygroup_constructor_args():
    sig = inspect.signature(uml::ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml::slot_is_not_abstract():
    assert not inspect.isabstract(uml::Slot)


def test_uml::slot_constructor_exists():
    assert callable(uml::Slot.__init__)


def test_uml::slot_constructor_args():
    sig = inspect.signature(uml::Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml::image_is_not_abstract():
    assert not inspect.isabstract(uml::Image)


def test_uml::image_constructor_exists():
    assert callable(uml::Image.__init__)


def test_uml::image_constructor_args():
    sig = inspect.signature(uml::Image.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "content" in params, "Missing parameter 'content'"
    assert "format" in params, "Missing parameter 'format'"

def test_uml::image_has_location():
    assert hasattr(uml::Image, "location")
    descriptor = None
    for klass in uml::Image.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_uml::image_has_content():
    assert hasattr(uml::Image, "content")
    descriptor = None
    for klass in uml::Image.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_uml::image_has_format():
    assert hasattr(uml::Image, "format")
    descriptor = None
    for klass in uml::Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_uml::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(uml::MultiplicityElement)


def test_uml::multiplicityelement_constructor_exists():
    assert callable(uml::MultiplicityElement.__init__)


def test_uml::multiplicityelement_constructor_args():
    sig = inspect.signature(uml::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_uml::multiplicityelement_has_isUnique():
    assert hasattr(uml::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in uml::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_uml::multiplicityelement_has_lower():
    assert hasattr(uml::MultiplicityElement, "lower")
    descriptor = None
    for klass in uml::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml::multiplicityelement_has_upper():
    assert hasattr(uml::MultiplicityElement, "upper")
    descriptor = None
    for klass in uml::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml::multiplicityelement_has_isOrdered():
    assert hasattr(uml::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in uml::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_uml::clause_is_not_abstract():
    assert not inspect.isabstract(uml::Clause)


def test_uml::clause_constructor_exists():
    assert callable(uml::Clause.__init__)


def test_uml::clause_constructor_args():
    sig = inspect.signature(uml::Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml::ExceptionHandler)


def test_uml::exceptionhandler_constructor_exists():
    assert callable(uml::ExceptionHandler.__init__)


def test_uml::exceptionhandler_constructor_args():
    sig = inspect.signature(uml::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml::ReadVariableAction)


def test_uml::readvariableaction_constructor_exists():
    assert callable(uml::ReadVariableAction.__init__)


def test_uml::readvariableaction_constructor_args():
    sig = inspect.signature(uml::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::comment_is_not_abstract():
    assert not inspect.isabstract(uml::Comment)


def test_uml::comment_constructor_exists():
    assert callable(uml::Comment.__init__)


def test_uml::comment_constructor_args():
    sig = inspect.signature(uml::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uml::comment_has_body():
    assert hasattr(uml::Comment, "body")
    descriptor = None
    for klass in uml::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uml::variableaction_is_not_abstract():
    assert not inspect.isabstract(uml::VariableAction)


def test_uml::variableaction_constructor_exists():
    assert callable(uml::VariableAction.__init__)


def test_uml::variableaction_constructor_args():
    sig = inspect.signature(uml::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::element_is_not_abstract():
    assert not inspect.isabstract(uml::Element)


def test_uml::element_constructor_exists():
    assert callable(uml::Element.__init__)


def test_uml::element_constructor_args():
    sig = inspect.signature(uml::Element.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::pin_is_not_abstract():
    assert not inspect.isabstract(uml::Pin)


def test_uml::pin_constructor_exists():
    assert callable(uml::Pin.__init__)


def test_uml::pin_constructor_args():
    sig = inspect.signature(uml::Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_uml::pin_has_isControl():
    assert hasattr(uml::Pin, "isControl")
    descriptor = None
    for klass in uml::Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_uml::connectorend_is_not_abstract():
    assert not inspect.isabstract(uml::ConnectorEnd)


def test_uml::connectorend_constructor_exists():
    assert callable(uml::ConnectorEnd.__init__)


def test_uml::connectorend_constructor_args():
    sig = inspect.signature(uml::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::variable_is_not_abstract():
    assert not inspect.isabstract(uml::Variable)


def test_uml::variable_constructor_exists():
    assert callable(uml::Variable.__init__)


def test_uml::variable_constructor_args():
    sig = inspect.signature(uml::Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavior_is_not_abstract():
    assert not inspect.isabstract(uml::Behavior)


def test_uml::behavior_constructor_exists():
    assert callable(uml::Behavior.__init__)


def test_uml::behavior_constructor_args():
    sig = inspect.signature(uml::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_uml::behavior_has_isReentrant():
    assert hasattr(uml::Behavior, "isReentrant")
    descriptor = None
    for klass in uml::Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_uml::parameter_is_not_abstract():
    assert not inspect.isabstract(uml::Parameter)


def test_uml::parameter_constructor_exists():
    assert callable(uml::Parameter.__init__)


def test_uml::parameter_constructor_args():
    sig = inspect.signature(uml::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "default" in params, "Missing parameter 'default'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isStream" in params, "Missing parameter 'isStream'"

def test_uml::parameter_has_effect():
    assert hasattr(uml::Parameter, "effect")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_uml::parameter_has_isException():
    assert hasattr(uml::Parameter, "isException")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_uml::parameter_has_default():
    assert hasattr(uml::Parameter, "default")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml::parameter_has_direction():
    assert hasattr(uml::Parameter, "direction")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_uml::parameter_has_isStream():
    assert hasattr(uml::Parameter, "isStream")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "isStream" in klass.__dict__:
            descriptor = klass.__dict__["isStream"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::literalspecification_is_not_abstract():
    assert not inspect.isabstract(uml::LiteralSpecification)


def test_uml::literalspecification_constructor_exists():
    assert callable(uml::LiteralSpecification.__init__)


def test_uml::literalspecification_constructor_args():
    sig = inspect.signature(uml::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::timeexpression_is_not_abstract():
    assert not inspect.isabstract(uml::TimeExpression)


def test_uml::timeexpression_constructor_exists():
    assert callable(uml::TimeExpression.__init__)


def test_uml::timeexpression_constructor_args():
    sig = inspect.signature(uml::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml::duration_is_not_abstract():
    assert not inspect.isabstract(uml::Duration)


def test_uml::duration_constructor_exists():
    assert callable(uml::Duration.__init__)


def test_uml::duration_constructor_args():
    sig = inspect.signature(uml::Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml::interval_is_not_abstract():
    assert not inspect.isabstract(uml::Interval)


def test_uml::interval_constructor_exists():
    assert callable(uml::Interval.__init__)


def test_uml::interval_constructor_args():
    sig = inspect.signature(uml::Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml::instancevalue_is_not_abstract():
    assert not inspect.isabstract(uml::InstanceValue)


def test_uml::instancevalue_constructor_exists():
    assert callable(uml::InstanceValue.__init__)


def test_uml::instancevalue_constructor_args():
    sig = inspect.signature(uml::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml::expression_is_not_abstract():
    assert not inspect.isabstract(uml::Expression)


def test_uml::expression_constructor_exists():
    assert callable(uml::Expression.__init__)


def test_uml::expression_constructor_args():
    sig = inspect.signature(uml::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_uml::expression_has_symbol():
    assert hasattr(uml::Expression, "symbol")
    descriptor = None
    for klass in uml::Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_uml::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml::OpaqueExpression)


def test_uml::opaqueexpression_constructor_exists():
    assert callable(uml::OpaqueExpression.__init__)


def test_uml::opaqueexpression_constructor_args():
    sig = inspect.signature(uml::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_uml::opaqueexpression_has_language():
    assert hasattr(uml::OpaqueExpression, "language")
    descriptor = None
    for klass in uml::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml::opaqueexpression_has_body():
    assert hasattr(uml::OpaqueExpression, "body")
    descriptor = None
    for klass in uml::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml::deployment_is_not_abstract():
    assert not inspect.isabstract(uml::Deployment)


def test_uml::deployment_constructor_exists():
    assert callable(uml::Deployment.__init__)


def test_uml::deployment_constructor_args():
    sig = inspect.signature(uml::Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml::usage_is_not_abstract():
    assert not inspect.isabstract(uml::Usage)


def test_uml::usage_constructor_exists():
    assert callable(uml::Usage.__init__)


def test_uml::usage_constructor_args():
    sig = inspect.signature(uml::Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml::abstraction_is_not_abstract():
    assert not inspect.isabstract(uml::Abstraction)


def test_uml::abstraction_constructor_exists():
    assert callable(uml::Abstraction.__init__)


def test_uml::abstraction_constructor_args():
    sig = inspect.signature(uml::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml::manifestation_is_not_abstract():
    assert not inspect.isabstract(uml::Manifestation)


def test_uml::manifestation_constructor_exists():
    assert callable(uml::Manifestation.__init__)


def test_uml::manifestation_constructor_args():
    sig = inspect.signature(uml::Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml::realization_is_not_abstract():
    assert not inspect.isabstract(uml::Realization)


def test_uml::realization_constructor_exists():
    assert callable(uml::Realization.__init__)


def test_uml::realization_constructor_args():
    sig = inspect.signature(uml::Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml::parameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml::ParameterableElement)


def test_uml::parameterableelement_constructor_exists():
    assert callable(uml::ParameterableElement.__init__)


def test_uml::parameterableelement_constructor_args():
    sig = inspect.signature(uml::ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::usecase_is_not_abstract():
    assert not inspect.isabstract(uml::UseCase)


def test_uml::usecase_constructor_exists():
    assert callable(uml::UseCase.__init__)


def test_uml::usecase_constructor_args():
    sig = inspect.signature(uml::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml::substitution_is_not_abstract():
    assert not inspect.isabstract(uml::Substitution)


def test_uml::substitution_constructor_exists():
    assert callable(uml::Substitution.__init__)


def test_uml::substitution_constructor_args():
    sig = inspect.signature(uml::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml::templateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::TemplateParameter)


def test_uml::templateparameter_constructor_exists():
    assert callable(uml::TemplateParameter.__init__)


def test_uml::templateparameter_constructor_args():
    sig = inspect.signature(uml::TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml::templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml::TemplateParameterSubstitution)


def test_uml::templateparametersubstitution_constructor_exists():
    assert callable(uml::TemplateParameterSubstitution.__init__)


def test_uml::templateparametersubstitution_constructor_args():
    sig = inspect.signature(uml::TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml::templatesignature_is_not_abstract():
    assert not inspect.isabstract(uml::TemplateSignature)


def test_uml::templatesignature_constructor_exists():
    assert callable(uml::TemplateSignature.__init__)


def test_uml::templatesignature_constructor_args():
    sig = inspect.signature(uml::TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml::templatebinding_is_not_abstract():
    assert not inspect.isabstract(uml::TemplateBinding)


def test_uml::templatebinding_constructor_exists():
    assert callable(uml::TemplateBinding.__init__)


def test_uml::templatebinding_constructor_args():
    sig = inspect.signature(uml::TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_uml::templateableelement_is_not_abstract():
    assert not inspect.isabstract(uml::TemplateableElement)


def test_uml::templateableelement_constructor_exists():
    assert callable(uml::TemplateableElement.__init__)


def test_uml::templateableelement_constructor_args():
    sig = inspect.signature(uml::TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::property_is_not_abstract():
    assert not inspect.isabstract(uml::Property)


def test_uml::property_constructor_exists():
    assert callable(uml::Property.__init__)


def test_uml::property_constructor_args():
    sig = inspect.signature(uml::Property.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_uml::property_has_default():
    assert hasattr(uml::Property, "default")
    descriptor = None
    for klass in uml::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml::property_has_aggregation():
    assert hasattr(uml::Property, "aggregation")
    descriptor = None
    for klass in uml::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_uml::property_has_isDerived():
    assert hasattr(uml::Property, "isDerived")
    descriptor = None
    for klass in uml::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_uml::property_has_isDerivedUnion():
    assert hasattr(uml::Property, "isDerivedUnion")
    descriptor = None
    for klass in uml::Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_uml::property_has_isComposite():
    assert hasattr(uml::Property, "isComposite")
    descriptor = None
    for klass in uml::Property.__mro__:
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



def test_uml::signal_is_not_abstract():
    assert not inspect.isabstract(uml::Signal)


def test_uml::signal_constructor_exists():
    assert callable(uml::Signal.__init__)


def test_uml::signal_constructor_args():
    sig = inspect.signature(uml::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::StructuredClassifier)


def test_uml::structuredclassifier_constructor_exists():
    assert callable(uml::StructuredClassifier.__init__)


def test_uml::structuredclassifier_constructor_args():
    sig = inspect.signature(uml::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::BehavioredClassifier)


def test_uml::behavioredclassifier_constructor_exists():
    assert callable(uml::BehavioredClassifier.__init__)


def test_uml::behavioredclassifier_constructor_args():
    sig = inspect.signature(uml::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::interface_is_not_abstract():
    assert not inspect.isabstract(uml::Interface)


def test_uml::interface_constructor_exists():
    assert callable(uml::Interface.__init__)


def test_uml::interface_constructor_args():
    sig = inspect.signature(uml::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml::datatype_is_not_abstract():
    assert not inspect.isabstract(uml::DataType)


def test_uml::datatype_constructor_exists():
    assert callable(uml::DataType.__init__)


def test_uml::datatype_constructor_args():
    sig = inspect.signature(uml::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml::informationitem_is_not_abstract():
    assert not inspect.isabstract(uml::InformationItem)


def test_uml::informationitem_constructor_exists():
    assert callable(uml::InformationItem.__init__)


def test_uml::informationitem_constructor_args():
    sig = inspect.signature(uml::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml::artifact_is_not_abstract():
    assert not inspect.isabstract(uml::Artifact)


def test_uml::artifact_constructor_exists():
    assert callable(uml::Artifact.__init__)


def test_uml::artifact_constructor_args():
    sig = inspect.signature(uml::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_uml::artifact_has_fileName():
    assert hasattr(uml::Artifact, "fileName")
    descriptor = None
    for klass in uml::Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml::StructuralFeature)


def test_uml::structuralfeature_constructor_exists():
    assert callable(uml::StructuralFeature.__init__)


def test_uml::structuralfeature_constructor_args():
    sig = inspect.signature(uml::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml::structuralfeature_has_isReadOnly():
    assert hasattr(uml::StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in uml::StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_uml::objectnode_is_not_abstract():
    assert not inspect.isabstract(uml::ObjectNode)


def test_uml::objectnode_constructor_exists():
    assert callable(uml::ObjectNode.__init__)


def test_uml::objectnode_constructor_args():
    sig = inspect.signature(uml::ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"

def test_uml::objectnode_has_ordering():
    assert hasattr(uml::ObjectNode, "ordering")
    descriptor = None
    for klass in uml::ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_uml::objectnode_has_isControlType():
    assert hasattr(uml::ObjectNode, "isControlType")
    descriptor = None
    for klass in uml::ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)



def test_uml::generalization_is_not_abstract():
    assert not inspect.isabstract(uml::Generalization)


def test_uml::generalization_constructor_exists():
    assert callable(uml::Generalization.__init__)


def test_uml::generalization_constructor_args():
    sig = inspect.signature(uml::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_uml::generalization_has_isSubstitutable():
    assert hasattr(uml::Generalization, "isSubstitutable")
    descriptor = None
    for klass in uml::Generalization.__mro__:
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



def test_uml::feature_is_not_abstract():
    assert not inspect.isabstract(uml::Feature)


def test_uml::feature_constructor_exists():
    assert callable(uml::Feature.__init__)


def test_uml::feature_constructor_args():
    sig = inspect.signature(uml::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml::feature_has_isStatic():
    assert hasattr(uml::Feature, "isStatic")
    descriptor = None
    for klass in uml::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_uml::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml::ExtensionPoint)


def test_uml::extensionpoint_constructor_exists():
    assert callable(uml::ExtensionPoint.__init__)


def test_uml::extensionpoint_constructor_args():
    sig = inspect.signature(uml::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml::activityedge_is_not_abstract():
    assert not inspect.isabstract(uml::ActivityEdge)


def test_uml::activityedge_constructor_exists():
    assert callable(uml::ActivityEdge.__init__)


def test_uml::activityedge_constructor_args():
    sig = inspect.signature(uml::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml::redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml::RedefinableTemplateSignature)


def test_uml::redefinabletemplatesignature_constructor_exists():
    assert callable(uml::RedefinableTemplateSignature.__init__)


def test_uml::redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(uml::RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml::activitynode_is_not_abstract():
    assert not inspect.isabstract(uml::ActivityNode)


def test_uml::activitynode_constructor_exists():
    assert callable(uml::ActivityNode.__init__)


def test_uml::activitynode_constructor_args():
    sig = inspect.signature(uml::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::packageimport_is_not_abstract():
    assert not inspect.isabstract(uml::PackageImport)


def test_uml::packageimport_constructor_exists():
    assert callable(uml::PackageImport.__init__)


def test_uml::packageimport_constructor_args():
    sig = inspect.signature(uml::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml::packageimport_has_visibility():
    assert hasattr(uml::PackageImport, "visibility")
    descriptor = None
    for klass in uml::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml::elementimport_is_not_abstract():
    assert not inspect.isabstract(uml::ElementImport)


def test_uml::elementimport_constructor_exists():
    assert callable(uml::ElementImport.__init__)


def test_uml::elementimport_constructor_args():
    sig = inspect.signature(uml::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_uml::elementimport_has_visibility():
    assert hasattr(uml::ElementImport, "visibility")
    descriptor = None
    for klass in uml::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml::elementimport_has_alias():
    assert hasattr(uml::ElementImport, "alias")
    descriptor = None
    for klass in uml::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_uml::relationship_is_not_abstract():
    assert not inspect.isabstract(uml::Relationship)


def test_uml::relationship_constructor_exists():
    assert callable(uml::Relationship.__init__)


def test_uml::relationship_constructor_args():
    sig = inspect.signature(uml::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml::namedelement_is_not_abstract():
    assert not inspect.isabstract(uml::NamedElement)


def test_uml::namedelement_constructor_exists():
    assert callable(uml::NamedElement.__init__)


def test_uml::namedelement_constructor_args():
    sig = inspect.signature(uml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml::namedelement_has_name():
    assert hasattr(uml::NamedElement, "name")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uml::namedelement_has_qualifiedName():
    assert hasattr(uml::NamedElement, "qualifiedName")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_uml::namedelement_has_visibility():
    assert hasattr(uml::NamedElement, "visibility")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::connectableelement_is_not_abstract():
    assert not inspect.isabstract(uml::ConnectableElement)


def test_uml::connectableelement_constructor_exists():
    assert callable(uml::ConnectableElement.__init__)


def test_uml::connectableelement_constructor_args():
    sig = inspect.signature(uml::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(uml::InteractionFragment)


def test_uml::interactionfragment_constructor_exists():
    assert callable(uml::InteractionFragment.__init__)


def test_uml::interactionfragment_constructor_args():
    sig = inspect.signature(uml::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml::messageend_is_not_abstract():
    assert not inspect.isabstract(uml::MessageEnd)


def test_uml::messageend_constructor_exists():
    assert callable(uml::MessageEnd.__init__)


def test_uml::messageend_constructor_args():
    sig = inspect.signature(uml::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml::collaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml::CollaborationUse)


def test_uml::collaborationuse_constructor_exists():
    assert callable(uml::CollaborationUse.__init__)


def test_uml::collaborationuse_constructor_args():
    sig = inspect.signature(uml::CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_uml::generalordering_is_not_abstract():
    assert not inspect.isabstract(uml::GeneralOrdering)


def test_uml::generalordering_constructor_exists():
    assert callable(uml::GeneralOrdering.__init__)


def test_uml::generalordering_constructor_args():
    sig = inspect.signature(uml::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml::extend_is_not_abstract():
    assert not inspect.isabstract(uml::Extend)


def test_uml::extend_constructor_exists():
    assert callable(uml::Extend.__init__)


def test_uml::extend_constructor_args():
    sig = inspect.signature(uml::Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml::typedelement_is_not_abstract():
    assert not inspect.isabstract(uml::TypedElement)


def test_uml::typedelement_constructor_exists():
    assert callable(uml::TypedElement.__init__)


def test_uml::typedelement_constructor_args():
    sig = inspect.signature(uml::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::include_is_not_abstract():
    assert not inspect.isabstract(uml::Include)


def test_uml::include_constructor_exists():
    assert callable(uml::Include.__init__)


def test_uml::include_constructor_args():
    sig = inspect.signature(uml::Include.__init__)
    params = list(sig.parameters.keys())



def test_uml::vertex_is_not_abstract():
    assert not inspect.isabstract(uml::Vertex)


def test_uml::vertex_constructor_exists():
    assert callable(uml::Vertex.__init__)


def test_uml::vertex_constructor_args():
    sig = inspect.signature(uml::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml::message_is_not_abstract():
    assert not inspect.isabstract(uml::Message)


def test_uml::message_constructor_exists():
    assert callable(uml::Message.__init__)


def test_uml::message_constructor_args():
    sig = inspect.signature(uml::Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageSort" in params, "Missing parameter 'messageSort'"
    assert "messageKind" in params, "Missing parameter 'messageKind'"

def test_uml::message_has_messageSort():
    assert hasattr(uml::Message, "messageSort")
    descriptor = None
    for klass in uml::Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)

def test_uml::message_has_messageKind():
    assert hasattr(uml::Message, "messageKind")
    descriptor = None
    for klass in uml::Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)



def test_uml::deployedartifact_is_not_abstract():
    assert not inspect.isabstract(uml::DeployedArtifact)


def test_uml::deployedartifact_constructor_exists():
    assert callable(uml::DeployedArtifact.__init__)


def test_uml::deployedartifact_constructor_args():
    sig = inspect.signature(uml::DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml::deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(uml::DeploymentTarget)


def test_uml::deploymenttarget_constructor_exists():
    assert callable(uml::DeploymentTarget.__init__)


def test_uml::deploymenttarget_constructor_args():
    sig = inspect.signature(uml::DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml::trigger_is_not_abstract():
    assert not inspect.isabstract(uml::Trigger)


def test_uml::trigger_constructor_exists():
    assert callable(uml::Trigger.__init__)


def test_uml::trigger_constructor_args():
    sig = inspect.signature(uml::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml::namespace_is_not_abstract():
    assert not inspect.isabstract(uml::Namespace)


def test_uml::namespace_constructor_exists():
    assert callable(uml::Namespace.__init__)


def test_uml::namespace_constructor_args():
    sig = inspect.signature(uml::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml::RedefinableElement)


def test_uml::redefinableelement_constructor_exists():
    assert callable(uml::RedefinableElement.__init__)


def test_uml::redefinableelement_constructor_args():
    sig = inspect.signature(uml::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_uml::redefinableelement_has_isLeaf():
    assert hasattr(uml::RedefinableElement, "isLeaf")
    descriptor = None
    for klass in uml::RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_uml::activitypartition_is_not_abstract():
    assert not inspect.isabstract(uml::ActivityPartition)


def test_uml::activitypartition_constructor_exists():
    assert callable(uml::ActivityPartition.__init__)


def test_uml::activitypartition_constructor_args():
    sig = inspect.signature(uml::ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "isDimension" in params, "Missing parameter 'isDimension'"

def test_uml::activitypartition_has_isExternal():
    assert hasattr(uml::ActivityPartition, "isExternal")
    descriptor = None
    for klass in uml::ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_uml::activitypartition_has_isDimension():
    assert hasattr(uml::ActivityPartition, "isDimension")
    descriptor = None
    for klass in uml::ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)



def test_uml::parameterset_is_not_abstract():
    assert not inspect.isabstract(uml::ParameterSet)


def test_uml::parameterset_constructor_exists():
    assert callable(uml::ParameterSet.__init__)


def test_uml::parameterset_constructor_args():
    sig = inspect.signature(uml::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml::lifeline_is_not_abstract():
    assert not inspect.isabstract(uml::Lifeline)


def test_uml::lifeline_constructor_exists():
    assert callable(uml::Lifeline.__init__)


def test_uml::lifeline_constructor_args():
    sig = inspect.signature(uml::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml::profileapplication_is_not_abstract():
    assert not inspect.isabstract(uml::ProfileApplication)


def test_uml::profileapplication_constructor_exists():
    assert callable(uml::ProfileApplication.__init__)


def test_uml::profileapplication_constructor_args():
    sig = inspect.signature(uml::ProfileApplication.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_uml::profileapplication_has_isStrict():
    assert hasattr(uml::ProfileApplication, "isStrict")
    descriptor = None
    for klass in uml::ProfileApplication.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_uml::packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml::PackageableElement)


def test_uml::packageableelement_constructor_exists():
    assert callable(uml::PackageableElement.__init__)


def test_uml::packageableelement_constructor_args():
    sig = inspect.signature(uml::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::packagemerge_is_not_abstract():
    assert not inspect.isabstract(uml::PackageMerge)


def test_uml::packagemerge_constructor_exists():
    assert callable(uml::PackageMerge.__init__)


def test_uml::packagemerge_constructor_args():
    sig = inspect.signature(uml::PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::stringexpression_is_not_abstract():
    assert not inspect.isabstract(uml::StringExpression)


def test_uml::stringexpression_constructor_exists():
    assert callable(uml::StringExpression.__init__)


def test_uml::stringexpression_constructor_args():
    sig = inspect.signature(uml::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml::operation_is_not_abstract():
    assert not inspect.isabstract(uml::Operation)


def test_uml::operation_constructor_exists():
    assert callable(uml::Operation.__init__)


def test_uml::operation_constructor_args():
    sig = inspect.signature(uml::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_uml::operation_has_isUnique():
    assert hasattr(uml::Operation, "isUnique")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_isQuery():
    assert hasattr(uml::Operation, "isQuery")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_upper():
    assert hasattr(uml::Operation, "upper")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_isOrdered():
    assert hasattr(uml::Operation, "isOrdered")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_lower():
    assert hasattr(uml::Operation, "lower")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::type_is_not_abstract():
    assert not inspect.isabstract(uml::Type)


def test_uml::type_constructor_exists():
    assert callable(uml::Type.__init__)


def test_uml::type_constructor_args():
    sig = inspect.signature(uml::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml::dependency_is_not_abstract():
    assert not inspect.isabstract(uml::Dependency)


def test_uml::dependency_constructor_exists():
    assert callable(uml::Dependency.__init__)


def test_uml::dependency_constructor_args():
    sig = inspect.signature(uml::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml::valuespecification_is_not_abstract():
    assert not inspect.isabstract(uml::ValueSpecification)


def test_uml::valuespecification_constructor_exists():
    assert callable(uml::ValueSpecification.__init__)


def test_uml::valuespecification_constructor_args():
    sig = inspect.signature(uml::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::instancespecification_is_not_abstract():
    assert not inspect.isabstract(uml::InstanceSpecification)


def test_uml::instancespecification_constructor_exists():
    assert callable(uml::InstanceSpecification.__init__)


def test_uml::instancespecification_constructor_args():
    sig = inspect.signature(uml::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::generalizationset_is_not_abstract():
    assert not inspect.isabstract(uml::GeneralizationSet)


def test_uml::generalizationset_constructor_exists():
    assert callable(uml::GeneralizationSet.__init__)


def test_uml::generalizationset_constructor_args():
    sig = inspect.signature(uml::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"

def test_uml::generalizationset_has_isCovering():
    assert hasattr(uml::GeneralizationSet, "isCovering")
    descriptor = None
    for klass in uml::GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)

def test_uml::generalizationset_has_isDisjoint():
    assert hasattr(uml::GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in uml::GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)



def test_uml::observation_is_not_abstract():
    assert not inspect.isabstract(uml::Observation)


def test_uml::observation_constructor_exists():
    assert callable(uml::Observation.__init__)


def test_uml::observation_constructor_args():
    sig = inspect.signature(uml::Observation.__init__)
    params = list(sig.parameters.keys())



def test_uml::informationflow_is_not_abstract():
    assert not inspect.isabstract(uml::InformationFlow)


def test_uml::informationflow_constructor_exists():
    assert callable(uml::InformationFlow.__init__)


def test_uml::informationflow_constructor_args():
    sig = inspect.signature(uml::InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml::event_is_not_abstract():
    assert not inspect.isabstract(uml::Event)


def test_uml::event_constructor_exists():
    assert callable(uml::Event.__init__)


def test_uml::event_constructor_args():
    sig = inspect.signature(uml::Event.__init__)
    params = list(sig.parameters.keys())



def test_uml::constraint_is_not_abstract():
    assert not inspect.isabstract(uml::Constraint)


def test_uml::constraint_constructor_exists():
    assert callable(uml::Constraint.__init__)


def test_uml::constraint_constructor_args():
    sig = inspect.signature(uml::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml::classifier_is_not_abstract():
    assert not inspect.isabstract(uml::Classifier)


def test_uml::classifier_constructor_exists():
    assert callable(uml::Classifier.__init__)


def test_uml::classifier_constructor_args():
    sig = inspect.signature(uml::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml::classifier_has_isAbstract():
    assert hasattr(uml::Classifier, "isAbstract")
    descriptor = None
    for klass in uml::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml::region_is_not_abstract():
    assert not inspect.isabstract(uml::Region)


def test_uml::region_constructor_exists():
    assert callable(uml::Region.__init__)


def test_uml::region_constructor_args():
    sig = inspect.signature(uml::Region.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml::BehavioralFeature)


def test_uml::behavioralfeature_constructor_exists():
    assert callable(uml::BehavioralFeature.__init__)


def test_uml::behavioralfeature_constructor_args():
    sig = inspect.signature(uml::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml::behavioralfeature_has_concurrency():
    assert hasattr(uml::BehavioralFeature, "concurrency")
    descriptor = None
    for klass in uml::BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_uml::behavioralfeature_has_isAbstract():
    assert hasattr(uml::BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in uml::BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml::state_is_not_abstract():
    assert not inspect.isabstract(uml::State)


def test_uml::state_constructor_exists():
    assert callable(uml::State.__init__)


def test_uml::state_constructor_args():
    sig = inspect.signature(uml::State.__init__)
    params = list(sig.parameters.keys())
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_uml::state_has_isSubmachineState():
    assert hasattr(uml::State, "isSubmachineState")
    descriptor = None
    for klass in uml::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_uml::state_has_isSimple():
    assert hasattr(uml::State, "isSimple")
    descriptor = None
    for klass in uml::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_uml::state_has_isOrthogonal():
    assert hasattr(uml::State, "isOrthogonal")
    descriptor = None
    for klass in uml::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_uml::state_has_isComposite():
    assert hasattr(uml::State, "isComposite")
    descriptor = None
    for klass in uml::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_uml::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml::StructuredActivityNode)


def test_uml::structuredactivitynode_constructor_exists():
    assert callable(uml::StructuredActivityNode.__init__)


def test_uml::structuredactivitynode_constructor_args():
    sig = inspect.signature(uml::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_uml::structuredactivitynode_has_mustIsolate():
    assert hasattr(uml::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in uml::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_uml::transition_is_not_abstract():
    assert not inspect.isabstract(uml::Transition)


def test_uml::transition_constructor_exists():
    assert callable(uml::Transition.__init__)


def test_uml::transition_constructor_args():
    sig = inspect.signature(uml::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml::transition_has_kind():
    assert hasattr(uml::Transition, "kind")
    descriptor = None
    for klass in uml::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(uml::InteractionOperand)


def test_uml::interactionoperand_constructor_exists():
    assert callable(uml::InteractionOperand.__init__)


def test_uml::interactionoperand_constructor_args():
    sig = inspect.signature(uml::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml::package_is_not_abstract():
    assert not inspect.isabstract(uml::Package)


def test_uml::package_constructor_exists():
    assert callable(uml::Package.__init__)


def test_uml::package_constructor_args():
    sig = inspect.signature(uml::Package.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml::association_is_not_abstract():
    assert not inspect.isabstract(uml::Association)


def test_uml::association_constructor_exists():
    assert callable(uml::Association.__init__)


def test_uml::association_constructor_args():
    sig = inspect.signature(uml::Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml::association_has_isDerived():
    assert hasattr(uml::Association, "isDerived")
    descriptor = None
    for klass in uml::Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_uml::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml::DirectedRelationship)


def test_uml::directedrelationship_constructor_exists():
    assert callable(uml::DirectedRelationship.__init__)


def test_uml::directedrelationship_constructor_args():
    sig = inspect.signature(uml::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "unordered",
        "FIFO",
        "LIFO",
        "ordered",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

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

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "delete",
        "update",
        "read",
        "create",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "unknown",
        "lost",
        "complete",
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
        "composite",
        "none",
        "shared",
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
        "external",
        "internal",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "sequential",
        "guarded",
        "concurrent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "protected",
        "public",
        "package",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_connectorkind_exists():
    # Check that the Enumeration exists
    assert ConnectorKind is not None

def test_connectorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectorKind]
    expected_literals = [
        "assembly",
        "delegation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectorKind"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "inout",
        "out",
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
        "asynchSignal",
        "deleteMessage",
        "synchCall",
        "asynchCall",
        "reply",
        "createMessage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "break_",
        "ignore",
        "strict",
        "alt",
        "assert_",
        "critical",
        "opt",
        "seq",
        "neg",
        "loop",
        "par",
        "consider",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "shallowHistory",
        "choice",
        "initial",
        "deepHistory",
        "exitPoint",
        "terminate",
        "junction",
        "entryPoint",
        "join",
        "fork",
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
State_strategy = st.builds(
    State,
)
uml::FinalState_strategy = st.builds(
    uml::FinalState,
)
Observation_strategy = st.builds(
    Observation,
)
uml::DurationObservation_strategy = st.builds(
    uml::DurationObservation,
    firstEvent=
        safe_text
)
uml::TimeObservation_strategy = st.builds(
    uml::TimeObservation,
    firstEvent=
        safe_text
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
uml::DurationConstraint_strategy = st.builds(
    uml::DurationConstraint,
    firstEvent=
        safe_text
)
uml::TimeConstraint_strategy = st.builds(
    uml::TimeConstraint,
    firstEvent=
        safe_text
)
Interval_strategy = st.builds(
    Interval,
)
uml::TimeInterval_strategy = st.builds(
    uml::TimeInterval,
)
uml::DurationInterval_strategy = st.builds(
    uml::DurationInterval,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
uml::DestroyLinkAction_strategy = st.builds(
    uml::DestroyLinkAction,
)
uml::CreateLinkAction_strategy = st.builds(
    uml::CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
uml::LinkEndDestructionData_strategy = st.builds(
    uml::LinkEndDestructionData,
    isDestroyDuplicates=
        safe_text
)
uml::LinkEndCreationData_strategy = st.builds(
    uml::LinkEndCreationData,
    isReplaceAll=
        safe_text
)
LinkAction_strategy = st.builds(
    LinkAction,
)
uml::WriteLinkAction_strategy = st.builds(
    uml::WriteLinkAction,
)
uml::ReadLinkAction_strategy = st.builds(
    uml::ReadLinkAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
uml::WriteStructuralFeatureAction_strategy = st.builds(
    uml::WriteStructuralFeatureAction,
)
uml::ClearStructuralFeatureAction_strategy = st.builds(
    uml::ClearStructuralFeatureAction,
)
uml::ReadStructuralFeatureAction_strategy = st.builds(
    uml::ReadStructuralFeatureAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
uml::AddStructuralFeatureValueAction_strategy = st.builds(
    uml::AddStructuralFeatureValueAction,
    isReplaceAll=
        safe_text
)
uml::RemoveStructuralFeatureValueAction_strategy = st.builds(
    uml::RemoveStructuralFeatureValueAction,
    isRemoveDuplicates=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
uml::ExecutionEnvironment_strategy = st.builds(
    uml::ExecutionEnvironment,
)
uml::Device_strategy = st.builds(
    uml::Device,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
uml::ConsiderIgnoreFragment_strategy = st.builds(
    uml::ConsiderIgnoreFragment,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
uml::ActivityFinalNode_strategy = st.builds(
    uml::ActivityFinalNode,
)
uml::FlowFinalNode_strategy = st.builds(
    uml::FlowFinalNode,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
uml::CallEvent_strategy = st.builds(
    uml::CallEvent,
)
uml::ReceiveSignalEvent_strategy = st.builds(
    uml::ReceiveSignalEvent,
)
uml::SignalEvent_strategy = st.builds(
    uml::SignalEvent,
)
uml::ReceiveOperationEvent_strategy = st.builds(
    uml::ReceiveOperationEvent,
)
uml::AnyReceiveEvent_strategy = st.builds(
    uml::AnyReceiveEvent,
)
uml::SendSignalEvent_strategy = st.builds(
    uml::SendSignalEvent,
)
uml::SendOperationEvent_strategy = st.builds(
    uml::SendOperationEvent,
)
Event_strategy = st.builds(
    Event,
)
uml::ChangeEvent_strategy = st.builds(
    uml::ChangeEvent,
)
uml::DestructionEvent_strategy = st.builds(
    uml::DestructionEvent,
)
uml::MessageEvent_strategy = st.builds(
    uml::MessageEvent,
)
uml::TimeEvent_strategy = st.builds(
    uml::TimeEvent,
    isRelative=
        safe_text
)
uml::CreationEvent_strategy = st.builds(
    uml::CreationEvent,
)
uml::ExecutionEvent_strategy = st.builds(
    uml::ExecutionEvent,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
uml::BehaviorExecutionSpecification_strategy = st.builds(
    uml::BehaviorExecutionSpecification,
)
uml::ActionExecutionSpecification_strategy = st.builds(
    uml::ActionExecutionSpecification,
)
Constraint_strategy = st.builds(
    Constraint,
)
uml::IntervalConstraint_strategy = st.builds(
    uml::IntervalConstraint,
)
uml::InteractionConstraint_strategy = st.builds(
    uml::InteractionConstraint,
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
uml::ExecutionOccurrenceSpecification_strategy = st.builds(
    uml::ExecutionOccurrenceSpecification,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
uml::MessageOccurrenceSpecification_strategy = st.builds(
    uml::MessageOccurrenceSpecification,
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
uml::PartDecomposition_strategy = st.builds(
    uml::PartDecomposition,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
uml::StateInvariant_strategy = st.builds(
    uml::StateInvariant,
)
uml::OccurrenceSpecification_strategy = st.builds(
    uml::OccurrenceSpecification,
)
uml::Continuation_strategy = st.builds(
    uml::Continuation,
    setting=
        safe_text
)
uml::ExecutionSpecification_strategy = st.builds(
    uml::ExecutionSpecification,
)
uml::InteractionUse_strategy = st.builds(
    uml::InteractionUse,
)
uml::CombinedFragment_strategy = st.builds(
    uml::CombinedFragment,
    interactionOperator=
        safe_text
)
InputPin_strategy = st.builds(
    InputPin,
)
uml::ValuePin_strategy = st.builds(
    uml::ValuePin,
)
uml::Gate_strategy = st.builds(
    uml::Gate,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
uml::SequenceNode_strategy = st.builds(
    uml::SequenceNode,
)
CallAction_strategy = st.builds(
    CallAction,
)
uml::CallBehaviorAction_strategy = st.builds(
    uml::CallBehaviorAction,
)
uml::CallOperationAction_strategy = st.builds(
    uml::CallOperationAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
uml::BroadcastSignalAction_strategy = st.builds(
    uml::BroadcastSignalAction,
)
uml::SendSignalAction_strategy = st.builds(
    uml::SendSignalAction,
)
uml::SendObjectAction_strategy = st.builds(
    uml::SendObjectAction,
)
uml::CallAction_strategy = st.builds(
    uml::CallAction,
    isSynchronous=
        safe_text
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
uml::CentralBufferNode_strategy = st.builds(
    uml::CentralBufferNode,
)
Pin_strategy = st.builds(
    Pin,
)
uml::ActivityParameterNode_strategy = st.builds(
    uml::ActivityParameterNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
uml::MergeNode_strategy = st.builds(
    uml::MergeNode,
)
uml::FinalNode_strategy = st.builds(
    uml::FinalNode,
)
uml::DecisionNode_strategy = st.builds(
    uml::DecisionNode,
)
uml::ForkNode_strategy = st.builds(
    uml::ForkNode,
)
uml::InitialNode_strategy = st.builds(
    uml::InitialNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
uml::ObjectFlow_strategy = st.builds(
    uml::ObjectFlow,
    isMultireceive=
        safe_text,
    isMulticast=
        safe_text
)
uml::ControlFlow_strategy = st.builds(
    uml::ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
uml::InterruptibleActivityRegion_strategy = st.builds(
    uml::InterruptibleActivityRegion,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
uml::ControlNode_strategy = st.builds(
    uml::ControlNode,
)
uml::ExecutableNode_strategy = st.builds(
    uml::ExecutableNode,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
uml::Action_strategy = st.builds(
    uml::Action,
)
uml::OutputPin_strategy = st.builds(
    uml::OutputPin,
)
uml::InputPin_strategy = st.builds(
    uml::InputPin,
)
Action_strategy = st.builds(
    Action,
)
uml::InvocationAction_strategy = st.builds(
    uml::InvocationAction,
)
uml::ValueSpecificationAction_strategy = st.builds(
    uml::ValueSpecificationAction,
)
uml::ReadSelfAction_strategy = st.builds(
    uml::ReadSelfAction,
)
uml::StructuralFeatureAction_strategy = st.builds(
    uml::StructuralFeatureAction,
)
uml::DestroyObjectAction_strategy = st.builds(
    uml::DestroyObjectAction,
    isDestroyOwnedObjects=
        safe_text,
    isDestroyLinks=
        safe_text
)
uml::CreateObjectAction_strategy = st.builds(
    uml::CreateObjectAction,
)
uml::LinkAction_strategy = st.builds(
    uml::LinkAction,
)
uml::TestIdentityAction_strategy = st.builds(
    uml::TestIdentityAction,
)
uml::ClearAssociationAction_strategy = st.builds(
    uml::ClearAssociationAction,
)
uml::OpaqueAction_strategy = st.builds(
    uml::OpaqueAction,
    language=
        safe_text,
    body=
        safe_text
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
uml::FunctionBehavior_strategy = st.builds(
    uml::FunctionBehavior,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
uml::LiteralUnlimitedNatural_strategy = st.builds(
    uml::LiteralUnlimitedNatural,
    value=
        safe_text
)
uml::LiteralNull_strategy = st.builds(
    uml::LiteralNull,
)
uml::LiteralString_strategy = st.builds(
    uml::LiteralString,
    value=
        safe_text
)
uml::LiteralBoolean_strategy = st.builds(
    uml::LiteralBoolean,
    value=
        safe_text
)
uml::LiteralInteger_strategy = st.builds(
    uml::LiteralInteger,
    value=
        safe_text
)
uml::EnumerationLiteral_strategy = st.builds(
    uml::EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
uml::PrimitiveType_strategy = st.builds(
    uml::PrimitiveType,
)
uml::Enumeration_strategy = st.builds(
    uml::Enumeration,
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
uml::ClassifierTemplateParameter_strategy = st.builds(
    uml::ClassifierTemplateParameter,
    allowSubstitutable=
        safe_text
)
uml::ConnectableElementTemplateParameter_strategy = st.builds(
    uml::ConnectableElementTemplateParameter,
)
uml::OperationTemplateParameter_strategy = st.builds(
    uml::OperationTemplateParameter,
)
Association_strategy = st.builds(
    Association,
)
uml::CommunicationPath_strategy = st.builds(
    uml::CommunicationPath,
)
Package_strategy = st.builds(
    Package,
)
uml::Model_strategy = st.builds(
    uml::Model,
    viewpoint=
        safe_text
)
uml::Profile_strategy = st.builds(
    uml::Profile,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
uml::EncapsulatedClassifier_strategy = st.builds(
    uml::EncapsulatedClassifier,
)
Vertex_strategy = st.builds(
    Vertex,
)
Property_strategy = st.builds(
    Property,
)
uml::ExtensionEnd_strategy = st.builds(
    uml::ExtensionEnd,
)
uml::Port_strategy = st.builds(
    uml::Port,
    isService=
        safe_text,
    isBehavior=
        safe_text
)
uml::ConnectionPointReference_strategy = st.builds(
    uml::ConnectionPointReference,
)
uml::Pseudostate_strategy = st.builds(
    uml::Pseudostate,
    kind=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
uml::Interaction_strategy = st.builds(
    uml::Interaction,
)
uml::OpaqueBehavior_strategy = st.builds(
    uml::OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)
uml::Activity_strategy = st.builds(
    uml::Activity,
    isReadOnly=
        safe_text,
    isSingleExecution=
        safe_text
)
uml::StateMachine_strategy = st.builds(
    uml::StateMachine,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
uml::ProtocolStateMachine_strategy = st.builds(
    uml::ProtocolStateMachine,
)
Class_strategy = st.builds(
    Class,
)
uml::Stereotype_strategy = st.builds(
    uml::Stereotype,
)
uml::Component_strategy = st.builds(
    uml::Component,
    isIndirectlyInstantiated=
        safe_text
)
uml::Extension_strategy = st.builds(
    uml::Extension,
    isRequired=
        safe_text
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
uml::Actor_strategy = st.builds(
    uml::Actor,
)
uml::Collaboration_strategy = st.builds(
    uml::Collaboration,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
uml::Reception_strategy = st.builds(
    uml::Reception,
)
Feature_strategy = st.builds(
    Feature,
)
uml::Connector_strategy = st.builds(
    uml::Connector,
    kind=
        safe_text
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
Artifact_strategy = st.builds(
    Artifact,
)
uml::DeploymentSpecification_strategy = st.builds(
    uml::DeploymentSpecification,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text
)
uml::Class_strategy = st.builds(
    uml::Class,
    isActive=
        safe_text
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
uml::Node_strategy = st.builds(
    uml::Node,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
Realization_strategy = st.builds(
    Realization,
)
uml::InterfaceRealization_strategy = st.builds(
    uml::InterfaceRealization,
)
uml::ComponentRealization_strategy = st.builds(
    uml::ComponentRealization,
)
uml::AssociationClass_strategy = st.builds(
    uml::AssociationClass,
)
Transition_strategy = st.builds(
    Transition,
)
uml::ProtocolTransition_strategy = st.builds(
    uml::ProtocolTransition,
)
uml::ExpansionRegion_strategy = st.builds(
    uml::ExpansionRegion,
    mode=
        safe_text
)
uml::ExpansionNode_strategy = st.builds(
    uml::ExpansionNode,
)
uml::LoopNode_strategy = st.builds(
    uml::LoopNode,
    isTestedFirst=
        safe_text
)
uml::ConditionalNode_strategy = st.builds(
    uml::ConditionalNode,
    isAssured=
        safe_text,
    isDeterminate=
        safe_text
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
uml::DataStoreNode_strategy = st.builds(
    uml::DataStoreNode,
)
uml::JoinNode_strategy = st.builds(
    uml::JoinNode,
    isCombineDuplicate=
        safe_text
)
uml::StartObjectBehaviorAction_strategy = st.builds(
    uml::StartObjectBehaviorAction,
)
uml::ReduceAction_strategy = st.builds(
    uml::ReduceAction,
    isOrdered=
        safe_text
)
uml::UnmarshallAction_strategy = st.builds(
    uml::UnmarshallAction,
)
uml::ReplyAction_strategy = st.builds(
    uml::ReplyAction,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
uml::AcceptCallAction_strategy = st.builds(
    uml::AcceptCallAction,
)
uml::AcceptEventAction_strategy = st.builds(
    uml::AcceptEventAction,
    isUnmarshall=
        safe_text
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
uml::CreateLinkObjectAction_strategy = st.builds(
    uml::CreateLinkObjectAction,
)
uml::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml::ReadLinkObjectEndQualifierAction,
)
uml::StartClassifierBehaviorAction_strategy = st.builds(
    uml::StartClassifierBehaviorAction,
)
uml::ReadIsClassifiedObjectAction_strategy = st.builds(
    uml::ReadIsClassifiedObjectAction,
    isDirect=
        safe_text
)
uml::ReclassifyObjectAction_strategy = st.builds(
    uml::ReclassifyObjectAction,
    isReplaceAll=
        safe_text
)
uml::ReadLinkObjectEndAction_strategy = st.builds(
    uml::ReadLinkObjectEndAction,
)
uml::ReadExtentAction_strategy = st.builds(
    uml::ReadExtentAction,
)
uml::ActionInputPin_strategy = st.builds(
    uml::ActionInputPin,
)
uml::RaiseExceptionAction_strategy = st.builds(
    uml::RaiseExceptionAction,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
uml::RemoveVariableValueAction_strategy = st.builds(
    uml::RemoveVariableValueAction,
    isRemoveDuplicates=
        safe_text
)
uml::AddVariableValueAction_strategy = st.builds(
    uml::AddVariableValueAction,
    isReplaceAll=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
uml::ProtocolConformance_strategy = st.builds(
    uml::ProtocolConformance,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
uml::ClearVariableAction_strategy = st.builds(
    uml::ClearVariableAction,
)
uml::WriteVariableAction_strategy = st.builds(
    uml::WriteVariableAction,
)
Element_strategy = st.builds(
    Element,
)
uml::QualifierValue_strategy = st.builds(
    uml::QualifierValue,
)
uml::LinkEndData_strategy = st.builds(
    uml::LinkEndData,
)
uml::ActivityGroup_strategy = st.builds(
    uml::ActivityGroup,
)
uml::Slot_strategy = st.builds(
    uml::Slot,
)
uml::Image_strategy = st.builds(
    uml::Image,
    location=
        safe_text,
    content=
        safe_text,
    format=
        safe_text
)
uml::MultiplicityElement_strategy = st.builds(
    uml::MultiplicityElement,
    isUnique=
        safe_text,
    lower=
        safe_text,
    upper=
        safe_text,
    isOrdered=
        safe_text
)
uml::Clause_strategy = st.builds(
    uml::Clause,
)
uml::ExceptionHandler_strategy = st.builds(
    uml::ExceptionHandler,
)
uml::ReadVariableAction_strategy = st.builds(
    uml::ReadVariableAction,
)
uml::Comment_strategy = st.builds(
    uml::Comment,
    body=
        safe_text
)
uml::VariableAction_strategy = st.builds(
    uml::VariableAction,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
uml::Element_strategy = st.builds(
    uml::Element,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
uml::Pin_strategy = st.builds(
    uml::Pin,
    isControl=
        safe_text
)
uml::ConnectorEnd_strategy = st.builds(
    uml::ConnectorEnd,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
uml::Variable_strategy = st.builds(
    uml::Variable,
)
uml::Behavior_strategy = st.builds(
    uml::Behavior,
    isReentrant=
        safe_text
)
uml::Parameter_strategy = st.builds(
    uml::Parameter,
    effect=
        safe_text,
    isException=
        safe_text,
    default=
        safe_text,
    direction=
        safe_text,
    isStream=
        safe_text
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
uml::LiteralSpecification_strategy = st.builds(
    uml::LiteralSpecification,
)
uml::TimeExpression_strategy = st.builds(
    uml::TimeExpression,
)
uml::Duration_strategy = st.builds(
    uml::Duration,
)
uml::Interval_strategy = st.builds(
    uml::Interval,
)
uml::InstanceValue_strategy = st.builds(
    uml::InstanceValue,
)
uml::Expression_strategy = st.builds(
    uml::Expression,
    symbol=
        safe_text
)
uml::OpaqueExpression_strategy = st.builds(
    uml::OpaqueExpression,
    language=
        safe_text,
    body=
        safe_text
)
Dependency_strategy = st.builds(
    Dependency,
)
uml::Deployment_strategy = st.builds(
    uml::Deployment,
)
uml::Usage_strategy = st.builds(
    uml::Usage,
)
uml::Abstraction_strategy = st.builds(
    uml::Abstraction,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
uml::Manifestation_strategy = st.builds(
    uml::Manifestation,
)
uml::Realization_strategy = st.builds(
    uml::Realization,
)
uml::ParameterableElement_strategy = st.builds(
    uml::ParameterableElement,
)
uml::UseCase_strategy = st.builds(
    uml::UseCase,
)
uml::Substitution_strategy = st.builds(
    uml::Substitution,
)
uml::TemplateParameter_strategy = st.builds(
    uml::TemplateParameter,
)
uml::TemplateParameterSubstitution_strategy = st.builds(
    uml::TemplateParameterSubstitution,
)
uml::TemplateSignature_strategy = st.builds(
    uml::TemplateSignature,
)
uml::TemplateBinding_strategy = st.builds(
    uml::TemplateBinding,
)
uml::TemplateableElement_strategy = st.builds(
    uml::TemplateableElement,
)
uml::Property_strategy = st.builds(
    uml::Property,
    default=
        safe_text,
    aggregation=
        safe_text,
    isDerived=
        safe_text,
    isDerivedUnion=
        safe_text,
    isComposite=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uml::Signal_strategy = st.builds(
    uml::Signal,
)
uml::StructuredClassifier_strategy = st.builds(
    uml::StructuredClassifier,
)
uml::BehavioredClassifier_strategy = st.builds(
    uml::BehavioredClassifier,
)
uml::Interface_strategy = st.builds(
    uml::Interface,
)
uml::DataType_strategy = st.builds(
    uml::DataType,
)
uml::InformationItem_strategy = st.builds(
    uml::InformationItem,
)
uml::Artifact_strategy = st.builds(
    uml::Artifact,
    fileName=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uml::StructuralFeature_strategy = st.builds(
    uml::StructuralFeature,
    isReadOnly=
        safe_text
)
uml::ObjectNode_strategy = st.builds(
    uml::ObjectNode,
    ordering=
        safe_text,
    isControlType=
        safe_text
)
uml::Generalization_strategy = st.builds(
    uml::Generalization,
    isSubstitutable=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
uml::Feature_strategy = st.builds(
    uml::Feature,
    isStatic=
        safe_text
)
uml::ExtensionPoint_strategy = st.builds(
    uml::ExtensionPoint,
)
uml::ActivityEdge_strategy = st.builds(
    uml::ActivityEdge,
)
uml::RedefinableTemplateSignature_strategy = st.builds(
    uml::RedefinableTemplateSignature,
)
uml::ActivityNode_strategy = st.builds(
    uml::ActivityNode,
)
uml::PackageImport_strategy = st.builds(
    uml::PackageImport,
    visibility=
        safe_text
)
uml::ElementImport_strategy = st.builds(
    uml::ElementImport,
    visibility=
        safe_text,
    alias=
        safe_text
)
uml::Relationship_strategy = st.builds(
    uml::Relationship,
)
uml::NamedElement_strategy = st.builds(
    uml::NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text,
    visibility=
        safe_text
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
uml::ConnectableElement_strategy = st.builds(
    uml::ConnectableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml::InteractionFragment_strategy = st.builds(
    uml::InteractionFragment,
)
uml::MessageEnd_strategy = st.builds(
    uml::MessageEnd,
)
uml::CollaborationUse_strategy = st.builds(
    uml::CollaborationUse,
)
uml::GeneralOrdering_strategy = st.builds(
    uml::GeneralOrdering,
)
uml::Extend_strategy = st.builds(
    uml::Extend,
)
uml::TypedElement_strategy = st.builds(
    uml::TypedElement,
)
uml::Include_strategy = st.builds(
    uml::Include,
)
uml::Vertex_strategy = st.builds(
    uml::Vertex,
)
uml::Message_strategy = st.builds(
    uml::Message,
    messageSort=
        safe_text,
    messageKind=
        safe_text
)
uml::DeployedArtifact_strategy = st.builds(
    uml::DeployedArtifact,
)
uml::DeploymentTarget_strategy = st.builds(
    uml::DeploymentTarget,
)
uml::Trigger_strategy = st.builds(
    uml::Trigger,
)
uml::Namespace_strategy = st.builds(
    uml::Namespace,
)
uml::RedefinableElement_strategy = st.builds(
    uml::RedefinableElement,
    isLeaf=
        safe_text
)
uml::ActivityPartition_strategy = st.builds(
    uml::ActivityPartition,
    isExternal=
        safe_text,
    isDimension=
        safe_text
)
uml::ParameterSet_strategy = st.builds(
    uml::ParameterSet,
)
uml::Lifeline_strategy = st.builds(
    uml::Lifeline,
)
uml::ProfileApplication_strategy = st.builds(
    uml::ProfileApplication,
    isStrict=
        safe_text
)
uml::PackageableElement_strategy = st.builds(
    uml::PackageableElement,
)
uml::PackageMerge_strategy = st.builds(
    uml::PackageMerge,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
uml::StringExpression_strategy = st.builds(
    uml::StringExpression,
)
uml::Operation_strategy = st.builds(
    uml::Operation,
    isUnique=
        safe_text,
    isQuery=
        safe_text,
    upper=
        safe_text,
    isOrdered=
        safe_text,
    lower=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml::Type_strategy = st.builds(
    uml::Type,
)
uml::Dependency_strategy = st.builds(
    uml::Dependency,
)
uml::ValueSpecification_strategy = st.builds(
    uml::ValueSpecification,
)
uml::InstanceSpecification_strategy = st.builds(
    uml::InstanceSpecification,
)
uml::GeneralizationSet_strategy = st.builds(
    uml::GeneralizationSet,
    isCovering=
        safe_text,
    isDisjoint=
        safe_text
)
uml::Observation_strategy = st.builds(
    uml::Observation,
)
uml::InformationFlow_strategy = st.builds(
    uml::InformationFlow,
)
uml::Event_strategy = st.builds(
    uml::Event,
)
uml::Constraint_strategy = st.builds(
    uml::Constraint,
)
Namespace_strategy = st.builds(
    Namespace,
)
uml::Classifier_strategy = st.builds(
    uml::Classifier,
    isAbstract=
        safe_text
)
uml::Region_strategy = st.builds(
    uml::Region,
)
uml::BehavioralFeature_strategy = st.builds(
    uml::BehavioralFeature,
    concurrency=
        safe_text,
    isAbstract=
        safe_text
)
uml::State_strategy = st.builds(
    uml::State,
    isSubmachineState=
        safe_text,
    isSimple=
        safe_text,
    isOrthogonal=
        safe_text,
    isComposite=
        safe_text
)
uml::StructuredActivityNode_strategy = st.builds(
    uml::StructuredActivityNode,
    mustIsolate=
        safe_text
)
uml::Transition_strategy = st.builds(
    uml::Transition,
    kind=
        safe_text
)
uml::InteractionOperand_strategy = st.builds(
    uml::InteractionOperand,
)
uml::Package_strategy = st.builds(
    uml::Package,
)
Relationship_strategy = st.builds(
    Relationship,
)
uml::Association_strategy = st.builds(
    uml::Association,
    isDerived=
        safe_text
)
uml::DirectedRelationship_strategy = st.builds(
    uml::DirectedRelationship,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=uml::FinalState_strategy)
@settings(max_examples=50)
def test_uml::finalstate_instantiation(instance):
    assert isinstance(instance, uml::FinalState)

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=uml::DurationObservation_strategy)
@settings(max_examples=50)
def test_uml::durationobservation_instantiation(instance):
    assert isinstance(instance, uml::DurationObservation)

@given(instance=uml::DurationObservation_strategy)
def test_uml::durationobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml::DurationObservation_strategy)
def test_uml::durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml::TimeObservation_strategy)
@settings(max_examples=50)
def test_uml::timeobservation_instantiation(instance):
    assert isinstance(instance, uml::TimeObservation)

@given(instance=uml::TimeObservation_strategy)
def test_uml::timeobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml::TimeObservation_strategy)
def test_uml::timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=uml::DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml::durationconstraint_instantiation(instance):
    assert isinstance(instance, uml::DurationConstraint)

@given(instance=uml::DurationConstraint_strategy)
def test_uml::durationconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml::DurationConstraint_strategy)
def test_uml::durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=uml::TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml::timeconstraint_instantiation(instance):
    assert isinstance(instance, uml::TimeConstraint)

@given(instance=uml::TimeConstraint_strategy)
def test_uml::timeconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=uml::TimeConstraint_strategy)
def test_uml::timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=uml::TimeInterval_strategy)
@settings(max_examples=50)
def test_uml::timeinterval_instantiation(instance):
    assert isinstance(instance, uml::TimeInterval)

@given(instance=uml::DurationInterval_strategy)
@settings(max_examples=50)
def test_uml::durationinterval_instantiation(instance):
    assert isinstance(instance, uml::DurationInterval)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=uml::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml::destroylinkaction_instantiation(instance):
    assert isinstance(instance, uml::DestroyLinkAction)

@given(instance=uml::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml::createlinkaction_instantiation(instance):
    assert isinstance(instance, uml::CreateLinkAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=uml::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_uml::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, uml::LinkEndDestructionData)

@given(instance=uml::LinkEndDestructionData_strategy)
def test_uml::linkenddestructiondata_isDestroyDuplicates_type(instance):
    assert isinstance(instance.isDestroyDuplicates, str)


@given(instance=uml::LinkEndDestructionData_strategy)
def test_uml::linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=uml::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, uml::LinkEndCreationData)

@given(instance=uml::LinkEndCreationData_strategy)
def test_uml::linkendcreationdata_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml::LinkEndCreationData_strategy)
def test_uml::linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=uml::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml::writelinkaction_instantiation(instance):
    assert isinstance(instance, uml::WriteLinkAction)

@given(instance=uml::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml::readlinkaction_instantiation(instance):
    assert isinstance(instance, uml::ReadLinkAction)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=uml::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml::WriteStructuralFeatureAction)

@given(instance=uml::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml::ClearStructuralFeatureAction)

@given(instance=uml::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml::ReadStructuralFeatureAction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=uml::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml::AddStructuralFeatureValueAction)

@given(instance=uml::AddStructuralFeatureValueAction_strategy)
def test_uml::addstructuralfeaturevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml::AddStructuralFeatureValueAction_strategy)
def test_uml::addstructuralfeaturevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml::RemoveStructuralFeatureValueAction)

@given(instance=uml::RemoveStructuralFeatureValueAction_strategy)
def test_uml::removestructuralfeaturevalueaction_isRemoveDuplicates_type(instance):
    assert isinstance(instance.isRemoveDuplicates, str)


@given(instance=uml::RemoveStructuralFeatureValueAction_strategy)
def test_uml::removestructuralfeaturevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=uml::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml::executionenvironment_instantiation(instance):
    assert isinstance(instance, uml::ExecutionEnvironment)

@given(instance=uml::Device_strategy)
@settings(max_examples=50)
def test_uml::device_instantiation(instance):
    assert isinstance(instance, uml::Device)

@given(instance=CombinedFragment_strategy)
@settings(max_examples=50)
def test_combinedfragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)

@given(instance=uml::ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_uml::considerignorefragment_instantiation(instance):
    assert isinstance(instance, uml::ConsiderIgnoreFragment)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=uml::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml::activityfinalnode_instantiation(instance):
    assert isinstance(instance, uml::ActivityFinalNode)

@given(instance=uml::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml::flowfinalnode_instantiation(instance):
    assert isinstance(instance, uml::FlowFinalNode)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=uml::CallEvent_strategy)
@settings(max_examples=50)
def test_uml::callevent_instantiation(instance):
    assert isinstance(instance, uml::CallEvent)

@given(instance=uml::ReceiveSignalEvent_strategy)
@settings(max_examples=50)
def test_uml::receivesignalevent_instantiation(instance):
    assert isinstance(instance, uml::ReceiveSignalEvent)

@given(instance=uml::SignalEvent_strategy)
@settings(max_examples=50)
def test_uml::signalevent_instantiation(instance):
    assert isinstance(instance, uml::SignalEvent)

@given(instance=uml::ReceiveOperationEvent_strategy)
@settings(max_examples=50)
def test_uml::receiveoperationevent_instantiation(instance):
    assert isinstance(instance, uml::ReceiveOperationEvent)

@given(instance=uml::AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml::anyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml::AnyReceiveEvent)

@given(instance=uml::SendSignalEvent_strategy)
@settings(max_examples=50)
def test_uml::sendsignalevent_instantiation(instance):
    assert isinstance(instance, uml::SendSignalEvent)

@given(instance=uml::SendOperationEvent_strategy)
@settings(max_examples=50)
def test_uml::sendoperationevent_instantiation(instance):
    assert isinstance(instance, uml::SendOperationEvent)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=uml::ChangeEvent_strategy)
@settings(max_examples=50)
def test_uml::changeevent_instantiation(instance):
    assert isinstance(instance, uml::ChangeEvent)

@given(instance=uml::DestructionEvent_strategy)
@settings(max_examples=50)
def test_uml::destructionevent_instantiation(instance):
    assert isinstance(instance, uml::DestructionEvent)

@given(instance=uml::MessageEvent_strategy)
@settings(max_examples=50)
def test_uml::messageevent_instantiation(instance):
    assert isinstance(instance, uml::MessageEvent)

@given(instance=uml::TimeEvent_strategy)
@settings(max_examples=50)
def test_uml::timeevent_instantiation(instance):
    assert isinstance(instance, uml::TimeEvent)

@given(instance=uml::TimeEvent_strategy)
def test_uml::timeevent_isRelative_type(instance):
    assert isinstance(instance.isRelative, str)


@given(instance=uml::TimeEvent_strategy)
def test_uml::timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=uml::CreationEvent_strategy)
@settings(max_examples=50)
def test_uml::creationevent_instantiation(instance):
    assert isinstance(instance, uml::CreationEvent)

@given(instance=uml::ExecutionEvent_strategy)
@settings(max_examples=50)
def test_uml::executionevent_instantiation(instance):
    assert isinstance(instance, uml::ExecutionEvent)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=uml::BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml::behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml::BehaviorExecutionSpecification)

@given(instance=uml::ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml::actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml::ActionExecutionSpecification)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=uml::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml::intervalconstraint_instantiation(instance):
    assert isinstance(instance, uml::IntervalConstraint)

@given(instance=uml::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml::interactionconstraint_instantiation(instance):
    assert isinstance(instance, uml::InteractionConstraint)

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=uml::ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml::executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml::ExecutionOccurrenceSpecification)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=uml::MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml::messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml::MessageOccurrenceSpecification)

@given(instance=InteractionUse_strategy)
@settings(max_examples=50)
def test_interactionuse_instantiation(instance):
    assert isinstance(instance, InteractionUse)

@given(instance=uml::PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml::partdecomposition_instantiation(instance):
    assert isinstance(instance, uml::PartDecomposition)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=uml::StateInvariant_strategy)
@settings(max_examples=50)
def test_uml::stateinvariant_instantiation(instance):
    assert isinstance(instance, uml::StateInvariant)

@given(instance=uml::OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml::occurrencespecification_instantiation(instance):
    assert isinstance(instance, uml::OccurrenceSpecification)

@given(instance=uml::Continuation_strategy)
@settings(max_examples=50)
def test_uml::continuation_instantiation(instance):
    assert isinstance(instance, uml::Continuation)

@given(instance=uml::Continuation_strategy)
def test_uml::continuation_setting_type(instance):
    assert isinstance(instance.setting, str)


@given(instance=uml::Continuation_strategy)
def test_uml::continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=uml::ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml::executionspecification_instantiation(instance):
    assert isinstance(instance, uml::ExecutionSpecification)

@given(instance=uml::InteractionUse_strategy)
@settings(max_examples=50)
def test_uml::interactionuse_instantiation(instance):
    assert isinstance(instance, uml::InteractionUse)

@given(instance=uml::CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml::combinedfragment_instantiation(instance):
    assert isinstance(instance, uml::CombinedFragment)

@given(instance=uml::CombinedFragment_strategy)
def test_uml::combinedfragment_interactionOperator_type(instance):
    assert isinstance(instance.interactionOperator, str)


@given(instance=uml::CombinedFragment_strategy)
def test_uml::combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=uml::ValuePin_strategy)
@settings(max_examples=50)
def test_uml::valuepin_instantiation(instance):
    assert isinstance(instance, uml::ValuePin)

@given(instance=uml::Gate_strategy)
@settings(max_examples=50)
def test_uml::gate_instantiation(instance):
    assert isinstance(instance, uml::Gate)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=uml::SequenceNode_strategy)
@settings(max_examples=50)
def test_uml::sequencenode_instantiation(instance):
    assert isinstance(instance, uml::SequenceNode)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=uml::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml::callbehavioraction_instantiation(instance):
    assert isinstance(instance, uml::CallBehaviorAction)

@given(instance=uml::CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml::calloperationaction_instantiation(instance):
    assert isinstance(instance, uml::CallOperationAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=uml::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml::BroadcastSignalAction)

@given(instance=uml::SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml::sendsignalaction_instantiation(instance):
    assert isinstance(instance, uml::SendSignalAction)

@given(instance=uml::SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml::sendobjectaction_instantiation(instance):
    assert isinstance(instance, uml::SendObjectAction)

@given(instance=uml::CallAction_strategy)
@settings(max_examples=50)
def test_uml::callaction_instantiation(instance):
    assert isinstance(instance, uml::CallAction)

@given(instance=uml::CallAction_strategy)
def test_uml::callaction_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, str)


@given(instance=uml::CallAction_strategy)
def test_uml::callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=uml::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml::centralbuffernode_instantiation(instance):
    assert isinstance(instance, uml::CentralBufferNode)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=uml::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml::activityparameternode_instantiation(instance):
    assert isinstance(instance, uml::ActivityParameterNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=uml::MergeNode_strategy)
@settings(max_examples=50)
def test_uml::mergenode_instantiation(instance):
    assert isinstance(instance, uml::MergeNode)

@given(instance=uml::FinalNode_strategy)
@settings(max_examples=50)
def test_uml::finalnode_instantiation(instance):
    assert isinstance(instance, uml::FinalNode)

@given(instance=uml::DecisionNode_strategy)
@settings(max_examples=50)
def test_uml::decisionnode_instantiation(instance):
    assert isinstance(instance, uml::DecisionNode)

@given(instance=uml::ForkNode_strategy)
@settings(max_examples=50)
def test_uml::forknode_instantiation(instance):
    assert isinstance(instance, uml::ForkNode)

@given(instance=uml::InitialNode_strategy)
@settings(max_examples=50)
def test_uml::initialnode_instantiation(instance):
    assert isinstance(instance, uml::InitialNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=uml::ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml::objectflow_instantiation(instance):
    assert isinstance(instance, uml::ObjectFlow)

@given(instance=uml::ObjectFlow_strategy)
def test_uml::objectflow_isMultireceive_type(instance):
    assert isinstance(instance.isMultireceive, str)


@given(instance=uml::ObjectFlow_strategy)
def test_uml::objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=uml::ObjectFlow_strategy)
def test_uml::objectflow_isMulticast_type(instance):
    assert isinstance(instance.isMulticast, str)


@given(instance=uml::ObjectFlow_strategy)
def test_uml::objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=uml::ControlFlow_strategy)
@settings(max_examples=50)
def test_uml::controlflow_instantiation(instance):
    assert isinstance(instance, uml::ControlFlow)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=uml::InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml::interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml::InterruptibleActivityRegion)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=uml::ControlNode_strategy)
@settings(max_examples=50)
def test_uml::controlnode_instantiation(instance):
    assert isinstance(instance, uml::ControlNode)

@given(instance=uml::ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml::executablenode_instantiation(instance):
    assert isinstance(instance, uml::ExecutableNode)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=uml::Action_strategy)
@settings(max_examples=50)
def test_uml::action_instantiation(instance):
    assert isinstance(instance, uml::Action)

@given(instance=uml::OutputPin_strategy)
@settings(max_examples=50)
def test_uml::outputpin_instantiation(instance):
    assert isinstance(instance, uml::OutputPin)

@given(instance=uml::InputPin_strategy)
@settings(max_examples=50)
def test_uml::inputpin_instantiation(instance):
    assert isinstance(instance, uml::InputPin)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=uml::InvocationAction_strategy)
@settings(max_examples=50)
def test_uml::invocationaction_instantiation(instance):
    assert isinstance(instance, uml::InvocationAction)

@given(instance=uml::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, uml::ValueSpecificationAction)

@given(instance=uml::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml::readselfaction_instantiation(instance):
    assert isinstance(instance, uml::ReadSelfAction)

@given(instance=uml::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml::StructuralFeatureAction)

@given(instance=uml::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml::DestroyObjectAction)

@given(instance=uml::DestroyObjectAction_strategy)
def test_uml::destroyobjectaction_isDestroyOwnedObjects_type(instance):
    assert isinstance(instance.isDestroyOwnedObjects, str)


@given(instance=uml::DestroyObjectAction_strategy)
def test_uml::destroyobjectaction_isDestroyOwnedObjects_setter(instance):
    original = instance.isDestroyOwnedObjects
    instance.isDestroyOwnedObjects = original
    assert instance.isDestroyOwnedObjects == original

@given(instance=uml::DestroyObjectAction_strategy)
def test_uml::destroyobjectaction_isDestroyLinks_type(instance):
    assert isinstance(instance.isDestroyLinks, str)


@given(instance=uml::DestroyObjectAction_strategy)
def test_uml::destroyobjectaction_isDestroyLinks_setter(instance):
    original = instance.isDestroyLinks
    instance.isDestroyLinks = original
    assert instance.isDestroyLinks == original

@given(instance=uml::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml::createobjectaction_instantiation(instance):
    assert isinstance(instance, uml::CreateObjectAction)

@given(instance=uml::LinkAction_strategy)
@settings(max_examples=50)
def test_uml::linkaction_instantiation(instance):
    assert isinstance(instance, uml::LinkAction)

@given(instance=uml::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml::testidentityaction_instantiation(instance):
    assert isinstance(instance, uml::TestIdentityAction)

@given(instance=uml::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml::clearassociationaction_instantiation(instance):
    assert isinstance(instance, uml::ClearAssociationAction)

@given(instance=uml::OpaqueAction_strategy)
@settings(max_examples=50)
def test_uml::opaqueaction_instantiation(instance):
    assert isinstance(instance, uml::OpaqueAction)

@given(instance=uml::OpaqueAction_strategy)
def test_uml::opaqueaction_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=uml::OpaqueAction_strategy)
def test_uml::opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=uml::OpaqueAction_strategy)
def test_uml::opaqueaction_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml::OpaqueAction_strategy)
def test_uml::opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=uml::FunctionBehavior_strategy)
@settings(max_examples=50)
def test_uml::functionbehavior_instantiation(instance):
    assert isinstance(instance, uml::FunctionBehavior)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=uml::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml::LiteralUnlimitedNatural)

@given(instance=uml::LiteralUnlimitedNatural_strategy)
def test_uml::literalunlimitednatural_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml::LiteralUnlimitedNatural_strategy)
def test_uml::literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml::LiteralNull_strategy)
@settings(max_examples=50)
def test_uml::literalnull_instantiation(instance):
    assert isinstance(instance, uml::LiteralNull)

@given(instance=uml::LiteralString_strategy)
@settings(max_examples=50)
def test_uml::literalstring_instantiation(instance):
    assert isinstance(instance, uml::LiteralString)

@given(instance=uml::LiteralString_strategy)
def test_uml::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml::LiteralString_strategy)
def test_uml::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml::literalboolean_instantiation(instance):
    assert isinstance(instance, uml::LiteralBoolean)

@given(instance=uml::LiteralBoolean_strategy)
def test_uml::literalboolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml::LiteralBoolean_strategy)
def test_uml::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml::LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml::literalinteger_instantiation(instance):
    assert isinstance(instance, uml::LiteralInteger)

@given(instance=uml::LiteralInteger_strategy)
def test_uml::literalinteger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uml::LiteralInteger_strategy)
def test_uml::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml::enumerationliteral_instantiation(instance):
    assert isinstance(instance, uml::EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=uml::PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml::primitivetype_instantiation(instance):
    assert isinstance(instance, uml::PrimitiveType)

@given(instance=uml::Enumeration_strategy)
@settings(max_examples=50)
def test_uml::enumeration_instantiation(instance):
    assert isinstance(instance, uml::Enumeration)

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

@given(instance=uml::ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, uml::ClassifierTemplateParameter)

@given(instance=uml::ClassifierTemplateParameter_strategy)
def test_uml::classifiertemplateparameter_allowSubstitutable_type(instance):
    assert isinstance(instance.allowSubstitutable, str)


@given(instance=uml::ClassifierTemplateParameter_strategy)
def test_uml::classifiertemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=uml::ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml::ConnectableElementTemplateParameter)

@given(instance=uml::OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml::OperationTemplateParameter)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=uml::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml::communicationpath_instantiation(instance):
    assert isinstance(instance, uml::CommunicationPath)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=uml::Model_strategy)
@settings(max_examples=50)
def test_uml::model_instantiation(instance):
    assert isinstance(instance, uml::Model)

@given(instance=uml::Model_strategy)
def test_uml::model_viewpoint_type(instance):
    assert isinstance(instance.viewpoint, str)


@given(instance=uml::Model_strategy)
def test_uml::model_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original

@given(instance=uml::Profile_strategy)
@settings(max_examples=50)
def test_uml::profile_instantiation(instance):
    assert isinstance(instance, uml::Profile)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=uml::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, uml::EncapsulatedClassifier)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=uml::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml::extensionend_instantiation(instance):
    assert isinstance(instance, uml::ExtensionEnd)

@given(instance=uml::Port_strategy)
@settings(max_examples=50)
def test_uml::port_instantiation(instance):
    assert isinstance(instance, uml::Port)

@given(instance=uml::Port_strategy)
def test_uml::port_isService_type(instance):
    assert isinstance(instance.isService, str)


@given(instance=uml::Port_strategy)
def test_uml::port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original

@given(instance=uml::Port_strategy)
def test_uml::port_isBehavior_type(instance):
    assert isinstance(instance.isBehavior, str)


@given(instance=uml::Port_strategy)
def test_uml::port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original

@given(instance=uml::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml::connectionpointreference_instantiation(instance):
    assert isinstance(instance, uml::ConnectionPointReference)

@given(instance=uml::Pseudostate_strategy)
@settings(max_examples=50)
def test_uml::pseudostate_instantiation(instance):
    assert isinstance(instance, uml::Pseudostate)

@given(instance=uml::Pseudostate_strategy)
def test_uml::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml::Pseudostate_strategy)
def test_uml::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=uml::Interaction_strategy)
@settings(max_examples=50)
def test_uml::interaction_instantiation(instance):
    assert isinstance(instance, uml::Interaction)

@given(instance=uml::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_uml::opaquebehavior_instantiation(instance):
    assert isinstance(instance, uml::OpaqueBehavior)

@given(instance=uml::OpaqueBehavior_strategy)
def test_uml::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml::OpaqueBehavior_strategy)
def test_uml::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml::OpaqueBehavior_strategy)
def test_uml::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=uml::OpaqueBehavior_strategy)
def test_uml::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=uml::Activity_strategy)
@settings(max_examples=50)
def test_uml::activity_instantiation(instance):
    assert isinstance(instance, uml::Activity)

@given(instance=uml::Activity_strategy)
def test_uml::activity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=uml::Activity_strategy)
def test_uml::activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=uml::Activity_strategy)
def test_uml::activity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, str)


@given(instance=uml::Activity_strategy)
def test_uml::activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=uml::StateMachine_strategy)
@settings(max_examples=50)
def test_uml::statemachine_instantiation(instance):
    assert isinstance(instance, uml::StateMachine)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=uml::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, uml::ProtocolStateMachine)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=uml::Stereotype_strategy)
@settings(max_examples=50)
def test_uml::stereotype_instantiation(instance):
    assert isinstance(instance, uml::Stereotype)

@given(instance=uml::Component_strategy)
@settings(max_examples=50)
def test_uml::component_instantiation(instance):
    assert isinstance(instance, uml::Component)

@given(instance=uml::Component_strategy)
def test_uml::component_isIndirectlyInstantiated_type(instance):
    assert isinstance(instance.isIndirectlyInstantiated, str)


@given(instance=uml::Component_strategy)
def test_uml::component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original

@given(instance=uml::Extension_strategy)
@settings(max_examples=50)
def test_uml::extension_instantiation(instance):
    assert isinstance(instance, uml::Extension)

@given(instance=uml::Extension_strategy)
def test_uml::extension_isRequired_type(instance):
    assert isinstance(instance.isRequired, str)


@given(instance=uml::Extension_strategy)
def test_uml::extension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=uml::Actor_strategy)
@settings(max_examples=50)
def test_uml::actor_instantiation(instance):
    assert isinstance(instance, uml::Actor)

@given(instance=uml::Collaboration_strategy)
@settings(max_examples=50)
def test_uml::collaboration_instantiation(instance):
    assert isinstance(instance, uml::Collaboration)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=uml::Reception_strategy)
@settings(max_examples=50)
def test_uml::reception_instantiation(instance):
    assert isinstance(instance, uml::Reception)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=uml::Connector_strategy)
@settings(max_examples=50)
def test_uml::connector_instantiation(instance):
    assert isinstance(instance, uml::Connector)

@given(instance=uml::Connector_strategy)
def test_uml::connector_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml::Connector_strategy)
def test_uml::connector_kind_setter(instance):
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

@given(instance=uml::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml::deploymentspecification_instantiation(instance):
    assert isinstance(instance, uml::DeploymentSpecification)

@given(instance=uml::DeploymentSpecification_strategy)
def test_uml::deploymentspecification_executionLocation_type(instance):
    assert isinstance(instance.executionLocation, str)


@given(instance=uml::DeploymentSpecification_strategy)
def test_uml::deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original

@given(instance=uml::DeploymentSpecification_strategy)
def test_uml::deploymentspecification_deploymentLocation_type(instance):
    assert isinstance(instance.deploymentLocation, str)


@given(instance=uml::DeploymentSpecification_strategy)
def test_uml::deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=uml::Class_strategy)
@settings(max_examples=50)
def test_uml::class_instantiation(instance):
    assert isinstance(instance, uml::Class)

@given(instance=uml::Class_strategy)
def test_uml::class_isActive_type(instance):
    assert isinstance(instance.isActive, str)


@given(instance=uml::Class_strategy)
def test_uml::class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=uml::Node_strategy)
@settings(max_examples=50)
def test_uml::node_instantiation(instance):
    assert isinstance(instance, uml::Node)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=uml::InterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml::interfacerealization_instantiation(instance):
    assert isinstance(instance, uml::InterfaceRealization)

@given(instance=uml::ComponentRealization_strategy)
@settings(max_examples=50)
def test_uml::componentrealization_instantiation(instance):
    assert isinstance(instance, uml::ComponentRealization)

@given(instance=uml::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml::associationclass_instantiation(instance):
    assert isinstance(instance, uml::AssociationClass)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=uml::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml::protocoltransition_instantiation(instance):
    assert isinstance(instance, uml::ProtocolTransition)

@given(instance=uml::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml::expansionregion_instantiation(instance):
    assert isinstance(instance, uml::ExpansionRegion)

@given(instance=uml::ExpansionRegion_strategy)
def test_uml::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=uml::ExpansionRegion_strategy)
def test_uml::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=uml::ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml::expansionnode_instantiation(instance):
    assert isinstance(instance, uml::ExpansionNode)

@given(instance=uml::LoopNode_strategy)
@settings(max_examples=50)
def test_uml::loopnode_instantiation(instance):
    assert isinstance(instance, uml::LoopNode)

@given(instance=uml::LoopNode_strategy)
def test_uml::loopnode_isTestedFirst_type(instance):
    assert isinstance(instance.isTestedFirst, str)


@given(instance=uml::LoopNode_strategy)
def test_uml::loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=uml::ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml::conditionalnode_instantiation(instance):
    assert isinstance(instance, uml::ConditionalNode)

@given(instance=uml::ConditionalNode_strategy)
def test_uml::conditionalnode_isAssured_type(instance):
    assert isinstance(instance.isAssured, str)


@given(instance=uml::ConditionalNode_strategy)
def test_uml::conditionalnode_isAssured_setter(instance):
    original = instance.isAssured
    instance.isAssured = original
    assert instance.isAssured == original

@given(instance=uml::ConditionalNode_strategy)
def test_uml::conditionalnode_isDeterminate_type(instance):
    assert isinstance(instance.isDeterminate, str)


@given(instance=uml::ConditionalNode_strategy)
def test_uml::conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=uml::DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml::datastorenode_instantiation(instance):
    assert isinstance(instance, uml::DataStoreNode)

@given(instance=uml::JoinNode_strategy)
@settings(max_examples=50)
def test_uml::joinnode_instantiation(instance):
    assert isinstance(instance, uml::JoinNode)

@given(instance=uml::JoinNode_strategy)
def test_uml::joinnode_isCombineDuplicate_type(instance):
    assert isinstance(instance.isCombineDuplicate, str)


@given(instance=uml::JoinNode_strategy)
def test_uml::joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=uml::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml::StartObjectBehaviorAction)

@given(instance=uml::ReduceAction_strategy)
@settings(max_examples=50)
def test_uml::reduceaction_instantiation(instance):
    assert isinstance(instance, uml::ReduceAction)

@given(instance=uml::ReduceAction_strategy)
def test_uml::reduceaction_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=uml::ReduceAction_strategy)
def test_uml::reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml::UnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml::unmarshallaction_instantiation(instance):
    assert isinstance(instance, uml::UnmarshallAction)

@given(instance=uml::ReplyAction_strategy)
@settings(max_examples=50)
def test_uml::replyaction_instantiation(instance):
    assert isinstance(instance, uml::ReplyAction)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=uml::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml::acceptcallaction_instantiation(instance):
    assert isinstance(instance, uml::AcceptCallAction)

@given(instance=uml::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml::accepteventaction_instantiation(instance):
    assert isinstance(instance, uml::AcceptEventAction)

@given(instance=uml::AcceptEventAction_strategy)
def test_uml::accepteventaction_isUnmarshall_type(instance):
    assert isinstance(instance.isUnmarshall, str)


@given(instance=uml::AcceptEventAction_strategy)
def test_uml::accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=uml::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, uml::CreateLinkObjectAction)

@given(instance=uml::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml::ReadLinkObjectEndQualifierAction)

@given(instance=uml::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml::StartClassifierBehaviorAction)

@given(instance=uml::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml::ReadIsClassifiedObjectAction)

@given(instance=uml::ReadIsClassifiedObjectAction_strategy)
def test_uml::readisclassifiedobjectaction_isDirect_type(instance):
    assert isinstance(instance.isDirect, str)


@given(instance=uml::ReadIsClassifiedObjectAction_strategy)
def test_uml::readisclassifiedobjectaction_isDirect_setter(instance):
    original = instance.isDirect
    instance.isDirect = original
    assert instance.isDirect == original

@given(instance=uml::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml::ReclassifyObjectAction)

@given(instance=uml::ReclassifyObjectAction_strategy)
def test_uml::reclassifyobjectaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml::ReclassifyObjectAction_strategy)
def test_uml::reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=uml::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml::ReadLinkObjectEndAction)

@given(instance=uml::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml::readextentaction_instantiation(instance):
    assert isinstance(instance, uml::ReadExtentAction)

@given(instance=uml::ActionInputPin_strategy)
@settings(max_examples=50)
def test_uml::actioninputpin_instantiation(instance):
    assert isinstance(instance, uml::ActionInputPin)

@given(instance=uml::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml::RaiseExceptionAction)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=uml::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml::RemoveVariableValueAction)

@given(instance=uml::RemoveVariableValueAction_strategy)
def test_uml::removevariablevalueaction_isRemoveDuplicates_type(instance):
    assert isinstance(instance.isRemoveDuplicates, str)


@given(instance=uml::RemoveVariableValueAction_strategy)
def test_uml::removevariablevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=uml::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml::AddVariableValueAction)

@given(instance=uml::AddVariableValueAction_strategy)
def test_uml::addvariablevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=uml::AddVariableValueAction_strategy)
def test_uml::addvariablevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=uml::ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml::protocolconformance_instantiation(instance):
    assert isinstance(instance, uml::ProtocolConformance)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=uml::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml::clearvariableaction_instantiation(instance):
    assert isinstance(instance, uml::ClearVariableAction)

@given(instance=uml::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml::writevariableaction_instantiation(instance):
    assert isinstance(instance, uml::WriteVariableAction)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uml::QualifierValue_strategy)
@settings(max_examples=50)
def test_uml::qualifiervalue_instantiation(instance):
    assert isinstance(instance, uml::QualifierValue)

@given(instance=uml::LinkEndData_strategy)
@settings(max_examples=50)
def test_uml::linkenddata_instantiation(instance):
    assert isinstance(instance, uml::LinkEndData)

@given(instance=uml::ActivityGroup_strategy)
@settings(max_examples=50)
def test_uml::activitygroup_instantiation(instance):
    assert isinstance(instance, uml::ActivityGroup)

@given(instance=uml::Slot_strategy)
@settings(max_examples=50)
def test_uml::slot_instantiation(instance):
    assert isinstance(instance, uml::Slot)

@given(instance=uml::Image_strategy)
@settings(max_examples=50)
def test_uml::image_instantiation(instance):
    assert isinstance(instance, uml::Image)

@given(instance=uml::Image_strategy)
def test_uml::image_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=uml::Image_strategy)
def test_uml::image_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=uml::Image_strategy)
def test_uml::image_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=uml::Image_strategy)
def test_uml::image_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=uml::Image_strategy)
def test_uml::image_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=uml::Image_strategy)
def test_uml::image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=uml::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml::multiplicityelement_instantiation(instance):
    assert isinstance(instance, uml::MultiplicityElement)

@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=uml::MultiplicityElement_strategy)
def test_uml::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml::Clause_strategy)
@settings(max_examples=50)
def test_uml::clause_instantiation(instance):
    assert isinstance(instance, uml::Clause)

@given(instance=uml::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml::exceptionhandler_instantiation(instance):
    assert isinstance(instance, uml::ExceptionHandler)

@given(instance=uml::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml::readvariableaction_instantiation(instance):
    assert isinstance(instance, uml::ReadVariableAction)

@given(instance=uml::Comment_strategy)
@settings(max_examples=50)
def test_uml::comment_instantiation(instance):
    assert isinstance(instance, uml::Comment)

@given(instance=uml::Comment_strategy)
def test_uml::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml::Comment_strategy)
def test_uml::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml::VariableAction_strategy)
@settings(max_examples=50)
def test_uml::variableaction_instantiation(instance):
    assert isinstance(instance, uml::VariableAction)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=uml::Element_strategy)
@settings(max_examples=50)
def test_uml::element_instantiation(instance):
    assert isinstance(instance, uml::Element)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=uml::Pin_strategy)
@settings(max_examples=50)
def test_uml::pin_instantiation(instance):
    assert isinstance(instance, uml::Pin)

@given(instance=uml::Pin_strategy)
def test_uml::pin_isControl_type(instance):
    assert isinstance(instance.isControl, str)


@given(instance=uml::Pin_strategy)
def test_uml::pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=uml::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml::connectorend_instantiation(instance):
    assert isinstance(instance, uml::ConnectorEnd)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=uml::Variable_strategy)
@settings(max_examples=50)
def test_uml::variable_instantiation(instance):
    assert isinstance(instance, uml::Variable)

@given(instance=uml::Behavior_strategy)
@settings(max_examples=50)
def test_uml::behavior_instantiation(instance):
    assert isinstance(instance, uml::Behavior)

@given(instance=uml::Behavior_strategy)
def test_uml::behavior_isReentrant_type(instance):
    assert isinstance(instance.isReentrant, str)


@given(instance=uml::Behavior_strategy)
def test_uml::behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=uml::Parameter_strategy)
@settings(max_examples=50)
def test_uml::parameter_instantiation(instance):
    assert isinstance(instance, uml::Parameter)

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isException_type(instance):
    assert isinstance(instance.isException, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isStream_type(instance):
    assert isinstance(instance.isStream, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=uml::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml::literalspecification_instantiation(instance):
    assert isinstance(instance, uml::LiteralSpecification)

@given(instance=uml::TimeExpression_strategy)
@settings(max_examples=50)
def test_uml::timeexpression_instantiation(instance):
    assert isinstance(instance, uml::TimeExpression)

@given(instance=uml::Duration_strategy)
@settings(max_examples=50)
def test_uml::duration_instantiation(instance):
    assert isinstance(instance, uml::Duration)

@given(instance=uml::Interval_strategy)
@settings(max_examples=50)
def test_uml::interval_instantiation(instance):
    assert isinstance(instance, uml::Interval)

@given(instance=uml::InstanceValue_strategy)
@settings(max_examples=50)
def test_uml::instancevalue_instantiation(instance):
    assert isinstance(instance, uml::InstanceValue)

@given(instance=uml::Expression_strategy)
@settings(max_examples=50)
def test_uml::expression_instantiation(instance):
    assert isinstance(instance, uml::Expression)

@given(instance=uml::Expression_strategy)
def test_uml::expression_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=uml::Expression_strategy)
def test_uml::expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=uml::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml::opaqueexpression_instantiation(instance):
    assert isinstance(instance, uml::OpaqueExpression)

@given(instance=uml::OpaqueExpression_strategy)
def test_uml::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=uml::OpaqueExpression_strategy)
def test_uml::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=uml::OpaqueExpression_strategy)
def test_uml::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml::OpaqueExpression_strategy)
def test_uml::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=uml::Deployment_strategy)
@settings(max_examples=50)
def test_uml::deployment_instantiation(instance):
    assert isinstance(instance, uml::Deployment)

@given(instance=uml::Usage_strategy)
@settings(max_examples=50)
def test_uml::usage_instantiation(instance):
    assert isinstance(instance, uml::Usage)

@given(instance=uml::Abstraction_strategy)
@settings(max_examples=50)
def test_uml::abstraction_instantiation(instance):
    assert isinstance(instance, uml::Abstraction)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=uml::Manifestation_strategy)
@settings(max_examples=50)
def test_uml::manifestation_instantiation(instance):
    assert isinstance(instance, uml::Manifestation)

@given(instance=uml::Realization_strategy)
@settings(max_examples=50)
def test_uml::realization_instantiation(instance):
    assert isinstance(instance, uml::Realization)

@given(instance=uml::ParameterableElement_strategy)
@settings(max_examples=50)
def test_uml::parameterableelement_instantiation(instance):
    assert isinstance(instance, uml::ParameterableElement)

@given(instance=uml::UseCase_strategy)
@settings(max_examples=50)
def test_uml::usecase_instantiation(instance):
    assert isinstance(instance, uml::UseCase)

@given(instance=uml::Substitution_strategy)
@settings(max_examples=50)
def test_uml::substitution_instantiation(instance):
    assert isinstance(instance, uml::Substitution)

@given(instance=uml::TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::templateparameter_instantiation(instance):
    assert isinstance(instance, uml::TemplateParameter)

@given(instance=uml::TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml::templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml::TemplateParameterSubstitution)

@given(instance=uml::TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml::templatesignature_instantiation(instance):
    assert isinstance(instance, uml::TemplateSignature)

@given(instance=uml::TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml::templatebinding_instantiation(instance):
    assert isinstance(instance, uml::TemplateBinding)

@given(instance=uml::TemplateableElement_strategy)
@settings(max_examples=50)
def test_uml::templateableelement_instantiation(instance):
    assert isinstance(instance, uml::TemplateableElement)

@given(instance=uml::Property_strategy)
@settings(max_examples=50)
def test_uml::property_instantiation(instance):
    assert isinstance(instance, uml::Property)

@given(instance=uml::Property_strategy)
def test_uml::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=uml::Property_strategy)
def test_uml::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=uml::Property_strategy)
def test_uml::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=uml::Property_strategy)
def test_uml::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=uml::Property_strategy)
def test_uml::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=uml::Property_strategy)
def test_uml::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml::Property_strategy)
def test_uml::property_isDerivedUnion_type(instance):
    assert isinstance(instance.isDerivedUnion, str)


@given(instance=uml::Property_strategy)
def test_uml::property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original

@given(instance=uml::Property_strategy)
def test_uml::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=uml::Property_strategy)
def test_uml::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml::Signal_strategy)
@settings(max_examples=50)
def test_uml::signal_instantiation(instance):
    assert isinstance(instance, uml::Signal)

@given(instance=uml::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml::structuredclassifier_instantiation(instance):
    assert isinstance(instance, uml::StructuredClassifier)

@given(instance=uml::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml::BehavioredClassifier)

@given(instance=uml::Interface_strategy)
@settings(max_examples=50)
def test_uml::interface_instantiation(instance):
    assert isinstance(instance, uml::Interface)

@given(instance=uml::DataType_strategy)
@settings(max_examples=50)
def test_uml::datatype_instantiation(instance):
    assert isinstance(instance, uml::DataType)

@given(instance=uml::InformationItem_strategy)
@settings(max_examples=50)
def test_uml::informationitem_instantiation(instance):
    assert isinstance(instance, uml::InformationItem)

@given(instance=uml::Artifact_strategy)
@settings(max_examples=50)
def test_uml::artifact_instantiation(instance):
    assert isinstance(instance, uml::Artifact)

@given(instance=uml::Artifact_strategy)
def test_uml::artifact_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=uml::Artifact_strategy)
def test_uml::artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=uml::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml::structuralfeature_instantiation(instance):
    assert isinstance(instance, uml::StructuralFeature)

@given(instance=uml::StructuralFeature_strategy)
def test_uml::structuralfeature_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=uml::StructuralFeature_strategy)
def test_uml::structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=uml::ObjectNode_strategy)
@settings(max_examples=50)
def test_uml::objectnode_instantiation(instance):
    assert isinstance(instance, uml::ObjectNode)

@given(instance=uml::ObjectNode_strategy)
def test_uml::objectnode_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=uml::ObjectNode_strategy)
def test_uml::objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=uml::ObjectNode_strategy)
def test_uml::objectnode_isControlType_type(instance):
    assert isinstance(instance.isControlType, str)


@given(instance=uml::ObjectNode_strategy)
def test_uml::objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=uml::Generalization_strategy)
@settings(max_examples=50)
def test_uml::generalization_instantiation(instance):
    assert isinstance(instance, uml::Generalization)

@given(instance=uml::Generalization_strategy)
def test_uml::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, str)


@given(instance=uml::Generalization_strategy)
def test_uml::generalization_isSubstitutable_setter(instance):
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

@given(instance=uml::Feature_strategy)
@settings(max_examples=50)
def test_uml::feature_instantiation(instance):
    assert isinstance(instance, uml::Feature)

@given(instance=uml::Feature_strategy)
def test_uml::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=uml::Feature_strategy)
def test_uml::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=uml::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml::extensionpoint_instantiation(instance):
    assert isinstance(instance, uml::ExtensionPoint)

@given(instance=uml::ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml::activityedge_instantiation(instance):
    assert isinstance(instance, uml::ActivityEdge)

@given(instance=uml::RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml::redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, uml::RedefinableTemplateSignature)

@given(instance=uml::ActivityNode_strategy)
@settings(max_examples=50)
def test_uml::activitynode_instantiation(instance):
    assert isinstance(instance, uml::ActivityNode)

@given(instance=uml::PackageImport_strategy)
@settings(max_examples=50)
def test_uml::packageimport_instantiation(instance):
    assert isinstance(instance, uml::PackageImport)

@given(instance=uml::PackageImport_strategy)
def test_uml::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml::PackageImport_strategy)
def test_uml::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml::ElementImport_strategy)
@settings(max_examples=50)
def test_uml::elementimport_instantiation(instance):
    assert isinstance(instance, uml::ElementImport)

@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=uml::Relationship_strategy)
@settings(max_examples=50)
def test_uml::relationship_instantiation(instance):
    assert isinstance(instance, uml::Relationship)

@given(instance=uml::NamedElement_strategy)
@settings(max_examples=50)
def test_uml::namedelement_instantiation(instance):
    assert isinstance(instance, uml::NamedElement)

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=uml::ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml::connectableelement_instantiation(instance):
    assert isinstance(instance, uml::ConnectableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml::InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml::interactionfragment_instantiation(instance):
    assert isinstance(instance, uml::InteractionFragment)

@given(instance=uml::MessageEnd_strategy)
@settings(max_examples=50)
def test_uml::messageend_instantiation(instance):
    assert isinstance(instance, uml::MessageEnd)

@given(instance=uml::CollaborationUse_strategy)
@settings(max_examples=50)
def test_uml::collaborationuse_instantiation(instance):
    assert isinstance(instance, uml::CollaborationUse)

@given(instance=uml::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml::generalordering_instantiation(instance):
    assert isinstance(instance, uml::GeneralOrdering)

@given(instance=uml::Extend_strategy)
@settings(max_examples=50)
def test_uml::extend_instantiation(instance):
    assert isinstance(instance, uml::Extend)

@given(instance=uml::TypedElement_strategy)
@settings(max_examples=50)
def test_uml::typedelement_instantiation(instance):
    assert isinstance(instance, uml::TypedElement)

@given(instance=uml::Include_strategy)
@settings(max_examples=50)
def test_uml::include_instantiation(instance):
    assert isinstance(instance, uml::Include)

@given(instance=uml::Vertex_strategy)
@settings(max_examples=50)
def test_uml::vertex_instantiation(instance):
    assert isinstance(instance, uml::Vertex)

@given(instance=uml::Message_strategy)
@settings(max_examples=50)
def test_uml::message_instantiation(instance):
    assert isinstance(instance, uml::Message)

@given(instance=uml::Message_strategy)
def test_uml::message_messageSort_type(instance):
    assert isinstance(instance.messageSort, str)


@given(instance=uml::Message_strategy)
def test_uml::message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original

@given(instance=uml::Message_strategy)
def test_uml::message_messageKind_type(instance):
    assert isinstance(instance.messageKind, str)


@given(instance=uml::Message_strategy)
def test_uml::message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original

@given(instance=uml::DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml::deployedartifact_instantiation(instance):
    assert isinstance(instance, uml::DeployedArtifact)

@given(instance=uml::DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml::deploymenttarget_instantiation(instance):
    assert isinstance(instance, uml::DeploymentTarget)

@given(instance=uml::Trigger_strategy)
@settings(max_examples=50)
def test_uml::trigger_instantiation(instance):
    assert isinstance(instance, uml::Trigger)

@given(instance=uml::Namespace_strategy)
@settings(max_examples=50)
def test_uml::namespace_instantiation(instance):
    assert isinstance(instance, uml::Namespace)

@given(instance=uml::RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml::redefinableelement_instantiation(instance):
    assert isinstance(instance, uml::RedefinableElement)

@given(instance=uml::RedefinableElement_strategy)
def test_uml::redefinableelement_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, str)


@given(instance=uml::RedefinableElement_strategy)
def test_uml::redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=uml::ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml::activitypartition_instantiation(instance):
    assert isinstance(instance, uml::ActivityPartition)

@given(instance=uml::ActivityPartition_strategy)
def test_uml::activitypartition_isExternal_type(instance):
    assert isinstance(instance.isExternal, str)


@given(instance=uml::ActivityPartition_strategy)
def test_uml::activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=uml::ActivityPartition_strategy)
def test_uml::activitypartition_isDimension_type(instance):
    assert isinstance(instance.isDimension, str)


@given(instance=uml::ActivityPartition_strategy)
def test_uml::activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=uml::ParameterSet_strategy)
@settings(max_examples=50)
def test_uml::parameterset_instantiation(instance):
    assert isinstance(instance, uml::ParameterSet)

@given(instance=uml::Lifeline_strategy)
@settings(max_examples=50)
def test_uml::lifeline_instantiation(instance):
    assert isinstance(instance, uml::Lifeline)

@given(instance=uml::ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml::profileapplication_instantiation(instance):
    assert isinstance(instance, uml::ProfileApplication)

@given(instance=uml::ProfileApplication_strategy)
def test_uml::profileapplication_isStrict_type(instance):
    assert isinstance(instance.isStrict, str)


@given(instance=uml::ProfileApplication_strategy)
def test_uml::profileapplication_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=uml::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml::packageableelement_instantiation(instance):
    assert isinstance(instance, uml::PackageableElement)

@given(instance=uml::PackageMerge_strategy)
@settings(max_examples=50)
def test_uml::packagemerge_instantiation(instance):
    assert isinstance(instance, uml::PackageMerge)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=uml::StringExpression_strategy)
@settings(max_examples=50)
def test_uml::stringexpression_instantiation(instance):
    assert isinstance(instance, uml::StringExpression)

@given(instance=uml::Operation_strategy)
@settings(max_examples=50)
def test_uml::operation_instantiation(instance):
    assert isinstance(instance, uml::Operation)

@given(instance=uml::Operation_strategy)
def test_uml::operation_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uml::Type_strategy)
@settings(max_examples=50)
def test_uml::type_instantiation(instance):
    assert isinstance(instance, uml::Type)

@given(instance=uml::Dependency_strategy)
@settings(max_examples=50)
def test_uml::dependency_instantiation(instance):
    assert isinstance(instance, uml::Dependency)

@given(instance=uml::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml::valuespecification_instantiation(instance):
    assert isinstance(instance, uml::ValueSpecification)

@given(instance=uml::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml::instancespecification_instantiation(instance):
    assert isinstance(instance, uml::InstanceSpecification)

@given(instance=uml::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml::generalizationset_instantiation(instance):
    assert isinstance(instance, uml::GeneralizationSet)

@given(instance=uml::GeneralizationSet_strategy)
def test_uml::generalizationset_isCovering_type(instance):
    assert isinstance(instance.isCovering, str)


@given(instance=uml::GeneralizationSet_strategy)
def test_uml::generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=uml::GeneralizationSet_strategy)
def test_uml::generalizationset_isDisjoint_type(instance):
    assert isinstance(instance.isDisjoint, str)


@given(instance=uml::GeneralizationSet_strategy)
def test_uml::generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=uml::Observation_strategy)
@settings(max_examples=50)
def test_uml::observation_instantiation(instance):
    assert isinstance(instance, uml::Observation)

@given(instance=uml::InformationFlow_strategy)
@settings(max_examples=50)
def test_uml::informationflow_instantiation(instance):
    assert isinstance(instance, uml::InformationFlow)

@given(instance=uml::Event_strategy)
@settings(max_examples=50)
def test_uml::event_instantiation(instance):
    assert isinstance(instance, uml::Event)

@given(instance=uml::Constraint_strategy)
@settings(max_examples=50)
def test_uml::constraint_instantiation(instance):
    assert isinstance(instance, uml::Constraint)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=uml::Classifier_strategy)
@settings(max_examples=50)
def test_uml::classifier_instantiation(instance):
    assert isinstance(instance, uml::Classifier)

@given(instance=uml::Classifier_strategy)
def test_uml::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uml::Classifier_strategy)
def test_uml::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml::Region_strategy)
@settings(max_examples=50)
def test_uml::region_instantiation(instance):
    assert isinstance(instance, uml::Region)

@given(instance=uml::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml::behavioralfeature_instantiation(instance):
    assert isinstance(instance, uml::BehavioralFeature)

@given(instance=uml::BehavioralFeature_strategy)
def test_uml::behavioralfeature_concurrency_type(instance):
    assert isinstance(instance.concurrency, str)


@given(instance=uml::BehavioralFeature_strategy)
def test_uml::behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=uml::BehavioralFeature_strategy)
def test_uml::behavioralfeature_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uml::BehavioralFeature_strategy)
def test_uml::behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml::State_strategy)
@settings(max_examples=50)
def test_uml::state_instantiation(instance):
    assert isinstance(instance, uml::State)

@given(instance=uml::State_strategy)
def test_uml::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, str)


@given(instance=uml::State_strategy)
def test_uml::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=uml::State_strategy)
def test_uml::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, str)


@given(instance=uml::State_strategy)
def test_uml::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=uml::State_strategy)
def test_uml::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, str)


@given(instance=uml::State_strategy)
def test_uml::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=uml::State_strategy)
def test_uml::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=uml::State_strategy)
def test_uml::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=uml::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml::StructuredActivityNode)

@given(instance=uml::StructuredActivityNode_strategy)
def test_uml::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, str)


@given(instance=uml::StructuredActivityNode_strategy)
def test_uml::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=uml::Transition_strategy)
@settings(max_examples=50)
def test_uml::transition_instantiation(instance):
    assert isinstance(instance, uml::Transition)

@given(instance=uml::Transition_strategy)
def test_uml::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml::Transition_strategy)
def test_uml::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uml::InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml::interactionoperand_instantiation(instance):
    assert isinstance(instance, uml::InteractionOperand)

@given(instance=uml::Package_strategy)
@settings(max_examples=50)
def test_uml::package_instantiation(instance):
    assert isinstance(instance, uml::Package)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=uml::Association_strategy)
@settings(max_examples=50)
def test_uml::association_instantiation(instance):
    assert isinstance(instance, uml::Association)

@given(instance=uml::Association_strategy)
def test_uml::association_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=uml::Association_strategy)
def test_uml::association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml::directedrelationship_instantiation(instance):
    assert isinstance(instance, uml::DirectedRelationship)

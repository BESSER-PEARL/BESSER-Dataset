import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CallAction,
    UML2::CallOperationAction,
    InvocationAction,
    UML2::CallAction,
    Property,
    UML2::Port,
    Class,
    UML2::Component,
    EncapsulatedClassifier,
    Pin,
    UML2::InputPin,
    LinkAction,
    UML2::WriteLinkAction,
    MessageTrigger,
    UML2::SignalTrigger,
    AcceptEventAction,
    UML2::AcceptCallAction,
    Behavior,
    UML2::Activity,
    TypedElement,
    ConnectableElement,
    UML2::Parameter,
    UML2::Variable,
    ActivityEdge,
    UML2::ControlFlow,
    UML2::ObjectFlow,
    StructuralFeatureAction,
    UML2::WriteStructuralFeatureAction,
    Package,
    UML2::Model,
    DeployedArtifact,
    DeploymentTarget,
    PackageableElement,
    UML2::InstanceSpecification,
    Interval,
    UML2::TimeInterval,
    InstanceSpecification,
    UML2::EnumerationLiteral,
    DataType,
    UML2::PrimitiveType,
    Realization,
    UML2::Substitution,
    UML2::Implementation,
    Node,
    UML2::ExecutionEnvironment,
    ControlNode,
    UML2::JoinNode,
    UML2::DecisionNode,
    State,
    UML2::FinalState,
    WriteStructuralFeatureAction,
    UML2::DurationObservationAction,
    UML2::Generalization,
    UML2::NamedElement,
    Type,
    ValueSpecification,
    UML2::LiteralSpecification,
    UML2::OpaqueExpression,
    UML2::Profile,
    StructuredActivityNode,
    UML2::ExpansionRegion,
    InteractionFragment,
    UML2::Interaction,
    UML2::CombinedFragment,
    UML2::InteractionOccurrence,
    UML2::StateInvariant,
    FinalNode,
    UML2::FlowFinalNode,
    LiteralSpecification,
    UML2::LiteralInteger,
    UML2::LiteralUnlimitedNatural,
    UML2::LiteralString,
    NamedElement,
    UML2::InteractionFragment,
    UML2::CollaborationOccurrence,
    UML2::ActivityPartition,
    UML2::Include,
    UML2::GeneralOrdering,
    UML2::DeployedArtifact,
    UML2::TypedElement,
    UML2::ParameterSet,
    Trigger,
    UML2::MessageTrigger,
    UML2::ChangeTrigger,
    UML2::TimeTrigger,
    BehavioredClassifier,
    UML2::Class,
    UML2::UseCase,
    WriteVariableAction,
    UML2::AddVariableValueAction,
    UML2::RemoveVariableValueAction,
    Feature,
    UML2::Connector,
    Vertex,
    UML2::Pseudostate,
    RedefinableElement,
    UML2::ActivityNode,
    UML2::ActivityEdge,
    Namespace,
    UML2::BehavioralFeature,
    UML2::Region,
    UML2::Classifier,
    UML2::State,
    Classifier,
    UML2::StructuredClassifier,
    UML2::Association,
    UML2::BehavioredClassifier,
    UML2::Actor,
    Dependency,
    UML2::Permission,
    UML2::Deployment,
    Transition,
    UML2::ProtocolTransition,
    Action,
    UML2::LinkAction,
    UML2::StartOwnedBehaviorAction,
    UML2::ClearAssociationAction,
    UML2::CreateObjectAction,
    UML2::ReadExtentAction,
    UML2::InvocationAction,
    UML2::ApplyFunctionAction,
    UML2::TestIdentityAction,
    UML2::DestroyObjectAction,
    ObjectNode,
    UML2::CentralBufferNode,
    UML2::ActivityParameterNode,
    UML2::ExpansionNode,
    VariableAction,
    UML2::WriteVariableAction,
    StructuralFeature,
    UML2::Property,
    UML2::Lifeline,
    UML2::ReadStructuralFeatureAction,
    UML2::GeneralizationSet,
    UML2::InitialNode,
    UML2::SendSignalAction,
    UML2::FinalNode,
    UML2::RaiseExceptionAction,
    Constraint,
    UML2::InteractionConstraint,
    UML2::IntervalConstraint,
    UML2::ClearVariableAction,
    UML2::Constraint,
    UML2::ReadLinkObjectEndQualifierAction,
    UML2::Message,
    UML2::RedefinableElement,
    UML2::Pin,
    UML2::AcceptEventAction,
    UML2::TemplateableClassifier,
    InputPin,
    UML2::ValuePin,
    UML2::ReadIsClassifiedObjectAction,
    UML2::ReadVariableAction,
    UML2::Dependency,
    UML2::Artifact,
    UML2::ConnectableElement,
    UML2::AddStructuralFeatureValueAction,
    UML2::ReadLinkObjectEndAction,
    UML2::DataType,
    UML2::Vertex,
    UML2::Behavior,
    UML2::ForkNode,
    UML2::ValueSpecification,
    UML2::MessageEnd,
    CreateLinkAction,
    UML2::CreateLinkObjectAction,
    UML2::StructuredActivityNode,
    UML2::StructuralFeature,
    UML2::DurationInterval,
    UML2::Signal,
    UML2::ReplyAction,
    UML2::Trigger,
    UML2::ConnectionPointReference,
    StructuredClassifier,
    UML2::Collaboration,
    UML2::EncapsulatedClassifier,
    UML2::VariableAction,
    UML2::AnyTrigger,
    UML2::LiteralBoolean,
    UML2::InformationItem,
    UML2::InteractionOperand,
    UML2::Namespace,
    UML2::CallBehaviorAction,
    InteractionOccurrence,
    UML2::PartDecomposition,
    UML2::ActivityFinalNode,
    UML2::Feature,
    UML2::LiteralNull,
    UML2::DeploymentTarget,
    OpaqueExpression,
    UML2::Expression,
    UML2::OutputPin,
    UML2::Node,
    UML2::SendObjectAction,
    UML2::RemoveStructuralFeatureValueAction,
    UML2::PrimitiveFunction,
    EventOccurrence,
    UML2::Stop,
    UML2::Interval,
    UML2::Type,
    UML2::StateMachine,
    UML2::ConditionalNode,
    UML2::CallTrigger,
    UML2::ParameterableClassifier,
    UML2::ExecutionOccurrence,
    IntervalConstraint,
    UML2::TimeConstraint,
    UML2::DurationConstraint,
    UML2::BroadcastSignalAction,
    BehavioralFeature,
    UML2::Operation,
    UML2::Reception,
    UML2::Interface,
    UML2::Transition,
    UML2::RedefinableTemplateSignature,
    UML2::ExtensionEnd,
    UML2::ReadLinkAction,
    CentralBufferNode,
    UML2::DataStoreNode,
    ExecutableNode,
    UML2::Action,
    UML2::InformationFlow,
    UML2::Enumeration,
    UML2::Package,
    UML2::Continuation,
    UML2::Usage,
    UML2::ClearStructuralFeatureAction,
    UML2::Abstraction,
    UML2::ReclassifyObjectAction,
    UML2::InstanceValue,
    UML2::ReadSelfAction,
    WriteLinkAction,
    UML2::DestroyLinkAction,
    UML2::CreateLinkAction,
    UML2::TimeExpression,
    UML2::MergeNode,
    UML2::PackageableElement,
    Association,
    UML2::AssociationClass,
    UML2::CommunicationPath,
    UML2::Extension,
    UML2::Duration,
    Artifact,
    UML2::DeploymentSpecification,
    StateMachine,
    UML2::ProtocolStateMachine,
    UML2::Extend,
    UML2::TimeObservationAction,
    UML2::StructuralFeatureAction,
    UML2::LoopNode,
    UML2::Device,
    Abstraction,
    UML2::Realization,
    UML2::Manifestation,
    UML2::Stereotype,
    ActivityNode,
    UML2::ObjectNode,
    UML2::ControlNode,
    UML2::ExecutableNode,
    MessageEnd,
    UML2::EventOccurrence,
    UML2::Gate,
    UML2::ExtensionPoint,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallOperationAction)


def test_uml2::calloperationaction_constructor_exists():
    assert callable(UML2::CallOperationAction.__init__)


def test_uml2::calloperationaction_constructor_args():
    sig = inspect.signature(UML2::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::callaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallAction)


def test_uml2::callaction_constructor_exists():
    assert callable(UML2::CallAction.__init__)


def test_uml2::callaction_constructor_args():
    sig = inspect.signature(UML2::CallAction.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2::port_is_not_abstract():
    assert not inspect.isabstract(UML2::Port)


def test_uml2::port_constructor_exists():
    assert callable(UML2::Port.__init__)


def test_uml2::port_constructor_args():
    sig = inspect.signature(UML2::Port.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2::component_is_not_abstract():
    assert not inspect.isabstract(UML2::Component)


def test_uml2::component_constructor_exists():
    assert callable(UML2::Component.__init__)


def test_uml2::component_constructor_args():
    sig = inspect.signature(UML2::Component.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2::InputPin)


def test_uml2::inputpin_constructor_exists():
    assert callable(UML2::InputPin.__init__)


def test_uml2::inputpin_constructor_args():
    sig = inspect.signature(UML2::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteLinkAction)


def test_uml2::writelinkaction_constructor_exists():
    assert callable(UML2::WriteLinkAction.__init__)


def test_uml2::writelinkaction_constructor_args():
    sig = inspect.signature(UML2::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_messagetrigger_is_not_abstract():
    assert not inspect.isabstract(MessageTrigger)


def test_messagetrigger_constructor_exists():
    assert callable(MessageTrigger.__init__)


def test_messagetrigger_constructor_args():
    sig = inspect.signature(MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::signaltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::SignalTrigger)


def test_uml2::signaltrigger_constructor_exists():
    assert callable(UML2::SignalTrigger.__init__)


def test_uml2::signaltrigger_constructor_args():
    sig = inspect.signature(UML2::SignalTrigger.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AcceptCallAction)


def test_uml2::acceptcallaction_constructor_exists():
    assert callable(UML2::AcceptCallAction.__init__)


def test_uml2::acceptcallaction_constructor_args():
    sig = inspect.signature(UML2::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activity_is_not_abstract():
    assert not inspect.isabstract(UML2::Activity)


def test_uml2::activity_constructor_exists():
    assert callable(UML2::Activity.__init__)


def test_uml2::activity_constructor_args():
    sig = inspect.signature(UML2::Activity.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameter_is_not_abstract():
    assert not inspect.isabstract(UML2::Parameter)


def test_uml2::parameter_constructor_exists():
    assert callable(UML2::Parameter.__init__)


def test_uml2::parameter_constructor_args():
    sig = inspect.signature(UML2::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2::variable_is_not_abstract():
    assert not inspect.isabstract(UML2::Variable)


def test_uml2::variable_constructor_exists():
    assert callable(UML2::Variable.__init__)


def test_uml2::variable_constructor_args():
    sig = inspect.signature(UML2::Variable.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml2::controlflow_is_not_abstract():
    assert not inspect.isabstract(UML2::ControlFlow)


def test_uml2::controlflow_constructor_exists():
    assert callable(UML2::ControlFlow.__init__)


def test_uml2::controlflow_constructor_args():
    sig = inspect.signature(UML2::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2::objectflow_is_not_abstract():
    assert not inspect.isabstract(UML2::ObjectFlow)


def test_uml2::objectflow_constructor_exists():
    assert callable(UML2::ObjectFlow.__init__)


def test_uml2::objectflow_constructor_args():
    sig = inspect.signature(UML2::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteStructuralFeatureAction)


def test_uml2::writestructuralfeatureaction_constructor_exists():
    assert callable(UML2::WriteStructuralFeatureAction.__init__)


def test_uml2::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2::model_is_not_abstract():
    assert not inspect.isabstract(UML2::Model)


def test_uml2::model_constructor_exists():
    assert callable(UML2::Model.__init__)


def test_uml2::model_constructor_args():
    sig = inspect.signature(UML2::Model.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::instancespecification_is_not_abstract():
    assert not inspect.isabstract(UML2::InstanceSpecification)


def test_uml2::instancespecification_constructor_exists():
    assert callable(UML2::InstanceSpecification.__init__)


def test_uml2::instancespecification_constructor_args():
    sig = inspect.signature(UML2::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeInterval)


def test_uml2::timeinterval_constructor_exists():
    assert callable(UML2::TimeInterval.__init__)


def test_uml2::timeinterval_constructor_args():
    sig = inspect.signature(UML2::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(UML2::EnumerationLiteral)


def test_uml2::enumerationliteral_constructor_exists():
    assert callable(UML2::EnumerationLiteral.__init__)


def test_uml2::enumerationliteral_constructor_args():
    sig = inspect.signature(UML2::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2::PrimitiveType)


def test_uml2::primitivetype_constructor_exists():
    assert callable(UML2::PrimitiveType.__init__)


def test_uml2::primitivetype_constructor_args():
    sig = inspect.signature(UML2::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml2::substitution_is_not_abstract():
    assert not inspect.isabstract(UML2::Substitution)


def test_uml2::substitution_constructor_exists():
    assert callable(UML2::Substitution.__init__)


def test_uml2::substitution_constructor_args():
    sig = inspect.signature(UML2::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2::implementation_is_not_abstract():
    assert not inspect.isabstract(UML2::Implementation)


def test_uml2::implementation_constructor_exists():
    assert callable(UML2::Implementation.__init__)


def test_uml2::implementation_constructor_args():
    sig = inspect.signature(UML2::Implementation.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutionEnvironment)


def test_uml2::executionenvironment_constructor_exists():
    assert callable(UML2::ExecutionEnvironment.__init__)


def test_uml2::executionenvironment_constructor_args():
    sig = inspect.signature(UML2::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::joinnode_is_not_abstract():
    assert not inspect.isabstract(UML2::JoinNode)


def test_uml2::joinnode_constructor_exists():
    assert callable(UML2::JoinNode.__init__)


def test_uml2::joinnode_constructor_args():
    sig = inspect.signature(UML2::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::decisionnode_is_not_abstract():
    assert not inspect.isabstract(UML2::DecisionNode)


def test_uml2::decisionnode_constructor_exists():
    assert callable(UML2::DecisionNode.__init__)


def test_uml2::decisionnode_constructor_args():
    sig = inspect.signature(UML2::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_uml2::finalstate_is_not_abstract():
    assert not inspect.isabstract(UML2::FinalState)


def test_uml2::finalstate_constructor_exists():
    assert callable(UML2::FinalState.__init__)


def test_uml2::finalstate_constructor_args():
    sig = inspect.signature(UML2::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationObservationAction)


def test_uml2::durationobservationaction_constructor_exists():
    assert callable(UML2::DurationObservationAction.__init__)


def test_uml2::durationobservationaction_constructor_args():
    sig = inspect.signature(UML2::DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::generalization_is_not_abstract():
    assert not inspect.isabstract(UML2::Generalization)


def test_uml2::generalization_constructor_exists():
    assert callable(UML2::Generalization.__init__)


def test_uml2::generalization_constructor_args():
    sig = inspect.signature(UML2::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_uml2::namedelement_is_not_abstract():
    assert not inspect.isabstract(UML2::NamedElement)


def test_uml2::namedelement_constructor_exists():
    assert callable(UML2::NamedElement.__init__)


def test_uml2::namedelement_constructor_args():
    sig = inspect.signature(UML2::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml2::namedelement_has_visibility():
    assert hasattr(UML2::NamedElement, "visibility")
    descriptor = None
    for klass in UML2::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralSpecification)


def test_uml2::literalspecification_constructor_exists():
    assert callable(UML2::LiteralSpecification.__init__)


def test_uml2::literalspecification_constructor_args():
    sig = inspect.signature(UML2::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::OpaqueExpression)


def test_uml2::opaqueexpression_constructor_exists():
    assert callable(UML2::OpaqueExpression.__init__)


def test_uml2::opaqueexpression_constructor_args():
    sig = inspect.signature(UML2::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::profile_is_not_abstract():
    assert not inspect.isabstract(UML2::Profile)


def test_uml2::profile_constructor_exists():
    assert callable(UML2::Profile.__init__)


def test_uml2::profile_constructor_args():
    sig = inspect.signature(UML2::Profile.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML2::ExpansionRegion)


def test_uml2::expansionregion_constructor_exists():
    assert callable(UML2::ExpansionRegion.__init__)


def test_uml2::expansionregion_constructor_args():
    sig = inspect.signature(UML2::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interaction_is_not_abstract():
    assert not inspect.isabstract(UML2::Interaction)


def test_uml2::interaction_constructor_exists():
    assert callable(UML2::Interaction.__init__)


def test_uml2::interaction_constructor_args():
    sig = inspect.signature(UML2::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(UML2::CombinedFragment)


def test_uml2::combinedfragment_constructor_exists():
    assert callable(UML2::CombinedFragment.__init__)


def test_uml2::combinedfragment_constructor_args():
    sig = inspect.signature(UML2::CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionOccurrence)


def test_uml2::interactionoccurrence_constructor_exists():
    assert callable(UML2::InteractionOccurrence.__init__)


def test_uml2::interactionoccurrence_constructor_args():
    sig = inspect.signature(UML2::InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stateinvariant_is_not_abstract():
    assert not inspect.isabstract(UML2::StateInvariant)


def test_uml2::stateinvariant_constructor_exists():
    assert callable(UML2::StateInvariant.__init__)


def test_uml2::stateinvariant_constructor_args():
    sig = inspect.signature(UML2::StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::FlowFinalNode)


def test_uml2::flowfinalnode_constructor_exists():
    assert callable(UML2::FlowFinalNode.__init__)


def test_uml2::flowfinalnode_constructor_args():
    sig = inspect.signature(UML2::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalinteger_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralInteger)


def test_uml2::literalinteger_constructor_exists():
    assert callable(UML2::LiteralInteger.__init__)


def test_uml2::literalinteger_constructor_args():
    sig = inspect.signature(UML2::LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralUnlimitedNatural)


def test_uml2::literalunlimitednatural_constructor_exists():
    assert callable(UML2::LiteralUnlimitedNatural.__init__)


def test_uml2::literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralString)


def test_uml2::literalstring_constructor_exists():
    assert callable(UML2::LiteralString.__init__)


def test_uml2::literalstring_constructor_args():
    sig = inspect.signature(UML2::LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionFragment)


def test_uml2::interactionfragment_constructor_exists():
    assert callable(UML2::InteractionFragment.__init__)


def test_uml2::interactionfragment_constructor_args():
    sig = inspect.signature(UML2::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::collaborationoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::CollaborationOccurrence)


def test_uml2::collaborationoccurrence_constructor_exists():
    assert callable(UML2::CollaborationOccurrence.__init__)


def test_uml2::collaborationoccurrence_constructor_args():
    sig = inspect.signature(UML2::CollaborationOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activitypartition_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityPartition)


def test_uml2::activitypartition_constructor_exists():
    assert callable(UML2::ActivityPartition.__init__)


def test_uml2::activitypartition_constructor_args():
    sig = inspect.signature(UML2::ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml2::include_is_not_abstract():
    assert not inspect.isabstract(UML2::Include)


def test_uml2::include_constructor_exists():
    assert callable(UML2::Include.__init__)


def test_uml2::include_constructor_args():
    sig = inspect.signature(UML2::Include.__init__)
    params = list(sig.parameters.keys())



def test_uml2::generalordering_is_not_abstract():
    assert not inspect.isabstract(UML2::GeneralOrdering)


def test_uml2::generalordering_constructor_exists():
    assert callable(UML2::GeneralOrdering.__init__)


def test_uml2::generalordering_constructor_args():
    sig = inspect.signature(UML2::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deployedartifact_is_not_abstract():
    assert not inspect.isabstract(UML2::DeployedArtifact)


def test_uml2::deployedartifact_constructor_exists():
    assert callable(UML2::DeployedArtifact.__init__)


def test_uml2::deployedartifact_constructor_args():
    sig = inspect.signature(UML2::DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2::TypedElement)


def test_uml2::typedelement_constructor_exists():
    assert callable(UML2::TypedElement.__init__)


def test_uml2::typedelement_constructor_args():
    sig = inspect.signature(UML2::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterset_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterSet)


def test_uml2::parameterset_constructor_exists():
    assert callable(UML2::ParameterSet.__init__)


def test_uml2::parameterset_constructor_args():
    sig = inspect.signature(UML2::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::messagetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::MessageTrigger)


def test_uml2::messagetrigger_constructor_exists():
    assert callable(UML2::MessageTrigger.__init__)


def test_uml2::messagetrigger_constructor_args():
    sig = inspect.signature(UML2::MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::changetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::ChangeTrigger)


def test_uml2::changetrigger_constructor_exists():
    assert callable(UML2::ChangeTrigger.__init__)


def test_uml2::changetrigger_constructor_args():
    sig = inspect.signature(UML2::ChangeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeTrigger)


def test_uml2::timetrigger_constructor_exists():
    assert callable(UML2::TimeTrigger.__init__)


def test_uml2::timetrigger_constructor_args():
    sig = inspect.signature(UML2::TimeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::class_is_not_abstract():
    assert not inspect.isabstract(UML2::Class)


def test_uml2::class_constructor_exists():
    assert callable(UML2::Class.__init__)


def test_uml2::class_constructor_args():
    sig = inspect.signature(UML2::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2::UseCase)


def test_uml2::usecase_constructor_exists():
    assert callable(UML2::UseCase.__init__)


def test_uml2::usecase_constructor_args():
    sig = inspect.signature(UML2::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AddVariableValueAction)


def test_uml2::addvariablevalueaction_constructor_exists():
    assert callable(UML2::AddVariableValueAction.__init__)


def test_uml2::addvariablevalueaction_constructor_args():
    sig = inspect.signature(UML2::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RemoveVariableValueAction)


def test_uml2::removevariablevalueaction_constructor_exists():
    assert callable(UML2::RemoveVariableValueAction.__init__)


def test_uml2::removevariablevalueaction_constructor_args():
    sig = inspect.signature(UML2::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::connector_is_not_abstract():
    assert not inspect.isabstract(UML2::Connector)


def test_uml2::connector_constructor_exists():
    assert callable(UML2::Connector.__init__)


def test_uml2::connector_constructor_args():
    sig = inspect.signature(UML2::Connector.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2::pseudostate_is_not_abstract():
    assert not inspect.isabstract(UML2::Pseudostate)


def test_uml2::pseudostate_constructor_exists():
    assert callable(UML2::Pseudostate.__init__)


def test_uml2::pseudostate_constructor_args():
    sig = inspect.signature(UML2::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activitynode_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityNode)


def test_uml2::activitynode_constructor_exists():
    assert callable(UML2::ActivityNode.__init__)


def test_uml2::activitynode_constructor_args():
    sig = inspect.signature(UML2::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activityedge_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityEdge)


def test_uml2::activityedge_constructor_exists():
    assert callable(UML2::ActivityEdge.__init__)


def test_uml2::activityedge_constructor_args():
    sig = inspect.signature(UML2::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioralFeature)


def test_uml2::behavioralfeature_constructor_exists():
    assert callable(UML2::BehavioralFeature.__init__)


def test_uml2::behavioralfeature_constructor_args():
    sig = inspect.signature(UML2::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::region_is_not_abstract():
    assert not inspect.isabstract(UML2::Region)


def test_uml2::region_constructor_exists():
    assert callable(UML2::Region.__init__)


def test_uml2::region_constructor_args():
    sig = inspect.signature(UML2::Region.__init__)
    params = list(sig.parameters.keys())



def test_uml2::classifier_is_not_abstract():
    assert not inspect.isabstract(UML2::Classifier)


def test_uml2::classifier_constructor_exists():
    assert callable(UML2::Classifier.__init__)


def test_uml2::classifier_constructor_args():
    sig = inspect.signature(UML2::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::state_is_not_abstract():
    assert not inspect.isabstract(UML2::State)


def test_uml2::state_constructor_exists():
    assert callable(UML2::State.__init__)


def test_uml2::state_constructor_args():
    sig = inspect.signature(UML2::State.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuredClassifier)


def test_uml2::structuredclassifier_constructor_exists():
    assert callable(UML2::StructuredClassifier.__init__)


def test_uml2::structuredclassifier_constructor_args():
    sig = inspect.signature(UML2::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::association_is_not_abstract():
    assert not inspect.isabstract(UML2::Association)


def test_uml2::association_constructor_exists():
    assert callable(UML2::Association.__init__)


def test_uml2::association_constructor_args():
    sig = inspect.signature(UML2::Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioredClassifier)


def test_uml2::behavioredclassifier_constructor_exists():
    assert callable(UML2::BehavioredClassifier.__init__)


def test_uml2::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::actor_is_not_abstract():
    assert not inspect.isabstract(UML2::Actor)


def test_uml2::actor_constructor_exists():
    assert callable(UML2::Actor.__init__)


def test_uml2::actor_constructor_args():
    sig = inspect.signature(UML2::Actor.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml2::permission_is_not_abstract():
    assert not inspect.isabstract(UML2::Permission)


def test_uml2::permission_constructor_exists():
    assert callable(UML2::Permission.__init__)


def test_uml2::permission_constructor_args():
    sig = inspect.signature(UML2::Permission.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deployment_is_not_abstract():
    assert not inspect.isabstract(UML2::Deployment)


def test_uml2::deployment_constructor_exists():
    assert callable(UML2::Deployment.__init__)


def test_uml2::deployment_constructor_args():
    sig = inspect.signature(UML2::Deployment.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml2::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(UML2::ProtocolTransition)


def test_uml2::protocoltransition_constructor_exists():
    assert callable(UML2::ProtocolTransition.__init__)


def test_uml2::protocoltransition_constructor_args():
    sig = inspect.signature(UML2::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2::linkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::LinkAction)


def test_uml2::linkaction_constructor_exists():
    assert callable(UML2::LinkAction.__init__)


def test_uml2::linkaction_constructor_args():
    sig = inspect.signature(UML2::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::startownedbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2::StartOwnedBehaviorAction)


def test_uml2::startownedbehavioraction_constructor_exists():
    assert callable(UML2::StartOwnedBehaviorAction.__init__)


def test_uml2::startownedbehavioraction_constructor_args():
    sig = inspect.signature(UML2::StartOwnedBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearAssociationAction)


def test_uml2::clearassociationaction_constructor_exists():
    assert callable(UML2::ClearAssociationAction.__init__)


def test_uml2::clearassociationaction_constructor_args():
    sig = inspect.signature(UML2::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateObjectAction)


def test_uml2::createobjectaction_constructor_exists():
    assert callable(UML2::CreateObjectAction.__init__)


def test_uml2::createobjectaction_constructor_args():
    sig = inspect.signature(UML2::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readextentaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadExtentAction)


def test_uml2::readextentaction_constructor_exists():
    assert callable(UML2::ReadExtentAction.__init__)


def test_uml2::readextentaction_constructor_args():
    sig = inspect.signature(UML2::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::invocationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::InvocationAction)


def test_uml2::invocationaction_constructor_exists():
    assert callable(UML2::InvocationAction.__init__)


def test_uml2::invocationaction_constructor_args():
    sig = inspect.signature(UML2::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::applyfunctionaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ApplyFunctionAction)


def test_uml2::applyfunctionaction_constructor_exists():
    assert callable(UML2::ApplyFunctionAction.__init__)


def test_uml2::applyfunctionaction_constructor_args():
    sig = inspect.signature(UML2::ApplyFunctionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2::TestIdentityAction)


def test_uml2::testidentityaction_constructor_exists():
    assert callable(UML2::TestIdentityAction.__init__)


def test_uml2::testidentityaction_constructor_args():
    sig = inspect.signature(UML2::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DestroyObjectAction)


def test_uml2::destroyobjectaction_constructor_exists():
    assert callable(UML2::DestroyObjectAction.__init__)


def test_uml2::destroyobjectaction_constructor_args():
    sig = inspect.signature(UML2::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2::CentralBufferNode)


def test_uml2::centralbuffernode_constructor_exists():
    assert callable(UML2::CentralBufferNode.__init__)


def test_uml2::centralbuffernode_constructor_args():
    sig = inspect.signature(UML2::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityParameterNode)


def test_uml2::activityparameternode_constructor_exists():
    assert callable(UML2::ActivityParameterNode.__init__)


def test_uml2::activityparameternode_constructor_args():
    sig = inspect.signature(UML2::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ExpansionNode)


def test_uml2::expansionnode_constructor_exists():
    assert callable(UML2::ExpansionNode.__init__)


def test_uml2::expansionnode_constructor_args():
    sig = inspect.signature(UML2::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteVariableAction)


def test_uml2::writevariableaction_constructor_exists():
    assert callable(UML2::WriteVariableAction.__init__)


def test_uml2::writevariableaction_constructor_args():
    sig = inspect.signature(UML2::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::property_is_not_abstract():
    assert not inspect.isabstract(UML2::Property)


def test_uml2::property_constructor_exists():
    assert callable(UML2::Property.__init__)


def test_uml2::property_constructor_args():
    sig = inspect.signature(UML2::Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2::lifeline_is_not_abstract():
    assert not inspect.isabstract(UML2::Lifeline)


def test_uml2::lifeline_constructor_exists():
    assert callable(UML2::Lifeline.__init__)


def test_uml2::lifeline_constructor_args():
    sig = inspect.signature(UML2::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadStructuralFeatureAction)


def test_uml2::readstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ReadStructuralFeatureAction.__init__)


def test_uml2::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::generalizationset_is_not_abstract():
    assert not inspect.isabstract(UML2::GeneralizationSet)


def test_uml2::generalizationset_constructor_exists():
    assert callable(UML2::GeneralizationSet.__init__)


def test_uml2::generalizationset_constructor_args():
    sig = inspect.signature(UML2::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_uml2::initialnode_is_not_abstract():
    assert not inspect.isabstract(UML2::InitialNode)


def test_uml2::initialnode_constructor_exists():
    assert callable(UML2::InitialNode.__init__)


def test_uml2::initialnode_constructor_args():
    sig = inspect.signature(UML2::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2::SendSignalAction)


def test_uml2::sendsignalaction_constructor_exists():
    assert callable(UML2::SendSignalAction.__init__)


def test_uml2::sendsignalaction_constructor_args():
    sig = inspect.signature(UML2::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::finalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::FinalNode)


def test_uml2::finalnode_constructor_exists():
    assert callable(UML2::FinalNode.__init__)


def test_uml2::finalnode_constructor_args():
    sig = inspect.signature(UML2::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RaiseExceptionAction)


def test_uml2::raiseexceptionaction_constructor_exists():
    assert callable(UML2::RaiseExceptionAction.__init__)


def test_uml2::raiseexceptionaction_constructor_args():
    sig = inspect.signature(UML2::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionConstraint)


def test_uml2::interactionconstraint_constructor_exists():
    assert callable(UML2::InteractionConstraint.__init__)


def test_uml2::interactionconstraint_constructor_args():
    sig = inspect.signature(UML2::InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::IntervalConstraint)


def test_uml2::intervalconstraint_constructor_exists():
    assert callable(UML2::IntervalConstraint.__init__)


def test_uml2::intervalconstraint_constructor_args():
    sig = inspect.signature(UML2::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearVariableAction)


def test_uml2::clearvariableaction_constructor_exists():
    assert callable(UML2::ClearVariableAction.__init__)


def test_uml2::clearvariableaction_constructor_args():
    sig = inspect.signature(UML2::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::constraint_is_not_abstract():
    assert not inspect.isabstract(UML2::Constraint)


def test_uml2::constraint_constructor_exists():
    assert callable(UML2::Constraint.__init__)


def test_uml2::constraint_constructor_args():
    sig = inspect.signature(UML2::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkObjectEndQualifierAction)


def test_uml2::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UML2::ReadLinkObjectEndQualifierAction.__init__)


def test_uml2::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::message_is_not_abstract():
    assert not inspect.isabstract(UML2::Message)


def test_uml2::message_constructor_exists():
    assert callable(UML2::Message.__init__)


def test_uml2::message_constructor_args():
    sig = inspect.signature(UML2::Message.__init__)
    params = list(sig.parameters.keys())



def test_uml2::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::RedefinableElement)


def test_uml2::redefinableelement_constructor_exists():
    assert callable(UML2::RedefinableElement.__init__)


def test_uml2::redefinableelement_constructor_args():
    sig = inspect.signature(UML2::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::pin_is_not_abstract():
    assert not inspect.isabstract(UML2::Pin)


def test_uml2::pin_constructor_exists():
    assert callable(UML2::Pin.__init__)


def test_uml2::pin_constructor_args():
    sig = inspect.signature(UML2::Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AcceptEventAction)


def test_uml2::accepteventaction_constructor_exists():
    assert callable(UML2::AcceptEventAction.__init__)


def test_uml2::accepteventaction_constructor_args():
    sig = inspect.signature(UML2::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateableClassifier)


def test_uml2::templateableclassifier_constructor_exists():
    assert callable(UML2::TemplateableClassifier.__init__)


def test_uml2::templateableclassifier_constructor_args():
    sig = inspect.signature(UML2::TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2::ValuePin)


def test_uml2::valuepin_constructor_exists():
    assert callable(UML2::ValuePin.__init__)


def test_uml2::valuepin_constructor_args():
    sig = inspect.signature(UML2::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadIsClassifiedObjectAction)


def test_uml2::readisclassifiedobjectaction_constructor_exists():
    assert callable(UML2::ReadIsClassifiedObjectAction.__init__)


def test_uml2::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UML2::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadVariableAction)


def test_uml2::readvariableaction_constructor_exists():
    assert callable(UML2::ReadVariableAction.__init__)


def test_uml2::readvariableaction_constructor_args():
    sig = inspect.signature(UML2::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::dependency_is_not_abstract():
    assert not inspect.isabstract(UML2::Dependency)


def test_uml2::dependency_constructor_exists():
    assert callable(UML2::Dependency.__init__)


def test_uml2::dependency_constructor_args():
    sig = inspect.signature(UML2::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml2::artifact_is_not_abstract():
    assert not inspect.isabstract(UML2::Artifact)


def test_uml2::artifact_constructor_exists():
    assert callable(UML2::Artifact.__init__)


def test_uml2::artifact_constructor_args():
    sig = inspect.signature(UML2::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::connectableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::ConnectableElement)


def test_uml2::connectableelement_constructor_exists():
    assert callable(UML2::ConnectableElement.__init__)


def test_uml2::connectableelement_constructor_args():
    sig = inspect.signature(UML2::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AddStructuralFeatureValueAction)


def test_uml2::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::AddStructuralFeatureValueAction.__init__)


def test_uml2::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkObjectEndAction)


def test_uml2::readlinkobjectendaction_constructor_exists():
    assert callable(UML2::ReadLinkObjectEndAction.__init__)


def test_uml2::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::datatype_is_not_abstract():
    assert not inspect.isabstract(UML2::DataType)


def test_uml2::datatype_constructor_exists():
    assert callable(UML2::DataType.__init__)


def test_uml2::datatype_constructor_args():
    sig = inspect.signature(UML2::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::vertex_is_not_abstract():
    assert not inspect.isabstract(UML2::Vertex)


def test_uml2::vertex_constructor_exists():
    assert callable(UML2::Vertex.__init__)


def test_uml2::vertex_constructor_args():
    sig = inspect.signature(UML2::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2::Behavior)


def test_uml2::behavior_constructor_exists():
    assert callable(UML2::Behavior.__init__)


def test_uml2::behavior_constructor_args():
    sig = inspect.signature(UML2::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::forknode_is_not_abstract():
    assert not inspect.isabstract(UML2::ForkNode)


def test_uml2::forknode_constructor_exists():
    assert callable(UML2::ForkNode.__init__)


def test_uml2::forknode_constructor_args():
    sig = inspect.signature(UML2::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2::ValueSpecification)


def test_uml2::valuespecification_constructor_exists():
    assert callable(UML2::ValueSpecification.__init__)


def test_uml2::valuespecification_constructor_args():
    sig = inspect.signature(UML2::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::messageend_is_not_abstract():
    assert not inspect.isabstract(UML2::MessageEnd)


def test_uml2::messageend_constructor_exists():
    assert callable(UML2::MessageEnd.__init__)


def test_uml2::messageend_constructor_args():
    sig = inspect.signature(UML2::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateLinkObjectAction)


def test_uml2::createlinkobjectaction_constructor_exists():
    assert callable(UML2::CreateLinkObjectAction.__init__)


def test_uml2::createlinkobjectaction_constructor_args():
    sig = inspect.signature(UML2::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuredActivityNode)


def test_uml2::structuredactivitynode_constructor_exists():
    assert callable(UML2::StructuredActivityNode.__init__)


def test_uml2::structuredactivitynode_constructor_args():
    sig = inspect.signature(UML2::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeature)


def test_uml2::structuralfeature_constructor_exists():
    assert callable(UML2::StructuralFeature.__init__)


def test_uml2::structuralfeature_constructor_args():
    sig = inspect.signature(UML2::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationInterval)


def test_uml2::durationinterval_constructor_exists():
    assert callable(UML2::DurationInterval.__init__)


def test_uml2::durationinterval_constructor_args():
    sig = inspect.signature(UML2::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::signal_is_not_abstract():
    assert not inspect.isabstract(UML2::Signal)


def test_uml2::signal_constructor_exists():
    assert callable(UML2::Signal.__init__)


def test_uml2::signal_constructor_args():
    sig = inspect.signature(UML2::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2::replyaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReplyAction)


def test_uml2::replyaction_constructor_exists():
    assert callable(UML2::ReplyAction.__init__)


def test_uml2::replyaction_constructor_args():
    sig = inspect.signature(UML2::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::trigger_is_not_abstract():
    assert not inspect.isabstract(UML2::Trigger)


def test_uml2::trigger_constructor_exists():
    assert callable(UML2::Trigger.__init__)


def test_uml2::trigger_constructor_args():
    sig = inspect.signature(UML2::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(UML2::ConnectionPointReference)


def test_uml2::connectionpointreference_constructor_exists():
    assert callable(UML2::ConnectionPointReference.__init__)


def test_uml2::connectionpointreference_constructor_args():
    sig = inspect.signature(UML2::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2::Collaboration)


def test_uml2::collaboration_constructor_exists():
    assert callable(UML2::Collaboration.__init__)


def test_uml2::collaboration_constructor_args():
    sig = inspect.signature(UML2::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::EncapsulatedClassifier)


def test_uml2::encapsulatedclassifier_constructor_exists():
    assert callable(UML2::EncapsulatedClassifier.__init__)


def test_uml2::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::variableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::VariableAction)


def test_uml2::variableaction_constructor_exists():
    assert callable(UML2::VariableAction.__init__)


def test_uml2::variableaction_constructor_args():
    sig = inspect.signature(UML2::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::anytrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::AnyTrigger)


def test_uml2::anytrigger_constructor_exists():
    assert callable(UML2::AnyTrigger.__init__)


def test_uml2::anytrigger_constructor_args():
    sig = inspect.signature(UML2::AnyTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralBoolean)


def test_uml2::literalboolean_constructor_exists():
    assert callable(UML2::LiteralBoolean.__init__)


def test_uml2::literalboolean_constructor_args():
    sig = inspect.signature(UML2::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml2::informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2::InformationItem)


def test_uml2::informationitem_constructor_exists():
    assert callable(UML2::InformationItem.__init__)


def test_uml2::informationitem_constructor_args():
    sig = inspect.signature(UML2::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionOperand)


def test_uml2::interactionoperand_constructor_exists():
    assert callable(UML2::InteractionOperand.__init__)


def test_uml2::interactionoperand_constructor_args():
    sig = inspect.signature(UML2::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml2::namespace_is_not_abstract():
    assert not inspect.isabstract(UML2::Namespace)


def test_uml2::namespace_constructor_exists():
    assert callable(UML2::Namespace.__init__)


def test_uml2::namespace_constructor_args():
    sig = inspect.signature(UML2::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallBehaviorAction)


def test_uml2::callbehavioraction_constructor_exists():
    assert callable(UML2::CallBehaviorAction.__init__)


def test_uml2::callbehavioraction_constructor_args():
    sig = inspect.signature(UML2::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(InteractionOccurrence)


def test_interactionoccurrence_constructor_exists():
    assert callable(InteractionOccurrence.__init__)


def test_interactionoccurrence_constructor_args():
    sig = inspect.signature(InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::partdecomposition_is_not_abstract():
    assert not inspect.isabstract(UML2::PartDecomposition)


def test_uml2::partdecomposition_constructor_exists():
    assert callable(UML2::PartDecomposition.__init__)


def test_uml2::partdecomposition_constructor_args():
    sig = inspect.signature(UML2::PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityFinalNode)


def test_uml2::activityfinalnode_constructor_exists():
    assert callable(UML2::ActivityFinalNode.__init__)


def test_uml2::activityfinalnode_constructor_args():
    sig = inspect.signature(UML2::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::feature_is_not_abstract():
    assert not inspect.isabstract(UML2::Feature)


def test_uml2::feature_constructor_exists():
    assert callable(UML2::Feature.__init__)


def test_uml2::feature_constructor_args():
    sig = inspect.signature(UML2::Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralNull)


def test_uml2::literalnull_constructor_exists():
    assert callable(UML2::LiteralNull.__init__)


def test_uml2::literalnull_constructor_args():
    sig = inspect.signature(UML2::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(UML2::DeploymentTarget)


def test_uml2::deploymenttarget_constructor_exists():
    assert callable(UML2::DeploymentTarget.__init__)


def test_uml2::deploymenttarget_constructor_args():
    sig = inspect.signature(UML2::DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::expression_is_not_abstract():
    assert not inspect.isabstract(UML2::Expression)


def test_uml2::expression_constructor_exists():
    assert callable(UML2::Expression.__init__)


def test_uml2::expression_constructor_args():
    sig = inspect.signature(UML2::Expression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2::OutputPin)


def test_uml2::outputpin_constructor_exists():
    assert callable(UML2::OutputPin.__init__)


def test_uml2::outputpin_constructor_args():
    sig = inspect.signature(UML2::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::node_is_not_abstract():
    assert not inspect.isabstract(UML2::Node)


def test_uml2::node_constructor_exists():
    assert callable(UML2::Node.__init__)


def test_uml2::node_constructor_args():
    sig = inspect.signature(UML2::Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::SendObjectAction)


def test_uml2::sendobjectaction_constructor_exists():
    assert callable(UML2::SendObjectAction.__init__)


def test_uml2::sendobjectaction_constructor_args():
    sig = inspect.signature(UML2::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RemoveStructuralFeatureValueAction)


def test_uml2::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::RemoveStructuralFeatureValueAction.__init__)


def test_uml2::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::primitivefunction_is_not_abstract():
    assert not inspect.isabstract(UML2::PrimitiveFunction)


def test_uml2::primitivefunction_constructor_exists():
    assert callable(UML2::PrimitiveFunction.__init__)


def test_uml2::primitivefunction_constructor_args():
    sig = inspect.signature(UML2::PrimitiveFunction.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stop_is_not_abstract():
    assert not inspect.isabstract(UML2::Stop)


def test_uml2::stop_constructor_exists():
    assert callable(UML2::Stop.__init__)


def test_uml2::stop_constructor_args():
    sig = inspect.signature(UML2::Stop.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interval_is_not_abstract():
    assert not inspect.isabstract(UML2::Interval)


def test_uml2::interval_constructor_exists():
    assert callable(UML2::Interval.__init__)


def test_uml2::interval_constructor_args():
    sig = inspect.signature(UML2::Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::type_is_not_abstract():
    assert not inspect.isabstract(UML2::Type)


def test_uml2::type_constructor_exists():
    assert callable(UML2::Type.__init__)


def test_uml2::type_constructor_args():
    sig = inspect.signature(UML2::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2::statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2::StateMachine)


def test_uml2::statemachine_constructor_exists():
    assert callable(UML2::StateMachine.__init__)


def test_uml2::statemachine_constructor_args():
    sig = inspect.signature(UML2::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ConditionalNode)


def test_uml2::conditionalnode_constructor_exists():
    assert callable(UML2::ConditionalNode.__init__)


def test_uml2::conditionalnode_constructor_args():
    sig = inspect.signature(UML2::ConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::calltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::CallTrigger)


def test_uml2::calltrigger_constructor_exists():
    assert callable(UML2::CallTrigger.__init__)


def test_uml2::calltrigger_constructor_args():
    sig = inspect.signature(UML2::CallTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterableClassifier)


def test_uml2::parameterableclassifier_constructor_exists():
    assert callable(UML2::ParameterableClassifier.__init__)


def test_uml2::parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2::ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::executionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutionOccurrence)


def test_uml2::executionoccurrence_constructor_exists():
    assert callable(UML2::ExecutionOccurrence.__init__)


def test_uml2::executionoccurrence_constructor_args():
    sig = inspect.signature(UML2::ExecutionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeConstraint)


def test_uml2::timeconstraint_constructor_exists():
    assert callable(UML2::TimeConstraint.__init__)


def test_uml2::timeconstraint_constructor_args():
    sig = inspect.signature(UML2::TimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationConstraint)


def test_uml2::durationconstraint_constructor_exists():
    assert callable(UML2::DurationConstraint.__init__)


def test_uml2::durationconstraint_constructor_args():
    sig = inspect.signature(UML2::DurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2::BroadcastSignalAction)


def test_uml2::broadcastsignalaction_constructor_exists():
    assert callable(UML2::BroadcastSignalAction.__init__)


def test_uml2::broadcastsignalaction_constructor_args():
    sig = inspect.signature(UML2::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::operation_is_not_abstract():
    assert not inspect.isabstract(UML2::Operation)


def test_uml2::operation_constructor_exists():
    assert callable(UML2::Operation.__init__)


def test_uml2::operation_constructor_args():
    sig = inspect.signature(UML2::Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2::reception_is_not_abstract():
    assert not inspect.isabstract(UML2::Reception)


def test_uml2::reception_constructor_exists():
    assert callable(UML2::Reception.__init__)


def test_uml2::reception_constructor_args():
    sig = inspect.signature(UML2::Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interface_is_not_abstract():
    assert not inspect.isabstract(UML2::Interface)


def test_uml2::interface_constructor_exists():
    assert callable(UML2::Interface.__init__)


def test_uml2::interface_constructor_args():
    sig = inspect.signature(UML2::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2::transition_is_not_abstract():
    assert not inspect.isabstract(UML2::Transition)


def test_uml2::transition_constructor_exists():
    assert callable(UML2::Transition.__init__)


def test_uml2::transition_constructor_args():
    sig = inspect.signature(UML2::Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml2::redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2::RedefinableTemplateSignature)


def test_uml2::redefinabletemplatesignature_constructor_exists():
    assert callable(UML2::RedefinableTemplateSignature.__init__)


def test_uml2::redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(UML2::RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionEnd)


def test_uml2::extensionend_constructor_exists():
    assert callable(UML2::ExtensionEnd.__init__)


def test_uml2::extensionend_constructor_args():
    sig = inspect.signature(UML2::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkAction)


def test_uml2::readlinkaction_constructor_exists():
    assert callable(UML2::ReadLinkAction.__init__)


def test_uml2::readlinkaction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML2::DataStoreNode)


def test_uml2::datastorenode_constructor_exists():
    assert callable(UML2::DataStoreNode.__init__)


def test_uml2::datastorenode_constructor_args():
    sig = inspect.signature(UML2::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::action_is_not_abstract():
    assert not inspect.isabstract(UML2::Action)


def test_uml2::action_constructor_exists():
    assert callable(UML2::Action.__init__)


def test_uml2::action_constructor_args():
    sig = inspect.signature(UML2::Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2::informationflow_is_not_abstract():
    assert not inspect.isabstract(UML2::InformationFlow)


def test_uml2::informationflow_constructor_exists():
    assert callable(UML2::InformationFlow.__init__)


def test_uml2::informationflow_constructor_args():
    sig = inspect.signature(UML2::InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2::enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2::Enumeration)


def test_uml2::enumeration_constructor_exists():
    assert callable(UML2::Enumeration.__init__)


def test_uml2::enumeration_constructor_args():
    sig = inspect.signature(UML2::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2::package_is_not_abstract():
    assert not inspect.isabstract(UML2::Package)


def test_uml2::package_constructor_exists():
    assert callable(UML2::Package.__init__)


def test_uml2::package_constructor_args():
    sig = inspect.signature(UML2::Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2::continuation_is_not_abstract():
    assert not inspect.isabstract(UML2::Continuation)


def test_uml2::continuation_constructor_exists():
    assert callable(UML2::Continuation.__init__)


def test_uml2::continuation_constructor_args():
    sig = inspect.signature(UML2::Continuation.__init__)
    params = list(sig.parameters.keys())



def test_uml2::usage_is_not_abstract():
    assert not inspect.isabstract(UML2::Usage)


def test_uml2::usage_constructor_exists():
    assert callable(UML2::Usage.__init__)


def test_uml2::usage_constructor_args():
    sig = inspect.signature(UML2::Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearStructuralFeatureAction)


def test_uml2::clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ClearStructuralFeatureAction.__init__)


def test_uml2::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::abstraction_is_not_abstract():
    assert not inspect.isabstract(UML2::Abstraction)


def test_uml2::abstraction_constructor_exists():
    assert callable(UML2::Abstraction.__init__)


def test_uml2::abstraction_constructor_args():
    sig = inspect.signature(UML2::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReclassifyObjectAction)


def test_uml2::reclassifyobjectaction_constructor_exists():
    assert callable(UML2::ReclassifyObjectAction.__init__)


def test_uml2::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UML2::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2::InstanceValue)


def test_uml2::instancevalue_constructor_exists():
    assert callable(UML2::InstanceValue.__init__)


def test_uml2::instancevalue_constructor_args():
    sig = inspect.signature(UML2::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readselfaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadSelfAction)


def test_uml2::readselfaction_constructor_exists():
    assert callable(UML2::ReadSelfAction.__init__)


def test_uml2::readselfaction_constructor_args():
    sig = inspect.signature(UML2::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DestroyLinkAction)


def test_uml2::destroylinkaction_constructor_exists():
    assert callable(UML2::DestroyLinkAction.__init__)


def test_uml2::destroylinkaction_constructor_args():
    sig = inspect.signature(UML2::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateLinkAction)


def test_uml2::createlinkaction_constructor_exists():
    assert callable(UML2::CreateLinkAction.__init__)


def test_uml2::createlinkaction_constructor_args():
    sig = inspect.signature(UML2::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeExpression)


def test_uml2::timeexpression_constructor_exists():
    assert callable(UML2::TimeExpression.__init__)


def test_uml2::timeexpression_constructor_args():
    sig = inspect.signature(UML2::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::mergenode_is_not_abstract():
    assert not inspect.isabstract(UML2::MergeNode)


def test_uml2::mergenode_constructor_exists():
    assert callable(UML2::MergeNode.__init__)


def test_uml2::mergenode_constructor_args():
    sig = inspect.signature(UML2::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::packageableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::PackageableElement)


def test_uml2::packageableelement_constructor_exists():
    assert callable(UML2::PackageableElement.__init__)


def test_uml2::packageableelement_constructor_args():
    sig = inspect.signature(UML2::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2::AssociationClass)


def test_uml2::associationclass_constructor_exists():
    assert callable(UML2::AssociationClass.__init__)


def test_uml2::associationclass_constructor_args():
    sig = inspect.signature(UML2::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2::CommunicationPath)


def test_uml2::communicationpath_constructor_exists():
    assert callable(UML2::CommunicationPath.__init__)


def test_uml2::communicationpath_constructor_args():
    sig = inspect.signature(UML2::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extension_is_not_abstract():
    assert not inspect.isabstract(UML2::Extension)


def test_uml2::extension_constructor_exists():
    assert callable(UML2::Extension.__init__)


def test_uml2::extension_constructor_args():
    sig = inspect.signature(UML2::Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2::duration_is_not_abstract():
    assert not inspect.isabstract(UML2::Duration)


def test_uml2::duration_constructor_exists():
    assert callable(UML2::Duration.__init__)


def test_uml2::duration_constructor_args():
    sig = inspect.signature(UML2::Duration.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2::DeploymentSpecification)


def test_uml2::deploymentspecification_constructor_exists():
    assert callable(UML2::DeploymentSpecification.__init__)


def test_uml2::deploymentspecification_constructor_args():
    sig = inspect.signature(UML2::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2::ProtocolStateMachine)


def test_uml2::protocolstatemachine_constructor_exists():
    assert callable(UML2::ProtocolStateMachine.__init__)


def test_uml2::protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extend_is_not_abstract():
    assert not inspect.isabstract(UML2::Extend)


def test_uml2::extend_constructor_exists():
    assert callable(UML2::Extend.__init__)


def test_uml2::extend_constructor_args():
    sig = inspect.signature(UML2::Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeObservationAction)


def test_uml2::timeobservationaction_constructor_exists():
    assert callable(UML2::TimeObservationAction.__init__)


def test_uml2::timeobservationaction_constructor_args():
    sig = inspect.signature(UML2::TimeObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeatureAction)


def test_uml2::structuralfeatureaction_constructor_exists():
    assert callable(UML2::StructuralFeatureAction.__init__)


def test_uml2::structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::loopnode_is_not_abstract():
    assert not inspect.isabstract(UML2::LoopNode)


def test_uml2::loopnode_constructor_exists():
    assert callable(UML2::LoopNode.__init__)


def test_uml2::loopnode_constructor_args():
    sig = inspect.signature(UML2::LoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::device_is_not_abstract():
    assert not inspect.isabstract(UML2::Device)


def test_uml2::device_constructor_exists():
    assert callable(UML2::Device.__init__)


def test_uml2::device_constructor_args():
    sig = inspect.signature(UML2::Device.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::realization_is_not_abstract():
    assert not inspect.isabstract(UML2::Realization)


def test_uml2::realization_constructor_exists():
    assert callable(UML2::Realization.__init__)


def test_uml2::realization_constructor_args():
    sig = inspect.signature(UML2::Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml2::manifestation_is_not_abstract():
    assert not inspect.isabstract(UML2::Manifestation)


def test_uml2::manifestation_constructor_exists():
    assert callable(UML2::Manifestation.__init__)


def test_uml2::manifestation_constructor_args():
    sig = inspect.signature(UML2::Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2::Stereotype)


def test_uml2::stereotype_constructor_exists():
    assert callable(UML2::Stereotype.__init__)


def test_uml2::stereotype_constructor_args():
    sig = inspect.signature(UML2::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ObjectNode)


def test_uml2::objectnode_constructor_exists():
    assert callable(UML2::ObjectNode.__init__)


def test_uml2::objectnode_constructor_args():
    sig = inspect.signature(UML2::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::controlnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ControlNode)


def test_uml2::controlnode_constructor_exists():
    assert callable(UML2::ControlNode.__init__)


def test_uml2::controlnode_constructor_args():
    sig = inspect.signature(UML2::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::executablenode_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutableNode)


def test_uml2::executablenode_constructor_exists():
    assert callable(UML2::ExecutableNode.__init__)


def test_uml2::executablenode_constructor_args():
    sig = inspect.signature(UML2::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2::eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::EventOccurrence)


def test_uml2::eventoccurrence_constructor_exists():
    assert callable(UML2::EventOccurrence.__init__)


def test_uml2::eventoccurrence_constructor_args():
    sig = inspect.signature(UML2::EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::gate_is_not_abstract():
    assert not inspect.isabstract(UML2::Gate)


def test_uml2::gate_constructor_exists():
    assert callable(UML2::Gate.__init__)


def test_uml2::gate_constructor_args():
    sig = inspect.signature(UML2::Gate.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionPoint)


def test_uml2::extensionpoint_constructor_exists():
    assert callable(UML2::ExtensionPoint.__init__)


def test_uml2::extensionpoint_constructor_args():
    sig = inspect.signature(UML2::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "package",
        "private",
        "public",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"


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
CallAction_strategy = st.builds(
    CallAction,
)
UML2::CallOperationAction_strategy = st.builds(
    UML2::CallOperationAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
UML2::CallAction_strategy = st.builds(
    UML2::CallAction,
)
Property_strategy = st.builds(
    Property,
)
UML2::Port_strategy = st.builds(
    UML2::Port,
)
Class_strategy = st.builds(
    Class,
)
UML2::Component_strategy = st.builds(
    UML2::Component,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
Pin_strategy = st.builds(
    Pin,
)
UML2::InputPin_strategy = st.builds(
    UML2::InputPin,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UML2::WriteLinkAction_strategy = st.builds(
    UML2::WriteLinkAction,
)
MessageTrigger_strategy = st.builds(
    MessageTrigger,
)
UML2::SignalTrigger_strategy = st.builds(
    UML2::SignalTrigger,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
UML2::AcceptCallAction_strategy = st.builds(
    UML2::AcceptCallAction,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2::Activity_strategy = st.builds(
    UML2::Activity,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
UML2::Parameter_strategy = st.builds(
    UML2::Parameter,
)
UML2::Variable_strategy = st.builds(
    UML2::Variable,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
UML2::ControlFlow_strategy = st.builds(
    UML2::ControlFlow,
)
UML2::ObjectFlow_strategy = st.builds(
    UML2::ObjectFlow,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UML2::WriteStructuralFeatureAction_strategy = st.builds(
    UML2::WriteStructuralFeatureAction,
)
Package_strategy = st.builds(
    Package,
)
UML2::Model_strategy = st.builds(
    UML2::Model,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
UML2::InstanceSpecification_strategy = st.builds(
    UML2::InstanceSpecification,
)
Interval_strategy = st.builds(
    Interval,
)
UML2::TimeInterval_strategy = st.builds(
    UML2::TimeInterval,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
UML2::EnumerationLiteral_strategy = st.builds(
    UML2::EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
UML2::PrimitiveType_strategy = st.builds(
    UML2::PrimitiveType,
)
Realization_strategy = st.builds(
    Realization,
)
UML2::Substitution_strategy = st.builds(
    UML2::Substitution,
)
UML2::Implementation_strategy = st.builds(
    UML2::Implementation,
)
Node_strategy = st.builds(
    Node,
)
UML2::ExecutionEnvironment_strategy = st.builds(
    UML2::ExecutionEnvironment,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
UML2::JoinNode_strategy = st.builds(
    UML2::JoinNode,
)
UML2::DecisionNode_strategy = st.builds(
    UML2::DecisionNode,
)
State_strategy = st.builds(
    State,
)
UML2::FinalState_strategy = st.builds(
    UML2::FinalState,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UML2::DurationObservationAction_strategy = st.builds(
    UML2::DurationObservationAction,
)
UML2::Generalization_strategy = st.builds(
    UML2::Generalization,
)
UML2::NamedElement_strategy = st.builds(
    UML2::NamedElement,
    visibility=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UML2::LiteralSpecification_strategy = st.builds(
    UML2::LiteralSpecification,
)
UML2::OpaqueExpression_strategy = st.builds(
    UML2::OpaqueExpression,
)
UML2::Profile_strategy = st.builds(
    UML2::Profile,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
UML2::ExpansionRegion_strategy = st.builds(
    UML2::ExpansionRegion,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
UML2::Interaction_strategy = st.builds(
    UML2::Interaction,
)
UML2::CombinedFragment_strategy = st.builds(
    UML2::CombinedFragment,
)
UML2::InteractionOccurrence_strategy = st.builds(
    UML2::InteractionOccurrence,
)
UML2::StateInvariant_strategy = st.builds(
    UML2::StateInvariant,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
UML2::FlowFinalNode_strategy = st.builds(
    UML2::FlowFinalNode,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UML2::LiteralInteger_strategy = st.builds(
    UML2::LiteralInteger,
)
UML2::LiteralUnlimitedNatural_strategy = st.builds(
    UML2::LiteralUnlimitedNatural,
)
UML2::LiteralString_strategy = st.builds(
    UML2::LiteralString,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
UML2::InteractionFragment_strategy = st.builds(
    UML2::InteractionFragment,
)
UML2::CollaborationOccurrence_strategy = st.builds(
    UML2::CollaborationOccurrence,
)
UML2::ActivityPartition_strategy = st.builds(
    UML2::ActivityPartition,
)
UML2::Include_strategy = st.builds(
    UML2::Include,
)
UML2::GeneralOrdering_strategy = st.builds(
    UML2::GeneralOrdering,
)
UML2::DeployedArtifact_strategy = st.builds(
    UML2::DeployedArtifact,
)
UML2::TypedElement_strategy = st.builds(
    UML2::TypedElement,
)
UML2::ParameterSet_strategy = st.builds(
    UML2::ParameterSet,
)
Trigger_strategy = st.builds(
    Trigger,
)
UML2::MessageTrigger_strategy = st.builds(
    UML2::MessageTrigger,
)
UML2::ChangeTrigger_strategy = st.builds(
    UML2::ChangeTrigger,
)
UML2::TimeTrigger_strategy = st.builds(
    UML2::TimeTrigger,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UML2::Class_strategy = st.builds(
    UML2::Class,
)
UML2::UseCase_strategy = st.builds(
    UML2::UseCase,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UML2::AddVariableValueAction_strategy = st.builds(
    UML2::AddVariableValueAction,
)
UML2::RemoveVariableValueAction_strategy = st.builds(
    UML2::RemoveVariableValueAction,
)
Feature_strategy = st.builds(
    Feature,
)
UML2::Connector_strategy = st.builds(
    UML2::Connector,
)
Vertex_strategy = st.builds(
    Vertex,
)
UML2::Pseudostate_strategy = st.builds(
    UML2::Pseudostate,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
UML2::ActivityNode_strategy = st.builds(
    UML2::ActivityNode,
)
UML2::ActivityEdge_strategy = st.builds(
    UML2::ActivityEdge,
)
Namespace_strategy = st.builds(
    Namespace,
)
UML2::BehavioralFeature_strategy = st.builds(
    UML2::BehavioralFeature,
)
UML2::Region_strategy = st.builds(
    UML2::Region,
)
UML2::Classifier_strategy = st.builds(
    UML2::Classifier,
)
UML2::State_strategy = st.builds(
    UML2::State,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2::StructuredClassifier_strategy = st.builds(
    UML2::StructuredClassifier,
)
UML2::Association_strategy = st.builds(
    UML2::Association,
)
UML2::BehavioredClassifier_strategy = st.builds(
    UML2::BehavioredClassifier,
)
UML2::Actor_strategy = st.builds(
    UML2::Actor,
)
Dependency_strategy = st.builds(
    Dependency,
)
UML2::Permission_strategy = st.builds(
    UML2::Permission,
)
UML2::Deployment_strategy = st.builds(
    UML2::Deployment,
)
Transition_strategy = st.builds(
    Transition,
)
UML2::ProtocolTransition_strategy = st.builds(
    UML2::ProtocolTransition,
)
Action_strategy = st.builds(
    Action,
)
UML2::LinkAction_strategy = st.builds(
    UML2::LinkAction,
)
UML2::StartOwnedBehaviorAction_strategy = st.builds(
    UML2::StartOwnedBehaviorAction,
)
UML2::ClearAssociationAction_strategy = st.builds(
    UML2::ClearAssociationAction,
)
UML2::CreateObjectAction_strategy = st.builds(
    UML2::CreateObjectAction,
)
UML2::ReadExtentAction_strategy = st.builds(
    UML2::ReadExtentAction,
)
UML2::InvocationAction_strategy = st.builds(
    UML2::InvocationAction,
)
UML2::ApplyFunctionAction_strategy = st.builds(
    UML2::ApplyFunctionAction,
)
UML2::TestIdentityAction_strategy = st.builds(
    UML2::TestIdentityAction,
)
UML2::DestroyObjectAction_strategy = st.builds(
    UML2::DestroyObjectAction,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UML2::CentralBufferNode_strategy = st.builds(
    UML2::CentralBufferNode,
)
UML2::ActivityParameterNode_strategy = st.builds(
    UML2::ActivityParameterNode,
)
UML2::ExpansionNode_strategy = st.builds(
    UML2::ExpansionNode,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
UML2::WriteVariableAction_strategy = st.builds(
    UML2::WriteVariableAction,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2::Property_strategy = st.builds(
    UML2::Property,
)
UML2::Lifeline_strategy = st.builds(
    UML2::Lifeline,
)
UML2::ReadStructuralFeatureAction_strategy = st.builds(
    UML2::ReadStructuralFeatureAction,
)
UML2::GeneralizationSet_strategy = st.builds(
    UML2::GeneralizationSet,
)
UML2::InitialNode_strategy = st.builds(
    UML2::InitialNode,
)
UML2::SendSignalAction_strategy = st.builds(
    UML2::SendSignalAction,
)
UML2::FinalNode_strategy = st.builds(
    UML2::FinalNode,
)
UML2::RaiseExceptionAction_strategy = st.builds(
    UML2::RaiseExceptionAction,
)
Constraint_strategy = st.builds(
    Constraint,
)
UML2::InteractionConstraint_strategy = st.builds(
    UML2::InteractionConstraint,
)
UML2::IntervalConstraint_strategy = st.builds(
    UML2::IntervalConstraint,
)
UML2::ClearVariableAction_strategy = st.builds(
    UML2::ClearVariableAction,
)
UML2::Constraint_strategy = st.builds(
    UML2::Constraint,
)
UML2::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UML2::ReadLinkObjectEndQualifierAction,
)
UML2::Message_strategy = st.builds(
    UML2::Message,
)
UML2::RedefinableElement_strategy = st.builds(
    UML2::RedefinableElement,
)
UML2::Pin_strategy = st.builds(
    UML2::Pin,
)
UML2::AcceptEventAction_strategy = st.builds(
    UML2::AcceptEventAction,
)
UML2::TemplateableClassifier_strategy = st.builds(
    UML2::TemplateableClassifier,
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2::ValuePin_strategy = st.builds(
    UML2::ValuePin,
)
UML2::ReadIsClassifiedObjectAction_strategy = st.builds(
    UML2::ReadIsClassifiedObjectAction,
)
UML2::ReadVariableAction_strategy = st.builds(
    UML2::ReadVariableAction,
)
UML2::Dependency_strategy = st.builds(
    UML2::Dependency,
)
UML2::Artifact_strategy = st.builds(
    UML2::Artifact,
)
UML2::ConnectableElement_strategy = st.builds(
    UML2::ConnectableElement,
)
UML2::AddStructuralFeatureValueAction_strategy = st.builds(
    UML2::AddStructuralFeatureValueAction,
)
UML2::ReadLinkObjectEndAction_strategy = st.builds(
    UML2::ReadLinkObjectEndAction,
)
UML2::DataType_strategy = st.builds(
    UML2::DataType,
)
UML2::Vertex_strategy = st.builds(
    UML2::Vertex,
)
UML2::Behavior_strategy = st.builds(
    UML2::Behavior,
)
UML2::ForkNode_strategy = st.builds(
    UML2::ForkNode,
)
UML2::ValueSpecification_strategy = st.builds(
    UML2::ValueSpecification,
)
UML2::MessageEnd_strategy = st.builds(
    UML2::MessageEnd,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
UML2::CreateLinkObjectAction_strategy = st.builds(
    UML2::CreateLinkObjectAction,
)
UML2::StructuredActivityNode_strategy = st.builds(
    UML2::StructuredActivityNode,
)
UML2::StructuralFeature_strategy = st.builds(
    UML2::StructuralFeature,
)
UML2::DurationInterval_strategy = st.builds(
    UML2::DurationInterval,
)
UML2::Signal_strategy = st.builds(
    UML2::Signal,
)
UML2::ReplyAction_strategy = st.builds(
    UML2::ReplyAction,
)
UML2::Trigger_strategy = st.builds(
    UML2::Trigger,
)
UML2::ConnectionPointReference_strategy = st.builds(
    UML2::ConnectionPointReference,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UML2::Collaboration_strategy = st.builds(
    UML2::Collaboration,
)
UML2::EncapsulatedClassifier_strategy = st.builds(
    UML2::EncapsulatedClassifier,
)
UML2::VariableAction_strategy = st.builds(
    UML2::VariableAction,
)
UML2::AnyTrigger_strategy = st.builds(
    UML2::AnyTrigger,
)
UML2::LiteralBoolean_strategy = st.builds(
    UML2::LiteralBoolean,
)
UML2::InformationItem_strategy = st.builds(
    UML2::InformationItem,
)
UML2::InteractionOperand_strategy = st.builds(
    UML2::InteractionOperand,
)
UML2::Namespace_strategy = st.builds(
    UML2::Namespace,
)
UML2::CallBehaviorAction_strategy = st.builds(
    UML2::CallBehaviorAction,
)
InteractionOccurrence_strategy = st.builds(
    InteractionOccurrence,
)
UML2::PartDecomposition_strategy = st.builds(
    UML2::PartDecomposition,
)
UML2::ActivityFinalNode_strategy = st.builds(
    UML2::ActivityFinalNode,
)
UML2::Feature_strategy = st.builds(
    UML2::Feature,
)
UML2::LiteralNull_strategy = st.builds(
    UML2::LiteralNull,
)
UML2::DeploymentTarget_strategy = st.builds(
    UML2::DeploymentTarget,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
UML2::Expression_strategy = st.builds(
    UML2::Expression,
)
UML2::OutputPin_strategy = st.builds(
    UML2::OutputPin,
)
UML2::Node_strategy = st.builds(
    UML2::Node,
)
UML2::SendObjectAction_strategy = st.builds(
    UML2::SendObjectAction,
)
UML2::RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2::RemoveStructuralFeatureValueAction,
)
UML2::PrimitiveFunction_strategy = st.builds(
    UML2::PrimitiveFunction,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
UML2::Stop_strategy = st.builds(
    UML2::Stop,
)
UML2::Interval_strategy = st.builds(
    UML2::Interval,
)
UML2::Type_strategy = st.builds(
    UML2::Type,
)
UML2::StateMachine_strategy = st.builds(
    UML2::StateMachine,
)
UML2::ConditionalNode_strategy = st.builds(
    UML2::ConditionalNode,
)
UML2::CallTrigger_strategy = st.builds(
    UML2::CallTrigger,
)
UML2::ParameterableClassifier_strategy = st.builds(
    UML2::ParameterableClassifier,
)
UML2::ExecutionOccurrence_strategy = st.builds(
    UML2::ExecutionOccurrence,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
UML2::TimeConstraint_strategy = st.builds(
    UML2::TimeConstraint,
)
UML2::DurationConstraint_strategy = st.builds(
    UML2::DurationConstraint,
)
UML2::BroadcastSignalAction_strategy = st.builds(
    UML2::BroadcastSignalAction,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
UML2::Operation_strategy = st.builds(
    UML2::Operation,
)
UML2::Reception_strategy = st.builds(
    UML2::Reception,
)
UML2::Interface_strategy = st.builds(
    UML2::Interface,
)
UML2::Transition_strategy = st.builds(
    UML2::Transition,
)
UML2::RedefinableTemplateSignature_strategy = st.builds(
    UML2::RedefinableTemplateSignature,
)
UML2::ExtensionEnd_strategy = st.builds(
    UML2::ExtensionEnd,
)
UML2::ReadLinkAction_strategy = st.builds(
    UML2::ReadLinkAction,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UML2::DataStoreNode_strategy = st.builds(
    UML2::DataStoreNode,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
UML2::Action_strategy = st.builds(
    UML2::Action,
)
UML2::InformationFlow_strategy = st.builds(
    UML2::InformationFlow,
)
UML2::Enumeration_strategy = st.builds(
    UML2::Enumeration,
)
UML2::Package_strategy = st.builds(
    UML2::Package,
)
UML2::Continuation_strategy = st.builds(
    UML2::Continuation,
)
UML2::Usage_strategy = st.builds(
    UML2::Usage,
)
UML2::ClearStructuralFeatureAction_strategy = st.builds(
    UML2::ClearStructuralFeatureAction,
)
UML2::Abstraction_strategy = st.builds(
    UML2::Abstraction,
)
UML2::ReclassifyObjectAction_strategy = st.builds(
    UML2::ReclassifyObjectAction,
)
UML2::InstanceValue_strategy = st.builds(
    UML2::InstanceValue,
)
UML2::ReadSelfAction_strategy = st.builds(
    UML2::ReadSelfAction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
UML2::DestroyLinkAction_strategy = st.builds(
    UML2::DestroyLinkAction,
)
UML2::CreateLinkAction_strategy = st.builds(
    UML2::CreateLinkAction,
)
UML2::TimeExpression_strategy = st.builds(
    UML2::TimeExpression,
)
UML2::MergeNode_strategy = st.builds(
    UML2::MergeNode,
)
UML2::PackageableElement_strategy = st.builds(
    UML2::PackageableElement,
)
Association_strategy = st.builds(
    Association,
)
UML2::AssociationClass_strategy = st.builds(
    UML2::AssociationClass,
)
UML2::CommunicationPath_strategy = st.builds(
    UML2::CommunicationPath,
)
UML2::Extension_strategy = st.builds(
    UML2::Extension,
)
UML2::Duration_strategy = st.builds(
    UML2::Duration,
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2::DeploymentSpecification_strategy = st.builds(
    UML2::DeploymentSpecification,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2::ProtocolStateMachine_strategy = st.builds(
    UML2::ProtocolStateMachine,
)
UML2::Extend_strategy = st.builds(
    UML2::Extend,
)
UML2::TimeObservationAction_strategy = st.builds(
    UML2::TimeObservationAction,
)
UML2::StructuralFeatureAction_strategy = st.builds(
    UML2::StructuralFeatureAction,
)
UML2::LoopNode_strategy = st.builds(
    UML2::LoopNode,
)
UML2::Device_strategy = st.builds(
    UML2::Device,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
UML2::Realization_strategy = st.builds(
    UML2::Realization,
)
UML2::Manifestation_strategy = st.builds(
    UML2::Manifestation,
)
UML2::Stereotype_strategy = st.builds(
    UML2::Stereotype,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
UML2::ObjectNode_strategy = st.builds(
    UML2::ObjectNode,
)
UML2::ControlNode_strategy = st.builds(
    UML2::ControlNode,
)
UML2::ExecutableNode_strategy = st.builds(
    UML2::ExecutableNode,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
UML2::EventOccurrence_strategy = st.builds(
    UML2::EventOccurrence,
)
UML2::Gate_strategy = st.builds(
    UML2::Gate,
)
UML2::ExtensionPoint_strategy = st.builds(
    UML2::ExtensionPoint,
)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=UML2::CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml2::calloperationaction_instantiation(instance):
    assert isinstance(instance, UML2::CallOperationAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=UML2::CallAction_strategy)
@settings(max_examples=50)
def test_uml2::callaction_instantiation(instance):
    assert isinstance(instance, UML2::CallAction)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2::Port_strategy)
@settings(max_examples=50)
def test_uml2::port_instantiation(instance):
    assert isinstance(instance, UML2::Port)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2::Component_strategy)
@settings(max_examples=50)
def test_uml2::component_instantiation(instance):
    assert isinstance(instance, UML2::Component)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=UML2::InputPin_strategy)
@settings(max_examples=50)
def test_uml2::inputpin_instantiation(instance):
    assert isinstance(instance, UML2::InputPin)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UML2::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::writelinkaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteLinkAction)

@given(instance=MessageTrigger_strategy)
@settings(max_examples=50)
def test_messagetrigger_instantiation(instance):
    assert isinstance(instance, MessageTrigger)

@given(instance=UML2::SignalTrigger_strategy)
@settings(max_examples=50)
def test_uml2::signaltrigger_instantiation(instance):
    assert isinstance(instance, UML2::SignalTrigger)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=UML2::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml2::acceptcallaction_instantiation(instance):
    assert isinstance(instance, UML2::AcceptCallAction)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2::Activity_strategy)
@settings(max_examples=50)
def test_uml2::activity_instantiation(instance):
    assert isinstance(instance, UML2::Activity)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=UML2::Parameter_strategy)
@settings(max_examples=50)
def test_uml2::parameter_instantiation(instance):
    assert isinstance(instance, UML2::Parameter)

@given(instance=UML2::Variable_strategy)
@settings(max_examples=50)
def test_uml2::variable_instantiation(instance):
    assert isinstance(instance, UML2::Variable)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=UML2::ControlFlow_strategy)
@settings(max_examples=50)
def test_uml2::controlflow_instantiation(instance):
    assert isinstance(instance, UML2::ControlFlow)

@given(instance=UML2::ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml2::objectflow_instantiation(instance):
    assert isinstance(instance, UML2::ObjectFlow)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UML2::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteStructuralFeatureAction)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=UML2::Model_strategy)
@settings(max_examples=50)
def test_uml2::model_instantiation(instance):
    assert isinstance(instance, UML2::Model)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=UML2::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml2::instancespecification_instantiation(instance):
    assert isinstance(instance, UML2::InstanceSpecification)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UML2::TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2::timeinterval_instantiation(instance):
    assert isinstance(instance, UML2::TimeInterval)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=UML2::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml2::enumerationliteral_instantiation(instance):
    assert isinstance(instance, UML2::EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UML2::PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2::primitivetype_instantiation(instance):
    assert isinstance(instance, UML2::PrimitiveType)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=UML2::Substitution_strategy)
@settings(max_examples=50)
def test_uml2::substitution_instantiation(instance):
    assert isinstance(instance, UML2::Substitution)

@given(instance=UML2::Implementation_strategy)
@settings(max_examples=50)
def test_uml2::implementation_instantiation(instance):
    assert isinstance(instance, UML2::Implementation)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2::ExecutionEnvironment)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=UML2::JoinNode_strategy)
@settings(max_examples=50)
def test_uml2::joinnode_instantiation(instance):
    assert isinstance(instance, UML2::JoinNode)

@given(instance=UML2::DecisionNode_strategy)
@settings(max_examples=50)
def test_uml2::decisionnode_instantiation(instance):
    assert isinstance(instance, UML2::DecisionNode)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UML2::FinalState_strategy)
@settings(max_examples=50)
def test_uml2::finalstate_instantiation(instance):
    assert isinstance(instance, UML2::FinalState)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UML2::DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::DurationObservationAction)

@given(instance=UML2::Generalization_strategy)
@settings(max_examples=50)
def test_uml2::generalization_instantiation(instance):
    assert isinstance(instance, UML2::Generalization)

@given(instance=UML2::NamedElement_strategy)
@settings(max_examples=50)
def test_uml2::namedelement_instantiation(instance):
    assert isinstance(instance, UML2::NamedElement)

@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UML2::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2::literalspecification_instantiation(instance):
    assert isinstance(instance, UML2::LiteralSpecification)

@given(instance=UML2::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2::opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2::OpaqueExpression)

@given(instance=UML2::Profile_strategy)
@settings(max_examples=50)
def test_uml2::profile_instantiation(instance):
    assert isinstance(instance, UML2::Profile)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=UML2::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml2::expansionregion_instantiation(instance):
    assert isinstance(instance, UML2::ExpansionRegion)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=UML2::Interaction_strategy)
@settings(max_examples=50)
def test_uml2::interaction_instantiation(instance):
    assert isinstance(instance, UML2::Interaction)

@given(instance=UML2::CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml2::combinedfragment_instantiation(instance):
    assert isinstance(instance, UML2::CombinedFragment)

@given(instance=UML2::InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::interactionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::InteractionOccurrence)

@given(instance=UML2::StateInvariant_strategy)
@settings(max_examples=50)
def test_uml2::stateinvariant_instantiation(instance):
    assert isinstance(instance, UML2::StateInvariant)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=UML2::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml2::flowfinalnode_instantiation(instance):
    assert isinstance(instance, UML2::FlowFinalNode)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UML2::LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2::literalinteger_instantiation(instance):
    assert isinstance(instance, UML2::LiteralInteger)

@given(instance=UML2::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2::LiteralUnlimitedNatural)

@given(instance=UML2::LiteralString_strategy)
@settings(max_examples=50)
def test_uml2::literalstring_instantiation(instance):
    assert isinstance(instance, UML2::LiteralString)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=UML2::InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml2::interactionfragment_instantiation(instance):
    assert isinstance(instance, UML2::InteractionFragment)

@given(instance=UML2::CollaborationOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::collaborationoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::CollaborationOccurrence)

@given(instance=UML2::ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml2::activitypartition_instantiation(instance):
    assert isinstance(instance, UML2::ActivityPartition)

@given(instance=UML2::Include_strategy)
@settings(max_examples=50)
def test_uml2::include_instantiation(instance):
    assert isinstance(instance, UML2::Include)

@given(instance=UML2::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml2::generalordering_instantiation(instance):
    assert isinstance(instance, UML2::GeneralOrdering)

@given(instance=UML2::DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml2::deployedartifact_instantiation(instance):
    assert isinstance(instance, UML2::DeployedArtifact)

@given(instance=UML2::TypedElement_strategy)
@settings(max_examples=50)
def test_uml2::typedelement_instantiation(instance):
    assert isinstance(instance, UML2::TypedElement)

@given(instance=UML2::ParameterSet_strategy)
@settings(max_examples=50)
def test_uml2::parameterset_instantiation(instance):
    assert isinstance(instance, UML2::ParameterSet)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=UML2::MessageTrigger_strategy)
@settings(max_examples=50)
def test_uml2::messagetrigger_instantiation(instance):
    assert isinstance(instance, UML2::MessageTrigger)

@given(instance=UML2::ChangeTrigger_strategy)
@settings(max_examples=50)
def test_uml2::changetrigger_instantiation(instance):
    assert isinstance(instance, UML2::ChangeTrigger)

@given(instance=UML2::TimeTrigger_strategy)
@settings(max_examples=50)
def test_uml2::timetrigger_instantiation(instance):
    assert isinstance(instance, UML2::TimeTrigger)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UML2::Class_strategy)
@settings(max_examples=50)
def test_uml2::class_instantiation(instance):
    assert isinstance(instance, UML2::Class)

@given(instance=UML2::UseCase_strategy)
@settings(max_examples=50)
def test_uml2::usecase_instantiation(instance):
    assert isinstance(instance, UML2::UseCase)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UML2::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::AddVariableValueAction)

@given(instance=UML2::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::RemoveVariableValueAction)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=UML2::Connector_strategy)
@settings(max_examples=50)
def test_uml2::connector_instantiation(instance):
    assert isinstance(instance, UML2::Connector)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=UML2::Pseudostate_strategy)
@settings(max_examples=50)
def test_uml2::pseudostate_instantiation(instance):
    assert isinstance(instance, UML2::Pseudostate)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=UML2::ActivityNode_strategy)
@settings(max_examples=50)
def test_uml2::activitynode_instantiation(instance):
    assert isinstance(instance, UML2::ActivityNode)

@given(instance=UML2::ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml2::activityedge_instantiation(instance):
    assert isinstance(instance, UML2::ActivityEdge)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=UML2::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2::BehavioralFeature)

@given(instance=UML2::Region_strategy)
@settings(max_examples=50)
def test_uml2::region_instantiation(instance):
    assert isinstance(instance, UML2::Region)

@given(instance=UML2::Classifier_strategy)
@settings(max_examples=50)
def test_uml2::classifier_instantiation(instance):
    assert isinstance(instance, UML2::Classifier)

@given(instance=UML2::State_strategy)
@settings(max_examples=50)
def test_uml2::state_instantiation(instance):
    assert isinstance(instance, UML2::State)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::StructuredClassifier)

@given(instance=UML2::Association_strategy)
@settings(max_examples=50)
def test_uml2::association_instantiation(instance):
    assert isinstance(instance, UML2::Association)

@given(instance=UML2::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::BehavioredClassifier)

@given(instance=UML2::Actor_strategy)
@settings(max_examples=50)
def test_uml2::actor_instantiation(instance):
    assert isinstance(instance, UML2::Actor)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=UML2::Permission_strategy)
@settings(max_examples=50)
def test_uml2::permission_instantiation(instance):
    assert isinstance(instance, UML2::Permission)

@given(instance=UML2::Deployment_strategy)
@settings(max_examples=50)
def test_uml2::deployment_instantiation(instance):
    assert isinstance(instance, UML2::Deployment)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=UML2::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml2::protocoltransition_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolTransition)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UML2::LinkAction_strategy)
@settings(max_examples=50)
def test_uml2::linkaction_instantiation(instance):
    assert isinstance(instance, UML2::LinkAction)

@given(instance=UML2::StartOwnedBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2::startownedbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2::StartOwnedBehaviorAction)

@given(instance=UML2::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml2::clearassociationaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearAssociationAction)

@given(instance=UML2::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::createobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateObjectAction)

@given(instance=UML2::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml2::readextentaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadExtentAction)

@given(instance=UML2::InvocationAction_strategy)
@settings(max_examples=50)
def test_uml2::invocationaction_instantiation(instance):
    assert isinstance(instance, UML2::InvocationAction)

@given(instance=UML2::ApplyFunctionAction_strategy)
@settings(max_examples=50)
def test_uml2::applyfunctionaction_instantiation(instance):
    assert isinstance(instance, UML2::ApplyFunctionAction)

@given(instance=UML2::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2::testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2::TestIdentityAction)

@given(instance=UML2::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::DestroyObjectAction)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UML2::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2::centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2::CentralBufferNode)

@given(instance=UML2::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2::activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2::ActivityParameterNode)

@given(instance=UML2::ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2::expansionnode_instantiation(instance):
    assert isinstance(instance, UML2::ExpansionNode)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=UML2::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::writevariableaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteVariableAction)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=UML2::Lifeline_strategy)
@settings(max_examples=50)
def test_uml2::lifeline_instantiation(instance):
    assert isinstance(instance, UML2::Lifeline)

@given(instance=UML2::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadStructuralFeatureAction)

@given(instance=UML2::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml2::generalizationset_instantiation(instance):
    assert isinstance(instance, UML2::GeneralizationSet)

@given(instance=UML2::InitialNode_strategy)
@settings(max_examples=50)
def test_uml2::initialnode_instantiation(instance):
    assert isinstance(instance, UML2::InitialNode)

@given(instance=UML2::SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml2::sendsignalaction_instantiation(instance):
    assert isinstance(instance, UML2::SendSignalAction)

@given(instance=UML2::FinalNode_strategy)
@settings(max_examples=50)
def test_uml2::finalnode_instantiation(instance):
    assert isinstance(instance, UML2::FinalNode)

@given(instance=UML2::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml2::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UML2::RaiseExceptionAction)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UML2::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml2::interactionconstraint_instantiation(instance):
    assert isinstance(instance, UML2::InteractionConstraint)

@given(instance=UML2::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml2::intervalconstraint_instantiation(instance):
    assert isinstance(instance, UML2::IntervalConstraint)

@given(instance=UML2::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::clearvariableaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearVariableAction)

@given(instance=UML2::Constraint_strategy)
@settings(max_examples=50)
def test_uml2::constraint_instantiation(instance):
    assert isinstance(instance, UML2::Constraint)

@given(instance=UML2::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkObjectEndQualifierAction)

@given(instance=UML2::Message_strategy)
@settings(max_examples=50)
def test_uml2::message_instantiation(instance):
    assert isinstance(instance, UML2::Message)

@given(instance=UML2::RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml2::redefinableelement_instantiation(instance):
    assert isinstance(instance, UML2::RedefinableElement)

@given(instance=UML2::Pin_strategy)
@settings(max_examples=50)
def test_uml2::pin_instantiation(instance):
    assert isinstance(instance, UML2::Pin)

@given(instance=UML2::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml2::accepteventaction_instantiation(instance):
    assert isinstance(instance, UML2::AcceptEventAction)

@given(instance=UML2::TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::TemplateableClassifier)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2::ValuePin_strategy)
@settings(max_examples=50)
def test_uml2::valuepin_instantiation(instance):
    assert isinstance(instance, UML2::ValuePin)

@given(instance=UML2::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadIsClassifiedObjectAction)

@given(instance=UML2::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::readvariableaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadVariableAction)

@given(instance=UML2::Dependency_strategy)
@settings(max_examples=50)
def test_uml2::dependency_instantiation(instance):
    assert isinstance(instance, UML2::Dependency)

@given(instance=UML2::Artifact_strategy)
@settings(max_examples=50)
def test_uml2::artifact_instantiation(instance):
    assert isinstance(instance, UML2::Artifact)

@given(instance=UML2::ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml2::connectableelement_instantiation(instance):
    assert isinstance(instance, UML2::ConnectableElement)

@given(instance=UML2::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::AddStructuralFeatureValueAction)

@given(instance=UML2::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkObjectEndAction)

@given(instance=UML2::DataType_strategy)
@settings(max_examples=50)
def test_uml2::datatype_instantiation(instance):
    assert isinstance(instance, UML2::DataType)

@given(instance=UML2::Vertex_strategy)
@settings(max_examples=50)
def test_uml2::vertex_instantiation(instance):
    assert isinstance(instance, UML2::Vertex)

@given(instance=UML2::Behavior_strategy)
@settings(max_examples=50)
def test_uml2::behavior_instantiation(instance):
    assert isinstance(instance, UML2::Behavior)

@given(instance=UML2::ForkNode_strategy)
@settings(max_examples=50)
def test_uml2::forknode_instantiation(instance):
    assert isinstance(instance, UML2::ForkNode)

@given(instance=UML2::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2::valuespecification_instantiation(instance):
    assert isinstance(instance, UML2::ValueSpecification)

@given(instance=UML2::MessageEnd_strategy)
@settings(max_examples=50)
def test_uml2::messageend_instantiation(instance):
    assert isinstance(instance, UML2::MessageEnd)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=UML2::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateLinkObjectAction)

@given(instance=UML2::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml2::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UML2::StructuredActivityNode)

@given(instance=UML2::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeature)

@given(instance=UML2::DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2::durationinterval_instantiation(instance):
    assert isinstance(instance, UML2::DurationInterval)

@given(instance=UML2::Signal_strategy)
@settings(max_examples=50)
def test_uml2::signal_instantiation(instance):
    assert isinstance(instance, UML2::Signal)

@given(instance=UML2::ReplyAction_strategy)
@settings(max_examples=50)
def test_uml2::replyaction_instantiation(instance):
    assert isinstance(instance, UML2::ReplyAction)

@given(instance=UML2::Trigger_strategy)
@settings(max_examples=50)
def test_uml2::trigger_instantiation(instance):
    assert isinstance(instance, UML2::Trigger)

@given(instance=UML2::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml2::connectionpointreference_instantiation(instance):
    assert isinstance(instance, UML2::ConnectionPointReference)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UML2::Collaboration_strategy)
@settings(max_examples=50)
def test_uml2::collaboration_instantiation(instance):
    assert isinstance(instance, UML2::Collaboration)

@given(instance=UML2::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2::EncapsulatedClassifier)

@given(instance=UML2::VariableAction_strategy)
@settings(max_examples=50)
def test_uml2::variableaction_instantiation(instance):
    assert isinstance(instance, UML2::VariableAction)

@given(instance=UML2::AnyTrigger_strategy)
@settings(max_examples=50)
def test_uml2::anytrigger_instantiation(instance):
    assert isinstance(instance, UML2::AnyTrigger)

@given(instance=UML2::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2::literalboolean_instantiation(instance):
    assert isinstance(instance, UML2::LiteralBoolean)

@given(instance=UML2::InformationItem_strategy)
@settings(max_examples=50)
def test_uml2::informationitem_instantiation(instance):
    assert isinstance(instance, UML2::InformationItem)

@given(instance=UML2::InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml2::interactionoperand_instantiation(instance):
    assert isinstance(instance, UML2::InteractionOperand)

@given(instance=UML2::Namespace_strategy)
@settings(max_examples=50)
def test_uml2::namespace_instantiation(instance):
    assert isinstance(instance, UML2::Namespace)

@given(instance=UML2::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2::callbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2::CallBehaviorAction)

@given(instance=InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_interactionoccurrence_instantiation(instance):
    assert isinstance(instance, InteractionOccurrence)

@given(instance=UML2::PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml2::partdecomposition_instantiation(instance):
    assert isinstance(instance, UML2::PartDecomposition)

@given(instance=UML2::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml2::activityfinalnode_instantiation(instance):
    assert isinstance(instance, UML2::ActivityFinalNode)

@given(instance=UML2::Feature_strategy)
@settings(max_examples=50)
def test_uml2::feature_instantiation(instance):
    assert isinstance(instance, UML2::Feature)

@given(instance=UML2::LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2::literalnull_instantiation(instance):
    assert isinstance(instance, UML2::LiteralNull)

@given(instance=UML2::DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml2::deploymenttarget_instantiation(instance):
    assert isinstance(instance, UML2::DeploymentTarget)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2::Expression_strategy)
@settings(max_examples=50)
def test_uml2::expression_instantiation(instance):
    assert isinstance(instance, UML2::Expression)

@given(instance=UML2::OutputPin_strategy)
@settings(max_examples=50)
def test_uml2::outputpin_instantiation(instance):
    assert isinstance(instance, UML2::OutputPin)

@given(instance=UML2::Node_strategy)
@settings(max_examples=50)
def test_uml2::node_instantiation(instance):
    assert isinstance(instance, UML2::Node)

@given(instance=UML2::SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::sendobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::SendObjectAction)

@given(instance=UML2::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::RemoveStructuralFeatureValueAction)

@given(instance=UML2::PrimitiveFunction_strategy)
@settings(max_examples=50)
def test_uml2::primitivefunction_instantiation(instance):
    assert isinstance(instance, UML2::PrimitiveFunction)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=UML2::Stop_strategy)
@settings(max_examples=50)
def test_uml2::stop_instantiation(instance):
    assert isinstance(instance, UML2::Stop)

@given(instance=UML2::Interval_strategy)
@settings(max_examples=50)
def test_uml2::interval_instantiation(instance):
    assert isinstance(instance, UML2::Interval)

@given(instance=UML2::Type_strategy)
@settings(max_examples=50)
def test_uml2::type_instantiation(instance):
    assert isinstance(instance, UML2::Type)

@given(instance=UML2::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2::statemachine_instantiation(instance):
    assert isinstance(instance, UML2::StateMachine)

@given(instance=UML2::ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml2::conditionalnode_instantiation(instance):
    assert isinstance(instance, UML2::ConditionalNode)

@given(instance=UML2::CallTrigger_strategy)
@settings(max_examples=50)
def test_uml2::calltrigger_instantiation(instance):
    assert isinstance(instance, UML2::CallTrigger)

@given(instance=UML2::ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::ParameterableClassifier)

@given(instance=UML2::ExecutionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::executionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::ExecutionOccurrence)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=UML2::TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml2::timeconstraint_instantiation(instance):
    assert isinstance(instance, UML2::TimeConstraint)

@given(instance=UML2::DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml2::durationconstraint_instantiation(instance):
    assert isinstance(instance, UML2::DurationConstraint)

@given(instance=UML2::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml2::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UML2::BroadcastSignalAction)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=UML2::Operation_strategy)
@settings(max_examples=50)
def test_uml2::operation_instantiation(instance):
    assert isinstance(instance, UML2::Operation)

@given(instance=UML2::Reception_strategy)
@settings(max_examples=50)
def test_uml2::reception_instantiation(instance):
    assert isinstance(instance, UML2::Reception)

@given(instance=UML2::Interface_strategy)
@settings(max_examples=50)
def test_uml2::interface_instantiation(instance):
    assert isinstance(instance, UML2::Interface)

@given(instance=UML2::Transition_strategy)
@settings(max_examples=50)
def test_uml2::transition_instantiation(instance):
    assert isinstance(instance, UML2::Transition)

@given(instance=UML2::RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2::redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, UML2::RedefinableTemplateSignature)

@given(instance=UML2::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2::extensionend_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionEnd)

@given(instance=UML2::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkAction)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UML2::DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2::datastorenode_instantiation(instance):
    assert isinstance(instance, UML2::DataStoreNode)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=UML2::Action_strategy)
@settings(max_examples=50)
def test_uml2::action_instantiation(instance):
    assert isinstance(instance, UML2::Action)

@given(instance=UML2::InformationFlow_strategy)
@settings(max_examples=50)
def test_uml2::informationflow_instantiation(instance):
    assert isinstance(instance, UML2::InformationFlow)

@given(instance=UML2::Enumeration_strategy)
@settings(max_examples=50)
def test_uml2::enumeration_instantiation(instance):
    assert isinstance(instance, UML2::Enumeration)

@given(instance=UML2::Package_strategy)
@settings(max_examples=50)
def test_uml2::package_instantiation(instance):
    assert isinstance(instance, UML2::Package)

@given(instance=UML2::Continuation_strategy)
@settings(max_examples=50)
def test_uml2::continuation_instantiation(instance):
    assert isinstance(instance, UML2::Continuation)

@given(instance=UML2::Usage_strategy)
@settings(max_examples=50)
def test_uml2::usage_instantiation(instance):
    assert isinstance(instance, UML2::Usage)

@given(instance=UML2::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearStructuralFeatureAction)

@given(instance=UML2::Abstraction_strategy)
@settings(max_examples=50)
def test_uml2::abstraction_instantiation(instance):
    assert isinstance(instance, UML2::Abstraction)

@given(instance=UML2::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::ReclassifyObjectAction)

@given(instance=UML2::InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2::instancevalue_instantiation(instance):
    assert isinstance(instance, UML2::InstanceValue)

@given(instance=UML2::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml2::readselfaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadSelfAction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=UML2::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::destroylinkaction_instantiation(instance):
    assert isinstance(instance, UML2::DestroyLinkAction)

@given(instance=UML2::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::createlinkaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateLinkAction)

@given(instance=UML2::TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2::timeexpression_instantiation(instance):
    assert isinstance(instance, UML2::TimeExpression)

@given(instance=UML2::MergeNode_strategy)
@settings(max_examples=50)
def test_uml2::mergenode_instantiation(instance):
    assert isinstance(instance, UML2::MergeNode)

@given(instance=UML2::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml2::packageableelement_instantiation(instance):
    assert isinstance(instance, UML2::PackageableElement)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2::associationclass_instantiation(instance):
    assert isinstance(instance, UML2::AssociationClass)

@given(instance=UML2::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2::communicationpath_instantiation(instance):
    assert isinstance(instance, UML2::CommunicationPath)

@given(instance=UML2::Extension_strategy)
@settings(max_examples=50)
def test_uml2::extension_instantiation(instance):
    assert isinstance(instance, UML2::Extension)

@given(instance=UML2::Duration_strategy)
@settings(max_examples=50)
def test_uml2::duration_instantiation(instance):
    assert isinstance(instance, UML2::Duration)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2::DeploymentSpecification)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolStateMachine)

@given(instance=UML2::Extend_strategy)
@settings(max_examples=50)
def test_uml2::extend_instantiation(instance):
    assert isinstance(instance, UML2::Extend)

@given(instance=UML2::TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::TimeObservationAction)

@given(instance=UML2::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeatureAction)

@given(instance=UML2::LoopNode_strategy)
@settings(max_examples=50)
def test_uml2::loopnode_instantiation(instance):
    assert isinstance(instance, UML2::LoopNode)

@given(instance=UML2::Device_strategy)
@settings(max_examples=50)
def test_uml2::device_instantiation(instance):
    assert isinstance(instance, UML2::Device)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=UML2::Realization_strategy)
@settings(max_examples=50)
def test_uml2::realization_instantiation(instance):
    assert isinstance(instance, UML2::Realization)

@given(instance=UML2::Manifestation_strategy)
@settings(max_examples=50)
def test_uml2::manifestation_instantiation(instance):
    assert isinstance(instance, UML2::Manifestation)

@given(instance=UML2::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2::stereotype_instantiation(instance):
    assert isinstance(instance, UML2::Stereotype)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=UML2::ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2::objectnode_instantiation(instance):
    assert isinstance(instance, UML2::ObjectNode)

@given(instance=UML2::ControlNode_strategy)
@settings(max_examples=50)
def test_uml2::controlnode_instantiation(instance):
    assert isinstance(instance, UML2::ControlNode)

@given(instance=UML2::ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml2::executablenode_instantiation(instance):
    assert isinstance(instance, UML2::ExecutableNode)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=UML2::EventOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::eventoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::EventOccurrence)

@given(instance=UML2::Gate_strategy)
@settings(max_examples=50)
def test_uml2::gate_instantiation(instance):
    assert isinstance(instance, UML2::Gate)

@given(instance=UML2::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml2::extensionpoint_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionPoint)

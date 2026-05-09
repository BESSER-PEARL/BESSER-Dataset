import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML2WithID::Element,
    Transition,
    EventOccurrence,
    Type,
    CallAction,
    Dependency,
    EncapsulatedClassifier,
    InstanceSpecification,
    Node,
    OpaqueExpression,
    StructuralFeature,
    MessageEnd,
    StateMachine,
    ActivityEdge,
    Package,
    FinalNode,
    ObjectNode,
    MessageTrigger,
    Trigger,
    Abstraction,
    WriteLinkAction,
    StructuredActivityNode,
    Artifact,
    StructuralFeatureAction,
    ControlNode,
    CreateLinkAction,
    Interval,
    IntervalConstraint,
    ExecutableNode,
    State,
    VariableAction,
    StructuredClassifier,
    BehavioredClassifier,
    Association,
    Feature,
    Property,
    Vertex,
    DeploymentTarget,
    Class,
    WriteStructuralFeatureAction,
    Pin,
    DeployedArtifact,
    PackageableElement,
    Classifier,
    Behavior,
    InputPin,
    Realization,
    TypedElement,
    ActivityNode,
    ValueSpecification,
    NamedElement,
    RedefinableElement,
    BehavioralFeature,
    AcceptEventAction,
    InvocationAction,
    LiteralSpecification,
    DataType,
    InteractionOccurrence,
    InteractionFragment,
    Namespace,
    Element,
    UML2WithID::AnyTrigger,
    UML2WithID::Duration,
    UML2WithID::CollaborationOccurrence,
    UML2WithID::InteractionOperand,
    UML2WithID::Abstraction,
    UML2WithID::Enumeration,
    UML2WithID::LiteralUnlimitedNatural,
    UML2WithID::Stop,
    UML2WithID::WriteStructuralFeatureAction,
    UML2WithID::ActivityFinalNode,
    UML2WithID::ConditionalNode,
    UML2WithID::ProtocolStateMachine,
    UML2WithID::ActivityNode,
    UML2WithID::ExecutableNode,
    UML2WithID::Manifestation,
    UML2WithID::GeneralizationSet,
    UML2WithID::TypedElement,
    UML2WithID::DurationInterval,
    UML2WithID::CreateLinkAction,
    UML2WithID::ControlNode,
    UML2WithID::Class,
    UML2WithID::DataType,
    UML2WithID::ReadVariableAction,
    UML2WithID::Reception,
    UML2WithID::LiteralBoolean,
    UML2WithID::Expression,
    UML2WithID::DurationConstraint,
    UML2WithID::DeploymentSpecification,
    UML2WithID::LiteralNull,
    UML2WithID::RedefinableTemplateSignature,
    UML2WithID::ActivityPartition,
    UML2WithID::BroadcastSignalAction,
    UML2WithID::TimeExpression,
    UML2WithID::ForkNode,
    UML2WithID::ExtensionEnd,
    UML2WithID::CallOperationAction,
    UML2WithID::WriteVariableAction,
    UML2WithID::MessageTrigger,
    UML2WithID::ActivityEdge,
    UML2WithID::UseCase,
    UML2WithID::EventOccurrence,
    UML2WithID::StructuralFeature,
    UML2WithID::ObjectNode,
    UML2WithID::AssociationClass,
    UML2WithID::InputPin,
    UML2WithID::CallAction,
    UML2WithID::Association,
    UML2WithID::SignalTrigger,
    UML2WithID::Interaction,
    UML2WithID::ClearVariableAction,
    UML2WithID::Continuation,
    UML2WithID::TimeTrigger,
    UML2WithID::CentralBufferNode,
    UML2WithID::PartDecomposition,
    UML2WithID::Usage,
    UML2WithID::Port,
    UML2WithID::Actor,
    UML2WithID::ValueSpecification,
    UML2WithID::Package,
    UML2WithID::Signal,
    UML2WithID::ConnectionPointReference,
    UML2WithID::ClearStructuralFeatureAction,
    UML2WithID::Profile,
    UML2WithID::BehavioralFeature,
    UML2WithID::InformationFlow,
    UML2WithID::Region,
    UML2WithID::Include,
    UML2WithID::Substitution,
    UML2WithID::Vertex,
    UML2WithID::MessageEnd,
    UML2WithID::Interface,
    UML2WithID::ParameterSet,
    UML2WithID::DecisionNode,
    UML2WithID::InteractionFragment,
    UML2WithID::StateMachine,
    UML2WithID::Node,
    UML2WithID::TimeObservationAction,
    UML2WithID::SendObjectAction,
    UML2WithID::GeneralOrdering,
    UML2WithID::ParameterableClassifier,
    UML2WithID::Activity,
    UML2WithID::FinalNode,
    UML2WithID::AcceptCallAction,
    UML2WithID::Realization,
    UML2WithID::InitialNode,
    UML2WithID::Device,
    UML2WithID::Artifact,
    UML2WithID::NamedElement,
    UML2WithID::ActivityParameterNode,
    UML2WithID::BehavioredClassifier,
    UML2WithID::DestroyLinkAction,
    UML2WithID::Feature,
    UML2WithID::Pin,
    UML2WithID::Type,
    UML2WithID::AddStructuralFeatureValueAction,
    UML2WithID::CombinedFragment,
    UML2WithID::OpaqueExpression,
    UML2WithID::Extension,
    UML2WithID::MergeNode,
    UML2WithID::TimeInterval,
    UML2WithID::PackageableElement,
    UML2WithID::FinalState,
    UML2WithID::Implementation,
    UML2WithID::Behavior,
    UML2WithID::StructuredClassifier,
    UML2WithID::EncapsulatedClassifier,
    UML2WithID::InteractionOccurrence,
    UML2WithID::Message,
    UML2WithID::TimeConstraint,
    UML2WithID::Model,
    UML2WithID::Namespace,
    UML2WithID::Interval,
    UML2WithID::ChangeTrigger,
    UML2WithID::InstanceSpecification,
    UML2WithID::Operation,
    UML2WithID::ExecutionEnvironment,
    UML2WithID::Trigger,
    UML2WithID::StateInvariant,
    UML2WithID::LiteralString,
    UML2WithID::Constraint,
    UML2WithID::DeploymentTarget,
    UML2WithID::ExecutionOccurrence,
    UML2WithID::Gate,
    UML2WithID::Deployment,
    UML2WithID::CommunicationPath,
    UML2WithID::LiteralInteger,
    UML2WithID::FlowFinalNode,
    UML2WithID::Connector,
    UML2WithID::DurationObservationAction,
    UML2WithID::InformationItem,
    UML2WithID::Classifier,
    UML2WithID::Pseudostate,
    UML2WithID::LoopNode,
    UML2WithID::Action,
    UML2WithID::DeployedArtifact,
    UML2WithID::ExpansionRegion,
    UML2WithID::Permission,
    UML2WithID::InstanceValue,
    UML2WithID::JoinNode,
    UML2WithID::Transition,
    UML2WithID::ExpansionNode,
    UML2WithID::Lifeline,
    UML2WithID::SendSignalAction,
    UML2WithID::PrimitiveFunction,
    UML2WithID::Extend,
    UML2WithID::ConnectableElement,
    UML2WithID::Stereotype,
    UML2WithID::RemoveStructuralFeatureValueAction,
    UML2WithID::ProtocolTransition,
    UML2WithID::Collaboration,
    UML2WithID::ValuePin,
    UML2WithID::CallTrigger,
    UML2WithID::State,
    UML2WithID::TemplateableClassifier,
    UML2WithID::LiteralSpecification,
    UML2WithID::ObjectFlow,
    UML2WithID::Component,
    UML2WithID::RedefinableElement,
    UML2WithID::OutputPin,
    UML2WithID::ControlFlow,
    UML2WithID::Dependency,
    UML2WithID::CreateLinkObjectAction,
    UML2WithID::CallBehaviorAction,
    UML2WithID::PrimitiveType,
    UML2WithID::ReadStructuralFeatureAction,
    UML2WithID::EnumerationLiteral,
    Action,
    UML2WithID::TestIdentityAction,
    UML2WithID::ReadExtentAction,
    UML2WithID::StructuralFeatureAction,
    UML2WithID::ApplyFunctionAction,
    UML2WithID::RaiseExceptionAction,
    UML2WithID::ReadIsClassifiedObjectAction,
    UML2WithID::VariableAction,
    UML2WithID::StartOwnedBehaviorAction,
    UML2WithID::ReclassifyObjectAction,
    UML2WithID::StructuredActivityNode,
    UML2WithID::AcceptEventAction,
    UML2WithID::LinkAction,
    UML2WithID::ReplyAction,
    UML2WithID::ReadLinkObjectEndAction,
    UML2WithID::ReadSelfAction,
    UML2WithID::InvocationAction,
    UML2WithID::ClearAssociationAction,
    UML2WithID::ReadLinkObjectEndQualifierAction,
    Constraint,
    UML2WithID::IntervalConstraint,
    UML2WithID::InteractionConstraint,
    WriteVariableAction,
    UML2WithID::RemoveVariableValueAction,
    UML2WithID::AddVariableValueAction,
    UML2WithID::DestroyObjectAction,
    LinkAction,
    UML2WithID::WriteLinkAction,
    UML2WithID::ReadLinkAction,
    UML2WithID::CreateObjectAction,
    CentralBufferNode,
    UML2WithID::DataStoreNode,
    ConnectableElement,
    UML2WithID::Parameter,
    UML2WithID::Property,
    UML2WithID::Variable,
    UML2WithID::ExtensionPoint,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2withid::element_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Element)


def test_uml2withid::element_constructor_exists():
    assert callable(UML2WithID::Element.__init__)


def test_uml2withid::element_constructor_args():
    sig = inspect.signature(UML2WithID::Element.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_uml2withid::element_has_ID():
    assert hasattr(UML2WithID::Element, "ID")
    descriptor = None
    for klass in UML2WithID::Element.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_messagetrigger_is_not_abstract():
    assert not inspect.isabstract(MessageTrigger)


def test_messagetrigger_constructor_exists():
    assert callable(MessageTrigger.__init__)


def test_messagetrigger_constructor_args():
    sig = inspect.signature(MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(InteractionOccurrence)


def test_interactionoccurrence_constructor_exists():
    assert callable(InteractionOccurrence.__init__)


def test_interactionoccurrence_constructor_args():
    sig = inspect.signature(InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::anytrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AnyTrigger)


def test_uml2withid::anytrigger_constructor_exists():
    assert callable(UML2WithID::AnyTrigger.__init__)


def test_uml2withid::anytrigger_constructor_args():
    sig = inspect.signature(UML2WithID::AnyTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::duration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Duration)


def test_uml2withid::duration_constructor_exists():
    assert callable(UML2WithID::Duration.__init__)


def test_uml2withid::duration_constructor_args():
    sig = inspect.signature(UML2WithID::Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::collaborationoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CollaborationOccurrence)


def test_uml2withid::collaborationoccurrence_constructor_exists():
    assert callable(UML2WithID::CollaborationOccurrence.__init__)


def test_uml2withid::collaborationoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID::CollaborationOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InteractionOperand)


def test_uml2withid::interactionoperand_constructor_exists():
    assert callable(UML2WithID::InteractionOperand.__init__)


def test_uml2withid::interactionoperand_constructor_args():
    sig = inspect.signature(UML2WithID::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::abstraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Abstraction)


def test_uml2withid::abstraction_constructor_exists():
    assert callable(UML2WithID::Abstraction.__init__)


def test_uml2withid::abstraction_constructor_args():
    sig = inspect.signature(UML2WithID::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Enumeration)


def test_uml2withid::enumeration_constructor_exists():
    assert callable(UML2WithID::Enumeration.__init__)


def test_uml2withid::enumeration_constructor_args():
    sig = inspect.signature(UML2WithID::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LiteralUnlimitedNatural)


def test_uml2withid::literalunlimitednatural_constructor_exists():
    assert callable(UML2WithID::LiteralUnlimitedNatural.__init__)


def test_uml2withid::literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2WithID::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::stop_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Stop)


def test_uml2withid::stop_constructor_exists():
    assert callable(UML2WithID::Stop.__init__)


def test_uml2withid::stop_constructor_args():
    sig = inspect.signature(UML2WithID::Stop.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::WriteStructuralFeatureAction)


def test_uml2withid::writestructuralfeatureaction_constructor_exists():
    assert callable(UML2WithID::WriteStructuralFeatureAction.__init__)


def test_uml2withid::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ActivityFinalNode)


def test_uml2withid::activityfinalnode_constructor_exists():
    assert callable(UML2WithID::ActivityFinalNode.__init__)


def test_uml2withid::activityfinalnode_constructor_args():
    sig = inspect.signature(UML2WithID::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ConditionalNode)


def test_uml2withid::conditionalnode_constructor_exists():
    assert callable(UML2WithID::ConditionalNode.__init__)


def test_uml2withid::conditionalnode_constructor_args():
    sig = inspect.signature(UML2WithID::ConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ProtocolStateMachine)


def test_uml2withid::protocolstatemachine_constructor_exists():
    assert callable(UML2WithID::ProtocolStateMachine.__init__)


def test_uml2withid::protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2WithID::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::activitynode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ActivityNode)


def test_uml2withid::activitynode_constructor_exists():
    assert callable(UML2WithID::ActivityNode.__init__)


def test_uml2withid::activitynode_constructor_args():
    sig = inspect.signature(UML2WithID::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::executablenode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExecutableNode)


def test_uml2withid::executablenode_constructor_exists():
    assert callable(UML2WithID::ExecutableNode.__init__)


def test_uml2withid::executablenode_constructor_args():
    sig = inspect.signature(UML2WithID::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::manifestation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Manifestation)


def test_uml2withid::manifestation_constructor_exists():
    assert callable(UML2WithID::Manifestation.__init__)


def test_uml2withid::manifestation_constructor_args():
    sig = inspect.signature(UML2WithID::Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::generalizationset_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::GeneralizationSet)


def test_uml2withid::generalizationset_constructor_exists():
    assert callable(UML2WithID::GeneralizationSet.__init__)


def test_uml2withid::generalizationset_constructor_args():
    sig = inspect.signature(UML2WithID::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TypedElement)


def test_uml2withid::typedelement_constructor_exists():
    assert callable(UML2WithID::TypedElement.__init__)


def test_uml2withid::typedelement_constructor_args():
    sig = inspect.signature(UML2WithID::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DurationInterval)


def test_uml2withid::durationinterval_constructor_exists():
    assert callable(UML2WithID::DurationInterval.__init__)


def test_uml2withid::durationinterval_constructor_args():
    sig = inspect.signature(UML2WithID::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CreateLinkAction)


def test_uml2withid::createlinkaction_constructor_exists():
    assert callable(UML2WithID::CreateLinkAction.__init__)


def test_uml2withid::createlinkaction_constructor_args():
    sig = inspect.signature(UML2WithID::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::controlnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ControlNode)


def test_uml2withid::controlnode_constructor_exists():
    assert callable(UML2WithID::ControlNode.__init__)


def test_uml2withid::controlnode_constructor_args():
    sig = inspect.signature(UML2WithID::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::class_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Class)


def test_uml2withid::class_constructor_exists():
    assert callable(UML2WithID::Class.__init__)


def test_uml2withid::class_constructor_args():
    sig = inspect.signature(UML2WithID::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::datatype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DataType)


def test_uml2withid::datatype_constructor_exists():
    assert callable(UML2WithID::DataType.__init__)


def test_uml2withid::datatype_constructor_args():
    sig = inspect.signature(UML2WithID::DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadVariableAction)


def test_uml2withid::readvariableaction_constructor_exists():
    assert callable(UML2WithID::ReadVariableAction.__init__)


def test_uml2withid::readvariableaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::reception_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Reception)


def test_uml2withid::reception_constructor_exists():
    assert callable(UML2WithID::Reception.__init__)


def test_uml2withid::reception_constructor_args():
    sig = inspect.signature(UML2WithID::Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LiteralBoolean)


def test_uml2withid::literalboolean_constructor_exists():
    assert callable(UML2WithID::LiteralBoolean.__init__)


def test_uml2withid::literalboolean_constructor_args():
    sig = inspect.signature(UML2WithID::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::expression_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Expression)


def test_uml2withid::expression_constructor_exists():
    assert callable(UML2WithID::Expression.__init__)


def test_uml2withid::expression_constructor_args():
    sig = inspect.signature(UML2WithID::Expression.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DurationConstraint)


def test_uml2withid::durationconstraint_constructor_exists():
    assert callable(UML2WithID::DurationConstraint.__init__)


def test_uml2withid::durationconstraint_constructor_args():
    sig = inspect.signature(UML2WithID::DurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DeploymentSpecification)


def test_uml2withid::deploymentspecification_constructor_exists():
    assert callable(UML2WithID::DeploymentSpecification.__init__)


def test_uml2withid::deploymentspecification_constructor_args():
    sig = inspect.signature(UML2WithID::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LiteralNull)


def test_uml2withid::literalnull_constructor_exists():
    assert callable(UML2WithID::LiteralNull.__init__)


def test_uml2withid::literalnull_constructor_args():
    sig = inspect.signature(UML2WithID::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::RedefinableTemplateSignature)


def test_uml2withid::redefinabletemplatesignature_constructor_exists():
    assert callable(UML2WithID::RedefinableTemplateSignature.__init__)


def test_uml2withid::redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(UML2WithID::RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::activitypartition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ActivityPartition)


def test_uml2withid::activitypartition_constructor_exists():
    assert callable(UML2WithID::ActivityPartition.__init__)


def test_uml2withid::activitypartition_constructor_args():
    sig = inspect.signature(UML2WithID::ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::BroadcastSignalAction)


def test_uml2withid::broadcastsignalaction_constructor_exists():
    assert callable(UML2WithID::BroadcastSignalAction.__init__)


def test_uml2withid::broadcastsignalaction_constructor_args():
    sig = inspect.signature(UML2WithID::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TimeExpression)


def test_uml2withid::timeexpression_constructor_exists():
    assert callable(UML2WithID::TimeExpression.__init__)


def test_uml2withid::timeexpression_constructor_args():
    sig = inspect.signature(UML2WithID::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::forknode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ForkNode)


def test_uml2withid::forknode_constructor_exists():
    assert callable(UML2WithID::ForkNode.__init__)


def test_uml2withid::forknode_constructor_args():
    sig = inspect.signature(UML2WithID::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExtensionEnd)


def test_uml2withid::extensionend_constructor_exists():
    assert callable(UML2WithID::ExtensionEnd.__init__)


def test_uml2withid::extensionend_constructor_args():
    sig = inspect.signature(UML2WithID::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CallOperationAction)


def test_uml2withid::calloperationaction_constructor_exists():
    assert callable(UML2WithID::CallOperationAction.__init__)


def test_uml2withid::calloperationaction_constructor_args():
    sig = inspect.signature(UML2WithID::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::WriteVariableAction)


def test_uml2withid::writevariableaction_constructor_exists():
    assert callable(UML2WithID::WriteVariableAction.__init__)


def test_uml2withid::writevariableaction_constructor_args():
    sig = inspect.signature(UML2WithID::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::messagetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::MessageTrigger)


def test_uml2withid::messagetrigger_constructor_exists():
    assert callable(UML2WithID::MessageTrigger.__init__)


def test_uml2withid::messagetrigger_constructor_args():
    sig = inspect.signature(UML2WithID::MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::activityedge_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ActivityEdge)


def test_uml2withid::activityedge_constructor_exists():
    assert callable(UML2WithID::ActivityEdge.__init__)


def test_uml2withid::activityedge_constructor_args():
    sig = inspect.signature(UML2WithID::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::UseCase)


def test_uml2withid::usecase_constructor_exists():
    assert callable(UML2WithID::UseCase.__init__)


def test_uml2withid::usecase_constructor_args():
    sig = inspect.signature(UML2WithID::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::EventOccurrence)


def test_uml2withid::eventoccurrence_constructor_exists():
    assert callable(UML2WithID::EventOccurrence.__init__)


def test_uml2withid::eventoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID::EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StructuralFeature)


def test_uml2withid::structuralfeature_constructor_exists():
    assert callable(UML2WithID::StructuralFeature.__init__)


def test_uml2withid::structuralfeature_constructor_args():
    sig = inspect.signature(UML2WithID::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ObjectNode)


def test_uml2withid::objectnode_constructor_exists():
    assert callable(UML2WithID::ObjectNode.__init__)


def test_uml2withid::objectnode_constructor_args():
    sig = inspect.signature(UML2WithID::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AssociationClass)


def test_uml2withid::associationclass_constructor_exists():
    assert callable(UML2WithID::AssociationClass.__init__)


def test_uml2withid::associationclass_constructor_args():
    sig = inspect.signature(UML2WithID::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InputPin)


def test_uml2withid::inputpin_constructor_exists():
    assert callable(UML2WithID::InputPin.__init__)


def test_uml2withid::inputpin_constructor_args():
    sig = inspect.signature(UML2WithID::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::callaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CallAction)


def test_uml2withid::callaction_constructor_exists():
    assert callable(UML2WithID::CallAction.__init__)


def test_uml2withid::callaction_constructor_args():
    sig = inspect.signature(UML2WithID::CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::association_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Association)


def test_uml2withid::association_constructor_exists():
    assert callable(UML2WithID::Association.__init__)


def test_uml2withid::association_constructor_args():
    sig = inspect.signature(UML2WithID::Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::signaltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::SignalTrigger)


def test_uml2withid::signaltrigger_constructor_exists():
    assert callable(UML2WithID::SignalTrigger.__init__)


def test_uml2withid::signaltrigger_constructor_args():
    sig = inspect.signature(UML2WithID::SignalTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Interaction)


def test_uml2withid::interaction_constructor_exists():
    assert callable(UML2WithID::Interaction.__init__)


def test_uml2withid::interaction_constructor_args():
    sig = inspect.signature(UML2WithID::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ClearVariableAction)


def test_uml2withid::clearvariableaction_constructor_exists():
    assert callable(UML2WithID::ClearVariableAction.__init__)


def test_uml2withid::clearvariableaction_constructor_args():
    sig = inspect.signature(UML2WithID::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::continuation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Continuation)


def test_uml2withid::continuation_constructor_exists():
    assert callable(UML2WithID::Continuation.__init__)


def test_uml2withid::continuation_constructor_args():
    sig = inspect.signature(UML2WithID::Continuation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::timetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TimeTrigger)


def test_uml2withid::timetrigger_constructor_exists():
    assert callable(UML2WithID::TimeTrigger.__init__)


def test_uml2withid::timetrigger_constructor_args():
    sig = inspect.signature(UML2WithID::TimeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CentralBufferNode)


def test_uml2withid::centralbuffernode_constructor_exists():
    assert callable(UML2WithID::CentralBufferNode.__init__)


def test_uml2withid::centralbuffernode_constructor_args():
    sig = inspect.signature(UML2WithID::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::partdecomposition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::PartDecomposition)


def test_uml2withid::partdecomposition_constructor_exists():
    assert callable(UML2WithID::PartDecomposition.__init__)


def test_uml2withid::partdecomposition_constructor_args():
    sig = inspect.signature(UML2WithID::PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::usage_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Usage)


def test_uml2withid::usage_constructor_exists():
    assert callable(UML2WithID::Usage.__init__)


def test_uml2withid::usage_constructor_args():
    sig = inspect.signature(UML2WithID::Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::port_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Port)


def test_uml2withid::port_constructor_exists():
    assert callable(UML2WithID::Port.__init__)


def test_uml2withid::port_constructor_args():
    sig = inspect.signature(UML2WithID::Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::actor_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Actor)


def test_uml2withid::actor_constructor_exists():
    assert callable(UML2WithID::Actor.__init__)


def test_uml2withid::actor_constructor_args():
    sig = inspect.signature(UML2WithID::Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ValueSpecification)


def test_uml2withid::valuespecification_constructor_exists():
    assert callable(UML2WithID::ValueSpecification.__init__)


def test_uml2withid::valuespecification_constructor_args():
    sig = inspect.signature(UML2WithID::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::package_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Package)


def test_uml2withid::package_constructor_exists():
    assert callable(UML2WithID::Package.__init__)


def test_uml2withid::package_constructor_args():
    sig = inspect.signature(UML2WithID::Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::signal_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Signal)


def test_uml2withid::signal_constructor_exists():
    assert callable(UML2WithID::Signal.__init__)


def test_uml2withid::signal_constructor_args():
    sig = inspect.signature(UML2WithID::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ConnectionPointReference)


def test_uml2withid::connectionpointreference_constructor_exists():
    assert callable(UML2WithID::ConnectionPointReference.__init__)


def test_uml2withid::connectionpointreference_constructor_args():
    sig = inspect.signature(UML2WithID::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ClearStructuralFeatureAction)


def test_uml2withid::clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2WithID::ClearStructuralFeatureAction.__init__)


def test_uml2withid::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::profile_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Profile)


def test_uml2withid::profile_constructor_exists():
    assert callable(UML2WithID::Profile.__init__)


def test_uml2withid::profile_constructor_args():
    sig = inspect.signature(UML2WithID::Profile.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::BehavioralFeature)


def test_uml2withid::behavioralfeature_constructor_exists():
    assert callable(UML2WithID::BehavioralFeature.__init__)


def test_uml2withid::behavioralfeature_constructor_args():
    sig = inspect.signature(UML2WithID::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::informationflow_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InformationFlow)


def test_uml2withid::informationflow_constructor_exists():
    assert callable(UML2WithID::InformationFlow.__init__)


def test_uml2withid::informationflow_constructor_args():
    sig = inspect.signature(UML2WithID::InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::region_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Region)


def test_uml2withid::region_constructor_exists():
    assert callable(UML2WithID::Region.__init__)


def test_uml2withid::region_constructor_args():
    sig = inspect.signature(UML2WithID::Region.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::include_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Include)


def test_uml2withid::include_constructor_exists():
    assert callable(UML2WithID::Include.__init__)


def test_uml2withid::include_constructor_args():
    sig = inspect.signature(UML2WithID::Include.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::substitution_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Substitution)


def test_uml2withid::substitution_constructor_exists():
    assert callable(UML2WithID::Substitution.__init__)


def test_uml2withid::substitution_constructor_args():
    sig = inspect.signature(UML2WithID::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::vertex_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Vertex)


def test_uml2withid::vertex_constructor_exists():
    assert callable(UML2WithID::Vertex.__init__)


def test_uml2withid::vertex_constructor_args():
    sig = inspect.signature(UML2WithID::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::messageend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::MessageEnd)


def test_uml2withid::messageend_constructor_exists():
    assert callable(UML2WithID::MessageEnd.__init__)


def test_uml2withid::messageend_constructor_args():
    sig = inspect.signature(UML2WithID::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interface_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Interface)


def test_uml2withid::interface_constructor_exists():
    assert callable(UML2WithID::Interface.__init__)


def test_uml2withid::interface_constructor_args():
    sig = inspect.signature(UML2WithID::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::parameterset_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ParameterSet)


def test_uml2withid::parameterset_constructor_exists():
    assert callable(UML2WithID::ParameterSet.__init__)


def test_uml2withid::parameterset_constructor_args():
    sig = inspect.signature(UML2WithID::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::decisionnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DecisionNode)


def test_uml2withid::decisionnode_constructor_exists():
    assert callable(UML2WithID::DecisionNode.__init__)


def test_uml2withid::decisionnode_constructor_args():
    sig = inspect.signature(UML2WithID::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InteractionFragment)


def test_uml2withid::interactionfragment_constructor_exists():
    assert callable(UML2WithID::InteractionFragment.__init__)


def test_uml2withid::interactionfragment_constructor_args():
    sig = inspect.signature(UML2WithID::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StateMachine)


def test_uml2withid::statemachine_constructor_exists():
    assert callable(UML2WithID::StateMachine.__init__)


def test_uml2withid::statemachine_constructor_args():
    sig = inspect.signature(UML2WithID::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::node_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Node)


def test_uml2withid::node_constructor_exists():
    assert callable(UML2WithID::Node.__init__)


def test_uml2withid::node_constructor_args():
    sig = inspect.signature(UML2WithID::Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TimeObservationAction)


def test_uml2withid::timeobservationaction_constructor_exists():
    assert callable(UML2WithID::TimeObservationAction.__init__)


def test_uml2withid::timeobservationaction_constructor_args():
    sig = inspect.signature(UML2WithID::TimeObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::SendObjectAction)


def test_uml2withid::sendobjectaction_constructor_exists():
    assert callable(UML2WithID::SendObjectAction.__init__)


def test_uml2withid::sendobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::generalordering_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::GeneralOrdering)


def test_uml2withid::generalordering_constructor_exists():
    assert callable(UML2WithID::GeneralOrdering.__init__)


def test_uml2withid::generalordering_constructor_args():
    sig = inspect.signature(UML2WithID::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ParameterableClassifier)


def test_uml2withid::parameterableclassifier_constructor_exists():
    assert callable(UML2WithID::ParameterableClassifier.__init__)


def test_uml2withid::parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::activity_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Activity)


def test_uml2withid::activity_constructor_exists():
    assert callable(UML2WithID::Activity.__init__)


def test_uml2withid::activity_constructor_args():
    sig = inspect.signature(UML2WithID::Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::finalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::FinalNode)


def test_uml2withid::finalnode_constructor_exists():
    assert callable(UML2WithID::FinalNode.__init__)


def test_uml2withid::finalnode_constructor_args():
    sig = inspect.signature(UML2WithID::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AcceptCallAction)


def test_uml2withid::acceptcallaction_constructor_exists():
    assert callable(UML2WithID::AcceptCallAction.__init__)


def test_uml2withid::acceptcallaction_constructor_args():
    sig = inspect.signature(UML2WithID::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::realization_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Realization)


def test_uml2withid::realization_constructor_exists():
    assert callable(UML2WithID::Realization.__init__)


def test_uml2withid::realization_constructor_args():
    sig = inspect.signature(UML2WithID::Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::initialnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InitialNode)


def test_uml2withid::initialnode_constructor_exists():
    assert callable(UML2WithID::InitialNode.__init__)


def test_uml2withid::initialnode_constructor_args():
    sig = inspect.signature(UML2WithID::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::device_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Device)


def test_uml2withid::device_constructor_exists():
    assert callable(UML2WithID::Device.__init__)


def test_uml2withid::device_constructor_args():
    sig = inspect.signature(UML2WithID::Device.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::artifact_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Artifact)


def test_uml2withid::artifact_constructor_exists():
    assert callable(UML2WithID::Artifact.__init__)


def test_uml2withid::artifact_constructor_args():
    sig = inspect.signature(UML2WithID::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::namedelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::NamedElement)


def test_uml2withid::namedelement_constructor_exists():
    assert callable(UML2WithID::NamedElement.__init__)


def test_uml2withid::namedelement_constructor_args():
    sig = inspect.signature(UML2WithID::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml2withid::namedelement_has_visibility():
    assert hasattr(UML2WithID::NamedElement, "visibility")
    descriptor = None
    for klass in UML2WithID::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml2withid::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ActivityParameterNode)


def test_uml2withid::activityparameternode_constructor_exists():
    assert callable(UML2WithID::ActivityParameterNode.__init__)


def test_uml2withid::activityparameternode_constructor_args():
    sig = inspect.signature(UML2WithID::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::BehavioredClassifier)


def test_uml2withid::behavioredclassifier_constructor_exists():
    assert callable(UML2WithID::BehavioredClassifier.__init__)


def test_uml2withid::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DestroyLinkAction)


def test_uml2withid::destroylinkaction_constructor_exists():
    assert callable(UML2WithID::DestroyLinkAction.__init__)


def test_uml2withid::destroylinkaction_constructor_args():
    sig = inspect.signature(UML2WithID::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::feature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Feature)


def test_uml2withid::feature_constructor_exists():
    assert callable(UML2WithID::Feature.__init__)


def test_uml2withid::feature_constructor_args():
    sig = inspect.signature(UML2WithID::Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::pin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Pin)


def test_uml2withid::pin_constructor_exists():
    assert callable(UML2WithID::Pin.__init__)


def test_uml2withid::pin_constructor_args():
    sig = inspect.signature(UML2WithID::Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::type_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Type)


def test_uml2withid::type_constructor_exists():
    assert callable(UML2WithID::Type.__init__)


def test_uml2withid::type_constructor_args():
    sig = inspect.signature(UML2WithID::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AddStructuralFeatureValueAction)


def test_uml2withid::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2WithID::AddStructuralFeatureValueAction.__init__)


def test_uml2withid::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CombinedFragment)


def test_uml2withid::combinedfragment_constructor_exists():
    assert callable(UML2WithID::CombinedFragment.__init__)


def test_uml2withid::combinedfragment_constructor_args():
    sig = inspect.signature(UML2WithID::CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::OpaqueExpression)


def test_uml2withid::opaqueexpression_constructor_exists():
    assert callable(UML2WithID::OpaqueExpression.__init__)


def test_uml2withid::opaqueexpression_constructor_args():
    sig = inspect.signature(UML2WithID::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extension_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Extension)


def test_uml2withid::extension_constructor_exists():
    assert callable(UML2WithID::Extension.__init__)


def test_uml2withid::extension_constructor_args():
    sig = inspect.signature(UML2WithID::Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::mergenode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::MergeNode)


def test_uml2withid::mergenode_constructor_exists():
    assert callable(UML2WithID::MergeNode.__init__)


def test_uml2withid::mergenode_constructor_args():
    sig = inspect.signature(UML2WithID::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TimeInterval)


def test_uml2withid::timeinterval_constructor_exists():
    assert callable(UML2WithID::TimeInterval.__init__)


def test_uml2withid::timeinterval_constructor_args():
    sig = inspect.signature(UML2WithID::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::packageableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::PackageableElement)


def test_uml2withid::packageableelement_constructor_exists():
    assert callable(UML2WithID::PackageableElement.__init__)


def test_uml2withid::packageableelement_constructor_args():
    sig = inspect.signature(UML2WithID::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::finalstate_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::FinalState)


def test_uml2withid::finalstate_constructor_exists():
    assert callable(UML2WithID::FinalState.__init__)


def test_uml2withid::finalstate_constructor_args():
    sig = inspect.signature(UML2WithID::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::implementation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Implementation)


def test_uml2withid::implementation_constructor_exists():
    assert callable(UML2WithID::Implementation.__init__)


def test_uml2withid::implementation_constructor_args():
    sig = inspect.signature(UML2WithID::Implementation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Behavior)


def test_uml2withid::behavior_constructor_exists():
    assert callable(UML2WithID::Behavior.__init__)


def test_uml2withid::behavior_constructor_args():
    sig = inspect.signature(UML2WithID::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StructuredClassifier)


def test_uml2withid::structuredclassifier_constructor_exists():
    assert callable(UML2WithID::StructuredClassifier.__init__)


def test_uml2withid::structuredclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::EncapsulatedClassifier)


def test_uml2withid::encapsulatedclassifier_constructor_exists():
    assert callable(UML2WithID::EncapsulatedClassifier.__init__)


def test_uml2withid::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InteractionOccurrence)


def test_uml2withid::interactionoccurrence_constructor_exists():
    assert callable(UML2WithID::InteractionOccurrence.__init__)


def test_uml2withid::interactionoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID::InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::message_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Message)


def test_uml2withid::message_constructor_exists():
    assert callable(UML2WithID::Message.__init__)


def test_uml2withid::message_constructor_args():
    sig = inspect.signature(UML2WithID::Message.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TimeConstraint)


def test_uml2withid::timeconstraint_constructor_exists():
    assert callable(UML2WithID::TimeConstraint.__init__)


def test_uml2withid::timeconstraint_constructor_args():
    sig = inspect.signature(UML2WithID::TimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::model_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Model)


def test_uml2withid::model_constructor_exists():
    assert callable(UML2WithID::Model.__init__)


def test_uml2withid::model_constructor_args():
    sig = inspect.signature(UML2WithID::Model.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::namespace_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Namespace)


def test_uml2withid::namespace_constructor_exists():
    assert callable(UML2WithID::Namespace.__init__)


def test_uml2withid::namespace_constructor_args():
    sig = inspect.signature(UML2WithID::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interval_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Interval)


def test_uml2withid::interval_constructor_exists():
    assert callable(UML2WithID::Interval.__init__)


def test_uml2withid::interval_constructor_args():
    sig = inspect.signature(UML2WithID::Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::changetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ChangeTrigger)


def test_uml2withid::changetrigger_constructor_exists():
    assert callable(UML2WithID::ChangeTrigger.__init__)


def test_uml2withid::changetrigger_constructor_args():
    sig = inspect.signature(UML2WithID::ChangeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::instancespecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InstanceSpecification)


def test_uml2withid::instancespecification_constructor_exists():
    assert callable(UML2WithID::InstanceSpecification.__init__)


def test_uml2withid::instancespecification_constructor_args():
    sig = inspect.signature(UML2WithID::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::operation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Operation)


def test_uml2withid::operation_constructor_exists():
    assert callable(UML2WithID::Operation.__init__)


def test_uml2withid::operation_constructor_args():
    sig = inspect.signature(UML2WithID::Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExecutionEnvironment)


def test_uml2withid::executionenvironment_constructor_exists():
    assert callable(UML2WithID::ExecutionEnvironment.__init__)


def test_uml2withid::executionenvironment_constructor_args():
    sig = inspect.signature(UML2WithID::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::trigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Trigger)


def test_uml2withid::trigger_constructor_exists():
    assert callable(UML2WithID::Trigger.__init__)


def test_uml2withid::trigger_constructor_args():
    sig = inspect.signature(UML2WithID::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::stateinvariant_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StateInvariant)


def test_uml2withid::stateinvariant_constructor_exists():
    assert callable(UML2WithID::StateInvariant.__init__)


def test_uml2withid::stateinvariant_constructor_args():
    sig = inspect.signature(UML2WithID::StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LiteralString)


def test_uml2withid::literalstring_constructor_exists():
    assert callable(UML2WithID::LiteralString.__init__)


def test_uml2withid::literalstring_constructor_args():
    sig = inspect.signature(UML2WithID::LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::constraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Constraint)


def test_uml2withid::constraint_constructor_exists():
    assert callable(UML2WithID::Constraint.__init__)


def test_uml2withid::constraint_constructor_args():
    sig = inspect.signature(UML2WithID::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DeploymentTarget)


def test_uml2withid::deploymenttarget_constructor_exists():
    assert callable(UML2WithID::DeploymentTarget.__init__)


def test_uml2withid::deploymenttarget_constructor_args():
    sig = inspect.signature(UML2WithID::DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::executionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExecutionOccurrence)


def test_uml2withid::executionoccurrence_constructor_exists():
    assert callable(UML2WithID::ExecutionOccurrence.__init__)


def test_uml2withid::executionoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID::ExecutionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::gate_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Gate)


def test_uml2withid::gate_constructor_exists():
    assert callable(UML2WithID::Gate.__init__)


def test_uml2withid::gate_constructor_args():
    sig = inspect.signature(UML2WithID::Gate.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::deployment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Deployment)


def test_uml2withid::deployment_constructor_exists():
    assert callable(UML2WithID::Deployment.__init__)


def test_uml2withid::deployment_constructor_args():
    sig = inspect.signature(UML2WithID::Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CommunicationPath)


def test_uml2withid::communicationpath_constructor_exists():
    assert callable(UML2WithID::CommunicationPath.__init__)


def test_uml2withid::communicationpath_constructor_args():
    sig = inspect.signature(UML2WithID::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::literalinteger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LiteralInteger)


def test_uml2withid::literalinteger_constructor_exists():
    assert callable(UML2WithID::LiteralInteger.__init__)


def test_uml2withid::literalinteger_constructor_args():
    sig = inspect.signature(UML2WithID::LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::FlowFinalNode)


def test_uml2withid::flowfinalnode_constructor_exists():
    assert callable(UML2WithID::FlowFinalNode.__init__)


def test_uml2withid::flowfinalnode_constructor_args():
    sig = inspect.signature(UML2WithID::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::connector_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Connector)


def test_uml2withid::connector_constructor_exists():
    assert callable(UML2WithID::Connector.__init__)


def test_uml2withid::connector_constructor_args():
    sig = inspect.signature(UML2WithID::Connector.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DurationObservationAction)


def test_uml2withid::durationobservationaction_constructor_exists():
    assert callable(UML2WithID::DurationObservationAction.__init__)


def test_uml2withid::durationobservationaction_constructor_args():
    sig = inspect.signature(UML2WithID::DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InformationItem)


def test_uml2withid::informationitem_constructor_exists():
    assert callable(UML2WithID::InformationItem.__init__)


def test_uml2withid::informationitem_constructor_args():
    sig = inspect.signature(UML2WithID::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::classifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Classifier)


def test_uml2withid::classifier_constructor_exists():
    assert callable(UML2WithID::Classifier.__init__)


def test_uml2withid::classifier_constructor_args():
    sig = inspect.signature(UML2WithID::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::pseudostate_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Pseudostate)


def test_uml2withid::pseudostate_constructor_exists():
    assert callable(UML2WithID::Pseudostate.__init__)


def test_uml2withid::pseudostate_constructor_args():
    sig = inspect.signature(UML2WithID::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::loopnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LoopNode)


def test_uml2withid::loopnode_constructor_exists():
    assert callable(UML2WithID::LoopNode.__init__)


def test_uml2withid::loopnode_constructor_args():
    sig = inspect.signature(UML2WithID::LoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::action_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Action)


def test_uml2withid::action_constructor_exists():
    assert callable(UML2WithID::Action.__init__)


def test_uml2withid::action_constructor_args():
    sig = inspect.signature(UML2WithID::Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::deployedartifact_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DeployedArtifact)


def test_uml2withid::deployedartifact_constructor_exists():
    assert callable(UML2WithID::DeployedArtifact.__init__)


def test_uml2withid::deployedartifact_constructor_args():
    sig = inspect.signature(UML2WithID::DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExpansionRegion)


def test_uml2withid::expansionregion_constructor_exists():
    assert callable(UML2WithID::ExpansionRegion.__init__)


def test_uml2withid::expansionregion_constructor_args():
    sig = inspect.signature(UML2WithID::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::permission_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Permission)


def test_uml2withid::permission_constructor_exists():
    assert callable(UML2WithID::Permission.__init__)


def test_uml2withid::permission_constructor_args():
    sig = inspect.signature(UML2WithID::Permission.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InstanceValue)


def test_uml2withid::instancevalue_constructor_exists():
    assert callable(UML2WithID::InstanceValue.__init__)


def test_uml2withid::instancevalue_constructor_args():
    sig = inspect.signature(UML2WithID::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::joinnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::JoinNode)


def test_uml2withid::joinnode_constructor_exists():
    assert callable(UML2WithID::JoinNode.__init__)


def test_uml2withid::joinnode_constructor_args():
    sig = inspect.signature(UML2WithID::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::transition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Transition)


def test_uml2withid::transition_constructor_exists():
    assert callable(UML2WithID::Transition.__init__)


def test_uml2withid::transition_constructor_args():
    sig = inspect.signature(UML2WithID::Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExpansionNode)


def test_uml2withid::expansionnode_constructor_exists():
    assert callable(UML2WithID::ExpansionNode.__init__)


def test_uml2withid::expansionnode_constructor_args():
    sig = inspect.signature(UML2WithID::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::lifeline_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Lifeline)


def test_uml2withid::lifeline_constructor_exists():
    assert callable(UML2WithID::Lifeline.__init__)


def test_uml2withid::lifeline_constructor_args():
    sig = inspect.signature(UML2WithID::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::SendSignalAction)


def test_uml2withid::sendsignalaction_constructor_exists():
    assert callable(UML2WithID::SendSignalAction.__init__)


def test_uml2withid::sendsignalaction_constructor_args():
    sig = inspect.signature(UML2WithID::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::primitivefunction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::PrimitiveFunction)


def test_uml2withid::primitivefunction_constructor_exists():
    assert callable(UML2WithID::PrimitiveFunction.__init__)


def test_uml2withid::primitivefunction_constructor_args():
    sig = inspect.signature(UML2WithID::PrimitiveFunction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Extend)


def test_uml2withid::extend_constructor_exists():
    assert callable(UML2WithID::Extend.__init__)


def test_uml2withid::extend_constructor_args():
    sig = inspect.signature(UML2WithID::Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::connectableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ConnectableElement)


def test_uml2withid::connectableelement_constructor_exists():
    assert callable(UML2WithID::ConnectableElement.__init__)


def test_uml2withid::connectableelement_constructor_args():
    sig = inspect.signature(UML2WithID::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Stereotype)


def test_uml2withid::stereotype_constructor_exists():
    assert callable(UML2WithID::Stereotype.__init__)


def test_uml2withid::stereotype_constructor_args():
    sig = inspect.signature(UML2WithID::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::RemoveStructuralFeatureValueAction)


def test_uml2withid::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2WithID::RemoveStructuralFeatureValueAction.__init__)


def test_uml2withid::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ProtocolTransition)


def test_uml2withid::protocoltransition_constructor_exists():
    assert callable(UML2WithID::ProtocolTransition.__init__)


def test_uml2withid::protocoltransition_constructor_args():
    sig = inspect.signature(UML2WithID::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Collaboration)


def test_uml2withid::collaboration_constructor_exists():
    assert callable(UML2WithID::Collaboration.__init__)


def test_uml2withid::collaboration_constructor_args():
    sig = inspect.signature(UML2WithID::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ValuePin)


def test_uml2withid::valuepin_constructor_exists():
    assert callable(UML2WithID::ValuePin.__init__)


def test_uml2withid::valuepin_constructor_args():
    sig = inspect.signature(UML2WithID::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::calltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CallTrigger)


def test_uml2withid::calltrigger_constructor_exists():
    assert callable(UML2WithID::CallTrigger.__init__)


def test_uml2withid::calltrigger_constructor_args():
    sig = inspect.signature(UML2WithID::CallTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::state_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::State)


def test_uml2withid::state_constructor_exists():
    assert callable(UML2WithID::State.__init__)


def test_uml2withid::state_constructor_args():
    sig = inspect.signature(UML2WithID::State.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TemplateableClassifier)


def test_uml2withid::templateableclassifier_constructor_exists():
    assert callable(UML2WithID::TemplateableClassifier.__init__)


def test_uml2withid::templateableclassifier_constructor_args():
    sig = inspect.signature(UML2WithID::TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LiteralSpecification)


def test_uml2withid::literalspecification_constructor_exists():
    assert callable(UML2WithID::LiteralSpecification.__init__)


def test_uml2withid::literalspecification_constructor_args():
    sig = inspect.signature(UML2WithID::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::objectflow_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ObjectFlow)


def test_uml2withid::objectflow_constructor_exists():
    assert callable(UML2WithID::ObjectFlow.__init__)


def test_uml2withid::objectflow_constructor_args():
    sig = inspect.signature(UML2WithID::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::component_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Component)


def test_uml2withid::component_constructor_exists():
    assert callable(UML2WithID::Component.__init__)


def test_uml2withid::component_constructor_args():
    sig = inspect.signature(UML2WithID::Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::RedefinableElement)


def test_uml2withid::redefinableelement_constructor_exists():
    assert callable(UML2WithID::RedefinableElement.__init__)


def test_uml2withid::redefinableelement_constructor_args():
    sig = inspect.signature(UML2WithID::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::OutputPin)


def test_uml2withid::outputpin_constructor_exists():
    assert callable(UML2WithID::OutputPin.__init__)


def test_uml2withid::outputpin_constructor_args():
    sig = inspect.signature(UML2WithID::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::controlflow_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ControlFlow)


def test_uml2withid::controlflow_constructor_exists():
    assert callable(UML2WithID::ControlFlow.__init__)


def test_uml2withid::controlflow_constructor_args():
    sig = inspect.signature(UML2WithID::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::dependency_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Dependency)


def test_uml2withid::dependency_constructor_exists():
    assert callable(UML2WithID::Dependency.__init__)


def test_uml2withid::dependency_constructor_args():
    sig = inspect.signature(UML2WithID::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CreateLinkObjectAction)


def test_uml2withid::createlinkobjectaction_constructor_exists():
    assert callable(UML2WithID::CreateLinkObjectAction.__init__)


def test_uml2withid::createlinkobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CallBehaviorAction)


def test_uml2withid::callbehavioraction_constructor_exists():
    assert callable(UML2WithID::CallBehaviorAction.__init__)


def test_uml2withid::callbehavioraction_constructor_args():
    sig = inspect.signature(UML2WithID::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::PrimitiveType)


def test_uml2withid::primitivetype_constructor_exists():
    assert callable(UML2WithID::PrimitiveType.__init__)


def test_uml2withid::primitivetype_constructor_args():
    sig = inspect.signature(UML2WithID::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadStructuralFeatureAction)


def test_uml2withid::readstructuralfeatureaction_constructor_exists():
    assert callable(UML2WithID::ReadStructuralFeatureAction.__init__)


def test_uml2withid::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::EnumerationLiteral)


def test_uml2withid::enumerationliteral_constructor_exists():
    assert callable(UML2WithID::EnumerationLiteral.__init__)


def test_uml2withid::enumerationliteral_constructor_args():
    sig = inspect.signature(UML2WithID::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::TestIdentityAction)


def test_uml2withid::testidentityaction_constructor_exists():
    assert callable(UML2WithID::TestIdentityAction.__init__)


def test_uml2withid::testidentityaction_constructor_args():
    sig = inspect.signature(UML2WithID::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readextentaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadExtentAction)


def test_uml2withid::readextentaction_constructor_exists():
    assert callable(UML2WithID::ReadExtentAction.__init__)


def test_uml2withid::readextentaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StructuralFeatureAction)


def test_uml2withid::structuralfeatureaction_constructor_exists():
    assert callable(UML2WithID::StructuralFeatureAction.__init__)


def test_uml2withid::structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::applyfunctionaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ApplyFunctionAction)


def test_uml2withid::applyfunctionaction_constructor_exists():
    assert callable(UML2WithID::ApplyFunctionAction.__init__)


def test_uml2withid::applyfunctionaction_constructor_args():
    sig = inspect.signature(UML2WithID::ApplyFunctionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::RaiseExceptionAction)


def test_uml2withid::raiseexceptionaction_constructor_exists():
    assert callable(UML2WithID::RaiseExceptionAction.__init__)


def test_uml2withid::raiseexceptionaction_constructor_args():
    sig = inspect.signature(UML2WithID::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadIsClassifiedObjectAction)


def test_uml2withid::readisclassifiedobjectaction_constructor_exists():
    assert callable(UML2WithID::ReadIsClassifiedObjectAction.__init__)


def test_uml2withid::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::variableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::VariableAction)


def test_uml2withid::variableaction_constructor_exists():
    assert callable(UML2WithID::VariableAction.__init__)


def test_uml2withid::variableaction_constructor_args():
    sig = inspect.signature(UML2WithID::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::startownedbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StartOwnedBehaviorAction)


def test_uml2withid::startownedbehavioraction_constructor_exists():
    assert callable(UML2WithID::StartOwnedBehaviorAction.__init__)


def test_uml2withid::startownedbehavioraction_constructor_args():
    sig = inspect.signature(UML2WithID::StartOwnedBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReclassifyObjectAction)


def test_uml2withid::reclassifyobjectaction_constructor_exists():
    assert callable(UML2WithID::ReclassifyObjectAction.__init__)


def test_uml2withid::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::StructuredActivityNode)


def test_uml2withid::structuredactivitynode_constructor_exists():
    assert callable(UML2WithID::StructuredActivityNode.__init__)


def test_uml2withid::structuredactivitynode_constructor_args():
    sig = inspect.signature(UML2WithID::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AcceptEventAction)


def test_uml2withid::accepteventaction_constructor_exists():
    assert callable(UML2WithID::AcceptEventAction.__init__)


def test_uml2withid::accepteventaction_constructor_args():
    sig = inspect.signature(UML2WithID::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::linkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::LinkAction)


def test_uml2withid::linkaction_constructor_exists():
    assert callable(UML2WithID::LinkAction.__init__)


def test_uml2withid::linkaction_constructor_args():
    sig = inspect.signature(UML2WithID::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::replyaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReplyAction)


def test_uml2withid::replyaction_constructor_exists():
    assert callable(UML2WithID::ReplyAction.__init__)


def test_uml2withid::replyaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadLinkObjectEndAction)


def test_uml2withid::readlinkobjectendaction_constructor_exists():
    assert callable(UML2WithID::ReadLinkObjectEndAction.__init__)


def test_uml2withid::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readselfaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadSelfAction)


def test_uml2withid::readselfaction_constructor_exists():
    assert callable(UML2WithID::ReadSelfAction.__init__)


def test_uml2withid::readselfaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::invocationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InvocationAction)


def test_uml2withid::invocationaction_constructor_exists():
    assert callable(UML2WithID::InvocationAction.__init__)


def test_uml2withid::invocationaction_constructor_args():
    sig = inspect.signature(UML2WithID::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ClearAssociationAction)


def test_uml2withid::clearassociationaction_constructor_exists():
    assert callable(UML2WithID::ClearAssociationAction.__init__)


def test_uml2withid::clearassociationaction_constructor_args():
    sig = inspect.signature(UML2WithID::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadLinkObjectEndQualifierAction)


def test_uml2withid::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UML2WithID::ReadLinkObjectEndQualifierAction.__init__)


def test_uml2withid::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::IntervalConstraint)


def test_uml2withid::intervalconstraint_constructor_exists():
    assert callable(UML2WithID::IntervalConstraint.__init__)


def test_uml2withid::intervalconstraint_constructor_args():
    sig = inspect.signature(UML2WithID::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::InteractionConstraint)


def test_uml2withid::interactionconstraint_constructor_exists():
    assert callable(UML2WithID::InteractionConstraint.__init__)


def test_uml2withid::interactionconstraint_constructor_args():
    sig = inspect.signature(UML2WithID::InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::RemoveVariableValueAction)


def test_uml2withid::removevariablevalueaction_constructor_exists():
    assert callable(UML2WithID::RemoveVariableValueAction.__init__)


def test_uml2withid::removevariablevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AddVariableValueAction)


def test_uml2withid::addvariablevalueaction_constructor_exists():
    assert callable(UML2WithID::AddVariableValueAction.__init__)


def test_uml2withid::addvariablevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DestroyObjectAction)


def test_uml2withid::destroyobjectaction_constructor_exists():
    assert callable(UML2WithID::DestroyObjectAction.__init__)


def test_uml2withid::destroyobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::WriteLinkAction)


def test_uml2withid::writelinkaction_constructor_exists():
    assert callable(UML2WithID::WriteLinkAction.__init__)


def test_uml2withid::writelinkaction_constructor_args():
    sig = inspect.signature(UML2WithID::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ReadLinkAction)


def test_uml2withid::readlinkaction_constructor_exists():
    assert callable(UML2WithID::ReadLinkAction.__init__)


def test_uml2withid::readlinkaction_constructor_args():
    sig = inspect.signature(UML2WithID::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CreateObjectAction)


def test_uml2withid::createobjectaction_constructor_exists():
    assert callable(UML2WithID::CreateObjectAction.__init__)


def test_uml2withid::createobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::DataStoreNode)


def test_uml2withid::datastorenode_constructor_exists():
    assert callable(UML2WithID::DataStoreNode.__init__)


def test_uml2withid::datastorenode_constructor_args():
    sig = inspect.signature(UML2WithID::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::parameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Parameter)


def test_uml2withid::parameter_constructor_exists():
    assert callable(UML2WithID::Parameter.__init__)


def test_uml2withid::parameter_constructor_args():
    sig = inspect.signature(UML2WithID::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::property_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Property)


def test_uml2withid::property_constructor_exists():
    assert callable(UML2WithID::Property.__init__)


def test_uml2withid::property_constructor_args():
    sig = inspect.signature(UML2WithID::Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::variable_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Variable)


def test_uml2withid::variable_constructor_exists():
    assert callable(UML2WithID::Variable.__init__)


def test_uml2withid::variable_constructor_args():
    sig = inspect.signature(UML2WithID::Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExtensionPoint)


def test_uml2withid::extensionpoint_constructor_exists():
    assert callable(UML2WithID::ExtensionPoint.__init__)


def test_uml2withid::extensionpoint_constructor_args():
    sig = inspect.signature(UML2WithID::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "protected",
        "private",
        "package",
        "public",
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
UML2WithID::Element_strategy = st.builds(
    UML2WithID::Element,
    ID=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
Type_strategy = st.builds(
    Type,
)
CallAction_strategy = st.builds(
    CallAction,
)
Dependency_strategy = st.builds(
    Dependency,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
Node_strategy = st.builds(
    Node,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
Package_strategy = st.builds(
    Package,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
MessageTrigger_strategy = st.builds(
    MessageTrigger,
)
Trigger_strategy = st.builds(
    Trigger,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
Artifact_strategy = st.builds(
    Artifact,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
Interval_strategy = st.builds(
    Interval,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
State_strategy = st.builds(
    State,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
Association_strategy = st.builds(
    Association,
)
Feature_strategy = st.builds(
    Feature,
)
Property_strategy = st.builds(
    Property,
)
Vertex_strategy = st.builds(
    Vertex,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
Class_strategy = st.builds(
    Class,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
Pin_strategy = st.builds(
    Pin,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
Classifier_strategy = st.builds(
    Classifier,
)
Behavior_strategy = st.builds(
    Behavior,
)
InputPin_strategy = st.builds(
    InputPin,
)
Realization_strategy = st.builds(
    Realization,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
DataType_strategy = st.builds(
    DataType,
)
InteractionOccurrence_strategy = st.builds(
    InteractionOccurrence,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
Namespace_strategy = st.builds(
    Namespace,
)
Element_strategy = st.builds(
    Element,
)
UML2WithID::AnyTrigger_strategy = st.builds(
    UML2WithID::AnyTrigger,
)
UML2WithID::Duration_strategy = st.builds(
    UML2WithID::Duration,
)
UML2WithID::CollaborationOccurrence_strategy = st.builds(
    UML2WithID::CollaborationOccurrence,
)
UML2WithID::InteractionOperand_strategy = st.builds(
    UML2WithID::InteractionOperand,
)
UML2WithID::Abstraction_strategy = st.builds(
    UML2WithID::Abstraction,
)
UML2WithID::Enumeration_strategy = st.builds(
    UML2WithID::Enumeration,
)
UML2WithID::LiteralUnlimitedNatural_strategy = st.builds(
    UML2WithID::LiteralUnlimitedNatural,
)
UML2WithID::Stop_strategy = st.builds(
    UML2WithID::Stop,
)
UML2WithID::WriteStructuralFeatureAction_strategy = st.builds(
    UML2WithID::WriteStructuralFeatureAction,
)
UML2WithID::ActivityFinalNode_strategy = st.builds(
    UML2WithID::ActivityFinalNode,
)
UML2WithID::ConditionalNode_strategy = st.builds(
    UML2WithID::ConditionalNode,
)
UML2WithID::ProtocolStateMachine_strategy = st.builds(
    UML2WithID::ProtocolStateMachine,
)
UML2WithID::ActivityNode_strategy = st.builds(
    UML2WithID::ActivityNode,
)
UML2WithID::ExecutableNode_strategy = st.builds(
    UML2WithID::ExecutableNode,
)
UML2WithID::Manifestation_strategy = st.builds(
    UML2WithID::Manifestation,
)
UML2WithID::GeneralizationSet_strategy = st.builds(
    UML2WithID::GeneralizationSet,
)
UML2WithID::TypedElement_strategy = st.builds(
    UML2WithID::TypedElement,
)
UML2WithID::DurationInterval_strategy = st.builds(
    UML2WithID::DurationInterval,
)
UML2WithID::CreateLinkAction_strategy = st.builds(
    UML2WithID::CreateLinkAction,
)
UML2WithID::ControlNode_strategy = st.builds(
    UML2WithID::ControlNode,
)
UML2WithID::Class_strategy = st.builds(
    UML2WithID::Class,
)
UML2WithID::DataType_strategy = st.builds(
    UML2WithID::DataType,
)
UML2WithID::ReadVariableAction_strategy = st.builds(
    UML2WithID::ReadVariableAction,
)
UML2WithID::Reception_strategy = st.builds(
    UML2WithID::Reception,
)
UML2WithID::LiteralBoolean_strategy = st.builds(
    UML2WithID::LiteralBoolean,
)
UML2WithID::Expression_strategy = st.builds(
    UML2WithID::Expression,
)
UML2WithID::DurationConstraint_strategy = st.builds(
    UML2WithID::DurationConstraint,
)
UML2WithID::DeploymentSpecification_strategy = st.builds(
    UML2WithID::DeploymentSpecification,
)
UML2WithID::LiteralNull_strategy = st.builds(
    UML2WithID::LiteralNull,
)
UML2WithID::RedefinableTemplateSignature_strategy = st.builds(
    UML2WithID::RedefinableTemplateSignature,
)
UML2WithID::ActivityPartition_strategy = st.builds(
    UML2WithID::ActivityPartition,
)
UML2WithID::BroadcastSignalAction_strategy = st.builds(
    UML2WithID::BroadcastSignalAction,
)
UML2WithID::TimeExpression_strategy = st.builds(
    UML2WithID::TimeExpression,
)
UML2WithID::ForkNode_strategy = st.builds(
    UML2WithID::ForkNode,
)
UML2WithID::ExtensionEnd_strategy = st.builds(
    UML2WithID::ExtensionEnd,
)
UML2WithID::CallOperationAction_strategy = st.builds(
    UML2WithID::CallOperationAction,
)
UML2WithID::WriteVariableAction_strategy = st.builds(
    UML2WithID::WriteVariableAction,
)
UML2WithID::MessageTrigger_strategy = st.builds(
    UML2WithID::MessageTrigger,
)
UML2WithID::ActivityEdge_strategy = st.builds(
    UML2WithID::ActivityEdge,
)
UML2WithID::UseCase_strategy = st.builds(
    UML2WithID::UseCase,
)
UML2WithID::EventOccurrence_strategy = st.builds(
    UML2WithID::EventOccurrence,
)
UML2WithID::StructuralFeature_strategy = st.builds(
    UML2WithID::StructuralFeature,
)
UML2WithID::ObjectNode_strategy = st.builds(
    UML2WithID::ObjectNode,
)
UML2WithID::AssociationClass_strategy = st.builds(
    UML2WithID::AssociationClass,
)
UML2WithID::InputPin_strategy = st.builds(
    UML2WithID::InputPin,
)
UML2WithID::CallAction_strategy = st.builds(
    UML2WithID::CallAction,
)
UML2WithID::Association_strategy = st.builds(
    UML2WithID::Association,
)
UML2WithID::SignalTrigger_strategy = st.builds(
    UML2WithID::SignalTrigger,
)
UML2WithID::Interaction_strategy = st.builds(
    UML2WithID::Interaction,
)
UML2WithID::ClearVariableAction_strategy = st.builds(
    UML2WithID::ClearVariableAction,
)
UML2WithID::Continuation_strategy = st.builds(
    UML2WithID::Continuation,
)
UML2WithID::TimeTrigger_strategy = st.builds(
    UML2WithID::TimeTrigger,
)
UML2WithID::CentralBufferNode_strategy = st.builds(
    UML2WithID::CentralBufferNode,
)
UML2WithID::PartDecomposition_strategy = st.builds(
    UML2WithID::PartDecomposition,
)
UML2WithID::Usage_strategy = st.builds(
    UML2WithID::Usage,
)
UML2WithID::Port_strategy = st.builds(
    UML2WithID::Port,
)
UML2WithID::Actor_strategy = st.builds(
    UML2WithID::Actor,
)
UML2WithID::ValueSpecification_strategy = st.builds(
    UML2WithID::ValueSpecification,
)
UML2WithID::Package_strategy = st.builds(
    UML2WithID::Package,
)
UML2WithID::Signal_strategy = st.builds(
    UML2WithID::Signal,
)
UML2WithID::ConnectionPointReference_strategy = st.builds(
    UML2WithID::ConnectionPointReference,
)
UML2WithID::ClearStructuralFeatureAction_strategy = st.builds(
    UML2WithID::ClearStructuralFeatureAction,
)
UML2WithID::Profile_strategy = st.builds(
    UML2WithID::Profile,
)
UML2WithID::BehavioralFeature_strategy = st.builds(
    UML2WithID::BehavioralFeature,
)
UML2WithID::InformationFlow_strategy = st.builds(
    UML2WithID::InformationFlow,
)
UML2WithID::Region_strategy = st.builds(
    UML2WithID::Region,
)
UML2WithID::Include_strategy = st.builds(
    UML2WithID::Include,
)
UML2WithID::Substitution_strategy = st.builds(
    UML2WithID::Substitution,
)
UML2WithID::Vertex_strategy = st.builds(
    UML2WithID::Vertex,
)
UML2WithID::MessageEnd_strategy = st.builds(
    UML2WithID::MessageEnd,
)
UML2WithID::Interface_strategy = st.builds(
    UML2WithID::Interface,
)
UML2WithID::ParameterSet_strategy = st.builds(
    UML2WithID::ParameterSet,
)
UML2WithID::DecisionNode_strategy = st.builds(
    UML2WithID::DecisionNode,
)
UML2WithID::InteractionFragment_strategy = st.builds(
    UML2WithID::InteractionFragment,
)
UML2WithID::StateMachine_strategy = st.builds(
    UML2WithID::StateMachine,
)
UML2WithID::Node_strategy = st.builds(
    UML2WithID::Node,
)
UML2WithID::TimeObservationAction_strategy = st.builds(
    UML2WithID::TimeObservationAction,
)
UML2WithID::SendObjectAction_strategy = st.builds(
    UML2WithID::SendObjectAction,
)
UML2WithID::GeneralOrdering_strategy = st.builds(
    UML2WithID::GeneralOrdering,
)
UML2WithID::ParameterableClassifier_strategy = st.builds(
    UML2WithID::ParameterableClassifier,
)
UML2WithID::Activity_strategy = st.builds(
    UML2WithID::Activity,
)
UML2WithID::FinalNode_strategy = st.builds(
    UML2WithID::FinalNode,
)
UML2WithID::AcceptCallAction_strategy = st.builds(
    UML2WithID::AcceptCallAction,
)
UML2WithID::Realization_strategy = st.builds(
    UML2WithID::Realization,
)
UML2WithID::InitialNode_strategy = st.builds(
    UML2WithID::InitialNode,
)
UML2WithID::Device_strategy = st.builds(
    UML2WithID::Device,
)
UML2WithID::Artifact_strategy = st.builds(
    UML2WithID::Artifact,
)
UML2WithID::NamedElement_strategy = st.builds(
    UML2WithID::NamedElement,
    visibility=
        safe_text
)
UML2WithID::ActivityParameterNode_strategy = st.builds(
    UML2WithID::ActivityParameterNode,
)
UML2WithID::BehavioredClassifier_strategy = st.builds(
    UML2WithID::BehavioredClassifier,
)
UML2WithID::DestroyLinkAction_strategy = st.builds(
    UML2WithID::DestroyLinkAction,
)
UML2WithID::Feature_strategy = st.builds(
    UML2WithID::Feature,
)
UML2WithID::Pin_strategy = st.builds(
    UML2WithID::Pin,
)
UML2WithID::Type_strategy = st.builds(
    UML2WithID::Type,
)
UML2WithID::AddStructuralFeatureValueAction_strategy = st.builds(
    UML2WithID::AddStructuralFeatureValueAction,
)
UML2WithID::CombinedFragment_strategy = st.builds(
    UML2WithID::CombinedFragment,
)
UML2WithID::OpaqueExpression_strategy = st.builds(
    UML2WithID::OpaqueExpression,
)
UML2WithID::Extension_strategy = st.builds(
    UML2WithID::Extension,
)
UML2WithID::MergeNode_strategy = st.builds(
    UML2WithID::MergeNode,
)
UML2WithID::TimeInterval_strategy = st.builds(
    UML2WithID::TimeInterval,
)
UML2WithID::PackageableElement_strategy = st.builds(
    UML2WithID::PackageableElement,
)
UML2WithID::FinalState_strategy = st.builds(
    UML2WithID::FinalState,
)
UML2WithID::Implementation_strategy = st.builds(
    UML2WithID::Implementation,
)
UML2WithID::Behavior_strategy = st.builds(
    UML2WithID::Behavior,
)
UML2WithID::StructuredClassifier_strategy = st.builds(
    UML2WithID::StructuredClassifier,
)
UML2WithID::EncapsulatedClassifier_strategy = st.builds(
    UML2WithID::EncapsulatedClassifier,
)
UML2WithID::InteractionOccurrence_strategy = st.builds(
    UML2WithID::InteractionOccurrence,
)
UML2WithID::Message_strategy = st.builds(
    UML2WithID::Message,
)
UML2WithID::TimeConstraint_strategy = st.builds(
    UML2WithID::TimeConstraint,
)
UML2WithID::Model_strategy = st.builds(
    UML2WithID::Model,
)
UML2WithID::Namespace_strategy = st.builds(
    UML2WithID::Namespace,
)
UML2WithID::Interval_strategy = st.builds(
    UML2WithID::Interval,
)
UML2WithID::ChangeTrigger_strategy = st.builds(
    UML2WithID::ChangeTrigger,
)
UML2WithID::InstanceSpecification_strategy = st.builds(
    UML2WithID::InstanceSpecification,
)
UML2WithID::Operation_strategy = st.builds(
    UML2WithID::Operation,
)
UML2WithID::ExecutionEnvironment_strategy = st.builds(
    UML2WithID::ExecutionEnvironment,
)
UML2WithID::Trigger_strategy = st.builds(
    UML2WithID::Trigger,
)
UML2WithID::StateInvariant_strategy = st.builds(
    UML2WithID::StateInvariant,
)
UML2WithID::LiteralString_strategy = st.builds(
    UML2WithID::LiteralString,
)
UML2WithID::Constraint_strategy = st.builds(
    UML2WithID::Constraint,
)
UML2WithID::DeploymentTarget_strategy = st.builds(
    UML2WithID::DeploymentTarget,
)
UML2WithID::ExecutionOccurrence_strategy = st.builds(
    UML2WithID::ExecutionOccurrence,
)
UML2WithID::Gate_strategy = st.builds(
    UML2WithID::Gate,
)
UML2WithID::Deployment_strategy = st.builds(
    UML2WithID::Deployment,
)
UML2WithID::CommunicationPath_strategy = st.builds(
    UML2WithID::CommunicationPath,
)
UML2WithID::LiteralInteger_strategy = st.builds(
    UML2WithID::LiteralInteger,
)
UML2WithID::FlowFinalNode_strategy = st.builds(
    UML2WithID::FlowFinalNode,
)
UML2WithID::Connector_strategy = st.builds(
    UML2WithID::Connector,
)
UML2WithID::DurationObservationAction_strategy = st.builds(
    UML2WithID::DurationObservationAction,
)
UML2WithID::InformationItem_strategy = st.builds(
    UML2WithID::InformationItem,
)
UML2WithID::Classifier_strategy = st.builds(
    UML2WithID::Classifier,
)
UML2WithID::Pseudostate_strategy = st.builds(
    UML2WithID::Pseudostate,
)
UML2WithID::LoopNode_strategy = st.builds(
    UML2WithID::LoopNode,
)
UML2WithID::Action_strategy = st.builds(
    UML2WithID::Action,
)
UML2WithID::DeployedArtifact_strategy = st.builds(
    UML2WithID::DeployedArtifact,
)
UML2WithID::ExpansionRegion_strategy = st.builds(
    UML2WithID::ExpansionRegion,
)
UML2WithID::Permission_strategy = st.builds(
    UML2WithID::Permission,
)
UML2WithID::InstanceValue_strategy = st.builds(
    UML2WithID::InstanceValue,
)
UML2WithID::JoinNode_strategy = st.builds(
    UML2WithID::JoinNode,
)
UML2WithID::Transition_strategy = st.builds(
    UML2WithID::Transition,
)
UML2WithID::ExpansionNode_strategy = st.builds(
    UML2WithID::ExpansionNode,
)
UML2WithID::Lifeline_strategy = st.builds(
    UML2WithID::Lifeline,
)
UML2WithID::SendSignalAction_strategy = st.builds(
    UML2WithID::SendSignalAction,
)
UML2WithID::PrimitiveFunction_strategy = st.builds(
    UML2WithID::PrimitiveFunction,
)
UML2WithID::Extend_strategy = st.builds(
    UML2WithID::Extend,
)
UML2WithID::ConnectableElement_strategy = st.builds(
    UML2WithID::ConnectableElement,
)
UML2WithID::Stereotype_strategy = st.builds(
    UML2WithID::Stereotype,
)
UML2WithID::RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2WithID::RemoveStructuralFeatureValueAction,
)
UML2WithID::ProtocolTransition_strategy = st.builds(
    UML2WithID::ProtocolTransition,
)
UML2WithID::Collaboration_strategy = st.builds(
    UML2WithID::Collaboration,
)
UML2WithID::ValuePin_strategy = st.builds(
    UML2WithID::ValuePin,
)
UML2WithID::CallTrigger_strategy = st.builds(
    UML2WithID::CallTrigger,
)
UML2WithID::State_strategy = st.builds(
    UML2WithID::State,
)
UML2WithID::TemplateableClassifier_strategy = st.builds(
    UML2WithID::TemplateableClassifier,
)
UML2WithID::LiteralSpecification_strategy = st.builds(
    UML2WithID::LiteralSpecification,
)
UML2WithID::ObjectFlow_strategy = st.builds(
    UML2WithID::ObjectFlow,
)
UML2WithID::Component_strategy = st.builds(
    UML2WithID::Component,
)
UML2WithID::RedefinableElement_strategy = st.builds(
    UML2WithID::RedefinableElement,
)
UML2WithID::OutputPin_strategy = st.builds(
    UML2WithID::OutputPin,
)
UML2WithID::ControlFlow_strategy = st.builds(
    UML2WithID::ControlFlow,
)
UML2WithID::Dependency_strategy = st.builds(
    UML2WithID::Dependency,
)
UML2WithID::CreateLinkObjectAction_strategy = st.builds(
    UML2WithID::CreateLinkObjectAction,
)
UML2WithID::CallBehaviorAction_strategy = st.builds(
    UML2WithID::CallBehaviorAction,
)
UML2WithID::PrimitiveType_strategy = st.builds(
    UML2WithID::PrimitiveType,
)
UML2WithID::ReadStructuralFeatureAction_strategy = st.builds(
    UML2WithID::ReadStructuralFeatureAction,
)
UML2WithID::EnumerationLiteral_strategy = st.builds(
    UML2WithID::EnumerationLiteral,
)
Action_strategy = st.builds(
    Action,
)
UML2WithID::TestIdentityAction_strategy = st.builds(
    UML2WithID::TestIdentityAction,
)
UML2WithID::ReadExtentAction_strategy = st.builds(
    UML2WithID::ReadExtentAction,
)
UML2WithID::StructuralFeatureAction_strategy = st.builds(
    UML2WithID::StructuralFeatureAction,
)
UML2WithID::ApplyFunctionAction_strategy = st.builds(
    UML2WithID::ApplyFunctionAction,
)
UML2WithID::RaiseExceptionAction_strategy = st.builds(
    UML2WithID::RaiseExceptionAction,
)
UML2WithID::ReadIsClassifiedObjectAction_strategy = st.builds(
    UML2WithID::ReadIsClassifiedObjectAction,
)
UML2WithID::VariableAction_strategy = st.builds(
    UML2WithID::VariableAction,
)
UML2WithID::StartOwnedBehaviorAction_strategy = st.builds(
    UML2WithID::StartOwnedBehaviorAction,
)
UML2WithID::ReclassifyObjectAction_strategy = st.builds(
    UML2WithID::ReclassifyObjectAction,
)
UML2WithID::StructuredActivityNode_strategy = st.builds(
    UML2WithID::StructuredActivityNode,
)
UML2WithID::AcceptEventAction_strategy = st.builds(
    UML2WithID::AcceptEventAction,
)
UML2WithID::LinkAction_strategy = st.builds(
    UML2WithID::LinkAction,
)
UML2WithID::ReplyAction_strategy = st.builds(
    UML2WithID::ReplyAction,
)
UML2WithID::ReadLinkObjectEndAction_strategy = st.builds(
    UML2WithID::ReadLinkObjectEndAction,
)
UML2WithID::ReadSelfAction_strategy = st.builds(
    UML2WithID::ReadSelfAction,
)
UML2WithID::InvocationAction_strategy = st.builds(
    UML2WithID::InvocationAction,
)
UML2WithID::ClearAssociationAction_strategy = st.builds(
    UML2WithID::ClearAssociationAction,
)
UML2WithID::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UML2WithID::ReadLinkObjectEndQualifierAction,
)
Constraint_strategy = st.builds(
    Constraint,
)
UML2WithID::IntervalConstraint_strategy = st.builds(
    UML2WithID::IntervalConstraint,
)
UML2WithID::InteractionConstraint_strategy = st.builds(
    UML2WithID::InteractionConstraint,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UML2WithID::RemoveVariableValueAction_strategy = st.builds(
    UML2WithID::RemoveVariableValueAction,
)
UML2WithID::AddVariableValueAction_strategy = st.builds(
    UML2WithID::AddVariableValueAction,
)
UML2WithID::DestroyObjectAction_strategy = st.builds(
    UML2WithID::DestroyObjectAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UML2WithID::WriteLinkAction_strategy = st.builds(
    UML2WithID::WriteLinkAction,
)
UML2WithID::ReadLinkAction_strategy = st.builds(
    UML2WithID::ReadLinkAction,
)
UML2WithID::CreateObjectAction_strategy = st.builds(
    UML2WithID::CreateObjectAction,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UML2WithID::DataStoreNode_strategy = st.builds(
    UML2WithID::DataStoreNode,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
UML2WithID::Parameter_strategy = st.builds(
    UML2WithID::Parameter,
)
UML2WithID::Property_strategy = st.builds(
    UML2WithID::Property,
)
UML2WithID::Variable_strategy = st.builds(
    UML2WithID::Variable,
)
UML2WithID::ExtensionPoint_strategy = st.builds(
    UML2WithID::ExtensionPoint,
)

@given(instance=UML2WithID::Element_strategy)
@settings(max_examples=50)
def test_uml2withid::element_instantiation(instance):
    assert isinstance(instance, UML2WithID::Element)

@given(instance=UML2WithID::Element_strategy)
def test_uml2withid::element_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=UML2WithID::Element_strategy)
def test_uml2withid::element_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=MessageTrigger_strategy)
@settings(max_examples=50)
def test_messagetrigger_instantiation(instance):
    assert isinstance(instance, MessageTrigger)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_interactionoccurrence_instantiation(instance):
    assert isinstance(instance, InteractionOccurrence)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID::AnyTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid::anytrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID::AnyTrigger)

@given(instance=UML2WithID::Duration_strategy)
@settings(max_examples=50)
def test_uml2withid::duration_instantiation(instance):
    assert isinstance(instance, UML2WithID::Duration)

@given(instance=UML2WithID::CollaborationOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid::collaborationoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID::CollaborationOccurrence)

@given(instance=UML2WithID::InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml2withid::interactionoperand_instantiation(instance):
    assert isinstance(instance, UML2WithID::InteractionOperand)

@given(instance=UML2WithID::Abstraction_strategy)
@settings(max_examples=50)
def test_uml2withid::abstraction_instantiation(instance):
    assert isinstance(instance, UML2WithID::Abstraction)

@given(instance=UML2WithID::Enumeration_strategy)
@settings(max_examples=50)
def test_uml2withid::enumeration_instantiation(instance):
    assert isinstance(instance, UML2WithID::Enumeration)

@given(instance=UML2WithID::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2withid::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2WithID::LiteralUnlimitedNatural)

@given(instance=UML2WithID::Stop_strategy)
@settings(max_examples=50)
def test_uml2withid::stop_instantiation(instance):
    assert isinstance(instance, UML2WithID::Stop)

@given(instance=UML2WithID::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::WriteStructuralFeatureAction)

@given(instance=UML2WithID::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml2withid::activityfinalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ActivityFinalNode)

@given(instance=UML2WithID::ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml2withid::conditionalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ConditionalNode)

@given(instance=UML2WithID::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID::ProtocolStateMachine)

@given(instance=UML2WithID::ActivityNode_strategy)
@settings(max_examples=50)
def test_uml2withid::activitynode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ActivityNode)

@given(instance=UML2WithID::ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml2withid::executablenode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExecutableNode)

@given(instance=UML2WithID::Manifestation_strategy)
@settings(max_examples=50)
def test_uml2withid::manifestation_instantiation(instance):
    assert isinstance(instance, UML2WithID::Manifestation)

@given(instance=UML2WithID::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml2withid::generalizationset_instantiation(instance):
    assert isinstance(instance, UML2WithID::GeneralizationSet)

@given(instance=UML2WithID::TypedElement_strategy)
@settings(max_examples=50)
def test_uml2withid::typedelement_instantiation(instance):
    assert isinstance(instance, UML2WithID::TypedElement)

@given(instance=UML2WithID::DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2withid::durationinterval_instantiation(instance):
    assert isinstance(instance, UML2WithID::DurationInterval)

@given(instance=UML2WithID::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid::createlinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::CreateLinkAction)

@given(instance=UML2WithID::ControlNode_strategy)
@settings(max_examples=50)
def test_uml2withid::controlnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ControlNode)

@given(instance=UML2WithID::Class_strategy)
@settings(max_examples=50)
def test_uml2withid::class_instantiation(instance):
    assert isinstance(instance, UML2WithID::Class)

@given(instance=UML2WithID::DataType_strategy)
@settings(max_examples=50)
def test_uml2withid::datatype_instantiation(instance):
    assert isinstance(instance, UML2WithID::DataType)

@given(instance=UML2WithID::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readvariableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadVariableAction)

@given(instance=UML2WithID::Reception_strategy)
@settings(max_examples=50)
def test_uml2withid::reception_instantiation(instance):
    assert isinstance(instance, UML2WithID::Reception)

@given(instance=UML2WithID::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2withid::literalboolean_instantiation(instance):
    assert isinstance(instance, UML2WithID::LiteralBoolean)

@given(instance=UML2WithID::Expression_strategy)
@settings(max_examples=50)
def test_uml2withid::expression_instantiation(instance):
    assert isinstance(instance, UML2WithID::Expression)

@given(instance=UML2WithID::DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid::durationconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID::DurationConstraint)

@given(instance=UML2WithID::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2WithID::DeploymentSpecification)

@given(instance=UML2WithID::LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2withid::literalnull_instantiation(instance):
    assert isinstance(instance, UML2WithID::LiteralNull)

@given(instance=UML2WithID::RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2withid::redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, UML2WithID::RedefinableTemplateSignature)

@given(instance=UML2WithID::ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml2withid::activitypartition_instantiation(instance):
    assert isinstance(instance, UML2WithID::ActivityPartition)

@given(instance=UML2WithID::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml2withid::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::BroadcastSignalAction)

@given(instance=UML2WithID::TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2withid::timeexpression_instantiation(instance):
    assert isinstance(instance, UML2WithID::TimeExpression)

@given(instance=UML2WithID::ForkNode_strategy)
@settings(max_examples=50)
def test_uml2withid::forknode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ForkNode)

@given(instance=UML2WithID::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2withid::extensionend_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExtensionEnd)

@given(instance=UML2WithID::CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml2withid::calloperationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::CallOperationAction)

@given(instance=UML2WithID::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid::writevariableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::WriteVariableAction)

@given(instance=UML2WithID::MessageTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid::messagetrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID::MessageTrigger)

@given(instance=UML2WithID::ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml2withid::activityedge_instantiation(instance):
    assert isinstance(instance, UML2WithID::ActivityEdge)

@given(instance=UML2WithID::UseCase_strategy)
@settings(max_examples=50)
def test_uml2withid::usecase_instantiation(instance):
    assert isinstance(instance, UML2WithID::UseCase)

@given(instance=UML2WithID::EventOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid::eventoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID::EventOccurrence)

@given(instance=UML2WithID::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2withid::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2WithID::StructuralFeature)

@given(instance=UML2WithID::ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2withid::objectnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ObjectNode)

@given(instance=UML2WithID::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2withid::associationclass_instantiation(instance):
    assert isinstance(instance, UML2WithID::AssociationClass)

@given(instance=UML2WithID::InputPin_strategy)
@settings(max_examples=50)
def test_uml2withid::inputpin_instantiation(instance):
    assert isinstance(instance, UML2WithID::InputPin)

@given(instance=UML2WithID::CallAction_strategy)
@settings(max_examples=50)
def test_uml2withid::callaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::CallAction)

@given(instance=UML2WithID::Association_strategy)
@settings(max_examples=50)
def test_uml2withid::association_instantiation(instance):
    assert isinstance(instance, UML2WithID::Association)

@given(instance=UML2WithID::SignalTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid::signaltrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID::SignalTrigger)

@given(instance=UML2WithID::Interaction_strategy)
@settings(max_examples=50)
def test_uml2withid::interaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::Interaction)

@given(instance=UML2WithID::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid::clearvariableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ClearVariableAction)

@given(instance=UML2WithID::Continuation_strategy)
@settings(max_examples=50)
def test_uml2withid::continuation_instantiation(instance):
    assert isinstance(instance, UML2WithID::Continuation)

@given(instance=UML2WithID::TimeTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid::timetrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID::TimeTrigger)

@given(instance=UML2WithID::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2withid::centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2WithID::CentralBufferNode)

@given(instance=UML2WithID::PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml2withid::partdecomposition_instantiation(instance):
    assert isinstance(instance, UML2WithID::PartDecomposition)

@given(instance=UML2WithID::Usage_strategy)
@settings(max_examples=50)
def test_uml2withid::usage_instantiation(instance):
    assert isinstance(instance, UML2WithID::Usage)

@given(instance=UML2WithID::Port_strategy)
@settings(max_examples=50)
def test_uml2withid::port_instantiation(instance):
    assert isinstance(instance, UML2WithID::Port)

@given(instance=UML2WithID::Actor_strategy)
@settings(max_examples=50)
def test_uml2withid::actor_instantiation(instance):
    assert isinstance(instance, UML2WithID::Actor)

@given(instance=UML2WithID::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid::valuespecification_instantiation(instance):
    assert isinstance(instance, UML2WithID::ValueSpecification)

@given(instance=UML2WithID::Package_strategy)
@settings(max_examples=50)
def test_uml2withid::package_instantiation(instance):
    assert isinstance(instance, UML2WithID::Package)

@given(instance=UML2WithID::Signal_strategy)
@settings(max_examples=50)
def test_uml2withid::signal_instantiation(instance):
    assert isinstance(instance, UML2WithID::Signal)

@given(instance=UML2WithID::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml2withid::connectionpointreference_instantiation(instance):
    assert isinstance(instance, UML2WithID::ConnectionPointReference)

@given(instance=UML2WithID::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ClearStructuralFeatureAction)

@given(instance=UML2WithID::Profile_strategy)
@settings(max_examples=50)
def test_uml2withid::profile_instantiation(instance):
    assert isinstance(instance, UML2WithID::Profile)

@given(instance=UML2WithID::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2withid::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2WithID::BehavioralFeature)

@given(instance=UML2WithID::InformationFlow_strategy)
@settings(max_examples=50)
def test_uml2withid::informationflow_instantiation(instance):
    assert isinstance(instance, UML2WithID::InformationFlow)

@given(instance=UML2WithID::Region_strategy)
@settings(max_examples=50)
def test_uml2withid::region_instantiation(instance):
    assert isinstance(instance, UML2WithID::Region)

@given(instance=UML2WithID::Include_strategy)
@settings(max_examples=50)
def test_uml2withid::include_instantiation(instance):
    assert isinstance(instance, UML2WithID::Include)

@given(instance=UML2WithID::Substitution_strategy)
@settings(max_examples=50)
def test_uml2withid::substitution_instantiation(instance):
    assert isinstance(instance, UML2WithID::Substitution)

@given(instance=UML2WithID::Vertex_strategy)
@settings(max_examples=50)
def test_uml2withid::vertex_instantiation(instance):
    assert isinstance(instance, UML2WithID::Vertex)

@given(instance=UML2WithID::MessageEnd_strategy)
@settings(max_examples=50)
def test_uml2withid::messageend_instantiation(instance):
    assert isinstance(instance, UML2WithID::MessageEnd)

@given(instance=UML2WithID::Interface_strategy)
@settings(max_examples=50)
def test_uml2withid::interface_instantiation(instance):
    assert isinstance(instance, UML2WithID::Interface)

@given(instance=UML2WithID::ParameterSet_strategy)
@settings(max_examples=50)
def test_uml2withid::parameterset_instantiation(instance):
    assert isinstance(instance, UML2WithID::ParameterSet)

@given(instance=UML2WithID::DecisionNode_strategy)
@settings(max_examples=50)
def test_uml2withid::decisionnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::DecisionNode)

@given(instance=UML2WithID::InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml2withid::interactionfragment_instantiation(instance):
    assert isinstance(instance, UML2WithID::InteractionFragment)

@given(instance=UML2WithID::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid::statemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID::StateMachine)

@given(instance=UML2WithID::Node_strategy)
@settings(max_examples=50)
def test_uml2withid::node_instantiation(instance):
    assert isinstance(instance, UML2WithID::Node)

@given(instance=UML2WithID::TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2withid::timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::TimeObservationAction)

@given(instance=UML2WithID::SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid::sendobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::SendObjectAction)

@given(instance=UML2WithID::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml2withid::generalordering_instantiation(instance):
    assert isinstance(instance, UML2WithID::GeneralOrdering)

@given(instance=UML2WithID::ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::ParameterableClassifier)

@given(instance=UML2WithID::Activity_strategy)
@settings(max_examples=50)
def test_uml2withid::activity_instantiation(instance):
    assert isinstance(instance, UML2WithID::Activity)

@given(instance=UML2WithID::FinalNode_strategy)
@settings(max_examples=50)
def test_uml2withid::finalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::FinalNode)

@given(instance=UML2WithID::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml2withid::acceptcallaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::AcceptCallAction)

@given(instance=UML2WithID::Realization_strategy)
@settings(max_examples=50)
def test_uml2withid::realization_instantiation(instance):
    assert isinstance(instance, UML2WithID::Realization)

@given(instance=UML2WithID::InitialNode_strategy)
@settings(max_examples=50)
def test_uml2withid::initialnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::InitialNode)

@given(instance=UML2WithID::Device_strategy)
@settings(max_examples=50)
def test_uml2withid::device_instantiation(instance):
    assert isinstance(instance, UML2WithID::Device)

@given(instance=UML2WithID::Artifact_strategy)
@settings(max_examples=50)
def test_uml2withid::artifact_instantiation(instance):
    assert isinstance(instance, UML2WithID::Artifact)

@given(instance=UML2WithID::NamedElement_strategy)
@settings(max_examples=50)
def test_uml2withid::namedelement_instantiation(instance):
    assert isinstance(instance, UML2WithID::NamedElement)

@given(instance=UML2WithID::NamedElement_strategy)
def test_uml2withid::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UML2WithID::NamedElement_strategy)
def test_uml2withid::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=UML2WithID::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2withid::activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ActivityParameterNode)

@given(instance=UML2WithID::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::BehavioredClassifier)

@given(instance=UML2WithID::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid::destroylinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::DestroyLinkAction)

@given(instance=UML2WithID::Feature_strategy)
@settings(max_examples=50)
def test_uml2withid::feature_instantiation(instance):
    assert isinstance(instance, UML2WithID::Feature)

@given(instance=UML2WithID::Pin_strategy)
@settings(max_examples=50)
def test_uml2withid::pin_instantiation(instance):
    assert isinstance(instance, UML2WithID::Pin)

@given(instance=UML2WithID::Type_strategy)
@settings(max_examples=50)
def test_uml2withid::type_instantiation(instance):
    assert isinstance(instance, UML2WithID::Type)

@given(instance=UML2WithID::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::AddStructuralFeatureValueAction)

@given(instance=UML2WithID::CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml2withid::combinedfragment_instantiation(instance):
    assert isinstance(instance, UML2WithID::CombinedFragment)

@given(instance=UML2WithID::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2withid::opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2WithID::OpaqueExpression)

@given(instance=UML2WithID::Extension_strategy)
@settings(max_examples=50)
def test_uml2withid::extension_instantiation(instance):
    assert isinstance(instance, UML2WithID::Extension)

@given(instance=UML2WithID::MergeNode_strategy)
@settings(max_examples=50)
def test_uml2withid::mergenode_instantiation(instance):
    assert isinstance(instance, UML2WithID::MergeNode)

@given(instance=UML2WithID::TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2withid::timeinterval_instantiation(instance):
    assert isinstance(instance, UML2WithID::TimeInterval)

@given(instance=UML2WithID::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml2withid::packageableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID::PackageableElement)

@given(instance=UML2WithID::FinalState_strategy)
@settings(max_examples=50)
def test_uml2withid::finalstate_instantiation(instance):
    assert isinstance(instance, UML2WithID::FinalState)

@given(instance=UML2WithID::Implementation_strategy)
@settings(max_examples=50)
def test_uml2withid::implementation_instantiation(instance):
    assert isinstance(instance, UML2WithID::Implementation)

@given(instance=UML2WithID::Behavior_strategy)
@settings(max_examples=50)
def test_uml2withid::behavior_instantiation(instance):
    assert isinstance(instance, UML2WithID::Behavior)

@given(instance=UML2WithID::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::StructuredClassifier)

@given(instance=UML2WithID::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::EncapsulatedClassifier)

@given(instance=UML2WithID::InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid::interactionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID::InteractionOccurrence)

@given(instance=UML2WithID::Message_strategy)
@settings(max_examples=50)
def test_uml2withid::message_instantiation(instance):
    assert isinstance(instance, UML2WithID::Message)

@given(instance=UML2WithID::TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid::timeconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID::TimeConstraint)

@given(instance=UML2WithID::Model_strategy)
@settings(max_examples=50)
def test_uml2withid::model_instantiation(instance):
    assert isinstance(instance, UML2WithID::Model)

@given(instance=UML2WithID::Namespace_strategy)
@settings(max_examples=50)
def test_uml2withid::namespace_instantiation(instance):
    assert isinstance(instance, UML2WithID::Namespace)

@given(instance=UML2WithID::Interval_strategy)
@settings(max_examples=50)
def test_uml2withid::interval_instantiation(instance):
    assert isinstance(instance, UML2WithID::Interval)

@given(instance=UML2WithID::ChangeTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid::changetrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID::ChangeTrigger)

@given(instance=UML2WithID::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid::instancespecification_instantiation(instance):
    assert isinstance(instance, UML2WithID::InstanceSpecification)

@given(instance=UML2WithID::Operation_strategy)
@settings(max_examples=50)
def test_uml2withid::operation_instantiation(instance):
    assert isinstance(instance, UML2WithID::Operation)

@given(instance=UML2WithID::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2withid::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExecutionEnvironment)

@given(instance=UML2WithID::Trigger_strategy)
@settings(max_examples=50)
def test_uml2withid::trigger_instantiation(instance):
    assert isinstance(instance, UML2WithID::Trigger)

@given(instance=UML2WithID::StateInvariant_strategy)
@settings(max_examples=50)
def test_uml2withid::stateinvariant_instantiation(instance):
    assert isinstance(instance, UML2WithID::StateInvariant)

@given(instance=UML2WithID::LiteralString_strategy)
@settings(max_examples=50)
def test_uml2withid::literalstring_instantiation(instance):
    assert isinstance(instance, UML2WithID::LiteralString)

@given(instance=UML2WithID::Constraint_strategy)
@settings(max_examples=50)
def test_uml2withid::constraint_instantiation(instance):
    assert isinstance(instance, UML2WithID::Constraint)

@given(instance=UML2WithID::DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml2withid::deploymenttarget_instantiation(instance):
    assert isinstance(instance, UML2WithID::DeploymentTarget)

@given(instance=UML2WithID::ExecutionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid::executionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExecutionOccurrence)

@given(instance=UML2WithID::Gate_strategy)
@settings(max_examples=50)
def test_uml2withid::gate_instantiation(instance):
    assert isinstance(instance, UML2WithID::Gate)

@given(instance=UML2WithID::Deployment_strategy)
@settings(max_examples=50)
def test_uml2withid::deployment_instantiation(instance):
    assert isinstance(instance, UML2WithID::Deployment)

@given(instance=UML2WithID::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2withid::communicationpath_instantiation(instance):
    assert isinstance(instance, UML2WithID::CommunicationPath)

@given(instance=UML2WithID::LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2withid::literalinteger_instantiation(instance):
    assert isinstance(instance, UML2WithID::LiteralInteger)

@given(instance=UML2WithID::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml2withid::flowfinalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::FlowFinalNode)

@given(instance=UML2WithID::Connector_strategy)
@settings(max_examples=50)
def test_uml2withid::connector_instantiation(instance):
    assert isinstance(instance, UML2WithID::Connector)

@given(instance=UML2WithID::DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2withid::durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::DurationObservationAction)

@given(instance=UML2WithID::InformationItem_strategy)
@settings(max_examples=50)
def test_uml2withid::informationitem_instantiation(instance):
    assert isinstance(instance, UML2WithID::InformationItem)

@given(instance=UML2WithID::Classifier_strategy)
@settings(max_examples=50)
def test_uml2withid::classifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::Classifier)

@given(instance=UML2WithID::Pseudostate_strategy)
@settings(max_examples=50)
def test_uml2withid::pseudostate_instantiation(instance):
    assert isinstance(instance, UML2WithID::Pseudostate)

@given(instance=UML2WithID::LoopNode_strategy)
@settings(max_examples=50)
def test_uml2withid::loopnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::LoopNode)

@given(instance=UML2WithID::Action_strategy)
@settings(max_examples=50)
def test_uml2withid::action_instantiation(instance):
    assert isinstance(instance, UML2WithID::Action)

@given(instance=UML2WithID::DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml2withid::deployedartifact_instantiation(instance):
    assert isinstance(instance, UML2WithID::DeployedArtifact)

@given(instance=UML2WithID::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml2withid::expansionregion_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExpansionRegion)

@given(instance=UML2WithID::Permission_strategy)
@settings(max_examples=50)
def test_uml2withid::permission_instantiation(instance):
    assert isinstance(instance, UML2WithID::Permission)

@given(instance=UML2WithID::InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2withid::instancevalue_instantiation(instance):
    assert isinstance(instance, UML2WithID::InstanceValue)

@given(instance=UML2WithID::JoinNode_strategy)
@settings(max_examples=50)
def test_uml2withid::joinnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::JoinNode)

@given(instance=UML2WithID::Transition_strategy)
@settings(max_examples=50)
def test_uml2withid::transition_instantiation(instance):
    assert isinstance(instance, UML2WithID::Transition)

@given(instance=UML2WithID::ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2withid::expansionnode_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExpansionNode)

@given(instance=UML2WithID::Lifeline_strategy)
@settings(max_examples=50)
def test_uml2withid::lifeline_instantiation(instance):
    assert isinstance(instance, UML2WithID::Lifeline)

@given(instance=UML2WithID::SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml2withid::sendsignalaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::SendSignalAction)

@given(instance=UML2WithID::PrimitiveFunction_strategy)
@settings(max_examples=50)
def test_uml2withid::primitivefunction_instantiation(instance):
    assert isinstance(instance, UML2WithID::PrimitiveFunction)

@given(instance=UML2WithID::Extend_strategy)
@settings(max_examples=50)
def test_uml2withid::extend_instantiation(instance):
    assert isinstance(instance, UML2WithID::Extend)

@given(instance=UML2WithID::ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml2withid::connectableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID::ConnectableElement)

@given(instance=UML2WithID::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2withid::stereotype_instantiation(instance):
    assert isinstance(instance, UML2WithID::Stereotype)

@given(instance=UML2WithID::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::RemoveStructuralFeatureValueAction)

@given(instance=UML2WithID::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml2withid::protocoltransition_instantiation(instance):
    assert isinstance(instance, UML2WithID::ProtocolTransition)

@given(instance=UML2WithID::Collaboration_strategy)
@settings(max_examples=50)
def test_uml2withid::collaboration_instantiation(instance):
    assert isinstance(instance, UML2WithID::Collaboration)

@given(instance=UML2WithID::ValuePin_strategy)
@settings(max_examples=50)
def test_uml2withid::valuepin_instantiation(instance):
    assert isinstance(instance, UML2WithID::ValuePin)

@given(instance=UML2WithID::CallTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid::calltrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID::CallTrigger)

@given(instance=UML2WithID::State_strategy)
@settings(max_examples=50)
def test_uml2withid::state_instantiation(instance):
    assert isinstance(instance, UML2WithID::State)

@given(instance=UML2WithID::TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid::templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID::TemplateableClassifier)

@given(instance=UML2WithID::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid::literalspecification_instantiation(instance):
    assert isinstance(instance, UML2WithID::LiteralSpecification)

@given(instance=UML2WithID::ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml2withid::objectflow_instantiation(instance):
    assert isinstance(instance, UML2WithID::ObjectFlow)

@given(instance=UML2WithID::Component_strategy)
@settings(max_examples=50)
def test_uml2withid::component_instantiation(instance):
    assert isinstance(instance, UML2WithID::Component)

@given(instance=UML2WithID::RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml2withid::redefinableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID::RedefinableElement)

@given(instance=UML2WithID::OutputPin_strategy)
@settings(max_examples=50)
def test_uml2withid::outputpin_instantiation(instance):
    assert isinstance(instance, UML2WithID::OutputPin)

@given(instance=UML2WithID::ControlFlow_strategy)
@settings(max_examples=50)
def test_uml2withid::controlflow_instantiation(instance):
    assert isinstance(instance, UML2WithID::ControlFlow)

@given(instance=UML2WithID::Dependency_strategy)
@settings(max_examples=50)
def test_uml2withid::dependency_instantiation(instance):
    assert isinstance(instance, UML2WithID::Dependency)

@given(instance=UML2WithID::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::CreateLinkObjectAction)

@given(instance=UML2WithID::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2withid::callbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2WithID::CallBehaviorAction)

@given(instance=UML2WithID::PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2withid::primitivetype_instantiation(instance):
    assert isinstance(instance, UML2WithID::PrimitiveType)

@given(instance=UML2WithID::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadStructuralFeatureAction)

@given(instance=UML2WithID::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml2withid::enumerationliteral_instantiation(instance):
    assert isinstance(instance, UML2WithID::EnumerationLiteral)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UML2WithID::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2withid::testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::TestIdentityAction)

@given(instance=UML2WithID::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readextentaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadExtentAction)

@given(instance=UML2WithID::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::StructuralFeatureAction)

@given(instance=UML2WithID::ApplyFunctionAction_strategy)
@settings(max_examples=50)
def test_uml2withid::applyfunctionaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ApplyFunctionAction)

@given(instance=UML2WithID::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml2withid::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::RaiseExceptionAction)

@given(instance=UML2WithID::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadIsClassifiedObjectAction)

@given(instance=UML2WithID::VariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid::variableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::VariableAction)

@given(instance=UML2WithID::StartOwnedBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2withid::startownedbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2WithID::StartOwnedBehaviorAction)

@given(instance=UML2WithID::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReclassifyObjectAction)

@given(instance=UML2WithID::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml2withid::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UML2WithID::StructuredActivityNode)

@given(instance=UML2WithID::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml2withid::accepteventaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::AcceptEventAction)

@given(instance=UML2WithID::LinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid::linkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::LinkAction)

@given(instance=UML2WithID::ReplyAction_strategy)
@settings(max_examples=50)
def test_uml2withid::replyaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReplyAction)

@given(instance=UML2WithID::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadLinkObjectEndAction)

@given(instance=UML2WithID::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readselfaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadSelfAction)

@given(instance=UML2WithID::InvocationAction_strategy)
@settings(max_examples=50)
def test_uml2withid::invocationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::InvocationAction)

@given(instance=UML2WithID::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml2withid::clearassociationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ClearAssociationAction)

@given(instance=UML2WithID::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadLinkObjectEndQualifierAction)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UML2WithID::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid::intervalconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID::IntervalConstraint)

@given(instance=UML2WithID::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid::interactionconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID::InteractionConstraint)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UML2WithID::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::RemoveVariableValueAction)

@given(instance=UML2WithID::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::AddVariableValueAction)

@given(instance=UML2WithID::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::DestroyObjectAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UML2WithID::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid::writelinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::WriteLinkAction)

@given(instance=UML2WithID::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid::readlinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::ReadLinkAction)

@given(instance=UML2WithID::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid::createobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID::CreateObjectAction)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UML2WithID::DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2withid::datastorenode_instantiation(instance):
    assert isinstance(instance, UML2WithID::DataStoreNode)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=UML2WithID::Parameter_strategy)
@settings(max_examples=50)
def test_uml2withid::parameter_instantiation(instance):
    assert isinstance(instance, UML2WithID::Parameter)

@given(instance=UML2WithID::Property_strategy)
@settings(max_examples=50)
def test_uml2withid::property_instantiation(instance):
    assert isinstance(instance, UML2WithID::Property)

@given(instance=UML2WithID::Variable_strategy)
@settings(max_examples=50)
def test_uml2withid::variable_instantiation(instance):
    assert isinstance(instance, UML2WithID::Variable)

@given(instance=UML2WithID::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml2withid::extensionpoint_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExtensionPoint)

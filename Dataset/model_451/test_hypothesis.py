import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CreateLinkAction,
    InvocationAction,
    UML2::CallAction,
    CallAction,
    UML2::CallBehaviorAction,
    UML2::CallOperationAction,
    UML2::SendObjectAction,
    UML2::BroadcastSignalAction,
    VariableAction,
    UML2::ReadVariableAction,
    WriteLinkAction,
    UML2::DestroyLinkAction,
    UML2::CreateLinkAction,
    LinkEndData,
    UML2::LinkEndCreationData,
    WriteVariableAction,
    UML2::RemoveVariableValueAction,
    UML2::AddVariableValueAction,
    UML2::ClearVariableAction,
    UML2::WriteVariableAction,
    StructuralFeatureAction,
    UML2::ClearStructuralFeatureAction,
    UML2::WriteStructuralFeatureAction,
    UML2::ReadStructuralFeatureAction,
    LinkAction,
    UML2::WriteLinkAction,
    UML2::ReadLinkAction,
    WriteStructuralFeatureAction,
    UML2::AddStructuralFeatureValueAction,
    UML2::RemoveStructuralFeatureValueAction,
    State,
    UML2::FinalState,
    Vertex,
    UML2::ConnectionPointReference,
    UML2::Pseudostate,
    Constraint,
    UML2::InteractionConstraint,
    InteractionOccurrence,
    TemplateSignature,
    TemplateParameter,
    UML2::ClassifierTemplateParameter,
    UML2::ConnectableElementTemplateParameter,
    UML2::OperationTemplateParameter,
    MessageEnd,
    EventOccurrence,
    UML2::Stop,
    UML2::PartDecomposition,
    UML2::Gate,
    InteractionFragment,
    UML2::CombinedFragment,
    UML2::InteractionOccurrence,
    UML2::EventOccurrence,
    UML2::ExecutionOccurrence,
    UML2::Continuation,
    UML2::StateInvariant,
    StructuredActivityNode,
    UML2::LoopNode,
    UML2::ExpansionRegion,
    UML2::ConditionalNode,
    Trigger,
    UML2::ChangeTrigger,
    UML2::MessageTrigger,
    MessageTrigger,
    UML2::CallTrigger,
    ActivityGroup,
    Action,
    UML2::LinkAction,
    UML2::CreateObjectAction,
    UML2::ReadSelfAction,
    UML2::ClearAssociationAction,
    UML2::ApplyFunctionAction,
    UML2::StructuralFeatureAction,
    UML2::DestroyObjectAction,
    UML2::VariableAction,
    UML2::TestIdentityAction,
    UML2::AcceptEventAction,
    UML2::AnyTrigger,
    UML2::TimeTrigger,
    UML2::SignalTrigger,
    StructuredClassifier,
    UML2::EncapsulatedClassifier,
    InputPin,
    UML2::ValuePin,
    ActivityNode,
    ObjectNode,
    UML2::ActivityParameterNode,
    UML2::ExpansionNode,
    UML2::CentralBufferNode,
    Pin,
    UML2::InputPin,
    UML2::ExecutableNode,
    FinalNode,
    UML2::FlowFinalNode,
    UML2::ActivityFinalNode,
    ControlNode,
    UML2::DecisionNode,
    UML2::MergeNode,
    UML2::JoinNode,
    UML2::FinalNode,
    UML2::ForkNode,
    UML2::InitialNode,
    ActivityEdge,
    UML2::ObjectFlow,
    UML2::ControlFlow,
    UML2::ControlNode,
    UML2::OutputPin,
    ExecutableNode,
    UML2::InterruptibleActivityRegion,
    UML2::Action,
    Realization,
    Abstraction,
    UML2::Manifestation,
    UML2::Realization,
    Dependency,
    UML2::Usage,
    UML2::Abstraction,
    UML2::Permission,
    Property,
    UML2::Port,
    UML2::ExtensionEnd,
    Association,
    Behavior,
    UML2::Interaction,
    UML2::Activity,
    UML2::StateMachine,
    UML2::Implementation,
    PackageImport,
    Package,
    UML2::Model,
    UML2::Profile,
    Class,
    UML2::AssociationClass,
    UML2::Component,
    UML2::Stereotype,
    DeployedArtifact,
    DirectedRelationship,
    UML2::TemplateBinding,
    Feature,
    UML2::Connector,
    LiteralSpecification,
    UML2::LiteralInteger,
    UML2::LiteralString,
    UML2::LiteralUnlimitedNatural,
    UML2::LiteralNull,
    UML2::LiteralBoolean,
    Classifier,
    UML2::StructuredClassifier,
    UML2::TemplateableClassifier,
    UML2::Artifact,
    UML2::BehavioredClassifier,
    UML2::InformationItem,
    UML2::Actor,
    UML2::Signal,
    UML2::Interface,
    UML2::ParameterableClassifier,
    DataType,
    UML2::Enumeration,
    UML2::ProfileApplication,
    UML2::PackageMerge,
    UML2::Substitution,
    UML2::Generalization,
    RedefinableElement,
    UML2::ActivityNode,
    UML2::RedefinableTemplateSignature,
    UML2::Feature,
    UML2::Transition,
    UML2::ActivityEdge,
    UML2::ExtensionPoint,
    Type,
    UML2::PrimitiveType,
    InstanceSpecification,
    UML2::EnumerationLiteral,
    Namespace,
    UML2::State,
    UML2::Region,
    UML2::InteractionOperand,
    UML2::BehavioralFeature,
    UML2::StructuredActivityNode,
    DeploymentTarget,
    ConnectableElement,
    StructuralFeature,
    UML2::Property,
    PackageableElement,
    UML2::GeneralizationSet,
    UML2::InformationFlow,
    UML2::PrimitiveFunction,
    UML2::Package,
    UML2::InstanceSpecification,
    UML2::Type,
    UML2::Classifier,
    UML2::Extension,
    MultiplicityElement,
    UML2::ConnectorEnd,
    UML2::Pin,
    BehavioralFeature,
    UML2::Reception,
    UML2::DataType,
    EncapsulatedClassifier,
    BehavioredClassifier,
    UML2::Collaboration,
    UML2::UseCase,
    UML2::Class,
    Relationship,
    UML2::Association,
    UML2::DirectedRelationship,
    UML2::Dependency,
    TemplateableElement,
    UML2::NamedElement,
    Element,
    UML2::Relationship,
    UML2::QualifierValue,
    UML2::LinkEndData,
    UML2::TemplateSignature,
    UML2::Clause,
    UML2::ParameterableElement,
    UML2::ExceptionHandler,
    UML2::TemplateParameterSubstitution,
    UML2::TemplateableElement,
    UML2::ActivityGroup,
    UML2::Slot,
    UML2::TemplateParameter,
    UML2::MultiplicityElement,
    OpaqueExpression,
    UML2::Expression,
    ParameterableElement,
    TypedElement,
    UML2::Variable,
    UML2::ObjectNode,
    UML2::Operation,
    UML2::ValueSpecification,
    UML2::StructuralFeature,
    UML2::Behavior,
    UML2::Parameter,
    ValueSpecification,
    UML2::InstanceValue,
    UML2::LiteralSpecification,
    UML2::CreateLinkObjectAction,
    UML2::OpaqueExpression,
    UML2::ReadLinkObjectEndQualifierAction,
    UML2::PackageImport,
    UML2::ElementImport,
    Artifact,
    UML2::RaiseExceptionAction,
    UML2::ReplyAction,
    UML2::Constraint,
    AcceptEventAction,
    NamedElement,
    UML2::Message,
    UML2::ActivityPartition,
    UML2::GeneralOrdering,
    UML2::ParameterSet,
    UML2::TypedElement,
    UML2::Trigger,
    UML2::InteractionFragment,
    UML2::PackageableElement,
    UML2::ConnectableElement,
    UML2::RedefinableElement,
    UML2::Include,
    UML2::CollaborationOccurrence,
    UML2::Lifeline,
    UML2::MessageEnd,
    UML2::Vertex,
    UML2::Extend,
    UML2::AcceptCallAction,
    UML2::ReadIsClassifiedObjectAction,
    UML2::ReclassifyObjectAction,
    UML2::ReadLinkObjectEndAction,
    UML2::StartOwnedBehaviorAction,
    StateMachine,
    UML2::ProtocolStateMachine,
    UML2::ProtocolConformance,
    UML2::CommunicationPath,
    Node,
    UML2::ExecutionEnvironment,
    UML2::Device,
    UML2::ReadExtentAction,
    Transition,
    UML2::ProtocolTransition,
    UML2::Node,
    UML2::DeploymentSpecification,
    UML2::DeploymentTarget,
    UML2::DeployedArtifact,
    UML2::Deployment,
    UML2::Interval,
    Interval,
    UML2::DurationInterval,
    UML2::TimeObservationAction,
    UML2::Duration,
    UML2::TimeExpression,
    CentralBufferNode,
    UML2::DataStoreNode,
    UML2::DurationObservationAction,
    UML2::TimeInterval,
    UML2::IntervalConstraint,
    IntervalConstraint,
    UML2::DurationConstraint,
    UML2::TimeConstraint,
    UML2::SendSignalAction,
    UML2::InvocationAction,
    UML2::Namespace,
    UML2::StringExpression,
    UML2::Comment,
    UML2::Element,
    ConnectorKind,
    TransitionKind,
    MessageKind,
    PseudostateKind,
    ParameterEffectKind,
    VisibilityKind,
    InteractionOperator,
    AggregationKind,
    CallConcurrencyKind,
    ExpansionKind,
    ParameterDirectionKind,
    ObjectNodeOrderingKind,
    MessageSort,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
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
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_uml2::callaction_has_isSynchronous():
    assert hasattr(UML2::CallAction, "isSynchronous")
    descriptor = None
    for klass in UML2::CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallBehaviorAction)


def test_uml2::callbehavioraction_constructor_exists():
    assert callable(UML2::CallBehaviorAction.__init__)


def test_uml2::callbehavioraction_constructor_args():
    sig = inspect.signature(UML2::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CallOperationAction)


def test_uml2::calloperationaction_constructor_exists():
    assert callable(UML2::CallOperationAction.__init__)


def test_uml2::calloperationaction_constructor_args():
    sig = inspect.signature(UML2::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::SendObjectAction)


def test_uml2::sendobjectaction_constructor_exists():
    assert callable(UML2::SendObjectAction.__init__)


def test_uml2::sendobjectaction_constructor_args():
    sig = inspect.signature(UML2::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2::BroadcastSignalAction)


def test_uml2::broadcastsignalaction_constructor_exists():
    assert callable(UML2::BroadcastSignalAction.__init__)


def test_uml2::broadcastsignalaction_constructor_args():
    sig = inspect.signature(UML2::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadVariableAction)


def test_uml2::readvariableaction_constructor_exists():
    assert callable(UML2::ReadVariableAction.__init__)


def test_uml2::readvariableaction_constructor_args():
    sig = inspect.signature(UML2::ReadVariableAction.__init__)
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



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml2::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(UML2::LinkEndCreationData)


def test_uml2::linkendcreationdata_constructor_exists():
    assert callable(UML2::LinkEndCreationData.__init__)


def test_uml2::linkendcreationdata_constructor_args():
    sig = inspect.signature(UML2::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml2::linkendcreationdata_has_isReplaceAll():
    assert hasattr(UML2::LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in UML2::LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RemoveVariableValueAction)


def test_uml2::removevariablevalueaction_constructor_exists():
    assert callable(UML2::RemoveVariableValueAction.__init__)


def test_uml2::removevariablevalueaction_constructor_args():
    sig = inspect.signature(UML2::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AddVariableValueAction)


def test_uml2::addvariablevalueaction_constructor_exists():
    assert callable(UML2::AddVariableValueAction.__init__)


def test_uml2::addvariablevalueaction_constructor_args():
    sig = inspect.signature(UML2::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml2::addvariablevalueaction_has_isReplaceAll():
    assert hasattr(UML2::AddVariableValueAction, "isReplaceAll")
    descriptor = None
    for klass in UML2::AddVariableValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml2::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearVariableAction)


def test_uml2::clearvariableaction_constructor_exists():
    assert callable(UML2::ClearVariableAction.__init__)


def test_uml2::clearvariableaction_constructor_args():
    sig = inspect.signature(UML2::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteVariableAction)


def test_uml2::writevariableaction_constructor_exists():
    assert callable(UML2::WriteVariableAction.__init__)


def test_uml2::writevariableaction_constructor_args():
    sig = inspect.signature(UML2::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearStructuralFeatureAction)


def test_uml2::clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ClearStructuralFeatureAction.__init__)


def test_uml2::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::WriteStructuralFeatureAction)


def test_uml2::writestructuralfeatureaction_constructor_exists():
    assert callable(UML2::WriteStructuralFeatureAction.__init__)


def test_uml2::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadStructuralFeatureAction)


def test_uml2::readstructuralfeatureaction_constructor_exists():
    assert callable(UML2::ReadStructuralFeatureAction.__init__)


def test_uml2::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::ReadStructuralFeatureAction.__init__)
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



def test_uml2::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkAction)


def test_uml2::readlinkaction_constructor_exists():
    assert callable(UML2::ReadLinkAction.__init__)


def test_uml2::readlinkaction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AddStructuralFeatureValueAction)


def test_uml2::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::AddStructuralFeatureValueAction.__init__)


def test_uml2::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml2::addstructuralfeaturevalueaction_has_isReplaceAll():
    assert hasattr(UML2::AddStructuralFeatureValueAction, "isReplaceAll")
    descriptor = None
    for klass in UML2::AddStructuralFeatureValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml2::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RemoveStructuralFeatureValueAction)


def test_uml2::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2::RemoveStructuralFeatureValueAction.__init__)


def test_uml2::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2::RemoveStructuralFeatureValueAction.__init__)
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



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(UML2::ConnectionPointReference)


def test_uml2::connectionpointreference_constructor_exists():
    assert callable(UML2::ConnectionPointReference.__init__)


def test_uml2::connectionpointreference_constructor_args():
    sig = inspect.signature(UML2::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml2::pseudostate_is_not_abstract():
    assert not inspect.isabstract(UML2::Pseudostate)


def test_uml2::pseudostate_constructor_exists():
    assert callable(UML2::Pseudostate.__init__)


def test_uml2::pseudostate_constructor_args():
    sig = inspect.signature(UML2::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml2::pseudostate_has_kind():
    assert hasattr(UML2::Pseudostate, "kind")
    descriptor = None
    for klass in UML2::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



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



def test_interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(InteractionOccurrence)


def test_interactionoccurrence_constructor_exists():
    assert callable(InteractionOccurrence.__init__)


def test_interactionoccurrence_constructor_args():
    sig = inspect.signature(InteractionOccurrence.__init__)
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



def test_uml2::classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2::ClassifierTemplateParameter)


def test_uml2::classifiertemplateparameter_constructor_exists():
    assert callable(UML2::ClassifierTemplateParameter.__init__)


def test_uml2::classifiertemplateparameter_constructor_args():
    sig = inspect.signature(UML2::ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"

def test_uml2::classifiertemplateparameter_has_allowSubstitutable():
    assert hasattr(UML2::ClassifierTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in UML2::ClassifierTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml2::connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2::ConnectableElementTemplateParameter)


def test_uml2::connectableelementtemplateparameter_constructor_exists():
    assert callable(UML2::ConnectableElementTemplateParameter.__init__)


def test_uml2::connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(UML2::ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2::operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2::OperationTemplateParameter)


def test_uml2::operationtemplateparameter_constructor_exists():
    assert callable(UML2::OperationTemplateParameter.__init__)


def test_uml2::operationtemplateparameter_constructor_args():
    sig = inspect.signature(UML2::OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
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



def test_uml2::partdecomposition_is_not_abstract():
    assert not inspect.isabstract(UML2::PartDecomposition)


def test_uml2::partdecomposition_constructor_exists():
    assert callable(UML2::PartDecomposition.__init__)


def test_uml2::partdecomposition_constructor_args():
    sig = inspect.signature(UML2::PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml2::gate_is_not_abstract():
    assert not inspect.isabstract(UML2::Gate)


def test_uml2::gate_constructor_exists():
    assert callable(UML2::Gate.__init__)


def test_uml2::gate_constructor_args():
    sig = inspect.signature(UML2::Gate.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(UML2::CombinedFragment)


def test_uml2::combinedfragment_constructor_exists():
    assert callable(UML2::CombinedFragment.__init__)


def test_uml2::combinedfragment_constructor_args():
    sig = inspect.signature(UML2::CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_uml2::combinedfragment_has_interactionOperator():
    assert hasattr(UML2::CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in UML2::CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_uml2::interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionOccurrence)


def test_uml2::interactionoccurrence_constructor_exists():
    assert callable(UML2::InteractionOccurrence.__init__)


def test_uml2::interactionoccurrence_constructor_args():
    sig = inspect.signature(UML2::InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::EventOccurrence)


def test_uml2::eventoccurrence_constructor_exists():
    assert callable(UML2::EventOccurrence.__init__)


def test_uml2::eventoccurrence_constructor_args():
    sig = inspect.signature(UML2::EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::executionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutionOccurrence)


def test_uml2::executionoccurrence_constructor_exists():
    assert callable(UML2::ExecutionOccurrence.__init__)


def test_uml2::executionoccurrence_constructor_args():
    sig = inspect.signature(UML2::ExecutionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::continuation_is_not_abstract():
    assert not inspect.isabstract(UML2::Continuation)


def test_uml2::continuation_constructor_exists():
    assert callable(UML2::Continuation.__init__)


def test_uml2::continuation_constructor_args():
    sig = inspect.signature(UML2::Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_uml2::continuation_has_setting():
    assert hasattr(UML2::Continuation, "setting")
    descriptor = None
    for klass in UML2::Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_uml2::stateinvariant_is_not_abstract():
    assert not inspect.isabstract(UML2::StateInvariant)


def test_uml2::stateinvariant_constructor_exists():
    assert callable(UML2::StateInvariant.__init__)


def test_uml2::stateinvariant_constructor_args():
    sig = inspect.signature(UML2::StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::loopnode_is_not_abstract():
    assert not inspect.isabstract(UML2::LoopNode)


def test_uml2::loopnode_constructor_exists():
    assert callable(UML2::LoopNode.__init__)


def test_uml2::loopnode_constructor_args():
    sig = inspect.signature(UML2::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_uml2::loopnode_has_isTestedFirst():
    assert hasattr(UML2::LoopNode, "isTestedFirst")
    descriptor = None
    for klass in UML2::LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_uml2::expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML2::ExpansionRegion)


def test_uml2::expansionregion_constructor_exists():
    assert callable(UML2::ExpansionRegion.__init__)


def test_uml2::expansionregion_constructor_args():
    sig = inspect.signature(UML2::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_uml2::expansionregion_has_mode():
    assert hasattr(UML2::ExpansionRegion, "mode")
    descriptor = None
    for klass in UML2::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_uml2::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ConditionalNode)


def test_uml2::conditionalnode_constructor_exists():
    assert callable(UML2::ConditionalNode.__init__)


def test_uml2::conditionalnode_constructor_args():
    sig = inspect.signature(UML2::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isAssured" in params, "Missing parameter 'isAssured'"
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"

def test_uml2::conditionalnode_has_isAssured():
    assert hasattr(UML2::ConditionalNode, "isAssured")
    descriptor = None
    for klass in UML2::ConditionalNode.__mro__:
        if "isAssured" in klass.__dict__:
            descriptor = klass.__dict__["isAssured"]
            break
    assert isinstance(descriptor, property)

def test_uml2::conditionalnode_has_isDeterminate():
    assert hasattr(UML2::ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in UML2::ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::changetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::ChangeTrigger)


def test_uml2::changetrigger_constructor_exists():
    assert callable(UML2::ChangeTrigger.__init__)


def test_uml2::changetrigger_constructor_args():
    sig = inspect.signature(UML2::ChangeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::messagetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::MessageTrigger)


def test_uml2::messagetrigger_constructor_exists():
    assert callable(UML2::MessageTrigger.__init__)


def test_uml2::messagetrigger_constructor_args():
    sig = inspect.signature(UML2::MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_messagetrigger_is_not_abstract():
    assert not inspect.isabstract(MessageTrigger)


def test_messagetrigger_constructor_exists():
    assert callable(MessageTrigger.__init__)


def test_messagetrigger_constructor_args():
    sig = inspect.signature(MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::calltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::CallTrigger)


def test_uml2::calltrigger_constructor_exists():
    assert callable(UML2::CallTrigger.__init__)


def test_uml2::calltrigger_constructor_args():
    sig = inspect.signature(UML2::CallTrigger.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
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



def test_uml2::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateObjectAction)


def test_uml2::createobjectaction_constructor_exists():
    assert callable(UML2::CreateObjectAction.__init__)


def test_uml2::createobjectaction_constructor_args():
    sig = inspect.signature(UML2::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readselfaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadSelfAction)


def test_uml2::readselfaction_constructor_exists():
    assert callable(UML2::ReadSelfAction.__init__)


def test_uml2::readselfaction_constructor_args():
    sig = inspect.signature(UML2::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ClearAssociationAction)


def test_uml2::clearassociationaction_constructor_exists():
    assert callable(UML2::ClearAssociationAction.__init__)


def test_uml2::clearassociationaction_constructor_args():
    sig = inspect.signature(UML2::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::applyfunctionaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ApplyFunctionAction)


def test_uml2::applyfunctionaction_constructor_exists():
    assert callable(UML2::ApplyFunctionAction.__init__)


def test_uml2::applyfunctionaction_constructor_args():
    sig = inspect.signature(UML2::ApplyFunctionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeatureAction)


def test_uml2::structuralfeatureaction_constructor_exists():
    assert callable(UML2::StructuralFeatureAction.__init__)


def test_uml2::structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DestroyObjectAction)


def test_uml2::destroyobjectaction_constructor_exists():
    assert callable(UML2::DestroyObjectAction.__init__)


def test_uml2::destroyobjectaction_constructor_args():
    sig = inspect.signature(UML2::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyOwnedObjects" in params, "Missing parameter 'isDestroyOwnedObjects'"
    assert "isDestroyLinks" in params, "Missing parameter 'isDestroyLinks'"

def test_uml2::destroyobjectaction_has_isDestroyOwnedObjects():
    assert hasattr(UML2::DestroyObjectAction, "isDestroyOwnedObjects")
    descriptor = None
    for klass in UML2::DestroyObjectAction.__mro__:
        if "isDestroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)

def test_uml2::destroyobjectaction_has_isDestroyLinks():
    assert hasattr(UML2::DestroyObjectAction, "isDestroyLinks")
    descriptor = None
    for klass in UML2::DestroyObjectAction.__mro__:
        if "isDestroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyLinks"]
            break
    assert isinstance(descriptor, property)



def test_uml2::variableaction_is_not_abstract():
    assert not inspect.isabstract(UML2::VariableAction)


def test_uml2::variableaction_constructor_exists():
    assert callable(UML2::VariableAction.__init__)


def test_uml2::variableaction_constructor_args():
    sig = inspect.signature(UML2::VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2::TestIdentityAction)


def test_uml2::testidentityaction_constructor_exists():
    assert callable(UML2::TestIdentityAction.__init__)


def test_uml2::testidentityaction_constructor_args():
    sig = inspect.signature(UML2::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AcceptEventAction)


def test_uml2::accepteventaction_constructor_exists():
    assert callable(UML2::AcceptEventAction.__init__)


def test_uml2::accepteventaction_constructor_args():
    sig = inspect.signature(UML2::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::anytrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::AnyTrigger)


def test_uml2::anytrigger_constructor_exists():
    assert callable(UML2::AnyTrigger.__init__)


def test_uml2::anytrigger_constructor_args():
    sig = inspect.signature(UML2::AnyTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeTrigger)


def test_uml2::timetrigger_constructor_exists():
    assert callable(UML2::TimeTrigger.__init__)


def test_uml2::timetrigger_constructor_args():
    sig = inspect.signature(UML2::TimeTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_uml2::timetrigger_has_isRelative():
    assert hasattr(UML2::TimeTrigger, "isRelative")
    descriptor = None
    for klass in UML2::TimeTrigger.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_uml2::signaltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2::SignalTrigger)


def test_uml2::signaltrigger_constructor_exists():
    assert callable(UML2::SignalTrigger.__init__)


def test_uml2::signaltrigger_constructor_args():
    sig = inspect.signature(UML2::SignalTrigger.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::EncapsulatedClassifier)


def test_uml2::encapsulatedclassifier_constructor_exists():
    assert callable(UML2::EncapsulatedClassifier.__init__)


def test_uml2::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2::EncapsulatedClassifier.__init__)
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



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
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



def test_uml2::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2::CentralBufferNode)


def test_uml2::centralbuffernode_constructor_exists():
    assert callable(UML2::CentralBufferNode.__init__)


def test_uml2::centralbuffernode_constructor_args():
    sig = inspect.signature(UML2::CentralBufferNode.__init__)
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



def test_uml2::executablenode_is_not_abstract():
    assert not inspect.isabstract(UML2::ExecutableNode)


def test_uml2::executablenode_constructor_exists():
    assert callable(UML2::ExecutableNode.__init__)


def test_uml2::executablenode_constructor_args():
    sig = inspect.signature(UML2::ExecutableNode.__init__)
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



def test_uml2::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityFinalNode)


def test_uml2::activityfinalnode_constructor_exists():
    assert callable(UML2::ActivityFinalNode.__init__)


def test_uml2::activityfinalnode_constructor_args():
    sig = inspect.signature(UML2::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::decisionnode_is_not_abstract():
    assert not inspect.isabstract(UML2::DecisionNode)


def test_uml2::decisionnode_constructor_exists():
    assert callable(UML2::DecisionNode.__init__)


def test_uml2::decisionnode_constructor_args():
    sig = inspect.signature(UML2::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::mergenode_is_not_abstract():
    assert not inspect.isabstract(UML2::MergeNode)


def test_uml2::mergenode_constructor_exists():
    assert callable(UML2::MergeNode.__init__)


def test_uml2::mergenode_constructor_args():
    sig = inspect.signature(UML2::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::joinnode_is_not_abstract():
    assert not inspect.isabstract(UML2::JoinNode)


def test_uml2::joinnode_constructor_exists():
    assert callable(UML2::JoinNode.__init__)


def test_uml2::joinnode_constructor_args():
    sig = inspect.signature(UML2::JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_uml2::joinnode_has_isCombineDuplicate():
    assert hasattr(UML2::JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in UML2::JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_uml2::finalnode_is_not_abstract():
    assert not inspect.isabstract(UML2::FinalNode)


def test_uml2::finalnode_constructor_exists():
    assert callable(UML2::FinalNode.__init__)


def test_uml2::finalnode_constructor_args():
    sig = inspect.signature(UML2::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::forknode_is_not_abstract():
    assert not inspect.isabstract(UML2::ForkNode)


def test_uml2::forknode_constructor_exists():
    assert callable(UML2::ForkNode.__init__)


def test_uml2::forknode_constructor_args():
    sig = inspect.signature(UML2::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::initialnode_is_not_abstract():
    assert not inspect.isabstract(UML2::InitialNode)


def test_uml2::initialnode_constructor_exists():
    assert callable(UML2::InitialNode.__init__)


def test_uml2::initialnode_constructor_args():
    sig = inspect.signature(UML2::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml2::objectflow_is_not_abstract():
    assert not inspect.isabstract(UML2::ObjectFlow)


def test_uml2::objectflow_constructor_exists():
    assert callable(UML2::ObjectFlow.__init__)


def test_uml2::objectflow_constructor_args():
    sig = inspect.signature(UML2::ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"

def test_uml2::objectflow_has_isMultireceive():
    assert hasattr(UML2::ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in UML2::ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_uml2::objectflow_has_isMulticast():
    assert hasattr(UML2::ObjectFlow, "isMulticast")
    descriptor = None
    for klass in UML2::ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)



def test_uml2::controlflow_is_not_abstract():
    assert not inspect.isabstract(UML2::ControlFlow)


def test_uml2::controlflow_constructor_exists():
    assert callable(UML2::ControlFlow.__init__)


def test_uml2::controlflow_constructor_args():
    sig = inspect.signature(UML2::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2::controlnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ControlNode)


def test_uml2::controlnode_constructor_exists():
    assert callable(UML2::ControlNode.__init__)


def test_uml2::controlnode_constructor_args():
    sig = inspect.signature(UML2::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2::OutputPin)


def test_uml2::outputpin_constructor_exists():
    assert callable(UML2::OutputPin.__init__)


def test_uml2::outputpin_constructor_args():
    sig = inspect.signature(UML2::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(UML2::InterruptibleActivityRegion)


def test_uml2::interruptibleactivityregion_constructor_exists():
    assert callable(UML2::InterruptibleActivityRegion.__init__)


def test_uml2::interruptibleactivityregion_constructor_args():
    sig = inspect.signature(UML2::InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml2::action_is_not_abstract():
    assert not inspect.isabstract(UML2::Action)


def test_uml2::action_constructor_exists():
    assert callable(UML2::Action.__init__)


def test_uml2::action_constructor_args():
    sig = inspect.signature(UML2::Action.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"

def test_uml2::action_has_effect():
    assert hasattr(UML2::Action, "effect")
    descriptor = None
    for klass in UML2::Action.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::manifestation_is_not_abstract():
    assert not inspect.isabstract(UML2::Manifestation)


def test_uml2::manifestation_constructor_exists():
    assert callable(UML2::Manifestation.__init__)


def test_uml2::manifestation_constructor_args():
    sig = inspect.signature(UML2::Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml2::realization_is_not_abstract():
    assert not inspect.isabstract(UML2::Realization)


def test_uml2::realization_constructor_exists():
    assert callable(UML2::Realization.__init__)


def test_uml2::realization_constructor_args():
    sig = inspect.signature(UML2::Realization.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml2::usage_is_not_abstract():
    assert not inspect.isabstract(UML2::Usage)


def test_uml2::usage_constructor_exists():
    assert callable(UML2::Usage.__init__)


def test_uml2::usage_constructor_args():
    sig = inspect.signature(UML2::Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml2::abstraction_is_not_abstract():
    assert not inspect.isabstract(UML2::Abstraction)


def test_uml2::abstraction_constructor_exists():
    assert callable(UML2::Abstraction.__init__)


def test_uml2::abstraction_constructor_args():
    sig = inspect.signature(UML2::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::permission_is_not_abstract():
    assert not inspect.isabstract(UML2::Permission)


def test_uml2::permission_constructor_exists():
    assert callable(UML2::Permission.__init__)


def test_uml2::permission_constructor_args():
    sig = inspect.signature(UML2::Permission.__init__)
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
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"
    assert "isService" in params, "Missing parameter 'isService'"

def test_uml2::port_has_isBehavior():
    assert hasattr(UML2::Port, "isBehavior")
    descriptor = None
    for klass in UML2::Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)

def test_uml2::port_has_isService():
    assert hasattr(UML2::Port, "isService")
    descriptor = None
    for klass in UML2::Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)



def test_uml2::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionEnd)


def test_uml2::extensionend_constructor_exists():
    assert callable(UML2::ExtensionEnd.__init__)


def test_uml2::extensionend_constructor_args():
    sig = inspect.signature(UML2::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interaction_is_not_abstract():
    assert not inspect.isabstract(UML2::Interaction)


def test_uml2::interaction_constructor_exists():
    assert callable(UML2::Interaction.__init__)


def test_uml2::interaction_constructor_args():
    sig = inspect.signature(UML2::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activity_is_not_abstract():
    assert not inspect.isabstract(UML2::Activity)


def test_uml2::activity_constructor_exists():
    assert callable(UML2::Activity.__init__)


def test_uml2::activity_constructor_args():
    sig = inspect.signature(UML2::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "language" in params, "Missing parameter 'language'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml2::activity_has_body():
    assert hasattr(UML2::Activity, "body")
    descriptor = None
    for klass in UML2::Activity.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml2::activity_has_isSingleExecution():
    assert hasattr(UML2::Activity, "isSingleExecution")
    descriptor = None
    for klass in UML2::Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_uml2::activity_has_language():
    assert hasattr(UML2::Activity, "language")
    descriptor = None
    for klass in UML2::Activity.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml2::activity_has_isReadOnly():
    assert hasattr(UML2::Activity, "isReadOnly")
    descriptor = None
    for klass in UML2::Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_uml2::statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2::StateMachine)


def test_uml2::statemachine_constructor_exists():
    assert callable(UML2::StateMachine.__init__)


def test_uml2::statemachine_constructor_args():
    sig = inspect.signature(UML2::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::implementation_is_not_abstract():
    assert not inspect.isabstract(UML2::Implementation)


def test_uml2::implementation_constructor_exists():
    assert callable(UML2::Implementation.__init__)


def test_uml2::implementation_constructor_args():
    sig = inspect.signature(UML2::Implementation.__init__)
    params = list(sig.parameters.keys())



def test_packageimport_is_not_abstract():
    assert not inspect.isabstract(PackageImport)


def test_packageimport_constructor_exists():
    assert callable(PackageImport.__init__)


def test_packageimport_constructor_args():
    sig = inspect.signature(PackageImport.__init__)
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
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"

def test_uml2::model_has_viewpoint():
    assert hasattr(UML2::Model, "viewpoint")
    descriptor = None
    for klass in UML2::Model.__mro__:
        if "viewpoint" in klass.__dict__:
            descriptor = klass.__dict__["viewpoint"]
            break
    assert isinstance(descriptor, property)



def test_uml2::profile_is_not_abstract():
    assert not inspect.isabstract(UML2::Profile)


def test_uml2::profile_constructor_exists():
    assert callable(UML2::Profile.__init__)


def test_uml2::profile_constructor_args():
    sig = inspect.signature(UML2::Profile.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2::AssociationClass)


def test_uml2::associationclass_constructor_exists():
    assert callable(UML2::AssociationClass.__init__)


def test_uml2::associationclass_constructor_args():
    sig = inspect.signature(UML2::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2::component_is_not_abstract():
    assert not inspect.isabstract(UML2::Component)


def test_uml2::component_constructor_exists():
    assert callable(UML2::Component.__init__)


def test_uml2::component_constructor_args():
    sig = inspect.signature(UML2::Component.__init__)
    params = list(sig.parameters.keys())
    assert "isIndirectlyInstantiated" in params, "Missing parameter 'isIndirectlyInstantiated'"

def test_uml2::component_has_isIndirectlyInstantiated():
    assert hasattr(UML2::Component, "isIndirectlyInstantiated")
    descriptor = None
    for klass in UML2::Component.__mro__:
        if "isIndirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["isIndirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)



def test_uml2::stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2::Stereotype)


def test_uml2::stereotype_constructor_exists():
    assert callable(UML2::Stereotype.__init__)


def test_uml2::stereotype_constructor_args():
    sig = inspect.signature(UML2::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templatebinding_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateBinding)


def test_uml2::templatebinding_constructor_exists():
    assert callable(UML2::TemplateBinding.__init__)


def test_uml2::templatebinding_constructor_args():
    sig = inspect.signature(UML2::TemplateBinding.__init__)
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
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml2::connector_has_kind():
    assert hasattr(UML2::Connector, "kind")
    descriptor = None
    for klass in UML2::Connector.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



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
    assert "value" in params, "Missing parameter 'value'"

def test_uml2::literalinteger_has_value():
    assert hasattr(UML2::LiteralInteger, "value")
    descriptor = None
    for klass in UML2::LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml2::literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralString)


def test_uml2::literalstring_constructor_exists():
    assert callable(UML2::LiteralString.__init__)


def test_uml2::literalstring_constructor_args():
    sig = inspect.signature(UML2::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml2::literalstring_has_value():
    assert hasattr(UML2::LiteralString, "value")
    descriptor = None
    for klass in UML2::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml2::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralUnlimitedNatural)


def test_uml2::literalunlimitednatural_constructor_exists():
    assert callable(UML2::LiteralUnlimitedNatural.__init__)


def test_uml2::literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml2::literalunlimitednatural_has_value():
    assert hasattr(UML2::LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in UML2::LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml2::literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralNull)


def test_uml2::literalnull_constructor_exists():
    assert callable(UML2::LiteralNull.__init__)


def test_uml2::literalnull_constructor_args():
    sig = inspect.signature(UML2::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralBoolean)


def test_uml2::literalboolean_constructor_exists():
    assert callable(UML2::LiteralBoolean.__init__)


def test_uml2::literalboolean_constructor_args():
    sig = inspect.signature(UML2::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml2::literalboolean_has_value():
    assert hasattr(UML2::LiteralBoolean, "value")
    descriptor = None
    for klass in UML2::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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



def test_uml2::templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateableClassifier)


def test_uml2::templateableclassifier_constructor_exists():
    assert callable(UML2::TemplateableClassifier.__init__)


def test_uml2::templateableclassifier_constructor_args():
    sig = inspect.signature(UML2::TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::artifact_is_not_abstract():
    assert not inspect.isabstract(UML2::Artifact)


def test_uml2::artifact_constructor_exists():
    assert callable(UML2::Artifact.__init__)


def test_uml2::artifact_constructor_args():
    sig = inspect.signature(UML2::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_uml2::artifact_has_fileName():
    assert hasattr(UML2::Artifact, "fileName")
    descriptor = None
    for klass in UML2::Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_uml2::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioredClassifier)


def test_uml2::behavioredclassifier_constructor_exists():
    assert callable(UML2::BehavioredClassifier.__init__)


def test_uml2::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2::InformationItem)


def test_uml2::informationitem_constructor_exists():
    assert callable(UML2::InformationItem.__init__)


def test_uml2::informationitem_constructor_args():
    sig = inspect.signature(UML2::InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2::actor_is_not_abstract():
    assert not inspect.isabstract(UML2::Actor)


def test_uml2::actor_constructor_exists():
    assert callable(UML2::Actor.__init__)


def test_uml2::actor_constructor_args():
    sig = inspect.signature(UML2::Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2::signal_is_not_abstract():
    assert not inspect.isabstract(UML2::Signal)


def test_uml2::signal_constructor_exists():
    assert callable(UML2::Signal.__init__)


def test_uml2::signal_constructor_args():
    sig = inspect.signature(UML2::Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interface_is_not_abstract():
    assert not inspect.isabstract(UML2::Interface)


def test_uml2::interface_constructor_exists():
    assert callable(UML2::Interface.__init__)


def test_uml2::interface_constructor_args():
    sig = inspect.signature(UML2::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterableClassifier)


def test_uml2::parameterableclassifier_constructor_exists():
    assert callable(UML2::ParameterableClassifier.__init__)


def test_uml2::parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2::ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2::enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2::Enumeration)


def test_uml2::enumeration_constructor_exists():
    assert callable(UML2::Enumeration.__init__)


def test_uml2::enumeration_constructor_args():
    sig = inspect.signature(UML2::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2::profileapplication_is_not_abstract():
    assert not inspect.isabstract(UML2::ProfileApplication)


def test_uml2::profileapplication_constructor_exists():
    assert callable(UML2::ProfileApplication.__init__)


def test_uml2::profileapplication_constructor_args():
    sig = inspect.signature(UML2::ProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_uml2::packagemerge_is_not_abstract():
    assert not inspect.isabstract(UML2::PackageMerge)


def test_uml2::packagemerge_constructor_exists():
    assert callable(UML2::PackageMerge.__init__)


def test_uml2::packagemerge_constructor_args():
    sig = inspect.signature(UML2::PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml2::substitution_is_not_abstract():
    assert not inspect.isabstract(UML2::Substitution)


def test_uml2::substitution_constructor_exists():
    assert callable(UML2::Substitution.__init__)


def test_uml2::substitution_constructor_args():
    sig = inspect.signature(UML2::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2::generalization_is_not_abstract():
    assert not inspect.isabstract(UML2::Generalization)


def test_uml2::generalization_constructor_exists():
    assert callable(UML2::Generalization.__init__)


def test_uml2::generalization_constructor_args():
    sig = inspect.signature(UML2::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_uml2::generalization_has_isSubstitutable():
    assert hasattr(UML2::Generalization, "isSubstitutable")
    descriptor = None
    for klass in UML2::Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



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



def test_uml2::redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2::RedefinableTemplateSignature)


def test_uml2::redefinabletemplatesignature_constructor_exists():
    assert callable(UML2::RedefinableTemplateSignature.__init__)


def test_uml2::redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(UML2::RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::feature_is_not_abstract():
    assert not inspect.isabstract(UML2::Feature)


def test_uml2::feature_constructor_exists():
    assert callable(UML2::Feature.__init__)


def test_uml2::feature_constructor_args():
    sig = inspect.signature(UML2::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml2::feature_has_isStatic():
    assert hasattr(UML2::Feature, "isStatic")
    descriptor = None
    for klass in UML2::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_uml2::transition_is_not_abstract():
    assert not inspect.isabstract(UML2::Transition)


def test_uml2::transition_constructor_exists():
    assert callable(UML2::Transition.__init__)


def test_uml2::transition_constructor_args():
    sig = inspect.signature(UML2::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml2::transition_has_kind():
    assert hasattr(UML2::Transition, "kind")
    descriptor = None
    for klass in UML2::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml2::activityedge_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityEdge)


def test_uml2::activityedge_constructor_exists():
    assert callable(UML2::ActivityEdge.__init__)


def test_uml2::activityedge_constructor_args():
    sig = inspect.signature(UML2::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionPoint)


def test_uml2::extensionpoint_constructor_exists():
    assert callable(UML2::ExtensionPoint.__init__)


def test_uml2::extensionpoint_constructor_args():
    sig = inspect.signature(UML2::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2::primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2::PrimitiveType)


def test_uml2::primitivetype_constructor_exists():
    assert callable(UML2::PrimitiveType.__init__)


def test_uml2::primitivetype_constructor_args():
    sig = inspect.signature(UML2::PrimitiveType.__init__)
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



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2::state_is_not_abstract():
    assert not inspect.isabstract(UML2::State)


def test_uml2::state_constructor_exists():
    assert callable(UML2::State.__init__)


def test_uml2::state_constructor_args():
    sig = inspect.signature(UML2::State.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"

def test_uml2::state_has_isComposite():
    assert hasattr(UML2::State, "isComposite")
    descriptor = None
    for klass in UML2::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml2::state_has_isSubmachineState():
    assert hasattr(UML2::State, "isSubmachineState")
    descriptor = None
    for klass in UML2::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_uml2::state_has_isSimple():
    assert hasattr(UML2::State, "isSimple")
    descriptor = None
    for klass in UML2::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_uml2::state_has_isOrthogonal():
    assert hasattr(UML2::State, "isOrthogonal")
    descriptor = None
    for klass in UML2::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)



def test_uml2::region_is_not_abstract():
    assert not inspect.isabstract(UML2::Region)


def test_uml2::region_constructor_exists():
    assert callable(UML2::Region.__init__)


def test_uml2::region_constructor_args():
    sig = inspect.signature(UML2::Region.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionOperand)


def test_uml2::interactionoperand_constructor_exists():
    assert callable(UML2::InteractionOperand.__init__)


def test_uml2::interactionoperand_constructor_args():
    sig = inspect.signature(UML2::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::BehavioralFeature)


def test_uml2::behavioralfeature_constructor_exists():
    assert callable(UML2::BehavioralFeature.__init__)


def test_uml2::behavioralfeature_constructor_args():
    sig = inspect.signature(UML2::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "concurrency" in params, "Missing parameter 'concurrency'"

def test_uml2::behavioralfeature_has_isAbstract():
    assert hasattr(UML2::BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in UML2::BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_uml2::behavioralfeature_has_concurrency():
    assert hasattr(UML2::BehavioralFeature, "concurrency")
    descriptor = None
    for klass in UML2::BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)



def test_uml2::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuredActivityNode)


def test_uml2::structuredactivitynode_constructor_exists():
    assert callable(UML2::StructuredActivityNode.__init__)


def test_uml2::structuredactivitynode_constructor_args():
    sig = inspect.signature(UML2::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_uml2::structuredactivitynode_has_mustIsolate():
    assert hasattr(UML2::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in UML2::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
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



def test_uml2::property_is_not_abstract():
    assert not inspect.isabstract(UML2::Property)


def test_uml2::property_constructor_exists():
    assert callable(UML2::Property.__init__)


def test_uml2::property_constructor_args():
    sig = inspect.signature(UML2::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml2::property_has_isComposite():
    assert hasattr(UML2::Property, "isComposite")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml2::property_has_isDerivedUnion():
    assert hasattr(UML2::Property, "isDerivedUnion")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_uml2::property_has_aggregation():
    assert hasattr(UML2::Property, "aggregation")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_uml2::property_has_default():
    assert hasattr(UML2::Property, "default")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml2::property_has_isDerived():
    assert hasattr(UML2::Property, "isDerived")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::generalizationset_is_not_abstract():
    assert not inspect.isabstract(UML2::GeneralizationSet)


def test_uml2::generalizationset_constructor_exists():
    assert callable(UML2::GeneralizationSet.__init__)


def test_uml2::generalizationset_constructor_args():
    sig = inspect.signature(UML2::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"

def test_uml2::generalizationset_has_isCovering():
    assert hasattr(UML2::GeneralizationSet, "isCovering")
    descriptor = None
    for klass in UML2::GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)

def test_uml2::generalizationset_has_isDisjoint():
    assert hasattr(UML2::GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in UML2::GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)



def test_uml2::informationflow_is_not_abstract():
    assert not inspect.isabstract(UML2::InformationFlow)


def test_uml2::informationflow_constructor_exists():
    assert callable(UML2::InformationFlow.__init__)


def test_uml2::informationflow_constructor_args():
    sig = inspect.signature(UML2::InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2::primitivefunction_is_not_abstract():
    assert not inspect.isabstract(UML2::PrimitiveFunction)


def test_uml2::primitivefunction_constructor_exists():
    assert callable(UML2::PrimitiveFunction.__init__)


def test_uml2::primitivefunction_constructor_args():
    sig = inspect.signature(UML2::PrimitiveFunction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_uml2::primitivefunction_has_body():
    assert hasattr(UML2::PrimitiveFunction, "body")
    descriptor = None
    for klass in UML2::PrimitiveFunction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_uml2::primitivefunction_has_language():
    assert hasattr(UML2::PrimitiveFunction, "language")
    descriptor = None
    for klass in UML2::PrimitiveFunction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_uml2::package_is_not_abstract():
    assert not inspect.isabstract(UML2::Package)


def test_uml2::package_constructor_exists():
    assert callable(UML2::Package.__init__)


def test_uml2::package_constructor_args():
    sig = inspect.signature(UML2::Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2::instancespecification_is_not_abstract():
    assert not inspect.isabstract(UML2::InstanceSpecification)


def test_uml2::instancespecification_constructor_exists():
    assert callable(UML2::InstanceSpecification.__init__)


def test_uml2::instancespecification_constructor_args():
    sig = inspect.signature(UML2::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::type_is_not_abstract():
    assert not inspect.isabstract(UML2::Type)


def test_uml2::type_constructor_exists():
    assert callable(UML2::Type.__init__)


def test_uml2::type_constructor_args():
    sig = inspect.signature(UML2::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2::classifier_is_not_abstract():
    assert not inspect.isabstract(UML2::Classifier)


def test_uml2::classifier_constructor_exists():
    assert callable(UML2::Classifier.__init__)


def test_uml2::classifier_constructor_args():
    sig = inspect.signature(UML2::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml2::classifier_has_isAbstract():
    assert hasattr(UML2::Classifier, "isAbstract")
    descriptor = None
    for klass in UML2::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml2::extension_is_not_abstract():
    assert not inspect.isabstract(UML2::Extension)


def test_uml2::extension_constructor_exists():
    assert callable(UML2::Extension.__init__)


def test_uml2::extension_constructor_args():
    sig = inspect.signature(UML2::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_uml2::extension_has_isRequired():
    assert hasattr(UML2::Extension, "isRequired")
    descriptor = None
    for klass in UML2::Extension.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::connectorend_is_not_abstract():
    assert not inspect.isabstract(UML2::ConnectorEnd)


def test_uml2::connectorend_constructor_exists():
    assert callable(UML2::ConnectorEnd.__init__)


def test_uml2::connectorend_constructor_args():
    sig = inspect.signature(UML2::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2::pin_is_not_abstract():
    assert not inspect.isabstract(UML2::Pin)


def test_uml2::pin_constructor_exists():
    assert callable(UML2::Pin.__init__)


def test_uml2::pin_constructor_args():
    sig = inspect.signature(UML2::Pin.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::reception_is_not_abstract():
    assert not inspect.isabstract(UML2::Reception)


def test_uml2::reception_constructor_exists():
    assert callable(UML2::Reception.__init__)


def test_uml2::reception_constructor_args():
    sig = inspect.signature(UML2::Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2::datatype_is_not_abstract():
    assert not inspect.isabstract(UML2::DataType)


def test_uml2::datatype_constructor_exists():
    assert callable(UML2::DataType.__init__)


def test_uml2::datatype_constructor_args():
    sig = inspect.signature(UML2::DataType.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2::collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2::Collaboration)


def test_uml2::collaboration_constructor_exists():
    assert callable(UML2::Collaboration.__init__)


def test_uml2::collaboration_constructor_args():
    sig = inspect.signature(UML2::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2::usecase_is_not_abstract():
    assert not inspect.isabstract(UML2::UseCase)


def test_uml2::usecase_constructor_exists():
    assert callable(UML2::UseCase.__init__)


def test_uml2::usecase_constructor_args():
    sig = inspect.signature(UML2::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml2::class_is_not_abstract():
    assert not inspect.isabstract(UML2::Class)


def test_uml2::class_constructor_exists():
    assert callable(UML2::Class.__init__)


def test_uml2::class_constructor_args():
    sig = inspect.signature(UML2::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml2::class_has_isActive():
    assert hasattr(UML2::Class, "isActive")
    descriptor = None
    for klass in UML2::Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2::association_is_not_abstract():
    assert not inspect.isabstract(UML2::Association)


def test_uml2::association_constructor_exists():
    assert callable(UML2::Association.__init__)


def test_uml2::association_constructor_args():
    sig = inspect.signature(UML2::Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml2::association_has_isDerived():
    assert hasattr(UML2::Association, "isDerived")
    descriptor = None
    for klass in UML2::Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_uml2::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(UML2::DirectedRelationship)


def test_uml2::directedrelationship_constructor_exists():
    assert callable(UML2::DirectedRelationship.__init__)


def test_uml2::directedrelationship_constructor_args():
    sig = inspect.signature(UML2::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2::dependency_is_not_abstract():
    assert not inspect.isabstract(UML2::Dependency)


def test_uml2::dependency_constructor_exists():
    assert callable(UML2::Dependency.__init__)


def test_uml2::dependency_constructor_args():
    sig = inspect.signature(UML2::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::namedelement_is_not_abstract():
    assert not inspect.isabstract(UML2::NamedElement)


def test_uml2::namedelement_constructor_exists():
    assert callable(UML2::NamedElement.__init__)


def test_uml2::namedelement_constructor_args():
    sig = inspect.signature(UML2::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_uml2::namedelement_has_qualifiedName():
    assert hasattr(UML2::NamedElement, "qualifiedName")
    descriptor = None
    for klass in UML2::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_uml2::namedelement_has_visibility():
    assert hasattr(UML2::NamedElement, "visibility")
    descriptor = None
    for klass in UML2::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml2::namedelement_has_name():
    assert hasattr(UML2::NamedElement, "name")
    descriptor = None
    for klass in UML2::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2::relationship_is_not_abstract():
    assert not inspect.isabstract(UML2::Relationship)


def test_uml2::relationship_constructor_exists():
    assert callable(UML2::Relationship.__init__)


def test_uml2::relationship_constructor_args():
    sig = inspect.signature(UML2::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(UML2::QualifierValue)


def test_uml2::qualifiervalue_constructor_exists():
    assert callable(UML2::QualifierValue.__init__)


def test_uml2::qualifiervalue_constructor_args():
    sig = inspect.signature(UML2::QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2::linkenddata_is_not_abstract():
    assert not inspect.isabstract(UML2::LinkEndData)


def test_uml2::linkenddata_constructor_exists():
    assert callable(UML2::LinkEndData.__init__)


def test_uml2::linkenddata_constructor_args():
    sig = inspect.signature(UML2::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateSignature)


def test_uml2::templatesignature_constructor_exists():
    assert callable(UML2::TemplateSignature.__init__)


def test_uml2::templatesignature_constructor_args():
    sig = inspect.signature(UML2::TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::clause_is_not_abstract():
    assert not inspect.isabstract(UML2::Clause)


def test_uml2::clause_constructor_exists():
    assert callable(UML2::Clause.__init__)


def test_uml2::clause_constructor_args():
    sig = inspect.signature(UML2::Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterableElement)


def test_uml2::parameterableelement_constructor_exists():
    assert callable(UML2::ParameterableElement.__init__)


def test_uml2::parameterableelement_constructor_args():
    sig = inspect.signature(UML2::ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(UML2::ExceptionHandler)


def test_uml2::exceptionhandler_constructor_exists():
    assert callable(UML2::ExceptionHandler.__init__)


def test_uml2::exceptionhandler_constructor_args():
    sig = inspect.signature(UML2::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateParameterSubstitution)


def test_uml2::templateparametersubstitution_constructor_exists():
    assert callable(UML2::TemplateParameterSubstitution.__init__)


def test_uml2::templateparametersubstitution_constructor_args():
    sig = inspect.signature(UML2::TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templateableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateableElement)


def test_uml2::templateableelement_constructor_exists():
    assert callable(UML2::TemplateableElement.__init__)


def test_uml2::templateableelement_constructor_args():
    sig = inspect.signature(UML2::TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activitygroup_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityGroup)


def test_uml2::activitygroup_constructor_exists():
    assert callable(UML2::ActivityGroup.__init__)


def test_uml2::activitygroup_constructor_args():
    sig = inspect.signature(UML2::ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml2::slot_is_not_abstract():
    assert not inspect.isabstract(UML2::Slot)


def test_uml2::slot_constructor_exists():
    assert callable(UML2::Slot.__init__)


def test_uml2::slot_constructor_args():
    sig = inspect.signature(UML2::Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml2::templateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2::TemplateParameter)


def test_uml2::templateparameter_constructor_exists():
    assert callable(UML2::TemplateParameter.__init__)


def test_uml2::templateparameter_constructor_args():
    sig = inspect.signature(UML2::TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(UML2::MultiplicityElement)


def test_uml2::multiplicityelement_constructor_exists():
    assert callable(UML2::MultiplicityElement.__init__)


def test_uml2::multiplicityelement_constructor_args():
    sig = inspect.signature(UML2::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_uml2::multiplicityelement_has_lower():
    assert hasattr(UML2::MultiplicityElement, "lower")
    descriptor = None
    for klass in UML2::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml2::multiplicityelement_has_upper():
    assert hasattr(UML2::MultiplicityElement, "upper")
    descriptor = None
    for klass in UML2::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml2::multiplicityelement_has_isUnique():
    assert hasattr(UML2::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in UML2::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_uml2::multiplicityelement_has_isOrdered():
    assert hasattr(UML2::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in UML2::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



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
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_uml2::expression_has_symbol():
    assert hasattr(UML2::Expression, "symbol")
    descriptor = None
    for klass in UML2::Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::variable_is_not_abstract():
    assert not inspect.isabstract(UML2::Variable)


def test_uml2::variable_constructor_exists():
    assert callable(UML2::Variable.__init__)


def test_uml2::variable_constructor_args():
    sig = inspect.signature(UML2::Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2::objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2::ObjectNode)


def test_uml2::objectnode_constructor_exists():
    assert callable(UML2::ObjectNode.__init__)


def test_uml2::objectnode_constructor_args():
    sig = inspect.signature(UML2::ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_uml2::objectnode_has_ordering():
    assert hasattr(UML2::ObjectNode, "ordering")
    descriptor = None
    for klass in UML2::ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)



def test_uml2::operation_is_not_abstract():
    assert not inspect.isabstract(UML2::Operation)


def test_uml2::operation_constructor_exists():
    assert callable(UML2::Operation.__init__)


def test_uml2::operation_constructor_args():
    sig = inspect.signature(UML2::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_uml2::operation_has_isQuery():
    assert hasattr(UML2::Operation, "isQuery")
    descriptor = None
    for klass in UML2::Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_uml2::valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2::ValueSpecification)


def test_uml2::valuespecification_constructor_exists():
    assert callable(UML2::ValueSpecification.__init__)


def test_uml2::valuespecification_constructor_args():
    sig = inspect.signature(UML2::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeature)


def test_uml2::structuralfeature_constructor_exists():
    assert callable(UML2::StructuralFeature.__init__)


def test_uml2::structuralfeature_constructor_args():
    sig = inspect.signature(UML2::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml2::structuralfeature_has_isReadOnly():
    assert hasattr(UML2::StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in UML2::StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_uml2::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2::Behavior)


def test_uml2::behavior_constructor_exists():
    assert callable(UML2::Behavior.__init__)


def test_uml2::behavior_constructor_args():
    sig = inspect.signature(UML2::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_uml2::behavior_has_isReentrant():
    assert hasattr(UML2::Behavior, "isReentrant")
    descriptor = None
    for klass in UML2::Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_uml2::parameter_is_not_abstract():
    assert not inspect.isabstract(UML2::Parameter)


def test_uml2::parameter_constructor_exists():
    assert callable(UML2::Parameter.__init__)


def test_uml2::parameter_constructor_args():
    sig = inspect.signature(UML2::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "isStream" in params, "Missing parameter 'isStream'"

def test_uml2::parameter_has_default():
    assert hasattr(UML2::Parameter, "default")
    descriptor = None
    for klass in UML2::Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_uml2::parameter_has_effect():
    assert hasattr(UML2::Parameter, "effect")
    descriptor = None
    for klass in UML2::Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_uml2::parameter_has_direction():
    assert hasattr(UML2::Parameter, "direction")
    descriptor = None
    for klass in UML2::Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_uml2::parameter_has_isException():
    assert hasattr(UML2::Parameter, "isException")
    descriptor = None
    for klass in UML2::Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_uml2::parameter_has_isStream():
    assert hasattr(UML2::Parameter, "isStream")
    descriptor = None
    for klass in UML2::Parameter.__mro__:
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



def test_uml2::instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2::InstanceValue)


def test_uml2::instancevalue_constructor_exists():
    assert callable(UML2::InstanceValue.__init__)


def test_uml2::instancevalue_constructor_args():
    sig = inspect.signature(UML2::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2::literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2::LiteralSpecification)


def test_uml2::literalspecification_constructor_exists():
    assert callable(UML2::LiteralSpecification.__init__)


def test_uml2::literalspecification_constructor_args():
    sig = inspect.signature(UML2::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::CreateLinkObjectAction)


def test_uml2::createlinkobjectaction_constructor_exists():
    assert callable(UML2::CreateLinkObjectAction.__init__)


def test_uml2::createlinkobjectaction_constructor_args():
    sig = inspect.signature(UML2::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::OpaqueExpression)


def test_uml2::opaqueexpression_constructor_exists():
    assert callable(UML2::OpaqueExpression.__init__)


def test_uml2::opaqueexpression_constructor_args():
    sig = inspect.signature(UML2::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "bodies" in params, "Missing parameter 'bodies'"

def test_uml2::opaqueexpression_has_language():
    assert hasattr(UML2::OpaqueExpression, "language")
    descriptor = None
    for klass in UML2::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml2::opaqueexpression_has_bodies():
    assert hasattr(UML2::OpaqueExpression, "bodies")
    descriptor = None
    for klass in UML2::OpaqueExpression.__mro__:
        if "bodies" in klass.__dict__:
            descriptor = klass.__dict__["bodies"]
            break
    assert isinstance(descriptor, property)



def test_uml2::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkObjectEndQualifierAction)


def test_uml2::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UML2::ReadLinkObjectEndQualifierAction.__init__)


def test_uml2::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::packageimport_is_not_abstract():
    assert not inspect.isabstract(UML2::PackageImport)


def test_uml2::packageimport_constructor_exists():
    assert callable(UML2::PackageImport.__init__)


def test_uml2::packageimport_constructor_args():
    sig = inspect.signature(UML2::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml2::packageimport_has_visibility():
    assert hasattr(UML2::PackageImport, "visibility")
    descriptor = None
    for klass in UML2::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml2::elementimport_is_not_abstract():
    assert not inspect.isabstract(UML2::ElementImport)


def test_uml2::elementimport_constructor_exists():
    assert callable(UML2::ElementImport.__init__)


def test_uml2::elementimport_constructor_args():
    sig = inspect.signature(UML2::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_uml2::elementimport_has_visibility():
    assert hasattr(UML2::ElementImport, "visibility")
    descriptor = None
    for klass in UML2::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml2::elementimport_has_alias():
    assert hasattr(UML2::ElementImport, "alias")
    descriptor = None
    for klass in UML2::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UML2::RaiseExceptionAction)


def test_uml2::raiseexceptionaction_constructor_exists():
    assert callable(UML2::RaiseExceptionAction.__init__)


def test_uml2::raiseexceptionaction_constructor_args():
    sig = inspect.signature(UML2::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::replyaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReplyAction)


def test_uml2::replyaction_constructor_exists():
    assert callable(UML2::ReplyAction.__init__)


def test_uml2::replyaction_constructor_args():
    sig = inspect.signature(UML2::ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::constraint_is_not_abstract():
    assert not inspect.isabstract(UML2::Constraint)


def test_uml2::constraint_constructor_exists():
    assert callable(UML2::Constraint.__init__)


def test_uml2::constraint_constructor_args():
    sig = inspect.signature(UML2::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::message_is_not_abstract():
    assert not inspect.isabstract(UML2::Message)


def test_uml2::message_constructor_exists():
    assert callable(UML2::Message.__init__)


def test_uml2::message_constructor_args():
    sig = inspect.signature(UML2::Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageKind" in params, "Missing parameter 'messageKind'"
    assert "messageSort" in params, "Missing parameter 'messageSort'"

def test_uml2::message_has_messageKind():
    assert hasattr(UML2::Message, "messageKind")
    descriptor = None
    for klass in UML2::Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)

def test_uml2::message_has_messageSort():
    assert hasattr(UML2::Message, "messageSort")
    descriptor = None
    for klass in UML2::Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)



def test_uml2::activitypartition_is_not_abstract():
    assert not inspect.isabstract(UML2::ActivityPartition)


def test_uml2::activitypartition_constructor_exists():
    assert callable(UML2::ActivityPartition.__init__)


def test_uml2::activitypartition_constructor_args():
    sig = inspect.signature(UML2::ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "isDimension" in params, "Missing parameter 'isDimension'"

def test_uml2::activitypartition_has_isExternal():
    assert hasattr(UML2::ActivityPartition, "isExternal")
    descriptor = None
    for klass in UML2::ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_uml2::activitypartition_has_isDimension():
    assert hasattr(UML2::ActivityPartition, "isDimension")
    descriptor = None
    for klass in UML2::ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)



def test_uml2::generalordering_is_not_abstract():
    assert not inspect.isabstract(UML2::GeneralOrdering)


def test_uml2::generalordering_constructor_exists():
    assert callable(UML2::GeneralOrdering.__init__)


def test_uml2::generalordering_constructor_args():
    sig = inspect.signature(UML2::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterset_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterSet)


def test_uml2::parameterset_constructor_exists():
    assert callable(UML2::ParameterSet.__init__)


def test_uml2::parameterset_constructor_args():
    sig = inspect.signature(UML2::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml2::typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2::TypedElement)


def test_uml2::typedelement_constructor_exists():
    assert callable(UML2::TypedElement.__init__)


def test_uml2::typedelement_constructor_args():
    sig = inspect.signature(UML2::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::trigger_is_not_abstract():
    assert not inspect.isabstract(UML2::Trigger)


def test_uml2::trigger_constructor_exists():
    assert callable(UML2::Trigger.__init__)


def test_uml2::trigger_constructor_args():
    sig = inspect.signature(UML2::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(UML2::InteractionFragment)


def test_uml2::interactionfragment_constructor_exists():
    assert callable(UML2::InteractionFragment.__init__)


def test_uml2::interactionfragment_constructor_args():
    sig = inspect.signature(UML2::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::packageableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::PackageableElement)


def test_uml2::packageableelement_constructor_exists():
    assert callable(UML2::PackageableElement.__init__)


def test_uml2::packageableelement_constructor_args():
    sig = inspect.signature(UML2::PackageableElement.__init__)
    params = list(sig.parameters.keys())
    assert "packageableElement_visibility" in params, "Missing parameter 'packageableElement_visibility'"

def test_uml2::packageableelement_has_packageableElement_visibility():
    assert hasattr(UML2::PackageableElement, "packageableElement_visibility")
    descriptor = None
    for klass in UML2::PackageableElement.__mro__:
        if "packageableElement_visibility" in klass.__dict__:
            descriptor = klass.__dict__["packageableElement_visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml2::connectableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::ConnectableElement)


def test_uml2::connectableelement_constructor_exists():
    assert callable(UML2::ConnectableElement.__init__)


def test_uml2::connectableelement_constructor_args():
    sig = inspect.signature(UML2::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UML2::RedefinableElement)


def test_uml2::redefinableelement_constructor_exists():
    assert callable(UML2::RedefinableElement.__init__)


def test_uml2::redefinableelement_constructor_args():
    sig = inspect.signature(UML2::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_uml2::redefinableelement_has_isLeaf():
    assert hasattr(UML2::RedefinableElement, "isLeaf")
    descriptor = None
    for klass in UML2::RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_uml2::include_is_not_abstract():
    assert not inspect.isabstract(UML2::Include)


def test_uml2::include_constructor_exists():
    assert callable(UML2::Include.__init__)


def test_uml2::include_constructor_args():
    sig = inspect.signature(UML2::Include.__init__)
    params = list(sig.parameters.keys())



def test_uml2::collaborationoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2::CollaborationOccurrence)


def test_uml2::collaborationoccurrence_constructor_exists():
    assert callable(UML2::CollaborationOccurrence.__init__)


def test_uml2::collaborationoccurrence_constructor_args():
    sig = inspect.signature(UML2::CollaborationOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2::lifeline_is_not_abstract():
    assert not inspect.isabstract(UML2::Lifeline)


def test_uml2::lifeline_constructor_exists():
    assert callable(UML2::Lifeline.__init__)


def test_uml2::lifeline_constructor_args():
    sig = inspect.signature(UML2::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml2::messageend_is_not_abstract():
    assert not inspect.isabstract(UML2::MessageEnd)


def test_uml2::messageend_constructor_exists():
    assert callable(UML2::MessageEnd.__init__)


def test_uml2::messageend_constructor_args():
    sig = inspect.signature(UML2::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2::vertex_is_not_abstract():
    assert not inspect.isabstract(UML2::Vertex)


def test_uml2::vertex_constructor_exists():
    assert callable(UML2::Vertex.__init__)


def test_uml2::vertex_constructor_args():
    sig = inspect.signature(UML2::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extend_is_not_abstract():
    assert not inspect.isabstract(UML2::Extend)


def test_uml2::extend_constructor_exists():
    assert callable(UML2::Extend.__init__)


def test_uml2::extend_constructor_args():
    sig = inspect.signature(UML2::Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml2::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UML2::AcceptCallAction)


def test_uml2::acceptcallaction_constructor_exists():
    assert callable(UML2::AcceptCallAction.__init__)


def test_uml2::acceptcallaction_constructor_args():
    sig = inspect.signature(UML2::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadIsClassifiedObjectAction)


def test_uml2::readisclassifiedobjectaction_constructor_exists():
    assert callable(UML2::ReadIsClassifiedObjectAction.__init__)


def test_uml2::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UML2::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDirect" in params, "Missing parameter 'isDirect'"

def test_uml2::readisclassifiedobjectaction_has_isDirect():
    assert hasattr(UML2::ReadIsClassifiedObjectAction, "isDirect")
    descriptor = None
    for klass in UML2::ReadIsClassifiedObjectAction.__mro__:
        if "isDirect" in klass.__dict__:
            descriptor = klass.__dict__["isDirect"]
            break
    assert isinstance(descriptor, property)



def test_uml2::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReclassifyObjectAction)


def test_uml2::reclassifyobjectaction_constructor_exists():
    assert callable(UML2::ReclassifyObjectAction.__init__)


def test_uml2::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UML2::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_uml2::reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(UML2::ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in UML2::ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_uml2::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadLinkObjectEndAction)


def test_uml2::readlinkobjectendaction_constructor_exists():
    assert callable(UML2::ReadLinkObjectEndAction.__init__)


def test_uml2::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UML2::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::startownedbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2::StartOwnedBehaviorAction)


def test_uml2::startownedbehavioraction_constructor_exists():
    assert callable(UML2::StartOwnedBehaviorAction.__init__)


def test_uml2::startownedbehavioraction_constructor_args():
    sig = inspect.signature(UML2::StartOwnedBehaviorAction.__init__)
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



def test_uml2::protocolconformance_is_not_abstract():
    assert not inspect.isabstract(UML2::ProtocolConformance)


def test_uml2::protocolconformance_constructor_exists():
    assert callable(UML2::ProtocolConformance.__init__)


def test_uml2::protocolconformance_constructor_args():
    sig = inspect.signature(UML2::ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml2::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2::CommunicationPath)


def test_uml2::communicationpath_constructor_exists():
    assert callable(UML2::CommunicationPath.__init__)


def test_uml2::communicationpath_constructor_args():
    sig = inspect.signature(UML2::CommunicationPath.__init__)
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



def test_uml2::device_is_not_abstract():
    assert not inspect.isabstract(UML2::Device)


def test_uml2::device_constructor_exists():
    assert callable(UML2::Device.__init__)


def test_uml2::device_constructor_args():
    sig = inspect.signature(UML2::Device.__init__)
    params = list(sig.parameters.keys())



def test_uml2::readextentaction_is_not_abstract():
    assert not inspect.isabstract(UML2::ReadExtentAction)


def test_uml2::readextentaction_constructor_exists():
    assert callable(UML2::ReadExtentAction.__init__)


def test_uml2::readextentaction_constructor_args():
    sig = inspect.signature(UML2::ReadExtentAction.__init__)
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



def test_uml2::node_is_not_abstract():
    assert not inspect.isabstract(UML2::Node)


def test_uml2::node_constructor_exists():
    assert callable(UML2::Node.__init__)


def test_uml2::node_constructor_args():
    sig = inspect.signature(UML2::Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2::DeploymentSpecification)


def test_uml2::deploymentspecification_constructor_exists():
    assert callable(UML2::DeploymentSpecification.__init__)


def test_uml2::deploymentspecification_constructor_args():
    sig = inspect.signature(UML2::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"

def test_uml2::deploymentspecification_has_executionLocation():
    assert hasattr(UML2::DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in UML2::DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)

def test_uml2::deploymentspecification_has_deploymentLocation():
    assert hasattr(UML2::DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in UML2::DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)



def test_uml2::deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(UML2::DeploymentTarget)


def test_uml2::deploymenttarget_constructor_exists():
    assert callable(UML2::DeploymentTarget.__init__)


def test_uml2::deploymenttarget_constructor_args():
    sig = inspect.signature(UML2::DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deployedartifact_is_not_abstract():
    assert not inspect.isabstract(UML2::DeployedArtifact)


def test_uml2::deployedartifact_constructor_exists():
    assert callable(UML2::DeployedArtifact.__init__)


def test_uml2::deployedartifact_constructor_args():
    sig = inspect.signature(UML2::DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2::deployment_is_not_abstract():
    assert not inspect.isabstract(UML2::Deployment)


def test_uml2::deployment_constructor_exists():
    assert callable(UML2::Deployment.__init__)


def test_uml2::deployment_constructor_args():
    sig = inspect.signature(UML2::Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interval_is_not_abstract():
    assert not inspect.isabstract(UML2::Interval)


def test_uml2::interval_constructor_exists():
    assert callable(UML2::Interval.__init__)


def test_uml2::interval_constructor_args():
    sig = inspect.signature(UML2::Interval.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationInterval)


def test_uml2::durationinterval_constructor_exists():
    assert callable(UML2::DurationInterval.__init__)


def test_uml2::durationinterval_constructor_args():
    sig = inspect.signature(UML2::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeObservationAction)


def test_uml2::timeobservationaction_constructor_exists():
    assert callable(UML2::TimeObservationAction.__init__)


def test_uml2::timeobservationaction_constructor_args():
    sig = inspect.signature(UML2::TimeObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::duration_is_not_abstract():
    assert not inspect.isabstract(UML2::Duration)


def test_uml2::duration_constructor_exists():
    assert callable(UML2::Duration.__init__)


def test_uml2::duration_constructor_args():
    sig = inspect.signature(UML2::Duration.__init__)
    params = list(sig.parameters.keys())
    assert "firstTime" in params, "Missing parameter 'firstTime'"

def test_uml2::duration_has_firstTime():
    assert hasattr(UML2::Duration, "firstTime")
    descriptor = None
    for klass in UML2::Duration.__mro__:
        if "firstTime" in klass.__dict__:
            descriptor = klass.__dict__["firstTime"]
            break
    assert isinstance(descriptor, property)



def test_uml2::timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeExpression)


def test_uml2::timeexpression_constructor_exists():
    assert callable(UML2::TimeExpression.__init__)


def test_uml2::timeexpression_constructor_args():
    sig = inspect.signature(UML2::TimeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "firstTime" in params, "Missing parameter 'firstTime'"

def test_uml2::timeexpression_has_firstTime():
    assert hasattr(UML2::TimeExpression, "firstTime")
    descriptor = None
    for klass in UML2::TimeExpression.__mro__:
        if "firstTime" in klass.__dict__:
            descriptor = klass.__dict__["firstTime"]
            break
    assert isinstance(descriptor, property)



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



def test_uml2::durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationObservationAction)


def test_uml2::durationobservationaction_constructor_exists():
    assert callable(UML2::DurationObservationAction.__init__)


def test_uml2::durationobservationaction_constructor_args():
    sig = inspect.signature(UML2::DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeInterval)


def test_uml2::timeinterval_constructor_exists():
    assert callable(UML2::TimeInterval.__init__)


def test_uml2::timeinterval_constructor_args():
    sig = inspect.signature(UML2::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::IntervalConstraint)


def test_uml2::intervalconstraint_constructor_exists():
    assert callable(UML2::IntervalConstraint.__init__)


def test_uml2::intervalconstraint_constructor_args():
    sig = inspect.signature(UML2::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::DurationConstraint)


def test_uml2::durationconstraint_constructor_exists():
    assert callable(UML2::DurationConstraint.__init__)


def test_uml2::durationconstraint_constructor_args():
    sig = inspect.signature(UML2::DurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2::TimeConstraint)


def test_uml2::timeconstraint_constructor_exists():
    assert callable(UML2::TimeConstraint.__init__)


def test_uml2::timeconstraint_constructor_args():
    sig = inspect.signature(UML2::TimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2::SendSignalAction)


def test_uml2::sendsignalaction_constructor_exists():
    assert callable(UML2::SendSignalAction.__init__)


def test_uml2::sendsignalaction_constructor_args():
    sig = inspect.signature(UML2::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::invocationaction_is_not_abstract():
    assert not inspect.isabstract(UML2::InvocationAction)


def test_uml2::invocationaction_constructor_exists():
    assert callable(UML2::InvocationAction.__init__)


def test_uml2::invocationaction_constructor_args():
    sig = inspect.signature(UML2::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::namespace_is_not_abstract():
    assert not inspect.isabstract(UML2::Namespace)


def test_uml2::namespace_constructor_exists():
    assert callable(UML2::Namespace.__init__)


def test_uml2::namespace_constructor_args():
    sig = inspect.signature(UML2::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2::stringexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::StringExpression)


def test_uml2::stringexpression_constructor_exists():
    assert callable(UML2::StringExpression.__init__)


def test_uml2::stringexpression_constructor_args():
    sig = inspect.signature(UML2::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::comment_is_not_abstract():
    assert not inspect.isabstract(UML2::Comment)


def test_uml2::comment_constructor_exists():
    assert callable(UML2::Comment.__init__)


def test_uml2::comment_constructor_args():
    sig = inspect.signature(UML2::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uml2::comment_has_body():
    assert hasattr(UML2::Comment, "body")
    descriptor = None
    for klass in UML2::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uml2::element_is_not_abstract():
    assert not inspect.isabstract(UML2::Element)


def test_uml2::element_constructor_exists():
    assert callable(UML2::Element.__init__)


def test_uml2::element_constructor_args():
    sig = inspect.signature(UML2::Element.__init__)
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
        "lost",
        "found",
        "complete",
        "unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "join",
        "terminate",
        "exitPoint",
        "initial",
        "deepHistory",
        "choice",
        "fork",
        "shallowHistory",
        "entryPoint",
        "junction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "read",
        "delete",
        "create",
        "update",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "package",
        "public",
        "protected",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_interactionoperator_exists():
    # Check that the Enumeration exists
    assert InteractionOperator is not None

def test_interactionoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperator]
    expected_literals = [
        "alt",
        "consider",
        "critical",
        "ignore",
        "break_",
        "par",
        "assert_",
        "neg",
        "opt",
        "strict",
        "loop",
        "seq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperator"

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

def test_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "parallel",
        "iterative",
        "stream",
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
        "in_",
        "inout",
        "return_",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "FIFO",
        "LIFO",
        "ordered",
        "unordered",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "asynchCall",
        "asynchSignal",
        "synchSignal",
        "synchCall",
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
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
UML2::CallAction_strategy = st.builds(
    UML2::CallAction,
    isSynchronous=
        st.booleans()
)
CallAction_strategy = st.builds(
    CallAction,
)
UML2::CallBehaviorAction_strategy = st.builds(
    UML2::CallBehaviorAction,
)
UML2::CallOperationAction_strategy = st.builds(
    UML2::CallOperationAction,
)
UML2::SendObjectAction_strategy = st.builds(
    UML2::SendObjectAction,
)
UML2::BroadcastSignalAction_strategy = st.builds(
    UML2::BroadcastSignalAction,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
UML2::ReadVariableAction_strategy = st.builds(
    UML2::ReadVariableAction,
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
LinkEndData_strategy = st.builds(
    LinkEndData,
)
UML2::LinkEndCreationData_strategy = st.builds(
    UML2::LinkEndCreationData,
    isReplaceAll=
        st.booleans()
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UML2::RemoveVariableValueAction_strategy = st.builds(
    UML2::RemoveVariableValueAction,
)
UML2::AddVariableValueAction_strategy = st.builds(
    UML2::AddVariableValueAction,
    isReplaceAll=
        st.booleans()
)
UML2::ClearVariableAction_strategy = st.builds(
    UML2::ClearVariableAction,
)
UML2::WriteVariableAction_strategy = st.builds(
    UML2::WriteVariableAction,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UML2::ClearStructuralFeatureAction_strategy = st.builds(
    UML2::ClearStructuralFeatureAction,
)
UML2::WriteStructuralFeatureAction_strategy = st.builds(
    UML2::WriteStructuralFeatureAction,
)
UML2::ReadStructuralFeatureAction_strategy = st.builds(
    UML2::ReadStructuralFeatureAction,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UML2::WriteLinkAction_strategy = st.builds(
    UML2::WriteLinkAction,
)
UML2::ReadLinkAction_strategy = st.builds(
    UML2::ReadLinkAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UML2::AddStructuralFeatureValueAction_strategy = st.builds(
    UML2::AddStructuralFeatureValueAction,
    isReplaceAll=
        st.booleans()
)
UML2::RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2::RemoveStructuralFeatureValueAction,
)
State_strategy = st.builds(
    State,
)
UML2::FinalState_strategy = st.builds(
    UML2::FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
UML2::ConnectionPointReference_strategy = st.builds(
    UML2::ConnectionPointReference,
)
UML2::Pseudostate_strategy = st.builds(
    UML2::Pseudostate,
    kind=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
UML2::InteractionConstraint_strategy = st.builds(
    UML2::InteractionConstraint,
)
InteractionOccurrence_strategy = st.builds(
    InteractionOccurrence,
)
TemplateSignature_strategy = st.builds(
    TemplateSignature,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
UML2::ClassifierTemplateParameter_strategy = st.builds(
    UML2::ClassifierTemplateParameter,
    allowSubstitutable=
        st.booleans()
)
UML2::ConnectableElementTemplateParameter_strategy = st.builds(
    UML2::ConnectableElementTemplateParameter,
)
UML2::OperationTemplateParameter_strategy = st.builds(
    UML2::OperationTemplateParameter,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
UML2::Stop_strategy = st.builds(
    UML2::Stop,
)
UML2::PartDecomposition_strategy = st.builds(
    UML2::PartDecomposition,
)
UML2::Gate_strategy = st.builds(
    UML2::Gate,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
UML2::CombinedFragment_strategy = st.builds(
    UML2::CombinedFragment,
    interactionOperator=
        safe_text
)
UML2::InteractionOccurrence_strategy = st.builds(
    UML2::InteractionOccurrence,
)
UML2::EventOccurrence_strategy = st.builds(
    UML2::EventOccurrence,
)
UML2::ExecutionOccurrence_strategy = st.builds(
    UML2::ExecutionOccurrence,
)
UML2::Continuation_strategy = st.builds(
    UML2::Continuation,
    setting=
        st.booleans()
)
UML2::StateInvariant_strategy = st.builds(
    UML2::StateInvariant,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
UML2::LoopNode_strategy = st.builds(
    UML2::LoopNode,
    isTestedFirst=
        st.booleans()
)
UML2::ExpansionRegion_strategy = st.builds(
    UML2::ExpansionRegion,
    mode=
        safe_text
)
UML2::ConditionalNode_strategy = st.builds(
    UML2::ConditionalNode,
    isAssured=
        st.booleans(),
    isDeterminate=
        st.booleans()
)
Trigger_strategy = st.builds(
    Trigger,
)
UML2::ChangeTrigger_strategy = st.builds(
    UML2::ChangeTrigger,
)
UML2::MessageTrigger_strategy = st.builds(
    UML2::MessageTrigger,
)
MessageTrigger_strategy = st.builds(
    MessageTrigger,
)
UML2::CallTrigger_strategy = st.builds(
    UML2::CallTrigger,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
Action_strategy = st.builds(
    Action,
)
UML2::LinkAction_strategy = st.builds(
    UML2::LinkAction,
)
UML2::CreateObjectAction_strategy = st.builds(
    UML2::CreateObjectAction,
)
UML2::ReadSelfAction_strategy = st.builds(
    UML2::ReadSelfAction,
)
UML2::ClearAssociationAction_strategy = st.builds(
    UML2::ClearAssociationAction,
)
UML2::ApplyFunctionAction_strategy = st.builds(
    UML2::ApplyFunctionAction,
)
UML2::StructuralFeatureAction_strategy = st.builds(
    UML2::StructuralFeatureAction,
)
UML2::DestroyObjectAction_strategy = st.builds(
    UML2::DestroyObjectAction,
    isDestroyOwnedObjects=
        st.booleans(),
    isDestroyLinks=
        st.booleans()
)
UML2::VariableAction_strategy = st.builds(
    UML2::VariableAction,
)
UML2::TestIdentityAction_strategy = st.builds(
    UML2::TestIdentityAction,
)
UML2::AcceptEventAction_strategy = st.builds(
    UML2::AcceptEventAction,
)
UML2::AnyTrigger_strategy = st.builds(
    UML2::AnyTrigger,
)
UML2::TimeTrigger_strategy = st.builds(
    UML2::TimeTrigger,
    isRelative=
        st.booleans()
)
UML2::SignalTrigger_strategy = st.builds(
    UML2::SignalTrigger,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UML2::EncapsulatedClassifier_strategy = st.builds(
    UML2::EncapsulatedClassifier,
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2::ValuePin_strategy = st.builds(
    UML2::ValuePin,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UML2::ActivityParameterNode_strategy = st.builds(
    UML2::ActivityParameterNode,
)
UML2::ExpansionNode_strategy = st.builds(
    UML2::ExpansionNode,
)
UML2::CentralBufferNode_strategy = st.builds(
    UML2::CentralBufferNode,
)
Pin_strategy = st.builds(
    Pin,
)
UML2::InputPin_strategy = st.builds(
    UML2::InputPin,
)
UML2::ExecutableNode_strategy = st.builds(
    UML2::ExecutableNode,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
UML2::FlowFinalNode_strategy = st.builds(
    UML2::FlowFinalNode,
)
UML2::ActivityFinalNode_strategy = st.builds(
    UML2::ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
UML2::DecisionNode_strategy = st.builds(
    UML2::DecisionNode,
)
UML2::MergeNode_strategy = st.builds(
    UML2::MergeNode,
)
UML2::JoinNode_strategy = st.builds(
    UML2::JoinNode,
    isCombineDuplicate=
        st.booleans()
)
UML2::FinalNode_strategy = st.builds(
    UML2::FinalNode,
)
UML2::ForkNode_strategy = st.builds(
    UML2::ForkNode,
)
UML2::InitialNode_strategy = st.builds(
    UML2::InitialNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
UML2::ObjectFlow_strategy = st.builds(
    UML2::ObjectFlow,
    isMultireceive=
        st.booleans(),
    isMulticast=
        st.booleans()
)
UML2::ControlFlow_strategy = st.builds(
    UML2::ControlFlow,
)
UML2::ControlNode_strategy = st.builds(
    UML2::ControlNode,
)
UML2::OutputPin_strategy = st.builds(
    UML2::OutputPin,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
UML2::InterruptibleActivityRegion_strategy = st.builds(
    UML2::InterruptibleActivityRegion,
)
UML2::Action_strategy = st.builds(
    UML2::Action,
    effect=
        safe_text
)
Realization_strategy = st.builds(
    Realization,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
UML2::Manifestation_strategy = st.builds(
    UML2::Manifestation,
)
UML2::Realization_strategy = st.builds(
    UML2::Realization,
)
Dependency_strategy = st.builds(
    Dependency,
)
UML2::Usage_strategy = st.builds(
    UML2::Usage,
)
UML2::Abstraction_strategy = st.builds(
    UML2::Abstraction,
)
UML2::Permission_strategy = st.builds(
    UML2::Permission,
)
Property_strategy = st.builds(
    Property,
)
UML2::Port_strategy = st.builds(
    UML2::Port,
    isBehavior=
        st.booleans(),
    isService=
        st.booleans()
)
UML2::ExtensionEnd_strategy = st.builds(
    UML2::ExtensionEnd,
)
Association_strategy = st.builds(
    Association,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2::Interaction_strategy = st.builds(
    UML2::Interaction,
)
UML2::Activity_strategy = st.builds(
    UML2::Activity,
    body=
        safe_text,
    isSingleExecution=
        st.booleans(),
    language=
        safe_text,
    isReadOnly=
        st.booleans()
)
UML2::StateMachine_strategy = st.builds(
    UML2::StateMachine,
)
UML2::Implementation_strategy = st.builds(
    UML2::Implementation,
)
PackageImport_strategy = st.builds(
    PackageImport,
)
Package_strategy = st.builds(
    Package,
)
UML2::Model_strategy = st.builds(
    UML2::Model,
    viewpoint=
        safe_text
)
UML2::Profile_strategy = st.builds(
    UML2::Profile,
)
Class_strategy = st.builds(
    Class,
)
UML2::AssociationClass_strategy = st.builds(
    UML2::AssociationClass,
)
UML2::Component_strategy = st.builds(
    UML2::Component,
    isIndirectlyInstantiated=
        st.booleans()
)
UML2::Stereotype_strategy = st.builds(
    UML2::Stereotype,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
UML2::TemplateBinding_strategy = st.builds(
    UML2::TemplateBinding,
)
Feature_strategy = st.builds(
    Feature,
)
UML2::Connector_strategy = st.builds(
    UML2::Connector,
    kind=
        safe_text
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UML2::LiteralInteger_strategy = st.builds(
    UML2::LiteralInteger,
    value=
        st.integers()
)
UML2::LiteralString_strategy = st.builds(
    UML2::LiteralString,
    value=
        safe_text
)
UML2::LiteralUnlimitedNatural_strategy = st.builds(
    UML2::LiteralUnlimitedNatural,
    value=
        safe_text
)
UML2::LiteralNull_strategy = st.builds(
    UML2::LiteralNull,
)
UML2::LiteralBoolean_strategy = st.builds(
    UML2::LiteralBoolean,
    value=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2::StructuredClassifier_strategy = st.builds(
    UML2::StructuredClassifier,
)
UML2::TemplateableClassifier_strategy = st.builds(
    UML2::TemplateableClassifier,
)
UML2::Artifact_strategy = st.builds(
    UML2::Artifact,
    fileName=
        safe_text
)
UML2::BehavioredClassifier_strategy = st.builds(
    UML2::BehavioredClassifier,
)
UML2::InformationItem_strategy = st.builds(
    UML2::InformationItem,
)
UML2::Actor_strategy = st.builds(
    UML2::Actor,
)
UML2::Signal_strategy = st.builds(
    UML2::Signal,
)
UML2::Interface_strategy = st.builds(
    UML2::Interface,
)
UML2::ParameterableClassifier_strategy = st.builds(
    UML2::ParameterableClassifier,
)
DataType_strategy = st.builds(
    DataType,
)
UML2::Enumeration_strategy = st.builds(
    UML2::Enumeration,
)
UML2::ProfileApplication_strategy = st.builds(
    UML2::ProfileApplication,
)
UML2::PackageMerge_strategy = st.builds(
    UML2::PackageMerge,
)
UML2::Substitution_strategy = st.builds(
    UML2::Substitution,
)
UML2::Generalization_strategy = st.builds(
    UML2::Generalization,
    isSubstitutable=
        st.booleans()
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
UML2::ActivityNode_strategy = st.builds(
    UML2::ActivityNode,
)
UML2::RedefinableTemplateSignature_strategy = st.builds(
    UML2::RedefinableTemplateSignature,
)
UML2::Feature_strategy = st.builds(
    UML2::Feature,
    isStatic=
        st.booleans()
)
UML2::Transition_strategy = st.builds(
    UML2::Transition,
    kind=
        safe_text
)
UML2::ActivityEdge_strategy = st.builds(
    UML2::ActivityEdge,
)
UML2::ExtensionPoint_strategy = st.builds(
    UML2::ExtensionPoint,
)
Type_strategy = st.builds(
    Type,
)
UML2::PrimitiveType_strategy = st.builds(
    UML2::PrimitiveType,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
UML2::EnumerationLiteral_strategy = st.builds(
    UML2::EnumerationLiteral,
)
Namespace_strategy = st.builds(
    Namespace,
)
UML2::State_strategy = st.builds(
    UML2::State,
    isComposite=
        st.booleans(),
    isSubmachineState=
        st.booleans(),
    isSimple=
        st.booleans(),
    isOrthogonal=
        st.booleans()
)
UML2::Region_strategy = st.builds(
    UML2::Region,
)
UML2::InteractionOperand_strategy = st.builds(
    UML2::InteractionOperand,
)
UML2::BehavioralFeature_strategy = st.builds(
    UML2::BehavioralFeature,
    isAbstract=
        st.booleans(),
    concurrency=
        safe_text
)
UML2::StructuredActivityNode_strategy = st.builds(
    UML2::StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2::Property_strategy = st.builds(
    UML2::Property,
    isComposite=
        st.booleans(),
    isDerivedUnion=
        st.booleans(),
    aggregation=
        safe_text,
    default=
        safe_text,
    isDerived=
        st.booleans()
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
UML2::GeneralizationSet_strategy = st.builds(
    UML2::GeneralizationSet,
    isCovering=
        st.booleans(),
    isDisjoint=
        st.booleans()
)
UML2::InformationFlow_strategy = st.builds(
    UML2::InformationFlow,
)
UML2::PrimitiveFunction_strategy = st.builds(
    UML2::PrimitiveFunction,
    body=
        safe_text,
    language=
        safe_text
)
UML2::Package_strategy = st.builds(
    UML2::Package,
)
UML2::InstanceSpecification_strategy = st.builds(
    UML2::InstanceSpecification,
)
UML2::Type_strategy = st.builds(
    UML2::Type,
)
UML2::Classifier_strategy = st.builds(
    UML2::Classifier,
    isAbstract=
        st.booleans()
)
UML2::Extension_strategy = st.builds(
    UML2::Extension,
    isRequired=
        st.booleans()
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
UML2::ConnectorEnd_strategy = st.builds(
    UML2::ConnectorEnd,
)
UML2::Pin_strategy = st.builds(
    UML2::Pin,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
UML2::Reception_strategy = st.builds(
    UML2::Reception,
)
UML2::DataType_strategy = st.builds(
    UML2::DataType,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UML2::Collaboration_strategy = st.builds(
    UML2::Collaboration,
)
UML2::UseCase_strategy = st.builds(
    UML2::UseCase,
)
UML2::Class_strategy = st.builds(
    UML2::Class,
    isActive=
        st.booleans()
)
Relationship_strategy = st.builds(
    Relationship,
)
UML2::Association_strategy = st.builds(
    UML2::Association,
    isDerived=
        st.booleans()
)
UML2::DirectedRelationship_strategy = st.builds(
    UML2::DirectedRelationship,
)
UML2::Dependency_strategy = st.builds(
    UML2::Dependency,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
UML2::NamedElement_strategy = st.builds(
    UML2::NamedElement,
    qualifiedName=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
UML2::Relationship_strategy = st.builds(
    UML2::Relationship,
)
UML2::QualifierValue_strategy = st.builds(
    UML2::QualifierValue,
)
UML2::LinkEndData_strategy = st.builds(
    UML2::LinkEndData,
)
UML2::TemplateSignature_strategy = st.builds(
    UML2::TemplateSignature,
)
UML2::Clause_strategy = st.builds(
    UML2::Clause,
)
UML2::ParameterableElement_strategy = st.builds(
    UML2::ParameterableElement,
)
UML2::ExceptionHandler_strategy = st.builds(
    UML2::ExceptionHandler,
)
UML2::TemplateParameterSubstitution_strategy = st.builds(
    UML2::TemplateParameterSubstitution,
)
UML2::TemplateableElement_strategy = st.builds(
    UML2::TemplateableElement,
)
UML2::ActivityGroup_strategy = st.builds(
    UML2::ActivityGroup,
)
UML2::Slot_strategy = st.builds(
    UML2::Slot,
)
UML2::TemplateParameter_strategy = st.builds(
    UML2::TemplateParameter,
)
UML2::MultiplicityElement_strategy = st.builds(
    UML2::MultiplicityElement,
    lower=
        st.integers(),
    upper=
        safe_text,
    isUnique=
        st.booleans(),
    isOrdered=
        st.booleans()
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
UML2::Expression_strategy = st.builds(
    UML2::Expression,
    symbol=
        safe_text
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
UML2::Variable_strategy = st.builds(
    UML2::Variable,
)
UML2::ObjectNode_strategy = st.builds(
    UML2::ObjectNode,
    ordering=
        safe_text
)
UML2::Operation_strategy = st.builds(
    UML2::Operation,
    isQuery=
        st.booleans()
)
UML2::ValueSpecification_strategy = st.builds(
    UML2::ValueSpecification,
)
UML2::StructuralFeature_strategy = st.builds(
    UML2::StructuralFeature,
    isReadOnly=
        st.booleans()
)
UML2::Behavior_strategy = st.builds(
    UML2::Behavior,
    isReentrant=
        st.booleans()
)
UML2::Parameter_strategy = st.builds(
    UML2::Parameter,
    default=
        safe_text,
    effect=
        safe_text,
    direction=
        safe_text,
    isException=
        st.booleans(),
    isStream=
        st.booleans()
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UML2::InstanceValue_strategy = st.builds(
    UML2::InstanceValue,
)
UML2::LiteralSpecification_strategy = st.builds(
    UML2::LiteralSpecification,
)
UML2::CreateLinkObjectAction_strategy = st.builds(
    UML2::CreateLinkObjectAction,
)
UML2::OpaqueExpression_strategy = st.builds(
    UML2::OpaqueExpression,
    language=
        safe_text,
    bodies=
        safe_text
)
UML2::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UML2::ReadLinkObjectEndQualifierAction,
)
UML2::PackageImport_strategy = st.builds(
    UML2::PackageImport,
    visibility=
        safe_text
)
UML2::ElementImport_strategy = st.builds(
    UML2::ElementImport,
    visibility=
        safe_text,
    alias=
        safe_text
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2::RaiseExceptionAction_strategy = st.builds(
    UML2::RaiseExceptionAction,
)
UML2::ReplyAction_strategy = st.builds(
    UML2::ReplyAction,
)
UML2::Constraint_strategy = st.builds(
    UML2::Constraint,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
UML2::Message_strategy = st.builds(
    UML2::Message,
    messageKind=
        safe_text,
    messageSort=
        safe_text
)
UML2::ActivityPartition_strategy = st.builds(
    UML2::ActivityPartition,
    isExternal=
        st.booleans(),
    isDimension=
        st.booleans()
)
UML2::GeneralOrdering_strategy = st.builds(
    UML2::GeneralOrdering,
)
UML2::ParameterSet_strategy = st.builds(
    UML2::ParameterSet,
)
UML2::TypedElement_strategy = st.builds(
    UML2::TypedElement,
)
UML2::Trigger_strategy = st.builds(
    UML2::Trigger,
)
UML2::InteractionFragment_strategy = st.builds(
    UML2::InteractionFragment,
)
UML2::PackageableElement_strategy = st.builds(
    UML2::PackageableElement,
    packageableElement_visibility=
        safe_text
)
UML2::ConnectableElement_strategy = st.builds(
    UML2::ConnectableElement,
)
UML2::RedefinableElement_strategy = st.builds(
    UML2::RedefinableElement,
    isLeaf=
        st.booleans()
)
UML2::Include_strategy = st.builds(
    UML2::Include,
)
UML2::CollaborationOccurrence_strategy = st.builds(
    UML2::CollaborationOccurrence,
)
UML2::Lifeline_strategy = st.builds(
    UML2::Lifeline,
)
UML2::MessageEnd_strategy = st.builds(
    UML2::MessageEnd,
)
UML2::Vertex_strategy = st.builds(
    UML2::Vertex,
)
UML2::Extend_strategy = st.builds(
    UML2::Extend,
)
UML2::AcceptCallAction_strategy = st.builds(
    UML2::AcceptCallAction,
)
UML2::ReadIsClassifiedObjectAction_strategy = st.builds(
    UML2::ReadIsClassifiedObjectAction,
    isDirect=
        st.booleans()
)
UML2::ReclassifyObjectAction_strategy = st.builds(
    UML2::ReclassifyObjectAction,
    isReplaceAll=
        st.booleans()
)
UML2::ReadLinkObjectEndAction_strategy = st.builds(
    UML2::ReadLinkObjectEndAction,
)
UML2::StartOwnedBehaviorAction_strategy = st.builds(
    UML2::StartOwnedBehaviorAction,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2::ProtocolStateMachine_strategy = st.builds(
    UML2::ProtocolStateMachine,
)
UML2::ProtocolConformance_strategy = st.builds(
    UML2::ProtocolConformance,
)
UML2::CommunicationPath_strategy = st.builds(
    UML2::CommunicationPath,
)
Node_strategy = st.builds(
    Node,
)
UML2::ExecutionEnvironment_strategy = st.builds(
    UML2::ExecutionEnvironment,
)
UML2::Device_strategy = st.builds(
    UML2::Device,
)
UML2::ReadExtentAction_strategy = st.builds(
    UML2::ReadExtentAction,
)
Transition_strategy = st.builds(
    Transition,
)
UML2::ProtocolTransition_strategy = st.builds(
    UML2::ProtocolTransition,
)
UML2::Node_strategy = st.builds(
    UML2::Node,
)
UML2::DeploymentSpecification_strategy = st.builds(
    UML2::DeploymentSpecification,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text
)
UML2::DeploymentTarget_strategy = st.builds(
    UML2::DeploymentTarget,
)
UML2::DeployedArtifact_strategy = st.builds(
    UML2::DeployedArtifact,
)
UML2::Deployment_strategy = st.builds(
    UML2::Deployment,
)
UML2::Interval_strategy = st.builds(
    UML2::Interval,
)
Interval_strategy = st.builds(
    Interval,
)
UML2::DurationInterval_strategy = st.builds(
    UML2::DurationInterval,
)
UML2::TimeObservationAction_strategy = st.builds(
    UML2::TimeObservationAction,
)
UML2::Duration_strategy = st.builds(
    UML2::Duration,
    firstTime=
        st.booleans()
)
UML2::TimeExpression_strategy = st.builds(
    UML2::TimeExpression,
    firstTime=
        st.booleans()
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UML2::DataStoreNode_strategy = st.builds(
    UML2::DataStoreNode,
)
UML2::DurationObservationAction_strategy = st.builds(
    UML2::DurationObservationAction,
)
UML2::TimeInterval_strategy = st.builds(
    UML2::TimeInterval,
)
UML2::IntervalConstraint_strategy = st.builds(
    UML2::IntervalConstraint,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
UML2::DurationConstraint_strategy = st.builds(
    UML2::DurationConstraint,
)
UML2::TimeConstraint_strategy = st.builds(
    UML2::TimeConstraint,
)
UML2::SendSignalAction_strategy = st.builds(
    UML2::SendSignalAction,
)
UML2::InvocationAction_strategy = st.builds(
    UML2::InvocationAction,
)
UML2::Namespace_strategy = st.builds(
    UML2::Namespace,
)
UML2::StringExpression_strategy = st.builds(
    UML2::StringExpression,
)
UML2::Comment_strategy = st.builds(
    UML2::Comment,
    body=
        safe_text
)
UML2::Element_strategy = st.builds(
    UML2::Element,
)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=UML2::CallAction_strategy)
@settings(max_examples=50)
def test_uml2::callaction_instantiation(instance):
    assert isinstance(instance, UML2::CallAction)

@given(instance=UML2::CallAction_strategy)
def test_uml2::callaction_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, bool)


@given(instance=UML2::CallAction_strategy)
def test_uml2::callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=UML2::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2::callbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2::CallBehaviorAction)

@given(instance=UML2::CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml2::calloperationaction_instantiation(instance):
    assert isinstance(instance, UML2::CallOperationAction)

@given(instance=UML2::SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::sendobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::SendObjectAction)

@given(instance=UML2::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml2::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UML2::BroadcastSignalAction)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=UML2::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::readvariableaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadVariableAction)

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

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=UML2::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml2::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, UML2::LinkEndCreationData)

@given(instance=UML2::LinkEndCreationData_strategy)
def test_uml2::linkendcreationdata_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=UML2::LinkEndCreationData_strategy)
def test_uml2::linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UML2::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::RemoveVariableValueAction)

@given(instance=UML2::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::AddVariableValueAction)

@given(instance=UML2::AddVariableValueAction_strategy)
def test_uml2::addvariablevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=UML2::AddVariableValueAction_strategy)
def test_uml2::addvariablevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=UML2::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::clearvariableaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearVariableAction)

@given(instance=UML2::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml2::writevariableaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteVariableAction)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UML2::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearStructuralFeatureAction)

@given(instance=UML2::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteStructuralFeatureAction)

@given(instance=UML2::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadStructuralFeatureAction)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UML2::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::writelinkaction_instantiation(instance):
    assert isinstance(instance, UML2::WriteLinkAction)

@given(instance=UML2::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkAction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UML2::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::AddStructuralFeatureValueAction)

@given(instance=UML2::AddStructuralFeatureValueAction_strategy)
def test_uml2::addstructuralfeaturevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=UML2::AddStructuralFeatureValueAction_strategy)
def test_uml2::addstructuralfeaturevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=UML2::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2::RemoveStructuralFeatureValueAction)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UML2::FinalState_strategy)
@settings(max_examples=50)
def test_uml2::finalstate_instantiation(instance):
    assert isinstance(instance, UML2::FinalState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=UML2::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml2::connectionpointreference_instantiation(instance):
    assert isinstance(instance, UML2::ConnectionPointReference)

@given(instance=UML2::Pseudostate_strategy)
@settings(max_examples=50)
def test_uml2::pseudostate_instantiation(instance):
    assert isinstance(instance, UML2::Pseudostate)

@given(instance=UML2::Pseudostate_strategy)
def test_uml2::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UML2::Pseudostate_strategy)
def test_uml2::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UML2::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml2::interactionconstraint_instantiation(instance):
    assert isinstance(instance, UML2::InteractionConstraint)

@given(instance=InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_interactionoccurrence_instantiation(instance):
    assert isinstance(instance, InteractionOccurrence)

@given(instance=TemplateSignature_strategy)
@settings(max_examples=50)
def test_templatesignature_instantiation(instance):
    assert isinstance(instance, TemplateSignature)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=UML2::ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2::classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2::ClassifierTemplateParameter)

@given(instance=UML2::ClassifierTemplateParameter_strategy)
def test_uml2::classifiertemplateparameter_allowSubstitutable_type(instance):
    assert isinstance(instance.allowSubstitutable, bool)


@given(instance=UML2::ClassifierTemplateParameter_strategy)
def test_uml2::classifiertemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=UML2::ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2::connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2::ConnectableElementTemplateParameter)

@given(instance=UML2::OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2::operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2::OperationTemplateParameter)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=UML2::Stop_strategy)
@settings(max_examples=50)
def test_uml2::stop_instantiation(instance):
    assert isinstance(instance, UML2::Stop)

@given(instance=UML2::PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml2::partdecomposition_instantiation(instance):
    assert isinstance(instance, UML2::PartDecomposition)

@given(instance=UML2::Gate_strategy)
@settings(max_examples=50)
def test_uml2::gate_instantiation(instance):
    assert isinstance(instance, UML2::Gate)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=UML2::CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml2::combinedfragment_instantiation(instance):
    assert isinstance(instance, UML2::CombinedFragment)

@given(instance=UML2::CombinedFragment_strategy)
def test_uml2::combinedfragment_interactionOperator_type(instance):
    assert isinstance(instance.interactionOperator, str)


@given(instance=UML2::CombinedFragment_strategy)
def test_uml2::combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=UML2::InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::interactionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::InteractionOccurrence)

@given(instance=UML2::EventOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::eventoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::EventOccurrence)

@given(instance=UML2::ExecutionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::executionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::ExecutionOccurrence)

@given(instance=UML2::Continuation_strategy)
@settings(max_examples=50)
def test_uml2::continuation_instantiation(instance):
    assert isinstance(instance, UML2::Continuation)

@given(instance=UML2::Continuation_strategy)
def test_uml2::continuation_setting_type(instance):
    assert isinstance(instance.setting, bool)


@given(instance=UML2::Continuation_strategy)
def test_uml2::continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=UML2::StateInvariant_strategy)
@settings(max_examples=50)
def test_uml2::stateinvariant_instantiation(instance):
    assert isinstance(instance, UML2::StateInvariant)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=UML2::LoopNode_strategy)
@settings(max_examples=50)
def test_uml2::loopnode_instantiation(instance):
    assert isinstance(instance, UML2::LoopNode)

@given(instance=UML2::LoopNode_strategy)
def test_uml2::loopnode_isTestedFirst_type(instance):
    assert isinstance(instance.isTestedFirst, bool)


@given(instance=UML2::LoopNode_strategy)
def test_uml2::loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=UML2::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml2::expansionregion_instantiation(instance):
    assert isinstance(instance, UML2::ExpansionRegion)

@given(instance=UML2::ExpansionRegion_strategy)
def test_uml2::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=UML2::ExpansionRegion_strategy)
def test_uml2::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=UML2::ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml2::conditionalnode_instantiation(instance):
    assert isinstance(instance, UML2::ConditionalNode)

@given(instance=UML2::ConditionalNode_strategy)
def test_uml2::conditionalnode_isAssured_type(instance):
    assert isinstance(instance.isAssured, bool)


@given(instance=UML2::ConditionalNode_strategy)
def test_uml2::conditionalnode_isAssured_setter(instance):
    original = instance.isAssured
    instance.isAssured = original
    assert instance.isAssured == original

@given(instance=UML2::ConditionalNode_strategy)
def test_uml2::conditionalnode_isDeterminate_type(instance):
    assert isinstance(instance.isDeterminate, bool)


@given(instance=UML2::ConditionalNode_strategy)
def test_uml2::conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=UML2::ChangeTrigger_strategy)
@settings(max_examples=50)
def test_uml2::changetrigger_instantiation(instance):
    assert isinstance(instance, UML2::ChangeTrigger)

@given(instance=UML2::MessageTrigger_strategy)
@settings(max_examples=50)
def test_uml2::messagetrigger_instantiation(instance):
    assert isinstance(instance, UML2::MessageTrigger)

@given(instance=MessageTrigger_strategy)
@settings(max_examples=50)
def test_messagetrigger_instantiation(instance):
    assert isinstance(instance, MessageTrigger)

@given(instance=UML2::CallTrigger_strategy)
@settings(max_examples=50)
def test_uml2::calltrigger_instantiation(instance):
    assert isinstance(instance, UML2::CallTrigger)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UML2::LinkAction_strategy)
@settings(max_examples=50)
def test_uml2::linkaction_instantiation(instance):
    assert isinstance(instance, UML2::LinkAction)

@given(instance=UML2::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::createobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateObjectAction)

@given(instance=UML2::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml2::readselfaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadSelfAction)

@given(instance=UML2::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml2::clearassociationaction_instantiation(instance):
    assert isinstance(instance, UML2::ClearAssociationAction)

@given(instance=UML2::ApplyFunctionAction_strategy)
@settings(max_examples=50)
def test_uml2::applyfunctionaction_instantiation(instance):
    assert isinstance(instance, UML2::ApplyFunctionAction)

@given(instance=UML2::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeatureAction)

@given(instance=UML2::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::DestroyObjectAction)

@given(instance=UML2::DestroyObjectAction_strategy)
def test_uml2::destroyobjectaction_isDestroyOwnedObjects_type(instance):
    assert isinstance(instance.isDestroyOwnedObjects, bool)


@given(instance=UML2::DestroyObjectAction_strategy)
def test_uml2::destroyobjectaction_isDestroyOwnedObjects_setter(instance):
    original = instance.isDestroyOwnedObjects
    instance.isDestroyOwnedObjects = original
    assert instance.isDestroyOwnedObjects == original

@given(instance=UML2::DestroyObjectAction_strategy)
def test_uml2::destroyobjectaction_isDestroyLinks_type(instance):
    assert isinstance(instance.isDestroyLinks, bool)


@given(instance=UML2::DestroyObjectAction_strategy)
def test_uml2::destroyobjectaction_isDestroyLinks_setter(instance):
    original = instance.isDestroyLinks
    instance.isDestroyLinks = original
    assert instance.isDestroyLinks == original

@given(instance=UML2::VariableAction_strategy)
@settings(max_examples=50)
def test_uml2::variableaction_instantiation(instance):
    assert isinstance(instance, UML2::VariableAction)

@given(instance=UML2::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2::testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2::TestIdentityAction)

@given(instance=UML2::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml2::accepteventaction_instantiation(instance):
    assert isinstance(instance, UML2::AcceptEventAction)

@given(instance=UML2::AnyTrigger_strategy)
@settings(max_examples=50)
def test_uml2::anytrigger_instantiation(instance):
    assert isinstance(instance, UML2::AnyTrigger)

@given(instance=UML2::TimeTrigger_strategy)
@settings(max_examples=50)
def test_uml2::timetrigger_instantiation(instance):
    assert isinstance(instance, UML2::TimeTrigger)

@given(instance=UML2::TimeTrigger_strategy)
def test_uml2::timetrigger_isRelative_type(instance):
    assert isinstance(instance.isRelative, bool)


@given(instance=UML2::TimeTrigger_strategy)
def test_uml2::timetrigger_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=UML2::SignalTrigger_strategy)
@settings(max_examples=50)
def test_uml2::signaltrigger_instantiation(instance):
    assert isinstance(instance, UML2::SignalTrigger)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UML2::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2::EncapsulatedClassifier)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2::ValuePin_strategy)
@settings(max_examples=50)
def test_uml2::valuepin_instantiation(instance):
    assert isinstance(instance, UML2::ValuePin)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UML2::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2::activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2::ActivityParameterNode)

@given(instance=UML2::ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2::expansionnode_instantiation(instance):
    assert isinstance(instance, UML2::ExpansionNode)

@given(instance=UML2::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2::centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2::CentralBufferNode)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=UML2::InputPin_strategy)
@settings(max_examples=50)
def test_uml2::inputpin_instantiation(instance):
    assert isinstance(instance, UML2::InputPin)

@given(instance=UML2::ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml2::executablenode_instantiation(instance):
    assert isinstance(instance, UML2::ExecutableNode)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=UML2::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml2::flowfinalnode_instantiation(instance):
    assert isinstance(instance, UML2::FlowFinalNode)

@given(instance=UML2::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml2::activityfinalnode_instantiation(instance):
    assert isinstance(instance, UML2::ActivityFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=UML2::DecisionNode_strategy)
@settings(max_examples=50)
def test_uml2::decisionnode_instantiation(instance):
    assert isinstance(instance, UML2::DecisionNode)

@given(instance=UML2::MergeNode_strategy)
@settings(max_examples=50)
def test_uml2::mergenode_instantiation(instance):
    assert isinstance(instance, UML2::MergeNode)

@given(instance=UML2::JoinNode_strategy)
@settings(max_examples=50)
def test_uml2::joinnode_instantiation(instance):
    assert isinstance(instance, UML2::JoinNode)

@given(instance=UML2::JoinNode_strategy)
def test_uml2::joinnode_isCombineDuplicate_type(instance):
    assert isinstance(instance.isCombineDuplicate, bool)


@given(instance=UML2::JoinNode_strategy)
def test_uml2::joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=UML2::FinalNode_strategy)
@settings(max_examples=50)
def test_uml2::finalnode_instantiation(instance):
    assert isinstance(instance, UML2::FinalNode)

@given(instance=UML2::ForkNode_strategy)
@settings(max_examples=50)
def test_uml2::forknode_instantiation(instance):
    assert isinstance(instance, UML2::ForkNode)

@given(instance=UML2::InitialNode_strategy)
@settings(max_examples=50)
def test_uml2::initialnode_instantiation(instance):
    assert isinstance(instance, UML2::InitialNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=UML2::ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml2::objectflow_instantiation(instance):
    assert isinstance(instance, UML2::ObjectFlow)

@given(instance=UML2::ObjectFlow_strategy)
def test_uml2::objectflow_isMultireceive_type(instance):
    assert isinstance(instance.isMultireceive, bool)


@given(instance=UML2::ObjectFlow_strategy)
def test_uml2::objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=UML2::ObjectFlow_strategy)
def test_uml2::objectflow_isMulticast_type(instance):
    assert isinstance(instance.isMulticast, bool)


@given(instance=UML2::ObjectFlow_strategy)
def test_uml2::objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=UML2::ControlFlow_strategy)
@settings(max_examples=50)
def test_uml2::controlflow_instantiation(instance):
    assert isinstance(instance, UML2::ControlFlow)

@given(instance=UML2::ControlNode_strategy)
@settings(max_examples=50)
def test_uml2::controlnode_instantiation(instance):
    assert isinstance(instance, UML2::ControlNode)

@given(instance=UML2::OutputPin_strategy)
@settings(max_examples=50)
def test_uml2::outputpin_instantiation(instance):
    assert isinstance(instance, UML2::OutputPin)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=UML2::InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml2::interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, UML2::InterruptibleActivityRegion)

@given(instance=UML2::Action_strategy)
@settings(max_examples=50)
def test_uml2::action_instantiation(instance):
    assert isinstance(instance, UML2::Action)

@given(instance=UML2::Action_strategy)
def test_uml2::action_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=UML2::Action_strategy)
def test_uml2::action_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=UML2::Manifestation_strategy)
@settings(max_examples=50)
def test_uml2::manifestation_instantiation(instance):
    assert isinstance(instance, UML2::Manifestation)

@given(instance=UML2::Realization_strategy)
@settings(max_examples=50)
def test_uml2::realization_instantiation(instance):
    assert isinstance(instance, UML2::Realization)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=UML2::Usage_strategy)
@settings(max_examples=50)
def test_uml2::usage_instantiation(instance):
    assert isinstance(instance, UML2::Usage)

@given(instance=UML2::Abstraction_strategy)
@settings(max_examples=50)
def test_uml2::abstraction_instantiation(instance):
    assert isinstance(instance, UML2::Abstraction)

@given(instance=UML2::Permission_strategy)
@settings(max_examples=50)
def test_uml2::permission_instantiation(instance):
    assert isinstance(instance, UML2::Permission)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2::Port_strategy)
@settings(max_examples=50)
def test_uml2::port_instantiation(instance):
    assert isinstance(instance, UML2::Port)

@given(instance=UML2::Port_strategy)
def test_uml2::port_isBehavior_type(instance):
    assert isinstance(instance.isBehavior, bool)


@given(instance=UML2::Port_strategy)
def test_uml2::port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original

@given(instance=UML2::Port_strategy)
def test_uml2::port_isService_type(instance):
    assert isinstance(instance.isService, bool)


@given(instance=UML2::Port_strategy)
def test_uml2::port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original

@given(instance=UML2::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2::extensionend_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionEnd)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2::Interaction_strategy)
@settings(max_examples=50)
def test_uml2::interaction_instantiation(instance):
    assert isinstance(instance, UML2::Interaction)

@given(instance=UML2::Activity_strategy)
@settings(max_examples=50)
def test_uml2::activity_instantiation(instance):
    assert isinstance(instance, UML2::Activity)

@given(instance=UML2::Activity_strategy)
def test_uml2::activity_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UML2::Activity_strategy)
def test_uml2::activity_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UML2::Activity_strategy)
def test_uml2::activity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, bool)


@given(instance=UML2::Activity_strategy)
def test_uml2::activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=UML2::Activity_strategy)
def test_uml2::activity_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=UML2::Activity_strategy)
def test_uml2::activity_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UML2::Activity_strategy)
def test_uml2::activity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=UML2::Activity_strategy)
def test_uml2::activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=UML2::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2::statemachine_instantiation(instance):
    assert isinstance(instance, UML2::StateMachine)

@given(instance=UML2::Implementation_strategy)
@settings(max_examples=50)
def test_uml2::implementation_instantiation(instance):
    assert isinstance(instance, UML2::Implementation)

@given(instance=PackageImport_strategy)
@settings(max_examples=50)
def test_packageimport_instantiation(instance):
    assert isinstance(instance, PackageImport)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=UML2::Model_strategy)
@settings(max_examples=50)
def test_uml2::model_instantiation(instance):
    assert isinstance(instance, UML2::Model)

@given(instance=UML2::Model_strategy)
def test_uml2::model_viewpoint_type(instance):
    assert isinstance(instance.viewpoint, str)


@given(instance=UML2::Model_strategy)
def test_uml2::model_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original

@given(instance=UML2::Profile_strategy)
@settings(max_examples=50)
def test_uml2::profile_instantiation(instance):
    assert isinstance(instance, UML2::Profile)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2::associationclass_instantiation(instance):
    assert isinstance(instance, UML2::AssociationClass)

@given(instance=UML2::Component_strategy)
@settings(max_examples=50)
def test_uml2::component_instantiation(instance):
    assert isinstance(instance, UML2::Component)

@given(instance=UML2::Component_strategy)
def test_uml2::component_isIndirectlyInstantiated_type(instance):
    assert isinstance(instance.isIndirectlyInstantiated, bool)


@given(instance=UML2::Component_strategy)
def test_uml2::component_isIndirectlyInstantiated_setter(instance):
    original = instance.isIndirectlyInstantiated
    instance.isIndirectlyInstantiated = original
    assert instance.isIndirectlyInstantiated == original

@given(instance=UML2::Stereotype_strategy)
@settings(max_examples=50)
def test_uml2::stereotype_instantiation(instance):
    assert isinstance(instance, UML2::Stereotype)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=UML2::TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml2::templatebinding_instantiation(instance):
    assert isinstance(instance, UML2::TemplateBinding)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=UML2::Connector_strategy)
@settings(max_examples=50)
def test_uml2::connector_instantiation(instance):
    assert isinstance(instance, UML2::Connector)

@given(instance=UML2::Connector_strategy)
def test_uml2::connector_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UML2::Connector_strategy)
def test_uml2::connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UML2::LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2::literalinteger_instantiation(instance):
    assert isinstance(instance, UML2::LiteralInteger)

@given(instance=UML2::LiteralInteger_strategy)
def test_uml2::literalinteger_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=UML2::LiteralInteger_strategy)
def test_uml2::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UML2::LiteralString_strategy)
@settings(max_examples=50)
def test_uml2::literalstring_instantiation(instance):
    assert isinstance(instance, UML2::LiteralString)

@given(instance=UML2::LiteralString_strategy)
def test_uml2::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UML2::LiteralString_strategy)
def test_uml2::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UML2::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2::LiteralUnlimitedNatural)

@given(instance=UML2::LiteralUnlimitedNatural_strategy)
def test_uml2::literalunlimitednatural_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UML2::LiteralUnlimitedNatural_strategy)
def test_uml2::literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UML2::LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2::literalnull_instantiation(instance):
    assert isinstance(instance, UML2::LiteralNull)

@given(instance=UML2::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2::literalboolean_instantiation(instance):
    assert isinstance(instance, UML2::LiteralBoolean)

@given(instance=UML2::LiteralBoolean_strategy)
def test_uml2::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=UML2::LiteralBoolean_strategy)
def test_uml2::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::StructuredClassifier)

@given(instance=UML2::TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::TemplateableClassifier)

@given(instance=UML2::Artifact_strategy)
@settings(max_examples=50)
def test_uml2::artifact_instantiation(instance):
    assert isinstance(instance, UML2::Artifact)

@given(instance=UML2::Artifact_strategy)
def test_uml2::artifact_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=UML2::Artifact_strategy)
def test_uml2::artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=UML2::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2::BehavioredClassifier)

@given(instance=UML2::InformationItem_strategy)
@settings(max_examples=50)
def test_uml2::informationitem_instantiation(instance):
    assert isinstance(instance, UML2::InformationItem)

@given(instance=UML2::Actor_strategy)
@settings(max_examples=50)
def test_uml2::actor_instantiation(instance):
    assert isinstance(instance, UML2::Actor)

@given(instance=UML2::Signal_strategy)
@settings(max_examples=50)
def test_uml2::signal_instantiation(instance):
    assert isinstance(instance, UML2::Signal)

@given(instance=UML2::Interface_strategy)
@settings(max_examples=50)
def test_uml2::interface_instantiation(instance):
    assert isinstance(instance, UML2::Interface)

@given(instance=UML2::ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2::parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2::ParameterableClassifier)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UML2::Enumeration_strategy)
@settings(max_examples=50)
def test_uml2::enumeration_instantiation(instance):
    assert isinstance(instance, UML2::Enumeration)

@given(instance=UML2::ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml2::profileapplication_instantiation(instance):
    assert isinstance(instance, UML2::ProfileApplication)

@given(instance=UML2::PackageMerge_strategy)
@settings(max_examples=50)
def test_uml2::packagemerge_instantiation(instance):
    assert isinstance(instance, UML2::PackageMerge)

@given(instance=UML2::Substitution_strategy)
@settings(max_examples=50)
def test_uml2::substitution_instantiation(instance):
    assert isinstance(instance, UML2::Substitution)

@given(instance=UML2::Generalization_strategy)
@settings(max_examples=50)
def test_uml2::generalization_instantiation(instance):
    assert isinstance(instance, UML2::Generalization)

@given(instance=UML2::Generalization_strategy)
def test_uml2::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, bool)


@given(instance=UML2::Generalization_strategy)
def test_uml2::generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=UML2::ActivityNode_strategy)
@settings(max_examples=50)
def test_uml2::activitynode_instantiation(instance):
    assert isinstance(instance, UML2::ActivityNode)

@given(instance=UML2::RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2::redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, UML2::RedefinableTemplateSignature)

@given(instance=UML2::Feature_strategy)
@settings(max_examples=50)
def test_uml2::feature_instantiation(instance):
    assert isinstance(instance, UML2::Feature)

@given(instance=UML2::Feature_strategy)
def test_uml2::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=UML2::Feature_strategy)
def test_uml2::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=UML2::Transition_strategy)
@settings(max_examples=50)
def test_uml2::transition_instantiation(instance):
    assert isinstance(instance, UML2::Transition)

@given(instance=UML2::Transition_strategy)
def test_uml2::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UML2::Transition_strategy)
def test_uml2::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UML2::ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml2::activityedge_instantiation(instance):
    assert isinstance(instance, UML2::ActivityEdge)

@given(instance=UML2::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml2::extensionpoint_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionPoint)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=UML2::PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2::primitivetype_instantiation(instance):
    assert isinstance(instance, UML2::PrimitiveType)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=UML2::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml2::enumerationliteral_instantiation(instance):
    assert isinstance(instance, UML2::EnumerationLiteral)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=UML2::State_strategy)
@settings(max_examples=50)
def test_uml2::state_instantiation(instance):
    assert isinstance(instance, UML2::State)

@given(instance=UML2::State_strategy)
def test_uml2::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=UML2::State_strategy)
def test_uml2::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=UML2::State_strategy)
def test_uml2::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, bool)


@given(instance=UML2::State_strategy)
def test_uml2::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=UML2::State_strategy)
def test_uml2::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, bool)


@given(instance=UML2::State_strategy)
def test_uml2::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=UML2::State_strategy)
def test_uml2::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, bool)


@given(instance=UML2::State_strategy)
def test_uml2::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=UML2::Region_strategy)
@settings(max_examples=50)
def test_uml2::region_instantiation(instance):
    assert isinstance(instance, UML2::Region)

@given(instance=UML2::InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml2::interactionoperand_instantiation(instance):
    assert isinstance(instance, UML2::InteractionOperand)

@given(instance=UML2::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2::BehavioralFeature)

@given(instance=UML2::BehavioralFeature_strategy)
def test_uml2::behavioralfeature_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=UML2::BehavioralFeature_strategy)
def test_uml2::behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=UML2::BehavioralFeature_strategy)
def test_uml2::behavioralfeature_concurrency_type(instance):
    assert isinstance(instance.concurrency, str)


@given(instance=UML2::BehavioralFeature_strategy)
def test_uml2::behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=UML2::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml2::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UML2::StructuredActivityNode)

@given(instance=UML2::StructuredActivityNode_strategy)
def test_uml2::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, bool)


@given(instance=UML2::StructuredActivityNode_strategy)
def test_uml2::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=UML2::Property_strategy)
def test_uml2::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=UML2::Property_strategy)
def test_uml2::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=UML2::Property_strategy)
def test_uml2::property_isDerivedUnion_type(instance):
    assert isinstance(instance.isDerivedUnion, bool)


@given(instance=UML2::Property_strategy)
def test_uml2::property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original

@given(instance=UML2::Property_strategy)
def test_uml2::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=UML2::Property_strategy)
def test_uml2::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=UML2::Property_strategy)
def test_uml2::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=UML2::Property_strategy)
def test_uml2::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=UML2::Property_strategy)
def test_uml2::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=UML2::Property_strategy)
def test_uml2::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=UML2::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml2::generalizationset_instantiation(instance):
    assert isinstance(instance, UML2::GeneralizationSet)

@given(instance=UML2::GeneralizationSet_strategy)
def test_uml2::generalizationset_isCovering_type(instance):
    assert isinstance(instance.isCovering, bool)


@given(instance=UML2::GeneralizationSet_strategy)
def test_uml2::generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=UML2::GeneralizationSet_strategy)
def test_uml2::generalizationset_isDisjoint_type(instance):
    assert isinstance(instance.isDisjoint, bool)


@given(instance=UML2::GeneralizationSet_strategy)
def test_uml2::generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=UML2::InformationFlow_strategy)
@settings(max_examples=50)
def test_uml2::informationflow_instantiation(instance):
    assert isinstance(instance, UML2::InformationFlow)

@given(instance=UML2::PrimitiveFunction_strategy)
@settings(max_examples=50)
def test_uml2::primitivefunction_instantiation(instance):
    assert isinstance(instance, UML2::PrimitiveFunction)

@given(instance=UML2::PrimitiveFunction_strategy)
def test_uml2::primitivefunction_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UML2::PrimitiveFunction_strategy)
def test_uml2::primitivefunction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UML2::PrimitiveFunction_strategy)
def test_uml2::primitivefunction_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=UML2::PrimitiveFunction_strategy)
def test_uml2::primitivefunction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UML2::Package_strategy)
@settings(max_examples=50)
def test_uml2::package_instantiation(instance):
    assert isinstance(instance, UML2::Package)

@given(instance=UML2::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml2::instancespecification_instantiation(instance):
    assert isinstance(instance, UML2::InstanceSpecification)

@given(instance=UML2::Type_strategy)
@settings(max_examples=50)
def test_uml2::type_instantiation(instance):
    assert isinstance(instance, UML2::Type)

@given(instance=UML2::Classifier_strategy)
@settings(max_examples=50)
def test_uml2::classifier_instantiation(instance):
    assert isinstance(instance, UML2::Classifier)

@given(instance=UML2::Classifier_strategy)
def test_uml2::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=UML2::Classifier_strategy)
def test_uml2::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=UML2::Extension_strategy)
@settings(max_examples=50)
def test_uml2::extension_instantiation(instance):
    assert isinstance(instance, UML2::Extension)

@given(instance=UML2::Extension_strategy)
def test_uml2::extension_isRequired_type(instance):
    assert isinstance(instance.isRequired, bool)


@given(instance=UML2::Extension_strategy)
def test_uml2::extension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=UML2::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml2::connectorend_instantiation(instance):
    assert isinstance(instance, UML2::ConnectorEnd)

@given(instance=UML2::Pin_strategy)
@settings(max_examples=50)
def test_uml2::pin_instantiation(instance):
    assert isinstance(instance, UML2::Pin)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=UML2::Reception_strategy)
@settings(max_examples=50)
def test_uml2::reception_instantiation(instance):
    assert isinstance(instance, UML2::Reception)

@given(instance=UML2::DataType_strategy)
@settings(max_examples=50)
def test_uml2::datatype_instantiation(instance):
    assert isinstance(instance, UML2::DataType)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UML2::Collaboration_strategy)
@settings(max_examples=50)
def test_uml2::collaboration_instantiation(instance):
    assert isinstance(instance, UML2::Collaboration)

@given(instance=UML2::UseCase_strategy)
@settings(max_examples=50)
def test_uml2::usecase_instantiation(instance):
    assert isinstance(instance, UML2::UseCase)

@given(instance=UML2::Class_strategy)
@settings(max_examples=50)
def test_uml2::class_instantiation(instance):
    assert isinstance(instance, UML2::Class)

@given(instance=UML2::Class_strategy)
def test_uml2::class_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=UML2::Class_strategy)
def test_uml2::class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=UML2::Association_strategy)
@settings(max_examples=50)
def test_uml2::association_instantiation(instance):
    assert isinstance(instance, UML2::Association)

@given(instance=UML2::Association_strategy)
def test_uml2::association_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=UML2::Association_strategy)
def test_uml2::association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=UML2::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml2::directedrelationship_instantiation(instance):
    assert isinstance(instance, UML2::DirectedRelationship)

@given(instance=UML2::Dependency_strategy)
@settings(max_examples=50)
def test_uml2::dependency_instantiation(instance):
    assert isinstance(instance, UML2::Dependency)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=UML2::NamedElement_strategy)
@settings(max_examples=50)
def test_uml2::namedelement_instantiation(instance):
    assert isinstance(instance, UML2::NamedElement)

@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UML2::NamedElement_strategy)
def test_uml2::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2::Relationship_strategy)
@settings(max_examples=50)
def test_uml2::relationship_instantiation(instance):
    assert isinstance(instance, UML2::Relationship)

@given(instance=UML2::QualifierValue_strategy)
@settings(max_examples=50)
def test_uml2::qualifiervalue_instantiation(instance):
    assert isinstance(instance, UML2::QualifierValue)

@given(instance=UML2::LinkEndData_strategy)
@settings(max_examples=50)
def test_uml2::linkenddata_instantiation(instance):
    assert isinstance(instance, UML2::LinkEndData)

@given(instance=UML2::TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2::templatesignature_instantiation(instance):
    assert isinstance(instance, UML2::TemplateSignature)

@given(instance=UML2::Clause_strategy)
@settings(max_examples=50)
def test_uml2::clause_instantiation(instance):
    assert isinstance(instance, UML2::Clause)

@given(instance=UML2::ParameterableElement_strategy)
@settings(max_examples=50)
def test_uml2::parameterableelement_instantiation(instance):
    assert isinstance(instance, UML2::ParameterableElement)

@given(instance=UML2::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml2::exceptionhandler_instantiation(instance):
    assert isinstance(instance, UML2::ExceptionHandler)

@given(instance=UML2::TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml2::templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, UML2::TemplateParameterSubstitution)

@given(instance=UML2::TemplateableElement_strategy)
@settings(max_examples=50)
def test_uml2::templateableelement_instantiation(instance):
    assert isinstance(instance, UML2::TemplateableElement)

@given(instance=UML2::ActivityGroup_strategy)
@settings(max_examples=50)
def test_uml2::activitygroup_instantiation(instance):
    assert isinstance(instance, UML2::ActivityGroup)

@given(instance=UML2::Slot_strategy)
@settings(max_examples=50)
def test_uml2::slot_instantiation(instance):
    assert isinstance(instance, UML2::Slot)

@given(instance=UML2::TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2::templateparameter_instantiation(instance):
    assert isinstance(instance, UML2::TemplateParameter)

@given(instance=UML2::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml2::multiplicityelement_instantiation(instance):
    assert isinstance(instance, UML2::MultiplicityElement)

@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2::Expression_strategy)
@settings(max_examples=50)
def test_uml2::expression_instantiation(instance):
    assert isinstance(instance, UML2::Expression)

@given(instance=UML2::Expression_strategy)
def test_uml2::expression_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=UML2::Expression_strategy)
def test_uml2::expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=UML2::Variable_strategy)
@settings(max_examples=50)
def test_uml2::variable_instantiation(instance):
    assert isinstance(instance, UML2::Variable)

@given(instance=UML2::ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2::objectnode_instantiation(instance):
    assert isinstance(instance, UML2::ObjectNode)

@given(instance=UML2::ObjectNode_strategy)
def test_uml2::objectnode_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=UML2::ObjectNode_strategy)
def test_uml2::objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=UML2::Operation_strategy)
@settings(max_examples=50)
def test_uml2::operation_instantiation(instance):
    assert isinstance(instance, UML2::Operation)

@given(instance=UML2::Operation_strategy)
def test_uml2::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, bool)


@given(instance=UML2::Operation_strategy)
def test_uml2::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=UML2::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2::valuespecification_instantiation(instance):
    assert isinstance(instance, UML2::ValueSpecification)

@given(instance=UML2::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeature)

@given(instance=UML2::StructuralFeature_strategy)
def test_uml2::structuralfeature_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=UML2::StructuralFeature_strategy)
def test_uml2::structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=UML2::Behavior_strategy)
@settings(max_examples=50)
def test_uml2::behavior_instantiation(instance):
    assert isinstance(instance, UML2::Behavior)

@given(instance=UML2::Behavior_strategy)
def test_uml2::behavior_isReentrant_type(instance):
    assert isinstance(instance.isReentrant, bool)


@given(instance=UML2::Behavior_strategy)
def test_uml2::behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=UML2::Parameter_strategy)
@settings(max_examples=50)
def test_uml2::parameter_instantiation(instance):
    assert isinstance(instance, UML2::Parameter)

@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_isException_type(instance):
    assert isinstance(instance.isException, bool)


@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original

@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_isStream_type(instance):
    assert isinstance(instance.isStream, bool)


@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UML2::InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2::instancevalue_instantiation(instance):
    assert isinstance(instance, UML2::InstanceValue)

@given(instance=UML2::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2::literalspecification_instantiation(instance):
    assert isinstance(instance, UML2::LiteralSpecification)

@given(instance=UML2::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::CreateLinkObjectAction)

@given(instance=UML2::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2::opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2::OpaqueExpression)

@given(instance=UML2::OpaqueExpression_strategy)
def test_uml2::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=UML2::OpaqueExpression_strategy)
def test_uml2::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UML2::OpaqueExpression_strategy)
def test_uml2::opaqueexpression_bodies_type(instance):
    assert isinstance(instance.bodies, str)


@given(instance=UML2::OpaqueExpression_strategy)
def test_uml2::opaqueexpression_bodies_setter(instance):
    original = instance.bodies
    instance.bodies = original
    assert instance.bodies == original

@given(instance=UML2::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkObjectEndQualifierAction)

@given(instance=UML2::PackageImport_strategy)
@settings(max_examples=50)
def test_uml2::packageimport_instantiation(instance):
    assert isinstance(instance, UML2::PackageImport)

@given(instance=UML2::PackageImport_strategy)
def test_uml2::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UML2::PackageImport_strategy)
def test_uml2::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=UML2::ElementImport_strategy)
@settings(max_examples=50)
def test_uml2::elementimport_instantiation(instance):
    assert isinstance(instance, UML2::ElementImport)

@given(instance=UML2::ElementImport_strategy)
def test_uml2::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UML2::ElementImport_strategy)
def test_uml2::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=UML2::ElementImport_strategy)
def test_uml2::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=UML2::ElementImport_strategy)
def test_uml2::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml2::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UML2::RaiseExceptionAction)

@given(instance=UML2::ReplyAction_strategy)
@settings(max_examples=50)
def test_uml2::replyaction_instantiation(instance):
    assert isinstance(instance, UML2::ReplyAction)

@given(instance=UML2::Constraint_strategy)
@settings(max_examples=50)
def test_uml2::constraint_instantiation(instance):
    assert isinstance(instance, UML2::Constraint)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=UML2::Message_strategy)
@settings(max_examples=50)
def test_uml2::message_instantiation(instance):
    assert isinstance(instance, UML2::Message)

@given(instance=UML2::Message_strategy)
def test_uml2::message_messageKind_type(instance):
    assert isinstance(instance.messageKind, str)


@given(instance=UML2::Message_strategy)
def test_uml2::message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original

@given(instance=UML2::Message_strategy)
def test_uml2::message_messageSort_type(instance):
    assert isinstance(instance.messageSort, str)


@given(instance=UML2::Message_strategy)
def test_uml2::message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original

@given(instance=UML2::ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml2::activitypartition_instantiation(instance):
    assert isinstance(instance, UML2::ActivityPartition)

@given(instance=UML2::ActivityPartition_strategy)
def test_uml2::activitypartition_isExternal_type(instance):
    assert isinstance(instance.isExternal, bool)


@given(instance=UML2::ActivityPartition_strategy)
def test_uml2::activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=UML2::ActivityPartition_strategy)
def test_uml2::activitypartition_isDimension_type(instance):
    assert isinstance(instance.isDimension, bool)


@given(instance=UML2::ActivityPartition_strategy)
def test_uml2::activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=UML2::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml2::generalordering_instantiation(instance):
    assert isinstance(instance, UML2::GeneralOrdering)

@given(instance=UML2::ParameterSet_strategy)
@settings(max_examples=50)
def test_uml2::parameterset_instantiation(instance):
    assert isinstance(instance, UML2::ParameterSet)

@given(instance=UML2::TypedElement_strategy)
@settings(max_examples=50)
def test_uml2::typedelement_instantiation(instance):
    assert isinstance(instance, UML2::TypedElement)

@given(instance=UML2::Trigger_strategy)
@settings(max_examples=50)
def test_uml2::trigger_instantiation(instance):
    assert isinstance(instance, UML2::Trigger)

@given(instance=UML2::InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml2::interactionfragment_instantiation(instance):
    assert isinstance(instance, UML2::InteractionFragment)

@given(instance=UML2::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml2::packageableelement_instantiation(instance):
    assert isinstance(instance, UML2::PackageableElement)

@given(instance=UML2::PackageableElement_strategy)
def test_uml2::packageableelement_packageableElement_visibility_type(instance):
    assert isinstance(instance.packageableElement_visibility, str)


@given(instance=UML2::PackageableElement_strategy)
def test_uml2::packageableelement_packageableElement_visibility_setter(instance):
    original = instance.packageableElement_visibility
    instance.packageableElement_visibility = original
    assert instance.packageableElement_visibility == original

@given(instance=UML2::ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml2::connectableelement_instantiation(instance):
    assert isinstance(instance, UML2::ConnectableElement)

@given(instance=UML2::RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml2::redefinableelement_instantiation(instance):
    assert isinstance(instance, UML2::RedefinableElement)

@given(instance=UML2::RedefinableElement_strategy)
def test_uml2::redefinableelement_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, bool)


@given(instance=UML2::RedefinableElement_strategy)
def test_uml2::redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=UML2::Include_strategy)
@settings(max_examples=50)
def test_uml2::include_instantiation(instance):
    assert isinstance(instance, UML2::Include)

@given(instance=UML2::CollaborationOccurrence_strategy)
@settings(max_examples=50)
def test_uml2::collaborationoccurrence_instantiation(instance):
    assert isinstance(instance, UML2::CollaborationOccurrence)

@given(instance=UML2::Lifeline_strategy)
@settings(max_examples=50)
def test_uml2::lifeline_instantiation(instance):
    assert isinstance(instance, UML2::Lifeline)

@given(instance=UML2::MessageEnd_strategy)
@settings(max_examples=50)
def test_uml2::messageend_instantiation(instance):
    assert isinstance(instance, UML2::MessageEnd)

@given(instance=UML2::Vertex_strategy)
@settings(max_examples=50)
def test_uml2::vertex_instantiation(instance):
    assert isinstance(instance, UML2::Vertex)

@given(instance=UML2::Extend_strategy)
@settings(max_examples=50)
def test_uml2::extend_instantiation(instance):
    assert isinstance(instance, UML2::Extend)

@given(instance=UML2::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml2::acceptcallaction_instantiation(instance):
    assert isinstance(instance, UML2::AcceptCallAction)

@given(instance=UML2::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadIsClassifiedObjectAction)

@given(instance=UML2::ReadIsClassifiedObjectAction_strategy)
def test_uml2::readisclassifiedobjectaction_isDirect_type(instance):
    assert isinstance(instance.isDirect, bool)


@given(instance=UML2::ReadIsClassifiedObjectAction_strategy)
def test_uml2::readisclassifiedobjectaction_isDirect_setter(instance):
    original = instance.isDirect
    instance.isDirect = original
    assert instance.isDirect == original

@given(instance=UML2::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2::ReclassifyObjectAction)

@given(instance=UML2::ReclassifyObjectAction_strategy)
def test_uml2::reclassifyobjectaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, bool)


@given(instance=UML2::ReclassifyObjectAction_strategy)
def test_uml2::reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=UML2::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml2::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadLinkObjectEndAction)

@given(instance=UML2::StartOwnedBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2::startownedbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2::StartOwnedBehaviorAction)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolStateMachine)

@given(instance=UML2::ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml2::protocolconformance_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolConformance)

@given(instance=UML2::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2::communicationpath_instantiation(instance):
    assert isinstance(instance, UML2::CommunicationPath)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2::executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2::ExecutionEnvironment)

@given(instance=UML2::Device_strategy)
@settings(max_examples=50)
def test_uml2::device_instantiation(instance):
    assert isinstance(instance, UML2::Device)

@given(instance=UML2::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml2::readextentaction_instantiation(instance):
    assert isinstance(instance, UML2::ReadExtentAction)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=UML2::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml2::protocoltransition_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolTransition)

@given(instance=UML2::Node_strategy)
@settings(max_examples=50)
def test_uml2::node_instantiation(instance):
    assert isinstance(instance, UML2::Node)

@given(instance=UML2::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2::DeploymentSpecification)

@given(instance=UML2::DeploymentSpecification_strategy)
def test_uml2::deploymentspecification_executionLocation_type(instance):
    assert isinstance(instance.executionLocation, str)


@given(instance=UML2::DeploymentSpecification_strategy)
def test_uml2::deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original

@given(instance=UML2::DeploymentSpecification_strategy)
def test_uml2::deploymentspecification_deploymentLocation_type(instance):
    assert isinstance(instance.deploymentLocation, str)


@given(instance=UML2::DeploymentSpecification_strategy)
def test_uml2::deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=UML2::DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml2::deploymenttarget_instantiation(instance):
    assert isinstance(instance, UML2::DeploymentTarget)

@given(instance=UML2::DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml2::deployedartifact_instantiation(instance):
    assert isinstance(instance, UML2::DeployedArtifact)

@given(instance=UML2::Deployment_strategy)
@settings(max_examples=50)
def test_uml2::deployment_instantiation(instance):
    assert isinstance(instance, UML2::Deployment)

@given(instance=UML2::Interval_strategy)
@settings(max_examples=50)
def test_uml2::interval_instantiation(instance):
    assert isinstance(instance, UML2::Interval)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UML2::DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2::durationinterval_instantiation(instance):
    assert isinstance(instance, UML2::DurationInterval)

@given(instance=UML2::TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::TimeObservationAction)

@given(instance=UML2::Duration_strategy)
@settings(max_examples=50)
def test_uml2::duration_instantiation(instance):
    assert isinstance(instance, UML2::Duration)

@given(instance=UML2::Duration_strategy)
def test_uml2::duration_firstTime_type(instance):
    assert isinstance(instance.firstTime, bool)


@given(instance=UML2::Duration_strategy)
def test_uml2::duration_firstTime_setter(instance):
    original = instance.firstTime
    instance.firstTime = original
    assert instance.firstTime == original

@given(instance=UML2::TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2::timeexpression_instantiation(instance):
    assert isinstance(instance, UML2::TimeExpression)

@given(instance=UML2::TimeExpression_strategy)
def test_uml2::timeexpression_firstTime_type(instance):
    assert isinstance(instance.firstTime, bool)


@given(instance=UML2::TimeExpression_strategy)
def test_uml2::timeexpression_firstTime_setter(instance):
    original = instance.firstTime
    instance.firstTime = original
    assert instance.firstTime == original

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UML2::DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2::datastorenode_instantiation(instance):
    assert isinstance(instance, UML2::DataStoreNode)

@given(instance=UML2::DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2::durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2::DurationObservationAction)

@given(instance=UML2::TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2::timeinterval_instantiation(instance):
    assert isinstance(instance, UML2::TimeInterval)

@given(instance=UML2::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml2::intervalconstraint_instantiation(instance):
    assert isinstance(instance, UML2::IntervalConstraint)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=UML2::DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml2::durationconstraint_instantiation(instance):
    assert isinstance(instance, UML2::DurationConstraint)

@given(instance=UML2::TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml2::timeconstraint_instantiation(instance):
    assert isinstance(instance, UML2::TimeConstraint)

@given(instance=UML2::SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml2::sendsignalaction_instantiation(instance):
    assert isinstance(instance, UML2::SendSignalAction)

@given(instance=UML2::InvocationAction_strategy)
@settings(max_examples=50)
def test_uml2::invocationaction_instantiation(instance):
    assert isinstance(instance, UML2::InvocationAction)

@given(instance=UML2::Namespace_strategy)
@settings(max_examples=50)
def test_uml2::namespace_instantiation(instance):
    assert isinstance(instance, UML2::Namespace)

@given(instance=UML2::StringExpression_strategy)
@settings(max_examples=50)
def test_uml2::stringexpression_instantiation(instance):
    assert isinstance(instance, UML2::StringExpression)

@given(instance=UML2::Comment_strategy)
@settings(max_examples=50)
def test_uml2::comment_instantiation(instance):
    assert isinstance(instance, UML2::Comment)

@given(instance=UML2::Comment_strategy)
def test_uml2::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UML2::Comment_strategy)
def test_uml2::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UML2::Element_strategy)
@settings(max_examples=50)
def test_uml2::element_instantiation(instance):
    assert isinstance(instance, UML2::Element)

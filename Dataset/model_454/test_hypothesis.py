import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    TemplateSignature,
    LinkAction,
    UMLModel::ReadLinkAction,
    StructuralFeature,
    Transition,
    UMLModel::ProtocolTransition,
    StateMachine,
    InteractionUse,
    UMLModel::PartDecomposition,
    ConnectableElement,
    BehavioralFeature,
    Package,
    UMLModel::Profile,
    UMLModel::Model,
    Abstraction,
    UMLModel::Realization,
    LinkEndData,
    UMLModel::LinkEndDestructionData,
    UMLModel::LinkEndCreationData,
    LiteralSpecification,
    UMLModel::LiteralString,
    UMLModel::LiteralUnlimitedNatural,
    UMLModel::LiteralBoolean,
    UMLModel::LiteralNull,
    UMLModel::LiteralInteger,
    Constraint,
    UMLModel::IntervalConstraint,
    UMLModel::InteractionConstraint,
    Pin,
    DeploymentTarget,
    UMLModel::ProtocolStateMachine,
    MessageEnd,
    OpaqueBehavior,
    UMLModel::FunctionBehavior,
    State,
    UMLModel::FinalState,
    Property,
    UMLModel::Port,
    UMLModel::ExtensionEnd,
    OccurrenceSpecification,
    UMLModel::MessageOccurrenceSpecification,
    UMLModel::ExecutionOccurrenceSpecification,
    InstanceSpecification,
    UMLModel::WriteLinkAction,
    EObject,
    UMLModel::UMLBase,
    CallAction,
    UMLModel::CallBehaviorAction,
    InvocationAction,
    UMLModel::CallAction,
    UMLModel::SendObjectAction,
    UMLModel::SendSignalAction,
    UMLModel::BroadcastSignalAction,
    UMLModel::Manifestation,
    DeployedArtifact,
    Classifier,
    UMLModel::StructuredClassifier,
    UMLModel::InformationItem,
    UMLModel::Signal,
    UMLModel::Interface,
    UMLModel::Artifact,
    MessageEvent,
    UMLModel::SignalEvent,
    UMLModel::ReceiveOperationEvent,
    UMLModel::SendSignalEvent,
    UMLModel::ReceiveSignalEvent,
    UMLModel::AnyReceiveEvent,
    WriteVariableAction,
    UMLModel::RemoveVariableValueAction,
    UMLModel::AddVariableValueAction,
    UMLModel::InputPin,
    WriteStructuralFeatureAction,
    UMLModel::RemoveStructuralFeatureValueAction,
    UMLModel::AddStructuralFeatureValueAction,
    BehavioredClassifier,
    UMLModel::Actor,
    Association,
    UMLModel::Extension,
    Class,
    UMLModel::Stereotype,
    UMLModel::Node,
    UMLModel::AssociationClass,
    Relationship,
    UMLModel::Association,
    Element,
    UMLModel::ParameterableElement,
    UMLModel::Relationship,
    UMLModel::MultiplicityElement,
    UMLModel::LinkEndData,
    UMLModel::Image,
    UMLModel::Slot,
    UMLModel::TemplateSignature,
    UMLModel::NamedElement,
    UMLModel::TemplateableElement,
    UMLModel::TemplateParameter,
    UMLModel::QualifierValue,
    UMLModel::ExceptionHandler,
    UMLModel::TemplateParameterSubstitution,
    FinalNode,
    UMLModel::FlowFinalNode,
    UMLModel::ActivityFinalNode,
    ObjectNode,
    UMLModel::ExpansionNode,
    UMLModel::ActivityParameterNode,
    RedefinableElement,
    UMLModel::Feature,
    UMLModel::RedefinableTemplateSignature,
    UMLModel::ExtensionPoint,
    ActivityGroup,
    UMLModel::InterruptibleActivityRegion,
    NamedElement,
    UMLModel::TypedElement,
    UMLModel::InteractionFragment,
    UMLModel::Vertex,
    UMLModel::GeneralOrdering,
    UMLModel::Namespace,
    UMLModel::RedefinableElement,
    UMLModel::Lifeline,
    UMLModel::MessageEnd,
    UMLModel::Message,
    UMLModel::ActivityPartition,
    UMLModel::ActivityNode,
    Behavior,
    UMLModel::StateMachine,
    UMLModel::OpaqueBehavior,
    UMLModel::Activity,
    InputPin,
    UMLModel::ValuePin,
    UMLModel::ActionInputPin,
    ExecutionSpecification,
    UMLModel::ActionExecutionSpecification,
    UMLModel::ActivityGroup,
    UMLModel::ActivityEdge,
    AcceptEventAction,
    UMLModel::AcceptCallAction,
    Dependency,
    UMLModel::Usage,
    UMLModel::Abstraction,
    ExecutableNode,
    UMLModel::Action,
    UMLModel::Trigger,
    Action,
    UMLModel::VariableAction,
    UMLModel::UnmarshallAction,
    UMLModel::TestIdentityAction,
    UMLModel::StartClassifierBehaviorAction,
    UMLModel::RaiseExceptionAction,
    UMLModel::ReadExtentAction,
    UMLModel::ReclassifyObjectAction,
    UMLModel::InvocationAction,
    UMLModel::ReadIsClassifiedObjectAction,
    UMLModel::ReadLinkObjectEndAction,
    UMLModel::ReadLinkObjectEndQualifierAction,
    UMLModel::OpaqueAction,
    UMLModel::LinkAction,
    UMLModel::ValueSpecificationAction,
    UMLModel::ReduceAction,
    UMLModel::ReplyAction,
    UMLModel::StructuralFeatureAction,
    UMLModel::ReadSelfAction,
    UMLModel::AcceptEventAction,
    UMLModel::OutputPin,
    UMLBase,
    UMLModel::Element,
    Observation,
    UMLModel::TimeObservation,
    UMLModel::DurationObservation,
    Interval,
    UMLModel::TimeInterval,
    UMLModel::DurationInterval,
    IntervalConstraint,
    UMLModel::TimeConstraint,
    UMLModel::DurationConstraint,
    ValueSpecification,
    UMLModel::LiteralSpecification,
    UMLModel::Interval,
    UMLModel::InstanceValue,
    UMLModel::OpaqueExpression,
    UMLModel::TimeExpression,
    UMLModel::Expression,
    UMLModel::Duration,
    UMLModel::EnumerationLiteral,
    DataType,
    UMLModel::PrimitiveType,
    UMLModel::Enumeration,
    UMLModel::DestroyObjectAction,
    Node,
    UMLModel::ExecutionEnvironment,
    UMLModel::Device,
    UMLModel::DirectedRelationship,
    Artifact,
    UMLModel::DeployedArtifact,
    UMLModel::DeploymentSpecification,
    UMLModel::Deployment,
    UMLModel::DeploymentTarget,
    MultiplicityElement,
    UMLModel::Pin,
    UMLModel::Variable,
    UMLModel::ConnectorEnd,
    DirectedRelationship,
    UMLModel::Extend,
    UMLModel::ProtocolConformance,
    UMLModel::ElementImport,
    UMLModel::Include,
    UMLModel::TemplateBinding,
    UMLModel::ProfileApplication,
    UMLModel::PackageMerge,
    UMLModel::PackageImport,
    ParameterableElement,
    TypedElement,
    ControlNode,
    UMLModel::ForkNode,
    UMLModel::JoinNode,
    UMLModel::FinalNode,
    UMLModel::MergeNode,
    UMLModel::InitialNode,
    UMLModel::ConnectableElement,
    UMLModel::DecisionNode,
    CombinedFragment,
    UMLModel::ConsiderIgnoreFragment,
    UMLModel::DataType,
    CentralBufferNode,
    UMLModel::DataStoreNode,
    UMLModel::CentralBufferNode,
    WriteLinkAction,
    UMLModel::DestroyLinkAction,
    UMLModel::CreateLinkAction,
    PackageableElement,
    UMLModel::Type,
    UMLModel::Event,
    UMLModel::Observation,
    UMLModel::InstanceSpecification,
    UMLModel::GeneralizationSet,
    UMLModel::ValueSpecification,
    UMLModel::InformationFlow,
    UMLModel::Constraint,
    UMLModel::CreateObjectAction,
    CreateLinkAction,
    UMLModel::CreateLinkObjectAction,
    StructuredActivityNode,
    UMLModel::ExpansionRegion,
    UMLModel::SequenceNode,
    UMLModel::LoopNode,
    UMLModel::ConditionalNode,
    UMLModel::Gate,
    ActivityNode,
    UMLModel::ObjectNode,
    UMLModel::ExecutableNode,
    UMLModel::ControlNode,
    ActivityEdge,
    UMLModel::ObjectFlow,
    UMLModel::ControlFlow,
    Vertex,
    UMLModel::Pseudostate,
    UMLModel::ConnectionPointReference,
    UMLModel::Comment,
    UMLModel::Dependency,
    StructuredClassifier,
    UMLModel::EncapsulatedClassifier,
    UMLModel::Collaboration,
    StructuralFeatureAction,
    UMLModel::ReadStructuralFeatureAction,
    UMLModel::WriteStructuralFeatureAction,
    UMLModel::ClearStructuralFeatureAction,
    UMLModel::ClearAssociationAction,
    VariableAction,
    UMLModel::ReadVariableAction,
    UMLModel::WriteVariableAction,
    UMLModel::ClearVariableAction,
    UMLModel::Clause,
    InteractionFragment,
    UMLModel::StateInvariant,
    UMLModel::OccurrenceSpecification,
    UMLModel::InteractionUse,
    UMLModel::Interaction,
    UMLModel::Continuation,
    UMLModel::ExecutionSpecification,
    UMLModel::CombinedFragment,
    Realization,
    UMLModel::ComponentRealization,
    UMLModel::PackageableElement,
    UMLModel::Component,
    UMLModel::CommunicationPath,
    UMLModel::Generalization,
    TemplateableElement,
    UMLModel::Property,
    UMLModel::Operation,
    UMLModel::StringExpression,
    Type,
    UMLModel::Reception,
    EncapsulatedClassifier,
    UMLModel::Class,
    Event,
    UMLModel::ExecutionEvent,
    UMLModel::DestructionEvent,
    UMLModel::MessageEvent,
    UMLModel::TimeEvent,
    UMLModel::CreationEvent,
    UMLModel::ChangeEvent,
    UMLModel::CallOperationAction,
    TemplateParameter,
    UMLModel::ConnectableElementTemplateParameter,
    UMLModel::OperationTemplateParameter,
    UMLModel::ClassifierTemplateParameter,
    UMLModel::UseCase,
    UMLModel::CollaborationUse,
    UMLModel::Substitution,
    UMLModel::InterfaceRealization,
    UMLModel::BehavioredClassifier,
    Feature,
    UMLModel::Connector,
    UMLModel::StructuralFeature,
    Namespace,
    UMLModel::InteractionOperand,
    UMLModel::Transition,
    UMLModel::Classifier,
    UMLModel::Package,
    UMLModel::StructuredActivityNode,
    UMLModel::Region,
    UMLModel::State,
    UMLModel::BehavioralFeature,
    UMLModel::BehaviorExecutionSpecification,
    UMLModel::ParameterSet,
    UMLModel::Parameter,
    UMLModel::CallEvent,
    UMLModel::Behavior,
    AggregationKind,
    CallConcurrencyKind,
    MessageSort,
    MessageKind,
    InteractionOperatorKind,
    VisibilityKind,
    ConnectorKind,
    ExpansionKind,
    ParameterDirectionKind,
    PseudostateKind,
    ObjectNodeOrderingKind,
    ParameterEffectKind,
    TransitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadLinkAction)


def test_umlmodel::readlinkaction_constructor_exists():
    assert callable(UMLModel::ReadLinkAction.__init__)


def test_umlmodel::readlinkaction_constructor_args():
    sig = inspect.signature(UMLModel::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::protocoltransition_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ProtocolTransition)


def test_umlmodel::protocoltransition_constructor_exists():
    assert callable(UMLModel::ProtocolTransition.__init__)


def test_umlmodel::protocoltransition_constructor_args():
    sig = inspect.signature(UMLModel::ProtocolTransition.__init__)
    params = list(sig.parameters.keys())
    assert "preCondition" in params, "Missing parameter 'preCondition'"
    assert "referred" in params, "Missing parameter 'referred'"
    assert "postCondition" in params, "Missing parameter 'postCondition'"

def test_umlmodel::protocoltransition_has_preCondition():
    assert hasattr(UMLModel::ProtocolTransition, "preCondition")
    descriptor = None
    for klass in UMLModel::ProtocolTransition.__mro__:
        if "preCondition" in klass.__dict__:
            descriptor = klass.__dict__["preCondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::protocoltransition_has_referred():
    assert hasattr(UMLModel::ProtocolTransition, "referred")
    descriptor = None
    for klass in UMLModel::ProtocolTransition.__mro__:
        if "referred" in klass.__dict__:
            descriptor = klass.__dict__["referred"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::protocoltransition_has_postCondition():
    assert hasattr(UMLModel::ProtocolTransition, "postCondition")
    descriptor = None
    for klass in UMLModel::ProtocolTransition.__mro__:
        if "postCondition" in klass.__dict__:
            descriptor = klass.__dict__["postCondition"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_interactionuse_is_not_abstract():
    assert not inspect.isabstract(InteractionUse)


def test_interactionuse_constructor_exists():
    assert callable(InteractionUse.__init__)


def test_interactionuse_constructor_args():
    sig = inspect.signature(InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::partdecomposition_is_not_abstract():
    assert not inspect.isabstract(UMLModel::PartDecomposition)


def test_umlmodel::partdecomposition_constructor_exists():
    assert callable(UMLModel::PartDecomposition.__init__)


def test_umlmodel::partdecomposition_constructor_args():
    sig = inspect.signature(UMLModel::PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::profile_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Profile)


def test_umlmodel::profile_constructor_exists():
    assert callable(UMLModel::Profile.__init__)


def test_umlmodel::profile_constructor_args():
    sig = inspect.signature(UMLModel::Profile.__init__)
    params = list(sig.parameters.keys())
    assert "metaclassReference" in params, "Missing parameter 'metaclassReference'"
    assert "metamodelReference" in params, "Missing parameter 'metamodelReference'"
    assert "ownedStereotype" in params, "Missing parameter 'ownedStereotype'"

def test_umlmodel::profile_has_metaclassReference():
    assert hasattr(UMLModel::Profile, "metaclassReference")
    descriptor = None
    for klass in UMLModel::Profile.__mro__:
        if "metaclassReference" in klass.__dict__:
            descriptor = klass.__dict__["metaclassReference"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::profile_has_metamodelReference():
    assert hasattr(UMLModel::Profile, "metamodelReference")
    descriptor = None
    for klass in UMLModel::Profile.__mro__:
        if "metamodelReference" in klass.__dict__:
            descriptor = klass.__dict__["metamodelReference"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::profile_has_ownedStereotype():
    assert hasattr(UMLModel::Profile, "ownedStereotype")
    descriptor = None
    for klass in UMLModel::Profile.__mro__:
        if "ownedStereotype" in klass.__dict__:
            descriptor = klass.__dict__["ownedStereotype"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::model_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Model)


def test_umlmodel::model_constructor_exists():
    assert callable(UMLModel::Model.__init__)


def test_umlmodel::model_constructor_args():
    sig = inspect.signature(UMLModel::Model.__init__)
    params = list(sig.parameters.keys())
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"

def test_umlmodel::model_has_viewpoint():
    assert hasattr(UMLModel::Model, "viewpoint")
    descriptor = None
    for klass in UMLModel::Model.__mro__:
        if "viewpoint" in klass.__dict__:
            descriptor = klass.__dict__["viewpoint"]
            break
    assert isinstance(descriptor, property)



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::realization_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Realization)


def test_umlmodel::realization_constructor_exists():
    assert callable(UMLModel::Realization.__init__)


def test_umlmodel::realization_constructor_args():
    sig = inspect.signature(UMLModel::Realization.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LinkEndDestructionData)


def test_umlmodel::linkenddestructiondata_constructor_exists():
    assert callable(UMLModel::LinkEndDestructionData.__init__)


def test_umlmodel::linkenddestructiondata_constructor_args():
    sig = inspect.signature(UMLModel::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"
    assert "destroyAt" in params, "Missing parameter 'destroyAt'"

def test_umlmodel::linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(UMLModel::LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in UMLModel::LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::linkenddestructiondata_has_destroyAt():
    assert hasattr(UMLModel::LinkEndDestructionData, "destroyAt")
    descriptor = None
    for klass in UMLModel::LinkEndDestructionData.__mro__:
        if "destroyAt" in klass.__dict__:
            descriptor = klass.__dict__["destroyAt"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LinkEndCreationData)


def test_umlmodel::linkendcreationdata_constructor_exists():
    assert callable(UMLModel::LinkEndCreationData.__init__)


def test_umlmodel::linkendcreationdata_constructor_args():
    sig = inspect.signature(UMLModel::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "insertAt" in params, "Missing parameter 'insertAt'"
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_umlmodel::linkendcreationdata_has_insertAt():
    assert hasattr(UMLModel::LinkEndCreationData, "insertAt")
    descriptor = None
    for klass in UMLModel::LinkEndCreationData.__mro__:
        if "insertAt" in klass.__dict__:
            descriptor = klass.__dict__["insertAt"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::linkendcreationdata_has_isReplaceAll():
    assert hasattr(UMLModel::LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in UMLModel::LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::literalstring_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LiteralString)


def test_umlmodel::literalstring_constructor_exists():
    assert callable(UMLModel::LiteralString.__init__)


def test_umlmodel::literalstring_constructor_args():
    sig = inspect.signature(UMLModel::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel::literalstring_has_value():
    assert hasattr(UMLModel::LiteralString, "value")
    descriptor = None
    for klass in UMLModel::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LiteralUnlimitedNatural)


def test_umlmodel::literalunlimitednatural_constructor_exists():
    assert callable(UMLModel::LiteralUnlimitedNatural.__init__)


def test_umlmodel::literalunlimitednatural_constructor_args():
    sig = inspect.signature(UMLModel::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel::literalunlimitednatural_has_value():
    assert hasattr(UMLModel::LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in UMLModel::LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::literalboolean_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LiteralBoolean)


def test_umlmodel::literalboolean_constructor_exists():
    assert callable(UMLModel::LiteralBoolean.__init__)


def test_umlmodel::literalboolean_constructor_args():
    sig = inspect.signature(UMLModel::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel::literalboolean_has_value():
    assert hasattr(UMLModel::LiteralBoolean, "value")
    descriptor = None
    for klass in UMLModel::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::literalnull_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LiteralNull)


def test_umlmodel::literalnull_constructor_exists():
    assert callable(UMLModel::LiteralNull.__init__)


def test_umlmodel::literalnull_constructor_args():
    sig = inspect.signature(UMLModel::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::literalinteger_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LiteralInteger)


def test_umlmodel::literalinteger_constructor_exists():
    assert callable(UMLModel::LiteralInteger.__init__)


def test_umlmodel::literalinteger_constructor_args():
    sig = inspect.signature(UMLModel::LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel::literalinteger_has_value():
    assert hasattr(UMLModel::LiteralInteger, "value")
    descriptor = None
    for klass in UMLModel::LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel::IntervalConstraint)


def test_umlmodel::intervalconstraint_constructor_exists():
    assert callable(UMLModel::IntervalConstraint.__init__)


def test_umlmodel::intervalconstraint_constructor_args():
    sig = inspect.signature(UMLModel::IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InteractionConstraint)


def test_umlmodel::interactionconstraint_constructor_exists():
    assert callable(UMLModel::InteractionConstraint.__init__)


def test_umlmodel::interactionconstraint_constructor_args():
    sig = inspect.signature(UMLModel::InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ProtocolStateMachine)


def test_umlmodel::protocolstatemachine_constructor_exists():
    assert callable(UMLModel::ProtocolStateMachine.__init__)


def test_umlmodel::protocolstatemachine_constructor_args():
    sig = inspect.signature(UMLModel::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::functionbehavior_is_not_abstract():
    assert not inspect.isabstract(UMLModel::FunctionBehavior)


def test_umlmodel::functionbehavior_constructor_exists():
    assert callable(UMLModel::FunctionBehavior.__init__)


def test_umlmodel::functionbehavior_constructor_args():
    sig = inspect.signature(UMLModel::FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::finalstate_is_not_abstract():
    assert not inspect.isabstract(UMLModel::FinalState)


def test_umlmodel::finalstate_constructor_exists():
    assert callable(UMLModel::FinalState.__init__)


def test_umlmodel::finalstate_constructor_args():
    sig = inspect.signature(UMLModel::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::port_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Port)


def test_umlmodel::port_constructor_exists():
    assert callable(UMLModel::Port.__init__)


def test_umlmodel::port_constructor_args():
    sig = inspect.signature(UMLModel::Port.__init__)
    params = list(sig.parameters.keys())
    assert "isService" in params, "Missing parameter 'isService'"
    assert "provided" in params, "Missing parameter 'provided'"
    assert "protocol" in params, "Missing parameter 'protocol'"
    assert "required" in params, "Missing parameter 'required'"
    assert "redefinedPort" in params, "Missing parameter 'redefinedPort'"
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"

def test_umlmodel::port_has_isService():
    assert hasattr(UMLModel::Port, "isService")
    descriptor = None
    for klass in UMLModel::Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::port_has_provided():
    assert hasattr(UMLModel::Port, "provided")
    descriptor = None
    for klass in UMLModel::Port.__mro__:
        if "provided" in klass.__dict__:
            descriptor = klass.__dict__["provided"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::port_has_protocol():
    assert hasattr(UMLModel::Port, "protocol")
    descriptor = None
    for klass in UMLModel::Port.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::port_has_required():
    assert hasattr(UMLModel::Port, "required")
    descriptor = None
    for klass in UMLModel::Port.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::port_has_redefinedPort():
    assert hasattr(UMLModel::Port, "redefinedPort")
    descriptor = None
    for klass in UMLModel::Port.__mro__:
        if "redefinedPort" in klass.__dict__:
            descriptor = klass.__dict__["redefinedPort"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::port_has_isBehavior():
    assert hasattr(UMLModel::Port, "isBehavior")
    descriptor = None
    for klass in UMLModel::Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::extensionend_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExtensionEnd)


def test_umlmodel::extensionend_constructor_exists():
    assert callable(UMLModel::ExtensionEnd.__init__)


def test_umlmodel::extensionend_constructor_args():
    sig = inspect.signature(UMLModel::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::MessageOccurrenceSpecification)


def test_umlmodel::messageoccurrencespecification_constructor_exists():
    assert callable(UMLModel::MessageOccurrenceSpecification.__init__)


def test_umlmodel::messageoccurrencespecification_constructor_args():
    sig = inspect.signature(UMLModel::MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExecutionOccurrenceSpecification)


def test_umlmodel::executionoccurrencespecification_constructor_exists():
    assert callable(UMLModel::ExecutionOccurrenceSpecification.__init__)


def test_umlmodel::executionoccurrencespecification_constructor_args():
    sig = inspect.signature(UMLModel::ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "execution" in params, "Missing parameter 'execution'"

def test_umlmodel::executionoccurrencespecification_has_execution():
    assert hasattr(UMLModel::ExecutionOccurrenceSpecification, "execution")
    descriptor = None
    for klass in UMLModel::ExecutionOccurrenceSpecification.__mro__:
        if "execution" in klass.__dict__:
            descriptor = klass.__dict__["execution"]
            break
    assert isinstance(descriptor, property)



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::WriteLinkAction)


def test_umlmodel::writelinkaction_constructor_exists():
    assert callable(UMLModel::WriteLinkAction.__init__)


def test_umlmodel::writelinkaction_constructor_args():
    sig = inspect.signature(UMLModel::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::umlbase_is_not_abstract():
    assert not inspect.isabstract(UMLModel::UMLBase)


def test_umlmodel::umlbase_constructor_exists():
    assert callable(UMLModel::UMLBase.__init__)


def test_umlmodel::umlbase_constructor_args():
    sig = inspect.signature(UMLModel::UMLBase.__init__)
    params = list(sig.parameters.keys())
    assert "umlID" in params, "Missing parameter 'umlID'"

def test_umlmodel::umlbase_has_umlID():
    assert hasattr(UMLModel::UMLBase, "umlID")
    descriptor = None
    for klass in UMLModel::UMLBase.__mro__:
        if "umlID" in klass.__dict__:
            descriptor = klass.__dict__["umlID"]
            break
    assert isinstance(descriptor, property)



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CallBehaviorAction)


def test_umlmodel::callbehavioraction_constructor_exists():
    assert callable(UMLModel::CallBehaviorAction.__init__)


def test_umlmodel::callbehavioraction_constructor_args():
    sig = inspect.signature(UMLModel::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"

def test_umlmodel::callbehavioraction_has_behavior():
    assert hasattr(UMLModel::CallBehaviorAction, "behavior")
    descriptor = None
    for klass in UMLModel::CallBehaviorAction.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::callaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CallAction)


def test_umlmodel::callaction_constructor_exists():
    assert callable(UMLModel::CallAction.__init__)


def test_umlmodel::callaction_constructor_args():
    sig = inspect.signature(UMLModel::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_umlmodel::callaction_has_isSynchronous():
    assert hasattr(UMLModel::CallAction, "isSynchronous")
    descriptor = None
    for klass in UMLModel::CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::SendObjectAction)


def test_umlmodel::sendobjectaction_constructor_exists():
    assert callable(UMLModel::SendObjectAction.__init__)


def test_umlmodel::sendobjectaction_constructor_args():
    sig = inspect.signature(UMLModel::SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::SendSignalAction)


def test_umlmodel::sendsignalaction_constructor_exists():
    assert callable(UMLModel::SendSignalAction.__init__)


def test_umlmodel::sendsignalaction_constructor_args():
    sig = inspect.signature(UMLModel::SendSignalAction.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel::sendsignalaction_has_signal():
    assert hasattr(UMLModel::SendSignalAction, "signal")
    descriptor = None
    for klass in UMLModel::SendSignalAction.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::BroadcastSignalAction)


def test_umlmodel::broadcastsignalaction_constructor_exists():
    assert callable(UMLModel::BroadcastSignalAction.__init__)


def test_umlmodel::broadcastsignalaction_constructor_args():
    sig = inspect.signature(UMLModel::BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel::broadcastsignalaction_has_signal():
    assert hasattr(UMLModel::BroadcastSignalAction, "signal")
    descriptor = None
    for klass in UMLModel::BroadcastSignalAction.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::manifestation_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Manifestation)


def test_umlmodel::manifestation_constructor_exists():
    assert callable(UMLModel::Manifestation.__init__)


def test_umlmodel::manifestation_constructor_args():
    sig = inspect.signature(UMLModel::Manifestation.__init__)
    params = list(sig.parameters.keys())
    assert "utilizedElement" in params, "Missing parameter 'utilizedElement'"

def test_umlmodel::manifestation_has_utilizedElement():
    assert hasattr(UMLModel::Manifestation, "utilizedElement")
    descriptor = None
    for klass in UMLModel::Manifestation.__mro__:
        if "utilizedElement" in klass.__dict__:
            descriptor = klass.__dict__["utilizedElement"]
            break
    assert isinstance(descriptor, property)



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StructuredClassifier)


def test_umlmodel::structuredclassifier_constructor_exists():
    assert callable(UMLModel::StructuredClassifier.__init__)


def test_umlmodel::structuredclassifier_constructor_args():
    sig = inspect.signature(UMLModel::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "part" in params, "Missing parameter 'part'"
    assert "role" in params, "Missing parameter 'role'"

def test_umlmodel::structuredclassifier_has_part():
    assert hasattr(UMLModel::StructuredClassifier, "part")
    descriptor = None
    for klass in UMLModel::StructuredClassifier.__mro__:
        if "part" in klass.__dict__:
            descriptor = klass.__dict__["part"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::structuredclassifier_has_role():
    assert hasattr(UMLModel::StructuredClassifier, "role")
    descriptor = None
    for klass in UMLModel::StructuredClassifier.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::informationitem_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InformationItem)


def test_umlmodel::informationitem_constructor_exists():
    assert callable(UMLModel::InformationItem.__init__)


def test_umlmodel::informationitem_constructor_args():
    sig = inspect.signature(UMLModel::InformationItem.__init__)
    params = list(sig.parameters.keys())
    assert "represented" in params, "Missing parameter 'represented'"

def test_umlmodel::informationitem_has_represented():
    assert hasattr(UMLModel::InformationItem, "represented")
    descriptor = None
    for klass in UMLModel::InformationItem.__mro__:
        if "represented" in klass.__dict__:
            descriptor = klass.__dict__["represented"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::signal_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Signal)


def test_umlmodel::signal_constructor_exists():
    assert callable(UMLModel::Signal.__init__)


def test_umlmodel::signal_constructor_args():
    sig = inspect.signature(UMLModel::Signal.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::interface_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Interface)


def test_umlmodel::interface_constructor_exists():
    assert callable(UMLModel::Interface.__init__)


def test_umlmodel::interface_constructor_args():
    sig = inspect.signature(UMLModel::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedInterface" in params, "Missing parameter 'redefinedInterface'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_umlmodel::interface_has_redefinedInterface():
    assert hasattr(UMLModel::Interface, "redefinedInterface")
    descriptor = None
    for klass in UMLModel::Interface.__mro__:
        if "redefinedInterface" in klass.__dict__:
            descriptor = klass.__dict__["redefinedInterface"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::interface_has_isActive():
    assert hasattr(UMLModel::Interface, "isActive")
    descriptor = None
    for klass in UMLModel::Interface.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::artifact_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Artifact)


def test_umlmodel::artifact_constructor_exists():
    assert callable(UMLModel::Artifact.__init__)


def test_umlmodel::artifact_constructor_args():
    sig = inspect.signature(UMLModel::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_umlmodel::artifact_has_fileName():
    assert hasattr(UMLModel::Artifact, "fileName")
    descriptor = None
    for klass in UMLModel::Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::signalevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::SignalEvent)


def test_umlmodel::signalevent_constructor_exists():
    assert callable(UMLModel::SignalEvent.__init__)


def test_umlmodel::signalevent_constructor_args():
    sig = inspect.signature(UMLModel::SignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel::signalevent_has_signal():
    assert hasattr(UMLModel::SignalEvent, "signal")
    descriptor = None
    for klass in UMLModel::SignalEvent.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::receiveoperationevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReceiveOperationEvent)


def test_umlmodel::receiveoperationevent_constructor_exists():
    assert callable(UMLModel::ReceiveOperationEvent.__init__)


def test_umlmodel::receiveoperationevent_constructor_args():
    sig = inspect.signature(UMLModel::ReceiveOperationEvent.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel::receiveoperationevent_has_operation():
    assert hasattr(UMLModel::ReceiveOperationEvent, "operation")
    descriptor = None
    for klass in UMLModel::ReceiveOperationEvent.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::sendsignalevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::SendSignalEvent)


def test_umlmodel::sendsignalevent_constructor_exists():
    assert callable(UMLModel::SendSignalEvent.__init__)


def test_umlmodel::sendsignalevent_constructor_args():
    sig = inspect.signature(UMLModel::SendSignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel::sendsignalevent_has_signal():
    assert hasattr(UMLModel::SendSignalEvent, "signal")
    descriptor = None
    for klass in UMLModel::SendSignalEvent.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::receivesignalevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReceiveSignalEvent)


def test_umlmodel::receivesignalevent_constructor_exists():
    assert callable(UMLModel::ReceiveSignalEvent.__init__)


def test_umlmodel::receivesignalevent_constructor_args():
    sig = inspect.signature(UMLModel::ReceiveSignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel::receivesignalevent_has_signal():
    assert hasattr(UMLModel::ReceiveSignalEvent, "signal")
    descriptor = None
    for klass in UMLModel::ReceiveSignalEvent.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::AnyReceiveEvent)


def test_umlmodel::anyreceiveevent_constructor_exists():
    assert callable(UMLModel::AnyReceiveEvent.__init__)


def test_umlmodel::anyreceiveevent_constructor_args():
    sig = inspect.signature(UMLModel::AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::RemoveVariableValueAction)


def test_umlmodel::removevariablevalueaction_constructor_exists():
    assert callable(UMLModel::RemoveVariableValueAction.__init__)


def test_umlmodel::removevariablevalueaction_constructor_args():
    sig = inspect.signature(UMLModel::RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_umlmodel::removevariablevalueaction_has_isRemoveDuplicates():
    assert hasattr(UMLModel::RemoveVariableValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in UMLModel::RemoveVariableValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::AddVariableValueAction)


def test_umlmodel::addvariablevalueaction_constructor_exists():
    assert callable(UMLModel::AddVariableValueAction.__init__)


def test_umlmodel::addvariablevalueaction_constructor_args():
    sig = inspect.signature(UMLModel::AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_umlmodel::addvariablevalueaction_has_isReplaceAll():
    assert hasattr(UMLModel::AddVariableValueAction, "isReplaceAll")
    descriptor = None
    for klass in UMLModel::AddVariableValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::inputpin_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InputPin)


def test_umlmodel::inputpin_constructor_exists():
    assert callable(UMLModel::InputPin.__init__)


def test_umlmodel::inputpin_constructor_args():
    sig = inspect.signature(UMLModel::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::RemoveStructuralFeatureValueAction)


def test_umlmodel::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UMLModel::RemoveStructuralFeatureValueAction.__init__)


def test_umlmodel::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UMLModel::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_umlmodel::removestructuralfeaturevalueaction_has_isRemoveDuplicates():
    assert hasattr(UMLModel::RemoveStructuralFeatureValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in UMLModel::RemoveStructuralFeatureValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::AddStructuralFeatureValueAction)


def test_umlmodel::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UMLModel::AddStructuralFeatureValueAction.__init__)


def test_umlmodel::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UMLModel::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_umlmodel::addstructuralfeaturevalueaction_has_isReplaceAll():
    assert hasattr(UMLModel::AddStructuralFeatureValueAction, "isReplaceAll")
    descriptor = None
    for klass in UMLModel::AddStructuralFeatureValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::actor_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Actor)


def test_umlmodel::actor_constructor_exists():
    assert callable(UMLModel::Actor.__init__)


def test_umlmodel::actor_constructor_args():
    sig = inspect.signature(UMLModel::Actor.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::extension_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Extension)


def test_umlmodel::extension_constructor_exists():
    assert callable(UMLModel::Extension.__init__)


def test_umlmodel::extension_constructor_args():
    sig = inspect.signature(UMLModel::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "metaClass" in params, "Missing parameter 'metaClass'"
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_umlmodel::extension_has_metaClass():
    assert hasattr(UMLModel::Extension, "metaClass")
    descriptor = None
    for klass in UMLModel::Extension.__mro__:
        if "metaClass" in klass.__dict__:
            descriptor = klass.__dict__["metaClass"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::extension_has_isRequired():
    assert hasattr(UMLModel::Extension, "isRequired")
    descriptor = None
    for klass in UMLModel::Extension.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::stereotype_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Stereotype)


def test_umlmodel::stereotype_constructor_exists():
    assert callable(UMLModel::Stereotype.__init__)


def test_umlmodel::stereotype_constructor_args():
    sig = inspect.signature(UMLModel::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::node_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Node)


def test_umlmodel::node_constructor_exists():
    assert callable(UMLModel::Node.__init__)


def test_umlmodel::node_constructor_args():
    sig = inspect.signature(UMLModel::Node.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::associationclass_is_not_abstract():
    assert not inspect.isabstract(UMLModel::AssociationClass)


def test_umlmodel::associationclass_constructor_exists():
    assert callable(UMLModel::AssociationClass.__init__)


def test_umlmodel::associationclass_constructor_args():
    sig = inspect.signature(UMLModel::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::association_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Association)


def test_umlmodel::association_constructor_exists():
    assert callable(UMLModel::Association.__init__)


def test_umlmodel::association_constructor_args():
    sig = inspect.signature(UMLModel::Association.__init__)
    params = list(sig.parameters.keys())
    assert "navigableOwnedEnd" in params, "Missing parameter 'navigableOwnedEnd'"
    assert "memberEnd" in params, "Missing parameter 'memberEnd'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "endType" in params, "Missing parameter 'endType'"

def test_umlmodel::association_has_navigableOwnedEnd():
    assert hasattr(UMLModel::Association, "navigableOwnedEnd")
    descriptor = None
    for klass in UMLModel::Association.__mro__:
        if "navigableOwnedEnd" in klass.__dict__:
            descriptor = klass.__dict__["navigableOwnedEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::association_has_memberEnd():
    assert hasattr(UMLModel::Association, "memberEnd")
    descriptor = None
    for klass in UMLModel::Association.__mro__:
        if "memberEnd" in klass.__dict__:
            descriptor = klass.__dict__["memberEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::association_has_isDerived():
    assert hasattr(UMLModel::Association, "isDerived")
    descriptor = None
    for klass in UMLModel::Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::association_has_endType():
    assert hasattr(UMLModel::Association, "endType")
    descriptor = None
    for klass in UMLModel::Association.__mro__:
        if "endType" in klass.__dict__:
            descriptor = klass.__dict__["endType"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::parameterableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ParameterableElement)


def test_umlmodel::parameterableelement_constructor_exists():
    assert callable(UMLModel::ParameterableElement.__init__)


def test_umlmodel::parameterableelement_constructor_args():
    sig = inspect.signature(UMLModel::ParameterableElement.__init__)
    params = list(sig.parameters.keys())
    assert "templateParameter" in params, "Missing parameter 'templateParameter'"
    assert "owningTemplateParameter" in params, "Missing parameter 'owningTemplateParameter'"

def test_umlmodel::parameterableelement_has_templateParameter():
    assert hasattr(UMLModel::ParameterableElement, "templateParameter")
    descriptor = None
    for klass in UMLModel::ParameterableElement.__mro__:
        if "templateParameter" in klass.__dict__:
            descriptor = klass.__dict__["templateParameter"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::parameterableelement_has_owningTemplateParameter():
    assert hasattr(UMLModel::ParameterableElement, "owningTemplateParameter")
    descriptor = None
    for klass in UMLModel::ParameterableElement.__mro__:
        if "owningTemplateParameter" in klass.__dict__:
            descriptor = klass.__dict__["owningTemplateParameter"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::relationship_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Relationship)


def test_umlmodel::relationship_constructor_exists():
    assert callable(UMLModel::Relationship.__init__)


def test_umlmodel::relationship_constructor_args():
    sig = inspect.signature(UMLModel::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "relatedElement" in params, "Missing parameter 'relatedElement'"

def test_umlmodel::relationship_has_relatedElement():
    assert hasattr(UMLModel::Relationship, "relatedElement")
    descriptor = None
    for klass in UMLModel::Relationship.__mro__:
        if "relatedElement" in klass.__dict__:
            descriptor = klass.__dict__["relatedElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::MultiplicityElement)


def test_umlmodel::multiplicityelement_constructor_exists():
    assert callable(UMLModel::MultiplicityElement.__init__)


def test_umlmodel::multiplicityelement_constructor_args():
    sig = inspect.signature(UMLModel::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_umlmodel::multiplicityelement_has_isOrdered():
    assert hasattr(UMLModel::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in UMLModel::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::multiplicityelement_has_isUnique():
    assert hasattr(UMLModel::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in UMLModel::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::multiplicityelement_has_upper():
    assert hasattr(UMLModel::MultiplicityElement, "upper")
    descriptor = None
    for klass in UMLModel::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::multiplicityelement_has_lower():
    assert hasattr(UMLModel::MultiplicityElement, "lower")
    descriptor = None
    for klass in UMLModel::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::linkenddata_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LinkEndData)


def test_umlmodel::linkenddata_constructor_exists():
    assert callable(UMLModel::LinkEndData.__init__)


def test_umlmodel::linkenddata_constructor_args():
    sig = inspect.signature(UMLModel::LinkEndData.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel::linkenddata_has_end():
    assert hasattr(UMLModel::LinkEndData, "end")
    descriptor = None
    for klass in UMLModel::LinkEndData.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::linkenddata_has_value():
    assert hasattr(UMLModel::LinkEndData, "value")
    descriptor = None
    for klass in UMLModel::LinkEndData.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::image_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Image)


def test_umlmodel::image_constructor_exists():
    assert callable(UMLModel::Image.__init__)


def test_umlmodel::image_constructor_args():
    sig = inspect.signature(UMLModel::Image.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "format" in params, "Missing parameter 'format'"
    assert "content" in params, "Missing parameter 'content'"

def test_umlmodel::image_has_location():
    assert hasattr(UMLModel::Image, "location")
    descriptor = None
    for klass in UMLModel::Image.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::image_has_format():
    assert hasattr(UMLModel::Image, "format")
    descriptor = None
    for klass in UMLModel::Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::image_has_content():
    assert hasattr(UMLModel::Image, "content")
    descriptor = None
    for klass in UMLModel::Image.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::slot_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Slot)


def test_umlmodel::slot_constructor_exists():
    assert callable(UMLModel::Slot.__init__)


def test_umlmodel::slot_constructor_args():
    sig = inspect.signature(UMLModel::Slot.__init__)
    params = list(sig.parameters.keys())
    assert "definingFeature" in params, "Missing parameter 'definingFeature'"
    assert "owningInstance" in params, "Missing parameter 'owningInstance'"

def test_umlmodel::slot_has_definingFeature():
    assert hasattr(UMLModel::Slot, "definingFeature")
    descriptor = None
    for klass in UMLModel::Slot.__mro__:
        if "definingFeature" in klass.__dict__:
            descriptor = klass.__dict__["definingFeature"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::slot_has_owningInstance():
    assert hasattr(UMLModel::Slot, "owningInstance")
    descriptor = None
    for klass in UMLModel::Slot.__mro__:
        if "owningInstance" in klass.__dict__:
            descriptor = klass.__dict__["owningInstance"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::templatesignature_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TemplateSignature)


def test_umlmodel::templatesignature_constructor_exists():
    assert callable(UMLModel::TemplateSignature.__init__)


def test_umlmodel::templatesignature_constructor_args():
    sig = inspect.signature(UMLModel::TemplateSignature.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "template" in params, "Missing parameter 'template'"

def test_umlmodel::templatesignature_has_parameter():
    assert hasattr(UMLModel::TemplateSignature, "parameter")
    descriptor = None
    for klass in UMLModel::TemplateSignature.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::templatesignature_has_template():
    assert hasattr(UMLModel::TemplateSignature, "template")
    descriptor = None
    for klass in UMLModel::TemplateSignature.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::namedelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::NamedElement)


def test_umlmodel::namedelement_constructor_exists():
    assert callable(UMLModel::NamedElement.__init__)


def test_umlmodel::namedelement_constructor_args():
    sig = inspect.signature(UMLModel::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "clientDependency" in params, "Missing parameter 'clientDependency'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "name" in params, "Missing parameter 'name'"

def test_umlmodel::namedelement_has_visibility():
    assert hasattr(UMLModel::NamedElement, "visibility")
    descriptor = None
    for klass in UMLModel::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::namedelement_has_namespace():
    assert hasattr(UMLModel::NamedElement, "namespace")
    descriptor = None
    for klass in UMLModel::NamedElement.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::namedelement_has_clientDependency():
    assert hasattr(UMLModel::NamedElement, "clientDependency")
    descriptor = None
    for klass in UMLModel::NamedElement.__mro__:
        if "clientDependency" in klass.__dict__:
            descriptor = klass.__dict__["clientDependency"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::namedelement_has_qualifiedName():
    assert hasattr(UMLModel::NamedElement, "qualifiedName")
    descriptor = None
    for klass in UMLModel::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::namedelement_has_name():
    assert hasattr(UMLModel::NamedElement, "name")
    descriptor = None
    for klass in UMLModel::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::templateableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TemplateableElement)


def test_umlmodel::templateableelement_constructor_exists():
    assert callable(UMLModel::TemplateableElement.__init__)


def test_umlmodel::templateableelement_constructor_args():
    sig = inspect.signature(UMLModel::TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::templateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TemplateParameter)


def test_umlmodel::templateparameter_constructor_exists():
    assert callable(UMLModel::TemplateParameter.__init__)


def test_umlmodel::templateparameter_constructor_args():
    sig = inspect.signature(UMLModel::TemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameteredElement" in params, "Missing parameter 'parameteredElement'"
    assert "default" in params, "Missing parameter 'default'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_umlmodel::templateparameter_has_parameteredElement():
    assert hasattr(UMLModel::TemplateParameter, "parameteredElement")
    descriptor = None
    for klass in UMLModel::TemplateParameter.__mro__:
        if "parameteredElement" in klass.__dict__:
            descriptor = klass.__dict__["parameteredElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::templateparameter_has_default():
    assert hasattr(UMLModel::TemplateParameter, "default")
    descriptor = None
    for klass in UMLModel::TemplateParameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::templateparameter_has_signature():
    assert hasattr(UMLModel::TemplateParameter, "signature")
    descriptor = None
    for klass in UMLModel::TemplateParameter.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(UMLModel::QualifierValue)


def test_umlmodel::qualifiervalue_constructor_exists():
    assert callable(UMLModel::QualifierValue.__init__)


def test_umlmodel::qualifiervalue_constructor_args():
    sig = inspect.signature(UMLModel::QualifierValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_umlmodel::qualifiervalue_has_value():
    assert hasattr(UMLModel::QualifierValue, "value")
    descriptor = None
    for klass in UMLModel::QualifierValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::qualifiervalue_has_qualifier():
    assert hasattr(UMLModel::QualifierValue, "qualifier")
    descriptor = None
    for klass in UMLModel::QualifierValue.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExceptionHandler)


def test_umlmodel::exceptionhandler_constructor_exists():
    assert callable(UMLModel::ExceptionHandler.__init__)


def test_umlmodel::exceptionhandler_constructor_args():
    sig = inspect.signature(UMLModel::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionInput" in params, "Missing parameter 'exceptionInput'"
    assert "handlerBody" in params, "Missing parameter 'handlerBody'"
    assert "exceptionType" in params, "Missing parameter 'exceptionType'"
    assert "protectedNode" in params, "Missing parameter 'protectedNode'"

def test_umlmodel::exceptionhandler_has_exceptionInput():
    assert hasattr(UMLModel::ExceptionHandler, "exceptionInput")
    descriptor = None
    for klass in UMLModel::ExceptionHandler.__mro__:
        if "exceptionInput" in klass.__dict__:
            descriptor = klass.__dict__["exceptionInput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::exceptionhandler_has_handlerBody():
    assert hasattr(UMLModel::ExceptionHandler, "handlerBody")
    descriptor = None
    for klass in UMLModel::ExceptionHandler.__mro__:
        if "handlerBody" in klass.__dict__:
            descriptor = klass.__dict__["handlerBody"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::exceptionhandler_has_exceptionType():
    assert hasattr(UMLModel::ExceptionHandler, "exceptionType")
    descriptor = None
    for klass in UMLModel::ExceptionHandler.__mro__:
        if "exceptionType" in klass.__dict__:
            descriptor = klass.__dict__["exceptionType"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::exceptionhandler_has_protectedNode():
    assert hasattr(UMLModel::ExceptionHandler, "protectedNode")
    descriptor = None
    for klass in UMLModel::ExceptionHandler.__mro__:
        if "protectedNode" in klass.__dict__:
            descriptor = klass.__dict__["protectedNode"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TemplateParameterSubstitution)


def test_umlmodel::templateparametersubstitution_constructor_exists():
    assert callable(UMLModel::TemplateParameterSubstitution.__init__)


def test_umlmodel::templateparametersubstitution_constructor_args():
    sig = inspect.signature(UMLModel::TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"
    assert "actual" in params, "Missing parameter 'actual'"
    assert "templateBinding" in params, "Missing parameter 'templateBinding'"

def test_umlmodel::templateparametersubstitution_has_formal():
    assert hasattr(UMLModel::TemplateParameterSubstitution, "formal")
    descriptor = None
    for klass in UMLModel::TemplateParameterSubstitution.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::templateparametersubstitution_has_actual():
    assert hasattr(UMLModel::TemplateParameterSubstitution, "actual")
    descriptor = None
    for klass in UMLModel::TemplateParameterSubstitution.__mro__:
        if "actual" in klass.__dict__:
            descriptor = klass.__dict__["actual"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::templateparametersubstitution_has_templateBinding():
    assert hasattr(UMLModel::TemplateParameterSubstitution, "templateBinding")
    descriptor = None
    for klass in UMLModel::TemplateParameterSubstitution.__mro__:
        if "templateBinding" in klass.__dict__:
            descriptor = klass.__dict__["templateBinding"]
            break
    assert isinstance(descriptor, property)



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::FlowFinalNode)


def test_umlmodel::flowfinalnode_constructor_exists():
    assert callable(UMLModel::FlowFinalNode.__init__)


def test_umlmodel::flowfinalnode_constructor_args():
    sig = inspect.signature(UMLModel::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActivityFinalNode)


def test_umlmodel::activityfinalnode_constructor_exists():
    assert callable(UMLModel::ActivityFinalNode.__init__)


def test_umlmodel::activityfinalnode_constructor_args():
    sig = inspect.signature(UMLModel::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::expansionnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExpansionNode)


def test_umlmodel::expansionnode_constructor_exists():
    assert callable(UMLModel::ExpansionNode.__init__)


def test_umlmodel::expansionnode_constructor_args():
    sig = inspect.signature(UMLModel::ExpansionNode.__init__)
    params = list(sig.parameters.keys())
    assert "regionAsOutput" in params, "Missing parameter 'regionAsOutput'"
    assert "regionAsInput" in params, "Missing parameter 'regionAsInput'"

def test_umlmodel::expansionnode_has_regionAsOutput():
    assert hasattr(UMLModel::ExpansionNode, "regionAsOutput")
    descriptor = None
    for klass in UMLModel::ExpansionNode.__mro__:
        if "regionAsOutput" in klass.__dict__:
            descriptor = klass.__dict__["regionAsOutput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::expansionnode_has_regionAsInput():
    assert hasattr(UMLModel::ExpansionNode, "regionAsInput")
    descriptor = None
    for klass in UMLModel::ExpansionNode.__mro__:
        if "regionAsInput" in klass.__dict__:
            descriptor = klass.__dict__["regionAsInput"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActivityParameterNode)


def test_umlmodel::activityparameternode_constructor_exists():
    assert callable(UMLModel::ActivityParameterNode.__init__)


def test_umlmodel::activityparameternode_constructor_args():
    sig = inspect.signature(UMLModel::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_umlmodel::activityparameternode_has_parameter():
    assert hasattr(UMLModel::ActivityParameterNode, "parameter")
    descriptor = None
    for klass in UMLModel::ActivityParameterNode.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::feature_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Feature)


def test_umlmodel::feature_constructor_exists():
    assert callable(UMLModel::Feature.__init__)


def test_umlmodel::feature_constructor_args():
    sig = inspect.signature(UMLModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "featuringClassifier" in params, "Missing parameter 'featuringClassifier'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_umlmodel::feature_has_featuringClassifier():
    assert hasattr(UMLModel::Feature, "featuringClassifier")
    descriptor = None
    for klass in UMLModel::Feature.__mro__:
        if "featuringClassifier" in klass.__dict__:
            descriptor = klass.__dict__["featuringClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::feature_has_isStatic():
    assert hasattr(UMLModel::Feature, "isStatic")
    descriptor = None
    for klass in UMLModel::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(UMLModel::RedefinableTemplateSignature)


def test_umlmodel::redefinabletemplatesignature_constructor_exists():
    assert callable(UMLModel::RedefinableTemplateSignature.__init__)


def test_umlmodel::redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(UMLModel::RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())
    assert "extendedSignature" in params, "Missing parameter 'extendedSignature'"
    assert "classifier" in params, "Missing parameter 'classifier'"
    assert "inheritedParameter" in params, "Missing parameter 'inheritedParameter'"

def test_umlmodel::redefinabletemplatesignature_has_extendedSignature():
    assert hasattr(UMLModel::RedefinableTemplateSignature, "extendedSignature")
    descriptor = None
    for klass in UMLModel::RedefinableTemplateSignature.__mro__:
        if "extendedSignature" in klass.__dict__:
            descriptor = klass.__dict__["extendedSignature"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::redefinabletemplatesignature_has_classifier():
    assert hasattr(UMLModel::RedefinableTemplateSignature, "classifier")
    descriptor = None
    for klass in UMLModel::RedefinableTemplateSignature.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::redefinabletemplatesignature_has_inheritedParameter():
    assert hasattr(UMLModel::RedefinableTemplateSignature, "inheritedParameter")
    descriptor = None
    for klass in UMLModel::RedefinableTemplateSignature.__mro__:
        if "inheritedParameter" in klass.__dict__:
            descriptor = klass.__dict__["inheritedParameter"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExtensionPoint)


def test_umlmodel::extensionpoint_constructor_exists():
    assert callable(UMLModel::ExtensionPoint.__init__)


def test_umlmodel::extensionpoint_constructor_args():
    sig = inspect.signature(UMLModel::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "useCase" in params, "Missing parameter 'useCase'"

def test_umlmodel::extensionpoint_has_useCase():
    assert hasattr(UMLModel::ExtensionPoint, "useCase")
    descriptor = None
    for klass in UMLModel::ExtensionPoint.__mro__:
        if "useCase" in klass.__dict__:
            descriptor = klass.__dict__["useCase"]
            break
    assert isinstance(descriptor, property)



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InterruptibleActivityRegion)


def test_umlmodel::interruptibleactivityregion_constructor_exists():
    assert callable(UMLModel::InterruptibleActivityRegion.__init__)


def test_umlmodel::interruptibleactivityregion_constructor_args():
    sig = inspect.signature(UMLModel::InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())
    assert "node" in params, "Missing parameter 'node'"
    assert "interruptingEdge" in params, "Missing parameter 'interruptingEdge'"

def test_umlmodel::interruptibleactivityregion_has_node():
    assert hasattr(UMLModel::InterruptibleActivityRegion, "node")
    descriptor = None
    for klass in UMLModel::InterruptibleActivityRegion.__mro__:
        if "node" in klass.__dict__:
            descriptor = klass.__dict__["node"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::interruptibleactivityregion_has_interruptingEdge():
    assert hasattr(UMLModel::InterruptibleActivityRegion, "interruptingEdge")
    descriptor = None
    for klass in UMLModel::InterruptibleActivityRegion.__mro__:
        if "interruptingEdge" in klass.__dict__:
            descriptor = klass.__dict__["interruptingEdge"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::typedelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TypedElement)


def test_umlmodel::typedelement_constructor_exists():
    assert callable(UMLModel::TypedElement.__init__)


def test_umlmodel::typedelement_constructor_args():
    sig = inspect.signature(UMLModel::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_umlmodel::typedelement_has_type():
    assert hasattr(UMLModel::TypedElement, "type")
    descriptor = None
    for klass in UMLModel::TypedElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InteractionFragment)


def test_umlmodel::interactionfragment_constructor_exists():
    assert callable(UMLModel::InteractionFragment.__init__)


def test_umlmodel::interactionfragment_constructor_args():
    sig = inspect.signature(UMLModel::InteractionFragment.__init__)
    params = list(sig.parameters.keys())
    assert "enclosingOperand" in params, "Missing parameter 'enclosingOperand'"
    assert "enclosingInteraction" in params, "Missing parameter 'enclosingInteraction'"
    assert "covered" in params, "Missing parameter 'covered'"

def test_umlmodel::interactionfragment_has_enclosingOperand():
    assert hasattr(UMLModel::InteractionFragment, "enclosingOperand")
    descriptor = None
    for klass in UMLModel::InteractionFragment.__mro__:
        if "enclosingOperand" in klass.__dict__:
            descriptor = klass.__dict__["enclosingOperand"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::interactionfragment_has_enclosingInteraction():
    assert hasattr(UMLModel::InteractionFragment, "enclosingInteraction")
    descriptor = None
    for klass in UMLModel::InteractionFragment.__mro__:
        if "enclosingInteraction" in klass.__dict__:
            descriptor = klass.__dict__["enclosingInteraction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::interactionfragment_has_covered():
    assert hasattr(UMLModel::InteractionFragment, "covered")
    descriptor = None
    for klass in UMLModel::InteractionFragment.__mro__:
        if "covered" in klass.__dict__:
            descriptor = klass.__dict__["covered"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::vertex_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Vertex)


def test_umlmodel::vertex_constructor_exists():
    assert callable(UMLModel::Vertex.__init__)


def test_umlmodel::vertex_constructor_args():
    sig = inspect.signature(UMLModel::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "outgoing" in params, "Missing parameter 'outgoing'"
    assert "incoming" in params, "Missing parameter 'incoming'"
    assert "container" in params, "Missing parameter 'container'"

def test_umlmodel::vertex_has_outgoing():
    assert hasattr(UMLModel::Vertex, "outgoing")
    descriptor = None
    for klass in UMLModel::Vertex.__mro__:
        if "outgoing" in klass.__dict__:
            descriptor = klass.__dict__["outgoing"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::vertex_has_incoming():
    assert hasattr(UMLModel::Vertex, "incoming")
    descriptor = None
    for klass in UMLModel::Vertex.__mro__:
        if "incoming" in klass.__dict__:
            descriptor = klass.__dict__["incoming"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::vertex_has_container():
    assert hasattr(UMLModel::Vertex, "container")
    descriptor = None
    for klass in UMLModel::Vertex.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::generalordering_is_not_abstract():
    assert not inspect.isabstract(UMLModel::GeneralOrdering)


def test_umlmodel::generalordering_constructor_exists():
    assert callable(UMLModel::GeneralOrdering.__init__)


def test_umlmodel::generalordering_constructor_args():
    sig = inspect.signature(UMLModel::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())
    assert "before" in params, "Missing parameter 'before'"
    assert "after" in params, "Missing parameter 'after'"

def test_umlmodel::generalordering_has_before():
    assert hasattr(UMLModel::GeneralOrdering, "before")
    descriptor = None
    for klass in UMLModel::GeneralOrdering.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::generalordering_has_after():
    assert hasattr(UMLModel::GeneralOrdering, "after")
    descriptor = None
    for klass in UMLModel::GeneralOrdering.__mro__:
        if "after" in klass.__dict__:
            descriptor = klass.__dict__["after"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::namespace_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Namespace)


def test_umlmodel::namespace_constructor_exists():
    assert callable(UMLModel::Namespace.__init__)


def test_umlmodel::namespace_constructor_args():
    sig = inspect.signature(UMLModel::Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "ownedMember" in params, "Missing parameter 'ownedMember'"
    assert "importedMember" in params, "Missing parameter 'importedMember'"
    assert "member" in params, "Missing parameter 'member'"

def test_umlmodel::namespace_has_ownedMember():
    assert hasattr(UMLModel::Namespace, "ownedMember")
    descriptor = None
    for klass in UMLModel::Namespace.__mro__:
        if "ownedMember" in klass.__dict__:
            descriptor = klass.__dict__["ownedMember"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::namespace_has_importedMember():
    assert hasattr(UMLModel::Namespace, "importedMember")
    descriptor = None
    for klass in UMLModel::Namespace.__mro__:
        if "importedMember" in klass.__dict__:
            descriptor = klass.__dict__["importedMember"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::namespace_has_member():
    assert hasattr(UMLModel::Namespace, "member")
    descriptor = None
    for klass in UMLModel::Namespace.__mro__:
        if "member" in klass.__dict__:
            descriptor = klass.__dict__["member"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::RedefinableElement)


def test_umlmodel::redefinableelement_constructor_exists():
    assert callable(UMLModel::RedefinableElement.__init__)


def test_umlmodel::redefinableelement_constructor_args():
    sig = inspect.signature(UMLModel::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"
    assert "redefinedElement" in params, "Missing parameter 'redefinedElement'"
    assert "redefinitionContext" in params, "Missing parameter 'redefinitionContext'"

def test_umlmodel::redefinableelement_has_isLeaf():
    assert hasattr(UMLModel::RedefinableElement, "isLeaf")
    descriptor = None
    for klass in UMLModel::RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::redefinableelement_has_redefinedElement():
    assert hasattr(UMLModel::RedefinableElement, "redefinedElement")
    descriptor = None
    for klass in UMLModel::RedefinableElement.__mro__:
        if "redefinedElement" in klass.__dict__:
            descriptor = klass.__dict__["redefinedElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::redefinableelement_has_redefinitionContext():
    assert hasattr(UMLModel::RedefinableElement, "redefinitionContext")
    descriptor = None
    for klass in UMLModel::RedefinableElement.__mro__:
        if "redefinitionContext" in klass.__dict__:
            descriptor = klass.__dict__["redefinitionContext"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::lifeline_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Lifeline)


def test_umlmodel::lifeline_constructor_exists():
    assert callable(UMLModel::Lifeline.__init__)


def test_umlmodel::lifeline_constructor_args():
    sig = inspect.signature(UMLModel::Lifeline.__init__)
    params = list(sig.parameters.keys())
    assert "interaction" in params, "Missing parameter 'interaction'"
    assert "decomposedAs" in params, "Missing parameter 'decomposedAs'"
    assert "coveredBy" in params, "Missing parameter 'coveredBy'"
    assert "represents" in params, "Missing parameter 'represents'"

def test_umlmodel::lifeline_has_interaction():
    assert hasattr(UMLModel::Lifeline, "interaction")
    descriptor = None
    for klass in UMLModel::Lifeline.__mro__:
        if "interaction" in klass.__dict__:
            descriptor = klass.__dict__["interaction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::lifeline_has_decomposedAs():
    assert hasattr(UMLModel::Lifeline, "decomposedAs")
    descriptor = None
    for klass in UMLModel::Lifeline.__mro__:
        if "decomposedAs" in klass.__dict__:
            descriptor = klass.__dict__["decomposedAs"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::lifeline_has_coveredBy():
    assert hasattr(UMLModel::Lifeline, "coveredBy")
    descriptor = None
    for klass in UMLModel::Lifeline.__mro__:
        if "coveredBy" in klass.__dict__:
            descriptor = klass.__dict__["coveredBy"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::lifeline_has_represents():
    assert hasattr(UMLModel::Lifeline, "represents")
    descriptor = None
    for klass in UMLModel::Lifeline.__mro__:
        if "represents" in klass.__dict__:
            descriptor = klass.__dict__["represents"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::messageend_is_not_abstract():
    assert not inspect.isabstract(UMLModel::MessageEnd)


def test_umlmodel::messageend_constructor_exists():
    assert callable(UMLModel::MessageEnd.__init__)


def test_umlmodel::messageend_constructor_args():
    sig = inspect.signature(UMLModel::MessageEnd.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_umlmodel::messageend_has_message():
    assert hasattr(UMLModel::MessageEnd, "message")
    descriptor = None
    for klass in UMLModel::MessageEnd.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::message_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Message)


def test_umlmodel::message_constructor_exists():
    assert callable(UMLModel::Message.__init__)


def test_umlmodel::message_constructor_args():
    sig = inspect.signature(UMLModel::Message.__init__)
    params = list(sig.parameters.keys())
    assert "sendEvent" in params, "Missing parameter 'sendEvent'"
    assert "interaction" in params, "Missing parameter 'interaction'"
    assert "messageKind" in params, "Missing parameter 'messageKind'"
    assert "connector" in params, "Missing parameter 'connector'"
    assert "messageSort" in params, "Missing parameter 'messageSort'"
    assert "receiveEvent" in params, "Missing parameter 'receiveEvent'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_umlmodel::message_has_sendEvent():
    assert hasattr(UMLModel::Message, "sendEvent")
    descriptor = None
    for klass in UMLModel::Message.__mro__:
        if "sendEvent" in klass.__dict__:
            descriptor = klass.__dict__["sendEvent"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::message_has_interaction():
    assert hasattr(UMLModel::Message, "interaction")
    descriptor = None
    for klass in UMLModel::Message.__mro__:
        if "interaction" in klass.__dict__:
            descriptor = klass.__dict__["interaction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::message_has_messageKind():
    assert hasattr(UMLModel::Message, "messageKind")
    descriptor = None
    for klass in UMLModel::Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::message_has_connector():
    assert hasattr(UMLModel::Message, "connector")
    descriptor = None
    for klass in UMLModel::Message.__mro__:
        if "connector" in klass.__dict__:
            descriptor = klass.__dict__["connector"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::message_has_messageSort():
    assert hasattr(UMLModel::Message, "messageSort")
    descriptor = None
    for klass in UMLModel::Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::message_has_receiveEvent():
    assert hasattr(UMLModel::Message, "receiveEvent")
    descriptor = None
    for klass in UMLModel::Message.__mro__:
        if "receiveEvent" in klass.__dict__:
            descriptor = klass.__dict__["receiveEvent"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::message_has_signature():
    assert hasattr(UMLModel::Message, "signature")
    descriptor = None
    for klass in UMLModel::Message.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::activitypartition_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActivityPartition)


def test_umlmodel::activitypartition_constructor_exists():
    assert callable(UMLModel::ActivityPartition.__init__)


def test_umlmodel::activitypartition_constructor_args():
    sig = inspect.signature(UMLModel::ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "node" in params, "Missing parameter 'node'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "isDimension" in params, "Missing parameter 'isDimension'"
    assert "superPartition" in params, "Missing parameter 'superPartition'"
    assert "represents" in params, "Missing parameter 'represents'"
    assert "edge" in params, "Missing parameter 'edge'"
    assert "subpartition" in params, "Missing parameter 'subpartition'"

def test_umlmodel::activitypartition_has_node():
    assert hasattr(UMLModel::ActivityPartition, "node")
    descriptor = None
    for klass in UMLModel::ActivityPartition.__mro__:
        if "node" in klass.__dict__:
            descriptor = klass.__dict__["node"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitypartition_has_isExternal():
    assert hasattr(UMLModel::ActivityPartition, "isExternal")
    descriptor = None
    for klass in UMLModel::ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitypartition_has_isDimension():
    assert hasattr(UMLModel::ActivityPartition, "isDimension")
    descriptor = None
    for klass in UMLModel::ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitypartition_has_superPartition():
    assert hasattr(UMLModel::ActivityPartition, "superPartition")
    descriptor = None
    for klass in UMLModel::ActivityPartition.__mro__:
        if "superPartition" in klass.__dict__:
            descriptor = klass.__dict__["superPartition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitypartition_has_represents():
    assert hasattr(UMLModel::ActivityPartition, "represents")
    descriptor = None
    for klass in UMLModel::ActivityPartition.__mro__:
        if "represents" in klass.__dict__:
            descriptor = klass.__dict__["represents"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitypartition_has_edge():
    assert hasattr(UMLModel::ActivityPartition, "edge")
    descriptor = None
    for klass in UMLModel::ActivityPartition.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitypartition_has_subpartition():
    assert hasattr(UMLModel::ActivityPartition, "subpartition")
    descriptor = None
    for klass in UMLModel::ActivityPartition.__mro__:
        if "subpartition" in klass.__dict__:
            descriptor = klass.__dict__["subpartition"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::activitynode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActivityNode)


def test_umlmodel::activitynode_constructor_exists():
    assert callable(UMLModel::ActivityNode.__init__)


def test_umlmodel::activitynode_constructor_args():
    sig = inspect.signature(UMLModel::ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "inStructuredNode" in params, "Missing parameter 'inStructuredNode'"
    assert "inGroup" in params, "Missing parameter 'inGroup'"
    assert "inPartition" in params, "Missing parameter 'inPartition'"
    assert "redefinedNode" in params, "Missing parameter 'redefinedNode'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "outgoing" in params, "Missing parameter 'outgoing'"
    assert "incoming" in params, "Missing parameter 'incoming'"
    assert "inInterruptibleRegion" in params, "Missing parameter 'inInterruptibleRegion'"

def test_umlmodel::activitynode_has_inStructuredNode():
    assert hasattr(UMLModel::ActivityNode, "inStructuredNode")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "inStructuredNode" in klass.__dict__:
            descriptor = klass.__dict__["inStructuredNode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitynode_has_inGroup():
    assert hasattr(UMLModel::ActivityNode, "inGroup")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "inGroup" in klass.__dict__:
            descriptor = klass.__dict__["inGroup"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitynode_has_inPartition():
    assert hasattr(UMLModel::ActivityNode, "inPartition")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "inPartition" in klass.__dict__:
            descriptor = klass.__dict__["inPartition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitynode_has_redefinedNode():
    assert hasattr(UMLModel::ActivityNode, "redefinedNode")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "redefinedNode" in klass.__dict__:
            descriptor = klass.__dict__["redefinedNode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitynode_has_activity():
    assert hasattr(UMLModel::ActivityNode, "activity")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitynode_has_outgoing():
    assert hasattr(UMLModel::ActivityNode, "outgoing")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "outgoing" in klass.__dict__:
            descriptor = klass.__dict__["outgoing"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitynode_has_incoming():
    assert hasattr(UMLModel::ActivityNode, "incoming")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "incoming" in klass.__dict__:
            descriptor = klass.__dict__["incoming"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitynode_has_inInterruptibleRegion():
    assert hasattr(UMLModel::ActivityNode, "inInterruptibleRegion")
    descriptor = None
    for klass in UMLModel::ActivityNode.__mro__:
        if "inInterruptibleRegion" in klass.__dict__:
            descriptor = klass.__dict__["inInterruptibleRegion"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::statemachine_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StateMachine)


def test_umlmodel::statemachine_constructor_exists():
    assert callable(UMLModel::StateMachine.__init__)


def test_umlmodel::statemachine_constructor_args():
    sig = inspect.signature(UMLModel::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "extendedStateMachine" in params, "Missing parameter 'extendedStateMachine'"
    assert "submachineState" in params, "Missing parameter 'submachineState'"

def test_umlmodel::statemachine_has_extendedStateMachine():
    assert hasattr(UMLModel::StateMachine, "extendedStateMachine")
    descriptor = None
    for klass in UMLModel::StateMachine.__mro__:
        if "extendedStateMachine" in klass.__dict__:
            descriptor = klass.__dict__["extendedStateMachine"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::statemachine_has_submachineState():
    assert hasattr(UMLModel::StateMachine, "submachineState")
    descriptor = None
    for klass in UMLModel::StateMachine.__mro__:
        if "submachineState" in klass.__dict__:
            descriptor = klass.__dict__["submachineState"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(UMLModel::OpaqueBehavior)


def test_umlmodel::opaquebehavior_constructor_exists():
    assert callable(UMLModel::OpaqueBehavior.__init__)


def test_umlmodel::opaquebehavior_constructor_args():
    sig = inspect.signature(UMLModel::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_umlmodel::opaquebehavior_has_language():
    assert hasattr(UMLModel::OpaqueBehavior, "language")
    descriptor = None
    for klass in UMLModel::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::opaquebehavior_has_body():
    assert hasattr(UMLModel::OpaqueBehavior, "body")
    descriptor = None
    for klass in UMLModel::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::activity_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Activity)


def test_umlmodel::activity_constructor_exists():
    assert callable(UMLModel::Activity.__init__)


def test_umlmodel::activity_constructor_args():
    sig = inspect.signature(UMLModel::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "partition" in params, "Missing parameter 'partition'"
    assert "structuredNode" in params, "Missing parameter 'structuredNode'"

def test_umlmodel::activity_has_isSingleExecution():
    assert hasattr(UMLModel::Activity, "isSingleExecution")
    descriptor = None
    for klass in UMLModel::Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activity_has_isReadOnly():
    assert hasattr(UMLModel::Activity, "isReadOnly")
    descriptor = None
    for klass in UMLModel::Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activity_has_partition():
    assert hasattr(UMLModel::Activity, "partition")
    descriptor = None
    for klass in UMLModel::Activity.__mro__:
        if "partition" in klass.__dict__:
            descriptor = klass.__dict__["partition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activity_has_structuredNode():
    assert hasattr(UMLModel::Activity, "structuredNode")
    descriptor = None
    for klass in UMLModel::Activity.__mro__:
        if "structuredNode" in klass.__dict__:
            descriptor = klass.__dict__["structuredNode"]
            break
    assert isinstance(descriptor, property)



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::valuepin_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ValuePin)


def test_umlmodel::valuepin_constructor_exists():
    assert callable(UMLModel::ValuePin.__init__)


def test_umlmodel::valuepin_constructor_args():
    sig = inspect.signature(UMLModel::ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::actioninputpin_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActionInputPin)


def test_umlmodel::actioninputpin_constructor_exists():
    assert callable(UMLModel::ActionInputPin.__init__)


def test_umlmodel::actioninputpin_constructor_args():
    sig = inspect.signature(UMLModel::ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActionExecutionSpecification)


def test_umlmodel::actionexecutionspecification_constructor_exists():
    assert callable(UMLModel::ActionExecutionSpecification.__init__)


def test_umlmodel::actionexecutionspecification_constructor_args():
    sig = inspect.signature(UMLModel::ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_umlmodel::actionexecutionspecification_has_action():
    assert hasattr(UMLModel::ActionExecutionSpecification, "action")
    descriptor = None
    for klass in UMLModel::ActionExecutionSpecification.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::activitygroup_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActivityGroup)


def test_umlmodel::activitygroup_constructor_exists():
    assert callable(UMLModel::ActivityGroup.__init__)


def test_umlmodel::activitygroup_constructor_args():
    sig = inspect.signature(UMLModel::ActivityGroup.__init__)
    params = list(sig.parameters.keys())
    assert "subgroup" in params, "Missing parameter 'subgroup'"
    assert "superGroup" in params, "Missing parameter 'superGroup'"
    assert "inActivity" in params, "Missing parameter 'inActivity'"

def test_umlmodel::activitygroup_has_subgroup():
    assert hasattr(UMLModel::ActivityGroup, "subgroup")
    descriptor = None
    for klass in UMLModel::ActivityGroup.__mro__:
        if "subgroup" in klass.__dict__:
            descriptor = klass.__dict__["subgroup"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitygroup_has_superGroup():
    assert hasattr(UMLModel::ActivityGroup, "superGroup")
    descriptor = None
    for klass in UMLModel::ActivityGroup.__mro__:
        if "superGroup" in klass.__dict__:
            descriptor = klass.__dict__["superGroup"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activitygroup_has_inActivity():
    assert hasattr(UMLModel::ActivityGroup, "inActivity")
    descriptor = None
    for klass in UMLModel::ActivityGroup.__mro__:
        if "inActivity" in klass.__dict__:
            descriptor = klass.__dict__["inActivity"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::activityedge_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ActivityEdge)


def test_umlmodel::activityedge_constructor_exists():
    assert callable(UMLModel::ActivityEdge.__init__)


def test_umlmodel::activityedge_constructor_args():
    sig = inspect.signature(UMLModel::ActivityEdge.__init__)
    params = list(sig.parameters.keys())
    assert "interrupts" in params, "Missing parameter 'interrupts'"
    assert "source" in params, "Missing parameter 'source'"
    assert "inGroup" in params, "Missing parameter 'inGroup'"
    assert "redefinedEdge" in params, "Missing parameter 'redefinedEdge'"
    assert "inPartition" in params, "Missing parameter 'inPartition'"
    assert "target" in params, "Missing parameter 'target'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "inStructuredNode" in params, "Missing parameter 'inStructuredNode'"

def test_umlmodel::activityedge_has_interrupts():
    assert hasattr(UMLModel::ActivityEdge, "interrupts")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "interrupts" in klass.__dict__:
            descriptor = klass.__dict__["interrupts"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activityedge_has_source():
    assert hasattr(UMLModel::ActivityEdge, "source")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activityedge_has_inGroup():
    assert hasattr(UMLModel::ActivityEdge, "inGroup")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "inGroup" in klass.__dict__:
            descriptor = klass.__dict__["inGroup"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activityedge_has_redefinedEdge():
    assert hasattr(UMLModel::ActivityEdge, "redefinedEdge")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "redefinedEdge" in klass.__dict__:
            descriptor = klass.__dict__["redefinedEdge"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activityedge_has_inPartition():
    assert hasattr(UMLModel::ActivityEdge, "inPartition")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "inPartition" in klass.__dict__:
            descriptor = klass.__dict__["inPartition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activityedge_has_target():
    assert hasattr(UMLModel::ActivityEdge, "target")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activityedge_has_activity():
    assert hasattr(UMLModel::ActivityEdge, "activity")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::activityedge_has_inStructuredNode():
    assert hasattr(UMLModel::ActivityEdge, "inStructuredNode")
    descriptor = None
    for klass in UMLModel::ActivityEdge.__mro__:
        if "inStructuredNode" in klass.__dict__:
            descriptor = klass.__dict__["inStructuredNode"]
            break
    assert isinstance(descriptor, property)



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::AcceptCallAction)


def test_umlmodel::acceptcallaction_constructor_exists():
    assert callable(UMLModel::AcceptCallAction.__init__)


def test_umlmodel::acceptcallaction_constructor_args():
    sig = inspect.signature(UMLModel::AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::usage_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Usage)


def test_umlmodel::usage_constructor_exists():
    assert callable(UMLModel::Usage.__init__)


def test_umlmodel::usage_constructor_args():
    sig = inspect.signature(UMLModel::Usage.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::abstraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Abstraction)


def test_umlmodel::abstraction_constructor_exists():
    assert callable(UMLModel::Abstraction.__init__)


def test_umlmodel::abstraction_constructor_args():
    sig = inspect.signature(UMLModel::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::action_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Action)


def test_umlmodel::action_constructor_exists():
    assert callable(UMLModel::Action.__init__)


def test_umlmodel::action_constructor_args():
    sig = inspect.signature(UMLModel::Action.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "context" in params, "Missing parameter 'context'"
    assert "output" in params, "Missing parameter 'output'"

def test_umlmodel::action_has_input():
    assert hasattr(UMLModel::Action, "input")
    descriptor = None
    for klass in UMLModel::Action.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::action_has_context():
    assert hasattr(UMLModel::Action, "context")
    descriptor = None
    for klass in UMLModel::Action.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::action_has_output():
    assert hasattr(UMLModel::Action, "output")
    descriptor = None
    for klass in UMLModel::Action.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::trigger_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Trigger)


def test_umlmodel::trigger_constructor_exists():
    assert callable(UMLModel::Trigger.__init__)


def test_umlmodel::trigger_constructor_args():
    sig = inspect.signature(UMLModel::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "port" in params, "Missing parameter 'port'"

def test_umlmodel::trigger_has_event():
    assert hasattr(UMLModel::Trigger, "event")
    descriptor = None
    for klass in UMLModel::Trigger.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::trigger_has_port():
    assert hasattr(UMLModel::Trigger, "port")
    descriptor = None
    for klass in UMLModel::Trigger.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::variableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::VariableAction)


def test_umlmodel::variableaction_constructor_exists():
    assert callable(UMLModel::VariableAction.__init__)


def test_umlmodel::variableaction_constructor_args():
    sig = inspect.signature(UMLModel::VariableAction.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_umlmodel::variableaction_has_variable():
    assert hasattr(UMLModel::VariableAction, "variable")
    descriptor = None
    for klass in UMLModel::VariableAction.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::UnmarshallAction)


def test_umlmodel::unmarshallaction_constructor_exists():
    assert callable(UMLModel::UnmarshallAction.__init__)


def test_umlmodel::unmarshallaction_constructor_args():
    sig = inspect.signature(UMLModel::UnmarshallAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshallType" in params, "Missing parameter 'unmarshallType'"

def test_umlmodel::unmarshallaction_has_unmarshallType():
    assert hasattr(UMLModel::UnmarshallAction, "unmarshallType")
    descriptor = None
    for klass in UMLModel::UnmarshallAction.__mro__:
        if "unmarshallType" in klass.__dict__:
            descriptor = klass.__dict__["unmarshallType"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TestIdentityAction)


def test_umlmodel::testidentityaction_constructor_exists():
    assert callable(UMLModel::TestIdentityAction.__init__)


def test_umlmodel::testidentityaction_constructor_args():
    sig = inspect.signature(UMLModel::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StartClassifierBehaviorAction)


def test_umlmodel::startclassifierbehavioraction_constructor_exists():
    assert callable(UMLModel::StartClassifierBehaviorAction.__init__)


def test_umlmodel::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(UMLModel::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::RaiseExceptionAction)


def test_umlmodel::raiseexceptionaction_constructor_exists():
    assert callable(UMLModel::RaiseExceptionAction.__init__)


def test_umlmodel::raiseexceptionaction_constructor_args():
    sig = inspect.signature(UMLModel::RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::readextentaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadExtentAction)


def test_umlmodel::readextentaction_constructor_exists():
    assert callable(UMLModel::ReadExtentAction.__init__)


def test_umlmodel::readextentaction_constructor_args():
    sig = inspect.signature(UMLModel::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel::readextentaction_has_classifier():
    assert hasattr(UMLModel::ReadExtentAction, "classifier")
    descriptor = None
    for klass in UMLModel::ReadExtentAction.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReclassifyObjectAction)


def test_umlmodel::reclassifyobjectaction_constructor_exists():
    assert callable(UMLModel::ReclassifyObjectAction.__init__)


def test_umlmodel::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UMLModel::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"
    assert "oldClassifier" in params, "Missing parameter 'oldClassifier'"
    assert "newClassifier" in params, "Missing parameter 'newClassifier'"

def test_umlmodel::reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(UMLModel::ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in UMLModel::ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::reclassifyobjectaction_has_oldClassifier():
    assert hasattr(UMLModel::ReclassifyObjectAction, "oldClassifier")
    descriptor = None
    for klass in UMLModel::ReclassifyObjectAction.__mro__:
        if "oldClassifier" in klass.__dict__:
            descriptor = klass.__dict__["oldClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::reclassifyobjectaction_has_newClassifier():
    assert hasattr(UMLModel::ReclassifyObjectAction, "newClassifier")
    descriptor = None
    for klass in UMLModel::ReclassifyObjectAction.__mro__:
        if "newClassifier" in klass.__dict__:
            descriptor = klass.__dict__["newClassifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::invocationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InvocationAction)


def test_umlmodel::invocationaction_constructor_exists():
    assert callable(UMLModel::InvocationAction.__init__)


def test_umlmodel::invocationaction_constructor_args():
    sig = inspect.signature(UMLModel::InvocationAction.__init__)
    params = list(sig.parameters.keys())
    assert "onPort" in params, "Missing parameter 'onPort'"

def test_umlmodel::invocationaction_has_onPort():
    assert hasattr(UMLModel::InvocationAction, "onPort")
    descriptor = None
    for klass in UMLModel::InvocationAction.__mro__:
        if "onPort" in klass.__dict__:
            descriptor = klass.__dict__["onPort"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadIsClassifiedObjectAction)


def test_umlmodel::readisclassifiedobjectaction_constructor_exists():
    assert callable(UMLModel::ReadIsClassifiedObjectAction.__init__)


def test_umlmodel::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UMLModel::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"
    assert "isDirect" in params, "Missing parameter 'isDirect'"

def test_umlmodel::readisclassifiedobjectaction_has_classifier():
    assert hasattr(UMLModel::ReadIsClassifiedObjectAction, "classifier")
    descriptor = None
    for klass in UMLModel::ReadIsClassifiedObjectAction.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::readisclassifiedobjectaction_has_isDirect():
    assert hasattr(UMLModel::ReadIsClassifiedObjectAction, "isDirect")
    descriptor = None
    for klass in UMLModel::ReadIsClassifiedObjectAction.__mro__:
        if "isDirect" in klass.__dict__:
            descriptor = klass.__dict__["isDirect"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadLinkObjectEndAction)


def test_umlmodel::readlinkobjectendaction_constructor_exists():
    assert callable(UMLModel::ReadLinkObjectEndAction.__init__)


def test_umlmodel::readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UMLModel::ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_umlmodel::readlinkobjectendaction_has_end():
    assert hasattr(UMLModel::ReadLinkObjectEndAction, "end")
    descriptor = None
    for klass in UMLModel::ReadLinkObjectEndAction.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadLinkObjectEndQualifierAction)


def test_umlmodel::readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UMLModel::ReadLinkObjectEndQualifierAction.__init__)


def test_umlmodel::readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UMLModel::ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_umlmodel::readlinkobjectendqualifieraction_has_qualifier():
    assert hasattr(UMLModel::ReadLinkObjectEndQualifierAction, "qualifier")
    descriptor = None
    for klass in UMLModel::ReadLinkObjectEndQualifierAction.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::OpaqueAction)


def test_umlmodel::opaqueaction_constructor_exists():
    assert callable(UMLModel::OpaqueAction.__init__)


def test_umlmodel::opaqueaction_constructor_args():
    sig = inspect.signature(UMLModel::OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_umlmodel::opaqueaction_has_body():
    assert hasattr(UMLModel::OpaqueAction, "body")
    descriptor = None
    for klass in UMLModel::OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::opaqueaction_has_language():
    assert hasattr(UMLModel::OpaqueAction, "language")
    descriptor = None
    for klass in UMLModel::OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::linkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LinkAction)


def test_umlmodel::linkaction_constructor_exists():
    assert callable(UMLModel::LinkAction.__init__)


def test_umlmodel::linkaction_constructor_args():
    sig = inspect.signature(UMLModel::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ValueSpecificationAction)


def test_umlmodel::valuespecificationaction_constructor_exists():
    assert callable(UMLModel::ValueSpecificationAction.__init__)


def test_umlmodel::valuespecificationaction_constructor_args():
    sig = inspect.signature(UMLModel::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::reduceaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReduceAction)


def test_umlmodel::reduceaction_constructor_exists():
    assert callable(UMLModel::ReduceAction.__init__)


def test_umlmodel::reduceaction_constructor_args():
    sig = inspect.signature(UMLModel::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "reducer" in params, "Missing parameter 'reducer'"

def test_umlmodel::reduceaction_has_isOrdered():
    assert hasattr(UMLModel::ReduceAction, "isOrdered")
    descriptor = None
    for klass in UMLModel::ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::reduceaction_has_reducer():
    assert hasattr(UMLModel::ReduceAction, "reducer")
    descriptor = None
    for klass in UMLModel::ReduceAction.__mro__:
        if "reducer" in klass.__dict__:
            descriptor = klass.__dict__["reducer"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::replyaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReplyAction)


def test_umlmodel::replyaction_constructor_exists():
    assert callable(UMLModel::ReplyAction.__init__)


def test_umlmodel::replyaction_constructor_args():
    sig = inspect.signature(UMLModel::ReplyAction.__init__)
    params = list(sig.parameters.keys())
    assert "replyToCall" in params, "Missing parameter 'replyToCall'"

def test_umlmodel::replyaction_has_replyToCall():
    assert hasattr(UMLModel::ReplyAction, "replyToCall")
    descriptor = None
    for klass in UMLModel::ReplyAction.__mro__:
        if "replyToCall" in klass.__dict__:
            descriptor = klass.__dict__["replyToCall"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StructuralFeatureAction)


def test_umlmodel::structuralfeatureaction_constructor_exists():
    assert callable(UMLModel::StructuralFeatureAction.__init__)


def test_umlmodel::structuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())
    assert "structuralFeature" in params, "Missing parameter 'structuralFeature'"

def test_umlmodel::structuralfeatureaction_has_structuralFeature():
    assert hasattr(UMLModel::StructuralFeatureAction, "structuralFeature")
    descriptor = None
    for klass in UMLModel::StructuralFeatureAction.__mro__:
        if "structuralFeature" in klass.__dict__:
            descriptor = klass.__dict__["structuralFeature"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::readselfaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadSelfAction)


def test_umlmodel::readselfaction_constructor_exists():
    assert callable(UMLModel::ReadSelfAction.__init__)


def test_umlmodel::readselfaction_constructor_args():
    sig = inspect.signature(UMLModel::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::AcceptEventAction)


def test_umlmodel::accepteventaction_constructor_exists():
    assert callable(UMLModel::AcceptEventAction.__init__)


def test_umlmodel::accepteventaction_constructor_args():
    sig = inspect.signature(UMLModel::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_umlmodel::accepteventaction_has_isUnmarshall():
    assert hasattr(UMLModel::AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in UMLModel::AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::outputpin_is_not_abstract():
    assert not inspect.isabstract(UMLModel::OutputPin)


def test_umlmodel::outputpin_constructor_exists():
    assert callable(UMLModel::OutputPin.__init__)


def test_umlmodel::outputpin_constructor_args():
    sig = inspect.signature(UMLModel::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_umlbase_is_not_abstract():
    assert not inspect.isabstract(UMLBase)


def test_umlbase_constructor_exists():
    assert callable(UMLBase.__init__)


def test_umlbase_constructor_args():
    sig = inspect.signature(UMLBase.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::element_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Element)


def test_umlmodel::element_constructor_exists():
    assert callable(UMLModel::Element.__init__)


def test_umlmodel::element_constructor_args():
    sig = inspect.signature(UMLModel::Element.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"
    assert "owner" in params, "Missing parameter 'owner'"
    assert "ownedElement" in params, "Missing parameter 'ownedElement'"

def test_umlmodel::element_has_href():
    assert hasattr(UMLModel::Element, "href")
    descriptor = None
    for klass in UMLModel::Element.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::element_has_owner():
    assert hasattr(UMLModel::Element, "owner")
    descriptor = None
    for klass in UMLModel::Element.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::element_has_ownedElement():
    assert hasattr(UMLModel::Element, "ownedElement")
    descriptor = None
    for klass in UMLModel::Element.__mro__:
        if "ownedElement" in klass.__dict__:
            descriptor = klass.__dict__["ownedElement"]
            break
    assert isinstance(descriptor, property)



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::timeobservation_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TimeObservation)


def test_umlmodel::timeobservation_constructor_exists():
    assert callable(UMLModel::TimeObservation.__init__)


def test_umlmodel::timeobservation_constructor_args():
    sig = inspect.signature(UMLModel::TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"
    assert "event" in params, "Missing parameter 'event'"

def test_umlmodel::timeobservation_has_firstEvent():
    assert hasattr(UMLModel::TimeObservation, "firstEvent")
    descriptor = None
    for klass in UMLModel::TimeObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::timeobservation_has_event():
    assert hasattr(UMLModel::TimeObservation, "event")
    descriptor = None
    for klass in UMLModel::TimeObservation.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::durationobservation_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DurationObservation)


def test_umlmodel::durationobservation_constructor_exists():
    assert callable(UMLModel::DurationObservation.__init__)


def test_umlmodel::durationobservation_constructor_args():
    sig = inspect.signature(UMLModel::DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_umlmodel::durationobservation_has_event():
    assert hasattr(UMLModel::DurationObservation, "event")
    descriptor = None
    for klass in UMLModel::DurationObservation.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::durationobservation_has_firstEvent():
    assert hasattr(UMLModel::DurationObservation, "firstEvent")
    descriptor = None
    for klass in UMLModel::DurationObservation.__mro__:
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



def test_umlmodel::timeinterval_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TimeInterval)


def test_umlmodel::timeinterval_constructor_exists():
    assert callable(UMLModel::TimeInterval.__init__)


def test_umlmodel::timeinterval_constructor_args():
    sig = inspect.signature(UMLModel::TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::durationinterval_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DurationInterval)


def test_umlmodel::durationinterval_constructor_exists():
    assert callable(UMLModel::DurationInterval.__init__)


def test_umlmodel::durationinterval_constructor_args():
    sig = inspect.signature(UMLModel::DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TimeConstraint)


def test_umlmodel::timeconstraint_constructor_exists():
    assert callable(UMLModel::TimeConstraint.__init__)


def test_umlmodel::timeconstraint_constructor_args():
    sig = inspect.signature(UMLModel::TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_umlmodel::timeconstraint_has_firstEvent():
    assert hasattr(UMLModel::TimeConstraint, "firstEvent")
    descriptor = None
    for klass in UMLModel::TimeConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DurationConstraint)


def test_umlmodel::durationconstraint_constructor_exists():
    assert callable(UMLModel::DurationConstraint.__init__)


def test_umlmodel::durationconstraint_constructor_args():
    sig = inspect.signature(UMLModel::DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_umlmodel::durationconstraint_has_firstEvent():
    assert hasattr(UMLModel::DurationConstraint, "firstEvent")
    descriptor = None
    for klass in UMLModel::DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::literalspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LiteralSpecification)


def test_umlmodel::literalspecification_constructor_exists():
    assert callable(UMLModel::LiteralSpecification.__init__)


def test_umlmodel::literalspecification_constructor_args():
    sig = inspect.signature(UMLModel::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::interval_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Interval)


def test_umlmodel::interval_constructor_exists():
    assert callable(UMLModel::Interval.__init__)


def test_umlmodel::interval_constructor_args():
    sig = inspect.signature(UMLModel::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_umlmodel::interval_has_max():
    assert hasattr(UMLModel::Interval, "max")
    descriptor = None
    for klass in UMLModel::Interval.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::interval_has_min():
    assert hasattr(UMLModel::Interval, "min")
    descriptor = None
    for klass in UMLModel::Interval.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::instancevalue_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InstanceValue)


def test_umlmodel::instancevalue_constructor_exists():
    assert callable(UMLModel::InstanceValue.__init__)


def test_umlmodel::instancevalue_constructor_args():
    sig = inspect.signature(UMLModel::InstanceValue.__init__)
    params = list(sig.parameters.keys())
    assert "instance" in params, "Missing parameter 'instance'"

def test_umlmodel::instancevalue_has_instance():
    assert hasattr(UMLModel::InstanceValue, "instance")
    descriptor = None
    for klass in UMLModel::InstanceValue.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UMLModel::OpaqueExpression)


def test_umlmodel::opaqueexpression_constructor_exists():
    assert callable(UMLModel::OpaqueExpression.__init__)


def test_umlmodel::opaqueexpression_constructor_args():
    sig = inspect.signature(UMLModel::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"
    assert "result" in params, "Missing parameter 'result'"

def test_umlmodel::opaqueexpression_has_behavior():
    assert hasattr(UMLModel::OpaqueExpression, "behavior")
    descriptor = None
    for klass in UMLModel::OpaqueExpression.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::opaqueexpression_has_body():
    assert hasattr(UMLModel::OpaqueExpression, "body")
    descriptor = None
    for klass in UMLModel::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::opaqueexpression_has_language():
    assert hasattr(UMLModel::OpaqueExpression, "language")
    descriptor = None
    for klass in UMLModel::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::opaqueexpression_has_result():
    assert hasattr(UMLModel::OpaqueExpression, "result")
    descriptor = None
    for klass in UMLModel::OpaqueExpression.__mro__:
        if "result" in klass.__dict__:
            descriptor = klass.__dict__["result"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::timeexpression_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TimeExpression)


def test_umlmodel::timeexpression_constructor_exists():
    assert callable(UMLModel::TimeExpression.__init__)


def test_umlmodel::timeexpression_constructor_args():
    sig = inspect.signature(UMLModel::TimeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "observation" in params, "Missing parameter 'observation'"

def test_umlmodel::timeexpression_has_expr():
    assert hasattr(UMLModel::TimeExpression, "expr")
    descriptor = None
    for klass in UMLModel::TimeExpression.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::timeexpression_has_observation():
    assert hasattr(UMLModel::TimeExpression, "observation")
    descriptor = None
    for klass in UMLModel::TimeExpression.__mro__:
        if "observation" in klass.__dict__:
            descriptor = klass.__dict__["observation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::expression_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Expression)


def test_umlmodel::expression_constructor_exists():
    assert callable(UMLModel::Expression.__init__)


def test_umlmodel::expression_constructor_args():
    sig = inspect.signature(UMLModel::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_umlmodel::expression_has_symbol():
    assert hasattr(UMLModel::Expression, "symbol")
    descriptor = None
    for klass in UMLModel::Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::duration_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Duration)


def test_umlmodel::duration_constructor_exists():
    assert callable(UMLModel::Duration.__init__)


def test_umlmodel::duration_constructor_args():
    sig = inspect.signature(UMLModel::Duration.__init__)
    params = list(sig.parameters.keys())
    assert "observation" in params, "Missing parameter 'observation'"
    assert "expr" in params, "Missing parameter 'expr'"

def test_umlmodel::duration_has_observation():
    assert hasattr(UMLModel::Duration, "observation")
    descriptor = None
    for klass in UMLModel::Duration.__mro__:
        if "observation" in klass.__dict__:
            descriptor = klass.__dict__["observation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::duration_has_expr():
    assert hasattr(UMLModel::Duration, "expr")
    descriptor = None
    for klass in UMLModel::Duration.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(UMLModel::EnumerationLiteral)


def test_umlmodel::enumerationliteral_constructor_exists():
    assert callable(UMLModel::EnumerationLiteral.__init__)


def test_umlmodel::enumerationliteral_constructor_args():
    sig = inspect.signature(UMLModel::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "enumeration" in params, "Missing parameter 'enumeration'"

def test_umlmodel::enumerationliteral_has_enumeration():
    assert hasattr(UMLModel::EnumerationLiteral, "enumeration")
    descriptor = None
    for klass in UMLModel::EnumerationLiteral.__mro__:
        if "enumeration" in klass.__dict__:
            descriptor = klass.__dict__["enumeration"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::primitivetype_is_not_abstract():
    assert not inspect.isabstract(UMLModel::PrimitiveType)


def test_umlmodel::primitivetype_constructor_exists():
    assert callable(UMLModel::PrimitiveType.__init__)


def test_umlmodel::primitivetype_constructor_args():
    sig = inspect.signature(UMLModel::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::enumeration_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Enumeration)


def test_umlmodel::enumeration_constructor_exists():
    assert callable(UMLModel::Enumeration.__init__)


def test_umlmodel::enumeration_constructor_args():
    sig = inspect.signature(UMLModel::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DestroyObjectAction)


def test_umlmodel::destroyobjectaction_constructor_exists():
    assert callable(UMLModel::DestroyObjectAction.__init__)


def test_umlmodel::destroyobjectaction_constructor_args():
    sig = inspect.signature(UMLModel::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyOwnedObjects" in params, "Missing parameter 'isDestroyOwnedObjects'"
    assert "isDestroyLinks" in params, "Missing parameter 'isDestroyLinks'"

def test_umlmodel::destroyobjectaction_has_isDestroyOwnedObjects():
    assert hasattr(UMLModel::DestroyObjectAction, "isDestroyOwnedObjects")
    descriptor = None
    for klass in UMLModel::DestroyObjectAction.__mro__:
        if "isDestroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::destroyobjectaction_has_isDestroyLinks():
    assert hasattr(UMLModel::DestroyObjectAction, "isDestroyLinks")
    descriptor = None
    for klass in UMLModel::DestroyObjectAction.__mro__:
        if "isDestroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyLinks"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExecutionEnvironment)


def test_umlmodel::executionenvironment_constructor_exists():
    assert callable(UMLModel::ExecutionEnvironment.__init__)


def test_umlmodel::executionenvironment_constructor_args():
    sig = inspect.signature(UMLModel::ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::device_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Device)


def test_umlmodel::device_constructor_exists():
    assert callable(UMLModel::Device.__init__)


def test_umlmodel::device_constructor_args():
    sig = inspect.signature(UMLModel::Device.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DirectedRelationship)


def test_umlmodel::directedrelationship_constructor_exists():
    assert callable(UMLModel::DirectedRelationship.__init__)


def test_umlmodel::directedrelationship_constructor_args():
    sig = inspect.signature(UMLModel::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"

def test_umlmodel::directedrelationship_has_source():
    assert hasattr(UMLModel::DirectedRelationship, "source")
    descriptor = None
    for klass in UMLModel::DirectedRelationship.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::directedrelationship_has_target():
    assert hasattr(UMLModel::DirectedRelationship, "target")
    descriptor = None
    for klass in UMLModel::DirectedRelationship.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::deployedartifact_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DeployedArtifact)


def test_umlmodel::deployedartifact_constructor_exists():
    assert callable(UMLModel::DeployedArtifact.__init__)


def test_umlmodel::deployedartifact_constructor_args():
    sig = inspect.signature(UMLModel::DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DeploymentSpecification)


def test_umlmodel::deploymentspecification_constructor_exists():
    assert callable(UMLModel::DeploymentSpecification.__init__)


def test_umlmodel::deploymentspecification_constructor_args():
    sig = inspect.signature(UMLModel::DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"
    assert "deployment" in params, "Missing parameter 'deployment'"

def test_umlmodel::deploymentspecification_has_executionLocation():
    assert hasattr(UMLModel::DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in UMLModel::DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::deploymentspecification_has_deploymentLocation():
    assert hasattr(UMLModel::DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in UMLModel::DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::deploymentspecification_has_deployment():
    assert hasattr(UMLModel::DeploymentSpecification, "deployment")
    descriptor = None
    for klass in UMLModel::DeploymentSpecification.__mro__:
        if "deployment" in klass.__dict__:
            descriptor = klass.__dict__["deployment"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::deployment_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Deployment)


def test_umlmodel::deployment_constructor_exists():
    assert callable(UMLModel::Deployment.__init__)


def test_umlmodel::deployment_constructor_args():
    sig = inspect.signature(UMLModel::Deployment.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "deployedArtifact" in params, "Missing parameter 'deployedArtifact'"

def test_umlmodel::deployment_has_location():
    assert hasattr(UMLModel::Deployment, "location")
    descriptor = None
    for klass in UMLModel::Deployment.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::deployment_has_deployedArtifact():
    assert hasattr(UMLModel::Deployment, "deployedArtifact")
    descriptor = None
    for klass in UMLModel::Deployment.__mro__:
        if "deployedArtifact" in klass.__dict__:
            descriptor = klass.__dict__["deployedArtifact"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DeploymentTarget)


def test_umlmodel::deploymenttarget_constructor_exists():
    assert callable(UMLModel::DeploymentTarget.__init__)


def test_umlmodel::deploymenttarget_constructor_args():
    sig = inspect.signature(UMLModel::DeploymentTarget.__init__)
    params = list(sig.parameters.keys())
    assert "deployedElement" in params, "Missing parameter 'deployedElement'"

def test_umlmodel::deploymenttarget_has_deployedElement():
    assert hasattr(UMLModel::DeploymentTarget, "deployedElement")
    descriptor = None
    for klass in UMLModel::DeploymentTarget.__mro__:
        if "deployedElement" in klass.__dict__:
            descriptor = klass.__dict__["deployedElement"]
            break
    assert isinstance(descriptor, property)



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::pin_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Pin)


def test_umlmodel::pin_constructor_exists():
    assert callable(UMLModel::Pin.__init__)


def test_umlmodel::pin_constructor_args():
    sig = inspect.signature(UMLModel::Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_umlmodel::pin_has_isControl():
    assert hasattr(UMLModel::Pin, "isControl")
    descriptor = None
    for klass in UMLModel::Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::variable_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Variable)


def test_umlmodel::variable_constructor_exists():
    assert callable(UMLModel::Variable.__init__)


def test_umlmodel::variable_constructor_args():
    sig = inspect.signature(UMLModel::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "activityScope" in params, "Missing parameter 'activityScope'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_umlmodel::variable_has_activityScope():
    assert hasattr(UMLModel::Variable, "activityScope")
    descriptor = None
    for klass in UMLModel::Variable.__mro__:
        if "activityScope" in klass.__dict__:
            descriptor = klass.__dict__["activityScope"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::variable_has_scope():
    assert hasattr(UMLModel::Variable, "scope")
    descriptor = None
    for klass in UMLModel::Variable.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::connectorend_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ConnectorEnd)


def test_umlmodel::connectorend_constructor_exists():
    assert callable(UMLModel::ConnectorEnd.__init__)


def test_umlmodel::connectorend_constructor_args():
    sig = inspect.signature(UMLModel::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "definingEnd" in params, "Missing parameter 'definingEnd'"
    assert "partWithPort" in params, "Missing parameter 'partWithPort'"

def test_umlmodel::connectorend_has_role():
    assert hasattr(UMLModel::ConnectorEnd, "role")
    descriptor = None
    for klass in UMLModel::ConnectorEnd.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::connectorend_has_definingEnd():
    assert hasattr(UMLModel::ConnectorEnd, "definingEnd")
    descriptor = None
    for klass in UMLModel::ConnectorEnd.__mro__:
        if "definingEnd" in klass.__dict__:
            descriptor = klass.__dict__["definingEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::connectorend_has_partWithPort():
    assert hasattr(UMLModel::ConnectorEnd, "partWithPort")
    descriptor = None
    for klass in UMLModel::ConnectorEnd.__mro__:
        if "partWithPort" in klass.__dict__:
            descriptor = klass.__dict__["partWithPort"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::extend_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Extend)


def test_umlmodel::extend_constructor_exists():
    assert callable(UMLModel::Extend.__init__)


def test_umlmodel::extend_constructor_args():
    sig = inspect.signature(UMLModel::Extend.__init__)
    params = list(sig.parameters.keys())
    assert "extensionLocation" in params, "Missing parameter 'extensionLocation'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "extendedCase" in params, "Missing parameter 'extendedCase'"

def test_umlmodel::extend_has_extensionLocation():
    assert hasattr(UMLModel::Extend, "extensionLocation")
    descriptor = None
    for klass in UMLModel::Extend.__mro__:
        if "extensionLocation" in klass.__dict__:
            descriptor = klass.__dict__["extensionLocation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::extend_has_extension():
    assert hasattr(UMLModel::Extend, "extension")
    descriptor = None
    for klass in UMLModel::Extend.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::extend_has_extendedCase():
    assert hasattr(UMLModel::Extend, "extendedCase")
    descriptor = None
    for klass in UMLModel::Extend.__mro__:
        if "extendedCase" in klass.__dict__:
            descriptor = klass.__dict__["extendedCase"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::protocolconformance_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ProtocolConformance)


def test_umlmodel::protocolconformance_constructor_exists():
    assert callable(UMLModel::ProtocolConformance.__init__)


def test_umlmodel::protocolconformance_constructor_args():
    sig = inspect.signature(UMLModel::ProtocolConformance.__init__)
    params = list(sig.parameters.keys())
    assert "specificMachine" in params, "Missing parameter 'specificMachine'"
    assert "generalMachine" in params, "Missing parameter 'generalMachine'"

def test_umlmodel::protocolconformance_has_specificMachine():
    assert hasattr(UMLModel::ProtocolConformance, "specificMachine")
    descriptor = None
    for klass in UMLModel::ProtocolConformance.__mro__:
        if "specificMachine" in klass.__dict__:
            descriptor = klass.__dict__["specificMachine"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::protocolconformance_has_generalMachine():
    assert hasattr(UMLModel::ProtocolConformance, "generalMachine")
    descriptor = None
    for klass in UMLModel::ProtocolConformance.__mro__:
        if "generalMachine" in klass.__dict__:
            descriptor = klass.__dict__["generalMachine"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::elementimport_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ElementImport)


def test_umlmodel::elementimport_constructor_exists():
    assert callable(UMLModel::ElementImport.__init__)


def test_umlmodel::elementimport_constructor_args():
    sig = inspect.signature(UMLModel::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "importingNamespace" in params, "Missing parameter 'importingNamespace'"

def test_umlmodel::elementimport_has_visibility():
    assert hasattr(UMLModel::ElementImport, "visibility")
    descriptor = None
    for klass in UMLModel::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::elementimport_has_alias():
    assert hasattr(UMLModel::ElementImport, "alias")
    descriptor = None
    for klass in UMLModel::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::elementimport_has_importingNamespace():
    assert hasattr(UMLModel::ElementImport, "importingNamespace")
    descriptor = None
    for klass in UMLModel::ElementImport.__mro__:
        if "importingNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importingNamespace"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::include_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Include)


def test_umlmodel::include_constructor_exists():
    assert callable(UMLModel::Include.__init__)


def test_umlmodel::include_constructor_args():
    sig = inspect.signature(UMLModel::Include.__init__)
    params = list(sig.parameters.keys())
    assert "addition" in params, "Missing parameter 'addition'"
    assert "includingCase" in params, "Missing parameter 'includingCase'"

def test_umlmodel::include_has_addition():
    assert hasattr(UMLModel::Include, "addition")
    descriptor = None
    for klass in UMLModel::Include.__mro__:
        if "addition" in klass.__dict__:
            descriptor = klass.__dict__["addition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::include_has_includingCase():
    assert hasattr(UMLModel::Include, "includingCase")
    descriptor = None
    for klass in UMLModel::Include.__mro__:
        if "includingCase" in klass.__dict__:
            descriptor = klass.__dict__["includingCase"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::templatebinding_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TemplateBinding)


def test_umlmodel::templatebinding_constructor_exists():
    assert callable(UMLModel::TemplateBinding.__init__)


def test_umlmodel::templatebinding_constructor_args():
    sig = inspect.signature(UMLModel::TemplateBinding.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "boundElement" in params, "Missing parameter 'boundElement'"

def test_umlmodel::templatebinding_has_signature():
    assert hasattr(UMLModel::TemplateBinding, "signature")
    descriptor = None
    for klass in UMLModel::TemplateBinding.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::templatebinding_has_boundElement():
    assert hasattr(UMLModel::TemplateBinding, "boundElement")
    descriptor = None
    for klass in UMLModel::TemplateBinding.__mro__:
        if "boundElement" in klass.__dict__:
            descriptor = klass.__dict__["boundElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::profileapplication_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ProfileApplication)


def test_umlmodel::profileapplication_constructor_exists():
    assert callable(UMLModel::ProfileApplication.__init__)


def test_umlmodel::profileapplication_constructor_args():
    sig = inspect.signature(UMLModel::ProfileApplication.__init__)
    params = list(sig.parameters.keys())
    assert "appliedProfile" in params, "Missing parameter 'appliedProfile'"
    assert "applyingPackage" in params, "Missing parameter 'applyingPackage'"
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_umlmodel::profileapplication_has_appliedProfile():
    assert hasattr(UMLModel::ProfileApplication, "appliedProfile")
    descriptor = None
    for klass in UMLModel::ProfileApplication.__mro__:
        if "appliedProfile" in klass.__dict__:
            descriptor = klass.__dict__["appliedProfile"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::profileapplication_has_applyingPackage():
    assert hasattr(UMLModel::ProfileApplication, "applyingPackage")
    descriptor = None
    for klass in UMLModel::ProfileApplication.__mro__:
        if "applyingPackage" in klass.__dict__:
            descriptor = klass.__dict__["applyingPackage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::profileapplication_has_isStrict():
    assert hasattr(UMLModel::ProfileApplication, "isStrict")
    descriptor = None
    for klass in UMLModel::ProfileApplication.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::packagemerge_is_not_abstract():
    assert not inspect.isabstract(UMLModel::PackageMerge)


def test_umlmodel::packagemerge_constructor_exists():
    assert callable(UMLModel::PackageMerge.__init__)


def test_umlmodel::packagemerge_constructor_args():
    sig = inspect.signature(UMLModel::PackageMerge.__init__)
    params = list(sig.parameters.keys())
    assert "receivingPackage" in params, "Missing parameter 'receivingPackage'"
    assert "mergedPackage" in params, "Missing parameter 'mergedPackage'"

def test_umlmodel::packagemerge_has_receivingPackage():
    assert hasattr(UMLModel::PackageMerge, "receivingPackage")
    descriptor = None
    for klass in UMLModel::PackageMerge.__mro__:
        if "receivingPackage" in klass.__dict__:
            descriptor = klass.__dict__["receivingPackage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::packagemerge_has_mergedPackage():
    assert hasattr(UMLModel::PackageMerge, "mergedPackage")
    descriptor = None
    for klass in UMLModel::PackageMerge.__mro__:
        if "mergedPackage" in klass.__dict__:
            descriptor = klass.__dict__["mergedPackage"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::packageimport_is_not_abstract():
    assert not inspect.isabstract(UMLModel::PackageImport)


def test_umlmodel::packageimport_constructor_exists():
    assert callable(UMLModel::PackageImport.__init__)


def test_umlmodel::packageimport_constructor_args():
    sig = inspect.signature(UMLModel::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "importingNamespace" in params, "Missing parameter 'importingNamespace'"

def test_umlmodel::packageimport_has_visibility():
    assert hasattr(UMLModel::PackageImport, "visibility")
    descriptor = None
    for klass in UMLModel::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::packageimport_has_importingNamespace():
    assert hasattr(UMLModel::PackageImport, "importingNamespace")
    descriptor = None
    for klass in UMLModel::PackageImport.__mro__:
        if "importingNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importingNamespace"]
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



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::forknode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ForkNode)


def test_umlmodel::forknode_constructor_exists():
    assert callable(UMLModel::ForkNode.__init__)


def test_umlmodel::forknode_constructor_args():
    sig = inspect.signature(UMLModel::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::joinnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::JoinNode)


def test_umlmodel::joinnode_constructor_exists():
    assert callable(UMLModel::JoinNode.__init__)


def test_umlmodel::joinnode_constructor_args():
    sig = inspect.signature(UMLModel::JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_umlmodel::joinnode_has_isCombineDuplicate():
    assert hasattr(UMLModel::JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in UMLModel::JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::finalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::FinalNode)


def test_umlmodel::finalnode_constructor_exists():
    assert callable(UMLModel::FinalNode.__init__)


def test_umlmodel::finalnode_constructor_args():
    sig = inspect.signature(UMLModel::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::mergenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::MergeNode)


def test_umlmodel::mergenode_constructor_exists():
    assert callable(UMLModel::MergeNode.__init__)


def test_umlmodel::mergenode_constructor_args():
    sig = inspect.signature(UMLModel::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::initialnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InitialNode)


def test_umlmodel::initialnode_constructor_exists():
    assert callable(UMLModel::InitialNode.__init__)


def test_umlmodel::initialnode_constructor_args():
    sig = inspect.signature(UMLModel::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::connectableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ConnectableElement)


def test_umlmodel::connectableelement_constructor_exists():
    assert callable(UMLModel::ConnectableElement.__init__)


def test_umlmodel::connectableelement_constructor_args():
    sig = inspect.signature(UMLModel::ConnectableElement.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_umlmodel::connectableelement_has_end():
    assert hasattr(UMLModel::ConnectableElement, "end")
    descriptor = None
    for klass in UMLModel::ConnectableElement.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::decisionnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DecisionNode)


def test_umlmodel::decisionnode_constructor_exists():
    assert callable(UMLModel::DecisionNode.__init__)


def test_umlmodel::decisionnode_constructor_args():
    sig = inspect.signature(UMLModel::DecisionNode.__init__)
    params = list(sig.parameters.keys())
    assert "decisionInput" in params, "Missing parameter 'decisionInput'"

def test_umlmodel::decisionnode_has_decisionInput():
    assert hasattr(UMLModel::DecisionNode, "decisionInput")
    descriptor = None
    for klass in UMLModel::DecisionNode.__mro__:
        if "decisionInput" in klass.__dict__:
            descriptor = klass.__dict__["decisionInput"]
            break
    assert isinstance(descriptor, property)



def test_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ConsiderIgnoreFragment)


def test_umlmodel::considerignorefragment_constructor_exists():
    assert callable(UMLModel::ConsiderIgnoreFragment.__init__)


def test_umlmodel::considerignorefragment_constructor_args():
    sig = inspect.signature(UMLModel::ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_umlmodel::considerignorefragment_has_message():
    assert hasattr(UMLModel::ConsiderIgnoreFragment, "message")
    descriptor = None
    for klass in UMLModel::ConsiderIgnoreFragment.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::datatype_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DataType)


def test_umlmodel::datatype_constructor_exists():
    assert callable(UMLModel::DataType.__init__)


def test_umlmodel::datatype_constructor_args():
    sig = inspect.signature(UMLModel::DataType.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::datastorenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DataStoreNode)


def test_umlmodel::datastorenode_constructor_exists():
    assert callable(UMLModel::DataStoreNode.__init__)


def test_umlmodel::datastorenode_constructor_args():
    sig = inspect.signature(UMLModel::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CentralBufferNode)


def test_umlmodel::centralbuffernode_constructor_exists():
    assert callable(UMLModel::CentralBufferNode.__init__)


def test_umlmodel::centralbuffernode_constructor_args():
    sig = inspect.signature(UMLModel::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DestroyLinkAction)


def test_umlmodel::destroylinkaction_constructor_exists():
    assert callable(UMLModel::DestroyLinkAction.__init__)


def test_umlmodel::destroylinkaction_constructor_args():
    sig = inspect.signature(UMLModel::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CreateLinkAction)


def test_umlmodel::createlinkaction_constructor_exists():
    assert callable(UMLModel::CreateLinkAction.__init__)


def test_umlmodel::createlinkaction_constructor_args():
    sig = inspect.signature(UMLModel::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::type_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Type)


def test_umlmodel::type_constructor_exists():
    assert callable(UMLModel::Type.__init__)


def test_umlmodel::type_constructor_args():
    sig = inspect.signature(UMLModel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_umlmodel::type_has_package():
    assert hasattr(UMLModel::Type, "package")
    descriptor = None
    for klass in UMLModel::Type.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::event_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Event)


def test_umlmodel::event_constructor_exists():
    assert callable(UMLModel::Event.__init__)


def test_umlmodel::event_constructor_args():
    sig = inspect.signature(UMLModel::Event.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::observation_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Observation)


def test_umlmodel::observation_constructor_exists():
    assert callable(UMLModel::Observation.__init__)


def test_umlmodel::observation_constructor_args():
    sig = inspect.signature(UMLModel::Observation.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::instancespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InstanceSpecification)


def test_umlmodel::instancespecification_constructor_exists():
    assert callable(UMLModel::InstanceSpecification.__init__)


def test_umlmodel::instancespecification_constructor_args():
    sig = inspect.signature(UMLModel::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel::instancespecification_has_classifier():
    assert hasattr(UMLModel::InstanceSpecification, "classifier")
    descriptor = None
    for klass in UMLModel::InstanceSpecification.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::generalizationset_is_not_abstract():
    assert not inspect.isabstract(UMLModel::GeneralizationSet)


def test_umlmodel::generalizationset_constructor_exists():
    assert callable(UMLModel::GeneralizationSet.__init__)


def test_umlmodel::generalizationset_constructor_args():
    sig = inspect.signature(UMLModel::GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"
    assert "generalization" in params, "Missing parameter 'generalization'"
    assert "powerType" in params, "Missing parameter 'powerType'"
    assert "isCovering" in params, "Missing parameter 'isCovering'"

def test_umlmodel::generalizationset_has_isDisjoint():
    assert hasattr(UMLModel::GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in UMLModel::GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::generalizationset_has_generalization():
    assert hasattr(UMLModel::GeneralizationSet, "generalization")
    descriptor = None
    for klass in UMLModel::GeneralizationSet.__mro__:
        if "generalization" in klass.__dict__:
            descriptor = klass.__dict__["generalization"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::generalizationset_has_powerType():
    assert hasattr(UMLModel::GeneralizationSet, "powerType")
    descriptor = None
    for klass in UMLModel::GeneralizationSet.__mro__:
        if "powerType" in klass.__dict__:
            descriptor = klass.__dict__["powerType"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::generalizationset_has_isCovering():
    assert hasattr(UMLModel::GeneralizationSet, "isCovering")
    descriptor = None
    for klass in UMLModel::GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::valuespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ValueSpecification)


def test_umlmodel::valuespecification_constructor_exists():
    assert callable(UMLModel::ValueSpecification.__init__)


def test_umlmodel::valuespecification_constructor_args():
    sig = inspect.signature(UMLModel::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::informationflow_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InformationFlow)


def test_umlmodel::informationflow_constructor_exists():
    assert callable(UMLModel::InformationFlow.__init__)


def test_umlmodel::informationflow_constructor_args():
    sig = inspect.signature(UMLModel::InformationFlow.__init__)
    params = list(sig.parameters.keys())
    assert "realizingActivityEdge" in params, "Missing parameter 'realizingActivityEdge'"
    assert "realizingConnector" in params, "Missing parameter 'realizingConnector'"
    assert "realization" in params, "Missing parameter 'realization'"
    assert "informationTarget" in params, "Missing parameter 'informationTarget'"
    assert "realizingMessage" in params, "Missing parameter 'realizingMessage'"
    assert "informationSource" in params, "Missing parameter 'informationSource'"
    assert "conveyed" in params, "Missing parameter 'conveyed'"

def test_umlmodel::informationflow_has_realizingActivityEdge():
    assert hasattr(UMLModel::InformationFlow, "realizingActivityEdge")
    descriptor = None
    for klass in UMLModel::InformationFlow.__mro__:
        if "realizingActivityEdge" in klass.__dict__:
            descriptor = klass.__dict__["realizingActivityEdge"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::informationflow_has_realizingConnector():
    assert hasattr(UMLModel::InformationFlow, "realizingConnector")
    descriptor = None
    for klass in UMLModel::InformationFlow.__mro__:
        if "realizingConnector" in klass.__dict__:
            descriptor = klass.__dict__["realizingConnector"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::informationflow_has_realization():
    assert hasattr(UMLModel::InformationFlow, "realization")
    descriptor = None
    for klass in UMLModel::InformationFlow.__mro__:
        if "realization" in klass.__dict__:
            descriptor = klass.__dict__["realization"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::informationflow_has_informationTarget():
    assert hasattr(UMLModel::InformationFlow, "informationTarget")
    descriptor = None
    for klass in UMLModel::InformationFlow.__mro__:
        if "informationTarget" in klass.__dict__:
            descriptor = klass.__dict__["informationTarget"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::informationflow_has_realizingMessage():
    assert hasattr(UMLModel::InformationFlow, "realizingMessage")
    descriptor = None
    for klass in UMLModel::InformationFlow.__mro__:
        if "realizingMessage" in klass.__dict__:
            descriptor = klass.__dict__["realizingMessage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::informationflow_has_informationSource():
    assert hasattr(UMLModel::InformationFlow, "informationSource")
    descriptor = None
    for klass in UMLModel::InformationFlow.__mro__:
        if "informationSource" in klass.__dict__:
            descriptor = klass.__dict__["informationSource"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::informationflow_has_conveyed():
    assert hasattr(UMLModel::InformationFlow, "conveyed")
    descriptor = None
    for klass in UMLModel::InformationFlow.__mro__:
        if "conveyed" in klass.__dict__:
            descriptor = klass.__dict__["conveyed"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::constraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Constraint)


def test_umlmodel::constraint_constructor_exists():
    assert callable(UMLModel::Constraint.__init__)


def test_umlmodel::constraint_constructor_args():
    sig = inspect.signature(UMLModel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "constrainedElement" in params, "Missing parameter 'constrainedElement'"
    assert "context" in params, "Missing parameter 'context'"

def test_umlmodel::constraint_has_constrainedElement():
    assert hasattr(UMLModel::Constraint, "constrainedElement")
    descriptor = None
    for klass in UMLModel::Constraint.__mro__:
        if "constrainedElement" in klass.__dict__:
            descriptor = klass.__dict__["constrainedElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::constraint_has_context():
    assert hasattr(UMLModel::Constraint, "context")
    descriptor = None
    for klass in UMLModel::Constraint.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CreateObjectAction)


def test_umlmodel::createobjectaction_constructor_exists():
    assert callable(UMLModel::CreateObjectAction.__init__)


def test_umlmodel::createobjectaction_constructor_args():
    sig = inspect.signature(UMLModel::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel::createobjectaction_has_classifier():
    assert hasattr(UMLModel::CreateObjectAction, "classifier")
    descriptor = None
    for klass in UMLModel::CreateObjectAction.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CreateLinkObjectAction)


def test_umlmodel::createlinkobjectaction_constructor_exists():
    assert callable(UMLModel::CreateLinkObjectAction.__init__)


def test_umlmodel::createlinkobjectaction_constructor_args():
    sig = inspect.signature(UMLModel::CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::expansionregion_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExpansionRegion)


def test_umlmodel::expansionregion_constructor_exists():
    assert callable(UMLModel::ExpansionRegion.__init__)


def test_umlmodel::expansionregion_constructor_args():
    sig = inspect.signature(UMLModel::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "inputElement" in params, "Missing parameter 'inputElement'"
    assert "outputElement" in params, "Missing parameter 'outputElement'"

def test_umlmodel::expansionregion_has_mode():
    assert hasattr(UMLModel::ExpansionRegion, "mode")
    descriptor = None
    for klass in UMLModel::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::expansionregion_has_inputElement():
    assert hasattr(UMLModel::ExpansionRegion, "inputElement")
    descriptor = None
    for klass in UMLModel::ExpansionRegion.__mro__:
        if "inputElement" in klass.__dict__:
            descriptor = klass.__dict__["inputElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::expansionregion_has_outputElement():
    assert hasattr(UMLModel::ExpansionRegion, "outputElement")
    descriptor = None
    for klass in UMLModel::ExpansionRegion.__mro__:
        if "outputElement" in klass.__dict__:
            descriptor = klass.__dict__["outputElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::sequencenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::SequenceNode)


def test_umlmodel::sequencenode_constructor_exists():
    assert callable(UMLModel::SequenceNode.__init__)


def test_umlmodel::sequencenode_constructor_args():
    sig = inspect.signature(UMLModel::SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::loopnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::LoopNode)


def test_umlmodel::loopnode_constructor_exists():
    assert callable(UMLModel::LoopNode.__init__)


def test_umlmodel::loopnode_constructor_args():
    sig = inspect.signature(UMLModel::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "decider" in params, "Missing parameter 'decider'"
    assert "bodyOutput" in params, "Missing parameter 'bodyOutput'"
    assert "loopVariable" in params, "Missing parameter 'loopVariable'"
    assert "bodyPart" in params, "Missing parameter 'bodyPart'"
    assert "setupPart" in params, "Missing parameter 'setupPart'"
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"
    assert "test" in params, "Missing parameter 'test'"

def test_umlmodel::loopnode_has_decider():
    assert hasattr(UMLModel::LoopNode, "decider")
    descriptor = None
    for klass in UMLModel::LoopNode.__mro__:
        if "decider" in klass.__dict__:
            descriptor = klass.__dict__["decider"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::loopnode_has_bodyOutput():
    assert hasattr(UMLModel::LoopNode, "bodyOutput")
    descriptor = None
    for klass in UMLModel::LoopNode.__mro__:
        if "bodyOutput" in klass.__dict__:
            descriptor = klass.__dict__["bodyOutput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::loopnode_has_loopVariable():
    assert hasattr(UMLModel::LoopNode, "loopVariable")
    descriptor = None
    for klass in UMLModel::LoopNode.__mro__:
        if "loopVariable" in klass.__dict__:
            descriptor = klass.__dict__["loopVariable"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::loopnode_has_bodyPart():
    assert hasattr(UMLModel::LoopNode, "bodyPart")
    descriptor = None
    for klass in UMLModel::LoopNode.__mro__:
        if "bodyPart" in klass.__dict__:
            descriptor = klass.__dict__["bodyPart"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::loopnode_has_setupPart():
    assert hasattr(UMLModel::LoopNode, "setupPart")
    descriptor = None
    for klass in UMLModel::LoopNode.__mro__:
        if "setupPart" in klass.__dict__:
            descriptor = klass.__dict__["setupPart"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::loopnode_has_isTestedFirst():
    assert hasattr(UMLModel::LoopNode, "isTestedFirst")
    descriptor = None
    for klass in UMLModel::LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::loopnode_has_test():
    assert hasattr(UMLModel::LoopNode, "test")
    descriptor = None
    for klass in UMLModel::LoopNode.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ConditionalNode)


def test_umlmodel::conditionalnode_constructor_exists():
    assert callable(UMLModel::ConditionalNode.__init__)


def test_umlmodel::conditionalnode_constructor_args():
    sig = inspect.signature(UMLModel::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssured" in params, "Missing parameter 'isAssured'"

def test_umlmodel::conditionalnode_has_isDeterminate():
    assert hasattr(UMLModel::ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in UMLModel::ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::conditionalnode_has_isAssured():
    assert hasattr(UMLModel::ConditionalNode, "isAssured")
    descriptor = None
    for klass in UMLModel::ConditionalNode.__mro__:
        if "isAssured" in klass.__dict__:
            descriptor = klass.__dict__["isAssured"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::gate_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Gate)


def test_umlmodel::gate_constructor_exists():
    assert callable(UMLModel::Gate.__init__)


def test_umlmodel::gate_constructor_args():
    sig = inspect.signature(UMLModel::Gate.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::objectnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ObjectNode)


def test_umlmodel::objectnode_constructor_exists():
    assert callable(UMLModel::ObjectNode.__init__)


def test_umlmodel::objectnode_constructor_args():
    sig = inspect.signature(UMLModel::ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "inState" in params, "Missing parameter 'inState'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"

def test_umlmodel::objectnode_has_selection():
    assert hasattr(UMLModel::ObjectNode, "selection")
    descriptor = None
    for klass in UMLModel::ObjectNode.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::objectnode_has_ordering():
    assert hasattr(UMLModel::ObjectNode, "ordering")
    descriptor = None
    for klass in UMLModel::ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::objectnode_has_inState():
    assert hasattr(UMLModel::ObjectNode, "inState")
    descriptor = None
    for klass in UMLModel::ObjectNode.__mro__:
        if "inState" in klass.__dict__:
            descriptor = klass.__dict__["inState"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::objectnode_has_isControlType():
    assert hasattr(UMLModel::ObjectNode, "isControlType")
    descriptor = None
    for klass in UMLModel::ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::executablenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExecutableNode)


def test_umlmodel::executablenode_constructor_exists():
    assert callable(UMLModel::ExecutableNode.__init__)


def test_umlmodel::executablenode_constructor_args():
    sig = inspect.signature(UMLModel::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::controlnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ControlNode)


def test_umlmodel::controlnode_constructor_exists():
    assert callable(UMLModel::ControlNode.__init__)


def test_umlmodel::controlnode_constructor_args():
    sig = inspect.signature(UMLModel::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::objectflow_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ObjectFlow)


def test_umlmodel::objectflow_constructor_exists():
    assert callable(UMLModel::ObjectFlow.__init__)


def test_umlmodel::objectflow_constructor_args():
    sig = inspect.signature(UMLModel::ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "transformation" in params, "Missing parameter 'transformation'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "selection" in params, "Missing parameter 'selection'"

def test_umlmodel::objectflow_has_isMultireceive():
    assert hasattr(UMLModel::ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in UMLModel::ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::objectflow_has_transformation():
    assert hasattr(UMLModel::ObjectFlow, "transformation")
    descriptor = None
    for klass in UMLModel::ObjectFlow.__mro__:
        if "transformation" in klass.__dict__:
            descriptor = klass.__dict__["transformation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::objectflow_has_isMulticast():
    assert hasattr(UMLModel::ObjectFlow, "isMulticast")
    descriptor = None
    for klass in UMLModel::ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::objectflow_has_selection():
    assert hasattr(UMLModel::ObjectFlow, "selection")
    descriptor = None
    for klass in UMLModel::ObjectFlow.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::controlflow_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ControlFlow)


def test_umlmodel::controlflow_constructor_exists():
    assert callable(UMLModel::ControlFlow.__init__)


def test_umlmodel::controlflow_constructor_args():
    sig = inspect.signature(UMLModel::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::pseudostate_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Pseudostate)


def test_umlmodel::pseudostate_constructor_exists():
    assert callable(UMLModel::Pseudostate.__init__)


def test_umlmodel::pseudostate_constructor_args():
    sig = inspect.signature(UMLModel::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "state" in params, "Missing parameter 'state'"
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"

def test_umlmodel::pseudostate_has_kind():
    assert hasattr(UMLModel::Pseudostate, "kind")
    descriptor = None
    for klass in UMLModel::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::pseudostate_has_state():
    assert hasattr(UMLModel::Pseudostate, "state")
    descriptor = None
    for klass in UMLModel::Pseudostate.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::pseudostate_has_stateMachine():
    assert hasattr(UMLModel::Pseudostate, "stateMachine")
    descriptor = None
    for klass in UMLModel::Pseudostate.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ConnectionPointReference)


def test_umlmodel::connectionpointreference_constructor_exists():
    assert callable(UMLModel::ConnectionPointReference.__init__)


def test_umlmodel::connectionpointreference_constructor_args():
    sig = inspect.signature(UMLModel::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "entry" in params, "Missing parameter 'entry'"
    assert "exit" in params, "Missing parameter 'exit'"

def test_umlmodel::connectionpointreference_has_state():
    assert hasattr(UMLModel::ConnectionPointReference, "state")
    descriptor = None
    for klass in UMLModel::ConnectionPointReference.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::connectionpointreference_has_entry():
    assert hasattr(UMLModel::ConnectionPointReference, "entry")
    descriptor = None
    for klass in UMLModel::ConnectionPointReference.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::connectionpointreference_has_exit():
    assert hasattr(UMLModel::ConnectionPointReference, "exit")
    descriptor = None
    for klass in UMLModel::ConnectionPointReference.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::comment_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Comment)


def test_umlmodel::comment_constructor_exists():
    assert callable(UMLModel::Comment.__init__)


def test_umlmodel::comment_constructor_args():
    sig = inspect.signature(UMLModel::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "annotatedElement" in params, "Missing parameter 'annotatedElement'"

def test_umlmodel::comment_has_body():
    assert hasattr(UMLModel::Comment, "body")
    descriptor = None
    for klass in UMLModel::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::comment_has_annotatedElement():
    assert hasattr(UMLModel::Comment, "annotatedElement")
    descriptor = None
    for klass in UMLModel::Comment.__mro__:
        if "annotatedElement" in klass.__dict__:
            descriptor = klass.__dict__["annotatedElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::dependency_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Dependency)


def test_umlmodel::dependency_constructor_exists():
    assert callable(UMLModel::Dependency.__init__)


def test_umlmodel::dependency_constructor_args():
    sig = inspect.signature(UMLModel::Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "client" in params, "Missing parameter 'client'"
    assert "supplier" in params, "Missing parameter 'supplier'"

def test_umlmodel::dependency_has_client():
    assert hasattr(UMLModel::Dependency, "client")
    descriptor = None
    for klass in UMLModel::Dependency.__mro__:
        if "client" in klass.__dict__:
            descriptor = klass.__dict__["client"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::dependency_has_supplier():
    assert hasattr(UMLModel::Dependency, "supplier")
    descriptor = None
    for klass in UMLModel::Dependency.__mro__:
        if "supplier" in klass.__dict__:
            descriptor = klass.__dict__["supplier"]
            break
    assert isinstance(descriptor, property)



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel::EncapsulatedClassifier)


def test_umlmodel::encapsulatedclassifier_constructor_exists():
    assert callable(UMLModel::EncapsulatedClassifier.__init__)


def test_umlmodel::encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UMLModel::EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "ownedPort" in params, "Missing parameter 'ownedPort'"

def test_umlmodel::encapsulatedclassifier_has_ownedPort():
    assert hasattr(UMLModel::EncapsulatedClassifier, "ownedPort")
    descriptor = None
    for klass in UMLModel::EncapsulatedClassifier.__mro__:
        if "ownedPort" in klass.__dict__:
            descriptor = klass.__dict__["ownedPort"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::collaboration_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Collaboration)


def test_umlmodel::collaboration_constructor_exists():
    assert callable(UMLModel::Collaboration.__init__)


def test_umlmodel::collaboration_constructor_args():
    sig = inspect.signature(UMLModel::Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "collaborationRole" in params, "Missing parameter 'collaborationRole'"

def test_umlmodel::collaboration_has_collaborationRole():
    assert hasattr(UMLModel::Collaboration, "collaborationRole")
    descriptor = None
    for klass in UMLModel::Collaboration.__mro__:
        if "collaborationRole" in klass.__dict__:
            descriptor = klass.__dict__["collaborationRole"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadStructuralFeatureAction)


def test_umlmodel::readstructuralfeatureaction_constructor_exists():
    assert callable(UMLModel::ReadStructuralFeatureAction.__init__)


def test_umlmodel::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::WriteStructuralFeatureAction)


def test_umlmodel::writestructuralfeatureaction_constructor_exists():
    assert callable(UMLModel::WriteStructuralFeatureAction.__init__)


def test_umlmodel::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ClearStructuralFeatureAction)


def test_umlmodel::clearstructuralfeatureaction_constructor_exists():
    assert callable(UMLModel::ClearStructuralFeatureAction.__init__)


def test_umlmodel::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ClearAssociationAction)


def test_umlmodel::clearassociationaction_constructor_exists():
    assert callable(UMLModel::ClearAssociationAction.__init__)


def test_umlmodel::clearassociationaction_constructor_args():
    sig = inspect.signature(UMLModel::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())
    assert "association" in params, "Missing parameter 'association'"

def test_umlmodel::clearassociationaction_has_association():
    assert hasattr(UMLModel::ClearAssociationAction, "association")
    descriptor = None
    for klass in UMLModel::ClearAssociationAction.__mro__:
        if "association" in klass.__dict__:
            descriptor = klass.__dict__["association"]
            break
    assert isinstance(descriptor, property)



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ReadVariableAction)


def test_umlmodel::readvariableaction_constructor_exists():
    assert callable(UMLModel::ReadVariableAction.__init__)


def test_umlmodel::readvariableaction_constructor_args():
    sig = inspect.signature(UMLModel::ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::WriteVariableAction)


def test_umlmodel::writevariableaction_constructor_exists():
    assert callable(UMLModel::WriteVariableAction.__init__)


def test_umlmodel::writevariableaction_constructor_args():
    sig = inspect.signature(UMLModel::WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ClearVariableAction)


def test_umlmodel::clearvariableaction_constructor_exists():
    assert callable(UMLModel::ClearVariableAction.__init__)


def test_umlmodel::clearvariableaction_constructor_args():
    sig = inspect.signature(UMLModel::ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::clause_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Clause)


def test_umlmodel::clause_constructor_exists():
    assert callable(UMLModel::Clause.__init__)


def test_umlmodel::clause_constructor_args():
    sig = inspect.signature(UMLModel::Clause.__init__)
    params = list(sig.parameters.keys())
    assert "bodyOutput" in params, "Missing parameter 'bodyOutput'"
    assert "predecessorClause" in params, "Missing parameter 'predecessorClause'"
    assert "test" in params, "Missing parameter 'test'"
    assert "decider" in params, "Missing parameter 'decider'"
    assert "body" in params, "Missing parameter 'body'"
    assert "successorClause" in params, "Missing parameter 'successorClause'"

def test_umlmodel::clause_has_bodyOutput():
    assert hasattr(UMLModel::Clause, "bodyOutput")
    descriptor = None
    for klass in UMLModel::Clause.__mro__:
        if "bodyOutput" in klass.__dict__:
            descriptor = klass.__dict__["bodyOutput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::clause_has_predecessorClause():
    assert hasattr(UMLModel::Clause, "predecessorClause")
    descriptor = None
    for klass in UMLModel::Clause.__mro__:
        if "predecessorClause" in klass.__dict__:
            descriptor = klass.__dict__["predecessorClause"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::clause_has_test():
    assert hasattr(UMLModel::Clause, "test")
    descriptor = None
    for klass in UMLModel::Clause.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::clause_has_decider():
    assert hasattr(UMLModel::Clause, "decider")
    descriptor = None
    for klass in UMLModel::Clause.__mro__:
        if "decider" in klass.__dict__:
            descriptor = klass.__dict__["decider"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::clause_has_body():
    assert hasattr(UMLModel::Clause, "body")
    descriptor = None
    for klass in UMLModel::Clause.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::clause_has_successorClause():
    assert hasattr(UMLModel::Clause, "successorClause")
    descriptor = None
    for klass in UMLModel::Clause.__mro__:
        if "successorClause" in klass.__dict__:
            descriptor = klass.__dict__["successorClause"]
            break
    assert isinstance(descriptor, property)



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::stateinvariant_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StateInvariant)


def test_umlmodel::stateinvariant_constructor_exists():
    assert callable(UMLModel::StateInvariant.__init__)


def test_umlmodel::stateinvariant_constructor_args():
    sig = inspect.signature(UMLModel::StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::OccurrenceSpecification)


def test_umlmodel::occurrencespecification_constructor_exists():
    assert callable(UMLModel::OccurrenceSpecification.__init__)


def test_umlmodel::occurrencespecification_constructor_args():
    sig = inspect.signature(UMLModel::OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "toAfter" in params, "Missing parameter 'toAfter'"
    assert "event" in params, "Missing parameter 'event'"
    assert "toBefore" in params, "Missing parameter 'toBefore'"

def test_umlmodel::occurrencespecification_has_toAfter():
    assert hasattr(UMLModel::OccurrenceSpecification, "toAfter")
    descriptor = None
    for klass in UMLModel::OccurrenceSpecification.__mro__:
        if "toAfter" in klass.__dict__:
            descriptor = klass.__dict__["toAfter"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::occurrencespecification_has_event():
    assert hasattr(UMLModel::OccurrenceSpecification, "event")
    descriptor = None
    for klass in UMLModel::OccurrenceSpecification.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::occurrencespecification_has_toBefore():
    assert hasattr(UMLModel::OccurrenceSpecification, "toBefore")
    descriptor = None
    for klass in UMLModel::OccurrenceSpecification.__mro__:
        if "toBefore" in klass.__dict__:
            descriptor = klass.__dict__["toBefore"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::interactionuse_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InteractionUse)


def test_umlmodel::interactionuse_constructor_exists():
    assert callable(UMLModel::InteractionUse.__init__)


def test_umlmodel::interactionuse_constructor_args():
    sig = inspect.signature(UMLModel::InteractionUse.__init__)
    params = list(sig.parameters.keys())
    assert "refersTo" in params, "Missing parameter 'refersTo'"

def test_umlmodel::interactionuse_has_refersTo():
    assert hasattr(UMLModel::InteractionUse, "refersTo")
    descriptor = None
    for klass in UMLModel::InteractionUse.__mro__:
        if "refersTo" in klass.__dict__:
            descriptor = klass.__dict__["refersTo"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::interaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Interaction)


def test_umlmodel::interaction_constructor_exists():
    assert callable(UMLModel::Interaction.__init__)


def test_umlmodel::interaction_constructor_args():
    sig = inspect.signature(UMLModel::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::continuation_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Continuation)


def test_umlmodel::continuation_constructor_exists():
    assert callable(UMLModel::Continuation.__init__)


def test_umlmodel::continuation_constructor_args():
    sig = inspect.signature(UMLModel::Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_umlmodel::continuation_has_setting():
    assert hasattr(UMLModel::Continuation, "setting")
    descriptor = None
    for klass in UMLModel::Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::executionspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExecutionSpecification)


def test_umlmodel::executionspecification_constructor_exists():
    assert callable(UMLModel::ExecutionSpecification.__init__)


def test_umlmodel::executionspecification_constructor_args():
    sig = inspect.signature(UMLModel::ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "finish" in params, "Missing parameter 'finish'"

def test_umlmodel::executionspecification_has_start():
    assert hasattr(UMLModel::ExecutionSpecification, "start")
    descriptor = None
    for klass in UMLModel::ExecutionSpecification.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::executionspecification_has_finish():
    assert hasattr(UMLModel::ExecutionSpecification, "finish")
    descriptor = None
    for klass in UMLModel::ExecutionSpecification.__mro__:
        if "finish" in klass.__dict__:
            descriptor = klass.__dict__["finish"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CombinedFragment)


def test_umlmodel::combinedfragment_constructor_exists():
    assert callable(UMLModel::CombinedFragment.__init__)


def test_umlmodel::combinedfragment_constructor_args():
    sig = inspect.signature(UMLModel::CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_umlmodel::combinedfragment_has_interactionOperator():
    assert hasattr(UMLModel::CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in UMLModel::CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::componentrealization_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ComponentRealization)


def test_umlmodel::componentrealization_constructor_exists():
    assert callable(UMLModel::ComponentRealization.__init__)


def test_umlmodel::componentrealization_constructor_args():
    sig = inspect.signature(UMLModel::ComponentRealization.__init__)
    params = list(sig.parameters.keys())
    assert "realizingClassifier" in params, "Missing parameter 'realizingClassifier'"
    assert "abstraction" in params, "Missing parameter 'abstraction'"

def test_umlmodel::componentrealization_has_realizingClassifier():
    assert hasattr(UMLModel::ComponentRealization, "realizingClassifier")
    descriptor = None
    for klass in UMLModel::ComponentRealization.__mro__:
        if "realizingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["realizingClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::componentrealization_has_abstraction():
    assert hasattr(UMLModel::ComponentRealization, "abstraction")
    descriptor = None
    for klass in UMLModel::ComponentRealization.__mro__:
        if "abstraction" in klass.__dict__:
            descriptor = klass.__dict__["abstraction"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::packageableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel::PackageableElement)


def test_umlmodel::packageableelement_constructor_exists():
    assert callable(UMLModel::PackageableElement.__init__)


def test_umlmodel::packageableelement_constructor_args():
    sig = inspect.signature(UMLModel::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::component_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Component)


def test_umlmodel::component_constructor_exists():
    assert callable(UMLModel::Component.__init__)


def test_umlmodel::component_constructor_args():
    sig = inspect.signature(UMLModel::Component.__init__)
    params = list(sig.parameters.keys())
    assert "provided" in params, "Missing parameter 'provided'"
    assert "indirectlyInstantiated" in params, "Missing parameter 'indirectlyInstantiated'"
    assert "required" in params, "Missing parameter 'required'"

def test_umlmodel::component_has_provided():
    assert hasattr(UMLModel::Component, "provided")
    descriptor = None
    for klass in UMLModel::Component.__mro__:
        if "provided" in klass.__dict__:
            descriptor = klass.__dict__["provided"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::component_has_indirectlyInstantiated():
    assert hasattr(UMLModel::Component, "indirectlyInstantiated")
    descriptor = None
    for klass in UMLModel::Component.__mro__:
        if "indirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["indirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::component_has_required():
    assert hasattr(UMLModel::Component, "required")
    descriptor = None
    for klass in UMLModel::Component.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CommunicationPath)


def test_umlmodel::communicationpath_constructor_exists():
    assert callable(UMLModel::CommunicationPath.__init__)


def test_umlmodel::communicationpath_constructor_args():
    sig = inspect.signature(UMLModel::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::generalization_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Generalization)


def test_umlmodel::generalization_constructor_exists():
    assert callable(UMLModel::Generalization.__init__)


def test_umlmodel::generalization_constructor_args():
    sig = inspect.signature(UMLModel::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "generalizationSet" in params, "Missing parameter 'generalizationSet'"
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"
    assert "specific" in params, "Missing parameter 'specific'"
    assert "general" in params, "Missing parameter 'general'"

def test_umlmodel::generalization_has_generalizationSet():
    assert hasattr(UMLModel::Generalization, "generalizationSet")
    descriptor = None
    for klass in UMLModel::Generalization.__mro__:
        if "generalizationSet" in klass.__dict__:
            descriptor = klass.__dict__["generalizationSet"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::generalization_has_isSubstitutable():
    assert hasattr(UMLModel::Generalization, "isSubstitutable")
    descriptor = None
    for klass in UMLModel::Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::generalization_has_specific():
    assert hasattr(UMLModel::Generalization, "specific")
    descriptor = None
    for klass in UMLModel::Generalization.__mro__:
        if "specific" in klass.__dict__:
            descriptor = klass.__dict__["specific"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::generalization_has_general():
    assert hasattr(UMLModel::Generalization, "general")
    descriptor = None
    for klass in UMLModel::Generalization.__mro__:
        if "general" in klass.__dict__:
            descriptor = klass.__dict__["general"]
            break
    assert isinstance(descriptor, property)



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::property_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Property)


def test_umlmodel::property_constructor_exists():
    assert callable(UMLModel::Property.__init__)


def test_umlmodel::property_constructor_args():
    sig = inspect.signature(UMLModel::Property.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedProperty" in params, "Missing parameter 'redefinedProperty'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "opposite" in params, "Missing parameter 'opposite'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "default" in params, "Missing parameter 'default'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "association" in params, "Missing parameter 'association'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "owningAssociation" in params, "Missing parameter 'owningAssociation'"
    assert "associationEnd" in params, "Missing parameter 'associationEnd'"
    assert "datatype" in params, "Missing parameter 'datatype'"
    assert "subsettedProperty" in params, "Missing parameter 'subsettedProperty'"

def test_umlmodel::property_has_redefinedProperty():
    assert hasattr(UMLModel::Property, "redefinedProperty")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "redefinedProperty" in klass.__dict__:
            descriptor = klass.__dict__["redefinedProperty"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_aggregation():
    assert hasattr(UMLModel::Property, "aggregation")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_opposite():
    assert hasattr(UMLModel::Property, "opposite")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "opposite" in klass.__dict__:
            descriptor = klass.__dict__["opposite"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_isComposite():
    assert hasattr(UMLModel::Property, "isComposite")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_default():
    assert hasattr(UMLModel::Property, "default")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_class_():
    assert hasattr(UMLModel::Property, "class_")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_association():
    assert hasattr(UMLModel::Property, "association")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "association" in klass.__dict__:
            descriptor = klass.__dict__["association"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_isDerived():
    assert hasattr(UMLModel::Property, "isDerived")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_isDerivedUnion():
    assert hasattr(UMLModel::Property, "isDerivedUnion")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_owningAssociation():
    assert hasattr(UMLModel::Property, "owningAssociation")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "owningAssociation" in klass.__dict__:
            descriptor = klass.__dict__["owningAssociation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_associationEnd():
    assert hasattr(UMLModel::Property, "associationEnd")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "associationEnd" in klass.__dict__:
            descriptor = klass.__dict__["associationEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_datatype():
    assert hasattr(UMLModel::Property, "datatype")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "datatype" in klass.__dict__:
            descriptor = klass.__dict__["datatype"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::property_has_subsettedProperty():
    assert hasattr(UMLModel::Property, "subsettedProperty")
    descriptor = None
    for klass in UMLModel::Property.__mro__:
        if "subsettedProperty" in klass.__dict__:
            descriptor = klass.__dict__["subsettedProperty"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::operation_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Operation)


def test_umlmodel::operation_constructor_exists():
    assert callable(UMLModel::Operation.__init__)


def test_umlmodel::operation_constructor_args():
    sig = inspect.signature(UMLModel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "bodyCondition" in params, "Missing parameter 'bodyCondition'"
    assert "type" in params, "Missing parameter 'type'"
    assert "datatype" in params, "Missing parameter 'datatype'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "interface" in params, "Missing parameter 'interface'"
    assert "redefinedOperation" in params, "Missing parameter 'redefinedOperation'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_umlmodel::operation_has_isUnique():
    assert hasattr(UMLModel::Operation, "isUnique")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_precondition():
    assert hasattr(UMLModel::Operation, "precondition")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_upper():
    assert hasattr(UMLModel::Operation, "upper")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_bodyCondition():
    assert hasattr(UMLModel::Operation, "bodyCondition")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "bodyCondition" in klass.__dict__:
            descriptor = klass.__dict__["bodyCondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_type():
    assert hasattr(UMLModel::Operation, "type")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_datatype():
    assert hasattr(UMLModel::Operation, "datatype")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "datatype" in klass.__dict__:
            descriptor = klass.__dict__["datatype"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_class_():
    assert hasattr(UMLModel::Operation, "class_")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_interface():
    assert hasattr(UMLModel::Operation, "interface")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_redefinedOperation():
    assert hasattr(UMLModel::Operation, "redefinedOperation")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "redefinedOperation" in klass.__dict__:
            descriptor = klass.__dict__["redefinedOperation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_postcondition():
    assert hasattr(UMLModel::Operation, "postcondition")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_isOrdered():
    assert hasattr(UMLModel::Operation, "isOrdered")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_isQuery():
    assert hasattr(UMLModel::Operation, "isQuery")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::operation_has_lower():
    assert hasattr(UMLModel::Operation, "lower")
    descriptor = None
    for klass in UMLModel::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::stringexpression_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StringExpression)


def test_umlmodel::stringexpression_constructor_exists():
    assert callable(UMLModel::StringExpression.__init__)


def test_umlmodel::stringexpression_constructor_args():
    sig = inspect.signature(UMLModel::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "owningExpression" in params, "Missing parameter 'owningExpression'"

def test_umlmodel::stringexpression_has_owningExpression():
    assert hasattr(UMLModel::StringExpression, "owningExpression")
    descriptor = None
    for klass in UMLModel::StringExpression.__mro__:
        if "owningExpression" in klass.__dict__:
            descriptor = klass.__dict__["owningExpression"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::reception_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Reception)


def test_umlmodel::reception_constructor_exists():
    assert callable(UMLModel::Reception.__init__)


def test_umlmodel::reception_constructor_args():
    sig = inspect.signature(UMLModel::Reception.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel::reception_has_signal():
    assert hasattr(UMLModel::Reception, "signal")
    descriptor = None
    for klass in UMLModel::Reception.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::class_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Class)


def test_umlmodel::class_constructor_exists():
    assert callable(UMLModel::Class.__init__)


def test_umlmodel::class_constructor_args():
    sig = inspect.signature(UMLModel::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "superclass" in params, "Missing parameter 'superclass'"
    assert "extension" in params, "Missing parameter 'extension'"

def test_umlmodel::class_has_isActive():
    assert hasattr(UMLModel::Class, "isActive")
    descriptor = None
    for klass in UMLModel::Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::class_has_superclass():
    assert hasattr(UMLModel::Class, "superclass")
    descriptor = None
    for klass in UMLModel::Class.__mro__:
        if "superclass" in klass.__dict__:
            descriptor = klass.__dict__["superclass"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::class_has_extension():
    assert hasattr(UMLModel::Class, "extension")
    descriptor = None
    for klass in UMLModel::Class.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::executionevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ExecutionEvent)


def test_umlmodel::executionevent_constructor_exists():
    assert callable(UMLModel::ExecutionEvent.__init__)


def test_umlmodel::executionevent_constructor_args():
    sig = inspect.signature(UMLModel::ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::destructionevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::DestructionEvent)


def test_umlmodel::destructionevent_constructor_exists():
    assert callable(UMLModel::DestructionEvent.__init__)


def test_umlmodel::destructionevent_constructor_args():
    sig = inspect.signature(UMLModel::DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::messageevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::MessageEvent)


def test_umlmodel::messageevent_constructor_exists():
    assert callable(UMLModel::MessageEvent.__init__)


def test_umlmodel::messageevent_constructor_args():
    sig = inspect.signature(UMLModel::MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::timeevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::TimeEvent)


def test_umlmodel::timeevent_constructor_exists():
    assert callable(UMLModel::TimeEvent.__init__)


def test_umlmodel::timeevent_constructor_args():
    sig = inspect.signature(UMLModel::TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_umlmodel::timeevent_has_isRelative():
    assert hasattr(UMLModel::TimeEvent, "isRelative")
    descriptor = None
    for klass in UMLModel::TimeEvent.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::creationevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CreationEvent)


def test_umlmodel::creationevent_constructor_exists():
    assert callable(UMLModel::CreationEvent.__init__)


def test_umlmodel::creationevent_constructor_args():
    sig = inspect.signature(UMLModel::CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::changeevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ChangeEvent)


def test_umlmodel::changeevent_constructor_exists():
    assert callable(UMLModel::ChangeEvent.__init__)


def test_umlmodel::changeevent_constructor_args():
    sig = inspect.signature(UMLModel::ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CallOperationAction)


def test_umlmodel::calloperationaction_constructor_exists():
    assert callable(UMLModel::CallOperationAction.__init__)


def test_umlmodel::calloperationaction_constructor_args():
    sig = inspect.signature(UMLModel::CallOperationAction.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel::calloperationaction_has_operation():
    assert hasattr(UMLModel::CallOperationAction, "operation")
    descriptor = None
    for klass in UMLModel::CallOperationAction.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ConnectableElementTemplateParameter)


def test_umlmodel::connectableelementtemplateparameter_constructor_exists():
    assert callable(UMLModel::ConnectableElementTemplateParameter.__init__)


def test_umlmodel::connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(UMLModel::ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel::OperationTemplateParameter)


def test_umlmodel::operationtemplateparameter_constructor_exists():
    assert callable(UMLModel::OperationTemplateParameter.__init__)


def test_umlmodel::operationtemplateparameter_constructor_args():
    sig = inspect.signature(UMLModel::OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ClassifierTemplateParameter)


def test_umlmodel::classifiertemplateparameter_constructor_exists():
    assert callable(UMLModel::ClassifierTemplateParameter.__init__)


def test_umlmodel::classifiertemplateparameter_constructor_args():
    sig = inspect.signature(UMLModel::ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"
    assert "defaultClassifier" in params, "Missing parameter 'defaultClassifier'"
    assert "constrainingClassifier" in params, "Missing parameter 'constrainingClassifier'"

def test_umlmodel::classifiertemplateparameter_has_allowSubstitutable():
    assert hasattr(UMLModel::ClassifierTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in UMLModel::ClassifierTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifiertemplateparameter_has_defaultClassifier():
    assert hasattr(UMLModel::ClassifierTemplateParameter, "defaultClassifier")
    descriptor = None
    for klass in UMLModel::ClassifierTemplateParameter.__mro__:
        if "defaultClassifier" in klass.__dict__:
            descriptor = klass.__dict__["defaultClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifiertemplateparameter_has_constrainingClassifier():
    assert hasattr(UMLModel::ClassifierTemplateParameter, "constrainingClassifier")
    descriptor = None
    for klass in UMLModel::ClassifierTemplateParameter.__mro__:
        if "constrainingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["constrainingClassifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::usecase_is_not_abstract():
    assert not inspect.isabstract(UMLModel::UseCase)


def test_umlmodel::usecase_constructor_exists():
    assert callable(UMLModel::UseCase.__init__)


def test_umlmodel::usecase_constructor_args():
    sig = inspect.signature(UMLModel::UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"

def test_umlmodel::usecase_has_subject():
    assert hasattr(UMLModel::UseCase, "subject")
    descriptor = None
    for klass in UMLModel::UseCase.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::collaborationuse_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CollaborationUse)


def test_umlmodel::collaborationuse_constructor_exists():
    assert callable(UMLModel::CollaborationUse.__init__)


def test_umlmodel::collaborationuse_constructor_args():
    sig = inspect.signature(UMLModel::CollaborationUse.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_umlmodel::collaborationuse_has_type():
    assert hasattr(UMLModel::CollaborationUse, "type")
    descriptor = None
    for klass in UMLModel::CollaborationUse.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::substitution_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Substitution)


def test_umlmodel::substitution_constructor_exists():
    assert callable(UMLModel::Substitution.__init__)


def test_umlmodel::substitution_constructor_args():
    sig = inspect.signature(UMLModel::Substitution.__init__)
    params = list(sig.parameters.keys())
    assert "contract" in params, "Missing parameter 'contract'"
    assert "substitutingClassifier" in params, "Missing parameter 'substitutingClassifier'"

def test_umlmodel::substitution_has_contract():
    assert hasattr(UMLModel::Substitution, "contract")
    descriptor = None
    for klass in UMLModel::Substitution.__mro__:
        if "contract" in klass.__dict__:
            descriptor = klass.__dict__["contract"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::substitution_has_substitutingClassifier():
    assert hasattr(UMLModel::Substitution, "substitutingClassifier")
    descriptor = None
    for klass in UMLModel::Substitution.__mro__:
        if "substitutingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["substitutingClassifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::interfacerealization_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InterfaceRealization)


def test_umlmodel::interfacerealization_constructor_exists():
    assert callable(UMLModel::InterfaceRealization.__init__)


def test_umlmodel::interfacerealization_constructor_args():
    sig = inspect.signature(UMLModel::InterfaceRealization.__init__)
    params = list(sig.parameters.keys())
    assert "realizingClassifier" in params, "Missing parameter 'realizingClassifier'"
    assert "contract" in params, "Missing parameter 'contract'"

def test_umlmodel::interfacerealization_has_realizingClassifier():
    assert hasattr(UMLModel::InterfaceRealization, "realizingClassifier")
    descriptor = None
    for klass in UMLModel::InterfaceRealization.__mro__:
        if "realizingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["realizingClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::interfacerealization_has_contract():
    assert hasattr(UMLModel::InterfaceRealization, "contract")
    descriptor = None
    for klass in UMLModel::InterfaceRealization.__mro__:
        if "contract" in klass.__dict__:
            descriptor = klass.__dict__["contract"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel::BehavioredClassifier)


def test_umlmodel::behavioredclassifier_constructor_exists():
    assert callable(UMLModel::BehavioredClassifier.__init__)


def test_umlmodel::behavioredclassifier_constructor_args():
    sig = inspect.signature(UMLModel::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "classifierBehavior" in params, "Missing parameter 'classifierBehavior'"

def test_umlmodel::behavioredclassifier_has_classifierBehavior():
    assert hasattr(UMLModel::BehavioredClassifier, "classifierBehavior")
    descriptor = None
    for klass in UMLModel::BehavioredClassifier.__mro__:
        if "classifierBehavior" in klass.__dict__:
            descriptor = klass.__dict__["classifierBehavior"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::connector_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Connector)


def test_umlmodel::connector_constructor_exists():
    assert callable(UMLModel::Connector.__init__)


def test_umlmodel::connector_constructor_args():
    sig = inspect.signature(UMLModel::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "type" in params, "Missing parameter 'type'"
    assert "redefinedConnector" in params, "Missing parameter 'redefinedConnector'"
    assert "contract" in params, "Missing parameter 'contract'"

def test_umlmodel::connector_has_kind():
    assert hasattr(UMLModel::Connector, "kind")
    descriptor = None
    for klass in UMLModel::Connector.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::connector_has_type():
    assert hasattr(UMLModel::Connector, "type")
    descriptor = None
    for klass in UMLModel::Connector.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::connector_has_redefinedConnector():
    assert hasattr(UMLModel::Connector, "redefinedConnector")
    descriptor = None
    for klass in UMLModel::Connector.__mro__:
        if "redefinedConnector" in klass.__dict__:
            descriptor = klass.__dict__["redefinedConnector"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::connector_has_contract():
    assert hasattr(UMLModel::Connector, "contract")
    descriptor = None
    for klass in UMLModel::Connector.__mro__:
        if "contract" in klass.__dict__:
            descriptor = klass.__dict__["contract"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StructuralFeature)


def test_umlmodel::structuralfeature_constructor_exists():
    assert callable(UMLModel::StructuralFeature.__init__)


def test_umlmodel::structuralfeature_constructor_args():
    sig = inspect.signature(UMLModel::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_umlmodel::structuralfeature_has_isReadOnly():
    assert hasattr(UMLModel::StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in UMLModel::StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(UMLModel::InteractionOperand)


def test_umlmodel::interactionoperand_constructor_exists():
    assert callable(UMLModel::InteractionOperand.__init__)


def test_umlmodel::interactionoperand_constructor_args():
    sig = inspect.signature(UMLModel::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel::transition_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Transition)


def test_umlmodel::transition_constructor_exists():
    assert callable(UMLModel::Transition.__init__)


def test_umlmodel::transition_constructor_args():
    sig = inspect.signature(UMLModel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedTransition" in params, "Missing parameter 'redefinedTransition'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "source" in params, "Missing parameter 'source'"
    assert "container" in params, "Missing parameter 'container'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "target" in params, "Missing parameter 'target'"

def test_umlmodel::transition_has_redefinedTransition():
    assert hasattr(UMLModel::Transition, "redefinedTransition")
    descriptor = None
    for klass in UMLModel::Transition.__mro__:
        if "redefinedTransition" in klass.__dict__:
            descriptor = klass.__dict__["redefinedTransition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::transition_has_guard():
    assert hasattr(UMLModel::Transition, "guard")
    descriptor = None
    for klass in UMLModel::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::transition_has_source():
    assert hasattr(UMLModel::Transition, "source")
    descriptor = None
    for klass in UMLModel::Transition.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::transition_has_container():
    assert hasattr(UMLModel::Transition, "container")
    descriptor = None
    for klass in UMLModel::Transition.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::transition_has_kind():
    assert hasattr(UMLModel::Transition, "kind")
    descriptor = None
    for klass in UMLModel::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::transition_has_target():
    assert hasattr(UMLModel::Transition, "target")
    descriptor = None
    for klass in UMLModel::Transition.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::classifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Classifier)


def test_umlmodel::classifier_constructor_exists():
    assert callable(UMLModel::Classifier.__init__)


def test_umlmodel::classifier_constructor_args():
    sig = inspect.signature(UMLModel::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedClassifier" in params, "Missing parameter 'redefinedClassifier'"
    assert "general" in params, "Missing parameter 'general'"
    assert "feature" in params, "Missing parameter 'feature'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "inheritedMember" in params, "Missing parameter 'inheritedMember'"
    assert "representation" in params, "Missing parameter 'representation'"
    assert "useCase" in params, "Missing parameter 'useCase'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "powertypeExtent" in params, "Missing parameter 'powertypeExtent'"

def test_umlmodel::classifier_has_redefinedClassifier():
    assert hasattr(UMLModel::Classifier, "redefinedClassifier")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "redefinedClassifier" in klass.__dict__:
            descriptor = klass.__dict__["redefinedClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_general():
    assert hasattr(UMLModel::Classifier, "general")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "general" in klass.__dict__:
            descriptor = klass.__dict__["general"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_feature():
    assert hasattr(UMLModel::Classifier, "feature")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_isAbstract():
    assert hasattr(UMLModel::Classifier, "isAbstract")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_inheritedMember():
    assert hasattr(UMLModel::Classifier, "inheritedMember")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "inheritedMember" in klass.__dict__:
            descriptor = klass.__dict__["inheritedMember"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_representation():
    assert hasattr(UMLModel::Classifier, "representation")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "representation" in klass.__dict__:
            descriptor = klass.__dict__["representation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_useCase():
    assert hasattr(UMLModel::Classifier, "useCase")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "useCase" in klass.__dict__:
            descriptor = klass.__dict__["useCase"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_attribute():
    assert hasattr(UMLModel::Classifier, "attribute")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::classifier_has_powertypeExtent():
    assert hasattr(UMLModel::Classifier, "powertypeExtent")
    descriptor = None
    for klass in UMLModel::Classifier.__mro__:
        if "powertypeExtent" in klass.__dict__:
            descriptor = klass.__dict__["powertypeExtent"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::package_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Package)


def test_umlmodel::package_constructor_exists():
    assert callable(UMLModel::Package.__init__)


def test_umlmodel::package_constructor_args():
    sig = inspect.signature(UMLModel::Package.__init__)
    params = list(sig.parameters.keys())
    assert "nestedPackage" in params, "Missing parameter 'nestedPackage'"
    assert "nestingPackage" in params, "Missing parameter 'nestingPackage'"
    assert "ownedType" in params, "Missing parameter 'ownedType'"

def test_umlmodel::package_has_nestedPackage():
    assert hasattr(UMLModel::Package, "nestedPackage")
    descriptor = None
    for klass in UMLModel::Package.__mro__:
        if "nestedPackage" in klass.__dict__:
            descriptor = klass.__dict__["nestedPackage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::package_has_nestingPackage():
    assert hasattr(UMLModel::Package, "nestingPackage")
    descriptor = None
    for klass in UMLModel::Package.__mro__:
        if "nestingPackage" in klass.__dict__:
            descriptor = klass.__dict__["nestingPackage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::package_has_ownedType():
    assert hasattr(UMLModel::Package, "ownedType")
    descriptor = None
    for klass in UMLModel::Package.__mro__:
        if "ownedType" in klass.__dict__:
            descriptor = klass.__dict__["ownedType"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UMLModel::StructuredActivityNode)


def test_umlmodel::structuredactivitynode_constructor_exists():
    assert callable(UMLModel::StructuredActivityNode.__init__)


def test_umlmodel::structuredactivitynode_constructor_args():
    sig = inspect.signature(UMLModel::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_umlmodel::structuredactivitynode_has_mustIsolate():
    assert hasattr(UMLModel::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in UMLModel::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::region_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Region)


def test_umlmodel::region_constructor_exists():
    assert callable(UMLModel::Region.__init__)


def test_umlmodel::region_constructor_args():
    sig = inspect.signature(UMLModel::Region.__init__)
    params = list(sig.parameters.keys())
    assert "extendedRegion" in params, "Missing parameter 'extendedRegion'"
    assert "state" in params, "Missing parameter 'state'"
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"

def test_umlmodel::region_has_extendedRegion():
    assert hasattr(UMLModel::Region, "extendedRegion")
    descriptor = None
    for klass in UMLModel::Region.__mro__:
        if "extendedRegion" in klass.__dict__:
            descriptor = klass.__dict__["extendedRegion"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::region_has_state():
    assert hasattr(UMLModel::Region, "state")
    descriptor = None
    for klass in UMLModel::Region.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::region_has_stateMachine():
    assert hasattr(UMLModel::Region, "stateMachine")
    descriptor = None
    for klass in UMLModel::Region.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::state_is_not_abstract():
    assert not inspect.isabstract(UMLModel::State)


def test_umlmodel::state_constructor_exists():
    assert callable(UMLModel::State.__init__)


def test_umlmodel::state_constructor_args():
    sig = inspect.signature(UMLModel::State.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedState" in params, "Missing parameter 'redefinedState'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "submachine" in params, "Missing parameter 'submachine'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"

def test_umlmodel::state_has_redefinedState():
    assert hasattr(UMLModel::State, "redefinedState")
    descriptor = None
    for klass in UMLModel::State.__mro__:
        if "redefinedState" in klass.__dict__:
            descriptor = klass.__dict__["redefinedState"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::state_has_isOrthogonal():
    assert hasattr(UMLModel::State, "isOrthogonal")
    descriptor = None
    for klass in UMLModel::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::state_has_submachine():
    assert hasattr(UMLModel::State, "submachine")
    descriptor = None
    for klass in UMLModel::State.__mro__:
        if "submachine" in klass.__dict__:
            descriptor = klass.__dict__["submachine"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::state_has_isSimple():
    assert hasattr(UMLModel::State, "isSimple")
    descriptor = None
    for klass in UMLModel::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::state_has_isComposite():
    assert hasattr(UMLModel::State, "isComposite")
    descriptor = None
    for klass in UMLModel::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::state_has_isSubmachineState():
    assert hasattr(UMLModel::State, "isSubmachineState")
    descriptor = None
    for klass in UMLModel::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UMLModel::BehavioralFeature)


def test_umlmodel::behavioralfeature_constructor_exists():
    assert callable(UMLModel::BehavioralFeature.__init__)


def test_umlmodel::behavioralfeature_constructor_args():
    sig = inspect.signature(UMLModel::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "method" in params, "Missing parameter 'method'"
    assert "raisedException" in params, "Missing parameter 'raisedException'"

def test_umlmodel::behavioralfeature_has_isAbstract():
    assert hasattr(UMLModel::BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in UMLModel::BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavioralfeature_has_concurrency():
    assert hasattr(UMLModel::BehavioralFeature, "concurrency")
    descriptor = None
    for klass in UMLModel::BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavioralfeature_has_method():
    assert hasattr(UMLModel::BehavioralFeature, "method")
    descriptor = None
    for klass in UMLModel::BehavioralFeature.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavioralfeature_has_raisedException():
    assert hasattr(UMLModel::BehavioralFeature, "raisedException")
    descriptor = None
    for klass in UMLModel::BehavioralFeature.__mro__:
        if "raisedException" in klass.__dict__:
            descriptor = klass.__dict__["raisedException"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel::BehaviorExecutionSpecification)


def test_umlmodel::behaviorexecutionspecification_constructor_exists():
    assert callable(UMLModel::BehaviorExecutionSpecification.__init__)


def test_umlmodel::behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(UMLModel::BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"

def test_umlmodel::behaviorexecutionspecification_has_behavior():
    assert hasattr(UMLModel::BehaviorExecutionSpecification, "behavior")
    descriptor = None
    for klass in UMLModel::BehaviorExecutionSpecification.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::parameterset_is_not_abstract():
    assert not inspect.isabstract(UMLModel::ParameterSet)


def test_umlmodel::parameterset_constructor_exists():
    assert callable(UMLModel::ParameterSet.__init__)


def test_umlmodel::parameterset_constructor_args():
    sig = inspect.signature(UMLModel::ParameterSet.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_umlmodel::parameterset_has_parameter():
    assert hasattr(UMLModel::ParameterSet, "parameter")
    descriptor = None
    for klass in UMLModel::ParameterSet.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::parameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Parameter)


def test_umlmodel::parameter_constructor_exists():
    assert callable(UMLModel::Parameter.__init__)


def test_umlmodel::parameter_constructor_args():
    sig = inspect.signature(UMLModel::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "isException" in params, "Missing parameter 'isException'"
    assert "default" in params, "Missing parameter 'default'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "isStream" in params, "Missing parameter 'isStream'"
    assert "parameterSet" in params, "Missing parameter 'parameterSet'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel::parameter_has_isException():
    assert hasattr(UMLModel::Parameter, "isException")
    descriptor = None
    for klass in UMLModel::Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::parameter_has_default():
    assert hasattr(UMLModel::Parameter, "default")
    descriptor = None
    for klass in UMLModel::Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::parameter_has_effect():
    assert hasattr(UMLModel::Parameter, "effect")
    descriptor = None
    for klass in UMLModel::Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::parameter_has_isStream():
    assert hasattr(UMLModel::Parameter, "isStream")
    descriptor = None
    for klass in UMLModel::Parameter.__mro__:
        if "isStream" in klass.__dict__:
            descriptor = klass.__dict__["isStream"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::parameter_has_parameterSet():
    assert hasattr(UMLModel::Parameter, "parameterSet")
    descriptor = None
    for klass in UMLModel::Parameter.__mro__:
        if "parameterSet" in klass.__dict__:
            descriptor = klass.__dict__["parameterSet"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::parameter_has_direction():
    assert hasattr(UMLModel::Parameter, "direction")
    descriptor = None
    for klass in UMLModel::Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::parameter_has_operation():
    assert hasattr(UMLModel::Parameter, "operation")
    descriptor = None
    for klass in UMLModel::Parameter.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::callevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel::CallEvent)


def test_umlmodel::callevent_constructor_exists():
    assert callable(UMLModel::CallEvent.__init__)


def test_umlmodel::callevent_constructor_args():
    sig = inspect.signature(UMLModel::CallEvent.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel::callevent_has_operation():
    assert hasattr(UMLModel::CallEvent, "operation")
    descriptor = None
    for klass in UMLModel::CallEvent.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel::behavior_is_not_abstract():
    assert not inspect.isabstract(UMLModel::Behavior)


def test_umlmodel::behavior_constructor_exists():
    assert callable(UMLModel::Behavior.__init__)


def test_umlmodel::behavior_constructor_args():
    sig = inspect.signature(UMLModel::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "specification" in params, "Missing parameter 'specification'"
    assert "context" in params, "Missing parameter 'context'"
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "redefinedBahavior" in params, "Missing parameter 'redefinedBahavior'"

def test_umlmodel::behavior_has_postcondition():
    assert hasattr(UMLModel::Behavior, "postcondition")
    descriptor = None
    for klass in UMLModel::Behavior.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavior_has_specification():
    assert hasattr(UMLModel::Behavior, "specification")
    descriptor = None
    for klass in UMLModel::Behavior.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavior_has_context():
    assert hasattr(UMLModel::Behavior, "context")
    descriptor = None
    for klass in UMLModel::Behavior.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavior_has_isReentrant():
    assert hasattr(UMLModel::Behavior, "isReentrant")
    descriptor = None
    for klass in UMLModel::Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavior_has_precondition():
    assert hasattr(UMLModel::Behavior, "precondition")
    descriptor = None
    for klass in UMLModel::Behavior.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel::behavior_has_redefinedBahavior():
    assert hasattr(UMLModel::Behavior, "redefinedBahavior")
    descriptor = None
    for klass in UMLModel::Behavior.__mro__:
        if "redefinedBahavior" in klass.__dict__:
            descriptor = klass.__dict__["redefinedBahavior"]
            break
    assert isinstance(descriptor, property)

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

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "asynchCall",
        "deleteMessage",
        "asynchSignal",
        "createMessage",
        "synchCall",
        "reply",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "found",
        "unknown",
        "complete",
        "lost",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "break_",
        "strict",
        "consider",
        "alt",
        "opt",
        "assert_",
        "loop",
        "seq",
        "critical",
        "ignore",
        "neg",
        "par",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

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

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "return_",
        "inout",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "terminate",
        "junction",
        "entryPoint",
        "initial",
        "fork",
        "choice",
        "exitPoint",
        "shallowHistory",
        "deepHistory",
        "join",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "FIFO",
        "unordered",
        "ordered",
        "LIFO",
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
        "update",
        "create",
        "delete",
        "read",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "external",
        "local",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"


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
Expression_strategy = st.builds(
    Expression,
)
TemplateSignature_strategy = st.builds(
    TemplateSignature,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UMLModel::ReadLinkAction_strategy = st.builds(
    UMLModel::ReadLinkAction,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
Transition_strategy = st.builds(
    Transition,
)
UMLModel::ProtocolTransition_strategy = st.builds(
    UMLModel::ProtocolTransition,
    preCondition=
        safe_text,
    referred=
        safe_text,
    postCondition=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
UMLModel::PartDecomposition_strategy = st.builds(
    UMLModel::PartDecomposition,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
Package_strategy = st.builds(
    Package,
)
UMLModel::Profile_strategy = st.builds(
    UMLModel::Profile,
    metaclassReference=
        safe_text,
    metamodelReference=
        safe_text,
    ownedStereotype=
        safe_text
)
UMLModel::Model_strategy = st.builds(
    UMLModel::Model,
    viewpoint=
        safe_text
)
Abstraction_strategy = st.builds(
    Abstraction,
)
UMLModel::Realization_strategy = st.builds(
    UMLModel::Realization,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
UMLModel::LinkEndDestructionData_strategy = st.builds(
    UMLModel::LinkEndDestructionData,
    isDestroyDuplicates=
        safe_text,
    destroyAt=
        safe_text
)
UMLModel::LinkEndCreationData_strategy = st.builds(
    UMLModel::LinkEndCreationData,
    insertAt=
        safe_text,
    isReplaceAll=
        safe_text
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UMLModel::LiteralString_strategy = st.builds(
    UMLModel::LiteralString,
    value=
        safe_text
)
UMLModel::LiteralUnlimitedNatural_strategy = st.builds(
    UMLModel::LiteralUnlimitedNatural,
    value=
        safe_text
)
UMLModel::LiteralBoolean_strategy = st.builds(
    UMLModel::LiteralBoolean,
    value=
        safe_text
)
UMLModel::LiteralNull_strategy = st.builds(
    UMLModel::LiteralNull,
)
UMLModel::LiteralInteger_strategy = st.builds(
    UMLModel::LiteralInteger,
    value=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
UMLModel::IntervalConstraint_strategy = st.builds(
    UMLModel::IntervalConstraint,
)
UMLModel::InteractionConstraint_strategy = st.builds(
    UMLModel::InteractionConstraint,
)
Pin_strategy = st.builds(
    Pin,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
UMLModel::ProtocolStateMachine_strategy = st.builds(
    UMLModel::ProtocolStateMachine,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
UMLModel::FunctionBehavior_strategy = st.builds(
    UMLModel::FunctionBehavior,
)
State_strategy = st.builds(
    State,
)
UMLModel::FinalState_strategy = st.builds(
    UMLModel::FinalState,
)
Property_strategy = st.builds(
    Property,
)
UMLModel::Port_strategy = st.builds(
    UMLModel::Port,
    isService=
        safe_text,
    provided=
        safe_text,
    protocol=
        safe_text,
    required=
        safe_text,
    redefinedPort=
        safe_text,
    isBehavior=
        safe_text
)
UMLModel::ExtensionEnd_strategy = st.builds(
    UMLModel::ExtensionEnd,
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
UMLModel::MessageOccurrenceSpecification_strategy = st.builds(
    UMLModel::MessageOccurrenceSpecification,
)
UMLModel::ExecutionOccurrenceSpecification_strategy = st.builds(
    UMLModel::ExecutionOccurrenceSpecification,
    execution=
        safe_text
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
UMLModel::WriteLinkAction_strategy = st.builds(
    UMLModel::WriteLinkAction,
)
EObject_strategy = st.builds(
    EObject,
)
UMLModel::UMLBase_strategy = st.builds(
    UMLModel::UMLBase,
    umlID=
        safe_text
)
CallAction_strategy = st.builds(
    CallAction,
)
UMLModel::CallBehaviorAction_strategy = st.builds(
    UMLModel::CallBehaviorAction,
    behavior=
        safe_text
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
UMLModel::CallAction_strategy = st.builds(
    UMLModel::CallAction,
    isSynchronous=
        safe_text
)
UMLModel::SendObjectAction_strategy = st.builds(
    UMLModel::SendObjectAction,
)
UMLModel::SendSignalAction_strategy = st.builds(
    UMLModel::SendSignalAction,
    signal=
        safe_text
)
UMLModel::BroadcastSignalAction_strategy = st.builds(
    UMLModel::BroadcastSignalAction,
    signal=
        safe_text
)
UMLModel::Manifestation_strategy = st.builds(
    UMLModel::Manifestation,
    utilizedElement=
        safe_text
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
Classifier_strategy = st.builds(
    Classifier,
)
UMLModel::StructuredClassifier_strategy = st.builds(
    UMLModel::StructuredClassifier,
    part=
        safe_text,
    role=
        safe_text
)
UMLModel::InformationItem_strategy = st.builds(
    UMLModel::InformationItem,
    represented=
        safe_text
)
UMLModel::Signal_strategy = st.builds(
    UMLModel::Signal,
)
UMLModel::Interface_strategy = st.builds(
    UMLModel::Interface,
    redefinedInterface=
        safe_text,
    isActive=
        st.booleans()
)
UMLModel::Artifact_strategy = st.builds(
    UMLModel::Artifact,
    fileName=
        safe_text
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
UMLModel::SignalEvent_strategy = st.builds(
    UMLModel::SignalEvent,
    signal=
        safe_text
)
UMLModel::ReceiveOperationEvent_strategy = st.builds(
    UMLModel::ReceiveOperationEvent,
    operation=
        safe_text
)
UMLModel::SendSignalEvent_strategy = st.builds(
    UMLModel::SendSignalEvent,
    signal=
        safe_text
)
UMLModel::ReceiveSignalEvent_strategy = st.builds(
    UMLModel::ReceiveSignalEvent,
    signal=
        safe_text
)
UMLModel::AnyReceiveEvent_strategy = st.builds(
    UMLModel::AnyReceiveEvent,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UMLModel::RemoveVariableValueAction_strategy = st.builds(
    UMLModel::RemoveVariableValueAction,
    isRemoveDuplicates=
        safe_text
)
UMLModel::AddVariableValueAction_strategy = st.builds(
    UMLModel::AddVariableValueAction,
    isReplaceAll=
        safe_text
)
UMLModel::InputPin_strategy = st.builds(
    UMLModel::InputPin,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UMLModel::RemoveStructuralFeatureValueAction_strategy = st.builds(
    UMLModel::RemoveStructuralFeatureValueAction,
    isRemoveDuplicates=
        safe_text
)
UMLModel::AddStructuralFeatureValueAction_strategy = st.builds(
    UMLModel::AddStructuralFeatureValueAction,
    isReplaceAll=
        safe_text
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UMLModel::Actor_strategy = st.builds(
    UMLModel::Actor,
)
Association_strategy = st.builds(
    Association,
)
UMLModel::Extension_strategy = st.builds(
    UMLModel::Extension,
    metaClass=
        safe_text,
    isRequired=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
UMLModel::Stereotype_strategy = st.builds(
    UMLModel::Stereotype,
)
UMLModel::Node_strategy = st.builds(
    UMLModel::Node,
)
UMLModel::AssociationClass_strategy = st.builds(
    UMLModel::AssociationClass,
)
Relationship_strategy = st.builds(
    Relationship,
)
UMLModel::Association_strategy = st.builds(
    UMLModel::Association,
    navigableOwnedEnd=
        safe_text,
    memberEnd=
        safe_text,
    isDerived=
        safe_text,
    endType=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
UMLModel::ParameterableElement_strategy = st.builds(
    UMLModel::ParameterableElement,
    templateParameter=
        safe_text,
    owningTemplateParameter=
        safe_text
)
UMLModel::Relationship_strategy = st.builds(
    UMLModel::Relationship,
    relatedElement=
        safe_text
)
UMLModel::MultiplicityElement_strategy = st.builds(
    UMLModel::MultiplicityElement,
    isOrdered=
        safe_text,
    isUnique=
        safe_text,
    upper=
        safe_text,
    lower=
        safe_text
)
UMLModel::LinkEndData_strategy = st.builds(
    UMLModel::LinkEndData,
    end=
        safe_text,
    value=
        safe_text
)
UMLModel::Image_strategy = st.builds(
    UMLModel::Image,
    location=
        safe_text,
    format=
        safe_text,
    content=
        safe_text
)
UMLModel::Slot_strategy = st.builds(
    UMLModel::Slot,
    definingFeature=
        safe_text,
    owningInstance=
        safe_text
)
UMLModel::TemplateSignature_strategy = st.builds(
    UMLModel::TemplateSignature,
    parameter=
        safe_text,
    template=
        safe_text
)
UMLModel::NamedElement_strategy = st.builds(
    UMLModel::NamedElement,
    visibility=
        safe_text,
    namespace=
        safe_text,
    clientDependency=
        safe_text,
    qualifiedName=
        safe_text,
    name=
        safe_text
)
UMLModel::TemplateableElement_strategy = st.builds(
    UMLModel::TemplateableElement,
)
UMLModel::TemplateParameter_strategy = st.builds(
    UMLModel::TemplateParameter,
    parameteredElement=
        safe_text,
    default=
        safe_text,
    signature=
        safe_text
)
UMLModel::QualifierValue_strategy = st.builds(
    UMLModel::QualifierValue,
    value=
        safe_text,
    qualifier=
        safe_text
)
UMLModel::ExceptionHandler_strategy = st.builds(
    UMLModel::ExceptionHandler,
    exceptionInput=
        safe_text,
    handlerBody=
        safe_text,
    exceptionType=
        safe_text,
    protectedNode=
        safe_text
)
UMLModel::TemplateParameterSubstitution_strategy = st.builds(
    UMLModel::TemplateParameterSubstitution,
    formal=
        safe_text,
    actual=
        safe_text,
    templateBinding=
        safe_text
)
FinalNode_strategy = st.builds(
    FinalNode,
)
UMLModel::FlowFinalNode_strategy = st.builds(
    UMLModel::FlowFinalNode,
)
UMLModel::ActivityFinalNode_strategy = st.builds(
    UMLModel::ActivityFinalNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UMLModel::ExpansionNode_strategy = st.builds(
    UMLModel::ExpansionNode,
    regionAsOutput=
        safe_text,
    regionAsInput=
        safe_text
)
UMLModel::ActivityParameterNode_strategy = st.builds(
    UMLModel::ActivityParameterNode,
    parameter=
        safe_text
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
UMLModel::Feature_strategy = st.builds(
    UMLModel::Feature,
    featuringClassifier=
        safe_text,
    isStatic=
        safe_text
)
UMLModel::RedefinableTemplateSignature_strategy = st.builds(
    UMLModel::RedefinableTemplateSignature,
    extendedSignature=
        safe_text,
    classifier=
        safe_text,
    inheritedParameter=
        safe_text
)
UMLModel::ExtensionPoint_strategy = st.builds(
    UMLModel::ExtensionPoint,
    useCase=
        safe_text
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
UMLModel::InterruptibleActivityRegion_strategy = st.builds(
    UMLModel::InterruptibleActivityRegion,
    node=
        safe_text,
    interruptingEdge=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
UMLModel::TypedElement_strategy = st.builds(
    UMLModel::TypedElement,
    type=
        safe_text
)
UMLModel::InteractionFragment_strategy = st.builds(
    UMLModel::InteractionFragment,
    enclosingOperand=
        safe_text,
    enclosingInteraction=
        safe_text,
    covered=
        safe_text
)
UMLModel::Vertex_strategy = st.builds(
    UMLModel::Vertex,
    outgoing=
        safe_text,
    incoming=
        safe_text,
    container=
        safe_text
)
UMLModel::GeneralOrdering_strategy = st.builds(
    UMLModel::GeneralOrdering,
    before=
        safe_text,
    after=
        safe_text
)
UMLModel::Namespace_strategy = st.builds(
    UMLModel::Namespace,
    ownedMember=
        safe_text,
    importedMember=
        safe_text,
    member=
        safe_text
)
UMLModel::RedefinableElement_strategy = st.builds(
    UMLModel::RedefinableElement,
    isLeaf=
        safe_text,
    redefinedElement=
        safe_text,
    redefinitionContext=
        safe_text
)
UMLModel::Lifeline_strategy = st.builds(
    UMLModel::Lifeline,
    interaction=
        safe_text,
    decomposedAs=
        safe_text,
    coveredBy=
        safe_text,
    represents=
        safe_text
)
UMLModel::MessageEnd_strategy = st.builds(
    UMLModel::MessageEnd,
    message=
        safe_text
)
UMLModel::Message_strategy = st.builds(
    UMLModel::Message,
    sendEvent=
        safe_text,
    interaction=
        safe_text,
    messageKind=
        safe_text,
    connector=
        safe_text,
    messageSort=
        safe_text,
    receiveEvent=
        safe_text,
    signature=
        safe_text
)
UMLModel::ActivityPartition_strategy = st.builds(
    UMLModel::ActivityPartition,
    node=
        safe_text,
    isExternal=
        safe_text,
    isDimension=
        safe_text,
    superPartition=
        safe_text,
    represents=
        safe_text,
    edge=
        safe_text,
    subpartition=
        safe_text
)
UMLModel::ActivityNode_strategy = st.builds(
    UMLModel::ActivityNode,
    inStructuredNode=
        safe_text,
    inGroup=
        safe_text,
    inPartition=
        safe_text,
    redefinedNode=
        safe_text,
    activity=
        safe_text,
    outgoing=
        safe_text,
    incoming=
        safe_text,
    inInterruptibleRegion=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
UMLModel::StateMachine_strategy = st.builds(
    UMLModel::StateMachine,
    extendedStateMachine=
        safe_text,
    submachineState=
        safe_text
)
UMLModel::OpaqueBehavior_strategy = st.builds(
    UMLModel::OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
UMLModel::Activity_strategy = st.builds(
    UMLModel::Activity,
    isSingleExecution=
        safe_text,
    isReadOnly=
        safe_text,
    partition=
        safe_text,
    structuredNode=
        safe_text
)
InputPin_strategy = st.builds(
    InputPin,
)
UMLModel::ValuePin_strategy = st.builds(
    UMLModel::ValuePin,
)
UMLModel::ActionInputPin_strategy = st.builds(
    UMLModel::ActionInputPin,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
UMLModel::ActionExecutionSpecification_strategy = st.builds(
    UMLModel::ActionExecutionSpecification,
    action=
        safe_text
)
UMLModel::ActivityGroup_strategy = st.builds(
    UMLModel::ActivityGroup,
    subgroup=
        safe_text,
    superGroup=
        safe_text,
    inActivity=
        safe_text
)
UMLModel::ActivityEdge_strategy = st.builds(
    UMLModel::ActivityEdge,
    interrupts=
        safe_text,
    source=
        safe_text,
    inGroup=
        safe_text,
    redefinedEdge=
        safe_text,
    inPartition=
        safe_text,
    target=
        safe_text,
    activity=
        safe_text,
    inStructuredNode=
        safe_text
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
UMLModel::AcceptCallAction_strategy = st.builds(
    UMLModel::AcceptCallAction,
)
Dependency_strategy = st.builds(
    Dependency,
)
UMLModel::Usage_strategy = st.builds(
    UMLModel::Usage,
)
UMLModel::Abstraction_strategy = st.builds(
    UMLModel::Abstraction,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
UMLModel::Action_strategy = st.builds(
    UMLModel::Action,
    input=
        safe_text,
    context=
        safe_text,
    output=
        safe_text
)
UMLModel::Trigger_strategy = st.builds(
    UMLModel::Trigger,
    event=
        safe_text,
    port=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
UMLModel::VariableAction_strategy = st.builds(
    UMLModel::VariableAction,
    variable=
        safe_text
)
UMLModel::UnmarshallAction_strategy = st.builds(
    UMLModel::UnmarshallAction,
    unmarshallType=
        safe_text
)
UMLModel::TestIdentityAction_strategy = st.builds(
    UMLModel::TestIdentityAction,
)
UMLModel::StartClassifierBehaviorAction_strategy = st.builds(
    UMLModel::StartClassifierBehaviorAction,
)
UMLModel::RaiseExceptionAction_strategy = st.builds(
    UMLModel::RaiseExceptionAction,
)
UMLModel::ReadExtentAction_strategy = st.builds(
    UMLModel::ReadExtentAction,
    classifier=
        safe_text
)
UMLModel::ReclassifyObjectAction_strategy = st.builds(
    UMLModel::ReclassifyObjectAction,
    isReplaceAll=
        safe_text,
    oldClassifier=
        safe_text,
    newClassifier=
        safe_text
)
UMLModel::InvocationAction_strategy = st.builds(
    UMLModel::InvocationAction,
    onPort=
        safe_text
)
UMLModel::ReadIsClassifiedObjectAction_strategy = st.builds(
    UMLModel::ReadIsClassifiedObjectAction,
    classifier=
        safe_text,
    isDirect=
        safe_text
)
UMLModel::ReadLinkObjectEndAction_strategy = st.builds(
    UMLModel::ReadLinkObjectEndAction,
    end=
        safe_text
)
UMLModel::ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UMLModel::ReadLinkObjectEndQualifierAction,
    qualifier=
        safe_text
)
UMLModel::OpaqueAction_strategy = st.builds(
    UMLModel::OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
UMLModel::LinkAction_strategy = st.builds(
    UMLModel::LinkAction,
)
UMLModel::ValueSpecificationAction_strategy = st.builds(
    UMLModel::ValueSpecificationAction,
)
UMLModel::ReduceAction_strategy = st.builds(
    UMLModel::ReduceAction,
    isOrdered=
        safe_text,
    reducer=
        safe_text
)
UMLModel::ReplyAction_strategy = st.builds(
    UMLModel::ReplyAction,
    replyToCall=
        safe_text
)
UMLModel::StructuralFeatureAction_strategy = st.builds(
    UMLModel::StructuralFeatureAction,
    structuralFeature=
        safe_text
)
UMLModel::ReadSelfAction_strategy = st.builds(
    UMLModel::ReadSelfAction,
)
UMLModel::AcceptEventAction_strategy = st.builds(
    UMLModel::AcceptEventAction,
    isUnmarshall=
        safe_text
)
UMLModel::OutputPin_strategy = st.builds(
    UMLModel::OutputPin,
)
UMLBase_strategy = st.builds(
    UMLBase,
)
UMLModel::Element_strategy = st.builds(
    UMLModel::Element,
    href=
        safe_text,
    owner=
        safe_text,
    ownedElement=
        safe_text
)
Observation_strategy = st.builds(
    Observation,
)
UMLModel::TimeObservation_strategy = st.builds(
    UMLModel::TimeObservation,
    firstEvent=
        safe_text,
    event=
        safe_text
)
UMLModel::DurationObservation_strategy = st.builds(
    UMLModel::DurationObservation,
    event=
        safe_text,
    firstEvent=
        safe_text
)
Interval_strategy = st.builds(
    Interval,
)
UMLModel::TimeInterval_strategy = st.builds(
    UMLModel::TimeInterval,
)
UMLModel::DurationInterval_strategy = st.builds(
    UMLModel::DurationInterval,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
UMLModel::TimeConstraint_strategy = st.builds(
    UMLModel::TimeConstraint,
    firstEvent=
        safe_text
)
UMLModel::DurationConstraint_strategy = st.builds(
    UMLModel::DurationConstraint,
    firstEvent=
        safe_text
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UMLModel::LiteralSpecification_strategy = st.builds(
    UMLModel::LiteralSpecification,
)
UMLModel::Interval_strategy = st.builds(
    UMLModel::Interval,
    max=
        safe_text,
    min=
        safe_text
)
UMLModel::InstanceValue_strategy = st.builds(
    UMLModel::InstanceValue,
    instance=
        safe_text
)
UMLModel::OpaqueExpression_strategy = st.builds(
    UMLModel::OpaqueExpression,
    behavior=
        safe_text,
    body=
        safe_text,
    language=
        safe_text,
    result=
        safe_text
)
UMLModel::TimeExpression_strategy = st.builds(
    UMLModel::TimeExpression,
    expr=
        safe_text,
    observation=
        safe_text
)
UMLModel::Expression_strategy = st.builds(
    UMLModel::Expression,
    symbol=
        safe_text
)
UMLModel::Duration_strategy = st.builds(
    UMLModel::Duration,
    observation=
        safe_text,
    expr=
        safe_text
)
UMLModel::EnumerationLiteral_strategy = st.builds(
    UMLModel::EnumerationLiteral,
    enumeration=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
UMLModel::PrimitiveType_strategy = st.builds(
    UMLModel::PrimitiveType,
)
UMLModel::Enumeration_strategy = st.builds(
    UMLModel::Enumeration,
)
UMLModel::DestroyObjectAction_strategy = st.builds(
    UMLModel::DestroyObjectAction,
    isDestroyOwnedObjects=
        safe_text,
    isDestroyLinks=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
UMLModel::ExecutionEnvironment_strategy = st.builds(
    UMLModel::ExecutionEnvironment,
)
UMLModel::Device_strategy = st.builds(
    UMLModel::Device,
)
UMLModel::DirectedRelationship_strategy = st.builds(
    UMLModel::DirectedRelationship,
    source=
        safe_text,
    target=
        safe_text
)
Artifact_strategy = st.builds(
    Artifact,
)
UMLModel::DeployedArtifact_strategy = st.builds(
    UMLModel::DeployedArtifact,
)
UMLModel::DeploymentSpecification_strategy = st.builds(
    UMLModel::DeploymentSpecification,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text,
    deployment=
        safe_text
)
UMLModel::Deployment_strategy = st.builds(
    UMLModel::Deployment,
    location=
        safe_text,
    deployedArtifact=
        safe_text
)
UMLModel::DeploymentTarget_strategy = st.builds(
    UMLModel::DeploymentTarget,
    deployedElement=
        safe_text
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
UMLModel::Pin_strategy = st.builds(
    UMLModel::Pin,
    isControl=
        safe_text
)
UMLModel::Variable_strategy = st.builds(
    UMLModel::Variable,
    activityScope=
        safe_text,
    scope=
        safe_text
)
UMLModel::ConnectorEnd_strategy = st.builds(
    UMLModel::ConnectorEnd,
    role=
        safe_text,
    definingEnd=
        safe_text,
    partWithPort=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
UMLModel::Extend_strategy = st.builds(
    UMLModel::Extend,
    extensionLocation=
        safe_text,
    extension=
        safe_text,
    extendedCase=
        safe_text
)
UMLModel::ProtocolConformance_strategy = st.builds(
    UMLModel::ProtocolConformance,
    specificMachine=
        safe_text,
    generalMachine=
        safe_text
)
UMLModel::ElementImport_strategy = st.builds(
    UMLModel::ElementImport,
    visibility=
        safe_text,
    alias=
        safe_text,
    importingNamespace=
        safe_text
)
UMLModel::Include_strategy = st.builds(
    UMLModel::Include,
    addition=
        safe_text,
    includingCase=
        safe_text
)
UMLModel::TemplateBinding_strategy = st.builds(
    UMLModel::TemplateBinding,
    signature=
        safe_text,
    boundElement=
        safe_text
)
UMLModel::ProfileApplication_strategy = st.builds(
    UMLModel::ProfileApplication,
    appliedProfile=
        safe_text,
    applyingPackage=
        safe_text,
    isStrict=
        safe_text
)
UMLModel::PackageMerge_strategy = st.builds(
    UMLModel::PackageMerge,
    receivingPackage=
        safe_text,
    mergedPackage=
        safe_text
)
UMLModel::PackageImport_strategy = st.builds(
    UMLModel::PackageImport,
    visibility=
        safe_text,
    importingNamespace=
        safe_text
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
UMLModel::ForkNode_strategy = st.builds(
    UMLModel::ForkNode,
)
UMLModel::JoinNode_strategy = st.builds(
    UMLModel::JoinNode,
    isCombineDuplicate=
        safe_text
)
UMLModel::FinalNode_strategy = st.builds(
    UMLModel::FinalNode,
)
UMLModel::MergeNode_strategy = st.builds(
    UMLModel::MergeNode,
)
UMLModel::InitialNode_strategy = st.builds(
    UMLModel::InitialNode,
)
UMLModel::ConnectableElement_strategy = st.builds(
    UMLModel::ConnectableElement,
    end=
        safe_text
)
UMLModel::DecisionNode_strategy = st.builds(
    UMLModel::DecisionNode,
    decisionInput=
        safe_text
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
UMLModel::ConsiderIgnoreFragment_strategy = st.builds(
    UMLModel::ConsiderIgnoreFragment,
    message=
        safe_text
)
UMLModel::DataType_strategy = st.builds(
    UMLModel::DataType,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UMLModel::DataStoreNode_strategy = st.builds(
    UMLModel::DataStoreNode,
)
UMLModel::CentralBufferNode_strategy = st.builds(
    UMLModel::CentralBufferNode,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
UMLModel::DestroyLinkAction_strategy = st.builds(
    UMLModel::DestroyLinkAction,
)
UMLModel::CreateLinkAction_strategy = st.builds(
    UMLModel::CreateLinkAction,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
UMLModel::Type_strategy = st.builds(
    UMLModel::Type,
    package=
        safe_text
)
UMLModel::Event_strategy = st.builds(
    UMLModel::Event,
)
UMLModel::Observation_strategy = st.builds(
    UMLModel::Observation,
)
UMLModel::InstanceSpecification_strategy = st.builds(
    UMLModel::InstanceSpecification,
    classifier=
        safe_text
)
UMLModel::GeneralizationSet_strategy = st.builds(
    UMLModel::GeneralizationSet,
    isDisjoint=
        safe_text,
    generalization=
        safe_text,
    powerType=
        safe_text,
    isCovering=
        safe_text
)
UMLModel::ValueSpecification_strategy = st.builds(
    UMLModel::ValueSpecification,
)
UMLModel::InformationFlow_strategy = st.builds(
    UMLModel::InformationFlow,
    realizingActivityEdge=
        safe_text,
    realizingConnector=
        safe_text,
    realization=
        safe_text,
    informationTarget=
        safe_text,
    realizingMessage=
        safe_text,
    informationSource=
        safe_text,
    conveyed=
        safe_text
)
UMLModel::Constraint_strategy = st.builds(
    UMLModel::Constraint,
    constrainedElement=
        safe_text,
    context=
        safe_text
)
UMLModel::CreateObjectAction_strategy = st.builds(
    UMLModel::CreateObjectAction,
    classifier=
        safe_text
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
UMLModel::CreateLinkObjectAction_strategy = st.builds(
    UMLModel::CreateLinkObjectAction,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
UMLModel::ExpansionRegion_strategy = st.builds(
    UMLModel::ExpansionRegion,
    mode=
        safe_text,
    inputElement=
        safe_text,
    outputElement=
        safe_text
)
UMLModel::SequenceNode_strategy = st.builds(
    UMLModel::SequenceNode,
)
UMLModel::LoopNode_strategy = st.builds(
    UMLModel::LoopNode,
    decider=
        safe_text,
    bodyOutput=
        safe_text,
    loopVariable=
        safe_text,
    bodyPart=
        safe_text,
    setupPart=
        safe_text,
    isTestedFirst=
        safe_text,
    test=
        safe_text
)
UMLModel::ConditionalNode_strategy = st.builds(
    UMLModel::ConditionalNode,
    isDeterminate=
        safe_text,
    isAssured=
        safe_text
)
UMLModel::Gate_strategy = st.builds(
    UMLModel::Gate,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
UMLModel::ObjectNode_strategy = st.builds(
    UMLModel::ObjectNode,
    selection=
        safe_text,
    ordering=
        safe_text,
    inState=
        safe_text,
    isControlType=
        safe_text
)
UMLModel::ExecutableNode_strategy = st.builds(
    UMLModel::ExecutableNode,
)
UMLModel::ControlNode_strategy = st.builds(
    UMLModel::ControlNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
UMLModel::ObjectFlow_strategy = st.builds(
    UMLModel::ObjectFlow,
    isMultireceive=
        safe_text,
    transformation=
        safe_text,
    isMulticast=
        safe_text,
    selection=
        safe_text
)
UMLModel::ControlFlow_strategy = st.builds(
    UMLModel::ControlFlow,
)
Vertex_strategy = st.builds(
    Vertex,
)
UMLModel::Pseudostate_strategy = st.builds(
    UMLModel::Pseudostate,
    kind=
        safe_text,
    state=
        safe_text,
    stateMachine=
        safe_text
)
UMLModel::ConnectionPointReference_strategy = st.builds(
    UMLModel::ConnectionPointReference,
    state=
        safe_text,
    entry=
        safe_text,
    exit=
        safe_text
)
UMLModel::Comment_strategy = st.builds(
    UMLModel::Comment,
    body=
        safe_text,
    annotatedElement=
        safe_text
)
UMLModel::Dependency_strategy = st.builds(
    UMLModel::Dependency,
    client=
        safe_text,
    supplier=
        safe_text
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UMLModel::EncapsulatedClassifier_strategy = st.builds(
    UMLModel::EncapsulatedClassifier,
    ownedPort=
        safe_text
)
UMLModel::Collaboration_strategy = st.builds(
    UMLModel::Collaboration,
    collaborationRole=
        safe_text
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UMLModel::ReadStructuralFeatureAction_strategy = st.builds(
    UMLModel::ReadStructuralFeatureAction,
)
UMLModel::WriteStructuralFeatureAction_strategy = st.builds(
    UMLModel::WriteStructuralFeatureAction,
)
UMLModel::ClearStructuralFeatureAction_strategy = st.builds(
    UMLModel::ClearStructuralFeatureAction,
)
UMLModel::ClearAssociationAction_strategy = st.builds(
    UMLModel::ClearAssociationAction,
    association=
        safe_text
)
VariableAction_strategy = st.builds(
    VariableAction,
)
UMLModel::ReadVariableAction_strategy = st.builds(
    UMLModel::ReadVariableAction,
)
UMLModel::WriteVariableAction_strategy = st.builds(
    UMLModel::WriteVariableAction,
)
UMLModel::ClearVariableAction_strategy = st.builds(
    UMLModel::ClearVariableAction,
)
UMLModel::Clause_strategy = st.builds(
    UMLModel::Clause,
    bodyOutput=
        safe_text,
    predecessorClause=
        safe_text,
    test=
        safe_text,
    decider=
        safe_text,
    body=
        safe_text,
    successorClause=
        safe_text
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
UMLModel::StateInvariant_strategy = st.builds(
    UMLModel::StateInvariant,
)
UMLModel::OccurrenceSpecification_strategy = st.builds(
    UMLModel::OccurrenceSpecification,
    toAfter=
        safe_text,
    event=
        safe_text,
    toBefore=
        safe_text
)
UMLModel::InteractionUse_strategy = st.builds(
    UMLModel::InteractionUse,
    refersTo=
        safe_text
)
UMLModel::Interaction_strategy = st.builds(
    UMLModel::Interaction,
)
UMLModel::Continuation_strategy = st.builds(
    UMLModel::Continuation,
    setting=
        safe_text
)
UMLModel::ExecutionSpecification_strategy = st.builds(
    UMLModel::ExecutionSpecification,
    start=
        safe_text,
    finish=
        safe_text
)
UMLModel::CombinedFragment_strategy = st.builds(
    UMLModel::CombinedFragment,
    interactionOperator=
        safe_text
)
Realization_strategy = st.builds(
    Realization,
)
UMLModel::ComponentRealization_strategy = st.builds(
    UMLModel::ComponentRealization,
    realizingClassifier=
        safe_text,
    abstraction=
        safe_text
)
UMLModel::PackageableElement_strategy = st.builds(
    UMLModel::PackageableElement,
)
UMLModel::Component_strategy = st.builds(
    UMLModel::Component,
    provided=
        safe_text,
    indirectlyInstantiated=
        safe_text,
    required=
        safe_text
)
UMLModel::CommunicationPath_strategy = st.builds(
    UMLModel::CommunicationPath,
)
UMLModel::Generalization_strategy = st.builds(
    UMLModel::Generalization,
    generalizationSet=
        safe_text,
    isSubstitutable=
        safe_text,
    specific=
        safe_text,
    general=
        safe_text
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
UMLModel::Property_strategy = st.builds(
    UMLModel::Property,
    redefinedProperty=
        safe_text,
    aggregation=
        safe_text,
    opposite=
        safe_text,
    isComposite=
        safe_text,
    default=
        safe_text,
    class_=
        safe_text,
    association=
        safe_text,
    isDerived=
        safe_text,
    isDerivedUnion=
        safe_text,
    owningAssociation=
        safe_text,
    associationEnd=
        safe_text,
    datatype=
        safe_text,
    subsettedProperty=
        safe_text
)
UMLModel::Operation_strategy = st.builds(
    UMLModel::Operation,
    isUnique=
        safe_text,
    precondition=
        safe_text,
    upper=
        safe_text,
    bodyCondition=
        safe_text,
    type=
        safe_text,
    datatype=
        safe_text,
    class_=
        safe_text,
    interface=
        safe_text,
    redefinedOperation=
        safe_text,
    postcondition=
        safe_text,
    isOrdered=
        safe_text,
    isQuery=
        safe_text,
    lower=
        safe_text
)
UMLModel::StringExpression_strategy = st.builds(
    UMLModel::StringExpression,
    owningExpression=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
UMLModel::Reception_strategy = st.builds(
    UMLModel::Reception,
    signal=
        safe_text
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
UMLModel::Class_strategy = st.builds(
    UMLModel::Class,
    isActive=
        safe_text,
    superclass=
        safe_text,
    extension=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
UMLModel::ExecutionEvent_strategy = st.builds(
    UMLModel::ExecutionEvent,
)
UMLModel::DestructionEvent_strategy = st.builds(
    UMLModel::DestructionEvent,
)
UMLModel::MessageEvent_strategy = st.builds(
    UMLModel::MessageEvent,
)
UMLModel::TimeEvent_strategy = st.builds(
    UMLModel::TimeEvent,
    isRelative=
        safe_text
)
UMLModel::CreationEvent_strategy = st.builds(
    UMLModel::CreationEvent,
)
UMLModel::ChangeEvent_strategy = st.builds(
    UMLModel::ChangeEvent,
)
UMLModel::CallOperationAction_strategy = st.builds(
    UMLModel::CallOperationAction,
    operation=
        safe_text
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
UMLModel::ConnectableElementTemplateParameter_strategy = st.builds(
    UMLModel::ConnectableElementTemplateParameter,
)
UMLModel::OperationTemplateParameter_strategy = st.builds(
    UMLModel::OperationTemplateParameter,
)
UMLModel::ClassifierTemplateParameter_strategy = st.builds(
    UMLModel::ClassifierTemplateParameter,
    allowSubstitutable=
        safe_text,
    defaultClassifier=
        safe_text,
    constrainingClassifier=
        safe_text
)
UMLModel::UseCase_strategy = st.builds(
    UMLModel::UseCase,
    subject=
        safe_text
)
UMLModel::CollaborationUse_strategy = st.builds(
    UMLModel::CollaborationUse,
    type=
        safe_text
)
UMLModel::Substitution_strategy = st.builds(
    UMLModel::Substitution,
    contract=
        safe_text,
    substitutingClassifier=
        safe_text
)
UMLModel::InterfaceRealization_strategy = st.builds(
    UMLModel::InterfaceRealization,
    realizingClassifier=
        safe_text,
    contract=
        safe_text
)
UMLModel::BehavioredClassifier_strategy = st.builds(
    UMLModel::BehavioredClassifier,
    classifierBehavior=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
UMLModel::Connector_strategy = st.builds(
    UMLModel::Connector,
    kind=
        safe_text,
    type=
        safe_text,
    redefinedConnector=
        safe_text,
    contract=
        safe_text
)
UMLModel::StructuralFeature_strategy = st.builds(
    UMLModel::StructuralFeature,
    isReadOnly=
        safe_text
)
Namespace_strategy = st.builds(
    Namespace,
)
UMLModel::InteractionOperand_strategy = st.builds(
    UMLModel::InteractionOperand,
)
UMLModel::Transition_strategy = st.builds(
    UMLModel::Transition,
    redefinedTransition=
        safe_text,
    guard=
        safe_text,
    source=
        safe_text,
    container=
        safe_text,
    kind=
        safe_text,
    target=
        safe_text
)
UMLModel::Classifier_strategy = st.builds(
    UMLModel::Classifier,
    redefinedClassifier=
        safe_text,
    general=
        safe_text,
    feature=
        safe_text,
    isAbstract=
        safe_text,
    inheritedMember=
        safe_text,
    representation=
        safe_text,
    useCase=
        safe_text,
    attribute=
        safe_text,
    powertypeExtent=
        safe_text
)
UMLModel::Package_strategy = st.builds(
    UMLModel::Package,
    nestedPackage=
        safe_text,
    nestingPackage=
        safe_text,
    ownedType=
        safe_text
)
UMLModel::StructuredActivityNode_strategy = st.builds(
    UMLModel::StructuredActivityNode,
    mustIsolate=
        safe_text
)
UMLModel::Region_strategy = st.builds(
    UMLModel::Region,
    extendedRegion=
        safe_text,
    state=
        safe_text,
    stateMachine=
        safe_text
)
UMLModel::State_strategy = st.builds(
    UMLModel::State,
    redefinedState=
        safe_text,
    isOrthogonal=
        safe_text,
    submachine=
        safe_text,
    isSimple=
        safe_text,
    isComposite=
        safe_text,
    isSubmachineState=
        safe_text
)
UMLModel::BehavioralFeature_strategy = st.builds(
    UMLModel::BehavioralFeature,
    isAbstract=
        safe_text,
    concurrency=
        safe_text,
    method=
        safe_text,
    raisedException=
        safe_text
)
UMLModel::BehaviorExecutionSpecification_strategy = st.builds(
    UMLModel::BehaviorExecutionSpecification,
    behavior=
        safe_text
)
UMLModel::ParameterSet_strategy = st.builds(
    UMLModel::ParameterSet,
    parameter=
        safe_text
)
UMLModel::Parameter_strategy = st.builds(
    UMLModel::Parameter,
    isException=
        safe_text,
    default=
        safe_text,
    effect=
        safe_text,
    isStream=
        safe_text,
    parameterSet=
        safe_text,
    direction=
        safe_text,
    operation=
        safe_text
)
UMLModel::CallEvent_strategy = st.builds(
    UMLModel::CallEvent,
    operation=
        safe_text
)
UMLModel::Behavior_strategy = st.builds(
    UMLModel::Behavior,
    postcondition=
        safe_text,
    specification=
        safe_text,
    context=
        safe_text,
    isReentrant=
        safe_text,
    precondition=
        safe_text,
    redefinedBahavior=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=TemplateSignature_strategy)
@settings(max_examples=50)
def test_templatesignature_instantiation(instance):
    assert isinstance(instance, TemplateSignature)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UMLModel::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readlinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadLinkAction)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=UMLModel::ProtocolTransition_strategy)
@settings(max_examples=50)
def test_umlmodel::protocoltransition_instantiation(instance):
    assert isinstance(instance, UMLModel::ProtocolTransition)

@given(instance=UMLModel::ProtocolTransition_strategy)
def test_umlmodel::protocoltransition_preCondition_type(instance):
    assert isinstance(instance.preCondition, str)


@given(instance=UMLModel::ProtocolTransition_strategy)
def test_umlmodel::protocoltransition_preCondition_setter(instance):
    original = instance.preCondition
    instance.preCondition = original
    assert instance.preCondition == original

@given(instance=UMLModel::ProtocolTransition_strategy)
def test_umlmodel::protocoltransition_referred_type(instance):
    assert isinstance(instance.referred, str)


@given(instance=UMLModel::ProtocolTransition_strategy)
def test_umlmodel::protocoltransition_referred_setter(instance):
    original = instance.referred
    instance.referred = original
    assert instance.referred == original

@given(instance=UMLModel::ProtocolTransition_strategy)
def test_umlmodel::protocoltransition_postCondition_type(instance):
    assert isinstance(instance.postCondition, str)


@given(instance=UMLModel::ProtocolTransition_strategy)
def test_umlmodel::protocoltransition_postCondition_setter(instance):
    original = instance.postCondition
    instance.postCondition = original
    assert instance.postCondition == original

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=InteractionUse_strategy)
@settings(max_examples=50)
def test_interactionuse_instantiation(instance):
    assert isinstance(instance, InteractionUse)

@given(instance=UMLModel::PartDecomposition_strategy)
@settings(max_examples=50)
def test_umlmodel::partdecomposition_instantiation(instance):
    assert isinstance(instance, UMLModel::PartDecomposition)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=UMLModel::Profile_strategy)
@settings(max_examples=50)
def test_umlmodel::profile_instantiation(instance):
    assert isinstance(instance, UMLModel::Profile)

@given(instance=UMLModel::Profile_strategy)
def test_umlmodel::profile_metaclassReference_type(instance):
    assert isinstance(instance.metaclassReference, str)


@given(instance=UMLModel::Profile_strategy)
def test_umlmodel::profile_metaclassReference_setter(instance):
    original = instance.metaclassReference
    instance.metaclassReference = original
    assert instance.metaclassReference == original

@given(instance=UMLModel::Profile_strategy)
def test_umlmodel::profile_metamodelReference_type(instance):
    assert isinstance(instance.metamodelReference, str)


@given(instance=UMLModel::Profile_strategy)
def test_umlmodel::profile_metamodelReference_setter(instance):
    original = instance.metamodelReference
    instance.metamodelReference = original
    assert instance.metamodelReference == original

@given(instance=UMLModel::Profile_strategy)
def test_umlmodel::profile_ownedStereotype_type(instance):
    assert isinstance(instance.ownedStereotype, str)


@given(instance=UMLModel::Profile_strategy)
def test_umlmodel::profile_ownedStereotype_setter(instance):
    original = instance.ownedStereotype
    instance.ownedStereotype = original
    assert instance.ownedStereotype == original

@given(instance=UMLModel::Model_strategy)
@settings(max_examples=50)
def test_umlmodel::model_instantiation(instance):
    assert isinstance(instance, UMLModel::Model)

@given(instance=UMLModel::Model_strategy)
def test_umlmodel::model_viewpoint_type(instance):
    assert isinstance(instance.viewpoint, str)


@given(instance=UMLModel::Model_strategy)
def test_umlmodel::model_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=UMLModel::Realization_strategy)
@settings(max_examples=50)
def test_umlmodel::realization_instantiation(instance):
    assert isinstance(instance, UMLModel::Realization)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=UMLModel::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_umlmodel::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, UMLModel::LinkEndDestructionData)

@given(instance=UMLModel::LinkEndDestructionData_strategy)
def test_umlmodel::linkenddestructiondata_isDestroyDuplicates_type(instance):
    assert isinstance(instance.isDestroyDuplicates, str)


@given(instance=UMLModel::LinkEndDestructionData_strategy)
def test_umlmodel::linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=UMLModel::LinkEndDestructionData_strategy)
def test_umlmodel::linkenddestructiondata_destroyAt_type(instance):
    assert isinstance(instance.destroyAt, str)


@given(instance=UMLModel::LinkEndDestructionData_strategy)
def test_umlmodel::linkenddestructiondata_destroyAt_setter(instance):
    original = instance.destroyAt
    instance.destroyAt = original
    assert instance.destroyAt == original

@given(instance=UMLModel::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_umlmodel::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, UMLModel::LinkEndCreationData)

@given(instance=UMLModel::LinkEndCreationData_strategy)
def test_umlmodel::linkendcreationdata_insertAt_type(instance):
    assert isinstance(instance.insertAt, str)


@given(instance=UMLModel::LinkEndCreationData_strategy)
def test_umlmodel::linkendcreationdata_insertAt_setter(instance):
    original = instance.insertAt
    instance.insertAt = original
    assert instance.insertAt == original

@given(instance=UMLModel::LinkEndCreationData_strategy)
def test_umlmodel::linkendcreationdata_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=UMLModel::LinkEndCreationData_strategy)
def test_umlmodel::linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UMLModel::LiteralString_strategy)
@settings(max_examples=50)
def test_umlmodel::literalstring_instantiation(instance):
    assert isinstance(instance, UMLModel::LiteralString)

@given(instance=UMLModel::LiteralString_strategy)
def test_umlmodel::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UMLModel::LiteralString_strategy)
def test_umlmodel::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_umlmodel::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UMLModel::LiteralUnlimitedNatural)

@given(instance=UMLModel::LiteralUnlimitedNatural_strategy)
def test_umlmodel::literalunlimitednatural_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UMLModel::LiteralUnlimitedNatural_strategy)
def test_umlmodel::literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_umlmodel::literalboolean_instantiation(instance):
    assert isinstance(instance, UMLModel::LiteralBoolean)

@given(instance=UMLModel::LiteralBoolean_strategy)
def test_umlmodel::literalboolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UMLModel::LiteralBoolean_strategy)
def test_umlmodel::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel::LiteralNull_strategy)
@settings(max_examples=50)
def test_umlmodel::literalnull_instantiation(instance):
    assert isinstance(instance, UMLModel::LiteralNull)

@given(instance=UMLModel::LiteralInteger_strategy)
@settings(max_examples=50)
def test_umlmodel::literalinteger_instantiation(instance):
    assert isinstance(instance, UMLModel::LiteralInteger)

@given(instance=UMLModel::LiteralInteger_strategy)
def test_umlmodel::literalinteger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UMLModel::LiteralInteger_strategy)
def test_umlmodel::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UMLModel::IntervalConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel::intervalconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel::IntervalConstraint)

@given(instance=UMLModel::InteractionConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel::interactionconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel::InteractionConstraint)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=UMLModel::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_umlmodel::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UMLModel::ProtocolStateMachine)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=UMLModel::FunctionBehavior_strategy)
@settings(max_examples=50)
def test_umlmodel::functionbehavior_instantiation(instance):
    assert isinstance(instance, UMLModel::FunctionBehavior)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UMLModel::FinalState_strategy)
@settings(max_examples=50)
def test_umlmodel::finalstate_instantiation(instance):
    assert isinstance(instance, UMLModel::FinalState)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UMLModel::Port_strategy)
@settings(max_examples=50)
def test_umlmodel::port_instantiation(instance):
    assert isinstance(instance, UMLModel::Port)

@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_isService_type(instance):
    assert isinstance(instance.isService, str)


@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original

@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_provided_type(instance):
    assert isinstance(instance.provided, str)


@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_provided_setter(instance):
    original = instance.provided
    instance.provided = original
    assert instance.provided == original

@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_protocol_type(instance):
    assert isinstance(instance.protocol, str)


@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_required_type(instance):
    assert isinstance(instance.required, str)


@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_redefinedPort_type(instance):
    assert isinstance(instance.redefinedPort, str)


@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_redefinedPort_setter(instance):
    original = instance.redefinedPort
    instance.redefinedPort = original
    assert instance.redefinedPort == original

@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_isBehavior_type(instance):
    assert isinstance(instance.isBehavior, str)


@given(instance=UMLModel::Port_strategy)
def test_umlmodel::port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original

@given(instance=UMLModel::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_umlmodel::extensionend_instantiation(instance):
    assert isinstance(instance, UMLModel::ExtensionEnd)

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=UMLModel::MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, UMLModel::MessageOccurrenceSpecification)

@given(instance=UMLModel::ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, UMLModel::ExecutionOccurrenceSpecification)

@given(instance=UMLModel::ExecutionOccurrenceSpecification_strategy)
def test_umlmodel::executionoccurrencespecification_execution_type(instance):
    assert isinstance(instance.execution, str)


@given(instance=UMLModel::ExecutionOccurrenceSpecification_strategy)
def test_umlmodel::executionoccurrencespecification_execution_setter(instance):
    original = instance.execution
    instance.execution = original
    assert instance.execution == original

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=UMLModel::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel::writelinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel::WriteLinkAction)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=UMLModel::UMLBase_strategy)
@settings(max_examples=50)
def test_umlmodel::umlbase_instantiation(instance):
    assert isinstance(instance, UMLModel::UMLBase)

@given(instance=UMLModel::UMLBase_strategy)
def test_umlmodel::umlbase_umlID_type(instance):
    assert isinstance(instance.umlID, str)


@given(instance=UMLModel::UMLBase_strategy)
def test_umlmodel::umlbase_umlID_setter(instance):
    original = instance.umlID
    instance.umlID = original
    assert instance.umlID == original

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=UMLModel::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_umlmodel::callbehavioraction_instantiation(instance):
    assert isinstance(instance, UMLModel::CallBehaviorAction)

@given(instance=UMLModel::CallBehaviorAction_strategy)
def test_umlmodel::callbehavioraction_behavior_type(instance):
    assert isinstance(instance.behavior, str)


@given(instance=UMLModel::CallBehaviorAction_strategy)
def test_umlmodel::callbehavioraction_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=UMLModel::CallAction_strategy)
@settings(max_examples=50)
def test_umlmodel::callaction_instantiation(instance):
    assert isinstance(instance, UMLModel::CallAction)

@given(instance=UMLModel::CallAction_strategy)
def test_umlmodel::callaction_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, str)


@given(instance=UMLModel::CallAction_strategy)
def test_umlmodel::callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=UMLModel::SendObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel::sendobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel::SendObjectAction)

@given(instance=UMLModel::SendSignalAction_strategy)
@settings(max_examples=50)
def test_umlmodel::sendsignalaction_instantiation(instance):
    assert isinstance(instance, UMLModel::SendSignalAction)

@given(instance=UMLModel::SendSignalAction_strategy)
def test_umlmodel::sendsignalaction_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=UMLModel::SendSignalAction_strategy)
def test_umlmodel::sendsignalaction_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel::BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_umlmodel::broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UMLModel::BroadcastSignalAction)

@given(instance=UMLModel::BroadcastSignalAction_strategy)
def test_umlmodel::broadcastsignalaction_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=UMLModel::BroadcastSignalAction_strategy)
def test_umlmodel::broadcastsignalaction_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel::Manifestation_strategy)
@settings(max_examples=50)
def test_umlmodel::manifestation_instantiation(instance):
    assert isinstance(instance, UMLModel::Manifestation)

@given(instance=UMLModel::Manifestation_strategy)
def test_umlmodel::manifestation_utilizedElement_type(instance):
    assert isinstance(instance.utilizedElement, str)


@given(instance=UMLModel::Manifestation_strategy)
def test_umlmodel::manifestation_utilizedElement_setter(instance):
    original = instance.utilizedElement
    instance.utilizedElement = original
    assert instance.utilizedElement == original

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UMLModel::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_umlmodel::structuredclassifier_instantiation(instance):
    assert isinstance(instance, UMLModel::StructuredClassifier)

@given(instance=UMLModel::StructuredClassifier_strategy)
def test_umlmodel::structuredclassifier_part_type(instance):
    assert isinstance(instance.part, str)


@given(instance=UMLModel::StructuredClassifier_strategy)
def test_umlmodel::structuredclassifier_part_setter(instance):
    original = instance.part
    instance.part = original
    assert instance.part == original

@given(instance=UMLModel::StructuredClassifier_strategy)
def test_umlmodel::structuredclassifier_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=UMLModel::StructuredClassifier_strategy)
def test_umlmodel::structuredclassifier_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=UMLModel::InformationItem_strategy)
@settings(max_examples=50)
def test_umlmodel::informationitem_instantiation(instance):
    assert isinstance(instance, UMLModel::InformationItem)

@given(instance=UMLModel::InformationItem_strategy)
def test_umlmodel::informationitem_represented_type(instance):
    assert isinstance(instance.represented, str)


@given(instance=UMLModel::InformationItem_strategy)
def test_umlmodel::informationitem_represented_setter(instance):
    original = instance.represented
    instance.represented = original
    assert instance.represented == original

@given(instance=UMLModel::Signal_strategy)
@settings(max_examples=50)
def test_umlmodel::signal_instantiation(instance):
    assert isinstance(instance, UMLModel::Signal)

@given(instance=UMLModel::Interface_strategy)
@settings(max_examples=50)
def test_umlmodel::interface_instantiation(instance):
    assert isinstance(instance, UMLModel::Interface)

@given(instance=UMLModel::Interface_strategy)
def test_umlmodel::interface_redefinedInterface_type(instance):
    assert isinstance(instance.redefinedInterface, str)


@given(instance=UMLModel::Interface_strategy)
def test_umlmodel::interface_redefinedInterface_setter(instance):
    original = instance.redefinedInterface
    instance.redefinedInterface = original
    assert instance.redefinedInterface == original

@given(instance=UMLModel::Interface_strategy)
def test_umlmodel::interface_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=UMLModel::Interface_strategy)
def test_umlmodel::interface_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=UMLModel::Artifact_strategy)
@settings(max_examples=50)
def test_umlmodel::artifact_instantiation(instance):
    assert isinstance(instance, UMLModel::Artifact)

@given(instance=UMLModel::Artifact_strategy)
def test_umlmodel::artifact_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=UMLModel::Artifact_strategy)
def test_umlmodel::artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=UMLModel::SignalEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::signalevent_instantiation(instance):
    assert isinstance(instance, UMLModel::SignalEvent)

@given(instance=UMLModel::SignalEvent_strategy)
def test_umlmodel::signalevent_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=UMLModel::SignalEvent_strategy)
def test_umlmodel::signalevent_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel::ReceiveOperationEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::receiveoperationevent_instantiation(instance):
    assert isinstance(instance, UMLModel::ReceiveOperationEvent)

@given(instance=UMLModel::ReceiveOperationEvent_strategy)
def test_umlmodel::receiveoperationevent_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=UMLModel::ReceiveOperationEvent_strategy)
def test_umlmodel::receiveoperationevent_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=UMLModel::SendSignalEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::sendsignalevent_instantiation(instance):
    assert isinstance(instance, UMLModel::SendSignalEvent)

@given(instance=UMLModel::SendSignalEvent_strategy)
def test_umlmodel::sendsignalevent_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=UMLModel::SendSignalEvent_strategy)
def test_umlmodel::sendsignalevent_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel::ReceiveSignalEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::receivesignalevent_instantiation(instance):
    assert isinstance(instance, UMLModel::ReceiveSignalEvent)

@given(instance=UMLModel::ReceiveSignalEvent_strategy)
def test_umlmodel::receivesignalevent_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=UMLModel::ReceiveSignalEvent_strategy)
def test_umlmodel::receivesignalevent_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel::AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::anyreceiveevent_instantiation(instance):
    assert isinstance(instance, UMLModel::AnyReceiveEvent)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UMLModel::RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel::removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel::RemoveVariableValueAction)

@given(instance=UMLModel::RemoveVariableValueAction_strategy)
def test_umlmodel::removevariablevalueaction_isRemoveDuplicates_type(instance):
    assert isinstance(instance.isRemoveDuplicates, str)


@given(instance=UMLModel::RemoveVariableValueAction_strategy)
def test_umlmodel::removevariablevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=UMLModel::AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel::addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel::AddVariableValueAction)

@given(instance=UMLModel::AddVariableValueAction_strategy)
def test_umlmodel::addvariablevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=UMLModel::AddVariableValueAction_strategy)
def test_umlmodel::addvariablevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=UMLModel::InputPin_strategy)
@settings(max_examples=50)
def test_umlmodel::inputpin_instantiation(instance):
    assert isinstance(instance, UMLModel::InputPin)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UMLModel::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel::RemoveStructuralFeatureValueAction)

@given(instance=UMLModel::RemoveStructuralFeatureValueAction_strategy)
def test_umlmodel::removestructuralfeaturevalueaction_isRemoveDuplicates_type(instance):
    assert isinstance(instance.isRemoveDuplicates, str)


@given(instance=UMLModel::RemoveStructuralFeatureValueAction_strategy)
def test_umlmodel::removestructuralfeaturevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=UMLModel::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel::AddStructuralFeatureValueAction)

@given(instance=UMLModel::AddStructuralFeatureValueAction_strategy)
def test_umlmodel::addstructuralfeaturevalueaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=UMLModel::AddStructuralFeatureValueAction_strategy)
def test_umlmodel::addstructuralfeaturevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UMLModel::Actor_strategy)
@settings(max_examples=50)
def test_umlmodel::actor_instantiation(instance):
    assert isinstance(instance, UMLModel::Actor)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UMLModel::Extension_strategy)
@settings(max_examples=50)
def test_umlmodel::extension_instantiation(instance):
    assert isinstance(instance, UMLModel::Extension)

@given(instance=UMLModel::Extension_strategy)
def test_umlmodel::extension_metaClass_type(instance):
    assert isinstance(instance.metaClass, str)


@given(instance=UMLModel::Extension_strategy)
def test_umlmodel::extension_metaClass_setter(instance):
    original = instance.metaClass
    instance.metaClass = original
    assert instance.metaClass == original

@given(instance=UMLModel::Extension_strategy)
def test_umlmodel::extension_isRequired_type(instance):
    assert isinstance(instance.isRequired, str)


@given(instance=UMLModel::Extension_strategy)
def test_umlmodel::extension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UMLModel::Stereotype_strategy)
@settings(max_examples=50)
def test_umlmodel::stereotype_instantiation(instance):
    assert isinstance(instance, UMLModel::Stereotype)

@given(instance=UMLModel::Node_strategy)
@settings(max_examples=50)
def test_umlmodel::node_instantiation(instance):
    assert isinstance(instance, UMLModel::Node)

@given(instance=UMLModel::AssociationClass_strategy)
@settings(max_examples=50)
def test_umlmodel::associationclass_instantiation(instance):
    assert isinstance(instance, UMLModel::AssociationClass)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=UMLModel::Association_strategy)
@settings(max_examples=50)
def test_umlmodel::association_instantiation(instance):
    assert isinstance(instance, UMLModel::Association)

@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_navigableOwnedEnd_type(instance):
    assert isinstance(instance.navigableOwnedEnd, str)


@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_navigableOwnedEnd_setter(instance):
    original = instance.navigableOwnedEnd
    instance.navigableOwnedEnd = original
    assert instance.navigableOwnedEnd == original

@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_memberEnd_type(instance):
    assert isinstance(instance.memberEnd, str)


@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_memberEnd_setter(instance):
    original = instance.memberEnd
    instance.memberEnd = original
    assert instance.memberEnd == original

@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_endType_type(instance):
    assert isinstance(instance.endType, str)


@given(instance=UMLModel::Association_strategy)
def test_umlmodel::association_endType_setter(instance):
    original = instance.endType
    instance.endType = original
    assert instance.endType == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UMLModel::ParameterableElement_strategy)
@settings(max_examples=50)
def test_umlmodel::parameterableelement_instantiation(instance):
    assert isinstance(instance, UMLModel::ParameterableElement)

@given(instance=UMLModel::ParameterableElement_strategy)
def test_umlmodel::parameterableelement_templateParameter_type(instance):
    assert isinstance(instance.templateParameter, str)


@given(instance=UMLModel::ParameterableElement_strategy)
def test_umlmodel::parameterableelement_templateParameter_setter(instance):
    original = instance.templateParameter
    instance.templateParameter = original
    assert instance.templateParameter == original

@given(instance=UMLModel::ParameterableElement_strategy)
def test_umlmodel::parameterableelement_owningTemplateParameter_type(instance):
    assert isinstance(instance.owningTemplateParameter, str)


@given(instance=UMLModel::ParameterableElement_strategy)
def test_umlmodel::parameterableelement_owningTemplateParameter_setter(instance):
    original = instance.owningTemplateParameter
    instance.owningTemplateParameter = original
    assert instance.owningTemplateParameter == original

@given(instance=UMLModel::Relationship_strategy)
@settings(max_examples=50)
def test_umlmodel::relationship_instantiation(instance):
    assert isinstance(instance, UMLModel::Relationship)

@given(instance=UMLModel::Relationship_strategy)
def test_umlmodel::relationship_relatedElement_type(instance):
    assert isinstance(instance.relatedElement, str)


@given(instance=UMLModel::Relationship_strategy)
def test_umlmodel::relationship_relatedElement_setter(instance):
    original = instance.relatedElement
    instance.relatedElement = original
    assert instance.relatedElement == original

@given(instance=UMLModel::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_umlmodel::multiplicityelement_instantiation(instance):
    assert isinstance(instance, UMLModel::MultiplicityElement)

@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=UMLModel::MultiplicityElement_strategy)
def test_umlmodel::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=UMLModel::LinkEndData_strategy)
@settings(max_examples=50)
def test_umlmodel::linkenddata_instantiation(instance):
    assert isinstance(instance, UMLModel::LinkEndData)

@given(instance=UMLModel::LinkEndData_strategy)
def test_umlmodel::linkenddata_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=UMLModel::LinkEndData_strategy)
def test_umlmodel::linkenddata_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=UMLModel::LinkEndData_strategy)
def test_umlmodel::linkenddata_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UMLModel::LinkEndData_strategy)
def test_umlmodel::linkenddata_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel::Image_strategy)
@settings(max_examples=50)
def test_umlmodel::image_instantiation(instance):
    assert isinstance(instance, UMLModel::Image)

@given(instance=UMLModel::Image_strategy)
def test_umlmodel::image_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=UMLModel::Image_strategy)
def test_umlmodel::image_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=UMLModel::Image_strategy)
def test_umlmodel::image_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=UMLModel::Image_strategy)
def test_umlmodel::image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=UMLModel::Image_strategy)
def test_umlmodel::image_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=UMLModel::Image_strategy)
def test_umlmodel::image_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=UMLModel::Slot_strategy)
@settings(max_examples=50)
def test_umlmodel::slot_instantiation(instance):
    assert isinstance(instance, UMLModel::Slot)

@given(instance=UMLModel::Slot_strategy)
def test_umlmodel::slot_definingFeature_type(instance):
    assert isinstance(instance.definingFeature, str)


@given(instance=UMLModel::Slot_strategy)
def test_umlmodel::slot_definingFeature_setter(instance):
    original = instance.definingFeature
    instance.definingFeature = original
    assert instance.definingFeature == original

@given(instance=UMLModel::Slot_strategy)
def test_umlmodel::slot_owningInstance_type(instance):
    assert isinstance(instance.owningInstance, str)


@given(instance=UMLModel::Slot_strategy)
def test_umlmodel::slot_owningInstance_setter(instance):
    original = instance.owningInstance
    instance.owningInstance = original
    assert instance.owningInstance == original

@given(instance=UMLModel::TemplateSignature_strategy)
@settings(max_examples=50)
def test_umlmodel::templatesignature_instantiation(instance):
    assert isinstance(instance, UMLModel::TemplateSignature)

@given(instance=UMLModel::TemplateSignature_strategy)
def test_umlmodel::templatesignature_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=UMLModel::TemplateSignature_strategy)
def test_umlmodel::templatesignature_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=UMLModel::TemplateSignature_strategy)
def test_umlmodel::templatesignature_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=UMLModel::TemplateSignature_strategy)
def test_umlmodel::templatesignature_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=UMLModel::NamedElement_strategy)
@settings(max_examples=50)
def test_umlmodel::namedelement_instantiation(instance):
    assert isinstance(instance, UMLModel::NamedElement)

@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_clientDependency_type(instance):
    assert isinstance(instance.clientDependency, str)


@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_clientDependency_setter(instance):
    original = instance.clientDependency
    instance.clientDependency = original
    assert instance.clientDependency == original

@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UMLModel::NamedElement_strategy)
def test_umlmodel::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UMLModel::TemplateableElement_strategy)
@settings(max_examples=50)
def test_umlmodel::templateableelement_instantiation(instance):
    assert isinstance(instance, UMLModel::TemplateableElement)

@given(instance=UMLModel::TemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel::templateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel::TemplateParameter)

@given(instance=UMLModel::TemplateParameter_strategy)
def test_umlmodel::templateparameter_parameteredElement_type(instance):
    assert isinstance(instance.parameteredElement, str)


@given(instance=UMLModel::TemplateParameter_strategy)
def test_umlmodel::templateparameter_parameteredElement_setter(instance):
    original = instance.parameteredElement
    instance.parameteredElement = original
    assert instance.parameteredElement == original

@given(instance=UMLModel::TemplateParameter_strategy)
def test_umlmodel::templateparameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=UMLModel::TemplateParameter_strategy)
def test_umlmodel::templateparameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=UMLModel::TemplateParameter_strategy)
def test_umlmodel::templateparameter_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=UMLModel::TemplateParameter_strategy)
def test_umlmodel::templateparameter_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=UMLModel::QualifierValue_strategy)
@settings(max_examples=50)
def test_umlmodel::qualifiervalue_instantiation(instance):
    assert isinstance(instance, UMLModel::QualifierValue)

@given(instance=UMLModel::QualifierValue_strategy)
def test_umlmodel::qualifiervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=UMLModel::QualifierValue_strategy)
def test_umlmodel::qualifiervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel::QualifierValue_strategy)
def test_umlmodel::qualifiervalue_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=UMLModel::QualifierValue_strategy)
def test_umlmodel::qualifiervalue_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=UMLModel::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_umlmodel::exceptionhandler_instantiation(instance):
    assert isinstance(instance, UMLModel::ExceptionHandler)

@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_exceptionInput_type(instance):
    assert isinstance(instance.exceptionInput, str)


@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_exceptionInput_setter(instance):
    original = instance.exceptionInput
    instance.exceptionInput = original
    assert instance.exceptionInput == original

@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_handlerBody_type(instance):
    assert isinstance(instance.handlerBody, str)


@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_handlerBody_setter(instance):
    original = instance.handlerBody
    instance.handlerBody = original
    assert instance.handlerBody == original

@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_exceptionType_type(instance):
    assert isinstance(instance.exceptionType, str)


@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_exceptionType_setter(instance):
    original = instance.exceptionType
    instance.exceptionType = original
    assert instance.exceptionType == original

@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_protectedNode_type(instance):
    assert isinstance(instance.protectedNode, str)


@given(instance=UMLModel::ExceptionHandler_strategy)
def test_umlmodel::exceptionhandler_protectedNode_setter(instance):
    original = instance.protectedNode
    instance.protectedNode = original
    assert instance.protectedNode == original

@given(instance=UMLModel::TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_umlmodel::templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, UMLModel::TemplateParameterSubstitution)

@given(instance=UMLModel::TemplateParameterSubstitution_strategy)
def test_umlmodel::templateparametersubstitution_formal_type(instance):
    assert isinstance(instance.formal, str)


@given(instance=UMLModel::TemplateParameterSubstitution_strategy)
def test_umlmodel::templateparametersubstitution_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=UMLModel::TemplateParameterSubstitution_strategy)
def test_umlmodel::templateparametersubstitution_actual_type(instance):
    assert isinstance(instance.actual, str)


@given(instance=UMLModel::TemplateParameterSubstitution_strategy)
def test_umlmodel::templateparametersubstitution_actual_setter(instance):
    original = instance.actual
    instance.actual = original
    assert instance.actual == original

@given(instance=UMLModel::TemplateParameterSubstitution_strategy)
def test_umlmodel::templateparametersubstitution_templateBinding_type(instance):
    assert isinstance(instance.templateBinding, str)


@given(instance=UMLModel::TemplateParameterSubstitution_strategy)
def test_umlmodel::templateparametersubstitution_templateBinding_setter(instance):
    original = instance.templateBinding
    instance.templateBinding = original
    assert instance.templateBinding == original

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=UMLModel::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_umlmodel::flowfinalnode_instantiation(instance):
    assert isinstance(instance, UMLModel::FlowFinalNode)

@given(instance=UMLModel::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_umlmodel::activityfinalnode_instantiation(instance):
    assert isinstance(instance, UMLModel::ActivityFinalNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UMLModel::ExpansionNode_strategy)
@settings(max_examples=50)
def test_umlmodel::expansionnode_instantiation(instance):
    assert isinstance(instance, UMLModel::ExpansionNode)

@given(instance=UMLModel::ExpansionNode_strategy)
def test_umlmodel::expansionnode_regionAsOutput_type(instance):
    assert isinstance(instance.regionAsOutput, str)


@given(instance=UMLModel::ExpansionNode_strategy)
def test_umlmodel::expansionnode_regionAsOutput_setter(instance):
    original = instance.regionAsOutput
    instance.regionAsOutput = original
    assert instance.regionAsOutput == original

@given(instance=UMLModel::ExpansionNode_strategy)
def test_umlmodel::expansionnode_regionAsInput_type(instance):
    assert isinstance(instance.regionAsInput, str)


@given(instance=UMLModel::ExpansionNode_strategy)
def test_umlmodel::expansionnode_regionAsInput_setter(instance):
    original = instance.regionAsInput
    instance.regionAsInput = original
    assert instance.regionAsInput == original

@given(instance=UMLModel::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_umlmodel::activityparameternode_instantiation(instance):
    assert isinstance(instance, UMLModel::ActivityParameterNode)

@given(instance=UMLModel::ActivityParameterNode_strategy)
def test_umlmodel::activityparameternode_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=UMLModel::ActivityParameterNode_strategy)
def test_umlmodel::activityparameternode_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=UMLModel::Feature_strategy)
@settings(max_examples=50)
def test_umlmodel::feature_instantiation(instance):
    assert isinstance(instance, UMLModel::Feature)

@given(instance=UMLModel::Feature_strategy)
def test_umlmodel::feature_featuringClassifier_type(instance):
    assert isinstance(instance.featuringClassifier, str)


@given(instance=UMLModel::Feature_strategy)
def test_umlmodel::feature_featuringClassifier_setter(instance):
    original = instance.featuringClassifier
    instance.featuringClassifier = original
    assert instance.featuringClassifier == original

@given(instance=UMLModel::Feature_strategy)
def test_umlmodel::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=UMLModel::Feature_strategy)
def test_umlmodel::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=UMLModel::RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_umlmodel::redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, UMLModel::RedefinableTemplateSignature)

@given(instance=UMLModel::RedefinableTemplateSignature_strategy)
def test_umlmodel::redefinabletemplatesignature_extendedSignature_type(instance):
    assert isinstance(instance.extendedSignature, str)


@given(instance=UMLModel::RedefinableTemplateSignature_strategy)
def test_umlmodel::redefinabletemplatesignature_extendedSignature_setter(instance):
    original = instance.extendedSignature
    instance.extendedSignature = original
    assert instance.extendedSignature == original

@given(instance=UMLModel::RedefinableTemplateSignature_strategy)
def test_umlmodel::redefinabletemplatesignature_classifier_type(instance):
    assert isinstance(instance.classifier, str)


@given(instance=UMLModel::RedefinableTemplateSignature_strategy)
def test_umlmodel::redefinabletemplatesignature_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=UMLModel::RedefinableTemplateSignature_strategy)
def test_umlmodel::redefinabletemplatesignature_inheritedParameter_type(instance):
    assert isinstance(instance.inheritedParameter, str)


@given(instance=UMLModel::RedefinableTemplateSignature_strategy)
def test_umlmodel::redefinabletemplatesignature_inheritedParameter_setter(instance):
    original = instance.inheritedParameter
    instance.inheritedParameter = original
    assert instance.inheritedParameter == original

@given(instance=UMLModel::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_umlmodel::extensionpoint_instantiation(instance):
    assert isinstance(instance, UMLModel::ExtensionPoint)

@given(instance=UMLModel::ExtensionPoint_strategy)
def test_umlmodel::extensionpoint_useCase_type(instance):
    assert isinstance(instance.useCase, str)


@given(instance=UMLModel::ExtensionPoint_strategy)
def test_umlmodel::extensionpoint_useCase_setter(instance):
    original = instance.useCase
    instance.useCase = original
    assert instance.useCase == original

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=UMLModel::InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_umlmodel::interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, UMLModel::InterruptibleActivityRegion)

@given(instance=UMLModel::InterruptibleActivityRegion_strategy)
def test_umlmodel::interruptibleactivityregion_node_type(instance):
    assert isinstance(instance.node, str)


@given(instance=UMLModel::InterruptibleActivityRegion_strategy)
def test_umlmodel::interruptibleactivityregion_node_setter(instance):
    original = instance.node
    instance.node = original
    assert instance.node == original

@given(instance=UMLModel::InterruptibleActivityRegion_strategy)
def test_umlmodel::interruptibleactivityregion_interruptingEdge_type(instance):
    assert isinstance(instance.interruptingEdge, str)


@given(instance=UMLModel::InterruptibleActivityRegion_strategy)
def test_umlmodel::interruptibleactivityregion_interruptingEdge_setter(instance):
    original = instance.interruptingEdge
    instance.interruptingEdge = original
    assert instance.interruptingEdge == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=UMLModel::TypedElement_strategy)
@settings(max_examples=50)
def test_umlmodel::typedelement_instantiation(instance):
    assert isinstance(instance, UMLModel::TypedElement)

@given(instance=UMLModel::TypedElement_strategy)
def test_umlmodel::typedelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=UMLModel::TypedElement_strategy)
def test_umlmodel::typedelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UMLModel::InteractionFragment_strategy)
@settings(max_examples=50)
def test_umlmodel::interactionfragment_instantiation(instance):
    assert isinstance(instance, UMLModel::InteractionFragment)

@given(instance=UMLModel::InteractionFragment_strategy)
def test_umlmodel::interactionfragment_enclosingOperand_type(instance):
    assert isinstance(instance.enclosingOperand, str)


@given(instance=UMLModel::InteractionFragment_strategy)
def test_umlmodel::interactionfragment_enclosingOperand_setter(instance):
    original = instance.enclosingOperand
    instance.enclosingOperand = original
    assert instance.enclosingOperand == original

@given(instance=UMLModel::InteractionFragment_strategy)
def test_umlmodel::interactionfragment_enclosingInteraction_type(instance):
    assert isinstance(instance.enclosingInteraction, str)


@given(instance=UMLModel::InteractionFragment_strategy)
def test_umlmodel::interactionfragment_enclosingInteraction_setter(instance):
    original = instance.enclosingInteraction
    instance.enclosingInteraction = original
    assert instance.enclosingInteraction == original

@given(instance=UMLModel::InteractionFragment_strategy)
def test_umlmodel::interactionfragment_covered_type(instance):
    assert isinstance(instance.covered, str)


@given(instance=UMLModel::InteractionFragment_strategy)
def test_umlmodel::interactionfragment_covered_setter(instance):
    original = instance.covered
    instance.covered = original
    assert instance.covered == original

@given(instance=UMLModel::Vertex_strategy)
@settings(max_examples=50)
def test_umlmodel::vertex_instantiation(instance):
    assert isinstance(instance, UMLModel::Vertex)

@given(instance=UMLModel::Vertex_strategy)
def test_umlmodel::vertex_outgoing_type(instance):
    assert isinstance(instance.outgoing, str)


@given(instance=UMLModel::Vertex_strategy)
def test_umlmodel::vertex_outgoing_setter(instance):
    original = instance.outgoing
    instance.outgoing = original
    assert instance.outgoing == original

@given(instance=UMLModel::Vertex_strategy)
def test_umlmodel::vertex_incoming_type(instance):
    assert isinstance(instance.incoming, str)


@given(instance=UMLModel::Vertex_strategy)
def test_umlmodel::vertex_incoming_setter(instance):
    original = instance.incoming
    instance.incoming = original
    assert instance.incoming == original

@given(instance=UMLModel::Vertex_strategy)
def test_umlmodel::vertex_container_type(instance):
    assert isinstance(instance.container, str)


@given(instance=UMLModel::Vertex_strategy)
def test_umlmodel::vertex_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=UMLModel::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_umlmodel::generalordering_instantiation(instance):
    assert isinstance(instance, UMLModel::GeneralOrdering)

@given(instance=UMLModel::GeneralOrdering_strategy)
def test_umlmodel::generalordering_before_type(instance):
    assert isinstance(instance.before, str)


@given(instance=UMLModel::GeneralOrdering_strategy)
def test_umlmodel::generalordering_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original

@given(instance=UMLModel::GeneralOrdering_strategy)
def test_umlmodel::generalordering_after_type(instance):
    assert isinstance(instance.after, str)


@given(instance=UMLModel::GeneralOrdering_strategy)
def test_umlmodel::generalordering_after_setter(instance):
    original = instance.after
    instance.after = original
    assert instance.after == original

@given(instance=UMLModel::Namespace_strategy)
@settings(max_examples=50)
def test_umlmodel::namespace_instantiation(instance):
    assert isinstance(instance, UMLModel::Namespace)

@given(instance=UMLModel::Namespace_strategy)
def test_umlmodel::namespace_ownedMember_type(instance):
    assert isinstance(instance.ownedMember, str)


@given(instance=UMLModel::Namespace_strategy)
def test_umlmodel::namespace_ownedMember_setter(instance):
    original = instance.ownedMember
    instance.ownedMember = original
    assert instance.ownedMember == original

@given(instance=UMLModel::Namespace_strategy)
def test_umlmodel::namespace_importedMember_type(instance):
    assert isinstance(instance.importedMember, str)


@given(instance=UMLModel::Namespace_strategy)
def test_umlmodel::namespace_importedMember_setter(instance):
    original = instance.importedMember
    instance.importedMember = original
    assert instance.importedMember == original

@given(instance=UMLModel::Namespace_strategy)
def test_umlmodel::namespace_member_type(instance):
    assert isinstance(instance.member, str)


@given(instance=UMLModel::Namespace_strategy)
def test_umlmodel::namespace_member_setter(instance):
    original = instance.member
    instance.member = original
    assert instance.member == original

@given(instance=UMLModel::RedefinableElement_strategy)
@settings(max_examples=50)
def test_umlmodel::redefinableelement_instantiation(instance):
    assert isinstance(instance, UMLModel::RedefinableElement)

@given(instance=UMLModel::RedefinableElement_strategy)
def test_umlmodel::redefinableelement_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, str)


@given(instance=UMLModel::RedefinableElement_strategy)
def test_umlmodel::redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=UMLModel::RedefinableElement_strategy)
def test_umlmodel::redefinableelement_redefinedElement_type(instance):
    assert isinstance(instance.redefinedElement, str)


@given(instance=UMLModel::RedefinableElement_strategy)
def test_umlmodel::redefinableelement_redefinedElement_setter(instance):
    original = instance.redefinedElement
    instance.redefinedElement = original
    assert instance.redefinedElement == original

@given(instance=UMLModel::RedefinableElement_strategy)
def test_umlmodel::redefinableelement_redefinitionContext_type(instance):
    assert isinstance(instance.redefinitionContext, str)


@given(instance=UMLModel::RedefinableElement_strategy)
def test_umlmodel::redefinableelement_redefinitionContext_setter(instance):
    original = instance.redefinitionContext
    instance.redefinitionContext = original
    assert instance.redefinitionContext == original

@given(instance=UMLModel::Lifeline_strategy)
@settings(max_examples=50)
def test_umlmodel::lifeline_instantiation(instance):
    assert isinstance(instance, UMLModel::Lifeline)

@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_interaction_type(instance):
    assert isinstance(instance.interaction, str)


@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_interaction_setter(instance):
    original = instance.interaction
    instance.interaction = original
    assert instance.interaction == original

@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_decomposedAs_type(instance):
    assert isinstance(instance.decomposedAs, str)


@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_decomposedAs_setter(instance):
    original = instance.decomposedAs
    instance.decomposedAs = original
    assert instance.decomposedAs == original

@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_coveredBy_type(instance):
    assert isinstance(instance.coveredBy, str)


@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_coveredBy_setter(instance):
    original = instance.coveredBy
    instance.coveredBy = original
    assert instance.coveredBy == original

@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_represents_type(instance):
    assert isinstance(instance.represents, str)


@given(instance=UMLModel::Lifeline_strategy)
def test_umlmodel::lifeline_represents_setter(instance):
    original = instance.represents
    instance.represents = original
    assert instance.represents == original

@given(instance=UMLModel::MessageEnd_strategy)
@settings(max_examples=50)
def test_umlmodel::messageend_instantiation(instance):
    assert isinstance(instance, UMLModel::MessageEnd)

@given(instance=UMLModel::MessageEnd_strategy)
def test_umlmodel::messageend_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=UMLModel::MessageEnd_strategy)
def test_umlmodel::messageend_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=UMLModel::Message_strategy)
@settings(max_examples=50)
def test_umlmodel::message_instantiation(instance):
    assert isinstance(instance, UMLModel::Message)

@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_sendEvent_type(instance):
    assert isinstance(instance.sendEvent, str)


@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_sendEvent_setter(instance):
    original = instance.sendEvent
    instance.sendEvent = original
    assert instance.sendEvent == original

@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_interaction_type(instance):
    assert isinstance(instance.interaction, str)


@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_interaction_setter(instance):
    original = instance.interaction
    instance.interaction = original
    assert instance.interaction == original

@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_messageKind_type(instance):
    assert isinstance(instance.messageKind, str)


@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original

@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_connector_type(instance):
    assert isinstance(instance.connector, str)


@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_connector_setter(instance):
    original = instance.connector
    instance.connector = original
    assert instance.connector == original

@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_messageSort_type(instance):
    assert isinstance(instance.messageSort, str)


@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original

@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_receiveEvent_type(instance):
    assert isinstance(instance.receiveEvent, str)


@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_receiveEvent_setter(instance):
    original = instance.receiveEvent
    instance.receiveEvent = original
    assert instance.receiveEvent == original

@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=UMLModel::Message_strategy)
def test_umlmodel::message_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=UMLModel::ActivityPartition_strategy)
@settings(max_examples=50)
def test_umlmodel::activitypartition_instantiation(instance):
    assert isinstance(instance, UMLModel::ActivityPartition)

@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_node_type(instance):
    assert isinstance(instance.node, str)


@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_node_setter(instance):
    original = instance.node
    instance.node = original
    assert instance.node == original

@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_isExternal_type(instance):
    assert isinstance(instance.isExternal, str)


@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_isDimension_type(instance):
    assert isinstance(instance.isDimension, str)


@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_superPartition_type(instance):
    assert isinstance(instance.superPartition, str)


@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_superPartition_setter(instance):
    original = instance.superPartition
    instance.superPartition = original
    assert instance.superPartition == original

@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_represents_type(instance):
    assert isinstance(instance.represents, str)


@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_represents_setter(instance):
    original = instance.represents
    instance.represents = original
    assert instance.represents == original

@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_edge_type(instance):
    assert isinstance(instance.edge, str)


@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original

@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_subpartition_type(instance):
    assert isinstance(instance.subpartition, str)


@given(instance=UMLModel::ActivityPartition_strategy)
def test_umlmodel::activitypartition_subpartition_setter(instance):
    original = instance.subpartition
    instance.subpartition = original
    assert instance.subpartition == original

@given(instance=UMLModel::ActivityNode_strategy)
@settings(max_examples=50)
def test_umlmodel::activitynode_instantiation(instance):
    assert isinstance(instance, UMLModel::ActivityNode)

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inStructuredNode_type(instance):
    assert isinstance(instance.inStructuredNode, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inStructuredNode_setter(instance):
    original = instance.inStructuredNode
    instance.inStructuredNode = original
    assert instance.inStructuredNode == original

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inGroup_type(instance):
    assert isinstance(instance.inGroup, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inGroup_setter(instance):
    original = instance.inGroup
    instance.inGroup = original
    assert instance.inGroup == original

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inPartition_type(instance):
    assert isinstance(instance.inPartition, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inPartition_setter(instance):
    original = instance.inPartition
    instance.inPartition = original
    assert instance.inPartition == original

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_redefinedNode_type(instance):
    assert isinstance(instance.redefinedNode, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_redefinedNode_setter(instance):
    original = instance.redefinedNode
    instance.redefinedNode = original
    assert instance.redefinedNode == original

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_outgoing_type(instance):
    assert isinstance(instance.outgoing, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_outgoing_setter(instance):
    original = instance.outgoing
    instance.outgoing = original
    assert instance.outgoing == original

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_incoming_type(instance):
    assert isinstance(instance.incoming, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_incoming_setter(instance):
    original = instance.incoming
    instance.incoming = original
    assert instance.incoming == original

@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inInterruptibleRegion_type(instance):
    assert isinstance(instance.inInterruptibleRegion, str)


@given(instance=UMLModel::ActivityNode_strategy)
def test_umlmodel::activitynode_inInterruptibleRegion_setter(instance):
    original = instance.inInterruptibleRegion
    instance.inInterruptibleRegion = original
    assert instance.inInterruptibleRegion == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UMLModel::StateMachine_strategy)
@settings(max_examples=50)
def test_umlmodel::statemachine_instantiation(instance):
    assert isinstance(instance, UMLModel::StateMachine)

@given(instance=UMLModel::StateMachine_strategy)
def test_umlmodel::statemachine_extendedStateMachine_type(instance):
    assert isinstance(instance.extendedStateMachine, str)


@given(instance=UMLModel::StateMachine_strategy)
def test_umlmodel::statemachine_extendedStateMachine_setter(instance):
    original = instance.extendedStateMachine
    instance.extendedStateMachine = original
    assert instance.extendedStateMachine == original

@given(instance=UMLModel::StateMachine_strategy)
def test_umlmodel::statemachine_submachineState_type(instance):
    assert isinstance(instance.submachineState, str)


@given(instance=UMLModel::StateMachine_strategy)
def test_umlmodel::statemachine_submachineState_setter(instance):
    original = instance.submachineState
    instance.submachineState = original
    assert instance.submachineState == original

@given(instance=UMLModel::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_umlmodel::opaquebehavior_instantiation(instance):
    assert isinstance(instance, UMLModel::OpaqueBehavior)

@given(instance=UMLModel::OpaqueBehavior_strategy)
def test_umlmodel::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=UMLModel::OpaqueBehavior_strategy)
def test_umlmodel::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UMLModel::OpaqueBehavior_strategy)
def test_umlmodel::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UMLModel::OpaqueBehavior_strategy)
def test_umlmodel::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UMLModel::Activity_strategy)
@settings(max_examples=50)
def test_umlmodel::activity_instantiation(instance):
    assert isinstance(instance, UMLModel::Activity)

@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, str)


@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_partition_type(instance):
    assert isinstance(instance.partition, str)


@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_partition_setter(instance):
    original = instance.partition
    instance.partition = original
    assert instance.partition == original

@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_structuredNode_type(instance):
    assert isinstance(instance.structuredNode, str)


@given(instance=UMLModel::Activity_strategy)
def test_umlmodel::activity_structuredNode_setter(instance):
    original = instance.structuredNode
    instance.structuredNode = original
    assert instance.structuredNode == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UMLModel::ValuePin_strategy)
@settings(max_examples=50)
def test_umlmodel::valuepin_instantiation(instance):
    assert isinstance(instance, UMLModel::ValuePin)

@given(instance=UMLModel::ActionInputPin_strategy)
@settings(max_examples=50)
def test_umlmodel::actioninputpin_instantiation(instance):
    assert isinstance(instance, UMLModel::ActionInputPin)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=UMLModel::ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, UMLModel::ActionExecutionSpecification)

@given(instance=UMLModel::ActionExecutionSpecification_strategy)
def test_umlmodel::actionexecutionspecification_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=UMLModel::ActionExecutionSpecification_strategy)
def test_umlmodel::actionexecutionspecification_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=UMLModel::ActivityGroup_strategy)
@settings(max_examples=50)
def test_umlmodel::activitygroup_instantiation(instance):
    assert isinstance(instance, UMLModel::ActivityGroup)

@given(instance=UMLModel::ActivityGroup_strategy)
def test_umlmodel::activitygroup_subgroup_type(instance):
    assert isinstance(instance.subgroup, str)


@given(instance=UMLModel::ActivityGroup_strategy)
def test_umlmodel::activitygroup_subgroup_setter(instance):
    original = instance.subgroup
    instance.subgroup = original
    assert instance.subgroup == original

@given(instance=UMLModel::ActivityGroup_strategy)
def test_umlmodel::activitygroup_superGroup_type(instance):
    assert isinstance(instance.superGroup, str)


@given(instance=UMLModel::ActivityGroup_strategy)
def test_umlmodel::activitygroup_superGroup_setter(instance):
    original = instance.superGroup
    instance.superGroup = original
    assert instance.superGroup == original

@given(instance=UMLModel::ActivityGroup_strategy)
def test_umlmodel::activitygroup_inActivity_type(instance):
    assert isinstance(instance.inActivity, str)


@given(instance=UMLModel::ActivityGroup_strategy)
def test_umlmodel::activitygroup_inActivity_setter(instance):
    original = instance.inActivity
    instance.inActivity = original
    assert instance.inActivity == original

@given(instance=UMLModel::ActivityEdge_strategy)
@settings(max_examples=50)
def test_umlmodel::activityedge_instantiation(instance):
    assert isinstance(instance, UMLModel::ActivityEdge)

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_interrupts_type(instance):
    assert isinstance(instance.interrupts, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_interrupts_setter(instance):
    original = instance.interrupts
    instance.interrupts = original
    assert instance.interrupts == original

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_inGroup_type(instance):
    assert isinstance(instance.inGroup, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_inGroup_setter(instance):
    original = instance.inGroup
    instance.inGroup = original
    assert instance.inGroup == original

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_redefinedEdge_type(instance):
    assert isinstance(instance.redefinedEdge, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_redefinedEdge_setter(instance):
    original = instance.redefinedEdge
    instance.redefinedEdge = original
    assert instance.redefinedEdge == original

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_inPartition_type(instance):
    assert isinstance(instance.inPartition, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_inPartition_setter(instance):
    original = instance.inPartition
    instance.inPartition = original
    assert instance.inPartition == original

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_inStructuredNode_type(instance):
    assert isinstance(instance.inStructuredNode, str)


@given(instance=UMLModel::ActivityEdge_strategy)
def test_umlmodel::activityedge_inStructuredNode_setter(instance):
    original = instance.inStructuredNode
    instance.inStructuredNode = original
    assert instance.inStructuredNode == original

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=UMLModel::AcceptCallAction_strategy)
@settings(max_examples=50)
def test_umlmodel::acceptcallaction_instantiation(instance):
    assert isinstance(instance, UMLModel::AcceptCallAction)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=UMLModel::Usage_strategy)
@settings(max_examples=50)
def test_umlmodel::usage_instantiation(instance):
    assert isinstance(instance, UMLModel::Usage)

@given(instance=UMLModel::Abstraction_strategy)
@settings(max_examples=50)
def test_umlmodel::abstraction_instantiation(instance):
    assert isinstance(instance, UMLModel::Abstraction)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=UMLModel::Action_strategy)
@settings(max_examples=50)
def test_umlmodel::action_instantiation(instance):
    assert isinstance(instance, UMLModel::Action)

@given(instance=UMLModel::Action_strategy)
def test_umlmodel::action_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=UMLModel::Action_strategy)
def test_umlmodel::action_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=UMLModel::Action_strategy)
def test_umlmodel::action_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=UMLModel::Action_strategy)
def test_umlmodel::action_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=UMLModel::Action_strategy)
def test_umlmodel::action_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=UMLModel::Action_strategy)
def test_umlmodel::action_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=UMLModel::Trigger_strategy)
@settings(max_examples=50)
def test_umlmodel::trigger_instantiation(instance):
    assert isinstance(instance, UMLModel::Trigger)

@given(instance=UMLModel::Trigger_strategy)
def test_umlmodel::trigger_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=UMLModel::Trigger_strategy)
def test_umlmodel::trigger_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=UMLModel::Trigger_strategy)
def test_umlmodel::trigger_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=UMLModel::Trigger_strategy)
def test_umlmodel::trigger_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UMLModel::VariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel::variableaction_instantiation(instance):
    assert isinstance(instance, UMLModel::VariableAction)

@given(instance=UMLModel::VariableAction_strategy)
def test_umlmodel::variableaction_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=UMLModel::VariableAction_strategy)
def test_umlmodel::variableaction_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=UMLModel::UnmarshallAction_strategy)
@settings(max_examples=50)
def test_umlmodel::unmarshallaction_instantiation(instance):
    assert isinstance(instance, UMLModel::UnmarshallAction)

@given(instance=UMLModel::UnmarshallAction_strategy)
def test_umlmodel::unmarshallaction_unmarshallType_type(instance):
    assert isinstance(instance.unmarshallType, str)


@given(instance=UMLModel::UnmarshallAction_strategy)
def test_umlmodel::unmarshallaction_unmarshallType_setter(instance):
    original = instance.unmarshallType
    instance.unmarshallType = original
    assert instance.unmarshallType == original

@given(instance=UMLModel::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_umlmodel::testidentityaction_instantiation(instance):
    assert isinstance(instance, UMLModel::TestIdentityAction)

@given(instance=UMLModel::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_umlmodel::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, UMLModel::StartClassifierBehaviorAction)

@given(instance=UMLModel::RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_umlmodel::raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UMLModel::RaiseExceptionAction)

@given(instance=UMLModel::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readextentaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadExtentAction)

@given(instance=UMLModel::ReadExtentAction_strategy)
def test_umlmodel::readextentaction_classifier_type(instance):
    assert isinstance(instance.classifier, str)


@given(instance=UMLModel::ReadExtentAction_strategy)
def test_umlmodel::readextentaction_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=UMLModel::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReclassifyObjectAction)

@given(instance=UMLModel::ReclassifyObjectAction_strategy)
def test_umlmodel::reclassifyobjectaction_isReplaceAll_type(instance):
    assert isinstance(instance.isReplaceAll, str)


@given(instance=UMLModel::ReclassifyObjectAction_strategy)
def test_umlmodel::reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=UMLModel::ReclassifyObjectAction_strategy)
def test_umlmodel::reclassifyobjectaction_oldClassifier_type(instance):
    assert isinstance(instance.oldClassifier, str)


@given(instance=UMLModel::ReclassifyObjectAction_strategy)
def test_umlmodel::reclassifyobjectaction_oldClassifier_setter(instance):
    original = instance.oldClassifier
    instance.oldClassifier = original
    assert instance.oldClassifier == original

@given(instance=UMLModel::ReclassifyObjectAction_strategy)
def test_umlmodel::reclassifyobjectaction_newClassifier_type(instance):
    assert isinstance(instance.newClassifier, str)


@given(instance=UMLModel::ReclassifyObjectAction_strategy)
def test_umlmodel::reclassifyobjectaction_newClassifier_setter(instance):
    original = instance.newClassifier
    instance.newClassifier = original
    assert instance.newClassifier == original

@given(instance=UMLModel::InvocationAction_strategy)
@settings(max_examples=50)
def test_umlmodel::invocationaction_instantiation(instance):
    assert isinstance(instance, UMLModel::InvocationAction)

@given(instance=UMLModel::InvocationAction_strategy)
def test_umlmodel::invocationaction_onPort_type(instance):
    assert isinstance(instance.onPort, str)


@given(instance=UMLModel::InvocationAction_strategy)
def test_umlmodel::invocationaction_onPort_setter(instance):
    original = instance.onPort
    instance.onPort = original
    assert instance.onPort == original

@given(instance=UMLModel::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadIsClassifiedObjectAction)

@given(instance=UMLModel::ReadIsClassifiedObjectAction_strategy)
def test_umlmodel::readisclassifiedobjectaction_classifier_type(instance):
    assert isinstance(instance.classifier, str)


@given(instance=UMLModel::ReadIsClassifiedObjectAction_strategy)
def test_umlmodel::readisclassifiedobjectaction_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=UMLModel::ReadIsClassifiedObjectAction_strategy)
def test_umlmodel::readisclassifiedobjectaction_isDirect_type(instance):
    assert isinstance(instance.isDirect, str)


@given(instance=UMLModel::ReadIsClassifiedObjectAction_strategy)
def test_umlmodel::readisclassifiedobjectaction_isDirect_setter(instance):
    original = instance.isDirect
    instance.isDirect = original
    assert instance.isDirect == original

@given(instance=UMLModel::ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadLinkObjectEndAction)

@given(instance=UMLModel::ReadLinkObjectEndAction_strategy)
def test_umlmodel::readlinkobjectendaction_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=UMLModel::ReadLinkObjectEndAction_strategy)
def test_umlmodel::readlinkobjectendaction_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=UMLModel::ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadLinkObjectEndQualifierAction)

@given(instance=UMLModel::ReadLinkObjectEndQualifierAction_strategy)
def test_umlmodel::readlinkobjectendqualifieraction_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=UMLModel::ReadLinkObjectEndQualifierAction_strategy)
def test_umlmodel::readlinkobjectendqualifieraction_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=UMLModel::OpaqueAction_strategy)
@settings(max_examples=50)
def test_umlmodel::opaqueaction_instantiation(instance):
    assert isinstance(instance, UMLModel::OpaqueAction)

@given(instance=UMLModel::OpaqueAction_strategy)
def test_umlmodel::opaqueaction_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UMLModel::OpaqueAction_strategy)
def test_umlmodel::opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UMLModel::OpaqueAction_strategy)
def test_umlmodel::opaqueaction_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=UMLModel::OpaqueAction_strategy)
def test_umlmodel::opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UMLModel::LinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel::linkaction_instantiation(instance):
    assert isinstance(instance, UMLModel::LinkAction)

@given(instance=UMLModel::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_umlmodel::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ValueSpecificationAction)

@given(instance=UMLModel::ReduceAction_strategy)
@settings(max_examples=50)
def test_umlmodel::reduceaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReduceAction)

@given(instance=UMLModel::ReduceAction_strategy)
def test_umlmodel::reduceaction_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=UMLModel::ReduceAction_strategy)
def test_umlmodel::reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=UMLModel::ReduceAction_strategy)
def test_umlmodel::reduceaction_reducer_type(instance):
    assert isinstance(instance.reducer, str)


@given(instance=UMLModel::ReduceAction_strategy)
def test_umlmodel::reduceaction_reducer_setter(instance):
    original = instance.reducer
    instance.reducer = original
    assert instance.reducer == original

@given(instance=UMLModel::ReplyAction_strategy)
@settings(max_examples=50)
def test_umlmodel::replyaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReplyAction)

@given(instance=UMLModel::ReplyAction_strategy)
def test_umlmodel::replyaction_replyToCall_type(instance):
    assert isinstance(instance.replyToCall, str)


@given(instance=UMLModel::ReplyAction_strategy)
def test_umlmodel::replyaction_replyToCall_setter(instance):
    original = instance.replyToCall
    instance.replyToCall = original
    assert instance.replyToCall == original

@given(instance=UMLModel::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel::StructuralFeatureAction)

@given(instance=UMLModel::StructuralFeatureAction_strategy)
def test_umlmodel::structuralfeatureaction_structuralFeature_type(instance):
    assert isinstance(instance.structuralFeature, str)


@given(instance=UMLModel::StructuralFeatureAction_strategy)
def test_umlmodel::structuralfeatureaction_structuralFeature_setter(instance):
    original = instance.structuralFeature
    instance.structuralFeature = original
    assert instance.structuralFeature == original

@given(instance=UMLModel::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readselfaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadSelfAction)

@given(instance=UMLModel::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_umlmodel::accepteventaction_instantiation(instance):
    assert isinstance(instance, UMLModel::AcceptEventAction)

@given(instance=UMLModel::AcceptEventAction_strategy)
def test_umlmodel::accepteventaction_isUnmarshall_type(instance):
    assert isinstance(instance.isUnmarshall, str)


@given(instance=UMLModel::AcceptEventAction_strategy)
def test_umlmodel::accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=UMLModel::OutputPin_strategy)
@settings(max_examples=50)
def test_umlmodel::outputpin_instantiation(instance):
    assert isinstance(instance, UMLModel::OutputPin)

@given(instance=UMLBase_strategy)
@settings(max_examples=50)
def test_umlbase_instantiation(instance):
    assert isinstance(instance, UMLBase)

@given(instance=UMLModel::Element_strategy)
@settings(max_examples=50)
def test_umlmodel::element_instantiation(instance):
    assert isinstance(instance, UMLModel::Element)

@given(instance=UMLModel::Element_strategy)
def test_umlmodel::element_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=UMLModel::Element_strategy)
def test_umlmodel::element_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=UMLModel::Element_strategy)
def test_umlmodel::element_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=UMLModel::Element_strategy)
def test_umlmodel::element_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=UMLModel::Element_strategy)
def test_umlmodel::element_ownedElement_type(instance):
    assert isinstance(instance.ownedElement, str)


@given(instance=UMLModel::Element_strategy)
def test_umlmodel::element_ownedElement_setter(instance):
    original = instance.ownedElement
    instance.ownedElement = original
    assert instance.ownedElement == original

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=UMLModel::TimeObservation_strategy)
@settings(max_examples=50)
def test_umlmodel::timeobservation_instantiation(instance):
    assert isinstance(instance, UMLModel::TimeObservation)

@given(instance=UMLModel::TimeObservation_strategy)
def test_umlmodel::timeobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=UMLModel::TimeObservation_strategy)
def test_umlmodel::timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=UMLModel::TimeObservation_strategy)
def test_umlmodel::timeobservation_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=UMLModel::TimeObservation_strategy)
def test_umlmodel::timeobservation_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=UMLModel::DurationObservation_strategy)
@settings(max_examples=50)
def test_umlmodel::durationobservation_instantiation(instance):
    assert isinstance(instance, UMLModel::DurationObservation)

@given(instance=UMLModel::DurationObservation_strategy)
def test_umlmodel::durationobservation_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=UMLModel::DurationObservation_strategy)
def test_umlmodel::durationobservation_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=UMLModel::DurationObservation_strategy)
def test_umlmodel::durationobservation_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=UMLModel::DurationObservation_strategy)
def test_umlmodel::durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UMLModel::TimeInterval_strategy)
@settings(max_examples=50)
def test_umlmodel::timeinterval_instantiation(instance):
    assert isinstance(instance, UMLModel::TimeInterval)

@given(instance=UMLModel::DurationInterval_strategy)
@settings(max_examples=50)
def test_umlmodel::durationinterval_instantiation(instance):
    assert isinstance(instance, UMLModel::DurationInterval)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=UMLModel::TimeConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel::timeconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel::TimeConstraint)

@given(instance=UMLModel::TimeConstraint_strategy)
def test_umlmodel::timeconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=UMLModel::TimeConstraint_strategy)
def test_umlmodel::timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=UMLModel::DurationConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel::durationconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel::DurationConstraint)

@given(instance=UMLModel::DurationConstraint_strategy)
def test_umlmodel::durationconstraint_firstEvent_type(instance):
    assert isinstance(instance.firstEvent, str)


@given(instance=UMLModel::DurationConstraint_strategy)
def test_umlmodel::durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UMLModel::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::literalspecification_instantiation(instance):
    assert isinstance(instance, UMLModel::LiteralSpecification)

@given(instance=UMLModel::Interval_strategy)
@settings(max_examples=50)
def test_umlmodel::interval_instantiation(instance):
    assert isinstance(instance, UMLModel::Interval)

@given(instance=UMLModel::Interval_strategy)
def test_umlmodel::interval_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=UMLModel::Interval_strategy)
def test_umlmodel::interval_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=UMLModel::Interval_strategy)
def test_umlmodel::interval_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=UMLModel::Interval_strategy)
def test_umlmodel::interval_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=UMLModel::InstanceValue_strategy)
@settings(max_examples=50)
def test_umlmodel::instancevalue_instantiation(instance):
    assert isinstance(instance, UMLModel::InstanceValue)

@given(instance=UMLModel::InstanceValue_strategy)
def test_umlmodel::instancevalue_instance_type(instance):
    assert isinstance(instance.instance, str)


@given(instance=UMLModel::InstanceValue_strategy)
def test_umlmodel::instancevalue_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original

@given(instance=UMLModel::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_umlmodel::opaqueexpression_instantiation(instance):
    assert isinstance(instance, UMLModel::OpaqueExpression)

@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_behavior_type(instance):
    assert isinstance(instance.behavior, str)


@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_result_type(instance):
    assert isinstance(instance.result, str)


@given(instance=UMLModel::OpaqueExpression_strategy)
def test_umlmodel::opaqueexpression_result_setter(instance):
    original = instance.result
    instance.result = original
    assert instance.result == original

@given(instance=UMLModel::TimeExpression_strategy)
@settings(max_examples=50)
def test_umlmodel::timeexpression_instantiation(instance):
    assert isinstance(instance, UMLModel::TimeExpression)

@given(instance=UMLModel::TimeExpression_strategy)
def test_umlmodel::timeexpression_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=UMLModel::TimeExpression_strategy)
def test_umlmodel::timeexpression_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=UMLModel::TimeExpression_strategy)
def test_umlmodel::timeexpression_observation_type(instance):
    assert isinstance(instance.observation, str)


@given(instance=UMLModel::TimeExpression_strategy)
def test_umlmodel::timeexpression_observation_setter(instance):
    original = instance.observation
    instance.observation = original
    assert instance.observation == original

@given(instance=UMLModel::Expression_strategy)
@settings(max_examples=50)
def test_umlmodel::expression_instantiation(instance):
    assert isinstance(instance, UMLModel::Expression)

@given(instance=UMLModel::Expression_strategy)
def test_umlmodel::expression_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=UMLModel::Expression_strategy)
def test_umlmodel::expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=UMLModel::Duration_strategy)
@settings(max_examples=50)
def test_umlmodel::duration_instantiation(instance):
    assert isinstance(instance, UMLModel::Duration)

@given(instance=UMLModel::Duration_strategy)
def test_umlmodel::duration_observation_type(instance):
    assert isinstance(instance.observation, str)


@given(instance=UMLModel::Duration_strategy)
def test_umlmodel::duration_observation_setter(instance):
    original = instance.observation
    instance.observation = original
    assert instance.observation == original

@given(instance=UMLModel::Duration_strategy)
def test_umlmodel::duration_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=UMLModel::Duration_strategy)
def test_umlmodel::duration_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=UMLModel::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_umlmodel::enumerationliteral_instantiation(instance):
    assert isinstance(instance, UMLModel::EnumerationLiteral)

@given(instance=UMLModel::EnumerationLiteral_strategy)
def test_umlmodel::enumerationliteral_enumeration_type(instance):
    assert isinstance(instance.enumeration, str)


@given(instance=UMLModel::EnumerationLiteral_strategy)
def test_umlmodel::enumerationliteral_enumeration_setter(instance):
    original = instance.enumeration
    instance.enumeration = original
    assert instance.enumeration == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UMLModel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_umlmodel::primitivetype_instantiation(instance):
    assert isinstance(instance, UMLModel::PrimitiveType)

@given(instance=UMLModel::Enumeration_strategy)
@settings(max_examples=50)
def test_umlmodel::enumeration_instantiation(instance):
    assert isinstance(instance, UMLModel::Enumeration)

@given(instance=UMLModel::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel::DestroyObjectAction)

@given(instance=UMLModel::DestroyObjectAction_strategy)
def test_umlmodel::destroyobjectaction_isDestroyOwnedObjects_type(instance):
    assert isinstance(instance.isDestroyOwnedObjects, str)


@given(instance=UMLModel::DestroyObjectAction_strategy)
def test_umlmodel::destroyobjectaction_isDestroyOwnedObjects_setter(instance):
    original = instance.isDestroyOwnedObjects
    instance.isDestroyOwnedObjects = original
    assert instance.isDestroyOwnedObjects == original

@given(instance=UMLModel::DestroyObjectAction_strategy)
def test_umlmodel::destroyobjectaction_isDestroyLinks_type(instance):
    assert isinstance(instance.isDestroyLinks, str)


@given(instance=UMLModel::DestroyObjectAction_strategy)
def test_umlmodel::destroyobjectaction_isDestroyLinks_setter(instance):
    original = instance.isDestroyLinks
    instance.isDestroyLinks = original
    assert instance.isDestroyLinks == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UMLModel::ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_umlmodel::executionenvironment_instantiation(instance):
    assert isinstance(instance, UMLModel::ExecutionEnvironment)

@given(instance=UMLModel::Device_strategy)
@settings(max_examples=50)
def test_umlmodel::device_instantiation(instance):
    assert isinstance(instance, UMLModel::Device)

@given(instance=UMLModel::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_umlmodel::directedrelationship_instantiation(instance):
    assert isinstance(instance, UMLModel::DirectedRelationship)

@given(instance=UMLModel::DirectedRelationship_strategy)
def test_umlmodel::directedrelationship_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=UMLModel::DirectedRelationship_strategy)
def test_umlmodel::directedrelationship_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=UMLModel::DirectedRelationship_strategy)
def test_umlmodel::directedrelationship_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=UMLModel::DirectedRelationship_strategy)
def test_umlmodel::directedrelationship_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UMLModel::DeployedArtifact_strategy)
@settings(max_examples=50)
def test_umlmodel::deployedartifact_instantiation(instance):
    assert isinstance(instance, UMLModel::DeployedArtifact)

@given(instance=UMLModel::DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::deploymentspecification_instantiation(instance):
    assert isinstance(instance, UMLModel::DeploymentSpecification)

@given(instance=UMLModel::DeploymentSpecification_strategy)
def test_umlmodel::deploymentspecification_executionLocation_type(instance):
    assert isinstance(instance.executionLocation, str)


@given(instance=UMLModel::DeploymentSpecification_strategy)
def test_umlmodel::deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original

@given(instance=UMLModel::DeploymentSpecification_strategy)
def test_umlmodel::deploymentspecification_deploymentLocation_type(instance):
    assert isinstance(instance.deploymentLocation, str)


@given(instance=UMLModel::DeploymentSpecification_strategy)
def test_umlmodel::deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=UMLModel::DeploymentSpecification_strategy)
def test_umlmodel::deploymentspecification_deployment_type(instance):
    assert isinstance(instance.deployment, str)


@given(instance=UMLModel::DeploymentSpecification_strategy)
def test_umlmodel::deploymentspecification_deployment_setter(instance):
    original = instance.deployment
    instance.deployment = original
    assert instance.deployment == original

@given(instance=UMLModel::Deployment_strategy)
@settings(max_examples=50)
def test_umlmodel::deployment_instantiation(instance):
    assert isinstance(instance, UMLModel::Deployment)

@given(instance=UMLModel::Deployment_strategy)
def test_umlmodel::deployment_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=UMLModel::Deployment_strategy)
def test_umlmodel::deployment_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=UMLModel::Deployment_strategy)
def test_umlmodel::deployment_deployedArtifact_type(instance):
    assert isinstance(instance.deployedArtifact, str)


@given(instance=UMLModel::Deployment_strategy)
def test_umlmodel::deployment_deployedArtifact_setter(instance):
    original = instance.deployedArtifact
    instance.deployedArtifact = original
    assert instance.deployedArtifact == original

@given(instance=UMLModel::DeploymentTarget_strategy)
@settings(max_examples=50)
def test_umlmodel::deploymenttarget_instantiation(instance):
    assert isinstance(instance, UMLModel::DeploymentTarget)

@given(instance=UMLModel::DeploymentTarget_strategy)
def test_umlmodel::deploymenttarget_deployedElement_type(instance):
    assert isinstance(instance.deployedElement, str)


@given(instance=UMLModel::DeploymentTarget_strategy)
def test_umlmodel::deploymenttarget_deployedElement_setter(instance):
    original = instance.deployedElement
    instance.deployedElement = original
    assert instance.deployedElement == original

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=UMLModel::Pin_strategy)
@settings(max_examples=50)
def test_umlmodel::pin_instantiation(instance):
    assert isinstance(instance, UMLModel::Pin)

@given(instance=UMLModel::Pin_strategy)
def test_umlmodel::pin_isControl_type(instance):
    assert isinstance(instance.isControl, str)


@given(instance=UMLModel::Pin_strategy)
def test_umlmodel::pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=UMLModel::Variable_strategy)
@settings(max_examples=50)
def test_umlmodel::variable_instantiation(instance):
    assert isinstance(instance, UMLModel::Variable)

@given(instance=UMLModel::Variable_strategy)
def test_umlmodel::variable_activityScope_type(instance):
    assert isinstance(instance.activityScope, str)


@given(instance=UMLModel::Variable_strategy)
def test_umlmodel::variable_activityScope_setter(instance):
    original = instance.activityScope
    instance.activityScope = original
    assert instance.activityScope == original

@given(instance=UMLModel::Variable_strategy)
def test_umlmodel::variable_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=UMLModel::Variable_strategy)
def test_umlmodel::variable_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=UMLModel::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_umlmodel::connectorend_instantiation(instance):
    assert isinstance(instance, UMLModel::ConnectorEnd)

@given(instance=UMLModel::ConnectorEnd_strategy)
def test_umlmodel::connectorend_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=UMLModel::ConnectorEnd_strategy)
def test_umlmodel::connectorend_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=UMLModel::ConnectorEnd_strategy)
def test_umlmodel::connectorend_definingEnd_type(instance):
    assert isinstance(instance.definingEnd, str)


@given(instance=UMLModel::ConnectorEnd_strategy)
def test_umlmodel::connectorend_definingEnd_setter(instance):
    original = instance.definingEnd
    instance.definingEnd = original
    assert instance.definingEnd == original

@given(instance=UMLModel::ConnectorEnd_strategy)
def test_umlmodel::connectorend_partWithPort_type(instance):
    assert isinstance(instance.partWithPort, str)


@given(instance=UMLModel::ConnectorEnd_strategy)
def test_umlmodel::connectorend_partWithPort_setter(instance):
    original = instance.partWithPort
    instance.partWithPort = original
    assert instance.partWithPort == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=UMLModel::Extend_strategy)
@settings(max_examples=50)
def test_umlmodel::extend_instantiation(instance):
    assert isinstance(instance, UMLModel::Extend)

@given(instance=UMLModel::Extend_strategy)
def test_umlmodel::extend_extensionLocation_type(instance):
    assert isinstance(instance.extensionLocation, str)


@given(instance=UMLModel::Extend_strategy)
def test_umlmodel::extend_extensionLocation_setter(instance):
    original = instance.extensionLocation
    instance.extensionLocation = original
    assert instance.extensionLocation == original

@given(instance=UMLModel::Extend_strategy)
def test_umlmodel::extend_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=UMLModel::Extend_strategy)
def test_umlmodel::extend_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=UMLModel::Extend_strategy)
def test_umlmodel::extend_extendedCase_type(instance):
    assert isinstance(instance.extendedCase, str)


@given(instance=UMLModel::Extend_strategy)
def test_umlmodel::extend_extendedCase_setter(instance):
    original = instance.extendedCase
    instance.extendedCase = original
    assert instance.extendedCase == original

@given(instance=UMLModel::ProtocolConformance_strategy)
@settings(max_examples=50)
def test_umlmodel::protocolconformance_instantiation(instance):
    assert isinstance(instance, UMLModel::ProtocolConformance)

@given(instance=UMLModel::ProtocolConformance_strategy)
def test_umlmodel::protocolconformance_specificMachine_type(instance):
    assert isinstance(instance.specificMachine, str)


@given(instance=UMLModel::ProtocolConformance_strategy)
def test_umlmodel::protocolconformance_specificMachine_setter(instance):
    original = instance.specificMachine
    instance.specificMachine = original
    assert instance.specificMachine == original

@given(instance=UMLModel::ProtocolConformance_strategy)
def test_umlmodel::protocolconformance_generalMachine_type(instance):
    assert isinstance(instance.generalMachine, str)


@given(instance=UMLModel::ProtocolConformance_strategy)
def test_umlmodel::protocolconformance_generalMachine_setter(instance):
    original = instance.generalMachine
    instance.generalMachine = original
    assert instance.generalMachine == original

@given(instance=UMLModel::ElementImport_strategy)
@settings(max_examples=50)
def test_umlmodel::elementimport_instantiation(instance):
    assert isinstance(instance, UMLModel::ElementImport)

@given(instance=UMLModel::ElementImport_strategy)
def test_umlmodel::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UMLModel::ElementImport_strategy)
def test_umlmodel::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=UMLModel::ElementImport_strategy)
def test_umlmodel::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=UMLModel::ElementImport_strategy)
def test_umlmodel::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=UMLModel::ElementImport_strategy)
def test_umlmodel::elementimport_importingNamespace_type(instance):
    assert isinstance(instance.importingNamespace, str)


@given(instance=UMLModel::ElementImport_strategy)
def test_umlmodel::elementimport_importingNamespace_setter(instance):
    original = instance.importingNamespace
    instance.importingNamespace = original
    assert instance.importingNamespace == original

@given(instance=UMLModel::Include_strategy)
@settings(max_examples=50)
def test_umlmodel::include_instantiation(instance):
    assert isinstance(instance, UMLModel::Include)

@given(instance=UMLModel::Include_strategy)
def test_umlmodel::include_addition_type(instance):
    assert isinstance(instance.addition, str)


@given(instance=UMLModel::Include_strategy)
def test_umlmodel::include_addition_setter(instance):
    original = instance.addition
    instance.addition = original
    assert instance.addition == original

@given(instance=UMLModel::Include_strategy)
def test_umlmodel::include_includingCase_type(instance):
    assert isinstance(instance.includingCase, str)


@given(instance=UMLModel::Include_strategy)
def test_umlmodel::include_includingCase_setter(instance):
    original = instance.includingCase
    instance.includingCase = original
    assert instance.includingCase == original

@given(instance=UMLModel::TemplateBinding_strategy)
@settings(max_examples=50)
def test_umlmodel::templatebinding_instantiation(instance):
    assert isinstance(instance, UMLModel::TemplateBinding)

@given(instance=UMLModel::TemplateBinding_strategy)
def test_umlmodel::templatebinding_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=UMLModel::TemplateBinding_strategy)
def test_umlmodel::templatebinding_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=UMLModel::TemplateBinding_strategy)
def test_umlmodel::templatebinding_boundElement_type(instance):
    assert isinstance(instance.boundElement, str)


@given(instance=UMLModel::TemplateBinding_strategy)
def test_umlmodel::templatebinding_boundElement_setter(instance):
    original = instance.boundElement
    instance.boundElement = original
    assert instance.boundElement == original

@given(instance=UMLModel::ProfileApplication_strategy)
@settings(max_examples=50)
def test_umlmodel::profileapplication_instantiation(instance):
    assert isinstance(instance, UMLModel::ProfileApplication)

@given(instance=UMLModel::ProfileApplication_strategy)
def test_umlmodel::profileapplication_appliedProfile_type(instance):
    assert isinstance(instance.appliedProfile, str)


@given(instance=UMLModel::ProfileApplication_strategy)
def test_umlmodel::profileapplication_appliedProfile_setter(instance):
    original = instance.appliedProfile
    instance.appliedProfile = original
    assert instance.appliedProfile == original

@given(instance=UMLModel::ProfileApplication_strategy)
def test_umlmodel::profileapplication_applyingPackage_type(instance):
    assert isinstance(instance.applyingPackage, str)


@given(instance=UMLModel::ProfileApplication_strategy)
def test_umlmodel::profileapplication_applyingPackage_setter(instance):
    original = instance.applyingPackage
    instance.applyingPackage = original
    assert instance.applyingPackage == original

@given(instance=UMLModel::ProfileApplication_strategy)
def test_umlmodel::profileapplication_isStrict_type(instance):
    assert isinstance(instance.isStrict, str)


@given(instance=UMLModel::ProfileApplication_strategy)
def test_umlmodel::profileapplication_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=UMLModel::PackageMerge_strategy)
@settings(max_examples=50)
def test_umlmodel::packagemerge_instantiation(instance):
    assert isinstance(instance, UMLModel::PackageMerge)

@given(instance=UMLModel::PackageMerge_strategy)
def test_umlmodel::packagemerge_receivingPackage_type(instance):
    assert isinstance(instance.receivingPackage, str)


@given(instance=UMLModel::PackageMerge_strategy)
def test_umlmodel::packagemerge_receivingPackage_setter(instance):
    original = instance.receivingPackage
    instance.receivingPackage = original
    assert instance.receivingPackage == original

@given(instance=UMLModel::PackageMerge_strategy)
def test_umlmodel::packagemerge_mergedPackage_type(instance):
    assert isinstance(instance.mergedPackage, str)


@given(instance=UMLModel::PackageMerge_strategy)
def test_umlmodel::packagemerge_mergedPackage_setter(instance):
    original = instance.mergedPackage
    instance.mergedPackage = original
    assert instance.mergedPackage == original

@given(instance=UMLModel::PackageImport_strategy)
@settings(max_examples=50)
def test_umlmodel::packageimport_instantiation(instance):
    assert isinstance(instance, UMLModel::PackageImport)

@given(instance=UMLModel::PackageImport_strategy)
def test_umlmodel::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=UMLModel::PackageImport_strategy)
def test_umlmodel::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=UMLModel::PackageImport_strategy)
def test_umlmodel::packageimport_importingNamespace_type(instance):
    assert isinstance(instance.importingNamespace, str)


@given(instance=UMLModel::PackageImport_strategy)
def test_umlmodel::packageimport_importingNamespace_setter(instance):
    original = instance.importingNamespace
    instance.importingNamespace = original
    assert instance.importingNamespace == original

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=UMLModel::ForkNode_strategy)
@settings(max_examples=50)
def test_umlmodel::forknode_instantiation(instance):
    assert isinstance(instance, UMLModel::ForkNode)

@given(instance=UMLModel::JoinNode_strategy)
@settings(max_examples=50)
def test_umlmodel::joinnode_instantiation(instance):
    assert isinstance(instance, UMLModel::JoinNode)

@given(instance=UMLModel::JoinNode_strategy)
def test_umlmodel::joinnode_isCombineDuplicate_type(instance):
    assert isinstance(instance.isCombineDuplicate, str)


@given(instance=UMLModel::JoinNode_strategy)
def test_umlmodel::joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=UMLModel::FinalNode_strategy)
@settings(max_examples=50)
def test_umlmodel::finalnode_instantiation(instance):
    assert isinstance(instance, UMLModel::FinalNode)

@given(instance=UMLModel::MergeNode_strategy)
@settings(max_examples=50)
def test_umlmodel::mergenode_instantiation(instance):
    assert isinstance(instance, UMLModel::MergeNode)

@given(instance=UMLModel::InitialNode_strategy)
@settings(max_examples=50)
def test_umlmodel::initialnode_instantiation(instance):
    assert isinstance(instance, UMLModel::InitialNode)

@given(instance=UMLModel::ConnectableElement_strategy)
@settings(max_examples=50)
def test_umlmodel::connectableelement_instantiation(instance):
    assert isinstance(instance, UMLModel::ConnectableElement)

@given(instance=UMLModel::ConnectableElement_strategy)
def test_umlmodel::connectableelement_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=UMLModel::ConnectableElement_strategy)
def test_umlmodel::connectableelement_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=UMLModel::DecisionNode_strategy)
@settings(max_examples=50)
def test_umlmodel::decisionnode_instantiation(instance):
    assert isinstance(instance, UMLModel::DecisionNode)

@given(instance=UMLModel::DecisionNode_strategy)
def test_umlmodel::decisionnode_decisionInput_type(instance):
    assert isinstance(instance.decisionInput, str)


@given(instance=UMLModel::DecisionNode_strategy)
def test_umlmodel::decisionnode_decisionInput_setter(instance):
    original = instance.decisionInput
    instance.decisionInput = original
    assert instance.decisionInput == original

@given(instance=CombinedFragment_strategy)
@settings(max_examples=50)
def test_combinedfragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)

@given(instance=UMLModel::ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_umlmodel::considerignorefragment_instantiation(instance):
    assert isinstance(instance, UMLModel::ConsiderIgnoreFragment)

@given(instance=UMLModel::ConsiderIgnoreFragment_strategy)
def test_umlmodel::considerignorefragment_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=UMLModel::ConsiderIgnoreFragment_strategy)
def test_umlmodel::considerignorefragment_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=UMLModel::DataType_strategy)
@settings(max_examples=50)
def test_umlmodel::datatype_instantiation(instance):
    assert isinstance(instance, UMLModel::DataType)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UMLModel::DataStoreNode_strategy)
@settings(max_examples=50)
def test_umlmodel::datastorenode_instantiation(instance):
    assert isinstance(instance, UMLModel::DataStoreNode)

@given(instance=UMLModel::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_umlmodel::centralbuffernode_instantiation(instance):
    assert isinstance(instance, UMLModel::CentralBufferNode)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=UMLModel::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel::destroylinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel::DestroyLinkAction)

@given(instance=UMLModel::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel::createlinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel::CreateLinkAction)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=UMLModel::Type_strategy)
@settings(max_examples=50)
def test_umlmodel::type_instantiation(instance):
    assert isinstance(instance, UMLModel::Type)

@given(instance=UMLModel::Type_strategy)
def test_umlmodel::type_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=UMLModel::Type_strategy)
def test_umlmodel::type_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=UMLModel::Event_strategy)
@settings(max_examples=50)
def test_umlmodel::event_instantiation(instance):
    assert isinstance(instance, UMLModel::Event)

@given(instance=UMLModel::Observation_strategy)
@settings(max_examples=50)
def test_umlmodel::observation_instantiation(instance):
    assert isinstance(instance, UMLModel::Observation)

@given(instance=UMLModel::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::instancespecification_instantiation(instance):
    assert isinstance(instance, UMLModel::InstanceSpecification)

@given(instance=UMLModel::InstanceSpecification_strategy)
def test_umlmodel::instancespecification_classifier_type(instance):
    assert isinstance(instance.classifier, str)


@given(instance=UMLModel::InstanceSpecification_strategy)
def test_umlmodel::instancespecification_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=UMLModel::GeneralizationSet_strategy)
@settings(max_examples=50)
def test_umlmodel::generalizationset_instantiation(instance):
    assert isinstance(instance, UMLModel::GeneralizationSet)

@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_isDisjoint_type(instance):
    assert isinstance(instance.isDisjoint, str)


@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_generalization_type(instance):
    assert isinstance(instance.generalization, str)


@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_generalization_setter(instance):
    original = instance.generalization
    instance.generalization = original
    assert instance.generalization == original

@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_powerType_type(instance):
    assert isinstance(instance.powerType, str)


@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_powerType_setter(instance):
    original = instance.powerType
    instance.powerType = original
    assert instance.powerType == original

@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_isCovering_type(instance):
    assert isinstance(instance.isCovering, str)


@given(instance=UMLModel::GeneralizationSet_strategy)
def test_umlmodel::generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original

@given(instance=UMLModel::ValueSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::valuespecification_instantiation(instance):
    assert isinstance(instance, UMLModel::ValueSpecification)

@given(instance=UMLModel::InformationFlow_strategy)
@settings(max_examples=50)
def test_umlmodel::informationflow_instantiation(instance):
    assert isinstance(instance, UMLModel::InformationFlow)

@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realizingActivityEdge_type(instance):
    assert isinstance(instance.realizingActivityEdge, str)


@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realizingActivityEdge_setter(instance):
    original = instance.realizingActivityEdge
    instance.realizingActivityEdge = original
    assert instance.realizingActivityEdge == original

@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realizingConnector_type(instance):
    assert isinstance(instance.realizingConnector, str)


@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realizingConnector_setter(instance):
    original = instance.realizingConnector
    instance.realizingConnector = original
    assert instance.realizingConnector == original

@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realization_type(instance):
    assert isinstance(instance.realization, str)


@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realization_setter(instance):
    original = instance.realization
    instance.realization = original
    assert instance.realization == original

@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_informationTarget_type(instance):
    assert isinstance(instance.informationTarget, str)


@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_informationTarget_setter(instance):
    original = instance.informationTarget
    instance.informationTarget = original
    assert instance.informationTarget == original

@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realizingMessage_type(instance):
    assert isinstance(instance.realizingMessage, str)


@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_realizingMessage_setter(instance):
    original = instance.realizingMessage
    instance.realizingMessage = original
    assert instance.realizingMessage == original

@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_informationSource_type(instance):
    assert isinstance(instance.informationSource, str)


@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_informationSource_setter(instance):
    original = instance.informationSource
    instance.informationSource = original
    assert instance.informationSource == original

@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_conveyed_type(instance):
    assert isinstance(instance.conveyed, str)


@given(instance=UMLModel::InformationFlow_strategy)
def test_umlmodel::informationflow_conveyed_setter(instance):
    original = instance.conveyed
    instance.conveyed = original
    assert instance.conveyed == original

@given(instance=UMLModel::Constraint_strategy)
@settings(max_examples=50)
def test_umlmodel::constraint_instantiation(instance):
    assert isinstance(instance, UMLModel::Constraint)

@given(instance=UMLModel::Constraint_strategy)
def test_umlmodel::constraint_constrainedElement_type(instance):
    assert isinstance(instance.constrainedElement, str)


@given(instance=UMLModel::Constraint_strategy)
def test_umlmodel::constraint_constrainedElement_setter(instance):
    original = instance.constrainedElement
    instance.constrainedElement = original
    assert instance.constrainedElement == original

@given(instance=UMLModel::Constraint_strategy)
def test_umlmodel::constraint_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=UMLModel::Constraint_strategy)
def test_umlmodel::constraint_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=UMLModel::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel::createobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel::CreateObjectAction)

@given(instance=UMLModel::CreateObjectAction_strategy)
def test_umlmodel::createobjectaction_classifier_type(instance):
    assert isinstance(instance.classifier, str)


@given(instance=UMLModel::CreateObjectAction_strategy)
def test_umlmodel::createobjectaction_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=UMLModel::CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel::createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel::CreateLinkObjectAction)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=UMLModel::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_umlmodel::expansionregion_instantiation(instance):
    assert isinstance(instance, UMLModel::ExpansionRegion)

@given(instance=UMLModel::ExpansionRegion_strategy)
def test_umlmodel::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=UMLModel::ExpansionRegion_strategy)
def test_umlmodel::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=UMLModel::ExpansionRegion_strategy)
def test_umlmodel::expansionregion_inputElement_type(instance):
    assert isinstance(instance.inputElement, str)


@given(instance=UMLModel::ExpansionRegion_strategy)
def test_umlmodel::expansionregion_inputElement_setter(instance):
    original = instance.inputElement
    instance.inputElement = original
    assert instance.inputElement == original

@given(instance=UMLModel::ExpansionRegion_strategy)
def test_umlmodel::expansionregion_outputElement_type(instance):
    assert isinstance(instance.outputElement, str)


@given(instance=UMLModel::ExpansionRegion_strategy)
def test_umlmodel::expansionregion_outputElement_setter(instance):
    original = instance.outputElement
    instance.outputElement = original
    assert instance.outputElement == original

@given(instance=UMLModel::SequenceNode_strategy)
@settings(max_examples=50)
def test_umlmodel::sequencenode_instantiation(instance):
    assert isinstance(instance, UMLModel::SequenceNode)

@given(instance=UMLModel::LoopNode_strategy)
@settings(max_examples=50)
def test_umlmodel::loopnode_instantiation(instance):
    assert isinstance(instance, UMLModel::LoopNode)

@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_decider_type(instance):
    assert isinstance(instance.decider, str)


@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_decider_setter(instance):
    original = instance.decider
    instance.decider = original
    assert instance.decider == original

@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_bodyOutput_type(instance):
    assert isinstance(instance.bodyOutput, str)


@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_bodyOutput_setter(instance):
    original = instance.bodyOutput
    instance.bodyOutput = original
    assert instance.bodyOutput == original

@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_loopVariable_type(instance):
    assert isinstance(instance.loopVariable, str)


@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_loopVariable_setter(instance):
    original = instance.loopVariable
    instance.loopVariable = original
    assert instance.loopVariable == original

@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_bodyPart_type(instance):
    assert isinstance(instance.bodyPart, str)


@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_bodyPart_setter(instance):
    original = instance.bodyPart
    instance.bodyPart = original
    assert instance.bodyPart == original

@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_setupPart_type(instance):
    assert isinstance(instance.setupPart, str)


@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_setupPart_setter(instance):
    original = instance.setupPart
    instance.setupPart = original
    assert instance.setupPart == original

@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_isTestedFirst_type(instance):
    assert isinstance(instance.isTestedFirst, str)


@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_test_type(instance):
    assert isinstance(instance.test, str)


@given(instance=UMLModel::LoopNode_strategy)
def test_umlmodel::loopnode_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original

@given(instance=UMLModel::ConditionalNode_strategy)
@settings(max_examples=50)
def test_umlmodel::conditionalnode_instantiation(instance):
    assert isinstance(instance, UMLModel::ConditionalNode)

@given(instance=UMLModel::ConditionalNode_strategy)
def test_umlmodel::conditionalnode_isDeterminate_type(instance):
    assert isinstance(instance.isDeterminate, str)


@given(instance=UMLModel::ConditionalNode_strategy)
def test_umlmodel::conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original

@given(instance=UMLModel::ConditionalNode_strategy)
def test_umlmodel::conditionalnode_isAssured_type(instance):
    assert isinstance(instance.isAssured, str)


@given(instance=UMLModel::ConditionalNode_strategy)
def test_umlmodel::conditionalnode_isAssured_setter(instance):
    original = instance.isAssured
    instance.isAssured = original
    assert instance.isAssured == original

@given(instance=UMLModel::Gate_strategy)
@settings(max_examples=50)
def test_umlmodel::gate_instantiation(instance):
    assert isinstance(instance, UMLModel::Gate)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=UMLModel::ObjectNode_strategy)
@settings(max_examples=50)
def test_umlmodel::objectnode_instantiation(instance):
    assert isinstance(instance, UMLModel::ObjectNode)

@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_inState_type(instance):
    assert isinstance(instance.inState, str)


@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_inState_setter(instance):
    original = instance.inState
    instance.inState = original
    assert instance.inState == original

@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_isControlType_type(instance):
    assert isinstance(instance.isControlType, str)


@given(instance=UMLModel::ObjectNode_strategy)
def test_umlmodel::objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=UMLModel::ExecutableNode_strategy)
@settings(max_examples=50)
def test_umlmodel::executablenode_instantiation(instance):
    assert isinstance(instance, UMLModel::ExecutableNode)

@given(instance=UMLModel::ControlNode_strategy)
@settings(max_examples=50)
def test_umlmodel::controlnode_instantiation(instance):
    assert isinstance(instance, UMLModel::ControlNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=UMLModel::ObjectFlow_strategy)
@settings(max_examples=50)
def test_umlmodel::objectflow_instantiation(instance):
    assert isinstance(instance, UMLModel::ObjectFlow)

@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_isMultireceive_type(instance):
    assert isinstance(instance.isMultireceive, str)


@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_transformation_type(instance):
    assert isinstance(instance.transformation, str)


@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_transformation_setter(instance):
    original = instance.transformation
    instance.transformation = original
    assert instance.transformation == original

@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_isMulticast_type(instance):
    assert isinstance(instance.isMulticast, str)


@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=UMLModel::ObjectFlow_strategy)
def test_umlmodel::objectflow_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=UMLModel::ControlFlow_strategy)
@settings(max_examples=50)
def test_umlmodel::controlflow_instantiation(instance):
    assert isinstance(instance, UMLModel::ControlFlow)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=UMLModel::Pseudostate_strategy)
@settings(max_examples=50)
def test_umlmodel::pseudostate_instantiation(instance):
    assert isinstance(instance, UMLModel::Pseudostate)

@given(instance=UMLModel::Pseudostate_strategy)
def test_umlmodel::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UMLModel::Pseudostate_strategy)
def test_umlmodel::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UMLModel::Pseudostate_strategy)
def test_umlmodel::pseudostate_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=UMLModel::Pseudostate_strategy)
def test_umlmodel::pseudostate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=UMLModel::Pseudostate_strategy)
def test_umlmodel::pseudostate_stateMachine_type(instance):
    assert isinstance(instance.stateMachine, str)


@given(instance=UMLModel::Pseudostate_strategy)
def test_umlmodel::pseudostate_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original

@given(instance=UMLModel::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_umlmodel::connectionpointreference_instantiation(instance):
    assert isinstance(instance, UMLModel::ConnectionPointReference)

@given(instance=UMLModel::ConnectionPointReference_strategy)
def test_umlmodel::connectionpointreference_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=UMLModel::ConnectionPointReference_strategy)
def test_umlmodel::connectionpointreference_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=UMLModel::ConnectionPointReference_strategy)
def test_umlmodel::connectionpointreference_entry_type(instance):
    assert isinstance(instance.entry, str)


@given(instance=UMLModel::ConnectionPointReference_strategy)
def test_umlmodel::connectionpointreference_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=UMLModel::ConnectionPointReference_strategy)
def test_umlmodel::connectionpointreference_exit_type(instance):
    assert isinstance(instance.exit, str)


@given(instance=UMLModel::ConnectionPointReference_strategy)
def test_umlmodel::connectionpointreference_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original

@given(instance=UMLModel::Comment_strategy)
@settings(max_examples=50)
def test_umlmodel::comment_instantiation(instance):
    assert isinstance(instance, UMLModel::Comment)

@given(instance=UMLModel::Comment_strategy)
def test_umlmodel::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UMLModel::Comment_strategy)
def test_umlmodel::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UMLModel::Comment_strategy)
def test_umlmodel::comment_annotatedElement_type(instance):
    assert isinstance(instance.annotatedElement, str)


@given(instance=UMLModel::Comment_strategy)
def test_umlmodel::comment_annotatedElement_setter(instance):
    original = instance.annotatedElement
    instance.annotatedElement = original
    assert instance.annotatedElement == original

@given(instance=UMLModel::Dependency_strategy)
@settings(max_examples=50)
def test_umlmodel::dependency_instantiation(instance):
    assert isinstance(instance, UMLModel::Dependency)

@given(instance=UMLModel::Dependency_strategy)
def test_umlmodel::dependency_client_type(instance):
    assert isinstance(instance.client, str)


@given(instance=UMLModel::Dependency_strategy)
def test_umlmodel::dependency_client_setter(instance):
    original = instance.client
    instance.client = original
    assert instance.client == original

@given(instance=UMLModel::Dependency_strategy)
def test_umlmodel::dependency_supplier_type(instance):
    assert isinstance(instance.supplier, str)


@given(instance=UMLModel::Dependency_strategy)
def test_umlmodel::dependency_supplier_setter(instance):
    original = instance.supplier
    instance.supplier = original
    assert instance.supplier == original

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UMLModel::EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_umlmodel::encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UMLModel::EncapsulatedClassifier)

@given(instance=UMLModel::EncapsulatedClassifier_strategy)
def test_umlmodel::encapsulatedclassifier_ownedPort_type(instance):
    assert isinstance(instance.ownedPort, str)


@given(instance=UMLModel::EncapsulatedClassifier_strategy)
def test_umlmodel::encapsulatedclassifier_ownedPort_setter(instance):
    original = instance.ownedPort
    instance.ownedPort = original
    assert instance.ownedPort == original

@given(instance=UMLModel::Collaboration_strategy)
@settings(max_examples=50)
def test_umlmodel::collaboration_instantiation(instance):
    assert isinstance(instance, UMLModel::Collaboration)

@given(instance=UMLModel::Collaboration_strategy)
def test_umlmodel::collaboration_collaborationRole_type(instance):
    assert isinstance(instance.collaborationRole, str)


@given(instance=UMLModel::Collaboration_strategy)
def test_umlmodel::collaboration_collaborationRole_setter(instance):
    original = instance.collaborationRole
    instance.collaborationRole = original
    assert instance.collaborationRole == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UMLModel::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadStructuralFeatureAction)

@given(instance=UMLModel::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel::WriteStructuralFeatureAction)

@given(instance=UMLModel::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ClearStructuralFeatureAction)

@given(instance=UMLModel::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_umlmodel::clearassociationaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ClearAssociationAction)

@given(instance=UMLModel::ClearAssociationAction_strategy)
def test_umlmodel::clearassociationaction_association_type(instance):
    assert isinstance(instance.association, str)


@given(instance=UMLModel::ClearAssociationAction_strategy)
def test_umlmodel::clearassociationaction_association_setter(instance):
    original = instance.association
    instance.association = original
    assert instance.association == original

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=UMLModel::ReadVariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel::readvariableaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ReadVariableAction)

@given(instance=UMLModel::WriteVariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel::writevariableaction_instantiation(instance):
    assert isinstance(instance, UMLModel::WriteVariableAction)

@given(instance=UMLModel::ClearVariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel::clearvariableaction_instantiation(instance):
    assert isinstance(instance, UMLModel::ClearVariableAction)

@given(instance=UMLModel::Clause_strategy)
@settings(max_examples=50)
def test_umlmodel::clause_instantiation(instance):
    assert isinstance(instance, UMLModel::Clause)

@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_bodyOutput_type(instance):
    assert isinstance(instance.bodyOutput, str)


@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_bodyOutput_setter(instance):
    original = instance.bodyOutput
    instance.bodyOutput = original
    assert instance.bodyOutput == original

@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_predecessorClause_type(instance):
    assert isinstance(instance.predecessorClause, str)


@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_predecessorClause_setter(instance):
    original = instance.predecessorClause
    instance.predecessorClause = original
    assert instance.predecessorClause == original

@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_test_type(instance):
    assert isinstance(instance.test, str)


@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original

@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_decider_type(instance):
    assert isinstance(instance.decider, str)


@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_decider_setter(instance):
    original = instance.decider
    instance.decider = original
    assert instance.decider == original

@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_successorClause_type(instance):
    assert isinstance(instance.successorClause, str)


@given(instance=UMLModel::Clause_strategy)
def test_umlmodel::clause_successorClause_setter(instance):
    original = instance.successorClause
    instance.successorClause = original
    assert instance.successorClause == original

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=UMLModel::StateInvariant_strategy)
@settings(max_examples=50)
def test_umlmodel::stateinvariant_instantiation(instance):
    assert isinstance(instance, UMLModel::StateInvariant)

@given(instance=UMLModel::OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::occurrencespecification_instantiation(instance):
    assert isinstance(instance, UMLModel::OccurrenceSpecification)

@given(instance=UMLModel::OccurrenceSpecification_strategy)
def test_umlmodel::occurrencespecification_toAfter_type(instance):
    assert isinstance(instance.toAfter, str)


@given(instance=UMLModel::OccurrenceSpecification_strategy)
def test_umlmodel::occurrencespecification_toAfter_setter(instance):
    original = instance.toAfter
    instance.toAfter = original
    assert instance.toAfter == original

@given(instance=UMLModel::OccurrenceSpecification_strategy)
def test_umlmodel::occurrencespecification_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=UMLModel::OccurrenceSpecification_strategy)
def test_umlmodel::occurrencespecification_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=UMLModel::OccurrenceSpecification_strategy)
def test_umlmodel::occurrencespecification_toBefore_type(instance):
    assert isinstance(instance.toBefore, str)


@given(instance=UMLModel::OccurrenceSpecification_strategy)
def test_umlmodel::occurrencespecification_toBefore_setter(instance):
    original = instance.toBefore
    instance.toBefore = original
    assert instance.toBefore == original

@given(instance=UMLModel::InteractionUse_strategy)
@settings(max_examples=50)
def test_umlmodel::interactionuse_instantiation(instance):
    assert isinstance(instance, UMLModel::InteractionUse)

@given(instance=UMLModel::InteractionUse_strategy)
def test_umlmodel::interactionuse_refersTo_type(instance):
    assert isinstance(instance.refersTo, str)


@given(instance=UMLModel::InteractionUse_strategy)
def test_umlmodel::interactionuse_refersTo_setter(instance):
    original = instance.refersTo
    instance.refersTo = original
    assert instance.refersTo == original

@given(instance=UMLModel::Interaction_strategy)
@settings(max_examples=50)
def test_umlmodel::interaction_instantiation(instance):
    assert isinstance(instance, UMLModel::Interaction)

@given(instance=UMLModel::Continuation_strategy)
@settings(max_examples=50)
def test_umlmodel::continuation_instantiation(instance):
    assert isinstance(instance, UMLModel::Continuation)

@given(instance=UMLModel::Continuation_strategy)
def test_umlmodel::continuation_setting_type(instance):
    assert isinstance(instance.setting, str)


@given(instance=UMLModel::Continuation_strategy)
def test_umlmodel::continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=UMLModel::ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::executionspecification_instantiation(instance):
    assert isinstance(instance, UMLModel::ExecutionSpecification)

@given(instance=UMLModel::ExecutionSpecification_strategy)
def test_umlmodel::executionspecification_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=UMLModel::ExecutionSpecification_strategy)
def test_umlmodel::executionspecification_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=UMLModel::ExecutionSpecification_strategy)
def test_umlmodel::executionspecification_finish_type(instance):
    assert isinstance(instance.finish, str)


@given(instance=UMLModel::ExecutionSpecification_strategy)
def test_umlmodel::executionspecification_finish_setter(instance):
    original = instance.finish
    instance.finish = original
    assert instance.finish == original

@given(instance=UMLModel::CombinedFragment_strategy)
@settings(max_examples=50)
def test_umlmodel::combinedfragment_instantiation(instance):
    assert isinstance(instance, UMLModel::CombinedFragment)

@given(instance=UMLModel::CombinedFragment_strategy)
def test_umlmodel::combinedfragment_interactionOperator_type(instance):
    assert isinstance(instance.interactionOperator, str)


@given(instance=UMLModel::CombinedFragment_strategy)
def test_umlmodel::combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=UMLModel::ComponentRealization_strategy)
@settings(max_examples=50)
def test_umlmodel::componentrealization_instantiation(instance):
    assert isinstance(instance, UMLModel::ComponentRealization)

@given(instance=UMLModel::ComponentRealization_strategy)
def test_umlmodel::componentrealization_realizingClassifier_type(instance):
    assert isinstance(instance.realizingClassifier, str)


@given(instance=UMLModel::ComponentRealization_strategy)
def test_umlmodel::componentrealization_realizingClassifier_setter(instance):
    original = instance.realizingClassifier
    instance.realizingClassifier = original
    assert instance.realizingClassifier == original

@given(instance=UMLModel::ComponentRealization_strategy)
def test_umlmodel::componentrealization_abstraction_type(instance):
    assert isinstance(instance.abstraction, str)


@given(instance=UMLModel::ComponentRealization_strategy)
def test_umlmodel::componentrealization_abstraction_setter(instance):
    original = instance.abstraction
    instance.abstraction = original
    assert instance.abstraction == original

@given(instance=UMLModel::PackageableElement_strategy)
@settings(max_examples=50)
def test_umlmodel::packageableelement_instantiation(instance):
    assert isinstance(instance, UMLModel::PackageableElement)

@given(instance=UMLModel::Component_strategy)
@settings(max_examples=50)
def test_umlmodel::component_instantiation(instance):
    assert isinstance(instance, UMLModel::Component)

@given(instance=UMLModel::Component_strategy)
def test_umlmodel::component_provided_type(instance):
    assert isinstance(instance.provided, str)


@given(instance=UMLModel::Component_strategy)
def test_umlmodel::component_provided_setter(instance):
    original = instance.provided
    instance.provided = original
    assert instance.provided == original

@given(instance=UMLModel::Component_strategy)
def test_umlmodel::component_indirectlyInstantiated_type(instance):
    assert isinstance(instance.indirectlyInstantiated, str)


@given(instance=UMLModel::Component_strategy)
def test_umlmodel::component_indirectlyInstantiated_setter(instance):
    original = instance.indirectlyInstantiated
    instance.indirectlyInstantiated = original
    assert instance.indirectlyInstantiated == original

@given(instance=UMLModel::Component_strategy)
def test_umlmodel::component_required_type(instance):
    assert isinstance(instance.required, str)


@given(instance=UMLModel::Component_strategy)
def test_umlmodel::component_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=UMLModel::CommunicationPath_strategy)
@settings(max_examples=50)
def test_umlmodel::communicationpath_instantiation(instance):
    assert isinstance(instance, UMLModel::CommunicationPath)

@given(instance=UMLModel::Generalization_strategy)
@settings(max_examples=50)
def test_umlmodel::generalization_instantiation(instance):
    assert isinstance(instance, UMLModel::Generalization)

@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_generalizationSet_type(instance):
    assert isinstance(instance.generalizationSet, str)


@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_generalizationSet_setter(instance):
    original = instance.generalizationSet
    instance.generalizationSet = original
    assert instance.generalizationSet == original

@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, str)


@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_specific_type(instance):
    assert isinstance(instance.specific, str)


@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_specific_setter(instance):
    original = instance.specific
    instance.specific = original
    assert instance.specific == original

@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_general_type(instance):
    assert isinstance(instance.general, str)


@given(instance=UMLModel::Generalization_strategy)
def test_umlmodel::generalization_general_setter(instance):
    original = instance.general
    instance.general = original
    assert instance.general == original

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=UMLModel::Property_strategy)
@settings(max_examples=50)
def test_umlmodel::property_instantiation(instance):
    assert isinstance(instance, UMLModel::Property)

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_redefinedProperty_type(instance):
    assert isinstance(instance.redefinedProperty, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_redefinedProperty_setter(instance):
    original = instance.redefinedProperty
    instance.redefinedProperty = original
    assert instance.redefinedProperty == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_opposite_type(instance):
    assert isinstance(instance.opposite, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_opposite_setter(instance):
    original = instance.opposite
    instance.opposite = original
    assert instance.opposite == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_association_type(instance):
    assert isinstance(instance.association, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_association_setter(instance):
    original = instance.association
    instance.association = original
    assert instance.association == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_isDerivedUnion_type(instance):
    assert isinstance(instance.isDerivedUnion, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_owningAssociation_type(instance):
    assert isinstance(instance.owningAssociation, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_owningAssociation_setter(instance):
    original = instance.owningAssociation
    instance.owningAssociation = original
    assert instance.owningAssociation == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_associationEnd_type(instance):
    assert isinstance(instance.associationEnd, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_associationEnd_setter(instance):
    original = instance.associationEnd
    instance.associationEnd = original
    assert instance.associationEnd == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_datatype_type(instance):
    assert isinstance(instance.datatype, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_datatype_setter(instance):
    original = instance.datatype
    instance.datatype = original
    assert instance.datatype == original

@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_subsettedProperty_type(instance):
    assert isinstance(instance.subsettedProperty, str)


@given(instance=UMLModel::Property_strategy)
def test_umlmodel::property_subsettedProperty_setter(instance):
    original = instance.subsettedProperty
    instance.subsettedProperty = original
    assert instance.subsettedProperty == original

@given(instance=UMLModel::Operation_strategy)
@settings(max_examples=50)
def test_umlmodel::operation_instantiation(instance):
    assert isinstance(instance, UMLModel::Operation)

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_bodyCondition_type(instance):
    assert isinstance(instance.bodyCondition, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_bodyCondition_setter(instance):
    original = instance.bodyCondition
    instance.bodyCondition = original
    assert instance.bodyCondition == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_datatype_type(instance):
    assert isinstance(instance.datatype, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_datatype_setter(instance):
    original = instance.datatype
    instance.datatype = original
    assert instance.datatype == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_interface_type(instance):
    assert isinstance(instance.interface, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_redefinedOperation_type(instance):
    assert isinstance(instance.redefinedOperation, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_redefinedOperation_setter(instance):
    original = instance.redefinedOperation
    instance.redefinedOperation = original
    assert instance.redefinedOperation == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=UMLModel::Operation_strategy)
def test_umlmodel::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=UMLModel::StringExpression_strategy)
@settings(max_examples=50)
def test_umlmodel::stringexpression_instantiation(instance):
    assert isinstance(instance, UMLModel::StringExpression)

@given(instance=UMLModel::StringExpression_strategy)
def test_umlmodel::stringexpression_owningExpression_type(instance):
    assert isinstance(instance.owningExpression, str)


@given(instance=UMLModel::StringExpression_strategy)
def test_umlmodel::stringexpression_owningExpression_setter(instance):
    original = instance.owningExpression
    instance.owningExpression = original
    assert instance.owningExpression == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=UMLModel::Reception_strategy)
@settings(max_examples=50)
def test_umlmodel::reception_instantiation(instance):
    assert isinstance(instance, UMLModel::Reception)

@given(instance=UMLModel::Reception_strategy)
def test_umlmodel::reception_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=UMLModel::Reception_strategy)
def test_umlmodel::reception_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=UMLModel::Class_strategy)
@settings(max_examples=50)
def test_umlmodel::class_instantiation(instance):
    assert isinstance(instance, UMLModel::Class)

@given(instance=UMLModel::Class_strategy)
def test_umlmodel::class_isActive_type(instance):
    assert isinstance(instance.isActive, str)


@given(instance=UMLModel::Class_strategy)
def test_umlmodel::class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=UMLModel::Class_strategy)
def test_umlmodel::class_superclass_type(instance):
    assert isinstance(instance.superclass, str)


@given(instance=UMLModel::Class_strategy)
def test_umlmodel::class_superclass_setter(instance):
    original = instance.superclass
    instance.superclass = original
    assert instance.superclass == original

@given(instance=UMLModel::Class_strategy)
def test_umlmodel::class_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=UMLModel::Class_strategy)
def test_umlmodel::class_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=UMLModel::ExecutionEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::executionevent_instantiation(instance):
    assert isinstance(instance, UMLModel::ExecutionEvent)

@given(instance=UMLModel::DestructionEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::destructionevent_instantiation(instance):
    assert isinstance(instance, UMLModel::DestructionEvent)

@given(instance=UMLModel::MessageEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::messageevent_instantiation(instance):
    assert isinstance(instance, UMLModel::MessageEvent)

@given(instance=UMLModel::TimeEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::timeevent_instantiation(instance):
    assert isinstance(instance, UMLModel::TimeEvent)

@given(instance=UMLModel::TimeEvent_strategy)
def test_umlmodel::timeevent_isRelative_type(instance):
    assert isinstance(instance.isRelative, str)


@given(instance=UMLModel::TimeEvent_strategy)
def test_umlmodel::timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=UMLModel::CreationEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::creationevent_instantiation(instance):
    assert isinstance(instance, UMLModel::CreationEvent)

@given(instance=UMLModel::ChangeEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::changeevent_instantiation(instance):
    assert isinstance(instance, UMLModel::ChangeEvent)

@given(instance=UMLModel::CallOperationAction_strategy)
@settings(max_examples=50)
def test_umlmodel::calloperationaction_instantiation(instance):
    assert isinstance(instance, UMLModel::CallOperationAction)

@given(instance=UMLModel::CallOperationAction_strategy)
def test_umlmodel::calloperationaction_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=UMLModel::CallOperationAction_strategy)
def test_umlmodel::calloperationaction_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=UMLModel::ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel::connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel::ConnectableElementTemplateParameter)

@given(instance=UMLModel::OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel::operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel::OperationTemplateParameter)

@given(instance=UMLModel::ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel::classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel::ClassifierTemplateParameter)

@given(instance=UMLModel::ClassifierTemplateParameter_strategy)
def test_umlmodel::classifiertemplateparameter_allowSubstitutable_type(instance):
    assert isinstance(instance.allowSubstitutable, str)


@given(instance=UMLModel::ClassifierTemplateParameter_strategy)
def test_umlmodel::classifiertemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=UMLModel::ClassifierTemplateParameter_strategy)
def test_umlmodel::classifiertemplateparameter_defaultClassifier_type(instance):
    assert isinstance(instance.defaultClassifier, str)


@given(instance=UMLModel::ClassifierTemplateParameter_strategy)
def test_umlmodel::classifiertemplateparameter_defaultClassifier_setter(instance):
    original = instance.defaultClassifier
    instance.defaultClassifier = original
    assert instance.defaultClassifier == original

@given(instance=UMLModel::ClassifierTemplateParameter_strategy)
def test_umlmodel::classifiertemplateparameter_constrainingClassifier_type(instance):
    assert isinstance(instance.constrainingClassifier, str)


@given(instance=UMLModel::ClassifierTemplateParameter_strategy)
def test_umlmodel::classifiertemplateparameter_constrainingClassifier_setter(instance):
    original = instance.constrainingClassifier
    instance.constrainingClassifier = original
    assert instance.constrainingClassifier == original

@given(instance=UMLModel::UseCase_strategy)
@settings(max_examples=50)
def test_umlmodel::usecase_instantiation(instance):
    assert isinstance(instance, UMLModel::UseCase)

@given(instance=UMLModel::UseCase_strategy)
def test_umlmodel::usecase_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=UMLModel::UseCase_strategy)
def test_umlmodel::usecase_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=UMLModel::CollaborationUse_strategy)
@settings(max_examples=50)
def test_umlmodel::collaborationuse_instantiation(instance):
    assert isinstance(instance, UMLModel::CollaborationUse)

@given(instance=UMLModel::CollaborationUse_strategy)
def test_umlmodel::collaborationuse_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=UMLModel::CollaborationUse_strategy)
def test_umlmodel::collaborationuse_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UMLModel::Substitution_strategy)
@settings(max_examples=50)
def test_umlmodel::substitution_instantiation(instance):
    assert isinstance(instance, UMLModel::Substitution)

@given(instance=UMLModel::Substitution_strategy)
def test_umlmodel::substitution_contract_type(instance):
    assert isinstance(instance.contract, str)


@given(instance=UMLModel::Substitution_strategy)
def test_umlmodel::substitution_contract_setter(instance):
    original = instance.contract
    instance.contract = original
    assert instance.contract == original

@given(instance=UMLModel::Substitution_strategy)
def test_umlmodel::substitution_substitutingClassifier_type(instance):
    assert isinstance(instance.substitutingClassifier, str)


@given(instance=UMLModel::Substitution_strategy)
def test_umlmodel::substitution_substitutingClassifier_setter(instance):
    original = instance.substitutingClassifier
    instance.substitutingClassifier = original
    assert instance.substitutingClassifier == original

@given(instance=UMLModel::InterfaceRealization_strategy)
@settings(max_examples=50)
def test_umlmodel::interfacerealization_instantiation(instance):
    assert isinstance(instance, UMLModel::InterfaceRealization)

@given(instance=UMLModel::InterfaceRealization_strategy)
def test_umlmodel::interfacerealization_realizingClassifier_type(instance):
    assert isinstance(instance.realizingClassifier, str)


@given(instance=UMLModel::InterfaceRealization_strategy)
def test_umlmodel::interfacerealization_realizingClassifier_setter(instance):
    original = instance.realizingClassifier
    instance.realizingClassifier = original
    assert instance.realizingClassifier == original

@given(instance=UMLModel::InterfaceRealization_strategy)
def test_umlmodel::interfacerealization_contract_type(instance):
    assert isinstance(instance.contract, str)


@given(instance=UMLModel::InterfaceRealization_strategy)
def test_umlmodel::interfacerealization_contract_setter(instance):
    original = instance.contract
    instance.contract = original
    assert instance.contract == original

@given(instance=UMLModel::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_umlmodel::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UMLModel::BehavioredClassifier)

@given(instance=UMLModel::BehavioredClassifier_strategy)
def test_umlmodel::behavioredclassifier_classifierBehavior_type(instance):
    assert isinstance(instance.classifierBehavior, str)


@given(instance=UMLModel::BehavioredClassifier_strategy)
def test_umlmodel::behavioredclassifier_classifierBehavior_setter(instance):
    original = instance.classifierBehavior
    instance.classifierBehavior = original
    assert instance.classifierBehavior == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=UMLModel::Connector_strategy)
@settings(max_examples=50)
def test_umlmodel::connector_instantiation(instance):
    assert isinstance(instance, UMLModel::Connector)

@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_redefinedConnector_type(instance):
    assert isinstance(instance.redefinedConnector, str)


@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_redefinedConnector_setter(instance):
    original = instance.redefinedConnector
    instance.redefinedConnector = original
    assert instance.redefinedConnector == original

@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_contract_type(instance):
    assert isinstance(instance.contract, str)


@given(instance=UMLModel::Connector_strategy)
def test_umlmodel::connector_contract_setter(instance):
    original = instance.contract
    instance.contract = original
    assert instance.contract == original

@given(instance=UMLModel::StructuralFeature_strategy)
@settings(max_examples=50)
def test_umlmodel::structuralfeature_instantiation(instance):
    assert isinstance(instance, UMLModel::StructuralFeature)

@given(instance=UMLModel::StructuralFeature_strategy)
def test_umlmodel::structuralfeature_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=UMLModel::StructuralFeature_strategy)
def test_umlmodel::structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=UMLModel::InteractionOperand_strategy)
@settings(max_examples=50)
def test_umlmodel::interactionoperand_instantiation(instance):
    assert isinstance(instance, UMLModel::InteractionOperand)

@given(instance=UMLModel::Transition_strategy)
@settings(max_examples=50)
def test_umlmodel::transition_instantiation(instance):
    assert isinstance(instance, UMLModel::Transition)

@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_redefinedTransition_type(instance):
    assert isinstance(instance.redefinedTransition, str)


@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_redefinedTransition_setter(instance):
    original = instance.redefinedTransition
    instance.redefinedTransition = original
    assert instance.redefinedTransition == original

@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_container_type(instance):
    assert isinstance(instance.container, str)


@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=UMLModel::Transition_strategy)
def test_umlmodel::transition_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=UMLModel::Classifier_strategy)
@settings(max_examples=50)
def test_umlmodel::classifier_instantiation(instance):
    assert isinstance(instance, UMLModel::Classifier)

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_redefinedClassifier_type(instance):
    assert isinstance(instance.redefinedClassifier, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_redefinedClassifier_setter(instance):
    original = instance.redefinedClassifier
    instance.redefinedClassifier = original
    assert instance.redefinedClassifier == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_general_type(instance):
    assert isinstance(instance.general, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_general_setter(instance):
    original = instance.general
    instance.general = original
    assert instance.general == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_inheritedMember_type(instance):
    assert isinstance(instance.inheritedMember, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_inheritedMember_setter(instance):
    original = instance.inheritedMember
    instance.inheritedMember = original
    assert instance.inheritedMember == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_representation_type(instance):
    assert isinstance(instance.representation, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_representation_setter(instance):
    original = instance.representation
    instance.representation = original
    assert instance.representation == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_useCase_type(instance):
    assert isinstance(instance.useCase, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_useCase_setter(instance):
    original = instance.useCase
    instance.useCase = original
    assert instance.useCase == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_powertypeExtent_type(instance):
    assert isinstance(instance.powertypeExtent, str)


@given(instance=UMLModel::Classifier_strategy)
def test_umlmodel::classifier_powertypeExtent_setter(instance):
    original = instance.powertypeExtent
    instance.powertypeExtent = original
    assert instance.powertypeExtent == original

@given(instance=UMLModel::Package_strategy)
@settings(max_examples=50)
def test_umlmodel::package_instantiation(instance):
    assert isinstance(instance, UMLModel::Package)

@given(instance=UMLModel::Package_strategy)
def test_umlmodel::package_nestedPackage_type(instance):
    assert isinstance(instance.nestedPackage, str)


@given(instance=UMLModel::Package_strategy)
def test_umlmodel::package_nestedPackage_setter(instance):
    original = instance.nestedPackage
    instance.nestedPackage = original
    assert instance.nestedPackage == original

@given(instance=UMLModel::Package_strategy)
def test_umlmodel::package_nestingPackage_type(instance):
    assert isinstance(instance.nestingPackage, str)


@given(instance=UMLModel::Package_strategy)
def test_umlmodel::package_nestingPackage_setter(instance):
    original = instance.nestingPackage
    instance.nestingPackage = original
    assert instance.nestingPackage == original

@given(instance=UMLModel::Package_strategy)
def test_umlmodel::package_ownedType_type(instance):
    assert isinstance(instance.ownedType, str)


@given(instance=UMLModel::Package_strategy)
def test_umlmodel::package_ownedType_setter(instance):
    original = instance.ownedType
    instance.ownedType = original
    assert instance.ownedType == original

@given(instance=UMLModel::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_umlmodel::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UMLModel::StructuredActivityNode)

@given(instance=UMLModel::StructuredActivityNode_strategy)
def test_umlmodel::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, str)


@given(instance=UMLModel::StructuredActivityNode_strategy)
def test_umlmodel::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=UMLModel::Region_strategy)
@settings(max_examples=50)
def test_umlmodel::region_instantiation(instance):
    assert isinstance(instance, UMLModel::Region)

@given(instance=UMLModel::Region_strategy)
def test_umlmodel::region_extendedRegion_type(instance):
    assert isinstance(instance.extendedRegion, str)


@given(instance=UMLModel::Region_strategy)
def test_umlmodel::region_extendedRegion_setter(instance):
    original = instance.extendedRegion
    instance.extendedRegion = original
    assert instance.extendedRegion == original

@given(instance=UMLModel::Region_strategy)
def test_umlmodel::region_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=UMLModel::Region_strategy)
def test_umlmodel::region_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=UMLModel::Region_strategy)
def test_umlmodel::region_stateMachine_type(instance):
    assert isinstance(instance.stateMachine, str)


@given(instance=UMLModel::Region_strategy)
def test_umlmodel::region_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original

@given(instance=UMLModel::State_strategy)
@settings(max_examples=50)
def test_umlmodel::state_instantiation(instance):
    assert isinstance(instance, UMLModel::State)

@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_redefinedState_type(instance):
    assert isinstance(instance.redefinedState, str)


@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_redefinedState_setter(instance):
    original = instance.redefinedState
    instance.redefinedState = original
    assert instance.redefinedState == original

@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, str)


@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_submachine_type(instance):
    assert isinstance(instance.submachine, str)


@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_submachine_setter(instance):
    original = instance.submachine
    instance.submachine = original
    assert instance.submachine == original

@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, str)


@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, str)


@given(instance=UMLModel::State_strategy)
def test_umlmodel::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=UMLModel::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_umlmodel::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UMLModel::BehavioralFeature)

@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_concurrency_type(instance):
    assert isinstance(instance.concurrency, str)


@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_raisedException_type(instance):
    assert isinstance(instance.raisedException, str)


@given(instance=UMLModel::BehavioralFeature_strategy)
def test_umlmodel::behavioralfeature_raisedException_setter(instance):
    original = instance.raisedException
    instance.raisedException = original
    assert instance.raisedException == original

@given(instance=UMLModel::BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel::behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, UMLModel::BehaviorExecutionSpecification)

@given(instance=UMLModel::BehaviorExecutionSpecification_strategy)
def test_umlmodel::behaviorexecutionspecification_behavior_type(instance):
    assert isinstance(instance.behavior, str)


@given(instance=UMLModel::BehaviorExecutionSpecification_strategy)
def test_umlmodel::behaviorexecutionspecification_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=UMLModel::ParameterSet_strategy)
@settings(max_examples=50)
def test_umlmodel::parameterset_instantiation(instance):
    assert isinstance(instance, UMLModel::ParameterSet)

@given(instance=UMLModel::ParameterSet_strategy)
def test_umlmodel::parameterset_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=UMLModel::ParameterSet_strategy)
def test_umlmodel::parameterset_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=UMLModel::Parameter_strategy)
@settings(max_examples=50)
def test_umlmodel::parameter_instantiation(instance):
    assert isinstance(instance, UMLModel::Parameter)

@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_isException_type(instance):
    assert isinstance(instance.isException, str)


@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original

@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_isStream_type(instance):
    assert isinstance(instance.isStream, str)


@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original

@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_parameterSet_type(instance):
    assert isinstance(instance.parameterSet, str)


@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_parameterSet_setter(instance):
    original = instance.parameterSet
    instance.parameterSet = original
    assert instance.parameterSet == original

@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=UMLModel::Parameter_strategy)
def test_umlmodel::parameter_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=UMLModel::CallEvent_strategy)
@settings(max_examples=50)
def test_umlmodel::callevent_instantiation(instance):
    assert isinstance(instance, UMLModel::CallEvent)

@given(instance=UMLModel::CallEvent_strategy)
def test_umlmodel::callevent_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=UMLModel::CallEvent_strategy)
def test_umlmodel::callevent_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=UMLModel::Behavior_strategy)
@settings(max_examples=50)
def test_umlmodel::behavior_instantiation(instance):
    assert isinstance(instance, UMLModel::Behavior)

@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_isReentrant_type(instance):
    assert isinstance(instance.isReentrant, str)


@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_redefinedBahavior_type(instance):
    assert isinstance(instance.redefinedBahavior, str)


@given(instance=UMLModel::Behavior_strategy)
def test_umlmodel::behavior_redefinedBahavior_setter(instance):
    original = instance.redefinedBahavior
    instance.redefinedBahavior = original
    assert instance.redefinedBahavior == original

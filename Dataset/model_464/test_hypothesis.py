import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fUML::LociL1::SemanticVisitor,
    SemanticVisitor,
    fUML::Kernel::Value,
    Kernel::FeatureValue,
    CompoundValue,
    fUML::Kernel::DataValue,
    fUML::Kernel::ExtensionalValue,
    ExtensionalValue,
    fUML::Kernel::Link,
    fUML::Kernel::Object,
    Kernel::Object,
    StructuredValue,
    fUML::Kernel::CompoundValue,
    fUML::Kernel::Reference,
    Kernel::PrimitiveType,
    PrimitiveValue,
    fUML::Kernel::BooleanValue,
    fUML::Kernel::IntegerValue,
    fUML::Kernel::UnlimitedNaturalValue,
    Kernel::Value,
    fUML::Kernel::FeatureValue,
    Value,
    fUML::Kernel::EnumerationValue,
    fUML::Kernel::PrimitiveValue,
    fUML::Kernel::StructuredValue,
    fUML::Kernel::StringValue,
    InvocationAction,
    fUML::BasicActions::SendSignalAction,
    fUML::BasicActions::CallAction,
    IntermediateActivities::ObjectNode,
    Pin,
    fUML::BasicActions::OutputPin,
    fUML::BasicActions::InputPin,
    ExecutableNode,
    fUML::BasicActions::Action,
    Communications::Trigger,
    CallAction,
    fUML::BasicActions::CallBehaviorAction,
    fUML::BasicActions::CallOperationAction,
    fUML::CompleteActions::StartObjectBehaviorAction,
    WriteLinkAction,
    fUML::IntermediateActions::DestroyLinkAction,
    fUML::IntermediateActions::CreateLinkAction,
    LinkEndData,
    fUML::IntermediateActions::LinkEndDestructionData,
    fUML::IntermediateActions::LinkEndCreationData,
    WriteStructuralFeatureAction,
    fUML::IntermediateActions::AddStructuralFeatureValueAction,
    fUML::IntermediateActions::RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    fUML::IntermediateActions::ClearStructuralFeatureAction,
    fUML::IntermediateActions::ReadStructuralFeatureAction,
    fUML::IntermediateActions::WriteStructuralFeatureAction,
    IntermediateActions::LinkEndData,
    ExtraStructuredActivities::ExpansionNode,
    LinkAction,
    fUML::IntermediateActions::ReadLinkAction,
    fUML::IntermediateActions::WriteLinkAction,
    ExtraStructuredActivities::ExpansionRegion,
    Action,
    fUML::IntermediateActions::ClearAssociationAction,
    fUML::BasicActions::InvocationAction,
    fUML::IntermediateActions::ValueSpecificationAction,
    fUML::IntermediateActions::CreateObjectAction,
    fUML::CompleteActions::AcceptEventAction,
    fUML::IntermediateActions::TestIdentityAction,
    fUML::CompleteActions::ReclassifyObjectAction,
    fUML::IntermediateActions::StructuralFeatureAction,
    fUML::CompleteActions::ReduceAction,
    fUML::IntermediateActions::ReadSelfAction,
    fUML::CompleteActions::StartClassifierBehaviorAction,
    fUML::CompleteActions::ReadIsClassifiedObjectAction,
    fUML::IntermediateActions::DestroyObjectAction,
    fUML::CompleteActions::ReadExtentAction,
    fUML::IntermediateActions::LinkAction,
    fUML::CompleteStructuredActivities::StructuredActivityNode,
    BasicActions::InputPin,
    CompleteStructuredActivities::ExecutableNode,
    BasicActions::OutputPin,
    StructuredActivityNode,
    fUML::ExtraStructuredActivities::ExpansionRegion,
    fUML::CompleteStructuredActivities::ConditionalNode,
    fUML::CompleteStructuredActivities::LoopNode,
    ObjectNode,
    fUML::ExtraStructuredActivities::ExpansionNode,
    fUML::IntermediateActivities::ActivityParameterNode,
    CompleteStructuredActivities::Clause,
    ActivityNode,
    fUML::CompleteStructuredActivities::ExecutableNode,
    fUML::IntermediateActivities::ControlNode,
    ControlNode,
    fUML::IntermediateActivities::ForkNode,
    fUML::IntermediateActivities::InitialNode,
    fUML::IntermediateActivities::JoinNode,
    fUML::IntermediateActivities::FinalNode,
    fUML::IntermediateActivities::DecisionNode,
    fUML::IntermediateActivities::MergeNode,
    Kernel::StructuralFeature,
    Kernel::Slot,
    Kernel::Operation,
    DataType,
    fUML::Kernel::Enumeration,
    fUML::Kernel::PrimitiveType,
    Feature,
    fUML::Kernel::BehavioralFeature,
    Kernel::ValueSpecification,
    Kernel::Class,
    Kernel::DataType,
    Kernel::Association,
    StructuralFeature,
    fUML::Kernel::Property,
    Kernel::Generalization,
    Kernel::RedefinableElement,
    Kernel::Classifier,
    RedefinableElement,
    fUML::Kernel::Feature,
    Kernel::TypedElement,
    Kernel::MultiplicityElement,
    fUML::BasicActions::Pin,
    fUML::Kernel::Parameter,
    Kernel::Feature,
    fUML::Kernel::StructuralFeature,
    fUML::Kernel::Element,
    Kernel::Package,
    Kernel::PackageableElement,
    Kernel::PackageImport,
    Kernel::ElementImport,
    Kernel::NamedElement,
    fUML::Kernel::Comment,
    Kernel::Comment,
    Kernel::Element,
    Kernel::Namespace,
    fUML::Kernel::Package,
    Element,
    fUML::Kernel::Generalization,
    fUML::CompleteStructuredActivities::Clause,
    fUML::IntermediateActions::LinkEndData,
    fUML::Kernel::PackageImport,
    fUML::Kernel::ElementImport,
    fUML::Kernel::MultiplicityElement,
    fUML::Kernel::Slot,
    fUML::Kernel::NamedElement,
    Kernel::Type,
    fUML::Kernel::Classifier,
    TypedElement,
    fUML::Kernel::ValueSpecification,
    BehavioralFeature,
    fUML::Kernel::Operation,
    fUML::Communications::Reception,
    Event,
    fUML::Communications::MessageEvent,
    Communications::Signal,
    MessageEvent,
    fUML::Communications::SignalEvent,
    Kernel::Property,
    PackageableElement,
    fUML::Kernel::Type,
    fUML::Communications::Event,
    Communications::Event,
    NamedElement,
    fUML::Kernel::RedefinableElement,
    fUML::Kernel::PackageableElement,
    fUML::Kernel::TypedElement,
    fUML::Kernel::Namespace,
    fUML::Kernel::InstanceSpecification,
    fUML::Communications::Trigger,
    OpaqueBehavior,
    fUML::BasicBehaviors::FunctionBehavior,
    BasicBehaviors::Behavior,
    Classifier,
    fUML::Kernel::Association,
    fUML::Communications::Signal,
    fUML::Kernel::DataType,
    fUML::BasicBehaviors::BehavioredClassifier,
    BasicBehaviors::BehavioredClassifier,
    Kernel::Parameter,
    Kernel::BehavioralFeature,
    Class,
    fUML::BasicBehaviors::Behavior,
    Behavior,
    fUML::BasicBehaviors::OpaqueBehavior,
    fUML::IntermediateActivities::ActivityNode,
    IntermediateActivities::ActivityEdge,
    fUML::IntermediateActivities::Activity,
    FinalNode,
    fUML::IntermediateActivities::ActivityFinalNode,
    IntermediateActivities::ObjectFlow,
    CompleteStructuredActivities::StructuredActivityNode,
    IntermediateActivities::ActivityNode,
    fUML::IntermediateActivities::ObjectNode,
    IntermediateActivities::Activity,
    fUML::IntermediateActivities::ActivityEdge,
    ActivityEdge,
    fUML::IntermediateActivities::ControlFlow,
    fUML::IntermediateActivities::ObjectFlow,
    Communications::Reception,
    BehavioredClassifier,
    fUML::Kernel::Class,
    Kernel::Enumeration,
    InstanceSpecification,
    fUML::Kernel::EnumerationLiteral,
    Kernel::EnumerationLiteral,
    LiteralSpecification,
    fUML::Kernel::LiteralNull,
    fUML::Kernel::LiteralString,
    fUML::Kernel::LiteralUnlimitedNatural,
    fUML::Kernel::LiteralInteger,
    fUML::Kernel::LiteralBoolean,
    ValueSpecification,
    fUML::Kernel::LiteralSpecification,
    fUML::Kernel::InstanceValue,
    Kernel::InstanceSpecification,
    CallConcurrencyKind,
    ExpansionKind,
    AggregationKind,
    ParameterDirectionKind,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fuml::locil1::semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(fUML::LociL1::SemanticVisitor)


def test_fuml::locil1::semanticvisitor_constructor_exists():
    assert callable(fUML::LociL1::SemanticVisitor.__init__)


def test_fuml::locil1::semanticvisitor_constructor_args():
    sig = inspect.signature(fUML::LociL1::SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(SemanticVisitor)


def test_semanticvisitor_constructor_exists():
    assert callable(SemanticVisitor.__init__)


def test_semanticvisitor_constructor_args():
    sig = inspect.signature(SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::value_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Value)


def test_fuml::kernel::value_constructor_exists():
    assert callable(fUML::Kernel::Value.__init__)


def test_fuml::kernel::value_constructor_args():
    sig = inspect.signature(fUML::Kernel::Value.__init__)
    params = list(sig.parameters.keys())



def test_kernel::featurevalue_is_not_abstract():
    assert not inspect.isabstract(Kernel::FeatureValue)


def test_kernel::featurevalue_constructor_exists():
    assert callable(Kernel::FeatureValue.__init__)


def test_kernel::featurevalue_constructor_args():
    sig = inspect.signature(Kernel::FeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_compoundvalue_is_not_abstract():
    assert not inspect.isabstract(CompoundValue)


def test_compoundvalue_constructor_exists():
    assert callable(CompoundValue.__init__)


def test_compoundvalue_constructor_args():
    sig = inspect.signature(CompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::datavalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::DataValue)


def test_fuml::kernel::datavalue_constructor_exists():
    assert callable(fUML::Kernel::DataValue.__init__)


def test_fuml::kernel::datavalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::DataValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::extensionalvalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::ExtensionalValue)


def test_fuml::kernel::extensionalvalue_constructor_exists():
    assert callable(fUML::Kernel::ExtensionalValue.__init__)


def test_fuml::kernel::extensionalvalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::ExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_extensionalvalue_is_not_abstract():
    assert not inspect.isabstract(ExtensionalValue)


def test_extensionalvalue_constructor_exists():
    assert callable(ExtensionalValue.__init__)


def test_extensionalvalue_constructor_args():
    sig = inspect.signature(ExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::link_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Link)


def test_fuml::kernel::link_constructor_exists():
    assert callable(fUML::Kernel::Link.__init__)


def test_fuml::kernel::link_constructor_args():
    sig = inspect.signature(fUML::Kernel::Link.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::object_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Object)


def test_fuml::kernel::object_constructor_exists():
    assert callable(fUML::Kernel::Object.__init__)


def test_fuml::kernel::object_constructor_args():
    sig = inspect.signature(fUML::Kernel::Object.__init__)
    params = list(sig.parameters.keys())



def test_kernel::object_is_not_abstract():
    assert not inspect.isabstract(Kernel::Object)


def test_kernel::object_constructor_exists():
    assert callable(Kernel::Object.__init__)


def test_kernel::object_constructor_args():
    sig = inspect.signature(Kernel::Object.__init__)
    params = list(sig.parameters.keys())



def test_structuredvalue_is_not_abstract():
    assert not inspect.isabstract(StructuredValue)


def test_structuredvalue_constructor_exists():
    assert callable(StructuredValue.__init__)


def test_structuredvalue_constructor_args():
    sig = inspect.signature(StructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::compoundvalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::CompoundValue)


def test_fuml::kernel::compoundvalue_constructor_exists():
    assert callable(fUML::Kernel::CompoundValue.__init__)


def test_fuml::kernel::compoundvalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::CompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::reference_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Reference)


def test_fuml::kernel::reference_constructor_exists():
    assert callable(fUML::Kernel::Reference.__init__)


def test_fuml::kernel::reference_constructor_args():
    sig = inspect.signature(fUML::Kernel::Reference.__init__)
    params = list(sig.parameters.keys())



def test_kernel::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Kernel::PrimitiveType)


def test_kernel::primitivetype_constructor_exists():
    assert callable(Kernel::PrimitiveType.__init__)


def test_kernel::primitivetype_constructor_args():
    sig = inspect.signature(Kernel::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_primitivevalue_is_not_abstract():
    assert not inspect.isabstract(PrimitiveValue)


def test_primitivevalue_constructor_exists():
    assert callable(PrimitiveValue.__init__)


def test_primitivevalue_constructor_args():
    sig = inspect.signature(PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::BooleanValue)


def test_fuml::kernel::booleanvalue_constructor_exists():
    assert callable(fUML::Kernel::BooleanValue.__init__)


def test_fuml::kernel::booleanvalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::booleanvalue_has_value():
    assert hasattr(fUML::Kernel::BooleanValue, "value")
    descriptor = None
    for klass in fUML::Kernel::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::integervalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::IntegerValue)


def test_fuml::kernel::integervalue_constructor_exists():
    assert callable(fUML::Kernel::IntegerValue.__init__)


def test_fuml::kernel::integervalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::integervalue_has_value():
    assert hasattr(fUML::Kernel::IntegerValue, "value")
    descriptor = None
    for klass in fUML::Kernel::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::unlimitednaturalvalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::UnlimitedNaturalValue)


def test_fuml::kernel::unlimitednaturalvalue_constructor_exists():
    assert callable(fUML::Kernel::UnlimitedNaturalValue.__init__)


def test_fuml::kernel::unlimitednaturalvalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::UnlimitedNaturalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::unlimitednaturalvalue_has_value():
    assert hasattr(fUML::Kernel::UnlimitedNaturalValue, "value")
    descriptor = None
    for klass in fUML::Kernel::UnlimitedNaturalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel::value_is_not_abstract():
    assert not inspect.isabstract(Kernel::Value)


def test_kernel::value_constructor_exists():
    assert callable(Kernel::Value.__init__)


def test_kernel::value_constructor_args():
    sig = inspect.signature(Kernel::Value.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::featurevalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::FeatureValue)


def test_fuml::kernel::featurevalue_constructor_exists():
    assert callable(fUML::Kernel::FeatureValue.__init__)


def test_fuml::kernel::featurevalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::FeatureValue.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_fuml::kernel::featurevalue_has_position():
    assert hasattr(fUML::Kernel::FeatureValue, "position")
    descriptor = None
    for klass in fUML::Kernel::FeatureValue.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::enumerationvalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::EnumerationValue)


def test_fuml::kernel::enumerationvalue_constructor_exists():
    assert callable(fUML::Kernel::EnumerationValue.__init__)


def test_fuml::kernel::enumerationvalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::EnumerationValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::primitivevalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::PrimitiveValue)


def test_fuml::kernel::primitivevalue_constructor_exists():
    assert callable(fUML::Kernel::PrimitiveValue.__init__)


def test_fuml::kernel::primitivevalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::structuredvalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::StructuredValue)


def test_fuml::kernel::structuredvalue_constructor_exists():
    assert callable(fUML::Kernel::StructuredValue.__init__)


def test_fuml::kernel::structuredvalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::StructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::stringvalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::StringValue)


def test_fuml::kernel::stringvalue_constructor_exists():
    assert callable(fUML::Kernel::StringValue.__init__)


def test_fuml::kernel::stringvalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::stringvalue_has_value():
    assert hasattr(fUML::Kernel::StringValue, "value")
    descriptor = None
    for klass in fUML::Kernel::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::SendSignalAction)


def test_fuml::basicactions::sendsignalaction_constructor_exists():
    assert callable(fUML::BasicActions::SendSignalAction.__init__)


def test_fuml::basicactions::sendsignalaction_constructor_args():
    sig = inspect.signature(fUML::BasicActions::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::callaction_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::CallAction)


def test_fuml::basicactions::callaction_constructor_exists():
    assert callable(fUML::BasicActions::CallAction.__init__)


def test_fuml::basicactions::callaction_constructor_args():
    sig = inspect.signature(fUML::BasicActions::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "synchronous" in params, "Missing parameter 'synchronous'"

def test_fuml::basicactions::callaction_has_synchronous():
    assert hasattr(fUML::BasicActions::CallAction, "synchronous")
    descriptor = None
    for klass in fUML::BasicActions::CallAction.__mro__:
        if "synchronous" in klass.__dict__:
            descriptor = klass.__dict__["synchronous"]
            break
    assert isinstance(descriptor, property)



def test_intermediateactivities::objectnode_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::ObjectNode)


def test_intermediateactivities::objectnode_constructor_exists():
    assert callable(IntermediateActivities::ObjectNode.__init__)


def test_intermediateactivities::objectnode_constructor_args():
    sig = inspect.signature(IntermediateActivities::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::outputpin_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::OutputPin)


def test_fuml::basicactions::outputpin_constructor_exists():
    assert callable(fUML::BasicActions::OutputPin.__init__)


def test_fuml::basicactions::outputpin_constructor_args():
    sig = inspect.signature(fUML::BasicActions::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::inputpin_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::InputPin)


def test_fuml::basicactions::inputpin_constructor_exists():
    assert callable(fUML::BasicActions::InputPin.__init__)


def test_fuml::basicactions::inputpin_constructor_args():
    sig = inspect.signature(fUML::BasicActions::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::action_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::Action)


def test_fuml::basicactions::action_constructor_exists():
    assert callable(fUML::BasicActions::Action.__init__)


def test_fuml::basicactions::action_constructor_args():
    sig = inspect.signature(fUML::BasicActions::Action.__init__)
    params = list(sig.parameters.keys())
    assert "locallyReentrant" in params, "Missing parameter 'locallyReentrant'"

def test_fuml::basicactions::action_has_locallyReentrant():
    assert hasattr(fUML::BasicActions::Action, "locallyReentrant")
    descriptor = None
    for klass in fUML::BasicActions::Action.__mro__:
        if "locallyReentrant" in klass.__dict__:
            descriptor = klass.__dict__["locallyReentrant"]
            break
    assert isinstance(descriptor, property)



def test_communications::trigger_is_not_abstract():
    assert not inspect.isabstract(Communications::Trigger)


def test_communications::trigger_constructor_exists():
    assert callable(Communications::Trigger.__init__)


def test_communications::trigger_constructor_args():
    sig = inspect.signature(Communications::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::CallBehaviorAction)


def test_fuml::basicactions::callbehavioraction_constructor_exists():
    assert callable(fUML::BasicActions::CallBehaviorAction.__init__)


def test_fuml::basicactions::callbehavioraction_constructor_args():
    sig = inspect.signature(fUML::BasicActions::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::CallOperationAction)


def test_fuml::basicactions::calloperationaction_constructor_exists():
    assert callable(fUML::BasicActions::CallOperationAction.__init__)


def test_fuml::basicactions::calloperationaction_constructor_args():
    sig = inspect.signature(fUML::BasicActions::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteActions::StartObjectBehaviorAction)


def test_fuml::completeactions::startobjectbehavioraction_constructor_exists():
    assert callable(fUML::CompleteActions::StartObjectBehaviorAction.__init__)


def test_fuml::completeactions::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(fUML::CompleteActions::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::DestroyLinkAction)


def test_fuml::intermediateactions::destroylinkaction_constructor_exists():
    assert callable(fUML::IntermediateActions::DestroyLinkAction.__init__)


def test_fuml::intermediateactions::destroylinkaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::CreateLinkAction)


def test_fuml::intermediateactions::createlinkaction_constructor_exists():
    assert callable(fUML::IntermediateActions::CreateLinkAction.__init__)


def test_fuml::intermediateactions::createlinkaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::LinkEndDestructionData)


def test_fuml::intermediateactions::linkenddestructiondata_constructor_exists():
    assert callable(fUML::IntermediateActions::LinkEndDestructionData.__init__)


def test_fuml::intermediateactions::linkenddestructiondata_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "destroyDuplicates" in params, "Missing parameter 'destroyDuplicates'"

def test_fuml::intermediateactions::linkenddestructiondata_has_destroyDuplicates():
    assert hasattr(fUML::IntermediateActions::LinkEndDestructionData, "destroyDuplicates")
    descriptor = None
    for klass in fUML::IntermediateActions::LinkEndDestructionData.__mro__:
        if "destroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["destroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::LinkEndCreationData)


def test_fuml::intermediateactions::linkendcreationdata_constructor_exists():
    assert callable(fUML::IntermediateActions::LinkEndCreationData.__init__)


def test_fuml::intermediateactions::linkendcreationdata_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml::intermediateactions::linkendcreationdata_has_replaceAll():
    assert hasattr(fUML::IntermediateActions::LinkEndCreationData, "replaceAll")
    descriptor = None
    for klass in fUML::IntermediateActions::LinkEndCreationData.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::AddStructuralFeatureValueAction)


def test_fuml::intermediateactions::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(fUML::IntermediateActions::AddStructuralFeatureValueAction.__init__)


def test_fuml::intermediateactions::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml::intermediateactions::addstructuralfeaturevalueaction_has_replaceAll():
    assert hasattr(fUML::IntermediateActions::AddStructuralFeatureValueAction, "replaceAll")
    descriptor = None
    for klass in fUML::IntermediateActions::AddStructuralFeatureValueAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::RemoveStructuralFeatureValueAction)


def test_fuml::intermediateactions::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(fUML::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)


def test_fuml::intermediateactions::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "removeDuplicates" in params, "Missing parameter 'removeDuplicates'"

def test_fuml::intermediateactions::removestructuralfeaturevalueaction_has_removeDuplicates():
    assert hasattr(fUML::IntermediateActions::RemoveStructuralFeatureValueAction, "removeDuplicates")
    descriptor = None
    for klass in fUML::IntermediateActions::RemoveStructuralFeatureValueAction.__mro__:
        if "removeDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["removeDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::ClearStructuralFeatureAction)


def test_fuml::intermediateactions::clearstructuralfeatureaction_constructor_exists():
    assert callable(fUML::IntermediateActions::ClearStructuralFeatureAction.__init__)


def test_fuml::intermediateactions::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::ReadStructuralFeatureAction)


def test_fuml::intermediateactions::readstructuralfeatureaction_constructor_exists():
    assert callable(fUML::IntermediateActions::ReadStructuralFeatureAction.__init__)


def test_fuml::intermediateactions::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::WriteStructuralFeatureAction)


def test_fuml::intermediateactions::writestructuralfeatureaction_constructor_exists():
    assert callable(fUML::IntermediateActions::WriteStructuralFeatureAction.__init__)


def test_fuml::intermediateactions::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::linkenddata_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::LinkEndData)


def test_intermediateactions::linkenddata_constructor_exists():
    assert callable(IntermediateActions::LinkEndData.__init__)


def test_intermediateactions::linkenddata_constructor_args():
    sig = inspect.signature(IntermediateActions::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_extrastructuredactivities::expansionnode_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities::ExpansionNode)


def test_extrastructuredactivities::expansionnode_constructor_exists():
    assert callable(ExtraStructuredActivities::ExpansionNode.__init__)


def test_extrastructuredactivities::expansionnode_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::ReadLinkAction)


def test_fuml::intermediateactions::readlinkaction_constructor_exists():
    assert callable(fUML::IntermediateActions::ReadLinkAction.__init__)


def test_fuml::intermediateactions::readlinkaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::WriteLinkAction)


def test_fuml::intermediateactions::writelinkaction_constructor_exists():
    assert callable(fUML::IntermediateActions::WriteLinkAction.__init__)


def test_fuml::intermediateactions::writelinkaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_extrastructuredactivities::expansionregion_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities::ExpansionRegion)


def test_extrastructuredactivities::expansionregion_constructor_exists():
    assert callable(ExtraStructuredActivities::ExpansionRegion.__init__)


def test_extrastructuredactivities::expansionregion_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::ClearAssociationAction)


def test_fuml::intermediateactions::clearassociationaction_constructor_exists():
    assert callable(fUML::IntermediateActions::ClearAssociationAction.__init__)


def test_fuml::intermediateactions::clearassociationaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::invocationaction_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::InvocationAction)


def test_fuml::basicactions::invocationaction_constructor_exists():
    assert callable(fUML::BasicActions::InvocationAction.__init__)


def test_fuml::basicactions::invocationaction_constructor_args():
    sig = inspect.signature(fUML::BasicActions::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::ValueSpecificationAction)


def test_fuml::intermediateactions::valuespecificationaction_constructor_exists():
    assert callable(fUML::IntermediateActions::ValueSpecificationAction.__init__)


def test_fuml::intermediateactions::valuespecificationaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::CreateObjectAction)


def test_fuml::intermediateactions::createobjectaction_constructor_exists():
    assert callable(fUML::IntermediateActions::CreateObjectAction.__init__)


def test_fuml::intermediateactions::createobjectaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteActions::AcceptEventAction)


def test_fuml::completeactions::accepteventaction_constructor_exists():
    assert callable(fUML::CompleteActions::AcceptEventAction.__init__)


def test_fuml::completeactions::accepteventaction_constructor_args():
    sig = inspect.signature(fUML::CompleteActions::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshall" in params, "Missing parameter 'unmarshall'"

def test_fuml::completeactions::accepteventaction_has_unmarshall():
    assert hasattr(fUML::CompleteActions::AcceptEventAction, "unmarshall")
    descriptor = None
    for klass in fUML::CompleteActions::AcceptEventAction.__mro__:
        if "unmarshall" in klass.__dict__:
            descriptor = klass.__dict__["unmarshall"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::TestIdentityAction)


def test_fuml::intermediateactions::testidentityaction_constructor_exists():
    assert callable(fUML::IntermediateActions::TestIdentityAction.__init__)


def test_fuml::intermediateactions::testidentityaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteActions::ReclassifyObjectAction)


def test_fuml::completeactions::reclassifyobjectaction_constructor_exists():
    assert callable(fUML::CompleteActions::ReclassifyObjectAction.__init__)


def test_fuml::completeactions::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(fUML::CompleteActions::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml::completeactions::reclassifyobjectaction_has_replaceAll():
    assert hasattr(fUML::CompleteActions::ReclassifyObjectAction, "replaceAll")
    descriptor = None
    for klass in fUML::CompleteActions::ReclassifyObjectAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::StructuralFeatureAction)


def test_fuml::intermediateactions::structuralfeatureaction_constructor_exists():
    assert callable(fUML::IntermediateActions::StructuralFeatureAction.__init__)


def test_fuml::intermediateactions::structuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::reduceaction_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteActions::ReduceAction)


def test_fuml::completeactions::reduceaction_constructor_exists():
    assert callable(fUML::CompleteActions::ReduceAction.__init__)


def test_fuml::completeactions::reduceaction_constructor_args():
    sig = inspect.signature(fUML::CompleteActions::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_fuml::completeactions::reduceaction_has_ordered():
    assert hasattr(fUML::CompleteActions::ReduceAction, "ordered")
    descriptor = None
    for klass in fUML::CompleteActions::ReduceAction.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::readselfaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::ReadSelfAction)


def test_fuml::intermediateactions::readselfaction_constructor_exists():
    assert callable(fUML::IntermediateActions::ReadSelfAction.__init__)


def test_fuml::intermediateactions::readselfaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteActions::StartClassifierBehaviorAction)


def test_fuml::completeactions::startclassifierbehavioraction_constructor_exists():
    assert callable(fUML::CompleteActions::StartClassifierBehaviorAction.__init__)


def test_fuml::completeactions::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(fUML::CompleteActions::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteActions::ReadIsClassifiedObjectAction)


def test_fuml::completeactions::readisclassifiedobjectaction_constructor_exists():
    assert callable(fUML::CompleteActions::ReadIsClassifiedObjectAction.__init__)


def test_fuml::completeactions::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(fUML::CompleteActions::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "direct" in params, "Missing parameter 'direct'"

def test_fuml::completeactions::readisclassifiedobjectaction_has_direct():
    assert hasattr(fUML::CompleteActions::ReadIsClassifiedObjectAction, "direct")
    descriptor = None
    for klass in fUML::CompleteActions::ReadIsClassifiedObjectAction.__mro__:
        if "direct" in klass.__dict__:
            descriptor = klass.__dict__["direct"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::DestroyObjectAction)


def test_fuml::intermediateactions::destroyobjectaction_constructor_exists():
    assert callable(fUML::IntermediateActions::DestroyObjectAction.__init__)


def test_fuml::intermediateactions::destroyobjectaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "destroyLinks" in params, "Missing parameter 'destroyLinks'"
    assert "destroyOwnedObjects" in params, "Missing parameter 'destroyOwnedObjects'"

def test_fuml::intermediateactions::destroyobjectaction_has_destroyLinks():
    assert hasattr(fUML::IntermediateActions::DestroyObjectAction, "destroyLinks")
    descriptor = None
    for klass in fUML::IntermediateActions::DestroyObjectAction.__mro__:
        if "destroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["destroyLinks"]
            break
    assert isinstance(descriptor, property)

def test_fuml::intermediateactions::destroyobjectaction_has_destroyOwnedObjects():
    assert hasattr(fUML::IntermediateActions::DestroyObjectAction, "destroyOwnedObjects")
    descriptor = None
    for klass in fUML::IntermediateActions::DestroyObjectAction.__mro__:
        if "destroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["destroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completeactions::readextentaction_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteActions::ReadExtentAction)


def test_fuml::completeactions::readextentaction_constructor_exists():
    assert callable(fUML::CompleteActions::ReadExtentAction.__init__)


def test_fuml::completeactions::readextentaction_constructor_args():
    sig = inspect.signature(fUML::CompleteActions::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::linkaction_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::LinkAction)


def test_fuml::intermediateactions::linkaction_constructor_exists():
    assert callable(fUML::IntermediateActions::LinkAction.__init__)


def test_fuml::intermediateactions::linkaction_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completestructuredactivities::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteStructuredActivities::StructuredActivityNode)


def test_fuml::completestructuredactivities::structuredactivitynode_constructor_exists():
    assert callable(fUML::CompleteStructuredActivities::StructuredActivityNode.__init__)


def test_fuml::completestructuredactivities::structuredactivitynode_constructor_args():
    sig = inspect.signature(fUML::CompleteStructuredActivities::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_fuml::completestructuredactivities::structuredactivitynode_has_mustIsolate():
    assert hasattr(fUML::CompleteStructuredActivities::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in fUML::CompleteStructuredActivities::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_basicactions::inputpin_is_not_abstract():
    assert not inspect.isabstract(BasicActions::InputPin)


def test_basicactions::inputpin_constructor_exists():
    assert callable(BasicActions::InputPin.__init__)


def test_basicactions::inputpin_constructor_args():
    sig = inspect.signature(BasicActions::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_completestructuredactivities::executablenode_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities::ExecutableNode)


def test_completestructuredactivities::executablenode_constructor_exists():
    assert callable(CompleteStructuredActivities::ExecutableNode.__init__)


def test_completestructuredactivities::executablenode_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::outputpin_is_not_abstract():
    assert not inspect.isabstract(BasicActions::OutputPin)


def test_basicactions::outputpin_constructor_exists():
    assert callable(BasicActions::OutputPin.__init__)


def test_basicactions::outputpin_constructor_args():
    sig = inspect.signature(BasicActions::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::extrastructuredactivities::expansionregion_is_not_abstract():
    assert not inspect.isabstract(fUML::ExtraStructuredActivities::ExpansionRegion)


def test_fuml::extrastructuredactivities::expansionregion_constructor_exists():
    assert callable(fUML::ExtraStructuredActivities::ExpansionRegion.__init__)


def test_fuml::extrastructuredactivities::expansionregion_constructor_args():
    sig = inspect.signature(fUML::ExtraStructuredActivities::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_fuml::extrastructuredactivities::expansionregion_has_mode():
    assert hasattr(fUML::ExtraStructuredActivities::ExpansionRegion, "mode")
    descriptor = None
    for klass in fUML::ExtraStructuredActivities::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completestructuredactivities::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteStructuredActivities::ConditionalNode)


def test_fuml::completestructuredactivities::conditionalnode_constructor_exists():
    assert callable(fUML::CompleteStructuredActivities::ConditionalNode.__init__)


def test_fuml::completestructuredactivities::conditionalnode_constructor_args():
    sig = inspect.signature(fUML::CompleteStructuredActivities::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "assured" in params, "Missing parameter 'assured'"
    assert "determinate" in params, "Missing parameter 'determinate'"

def test_fuml::completestructuredactivities::conditionalnode_has_assured():
    assert hasattr(fUML::CompleteStructuredActivities::ConditionalNode, "assured")
    descriptor = None
    for klass in fUML::CompleteStructuredActivities::ConditionalNode.__mro__:
        if "assured" in klass.__dict__:
            descriptor = klass.__dict__["assured"]
            break
    assert isinstance(descriptor, property)

def test_fuml::completestructuredactivities::conditionalnode_has_determinate():
    assert hasattr(fUML::CompleteStructuredActivities::ConditionalNode, "determinate")
    descriptor = None
    for klass in fUML::CompleteStructuredActivities::ConditionalNode.__mro__:
        if "determinate" in klass.__dict__:
            descriptor = klass.__dict__["determinate"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completestructuredactivities::loopnode_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteStructuredActivities::LoopNode)


def test_fuml::completestructuredactivities::loopnode_constructor_exists():
    assert callable(fUML::CompleteStructuredActivities::LoopNode.__init__)


def test_fuml::completestructuredactivities::loopnode_constructor_args():
    sig = inspect.signature(fUML::CompleteStructuredActivities::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "testedFirst" in params, "Missing parameter 'testedFirst'"

def test_fuml::completestructuredactivities::loopnode_has_testedFirst():
    assert hasattr(fUML::CompleteStructuredActivities::LoopNode, "testedFirst")
    descriptor = None
    for klass in fUML::CompleteStructuredActivities::LoopNode.__mro__:
        if "testedFirst" in klass.__dict__:
            descriptor = klass.__dict__["testedFirst"]
            break
    assert isinstance(descriptor, property)



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::extrastructuredactivities::expansionnode_is_not_abstract():
    assert not inspect.isabstract(fUML::ExtraStructuredActivities::ExpansionNode)


def test_fuml::extrastructuredactivities::expansionnode_constructor_exists():
    assert callable(fUML::ExtraStructuredActivities::ExpansionNode.__init__)


def test_fuml::extrastructuredactivities::expansionnode_constructor_args():
    sig = inspect.signature(fUML::ExtraStructuredActivities::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ActivityParameterNode)


def test_fuml::intermediateactivities::activityparameternode_constructor_exists():
    assert callable(fUML::IntermediateActivities::ActivityParameterNode.__init__)


def test_fuml::intermediateactivities::activityparameternode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_completestructuredactivities::clause_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities::Clause)


def test_completestructuredactivities::clause_constructor_exists():
    assert callable(CompleteStructuredActivities::Clause.__init__)


def test_completestructuredactivities::clause_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities::Clause.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completestructuredactivities::executablenode_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteStructuredActivities::ExecutableNode)


def test_fuml::completestructuredactivities::executablenode_constructor_exists():
    assert callable(fUML::CompleteStructuredActivities::ExecutableNode.__init__)


def test_fuml::completestructuredactivities::executablenode_constructor_args():
    sig = inspect.signature(fUML::CompleteStructuredActivities::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::controlnode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ControlNode)


def test_fuml::intermediateactivities::controlnode_constructor_exists():
    assert callable(fUML::IntermediateActivities::ControlNode.__init__)


def test_fuml::intermediateactivities::controlnode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::forknode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ForkNode)


def test_fuml::intermediateactivities::forknode_constructor_exists():
    assert callable(fUML::IntermediateActivities::ForkNode.__init__)


def test_fuml::intermediateactivities::forknode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::initialnode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::InitialNode)


def test_fuml::intermediateactivities::initialnode_constructor_exists():
    assert callable(fUML::IntermediateActivities::InitialNode.__init__)


def test_fuml::intermediateactivities::initialnode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::joinnode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::JoinNode)


def test_fuml::intermediateactivities::joinnode_constructor_exists():
    assert callable(fUML::IntermediateActivities::JoinNode.__init__)


def test_fuml::intermediateactivities::joinnode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::finalnode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::FinalNode)


def test_fuml::intermediateactivities::finalnode_constructor_exists():
    assert callable(fUML::IntermediateActivities::FinalNode.__init__)


def test_fuml::intermediateactivities::finalnode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::decisionnode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::DecisionNode)


def test_fuml::intermediateactivities::decisionnode_constructor_exists():
    assert callable(fUML::IntermediateActivities::DecisionNode.__init__)


def test_fuml::intermediateactivities::decisionnode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::mergenode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::MergeNode)


def test_fuml::intermediateactivities::mergenode_constructor_exists():
    assert callable(fUML::IntermediateActivities::MergeNode.__init__)


def test_fuml::intermediateactivities::mergenode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_kernel::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(Kernel::StructuralFeature)


def test_kernel::structuralfeature_constructor_exists():
    assert callable(Kernel::StructuralFeature.__init__)


def test_kernel::structuralfeature_constructor_args():
    sig = inspect.signature(Kernel::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_kernel::slot_is_not_abstract():
    assert not inspect.isabstract(Kernel::Slot)


def test_kernel::slot_constructor_exists():
    assert callable(Kernel::Slot.__init__)


def test_kernel::slot_constructor_args():
    sig = inspect.signature(Kernel::Slot.__init__)
    params = list(sig.parameters.keys())



def test_kernel::operation_is_not_abstract():
    assert not inspect.isabstract(Kernel::Operation)


def test_kernel::operation_constructor_exists():
    assert callable(Kernel::Operation.__init__)


def test_kernel::operation_constructor_args():
    sig = inspect.signature(Kernel::Operation.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::enumeration_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Enumeration)


def test_fuml::kernel::enumeration_constructor_exists():
    assert callable(fUML::Kernel::Enumeration.__init__)


def test_fuml::kernel::enumeration_constructor_args():
    sig = inspect.signature(fUML::Kernel::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::primitivetype_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::PrimitiveType)


def test_fuml::kernel::primitivetype_constructor_exists():
    assert callable(fUML::Kernel::PrimitiveType.__init__)


def test_fuml::kernel::primitivetype_constructor_args():
    sig = inspect.signature(fUML::Kernel::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::BehavioralFeature)


def test_fuml::kernel::behavioralfeature_constructor_exists():
    assert callable(fUML::Kernel::BehavioralFeature.__init__)


def test_fuml::kernel::behavioralfeature_constructor_args():
    sig = inspect.signature(fUML::Kernel::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_fuml::kernel::behavioralfeature_has_concurrency():
    assert hasattr(fUML::Kernel::BehavioralFeature, "concurrency")
    descriptor = None
    for klass in fUML::Kernel::BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::behavioralfeature_has_abstract():
    assert hasattr(fUML::Kernel::BehavioralFeature, "abstract")
    descriptor = None
    for klass in fUML::Kernel::BehavioralFeature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_kernel::valuespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel::ValueSpecification)


def test_kernel::valuespecification_constructor_exists():
    assert callable(Kernel::ValueSpecification.__init__)


def test_kernel::valuespecification_constructor_args():
    sig = inspect.signature(Kernel::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel::class_is_not_abstract():
    assert not inspect.isabstract(Kernel::Class)


def test_kernel::class_constructor_exists():
    assert callable(Kernel::Class.__init__)


def test_kernel::class_constructor_args():
    sig = inspect.signature(Kernel::Class.__init__)
    params = list(sig.parameters.keys())



def test_kernel::datatype_is_not_abstract():
    assert not inspect.isabstract(Kernel::DataType)


def test_kernel::datatype_constructor_exists():
    assert callable(Kernel::DataType.__init__)


def test_kernel::datatype_constructor_args():
    sig = inspect.signature(Kernel::DataType.__init__)
    params = list(sig.parameters.keys())



def test_kernel::association_is_not_abstract():
    assert not inspect.isabstract(Kernel::Association)


def test_kernel::association_constructor_exists():
    assert callable(Kernel::Association.__init__)


def test_kernel::association_constructor_args():
    sig = inspect.signature(Kernel::Association.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::property_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Property)


def test_fuml::kernel::property_constructor_exists():
    assert callable(fUML::Kernel::Property.__init__)


def test_fuml::kernel::property_constructor_args():
    sig = inspect.signature(fUML::Kernel::Property.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "derivedUnion" in params, "Missing parameter 'derivedUnion'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "composite" in params, "Missing parameter 'composite'"

def test_fuml::kernel::property_has_aggregation():
    assert hasattr(fUML::Kernel::Property, "aggregation")
    descriptor = None
    for klass in fUML::Kernel::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::property_has_derivedUnion():
    assert hasattr(fUML::Kernel::Property, "derivedUnion")
    descriptor = None
    for klass in fUML::Kernel::Property.__mro__:
        if "derivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["derivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::property_has_derived():
    assert hasattr(fUML::Kernel::Property, "derived")
    descriptor = None
    for klass in fUML::Kernel::Property.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::property_has_composite():
    assert hasattr(fUML::Kernel::Property, "composite")
    descriptor = None
    for klass in fUML::Kernel::Property.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
            break
    assert isinstance(descriptor, property)



def test_kernel::generalization_is_not_abstract():
    assert not inspect.isabstract(Kernel::Generalization)


def test_kernel::generalization_constructor_exists():
    assert callable(Kernel::Generalization.__init__)


def test_kernel::generalization_constructor_args():
    sig = inspect.signature(Kernel::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_kernel::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(Kernel::RedefinableElement)


def test_kernel::redefinableelement_constructor_exists():
    assert callable(Kernel::RedefinableElement.__init__)


def test_kernel::redefinableelement_constructor_args():
    sig = inspect.signature(Kernel::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::classifier_is_not_abstract():
    assert not inspect.isabstract(Kernel::Classifier)


def test_kernel::classifier_constructor_exists():
    assert callable(Kernel::Classifier.__init__)


def test_kernel::classifier_constructor_args():
    sig = inspect.signature(Kernel::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::feature_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Feature)


def test_fuml::kernel::feature_constructor_exists():
    assert callable(fUML::Kernel::Feature.__init__)


def test_fuml::kernel::feature_constructor_args():
    sig = inspect.signature(fUML::Kernel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_fuml::kernel::feature_has_static():
    assert hasattr(fUML::Kernel::Feature, "static")
    descriptor = None
    for klass in fUML::Kernel::Feature.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_kernel::typedelement_is_not_abstract():
    assert not inspect.isabstract(Kernel::TypedElement)


def test_kernel::typedelement_constructor_exists():
    assert callable(Kernel::TypedElement.__init__)


def test_kernel::typedelement_constructor_args():
    sig = inspect.signature(Kernel::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(Kernel::MultiplicityElement)


def test_kernel::multiplicityelement_constructor_exists():
    assert callable(Kernel::MultiplicityElement.__init__)


def test_kernel::multiplicityelement_constructor_args():
    sig = inspect.signature(Kernel::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::pin_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicActions::Pin)


def test_fuml::basicactions::pin_constructor_exists():
    assert callable(fUML::BasicActions::Pin.__init__)


def test_fuml::basicactions::pin_constructor_args():
    sig = inspect.signature(fUML::BasicActions::Pin.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::parameter_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Parameter)


def test_fuml::kernel::parameter_constructor_exists():
    assert callable(fUML::Kernel::Parameter.__init__)


def test_fuml::kernel::parameter_constructor_args():
    sig = inspect.signature(fUML::Kernel::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_fuml::kernel::parameter_has_direction():
    assert hasattr(fUML::Kernel::Parameter, "direction")
    descriptor = None
    for klass in fUML::Kernel::Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_kernel::feature_is_not_abstract():
    assert not inspect.isabstract(Kernel::Feature)


def test_kernel::feature_constructor_exists():
    assert callable(Kernel::Feature.__init__)


def test_kernel::feature_constructor_args():
    sig = inspect.signature(Kernel::Feature.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::StructuralFeature)


def test_fuml::kernel::structuralfeature_constructor_exists():
    assert callable(fUML::Kernel::StructuralFeature.__init__)


def test_fuml::kernel::structuralfeature_constructor_args():
    sig = inspect.signature(fUML::Kernel::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_fuml::kernel::structuralfeature_has_readOnly():
    assert hasattr(fUML::Kernel::StructuralFeature, "readOnly")
    descriptor = None
    for klass in fUML::Kernel::StructuralFeature.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::element_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Element)


def test_fuml::kernel::element_constructor_exists():
    assert callable(fUML::Kernel::Element.__init__)


def test_fuml::kernel::element_constructor_args():
    sig = inspect.signature(fUML::Kernel::Element.__init__)
    params = list(sig.parameters.keys())



def test_kernel::package_is_not_abstract():
    assert not inspect.isabstract(Kernel::Package)


def test_kernel::package_constructor_exists():
    assert callable(Kernel::Package.__init__)


def test_kernel::package_constructor_args():
    sig = inspect.signature(Kernel::Package.__init__)
    params = list(sig.parameters.keys())



def test_kernel::packageableelement_is_not_abstract():
    assert not inspect.isabstract(Kernel::PackageableElement)


def test_kernel::packageableelement_constructor_exists():
    assert callable(Kernel::PackageableElement.__init__)


def test_kernel::packageableelement_constructor_args():
    sig = inspect.signature(Kernel::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::packageimport_is_not_abstract():
    assert not inspect.isabstract(Kernel::PackageImport)


def test_kernel::packageimport_constructor_exists():
    assert callable(Kernel::PackageImport.__init__)


def test_kernel::packageimport_constructor_args():
    sig = inspect.signature(Kernel::PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_kernel::elementimport_is_not_abstract():
    assert not inspect.isabstract(Kernel::ElementImport)


def test_kernel::elementimport_constructor_exists():
    assert callable(Kernel::ElementImport.__init__)


def test_kernel::elementimport_constructor_args():
    sig = inspect.signature(Kernel::ElementImport.__init__)
    params = list(sig.parameters.keys())



def test_kernel::namedelement_is_not_abstract():
    assert not inspect.isabstract(Kernel::NamedElement)


def test_kernel::namedelement_constructor_exists():
    assert callable(Kernel::NamedElement.__init__)


def test_kernel::namedelement_constructor_args():
    sig = inspect.signature(Kernel::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::comment_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Comment)


def test_fuml::kernel::comment_constructor_exists():
    assert callable(fUML::Kernel::Comment.__init__)


def test_fuml::kernel::comment_constructor_args():
    sig = inspect.signature(fUML::Kernel::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_fuml::kernel::comment_has_body():
    assert hasattr(fUML::Kernel::Comment, "body")
    descriptor = None
    for klass in fUML::Kernel::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_kernel::comment_is_not_abstract():
    assert not inspect.isabstract(Kernel::Comment)


def test_kernel::comment_constructor_exists():
    assert callable(Kernel::Comment.__init__)


def test_kernel::comment_constructor_args():
    sig = inspect.signature(Kernel::Comment.__init__)
    params = list(sig.parameters.keys())



def test_kernel::element_is_not_abstract():
    assert not inspect.isabstract(Kernel::Element)


def test_kernel::element_constructor_exists():
    assert callable(Kernel::Element.__init__)


def test_kernel::element_constructor_args():
    sig = inspect.signature(Kernel::Element.__init__)
    params = list(sig.parameters.keys())



def test_kernel::namespace_is_not_abstract():
    assert not inspect.isabstract(Kernel::Namespace)


def test_kernel::namespace_constructor_exists():
    assert callable(Kernel::Namespace.__init__)


def test_kernel::namespace_constructor_args():
    sig = inspect.signature(Kernel::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::package_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Package)


def test_fuml::kernel::package_constructor_exists():
    assert callable(fUML::Kernel::Package.__init__)


def test_fuml::kernel::package_constructor_args():
    sig = inspect.signature(fUML::Kernel::Package.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::generalization_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Generalization)


def test_fuml::kernel::generalization_constructor_exists():
    assert callable(fUML::Kernel::Generalization.__init__)


def test_fuml::kernel::generalization_constructor_args():
    sig = inspect.signature(fUML::Kernel::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "substitutable" in params, "Missing parameter 'substitutable'"

def test_fuml::kernel::generalization_has_substitutable():
    assert hasattr(fUML::Kernel::Generalization, "substitutable")
    descriptor = None
    for klass in fUML::Kernel::Generalization.__mro__:
        if "substitutable" in klass.__dict__:
            descriptor = klass.__dict__["substitutable"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completestructuredactivities::clause_is_not_abstract():
    assert not inspect.isabstract(fUML::CompleteStructuredActivities::Clause)


def test_fuml::completestructuredactivities::clause_constructor_exists():
    assert callable(fUML::CompleteStructuredActivities::Clause.__init__)


def test_fuml::completestructuredactivities::clause_constructor_args():
    sig = inspect.signature(fUML::CompleteStructuredActivities::Clause.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::linkenddata_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActions::LinkEndData)


def test_fuml::intermediateactions::linkenddata_constructor_exists():
    assert callable(fUML::IntermediateActions::LinkEndData.__init__)


def test_fuml::intermediateactions::linkenddata_constructor_args():
    sig = inspect.signature(fUML::IntermediateActions::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::packageimport_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::PackageImport)


def test_fuml::kernel::packageimport_constructor_exists():
    assert callable(fUML::Kernel::PackageImport.__init__)


def test_fuml::kernel::packageimport_constructor_args():
    sig = inspect.signature(fUML::Kernel::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_fuml::kernel::packageimport_has_visibility():
    assert hasattr(fUML::Kernel::PackageImport, "visibility")
    descriptor = None
    for klass in fUML::Kernel::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::elementimport_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::ElementImport)


def test_fuml::kernel::elementimport_constructor_exists():
    assert callable(fUML::Kernel::ElementImport.__init__)


def test_fuml::kernel::elementimport_constructor_args():
    sig = inspect.signature(fUML::Kernel::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_fuml::kernel::elementimport_has_alias():
    assert hasattr(fUML::Kernel::ElementImport, "alias")
    descriptor = None
    for klass in fUML::Kernel::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::elementimport_has_visibility():
    assert hasattr(fUML::Kernel::ElementImport, "visibility")
    descriptor = None
    for klass in fUML::Kernel::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::MultiplicityElement)


def test_fuml::kernel::multiplicityelement_constructor_exists():
    assert callable(fUML::Kernel::MultiplicityElement.__init__)


def test_fuml::kernel::multiplicityelement_constructor_args():
    sig = inspect.signature(fUML::Kernel::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_fuml::kernel::multiplicityelement_has_upper():
    assert hasattr(fUML::Kernel::MultiplicityElement, "upper")
    descriptor = None
    for klass in fUML::Kernel::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::multiplicityelement_has_lower():
    assert hasattr(fUML::Kernel::MultiplicityElement, "lower")
    descriptor = None
    for klass in fUML::Kernel::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::multiplicityelement_has_ordered():
    assert hasattr(fUML::Kernel::MultiplicityElement, "ordered")
    descriptor = None
    for klass in fUML::Kernel::MultiplicityElement.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::multiplicityelement_has_unique():
    assert hasattr(fUML::Kernel::MultiplicityElement, "unique")
    descriptor = None
    for klass in fUML::Kernel::MultiplicityElement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::slot_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Slot)


def test_fuml::kernel::slot_constructor_exists():
    assert callable(fUML::Kernel::Slot.__init__)


def test_fuml::kernel::slot_constructor_args():
    sig = inspect.signature(fUML::Kernel::Slot.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::namedelement_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::NamedElement)


def test_fuml::kernel::namedelement_constructor_exists():
    assert callable(fUML::Kernel::NamedElement.__init__)


def test_fuml::kernel::namedelement_constructor_args():
    sig = inspect.signature(fUML::Kernel::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_fuml::kernel::namedelement_has_visibility():
    assert hasattr(fUML::Kernel::NamedElement, "visibility")
    descriptor = None
    for klass in fUML::Kernel::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::namedelement_has_name():
    assert hasattr(fUML::Kernel::NamedElement, "name")
    descriptor = None
    for klass in fUML::Kernel::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::namedelement_has_qualifiedName():
    assert hasattr(fUML::Kernel::NamedElement, "qualifiedName")
    descriptor = None
    for klass in fUML::Kernel::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_kernel::type_is_not_abstract():
    assert not inspect.isabstract(Kernel::Type)


def test_kernel::type_constructor_exists():
    assert callable(Kernel::Type.__init__)


def test_kernel::type_constructor_args():
    sig = inspect.signature(Kernel::Type.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::classifier_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Classifier)


def test_fuml::kernel::classifier_constructor_exists():
    assert callable(fUML::Kernel::Classifier.__init__)


def test_fuml::kernel::classifier_constructor_args():
    sig = inspect.signature(fUML::Kernel::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "finalSpecialization" in params, "Missing parameter 'finalSpecialization'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_fuml::kernel::classifier_has_finalSpecialization():
    assert hasattr(fUML::Kernel::Classifier, "finalSpecialization")
    descriptor = None
    for klass in fUML::Kernel::Classifier.__mro__:
        if "finalSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["finalSpecialization"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::classifier_has_abstract():
    assert hasattr(fUML::Kernel::Classifier, "abstract")
    descriptor = None
    for klass in fUML::Kernel::Classifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::valuespecification_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::ValueSpecification)


def test_fuml::kernel::valuespecification_constructor_exists():
    assert callable(fUML::Kernel::ValueSpecification.__init__)


def test_fuml::kernel::valuespecification_constructor_args():
    sig = inspect.signature(fUML::Kernel::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::operation_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Operation)


def test_fuml::kernel::operation_constructor_exists():
    assert callable(fUML::Kernel::Operation.__init__)


def test_fuml::kernel::operation_constructor_args():
    sig = inspect.signature(fUML::Kernel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "query" in params, "Missing parameter 'query'"

def test_fuml::kernel::operation_has_ordered():
    assert hasattr(fUML::Kernel::Operation, "ordered")
    descriptor = None
    for klass in fUML::Kernel::Operation.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_unique():
    assert hasattr(fUML::Kernel::Operation, "unique")
    descriptor = None
    for klass in fUML::Kernel::Operation.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_lower():
    assert hasattr(fUML::Kernel::Operation, "lower")
    descriptor = None
    for klass in fUML::Kernel::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_upper():
    assert hasattr(fUML::Kernel::Operation, "upper")
    descriptor = None
    for klass in fUML::Kernel::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_query():
    assert hasattr(fUML::Kernel::Operation, "query")
    descriptor = None
    for klass in fUML::Kernel::Operation.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_fuml::communications::reception_is_not_abstract():
    assert not inspect.isabstract(fUML::Communications::Reception)


def test_fuml::communications::reception_constructor_exists():
    assert callable(fUML::Communications::Reception.__init__)


def test_fuml::communications::reception_constructor_args():
    sig = inspect.signature(fUML::Communications::Reception.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_fuml::communications::messageevent_is_not_abstract():
    assert not inspect.isabstract(fUML::Communications::MessageEvent)


def test_fuml::communications::messageevent_constructor_exists():
    assert callable(fUML::Communications::MessageEvent.__init__)


def test_fuml::communications::messageevent_constructor_args():
    sig = inspect.signature(fUML::Communications::MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_communications::signal_is_not_abstract():
    assert not inspect.isabstract(Communications::Signal)


def test_communications::signal_constructor_exists():
    assert callable(Communications::Signal.__init__)


def test_communications::signal_constructor_args():
    sig = inspect.signature(Communications::Signal.__init__)
    params = list(sig.parameters.keys())



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_fuml::communications::signalevent_is_not_abstract():
    assert not inspect.isabstract(fUML::Communications::SignalEvent)


def test_fuml::communications::signalevent_constructor_exists():
    assert callable(fUML::Communications::SignalEvent.__init__)


def test_fuml::communications::signalevent_constructor_args():
    sig = inspect.signature(fUML::Communications::SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_kernel::property_is_not_abstract():
    assert not inspect.isabstract(Kernel::Property)


def test_kernel::property_constructor_exists():
    assert callable(Kernel::Property.__init__)


def test_kernel::property_constructor_args():
    sig = inspect.signature(Kernel::Property.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::type_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Type)


def test_fuml::kernel::type_constructor_exists():
    assert callable(fUML::Kernel::Type.__init__)


def test_fuml::kernel::type_constructor_args():
    sig = inspect.signature(fUML::Kernel::Type.__init__)
    params = list(sig.parameters.keys())



def test_fuml::communications::event_is_not_abstract():
    assert not inspect.isabstract(fUML::Communications::Event)


def test_fuml::communications::event_constructor_exists():
    assert callable(fUML::Communications::Event.__init__)


def test_fuml::communications::event_constructor_args():
    sig = inspect.signature(fUML::Communications::Event.__init__)
    params = list(sig.parameters.keys())



def test_communications::event_is_not_abstract():
    assert not inspect.isabstract(Communications::Event)


def test_communications::event_constructor_exists():
    assert callable(Communications::Event.__init__)


def test_communications::event_constructor_args():
    sig = inspect.signature(Communications::Event.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::RedefinableElement)


def test_fuml::kernel::redefinableelement_constructor_exists():
    assert callable(fUML::Kernel::RedefinableElement.__init__)


def test_fuml::kernel::redefinableelement_constructor_args():
    sig = inspect.signature(fUML::Kernel::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "leaf" in params, "Missing parameter 'leaf'"

def test_fuml::kernel::redefinableelement_has_leaf():
    assert hasattr(fUML::Kernel::RedefinableElement, "leaf")
    descriptor = None
    for klass in fUML::Kernel::RedefinableElement.__mro__:
        if "leaf" in klass.__dict__:
            descriptor = klass.__dict__["leaf"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::packageableelement_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::PackageableElement)


def test_fuml::kernel::packageableelement_constructor_exists():
    assert callable(fUML::Kernel::PackageableElement.__init__)


def test_fuml::kernel::packageableelement_constructor_args():
    sig = inspect.signature(fUML::Kernel::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::typedelement_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::TypedElement)


def test_fuml::kernel::typedelement_constructor_exists():
    assert callable(fUML::Kernel::TypedElement.__init__)


def test_fuml::kernel::typedelement_constructor_args():
    sig = inspect.signature(fUML::Kernel::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::namespace_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Namespace)


def test_fuml::kernel::namespace_constructor_exists():
    assert callable(fUML::Kernel::Namespace.__init__)


def test_fuml::kernel::namespace_constructor_args():
    sig = inspect.signature(fUML::Kernel::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::instancespecification_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::InstanceSpecification)


def test_fuml::kernel::instancespecification_constructor_exists():
    assert callable(fUML::Kernel::InstanceSpecification.__init__)


def test_fuml::kernel::instancespecification_constructor_args():
    sig = inspect.signature(fUML::Kernel::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::communications::trigger_is_not_abstract():
    assert not inspect.isabstract(fUML::Communications::Trigger)


def test_fuml::communications::trigger_constructor_exists():
    assert callable(fUML::Communications::Trigger.__init__)


def test_fuml::communications::trigger_constructor_args():
    sig = inspect.signature(fUML::Communications::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicbehaviors::functionbehavior_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicBehaviors::FunctionBehavior)


def test_fuml::basicbehaviors::functionbehavior_constructor_exists():
    assert callable(fUML::BasicBehaviors::FunctionBehavior.__init__)


def test_fuml::basicbehaviors::functionbehavior_constructor_args():
    sig = inspect.signature(fUML::BasicBehaviors::FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors::behavior_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors::Behavior)


def test_basicbehaviors::behavior_constructor_exists():
    assert callable(BasicBehaviors::Behavior.__init__)


def test_basicbehaviors::behavior_constructor_args():
    sig = inspect.signature(BasicBehaviors::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::association_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Association)


def test_fuml::kernel::association_constructor_exists():
    assert callable(fUML::Kernel::Association.__init__)


def test_fuml::kernel::association_constructor_args():
    sig = inspect.signature(fUML::Kernel::Association.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"

def test_fuml::kernel::association_has_derived():
    assert hasattr(fUML::Kernel::Association, "derived")
    descriptor = None
    for klass in fUML::Kernel::Association.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_fuml::communications::signal_is_not_abstract():
    assert not inspect.isabstract(fUML::Communications::Signal)


def test_fuml::communications::signal_constructor_exists():
    assert callable(fUML::Communications::Signal.__init__)


def test_fuml::communications::signal_constructor_args():
    sig = inspect.signature(fUML::Communications::Signal.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::datatype_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::DataType)


def test_fuml::kernel::datatype_constructor_exists():
    assert callable(fUML::Kernel::DataType.__init__)


def test_fuml::kernel::datatype_constructor_args():
    sig = inspect.signature(fUML::Kernel::DataType.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicbehaviors::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicBehaviors::BehavioredClassifier)


def test_fuml::basicbehaviors::behavioredclassifier_constructor_exists():
    assert callable(fUML::BasicBehaviors::BehavioredClassifier.__init__)


def test_fuml::basicbehaviors::behavioredclassifier_constructor_args():
    sig = inspect.signature(fUML::BasicBehaviors::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors::BehavioredClassifier)


def test_basicbehaviors::behavioredclassifier_constructor_exists():
    assert callable(BasicBehaviors::BehavioredClassifier.__init__)


def test_basicbehaviors::behavioredclassifier_constructor_args():
    sig = inspect.signature(BasicBehaviors::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_kernel::parameter_is_not_abstract():
    assert not inspect.isabstract(Kernel::Parameter)


def test_kernel::parameter_constructor_exists():
    assert callable(Kernel::Parameter.__init__)


def test_kernel::parameter_constructor_args():
    sig = inspect.signature(Kernel::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_kernel::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(Kernel::BehavioralFeature)


def test_kernel::behavioralfeature_constructor_exists():
    assert callable(Kernel::BehavioralFeature.__init__)


def test_kernel::behavioralfeature_constructor_args():
    sig = inspect.signature(Kernel::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicbehaviors::behavior_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicBehaviors::Behavior)


def test_fuml::basicbehaviors::behavior_constructor_exists():
    assert callable(fUML::BasicBehaviors::Behavior.__init__)


def test_fuml::basicbehaviors::behavior_constructor_args():
    sig = inspect.signature(fUML::BasicBehaviors::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "reentrant" in params, "Missing parameter 'reentrant'"

def test_fuml::basicbehaviors::behavior_has_reentrant():
    assert hasattr(fUML::BasicBehaviors::Behavior, "reentrant")
    descriptor = None
    for klass in fUML::BasicBehaviors::Behavior.__mro__:
        if "reentrant" in klass.__dict__:
            descriptor = klass.__dict__["reentrant"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicbehaviors::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(fUML::BasicBehaviors::OpaqueBehavior)


def test_fuml::basicbehaviors::opaquebehavior_constructor_exists():
    assert callable(fUML::BasicBehaviors::OpaqueBehavior.__init__)


def test_fuml::basicbehaviors::opaquebehavior_constructor_args():
    sig = inspect.signature(fUML::BasicBehaviors::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_fuml::basicbehaviors::opaquebehavior_has_body():
    assert hasattr(fUML::BasicBehaviors::OpaqueBehavior, "body")
    descriptor = None
    for klass in fUML::BasicBehaviors::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_fuml::basicbehaviors::opaquebehavior_has_language():
    assert hasattr(fUML::BasicBehaviors::OpaqueBehavior, "language")
    descriptor = None
    for klass in fUML::BasicBehaviors::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactivities::activitynode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ActivityNode)


def test_fuml::intermediateactivities::activitynode_constructor_exists():
    assert callable(fUML::IntermediateActivities::ActivityNode.__init__)


def test_fuml::intermediateactivities::activitynode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::activityedge_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::ActivityEdge)


def test_intermediateactivities::activityedge_constructor_exists():
    assert callable(IntermediateActivities::ActivityEdge.__init__)


def test_intermediateactivities::activityedge_constructor_args():
    sig = inspect.signature(IntermediateActivities::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::activity_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::Activity)


def test_fuml::intermediateactivities::activity_constructor_exists():
    assert callable(fUML::IntermediateActivities::Activity.__init__)


def test_fuml::intermediateactivities::activity_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_fuml::intermediateactivities::activity_has_readOnly():
    assert hasattr(fUML::IntermediateActivities::Activity, "readOnly")
    descriptor = None
    for klass in fUML::IntermediateActivities::Activity.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ActivityFinalNode)


def test_fuml::intermediateactivities::activityfinalnode_constructor_exists():
    assert callable(fUML::IntermediateActivities::ActivityFinalNode.__init__)


def test_fuml::intermediateactivities::activityfinalnode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::objectflow_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::ObjectFlow)


def test_intermediateactivities::objectflow_constructor_exists():
    assert callable(IntermediateActivities::ObjectFlow.__init__)


def test_intermediateactivities::objectflow_constructor_args():
    sig = inspect.signature(IntermediateActivities::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_completestructuredactivities::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities::StructuredActivityNode)


def test_completestructuredactivities::structuredactivitynode_constructor_exists():
    assert callable(CompleteStructuredActivities::StructuredActivityNode.__init__)


def test_completestructuredactivities::structuredactivitynode_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::activitynode_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::ActivityNode)


def test_intermediateactivities::activitynode_constructor_exists():
    assert callable(IntermediateActivities::ActivityNode.__init__)


def test_intermediateactivities::activitynode_constructor_args():
    sig = inspect.signature(IntermediateActivities::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::objectnode_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ObjectNode)


def test_fuml::intermediateactivities::objectnode_constructor_exists():
    assert callable(fUML::IntermediateActivities::ObjectNode.__init__)


def test_fuml::intermediateactivities::objectnode_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::activity_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::Activity)


def test_intermediateactivities::activity_constructor_exists():
    assert callable(IntermediateActivities::Activity.__init__)


def test_intermediateactivities::activity_constructor_args():
    sig = inspect.signature(IntermediateActivities::Activity.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::activityedge_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ActivityEdge)


def test_fuml::intermediateactivities::activityedge_constructor_exists():
    assert callable(fUML::IntermediateActivities::ActivityEdge.__init__)


def test_fuml::intermediateactivities::activityedge_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::controlflow_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ControlFlow)


def test_fuml::intermediateactivities::controlflow_constructor_exists():
    assert callable(fUML::IntermediateActivities::ControlFlow.__init__)


def test_fuml::intermediateactivities::controlflow_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::objectflow_is_not_abstract():
    assert not inspect.isabstract(fUML::IntermediateActivities::ObjectFlow)


def test_fuml::intermediateactivities::objectflow_constructor_exists():
    assert callable(fUML::IntermediateActivities::ObjectFlow.__init__)


def test_fuml::intermediateactivities::objectflow_constructor_args():
    sig = inspect.signature(fUML::IntermediateActivities::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_communications::reception_is_not_abstract():
    assert not inspect.isabstract(Communications::Reception)


def test_communications::reception_constructor_exists():
    assert callable(Communications::Reception.__init__)


def test_communications::reception_constructor_args():
    sig = inspect.signature(Communications::Reception.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::class_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::Class)


def test_fuml::kernel::class_constructor_exists():
    assert callable(fUML::Kernel::Class.__init__)


def test_fuml::kernel::class_constructor_args():
    sig = inspect.signature(fUML::Kernel::Class.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_fuml::kernel::class_has_active():
    assert hasattr(fUML::Kernel::Class, "active")
    descriptor = None
    for klass in fUML::Kernel::Class.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_kernel::enumeration_is_not_abstract():
    assert not inspect.isabstract(Kernel::Enumeration)


def test_kernel::enumeration_constructor_exists():
    assert callable(Kernel::Enumeration.__init__)


def test_kernel::enumeration_constructor_args():
    sig = inspect.signature(Kernel::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::EnumerationLiteral)


def test_fuml::kernel::enumerationliteral_constructor_exists():
    assert callable(fUML::Kernel::EnumerationLiteral.__init__)


def test_fuml::kernel::enumerationliteral_constructor_args():
    sig = inspect.signature(fUML::Kernel::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_kernel::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(Kernel::EnumerationLiteral)


def test_kernel::enumerationliteral_constructor_exists():
    assert callable(Kernel::EnumerationLiteral.__init__)


def test_kernel::enumerationliteral_constructor_args():
    sig = inspect.signature(Kernel::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::literalnull_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::LiteralNull)


def test_fuml::kernel::literalnull_constructor_exists():
    assert callable(fUML::Kernel::LiteralNull.__init__)


def test_fuml::kernel::literalnull_constructor_args():
    sig = inspect.signature(fUML::Kernel::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::literalstring_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::LiteralString)


def test_fuml::kernel::literalstring_constructor_exists():
    assert callable(fUML::Kernel::LiteralString.__init__)


def test_fuml::kernel::literalstring_constructor_args():
    sig = inspect.signature(fUML::Kernel::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalstring_has_value():
    assert hasattr(fUML::Kernel::LiteralString, "value")
    descriptor = None
    for klass in fUML::Kernel::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::LiteralUnlimitedNatural)


def test_fuml::kernel::literalunlimitednatural_constructor_exists():
    assert callable(fUML::Kernel::LiteralUnlimitedNatural.__init__)


def test_fuml::kernel::literalunlimitednatural_constructor_args():
    sig = inspect.signature(fUML::Kernel::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalunlimitednatural_has_value():
    assert hasattr(fUML::Kernel::LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in fUML::Kernel::LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::literalinteger_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::LiteralInteger)


def test_fuml::kernel::literalinteger_constructor_exists():
    assert callable(fUML::Kernel::LiteralInteger.__init__)


def test_fuml::kernel::literalinteger_constructor_args():
    sig = inspect.signature(fUML::Kernel::LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalinteger_has_value():
    assert hasattr(fUML::Kernel::LiteralInteger, "value")
    descriptor = None
    for klass in fUML::Kernel::LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::literalboolean_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::LiteralBoolean)


def test_fuml::kernel::literalboolean_constructor_exists():
    assert callable(fUML::Kernel::LiteralBoolean.__init__)


def test_fuml::kernel::literalboolean_constructor_args():
    sig = inspect.signature(fUML::Kernel::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalboolean_has_value():
    assert hasattr(fUML::Kernel::LiteralBoolean, "value")
    descriptor = None
    for klass in fUML::Kernel::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::literalspecification_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::LiteralSpecification)


def test_fuml::kernel::literalspecification_constructor_exists():
    assert callable(fUML::Kernel::LiteralSpecification.__init__)


def test_fuml::kernel::literalspecification_constructor_args():
    sig = inspect.signature(fUML::Kernel::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::instancevalue_is_not_abstract():
    assert not inspect.isabstract(fUML::Kernel::InstanceValue)


def test_fuml::kernel::instancevalue_constructor_exists():
    assert callable(fUML::Kernel::InstanceValue.__init__)


def test_fuml::kernel::instancevalue_constructor_args():
    sig = inspect.signature(fUML::Kernel::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel::instancespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel::InstanceSpecification)


def test_kernel::instancespecification_constructor_exists():
    assert callable(Kernel::InstanceSpecification.__init__)


def test_kernel::instancespecification_constructor_args():
    sig = inspect.signature(Kernel::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "sequential",
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
        "stream",
        "parallel",
        "iterative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

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

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "out",
        "inout",
        "in_",
        "return_",
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
        "public",
        "private",
        "package",
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
fUML::LociL1::SemanticVisitor_strategy = st.builds(
    fUML::LociL1::SemanticVisitor,
)
SemanticVisitor_strategy = st.builds(
    SemanticVisitor,
)
fUML::Kernel::Value_strategy = st.builds(
    fUML::Kernel::Value,
)
Kernel::FeatureValue_strategy = st.builds(
    Kernel::FeatureValue,
)
CompoundValue_strategy = st.builds(
    CompoundValue,
)
fUML::Kernel::DataValue_strategy = st.builds(
    fUML::Kernel::DataValue,
)
fUML::Kernel::ExtensionalValue_strategy = st.builds(
    fUML::Kernel::ExtensionalValue,
)
ExtensionalValue_strategy = st.builds(
    ExtensionalValue,
)
fUML::Kernel::Link_strategy = st.builds(
    fUML::Kernel::Link,
)
fUML::Kernel::Object_strategy = st.builds(
    fUML::Kernel::Object,
)
Kernel::Object_strategy = st.builds(
    Kernel::Object,
)
StructuredValue_strategy = st.builds(
    StructuredValue,
)
fUML::Kernel::CompoundValue_strategy = st.builds(
    fUML::Kernel::CompoundValue,
)
fUML::Kernel::Reference_strategy = st.builds(
    fUML::Kernel::Reference,
)
Kernel::PrimitiveType_strategy = st.builds(
    Kernel::PrimitiveType,
)
PrimitiveValue_strategy = st.builds(
    PrimitiveValue,
)
fUML::Kernel::BooleanValue_strategy = st.builds(
    fUML::Kernel::BooleanValue,
    value=
        st.booleans()
)
fUML::Kernel::IntegerValue_strategy = st.builds(
    fUML::Kernel::IntegerValue,
    value=
        st.integers()
)
fUML::Kernel::UnlimitedNaturalValue_strategy = st.builds(
    fUML::Kernel::UnlimitedNaturalValue,
    value=
        st.integers()
)
Kernel::Value_strategy = st.builds(
    Kernel::Value,
)
fUML::Kernel::FeatureValue_strategy = st.builds(
    fUML::Kernel::FeatureValue,
    position=
        st.integers()
)
Value_strategy = st.builds(
    Value,
)
fUML::Kernel::EnumerationValue_strategy = st.builds(
    fUML::Kernel::EnumerationValue,
)
fUML::Kernel::PrimitiveValue_strategy = st.builds(
    fUML::Kernel::PrimitiveValue,
)
fUML::Kernel::StructuredValue_strategy = st.builds(
    fUML::Kernel::StructuredValue,
)
fUML::Kernel::StringValue_strategy = st.builds(
    fUML::Kernel::StringValue,
    value=
        safe_text
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
fUML::BasicActions::SendSignalAction_strategy = st.builds(
    fUML::BasicActions::SendSignalAction,
)
fUML::BasicActions::CallAction_strategy = st.builds(
    fUML::BasicActions::CallAction,
    synchronous=
        st.booleans()
)
IntermediateActivities::ObjectNode_strategy = st.builds(
    IntermediateActivities::ObjectNode,
)
Pin_strategy = st.builds(
    Pin,
)
fUML::BasicActions::OutputPin_strategy = st.builds(
    fUML::BasicActions::OutputPin,
)
fUML::BasicActions::InputPin_strategy = st.builds(
    fUML::BasicActions::InputPin,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
fUML::BasicActions::Action_strategy = st.builds(
    fUML::BasicActions::Action,
    locallyReentrant=
        st.booleans()
)
Communications::Trigger_strategy = st.builds(
    Communications::Trigger,
)
CallAction_strategy = st.builds(
    CallAction,
)
fUML::BasicActions::CallBehaviorAction_strategy = st.builds(
    fUML::BasicActions::CallBehaviorAction,
)
fUML::BasicActions::CallOperationAction_strategy = st.builds(
    fUML::BasicActions::CallOperationAction,
)
fUML::CompleteActions::StartObjectBehaviorAction_strategy = st.builds(
    fUML::CompleteActions::StartObjectBehaviorAction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
fUML::IntermediateActions::DestroyLinkAction_strategy = st.builds(
    fUML::IntermediateActions::DestroyLinkAction,
)
fUML::IntermediateActions::CreateLinkAction_strategy = st.builds(
    fUML::IntermediateActions::CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
fUML::IntermediateActions::LinkEndDestructionData_strategy = st.builds(
    fUML::IntermediateActions::LinkEndDestructionData,
    destroyDuplicates=
        st.booleans()
)
fUML::IntermediateActions::LinkEndCreationData_strategy = st.builds(
    fUML::IntermediateActions::LinkEndCreationData,
    replaceAll=
        st.booleans()
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
fUML::IntermediateActions::AddStructuralFeatureValueAction_strategy = st.builds(
    fUML::IntermediateActions::AddStructuralFeatureValueAction,
    replaceAll=
        st.booleans()
)
fUML::IntermediateActions::RemoveStructuralFeatureValueAction_strategy = st.builds(
    fUML::IntermediateActions::RemoveStructuralFeatureValueAction,
    removeDuplicates=
        st.booleans()
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
fUML::IntermediateActions::ClearStructuralFeatureAction_strategy = st.builds(
    fUML::IntermediateActions::ClearStructuralFeatureAction,
)
fUML::IntermediateActions::ReadStructuralFeatureAction_strategy = st.builds(
    fUML::IntermediateActions::ReadStructuralFeatureAction,
)
fUML::IntermediateActions::WriteStructuralFeatureAction_strategy = st.builds(
    fUML::IntermediateActions::WriteStructuralFeatureAction,
)
IntermediateActions::LinkEndData_strategy = st.builds(
    IntermediateActions::LinkEndData,
)
ExtraStructuredActivities::ExpansionNode_strategy = st.builds(
    ExtraStructuredActivities::ExpansionNode,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
fUML::IntermediateActions::ReadLinkAction_strategy = st.builds(
    fUML::IntermediateActions::ReadLinkAction,
)
fUML::IntermediateActions::WriteLinkAction_strategy = st.builds(
    fUML::IntermediateActions::WriteLinkAction,
)
ExtraStructuredActivities::ExpansionRegion_strategy = st.builds(
    ExtraStructuredActivities::ExpansionRegion,
)
Action_strategy = st.builds(
    Action,
)
fUML::IntermediateActions::ClearAssociationAction_strategy = st.builds(
    fUML::IntermediateActions::ClearAssociationAction,
)
fUML::BasicActions::InvocationAction_strategy = st.builds(
    fUML::BasicActions::InvocationAction,
)
fUML::IntermediateActions::ValueSpecificationAction_strategy = st.builds(
    fUML::IntermediateActions::ValueSpecificationAction,
)
fUML::IntermediateActions::CreateObjectAction_strategy = st.builds(
    fUML::IntermediateActions::CreateObjectAction,
)
fUML::CompleteActions::AcceptEventAction_strategy = st.builds(
    fUML::CompleteActions::AcceptEventAction,
    unmarshall=
        st.booleans()
)
fUML::IntermediateActions::TestIdentityAction_strategy = st.builds(
    fUML::IntermediateActions::TestIdentityAction,
)
fUML::CompleteActions::ReclassifyObjectAction_strategy = st.builds(
    fUML::CompleteActions::ReclassifyObjectAction,
    replaceAll=
        st.booleans()
)
fUML::IntermediateActions::StructuralFeatureAction_strategy = st.builds(
    fUML::IntermediateActions::StructuralFeatureAction,
)
fUML::CompleteActions::ReduceAction_strategy = st.builds(
    fUML::CompleteActions::ReduceAction,
    ordered=
        st.booleans()
)
fUML::IntermediateActions::ReadSelfAction_strategy = st.builds(
    fUML::IntermediateActions::ReadSelfAction,
)
fUML::CompleteActions::StartClassifierBehaviorAction_strategy = st.builds(
    fUML::CompleteActions::StartClassifierBehaviorAction,
)
fUML::CompleteActions::ReadIsClassifiedObjectAction_strategy = st.builds(
    fUML::CompleteActions::ReadIsClassifiedObjectAction,
    direct=
        st.booleans()
)
fUML::IntermediateActions::DestroyObjectAction_strategy = st.builds(
    fUML::IntermediateActions::DestroyObjectAction,
    destroyLinks=
        st.booleans(),
    destroyOwnedObjects=
        st.booleans()
)
fUML::CompleteActions::ReadExtentAction_strategy = st.builds(
    fUML::CompleteActions::ReadExtentAction,
)
fUML::IntermediateActions::LinkAction_strategy = st.builds(
    fUML::IntermediateActions::LinkAction,
)
fUML::CompleteStructuredActivities::StructuredActivityNode_strategy = st.builds(
    fUML::CompleteStructuredActivities::StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
BasicActions::InputPin_strategy = st.builds(
    BasicActions::InputPin,
)
CompleteStructuredActivities::ExecutableNode_strategy = st.builds(
    CompleteStructuredActivities::ExecutableNode,
)
BasicActions::OutputPin_strategy = st.builds(
    BasicActions::OutputPin,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
fUML::ExtraStructuredActivities::ExpansionRegion_strategy = st.builds(
    fUML::ExtraStructuredActivities::ExpansionRegion,
    mode=
        safe_text
)
fUML::CompleteStructuredActivities::ConditionalNode_strategy = st.builds(
    fUML::CompleteStructuredActivities::ConditionalNode,
    assured=
        st.booleans(),
    determinate=
        st.booleans()
)
fUML::CompleteStructuredActivities::LoopNode_strategy = st.builds(
    fUML::CompleteStructuredActivities::LoopNode,
    testedFirst=
        st.booleans()
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
fUML::ExtraStructuredActivities::ExpansionNode_strategy = st.builds(
    fUML::ExtraStructuredActivities::ExpansionNode,
)
fUML::IntermediateActivities::ActivityParameterNode_strategy = st.builds(
    fUML::IntermediateActivities::ActivityParameterNode,
)
CompleteStructuredActivities::Clause_strategy = st.builds(
    CompleteStructuredActivities::Clause,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
fUML::CompleteStructuredActivities::ExecutableNode_strategy = st.builds(
    fUML::CompleteStructuredActivities::ExecutableNode,
)
fUML::IntermediateActivities::ControlNode_strategy = st.builds(
    fUML::IntermediateActivities::ControlNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
fUML::IntermediateActivities::ForkNode_strategy = st.builds(
    fUML::IntermediateActivities::ForkNode,
)
fUML::IntermediateActivities::InitialNode_strategy = st.builds(
    fUML::IntermediateActivities::InitialNode,
)
fUML::IntermediateActivities::JoinNode_strategy = st.builds(
    fUML::IntermediateActivities::JoinNode,
)
fUML::IntermediateActivities::FinalNode_strategy = st.builds(
    fUML::IntermediateActivities::FinalNode,
)
fUML::IntermediateActivities::DecisionNode_strategy = st.builds(
    fUML::IntermediateActivities::DecisionNode,
)
fUML::IntermediateActivities::MergeNode_strategy = st.builds(
    fUML::IntermediateActivities::MergeNode,
)
Kernel::StructuralFeature_strategy = st.builds(
    Kernel::StructuralFeature,
)
Kernel::Slot_strategy = st.builds(
    Kernel::Slot,
)
Kernel::Operation_strategy = st.builds(
    Kernel::Operation,
)
DataType_strategy = st.builds(
    DataType,
)
fUML::Kernel::Enumeration_strategy = st.builds(
    fUML::Kernel::Enumeration,
)
fUML::Kernel::PrimitiveType_strategy = st.builds(
    fUML::Kernel::PrimitiveType,
)
Feature_strategy = st.builds(
    Feature,
)
fUML::Kernel::BehavioralFeature_strategy = st.builds(
    fUML::Kernel::BehavioralFeature,
    concurrency=
        safe_text,
    abstract=
        st.booleans()
)
Kernel::ValueSpecification_strategy = st.builds(
    Kernel::ValueSpecification,
)
Kernel::Class_strategy = st.builds(
    Kernel::Class,
)
Kernel::DataType_strategy = st.builds(
    Kernel::DataType,
)
Kernel::Association_strategy = st.builds(
    Kernel::Association,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
fUML::Kernel::Property_strategy = st.builds(
    fUML::Kernel::Property,
    aggregation=
        safe_text,
    derivedUnion=
        st.booleans(),
    derived=
        st.booleans(),
    composite=
        st.booleans()
)
Kernel::Generalization_strategy = st.builds(
    Kernel::Generalization,
)
Kernel::RedefinableElement_strategy = st.builds(
    Kernel::RedefinableElement,
)
Kernel::Classifier_strategy = st.builds(
    Kernel::Classifier,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
fUML::Kernel::Feature_strategy = st.builds(
    fUML::Kernel::Feature,
    static=
        st.booleans()
)
Kernel::TypedElement_strategy = st.builds(
    Kernel::TypedElement,
)
Kernel::MultiplicityElement_strategy = st.builds(
    Kernel::MultiplicityElement,
)
fUML::BasicActions::Pin_strategy = st.builds(
    fUML::BasicActions::Pin,
)
fUML::Kernel::Parameter_strategy = st.builds(
    fUML::Kernel::Parameter,
    direction=
        safe_text
)
Kernel::Feature_strategy = st.builds(
    Kernel::Feature,
)
fUML::Kernel::StructuralFeature_strategy = st.builds(
    fUML::Kernel::StructuralFeature,
    readOnly=
        st.booleans()
)
fUML::Kernel::Element_strategy = st.builds(
    fUML::Kernel::Element,
)
Kernel::Package_strategy = st.builds(
    Kernel::Package,
)
Kernel::PackageableElement_strategy = st.builds(
    Kernel::PackageableElement,
)
Kernel::PackageImport_strategy = st.builds(
    Kernel::PackageImport,
)
Kernel::ElementImport_strategy = st.builds(
    Kernel::ElementImport,
)
Kernel::NamedElement_strategy = st.builds(
    Kernel::NamedElement,
)
fUML::Kernel::Comment_strategy = st.builds(
    fUML::Kernel::Comment,
    body=
        safe_text
)
Kernel::Comment_strategy = st.builds(
    Kernel::Comment,
)
Kernel::Element_strategy = st.builds(
    Kernel::Element,
)
Kernel::Namespace_strategy = st.builds(
    Kernel::Namespace,
)
fUML::Kernel::Package_strategy = st.builds(
    fUML::Kernel::Package,
)
Element_strategy = st.builds(
    Element,
)
fUML::Kernel::Generalization_strategy = st.builds(
    fUML::Kernel::Generalization,
    substitutable=
        st.booleans()
)
fUML::CompleteStructuredActivities::Clause_strategy = st.builds(
    fUML::CompleteStructuredActivities::Clause,
)
fUML::IntermediateActions::LinkEndData_strategy = st.builds(
    fUML::IntermediateActions::LinkEndData,
)
fUML::Kernel::PackageImport_strategy = st.builds(
    fUML::Kernel::PackageImport,
    visibility=
        safe_text
)
fUML::Kernel::ElementImport_strategy = st.builds(
    fUML::Kernel::ElementImport,
    alias=
        safe_text,
    visibility=
        safe_text
)
fUML::Kernel::MultiplicityElement_strategy = st.builds(
    fUML::Kernel::MultiplicityElement,
    upper=
        st.integers(),
    lower=
        st.integers(),
    ordered=
        st.booleans(),
    unique=
        st.booleans()
)
fUML::Kernel::Slot_strategy = st.builds(
    fUML::Kernel::Slot,
)
fUML::Kernel::NamedElement_strategy = st.builds(
    fUML::Kernel::NamedElement,
    visibility=
        safe_text,
    name=
        safe_text,
    qualifiedName=
        safe_text
)
Kernel::Type_strategy = st.builds(
    Kernel::Type,
)
fUML::Kernel::Classifier_strategy = st.builds(
    fUML::Kernel::Classifier,
    finalSpecialization=
        st.booleans(),
    abstract=
        st.booleans()
)
TypedElement_strategy = st.builds(
    TypedElement,
)
fUML::Kernel::ValueSpecification_strategy = st.builds(
    fUML::Kernel::ValueSpecification,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
fUML::Kernel::Operation_strategy = st.builds(
    fUML::Kernel::Operation,
    ordered=
        st.booleans(),
    unique=
        st.booleans(),
    lower=
        st.integers(),
    upper=
        st.integers(),
    query=
        st.booleans()
)
fUML::Communications::Reception_strategy = st.builds(
    fUML::Communications::Reception,
)
Event_strategy = st.builds(
    Event,
)
fUML::Communications::MessageEvent_strategy = st.builds(
    fUML::Communications::MessageEvent,
)
Communications::Signal_strategy = st.builds(
    Communications::Signal,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
fUML::Communications::SignalEvent_strategy = st.builds(
    fUML::Communications::SignalEvent,
)
Kernel::Property_strategy = st.builds(
    Kernel::Property,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
fUML::Kernel::Type_strategy = st.builds(
    fUML::Kernel::Type,
)
fUML::Communications::Event_strategy = st.builds(
    fUML::Communications::Event,
)
Communications::Event_strategy = st.builds(
    Communications::Event,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fUML::Kernel::RedefinableElement_strategy = st.builds(
    fUML::Kernel::RedefinableElement,
    leaf=
        st.booleans()
)
fUML::Kernel::PackageableElement_strategy = st.builds(
    fUML::Kernel::PackageableElement,
)
fUML::Kernel::TypedElement_strategy = st.builds(
    fUML::Kernel::TypedElement,
)
fUML::Kernel::Namespace_strategy = st.builds(
    fUML::Kernel::Namespace,
)
fUML::Kernel::InstanceSpecification_strategy = st.builds(
    fUML::Kernel::InstanceSpecification,
)
fUML::Communications::Trigger_strategy = st.builds(
    fUML::Communications::Trigger,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
fUML::BasicBehaviors::FunctionBehavior_strategy = st.builds(
    fUML::BasicBehaviors::FunctionBehavior,
)
BasicBehaviors::Behavior_strategy = st.builds(
    BasicBehaviors::Behavior,
)
Classifier_strategy = st.builds(
    Classifier,
)
fUML::Kernel::Association_strategy = st.builds(
    fUML::Kernel::Association,
    derived=
        st.booleans()
)
fUML::Communications::Signal_strategy = st.builds(
    fUML::Communications::Signal,
)
fUML::Kernel::DataType_strategy = st.builds(
    fUML::Kernel::DataType,
)
fUML::BasicBehaviors::BehavioredClassifier_strategy = st.builds(
    fUML::BasicBehaviors::BehavioredClassifier,
)
BasicBehaviors::BehavioredClassifier_strategy = st.builds(
    BasicBehaviors::BehavioredClassifier,
)
Kernel::Parameter_strategy = st.builds(
    Kernel::Parameter,
)
Kernel::BehavioralFeature_strategy = st.builds(
    Kernel::BehavioralFeature,
)
Class_strategy = st.builds(
    Class,
)
fUML::BasicBehaviors::Behavior_strategy = st.builds(
    fUML::BasicBehaviors::Behavior,
    reentrant=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
fUML::BasicBehaviors::OpaqueBehavior_strategy = st.builds(
    fUML::BasicBehaviors::OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)
fUML::IntermediateActivities::ActivityNode_strategy = st.builds(
    fUML::IntermediateActivities::ActivityNode,
)
IntermediateActivities::ActivityEdge_strategy = st.builds(
    IntermediateActivities::ActivityEdge,
)
fUML::IntermediateActivities::Activity_strategy = st.builds(
    fUML::IntermediateActivities::Activity,
    readOnly=
        st.booleans()
)
FinalNode_strategy = st.builds(
    FinalNode,
)
fUML::IntermediateActivities::ActivityFinalNode_strategy = st.builds(
    fUML::IntermediateActivities::ActivityFinalNode,
)
IntermediateActivities::ObjectFlow_strategy = st.builds(
    IntermediateActivities::ObjectFlow,
)
CompleteStructuredActivities::StructuredActivityNode_strategy = st.builds(
    CompleteStructuredActivities::StructuredActivityNode,
)
IntermediateActivities::ActivityNode_strategy = st.builds(
    IntermediateActivities::ActivityNode,
)
fUML::IntermediateActivities::ObjectNode_strategy = st.builds(
    fUML::IntermediateActivities::ObjectNode,
)
IntermediateActivities::Activity_strategy = st.builds(
    IntermediateActivities::Activity,
)
fUML::IntermediateActivities::ActivityEdge_strategy = st.builds(
    fUML::IntermediateActivities::ActivityEdge,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
fUML::IntermediateActivities::ControlFlow_strategy = st.builds(
    fUML::IntermediateActivities::ControlFlow,
)
fUML::IntermediateActivities::ObjectFlow_strategy = st.builds(
    fUML::IntermediateActivities::ObjectFlow,
)
Communications::Reception_strategy = st.builds(
    Communications::Reception,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
fUML::Kernel::Class_strategy = st.builds(
    fUML::Kernel::Class,
    active=
        st.booleans()
)
Kernel::Enumeration_strategy = st.builds(
    Kernel::Enumeration,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
fUML::Kernel::EnumerationLiteral_strategy = st.builds(
    fUML::Kernel::EnumerationLiteral,
)
Kernel::EnumerationLiteral_strategy = st.builds(
    Kernel::EnumerationLiteral,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
fUML::Kernel::LiteralNull_strategy = st.builds(
    fUML::Kernel::LiteralNull,
)
fUML::Kernel::LiteralString_strategy = st.builds(
    fUML::Kernel::LiteralString,
    value=
        safe_text
)
fUML::Kernel::LiteralUnlimitedNatural_strategy = st.builds(
    fUML::Kernel::LiteralUnlimitedNatural,
    value=
        st.integers()
)
fUML::Kernel::LiteralInteger_strategy = st.builds(
    fUML::Kernel::LiteralInteger,
    value=
        st.integers()
)
fUML::Kernel::LiteralBoolean_strategy = st.builds(
    fUML::Kernel::LiteralBoolean,
    value=
        st.booleans()
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
fUML::Kernel::LiteralSpecification_strategy = st.builds(
    fUML::Kernel::LiteralSpecification,
)
fUML::Kernel::InstanceValue_strategy = st.builds(
    fUML::Kernel::InstanceValue,
)
Kernel::InstanceSpecification_strategy = st.builds(
    Kernel::InstanceSpecification,
)

@given(instance=fUML::LociL1::SemanticVisitor_strategy)
@settings(max_examples=50)
def test_fuml::locil1::semanticvisitor_instantiation(instance):
    assert isinstance(instance, fUML::LociL1::SemanticVisitor)

@given(instance=SemanticVisitor_strategy)
@settings(max_examples=50)
def test_semanticvisitor_instantiation(instance):
    assert isinstance(instance, SemanticVisitor)

@given(instance=fUML::Kernel::Value_strategy)
@settings(max_examples=50)
def test_fuml::kernel::value_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Value)

@given(instance=Kernel::FeatureValue_strategy)
@settings(max_examples=50)
def test_kernel::featurevalue_instantiation(instance):
    assert isinstance(instance, Kernel::FeatureValue)

@given(instance=CompoundValue_strategy)
@settings(max_examples=50)
def test_compoundvalue_instantiation(instance):
    assert isinstance(instance, CompoundValue)

@given(instance=fUML::Kernel::DataValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::datavalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::DataValue)

@given(instance=fUML::Kernel::ExtensionalValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::extensionalvalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::ExtensionalValue)

@given(instance=ExtensionalValue_strategy)
@settings(max_examples=50)
def test_extensionalvalue_instantiation(instance):
    assert isinstance(instance, ExtensionalValue)

@given(instance=fUML::Kernel::Link_strategy)
@settings(max_examples=50)
def test_fuml::kernel::link_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Link)

@given(instance=fUML::Kernel::Object_strategy)
@settings(max_examples=50)
def test_fuml::kernel::object_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Object)

@given(instance=Kernel::Object_strategy)
@settings(max_examples=50)
def test_kernel::object_instantiation(instance):
    assert isinstance(instance, Kernel::Object)

@given(instance=StructuredValue_strategy)
@settings(max_examples=50)
def test_structuredvalue_instantiation(instance):
    assert isinstance(instance, StructuredValue)

@given(instance=fUML::Kernel::CompoundValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::compoundvalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::CompoundValue)

@given(instance=fUML::Kernel::Reference_strategy)
@settings(max_examples=50)
def test_fuml::kernel::reference_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Reference)

@given(instance=Kernel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_kernel::primitivetype_instantiation(instance):
    assert isinstance(instance, Kernel::PrimitiveType)

@given(instance=PrimitiveValue_strategy)
@settings(max_examples=50)
def test_primitivevalue_instantiation(instance):
    assert isinstance(instance, PrimitiveValue)

@given(instance=fUML::Kernel::BooleanValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::booleanvalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::BooleanValue)

@given(instance=fUML::Kernel::BooleanValue_strategy)
def test_fuml::kernel::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fUML::Kernel::BooleanValue_strategy)
def test_fuml::kernel::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML::Kernel::IntegerValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::integervalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::IntegerValue)

@given(instance=fUML::Kernel::IntegerValue_strategy)
def test_fuml::kernel::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fUML::Kernel::IntegerValue_strategy)
def test_fuml::kernel::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML::Kernel::UnlimitedNaturalValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::unlimitednaturalvalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::UnlimitedNaturalValue)

@given(instance=fUML::Kernel::UnlimitedNaturalValue_strategy)
def test_fuml::kernel::unlimitednaturalvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fUML::Kernel::UnlimitedNaturalValue_strategy)
def test_fuml::kernel::unlimitednaturalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel::Value_strategy)
@settings(max_examples=50)
def test_kernel::value_instantiation(instance):
    assert isinstance(instance, Kernel::Value)

@given(instance=fUML::Kernel::FeatureValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::featurevalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::FeatureValue)

@given(instance=fUML::Kernel::FeatureValue_strategy)
def test_fuml::kernel::featurevalue_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=fUML::Kernel::FeatureValue_strategy)
def test_fuml::kernel::featurevalue_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=fUML::Kernel::EnumerationValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::enumerationvalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::EnumerationValue)

@given(instance=fUML::Kernel::PrimitiveValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::primitivevalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::PrimitiveValue)

@given(instance=fUML::Kernel::StructuredValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::structuredvalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::StructuredValue)

@given(instance=fUML::Kernel::StringValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::stringvalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::StringValue)

@given(instance=fUML::Kernel::StringValue_strategy)
def test_fuml::kernel::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fUML::Kernel::StringValue_strategy)
def test_fuml::kernel::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=fUML::BasicActions::SendSignalAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::sendsignalaction_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::SendSignalAction)

@given(instance=fUML::BasicActions::CallAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::callaction_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::CallAction)

@given(instance=fUML::BasicActions::CallAction_strategy)
def test_fuml::basicactions::callaction_synchronous_type(instance):
    assert isinstance(instance.synchronous, bool)


@given(instance=fUML::BasicActions::CallAction_strategy)
def test_fuml::basicactions::callaction_synchronous_setter(instance):
    original = instance.synchronous
    instance.synchronous = original
    assert instance.synchronous == original

@given(instance=IntermediateActivities::ObjectNode_strategy)
@settings(max_examples=50)
def test_intermediateactivities::objectnode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ObjectNode)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=fUML::BasicActions::OutputPin_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::outputpin_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::OutputPin)

@given(instance=fUML::BasicActions::InputPin_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::inputpin_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::InputPin)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=fUML::BasicActions::Action_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::action_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::Action)

@given(instance=fUML::BasicActions::Action_strategy)
def test_fuml::basicactions::action_locallyReentrant_type(instance):
    assert isinstance(instance.locallyReentrant, bool)


@given(instance=fUML::BasicActions::Action_strategy)
def test_fuml::basicactions::action_locallyReentrant_setter(instance):
    original = instance.locallyReentrant
    instance.locallyReentrant = original
    assert instance.locallyReentrant == original

@given(instance=Communications::Trigger_strategy)
@settings(max_examples=50)
def test_communications::trigger_instantiation(instance):
    assert isinstance(instance, Communications::Trigger)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=fUML::BasicActions::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::callbehavioraction_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::CallBehaviorAction)

@given(instance=fUML::BasicActions::CallOperationAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::calloperationaction_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::CallOperationAction)

@given(instance=fUML::CompleteActions::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, fUML::CompleteActions::StartObjectBehaviorAction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=fUML::IntermediateActions::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::destroylinkaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::DestroyLinkAction)

@given(instance=fUML::IntermediateActions::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::createlinkaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::CreateLinkAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=fUML::IntermediateActions::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::LinkEndDestructionData)

@given(instance=fUML::IntermediateActions::LinkEndDestructionData_strategy)
def test_fuml::intermediateactions::linkenddestructiondata_destroyDuplicates_type(instance):
    assert isinstance(instance.destroyDuplicates, bool)


@given(instance=fUML::IntermediateActions::LinkEndDestructionData_strategy)
def test_fuml::intermediateactions::linkenddestructiondata_destroyDuplicates_setter(instance):
    original = instance.destroyDuplicates
    instance.destroyDuplicates = original
    assert instance.destroyDuplicates == original

@given(instance=fUML::IntermediateActions::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::LinkEndCreationData)

@given(instance=fUML::IntermediateActions::LinkEndCreationData_strategy)
def test_fuml::intermediateactions::linkendcreationdata_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=fUML::IntermediateActions::LinkEndCreationData_strategy)
def test_fuml::intermediateactions::linkendcreationdata_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=fUML::IntermediateActions::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::AddStructuralFeatureValueAction)

@given(instance=fUML::IntermediateActions::AddStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::addstructuralfeaturevalueaction_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=fUML::IntermediateActions::AddStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::addstructuralfeaturevalueaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=fUML::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::RemoveStructuralFeatureValueAction)

@given(instance=fUML::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::removestructuralfeaturevalueaction_removeDuplicates_type(instance):
    assert isinstance(instance.removeDuplicates, bool)


@given(instance=fUML::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::removestructuralfeaturevalueaction_removeDuplicates_setter(instance):
    original = instance.removeDuplicates
    instance.removeDuplicates = original
    assert instance.removeDuplicates == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=fUML::IntermediateActions::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::ClearStructuralFeatureAction)

@given(instance=fUML::IntermediateActions::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::ReadStructuralFeatureAction)

@given(instance=fUML::IntermediateActions::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::WriteStructuralFeatureAction)

@given(instance=IntermediateActions::LinkEndData_strategy)
@settings(max_examples=50)
def test_intermediateactions::linkenddata_instantiation(instance):
    assert isinstance(instance, IntermediateActions::LinkEndData)

@given(instance=ExtraStructuredActivities::ExpansionNode_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities::expansionnode_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities::ExpansionNode)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=fUML::IntermediateActions::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::readlinkaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::ReadLinkAction)

@given(instance=fUML::IntermediateActions::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::writelinkaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::WriteLinkAction)

@given(instance=ExtraStructuredActivities::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities::expansionregion_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities::ExpansionRegion)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=fUML::IntermediateActions::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::clearassociationaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::ClearAssociationAction)

@given(instance=fUML::BasicActions::InvocationAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::invocationaction_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::InvocationAction)

@given(instance=fUML::IntermediateActions::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::ValueSpecificationAction)

@given(instance=fUML::IntermediateActions::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::createobjectaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::CreateObjectAction)

@given(instance=fUML::CompleteActions::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::accepteventaction_instantiation(instance):
    assert isinstance(instance, fUML::CompleteActions::AcceptEventAction)

@given(instance=fUML::CompleteActions::AcceptEventAction_strategy)
def test_fuml::completeactions::accepteventaction_unmarshall_type(instance):
    assert isinstance(instance.unmarshall, bool)


@given(instance=fUML::CompleteActions::AcceptEventAction_strategy)
def test_fuml::completeactions::accepteventaction_unmarshall_setter(instance):
    original = instance.unmarshall
    instance.unmarshall = original
    assert instance.unmarshall == original

@given(instance=fUML::IntermediateActions::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::testidentityaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::TestIdentityAction)

@given(instance=fUML::CompleteActions::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, fUML::CompleteActions::ReclassifyObjectAction)

@given(instance=fUML::CompleteActions::ReclassifyObjectAction_strategy)
def test_fuml::completeactions::reclassifyobjectaction_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=fUML::CompleteActions::ReclassifyObjectAction_strategy)
def test_fuml::completeactions::reclassifyobjectaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=fUML::IntermediateActions::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::StructuralFeatureAction)

@given(instance=fUML::CompleteActions::ReduceAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::reduceaction_instantiation(instance):
    assert isinstance(instance, fUML::CompleteActions::ReduceAction)

@given(instance=fUML::CompleteActions::ReduceAction_strategy)
def test_fuml::completeactions::reduceaction_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=fUML::CompleteActions::ReduceAction_strategy)
def test_fuml::completeactions::reduceaction_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fUML::IntermediateActions::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::readselfaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::ReadSelfAction)

@given(instance=fUML::CompleteActions::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, fUML::CompleteActions::StartClassifierBehaviorAction)

@given(instance=fUML::CompleteActions::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, fUML::CompleteActions::ReadIsClassifiedObjectAction)

@given(instance=fUML::CompleteActions::ReadIsClassifiedObjectAction_strategy)
def test_fuml::completeactions::readisclassifiedobjectaction_direct_type(instance):
    assert isinstance(instance.direct, bool)


@given(instance=fUML::CompleteActions::ReadIsClassifiedObjectAction_strategy)
def test_fuml::completeactions::readisclassifiedobjectaction_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original

@given(instance=fUML::IntermediateActions::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::DestroyObjectAction)

@given(instance=fUML::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyLinks_type(instance):
    assert isinstance(instance.destroyLinks, bool)


@given(instance=fUML::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyLinks_setter(instance):
    original = instance.destroyLinks
    instance.destroyLinks = original
    assert instance.destroyLinks == original

@given(instance=fUML::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyOwnedObjects_type(instance):
    assert isinstance(instance.destroyOwnedObjects, bool)


@given(instance=fUML::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyOwnedObjects_setter(instance):
    original = instance.destroyOwnedObjects
    instance.destroyOwnedObjects = original
    assert instance.destroyOwnedObjects == original

@given(instance=fUML::CompleteActions::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::readextentaction_instantiation(instance):
    assert isinstance(instance, fUML::CompleteActions::ReadExtentAction)

@given(instance=fUML::IntermediateActions::LinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkaction_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::LinkAction)

@given(instance=fUML::CompleteStructuredActivities::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, fUML::CompleteStructuredActivities::StructuredActivityNode)

@given(instance=fUML::CompleteStructuredActivities::StructuredActivityNode_strategy)
def test_fuml::completestructuredactivities::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, bool)


@given(instance=fUML::CompleteStructuredActivities::StructuredActivityNode_strategy)
def test_fuml::completestructuredactivities::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=BasicActions::InputPin_strategy)
@settings(max_examples=50)
def test_basicactions::inputpin_instantiation(instance):
    assert isinstance(instance, BasicActions::InputPin)

@given(instance=CompleteStructuredActivities::ExecutableNode_strategy)
@settings(max_examples=50)
def test_completestructuredactivities::executablenode_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities::ExecutableNode)

@given(instance=BasicActions::OutputPin_strategy)
@settings(max_examples=50)
def test_basicactions::outputpin_instantiation(instance):
    assert isinstance(instance, BasicActions::OutputPin)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=fUML::ExtraStructuredActivities::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_fuml::extrastructuredactivities::expansionregion_instantiation(instance):
    assert isinstance(instance, fUML::ExtraStructuredActivities::ExpansionRegion)

@given(instance=fUML::ExtraStructuredActivities::ExpansionRegion_strategy)
def test_fuml::extrastructuredactivities::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=fUML::ExtraStructuredActivities::ExpansionRegion_strategy)
def test_fuml::extrastructuredactivities::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=fUML::CompleteStructuredActivities::ConditionalNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::conditionalnode_instantiation(instance):
    assert isinstance(instance, fUML::CompleteStructuredActivities::ConditionalNode)

@given(instance=fUML::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_assured_type(instance):
    assert isinstance(instance.assured, bool)


@given(instance=fUML::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_assured_setter(instance):
    original = instance.assured
    instance.assured = original
    assert instance.assured == original

@given(instance=fUML::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_determinate_type(instance):
    assert isinstance(instance.determinate, bool)


@given(instance=fUML::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_determinate_setter(instance):
    original = instance.determinate
    instance.determinate = original
    assert instance.determinate == original

@given(instance=fUML::CompleteStructuredActivities::LoopNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::loopnode_instantiation(instance):
    assert isinstance(instance, fUML::CompleteStructuredActivities::LoopNode)

@given(instance=fUML::CompleteStructuredActivities::LoopNode_strategy)
def test_fuml::completestructuredactivities::loopnode_testedFirst_type(instance):
    assert isinstance(instance.testedFirst, bool)


@given(instance=fUML::CompleteStructuredActivities::LoopNode_strategy)
def test_fuml::completestructuredactivities::loopnode_testedFirst_setter(instance):
    original = instance.testedFirst
    instance.testedFirst = original
    assert instance.testedFirst == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=fUML::ExtraStructuredActivities::ExpansionNode_strategy)
@settings(max_examples=50)
def test_fuml::extrastructuredactivities::expansionnode_instantiation(instance):
    assert isinstance(instance, fUML::ExtraStructuredActivities::ExpansionNode)

@given(instance=fUML::IntermediateActivities::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activityparameternode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ActivityParameterNode)

@given(instance=CompleteStructuredActivities::Clause_strategy)
@settings(max_examples=50)
def test_completestructuredactivities::clause_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities::Clause)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=fUML::CompleteStructuredActivities::ExecutableNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::executablenode_instantiation(instance):
    assert isinstance(instance, fUML::CompleteStructuredActivities::ExecutableNode)

@given(instance=fUML::IntermediateActivities::ControlNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::controlnode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ControlNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=fUML::IntermediateActivities::ForkNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::forknode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ForkNode)

@given(instance=fUML::IntermediateActivities::InitialNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::initialnode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::InitialNode)

@given(instance=fUML::IntermediateActivities::JoinNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::joinnode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::JoinNode)

@given(instance=fUML::IntermediateActivities::FinalNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::finalnode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::FinalNode)

@given(instance=fUML::IntermediateActivities::DecisionNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::decisionnode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::DecisionNode)

@given(instance=fUML::IntermediateActivities::MergeNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::mergenode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::MergeNode)

@given(instance=Kernel::StructuralFeature_strategy)
@settings(max_examples=50)
def test_kernel::structuralfeature_instantiation(instance):
    assert isinstance(instance, Kernel::StructuralFeature)

@given(instance=Kernel::Slot_strategy)
@settings(max_examples=50)
def test_kernel::slot_instantiation(instance):
    assert isinstance(instance, Kernel::Slot)

@given(instance=Kernel::Operation_strategy)
@settings(max_examples=50)
def test_kernel::operation_instantiation(instance):
    assert isinstance(instance, Kernel::Operation)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=fUML::Kernel::Enumeration_strategy)
@settings(max_examples=50)
def test_fuml::kernel::enumeration_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Enumeration)

@given(instance=fUML::Kernel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_fuml::kernel::primitivetype_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::PrimitiveType)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=fUML::Kernel::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_fuml::kernel::behavioralfeature_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::BehavioralFeature)

@given(instance=fUML::Kernel::BehavioralFeature_strategy)
def test_fuml::kernel::behavioralfeature_concurrency_type(instance):
    assert isinstance(instance.concurrency, str)


@given(instance=fUML::Kernel::BehavioralFeature_strategy)
def test_fuml::kernel::behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=fUML::Kernel::BehavioralFeature_strategy)
def test_fuml::kernel::behavioralfeature_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=fUML::Kernel::BehavioralFeature_strategy)
def test_fuml::kernel::behavioralfeature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=Kernel::ValueSpecification_strategy)
@settings(max_examples=50)
def test_kernel::valuespecification_instantiation(instance):
    assert isinstance(instance, Kernel::ValueSpecification)

@given(instance=Kernel::Class_strategy)
@settings(max_examples=50)
def test_kernel::class_instantiation(instance):
    assert isinstance(instance, Kernel::Class)

@given(instance=Kernel::DataType_strategy)
@settings(max_examples=50)
def test_kernel::datatype_instantiation(instance):
    assert isinstance(instance, Kernel::DataType)

@given(instance=Kernel::Association_strategy)
@settings(max_examples=50)
def test_kernel::association_instantiation(instance):
    assert isinstance(instance, Kernel::Association)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=fUML::Kernel::Property_strategy)
@settings(max_examples=50)
def test_fuml::kernel::property_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Property)

@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_derivedUnion_type(instance):
    assert isinstance(instance.derivedUnion, bool)


@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_derivedUnion_setter(instance):
    original = instance.derivedUnion
    instance.derivedUnion = original
    assert instance.derivedUnion == original

@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_composite_type(instance):
    assert isinstance(instance.composite, bool)


@given(instance=fUML::Kernel::Property_strategy)
def test_fuml::kernel::property_composite_setter(instance):
    original = instance.composite
    instance.composite = original
    assert instance.composite == original

@given(instance=Kernel::Generalization_strategy)
@settings(max_examples=50)
def test_kernel::generalization_instantiation(instance):
    assert isinstance(instance, Kernel::Generalization)

@given(instance=Kernel::RedefinableElement_strategy)
@settings(max_examples=50)
def test_kernel::redefinableelement_instantiation(instance):
    assert isinstance(instance, Kernel::RedefinableElement)

@given(instance=Kernel::Classifier_strategy)
@settings(max_examples=50)
def test_kernel::classifier_instantiation(instance):
    assert isinstance(instance, Kernel::Classifier)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=fUML::Kernel::Feature_strategy)
@settings(max_examples=50)
def test_fuml::kernel::feature_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Feature)

@given(instance=fUML::Kernel::Feature_strategy)
def test_fuml::kernel::feature_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=fUML::Kernel::Feature_strategy)
def test_fuml::kernel::feature_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Kernel::TypedElement_strategy)
@settings(max_examples=50)
def test_kernel::typedelement_instantiation(instance):
    assert isinstance(instance, Kernel::TypedElement)

@given(instance=Kernel::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_kernel::multiplicityelement_instantiation(instance):
    assert isinstance(instance, Kernel::MultiplicityElement)

@given(instance=fUML::BasicActions::Pin_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::pin_instantiation(instance):
    assert isinstance(instance, fUML::BasicActions::Pin)

@given(instance=fUML::Kernel::Parameter_strategy)
@settings(max_examples=50)
def test_fuml::kernel::parameter_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Parameter)

@given(instance=fUML::Kernel::Parameter_strategy)
def test_fuml::kernel::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=fUML::Kernel::Parameter_strategy)
def test_fuml::kernel::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Kernel::Feature_strategy)
@settings(max_examples=50)
def test_kernel::feature_instantiation(instance):
    assert isinstance(instance, Kernel::Feature)

@given(instance=fUML::Kernel::StructuralFeature_strategy)
@settings(max_examples=50)
def test_fuml::kernel::structuralfeature_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::StructuralFeature)

@given(instance=fUML::Kernel::StructuralFeature_strategy)
def test_fuml::kernel::structuralfeature_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=fUML::Kernel::StructuralFeature_strategy)
def test_fuml::kernel::structuralfeature_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=fUML::Kernel::Element_strategy)
@settings(max_examples=50)
def test_fuml::kernel::element_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Element)

@given(instance=Kernel::Package_strategy)
@settings(max_examples=50)
def test_kernel::package_instantiation(instance):
    assert isinstance(instance, Kernel::Package)

@given(instance=Kernel::PackageableElement_strategy)
@settings(max_examples=50)
def test_kernel::packageableelement_instantiation(instance):
    assert isinstance(instance, Kernel::PackageableElement)

@given(instance=Kernel::PackageImport_strategy)
@settings(max_examples=50)
def test_kernel::packageimport_instantiation(instance):
    assert isinstance(instance, Kernel::PackageImport)

@given(instance=Kernel::ElementImport_strategy)
@settings(max_examples=50)
def test_kernel::elementimport_instantiation(instance):
    assert isinstance(instance, Kernel::ElementImport)

@given(instance=Kernel::NamedElement_strategy)
@settings(max_examples=50)
def test_kernel::namedelement_instantiation(instance):
    assert isinstance(instance, Kernel::NamedElement)

@given(instance=fUML::Kernel::Comment_strategy)
@settings(max_examples=50)
def test_fuml::kernel::comment_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Comment)

@given(instance=fUML::Kernel::Comment_strategy)
def test_fuml::kernel::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=fUML::Kernel::Comment_strategy)
def test_fuml::kernel::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Kernel::Comment_strategy)
@settings(max_examples=50)
def test_kernel::comment_instantiation(instance):
    assert isinstance(instance, Kernel::Comment)

@given(instance=Kernel::Element_strategy)
@settings(max_examples=50)
def test_kernel::element_instantiation(instance):
    assert isinstance(instance, Kernel::Element)

@given(instance=Kernel::Namespace_strategy)
@settings(max_examples=50)
def test_kernel::namespace_instantiation(instance):
    assert isinstance(instance, Kernel::Namespace)

@given(instance=fUML::Kernel::Package_strategy)
@settings(max_examples=50)
def test_fuml::kernel::package_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Package)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=fUML::Kernel::Generalization_strategy)
@settings(max_examples=50)
def test_fuml::kernel::generalization_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Generalization)

@given(instance=fUML::Kernel::Generalization_strategy)
def test_fuml::kernel::generalization_substitutable_type(instance):
    assert isinstance(instance.substitutable, bool)


@given(instance=fUML::Kernel::Generalization_strategy)
def test_fuml::kernel::generalization_substitutable_setter(instance):
    original = instance.substitutable
    instance.substitutable = original
    assert instance.substitutable == original

@given(instance=fUML::CompleteStructuredActivities::Clause_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::clause_instantiation(instance):
    assert isinstance(instance, fUML::CompleteStructuredActivities::Clause)

@given(instance=fUML::IntermediateActions::LinkEndData_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkenddata_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActions::LinkEndData)

@given(instance=fUML::Kernel::PackageImport_strategy)
@settings(max_examples=50)
def test_fuml::kernel::packageimport_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::PackageImport)

@given(instance=fUML::Kernel::PackageImport_strategy)
def test_fuml::kernel::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=fUML::Kernel::PackageImport_strategy)
def test_fuml::kernel::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=fUML::Kernel::ElementImport_strategy)
@settings(max_examples=50)
def test_fuml::kernel::elementimport_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::ElementImport)

@given(instance=fUML::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=fUML::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=fUML::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=fUML::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=fUML::Kernel::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::multiplicityelement_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::MultiplicityElement)

@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=fUML::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=fUML::Kernel::Slot_strategy)
@settings(max_examples=50)
def test_fuml::kernel::slot_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Slot)

@given(instance=fUML::Kernel::NamedElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::namedelement_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::NamedElement)

@given(instance=fUML::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=fUML::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=fUML::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fUML::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fUML::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=fUML::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=Kernel::Type_strategy)
@settings(max_examples=50)
def test_kernel::type_instantiation(instance):
    assert isinstance(instance, Kernel::Type)

@given(instance=fUML::Kernel::Classifier_strategy)
@settings(max_examples=50)
def test_fuml::kernel::classifier_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Classifier)

@given(instance=fUML::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_finalSpecialization_type(instance):
    assert isinstance(instance.finalSpecialization, bool)


@given(instance=fUML::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_finalSpecialization_setter(instance):
    original = instance.finalSpecialization
    instance.finalSpecialization = original
    assert instance.finalSpecialization == original

@given(instance=fUML::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=fUML::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=fUML::Kernel::ValueSpecification_strategy)
@settings(max_examples=50)
def test_fuml::kernel::valuespecification_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::ValueSpecification)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=fUML::Kernel::Operation_strategy)
@settings(max_examples=50)
def test_fuml::kernel::operation_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Operation)

@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_query_type(instance):
    assert isinstance(instance.query, bool)


@given(instance=fUML::Kernel::Operation_strategy)
def test_fuml::kernel::operation_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=fUML::Communications::Reception_strategy)
@settings(max_examples=50)
def test_fuml::communications::reception_instantiation(instance):
    assert isinstance(instance, fUML::Communications::Reception)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=fUML::Communications::MessageEvent_strategy)
@settings(max_examples=50)
def test_fuml::communications::messageevent_instantiation(instance):
    assert isinstance(instance, fUML::Communications::MessageEvent)

@given(instance=Communications::Signal_strategy)
@settings(max_examples=50)
def test_communications::signal_instantiation(instance):
    assert isinstance(instance, Communications::Signal)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=fUML::Communications::SignalEvent_strategy)
@settings(max_examples=50)
def test_fuml::communications::signalevent_instantiation(instance):
    assert isinstance(instance, fUML::Communications::SignalEvent)

@given(instance=Kernel::Property_strategy)
@settings(max_examples=50)
def test_kernel::property_instantiation(instance):
    assert isinstance(instance, Kernel::Property)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=fUML::Kernel::Type_strategy)
@settings(max_examples=50)
def test_fuml::kernel::type_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Type)

@given(instance=fUML::Communications::Event_strategy)
@settings(max_examples=50)
def test_fuml::communications::event_instantiation(instance):
    assert isinstance(instance, fUML::Communications::Event)

@given(instance=Communications::Event_strategy)
@settings(max_examples=50)
def test_communications::event_instantiation(instance):
    assert isinstance(instance, Communications::Event)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fUML::Kernel::RedefinableElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::redefinableelement_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::RedefinableElement)

@given(instance=fUML::Kernel::RedefinableElement_strategy)
def test_fuml::kernel::redefinableelement_leaf_type(instance):
    assert isinstance(instance.leaf, bool)


@given(instance=fUML::Kernel::RedefinableElement_strategy)
def test_fuml::kernel::redefinableelement_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original

@given(instance=fUML::Kernel::PackageableElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::packageableelement_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::PackageableElement)

@given(instance=fUML::Kernel::TypedElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::typedelement_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::TypedElement)

@given(instance=fUML::Kernel::Namespace_strategy)
@settings(max_examples=50)
def test_fuml::kernel::namespace_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Namespace)

@given(instance=fUML::Kernel::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_fuml::kernel::instancespecification_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::InstanceSpecification)

@given(instance=fUML::Communications::Trigger_strategy)
@settings(max_examples=50)
def test_fuml::communications::trigger_instantiation(instance):
    assert isinstance(instance, fUML::Communications::Trigger)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=fUML::BasicBehaviors::FunctionBehavior_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::functionbehavior_instantiation(instance):
    assert isinstance(instance, fUML::BasicBehaviors::FunctionBehavior)

@given(instance=BasicBehaviors::Behavior_strategy)
@settings(max_examples=50)
def test_basicbehaviors::behavior_instantiation(instance):
    assert isinstance(instance, BasicBehaviors::Behavior)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=fUML::Kernel::Association_strategy)
@settings(max_examples=50)
def test_fuml::kernel::association_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Association)

@given(instance=fUML::Kernel::Association_strategy)
def test_fuml::kernel::association_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=fUML::Kernel::Association_strategy)
def test_fuml::kernel::association_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=fUML::Communications::Signal_strategy)
@settings(max_examples=50)
def test_fuml::communications::signal_instantiation(instance):
    assert isinstance(instance, fUML::Communications::Signal)

@given(instance=fUML::Kernel::DataType_strategy)
@settings(max_examples=50)
def test_fuml::kernel::datatype_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::DataType)

@given(instance=fUML::BasicBehaviors::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, fUML::BasicBehaviors::BehavioredClassifier)

@given(instance=BasicBehaviors::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_basicbehaviors::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BasicBehaviors::BehavioredClassifier)

@given(instance=Kernel::Parameter_strategy)
@settings(max_examples=50)
def test_kernel::parameter_instantiation(instance):
    assert isinstance(instance, Kernel::Parameter)

@given(instance=Kernel::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_kernel::behavioralfeature_instantiation(instance):
    assert isinstance(instance, Kernel::BehavioralFeature)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=fUML::BasicBehaviors::Behavior_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::behavior_instantiation(instance):
    assert isinstance(instance, fUML::BasicBehaviors::Behavior)

@given(instance=fUML::BasicBehaviors::Behavior_strategy)
def test_fuml::basicbehaviors::behavior_reentrant_type(instance):
    assert isinstance(instance.reentrant, bool)


@given(instance=fUML::BasicBehaviors::Behavior_strategy)
def test_fuml::basicbehaviors::behavior_reentrant_setter(instance):
    original = instance.reentrant
    instance.reentrant = original
    assert instance.reentrant == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=fUML::BasicBehaviors::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::opaquebehavior_instantiation(instance):
    assert isinstance(instance, fUML::BasicBehaviors::OpaqueBehavior)

@given(instance=fUML::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=fUML::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=fUML::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=fUML::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=fUML::IntermediateActivities::ActivityNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activitynode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ActivityNode)

@given(instance=IntermediateActivities::ActivityEdge_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activityedge_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ActivityEdge)

@given(instance=fUML::IntermediateActivities::Activity_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activity_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::Activity)

@given(instance=fUML::IntermediateActivities::Activity_strategy)
def test_fuml::intermediateactivities::activity_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=fUML::IntermediateActivities::Activity_strategy)
def test_fuml::intermediateactivities::activity_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=fUML::IntermediateActivities::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activityfinalnode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ActivityFinalNode)

@given(instance=IntermediateActivities::ObjectFlow_strategy)
@settings(max_examples=50)
def test_intermediateactivities::objectflow_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ObjectFlow)

@given(instance=CompleteStructuredActivities::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_completestructuredactivities::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities::StructuredActivityNode)

@given(instance=IntermediateActivities::ActivityNode_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activitynode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ActivityNode)

@given(instance=fUML::IntermediateActivities::ObjectNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::objectnode_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ObjectNode)

@given(instance=IntermediateActivities::Activity_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activity_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::Activity)

@given(instance=fUML::IntermediateActivities::ActivityEdge_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activityedge_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ActivityEdge)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=fUML::IntermediateActivities::ControlFlow_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::controlflow_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ControlFlow)

@given(instance=fUML::IntermediateActivities::ObjectFlow_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::objectflow_instantiation(instance):
    assert isinstance(instance, fUML::IntermediateActivities::ObjectFlow)

@given(instance=Communications::Reception_strategy)
@settings(max_examples=50)
def test_communications::reception_instantiation(instance):
    assert isinstance(instance, Communications::Reception)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=fUML::Kernel::Class_strategy)
@settings(max_examples=50)
def test_fuml::kernel::class_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::Class)

@given(instance=fUML::Kernel::Class_strategy)
def test_fuml::kernel::class_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=fUML::Kernel::Class_strategy)
def test_fuml::kernel::class_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=Kernel::Enumeration_strategy)
@settings(max_examples=50)
def test_kernel::enumeration_instantiation(instance):
    assert isinstance(instance, Kernel::Enumeration)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=fUML::Kernel::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_fuml::kernel::enumerationliteral_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::EnumerationLiteral)

@given(instance=Kernel::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_kernel::enumerationliteral_instantiation(instance):
    assert isinstance(instance, Kernel::EnumerationLiteral)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=fUML::Kernel::LiteralNull_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalnull_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::LiteralNull)

@given(instance=fUML::Kernel::LiteralString_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalstring_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::LiteralString)

@given(instance=fUML::Kernel::LiteralString_strategy)
def test_fuml::kernel::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fUML::Kernel::LiteralString_strategy)
def test_fuml::kernel::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML::Kernel::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::LiteralUnlimitedNatural)

@given(instance=fUML::Kernel::LiteralUnlimitedNatural_strategy)
def test_fuml::kernel::literalunlimitednatural_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fUML::Kernel::LiteralUnlimitedNatural_strategy)
def test_fuml::kernel::literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML::Kernel::LiteralInteger_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalinteger_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::LiteralInteger)

@given(instance=fUML::Kernel::LiteralInteger_strategy)
def test_fuml::kernel::literalinteger_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fUML::Kernel::LiteralInteger_strategy)
def test_fuml::kernel::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML::Kernel::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalboolean_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::LiteralBoolean)

@given(instance=fUML::Kernel::LiteralBoolean_strategy)
def test_fuml::kernel::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fUML::Kernel::LiteralBoolean_strategy)
def test_fuml::kernel::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=fUML::Kernel::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalspecification_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::LiteralSpecification)

@given(instance=fUML::Kernel::InstanceValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::instancevalue_instantiation(instance):
    assert isinstance(instance, fUML::Kernel::InstanceValue)

@given(instance=Kernel::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_kernel::instancespecification_instantiation(instance):
    assert isinstance(instance, Kernel::InstanceSpecification)

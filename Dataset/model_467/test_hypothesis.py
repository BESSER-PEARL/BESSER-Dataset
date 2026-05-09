import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fuml::BasicBehaviors::ParameterValue,
    Kernel::ExtensionalValue,
    fuml::LociL1::Locus,
    fuml::LociL1::SemanticVisitor,
    SemanticVisitor,
    fuml::Kernel::Value,
    LociL1::Locus,
    CompoundValue,
    fuml::Kernel::DataValue,
    fuml::Kernel::ExtensionalValue,
    ExtensionalValue,
    fuml::Kernel::Object,
    Kernel::Object,
    StructuredValue,
    fuml::Kernel::CompoundValue,
    fuml::Kernel::Reference,
    Kernel::PrimitiveType,
    PrimitiveValue,
    fuml::Kernel::IntegerValue,
    fuml::Kernel::StringValue,
    fuml::Kernel::BooleanValue,
    fuml::Kernel::UnlimitedNaturalValue,
    Kernel::Value,
    fuml::Kernel::FeatureValue,
    fuml::Kernel::Link,
    Kernel::FeatureValue,
    InvocationAction,
    fuml::BasicActions::SendSignalAction,
    fuml::BasicActions::CallAction,
    IntermediateActivities::ObjectNode,
    Pin,
    fuml::BasicActions::OutputPin,
    fuml::BasicActions::InputPin,
    Value,
    fuml::Kernel::EnumerationValue,
    fuml::Kernel::PrimitiveValue,
    fuml::Kernel::StructuredValue,
    ExecutableNode,
    fuml::BasicActions::Action,
    Communications::Trigger,
    CallAction,
    fuml::BasicActions::CallOperationAction,
    fuml::BasicActions::CallBehaviorAction,
    fuml::CompleteActions::StartObjectBehaviorAction,
    WriteLinkAction,
    fuml::IntermediateActions::DestroyLinkAction,
    fuml::IntermediateActions::CreateLinkAction,
    LinkEndData,
    fuml::IntermediateActions::LinkEndDestructionData,
    fuml::IntermediateActions::LinkEndCreationData,
    WriteStructuralFeatureAction,
    fuml::IntermediateActions::AddStructuralFeatureValueAction,
    fuml::IntermediateActions::RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    fuml::IntermediateActions::ReadStructuralFeatureAction,
    fuml::IntermediateActions::ClearStructuralFeatureAction,
    fuml::IntermediateActions::WriteStructuralFeatureAction,
    IntermediateActions::LinkEndData,
    LinkAction,
    fuml::IntermediateActions::ReadLinkAction,
    fuml::IntermediateActions::WriteLinkAction,
    ExtraStructuredActivities::ExpansionNode,
    ExtraStructuredActivities::ExpansionRegion,
    Action,
    fuml::CompleteActions::AcceptEventAction,
    fuml::IntermediateActions::CreateObjectAction,
    fuml::CompleteActions::ReduceAction,
    fuml::BasicActions::InvocationAction,
    fuml::CompleteActions::ReadIsClassifiedObjectAction,
    fuml::IntermediateActions::ReadSelfAction,
    fuml::CompleteActions::ReadExtentAction,
    fuml::CompleteActions::StartClassifierBehaviorAction,
    fuml::IntermediateActions::TestIdentityAction,
    fuml::IntermediateActions::ClearAssociationAction,
    fuml::IntermediateActions::ValueSpecificationAction,
    fuml::IntermediateActions::StructuralFeatureAction,
    fuml::IntermediateActions::DestroyObjectAction,
    fuml::IntermediateActions::LinkAction,
    fuml::CompleteActions::ReclassifyObjectAction,
    fuml::CompleteStructuredActivities::StructuredActivityNode,
    CompleteStructuredActivities::Clause,
    BasicActions::InputPin,
    CompleteStructuredActivities::ExecutableNode,
    BasicActions::OutputPin,
    StructuredActivityNode,
    fuml::ExtraStructuredActivities::ExpansionRegion,
    fuml::CompleteStructuredActivities::ConditionalNode,
    fuml::CompleteStructuredActivities::LoopNode,
    ObjectNode,
    fuml::ExtraStructuredActivities::ExpansionNode,
    fuml::IntermediateActivities::ActivityParameterNode,
    FinalNode,
    fuml::IntermediateActivities::ActivityFinalNode,
    IntermediateActivities::ObjectFlow,
    ActivityNode,
    fuml::CompleteStructuredActivities::ExecutableNode,
    fuml::IntermediateActivities::ControlNode,
    ControlNode,
    fuml::IntermediateActivities::ForkNode,
    fuml::IntermediateActivities::FinalNode,
    fuml::IntermediateActivities::InitialNode,
    fuml::IntermediateActivities::JoinNode,
    fuml::IntermediateActivities::DecisionNode,
    fuml::IntermediateActivities::MergeNode,
    IntermediateActivities::ActivityEdge,
    CompleteStructuredActivities::StructuredActivityNode,
    IntermediateActivities::ActivityNode,
    IntermediateActivities::Activity,
    ActivityEdge,
    fuml::IntermediateActivities::ControlFlow,
    fuml::IntermediateActivities::ObjectFlow,
    LiteralSpecification,
    fuml::Kernel::LiteralBoolean,
    Communications::Reception,
    BehavioredClassifier,
    fuml::Kernel::Class,
    Kernel::Enumeration,
    InstanceSpecification,
    fuml::Kernel::EnumerationLiteral,
    Kernel::EnumerationLiteral,
    DataType,
    fuml::Kernel::Enumeration,
    fuml::Kernel::PrimitiveType,
    fuml::Kernel::LiteralUnlimitedNatural,
    fuml::Kernel::LiteralString,
    fuml::Kernel::LiteralNull,
    fuml::Kernel::LiteralInteger,
    ValueSpecification,
    fuml::Kernel::LiteralSpecification,
    fuml::Kernel::InstanceValue,
    Kernel::InstanceSpecification,
    Kernel::StructuralFeature,
    Kernel::Slot,
    Kernel::Operation,
    Feature,
    fuml::Kernel::BehavioralFeature,
    Kernel::ValueSpecification,
    Kernel::Class,
    Kernel::DataType,
    Kernel::Association,
    StructuralFeature,
    fuml::Kernel::Property,
    Kernel::Generalization,
    Kernel::RedefinableElement,
    Kernel::Classifier,
    RedefinableElement,
    fuml::IntermediateActivities::ActivityNode,
    fuml::IntermediateActivities::ActivityEdge,
    fuml::Kernel::Feature,
    Kernel::TypedElement,
    fuml::IntermediateActivities::ObjectNode,
    Kernel::MultiplicityElement,
    fuml::BasicActions::Pin,
    fuml::Kernel::Parameter,
    Kernel::Feature,
    fuml::Kernel::StructuralFeature,
    Kernel::Package,
    Kernel::PackageableElement,
    Kernel::PackageImport,
    Kernel::ElementImport,
    Kernel::NamedElement,
    fuml::Kernel::Comment,
    Kernel::Comment,
    Kernel::Element,
    fuml::Kernel::Element,
    Kernel::Namespace,
    fuml::Kernel::Package,
    Element,
    fuml::IntermediateActions::LinkEndData,
    fuml::Kernel::MultiplicityElement,
    fuml::Kernel::ElementImport,
    fuml::CompleteStructuredActivities::Clause,
    fuml::Kernel::Slot,
    fuml::Kernel::PackageImport,
    fuml::Kernel::Generalization,
    fuml::Kernel::NamedElement,
    Kernel::Type,
    fuml::Kernel::Classifier,
    TypedElement,
    fuml::Kernel::ValueSpecification,
    BehavioralFeature,
    fuml::Kernel::Operation,
    fuml::Communications::Reception,
    Event,
    fuml::Communications::MessageEvent,
    Communications::Signal,
    MessageEvent,
    fuml::Communications::SignalEvent,
    Kernel::Property,
    PackageableElement,
    fuml::Kernel::Type,
    fuml::Communications::Event,
    Communications::Event,
    NamedElement,
    fuml::Kernel::InstanceSpecification,
    fuml::Kernel::TypedElement,
    fuml::Kernel::Namespace,
    fuml::Kernel::PackageableElement,
    fuml::Kernel::RedefinableElement,
    fuml::Communications::Trigger,
    OpaqueBehavior,
    fuml::BasicBehaviors::FunctionBehavior,
    BasicBehaviors::Behavior,
    Classifier,
    fuml::Kernel::Association,
    fuml::Kernel::DataType,
    fuml::Communications::Signal,
    fuml::BasicBehaviors::BehavioredClassifier,
    BasicBehaviors::BehavioredClassifier,
    Kernel::Parameter,
    Kernel::BehavioralFeature,
    Class,
    fuml::BasicBehaviors::Behavior,
    Behavior,
    fuml::IntermediateActivities::Activity,
    fuml::BasicBehaviors::OpaqueBehavior,
    VisibilityKind,
    ExpansionKind,
    AggregationKind,
    ParameterDirectionKind,
    CallConcurrencyKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fuml::basicbehaviors::parametervalue_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicBehaviors::ParameterValue)


def test_fuml::basicbehaviors::parametervalue_constructor_exists():
    assert callable(fuml::BasicBehaviors::ParameterValue.__init__)


def test_fuml::basicbehaviors::parametervalue_constructor_args():
    sig = inspect.signature(fuml::BasicBehaviors::ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel::extensionalvalue_is_not_abstract():
    assert not inspect.isabstract(Kernel::ExtensionalValue)


def test_kernel::extensionalvalue_constructor_exists():
    assert callable(Kernel::ExtensionalValue.__init__)


def test_kernel::extensionalvalue_constructor_args():
    sig = inspect.signature(Kernel::ExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::locil1::locus_is_not_abstract():
    assert not inspect.isabstract(fuml::LociL1::Locus)


def test_fuml::locil1::locus_constructor_exists():
    assert callable(fuml::LociL1::Locus.__init__)


def test_fuml::locil1::locus_constructor_args():
    sig = inspect.signature(fuml::LociL1::Locus.__init__)
    params = list(sig.parameters.keys())



def test_fuml::locil1::semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(fuml::LociL1::SemanticVisitor)


def test_fuml::locil1::semanticvisitor_constructor_exists():
    assert callable(fuml::LociL1::SemanticVisitor.__init__)


def test_fuml::locil1::semanticvisitor_constructor_args():
    sig = inspect.signature(fuml::LociL1::SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(SemanticVisitor)


def test_semanticvisitor_constructor_exists():
    assert callable(SemanticVisitor.__init__)


def test_semanticvisitor_constructor_args():
    sig = inspect.signature(SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::value_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Value)


def test_fuml::kernel::value_constructor_exists():
    assert callable(fuml::Kernel::Value.__init__)


def test_fuml::kernel::value_constructor_args():
    sig = inspect.signature(fuml::Kernel::Value.__init__)
    params = list(sig.parameters.keys())



def test_locil1::locus_is_not_abstract():
    assert not inspect.isabstract(LociL1::Locus)


def test_locil1::locus_constructor_exists():
    assert callable(LociL1::Locus.__init__)


def test_locil1::locus_constructor_args():
    sig = inspect.signature(LociL1::Locus.__init__)
    params = list(sig.parameters.keys())



def test_compoundvalue_is_not_abstract():
    assert not inspect.isabstract(CompoundValue)


def test_compoundvalue_constructor_exists():
    assert callable(CompoundValue.__init__)


def test_compoundvalue_constructor_args():
    sig = inspect.signature(CompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::datavalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::DataValue)


def test_fuml::kernel::datavalue_constructor_exists():
    assert callable(fuml::Kernel::DataValue.__init__)


def test_fuml::kernel::datavalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::DataValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::extensionalvalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::ExtensionalValue)


def test_fuml::kernel::extensionalvalue_constructor_exists():
    assert callable(fuml::Kernel::ExtensionalValue.__init__)


def test_fuml::kernel::extensionalvalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::ExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_extensionalvalue_is_not_abstract():
    assert not inspect.isabstract(ExtensionalValue)


def test_extensionalvalue_constructor_exists():
    assert callable(ExtensionalValue.__init__)


def test_extensionalvalue_constructor_args():
    sig = inspect.signature(ExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::object_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Object)


def test_fuml::kernel::object_constructor_exists():
    assert callable(fuml::Kernel::Object.__init__)


def test_fuml::kernel::object_constructor_args():
    sig = inspect.signature(fuml::Kernel::Object.__init__)
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
    assert not inspect.isabstract(fuml::Kernel::CompoundValue)


def test_fuml::kernel::compoundvalue_constructor_exists():
    assert callable(fuml::Kernel::CompoundValue.__init__)


def test_fuml::kernel::compoundvalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::CompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::reference_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Reference)


def test_fuml::kernel::reference_constructor_exists():
    assert callable(fuml::Kernel::Reference.__init__)


def test_fuml::kernel::reference_constructor_args():
    sig = inspect.signature(fuml::Kernel::Reference.__init__)
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



def test_fuml::kernel::integervalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::IntegerValue)


def test_fuml::kernel::integervalue_constructor_exists():
    assert callable(fuml::Kernel::IntegerValue.__init__)


def test_fuml::kernel::integervalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::integervalue_has_value():
    assert hasattr(fuml::Kernel::IntegerValue, "value")
    descriptor = None
    for klass in fuml::Kernel::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::stringvalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::StringValue)


def test_fuml::kernel::stringvalue_constructor_exists():
    assert callable(fuml::Kernel::StringValue.__init__)


def test_fuml::kernel::stringvalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::stringvalue_has_value():
    assert hasattr(fuml::Kernel::StringValue, "value")
    descriptor = None
    for klass in fuml::Kernel::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::BooleanValue)


def test_fuml::kernel::booleanvalue_constructor_exists():
    assert callable(fuml::Kernel::BooleanValue.__init__)


def test_fuml::kernel::booleanvalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::booleanvalue_has_value():
    assert hasattr(fuml::Kernel::BooleanValue, "value")
    descriptor = None
    for klass in fuml::Kernel::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::unlimitednaturalvalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::UnlimitedNaturalValue)


def test_fuml::kernel::unlimitednaturalvalue_constructor_exists():
    assert callable(fuml::Kernel::UnlimitedNaturalValue.__init__)


def test_fuml::kernel::unlimitednaturalvalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::UnlimitedNaturalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::unlimitednaturalvalue_has_value():
    assert hasattr(fuml::Kernel::UnlimitedNaturalValue, "value")
    descriptor = None
    for klass in fuml::Kernel::UnlimitedNaturalValue.__mro__:
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
    assert not inspect.isabstract(fuml::Kernel::FeatureValue)


def test_fuml::kernel::featurevalue_constructor_exists():
    assert callable(fuml::Kernel::FeatureValue.__init__)


def test_fuml::kernel::featurevalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::FeatureValue.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_fuml::kernel::featurevalue_has_position():
    assert hasattr(fuml::Kernel::FeatureValue, "position")
    descriptor = None
    for klass in fuml::Kernel::FeatureValue.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::link_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Link)


def test_fuml::kernel::link_constructor_exists():
    assert callable(fuml::Kernel::Link.__init__)


def test_fuml::kernel::link_constructor_args():
    sig = inspect.signature(fuml::Kernel::Link.__init__)
    params = list(sig.parameters.keys())



def test_kernel::featurevalue_is_not_abstract():
    assert not inspect.isabstract(Kernel::FeatureValue)


def test_kernel::featurevalue_constructor_exists():
    assert callable(Kernel::FeatureValue.__init__)


def test_kernel::featurevalue_constructor_args():
    sig = inspect.signature(Kernel::FeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::SendSignalAction)


def test_fuml::basicactions::sendsignalaction_constructor_exists():
    assert callable(fuml::BasicActions::SendSignalAction.__init__)


def test_fuml::basicactions::sendsignalaction_constructor_args():
    sig = inspect.signature(fuml::BasicActions::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::callaction_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::CallAction)


def test_fuml::basicactions::callaction_constructor_exists():
    assert callable(fuml::BasicActions::CallAction.__init__)


def test_fuml::basicactions::callaction_constructor_args():
    sig = inspect.signature(fuml::BasicActions::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "synchronous" in params, "Missing parameter 'synchronous'"

def test_fuml::basicactions::callaction_has_synchronous():
    assert hasattr(fuml::BasicActions::CallAction, "synchronous")
    descriptor = None
    for klass in fuml::BasicActions::CallAction.__mro__:
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
    assert not inspect.isabstract(fuml::BasicActions::OutputPin)


def test_fuml::basicactions::outputpin_constructor_exists():
    assert callable(fuml::BasicActions::OutputPin.__init__)


def test_fuml::basicactions::outputpin_constructor_args():
    sig = inspect.signature(fuml::BasicActions::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::inputpin_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::InputPin)


def test_fuml::basicactions::inputpin_constructor_exists():
    assert callable(fuml::BasicActions::InputPin.__init__)


def test_fuml::basicactions::inputpin_constructor_args():
    sig = inspect.signature(fuml::BasicActions::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::enumerationvalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::EnumerationValue)


def test_fuml::kernel::enumerationvalue_constructor_exists():
    assert callable(fuml::Kernel::EnumerationValue.__init__)


def test_fuml::kernel::enumerationvalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::EnumerationValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::primitivevalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::PrimitiveValue)


def test_fuml::kernel::primitivevalue_constructor_exists():
    assert callable(fuml::Kernel::PrimitiveValue.__init__)


def test_fuml::kernel::primitivevalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::structuredvalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::StructuredValue)


def test_fuml::kernel::structuredvalue_constructor_exists():
    assert callable(fuml::Kernel::StructuredValue.__init__)


def test_fuml::kernel::structuredvalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::StructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::action_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::Action)


def test_fuml::basicactions::action_constructor_exists():
    assert callable(fuml::BasicActions::Action.__init__)


def test_fuml::basicactions::action_constructor_args():
    sig = inspect.signature(fuml::BasicActions::Action.__init__)
    params = list(sig.parameters.keys())
    assert "locallyReentrant" in params, "Missing parameter 'locallyReentrant'"

def test_fuml::basicactions::action_has_locallyReentrant():
    assert hasattr(fuml::BasicActions::Action, "locallyReentrant")
    descriptor = None
    for klass in fuml::BasicActions::Action.__mro__:
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



def test_fuml::basicactions::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::CallOperationAction)


def test_fuml::basicactions::calloperationaction_constructor_exists():
    assert callable(fuml::BasicActions::CallOperationAction.__init__)


def test_fuml::basicactions::calloperationaction_constructor_args():
    sig = inspect.signature(fuml::BasicActions::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::CallBehaviorAction)


def test_fuml::basicactions::callbehavioraction_constructor_exists():
    assert callable(fuml::BasicActions::CallBehaviorAction.__init__)


def test_fuml::basicactions::callbehavioraction_constructor_args():
    sig = inspect.signature(fuml::BasicActions::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteActions::StartObjectBehaviorAction)


def test_fuml::completeactions::startobjectbehavioraction_constructor_exists():
    assert callable(fuml::CompleteActions::StartObjectBehaviorAction.__init__)


def test_fuml::completeactions::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(fuml::CompleteActions::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::DestroyLinkAction)


def test_fuml::intermediateactions::destroylinkaction_constructor_exists():
    assert callable(fuml::IntermediateActions::DestroyLinkAction.__init__)


def test_fuml::intermediateactions::destroylinkaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::CreateLinkAction)


def test_fuml::intermediateactions::createlinkaction_constructor_exists():
    assert callable(fuml::IntermediateActions::CreateLinkAction.__init__)


def test_fuml::intermediateactions::createlinkaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::LinkEndDestructionData)


def test_fuml::intermediateactions::linkenddestructiondata_constructor_exists():
    assert callable(fuml::IntermediateActions::LinkEndDestructionData.__init__)


def test_fuml::intermediateactions::linkenddestructiondata_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "destroyDuplicates" in params, "Missing parameter 'destroyDuplicates'"

def test_fuml::intermediateactions::linkenddestructiondata_has_destroyDuplicates():
    assert hasattr(fuml::IntermediateActions::LinkEndDestructionData, "destroyDuplicates")
    descriptor = None
    for klass in fuml::IntermediateActions::LinkEndDestructionData.__mro__:
        if "destroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["destroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::LinkEndCreationData)


def test_fuml::intermediateactions::linkendcreationdata_constructor_exists():
    assert callable(fuml::IntermediateActions::LinkEndCreationData.__init__)


def test_fuml::intermediateactions::linkendcreationdata_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml::intermediateactions::linkendcreationdata_has_replaceAll():
    assert hasattr(fuml::IntermediateActions::LinkEndCreationData, "replaceAll")
    descriptor = None
    for klass in fuml::IntermediateActions::LinkEndCreationData.__mro__:
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
    assert not inspect.isabstract(fuml::IntermediateActions::AddStructuralFeatureValueAction)


def test_fuml::intermediateactions::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(fuml::IntermediateActions::AddStructuralFeatureValueAction.__init__)


def test_fuml::intermediateactions::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml::intermediateactions::addstructuralfeaturevalueaction_has_replaceAll():
    assert hasattr(fuml::IntermediateActions::AddStructuralFeatureValueAction, "replaceAll")
    descriptor = None
    for klass in fuml::IntermediateActions::AddStructuralFeatureValueAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::RemoveStructuralFeatureValueAction)


def test_fuml::intermediateactions::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(fuml::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)


def test_fuml::intermediateactions::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "removeDuplicates" in params, "Missing parameter 'removeDuplicates'"

def test_fuml::intermediateactions::removestructuralfeaturevalueaction_has_removeDuplicates():
    assert hasattr(fuml::IntermediateActions::RemoveStructuralFeatureValueAction, "removeDuplicates")
    descriptor = None
    for klass in fuml::IntermediateActions::RemoveStructuralFeatureValueAction.__mro__:
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



def test_fuml::intermediateactions::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::ReadStructuralFeatureAction)


def test_fuml::intermediateactions::readstructuralfeatureaction_constructor_exists():
    assert callable(fuml::IntermediateActions::ReadStructuralFeatureAction.__init__)


def test_fuml::intermediateactions::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::ClearStructuralFeatureAction)


def test_fuml::intermediateactions::clearstructuralfeatureaction_constructor_exists():
    assert callable(fuml::IntermediateActions::ClearStructuralFeatureAction.__init__)


def test_fuml::intermediateactions::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::WriteStructuralFeatureAction)


def test_fuml::intermediateactions::writestructuralfeatureaction_constructor_exists():
    assert callable(fuml::IntermediateActions::WriteStructuralFeatureAction.__init__)


def test_fuml::intermediateactions::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::linkenddata_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::LinkEndData)


def test_intermediateactions::linkenddata_constructor_exists():
    assert callable(IntermediateActions::LinkEndData.__init__)


def test_intermediateactions::linkenddata_constructor_args():
    sig = inspect.signature(IntermediateActions::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::ReadLinkAction)


def test_fuml::intermediateactions::readlinkaction_constructor_exists():
    assert callable(fuml::IntermediateActions::ReadLinkAction.__init__)


def test_fuml::intermediateactions::readlinkaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::WriteLinkAction)


def test_fuml::intermediateactions::writelinkaction_constructor_exists():
    assert callable(fuml::IntermediateActions::WriteLinkAction.__init__)


def test_fuml::intermediateactions::writelinkaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_extrastructuredactivities::expansionnode_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities::ExpansionNode)


def test_extrastructuredactivities::expansionnode_constructor_exists():
    assert callable(ExtraStructuredActivities::ExpansionNode.__init__)


def test_extrastructuredactivities::expansionnode_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities::ExpansionNode.__init__)
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



def test_fuml::completeactions::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteActions::AcceptEventAction)


def test_fuml::completeactions::accepteventaction_constructor_exists():
    assert callable(fuml::CompleteActions::AcceptEventAction.__init__)


def test_fuml::completeactions::accepteventaction_constructor_args():
    sig = inspect.signature(fuml::CompleteActions::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshall" in params, "Missing parameter 'unmarshall'"

def test_fuml::completeactions::accepteventaction_has_unmarshall():
    assert hasattr(fuml::CompleteActions::AcceptEventAction, "unmarshall")
    descriptor = None
    for klass in fuml::CompleteActions::AcceptEventAction.__mro__:
        if "unmarshall" in klass.__dict__:
            descriptor = klass.__dict__["unmarshall"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::CreateObjectAction)


def test_fuml::intermediateactions::createobjectaction_constructor_exists():
    assert callable(fuml::IntermediateActions::CreateObjectAction.__init__)


def test_fuml::intermediateactions::createobjectaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::reduceaction_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteActions::ReduceAction)


def test_fuml::completeactions::reduceaction_constructor_exists():
    assert callable(fuml::CompleteActions::ReduceAction.__init__)


def test_fuml::completeactions::reduceaction_constructor_args():
    sig = inspect.signature(fuml::CompleteActions::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_fuml::completeactions::reduceaction_has_ordered():
    assert hasattr(fuml::CompleteActions::ReduceAction, "ordered")
    descriptor = None
    for klass in fuml::CompleteActions::ReduceAction.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_fuml::basicactions::invocationaction_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::InvocationAction)


def test_fuml::basicactions::invocationaction_constructor_exists():
    assert callable(fuml::BasicActions::InvocationAction.__init__)


def test_fuml::basicactions::invocationaction_constructor_args():
    sig = inspect.signature(fuml::BasicActions::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteActions::ReadIsClassifiedObjectAction)


def test_fuml::completeactions::readisclassifiedobjectaction_constructor_exists():
    assert callable(fuml::CompleteActions::ReadIsClassifiedObjectAction.__init__)


def test_fuml::completeactions::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(fuml::CompleteActions::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "direct" in params, "Missing parameter 'direct'"

def test_fuml::completeactions::readisclassifiedobjectaction_has_direct():
    assert hasattr(fuml::CompleteActions::ReadIsClassifiedObjectAction, "direct")
    descriptor = None
    for klass in fuml::CompleteActions::ReadIsClassifiedObjectAction.__mro__:
        if "direct" in klass.__dict__:
            descriptor = klass.__dict__["direct"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::readselfaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::ReadSelfAction)


def test_fuml::intermediateactions::readselfaction_constructor_exists():
    assert callable(fuml::IntermediateActions::ReadSelfAction.__init__)


def test_fuml::intermediateactions::readselfaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::readextentaction_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteActions::ReadExtentAction)


def test_fuml::completeactions::readextentaction_constructor_exists():
    assert callable(fuml::CompleteActions::ReadExtentAction.__init__)


def test_fuml::completeactions::readextentaction_constructor_args():
    sig = inspect.signature(fuml::CompleteActions::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteActions::StartClassifierBehaviorAction)


def test_fuml::completeactions::startclassifierbehavioraction_constructor_exists():
    assert callable(fuml::CompleteActions::StartClassifierBehaviorAction.__init__)


def test_fuml::completeactions::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(fuml::CompleteActions::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::TestIdentityAction)


def test_fuml::intermediateactions::testidentityaction_constructor_exists():
    assert callable(fuml::IntermediateActions::TestIdentityAction.__init__)


def test_fuml::intermediateactions::testidentityaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::ClearAssociationAction)


def test_fuml::intermediateactions::clearassociationaction_constructor_exists():
    assert callable(fuml::IntermediateActions::ClearAssociationAction.__init__)


def test_fuml::intermediateactions::clearassociationaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::ValueSpecificationAction)


def test_fuml::intermediateactions::valuespecificationaction_constructor_exists():
    assert callable(fuml::IntermediateActions::ValueSpecificationAction.__init__)


def test_fuml::intermediateactions::valuespecificationaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::StructuralFeatureAction)


def test_fuml::intermediateactions::structuralfeatureaction_constructor_exists():
    assert callable(fuml::IntermediateActions::StructuralFeatureAction.__init__)


def test_fuml::intermediateactions::structuralfeatureaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::DestroyObjectAction)


def test_fuml::intermediateactions::destroyobjectaction_constructor_exists():
    assert callable(fuml::IntermediateActions::DestroyObjectAction.__init__)


def test_fuml::intermediateactions::destroyobjectaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "destroyLinks" in params, "Missing parameter 'destroyLinks'"
    assert "destroyOwnedObjects" in params, "Missing parameter 'destroyOwnedObjects'"

def test_fuml::intermediateactions::destroyobjectaction_has_destroyLinks():
    assert hasattr(fuml::IntermediateActions::DestroyObjectAction, "destroyLinks")
    descriptor = None
    for klass in fuml::IntermediateActions::DestroyObjectAction.__mro__:
        if "destroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["destroyLinks"]
            break
    assert isinstance(descriptor, property)

def test_fuml::intermediateactions::destroyobjectaction_has_destroyOwnedObjects():
    assert hasattr(fuml::IntermediateActions::DestroyObjectAction, "destroyOwnedObjects")
    descriptor = None
    for klass in fuml::IntermediateActions::DestroyObjectAction.__mro__:
        if "destroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["destroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)



def test_fuml::intermediateactions::linkaction_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::LinkAction)


def test_fuml::intermediateactions::linkaction_constructor_exists():
    assert callable(fuml::IntermediateActions::LinkAction.__init__)


def test_fuml::intermediateactions::linkaction_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completeactions::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteActions::ReclassifyObjectAction)


def test_fuml::completeactions::reclassifyobjectaction_constructor_exists():
    assert callable(fuml::CompleteActions::ReclassifyObjectAction.__init__)


def test_fuml::completeactions::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(fuml::CompleteActions::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml::completeactions::reclassifyobjectaction_has_replaceAll():
    assert hasattr(fuml::CompleteActions::ReclassifyObjectAction, "replaceAll")
    descriptor = None
    for klass in fuml::CompleteActions::ReclassifyObjectAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completestructuredactivities::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteStructuredActivities::StructuredActivityNode)


def test_fuml::completestructuredactivities::structuredactivitynode_constructor_exists():
    assert callable(fuml::CompleteStructuredActivities::StructuredActivityNode.__init__)


def test_fuml::completestructuredactivities::structuredactivitynode_constructor_args():
    sig = inspect.signature(fuml::CompleteStructuredActivities::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_fuml::completestructuredactivities::structuredactivitynode_has_mustIsolate():
    assert hasattr(fuml::CompleteStructuredActivities::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in fuml::CompleteStructuredActivities::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_completestructuredactivities::clause_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities::Clause)


def test_completestructuredactivities::clause_constructor_exists():
    assert callable(CompleteStructuredActivities::Clause.__init__)


def test_completestructuredactivities::clause_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities::Clause.__init__)
    params = list(sig.parameters.keys())



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
    assert not inspect.isabstract(fuml::ExtraStructuredActivities::ExpansionRegion)


def test_fuml::extrastructuredactivities::expansionregion_constructor_exists():
    assert callable(fuml::ExtraStructuredActivities::ExpansionRegion.__init__)


def test_fuml::extrastructuredactivities::expansionregion_constructor_args():
    sig = inspect.signature(fuml::ExtraStructuredActivities::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_fuml::extrastructuredactivities::expansionregion_has_mode():
    assert hasattr(fuml::ExtraStructuredActivities::ExpansionRegion, "mode")
    descriptor = None
    for klass in fuml::ExtraStructuredActivities::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completestructuredactivities::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteStructuredActivities::ConditionalNode)


def test_fuml::completestructuredactivities::conditionalnode_constructor_exists():
    assert callable(fuml::CompleteStructuredActivities::ConditionalNode.__init__)


def test_fuml::completestructuredactivities::conditionalnode_constructor_args():
    sig = inspect.signature(fuml::CompleteStructuredActivities::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "determinate" in params, "Missing parameter 'determinate'"
    assert "assured" in params, "Missing parameter 'assured'"

def test_fuml::completestructuredactivities::conditionalnode_has_determinate():
    assert hasattr(fuml::CompleteStructuredActivities::ConditionalNode, "determinate")
    descriptor = None
    for klass in fuml::CompleteStructuredActivities::ConditionalNode.__mro__:
        if "determinate" in klass.__dict__:
            descriptor = klass.__dict__["determinate"]
            break
    assert isinstance(descriptor, property)

def test_fuml::completestructuredactivities::conditionalnode_has_assured():
    assert hasattr(fuml::CompleteStructuredActivities::ConditionalNode, "assured")
    descriptor = None
    for klass in fuml::CompleteStructuredActivities::ConditionalNode.__mro__:
        if "assured" in klass.__dict__:
            descriptor = klass.__dict__["assured"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completestructuredactivities::loopnode_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteStructuredActivities::LoopNode)


def test_fuml::completestructuredactivities::loopnode_constructor_exists():
    assert callable(fuml::CompleteStructuredActivities::LoopNode.__init__)


def test_fuml::completestructuredactivities::loopnode_constructor_args():
    sig = inspect.signature(fuml::CompleteStructuredActivities::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "testedFirst" in params, "Missing parameter 'testedFirst'"

def test_fuml::completestructuredactivities::loopnode_has_testedFirst():
    assert hasattr(fuml::CompleteStructuredActivities::LoopNode, "testedFirst")
    descriptor = None
    for klass in fuml::CompleteStructuredActivities::LoopNode.__mro__:
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
    assert not inspect.isabstract(fuml::ExtraStructuredActivities::ExpansionNode)


def test_fuml::extrastructuredactivities::expansionnode_constructor_exists():
    assert callable(fuml::ExtraStructuredActivities::ExpansionNode.__init__)


def test_fuml::extrastructuredactivities::expansionnode_constructor_args():
    sig = inspect.signature(fuml::ExtraStructuredActivities::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ActivityParameterNode)


def test_fuml::intermediateactivities::activityparameternode_constructor_exists():
    assert callable(fuml::IntermediateActivities::ActivityParameterNode.__init__)


def test_fuml::intermediateactivities::activityparameternode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ActivityFinalNode)


def test_fuml::intermediateactivities::activityfinalnode_constructor_exists():
    assert callable(fuml::IntermediateActivities::ActivityFinalNode.__init__)


def test_fuml::intermediateactivities::activityfinalnode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::objectflow_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::ObjectFlow)


def test_intermediateactivities::objectflow_constructor_exists():
    assert callable(IntermediateActivities::ObjectFlow.__init__)


def test_intermediateactivities::objectflow_constructor_args():
    sig = inspect.signature(IntermediateActivities::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::completestructuredactivities::executablenode_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteStructuredActivities::ExecutableNode)


def test_fuml::completestructuredactivities::executablenode_constructor_exists():
    assert callable(fuml::CompleteStructuredActivities::ExecutableNode.__init__)


def test_fuml::completestructuredactivities::executablenode_constructor_args():
    sig = inspect.signature(fuml::CompleteStructuredActivities::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::controlnode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ControlNode)


def test_fuml::intermediateactivities::controlnode_constructor_exists():
    assert callable(fuml::IntermediateActivities::ControlNode.__init__)


def test_fuml::intermediateactivities::controlnode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::forknode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ForkNode)


def test_fuml::intermediateactivities::forknode_constructor_exists():
    assert callable(fuml::IntermediateActivities::ForkNode.__init__)


def test_fuml::intermediateactivities::forknode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::finalnode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::FinalNode)


def test_fuml::intermediateactivities::finalnode_constructor_exists():
    assert callable(fuml::IntermediateActivities::FinalNode.__init__)


def test_fuml::intermediateactivities::finalnode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::initialnode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::InitialNode)


def test_fuml::intermediateactivities::initialnode_constructor_exists():
    assert callable(fuml::IntermediateActivities::InitialNode.__init__)


def test_fuml::intermediateactivities::initialnode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::joinnode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::JoinNode)


def test_fuml::intermediateactivities::joinnode_constructor_exists():
    assert callable(fuml::IntermediateActivities::JoinNode.__init__)


def test_fuml::intermediateactivities::joinnode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::decisionnode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::DecisionNode)


def test_fuml::intermediateactivities::decisionnode_constructor_exists():
    assert callable(fuml::IntermediateActivities::DecisionNode.__init__)


def test_fuml::intermediateactivities::decisionnode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::mergenode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::MergeNode)


def test_fuml::intermediateactivities::mergenode_constructor_exists():
    assert callable(fuml::IntermediateActivities::MergeNode.__init__)


def test_fuml::intermediateactivities::mergenode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::activityedge_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::ActivityEdge)


def test_intermediateactivities::activityedge_constructor_exists():
    assert callable(IntermediateActivities::ActivityEdge.__init__)


def test_intermediateactivities::activityedge_constructor_args():
    sig = inspect.signature(IntermediateActivities::ActivityEdge.__init__)
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



def test_intermediateactivities::activity_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::Activity)


def test_intermediateactivities::activity_constructor_exists():
    assert callable(IntermediateActivities::Activity.__init__)


def test_intermediateactivities::activity_constructor_args():
    sig = inspect.signature(IntermediateActivities::Activity.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::controlflow_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ControlFlow)


def test_fuml::intermediateactivities::controlflow_constructor_exists():
    assert callable(fuml::IntermediateActivities::ControlFlow.__init__)


def test_fuml::intermediateactivities::controlflow_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::objectflow_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ObjectFlow)


def test_fuml::intermediateactivities::objectflow_constructor_exists():
    assert callable(fuml::IntermediateActivities::ObjectFlow.__init__)


def test_fuml::intermediateactivities::objectflow_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::literalboolean_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::LiteralBoolean)


def test_fuml::kernel::literalboolean_constructor_exists():
    assert callable(fuml::Kernel::LiteralBoolean.__init__)


def test_fuml::kernel::literalboolean_constructor_args():
    sig = inspect.signature(fuml::Kernel::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalboolean_has_value():
    assert hasattr(fuml::Kernel::LiteralBoolean, "value")
    descriptor = None
    for klass in fuml::Kernel::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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
    assert not inspect.isabstract(fuml::Kernel::Class)


def test_fuml::kernel::class_constructor_exists():
    assert callable(fuml::Kernel::Class.__init__)


def test_fuml::kernel::class_constructor_args():
    sig = inspect.signature(fuml::Kernel::Class.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_fuml::kernel::class_has_active():
    assert hasattr(fuml::Kernel::Class, "active")
    descriptor = None
    for klass in fuml::Kernel::Class.__mro__:
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
    assert not inspect.isabstract(fuml::Kernel::EnumerationLiteral)


def test_fuml::kernel::enumerationliteral_constructor_exists():
    assert callable(fuml::Kernel::EnumerationLiteral.__init__)


def test_fuml::kernel::enumerationliteral_constructor_args():
    sig = inspect.signature(fuml::Kernel::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_kernel::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(Kernel::EnumerationLiteral)


def test_kernel::enumerationliteral_constructor_exists():
    assert callable(Kernel::EnumerationLiteral.__init__)


def test_kernel::enumerationliteral_constructor_args():
    sig = inspect.signature(Kernel::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::enumeration_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Enumeration)


def test_fuml::kernel::enumeration_constructor_exists():
    assert callable(fuml::Kernel::Enumeration.__init__)


def test_fuml::kernel::enumeration_constructor_args():
    sig = inspect.signature(fuml::Kernel::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::primitivetype_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::PrimitiveType)


def test_fuml::kernel::primitivetype_constructor_exists():
    assert callable(fuml::Kernel::PrimitiveType.__init__)


def test_fuml::kernel::primitivetype_constructor_args():
    sig = inspect.signature(fuml::Kernel::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::LiteralUnlimitedNatural)


def test_fuml::kernel::literalunlimitednatural_constructor_exists():
    assert callable(fuml::Kernel::LiteralUnlimitedNatural.__init__)


def test_fuml::kernel::literalunlimitednatural_constructor_args():
    sig = inspect.signature(fuml::Kernel::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalunlimitednatural_has_value():
    assert hasattr(fuml::Kernel::LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in fuml::Kernel::LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::literalstring_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::LiteralString)


def test_fuml::kernel::literalstring_constructor_exists():
    assert callable(fuml::Kernel::LiteralString.__init__)


def test_fuml::kernel::literalstring_constructor_args():
    sig = inspect.signature(fuml::Kernel::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalstring_has_value():
    assert hasattr(fuml::Kernel::LiteralString, "value")
    descriptor = None
    for klass in fuml::Kernel::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::literalnull_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::LiteralNull)


def test_fuml::kernel::literalnull_constructor_exists():
    assert callable(fuml::Kernel::LiteralNull.__init__)


def test_fuml::kernel::literalnull_constructor_args():
    sig = inspect.signature(fuml::Kernel::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::literalinteger_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::LiteralInteger)


def test_fuml::kernel::literalinteger_constructor_exists():
    assert callable(fuml::Kernel::LiteralInteger.__init__)


def test_fuml::kernel::literalinteger_constructor_args():
    sig = inspect.signature(fuml::Kernel::LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml::kernel::literalinteger_has_value():
    assert hasattr(fuml::Kernel::LiteralInteger, "value")
    descriptor = None
    for klass in fuml::Kernel::LiteralInteger.__mro__:
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
    assert not inspect.isabstract(fuml::Kernel::LiteralSpecification)


def test_fuml::kernel::literalspecification_constructor_exists():
    assert callable(fuml::Kernel::LiteralSpecification.__init__)


def test_fuml::kernel::literalspecification_constructor_args():
    sig = inspect.signature(fuml::Kernel::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::instancevalue_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::InstanceValue)


def test_fuml::kernel::instancevalue_constructor_exists():
    assert callable(fuml::Kernel::InstanceValue.__init__)


def test_fuml::kernel::instancevalue_constructor_args():
    sig = inspect.signature(fuml::Kernel::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel::instancespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel::InstanceSpecification)


def test_kernel::instancespecification_constructor_exists():
    assert callable(Kernel::InstanceSpecification.__init__)


def test_kernel::instancespecification_constructor_args():
    sig = inspect.signature(Kernel::InstanceSpecification.__init__)
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



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::BehavioralFeature)


def test_fuml::kernel::behavioralfeature_constructor_exists():
    assert callable(fuml::Kernel::BehavioralFeature.__init__)


def test_fuml::kernel::behavioralfeature_constructor_args():
    sig = inspect.signature(fuml::Kernel::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_fuml::kernel::behavioralfeature_has_concurrency():
    assert hasattr(fuml::Kernel::BehavioralFeature, "concurrency")
    descriptor = None
    for klass in fuml::Kernel::BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::behavioralfeature_has_abstract():
    assert hasattr(fuml::Kernel::BehavioralFeature, "abstract")
    descriptor = None
    for klass in fuml::Kernel::BehavioralFeature.__mro__:
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
    assert not inspect.isabstract(fuml::Kernel::Property)


def test_fuml::kernel::property_constructor_exists():
    assert callable(fuml::Kernel::Property.__init__)


def test_fuml::kernel::property_constructor_args():
    sig = inspect.signature(fuml::Kernel::Property.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "composite" in params, "Missing parameter 'composite'"
    assert "derivedUnion" in params, "Missing parameter 'derivedUnion'"

def test_fuml::kernel::property_has_aggregation():
    assert hasattr(fuml::Kernel::Property, "aggregation")
    descriptor = None
    for klass in fuml::Kernel::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::property_has_derived():
    assert hasattr(fuml::Kernel::Property, "derived")
    descriptor = None
    for klass in fuml::Kernel::Property.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::property_has_composite():
    assert hasattr(fuml::Kernel::Property, "composite")
    descriptor = None
    for klass in fuml::Kernel::Property.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::property_has_derivedUnion():
    assert hasattr(fuml::Kernel::Property, "derivedUnion")
    descriptor = None
    for klass in fuml::Kernel::Property.__mro__:
        if "derivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["derivedUnion"]
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



def test_fuml::intermediateactivities::activitynode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ActivityNode)


def test_fuml::intermediateactivities::activitynode_constructor_exists():
    assert callable(fuml::IntermediateActivities::ActivityNode.__init__)


def test_fuml::intermediateactivities::activitynode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactivities::activityedge_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ActivityEdge)


def test_fuml::intermediateactivities::activityedge_constructor_exists():
    assert callable(fuml::IntermediateActivities::ActivityEdge.__init__)


def test_fuml::intermediateactivities::activityedge_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::feature_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Feature)


def test_fuml::kernel::feature_constructor_exists():
    assert callable(fuml::Kernel::Feature.__init__)


def test_fuml::kernel::feature_constructor_args():
    sig = inspect.signature(fuml::Kernel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_fuml::kernel::feature_has_static():
    assert hasattr(fuml::Kernel::Feature, "static")
    descriptor = None
    for klass in fuml::Kernel::Feature.__mro__:
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



def test_fuml::intermediateactivities::objectnode_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::ObjectNode)


def test_fuml::intermediateactivities::objectnode_constructor_exists():
    assert callable(fuml::IntermediateActivities::ObjectNode.__init__)


def test_fuml::intermediateactivities::objectnode_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_kernel::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(Kernel::MultiplicityElement)


def test_kernel::multiplicityelement_constructor_exists():
    assert callable(Kernel::MultiplicityElement.__init__)


def test_kernel::multiplicityelement_constructor_args():
    sig = inspect.signature(Kernel::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicactions::pin_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicActions::Pin)


def test_fuml::basicactions::pin_constructor_exists():
    assert callable(fuml::BasicActions::Pin.__init__)


def test_fuml::basicactions::pin_constructor_args():
    sig = inspect.signature(fuml::BasicActions::Pin.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::parameter_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Parameter)


def test_fuml::kernel::parameter_constructor_exists():
    assert callable(fuml::Kernel::Parameter.__init__)


def test_fuml::kernel::parameter_constructor_args():
    sig = inspect.signature(fuml::Kernel::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_fuml::kernel::parameter_has_direction():
    assert hasattr(fuml::Kernel::Parameter, "direction")
    descriptor = None
    for klass in fuml::Kernel::Parameter.__mro__:
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
    assert not inspect.isabstract(fuml::Kernel::StructuralFeature)


def test_fuml::kernel::structuralfeature_constructor_exists():
    assert callable(fuml::Kernel::StructuralFeature.__init__)


def test_fuml::kernel::structuralfeature_constructor_args():
    sig = inspect.signature(fuml::Kernel::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_fuml::kernel::structuralfeature_has_readOnly():
    assert hasattr(fuml::Kernel::StructuralFeature, "readOnly")
    descriptor = None
    for klass in fuml::Kernel::StructuralFeature.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



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
    assert not inspect.isabstract(fuml::Kernel::Comment)


def test_fuml::kernel::comment_constructor_exists():
    assert callable(fuml::Kernel::Comment.__init__)


def test_fuml::kernel::comment_constructor_args():
    sig = inspect.signature(fuml::Kernel::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_fuml::kernel::comment_has_body():
    assert hasattr(fuml::Kernel::Comment, "body")
    descriptor = None
    for klass in fuml::Kernel::Comment.__mro__:
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



def test_fuml::kernel::element_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Element)


def test_fuml::kernel::element_constructor_exists():
    assert callable(fuml::Kernel::Element.__init__)


def test_fuml::kernel::element_constructor_args():
    sig = inspect.signature(fuml::Kernel::Element.__init__)
    params = list(sig.parameters.keys())



def test_kernel::namespace_is_not_abstract():
    assert not inspect.isabstract(Kernel::Namespace)


def test_kernel::namespace_constructor_exists():
    assert callable(Kernel::Namespace.__init__)


def test_kernel::namespace_constructor_args():
    sig = inspect.signature(Kernel::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::package_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Package)


def test_fuml::kernel::package_constructor_exists():
    assert callable(fuml::Kernel::Package.__init__)


def test_fuml::kernel::package_constructor_args():
    sig = inspect.signature(fuml::Kernel::Package.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_fuml::intermediateactions::linkenddata_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActions::LinkEndData)


def test_fuml::intermediateactions::linkenddata_constructor_exists():
    assert callable(fuml::IntermediateActions::LinkEndData.__init__)


def test_fuml::intermediateactions::linkenddata_constructor_args():
    sig = inspect.signature(fuml::IntermediateActions::LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::MultiplicityElement)


def test_fuml::kernel::multiplicityelement_constructor_exists():
    assert callable(fuml::Kernel::MultiplicityElement.__init__)


def test_fuml::kernel::multiplicityelement_constructor_args():
    sig = inspect.signature(fuml::Kernel::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_fuml::kernel::multiplicityelement_has_lower():
    assert hasattr(fuml::Kernel::MultiplicityElement, "lower")
    descriptor = None
    for klass in fuml::Kernel::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::multiplicityelement_has_ordered():
    assert hasattr(fuml::Kernel::MultiplicityElement, "ordered")
    descriptor = None
    for klass in fuml::Kernel::MultiplicityElement.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::multiplicityelement_has_upper():
    assert hasattr(fuml::Kernel::MultiplicityElement, "upper")
    descriptor = None
    for klass in fuml::Kernel::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::multiplicityelement_has_unique():
    assert hasattr(fuml::Kernel::MultiplicityElement, "unique")
    descriptor = None
    for klass in fuml::Kernel::MultiplicityElement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::elementimport_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::ElementImport)


def test_fuml::kernel::elementimport_constructor_exists():
    assert callable(fuml::Kernel::ElementImport.__init__)


def test_fuml::kernel::elementimport_constructor_args():
    sig = inspect.signature(fuml::Kernel::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_fuml::kernel::elementimport_has_visibility():
    assert hasattr(fuml::Kernel::ElementImport, "visibility")
    descriptor = None
    for klass in fuml::Kernel::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::elementimport_has_alias():
    assert hasattr(fuml::Kernel::ElementImport, "alias")
    descriptor = None
    for klass in fuml::Kernel::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_fuml::completestructuredactivities::clause_is_not_abstract():
    assert not inspect.isabstract(fuml::CompleteStructuredActivities::Clause)


def test_fuml::completestructuredactivities::clause_constructor_exists():
    assert callable(fuml::CompleteStructuredActivities::Clause.__init__)


def test_fuml::completestructuredactivities::clause_constructor_args():
    sig = inspect.signature(fuml::CompleteStructuredActivities::Clause.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::slot_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Slot)


def test_fuml::kernel::slot_constructor_exists():
    assert callable(fuml::Kernel::Slot.__init__)


def test_fuml::kernel::slot_constructor_args():
    sig = inspect.signature(fuml::Kernel::Slot.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::packageimport_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::PackageImport)


def test_fuml::kernel::packageimport_constructor_exists():
    assert callable(fuml::Kernel::PackageImport.__init__)


def test_fuml::kernel::packageimport_constructor_args():
    sig = inspect.signature(fuml::Kernel::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_fuml::kernel::packageimport_has_visibility():
    assert hasattr(fuml::Kernel::PackageImport, "visibility")
    descriptor = None
    for klass in fuml::Kernel::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::generalization_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Generalization)


def test_fuml::kernel::generalization_constructor_exists():
    assert callable(fuml::Kernel::Generalization.__init__)


def test_fuml::kernel::generalization_constructor_args():
    sig = inspect.signature(fuml::Kernel::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "substitutable" in params, "Missing parameter 'substitutable'"

def test_fuml::kernel::generalization_has_substitutable():
    assert hasattr(fuml::Kernel::Generalization, "substitutable")
    descriptor = None
    for klass in fuml::Kernel::Generalization.__mro__:
        if "substitutable" in klass.__dict__:
            descriptor = klass.__dict__["substitutable"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::namedelement_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::NamedElement)


def test_fuml::kernel::namedelement_constructor_exists():
    assert callable(fuml::Kernel::NamedElement.__init__)


def test_fuml::kernel::namedelement_constructor_args():
    sig = inspect.signature(fuml::Kernel::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_fuml::kernel::namedelement_has_name():
    assert hasattr(fuml::Kernel::NamedElement, "name")
    descriptor = None
    for klass in fuml::Kernel::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::namedelement_has_qualifiedName():
    assert hasattr(fuml::Kernel::NamedElement, "qualifiedName")
    descriptor = None
    for klass in fuml::Kernel::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::namedelement_has_visibility():
    assert hasattr(fuml::Kernel::NamedElement, "visibility")
    descriptor = None
    for klass in fuml::Kernel::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
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
    assert not inspect.isabstract(fuml::Kernel::Classifier)


def test_fuml::kernel::classifier_constructor_exists():
    assert callable(fuml::Kernel::Classifier.__init__)


def test_fuml::kernel::classifier_constructor_args():
    sig = inspect.signature(fuml::Kernel::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "finalSpecialization" in params, "Missing parameter 'finalSpecialization'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_fuml::kernel::classifier_has_finalSpecialization():
    assert hasattr(fuml::Kernel::Classifier, "finalSpecialization")
    descriptor = None
    for klass in fuml::Kernel::Classifier.__mro__:
        if "finalSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["finalSpecialization"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::classifier_has_abstract():
    assert hasattr(fuml::Kernel::Classifier, "abstract")
    descriptor = None
    for klass in fuml::Kernel::Classifier.__mro__:
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
    assert not inspect.isabstract(fuml::Kernel::ValueSpecification)


def test_fuml::kernel::valuespecification_constructor_exists():
    assert callable(fuml::Kernel::ValueSpecification.__init__)


def test_fuml::kernel::valuespecification_constructor_args():
    sig = inspect.signature(fuml::Kernel::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::operation_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Operation)


def test_fuml::kernel::operation_constructor_exists():
    assert callable(fuml::Kernel::Operation.__init__)


def test_fuml::kernel::operation_constructor_args():
    sig = inspect.signature(fuml::Kernel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "query" in params, "Missing parameter 'query'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_fuml::kernel::operation_has_ordered():
    assert hasattr(fuml::Kernel::Operation, "ordered")
    descriptor = None
    for klass in fuml::Kernel::Operation.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_upper():
    assert hasattr(fuml::Kernel::Operation, "upper")
    descriptor = None
    for klass in fuml::Kernel::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_lower():
    assert hasattr(fuml::Kernel::Operation, "lower")
    descriptor = None
    for klass in fuml::Kernel::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_query():
    assert hasattr(fuml::Kernel::Operation, "query")
    descriptor = None
    for klass in fuml::Kernel::Operation.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_fuml::kernel::operation_has_unique():
    assert hasattr(fuml::Kernel::Operation, "unique")
    descriptor = None
    for klass in fuml::Kernel::Operation.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_fuml::communications::reception_is_not_abstract():
    assert not inspect.isabstract(fuml::Communications::Reception)


def test_fuml::communications::reception_constructor_exists():
    assert callable(fuml::Communications::Reception.__init__)


def test_fuml::communications::reception_constructor_args():
    sig = inspect.signature(fuml::Communications::Reception.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_fuml::communications::messageevent_is_not_abstract():
    assert not inspect.isabstract(fuml::Communications::MessageEvent)


def test_fuml::communications::messageevent_constructor_exists():
    assert callable(fuml::Communications::MessageEvent.__init__)


def test_fuml::communications::messageevent_constructor_args():
    sig = inspect.signature(fuml::Communications::MessageEvent.__init__)
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
    assert not inspect.isabstract(fuml::Communications::SignalEvent)


def test_fuml::communications::signalevent_constructor_exists():
    assert callable(fuml::Communications::SignalEvent.__init__)


def test_fuml::communications::signalevent_constructor_args():
    sig = inspect.signature(fuml::Communications::SignalEvent.__init__)
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
    assert not inspect.isabstract(fuml::Kernel::Type)


def test_fuml::kernel::type_constructor_exists():
    assert callable(fuml::Kernel::Type.__init__)


def test_fuml::kernel::type_constructor_args():
    sig = inspect.signature(fuml::Kernel::Type.__init__)
    params = list(sig.parameters.keys())



def test_fuml::communications::event_is_not_abstract():
    assert not inspect.isabstract(fuml::Communications::Event)


def test_fuml::communications::event_constructor_exists():
    assert callable(fuml::Communications::Event.__init__)


def test_fuml::communications::event_constructor_args():
    sig = inspect.signature(fuml::Communications::Event.__init__)
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



def test_fuml::kernel::instancespecification_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::InstanceSpecification)


def test_fuml::kernel::instancespecification_constructor_exists():
    assert callable(fuml::Kernel::InstanceSpecification.__init__)


def test_fuml::kernel::instancespecification_constructor_args():
    sig = inspect.signature(fuml::Kernel::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::typedelement_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::TypedElement)


def test_fuml::kernel::typedelement_constructor_exists():
    assert callable(fuml::Kernel::TypedElement.__init__)


def test_fuml::kernel::typedelement_constructor_args():
    sig = inspect.signature(fuml::Kernel::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::namespace_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::Namespace)


def test_fuml::kernel::namespace_constructor_exists():
    assert callable(fuml::Kernel::Namespace.__init__)


def test_fuml::kernel::namespace_constructor_args():
    sig = inspect.signature(fuml::Kernel::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::packageableelement_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::PackageableElement)


def test_fuml::kernel::packageableelement_constructor_exists():
    assert callable(fuml::Kernel::PackageableElement.__init__)


def test_fuml::kernel::packageableelement_constructor_args():
    sig = inspect.signature(fuml::Kernel::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml::kernel::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::RedefinableElement)


def test_fuml::kernel::redefinableelement_constructor_exists():
    assert callable(fuml::Kernel::RedefinableElement.__init__)


def test_fuml::kernel::redefinableelement_constructor_args():
    sig = inspect.signature(fuml::Kernel::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "leaf" in params, "Missing parameter 'leaf'"

def test_fuml::kernel::redefinableelement_has_leaf():
    assert hasattr(fuml::Kernel::RedefinableElement, "leaf")
    descriptor = None
    for klass in fuml::Kernel::RedefinableElement.__mro__:
        if "leaf" in klass.__dict__:
            descriptor = klass.__dict__["leaf"]
            break
    assert isinstance(descriptor, property)



def test_fuml::communications::trigger_is_not_abstract():
    assert not inspect.isabstract(fuml::Communications::Trigger)


def test_fuml::communications::trigger_constructor_exists():
    assert callable(fuml::Communications::Trigger.__init__)


def test_fuml::communications::trigger_constructor_args():
    sig = inspect.signature(fuml::Communications::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicbehaviors::functionbehavior_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicBehaviors::FunctionBehavior)


def test_fuml::basicbehaviors::functionbehavior_constructor_exists():
    assert callable(fuml::BasicBehaviors::FunctionBehavior.__init__)


def test_fuml::basicbehaviors::functionbehavior_constructor_args():
    sig = inspect.signature(fuml::BasicBehaviors::FunctionBehavior.__init__)
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
    assert not inspect.isabstract(fuml::Kernel::Association)


def test_fuml::kernel::association_constructor_exists():
    assert callable(fuml::Kernel::Association.__init__)


def test_fuml::kernel::association_constructor_args():
    sig = inspect.signature(fuml::Kernel::Association.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"

def test_fuml::kernel::association_has_derived():
    assert hasattr(fuml::Kernel::Association, "derived")
    descriptor = None
    for klass in fuml::Kernel::Association.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_fuml::kernel::datatype_is_not_abstract():
    assert not inspect.isabstract(fuml::Kernel::DataType)


def test_fuml::kernel::datatype_constructor_exists():
    assert callable(fuml::Kernel::DataType.__init__)


def test_fuml::kernel::datatype_constructor_args():
    sig = inspect.signature(fuml::Kernel::DataType.__init__)
    params = list(sig.parameters.keys())



def test_fuml::communications::signal_is_not_abstract():
    assert not inspect.isabstract(fuml::Communications::Signal)


def test_fuml::communications::signal_constructor_exists():
    assert callable(fuml::Communications::Signal.__init__)


def test_fuml::communications::signal_constructor_args():
    sig = inspect.signature(fuml::Communications::Signal.__init__)
    params = list(sig.parameters.keys())



def test_fuml::basicbehaviors::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicBehaviors::BehavioredClassifier)


def test_fuml::basicbehaviors::behavioredclassifier_constructor_exists():
    assert callable(fuml::BasicBehaviors::BehavioredClassifier.__init__)


def test_fuml::basicbehaviors::behavioredclassifier_constructor_args():
    sig = inspect.signature(fuml::BasicBehaviors::BehavioredClassifier.__init__)
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
    assert not inspect.isabstract(fuml::BasicBehaviors::Behavior)


def test_fuml::basicbehaviors::behavior_constructor_exists():
    assert callable(fuml::BasicBehaviors::Behavior.__init__)


def test_fuml::basicbehaviors::behavior_constructor_args():
    sig = inspect.signature(fuml::BasicBehaviors::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "reentrant" in params, "Missing parameter 'reentrant'"

def test_fuml::basicbehaviors::behavior_has_reentrant():
    assert hasattr(fuml::BasicBehaviors::Behavior, "reentrant")
    descriptor = None
    for klass in fuml::BasicBehaviors::Behavior.__mro__:
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



def test_fuml::intermediateactivities::activity_is_not_abstract():
    assert not inspect.isabstract(fuml::IntermediateActivities::Activity)


def test_fuml::intermediateactivities::activity_constructor_exists():
    assert callable(fuml::IntermediateActivities::Activity.__init__)


def test_fuml::intermediateactivities::activity_constructor_args():
    sig = inspect.signature(fuml::IntermediateActivities::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_fuml::intermediateactivities::activity_has_readOnly():
    assert hasattr(fuml::IntermediateActivities::Activity, "readOnly")
    descriptor = None
    for klass in fuml::IntermediateActivities::Activity.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_fuml::basicbehaviors::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(fuml::BasicBehaviors::OpaqueBehavior)


def test_fuml::basicbehaviors::opaquebehavior_constructor_exists():
    assert callable(fuml::BasicBehaviors::OpaqueBehavior.__init__)


def test_fuml::basicbehaviors::opaquebehavior_constructor_args():
    sig = inspect.signature(fuml::BasicBehaviors::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_fuml::basicbehaviors::opaquebehavior_has_body():
    assert hasattr(fuml::BasicBehaviors::OpaqueBehavior, "body")
    descriptor = None
    for klass in fuml::BasicBehaviors::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_fuml::basicbehaviors::opaquebehavior_has_language():
    assert hasattr(fuml::BasicBehaviors::OpaqueBehavior, "language")
    descriptor = None
    for klass in fuml::BasicBehaviors::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "package",
        "protected",
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

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
fuml::BasicBehaviors::ParameterValue_strategy = st.builds(
    fuml::BasicBehaviors::ParameterValue,
)
Kernel::ExtensionalValue_strategy = st.builds(
    Kernel::ExtensionalValue,
)
fuml::LociL1::Locus_strategy = st.builds(
    fuml::LociL1::Locus,
)
fuml::LociL1::SemanticVisitor_strategy = st.builds(
    fuml::LociL1::SemanticVisitor,
)
SemanticVisitor_strategy = st.builds(
    SemanticVisitor,
)
fuml::Kernel::Value_strategy = st.builds(
    fuml::Kernel::Value,
)
LociL1::Locus_strategy = st.builds(
    LociL1::Locus,
)
CompoundValue_strategy = st.builds(
    CompoundValue,
)
fuml::Kernel::DataValue_strategy = st.builds(
    fuml::Kernel::DataValue,
)
fuml::Kernel::ExtensionalValue_strategy = st.builds(
    fuml::Kernel::ExtensionalValue,
)
ExtensionalValue_strategy = st.builds(
    ExtensionalValue,
)
fuml::Kernel::Object_strategy = st.builds(
    fuml::Kernel::Object,
)
Kernel::Object_strategy = st.builds(
    Kernel::Object,
)
StructuredValue_strategy = st.builds(
    StructuredValue,
)
fuml::Kernel::CompoundValue_strategy = st.builds(
    fuml::Kernel::CompoundValue,
)
fuml::Kernel::Reference_strategy = st.builds(
    fuml::Kernel::Reference,
)
Kernel::PrimitiveType_strategy = st.builds(
    Kernel::PrimitiveType,
)
PrimitiveValue_strategy = st.builds(
    PrimitiveValue,
)
fuml::Kernel::IntegerValue_strategy = st.builds(
    fuml::Kernel::IntegerValue,
    value=
        st.integers()
)
fuml::Kernel::StringValue_strategy = st.builds(
    fuml::Kernel::StringValue,
    value=
        safe_text
)
fuml::Kernel::BooleanValue_strategy = st.builds(
    fuml::Kernel::BooleanValue,
    value=
        st.booleans()
)
fuml::Kernel::UnlimitedNaturalValue_strategy = st.builds(
    fuml::Kernel::UnlimitedNaturalValue,
    value=
        st.integers()
)
Kernel::Value_strategy = st.builds(
    Kernel::Value,
)
fuml::Kernel::FeatureValue_strategy = st.builds(
    fuml::Kernel::FeatureValue,
    position=
        st.integers()
)
fuml::Kernel::Link_strategy = st.builds(
    fuml::Kernel::Link,
)
Kernel::FeatureValue_strategy = st.builds(
    Kernel::FeatureValue,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
fuml::BasicActions::SendSignalAction_strategy = st.builds(
    fuml::BasicActions::SendSignalAction,
)
fuml::BasicActions::CallAction_strategy = st.builds(
    fuml::BasicActions::CallAction,
    synchronous=
        st.booleans()
)
IntermediateActivities::ObjectNode_strategy = st.builds(
    IntermediateActivities::ObjectNode,
)
Pin_strategy = st.builds(
    Pin,
)
fuml::BasicActions::OutputPin_strategy = st.builds(
    fuml::BasicActions::OutputPin,
)
fuml::BasicActions::InputPin_strategy = st.builds(
    fuml::BasicActions::InputPin,
)
Value_strategy = st.builds(
    Value,
)
fuml::Kernel::EnumerationValue_strategy = st.builds(
    fuml::Kernel::EnumerationValue,
)
fuml::Kernel::PrimitiveValue_strategy = st.builds(
    fuml::Kernel::PrimitiveValue,
)
fuml::Kernel::StructuredValue_strategy = st.builds(
    fuml::Kernel::StructuredValue,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
fuml::BasicActions::Action_strategy = st.builds(
    fuml::BasicActions::Action,
    locallyReentrant=
        st.booleans()
)
Communications::Trigger_strategy = st.builds(
    Communications::Trigger,
)
CallAction_strategy = st.builds(
    CallAction,
)
fuml::BasicActions::CallOperationAction_strategy = st.builds(
    fuml::BasicActions::CallOperationAction,
)
fuml::BasicActions::CallBehaviorAction_strategy = st.builds(
    fuml::BasicActions::CallBehaviorAction,
)
fuml::CompleteActions::StartObjectBehaviorAction_strategy = st.builds(
    fuml::CompleteActions::StartObjectBehaviorAction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
fuml::IntermediateActions::DestroyLinkAction_strategy = st.builds(
    fuml::IntermediateActions::DestroyLinkAction,
)
fuml::IntermediateActions::CreateLinkAction_strategy = st.builds(
    fuml::IntermediateActions::CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
fuml::IntermediateActions::LinkEndDestructionData_strategy = st.builds(
    fuml::IntermediateActions::LinkEndDestructionData,
    destroyDuplicates=
        st.booleans()
)
fuml::IntermediateActions::LinkEndCreationData_strategy = st.builds(
    fuml::IntermediateActions::LinkEndCreationData,
    replaceAll=
        st.booleans()
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
fuml::IntermediateActions::AddStructuralFeatureValueAction_strategy = st.builds(
    fuml::IntermediateActions::AddStructuralFeatureValueAction,
    replaceAll=
        st.booleans()
)
fuml::IntermediateActions::RemoveStructuralFeatureValueAction_strategy = st.builds(
    fuml::IntermediateActions::RemoveStructuralFeatureValueAction,
    removeDuplicates=
        st.booleans()
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
fuml::IntermediateActions::ReadStructuralFeatureAction_strategy = st.builds(
    fuml::IntermediateActions::ReadStructuralFeatureAction,
)
fuml::IntermediateActions::ClearStructuralFeatureAction_strategy = st.builds(
    fuml::IntermediateActions::ClearStructuralFeatureAction,
)
fuml::IntermediateActions::WriteStructuralFeatureAction_strategy = st.builds(
    fuml::IntermediateActions::WriteStructuralFeatureAction,
)
IntermediateActions::LinkEndData_strategy = st.builds(
    IntermediateActions::LinkEndData,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
fuml::IntermediateActions::ReadLinkAction_strategy = st.builds(
    fuml::IntermediateActions::ReadLinkAction,
)
fuml::IntermediateActions::WriteLinkAction_strategy = st.builds(
    fuml::IntermediateActions::WriteLinkAction,
)
ExtraStructuredActivities::ExpansionNode_strategy = st.builds(
    ExtraStructuredActivities::ExpansionNode,
)
ExtraStructuredActivities::ExpansionRegion_strategy = st.builds(
    ExtraStructuredActivities::ExpansionRegion,
)
Action_strategy = st.builds(
    Action,
)
fuml::CompleteActions::AcceptEventAction_strategy = st.builds(
    fuml::CompleteActions::AcceptEventAction,
    unmarshall=
        st.booleans()
)
fuml::IntermediateActions::CreateObjectAction_strategy = st.builds(
    fuml::IntermediateActions::CreateObjectAction,
)
fuml::CompleteActions::ReduceAction_strategy = st.builds(
    fuml::CompleteActions::ReduceAction,
    ordered=
        st.booleans()
)
fuml::BasicActions::InvocationAction_strategy = st.builds(
    fuml::BasicActions::InvocationAction,
)
fuml::CompleteActions::ReadIsClassifiedObjectAction_strategy = st.builds(
    fuml::CompleteActions::ReadIsClassifiedObjectAction,
    direct=
        st.booleans()
)
fuml::IntermediateActions::ReadSelfAction_strategy = st.builds(
    fuml::IntermediateActions::ReadSelfAction,
)
fuml::CompleteActions::ReadExtentAction_strategy = st.builds(
    fuml::CompleteActions::ReadExtentAction,
)
fuml::CompleteActions::StartClassifierBehaviorAction_strategy = st.builds(
    fuml::CompleteActions::StartClassifierBehaviorAction,
)
fuml::IntermediateActions::TestIdentityAction_strategy = st.builds(
    fuml::IntermediateActions::TestIdentityAction,
)
fuml::IntermediateActions::ClearAssociationAction_strategy = st.builds(
    fuml::IntermediateActions::ClearAssociationAction,
)
fuml::IntermediateActions::ValueSpecificationAction_strategy = st.builds(
    fuml::IntermediateActions::ValueSpecificationAction,
)
fuml::IntermediateActions::StructuralFeatureAction_strategy = st.builds(
    fuml::IntermediateActions::StructuralFeatureAction,
)
fuml::IntermediateActions::DestroyObjectAction_strategy = st.builds(
    fuml::IntermediateActions::DestroyObjectAction,
    destroyLinks=
        st.booleans(),
    destroyOwnedObjects=
        st.booleans()
)
fuml::IntermediateActions::LinkAction_strategy = st.builds(
    fuml::IntermediateActions::LinkAction,
)
fuml::CompleteActions::ReclassifyObjectAction_strategy = st.builds(
    fuml::CompleteActions::ReclassifyObjectAction,
    replaceAll=
        st.booleans()
)
fuml::CompleteStructuredActivities::StructuredActivityNode_strategy = st.builds(
    fuml::CompleteStructuredActivities::StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
CompleteStructuredActivities::Clause_strategy = st.builds(
    CompleteStructuredActivities::Clause,
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
fuml::ExtraStructuredActivities::ExpansionRegion_strategy = st.builds(
    fuml::ExtraStructuredActivities::ExpansionRegion,
    mode=
        safe_text
)
fuml::CompleteStructuredActivities::ConditionalNode_strategy = st.builds(
    fuml::CompleteStructuredActivities::ConditionalNode,
    determinate=
        st.booleans(),
    assured=
        st.booleans()
)
fuml::CompleteStructuredActivities::LoopNode_strategy = st.builds(
    fuml::CompleteStructuredActivities::LoopNode,
    testedFirst=
        st.booleans()
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
fuml::ExtraStructuredActivities::ExpansionNode_strategy = st.builds(
    fuml::ExtraStructuredActivities::ExpansionNode,
)
fuml::IntermediateActivities::ActivityParameterNode_strategy = st.builds(
    fuml::IntermediateActivities::ActivityParameterNode,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
fuml::IntermediateActivities::ActivityFinalNode_strategy = st.builds(
    fuml::IntermediateActivities::ActivityFinalNode,
)
IntermediateActivities::ObjectFlow_strategy = st.builds(
    IntermediateActivities::ObjectFlow,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
fuml::CompleteStructuredActivities::ExecutableNode_strategy = st.builds(
    fuml::CompleteStructuredActivities::ExecutableNode,
)
fuml::IntermediateActivities::ControlNode_strategy = st.builds(
    fuml::IntermediateActivities::ControlNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
fuml::IntermediateActivities::ForkNode_strategy = st.builds(
    fuml::IntermediateActivities::ForkNode,
)
fuml::IntermediateActivities::FinalNode_strategy = st.builds(
    fuml::IntermediateActivities::FinalNode,
)
fuml::IntermediateActivities::InitialNode_strategy = st.builds(
    fuml::IntermediateActivities::InitialNode,
)
fuml::IntermediateActivities::JoinNode_strategy = st.builds(
    fuml::IntermediateActivities::JoinNode,
)
fuml::IntermediateActivities::DecisionNode_strategy = st.builds(
    fuml::IntermediateActivities::DecisionNode,
)
fuml::IntermediateActivities::MergeNode_strategy = st.builds(
    fuml::IntermediateActivities::MergeNode,
)
IntermediateActivities::ActivityEdge_strategy = st.builds(
    IntermediateActivities::ActivityEdge,
)
CompleteStructuredActivities::StructuredActivityNode_strategy = st.builds(
    CompleteStructuredActivities::StructuredActivityNode,
)
IntermediateActivities::ActivityNode_strategy = st.builds(
    IntermediateActivities::ActivityNode,
)
IntermediateActivities::Activity_strategy = st.builds(
    IntermediateActivities::Activity,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
fuml::IntermediateActivities::ControlFlow_strategy = st.builds(
    fuml::IntermediateActivities::ControlFlow,
)
fuml::IntermediateActivities::ObjectFlow_strategy = st.builds(
    fuml::IntermediateActivities::ObjectFlow,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
fuml::Kernel::LiteralBoolean_strategy = st.builds(
    fuml::Kernel::LiteralBoolean,
    value=
        st.booleans()
)
Communications::Reception_strategy = st.builds(
    Communications::Reception,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
fuml::Kernel::Class_strategy = st.builds(
    fuml::Kernel::Class,
    active=
        st.booleans()
)
Kernel::Enumeration_strategy = st.builds(
    Kernel::Enumeration,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
fuml::Kernel::EnumerationLiteral_strategy = st.builds(
    fuml::Kernel::EnumerationLiteral,
)
Kernel::EnumerationLiteral_strategy = st.builds(
    Kernel::EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
fuml::Kernel::Enumeration_strategy = st.builds(
    fuml::Kernel::Enumeration,
)
fuml::Kernel::PrimitiveType_strategy = st.builds(
    fuml::Kernel::PrimitiveType,
)
fuml::Kernel::LiteralUnlimitedNatural_strategy = st.builds(
    fuml::Kernel::LiteralUnlimitedNatural,
    value=
        st.integers()
)
fuml::Kernel::LiteralString_strategy = st.builds(
    fuml::Kernel::LiteralString,
    value=
        safe_text
)
fuml::Kernel::LiteralNull_strategy = st.builds(
    fuml::Kernel::LiteralNull,
)
fuml::Kernel::LiteralInteger_strategy = st.builds(
    fuml::Kernel::LiteralInteger,
    value=
        st.integers()
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
fuml::Kernel::LiteralSpecification_strategy = st.builds(
    fuml::Kernel::LiteralSpecification,
)
fuml::Kernel::InstanceValue_strategy = st.builds(
    fuml::Kernel::InstanceValue,
)
Kernel::InstanceSpecification_strategy = st.builds(
    Kernel::InstanceSpecification,
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
Feature_strategy = st.builds(
    Feature,
)
fuml::Kernel::BehavioralFeature_strategy = st.builds(
    fuml::Kernel::BehavioralFeature,
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
fuml::Kernel::Property_strategy = st.builds(
    fuml::Kernel::Property,
    aggregation=
        safe_text,
    derived=
        st.booleans(),
    composite=
        st.booleans(),
    derivedUnion=
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
fuml::IntermediateActivities::ActivityNode_strategy = st.builds(
    fuml::IntermediateActivities::ActivityNode,
)
fuml::IntermediateActivities::ActivityEdge_strategy = st.builds(
    fuml::IntermediateActivities::ActivityEdge,
)
fuml::Kernel::Feature_strategy = st.builds(
    fuml::Kernel::Feature,
    static=
        st.booleans()
)
Kernel::TypedElement_strategy = st.builds(
    Kernel::TypedElement,
)
fuml::IntermediateActivities::ObjectNode_strategy = st.builds(
    fuml::IntermediateActivities::ObjectNode,
)
Kernel::MultiplicityElement_strategy = st.builds(
    Kernel::MultiplicityElement,
)
fuml::BasicActions::Pin_strategy = st.builds(
    fuml::BasicActions::Pin,
)
fuml::Kernel::Parameter_strategy = st.builds(
    fuml::Kernel::Parameter,
    direction=
        safe_text
)
Kernel::Feature_strategy = st.builds(
    Kernel::Feature,
)
fuml::Kernel::StructuralFeature_strategy = st.builds(
    fuml::Kernel::StructuralFeature,
    readOnly=
        st.booleans()
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
fuml::Kernel::Comment_strategy = st.builds(
    fuml::Kernel::Comment,
    body=
        safe_text
)
Kernel::Comment_strategy = st.builds(
    Kernel::Comment,
)
Kernel::Element_strategy = st.builds(
    Kernel::Element,
)
fuml::Kernel::Element_strategy = st.builds(
    fuml::Kernel::Element,
)
Kernel::Namespace_strategy = st.builds(
    Kernel::Namespace,
)
fuml::Kernel::Package_strategy = st.builds(
    fuml::Kernel::Package,
)
Element_strategy = st.builds(
    Element,
)
fuml::IntermediateActions::LinkEndData_strategy = st.builds(
    fuml::IntermediateActions::LinkEndData,
)
fuml::Kernel::MultiplicityElement_strategy = st.builds(
    fuml::Kernel::MultiplicityElement,
    lower=
        st.integers(),
    ordered=
        st.booleans(),
    upper=
        st.integers(),
    unique=
        st.booleans()
)
fuml::Kernel::ElementImport_strategy = st.builds(
    fuml::Kernel::ElementImport,
    visibility=
        safe_text,
    alias=
        safe_text
)
fuml::CompleteStructuredActivities::Clause_strategy = st.builds(
    fuml::CompleteStructuredActivities::Clause,
)
fuml::Kernel::Slot_strategy = st.builds(
    fuml::Kernel::Slot,
)
fuml::Kernel::PackageImport_strategy = st.builds(
    fuml::Kernel::PackageImport,
    visibility=
        safe_text
)
fuml::Kernel::Generalization_strategy = st.builds(
    fuml::Kernel::Generalization,
    substitutable=
        st.booleans()
)
fuml::Kernel::NamedElement_strategy = st.builds(
    fuml::Kernel::NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text,
    visibility=
        safe_text
)
Kernel::Type_strategy = st.builds(
    Kernel::Type,
)
fuml::Kernel::Classifier_strategy = st.builds(
    fuml::Kernel::Classifier,
    finalSpecialization=
        st.booleans(),
    abstract=
        st.booleans()
)
TypedElement_strategy = st.builds(
    TypedElement,
)
fuml::Kernel::ValueSpecification_strategy = st.builds(
    fuml::Kernel::ValueSpecification,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
fuml::Kernel::Operation_strategy = st.builds(
    fuml::Kernel::Operation,
    ordered=
        st.booleans(),
    upper=
        st.integers(),
    lower=
        st.integers(),
    query=
        st.booleans(),
    unique=
        st.booleans()
)
fuml::Communications::Reception_strategy = st.builds(
    fuml::Communications::Reception,
)
Event_strategy = st.builds(
    Event,
)
fuml::Communications::MessageEvent_strategy = st.builds(
    fuml::Communications::MessageEvent,
)
Communications::Signal_strategy = st.builds(
    Communications::Signal,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
fuml::Communications::SignalEvent_strategy = st.builds(
    fuml::Communications::SignalEvent,
)
Kernel::Property_strategy = st.builds(
    Kernel::Property,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
fuml::Kernel::Type_strategy = st.builds(
    fuml::Kernel::Type,
)
fuml::Communications::Event_strategy = st.builds(
    fuml::Communications::Event,
)
Communications::Event_strategy = st.builds(
    Communications::Event,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fuml::Kernel::InstanceSpecification_strategy = st.builds(
    fuml::Kernel::InstanceSpecification,
)
fuml::Kernel::TypedElement_strategy = st.builds(
    fuml::Kernel::TypedElement,
)
fuml::Kernel::Namespace_strategy = st.builds(
    fuml::Kernel::Namespace,
)
fuml::Kernel::PackageableElement_strategy = st.builds(
    fuml::Kernel::PackageableElement,
)
fuml::Kernel::RedefinableElement_strategy = st.builds(
    fuml::Kernel::RedefinableElement,
    leaf=
        st.booleans()
)
fuml::Communications::Trigger_strategy = st.builds(
    fuml::Communications::Trigger,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
fuml::BasicBehaviors::FunctionBehavior_strategy = st.builds(
    fuml::BasicBehaviors::FunctionBehavior,
)
BasicBehaviors::Behavior_strategy = st.builds(
    BasicBehaviors::Behavior,
)
Classifier_strategy = st.builds(
    Classifier,
)
fuml::Kernel::Association_strategy = st.builds(
    fuml::Kernel::Association,
    derived=
        st.booleans()
)
fuml::Kernel::DataType_strategy = st.builds(
    fuml::Kernel::DataType,
)
fuml::Communications::Signal_strategy = st.builds(
    fuml::Communications::Signal,
)
fuml::BasicBehaviors::BehavioredClassifier_strategy = st.builds(
    fuml::BasicBehaviors::BehavioredClassifier,
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
fuml::BasicBehaviors::Behavior_strategy = st.builds(
    fuml::BasicBehaviors::Behavior,
    reentrant=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
fuml::IntermediateActivities::Activity_strategy = st.builds(
    fuml::IntermediateActivities::Activity,
    readOnly=
        st.booleans()
)
fuml::BasicBehaviors::OpaqueBehavior_strategy = st.builds(
    fuml::BasicBehaviors::OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)

@given(instance=fuml::BasicBehaviors::ParameterValue_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::parametervalue_instantiation(instance):
    assert isinstance(instance, fuml::BasicBehaviors::ParameterValue)

@given(instance=Kernel::ExtensionalValue_strategy)
@settings(max_examples=50)
def test_kernel::extensionalvalue_instantiation(instance):
    assert isinstance(instance, Kernel::ExtensionalValue)

@given(instance=fuml::LociL1::Locus_strategy)
@settings(max_examples=50)
def test_fuml::locil1::locus_instantiation(instance):
    assert isinstance(instance, fuml::LociL1::Locus)

@given(instance=fuml::LociL1::SemanticVisitor_strategy)
@settings(max_examples=50)
def test_fuml::locil1::semanticvisitor_instantiation(instance):
    assert isinstance(instance, fuml::LociL1::SemanticVisitor)

@given(instance=SemanticVisitor_strategy)
@settings(max_examples=50)
def test_semanticvisitor_instantiation(instance):
    assert isinstance(instance, SemanticVisitor)

@given(instance=fuml::Kernel::Value_strategy)
@settings(max_examples=50)
def test_fuml::kernel::value_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Value)

@given(instance=LociL1::Locus_strategy)
@settings(max_examples=50)
def test_locil1::locus_instantiation(instance):
    assert isinstance(instance, LociL1::Locus)

@given(instance=CompoundValue_strategy)
@settings(max_examples=50)
def test_compoundvalue_instantiation(instance):
    assert isinstance(instance, CompoundValue)

@given(instance=fuml::Kernel::DataValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::datavalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::DataValue)

@given(instance=fuml::Kernel::ExtensionalValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::extensionalvalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::ExtensionalValue)

@given(instance=ExtensionalValue_strategy)
@settings(max_examples=50)
def test_extensionalvalue_instantiation(instance):
    assert isinstance(instance, ExtensionalValue)

@given(instance=fuml::Kernel::Object_strategy)
@settings(max_examples=50)
def test_fuml::kernel::object_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Object)

@given(instance=Kernel::Object_strategy)
@settings(max_examples=50)
def test_kernel::object_instantiation(instance):
    assert isinstance(instance, Kernel::Object)

@given(instance=StructuredValue_strategy)
@settings(max_examples=50)
def test_structuredvalue_instantiation(instance):
    assert isinstance(instance, StructuredValue)

@given(instance=fuml::Kernel::CompoundValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::compoundvalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::CompoundValue)

@given(instance=fuml::Kernel::Reference_strategy)
@settings(max_examples=50)
def test_fuml::kernel::reference_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Reference)

@given(instance=Kernel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_kernel::primitivetype_instantiation(instance):
    assert isinstance(instance, Kernel::PrimitiveType)

@given(instance=PrimitiveValue_strategy)
@settings(max_examples=50)
def test_primitivevalue_instantiation(instance):
    assert isinstance(instance, PrimitiveValue)

@given(instance=fuml::Kernel::IntegerValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::integervalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::IntegerValue)

@given(instance=fuml::Kernel::IntegerValue_strategy)
def test_fuml::kernel::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fuml::Kernel::IntegerValue_strategy)
def test_fuml::kernel::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fuml::Kernel::StringValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::stringvalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::StringValue)

@given(instance=fuml::Kernel::StringValue_strategy)
def test_fuml::kernel::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fuml::Kernel::StringValue_strategy)
def test_fuml::kernel::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fuml::Kernel::BooleanValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::booleanvalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::BooleanValue)

@given(instance=fuml::Kernel::BooleanValue_strategy)
def test_fuml::kernel::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fuml::Kernel::BooleanValue_strategy)
def test_fuml::kernel::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fuml::Kernel::UnlimitedNaturalValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::unlimitednaturalvalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::UnlimitedNaturalValue)

@given(instance=fuml::Kernel::UnlimitedNaturalValue_strategy)
def test_fuml::kernel::unlimitednaturalvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fuml::Kernel::UnlimitedNaturalValue_strategy)
def test_fuml::kernel::unlimitednaturalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel::Value_strategy)
@settings(max_examples=50)
def test_kernel::value_instantiation(instance):
    assert isinstance(instance, Kernel::Value)

@given(instance=fuml::Kernel::FeatureValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::featurevalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::FeatureValue)

@given(instance=fuml::Kernel::FeatureValue_strategy)
def test_fuml::kernel::featurevalue_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=fuml::Kernel::FeatureValue_strategy)
def test_fuml::kernel::featurevalue_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=fuml::Kernel::Link_strategy)
@settings(max_examples=50)
def test_fuml::kernel::link_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Link)

@given(instance=Kernel::FeatureValue_strategy)
@settings(max_examples=50)
def test_kernel::featurevalue_instantiation(instance):
    assert isinstance(instance, Kernel::FeatureValue)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=fuml::BasicActions::SendSignalAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::sendsignalaction_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::SendSignalAction)

@given(instance=fuml::BasicActions::CallAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::callaction_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::CallAction)

@given(instance=fuml::BasicActions::CallAction_strategy)
def test_fuml::basicactions::callaction_synchronous_type(instance):
    assert isinstance(instance.synchronous, bool)


@given(instance=fuml::BasicActions::CallAction_strategy)
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

@given(instance=fuml::BasicActions::OutputPin_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::outputpin_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::OutputPin)

@given(instance=fuml::BasicActions::InputPin_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::inputpin_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::InputPin)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=fuml::Kernel::EnumerationValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::enumerationvalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::EnumerationValue)

@given(instance=fuml::Kernel::PrimitiveValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::primitivevalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::PrimitiveValue)

@given(instance=fuml::Kernel::StructuredValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::structuredvalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::StructuredValue)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=fuml::BasicActions::Action_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::action_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::Action)

@given(instance=fuml::BasicActions::Action_strategy)
def test_fuml::basicactions::action_locallyReentrant_type(instance):
    assert isinstance(instance.locallyReentrant, bool)


@given(instance=fuml::BasicActions::Action_strategy)
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

@given(instance=fuml::BasicActions::CallOperationAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::calloperationaction_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::CallOperationAction)

@given(instance=fuml::BasicActions::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::callbehavioraction_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::CallBehaviorAction)

@given(instance=fuml::CompleteActions::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, fuml::CompleteActions::StartObjectBehaviorAction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=fuml::IntermediateActions::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::destroylinkaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::DestroyLinkAction)

@given(instance=fuml::IntermediateActions::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::createlinkaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::CreateLinkAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=fuml::IntermediateActions::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::LinkEndDestructionData)

@given(instance=fuml::IntermediateActions::LinkEndDestructionData_strategy)
def test_fuml::intermediateactions::linkenddestructiondata_destroyDuplicates_type(instance):
    assert isinstance(instance.destroyDuplicates, bool)


@given(instance=fuml::IntermediateActions::LinkEndDestructionData_strategy)
def test_fuml::intermediateactions::linkenddestructiondata_destroyDuplicates_setter(instance):
    original = instance.destroyDuplicates
    instance.destroyDuplicates = original
    assert instance.destroyDuplicates == original

@given(instance=fuml::IntermediateActions::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::LinkEndCreationData)

@given(instance=fuml::IntermediateActions::LinkEndCreationData_strategy)
def test_fuml::intermediateactions::linkendcreationdata_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=fuml::IntermediateActions::LinkEndCreationData_strategy)
def test_fuml::intermediateactions::linkendcreationdata_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=fuml::IntermediateActions::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::AddStructuralFeatureValueAction)

@given(instance=fuml::IntermediateActions::AddStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::addstructuralfeaturevalueaction_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=fuml::IntermediateActions::AddStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::addstructuralfeaturevalueaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=fuml::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::RemoveStructuralFeatureValueAction)

@given(instance=fuml::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::removestructuralfeaturevalueaction_removeDuplicates_type(instance):
    assert isinstance(instance.removeDuplicates, bool)


@given(instance=fuml::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
def test_fuml::intermediateactions::removestructuralfeaturevalueaction_removeDuplicates_setter(instance):
    original = instance.removeDuplicates
    instance.removeDuplicates = original
    assert instance.removeDuplicates == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=fuml::IntermediateActions::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::ReadStructuralFeatureAction)

@given(instance=fuml::IntermediateActions::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::ClearStructuralFeatureAction)

@given(instance=fuml::IntermediateActions::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::WriteStructuralFeatureAction)

@given(instance=IntermediateActions::LinkEndData_strategy)
@settings(max_examples=50)
def test_intermediateactions::linkenddata_instantiation(instance):
    assert isinstance(instance, IntermediateActions::LinkEndData)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=fuml::IntermediateActions::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::readlinkaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::ReadLinkAction)

@given(instance=fuml::IntermediateActions::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::writelinkaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::WriteLinkAction)

@given(instance=ExtraStructuredActivities::ExpansionNode_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities::expansionnode_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities::ExpansionNode)

@given(instance=ExtraStructuredActivities::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities::expansionregion_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities::ExpansionRegion)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=fuml::CompleteActions::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::accepteventaction_instantiation(instance):
    assert isinstance(instance, fuml::CompleteActions::AcceptEventAction)

@given(instance=fuml::CompleteActions::AcceptEventAction_strategy)
def test_fuml::completeactions::accepteventaction_unmarshall_type(instance):
    assert isinstance(instance.unmarshall, bool)


@given(instance=fuml::CompleteActions::AcceptEventAction_strategy)
def test_fuml::completeactions::accepteventaction_unmarshall_setter(instance):
    original = instance.unmarshall
    instance.unmarshall = original
    assert instance.unmarshall == original

@given(instance=fuml::IntermediateActions::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::createobjectaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::CreateObjectAction)

@given(instance=fuml::CompleteActions::ReduceAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::reduceaction_instantiation(instance):
    assert isinstance(instance, fuml::CompleteActions::ReduceAction)

@given(instance=fuml::CompleteActions::ReduceAction_strategy)
def test_fuml::completeactions::reduceaction_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=fuml::CompleteActions::ReduceAction_strategy)
def test_fuml::completeactions::reduceaction_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fuml::BasicActions::InvocationAction_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::invocationaction_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::InvocationAction)

@given(instance=fuml::CompleteActions::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, fuml::CompleteActions::ReadIsClassifiedObjectAction)

@given(instance=fuml::CompleteActions::ReadIsClassifiedObjectAction_strategy)
def test_fuml::completeactions::readisclassifiedobjectaction_direct_type(instance):
    assert isinstance(instance.direct, bool)


@given(instance=fuml::CompleteActions::ReadIsClassifiedObjectAction_strategy)
def test_fuml::completeactions::readisclassifiedobjectaction_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original

@given(instance=fuml::IntermediateActions::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::readselfaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::ReadSelfAction)

@given(instance=fuml::CompleteActions::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::readextentaction_instantiation(instance):
    assert isinstance(instance, fuml::CompleteActions::ReadExtentAction)

@given(instance=fuml::CompleteActions::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, fuml::CompleteActions::StartClassifierBehaviorAction)

@given(instance=fuml::IntermediateActions::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::testidentityaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::TestIdentityAction)

@given(instance=fuml::IntermediateActions::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::clearassociationaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::ClearAssociationAction)

@given(instance=fuml::IntermediateActions::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::ValueSpecificationAction)

@given(instance=fuml::IntermediateActions::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::StructuralFeatureAction)

@given(instance=fuml::IntermediateActions::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::DestroyObjectAction)

@given(instance=fuml::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyLinks_type(instance):
    assert isinstance(instance.destroyLinks, bool)


@given(instance=fuml::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyLinks_setter(instance):
    original = instance.destroyLinks
    instance.destroyLinks = original
    assert instance.destroyLinks == original

@given(instance=fuml::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyOwnedObjects_type(instance):
    assert isinstance(instance.destroyOwnedObjects, bool)


@given(instance=fuml::IntermediateActions::DestroyObjectAction_strategy)
def test_fuml::intermediateactions::destroyobjectaction_destroyOwnedObjects_setter(instance):
    original = instance.destroyOwnedObjects
    instance.destroyOwnedObjects = original
    assert instance.destroyOwnedObjects == original

@given(instance=fuml::IntermediateActions::LinkAction_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkaction_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::LinkAction)

@given(instance=fuml::CompleteActions::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_fuml::completeactions::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, fuml::CompleteActions::ReclassifyObjectAction)

@given(instance=fuml::CompleteActions::ReclassifyObjectAction_strategy)
def test_fuml::completeactions::reclassifyobjectaction_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=fuml::CompleteActions::ReclassifyObjectAction_strategy)
def test_fuml::completeactions::reclassifyobjectaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=fuml::CompleteStructuredActivities::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, fuml::CompleteStructuredActivities::StructuredActivityNode)

@given(instance=fuml::CompleteStructuredActivities::StructuredActivityNode_strategy)
def test_fuml::completestructuredactivities::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, bool)


@given(instance=fuml::CompleteStructuredActivities::StructuredActivityNode_strategy)
def test_fuml::completestructuredactivities::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=CompleteStructuredActivities::Clause_strategy)
@settings(max_examples=50)
def test_completestructuredactivities::clause_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities::Clause)

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

@given(instance=fuml::ExtraStructuredActivities::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_fuml::extrastructuredactivities::expansionregion_instantiation(instance):
    assert isinstance(instance, fuml::ExtraStructuredActivities::ExpansionRegion)

@given(instance=fuml::ExtraStructuredActivities::ExpansionRegion_strategy)
def test_fuml::extrastructuredactivities::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=fuml::ExtraStructuredActivities::ExpansionRegion_strategy)
def test_fuml::extrastructuredactivities::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=fuml::CompleteStructuredActivities::ConditionalNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::conditionalnode_instantiation(instance):
    assert isinstance(instance, fuml::CompleteStructuredActivities::ConditionalNode)

@given(instance=fuml::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_determinate_type(instance):
    assert isinstance(instance.determinate, bool)


@given(instance=fuml::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_determinate_setter(instance):
    original = instance.determinate
    instance.determinate = original
    assert instance.determinate == original

@given(instance=fuml::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_assured_type(instance):
    assert isinstance(instance.assured, bool)


@given(instance=fuml::CompleteStructuredActivities::ConditionalNode_strategy)
def test_fuml::completestructuredactivities::conditionalnode_assured_setter(instance):
    original = instance.assured
    instance.assured = original
    assert instance.assured == original

@given(instance=fuml::CompleteStructuredActivities::LoopNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::loopnode_instantiation(instance):
    assert isinstance(instance, fuml::CompleteStructuredActivities::LoopNode)

@given(instance=fuml::CompleteStructuredActivities::LoopNode_strategy)
def test_fuml::completestructuredactivities::loopnode_testedFirst_type(instance):
    assert isinstance(instance.testedFirst, bool)


@given(instance=fuml::CompleteStructuredActivities::LoopNode_strategy)
def test_fuml::completestructuredactivities::loopnode_testedFirst_setter(instance):
    original = instance.testedFirst
    instance.testedFirst = original
    assert instance.testedFirst == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=fuml::ExtraStructuredActivities::ExpansionNode_strategy)
@settings(max_examples=50)
def test_fuml::extrastructuredactivities::expansionnode_instantiation(instance):
    assert isinstance(instance, fuml::ExtraStructuredActivities::ExpansionNode)

@given(instance=fuml::IntermediateActivities::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activityparameternode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ActivityParameterNode)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=fuml::IntermediateActivities::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activityfinalnode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ActivityFinalNode)

@given(instance=IntermediateActivities::ObjectFlow_strategy)
@settings(max_examples=50)
def test_intermediateactivities::objectflow_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ObjectFlow)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=fuml::CompleteStructuredActivities::ExecutableNode_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::executablenode_instantiation(instance):
    assert isinstance(instance, fuml::CompleteStructuredActivities::ExecutableNode)

@given(instance=fuml::IntermediateActivities::ControlNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::controlnode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ControlNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=fuml::IntermediateActivities::ForkNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::forknode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ForkNode)

@given(instance=fuml::IntermediateActivities::FinalNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::finalnode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::FinalNode)

@given(instance=fuml::IntermediateActivities::InitialNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::initialnode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::InitialNode)

@given(instance=fuml::IntermediateActivities::JoinNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::joinnode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::JoinNode)

@given(instance=fuml::IntermediateActivities::DecisionNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::decisionnode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::DecisionNode)

@given(instance=fuml::IntermediateActivities::MergeNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::mergenode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::MergeNode)

@given(instance=IntermediateActivities::ActivityEdge_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activityedge_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ActivityEdge)

@given(instance=CompleteStructuredActivities::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_completestructuredactivities::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities::StructuredActivityNode)

@given(instance=IntermediateActivities::ActivityNode_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activitynode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ActivityNode)

@given(instance=IntermediateActivities::Activity_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activity_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::Activity)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=fuml::IntermediateActivities::ControlFlow_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::controlflow_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ControlFlow)

@given(instance=fuml::IntermediateActivities::ObjectFlow_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::objectflow_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ObjectFlow)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=fuml::Kernel::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalboolean_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::LiteralBoolean)

@given(instance=fuml::Kernel::LiteralBoolean_strategy)
def test_fuml::kernel::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fuml::Kernel::LiteralBoolean_strategy)
def test_fuml::kernel::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Communications::Reception_strategy)
@settings(max_examples=50)
def test_communications::reception_instantiation(instance):
    assert isinstance(instance, Communications::Reception)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=fuml::Kernel::Class_strategy)
@settings(max_examples=50)
def test_fuml::kernel::class_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Class)

@given(instance=fuml::Kernel::Class_strategy)
def test_fuml::kernel::class_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=fuml::Kernel::Class_strategy)
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

@given(instance=fuml::Kernel::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_fuml::kernel::enumerationliteral_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::EnumerationLiteral)

@given(instance=Kernel::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_kernel::enumerationliteral_instantiation(instance):
    assert isinstance(instance, Kernel::EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=fuml::Kernel::Enumeration_strategy)
@settings(max_examples=50)
def test_fuml::kernel::enumeration_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Enumeration)

@given(instance=fuml::Kernel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_fuml::kernel::primitivetype_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::PrimitiveType)

@given(instance=fuml::Kernel::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::LiteralUnlimitedNatural)

@given(instance=fuml::Kernel::LiteralUnlimitedNatural_strategy)
def test_fuml::kernel::literalunlimitednatural_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fuml::Kernel::LiteralUnlimitedNatural_strategy)
def test_fuml::kernel::literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fuml::Kernel::LiteralString_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalstring_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::LiteralString)

@given(instance=fuml::Kernel::LiteralString_strategy)
def test_fuml::kernel::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fuml::Kernel::LiteralString_strategy)
def test_fuml::kernel::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fuml::Kernel::LiteralNull_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalnull_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::LiteralNull)

@given(instance=fuml::Kernel::LiteralInteger_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalinteger_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::LiteralInteger)

@given(instance=fuml::Kernel::LiteralInteger_strategy)
def test_fuml::kernel::literalinteger_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fuml::Kernel::LiteralInteger_strategy)
def test_fuml::kernel::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=fuml::Kernel::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_fuml::kernel::literalspecification_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::LiteralSpecification)

@given(instance=fuml::Kernel::InstanceValue_strategy)
@settings(max_examples=50)
def test_fuml::kernel::instancevalue_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::InstanceValue)

@given(instance=Kernel::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_kernel::instancespecification_instantiation(instance):
    assert isinstance(instance, Kernel::InstanceSpecification)

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

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=fuml::Kernel::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_fuml::kernel::behavioralfeature_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::BehavioralFeature)

@given(instance=fuml::Kernel::BehavioralFeature_strategy)
def test_fuml::kernel::behavioralfeature_concurrency_type(instance):
    assert isinstance(instance.concurrency, str)


@given(instance=fuml::Kernel::BehavioralFeature_strategy)
def test_fuml::kernel::behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=fuml::Kernel::BehavioralFeature_strategy)
def test_fuml::kernel::behavioralfeature_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=fuml::Kernel::BehavioralFeature_strategy)
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

@given(instance=fuml::Kernel::Property_strategy)
@settings(max_examples=50)
def test_fuml::kernel::property_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Property)

@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_composite_type(instance):
    assert isinstance(instance.composite, bool)


@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_composite_setter(instance):
    original = instance.composite
    instance.composite = original
    assert instance.composite == original

@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_derivedUnion_type(instance):
    assert isinstance(instance.derivedUnion, bool)


@given(instance=fuml::Kernel::Property_strategy)
def test_fuml::kernel::property_derivedUnion_setter(instance):
    original = instance.derivedUnion
    instance.derivedUnion = original
    assert instance.derivedUnion == original

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

@given(instance=fuml::IntermediateActivities::ActivityNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activitynode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ActivityNode)

@given(instance=fuml::IntermediateActivities::ActivityEdge_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activityedge_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ActivityEdge)

@given(instance=fuml::Kernel::Feature_strategy)
@settings(max_examples=50)
def test_fuml::kernel::feature_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Feature)

@given(instance=fuml::Kernel::Feature_strategy)
def test_fuml::kernel::feature_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=fuml::Kernel::Feature_strategy)
def test_fuml::kernel::feature_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Kernel::TypedElement_strategy)
@settings(max_examples=50)
def test_kernel::typedelement_instantiation(instance):
    assert isinstance(instance, Kernel::TypedElement)

@given(instance=fuml::IntermediateActivities::ObjectNode_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::objectnode_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::ObjectNode)

@given(instance=Kernel::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_kernel::multiplicityelement_instantiation(instance):
    assert isinstance(instance, Kernel::MultiplicityElement)

@given(instance=fuml::BasicActions::Pin_strategy)
@settings(max_examples=50)
def test_fuml::basicactions::pin_instantiation(instance):
    assert isinstance(instance, fuml::BasicActions::Pin)

@given(instance=fuml::Kernel::Parameter_strategy)
@settings(max_examples=50)
def test_fuml::kernel::parameter_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Parameter)

@given(instance=fuml::Kernel::Parameter_strategy)
def test_fuml::kernel::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=fuml::Kernel::Parameter_strategy)
def test_fuml::kernel::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Kernel::Feature_strategy)
@settings(max_examples=50)
def test_kernel::feature_instantiation(instance):
    assert isinstance(instance, Kernel::Feature)

@given(instance=fuml::Kernel::StructuralFeature_strategy)
@settings(max_examples=50)
def test_fuml::kernel::structuralfeature_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::StructuralFeature)

@given(instance=fuml::Kernel::StructuralFeature_strategy)
def test_fuml::kernel::structuralfeature_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=fuml::Kernel::StructuralFeature_strategy)
def test_fuml::kernel::structuralfeature_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

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

@given(instance=fuml::Kernel::Comment_strategy)
@settings(max_examples=50)
def test_fuml::kernel::comment_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Comment)

@given(instance=fuml::Kernel::Comment_strategy)
def test_fuml::kernel::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=fuml::Kernel::Comment_strategy)
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

@given(instance=fuml::Kernel::Element_strategy)
@settings(max_examples=50)
def test_fuml::kernel::element_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Element)

@given(instance=Kernel::Namespace_strategy)
@settings(max_examples=50)
def test_kernel::namespace_instantiation(instance):
    assert isinstance(instance, Kernel::Namespace)

@given(instance=fuml::Kernel::Package_strategy)
@settings(max_examples=50)
def test_fuml::kernel::package_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Package)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=fuml::IntermediateActions::LinkEndData_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactions::linkenddata_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActions::LinkEndData)

@given(instance=fuml::Kernel::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::multiplicityelement_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::MultiplicityElement)

@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=fuml::Kernel::MultiplicityElement_strategy)
def test_fuml::kernel::multiplicityelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=fuml::Kernel::ElementImport_strategy)
@settings(max_examples=50)
def test_fuml::kernel::elementimport_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::ElementImport)

@given(instance=fuml::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=fuml::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=fuml::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=fuml::Kernel::ElementImport_strategy)
def test_fuml::kernel::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=fuml::CompleteStructuredActivities::Clause_strategy)
@settings(max_examples=50)
def test_fuml::completestructuredactivities::clause_instantiation(instance):
    assert isinstance(instance, fuml::CompleteStructuredActivities::Clause)

@given(instance=fuml::Kernel::Slot_strategy)
@settings(max_examples=50)
def test_fuml::kernel::slot_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Slot)

@given(instance=fuml::Kernel::PackageImport_strategy)
@settings(max_examples=50)
def test_fuml::kernel::packageimport_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::PackageImport)

@given(instance=fuml::Kernel::PackageImport_strategy)
def test_fuml::kernel::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=fuml::Kernel::PackageImport_strategy)
def test_fuml::kernel::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=fuml::Kernel::Generalization_strategy)
@settings(max_examples=50)
def test_fuml::kernel::generalization_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Generalization)

@given(instance=fuml::Kernel::Generalization_strategy)
def test_fuml::kernel::generalization_substitutable_type(instance):
    assert isinstance(instance.substitutable, bool)


@given(instance=fuml::Kernel::Generalization_strategy)
def test_fuml::kernel::generalization_substitutable_setter(instance):
    original = instance.substitutable
    instance.substitutable = original
    assert instance.substitutable == original

@given(instance=fuml::Kernel::NamedElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::namedelement_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::NamedElement)

@given(instance=fuml::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fuml::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fuml::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=fuml::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=fuml::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=fuml::Kernel::NamedElement_strategy)
def test_fuml::kernel::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Kernel::Type_strategy)
@settings(max_examples=50)
def test_kernel::type_instantiation(instance):
    assert isinstance(instance, Kernel::Type)

@given(instance=fuml::Kernel::Classifier_strategy)
@settings(max_examples=50)
def test_fuml::kernel::classifier_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Classifier)

@given(instance=fuml::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_finalSpecialization_type(instance):
    assert isinstance(instance.finalSpecialization, bool)


@given(instance=fuml::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_finalSpecialization_setter(instance):
    original = instance.finalSpecialization
    instance.finalSpecialization = original
    assert instance.finalSpecialization == original

@given(instance=fuml::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=fuml::Kernel::Classifier_strategy)
def test_fuml::kernel::classifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=fuml::Kernel::ValueSpecification_strategy)
@settings(max_examples=50)
def test_fuml::kernel::valuespecification_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::ValueSpecification)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=fuml::Kernel::Operation_strategy)
@settings(max_examples=50)
def test_fuml::kernel::operation_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Operation)

@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_query_type(instance):
    assert isinstance(instance.query, bool)


@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=fuml::Kernel::Operation_strategy)
def test_fuml::kernel::operation_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=fuml::Communications::Reception_strategy)
@settings(max_examples=50)
def test_fuml::communications::reception_instantiation(instance):
    assert isinstance(instance, fuml::Communications::Reception)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=fuml::Communications::MessageEvent_strategy)
@settings(max_examples=50)
def test_fuml::communications::messageevent_instantiation(instance):
    assert isinstance(instance, fuml::Communications::MessageEvent)

@given(instance=Communications::Signal_strategy)
@settings(max_examples=50)
def test_communications::signal_instantiation(instance):
    assert isinstance(instance, Communications::Signal)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=fuml::Communications::SignalEvent_strategy)
@settings(max_examples=50)
def test_fuml::communications::signalevent_instantiation(instance):
    assert isinstance(instance, fuml::Communications::SignalEvent)

@given(instance=Kernel::Property_strategy)
@settings(max_examples=50)
def test_kernel::property_instantiation(instance):
    assert isinstance(instance, Kernel::Property)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=fuml::Kernel::Type_strategy)
@settings(max_examples=50)
def test_fuml::kernel::type_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Type)

@given(instance=fuml::Communications::Event_strategy)
@settings(max_examples=50)
def test_fuml::communications::event_instantiation(instance):
    assert isinstance(instance, fuml::Communications::Event)

@given(instance=Communications::Event_strategy)
@settings(max_examples=50)
def test_communications::event_instantiation(instance):
    assert isinstance(instance, Communications::Event)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fuml::Kernel::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_fuml::kernel::instancespecification_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::InstanceSpecification)

@given(instance=fuml::Kernel::TypedElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::typedelement_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::TypedElement)

@given(instance=fuml::Kernel::Namespace_strategy)
@settings(max_examples=50)
def test_fuml::kernel::namespace_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Namespace)

@given(instance=fuml::Kernel::PackageableElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::packageableelement_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::PackageableElement)

@given(instance=fuml::Kernel::RedefinableElement_strategy)
@settings(max_examples=50)
def test_fuml::kernel::redefinableelement_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::RedefinableElement)

@given(instance=fuml::Kernel::RedefinableElement_strategy)
def test_fuml::kernel::redefinableelement_leaf_type(instance):
    assert isinstance(instance.leaf, bool)


@given(instance=fuml::Kernel::RedefinableElement_strategy)
def test_fuml::kernel::redefinableelement_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original

@given(instance=fuml::Communications::Trigger_strategy)
@settings(max_examples=50)
def test_fuml::communications::trigger_instantiation(instance):
    assert isinstance(instance, fuml::Communications::Trigger)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=fuml::BasicBehaviors::FunctionBehavior_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::functionbehavior_instantiation(instance):
    assert isinstance(instance, fuml::BasicBehaviors::FunctionBehavior)

@given(instance=BasicBehaviors::Behavior_strategy)
@settings(max_examples=50)
def test_basicbehaviors::behavior_instantiation(instance):
    assert isinstance(instance, BasicBehaviors::Behavior)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=fuml::Kernel::Association_strategy)
@settings(max_examples=50)
def test_fuml::kernel::association_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::Association)

@given(instance=fuml::Kernel::Association_strategy)
def test_fuml::kernel::association_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=fuml::Kernel::Association_strategy)
def test_fuml::kernel::association_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=fuml::Kernel::DataType_strategy)
@settings(max_examples=50)
def test_fuml::kernel::datatype_instantiation(instance):
    assert isinstance(instance, fuml::Kernel::DataType)

@given(instance=fuml::Communications::Signal_strategy)
@settings(max_examples=50)
def test_fuml::communications::signal_instantiation(instance):
    assert isinstance(instance, fuml::Communications::Signal)

@given(instance=fuml::BasicBehaviors::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, fuml::BasicBehaviors::BehavioredClassifier)

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

@given(instance=fuml::BasicBehaviors::Behavior_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::behavior_instantiation(instance):
    assert isinstance(instance, fuml::BasicBehaviors::Behavior)

@given(instance=fuml::BasicBehaviors::Behavior_strategy)
def test_fuml::basicbehaviors::behavior_reentrant_type(instance):
    assert isinstance(instance.reentrant, bool)


@given(instance=fuml::BasicBehaviors::Behavior_strategy)
def test_fuml::basicbehaviors::behavior_reentrant_setter(instance):
    original = instance.reentrant
    instance.reentrant = original
    assert instance.reentrant == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=fuml::IntermediateActivities::Activity_strategy)
@settings(max_examples=50)
def test_fuml::intermediateactivities::activity_instantiation(instance):
    assert isinstance(instance, fuml::IntermediateActivities::Activity)

@given(instance=fuml::IntermediateActivities::Activity_strategy)
def test_fuml::intermediateactivities::activity_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=fuml::IntermediateActivities::Activity_strategy)
def test_fuml::intermediateactivities::activity_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=fuml::BasicBehaviors::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_fuml::basicbehaviors::opaquebehavior_instantiation(instance):
    assert isinstance(instance, fuml::BasicBehaviors::OpaqueBehavior)

@given(instance=fuml::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=fuml::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=fuml::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=fuml::BasicBehaviors::OpaqueBehavior_strategy)
def test_fuml::basicbehaviors::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

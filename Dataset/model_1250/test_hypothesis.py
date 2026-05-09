import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BasicBehaviors::ParameterValue,
    xmof::BasicBehaviors::ParameterValueDefinition,
    Kernel::Value,
    xmof::BasicBehaviors::ParameterValue,
    PrimitiveValue,
    xmof::Kernel::IntegerValue,
    xmof::Kernel::StringValue,
    Kernel::PrimitiveType,
    Value,
    xmof::Kernel::EnumerationValue,
    xmof::Kernel::PrimitiveValue,
    xmof::LociL1::SemanticVisitor,
    Kernel::xmof::EObject,
    xmof::Kernel::ObjectValue,
    SemanticVisitor,
    xmof::Kernel::Value,
    xmof::Kernel::BooleanValue,
    Kernel::xmof::EEnum,
    InvocationAction,
    xmof::BasicActions::CallAction,
    IntermediateActivities::ObjectNode,
    Pin,
    xmof::BasicActions::OutputPin,
    xmof::BasicActions::InputPin,
    ActivityEdge,
    xmof::IntermediateActivities::ObjectFlow,
    IntermediateActivities::ActivityEdge,
    Kernel::InstanceSpecification,
    Kernel::ValueSpecification,
    EDataType,
    xmof::Kernel::PrimitiveType,
    LiteralSpecification,
    xmof::Kernel::LiteralUnlimitedNatural,
    xmof::Kernel::LiteralNull,
    xmof::Kernel::LiteralInteger,
    xmof::Kernel::LiteralString,
    xmof::Kernel::LiteralBoolean,
    Kernel::Slot,
    Kernel::xmof::EClassifier,
    Kernel::xmof::EStructuralFeature,
    EModelElement,
    xmof::Kernel::Slot,
    EOperation,
    xmof::Kernel::BehavioredEOperation,
    BehavioredEOperation,
    xmof::Communications::Reception,
    Event,
    xmof::Communications::MessageEvent,
    Communications::Signal,
    MessageEvent,
    xmof::Communications::SignalEvent,
    ETypedElement,
    xmof::BasicActions::Pin,
    xmof::Kernel::ValueSpecification,
    Kernel::EEnumLiteralSpecification,
    ValueSpecification,
    xmof::Kernel::InstanceValue,
    xmof::Kernel::LiteralSpecification,
    xmof::Kernel::EnumValue,
    Kernel::xmof::EEnumLiteral,
    InstanceSpecification,
    xmof::Kernel::EEnumLiteralSpecification,
    EParameter,
    xmof::Kernel::DirectedParameter,
    EClass,
    OpaqueBehavior,
    xmof::BasicBehaviors::FunctionBehavior,
    BasicBehaviors::Behavior,
    EClassifier,
    xmof::BasicBehaviors::BehavioredClassifier,
    Communications::xmof::EAttribute,
    xmof::Communications::Signal,
    Communications::Event,
    ENamedElement,
    xmof::Communications::Event,
    xmof::Kernel::InstanceSpecification,
    xmof::IntermediateActivities::ActivityNode,
    xmof::Communications::Trigger,
    BehavioredEClass,
    xmof::BasicBehaviors::Behavior,
    Behavior,
    xmof::IntermediateActivities::Activity,
    xmof::BasicBehaviors::OpaqueBehavior,
    BasicBehaviors::BehavioredClassifier,
    xmof::Kernel::BehavioredEClass,
    Kernel::DirectedParameter,
    Kernel::BehavioredEOperation,
    xmof::BasicActions::SendSignalAction,
    BasicActions::xmof::EClassifier,
    ExecutableNode,
    xmof::BasicActions::Action,
    Communications::Trigger,
    CompleteActions::xmof::EClassifier,
    WriteLinkAction,
    xmof::IntermediateActions::CreateLinkAction,
    CallAction,
    xmof::BasicActions::CallBehaviorAction,
    xmof::BasicActions::CallOperationAction,
    xmof::CompleteActions::StartObjectBehaviorAction,
    xmof::IntermediateActions::DestroyLinkAction,
    IntermediateActions::xmof::EClassifier,
    WriteStructuralFeatureAction,
    xmof::IntermediateActions::AddStructuralFeatureValueAction,
    xmof::IntermediateActions::RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    xmof::IntermediateActions::ClearStructuralFeatureAction,
    xmof::IntermediateActions::WriteStructuralFeatureAction,
    IntermediateActions::xmof::EReference,
    LinkEndData,
    xmof::IntermediateActions::LinkEndDestructionData,
    xmof::IntermediateActions::LinkEndCreationData,
    xmof::IntermediateActions::ReadStructuralFeatureAction,
    IntermediateActions::xmof::EStructuralFeature,
    xmof::IntermediateActions::LinkEndData,
    IntermediateActions::LinkEndData,
    LinkAction,
    xmof::IntermediateActions::ReadLinkAction,
    xmof::IntermediateActions::WriteLinkAction,
    Action,
    xmof::IntermediateActions::ReadSelfAction,
    xmof::IntermediateActions::CreateObjectAction,
    xmof::IntermediateActions::ValueSpecificationAction,
    xmof::CompleteActions::ReduceAction,
    xmof::IntermediateActions::LinkAction,
    xmof::IntermediateActions::DestroyObjectAction,
    xmof::BasicActions::InvocationAction,
    xmof::CompleteActions::ReadIsClassifiedObjectAction,
    xmof::IntermediateActions::ClearAssociationAction,
    xmof::CompleteActions::ReclassifyObjectAction,
    xmof::CompleteActions::ReadExtentAction,
    xmof::CompleteActions::StartClassifierBehaviorAction,
    xmof::IntermediateActions::TestIdentityAction,
    xmof::CompleteActions::AcceptEventAction,
    xmof::IntermediateActions::StructuralFeatureAction,
    xmof::CompleteStructuredActivities::StructuredActivityNode,
    ExtraStructuredActivities::ExpansionNode,
    ExtraStructuredActivities::ExpansionRegion,
    xmof::CompleteStructuredActivities::Clause,
    CompleteStructuredActivities::Clause,
    xmof::IntermediateActivities::ControlFlow,
    ActivityNode,
    xmof::CompleteStructuredActivities::ExecutableNode,
    xmof::IntermediateActivities::ControlNode,
    ControlNode,
    xmof::IntermediateActivities::ForkNode,
    xmof::IntermediateActivities::JoinNode,
    xmof::IntermediateActivities::InitialNode,
    xmof::IntermediateActivities::FinalNode,
    xmof::IntermediateActivities::DecisionNode,
    xmof::IntermediateActivities::MergeNode,
    BasicActions::InputPin,
    CompleteStructuredActivities::ExecutableNode,
    BasicActions::OutputPin,
    StructuredActivityNode,
    xmof::CompleteStructuredActivities::ConditionalNode,
    xmof::ExtraStructuredActivities::ExpansionRegion,
    xmof::CompleteStructuredActivities::LoopNode,
    ObjectNode,
    xmof::ExtraStructuredActivities::ExpansionNode,
    xmof::IntermediateActivities::ActivityParameterNode,
    FinalNode,
    xmof::IntermediateActivities::ActivityFinalNode,
    IntermediateActivities::ObjectFlow,
    CompleteStructuredActivities::StructuredActivityNode,
    IntermediateActivities::ActivityNode,
    xmof::IntermediateActivities::ObjectNode,
    IntermediateActivities::Activity,
    xmof::IntermediateActivities::ActivityEdge,
    ExpansionKind,
    CallConcurrencyKind,
    ParameterDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basicbehaviors::parametervalue_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors::ParameterValue)


def test_basicbehaviors::parametervalue_constructor_exists():
    assert callable(BasicBehaviors::ParameterValue.__init__)


def test_basicbehaviors::parametervalue_constructor_args():
    sig = inspect.signature(BasicBehaviors::ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicbehaviors::parametervaluedefinition_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicBehaviors::ParameterValueDefinition)


def test_xmof::basicbehaviors::parametervaluedefinition_constructor_exists():
    assert callable(xmof::BasicBehaviors::ParameterValueDefinition.__init__)


def test_xmof::basicbehaviors::parametervaluedefinition_constructor_args():
    sig = inspect.signature(xmof::BasicBehaviors::ParameterValueDefinition.__init__)
    params = list(sig.parameters.keys())



def test_kernel::value_is_not_abstract():
    assert not inspect.isabstract(Kernel::Value)


def test_kernel::value_constructor_exists():
    assert callable(Kernel::Value.__init__)


def test_kernel::value_constructor_args():
    sig = inspect.signature(Kernel::Value.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicbehaviors::parametervalue_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicBehaviors::ParameterValue)


def test_xmof::basicbehaviors::parametervalue_constructor_exists():
    assert callable(xmof::BasicBehaviors::ParameterValue.__init__)


def test_xmof::basicbehaviors::parametervalue_constructor_args():
    sig = inspect.signature(xmof::BasicBehaviors::ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_primitivevalue_is_not_abstract():
    assert not inspect.isabstract(PrimitiveValue)


def test_primitivevalue_constructor_exists():
    assert callable(PrimitiveValue.__init__)


def test_primitivevalue_constructor_args():
    sig = inspect.signature(PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::integervalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::IntegerValue)


def test_xmof::kernel::integervalue_constructor_exists():
    assert callable(xmof::Kernel::IntegerValue.__init__)


def test_xmof::kernel::integervalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof::kernel::integervalue_has_value():
    assert hasattr(xmof::Kernel::IntegerValue, "value")
    descriptor = None
    for klass in xmof::Kernel::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof::kernel::stringvalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::StringValue)


def test_xmof::kernel::stringvalue_constructor_exists():
    assert callable(xmof::Kernel::StringValue.__init__)


def test_xmof::kernel::stringvalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof::kernel::stringvalue_has_value():
    assert hasattr(xmof::Kernel::StringValue, "value")
    descriptor = None
    for klass in xmof::Kernel::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Kernel::PrimitiveType)


def test_kernel::primitivetype_constructor_exists():
    assert callable(Kernel::PrimitiveType.__init__)


def test_kernel::primitivetype_constructor_args():
    sig = inspect.signature(Kernel::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::enumerationvalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::EnumerationValue)


def test_xmof::kernel::enumerationvalue_constructor_exists():
    assert callable(xmof::Kernel::EnumerationValue.__init__)


def test_xmof::kernel::enumerationvalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::EnumerationValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::primitivevalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::PrimitiveValue)


def test_xmof::kernel::primitivevalue_constructor_exists():
    assert callable(xmof::Kernel::PrimitiveValue.__init__)


def test_xmof::kernel::primitivevalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof::locil1::semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(xmof::LociL1::SemanticVisitor)


def test_xmof::locil1::semanticvisitor_constructor_exists():
    assert callable(xmof::LociL1::SemanticVisitor.__init__)


def test_xmof::locil1::semanticvisitor_constructor_args():
    sig = inspect.signature(xmof::LociL1::SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_kernel::xmof::eobject_is_not_abstract():
    assert not inspect.isabstract(Kernel::xmof::EObject)


def test_kernel::xmof::eobject_constructor_exists():
    assert callable(Kernel::xmof::EObject.__init__)


def test_kernel::xmof::eobject_constructor_args():
    sig = inspect.signature(Kernel::xmof::EObject.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::objectvalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::ObjectValue)


def test_xmof::kernel::objectvalue_constructor_exists():
    assert callable(xmof::Kernel::ObjectValue.__init__)


def test_xmof::kernel::objectvalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::ObjectValue.__init__)
    params = list(sig.parameters.keys())



def test_semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(SemanticVisitor)


def test_semanticvisitor_constructor_exists():
    assert callable(SemanticVisitor.__init__)


def test_semanticvisitor_constructor_args():
    sig = inspect.signature(SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::value_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::Value)


def test_xmof::kernel::value_constructor_exists():
    assert callable(xmof::Kernel::Value.__init__)


def test_xmof::kernel::value_constructor_args():
    sig = inspect.signature(xmof::Kernel::Value.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::BooleanValue)


def test_xmof::kernel::booleanvalue_constructor_exists():
    assert callable(xmof::Kernel::BooleanValue.__init__)


def test_xmof::kernel::booleanvalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof::kernel::booleanvalue_has_value():
    assert hasattr(xmof::Kernel::BooleanValue, "value")
    descriptor = None
    for klass in xmof::Kernel::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel::xmof::eenum_is_not_abstract():
    assert not inspect.isabstract(Kernel::xmof::EEnum)


def test_kernel::xmof::eenum_constructor_exists():
    assert callable(Kernel::xmof::EEnum.__init__)


def test_kernel::xmof::eenum_constructor_args():
    sig = inspect.signature(Kernel::xmof::EEnum.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicactions::callaction_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::CallAction)


def test_xmof::basicactions::callaction_constructor_exists():
    assert callable(xmof::BasicActions::CallAction.__init__)


def test_xmof::basicactions::callaction_constructor_args():
    sig = inspect.signature(xmof::BasicActions::CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "synchronous" in params, "Missing parameter 'synchronous'"

def test_xmof::basicactions::callaction_has_synchronous():
    assert hasattr(xmof::BasicActions::CallAction, "synchronous")
    descriptor = None
    for klass in xmof::BasicActions::CallAction.__mro__:
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



def test_xmof::basicactions::outputpin_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::OutputPin)


def test_xmof::basicactions::outputpin_constructor_exists():
    assert callable(xmof::BasicActions::OutputPin.__init__)


def test_xmof::basicactions::outputpin_constructor_args():
    sig = inspect.signature(xmof::BasicActions::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicactions::inputpin_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::InputPin)


def test_xmof::basicactions::inputpin_constructor_exists():
    assert callable(xmof::BasicActions::InputPin.__init__)


def test_xmof::basicactions::inputpin_constructor_args():
    sig = inspect.signature(xmof::BasicActions::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::objectflow_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ObjectFlow)


def test_xmof::intermediateactivities::objectflow_constructor_exists():
    assert callable(xmof::IntermediateActivities::ObjectFlow.__init__)


def test_xmof::intermediateactivities::objectflow_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::activityedge_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::ActivityEdge)


def test_intermediateactivities::activityedge_constructor_exists():
    assert callable(IntermediateActivities::ActivityEdge.__init__)


def test_intermediateactivities::activityedge_constructor_args():
    sig = inspect.signature(IntermediateActivities::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_kernel::instancespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel::InstanceSpecification)


def test_kernel::instancespecification_constructor_exists():
    assert callable(Kernel::InstanceSpecification.__init__)


def test_kernel::instancespecification_constructor_args():
    sig = inspect.signature(Kernel::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel::valuespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel::ValueSpecification)


def test_kernel::valuespecification_constructor_exists():
    assert callable(Kernel::ValueSpecification.__init__)


def test_kernel::valuespecification_constructor_args():
    sig = inspect.signature(Kernel::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::primitivetype_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::PrimitiveType)


def test_xmof::kernel::primitivetype_constructor_exists():
    assert callable(xmof::Kernel::PrimitiveType.__init__)


def test_xmof::kernel::primitivetype_constructor_args():
    sig = inspect.signature(xmof::Kernel::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::LiteralUnlimitedNatural)


def test_xmof::kernel::literalunlimitednatural_constructor_exists():
    assert callable(xmof::Kernel::LiteralUnlimitedNatural.__init__)


def test_xmof::kernel::literalunlimitednatural_constructor_args():
    sig = inspect.signature(xmof::Kernel::LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof::kernel::literalunlimitednatural_has_value():
    assert hasattr(xmof::Kernel::LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in xmof::Kernel::LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof::kernel::literalnull_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::LiteralNull)


def test_xmof::kernel::literalnull_constructor_exists():
    assert callable(xmof::Kernel::LiteralNull.__init__)


def test_xmof::kernel::literalnull_constructor_args():
    sig = inspect.signature(xmof::Kernel::LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::literalinteger_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::LiteralInteger)


def test_xmof::kernel::literalinteger_constructor_exists():
    assert callable(xmof::Kernel::LiteralInteger.__init__)


def test_xmof::kernel::literalinteger_constructor_args():
    sig = inspect.signature(xmof::Kernel::LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof::kernel::literalinteger_has_value():
    assert hasattr(xmof::Kernel::LiteralInteger, "value")
    descriptor = None
    for klass in xmof::Kernel::LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof::kernel::literalstring_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::LiteralString)


def test_xmof::kernel::literalstring_constructor_exists():
    assert callable(xmof::Kernel::LiteralString.__init__)


def test_xmof::kernel::literalstring_constructor_args():
    sig = inspect.signature(xmof::Kernel::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof::kernel::literalstring_has_value():
    assert hasattr(xmof::Kernel::LiteralString, "value")
    descriptor = None
    for klass in xmof::Kernel::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof::kernel::literalboolean_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::LiteralBoolean)


def test_xmof::kernel::literalboolean_constructor_exists():
    assert callable(xmof::Kernel::LiteralBoolean.__init__)


def test_xmof::kernel::literalboolean_constructor_args():
    sig = inspect.signature(xmof::Kernel::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof::kernel::literalboolean_has_value():
    assert hasattr(xmof::Kernel::LiteralBoolean, "value")
    descriptor = None
    for klass in xmof::Kernel::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel::slot_is_not_abstract():
    assert not inspect.isabstract(Kernel::Slot)


def test_kernel::slot_constructor_exists():
    assert callable(Kernel::Slot.__init__)


def test_kernel::slot_constructor_args():
    sig = inspect.signature(Kernel::Slot.__init__)
    params = list(sig.parameters.keys())



def test_kernel::xmof::eclassifier_is_not_abstract():
    assert not inspect.isabstract(Kernel::xmof::EClassifier)


def test_kernel::xmof::eclassifier_constructor_exists():
    assert callable(Kernel::xmof::EClassifier.__init__)


def test_kernel::xmof::eclassifier_constructor_args():
    sig = inspect.signature(Kernel::xmof::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_kernel::xmof::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(Kernel::xmof::EStructuralFeature)


def test_kernel::xmof::estructuralfeature_constructor_exists():
    assert callable(Kernel::xmof::EStructuralFeature.__init__)


def test_kernel::xmof::estructuralfeature_constructor_args():
    sig = inspect.signature(Kernel::xmof::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::slot_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::Slot)


def test_xmof::kernel::slot_constructor_exists():
    assert callable(xmof::Kernel::Slot.__init__)


def test_xmof::kernel::slot_constructor_args():
    sig = inspect.signature(xmof::Kernel::Slot.__init__)
    params = list(sig.parameters.keys())



def test_eoperation_is_not_abstract():
    assert not inspect.isabstract(EOperation)


def test_eoperation_constructor_exists():
    assert callable(EOperation.__init__)


def test_eoperation_constructor_args():
    sig = inspect.signature(EOperation.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::BehavioredEOperation)


def test_xmof::kernel::behavioredeoperation_constructor_exists():
    assert callable(xmof::Kernel::BehavioredEOperation.__init__)


def test_xmof::kernel::behavioredeoperation_constructor_args():
    sig = inspect.signature(xmof::Kernel::BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(BehavioredEOperation)


def test_behavioredeoperation_constructor_exists():
    assert callable(BehavioredEOperation.__init__)


def test_behavioredeoperation_constructor_args():
    sig = inspect.signature(BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_xmof::communications::reception_is_not_abstract():
    assert not inspect.isabstract(xmof::Communications::Reception)


def test_xmof::communications::reception_constructor_exists():
    assert callable(xmof::Communications::Reception.__init__)


def test_xmof::communications::reception_constructor_args():
    sig = inspect.signature(xmof::Communications::Reception.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_xmof::communications::messageevent_is_not_abstract():
    assert not inspect.isabstract(xmof::Communications::MessageEvent)


def test_xmof::communications::messageevent_constructor_exists():
    assert callable(xmof::Communications::MessageEvent.__init__)


def test_xmof::communications::messageevent_constructor_args():
    sig = inspect.signature(xmof::Communications::MessageEvent.__init__)
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



def test_xmof::communications::signalevent_is_not_abstract():
    assert not inspect.isabstract(xmof::Communications::SignalEvent)


def test_xmof::communications::signalevent_constructor_exists():
    assert callable(xmof::Communications::SignalEvent.__init__)


def test_xmof::communications::signalevent_constructor_args():
    sig = inspect.signature(xmof::Communications::SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicactions::pin_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::Pin)


def test_xmof::basicactions::pin_constructor_exists():
    assert callable(xmof::BasicActions::Pin.__init__)


def test_xmof::basicactions::pin_constructor_args():
    sig = inspect.signature(xmof::BasicActions::Pin.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::valuespecification_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::ValueSpecification)


def test_xmof::kernel::valuespecification_constructor_exists():
    assert callable(xmof::Kernel::ValueSpecification.__init__)


def test_xmof::kernel::valuespecification_constructor_args():
    sig = inspect.signature(xmof::Kernel::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel::eenumliteralspecification_is_not_abstract():
    assert not inspect.isabstract(Kernel::EEnumLiteralSpecification)


def test_kernel::eenumliteralspecification_constructor_exists():
    assert callable(Kernel::EEnumLiteralSpecification.__init__)


def test_kernel::eenumliteralspecification_constructor_args():
    sig = inspect.signature(Kernel::EEnumLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::instancevalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::InstanceValue)


def test_xmof::kernel::instancevalue_constructor_exists():
    assert callable(xmof::Kernel::InstanceValue.__init__)


def test_xmof::kernel::instancevalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::literalspecification_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::LiteralSpecification)


def test_xmof::kernel::literalspecification_constructor_exists():
    assert callable(xmof::Kernel::LiteralSpecification.__init__)


def test_xmof::kernel::literalspecification_constructor_args():
    sig = inspect.signature(xmof::Kernel::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::enumvalue_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::EnumValue)


def test_xmof::kernel::enumvalue_constructor_exists():
    assert callable(xmof::Kernel::EnumValue.__init__)


def test_xmof::kernel::enumvalue_constructor_args():
    sig = inspect.signature(xmof::Kernel::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel::xmof::eenumliteral_is_not_abstract():
    assert not inspect.isabstract(Kernel::xmof::EEnumLiteral)


def test_kernel::xmof::eenumliteral_constructor_exists():
    assert callable(Kernel::xmof::EEnumLiteral.__init__)


def test_kernel::xmof::eenumliteral_constructor_args():
    sig = inspect.signature(Kernel::xmof::EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::eenumliteralspecification_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::EEnumLiteralSpecification)


def test_xmof::kernel::eenumliteralspecification_constructor_exists():
    assert callable(xmof::Kernel::EEnumLiteralSpecification.__init__)


def test_xmof::kernel::eenumliteralspecification_constructor_args():
    sig = inspect.signature(xmof::Kernel::EEnumLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_eparameter_is_not_abstract():
    assert not inspect.isabstract(EParameter)


def test_eparameter_constructor_exists():
    assert callable(EParameter.__init__)


def test_eparameter_constructor_args():
    sig = inspect.signature(EParameter.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::directedparameter_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::DirectedParameter)


def test_xmof::kernel::directedparameter_constructor_exists():
    assert callable(xmof::Kernel::DirectedParameter.__init__)


def test_xmof::kernel::directedparameter_constructor_args():
    sig = inspect.signature(xmof::Kernel::DirectedParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_xmof::kernel::directedparameter_has_direction():
    assert hasattr(xmof::Kernel::DirectedParameter, "direction")
    descriptor = None
    for klass in xmof::Kernel::DirectedParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicbehaviors::functionbehavior_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicBehaviors::FunctionBehavior)


def test_xmof::basicbehaviors::functionbehavior_constructor_exists():
    assert callable(xmof::BasicBehaviors::FunctionBehavior.__init__)


def test_xmof::basicbehaviors::functionbehavior_constructor_args():
    sig = inspect.signature(xmof::BasicBehaviors::FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors::behavior_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors::Behavior)


def test_basicbehaviors::behavior_constructor_exists():
    assert callable(BasicBehaviors::Behavior.__init__)


def test_basicbehaviors::behavior_constructor_args():
    sig = inspect.signature(BasicBehaviors::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicbehaviors::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicBehaviors::BehavioredClassifier)


def test_xmof::basicbehaviors::behavioredclassifier_constructor_exists():
    assert callable(xmof::BasicBehaviors::BehavioredClassifier.__init__)


def test_xmof::basicbehaviors::behavioredclassifier_constructor_args():
    sig = inspect.signature(xmof::BasicBehaviors::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_communications::xmof::eattribute_is_not_abstract():
    assert not inspect.isabstract(Communications::xmof::EAttribute)


def test_communications::xmof::eattribute_constructor_exists():
    assert callable(Communications::xmof::EAttribute.__init__)


def test_communications::xmof::eattribute_constructor_args():
    sig = inspect.signature(Communications::xmof::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_xmof::communications::signal_is_not_abstract():
    assert not inspect.isabstract(xmof::Communications::Signal)


def test_xmof::communications::signal_constructor_exists():
    assert callable(xmof::Communications::Signal.__init__)


def test_xmof::communications::signal_constructor_args():
    sig = inspect.signature(xmof::Communications::Signal.__init__)
    params = list(sig.parameters.keys())



def test_communications::event_is_not_abstract():
    assert not inspect.isabstract(Communications::Event)


def test_communications::event_constructor_exists():
    assert callable(Communications::Event.__init__)


def test_communications::event_constructor_args():
    sig = inspect.signature(Communications::Event.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_xmof::communications::event_is_not_abstract():
    assert not inspect.isabstract(xmof::Communications::Event)


def test_xmof::communications::event_constructor_exists():
    assert callable(xmof::Communications::Event.__init__)


def test_xmof::communications::event_constructor_args():
    sig = inspect.signature(xmof::Communications::Event.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::instancespecification_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::InstanceSpecification)


def test_xmof::kernel::instancespecification_constructor_exists():
    assert callable(xmof::Kernel::InstanceSpecification.__init__)


def test_xmof::kernel::instancespecification_constructor_args():
    sig = inspect.signature(xmof::Kernel::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::activitynode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ActivityNode)


def test_xmof::intermediateactivities::activitynode_constructor_exists():
    assert callable(xmof::IntermediateActivities::ActivityNode.__init__)


def test_xmof::intermediateactivities::activitynode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::communications::trigger_is_not_abstract():
    assert not inspect.isabstract(xmof::Communications::Trigger)


def test_xmof::communications::trigger_constructor_exists():
    assert callable(xmof::Communications::Trigger.__init__)


def test_xmof::communications::trigger_constructor_args():
    sig = inspect.signature(xmof::Communications::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_behavioredeclass_is_not_abstract():
    assert not inspect.isabstract(BehavioredEClass)


def test_behavioredeclass_constructor_exists():
    assert callable(BehavioredEClass.__init__)


def test_behavioredeclass_constructor_args():
    sig = inspect.signature(BehavioredEClass.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicbehaviors::behavior_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicBehaviors::Behavior)


def test_xmof::basicbehaviors::behavior_constructor_exists():
    assert callable(xmof::BasicBehaviors::Behavior.__init__)


def test_xmof::basicbehaviors::behavior_constructor_args():
    sig = inspect.signature(xmof::BasicBehaviors::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "reentrant" in params, "Missing parameter 'reentrant'"

def test_xmof::basicbehaviors::behavior_has_reentrant():
    assert hasattr(xmof::BasicBehaviors::Behavior, "reentrant")
    descriptor = None
    for klass in xmof::BasicBehaviors::Behavior.__mro__:
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



def test_xmof::intermediateactivities::activity_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::Activity)


def test_xmof::intermediateactivities::activity_constructor_exists():
    assert callable(xmof::IntermediateActivities::Activity.__init__)


def test_xmof::intermediateactivities::activity_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_xmof::intermediateactivities::activity_has_readOnly():
    assert hasattr(xmof::IntermediateActivities::Activity, "readOnly")
    descriptor = None
    for klass in xmof::IntermediateActivities::Activity.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_xmof::basicbehaviors::opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicBehaviors::OpaqueBehavior)


def test_xmof::basicbehaviors::opaquebehavior_constructor_exists():
    assert callable(xmof::BasicBehaviors::OpaqueBehavior.__init__)


def test_xmof::basicbehaviors::opaquebehavior_constructor_args():
    sig = inspect.signature(xmof::BasicBehaviors::OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_xmof::basicbehaviors::opaquebehavior_has_body():
    assert hasattr(xmof::BasicBehaviors::OpaqueBehavior, "body")
    descriptor = None
    for klass in xmof::BasicBehaviors::OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_xmof::basicbehaviors::opaquebehavior_has_language():
    assert hasattr(xmof::BasicBehaviors::OpaqueBehavior, "language")
    descriptor = None
    for klass in xmof::BasicBehaviors::OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_basicbehaviors::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors::BehavioredClassifier)


def test_basicbehaviors::behavioredclassifier_constructor_exists():
    assert callable(BasicBehaviors::BehavioredClassifier.__init__)


def test_basicbehaviors::behavioredclassifier_constructor_args():
    sig = inspect.signature(BasicBehaviors::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_xmof::kernel::behavioredeclass_is_not_abstract():
    assert not inspect.isabstract(xmof::Kernel::BehavioredEClass)


def test_xmof::kernel::behavioredeclass_constructor_exists():
    assert callable(xmof::Kernel::BehavioredEClass.__init__)


def test_xmof::kernel::behavioredeclass_constructor_args():
    sig = inspect.signature(xmof::Kernel::BehavioredEClass.__init__)
    params = list(sig.parameters.keys())



def test_kernel::directedparameter_is_not_abstract():
    assert not inspect.isabstract(Kernel::DirectedParameter)


def test_kernel::directedparameter_constructor_exists():
    assert callable(Kernel::DirectedParameter.__init__)


def test_kernel::directedparameter_constructor_args():
    sig = inspect.signature(Kernel::DirectedParameter.__init__)
    params = list(sig.parameters.keys())



def test_kernel::behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(Kernel::BehavioredEOperation)


def test_kernel::behavioredeoperation_constructor_exists():
    assert callable(Kernel::BehavioredEOperation.__init__)


def test_kernel::behavioredeoperation_constructor_args():
    sig = inspect.signature(Kernel::BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicactions::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::SendSignalAction)


def test_xmof::basicactions::sendsignalaction_constructor_exists():
    assert callable(xmof::BasicActions::SendSignalAction.__init__)


def test_xmof::basicactions::sendsignalaction_constructor_args():
    sig = inspect.signature(xmof::BasicActions::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::xmof::eclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicActions::xmof::EClassifier)


def test_basicactions::xmof::eclassifier_constructor_exists():
    assert callable(BasicActions::xmof::EClassifier.__init__)


def test_basicactions::xmof::eclassifier_constructor_args():
    sig = inspect.signature(BasicActions::xmof::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicactions::action_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::Action)


def test_xmof::basicactions::action_constructor_exists():
    assert callable(xmof::BasicActions::Action.__init__)


def test_xmof::basicactions::action_constructor_args():
    sig = inspect.signature(xmof::BasicActions::Action.__init__)
    params = list(sig.parameters.keys())
    assert "locallyReentrant" in params, "Missing parameter 'locallyReentrant'"

def test_xmof::basicactions::action_has_locallyReentrant():
    assert hasattr(xmof::BasicActions::Action, "locallyReentrant")
    descriptor = None
    for klass in xmof::BasicActions::Action.__mro__:
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



def test_completeactions::xmof::eclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteActions::xmof::EClassifier)


def test_completeactions::xmof::eclassifier_constructor_exists():
    assert callable(CompleteActions::xmof::EClassifier.__init__)


def test_completeactions::xmof::eclassifier_constructor_args():
    sig = inspect.signature(CompleteActions::xmof::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::createlinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::CreateLinkAction)


def test_xmof::intermediateactions::createlinkaction_constructor_exists():
    assert callable(xmof::IntermediateActions::CreateLinkAction.__init__)


def test_xmof::intermediateactions::createlinkaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicactions::callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::CallBehaviorAction)


def test_xmof::basicactions::callbehavioraction_constructor_exists():
    assert callable(xmof::BasicActions::CallBehaviorAction.__init__)


def test_xmof::basicactions::callbehavioraction_constructor_args():
    sig = inspect.signature(xmof::BasicActions::CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::basicactions::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::CallOperationAction)


def test_xmof::basicactions::calloperationaction_constructor_exists():
    assert callable(xmof::BasicActions::CallOperationAction.__init__)


def test_xmof::basicactions::calloperationaction_constructor_args():
    sig = inspect.signature(xmof::BasicActions::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completeactions::startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteActions::StartObjectBehaviorAction)


def test_xmof::completeactions::startobjectbehavioraction_constructor_exists():
    assert callable(xmof::CompleteActions::StartObjectBehaviorAction.__init__)


def test_xmof::completeactions::startobjectbehavioraction_constructor_args():
    sig = inspect.signature(xmof::CompleteActions::StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::DestroyLinkAction)


def test_xmof::intermediateactions::destroylinkaction_constructor_exists():
    assert callable(xmof::IntermediateActions::DestroyLinkAction.__init__)


def test_xmof::intermediateactions::destroylinkaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::xmof::eclassifier_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::xmof::EClassifier)


def test_intermediateactions::xmof::eclassifier_constructor_exists():
    assert callable(IntermediateActions::xmof::EClassifier.__init__)


def test_intermediateactions::xmof::eclassifier_constructor_args():
    sig = inspect.signature(IntermediateActions::xmof::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::AddStructuralFeatureValueAction)


def test_xmof::intermediateactions::addstructuralfeaturevalueaction_constructor_exists():
    assert callable(xmof::IntermediateActions::AddStructuralFeatureValueAction.__init__)


def test_xmof::intermediateactions::addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_xmof::intermediateactions::addstructuralfeaturevalueaction_has_replaceAll():
    assert hasattr(xmof::IntermediateActions::AddStructuralFeatureValueAction, "replaceAll")
    descriptor = None
    for klass in xmof::IntermediateActions::AddStructuralFeatureValueAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_xmof::intermediateactions::removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::RemoveStructuralFeatureValueAction)


def test_xmof::intermediateactions::removestructuralfeaturevalueaction_constructor_exists():
    assert callable(xmof::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)


def test_xmof::intermediateactions::removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "removeDuplicates" in params, "Missing parameter 'removeDuplicates'"

def test_xmof::intermediateactions::removestructuralfeaturevalueaction_has_removeDuplicates():
    assert hasattr(xmof::IntermediateActions::RemoveStructuralFeatureValueAction, "removeDuplicates")
    descriptor = None
    for klass in xmof::IntermediateActions::RemoveStructuralFeatureValueAction.__mro__:
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



def test_xmof::intermediateactions::clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::ClearStructuralFeatureAction)


def test_xmof::intermediateactions::clearstructuralfeatureaction_constructor_exists():
    assert callable(xmof::IntermediateActions::ClearStructuralFeatureAction.__init__)


def test_xmof::intermediateactions::clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::WriteStructuralFeatureAction)


def test_xmof::intermediateactions::writestructuralfeatureaction_constructor_exists():
    assert callable(xmof::IntermediateActions::WriteStructuralFeatureAction.__init__)


def test_xmof::intermediateactions::writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::xmof::ereference_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::xmof::EReference)


def test_intermediateactions::xmof::ereference_constructor_exists():
    assert callable(IntermediateActions::xmof::EReference.__init__)


def test_intermediateactions::xmof::ereference_constructor_args():
    sig = inspect.signature(IntermediateActions::xmof::EReference.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::LinkEndDestructionData)


def test_xmof::intermediateactions::linkenddestructiondata_constructor_exists():
    assert callable(xmof::IntermediateActions::LinkEndDestructionData.__init__)


def test_xmof::intermediateactions::linkenddestructiondata_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "destroyDuplicates" in params, "Missing parameter 'destroyDuplicates'"

def test_xmof::intermediateactions::linkenddestructiondata_has_destroyDuplicates():
    assert hasattr(xmof::IntermediateActions::LinkEndDestructionData, "destroyDuplicates")
    descriptor = None
    for klass in xmof::IntermediateActions::LinkEndDestructionData.__mro__:
        if "destroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["destroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_xmof::intermediateactions::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::LinkEndCreationData)


def test_xmof::intermediateactions::linkendcreationdata_constructor_exists():
    assert callable(xmof::IntermediateActions::LinkEndCreationData.__init__)


def test_xmof::intermediateactions::linkendcreationdata_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_xmof::intermediateactions::linkendcreationdata_has_replaceAll():
    assert hasattr(xmof::IntermediateActions::LinkEndCreationData, "replaceAll")
    descriptor = None
    for klass in xmof::IntermediateActions::LinkEndCreationData.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_xmof::intermediateactions::readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::ReadStructuralFeatureAction)


def test_xmof::intermediateactions::readstructuralfeatureaction_constructor_exists():
    assert callable(xmof::IntermediateActions::ReadStructuralFeatureAction.__init__)


def test_xmof::intermediateactions::readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::xmof::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::xmof::EStructuralFeature)


def test_intermediateactions::xmof::estructuralfeature_constructor_exists():
    assert callable(IntermediateActions::xmof::EStructuralFeature.__init__)


def test_intermediateactions::xmof::estructuralfeature_constructor_args():
    sig = inspect.signature(IntermediateActions::xmof::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::linkenddata_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::LinkEndData)


def test_xmof::intermediateactions::linkenddata_constructor_exists():
    assert callable(xmof::IntermediateActions::LinkEndData.__init__)


def test_xmof::intermediateactions::linkenddata_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::LinkEndData.__init__)
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



def test_xmof::intermediateactions::readlinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::ReadLinkAction)


def test_xmof::intermediateactions::readlinkaction_constructor_exists():
    assert callable(xmof::IntermediateActions::ReadLinkAction.__init__)


def test_xmof::intermediateactions::readlinkaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::writelinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::WriteLinkAction)


def test_xmof::intermediateactions::writelinkaction_constructor_exists():
    assert callable(xmof::IntermediateActions::WriteLinkAction.__init__)


def test_xmof::intermediateactions::writelinkaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::readselfaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::ReadSelfAction)


def test_xmof::intermediateactions::readselfaction_constructor_exists():
    assert callable(xmof::IntermediateActions::ReadSelfAction.__init__)


def test_xmof::intermediateactions::readselfaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::createobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::CreateObjectAction)


def test_xmof::intermediateactions::createobjectaction_constructor_exists():
    assert callable(xmof::IntermediateActions::CreateObjectAction.__init__)


def test_xmof::intermediateactions::createobjectaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::ValueSpecificationAction)


def test_xmof::intermediateactions::valuespecificationaction_constructor_exists():
    assert callable(xmof::IntermediateActions::ValueSpecificationAction.__init__)


def test_xmof::intermediateactions::valuespecificationaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completeactions::reduceaction_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteActions::ReduceAction)


def test_xmof::completeactions::reduceaction_constructor_exists():
    assert callable(xmof::CompleteActions::ReduceAction.__init__)


def test_xmof::completeactions::reduceaction_constructor_args():
    sig = inspect.signature(xmof::CompleteActions::ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_xmof::completeactions::reduceaction_has_ordered():
    assert hasattr(xmof::CompleteActions::ReduceAction, "ordered")
    descriptor = None
    for klass in xmof::CompleteActions::ReduceAction.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_xmof::intermediateactions::linkaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::LinkAction)


def test_xmof::intermediateactions::linkaction_constructor_exists():
    assert callable(xmof::IntermediateActions::LinkAction.__init__)


def test_xmof::intermediateactions::linkaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::DestroyObjectAction)


def test_xmof::intermediateactions::destroyobjectaction_constructor_exists():
    assert callable(xmof::IntermediateActions::DestroyObjectAction.__init__)


def test_xmof::intermediateactions::destroyobjectaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "destroyLinks" in params, "Missing parameter 'destroyLinks'"
    assert "destroyOwnedObjects" in params, "Missing parameter 'destroyOwnedObjects'"

def test_xmof::intermediateactions::destroyobjectaction_has_destroyLinks():
    assert hasattr(xmof::IntermediateActions::DestroyObjectAction, "destroyLinks")
    descriptor = None
    for klass in xmof::IntermediateActions::DestroyObjectAction.__mro__:
        if "destroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["destroyLinks"]
            break
    assert isinstance(descriptor, property)

def test_xmof::intermediateactions::destroyobjectaction_has_destroyOwnedObjects():
    assert hasattr(xmof::IntermediateActions::DestroyObjectAction, "destroyOwnedObjects")
    descriptor = None
    for klass in xmof::IntermediateActions::DestroyObjectAction.__mro__:
        if "destroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["destroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)



def test_xmof::basicactions::invocationaction_is_not_abstract():
    assert not inspect.isabstract(xmof::BasicActions::InvocationAction)


def test_xmof::basicactions::invocationaction_constructor_exists():
    assert callable(xmof::BasicActions::InvocationAction.__init__)


def test_xmof::basicactions::invocationaction_constructor_args():
    sig = inspect.signature(xmof::BasicActions::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completeactions::readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteActions::ReadIsClassifiedObjectAction)


def test_xmof::completeactions::readisclassifiedobjectaction_constructor_exists():
    assert callable(xmof::CompleteActions::ReadIsClassifiedObjectAction.__init__)


def test_xmof::completeactions::readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(xmof::CompleteActions::ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "direct" in params, "Missing parameter 'direct'"

def test_xmof::completeactions::readisclassifiedobjectaction_has_direct():
    assert hasattr(xmof::CompleteActions::ReadIsClassifiedObjectAction, "direct")
    descriptor = None
    for klass in xmof::CompleteActions::ReadIsClassifiedObjectAction.__mro__:
        if "direct" in klass.__dict__:
            descriptor = klass.__dict__["direct"]
            break
    assert isinstance(descriptor, property)



def test_xmof::intermediateactions::clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::ClearAssociationAction)


def test_xmof::intermediateactions::clearassociationaction_constructor_exists():
    assert callable(xmof::IntermediateActions::ClearAssociationAction.__init__)


def test_xmof::intermediateactions::clearassociationaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completeactions::reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteActions::ReclassifyObjectAction)


def test_xmof::completeactions::reclassifyobjectaction_constructor_exists():
    assert callable(xmof::CompleteActions::ReclassifyObjectAction.__init__)


def test_xmof::completeactions::reclassifyobjectaction_constructor_args():
    sig = inspect.signature(xmof::CompleteActions::ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_xmof::completeactions::reclassifyobjectaction_has_replaceAll():
    assert hasattr(xmof::CompleteActions::ReclassifyObjectAction, "replaceAll")
    descriptor = None
    for klass in xmof::CompleteActions::ReclassifyObjectAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_xmof::completeactions::readextentaction_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteActions::ReadExtentAction)


def test_xmof::completeactions::readextentaction_constructor_exists():
    assert callable(xmof::CompleteActions::ReadExtentAction.__init__)


def test_xmof::completeactions::readextentaction_constructor_args():
    sig = inspect.signature(xmof::CompleteActions::ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completeactions::startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteActions::StartClassifierBehaviorAction)


def test_xmof::completeactions::startclassifierbehavioraction_constructor_exists():
    assert callable(xmof::CompleteActions::StartClassifierBehaviorAction.__init__)


def test_xmof::completeactions::startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(xmof::CompleteActions::StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactions::testidentityaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::TestIdentityAction)


def test_xmof::intermediateactions::testidentityaction_constructor_exists():
    assert callable(xmof::IntermediateActions::TestIdentityAction.__init__)


def test_xmof::intermediateactions::testidentityaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completeactions::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteActions::AcceptEventAction)


def test_xmof::completeactions::accepteventaction_constructor_exists():
    assert callable(xmof::CompleteActions::AcceptEventAction.__init__)


def test_xmof::completeactions::accepteventaction_constructor_args():
    sig = inspect.signature(xmof::CompleteActions::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshall" in params, "Missing parameter 'unmarshall'"

def test_xmof::completeactions::accepteventaction_has_unmarshall():
    assert hasattr(xmof::CompleteActions::AcceptEventAction, "unmarshall")
    descriptor = None
    for klass in xmof::CompleteActions::AcceptEventAction.__mro__:
        if "unmarshall" in klass.__dict__:
            descriptor = klass.__dict__["unmarshall"]
            break
    assert isinstance(descriptor, property)



def test_xmof::intermediateactions::structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActions::StructuralFeatureAction)


def test_xmof::intermediateactions::structuralfeatureaction_constructor_exists():
    assert callable(xmof::IntermediateActions::StructuralFeatureAction.__init__)


def test_xmof::intermediateactions::structuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof::IntermediateActions::StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completestructuredactivities::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteStructuredActivities::StructuredActivityNode)


def test_xmof::completestructuredactivities::structuredactivitynode_constructor_exists():
    assert callable(xmof::CompleteStructuredActivities::StructuredActivityNode.__init__)


def test_xmof::completestructuredactivities::structuredactivitynode_constructor_args():
    sig = inspect.signature(xmof::CompleteStructuredActivities::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_xmof::completestructuredactivities::structuredactivitynode_has_mustIsolate():
    assert hasattr(xmof::CompleteStructuredActivities::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in xmof::CompleteStructuredActivities::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



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



def test_xmof::completestructuredactivities::clause_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteStructuredActivities::Clause)


def test_xmof::completestructuredactivities::clause_constructor_exists():
    assert callable(xmof::CompleteStructuredActivities::Clause.__init__)


def test_xmof::completestructuredactivities::clause_constructor_args():
    sig = inspect.signature(xmof::CompleteStructuredActivities::Clause.__init__)
    params = list(sig.parameters.keys())



def test_completestructuredactivities::clause_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities::Clause)


def test_completestructuredactivities::clause_constructor_exists():
    assert callable(CompleteStructuredActivities::Clause.__init__)


def test_completestructuredactivities::clause_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities::Clause.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::controlflow_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ControlFlow)


def test_xmof::intermediateactivities::controlflow_constructor_exists():
    assert callable(xmof::IntermediateActivities::ControlFlow.__init__)


def test_xmof::intermediateactivities::controlflow_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::completestructuredactivities::executablenode_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteStructuredActivities::ExecutableNode)


def test_xmof::completestructuredactivities::executablenode_constructor_exists():
    assert callable(xmof::CompleteStructuredActivities::ExecutableNode.__init__)


def test_xmof::completestructuredactivities::executablenode_constructor_args():
    sig = inspect.signature(xmof::CompleteStructuredActivities::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::controlnode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ControlNode)


def test_xmof::intermediateactivities::controlnode_constructor_exists():
    assert callable(xmof::IntermediateActivities::ControlNode.__init__)


def test_xmof::intermediateactivities::controlnode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::forknode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ForkNode)


def test_xmof::intermediateactivities::forknode_constructor_exists():
    assert callable(xmof::IntermediateActivities::ForkNode.__init__)


def test_xmof::intermediateactivities::forknode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::joinnode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::JoinNode)


def test_xmof::intermediateactivities::joinnode_constructor_exists():
    assert callable(xmof::IntermediateActivities::JoinNode.__init__)


def test_xmof::intermediateactivities::joinnode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::initialnode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::InitialNode)


def test_xmof::intermediateactivities::initialnode_constructor_exists():
    assert callable(xmof::IntermediateActivities::InitialNode.__init__)


def test_xmof::intermediateactivities::initialnode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::finalnode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::FinalNode)


def test_xmof::intermediateactivities::finalnode_constructor_exists():
    assert callable(xmof::IntermediateActivities::FinalNode.__init__)


def test_xmof::intermediateactivities::finalnode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::decisionnode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::DecisionNode)


def test_xmof::intermediateactivities::decisionnode_constructor_exists():
    assert callable(xmof::IntermediateActivities::DecisionNode.__init__)


def test_xmof::intermediateactivities::decisionnode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::mergenode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::MergeNode)


def test_xmof::intermediateactivities::mergenode_constructor_exists():
    assert callable(xmof::IntermediateActivities::MergeNode.__init__)


def test_xmof::intermediateactivities::mergenode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::MergeNode.__init__)
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



def test_xmof::completestructuredactivities::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteStructuredActivities::ConditionalNode)


def test_xmof::completestructuredactivities::conditionalnode_constructor_exists():
    assert callable(xmof::CompleteStructuredActivities::ConditionalNode.__init__)


def test_xmof::completestructuredactivities::conditionalnode_constructor_args():
    sig = inspect.signature(xmof::CompleteStructuredActivities::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "determinate" in params, "Missing parameter 'determinate'"
    assert "assured" in params, "Missing parameter 'assured'"

def test_xmof::completestructuredactivities::conditionalnode_has_determinate():
    assert hasattr(xmof::CompleteStructuredActivities::ConditionalNode, "determinate")
    descriptor = None
    for klass in xmof::CompleteStructuredActivities::ConditionalNode.__mro__:
        if "determinate" in klass.__dict__:
            descriptor = klass.__dict__["determinate"]
            break
    assert isinstance(descriptor, property)

def test_xmof::completestructuredactivities::conditionalnode_has_assured():
    assert hasattr(xmof::CompleteStructuredActivities::ConditionalNode, "assured")
    descriptor = None
    for klass in xmof::CompleteStructuredActivities::ConditionalNode.__mro__:
        if "assured" in klass.__dict__:
            descriptor = klass.__dict__["assured"]
            break
    assert isinstance(descriptor, property)



def test_xmof::extrastructuredactivities::expansionregion_is_not_abstract():
    assert not inspect.isabstract(xmof::ExtraStructuredActivities::ExpansionRegion)


def test_xmof::extrastructuredactivities::expansionregion_constructor_exists():
    assert callable(xmof::ExtraStructuredActivities::ExpansionRegion.__init__)


def test_xmof::extrastructuredactivities::expansionregion_constructor_args():
    sig = inspect.signature(xmof::ExtraStructuredActivities::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_xmof::extrastructuredactivities::expansionregion_has_mode():
    assert hasattr(xmof::ExtraStructuredActivities::ExpansionRegion, "mode")
    descriptor = None
    for klass in xmof::ExtraStructuredActivities::ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_xmof::completestructuredactivities::loopnode_is_not_abstract():
    assert not inspect.isabstract(xmof::CompleteStructuredActivities::LoopNode)


def test_xmof::completestructuredactivities::loopnode_constructor_exists():
    assert callable(xmof::CompleteStructuredActivities::LoopNode.__init__)


def test_xmof::completestructuredactivities::loopnode_constructor_args():
    sig = inspect.signature(xmof::CompleteStructuredActivities::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "testedFirst" in params, "Missing parameter 'testedFirst'"

def test_xmof::completestructuredactivities::loopnode_has_testedFirst():
    assert hasattr(xmof::CompleteStructuredActivities::LoopNode, "testedFirst")
    descriptor = None
    for klass in xmof::CompleteStructuredActivities::LoopNode.__mro__:
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



def test_xmof::extrastructuredactivities::expansionnode_is_not_abstract():
    assert not inspect.isabstract(xmof::ExtraStructuredActivities::ExpansionNode)


def test_xmof::extrastructuredactivities::expansionnode_constructor_exists():
    assert callable(xmof::ExtraStructuredActivities::ExpansionNode.__init__)


def test_xmof::extrastructuredactivities::expansionnode_constructor_args():
    sig = inspect.signature(xmof::ExtraStructuredActivities::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ActivityParameterNode)


def test_xmof::intermediateactivities::activityparameternode_constructor_exists():
    assert callable(xmof::IntermediateActivities::ActivityParameterNode.__init__)


def test_xmof::intermediateactivities::activityparameternode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ActivityFinalNode)


def test_xmof::intermediateactivities::activityfinalnode_constructor_exists():
    assert callable(xmof::IntermediateActivities::ActivityFinalNode.__init__)


def test_xmof::intermediateactivities::activityfinalnode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ActivityFinalNode.__init__)
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



def test_xmof::intermediateactivities::objectnode_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ObjectNode)


def test_xmof::intermediateactivities::objectnode_constructor_exists():
    assert callable(xmof::IntermediateActivities::ObjectNode.__init__)


def test_xmof::intermediateactivities::objectnode_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::activity_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::Activity)


def test_intermediateactivities::activity_constructor_exists():
    assert callable(IntermediateActivities::Activity.__init__)


def test_intermediateactivities::activity_constructor_args():
    sig = inspect.signature(IntermediateActivities::Activity.__init__)
    params = list(sig.parameters.keys())



def test_xmof::intermediateactivities::activityedge_is_not_abstract():
    assert not inspect.isabstract(xmof::IntermediateActivities::ActivityEdge)


def test_xmof::intermediateactivities::activityedge_constructor_exists():
    assert callable(xmof::IntermediateActivities::ActivityEdge.__init__)


def test_xmof::intermediateactivities::activityedge_constructor_args():
    sig = inspect.signature(xmof::IntermediateActivities::ActivityEdge.__init__)
    params = list(sig.parameters.keys())

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

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "return_",
        "out",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"


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
BasicBehaviors::ParameterValue_strategy = st.builds(
    BasicBehaviors::ParameterValue,
)
xmof::BasicBehaviors::ParameterValueDefinition_strategy = st.builds(
    xmof::BasicBehaviors::ParameterValueDefinition,
)
Kernel::Value_strategy = st.builds(
    Kernel::Value,
)
xmof::BasicBehaviors::ParameterValue_strategy = st.builds(
    xmof::BasicBehaviors::ParameterValue,
)
PrimitiveValue_strategy = st.builds(
    PrimitiveValue,
)
xmof::Kernel::IntegerValue_strategy = st.builds(
    xmof::Kernel::IntegerValue,
    value=
        st.integers()
)
xmof::Kernel::StringValue_strategy = st.builds(
    xmof::Kernel::StringValue,
    value=
        safe_text
)
Kernel::PrimitiveType_strategy = st.builds(
    Kernel::PrimitiveType,
)
Value_strategy = st.builds(
    Value,
)
xmof::Kernel::EnumerationValue_strategy = st.builds(
    xmof::Kernel::EnumerationValue,
)
xmof::Kernel::PrimitiveValue_strategy = st.builds(
    xmof::Kernel::PrimitiveValue,
)
xmof::LociL1::SemanticVisitor_strategy = st.builds(
    xmof::LociL1::SemanticVisitor,
)
Kernel::xmof::EObject_strategy = st.builds(
    Kernel::xmof::EObject,
)
xmof::Kernel::ObjectValue_strategy = st.builds(
    xmof::Kernel::ObjectValue,
)
SemanticVisitor_strategy = st.builds(
    SemanticVisitor,
)
xmof::Kernel::Value_strategy = st.builds(
    xmof::Kernel::Value,
)
xmof::Kernel::BooleanValue_strategy = st.builds(
    xmof::Kernel::BooleanValue,
    value=
        st.booleans()
)
Kernel::xmof::EEnum_strategy = st.builds(
    Kernel::xmof::EEnum,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
xmof::BasicActions::CallAction_strategy = st.builds(
    xmof::BasicActions::CallAction,
    synchronous=
        st.booleans()
)
IntermediateActivities::ObjectNode_strategy = st.builds(
    IntermediateActivities::ObjectNode,
)
Pin_strategy = st.builds(
    Pin,
)
xmof::BasicActions::OutputPin_strategy = st.builds(
    xmof::BasicActions::OutputPin,
)
xmof::BasicActions::InputPin_strategy = st.builds(
    xmof::BasicActions::InputPin,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
xmof::IntermediateActivities::ObjectFlow_strategy = st.builds(
    xmof::IntermediateActivities::ObjectFlow,
)
IntermediateActivities::ActivityEdge_strategy = st.builds(
    IntermediateActivities::ActivityEdge,
)
Kernel::InstanceSpecification_strategy = st.builds(
    Kernel::InstanceSpecification,
)
Kernel::ValueSpecification_strategy = st.builds(
    Kernel::ValueSpecification,
)
EDataType_strategy = st.builds(
    EDataType,
)
xmof::Kernel::PrimitiveType_strategy = st.builds(
    xmof::Kernel::PrimitiveType,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
xmof::Kernel::LiteralUnlimitedNatural_strategy = st.builds(
    xmof::Kernel::LiteralUnlimitedNatural,
    value=
        st.integers()
)
xmof::Kernel::LiteralNull_strategy = st.builds(
    xmof::Kernel::LiteralNull,
)
xmof::Kernel::LiteralInteger_strategy = st.builds(
    xmof::Kernel::LiteralInteger,
    value=
        st.integers()
)
xmof::Kernel::LiteralString_strategy = st.builds(
    xmof::Kernel::LiteralString,
    value=
        safe_text
)
xmof::Kernel::LiteralBoolean_strategy = st.builds(
    xmof::Kernel::LiteralBoolean,
    value=
        st.booleans()
)
Kernel::Slot_strategy = st.builds(
    Kernel::Slot,
)
Kernel::xmof::EClassifier_strategy = st.builds(
    Kernel::xmof::EClassifier,
)
Kernel::xmof::EStructuralFeature_strategy = st.builds(
    Kernel::xmof::EStructuralFeature,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
xmof::Kernel::Slot_strategy = st.builds(
    xmof::Kernel::Slot,
)
EOperation_strategy = st.builds(
    EOperation,
)
xmof::Kernel::BehavioredEOperation_strategy = st.builds(
    xmof::Kernel::BehavioredEOperation,
)
BehavioredEOperation_strategy = st.builds(
    BehavioredEOperation,
)
xmof::Communications::Reception_strategy = st.builds(
    xmof::Communications::Reception,
)
Event_strategy = st.builds(
    Event,
)
xmof::Communications::MessageEvent_strategy = st.builds(
    xmof::Communications::MessageEvent,
)
Communications::Signal_strategy = st.builds(
    Communications::Signal,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
xmof::Communications::SignalEvent_strategy = st.builds(
    xmof::Communications::SignalEvent,
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
xmof::BasicActions::Pin_strategy = st.builds(
    xmof::BasicActions::Pin,
)
xmof::Kernel::ValueSpecification_strategy = st.builds(
    xmof::Kernel::ValueSpecification,
)
Kernel::EEnumLiteralSpecification_strategy = st.builds(
    Kernel::EEnumLiteralSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
xmof::Kernel::InstanceValue_strategy = st.builds(
    xmof::Kernel::InstanceValue,
)
xmof::Kernel::LiteralSpecification_strategy = st.builds(
    xmof::Kernel::LiteralSpecification,
)
xmof::Kernel::EnumValue_strategy = st.builds(
    xmof::Kernel::EnumValue,
)
Kernel::xmof::EEnumLiteral_strategy = st.builds(
    Kernel::xmof::EEnumLiteral,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
xmof::Kernel::EEnumLiteralSpecification_strategy = st.builds(
    xmof::Kernel::EEnumLiteralSpecification,
)
EParameter_strategy = st.builds(
    EParameter,
)
xmof::Kernel::DirectedParameter_strategy = st.builds(
    xmof::Kernel::DirectedParameter,
    direction=
        safe_text
)
EClass_strategy = st.builds(
    EClass,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
xmof::BasicBehaviors::FunctionBehavior_strategy = st.builds(
    xmof::BasicBehaviors::FunctionBehavior,
)
BasicBehaviors::Behavior_strategy = st.builds(
    BasicBehaviors::Behavior,
)
EClassifier_strategy = st.builds(
    EClassifier,
)
xmof::BasicBehaviors::BehavioredClassifier_strategy = st.builds(
    xmof::BasicBehaviors::BehavioredClassifier,
)
Communications::xmof::EAttribute_strategy = st.builds(
    Communications::xmof::EAttribute,
)
xmof::Communications::Signal_strategy = st.builds(
    xmof::Communications::Signal,
)
Communications::Event_strategy = st.builds(
    Communications::Event,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
xmof::Communications::Event_strategy = st.builds(
    xmof::Communications::Event,
)
xmof::Kernel::InstanceSpecification_strategy = st.builds(
    xmof::Kernel::InstanceSpecification,
)
xmof::IntermediateActivities::ActivityNode_strategy = st.builds(
    xmof::IntermediateActivities::ActivityNode,
)
xmof::Communications::Trigger_strategy = st.builds(
    xmof::Communications::Trigger,
)
BehavioredEClass_strategy = st.builds(
    BehavioredEClass,
)
xmof::BasicBehaviors::Behavior_strategy = st.builds(
    xmof::BasicBehaviors::Behavior,
    reentrant=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
xmof::IntermediateActivities::Activity_strategy = st.builds(
    xmof::IntermediateActivities::Activity,
    readOnly=
        st.booleans()
)
xmof::BasicBehaviors::OpaqueBehavior_strategy = st.builds(
    xmof::BasicBehaviors::OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)
BasicBehaviors::BehavioredClassifier_strategy = st.builds(
    BasicBehaviors::BehavioredClassifier,
)
xmof::Kernel::BehavioredEClass_strategy = st.builds(
    xmof::Kernel::BehavioredEClass,
)
Kernel::DirectedParameter_strategy = st.builds(
    Kernel::DirectedParameter,
)
Kernel::BehavioredEOperation_strategy = st.builds(
    Kernel::BehavioredEOperation,
)
xmof::BasicActions::SendSignalAction_strategy = st.builds(
    xmof::BasicActions::SendSignalAction,
)
BasicActions::xmof::EClassifier_strategy = st.builds(
    BasicActions::xmof::EClassifier,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
xmof::BasicActions::Action_strategy = st.builds(
    xmof::BasicActions::Action,
    locallyReentrant=
        st.booleans()
)
Communications::Trigger_strategy = st.builds(
    Communications::Trigger,
)
CompleteActions::xmof::EClassifier_strategy = st.builds(
    CompleteActions::xmof::EClassifier,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
xmof::IntermediateActions::CreateLinkAction_strategy = st.builds(
    xmof::IntermediateActions::CreateLinkAction,
)
CallAction_strategy = st.builds(
    CallAction,
)
xmof::BasicActions::CallBehaviorAction_strategy = st.builds(
    xmof::BasicActions::CallBehaviorAction,
)
xmof::BasicActions::CallOperationAction_strategy = st.builds(
    xmof::BasicActions::CallOperationAction,
)
xmof::CompleteActions::StartObjectBehaviorAction_strategy = st.builds(
    xmof::CompleteActions::StartObjectBehaviorAction,
)
xmof::IntermediateActions::DestroyLinkAction_strategy = st.builds(
    xmof::IntermediateActions::DestroyLinkAction,
)
IntermediateActions::xmof::EClassifier_strategy = st.builds(
    IntermediateActions::xmof::EClassifier,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
xmof::IntermediateActions::AddStructuralFeatureValueAction_strategy = st.builds(
    xmof::IntermediateActions::AddStructuralFeatureValueAction,
    replaceAll=
        st.booleans()
)
xmof::IntermediateActions::RemoveStructuralFeatureValueAction_strategy = st.builds(
    xmof::IntermediateActions::RemoveStructuralFeatureValueAction,
    removeDuplicates=
        st.booleans()
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
xmof::IntermediateActions::ClearStructuralFeatureAction_strategy = st.builds(
    xmof::IntermediateActions::ClearStructuralFeatureAction,
)
xmof::IntermediateActions::WriteStructuralFeatureAction_strategy = st.builds(
    xmof::IntermediateActions::WriteStructuralFeatureAction,
)
IntermediateActions::xmof::EReference_strategy = st.builds(
    IntermediateActions::xmof::EReference,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
xmof::IntermediateActions::LinkEndDestructionData_strategy = st.builds(
    xmof::IntermediateActions::LinkEndDestructionData,
    destroyDuplicates=
        st.booleans()
)
xmof::IntermediateActions::LinkEndCreationData_strategy = st.builds(
    xmof::IntermediateActions::LinkEndCreationData,
    replaceAll=
        st.booleans()
)
xmof::IntermediateActions::ReadStructuralFeatureAction_strategy = st.builds(
    xmof::IntermediateActions::ReadStructuralFeatureAction,
)
IntermediateActions::xmof::EStructuralFeature_strategy = st.builds(
    IntermediateActions::xmof::EStructuralFeature,
)
xmof::IntermediateActions::LinkEndData_strategy = st.builds(
    xmof::IntermediateActions::LinkEndData,
)
IntermediateActions::LinkEndData_strategy = st.builds(
    IntermediateActions::LinkEndData,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
xmof::IntermediateActions::ReadLinkAction_strategy = st.builds(
    xmof::IntermediateActions::ReadLinkAction,
)
xmof::IntermediateActions::WriteLinkAction_strategy = st.builds(
    xmof::IntermediateActions::WriteLinkAction,
)
Action_strategy = st.builds(
    Action,
)
xmof::IntermediateActions::ReadSelfAction_strategy = st.builds(
    xmof::IntermediateActions::ReadSelfAction,
)
xmof::IntermediateActions::CreateObjectAction_strategy = st.builds(
    xmof::IntermediateActions::CreateObjectAction,
)
xmof::IntermediateActions::ValueSpecificationAction_strategy = st.builds(
    xmof::IntermediateActions::ValueSpecificationAction,
)
xmof::CompleteActions::ReduceAction_strategy = st.builds(
    xmof::CompleteActions::ReduceAction,
    ordered=
        st.booleans()
)
xmof::IntermediateActions::LinkAction_strategy = st.builds(
    xmof::IntermediateActions::LinkAction,
)
xmof::IntermediateActions::DestroyObjectAction_strategy = st.builds(
    xmof::IntermediateActions::DestroyObjectAction,
    destroyLinks=
        st.booleans(),
    destroyOwnedObjects=
        st.booleans()
)
xmof::BasicActions::InvocationAction_strategy = st.builds(
    xmof::BasicActions::InvocationAction,
)
xmof::CompleteActions::ReadIsClassifiedObjectAction_strategy = st.builds(
    xmof::CompleteActions::ReadIsClassifiedObjectAction,
    direct=
        st.booleans()
)
xmof::IntermediateActions::ClearAssociationAction_strategy = st.builds(
    xmof::IntermediateActions::ClearAssociationAction,
)
xmof::CompleteActions::ReclassifyObjectAction_strategy = st.builds(
    xmof::CompleteActions::ReclassifyObjectAction,
    replaceAll=
        st.booleans()
)
xmof::CompleteActions::ReadExtentAction_strategy = st.builds(
    xmof::CompleteActions::ReadExtentAction,
)
xmof::CompleteActions::StartClassifierBehaviorAction_strategy = st.builds(
    xmof::CompleteActions::StartClassifierBehaviorAction,
)
xmof::IntermediateActions::TestIdentityAction_strategy = st.builds(
    xmof::IntermediateActions::TestIdentityAction,
)
xmof::CompleteActions::AcceptEventAction_strategy = st.builds(
    xmof::CompleteActions::AcceptEventAction,
    unmarshall=
        st.booleans()
)
xmof::IntermediateActions::StructuralFeatureAction_strategy = st.builds(
    xmof::IntermediateActions::StructuralFeatureAction,
)
xmof::CompleteStructuredActivities::StructuredActivityNode_strategy = st.builds(
    xmof::CompleteStructuredActivities::StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
ExtraStructuredActivities::ExpansionNode_strategy = st.builds(
    ExtraStructuredActivities::ExpansionNode,
)
ExtraStructuredActivities::ExpansionRegion_strategy = st.builds(
    ExtraStructuredActivities::ExpansionRegion,
)
xmof::CompleteStructuredActivities::Clause_strategy = st.builds(
    xmof::CompleteStructuredActivities::Clause,
)
CompleteStructuredActivities::Clause_strategy = st.builds(
    CompleteStructuredActivities::Clause,
)
xmof::IntermediateActivities::ControlFlow_strategy = st.builds(
    xmof::IntermediateActivities::ControlFlow,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
xmof::CompleteStructuredActivities::ExecutableNode_strategy = st.builds(
    xmof::CompleteStructuredActivities::ExecutableNode,
)
xmof::IntermediateActivities::ControlNode_strategy = st.builds(
    xmof::IntermediateActivities::ControlNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
xmof::IntermediateActivities::ForkNode_strategy = st.builds(
    xmof::IntermediateActivities::ForkNode,
)
xmof::IntermediateActivities::JoinNode_strategy = st.builds(
    xmof::IntermediateActivities::JoinNode,
)
xmof::IntermediateActivities::InitialNode_strategy = st.builds(
    xmof::IntermediateActivities::InitialNode,
)
xmof::IntermediateActivities::FinalNode_strategy = st.builds(
    xmof::IntermediateActivities::FinalNode,
)
xmof::IntermediateActivities::DecisionNode_strategy = st.builds(
    xmof::IntermediateActivities::DecisionNode,
)
xmof::IntermediateActivities::MergeNode_strategy = st.builds(
    xmof::IntermediateActivities::MergeNode,
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
xmof::CompleteStructuredActivities::ConditionalNode_strategy = st.builds(
    xmof::CompleteStructuredActivities::ConditionalNode,
    determinate=
        st.booleans(),
    assured=
        st.booleans()
)
xmof::ExtraStructuredActivities::ExpansionRegion_strategy = st.builds(
    xmof::ExtraStructuredActivities::ExpansionRegion,
    mode=
        safe_text
)
xmof::CompleteStructuredActivities::LoopNode_strategy = st.builds(
    xmof::CompleteStructuredActivities::LoopNode,
    testedFirst=
        st.booleans()
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
xmof::ExtraStructuredActivities::ExpansionNode_strategy = st.builds(
    xmof::ExtraStructuredActivities::ExpansionNode,
)
xmof::IntermediateActivities::ActivityParameterNode_strategy = st.builds(
    xmof::IntermediateActivities::ActivityParameterNode,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
xmof::IntermediateActivities::ActivityFinalNode_strategy = st.builds(
    xmof::IntermediateActivities::ActivityFinalNode,
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
xmof::IntermediateActivities::ObjectNode_strategy = st.builds(
    xmof::IntermediateActivities::ObjectNode,
)
IntermediateActivities::Activity_strategy = st.builds(
    IntermediateActivities::Activity,
)
xmof::IntermediateActivities::ActivityEdge_strategy = st.builds(
    xmof::IntermediateActivities::ActivityEdge,
)

@given(instance=BasicBehaviors::ParameterValue_strategy)
@settings(max_examples=50)
def test_basicbehaviors::parametervalue_instantiation(instance):
    assert isinstance(instance, BasicBehaviors::ParameterValue)

@given(instance=xmof::BasicBehaviors::ParameterValueDefinition_strategy)
@settings(max_examples=50)
def test_xmof::basicbehaviors::parametervaluedefinition_instantiation(instance):
    assert isinstance(instance, xmof::BasicBehaviors::ParameterValueDefinition)

@given(instance=Kernel::Value_strategy)
@settings(max_examples=50)
def test_kernel::value_instantiation(instance):
    assert isinstance(instance, Kernel::Value)

@given(instance=xmof::BasicBehaviors::ParameterValue_strategy)
@settings(max_examples=50)
def test_xmof::basicbehaviors::parametervalue_instantiation(instance):
    assert isinstance(instance, xmof::BasicBehaviors::ParameterValue)

@given(instance=PrimitiveValue_strategy)
@settings(max_examples=50)
def test_primitivevalue_instantiation(instance):
    assert isinstance(instance, PrimitiveValue)

@given(instance=xmof::Kernel::IntegerValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::integervalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::IntegerValue)

@given(instance=xmof::Kernel::IntegerValue_strategy)
def test_xmof::kernel::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=xmof::Kernel::IntegerValue_strategy)
def test_xmof::kernel::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof::Kernel::StringValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::stringvalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::StringValue)

@given(instance=xmof::Kernel::StringValue_strategy)
def test_xmof::kernel::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xmof::Kernel::StringValue_strategy)
def test_xmof::kernel::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_kernel::primitivetype_instantiation(instance):
    assert isinstance(instance, Kernel::PrimitiveType)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=xmof::Kernel::EnumerationValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::enumerationvalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::EnumerationValue)

@given(instance=xmof::Kernel::PrimitiveValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::primitivevalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::PrimitiveValue)

@given(instance=xmof::LociL1::SemanticVisitor_strategy)
@settings(max_examples=50)
def test_xmof::locil1::semanticvisitor_instantiation(instance):
    assert isinstance(instance, xmof::LociL1::SemanticVisitor)

@given(instance=Kernel::xmof::EObject_strategy)
@settings(max_examples=50)
def test_kernel::xmof::eobject_instantiation(instance):
    assert isinstance(instance, Kernel::xmof::EObject)

@given(instance=xmof::Kernel::ObjectValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::objectvalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::ObjectValue)

@given(instance=SemanticVisitor_strategy)
@settings(max_examples=50)
def test_semanticvisitor_instantiation(instance):
    assert isinstance(instance, SemanticVisitor)

@given(instance=xmof::Kernel::Value_strategy)
@settings(max_examples=50)
def test_xmof::kernel::value_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::Value)

@given(instance=xmof::Kernel::BooleanValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::booleanvalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::BooleanValue)

@given(instance=xmof::Kernel::BooleanValue_strategy)
def test_xmof::kernel::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=xmof::Kernel::BooleanValue_strategy)
def test_xmof::kernel::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel::xmof::EEnum_strategy)
@settings(max_examples=50)
def test_kernel::xmof::eenum_instantiation(instance):
    assert isinstance(instance, Kernel::xmof::EEnum)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=xmof::BasicActions::CallAction_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::callaction_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::CallAction)

@given(instance=xmof::BasicActions::CallAction_strategy)
def test_xmof::basicactions::callaction_synchronous_type(instance):
    assert isinstance(instance.synchronous, bool)


@given(instance=xmof::BasicActions::CallAction_strategy)
def test_xmof::basicactions::callaction_synchronous_setter(instance):
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

@given(instance=xmof::BasicActions::OutputPin_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::outputpin_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::OutputPin)

@given(instance=xmof::BasicActions::InputPin_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::inputpin_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::InputPin)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=xmof::IntermediateActivities::ObjectFlow_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::objectflow_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ObjectFlow)

@given(instance=IntermediateActivities::ActivityEdge_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activityedge_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::ActivityEdge)

@given(instance=Kernel::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_kernel::instancespecification_instantiation(instance):
    assert isinstance(instance, Kernel::InstanceSpecification)

@given(instance=Kernel::ValueSpecification_strategy)
@settings(max_examples=50)
def test_kernel::valuespecification_instantiation(instance):
    assert isinstance(instance, Kernel::ValueSpecification)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=xmof::Kernel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_xmof::kernel::primitivetype_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::PrimitiveType)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=xmof::Kernel::LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_xmof::kernel::literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::LiteralUnlimitedNatural)

@given(instance=xmof::Kernel::LiteralUnlimitedNatural_strategy)
def test_xmof::kernel::literalunlimitednatural_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=xmof::Kernel::LiteralUnlimitedNatural_strategy)
def test_xmof::kernel::literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof::Kernel::LiteralNull_strategy)
@settings(max_examples=50)
def test_xmof::kernel::literalnull_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::LiteralNull)

@given(instance=xmof::Kernel::LiteralInteger_strategy)
@settings(max_examples=50)
def test_xmof::kernel::literalinteger_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::LiteralInteger)

@given(instance=xmof::Kernel::LiteralInteger_strategy)
def test_xmof::kernel::literalinteger_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=xmof::Kernel::LiteralInteger_strategy)
def test_xmof::kernel::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof::Kernel::LiteralString_strategy)
@settings(max_examples=50)
def test_xmof::kernel::literalstring_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::LiteralString)

@given(instance=xmof::Kernel::LiteralString_strategy)
def test_xmof::kernel::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xmof::Kernel::LiteralString_strategy)
def test_xmof::kernel::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof::Kernel::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_xmof::kernel::literalboolean_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::LiteralBoolean)

@given(instance=xmof::Kernel::LiteralBoolean_strategy)
def test_xmof::kernel::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=xmof::Kernel::LiteralBoolean_strategy)
def test_xmof::kernel::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel::Slot_strategy)
@settings(max_examples=50)
def test_kernel::slot_instantiation(instance):
    assert isinstance(instance, Kernel::Slot)

@given(instance=Kernel::xmof::EClassifier_strategy)
@settings(max_examples=50)
def test_kernel::xmof::eclassifier_instantiation(instance):
    assert isinstance(instance, Kernel::xmof::EClassifier)

@given(instance=Kernel::xmof::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_kernel::xmof::estructuralfeature_instantiation(instance):
    assert isinstance(instance, Kernel::xmof::EStructuralFeature)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=xmof::Kernel::Slot_strategy)
@settings(max_examples=50)
def test_xmof::kernel::slot_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::Slot)

@given(instance=EOperation_strategy)
@settings(max_examples=50)
def test_eoperation_instantiation(instance):
    assert isinstance(instance, EOperation)

@given(instance=xmof::Kernel::BehavioredEOperation_strategy)
@settings(max_examples=50)
def test_xmof::kernel::behavioredeoperation_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::BehavioredEOperation)

@given(instance=BehavioredEOperation_strategy)
@settings(max_examples=50)
def test_behavioredeoperation_instantiation(instance):
    assert isinstance(instance, BehavioredEOperation)

@given(instance=xmof::Communications::Reception_strategy)
@settings(max_examples=50)
def test_xmof::communications::reception_instantiation(instance):
    assert isinstance(instance, xmof::Communications::Reception)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=xmof::Communications::MessageEvent_strategy)
@settings(max_examples=50)
def test_xmof::communications::messageevent_instantiation(instance):
    assert isinstance(instance, xmof::Communications::MessageEvent)

@given(instance=Communications::Signal_strategy)
@settings(max_examples=50)
def test_communications::signal_instantiation(instance):
    assert isinstance(instance, Communications::Signal)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=xmof::Communications::SignalEvent_strategy)
@settings(max_examples=50)
def test_xmof::communications::signalevent_instantiation(instance):
    assert isinstance(instance, xmof::Communications::SignalEvent)

@given(instance=ETypedElement_strategy)
@settings(max_examples=50)
def test_etypedelement_instantiation(instance):
    assert isinstance(instance, ETypedElement)

@given(instance=xmof::BasicActions::Pin_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::pin_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::Pin)

@given(instance=xmof::Kernel::ValueSpecification_strategy)
@settings(max_examples=50)
def test_xmof::kernel::valuespecification_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::ValueSpecification)

@given(instance=Kernel::EEnumLiteralSpecification_strategy)
@settings(max_examples=50)
def test_kernel::eenumliteralspecification_instantiation(instance):
    assert isinstance(instance, Kernel::EEnumLiteralSpecification)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=xmof::Kernel::InstanceValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::instancevalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::InstanceValue)

@given(instance=xmof::Kernel::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_xmof::kernel::literalspecification_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::LiteralSpecification)

@given(instance=xmof::Kernel::EnumValue_strategy)
@settings(max_examples=50)
def test_xmof::kernel::enumvalue_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::EnumValue)

@given(instance=Kernel::xmof::EEnumLiteral_strategy)
@settings(max_examples=50)
def test_kernel::xmof::eenumliteral_instantiation(instance):
    assert isinstance(instance, Kernel::xmof::EEnumLiteral)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=xmof::Kernel::EEnumLiteralSpecification_strategy)
@settings(max_examples=50)
def test_xmof::kernel::eenumliteralspecification_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::EEnumLiteralSpecification)

@given(instance=EParameter_strategy)
@settings(max_examples=50)
def test_eparameter_instantiation(instance):
    assert isinstance(instance, EParameter)

@given(instance=xmof::Kernel::DirectedParameter_strategy)
@settings(max_examples=50)
def test_xmof::kernel::directedparameter_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::DirectedParameter)

@given(instance=xmof::Kernel::DirectedParameter_strategy)
def test_xmof::kernel::directedparameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=xmof::Kernel::DirectedParameter_strategy)
def test_xmof::kernel::directedparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=xmof::BasicBehaviors::FunctionBehavior_strategy)
@settings(max_examples=50)
def test_xmof::basicbehaviors::functionbehavior_instantiation(instance):
    assert isinstance(instance, xmof::BasicBehaviors::FunctionBehavior)

@given(instance=BasicBehaviors::Behavior_strategy)
@settings(max_examples=50)
def test_basicbehaviors::behavior_instantiation(instance):
    assert isinstance(instance, BasicBehaviors::Behavior)

@given(instance=EClassifier_strategy)
@settings(max_examples=50)
def test_eclassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)

@given(instance=xmof::BasicBehaviors::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_xmof::basicbehaviors::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, xmof::BasicBehaviors::BehavioredClassifier)

@given(instance=Communications::xmof::EAttribute_strategy)
@settings(max_examples=50)
def test_communications::xmof::eattribute_instantiation(instance):
    assert isinstance(instance, Communications::xmof::EAttribute)

@given(instance=xmof::Communications::Signal_strategy)
@settings(max_examples=50)
def test_xmof::communications::signal_instantiation(instance):
    assert isinstance(instance, xmof::Communications::Signal)

@given(instance=Communications::Event_strategy)
@settings(max_examples=50)
def test_communications::event_instantiation(instance):
    assert isinstance(instance, Communications::Event)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=xmof::Communications::Event_strategy)
@settings(max_examples=50)
def test_xmof::communications::event_instantiation(instance):
    assert isinstance(instance, xmof::Communications::Event)

@given(instance=xmof::Kernel::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_xmof::kernel::instancespecification_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::InstanceSpecification)

@given(instance=xmof::IntermediateActivities::ActivityNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::activitynode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ActivityNode)

@given(instance=xmof::Communications::Trigger_strategy)
@settings(max_examples=50)
def test_xmof::communications::trigger_instantiation(instance):
    assert isinstance(instance, xmof::Communications::Trigger)

@given(instance=BehavioredEClass_strategy)
@settings(max_examples=50)
def test_behavioredeclass_instantiation(instance):
    assert isinstance(instance, BehavioredEClass)

@given(instance=xmof::BasicBehaviors::Behavior_strategy)
@settings(max_examples=50)
def test_xmof::basicbehaviors::behavior_instantiation(instance):
    assert isinstance(instance, xmof::BasicBehaviors::Behavior)

@given(instance=xmof::BasicBehaviors::Behavior_strategy)
def test_xmof::basicbehaviors::behavior_reentrant_type(instance):
    assert isinstance(instance.reentrant, bool)


@given(instance=xmof::BasicBehaviors::Behavior_strategy)
def test_xmof::basicbehaviors::behavior_reentrant_setter(instance):
    original = instance.reentrant
    instance.reentrant = original
    assert instance.reentrant == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=xmof::IntermediateActivities::Activity_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::activity_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::Activity)

@given(instance=xmof::IntermediateActivities::Activity_strategy)
def test_xmof::intermediateactivities::activity_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=xmof::IntermediateActivities::Activity_strategy)
def test_xmof::intermediateactivities::activity_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=xmof::BasicBehaviors::OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_xmof::basicbehaviors::opaquebehavior_instantiation(instance):
    assert isinstance(instance, xmof::BasicBehaviors::OpaqueBehavior)

@given(instance=xmof::BasicBehaviors::OpaqueBehavior_strategy)
def test_xmof::basicbehaviors::opaquebehavior_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=xmof::BasicBehaviors::OpaqueBehavior_strategy)
def test_xmof::basicbehaviors::opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=xmof::BasicBehaviors::OpaqueBehavior_strategy)
def test_xmof::basicbehaviors::opaquebehavior_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=xmof::BasicBehaviors::OpaqueBehavior_strategy)
def test_xmof::basicbehaviors::opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=BasicBehaviors::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_basicbehaviors::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BasicBehaviors::BehavioredClassifier)

@given(instance=xmof::Kernel::BehavioredEClass_strategy)
@settings(max_examples=50)
def test_xmof::kernel::behavioredeclass_instantiation(instance):
    assert isinstance(instance, xmof::Kernel::BehavioredEClass)

@given(instance=Kernel::DirectedParameter_strategy)
@settings(max_examples=50)
def test_kernel::directedparameter_instantiation(instance):
    assert isinstance(instance, Kernel::DirectedParameter)

@given(instance=Kernel::BehavioredEOperation_strategy)
@settings(max_examples=50)
def test_kernel::behavioredeoperation_instantiation(instance):
    assert isinstance(instance, Kernel::BehavioredEOperation)

@given(instance=xmof::BasicActions::SendSignalAction_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::sendsignalaction_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::SendSignalAction)

@given(instance=BasicActions::xmof::EClassifier_strategy)
@settings(max_examples=50)
def test_basicactions::xmof::eclassifier_instantiation(instance):
    assert isinstance(instance, BasicActions::xmof::EClassifier)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=xmof::BasicActions::Action_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::action_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::Action)

@given(instance=xmof::BasicActions::Action_strategy)
def test_xmof::basicactions::action_locallyReentrant_type(instance):
    assert isinstance(instance.locallyReentrant, bool)


@given(instance=xmof::BasicActions::Action_strategy)
def test_xmof::basicactions::action_locallyReentrant_setter(instance):
    original = instance.locallyReentrant
    instance.locallyReentrant = original
    assert instance.locallyReentrant == original

@given(instance=Communications::Trigger_strategy)
@settings(max_examples=50)
def test_communications::trigger_instantiation(instance):
    assert isinstance(instance, Communications::Trigger)

@given(instance=CompleteActions::xmof::EClassifier_strategy)
@settings(max_examples=50)
def test_completeactions::xmof::eclassifier_instantiation(instance):
    assert isinstance(instance, CompleteActions::xmof::EClassifier)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=xmof::IntermediateActions::CreateLinkAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::createlinkaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::CreateLinkAction)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=xmof::BasicActions::CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::callbehavioraction_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::CallBehaviorAction)

@given(instance=xmof::BasicActions::CallOperationAction_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::calloperationaction_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::CallOperationAction)

@given(instance=xmof::CompleteActions::StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_xmof::completeactions::startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, xmof::CompleteActions::StartObjectBehaviorAction)

@given(instance=xmof::IntermediateActions::DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::destroylinkaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::DestroyLinkAction)

@given(instance=IntermediateActions::xmof::EClassifier_strategy)
@settings(max_examples=50)
def test_intermediateactions::xmof::eclassifier_instantiation(instance):
    assert isinstance(instance, IntermediateActions::xmof::EClassifier)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=xmof::IntermediateActions::AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::AddStructuralFeatureValueAction)

@given(instance=xmof::IntermediateActions::AddStructuralFeatureValueAction_strategy)
def test_xmof::intermediateactions::addstructuralfeaturevalueaction_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=xmof::IntermediateActions::AddStructuralFeatureValueAction_strategy)
def test_xmof::intermediateactions::addstructuralfeaturevalueaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=xmof::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::RemoveStructuralFeatureValueAction)

@given(instance=xmof::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
def test_xmof::intermediateactions::removestructuralfeaturevalueaction_removeDuplicates_type(instance):
    assert isinstance(instance.removeDuplicates, bool)


@given(instance=xmof::IntermediateActions::RemoveStructuralFeatureValueAction_strategy)
def test_xmof::intermediateactions::removestructuralfeaturevalueaction_removeDuplicates_setter(instance):
    original = instance.removeDuplicates
    instance.removeDuplicates = original
    assert instance.removeDuplicates == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=xmof::IntermediateActions::ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::ClearStructuralFeatureAction)

@given(instance=xmof::IntermediateActions::WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::WriteStructuralFeatureAction)

@given(instance=IntermediateActions::xmof::EReference_strategy)
@settings(max_examples=50)
def test_intermediateactions::xmof::ereference_instantiation(instance):
    assert isinstance(instance, IntermediateActions::xmof::EReference)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=xmof::IntermediateActions::LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::LinkEndDestructionData)

@given(instance=xmof::IntermediateActions::LinkEndDestructionData_strategy)
def test_xmof::intermediateactions::linkenddestructiondata_destroyDuplicates_type(instance):
    assert isinstance(instance.destroyDuplicates, bool)


@given(instance=xmof::IntermediateActions::LinkEndDestructionData_strategy)
def test_xmof::intermediateactions::linkenddestructiondata_destroyDuplicates_setter(instance):
    original = instance.destroyDuplicates
    instance.destroyDuplicates = original
    assert instance.destroyDuplicates == original

@given(instance=xmof::IntermediateActions::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::LinkEndCreationData)

@given(instance=xmof::IntermediateActions::LinkEndCreationData_strategy)
def test_xmof::intermediateactions::linkendcreationdata_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=xmof::IntermediateActions::LinkEndCreationData_strategy)
def test_xmof::intermediateactions::linkendcreationdata_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=xmof::IntermediateActions::ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::ReadStructuralFeatureAction)

@given(instance=IntermediateActions::xmof::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_intermediateactions::xmof::estructuralfeature_instantiation(instance):
    assert isinstance(instance, IntermediateActions::xmof::EStructuralFeature)

@given(instance=xmof::IntermediateActions::LinkEndData_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::linkenddata_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::LinkEndData)

@given(instance=IntermediateActions::LinkEndData_strategy)
@settings(max_examples=50)
def test_intermediateactions::linkenddata_instantiation(instance):
    assert isinstance(instance, IntermediateActions::LinkEndData)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=xmof::IntermediateActions::ReadLinkAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::readlinkaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::ReadLinkAction)

@given(instance=xmof::IntermediateActions::WriteLinkAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::writelinkaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::WriteLinkAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=xmof::IntermediateActions::ReadSelfAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::readselfaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::ReadSelfAction)

@given(instance=xmof::IntermediateActions::CreateObjectAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::createobjectaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::CreateObjectAction)

@given(instance=xmof::IntermediateActions::ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::valuespecificationaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::ValueSpecificationAction)

@given(instance=xmof::CompleteActions::ReduceAction_strategy)
@settings(max_examples=50)
def test_xmof::completeactions::reduceaction_instantiation(instance):
    assert isinstance(instance, xmof::CompleteActions::ReduceAction)

@given(instance=xmof::CompleteActions::ReduceAction_strategy)
def test_xmof::completeactions::reduceaction_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=xmof::CompleteActions::ReduceAction_strategy)
def test_xmof::completeactions::reduceaction_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=xmof::IntermediateActions::LinkAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::linkaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::LinkAction)

@given(instance=xmof::IntermediateActions::DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::destroyobjectaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::DestroyObjectAction)

@given(instance=xmof::IntermediateActions::DestroyObjectAction_strategy)
def test_xmof::intermediateactions::destroyobjectaction_destroyLinks_type(instance):
    assert isinstance(instance.destroyLinks, bool)


@given(instance=xmof::IntermediateActions::DestroyObjectAction_strategy)
def test_xmof::intermediateactions::destroyobjectaction_destroyLinks_setter(instance):
    original = instance.destroyLinks
    instance.destroyLinks = original
    assert instance.destroyLinks == original

@given(instance=xmof::IntermediateActions::DestroyObjectAction_strategy)
def test_xmof::intermediateactions::destroyobjectaction_destroyOwnedObjects_type(instance):
    assert isinstance(instance.destroyOwnedObjects, bool)


@given(instance=xmof::IntermediateActions::DestroyObjectAction_strategy)
def test_xmof::intermediateactions::destroyobjectaction_destroyOwnedObjects_setter(instance):
    original = instance.destroyOwnedObjects
    instance.destroyOwnedObjects = original
    assert instance.destroyOwnedObjects == original

@given(instance=xmof::BasicActions::InvocationAction_strategy)
@settings(max_examples=50)
def test_xmof::basicactions::invocationaction_instantiation(instance):
    assert isinstance(instance, xmof::BasicActions::InvocationAction)

@given(instance=xmof::CompleteActions::ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_xmof::completeactions::readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, xmof::CompleteActions::ReadIsClassifiedObjectAction)

@given(instance=xmof::CompleteActions::ReadIsClassifiedObjectAction_strategy)
def test_xmof::completeactions::readisclassifiedobjectaction_direct_type(instance):
    assert isinstance(instance.direct, bool)


@given(instance=xmof::CompleteActions::ReadIsClassifiedObjectAction_strategy)
def test_xmof::completeactions::readisclassifiedobjectaction_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original

@given(instance=xmof::IntermediateActions::ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::clearassociationaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::ClearAssociationAction)

@given(instance=xmof::CompleteActions::ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_xmof::completeactions::reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, xmof::CompleteActions::ReclassifyObjectAction)

@given(instance=xmof::CompleteActions::ReclassifyObjectAction_strategy)
def test_xmof::completeactions::reclassifyobjectaction_replaceAll_type(instance):
    assert isinstance(instance.replaceAll, bool)


@given(instance=xmof::CompleteActions::ReclassifyObjectAction_strategy)
def test_xmof::completeactions::reclassifyobjectaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=xmof::CompleteActions::ReadExtentAction_strategy)
@settings(max_examples=50)
def test_xmof::completeactions::readextentaction_instantiation(instance):
    assert isinstance(instance, xmof::CompleteActions::ReadExtentAction)

@given(instance=xmof::CompleteActions::StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_xmof::completeactions::startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, xmof::CompleteActions::StartClassifierBehaviorAction)

@given(instance=xmof::IntermediateActions::TestIdentityAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::testidentityaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::TestIdentityAction)

@given(instance=xmof::CompleteActions::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_xmof::completeactions::accepteventaction_instantiation(instance):
    assert isinstance(instance, xmof::CompleteActions::AcceptEventAction)

@given(instance=xmof::CompleteActions::AcceptEventAction_strategy)
def test_xmof::completeactions::accepteventaction_unmarshall_type(instance):
    assert isinstance(instance.unmarshall, bool)


@given(instance=xmof::CompleteActions::AcceptEventAction_strategy)
def test_xmof::completeactions::accepteventaction_unmarshall_setter(instance):
    original = instance.unmarshall
    instance.unmarshall = original
    assert instance.unmarshall == original

@given(instance=xmof::IntermediateActions::StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactions::structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActions::StructuralFeatureAction)

@given(instance=xmof::CompleteStructuredActivities::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_xmof::completestructuredactivities::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, xmof::CompleteStructuredActivities::StructuredActivityNode)

@given(instance=xmof::CompleteStructuredActivities::StructuredActivityNode_strategy)
def test_xmof::completestructuredactivities::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, bool)


@given(instance=xmof::CompleteStructuredActivities::StructuredActivityNode_strategy)
def test_xmof::completestructuredactivities::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=ExtraStructuredActivities::ExpansionNode_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities::expansionnode_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities::ExpansionNode)

@given(instance=ExtraStructuredActivities::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities::expansionregion_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities::ExpansionRegion)

@given(instance=xmof::CompleteStructuredActivities::Clause_strategy)
@settings(max_examples=50)
def test_xmof::completestructuredactivities::clause_instantiation(instance):
    assert isinstance(instance, xmof::CompleteStructuredActivities::Clause)

@given(instance=CompleteStructuredActivities::Clause_strategy)
@settings(max_examples=50)
def test_completestructuredactivities::clause_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities::Clause)

@given(instance=xmof::IntermediateActivities::ControlFlow_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::controlflow_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ControlFlow)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=xmof::CompleteStructuredActivities::ExecutableNode_strategy)
@settings(max_examples=50)
def test_xmof::completestructuredactivities::executablenode_instantiation(instance):
    assert isinstance(instance, xmof::CompleteStructuredActivities::ExecutableNode)

@given(instance=xmof::IntermediateActivities::ControlNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::controlnode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ControlNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=xmof::IntermediateActivities::ForkNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::forknode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ForkNode)

@given(instance=xmof::IntermediateActivities::JoinNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::joinnode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::JoinNode)

@given(instance=xmof::IntermediateActivities::InitialNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::initialnode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::InitialNode)

@given(instance=xmof::IntermediateActivities::FinalNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::finalnode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::FinalNode)

@given(instance=xmof::IntermediateActivities::DecisionNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::decisionnode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::DecisionNode)

@given(instance=xmof::IntermediateActivities::MergeNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::mergenode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::MergeNode)

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

@given(instance=xmof::CompleteStructuredActivities::ConditionalNode_strategy)
@settings(max_examples=50)
def test_xmof::completestructuredactivities::conditionalnode_instantiation(instance):
    assert isinstance(instance, xmof::CompleteStructuredActivities::ConditionalNode)

@given(instance=xmof::CompleteStructuredActivities::ConditionalNode_strategy)
def test_xmof::completestructuredactivities::conditionalnode_determinate_type(instance):
    assert isinstance(instance.determinate, bool)


@given(instance=xmof::CompleteStructuredActivities::ConditionalNode_strategy)
def test_xmof::completestructuredactivities::conditionalnode_determinate_setter(instance):
    original = instance.determinate
    instance.determinate = original
    assert instance.determinate == original

@given(instance=xmof::CompleteStructuredActivities::ConditionalNode_strategy)
def test_xmof::completestructuredactivities::conditionalnode_assured_type(instance):
    assert isinstance(instance.assured, bool)


@given(instance=xmof::CompleteStructuredActivities::ConditionalNode_strategy)
def test_xmof::completestructuredactivities::conditionalnode_assured_setter(instance):
    original = instance.assured
    instance.assured = original
    assert instance.assured == original

@given(instance=xmof::ExtraStructuredActivities::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_xmof::extrastructuredactivities::expansionregion_instantiation(instance):
    assert isinstance(instance, xmof::ExtraStructuredActivities::ExpansionRegion)

@given(instance=xmof::ExtraStructuredActivities::ExpansionRegion_strategy)
def test_xmof::extrastructuredactivities::expansionregion_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=xmof::ExtraStructuredActivities::ExpansionRegion_strategy)
def test_xmof::extrastructuredactivities::expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=xmof::CompleteStructuredActivities::LoopNode_strategy)
@settings(max_examples=50)
def test_xmof::completestructuredactivities::loopnode_instantiation(instance):
    assert isinstance(instance, xmof::CompleteStructuredActivities::LoopNode)

@given(instance=xmof::CompleteStructuredActivities::LoopNode_strategy)
def test_xmof::completestructuredactivities::loopnode_testedFirst_type(instance):
    assert isinstance(instance.testedFirst, bool)


@given(instance=xmof::CompleteStructuredActivities::LoopNode_strategy)
def test_xmof::completestructuredactivities::loopnode_testedFirst_setter(instance):
    original = instance.testedFirst
    instance.testedFirst = original
    assert instance.testedFirst == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=xmof::ExtraStructuredActivities::ExpansionNode_strategy)
@settings(max_examples=50)
def test_xmof::extrastructuredactivities::expansionnode_instantiation(instance):
    assert isinstance(instance, xmof::ExtraStructuredActivities::ExpansionNode)

@given(instance=xmof::IntermediateActivities::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::activityparameternode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ActivityParameterNode)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=xmof::IntermediateActivities::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::activityfinalnode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ActivityFinalNode)

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

@given(instance=xmof::IntermediateActivities::ObjectNode_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::objectnode_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ObjectNode)

@given(instance=IntermediateActivities::Activity_strategy)
@settings(max_examples=50)
def test_intermediateactivities::activity_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::Activity)

@given(instance=xmof::IntermediateActivities::ActivityEdge_strategy)
@settings(max_examples=50)
def test_xmof::intermediateactivities::activityedge_instantiation(instance):
    assert isinstance(instance, xmof::IntermediateActivities::ActivityEdge)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ram::InteractionFragment,
    ram::TemporaryProperty,
    ram::Message,
    ram::Lifeline,
    FragmentContainer,
    ram::Interaction,
    AbstractMessageView,
    ram::MessageViewReference,
    ram::MessageView,
    PrimitiveType,
    ram::RChar,
    ram::RInt,
    ram::REnum,
    ram::RString,
    ram::RBoolean,
    ImplementationClass,
    Type,
    ram::RVoid,
    ram::RAny,
    TypedElement,
    ram::PrimitiveType,
    TemporaryProperty,
    StructuralFeature,
    MappableElement,
    ram::Parameter,
    ram::Attribute,
    ram::ObjectType,
    Substitution,
    ram::TransitionSubstitution,
    ram::RFloat,
    ram::RDouble,
    ram::Constraint,
    ram::Substitution,
    ram::StateMachine,
    Mapping,
    ram::OperationMapping,
    ram::AttributeMapping,
    ram::ParameterMapping,
    ram::Property,
    ObjectType,
    ram::LayoutElement,
    ram::ElementMap,
    ram::EObject,
    ram::ContainerMap,
    RCollection,
    ram::RSequence,
    ram::RSet,
    ram::RCollection,
    LiteralSpecification,
    ram::LiteralInteger,
    ram::LiteralBoolean,
    ram::LiteralString,
    OccurrenceSpecification,
    ValueSpecification,
    ram::LiteralSpecification,
    ram::ParameterValue,
    ram::OpaqueExpression,
    ram::StructuralFeatureValue,
    ram::InteractionOperand,
    ram::FragmentContainer,
    MessageOccurrenceSpecification,
    ram::DestructionOccurrenceSpecification,
    InteractionFragment,
    ram::OriginalBehaviorExecution,
    ram::CombinedFragment,
    ram::ExecutionStatement,
    ram::OccurrenceSpecification,
    MessageEnd,
    ram::MessageOccurrenceSpecification,
    ram::ValueSpecification,
    ram::ParameterValueMapping,
    ram::StructuralFeature,
    ram::MessageEnd,
    ram::Mapping,
    ram::ClassifierMapping,
    ram::NamedElement,
    Property,
    ram::AssociationEnd,
    ram::Reference,
    Classifier,
    ram::ImplementationClass,
    ram::Class,
    ram::Classifier,
    ram::Layout,
    ram::Instantiation,
    ram::AbstractMessageView,
    ram::StructuralView,
    NamedElement,
    ram::Gate,
    ram::Operation,
    ram::StateView,
    ram::Transition,
    ram::TypedElement,
    ram::AspectMessageView,
    ram::Association,
    ram::Aspect,
    ram::MappableElement,
    ram::REnumLiteral,
    ram::State,
    ram::Type,
    Visibility,
    MessageSort,
    InstantiationType,
    InteractionOperatorKind,
    ReferenceType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ram::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(ram::InteractionFragment)


def test_ram::interactionfragment_constructor_exists():
    assert callable(ram::InteractionFragment.__init__)


def test_ram::interactionfragment_constructor_args():
    sig = inspect.signature(ram::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_ram::temporaryproperty_is_not_abstract():
    assert not inspect.isabstract(ram::TemporaryProperty)


def test_ram::temporaryproperty_constructor_exists():
    assert callable(ram::TemporaryProperty.__init__)


def test_ram::temporaryproperty_constructor_args():
    sig = inspect.signature(ram::TemporaryProperty.__init__)
    params = list(sig.parameters.keys())



def test_ram::message_is_not_abstract():
    assert not inspect.isabstract(ram::Message)


def test_ram::message_constructor_exists():
    assert callable(ram::Message.__init__)


def test_ram::message_constructor_args():
    sig = inspect.signature(ram::Message.__init__)
    params = list(sig.parameters.keys())
    assert "selfMessage" in params, "Missing parameter 'selfMessage'"
    assert "messageSort" in params, "Missing parameter 'messageSort'"

def test_ram::message_has_selfMessage():
    assert hasattr(ram::Message, "selfMessage")
    descriptor = None
    for klass in ram::Message.__mro__:
        if "selfMessage" in klass.__dict__:
            descriptor = klass.__dict__["selfMessage"]
            break
    assert isinstance(descriptor, property)

def test_ram::message_has_messageSort():
    assert hasattr(ram::Message, "messageSort")
    descriptor = None
    for klass in ram::Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)



def test_ram::lifeline_is_not_abstract():
    assert not inspect.isabstract(ram::Lifeline)


def test_ram::lifeline_constructor_exists():
    assert callable(ram::Lifeline.__init__)


def test_ram::lifeline_constructor_args():
    sig = inspect.signature(ram::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_fragmentcontainer_is_not_abstract():
    assert not inspect.isabstract(FragmentContainer)


def test_fragmentcontainer_constructor_exists():
    assert callable(FragmentContainer.__init__)


def test_fragmentcontainer_constructor_args():
    sig = inspect.signature(FragmentContainer.__init__)
    params = list(sig.parameters.keys())



def test_ram::interaction_is_not_abstract():
    assert not inspect.isabstract(ram::Interaction)


def test_ram::interaction_constructor_exists():
    assert callable(ram::Interaction.__init__)


def test_ram::interaction_constructor_args():
    sig = inspect.signature(ram::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_abstractmessageview_is_not_abstract():
    assert not inspect.isabstract(AbstractMessageView)


def test_abstractmessageview_constructor_exists():
    assert callable(AbstractMessageView.__init__)


def test_abstractmessageview_constructor_args():
    sig = inspect.signature(AbstractMessageView.__init__)
    params = list(sig.parameters.keys())



def test_ram::messageviewreference_is_not_abstract():
    assert not inspect.isabstract(ram::MessageViewReference)


def test_ram::messageviewreference_constructor_exists():
    assert callable(ram::MessageViewReference.__init__)


def test_ram::messageviewreference_constructor_args():
    sig = inspect.signature(ram::MessageViewReference.__init__)
    params = list(sig.parameters.keys())



def test_ram::messageview_is_not_abstract():
    assert not inspect.isabstract(ram::MessageView)


def test_ram::messageview_constructor_exists():
    assert callable(ram::MessageView.__init__)


def test_ram::messageview_constructor_args():
    sig = inspect.signature(ram::MessageView.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ram::rchar_is_not_abstract():
    assert not inspect.isabstract(ram::RChar)


def test_ram::rchar_constructor_exists():
    assert callable(ram::RChar.__init__)


def test_ram::rchar_constructor_args():
    sig = inspect.signature(ram::RChar.__init__)
    params = list(sig.parameters.keys())



def test_ram::rint_is_not_abstract():
    assert not inspect.isabstract(ram::RInt)


def test_ram::rint_constructor_exists():
    assert callable(ram::RInt.__init__)


def test_ram::rint_constructor_args():
    sig = inspect.signature(ram::RInt.__init__)
    params = list(sig.parameters.keys())



def test_ram::renum_is_not_abstract():
    assert not inspect.isabstract(ram::REnum)


def test_ram::renum_constructor_exists():
    assert callable(ram::REnum.__init__)


def test_ram::renum_constructor_args():
    sig = inspect.signature(ram::REnum.__init__)
    params = list(sig.parameters.keys())



def test_ram::rstring_is_not_abstract():
    assert not inspect.isabstract(ram::RString)


def test_ram::rstring_constructor_exists():
    assert callable(ram::RString.__init__)


def test_ram::rstring_constructor_args():
    sig = inspect.signature(ram::RString.__init__)
    params = list(sig.parameters.keys())



def test_ram::rboolean_is_not_abstract():
    assert not inspect.isabstract(ram::RBoolean)


def test_ram::rboolean_constructor_exists():
    assert callable(ram::RBoolean.__init__)


def test_ram::rboolean_constructor_args():
    sig = inspect.signature(ram::RBoolean.__init__)
    params = list(sig.parameters.keys())



def test_implementationclass_is_not_abstract():
    assert not inspect.isabstract(ImplementationClass)


def test_implementationclass_constructor_exists():
    assert callable(ImplementationClass.__init__)


def test_implementationclass_constructor_args():
    sig = inspect.signature(ImplementationClass.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ram::rvoid_is_not_abstract():
    assert not inspect.isabstract(ram::RVoid)


def test_ram::rvoid_constructor_exists():
    assert callable(ram::RVoid.__init__)


def test_ram::rvoid_constructor_args():
    sig = inspect.signature(ram::RVoid.__init__)
    params = list(sig.parameters.keys())



def test_ram::rany_is_not_abstract():
    assert not inspect.isabstract(ram::RAny)


def test_ram::rany_constructor_exists():
    assert callable(ram::RAny.__init__)


def test_ram::rany_constructor_args():
    sig = inspect.signature(ram::RAny.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ram::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ram::PrimitiveType)


def test_ram::primitivetype_constructor_exists():
    assert callable(ram::PrimitiveType.__init__)


def test_ram::primitivetype_constructor_args():
    sig = inspect.signature(ram::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_temporaryproperty_is_not_abstract():
    assert not inspect.isabstract(TemporaryProperty)


def test_temporaryproperty_constructor_exists():
    assert callable(TemporaryProperty.__init__)


def test_temporaryproperty_constructor_args():
    sig = inspect.signature(TemporaryProperty.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_mappableelement_is_not_abstract():
    assert not inspect.isabstract(MappableElement)


def test_mappableelement_constructor_exists():
    assert callable(MappableElement.__init__)


def test_mappableelement_constructor_args():
    sig = inspect.signature(MappableElement.__init__)
    params = list(sig.parameters.keys())



def test_ram::parameter_is_not_abstract():
    assert not inspect.isabstract(ram::Parameter)


def test_ram::parameter_constructor_exists():
    assert callable(ram::Parameter.__init__)


def test_ram::parameter_constructor_args():
    sig = inspect.signature(ram::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ram::attribute_is_not_abstract():
    assert not inspect.isabstract(ram::Attribute)


def test_ram::attribute_constructor_exists():
    assert callable(ram::Attribute.__init__)


def test_ram::attribute_constructor_args():
    sig = inspect.signature(ram::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_ram::objecttype_is_not_abstract():
    assert not inspect.isabstract(ram::ObjectType)


def test_ram::objecttype_constructor_exists():
    assert callable(ram::ObjectType.__init__)


def test_ram::objecttype_constructor_args():
    sig = inspect.signature(ram::ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_substitution_is_not_abstract():
    assert not inspect.isabstract(Substitution)


def test_substitution_constructor_exists():
    assert callable(Substitution.__init__)


def test_substitution_constructor_args():
    sig = inspect.signature(Substitution.__init__)
    params = list(sig.parameters.keys())



def test_ram::transitionsubstitution_is_not_abstract():
    assert not inspect.isabstract(ram::TransitionSubstitution)


def test_ram::transitionsubstitution_constructor_exists():
    assert callable(ram::TransitionSubstitution.__init__)


def test_ram::transitionsubstitution_constructor_args():
    sig = inspect.signature(ram::TransitionSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_ram::rfloat_is_not_abstract():
    assert not inspect.isabstract(ram::RFloat)


def test_ram::rfloat_constructor_exists():
    assert callable(ram::RFloat.__init__)


def test_ram::rfloat_constructor_args():
    sig = inspect.signature(ram::RFloat.__init__)
    params = list(sig.parameters.keys())



def test_ram::rdouble_is_not_abstract():
    assert not inspect.isabstract(ram::RDouble)


def test_ram::rdouble_constructor_exists():
    assert callable(ram::RDouble.__init__)


def test_ram::rdouble_constructor_args():
    sig = inspect.signature(ram::RDouble.__init__)
    params = list(sig.parameters.keys())



def test_ram::constraint_is_not_abstract():
    assert not inspect.isabstract(ram::Constraint)


def test_ram::constraint_constructor_exists():
    assert callable(ram::Constraint.__init__)


def test_ram::constraint_constructor_args():
    sig = inspect.signature(ram::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ram::substitution_is_not_abstract():
    assert not inspect.isabstract(ram::Substitution)


def test_ram::substitution_constructor_exists():
    assert callable(ram::Substitution.__init__)


def test_ram::substitution_constructor_args():
    sig = inspect.signature(ram::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_ram::statemachine_is_not_abstract():
    assert not inspect.isabstract(ram::StateMachine)


def test_ram::statemachine_constructor_exists():
    assert callable(ram::StateMachine.__init__)


def test_ram::statemachine_constructor_args():
    sig = inspect.signature(ram::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_ram::operationmapping_is_not_abstract():
    assert not inspect.isabstract(ram::OperationMapping)


def test_ram::operationmapping_constructor_exists():
    assert callable(ram::OperationMapping.__init__)


def test_ram::operationmapping_constructor_args():
    sig = inspect.signature(ram::OperationMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram::attributemapping_is_not_abstract():
    assert not inspect.isabstract(ram::AttributeMapping)


def test_ram::attributemapping_constructor_exists():
    assert callable(ram::AttributeMapping.__init__)


def test_ram::attributemapping_constructor_args():
    sig = inspect.signature(ram::AttributeMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram::parametermapping_is_not_abstract():
    assert not inspect.isabstract(ram::ParameterMapping)


def test_ram::parametermapping_constructor_exists():
    assert callable(ram::ParameterMapping.__init__)


def test_ram::parametermapping_constructor_args():
    sig = inspect.signature(ram::ParameterMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram::property_is_not_abstract():
    assert not inspect.isabstract(ram::Property)


def test_ram::property_constructor_exists():
    assert callable(ram::Property.__init__)


def test_ram::property_constructor_args():
    sig = inspect.signature(ram::Property.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "referenceType" in params, "Missing parameter 'referenceType'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_ram::property_has_upperBound():
    assert hasattr(ram::Property, "upperBound")
    descriptor = None
    for klass in ram::Property.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_ram::property_has_referenceType():
    assert hasattr(ram::Property, "referenceType")
    descriptor = None
    for klass in ram::Property.__mro__:
        if "referenceType" in klass.__dict__:
            descriptor = klass.__dict__["referenceType"]
            break
    assert isinstance(descriptor, property)

def test_ram::property_has_lowerBound():
    assert hasattr(ram::Property, "lowerBound")
    descriptor = None
    for klass in ram::Property.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_objecttype_is_not_abstract():
    assert not inspect.isabstract(ObjectType)


def test_objecttype_constructor_exists():
    assert callable(ObjectType.__init__)


def test_objecttype_constructor_args():
    sig = inspect.signature(ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ram::layoutelement_is_not_abstract():
    assert not inspect.isabstract(ram::LayoutElement)


def test_ram::layoutelement_constructor_exists():
    assert callable(ram::LayoutElement.__init__)


def test_ram::layoutelement_constructor_args():
    sig = inspect.signature(ram::LayoutElement.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_ram::layoutelement_has_x():
    assert hasattr(ram::LayoutElement, "x")
    descriptor = None
    for klass in ram::LayoutElement.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_ram::layoutelement_has_y():
    assert hasattr(ram::LayoutElement, "y")
    descriptor = None
    for klass in ram::LayoutElement.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_ram::elementmap_is_not_abstract():
    assert not inspect.isabstract(ram::ElementMap)


def test_ram::elementmap_constructor_exists():
    assert callable(ram::ElementMap.__init__)


def test_ram::elementmap_constructor_args():
    sig = inspect.signature(ram::ElementMap.__init__)
    params = list(sig.parameters.keys())



def test_ram::eobject_is_not_abstract():
    assert not inspect.isabstract(ram::EObject)


def test_ram::eobject_constructor_exists():
    assert callable(ram::EObject.__init__)


def test_ram::eobject_constructor_args():
    sig = inspect.signature(ram::EObject.__init__)
    params = list(sig.parameters.keys())



def test_ram::containermap_is_not_abstract():
    assert not inspect.isabstract(ram::ContainerMap)


def test_ram::containermap_constructor_exists():
    assert callable(ram::ContainerMap.__init__)


def test_ram::containermap_constructor_args():
    sig = inspect.signature(ram::ContainerMap.__init__)
    params = list(sig.parameters.keys())



def test_rcollection_is_not_abstract():
    assert not inspect.isabstract(RCollection)


def test_rcollection_constructor_exists():
    assert callable(RCollection.__init__)


def test_rcollection_constructor_args():
    sig = inspect.signature(RCollection.__init__)
    params = list(sig.parameters.keys())



def test_ram::rsequence_is_not_abstract():
    assert not inspect.isabstract(ram::RSequence)


def test_ram::rsequence_constructor_exists():
    assert callable(ram::RSequence.__init__)


def test_ram::rsequence_constructor_args():
    sig = inspect.signature(ram::RSequence.__init__)
    params = list(sig.parameters.keys())



def test_ram::rset_is_not_abstract():
    assert not inspect.isabstract(ram::RSet)


def test_ram::rset_constructor_exists():
    assert callable(ram::RSet.__init__)


def test_ram::rset_constructor_args():
    sig = inspect.signature(ram::RSet.__init__)
    params = list(sig.parameters.keys())



def test_ram::rcollection_is_not_abstract():
    assert not inspect.isabstract(ram::RCollection)


def test_ram::rcollection_constructor_exists():
    assert callable(ram::RCollection.__init__)


def test_ram::rcollection_constructor_args():
    sig = inspect.signature(ram::RCollection.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram::literalinteger_is_not_abstract():
    assert not inspect.isabstract(ram::LiteralInteger)


def test_ram::literalinteger_constructor_exists():
    assert callable(ram::LiteralInteger.__init__)


def test_ram::literalinteger_constructor_args():
    sig = inspect.signature(ram::LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ram::literalinteger_has_value():
    assert hasattr(ram::LiteralInteger, "value")
    descriptor = None
    for klass in ram::LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ram::literalboolean_is_not_abstract():
    assert not inspect.isabstract(ram::LiteralBoolean)


def test_ram::literalboolean_constructor_exists():
    assert callable(ram::LiteralBoolean.__init__)


def test_ram::literalboolean_constructor_args():
    sig = inspect.signature(ram::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ram::literalboolean_has_value():
    assert hasattr(ram::LiteralBoolean, "value")
    descriptor = None
    for klass in ram::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ram::literalstring_is_not_abstract():
    assert not inspect.isabstract(ram::LiteralString)


def test_ram::literalstring_constructor_exists():
    assert callable(ram::LiteralString.__init__)


def test_ram::literalstring_constructor_args():
    sig = inspect.signature(ram::LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ram::literalstring_has_value():
    assert hasattr(ram::LiteralString, "value")
    descriptor = None
    for klass in ram::LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram::literalspecification_is_not_abstract():
    assert not inspect.isabstract(ram::LiteralSpecification)


def test_ram::literalspecification_constructor_exists():
    assert callable(ram::LiteralSpecification.__init__)


def test_ram::literalspecification_constructor_args():
    sig = inspect.signature(ram::LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram::parametervalue_is_not_abstract():
    assert not inspect.isabstract(ram::ParameterValue)


def test_ram::parametervalue_constructor_exists():
    assert callable(ram::ParameterValue.__init__)


def test_ram::parametervalue_constructor_args():
    sig = inspect.signature(ram::ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_ram::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(ram::OpaqueExpression)


def test_ram::opaqueexpression_constructor_exists():
    assert callable(ram::OpaqueExpression.__init__)


def test_ram::opaqueexpression_constructor_args():
    sig = inspect.signature(ram::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_ram::opaqueexpression_has_body():
    assert hasattr(ram::OpaqueExpression, "body")
    descriptor = None
    for klass in ram::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_ram::opaqueexpression_has_language():
    assert hasattr(ram::OpaqueExpression, "language")
    descriptor = None
    for klass in ram::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_ram::structuralfeaturevalue_is_not_abstract():
    assert not inspect.isabstract(ram::StructuralFeatureValue)


def test_ram::structuralfeaturevalue_constructor_exists():
    assert callable(ram::StructuralFeatureValue.__init__)


def test_ram::structuralfeaturevalue_constructor_args():
    sig = inspect.signature(ram::StructuralFeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_ram::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(ram::InteractionOperand)


def test_ram::interactionoperand_constructor_exists():
    assert callable(ram::InteractionOperand.__init__)


def test_ram::interactionoperand_constructor_args():
    sig = inspect.signature(ram::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_ram::fragmentcontainer_is_not_abstract():
    assert not inspect.isabstract(ram::FragmentContainer)


def test_ram::fragmentcontainer_constructor_exists():
    assert callable(ram::FragmentContainer.__init__)


def test_ram::fragmentcontainer_constructor_args():
    sig = inspect.signature(ram::FragmentContainer.__init__)
    params = list(sig.parameters.keys())



def test_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(MessageOccurrenceSpecification)


def test_messageoccurrencespecification_constructor_exists():
    assert callable(MessageOccurrenceSpecification.__init__)


def test_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram::destructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(ram::DestructionOccurrenceSpecification)


def test_ram::destructionoccurrencespecification_constructor_exists():
    assert callable(ram::DestructionOccurrenceSpecification.__init__)


def test_ram::destructionoccurrencespecification_constructor_args():
    sig = inspect.signature(ram::DestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_ram::originalbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(ram::OriginalBehaviorExecution)


def test_ram::originalbehaviorexecution_constructor_exists():
    assert callable(ram::OriginalBehaviorExecution.__init__)


def test_ram::originalbehaviorexecution_constructor_args():
    sig = inspect.signature(ram::OriginalBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_ram::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(ram::CombinedFragment)


def test_ram::combinedfragment_constructor_exists():
    assert callable(ram::CombinedFragment.__init__)


def test_ram::combinedfragment_constructor_args():
    sig = inspect.signature(ram::CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_ram::combinedfragment_has_interactionOperator():
    assert hasattr(ram::CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in ram::CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_ram::executionstatement_is_not_abstract():
    assert not inspect.isabstract(ram::ExecutionStatement)


def test_ram::executionstatement_constructor_exists():
    assert callable(ram::ExecutionStatement.__init__)


def test_ram::executionstatement_constructor_args():
    sig = inspect.signature(ram::ExecutionStatement.__init__)
    params = list(sig.parameters.keys())



def test_ram::occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(ram::OccurrenceSpecification)


def test_ram::occurrencespecification_constructor_exists():
    assert callable(ram::OccurrenceSpecification.__init__)


def test_ram::occurrencespecification_constructor_args():
    sig = inspect.signature(ram::OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_ram::messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(ram::MessageOccurrenceSpecification)


def test_ram::messageoccurrencespecification_constructor_exists():
    assert callable(ram::MessageOccurrenceSpecification.__init__)


def test_ram::messageoccurrencespecification_constructor_args():
    sig = inspect.signature(ram::MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram::valuespecification_is_not_abstract():
    assert not inspect.isabstract(ram::ValueSpecification)


def test_ram::valuespecification_constructor_exists():
    assert callable(ram::ValueSpecification.__init__)


def test_ram::valuespecification_constructor_args():
    sig = inspect.signature(ram::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram::parametervaluemapping_is_not_abstract():
    assert not inspect.isabstract(ram::ParameterValueMapping)


def test_ram::parametervaluemapping_constructor_exists():
    assert callable(ram::ParameterValueMapping.__init__)


def test_ram::parametervaluemapping_constructor_args():
    sig = inspect.signature(ram::ParameterValueMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(ram::StructuralFeature)


def test_ram::structuralfeature_constructor_exists():
    assert callable(ram::StructuralFeature.__init__)


def test_ram::structuralfeature_constructor_args():
    sig = inspect.signature(ram::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ram::structuralfeature_has_static():
    assert hasattr(ram::StructuralFeature, "static")
    descriptor = None
    for klass in ram::StructuralFeature.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ram::messageend_is_not_abstract():
    assert not inspect.isabstract(ram::MessageEnd)


def test_ram::messageend_constructor_exists():
    assert callable(ram::MessageEnd.__init__)


def test_ram::messageend_constructor_args():
    sig = inspect.signature(ram::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_ram::mapping_is_not_abstract():
    assert not inspect.isabstract(ram::Mapping)


def test_ram::mapping_constructor_exists():
    assert callable(ram::Mapping.__init__)


def test_ram::mapping_constructor_args():
    sig = inspect.signature(ram::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_ram::classifiermapping_is_not_abstract():
    assert not inspect.isabstract(ram::ClassifierMapping)


def test_ram::classifiermapping_constructor_exists():
    assert callable(ram::ClassifierMapping.__init__)


def test_ram::classifiermapping_constructor_args():
    sig = inspect.signature(ram::ClassifierMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram::namedelement_is_not_abstract():
    assert not inspect.isabstract(ram::NamedElement)


def test_ram::namedelement_constructor_exists():
    assert callable(ram::NamedElement.__init__)


def test_ram::namedelement_constructor_args():
    sig = inspect.signature(ram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ram::namedelement_has_name():
    assert hasattr(ram::NamedElement, "name")
    descriptor = None
    for klass in ram::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_ram::associationend_is_not_abstract():
    assert not inspect.isabstract(ram::AssociationEnd)


def test_ram::associationend_constructor_exists():
    assert callable(ram::AssociationEnd.__init__)


def test_ram::associationend_constructor_args():
    sig = inspect.signature(ram::AssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "navigable" in params, "Missing parameter 'navigable'"

def test_ram::associationend_has_navigable():
    assert hasattr(ram::AssociationEnd, "navigable")
    descriptor = None
    for klass in ram::AssociationEnd.__mro__:
        if "navigable" in klass.__dict__:
            descriptor = klass.__dict__["navigable"]
            break
    assert isinstance(descriptor, property)



def test_ram::reference_is_not_abstract():
    assert not inspect.isabstract(ram::Reference)


def test_ram::reference_constructor_exists():
    assert callable(ram::Reference.__init__)


def test_ram::reference_constructor_args():
    sig = inspect.signature(ram::Reference.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_ram::implementationclass_is_not_abstract():
    assert not inspect.isabstract(ram::ImplementationClass)


def test_ram::implementationclass_constructor_exists():
    assert callable(ram::ImplementationClass.__init__)


def test_ram::implementationclass_constructor_args():
    sig = inspect.signature(ram::ImplementationClass.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_ram::implementationclass_has_instanceClassName():
    assert hasattr(ram::ImplementationClass, "instanceClassName")
    descriptor = None
    for klass in ram::ImplementationClass.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_ram::class_is_not_abstract():
    assert not inspect.isabstract(ram::Class)


def test_ram::class_constructor_exists():
    assert callable(ram::Class.__init__)


def test_ram::class_constructor_args():
    sig = inspect.signature(ram::Class.__init__)
    params = list(sig.parameters.keys())
    assert "partial" in params, "Missing parameter 'partial'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_ram::class_has_partial():
    assert hasattr(ram::Class, "partial")
    descriptor = None
    for klass in ram::Class.__mro__:
        if "partial" in klass.__dict__:
            descriptor = klass.__dict__["partial"]
            break
    assert isinstance(descriptor, property)

def test_ram::class_has_abstract():
    assert hasattr(ram::Class, "abstract")
    descriptor = None
    for klass in ram::Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_ram::classifier_is_not_abstract():
    assert not inspect.isabstract(ram::Classifier)


def test_ram::classifier_constructor_exists():
    assert callable(ram::Classifier.__init__)


def test_ram::classifier_constructor_args():
    sig = inspect.signature(ram::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_ram::layout_is_not_abstract():
    assert not inspect.isabstract(ram::Layout)


def test_ram::layout_constructor_exists():
    assert callable(ram::Layout.__init__)


def test_ram::layout_constructor_args():
    sig = inspect.signature(ram::Layout.__init__)
    params = list(sig.parameters.keys())



def test_ram::instantiation_is_not_abstract():
    assert not inspect.isabstract(ram::Instantiation)


def test_ram::instantiation_constructor_exists():
    assert callable(ram::Instantiation.__init__)


def test_ram::instantiation_constructor_args():
    sig = inspect.signature(ram::Instantiation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ram::instantiation_has_type():
    assert hasattr(ram::Instantiation, "type")
    descriptor = None
    for klass in ram::Instantiation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ram::abstractmessageview_is_not_abstract():
    assert not inspect.isabstract(ram::AbstractMessageView)


def test_ram::abstractmessageview_constructor_exists():
    assert callable(ram::AbstractMessageView.__init__)


def test_ram::abstractmessageview_constructor_args():
    sig = inspect.signature(ram::AbstractMessageView.__init__)
    params = list(sig.parameters.keys())



def test_ram::structuralview_is_not_abstract():
    assert not inspect.isabstract(ram::StructuralView)


def test_ram::structuralview_constructor_exists():
    assert callable(ram::StructuralView.__init__)


def test_ram::structuralview_constructor_args():
    sig = inspect.signature(ram::StructuralView.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ram::gate_is_not_abstract():
    assert not inspect.isabstract(ram::Gate)


def test_ram::gate_constructor_exists():
    assert callable(ram::Gate.__init__)


def test_ram::gate_constructor_args():
    sig = inspect.signature(ram::Gate.__init__)
    params = list(sig.parameters.keys())



def test_ram::operation_is_not_abstract():
    assert not inspect.isabstract(ram::Operation)


def test_ram::operation_constructor_exists():
    assert callable(ram::Operation.__init__)


def test_ram::operation_constructor_args():
    sig = inspect.signature(ram::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "partial" in params, "Missing parameter 'partial'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"

def test_ram::operation_has_partial():
    assert hasattr(ram::Operation, "partial")
    descriptor = None
    for klass in ram::Operation.__mro__:
        if "partial" in klass.__dict__:
            descriptor = klass.__dict__["partial"]
            break
    assert isinstance(descriptor, property)

def test_ram::operation_has_abstract():
    assert hasattr(ram::Operation, "abstract")
    descriptor = None
    for klass in ram::Operation.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_ram::operation_has_visibility():
    assert hasattr(ram::Operation, "visibility")
    descriptor = None
    for klass in ram::Operation.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_ram::operation_has_static():
    assert hasattr(ram::Operation, "static")
    descriptor = None
    for klass in ram::Operation.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ram::stateview_is_not_abstract():
    assert not inspect.isabstract(ram::StateView)


def test_ram::stateview_constructor_exists():
    assert callable(ram::StateView.__init__)


def test_ram::stateview_constructor_args():
    sig = inspect.signature(ram::StateView.__init__)
    params = list(sig.parameters.keys())



def test_ram::transition_is_not_abstract():
    assert not inspect.isabstract(ram::Transition)


def test_ram::transition_constructor_exists():
    assert callable(ram::Transition.__init__)


def test_ram::transition_constructor_args():
    sig = inspect.signature(ram::Transition.__init__)
    params = list(sig.parameters.keys())



def test_ram::typedelement_is_not_abstract():
    assert not inspect.isabstract(ram::TypedElement)


def test_ram::typedelement_constructor_exists():
    assert callable(ram::TypedElement.__init__)


def test_ram::typedelement_constructor_args():
    sig = inspect.signature(ram::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ram::aspectmessageview_is_not_abstract():
    assert not inspect.isabstract(ram::AspectMessageView)


def test_ram::aspectmessageview_constructor_exists():
    assert callable(ram::AspectMessageView.__init__)


def test_ram::aspectmessageview_constructor_args():
    sig = inspect.signature(ram::AspectMessageView.__init__)
    params = list(sig.parameters.keys())



def test_ram::association_is_not_abstract():
    assert not inspect.isabstract(ram::Association)


def test_ram::association_constructor_exists():
    assert callable(ram::Association.__init__)


def test_ram::association_constructor_args():
    sig = inspect.signature(ram::Association.__init__)
    params = list(sig.parameters.keys())



def test_ram::aspect_is_not_abstract():
    assert not inspect.isabstract(ram::Aspect)


def test_ram::aspect_constructor_exists():
    assert callable(ram::Aspect.__init__)


def test_ram::aspect_constructor_args():
    sig = inspect.signature(ram::Aspect.__init__)
    params = list(sig.parameters.keys())



def test_ram::mappableelement_is_not_abstract():
    assert not inspect.isabstract(ram::MappableElement)


def test_ram::mappableelement_constructor_exists():
    assert callable(ram::MappableElement.__init__)


def test_ram::mappableelement_constructor_args():
    sig = inspect.signature(ram::MappableElement.__init__)
    params = list(sig.parameters.keys())



def test_ram::renumliteral_is_not_abstract():
    assert not inspect.isabstract(ram::REnumLiteral)


def test_ram::renumliteral_constructor_exists():
    assert callable(ram::REnumLiteral.__init__)


def test_ram::renumliteral_constructor_args():
    sig = inspect.signature(ram::REnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ram::state_is_not_abstract():
    assert not inspect.isabstract(ram::State)


def test_ram::state_constructor_exists():
    assert callable(ram::State.__init__)


def test_ram::state_constructor_args():
    sig = inspect.signature(ram::State.__init__)
    params = list(sig.parameters.keys())



def test_ram::type_is_not_abstract():
    assert not inspect.isabstract(ram::Type)


def test_ram::type_constructor_exists():
    assert callable(ram::Type.__init__)


def test_ram::type_constructor_args():
    sig = inspect.signature(ram::Type.__init__)
    params = list(sig.parameters.keys())

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "package",
        "public",
        "protected",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "deleteMessage",
        "reply",
        "synchCall",
        "createMessage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_instantiationtype_exists():
    # Check that the Enumeration exists
    assert InstantiationType is not None

def test_instantiationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InstantiationType]
    expected_literals = [
        "Extends",
        "Depends",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InstantiationType"

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "loop",
        "opt",
        "alt",
        "critical",
        "disruptable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_referencetype_exists():
    # Check that the Enumeration exists
    assert ReferenceType is not None

def test_referencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceType]
    expected_literals = [
        "Regular",
        "Aggregation",
        "Composition",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceType"


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
ram::InteractionFragment_strategy = st.builds(
    ram::InteractionFragment,
)
ram::TemporaryProperty_strategy = st.builds(
    ram::TemporaryProperty,
)
ram::Message_strategy = st.builds(
    ram::Message,
    selfMessage=
        st.booleans(),
    messageSort=
        safe_text
)
ram::Lifeline_strategy = st.builds(
    ram::Lifeline,
)
FragmentContainer_strategy = st.builds(
    FragmentContainer,
)
ram::Interaction_strategy = st.builds(
    ram::Interaction,
)
AbstractMessageView_strategy = st.builds(
    AbstractMessageView,
)
ram::MessageViewReference_strategy = st.builds(
    ram::MessageViewReference,
)
ram::MessageView_strategy = st.builds(
    ram::MessageView,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
ram::RChar_strategy = st.builds(
    ram::RChar,
)
ram::RInt_strategy = st.builds(
    ram::RInt,
)
ram::REnum_strategy = st.builds(
    ram::REnum,
)
ram::RString_strategy = st.builds(
    ram::RString,
)
ram::RBoolean_strategy = st.builds(
    ram::RBoolean,
)
ImplementationClass_strategy = st.builds(
    ImplementationClass,
)
Type_strategy = st.builds(
    Type,
)
ram::RVoid_strategy = st.builds(
    ram::RVoid,
)
ram::RAny_strategy = st.builds(
    ram::RAny,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ram::PrimitiveType_strategy = st.builds(
    ram::PrimitiveType,
)
TemporaryProperty_strategy = st.builds(
    TemporaryProperty,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
MappableElement_strategy = st.builds(
    MappableElement,
)
ram::Parameter_strategy = st.builds(
    ram::Parameter,
)
ram::Attribute_strategy = st.builds(
    ram::Attribute,
)
ram::ObjectType_strategy = st.builds(
    ram::ObjectType,
)
Substitution_strategy = st.builds(
    Substitution,
)
ram::TransitionSubstitution_strategy = st.builds(
    ram::TransitionSubstitution,
)
ram::RFloat_strategy = st.builds(
    ram::RFloat,
)
ram::RDouble_strategy = st.builds(
    ram::RDouble,
)
ram::Constraint_strategy = st.builds(
    ram::Constraint,
)
ram::Substitution_strategy = st.builds(
    ram::Substitution,
)
ram::StateMachine_strategy = st.builds(
    ram::StateMachine,
)
Mapping_strategy = st.builds(
    Mapping,
)
ram::OperationMapping_strategy = st.builds(
    ram::OperationMapping,
)
ram::AttributeMapping_strategy = st.builds(
    ram::AttributeMapping,
)
ram::ParameterMapping_strategy = st.builds(
    ram::ParameterMapping,
)
ram::Property_strategy = st.builds(
    ram::Property,
    upperBound=
        st.integers(),
    referenceType=
        safe_text,
    lowerBound=
        st.integers()
)
ObjectType_strategy = st.builds(
    ObjectType,
)
ram::LayoutElement_strategy = st.builds(
    ram::LayoutElement,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ram::ElementMap_strategy = st.builds(
    ram::ElementMap,
)
ram::EObject_strategy = st.builds(
    ram::EObject,
)
ram::ContainerMap_strategy = st.builds(
    ram::ContainerMap,
)
RCollection_strategy = st.builds(
    RCollection,
)
ram::RSequence_strategy = st.builds(
    ram::RSequence,
)
ram::RSet_strategy = st.builds(
    ram::RSet,
)
ram::RCollection_strategy = st.builds(
    ram::RCollection,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
ram::LiteralInteger_strategy = st.builds(
    ram::LiteralInteger,
    value=
        st.integers()
)
ram::LiteralBoolean_strategy = st.builds(
    ram::LiteralBoolean,
    value=
        st.booleans()
)
ram::LiteralString_strategy = st.builds(
    ram::LiteralString,
    value=
        safe_text
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
ram::LiteralSpecification_strategy = st.builds(
    ram::LiteralSpecification,
)
ram::ParameterValue_strategy = st.builds(
    ram::ParameterValue,
)
ram::OpaqueExpression_strategy = st.builds(
    ram::OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
ram::StructuralFeatureValue_strategy = st.builds(
    ram::StructuralFeatureValue,
)
ram::InteractionOperand_strategy = st.builds(
    ram::InteractionOperand,
)
ram::FragmentContainer_strategy = st.builds(
    ram::FragmentContainer,
)
MessageOccurrenceSpecification_strategy = st.builds(
    MessageOccurrenceSpecification,
)
ram::DestructionOccurrenceSpecification_strategy = st.builds(
    ram::DestructionOccurrenceSpecification,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
ram::OriginalBehaviorExecution_strategy = st.builds(
    ram::OriginalBehaviorExecution,
)
ram::CombinedFragment_strategy = st.builds(
    ram::CombinedFragment,
    interactionOperator=
        safe_text
)
ram::ExecutionStatement_strategy = st.builds(
    ram::ExecutionStatement,
)
ram::OccurrenceSpecification_strategy = st.builds(
    ram::OccurrenceSpecification,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
ram::MessageOccurrenceSpecification_strategy = st.builds(
    ram::MessageOccurrenceSpecification,
)
ram::ValueSpecification_strategy = st.builds(
    ram::ValueSpecification,
)
ram::ParameterValueMapping_strategy = st.builds(
    ram::ParameterValueMapping,
)
ram::StructuralFeature_strategy = st.builds(
    ram::StructuralFeature,
    static=
        st.booleans()
)
ram::MessageEnd_strategy = st.builds(
    ram::MessageEnd,
)
ram::Mapping_strategy = st.builds(
    ram::Mapping,
)
ram::ClassifierMapping_strategy = st.builds(
    ram::ClassifierMapping,
)
ram::NamedElement_strategy = st.builds(
    ram::NamedElement,
    name=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
ram::AssociationEnd_strategy = st.builds(
    ram::AssociationEnd,
    navigable=
        st.booleans()
)
ram::Reference_strategy = st.builds(
    ram::Reference,
)
Classifier_strategy = st.builds(
    Classifier,
)
ram::ImplementationClass_strategy = st.builds(
    ram::ImplementationClass,
    instanceClassName=
        safe_text
)
ram::Class_strategy = st.builds(
    ram::Class,
    partial=
        st.booleans(),
    abstract=
        st.booleans()
)
ram::Classifier_strategy = st.builds(
    ram::Classifier,
)
ram::Layout_strategy = st.builds(
    ram::Layout,
)
ram::Instantiation_strategy = st.builds(
    ram::Instantiation,
    type=
        safe_text
)
ram::AbstractMessageView_strategy = st.builds(
    ram::AbstractMessageView,
)
ram::StructuralView_strategy = st.builds(
    ram::StructuralView,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ram::Gate_strategy = st.builds(
    ram::Gate,
)
ram::Operation_strategy = st.builds(
    ram::Operation,
    partial=
        st.booleans(),
    abstract=
        st.booleans(),
    visibility=
        safe_text,
    static=
        st.booleans()
)
ram::StateView_strategy = st.builds(
    ram::StateView,
)
ram::Transition_strategy = st.builds(
    ram::Transition,
)
ram::TypedElement_strategy = st.builds(
    ram::TypedElement,
)
ram::AspectMessageView_strategy = st.builds(
    ram::AspectMessageView,
)
ram::Association_strategy = st.builds(
    ram::Association,
)
ram::Aspect_strategy = st.builds(
    ram::Aspect,
)
ram::MappableElement_strategy = st.builds(
    ram::MappableElement,
)
ram::REnumLiteral_strategy = st.builds(
    ram::REnumLiteral,
)
ram::State_strategy = st.builds(
    ram::State,
)
ram::Type_strategy = st.builds(
    ram::Type,
)

@given(instance=ram::InteractionFragment_strategy)
@settings(max_examples=50)
def test_ram::interactionfragment_instantiation(instance):
    assert isinstance(instance, ram::InteractionFragment)

@given(instance=ram::TemporaryProperty_strategy)
@settings(max_examples=50)
def test_ram::temporaryproperty_instantiation(instance):
    assert isinstance(instance, ram::TemporaryProperty)

@given(instance=ram::Message_strategy)
@settings(max_examples=50)
def test_ram::message_instantiation(instance):
    assert isinstance(instance, ram::Message)

@given(instance=ram::Message_strategy)
def test_ram::message_selfMessage_type(instance):
    assert isinstance(instance.selfMessage, bool)


@given(instance=ram::Message_strategy)
def test_ram::message_selfMessage_setter(instance):
    original = instance.selfMessage
    instance.selfMessage = original
    assert instance.selfMessage == original

@given(instance=ram::Message_strategy)
def test_ram::message_messageSort_type(instance):
    assert isinstance(instance.messageSort, str)


@given(instance=ram::Message_strategy)
def test_ram::message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original

@given(instance=ram::Lifeline_strategy)
@settings(max_examples=50)
def test_ram::lifeline_instantiation(instance):
    assert isinstance(instance, ram::Lifeline)

@given(instance=FragmentContainer_strategy)
@settings(max_examples=50)
def test_fragmentcontainer_instantiation(instance):
    assert isinstance(instance, FragmentContainer)

@given(instance=ram::Interaction_strategy)
@settings(max_examples=50)
def test_ram::interaction_instantiation(instance):
    assert isinstance(instance, ram::Interaction)

@given(instance=AbstractMessageView_strategy)
@settings(max_examples=50)
def test_abstractmessageview_instantiation(instance):
    assert isinstance(instance, AbstractMessageView)

@given(instance=ram::MessageViewReference_strategy)
@settings(max_examples=50)
def test_ram::messageviewreference_instantiation(instance):
    assert isinstance(instance, ram::MessageViewReference)

@given(instance=ram::MessageView_strategy)
@settings(max_examples=50)
def test_ram::messageview_instantiation(instance):
    assert isinstance(instance, ram::MessageView)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=ram::RChar_strategy)
@settings(max_examples=50)
def test_ram::rchar_instantiation(instance):
    assert isinstance(instance, ram::RChar)

@given(instance=ram::RInt_strategy)
@settings(max_examples=50)
def test_ram::rint_instantiation(instance):
    assert isinstance(instance, ram::RInt)

@given(instance=ram::REnum_strategy)
@settings(max_examples=50)
def test_ram::renum_instantiation(instance):
    assert isinstance(instance, ram::REnum)

@given(instance=ram::RString_strategy)
@settings(max_examples=50)
def test_ram::rstring_instantiation(instance):
    assert isinstance(instance, ram::RString)

@given(instance=ram::RBoolean_strategy)
@settings(max_examples=50)
def test_ram::rboolean_instantiation(instance):
    assert isinstance(instance, ram::RBoolean)

@given(instance=ImplementationClass_strategy)
@settings(max_examples=50)
def test_implementationclass_instantiation(instance):
    assert isinstance(instance, ImplementationClass)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ram::RVoid_strategy)
@settings(max_examples=50)
def test_ram::rvoid_instantiation(instance):
    assert isinstance(instance, ram::RVoid)

@given(instance=ram::RAny_strategy)
@settings(max_examples=50)
def test_ram::rany_instantiation(instance):
    assert isinstance(instance, ram::RAny)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ram::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ram::primitivetype_instantiation(instance):
    assert isinstance(instance, ram::PrimitiveType)

@given(instance=TemporaryProperty_strategy)
@settings(max_examples=50)
def test_temporaryproperty_instantiation(instance):
    assert isinstance(instance, TemporaryProperty)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=MappableElement_strategy)
@settings(max_examples=50)
def test_mappableelement_instantiation(instance):
    assert isinstance(instance, MappableElement)

@given(instance=ram::Parameter_strategy)
@settings(max_examples=50)
def test_ram::parameter_instantiation(instance):
    assert isinstance(instance, ram::Parameter)

@given(instance=ram::Attribute_strategy)
@settings(max_examples=50)
def test_ram::attribute_instantiation(instance):
    assert isinstance(instance, ram::Attribute)

@given(instance=ram::ObjectType_strategy)
@settings(max_examples=50)
def test_ram::objecttype_instantiation(instance):
    assert isinstance(instance, ram::ObjectType)

@given(instance=Substitution_strategy)
@settings(max_examples=50)
def test_substitution_instantiation(instance):
    assert isinstance(instance, Substitution)

@given(instance=ram::TransitionSubstitution_strategy)
@settings(max_examples=50)
def test_ram::transitionsubstitution_instantiation(instance):
    assert isinstance(instance, ram::TransitionSubstitution)

@given(instance=ram::RFloat_strategy)
@settings(max_examples=50)
def test_ram::rfloat_instantiation(instance):
    assert isinstance(instance, ram::RFloat)

@given(instance=ram::RDouble_strategy)
@settings(max_examples=50)
def test_ram::rdouble_instantiation(instance):
    assert isinstance(instance, ram::RDouble)

@given(instance=ram::Constraint_strategy)
@settings(max_examples=50)
def test_ram::constraint_instantiation(instance):
    assert isinstance(instance, ram::Constraint)

@given(instance=ram::Substitution_strategy)
@settings(max_examples=50)
def test_ram::substitution_instantiation(instance):
    assert isinstance(instance, ram::Substitution)

@given(instance=ram::StateMachine_strategy)
@settings(max_examples=50)
def test_ram::statemachine_instantiation(instance):
    assert isinstance(instance, ram::StateMachine)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=ram::OperationMapping_strategy)
@settings(max_examples=50)
def test_ram::operationmapping_instantiation(instance):
    assert isinstance(instance, ram::OperationMapping)

@given(instance=ram::AttributeMapping_strategy)
@settings(max_examples=50)
def test_ram::attributemapping_instantiation(instance):
    assert isinstance(instance, ram::AttributeMapping)

@given(instance=ram::ParameterMapping_strategy)
@settings(max_examples=50)
def test_ram::parametermapping_instantiation(instance):
    assert isinstance(instance, ram::ParameterMapping)

@given(instance=ram::Property_strategy)
@settings(max_examples=50)
def test_ram::property_instantiation(instance):
    assert isinstance(instance, ram::Property)

@given(instance=ram::Property_strategy)
def test_ram::property_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=ram::Property_strategy)
def test_ram::property_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=ram::Property_strategy)
def test_ram::property_referenceType_type(instance):
    assert isinstance(instance.referenceType, str)


@given(instance=ram::Property_strategy)
def test_ram::property_referenceType_setter(instance):
    original = instance.referenceType
    instance.referenceType = original
    assert instance.referenceType == original

@given(instance=ram::Property_strategy)
def test_ram::property_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=ram::Property_strategy)
def test_ram::property_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=ObjectType_strategy)
@settings(max_examples=50)
def test_objecttype_instantiation(instance):
    assert isinstance(instance, ObjectType)

@given(instance=ram::LayoutElement_strategy)
@settings(max_examples=50)
def test_ram::layoutelement_instantiation(instance):
    assert isinstance(instance, ram::LayoutElement)

@given(instance=ram::LayoutElement_strategy)
def test_ram::layoutelement_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=ram::LayoutElement_strategy)
def test_ram::layoutelement_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=ram::LayoutElement_strategy)
def test_ram::layoutelement_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=ram::LayoutElement_strategy)
def test_ram::layoutelement_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=ram::ElementMap_strategy)
@settings(max_examples=50)
def test_ram::elementmap_instantiation(instance):
    assert isinstance(instance, ram::ElementMap)

@given(instance=ram::EObject_strategy)
@settings(max_examples=50)
def test_ram::eobject_instantiation(instance):
    assert isinstance(instance, ram::EObject)

@given(instance=ram::ContainerMap_strategy)
@settings(max_examples=50)
def test_ram::containermap_instantiation(instance):
    assert isinstance(instance, ram::ContainerMap)

@given(instance=RCollection_strategy)
@settings(max_examples=50)
def test_rcollection_instantiation(instance):
    assert isinstance(instance, RCollection)

@given(instance=ram::RSequence_strategy)
@settings(max_examples=50)
def test_ram::rsequence_instantiation(instance):
    assert isinstance(instance, ram::RSequence)

@given(instance=ram::RSet_strategy)
@settings(max_examples=50)
def test_ram::rset_instantiation(instance):
    assert isinstance(instance, ram::RSet)

@given(instance=ram::RCollection_strategy)
@settings(max_examples=50)
def test_ram::rcollection_instantiation(instance):
    assert isinstance(instance, ram::RCollection)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=ram::LiteralInteger_strategy)
@settings(max_examples=50)
def test_ram::literalinteger_instantiation(instance):
    assert isinstance(instance, ram::LiteralInteger)

@given(instance=ram::LiteralInteger_strategy)
def test_ram::literalinteger_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ram::LiteralInteger_strategy)
def test_ram::literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ram::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_ram::literalboolean_instantiation(instance):
    assert isinstance(instance, ram::LiteralBoolean)

@given(instance=ram::LiteralBoolean_strategy)
def test_ram::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=ram::LiteralBoolean_strategy)
def test_ram::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ram::LiteralString_strategy)
@settings(max_examples=50)
def test_ram::literalstring_instantiation(instance):
    assert isinstance(instance, ram::LiteralString)

@given(instance=ram::LiteralString_strategy)
def test_ram::literalstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ram::LiteralString_strategy)
def test_ram::literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=ram::LiteralSpecification_strategy)
@settings(max_examples=50)
def test_ram::literalspecification_instantiation(instance):
    assert isinstance(instance, ram::LiteralSpecification)

@given(instance=ram::ParameterValue_strategy)
@settings(max_examples=50)
def test_ram::parametervalue_instantiation(instance):
    assert isinstance(instance, ram::ParameterValue)

@given(instance=ram::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_ram::opaqueexpression_instantiation(instance):
    assert isinstance(instance, ram::OpaqueExpression)

@given(instance=ram::OpaqueExpression_strategy)
def test_ram::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=ram::OpaqueExpression_strategy)
def test_ram::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=ram::OpaqueExpression_strategy)
def test_ram::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=ram::OpaqueExpression_strategy)
def test_ram::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=ram::StructuralFeatureValue_strategy)
@settings(max_examples=50)
def test_ram::structuralfeaturevalue_instantiation(instance):
    assert isinstance(instance, ram::StructuralFeatureValue)

@given(instance=ram::InteractionOperand_strategy)
@settings(max_examples=50)
def test_ram::interactionoperand_instantiation(instance):
    assert isinstance(instance, ram::InteractionOperand)

@given(instance=ram::FragmentContainer_strategy)
@settings(max_examples=50)
def test_ram::fragmentcontainer_instantiation(instance):
    assert isinstance(instance, ram::FragmentContainer)

@given(instance=MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, MessageOccurrenceSpecification)

@given(instance=ram::DestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_ram::destructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, ram::DestructionOccurrenceSpecification)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=ram::OriginalBehaviorExecution_strategy)
@settings(max_examples=50)
def test_ram::originalbehaviorexecution_instantiation(instance):
    assert isinstance(instance, ram::OriginalBehaviorExecution)

@given(instance=ram::CombinedFragment_strategy)
@settings(max_examples=50)
def test_ram::combinedfragment_instantiation(instance):
    assert isinstance(instance, ram::CombinedFragment)

@given(instance=ram::CombinedFragment_strategy)
def test_ram::combinedfragment_interactionOperator_type(instance):
    assert isinstance(instance.interactionOperator, str)


@given(instance=ram::CombinedFragment_strategy)
def test_ram::combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=ram::ExecutionStatement_strategy)
@settings(max_examples=50)
def test_ram::executionstatement_instantiation(instance):
    assert isinstance(instance, ram::ExecutionStatement)

@given(instance=ram::OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_ram::occurrencespecification_instantiation(instance):
    assert isinstance(instance, ram::OccurrenceSpecification)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=ram::MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_ram::messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, ram::MessageOccurrenceSpecification)

@given(instance=ram::ValueSpecification_strategy)
@settings(max_examples=50)
def test_ram::valuespecification_instantiation(instance):
    assert isinstance(instance, ram::ValueSpecification)

@given(instance=ram::ParameterValueMapping_strategy)
@settings(max_examples=50)
def test_ram::parametervaluemapping_instantiation(instance):
    assert isinstance(instance, ram::ParameterValueMapping)

@given(instance=ram::StructuralFeature_strategy)
@settings(max_examples=50)
def test_ram::structuralfeature_instantiation(instance):
    assert isinstance(instance, ram::StructuralFeature)

@given(instance=ram::StructuralFeature_strategy)
def test_ram::structuralfeature_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=ram::StructuralFeature_strategy)
def test_ram::structuralfeature_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ram::MessageEnd_strategy)
@settings(max_examples=50)
def test_ram::messageend_instantiation(instance):
    assert isinstance(instance, ram::MessageEnd)

@given(instance=ram::Mapping_strategy)
@settings(max_examples=50)
def test_ram::mapping_instantiation(instance):
    assert isinstance(instance, ram::Mapping)

@given(instance=ram::ClassifierMapping_strategy)
@settings(max_examples=50)
def test_ram::classifiermapping_instantiation(instance):
    assert isinstance(instance, ram::ClassifierMapping)

@given(instance=ram::NamedElement_strategy)
@settings(max_examples=50)
def test_ram::namedelement_instantiation(instance):
    assert isinstance(instance, ram::NamedElement)

@given(instance=ram::NamedElement_strategy)
def test_ram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ram::NamedElement_strategy)
def test_ram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=ram::AssociationEnd_strategy)
@settings(max_examples=50)
def test_ram::associationend_instantiation(instance):
    assert isinstance(instance, ram::AssociationEnd)

@given(instance=ram::AssociationEnd_strategy)
def test_ram::associationend_navigable_type(instance):
    assert isinstance(instance.navigable, bool)


@given(instance=ram::AssociationEnd_strategy)
def test_ram::associationend_navigable_setter(instance):
    original = instance.navigable
    instance.navigable = original
    assert instance.navigable == original

@given(instance=ram::Reference_strategy)
@settings(max_examples=50)
def test_ram::reference_instantiation(instance):
    assert isinstance(instance, ram::Reference)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ram::ImplementationClass_strategy)
@settings(max_examples=50)
def test_ram::implementationclass_instantiation(instance):
    assert isinstance(instance, ram::ImplementationClass)

@given(instance=ram::ImplementationClass_strategy)
def test_ram::implementationclass_instanceClassName_type(instance):
    assert isinstance(instance.instanceClassName, str)


@given(instance=ram::ImplementationClass_strategy)
def test_ram::implementationclass_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

@given(instance=ram::Class_strategy)
@settings(max_examples=50)
def test_ram::class_instantiation(instance):
    assert isinstance(instance, ram::Class)

@given(instance=ram::Class_strategy)
def test_ram::class_partial_type(instance):
    assert isinstance(instance.partial, bool)


@given(instance=ram::Class_strategy)
def test_ram::class_partial_setter(instance):
    original = instance.partial
    instance.partial = original
    assert instance.partial == original

@given(instance=ram::Class_strategy)
def test_ram::class_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=ram::Class_strategy)
def test_ram::class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=ram::Classifier_strategy)
@settings(max_examples=50)
def test_ram::classifier_instantiation(instance):
    assert isinstance(instance, ram::Classifier)

@given(instance=ram::Layout_strategy)
@settings(max_examples=50)
def test_ram::layout_instantiation(instance):
    assert isinstance(instance, ram::Layout)

@given(instance=ram::Instantiation_strategy)
@settings(max_examples=50)
def test_ram::instantiation_instantiation(instance):
    assert isinstance(instance, ram::Instantiation)

@given(instance=ram::Instantiation_strategy)
def test_ram::instantiation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ram::Instantiation_strategy)
def test_ram::instantiation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ram::AbstractMessageView_strategy)
@settings(max_examples=50)
def test_ram::abstractmessageview_instantiation(instance):
    assert isinstance(instance, ram::AbstractMessageView)

@given(instance=ram::StructuralView_strategy)
@settings(max_examples=50)
def test_ram::structuralview_instantiation(instance):
    assert isinstance(instance, ram::StructuralView)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ram::Gate_strategy)
@settings(max_examples=50)
def test_ram::gate_instantiation(instance):
    assert isinstance(instance, ram::Gate)

@given(instance=ram::Operation_strategy)
@settings(max_examples=50)
def test_ram::operation_instantiation(instance):
    assert isinstance(instance, ram::Operation)

@given(instance=ram::Operation_strategy)
def test_ram::operation_partial_type(instance):
    assert isinstance(instance.partial, bool)


@given(instance=ram::Operation_strategy)
def test_ram::operation_partial_setter(instance):
    original = instance.partial
    instance.partial = original
    assert instance.partial == original

@given(instance=ram::Operation_strategy)
def test_ram::operation_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=ram::Operation_strategy)
def test_ram::operation_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=ram::Operation_strategy)
def test_ram::operation_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=ram::Operation_strategy)
def test_ram::operation_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ram::Operation_strategy)
def test_ram::operation_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=ram::Operation_strategy)
def test_ram::operation_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ram::StateView_strategy)
@settings(max_examples=50)
def test_ram::stateview_instantiation(instance):
    assert isinstance(instance, ram::StateView)

@given(instance=ram::Transition_strategy)
@settings(max_examples=50)
def test_ram::transition_instantiation(instance):
    assert isinstance(instance, ram::Transition)

@given(instance=ram::TypedElement_strategy)
@settings(max_examples=50)
def test_ram::typedelement_instantiation(instance):
    assert isinstance(instance, ram::TypedElement)

@given(instance=ram::AspectMessageView_strategy)
@settings(max_examples=50)
def test_ram::aspectmessageview_instantiation(instance):
    assert isinstance(instance, ram::AspectMessageView)

@given(instance=ram::Association_strategy)
@settings(max_examples=50)
def test_ram::association_instantiation(instance):
    assert isinstance(instance, ram::Association)

@given(instance=ram::Aspect_strategy)
@settings(max_examples=50)
def test_ram::aspect_instantiation(instance):
    assert isinstance(instance, ram::Aspect)

@given(instance=ram::MappableElement_strategy)
@settings(max_examples=50)
def test_ram::mappableelement_instantiation(instance):
    assert isinstance(instance, ram::MappableElement)

@given(instance=ram::REnumLiteral_strategy)
@settings(max_examples=50)
def test_ram::renumliteral_instantiation(instance):
    assert isinstance(instance, ram::REnumLiteral)

@given(instance=ram::State_strategy)
@settings(max_examples=50)
def test_ram::state_instantiation(instance):
    assert isinstance(instance, ram::State)

@given(instance=ram::Type_strategy)
@settings(max_examples=50)
def test_ram::type_instantiation(instance):
    assert isinstance(instance, ram::Type)

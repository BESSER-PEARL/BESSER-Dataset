import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Substitution,
    ram_TransitionSubstitution,
    ram_Constraint,
    ram_Substitution,
    ram_StateMachine,
    Mapping,
    ram_OperationMapping,
    ram_ParameterMapping,
    ram_AttributeMapping,
    ObjectType,
    ram_LayoutElement,
    ram_ElementMap,
    ram_EObject,
    ram_ContainerMap,
    RCollection,
    ram_RSequence,
    ram_RSet,
    LiteralSpecification,
    ram_LiteralBoolean,
    ram_LiteralInteger,
    ram_LiteralString,
    OccurrenceSpecification,
    ValueSpecification,
    ram_OpaqueExpression,
    ram_ParameterValue,
    ram_LiteralSpecification,
    ram_StructuralFeatureValue,
    ram_FragmentContainer,
    MessageOccurrenceSpecification,
    ram_DestructionOccurrenceSpecification,
    InteractionFragment,
    ram_OriginalBehaviorExecution,
    ram_CombinedFragment,
    ram_ExecutionStatement,
    ram_OccurrenceSpecification,
    MessageEnd,
    ram_MessageOccurrenceSpecification,
    ram_ValueSpecification,
    ram_ParameterValueMapping,
    ram_MessageEnd,
    ram_InteractionFragment,
    ram_TemporaryProperty,
    ram_Message,
    ram_Lifeline,
    FragmentContainer,
    ram_InteractionOperand,
    ram_Interaction,
    AbstractMessageView,
    ram_MessageViewReference,
    ram_MessageView,
    PrimitiveType,
    ram_RFloat,
    ram_RChar,
    ram_REnum,
    ram_RDouble,
    ram_RInt,
    ram_RString,
    ram_RBoolean,
    ImplementationClass,
    Type,
    ram_RAny,
    ram_RVoid,
    ram_RCollection,
    TypedElement,
    ram_StructuralFeature,
    ram_PrimitiveType,
    TemporaryProperty,
    StructuralFeature,
    ram_Property,
    MappableElement,
    ram_ObjectType,
    ram_Attribute,
    ram_Parameter,
    ram_Mapping,
    ram_ClassifierMapping,
    ram_NamedElement,
    Property,
    ram_AssociationEnd,
    ram_Reference,
    Classifier,
    ram_ImplementationClass,
    ram_Class,
    ram_Classifier,
    ram_Layout,
    ram_Instantiation,
    ram_AbstractMessageView,
    ram_StructuralView,
    NamedElement,
    ram_Operation,
    ram_State,
    ram_Transition,
    ram_AspectMessageView,
    ram_StateView,
    ram_Aspect,
    ram_Association,
    ram_MappableElement,
    ram_Type,
    ram_REnumLiteral,
    ram_TypedElement,
    ram_Gate,
    InteractionOperatorKind,
    InstantiationType,
    Visibility,
    ReferenceType,
    MessageSort,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_substitution_is_not_abstract():
    assert not inspect.isabstract(Substitution)


def test_substitution_constructor_exists():
    assert callable(Substitution.__init__)


def test_substitution_constructor_args():
    sig = inspect.signature(Substitution.__init__)
    params = list(sig.parameters.keys())



def test_ram_transitionsubstitution_is_not_abstract():
    assert not inspect.isabstract(ram_TransitionSubstitution)


def test_ram_transitionsubstitution_constructor_exists():
    assert callable(ram_TransitionSubstitution.__init__)


def test_ram_transitionsubstitution_constructor_args():
    sig = inspect.signature(ram_TransitionSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_ram_constraint_is_not_abstract():
    assert not inspect.isabstract(ram_Constraint)


def test_ram_constraint_constructor_exists():
    assert callable(ram_Constraint.__init__)


def test_ram_constraint_constructor_args():
    sig = inspect.signature(ram_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ram_substitution_is_not_abstract():
    assert not inspect.isabstract(ram_Substitution)


def test_ram_substitution_constructor_exists():
    assert callable(ram_Substitution.__init__)


def test_ram_substitution_constructor_args():
    sig = inspect.signature(ram_Substitution.__init__)
    params = list(sig.parameters.keys())



def test_ram_statemachine_is_not_abstract():
    assert not inspect.isabstract(ram_StateMachine)


def test_ram_statemachine_constructor_exists():
    assert callable(ram_StateMachine.__init__)


def test_ram_statemachine_constructor_args():
    sig = inspect.signature(ram_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_ram_operationmapping_is_not_abstract():
    assert not inspect.isabstract(ram_OperationMapping)


def test_ram_operationmapping_constructor_exists():
    assert callable(ram_OperationMapping.__init__)


def test_ram_operationmapping_constructor_args():
    sig = inspect.signature(ram_OperationMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram_parametermapping_is_not_abstract():
    assert not inspect.isabstract(ram_ParameterMapping)


def test_ram_parametermapping_constructor_exists():
    assert callable(ram_ParameterMapping.__init__)


def test_ram_parametermapping_constructor_args():
    sig = inspect.signature(ram_ParameterMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram_attributemapping_is_not_abstract():
    assert not inspect.isabstract(ram_AttributeMapping)


def test_ram_attributemapping_constructor_exists():
    assert callable(ram_AttributeMapping.__init__)


def test_ram_attributemapping_constructor_args():
    sig = inspect.signature(ram_AttributeMapping.__init__)
    params = list(sig.parameters.keys())



def test_objecttype_is_not_abstract():
    assert not inspect.isabstract(ObjectType)


def test_objecttype_constructor_exists():
    assert callable(ObjectType.__init__)


def test_objecttype_constructor_args():
    sig = inspect.signature(ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ram_layoutelement_is_not_abstract():
    assert not inspect.isabstract(ram_LayoutElement)


def test_ram_layoutelement_constructor_exists():
    assert callable(ram_LayoutElement.__init__)


def test_ram_layoutelement_constructor_args():
    sig = inspect.signature(ram_LayoutElement.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_ram_layoutelement_has_x():
    assert hasattr(ram_LayoutElement, "x")
    descriptor = None
    for klass in ram_LayoutElement.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_ram_layoutelement_has_y():
    assert hasattr(ram_LayoutElement, "y")
    descriptor = None
    for klass in ram_LayoutElement.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_ram_elementmap_is_not_abstract():
    assert not inspect.isabstract(ram_ElementMap)


def test_ram_elementmap_constructor_exists():
    assert callable(ram_ElementMap.__init__)


def test_ram_elementmap_constructor_args():
    sig = inspect.signature(ram_ElementMap.__init__)
    params = list(sig.parameters.keys())



def test_ram_eobject_is_not_abstract():
    assert not inspect.isabstract(ram_EObject)


def test_ram_eobject_constructor_exists():
    assert callable(ram_EObject.__init__)


def test_ram_eobject_constructor_args():
    sig = inspect.signature(ram_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ram_containermap_is_not_abstract():
    assert not inspect.isabstract(ram_ContainerMap)


def test_ram_containermap_constructor_exists():
    assert callable(ram_ContainerMap.__init__)


def test_ram_containermap_constructor_args():
    sig = inspect.signature(ram_ContainerMap.__init__)
    params = list(sig.parameters.keys())



def test_rcollection_is_not_abstract():
    assert not inspect.isabstract(RCollection)


def test_rcollection_constructor_exists():
    assert callable(RCollection.__init__)


def test_rcollection_constructor_args():
    sig = inspect.signature(RCollection.__init__)
    params = list(sig.parameters.keys())



def test_ram_rsequence_is_not_abstract():
    assert not inspect.isabstract(ram_RSequence)


def test_ram_rsequence_constructor_exists():
    assert callable(ram_RSequence.__init__)


def test_ram_rsequence_constructor_args():
    sig = inspect.signature(ram_RSequence.__init__)
    params = list(sig.parameters.keys())



def test_ram_rset_is_not_abstract():
    assert not inspect.isabstract(ram_RSet)


def test_ram_rset_constructor_exists():
    assert callable(ram_RSet.__init__)


def test_ram_rset_constructor_args():
    sig = inspect.signature(ram_RSet.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram_literalboolean_is_not_abstract():
    assert not inspect.isabstract(ram_LiteralBoolean)


def test_ram_literalboolean_constructor_exists():
    assert callable(ram_LiteralBoolean.__init__)


def test_ram_literalboolean_constructor_args():
    sig = inspect.signature(ram_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ram_literalboolean_has_value():
    assert hasattr(ram_LiteralBoolean, "value")
    descriptor = None
    for klass in ram_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ram_literalinteger_is_not_abstract():
    assert not inspect.isabstract(ram_LiteralInteger)


def test_ram_literalinteger_constructor_exists():
    assert callable(ram_LiteralInteger.__init__)


def test_ram_literalinteger_constructor_args():
    sig = inspect.signature(ram_LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ram_literalinteger_has_value():
    assert hasattr(ram_LiteralInteger, "value")
    descriptor = None
    for klass in ram_LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ram_literalstring_is_not_abstract():
    assert not inspect.isabstract(ram_LiteralString)


def test_ram_literalstring_constructor_exists():
    assert callable(ram_LiteralString.__init__)


def test_ram_literalstring_constructor_args():
    sig = inspect.signature(ram_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ram_literalstring_has_value():
    assert hasattr(ram_LiteralString, "value")
    descriptor = None
    for klass in ram_LiteralString.__mro__:
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



def test_ram_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(ram_OpaqueExpression)


def test_ram_opaqueexpression_constructor_exists():
    assert callable(ram_OpaqueExpression.__init__)


def test_ram_opaqueexpression_constructor_args():
    sig = inspect.signature(ram_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_ram_opaqueexpression_has_language():
    assert hasattr(ram_OpaqueExpression, "language")
    descriptor = None
    for klass in ram_OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_ram_opaqueexpression_has_body():
    assert hasattr(ram_OpaqueExpression, "body")
    descriptor = None
    for klass in ram_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_ram_parametervalue_is_not_abstract():
    assert not inspect.isabstract(ram_ParameterValue)


def test_ram_parametervalue_constructor_exists():
    assert callable(ram_ParameterValue.__init__)


def test_ram_parametervalue_constructor_args():
    sig = inspect.signature(ram_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_ram_literalspecification_is_not_abstract():
    assert not inspect.isabstract(ram_LiteralSpecification)


def test_ram_literalspecification_constructor_exists():
    assert callable(ram_LiteralSpecification.__init__)


def test_ram_literalspecification_constructor_args():
    sig = inspect.signature(ram_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram_structuralfeaturevalue_is_not_abstract():
    assert not inspect.isabstract(ram_StructuralFeatureValue)


def test_ram_structuralfeaturevalue_constructor_exists():
    assert callable(ram_StructuralFeatureValue.__init__)


def test_ram_structuralfeaturevalue_constructor_args():
    sig = inspect.signature(ram_StructuralFeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_ram_fragmentcontainer_is_not_abstract():
    assert not inspect.isabstract(ram_FragmentContainer)


def test_ram_fragmentcontainer_constructor_exists():
    assert callable(ram_FragmentContainer.__init__)


def test_ram_fragmentcontainer_constructor_args():
    sig = inspect.signature(ram_FragmentContainer.__init__)
    params = list(sig.parameters.keys())



def test_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(MessageOccurrenceSpecification)


def test_messageoccurrencespecification_constructor_exists():
    assert callable(MessageOccurrenceSpecification.__init__)


def test_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram_destructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(ram_DestructionOccurrenceSpecification)


def test_ram_destructionoccurrencespecification_constructor_exists():
    assert callable(ram_DestructionOccurrenceSpecification.__init__)


def test_ram_destructionoccurrencespecification_constructor_args():
    sig = inspect.signature(ram_DestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_ram_originalbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(ram_OriginalBehaviorExecution)


def test_ram_originalbehaviorexecution_constructor_exists():
    assert callable(ram_OriginalBehaviorExecution.__init__)


def test_ram_originalbehaviorexecution_constructor_args():
    sig = inspect.signature(ram_OriginalBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_ram_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(ram_CombinedFragment)


def test_ram_combinedfragment_constructor_exists():
    assert callable(ram_CombinedFragment.__init__)


def test_ram_combinedfragment_constructor_args():
    sig = inspect.signature(ram_CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_ram_combinedfragment_has_interactionOperator():
    assert hasattr(ram_CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in ram_CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_ram_executionstatement_is_not_abstract():
    assert not inspect.isabstract(ram_ExecutionStatement)


def test_ram_executionstatement_constructor_exists():
    assert callable(ram_ExecutionStatement.__init__)


def test_ram_executionstatement_constructor_args():
    sig = inspect.signature(ram_ExecutionStatement.__init__)
    params = list(sig.parameters.keys())



def test_ram_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(ram_OccurrenceSpecification)


def test_ram_occurrencespecification_constructor_exists():
    assert callable(ram_OccurrenceSpecification.__init__)


def test_ram_occurrencespecification_constructor_args():
    sig = inspect.signature(ram_OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_ram_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(ram_MessageOccurrenceSpecification)


def test_ram_messageoccurrencespecification_constructor_exists():
    assert callable(ram_MessageOccurrenceSpecification.__init__)


def test_ram_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(ram_MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ram_ValueSpecification)


def test_ram_valuespecification_constructor_exists():
    assert callable(ram_ValueSpecification.__init__)


def test_ram_valuespecification_constructor_args():
    sig = inspect.signature(ram_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ram_parametervaluemapping_is_not_abstract():
    assert not inspect.isabstract(ram_ParameterValueMapping)


def test_ram_parametervaluemapping_constructor_exists():
    assert callable(ram_ParameterValueMapping.__init__)


def test_ram_parametervaluemapping_constructor_args():
    sig = inspect.signature(ram_ParameterValueMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram_messageend_is_not_abstract():
    assert not inspect.isabstract(ram_MessageEnd)


def test_ram_messageend_constructor_exists():
    assert callable(ram_MessageEnd.__init__)


def test_ram_messageend_constructor_args():
    sig = inspect.signature(ram_MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_ram_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(ram_InteractionFragment)


def test_ram_interactionfragment_constructor_exists():
    assert callable(ram_InteractionFragment.__init__)


def test_ram_interactionfragment_constructor_args():
    sig = inspect.signature(ram_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_ram_temporaryproperty_is_not_abstract():
    assert not inspect.isabstract(ram_TemporaryProperty)


def test_ram_temporaryproperty_constructor_exists():
    assert callable(ram_TemporaryProperty.__init__)


def test_ram_temporaryproperty_constructor_args():
    sig = inspect.signature(ram_TemporaryProperty.__init__)
    params = list(sig.parameters.keys())



def test_ram_message_is_not_abstract():
    assert not inspect.isabstract(ram_Message)


def test_ram_message_constructor_exists():
    assert callable(ram_Message.__init__)


def test_ram_message_constructor_args():
    sig = inspect.signature(ram_Message.__init__)
    params = list(sig.parameters.keys())
    assert "messageSort" in params, "Missing parameter 'messageSort'"
    assert "selfMessage" in params, "Missing parameter 'selfMessage'"

def test_ram_message_has_messageSort():
    assert hasattr(ram_Message, "messageSort")
    descriptor = None
    for klass in ram_Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)

def test_ram_message_has_selfMessage():
    assert hasattr(ram_Message, "selfMessage")
    descriptor = None
    for klass in ram_Message.__mro__:
        if "selfMessage" in klass.__dict__:
            descriptor = klass.__dict__["selfMessage"]
            break
    assert isinstance(descriptor, property)



def test_ram_lifeline_is_not_abstract():
    assert not inspect.isabstract(ram_Lifeline)


def test_ram_lifeline_constructor_exists():
    assert callable(ram_Lifeline.__init__)


def test_ram_lifeline_constructor_args():
    sig = inspect.signature(ram_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_fragmentcontainer_is_not_abstract():
    assert not inspect.isabstract(FragmentContainer)


def test_fragmentcontainer_constructor_exists():
    assert callable(FragmentContainer.__init__)


def test_fragmentcontainer_constructor_args():
    sig = inspect.signature(FragmentContainer.__init__)
    params = list(sig.parameters.keys())



def test_ram_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(ram_InteractionOperand)


def test_ram_interactionoperand_constructor_exists():
    assert callable(ram_InteractionOperand.__init__)


def test_ram_interactionoperand_constructor_args():
    sig = inspect.signature(ram_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_ram_interaction_is_not_abstract():
    assert not inspect.isabstract(ram_Interaction)


def test_ram_interaction_constructor_exists():
    assert callable(ram_Interaction.__init__)


def test_ram_interaction_constructor_args():
    sig = inspect.signature(ram_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_abstractmessageview_is_not_abstract():
    assert not inspect.isabstract(AbstractMessageView)


def test_abstractmessageview_constructor_exists():
    assert callable(AbstractMessageView.__init__)


def test_abstractmessageview_constructor_args():
    sig = inspect.signature(AbstractMessageView.__init__)
    params = list(sig.parameters.keys())



def test_ram_messageviewreference_is_not_abstract():
    assert not inspect.isabstract(ram_MessageViewReference)


def test_ram_messageviewreference_constructor_exists():
    assert callable(ram_MessageViewReference.__init__)


def test_ram_messageviewreference_constructor_args():
    sig = inspect.signature(ram_MessageViewReference.__init__)
    params = list(sig.parameters.keys())



def test_ram_messageview_is_not_abstract():
    assert not inspect.isabstract(ram_MessageView)


def test_ram_messageview_constructor_exists():
    assert callable(ram_MessageView.__init__)


def test_ram_messageview_constructor_args():
    sig = inspect.signature(ram_MessageView.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ram_rfloat_is_not_abstract():
    assert not inspect.isabstract(ram_RFloat)


def test_ram_rfloat_constructor_exists():
    assert callable(ram_RFloat.__init__)


def test_ram_rfloat_constructor_args():
    sig = inspect.signature(ram_RFloat.__init__)
    params = list(sig.parameters.keys())



def test_ram_rchar_is_not_abstract():
    assert not inspect.isabstract(ram_RChar)


def test_ram_rchar_constructor_exists():
    assert callable(ram_RChar.__init__)


def test_ram_rchar_constructor_args():
    sig = inspect.signature(ram_RChar.__init__)
    params = list(sig.parameters.keys())



def test_ram_renum_is_not_abstract():
    assert not inspect.isabstract(ram_REnum)


def test_ram_renum_constructor_exists():
    assert callable(ram_REnum.__init__)


def test_ram_renum_constructor_args():
    sig = inspect.signature(ram_REnum.__init__)
    params = list(sig.parameters.keys())



def test_ram_rdouble_is_not_abstract():
    assert not inspect.isabstract(ram_RDouble)


def test_ram_rdouble_constructor_exists():
    assert callable(ram_RDouble.__init__)


def test_ram_rdouble_constructor_args():
    sig = inspect.signature(ram_RDouble.__init__)
    params = list(sig.parameters.keys())



def test_ram_rint_is_not_abstract():
    assert not inspect.isabstract(ram_RInt)


def test_ram_rint_constructor_exists():
    assert callable(ram_RInt.__init__)


def test_ram_rint_constructor_args():
    sig = inspect.signature(ram_RInt.__init__)
    params = list(sig.parameters.keys())



def test_ram_rstring_is_not_abstract():
    assert not inspect.isabstract(ram_RString)


def test_ram_rstring_constructor_exists():
    assert callable(ram_RString.__init__)


def test_ram_rstring_constructor_args():
    sig = inspect.signature(ram_RString.__init__)
    params = list(sig.parameters.keys())



def test_ram_rboolean_is_not_abstract():
    assert not inspect.isabstract(ram_RBoolean)


def test_ram_rboolean_constructor_exists():
    assert callable(ram_RBoolean.__init__)


def test_ram_rboolean_constructor_args():
    sig = inspect.signature(ram_RBoolean.__init__)
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



def test_ram_rany_is_not_abstract():
    assert not inspect.isabstract(ram_RAny)


def test_ram_rany_constructor_exists():
    assert callable(ram_RAny.__init__)


def test_ram_rany_constructor_args():
    sig = inspect.signature(ram_RAny.__init__)
    params = list(sig.parameters.keys())



def test_ram_rvoid_is_not_abstract():
    assert not inspect.isabstract(ram_RVoid)


def test_ram_rvoid_constructor_exists():
    assert callable(ram_RVoid.__init__)


def test_ram_rvoid_constructor_args():
    sig = inspect.signature(ram_RVoid.__init__)
    params = list(sig.parameters.keys())



def test_ram_rcollection_is_not_abstract():
    assert not inspect.isabstract(ram_RCollection)


def test_ram_rcollection_constructor_exists():
    assert callable(ram_RCollection.__init__)


def test_ram_rcollection_constructor_args():
    sig = inspect.signature(ram_RCollection.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ram_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(ram_StructuralFeature)


def test_ram_structuralfeature_constructor_exists():
    assert callable(ram_StructuralFeature.__init__)


def test_ram_structuralfeature_constructor_args():
    sig = inspect.signature(ram_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ram_structuralfeature_has_static():
    assert hasattr(ram_StructuralFeature, "static")
    descriptor = None
    for klass in ram_StructuralFeature.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ram_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ram_PrimitiveType)


def test_ram_primitivetype_constructor_exists():
    assert callable(ram_PrimitiveType.__init__)


def test_ram_primitivetype_constructor_args():
    sig = inspect.signature(ram_PrimitiveType.__init__)
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



def test_ram_property_is_not_abstract():
    assert not inspect.isabstract(ram_Property)


def test_ram_property_constructor_exists():
    assert callable(ram_Property.__init__)


def test_ram_property_constructor_args():
    sig = inspect.signature(ram_Property.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "referenceType" in params, "Missing parameter 'referenceType'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_ram_property_has_lowerBound():
    assert hasattr(ram_Property, "lowerBound")
    descriptor = None
    for klass in ram_Property.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_ram_property_has_referenceType():
    assert hasattr(ram_Property, "referenceType")
    descriptor = None
    for klass in ram_Property.__mro__:
        if "referenceType" in klass.__dict__:
            descriptor = klass.__dict__["referenceType"]
            break
    assert isinstance(descriptor, property)

def test_ram_property_has_upperBound():
    assert hasattr(ram_Property, "upperBound")
    descriptor = None
    for klass in ram_Property.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_mappableelement_is_not_abstract():
    assert not inspect.isabstract(MappableElement)


def test_mappableelement_constructor_exists():
    assert callable(MappableElement.__init__)


def test_mappableelement_constructor_args():
    sig = inspect.signature(MappableElement.__init__)
    params = list(sig.parameters.keys())



def test_ram_objecttype_is_not_abstract():
    assert not inspect.isabstract(ram_ObjectType)


def test_ram_objecttype_constructor_exists():
    assert callable(ram_ObjectType.__init__)


def test_ram_objecttype_constructor_args():
    sig = inspect.signature(ram_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_ram_attribute_is_not_abstract():
    assert not inspect.isabstract(ram_Attribute)


def test_ram_attribute_constructor_exists():
    assert callable(ram_Attribute.__init__)


def test_ram_attribute_constructor_args():
    sig = inspect.signature(ram_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_ram_parameter_is_not_abstract():
    assert not inspect.isabstract(ram_Parameter)


def test_ram_parameter_constructor_exists():
    assert callable(ram_Parameter.__init__)


def test_ram_parameter_constructor_args():
    sig = inspect.signature(ram_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ram_mapping_is_not_abstract():
    assert not inspect.isabstract(ram_Mapping)


def test_ram_mapping_constructor_exists():
    assert callable(ram_Mapping.__init__)


def test_ram_mapping_constructor_args():
    sig = inspect.signature(ram_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_ram_classifiermapping_is_not_abstract():
    assert not inspect.isabstract(ram_ClassifierMapping)


def test_ram_classifiermapping_constructor_exists():
    assert callable(ram_ClassifierMapping.__init__)


def test_ram_classifiermapping_constructor_args():
    sig = inspect.signature(ram_ClassifierMapping.__init__)
    params = list(sig.parameters.keys())



def test_ram_namedelement_is_not_abstract():
    assert not inspect.isabstract(ram_NamedElement)


def test_ram_namedelement_constructor_exists():
    assert callable(ram_NamedElement.__init__)


def test_ram_namedelement_constructor_args():
    sig = inspect.signature(ram_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ram_namedelement_has_name():
    assert hasattr(ram_NamedElement, "name")
    descriptor = None
    for klass in ram_NamedElement.__mro__:
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



def test_ram_associationend_is_not_abstract():
    assert not inspect.isabstract(ram_AssociationEnd)


def test_ram_associationend_constructor_exists():
    assert callable(ram_AssociationEnd.__init__)


def test_ram_associationend_constructor_args():
    sig = inspect.signature(ram_AssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "navigable" in params, "Missing parameter 'navigable'"

def test_ram_associationend_has_navigable():
    assert hasattr(ram_AssociationEnd, "navigable")
    descriptor = None
    for klass in ram_AssociationEnd.__mro__:
        if "navigable" in klass.__dict__:
            descriptor = klass.__dict__["navigable"]
            break
    assert isinstance(descriptor, property)



def test_ram_reference_is_not_abstract():
    assert not inspect.isabstract(ram_Reference)


def test_ram_reference_constructor_exists():
    assert callable(ram_Reference.__init__)


def test_ram_reference_constructor_args():
    sig = inspect.signature(ram_Reference.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_ram_implementationclass_is_not_abstract():
    assert not inspect.isabstract(ram_ImplementationClass)


def test_ram_implementationclass_constructor_exists():
    assert callable(ram_ImplementationClass.__init__)


def test_ram_implementationclass_constructor_args():
    sig = inspect.signature(ram_ImplementationClass.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_ram_implementationclass_has_instanceClassName():
    assert hasattr(ram_ImplementationClass, "instanceClassName")
    descriptor = None
    for klass in ram_ImplementationClass.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_ram_class_is_not_abstract():
    assert not inspect.isabstract(ram_Class)


def test_ram_class_constructor_exists():
    assert callable(ram_Class.__init__)


def test_ram_class_constructor_args():
    sig = inspect.signature(ram_Class.__init__)
    params = list(sig.parameters.keys())
    assert "partial" in params, "Missing parameter 'partial'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_ram_class_has_partial():
    assert hasattr(ram_Class, "partial")
    descriptor = None
    for klass in ram_Class.__mro__:
        if "partial" in klass.__dict__:
            descriptor = klass.__dict__["partial"]
            break
    assert isinstance(descriptor, property)

def test_ram_class_has_abstract():
    assert hasattr(ram_Class, "abstract")
    descriptor = None
    for klass in ram_Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_ram_classifier_is_not_abstract():
    assert not inspect.isabstract(ram_Classifier)


def test_ram_classifier_constructor_exists():
    assert callable(ram_Classifier.__init__)


def test_ram_classifier_constructor_args():
    sig = inspect.signature(ram_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_ram_layout_is_not_abstract():
    assert not inspect.isabstract(ram_Layout)


def test_ram_layout_constructor_exists():
    assert callable(ram_Layout.__init__)


def test_ram_layout_constructor_args():
    sig = inspect.signature(ram_Layout.__init__)
    params = list(sig.parameters.keys())



def test_ram_instantiation_is_not_abstract():
    assert not inspect.isabstract(ram_Instantiation)


def test_ram_instantiation_constructor_exists():
    assert callable(ram_Instantiation.__init__)


def test_ram_instantiation_constructor_args():
    sig = inspect.signature(ram_Instantiation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ram_instantiation_has_type():
    assert hasattr(ram_Instantiation, "type")
    descriptor = None
    for klass in ram_Instantiation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ram_abstractmessageview_is_not_abstract():
    assert not inspect.isabstract(ram_AbstractMessageView)


def test_ram_abstractmessageview_constructor_exists():
    assert callable(ram_AbstractMessageView.__init__)


def test_ram_abstractmessageview_constructor_args():
    sig = inspect.signature(ram_AbstractMessageView.__init__)
    params = list(sig.parameters.keys())



def test_ram_structuralview_is_not_abstract():
    assert not inspect.isabstract(ram_StructuralView)


def test_ram_structuralview_constructor_exists():
    assert callable(ram_StructuralView.__init__)


def test_ram_structuralview_constructor_args():
    sig = inspect.signature(ram_StructuralView.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ram_operation_is_not_abstract():
    assert not inspect.isabstract(ram_Operation)


def test_ram_operation_constructor_exists():
    assert callable(ram_Operation.__init__)


def test_ram_operation_constructor_args():
    sig = inspect.signature(ram_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "partial" in params, "Missing parameter 'partial'"
    assert "static" in params, "Missing parameter 'static'"

def test_ram_operation_has_abstract():
    assert hasattr(ram_Operation, "abstract")
    descriptor = None
    for klass in ram_Operation.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_ram_operation_has_visibility():
    assert hasattr(ram_Operation, "visibility")
    descriptor = None
    for klass in ram_Operation.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_ram_operation_has_partial():
    assert hasattr(ram_Operation, "partial")
    descriptor = None
    for klass in ram_Operation.__mro__:
        if "partial" in klass.__dict__:
            descriptor = klass.__dict__["partial"]
            break
    assert isinstance(descriptor, property)

def test_ram_operation_has_static():
    assert hasattr(ram_Operation, "static")
    descriptor = None
    for klass in ram_Operation.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ram_state_is_not_abstract():
    assert not inspect.isabstract(ram_State)


def test_ram_state_constructor_exists():
    assert callable(ram_State.__init__)


def test_ram_state_constructor_args():
    sig = inspect.signature(ram_State.__init__)
    params = list(sig.parameters.keys())



def test_ram_transition_is_not_abstract():
    assert not inspect.isabstract(ram_Transition)


def test_ram_transition_constructor_exists():
    assert callable(ram_Transition.__init__)


def test_ram_transition_constructor_args():
    sig = inspect.signature(ram_Transition.__init__)
    params = list(sig.parameters.keys())



def test_ram_aspectmessageview_is_not_abstract():
    assert not inspect.isabstract(ram_AspectMessageView)


def test_ram_aspectmessageview_constructor_exists():
    assert callable(ram_AspectMessageView.__init__)


def test_ram_aspectmessageview_constructor_args():
    sig = inspect.signature(ram_AspectMessageView.__init__)
    params = list(sig.parameters.keys())



def test_ram_stateview_is_not_abstract():
    assert not inspect.isabstract(ram_StateView)


def test_ram_stateview_constructor_exists():
    assert callable(ram_StateView.__init__)


def test_ram_stateview_constructor_args():
    sig = inspect.signature(ram_StateView.__init__)
    params = list(sig.parameters.keys())



def test_ram_aspect_is_not_abstract():
    assert not inspect.isabstract(ram_Aspect)


def test_ram_aspect_constructor_exists():
    assert callable(ram_Aspect.__init__)


def test_ram_aspect_constructor_args():
    sig = inspect.signature(ram_Aspect.__init__)
    params = list(sig.parameters.keys())



def test_ram_association_is_not_abstract():
    assert not inspect.isabstract(ram_Association)


def test_ram_association_constructor_exists():
    assert callable(ram_Association.__init__)


def test_ram_association_constructor_args():
    sig = inspect.signature(ram_Association.__init__)
    params = list(sig.parameters.keys())



def test_ram_mappableelement_is_not_abstract():
    assert not inspect.isabstract(ram_MappableElement)


def test_ram_mappableelement_constructor_exists():
    assert callable(ram_MappableElement.__init__)


def test_ram_mappableelement_constructor_args():
    sig = inspect.signature(ram_MappableElement.__init__)
    params = list(sig.parameters.keys())



def test_ram_type_is_not_abstract():
    assert not inspect.isabstract(ram_Type)


def test_ram_type_constructor_exists():
    assert callable(ram_Type.__init__)


def test_ram_type_constructor_args():
    sig = inspect.signature(ram_Type.__init__)
    params = list(sig.parameters.keys())



def test_ram_renumliteral_is_not_abstract():
    assert not inspect.isabstract(ram_REnumLiteral)


def test_ram_renumliteral_constructor_exists():
    assert callable(ram_REnumLiteral.__init__)


def test_ram_renumliteral_constructor_args():
    sig = inspect.signature(ram_REnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ram_typedelement_is_not_abstract():
    assert not inspect.isabstract(ram_TypedElement)


def test_ram_typedelement_constructor_exists():
    assert callable(ram_TypedElement.__init__)


def test_ram_typedelement_constructor_args():
    sig = inspect.signature(ram_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ram_gate_is_not_abstract():
    assert not inspect.isabstract(ram_Gate)


def test_ram_gate_constructor_exists():
    assert callable(ram_Gate.__init__)


def test_ram_gate_constructor_args():
    sig = inspect.signature(ram_Gate.__init__)
    params = list(sig.parameters.keys())

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "critical",
        "alt",
        "loop",
        "disruptable",
        "opt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

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

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "package",
        "private",
        "public",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_referencetype_exists():
    # Check that the Enumeration exists
    assert ReferenceType is not None

def test_referencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceType]
    expected_literals = [
        "Composition",
        "Regular",
        "Aggregation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceType"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "createMessage",
        "deleteMessage",
        "synchCall",
        "reply",
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
Substitution_strategy = st.builds(
    Substitution,
)
ram_TransitionSubstitution_strategy = st.builds(
    ram_TransitionSubstitution,
)
ram_Constraint_strategy = st.builds(
    ram_Constraint,
)
ram_Substitution_strategy = st.builds(
    ram_Substitution,
)
ram_StateMachine_strategy = st.builds(
    ram_StateMachine,
)
Mapping_strategy = st.builds(
    Mapping,
)
ram_OperationMapping_strategy = st.builds(
    ram_OperationMapping,
)
ram_ParameterMapping_strategy = st.builds(
    ram_ParameterMapping,
)
ram_AttributeMapping_strategy = st.builds(
    ram_AttributeMapping,
)
ObjectType_strategy = st.builds(
    ObjectType,
)
ram_LayoutElement_strategy = st.builds(
    ram_LayoutElement,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ram_ElementMap_strategy = st.builds(
    ram_ElementMap,
)
ram_EObject_strategy = st.builds(
    ram_EObject,
)
ram_ContainerMap_strategy = st.builds(
    ram_ContainerMap,
)
RCollection_strategy = st.builds(
    RCollection,
)
ram_RSequence_strategy = st.builds(
    ram_RSequence,
)
ram_RSet_strategy = st.builds(
    ram_RSet,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
ram_LiteralBoolean_strategy = st.builds(
    ram_LiteralBoolean,
    value=
        st.booleans()
)
ram_LiteralInteger_strategy = st.builds(
    ram_LiteralInteger,
    value=
        st.integers()
)
ram_LiteralString_strategy = st.builds(
    ram_LiteralString,
    value=
        safe_text
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
ram_OpaqueExpression_strategy = st.builds(
    ram_OpaqueExpression,
    language=
        safe_text,
    body=
        safe_text
)
ram_ParameterValue_strategy = st.builds(
    ram_ParameterValue,
)
ram_LiteralSpecification_strategy = st.builds(
    ram_LiteralSpecification,
)
ram_StructuralFeatureValue_strategy = st.builds(
    ram_StructuralFeatureValue,
)
ram_FragmentContainer_strategy = st.builds(
    ram_FragmentContainer,
)
MessageOccurrenceSpecification_strategy = st.builds(
    MessageOccurrenceSpecification,
)
ram_DestructionOccurrenceSpecification_strategy = st.builds(
    ram_DestructionOccurrenceSpecification,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
ram_OriginalBehaviorExecution_strategy = st.builds(
    ram_OriginalBehaviorExecution,
)
ram_CombinedFragment_strategy = st.builds(
    ram_CombinedFragment,
    interactionOperator=
        safe_text
)
ram_ExecutionStatement_strategy = st.builds(
    ram_ExecutionStatement,
)
ram_OccurrenceSpecification_strategy = st.builds(
    ram_OccurrenceSpecification,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
ram_MessageOccurrenceSpecification_strategy = st.builds(
    ram_MessageOccurrenceSpecification,
)
ram_ValueSpecification_strategy = st.builds(
    ram_ValueSpecification,
)
ram_ParameterValueMapping_strategy = st.builds(
    ram_ParameterValueMapping,
)
ram_MessageEnd_strategy = st.builds(
    ram_MessageEnd,
)
ram_InteractionFragment_strategy = st.builds(
    ram_InteractionFragment,
)
ram_TemporaryProperty_strategy = st.builds(
    ram_TemporaryProperty,
)
ram_Message_strategy = st.builds(
    ram_Message,
    messageSort=
        safe_text,
    selfMessage=
        st.booleans()
)
ram_Lifeline_strategy = st.builds(
    ram_Lifeline,
)
FragmentContainer_strategy = st.builds(
    FragmentContainer,
)
ram_InteractionOperand_strategy = st.builds(
    ram_InteractionOperand,
)
ram_Interaction_strategy = st.builds(
    ram_Interaction,
)
AbstractMessageView_strategy = st.builds(
    AbstractMessageView,
)
ram_MessageViewReference_strategy = st.builds(
    ram_MessageViewReference,
)
ram_MessageView_strategy = st.builds(
    ram_MessageView,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
ram_RFloat_strategy = st.builds(
    ram_RFloat,
)
ram_RChar_strategy = st.builds(
    ram_RChar,
)
ram_REnum_strategy = st.builds(
    ram_REnum,
)
ram_RDouble_strategy = st.builds(
    ram_RDouble,
)
ram_RInt_strategy = st.builds(
    ram_RInt,
)
ram_RString_strategy = st.builds(
    ram_RString,
)
ram_RBoolean_strategy = st.builds(
    ram_RBoolean,
)
ImplementationClass_strategy = st.builds(
    ImplementationClass,
)
Type_strategy = st.builds(
    Type,
)
ram_RAny_strategy = st.builds(
    ram_RAny,
)
ram_RVoid_strategy = st.builds(
    ram_RVoid,
)
ram_RCollection_strategy = st.builds(
    ram_RCollection,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ram_StructuralFeature_strategy = st.builds(
    ram_StructuralFeature,
    static=
        st.booleans()
)
ram_PrimitiveType_strategy = st.builds(
    ram_PrimitiveType,
)
TemporaryProperty_strategy = st.builds(
    TemporaryProperty,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
ram_Property_strategy = st.builds(
    ram_Property,
    lowerBound=
        st.integers(),
    referenceType=
        safe_text,
    upperBound=
        st.integers()
)
MappableElement_strategy = st.builds(
    MappableElement,
)
ram_ObjectType_strategy = st.builds(
    ram_ObjectType,
)
ram_Attribute_strategy = st.builds(
    ram_Attribute,
)
ram_Parameter_strategy = st.builds(
    ram_Parameter,
)
ram_Mapping_strategy = st.builds(
    ram_Mapping,
)
ram_ClassifierMapping_strategy = st.builds(
    ram_ClassifierMapping,
)
ram_NamedElement_strategy = st.builds(
    ram_NamedElement,
    name=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
ram_AssociationEnd_strategy = st.builds(
    ram_AssociationEnd,
    navigable=
        st.booleans()
)
ram_Reference_strategy = st.builds(
    ram_Reference,
)
Classifier_strategy = st.builds(
    Classifier,
)
ram_ImplementationClass_strategy = st.builds(
    ram_ImplementationClass,
    instanceClassName=
        safe_text
)
ram_Class_strategy = st.builds(
    ram_Class,
    partial=
        st.booleans(),
    abstract=
        st.booleans()
)
ram_Classifier_strategy = st.builds(
    ram_Classifier,
)
ram_Layout_strategy = st.builds(
    ram_Layout,
)
ram_Instantiation_strategy = st.builds(
    ram_Instantiation,
    type=
        safe_text
)
ram_AbstractMessageView_strategy = st.builds(
    ram_AbstractMessageView,
)
ram_StructuralView_strategy = st.builds(
    ram_StructuralView,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ram_Operation_strategy = st.builds(
    ram_Operation,
    abstract=
        st.booleans(),
    visibility=
        safe_text,
    partial=
        st.booleans(),
    static=
        st.booleans()
)
ram_State_strategy = st.builds(
    ram_State,
)
ram_Transition_strategy = st.builds(
    ram_Transition,
)
ram_AspectMessageView_strategy = st.builds(
    ram_AspectMessageView,
)
ram_StateView_strategy = st.builds(
    ram_StateView,
)
ram_Aspect_strategy = st.builds(
    ram_Aspect,
)
ram_Association_strategy = st.builds(
    ram_Association,
)
ram_MappableElement_strategy = st.builds(
    ram_MappableElement,
)
ram_Type_strategy = st.builds(
    ram_Type,
)
ram_REnumLiteral_strategy = st.builds(
    ram_REnumLiteral,
)
ram_TypedElement_strategy = st.builds(
    ram_TypedElement,
)
ram_Gate_strategy = st.builds(
    ram_Gate,
)

@given(instance=Substitution_strategy)
@settings(max_examples=50)
def test_substitution_instantiation(instance):
    assert isinstance(instance, Substitution)

@given(instance=ram_TransitionSubstitution_strategy)
@settings(max_examples=50)
def test_ram_transitionsubstitution_instantiation(instance):
    assert isinstance(instance, ram_TransitionSubstitution)

@given(instance=ram_Constraint_strategy)
@settings(max_examples=50)
def test_ram_constraint_instantiation(instance):
    assert isinstance(instance, ram_Constraint)

@given(instance=ram_Substitution_strategy)
@settings(max_examples=50)
def test_ram_substitution_instantiation(instance):
    assert isinstance(instance, ram_Substitution)

@given(instance=ram_StateMachine_strategy)
@settings(max_examples=50)
def test_ram_statemachine_instantiation(instance):
    assert isinstance(instance, ram_StateMachine)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=ram_OperationMapping_strategy)
@settings(max_examples=50)
def test_ram_operationmapping_instantiation(instance):
    assert isinstance(instance, ram_OperationMapping)

@given(instance=ram_ParameterMapping_strategy)
@settings(max_examples=50)
def test_ram_parametermapping_instantiation(instance):
    assert isinstance(instance, ram_ParameterMapping)

@given(instance=ram_AttributeMapping_strategy)
@settings(max_examples=50)
def test_ram_attributemapping_instantiation(instance):
    assert isinstance(instance, ram_AttributeMapping)

@given(instance=ObjectType_strategy)
@settings(max_examples=50)
def test_objecttype_instantiation(instance):
    assert isinstance(instance, ObjectType)

@given(instance=ram_LayoutElement_strategy)
@settings(max_examples=50)
def test_ram_layoutelement_instantiation(instance):
    assert isinstance(instance, ram_LayoutElement)



@given(instance=ram_LayoutElement_strategy)
def test_ram_layoutelement_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=ram_LayoutElement_strategy)
def test_ram_layoutelement_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=ram_ElementMap_strategy)
@settings(max_examples=50)
def test_ram_elementmap_instantiation(instance):
    assert isinstance(instance, ram_ElementMap)

@given(instance=ram_EObject_strategy)
@settings(max_examples=50)
def test_ram_eobject_instantiation(instance):
    assert isinstance(instance, ram_EObject)

@given(instance=ram_ContainerMap_strategy)
@settings(max_examples=50)
def test_ram_containermap_instantiation(instance):
    assert isinstance(instance, ram_ContainerMap)

@given(instance=RCollection_strategy)
@settings(max_examples=50)
def test_rcollection_instantiation(instance):
    assert isinstance(instance, RCollection)

@given(instance=ram_RSequence_strategy)
@settings(max_examples=50)
def test_ram_rsequence_instantiation(instance):
    assert isinstance(instance, ram_RSequence)

@given(instance=ram_RSet_strategy)
@settings(max_examples=50)
def test_ram_rset_instantiation(instance):
    assert isinstance(instance, ram_RSet)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=ram_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_ram_literalboolean_instantiation(instance):
    assert isinstance(instance, ram_LiteralBoolean)



@given(instance=ram_LiteralBoolean_strategy)
def test_ram_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ram_LiteralInteger_strategy)
@settings(max_examples=50)
def test_ram_literalinteger_instantiation(instance):
    assert isinstance(instance, ram_LiteralInteger)



@given(instance=ram_LiteralInteger_strategy)
def test_ram_literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ram_LiteralString_strategy)
@settings(max_examples=50)
def test_ram_literalstring_instantiation(instance):
    assert isinstance(instance, ram_LiteralString)



@given(instance=ram_LiteralString_strategy)
def test_ram_literalstring_value_setter(instance):
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

@given(instance=ram_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_ram_opaqueexpression_instantiation(instance):
    assert isinstance(instance, ram_OpaqueExpression)



@given(instance=ram_OpaqueExpression_strategy)
def test_ram_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=ram_OpaqueExpression_strategy)
def test_ram_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=ram_ParameterValue_strategy)
@settings(max_examples=50)
def test_ram_parametervalue_instantiation(instance):
    assert isinstance(instance, ram_ParameterValue)

@given(instance=ram_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_ram_literalspecification_instantiation(instance):
    assert isinstance(instance, ram_LiteralSpecification)

@given(instance=ram_StructuralFeatureValue_strategy)
@settings(max_examples=50)
def test_ram_structuralfeaturevalue_instantiation(instance):
    assert isinstance(instance, ram_StructuralFeatureValue)

@given(instance=ram_FragmentContainer_strategy)
@settings(max_examples=50)
def test_ram_fragmentcontainer_instantiation(instance):
    assert isinstance(instance, ram_FragmentContainer)

@given(instance=MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, MessageOccurrenceSpecification)

@given(instance=ram_DestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_ram_destructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, ram_DestructionOccurrenceSpecification)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=ram_OriginalBehaviorExecution_strategy)
@settings(max_examples=50)
def test_ram_originalbehaviorexecution_instantiation(instance):
    assert isinstance(instance, ram_OriginalBehaviorExecution)

@given(instance=ram_CombinedFragment_strategy)
@settings(max_examples=50)
def test_ram_combinedfragment_instantiation(instance):
    assert isinstance(instance, ram_CombinedFragment)



@given(instance=ram_CombinedFragment_strategy)
def test_ram_combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=ram_ExecutionStatement_strategy)
@settings(max_examples=50)
def test_ram_executionstatement_instantiation(instance):
    assert isinstance(instance, ram_ExecutionStatement)

@given(instance=ram_OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_ram_occurrencespecification_instantiation(instance):
    assert isinstance(instance, ram_OccurrenceSpecification)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=ram_MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_ram_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, ram_MessageOccurrenceSpecification)

@given(instance=ram_ValueSpecification_strategy)
@settings(max_examples=50)
def test_ram_valuespecification_instantiation(instance):
    assert isinstance(instance, ram_ValueSpecification)

@given(instance=ram_ParameterValueMapping_strategy)
@settings(max_examples=50)
def test_ram_parametervaluemapping_instantiation(instance):
    assert isinstance(instance, ram_ParameterValueMapping)

@given(instance=ram_MessageEnd_strategy)
@settings(max_examples=50)
def test_ram_messageend_instantiation(instance):
    assert isinstance(instance, ram_MessageEnd)

@given(instance=ram_InteractionFragment_strategy)
@settings(max_examples=50)
def test_ram_interactionfragment_instantiation(instance):
    assert isinstance(instance, ram_InteractionFragment)

@given(instance=ram_TemporaryProperty_strategy)
@settings(max_examples=50)
def test_ram_temporaryproperty_instantiation(instance):
    assert isinstance(instance, ram_TemporaryProperty)

@given(instance=ram_Message_strategy)
@settings(max_examples=50)
def test_ram_message_instantiation(instance):
    assert isinstance(instance, ram_Message)



@given(instance=ram_Message_strategy)
def test_ram_message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original



@given(instance=ram_Message_strategy)
def test_ram_message_selfMessage_setter(instance):
    original = instance.selfMessage
    instance.selfMessage = original
    assert instance.selfMessage == original

@given(instance=ram_Lifeline_strategy)
@settings(max_examples=50)
def test_ram_lifeline_instantiation(instance):
    assert isinstance(instance, ram_Lifeline)

@given(instance=FragmentContainer_strategy)
@settings(max_examples=50)
def test_fragmentcontainer_instantiation(instance):
    assert isinstance(instance, FragmentContainer)

@given(instance=ram_InteractionOperand_strategy)
@settings(max_examples=50)
def test_ram_interactionoperand_instantiation(instance):
    assert isinstance(instance, ram_InteractionOperand)

@given(instance=ram_Interaction_strategy)
@settings(max_examples=50)
def test_ram_interaction_instantiation(instance):
    assert isinstance(instance, ram_Interaction)

@given(instance=AbstractMessageView_strategy)
@settings(max_examples=50)
def test_abstractmessageview_instantiation(instance):
    assert isinstance(instance, AbstractMessageView)

@given(instance=ram_MessageViewReference_strategy)
@settings(max_examples=50)
def test_ram_messageviewreference_instantiation(instance):
    assert isinstance(instance, ram_MessageViewReference)

@given(instance=ram_MessageView_strategy)
@settings(max_examples=50)
def test_ram_messageview_instantiation(instance):
    assert isinstance(instance, ram_MessageView)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=ram_RFloat_strategy)
@settings(max_examples=50)
def test_ram_rfloat_instantiation(instance):
    assert isinstance(instance, ram_RFloat)

@given(instance=ram_RChar_strategy)
@settings(max_examples=50)
def test_ram_rchar_instantiation(instance):
    assert isinstance(instance, ram_RChar)

@given(instance=ram_REnum_strategy)
@settings(max_examples=50)
def test_ram_renum_instantiation(instance):
    assert isinstance(instance, ram_REnum)

@given(instance=ram_RDouble_strategy)
@settings(max_examples=50)
def test_ram_rdouble_instantiation(instance):
    assert isinstance(instance, ram_RDouble)

@given(instance=ram_RInt_strategy)
@settings(max_examples=50)
def test_ram_rint_instantiation(instance):
    assert isinstance(instance, ram_RInt)

@given(instance=ram_RString_strategy)
@settings(max_examples=50)
def test_ram_rstring_instantiation(instance):
    assert isinstance(instance, ram_RString)

@given(instance=ram_RBoolean_strategy)
@settings(max_examples=50)
def test_ram_rboolean_instantiation(instance):
    assert isinstance(instance, ram_RBoolean)

@given(instance=ImplementationClass_strategy)
@settings(max_examples=50)
def test_implementationclass_instantiation(instance):
    assert isinstance(instance, ImplementationClass)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ram_RAny_strategy)
@settings(max_examples=50)
def test_ram_rany_instantiation(instance):
    assert isinstance(instance, ram_RAny)

@given(instance=ram_RVoid_strategy)
@settings(max_examples=50)
def test_ram_rvoid_instantiation(instance):
    assert isinstance(instance, ram_RVoid)

@given(instance=ram_RCollection_strategy)
@settings(max_examples=50)
def test_ram_rcollection_instantiation(instance):
    assert isinstance(instance, ram_RCollection)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ram_StructuralFeature_strategy)
@settings(max_examples=50)
def test_ram_structuralfeature_instantiation(instance):
    assert isinstance(instance, ram_StructuralFeature)



@given(instance=ram_StructuralFeature_strategy)
def test_ram_structuralfeature_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ram_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ram_primitivetype_instantiation(instance):
    assert isinstance(instance, ram_PrimitiveType)

@given(instance=TemporaryProperty_strategy)
@settings(max_examples=50)
def test_temporaryproperty_instantiation(instance):
    assert isinstance(instance, TemporaryProperty)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=ram_Property_strategy)
@settings(max_examples=50)
def test_ram_property_instantiation(instance):
    assert isinstance(instance, ram_Property)



@given(instance=ram_Property_strategy)
def test_ram_property_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=ram_Property_strategy)
def test_ram_property_referenceType_setter(instance):
    original = instance.referenceType
    instance.referenceType = original
    assert instance.referenceType == original



@given(instance=ram_Property_strategy)
def test_ram_property_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=MappableElement_strategy)
@settings(max_examples=50)
def test_mappableelement_instantiation(instance):
    assert isinstance(instance, MappableElement)

@given(instance=ram_ObjectType_strategy)
@settings(max_examples=50)
def test_ram_objecttype_instantiation(instance):
    assert isinstance(instance, ram_ObjectType)

@given(instance=ram_Attribute_strategy)
@settings(max_examples=50)
def test_ram_attribute_instantiation(instance):
    assert isinstance(instance, ram_Attribute)

@given(instance=ram_Parameter_strategy)
@settings(max_examples=50)
def test_ram_parameter_instantiation(instance):
    assert isinstance(instance, ram_Parameter)

@given(instance=ram_Mapping_strategy)
@settings(max_examples=50)
def test_ram_mapping_instantiation(instance):
    assert isinstance(instance, ram_Mapping)

@given(instance=ram_ClassifierMapping_strategy)
@settings(max_examples=50)
def test_ram_classifiermapping_instantiation(instance):
    assert isinstance(instance, ram_ClassifierMapping)

@given(instance=ram_NamedElement_strategy)
@settings(max_examples=50)
def test_ram_namedelement_instantiation(instance):
    assert isinstance(instance, ram_NamedElement)



@given(instance=ram_NamedElement_strategy)
def test_ram_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=ram_AssociationEnd_strategy)
@settings(max_examples=50)
def test_ram_associationend_instantiation(instance):
    assert isinstance(instance, ram_AssociationEnd)



@given(instance=ram_AssociationEnd_strategy)
def test_ram_associationend_navigable_setter(instance):
    original = instance.navigable
    instance.navigable = original
    assert instance.navigable == original

@given(instance=ram_Reference_strategy)
@settings(max_examples=50)
def test_ram_reference_instantiation(instance):
    assert isinstance(instance, ram_Reference)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ram_ImplementationClass_strategy)
@settings(max_examples=50)
def test_ram_implementationclass_instantiation(instance):
    assert isinstance(instance, ram_ImplementationClass)



@given(instance=ram_ImplementationClass_strategy)
def test_ram_implementationclass_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

@given(instance=ram_Class_strategy)
@settings(max_examples=50)
def test_ram_class_instantiation(instance):
    assert isinstance(instance, ram_Class)



@given(instance=ram_Class_strategy)
def test_ram_class_partial_setter(instance):
    original = instance.partial
    instance.partial = original
    assert instance.partial == original



@given(instance=ram_Class_strategy)
def test_ram_class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=ram_Classifier_strategy)
@settings(max_examples=50)
def test_ram_classifier_instantiation(instance):
    assert isinstance(instance, ram_Classifier)

@given(instance=ram_Layout_strategy)
@settings(max_examples=50)
def test_ram_layout_instantiation(instance):
    assert isinstance(instance, ram_Layout)

@given(instance=ram_Instantiation_strategy)
@settings(max_examples=50)
def test_ram_instantiation_instantiation(instance):
    assert isinstance(instance, ram_Instantiation)



@given(instance=ram_Instantiation_strategy)
def test_ram_instantiation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ram_AbstractMessageView_strategy)
@settings(max_examples=50)
def test_ram_abstractmessageview_instantiation(instance):
    assert isinstance(instance, ram_AbstractMessageView)

@given(instance=ram_StructuralView_strategy)
@settings(max_examples=50)
def test_ram_structuralview_instantiation(instance):
    assert isinstance(instance, ram_StructuralView)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ram_Operation_strategy)
@settings(max_examples=50)
def test_ram_operation_instantiation(instance):
    assert isinstance(instance, ram_Operation)



@given(instance=ram_Operation_strategy)
def test_ram_operation_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=ram_Operation_strategy)
def test_ram_operation_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=ram_Operation_strategy)
def test_ram_operation_partial_setter(instance):
    original = instance.partial
    instance.partial = original
    assert instance.partial == original



@given(instance=ram_Operation_strategy)
def test_ram_operation_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ram_State_strategy)
@settings(max_examples=50)
def test_ram_state_instantiation(instance):
    assert isinstance(instance, ram_State)

@given(instance=ram_Transition_strategy)
@settings(max_examples=50)
def test_ram_transition_instantiation(instance):
    assert isinstance(instance, ram_Transition)

@given(instance=ram_AspectMessageView_strategy)
@settings(max_examples=50)
def test_ram_aspectmessageview_instantiation(instance):
    assert isinstance(instance, ram_AspectMessageView)

@given(instance=ram_StateView_strategy)
@settings(max_examples=50)
def test_ram_stateview_instantiation(instance):
    assert isinstance(instance, ram_StateView)

@given(instance=ram_Aspect_strategy)
@settings(max_examples=50)
def test_ram_aspect_instantiation(instance):
    assert isinstance(instance, ram_Aspect)

@given(instance=ram_Association_strategy)
@settings(max_examples=50)
def test_ram_association_instantiation(instance):
    assert isinstance(instance, ram_Association)

@given(instance=ram_MappableElement_strategy)
@settings(max_examples=50)
def test_ram_mappableelement_instantiation(instance):
    assert isinstance(instance, ram_MappableElement)

@given(instance=ram_Type_strategy)
@settings(max_examples=50)
def test_ram_type_instantiation(instance):
    assert isinstance(instance, ram_Type)

@given(instance=ram_REnumLiteral_strategy)
@settings(max_examples=50)
def test_ram_renumliteral_instantiation(instance):
    assert isinstance(instance, ram_REnumLiteral)

@given(instance=ram_TypedElement_strategy)
@settings(max_examples=50)
def test_ram_typedelement_instantiation(instance):
    assert isinstance(instance, ram_TypedElement)

@given(instance=ram_Gate_strategy)
@settings(max_examples=50)
def test_ram_gate_instantiation(instance):
    assert isinstance(instance, ram_Gate)

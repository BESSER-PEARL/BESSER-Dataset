import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BinaryExpression,
    thingml_MinusExpression,
    thingml_TimesExpression,
    thingml_PlusExpression,
    UnaryExpression,
    thingml_UnaryMinus,
    thingml_NotExpression,
    PropertyReference,
    thingml_DictionaryReference,
    ControlStructure,
    thingml_ConditionalAction,
    thingml_LoopAction,
    Port,
    thingml_RequiredPort,
    Property,
    thingml_Dictionary,
    Event,
    thingml_ReceiveMessage,
    Literal,
    thingml_BooleanLiteral,
    thingml_IntegerLiteral,
    thingml_StringLiteral,
    thingml_DoubleLiteral,
    thingml_EnumLiteralRef,
    thingml_ProvidedPort,
    Region,
    thingml_ParallelRegion,
    State,
    thingml_CompositeState,
    Expression,
    thingml_EventReference,
    thingml_UnaryExpression,
    thingml_ArrayIndex,
    thingml_BinaryExpression,
    thingml_Literal,
    thingml_PropertyReference,
    thingml_ExternExpression,
    Action,
    thingml_VariableAssignment,
    thingml_SendAction,
    thingml_ExternStatement,
    thingml_ActionBlock,
    CompositeState,
    ThingMLElement,
    thingml_AnnotatedElement,
    thingml_PlatformAnnotation,
    Handler,
    thingml_InternalTransition,
    thingml_Transition,
    thingml_Event,
    thingml_StateMachine,
    Type,
    thingml_PrimitiveType,
    thingml_Enumeration,
    thingml_Thing,
    thingml_Expression,
    thingml_TypedElement,
    thingml_ThingMLElement,
    Variable,
    thingml_Property,
    thingml_ThingMLModel,
    thingml_Action,
    thingml_Parameter,
    TypedElement,
    AnnotatedElement,
    thingml_Port,
    thingml_State,
    thingml_Handler,
    thingml_Variable,
    thingml_PropertyAssign,
    thingml_EnumerationLiteral,
    thingml_Region,
    thingml_Message,
    thingml_Function,
    thingml_Configuration,
    thingml_Type,
    thingml_LocalVariable,
    FunctionCall,
    thingml_FunctionCallExpression,
    thingml_FunctionCallStatement,
    thingml_FunctionCall,
    thingml_ConfigPropertyAssign,
    thingml_ConfigInclude,
    thingml_Connector,
    thingml_Instance,
    thingml_ErrorAction,
    thingml_PrintAction,
    thingml_ReturnAction,
    thingml_ExpressionGroup,
    thingml_InstanceRef,
    thingml_ControlStructure,
    thingml_OrExpression,
    thingml_AndExpression,
    thingml_LowerExpression,
    thingml_GreaterExpression,
    thingml_EqualsExpression,
    thingml_ModExpression,
    thingml_DivExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_minusexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_MinusExpression)


def test_thingml_minusexpression_constructor_exists():
    assert callable(thingml_MinusExpression.__init__)


def test_thingml_minusexpression_constructor_args():
    sig = inspect.signature(thingml_MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_timesexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_TimesExpression)


def test_thingml_timesexpression_constructor_exists():
    assert callable(thingml_TimesExpression.__init__)


def test_thingml_timesexpression_constructor_args():
    sig = inspect.signature(thingml_TimesExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_plusexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_PlusExpression)


def test_thingml_plusexpression_constructor_exists():
    assert callable(thingml_PlusExpression.__init__)


def test_thingml_plusexpression_constructor_args():
    sig = inspect.signature(thingml_PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_unaryminus_is_not_abstract():
    assert not inspect.isabstract(thingml_UnaryMinus)


def test_thingml_unaryminus_constructor_exists():
    assert callable(thingml_UnaryMinus.__init__)


def test_thingml_unaryminus_constructor_args():
    sig = inspect.signature(thingml_UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_thingml_notexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_NotExpression)


def test_thingml_notexpression_constructor_exists():
    assert callable(thingml_NotExpression.__init__)


def test_thingml_notexpression_constructor_args():
    sig = inspect.signature(thingml_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_propertyreference_is_not_abstract():
    assert not inspect.isabstract(PropertyReference)


def test_propertyreference_constructor_exists():
    assert callable(PropertyReference.__init__)


def test_propertyreference_constructor_args():
    sig = inspect.signature(PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml_dictionaryreference_is_not_abstract():
    assert not inspect.isabstract(thingml_DictionaryReference)


def test_thingml_dictionaryreference_constructor_exists():
    assert callable(thingml_DictionaryReference.__init__)


def test_thingml_dictionaryreference_constructor_args():
    sig = inspect.signature(thingml_DictionaryReference.__init__)
    params = list(sig.parameters.keys())



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_thingml_conditionalaction_is_not_abstract():
    assert not inspect.isabstract(thingml_ConditionalAction)


def test_thingml_conditionalaction_constructor_exists():
    assert callable(thingml_ConditionalAction.__init__)


def test_thingml_conditionalaction_constructor_args():
    sig = inspect.signature(thingml_ConditionalAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_loopaction_is_not_abstract():
    assert not inspect.isabstract(thingml_LoopAction)


def test_thingml_loopaction_constructor_exists():
    assert callable(thingml_LoopAction.__init__)


def test_thingml_loopaction_constructor_args():
    sig = inspect.signature(thingml_LoopAction.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_thingml_requiredport_is_not_abstract():
    assert not inspect.isabstract(thingml_RequiredPort)


def test_thingml_requiredport_constructor_exists():
    assert callable(thingml_RequiredPort.__init__)


def test_thingml_requiredport_constructor_args():
    sig = inspect.signature(thingml_RequiredPort.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"

def test_thingml_requiredport_has_optional():
    assert hasattr(thingml_RequiredPort, "optional")
    descriptor = None
    for klass in thingml_RequiredPort.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_thingml_dictionary_is_not_abstract():
    assert not inspect.isabstract(thingml_Dictionary)


def test_thingml_dictionary_constructor_exists():
    assert callable(thingml_Dictionary.__init__)


def test_thingml_dictionary_constructor_args():
    sig = inspect.signature(thingml_Dictionary.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_thingml_receivemessage_is_not_abstract():
    assert not inspect.isabstract(thingml_ReceiveMessage)


def test_thingml_receivemessage_constructor_exists():
    assert callable(thingml_ReceiveMessage.__init__)


def test_thingml_receivemessage_constructor_args():
    sig = inspect.signature(thingml_ReceiveMessage.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_thingml_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(thingml_BooleanLiteral)


def test_thingml_booleanliteral_constructor_exists():
    assert callable(thingml_BooleanLiteral.__init__)


def test_thingml_booleanliteral_constructor_args():
    sig = inspect.signature(thingml_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "boolValue" in params, "Missing parameter 'boolValue'"

def test_thingml_booleanliteral_has_boolValue():
    assert hasattr(thingml_BooleanLiteral, "boolValue")
    descriptor = None
    for klass in thingml_BooleanLiteral.__mro__:
        if "boolValue" in klass.__dict__:
            descriptor = klass.__dict__["boolValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_integerliteral_is_not_abstract():
    assert not inspect.isabstract(thingml_IntegerLiteral)


def test_thingml_integerliteral_constructor_exists():
    assert callable(thingml_IntegerLiteral.__init__)


def test_thingml_integerliteral_constructor_args():
    sig = inspect.signature(thingml_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_thingml_integerliteral_has_intValue():
    assert hasattr(thingml_IntegerLiteral, "intValue")
    descriptor = None
    for klass in thingml_IntegerLiteral.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_stringliteral_is_not_abstract():
    assert not inspect.isabstract(thingml_StringLiteral)


def test_thingml_stringliteral_constructor_exists():
    assert callable(thingml_StringLiteral.__init__)


def test_thingml_stringliteral_constructor_args():
    sig = inspect.signature(thingml_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_thingml_stringliteral_has_stringValue():
    assert hasattr(thingml_StringLiteral, "stringValue")
    descriptor = None
    for klass in thingml_StringLiteral.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(thingml_DoubleLiteral)


def test_thingml_doubleliteral_constructor_exists():
    assert callable(thingml_DoubleLiteral.__init__)


def test_thingml_doubleliteral_constructor_args():
    sig = inspect.signature(thingml_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_thingml_doubleliteral_has_doubleValue():
    assert hasattr(thingml_DoubleLiteral, "doubleValue")
    descriptor = None
    for klass in thingml_DoubleLiteral.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_enumliteralref_is_not_abstract():
    assert not inspect.isabstract(thingml_EnumLiteralRef)


def test_thingml_enumliteralref_constructor_exists():
    assert callable(thingml_EnumLiteralRef.__init__)


def test_thingml_enumliteralref_constructor_args():
    sig = inspect.signature(thingml_EnumLiteralRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml_providedport_is_not_abstract():
    assert not inspect.isabstract(thingml_ProvidedPort)


def test_thingml_providedport_constructor_exists():
    assert callable(thingml_ProvidedPort.__init__)


def test_thingml_providedport_constructor_args():
    sig = inspect.signature(thingml_ProvidedPort.__init__)
    params = list(sig.parameters.keys())



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_thingml_parallelregion_is_not_abstract():
    assert not inspect.isabstract(thingml_ParallelRegion)


def test_thingml_parallelregion_constructor_exists():
    assert callable(thingml_ParallelRegion.__init__)


def test_thingml_parallelregion_constructor_args():
    sig = inspect.signature(thingml_ParallelRegion.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_thingml_compositestate_is_not_abstract():
    assert not inspect.isabstract(thingml_CompositeState)


def test_thingml_compositestate_constructor_exists():
    assert callable(thingml_CompositeState.__init__)


def test_thingml_compositestate_constructor_args():
    sig = inspect.signature(thingml_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_eventreference_is_not_abstract():
    assert not inspect.isabstract(thingml_EventReference)


def test_thingml_eventreference_constructor_exists():
    assert callable(thingml_EventReference.__init__)


def test_thingml_eventreference_constructor_args():
    sig = inspect.signature(thingml_EventReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_UnaryExpression)


def test_thingml_unaryexpression_constructor_exists():
    assert callable(thingml_UnaryExpression.__init__)


def test_thingml_unaryexpression_constructor_args():
    sig = inspect.signature(thingml_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_arrayindex_is_not_abstract():
    assert not inspect.isabstract(thingml_ArrayIndex)


def test_thingml_arrayindex_constructor_exists():
    assert callable(thingml_ArrayIndex.__init__)


def test_thingml_arrayindex_constructor_args():
    sig = inspect.signature(thingml_ArrayIndex.__init__)
    params = list(sig.parameters.keys())



def test_thingml_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_BinaryExpression)


def test_thingml_binaryexpression_constructor_exists():
    assert callable(thingml_BinaryExpression.__init__)


def test_thingml_binaryexpression_constructor_args():
    sig = inspect.signature(thingml_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_literal_is_not_abstract():
    assert not inspect.isabstract(thingml_Literal)


def test_thingml_literal_constructor_exists():
    assert callable(thingml_Literal.__init__)


def test_thingml_literal_constructor_args():
    sig = inspect.signature(thingml_Literal.__init__)
    params = list(sig.parameters.keys())



def test_thingml_propertyreference_is_not_abstract():
    assert not inspect.isabstract(thingml_PropertyReference)


def test_thingml_propertyreference_constructor_exists():
    assert callable(thingml_PropertyReference.__init__)


def test_thingml_propertyreference_constructor_args():
    sig = inspect.signature(thingml_PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml_externexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_ExternExpression)


def test_thingml_externexpression_constructor_exists():
    assert callable(thingml_ExternExpression.__init__)


def test_thingml_externexpression_constructor_args():
    sig = inspect.signature(thingml_ExternExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_thingml_externexpression_has_expression():
    assert hasattr(thingml_ExternExpression, "expression")
    descriptor = None
    for klass in thingml_ExternExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_thingml_variableassignment_is_not_abstract():
    assert not inspect.isabstract(thingml_VariableAssignment)


def test_thingml_variableassignment_constructor_exists():
    assert callable(thingml_VariableAssignment.__init__)


def test_thingml_variableassignment_constructor_args():
    sig = inspect.signature(thingml_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_thingml_sendaction_is_not_abstract():
    assert not inspect.isabstract(thingml_SendAction)


def test_thingml_sendaction_constructor_exists():
    assert callable(thingml_SendAction.__init__)


def test_thingml_sendaction_constructor_args():
    sig = inspect.signature(thingml_SendAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_externstatement_is_not_abstract():
    assert not inspect.isabstract(thingml_ExternStatement)


def test_thingml_externstatement_constructor_exists():
    assert callable(thingml_ExternStatement.__init__)


def test_thingml_externstatement_constructor_args():
    sig = inspect.signature(thingml_ExternStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statement" in params, "Missing parameter 'statement'"

def test_thingml_externstatement_has_statement():
    assert hasattr(thingml_ExternStatement, "statement")
    descriptor = None
    for klass in thingml_ExternStatement.__mro__:
        if "statement" in klass.__dict__:
            descriptor = klass.__dict__["statement"]
            break
    assert isinstance(descriptor, property)



def test_thingml_actionblock_is_not_abstract():
    assert not inspect.isabstract(thingml_ActionBlock)


def test_thingml_actionblock_constructor_exists():
    assert callable(thingml_ActionBlock.__init__)


def test_thingml_actionblock_constructor_args():
    sig = inspect.signature(thingml_ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_thingmlelement_is_not_abstract():
    assert not inspect.isabstract(ThingMLElement)


def test_thingmlelement_constructor_exists():
    assert callable(ThingMLElement.__init__)


def test_thingmlelement_constructor_args():
    sig = inspect.signature(ThingMLElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(thingml_AnnotatedElement)


def test_thingml_annotatedelement_constructor_exists():
    assert callable(thingml_AnnotatedElement.__init__)


def test_thingml_annotatedelement_constructor_args():
    sig = inspect.signature(thingml_AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_platformannotation_is_not_abstract():
    assert not inspect.isabstract(thingml_PlatformAnnotation)


def test_thingml_platformannotation_constructor_exists():
    assert callable(thingml_PlatformAnnotation.__init__)


def test_thingml_platformannotation_constructor_args():
    sig = inspect.signature(thingml_PlatformAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_thingml_platformannotation_has_value():
    assert hasattr(thingml_PlatformAnnotation, "value")
    descriptor = None
    for klass in thingml_PlatformAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_handler_is_not_abstract():
    assert not inspect.isabstract(Handler)


def test_handler_constructor_exists():
    assert callable(Handler.__init__)


def test_handler_constructor_args():
    sig = inspect.signature(Handler.__init__)
    params = list(sig.parameters.keys())



def test_thingml_internaltransition_is_not_abstract():
    assert not inspect.isabstract(thingml_InternalTransition)


def test_thingml_internaltransition_constructor_exists():
    assert callable(thingml_InternalTransition.__init__)


def test_thingml_internaltransition_constructor_args():
    sig = inspect.signature(thingml_InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_thingml_transition_is_not_abstract():
    assert not inspect.isabstract(thingml_Transition)


def test_thingml_transition_constructor_exists():
    assert callable(thingml_Transition.__init__)


def test_thingml_transition_constructor_args():
    sig = inspect.signature(thingml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_thingml_event_is_not_abstract():
    assert not inspect.isabstract(thingml_Event)


def test_thingml_event_constructor_exists():
    assert callable(thingml_Event.__init__)


def test_thingml_event_constructor_args():
    sig = inspect.signature(thingml_Event.__init__)
    params = list(sig.parameters.keys())



def test_thingml_statemachine_is_not_abstract():
    assert not inspect.isabstract(thingml_StateMachine)


def test_thingml_statemachine_constructor_exists():
    assert callable(thingml_StateMachine.__init__)


def test_thingml_statemachine_constructor_args():
    sig = inspect.signature(thingml_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_thingml_primitivetype_is_not_abstract():
    assert not inspect.isabstract(thingml_PrimitiveType)


def test_thingml_primitivetype_constructor_exists():
    assert callable(thingml_PrimitiveType.__init__)


def test_thingml_primitivetype_constructor_args():
    sig = inspect.signature(thingml_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_thingml_enumeration_is_not_abstract():
    assert not inspect.isabstract(thingml_Enumeration)


def test_thingml_enumeration_constructor_exists():
    assert callable(thingml_Enumeration.__init__)


def test_thingml_enumeration_constructor_args():
    sig = inspect.signature(thingml_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_thingml_thing_is_not_abstract():
    assert not inspect.isabstract(thingml_Thing)


def test_thingml_thing_constructor_exists():
    assert callable(thingml_Thing.__init__)


def test_thingml_thing_constructor_args():
    sig = inspect.signature(thingml_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_thingml_thing_has_fragment():
    assert hasattr(thingml_Thing, "fragment")
    descriptor = None
    for klass in thingml_Thing.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_thingml_expression_is_not_abstract():
    assert not inspect.isabstract(thingml_Expression)


def test_thingml_expression_constructor_exists():
    assert callable(thingml_Expression.__init__)


def test_thingml_expression_constructor_args():
    sig = inspect.signature(thingml_Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_typedelement_is_not_abstract():
    assert not inspect.isabstract(thingml_TypedElement)


def test_thingml_typedelement_constructor_exists():
    assert callable(thingml_TypedElement.__init__)


def test_thingml_typedelement_constructor_args():
    sig = inspect.signature(thingml_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_thingmlelement_is_not_abstract():
    assert not inspect.isabstract(thingml_ThingMLElement)


def test_thingml_thingmlelement_constructor_exists():
    assert callable(thingml_ThingMLElement.__init__)


def test_thingml_thingmlelement_constructor_args():
    sig = inspect.signature(thingml_ThingMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_thingmlelement_has_name():
    assert hasattr(thingml_ThingMLElement, "name")
    descriptor = None
    for klass in thingml_ThingMLElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_thingml_property_is_not_abstract():
    assert not inspect.isabstract(thingml_Property)


def test_thingml_property_constructor_exists():
    assert callable(thingml_Property.__init__)


def test_thingml_property_constructor_args():
    sig = inspect.signature(thingml_Property.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_thingml_property_has_changeable():
    assert hasattr(thingml_Property, "changeable")
    descriptor = None
    for klass in thingml_Property.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_thingml_thingmlmodel_is_not_abstract():
    assert not inspect.isabstract(thingml_ThingMLModel)


def test_thingml_thingmlmodel_constructor_exists():
    assert callable(thingml_ThingMLModel.__init__)


def test_thingml_thingmlmodel_constructor_args():
    sig = inspect.signature(thingml_ThingMLModel.__init__)
    params = list(sig.parameters.keys())



def test_thingml_action_is_not_abstract():
    assert not inspect.isabstract(thingml_Action)


def test_thingml_action_constructor_exists():
    assert callable(thingml_Action.__init__)


def test_thingml_action_constructor_args():
    sig = inspect.signature(thingml_Action.__init__)
    params = list(sig.parameters.keys())



def test_thingml_parameter_is_not_abstract():
    assert not inspect.isabstract(thingml_Parameter)


def test_thingml_parameter_constructor_exists():
    assert callable(thingml_Parameter.__init__)


def test_thingml_parameter_constructor_args():
    sig = inspect.signature(thingml_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_port_is_not_abstract():
    assert not inspect.isabstract(thingml_Port)


def test_thingml_port_constructor_exists():
    assert callable(thingml_Port.__init__)


def test_thingml_port_constructor_args():
    sig = inspect.signature(thingml_Port.__init__)
    params = list(sig.parameters.keys())



def test_thingml_state_is_not_abstract():
    assert not inspect.isabstract(thingml_State)


def test_thingml_state_constructor_exists():
    assert callable(thingml_State.__init__)


def test_thingml_state_constructor_args():
    sig = inspect.signature(thingml_State.__init__)
    params = list(sig.parameters.keys())



def test_thingml_handler_is_not_abstract():
    assert not inspect.isabstract(thingml_Handler)


def test_thingml_handler_constructor_exists():
    assert callable(thingml_Handler.__init__)


def test_thingml_handler_constructor_args():
    sig = inspect.signature(thingml_Handler.__init__)
    params = list(sig.parameters.keys())



def test_thingml_variable_is_not_abstract():
    assert not inspect.isabstract(thingml_Variable)


def test_thingml_variable_constructor_exists():
    assert callable(thingml_Variable.__init__)


def test_thingml_variable_constructor_args():
    sig = inspect.signature(thingml_Variable.__init__)
    params = list(sig.parameters.keys())



def test_thingml_propertyassign_is_not_abstract():
    assert not inspect.isabstract(thingml_PropertyAssign)


def test_thingml_propertyassign_constructor_exists():
    assert callable(thingml_PropertyAssign.__init__)


def test_thingml_propertyassign_constructor_args():
    sig = inspect.signature(thingml_PropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_thingml_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(thingml_EnumerationLiteral)


def test_thingml_enumerationliteral_constructor_exists():
    assert callable(thingml_EnumerationLiteral.__init__)


def test_thingml_enumerationliteral_constructor_args():
    sig = inspect.signature(thingml_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_thingml_region_is_not_abstract():
    assert not inspect.isabstract(thingml_Region)


def test_thingml_region_constructor_exists():
    assert callable(thingml_Region.__init__)


def test_thingml_region_constructor_args():
    sig = inspect.signature(thingml_Region.__init__)
    params = list(sig.parameters.keys())
    assert "history" in params, "Missing parameter 'history'"

def test_thingml_region_has_history():
    assert hasattr(thingml_Region, "history")
    descriptor = None
    for klass in thingml_Region.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
            break
    assert isinstance(descriptor, property)



def test_thingml_message_is_not_abstract():
    assert not inspect.isabstract(thingml_Message)


def test_thingml_message_constructor_exists():
    assert callable(thingml_Message.__init__)


def test_thingml_message_constructor_args():
    sig = inspect.signature(thingml_Message.__init__)
    params = list(sig.parameters.keys())



def test_thingml_function_is_not_abstract():
    assert not inspect.isabstract(thingml_Function)


def test_thingml_function_constructor_exists():
    assert callable(thingml_Function.__init__)


def test_thingml_function_constructor_args():
    sig = inspect.signature(thingml_Function.__init__)
    params = list(sig.parameters.keys())



def test_thingml_configuration_is_not_abstract():
    assert not inspect.isabstract(thingml_Configuration)


def test_thingml_configuration_constructor_exists():
    assert callable(thingml_Configuration.__init__)


def test_thingml_configuration_constructor_args():
    sig = inspect.signature(thingml_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_thingml_configuration_has_fragment():
    assert hasattr(thingml_Configuration, "fragment")
    descriptor = None
    for klass in thingml_Configuration.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_thingml_type_is_not_abstract():
    assert not inspect.isabstract(thingml_Type)


def test_thingml_type_constructor_exists():
    assert callable(thingml_Type.__init__)


def test_thingml_type_constructor_args():
    sig = inspect.signature(thingml_Type.__init__)
    params = list(sig.parameters.keys())



def test_thingml_localvariable_is_not_abstract():
    assert not inspect.isabstract(thingml_LocalVariable)


def test_thingml_localvariable_constructor_exists():
    assert callable(thingml_LocalVariable.__init__)


def test_thingml_localvariable_constructor_args():
    sig = inspect.signature(thingml_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_thingml_localvariable_has_changeable():
    assert hasattr(thingml_LocalVariable, "changeable")
    descriptor = None
    for klass in thingml_LocalVariable.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_functioncall_is_not_abstract():
    assert not inspect.isabstract(FunctionCall)


def test_functioncall_constructor_exists():
    assert callable(FunctionCall.__init__)


def test_functioncall_constructor_args():
    sig = inspect.signature(FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_thingml_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_FunctionCallExpression)


def test_thingml_functioncallexpression_constructor_exists():
    assert callable(thingml_FunctionCallExpression.__init__)


def test_thingml_functioncallexpression_constructor_args():
    sig = inspect.signature(thingml_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(thingml_FunctionCallStatement)


def test_thingml_functioncallstatement_constructor_exists():
    assert callable(thingml_FunctionCallStatement.__init__)


def test_thingml_functioncallstatement_constructor_args():
    sig = inspect.signature(thingml_FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_functioncall_is_not_abstract():
    assert not inspect.isabstract(thingml_FunctionCall)


def test_thingml_functioncall_constructor_exists():
    assert callable(thingml_FunctionCall.__init__)


def test_thingml_functioncall_constructor_args():
    sig = inspect.signature(thingml_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_thingml_configpropertyassign_is_not_abstract():
    assert not inspect.isabstract(thingml_ConfigPropertyAssign)


def test_thingml_configpropertyassign_constructor_exists():
    assert callable(thingml_ConfigPropertyAssign.__init__)


def test_thingml_configpropertyassign_constructor_args():
    sig = inspect.signature(thingml_ConfigPropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_thingml_configinclude_is_not_abstract():
    assert not inspect.isabstract(thingml_ConfigInclude)


def test_thingml_configinclude_constructor_exists():
    assert callable(thingml_ConfigInclude.__init__)


def test_thingml_configinclude_constructor_args():
    sig = inspect.signature(thingml_ConfigInclude.__init__)
    params = list(sig.parameters.keys())



def test_thingml_connector_is_not_abstract():
    assert not inspect.isabstract(thingml_Connector)


def test_thingml_connector_constructor_exists():
    assert callable(thingml_Connector.__init__)


def test_thingml_connector_constructor_args():
    sig = inspect.signature(thingml_Connector.__init__)
    params = list(sig.parameters.keys())



def test_thingml_instance_is_not_abstract():
    assert not inspect.isabstract(thingml_Instance)


def test_thingml_instance_constructor_exists():
    assert callable(thingml_Instance.__init__)


def test_thingml_instance_constructor_args():
    sig = inspect.signature(thingml_Instance.__init__)
    params = list(sig.parameters.keys())



def test_thingml_erroraction_is_not_abstract():
    assert not inspect.isabstract(thingml_ErrorAction)


def test_thingml_erroraction_constructor_exists():
    assert callable(thingml_ErrorAction.__init__)


def test_thingml_erroraction_constructor_args():
    sig = inspect.signature(thingml_ErrorAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_printaction_is_not_abstract():
    assert not inspect.isabstract(thingml_PrintAction)


def test_thingml_printaction_constructor_exists():
    assert callable(thingml_PrintAction.__init__)


def test_thingml_printaction_constructor_args():
    sig = inspect.signature(thingml_PrintAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_returnaction_is_not_abstract():
    assert not inspect.isabstract(thingml_ReturnAction)


def test_thingml_returnaction_constructor_exists():
    assert callable(thingml_ReturnAction.__init__)


def test_thingml_returnaction_constructor_args():
    sig = inspect.signature(thingml_ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_expressiongroup_is_not_abstract():
    assert not inspect.isabstract(thingml_ExpressionGroup)


def test_thingml_expressiongroup_constructor_exists():
    assert callable(thingml_ExpressionGroup.__init__)


def test_thingml_expressiongroup_constructor_args():
    sig = inspect.signature(thingml_ExpressionGroup.__init__)
    params = list(sig.parameters.keys())



def test_thingml_instanceref_is_not_abstract():
    assert not inspect.isabstract(thingml_InstanceRef)


def test_thingml_instanceref_constructor_exists():
    assert callable(thingml_InstanceRef.__init__)


def test_thingml_instanceref_constructor_args():
    sig = inspect.signature(thingml_InstanceRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml_controlstructure_is_not_abstract():
    assert not inspect.isabstract(thingml_ControlStructure)


def test_thingml_controlstructure_constructor_exists():
    assert callable(thingml_ControlStructure.__init__)


def test_thingml_controlstructure_constructor_args():
    sig = inspect.signature(thingml_ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_thingml_orexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_OrExpression)


def test_thingml_orexpression_constructor_exists():
    assert callable(thingml_OrExpression.__init__)


def test_thingml_orexpression_constructor_args():
    sig = inspect.signature(thingml_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_andexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_AndExpression)


def test_thingml_andexpression_constructor_exists():
    assert callable(thingml_AndExpression.__init__)


def test_thingml_andexpression_constructor_args():
    sig = inspect.signature(thingml_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_lowerexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_LowerExpression)


def test_thingml_lowerexpression_constructor_exists():
    assert callable(thingml_LowerExpression.__init__)


def test_thingml_lowerexpression_constructor_args():
    sig = inspect.signature(thingml_LowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_greaterexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_GreaterExpression)


def test_thingml_greaterexpression_constructor_exists():
    assert callable(thingml_GreaterExpression.__init__)


def test_thingml_greaterexpression_constructor_args():
    sig = inspect.signature(thingml_GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_equalsexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_EqualsExpression)


def test_thingml_equalsexpression_constructor_exists():
    assert callable(thingml_EqualsExpression.__init__)


def test_thingml_equalsexpression_constructor_args():
    sig = inspect.signature(thingml_EqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_modexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_ModExpression)


def test_thingml_modexpression_constructor_exists():
    assert callable(thingml_ModExpression.__init__)


def test_thingml_modexpression_constructor_args():
    sig = inspect.signature(thingml_ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_divexpression_is_not_abstract():
    assert not inspect.isabstract(thingml_DivExpression)


def test_thingml_divexpression_constructor_exists():
    assert callable(thingml_DivExpression.__init__)


def test_thingml_divexpression_constructor_args():
    sig = inspect.signature(thingml_DivExpression.__init__)
    params = list(sig.parameters.keys())


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
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
thingml_MinusExpression_strategy = st.builds(
    thingml_MinusExpression,
)
thingml_TimesExpression_strategy = st.builds(
    thingml_TimesExpression,
)
thingml_PlusExpression_strategy = st.builds(
    thingml_PlusExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
thingml_UnaryMinus_strategy = st.builds(
    thingml_UnaryMinus,
)
thingml_NotExpression_strategy = st.builds(
    thingml_NotExpression,
)
PropertyReference_strategy = st.builds(
    PropertyReference,
)
thingml_DictionaryReference_strategy = st.builds(
    thingml_DictionaryReference,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
thingml_ConditionalAction_strategy = st.builds(
    thingml_ConditionalAction,
)
thingml_LoopAction_strategy = st.builds(
    thingml_LoopAction,
)
Port_strategy = st.builds(
    Port,
)
thingml_RequiredPort_strategy = st.builds(
    thingml_RequiredPort,
    optional=
        st.booleans()
)
Property_strategy = st.builds(
    Property,
)
thingml_Dictionary_strategy = st.builds(
    thingml_Dictionary,
)
Event_strategy = st.builds(
    Event,
)
thingml_ReceiveMessage_strategy = st.builds(
    thingml_ReceiveMessage,
)
Literal_strategy = st.builds(
    Literal,
)
thingml_BooleanLiteral_strategy = st.builds(
    thingml_BooleanLiteral,
    boolValue=
        st.booleans()
)
thingml_IntegerLiteral_strategy = st.builds(
    thingml_IntegerLiteral,
    intValue=
        st.integers()
)
thingml_StringLiteral_strategy = st.builds(
    thingml_StringLiteral,
    stringValue=
        safe_text
)
thingml_DoubleLiteral_strategy = st.builds(
    thingml_DoubleLiteral,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
thingml_EnumLiteralRef_strategy = st.builds(
    thingml_EnumLiteralRef,
)
thingml_ProvidedPort_strategy = st.builds(
    thingml_ProvidedPort,
)
Region_strategy = st.builds(
    Region,
)
thingml_ParallelRegion_strategy = st.builds(
    thingml_ParallelRegion,
)
State_strategy = st.builds(
    State,
)
thingml_CompositeState_strategy = st.builds(
    thingml_CompositeState,
)
Expression_strategy = st.builds(
    Expression,
)
thingml_EventReference_strategy = st.builds(
    thingml_EventReference,
)
thingml_UnaryExpression_strategy = st.builds(
    thingml_UnaryExpression,
)
thingml_ArrayIndex_strategy = st.builds(
    thingml_ArrayIndex,
)
thingml_BinaryExpression_strategy = st.builds(
    thingml_BinaryExpression,
)
thingml_Literal_strategy = st.builds(
    thingml_Literal,
)
thingml_PropertyReference_strategy = st.builds(
    thingml_PropertyReference,
)
thingml_ExternExpression_strategy = st.builds(
    thingml_ExternExpression,
    expression=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
thingml_VariableAssignment_strategy = st.builds(
    thingml_VariableAssignment,
)
thingml_SendAction_strategy = st.builds(
    thingml_SendAction,
)
thingml_ExternStatement_strategy = st.builds(
    thingml_ExternStatement,
    statement=
        safe_text
)
thingml_ActionBlock_strategy = st.builds(
    thingml_ActionBlock,
)
CompositeState_strategy = st.builds(
    CompositeState,
)
ThingMLElement_strategy = st.builds(
    ThingMLElement,
)
thingml_AnnotatedElement_strategy = st.builds(
    thingml_AnnotatedElement,
)
thingml_PlatformAnnotation_strategy = st.builds(
    thingml_PlatformAnnotation,
    value=
        safe_text
)
Handler_strategy = st.builds(
    Handler,
)
thingml_InternalTransition_strategy = st.builds(
    thingml_InternalTransition,
)
thingml_Transition_strategy = st.builds(
    thingml_Transition,
)
thingml_Event_strategy = st.builds(
    thingml_Event,
)
thingml_StateMachine_strategy = st.builds(
    thingml_StateMachine,
)
Type_strategy = st.builds(
    Type,
)
thingml_PrimitiveType_strategy = st.builds(
    thingml_PrimitiveType,
)
thingml_Enumeration_strategy = st.builds(
    thingml_Enumeration,
)
thingml_Thing_strategy = st.builds(
    thingml_Thing,
    fragment=
        st.booleans()
)
thingml_Expression_strategy = st.builds(
    thingml_Expression,
)
thingml_TypedElement_strategy = st.builds(
    thingml_TypedElement,
)
thingml_ThingMLElement_strategy = st.builds(
    thingml_ThingMLElement,
    name=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
thingml_Property_strategy = st.builds(
    thingml_Property,
    changeable=
        st.booleans()
)
thingml_ThingMLModel_strategy = st.builds(
    thingml_ThingMLModel,
)
thingml_Action_strategy = st.builds(
    thingml_Action,
)
thingml_Parameter_strategy = st.builds(
    thingml_Parameter,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
thingml_Port_strategy = st.builds(
    thingml_Port,
)
thingml_State_strategy = st.builds(
    thingml_State,
)
thingml_Handler_strategy = st.builds(
    thingml_Handler,
)
thingml_Variable_strategy = st.builds(
    thingml_Variable,
)
thingml_PropertyAssign_strategy = st.builds(
    thingml_PropertyAssign,
)
thingml_EnumerationLiteral_strategy = st.builds(
    thingml_EnumerationLiteral,
)
thingml_Region_strategy = st.builds(
    thingml_Region,
    history=
        st.booleans()
)
thingml_Message_strategy = st.builds(
    thingml_Message,
)
thingml_Function_strategy = st.builds(
    thingml_Function,
)
thingml_Configuration_strategy = st.builds(
    thingml_Configuration,
    fragment=
        st.booleans()
)
thingml_Type_strategy = st.builds(
    thingml_Type,
)
thingml_LocalVariable_strategy = st.builds(
    thingml_LocalVariable,
    changeable=
        st.booleans()
)
FunctionCall_strategy = st.builds(
    FunctionCall,
)
thingml_FunctionCallExpression_strategy = st.builds(
    thingml_FunctionCallExpression,
)
thingml_FunctionCallStatement_strategy = st.builds(
    thingml_FunctionCallStatement,
)
thingml_FunctionCall_strategy = st.builds(
    thingml_FunctionCall,
)
thingml_ConfigPropertyAssign_strategy = st.builds(
    thingml_ConfigPropertyAssign,
)
thingml_ConfigInclude_strategy = st.builds(
    thingml_ConfigInclude,
)
thingml_Connector_strategy = st.builds(
    thingml_Connector,
)
thingml_Instance_strategy = st.builds(
    thingml_Instance,
)
thingml_ErrorAction_strategy = st.builds(
    thingml_ErrorAction,
)
thingml_PrintAction_strategy = st.builds(
    thingml_PrintAction,
)
thingml_ReturnAction_strategy = st.builds(
    thingml_ReturnAction,
)
thingml_ExpressionGroup_strategy = st.builds(
    thingml_ExpressionGroup,
)
thingml_InstanceRef_strategy = st.builds(
    thingml_InstanceRef,
)
thingml_ControlStructure_strategy = st.builds(
    thingml_ControlStructure,
)
thingml_OrExpression_strategy = st.builds(
    thingml_OrExpression,
)
thingml_AndExpression_strategy = st.builds(
    thingml_AndExpression,
)
thingml_LowerExpression_strategy = st.builds(
    thingml_LowerExpression,
)
thingml_GreaterExpression_strategy = st.builds(
    thingml_GreaterExpression,
)
thingml_EqualsExpression_strategy = st.builds(
    thingml_EqualsExpression,
)
thingml_ModExpression_strategy = st.builds(
    thingml_ModExpression,
)
thingml_DivExpression_strategy = st.builds(
    thingml_DivExpression,
)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=thingml_MinusExpression_strategy)
@settings(max_examples=50)
def test_thingml_minusexpression_instantiation(instance):
    assert isinstance(instance, thingml_MinusExpression)

@given(instance=thingml_TimesExpression_strategy)
@settings(max_examples=50)
def test_thingml_timesexpression_instantiation(instance):
    assert isinstance(instance, thingml_TimesExpression)

@given(instance=thingml_PlusExpression_strategy)
@settings(max_examples=50)
def test_thingml_plusexpression_instantiation(instance):
    assert isinstance(instance, thingml_PlusExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=thingml_UnaryMinus_strategy)
@settings(max_examples=50)
def test_thingml_unaryminus_instantiation(instance):
    assert isinstance(instance, thingml_UnaryMinus)

@given(instance=thingml_NotExpression_strategy)
@settings(max_examples=50)
def test_thingml_notexpression_instantiation(instance):
    assert isinstance(instance, thingml_NotExpression)

@given(instance=PropertyReference_strategy)
@settings(max_examples=50)
def test_propertyreference_instantiation(instance):
    assert isinstance(instance, PropertyReference)

@given(instance=thingml_DictionaryReference_strategy)
@settings(max_examples=50)
def test_thingml_dictionaryreference_instantiation(instance):
    assert isinstance(instance, thingml_DictionaryReference)

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=thingml_ConditionalAction_strategy)
@settings(max_examples=50)
def test_thingml_conditionalaction_instantiation(instance):
    assert isinstance(instance, thingml_ConditionalAction)

@given(instance=thingml_LoopAction_strategy)
@settings(max_examples=50)
def test_thingml_loopaction_instantiation(instance):
    assert isinstance(instance, thingml_LoopAction)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=thingml_RequiredPort_strategy)
@settings(max_examples=50)
def test_thingml_requiredport_instantiation(instance):
    assert isinstance(instance, thingml_RequiredPort)



@given(instance=thingml_RequiredPort_strategy)
def test_thingml_requiredport_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=thingml_Dictionary_strategy)
@settings(max_examples=50)
def test_thingml_dictionary_instantiation(instance):
    assert isinstance(instance, thingml_Dictionary)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=thingml_ReceiveMessage_strategy)
@settings(max_examples=50)
def test_thingml_receivemessage_instantiation(instance):
    assert isinstance(instance, thingml_ReceiveMessage)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=thingml_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_thingml_booleanliteral_instantiation(instance):
    assert isinstance(instance, thingml_BooleanLiteral)



@given(instance=thingml_BooleanLiteral_strategy)
def test_thingml_booleanliteral_boolValue_setter(instance):
    original = instance.boolValue
    instance.boolValue = original
    assert instance.boolValue == original

@given(instance=thingml_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_thingml_integerliteral_instantiation(instance):
    assert isinstance(instance, thingml_IntegerLiteral)



@given(instance=thingml_IntegerLiteral_strategy)
def test_thingml_integerliteral_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=thingml_StringLiteral_strategy)
@settings(max_examples=50)
def test_thingml_stringliteral_instantiation(instance):
    assert isinstance(instance, thingml_StringLiteral)



@given(instance=thingml_StringLiteral_strategy)
def test_thingml_stringliteral_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=thingml_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_thingml_doubleliteral_instantiation(instance):
    assert isinstance(instance, thingml_DoubleLiteral)



@given(instance=thingml_DoubleLiteral_strategy)
def test_thingml_doubleliteral_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=thingml_EnumLiteralRef_strategy)
@settings(max_examples=50)
def test_thingml_enumliteralref_instantiation(instance):
    assert isinstance(instance, thingml_EnumLiteralRef)

@given(instance=thingml_ProvidedPort_strategy)
@settings(max_examples=50)
def test_thingml_providedport_instantiation(instance):
    assert isinstance(instance, thingml_ProvidedPort)

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=thingml_ParallelRegion_strategy)
@settings(max_examples=50)
def test_thingml_parallelregion_instantiation(instance):
    assert isinstance(instance, thingml_ParallelRegion)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=thingml_CompositeState_strategy)
@settings(max_examples=50)
def test_thingml_compositestate_instantiation(instance):
    assert isinstance(instance, thingml_CompositeState)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=thingml_EventReference_strategy)
@settings(max_examples=50)
def test_thingml_eventreference_instantiation(instance):
    assert isinstance(instance, thingml_EventReference)

@given(instance=thingml_UnaryExpression_strategy)
@settings(max_examples=50)
def test_thingml_unaryexpression_instantiation(instance):
    assert isinstance(instance, thingml_UnaryExpression)

@given(instance=thingml_ArrayIndex_strategy)
@settings(max_examples=50)
def test_thingml_arrayindex_instantiation(instance):
    assert isinstance(instance, thingml_ArrayIndex)

@given(instance=thingml_BinaryExpression_strategy)
@settings(max_examples=50)
def test_thingml_binaryexpression_instantiation(instance):
    assert isinstance(instance, thingml_BinaryExpression)

@given(instance=thingml_Literal_strategy)
@settings(max_examples=50)
def test_thingml_literal_instantiation(instance):
    assert isinstance(instance, thingml_Literal)

@given(instance=thingml_PropertyReference_strategy)
@settings(max_examples=50)
def test_thingml_propertyreference_instantiation(instance):
    assert isinstance(instance, thingml_PropertyReference)

@given(instance=thingml_ExternExpression_strategy)
@settings(max_examples=50)
def test_thingml_externexpression_instantiation(instance):
    assert isinstance(instance, thingml_ExternExpression)



@given(instance=thingml_ExternExpression_strategy)
def test_thingml_externexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=thingml_VariableAssignment_strategy)
@settings(max_examples=50)
def test_thingml_variableassignment_instantiation(instance):
    assert isinstance(instance, thingml_VariableAssignment)

@given(instance=thingml_SendAction_strategy)
@settings(max_examples=50)
def test_thingml_sendaction_instantiation(instance):
    assert isinstance(instance, thingml_SendAction)

@given(instance=thingml_ExternStatement_strategy)
@settings(max_examples=50)
def test_thingml_externstatement_instantiation(instance):
    assert isinstance(instance, thingml_ExternStatement)



@given(instance=thingml_ExternStatement_strategy)
def test_thingml_externstatement_statement_setter(instance):
    original = instance.statement
    instance.statement = original
    assert instance.statement == original

@given(instance=thingml_ActionBlock_strategy)
@settings(max_examples=50)
def test_thingml_actionblock_instantiation(instance):
    assert isinstance(instance, thingml_ActionBlock)

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=ThingMLElement_strategy)
@settings(max_examples=50)
def test_thingmlelement_instantiation(instance):
    assert isinstance(instance, ThingMLElement)

@given(instance=thingml_AnnotatedElement_strategy)
@settings(max_examples=50)
def test_thingml_annotatedelement_instantiation(instance):
    assert isinstance(instance, thingml_AnnotatedElement)

@given(instance=thingml_PlatformAnnotation_strategy)
@settings(max_examples=50)
def test_thingml_platformannotation_instantiation(instance):
    assert isinstance(instance, thingml_PlatformAnnotation)



@given(instance=thingml_PlatformAnnotation_strategy)
def test_thingml_platformannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Handler_strategy)
@settings(max_examples=50)
def test_handler_instantiation(instance):
    assert isinstance(instance, Handler)

@given(instance=thingml_InternalTransition_strategy)
@settings(max_examples=50)
def test_thingml_internaltransition_instantiation(instance):
    assert isinstance(instance, thingml_InternalTransition)

@given(instance=thingml_Transition_strategy)
@settings(max_examples=50)
def test_thingml_transition_instantiation(instance):
    assert isinstance(instance, thingml_Transition)

@given(instance=thingml_Event_strategy)
@settings(max_examples=50)
def test_thingml_event_instantiation(instance):
    assert isinstance(instance, thingml_Event)

@given(instance=thingml_StateMachine_strategy)
@settings(max_examples=50)
def test_thingml_statemachine_instantiation(instance):
    assert isinstance(instance, thingml_StateMachine)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=thingml_PrimitiveType_strategy)
@settings(max_examples=50)
def test_thingml_primitivetype_instantiation(instance):
    assert isinstance(instance, thingml_PrimitiveType)

@given(instance=thingml_Enumeration_strategy)
@settings(max_examples=50)
def test_thingml_enumeration_instantiation(instance):
    assert isinstance(instance, thingml_Enumeration)

@given(instance=thingml_Thing_strategy)
@settings(max_examples=50)
def test_thingml_thing_instantiation(instance):
    assert isinstance(instance, thingml_Thing)



@given(instance=thingml_Thing_strategy)
def test_thingml_thing_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=thingml_Expression_strategy)
@settings(max_examples=50)
def test_thingml_expression_instantiation(instance):
    assert isinstance(instance, thingml_Expression)

@given(instance=thingml_TypedElement_strategy)
@settings(max_examples=50)
def test_thingml_typedelement_instantiation(instance):
    assert isinstance(instance, thingml_TypedElement)

@given(instance=thingml_ThingMLElement_strategy)
@settings(max_examples=50)
def test_thingml_thingmlelement_instantiation(instance):
    assert isinstance(instance, thingml_ThingMLElement)



@given(instance=thingml_ThingMLElement_strategy)
def test_thingml_thingmlelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=thingml_Property_strategy)
@settings(max_examples=50)
def test_thingml_property_instantiation(instance):
    assert isinstance(instance, thingml_Property)



@given(instance=thingml_Property_strategy)
def test_thingml_property_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=thingml_ThingMLModel_strategy)
@settings(max_examples=50)
def test_thingml_thingmlmodel_instantiation(instance):
    assert isinstance(instance, thingml_ThingMLModel)

@given(instance=thingml_Action_strategy)
@settings(max_examples=50)
def test_thingml_action_instantiation(instance):
    assert isinstance(instance, thingml_Action)

@given(instance=thingml_Parameter_strategy)
@settings(max_examples=50)
def test_thingml_parameter_instantiation(instance):
    assert isinstance(instance, thingml_Parameter)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=thingml_Port_strategy)
@settings(max_examples=50)
def test_thingml_port_instantiation(instance):
    assert isinstance(instance, thingml_Port)

@given(instance=thingml_State_strategy)
@settings(max_examples=50)
def test_thingml_state_instantiation(instance):
    assert isinstance(instance, thingml_State)

@given(instance=thingml_Handler_strategy)
@settings(max_examples=50)
def test_thingml_handler_instantiation(instance):
    assert isinstance(instance, thingml_Handler)

@given(instance=thingml_Variable_strategy)
@settings(max_examples=50)
def test_thingml_variable_instantiation(instance):
    assert isinstance(instance, thingml_Variable)

@given(instance=thingml_PropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml_propertyassign_instantiation(instance):
    assert isinstance(instance, thingml_PropertyAssign)

@given(instance=thingml_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_thingml_enumerationliteral_instantiation(instance):
    assert isinstance(instance, thingml_EnumerationLiteral)

@given(instance=thingml_Region_strategy)
@settings(max_examples=50)
def test_thingml_region_instantiation(instance):
    assert isinstance(instance, thingml_Region)



@given(instance=thingml_Region_strategy)
def test_thingml_region_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original

@given(instance=thingml_Message_strategy)
@settings(max_examples=50)
def test_thingml_message_instantiation(instance):
    assert isinstance(instance, thingml_Message)

@given(instance=thingml_Function_strategy)
@settings(max_examples=50)
def test_thingml_function_instantiation(instance):
    assert isinstance(instance, thingml_Function)

@given(instance=thingml_Configuration_strategy)
@settings(max_examples=50)
def test_thingml_configuration_instantiation(instance):
    assert isinstance(instance, thingml_Configuration)



@given(instance=thingml_Configuration_strategy)
def test_thingml_configuration_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=thingml_Type_strategy)
@settings(max_examples=50)
def test_thingml_type_instantiation(instance):
    assert isinstance(instance, thingml_Type)

@given(instance=thingml_LocalVariable_strategy)
@settings(max_examples=50)
def test_thingml_localvariable_instantiation(instance):
    assert isinstance(instance, thingml_LocalVariable)



@given(instance=thingml_LocalVariable_strategy)
def test_thingml_localvariable_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=FunctionCall_strategy)
@settings(max_examples=50)
def test_functioncall_instantiation(instance):
    assert isinstance(instance, FunctionCall)

@given(instance=thingml_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_thingml_functioncallexpression_instantiation(instance):
    assert isinstance(instance, thingml_FunctionCallExpression)

@given(instance=thingml_FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_thingml_functioncallstatement_instantiation(instance):
    assert isinstance(instance, thingml_FunctionCallStatement)

@given(instance=thingml_FunctionCall_strategy)
@settings(max_examples=50)
def test_thingml_functioncall_instantiation(instance):
    assert isinstance(instance, thingml_FunctionCall)

@given(instance=thingml_ConfigPropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml_configpropertyassign_instantiation(instance):
    assert isinstance(instance, thingml_ConfigPropertyAssign)

@given(instance=thingml_ConfigInclude_strategy)
@settings(max_examples=50)
def test_thingml_configinclude_instantiation(instance):
    assert isinstance(instance, thingml_ConfigInclude)

@given(instance=thingml_Connector_strategy)
@settings(max_examples=50)
def test_thingml_connector_instantiation(instance):
    assert isinstance(instance, thingml_Connector)

@given(instance=thingml_Instance_strategy)
@settings(max_examples=50)
def test_thingml_instance_instantiation(instance):
    assert isinstance(instance, thingml_Instance)

@given(instance=thingml_ErrorAction_strategy)
@settings(max_examples=50)
def test_thingml_erroraction_instantiation(instance):
    assert isinstance(instance, thingml_ErrorAction)

@given(instance=thingml_PrintAction_strategy)
@settings(max_examples=50)
def test_thingml_printaction_instantiation(instance):
    assert isinstance(instance, thingml_PrintAction)

@given(instance=thingml_ReturnAction_strategy)
@settings(max_examples=50)
def test_thingml_returnaction_instantiation(instance):
    assert isinstance(instance, thingml_ReturnAction)

@given(instance=thingml_ExpressionGroup_strategy)
@settings(max_examples=50)
def test_thingml_expressiongroup_instantiation(instance):
    assert isinstance(instance, thingml_ExpressionGroup)

@given(instance=thingml_InstanceRef_strategy)
@settings(max_examples=50)
def test_thingml_instanceref_instantiation(instance):
    assert isinstance(instance, thingml_InstanceRef)

@given(instance=thingml_ControlStructure_strategy)
@settings(max_examples=50)
def test_thingml_controlstructure_instantiation(instance):
    assert isinstance(instance, thingml_ControlStructure)

@given(instance=thingml_OrExpression_strategy)
@settings(max_examples=50)
def test_thingml_orexpression_instantiation(instance):
    assert isinstance(instance, thingml_OrExpression)

@given(instance=thingml_AndExpression_strategy)
@settings(max_examples=50)
def test_thingml_andexpression_instantiation(instance):
    assert isinstance(instance, thingml_AndExpression)

@given(instance=thingml_LowerExpression_strategy)
@settings(max_examples=50)
def test_thingml_lowerexpression_instantiation(instance):
    assert isinstance(instance, thingml_LowerExpression)

@given(instance=thingml_GreaterExpression_strategy)
@settings(max_examples=50)
def test_thingml_greaterexpression_instantiation(instance):
    assert isinstance(instance, thingml_GreaterExpression)

@given(instance=thingml_EqualsExpression_strategy)
@settings(max_examples=50)
def test_thingml_equalsexpression_instantiation(instance):
    assert isinstance(instance, thingml_EqualsExpression)

@given(instance=thingml_ModExpression_strategy)
@settings(max_examples=50)
def test_thingml_modexpression_instantiation(instance):
    assert isinstance(instance, thingml_ModExpression)

@given(instance=thingml_DivExpression_strategy)
@settings(max_examples=50)
def test_thingml_divexpression_instantiation(instance):
    assert isinstance(instance, thingml_DivExpression)

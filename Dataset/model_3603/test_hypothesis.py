import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractConnector,
    thingML_ExternalConnector,
    thingML_Connector,
    thingML_InstanceRef,
    thingML_ConfigPropertyAssign,
    Expression,
    thingML_NotEqualsExpression,
    thingML_ModExpression,
    thingML_PropertyReference,
    thingML_IntegerLiteral,
    thingML_UnaryMinus,
    thingML_TimesExpression,
    thingML_MinusExpression,
    thingML_NotExpression,
    thingML_GreaterOrEqualExpression,
    thingML_StringLiteral,
    thingML_Reference,
    thingML_LowerExpression,
    thingML_OrExpression,
    thingML_GreaterExpression,
    thingML_PlusExpression,
    thingML_DivExpression,
    thingML_EqualsExpression,
    thingML_BooleanLiteral,
    thingML_FunctionCallExpression,
    thingML_EnumLiteralRef,
    thingML_AndExpression,
    thingML_ArrayIndex,
    thingML_DoubleLiteral,
    thingML_LowerOrEqualExpression,
    thingML_ExternExpression,
    Handler,
    thingML_Event,
    thingML_Transition,
    thingML_InternalTransition,
    thingML_Action,
    Action,
    thingML_ConditionalAction,
    thingML_ExternStatement,
    thingML_Decrement,
    thingML_StartSession,
    thingML_ReturnAction,
    thingML_ErrorAction,
    thingML_LoopAction,
    thingML_FunctionCallStatement,
    thingML_VariableAssignment,
    thingML_PrintAction,
    thingML_Increment,
    thingML_Variable,
    Event,
    State,
    Region,
    thingML_Region,
    ElmtProperty,
    thingML_ArrayParamRef,
    thingML_LengthArray,
    thingML_SimpleParamRef,
    Source,
    thingML_ElmtProperty,
    thingML_ReferencedElmt,
    thingML_ViewSource,
    thingML_SendAction,
    thingML_Source,
    ViewSource,
    thingML_TimeWindow,
    thingML_LengthWindow,
    thingML_Filter,
    Variable,
    ReferencedElmt,
    thingML_JoinSources,
    thingML_ReceiveMessage,
    thingML_SimpleSource,
    thingML_MessageParameter,
    thingML_MergeSources,
    thingML_ActionBlock,
    Port,
    thingML_ProvidedPort,
    thingML_InternalPort,
    thingML_RequiredPort,
    thingML_EnumerationLiteral,
    thingML_TypeRef,
    thingML_AnnotatedElement,
    thingML_PlatformAnnotation,
    thingML_Import,
    Type,
    thingML_ObjectType,
    thingML_Enumeration,
    thingML_Thing,
    thingML_PrimitiveType,
    AnnotatedElement,
    thingML_Function,
    thingML_Session,
    thingML_Protocol,
    thingML_State,
    thingML_PropertyAssign,
    thingML_FinalState,
    thingML_Message,
    thingML_LocalVariable,
    thingML_Instance,
    thingML_CompositeState,
    thingML_Type,
    thingML_ParallelRegion,
    thingML_Handler,
    thingML_Port,
    thingML_Parameter,
    thingML_Stream,
    thingML_Configuration,
    thingML_Property,
    thingML_AbstractConnector,
    thingML_Expression,
    thingML_ThingMLModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractconnector_is_not_abstract():
    assert not inspect.isabstract(AbstractConnector)


def test_abstractconnector_constructor_exists():
    assert callable(AbstractConnector.__init__)


def test_abstractconnector_constructor_args():
    sig = inspect.signature(AbstractConnector.__init__)
    params = list(sig.parameters.keys())



def test_thingml_externalconnector_is_not_abstract():
    assert not inspect.isabstract(thingML_ExternalConnector)


def test_thingml_externalconnector_constructor_exists():
    assert callable(thingML_ExternalConnector.__init__)


def test_thingml_externalconnector_constructor_args():
    sig = inspect.signature(thingML_ExternalConnector.__init__)
    params = list(sig.parameters.keys())



def test_thingml_connector_is_not_abstract():
    assert not inspect.isabstract(thingML_Connector)


def test_thingml_connector_constructor_exists():
    assert callable(thingML_Connector.__init__)


def test_thingml_connector_constructor_args():
    sig = inspect.signature(thingML_Connector.__init__)
    params = list(sig.parameters.keys())



def test_thingml_instanceref_is_not_abstract():
    assert not inspect.isabstract(thingML_InstanceRef)


def test_thingml_instanceref_constructor_exists():
    assert callable(thingML_InstanceRef.__init__)


def test_thingml_instanceref_constructor_args():
    sig = inspect.signature(thingML_InstanceRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml_configpropertyassign_is_not_abstract():
    assert not inspect.isabstract(thingML_ConfigPropertyAssign)


def test_thingml_configpropertyassign_constructor_exists():
    assert callable(thingML_ConfigPropertyAssign.__init__)


def test_thingml_configpropertyassign_constructor_args():
    sig = inspect.signature(thingML_ConfigPropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_notequalsexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_NotEqualsExpression)


def test_thingml_notequalsexpression_constructor_exists():
    assert callable(thingML_NotEqualsExpression.__init__)


def test_thingml_notequalsexpression_constructor_args():
    sig = inspect.signature(thingML_NotEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_modexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_ModExpression)


def test_thingml_modexpression_constructor_exists():
    assert callable(thingML_ModExpression.__init__)


def test_thingml_modexpression_constructor_args():
    sig = inspect.signature(thingML_ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_propertyreference_is_not_abstract():
    assert not inspect.isabstract(thingML_PropertyReference)


def test_thingml_propertyreference_constructor_exists():
    assert callable(thingML_PropertyReference.__init__)


def test_thingml_propertyreference_constructor_args():
    sig = inspect.signature(thingML_PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_thingml_integerliteral_is_not_abstract():
    assert not inspect.isabstract(thingML_IntegerLiteral)


def test_thingml_integerliteral_constructor_exists():
    assert callable(thingML_IntegerLiteral.__init__)


def test_thingml_integerliteral_constructor_args():
    sig = inspect.signature(thingML_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_thingml_integerliteral_has_intValue():
    assert hasattr(thingML_IntegerLiteral, "intValue")
    descriptor = None
    for klass in thingML_IntegerLiteral.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_unaryminus_is_not_abstract():
    assert not inspect.isabstract(thingML_UnaryMinus)


def test_thingml_unaryminus_constructor_exists():
    assert callable(thingML_UnaryMinus.__init__)


def test_thingml_unaryminus_constructor_args():
    sig = inspect.signature(thingML_UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_thingml_timesexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_TimesExpression)


def test_thingml_timesexpression_constructor_exists():
    assert callable(thingML_TimesExpression.__init__)


def test_thingml_timesexpression_constructor_args():
    sig = inspect.signature(thingML_TimesExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_minusexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_MinusExpression)


def test_thingml_minusexpression_constructor_exists():
    assert callable(thingML_MinusExpression.__init__)


def test_thingml_minusexpression_constructor_args():
    sig = inspect.signature(thingML_MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_notexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_NotExpression)


def test_thingml_notexpression_constructor_exists():
    assert callable(thingML_NotExpression.__init__)


def test_thingml_notexpression_constructor_args():
    sig = inspect.signature(thingML_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_greaterorequalexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_GreaterOrEqualExpression)


def test_thingml_greaterorequalexpression_constructor_exists():
    assert callable(thingML_GreaterOrEqualExpression.__init__)


def test_thingml_greaterorequalexpression_constructor_args():
    sig = inspect.signature(thingML_GreaterOrEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_stringliteral_is_not_abstract():
    assert not inspect.isabstract(thingML_StringLiteral)


def test_thingml_stringliteral_constructor_exists():
    assert callable(thingML_StringLiteral.__init__)


def test_thingml_stringliteral_constructor_args():
    sig = inspect.signature(thingML_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_thingml_stringliteral_has_stringValue():
    assert hasattr(thingML_StringLiteral, "stringValue")
    descriptor = None
    for klass in thingML_StringLiteral.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_reference_is_not_abstract():
    assert not inspect.isabstract(thingML_Reference)


def test_thingml_reference_constructor_exists():
    assert callable(thingML_Reference.__init__)


def test_thingml_reference_constructor_args():
    sig = inspect.signature(thingML_Reference.__init__)
    params = list(sig.parameters.keys())



def test_thingml_lowerexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_LowerExpression)


def test_thingml_lowerexpression_constructor_exists():
    assert callable(thingML_LowerExpression.__init__)


def test_thingml_lowerexpression_constructor_args():
    sig = inspect.signature(thingML_LowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_orexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_OrExpression)


def test_thingml_orexpression_constructor_exists():
    assert callable(thingML_OrExpression.__init__)


def test_thingml_orexpression_constructor_args():
    sig = inspect.signature(thingML_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_greaterexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_GreaterExpression)


def test_thingml_greaterexpression_constructor_exists():
    assert callable(thingML_GreaterExpression.__init__)


def test_thingml_greaterexpression_constructor_args():
    sig = inspect.signature(thingML_GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_plusexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_PlusExpression)


def test_thingml_plusexpression_constructor_exists():
    assert callable(thingML_PlusExpression.__init__)


def test_thingml_plusexpression_constructor_args():
    sig = inspect.signature(thingML_PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_divexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_DivExpression)


def test_thingml_divexpression_constructor_exists():
    assert callable(thingML_DivExpression.__init__)


def test_thingml_divexpression_constructor_args():
    sig = inspect.signature(thingML_DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_equalsexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_EqualsExpression)


def test_thingml_equalsexpression_constructor_exists():
    assert callable(thingML_EqualsExpression.__init__)


def test_thingml_equalsexpression_constructor_args():
    sig = inspect.signature(thingML_EqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(thingML_BooleanLiteral)


def test_thingml_booleanliteral_constructor_exists():
    assert callable(thingML_BooleanLiteral.__init__)


def test_thingml_booleanliteral_constructor_args():
    sig = inspect.signature(thingML_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "boolValue" in params, "Missing parameter 'boolValue'"

def test_thingml_booleanliteral_has_boolValue():
    assert hasattr(thingML_BooleanLiteral, "boolValue")
    descriptor = None
    for klass in thingML_BooleanLiteral.__mro__:
        if "boolValue" in klass.__dict__:
            descriptor = klass.__dict__["boolValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_FunctionCallExpression)


def test_thingml_functioncallexpression_constructor_exists():
    assert callable(thingML_FunctionCallExpression.__init__)


def test_thingml_functioncallexpression_constructor_args():
    sig = inspect.signature(thingML_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_enumliteralref_is_not_abstract():
    assert not inspect.isabstract(thingML_EnumLiteralRef)


def test_thingml_enumliteralref_constructor_exists():
    assert callable(thingML_EnumLiteralRef.__init__)


def test_thingml_enumliteralref_constructor_args():
    sig = inspect.signature(thingML_EnumLiteralRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml_andexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_AndExpression)


def test_thingml_andexpression_constructor_exists():
    assert callable(thingML_AndExpression.__init__)


def test_thingml_andexpression_constructor_args():
    sig = inspect.signature(thingML_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_arrayindex_is_not_abstract():
    assert not inspect.isabstract(thingML_ArrayIndex)


def test_thingml_arrayindex_constructor_exists():
    assert callable(thingML_ArrayIndex.__init__)


def test_thingml_arrayindex_constructor_args():
    sig = inspect.signature(thingML_ArrayIndex.__init__)
    params = list(sig.parameters.keys())



def test_thingml_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(thingML_DoubleLiteral)


def test_thingml_doubleliteral_constructor_exists():
    assert callable(thingML_DoubleLiteral.__init__)


def test_thingml_doubleliteral_constructor_args():
    sig = inspect.signature(thingML_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_thingml_doubleliteral_has_doubleValue():
    assert hasattr(thingML_DoubleLiteral, "doubleValue")
    descriptor = None
    for klass in thingML_DoubleLiteral.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_thingml_lowerorequalexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_LowerOrEqualExpression)


def test_thingml_lowerorequalexpression_constructor_exists():
    assert callable(thingML_LowerOrEqualExpression.__init__)


def test_thingml_lowerorequalexpression_constructor_args():
    sig = inspect.signature(thingML_LowerOrEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_externexpression_is_not_abstract():
    assert not inspect.isabstract(thingML_ExternExpression)


def test_thingml_externexpression_constructor_exists():
    assert callable(thingML_ExternExpression.__init__)


def test_thingml_externexpression_constructor_args():
    sig = inspect.signature(thingML_ExternExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_thingml_externexpression_has_expression():
    assert hasattr(thingML_ExternExpression, "expression")
    descriptor = None
    for klass in thingML_ExternExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_handler_is_not_abstract():
    assert not inspect.isabstract(Handler)


def test_handler_constructor_exists():
    assert callable(Handler.__init__)


def test_handler_constructor_args():
    sig = inspect.signature(Handler.__init__)
    params = list(sig.parameters.keys())



def test_thingml_event_is_not_abstract():
    assert not inspect.isabstract(thingML_Event)


def test_thingml_event_constructor_exists():
    assert callable(thingML_Event.__init__)


def test_thingml_event_constructor_args():
    sig = inspect.signature(thingML_Event.__init__)
    params = list(sig.parameters.keys())



def test_thingml_transition_is_not_abstract():
    assert not inspect.isabstract(thingML_Transition)


def test_thingml_transition_constructor_exists():
    assert callable(thingML_Transition.__init__)


def test_thingml_transition_constructor_args():
    sig = inspect.signature(thingML_Transition.__init__)
    params = list(sig.parameters.keys())



def test_thingml_internaltransition_is_not_abstract():
    assert not inspect.isabstract(thingML_InternalTransition)


def test_thingml_internaltransition_constructor_exists():
    assert callable(thingML_InternalTransition.__init__)


def test_thingml_internaltransition_constructor_args():
    sig = inspect.signature(thingML_InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_thingml_action_is_not_abstract():
    assert not inspect.isabstract(thingML_Action)


def test_thingml_action_constructor_exists():
    assert callable(thingML_Action.__init__)


def test_thingml_action_constructor_args():
    sig = inspect.signature(thingML_Action.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_thingml_conditionalaction_is_not_abstract():
    assert not inspect.isabstract(thingML_ConditionalAction)


def test_thingml_conditionalaction_constructor_exists():
    assert callable(thingML_ConditionalAction.__init__)


def test_thingml_conditionalaction_constructor_args():
    sig = inspect.signature(thingML_ConditionalAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_externstatement_is_not_abstract():
    assert not inspect.isabstract(thingML_ExternStatement)


def test_thingml_externstatement_constructor_exists():
    assert callable(thingML_ExternStatement.__init__)


def test_thingml_externstatement_constructor_args():
    sig = inspect.signature(thingML_ExternStatement.__init__)
    params = list(sig.parameters.keys())
    assert "statement" in params, "Missing parameter 'statement'"

def test_thingml_externstatement_has_statement():
    assert hasattr(thingML_ExternStatement, "statement")
    descriptor = None
    for klass in thingML_ExternStatement.__mro__:
        if "statement" in klass.__dict__:
            descriptor = klass.__dict__["statement"]
            break
    assert isinstance(descriptor, property)



def test_thingml_decrement_is_not_abstract():
    assert not inspect.isabstract(thingML_Decrement)


def test_thingml_decrement_constructor_exists():
    assert callable(thingML_Decrement.__init__)


def test_thingml_decrement_constructor_args():
    sig = inspect.signature(thingML_Decrement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_startsession_is_not_abstract():
    assert not inspect.isabstract(thingML_StartSession)


def test_thingml_startsession_constructor_exists():
    assert callable(thingML_StartSession.__init__)


def test_thingml_startsession_constructor_args():
    sig = inspect.signature(thingML_StartSession.__init__)
    params = list(sig.parameters.keys())



def test_thingml_returnaction_is_not_abstract():
    assert not inspect.isabstract(thingML_ReturnAction)


def test_thingml_returnaction_constructor_exists():
    assert callable(thingML_ReturnAction.__init__)


def test_thingml_returnaction_constructor_args():
    sig = inspect.signature(thingML_ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_erroraction_is_not_abstract():
    assert not inspect.isabstract(thingML_ErrorAction)


def test_thingml_erroraction_constructor_exists():
    assert callable(thingML_ErrorAction.__init__)


def test_thingml_erroraction_constructor_args():
    sig = inspect.signature(thingML_ErrorAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_loopaction_is_not_abstract():
    assert not inspect.isabstract(thingML_LoopAction)


def test_thingml_loopaction_constructor_exists():
    assert callable(thingML_LoopAction.__init__)


def test_thingml_loopaction_constructor_args():
    sig = inspect.signature(thingML_LoopAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(thingML_FunctionCallStatement)


def test_thingml_functioncallstatement_constructor_exists():
    assert callable(thingML_FunctionCallStatement.__init__)


def test_thingml_functioncallstatement_constructor_args():
    sig = inspect.signature(thingML_FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_variableassignment_is_not_abstract():
    assert not inspect.isabstract(thingML_VariableAssignment)


def test_thingml_variableassignment_constructor_exists():
    assert callable(thingML_VariableAssignment.__init__)


def test_thingml_variableassignment_constructor_args():
    sig = inspect.signature(thingML_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_thingml_printaction_is_not_abstract():
    assert not inspect.isabstract(thingML_PrintAction)


def test_thingml_printaction_constructor_exists():
    assert callable(thingML_PrintAction.__init__)


def test_thingml_printaction_constructor_args():
    sig = inspect.signature(thingML_PrintAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_increment_is_not_abstract():
    assert not inspect.isabstract(thingML_Increment)


def test_thingml_increment_constructor_exists():
    assert callable(thingML_Increment.__init__)


def test_thingml_increment_constructor_args():
    sig = inspect.signature(thingML_Increment.__init__)
    params = list(sig.parameters.keys())



def test_thingml_variable_is_not_abstract():
    assert not inspect.isabstract(thingML_Variable)


def test_thingml_variable_constructor_exists():
    assert callable(thingML_Variable.__init__)


def test_thingml_variable_constructor_args():
    sig = inspect.signature(thingML_Variable.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_thingml_region_is_not_abstract():
    assert not inspect.isabstract(thingML_Region)


def test_thingml_region_constructor_exists():
    assert callable(thingML_Region.__init__)


def test_thingml_region_constructor_args():
    sig = inspect.signature(thingML_Region.__init__)
    params = list(sig.parameters.keys())



def test_elmtproperty_is_not_abstract():
    assert not inspect.isabstract(ElmtProperty)


def test_elmtproperty_constructor_exists():
    assert callable(ElmtProperty.__init__)


def test_elmtproperty_constructor_args():
    sig = inspect.signature(ElmtProperty.__init__)
    params = list(sig.parameters.keys())



def test_thingml_arrayparamref_is_not_abstract():
    assert not inspect.isabstract(thingML_ArrayParamRef)


def test_thingml_arrayparamref_constructor_exists():
    assert callable(thingML_ArrayParamRef.__init__)


def test_thingml_arrayparamref_constructor_args():
    sig = inspect.signature(thingML_ArrayParamRef.__init__)
    params = list(sig.parameters.keys())



def test_thingml_lengtharray_is_not_abstract():
    assert not inspect.isabstract(thingML_LengthArray)


def test_thingml_lengtharray_constructor_exists():
    assert callable(thingML_LengthArray.__init__)


def test_thingml_lengtharray_constructor_args():
    sig = inspect.signature(thingML_LengthArray.__init__)
    params = list(sig.parameters.keys())



def test_thingml_simpleparamref_is_not_abstract():
    assert not inspect.isabstract(thingML_SimpleParamRef)


def test_thingml_simpleparamref_constructor_exists():
    assert callable(thingML_SimpleParamRef.__init__)


def test_thingml_simpleparamref_constructor_args():
    sig = inspect.signature(thingML_SimpleParamRef.__init__)
    params = list(sig.parameters.keys())



def test_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_source_constructor_exists():
    assert callable(Source.__init__)


def test_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_thingml_elmtproperty_is_not_abstract():
    assert not inspect.isabstract(thingML_ElmtProperty)


def test_thingml_elmtproperty_constructor_exists():
    assert callable(thingML_ElmtProperty.__init__)


def test_thingml_elmtproperty_constructor_args():
    sig = inspect.signature(thingML_ElmtProperty.__init__)
    params = list(sig.parameters.keys())



def test_thingml_referencedelmt_is_not_abstract():
    assert not inspect.isabstract(thingML_ReferencedElmt)


def test_thingml_referencedelmt_constructor_exists():
    assert callable(thingML_ReferencedElmt.__init__)


def test_thingml_referencedelmt_constructor_args():
    sig = inspect.signature(thingML_ReferencedElmt.__init__)
    params = list(sig.parameters.keys())



def test_thingml_viewsource_is_not_abstract():
    assert not inspect.isabstract(thingML_ViewSource)


def test_thingml_viewsource_constructor_exists():
    assert callable(thingML_ViewSource.__init__)


def test_thingml_viewsource_constructor_args():
    sig = inspect.signature(thingML_ViewSource.__init__)
    params = list(sig.parameters.keys())



def test_thingml_sendaction_is_not_abstract():
    assert not inspect.isabstract(thingML_SendAction)


def test_thingml_sendaction_constructor_exists():
    assert callable(thingML_SendAction.__init__)


def test_thingml_sendaction_constructor_args():
    sig = inspect.signature(thingML_SendAction.__init__)
    params = list(sig.parameters.keys())



def test_thingml_source_is_not_abstract():
    assert not inspect.isabstract(thingML_Source)


def test_thingml_source_constructor_exists():
    assert callable(thingML_Source.__init__)


def test_thingml_source_constructor_args():
    sig = inspect.signature(thingML_Source.__init__)
    params = list(sig.parameters.keys())



def test_viewsource_is_not_abstract():
    assert not inspect.isabstract(ViewSource)


def test_viewsource_constructor_exists():
    assert callable(ViewSource.__init__)


def test_viewsource_constructor_args():
    sig = inspect.signature(ViewSource.__init__)
    params = list(sig.parameters.keys())



def test_thingml_timewindow_is_not_abstract():
    assert not inspect.isabstract(thingML_TimeWindow)


def test_thingml_timewindow_constructor_exists():
    assert callable(thingML_TimeWindow.__init__)


def test_thingml_timewindow_constructor_args():
    sig = inspect.signature(thingML_TimeWindow.__init__)
    params = list(sig.parameters.keys())



def test_thingml_lengthwindow_is_not_abstract():
    assert not inspect.isabstract(thingML_LengthWindow)


def test_thingml_lengthwindow_constructor_exists():
    assert callable(thingML_LengthWindow.__init__)


def test_thingml_lengthwindow_constructor_args():
    sig = inspect.signature(thingML_LengthWindow.__init__)
    params = list(sig.parameters.keys())



def test_thingml_filter_is_not_abstract():
    assert not inspect.isabstract(thingML_Filter)


def test_thingml_filter_constructor_exists():
    assert callable(thingML_Filter.__init__)


def test_thingml_filter_constructor_args():
    sig = inspect.signature(thingML_Filter.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_referencedelmt_is_not_abstract():
    assert not inspect.isabstract(ReferencedElmt)


def test_referencedelmt_constructor_exists():
    assert callable(ReferencedElmt.__init__)


def test_referencedelmt_constructor_args():
    sig = inspect.signature(ReferencedElmt.__init__)
    params = list(sig.parameters.keys())



def test_thingml_joinsources_is_not_abstract():
    assert not inspect.isabstract(thingML_JoinSources)


def test_thingml_joinsources_constructor_exists():
    assert callable(thingML_JoinSources.__init__)


def test_thingml_joinsources_constructor_args():
    sig = inspect.signature(thingML_JoinSources.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_joinsources_has_name():
    assert hasattr(thingML_JoinSources, "name")
    descriptor = None
    for klass in thingML_JoinSources.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_receivemessage_is_not_abstract():
    assert not inspect.isabstract(thingML_ReceiveMessage)


def test_thingml_receivemessage_constructor_exists():
    assert callable(thingML_ReceiveMessage.__init__)


def test_thingml_receivemessage_constructor_args():
    sig = inspect.signature(thingML_ReceiveMessage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_receivemessage_has_name():
    assert hasattr(thingML_ReceiveMessage, "name")
    descriptor = None
    for klass in thingML_ReceiveMessage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_simplesource_is_not_abstract():
    assert not inspect.isabstract(thingML_SimpleSource)


def test_thingml_simplesource_constructor_exists():
    assert callable(thingML_SimpleSource.__init__)


def test_thingml_simplesource_constructor_args():
    sig = inspect.signature(thingML_SimpleSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_simplesource_has_name():
    assert hasattr(thingML_SimpleSource, "name")
    descriptor = None
    for klass in thingML_SimpleSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_messageparameter_is_not_abstract():
    assert not inspect.isabstract(thingML_MessageParameter)


def test_thingml_messageparameter_constructor_exists():
    assert callable(thingML_MessageParameter.__init__)


def test_thingml_messageparameter_constructor_args():
    sig = inspect.signature(thingML_MessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_messageparameter_has_name():
    assert hasattr(thingML_MessageParameter, "name")
    descriptor = None
    for klass in thingML_MessageParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_mergesources_is_not_abstract():
    assert not inspect.isabstract(thingML_MergeSources)


def test_thingml_mergesources_constructor_exists():
    assert callable(thingML_MergeSources.__init__)


def test_thingml_mergesources_constructor_args():
    sig = inspect.signature(thingML_MergeSources.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_mergesources_has_name():
    assert hasattr(thingML_MergeSources, "name")
    descriptor = None
    for klass in thingML_MergeSources.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_actionblock_is_not_abstract():
    assert not inspect.isabstract(thingML_ActionBlock)


def test_thingml_actionblock_constructor_exists():
    assert callable(thingML_ActionBlock.__init__)


def test_thingml_actionblock_constructor_args():
    sig = inspect.signature(thingML_ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_thingml_providedport_is_not_abstract():
    assert not inspect.isabstract(thingML_ProvidedPort)


def test_thingml_providedport_constructor_exists():
    assert callable(thingML_ProvidedPort.__init__)


def test_thingml_providedport_constructor_args():
    sig = inspect.signature(thingML_ProvidedPort.__init__)
    params = list(sig.parameters.keys())



def test_thingml_internalport_is_not_abstract():
    assert not inspect.isabstract(thingML_InternalPort)


def test_thingml_internalport_constructor_exists():
    assert callable(thingML_InternalPort.__init__)


def test_thingml_internalport_constructor_args():
    sig = inspect.signature(thingML_InternalPort.__init__)
    params = list(sig.parameters.keys())



def test_thingml_requiredport_is_not_abstract():
    assert not inspect.isabstract(thingML_RequiredPort)


def test_thingml_requiredport_constructor_exists():
    assert callable(thingML_RequiredPort.__init__)


def test_thingml_requiredport_constructor_args():
    sig = inspect.signature(thingML_RequiredPort.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"

def test_thingml_requiredport_has_optional():
    assert hasattr(thingML_RequiredPort, "optional")
    descriptor = None
    for klass in thingML_RequiredPort.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_thingml_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(thingML_EnumerationLiteral)


def test_thingml_enumerationliteral_constructor_exists():
    assert callable(thingML_EnumerationLiteral.__init__)


def test_thingml_enumerationliteral_constructor_args():
    sig = inspect.signature(thingML_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_enumerationliteral_has_name():
    assert hasattr(thingML_EnumerationLiteral, "name")
    descriptor = None
    for klass in thingML_EnumerationLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_typeref_is_not_abstract():
    assert not inspect.isabstract(thingML_TypeRef)


def test_thingml_typeref_constructor_exists():
    assert callable(thingML_TypeRef.__init__)


def test_thingml_typeref_constructor_args():
    sig = inspect.signature(thingML_TypeRef.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_thingml_typeref_has_isArray():
    assert hasattr(thingML_TypeRef, "isArray")
    descriptor = None
    for klass in thingML_TypeRef.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_thingml_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(thingML_AnnotatedElement)


def test_thingml_annotatedelement_constructor_exists():
    assert callable(thingML_AnnotatedElement.__init__)


def test_thingml_annotatedelement_constructor_args():
    sig = inspect.signature(thingML_AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_platformannotation_is_not_abstract():
    assert not inspect.isabstract(thingML_PlatformAnnotation)


def test_thingml_platformannotation_constructor_exists():
    assert callable(thingML_PlatformAnnotation.__init__)


def test_thingml_platformannotation_constructor_args():
    sig = inspect.signature(thingML_PlatformAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_thingml_platformannotation_has_name():
    assert hasattr(thingML_PlatformAnnotation, "name")
    descriptor = None
    for klass in thingML_PlatformAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_thingml_platformannotation_has_value():
    assert hasattr(thingML_PlatformAnnotation, "value")
    descriptor = None
    for klass in thingML_PlatformAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_thingml_import_is_not_abstract():
    assert not inspect.isabstract(thingML_Import)


def test_thingml_import_constructor_exists():
    assert callable(thingML_Import.__init__)


def test_thingml_import_constructor_args():
    sig = inspect.signature(thingML_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_thingml_import_has_importURI():
    assert hasattr(thingML_Import, "importURI")
    descriptor = None
    for klass in thingML_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_thingml_objecttype_is_not_abstract():
    assert not inspect.isabstract(thingML_ObjectType)


def test_thingml_objecttype_constructor_exists():
    assert callable(thingML_ObjectType.__init__)


def test_thingml_objecttype_constructor_args():
    sig = inspect.signature(thingML_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_thingml_enumeration_is_not_abstract():
    assert not inspect.isabstract(thingML_Enumeration)


def test_thingml_enumeration_constructor_exists():
    assert callable(thingML_Enumeration.__init__)


def test_thingml_enumeration_constructor_args():
    sig = inspect.signature(thingML_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_thingml_thing_is_not_abstract():
    assert not inspect.isabstract(thingML_Thing)


def test_thingml_thing_constructor_exists():
    assert callable(thingML_Thing.__init__)


def test_thingml_thing_constructor_args():
    sig = inspect.signature(thingML_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "fragment" in params, "Missing parameter 'fragment'"

def test_thingml_thing_has_fragment():
    assert hasattr(thingML_Thing, "fragment")
    descriptor = None
    for klass in thingML_Thing.__mro__:
        if "fragment" in klass.__dict__:
            descriptor = klass.__dict__["fragment"]
            break
    assert isinstance(descriptor, property)



def test_thingml_primitivetype_is_not_abstract():
    assert not inspect.isabstract(thingML_PrimitiveType)


def test_thingml_primitivetype_constructor_exists():
    assert callable(thingML_PrimitiveType.__init__)


def test_thingml_primitivetype_constructor_args():
    sig = inspect.signature(thingML_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "ByteSize" in params, "Missing parameter 'ByteSize'"

def test_thingml_primitivetype_has_ByteSize():
    assert hasattr(thingML_PrimitiveType, "ByteSize")
    descriptor = None
    for klass in thingML_PrimitiveType.__mro__:
        if "ByteSize" in klass.__dict__:
            descriptor = klass.__dict__["ByteSize"]
            break
    assert isinstance(descriptor, property)



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_thingml_function_is_not_abstract():
    assert not inspect.isabstract(thingML_Function)


def test_thingml_function_constructor_exists():
    assert callable(thingML_Function.__init__)


def test_thingml_function_constructor_args():
    sig = inspect.signature(thingML_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_function_has_name():
    assert hasattr(thingML_Function, "name")
    descriptor = None
    for klass in thingML_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_session_is_not_abstract():
    assert not inspect.isabstract(thingML_Session)


def test_thingml_session_constructor_exists():
    assert callable(thingML_Session.__init__)


def test_thingml_session_constructor_args():
    sig = inspect.signature(thingML_Session.__init__)
    params = list(sig.parameters.keys())
    assert "maxInstances" in params, "Missing parameter 'maxInstances'"

def test_thingml_session_has_maxInstances():
    assert hasattr(thingML_Session, "maxInstances")
    descriptor = None
    for klass in thingML_Session.__mro__:
        if "maxInstances" in klass.__dict__:
            descriptor = klass.__dict__["maxInstances"]
            break
    assert isinstance(descriptor, property)



def test_thingml_protocol_is_not_abstract():
    assert not inspect.isabstract(thingML_Protocol)


def test_thingml_protocol_constructor_exists():
    assert callable(thingML_Protocol.__init__)


def test_thingml_protocol_constructor_args():
    sig = inspect.signature(thingML_Protocol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_protocol_has_name():
    assert hasattr(thingML_Protocol, "name")
    descriptor = None
    for klass in thingML_Protocol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_state_is_not_abstract():
    assert not inspect.isabstract(thingML_State)


def test_thingml_state_constructor_exists():
    assert callable(thingML_State.__init__)


def test_thingml_state_constructor_args():
    sig = inspect.signature(thingML_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_state_has_name():
    assert hasattr(thingML_State, "name")
    descriptor = None
    for klass in thingML_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_propertyassign_is_not_abstract():
    assert not inspect.isabstract(thingML_PropertyAssign)


def test_thingml_propertyassign_constructor_exists():
    assert callable(thingML_PropertyAssign.__init__)


def test_thingml_propertyassign_constructor_args():
    sig = inspect.signature(thingML_PropertyAssign.__init__)
    params = list(sig.parameters.keys())



def test_thingml_finalstate_is_not_abstract():
    assert not inspect.isabstract(thingML_FinalState)


def test_thingml_finalstate_constructor_exists():
    assert callable(thingML_FinalState.__init__)


def test_thingml_finalstate_constructor_args():
    sig = inspect.signature(thingML_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_thingml_message_is_not_abstract():
    assert not inspect.isabstract(thingML_Message)


def test_thingml_message_constructor_exists():
    assert callable(thingML_Message.__init__)


def test_thingml_message_constructor_args():
    sig = inspect.signature(thingML_Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_message_has_name():
    assert hasattr(thingML_Message, "name")
    descriptor = None
    for klass in thingML_Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_localvariable_is_not_abstract():
    assert not inspect.isabstract(thingML_LocalVariable)


def test_thingml_localvariable_constructor_exists():
    assert callable(thingML_LocalVariable.__init__)


def test_thingml_localvariable_constructor_args():
    sig = inspect.signature(thingML_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_localvariable_has_changeable():
    assert hasattr(thingML_LocalVariable, "changeable")
    descriptor = None
    for klass in thingML_LocalVariable.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)

def test_thingml_localvariable_has_name():
    assert hasattr(thingML_LocalVariable, "name")
    descriptor = None
    for klass in thingML_LocalVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_instance_is_not_abstract():
    assert not inspect.isabstract(thingML_Instance)


def test_thingml_instance_constructor_exists():
    assert callable(thingML_Instance.__init__)


def test_thingml_instance_constructor_args():
    sig = inspect.signature(thingML_Instance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_instance_has_name():
    assert hasattr(thingML_Instance, "name")
    descriptor = None
    for klass in thingML_Instance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_compositestate_is_not_abstract():
    assert not inspect.isabstract(thingML_CompositeState)


def test_thingml_compositestate_constructor_exists():
    assert callable(thingML_CompositeState.__init__)


def test_thingml_compositestate_constructor_args():
    sig = inspect.signature(thingML_CompositeState.__init__)
    params = list(sig.parameters.keys())
    assert "history" in params, "Missing parameter 'history'"

def test_thingml_compositestate_has_history():
    assert hasattr(thingML_CompositeState, "history")
    descriptor = None
    for klass in thingML_CompositeState.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
            break
    assert isinstance(descriptor, property)



def test_thingml_type_is_not_abstract():
    assert not inspect.isabstract(thingML_Type)


def test_thingml_type_constructor_exists():
    assert callable(thingML_Type.__init__)


def test_thingml_type_constructor_args():
    sig = inspect.signature(thingML_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_type_has_name():
    assert hasattr(thingML_Type, "name")
    descriptor = None
    for klass in thingML_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_parallelregion_is_not_abstract():
    assert not inspect.isabstract(thingML_ParallelRegion)


def test_thingml_parallelregion_constructor_exists():
    assert callable(thingML_ParallelRegion.__init__)


def test_thingml_parallelregion_constructor_args():
    sig = inspect.signature(thingML_ParallelRegion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "history" in params, "Missing parameter 'history'"

def test_thingml_parallelregion_has_name():
    assert hasattr(thingML_ParallelRegion, "name")
    descriptor = None
    for klass in thingML_ParallelRegion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_thingml_parallelregion_has_history():
    assert hasattr(thingML_ParallelRegion, "history")
    descriptor = None
    for klass in thingML_ParallelRegion.__mro__:
        if "history" in klass.__dict__:
            descriptor = klass.__dict__["history"]
            break
    assert isinstance(descriptor, property)



def test_thingml_handler_is_not_abstract():
    assert not inspect.isabstract(thingML_Handler)


def test_thingml_handler_constructor_exists():
    assert callable(thingML_Handler.__init__)


def test_thingml_handler_constructor_args():
    sig = inspect.signature(thingML_Handler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_handler_has_name():
    assert hasattr(thingML_Handler, "name")
    descriptor = None
    for klass in thingML_Handler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_port_is_not_abstract():
    assert not inspect.isabstract(thingML_Port)


def test_thingml_port_constructor_exists():
    assert callable(thingML_Port.__init__)


def test_thingml_port_constructor_args():
    sig = inspect.signature(thingML_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_port_has_name():
    assert hasattr(thingML_Port, "name")
    descriptor = None
    for klass in thingML_Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_parameter_is_not_abstract():
    assert not inspect.isabstract(thingML_Parameter)


def test_thingml_parameter_constructor_exists():
    assert callable(thingML_Parameter.__init__)


def test_thingml_parameter_constructor_args():
    sig = inspect.signature(thingML_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_parameter_has_name():
    assert hasattr(thingML_Parameter, "name")
    descriptor = None
    for klass in thingML_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_stream_is_not_abstract():
    assert not inspect.isabstract(thingML_Stream)


def test_thingml_stream_constructor_exists():
    assert callable(thingML_Stream.__init__)


def test_thingml_stream_constructor_args():
    sig = inspect.signature(thingML_Stream.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_stream_has_name():
    assert hasattr(thingML_Stream, "name")
    descriptor = None
    for klass in thingML_Stream.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_configuration_is_not_abstract():
    assert not inspect.isabstract(thingML_Configuration)


def test_thingml_configuration_constructor_exists():
    assert callable(thingML_Configuration.__init__)


def test_thingml_configuration_constructor_args():
    sig = inspect.signature(thingML_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_configuration_has_name():
    assert hasattr(thingML_Configuration, "name")
    descriptor = None
    for klass in thingML_Configuration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_property_is_not_abstract():
    assert not inspect.isabstract(thingML_Property)


def test_thingml_property_constructor_exists():
    assert callable(thingML_Property.__init__)


def test_thingml_property_constructor_args():
    sig = inspect.signature(thingML_Property.__init__)
    params = list(sig.parameters.keys())
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_property_has_changeable():
    assert hasattr(thingML_Property, "changeable")
    descriptor = None
    for klass in thingML_Property.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)

def test_thingml_property_has_name():
    assert hasattr(thingML_Property, "name")
    descriptor = None
    for klass in thingML_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_abstractconnector_is_not_abstract():
    assert not inspect.isabstract(thingML_AbstractConnector)


def test_thingml_abstractconnector_constructor_exists():
    assert callable(thingML_AbstractConnector.__init__)


def test_thingml_abstractconnector_constructor_args():
    sig = inspect.signature(thingML_AbstractConnector.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_thingml_abstractconnector_has_name():
    assert hasattr(thingML_AbstractConnector, "name")
    descriptor = None
    for klass in thingML_AbstractConnector.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thingml_expression_is_not_abstract():
    assert not inspect.isabstract(thingML_Expression)


def test_thingml_expression_constructor_exists():
    assert callable(thingML_Expression.__init__)


def test_thingml_expression_constructor_args():
    sig = inspect.signature(thingML_Expression.__init__)
    params = list(sig.parameters.keys())



def test_thingml_thingmlmodel_is_not_abstract():
    assert not inspect.isabstract(thingML_ThingMLModel)


def test_thingml_thingmlmodel_constructor_exists():
    assert callable(thingML_ThingMLModel.__init__)


def test_thingml_thingmlmodel_constructor_args():
    sig = inspect.signature(thingML_ThingMLModel.__init__)
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
AbstractConnector_strategy = st.builds(
    AbstractConnector,
)
thingML_ExternalConnector_strategy = st.builds(
    thingML_ExternalConnector,
)
thingML_Connector_strategy = st.builds(
    thingML_Connector,
)
thingML_InstanceRef_strategy = st.builds(
    thingML_InstanceRef,
)
thingML_ConfigPropertyAssign_strategy = st.builds(
    thingML_ConfigPropertyAssign,
)
Expression_strategy = st.builds(
    Expression,
)
thingML_NotEqualsExpression_strategy = st.builds(
    thingML_NotEqualsExpression,
)
thingML_ModExpression_strategy = st.builds(
    thingML_ModExpression,
)
thingML_PropertyReference_strategy = st.builds(
    thingML_PropertyReference,
)
thingML_IntegerLiteral_strategy = st.builds(
    thingML_IntegerLiteral,
    intValue=
        st.integers()
)
thingML_UnaryMinus_strategy = st.builds(
    thingML_UnaryMinus,
)
thingML_TimesExpression_strategy = st.builds(
    thingML_TimesExpression,
)
thingML_MinusExpression_strategy = st.builds(
    thingML_MinusExpression,
)
thingML_NotExpression_strategy = st.builds(
    thingML_NotExpression,
)
thingML_GreaterOrEqualExpression_strategy = st.builds(
    thingML_GreaterOrEqualExpression,
)
thingML_StringLiteral_strategy = st.builds(
    thingML_StringLiteral,
    stringValue=
        safe_text
)
thingML_Reference_strategy = st.builds(
    thingML_Reference,
)
thingML_LowerExpression_strategy = st.builds(
    thingML_LowerExpression,
)
thingML_OrExpression_strategy = st.builds(
    thingML_OrExpression,
)
thingML_GreaterExpression_strategy = st.builds(
    thingML_GreaterExpression,
)
thingML_PlusExpression_strategy = st.builds(
    thingML_PlusExpression,
)
thingML_DivExpression_strategy = st.builds(
    thingML_DivExpression,
)
thingML_EqualsExpression_strategy = st.builds(
    thingML_EqualsExpression,
)
thingML_BooleanLiteral_strategy = st.builds(
    thingML_BooleanLiteral,
    boolValue=
        safe_text
)
thingML_FunctionCallExpression_strategy = st.builds(
    thingML_FunctionCallExpression,
)
thingML_EnumLiteralRef_strategy = st.builds(
    thingML_EnumLiteralRef,
)
thingML_AndExpression_strategy = st.builds(
    thingML_AndExpression,
)
thingML_ArrayIndex_strategy = st.builds(
    thingML_ArrayIndex,
)
thingML_DoubleLiteral_strategy = st.builds(
    thingML_DoubleLiteral,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
thingML_LowerOrEqualExpression_strategy = st.builds(
    thingML_LowerOrEqualExpression,
)
thingML_ExternExpression_strategy = st.builds(
    thingML_ExternExpression,
    expression=
        safe_text
)
Handler_strategy = st.builds(
    Handler,
)
thingML_Event_strategy = st.builds(
    thingML_Event,
)
thingML_Transition_strategy = st.builds(
    thingML_Transition,
)
thingML_InternalTransition_strategy = st.builds(
    thingML_InternalTransition,
)
thingML_Action_strategy = st.builds(
    thingML_Action,
)
Action_strategy = st.builds(
    Action,
)
thingML_ConditionalAction_strategy = st.builds(
    thingML_ConditionalAction,
)
thingML_ExternStatement_strategy = st.builds(
    thingML_ExternStatement,
    statement=
        safe_text
)
thingML_Decrement_strategy = st.builds(
    thingML_Decrement,
)
thingML_StartSession_strategy = st.builds(
    thingML_StartSession,
)
thingML_ReturnAction_strategy = st.builds(
    thingML_ReturnAction,
)
thingML_ErrorAction_strategy = st.builds(
    thingML_ErrorAction,
)
thingML_LoopAction_strategy = st.builds(
    thingML_LoopAction,
)
thingML_FunctionCallStatement_strategy = st.builds(
    thingML_FunctionCallStatement,
)
thingML_VariableAssignment_strategy = st.builds(
    thingML_VariableAssignment,
)
thingML_PrintAction_strategy = st.builds(
    thingML_PrintAction,
)
thingML_Increment_strategy = st.builds(
    thingML_Increment,
)
thingML_Variable_strategy = st.builds(
    thingML_Variable,
)
Event_strategy = st.builds(
    Event,
)
State_strategy = st.builds(
    State,
)
Region_strategy = st.builds(
    Region,
)
thingML_Region_strategy = st.builds(
    thingML_Region,
)
ElmtProperty_strategy = st.builds(
    ElmtProperty,
)
thingML_ArrayParamRef_strategy = st.builds(
    thingML_ArrayParamRef,
)
thingML_LengthArray_strategy = st.builds(
    thingML_LengthArray,
)
thingML_SimpleParamRef_strategy = st.builds(
    thingML_SimpleParamRef,
)
Source_strategy = st.builds(
    Source,
)
thingML_ElmtProperty_strategy = st.builds(
    thingML_ElmtProperty,
)
thingML_ReferencedElmt_strategy = st.builds(
    thingML_ReferencedElmt,
)
thingML_ViewSource_strategy = st.builds(
    thingML_ViewSource,
)
thingML_SendAction_strategy = st.builds(
    thingML_SendAction,
)
thingML_Source_strategy = st.builds(
    thingML_Source,
)
ViewSource_strategy = st.builds(
    ViewSource,
)
thingML_TimeWindow_strategy = st.builds(
    thingML_TimeWindow,
)
thingML_LengthWindow_strategy = st.builds(
    thingML_LengthWindow,
)
thingML_Filter_strategy = st.builds(
    thingML_Filter,
)
Variable_strategy = st.builds(
    Variable,
)
ReferencedElmt_strategy = st.builds(
    ReferencedElmt,
)
thingML_JoinSources_strategy = st.builds(
    thingML_JoinSources,
    name=
        safe_text
)
thingML_ReceiveMessage_strategy = st.builds(
    thingML_ReceiveMessage,
    name=
        safe_text
)
thingML_SimpleSource_strategy = st.builds(
    thingML_SimpleSource,
    name=
        safe_text
)
thingML_MessageParameter_strategy = st.builds(
    thingML_MessageParameter,
    name=
        safe_text
)
thingML_MergeSources_strategy = st.builds(
    thingML_MergeSources,
    name=
        safe_text
)
thingML_ActionBlock_strategy = st.builds(
    thingML_ActionBlock,
)
Port_strategy = st.builds(
    Port,
)
thingML_ProvidedPort_strategy = st.builds(
    thingML_ProvidedPort,
)
thingML_InternalPort_strategy = st.builds(
    thingML_InternalPort,
)
thingML_RequiredPort_strategy = st.builds(
    thingML_RequiredPort,
    optional=
        st.booleans()
)
thingML_EnumerationLiteral_strategy = st.builds(
    thingML_EnumerationLiteral,
    name=
        safe_text
)
thingML_TypeRef_strategy = st.builds(
    thingML_TypeRef,
    isArray=
        st.booleans()
)
thingML_AnnotatedElement_strategy = st.builds(
    thingML_AnnotatedElement,
)
thingML_PlatformAnnotation_strategy = st.builds(
    thingML_PlatformAnnotation,
    name=
        safe_text,
    value=
        safe_text
)
thingML_Import_strategy = st.builds(
    thingML_Import,
    importURI=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
thingML_ObjectType_strategy = st.builds(
    thingML_ObjectType,
)
thingML_Enumeration_strategy = st.builds(
    thingML_Enumeration,
)
thingML_Thing_strategy = st.builds(
    thingML_Thing,
    fragment=
        st.booleans()
)
thingML_PrimitiveType_strategy = st.builds(
    thingML_PrimitiveType,
    ByteSize=
        st.integers()
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
thingML_Function_strategy = st.builds(
    thingML_Function,
    name=
        safe_text
)
thingML_Session_strategy = st.builds(
    thingML_Session,
    maxInstances=
        st.integers()
)
thingML_Protocol_strategy = st.builds(
    thingML_Protocol,
    name=
        safe_text
)
thingML_State_strategy = st.builds(
    thingML_State,
    name=
        safe_text
)
thingML_PropertyAssign_strategy = st.builds(
    thingML_PropertyAssign,
)
thingML_FinalState_strategy = st.builds(
    thingML_FinalState,
)
thingML_Message_strategy = st.builds(
    thingML_Message,
    name=
        safe_text
)
thingML_LocalVariable_strategy = st.builds(
    thingML_LocalVariable,
    changeable=
        st.booleans(),
    name=
        safe_text
)
thingML_Instance_strategy = st.builds(
    thingML_Instance,
    name=
        safe_text
)
thingML_CompositeState_strategy = st.builds(
    thingML_CompositeState,
    history=
        st.booleans()
)
thingML_Type_strategy = st.builds(
    thingML_Type,
    name=
        safe_text
)
thingML_ParallelRegion_strategy = st.builds(
    thingML_ParallelRegion,
    name=
        safe_text,
    history=
        st.booleans()
)
thingML_Handler_strategy = st.builds(
    thingML_Handler,
    name=
        safe_text
)
thingML_Port_strategy = st.builds(
    thingML_Port,
    name=
        safe_text
)
thingML_Parameter_strategy = st.builds(
    thingML_Parameter,
    name=
        safe_text
)
thingML_Stream_strategy = st.builds(
    thingML_Stream,
    name=
        safe_text
)
thingML_Configuration_strategy = st.builds(
    thingML_Configuration,
    name=
        safe_text
)
thingML_Property_strategy = st.builds(
    thingML_Property,
    changeable=
        st.booleans(),
    name=
        safe_text
)
thingML_AbstractConnector_strategy = st.builds(
    thingML_AbstractConnector,
    name=
        safe_text
)
thingML_Expression_strategy = st.builds(
    thingML_Expression,
)
thingML_ThingMLModel_strategy = st.builds(
    thingML_ThingMLModel,
)

@given(instance=AbstractConnector_strategy)
@settings(max_examples=50)
def test_abstractconnector_instantiation(instance):
    assert isinstance(instance, AbstractConnector)

@given(instance=thingML_ExternalConnector_strategy)
@settings(max_examples=50)
def test_thingml_externalconnector_instantiation(instance):
    assert isinstance(instance, thingML_ExternalConnector)

@given(instance=thingML_Connector_strategy)
@settings(max_examples=50)
def test_thingml_connector_instantiation(instance):
    assert isinstance(instance, thingML_Connector)

@given(instance=thingML_InstanceRef_strategy)
@settings(max_examples=50)
def test_thingml_instanceref_instantiation(instance):
    assert isinstance(instance, thingML_InstanceRef)

@given(instance=thingML_ConfigPropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml_configpropertyassign_instantiation(instance):
    assert isinstance(instance, thingML_ConfigPropertyAssign)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=thingML_NotEqualsExpression_strategy)
@settings(max_examples=50)
def test_thingml_notequalsexpression_instantiation(instance):
    assert isinstance(instance, thingML_NotEqualsExpression)

@given(instance=thingML_ModExpression_strategy)
@settings(max_examples=50)
def test_thingml_modexpression_instantiation(instance):
    assert isinstance(instance, thingML_ModExpression)

@given(instance=thingML_PropertyReference_strategy)
@settings(max_examples=50)
def test_thingml_propertyreference_instantiation(instance):
    assert isinstance(instance, thingML_PropertyReference)

@given(instance=thingML_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_thingml_integerliteral_instantiation(instance):
    assert isinstance(instance, thingML_IntegerLiteral)



@given(instance=thingML_IntegerLiteral_strategy)
def test_thingml_integerliteral_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=thingML_UnaryMinus_strategy)
@settings(max_examples=50)
def test_thingml_unaryminus_instantiation(instance):
    assert isinstance(instance, thingML_UnaryMinus)

@given(instance=thingML_TimesExpression_strategy)
@settings(max_examples=50)
def test_thingml_timesexpression_instantiation(instance):
    assert isinstance(instance, thingML_TimesExpression)

@given(instance=thingML_MinusExpression_strategy)
@settings(max_examples=50)
def test_thingml_minusexpression_instantiation(instance):
    assert isinstance(instance, thingML_MinusExpression)

@given(instance=thingML_NotExpression_strategy)
@settings(max_examples=50)
def test_thingml_notexpression_instantiation(instance):
    assert isinstance(instance, thingML_NotExpression)

@given(instance=thingML_GreaterOrEqualExpression_strategy)
@settings(max_examples=50)
def test_thingml_greaterorequalexpression_instantiation(instance):
    assert isinstance(instance, thingML_GreaterOrEqualExpression)

@given(instance=thingML_StringLiteral_strategy)
@settings(max_examples=50)
def test_thingml_stringliteral_instantiation(instance):
    assert isinstance(instance, thingML_StringLiteral)



@given(instance=thingML_StringLiteral_strategy)
def test_thingml_stringliteral_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=thingML_Reference_strategy)
@settings(max_examples=50)
def test_thingml_reference_instantiation(instance):
    assert isinstance(instance, thingML_Reference)

@given(instance=thingML_LowerExpression_strategy)
@settings(max_examples=50)
def test_thingml_lowerexpression_instantiation(instance):
    assert isinstance(instance, thingML_LowerExpression)

@given(instance=thingML_OrExpression_strategy)
@settings(max_examples=50)
def test_thingml_orexpression_instantiation(instance):
    assert isinstance(instance, thingML_OrExpression)

@given(instance=thingML_GreaterExpression_strategy)
@settings(max_examples=50)
def test_thingml_greaterexpression_instantiation(instance):
    assert isinstance(instance, thingML_GreaterExpression)

@given(instance=thingML_PlusExpression_strategy)
@settings(max_examples=50)
def test_thingml_plusexpression_instantiation(instance):
    assert isinstance(instance, thingML_PlusExpression)

@given(instance=thingML_DivExpression_strategy)
@settings(max_examples=50)
def test_thingml_divexpression_instantiation(instance):
    assert isinstance(instance, thingML_DivExpression)

@given(instance=thingML_EqualsExpression_strategy)
@settings(max_examples=50)
def test_thingml_equalsexpression_instantiation(instance):
    assert isinstance(instance, thingML_EqualsExpression)

@given(instance=thingML_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_thingml_booleanliteral_instantiation(instance):
    assert isinstance(instance, thingML_BooleanLiteral)



@given(instance=thingML_BooleanLiteral_strategy)
def test_thingml_booleanliteral_boolValue_setter(instance):
    original = instance.boolValue
    instance.boolValue = original
    assert instance.boolValue == original

@given(instance=thingML_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_thingml_functioncallexpression_instantiation(instance):
    assert isinstance(instance, thingML_FunctionCallExpression)

@given(instance=thingML_EnumLiteralRef_strategy)
@settings(max_examples=50)
def test_thingml_enumliteralref_instantiation(instance):
    assert isinstance(instance, thingML_EnumLiteralRef)

@given(instance=thingML_AndExpression_strategy)
@settings(max_examples=50)
def test_thingml_andexpression_instantiation(instance):
    assert isinstance(instance, thingML_AndExpression)

@given(instance=thingML_ArrayIndex_strategy)
@settings(max_examples=50)
def test_thingml_arrayindex_instantiation(instance):
    assert isinstance(instance, thingML_ArrayIndex)

@given(instance=thingML_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_thingml_doubleliteral_instantiation(instance):
    assert isinstance(instance, thingML_DoubleLiteral)



@given(instance=thingML_DoubleLiteral_strategy)
def test_thingml_doubleliteral_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=thingML_LowerOrEqualExpression_strategy)
@settings(max_examples=50)
def test_thingml_lowerorequalexpression_instantiation(instance):
    assert isinstance(instance, thingML_LowerOrEqualExpression)

@given(instance=thingML_ExternExpression_strategy)
@settings(max_examples=50)
def test_thingml_externexpression_instantiation(instance):
    assert isinstance(instance, thingML_ExternExpression)



@given(instance=thingML_ExternExpression_strategy)
def test_thingml_externexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Handler_strategy)
@settings(max_examples=50)
def test_handler_instantiation(instance):
    assert isinstance(instance, Handler)

@given(instance=thingML_Event_strategy)
@settings(max_examples=50)
def test_thingml_event_instantiation(instance):
    assert isinstance(instance, thingML_Event)

@given(instance=thingML_Transition_strategy)
@settings(max_examples=50)
def test_thingml_transition_instantiation(instance):
    assert isinstance(instance, thingML_Transition)

@given(instance=thingML_InternalTransition_strategy)
@settings(max_examples=50)
def test_thingml_internaltransition_instantiation(instance):
    assert isinstance(instance, thingML_InternalTransition)

@given(instance=thingML_Action_strategy)
@settings(max_examples=50)
def test_thingml_action_instantiation(instance):
    assert isinstance(instance, thingML_Action)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=thingML_ConditionalAction_strategy)
@settings(max_examples=50)
def test_thingml_conditionalaction_instantiation(instance):
    assert isinstance(instance, thingML_ConditionalAction)

@given(instance=thingML_ExternStatement_strategy)
@settings(max_examples=50)
def test_thingml_externstatement_instantiation(instance):
    assert isinstance(instance, thingML_ExternStatement)



@given(instance=thingML_ExternStatement_strategy)
def test_thingml_externstatement_statement_setter(instance):
    original = instance.statement
    instance.statement = original
    assert instance.statement == original

@given(instance=thingML_Decrement_strategy)
@settings(max_examples=50)
def test_thingml_decrement_instantiation(instance):
    assert isinstance(instance, thingML_Decrement)

@given(instance=thingML_StartSession_strategy)
@settings(max_examples=50)
def test_thingml_startsession_instantiation(instance):
    assert isinstance(instance, thingML_StartSession)

@given(instance=thingML_ReturnAction_strategy)
@settings(max_examples=50)
def test_thingml_returnaction_instantiation(instance):
    assert isinstance(instance, thingML_ReturnAction)

@given(instance=thingML_ErrorAction_strategy)
@settings(max_examples=50)
def test_thingml_erroraction_instantiation(instance):
    assert isinstance(instance, thingML_ErrorAction)

@given(instance=thingML_LoopAction_strategy)
@settings(max_examples=50)
def test_thingml_loopaction_instantiation(instance):
    assert isinstance(instance, thingML_LoopAction)

@given(instance=thingML_FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_thingml_functioncallstatement_instantiation(instance):
    assert isinstance(instance, thingML_FunctionCallStatement)

@given(instance=thingML_VariableAssignment_strategy)
@settings(max_examples=50)
def test_thingml_variableassignment_instantiation(instance):
    assert isinstance(instance, thingML_VariableAssignment)

@given(instance=thingML_PrintAction_strategy)
@settings(max_examples=50)
def test_thingml_printaction_instantiation(instance):
    assert isinstance(instance, thingML_PrintAction)

@given(instance=thingML_Increment_strategy)
@settings(max_examples=50)
def test_thingml_increment_instantiation(instance):
    assert isinstance(instance, thingML_Increment)

@given(instance=thingML_Variable_strategy)
@settings(max_examples=50)
def test_thingml_variable_instantiation(instance):
    assert isinstance(instance, thingML_Variable)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=thingML_Region_strategy)
@settings(max_examples=50)
def test_thingml_region_instantiation(instance):
    assert isinstance(instance, thingML_Region)

@given(instance=ElmtProperty_strategy)
@settings(max_examples=50)
def test_elmtproperty_instantiation(instance):
    assert isinstance(instance, ElmtProperty)

@given(instance=thingML_ArrayParamRef_strategy)
@settings(max_examples=50)
def test_thingml_arrayparamref_instantiation(instance):
    assert isinstance(instance, thingML_ArrayParamRef)

@given(instance=thingML_LengthArray_strategy)
@settings(max_examples=50)
def test_thingml_lengtharray_instantiation(instance):
    assert isinstance(instance, thingML_LengthArray)

@given(instance=thingML_SimpleParamRef_strategy)
@settings(max_examples=50)
def test_thingml_simpleparamref_instantiation(instance):
    assert isinstance(instance, thingML_SimpleParamRef)

@given(instance=Source_strategy)
@settings(max_examples=50)
def test_source_instantiation(instance):
    assert isinstance(instance, Source)

@given(instance=thingML_ElmtProperty_strategy)
@settings(max_examples=50)
def test_thingml_elmtproperty_instantiation(instance):
    assert isinstance(instance, thingML_ElmtProperty)

@given(instance=thingML_ReferencedElmt_strategy)
@settings(max_examples=50)
def test_thingml_referencedelmt_instantiation(instance):
    assert isinstance(instance, thingML_ReferencedElmt)

@given(instance=thingML_ViewSource_strategy)
@settings(max_examples=50)
def test_thingml_viewsource_instantiation(instance):
    assert isinstance(instance, thingML_ViewSource)

@given(instance=thingML_SendAction_strategy)
@settings(max_examples=50)
def test_thingml_sendaction_instantiation(instance):
    assert isinstance(instance, thingML_SendAction)

@given(instance=thingML_Source_strategy)
@settings(max_examples=50)
def test_thingml_source_instantiation(instance):
    assert isinstance(instance, thingML_Source)

@given(instance=ViewSource_strategy)
@settings(max_examples=50)
def test_viewsource_instantiation(instance):
    assert isinstance(instance, ViewSource)

@given(instance=thingML_TimeWindow_strategy)
@settings(max_examples=50)
def test_thingml_timewindow_instantiation(instance):
    assert isinstance(instance, thingML_TimeWindow)

@given(instance=thingML_LengthWindow_strategy)
@settings(max_examples=50)
def test_thingml_lengthwindow_instantiation(instance):
    assert isinstance(instance, thingML_LengthWindow)

@given(instance=thingML_Filter_strategy)
@settings(max_examples=50)
def test_thingml_filter_instantiation(instance):
    assert isinstance(instance, thingML_Filter)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ReferencedElmt_strategy)
@settings(max_examples=50)
def test_referencedelmt_instantiation(instance):
    assert isinstance(instance, ReferencedElmt)

@given(instance=thingML_JoinSources_strategy)
@settings(max_examples=50)
def test_thingml_joinsources_instantiation(instance):
    assert isinstance(instance, thingML_JoinSources)



@given(instance=thingML_JoinSources_strategy)
def test_thingml_joinsources_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_ReceiveMessage_strategy)
@settings(max_examples=50)
def test_thingml_receivemessage_instantiation(instance):
    assert isinstance(instance, thingML_ReceiveMessage)



@given(instance=thingML_ReceiveMessage_strategy)
def test_thingml_receivemessage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_SimpleSource_strategy)
@settings(max_examples=50)
def test_thingml_simplesource_instantiation(instance):
    assert isinstance(instance, thingML_SimpleSource)



@given(instance=thingML_SimpleSource_strategy)
def test_thingml_simplesource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_MessageParameter_strategy)
@settings(max_examples=50)
def test_thingml_messageparameter_instantiation(instance):
    assert isinstance(instance, thingML_MessageParameter)



@given(instance=thingML_MessageParameter_strategy)
def test_thingml_messageparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_MergeSources_strategy)
@settings(max_examples=50)
def test_thingml_mergesources_instantiation(instance):
    assert isinstance(instance, thingML_MergeSources)



@given(instance=thingML_MergeSources_strategy)
def test_thingml_mergesources_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_ActionBlock_strategy)
@settings(max_examples=50)
def test_thingml_actionblock_instantiation(instance):
    assert isinstance(instance, thingML_ActionBlock)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=thingML_ProvidedPort_strategy)
@settings(max_examples=50)
def test_thingml_providedport_instantiation(instance):
    assert isinstance(instance, thingML_ProvidedPort)

@given(instance=thingML_InternalPort_strategy)
@settings(max_examples=50)
def test_thingml_internalport_instantiation(instance):
    assert isinstance(instance, thingML_InternalPort)

@given(instance=thingML_RequiredPort_strategy)
@settings(max_examples=50)
def test_thingml_requiredport_instantiation(instance):
    assert isinstance(instance, thingML_RequiredPort)



@given(instance=thingML_RequiredPort_strategy)
def test_thingml_requiredport_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=thingML_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_thingml_enumerationliteral_instantiation(instance):
    assert isinstance(instance, thingML_EnumerationLiteral)



@given(instance=thingML_EnumerationLiteral_strategy)
def test_thingml_enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_TypeRef_strategy)
@settings(max_examples=50)
def test_thingml_typeref_instantiation(instance):
    assert isinstance(instance, thingML_TypeRef)



@given(instance=thingML_TypeRef_strategy)
def test_thingml_typeref_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=thingML_AnnotatedElement_strategy)
@settings(max_examples=50)
def test_thingml_annotatedelement_instantiation(instance):
    assert isinstance(instance, thingML_AnnotatedElement)

@given(instance=thingML_PlatformAnnotation_strategy)
@settings(max_examples=50)
def test_thingml_platformannotation_instantiation(instance):
    assert isinstance(instance, thingML_PlatformAnnotation)



@given(instance=thingML_PlatformAnnotation_strategy)
def test_thingml_platformannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=thingML_PlatformAnnotation_strategy)
def test_thingml_platformannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=thingML_Import_strategy)
@settings(max_examples=50)
def test_thingml_import_instantiation(instance):
    assert isinstance(instance, thingML_Import)



@given(instance=thingML_Import_strategy)
def test_thingml_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=thingML_ObjectType_strategy)
@settings(max_examples=50)
def test_thingml_objecttype_instantiation(instance):
    assert isinstance(instance, thingML_ObjectType)

@given(instance=thingML_Enumeration_strategy)
@settings(max_examples=50)
def test_thingml_enumeration_instantiation(instance):
    assert isinstance(instance, thingML_Enumeration)

@given(instance=thingML_Thing_strategy)
@settings(max_examples=50)
def test_thingml_thing_instantiation(instance):
    assert isinstance(instance, thingML_Thing)



@given(instance=thingML_Thing_strategy)
def test_thingml_thing_fragment_setter(instance):
    original = instance.fragment
    instance.fragment = original
    assert instance.fragment == original

@given(instance=thingML_PrimitiveType_strategy)
@settings(max_examples=50)
def test_thingml_primitivetype_instantiation(instance):
    assert isinstance(instance, thingML_PrimitiveType)



@given(instance=thingML_PrimitiveType_strategy)
def test_thingml_primitivetype_ByteSize_setter(instance):
    original = instance.ByteSize
    instance.ByteSize = original
    assert instance.ByteSize == original

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=thingML_Function_strategy)
@settings(max_examples=50)
def test_thingml_function_instantiation(instance):
    assert isinstance(instance, thingML_Function)



@given(instance=thingML_Function_strategy)
def test_thingml_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Session_strategy)
@settings(max_examples=50)
def test_thingml_session_instantiation(instance):
    assert isinstance(instance, thingML_Session)



@given(instance=thingML_Session_strategy)
def test_thingml_session_maxInstances_setter(instance):
    original = instance.maxInstances
    instance.maxInstances = original
    assert instance.maxInstances == original

@given(instance=thingML_Protocol_strategy)
@settings(max_examples=50)
def test_thingml_protocol_instantiation(instance):
    assert isinstance(instance, thingML_Protocol)



@given(instance=thingML_Protocol_strategy)
def test_thingml_protocol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_State_strategy)
@settings(max_examples=50)
def test_thingml_state_instantiation(instance):
    assert isinstance(instance, thingML_State)



@given(instance=thingML_State_strategy)
def test_thingml_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_PropertyAssign_strategy)
@settings(max_examples=50)
def test_thingml_propertyassign_instantiation(instance):
    assert isinstance(instance, thingML_PropertyAssign)

@given(instance=thingML_FinalState_strategy)
@settings(max_examples=50)
def test_thingml_finalstate_instantiation(instance):
    assert isinstance(instance, thingML_FinalState)

@given(instance=thingML_Message_strategy)
@settings(max_examples=50)
def test_thingml_message_instantiation(instance):
    assert isinstance(instance, thingML_Message)



@given(instance=thingML_Message_strategy)
def test_thingml_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_LocalVariable_strategy)
@settings(max_examples=50)
def test_thingml_localvariable_instantiation(instance):
    assert isinstance(instance, thingML_LocalVariable)



@given(instance=thingML_LocalVariable_strategy)
def test_thingml_localvariable_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=thingML_LocalVariable_strategy)
def test_thingml_localvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Instance_strategy)
@settings(max_examples=50)
def test_thingml_instance_instantiation(instance):
    assert isinstance(instance, thingML_Instance)



@given(instance=thingML_Instance_strategy)
def test_thingml_instance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_CompositeState_strategy)
@settings(max_examples=50)
def test_thingml_compositestate_instantiation(instance):
    assert isinstance(instance, thingML_CompositeState)



@given(instance=thingML_CompositeState_strategy)
def test_thingml_compositestate_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original

@given(instance=thingML_Type_strategy)
@settings(max_examples=50)
def test_thingml_type_instantiation(instance):
    assert isinstance(instance, thingML_Type)



@given(instance=thingML_Type_strategy)
def test_thingml_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_ParallelRegion_strategy)
@settings(max_examples=50)
def test_thingml_parallelregion_instantiation(instance):
    assert isinstance(instance, thingML_ParallelRegion)



@given(instance=thingML_ParallelRegion_strategy)
def test_thingml_parallelregion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=thingML_ParallelRegion_strategy)
def test_thingml_parallelregion_history_setter(instance):
    original = instance.history
    instance.history = original
    assert instance.history == original

@given(instance=thingML_Handler_strategy)
@settings(max_examples=50)
def test_thingml_handler_instantiation(instance):
    assert isinstance(instance, thingML_Handler)



@given(instance=thingML_Handler_strategy)
def test_thingml_handler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Port_strategy)
@settings(max_examples=50)
def test_thingml_port_instantiation(instance):
    assert isinstance(instance, thingML_Port)



@given(instance=thingML_Port_strategy)
def test_thingml_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Parameter_strategy)
@settings(max_examples=50)
def test_thingml_parameter_instantiation(instance):
    assert isinstance(instance, thingML_Parameter)



@given(instance=thingML_Parameter_strategy)
def test_thingml_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Stream_strategy)
@settings(max_examples=50)
def test_thingml_stream_instantiation(instance):
    assert isinstance(instance, thingML_Stream)



@given(instance=thingML_Stream_strategy)
def test_thingml_stream_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Configuration_strategy)
@settings(max_examples=50)
def test_thingml_configuration_instantiation(instance):
    assert isinstance(instance, thingML_Configuration)



@given(instance=thingML_Configuration_strategy)
def test_thingml_configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Property_strategy)
@settings(max_examples=50)
def test_thingml_property_instantiation(instance):
    assert isinstance(instance, thingML_Property)



@given(instance=thingML_Property_strategy)
def test_thingml_property_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=thingML_Property_strategy)
def test_thingml_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_AbstractConnector_strategy)
@settings(max_examples=50)
def test_thingml_abstractconnector_instantiation(instance):
    assert isinstance(instance, thingML_AbstractConnector)



@given(instance=thingML_AbstractConnector_strategy)
def test_thingml_abstractconnector_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=thingML_Expression_strategy)
@settings(max_examples=50)
def test_thingml_expression_instantiation(instance):
    assert isinstance(instance, thingML_Expression)

@given(instance=thingML_ThingMLModel_strategy)
@settings(max_examples=50)
def test_thingml_thingmlmodel_instantiation(instance):
    assert isinstance(instance, thingML_ThingMLModel)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rcl_RoverValue,
    rcl_Param,
    rcl_RoverProgram,
    Action,
    rcl_ForwardMinAction,
    rcl_ForwardAction,
    rcl_SendAction,
    rcl_LogAction,
    rcl_StopAction,
    rcl_TurnDegAction,
    rcl_TurnAction,
    rcl_BackwardMinAction,
    rcl_BackwardAction,
    RoverExpression,
    rcl_NumericExpression,
    RoverValue,
    rcl_NumberValue,
    rcl_BooleanValue,
    rcl_BooleanExpression,
    rcl_StringValue,
    rcl_StringExpression,
    Statement,
    rcl_Action,
    rcl_RclBlock,
    rcl_VarAssignment,
    rcl_Statement,
    BooleanValue,
    StringValue,
    NumberValue,
    rcl_VarRef,
    Query,
    rcl_MessageQuery,
    rcl_HumidityQuery,
    rcl_ObstacleQuery,
    rcl_TemperatureQuery,
    rcl_Query,
    rcl_Loop,
    rcl_RoverExpression,
    rcl_Conditional,
    NumericOperator,
    StringOperator,
    BooleanOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rcl_rovervalue_is_not_abstract():
    assert not inspect.isabstract(rcl_RoverValue)


def test_rcl_rovervalue_constructor_exists():
    assert callable(rcl_RoverValue.__init__)


def test_rcl_rovervalue_constructor_args():
    sig = inspect.signature(rcl_RoverValue.__init__)
    params = list(sig.parameters.keys())



def test_rcl_param_is_not_abstract():
    assert not inspect.isabstract(rcl_Param)


def test_rcl_param_constructor_exists():
    assert callable(rcl_Param.__init__)


def test_rcl_param_constructor_args():
    sig = inspect.signature(rcl_Param.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl_param_has_name():
    assert hasattr(rcl_Param, "name")
    descriptor = None
    for klass in rcl_Param.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rcl_roverprogram_is_not_abstract():
    assert not inspect.isabstract(rcl_RoverProgram)


def test_rcl_roverprogram_constructor_exists():
    assert callable(rcl_RoverProgram.__init__)


def test_rcl_roverprogram_constructor_args():
    sig = inspect.signature(rcl_RoverProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl_roverprogram_has_name():
    assert hasattr(rcl_RoverProgram, "name")
    descriptor = None
    for klass in rcl_RoverProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_rcl_forwardminaction_is_not_abstract():
    assert not inspect.isabstract(rcl_ForwardMinAction)


def test_rcl_forwardminaction_constructor_exists():
    assert callable(rcl_ForwardMinAction.__init__)


def test_rcl_forwardminaction_constructor_args():
    sig = inspect.signature(rcl_ForwardMinAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl_forwardaction_is_not_abstract():
    assert not inspect.isabstract(rcl_ForwardAction)


def test_rcl_forwardaction_constructor_exists():
    assert callable(rcl_ForwardAction.__init__)


def test_rcl_forwardaction_constructor_args():
    sig = inspect.signature(rcl_ForwardAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl_sendaction_is_not_abstract():
    assert not inspect.isabstract(rcl_SendAction)


def test_rcl_sendaction_constructor_exists():
    assert callable(rcl_SendAction.__init__)


def test_rcl_sendaction_constructor_args():
    sig = inspect.signature(rcl_SendAction.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_rcl_sendaction_has_message():
    assert hasattr(rcl_SendAction, "message")
    descriptor = None
    for klass in rcl_SendAction.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_rcl_logaction_is_not_abstract():
    assert not inspect.isabstract(rcl_LogAction)


def test_rcl_logaction_constructor_exists():
    assert callable(rcl_LogAction.__init__)


def test_rcl_logaction_constructor_args():
    sig = inspect.signature(rcl_LogAction.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_rcl_logaction_has_message():
    assert hasattr(rcl_LogAction, "message")
    descriptor = None
    for klass in rcl_LogAction.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_rcl_stopaction_is_not_abstract():
    assert not inspect.isabstract(rcl_StopAction)


def test_rcl_stopaction_constructor_exists():
    assert callable(rcl_StopAction.__init__)


def test_rcl_stopaction_constructor_args():
    sig = inspect.signature(rcl_StopAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl_turndegaction_is_not_abstract():
    assert not inspect.isabstract(rcl_TurnDegAction)


def test_rcl_turndegaction_constructor_exists():
    assert callable(rcl_TurnDegAction.__init__)


def test_rcl_turndegaction_constructor_args():
    sig = inspect.signature(rcl_TurnDegAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl_turnaction_is_not_abstract():
    assert not inspect.isabstract(rcl_TurnAction)


def test_rcl_turnaction_constructor_exists():
    assert callable(rcl_TurnAction.__init__)


def test_rcl_turnaction_constructor_args():
    sig = inspect.signature(rcl_TurnAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl_backwardminaction_is_not_abstract():
    assert not inspect.isabstract(rcl_BackwardMinAction)


def test_rcl_backwardminaction_constructor_exists():
    assert callable(rcl_BackwardMinAction.__init__)


def test_rcl_backwardminaction_constructor_args():
    sig = inspect.signature(rcl_BackwardMinAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl_backwardaction_is_not_abstract():
    assert not inspect.isabstract(rcl_BackwardAction)


def test_rcl_backwardaction_constructor_exists():
    assert callable(rcl_BackwardAction.__init__)


def test_rcl_backwardaction_constructor_args():
    sig = inspect.signature(rcl_BackwardAction.__init__)
    params = list(sig.parameters.keys())



def test_roverexpression_is_not_abstract():
    assert not inspect.isabstract(RoverExpression)


def test_roverexpression_constructor_exists():
    assert callable(RoverExpression.__init__)


def test_roverexpression_constructor_args():
    sig = inspect.signature(RoverExpression.__init__)
    params = list(sig.parameters.keys())



def test_rcl_numericexpression_is_not_abstract():
    assert not inspect.isabstract(rcl_NumericExpression)


def test_rcl_numericexpression_constructor_exists():
    assert callable(rcl_NumericExpression.__init__)


def test_rcl_numericexpression_constructor_args():
    sig = inspect.signature(rcl_NumericExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rcl_numericexpression_has_op():
    assert hasattr(rcl_NumericExpression, "op")
    descriptor = None
    for klass in rcl_NumericExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rovervalue_is_not_abstract():
    assert not inspect.isabstract(RoverValue)


def test_rovervalue_constructor_exists():
    assert callable(RoverValue.__init__)


def test_rovervalue_constructor_args():
    sig = inspect.signature(RoverValue.__init__)
    params = list(sig.parameters.keys())



def test_rcl_numbervalue_is_not_abstract():
    assert not inspect.isabstract(rcl_NumberValue)


def test_rcl_numbervalue_constructor_exists():
    assert callable(rcl_NumberValue.__init__)


def test_rcl_numbervalue_constructor_args():
    sig = inspect.signature(rcl_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "nValue" in params, "Missing parameter 'nValue'"

def test_rcl_numbervalue_has_nValue():
    assert hasattr(rcl_NumberValue, "nValue")
    descriptor = None
    for klass in rcl_NumberValue.__mro__:
        if "nValue" in klass.__dict__:
            descriptor = klass.__dict__["nValue"]
            break
    assert isinstance(descriptor, property)



def test_rcl_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(rcl_BooleanValue)


def test_rcl_booleanvalue_constructor_exists():
    assert callable(rcl_BooleanValue.__init__)


def test_rcl_booleanvalue_constructor_args():
    sig = inspect.signature(rcl_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "bValue" in params, "Missing parameter 'bValue'"

def test_rcl_booleanvalue_has_bValue():
    assert hasattr(rcl_BooleanValue, "bValue")
    descriptor = None
    for klass in rcl_BooleanValue.__mro__:
        if "bValue" in klass.__dict__:
            descriptor = klass.__dict__["bValue"]
            break
    assert isinstance(descriptor, property)



def test_rcl_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(rcl_BooleanExpression)


def test_rcl_booleanexpression_constructor_exists():
    assert callable(rcl_BooleanExpression.__init__)


def test_rcl_booleanexpression_constructor_args():
    sig = inspect.signature(rcl_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rcl_booleanexpression_has_op():
    assert hasattr(rcl_BooleanExpression, "op")
    descriptor = None
    for klass in rcl_BooleanExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rcl_stringvalue_is_not_abstract():
    assert not inspect.isabstract(rcl_StringValue)


def test_rcl_stringvalue_constructor_exists():
    assert callable(rcl_StringValue.__init__)


def test_rcl_stringvalue_constructor_args():
    sig = inspect.signature(rcl_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "sValue" in params, "Missing parameter 'sValue'"

def test_rcl_stringvalue_has_sValue():
    assert hasattr(rcl_StringValue, "sValue")
    descriptor = None
    for klass in rcl_StringValue.__mro__:
        if "sValue" in klass.__dict__:
            descriptor = klass.__dict__["sValue"]
            break
    assert isinstance(descriptor, property)



def test_rcl_stringexpression_is_not_abstract():
    assert not inspect.isabstract(rcl_StringExpression)


def test_rcl_stringexpression_constructor_exists():
    assert callable(rcl_StringExpression.__init__)


def test_rcl_stringexpression_constructor_args():
    sig = inspect.signature(rcl_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rcl_stringexpression_has_op():
    assert hasattr(rcl_StringExpression, "op")
    descriptor = None
    for klass in rcl_StringExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_rcl_action_is_not_abstract():
    assert not inspect.isabstract(rcl_Action)


def test_rcl_action_constructor_exists():
    assert callable(rcl_Action.__init__)


def test_rcl_action_constructor_args():
    sig = inspect.signature(rcl_Action.__init__)
    params = list(sig.parameters.keys())



def test_rcl_rclblock_is_not_abstract():
    assert not inspect.isabstract(rcl_RclBlock)


def test_rcl_rclblock_constructor_exists():
    assert callable(rcl_RclBlock.__init__)


def test_rcl_rclblock_constructor_args():
    sig = inspect.signature(rcl_RclBlock.__init__)
    params = list(sig.parameters.keys())



def test_rcl_varassignment_is_not_abstract():
    assert not inspect.isabstract(rcl_VarAssignment)


def test_rcl_varassignment_constructor_exists():
    assert callable(rcl_VarAssignment.__init__)


def test_rcl_varassignment_constructor_args():
    sig = inspect.signature(rcl_VarAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl_varassignment_has_name():
    assert hasattr(rcl_VarAssignment, "name")
    descriptor = None
    for klass in rcl_VarAssignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rcl_statement_is_not_abstract():
    assert not inspect.isabstract(rcl_Statement)


def test_rcl_statement_constructor_exists():
    assert callable(rcl_Statement.__init__)


def test_rcl_statement_constructor_args():
    sig = inspect.signature(rcl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(BooleanValue)


def test_booleanvalue_constructor_exists():
    assert callable(BooleanValue.__init__)


def test_booleanvalue_constructor_args():
    sig = inspect.signature(BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_stringvalue_is_not_abstract():
    assert not inspect.isabstract(StringValue)


def test_stringvalue_constructor_exists():
    assert callable(StringValue.__init__)


def test_stringvalue_constructor_args():
    sig = inspect.signature(StringValue.__init__)
    params = list(sig.parameters.keys())



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_rcl_varref_is_not_abstract():
    assert not inspect.isabstract(rcl_VarRef)


def test_rcl_varref_constructor_exists():
    assert callable(rcl_VarRef.__init__)


def test_rcl_varref_constructor_args():
    sig = inspect.signature(rcl_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl_varref_has_name():
    assert hasattr(rcl_VarRef, "name")
    descriptor = None
    for klass in rcl_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_rcl_messagequery_is_not_abstract():
    assert not inspect.isabstract(rcl_MessageQuery)


def test_rcl_messagequery_constructor_exists():
    assert callable(rcl_MessageQuery.__init__)


def test_rcl_messagequery_constructor_args():
    sig = inspect.signature(rcl_MessageQuery.__init__)
    params = list(sig.parameters.keys())



def test_rcl_humidityquery_is_not_abstract():
    assert not inspect.isabstract(rcl_HumidityQuery)


def test_rcl_humidityquery_constructor_exists():
    assert callable(rcl_HumidityQuery.__init__)


def test_rcl_humidityquery_constructor_args():
    sig = inspect.signature(rcl_HumidityQuery.__init__)
    params = list(sig.parameters.keys())



def test_rcl_obstaclequery_is_not_abstract():
    assert not inspect.isabstract(rcl_ObstacleQuery)


def test_rcl_obstaclequery_constructor_exists():
    assert callable(rcl_ObstacleQuery.__init__)


def test_rcl_obstaclequery_constructor_args():
    sig = inspect.signature(rcl_ObstacleQuery.__init__)
    params = list(sig.parameters.keys())
    assert "front" in params, "Missing parameter 'front'"

def test_rcl_obstaclequery_has_front():
    assert hasattr(rcl_ObstacleQuery, "front")
    descriptor = None
    for klass in rcl_ObstacleQuery.__mro__:
        if "front" in klass.__dict__:
            descriptor = klass.__dict__["front"]
            break
    assert isinstance(descriptor, property)



def test_rcl_temperaturequery_is_not_abstract():
    assert not inspect.isabstract(rcl_TemperatureQuery)


def test_rcl_temperaturequery_constructor_exists():
    assert callable(rcl_TemperatureQuery.__init__)


def test_rcl_temperaturequery_constructor_args():
    sig = inspect.signature(rcl_TemperatureQuery.__init__)
    params = list(sig.parameters.keys())



def test_rcl_query_is_not_abstract():
    assert not inspect.isabstract(rcl_Query)


def test_rcl_query_constructor_exists():
    assert callable(rcl_Query.__init__)


def test_rcl_query_constructor_args():
    sig = inspect.signature(rcl_Query.__init__)
    params = list(sig.parameters.keys())



def test_rcl_loop_is_not_abstract():
    assert not inspect.isabstract(rcl_Loop)


def test_rcl_loop_constructor_exists():
    assert callable(rcl_Loop.__init__)


def test_rcl_loop_constructor_args():
    sig = inspect.signature(rcl_Loop.__init__)
    params = list(sig.parameters.keys())



def test_rcl_roverexpression_is_not_abstract():
    assert not inspect.isabstract(rcl_RoverExpression)


def test_rcl_roverexpression_constructor_exists():
    assert callable(rcl_RoverExpression.__init__)


def test_rcl_roverexpression_constructor_args():
    sig = inspect.signature(rcl_RoverExpression.__init__)
    params = list(sig.parameters.keys())



def test_rcl_conditional_is_not_abstract():
    assert not inspect.isabstract(rcl_Conditional)


def test_rcl_conditional_constructor_exists():
    assert callable(rcl_Conditional.__init__)


def test_rcl_conditional_constructor_args():
    sig = inspect.signature(rcl_Conditional.__init__)
    params = list(sig.parameters.keys())

def test_numericoperator_exists():
    # Check that the Enumeration exists
    assert NumericOperator is not None

def test_numericoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericOperator]
    expected_literals = [
        "gt",
        "lt",
        "leq",
        "eq",
        "geq",
        "neq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericOperator"

def test_stringoperator_exists():
    # Check that the Enumeration exists
    assert StringOperator is not None

def test_stringoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringOperator]
    expected_literals = [
        "eq",
        "neq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringOperator"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "eq",
        "neq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"


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
rcl_RoverValue_strategy = st.builds(
    rcl_RoverValue,
)
rcl_Param_strategy = st.builds(
    rcl_Param,
    name=
        safe_text
)
rcl_RoverProgram_strategy = st.builds(
    rcl_RoverProgram,
    name=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
rcl_ForwardMinAction_strategy = st.builds(
    rcl_ForwardMinAction,
)
rcl_ForwardAction_strategy = st.builds(
    rcl_ForwardAction,
)
rcl_SendAction_strategy = st.builds(
    rcl_SendAction,
    message=
        safe_text
)
rcl_LogAction_strategy = st.builds(
    rcl_LogAction,
    message=
        safe_text
)
rcl_StopAction_strategy = st.builds(
    rcl_StopAction,
)
rcl_TurnDegAction_strategy = st.builds(
    rcl_TurnDegAction,
)
rcl_TurnAction_strategy = st.builds(
    rcl_TurnAction,
)
rcl_BackwardMinAction_strategy = st.builds(
    rcl_BackwardMinAction,
)
rcl_BackwardAction_strategy = st.builds(
    rcl_BackwardAction,
)
RoverExpression_strategy = st.builds(
    RoverExpression,
)
rcl_NumericExpression_strategy = st.builds(
    rcl_NumericExpression,
    op=
        safe_text
)
RoverValue_strategy = st.builds(
    RoverValue,
)
rcl_NumberValue_strategy = st.builds(
    rcl_NumberValue,
    nValue=
        st.integers()
)
rcl_BooleanValue_strategy = st.builds(
    rcl_BooleanValue,
    bValue=
        st.booleans()
)
rcl_BooleanExpression_strategy = st.builds(
    rcl_BooleanExpression,
    op=
        safe_text
)
rcl_StringValue_strategy = st.builds(
    rcl_StringValue,
    sValue=
        safe_text
)
rcl_StringExpression_strategy = st.builds(
    rcl_StringExpression,
    op=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
rcl_Action_strategy = st.builds(
    rcl_Action,
)
rcl_RclBlock_strategy = st.builds(
    rcl_RclBlock,
)
rcl_VarAssignment_strategy = st.builds(
    rcl_VarAssignment,
    name=
        safe_text
)
rcl_Statement_strategy = st.builds(
    rcl_Statement,
)
BooleanValue_strategy = st.builds(
    BooleanValue,
)
StringValue_strategy = st.builds(
    StringValue,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
rcl_VarRef_strategy = st.builds(
    rcl_VarRef,
    name=
        safe_text
)
Query_strategy = st.builds(
    Query,
)
rcl_MessageQuery_strategy = st.builds(
    rcl_MessageQuery,
)
rcl_HumidityQuery_strategy = st.builds(
    rcl_HumidityQuery,
)
rcl_ObstacleQuery_strategy = st.builds(
    rcl_ObstacleQuery,
    front=
        st.booleans()
)
rcl_TemperatureQuery_strategy = st.builds(
    rcl_TemperatureQuery,
)
rcl_Query_strategy = st.builds(
    rcl_Query,
)
rcl_Loop_strategy = st.builds(
    rcl_Loop,
)
rcl_RoverExpression_strategy = st.builds(
    rcl_RoverExpression,
)
rcl_Conditional_strategy = st.builds(
    rcl_Conditional,
)

@given(instance=rcl_RoverValue_strategy)
@settings(max_examples=50)
def test_rcl_rovervalue_instantiation(instance):
    assert isinstance(instance, rcl_RoverValue)

@given(instance=rcl_Param_strategy)
@settings(max_examples=50)
def test_rcl_param_instantiation(instance):
    assert isinstance(instance, rcl_Param)



@given(instance=rcl_Param_strategy)
def test_rcl_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rcl_RoverProgram_strategy)
@settings(max_examples=50)
def test_rcl_roverprogram_instantiation(instance):
    assert isinstance(instance, rcl_RoverProgram)



@given(instance=rcl_RoverProgram_strategy)
def test_rcl_roverprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=rcl_ForwardMinAction_strategy)
@settings(max_examples=50)
def test_rcl_forwardminaction_instantiation(instance):
    assert isinstance(instance, rcl_ForwardMinAction)

@given(instance=rcl_ForwardAction_strategy)
@settings(max_examples=50)
def test_rcl_forwardaction_instantiation(instance):
    assert isinstance(instance, rcl_ForwardAction)

@given(instance=rcl_SendAction_strategy)
@settings(max_examples=50)
def test_rcl_sendaction_instantiation(instance):
    assert isinstance(instance, rcl_SendAction)



@given(instance=rcl_SendAction_strategy)
def test_rcl_sendaction_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=rcl_LogAction_strategy)
@settings(max_examples=50)
def test_rcl_logaction_instantiation(instance):
    assert isinstance(instance, rcl_LogAction)



@given(instance=rcl_LogAction_strategy)
def test_rcl_logaction_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=rcl_StopAction_strategy)
@settings(max_examples=50)
def test_rcl_stopaction_instantiation(instance):
    assert isinstance(instance, rcl_StopAction)

@given(instance=rcl_TurnDegAction_strategy)
@settings(max_examples=50)
def test_rcl_turndegaction_instantiation(instance):
    assert isinstance(instance, rcl_TurnDegAction)

@given(instance=rcl_TurnAction_strategy)
@settings(max_examples=50)
def test_rcl_turnaction_instantiation(instance):
    assert isinstance(instance, rcl_TurnAction)

@given(instance=rcl_BackwardMinAction_strategy)
@settings(max_examples=50)
def test_rcl_backwardminaction_instantiation(instance):
    assert isinstance(instance, rcl_BackwardMinAction)

@given(instance=rcl_BackwardAction_strategy)
@settings(max_examples=50)
def test_rcl_backwardaction_instantiation(instance):
    assert isinstance(instance, rcl_BackwardAction)

@given(instance=RoverExpression_strategy)
@settings(max_examples=50)
def test_roverexpression_instantiation(instance):
    assert isinstance(instance, RoverExpression)

@given(instance=rcl_NumericExpression_strategy)
@settings(max_examples=50)
def test_rcl_numericexpression_instantiation(instance):
    assert isinstance(instance, rcl_NumericExpression)



@given(instance=rcl_NumericExpression_strategy)
def test_rcl_numericexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=RoverValue_strategy)
@settings(max_examples=50)
def test_rovervalue_instantiation(instance):
    assert isinstance(instance, RoverValue)

@given(instance=rcl_NumberValue_strategy)
@settings(max_examples=50)
def test_rcl_numbervalue_instantiation(instance):
    assert isinstance(instance, rcl_NumberValue)



@given(instance=rcl_NumberValue_strategy)
def test_rcl_numbervalue_nValue_setter(instance):
    original = instance.nValue
    instance.nValue = original
    assert instance.nValue == original

@given(instance=rcl_BooleanValue_strategy)
@settings(max_examples=50)
def test_rcl_booleanvalue_instantiation(instance):
    assert isinstance(instance, rcl_BooleanValue)



@given(instance=rcl_BooleanValue_strategy)
def test_rcl_booleanvalue_bValue_setter(instance):
    original = instance.bValue
    instance.bValue = original
    assert instance.bValue == original

@given(instance=rcl_BooleanExpression_strategy)
@settings(max_examples=50)
def test_rcl_booleanexpression_instantiation(instance):
    assert isinstance(instance, rcl_BooleanExpression)



@given(instance=rcl_BooleanExpression_strategy)
def test_rcl_booleanexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rcl_StringValue_strategy)
@settings(max_examples=50)
def test_rcl_stringvalue_instantiation(instance):
    assert isinstance(instance, rcl_StringValue)



@given(instance=rcl_StringValue_strategy)
def test_rcl_stringvalue_sValue_setter(instance):
    original = instance.sValue
    instance.sValue = original
    assert instance.sValue == original

@given(instance=rcl_StringExpression_strategy)
@settings(max_examples=50)
def test_rcl_stringexpression_instantiation(instance):
    assert isinstance(instance, rcl_StringExpression)



@given(instance=rcl_StringExpression_strategy)
def test_rcl_stringexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=rcl_Action_strategy)
@settings(max_examples=50)
def test_rcl_action_instantiation(instance):
    assert isinstance(instance, rcl_Action)

@given(instance=rcl_RclBlock_strategy)
@settings(max_examples=50)
def test_rcl_rclblock_instantiation(instance):
    assert isinstance(instance, rcl_RclBlock)

@given(instance=rcl_VarAssignment_strategy)
@settings(max_examples=50)
def test_rcl_varassignment_instantiation(instance):
    assert isinstance(instance, rcl_VarAssignment)



@given(instance=rcl_VarAssignment_strategy)
def test_rcl_varassignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rcl_Statement_strategy)
@settings(max_examples=50)
def test_rcl_statement_instantiation(instance):
    assert isinstance(instance, rcl_Statement)

@given(instance=BooleanValue_strategy)
@settings(max_examples=50)
def test_booleanvalue_instantiation(instance):
    assert isinstance(instance, BooleanValue)

@given(instance=StringValue_strategy)
@settings(max_examples=50)
def test_stringvalue_instantiation(instance):
    assert isinstance(instance, StringValue)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=rcl_VarRef_strategy)
@settings(max_examples=50)
def test_rcl_varref_instantiation(instance):
    assert isinstance(instance, rcl_VarRef)



@given(instance=rcl_VarRef_strategy)
def test_rcl_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=rcl_MessageQuery_strategy)
@settings(max_examples=50)
def test_rcl_messagequery_instantiation(instance):
    assert isinstance(instance, rcl_MessageQuery)

@given(instance=rcl_HumidityQuery_strategy)
@settings(max_examples=50)
def test_rcl_humidityquery_instantiation(instance):
    assert isinstance(instance, rcl_HumidityQuery)

@given(instance=rcl_ObstacleQuery_strategy)
@settings(max_examples=50)
def test_rcl_obstaclequery_instantiation(instance):
    assert isinstance(instance, rcl_ObstacleQuery)



@given(instance=rcl_ObstacleQuery_strategy)
def test_rcl_obstaclequery_front_setter(instance):
    original = instance.front
    instance.front = original
    assert instance.front == original

@given(instance=rcl_TemperatureQuery_strategy)
@settings(max_examples=50)
def test_rcl_temperaturequery_instantiation(instance):
    assert isinstance(instance, rcl_TemperatureQuery)

@given(instance=rcl_Query_strategy)
@settings(max_examples=50)
def test_rcl_query_instantiation(instance):
    assert isinstance(instance, rcl_Query)

@given(instance=rcl_Loop_strategy)
@settings(max_examples=50)
def test_rcl_loop_instantiation(instance):
    assert isinstance(instance, rcl_Loop)

@given(instance=rcl_RoverExpression_strategy)
@settings(max_examples=50)
def test_rcl_roverexpression_instantiation(instance):
    assert isinstance(instance, rcl_RoverExpression)

@given(instance=rcl_Conditional_strategy)
@settings(max_examples=50)
def test_rcl_conditional_instantiation(instance):
    assert isinstance(instance, rcl_Conditional)

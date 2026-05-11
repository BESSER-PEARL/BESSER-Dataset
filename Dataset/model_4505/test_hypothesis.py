import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Action,
    rcl::ForwardMinAction,
    rcl::ForwardAction,
    rcl::SendAction,
    rcl::LogAction,
    rcl::StopAction,
    rcl::TurnDegAction,
    rcl::TurnAction,
    rcl::BackwardMinAction,
    rcl::BackwardAction,
    RoverExpression,
    rcl::NumericExpression,
    RoverValue,
    rcl::NumberValue,
    rcl::BooleanValue,
    rcl::BooleanExpression,
    rcl::StringValue,
    rcl::StringExpression,
    Statement,
    rcl::Action,
    rcl::VarAssignment,
    rcl::Statement,
    BooleanValue,
    StringValue,
    NumberValue,
    rcl::VarRef,
    Query,
    rcl::HumidityQuery,
    rcl::ObstacleQuery,
    rcl::MessageQuery,
    rcl::TemperatureQuery,
    rcl::Query,
    rcl::Loop,
    rcl::RoverExpression,
    rcl::Conditional,
    rcl::RoverValue,
    rcl::RclBlock,
    rcl::Param,
    rcl::RoverProgram,
    StringOperator,
    BooleanOperator,
    NumericOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_rcl::forwardminaction_is_not_abstract():
    assert not inspect.isabstract(rcl::ForwardMinAction)


def test_rcl::forwardminaction_constructor_exists():
    assert callable(rcl::ForwardMinAction.__init__)


def test_rcl::forwardminaction_constructor_args():
    sig = inspect.signature(rcl::ForwardMinAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl::forwardaction_is_not_abstract():
    assert not inspect.isabstract(rcl::ForwardAction)


def test_rcl::forwardaction_constructor_exists():
    assert callable(rcl::ForwardAction.__init__)


def test_rcl::forwardaction_constructor_args():
    sig = inspect.signature(rcl::ForwardAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl::sendaction_is_not_abstract():
    assert not inspect.isabstract(rcl::SendAction)


def test_rcl::sendaction_constructor_exists():
    assert callable(rcl::SendAction.__init__)


def test_rcl::sendaction_constructor_args():
    sig = inspect.signature(rcl::SendAction.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_rcl::sendaction_has_message():
    assert hasattr(rcl::SendAction, "message")
    descriptor = None
    for klass in rcl::SendAction.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_rcl::logaction_is_not_abstract():
    assert not inspect.isabstract(rcl::LogAction)


def test_rcl::logaction_constructor_exists():
    assert callable(rcl::LogAction.__init__)


def test_rcl::logaction_constructor_args():
    sig = inspect.signature(rcl::LogAction.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_rcl::logaction_has_message():
    assert hasattr(rcl::LogAction, "message")
    descriptor = None
    for klass in rcl::LogAction.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_rcl::stopaction_is_not_abstract():
    assert not inspect.isabstract(rcl::StopAction)


def test_rcl::stopaction_constructor_exists():
    assert callable(rcl::StopAction.__init__)


def test_rcl::stopaction_constructor_args():
    sig = inspect.signature(rcl::StopAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl::turndegaction_is_not_abstract():
    assert not inspect.isabstract(rcl::TurnDegAction)


def test_rcl::turndegaction_constructor_exists():
    assert callable(rcl::TurnDegAction.__init__)


def test_rcl::turndegaction_constructor_args():
    sig = inspect.signature(rcl::TurnDegAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl::turnaction_is_not_abstract():
    assert not inspect.isabstract(rcl::TurnAction)


def test_rcl::turnaction_constructor_exists():
    assert callable(rcl::TurnAction.__init__)


def test_rcl::turnaction_constructor_args():
    sig = inspect.signature(rcl::TurnAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl::backwardminaction_is_not_abstract():
    assert not inspect.isabstract(rcl::BackwardMinAction)


def test_rcl::backwardminaction_constructor_exists():
    assert callable(rcl::BackwardMinAction.__init__)


def test_rcl::backwardminaction_constructor_args():
    sig = inspect.signature(rcl::BackwardMinAction.__init__)
    params = list(sig.parameters.keys())



def test_rcl::backwardaction_is_not_abstract():
    assert not inspect.isabstract(rcl::BackwardAction)


def test_rcl::backwardaction_constructor_exists():
    assert callable(rcl::BackwardAction.__init__)


def test_rcl::backwardaction_constructor_args():
    sig = inspect.signature(rcl::BackwardAction.__init__)
    params = list(sig.parameters.keys())



def test_roverexpression_is_not_abstract():
    assert not inspect.isabstract(RoverExpression)


def test_roverexpression_constructor_exists():
    assert callable(RoverExpression.__init__)


def test_roverexpression_constructor_args():
    sig = inspect.signature(RoverExpression.__init__)
    params = list(sig.parameters.keys())



def test_rcl::numericexpression_is_not_abstract():
    assert not inspect.isabstract(rcl::NumericExpression)


def test_rcl::numericexpression_constructor_exists():
    assert callable(rcl::NumericExpression.__init__)


def test_rcl::numericexpression_constructor_args():
    sig = inspect.signature(rcl::NumericExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rcl::numericexpression_has_op():
    assert hasattr(rcl::NumericExpression, "op")
    descriptor = None
    for klass in rcl::NumericExpression.__mro__:
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



def test_rcl::numbervalue_is_not_abstract():
    assert not inspect.isabstract(rcl::NumberValue)


def test_rcl::numbervalue_constructor_exists():
    assert callable(rcl::NumberValue.__init__)


def test_rcl::numbervalue_constructor_args():
    sig = inspect.signature(rcl::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "nValue" in params, "Missing parameter 'nValue'"

def test_rcl::numbervalue_has_nValue():
    assert hasattr(rcl::NumberValue, "nValue")
    descriptor = None
    for klass in rcl::NumberValue.__mro__:
        if "nValue" in klass.__dict__:
            descriptor = klass.__dict__["nValue"]
            break
    assert isinstance(descriptor, property)



def test_rcl::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(rcl::BooleanValue)


def test_rcl::booleanvalue_constructor_exists():
    assert callable(rcl::BooleanValue.__init__)


def test_rcl::booleanvalue_constructor_args():
    sig = inspect.signature(rcl::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "bValue" in params, "Missing parameter 'bValue'"

def test_rcl::booleanvalue_has_bValue():
    assert hasattr(rcl::BooleanValue, "bValue")
    descriptor = None
    for klass in rcl::BooleanValue.__mro__:
        if "bValue" in klass.__dict__:
            descriptor = klass.__dict__["bValue"]
            break
    assert isinstance(descriptor, property)



def test_rcl::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(rcl::BooleanExpression)


def test_rcl::booleanexpression_constructor_exists():
    assert callable(rcl::BooleanExpression.__init__)


def test_rcl::booleanexpression_constructor_args():
    sig = inspect.signature(rcl::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rcl::booleanexpression_has_op():
    assert hasattr(rcl::BooleanExpression, "op")
    descriptor = None
    for klass in rcl::BooleanExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rcl::stringvalue_is_not_abstract():
    assert not inspect.isabstract(rcl::StringValue)


def test_rcl::stringvalue_constructor_exists():
    assert callable(rcl::StringValue.__init__)


def test_rcl::stringvalue_constructor_args():
    sig = inspect.signature(rcl::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "sValue" in params, "Missing parameter 'sValue'"

def test_rcl::stringvalue_has_sValue():
    assert hasattr(rcl::StringValue, "sValue")
    descriptor = None
    for klass in rcl::StringValue.__mro__:
        if "sValue" in klass.__dict__:
            descriptor = klass.__dict__["sValue"]
            break
    assert isinstance(descriptor, property)



def test_rcl::stringexpression_is_not_abstract():
    assert not inspect.isabstract(rcl::StringExpression)


def test_rcl::stringexpression_constructor_exists():
    assert callable(rcl::StringExpression.__init__)


def test_rcl::stringexpression_constructor_args():
    sig = inspect.signature(rcl::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rcl::stringexpression_has_op():
    assert hasattr(rcl::StringExpression, "op")
    descriptor = None
    for klass in rcl::StringExpression.__mro__:
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



def test_rcl::action_is_not_abstract():
    assert not inspect.isabstract(rcl::Action)


def test_rcl::action_constructor_exists():
    assert callable(rcl::Action.__init__)


def test_rcl::action_constructor_args():
    sig = inspect.signature(rcl::Action.__init__)
    params = list(sig.parameters.keys())



def test_rcl::varassignment_is_not_abstract():
    assert not inspect.isabstract(rcl::VarAssignment)


def test_rcl::varassignment_constructor_exists():
    assert callable(rcl::VarAssignment.__init__)


def test_rcl::varassignment_constructor_args():
    sig = inspect.signature(rcl::VarAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl::varassignment_has_name():
    assert hasattr(rcl::VarAssignment, "name")
    descriptor = None
    for klass in rcl::VarAssignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rcl::statement_is_not_abstract():
    assert not inspect.isabstract(rcl::Statement)


def test_rcl::statement_constructor_exists():
    assert callable(rcl::Statement.__init__)


def test_rcl::statement_constructor_args():
    sig = inspect.signature(rcl::Statement.__init__)
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



def test_rcl::varref_is_not_abstract():
    assert not inspect.isabstract(rcl::VarRef)


def test_rcl::varref_constructor_exists():
    assert callable(rcl::VarRef.__init__)


def test_rcl::varref_constructor_args():
    sig = inspect.signature(rcl::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl::varref_has_name():
    assert hasattr(rcl::VarRef, "name")
    descriptor = None
    for klass in rcl::VarRef.__mro__:
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



def test_rcl::humidityquery_is_not_abstract():
    assert not inspect.isabstract(rcl::HumidityQuery)


def test_rcl::humidityquery_constructor_exists():
    assert callable(rcl::HumidityQuery.__init__)


def test_rcl::humidityquery_constructor_args():
    sig = inspect.signature(rcl::HumidityQuery.__init__)
    params = list(sig.parameters.keys())



def test_rcl::obstaclequery_is_not_abstract():
    assert not inspect.isabstract(rcl::ObstacleQuery)


def test_rcl::obstaclequery_constructor_exists():
    assert callable(rcl::ObstacleQuery.__init__)


def test_rcl::obstaclequery_constructor_args():
    sig = inspect.signature(rcl::ObstacleQuery.__init__)
    params = list(sig.parameters.keys())
    assert "front" in params, "Missing parameter 'front'"

def test_rcl::obstaclequery_has_front():
    assert hasattr(rcl::ObstacleQuery, "front")
    descriptor = None
    for klass in rcl::ObstacleQuery.__mro__:
        if "front" in klass.__dict__:
            descriptor = klass.__dict__["front"]
            break
    assert isinstance(descriptor, property)



def test_rcl::messagequery_is_not_abstract():
    assert not inspect.isabstract(rcl::MessageQuery)


def test_rcl::messagequery_constructor_exists():
    assert callable(rcl::MessageQuery.__init__)


def test_rcl::messagequery_constructor_args():
    sig = inspect.signature(rcl::MessageQuery.__init__)
    params = list(sig.parameters.keys())



def test_rcl::temperaturequery_is_not_abstract():
    assert not inspect.isabstract(rcl::TemperatureQuery)


def test_rcl::temperaturequery_constructor_exists():
    assert callable(rcl::TemperatureQuery.__init__)


def test_rcl::temperaturequery_constructor_args():
    sig = inspect.signature(rcl::TemperatureQuery.__init__)
    params = list(sig.parameters.keys())



def test_rcl::query_is_not_abstract():
    assert not inspect.isabstract(rcl::Query)


def test_rcl::query_constructor_exists():
    assert callable(rcl::Query.__init__)


def test_rcl::query_constructor_args():
    sig = inspect.signature(rcl::Query.__init__)
    params = list(sig.parameters.keys())



def test_rcl::loop_is_not_abstract():
    assert not inspect.isabstract(rcl::Loop)


def test_rcl::loop_constructor_exists():
    assert callable(rcl::Loop.__init__)


def test_rcl::loop_constructor_args():
    sig = inspect.signature(rcl::Loop.__init__)
    params = list(sig.parameters.keys())



def test_rcl::roverexpression_is_not_abstract():
    assert not inspect.isabstract(rcl::RoverExpression)


def test_rcl::roverexpression_constructor_exists():
    assert callable(rcl::RoverExpression.__init__)


def test_rcl::roverexpression_constructor_args():
    sig = inspect.signature(rcl::RoverExpression.__init__)
    params = list(sig.parameters.keys())



def test_rcl::conditional_is_not_abstract():
    assert not inspect.isabstract(rcl::Conditional)


def test_rcl::conditional_constructor_exists():
    assert callable(rcl::Conditional.__init__)


def test_rcl::conditional_constructor_args():
    sig = inspect.signature(rcl::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_rcl::rovervalue_is_not_abstract():
    assert not inspect.isabstract(rcl::RoverValue)


def test_rcl::rovervalue_constructor_exists():
    assert callable(rcl::RoverValue.__init__)


def test_rcl::rovervalue_constructor_args():
    sig = inspect.signature(rcl::RoverValue.__init__)
    params = list(sig.parameters.keys())



def test_rcl::rclblock_is_not_abstract():
    assert not inspect.isabstract(rcl::RclBlock)


def test_rcl::rclblock_constructor_exists():
    assert callable(rcl::RclBlock.__init__)


def test_rcl::rclblock_constructor_args():
    sig = inspect.signature(rcl::RclBlock.__init__)
    params = list(sig.parameters.keys())



def test_rcl::param_is_not_abstract():
    assert not inspect.isabstract(rcl::Param)


def test_rcl::param_constructor_exists():
    assert callable(rcl::Param.__init__)


def test_rcl::param_constructor_args():
    sig = inspect.signature(rcl::Param.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl::param_has_name():
    assert hasattr(rcl::Param, "name")
    descriptor = None
    for klass in rcl::Param.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rcl::roverprogram_is_not_abstract():
    assert not inspect.isabstract(rcl::RoverProgram)


def test_rcl::roverprogram_constructor_exists():
    assert callable(rcl::RoverProgram.__init__)


def test_rcl::roverprogram_constructor_args():
    sig = inspect.signature(rcl::RoverProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcl::roverprogram_has_name():
    assert hasattr(rcl::RoverProgram, "name")
    descriptor = None
    for klass in rcl::RoverProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_stringoperator_exists():
    # Check that the Enumeration exists
    assert StringOperator is not None

def test_stringoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringOperator]
    expected_literals = [
        "neq",
        "eq",
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

def test_numericoperator_exists():
    # Check that the Enumeration exists
    assert NumericOperator is not None

def test_numericoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericOperator]
    expected_literals = [
        "eq",
        "geq",
        "neq",
        "lt",
        "leq",
        "gt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericOperator"


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
Action_strategy = st.builds(
    Action,
)
rcl::ForwardMinAction_strategy = st.builds(
    rcl::ForwardMinAction,
)
rcl::ForwardAction_strategy = st.builds(
    rcl::ForwardAction,
)
rcl::SendAction_strategy = st.builds(
    rcl::SendAction,
    message=
        safe_text
)
rcl::LogAction_strategy = st.builds(
    rcl::LogAction,
    message=
        safe_text
)
rcl::StopAction_strategy = st.builds(
    rcl::StopAction,
)
rcl::TurnDegAction_strategy = st.builds(
    rcl::TurnDegAction,
)
rcl::TurnAction_strategy = st.builds(
    rcl::TurnAction,
)
rcl::BackwardMinAction_strategy = st.builds(
    rcl::BackwardMinAction,
)
rcl::BackwardAction_strategy = st.builds(
    rcl::BackwardAction,
)
RoverExpression_strategy = st.builds(
    RoverExpression,
)
rcl::NumericExpression_strategy = st.builds(
    rcl::NumericExpression,
    op=
        safe_text
)
RoverValue_strategy = st.builds(
    RoverValue,
)
rcl::NumberValue_strategy = st.builds(
    rcl::NumberValue,
    nValue=
        st.integers()
)
rcl::BooleanValue_strategy = st.builds(
    rcl::BooleanValue,
    bValue=
        st.booleans()
)
rcl::BooleanExpression_strategy = st.builds(
    rcl::BooleanExpression,
    op=
        safe_text
)
rcl::StringValue_strategy = st.builds(
    rcl::StringValue,
    sValue=
        safe_text
)
rcl::StringExpression_strategy = st.builds(
    rcl::StringExpression,
    op=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
rcl::Action_strategy = st.builds(
    rcl::Action,
)
rcl::VarAssignment_strategy = st.builds(
    rcl::VarAssignment,
    name=
        safe_text
)
rcl::Statement_strategy = st.builds(
    rcl::Statement,
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
rcl::VarRef_strategy = st.builds(
    rcl::VarRef,
    name=
        safe_text
)
Query_strategy = st.builds(
    Query,
)
rcl::HumidityQuery_strategy = st.builds(
    rcl::HumidityQuery,
)
rcl::ObstacleQuery_strategy = st.builds(
    rcl::ObstacleQuery,
    front=
        st.booleans()
)
rcl::MessageQuery_strategy = st.builds(
    rcl::MessageQuery,
)
rcl::TemperatureQuery_strategy = st.builds(
    rcl::TemperatureQuery,
)
rcl::Query_strategy = st.builds(
    rcl::Query,
)
rcl::Loop_strategy = st.builds(
    rcl::Loop,
)
rcl::RoverExpression_strategy = st.builds(
    rcl::RoverExpression,
)
rcl::Conditional_strategy = st.builds(
    rcl::Conditional,
)
rcl::RoverValue_strategy = st.builds(
    rcl::RoverValue,
)
rcl::RclBlock_strategy = st.builds(
    rcl::RclBlock,
)
rcl::Param_strategy = st.builds(
    rcl::Param,
    name=
        safe_text
)
rcl::RoverProgram_strategy = st.builds(
    rcl::RoverProgram,
    name=
        safe_text
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=rcl::ForwardMinAction_strategy)
@settings(max_examples=50)
def test_rcl::forwardminaction_instantiation(instance):
    assert isinstance(instance, rcl::ForwardMinAction)

@given(instance=rcl::ForwardAction_strategy)
@settings(max_examples=50)
def test_rcl::forwardaction_instantiation(instance):
    assert isinstance(instance, rcl::ForwardAction)

@given(instance=rcl::SendAction_strategy)
@settings(max_examples=50)
def test_rcl::sendaction_instantiation(instance):
    assert isinstance(instance, rcl::SendAction)

@given(instance=rcl::SendAction_strategy)
def test_rcl::sendaction_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=rcl::SendAction_strategy)
def test_rcl::sendaction_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=rcl::LogAction_strategy)
@settings(max_examples=50)
def test_rcl::logaction_instantiation(instance):
    assert isinstance(instance, rcl::LogAction)

@given(instance=rcl::LogAction_strategy)
def test_rcl::logaction_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=rcl::LogAction_strategy)
def test_rcl::logaction_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=rcl::StopAction_strategy)
@settings(max_examples=50)
def test_rcl::stopaction_instantiation(instance):
    assert isinstance(instance, rcl::StopAction)

@given(instance=rcl::TurnDegAction_strategy)
@settings(max_examples=50)
def test_rcl::turndegaction_instantiation(instance):
    assert isinstance(instance, rcl::TurnDegAction)

@given(instance=rcl::TurnAction_strategy)
@settings(max_examples=50)
def test_rcl::turnaction_instantiation(instance):
    assert isinstance(instance, rcl::TurnAction)

@given(instance=rcl::BackwardMinAction_strategy)
@settings(max_examples=50)
def test_rcl::backwardminaction_instantiation(instance):
    assert isinstance(instance, rcl::BackwardMinAction)

@given(instance=rcl::BackwardAction_strategy)
@settings(max_examples=50)
def test_rcl::backwardaction_instantiation(instance):
    assert isinstance(instance, rcl::BackwardAction)

@given(instance=RoverExpression_strategy)
@settings(max_examples=50)
def test_roverexpression_instantiation(instance):
    assert isinstance(instance, RoverExpression)

@given(instance=rcl::NumericExpression_strategy)
@settings(max_examples=50)
def test_rcl::numericexpression_instantiation(instance):
    assert isinstance(instance, rcl::NumericExpression)

@given(instance=rcl::NumericExpression_strategy)
def test_rcl::numericexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=rcl::NumericExpression_strategy)
def test_rcl::numericexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=RoverValue_strategy)
@settings(max_examples=50)
def test_rovervalue_instantiation(instance):
    assert isinstance(instance, RoverValue)

@given(instance=rcl::NumberValue_strategy)
@settings(max_examples=50)
def test_rcl::numbervalue_instantiation(instance):
    assert isinstance(instance, rcl::NumberValue)

@given(instance=rcl::NumberValue_strategy)
def test_rcl::numbervalue_nValue_type(instance):
    assert isinstance(instance.nValue, int)


@given(instance=rcl::NumberValue_strategy)
def test_rcl::numbervalue_nValue_setter(instance):
    original = instance.nValue
    instance.nValue = original
    assert instance.nValue == original

@given(instance=rcl::BooleanValue_strategy)
@settings(max_examples=50)
def test_rcl::booleanvalue_instantiation(instance):
    assert isinstance(instance, rcl::BooleanValue)

@given(instance=rcl::BooleanValue_strategy)
def test_rcl::booleanvalue_bValue_type(instance):
    assert isinstance(instance.bValue, bool)


@given(instance=rcl::BooleanValue_strategy)
def test_rcl::booleanvalue_bValue_setter(instance):
    original = instance.bValue
    instance.bValue = original
    assert instance.bValue == original

@given(instance=rcl::BooleanExpression_strategy)
@settings(max_examples=50)
def test_rcl::booleanexpression_instantiation(instance):
    assert isinstance(instance, rcl::BooleanExpression)

@given(instance=rcl::BooleanExpression_strategy)
def test_rcl::booleanexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=rcl::BooleanExpression_strategy)
def test_rcl::booleanexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rcl::StringValue_strategy)
@settings(max_examples=50)
def test_rcl::stringvalue_instantiation(instance):
    assert isinstance(instance, rcl::StringValue)

@given(instance=rcl::StringValue_strategy)
def test_rcl::stringvalue_sValue_type(instance):
    assert isinstance(instance.sValue, str)


@given(instance=rcl::StringValue_strategy)
def test_rcl::stringvalue_sValue_setter(instance):
    original = instance.sValue
    instance.sValue = original
    assert instance.sValue == original

@given(instance=rcl::StringExpression_strategy)
@settings(max_examples=50)
def test_rcl::stringexpression_instantiation(instance):
    assert isinstance(instance, rcl::StringExpression)

@given(instance=rcl::StringExpression_strategy)
def test_rcl::stringexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=rcl::StringExpression_strategy)
def test_rcl::stringexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=rcl::Action_strategy)
@settings(max_examples=50)
def test_rcl::action_instantiation(instance):
    assert isinstance(instance, rcl::Action)

@given(instance=rcl::VarAssignment_strategy)
@settings(max_examples=50)
def test_rcl::varassignment_instantiation(instance):
    assert isinstance(instance, rcl::VarAssignment)

@given(instance=rcl::VarAssignment_strategy)
def test_rcl::varassignment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcl::VarAssignment_strategy)
def test_rcl::varassignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rcl::Statement_strategy)
@settings(max_examples=50)
def test_rcl::statement_instantiation(instance):
    assert isinstance(instance, rcl::Statement)

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

@given(instance=rcl::VarRef_strategy)
@settings(max_examples=50)
def test_rcl::varref_instantiation(instance):
    assert isinstance(instance, rcl::VarRef)

@given(instance=rcl::VarRef_strategy)
def test_rcl::varref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcl::VarRef_strategy)
def test_rcl::varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=rcl::HumidityQuery_strategy)
@settings(max_examples=50)
def test_rcl::humidityquery_instantiation(instance):
    assert isinstance(instance, rcl::HumidityQuery)

@given(instance=rcl::ObstacleQuery_strategy)
@settings(max_examples=50)
def test_rcl::obstaclequery_instantiation(instance):
    assert isinstance(instance, rcl::ObstacleQuery)

@given(instance=rcl::ObstacleQuery_strategy)
def test_rcl::obstaclequery_front_type(instance):
    assert isinstance(instance.front, bool)


@given(instance=rcl::ObstacleQuery_strategy)
def test_rcl::obstaclequery_front_setter(instance):
    original = instance.front
    instance.front = original
    assert instance.front == original

@given(instance=rcl::MessageQuery_strategy)
@settings(max_examples=50)
def test_rcl::messagequery_instantiation(instance):
    assert isinstance(instance, rcl::MessageQuery)

@given(instance=rcl::TemperatureQuery_strategy)
@settings(max_examples=50)
def test_rcl::temperaturequery_instantiation(instance):
    assert isinstance(instance, rcl::TemperatureQuery)

@given(instance=rcl::Query_strategy)
@settings(max_examples=50)
def test_rcl::query_instantiation(instance):
    assert isinstance(instance, rcl::Query)

@given(instance=rcl::Loop_strategy)
@settings(max_examples=50)
def test_rcl::loop_instantiation(instance):
    assert isinstance(instance, rcl::Loop)

@given(instance=rcl::RoverExpression_strategy)
@settings(max_examples=50)
def test_rcl::roverexpression_instantiation(instance):
    assert isinstance(instance, rcl::RoverExpression)

@given(instance=rcl::Conditional_strategy)
@settings(max_examples=50)
def test_rcl::conditional_instantiation(instance):
    assert isinstance(instance, rcl::Conditional)

@given(instance=rcl::RoverValue_strategy)
@settings(max_examples=50)
def test_rcl::rovervalue_instantiation(instance):
    assert isinstance(instance, rcl::RoverValue)

@given(instance=rcl::RclBlock_strategy)
@settings(max_examples=50)
def test_rcl::rclblock_instantiation(instance):
    assert isinstance(instance, rcl::RclBlock)

@given(instance=rcl::Param_strategy)
@settings(max_examples=50)
def test_rcl::param_instantiation(instance):
    assert isinstance(instance, rcl::Param)

@given(instance=rcl::Param_strategy)
def test_rcl::param_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcl::Param_strategy)
def test_rcl::param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rcl::RoverProgram_strategy)
@settings(max_examples=50)
def test_rcl::roverprogram_instantiation(instance):
    assert isinstance(instance, rcl::RoverProgram)

@given(instance=rcl::RoverProgram_strategy)
def test_rcl::roverprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcl::RoverProgram_strategy)
def test_rcl::roverprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    minilang::Program,
    Statement,
    minilang::IfStmt,
    minilang::Statement,
    minilang::RotateLeft,
    minilang::RotateRight,
    minilang::Move,
    minilang::CallMethod,
    BinaryOperation,
    minilang::Modulo,
    minilang::Sum,
    minilang::VariableAffect,
    Value,
    minilang::VariableRef,
    minilang::BinaryOperation,
    minilang::Constant,
    minilang::Value,
    Condition,
    minilang::GreaterThan,
    minilang::Condition,
    minilang::Block,
    minilang::Line,
    minilang::Variable,
    minilang::Method,
    Cardinals,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minilang::program_is_not_abstract():
    assert not inspect.isabstract(minilang::Program)


def test_minilang::program_constructor_exists():
    assert callable(minilang::Program.__init__)


def test_minilang::program_constructor_args():
    sig = inspect.signature(minilang::Program.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "angle" in params, "Missing parameter 'angle'"
    assert "distance" in params, "Missing parameter 'distance'"

def test_minilang::program_has_y():
    assert hasattr(minilang::Program, "y")
    descriptor = None
    for klass in minilang::Program.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_minilang::program_has_x():
    assert hasattr(minilang::Program, "x")
    descriptor = None
    for klass in minilang::Program.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_minilang::program_has_angle():
    assert hasattr(minilang::Program, "angle")
    descriptor = None
    for klass in minilang::Program.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)

def test_minilang::program_has_distance():
    assert hasattr(minilang::Program, "distance")
    descriptor = None
    for klass in minilang::Program.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_minilang::ifstmt_is_not_abstract():
    assert not inspect.isabstract(minilang::IfStmt)


def test_minilang::ifstmt_constructor_exists():
    assert callable(minilang::IfStmt.__init__)


def test_minilang::ifstmt_constructor_args():
    sig = inspect.signature(minilang::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_minilang::statement_is_not_abstract():
    assert not inspect.isabstract(minilang::Statement)


def test_minilang::statement_constructor_exists():
    assert callable(minilang::Statement.__init__)


def test_minilang::statement_constructor_args():
    sig = inspect.signature(minilang::Statement.__init__)
    params = list(sig.parameters.keys())



def test_minilang::rotateleft_is_not_abstract():
    assert not inspect.isabstract(minilang::RotateLeft)


def test_minilang::rotateleft_constructor_exists():
    assert callable(minilang::RotateLeft.__init__)


def test_minilang::rotateleft_constructor_args():
    sig = inspect.signature(minilang::RotateLeft.__init__)
    params = list(sig.parameters.keys())



def test_minilang::rotateright_is_not_abstract():
    assert not inspect.isabstract(minilang::RotateRight)


def test_minilang::rotateright_constructor_exists():
    assert callable(minilang::RotateRight.__init__)


def test_minilang::rotateright_constructor_args():
    sig = inspect.signature(minilang::RotateRight.__init__)
    params = list(sig.parameters.keys())



def test_minilang::move_is_not_abstract():
    assert not inspect.isabstract(minilang::Move)


def test_minilang::move_constructor_exists():
    assert callable(minilang::Move.__init__)


def test_minilang::move_constructor_args():
    sig = inspect.signature(minilang::Move.__init__)
    params = list(sig.parameters.keys())



def test_minilang::callmethod_is_not_abstract():
    assert not inspect.isabstract(minilang::CallMethod)


def test_minilang::callmethod_constructor_exists():
    assert callable(minilang::CallMethod.__init__)


def test_minilang::callmethod_constructor_args():
    sig = inspect.signature(minilang::CallMethod.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(BinaryOperation)


def test_binaryoperation_constructor_exists():
    assert callable(BinaryOperation.__init__)


def test_binaryoperation_constructor_args():
    sig = inspect.signature(BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_minilang::modulo_is_not_abstract():
    assert not inspect.isabstract(minilang::Modulo)


def test_minilang::modulo_constructor_exists():
    assert callable(minilang::Modulo.__init__)


def test_minilang::modulo_constructor_args():
    sig = inspect.signature(minilang::Modulo.__init__)
    params = list(sig.parameters.keys())



def test_minilang::sum_is_not_abstract():
    assert not inspect.isabstract(minilang::Sum)


def test_minilang::sum_constructor_exists():
    assert callable(minilang::Sum.__init__)


def test_minilang::sum_constructor_args():
    sig = inspect.signature(minilang::Sum.__init__)
    params = list(sig.parameters.keys())



def test_minilang::variableaffect_is_not_abstract():
    assert not inspect.isabstract(minilang::VariableAffect)


def test_minilang::variableaffect_constructor_exists():
    assert callable(minilang::VariableAffect.__init__)


def test_minilang::variableaffect_constructor_args():
    sig = inspect.signature(minilang::VariableAffect.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_minilang::variableref_is_not_abstract():
    assert not inspect.isabstract(minilang::VariableRef)


def test_minilang::variableref_constructor_exists():
    assert callable(minilang::VariableRef.__init__)


def test_minilang::variableref_constructor_args():
    sig = inspect.signature(minilang::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_minilang::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(minilang::BinaryOperation)


def test_minilang::binaryoperation_constructor_exists():
    assert callable(minilang::BinaryOperation.__init__)


def test_minilang::binaryoperation_constructor_args():
    sig = inspect.signature(minilang::BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_minilang::constant_is_not_abstract():
    assert not inspect.isabstract(minilang::Constant)


def test_minilang::constant_constructor_exists():
    assert callable(minilang::Constant.__init__)


def test_minilang::constant_constructor_args():
    sig = inspect.signature(minilang::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minilang::constant_has_value():
    assert hasattr(minilang::Constant, "value")
    descriptor = None
    for klass in minilang::Constant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minilang::value_is_not_abstract():
    assert not inspect.isabstract(minilang::Value)


def test_minilang::value_constructor_exists():
    assert callable(minilang::Value.__init__)


def test_minilang::value_constructor_args():
    sig = inspect.signature(minilang::Value.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_minilang::greaterthan_is_not_abstract():
    assert not inspect.isabstract(minilang::GreaterThan)


def test_minilang::greaterthan_constructor_exists():
    assert callable(minilang::GreaterThan.__init__)


def test_minilang::greaterthan_constructor_args():
    sig = inspect.signature(minilang::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_minilang::condition_is_not_abstract():
    assert not inspect.isabstract(minilang::Condition)


def test_minilang::condition_constructor_exists():
    assert callable(minilang::Condition.__init__)


def test_minilang::condition_constructor_args():
    sig = inspect.signature(minilang::Condition.__init__)
    params = list(sig.parameters.keys())



def test_minilang::block_is_not_abstract():
    assert not inspect.isabstract(minilang::Block)


def test_minilang::block_constructor_exists():
    assert callable(minilang::Block.__init__)


def test_minilang::block_constructor_args():
    sig = inspect.signature(minilang::Block.__init__)
    params = list(sig.parameters.keys())



def test_minilang::line_is_not_abstract():
    assert not inspect.isabstract(minilang::Line)


def test_minilang::line_constructor_exists():
    assert callable(minilang::Line.__init__)


def test_minilang::line_constructor_args():
    sig = inspect.signature(minilang::Line.__init__)
    params = list(sig.parameters.keys())
    assert "y2" in params, "Missing parameter 'y2'"
    assert "y1" in params, "Missing parameter 'y1'"
    assert "x1" in params, "Missing parameter 'x1'"
    assert "x2" in params, "Missing parameter 'x2'"

def test_minilang::line_has_y2():
    assert hasattr(minilang::Line, "y2")
    descriptor = None
    for klass in minilang::Line.__mro__:
        if "y2" in klass.__dict__:
            descriptor = klass.__dict__["y2"]
            break
    assert isinstance(descriptor, property)

def test_minilang::line_has_y1():
    assert hasattr(minilang::Line, "y1")
    descriptor = None
    for klass in minilang::Line.__mro__:
        if "y1" in klass.__dict__:
            descriptor = klass.__dict__["y1"]
            break
    assert isinstance(descriptor, property)

def test_minilang::line_has_x1():
    assert hasattr(minilang::Line, "x1")
    descriptor = None
    for klass in minilang::Line.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_minilang::line_has_x2():
    assert hasattr(minilang::Line, "x2")
    descriptor = None
    for klass in minilang::Line.__mro__:
        if "x2" in klass.__dict__:
            descriptor = klass.__dict__["x2"]
            break
    assert isinstance(descriptor, property)



def test_minilang::variable_is_not_abstract():
    assert not inspect.isabstract(minilang::Variable)


def test_minilang::variable_constructor_exists():
    assert callable(minilang::Variable.__init__)


def test_minilang::variable_constructor_args():
    sig = inspect.signature(minilang::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_minilang::variable_has_value():
    assert hasattr(minilang::Variable, "value")
    descriptor = None
    for klass in minilang::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_minilang::variable_has_name():
    assert hasattr(minilang::Variable, "name")
    descriptor = None
    for klass in minilang::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minilang::method_is_not_abstract():
    assert not inspect.isabstract(minilang::Method)


def test_minilang::method_constructor_exists():
    assert callable(minilang::Method.__init__)


def test_minilang::method_constructor_args():
    sig = inspect.signature(minilang::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minilang::method_has_name():
    assert hasattr(minilang::Method, "name")
    descriptor = None
    for klass in minilang::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cardinals_exists():
    # Check that the Enumeration exists
    assert Cardinals is not None

def test_cardinals_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinals]
    expected_literals = [
        "WEST",
        "SOUTH",
        "EAST",
        "NORTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cardinals"


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
minilang::Program_strategy = st.builds(
    minilang::Program,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    angle=
        safe_text,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Statement_strategy = st.builds(
    Statement,
)
minilang::IfStmt_strategy = st.builds(
    minilang::IfStmt,
)
minilang::Statement_strategy = st.builds(
    minilang::Statement,
)
minilang::RotateLeft_strategy = st.builds(
    minilang::RotateLeft,
)
minilang::RotateRight_strategy = st.builds(
    minilang::RotateRight,
)
minilang::Move_strategy = st.builds(
    minilang::Move,
)
minilang::CallMethod_strategy = st.builds(
    minilang::CallMethod,
)
BinaryOperation_strategy = st.builds(
    BinaryOperation,
)
minilang::Modulo_strategy = st.builds(
    minilang::Modulo,
)
minilang::Sum_strategy = st.builds(
    minilang::Sum,
)
minilang::VariableAffect_strategy = st.builds(
    minilang::VariableAffect,
)
Value_strategy = st.builds(
    Value,
)
minilang::VariableRef_strategy = st.builds(
    minilang::VariableRef,
)
minilang::BinaryOperation_strategy = st.builds(
    minilang::BinaryOperation,
)
minilang::Constant_strategy = st.builds(
    minilang::Constant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
minilang::Value_strategy = st.builds(
    minilang::Value,
)
Condition_strategy = st.builds(
    Condition,
)
minilang::GreaterThan_strategy = st.builds(
    minilang::GreaterThan,
)
minilang::Condition_strategy = st.builds(
    minilang::Condition,
)
minilang::Block_strategy = st.builds(
    minilang::Block,
)
minilang::Line_strategy = st.builds(
    minilang::Line,
    y2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
minilang::Variable_strategy = st.builds(
    minilang::Variable,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
minilang::Method_strategy = st.builds(
    minilang::Method,
    name=
        safe_text
)

@given(instance=minilang::Program_strategy)
@settings(max_examples=50)
def test_minilang::program_instantiation(instance):
    assert isinstance(instance, minilang::Program)

@given(instance=minilang::Program_strategy)
def test_minilang::program_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=minilang::Program_strategy)
def test_minilang::program_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=minilang::Program_strategy)
def test_minilang::program_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=minilang::Program_strategy)
def test_minilang::program_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=minilang::Program_strategy)
def test_minilang::program_angle_type(instance):
    assert isinstance(instance.angle, str)


@given(instance=minilang::Program_strategy)
def test_minilang::program_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=minilang::Program_strategy)
def test_minilang::program_distance_type(instance):
    assert isinstance(instance.distance, float)


@given(instance=minilang::Program_strategy)
def test_minilang::program_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=minilang::IfStmt_strategy)
@settings(max_examples=50)
def test_minilang::ifstmt_instantiation(instance):
    assert isinstance(instance, minilang::IfStmt)

@given(instance=minilang::Statement_strategy)
@settings(max_examples=50)
def test_minilang::statement_instantiation(instance):
    assert isinstance(instance, minilang::Statement)

@given(instance=minilang::RotateLeft_strategy)
@settings(max_examples=50)
def test_minilang::rotateleft_instantiation(instance):
    assert isinstance(instance, minilang::RotateLeft)

@given(instance=minilang::RotateRight_strategy)
@settings(max_examples=50)
def test_minilang::rotateright_instantiation(instance):
    assert isinstance(instance, minilang::RotateRight)

@given(instance=minilang::Move_strategy)
@settings(max_examples=50)
def test_minilang::move_instantiation(instance):
    assert isinstance(instance, minilang::Move)

@given(instance=minilang::CallMethod_strategy)
@settings(max_examples=50)
def test_minilang::callmethod_instantiation(instance):
    assert isinstance(instance, minilang::CallMethod)

@given(instance=BinaryOperation_strategy)
@settings(max_examples=50)
def test_binaryoperation_instantiation(instance):
    assert isinstance(instance, BinaryOperation)

@given(instance=minilang::Modulo_strategy)
@settings(max_examples=50)
def test_minilang::modulo_instantiation(instance):
    assert isinstance(instance, minilang::Modulo)

@given(instance=minilang::Sum_strategy)
@settings(max_examples=50)
def test_minilang::sum_instantiation(instance):
    assert isinstance(instance, minilang::Sum)

@given(instance=minilang::VariableAffect_strategy)
@settings(max_examples=50)
def test_minilang::variableaffect_instantiation(instance):
    assert isinstance(instance, minilang::VariableAffect)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=minilang::VariableRef_strategy)
@settings(max_examples=50)
def test_minilang::variableref_instantiation(instance):
    assert isinstance(instance, minilang::VariableRef)

@given(instance=minilang::BinaryOperation_strategy)
@settings(max_examples=50)
def test_minilang::binaryoperation_instantiation(instance):
    assert isinstance(instance, minilang::BinaryOperation)

@given(instance=minilang::Constant_strategy)
@settings(max_examples=50)
def test_minilang::constant_instantiation(instance):
    assert isinstance(instance, minilang::Constant)

@given(instance=minilang::Constant_strategy)
def test_minilang::constant_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=minilang::Constant_strategy)
def test_minilang::constant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=minilang::Value_strategy)
@settings(max_examples=50)
def test_minilang::value_instantiation(instance):
    assert isinstance(instance, minilang::Value)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=minilang::GreaterThan_strategy)
@settings(max_examples=50)
def test_minilang::greaterthan_instantiation(instance):
    assert isinstance(instance, minilang::GreaterThan)

@given(instance=minilang::Condition_strategy)
@settings(max_examples=50)
def test_minilang::condition_instantiation(instance):
    assert isinstance(instance, minilang::Condition)

@given(instance=minilang::Block_strategy)
@settings(max_examples=50)
def test_minilang::block_instantiation(instance):
    assert isinstance(instance, minilang::Block)

@given(instance=minilang::Line_strategy)
@settings(max_examples=50)
def test_minilang::line_instantiation(instance):
    assert isinstance(instance, minilang::Line)

@given(instance=minilang::Line_strategy)
def test_minilang::line_y2_type(instance):
    assert isinstance(instance.y2, float)


@given(instance=minilang::Line_strategy)
def test_minilang::line_y2_setter(instance):
    original = instance.y2
    instance.y2 = original
    assert instance.y2 == original

@given(instance=minilang::Line_strategy)
def test_minilang::line_y1_type(instance):
    assert isinstance(instance.y1, float)


@given(instance=minilang::Line_strategy)
def test_minilang::line_y1_setter(instance):
    original = instance.y1
    instance.y1 = original
    assert instance.y1 == original

@given(instance=minilang::Line_strategy)
def test_minilang::line_x1_type(instance):
    assert isinstance(instance.x1, float)


@given(instance=minilang::Line_strategy)
def test_minilang::line_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original

@given(instance=minilang::Line_strategy)
def test_minilang::line_x2_type(instance):
    assert isinstance(instance.x2, float)


@given(instance=minilang::Line_strategy)
def test_minilang::line_x2_setter(instance):
    original = instance.x2
    instance.x2 = original
    assert instance.x2 == original

@given(instance=minilang::Variable_strategy)
@settings(max_examples=50)
def test_minilang::variable_instantiation(instance):
    assert isinstance(instance, minilang::Variable)

@given(instance=minilang::Variable_strategy)
def test_minilang::variable_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=minilang::Variable_strategy)
def test_minilang::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=minilang::Variable_strategy)
def test_minilang::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minilang::Variable_strategy)
def test_minilang::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minilang::Method_strategy)
@settings(max_examples=50)
def test_minilang::method_instantiation(instance):
    assert isinstance(instance, minilang::Method)

@given(instance=minilang::Method_strategy)
def test_minilang::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minilang::Method_strategy)
def test_minilang::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

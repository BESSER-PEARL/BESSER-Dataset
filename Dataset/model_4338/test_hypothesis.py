import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    ast::Operand,
    ast::Operator,
    ast::Expression,
    Operand,
    ast::Number,
    ast::Variable,
    ast::Model,
    ArithmeticOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast::operand_is_not_abstract():
    assert not inspect.isabstract(ast::Operand)


def test_ast::operand_constructor_exists():
    assert callable(ast::Operand.__init__)


def test_ast::operand_constructor_args():
    sig = inspect.signature(ast::Operand.__init__)
    params = list(sig.parameters.keys())



def test_ast::operator_is_not_abstract():
    assert not inspect.isabstract(ast::Operator)


def test_ast::operator_constructor_exists():
    assert callable(ast::Operator.__init__)


def test_ast::operator_constructor_args():
    sig = inspect.signature(ast::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_ast::operator_has_op():
    assert hasattr(ast::Operator, "op")
    descriptor = None
    for klass in ast::Operator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_ast::expression_is_not_abstract():
    assert not inspect.isabstract(ast::Expression)


def test_ast::expression_constructor_exists():
    assert callable(ast::Expression.__init__)


def test_ast::expression_constructor_args():
    sig = inspect.signature(ast::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"

def test_ast::expression_has_incrementalID():
    assert hasattr(ast::Expression, "incrementalID")
    descriptor = None
    for klass in ast::Expression.__mro__:
        if "incrementalID" in klass.__dict__:
            descriptor = klass.__dict__["incrementalID"]
            break
    assert isinstance(descriptor, property)



def test_operand_is_not_abstract():
    assert not inspect.isabstract(Operand)


def test_operand_constructor_exists():
    assert callable(Operand.__init__)


def test_operand_constructor_args():
    sig = inspect.signature(Operand.__init__)
    params = list(sig.parameters.keys())



def test_ast::number_is_not_abstract():
    assert not inspect.isabstract(ast::Number)


def test_ast::number_constructor_exists():
    assert callable(ast::Number.__init__)


def test_ast::number_constructor_args():
    sig = inspect.signature(ast::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast::number_has_value():
    assert hasattr(ast::Number, "value")
    descriptor = None
    for klass in ast::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast::variable_is_not_abstract():
    assert not inspect.isabstract(ast::Variable)


def test_ast::variable_constructor_exists():
    assert callable(ast::Variable.__init__)


def test_ast::variable_constructor_args():
    sig = inspect.signature(ast::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::variable_has_name():
    assert hasattr(ast::Variable, "name")
    descriptor = None
    for klass in ast::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::model_is_not_abstract():
    assert not inspect.isabstract(ast::Model)


def test_ast::model_constructor_exists():
    assert callable(ast::Model.__init__)


def test_ast::model_constructor_args():
    sig = inspect.signature(ast::Model.__init__)
    params = list(sig.parameters.keys())

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "Multiply",
        "Subtract",
        "Add",
        "Divide",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"


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
Expression_strategy = st.builds(
    Expression,
)
ast::Operand_strategy = st.builds(
    ast::Operand,
)
ast::Operator_strategy = st.builds(
    ast::Operator,
    op=
        safe_text
)
ast::Expression_strategy = st.builds(
    ast::Expression,
    incrementalID=
        safe_text
)
Operand_strategy = st.builds(
    Operand,
)
ast::Number_strategy = st.builds(
    ast::Number,
    value=
        st.integers()
)
ast::Variable_strategy = st.builds(
    ast::Variable,
    name=
        safe_text
)
ast::Model_strategy = st.builds(
    ast::Model,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ast::Operand_strategy)
@settings(max_examples=50)
def test_ast::operand_instantiation(instance):
    assert isinstance(instance, ast::Operand)

@given(instance=ast::Operator_strategy)
@settings(max_examples=50)
def test_ast::operator_instantiation(instance):
    assert isinstance(instance, ast::Operator)

@given(instance=ast::Operator_strategy)
def test_ast::operator_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=ast::Operator_strategy)
def test_ast::operator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ast::Expression_strategy)
@settings(max_examples=50)
def test_ast::expression_instantiation(instance):
    assert isinstance(instance, ast::Expression)

@given(instance=ast::Expression_strategy)
def test_ast::expression_incrementalID_type(instance):
    assert isinstance(instance.incrementalID, str)


@given(instance=ast::Expression_strategy)
def test_ast::expression_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original

@given(instance=Operand_strategy)
@settings(max_examples=50)
def test_operand_instantiation(instance):
    assert isinstance(instance, Operand)

@given(instance=ast::Number_strategy)
@settings(max_examples=50)
def test_ast::number_instantiation(instance):
    assert isinstance(instance, ast::Number)

@given(instance=ast::Number_strategy)
def test_ast::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ast::Number_strategy)
def test_ast::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast::Variable_strategy)
@settings(max_examples=50)
def test_ast::variable_instantiation(instance):
    assert isinstance(instance, ast::Variable)

@given(instance=ast::Variable_strategy)
def test_ast::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::Variable_strategy)
def test_ast::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::Model_strategy)
@settings(max_examples=50)
def test_ast::model_instantiation(instance):
    assert isinstance(instance, ast::Model)

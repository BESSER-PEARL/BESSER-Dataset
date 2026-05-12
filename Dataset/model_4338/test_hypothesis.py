import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    ast_Operand,
    ast_Operator,
    ast_Expression,
    Operand,
    ast_Number,
    ast_Variable,
    ast_Model,
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



def test_ast_operand_is_not_abstract():
    assert not inspect.isabstract(ast_Operand)


def test_ast_operand_constructor_exists():
    assert callable(ast_Operand.__init__)


def test_ast_operand_constructor_args():
    sig = inspect.signature(ast_Operand.__init__)
    params = list(sig.parameters.keys())



def test_ast_operator_is_not_abstract():
    assert not inspect.isabstract(ast_Operator)


def test_ast_operator_constructor_exists():
    assert callable(ast_Operator.__init__)


def test_ast_operator_constructor_args():
    sig = inspect.signature(ast_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_ast_operator_has_op():
    assert hasattr(ast_Operator, "op")
    descriptor = None
    for klass in ast_Operator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_ast_expression_is_not_abstract():
    assert not inspect.isabstract(ast_Expression)


def test_ast_expression_constructor_exists():
    assert callable(ast_Expression.__init__)


def test_ast_expression_constructor_args():
    sig = inspect.signature(ast_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"

def test_ast_expression_has_incrementalID():
    assert hasattr(ast_Expression, "incrementalID")
    descriptor = None
    for klass in ast_Expression.__mro__:
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



def test_ast_number_is_not_abstract():
    assert not inspect.isabstract(ast_Number)


def test_ast_number_constructor_exists():
    assert callable(ast_Number.__init__)


def test_ast_number_constructor_args():
    sig = inspect.signature(ast_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast_number_has_value():
    assert hasattr(ast_Number, "value")
    descriptor = None
    for klass in ast_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast_variable_is_not_abstract():
    assert not inspect.isabstract(ast_Variable)


def test_ast_variable_constructor_exists():
    assert callable(ast_Variable.__init__)


def test_ast_variable_constructor_args():
    sig = inspect.signature(ast_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_variable_has_name():
    assert hasattr(ast_Variable, "name")
    descriptor = None
    for klass in ast_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_model_is_not_abstract():
    assert not inspect.isabstract(ast_Model)


def test_ast_model_constructor_exists():
    assert callable(ast_Model.__init__)


def test_ast_model_constructor_args():
    sig = inspect.signature(ast_Model.__init__)
    params = list(sig.parameters.keys())

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "Multiply",
        "Divide",
        "Subtract",
        "Add",
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
ast_Operand_strategy = st.builds(
    ast_Operand,
)
ast_Operator_strategy = st.builds(
    ast_Operator,
    op=
        safe_text
)
ast_Expression_strategy = st.builds(
    ast_Expression,
    incrementalID=
        safe_text
)
Operand_strategy = st.builds(
    Operand,
)
ast_Number_strategy = st.builds(
    ast_Number,
    value=
        st.integers()
)
ast_Variable_strategy = st.builds(
    ast_Variable,
    name=
        safe_text
)
ast_Model_strategy = st.builds(
    ast_Model,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ast_Operand_strategy)
@settings(max_examples=50)
def test_ast_operand_instantiation(instance):
    assert isinstance(instance, ast_Operand)

@given(instance=ast_Operator_strategy)
@settings(max_examples=50)
def test_ast_operator_instantiation(instance):
    assert isinstance(instance, ast_Operator)



@given(instance=ast_Operator_strategy)
def test_ast_operator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ast_Expression_strategy)
@settings(max_examples=50)
def test_ast_expression_instantiation(instance):
    assert isinstance(instance, ast_Expression)



@given(instance=ast_Expression_strategy)
def test_ast_expression_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original

@given(instance=Operand_strategy)
@settings(max_examples=50)
def test_operand_instantiation(instance):
    assert isinstance(instance, Operand)

@given(instance=ast_Number_strategy)
@settings(max_examples=50)
def test_ast_number_instantiation(instance):
    assert isinstance(instance, ast_Number)



@given(instance=ast_Number_strategy)
def test_ast_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast_Variable_strategy)
@settings(max_examples=50)
def test_ast_variable_instantiation(instance):
    assert isinstance(instance, ast_Variable)



@given(instance=ast_Variable_strategy)
def test_ast_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_Model_strategy)
@settings(max_examples=50)
def test_ast_model_instantiation(instance):
    assert isinstance(instance, ast_Model)

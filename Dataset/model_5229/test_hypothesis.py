import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryExpression,
    ilp::ArithmeticExpression,
    ilp::Expression,
    ilp::ObjectiveFunctionExpression,
    ilp::ConstraintExpression,
    ilp::Variable,
    Expression,
    ilp::BinaryExpression,
    ilp::VariableExpression,
    ilp::LiteralExpression,
    ilp::IntegerLinearProgram,
    ILPDataType,
    ObjectiveGoal,
    Operator,
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



def test_ilp::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ilp::ArithmeticExpression)


def test_ilp::arithmeticexpression_constructor_exists():
    assert callable(ilp::ArithmeticExpression.__init__)


def test_ilp::arithmeticexpression_constructor_args():
    sig = inspect.signature(ilp::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ilp::expression_is_not_abstract():
    assert not inspect.isabstract(ilp::Expression)


def test_ilp::expression_constructor_exists():
    assert callable(ilp::Expression.__init__)


def test_ilp::expression_constructor_args():
    sig = inspect.signature(ilp::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_ilp::expression_has_comment():
    assert hasattr(ilp::Expression, "comment")
    descriptor = None
    for klass in ilp::Expression.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_ilp::objectivefunctionexpression_is_not_abstract():
    assert not inspect.isabstract(ilp::ObjectiveFunctionExpression)


def test_ilp::objectivefunctionexpression_constructor_exists():
    assert callable(ilp::ObjectiveFunctionExpression.__init__)


def test_ilp::objectivefunctionexpression_constructor_args():
    sig = inspect.signature(ilp::ObjectiveFunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "goal" in params, "Missing parameter 'goal'"

def test_ilp::objectivefunctionexpression_has_goal():
    assert hasattr(ilp::ObjectiveFunctionExpression, "goal")
    descriptor = None
    for klass in ilp::ObjectiveFunctionExpression.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)



def test_ilp::constraintexpression_is_not_abstract():
    assert not inspect.isabstract(ilp::ConstraintExpression)


def test_ilp::constraintexpression_constructor_exists():
    assert callable(ilp::ConstraintExpression.__init__)


def test_ilp::constraintexpression_constructor_args():
    sig = inspect.signature(ilp::ConstraintExpression.__init__)
    params = list(sig.parameters.keys())



def test_ilp::variable_is_not_abstract():
    assert not inspect.isabstract(ilp::Variable)


def test_ilp::variable_constructor_exists():
    assert callable(ilp::Variable.__init__)


def test_ilp::variable_constructor_args():
    sig = inspect.signature(ilp::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_ilp::variable_has_name():
    assert hasattr(ilp::Variable, "name")
    descriptor = None
    for klass in ilp::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ilp::variable_has_dataType():
    assert hasattr(ilp::Variable, "dataType")
    descriptor = None
    for klass in ilp::Variable.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ilp::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ilp::BinaryExpression)


def test_ilp::binaryexpression_constructor_exists():
    assert callable(ilp::BinaryExpression.__init__)


def test_ilp::binaryexpression_constructor_args():
    sig = inspect.signature(ilp::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ilp::binaryexpression_has_operator():
    assert hasattr(ilp::BinaryExpression, "operator")
    descriptor = None
    for klass in ilp::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ilp::variableexpression_is_not_abstract():
    assert not inspect.isabstract(ilp::VariableExpression)


def test_ilp::variableexpression_constructor_exists():
    assert callable(ilp::VariableExpression.__init__)


def test_ilp::variableexpression_constructor_args():
    sig = inspect.signature(ilp::VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_ilp::literalexpression_is_not_abstract():
    assert not inspect.isabstract(ilp::LiteralExpression)


def test_ilp::literalexpression_constructor_exists():
    assert callable(ilp::LiteralExpression.__init__)


def test_ilp::literalexpression_constructor_args():
    sig = inspect.signature(ilp::LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ilp::literalexpression_has_value():
    assert hasattr(ilp::LiteralExpression, "value")
    descriptor = None
    for klass in ilp::LiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ilp::integerlinearprogram_is_not_abstract():
    assert not inspect.isabstract(ilp::IntegerLinearProgram)


def test_ilp::integerlinearprogram_constructor_exists():
    assert callable(ilp::IntegerLinearProgram.__init__)


def test_ilp::integerlinearprogram_constructor_args():
    sig = inspect.signature(ilp::IntegerLinearProgram.__init__)
    params = list(sig.parameters.keys())

def test_ilpdatatype_exists():
    # Check that the Enumeration exists
    assert ILPDataType is not None

def test_ilpdatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ILPDataType]
    expected_literals = [
        "REAL",
        "BINARY",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ILPDataType"

def test_objectivegoal_exists():
    # Check that the Enumeration exists
    assert ObjectiveGoal is not None

def test_objectivegoal_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectiveGoal]
    expected_literals = [
        "MIN",
        "MAX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectiveGoal"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "LESS_THAN_OR_EQUAL_TO",
        "PLUS",
        "GREATER_THAN_OR_EQUAL_TO",
        "MINUS",
        "EQUAL_TO",
        "TIMES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
ilp::ArithmeticExpression_strategy = st.builds(
    ilp::ArithmeticExpression,
)
ilp::Expression_strategy = st.builds(
    ilp::Expression,
    comment=
        safe_text
)
ilp::ObjectiveFunctionExpression_strategy = st.builds(
    ilp::ObjectiveFunctionExpression,
    goal=
        safe_text
)
ilp::ConstraintExpression_strategy = st.builds(
    ilp::ConstraintExpression,
)
ilp::Variable_strategy = st.builds(
    ilp::Variable,
    name=
        safe_text,
    dataType=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
ilp::BinaryExpression_strategy = st.builds(
    ilp::BinaryExpression,
    operator=
        safe_text
)
ilp::VariableExpression_strategy = st.builds(
    ilp::VariableExpression,
)
ilp::LiteralExpression_strategy = st.builds(
    ilp::LiteralExpression,
    value=
        safe_text
)
ilp::IntegerLinearProgram_strategy = st.builds(
    ilp::IntegerLinearProgram,
)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=ilp::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ilp::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ilp::ArithmeticExpression)

@given(instance=ilp::Expression_strategy)
@settings(max_examples=50)
def test_ilp::expression_instantiation(instance):
    assert isinstance(instance, ilp::Expression)

@given(instance=ilp::Expression_strategy)
def test_ilp::expression_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=ilp::Expression_strategy)
def test_ilp::expression_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ilp::ObjectiveFunctionExpression_strategy)
@settings(max_examples=50)
def test_ilp::objectivefunctionexpression_instantiation(instance):
    assert isinstance(instance, ilp::ObjectiveFunctionExpression)

@given(instance=ilp::ObjectiveFunctionExpression_strategy)
def test_ilp::objectivefunctionexpression_goal_type(instance):
    assert isinstance(instance.goal, str)


@given(instance=ilp::ObjectiveFunctionExpression_strategy)
def test_ilp::objectivefunctionexpression_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original

@given(instance=ilp::ConstraintExpression_strategy)
@settings(max_examples=50)
def test_ilp::constraintexpression_instantiation(instance):
    assert isinstance(instance, ilp::ConstraintExpression)

@given(instance=ilp::Variable_strategy)
@settings(max_examples=50)
def test_ilp::variable_instantiation(instance):
    assert isinstance(instance, ilp::Variable)

@given(instance=ilp::Variable_strategy)
def test_ilp::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ilp::Variable_strategy)
def test_ilp::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ilp::Variable_strategy)
def test_ilp::variable_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=ilp::Variable_strategy)
def test_ilp::variable_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ilp::BinaryExpression_strategy)
@settings(max_examples=50)
def test_ilp::binaryexpression_instantiation(instance):
    assert isinstance(instance, ilp::BinaryExpression)

@given(instance=ilp::BinaryExpression_strategy)
def test_ilp::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ilp::BinaryExpression_strategy)
def test_ilp::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ilp::VariableExpression_strategy)
@settings(max_examples=50)
def test_ilp::variableexpression_instantiation(instance):
    assert isinstance(instance, ilp::VariableExpression)

@given(instance=ilp::LiteralExpression_strategy)
@settings(max_examples=50)
def test_ilp::literalexpression_instantiation(instance):
    assert isinstance(instance, ilp::LiteralExpression)

@given(instance=ilp::LiteralExpression_strategy)
def test_ilp::literalexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ilp::LiteralExpression_strategy)
def test_ilp::literalexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ilp::IntegerLinearProgram_strategy)
@settings(max_examples=50)
def test_ilp::integerlinearprogram_instantiation(instance):
    assert isinstance(instance, ilp::IntegerLinearProgram)

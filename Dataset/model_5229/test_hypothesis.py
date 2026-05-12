import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BinaryExpression,
    ilp_ArithmeticExpression,
    ilp_Expression,
    ilp_ObjectiveFunctionExpression,
    ilp_ConstraintExpression,
    ilp_Variable,
    Expression,
    ilp_VariableExpression,
    ilp_BinaryExpression,
    ilp_LiteralExpression,
    ilp_IntegerLinearProgram,
    Operator,
    ILPDataType,
    ObjectiveGoal,
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



def test_ilp_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ilp_ArithmeticExpression)


def test_ilp_arithmeticexpression_constructor_exists():
    assert callable(ilp_ArithmeticExpression.__init__)


def test_ilp_arithmeticexpression_constructor_args():
    sig = inspect.signature(ilp_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ilp_expression_is_not_abstract():
    assert not inspect.isabstract(ilp_Expression)


def test_ilp_expression_constructor_exists():
    assert callable(ilp_Expression.__init__)


def test_ilp_expression_constructor_args():
    sig = inspect.signature(ilp_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_ilp_expression_has_comment():
    assert hasattr(ilp_Expression, "comment")
    descriptor = None
    for klass in ilp_Expression.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_ilp_objectivefunctionexpression_is_not_abstract():
    assert not inspect.isabstract(ilp_ObjectiveFunctionExpression)


def test_ilp_objectivefunctionexpression_constructor_exists():
    assert callable(ilp_ObjectiveFunctionExpression.__init__)


def test_ilp_objectivefunctionexpression_constructor_args():
    sig = inspect.signature(ilp_ObjectiveFunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "goal" in params, "Missing parameter 'goal'"

def test_ilp_objectivefunctionexpression_has_goal():
    assert hasattr(ilp_ObjectiveFunctionExpression, "goal")
    descriptor = None
    for klass in ilp_ObjectiveFunctionExpression.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)



def test_ilp_constraintexpression_is_not_abstract():
    assert not inspect.isabstract(ilp_ConstraintExpression)


def test_ilp_constraintexpression_constructor_exists():
    assert callable(ilp_ConstraintExpression.__init__)


def test_ilp_constraintexpression_constructor_args():
    sig = inspect.signature(ilp_ConstraintExpression.__init__)
    params = list(sig.parameters.keys())



def test_ilp_variable_is_not_abstract():
    assert not inspect.isabstract(ilp_Variable)


def test_ilp_variable_constructor_exists():
    assert callable(ilp_Variable.__init__)


def test_ilp_variable_constructor_args():
    sig = inspect.signature(ilp_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_ilp_variable_has_name():
    assert hasattr(ilp_Variable, "name")
    descriptor = None
    for klass in ilp_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ilp_variable_has_dataType():
    assert hasattr(ilp_Variable, "dataType")
    descriptor = None
    for klass in ilp_Variable.__mro__:
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



def test_ilp_variableexpression_is_not_abstract():
    assert not inspect.isabstract(ilp_VariableExpression)


def test_ilp_variableexpression_constructor_exists():
    assert callable(ilp_VariableExpression.__init__)


def test_ilp_variableexpression_constructor_args():
    sig = inspect.signature(ilp_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_ilp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ilp_BinaryExpression)


def test_ilp_binaryexpression_constructor_exists():
    assert callable(ilp_BinaryExpression.__init__)


def test_ilp_binaryexpression_constructor_args():
    sig = inspect.signature(ilp_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ilp_binaryexpression_has_operator():
    assert hasattr(ilp_BinaryExpression, "operator")
    descriptor = None
    for klass in ilp_BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ilp_literalexpression_is_not_abstract():
    assert not inspect.isabstract(ilp_LiteralExpression)


def test_ilp_literalexpression_constructor_exists():
    assert callable(ilp_LiteralExpression.__init__)


def test_ilp_literalexpression_constructor_args():
    sig = inspect.signature(ilp_LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ilp_literalexpression_has_value():
    assert hasattr(ilp_LiteralExpression, "value")
    descriptor = None
    for klass in ilp_LiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ilp_integerlinearprogram_is_not_abstract():
    assert not inspect.isabstract(ilp_IntegerLinearProgram)


def test_ilp_integerlinearprogram_constructor_exists():
    assert callable(ilp_IntegerLinearProgram.__init__)


def test_ilp_integerlinearprogram_constructor_args():
    sig = inspect.signature(ilp_IntegerLinearProgram.__init__)
    params = list(sig.parameters.keys())

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "GREATER_THAN_OR_EQUAL_TO",
        "LESS_THAN_OR_EQUAL_TO",
        "TIMES",
        "PLUS",
        "MINUS",
        "EQUAL_TO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

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
ilp_ArithmeticExpression_strategy = st.builds(
    ilp_ArithmeticExpression,
)
ilp_Expression_strategy = st.builds(
    ilp_Expression,
    comment=
        safe_text
)
ilp_ObjectiveFunctionExpression_strategy = st.builds(
    ilp_ObjectiveFunctionExpression,
    goal=
        safe_text
)
ilp_ConstraintExpression_strategy = st.builds(
    ilp_ConstraintExpression,
)
ilp_Variable_strategy = st.builds(
    ilp_Variable,
    name=
        safe_text,
    dataType=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
ilp_VariableExpression_strategy = st.builds(
    ilp_VariableExpression,
)
ilp_BinaryExpression_strategy = st.builds(
    ilp_BinaryExpression,
    operator=
        safe_text
)
ilp_LiteralExpression_strategy = st.builds(
    ilp_LiteralExpression,
    value=
        safe_text
)
ilp_IntegerLinearProgram_strategy = st.builds(
    ilp_IntegerLinearProgram,
)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=ilp_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ilp_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ilp_ArithmeticExpression)

@given(instance=ilp_Expression_strategy)
@settings(max_examples=50)
def test_ilp_expression_instantiation(instance):
    assert isinstance(instance, ilp_Expression)



@given(instance=ilp_Expression_strategy)
def test_ilp_expression_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ilp_ObjectiveFunctionExpression_strategy)
@settings(max_examples=50)
def test_ilp_objectivefunctionexpression_instantiation(instance):
    assert isinstance(instance, ilp_ObjectiveFunctionExpression)



@given(instance=ilp_ObjectiveFunctionExpression_strategy)
def test_ilp_objectivefunctionexpression_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original

@given(instance=ilp_ConstraintExpression_strategy)
@settings(max_examples=50)
def test_ilp_constraintexpression_instantiation(instance):
    assert isinstance(instance, ilp_ConstraintExpression)

@given(instance=ilp_Variable_strategy)
@settings(max_examples=50)
def test_ilp_variable_instantiation(instance):
    assert isinstance(instance, ilp_Variable)



@given(instance=ilp_Variable_strategy)
def test_ilp_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ilp_Variable_strategy)
def test_ilp_variable_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ilp_VariableExpression_strategy)
@settings(max_examples=50)
def test_ilp_variableexpression_instantiation(instance):
    assert isinstance(instance, ilp_VariableExpression)

@given(instance=ilp_BinaryExpression_strategy)
@settings(max_examples=50)
def test_ilp_binaryexpression_instantiation(instance):
    assert isinstance(instance, ilp_BinaryExpression)



@given(instance=ilp_BinaryExpression_strategy)
def test_ilp_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ilp_LiteralExpression_strategy)
@settings(max_examples=50)
def test_ilp_literalexpression_instantiation(instance):
    assert isinstance(instance, ilp_LiteralExpression)



@given(instance=ilp_LiteralExpression_strategy)
def test_ilp_literalexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ilp_IntegerLinearProgram_strategy)
@settings(max_examples=50)
def test_ilp_integerlinearprogram_instantiation(instance):
    assert isinstance(instance, ilp_IntegerLinearProgram)

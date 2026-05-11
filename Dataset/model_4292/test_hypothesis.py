import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    expression::SubExpression2,
    expression::SubExpression,
    SubExpression2,
    expression::NegativeIntExpression,
    expression::StringExpression,
    expression::ExpressionList,
    expression::Expression,
    SubExpression,
    expression::BooleanExpression,
    expression::IncludingExpression,
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



def test_expression::subexpression2_is_not_abstract():
    assert not inspect.isabstract(expression::SubExpression2)


def test_expression::subexpression2_constructor_exists():
    assert callable(expression::SubExpression2.__init__)


def test_expression::subexpression2_constructor_args():
    sig = inspect.signature(expression::SubExpression2.__init__)
    params = list(sig.parameters.keys())



def test_expression::subexpression_is_not_abstract():
    assert not inspect.isabstract(expression::SubExpression)


def test_expression::subexpression_constructor_exists():
    assert callable(expression::SubExpression.__init__)


def test_expression::subexpression_constructor_args():
    sig = inspect.signature(expression::SubExpression.__init__)
    params = list(sig.parameters.keys())



def test_subexpression2_is_not_abstract():
    assert not inspect.isabstract(SubExpression2)


def test_subexpression2_constructor_exists():
    assert callable(SubExpression2.__init__)


def test_subexpression2_constructor_args():
    sig = inspect.signature(SubExpression2.__init__)
    params = list(sig.parameters.keys())



def test_expression::negativeintexpression_is_not_abstract():
    assert not inspect.isabstract(expression::NegativeIntExpression)


def test_expression::negativeintexpression_constructor_exists():
    assert callable(expression::NegativeIntExpression.__init__)


def test_expression::negativeintexpression_constructor_args():
    sig = inspect.signature(expression::NegativeIntExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "isNegative" in params, "Missing parameter 'isNegative'"

def test_expression::negativeintexpression_has_value():
    assert hasattr(expression::NegativeIntExpression, "value")
    descriptor = None
    for klass in expression::NegativeIntExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_expression::negativeintexpression_has_isNegative():
    assert hasattr(expression::NegativeIntExpression, "isNegative")
    descriptor = None
    for klass in expression::NegativeIntExpression.__mro__:
        if "isNegative" in klass.__dict__:
            descriptor = klass.__dict__["isNegative"]
            break
    assert isinstance(descriptor, property)



def test_expression::stringexpression_is_not_abstract():
    assert not inspect.isabstract(expression::StringExpression)


def test_expression::stringexpression_constructor_exists():
    assert callable(expression::StringExpression.__init__)


def test_expression::stringexpression_constructor_args():
    sig = inspect.signature(expression::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::stringexpression_has_value():
    assert hasattr(expression::StringExpression, "value")
    descriptor = None
    for klass in expression::StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::expressionlist_is_not_abstract():
    assert not inspect.isabstract(expression::ExpressionList)


def test_expression::expressionlist_constructor_exists():
    assert callable(expression::ExpressionList.__init__)


def test_expression::expressionlist_constructor_args():
    sig = inspect.signature(expression::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_subexpression_is_not_abstract():
    assert not inspect.isabstract(SubExpression)


def test_subexpression_constructor_exists():
    assert callable(SubExpression.__init__)


def test_subexpression_constructor_args():
    sig = inspect.signature(SubExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(expression::BooleanExpression)


def test_expression::booleanexpression_constructor_exists():
    assert callable(expression::BooleanExpression.__init__)


def test_expression::booleanexpression_constructor_args():
    sig = inspect.signature(expression::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression::booleanexpression_has_value():
    assert hasattr(expression::BooleanExpression, "value")
    descriptor = None
    for klass in expression::BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::includingexpression_is_not_abstract():
    assert not inspect.isabstract(expression::IncludingExpression)


def test_expression::includingexpression_constructor_exists():
    assert callable(expression::IncludingExpression.__init__)


def test_expression::includingexpression_constructor_args():
    sig = inspect.signature(expression::IncludingExpression.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
expression::SubExpression2_strategy = st.builds(
    expression::SubExpression2,
)
expression::SubExpression_strategy = st.builds(
    expression::SubExpression,
)
SubExpression2_strategy = st.builds(
    SubExpression2,
)
expression::NegativeIntExpression_strategy = st.builds(
    expression::NegativeIntExpression,
    value=
        safe_text,
    isNegative=
        safe_text
)
expression::StringExpression_strategy = st.builds(
    expression::StringExpression,
    value=
        safe_text
)
expression::ExpressionList_strategy = st.builds(
    expression::ExpressionList,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
)
SubExpression_strategy = st.builds(
    SubExpression,
)
expression::BooleanExpression_strategy = st.builds(
    expression::BooleanExpression,
    value=
        safe_text
)
expression::IncludingExpression_strategy = st.builds(
    expression::IncludingExpression,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression::SubExpression2_strategy)
@settings(max_examples=50)
def test_expression::subexpression2_instantiation(instance):
    assert isinstance(instance, expression::SubExpression2)

@given(instance=expression::SubExpression_strategy)
@settings(max_examples=50)
def test_expression::subexpression_instantiation(instance):
    assert isinstance(instance, expression::SubExpression)

@given(instance=SubExpression2_strategy)
@settings(max_examples=50)
def test_subexpression2_instantiation(instance):
    assert isinstance(instance, SubExpression2)

@given(instance=expression::NegativeIntExpression_strategy)
@settings(max_examples=50)
def test_expression::negativeintexpression_instantiation(instance):
    assert isinstance(instance, expression::NegativeIntExpression)

@given(instance=expression::NegativeIntExpression_strategy)
def test_expression::negativeintexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expression::NegativeIntExpression_strategy)
def test_expression::negativeintexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::NegativeIntExpression_strategy)
def test_expression::negativeintexpression_isNegative_type(instance):
    assert isinstance(instance.isNegative, str)


@given(instance=expression::NegativeIntExpression_strategy)
def test_expression::negativeintexpression_isNegative_setter(instance):
    original = instance.isNegative
    instance.isNegative = original
    assert instance.isNegative == original

@given(instance=expression::StringExpression_strategy)
@settings(max_examples=50)
def test_expression::stringexpression_instantiation(instance):
    assert isinstance(instance, expression::StringExpression)

@given(instance=expression::StringExpression_strategy)
def test_expression::stringexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expression::StringExpression_strategy)
def test_expression::stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::ExpressionList_strategy)
@settings(max_examples=50)
def test_expression::expressionlist_instantiation(instance):
    assert isinstance(instance, expression::ExpressionList)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=SubExpression_strategy)
@settings(max_examples=50)
def test_subexpression_instantiation(instance):
    assert isinstance(instance, SubExpression)

@given(instance=expression::BooleanExpression_strategy)
@settings(max_examples=50)
def test_expression::booleanexpression_instantiation(instance):
    assert isinstance(instance, expression::BooleanExpression)

@given(instance=expression::BooleanExpression_strategy)
def test_expression::booleanexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expression::BooleanExpression_strategy)
def test_expression::booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::IncludingExpression_strategy)
@settings(max_examples=50)
def test_expression::includingexpression_instantiation(instance):
    assert isinstance(instance, expression::IncludingExpression)

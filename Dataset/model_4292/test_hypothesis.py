import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    expression_SubExpression2,
    expression_SubExpression,
    SubExpression2,
    expression_NegativeIntExpression,
    expression_StringExpression,
    expression_ExpressionList,
    expression_Expression,
    SubExpression,
    expression_BooleanExpression,
    expression_IncludingExpression,
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



def test_expression_subexpression2_is_not_abstract():
    assert not inspect.isabstract(expression_SubExpression2)


def test_expression_subexpression2_constructor_exists():
    assert callable(expression_SubExpression2.__init__)


def test_expression_subexpression2_constructor_args():
    sig = inspect.signature(expression_SubExpression2.__init__)
    params = list(sig.parameters.keys())



def test_expression_subexpression_is_not_abstract():
    assert not inspect.isabstract(expression_SubExpression)


def test_expression_subexpression_constructor_exists():
    assert callable(expression_SubExpression.__init__)


def test_expression_subexpression_constructor_args():
    sig = inspect.signature(expression_SubExpression.__init__)
    params = list(sig.parameters.keys())



def test_subexpression2_is_not_abstract():
    assert not inspect.isabstract(SubExpression2)


def test_subexpression2_constructor_exists():
    assert callable(SubExpression2.__init__)


def test_subexpression2_constructor_args():
    sig = inspect.signature(SubExpression2.__init__)
    params = list(sig.parameters.keys())



def test_expression_negativeintexpression_is_not_abstract():
    assert not inspect.isabstract(expression_NegativeIntExpression)


def test_expression_negativeintexpression_constructor_exists():
    assert callable(expression_NegativeIntExpression.__init__)


def test_expression_negativeintexpression_constructor_args():
    sig = inspect.signature(expression_NegativeIntExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "isNegative" in params, "Missing parameter 'isNegative'"

def test_expression_negativeintexpression_has_value():
    assert hasattr(expression_NegativeIntExpression, "value")
    descriptor = None
    for klass in expression_NegativeIntExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_expression_negativeintexpression_has_isNegative():
    assert hasattr(expression_NegativeIntExpression, "isNegative")
    descriptor = None
    for klass in expression_NegativeIntExpression.__mro__:
        if "isNegative" in klass.__dict__:
            descriptor = klass.__dict__["isNegative"]
            break
    assert isinstance(descriptor, property)



def test_expression_stringexpression_is_not_abstract():
    assert not inspect.isabstract(expression_StringExpression)


def test_expression_stringexpression_constructor_exists():
    assert callable(expression_StringExpression.__init__)


def test_expression_stringexpression_constructor_args():
    sig = inspect.signature(expression_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression_stringexpression_has_value():
    assert hasattr(expression_StringExpression, "value")
    descriptor = None
    for klass in expression_StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_expressionlist_is_not_abstract():
    assert not inspect.isabstract(expression_ExpressionList)


def test_expression_expressionlist_constructor_exists():
    assert callable(expression_ExpressionList.__init__)


def test_expression_expressionlist_constructor_args():
    sig = inspect.signature(expression_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_subexpression_is_not_abstract():
    assert not inspect.isabstract(SubExpression)


def test_subexpression_constructor_exists():
    assert callable(SubExpression.__init__)


def test_subexpression_constructor_args():
    sig = inspect.signature(SubExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(expression_BooleanExpression)


def test_expression_booleanexpression_constructor_exists():
    assert callable(expression_BooleanExpression.__init__)


def test_expression_booleanexpression_constructor_args():
    sig = inspect.signature(expression_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expression_booleanexpression_has_value():
    assert hasattr(expression_BooleanExpression, "value")
    descriptor = None
    for klass in expression_BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_includingexpression_is_not_abstract():
    assert not inspect.isabstract(expression_IncludingExpression)


def test_expression_includingexpression_constructor_exists():
    assert callable(expression_IncludingExpression.__init__)


def test_expression_includingexpression_constructor_args():
    sig = inspect.signature(expression_IncludingExpression.__init__)
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
expression_SubExpression2_strategy = st.builds(
    expression_SubExpression2,
)
expression_SubExpression_strategy = st.builds(
    expression_SubExpression,
)
SubExpression2_strategy = st.builds(
    SubExpression2,
)
expression_NegativeIntExpression_strategy = st.builds(
    expression_NegativeIntExpression,
    value=
        safe_text,
    isNegative=
        safe_text
)
expression_StringExpression_strategy = st.builds(
    expression_StringExpression,
    value=
        safe_text
)
expression_ExpressionList_strategy = st.builds(
    expression_ExpressionList,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
)
SubExpression_strategy = st.builds(
    SubExpression,
)
expression_BooleanExpression_strategy = st.builds(
    expression_BooleanExpression,
    value=
        safe_text
)
expression_IncludingExpression_strategy = st.builds(
    expression_IncludingExpression,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression_SubExpression2_strategy)
@settings(max_examples=50)
def test_expression_subexpression2_instantiation(instance):
    assert isinstance(instance, expression_SubExpression2)

@given(instance=expression_SubExpression_strategy)
@settings(max_examples=50)
def test_expression_subexpression_instantiation(instance):
    assert isinstance(instance, expression_SubExpression)

@given(instance=SubExpression2_strategy)
@settings(max_examples=50)
def test_subexpression2_instantiation(instance):
    assert isinstance(instance, SubExpression2)

@given(instance=expression_NegativeIntExpression_strategy)
@settings(max_examples=50)
def test_expression_negativeintexpression_instantiation(instance):
    assert isinstance(instance, expression_NegativeIntExpression)



@given(instance=expression_NegativeIntExpression_strategy)
def test_expression_negativeintexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=expression_NegativeIntExpression_strategy)
def test_expression_negativeintexpression_isNegative_setter(instance):
    original = instance.isNegative
    instance.isNegative = original
    assert instance.isNegative == original

@given(instance=expression_StringExpression_strategy)
@settings(max_examples=50)
def test_expression_stringexpression_instantiation(instance):
    assert isinstance(instance, expression_StringExpression)



@given(instance=expression_StringExpression_strategy)
def test_expression_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression_ExpressionList_strategy)
@settings(max_examples=50)
def test_expression_expressionlist_instantiation(instance):
    assert isinstance(instance, expression_ExpressionList)

@given(instance=expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)

@given(instance=SubExpression_strategy)
@settings(max_examples=50)
def test_subexpression_instantiation(instance):
    assert isinstance(instance, SubExpression)

@given(instance=expression_BooleanExpression_strategy)
@settings(max_examples=50)
def test_expression_booleanexpression_instantiation(instance):
    assert isinstance(instance, expression_BooleanExpression)



@given(instance=expression_BooleanExpression_strategy)
def test_expression_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression_IncludingExpression_strategy)
@settings(max_examples=50)
def test_expression_includingexpression_instantiation(instance):
    assert isinstance(instance, expression_IncludingExpression)

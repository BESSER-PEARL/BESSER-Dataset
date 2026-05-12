import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    myMath_Num,
    myMath_Mult,
    myMath_Sub,
    myMath_Add,
    myMath_Expression,
    myMath_MathExp,
    myMath_Div,
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



def test_mymath_num_is_not_abstract():
    assert not inspect.isabstract(myMath_Num)


def test_mymath_num_constructor_exists():
    assert callable(myMath_Num.__init__)


def test_mymath_num_constructor_args():
    sig = inspect.signature(myMath_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mymath_num_has_value():
    assert hasattr(myMath_Num, "value")
    descriptor = None
    for klass in myMath_Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mymath_mult_is_not_abstract():
    assert not inspect.isabstract(myMath_Mult)


def test_mymath_mult_constructor_exists():
    assert callable(myMath_Mult.__init__)


def test_mymath_mult_constructor_args():
    sig = inspect.signature(myMath_Mult.__init__)
    params = list(sig.parameters.keys())



def test_mymath_sub_is_not_abstract():
    assert not inspect.isabstract(myMath_Sub)


def test_mymath_sub_constructor_exists():
    assert callable(myMath_Sub.__init__)


def test_mymath_sub_constructor_args():
    sig = inspect.signature(myMath_Sub.__init__)
    params = list(sig.parameters.keys())



def test_mymath_add_is_not_abstract():
    assert not inspect.isabstract(myMath_Add)


def test_mymath_add_constructor_exists():
    assert callable(myMath_Add.__init__)


def test_mymath_add_constructor_args():
    sig = inspect.signature(myMath_Add.__init__)
    params = list(sig.parameters.keys())



def test_mymath_expression_is_not_abstract():
    assert not inspect.isabstract(myMath_Expression)


def test_mymath_expression_constructor_exists():
    assert callable(myMath_Expression.__init__)


def test_mymath_expression_constructor_args():
    sig = inspect.signature(myMath_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mymath_mathexp_is_not_abstract():
    assert not inspect.isabstract(myMath_MathExp)


def test_mymath_mathexp_constructor_exists():
    assert callable(myMath_MathExp.__init__)


def test_mymath_mathexp_constructor_args():
    sig = inspect.signature(myMath_MathExp.__init__)
    params = list(sig.parameters.keys())



def test_mymath_div_is_not_abstract():
    assert not inspect.isabstract(myMath_Div)


def test_mymath_div_constructor_exists():
    assert callable(myMath_Div.__init__)


def test_mymath_div_constructor_args():
    sig = inspect.signature(myMath_Div.__init__)
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
myMath_Num_strategy = st.builds(
    myMath_Num,
    value=
        st.integers()
)
myMath_Mult_strategy = st.builds(
    myMath_Mult,
)
myMath_Sub_strategy = st.builds(
    myMath_Sub,
)
myMath_Add_strategy = st.builds(
    myMath_Add,
)
myMath_Expression_strategy = st.builds(
    myMath_Expression,
)
myMath_MathExp_strategy = st.builds(
    myMath_MathExp,
)
myMath_Div_strategy = st.builds(
    myMath_Div,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=myMath_Num_strategy)
@settings(max_examples=50)
def test_mymath_num_instantiation(instance):
    assert isinstance(instance, myMath_Num)



@given(instance=myMath_Num_strategy)
def test_mymath_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myMath_Mult_strategy)
@settings(max_examples=50)
def test_mymath_mult_instantiation(instance):
    assert isinstance(instance, myMath_Mult)

@given(instance=myMath_Sub_strategy)
@settings(max_examples=50)
def test_mymath_sub_instantiation(instance):
    assert isinstance(instance, myMath_Sub)

@given(instance=myMath_Add_strategy)
@settings(max_examples=50)
def test_mymath_add_instantiation(instance):
    assert isinstance(instance, myMath_Add)

@given(instance=myMath_Expression_strategy)
@settings(max_examples=50)
def test_mymath_expression_instantiation(instance):
    assert isinstance(instance, myMath_Expression)

@given(instance=myMath_MathExp_strategy)
@settings(max_examples=50)
def test_mymath_mathexp_instantiation(instance):
    assert isinstance(instance, myMath_MathExp)

@given(instance=myMath_Div_strategy)
@settings(max_examples=50)
def test_mymath_div_instantiation(instance):
    assert isinstance(instance, myMath_Div)

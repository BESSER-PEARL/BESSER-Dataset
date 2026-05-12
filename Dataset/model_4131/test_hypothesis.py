import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ExpOp,
    mdsdassignment2_Sub,
    mdsdassignment2_Mult,
    mdsdassignment2_Div,
    mdsdassignment2_Parenthesis,
    mdsdassignment2_ExpOp,
    mdsdassignment2_Exp,
    mdsdassignment2_MathExp,
    mdsdassignment2_Add,
    mdsdassignment2_Num,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expop_is_not_abstract():
    assert not inspect.isabstract(ExpOp)


def test_expop_constructor_exists():
    assert callable(ExpOp.__init__)


def test_expop_constructor_args():
    sig = inspect.signature(ExpOp.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_sub_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Sub)


def test_mdsdassignment2_sub_constructor_exists():
    assert callable(mdsdassignment2_Sub.__init__)


def test_mdsdassignment2_sub_constructor_args():
    sig = inspect.signature(mdsdassignment2_Sub.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_mult_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Mult)


def test_mdsdassignment2_mult_constructor_exists():
    assert callable(mdsdassignment2_Mult.__init__)


def test_mdsdassignment2_mult_constructor_args():
    sig = inspect.signature(mdsdassignment2_Mult.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_div_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Div)


def test_mdsdassignment2_div_constructor_exists():
    assert callable(mdsdassignment2_Div.__init__)


def test_mdsdassignment2_div_constructor_args():
    sig = inspect.signature(mdsdassignment2_Div.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_parenthesis_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Parenthesis)


def test_mdsdassignment2_parenthesis_constructor_exists():
    assert callable(mdsdassignment2_Parenthesis.__init__)


def test_mdsdassignment2_parenthesis_constructor_args():
    sig = inspect.signature(mdsdassignment2_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_expop_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_ExpOp)


def test_mdsdassignment2_expop_constructor_exists():
    assert callable(mdsdassignment2_ExpOp.__init__)


def test_mdsdassignment2_expop_constructor_args():
    sig = inspect.signature(mdsdassignment2_ExpOp.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_exp_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Exp)


def test_mdsdassignment2_exp_constructor_exists():
    assert callable(mdsdassignment2_Exp.__init__)


def test_mdsdassignment2_exp_constructor_args():
    sig = inspect.signature(mdsdassignment2_Exp.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_mathexp_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_MathExp)


def test_mdsdassignment2_mathexp_constructor_exists():
    assert callable(mdsdassignment2_MathExp.__init__)


def test_mdsdassignment2_mathexp_constructor_args():
    sig = inspect.signature(mdsdassignment2_MathExp.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_add_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Add)


def test_mdsdassignment2_add_constructor_exists():
    assert callable(mdsdassignment2_Add.__init__)


def test_mdsdassignment2_add_constructor_args():
    sig = inspect.signature(mdsdassignment2_Add.__init__)
    params = list(sig.parameters.keys())



def test_mdsdassignment2_num_is_not_abstract():
    assert not inspect.isabstract(mdsdassignment2_Num)


def test_mdsdassignment2_num_constructor_exists():
    assert callable(mdsdassignment2_Num.__init__)


def test_mdsdassignment2_num_constructor_args():
    sig = inspect.signature(mdsdassignment2_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mdsdassignment2_num_has_value():
    assert hasattr(mdsdassignment2_Num, "value")
    descriptor = None
    for klass in mdsdassignment2_Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)


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
ExpOp_strategy = st.builds(
    ExpOp,
)
mdsdassignment2_Sub_strategy = st.builds(
    mdsdassignment2_Sub,
)
mdsdassignment2_Mult_strategy = st.builds(
    mdsdassignment2_Mult,
)
mdsdassignment2_Div_strategy = st.builds(
    mdsdassignment2_Div,
)
mdsdassignment2_Parenthesis_strategy = st.builds(
    mdsdassignment2_Parenthesis,
)
mdsdassignment2_ExpOp_strategy = st.builds(
    mdsdassignment2_ExpOp,
)
mdsdassignment2_Exp_strategy = st.builds(
    mdsdassignment2_Exp,
)
mdsdassignment2_MathExp_strategy = st.builds(
    mdsdassignment2_MathExp,
)
mdsdassignment2_Add_strategy = st.builds(
    mdsdassignment2_Add,
)
mdsdassignment2_Num_strategy = st.builds(
    mdsdassignment2_Num,
    value=
        st.integers()
)

@given(instance=ExpOp_strategy)
@settings(max_examples=50)
def test_expop_instantiation(instance):
    assert isinstance(instance, ExpOp)

@given(instance=mdsdassignment2_Sub_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_sub_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Sub)

@given(instance=mdsdassignment2_Mult_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_mult_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Mult)

@given(instance=mdsdassignment2_Div_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_div_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Div)

@given(instance=mdsdassignment2_Parenthesis_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_parenthesis_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Parenthesis)

@given(instance=mdsdassignment2_ExpOp_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_expop_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_ExpOp)

@given(instance=mdsdassignment2_Exp_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_exp_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Exp)

@given(instance=mdsdassignment2_MathExp_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_mathexp_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_MathExp)

@given(instance=mdsdassignment2_Add_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_add_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Add)

@given(instance=mdsdassignment2_Num_strategy)
@settings(max_examples=50)
def test_mdsdassignment2_num_instantiation(instance):
    assert isinstance(instance, mdsdassignment2_Num)



@given(instance=mdsdassignment2_Num_strategy)
def test_mdsdassignment2_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

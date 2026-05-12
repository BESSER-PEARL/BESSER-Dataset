import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    refac_K,
    refac_X,
    refac_N99,
    refac_M,
    refac_W,
    refac_C,
    refac_A,
    refac_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_refac_k_is_not_abstract():
    assert not inspect.isabstract(refac_K)


def test_refac_k_constructor_exists():
    assert callable(refac_K.__init__)


def test_refac_k_constructor_args():
    sig = inspect.signature(refac_K.__init__)
    params = list(sig.parameters.keys())



def test_refac_x_is_not_abstract():
    assert not inspect.isabstract(refac_X)


def test_refac_x_constructor_exists():
    assert callable(refac_X.__init__)


def test_refac_x_constructor_args():
    sig = inspect.signature(refac_X.__init__)
    params = list(sig.parameters.keys())



def test_refac_n99_is_not_abstract():
    assert not inspect.isabstract(refac_N99)


def test_refac_n99_constructor_exists():
    assert callable(refac_N99.__init__)


def test_refac_n99_constructor_args():
    sig = inspect.signature(refac_N99.__init__)
    params = list(sig.parameters.keys())



def test_refac_m_is_not_abstract():
    assert not inspect.isabstract(refac_M)


def test_refac_m_constructor_exists():
    assert callable(refac_M.__init__)


def test_refac_m_constructor_args():
    sig = inspect.signature(refac_M.__init__)
    params = list(sig.parameters.keys())



def test_refac_w_is_not_abstract():
    assert not inspect.isabstract(refac_W)


def test_refac_w_constructor_exists():
    assert callable(refac_W.__init__)


def test_refac_w_constructor_args():
    sig = inspect.signature(refac_W.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refac_w_has_name():
    assert hasattr(refac_W, "name")
    descriptor = None
    for klass in refac_W.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refac_c_is_not_abstract():
    assert not inspect.isabstract(refac_C)


def test_refac_c_constructor_exists():
    assert callable(refac_C.__init__)


def test_refac_c_constructor_args():
    sig = inspect.signature(refac_C.__init__)
    params = list(sig.parameters.keys())



def test_refac_a_is_not_abstract():
    assert not inspect.isabstract(refac_A)


def test_refac_a_constructor_exists():
    assert callable(refac_A.__init__)


def test_refac_a_constructor_args():
    sig = inspect.signature(refac_A.__init__)
    params = list(sig.parameters.keys())



def test_refac_b_is_not_abstract():
    assert not inspect.isabstract(refac_B)


def test_refac_b_constructor_exists():
    assert callable(refac_B.__init__)


def test_refac_b_constructor_args():
    sig = inspect.signature(refac_B.__init__)
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
refac_K_strategy = st.builds(
    refac_K,
)
refac_X_strategy = st.builds(
    refac_X,
)
refac_N99_strategy = st.builds(
    refac_N99,
)
refac_M_strategy = st.builds(
    refac_M,
)
refac_W_strategy = st.builds(
    refac_W,
    name=
        safe_text
)
refac_C_strategy = st.builds(
    refac_C,
)
refac_A_strategy = st.builds(
    refac_A,
)
refac_B_strategy = st.builds(
    refac_B,
)

@given(instance=refac_K_strategy)
@settings(max_examples=50)
def test_refac_k_instantiation(instance):
    assert isinstance(instance, refac_K)

@given(instance=refac_X_strategy)
@settings(max_examples=50)
def test_refac_x_instantiation(instance):
    assert isinstance(instance, refac_X)

@given(instance=refac_N99_strategy)
@settings(max_examples=50)
def test_refac_n99_instantiation(instance):
    assert isinstance(instance, refac_N99)

@given(instance=refac_M_strategy)
@settings(max_examples=50)
def test_refac_m_instantiation(instance):
    assert isinstance(instance, refac_M)

@given(instance=refac_W_strategy)
@settings(max_examples=50)
def test_refac_w_instantiation(instance):
    assert isinstance(instance, refac_W)



@given(instance=refac_W_strategy)
def test_refac_w_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=refac_C_strategy)
@settings(max_examples=50)
def test_refac_c_instantiation(instance):
    assert isinstance(instance, refac_C)

@given(instance=refac_A_strategy)
@settings(max_examples=50)
def test_refac_a_instantiation(instance):
    assert isinstance(instance, refac_A)

@given(instance=refac_B_strategy)
@settings(max_examples=50)
def test_refac_b_instantiation(instance):
    assert isinstance(instance, refac_B)

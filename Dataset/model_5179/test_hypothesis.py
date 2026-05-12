import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pmtest_A,
    A,
    pmtest_C,
    pmtest_B,
    pmtest_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pmtest_a_is_not_abstract():
    assert not inspect.isabstract(pmtest_A)


def test_pmtest_a_constructor_exists():
    assert callable(pmtest_A.__init__)


def test_pmtest_a_constructor_args():
    sig = inspect.signature(pmtest_A.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_pmtest_a_has_i():
    assert hasattr(pmtest_A, "i")
    descriptor = None
    for klass in pmtest_A.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_pmtest_c_is_not_abstract():
    assert not inspect.isabstract(pmtest_C)


def test_pmtest_c_constructor_exists():
    assert callable(pmtest_C.__init__)


def test_pmtest_c_constructor_args():
    sig = inspect.signature(pmtest_C.__init__)
    params = list(sig.parameters.keys())



def test_pmtest_b_is_not_abstract():
    assert not inspect.isabstract(pmtest_B)


def test_pmtest_b_constructor_exists():
    assert callable(pmtest_B.__init__)


def test_pmtest_b_constructor_args():
    sig = inspect.signature(pmtest_B.__init__)
    params = list(sig.parameters.keys())



def test_pmtest_d_is_not_abstract():
    assert not inspect.isabstract(pmtest_D)


def test_pmtest_d_constructor_exists():
    assert callable(pmtest_D.__init__)


def test_pmtest_d_constructor_args():
    sig = inspect.signature(pmtest_D.__init__)
    params = list(sig.parameters.keys())
    assert "j" in params, "Missing parameter 'j'"

def test_pmtest_d_has_j():
    assert hasattr(pmtest_D, "j")
    descriptor = None
    for klass in pmtest_D.__mro__:
        if "j" in klass.__dict__:
            descriptor = klass.__dict__["j"]
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
pmtest_A_strategy = st.builds(
    pmtest_A,
    i=
        st.integers()
)
A_strategy = st.builds(
    A,
)
pmtest_C_strategy = st.builds(
    pmtest_C,
)
pmtest_B_strategy = st.builds(
    pmtest_B,
)
pmtest_D_strategy = st.builds(
    pmtest_D,
    j=
        st.integers()
)

@given(instance=pmtest_A_strategy)
@settings(max_examples=50)
def test_pmtest_a_instantiation(instance):
    assert isinstance(instance, pmtest_A)



@given(instance=pmtest_A_strategy)
def test_pmtest_a_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=pmtest_C_strategy)
@settings(max_examples=50)
def test_pmtest_c_instantiation(instance):
    assert isinstance(instance, pmtest_C)

@given(instance=pmtest_B_strategy)
@settings(max_examples=50)
def test_pmtest_b_instantiation(instance):
    assert isinstance(instance, pmtest_B)

@given(instance=pmtest_D_strategy)
@settings(max_examples=50)
def test_pmtest_d_instantiation(instance):
    assert isinstance(instance, pmtest_D)



@given(instance=pmtest_D_strategy)
def test_pmtest_d_j_setter(instance):
    original = instance.j
    instance.j = original
    assert instance.j == original

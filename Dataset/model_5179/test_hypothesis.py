import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pmtest::A,
    A,
    pmtest::C,
    pmtest::B,
    pmtest::D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pmtest::a_is_not_abstract():
    assert not inspect.isabstract(pmtest::A)


def test_pmtest::a_constructor_exists():
    assert callable(pmtest::A.__init__)


def test_pmtest::a_constructor_args():
    sig = inspect.signature(pmtest::A.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_pmtest::a_has_i():
    assert hasattr(pmtest::A, "i")
    descriptor = None
    for klass in pmtest::A.__mro__:
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



def test_pmtest::c_is_not_abstract():
    assert not inspect.isabstract(pmtest::C)


def test_pmtest::c_constructor_exists():
    assert callable(pmtest::C.__init__)


def test_pmtest::c_constructor_args():
    sig = inspect.signature(pmtest::C.__init__)
    params = list(sig.parameters.keys())



def test_pmtest::b_is_not_abstract():
    assert not inspect.isabstract(pmtest::B)


def test_pmtest::b_constructor_exists():
    assert callable(pmtest::B.__init__)


def test_pmtest::b_constructor_args():
    sig = inspect.signature(pmtest::B.__init__)
    params = list(sig.parameters.keys())



def test_pmtest::d_is_not_abstract():
    assert not inspect.isabstract(pmtest::D)


def test_pmtest::d_constructor_exists():
    assert callable(pmtest::D.__init__)


def test_pmtest::d_constructor_args():
    sig = inspect.signature(pmtest::D.__init__)
    params = list(sig.parameters.keys())
    assert "j" in params, "Missing parameter 'j'"

def test_pmtest::d_has_j():
    assert hasattr(pmtest::D, "j")
    descriptor = None
    for klass in pmtest::D.__mro__:
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
pmtest::A_strategy = st.builds(
    pmtest::A,
    i=
        st.integers()
)
A_strategy = st.builds(
    A,
)
pmtest::C_strategy = st.builds(
    pmtest::C,
)
pmtest::B_strategy = st.builds(
    pmtest::B,
)
pmtest::D_strategy = st.builds(
    pmtest::D,
    j=
        st.integers()
)

@given(instance=pmtest::A_strategy)
@settings(max_examples=50)
def test_pmtest::a_instantiation(instance):
    assert isinstance(instance, pmtest::A)

@given(instance=pmtest::A_strategy)
def test_pmtest::a_i_type(instance):
    assert isinstance(instance.i, int)


@given(instance=pmtest::A_strategy)
def test_pmtest::a_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=pmtest::C_strategy)
@settings(max_examples=50)
def test_pmtest::c_instantiation(instance):
    assert isinstance(instance, pmtest::C)

@given(instance=pmtest::B_strategy)
@settings(max_examples=50)
def test_pmtest::b_instantiation(instance):
    assert isinstance(instance, pmtest::B)

@given(instance=pmtest::D_strategy)
@settings(max_examples=50)
def test_pmtest::d_instantiation(instance):
    assert isinstance(instance, pmtest::D)

@given(instance=pmtest::D_strategy)
def test_pmtest::d_j_type(instance):
    assert isinstance(instance.j, int)


@given(instance=pmtest::D_strategy)
def test_pmtest::d_j_setter(instance):
    original = instance.j
    instance.j = original
    assert instance.j == original

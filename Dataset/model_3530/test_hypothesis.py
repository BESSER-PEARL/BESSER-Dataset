import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    a::B,
    a::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::b_is_not_abstract():
    assert not inspect.isabstract(a::B)


def test_a::b_constructor_exists():
    assert callable(a::B.__init__)


def test_a::b_constructor_args():
    sig = inspect.signature(a::B.__init__)
    params = list(sig.parameters.keys())



def test_a::a_is_not_abstract():
    assert not inspect.isabstract(a::A)


def test_a::a_constructor_exists():
    assert callable(a::A.__init__)


def test_a::a_constructor_args():
    sig = inspect.signature(a::A.__init__)
    params = list(sig.parameters.keys())
    assert "m" in params, "Missing parameter 'm'"

def test_a::a_has_m():
    assert hasattr(a::A, "m")
    descriptor = None
    for klass in a::A.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
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
a::B_strategy = st.builds(
    a::B,
)
a::A_strategy = st.builds(
    a::A,
    m=
        st.integers()
)

@given(instance=a::B_strategy)
@settings(max_examples=50)
def test_a::b_instantiation(instance):
    assert isinstance(instance, a::B)

@given(instance=a::A_strategy)
@settings(max_examples=50)
def test_a::a_instantiation(instance):
    assert isinstance(instance, a::A)

@given(instance=a::A_strategy)
def test_a::a_m_type(instance):
    assert isinstance(instance.m, int)


@given(instance=a::A_strategy)
def test_a::a_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original

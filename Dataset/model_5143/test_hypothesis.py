import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lhs::B,
    lhs::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lhs::b_is_not_abstract():
    assert not inspect.isabstract(lhs::B)


def test_lhs::b_constructor_exists():
    assert callable(lhs::B.__init__)


def test_lhs::b_constructor_args():
    sig = inspect.signature(lhs::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_lhs::b_has_b():
    assert hasattr(lhs::B, "b")
    descriptor = None
    for klass in lhs::B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_lhs::a_is_not_abstract():
    assert not inspect.isabstract(lhs::A)


def test_lhs::a_constructor_exists():
    assert callable(lhs::A.__init__)


def test_lhs::a_constructor_args():
    sig = inspect.signature(lhs::A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_lhs::a_has_a():
    assert hasattr(lhs::A, "a")
    descriptor = None
    for klass in lhs::A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
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
lhs::B_strategy = st.builds(
    lhs::B,
    b=
        safe_text
)
lhs::A_strategy = st.builds(
    lhs::A,
    a=
        safe_text
)

@given(instance=lhs::B_strategy)
@settings(max_examples=50)
def test_lhs::b_instantiation(instance):
    assert isinstance(instance, lhs::B)

@given(instance=lhs::B_strategy)
def test_lhs::b_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=lhs::B_strategy)
def test_lhs::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=lhs::A_strategy)
@settings(max_examples=50)
def test_lhs::a_instantiation(instance):
    assert isinstance(instance, lhs::A)

@given(instance=lhs::A_strategy)
def test_lhs::a_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=lhs::A_strategy)
def test_lhs::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

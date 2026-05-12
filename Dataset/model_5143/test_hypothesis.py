import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lhs_B,
    lhs_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lhs_b_is_not_abstract():
    assert not inspect.isabstract(lhs_B)


def test_lhs_b_constructor_exists():
    assert callable(lhs_B.__init__)


def test_lhs_b_constructor_args():
    sig = inspect.signature(lhs_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_lhs_b_has_b():
    assert hasattr(lhs_B, "b")
    descriptor = None
    for klass in lhs_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_lhs_a_is_not_abstract():
    assert not inspect.isabstract(lhs_A)


def test_lhs_a_constructor_exists():
    assert callable(lhs_A.__init__)


def test_lhs_a_constructor_args():
    sig = inspect.signature(lhs_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_lhs_a_has_a():
    assert hasattr(lhs_A, "a")
    descriptor = None
    for klass in lhs_A.__mro__:
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
lhs_B_strategy = st.builds(
    lhs_B,
    b=
        safe_text
)
lhs_A_strategy = st.builds(
    lhs_A,
    a=
        safe_text
)

@given(instance=lhs_B_strategy)
@settings(max_examples=50)
def test_lhs_b_instantiation(instance):
    assert isinstance(instance, lhs_B)



@given(instance=lhs_B_strategy)
def test_lhs_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=lhs_A_strategy)
@settings(max_examples=50)
def test_lhs_a_instantiation(instance):
    assert isinstance(instance, lhs_A)



@given(instance=lhs_A_strategy)
def test_lhs_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

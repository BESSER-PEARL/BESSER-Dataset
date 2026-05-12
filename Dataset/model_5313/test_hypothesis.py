import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LHS_B,
    LHS_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lhs_b_is_not_abstract():
    assert not inspect.isabstract(LHS_B)


def test_lhs_b_constructor_exists():
    assert callable(LHS_B.__init__)


def test_lhs_b_constructor_args():
    sig = inspect.signature(LHS_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lhs_b_has_name():
    assert hasattr(LHS_B, "name")
    descriptor = None
    for klass in LHS_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lhs_a_is_not_abstract():
    assert not inspect.isabstract(LHS_A)


def test_lhs_a_constructor_exists():
    assert callable(LHS_A.__init__)


def test_lhs_a_constructor_args():
    sig = inspect.signature(LHS_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lhs_a_has_name():
    assert hasattr(LHS_A, "name")
    descriptor = None
    for klass in LHS_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
LHS_B_strategy = st.builds(
    LHS_B,
    name=
        safe_text
)
LHS_A_strategy = st.builds(
    LHS_A,
    name=
        safe_text
)

@given(instance=LHS_B_strategy)
@settings(max_examples=50)
def test_lhs_b_instantiation(instance):
    assert isinstance(instance, LHS_B)



@given(instance=LHS_B_strategy)
def test_lhs_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LHS_A_strategy)
@settings(max_examples=50)
def test_lhs_a_instantiation(instance):
    assert isinstance(instance, LHS_A)



@given(instance=LHS_A_strategy)
def test_lhs_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

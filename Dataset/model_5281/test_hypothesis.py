import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AB_A,
    AB_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ab_a_is_not_abstract():
    assert not inspect.isabstract(AB_A)


def test_ab_a_constructor_exists():
    assert callable(AB_A.__init__)


def test_ab_a_constructor_args():
    sig = inspect.signature(AB_A.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_ab_a_has_i():
    assert hasattr(AB_A, "i")
    descriptor = None
    for klass in AB_A.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)



def test_ab_b_is_not_abstract():
    assert not inspect.isabstract(AB_B)


def test_ab_b_constructor_exists():
    assert callable(AB_B.__init__)


def test_ab_b_constructor_args():
    sig = inspect.signature(AB_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ab_b_has_name():
    assert hasattr(AB_B, "name")
    descriptor = None
    for klass in AB_B.__mro__:
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
AB_A_strategy = st.builds(
    AB_A,
    i=
        st.integers()
)
AB_B_strategy = st.builds(
    AB_B,
    name=
        safe_text
)

@given(instance=AB_A_strategy)
@settings(max_examples=50)
def test_ab_a_instantiation(instance):
    assert isinstance(instance, AB_A)



@given(instance=AB_A_strategy)
def test_ab_a_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=AB_B_strategy)
@settings(max_examples=50)
def test_ab_b_instantiation(instance):
    assert isinstance(instance, AB_B)



@given(instance=AB_B_strategy)
def test_ab_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

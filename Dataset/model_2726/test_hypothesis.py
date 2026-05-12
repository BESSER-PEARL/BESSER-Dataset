import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A,
    direction_B,
    direction_A,
    direction_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_direction_b_is_not_abstract():
    assert not inspect.isabstract(direction_B)


def test_direction_b_constructor_exists():
    assert callable(direction_B.__init__)


def test_direction_b_constructor_args():
    sig = inspect.signature(direction_B.__init__)
    params = list(sig.parameters.keys())



def test_direction_a_is_not_abstract():
    assert not inspect.isabstract(direction_A)


def test_direction_a_constructor_exists():
    assert callable(direction_A.__init__)


def test_direction_a_constructor_args():
    sig = inspect.signature(direction_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_direction_a_has_name():
    assert hasattr(direction_A, "name")
    descriptor = None
    for klass in direction_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_direction_c_is_not_abstract():
    assert not inspect.isabstract(direction_C)


def test_direction_c_constructor_exists():
    assert callable(direction_C.__init__)


def test_direction_c_constructor_args():
    sig = inspect.signature(direction_C.__init__)
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
A_strategy = st.builds(
    A,
)
direction_B_strategy = st.builds(
    direction_B,
)
direction_A_strategy = st.builds(
    direction_A,
    name=
        safe_text
)
direction_C_strategy = st.builds(
    direction_C,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=direction_B_strategy)
@settings(max_examples=50)
def test_direction_b_instantiation(instance):
    assert isinstance(instance, direction_B)

@given(instance=direction_A_strategy)
@settings(max_examples=50)
def test_direction_a_instantiation(instance):
    assert isinstance(instance, direction_A)



@given(instance=direction_A_strategy)
def test_direction_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=direction_C_strategy)
@settings(max_examples=50)
def test_direction_c_instantiation(instance):
    assert isinstance(instance, direction_C)

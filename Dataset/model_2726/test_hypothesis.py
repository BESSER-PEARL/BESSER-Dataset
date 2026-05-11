import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    direction::B,
    direction::A,
    direction::C,
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



def test_direction::b_is_not_abstract():
    assert not inspect.isabstract(direction::B)


def test_direction::b_constructor_exists():
    assert callable(direction::B.__init__)


def test_direction::b_constructor_args():
    sig = inspect.signature(direction::B.__init__)
    params = list(sig.parameters.keys())



def test_direction::a_is_not_abstract():
    assert not inspect.isabstract(direction::A)


def test_direction::a_constructor_exists():
    assert callable(direction::A.__init__)


def test_direction::a_constructor_args():
    sig = inspect.signature(direction::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_direction::a_has_name():
    assert hasattr(direction::A, "name")
    descriptor = None
    for klass in direction::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_direction::c_is_not_abstract():
    assert not inspect.isabstract(direction::C)


def test_direction::c_constructor_exists():
    assert callable(direction::C.__init__)


def test_direction::c_constructor_args():
    sig = inspect.signature(direction::C.__init__)
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
direction::B_strategy = st.builds(
    direction::B,
)
direction::A_strategy = st.builds(
    direction::A,
    name=
        safe_text
)
direction::C_strategy = st.builds(
    direction::C,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=direction::B_strategy)
@settings(max_examples=50)
def test_direction::b_instantiation(instance):
    assert isinstance(instance, direction::B)

@given(instance=direction::A_strategy)
@settings(max_examples=50)
def test_direction::a_instantiation(instance):
    assert isinstance(instance, direction::A)

@given(instance=direction::A_strategy)
def test_direction::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=direction::A_strategy)
def test_direction::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=direction::C_strategy)
@settings(max_examples=50)
def test_direction::c_instantiation(instance):
    assert isinstance(instance, direction::C)

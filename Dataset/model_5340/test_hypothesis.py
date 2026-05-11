import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B::B2,
    B::B1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::b2_is_not_abstract():
    assert not inspect.isabstract(B::B2)


def test_b::b2_constructor_exists():
    assert callable(B::B2.__init__)


def test_b::b2_constructor_args():
    sig = inspect.signature(B::B2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::b2_has_name():
    assert hasattr(B::B2, "name")
    descriptor = None
    for klass in B::B2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::b1_is_not_abstract():
    assert not inspect.isabstract(B::B1)


def test_b::b1_constructor_exists():
    assert callable(B::B1.__init__)


def test_b::b1_constructor_args():
    sig = inspect.signature(B::B1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::b1_has_name():
    assert hasattr(B::B1, "name")
    descriptor = None
    for klass in B::B1.__mro__:
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
B::B2_strategy = st.builds(
    B::B2,
    name=
        safe_text
)
B::B1_strategy = st.builds(
    B::B1,
    name=
        safe_text
)

@given(instance=B::B2_strategy)
@settings(max_examples=50)
def test_b::b2_instantiation(instance):
    assert isinstance(instance, B::B2)

@given(instance=B::B2_strategy)
def test_b::b2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=B::B2_strategy)
def test_b::b2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B::B1_strategy)
@settings(max_examples=50)
def test_b::b1_instantiation(instance):
    assert isinstance(instance, B::B1)

@given(instance=B::B1_strategy)
def test_b::b1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=B::B1_strategy)
def test_b::b1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

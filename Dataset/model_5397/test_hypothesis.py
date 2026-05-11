import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(B::B)


def test_b::b_constructor_exists():
    assert callable(B::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(B::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description2" in params, "Missing parameter 'description2'"
    assert "description1" in params, "Missing parameter 'description1'"

def test_b::b_has_name():
    assert hasattr(B::B, "name")
    descriptor = None
    for klass in B::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_b::b_has_description2():
    assert hasattr(B::B, "description2")
    descriptor = None
    for klass in B::B.__mro__:
        if "description2" in klass.__dict__:
            descriptor = klass.__dict__["description2"]
            break
    assert isinstance(descriptor, property)

def test_b::b_has_description1():
    assert hasattr(B::B, "description1")
    descriptor = None
    for klass in B::B.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
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
B::B_strategy = st.builds(
    B::B,
    name=
        safe_text,
    description2=
        safe_text,
    description1=
        safe_text
)

@given(instance=B::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, B::B)

@given(instance=B::B_strategy)
def test_b::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=B::B_strategy)
def test_b::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B::B_strategy)
def test_b::b_description2_type(instance):
    assert isinstance(instance.description2, str)


@given(instance=B::B_strategy)
def test_b::b_description2_setter(instance):
    original = instance.description2
    instance.description2 = original
    assert instance.description2 == original

@given(instance=B::B_strategy)
def test_b::b_description1_type(instance):
    assert isinstance(instance.description1, str)


@given(instance=B::B_strategy)
def test_b::b_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original

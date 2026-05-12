import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeB_B,
    TypeB_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeb_b_is_not_abstract():
    assert not inspect.isabstract(TypeB_B)


def test_typeb_b_constructor_exists():
    assert callable(TypeB_B.__init__)


def test_typeb_b_constructor_args():
    sig = inspect.signature(TypeB_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb_b_has_name():
    assert hasattr(TypeB_B, "name")
    descriptor = None
    for klass in TypeB_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb_a_is_not_abstract():
    assert not inspect.isabstract(TypeB_A)


def test_typeb_a_constructor_exists():
    assert callable(TypeB_A.__init__)


def test_typeb_a_constructor_args():
    sig = inspect.signature(TypeB_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb_a_has_name():
    assert hasattr(TypeB_A, "name")
    descriptor = None
    for klass in TypeB_A.__mro__:
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
TypeB_B_strategy = st.builds(
    TypeB_B,
    name=
        safe_text
)
TypeB_A_strategy = st.builds(
    TypeB_A,
    name=
        safe_text
)

@given(instance=TypeB_B_strategy)
@settings(max_examples=50)
def test_typeb_b_instantiation(instance):
    assert isinstance(instance, TypeB_B)



@given(instance=TypeB_B_strategy)
def test_typeb_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeB_A_strategy)
@settings(max_examples=50)
def test_typeb_a_instantiation(instance):
    assert isinstance(instance, TypeB_A)



@given(instance=TypeB_A_strategy)
def test_typeb_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

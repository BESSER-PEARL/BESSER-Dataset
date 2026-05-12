import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(B_B)


def test_b_b_constructor_exists():
    assert callable(B_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(B_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description1" in params, "Missing parameter 'description1'"
    assert "description2" in params, "Missing parameter 'description2'"

def test_b_b_has_name():
    assert hasattr(B_B, "name")
    descriptor = None
    for klass in B_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_b_b_has_description1():
    assert hasattr(B_B, "description1")
    descriptor = None
    for klass in B_B.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)

def test_b_b_has_description2():
    assert hasattr(B_B, "description2")
    descriptor = None
    for klass in B_B.__mro__:
        if "description2" in klass.__dict__:
            descriptor = klass.__dict__["description2"]
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
B_B_strategy = st.builds(
    B_B,
    name=
        safe_text,
    description1=
        safe_text,
    description2=
        safe_text
)

@given(instance=B_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, B_B)



@given(instance=B_B_strategy)
def test_b_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=B_B_strategy)
def test_b_b_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original



@given(instance=B_B_strategy)
def test_b_b_description2_setter(instance):
    original = instance.description2
    instance.description2 = original
    assert instance.description2 == original

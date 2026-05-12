import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B_B2,
    B_B1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_b2_is_not_abstract():
    assert not inspect.isabstract(B_B2)


def test_b_b2_constructor_exists():
    assert callable(B_B2.__init__)


def test_b_b2_constructor_args():
    sig = inspect.signature(B_B2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_b2_has_name():
    assert hasattr(B_B2, "name")
    descriptor = None
    for klass in B_B2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b_b1_is_not_abstract():
    assert not inspect.isabstract(B_B1)


def test_b_b1_constructor_exists():
    assert callable(B_B1.__init__)


def test_b_b1_constructor_args():
    sig = inspect.signature(B_B1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_b1_has_name():
    assert hasattr(B_B1, "name")
    descriptor = None
    for klass in B_B1.__mro__:
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
B_B2_strategy = st.builds(
    B_B2,
    name=
        safe_text
)
B_B1_strategy = st.builds(
    B_B1,
    name=
        safe_text
)

@given(instance=B_B2_strategy)
@settings(max_examples=50)
def test_b_b2_instantiation(instance):
    assert isinstance(instance, B_B2)



@given(instance=B_B2_strategy)
def test_b_b2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B_B1_strategy)
@settings(max_examples=50)
def test_b_b1_instantiation(instance):
    assert isinstance(instance, B_B1)



@given(instance=B_B1_strategy)
def test_b_b1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

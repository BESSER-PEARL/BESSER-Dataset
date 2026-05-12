import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplea_B,
    simplea_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplea_b_is_not_abstract():
    assert not inspect.isabstract(simplea_B)


def test_simplea_b_constructor_exists():
    assert callable(simplea_B.__init__)


def test_simplea_b_constructor_args():
    sig = inspect.signature(simplea_B.__init__)
    params = list(sig.parameters.keys())



def test_simplea_a_is_not_abstract():
    assert not inspect.isabstract(simplea_A)


def test_simplea_a_constructor_exists():
    assert callable(simplea_A.__init__)


def test_simplea_a_constructor_args():
    sig = inspect.signature(simplea_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplea_a_has_name():
    assert hasattr(simplea_A, "name")
    descriptor = None
    for klass in simplea_A.__mro__:
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
simplea_B_strategy = st.builds(
    simplea_B,
)
simplea_A_strategy = st.builds(
    simplea_A,
    name=
        safe_text
)

@given(instance=simplea_B_strategy)
@settings(max_examples=50)
def test_simplea_b_instantiation(instance):
    assert isinstance(instance, simplea_B)

@given(instance=simplea_A_strategy)
@settings(max_examples=50)
def test_simplea_a_instantiation(instance):
    assert isinstance(instance, simplea_A)



@given(instance=simplea_A_strategy)
def test_simplea_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

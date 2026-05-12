import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RHS_X,
    RHS_Y,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rhs_x_is_not_abstract():
    assert not inspect.isabstract(RHS_X)


def test_rhs_x_constructor_exists():
    assert callable(RHS_X.__init__)


def test_rhs_x_constructor_args():
    sig = inspect.signature(RHS_X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rhs_x_has_name():
    assert hasattr(RHS_X, "name")
    descriptor = None
    for klass in RHS_X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rhs_y_is_not_abstract():
    assert not inspect.isabstract(RHS_Y)


def test_rhs_y_constructor_exists():
    assert callable(RHS_Y.__init__)


def test_rhs_y_constructor_args():
    sig = inspect.signature(RHS_Y.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rhs_y_has_name():
    assert hasattr(RHS_Y, "name")
    descriptor = None
    for klass in RHS_Y.__mro__:
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
RHS_X_strategy = st.builds(
    RHS_X,
    name=
        safe_text
)
RHS_Y_strategy = st.builds(
    RHS_Y,
    name=
        safe_text
)

@given(instance=RHS_X_strategy)
@settings(max_examples=50)
def test_rhs_x_instantiation(instance):
    assert isinstance(instance, RHS_X)



@given(instance=RHS_X_strategy)
def test_rhs_x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RHS_Y_strategy)
@settings(max_examples=50)
def test_rhs_y_instantiation(instance):
    assert isinstance(instance, RHS_Y)



@given(instance=RHS_Y_strategy)
def test_rhs_y_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

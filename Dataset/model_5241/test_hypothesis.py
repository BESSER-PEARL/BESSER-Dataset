import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rhs_Y,
    rhs_X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rhs_y_is_not_abstract():
    assert not inspect.isabstract(rhs_Y)


def test_rhs_y_constructor_exists():
    assert callable(rhs_Y.__init__)


def test_rhs_y_constructor_args():
    sig = inspect.signature(rhs_Y.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"

def test_rhs_y_has_y():
    assert hasattr(rhs_Y, "y")
    descriptor = None
    for klass in rhs_Y.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_rhs_x_is_not_abstract():
    assert not inspect.isabstract(rhs_X)


def test_rhs_x_constructor_exists():
    assert callable(rhs_X.__init__)


def test_rhs_x_constructor_args():
    sig = inspect.signature(rhs_X.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_rhs_x_has_x():
    assert hasattr(rhs_X, "x")
    descriptor = None
    for klass in rhs_X.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
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
rhs_Y_strategy = st.builds(
    rhs_Y,
    y=
        safe_text
)
rhs_X_strategy = st.builds(
    rhs_X,
    x=
        safe_text
)

@given(instance=rhs_Y_strategy)
@settings(max_examples=50)
def test_rhs_y_instantiation(instance):
    assert isinstance(instance, rhs_Y)



@given(instance=rhs_Y_strategy)
def test_rhs_y_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=rhs_X_strategy)
@settings(max_examples=50)
def test_rhs_x_instantiation(instance):
    assert isinstance(instance, rhs_X)



@given(instance=rhs_X_strategy)
def test_rhs_x_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

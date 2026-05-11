import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rhs::Y,
    rhs::X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rhs::y_is_not_abstract():
    assert not inspect.isabstract(rhs::Y)


def test_rhs::y_constructor_exists():
    assert callable(rhs::Y.__init__)


def test_rhs::y_constructor_args():
    sig = inspect.signature(rhs::Y.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"

def test_rhs::y_has_y():
    assert hasattr(rhs::Y, "y")
    descriptor = None
    for klass in rhs::Y.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_rhs::x_is_not_abstract():
    assert not inspect.isabstract(rhs::X)


def test_rhs::x_constructor_exists():
    assert callable(rhs::X.__init__)


def test_rhs::x_constructor_args():
    sig = inspect.signature(rhs::X.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_rhs::x_has_x():
    assert hasattr(rhs::X, "x")
    descriptor = None
    for klass in rhs::X.__mro__:
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
rhs::Y_strategy = st.builds(
    rhs::Y,
    y=
        safe_text
)
rhs::X_strategy = st.builds(
    rhs::X,
    x=
        safe_text
)

@given(instance=rhs::Y_strategy)
@settings(max_examples=50)
def test_rhs::y_instantiation(instance):
    assert isinstance(instance, rhs::Y)

@given(instance=rhs::Y_strategy)
def test_rhs::y_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=rhs::Y_strategy)
def test_rhs::y_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=rhs::X_strategy)
@settings(max_examples=50)
def test_rhs::x_instantiation(instance):
    assert isinstance(instance, rhs::X)

@given(instance=rhs::X_strategy)
def test_rhs::x_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=rhs::X_strategy)
def test_rhs::x_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RHS::V,
    RHS::X,
    RHS::W,
    RHS::Y,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rhs::v_is_not_abstract():
    assert not inspect.isabstract(RHS::V)


def test_rhs::v_constructor_exists():
    assert callable(RHS::V.__init__)


def test_rhs::v_constructor_args():
    sig = inspect.signature(RHS::V.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rhs::v_has_name():
    assert hasattr(RHS::V, "name")
    descriptor = None
    for klass in RHS::V.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rhs::x_is_not_abstract():
    assert not inspect.isabstract(RHS::X)


def test_rhs::x_constructor_exists():
    assert callable(RHS::X.__init__)


def test_rhs::x_constructor_args():
    sig = inspect.signature(RHS::X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rhs::x_has_name():
    assert hasattr(RHS::X, "name")
    descriptor = None
    for klass in RHS::X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rhs::w_is_not_abstract():
    assert not inspect.isabstract(RHS::W)


def test_rhs::w_constructor_exists():
    assert callable(RHS::W.__init__)


def test_rhs::w_constructor_args():
    sig = inspect.signature(RHS::W.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rhs::w_has_name():
    assert hasattr(RHS::W, "name")
    descriptor = None
    for klass in RHS::W.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rhs::y_is_not_abstract():
    assert not inspect.isabstract(RHS::Y)


def test_rhs::y_constructor_exists():
    assert callable(RHS::Y.__init__)


def test_rhs::y_constructor_args():
    sig = inspect.signature(RHS::Y.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rhs::y_has_name():
    assert hasattr(RHS::Y, "name")
    descriptor = None
    for klass in RHS::Y.__mro__:
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
RHS::V_strategy = st.builds(
    RHS::V,
    name=
        safe_text
)
RHS::X_strategy = st.builds(
    RHS::X,
    name=
        safe_text
)
RHS::W_strategy = st.builds(
    RHS::W,
    name=
        safe_text
)
RHS::Y_strategy = st.builds(
    RHS::Y,
    name=
        safe_text
)

@given(instance=RHS::V_strategy)
@settings(max_examples=50)
def test_rhs::v_instantiation(instance):
    assert isinstance(instance, RHS::V)

@given(instance=RHS::V_strategy)
def test_rhs::v_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RHS::V_strategy)
def test_rhs::v_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RHS::X_strategy)
@settings(max_examples=50)
def test_rhs::x_instantiation(instance):
    assert isinstance(instance, RHS::X)

@given(instance=RHS::X_strategy)
def test_rhs::x_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RHS::X_strategy)
def test_rhs::x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RHS::W_strategy)
@settings(max_examples=50)
def test_rhs::w_instantiation(instance):
    assert isinstance(instance, RHS::W)

@given(instance=RHS::W_strategy)
def test_rhs::w_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RHS::W_strategy)
def test_rhs::w_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RHS::Y_strategy)
@settings(max_examples=50)
def test_rhs::y_instantiation(instance):
    assert isinstance(instance, RHS::Y)

@given(instance=RHS::Y_strategy)
def test_rhs::y_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RHS::Y_strategy)
def test_rhs::y_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

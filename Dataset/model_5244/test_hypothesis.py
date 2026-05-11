import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hExample::6::RHS::Z,
    hExample::6::RHS::Y,
    hExample::6::RHS::X,
    hExample::6::RHS::model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hexample::6::rhs::z_is_not_abstract():
    assert not inspect.isabstract(hExample::6::RHS::Z)


def test_hexample::6::rhs::z_constructor_exists():
    assert callable(hExample::6::RHS::Z.__init__)


def test_hexample::6::rhs::z_constructor_args():
    sig = inspect.signature(hExample::6::RHS::Z.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hexample::6::rhs::z_has_name():
    assert hasattr(hExample::6::RHS::Z, "name")
    descriptor = None
    for klass in hExample::6::RHS::Z.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hexample::6::rhs::y_is_not_abstract():
    assert not inspect.isabstract(hExample::6::RHS::Y)


def test_hexample::6::rhs::y_constructor_exists():
    assert callable(hExample::6::RHS::Y.__init__)


def test_hexample::6::rhs::y_constructor_args():
    sig = inspect.signature(hExample::6::RHS::Y.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hexample::6::rhs::y_has_name():
    assert hasattr(hExample::6::RHS::Y, "name")
    descriptor = None
    for klass in hExample::6::RHS::Y.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hexample::6::rhs::x_is_not_abstract():
    assert not inspect.isabstract(hExample::6::RHS::X)


def test_hexample::6::rhs::x_constructor_exists():
    assert callable(hExample::6::RHS::X.__init__)


def test_hexample::6::rhs::x_constructor_args():
    sig = inspect.signature(hExample::6::RHS::X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hexample::6::rhs::x_has_name():
    assert hasattr(hExample::6::RHS::X, "name")
    descriptor = None
    for klass in hExample::6::RHS::X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hexample::6::rhs::model_is_not_abstract():
    assert not inspect.isabstract(hExample::6::RHS::model)


def test_hexample::6::rhs::model_constructor_exists():
    assert callable(hExample::6::RHS::model.__init__)


def test_hexample::6::rhs::model_constructor_args():
    sig = inspect.signature(hExample::6::RHS::model.__init__)
    params = list(sig.parameters.keys())


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
hExample::6::RHS::Z_strategy = st.builds(
    hExample::6::RHS::Z,
    name=
        safe_text
)
hExample::6::RHS::Y_strategy = st.builds(
    hExample::6::RHS::Y,
    name=
        safe_text
)
hExample::6::RHS::X_strategy = st.builds(
    hExample::6::RHS::X,
    name=
        safe_text
)
hExample::6::RHS::model_strategy = st.builds(
    hExample::6::RHS::model,
)

@given(instance=hExample::6::RHS::Z_strategy)
@settings(max_examples=50)
def test_hexample::6::rhs::z_instantiation(instance):
    assert isinstance(instance, hExample::6::RHS::Z)

@given(instance=hExample::6::RHS::Z_strategy)
def test_hexample::6::rhs::z_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hExample::6::RHS::Z_strategy)
def test_hexample::6::rhs::z_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hExample::6::RHS::Y_strategy)
@settings(max_examples=50)
def test_hexample::6::rhs::y_instantiation(instance):
    assert isinstance(instance, hExample::6::RHS::Y)

@given(instance=hExample::6::RHS::Y_strategy)
def test_hexample::6::rhs::y_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hExample::6::RHS::Y_strategy)
def test_hexample::6::rhs::y_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hExample::6::RHS::X_strategy)
@settings(max_examples=50)
def test_hexample::6::rhs::x_instantiation(instance):
    assert isinstance(instance, hExample::6::RHS::X)

@given(instance=hExample::6::RHS::X_strategy)
def test_hexample::6::rhs::x_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hExample::6::RHS::X_strategy)
def test_hexample::6::rhs::x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hExample::6::RHS::model_strategy)
@settings(max_examples=50)
def test_hexample::6::rhs::model_instantiation(instance):
    assert isinstance(instance, hExample::6::RHS::model)

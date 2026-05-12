import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    complworld_Satellite,
    complworld_Mars,
    complworld_Thing,
    complworld_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_complworld_satellite_is_not_abstract():
    assert not inspect.isabstract(complworld_Satellite)


def test_complworld_satellite_constructor_exists():
    assert callable(complworld_Satellite.__init__)


def test_complworld_satellite_constructor_args():
    sig = inspect.signature(complworld_Satellite.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_complworld_satellite_has_name():
    assert hasattr(complworld_Satellite, "name")
    descriptor = None
    for klass in complworld_Satellite.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complworld_mars_is_not_abstract():
    assert not inspect.isabstract(complworld_Mars)


def test_complworld_mars_constructor_exists():
    assert callable(complworld_Mars.__init__)


def test_complworld_mars_constructor_args():
    sig = inspect.signature(complworld_Mars.__init__)
    params = list(sig.parameters.keys())



def test_complworld_thing_is_not_abstract():
    assert not inspect.isabstract(complworld_Thing)


def test_complworld_thing_constructor_exists():
    assert callable(complworld_Thing.__init__)


def test_complworld_thing_constructor_args():
    sig = inspect.signature(complworld_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_complworld_thing_has_name():
    assert hasattr(complworld_Thing, "name")
    descriptor = None
    for klass in complworld_Thing.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complworld_world_is_not_abstract():
    assert not inspect.isabstract(complworld_World)


def test_complworld_world_constructor_exists():
    assert callable(complworld_World.__init__)


def test_complworld_world_constructor_args():
    sig = inspect.signature(complworld_World.__init__)
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
complworld_Satellite_strategy = st.builds(
    complworld_Satellite,
    name=
        safe_text
)
complworld_Mars_strategy = st.builds(
    complworld_Mars,
)
complworld_Thing_strategy = st.builds(
    complworld_Thing,
    name=
        safe_text
)
complworld_World_strategy = st.builds(
    complworld_World,
)

@given(instance=complworld_Satellite_strategy)
@settings(max_examples=50)
def test_complworld_satellite_instantiation(instance):
    assert isinstance(instance, complworld_Satellite)



@given(instance=complworld_Satellite_strategy)
def test_complworld_satellite_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=complworld_Mars_strategy)
@settings(max_examples=50)
def test_complworld_mars_instantiation(instance):
    assert isinstance(instance, complworld_Mars)

@given(instance=complworld_Thing_strategy)
@settings(max_examples=50)
def test_complworld_thing_instantiation(instance):
    assert isinstance(instance, complworld_Thing)



@given(instance=complworld_Thing_strategy)
def test_complworld_thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=complworld_World_strategy)
@settings(max_examples=50)
def test_complworld_world_instantiation(instance):
    assert isinstance(instance, complworld_World)

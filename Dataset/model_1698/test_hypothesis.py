import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    complworld::Satellite,
    complworld::Mars,
    complworld::Thing,
    complworld::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_complworld::satellite_is_not_abstract():
    assert not inspect.isabstract(complworld::Satellite)


def test_complworld::satellite_constructor_exists():
    assert callable(complworld::Satellite.__init__)


def test_complworld::satellite_constructor_args():
    sig = inspect.signature(complworld::Satellite.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_complworld::satellite_has_name():
    assert hasattr(complworld::Satellite, "name")
    descriptor = None
    for klass in complworld::Satellite.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complworld::mars_is_not_abstract():
    assert not inspect.isabstract(complworld::Mars)


def test_complworld::mars_constructor_exists():
    assert callable(complworld::Mars.__init__)


def test_complworld::mars_constructor_args():
    sig = inspect.signature(complworld::Mars.__init__)
    params = list(sig.parameters.keys())



def test_complworld::thing_is_not_abstract():
    assert not inspect.isabstract(complworld::Thing)


def test_complworld::thing_constructor_exists():
    assert callable(complworld::Thing.__init__)


def test_complworld::thing_constructor_args():
    sig = inspect.signature(complworld::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_complworld::thing_has_name():
    assert hasattr(complworld::Thing, "name")
    descriptor = None
    for klass in complworld::Thing.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complworld::world_is_not_abstract():
    assert not inspect.isabstract(complworld::World)


def test_complworld::world_constructor_exists():
    assert callable(complworld::World.__init__)


def test_complworld::world_constructor_args():
    sig = inspect.signature(complworld::World.__init__)
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
complworld::Satellite_strategy = st.builds(
    complworld::Satellite,
    name=
        safe_text
)
complworld::Mars_strategy = st.builds(
    complworld::Mars,
)
complworld::Thing_strategy = st.builds(
    complworld::Thing,
    name=
        safe_text
)
complworld::World_strategy = st.builds(
    complworld::World,
)

@given(instance=complworld::Satellite_strategy)
@settings(max_examples=50)
def test_complworld::satellite_instantiation(instance):
    assert isinstance(instance, complworld::Satellite)

@given(instance=complworld::Satellite_strategy)
def test_complworld::satellite_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=complworld::Satellite_strategy)
def test_complworld::satellite_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=complworld::Mars_strategy)
@settings(max_examples=50)
def test_complworld::mars_instantiation(instance):
    assert isinstance(instance, complworld::Mars)

@given(instance=complworld::Thing_strategy)
@settings(max_examples=50)
def test_complworld::thing_instantiation(instance):
    assert isinstance(instance, complworld::Thing)

@given(instance=complworld::Thing_strategy)
def test_complworld::thing_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=complworld::Thing_strategy)
def test_complworld::thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=complworld::World_strategy)
@settings(max_examples=50)
def test_complworld::world_instantiation(instance):
    assert isinstance(instance, complworld::World)

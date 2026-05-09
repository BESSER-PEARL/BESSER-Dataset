import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stuff::World,
    stuff::Property,
    stuff::Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stuff::world_is_not_abstract():
    assert not inspect.isabstract(stuff::World)


def test_stuff::world_constructor_exists():
    assert callable(stuff::World.__init__)


def test_stuff::world_constructor_args():
    sig = inspect.signature(stuff::World.__init__)
    params = list(sig.parameters.keys())



def test_stuff::property_is_not_abstract():
    assert not inspect.isabstract(stuff::Property)


def test_stuff::property_constructor_exists():
    assert callable(stuff::Property.__init__)


def test_stuff::property_constructor_args():
    sig = inspect.signature(stuff::Property.__init__)
    params = list(sig.parameters.keys())
    assert "intrinsic" in params, "Missing parameter 'intrinsic'"
    assert "name" in params, "Missing parameter 'name'"

def test_stuff::property_has_intrinsic():
    assert hasattr(stuff::Property, "intrinsic")
    descriptor = None
    for klass in stuff::Property.__mro__:
        if "intrinsic" in klass.__dict__:
            descriptor = klass.__dict__["intrinsic"]
            break
    assert isinstance(descriptor, property)

def test_stuff::property_has_name():
    assert hasattr(stuff::Property, "name")
    descriptor = None
    for klass in stuff::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stuff::thing_is_not_abstract():
    assert not inspect.isabstract(stuff::Thing)


def test_stuff::thing_constructor_exists():
    assert callable(stuff::Thing.__init__)


def test_stuff::thing_constructor_args():
    sig = inspect.signature(stuff::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stuff::thing_has_name():
    assert hasattr(stuff::Thing, "name")
    descriptor = None
    for klass in stuff::Thing.__mro__:
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
stuff::World_strategy = st.builds(
    stuff::World,
)
stuff::Property_strategy = st.builds(
    stuff::Property,
    intrinsic=
        st.booleans(),
    name=
        safe_text
)
stuff::Thing_strategy = st.builds(
    stuff::Thing,
    name=
        safe_text
)

@given(instance=stuff::World_strategy)
@settings(max_examples=50)
def test_stuff::world_instantiation(instance):
    assert isinstance(instance, stuff::World)

@given(instance=stuff::Property_strategy)
@settings(max_examples=50)
def test_stuff::property_instantiation(instance):
    assert isinstance(instance, stuff::Property)

@given(instance=stuff::Property_strategy)
def test_stuff::property_intrinsic_type(instance):
    assert isinstance(instance.intrinsic, bool)


@given(instance=stuff::Property_strategy)
def test_stuff::property_intrinsic_setter(instance):
    original = instance.intrinsic
    instance.intrinsic = original
    assert instance.intrinsic == original

@given(instance=stuff::Property_strategy)
def test_stuff::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stuff::Property_strategy)
def test_stuff::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stuff::Thing_strategy)
@settings(max_examples=50)
def test_stuff::thing_instantiation(instance):
    assert isinstance(instance, stuff::Thing)

@given(instance=stuff::Thing_strategy)
def test_stuff::thing_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stuff::Thing_strategy)
def test_stuff::thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stuff_World,
    stuff_Property,
    stuff_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stuff_world_is_not_abstract():
    assert not inspect.isabstract(stuff_World)


def test_stuff_world_constructor_exists():
    assert callable(stuff_World.__init__)


def test_stuff_world_constructor_args():
    sig = inspect.signature(stuff_World.__init__)
    params = list(sig.parameters.keys())



def test_stuff_property_is_not_abstract():
    assert not inspect.isabstract(stuff_Property)


def test_stuff_property_constructor_exists():
    assert callable(stuff_Property.__init__)


def test_stuff_property_constructor_args():
    sig = inspect.signature(stuff_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "intrinsic" in params, "Missing parameter 'intrinsic'"

def test_stuff_property_has_name():
    assert hasattr(stuff_Property, "name")
    descriptor = None
    for klass in stuff_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_stuff_property_has_intrinsic():
    assert hasattr(stuff_Property, "intrinsic")
    descriptor = None
    for klass in stuff_Property.__mro__:
        if "intrinsic" in klass.__dict__:
            descriptor = klass.__dict__["intrinsic"]
            break
    assert isinstance(descriptor, property)



def test_stuff_thing_is_not_abstract():
    assert not inspect.isabstract(stuff_Thing)


def test_stuff_thing_constructor_exists():
    assert callable(stuff_Thing.__init__)


def test_stuff_thing_constructor_args():
    sig = inspect.signature(stuff_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stuff_thing_has_name():
    assert hasattr(stuff_Thing, "name")
    descriptor = None
    for klass in stuff_Thing.__mro__:
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
stuff_World_strategy = st.builds(
    stuff_World,
)
stuff_Property_strategy = st.builds(
    stuff_Property,
    name=
        safe_text,
    intrinsic=
        st.booleans()
)
stuff_Thing_strategy = st.builds(
    stuff_Thing,
    name=
        safe_text
)

@given(instance=stuff_World_strategy)
@settings(max_examples=50)
def test_stuff_world_instantiation(instance):
    assert isinstance(instance, stuff_World)

@given(instance=stuff_Property_strategy)
@settings(max_examples=50)
def test_stuff_property_instantiation(instance):
    assert isinstance(instance, stuff_Property)



@given(instance=stuff_Property_strategy)
def test_stuff_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=stuff_Property_strategy)
def test_stuff_property_intrinsic_setter(instance):
    original = instance.intrinsic
    instance.intrinsic = original
    assert instance.intrinsic == original

@given(instance=stuff_Thing_strategy)
@settings(max_examples=50)
def test_stuff_thing_instantiation(instance):
    assert isinstance(instance, stuff_Thing)



@given(instance=stuff_Thing_strategy)
def test_stuff_thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

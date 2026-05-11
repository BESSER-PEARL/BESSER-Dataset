import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    genealogy::Person,
    genealogy::Genealogy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genealogy::person_is_not_abstract():
    assert not inspect.isabstract(genealogy::Person)


def test_genealogy::person_constructor_exists():
    assert callable(genealogy::Person.__init__)


def test_genealogy::person_constructor_args():
    sig = inspect.signature(genealogy::Person.__init__)
    params = list(sig.parameters.keys())
    assert "alive" in params, "Missing parameter 'alive'"
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_genealogy::person_has_alive():
    assert hasattr(genealogy::Person, "alive")
    descriptor = None
    for klass in genealogy::Person.__mro__:
        if "alive" in klass.__dict__:
            descriptor = klass.__dict__["alive"]
            break
    assert isinstance(descriptor, property)

def test_genealogy::person_has_age():
    assert hasattr(genealogy::Person, "age")
    descriptor = None
    for klass in genealogy::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_genealogy::person_has_name():
    assert hasattr(genealogy::Person, "name")
    descriptor = None
    for klass in genealogy::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_genealogy::genealogy_is_not_abstract():
    assert not inspect.isabstract(genealogy::Genealogy)


def test_genealogy::genealogy_constructor_exists():
    assert callable(genealogy::Genealogy.__init__)


def test_genealogy::genealogy_constructor_args():
    sig = inspect.signature(genealogy::Genealogy.__init__)
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
genealogy::Person_strategy = st.builds(
    genealogy::Person,
    alive=
        st.booleans(),
    age=
        st.integers(),
    name=
        safe_text
)
genealogy::Genealogy_strategy = st.builds(
    genealogy::Genealogy,
)

@given(instance=genealogy::Person_strategy)
@settings(max_examples=50)
def test_genealogy::person_instantiation(instance):
    assert isinstance(instance, genealogy::Person)

@given(instance=genealogy::Person_strategy)
def test_genealogy::person_alive_type(instance):
    assert isinstance(instance.alive, bool)


@given(instance=genealogy::Person_strategy)
def test_genealogy::person_alive_setter(instance):
    original = instance.alive
    instance.alive = original
    assert instance.alive == original

@given(instance=genealogy::Person_strategy)
def test_genealogy::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=genealogy::Person_strategy)
def test_genealogy::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=genealogy::Person_strategy)
def test_genealogy::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=genealogy::Person_strategy)
def test_genealogy::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=genealogy::Genealogy_strategy)
@settings(max_examples=50)
def test_genealogy::genealogy_instantiation(instance):
    assert isinstance(instance, genealogy::Genealogy)

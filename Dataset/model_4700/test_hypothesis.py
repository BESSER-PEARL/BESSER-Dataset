import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genealogy_Person,
    genealogy_Genealogy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genealogy_person_is_not_abstract():
    assert not inspect.isabstract(genealogy_Person)


def test_genealogy_person_constructor_exists():
    assert callable(genealogy_Person.__init__)


def test_genealogy_person_constructor_args():
    sig = inspect.signature(genealogy_Person.__init__)
    params = list(sig.parameters.keys())
    assert "alive" in params, "Missing parameter 'alive'"
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_genealogy_person_has_alive():
    assert hasattr(genealogy_Person, "alive")
    descriptor = None
    for klass in genealogy_Person.__mro__:
        if "alive" in klass.__dict__:
            descriptor = klass.__dict__["alive"]
            break
    assert isinstance(descriptor, property)

def test_genealogy_person_has_name():
    assert hasattr(genealogy_Person, "name")
    descriptor = None
    for klass in genealogy_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_genealogy_person_has_age():
    assert hasattr(genealogy_Person, "age")
    descriptor = None
    for klass in genealogy_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_genealogy_genealogy_is_not_abstract():
    assert not inspect.isabstract(genealogy_Genealogy)


def test_genealogy_genealogy_constructor_exists():
    assert callable(genealogy_Genealogy.__init__)


def test_genealogy_genealogy_constructor_args():
    sig = inspect.signature(genealogy_Genealogy.__init__)
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
genealogy_Person_strategy = st.builds(
    genealogy_Person,
    alive=
        st.booleans(),
    name=
        safe_text,
    age=
        st.integers()
)
genealogy_Genealogy_strategy = st.builds(
    genealogy_Genealogy,
)

@given(instance=genealogy_Person_strategy)
@settings(max_examples=50)
def test_genealogy_person_instantiation(instance):
    assert isinstance(instance, genealogy_Person)



@given(instance=genealogy_Person_strategy)
def test_genealogy_person_alive_setter(instance):
    original = instance.alive
    instance.alive = original
    assert instance.alive == original



@given(instance=genealogy_Person_strategy)
def test_genealogy_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=genealogy_Person_strategy)
def test_genealogy_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=genealogy_Genealogy_strategy)
@settings(max_examples=50)
def test_genealogy_genealogy_instantiation(instance):
    assert isinstance(instance, genealogy_Genealogy)

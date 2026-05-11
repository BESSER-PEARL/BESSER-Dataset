import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Persons::Person,
    Persons::PersonContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(Persons::Person)


def test_persons::person_constructor_exists():
    assert callable(Persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(Persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"

def test_persons::person_has_ID():
    assert hasattr(Persons::Person, "ID")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_persons::person_has_name():
    assert hasattr(Persons::Person, "name")
    descriptor = None
    for klass in Persons::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_persons::personcontainer_is_not_abstract():
    assert not inspect.isabstract(Persons::PersonContainer)


def test_persons::personcontainer_constructor_exists():
    assert callable(Persons::PersonContainer.__init__)


def test_persons::personcontainer_constructor_args():
    sig = inspect.signature(Persons::PersonContainer.__init__)
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
Persons::Person_strategy = st.builds(
    Persons::Person,
    ID=
        st.integers(),
    name=
        safe_text
)
Persons::PersonContainer_strategy = st.builds(
    Persons::PersonContainer,
)

@given(instance=Persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, Persons::Person)

@given(instance=Persons::Person_strategy)
def test_persons::person_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=Persons::Person_strategy)
def test_persons::person_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Persons::Person_strategy)
def test_persons::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Persons::Person_strategy)
def test_persons::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Persons::PersonContainer_strategy)
@settings(max_examples=50)
def test_persons::personcontainer_instantiation(instance):
    assert isinstance(instance, Persons::PersonContainer)

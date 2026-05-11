import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    personDsl::Person,
    personDsl::PersonContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persondsl::person_is_not_abstract():
    assert not inspect.isabstract(personDsl::Person)


def test_persondsl::person_constructor_exists():
    assert callable(personDsl::Person.__init__)


def test_persondsl::person_constructor_args():
    sig = inspect.signature(personDsl::Person.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"

def test_persondsl::person_has_ID():
    assert hasattr(personDsl::Person, "ID")
    descriptor = None
    for klass in personDsl::Person.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_persondsl::person_has_name():
    assert hasattr(personDsl::Person, "name")
    descriptor = None
    for klass in personDsl::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_persondsl::personcontainer_is_not_abstract():
    assert not inspect.isabstract(personDsl::PersonContainer)


def test_persondsl::personcontainer_constructor_exists():
    assert callable(personDsl::PersonContainer.__init__)


def test_persondsl::personcontainer_constructor_args():
    sig = inspect.signature(personDsl::PersonContainer.__init__)
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
personDsl::Person_strategy = st.builds(
    personDsl::Person,
    ID=
        st.integers(),
    name=
        safe_text
)
personDsl::PersonContainer_strategy = st.builds(
    personDsl::PersonContainer,
)

@given(instance=personDsl::Person_strategy)
@settings(max_examples=50)
def test_persondsl::person_instantiation(instance):
    assert isinstance(instance, personDsl::Person)

@given(instance=personDsl::Person_strategy)
def test_persondsl::person_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=personDsl::Person_strategy)
def test_persondsl::person_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=personDsl::Person_strategy)
def test_persondsl::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=personDsl::Person_strategy)
def test_persondsl::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=personDsl::PersonContainer_strategy)
@settings(max_examples=50)
def test_persondsl::personcontainer_instantiation(instance):
    assert isinstance(instance, personDsl::PersonContainer)

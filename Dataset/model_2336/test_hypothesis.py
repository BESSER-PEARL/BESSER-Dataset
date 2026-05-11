import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PersonsRegister::Person,
    PersonsRegister::PersonsRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personsregister::person_is_not_abstract():
    assert not inspect.isabstract(PersonsRegister::Person)


def test_personsregister::person_constructor_exists():
    assert callable(PersonsRegister::Person.__init__)


def test_personsregister::person_constructor_args():
    sig = inspect.signature(PersonsRegister::Person.__init__)
    params = list(sig.parameters.keys())
    assert "identity" in params, "Missing parameter 'identity'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_personsregister::person_has_identity():
    assert hasattr(PersonsRegister::Person, "identity")
    descriptor = None
    for klass in PersonsRegister::Person.__mro__:
        if "identity" in klass.__dict__:
            descriptor = klass.__dict__["identity"]
            break
    assert isinstance(descriptor, property)

def test_personsregister::person_has_lastName():
    assert hasattr(PersonsRegister::Person, "lastName")
    descriptor = None
    for klass in PersonsRegister::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_personsregister::person_has_firstName():
    assert hasattr(PersonsRegister::Person, "firstName")
    descriptor = None
    for klass in PersonsRegister::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_personsregister::personsregister_is_not_abstract():
    assert not inspect.isabstract(PersonsRegister::PersonsRegister)


def test_personsregister::personsregister_constructor_exists():
    assert callable(PersonsRegister::PersonsRegister.__init__)


def test_personsregister::personsregister_constructor_args():
    sig = inspect.signature(PersonsRegister::PersonsRegister.__init__)
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
PersonsRegister::Person_strategy = st.builds(
    PersonsRegister::Person,
    identity=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text
)
PersonsRegister::PersonsRegister_strategy = st.builds(
    PersonsRegister::PersonsRegister,
)

@given(instance=PersonsRegister::Person_strategy)
@settings(max_examples=50)
def test_personsregister::person_instantiation(instance):
    assert isinstance(instance, PersonsRegister::Person)

@given(instance=PersonsRegister::Person_strategy)
def test_personsregister::person_identity_type(instance):
    assert isinstance(instance.identity, str)


@given(instance=PersonsRegister::Person_strategy)
def test_personsregister::person_identity_setter(instance):
    original = instance.identity
    instance.identity = original
    assert instance.identity == original

@given(instance=PersonsRegister::Person_strategy)
def test_personsregister::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=PersonsRegister::Person_strategy)
def test_personsregister::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=PersonsRegister::Person_strategy)
def test_personsregister::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=PersonsRegister::Person_strategy)
def test_personsregister::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=PersonsRegister::PersonsRegister_strategy)
@settings(max_examples=50)
def test_personsregister::personsregister_instantiation(instance):
    assert isinstance(instance, PersonsRegister::PersonsRegister)

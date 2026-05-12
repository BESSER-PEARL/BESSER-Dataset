import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PersonsRegister_Person,
    PersonsRegister_PersonsRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_personsregister_person_is_not_abstract():
    assert not inspect.isabstract(PersonsRegister_Person)


def test_personsregister_person_constructor_exists():
    assert callable(PersonsRegister_Person.__init__)


def test_personsregister_person_constructor_args():
    sig = inspect.signature(PersonsRegister_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "identity" in params, "Missing parameter 'identity'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_personsregister_person_has_firstName():
    assert hasattr(PersonsRegister_Person, "firstName")
    descriptor = None
    for klass in PersonsRegister_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_personsregister_person_has_identity():
    assert hasattr(PersonsRegister_Person, "identity")
    descriptor = None
    for klass in PersonsRegister_Person.__mro__:
        if "identity" in klass.__dict__:
            descriptor = klass.__dict__["identity"]
            break
    assert isinstance(descriptor, property)

def test_personsregister_person_has_lastName():
    assert hasattr(PersonsRegister_Person, "lastName")
    descriptor = None
    for klass in PersonsRegister_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_personsregister_personsregister_is_not_abstract():
    assert not inspect.isabstract(PersonsRegister_PersonsRegister)


def test_personsregister_personsregister_constructor_exists():
    assert callable(PersonsRegister_PersonsRegister.__init__)


def test_personsregister_personsregister_constructor_args():
    sig = inspect.signature(PersonsRegister_PersonsRegister.__init__)
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
PersonsRegister_Person_strategy = st.builds(
    PersonsRegister_Person,
    firstName=
        safe_text,
    identity=
        safe_text,
    lastName=
        safe_text
)
PersonsRegister_PersonsRegister_strategy = st.builds(
    PersonsRegister_PersonsRegister,
)

@given(instance=PersonsRegister_Person_strategy)
@settings(max_examples=50)
def test_personsregister_person_instantiation(instance):
    assert isinstance(instance, PersonsRegister_Person)



@given(instance=PersonsRegister_Person_strategy)
def test_personsregister_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=PersonsRegister_Person_strategy)
def test_personsregister_person_identity_setter(instance):
    original = instance.identity
    instance.identity = original
    assert instance.identity == original



@given(instance=PersonsRegister_Person_strategy)
def test_personsregister_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=PersonsRegister_PersonsRegister_strategy)
@settings(max_examples=50)
def test_personsregister_personsregister_instantiation(instance):
    assert isinstance(instance, PersonsRegister_PersonsRegister)

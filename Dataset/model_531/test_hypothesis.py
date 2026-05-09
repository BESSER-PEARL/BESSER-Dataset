import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::Family,
    Parent,
    family::Father,
    family::Mother,
    Person,
    family::Child,
    family::Parent,
    family::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())



def test_parent_is_not_abstract():
    assert not inspect.isabstract(Parent)


def test_parent_constructor_exists():
    assert callable(Parent.__init__)


def test_parent_constructor_args():
    sig = inspect.signature(Parent.__init__)
    params = list(sig.parameters.keys())



def test_family::father_is_not_abstract():
    assert not inspect.isabstract(family::Father)


def test_family::father_constructor_exists():
    assert callable(family::Father.__init__)


def test_family::father_constructor_args():
    sig = inspect.signature(family::Father.__init__)
    params = list(sig.parameters.keys())



def test_family::mother_is_not_abstract():
    assert not inspect.isabstract(family::Mother)


def test_family::mother_constructor_exists():
    assert callable(family::Mother.__init__)


def test_family::mother_constructor_args():
    sig = inspect.signature(family::Mother.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_family::child_is_not_abstract():
    assert not inspect.isabstract(family::Child)


def test_family::child_constructor_exists():
    assert callable(family::Child.__init__)


def test_family::child_constructor_args():
    sig = inspect.signature(family::Child.__init__)
    params = list(sig.parameters.keys())



def test_family::parent_is_not_abstract():
    assert not inspect.isabstract(family::Parent)


def test_family::parent_constructor_exists():
    assert callable(family::Parent.__init__)


def test_family::parent_constructor_args():
    sig = inspect.signature(family::Parent.__init__)
    params = list(sig.parameters.keys())



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_family::person_has_birthdate():
    assert hasattr(family::Person, "birthdate")
    descriptor = None
    for klass in family::Person.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_firstname():
    assert hasattr(family::Person, "firstname")
    descriptor = None
    for klass in family::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_lastname():
    assert hasattr(family::Person, "lastname")
    descriptor = None
    for klass in family::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
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
family::Family_strategy = st.builds(
    family::Family,
)
Parent_strategy = st.builds(
    Parent,
)
family::Father_strategy = st.builds(
    family::Father,
)
family::Mother_strategy = st.builds(
    family::Mother,
)
Person_strategy = st.builds(
    Person,
)
family::Child_strategy = st.builds(
    family::Child,
)
family::Parent_strategy = st.builds(
    family::Parent,
)
family::Person_strategy = st.builds(
    family::Person,
    birthdate=
        st.dates(),
    firstname=
        safe_text,
    lastname=
        safe_text
)

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=Parent_strategy)
@settings(max_examples=50)
def test_parent_instantiation(instance):
    assert isinstance(instance, Parent)

@given(instance=family::Father_strategy)
@settings(max_examples=50)
def test_family::father_instantiation(instance):
    assert isinstance(instance, family::Father)

@given(instance=family::Mother_strategy)
@settings(max_examples=50)
def test_family::mother_instantiation(instance):
    assert isinstance(instance, family::Mother)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family::Child_strategy)
@settings(max_examples=50)
def test_family::child_instantiation(instance):
    assert isinstance(instance, family::Child)

@given(instance=family::Parent_strategy)
@settings(max_examples=50)
def test_family::parent_instantiation(instance):
    assert isinstance(instance, family::Parent)

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_birthdate_type(instance):
    assert isinstance(instance.birthdate, date)


@given(instance=family::Person_strategy)
def test_family::person_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original

@given(instance=family::Person_strategy)
def test_family::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=family::Person_strategy)
def test_family::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=family::Person_strategy)
def test_family::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=family::Person_strategy)
def test_family::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

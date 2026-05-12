import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_Family,
    Parent,
    family_Father,
    family_Mother,
    Person,
    family_Child,
    family_Parent,
    family_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())



def test_parent_is_not_abstract():
    assert not inspect.isabstract(Parent)


def test_parent_constructor_exists():
    assert callable(Parent.__init__)


def test_parent_constructor_args():
    sig = inspect.signature(Parent.__init__)
    params = list(sig.parameters.keys())



def test_family_father_is_not_abstract():
    assert not inspect.isabstract(family_Father)


def test_family_father_constructor_exists():
    assert callable(family_Father.__init__)


def test_family_father_constructor_args():
    sig = inspect.signature(family_Father.__init__)
    params = list(sig.parameters.keys())



def test_family_mother_is_not_abstract():
    assert not inspect.isabstract(family_Mother)


def test_family_mother_constructor_exists():
    assert callable(family_Mother.__init__)


def test_family_mother_constructor_args():
    sig = inspect.signature(family_Mother.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_family_child_is_not_abstract():
    assert not inspect.isabstract(family_Child)


def test_family_child_constructor_exists():
    assert callable(family_Child.__init__)


def test_family_child_constructor_args():
    sig = inspect.signature(family_Child.__init__)
    params = list(sig.parameters.keys())



def test_family_parent_is_not_abstract():
    assert not inspect.isabstract(family_Parent)


def test_family_parent_constructor_exists():
    assert callable(family_Parent.__init__)


def test_family_parent_constructor_args():
    sig = inspect.signature(family_Parent.__init__)
    params = list(sig.parameters.keys())



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_family_person_has_birthdate():
    assert hasattr(family_Person, "birthdate")
    descriptor = None
    for klass in family_Person.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_lastname():
    assert hasattr(family_Person, "lastname")
    descriptor = None
    for klass in family_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_firstname():
    assert hasattr(family_Person, "firstname")
    descriptor = None
    for klass in family_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
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
family_Family_strategy = st.builds(
    family_Family,
)
Parent_strategy = st.builds(
    Parent,
)
family_Father_strategy = st.builds(
    family_Father,
)
family_Mother_strategy = st.builds(
    family_Mother,
)
Person_strategy = st.builds(
    Person,
)
family_Child_strategy = st.builds(
    family_Child,
)
family_Parent_strategy = st.builds(
    family_Parent,
)
family_Person_strategy = st.builds(
    family_Person,
    birthdate=
        st.dates(),
    lastname=
        safe_text,
    firstname=
        safe_text
)

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)

@given(instance=Parent_strategy)
@settings(max_examples=50)
def test_parent_instantiation(instance):
    assert isinstance(instance, Parent)

@given(instance=family_Father_strategy)
@settings(max_examples=50)
def test_family_father_instantiation(instance):
    assert isinstance(instance, family_Father)

@given(instance=family_Mother_strategy)
@settings(max_examples=50)
def test_family_mother_instantiation(instance):
    assert isinstance(instance, family_Mother)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family_Child_strategy)
@settings(max_examples=50)
def test_family_child_instantiation(instance):
    assert isinstance(instance, family_Child)

@given(instance=family_Parent_strategy)
@settings(max_examples=50)
def test_family_parent_instantiation(instance):
    assert isinstance(instance, family_Parent)

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original



@given(instance=family_Person_strategy)
def test_family_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=family_Person_strategy)
def test_family_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

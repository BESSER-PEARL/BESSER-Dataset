import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::NamedElement,
    NamedElement,
    family::Family,
    family::Person,
    family::Members,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::namedelement_is_not_abstract():
    assert not inspect.isabstract(family::NamedElement)


def test_family::namedelement_constructor_exists():
    assert callable(family::NamedElement.__init__)


def test_family::namedelement_constructor_args():
    sig = inspect.signature(family::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::namedelement_has_name():
    assert hasattr(family::NamedElement, "name")
    descriptor = None
    for klass in family::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfComponents" in params, "Missing parameter 'numberOfComponents'"
    assert "familyIncome" in params, "Missing parameter 'familyIncome'"

def test_family::family_has_numberOfComponents():
    assert hasattr(family::Family, "numberOfComponents")
    descriptor = None
    for klass in family::Family.__mro__:
        if "numberOfComponents" in klass.__dict__:
            descriptor = klass.__dict__["numberOfComponents"]
            break
    assert isinstance(descriptor, property)

def test_family::family_has_familyIncome():
    assert hasattr(family::Family, "familyIncome")
    descriptor = None
    for klass in family::Family.__mro__:
        if "familyIncome" in klass.__dict__:
            descriptor = klass.__dict__["familyIncome"]
            break
    assert isinstance(descriptor, property)



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_family::person_has_age():
    assert hasattr(family::Person, "age")
    descriptor = None
    for klass in family::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_gender():
    assert hasattr(family::Person, "gender")
    descriptor = None
    for klass in family::Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_surname():
    assert hasattr(family::Person, "surname")
    descriptor = None
    for klass in family::Person.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_family::members_is_not_abstract():
    assert not inspect.isabstract(family::Members)


def test_family::members_constructor_exists():
    assert callable(family::Members.__init__)


def test_family::members_constructor_args():
    sig = inspect.signature(family::Members.__init__)
    params = list(sig.parameters.keys())
    assert "hasChild" in params, "Missing parameter 'hasChild'"

def test_family::members_has_hasChild():
    assert hasattr(family::Members, "hasChild")
    descriptor = None
    for klass in family::Members.__mro__:
        if "hasChild" in klass.__dict__:
            descriptor = klass.__dict__["hasChild"]
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
family::NamedElement_strategy = st.builds(
    family::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
family::Family_strategy = st.builds(
    family::Family,
    numberOfComponents=
        st.integers(),
    familyIncome=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
family::Person_strategy = st.builds(
    family::Person,
    age=
        st.integers(),
    gender=
        safe_text,
    surname=
        safe_text
)
family::Members_strategy = st.builds(
    family::Members,
    hasChild=
        st.booleans()
)

@given(instance=family::NamedElement_strategy)
@settings(max_examples=50)
def test_family::namedelement_instantiation(instance):
    assert isinstance(instance, family::NamedElement)

@given(instance=family::NamedElement_strategy)
def test_family::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::NamedElement_strategy)
def test_family::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_numberOfComponents_type(instance):
    assert isinstance(instance.numberOfComponents, int)


@given(instance=family::Family_strategy)
def test_family::family_numberOfComponents_setter(instance):
    original = instance.numberOfComponents
    instance.numberOfComponents = original
    assert instance.numberOfComponents == original

@given(instance=family::Family_strategy)
def test_family::family_familyIncome_type(instance):
    assert isinstance(instance.familyIncome, float)


@given(instance=family::Family_strategy)
def test_family::family_familyIncome_setter(instance):
    original = instance.familyIncome
    instance.familyIncome = original
    assert instance.familyIncome == original

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=family::Person_strategy)
def test_family::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family::Person_strategy)
def test_family::person_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=family::Person_strategy)
def test_family::person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original

@given(instance=family::Person_strategy)
def test_family::person_surname_type(instance):
    assert isinstance(instance.surname, str)


@given(instance=family::Person_strategy)
def test_family::person_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=family::Members_strategy)
@settings(max_examples=50)
def test_family::members_instantiation(instance):
    assert isinstance(instance, family::Members)

@given(instance=family::Members_strategy)
def test_family::members_hasChild_type(instance):
    assert isinstance(instance.hasChild, bool)


@given(instance=family::Members_strategy)
def test_family::members_hasChild_setter(instance):
    original = instance.hasChild
    instance.hasChild = original
    assert instance.hasChild == original

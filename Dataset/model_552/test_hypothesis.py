import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_NamedElement,
    NamedElement,
    family_Person,
    family_Family,
    family_Members,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_namedelement_is_not_abstract():
    assert not inspect.isabstract(family_NamedElement)


def test_family_namedelement_constructor_exists():
    assert callable(family_NamedElement.__init__)


def test_family_namedelement_constructor_args():
    sig = inspect.signature(family_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_namedelement_has_name():
    assert hasattr(family_NamedElement, "name")
    descriptor = None
    for klass in family_NamedElement.__mro__:
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



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "age" in params, "Missing parameter 'age'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_family_person_has_gender():
    assert hasattr(family_Person, "gender")
    descriptor = None
    for klass in family_Person.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_age():
    assert hasattr(family_Person, "age")
    descriptor = None
    for klass in family_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_surname():
    assert hasattr(family_Person, "surname")
    descriptor = None
    for klass in family_Person.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "familyIncome" in params, "Missing parameter 'familyIncome'"
    assert "numberOfComponents" in params, "Missing parameter 'numberOfComponents'"

def test_family_family_has_familyIncome():
    assert hasattr(family_Family, "familyIncome")
    descriptor = None
    for klass in family_Family.__mro__:
        if "familyIncome" in klass.__dict__:
            descriptor = klass.__dict__["familyIncome"]
            break
    assert isinstance(descriptor, property)

def test_family_family_has_numberOfComponents():
    assert hasattr(family_Family, "numberOfComponents")
    descriptor = None
    for klass in family_Family.__mro__:
        if "numberOfComponents" in klass.__dict__:
            descriptor = klass.__dict__["numberOfComponents"]
            break
    assert isinstance(descriptor, property)



def test_family_members_is_not_abstract():
    assert not inspect.isabstract(family_Members)


def test_family_members_constructor_exists():
    assert callable(family_Members.__init__)


def test_family_members_constructor_args():
    sig = inspect.signature(family_Members.__init__)
    params = list(sig.parameters.keys())
    assert "hasChild" in params, "Missing parameter 'hasChild'"

def test_family_members_has_hasChild():
    assert hasattr(family_Members, "hasChild")
    descriptor = None
    for klass in family_Members.__mro__:
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
family_NamedElement_strategy = st.builds(
    family_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
family_Person_strategy = st.builds(
    family_Person,
    gender=
        safe_text,
    age=
        st.integers(),
    surname=
        safe_text
)
family_Family_strategy = st.builds(
    family_Family,
    familyIncome=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    numberOfComponents=
        st.integers()
)
family_Members_strategy = st.builds(
    family_Members,
    hasChild=
        st.booleans()
)

@given(instance=family_NamedElement_strategy)
@settings(max_examples=50)
def test_family_namedelement_instantiation(instance):
    assert isinstance(instance, family_NamedElement)



@given(instance=family_NamedElement_strategy)
def test_family_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=family_Person_strategy)
def test_family_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=family_Person_strategy)
def test_family_person_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)



@given(instance=family_Family_strategy)
def test_family_family_familyIncome_setter(instance):
    original = instance.familyIncome
    instance.familyIncome = original
    assert instance.familyIncome == original



@given(instance=family_Family_strategy)
def test_family_family_numberOfComponents_setter(instance):
    original = instance.numberOfComponents
    instance.numberOfComponents = original
    assert instance.numberOfComponents == original

@given(instance=family_Members_strategy)
@settings(max_examples=50)
def test_family_members_instantiation(instance):
    assert isinstance(instance, family_Members)



@given(instance=family_Members_strategy)
def test_family_members_hasChild_setter(instance):
    original = instance.hasChild
    instance.hasChild = original
    assert instance.hasChild == original

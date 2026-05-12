import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    familyleft1_Son,
    familyleft1_Mother,
    familyleft1_Family,
    familyleft1_Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familyleft1_son_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Son)


def test_familyleft1_son_constructor_exists():
    assert callable(familyleft1_Son.__init__)


def test_familyleft1_son_constructor_args():
    sig = inspect.signature(familyleft1_Son.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_familyleft1_son_has_age():
    assert hasattr(familyleft1_Son, "age")
    descriptor = None
    for klass in familyleft1_Son.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1_son_has_name():
    assert hasattr(familyleft1_Son, "name")
    descriptor = None
    for klass in familyleft1_Son.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1_son_has_sex():
    assert hasattr(familyleft1_Son, "sex")
    descriptor = None
    for klass in familyleft1_Son.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_familyleft1_mother_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Mother)


def test_familyleft1_mother_constructor_exists():
    assert callable(familyleft1_Mother.__init__)


def test_familyleft1_mother_constructor_args():
    sig = inspect.signature(familyleft1_Mother.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_familyleft1_mother_has_name():
    assert hasattr(familyleft1_Mother, "name")
    descriptor = None
    for klass in familyleft1_Mother.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1_mother_has_age():
    assert hasattr(familyleft1_Mother, "age")
    descriptor = None
    for klass in familyleft1_Mother.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_familyleft1_family_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Family)


def test_familyleft1_family_constructor_exists():
    assert callable(familyleft1_Family.__init__)


def test_familyleft1_family_constructor_args():
    sig = inspect.signature(familyleft1_Family.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_familyleft1_family_has_location():
    assert hasattr(familyleft1_Family, "location")
    descriptor = None
    for klass in familyleft1_Family.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1_family_has_surname():
    assert hasattr(familyleft1_Family, "surname")
    descriptor = None
    for klass in familyleft1_Family.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_familyleft1_father_is_not_abstract():
    assert not inspect.isabstract(familyleft1_Father)


def test_familyleft1_father_constructor_exists():
    assert callable(familyleft1_Father.__init__)


def test_familyleft1_father_constructor_args():
    sig = inspect.signature(familyleft1_Father.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyleft1_father_has_age():
    assert hasattr(familyleft1_Father, "age")
    descriptor = None
    for klass in familyleft1_Father.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1_father_has_name():
    assert hasattr(familyleft1_Father, "name")
    descriptor = None
    for klass in familyleft1_Father.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
familyleft1_Son_strategy = st.builds(
    familyleft1_Son,
    age=
        st.integers(),
    name=
        safe_text,
    sex=
        safe_text
)
familyleft1_Mother_strategy = st.builds(
    familyleft1_Mother,
    name=
        safe_text,
    age=
        st.integers()
)
familyleft1_Family_strategy = st.builds(
    familyleft1_Family,
    location=
        safe_text,
    surname=
        safe_text
)
familyleft1_Father_strategy = st.builds(
    familyleft1_Father,
    age=
        st.integers(),
    name=
        safe_text
)

@given(instance=familyleft1_Son_strategy)
@settings(max_examples=50)
def test_familyleft1_son_instantiation(instance):
    assert isinstance(instance, familyleft1_Son)



@given(instance=familyleft1_Son_strategy)
def test_familyleft1_son_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=familyleft1_Son_strategy)
def test_familyleft1_son_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=familyleft1_Son_strategy)
def test_familyleft1_son_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=familyleft1_Mother_strategy)
@settings(max_examples=50)
def test_familyleft1_mother_instantiation(instance):
    assert isinstance(instance, familyleft1_Mother)



@given(instance=familyleft1_Mother_strategy)
def test_familyleft1_mother_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=familyleft1_Mother_strategy)
def test_familyleft1_mother_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyleft1_Family_strategy)
@settings(max_examples=50)
def test_familyleft1_family_instantiation(instance):
    assert isinstance(instance, familyleft1_Family)



@given(instance=familyleft1_Family_strategy)
def test_familyleft1_family_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=familyleft1_Family_strategy)
def test_familyleft1_family_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=familyleft1_Father_strategy)
@settings(max_examples=50)
def test_familyleft1_father_instantiation(instance):
    assert isinstance(instance, familyleft1_Father)



@given(instance=familyleft1_Father_strategy)
def test_familyleft1_father_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=familyleft1_Father_strategy)
def test_familyleft1_father_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

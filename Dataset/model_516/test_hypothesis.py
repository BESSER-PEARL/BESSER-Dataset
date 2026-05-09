import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    familyleft1::Son,
    familyleft1::Mother,
    familyleft1::Family,
    familyleft1::Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familyleft1::son_is_not_abstract():
    assert not inspect.isabstract(familyleft1::Son)


def test_familyleft1::son_constructor_exists():
    assert callable(familyleft1::Son.__init__)


def test_familyleft1::son_constructor_args():
    sig = inspect.signature(familyleft1::Son.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_familyleft1::son_has_name():
    assert hasattr(familyleft1::Son, "name")
    descriptor = None
    for klass in familyleft1::Son.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1::son_has_age():
    assert hasattr(familyleft1::Son, "age")
    descriptor = None
    for klass in familyleft1::Son.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1::son_has_sex():
    assert hasattr(familyleft1::Son, "sex")
    descriptor = None
    for klass in familyleft1::Son.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_familyleft1::mother_is_not_abstract():
    assert not inspect.isabstract(familyleft1::Mother)


def test_familyleft1::mother_constructor_exists():
    assert callable(familyleft1::Mother.__init__)


def test_familyleft1::mother_constructor_args():
    sig = inspect.signature(familyleft1::Mother.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyleft1::mother_has_age():
    assert hasattr(familyleft1::Mother, "age")
    descriptor = None
    for klass in familyleft1::Mother.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1::mother_has_name():
    assert hasattr(familyleft1::Mother, "name")
    descriptor = None
    for klass in familyleft1::Mother.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familyleft1::family_is_not_abstract():
    assert not inspect.isabstract(familyleft1::Family)


def test_familyleft1::family_constructor_exists():
    assert callable(familyleft1::Family.__init__)


def test_familyleft1::family_constructor_args():
    sig = inspect.signature(familyleft1::Family.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "surname" in params, "Missing parameter 'surname'"

def test_familyleft1::family_has_location():
    assert hasattr(familyleft1::Family, "location")
    descriptor = None
    for klass in familyleft1::Family.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1::family_has_surname():
    assert hasattr(familyleft1::Family, "surname")
    descriptor = None
    for klass in familyleft1::Family.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)



def test_familyleft1::father_is_not_abstract():
    assert not inspect.isabstract(familyleft1::Father)


def test_familyleft1::father_constructor_exists():
    assert callable(familyleft1::Father.__init__)


def test_familyleft1::father_constructor_args():
    sig = inspect.signature(familyleft1::Father.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyleft1::father_has_age():
    assert hasattr(familyleft1::Father, "age")
    descriptor = None
    for klass in familyleft1::Father.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyleft1::father_has_name():
    assert hasattr(familyleft1::Father, "name")
    descriptor = None
    for klass in familyleft1::Father.__mro__:
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
familyleft1::Son_strategy = st.builds(
    familyleft1::Son,
    name=
        safe_text,
    age=
        st.integers(),
    sex=
        safe_text
)
familyleft1::Mother_strategy = st.builds(
    familyleft1::Mother,
    age=
        st.integers(),
    name=
        safe_text
)
familyleft1::Family_strategy = st.builds(
    familyleft1::Family,
    location=
        safe_text,
    surname=
        safe_text
)
familyleft1::Father_strategy = st.builds(
    familyleft1::Father,
    age=
        st.integers(),
    name=
        safe_text
)

@given(instance=familyleft1::Son_strategy)
@settings(max_examples=50)
def test_familyleft1::son_instantiation(instance):
    assert isinstance(instance, familyleft1::Son)

@given(instance=familyleft1::Son_strategy)
def test_familyleft1::son_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyleft1::Son_strategy)
def test_familyleft1::son_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyleft1::Son_strategy)
def test_familyleft1::son_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyleft1::Son_strategy)
def test_familyleft1::son_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyleft1::Son_strategy)
def test_familyleft1::son_sex_type(instance):
    assert isinstance(instance.sex, str)


@given(instance=familyleft1::Son_strategy)
def test_familyleft1::son_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=familyleft1::Mother_strategy)
@settings(max_examples=50)
def test_familyleft1::mother_instantiation(instance):
    assert isinstance(instance, familyleft1::Mother)

@given(instance=familyleft1::Mother_strategy)
def test_familyleft1::mother_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyleft1::Mother_strategy)
def test_familyleft1::mother_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyleft1::Mother_strategy)
def test_familyleft1::mother_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyleft1::Mother_strategy)
def test_familyleft1::mother_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyleft1::Family_strategy)
@settings(max_examples=50)
def test_familyleft1::family_instantiation(instance):
    assert isinstance(instance, familyleft1::Family)

@given(instance=familyleft1::Family_strategy)
def test_familyleft1::family_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=familyleft1::Family_strategy)
def test_familyleft1::family_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=familyleft1::Family_strategy)
def test_familyleft1::family_surname_type(instance):
    assert isinstance(instance.surname, str)


@given(instance=familyleft1::Family_strategy)
def test_familyleft1::family_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original

@given(instance=familyleft1::Father_strategy)
@settings(max_examples=50)
def test_familyleft1::father_instantiation(instance):
    assert isinstance(instance, familyleft1::Father)

@given(instance=familyleft1::Father_strategy)
def test_familyleft1::father_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyleft1::Father_strategy)
def test_familyleft1::father_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyleft1::Father_strategy)
def test_familyleft1::father_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyleft1::Father_strategy)
def test_familyleft1::father_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

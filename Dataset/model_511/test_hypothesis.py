import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    familyright::Mother,
    familyright::Family,
    familyright::Father,
    familyright::Daughter,
    familyright::Son,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familyright::mother_is_not_abstract():
    assert not inspect.isabstract(familyright::Mother)


def test_familyright::mother_constructor_exists():
    assert callable(familyright::Mother.__init__)


def test_familyright::mother_constructor_args():
    sig = inspect.signature(familyright::Mother.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyright::mother_has_age():
    assert hasattr(familyright::Mother, "age")
    descriptor = None
    for klass in familyright::Mother.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyright::mother_has_address():
    assert hasattr(familyright::Mother, "address")
    descriptor = None
    for klass in familyright::Mother.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_familyright::mother_has_name():
    assert hasattr(familyright::Mother, "name")
    descriptor = None
    for klass in familyright::Mother.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familyright::family_is_not_abstract():
    assert not inspect.isabstract(familyright::Family)


def test_familyright::family_constructor_exists():
    assert callable(familyright::Family.__init__)


def test_familyright::family_constructor_args():
    sig = inspect.signature(familyright::Family.__init__)
    params = list(sig.parameters.keys())



def test_familyright::father_is_not_abstract():
    assert not inspect.isabstract(familyright::Father)


def test_familyright::father_constructor_exists():
    assert callable(familyright::Father.__init__)


def test_familyright::father_constructor_args():
    sig = inspect.signature(familyright::Father.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "address" in params, "Missing parameter 'address'"

def test_familyright::father_has_name():
    assert hasattr(familyright::Father, "name")
    descriptor = None
    for klass in familyright::Father.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyright::father_has_age():
    assert hasattr(familyright::Father, "age")
    descriptor = None
    for klass in familyright::Father.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyright::father_has_address():
    assert hasattr(familyright::Father, "address")
    descriptor = None
    for klass in familyright::Father.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_familyright::daughter_is_not_abstract():
    assert not inspect.isabstract(familyright::Daughter)


def test_familyright::daughter_constructor_exists():
    assert callable(familyright::Daughter.__init__)


def test_familyright::daughter_constructor_args():
    sig = inspect.signature(familyright::Daughter.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyright::daughter_has_age():
    assert hasattr(familyright::Daughter, "age")
    descriptor = None
    for klass in familyright::Daughter.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyright::daughter_has_name():
    assert hasattr(familyright::Daughter, "name")
    descriptor = None
    for klass in familyright::Daughter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familyright::son_is_not_abstract():
    assert not inspect.isabstract(familyright::Son)


def test_familyright::son_constructor_exists():
    assert callable(familyright::Son.__init__)


def test_familyright::son_constructor_args():
    sig = inspect.signature(familyright::Son.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyright::son_has_age():
    assert hasattr(familyright::Son, "age")
    descriptor = None
    for klass in familyright::Son.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyright::son_has_name():
    assert hasattr(familyright::Son, "name")
    descriptor = None
    for klass in familyright::Son.__mro__:
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
familyright::Mother_strategy = st.builds(
    familyright::Mother,
    age=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text
)
familyright::Family_strategy = st.builds(
    familyright::Family,
)
familyright::Father_strategy = st.builds(
    familyright::Father,
    name=
        safe_text,
    age=
        st.integers(),
    address=
        safe_text
)
familyright::Daughter_strategy = st.builds(
    familyright::Daughter,
    age=
        st.integers(),
    name=
        safe_text
)
familyright::Son_strategy = st.builds(
    familyright::Son,
    age=
        st.integers(),
    name=
        safe_text
)

@given(instance=familyright::Mother_strategy)
@settings(max_examples=50)
def test_familyright::mother_instantiation(instance):
    assert isinstance(instance, familyright::Mother)

@given(instance=familyright::Mother_strategy)
def test_familyright::mother_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyright::Mother_strategy)
def test_familyright::mother_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyright::Mother_strategy)
def test_familyright::mother_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=familyright::Mother_strategy)
def test_familyright::mother_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=familyright::Mother_strategy)
def test_familyright::mother_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyright::Mother_strategy)
def test_familyright::mother_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyright::Family_strategy)
@settings(max_examples=50)
def test_familyright::family_instantiation(instance):
    assert isinstance(instance, familyright::Family)

@given(instance=familyright::Father_strategy)
@settings(max_examples=50)
def test_familyright::father_instantiation(instance):
    assert isinstance(instance, familyright::Father)

@given(instance=familyright::Father_strategy)
def test_familyright::father_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyright::Father_strategy)
def test_familyright::father_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyright::Father_strategy)
def test_familyright::father_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyright::Father_strategy)
def test_familyright::father_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyright::Father_strategy)
def test_familyright::father_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=familyright::Father_strategy)
def test_familyright::father_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=familyright::Daughter_strategy)
@settings(max_examples=50)
def test_familyright::daughter_instantiation(instance):
    assert isinstance(instance, familyright::Daughter)

@given(instance=familyright::Daughter_strategy)
def test_familyright::daughter_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyright::Daughter_strategy)
def test_familyright::daughter_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyright::Daughter_strategy)
def test_familyright::daughter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyright::Daughter_strategy)
def test_familyright::daughter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyright::Son_strategy)
@settings(max_examples=50)
def test_familyright::son_instantiation(instance):
    assert isinstance(instance, familyright::Son)

@given(instance=familyright::Son_strategy)
def test_familyright::son_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyright::Son_strategy)
def test_familyright::son_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyright::Son_strategy)
def test_familyright::son_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyright::Son_strategy)
def test_familyright::son_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

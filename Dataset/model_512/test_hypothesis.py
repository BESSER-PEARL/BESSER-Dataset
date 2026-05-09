import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    familyleft2::Person,
    familyleft2::Family,
    Person,
    familyleft2::Son,
    familyleft2::Daughter,
    familyleft2::Mother,
    familyleft2::Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familyleft2::person_is_not_abstract():
    assert not inspect.isabstract(familyleft2::Person)


def test_familyleft2::person_constructor_exists():
    assert callable(familyleft2::Person.__init__)


def test_familyleft2::person_constructor_args():
    sig = inspect.signature(familyleft2::Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isMale" in params, "Missing parameter 'isMale'"

def test_familyleft2::person_has_age():
    assert hasattr(familyleft2::Person, "age")
    descriptor = None
    for klass in familyleft2::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyleft2::person_has_name():
    assert hasattr(familyleft2::Person, "name")
    descriptor = None
    for klass in familyleft2::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyleft2::person_has_isMale():
    assert hasattr(familyleft2::Person, "isMale")
    descriptor = None
    for klass in familyleft2::Person.__mro__:
        if "isMale" in klass.__dict__:
            descriptor = klass.__dict__["isMale"]
            break
    assert isinstance(descriptor, property)



def test_familyleft2::family_is_not_abstract():
    assert not inspect.isabstract(familyleft2::Family)


def test_familyleft2::family_constructor_exists():
    assert callable(familyleft2::Family.__init__)


def test_familyleft2::family_constructor_args():
    sig = inspect.signature(familyleft2::Family.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_familyleft2::son_is_not_abstract():
    assert not inspect.isabstract(familyleft2::Son)


def test_familyleft2::son_constructor_exists():
    assert callable(familyleft2::Son.__init__)


def test_familyleft2::son_constructor_args():
    sig = inspect.signature(familyleft2::Son.__init__)
    params = list(sig.parameters.keys())



def test_familyleft2::daughter_is_not_abstract():
    assert not inspect.isabstract(familyleft2::Daughter)


def test_familyleft2::daughter_constructor_exists():
    assert callable(familyleft2::Daughter.__init__)


def test_familyleft2::daughter_constructor_args():
    sig = inspect.signature(familyleft2::Daughter.__init__)
    params = list(sig.parameters.keys())



def test_familyleft2::mother_is_not_abstract():
    assert not inspect.isabstract(familyleft2::Mother)


def test_familyleft2::mother_constructor_exists():
    assert callable(familyleft2::Mother.__init__)


def test_familyleft2::mother_constructor_args():
    sig = inspect.signature(familyleft2::Mother.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_familyleft2::mother_has_address():
    assert hasattr(familyleft2::Mother, "address")
    descriptor = None
    for klass in familyleft2::Mother.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_familyleft2::father_is_not_abstract():
    assert not inspect.isabstract(familyleft2::Father)


def test_familyleft2::father_constructor_exists():
    assert callable(familyleft2::Father.__init__)


def test_familyleft2::father_constructor_args():
    sig = inspect.signature(familyleft2::Father.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_familyleft2::father_has_address():
    assert hasattr(familyleft2::Father, "address")
    descriptor = None
    for klass in familyleft2::Father.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
familyleft2::Person_strategy = st.builds(
    familyleft2::Person,
    age=
        st.integers(),
    name=
        safe_text,
    isMale=
        st.booleans()
)
familyleft2::Family_strategy = st.builds(
    familyleft2::Family,
)
Person_strategy = st.builds(
    Person,
)
familyleft2::Son_strategy = st.builds(
    familyleft2::Son,
)
familyleft2::Daughter_strategy = st.builds(
    familyleft2::Daughter,
)
familyleft2::Mother_strategy = st.builds(
    familyleft2::Mother,
    address=
        safe_text
)
familyleft2::Father_strategy = st.builds(
    familyleft2::Father,
    address=
        safe_text
)

@given(instance=familyleft2::Person_strategy)
@settings(max_examples=50)
def test_familyleft2::person_instantiation(instance):
    assert isinstance(instance, familyleft2::Person)

@given(instance=familyleft2::Person_strategy)
def test_familyleft2::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=familyleft2::Person_strategy)
def test_familyleft2::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyleft2::Person_strategy)
def test_familyleft2::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=familyleft2::Person_strategy)
def test_familyleft2::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyleft2::Person_strategy)
def test_familyleft2::person_isMale_type(instance):
    assert isinstance(instance.isMale, bool)


@given(instance=familyleft2::Person_strategy)
def test_familyleft2::person_isMale_setter(instance):
    original = instance.isMale
    instance.isMale = original
    assert instance.isMale == original

@given(instance=familyleft2::Family_strategy)
@settings(max_examples=50)
def test_familyleft2::family_instantiation(instance):
    assert isinstance(instance, familyleft2::Family)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familyleft2::Son_strategy)
@settings(max_examples=50)
def test_familyleft2::son_instantiation(instance):
    assert isinstance(instance, familyleft2::Son)

@given(instance=familyleft2::Daughter_strategy)
@settings(max_examples=50)
def test_familyleft2::daughter_instantiation(instance):
    assert isinstance(instance, familyleft2::Daughter)

@given(instance=familyleft2::Mother_strategy)
@settings(max_examples=50)
def test_familyleft2::mother_instantiation(instance):
    assert isinstance(instance, familyleft2::Mother)

@given(instance=familyleft2::Mother_strategy)
def test_familyleft2::mother_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=familyleft2::Mother_strategy)
def test_familyleft2::mother_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=familyleft2::Father_strategy)
@settings(max_examples=50)
def test_familyleft2::father_instantiation(instance):
    assert isinstance(instance, familyleft2::Father)

@given(instance=familyleft2::Father_strategy)
def test_familyleft2::father_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=familyleft2::Father_strategy)
def test_familyleft2::father_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

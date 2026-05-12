import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    familyleft2_Person,
    familyleft2_Family,
    Person,
    familyleft2_Mother,
    familyleft2_Son,
    familyleft2_Daughter,
    familyleft2_Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familyleft2_person_is_not_abstract():
    assert not inspect.isabstract(familyleft2_Person)


def test_familyleft2_person_constructor_exists():
    assert callable(familyleft2_Person.__init__)


def test_familyleft2_person_constructor_args():
    sig = inspect.signature(familyleft2_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMale" in params, "Missing parameter 'isMale'"
    assert "age" in params, "Missing parameter 'age'"

def test_familyleft2_person_has_name():
    assert hasattr(familyleft2_Person, "name")
    descriptor = None
    for klass in familyleft2_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyleft2_person_has_isMale():
    assert hasattr(familyleft2_Person, "isMale")
    descriptor = None
    for klass in familyleft2_Person.__mro__:
        if "isMale" in klass.__dict__:
            descriptor = klass.__dict__["isMale"]
            break
    assert isinstance(descriptor, property)

def test_familyleft2_person_has_age():
    assert hasattr(familyleft2_Person, "age")
    descriptor = None
    for klass in familyleft2_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_familyleft2_family_is_not_abstract():
    assert not inspect.isabstract(familyleft2_Family)


def test_familyleft2_family_constructor_exists():
    assert callable(familyleft2_Family.__init__)


def test_familyleft2_family_constructor_args():
    sig = inspect.signature(familyleft2_Family.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_familyleft2_mother_is_not_abstract():
    assert not inspect.isabstract(familyleft2_Mother)


def test_familyleft2_mother_constructor_exists():
    assert callable(familyleft2_Mother.__init__)


def test_familyleft2_mother_constructor_args():
    sig = inspect.signature(familyleft2_Mother.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_familyleft2_mother_has_address():
    assert hasattr(familyleft2_Mother, "address")
    descriptor = None
    for klass in familyleft2_Mother.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_familyleft2_son_is_not_abstract():
    assert not inspect.isabstract(familyleft2_Son)


def test_familyleft2_son_constructor_exists():
    assert callable(familyleft2_Son.__init__)


def test_familyleft2_son_constructor_args():
    sig = inspect.signature(familyleft2_Son.__init__)
    params = list(sig.parameters.keys())



def test_familyleft2_daughter_is_not_abstract():
    assert not inspect.isabstract(familyleft2_Daughter)


def test_familyleft2_daughter_constructor_exists():
    assert callable(familyleft2_Daughter.__init__)


def test_familyleft2_daughter_constructor_args():
    sig = inspect.signature(familyleft2_Daughter.__init__)
    params = list(sig.parameters.keys())



def test_familyleft2_father_is_not_abstract():
    assert not inspect.isabstract(familyleft2_Father)


def test_familyleft2_father_constructor_exists():
    assert callable(familyleft2_Father.__init__)


def test_familyleft2_father_constructor_args():
    sig = inspect.signature(familyleft2_Father.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_familyleft2_father_has_address():
    assert hasattr(familyleft2_Father, "address")
    descriptor = None
    for klass in familyleft2_Father.__mro__:
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
familyleft2_Person_strategy = st.builds(
    familyleft2_Person,
    name=
        safe_text,
    isMale=
        st.booleans(),
    age=
        st.integers()
)
familyleft2_Family_strategy = st.builds(
    familyleft2_Family,
)
Person_strategy = st.builds(
    Person,
)
familyleft2_Mother_strategy = st.builds(
    familyleft2_Mother,
    address=
        safe_text
)
familyleft2_Son_strategy = st.builds(
    familyleft2_Son,
)
familyleft2_Daughter_strategy = st.builds(
    familyleft2_Daughter,
)
familyleft2_Father_strategy = st.builds(
    familyleft2_Father,
    address=
        safe_text
)

@given(instance=familyleft2_Person_strategy)
@settings(max_examples=50)
def test_familyleft2_person_instantiation(instance):
    assert isinstance(instance, familyleft2_Person)



@given(instance=familyleft2_Person_strategy)
def test_familyleft2_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=familyleft2_Person_strategy)
def test_familyleft2_person_isMale_setter(instance):
    original = instance.isMale
    instance.isMale = original
    assert instance.isMale == original



@given(instance=familyleft2_Person_strategy)
def test_familyleft2_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyleft2_Family_strategy)
@settings(max_examples=50)
def test_familyleft2_family_instantiation(instance):
    assert isinstance(instance, familyleft2_Family)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=familyleft2_Mother_strategy)
@settings(max_examples=50)
def test_familyleft2_mother_instantiation(instance):
    assert isinstance(instance, familyleft2_Mother)



@given(instance=familyleft2_Mother_strategy)
def test_familyleft2_mother_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=familyleft2_Son_strategy)
@settings(max_examples=50)
def test_familyleft2_son_instantiation(instance):
    assert isinstance(instance, familyleft2_Son)

@given(instance=familyleft2_Daughter_strategy)
@settings(max_examples=50)
def test_familyleft2_daughter_instantiation(instance):
    assert isinstance(instance, familyleft2_Daughter)

@given(instance=familyleft2_Father_strategy)
@settings(max_examples=50)
def test_familyleft2_father_instantiation(instance):
    assert isinstance(instance, familyleft2_Father)



@given(instance=familyleft2_Father_strategy)
def test_familyleft2_father_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

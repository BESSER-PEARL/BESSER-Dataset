import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    familyright_Mother,
    familyright_Family,
    familyright_Father,
    familyright_Daughter,
    familyright_Son,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_familyright_mother_is_not_abstract():
    assert not inspect.isabstract(familyright_Mother)


def test_familyright_mother_constructor_exists():
    assert callable(familyright_Mother.__init__)


def test_familyright_mother_constructor_args():
    sig = inspect.signature(familyright_Mother.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyright_mother_has_age():
    assert hasattr(familyright_Mother, "age")
    descriptor = None
    for klass in familyright_Mother.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyright_mother_has_address():
    assert hasattr(familyright_Mother, "address")
    descriptor = None
    for klass in familyright_Mother.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_familyright_mother_has_name():
    assert hasattr(familyright_Mother, "name")
    descriptor = None
    for klass in familyright_Mother.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familyright_family_is_not_abstract():
    assert not inspect.isabstract(familyright_Family)


def test_familyright_family_constructor_exists():
    assert callable(familyright_Family.__init__)


def test_familyright_family_constructor_args():
    sig = inspect.signature(familyright_Family.__init__)
    params = list(sig.parameters.keys())



def test_familyright_father_is_not_abstract():
    assert not inspect.isabstract(familyright_Father)


def test_familyright_father_constructor_exists():
    assert callable(familyright_Father.__init__)


def test_familyright_father_constructor_args():
    sig = inspect.signature(familyright_Father.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_familyright_father_has_age():
    assert hasattr(familyright_Father, "age")
    descriptor = None
    for klass in familyright_Father.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_familyright_father_has_address():
    assert hasattr(familyright_Father, "address")
    descriptor = None
    for klass in familyright_Father.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_familyright_father_has_name():
    assert hasattr(familyright_Father, "name")
    descriptor = None
    for klass in familyright_Father.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_familyright_daughter_is_not_abstract():
    assert not inspect.isabstract(familyright_Daughter)


def test_familyright_daughter_constructor_exists():
    assert callable(familyright_Daughter.__init__)


def test_familyright_daughter_constructor_args():
    sig = inspect.signature(familyright_Daughter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_familyright_daughter_has_name():
    assert hasattr(familyright_Daughter, "name")
    descriptor = None
    for klass in familyright_Daughter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyright_daughter_has_age():
    assert hasattr(familyright_Daughter, "age")
    descriptor = None
    for klass in familyright_Daughter.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_familyright_son_is_not_abstract():
    assert not inspect.isabstract(familyright_Son)


def test_familyright_son_constructor_exists():
    assert callable(familyright_Son.__init__)


def test_familyright_son_constructor_args():
    sig = inspect.signature(familyright_Son.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_familyright_son_has_name():
    assert hasattr(familyright_Son, "name")
    descriptor = None
    for klass in familyright_Son.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_familyright_son_has_age():
    assert hasattr(familyright_Son, "age")
    descriptor = None
    for klass in familyright_Son.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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
familyright_Mother_strategy = st.builds(
    familyright_Mother,
    age=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text
)
familyright_Family_strategy = st.builds(
    familyright_Family,
)
familyright_Father_strategy = st.builds(
    familyright_Father,
    age=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text
)
familyright_Daughter_strategy = st.builds(
    familyright_Daughter,
    name=
        safe_text,
    age=
        st.integers()
)
familyright_Son_strategy = st.builds(
    familyright_Son,
    name=
        safe_text,
    age=
        st.integers()
)

@given(instance=familyright_Mother_strategy)
@settings(max_examples=50)
def test_familyright_mother_instantiation(instance):
    assert isinstance(instance, familyright_Mother)



@given(instance=familyright_Mother_strategy)
def test_familyright_mother_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=familyright_Mother_strategy)
def test_familyright_mother_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=familyright_Mother_strategy)
def test_familyright_mother_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyright_Family_strategy)
@settings(max_examples=50)
def test_familyright_family_instantiation(instance):
    assert isinstance(instance, familyright_Family)

@given(instance=familyright_Father_strategy)
@settings(max_examples=50)
def test_familyright_father_instantiation(instance):
    assert isinstance(instance, familyright_Father)



@given(instance=familyright_Father_strategy)
def test_familyright_father_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=familyright_Father_strategy)
def test_familyright_father_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=familyright_Father_strategy)
def test_familyright_father_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=familyright_Daughter_strategy)
@settings(max_examples=50)
def test_familyright_daughter_instantiation(instance):
    assert isinstance(instance, familyright_Daughter)



@given(instance=familyright_Daughter_strategy)
def test_familyright_daughter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=familyright_Daughter_strategy)
def test_familyright_daughter_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=familyright_Son_strategy)
@settings(max_examples=50)
def test_familyright_son_instantiation(instance):
    assert isinstance(instance, familyright_Son)



@given(instance=familyright_Son_strategy)
def test_familyright_son_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=familyright_Son_strategy)
def test_familyright_son_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

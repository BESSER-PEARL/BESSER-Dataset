import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::Family,
    family::course,
    family::university,
    family::person,
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



def test_family::course_is_not_abstract():
    assert not inspect.isabstract(family::course)


def test_family::course_constructor_exists():
    assert callable(family::course.__init__)


def test_family::course_constructor_args():
    sig = inspect.signature(family::course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::course_has_name():
    assert hasattr(family::course, "name")
    descriptor = None
    for klass in family::course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family::university_is_not_abstract():
    assert not inspect.isabstract(family::university)


def test_family::university_constructor_exists():
    assert callable(family::university.__init__)


def test_family::university_constructor_args():
    sig = inspect.signature(family::university.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::university_has_name():
    assert hasattr(family::university, "name")
    descriptor = None
    for klass in family::university.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::person)


def test_family::person_constructor_exists():
    assert callable(family::person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::person.__init__)
    params = list(sig.parameters.keys())
    assert "CPR" in params, "Missing parameter 'CPR'"
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_family::person_has_CPR():
    assert hasattr(family::person, "CPR")
    descriptor = None
    for klass in family::person.__mro__:
        if "CPR" in klass.__dict__:
            descriptor = klass.__dict__["CPR"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_age():
    assert hasattr(family::person, "age")
    descriptor = None
    for klass in family::person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_name():
    assert hasattr(family::person, "name")
    descriptor = None
    for klass in family::person.__mro__:
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
family::Family_strategy = st.builds(
    family::Family,
)
family::course_strategy = st.builds(
    family::course,
    name=
        safe_text
)
family::university_strategy = st.builds(
    family::university,
    name=
        safe_text
)
family::person_strategy = st.builds(
    family::person,
    CPR=
        safe_text,
    age=
        st.integers(),
    name=
        safe_text
)

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::course_strategy)
@settings(max_examples=50)
def test_family::course_instantiation(instance):
    assert isinstance(instance, family::course)

@given(instance=family::course_strategy)
def test_family::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::course_strategy)
def test_family::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::university_strategy)
@settings(max_examples=50)
def test_family::university_instantiation(instance):
    assert isinstance(instance, family::university)

@given(instance=family::university_strategy)
def test_family::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::university_strategy)
def test_family::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::person)

@given(instance=family::person_strategy)
def test_family::person_CPR_type(instance):
    assert isinstance(instance.CPR, str)


@given(instance=family::person_strategy)
def test_family::person_CPR_setter(instance):
    original = instance.CPR
    instance.CPR = original
    assert instance.CPR == original

@given(instance=family::person_strategy)
def test_family::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=family::person_strategy)
def test_family::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family::person_strategy)
def test_family::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::person_strategy)
def test_family::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_university,
    family_person,
    family_Family,
    family_course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_university_is_not_abstract():
    assert not inspect.isabstract(family_university)


def test_family_university_constructor_exists():
    assert callable(family_university.__init__)


def test_family_university_constructor_args():
    sig = inspect.signature(family_university.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_university_has_name():
    assert hasattr(family_university, "name")
    descriptor = None
    for klass in family_university.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_person)


def test_family_person_constructor_exists():
    assert callable(family_person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_person.__init__)
    params = list(sig.parameters.keys())
    assert "CPR" in params, "Missing parameter 'CPR'"
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_family_person_has_CPR():
    assert hasattr(family_person, "CPR")
    descriptor = None
    for klass in family_person.__mro__:
        if "CPR" in klass.__dict__:
            descriptor = klass.__dict__["CPR"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_name():
    assert hasattr(family_person, "name")
    descriptor = None
    for klass in family_person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family_person_has_age():
    assert hasattr(family_person, "age")
    descriptor = None
    for klass in family_person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())



def test_family_course_is_not_abstract():
    assert not inspect.isabstract(family_course)


def test_family_course_constructor_exists():
    assert callable(family_course.__init__)


def test_family_course_constructor_args():
    sig = inspect.signature(family_course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_course_has_name():
    assert hasattr(family_course, "name")
    descriptor = None
    for klass in family_course.__mro__:
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
family_university_strategy = st.builds(
    family_university,
    name=
        safe_text
)
family_person_strategy = st.builds(
    family_person,
    CPR=
        safe_text,
    name=
        safe_text,
    age=
        st.integers()
)
family_Family_strategy = st.builds(
    family_Family,
)
family_course_strategy = st.builds(
    family_course,
    name=
        safe_text
)

@given(instance=family_university_strategy)
@settings(max_examples=50)
def test_family_university_instantiation(instance):
    assert isinstance(instance, family_university)



@given(instance=family_university_strategy)
def test_family_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family_person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_person)



@given(instance=family_person_strategy)
def test_family_person_CPR_setter(instance):
    original = instance.CPR
    instance.CPR = original
    assert instance.CPR == original



@given(instance=family_person_strategy)
def test_family_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=family_person_strategy)
def test_family_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)

@given(instance=family_course_strategy)
@settings(max_examples=50)
def test_family_course_instantiation(instance):
    assert isinstance(instance, family_course)



@given(instance=family_course_strategy)
def test_family_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Univerity_University,
    Univerity_Person,
    Univerity_Courses,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_univerity_university_is_not_abstract():
    assert not inspect.isabstract(Univerity_University)


def test_univerity_university_constructor_exists():
    assert callable(Univerity_University.__init__)


def test_univerity_university_constructor_args():
    sig = inspect.signature(Univerity_University.__init__)
    params = list(sig.parameters.keys())



def test_univerity_person_is_not_abstract():
    assert not inspect.isabstract(Univerity_Person)


def test_univerity_person_constructor_exists():
    assert callable(Univerity_Person.__init__)


def test_univerity_person_constructor_args():
    sig = inspect.signature(Univerity_Person.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_univerity_person_has_Email():
    assert hasattr(Univerity_Person, "Email")
    descriptor = None
    for klass in Univerity_Person.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_univerity_person_has_Name():
    assert hasattr(Univerity_Person, "Name")
    descriptor = None
    for klass in Univerity_Person.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_univerity_courses_is_not_abstract():
    assert not inspect.isabstract(Univerity_Courses)


def test_univerity_courses_constructor_exists():
    assert callable(Univerity_Courses.__init__)


def test_univerity_courses_constructor_args():
    sig = inspect.signature(Univerity_Courses.__init__)
    params = list(sig.parameters.keys())
    assert "Semester" in params, "Missing parameter 'Semester'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "CFU" in params, "Missing parameter 'CFU'"

def test_univerity_courses_has_Semester():
    assert hasattr(Univerity_Courses, "Semester")
    descriptor = None
    for klass in Univerity_Courses.__mro__:
        if "Semester" in klass.__dict__:
            descriptor = klass.__dict__["Semester"]
            break
    assert isinstance(descriptor, property)

def test_univerity_courses_has_Name():
    assert hasattr(Univerity_Courses, "Name")
    descriptor = None
    for klass in Univerity_Courses.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_univerity_courses_has_CFU():
    assert hasattr(Univerity_Courses, "CFU")
    descriptor = None
    for klass in Univerity_Courses.__mro__:
        if "CFU" in klass.__dict__:
            descriptor = klass.__dict__["CFU"]
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
Univerity_University_strategy = st.builds(
    Univerity_University,
)
Univerity_Person_strategy = st.builds(
    Univerity_Person,
    Email=
        safe_text,
    Name=
        safe_text
)
Univerity_Courses_strategy = st.builds(
    Univerity_Courses,
    Semester=
        safe_text,
    Name=
        safe_text,
    CFU=
        st.integers()
)

@given(instance=Univerity_University_strategy)
@settings(max_examples=50)
def test_univerity_university_instantiation(instance):
    assert isinstance(instance, Univerity_University)

@given(instance=Univerity_Person_strategy)
@settings(max_examples=50)
def test_univerity_person_instantiation(instance):
    assert isinstance(instance, Univerity_Person)



@given(instance=Univerity_Person_strategy)
def test_univerity_person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Univerity_Person_strategy)
def test_univerity_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Univerity_Courses_strategy)
@settings(max_examples=50)
def test_univerity_courses_instantiation(instance):
    assert isinstance(instance, Univerity_Courses)



@given(instance=Univerity_Courses_strategy)
def test_univerity_courses_Semester_setter(instance):
    original = instance.Semester
    instance.Semester = original
    assert instance.Semester == original



@given(instance=Univerity_Courses_strategy)
def test_univerity_courses_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Univerity_Courses_strategy)
def test_univerity_courses_CFU_setter(instance):
    original = instance.CFU
    instance.CFU = original
    assert instance.CFU == original

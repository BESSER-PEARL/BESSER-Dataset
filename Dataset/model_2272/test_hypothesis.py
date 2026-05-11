import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Univerity::University,
    Univerity::Person,
    Univerity::Courses,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_univerity::university_is_not_abstract():
    assert not inspect.isabstract(Univerity::University)


def test_univerity::university_constructor_exists():
    assert callable(Univerity::University.__init__)


def test_univerity::university_constructor_args():
    sig = inspect.signature(Univerity::University.__init__)
    params = list(sig.parameters.keys())



def test_univerity::person_is_not_abstract():
    assert not inspect.isabstract(Univerity::Person)


def test_univerity::person_constructor_exists():
    assert callable(Univerity::Person.__init__)


def test_univerity::person_constructor_args():
    sig = inspect.signature(Univerity::Person.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_univerity::person_has_Name():
    assert hasattr(Univerity::Person, "Name")
    descriptor = None
    for klass in Univerity::Person.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_univerity::person_has_Email():
    assert hasattr(Univerity::Person, "Email")
    descriptor = None
    for klass in Univerity::Person.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_univerity::courses_is_not_abstract():
    assert not inspect.isabstract(Univerity::Courses)


def test_univerity::courses_constructor_exists():
    assert callable(Univerity::Courses.__init__)


def test_univerity::courses_constructor_args():
    sig = inspect.signature(Univerity::Courses.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "CFU" in params, "Missing parameter 'CFU'"
    assert "Semester" in params, "Missing parameter 'Semester'"

def test_univerity::courses_has_Name():
    assert hasattr(Univerity::Courses, "Name")
    descriptor = None
    for klass in Univerity::Courses.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_univerity::courses_has_CFU():
    assert hasattr(Univerity::Courses, "CFU")
    descriptor = None
    for klass in Univerity::Courses.__mro__:
        if "CFU" in klass.__dict__:
            descriptor = klass.__dict__["CFU"]
            break
    assert isinstance(descriptor, property)

def test_univerity::courses_has_Semester():
    assert hasattr(Univerity::Courses, "Semester")
    descriptor = None
    for klass in Univerity::Courses.__mro__:
        if "Semester" in klass.__dict__:
            descriptor = klass.__dict__["Semester"]
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
Univerity::University_strategy = st.builds(
    Univerity::University,
)
Univerity::Person_strategy = st.builds(
    Univerity::Person,
    Name=
        safe_text,
    Email=
        safe_text
)
Univerity::Courses_strategy = st.builds(
    Univerity::Courses,
    Name=
        safe_text,
    CFU=
        st.integers(),
    Semester=
        safe_text
)

@given(instance=Univerity::University_strategy)
@settings(max_examples=50)
def test_univerity::university_instantiation(instance):
    assert isinstance(instance, Univerity::University)

@given(instance=Univerity::Person_strategy)
@settings(max_examples=50)
def test_univerity::person_instantiation(instance):
    assert isinstance(instance, Univerity::Person)

@given(instance=Univerity::Person_strategy)
def test_univerity::person_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Univerity::Person_strategy)
def test_univerity::person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Univerity::Person_strategy)
def test_univerity::person_Email_type(instance):
    assert isinstance(instance.Email, str)


@given(instance=Univerity::Person_strategy)
def test_univerity::person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Univerity::Courses_strategy)
@settings(max_examples=50)
def test_univerity::courses_instantiation(instance):
    assert isinstance(instance, Univerity::Courses)

@given(instance=Univerity::Courses_strategy)
def test_univerity::courses_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Univerity::Courses_strategy)
def test_univerity::courses_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Univerity::Courses_strategy)
def test_univerity::courses_CFU_type(instance):
    assert isinstance(instance.CFU, int)


@given(instance=Univerity::Courses_strategy)
def test_univerity::courses_CFU_setter(instance):
    original = instance.CFU
    instance.CFU = original
    assert instance.CFU == original

@given(instance=Univerity::Courses_strategy)
def test_univerity::courses_Semester_type(instance):
    assert isinstance(instance.Semester, str)


@given(instance=Univerity::Courses_strategy)
def test_univerity::courses_Semester_setter(instance):
    original = instance.Semester
    instance.Semester = original
    assert instance.Semester == original

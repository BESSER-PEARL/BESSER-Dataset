import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    university_Address,
    university_Person,
    university_Staff,
    university_Course,
    university_CourseCatalog,
    Person,
    university_Professor,
    university_Assistant,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university_address_is_not_abstract():
    assert not inspect.isabstract(university_Address)


def test_university_address_constructor_exists():
    assert callable(university_Address.__init__)


def test_university_address_constructor_args():
    sig = inspect.signature(university_Address.__init__)
    params = list(sig.parameters.keys())



def test_university_person_is_not_abstract():
    assert not inspect.isabstract(university_Person)


def test_university_person_constructor_exists():
    assert callable(university_Person.__init__)


def test_university_person_constructor_args():
    sig = inspect.signature(university_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university_person_has_name():
    assert hasattr(university_Person, "name")
    descriptor = None
    for klass in university_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_staff_is_not_abstract():
    assert not inspect.isabstract(university_Staff)


def test_university_staff_constructor_exists():
    assert callable(university_Staff.__init__)


def test_university_staff_constructor_args():
    sig = inspect.signature(university_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "staff" in params, "Missing parameter 'staff'"

def test_university_staff_has_staff():
    assert hasattr(university_Staff, "staff")
    descriptor = None
    for klass in university_Staff.__mro__:
        if "staff" in klass.__dict__:
            descriptor = klass.__dict__["staff"]
            break
    assert isinstance(descriptor, property)



def test_university_course_is_not_abstract():
    assert not inspect.isabstract(university_Course)


def test_university_course_constructor_exists():
    assert callable(university_Course.__init__)


def test_university_course_constructor_args():
    sig = inspect.signature(university_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "etcs" in params, "Missing parameter 'etcs'"
    assert "id" in params, "Missing parameter 'id'"

def test_university_course_has_name():
    assert hasattr(university_Course, "name")
    descriptor = None
    for klass in university_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university_course_has_etcs():
    assert hasattr(university_Course, "etcs")
    descriptor = None
    for klass in university_Course.__mro__:
        if "etcs" in klass.__dict__:
            descriptor = klass.__dict__["etcs"]
            break
    assert isinstance(descriptor, property)

def test_university_course_has_id():
    assert hasattr(university_Course, "id")
    descriptor = None
    for klass in university_Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_university_coursecatalog_is_not_abstract():
    assert not inspect.isabstract(university_CourseCatalog)


def test_university_coursecatalog_constructor_exists():
    assert callable(university_CourseCatalog.__init__)


def test_university_coursecatalog_constructor_args():
    sig = inspect.signature(university_CourseCatalog.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_university_professor_is_not_abstract():
    assert not inspect.isabstract(university_Professor)


def test_university_professor_constructor_exists():
    assert callable(university_Professor.__init__)


def test_university_professor_constructor_args():
    sig = inspect.signature(university_Professor.__init__)
    params = list(sig.parameters.keys())



def test_university_assistant_is_not_abstract():
    assert not inspect.isabstract(university_Assistant)


def test_university_assistant_constructor_exists():
    assert callable(university_Assistant.__init__)


def test_university_assistant_constructor_args():
    sig = inspect.signature(university_Assistant.__init__)
    params = list(sig.parameters.keys())


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
university_Address_strategy = st.builds(
    university_Address,
)
university_Person_strategy = st.builds(
    university_Person,
    name=
        safe_text
)
university_Staff_strategy = st.builds(
    university_Staff,
    staff=
        safe_text
)
university_Course_strategy = st.builds(
    university_Course,
    name=
        safe_text,
    etcs=
        st.integers(),
    id=
        safe_text
)
university_CourseCatalog_strategy = st.builds(
    university_CourseCatalog,
)
Person_strategy = st.builds(
    Person,
)
university_Professor_strategy = st.builds(
    university_Professor,
)
university_Assistant_strategy = st.builds(
    university_Assistant,
)

@given(instance=university_Address_strategy)
@settings(max_examples=50)
def test_university_address_instantiation(instance):
    assert isinstance(instance, university_Address)

@given(instance=university_Person_strategy)
@settings(max_examples=50)
def test_university_person_instantiation(instance):
    assert isinstance(instance, university_Person)



@given(instance=university_Person_strategy)
def test_university_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_Staff_strategy)
@settings(max_examples=50)
def test_university_staff_instantiation(instance):
    assert isinstance(instance, university_Staff)



@given(instance=university_Staff_strategy)
def test_university_staff_staff_setter(instance):
    original = instance.staff
    instance.staff = original
    assert instance.staff == original

@given(instance=university_Course_strategy)
@settings(max_examples=50)
def test_university_course_instantiation(instance):
    assert isinstance(instance, university_Course)



@given(instance=university_Course_strategy)
def test_university_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=university_Course_strategy)
def test_university_course_etcs_setter(instance):
    original = instance.etcs
    instance.etcs = original
    assert instance.etcs == original



@given(instance=university_Course_strategy)
def test_university_course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=university_CourseCatalog_strategy)
@settings(max_examples=50)
def test_university_coursecatalog_instantiation(instance):
    assert isinstance(instance, university_CourseCatalog)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=university_Professor_strategy)
@settings(max_examples=50)
def test_university_professor_instantiation(instance):
    assert isinstance(instance, university_Professor)

@given(instance=university_Assistant_strategy)
@settings(max_examples=50)
def test_university_assistant_instantiation(instance):
    assert isinstance(instance, university_Assistant)

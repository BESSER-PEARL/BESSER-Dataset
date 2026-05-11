import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    university::Address,
    university::Person,
    university::Staff,
    university::Course,
    university::CourseCatalog,
    Person,
    university::Professor,
    university::Assistant,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university::address_is_not_abstract():
    assert not inspect.isabstract(university::Address)


def test_university::address_constructor_exists():
    assert callable(university::Address.__init__)


def test_university::address_constructor_args():
    sig = inspect.signature(university::Address.__init__)
    params = list(sig.parameters.keys())



def test_university::person_is_not_abstract():
    assert not inspect.isabstract(university::Person)


def test_university::person_constructor_exists():
    assert callable(university::Person.__init__)


def test_university::person_constructor_args():
    sig = inspect.signature(university::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::person_has_name():
    assert hasattr(university::Person, "name")
    descriptor = None
    for klass in university::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::staff_is_not_abstract():
    assert not inspect.isabstract(university::Staff)


def test_university::staff_constructor_exists():
    assert callable(university::Staff.__init__)


def test_university::staff_constructor_args():
    sig = inspect.signature(university::Staff.__init__)
    params = list(sig.parameters.keys())
    assert "staff" in params, "Missing parameter 'staff'"

def test_university::staff_has_staff():
    assert hasattr(university::Staff, "staff")
    descriptor = None
    for klass in university::Staff.__mro__:
        if "staff" in klass.__dict__:
            descriptor = klass.__dict__["staff"]
            break
    assert isinstance(descriptor, property)



def test_university::course_is_not_abstract():
    assert not inspect.isabstract(university::Course)


def test_university::course_constructor_exists():
    assert callable(university::Course.__init__)


def test_university::course_constructor_args():
    sig = inspect.signature(university::Course.__init__)
    params = list(sig.parameters.keys())
    assert "etcs" in params, "Missing parameter 'etcs'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_university::course_has_etcs():
    assert hasattr(university::Course, "etcs")
    descriptor = None
    for klass in university::Course.__mro__:
        if "etcs" in klass.__dict__:
            descriptor = klass.__dict__["etcs"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_id():
    assert hasattr(university::Course, "id")
    descriptor = None
    for klass in university::Course.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_university::course_has_name():
    assert hasattr(university::Course, "name")
    descriptor = None
    for klass in university::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::coursecatalog_is_not_abstract():
    assert not inspect.isabstract(university::CourseCatalog)


def test_university::coursecatalog_constructor_exists():
    assert callable(university::CourseCatalog.__init__)


def test_university::coursecatalog_constructor_args():
    sig = inspect.signature(university::CourseCatalog.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_university::professor_is_not_abstract():
    assert not inspect.isabstract(university::Professor)


def test_university::professor_constructor_exists():
    assert callable(university::Professor.__init__)


def test_university::professor_constructor_args():
    sig = inspect.signature(university::Professor.__init__)
    params = list(sig.parameters.keys())



def test_university::assistant_is_not_abstract():
    assert not inspect.isabstract(university::Assistant)


def test_university::assistant_constructor_exists():
    assert callable(university::Assistant.__init__)


def test_university::assistant_constructor_args():
    sig = inspect.signature(university::Assistant.__init__)
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
university::Address_strategy = st.builds(
    university::Address,
)
university::Person_strategy = st.builds(
    university::Person,
    name=
        safe_text
)
university::Staff_strategy = st.builds(
    university::Staff,
    staff=
        safe_text
)
university::Course_strategy = st.builds(
    university::Course,
    etcs=
        st.integers(),
    id=
        safe_text,
    name=
        safe_text
)
university::CourseCatalog_strategy = st.builds(
    university::CourseCatalog,
)
Person_strategy = st.builds(
    Person,
)
university::Professor_strategy = st.builds(
    university::Professor,
)
university::Assistant_strategy = st.builds(
    university::Assistant,
)

@given(instance=university::Address_strategy)
@settings(max_examples=50)
def test_university::address_instantiation(instance):
    assert isinstance(instance, university::Address)

@given(instance=university::Person_strategy)
@settings(max_examples=50)
def test_university::person_instantiation(instance):
    assert isinstance(instance, university::Person)

@given(instance=university::Person_strategy)
def test_university::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Person_strategy)
def test_university::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Staff_strategy)
@settings(max_examples=50)
def test_university::staff_instantiation(instance):
    assert isinstance(instance, university::Staff)

@given(instance=university::Staff_strategy)
def test_university::staff_staff_type(instance):
    assert isinstance(instance.staff, str)


@given(instance=university::Staff_strategy)
def test_university::staff_staff_setter(instance):
    original = instance.staff
    instance.staff = original
    assert instance.staff == original

@given(instance=university::Course_strategy)
@settings(max_examples=50)
def test_university::course_instantiation(instance):
    assert isinstance(instance, university::Course)

@given(instance=university::Course_strategy)
def test_university::course_etcs_type(instance):
    assert isinstance(instance.etcs, int)


@given(instance=university::Course_strategy)
def test_university::course_etcs_setter(instance):
    original = instance.etcs
    instance.etcs = original
    assert instance.etcs == original

@given(instance=university::Course_strategy)
def test_university::course_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=university::Course_strategy)
def test_university::course_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=university::Course_strategy)
def test_university::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Course_strategy)
def test_university::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::CourseCatalog_strategy)
@settings(max_examples=50)
def test_university::coursecatalog_instantiation(instance):
    assert isinstance(instance, university::CourseCatalog)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=university::Professor_strategy)
@settings(max_examples=50)
def test_university::professor_instantiation(instance):
    assert isinstance(instance, university::Professor)

@given(instance=university::Assistant_strategy)
@settings(max_examples=50)
def test_university::assistant_instantiation(instance):
    assert isinstance(instance, university::Assistant)

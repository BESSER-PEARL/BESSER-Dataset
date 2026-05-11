import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classmate::Classroom,
    classmate::Friend,
    classmate::School,
    classmate::ClassmateSystem,
    classmate::Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classmate::classroom_is_not_abstract():
    assert not inspect.isabstract(classmate::Classroom)


def test_classmate::classroom_constructor_exists():
    assert callable(classmate::Classroom.__init__)


def test_classmate::classroom_constructor_args():
    sig = inspect.signature(classmate::Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmate::classroom_has_name():
    assert hasattr(classmate::Classroom, "name")
    descriptor = None
    for klass in classmate::Classroom.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmate::friend_is_not_abstract():
    assert not inspect.isabstract(classmate::Friend)


def test_classmate::friend_constructor_exists():
    assert callable(classmate::Friend.__init__)


def test_classmate::friend_constructor_args():
    sig = inspect.signature(classmate::Friend.__init__)
    params = list(sig.parameters.keys())
    assert "fromDate" in params, "Missing parameter 'fromDate'"
    assert "toDate" in params, "Missing parameter 'toDate'"

def test_classmate::friend_has_fromDate():
    assert hasattr(classmate::Friend, "fromDate")
    descriptor = None
    for klass in classmate::Friend.__mro__:
        if "fromDate" in klass.__dict__:
            descriptor = klass.__dict__["fromDate"]
            break
    assert isinstance(descriptor, property)

def test_classmate::friend_has_toDate():
    assert hasattr(classmate::Friend, "toDate")
    descriptor = None
    for klass in classmate::Friend.__mro__:
        if "toDate" in klass.__dict__:
            descriptor = klass.__dict__["toDate"]
            break
    assert isinstance(descriptor, property)



def test_classmate::school_is_not_abstract():
    assert not inspect.isabstract(classmate::School)


def test_classmate::school_constructor_exists():
    assert callable(classmate::School.__init__)


def test_classmate::school_constructor_args():
    sig = inspect.signature(classmate::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmate::school_has_name():
    assert hasattr(classmate::School, "name")
    descriptor = None
    for klass in classmate::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmate::classmatesystem_is_not_abstract():
    assert not inspect.isabstract(classmate::ClassmateSystem)


def test_classmate::classmatesystem_constructor_exists():
    assert callable(classmate::ClassmateSystem.__init__)


def test_classmate::classmatesystem_constructor_args():
    sig = inspect.signature(classmate::ClassmateSystem.__init__)
    params = list(sig.parameters.keys())



def test_classmate::student_is_not_abstract():
    assert not inspect.isabstract(classmate::Student)


def test_classmate::student_constructor_exists():
    assert callable(classmate::Student.__init__)


def test_classmate::student_constructor_args():
    sig = inspect.signature(classmate::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmate::student_has_name():
    assert hasattr(classmate::Student, "name")
    descriptor = None
    for klass in classmate::Student.__mro__:
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
classmate::Classroom_strategy = st.builds(
    classmate::Classroom,
    name=
        safe_text
)
classmate::Friend_strategy = st.builds(
    classmate::Friend,
    fromDate=
        safe_text,
    toDate=
        safe_text
)
classmate::School_strategy = st.builds(
    classmate::School,
    name=
        safe_text
)
classmate::ClassmateSystem_strategy = st.builds(
    classmate::ClassmateSystem,
)
classmate::Student_strategy = st.builds(
    classmate::Student,
    name=
        safe_text
)

@given(instance=classmate::Classroom_strategy)
@settings(max_examples=50)
def test_classmate::classroom_instantiation(instance):
    assert isinstance(instance, classmate::Classroom)

@given(instance=classmate::Classroom_strategy)
def test_classmate::classroom_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmate::Classroom_strategy)
def test_classmate::classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmate::Friend_strategy)
@settings(max_examples=50)
def test_classmate::friend_instantiation(instance):
    assert isinstance(instance, classmate::Friend)

@given(instance=classmate::Friend_strategy)
def test_classmate::friend_fromDate_type(instance):
    assert isinstance(instance.fromDate, str)


@given(instance=classmate::Friend_strategy)
def test_classmate::friend_fromDate_setter(instance):
    original = instance.fromDate
    instance.fromDate = original
    assert instance.fromDate == original

@given(instance=classmate::Friend_strategy)
def test_classmate::friend_toDate_type(instance):
    assert isinstance(instance.toDate, str)


@given(instance=classmate::Friend_strategy)
def test_classmate::friend_toDate_setter(instance):
    original = instance.toDate
    instance.toDate = original
    assert instance.toDate == original

@given(instance=classmate::School_strategy)
@settings(max_examples=50)
def test_classmate::school_instantiation(instance):
    assert isinstance(instance, classmate::School)

@given(instance=classmate::School_strategy)
def test_classmate::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmate::School_strategy)
def test_classmate::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmate::ClassmateSystem_strategy)
@settings(max_examples=50)
def test_classmate::classmatesystem_instantiation(instance):
    assert isinstance(instance, classmate::ClassmateSystem)

@given(instance=classmate::Student_strategy)
@settings(max_examples=50)
def test_classmate::student_instantiation(instance):
    assert isinstance(instance, classmate::Student)

@given(instance=classmate::Student_strategy)
def test_classmate::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmate::Student_strategy)
def test_classmate::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

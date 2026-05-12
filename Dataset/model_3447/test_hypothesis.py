import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    classmate_Classroom,
    classmate_Friend,
    classmate_School,
    classmate_ClassmateSystem,
    classmate_Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classmate_classroom_is_not_abstract():
    assert not inspect.isabstract(classmate_Classroom)


def test_classmate_classroom_constructor_exists():
    assert callable(classmate_Classroom.__init__)


def test_classmate_classroom_constructor_args():
    sig = inspect.signature(classmate_Classroom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmate_classroom_has_name():
    assert hasattr(classmate_Classroom, "name")
    descriptor = None
    for klass in classmate_Classroom.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmate_friend_is_not_abstract():
    assert not inspect.isabstract(classmate_Friend)


def test_classmate_friend_constructor_exists():
    assert callable(classmate_Friend.__init__)


def test_classmate_friend_constructor_args():
    sig = inspect.signature(classmate_Friend.__init__)
    params = list(sig.parameters.keys())
    assert "fromDate" in params, "Missing parameter 'fromDate'"
    assert "toDate" in params, "Missing parameter 'toDate'"

def test_classmate_friend_has_fromDate():
    assert hasattr(classmate_Friend, "fromDate")
    descriptor = None
    for klass in classmate_Friend.__mro__:
        if "fromDate" in klass.__dict__:
            descriptor = klass.__dict__["fromDate"]
            break
    assert isinstance(descriptor, property)

def test_classmate_friend_has_toDate():
    assert hasattr(classmate_Friend, "toDate")
    descriptor = None
    for klass in classmate_Friend.__mro__:
        if "toDate" in klass.__dict__:
            descriptor = klass.__dict__["toDate"]
            break
    assert isinstance(descriptor, property)



def test_classmate_school_is_not_abstract():
    assert not inspect.isabstract(classmate_School)


def test_classmate_school_constructor_exists():
    assert callable(classmate_School.__init__)


def test_classmate_school_constructor_args():
    sig = inspect.signature(classmate_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmate_school_has_name():
    assert hasattr(classmate_School, "name")
    descriptor = None
    for klass in classmate_School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmate_classmatesystem_is_not_abstract():
    assert not inspect.isabstract(classmate_ClassmateSystem)


def test_classmate_classmatesystem_constructor_exists():
    assert callable(classmate_ClassmateSystem.__init__)


def test_classmate_classmatesystem_constructor_args():
    sig = inspect.signature(classmate_ClassmateSystem.__init__)
    params = list(sig.parameters.keys())



def test_classmate_student_is_not_abstract():
    assert not inspect.isabstract(classmate_Student)


def test_classmate_student_constructor_exists():
    assert callable(classmate_Student.__init__)


def test_classmate_student_constructor_args():
    sig = inspect.signature(classmate_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmate_student_has_name():
    assert hasattr(classmate_Student, "name")
    descriptor = None
    for klass in classmate_Student.__mro__:
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
classmate_Classroom_strategy = st.builds(
    classmate_Classroom,
    name=
        safe_text
)
classmate_Friend_strategy = st.builds(
    classmate_Friend,
    fromDate=
        safe_text,
    toDate=
        safe_text
)
classmate_School_strategy = st.builds(
    classmate_School,
    name=
        safe_text
)
classmate_ClassmateSystem_strategy = st.builds(
    classmate_ClassmateSystem,
)
classmate_Student_strategy = st.builds(
    classmate_Student,
    name=
        safe_text
)

@given(instance=classmate_Classroom_strategy)
@settings(max_examples=50)
def test_classmate_classroom_instantiation(instance):
    assert isinstance(instance, classmate_Classroom)



@given(instance=classmate_Classroom_strategy)
def test_classmate_classroom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmate_Friend_strategy)
@settings(max_examples=50)
def test_classmate_friend_instantiation(instance):
    assert isinstance(instance, classmate_Friend)



@given(instance=classmate_Friend_strategy)
def test_classmate_friend_fromDate_setter(instance):
    original = instance.fromDate
    instance.fromDate = original
    assert instance.fromDate == original



@given(instance=classmate_Friend_strategy)
def test_classmate_friend_toDate_setter(instance):
    original = instance.toDate
    instance.toDate = original
    assert instance.toDate == original

@given(instance=classmate_School_strategy)
@settings(max_examples=50)
def test_classmate_school_instantiation(instance):
    assert isinstance(instance, classmate_School)



@given(instance=classmate_School_strategy)
def test_classmate_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmate_ClassmateSystem_strategy)
@settings(max_examples=50)
def test_classmate_classmatesystem_instantiation(instance):
    assert isinstance(instance, classmate_ClassmateSystem)

@given(instance=classmate_Student_strategy)
@settings(max_examples=50)
def test_classmate_student_instantiation(instance):
    assert isinstance(instance, classmate_Student)



@given(instance=classmate_Student_strategy)
def test_classmate_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

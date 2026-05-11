import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    epdemo::Teacher,
    epdemo::Student,
    epdemo::Clazz,
    epdemo::School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_epdemo::teacher_is_not_abstract():
    assert not inspect.isabstract(epdemo::Teacher)


def test_epdemo::teacher_constructor_exists():
    assert callable(epdemo::Teacher.__init__)


def test_epdemo::teacher_constructor_args():
    sig = inspect.signature(epdemo::Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_epdemo::teacher_has_Id():
    assert hasattr(epdemo::Teacher, "Id")
    descriptor = None
    for klass in epdemo::Teacher.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_epdemo::teacher_has_Name():
    assert hasattr(epdemo::Teacher, "Name")
    descriptor = None
    for klass in epdemo::Teacher.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_epdemo::student_is_not_abstract():
    assert not inspect.isabstract(epdemo::Student)


def test_epdemo::student_constructor_exists():
    assert callable(epdemo::Student.__init__)


def test_epdemo::student_constructor_args():
    sig = inspect.signature(epdemo::Student.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_epdemo::student_has_Name():
    assert hasattr(epdemo::Student, "Name")
    descriptor = None
    for klass in epdemo::Student.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_epdemo::student_has_Id():
    assert hasattr(epdemo::Student, "Id")
    descriptor = None
    for klass in epdemo::Student.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_epdemo::clazz_is_not_abstract():
    assert not inspect.isabstract(epdemo::Clazz)


def test_epdemo::clazz_constructor_exists():
    assert callable(epdemo::Clazz.__init__)


def test_epdemo::clazz_constructor_args():
    sig = inspect.signature(epdemo::Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_epdemo::clazz_has_Id():
    assert hasattr(epdemo::Clazz, "Id")
    descriptor = None
    for klass in epdemo::Clazz.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_epdemo::clazz_has_Name():
    assert hasattr(epdemo::Clazz, "Name")
    descriptor = None
    for klass in epdemo::Clazz.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_epdemo::school_is_not_abstract():
    assert not inspect.isabstract(epdemo::School)


def test_epdemo::school_constructor_exists():
    assert callable(epdemo::School.__init__)


def test_epdemo::school_constructor_args():
    sig = inspect.signature(epdemo::School.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_epdemo::school_has_Name():
    assert hasattr(epdemo::School, "Name")
    descriptor = None
    for klass in epdemo::School.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_epdemo::school_has_Id():
    assert hasattr(epdemo::School, "Id")
    descriptor = None
    for klass in epdemo::School.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
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
epdemo::Teacher_strategy = st.builds(
    epdemo::Teacher,
    Id=
        safe_text,
    Name=
        safe_text
)
epdemo::Student_strategy = st.builds(
    epdemo::Student,
    Name=
        safe_text,
    Id=
        safe_text
)
epdemo::Clazz_strategy = st.builds(
    epdemo::Clazz,
    Id=
        safe_text,
    Name=
        safe_text
)
epdemo::School_strategy = st.builds(
    epdemo::School,
    Name=
        safe_text,
    Id=
        safe_text
)

@given(instance=epdemo::Teacher_strategy)
@settings(max_examples=50)
def test_epdemo::teacher_instantiation(instance):
    assert isinstance(instance, epdemo::Teacher)

@given(instance=epdemo::Teacher_strategy)
def test_epdemo::teacher_Id_type(instance):
    assert isinstance(instance.Id, str)


@given(instance=epdemo::Teacher_strategy)
def test_epdemo::teacher_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=epdemo::Teacher_strategy)
def test_epdemo::teacher_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=epdemo::Teacher_strategy)
def test_epdemo::teacher_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=epdemo::Student_strategy)
@settings(max_examples=50)
def test_epdemo::student_instantiation(instance):
    assert isinstance(instance, epdemo::Student)

@given(instance=epdemo::Student_strategy)
def test_epdemo::student_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=epdemo::Student_strategy)
def test_epdemo::student_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=epdemo::Student_strategy)
def test_epdemo::student_Id_type(instance):
    assert isinstance(instance.Id, str)


@given(instance=epdemo::Student_strategy)
def test_epdemo::student_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=epdemo::Clazz_strategy)
@settings(max_examples=50)
def test_epdemo::clazz_instantiation(instance):
    assert isinstance(instance, epdemo::Clazz)

@given(instance=epdemo::Clazz_strategy)
def test_epdemo::clazz_Id_type(instance):
    assert isinstance(instance.Id, str)


@given(instance=epdemo::Clazz_strategy)
def test_epdemo::clazz_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=epdemo::Clazz_strategy)
def test_epdemo::clazz_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=epdemo::Clazz_strategy)
def test_epdemo::clazz_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=epdemo::School_strategy)
@settings(max_examples=50)
def test_epdemo::school_instantiation(instance):
    assert isinstance(instance, epdemo::School)

@given(instance=epdemo::School_strategy)
def test_epdemo::school_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=epdemo::School_strategy)
def test_epdemo::school_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=epdemo::School_strategy)
def test_epdemo::school_Id_type(instance):
    assert isinstance(instance.Id, str)


@given(instance=epdemo::School_strategy)
def test_epdemo::school_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

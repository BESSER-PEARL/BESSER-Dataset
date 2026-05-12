import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    epdemo_Teacher,
    epdemo_Student,
    epdemo_Clazz,
    epdemo_School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_epdemo_teacher_is_not_abstract():
    assert not inspect.isabstract(epdemo_Teacher)


def test_epdemo_teacher_constructor_exists():
    assert callable(epdemo_Teacher.__init__)


def test_epdemo_teacher_constructor_args():
    sig = inspect.signature(epdemo_Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_epdemo_teacher_has_Name():
    assert hasattr(epdemo_Teacher, "Name")
    descriptor = None
    for klass in epdemo_Teacher.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_epdemo_teacher_has_Id():
    assert hasattr(epdemo_Teacher, "Id")
    descriptor = None
    for klass in epdemo_Teacher.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_epdemo_student_is_not_abstract():
    assert not inspect.isabstract(epdemo_Student)


def test_epdemo_student_constructor_exists():
    assert callable(epdemo_Student.__init__)


def test_epdemo_student_constructor_args():
    sig = inspect.signature(epdemo_Student.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_epdemo_student_has_Name():
    assert hasattr(epdemo_Student, "Name")
    descriptor = None
    for klass in epdemo_Student.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_epdemo_student_has_Id():
    assert hasattr(epdemo_Student, "Id")
    descriptor = None
    for klass in epdemo_Student.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_epdemo_clazz_is_not_abstract():
    assert not inspect.isabstract(epdemo_Clazz)


def test_epdemo_clazz_constructor_exists():
    assert callable(epdemo_Clazz.__init__)


def test_epdemo_clazz_constructor_args():
    sig = inspect.signature(epdemo_Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_epdemo_clazz_has_Name():
    assert hasattr(epdemo_Clazz, "Name")
    descriptor = None
    for klass in epdemo_Clazz.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_epdemo_clazz_has_Id():
    assert hasattr(epdemo_Clazz, "Id")
    descriptor = None
    for klass in epdemo_Clazz.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_epdemo_school_is_not_abstract():
    assert not inspect.isabstract(epdemo_School)


def test_epdemo_school_constructor_exists():
    assert callable(epdemo_School.__init__)


def test_epdemo_school_constructor_args():
    sig = inspect.signature(epdemo_School.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_epdemo_school_has_Name():
    assert hasattr(epdemo_School, "Name")
    descriptor = None
    for klass in epdemo_School.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_epdemo_school_has_Id():
    assert hasattr(epdemo_School, "Id")
    descriptor = None
    for klass in epdemo_School.__mro__:
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
epdemo_Teacher_strategy = st.builds(
    epdemo_Teacher,
    Name=
        safe_text,
    Id=
        safe_text
)
epdemo_Student_strategy = st.builds(
    epdemo_Student,
    Name=
        safe_text,
    Id=
        safe_text
)
epdemo_Clazz_strategy = st.builds(
    epdemo_Clazz,
    Name=
        safe_text,
    Id=
        safe_text
)
epdemo_School_strategy = st.builds(
    epdemo_School,
    Name=
        safe_text,
    Id=
        safe_text
)

@given(instance=epdemo_Teacher_strategy)
@settings(max_examples=50)
def test_epdemo_teacher_instantiation(instance):
    assert isinstance(instance, epdemo_Teacher)



@given(instance=epdemo_Teacher_strategy)
def test_epdemo_teacher_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=epdemo_Teacher_strategy)
def test_epdemo_teacher_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=epdemo_Student_strategy)
@settings(max_examples=50)
def test_epdemo_student_instantiation(instance):
    assert isinstance(instance, epdemo_Student)



@given(instance=epdemo_Student_strategy)
def test_epdemo_student_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=epdemo_Student_strategy)
def test_epdemo_student_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=epdemo_Clazz_strategy)
@settings(max_examples=50)
def test_epdemo_clazz_instantiation(instance):
    assert isinstance(instance, epdemo_Clazz)



@given(instance=epdemo_Clazz_strategy)
def test_epdemo_clazz_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=epdemo_Clazz_strategy)
def test_epdemo_clazz_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=epdemo_School_strategy)
@settings(max_examples=50)
def test_epdemo_school_instantiation(instance):
    assert isinstance(instance, epdemo_School)



@given(instance=epdemo_School_strategy)
def test_epdemo_school_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=epdemo_School_strategy)
def test_epdemo_school_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

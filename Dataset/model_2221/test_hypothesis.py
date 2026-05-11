import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    oving1APD::Slot,
    oving1APD::Course,
    oving1APD::StudyProgram,
    oving1APD::Department,
    oving1APD::Semester,
    oving1APD::Specialization,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oving1apd::slot_is_not_abstract():
    assert not inspect.isabstract(oving1APD::Slot)


def test_oving1apd::slot_constructor_exists():
    assert callable(oving1APD::Slot.__init__)


def test_oving1apd::slot_constructor_args():
    sig = inspect.signature(oving1APD::Slot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oving1apd::slot_has_name():
    assert hasattr(oving1APD::Slot, "name")
    descriptor = None
    for klass in oving1APD::Slot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oving1apd::course_is_not_abstract():
    assert not inspect.isabstract(oving1APD::Course)


def test_oving1apd::course_constructor_exists():
    assert callable(oving1APD::Course.__init__)


def test_oving1apd::course_constructor_args():
    sig = inspect.signature(oving1APD::Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credit" in params, "Missing parameter 'credit'"

def test_oving1apd::course_has_level():
    assert hasattr(oving1APD::Course, "level")
    descriptor = None
    for klass in oving1APD::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_oving1apd::course_has_code():
    assert hasattr(oving1APD::Course, "code")
    descriptor = None
    for klass in oving1APD::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_oving1apd::course_has_name():
    assert hasattr(oving1APD::Course, "name")
    descriptor = None
    for klass in oving1APD::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving1apd::course_has_credit():
    assert hasattr(oving1APD::Course, "credit")
    descriptor = None
    for klass in oving1APD::Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)



def test_oving1apd::studyprogram_is_not_abstract():
    assert not inspect.isabstract(oving1APD::StudyProgram)


def test_oving1apd::studyprogram_constructor_exists():
    assert callable(oving1APD::StudyProgram.__init__)


def test_oving1apd::studyprogram_constructor_args():
    sig = inspect.signature(oving1APD::StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"

def test_oving1apd::studyprogram_has_shortName():
    assert hasattr(oving1APD::StudyProgram, "shortName")
    descriptor = None
    for klass in oving1APD::StudyProgram.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_oving1apd::studyprogram_has_name():
    assert hasattr(oving1APD::StudyProgram, "name")
    descriptor = None
    for klass in oving1APD::StudyProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oving1apd::department_is_not_abstract():
    assert not inspect.isabstract(oving1APD::Department)


def test_oving1apd::department_constructor_exists():
    assert callable(oving1APD::Department.__init__)


def test_oving1apd::department_constructor_args():
    sig = inspect.signature(oving1APD::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shortName" in params, "Missing parameter 'shortName'"

def test_oving1apd::department_has_name():
    assert hasattr(oving1APD::Department, "name")
    descriptor = None
    for klass in oving1APD::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oving1apd::department_has_shortName():
    assert hasattr(oving1APD::Department, "shortName")
    descriptor = None
    for klass in oving1APD::Department.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)



def test_oving1apd::semester_is_not_abstract():
    assert not inspect.isabstract(oving1APD::Semester)


def test_oving1apd::semester_constructor_exists():
    assert callable(oving1APD::Semester.__init__)


def test_oving1apd::semester_constructor_args():
    sig = inspect.signature(oving1APD::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_oving1apd::semester_has_number():
    assert hasattr(oving1APD::Semester, "number")
    descriptor = None
    for klass in oving1APD::Semester.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_oving1apd::specialization_is_not_abstract():
    assert not inspect.isabstract(oving1APD::Specialization)


def test_oving1apd::specialization_constructor_exists():
    assert callable(oving1APD::Specialization.__init__)


def test_oving1apd::specialization_constructor_args():
    sig = inspect.signature(oving1APD::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oving1apd::specialization_has_name():
    assert hasattr(oving1APD::Specialization, "name")
    descriptor = None
    for klass in oving1APD::Specialization.__mro__:
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
oving1APD::Slot_strategy = st.builds(
    oving1APD::Slot,
    name=
        safe_text
)
oving1APD::Course_strategy = st.builds(
    oving1APD::Course,
    level=
        st.integers(),
    code=
        safe_text,
    name=
        safe_text,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oving1APD::StudyProgram_strategy = st.builds(
    oving1APD::StudyProgram,
    shortName=
        safe_text,
    name=
        safe_text
)
oving1APD::Department_strategy = st.builds(
    oving1APD::Department,
    name=
        safe_text,
    shortName=
        safe_text
)
oving1APD::Semester_strategy = st.builds(
    oving1APD::Semester,
    number=
        st.integers()
)
oving1APD::Specialization_strategy = st.builds(
    oving1APD::Specialization,
    name=
        safe_text
)

@given(instance=oving1APD::Slot_strategy)
@settings(max_examples=50)
def test_oving1apd::slot_instantiation(instance):
    assert isinstance(instance, oving1APD::Slot)

@given(instance=oving1APD::Slot_strategy)
def test_oving1apd::slot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving1APD::Slot_strategy)
def test_oving1apd::slot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving1APD::Course_strategy)
@settings(max_examples=50)
def test_oving1apd::course_instantiation(instance):
    assert isinstance(instance, oving1APD::Course)

@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=oving1APD::Course_strategy)
def test_oving1apd::course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=oving1APD::StudyProgram_strategy)
@settings(max_examples=50)
def test_oving1apd::studyprogram_instantiation(instance):
    assert isinstance(instance, oving1APD::StudyProgram)

@given(instance=oving1APD::StudyProgram_strategy)
def test_oving1apd::studyprogram_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=oving1APD::StudyProgram_strategy)
def test_oving1apd::studyprogram_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=oving1APD::StudyProgram_strategy)
def test_oving1apd::studyprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving1APD::StudyProgram_strategy)
def test_oving1apd::studyprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving1APD::Department_strategy)
@settings(max_examples=50)
def test_oving1apd::department_instantiation(instance):
    assert isinstance(instance, oving1APD::Department)

@given(instance=oving1APD::Department_strategy)
def test_oving1apd::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving1APD::Department_strategy)
def test_oving1apd::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oving1APD::Department_strategy)
def test_oving1apd::department_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=oving1APD::Department_strategy)
def test_oving1apd::department_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=oving1APD::Semester_strategy)
@settings(max_examples=50)
def test_oving1apd::semester_instantiation(instance):
    assert isinstance(instance, oving1APD::Semester)

@given(instance=oving1APD::Semester_strategy)
def test_oving1apd::semester_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=oving1APD::Semester_strategy)
def test_oving1apd::semester_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=oving1APD::Specialization_strategy)
@settings(max_examples=50)
def test_oving1apd::specialization_instantiation(instance):
    assert isinstance(instance, oving1APD::Specialization)

@given(instance=oving1APD::Specialization_strategy)
def test_oving1apd::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oving1APD::Specialization_strategy)
def test_oving1apd::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

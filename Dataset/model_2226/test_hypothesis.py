import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Program::Department,
    Program::Course,
    Program::SemesterCourse,
    Program::Semester,
    Program::Program,
    Program::Specialization,
    CourseStatus,
    SemesterStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_program::department_is_not_abstract():
    assert not inspect.isabstract(Program::Department)


def test_program::department_constructor_exists():
    assert callable(Program::Department.__init__)


def test_program::department_constructor_args():
    sig = inspect.signature(Program::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_program::department_has_name():
    assert hasattr(Program::Department, "name")
    descriptor = None
    for klass in Program::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_program::course_is_not_abstract():
    assert not inspect.isabstract(Program::Course)


def test_program::course_constructor_exists():
    assert callable(Program::Course.__init__)


def test_program::course_constructor_args():
    sig = inspect.signature(Program::Course.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_program::course_has_credit():
    assert hasattr(Program::Course, "credit")
    descriptor = None
    for klass in Program::Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_program::course_has_code():
    assert hasattr(Program::Course, "code")
    descriptor = None
    for klass in Program::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_program::course_has_name():
    assert hasattr(Program::Course, "name")
    descriptor = None
    for klass in Program::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_program::semestercourse_is_not_abstract():
    assert not inspect.isabstract(Program::SemesterCourse)


def test_program::semestercourse_constructor_exists():
    assert callable(Program::SemesterCourse.__init__)


def test_program::semestercourse_constructor_args():
    sig = inspect.signature(Program::SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_program::semestercourse_has_status():
    assert hasattr(Program::SemesterCourse, "status")
    descriptor = None
    for klass in Program::SemesterCourse.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_program::semester_is_not_abstract():
    assert not inspect.isabstract(Program::Semester)


def test_program::semester_constructor_exists():
    assert callable(Program::Semester.__init__)


def test_program::semester_constructor_args():
    sig = inspect.signature(Program::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_program::semester_has_status():
    assert hasattr(Program::Semester, "status")
    descriptor = None
    for klass in Program::Semester.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_program::semester_has_name():
    assert hasattr(Program::Semester, "name")
    descriptor = None
    for klass in Program::Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_program::semester_has_code():
    assert hasattr(Program::Semester, "code")
    descriptor = None
    for klass in Program::Semester.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_program::program_is_not_abstract():
    assert not inspect.isabstract(Program::Program)


def test_program::program_constructor_exists():
    assert callable(Program::Program.__init__)


def test_program::program_constructor_args():
    sig = inspect.signature(Program::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "year" in params, "Missing parameter 'year'"

def test_program::program_has_name():
    assert hasattr(Program::Program, "name")
    descriptor = None
    for klass in Program::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_program::program_has_year():
    assert hasattr(Program::Program, "year")
    descriptor = None
    for klass in Program::Program.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_program::specialization_is_not_abstract():
    assert not inspect.isabstract(Program::Specialization)


def test_program::specialization_constructor_exists():
    assert callable(Program::Specialization.__init__)


def test_program::specialization_constructor_args():
    sig = inspect.signature(Program::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_program::specialization_has_name():
    assert hasattr(Program::Specialization, "name")
    descriptor = None
    for klass in Program::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_coursestatus_exists():
    # Check that the Enumeration exists
    assert CourseStatus is not None

def test_coursestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseStatus]
    expected_literals = [
        "MANDATORY",
        "ELECTIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseStatus"

def test_semesterstatus_exists():
    # Check that the Enumeration exists
    assert SemesterStatus is not None

def test_semesterstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterStatus]
    expected_literals = [
        "FALL",
        "SPRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterStatus"


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
Program::Department_strategy = st.builds(
    Program::Department,
    name=
        safe_text
)
Program::Course_strategy = st.builds(
    Program::Course,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    name=
        safe_text
)
Program::SemesterCourse_strategy = st.builds(
    Program::SemesterCourse,
    status=
        safe_text
)
Program::Semester_strategy = st.builds(
    Program::Semester,
    status=
        safe_text,
    name=
        safe_text,
    code=
        safe_text
)
Program::Program_strategy = st.builds(
    Program::Program,
    name=
        safe_text,
    year=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Program::Specialization_strategy = st.builds(
    Program::Specialization,
    name=
        safe_text
)

@given(instance=Program::Department_strategy)
@settings(max_examples=50)
def test_program::department_instantiation(instance):
    assert isinstance(instance, Program::Department)

@given(instance=Program::Department_strategy)
def test_program::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Program::Department_strategy)
def test_program::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Program::Course_strategy)
@settings(max_examples=50)
def test_program::course_instantiation(instance):
    assert isinstance(instance, Program::Course)

@given(instance=Program::Course_strategy)
def test_program::course_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=Program::Course_strategy)
def test_program::course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=Program::Course_strategy)
def test_program::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=Program::Course_strategy)
def test_program::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=Program::Course_strategy)
def test_program::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Program::Course_strategy)
def test_program::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Program::SemesterCourse_strategy)
@settings(max_examples=50)
def test_program::semestercourse_instantiation(instance):
    assert isinstance(instance, Program::SemesterCourse)

@given(instance=Program::SemesterCourse_strategy)
def test_program::semestercourse_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=Program::SemesterCourse_strategy)
def test_program::semestercourse_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Program::Semester_strategy)
@settings(max_examples=50)
def test_program::semester_instantiation(instance):
    assert isinstance(instance, Program::Semester)

@given(instance=Program::Semester_strategy)
def test_program::semester_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=Program::Semester_strategy)
def test_program::semester_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Program::Semester_strategy)
def test_program::semester_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Program::Semester_strategy)
def test_program::semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Program::Semester_strategy)
def test_program::semester_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=Program::Semester_strategy)
def test_program::semester_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=Program::Program_strategy)
@settings(max_examples=50)
def test_program::program_instantiation(instance):
    assert isinstance(instance, Program::Program)

@given(instance=Program::Program_strategy)
def test_program::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Program::Program_strategy)
def test_program::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Program::Program_strategy)
def test_program::program_year_type(instance):
    assert isinstance(instance.year, float)


@given(instance=Program::Program_strategy)
def test_program::program_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=Program::Specialization_strategy)
@settings(max_examples=50)
def test_program::specialization_instantiation(instance):
    assert isinstance(instance, Program::Specialization)

@given(instance=Program::Specialization_strategy)
def test_program::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Program::Specialization_strategy)
def test_program::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

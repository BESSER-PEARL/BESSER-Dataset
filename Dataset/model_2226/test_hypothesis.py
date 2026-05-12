import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Program_Department,
    Program_Course,
    Program_SemesterCourse,
    Program_Semester,
    Program_Program,
    Program_Specialization,
    SemesterStatus,
    CourseStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_program_department_is_not_abstract():
    assert not inspect.isabstract(Program_Department)


def test_program_department_constructor_exists():
    assert callable(Program_Department.__init__)


def test_program_department_constructor_args():
    sig = inspect.signature(Program_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_program_department_has_name():
    assert hasattr(Program_Department, "name")
    descriptor = None
    for klass in Program_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_program_course_is_not_abstract():
    assert not inspect.isabstract(Program_Course)


def test_program_course_constructor_exists():
    assert callable(Program_Course.__init__)


def test_program_course_constructor_args():
    sig = inspect.signature(Program_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_program_course_has_credit():
    assert hasattr(Program_Course, "credit")
    descriptor = None
    for klass in Program_Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_program_course_has_code():
    assert hasattr(Program_Course, "code")
    descriptor = None
    for klass in Program_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_program_course_has_name():
    assert hasattr(Program_Course, "name")
    descriptor = None
    for klass in Program_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_program_semestercourse_is_not_abstract():
    assert not inspect.isabstract(Program_SemesterCourse)


def test_program_semestercourse_constructor_exists():
    assert callable(Program_SemesterCourse.__init__)


def test_program_semestercourse_constructor_args():
    sig = inspect.signature(Program_SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_program_semestercourse_has_status():
    assert hasattr(Program_SemesterCourse, "status")
    descriptor = None
    for klass in Program_SemesterCourse.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_program_semester_is_not_abstract():
    assert not inspect.isabstract(Program_Semester)


def test_program_semester_constructor_exists():
    assert callable(Program_Semester.__init__)


def test_program_semester_constructor_args():
    sig = inspect.signature(Program_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "status" in params, "Missing parameter 'status'"
    assert "code" in params, "Missing parameter 'code'"

def test_program_semester_has_name():
    assert hasattr(Program_Semester, "name")
    descriptor = None
    for klass in Program_Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_program_semester_has_status():
    assert hasattr(Program_Semester, "status")
    descriptor = None
    for klass in Program_Semester.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_program_semester_has_code():
    assert hasattr(Program_Semester, "code")
    descriptor = None
    for klass in Program_Semester.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_program_program_is_not_abstract():
    assert not inspect.isabstract(Program_Program)


def test_program_program_constructor_exists():
    assert callable(Program_Program.__init__)


def test_program_program_constructor_args():
    sig = inspect.signature(Program_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "year" in params, "Missing parameter 'year'"

def test_program_program_has_name():
    assert hasattr(Program_Program, "name")
    descriptor = None
    for klass in Program_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_program_program_has_year():
    assert hasattr(Program_Program, "year")
    descriptor = None
    for klass in Program_Program.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_program_specialization_is_not_abstract():
    assert not inspect.isabstract(Program_Specialization)


def test_program_specialization_constructor_exists():
    assert callable(Program_Specialization.__init__)


def test_program_specialization_constructor_args():
    sig = inspect.signature(Program_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_program_specialization_has_name():
    assert hasattr(Program_Specialization, "name")
    descriptor = None
    for klass in Program_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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
Program_Department_strategy = st.builds(
    Program_Department,
    name=
        safe_text
)
Program_Course_strategy = st.builds(
    Program_Course,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    name=
        safe_text
)
Program_SemesterCourse_strategy = st.builds(
    Program_SemesterCourse,
    status=
        safe_text
)
Program_Semester_strategy = st.builds(
    Program_Semester,
    name=
        safe_text,
    status=
        safe_text,
    code=
        safe_text
)
Program_Program_strategy = st.builds(
    Program_Program,
    name=
        safe_text,
    year=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Program_Specialization_strategy = st.builds(
    Program_Specialization,
    name=
        safe_text
)

@given(instance=Program_Department_strategy)
@settings(max_examples=50)
def test_program_department_instantiation(instance):
    assert isinstance(instance, Program_Department)



@given(instance=Program_Department_strategy)
def test_program_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Program_Course_strategy)
@settings(max_examples=50)
def test_program_course_instantiation(instance):
    assert isinstance(instance, Program_Course)



@given(instance=Program_Course_strategy)
def test_program_course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original



@given(instance=Program_Course_strategy)
def test_program_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Program_Course_strategy)
def test_program_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Program_SemesterCourse_strategy)
@settings(max_examples=50)
def test_program_semestercourse_instantiation(instance):
    assert isinstance(instance, Program_SemesterCourse)



@given(instance=Program_SemesterCourse_strategy)
def test_program_semestercourse_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Program_Semester_strategy)
@settings(max_examples=50)
def test_program_semester_instantiation(instance):
    assert isinstance(instance, Program_Semester)



@given(instance=Program_Semester_strategy)
def test_program_semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Program_Semester_strategy)
def test_program_semester_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Program_Semester_strategy)
def test_program_semester_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=Program_Program_strategy)
@settings(max_examples=50)
def test_program_program_instantiation(instance):
    assert isinstance(instance, Program_Program)



@given(instance=Program_Program_strategy)
def test_program_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Program_Program_strategy)
def test_program_program_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=Program_Specialization_strategy)
@settings(max_examples=50)
def test_program_specialization_instantiation(instance):
    assert isinstance(instance, Program_Specialization)



@given(instance=Program_Specialization_strategy)
def test_program_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

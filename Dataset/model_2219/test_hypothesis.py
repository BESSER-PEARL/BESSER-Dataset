import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyplan_Course,
    studyplan_SemesterCourse,
    studyplan_Program,
    studyplan_Department,
    studyplan_Specialization,
    studyplan_Semester,
    Season,
    CourseStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyplan_course_is_not_abstract():
    assert not inspect.isabstract(studyplan_Course)


def test_studyplan_course_constructor_exists():
    assert callable(studyplan_Course.__init__)


def test_studyplan_course_constructor_args():
    sig = inspect.signature(studyplan_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyplan_course_has_credits():
    assert hasattr(studyplan_Course, "credits")
    descriptor = None
    for klass in studyplan_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_name():
    assert hasattr(studyplan_Course, "name")
    descriptor = None
    for klass in studyplan_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_code():
    assert hasattr(studyplan_Course, "code")
    descriptor = None
    for klass in studyplan_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_semestercourse_is_not_abstract():
    assert not inspect.isabstract(studyplan_SemesterCourse)


def test_studyplan_semestercourse_constructor_exists():
    assert callable(studyplan_SemesterCourse.__init__)


def test_studyplan_semestercourse_constructor_args():
    sig = inspect.signature(studyplan_SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_studyplan_semestercourse_has_status():
    assert hasattr(studyplan_SemesterCourse, "status")
    descriptor = None
    for klass in studyplan_SemesterCourse.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_program_is_not_abstract():
    assert not inspect.isabstract(studyplan_Program)


def test_studyplan_program_constructor_exists():
    assert callable(studyplan_Program.__init__)


def test_studyplan_program_constructor_args():
    sig = inspect.signature(studyplan_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyplan_program_has_name():
    assert hasattr(studyplan_Program, "name")
    descriptor = None
    for klass in studyplan_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_program_has_code():
    assert hasattr(studyplan_Program, "code")
    descriptor = None
    for klass in studyplan_Program.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_department_is_not_abstract():
    assert not inspect.isabstract(studyplan_Department)


def test_studyplan_department_constructor_exists():
    assert callable(studyplan_Department.__init__)


def test_studyplan_department_constructor_args():
    sig = inspect.signature(studyplan_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan_department_has_name():
    assert hasattr(studyplan_Department, "name")
    descriptor = None
    for klass in studyplan_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_specialization_is_not_abstract():
    assert not inspect.isabstract(studyplan_Specialization)


def test_studyplan_specialization_constructor_exists():
    assert callable(studyplan_Specialization.__init__)


def test_studyplan_specialization_constructor_args():
    sig = inspect.signature(studyplan_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan_specialization_has_name():
    assert hasattr(studyplan_Specialization, "name")
    descriptor = None
    for klass in studyplan_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_semester_is_not_abstract():
    assert not inspect.isabstract(studyplan_Semester)


def test_studyplan_semester_constructor_exists():
    assert callable(studyplan_Semester.__init__)


def test_studyplan_semester_constructor_args():
    sig = inspect.signature(studyplan_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "season" in params, "Missing parameter 'season'"
    assert "name" in params, "Missing parameter 'name'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyplan_semester_has_season():
    assert hasattr(studyplan_Semester, "season")
    descriptor = None
    for klass in studyplan_Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_semester_has_name():
    assert hasattr(studyplan_Semester, "name")
    descriptor = None
    for klass in studyplan_Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_semester_has_year():
    assert hasattr(studyplan_Semester, "year")
    descriptor = None
    for klass in studyplan_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_season_exists():
    # Check that the Enumeration exists
    assert Season is not None

def test_season_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Season]
    expected_literals = [
        "FALL",
        "SPRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Season"

def test_coursestatus_exists():
    # Check that the Enumeration exists
    assert CourseStatus is not None

def test_coursestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseStatus]
    expected_literals = [
        "ELECTIVE",
        "MANDATORY",
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
studyplan_Course_strategy = st.builds(
    studyplan_Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text
)
studyplan_SemesterCourse_strategy = st.builds(
    studyplan_SemesterCourse,
    status=
        safe_text
)
studyplan_Program_strategy = st.builds(
    studyplan_Program,
    name=
        safe_text,
    code=
        safe_text
)
studyplan_Department_strategy = st.builds(
    studyplan_Department,
    name=
        safe_text
)
studyplan_Specialization_strategy = st.builds(
    studyplan_Specialization,
    name=
        safe_text
)
studyplan_Semester_strategy = st.builds(
    studyplan_Semester,
    season=
        safe_text,
    name=
        safe_text,
    year=
        st.integers()
)

@given(instance=studyplan_Course_strategy)
@settings(max_examples=50)
def test_studyplan_course_instantiation(instance):
    assert isinstance(instance, studyplan_Course)



@given(instance=studyplan_Course_strategy)
def test_studyplan_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=studyplan_Course_strategy)
def test_studyplan_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyplan_Course_strategy)
def test_studyplan_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyplan_SemesterCourse_strategy)
@settings(max_examples=50)
def test_studyplan_semestercourse_instantiation(instance):
    assert isinstance(instance, studyplan_SemesterCourse)



@given(instance=studyplan_SemesterCourse_strategy)
def test_studyplan_semestercourse_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=studyplan_Program_strategy)
@settings(max_examples=50)
def test_studyplan_program_instantiation(instance):
    assert isinstance(instance, studyplan_Program)



@given(instance=studyplan_Program_strategy)
def test_studyplan_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyplan_Program_strategy)
def test_studyplan_program_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyplan_Department_strategy)
@settings(max_examples=50)
def test_studyplan_department_instantiation(instance):
    assert isinstance(instance, studyplan_Department)



@given(instance=studyplan_Department_strategy)
def test_studyplan_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyplan_Specialization_strategy)
@settings(max_examples=50)
def test_studyplan_specialization_instantiation(instance):
    assert isinstance(instance, studyplan_Specialization)



@given(instance=studyplan_Specialization_strategy)
def test_studyplan_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyplan_Semester_strategy)
@settings(max_examples=50)
def test_studyplan_semester_instantiation(instance):
    assert isinstance(instance, studyplan_Semester)



@given(instance=studyplan_Semester_strategy)
def test_studyplan_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original



@given(instance=studyplan_Semester_strategy)
def test_studyplan_semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyplan_Semester_strategy)
def test_studyplan_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

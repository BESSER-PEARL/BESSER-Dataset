import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyplan::Course,
    studyplan::SemesterCourse,
    studyplan::Department,
    studyplan::Specialization,
    studyplan::Semester,
    studyplan::Program,
    Season,
    CourseStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyplan::course_is_not_abstract():
    assert not inspect.isabstract(studyplan::Course)


def test_studyplan::course_constructor_exists():
    assert callable(studyplan::Course.__init__)


def test_studyplan::course_constructor_args():
    sig = inspect.signature(studyplan::Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan::course_has_credits():
    assert hasattr(studyplan::Course, "credits")
    descriptor = None
    for klass in studyplan::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_code():
    assert hasattr(studyplan::Course, "code")
    descriptor = None
    for klass in studyplan::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_name():
    assert hasattr(studyplan::Course, "name")
    descriptor = None
    for klass in studyplan::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::semestercourse_is_not_abstract():
    assert not inspect.isabstract(studyplan::SemesterCourse)


def test_studyplan::semestercourse_constructor_exists():
    assert callable(studyplan::SemesterCourse.__init__)


def test_studyplan::semestercourse_constructor_args():
    sig = inspect.signature(studyplan::SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_studyplan::semestercourse_has_status():
    assert hasattr(studyplan::SemesterCourse, "status")
    descriptor = None
    for klass in studyplan::SemesterCourse.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::department_is_not_abstract():
    assert not inspect.isabstract(studyplan::Department)


def test_studyplan::department_constructor_exists():
    assert callable(studyplan::Department.__init__)


def test_studyplan::department_constructor_args():
    sig = inspect.signature(studyplan::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan::department_has_name():
    assert hasattr(studyplan::Department, "name")
    descriptor = None
    for klass in studyplan::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::specialization_is_not_abstract():
    assert not inspect.isabstract(studyplan::Specialization)


def test_studyplan::specialization_constructor_exists():
    assert callable(studyplan::Specialization.__init__)


def test_studyplan::specialization_constructor_args():
    sig = inspect.signature(studyplan::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyplan::specialization_has_name():
    assert hasattr(studyplan::Specialization, "name")
    descriptor = None
    for klass in studyplan::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::semester_is_not_abstract():
    assert not inspect.isabstract(studyplan::Semester)


def test_studyplan::semester_constructor_exists():
    assert callable(studyplan::Semester.__init__)


def test_studyplan::semester_constructor_args():
    sig = inspect.signature(studyplan::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "season" in params, "Missing parameter 'season'"
    assert "name" in params, "Missing parameter 'name'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyplan::semester_has_season():
    assert hasattr(studyplan::Semester, "season")
    descriptor = None
    for klass in studyplan::Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::semester_has_name():
    assert hasattr(studyplan::Semester, "name")
    descriptor = None
    for klass in studyplan::Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::semester_has_year():
    assert hasattr(studyplan::Semester, "year")
    descriptor = None
    for klass in studyplan::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::program_is_not_abstract():
    assert not inspect.isabstract(studyplan::Program)


def test_studyplan::program_constructor_exists():
    assert callable(studyplan::Program.__init__)


def test_studyplan::program_constructor_args():
    sig = inspect.signature(studyplan::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyplan::program_has_name():
    assert hasattr(studyplan::Program, "name")
    descriptor = None
    for klass in studyplan::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::program_has_code():
    assert hasattr(studyplan::Program, "code")
    descriptor = None
    for klass in studyplan::Program.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
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
studyplan::Course_strategy = st.builds(
    studyplan::Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    name=
        safe_text
)
studyplan::SemesterCourse_strategy = st.builds(
    studyplan::SemesterCourse,
    status=
        safe_text
)
studyplan::Department_strategy = st.builds(
    studyplan::Department,
    name=
        safe_text
)
studyplan::Specialization_strategy = st.builds(
    studyplan::Specialization,
    name=
        safe_text
)
studyplan::Semester_strategy = st.builds(
    studyplan::Semester,
    season=
        safe_text,
    name=
        safe_text,
    year=
        st.integers()
)
studyplan::Program_strategy = st.builds(
    studyplan::Program,
    name=
        safe_text,
    code=
        safe_text
)

@given(instance=studyplan::Course_strategy)
@settings(max_examples=50)
def test_studyplan::course_instantiation(instance):
    assert isinstance(instance, studyplan::Course)

@given(instance=studyplan::Course_strategy)
def test_studyplan::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=studyplan::Course_strategy)
def test_studyplan::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=studyplan::Course_strategy)
def test_studyplan::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studyplan::Course_strategy)
def test_studyplan::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyplan::Course_strategy)
def test_studyplan::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyplan::Course_strategy)
def test_studyplan::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyplan::SemesterCourse_strategy)
@settings(max_examples=50)
def test_studyplan::semestercourse_instantiation(instance):
    assert isinstance(instance, studyplan::SemesterCourse)

@given(instance=studyplan::SemesterCourse_strategy)
def test_studyplan::semestercourse_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=studyplan::SemesterCourse_strategy)
def test_studyplan::semestercourse_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=studyplan::Department_strategy)
@settings(max_examples=50)
def test_studyplan::department_instantiation(instance):
    assert isinstance(instance, studyplan::Department)

@given(instance=studyplan::Department_strategy)
def test_studyplan::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyplan::Department_strategy)
def test_studyplan::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyplan::Specialization_strategy)
@settings(max_examples=50)
def test_studyplan::specialization_instantiation(instance):
    assert isinstance(instance, studyplan::Specialization)

@given(instance=studyplan::Specialization_strategy)
def test_studyplan::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyplan::Specialization_strategy)
def test_studyplan::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyplan::Semester_strategy)
@settings(max_examples=50)
def test_studyplan::semester_instantiation(instance):
    assert isinstance(instance, studyplan::Semester)

@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_season_type(instance):
    assert isinstance(instance.season, str)


@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyplan::Program_strategy)
@settings(max_examples=50)
def test_studyplan::program_instantiation(instance):
    assert isinstance(instance, studyplan::Program)

@given(instance=studyplan::Program_strategy)
def test_studyplan::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyplan::Program_strategy)
def test_studyplan::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyplan::Program_strategy)
def test_studyplan::program_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studyplan::Program_strategy)
def test_studyplan::program_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

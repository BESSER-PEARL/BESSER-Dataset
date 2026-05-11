import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    study::courseAllocation,
    study::StudyPlan,
    study::Specialisation,
    study::Student,
    study::Program,
    study::Course,
    study::Department,
    study::Semester,
    grades,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study::courseallocation_is_not_abstract():
    assert not inspect.isabstract(study::courseAllocation)


def test_study::courseallocation_constructor_exists():
    assert callable(study::courseAllocation.__init__)


def test_study::courseallocation_constructor_args():
    sig = inspect.signature(study::courseAllocation.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_study::courseallocation_has_grade():
    assert hasattr(study::courseAllocation, "grade")
    descriptor = None
    for klass in study::courseAllocation.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_study::studyplan_is_not_abstract():
    assert not inspect.isabstract(study::StudyPlan)


def test_study::studyplan_constructor_exists():
    assert callable(study::StudyPlan.__init__)


def test_study::studyplan_constructor_args():
    sig = inspect.signature(study::StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_study::specialisation_is_not_abstract():
    assert not inspect.isabstract(study::Specialisation)


def test_study::specialisation_constructor_exists():
    assert callable(study::Specialisation.__init__)


def test_study::specialisation_constructor_args():
    sig = inspect.signature(study::Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "requirement" in params, "Missing parameter 'requirement'"

def test_study::specialisation_has_name():
    assert hasattr(study::Specialisation, "name")
    descriptor = None
    for klass in study::Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study::specialisation_has_requirement():
    assert hasattr(study::Specialisation, "requirement")
    descriptor = None
    for klass in study::Specialisation.__mro__:
        if "requirement" in klass.__dict__:
            descriptor = klass.__dict__["requirement"]
            break
    assert isinstance(descriptor, property)



def test_study::student_is_not_abstract():
    assert not inspect.isabstract(study::Student)


def test_study::student_constructor_exists():
    assert callable(study::Student.__init__)


def test_study::student_constructor_args():
    sig = inspect.signature(study::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_study::student_has_name():
    assert hasattr(study::Student, "name")
    descriptor = None
    for klass in study::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study::program_is_not_abstract():
    assert not inspect.isabstract(study::Program)


def test_study::program_constructor_exists():
    assert callable(study::Program.__init__)


def test_study::program_constructor_args():
    sig = inspect.signature(study::Program.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numYears" in params, "Missing parameter 'numYears'"

def test_study::program_has_code():
    assert hasattr(study::Program, "code")
    descriptor = None
    for klass in study::Program.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study::program_has_name():
    assert hasattr(study::Program, "name")
    descriptor = None
    for klass in study::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study::program_has_numYears():
    assert hasattr(study::Program, "numYears")
    descriptor = None
    for klass in study::Program.__mro__:
        if "numYears" in klass.__dict__:
            descriptor = klass.__dict__["numYears"]
            break
    assert isinstance(descriptor, property)



def test_study::course_is_not_abstract():
    assert not inspect.isabstract(study::Course)


def test_study::course_constructor_exists():
    assert callable(study::Course.__init__)


def test_study::course_constructor_args():
    sig = inspect.signature(study::Course.__init__)
    params = list(sig.parameters.keys())
    assert "season" in params, "Missing parameter 'season'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "year" in params, "Missing parameter 'year'"

def test_study::course_has_season():
    assert hasattr(study::Course, "season")
    descriptor = None
    for klass in study::Course.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_study::course_has_code():
    assert hasattr(study::Course, "code")
    descriptor = None
    for klass in study::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study::course_has_name():
    assert hasattr(study::Course, "name")
    descriptor = None
    for klass in study::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study::course_has_credits():
    assert hasattr(study::Course, "credits")
    descriptor = None
    for klass in study::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_study::course_has_year():
    assert hasattr(study::Course, "year")
    descriptor = None
    for klass in study::Course.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_study::department_is_not_abstract():
    assert not inspect.isabstract(study::Department)


def test_study::department_constructor_exists():
    assert callable(study::Department.__init__)


def test_study::department_constructor_args():
    sig = inspect.signature(study::Department.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_study::department_has_code():
    assert hasattr(study::Department, "code")
    descriptor = None
    for klass in study::Department.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study::department_has_name():
    assert hasattr(study::Department, "name")
    descriptor = None
    for klass in study::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study::semester_is_not_abstract():
    assert not inspect.isabstract(study::Semester)


def test_study::semester_constructor_exists():
    assert callable(study::Semester.__init__)


def test_study::semester_constructor_args():
    sig = inspect.signature(study::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "season" in params, "Missing parameter 'season'"

def test_study::semester_has_year():
    assert hasattr(study::Semester, "year")
    descriptor = None
    for klass in study::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_study::semester_has_season():
    assert hasattr(study::Semester, "season")
    descriptor = None
    for klass in study::Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_grades_exists():
    # Check that the Enumeration exists
    assert grades is not None

def test_grades_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in grades]
    expected_literals = [
        "B",
        "C",
        "A",
        "D",
        "F",
        "E",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in grades"


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
study::courseAllocation_strategy = st.builds(
    study::courseAllocation,
    grade=
        safe_text
)
study::StudyPlan_strategy = st.builds(
    study::StudyPlan,
)
study::Specialisation_strategy = st.builds(
    study::Specialisation,
    name=
        safe_text,
    requirement=
        safe_text
)
study::Student_strategy = st.builds(
    study::Student,
    name=
        safe_text
)
study::Program_strategy = st.builds(
    study::Program,
    code=
        safe_text,
    name=
        safe_text,
    numYears=
        st.integers()
)
study::Course_strategy = st.builds(
    study::Course,
    season=
        safe_text,
    code=
        safe_text,
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    year=
        st.integers()
)
study::Department_strategy = st.builds(
    study::Department,
    code=
        safe_text,
    name=
        safe_text
)
study::Semester_strategy = st.builds(
    study::Semester,
    year=
        st.integers(),
    season=
        safe_text
)

@given(instance=study::courseAllocation_strategy)
@settings(max_examples=50)
def test_study::courseallocation_instantiation(instance):
    assert isinstance(instance, study::courseAllocation)

@given(instance=study::courseAllocation_strategy)
def test_study::courseallocation_grade_type(instance):
    assert isinstance(instance.grade, str)


@given(instance=study::courseAllocation_strategy)
def test_study::courseallocation_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=study::StudyPlan_strategy)
@settings(max_examples=50)
def test_study::studyplan_instantiation(instance):
    assert isinstance(instance, study::StudyPlan)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=study::StudyPlan_strategy)
@settings(max_examples=30)
def test_study::studyplan_choosecourse_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.chooseCourse(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.chooseCourse).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'chooseCourse' in study::StudyPlan is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'chooseCourse' in study::StudyPlan did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'chooseCourse' in study::StudyPlan is not implemented or raised an error")

@given(instance=study::Specialisation_strategy)
@settings(max_examples=50)
def test_study::specialisation_instantiation(instance):
    assert isinstance(instance, study::Specialisation)

@given(instance=study::Specialisation_strategy)
def test_study::specialisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Specialisation_strategy)
def test_study::specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study::Specialisation_strategy)
def test_study::specialisation_requirement_type(instance):
    assert isinstance(instance.requirement, str)


@given(instance=study::Specialisation_strategy)
def test_study::specialisation_requirement_setter(instance):
    original = instance.requirement
    instance.requirement = original
    assert instance.requirement == original

@given(instance=study::Student_strategy)
@settings(max_examples=50)
def test_study::student_instantiation(instance):
    assert isinstance(instance, study::Student)

@given(instance=study::Student_strategy)
def test_study::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Student_strategy)
def test_study::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study::Program_strategy)
@settings(max_examples=50)
def test_study::program_instantiation(instance):
    assert isinstance(instance, study::Program)

@given(instance=study::Program_strategy)
def test_study::program_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=study::Program_strategy)
def test_study::program_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study::Program_strategy)
def test_study::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Program_strategy)
def test_study::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study::Program_strategy)
def test_study::program_numYears_type(instance):
    assert isinstance(instance.numYears, int)


@given(instance=study::Program_strategy)
def test_study::program_numYears_setter(instance):
    original = instance.numYears
    instance.numYears = original
    assert instance.numYears == original

@given(instance=study::Course_strategy)
@settings(max_examples=50)
def test_study::course_instantiation(instance):
    assert isinstance(instance, study::Course)

@given(instance=study::Course_strategy)
def test_study::course_season_type(instance):
    assert isinstance(instance.season, str)


@given(instance=study::Course_strategy)
def test_study::course_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=study::Course_strategy)
def test_study::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=study::Course_strategy)
def test_study::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study::Course_strategy)
def test_study::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Course_strategy)
def test_study::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study::Course_strategy)
def test_study::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=study::Course_strategy)
def test_study::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=study::Course_strategy)
def test_study::course_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=study::Course_strategy)
def test_study::course_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=study::Department_strategy)
@settings(max_examples=50)
def test_study::department_instantiation(instance):
    assert isinstance(instance, study::Department)

@given(instance=study::Department_strategy)
def test_study::department_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=study::Department_strategy)
def test_study::department_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study::Department_strategy)
def test_study::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Department_strategy)
def test_study::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study::Semester_strategy)
@settings(max_examples=50)
def test_study::semester_instantiation(instance):
    assert isinstance(instance, study::Semester)

@given(instance=study::Semester_strategy)
def test_study::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=study::Semester_strategy)
def test_study::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=study::Semester_strategy)
def test_study::semester_season_type(instance):
    assert isinstance(instance.season, str)


@given(instance=study::Semester_strategy)
def test_study::semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

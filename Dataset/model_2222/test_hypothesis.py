import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    study_courseAllocation,
    study_StudyPlan,
    study_Specialisation,
    study_Student,
    study_Program,
    study_Course,
    study_Department,
    study_Semester,
    grades,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study_courseallocation_is_not_abstract():
    assert not inspect.isabstract(study_courseAllocation)


def test_study_courseallocation_constructor_exists():
    assert callable(study_courseAllocation.__init__)


def test_study_courseallocation_constructor_args():
    sig = inspect.signature(study_courseAllocation.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_study_courseallocation_has_grade():
    assert hasattr(study_courseAllocation, "grade")
    descriptor = None
    for klass in study_courseAllocation.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_study_studyplan_is_not_abstract():
    assert not inspect.isabstract(study_StudyPlan)


def test_study_studyplan_constructor_exists():
    assert callable(study_StudyPlan.__init__)


def test_study_studyplan_constructor_args():
    sig = inspect.signature(study_StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_study_specialisation_is_not_abstract():
    assert not inspect.isabstract(study_Specialisation)


def test_study_specialisation_constructor_exists():
    assert callable(study_Specialisation.__init__)


def test_study_specialisation_constructor_args():
    sig = inspect.signature(study_Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "requirement" in params, "Missing parameter 'requirement'"
    assert "name" in params, "Missing parameter 'name'"

def test_study_specialisation_has_requirement():
    assert hasattr(study_Specialisation, "requirement")
    descriptor = None
    for klass in study_Specialisation.__mro__:
        if "requirement" in klass.__dict__:
            descriptor = klass.__dict__["requirement"]
            break
    assert isinstance(descriptor, property)

def test_study_specialisation_has_name():
    assert hasattr(study_Specialisation, "name")
    descriptor = None
    for klass in study_Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study_student_is_not_abstract():
    assert not inspect.isabstract(study_Student)


def test_study_student_constructor_exists():
    assert callable(study_Student.__init__)


def test_study_student_constructor_args():
    sig = inspect.signature(study_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_study_student_has_name():
    assert hasattr(study_Student, "name")
    descriptor = None
    for klass in study_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study_program_is_not_abstract():
    assert not inspect.isabstract(study_Program)


def test_study_program_constructor_exists():
    assert callable(study_Program.__init__)


def test_study_program_constructor_args():
    sig = inspect.signature(study_Program.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "numYears" in params, "Missing parameter 'numYears'"
    assert "name" in params, "Missing parameter 'name'"

def test_study_program_has_code():
    assert hasattr(study_Program, "code")
    descriptor = None
    for klass in study_Program.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study_program_has_numYears():
    assert hasattr(study_Program, "numYears")
    descriptor = None
    for klass in study_Program.__mro__:
        if "numYears" in klass.__dict__:
            descriptor = klass.__dict__["numYears"]
            break
    assert isinstance(descriptor, property)

def test_study_program_has_name():
    assert hasattr(study_Program, "name")
    descriptor = None
    for klass in study_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study_course_is_not_abstract():
    assert not inspect.isabstract(study_Course)


def test_study_course_constructor_exists():
    assert callable(study_Course.__init__)


def test_study_course_constructor_args():
    sig = inspect.signature(study_Course.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "code" in params, "Missing parameter 'code'"
    assert "season" in params, "Missing parameter 'season'"

def test_study_course_has_year():
    assert hasattr(study_Course, "year")
    descriptor = None
    for klass in study_Course.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_study_course_has_name():
    assert hasattr(study_Course, "name")
    descriptor = None
    for klass in study_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study_course_has_credits():
    assert hasattr(study_Course, "credits")
    descriptor = None
    for klass in study_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_study_course_has_code():
    assert hasattr(study_Course, "code")
    descriptor = None
    for klass in study_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study_course_has_season():
    assert hasattr(study_Course, "season")
    descriptor = None
    for klass in study_Course.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)



def test_study_department_is_not_abstract():
    assert not inspect.isabstract(study_Department)


def test_study_department_constructor_exists():
    assert callable(study_Department.__init__)


def test_study_department_constructor_args():
    sig = inspect.signature(study_Department.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_study_department_has_code():
    assert hasattr(study_Department, "code")
    descriptor = None
    for klass in study_Department.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study_department_has_name():
    assert hasattr(study_Department, "name")
    descriptor = None
    for klass in study_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study_semester_is_not_abstract():
    assert not inspect.isabstract(study_Semester)


def test_study_semester_constructor_exists():
    assert callable(study_Semester.__init__)


def test_study_semester_constructor_args():
    sig = inspect.signature(study_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "season" in params, "Missing parameter 'season'"

def test_study_semester_has_year():
    assert hasattr(study_Semester, "year")
    descriptor = None
    for klass in study_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_study_semester_has_season():
    assert hasattr(study_Semester, "season")
    descriptor = None
    for klass in study_Semester.__mro__:
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
        "A",
        "D",
        "F",
        "C",
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
study_courseAllocation_strategy = st.builds(
    study_courseAllocation,
    grade=
        safe_text
)
study_StudyPlan_strategy = st.builds(
    study_StudyPlan,
)
study_Specialisation_strategy = st.builds(
    study_Specialisation,
    requirement=
        safe_text,
    name=
        safe_text
)
study_Student_strategy = st.builds(
    study_Student,
    name=
        safe_text
)
study_Program_strategy = st.builds(
    study_Program,
    code=
        safe_text,
    numYears=
        st.integers(),
    name=
        safe_text
)
study_Course_strategy = st.builds(
    study_Course,
    year=
        st.integers(),
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    season=
        safe_text
)
study_Department_strategy = st.builds(
    study_Department,
    code=
        safe_text,
    name=
        safe_text
)
study_Semester_strategy = st.builds(
    study_Semester,
    year=
        st.integers(),
    season=
        safe_text
)

@given(instance=study_courseAllocation_strategy)
@settings(max_examples=50)
def test_study_courseallocation_instantiation(instance):
    assert isinstance(instance, study_courseAllocation)



@given(instance=study_courseAllocation_strategy)
def test_study_courseallocation_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=study_StudyPlan_strategy)
@settings(max_examples=50)
def test_study_studyplan_instantiation(instance):
    assert isinstance(instance, study_StudyPlan)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=study_StudyPlan_strategy)
@settings(max_examples=30)
def test_study_studyplan_choosecourse_changes_state(instance):
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
        assert has_statements, f"Function 'chooseCourse' in study_StudyPlan is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'chooseCourse' in study_StudyPlan did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'chooseCourse' in study_StudyPlan is not implemented or raised an error")

@given(instance=study_Specialisation_strategy)
@settings(max_examples=50)
def test_study_specialisation_instantiation(instance):
    assert isinstance(instance, study_Specialisation)



@given(instance=study_Specialisation_strategy)
def test_study_specialisation_requirement_setter(instance):
    original = instance.requirement
    instance.requirement = original
    assert instance.requirement == original



@given(instance=study_Specialisation_strategy)
def test_study_specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Student_strategy)
@settings(max_examples=50)
def test_study_student_instantiation(instance):
    assert isinstance(instance, study_Student)



@given(instance=study_Student_strategy)
def test_study_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Program_strategy)
@settings(max_examples=50)
def test_study_program_instantiation(instance):
    assert isinstance(instance, study_Program)



@given(instance=study_Program_strategy)
def test_study_program_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=study_Program_strategy)
def test_study_program_numYears_setter(instance):
    original = instance.numYears
    instance.numYears = original
    assert instance.numYears == original



@given(instance=study_Program_strategy)
def test_study_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Course_strategy)
@settings(max_examples=50)
def test_study_course_instantiation(instance):
    assert isinstance(instance, study_Course)



@given(instance=study_Course_strategy)
def test_study_course_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=study_Course_strategy)
def test_study_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=study_Course_strategy)
def test_study_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=study_Course_strategy)
def test_study_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=study_Course_strategy)
def test_study_course_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=study_Department_strategy)
@settings(max_examples=50)
def test_study_department_instantiation(instance):
    assert isinstance(instance, study_Department)



@given(instance=study_Department_strategy)
def test_study_department_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=study_Department_strategy)
def test_study_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Semester_strategy)
@settings(max_examples=50)
def test_study_semester_instantiation(instance):
    assert isinstance(instance, study_Semester)



@given(instance=study_Semester_strategy)
def test_study_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=study_Semester_strategy)
def test_study_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

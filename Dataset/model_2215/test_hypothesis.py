import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyProgramStructure::CourseGroup,
    studyProgramStructure::CourseAllocation,
    studyProgramStructure::StudyPlan,
    studyProgramStructure::Student,
    studyProgramStructure::University,
    studyProgramStructure::Semester,
    studyProgramStructure::Specialization,
    studyProgramStructure::Course,
    studyProgramStructure::Program,
    Grade,
    Season,
    CourseStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogramstructure::coursegroup_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::CourseGroup)


def test_studyprogramstructure::coursegroup_constructor_exists():
    assert callable(studyProgramStructure::CourseGroup.__init__)


def test_studyprogramstructure::coursegroup_constructor_args():
    sig = inspect.signature(studyProgramStructure::CourseGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "status" in params, "Missing parameter 'status'"

def test_studyprogramstructure::coursegroup_has_name():
    assert hasattr(studyProgramStructure::CourseGroup, "name")
    descriptor = None
    for klass in studyProgramStructure::CourseGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::coursegroup_has_status():
    assert hasattr(studyProgramStructure::CourseGroup, "status")
    descriptor = None
    for klass in studyProgramStructure::CourseGroup.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure::courseallocation_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::CourseAllocation)


def test_studyprogramstructure::courseallocation_constructor_exists():
    assert callable(studyProgramStructure::CourseAllocation.__init__)


def test_studyprogramstructure::courseallocation_constructor_args():
    sig = inspect.signature(studyProgramStructure::CourseAllocation.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_studyprogramstructure::courseallocation_has_grade():
    assert hasattr(studyProgramStructure::CourseAllocation, "grade")
    descriptor = None
    for klass in studyProgramStructure::CourseAllocation.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure::studyplan_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::StudyPlan)


def test_studyprogramstructure::studyplan_constructor_exists():
    assert callable(studyProgramStructure::StudyPlan.__init__)


def test_studyprogramstructure::studyplan_constructor_args():
    sig = inspect.signature(studyProgramStructure::StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramstructure::student_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::Student)


def test_studyprogramstructure::student_constructor_exists():
    assert callable(studyProgramStructure::Student.__init__)


def test_studyprogramstructure::student_constructor_args():
    sig = inspect.signature(studyProgramStructure::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure::student_has_name():
    assert hasattr(studyProgramStructure::Student, "name")
    descriptor = None
    for klass in studyProgramStructure::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure::university_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::University)


def test_studyprogramstructure::university_constructor_exists():
    assert callable(studyProgramStructure::University.__init__)


def test_studyprogramstructure::university_constructor_args():
    sig = inspect.signature(studyProgramStructure::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure::university_has_name():
    assert hasattr(studyProgramStructure::University, "name")
    descriptor = None
    for klass in studyProgramStructure::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure::semester_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::Semester)


def test_studyprogramstructure::semester_constructor_exists():
    assert callable(studyProgramStructure::Semester.__init__)


def test_studyprogramstructure::semester_constructor_args():
    sig = inspect.signature(studyProgramStructure::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "season" in params, "Missing parameter 'season'"

def test_studyprogramstructure::semester_has_year():
    assert hasattr(studyProgramStructure::Semester, "year")
    descriptor = None
    for klass in studyProgramStructure::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::semester_has_season():
    assert hasattr(studyProgramStructure::Semester, "season")
    descriptor = None
    for klass in studyProgramStructure::Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure::specialization_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::Specialization)


def test_studyprogramstructure::specialization_constructor_exists():
    assert callable(studyProgramStructure::Specialization.__init__)


def test_studyprogramstructure::specialization_constructor_args():
    sig = inspect.signature(studyProgramStructure::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "numOfSemesters" in params, "Missing parameter 'numOfSemesters'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure::specialization_has_numOfSemesters():
    assert hasattr(studyProgramStructure::Specialization, "numOfSemesters")
    descriptor = None
    for klass in studyProgramStructure::Specialization.__mro__:
        if "numOfSemesters" in klass.__dict__:
            descriptor = klass.__dict__["numOfSemesters"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::specialization_has_name():
    assert hasattr(studyProgramStructure::Specialization, "name")
    descriptor = None
    for klass in studyProgramStructure::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure::course_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::Course)


def test_studyprogramstructure::course_constructor_exists():
    assert callable(studyProgramStructure::Course.__init__)


def test_studyprogramstructure::course_constructor_args():
    sig = inspect.signature(studyProgramStructure::Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyprogramstructure::course_has_level():
    assert hasattr(studyProgramStructure::Course, "level")
    descriptor = None
    for klass in studyProgramStructure::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::course_has_credits():
    assert hasattr(studyProgramStructure::Course, "credits")
    descriptor = None
    for klass in studyProgramStructure::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::course_has_name():
    assert hasattr(studyProgramStructure::Course, "name")
    descriptor = None
    for klass in studyProgramStructure::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::course_has_code():
    assert hasattr(studyProgramStructure::Course, "code")
    descriptor = None
    for klass in studyProgramStructure::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure::program_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure::Program)


def test_studyprogramstructure::program_constructor_exists():
    assert callable(studyProgramStructure::Program.__init__)


def test_studyprogramstructure::program_constructor_args():
    sig = inspect.signature(studyProgramStructure::Program.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "numOfSemestersForBaseSpecialization" in params, "Missing parameter 'numOfSemestersForBaseSpecialization'"
    assert "numOfYears" in params, "Missing parameter 'numOfYears'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure::program_has_code():
    assert hasattr(studyProgramStructure::Program, "code")
    descriptor = None
    for klass in studyProgramStructure::Program.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::program_has_numOfSemestersForBaseSpecialization():
    assert hasattr(studyProgramStructure::Program, "numOfSemestersForBaseSpecialization")
    descriptor = None
    for klass in studyProgramStructure::Program.__mro__:
        if "numOfSemestersForBaseSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["numOfSemestersForBaseSpecialization"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::program_has_numOfYears():
    assert hasattr(studyProgramStructure::Program, "numOfYears")
    descriptor = None
    for klass in studyProgramStructure::Program.__mro__:
        if "numOfYears" in klass.__dict__:
            descriptor = klass.__dict__["numOfYears"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure::program_has_name():
    assert hasattr(studyProgramStructure::Program, "name")
    descriptor = None
    for klass in studyProgramStructure::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_grade_exists():
    # Check that the Enumeration exists
    assert Grade is not None

def test_grade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Grade]
    expected_literals = [
        "F",
        "B",
        "A",
        "E",
        "D",
        "C",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Grade"

def test_season_exists():
    # Check that the Enumeration exists
    assert Season is not None

def test_season_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Season]
    expected_literals = [
        "fall",
        "spring",
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
        "elective",
        "mandatory",
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
studyProgramStructure::CourseGroup_strategy = st.builds(
    studyProgramStructure::CourseGroup,
    name=
        safe_text,
    status=
        safe_text
)
studyProgramStructure::CourseAllocation_strategy = st.builds(
    studyProgramStructure::CourseAllocation,
    grade=
        safe_text
)
studyProgramStructure::StudyPlan_strategy = st.builds(
    studyProgramStructure::StudyPlan,
)
studyProgramStructure::Student_strategy = st.builds(
    studyProgramStructure::Student,
    name=
        safe_text
)
studyProgramStructure::University_strategy = st.builds(
    studyProgramStructure::University,
    name=
        safe_text
)
studyProgramStructure::Semester_strategy = st.builds(
    studyProgramStructure::Semester,
    year=
        st.integers(),
    season=
        safe_text
)
studyProgramStructure::Specialization_strategy = st.builds(
    studyProgramStructure::Specialization,
    numOfSemesters=
        st.integers(),
    name=
        safe_text
)
studyProgramStructure::Course_strategy = st.builds(
    studyProgramStructure::Course,
    level=
        st.integers(),
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text
)
studyProgramStructure::Program_strategy = st.builds(
    studyProgramStructure::Program,
    code=
        safe_text,
    numOfSemestersForBaseSpecialization=
        st.integers(),
    numOfYears=
        st.integers(),
    name=
        safe_text
)

@given(instance=studyProgramStructure::CourseGroup_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::coursegroup_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::CourseGroup)

@given(instance=studyProgramStructure::CourseGroup_strategy)
def test_studyprogramstructure::coursegroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyProgramStructure::CourseGroup_strategy)
def test_studyprogramstructure::coursegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure::CourseGroup_strategy)
def test_studyprogramstructure::coursegroup_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=studyProgramStructure::CourseGroup_strategy)
def test_studyprogramstructure::coursegroup_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=studyProgramStructure::CourseAllocation_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::courseallocation_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::CourseAllocation)

@given(instance=studyProgramStructure::CourseAllocation_strategy)
def test_studyprogramstructure::courseallocation_grade_type(instance):
    assert isinstance(instance.grade, str)


@given(instance=studyProgramStructure::CourseAllocation_strategy)
def test_studyprogramstructure::courseallocation_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=studyProgramStructure::StudyPlan_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::studyplan_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::StudyPlan)

@given(instance=studyProgramStructure::Student_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::student_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::Student)

@given(instance=studyProgramStructure::Student_strategy)
def test_studyprogramstructure::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyProgramStructure::Student_strategy)
def test_studyprogramstructure::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure::University_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::university_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::University)

@given(instance=studyProgramStructure::University_strategy)
def test_studyprogramstructure::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyProgramStructure::University_strategy)
def test_studyprogramstructure::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure::Semester_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::semester_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::Semester)

@given(instance=studyProgramStructure::Semester_strategy)
def test_studyprogramstructure::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studyProgramStructure::Semester_strategy)
def test_studyprogramstructure::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyProgramStructure::Semester_strategy)
def test_studyprogramstructure::semester_season_type(instance):
    assert isinstance(instance.season, str)


@given(instance=studyProgramStructure::Semester_strategy)
def test_studyprogramstructure::semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=studyProgramStructure::Specialization_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::specialization_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::Specialization)

@given(instance=studyProgramStructure::Specialization_strategy)
def test_studyprogramstructure::specialization_numOfSemesters_type(instance):
    assert isinstance(instance.numOfSemesters, int)


@given(instance=studyProgramStructure::Specialization_strategy)
def test_studyprogramstructure::specialization_numOfSemesters_setter(instance):
    original = instance.numOfSemesters
    instance.numOfSemesters = original
    assert instance.numOfSemesters == original

@given(instance=studyProgramStructure::Specialization_strategy)
def test_studyprogramstructure::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyProgramStructure::Specialization_strategy)
def test_studyprogramstructure::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure::Course_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::course_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::Course)

@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studyProgramStructure::Course_strategy)
def test_studyprogramstructure::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyProgramStructure::Program_strategy)
@settings(max_examples=50)
def test_studyprogramstructure::program_instantiation(instance):
    assert isinstance(instance, studyProgramStructure::Program)

@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_numOfSemestersForBaseSpecialization_type(instance):
    assert isinstance(instance.numOfSemestersForBaseSpecialization, int)


@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_numOfSemestersForBaseSpecialization_setter(instance):
    original = instance.numOfSemestersForBaseSpecialization
    instance.numOfSemestersForBaseSpecialization = original
    assert instance.numOfSemestersForBaseSpecialization == original

@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_numOfYears_type(instance):
    assert isinstance(instance.numOfYears, int)


@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_numOfYears_setter(instance):
    original = instance.numOfYears
    instance.numOfYears = original
    assert instance.numOfYears == original

@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyProgramStructure::Program_strategy)
def test_studyprogramstructure::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyProgramStructure_CourseGroup,
    studyProgramStructure_CourseAllocation,
    studyProgramStructure_StudyPlan,
    studyProgramStructure_Student,
    studyProgramStructure_University,
    studyProgramStructure_Semester,
    studyProgramStructure_Specialization,
    studyProgramStructure_Course,
    studyProgramStructure_Program,
    CourseStatus,
    Season,
    Grade,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogramstructure_coursegroup_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_CourseGroup)


def test_studyprogramstructure_coursegroup_constructor_exists():
    assert callable(studyProgramStructure_CourseGroup.__init__)


def test_studyprogramstructure_coursegroup_constructor_args():
    sig = inspect.signature(studyProgramStructure_CourseGroup.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure_coursegroup_has_status():
    assert hasattr(studyProgramStructure_CourseGroup, "status")
    descriptor = None
    for klass in studyProgramStructure_CourseGroup.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_coursegroup_has_name():
    assert hasattr(studyProgramStructure_CourseGroup, "name")
    descriptor = None
    for klass in studyProgramStructure_CourseGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure_courseallocation_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_CourseAllocation)


def test_studyprogramstructure_courseallocation_constructor_exists():
    assert callable(studyProgramStructure_CourseAllocation.__init__)


def test_studyprogramstructure_courseallocation_constructor_args():
    sig = inspect.signature(studyProgramStructure_CourseAllocation.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_studyprogramstructure_courseallocation_has_grade():
    assert hasattr(studyProgramStructure_CourseAllocation, "grade")
    descriptor = None
    for klass in studyProgramStructure_CourseAllocation.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure_studyplan_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_StudyPlan)


def test_studyprogramstructure_studyplan_constructor_exists():
    assert callable(studyProgramStructure_StudyPlan.__init__)


def test_studyprogramstructure_studyplan_constructor_args():
    sig = inspect.signature(studyProgramStructure_StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramstructure_student_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Student)


def test_studyprogramstructure_student_constructor_exists():
    assert callable(studyProgramStructure_Student.__init__)


def test_studyprogramstructure_student_constructor_args():
    sig = inspect.signature(studyProgramStructure_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure_student_has_name():
    assert hasattr(studyProgramStructure_Student, "name")
    descriptor = None
    for klass in studyProgramStructure_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure_university_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_University)


def test_studyprogramstructure_university_constructor_exists():
    assert callable(studyProgramStructure_University.__init__)


def test_studyprogramstructure_university_constructor_args():
    sig = inspect.signature(studyProgramStructure_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure_university_has_name():
    assert hasattr(studyProgramStructure_University, "name")
    descriptor = None
    for klass in studyProgramStructure_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure_semester_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Semester)


def test_studyprogramstructure_semester_constructor_exists():
    assert callable(studyProgramStructure_Semester.__init__)


def test_studyprogramstructure_semester_constructor_args():
    sig = inspect.signature(studyProgramStructure_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "season" in params, "Missing parameter 'season'"

def test_studyprogramstructure_semester_has_year():
    assert hasattr(studyProgramStructure_Semester, "year")
    descriptor = None
    for klass in studyProgramStructure_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_semester_has_season():
    assert hasattr(studyProgramStructure_Semester, "season")
    descriptor = None
    for klass in studyProgramStructure_Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure_specialization_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Specialization)


def test_studyprogramstructure_specialization_constructor_exists():
    assert callable(studyProgramStructure_Specialization.__init__)


def test_studyprogramstructure_specialization_constructor_args():
    sig = inspect.signature(studyProgramStructure_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "numOfSemesters" in params, "Missing parameter 'numOfSemesters'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure_specialization_has_numOfSemesters():
    assert hasattr(studyProgramStructure_Specialization, "numOfSemesters")
    descriptor = None
    for klass in studyProgramStructure_Specialization.__mro__:
        if "numOfSemesters" in klass.__dict__:
            descriptor = klass.__dict__["numOfSemesters"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_specialization_has_name():
    assert hasattr(studyProgramStructure_Specialization, "name")
    descriptor = None
    for klass in studyProgramStructure_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure_course_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Course)


def test_studyprogramstructure_course_constructor_exists():
    assert callable(studyProgramStructure_Course.__init__)


def test_studyprogramstructure_course_constructor_args():
    sig = inspect.signature(studyProgramStructure_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "code" in params, "Missing parameter 'code'"
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramstructure_course_has_credits():
    assert hasattr(studyProgramStructure_Course, "credits")
    descriptor = None
    for klass in studyProgramStructure_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_course_has_code():
    assert hasattr(studyProgramStructure_Course, "code")
    descriptor = None
    for klass in studyProgramStructure_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_course_has_level():
    assert hasattr(studyProgramStructure_Course, "level")
    descriptor = None
    for klass in studyProgramStructure_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_course_has_name():
    assert hasattr(studyProgramStructure_Course, "name")
    descriptor = None
    for klass in studyProgramStructure_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramstructure_program_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Program)


def test_studyprogramstructure_program_constructor_exists():
    assert callable(studyProgramStructure_Program.__init__)


def test_studyprogramstructure_program_constructor_args():
    sig = inspect.signature(studyProgramStructure_Program.__init__)
    params = list(sig.parameters.keys())
    assert "numOfYears" in params, "Missing parameter 'numOfYears'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numOfSemestersForBaseSpecialization" in params, "Missing parameter 'numOfSemestersForBaseSpecialization'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyprogramstructure_program_has_numOfYears():
    assert hasattr(studyProgramStructure_Program, "numOfYears")
    descriptor = None
    for klass in studyProgramStructure_Program.__mro__:
        if "numOfYears" in klass.__dict__:
            descriptor = klass.__dict__["numOfYears"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_program_has_name():
    assert hasattr(studyProgramStructure_Program, "name")
    descriptor = None
    for klass in studyProgramStructure_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_program_has_numOfSemestersForBaseSpecialization():
    assert hasattr(studyProgramStructure_Program, "numOfSemestersForBaseSpecialization")
    descriptor = None
    for klass in studyProgramStructure_Program.__mro__:
        if "numOfSemestersForBaseSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["numOfSemestersForBaseSpecialization"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramstructure_program_has_code():
    assert hasattr(studyProgramStructure_Program, "code")
    descriptor = None
    for klass in studyProgramStructure_Program.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_coursestatus_exists():
    # Check that the Enumeration exists
    assert CourseStatus is not None

def test_coursestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseStatus]
    expected_literals = [
        "mandatory",
        "elective",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseStatus"

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

def test_grade_exists():
    # Check that the Enumeration exists
    assert Grade is not None

def test_grade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Grade]
    expected_literals = [
        "E",
        "A",
        "D",
        "F",
        "C",
        "B",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Grade"


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
studyProgramStructure_CourseGroup_strategy = st.builds(
    studyProgramStructure_CourseGroup,
    status=
        safe_text,
    name=
        safe_text
)
studyProgramStructure_CourseAllocation_strategy = st.builds(
    studyProgramStructure_CourseAllocation,
    grade=
        safe_text
)
studyProgramStructure_StudyPlan_strategy = st.builds(
    studyProgramStructure_StudyPlan,
)
studyProgramStructure_Student_strategy = st.builds(
    studyProgramStructure_Student,
    name=
        safe_text
)
studyProgramStructure_University_strategy = st.builds(
    studyProgramStructure_University,
    name=
        safe_text
)
studyProgramStructure_Semester_strategy = st.builds(
    studyProgramStructure_Semester,
    year=
        st.integers(),
    season=
        safe_text
)
studyProgramStructure_Specialization_strategy = st.builds(
    studyProgramStructure_Specialization,
    numOfSemesters=
        st.integers(),
    name=
        safe_text
)
studyProgramStructure_Course_strategy = st.builds(
    studyProgramStructure_Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    level=
        st.integers(),
    name=
        safe_text
)
studyProgramStructure_Program_strategy = st.builds(
    studyProgramStructure_Program,
    numOfYears=
        st.integers(),
    name=
        safe_text,
    numOfSemestersForBaseSpecialization=
        st.integers(),
    code=
        safe_text
)

@given(instance=studyProgramStructure_CourseGroup_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_coursegroup_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_CourseGroup)



@given(instance=studyProgramStructure_CourseGroup_strategy)
def test_studyprogramstructure_coursegroup_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=studyProgramStructure_CourseGroup_strategy)
def test_studyprogramstructure_coursegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure_CourseAllocation_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_courseallocation_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_CourseAllocation)



@given(instance=studyProgramStructure_CourseAllocation_strategy)
def test_studyprogramstructure_courseallocation_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=studyProgramStructure_StudyPlan_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_studyplan_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_StudyPlan)

@given(instance=studyProgramStructure_Student_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_student_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Student)



@given(instance=studyProgramStructure_Student_strategy)
def test_studyprogramstructure_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure_University_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_university_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_University)



@given(instance=studyProgramStructure_University_strategy)
def test_studyprogramstructure_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure_Semester_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_semester_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Semester)



@given(instance=studyProgramStructure_Semester_strategy)
def test_studyprogramstructure_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=studyProgramStructure_Semester_strategy)
def test_studyprogramstructure_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=studyProgramStructure_Specialization_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_specialization_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Specialization)



@given(instance=studyProgramStructure_Specialization_strategy)
def test_studyprogramstructure_specialization_numOfSemesters_setter(instance):
    original = instance.numOfSemesters
    instance.numOfSemesters = original
    assert instance.numOfSemesters == original



@given(instance=studyProgramStructure_Specialization_strategy)
def test_studyprogramstructure_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure_Course_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_course_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Course)



@given(instance=studyProgramStructure_Course_strategy)
def test_studyprogramstructure_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=studyProgramStructure_Course_strategy)
def test_studyprogramstructure_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=studyProgramStructure_Course_strategy)
def test_studyprogramstructure_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=studyProgramStructure_Course_strategy)
def test_studyprogramstructure_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyProgramStructure_Program_strategy)
@settings(max_examples=50)
def test_studyprogramstructure_program_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Program)



@given(instance=studyProgramStructure_Program_strategy)
def test_studyprogramstructure_program_numOfYears_setter(instance):
    original = instance.numOfYears
    instance.numOfYears = original
    assert instance.numOfYears == original



@given(instance=studyProgramStructure_Program_strategy)
def test_studyprogramstructure_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyProgramStructure_Program_strategy)
def test_studyprogramstructure_program_numOfSemestersForBaseSpecialization_setter(instance):
    original = instance.numOfSemestersForBaseSpecialization
    instance.numOfSemestersForBaseSpecialization = original
    assert instance.numOfSemestersForBaseSpecialization == original



@given(instance=studyProgramStructure_Program_strategy)
def test_studyprogramstructure_program_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    study::ElectiveCourseList,
    study::Semester,
    study::Specialization,
    study::CourseRelationship,
    study::IndividualStudyPlan,
    study::University,
    study::Student,
    study::Course,
    study::StudyProgramme,
    GradeEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study::electivecourselist_is_not_abstract():
    assert not inspect.isabstract(study::ElectiveCourseList)


def test_study::electivecourselist_constructor_exists():
    assert callable(study::ElectiveCourseList.__init__)


def test_study::electivecourselist_constructor_args():
    sig = inspect.signature(study::ElectiveCourseList.__init__)
    params = list(sig.parameters.keys())



def test_study::semester_is_not_abstract():
    assert not inspect.isabstract(study::Semester)


def test_study::semester_constructor_exists():
    assert callable(study::Semester.__init__)


def test_study::semester_constructor_args():
    sig = inspect.signature(study::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_study::semester_has_ordinal():
    assert hasattr(study::Semester, "ordinal")
    descriptor = None
    for klass in study::Semester.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_study::specialization_is_not_abstract():
    assert not inspect.isabstract(study::Specialization)


def test_study::specialization_constructor_exists():
    assert callable(study::Specialization.__init__)


def test_study::specialization_constructor_args():
    sig = inspect.signature(study::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numYears" in params, "Missing parameter 'numYears'"

def test_study::specialization_has_name():
    assert hasattr(study::Specialization, "name")
    descriptor = None
    for klass in study::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study::specialization_has_numYears():
    assert hasattr(study::Specialization, "numYears")
    descriptor = None
    for klass in study::Specialization.__mro__:
        if "numYears" in klass.__dict__:
            descriptor = klass.__dict__["numYears"]
            break
    assert isinstance(descriptor, property)



def test_study::courserelationship_is_not_abstract():
    assert not inspect.isabstract(study::CourseRelationship)


def test_study::courserelationship_constructor_exists():
    assert callable(study::CourseRelationship.__init__)


def test_study::courserelationship_constructor_args():
    sig = inspect.signature(study::CourseRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"
    assert "numExamAttempts" in params, "Missing parameter 'numExamAttempts'"

def test_study::courserelationship_has_grade():
    assert hasattr(study::CourseRelationship, "grade")
    descriptor = None
    for klass in study::CourseRelationship.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)

def test_study::courserelationship_has_numExamAttempts():
    assert hasattr(study::CourseRelationship, "numExamAttempts")
    descriptor = None
    for klass in study::CourseRelationship.__mro__:
        if "numExamAttempts" in klass.__dict__:
            descriptor = klass.__dict__["numExamAttempts"]
            break
    assert isinstance(descriptor, property)



def test_study::individualstudyplan_is_not_abstract():
    assert not inspect.isabstract(study::IndividualStudyPlan)


def test_study::individualstudyplan_constructor_exists():
    assert callable(study::IndividualStudyPlan.__init__)


def test_study::individualstudyplan_constructor_args():
    sig = inspect.signature(study::IndividualStudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_study::university_is_not_abstract():
    assert not inspect.isabstract(study::University)


def test_study::university_constructor_exists():
    assert callable(study::University.__init__)


def test_study::university_constructor_args():
    sig = inspect.signature(study::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_study::university_has_name():
    assert hasattr(study::University, "name")
    descriptor = None
    for klass in study::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
    assert "username" in params, "Missing parameter 'username'"

def test_study::student_has_name():
    assert hasattr(study::Student, "name")
    descriptor = None
    for klass in study::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study::student_has_username():
    assert hasattr(study::Student, "username")
    descriptor = None
    for klass in study::Student.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_study::course_is_not_abstract():
    assert not inspect.isabstract(study::Course)


def test_study::course_constructor_exists():
    assert callable(study::Course.__init__)


def test_study::course_constructor_args():
    sig = inspect.signature(study::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "level" in params, "Missing parameter 'level'"
    assert "code" in params, "Missing parameter 'code'"

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

def test_study::course_has_level():
    assert hasattr(study::Course, "level")
    descriptor = None
    for klass in study::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
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



def test_study::studyprogramme_is_not_abstract():
    assert not inspect.isabstract(study::StudyProgramme)


def test_study::studyprogramme_constructor_exists():
    assert callable(study::StudyProgramme.__init__)


def test_study::studyprogramme_constructor_args():
    sig = inspect.signature(study::StudyProgramme.__init__)
    params = list(sig.parameters.keys())
    assert "numYears" in params, "Missing parameter 'numYears'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_study::studyprogramme_has_numYears():
    assert hasattr(study::StudyProgramme, "numYears")
    descriptor = None
    for klass in study::StudyProgramme.__mro__:
        if "numYears" in klass.__dict__:
            descriptor = klass.__dict__["numYears"]
            break
    assert isinstance(descriptor, property)

def test_study::studyprogramme_has_code():
    assert hasattr(study::StudyProgramme, "code")
    descriptor = None
    for klass in study::StudyProgramme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study::studyprogramme_has_name():
    assert hasattr(study::StudyProgramme, "name")
    descriptor = None
    for klass in study::StudyProgramme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gradeenum_exists():
    # Check that the Enumeration exists
    assert GradeEnum is not None

def test_gradeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GradeEnum]
    expected_literals = [
        "A",
        "F",
        "B",
        "D",
        "C",
        "E",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GradeEnum"


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
study::ElectiveCourseList_strategy = st.builds(
    study::ElectiveCourseList,
)
study::Semester_strategy = st.builds(
    study::Semester,
    ordinal=
        st.integers()
)
study::Specialization_strategy = st.builds(
    study::Specialization,
    name=
        safe_text,
    numYears=
        st.integers()
)
study::CourseRelationship_strategy = st.builds(
    study::CourseRelationship,
    grade=
        safe_text,
    numExamAttempts=
        st.integers()
)
study::IndividualStudyPlan_strategy = st.builds(
    study::IndividualStudyPlan,
)
study::University_strategy = st.builds(
    study::University,
    name=
        safe_text
)
study::Student_strategy = st.builds(
    study::Student,
    name=
        safe_text,
    username=
        safe_text
)
study::Course_strategy = st.builds(
    study::Course,
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    level=
        st.integers(),
    code=
        safe_text
)
study::StudyProgramme_strategy = st.builds(
    study::StudyProgramme,
    numYears=
        st.integers(),
    code=
        safe_text,
    name=
        safe_text
)

@given(instance=study::ElectiveCourseList_strategy)
@settings(max_examples=50)
def test_study::electivecourselist_instantiation(instance):
    assert isinstance(instance, study::ElectiveCourseList)

@given(instance=study::Semester_strategy)
@settings(max_examples=50)
def test_study::semester_instantiation(instance):
    assert isinstance(instance, study::Semester)

@given(instance=study::Semester_strategy)
def test_study::semester_ordinal_type(instance):
    assert isinstance(instance.ordinal, int)


@given(instance=study::Semester_strategy)
def test_study::semester_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=study::Specialization_strategy)
@settings(max_examples=50)
def test_study::specialization_instantiation(instance):
    assert isinstance(instance, study::Specialization)

@given(instance=study::Specialization_strategy)
def test_study::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Specialization_strategy)
def test_study::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study::Specialization_strategy)
def test_study::specialization_numYears_type(instance):
    assert isinstance(instance.numYears, int)


@given(instance=study::Specialization_strategy)
def test_study::specialization_numYears_setter(instance):
    original = instance.numYears
    instance.numYears = original
    assert instance.numYears == original

@given(instance=study::CourseRelationship_strategy)
@settings(max_examples=50)
def test_study::courserelationship_instantiation(instance):
    assert isinstance(instance, study::CourseRelationship)

@given(instance=study::CourseRelationship_strategy)
def test_study::courserelationship_grade_type(instance):
    assert isinstance(instance.grade, str)


@given(instance=study::CourseRelationship_strategy)
def test_study::courserelationship_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=study::CourseRelationship_strategy)
def test_study::courserelationship_numExamAttempts_type(instance):
    assert isinstance(instance.numExamAttempts, int)


@given(instance=study::CourseRelationship_strategy)
def test_study::courserelationship_numExamAttempts_setter(instance):
    original = instance.numExamAttempts
    instance.numExamAttempts = original
    assert instance.numExamAttempts == original

@given(instance=study::IndividualStudyPlan_strategy)
@settings(max_examples=50)
def test_study::individualstudyplan_instantiation(instance):
    assert isinstance(instance, study::IndividualStudyPlan)

@given(instance=study::University_strategy)
@settings(max_examples=50)
def test_study::university_instantiation(instance):
    assert isinstance(instance, study::University)

@given(instance=study::University_strategy)
def test_study::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::University_strategy)
def test_study::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=study::Student_strategy)
def test_study::student_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=study::Student_strategy)
def test_study::student_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=study::Course_strategy)
@settings(max_examples=50)
def test_study::course_instantiation(instance):
    assert isinstance(instance, study::Course)

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
def test_study::course_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=study::Course_strategy)
def test_study::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=study::Course_strategy)
def test_study::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=study::Course_strategy)
def test_study::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study::StudyProgramme_strategy)
@settings(max_examples=50)
def test_study::studyprogramme_instantiation(instance):
    assert isinstance(instance, study::StudyProgramme)

@given(instance=study::StudyProgramme_strategy)
def test_study::studyprogramme_numYears_type(instance):
    assert isinstance(instance.numYears, int)


@given(instance=study::StudyProgramme_strategy)
def test_study::studyprogramme_numYears_setter(instance):
    original = instance.numYears
    instance.numYears = original
    assert instance.numYears == original

@given(instance=study::StudyProgramme_strategy)
def test_study::studyprogramme_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=study::StudyProgramme_strategy)
def test_study::studyprogramme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study::StudyProgramme_strategy)
def test_study::studyprogramme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::StudyProgramme_strategy)
def test_study::studyprogramme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

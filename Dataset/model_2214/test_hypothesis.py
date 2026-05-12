import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    study_ElectiveCourseList,
    study_Semester,
    study_Specialization,
    study_CourseRelationship,
    study_IndividualStudyPlan,
    study_University,
    study_Student,
    study_Course,
    study_StudyProgramme,
    GradeEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study_electivecourselist_is_not_abstract():
    assert not inspect.isabstract(study_ElectiveCourseList)


def test_study_electivecourselist_constructor_exists():
    assert callable(study_ElectiveCourseList.__init__)


def test_study_electivecourselist_constructor_args():
    sig = inspect.signature(study_ElectiveCourseList.__init__)
    params = list(sig.parameters.keys())



def test_study_semester_is_not_abstract():
    assert not inspect.isabstract(study_Semester)


def test_study_semester_constructor_exists():
    assert callable(study_Semester.__init__)


def test_study_semester_constructor_args():
    sig = inspect.signature(study_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "ordinal" in params, "Missing parameter 'ordinal'"

def test_study_semester_has_ordinal():
    assert hasattr(study_Semester, "ordinal")
    descriptor = None
    for klass in study_Semester.__mro__:
        if "ordinal" in klass.__dict__:
            descriptor = klass.__dict__["ordinal"]
            break
    assert isinstance(descriptor, property)



def test_study_specialization_is_not_abstract():
    assert not inspect.isabstract(study_Specialization)


def test_study_specialization_constructor_exists():
    assert callable(study_Specialization.__init__)


def test_study_specialization_constructor_args():
    sig = inspect.signature(study_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numYears" in params, "Missing parameter 'numYears'"

def test_study_specialization_has_name():
    assert hasattr(study_Specialization, "name")
    descriptor = None
    for klass in study_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study_specialization_has_numYears():
    assert hasattr(study_Specialization, "numYears")
    descriptor = None
    for klass in study_Specialization.__mro__:
        if "numYears" in klass.__dict__:
            descriptor = klass.__dict__["numYears"]
            break
    assert isinstance(descriptor, property)



def test_study_courserelationship_is_not_abstract():
    assert not inspect.isabstract(study_CourseRelationship)


def test_study_courserelationship_constructor_exists():
    assert callable(study_CourseRelationship.__init__)


def test_study_courserelationship_constructor_args():
    sig = inspect.signature(study_CourseRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"
    assert "numExamAttempts" in params, "Missing parameter 'numExamAttempts'"

def test_study_courserelationship_has_grade():
    assert hasattr(study_CourseRelationship, "grade")
    descriptor = None
    for klass in study_CourseRelationship.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)

def test_study_courserelationship_has_numExamAttempts():
    assert hasattr(study_CourseRelationship, "numExamAttempts")
    descriptor = None
    for klass in study_CourseRelationship.__mro__:
        if "numExamAttempts" in klass.__dict__:
            descriptor = klass.__dict__["numExamAttempts"]
            break
    assert isinstance(descriptor, property)



def test_study_individualstudyplan_is_not_abstract():
    assert not inspect.isabstract(study_IndividualStudyPlan)


def test_study_individualstudyplan_constructor_exists():
    assert callable(study_IndividualStudyPlan.__init__)


def test_study_individualstudyplan_constructor_args():
    sig = inspect.signature(study_IndividualStudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_study_university_is_not_abstract():
    assert not inspect.isabstract(study_University)


def test_study_university_constructor_exists():
    assert callable(study_University.__init__)


def test_study_university_constructor_args():
    sig = inspect.signature(study_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_study_university_has_name():
    assert hasattr(study_University, "name")
    descriptor = None
    for klass in study_University.__mro__:
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
    assert "username" in params, "Missing parameter 'username'"
    assert "name" in params, "Missing parameter 'name'"

def test_study_student_has_username():
    assert hasattr(study_Student, "username")
    descriptor = None
    for klass in study_Student.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_study_student_has_name():
    assert hasattr(study_Student, "name")
    descriptor = None
    for klass in study_Student.__mro__:
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
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "code" in params, "Missing parameter 'code'"

def test_study_course_has_level():
    assert hasattr(study_Course, "level")
    descriptor = None
    for klass in study_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
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



def test_study_studyprogramme_is_not_abstract():
    assert not inspect.isabstract(study_StudyProgramme)


def test_study_studyprogramme_constructor_exists():
    assert callable(study_StudyProgramme.__init__)


def test_study_studyprogramme_constructor_args():
    sig = inspect.signature(study_StudyProgramme.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "numYears" in params, "Missing parameter 'numYears'"
    assert "name" in params, "Missing parameter 'name'"

def test_study_studyprogramme_has_code():
    assert hasattr(study_StudyProgramme, "code")
    descriptor = None
    for klass in study_StudyProgramme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_study_studyprogramme_has_numYears():
    assert hasattr(study_StudyProgramme, "numYears")
    descriptor = None
    for klass in study_StudyProgramme.__mro__:
        if "numYears" in klass.__dict__:
            descriptor = klass.__dict__["numYears"]
            break
    assert isinstance(descriptor, property)

def test_study_studyprogramme_has_name():
    assert hasattr(study_StudyProgramme, "name")
    descriptor = None
    for klass in study_StudyProgramme.__mro__:
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
        "B",
        "A",
        "F",
        "E",
        "C",
        "D",
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
study_ElectiveCourseList_strategy = st.builds(
    study_ElectiveCourseList,
)
study_Semester_strategy = st.builds(
    study_Semester,
    ordinal=
        st.integers()
)
study_Specialization_strategy = st.builds(
    study_Specialization,
    name=
        safe_text,
    numYears=
        st.integers()
)
study_CourseRelationship_strategy = st.builds(
    study_CourseRelationship,
    grade=
        safe_text,
    numExamAttempts=
        st.integers()
)
study_IndividualStudyPlan_strategy = st.builds(
    study_IndividualStudyPlan,
)
study_University_strategy = st.builds(
    study_University,
    name=
        safe_text
)
study_Student_strategy = st.builds(
    study_Student,
    username=
        safe_text,
    name=
        safe_text
)
study_Course_strategy = st.builds(
    study_Course,
    level=
        st.integers(),
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text
)
study_StudyProgramme_strategy = st.builds(
    study_StudyProgramme,
    code=
        safe_text,
    numYears=
        st.integers(),
    name=
        safe_text
)

@given(instance=study_ElectiveCourseList_strategy)
@settings(max_examples=50)
def test_study_electivecourselist_instantiation(instance):
    assert isinstance(instance, study_ElectiveCourseList)

@given(instance=study_Semester_strategy)
@settings(max_examples=50)
def test_study_semester_instantiation(instance):
    assert isinstance(instance, study_Semester)



@given(instance=study_Semester_strategy)
def test_study_semester_ordinal_setter(instance):
    original = instance.ordinal
    instance.ordinal = original
    assert instance.ordinal == original

@given(instance=study_Specialization_strategy)
@settings(max_examples=50)
def test_study_specialization_instantiation(instance):
    assert isinstance(instance, study_Specialization)



@given(instance=study_Specialization_strategy)
def test_study_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=study_Specialization_strategy)
def test_study_specialization_numYears_setter(instance):
    original = instance.numYears
    instance.numYears = original
    assert instance.numYears == original

@given(instance=study_CourseRelationship_strategy)
@settings(max_examples=50)
def test_study_courserelationship_instantiation(instance):
    assert isinstance(instance, study_CourseRelationship)



@given(instance=study_CourseRelationship_strategy)
def test_study_courserelationship_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original



@given(instance=study_CourseRelationship_strategy)
def test_study_courserelationship_numExamAttempts_setter(instance):
    original = instance.numExamAttempts
    instance.numExamAttempts = original
    assert instance.numExamAttempts == original

@given(instance=study_IndividualStudyPlan_strategy)
@settings(max_examples=50)
def test_study_individualstudyplan_instantiation(instance):
    assert isinstance(instance, study_IndividualStudyPlan)

@given(instance=study_University_strategy)
@settings(max_examples=50)
def test_study_university_instantiation(instance):
    assert isinstance(instance, study_University)



@given(instance=study_University_strategy)
def test_study_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Student_strategy)
@settings(max_examples=50)
def test_study_student_instantiation(instance):
    assert isinstance(instance, study_Student)



@given(instance=study_Student_strategy)
def test_study_student_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=study_Student_strategy)
def test_study_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Course_strategy)
@settings(max_examples=50)
def test_study_course_instantiation(instance):
    assert isinstance(instance, study_Course)



@given(instance=study_Course_strategy)
def test_study_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



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

@given(instance=study_StudyProgramme_strategy)
@settings(max_examples=50)
def test_study_studyprogramme_instantiation(instance):
    assert isinstance(instance, study_StudyProgramme)



@given(instance=study_StudyProgramme_strategy)
def test_study_studyprogramme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=study_StudyProgramme_strategy)
def test_study_studyprogramme_numYears_setter(instance):
    original = instance.numYears
    instance.numYears = original
    assert instance.numYears == original



@given(instance=study_StudyProgramme_strategy)
def test_study_studyprogramme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    study_CourseSlot,
    study_Semester,
    study_Specialization,
    study_StudyPlan,
    study_Course,
    study_Programme,
    study_Department,
    programmeCode,
    FallOrSpring,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study_courseslot_is_not_abstract():
    assert not inspect.isabstract(study_CourseSlot)


def test_study_courseslot_constructor_exists():
    assert callable(study_CourseSlot.__init__)


def test_study_courseslot_constructor_args():
    sig = inspect.signature(study_CourseSlot.__init__)
    params = list(sig.parameters.keys())
    assert "elective" in params, "Missing parameter 'elective'"

def test_study_courseslot_has_elective():
    assert hasattr(study_CourseSlot, "elective")
    descriptor = None
    for klass in study_CourseSlot.__mro__:
        if "elective" in klass.__dict__:
            descriptor = klass.__dict__["elective"]
            break
    assert isinstance(descriptor, property)



def test_study_semester_is_not_abstract():
    assert not inspect.isabstract(study_Semester)


def test_study_semester_constructor_exists():
    assert callable(study_Semester.__init__)


def test_study_semester_constructor_args():
    sig = inspect.signature(study_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"
    assert "fallOrSpring" in params, "Missing parameter 'fallOrSpring'"

def test_study_semester_has_semesterNumber():
    assert hasattr(study_Semester, "semesterNumber")
    descriptor = None
    for klass in study_Semester.__mro__:
        if "semesterNumber" in klass.__dict__:
            descriptor = klass.__dict__["semesterNumber"]
            break
    assert isinstance(descriptor, property)

def test_study_semester_has_fallOrSpring():
    assert hasattr(study_Semester, "fallOrSpring")
    descriptor = None
    for klass in study_Semester.__mro__:
        if "fallOrSpring" in klass.__dict__:
            descriptor = klass.__dict__["fallOrSpring"]
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

def test_study_specialization_has_name():
    assert hasattr(study_Specialization, "name")
    descriptor = None
    for klass in study_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study_studyplan_is_not_abstract():
    assert not inspect.isabstract(study_StudyPlan)


def test_study_studyplan_constructor_exists():
    assert callable(study_StudyPlan.__init__)


def test_study_studyplan_constructor_args():
    sig = inspect.signature(study_StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_study_course_is_not_abstract():
    assert not inspect.isabstract(study_Course)


def test_study_course_constructor_exists():
    assert callable(study_Course.__init__)


def test_study_course_constructor_args():
    sig = inspect.signature(study_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "points" in params, "Missing parameter 'points'"
    assert "code" in params, "Missing parameter 'code'"

def test_study_course_has_name():
    assert hasattr(study_Course, "name")
    descriptor = None
    for klass in study_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study_course_has_points():
    assert hasattr(study_Course, "points")
    descriptor = None
    for klass in study_Course.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
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



def test_study_programme_is_not_abstract():
    assert not inspect.isabstract(study_Programme)


def test_study_programme_constructor_exists():
    assert callable(study_Programme.__init__)


def test_study_programme_constructor_args():
    sig = inspect.signature(study_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "programmeCode" in params, "Missing parameter 'programmeCode'"
    assert "name" in params, "Missing parameter 'name'"

def test_study_programme_has_programmeCode():
    assert hasattr(study_Programme, "programmeCode")
    descriptor = None
    for klass in study_Programme.__mro__:
        if "programmeCode" in klass.__dict__:
            descriptor = klass.__dict__["programmeCode"]
            break
    assert isinstance(descriptor, property)

def test_study_programme_has_name():
    assert hasattr(study_Programme, "name")
    descriptor = None
    for klass in study_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study_department_is_not_abstract():
    assert not inspect.isabstract(study_Department)


def test_study_department_constructor_exists():
    assert callable(study_Department.__init__)


def test_study_department_constructor_args():
    sig = inspect.signature(study_Department.__init__)
    params = list(sig.parameters.keys())

def test_programmecode_exists():
    # Check that the Enumeration exists
    assert programmeCode is not None

def test_programmecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in programmeCode]
    expected_literals = [
        "Datateknologi2",
        "Datateknologi5",
        "Informatikk",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in programmeCode"

def test_fallorspring_exists():
    # Check that the Enumeration exists
    assert FallOrSpring is not None

def test_fallorspring_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FallOrSpring]
    expected_literals = [
        "Spring",
        "Fall",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FallOrSpring"


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
study_CourseSlot_strategy = st.builds(
    study_CourseSlot,
    elective=
        st.booleans()
)
study_Semester_strategy = st.builds(
    study_Semester,
    semesterNumber=
        st.integers(),
    fallOrSpring=
        safe_text
)
study_Specialization_strategy = st.builds(
    study_Specialization,
    name=
        safe_text
)
study_StudyPlan_strategy = st.builds(
    study_StudyPlan,
)
study_Course_strategy = st.builds(
    study_Course,
    name=
        safe_text,
    points=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text
)
study_Programme_strategy = st.builds(
    study_Programme,
    programmeCode=
        safe_text,
    name=
        safe_text
)
study_Department_strategy = st.builds(
    study_Department,
)

@given(instance=study_CourseSlot_strategy)
@settings(max_examples=50)
def test_study_courseslot_instantiation(instance):
    assert isinstance(instance, study_CourseSlot)



@given(instance=study_CourseSlot_strategy)
def test_study_courseslot_elective_setter(instance):
    original = instance.elective
    instance.elective = original
    assert instance.elective == original

@given(instance=study_Semester_strategy)
@settings(max_examples=50)
def test_study_semester_instantiation(instance):
    assert isinstance(instance, study_Semester)



@given(instance=study_Semester_strategy)
def test_study_semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original



@given(instance=study_Semester_strategy)
def test_study_semester_fallOrSpring_setter(instance):
    original = instance.fallOrSpring
    instance.fallOrSpring = original
    assert instance.fallOrSpring == original

@given(instance=study_Specialization_strategy)
@settings(max_examples=50)
def test_study_specialization_instantiation(instance):
    assert isinstance(instance, study_Specialization)



@given(instance=study_Specialization_strategy)
def test_study_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_StudyPlan_strategy)
@settings(max_examples=50)
def test_study_studyplan_instantiation(instance):
    assert isinstance(instance, study_StudyPlan)

@given(instance=study_Course_strategy)
@settings(max_examples=50)
def test_study_course_instantiation(instance):
    assert isinstance(instance, study_Course)



@given(instance=study_Course_strategy)
def test_study_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=study_Course_strategy)
def test_study_course_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=study_Course_strategy)
def test_study_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study_Programme_strategy)
@settings(max_examples=50)
def test_study_programme_instantiation(instance):
    assert isinstance(instance, study_Programme)



@given(instance=study_Programme_strategy)
def test_study_programme_programmeCode_setter(instance):
    original = instance.programmeCode
    instance.programmeCode = original
    assert instance.programmeCode == original



@given(instance=study_Programme_strategy)
def test_study_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Department_strategy)
@settings(max_examples=50)
def test_study_department_instantiation(instance):
    assert isinstance(instance, study_Department)

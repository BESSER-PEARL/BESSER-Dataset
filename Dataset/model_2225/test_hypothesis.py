import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    study::CourseSlot,
    study::Semester,
    study::Specialization,
    study::StudyPlan,
    study::Course,
    study::Programme,
    study::Department,
    FallOrSpring,
    programmeCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study::courseslot_is_not_abstract():
    assert not inspect.isabstract(study::CourseSlot)


def test_study::courseslot_constructor_exists():
    assert callable(study::CourseSlot.__init__)


def test_study::courseslot_constructor_args():
    sig = inspect.signature(study::CourseSlot.__init__)
    params = list(sig.parameters.keys())
    assert "elective" in params, "Missing parameter 'elective'"

def test_study::courseslot_has_elective():
    assert hasattr(study::CourseSlot, "elective")
    descriptor = None
    for klass in study::CourseSlot.__mro__:
        if "elective" in klass.__dict__:
            descriptor = klass.__dict__["elective"]
            break
    assert isinstance(descriptor, property)



def test_study::semester_is_not_abstract():
    assert not inspect.isabstract(study::Semester)


def test_study::semester_constructor_exists():
    assert callable(study::Semester.__init__)


def test_study::semester_constructor_args():
    sig = inspect.signature(study::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "fallOrSpring" in params, "Missing parameter 'fallOrSpring'"
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"

def test_study::semester_has_fallOrSpring():
    assert hasattr(study::Semester, "fallOrSpring")
    descriptor = None
    for klass in study::Semester.__mro__:
        if "fallOrSpring" in klass.__dict__:
            descriptor = klass.__dict__["fallOrSpring"]
            break
    assert isinstance(descriptor, property)

def test_study::semester_has_semesterNumber():
    assert hasattr(study::Semester, "semesterNumber")
    descriptor = None
    for klass in study::Semester.__mro__:
        if "semesterNumber" in klass.__dict__:
            descriptor = klass.__dict__["semesterNumber"]
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

def test_study::specialization_has_name():
    assert hasattr(study::Specialization, "name")
    descriptor = None
    for klass in study::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_study::studyplan_is_not_abstract():
    assert not inspect.isabstract(study::StudyPlan)


def test_study::studyplan_constructor_exists():
    assert callable(study::StudyPlan.__init__)


def test_study::studyplan_constructor_args():
    sig = inspect.signature(study::StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_study::course_is_not_abstract():
    assert not inspect.isabstract(study::Course)


def test_study::course_constructor_exists():
    assert callable(study::Course.__init__)


def test_study::course_constructor_args():
    sig = inspect.signature(study::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "points" in params, "Missing parameter 'points'"

def test_study::course_has_name():
    assert hasattr(study::Course, "name")
    descriptor = None
    for klass in study::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_study::course_has_points():
    assert hasattr(study::Course, "points")
    descriptor = None
    for klass in study::Course.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_study::programme_is_not_abstract():
    assert not inspect.isabstract(study::Programme)


def test_study::programme_constructor_exists():
    assert callable(study::Programme.__init__)


def test_study::programme_constructor_args():
    sig = inspect.signature(study::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "programmeCode" in params, "Missing parameter 'programmeCode'"

def test_study::programme_has_name():
    assert hasattr(study::Programme, "name")
    descriptor = None
    for klass in study::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study::programme_has_programmeCode():
    assert hasattr(study::Programme, "programmeCode")
    descriptor = None
    for klass in study::Programme.__mro__:
        if "programmeCode" in klass.__dict__:
            descriptor = klass.__dict__["programmeCode"]
            break
    assert isinstance(descriptor, property)



def test_study::department_is_not_abstract():
    assert not inspect.isabstract(study::Department)


def test_study::department_constructor_exists():
    assert callable(study::Department.__init__)


def test_study::department_constructor_args():
    sig = inspect.signature(study::Department.__init__)
    params = list(sig.parameters.keys())

def test_fallorspring_exists():
    # Check that the Enumeration exists
    assert FallOrSpring is not None

def test_fallorspring_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FallOrSpring]
    expected_literals = [
        "Fall",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FallOrSpring"

def test_programmecode_exists():
    # Check that the Enumeration exists
    assert programmeCode is not None

def test_programmecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in programmeCode]
    expected_literals = [
        "Datateknologi5",
        "Informatikk",
        "Datateknologi2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in programmeCode"


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
study::CourseSlot_strategy = st.builds(
    study::CourseSlot,
    elective=
        st.booleans()
)
study::Semester_strategy = st.builds(
    study::Semester,
    fallOrSpring=
        safe_text,
    semesterNumber=
        st.integers()
)
study::Specialization_strategy = st.builds(
    study::Specialization,
    name=
        safe_text
)
study::StudyPlan_strategy = st.builds(
    study::StudyPlan,
)
study::Course_strategy = st.builds(
    study::Course,
    name=
        safe_text,
    code=
        safe_text,
    points=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
study::Programme_strategy = st.builds(
    study::Programme,
    name=
        safe_text,
    programmeCode=
        safe_text
)
study::Department_strategy = st.builds(
    study::Department,
)

@given(instance=study::CourseSlot_strategy)
@settings(max_examples=50)
def test_study::courseslot_instantiation(instance):
    assert isinstance(instance, study::CourseSlot)

@given(instance=study::CourseSlot_strategy)
def test_study::courseslot_elective_type(instance):
    assert isinstance(instance.elective, bool)


@given(instance=study::CourseSlot_strategy)
def test_study::courseslot_elective_setter(instance):
    original = instance.elective
    instance.elective = original
    assert instance.elective == original

@given(instance=study::Semester_strategy)
@settings(max_examples=50)
def test_study::semester_instantiation(instance):
    assert isinstance(instance, study::Semester)

@given(instance=study::Semester_strategy)
def test_study::semester_fallOrSpring_type(instance):
    assert isinstance(instance.fallOrSpring, str)


@given(instance=study::Semester_strategy)
def test_study::semester_fallOrSpring_setter(instance):
    original = instance.fallOrSpring
    instance.fallOrSpring = original
    assert instance.fallOrSpring == original

@given(instance=study::Semester_strategy)
def test_study::semester_semesterNumber_type(instance):
    assert isinstance(instance.semesterNumber, int)


@given(instance=study::Semester_strategy)
def test_study::semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original

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

@given(instance=study::StudyPlan_strategy)
@settings(max_examples=50)
def test_study::studyplan_instantiation(instance):
    assert isinstance(instance, study::StudyPlan)

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
def test_study::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=study::Course_strategy)
def test_study::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study::Course_strategy)
def test_study::course_points_type(instance):
    assert isinstance(instance.points, float)


@given(instance=study::Course_strategy)
def test_study::course_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=study::Programme_strategy)
@settings(max_examples=50)
def test_study::programme_instantiation(instance):
    assert isinstance(instance, study::Programme)

@given(instance=study::Programme_strategy)
def test_study::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Programme_strategy)
def test_study::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study::Programme_strategy)
def test_study::programme_programmeCode_type(instance):
    assert isinstance(instance.programmeCode, str)


@given(instance=study::Programme_strategy)
def test_study::programme_programmeCode_setter(instance):
    original = instance.programmeCode
    instance.programmeCode = original
    assert instance.programmeCode == original

@given(instance=study::Department_strategy)
@settings(max_examples=50)
def test_study::department_instantiation(instance):
    assert isinstance(instance, study::Department)

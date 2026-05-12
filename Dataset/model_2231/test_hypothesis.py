import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ra_MandatoryCourse,
    ra_Specialization,
    ra_StudyPlan,
    ra_Course,
    ra_Semester,
    ra_Programme,
    ra_Department,
    programmeCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ra_mandatorycourse_is_not_abstract():
    assert not inspect.isabstract(ra_MandatoryCourse)


def test_ra_mandatorycourse_constructor_exists():
    assert callable(ra_MandatoryCourse.__init__)


def test_ra_mandatorycourse_constructor_args():
    sig = inspect.signature(ra_MandatoryCourse.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "credit" in params, "Missing parameter 'credit'"

def test_ra_mandatorycourse_has_mandatory():
    assert hasattr(ra_MandatoryCourse, "mandatory")
    descriptor = None
    for klass in ra_MandatoryCourse.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_ra_mandatorycourse_has_credit():
    assert hasattr(ra_MandatoryCourse, "credit")
    descriptor = None
    for klass in ra_MandatoryCourse.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)



def test_ra_specialization_is_not_abstract():
    assert not inspect.isabstract(ra_Specialization)


def test_ra_specialization_constructor_exists():
    assert callable(ra_Specialization.__init__)


def test_ra_specialization_constructor_args():
    sig = inspect.signature(ra_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ra_specialization_has_name():
    assert hasattr(ra_Specialization, "name")
    descriptor = None
    for klass in ra_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ra_studyplan_is_not_abstract():
    assert not inspect.isabstract(ra_StudyPlan)


def test_ra_studyplan_constructor_exists():
    assert callable(ra_StudyPlan.__init__)


def test_ra_studyplan_constructor_args():
    sig = inspect.signature(ra_StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_ra_course_is_not_abstract():
    assert not inspect.isabstract(ra_Course)


def test_ra_course_constructor_exists():
    assert callable(ra_Course.__init__)


def test_ra_course_constructor_args():
    sig = inspect.signature(ra_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_ra_course_has_code():
    assert hasattr(ra_Course, "code")
    descriptor = None
    for klass in ra_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_ra_course_has_name():
    assert hasattr(ra_Course, "name")
    descriptor = None
    for klass in ra_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ra_semester_is_not_abstract():
    assert not inspect.isabstract(ra_Semester)


def test_ra_semester_constructor_exists():
    assert callable(ra_Semester.__init__)


def test_ra_semester_constructor_args():
    sig = inspect.signature(ra_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "totalPoints" in params, "Missing parameter 'totalPoints'"
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"

def test_ra_semester_has_totalPoints():
    assert hasattr(ra_Semester, "totalPoints")
    descriptor = None
    for klass in ra_Semester.__mro__:
        if "totalPoints" in klass.__dict__:
            descriptor = klass.__dict__["totalPoints"]
            break
    assert isinstance(descriptor, property)

def test_ra_semester_has_semesterNumber():
    assert hasattr(ra_Semester, "semesterNumber")
    descriptor = None
    for klass in ra_Semester.__mro__:
        if "semesterNumber" in klass.__dict__:
            descriptor = klass.__dict__["semesterNumber"]
            break
    assert isinstance(descriptor, property)



def test_ra_programme_is_not_abstract():
    assert not inspect.isabstract(ra_Programme)


def test_ra_programme_constructor_exists():
    assert callable(ra_Programme.__init__)


def test_ra_programme_constructor_args():
    sig = inspect.signature(ra_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mCode" in params, "Missing parameter 'mCode'"

def test_ra_programme_has_name():
    assert hasattr(ra_Programme, "name")
    descriptor = None
    for klass in ra_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ra_programme_has_mCode():
    assert hasattr(ra_Programme, "mCode")
    descriptor = None
    for klass in ra_Programme.__mro__:
        if "mCode" in klass.__dict__:
            descriptor = klass.__dict__["mCode"]
            break
    assert isinstance(descriptor, property)



def test_ra_department_is_not_abstract():
    assert not inspect.isabstract(ra_Department)


def test_ra_department_constructor_exists():
    assert callable(ra_Department.__init__)


def test_ra_department_constructor_args():
    sig = inspect.signature(ra_Department.__init__)
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
ra_MandatoryCourse_strategy = st.builds(
    ra_MandatoryCourse,
    mandatory=
        st.booleans(),
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ra_Specialization_strategy = st.builds(
    ra_Specialization,
    name=
        safe_text
)
ra_StudyPlan_strategy = st.builds(
    ra_StudyPlan,
)
ra_Course_strategy = st.builds(
    ra_Course,
    code=
        safe_text,
    name=
        safe_text
)
ra_Semester_strategy = st.builds(
    ra_Semester,
    totalPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    semesterNumber=
        st.integers()
)
ra_Programme_strategy = st.builds(
    ra_Programme,
    name=
        safe_text,
    mCode=
        safe_text
)
ra_Department_strategy = st.builds(
    ra_Department,
)

@given(instance=ra_MandatoryCourse_strategy)
@settings(max_examples=50)
def test_ra_mandatorycourse_instantiation(instance):
    assert isinstance(instance, ra_MandatoryCourse)



@given(instance=ra_MandatoryCourse_strategy)
def test_ra_mandatorycourse_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=ra_MandatoryCourse_strategy)
def test_ra_mandatorycourse_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=ra_Specialization_strategy)
@settings(max_examples=50)
def test_ra_specialization_instantiation(instance):
    assert isinstance(instance, ra_Specialization)



@given(instance=ra_Specialization_strategy)
def test_ra_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ra_StudyPlan_strategy)
@settings(max_examples=50)
def test_ra_studyplan_instantiation(instance):
    assert isinstance(instance, ra_StudyPlan)

@given(instance=ra_Course_strategy)
@settings(max_examples=50)
def test_ra_course_instantiation(instance):
    assert isinstance(instance, ra_Course)



@given(instance=ra_Course_strategy)
def test_ra_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=ra_Course_strategy)
def test_ra_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ra_Semester_strategy)
@settings(max_examples=50)
def test_ra_semester_instantiation(instance):
    assert isinstance(instance, ra_Semester)



@given(instance=ra_Semester_strategy)
def test_ra_semester_totalPoints_setter(instance):
    original = instance.totalPoints
    instance.totalPoints = original
    assert instance.totalPoints == original



@given(instance=ra_Semester_strategy)
def test_ra_semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original

@given(instance=ra_Programme_strategy)
@settings(max_examples=50)
def test_ra_programme_instantiation(instance):
    assert isinstance(instance, ra_Programme)



@given(instance=ra_Programme_strategy)
def test_ra_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ra_Programme_strategy)
def test_ra_programme_mCode_setter(instance):
    original = instance.mCode
    instance.mCode = original
    assert instance.mCode == original

@given(instance=ra_Department_strategy)
@settings(max_examples=50)
def test_ra_department_instantiation(instance):
    assert isinstance(instance, ra_Department)

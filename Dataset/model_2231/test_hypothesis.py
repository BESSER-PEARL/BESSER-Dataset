import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ra::MandatoryCourse,
    ra::Specialization,
    ra::StudyPlan,
    ra::Course,
    ra::Semester,
    ra::Programme,
    ra::Department,
    programmeCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ra::mandatorycourse_is_not_abstract():
    assert not inspect.isabstract(ra::MandatoryCourse)


def test_ra::mandatorycourse_constructor_exists():
    assert callable(ra::MandatoryCourse.__init__)


def test_ra::mandatorycourse_constructor_args():
    sig = inspect.signature(ra::MandatoryCourse.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_ra::mandatorycourse_has_credit():
    assert hasattr(ra::MandatoryCourse, "credit")
    descriptor = None
    for klass in ra::MandatoryCourse.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_ra::mandatorycourse_has_mandatory():
    assert hasattr(ra::MandatoryCourse, "mandatory")
    descriptor = None
    for klass in ra::MandatoryCourse.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_ra::specialization_is_not_abstract():
    assert not inspect.isabstract(ra::Specialization)


def test_ra::specialization_constructor_exists():
    assert callable(ra::Specialization.__init__)


def test_ra::specialization_constructor_args():
    sig = inspect.signature(ra::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ra::specialization_has_name():
    assert hasattr(ra::Specialization, "name")
    descriptor = None
    for klass in ra::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ra::studyplan_is_not_abstract():
    assert not inspect.isabstract(ra::StudyPlan)


def test_ra::studyplan_constructor_exists():
    assert callable(ra::StudyPlan.__init__)


def test_ra::studyplan_constructor_args():
    sig = inspect.signature(ra::StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_ra::course_is_not_abstract():
    assert not inspect.isabstract(ra::Course)


def test_ra::course_constructor_exists():
    assert callable(ra::Course.__init__)


def test_ra::course_constructor_args():
    sig = inspect.signature(ra::Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_ra::course_has_code():
    assert hasattr(ra::Course, "code")
    descriptor = None
    for klass in ra::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_ra::course_has_name():
    assert hasattr(ra::Course, "name")
    descriptor = None
    for klass in ra::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ra::semester_is_not_abstract():
    assert not inspect.isabstract(ra::Semester)


def test_ra::semester_constructor_exists():
    assert callable(ra::Semester.__init__)


def test_ra::semester_constructor_args():
    sig = inspect.signature(ra::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "totalPoints" in params, "Missing parameter 'totalPoints'"
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"

def test_ra::semester_has_totalPoints():
    assert hasattr(ra::Semester, "totalPoints")
    descriptor = None
    for klass in ra::Semester.__mro__:
        if "totalPoints" in klass.__dict__:
            descriptor = klass.__dict__["totalPoints"]
            break
    assert isinstance(descriptor, property)

def test_ra::semester_has_semesterNumber():
    assert hasattr(ra::Semester, "semesterNumber")
    descriptor = None
    for klass in ra::Semester.__mro__:
        if "semesterNumber" in klass.__dict__:
            descriptor = klass.__dict__["semesterNumber"]
            break
    assert isinstance(descriptor, property)



def test_ra::programme_is_not_abstract():
    assert not inspect.isabstract(ra::Programme)


def test_ra::programme_constructor_exists():
    assert callable(ra::Programme.__init__)


def test_ra::programme_constructor_args():
    sig = inspect.signature(ra::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mCode" in params, "Missing parameter 'mCode'"

def test_ra::programme_has_name():
    assert hasattr(ra::Programme, "name")
    descriptor = None
    for klass in ra::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ra::programme_has_mCode():
    assert hasattr(ra::Programme, "mCode")
    descriptor = None
    for klass in ra::Programme.__mro__:
        if "mCode" in klass.__dict__:
            descriptor = klass.__dict__["mCode"]
            break
    assert isinstance(descriptor, property)



def test_ra::department_is_not_abstract():
    assert not inspect.isabstract(ra::Department)


def test_ra::department_constructor_exists():
    assert callable(ra::Department.__init__)


def test_ra::department_constructor_args():
    sig = inspect.signature(ra::Department.__init__)
    params = list(sig.parameters.keys())

def test_programmecode_exists():
    # Check that the Enumeration exists
    assert programmeCode is not None

def test_programmecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in programmeCode]
    expected_literals = [
        "Informatikk",
        "Datateknologi2",
        "Datateknologi5",
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
ra::MandatoryCourse_strategy = st.builds(
    ra::MandatoryCourse,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mandatory=
        st.booleans()
)
ra::Specialization_strategy = st.builds(
    ra::Specialization,
    name=
        safe_text
)
ra::StudyPlan_strategy = st.builds(
    ra::StudyPlan,
)
ra::Course_strategy = st.builds(
    ra::Course,
    code=
        safe_text,
    name=
        safe_text
)
ra::Semester_strategy = st.builds(
    ra::Semester,
    totalPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    semesterNumber=
        st.integers()
)
ra::Programme_strategy = st.builds(
    ra::Programme,
    name=
        safe_text,
    mCode=
        safe_text
)
ra::Department_strategy = st.builds(
    ra::Department,
)

@given(instance=ra::MandatoryCourse_strategy)
@settings(max_examples=50)
def test_ra::mandatorycourse_instantiation(instance):
    assert isinstance(instance, ra::MandatoryCourse)

@given(instance=ra::MandatoryCourse_strategy)
def test_ra::mandatorycourse_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=ra::MandatoryCourse_strategy)
def test_ra::mandatorycourse_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=ra::MandatoryCourse_strategy)
def test_ra::mandatorycourse_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=ra::MandatoryCourse_strategy)
def test_ra::mandatorycourse_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=ra::Specialization_strategy)
@settings(max_examples=50)
def test_ra::specialization_instantiation(instance):
    assert isinstance(instance, ra::Specialization)

@given(instance=ra::Specialization_strategy)
def test_ra::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ra::Specialization_strategy)
def test_ra::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ra::StudyPlan_strategy)
@settings(max_examples=50)
def test_ra::studyplan_instantiation(instance):
    assert isinstance(instance, ra::StudyPlan)

@given(instance=ra::Course_strategy)
@settings(max_examples=50)
def test_ra::course_instantiation(instance):
    assert isinstance(instance, ra::Course)

@given(instance=ra::Course_strategy)
def test_ra::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=ra::Course_strategy)
def test_ra::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=ra::Course_strategy)
def test_ra::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ra::Course_strategy)
def test_ra::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ra::Semester_strategy)
@settings(max_examples=50)
def test_ra::semester_instantiation(instance):
    assert isinstance(instance, ra::Semester)

@given(instance=ra::Semester_strategy)
def test_ra::semester_totalPoints_type(instance):
    assert isinstance(instance.totalPoints, float)


@given(instance=ra::Semester_strategy)
def test_ra::semester_totalPoints_setter(instance):
    original = instance.totalPoints
    instance.totalPoints = original
    assert instance.totalPoints == original

@given(instance=ra::Semester_strategy)
def test_ra::semester_semesterNumber_type(instance):
    assert isinstance(instance.semesterNumber, int)


@given(instance=ra::Semester_strategy)
def test_ra::semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original

@given(instance=ra::Programme_strategy)
@settings(max_examples=50)
def test_ra::programme_instantiation(instance):
    assert isinstance(instance, ra::Programme)

@given(instance=ra::Programme_strategy)
def test_ra::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ra::Programme_strategy)
def test_ra::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ra::Programme_strategy)
def test_ra::programme_mCode_type(instance):
    assert isinstance(instance.mCode, str)


@given(instance=ra::Programme_strategy)
def test_ra::programme_mCode_setter(instance):
    original = instance.mCode
    instance.mCode = original
    assert instance.mCode == original

@given(instance=ra::Department_strategy)
@settings(max_examples=50)
def test_ra::department_instantiation(instance):
    assert isinstance(instance, ra::Department)

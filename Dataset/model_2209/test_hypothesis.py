import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    study::Course,
    study::SemesterCourse,
    study::Department,
    study::Specialization,
    study::Semester,
    study::Programme,
    Season,
    IsMandatory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study::course_is_not_abstract():
    assert not inspect.isabstract(study::Course)


def test_study::course_constructor_exists():
    assert callable(study::Course.__init__)


def test_study::course_constructor_args():
    sig = inspect.signature(study::Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "level" in params, "Missing parameter 'level'"

def test_study::course_has_credits():
    assert hasattr(study::Course, "credits")
    descriptor = None
    for klass in study::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
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

def test_study::course_has_level():
    assert hasattr(study::Course, "level")
    descriptor = None
    for klass in study::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_study::semestercourse_is_not_abstract():
    assert not inspect.isabstract(study::SemesterCourse)


def test_study::semestercourse_constructor_exists():
    assert callable(study::SemesterCourse.__init__)


def test_study::semestercourse_constructor_args():
    sig = inspect.signature(study::SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_study::semestercourse_has_mandatory():
    assert hasattr(study::SemesterCourse, "mandatory")
    descriptor = None
    for klass in study::SemesterCourse.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_study::department_is_not_abstract():
    assert not inspect.isabstract(study::Department)


def test_study::department_constructor_exists():
    assert callable(study::Department.__init__)


def test_study::department_constructor_args():
    sig = inspect.signature(study::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_study::department_has_name():
    assert hasattr(study::Department, "name")
    descriptor = None
    for klass in study::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_study::semester_is_not_abstract():
    assert not inspect.isabstract(study::Semester)


def test_study::semester_constructor_exists():
    assert callable(study::Semester.__init__)


def test_study::semester_constructor_args():
    sig = inspect.signature(study::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "Season" in params, "Missing parameter 'Season'"
    assert "year" in params, "Missing parameter 'year'"

def test_study::semester_has_Season():
    assert hasattr(study::Semester, "Season")
    descriptor = None
    for klass in study::Semester.__mro__:
        if "Season" in klass.__dict__:
            descriptor = klass.__dict__["Season"]
            break
    assert isinstance(descriptor, property)

def test_study::semester_has_year():
    assert hasattr(study::Semester, "year")
    descriptor = None
    for klass in study::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
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
    assert "duration" in params, "Missing parameter 'duration'"
    assert "code" in params, "Missing parameter 'code'"

def test_study::programme_has_name():
    assert hasattr(study::Programme, "name")
    descriptor = None
    for klass in study::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study::programme_has_duration():
    assert hasattr(study::Programme, "duration")
    descriptor = None
    for klass in study::Programme.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_study::programme_has_code():
    assert hasattr(study::Programme, "code")
    descriptor = None
    for klass in study::Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_season_exists():
    # Check that the Enumeration exists
    assert Season is not None

def test_season_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Season]
    expected_literals = [
        "FALL",
        "SPRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Season"

def test_ismandatory_exists():
    # Check that the Enumeration exists
    assert IsMandatory is not None

def test_ismandatory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IsMandatory]
    expected_literals = [
        "MANDATORY",
        "ELECTIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IsMandatory"


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
study::Course_strategy = st.builds(
    study::Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    name=
        safe_text,
    level=
        st.integers()
)
study::SemesterCourse_strategy = st.builds(
    study::SemesterCourse,
    mandatory=
        safe_text
)
study::Department_strategy = st.builds(
    study::Department,
    name=
        safe_text
)
study::Specialization_strategy = st.builds(
    study::Specialization,
    name=
        safe_text
)
study::Semester_strategy = st.builds(
    study::Semester,
    Season=
        safe_text,
    year=
        st.integers()
)
study::Programme_strategy = st.builds(
    study::Programme,
    name=
        safe_text,
    duration=
        st.integers(),
    code=
        safe_text
)

@given(instance=study::Course_strategy)
@settings(max_examples=50)
def test_study::course_instantiation(instance):
    assert isinstance(instance, study::Course)

@given(instance=study::Course_strategy)
def test_study::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=study::Course_strategy)
def test_study::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

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
def test_study::course_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=study::Course_strategy)
def test_study::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=study::SemesterCourse_strategy)
@settings(max_examples=50)
def test_study::semestercourse_instantiation(instance):
    assert isinstance(instance, study::SemesterCourse)

@given(instance=study::SemesterCourse_strategy)
def test_study::semestercourse_mandatory_type(instance):
    assert isinstance(instance.mandatory, str)


@given(instance=study::SemesterCourse_strategy)
def test_study::semestercourse_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=study::Department_strategy)
@settings(max_examples=50)
def test_study::department_instantiation(instance):
    assert isinstance(instance, study::Department)

@given(instance=study::Department_strategy)
def test_study::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=study::Department_strategy)
def test_study::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=study::Semester_strategy)
@settings(max_examples=50)
def test_study::semester_instantiation(instance):
    assert isinstance(instance, study::Semester)

@given(instance=study::Semester_strategy)
def test_study::semester_Season_type(instance):
    assert isinstance(instance.Season, str)


@given(instance=study::Semester_strategy)
def test_study::semester_Season_setter(instance):
    original = instance.Season
    instance.Season = original
    assert instance.Season == original

@given(instance=study::Semester_strategy)
def test_study::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=study::Semester_strategy)
def test_study::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

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
def test_study::programme_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=study::Programme_strategy)
def test_study::programme_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=study::Programme_strategy)
def test_study::programme_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=study::Programme_strategy)
def test_study::programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    study_Department,
    study_Specialization,
    study_Semester,
    study_Programme,
    study_Course,
    study_SemesterCourse,
    Season,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_study_department_is_not_abstract():
    assert not inspect.isabstract(study_Department)


def test_study_department_constructor_exists():
    assert callable(study_Department.__init__)


def test_study_department_constructor_args():
    sig = inspect.signature(study_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_study_department_has_name():
    assert hasattr(study_Department, "name")
    descriptor = None
    for klass in study_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_study_semester_is_not_abstract():
    assert not inspect.isabstract(study_Semester)


def test_study_semester_constructor_exists():
    assert callable(study_Semester.__init__)


def test_study_semester_constructor_args():
    sig = inspect.signature(study_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "Season" in params, "Missing parameter 'Season'"

def test_study_semester_has_year():
    assert hasattr(study_Semester, "year")
    descriptor = None
    for klass in study_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_study_semester_has_Season():
    assert hasattr(study_Semester, "Season")
    descriptor = None
    for klass in study_Semester.__mro__:
        if "Season" in klass.__dict__:
            descriptor = klass.__dict__["Season"]
            break
    assert isinstance(descriptor, property)



def test_study_programme_is_not_abstract():
    assert not inspect.isabstract(study_Programme)


def test_study_programme_constructor_exists():
    assert callable(study_Programme.__init__)


def test_study_programme_constructor_args():
    sig = inspect.signature(study_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "code" in params, "Missing parameter 'code'"

def test_study_programme_has_name():
    assert hasattr(study_Programme, "name")
    descriptor = None
    for klass in study_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study_programme_has_duration():
    assert hasattr(study_Programme, "duration")
    descriptor = None
    for klass in study_Programme.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_study_programme_has_code():
    assert hasattr(study_Programme, "code")
    descriptor = None
    for klass in study_Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_study_course_is_not_abstract():
    assert not inspect.isabstract(study_Course)


def test_study_course_constructor_exists():
    assert callable(study_Course.__init__)


def test_study_course_constructor_args():
    sig = inspect.signature(study_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "level" in params, "Missing parameter 'level'"

def test_study_course_has_code():
    assert hasattr(study_Course, "code")
    descriptor = None
    for klass in study_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
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

def test_study_course_has_name():
    assert hasattr(study_Course, "name")
    descriptor = None
    for klass in study_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_study_course_has_level():
    assert hasattr(study_Course, "level")
    descriptor = None
    for klass in study_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_study_semestercourse_is_not_abstract():
    assert not inspect.isabstract(study_SemesterCourse)


def test_study_semestercourse_constructor_exists():
    assert callable(study_SemesterCourse.__init__)


def test_study_semestercourse_constructor_args():
    sig = inspect.signature(study_SemesterCourse.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_study_semestercourse_has_mandatory():
    assert hasattr(study_SemesterCourse, "mandatory")
    descriptor = None
    for klass in study_SemesterCourse.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
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
study_Department_strategy = st.builds(
    study_Department,
    name=
        safe_text
)
study_Specialization_strategy = st.builds(
    study_Specialization,
    name=
        safe_text
)
study_Semester_strategy = st.builds(
    study_Semester,
    year=
        st.integers(),
    Season=
        safe_text
)
study_Programme_strategy = st.builds(
    study_Programme,
    name=
        safe_text,
    duration=
        st.integers(),
    code=
        safe_text
)
study_Course_strategy = st.builds(
    study_Course,
    code=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    level=
        st.integers()
)
study_SemesterCourse_strategy = st.builds(
    study_SemesterCourse,
    mandatory=
        st.booleans()
)

@given(instance=study_Department_strategy)
@settings(max_examples=50)
def test_study_department_instantiation(instance):
    assert isinstance(instance, study_Department)



@given(instance=study_Department_strategy)
def test_study_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=study_Specialization_strategy)
@settings(max_examples=50)
def test_study_specialization_instantiation(instance):
    assert isinstance(instance, study_Specialization)



@given(instance=study_Specialization_strategy)
def test_study_specialization_name_setter(instance):
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
def test_study_semester_Season_setter(instance):
    original = instance.Season
    instance.Season = original
    assert instance.Season == original

@given(instance=study_Programme_strategy)
@settings(max_examples=50)
def test_study_programme_instantiation(instance):
    assert isinstance(instance, study_Programme)



@given(instance=study_Programme_strategy)
def test_study_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=study_Programme_strategy)
def test_study_programme_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=study_Programme_strategy)
def test_study_programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=study_Course_strategy)
@settings(max_examples=50)
def test_study_course_instantiation(instance):
    assert isinstance(instance, study_Course)



@given(instance=study_Course_strategy)
def test_study_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=study_Course_strategy)
def test_study_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=study_Course_strategy)
def test_study_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=study_Course_strategy)
def test_study_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=study_SemesterCourse_strategy)
@settings(max_examples=50)
def test_study_semestercourse_instantiation(instance):
    assert isinstance(instance, study_SemesterCourse)



@given(instance=study_SemesterCourse_strategy)
def test_study_semestercourse_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

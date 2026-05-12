import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyprogram_Department,
    studyprogram_Course,
    studyprogram_Slot,
    studyprogram_Specialization,
    studyprogram_Semester,
    studyprogram_Program,
    Season,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogram_department_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Department)


def test_studyprogram_department_constructor_exists():
    assert callable(studyprogram_Department.__init__)


def test_studyprogram_department_constructor_args():
    sig = inspect.signature(studyprogram_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_department_has_name():
    assert hasattr(studyprogram_Department, "name")
    descriptor = None
    for klass in studyprogram_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_course_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Course)


def test_studyprogram_course_constructor_exists():
    assert callable(studyprogram_Course.__init__)


def test_studyprogram_course_constructor_args():
    sig = inspect.signature(studyprogram_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_course_has_credits():
    assert hasattr(studyprogram_Course, "credits")
    descriptor = None
    for klass in studyprogram_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram_course_has_name():
    assert hasattr(studyprogram_Course, "name")
    descriptor = None
    for klass in studyprogram_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_slot_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Slot)


def test_studyprogram_slot_constructor_exists():
    assert callable(studyprogram_Slot.__init__)


def test_studyprogram_slot_constructor_args():
    sig = inspect.signature(studyprogram_Slot.__init__)
    params = list(sig.parameters.keys())



def test_studyprogram_specialization_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Specialization)


def test_studyprogram_specialization_constructor_exists():
    assert callable(studyprogram_Specialization.__init__)


def test_studyprogram_specialization_constructor_args():
    sig = inspect.signature(studyprogram_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_specialization_has_name():
    assert hasattr(studyprogram_Specialization, "name")
    descriptor = None
    for klass in studyprogram_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_semester_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Semester)


def test_studyprogram_semester_constructor_exists():
    assert callable(studyprogram_Semester.__init__)


def test_studyprogram_semester_constructor_args():
    sig = inspect.signature(studyprogram_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "season" in params, "Missing parameter 'season'"

def test_studyprogram_semester_has_year():
    assert hasattr(studyprogram_Semester, "year")
    descriptor = None
    for klass in studyprogram_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram_semester_has_season():
    assert hasattr(studyprogram_Semester, "season")
    descriptor = None
    for klass in studyprogram_Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram_program_is_not_abstract():
    assert not inspect.isabstract(studyprogram_Program)


def test_studyprogram_program_constructor_exists():
    assert callable(studyprogram_Program.__init__)


def test_studyprogram_program_constructor_args():
    sig = inspect.signature(studyprogram_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram_program_has_name():
    assert hasattr(studyprogram_Program, "name")
    descriptor = None
    for klass in studyprogram_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_season_exists():
    # Check that the Enumeration exists
    assert Season is not None

def test_season_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Season]
    expected_literals = [
        "Fall",
        "Summer",
        "Spring",
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
studyprogram_Department_strategy = st.builds(
    studyprogram_Department,
    name=
        safe_text
)
studyprogram_Course_strategy = st.builds(
    studyprogram_Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
studyprogram_Slot_strategy = st.builds(
    studyprogram_Slot,
)
studyprogram_Specialization_strategy = st.builds(
    studyprogram_Specialization,
    name=
        safe_text
)
studyprogram_Semester_strategy = st.builds(
    studyprogram_Semester,
    year=
        st.integers(),
    season=
        safe_text
)
studyprogram_Program_strategy = st.builds(
    studyprogram_Program,
    name=
        safe_text
)

@given(instance=studyprogram_Department_strategy)
@settings(max_examples=50)
def test_studyprogram_department_instantiation(instance):
    assert isinstance(instance, studyprogram_Department)



@given(instance=studyprogram_Department_strategy)
def test_studyprogram_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram_Course_strategy)
@settings(max_examples=50)
def test_studyprogram_course_instantiation(instance):
    assert isinstance(instance, studyprogram_Course)



@given(instance=studyprogram_Course_strategy)
def test_studyprogram_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=studyprogram_Course_strategy)
def test_studyprogram_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram_Slot_strategy)
@settings(max_examples=50)
def test_studyprogram_slot_instantiation(instance):
    assert isinstance(instance, studyprogram_Slot)

@given(instance=studyprogram_Specialization_strategy)
@settings(max_examples=50)
def test_studyprogram_specialization_instantiation(instance):
    assert isinstance(instance, studyprogram_Specialization)



@given(instance=studyprogram_Specialization_strategy)
def test_studyprogram_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram_Semester_strategy)
@settings(max_examples=50)
def test_studyprogram_semester_instantiation(instance):
    assert isinstance(instance, studyprogram_Semester)



@given(instance=studyprogram_Semester_strategy)
def test_studyprogram_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=studyprogram_Semester_strategy)
def test_studyprogram_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=studyprogram_Program_strategy)
@settings(max_examples=50)
def test_studyprogram_program_instantiation(instance):
    assert isinstance(instance, studyprogram_Program)



@given(instance=studyprogram_Program_strategy)
def test_studyprogram_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

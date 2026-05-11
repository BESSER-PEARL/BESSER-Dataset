import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyprogram::Department,
    studyprogram::Course,
    studyprogram::Slot,
    studyprogram::Specialization,
    studyprogram::Semester,
    studyprogram::Program,
    Season,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogram::department_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Department)


def test_studyprogram::department_constructor_exists():
    assert callable(studyprogram::Department.__init__)


def test_studyprogram::department_constructor_args():
    sig = inspect.signature(studyprogram::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::department_has_name():
    assert hasattr(studyprogram::Department, "name")
    descriptor = None
    for klass in studyprogram::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::course_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Course)


def test_studyprogram::course_constructor_exists():
    assert callable(studyprogram::Course.__init__)


def test_studyprogram::course_constructor_args():
    sig = inspect.signature(studyprogram::Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::course_has_credits():
    assert hasattr(studyprogram::Course, "credits")
    descriptor = None
    for klass in studyprogram::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram::course_has_name():
    assert hasattr(studyprogram::Course, "name")
    descriptor = None
    for klass in studyprogram::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::slot_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Slot)


def test_studyprogram::slot_constructor_exists():
    assert callable(studyprogram::Slot.__init__)


def test_studyprogram::slot_constructor_args():
    sig = inspect.signature(studyprogram::Slot.__init__)
    params = list(sig.parameters.keys())



def test_studyprogram::specialization_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Specialization)


def test_studyprogram::specialization_constructor_exists():
    assert callable(studyprogram::Specialization.__init__)


def test_studyprogram::specialization_constructor_args():
    sig = inspect.signature(studyprogram::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::specialization_has_name():
    assert hasattr(studyprogram::Specialization, "name")
    descriptor = None
    for klass in studyprogram::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::semester_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Semester)


def test_studyprogram::semester_constructor_exists():
    assert callable(studyprogram::Semester.__init__)


def test_studyprogram::semester_constructor_args():
    sig = inspect.signature(studyprogram::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "season" in params, "Missing parameter 'season'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyprogram::semester_has_season():
    assert hasattr(studyprogram::Semester, "season")
    descriptor = None
    for klass in studyprogram::Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_studyprogram::semester_has_year():
    assert hasattr(studyprogram::Semester, "year")
    descriptor = None
    for klass in studyprogram::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyprogram::program_is_not_abstract():
    assert not inspect.isabstract(studyprogram::Program)


def test_studyprogram::program_constructor_exists():
    assert callable(studyprogram::Program.__init__)


def test_studyprogram::program_constructor_args():
    sig = inspect.signature(studyprogram::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogram::program_has_name():
    assert hasattr(studyprogram::Program, "name")
    descriptor = None
    for klass in studyprogram::Program.__mro__:
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
        "Summer",
        "Fall",
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
studyprogram::Department_strategy = st.builds(
    studyprogram::Department,
    name=
        safe_text
)
studyprogram::Course_strategy = st.builds(
    studyprogram::Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
studyprogram::Slot_strategy = st.builds(
    studyprogram::Slot,
)
studyprogram::Specialization_strategy = st.builds(
    studyprogram::Specialization,
    name=
        safe_text
)
studyprogram::Semester_strategy = st.builds(
    studyprogram::Semester,
    season=
        safe_text,
    year=
        st.integers()
)
studyprogram::Program_strategy = st.builds(
    studyprogram::Program,
    name=
        safe_text
)

@given(instance=studyprogram::Department_strategy)
@settings(max_examples=50)
def test_studyprogram::department_instantiation(instance):
    assert isinstance(instance, studyprogram::Department)

@given(instance=studyprogram::Department_strategy)
def test_studyprogram::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Department_strategy)
def test_studyprogram::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::Course_strategy)
@settings(max_examples=50)
def test_studyprogram::course_instantiation(instance):
    assert isinstance(instance, studyprogram::Course)

@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Course_strategy)
def test_studyprogram::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::Slot_strategy)
@settings(max_examples=50)
def test_studyprogram::slot_instantiation(instance):
    assert isinstance(instance, studyprogram::Slot)

@given(instance=studyprogram::Specialization_strategy)
@settings(max_examples=50)
def test_studyprogram::specialization_instantiation(instance):
    assert isinstance(instance, studyprogram::Specialization)

@given(instance=studyprogram::Specialization_strategy)
def test_studyprogram::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Specialization_strategy)
def test_studyprogram::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogram::Semester_strategy)
@settings(max_examples=50)
def test_studyprogram::semester_instantiation(instance):
    assert isinstance(instance, studyprogram::Semester)

@given(instance=studyprogram::Semester_strategy)
def test_studyprogram::semester_season_type(instance):
    assert isinstance(instance.season, str)


@given(instance=studyprogram::Semester_strategy)
def test_studyprogram::semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=studyprogram::Semester_strategy)
def test_studyprogram::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studyprogram::Semester_strategy)
def test_studyprogram::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyprogram::Program_strategy)
@settings(max_examples=50)
def test_studyprogram::program_instantiation(instance):
    assert isinstance(instance, studyprogram::Program)

@given(instance=studyprogram::Program_strategy)
def test_studyprogram::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogram::Program_strategy)
def test_studyprogram::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

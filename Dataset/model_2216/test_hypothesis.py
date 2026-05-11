import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    university::Slot,
    university::Semesters,
    university::University,
    university::CourseInstances,
    university::Courses,
    university::Specializations,
    university::ProgrammeSemesters,
    university::ProgrammeInstances,
    university::Programmes,
    SlotType,
    SemesterTime,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university::slot_is_not_abstract():
    assert not inspect.isabstract(university::Slot)


def test_university::slot_constructor_exists():
    assert callable(university::Slot.__init__)


def test_university::slot_constructor_args():
    sig = inspect.signature(university::Slot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "points" in params, "Missing parameter 'points'"
    assert "slotType" in params, "Missing parameter 'slotType'"

def test_university::slot_has_name():
    assert hasattr(university::Slot, "name")
    descriptor = None
    for klass in university::Slot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university::slot_has_points():
    assert hasattr(university::Slot, "points")
    descriptor = None
    for klass in university::Slot.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_university::slot_has_slotType():
    assert hasattr(university::Slot, "slotType")
    descriptor = None
    for klass in university::Slot.__mro__:
        if "slotType" in klass.__dict__:
            descriptor = klass.__dict__["slotType"]
            break
    assert isinstance(descriptor, property)



def test_university::semesters_is_not_abstract():
    assert not inspect.isabstract(university::Semesters)


def test_university::semesters_constructor_exists():
    assert callable(university::Semesters.__init__)


def test_university::semesters_constructor_args():
    sig = inspect.signature(university::Semesters.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "semesterTime" in params, "Missing parameter 'semesterTime'"

def test_university::semesters_has_year():
    assert hasattr(university::Semesters, "year")
    descriptor = None
    for klass in university::Semesters.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_university::semesters_has_semesterTime():
    assert hasattr(university::Semesters, "semesterTime")
    descriptor = None
    for klass in university::Semesters.__mro__:
        if "semesterTime" in klass.__dict__:
            descriptor = klass.__dict__["semesterTime"]
            break
    assert isinstance(descriptor, property)



def test_university::university_is_not_abstract():
    assert not inspect.isabstract(university::University)


def test_university::university_constructor_exists():
    assert callable(university::University.__init__)


def test_university::university_constructor_args():
    sig = inspect.signature(university::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::university_has_name():
    assert hasattr(university::University, "name")
    descriptor = None
    for klass in university::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::courseinstances_is_not_abstract():
    assert not inspect.isabstract(university::CourseInstances)


def test_university::courseinstances_constructor_exists():
    assert callable(university::CourseInstances.__init__)


def test_university::courseinstances_constructor_args():
    sig = inspect.signature(university::CourseInstances.__init__)
    params = list(sig.parameters.keys())



def test_university::courses_is_not_abstract():
    assert not inspect.isabstract(university::Courses)


def test_university::courses_constructor_exists():
    assert callable(university::Courses.__init__)


def test_university::courses_constructor_args():
    sig = inspect.signature(university::Courses.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_university::courses_has_credits():
    assert hasattr(university::Courses, "credits")
    descriptor = None
    for klass in university::Courses.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_university::courses_has_name():
    assert hasattr(university::Courses, "name")
    descriptor = None
    for klass in university::Courses.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university::courses_has_code():
    assert hasattr(university::Courses, "code")
    descriptor = None
    for klass in university::Courses.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_university::specializations_is_not_abstract():
    assert not inspect.isabstract(university::Specializations)


def test_university::specializations_constructor_exists():
    assert callable(university::Specializations.__init__)


def test_university::specializations_constructor_args():
    sig = inspect.signature(university::Specializations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::specializations_has_name():
    assert hasattr(university::Specializations, "name")
    descriptor = None
    for klass in university::Specializations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::programmesemesters_is_not_abstract():
    assert not inspect.isabstract(university::ProgrammeSemesters)


def test_university::programmesemesters_constructor_exists():
    assert callable(university::ProgrammeSemesters.__init__)


def test_university::programmesemesters_constructor_args():
    sig = inspect.signature(university::ProgrammeSemesters.__init__)
    params = list(sig.parameters.keys())



def test_university::programmeinstances_is_not_abstract():
    assert not inspect.isabstract(university::ProgrammeInstances)


def test_university::programmeinstances_constructor_exists():
    assert callable(university::ProgrammeInstances.__init__)


def test_university::programmeinstances_constructor_args():
    sig = inspect.signature(university::ProgrammeInstances.__init__)
    params = list(sig.parameters.keys())
    assert "startYear" in params, "Missing parameter 'startYear'"

def test_university::programmeinstances_has_startYear():
    assert hasattr(university::ProgrammeInstances, "startYear")
    descriptor = None
    for klass in university::ProgrammeInstances.__mro__:
        if "startYear" in klass.__dict__:
            descriptor = klass.__dict__["startYear"]
            break
    assert isinstance(descriptor, property)



def test_university::programmes_is_not_abstract():
    assert not inspect.isabstract(university::Programmes)


def test_university::programmes_constructor_exists():
    assert callable(university::Programmes.__init__)


def test_university::programmes_constructor_args():
    sig = inspect.signature(university::Programmes.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_university::programmes_has_code():
    assert hasattr(university::Programmes, "code")
    descriptor = None
    for klass in university::Programmes.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_university::programmes_has_name():
    assert hasattr(university::Programmes, "name")
    descriptor = None
    for klass in university::Programmes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_slottype_exists():
    # Check that the Enumeration exists
    assert SlotType is not None

def test_slottype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SlotType]
    expected_literals = [
        "V2",
        "O",
        "V",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SlotType"

def test_semestertime_exists():
    # Check that the Enumeration exists
    assert SemesterTime is not None

def test_semestertime_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterTime]
    expected_literals = [
        "Fall",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterTime"


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
university::Slot_strategy = st.builds(
    university::Slot,
    name=
        safe_text,
    points=
        st.integers(),
    slotType=
        safe_text
)
university::Semesters_strategy = st.builds(
    university::Semesters,
    year=
        st.integers(),
    semesterTime=
        safe_text
)
university::University_strategy = st.builds(
    university::University,
    name=
        safe_text
)
university::CourseInstances_strategy = st.builds(
    university::CourseInstances,
)
university::Courses_strategy = st.builds(
    university::Courses,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text
)
university::Specializations_strategy = st.builds(
    university::Specializations,
    name=
        safe_text
)
university::ProgrammeSemesters_strategy = st.builds(
    university::ProgrammeSemesters,
)
university::ProgrammeInstances_strategy = st.builds(
    university::ProgrammeInstances,
    startYear=
        st.integers()
)
university::Programmes_strategy = st.builds(
    university::Programmes,
    code=
        safe_text,
    name=
        safe_text
)

@given(instance=university::Slot_strategy)
@settings(max_examples=50)
def test_university::slot_instantiation(instance):
    assert isinstance(instance, university::Slot)

@given(instance=university::Slot_strategy)
def test_university::slot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Slot_strategy)
def test_university::slot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Slot_strategy)
def test_university::slot_points_type(instance):
    assert isinstance(instance.points, int)


@given(instance=university::Slot_strategy)
def test_university::slot_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=university::Slot_strategy)
def test_university::slot_slotType_type(instance):
    assert isinstance(instance.slotType, str)


@given(instance=university::Slot_strategy)
def test_university::slot_slotType_setter(instance):
    original = instance.slotType
    instance.slotType = original
    assert instance.slotType == original

@given(instance=university::Semesters_strategy)
@settings(max_examples=50)
def test_university::semesters_instantiation(instance):
    assert isinstance(instance, university::Semesters)

@given(instance=university::Semesters_strategy)
def test_university::semesters_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=university::Semesters_strategy)
def test_university::semesters_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=university::Semesters_strategy)
def test_university::semesters_semesterTime_type(instance):
    assert isinstance(instance.semesterTime, str)


@given(instance=university::Semesters_strategy)
def test_university::semesters_semesterTime_setter(instance):
    original = instance.semesterTime
    instance.semesterTime = original
    assert instance.semesterTime == original

@given(instance=university::University_strategy)
@settings(max_examples=50)
def test_university::university_instantiation(instance):
    assert isinstance(instance, university::University)

@given(instance=university::University_strategy)
def test_university::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::University_strategy)
def test_university::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::CourseInstances_strategy)
@settings(max_examples=50)
def test_university::courseinstances_instantiation(instance):
    assert isinstance(instance, university::CourseInstances)

@given(instance=university::Courses_strategy)
@settings(max_examples=50)
def test_university::courses_instantiation(instance):
    assert isinstance(instance, university::Courses)

@given(instance=university::Courses_strategy)
def test_university::courses_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=university::Courses_strategy)
def test_university::courses_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=university::Courses_strategy)
def test_university::courses_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Courses_strategy)
def test_university::courses_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Courses_strategy)
def test_university::courses_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=university::Courses_strategy)
def test_university::courses_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=university::Specializations_strategy)
@settings(max_examples=50)
def test_university::specializations_instantiation(instance):
    assert isinstance(instance, university::Specializations)

@given(instance=university::Specializations_strategy)
def test_university::specializations_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Specializations_strategy)
def test_university::specializations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::ProgrammeSemesters_strategy)
@settings(max_examples=50)
def test_university::programmesemesters_instantiation(instance):
    assert isinstance(instance, university::ProgrammeSemesters)

@given(instance=university::ProgrammeInstances_strategy)
@settings(max_examples=50)
def test_university::programmeinstances_instantiation(instance):
    assert isinstance(instance, university::ProgrammeInstances)

@given(instance=university::ProgrammeInstances_strategy)
def test_university::programmeinstances_startYear_type(instance):
    assert isinstance(instance.startYear, int)


@given(instance=university::ProgrammeInstances_strategy)
def test_university::programmeinstances_startYear_setter(instance):
    original = instance.startYear
    instance.startYear = original
    assert instance.startYear == original

@given(instance=university::Programmes_strategy)
@settings(max_examples=50)
def test_university::programmes_instantiation(instance):
    assert isinstance(instance, university::Programmes)

@given(instance=university::Programmes_strategy)
def test_university::programmes_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=university::Programmes_strategy)
def test_university::programmes_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=university::Programmes_strategy)
def test_university::programmes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::Programmes_strategy)
def test_university::programmes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

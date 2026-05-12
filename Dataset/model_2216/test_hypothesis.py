import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    university_Slot,
    university_Semesters,
    university_University,
    university_CourseInstances,
    university_Courses,
    university_Specializations,
    university_ProgrammeSemesters,
    university_ProgrammeInstances,
    university_Programmes,
    SlotType,
    SemesterTime,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university_slot_is_not_abstract():
    assert not inspect.isabstract(university_Slot)


def test_university_slot_constructor_exists():
    assert callable(university_Slot.__init__)


def test_university_slot_constructor_args():
    sig = inspect.signature(university_Slot.__init__)
    params = list(sig.parameters.keys())
    assert "slotType" in params, "Missing parameter 'slotType'"
    assert "points" in params, "Missing parameter 'points'"
    assert "name" in params, "Missing parameter 'name'"

def test_university_slot_has_slotType():
    assert hasattr(university_Slot, "slotType")
    descriptor = None
    for klass in university_Slot.__mro__:
        if "slotType" in klass.__dict__:
            descriptor = klass.__dict__["slotType"]
            break
    assert isinstance(descriptor, property)

def test_university_slot_has_points():
    assert hasattr(university_Slot, "points")
    descriptor = None
    for klass in university_Slot.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_university_slot_has_name():
    assert hasattr(university_Slot, "name")
    descriptor = None
    for klass in university_Slot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_semesters_is_not_abstract():
    assert not inspect.isabstract(university_Semesters)


def test_university_semesters_constructor_exists():
    assert callable(university_Semesters.__init__)


def test_university_semesters_constructor_args():
    sig = inspect.signature(university_Semesters.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "semesterTime" in params, "Missing parameter 'semesterTime'"

def test_university_semesters_has_year():
    assert hasattr(university_Semesters, "year")
    descriptor = None
    for klass in university_Semesters.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_university_semesters_has_semesterTime():
    assert hasattr(university_Semesters, "semesterTime")
    descriptor = None
    for klass in university_Semesters.__mro__:
        if "semesterTime" in klass.__dict__:
            descriptor = klass.__dict__["semesterTime"]
            break
    assert isinstance(descriptor, property)



def test_university_university_is_not_abstract():
    assert not inspect.isabstract(university_University)


def test_university_university_constructor_exists():
    assert callable(university_University.__init__)


def test_university_university_constructor_args():
    sig = inspect.signature(university_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university_university_has_name():
    assert hasattr(university_University, "name")
    descriptor = None
    for klass in university_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_courseinstances_is_not_abstract():
    assert not inspect.isabstract(university_CourseInstances)


def test_university_courseinstances_constructor_exists():
    assert callable(university_CourseInstances.__init__)


def test_university_courseinstances_constructor_args():
    sig = inspect.signature(university_CourseInstances.__init__)
    params = list(sig.parameters.keys())



def test_university_courses_is_not_abstract():
    assert not inspect.isabstract(university_Courses)


def test_university_courses_constructor_exists():
    assert callable(university_Courses.__init__)


def test_university_courses_constructor_args():
    sig = inspect.signature(university_Courses.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "name" in params, "Missing parameter 'name'"

def test_university_courses_has_code():
    assert hasattr(university_Courses, "code")
    descriptor = None
    for klass in university_Courses.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_university_courses_has_credits():
    assert hasattr(university_Courses, "credits")
    descriptor = None
    for klass in university_Courses.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_university_courses_has_name():
    assert hasattr(university_Courses, "name")
    descriptor = None
    for klass in university_Courses.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_specializations_is_not_abstract():
    assert not inspect.isabstract(university_Specializations)


def test_university_specializations_constructor_exists():
    assert callable(university_Specializations.__init__)


def test_university_specializations_constructor_args():
    sig = inspect.signature(university_Specializations.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university_specializations_has_name():
    assert hasattr(university_Specializations, "name")
    descriptor = None
    for klass in university_Specializations.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_programmesemesters_is_not_abstract():
    assert not inspect.isabstract(university_ProgrammeSemesters)


def test_university_programmesemesters_constructor_exists():
    assert callable(university_ProgrammeSemesters.__init__)


def test_university_programmesemesters_constructor_args():
    sig = inspect.signature(university_ProgrammeSemesters.__init__)
    params = list(sig.parameters.keys())



def test_university_programmeinstances_is_not_abstract():
    assert not inspect.isabstract(university_ProgrammeInstances)


def test_university_programmeinstances_constructor_exists():
    assert callable(university_ProgrammeInstances.__init__)


def test_university_programmeinstances_constructor_args():
    sig = inspect.signature(university_ProgrammeInstances.__init__)
    params = list(sig.parameters.keys())
    assert "startYear" in params, "Missing parameter 'startYear'"

def test_university_programmeinstances_has_startYear():
    assert hasattr(university_ProgrammeInstances, "startYear")
    descriptor = None
    for klass in university_ProgrammeInstances.__mro__:
        if "startYear" in klass.__dict__:
            descriptor = klass.__dict__["startYear"]
            break
    assert isinstance(descriptor, property)



def test_university_programmes_is_not_abstract():
    assert not inspect.isabstract(university_Programmes)


def test_university_programmes_constructor_exists():
    assert callable(university_Programmes.__init__)


def test_university_programmes_constructor_args():
    sig = inspect.signature(university_Programmes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_university_programmes_has_name():
    assert hasattr(university_Programmes, "name")
    descriptor = None
    for klass in university_Programmes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_university_programmes_has_code():
    assert hasattr(university_Programmes, "code")
    descriptor = None
    for klass in university_Programmes.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_slottype_exists():
    # Check that the Enumeration exists
    assert SlotType is not None

def test_slottype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SlotType]
    expected_literals = [
        "V",
        "V2",
        "O",
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
        "Spring",
        "Fall",
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
university_Slot_strategy = st.builds(
    university_Slot,
    slotType=
        safe_text,
    points=
        st.integers(),
    name=
        safe_text
)
university_Semesters_strategy = st.builds(
    university_Semesters,
    year=
        st.integers(),
    semesterTime=
        safe_text
)
university_University_strategy = st.builds(
    university_University,
    name=
        safe_text
)
university_CourseInstances_strategy = st.builds(
    university_CourseInstances,
)
university_Courses_strategy = st.builds(
    university_Courses,
    code=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
university_Specializations_strategy = st.builds(
    university_Specializations,
    name=
        safe_text
)
university_ProgrammeSemesters_strategy = st.builds(
    university_ProgrammeSemesters,
)
university_ProgrammeInstances_strategy = st.builds(
    university_ProgrammeInstances,
    startYear=
        st.integers()
)
university_Programmes_strategy = st.builds(
    university_Programmes,
    name=
        safe_text,
    code=
        safe_text
)

@given(instance=university_Slot_strategy)
@settings(max_examples=50)
def test_university_slot_instantiation(instance):
    assert isinstance(instance, university_Slot)



@given(instance=university_Slot_strategy)
def test_university_slot_slotType_setter(instance):
    original = instance.slotType
    instance.slotType = original
    assert instance.slotType == original



@given(instance=university_Slot_strategy)
def test_university_slot_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=university_Slot_strategy)
def test_university_slot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_Semesters_strategy)
@settings(max_examples=50)
def test_university_semesters_instantiation(instance):
    assert isinstance(instance, university_Semesters)



@given(instance=university_Semesters_strategy)
def test_university_semesters_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=university_Semesters_strategy)
def test_university_semesters_semesterTime_setter(instance):
    original = instance.semesterTime
    instance.semesterTime = original
    assert instance.semesterTime == original

@given(instance=university_University_strategy)
@settings(max_examples=50)
def test_university_university_instantiation(instance):
    assert isinstance(instance, university_University)



@given(instance=university_University_strategy)
def test_university_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_CourseInstances_strategy)
@settings(max_examples=50)
def test_university_courseinstances_instantiation(instance):
    assert isinstance(instance, university_CourseInstances)

@given(instance=university_Courses_strategy)
@settings(max_examples=50)
def test_university_courses_instantiation(instance):
    assert isinstance(instance, university_Courses)



@given(instance=university_Courses_strategy)
def test_university_courses_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=university_Courses_strategy)
def test_university_courses_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=university_Courses_strategy)
def test_university_courses_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_Specializations_strategy)
@settings(max_examples=50)
def test_university_specializations_instantiation(instance):
    assert isinstance(instance, university_Specializations)



@given(instance=university_Specializations_strategy)
def test_university_specializations_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_ProgrammeSemesters_strategy)
@settings(max_examples=50)
def test_university_programmesemesters_instantiation(instance):
    assert isinstance(instance, university_ProgrammeSemesters)

@given(instance=university_ProgrammeInstances_strategy)
@settings(max_examples=50)
def test_university_programmeinstances_instantiation(instance):
    assert isinstance(instance, university_ProgrammeInstances)



@given(instance=university_ProgrammeInstances_strategy)
def test_university_programmeinstances_startYear_setter(instance):
    original = instance.startYear
    instance.startYear = original
    assert instance.startYear == original

@given(instance=university_Programmes_strategy)
@settings(max_examples=50)
def test_university_programmes_instantiation(instance):
    assert isinstance(instance, university_Programmes)



@given(instance=university_Programmes_strategy)
def test_university_programmes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=university_Programmes_strategy)
def test_university_programmes_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

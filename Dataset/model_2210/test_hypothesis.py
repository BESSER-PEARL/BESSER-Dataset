import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CourseSlot,
    universityStudies::ElectiveCourseSlot,
    universityStudies::MandatoryCourseSlot,
    universityStudies::Department,
    universityStudies::Semester,
    universityStudies::Specialization,
    universityStudies::Programme,
    universityStudies::CourseSlot,
    universityStudies::Course,
    Seasons,
    ProgrammeType,
    Credits,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_courseslot_is_not_abstract():
    assert not inspect.isabstract(CourseSlot)


def test_courseslot_constructor_exists():
    assert callable(CourseSlot.__init__)


def test_courseslot_constructor_args():
    sig = inspect.signature(CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies::electivecourseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies::ElectiveCourseSlot)


def test_universitystudies::electivecourseslot_constructor_exists():
    assert callable(universityStudies::ElectiveCourseSlot.__init__)


def test_universitystudies::electivecourseslot_constructor_args():
    sig = inspect.signature(universityStudies::ElectiveCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies::mandatorycourseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies::MandatoryCourseSlot)


def test_universitystudies::mandatorycourseslot_constructor_exists():
    assert callable(universityStudies::MandatoryCourseSlot.__init__)


def test_universitystudies::mandatorycourseslot_constructor_args():
    sig = inspect.signature(universityStudies::MandatoryCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies::department_is_not_abstract():
    assert not inspect.isabstract(universityStudies::Department)


def test_universitystudies::department_constructor_exists():
    assert callable(universityStudies::Department.__init__)


def test_universitystudies::department_constructor_args():
    sig = inspect.signature(universityStudies::Department.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies::semester_is_not_abstract():
    assert not inspect.isabstract(universityStudies::Semester)


def test_universitystudies::semester_constructor_exists():
    assert callable(universityStudies::Semester.__init__)


def test_universitystudies::semester_constructor_args():
    sig = inspect.signature(universityStudies::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "season" in params, "Missing parameter 'season'"
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_universitystudies::semester_has_season():
    assert hasattr(universityStudies::Semester, "season")
    descriptor = None
    for klass in universityStudies::Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies::semester_has_semesterNumber():
    assert hasattr(universityStudies::Semester, "semesterNumber")
    descriptor = None
    for klass in universityStudies::Semester.__mro__:
        if "semesterNumber" in klass.__dict__:
            descriptor = klass.__dict__["semesterNumber"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies::semester_has_name():
    assert hasattr(universityStudies::Semester, "name")
    descriptor = None
    for klass in universityStudies::Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_universitystudies::specialization_is_not_abstract():
    assert not inspect.isabstract(universityStudies::Specialization)


def test_universitystudies::specialization_constructor_exists():
    assert callable(universityStudies::Specialization.__init__)


def test_universitystudies::specialization_constructor_args():
    sig = inspect.signature(universityStudies::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_universitystudies::specialization_has_name():
    assert hasattr(universityStudies::Specialization, "name")
    descriptor = None
    for klass in universityStudies::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_universitystudies::programme_is_not_abstract():
    assert not inspect.isabstract(universityStudies::Programme)


def test_universitystudies::programme_constructor_exists():
    assert callable(universityStudies::Programme.__init__)


def test_universitystudies::programme_constructor_args():
    sig = inspect.signature(universityStudies::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfSemesters" in params, "Missing parameter 'numberOfSemesters'"
    assert "name" in params, "Missing parameter 'name'"
    assert "programmeType" in params, "Missing parameter 'programmeType'"

def test_universitystudies::programme_has_numberOfSemesters():
    assert hasattr(universityStudies::Programme, "numberOfSemesters")
    descriptor = None
    for klass in universityStudies::Programme.__mro__:
        if "numberOfSemesters" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSemesters"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies::programme_has_name():
    assert hasattr(universityStudies::Programme, "name")
    descriptor = None
    for klass in universityStudies::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies::programme_has_programmeType():
    assert hasattr(universityStudies::Programme, "programmeType")
    descriptor = None
    for klass in universityStudies::Programme.__mro__:
        if "programmeType" in klass.__dict__:
            descriptor = klass.__dict__["programmeType"]
            break
    assert isinstance(descriptor, property)



def test_universitystudies::courseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies::CourseSlot)


def test_universitystudies::courseslot_constructor_exists():
    assert callable(universityStudies::CourseSlot.__init__)


def test_universitystudies::courseslot_constructor_args():
    sig = inspect.signature(universityStudies::CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies::course_is_not_abstract():
    assert not inspect.isabstract(universityStudies::Course)


def test_universitystudies::course_constructor_exists():
    assert callable(universityStudies::Course.__init__)


def test_universitystudies::course_constructor_args():
    sig = inspect.signature(universityStudies::Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "credits" in params, "Missing parameter 'credits'"

def test_universitystudies::course_has_level():
    assert hasattr(universityStudies::Course, "level")
    descriptor = None
    for klass in universityStudies::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies::course_has_name():
    assert hasattr(universityStudies::Course, "name")
    descriptor = None
    for klass in universityStudies::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies::course_has_code():
    assert hasattr(universityStudies::Course, "code")
    descriptor = None
    for klass in universityStudies::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies::course_has_credits():
    assert hasattr(universityStudies::Course, "credits")
    descriptor = None
    for klass in universityStudies::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_seasons_exists():
    # Check that the Enumeration exists
    assert Seasons is not None

def test_seasons_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Seasons]
    expected_literals = [
        "Spring",
        "Fall",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Seasons"

def test_programmetype_exists():
    # Check that the Enumeration exists
    assert ProgrammeType is not None

def test_programmetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeType]
    expected_literals = [
        "Master",
        "Årsstudie",
        "IntegrertMaster",
        "Bachelor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeType"

def test_credits_exists():
    # Check that the Enumeration exists
    assert Credits is not None

def test_credits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Credits]
    expected_literals = [
        "Double",
        "Full",
        "Basic",
        "Minor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Credits"


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
CourseSlot_strategy = st.builds(
    CourseSlot,
)
universityStudies::ElectiveCourseSlot_strategy = st.builds(
    universityStudies::ElectiveCourseSlot,
)
universityStudies::MandatoryCourseSlot_strategy = st.builds(
    universityStudies::MandatoryCourseSlot,
)
universityStudies::Department_strategy = st.builds(
    universityStudies::Department,
)
universityStudies::Semester_strategy = st.builds(
    universityStudies::Semester,
    season=
        safe_text,
    semesterNumber=
        st.integers(),
    name=
        safe_text
)
universityStudies::Specialization_strategy = st.builds(
    universityStudies::Specialization,
    name=
        safe_text
)
universityStudies::Programme_strategy = st.builds(
    universityStudies::Programme,
    numberOfSemesters=
        st.integers(),
    name=
        safe_text,
    programmeType=
        safe_text
)
universityStudies::CourseSlot_strategy = st.builds(
    universityStudies::CourseSlot,
)
universityStudies::Course_strategy = st.builds(
    universityStudies::Course,
    level=
        st.integers(),
    name=
        safe_text,
    code=
        safe_text,
    credits=
        safe_text
)

@given(instance=CourseSlot_strategy)
@settings(max_examples=50)
def test_courseslot_instantiation(instance):
    assert isinstance(instance, CourseSlot)

@given(instance=universityStudies::ElectiveCourseSlot_strategy)
@settings(max_examples=50)
def test_universitystudies::electivecourseslot_instantiation(instance):
    assert isinstance(instance, universityStudies::ElectiveCourseSlot)

@given(instance=universityStudies::MandatoryCourseSlot_strategy)
@settings(max_examples=50)
def test_universitystudies::mandatorycourseslot_instantiation(instance):
    assert isinstance(instance, universityStudies::MandatoryCourseSlot)

@given(instance=universityStudies::Department_strategy)
@settings(max_examples=50)
def test_universitystudies::department_instantiation(instance):
    assert isinstance(instance, universityStudies::Department)

@given(instance=universityStudies::Semester_strategy)
@settings(max_examples=50)
def test_universitystudies::semester_instantiation(instance):
    assert isinstance(instance, universityStudies::Semester)

@given(instance=universityStudies::Semester_strategy)
def test_universitystudies::semester_season_type(instance):
    assert isinstance(instance.season, str)


@given(instance=universityStudies::Semester_strategy)
def test_universitystudies::semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=universityStudies::Semester_strategy)
def test_universitystudies::semester_semesterNumber_type(instance):
    assert isinstance(instance.semesterNumber, int)


@given(instance=universityStudies::Semester_strategy)
def test_universitystudies::semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original

@given(instance=universityStudies::Semester_strategy)
def test_universitystudies::semester_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=universityStudies::Semester_strategy)
def test_universitystudies::semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=universityStudies::Specialization_strategy)
@settings(max_examples=50)
def test_universitystudies::specialization_instantiation(instance):
    assert isinstance(instance, universityStudies::Specialization)

@given(instance=universityStudies::Specialization_strategy)
def test_universitystudies::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=universityStudies::Specialization_strategy)
def test_universitystudies::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=universityStudies::Programme_strategy)
@settings(max_examples=50)
def test_universitystudies::programme_instantiation(instance):
    assert isinstance(instance, universityStudies::Programme)

@given(instance=universityStudies::Programme_strategy)
def test_universitystudies::programme_numberOfSemesters_type(instance):
    assert isinstance(instance.numberOfSemesters, int)


@given(instance=universityStudies::Programme_strategy)
def test_universitystudies::programme_numberOfSemesters_setter(instance):
    original = instance.numberOfSemesters
    instance.numberOfSemesters = original
    assert instance.numberOfSemesters == original

@given(instance=universityStudies::Programme_strategy)
def test_universitystudies::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=universityStudies::Programme_strategy)
def test_universitystudies::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=universityStudies::Programme_strategy)
def test_universitystudies::programme_programmeType_type(instance):
    assert isinstance(instance.programmeType, str)


@given(instance=universityStudies::Programme_strategy)
def test_universitystudies::programme_programmeType_setter(instance):
    original = instance.programmeType
    instance.programmeType = original
    assert instance.programmeType == original

@given(instance=universityStudies::CourseSlot_strategy)
@settings(max_examples=50)
def test_universitystudies::courseslot_instantiation(instance):
    assert isinstance(instance, universityStudies::CourseSlot)

@given(instance=universityStudies::Course_strategy)
@settings(max_examples=50)
def test_universitystudies::course_instantiation(instance):
    assert isinstance(instance, universityStudies::Course)

@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_credits_type(instance):
    assert isinstance(instance.credits, str)


@given(instance=universityStudies::Course_strategy)
def test_universitystudies::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CourseSlot,
    universityStudies_ElectiveCourseSlot,
    universityStudies_MandatoryCourseSlot,
    universityStudies_Department,
    universityStudies_Semester,
    universityStudies_Specialization,
    universityStudies_Programme,
    universityStudies_CourseSlot,
    universityStudies_Course,
    ProgrammeType,
    Seasons,
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



def test_universitystudies_electivecourseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies_ElectiveCourseSlot)


def test_universitystudies_electivecourseslot_constructor_exists():
    assert callable(universityStudies_ElectiveCourseSlot.__init__)


def test_universitystudies_electivecourseslot_constructor_args():
    sig = inspect.signature(universityStudies_ElectiveCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies_mandatorycourseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies_MandatoryCourseSlot)


def test_universitystudies_mandatorycourseslot_constructor_exists():
    assert callable(universityStudies_MandatoryCourseSlot.__init__)


def test_universitystudies_mandatorycourseslot_constructor_args():
    sig = inspect.signature(universityStudies_MandatoryCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies_department_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Department)


def test_universitystudies_department_constructor_exists():
    assert callable(universityStudies_Department.__init__)


def test_universitystudies_department_constructor_args():
    sig = inspect.signature(universityStudies_Department.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies_semester_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Semester)


def test_universitystudies_semester_constructor_exists():
    assert callable(universityStudies_Semester.__init__)


def test_universitystudies_semester_constructor_args():
    sig = inspect.signature(universityStudies_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "season" in params, "Missing parameter 'season'"

def test_universitystudies_semester_has_semesterNumber():
    assert hasattr(universityStudies_Semester, "semesterNumber")
    descriptor = None
    for klass in universityStudies_Semester.__mro__:
        if "semesterNumber" in klass.__dict__:
            descriptor = klass.__dict__["semesterNumber"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies_semester_has_name():
    assert hasattr(universityStudies_Semester, "name")
    descriptor = None
    for klass in universityStudies_Semester.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies_semester_has_season():
    assert hasattr(universityStudies_Semester, "season")
    descriptor = None
    for klass in universityStudies_Semester.__mro__:
        if "season" in klass.__dict__:
            descriptor = klass.__dict__["season"]
            break
    assert isinstance(descriptor, property)



def test_universitystudies_specialization_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Specialization)


def test_universitystudies_specialization_constructor_exists():
    assert callable(universityStudies_Specialization.__init__)


def test_universitystudies_specialization_constructor_args():
    sig = inspect.signature(universityStudies_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_universitystudies_specialization_has_name():
    assert hasattr(universityStudies_Specialization, "name")
    descriptor = None
    for klass in universityStudies_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_universitystudies_programme_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Programme)


def test_universitystudies_programme_constructor_exists():
    assert callable(universityStudies_Programme.__init__)


def test_universitystudies_programme_constructor_args():
    sig = inspect.signature(universityStudies_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "programmeType" in params, "Missing parameter 'programmeType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numberOfSemesters" in params, "Missing parameter 'numberOfSemesters'"

def test_universitystudies_programme_has_programmeType():
    assert hasattr(universityStudies_Programme, "programmeType")
    descriptor = None
    for klass in universityStudies_Programme.__mro__:
        if "programmeType" in klass.__dict__:
            descriptor = klass.__dict__["programmeType"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies_programme_has_name():
    assert hasattr(universityStudies_Programme, "name")
    descriptor = None
    for klass in universityStudies_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies_programme_has_numberOfSemesters():
    assert hasattr(universityStudies_Programme, "numberOfSemesters")
    descriptor = None
    for klass in universityStudies_Programme.__mro__:
        if "numberOfSemesters" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSemesters"]
            break
    assert isinstance(descriptor, property)



def test_universitystudies_courseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies_CourseSlot)


def test_universitystudies_courseslot_constructor_exists():
    assert callable(universityStudies_CourseSlot.__init__)


def test_universitystudies_courseslot_constructor_args():
    sig = inspect.signature(universityStudies_CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_universitystudies_course_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Course)


def test_universitystudies_course_constructor_exists():
    assert callable(universityStudies_Course.__init__)


def test_universitystudies_course_constructor_args():
    sig = inspect.signature(universityStudies_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "level" in params, "Missing parameter 'level'"

def test_universitystudies_course_has_code():
    assert hasattr(universityStudies_Course, "code")
    descriptor = None
    for klass in universityStudies_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies_course_has_name():
    assert hasattr(universityStudies_Course, "name")
    descriptor = None
    for klass in universityStudies_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies_course_has_credits():
    assert hasattr(universityStudies_Course, "credits")
    descriptor = None
    for klass in universityStudies_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_universitystudies_course_has_level():
    assert hasattr(universityStudies_Course, "level")
    descriptor = None
    for klass in universityStudies_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_programmetype_exists():
    # Check that the Enumeration exists
    assert ProgrammeType is not None

def test_programmetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeType]
    expected_literals = [
        "IntegrertMaster",
        "Master",
        "Årsstudie",
        "Bachelor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeType"

def test_seasons_exists():
    # Check that the Enumeration exists
    assert Seasons is not None

def test_seasons_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Seasons]
    expected_literals = [
        "Fall",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Seasons"

def test_credits_exists():
    # Check that the Enumeration exists
    assert Credits is not None

def test_credits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Credits]
    expected_literals = [
        "Double",
        "Minor",
        "Basic",
        "Full",
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
universityStudies_ElectiveCourseSlot_strategy = st.builds(
    universityStudies_ElectiveCourseSlot,
)
universityStudies_MandatoryCourseSlot_strategy = st.builds(
    universityStudies_MandatoryCourseSlot,
)
universityStudies_Department_strategy = st.builds(
    universityStudies_Department,
)
universityStudies_Semester_strategy = st.builds(
    universityStudies_Semester,
    semesterNumber=
        st.integers(),
    name=
        safe_text,
    season=
        safe_text
)
universityStudies_Specialization_strategy = st.builds(
    universityStudies_Specialization,
    name=
        safe_text
)
universityStudies_Programme_strategy = st.builds(
    universityStudies_Programme,
    programmeType=
        safe_text,
    name=
        safe_text,
    numberOfSemesters=
        st.integers()
)
universityStudies_CourseSlot_strategy = st.builds(
    universityStudies_CourseSlot,
)
universityStudies_Course_strategy = st.builds(
    universityStudies_Course,
    code=
        safe_text,
    name=
        safe_text,
    credits=
        safe_text,
    level=
        st.integers()
)

@given(instance=CourseSlot_strategy)
@settings(max_examples=50)
def test_courseslot_instantiation(instance):
    assert isinstance(instance, CourseSlot)

@given(instance=universityStudies_ElectiveCourseSlot_strategy)
@settings(max_examples=50)
def test_universitystudies_electivecourseslot_instantiation(instance):
    assert isinstance(instance, universityStudies_ElectiveCourseSlot)

@given(instance=universityStudies_MandatoryCourseSlot_strategy)
@settings(max_examples=50)
def test_universitystudies_mandatorycourseslot_instantiation(instance):
    assert isinstance(instance, universityStudies_MandatoryCourseSlot)

@given(instance=universityStudies_Department_strategy)
@settings(max_examples=50)
def test_universitystudies_department_instantiation(instance):
    assert isinstance(instance, universityStudies_Department)

@given(instance=universityStudies_Semester_strategy)
@settings(max_examples=50)
def test_universitystudies_semester_instantiation(instance):
    assert isinstance(instance, universityStudies_Semester)



@given(instance=universityStudies_Semester_strategy)
def test_universitystudies_semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original



@given(instance=universityStudies_Semester_strategy)
def test_universitystudies_semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=universityStudies_Semester_strategy)
def test_universitystudies_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original

@given(instance=universityStudies_Specialization_strategy)
@settings(max_examples=50)
def test_universitystudies_specialization_instantiation(instance):
    assert isinstance(instance, universityStudies_Specialization)



@given(instance=universityStudies_Specialization_strategy)
def test_universitystudies_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=universityStudies_Programme_strategy)
@settings(max_examples=50)
def test_universitystudies_programme_instantiation(instance):
    assert isinstance(instance, universityStudies_Programme)



@given(instance=universityStudies_Programme_strategy)
def test_universitystudies_programme_programmeType_setter(instance):
    original = instance.programmeType
    instance.programmeType = original
    assert instance.programmeType == original



@given(instance=universityStudies_Programme_strategy)
def test_universitystudies_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=universityStudies_Programme_strategy)
def test_universitystudies_programme_numberOfSemesters_setter(instance):
    original = instance.numberOfSemesters
    instance.numberOfSemesters = original
    assert instance.numberOfSemesters == original

@given(instance=universityStudies_CourseSlot_strategy)
@settings(max_examples=50)
def test_universitystudies_courseslot_instantiation(instance):
    assert isinstance(instance, universityStudies_CourseSlot)

@given(instance=universityStudies_Course_strategy)
@settings(max_examples=50)
def test_universitystudies_course_instantiation(instance):
    assert isinstance(instance, universityStudies_Course)



@given(instance=universityStudies_Course_strategy)
def test_universitystudies_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=universityStudies_Course_strategy)
def test_universitystudies_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=universityStudies_Course_strategy)
def test_universitystudies_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=universityStudies_Course_strategy)
def test_universitystudies_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

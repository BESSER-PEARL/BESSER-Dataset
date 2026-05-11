import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyprogramme::Semester,
    CourseSlot,
    studyprogramme::CompulsoryCourseSlot,
    studyprogramme::University,
    studyprogramme::ElectiveCourseSlot,
    studyprogramme::ElectiveCourseList,
    studyprogramme::SemesterContainer,
    studyprogramme::CourseSlot,
    SemesterContainer,
    studyprogramme::Specialization,
    studyprogramme::Programme,
    studyprogramme::Course,
    ProgrammeType,
    ProgrammeCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogramme::semester_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::Semester)


def test_studyprogramme::semester_constructor_exists():
    assert callable(studyprogramme::Semester.__init__)


def test_studyprogramme::semester_constructor_args():
    sig = inspect.signature(studyprogramme::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"

def test_studyprogramme::semester_has_semesterNumber():
    assert hasattr(studyprogramme::Semester, "semesterNumber")
    descriptor = None
    for klass in studyprogramme::Semester.__mro__:
        if "semesterNumber" in klass.__dict__:
            descriptor = klass.__dict__["semesterNumber"]
            break
    assert isinstance(descriptor, property)



def test_courseslot_is_not_abstract():
    assert not inspect.isabstract(CourseSlot)


def test_courseslot_constructor_exists():
    assert callable(CourseSlot.__init__)


def test_courseslot_constructor_args():
    sig = inspect.signature(CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme::compulsorycourseslot_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::CompulsoryCourseSlot)


def test_studyprogramme::compulsorycourseslot_constructor_exists():
    assert callable(studyprogramme::CompulsoryCourseSlot.__init__)


def test_studyprogramme::compulsorycourseslot_constructor_args():
    sig = inspect.signature(studyprogramme::CompulsoryCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme::university_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::University)


def test_studyprogramme::university_constructor_exists():
    assert callable(studyprogramme::University.__init__)


def test_studyprogramme::university_constructor_args():
    sig = inspect.signature(studyprogramme::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramme::university_has_name():
    assert hasattr(studyprogramme::University, "name")
    descriptor = None
    for klass in studyprogramme::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme::electivecourseslot_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::ElectiveCourseSlot)


def test_studyprogramme::electivecourseslot_constructor_exists():
    assert callable(studyprogramme::ElectiveCourseSlot.__init__)


def test_studyprogramme::electivecourseslot_constructor_args():
    sig = inspect.signature(studyprogramme::ElectiveCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme::electivecourselist_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::ElectiveCourseList)


def test_studyprogramme::electivecourselist_constructor_exists():
    assert callable(studyprogramme::ElectiveCourseList.__init__)


def test_studyprogramme::electivecourselist_constructor_args():
    sig = inspect.signature(studyprogramme::ElectiveCourseList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramme::electivecourselist_has_name():
    assert hasattr(studyprogramme::ElectiveCourseList, "name")
    descriptor = None
    for klass in studyprogramme::ElectiveCourseList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme::semestercontainer_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::SemesterContainer)


def test_studyprogramme::semestercontainer_constructor_exists():
    assert callable(studyprogramme::SemesterContainer.__init__)


def test_studyprogramme::semestercontainer_constructor_args():
    sig = inspect.signature(studyprogramme::SemesterContainer.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme::courseslot_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::CourseSlot)


def test_studyprogramme::courseslot_constructor_exists():
    assert callable(studyprogramme::CourseSlot.__init__)


def test_studyprogramme::courseslot_constructor_args():
    sig = inspect.signature(studyprogramme::CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_semestercontainer_is_not_abstract():
    assert not inspect.isabstract(SemesterContainer)


def test_semestercontainer_constructor_exists():
    assert callable(SemesterContainer.__init__)


def test_semestercontainer_constructor_args():
    sig = inspect.signature(SemesterContainer.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme::specialization_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::Specialization)


def test_studyprogramme::specialization_constructor_exists():
    assert callable(studyprogramme::Specialization.__init__)


def test_studyprogramme::specialization_constructor_args():
    sig = inspect.signature(studyprogramme::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "selectionSemester" in params, "Missing parameter 'selectionSemester'"

def test_studyprogramme::specialization_has_name():
    assert hasattr(studyprogramme::Specialization, "name")
    descriptor = None
    for klass in studyprogramme::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::specialization_has_selectionSemester():
    assert hasattr(studyprogramme::Specialization, "selectionSemester")
    descriptor = None
    for klass in studyprogramme::Specialization.__mro__:
        if "selectionSemester" in klass.__dict__:
            descriptor = klass.__dict__["selectionSemester"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme::programme_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::Programme)


def test_studyprogramme::programme_constructor_exists():
    assert callable(studyprogramme::Programme.__init__)


def test_studyprogramme::programme_constructor_args():
    sig = inspect.signature(studyprogramme::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "programmeType" in params, "Missing parameter 'programmeType'"
    assert "numberOfYears" in params, "Missing parameter 'numberOfYears'"
    assert "programmeCode" in params, "Missing parameter 'programmeCode'"

def test_studyprogramme::programme_has_name():
    assert hasattr(studyprogramme::Programme, "name")
    descriptor = None
    for klass in studyprogramme::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::programme_has_programmeType():
    assert hasattr(studyprogramme::Programme, "programmeType")
    descriptor = None
    for klass in studyprogramme::Programme.__mro__:
        if "programmeType" in klass.__dict__:
            descriptor = klass.__dict__["programmeType"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::programme_has_numberOfYears():
    assert hasattr(studyprogramme::Programme, "numberOfYears")
    descriptor = None
    for klass in studyprogramme::Programme.__mro__:
        if "numberOfYears" in klass.__dict__:
            descriptor = klass.__dict__["numberOfYears"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::programme_has_programmeCode():
    assert hasattr(studyprogramme::Programme, "programmeCode")
    descriptor = None
    for klass in studyprogramme::Programme.__mro__:
        if "programmeCode" in klass.__dict__:
            descriptor = klass.__dict__["programmeCode"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme::course_is_not_abstract():
    assert not inspect.isabstract(studyprogramme::Course)


def test_studyprogramme::course_constructor_exists():
    assert callable(studyprogramme::Course.__init__)


def test_studyprogramme::course_constructor_args():
    sig = inspect.signature(studyprogramme::Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "courseCode" in params, "Missing parameter 'courseCode'"
    assert "name" in params, "Missing parameter 'name'"
    assert "displayedName" in params, "Missing parameter 'displayedName'"
    assert "credits" in params, "Missing parameter 'credits'"

def test_studyprogramme::course_has_level():
    assert hasattr(studyprogramme::Course, "level")
    descriptor = None
    for klass in studyprogramme::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::course_has_courseCode():
    assert hasattr(studyprogramme::Course, "courseCode")
    descriptor = None
    for klass in studyprogramme::Course.__mro__:
        if "courseCode" in klass.__dict__:
            descriptor = klass.__dict__["courseCode"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::course_has_name():
    assert hasattr(studyprogramme::Course, "name")
    descriptor = None
    for klass in studyprogramme::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::course_has_displayedName():
    assert hasattr(studyprogramme::Course, "displayedName")
    descriptor = None
    for klass in studyprogramme::Course.__mro__:
        if "displayedName" in klass.__dict__:
            descriptor = klass.__dict__["displayedName"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme::course_has_credits():
    assert hasattr(studyprogramme::Course, "credits")
    descriptor = None
    for klass in studyprogramme::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_programmetype_exists():
    # Check that the Enumeration exists
    assert ProgrammeType is not None

def test_programmetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeType]
    expected_literals = [
        "IntegratedMaster",
        "Masters",
        "Bachelors",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeType"

def test_programmecode_exists():
    # Check that the Enumeration exists
    assert ProgrammeCode is not None

def test_programmecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeCode]
    expected_literals = [
        "MIT",
        "MTIOT",
        "MTDT",
        "MIDT",
        "BIT",
        "MTPROD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeCode"


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
studyprogramme::Semester_strategy = st.builds(
    studyprogramme::Semester,
    semesterNumber=
        st.integers()
)
CourseSlot_strategy = st.builds(
    CourseSlot,
)
studyprogramme::CompulsoryCourseSlot_strategy = st.builds(
    studyprogramme::CompulsoryCourseSlot,
)
studyprogramme::University_strategy = st.builds(
    studyprogramme::University,
    name=
        safe_text
)
studyprogramme::ElectiveCourseSlot_strategy = st.builds(
    studyprogramme::ElectiveCourseSlot,
)
studyprogramme::ElectiveCourseList_strategy = st.builds(
    studyprogramme::ElectiveCourseList,
    name=
        safe_text
)
studyprogramme::SemesterContainer_strategy = st.builds(
    studyprogramme::SemesterContainer,
)
studyprogramme::CourseSlot_strategy = st.builds(
    studyprogramme::CourseSlot,
)
SemesterContainer_strategy = st.builds(
    SemesterContainer,
)
studyprogramme::Specialization_strategy = st.builds(
    studyprogramme::Specialization,
    name=
        safe_text,
    selectionSemester=
        st.integers()
)
studyprogramme::Programme_strategy = st.builds(
    studyprogramme::Programme,
    name=
        safe_text,
    programmeType=
        safe_text,
    numberOfYears=
        st.integers(),
    programmeCode=
        safe_text
)
studyprogramme::Course_strategy = st.builds(
    studyprogramme::Course,
    level=
        st.integers(),
    courseCode=
        safe_text,
    name=
        safe_text,
    displayedName=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=studyprogramme::Semester_strategy)
@settings(max_examples=50)
def test_studyprogramme::semester_instantiation(instance):
    assert isinstance(instance, studyprogramme::Semester)

@given(instance=studyprogramme::Semester_strategy)
def test_studyprogramme::semester_semesterNumber_type(instance):
    assert isinstance(instance.semesterNumber, int)


@given(instance=studyprogramme::Semester_strategy)
def test_studyprogramme::semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original

@given(instance=CourseSlot_strategy)
@settings(max_examples=50)
def test_courseslot_instantiation(instance):
    assert isinstance(instance, CourseSlot)

@given(instance=studyprogramme::CompulsoryCourseSlot_strategy)
@settings(max_examples=50)
def test_studyprogramme::compulsorycourseslot_instantiation(instance):
    assert isinstance(instance, studyprogramme::CompulsoryCourseSlot)

@given(instance=studyprogramme::University_strategy)
@settings(max_examples=50)
def test_studyprogramme::university_instantiation(instance):
    assert isinstance(instance, studyprogramme::University)

@given(instance=studyprogramme::University_strategy)
def test_studyprogramme::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogramme::University_strategy)
def test_studyprogramme::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme::ElectiveCourseSlot_strategy)
@settings(max_examples=50)
def test_studyprogramme::electivecourseslot_instantiation(instance):
    assert isinstance(instance, studyprogramme::ElectiveCourseSlot)

@given(instance=studyprogramme::ElectiveCourseList_strategy)
@settings(max_examples=50)
def test_studyprogramme::electivecourselist_instantiation(instance):
    assert isinstance(instance, studyprogramme::ElectiveCourseList)

@given(instance=studyprogramme::ElectiveCourseList_strategy)
def test_studyprogramme::electivecourselist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogramme::ElectiveCourseList_strategy)
def test_studyprogramme::electivecourselist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme::SemesterContainer_strategy)
@settings(max_examples=50)
def test_studyprogramme::semestercontainer_instantiation(instance):
    assert isinstance(instance, studyprogramme::SemesterContainer)

@given(instance=studyprogramme::CourseSlot_strategy)
@settings(max_examples=50)
def test_studyprogramme::courseslot_instantiation(instance):
    assert isinstance(instance, studyprogramme::CourseSlot)

@given(instance=SemesterContainer_strategy)
@settings(max_examples=50)
def test_semestercontainer_instantiation(instance):
    assert isinstance(instance, SemesterContainer)

@given(instance=studyprogramme::Specialization_strategy)
@settings(max_examples=50)
def test_studyprogramme::specialization_instantiation(instance):
    assert isinstance(instance, studyprogramme::Specialization)

@given(instance=studyprogramme::Specialization_strategy)
def test_studyprogramme::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogramme::Specialization_strategy)
def test_studyprogramme::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme::Specialization_strategy)
def test_studyprogramme::specialization_selectionSemester_type(instance):
    assert isinstance(instance.selectionSemester, int)


@given(instance=studyprogramme::Specialization_strategy)
def test_studyprogramme::specialization_selectionSemester_setter(instance):
    original = instance.selectionSemester
    instance.selectionSemester = original
    assert instance.selectionSemester == original

@given(instance=studyprogramme::Programme_strategy)
@settings(max_examples=50)
def test_studyprogramme::programme_instantiation(instance):
    assert isinstance(instance, studyprogramme::Programme)

@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_programmeType_type(instance):
    assert isinstance(instance.programmeType, str)


@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_programmeType_setter(instance):
    original = instance.programmeType
    instance.programmeType = original
    assert instance.programmeType == original

@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_numberOfYears_type(instance):
    assert isinstance(instance.numberOfYears, int)


@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_numberOfYears_setter(instance):
    original = instance.numberOfYears
    instance.numberOfYears = original
    assert instance.numberOfYears == original

@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_programmeCode_type(instance):
    assert isinstance(instance.programmeCode, str)


@given(instance=studyprogramme::Programme_strategy)
def test_studyprogramme::programme_programmeCode_setter(instance):
    original = instance.programmeCode
    instance.programmeCode = original
    assert instance.programmeCode == original

@given(instance=studyprogramme::Course_strategy)
@settings(max_examples=50)
def test_studyprogramme::course_instantiation(instance):
    assert isinstance(instance, studyprogramme::Course)

@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_courseCode_type(instance):
    assert isinstance(instance.courseCode, str)


@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_courseCode_setter(instance):
    original = instance.courseCode
    instance.courseCode = original
    assert instance.courseCode == original

@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_displayedName_type(instance):
    assert isinstance(instance.displayedName, str)


@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_displayedName_setter(instance):
    original = instance.displayedName
    instance.displayedName = original
    assert instance.displayedName == original

@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=studyprogramme::Course_strategy)
def test_studyprogramme::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

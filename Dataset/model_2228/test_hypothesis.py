import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyprogramme_Semester,
    CourseSlot,
    studyprogramme_CompulsoryCourseSlot,
    studyprogramme_University,
    studyprogramme_ElectiveCourseSlot,
    studyprogramme_ElectiveCourseList,
    studyprogramme_SemesterContainer,
    studyprogramme_CourseSlot,
    SemesterContainer,
    studyprogramme_Specialization,
    studyprogramme_Programme,
    studyprogramme_Course,
    ProgrammeCode,
    ProgrammeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogramme_semester_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_Semester)


def test_studyprogramme_semester_constructor_exists():
    assert callable(studyprogramme_Semester.__init__)


def test_studyprogramme_semester_constructor_args():
    sig = inspect.signature(studyprogramme_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"

def test_studyprogramme_semester_has_semesterNumber():
    assert hasattr(studyprogramme_Semester, "semesterNumber")
    descriptor = None
    for klass in studyprogramme_Semester.__mro__:
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



def test_studyprogramme_compulsorycourseslot_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_CompulsoryCourseSlot)


def test_studyprogramme_compulsorycourseslot_constructor_exists():
    assert callable(studyprogramme_CompulsoryCourseSlot.__init__)


def test_studyprogramme_compulsorycourseslot_constructor_args():
    sig = inspect.signature(studyprogramme_CompulsoryCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme_university_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_University)


def test_studyprogramme_university_constructor_exists():
    assert callable(studyprogramme_University.__init__)


def test_studyprogramme_university_constructor_args():
    sig = inspect.signature(studyprogramme_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramme_university_has_name():
    assert hasattr(studyprogramme_University, "name")
    descriptor = None
    for klass in studyprogramme_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme_electivecourseslot_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_ElectiveCourseSlot)


def test_studyprogramme_electivecourseslot_constructor_exists():
    assert callable(studyprogramme_ElectiveCourseSlot.__init__)


def test_studyprogramme_electivecourseslot_constructor_args():
    sig = inspect.signature(studyprogramme_ElectiveCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme_electivecourselist_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_ElectiveCourseList)


def test_studyprogramme_electivecourselist_constructor_exists():
    assert callable(studyprogramme_ElectiveCourseList.__init__)


def test_studyprogramme_electivecourselist_constructor_args():
    sig = inspect.signature(studyprogramme_ElectiveCourseList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramme_electivecourselist_has_name():
    assert hasattr(studyprogramme_ElectiveCourseList, "name")
    descriptor = None
    for klass in studyprogramme_ElectiveCourseList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme_semestercontainer_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_SemesterContainer)


def test_studyprogramme_semestercontainer_constructor_exists():
    assert callable(studyprogramme_SemesterContainer.__init__)


def test_studyprogramme_semestercontainer_constructor_args():
    sig = inspect.signature(studyprogramme_SemesterContainer.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme_courseslot_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_CourseSlot)


def test_studyprogramme_courseslot_constructor_exists():
    assert callable(studyprogramme_CourseSlot.__init__)


def test_studyprogramme_courseslot_constructor_args():
    sig = inspect.signature(studyprogramme_CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_semestercontainer_is_not_abstract():
    assert not inspect.isabstract(SemesterContainer)


def test_semestercontainer_constructor_exists():
    assert callable(SemesterContainer.__init__)


def test_semestercontainer_constructor_args():
    sig = inspect.signature(SemesterContainer.__init__)
    params = list(sig.parameters.keys())



def test_studyprogramme_specialization_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_Specialization)


def test_studyprogramme_specialization_constructor_exists():
    assert callable(studyprogramme_Specialization.__init__)


def test_studyprogramme_specialization_constructor_args():
    sig = inspect.signature(studyprogramme_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "selectionSemester" in params, "Missing parameter 'selectionSemester'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogramme_specialization_has_selectionSemester():
    assert hasattr(studyprogramme_Specialization, "selectionSemester")
    descriptor = None
    for klass in studyprogramme_Specialization.__mro__:
        if "selectionSemester" in klass.__dict__:
            descriptor = klass.__dict__["selectionSemester"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_specialization_has_name():
    assert hasattr(studyprogramme_Specialization, "name")
    descriptor = None
    for klass in studyprogramme_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme_programme_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_Programme)


def test_studyprogramme_programme_constructor_exists():
    assert callable(studyprogramme_Programme.__init__)


def test_studyprogramme_programme_constructor_args():
    sig = inspect.signature(studyprogramme_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numberOfYears" in params, "Missing parameter 'numberOfYears'"
    assert "programmeType" in params, "Missing parameter 'programmeType'"
    assert "programmeCode" in params, "Missing parameter 'programmeCode'"

def test_studyprogramme_programme_has_name():
    assert hasattr(studyprogramme_Programme, "name")
    descriptor = None
    for klass in studyprogramme_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_programme_has_numberOfYears():
    assert hasattr(studyprogramme_Programme, "numberOfYears")
    descriptor = None
    for klass in studyprogramme_Programme.__mro__:
        if "numberOfYears" in klass.__dict__:
            descriptor = klass.__dict__["numberOfYears"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_programme_has_programmeType():
    assert hasattr(studyprogramme_Programme, "programmeType")
    descriptor = None
    for klass in studyprogramme_Programme.__mro__:
        if "programmeType" in klass.__dict__:
            descriptor = klass.__dict__["programmeType"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_programme_has_programmeCode():
    assert hasattr(studyprogramme_Programme, "programmeCode")
    descriptor = None
    for klass in studyprogramme_Programme.__mro__:
        if "programmeCode" in klass.__dict__:
            descriptor = klass.__dict__["programmeCode"]
            break
    assert isinstance(descriptor, property)



def test_studyprogramme_course_is_not_abstract():
    assert not inspect.isabstract(studyprogramme_Course)


def test_studyprogramme_course_constructor_exists():
    assert callable(studyprogramme_Course.__init__)


def test_studyprogramme_course_constructor_args():
    sig = inspect.signature(studyprogramme_Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "displayedName" in params, "Missing parameter 'displayedName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "courseCode" in params, "Missing parameter 'courseCode'"

def test_studyprogramme_course_has_level():
    assert hasattr(studyprogramme_Course, "level")
    descriptor = None
    for klass in studyprogramme_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_course_has_credits():
    assert hasattr(studyprogramme_Course, "credits")
    descriptor = None
    for klass in studyprogramme_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_course_has_displayedName():
    assert hasattr(studyprogramme_Course, "displayedName")
    descriptor = None
    for klass in studyprogramme_Course.__mro__:
        if "displayedName" in klass.__dict__:
            descriptor = klass.__dict__["displayedName"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_course_has_name():
    assert hasattr(studyprogramme_Course, "name")
    descriptor = None
    for klass in studyprogramme_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogramme_course_has_courseCode():
    assert hasattr(studyprogramme_Course, "courseCode")
    descriptor = None
    for klass in studyprogramme_Course.__mro__:
        if "courseCode" in klass.__dict__:
            descriptor = klass.__dict__["courseCode"]
            break
    assert isinstance(descriptor, property)

def test_programmecode_exists():
    # Check that the Enumeration exists
    assert ProgrammeCode is not None

def test_programmecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeCode]
    expected_literals = [
        "MTDT",
        "BIT",
        "MIDT",
        "MTPROD",
        "MTIOT",
        "MIT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeCode"

def test_programmetype_exists():
    # Check that the Enumeration exists
    assert ProgrammeType is not None

def test_programmetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeType]
    expected_literals = [
        "Bachelors",
        "IntegratedMaster",
        "Masters",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeType"


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
studyprogramme_Semester_strategy = st.builds(
    studyprogramme_Semester,
    semesterNumber=
        st.integers()
)
CourseSlot_strategy = st.builds(
    CourseSlot,
)
studyprogramme_CompulsoryCourseSlot_strategy = st.builds(
    studyprogramme_CompulsoryCourseSlot,
)
studyprogramme_University_strategy = st.builds(
    studyprogramme_University,
    name=
        safe_text
)
studyprogramme_ElectiveCourseSlot_strategy = st.builds(
    studyprogramme_ElectiveCourseSlot,
)
studyprogramme_ElectiveCourseList_strategy = st.builds(
    studyprogramme_ElectiveCourseList,
    name=
        safe_text
)
studyprogramme_SemesterContainer_strategy = st.builds(
    studyprogramme_SemesterContainer,
)
studyprogramme_CourseSlot_strategy = st.builds(
    studyprogramme_CourseSlot,
)
SemesterContainer_strategy = st.builds(
    SemesterContainer,
)
studyprogramme_Specialization_strategy = st.builds(
    studyprogramme_Specialization,
    selectionSemester=
        st.integers(),
    name=
        safe_text
)
studyprogramme_Programme_strategy = st.builds(
    studyprogramme_Programme,
    name=
        safe_text,
    numberOfYears=
        st.integers(),
    programmeType=
        safe_text,
    programmeCode=
        safe_text
)
studyprogramme_Course_strategy = st.builds(
    studyprogramme_Course,
    level=
        st.integers(),
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    displayedName=
        safe_text,
    name=
        safe_text,
    courseCode=
        safe_text
)

@given(instance=studyprogramme_Semester_strategy)
@settings(max_examples=50)
def test_studyprogramme_semester_instantiation(instance):
    assert isinstance(instance, studyprogramme_Semester)



@given(instance=studyprogramme_Semester_strategy)
def test_studyprogramme_semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original

@given(instance=CourseSlot_strategy)
@settings(max_examples=50)
def test_courseslot_instantiation(instance):
    assert isinstance(instance, CourseSlot)

@given(instance=studyprogramme_CompulsoryCourseSlot_strategy)
@settings(max_examples=50)
def test_studyprogramme_compulsorycourseslot_instantiation(instance):
    assert isinstance(instance, studyprogramme_CompulsoryCourseSlot)

@given(instance=studyprogramme_University_strategy)
@settings(max_examples=50)
def test_studyprogramme_university_instantiation(instance):
    assert isinstance(instance, studyprogramme_University)



@given(instance=studyprogramme_University_strategy)
def test_studyprogramme_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme_ElectiveCourseSlot_strategy)
@settings(max_examples=50)
def test_studyprogramme_electivecourseslot_instantiation(instance):
    assert isinstance(instance, studyprogramme_ElectiveCourseSlot)

@given(instance=studyprogramme_ElectiveCourseList_strategy)
@settings(max_examples=50)
def test_studyprogramme_electivecourselist_instantiation(instance):
    assert isinstance(instance, studyprogramme_ElectiveCourseList)



@given(instance=studyprogramme_ElectiveCourseList_strategy)
def test_studyprogramme_electivecourselist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme_SemesterContainer_strategy)
@settings(max_examples=50)
def test_studyprogramme_semestercontainer_instantiation(instance):
    assert isinstance(instance, studyprogramme_SemesterContainer)

@given(instance=studyprogramme_CourseSlot_strategy)
@settings(max_examples=50)
def test_studyprogramme_courseslot_instantiation(instance):
    assert isinstance(instance, studyprogramme_CourseSlot)

@given(instance=SemesterContainer_strategy)
@settings(max_examples=50)
def test_semestercontainer_instantiation(instance):
    assert isinstance(instance, SemesterContainer)

@given(instance=studyprogramme_Specialization_strategy)
@settings(max_examples=50)
def test_studyprogramme_specialization_instantiation(instance):
    assert isinstance(instance, studyprogramme_Specialization)



@given(instance=studyprogramme_Specialization_strategy)
def test_studyprogramme_specialization_selectionSemester_setter(instance):
    original = instance.selectionSemester
    instance.selectionSemester = original
    assert instance.selectionSemester == original



@given(instance=studyprogramme_Specialization_strategy)
def test_studyprogramme_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprogramme_Programme_strategy)
@settings(max_examples=50)
def test_studyprogramme_programme_instantiation(instance):
    assert isinstance(instance, studyprogramme_Programme)



@given(instance=studyprogramme_Programme_strategy)
def test_studyprogramme_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyprogramme_Programme_strategy)
def test_studyprogramme_programme_numberOfYears_setter(instance):
    original = instance.numberOfYears
    instance.numberOfYears = original
    assert instance.numberOfYears == original



@given(instance=studyprogramme_Programme_strategy)
def test_studyprogramme_programme_programmeType_setter(instance):
    original = instance.programmeType
    instance.programmeType = original
    assert instance.programmeType == original



@given(instance=studyprogramme_Programme_strategy)
def test_studyprogramme_programme_programmeCode_setter(instance):
    original = instance.programmeCode
    instance.programmeCode = original
    assert instance.programmeCode == original

@given(instance=studyprogramme_Course_strategy)
@settings(max_examples=50)
def test_studyprogramme_course_instantiation(instance):
    assert isinstance(instance, studyprogramme_Course)



@given(instance=studyprogramme_Course_strategy)
def test_studyprogramme_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=studyprogramme_Course_strategy)
def test_studyprogramme_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=studyprogramme_Course_strategy)
def test_studyprogramme_course_displayedName_setter(instance):
    original = instance.displayedName
    instance.displayedName = original
    assert instance.displayedName == original



@given(instance=studyprogramme_Course_strategy)
def test_studyprogramme_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyprogramme_Course_strategy)
def test_studyprogramme_course_courseCode_setter(instance):
    original = instance.courseCode
    instance.courseCode = original
    assert instance.courseCode == original

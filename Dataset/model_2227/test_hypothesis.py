import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyprograms_Department,
    studyprograms_CourseAccess,
    studyprograms_Semester,
    studyprograms_Specialisation,
    studyprograms_Programme,
    studyprograms_Course,
    AvailableSemesters,
    Access,
    SemesterType,
    Level,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprograms_department_is_not_abstract():
    assert not inspect.isabstract(studyprograms_Department)


def test_studyprograms_department_constructor_exists():
    assert callable(studyprograms_Department.__init__)


def test_studyprograms_department_constructor_args():
    sig = inspect.signature(studyprograms_Department.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprograms_department_has_code():
    assert hasattr(studyprograms_Department, "code")
    descriptor = None
    for klass in studyprograms_Department.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_department_has_name():
    assert hasattr(studyprograms_Department, "name")
    descriptor = None
    for klass in studyprograms_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms_courseaccess_is_not_abstract():
    assert not inspect.isabstract(studyprograms_CourseAccess)


def test_studyprograms_courseaccess_constructor_exists():
    assert callable(studyprograms_CourseAccess.__init__)


def test_studyprograms_courseaccess_constructor_args():
    sig = inspect.signature(studyprograms_CourseAccess.__init__)
    params = list(sig.parameters.keys())
    assert "Access" in params, "Missing parameter 'Access'"

def test_studyprograms_courseaccess_has_Access():
    assert hasattr(studyprograms_CourseAccess, "Access")
    descriptor = None
    for klass in studyprograms_CourseAccess.__mro__:
        if "Access" in klass.__dict__:
            descriptor = klass.__dict__["Access"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms_semester_is_not_abstract():
    assert not inspect.isabstract(studyprograms_Semester)


def test_studyprograms_semester_constructor_exists():
    assert callable(studyprograms_Semester.__init__)


def test_studyprograms_semester_constructor_args():
    sig = inspect.signature(studyprograms_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterCode" in params, "Missing parameter 'semesterCode'"
    assert "year" in params, "Missing parameter 'year'"
    assert "semesterType" in params, "Missing parameter 'semesterType'"

def test_studyprograms_semester_has_semesterCode():
    assert hasattr(studyprograms_Semester, "semesterCode")
    descriptor = None
    for klass in studyprograms_Semester.__mro__:
        if "semesterCode" in klass.__dict__:
            descriptor = klass.__dict__["semesterCode"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_semester_has_year():
    assert hasattr(studyprograms_Semester, "year")
    descriptor = None
    for klass in studyprograms_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_semester_has_semesterType():
    assert hasattr(studyprograms_Semester, "semesterType")
    descriptor = None
    for klass in studyprograms_Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms_specialisation_is_not_abstract():
    assert not inspect.isabstract(studyprograms_Specialisation)


def test_studyprograms_specialisation_constructor_exists():
    assert callable(studyprograms_Specialisation.__init__)


def test_studyprograms_specialisation_constructor_args():
    sig = inspect.signature(studyprograms_Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "startSemester" in params, "Missing parameter 'startSemester'"

def test_studyprograms_specialisation_has_name():
    assert hasattr(studyprograms_Specialisation, "name")
    descriptor = None
    for klass in studyprograms_Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_specialisation_has_startSemester():
    assert hasattr(studyprograms_Specialisation, "startSemester")
    descriptor = None
    for klass in studyprograms_Specialisation.__mro__:
        if "startSemester" in klass.__dict__:
            descriptor = klass.__dict__["startSemester"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms_programme_is_not_abstract():
    assert not inspect.isabstract(studyprograms_Programme)


def test_studyprograms_programme_constructor_exists():
    assert callable(studyprograms_Programme.__init__)


def test_studyprograms_programme_constructor_args():
    sig = inspect.signature(studyprograms_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "startYear" in params, "Missing parameter 'startYear'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyprograms_programme_has_name():
    assert hasattr(studyprograms_Programme, "name")
    descriptor = None
    for klass in studyprograms_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_programme_has_duration():
    assert hasattr(studyprograms_Programme, "duration")
    descriptor = None
    for klass in studyprograms_Programme.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_programme_has_startYear():
    assert hasattr(studyprograms_Programme, "startYear")
    descriptor = None
    for klass in studyprograms_Programme.__mro__:
        if "startYear" in klass.__dict__:
            descriptor = klass.__dict__["startYear"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_programme_has_code():
    assert hasattr(studyprograms_Programme, "code")
    descriptor = None
    for klass in studyprograms_Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms_course_is_not_abstract():
    assert not inspect.isabstract(studyprograms_Course)


def test_studyprograms_course_constructor_exists():
    assert callable(studyprograms_Course.__init__)


def test_studyprograms_course_constructor_args():
    sig = inspect.signature(studyprograms_Course.__init__)
    params = list(sig.parameters.keys())
    assert "availableSemester" in params, "Missing parameter 'availableSemester'"
    assert "name" in params, "Missing parameter 'name'"
    assert "level" in params, "Missing parameter 'level'"
    assert "ects" in params, "Missing parameter 'ects'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyprograms_course_has_availableSemester():
    assert hasattr(studyprograms_Course, "availableSemester")
    descriptor = None
    for klass in studyprograms_Course.__mro__:
        if "availableSemester" in klass.__dict__:
            descriptor = klass.__dict__["availableSemester"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_course_has_name():
    assert hasattr(studyprograms_Course, "name")
    descriptor = None
    for klass in studyprograms_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_course_has_level():
    assert hasattr(studyprograms_Course, "level")
    descriptor = None
    for klass in studyprograms_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_course_has_ects():
    assert hasattr(studyprograms_Course, "ects")
    descriptor = None
    for klass in studyprograms_Course.__mro__:
        if "ects" in klass.__dict__:
            descriptor = klass.__dict__["ects"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms_course_has_code():
    assert hasattr(studyprograms_Course, "code")
    descriptor = None
    for klass in studyprograms_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_availablesemesters_exists():
    # Check that the Enumeration exists
    assert AvailableSemesters is not None

def test_availablesemesters_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AvailableSemesters]
    expected_literals = [
        "Both",
        "Spring",
        "Fall",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AvailableSemesters"

def test_access_exists():
    # Check that the Enumeration exists
    assert Access is not None

def test_access_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Access]
    expected_literals = [
        "M1A",
        "M2A",
        "NoAccess",
        "VA",
        "VB",
        "O",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Access"

def test_semestertype_exists():
    # Check that the Enumeration exists
    assert SemesterType is not None

def test_semestertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterType]
    expected_literals = [
        "Fall",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterType"

def test_level_exists():
    # Check that the Enumeration exists
    assert Level is not None

def test_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Level]
    expected_literals = [
        "Master",
        "Bachelor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Level"


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
studyprograms_Department_strategy = st.builds(
    studyprograms_Department,
    code=
        safe_text,
    name=
        safe_text
)
studyprograms_CourseAccess_strategy = st.builds(
    studyprograms_CourseAccess,
    Access=
        safe_text
)
studyprograms_Semester_strategy = st.builds(
    studyprograms_Semester,
    semesterCode=
        safe_text,
    year=
        st.integers(),
    semesterType=
        safe_text
)
studyprograms_Specialisation_strategy = st.builds(
    studyprograms_Specialisation,
    name=
        safe_text,
    startSemester=
        st.integers()
)
studyprograms_Programme_strategy = st.builds(
    studyprograms_Programme,
    name=
        safe_text,
    duration=
        st.integers(),
    startYear=
        st.integers(),
    code=
        safe_text
)
studyprograms_Course_strategy = st.builds(
    studyprograms_Course,
    availableSemester=
        safe_text,
    name=
        safe_text,
    level=
        safe_text,
    ects=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text
)

@given(instance=studyprograms_Department_strategy)
@settings(max_examples=50)
def test_studyprograms_department_instantiation(instance):
    assert isinstance(instance, studyprograms_Department)



@given(instance=studyprograms_Department_strategy)
def test_studyprograms_department_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=studyprograms_Department_strategy)
def test_studyprograms_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprograms_CourseAccess_strategy)
@settings(max_examples=50)
def test_studyprograms_courseaccess_instantiation(instance):
    assert isinstance(instance, studyprograms_CourseAccess)



@given(instance=studyprograms_CourseAccess_strategy)
def test_studyprograms_courseaccess_Access_setter(instance):
    original = instance.Access
    instance.Access = original
    assert instance.Access == original

@given(instance=studyprograms_Semester_strategy)
@settings(max_examples=50)
def test_studyprograms_semester_instantiation(instance):
    assert isinstance(instance, studyprograms_Semester)



@given(instance=studyprograms_Semester_strategy)
def test_studyprograms_semester_semesterCode_setter(instance):
    original = instance.semesterCode
    instance.semesterCode = original
    assert instance.semesterCode == original



@given(instance=studyprograms_Semester_strategy)
def test_studyprograms_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=studyprograms_Semester_strategy)
def test_studyprograms_semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original

@given(instance=studyprograms_Specialisation_strategy)
@settings(max_examples=50)
def test_studyprograms_specialisation_instantiation(instance):
    assert isinstance(instance, studyprograms_Specialisation)



@given(instance=studyprograms_Specialisation_strategy)
def test_studyprograms_specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyprograms_Specialisation_strategy)
def test_studyprograms_specialisation_startSemester_setter(instance):
    original = instance.startSemester
    instance.startSemester = original
    assert instance.startSemester == original

@given(instance=studyprograms_Programme_strategy)
@settings(max_examples=50)
def test_studyprograms_programme_instantiation(instance):
    assert isinstance(instance, studyprograms_Programme)



@given(instance=studyprograms_Programme_strategy)
def test_studyprograms_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyprograms_Programme_strategy)
def test_studyprograms_programme_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=studyprograms_Programme_strategy)
def test_studyprograms_programme_startYear_setter(instance):
    original = instance.startYear
    instance.startYear = original
    assert instance.startYear == original



@given(instance=studyprograms_Programme_strategy)
def test_studyprograms_programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyprograms_Course_strategy)
@settings(max_examples=50)
def test_studyprograms_course_instantiation(instance):
    assert isinstance(instance, studyprograms_Course)



@given(instance=studyprograms_Course_strategy)
def test_studyprograms_course_availableSemester_setter(instance):
    original = instance.availableSemester
    instance.availableSemester = original
    assert instance.availableSemester == original



@given(instance=studyprograms_Course_strategy)
def test_studyprograms_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyprograms_Course_strategy)
def test_studyprograms_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=studyprograms_Course_strategy)
def test_studyprograms_course_ects_setter(instance):
    original = instance.ects
    instance.ects = original
    assert instance.ects == original



@given(instance=studyprograms_Course_strategy)
def test_studyprograms_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

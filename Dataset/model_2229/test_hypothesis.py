import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyprograms::Department,
    studyprograms::CourseAccess,
    studyprograms::IndividualStudyPlan,
    studyprograms::Semester,
    studyprograms::Specialisation,
    studyprograms::Programme,
    studyprograms::Course,
    Level,
    AvailableSemesters,
    Access,
    SemesterType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprograms::department_is_not_abstract():
    assert not inspect.isabstract(studyprograms::Department)


def test_studyprograms::department_constructor_exists():
    assert callable(studyprograms::Department.__init__)


def test_studyprograms::department_constructor_args():
    sig = inspect.signature(studyprograms::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyprograms::department_has_name():
    assert hasattr(studyprograms::Department, "name")
    descriptor = None
    for klass in studyprograms::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::department_has_code():
    assert hasattr(studyprograms::Department, "code")
    descriptor = None
    for klass in studyprograms::Department.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms::courseaccess_is_not_abstract():
    assert not inspect.isabstract(studyprograms::CourseAccess)


def test_studyprograms::courseaccess_constructor_exists():
    assert callable(studyprograms::CourseAccess.__init__)


def test_studyprograms::courseaccess_constructor_args():
    sig = inspect.signature(studyprograms::CourseAccess.__init__)
    params = list(sig.parameters.keys())
    assert "Access" in params, "Missing parameter 'Access'"

def test_studyprograms::courseaccess_has_Access():
    assert hasattr(studyprograms::CourseAccess, "Access")
    descriptor = None
    for klass in studyprograms::CourseAccess.__mro__:
        if "Access" in klass.__dict__:
            descriptor = klass.__dict__["Access"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms::individualstudyplan_is_not_abstract():
    assert not inspect.isabstract(studyprograms::IndividualStudyPlan)


def test_studyprograms::individualstudyplan_constructor_exists():
    assert callable(studyprograms::IndividualStudyPlan.__init__)


def test_studyprograms::individualstudyplan_constructor_args():
    sig = inspect.signature(studyprograms::IndividualStudyPlan.__init__)
    params = list(sig.parameters.keys())
    assert "studentNo" in params, "Missing parameter 'studentNo'"

def test_studyprograms::individualstudyplan_has_studentNo():
    assert hasattr(studyprograms::IndividualStudyPlan, "studentNo")
    descriptor = None
    for klass in studyprograms::IndividualStudyPlan.__mro__:
        if "studentNo" in klass.__dict__:
            descriptor = klass.__dict__["studentNo"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms::semester_is_not_abstract():
    assert not inspect.isabstract(studyprograms::Semester)


def test_studyprograms::semester_constructor_exists():
    assert callable(studyprograms::Semester.__init__)


def test_studyprograms::semester_constructor_args():
    sig = inspect.signature(studyprograms::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterCode" in params, "Missing parameter 'semesterCode'"
    assert "year" in params, "Missing parameter 'year'"
    assert "semesterType" in params, "Missing parameter 'semesterType'"

def test_studyprograms::semester_has_semesterCode():
    assert hasattr(studyprograms::Semester, "semesterCode")
    descriptor = None
    for klass in studyprograms::Semester.__mro__:
        if "semesterCode" in klass.__dict__:
            descriptor = klass.__dict__["semesterCode"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::semester_has_year():
    assert hasattr(studyprograms::Semester, "year")
    descriptor = None
    for klass in studyprograms::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::semester_has_semesterType():
    assert hasattr(studyprograms::Semester, "semesterType")
    descriptor = None
    for klass in studyprograms::Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms::specialisation_is_not_abstract():
    assert not inspect.isabstract(studyprograms::Specialisation)


def test_studyprograms::specialisation_constructor_exists():
    assert callable(studyprograms::Specialisation.__init__)


def test_studyprograms::specialisation_constructor_args():
    sig = inspect.signature(studyprograms::Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "startSemester" in params, "Missing parameter 'startSemester'"

def test_studyprograms::specialisation_has_name():
    assert hasattr(studyprograms::Specialisation, "name")
    descriptor = None
    for klass in studyprograms::Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::specialisation_has_startSemester():
    assert hasattr(studyprograms::Specialisation, "startSemester")
    descriptor = None
    for klass in studyprograms::Specialisation.__mro__:
        if "startSemester" in klass.__dict__:
            descriptor = klass.__dict__["startSemester"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms::programme_is_not_abstract():
    assert not inspect.isabstract(studyprograms::Programme)


def test_studyprograms::programme_constructor_exists():
    assert callable(studyprograms::Programme.__init__)


def test_studyprograms::programme_constructor_args():
    sig = inspect.signature(studyprograms::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "startYear" in params, "Missing parameter 'startYear'"

def test_studyprograms::programme_has_duration():
    assert hasattr(studyprograms::Programme, "duration")
    descriptor = None
    for klass in studyprograms::Programme.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::programme_has_name():
    assert hasattr(studyprograms::Programme, "name")
    descriptor = None
    for klass in studyprograms::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::programme_has_code():
    assert hasattr(studyprograms::Programme, "code")
    descriptor = None
    for klass in studyprograms::Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::programme_has_startYear():
    assert hasattr(studyprograms::Programme, "startYear")
    descriptor = None
    for klass in studyprograms::Programme.__mro__:
        if "startYear" in klass.__dict__:
            descriptor = klass.__dict__["startYear"]
            break
    assert isinstance(descriptor, property)



def test_studyprograms::course_is_not_abstract():
    assert not inspect.isabstract(studyprograms::Course)


def test_studyprograms::course_constructor_exists():
    assert callable(studyprograms::Course.__init__)


def test_studyprograms::course_constructor_args():
    sig = inspect.signature(studyprograms::Course.__init__)
    params = list(sig.parameters.keys())
    assert "ects" in params, "Missing parameter 'ects'"
    assert "code" in params, "Missing parameter 'code'"
    assert "availableSemester" in params, "Missing parameter 'availableSemester'"
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprograms::course_has_ects():
    assert hasattr(studyprograms::Course, "ects")
    descriptor = None
    for klass in studyprograms::Course.__mro__:
        if "ects" in klass.__dict__:
            descriptor = klass.__dict__["ects"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::course_has_code():
    assert hasattr(studyprograms::Course, "code")
    descriptor = None
    for klass in studyprograms::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::course_has_availableSemester():
    assert hasattr(studyprograms::Course, "availableSemester")
    descriptor = None
    for klass in studyprograms::Course.__mro__:
        if "availableSemester" in klass.__dict__:
            descriptor = klass.__dict__["availableSemester"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::course_has_level():
    assert hasattr(studyprograms::Course, "level")
    descriptor = None
    for klass in studyprograms::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_studyprograms::course_has_name():
    assert hasattr(studyprograms::Course, "name")
    descriptor = None
    for klass in studyprograms::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_level_exists():
    # Check that the Enumeration exists
    assert Level is not None

def test_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Level]
    expected_literals = [
        "Bachelor",
        "Master",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Level"

def test_availablesemesters_exists():
    # Check that the Enumeration exists
    assert AvailableSemesters is not None

def test_availablesemesters_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AvailableSemesters]
    expected_literals = [
        "Spring",
        "Fall",
        "Both",
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
        "M2A",
        "NoAccess",
        "VB",
        "O",
        "M1A",
        "VA",
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
studyprograms::Department_strategy = st.builds(
    studyprograms::Department,
    name=
        safe_text,
    code=
        safe_text
)
studyprograms::CourseAccess_strategy = st.builds(
    studyprograms::CourseAccess,
    Access=
        safe_text
)
studyprograms::IndividualStudyPlan_strategy = st.builds(
    studyprograms::IndividualStudyPlan,
    studentNo=
        safe_text
)
studyprograms::Semester_strategy = st.builds(
    studyprograms::Semester,
    semesterCode=
        safe_text,
    year=
        st.integers(),
    semesterType=
        safe_text
)
studyprograms::Specialisation_strategy = st.builds(
    studyprograms::Specialisation,
    name=
        safe_text,
    startSemester=
        st.integers()
)
studyprograms::Programme_strategy = st.builds(
    studyprograms::Programme,
    duration=
        st.integers(),
    name=
        safe_text,
    code=
        safe_text,
    startYear=
        st.integers()
)
studyprograms::Course_strategy = st.builds(
    studyprograms::Course,
    ects=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    availableSemester=
        safe_text,
    level=
        safe_text,
    name=
        safe_text
)

@given(instance=studyprograms::Department_strategy)
@settings(max_examples=50)
def test_studyprograms::department_instantiation(instance):
    assert isinstance(instance, studyprograms::Department)

@given(instance=studyprograms::Department_strategy)
def test_studyprograms::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprograms::Department_strategy)
def test_studyprograms::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprograms::Department_strategy)
def test_studyprograms::department_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studyprograms::Department_strategy)
def test_studyprograms::department_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyprograms::CourseAccess_strategy)
@settings(max_examples=50)
def test_studyprograms::courseaccess_instantiation(instance):
    assert isinstance(instance, studyprograms::CourseAccess)

@given(instance=studyprograms::CourseAccess_strategy)
def test_studyprograms::courseaccess_Access_type(instance):
    assert isinstance(instance.Access, str)


@given(instance=studyprograms::CourseAccess_strategy)
def test_studyprograms::courseaccess_Access_setter(instance):
    original = instance.Access
    instance.Access = original
    assert instance.Access == original

@given(instance=studyprograms::IndividualStudyPlan_strategy)
@settings(max_examples=50)
def test_studyprograms::individualstudyplan_instantiation(instance):
    assert isinstance(instance, studyprograms::IndividualStudyPlan)

@given(instance=studyprograms::IndividualStudyPlan_strategy)
def test_studyprograms::individualstudyplan_studentNo_type(instance):
    assert isinstance(instance.studentNo, str)


@given(instance=studyprograms::IndividualStudyPlan_strategy)
def test_studyprograms::individualstudyplan_studentNo_setter(instance):
    original = instance.studentNo
    instance.studentNo = original
    assert instance.studentNo == original

@given(instance=studyprograms::Semester_strategy)
@settings(max_examples=50)
def test_studyprograms::semester_instantiation(instance):
    assert isinstance(instance, studyprograms::Semester)

@given(instance=studyprograms::Semester_strategy)
def test_studyprograms::semester_semesterCode_type(instance):
    assert isinstance(instance.semesterCode, str)


@given(instance=studyprograms::Semester_strategy)
def test_studyprograms::semester_semesterCode_setter(instance):
    original = instance.semesterCode
    instance.semesterCode = original
    assert instance.semesterCode == original

@given(instance=studyprograms::Semester_strategy)
def test_studyprograms::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studyprograms::Semester_strategy)
def test_studyprograms::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyprograms::Semester_strategy)
def test_studyprograms::semester_semesterType_type(instance):
    assert isinstance(instance.semesterType, str)


@given(instance=studyprograms::Semester_strategy)
def test_studyprograms::semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original

@given(instance=studyprograms::Specialisation_strategy)
@settings(max_examples=50)
def test_studyprograms::specialisation_instantiation(instance):
    assert isinstance(instance, studyprograms::Specialisation)

@given(instance=studyprograms::Specialisation_strategy)
def test_studyprograms::specialisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprograms::Specialisation_strategy)
def test_studyprograms::specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprograms::Specialisation_strategy)
def test_studyprograms::specialisation_startSemester_type(instance):
    assert isinstance(instance.startSemester, int)


@given(instance=studyprograms::Specialisation_strategy)
def test_studyprograms::specialisation_startSemester_setter(instance):
    original = instance.startSemester
    instance.startSemester = original
    assert instance.startSemester == original

@given(instance=studyprograms::Programme_strategy)
@settings(max_examples=50)
def test_studyprograms::programme_instantiation(instance):
    assert isinstance(instance, studyprograms::Programme)

@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_startYear_type(instance):
    assert isinstance(instance.startYear, int)


@given(instance=studyprograms::Programme_strategy)
def test_studyprograms::programme_startYear_setter(instance):
    original = instance.startYear
    instance.startYear = original
    assert instance.startYear == original

@given(instance=studyprograms::Course_strategy)
@settings(max_examples=50)
def test_studyprograms::course_instantiation(instance):
    assert isinstance(instance, studyprograms::Course)

@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_ects_type(instance):
    assert isinstance(instance.ects, float)


@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_ects_setter(instance):
    original = instance.ects
    instance.ects = original
    assert instance.ects == original

@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_availableSemester_type(instance):
    assert isinstance(instance.availableSemester, str)


@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_availableSemester_setter(instance):
    original = instance.availableSemester
    instance.availableSemester = original
    assert instance.availableSemester == original

@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studyprograms::Course_strategy)
def test_studyprograms::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

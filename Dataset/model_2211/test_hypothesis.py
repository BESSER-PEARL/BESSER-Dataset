import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StudyProgrammes::CourseAccess,
    StudyProgrammes::Semester,
    StudyProgrammes::Specialization,
    StudyProgrammes::Course,
    StudyProgrammes::Programme,
    StudyProgrammes::Department,
    SemesterSeason,
    Access,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogrammes::courseaccess_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes::CourseAccess)


def test_studyprogrammes::courseaccess_constructor_exists():
    assert callable(StudyProgrammes::CourseAccess.__init__)


def test_studyprogrammes::courseaccess_constructor_args():
    sig = inspect.signature(StudyProgrammes::CourseAccess.__init__)
    params = list(sig.parameters.keys())
    assert "access" in params, "Missing parameter 'access'"

def test_studyprogrammes::courseaccess_has_access():
    assert hasattr(StudyProgrammes::CourseAccess, "access")
    descriptor = None
    for klass in StudyProgrammes::CourseAccess.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes::semester_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes::Semester)


def test_studyprogrammes::semester_constructor_exists():
    assert callable(StudyProgrammes::Semester.__init__)


def test_studyprogrammes::semester_constructor_args():
    sig = inspect.signature(StudyProgrammes::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterSeason" in params, "Missing parameter 'semesterSeason'"
    assert "code" in params, "Missing parameter 'code'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyprogrammes::semester_has_semesterSeason():
    assert hasattr(StudyProgrammes::Semester, "semesterSeason")
    descriptor = None
    for klass in StudyProgrammes::Semester.__mro__:
        if "semesterSeason" in klass.__dict__:
            descriptor = klass.__dict__["semesterSeason"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::semester_has_code():
    assert hasattr(StudyProgrammes::Semester, "code")
    descriptor = None
    for klass in StudyProgrammes::Semester.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::semester_has_year():
    assert hasattr(StudyProgrammes::Semester, "year")
    descriptor = None
    for klass in StudyProgrammes::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes::specialization_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes::Specialization)


def test_studyprogrammes::specialization_constructor_exists():
    assert callable(StudyProgrammes::Specialization.__init__)


def test_studyprogrammes::specialization_constructor_args():
    sig = inspect.signature(StudyProgrammes::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "startSemester" in params, "Missing parameter 'startSemester'"
    assert "lengthInSemesters" in params, "Missing parameter 'lengthInSemesters'"
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogrammes::specialization_has_startSemester():
    assert hasattr(StudyProgrammes::Specialization, "startSemester")
    descriptor = None
    for klass in StudyProgrammes::Specialization.__mro__:
        if "startSemester" in klass.__dict__:
            descriptor = klass.__dict__["startSemester"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::specialization_has_lengthInSemesters():
    assert hasattr(StudyProgrammes::Specialization, "lengthInSemesters")
    descriptor = None
    for klass in StudyProgrammes::Specialization.__mro__:
        if "lengthInSemesters" in klass.__dict__:
            descriptor = klass.__dict__["lengthInSemesters"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::specialization_has_name():
    assert hasattr(StudyProgrammes::Specialization, "name")
    descriptor = None
    for klass in StudyProgrammes::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes::course_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes::Course)


def test_studyprogrammes::course_constructor_exists():
    assert callable(StudyProgrammes::Course.__init__)


def test_studyprogrammes::course_constructor_args():
    sig = inspect.signature(StudyProgrammes::Course.__init__)
    params = list(sig.parameters.keys())
    assert "availableSemesters" in params, "Missing parameter 'availableSemesters'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"

def test_studyprogrammes::course_has_availableSemesters():
    assert hasattr(StudyProgrammes::Course, "availableSemesters")
    descriptor = None
    for klass in StudyProgrammes::Course.__mro__:
        if "availableSemesters" in klass.__dict__:
            descriptor = klass.__dict__["availableSemesters"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::course_has_code():
    assert hasattr(StudyProgrammes::Course, "code")
    descriptor = None
    for klass in StudyProgrammes::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::course_has_name():
    assert hasattr(StudyProgrammes::Course, "name")
    descriptor = None
    for klass in StudyProgrammes::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::course_has_credits():
    assert hasattr(StudyProgrammes::Course, "credits")
    descriptor = None
    for klass in StudyProgrammes::Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes::programme_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes::Programme)


def test_studyprogrammes::programme_constructor_exists():
    assert callable(StudyProgrammes::Programme.__init__)


def test_studyprogrammes::programme_constructor_args():
    sig = inspect.signature(StudyProgrammes::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "startYear" in params, "Missing parameter 'startYear'"
    assert "code" in params, "Missing parameter 'code'"
    assert "totalNumberOfSemesters" in params, "Missing parameter 'totalNumberOfSemesters'"
    assert "semestersBeforeSpecialization" in params, "Missing parameter 'semestersBeforeSpecialization'"

def test_studyprogrammes::programme_has_name():
    assert hasattr(StudyProgrammes::Programme, "name")
    descriptor = None
    for klass in StudyProgrammes::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::programme_has_startYear():
    assert hasattr(StudyProgrammes::Programme, "startYear")
    descriptor = None
    for klass in StudyProgrammes::Programme.__mro__:
        if "startYear" in klass.__dict__:
            descriptor = klass.__dict__["startYear"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::programme_has_code():
    assert hasattr(StudyProgrammes::Programme, "code")
    descriptor = None
    for klass in StudyProgrammes::Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::programme_has_totalNumberOfSemesters():
    assert hasattr(StudyProgrammes::Programme, "totalNumberOfSemesters")
    descriptor = None
    for klass in StudyProgrammes::Programme.__mro__:
        if "totalNumberOfSemesters" in klass.__dict__:
            descriptor = klass.__dict__["totalNumberOfSemesters"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes::programme_has_semestersBeforeSpecialization():
    assert hasattr(StudyProgrammes::Programme, "semestersBeforeSpecialization")
    descriptor = None
    for klass in StudyProgrammes::Programme.__mro__:
        if "semestersBeforeSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["semestersBeforeSpecialization"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes::department_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes::Department)


def test_studyprogrammes::department_constructor_exists():
    assert callable(StudyProgrammes::Department.__init__)


def test_studyprogrammes::department_constructor_args():
    sig = inspect.signature(StudyProgrammes::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogrammes::department_has_name():
    assert hasattr(StudyProgrammes::Department, "name")
    descriptor = None
    for klass in StudyProgrammes::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_semesterseason_exists():
    # Check that the Enumeration exists
    assert SemesterSeason is not None

def test_semesterseason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterSeason]
    expected_literals = [
        "Fall",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterSeason"

def test_access_exists():
    # Check that the Enumeration exists
    assert Access is not None

def test_access_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Access]
    expected_literals = [
        "NA",
        "VA",
        "O",
        "M1A",
        "M2A",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Access"


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
StudyProgrammes::CourseAccess_strategy = st.builds(
    StudyProgrammes::CourseAccess,
    access=
        safe_text
)
StudyProgrammes::Semester_strategy = st.builds(
    StudyProgrammes::Semester,
    semesterSeason=
        safe_text,
    code=
        safe_text,
    year=
        st.integers()
)
StudyProgrammes::Specialization_strategy = st.builds(
    StudyProgrammes::Specialization,
    startSemester=
        st.integers(),
    lengthInSemesters=
        st.integers(),
    name=
        safe_text
)
StudyProgrammes::Course_strategy = st.builds(
    StudyProgrammes::Course,
    availableSemesters=
        safe_text,
    code=
        safe_text,
    name=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StudyProgrammes::Programme_strategy = st.builds(
    StudyProgrammes::Programme,
    name=
        safe_text,
    startYear=
        st.integers(),
    code=
        safe_text,
    totalNumberOfSemesters=
        st.integers(),
    semestersBeforeSpecialization=
        st.integers()
)
StudyProgrammes::Department_strategy = st.builds(
    StudyProgrammes::Department,
    name=
        safe_text
)

@given(instance=StudyProgrammes::CourseAccess_strategy)
@settings(max_examples=50)
def test_studyprogrammes::courseaccess_instantiation(instance):
    assert isinstance(instance, StudyProgrammes::CourseAccess)

@given(instance=StudyProgrammes::CourseAccess_strategy)
def test_studyprogrammes::courseaccess_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=StudyProgrammes::CourseAccess_strategy)
def test_studyprogrammes::courseaccess_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=StudyProgrammes::Semester_strategy)
@settings(max_examples=50)
def test_studyprogrammes::semester_instantiation(instance):
    assert isinstance(instance, StudyProgrammes::Semester)

@given(instance=StudyProgrammes::Semester_strategy)
def test_studyprogrammes::semester_semesterSeason_type(instance):
    assert isinstance(instance.semesterSeason, str)


@given(instance=StudyProgrammes::Semester_strategy)
def test_studyprogrammes::semester_semesterSeason_setter(instance):
    original = instance.semesterSeason
    instance.semesterSeason = original
    assert instance.semesterSeason == original

@given(instance=StudyProgrammes::Semester_strategy)
def test_studyprogrammes::semester_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=StudyProgrammes::Semester_strategy)
def test_studyprogrammes::semester_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=StudyProgrammes::Semester_strategy)
def test_studyprogrammes::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=StudyProgrammes::Semester_strategy)
def test_studyprogrammes::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=StudyProgrammes::Specialization_strategy)
@settings(max_examples=50)
def test_studyprogrammes::specialization_instantiation(instance):
    assert isinstance(instance, StudyProgrammes::Specialization)

@given(instance=StudyProgrammes::Specialization_strategy)
def test_studyprogrammes::specialization_startSemester_type(instance):
    assert isinstance(instance.startSemester, int)


@given(instance=StudyProgrammes::Specialization_strategy)
def test_studyprogrammes::specialization_startSemester_setter(instance):
    original = instance.startSemester
    instance.startSemester = original
    assert instance.startSemester == original

@given(instance=StudyProgrammes::Specialization_strategy)
def test_studyprogrammes::specialization_lengthInSemesters_type(instance):
    assert isinstance(instance.lengthInSemesters, int)


@given(instance=StudyProgrammes::Specialization_strategy)
def test_studyprogrammes::specialization_lengthInSemesters_setter(instance):
    original = instance.lengthInSemesters
    instance.lengthInSemesters = original
    assert instance.lengthInSemesters == original

@given(instance=StudyProgrammes::Specialization_strategy)
def test_studyprogrammes::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StudyProgrammes::Specialization_strategy)
def test_studyprogrammes::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StudyProgrammes::Course_strategy)
@settings(max_examples=50)
def test_studyprogrammes::course_instantiation(instance):
    assert isinstance(instance, StudyProgrammes::Course)

@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_availableSemesters_type(instance):
    assert isinstance(instance.availableSemesters, str)


@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_availableSemesters_setter(instance):
    original = instance.availableSemesters
    instance.availableSemesters = original
    assert instance.availableSemesters == original

@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=StudyProgrammes::Course_strategy)
def test_studyprogrammes::course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=StudyProgrammes::Programme_strategy)
@settings(max_examples=50)
def test_studyprogrammes::programme_instantiation(instance):
    assert isinstance(instance, StudyProgrammes::Programme)

@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_startYear_type(instance):
    assert isinstance(instance.startYear, int)


@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_startYear_setter(instance):
    original = instance.startYear
    instance.startYear = original
    assert instance.startYear == original

@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_totalNumberOfSemesters_type(instance):
    assert isinstance(instance.totalNumberOfSemesters, int)


@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_totalNumberOfSemesters_setter(instance):
    original = instance.totalNumberOfSemesters
    instance.totalNumberOfSemesters = original
    assert instance.totalNumberOfSemesters == original

@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_semestersBeforeSpecialization_type(instance):
    assert isinstance(instance.semestersBeforeSpecialization, int)


@given(instance=StudyProgrammes::Programme_strategy)
def test_studyprogrammes::programme_semestersBeforeSpecialization_setter(instance):
    original = instance.semestersBeforeSpecialization
    instance.semestersBeforeSpecialization = original
    assert instance.semestersBeforeSpecialization == original

@given(instance=StudyProgrammes::Department_strategy)
@settings(max_examples=50)
def test_studyprogrammes::department_instantiation(instance):
    assert isinstance(instance, StudyProgrammes::Department)

@given(instance=StudyProgrammes::Department_strategy)
def test_studyprogrammes::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StudyProgrammes::Department_strategy)
def test_studyprogrammes::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

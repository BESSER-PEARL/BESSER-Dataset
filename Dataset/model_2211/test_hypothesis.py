import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StudyProgrammes_CourseAccess,
    StudyProgrammes_Semester,
    StudyProgrammes_Specialization,
    StudyProgrammes_Course,
    StudyProgrammes_Programme,
    StudyProgrammes_Department,
    SemesterSeason,
    Access,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyprogrammes_courseaccess_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes_CourseAccess)


def test_studyprogrammes_courseaccess_constructor_exists():
    assert callable(StudyProgrammes_CourseAccess.__init__)


def test_studyprogrammes_courseaccess_constructor_args():
    sig = inspect.signature(StudyProgrammes_CourseAccess.__init__)
    params = list(sig.parameters.keys())
    assert "access" in params, "Missing parameter 'access'"

def test_studyprogrammes_courseaccess_has_access():
    assert hasattr(StudyProgrammes_CourseAccess, "access")
    descriptor = None
    for klass in StudyProgrammes_CourseAccess.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes_semester_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes_Semester)


def test_studyprogrammes_semester_constructor_exists():
    assert callable(StudyProgrammes_Semester.__init__)


def test_studyprogrammes_semester_constructor_args():
    sig = inspect.signature(StudyProgrammes_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterSeason" in params, "Missing parameter 'semesterSeason'"
    assert "year" in params, "Missing parameter 'year'"
    assert "code" in params, "Missing parameter 'code'"

def test_studyprogrammes_semester_has_semesterSeason():
    assert hasattr(StudyProgrammes_Semester, "semesterSeason")
    descriptor = None
    for klass in StudyProgrammes_Semester.__mro__:
        if "semesterSeason" in klass.__dict__:
            descriptor = klass.__dict__["semesterSeason"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_semester_has_year():
    assert hasattr(StudyProgrammes_Semester, "year")
    descriptor = None
    for klass in StudyProgrammes_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_semester_has_code():
    assert hasattr(StudyProgrammes_Semester, "code")
    descriptor = None
    for klass in StudyProgrammes_Semester.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes_specialization_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes_Specialization)


def test_studyprogrammes_specialization_constructor_exists():
    assert callable(StudyProgrammes_Specialization.__init__)


def test_studyprogrammes_specialization_constructor_args():
    sig = inspect.signature(StudyProgrammes_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "startSemester" in params, "Missing parameter 'startSemester'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lengthInSemesters" in params, "Missing parameter 'lengthInSemesters'"

def test_studyprogrammes_specialization_has_startSemester():
    assert hasattr(StudyProgrammes_Specialization, "startSemester")
    descriptor = None
    for klass in StudyProgrammes_Specialization.__mro__:
        if "startSemester" in klass.__dict__:
            descriptor = klass.__dict__["startSemester"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_specialization_has_name():
    assert hasattr(StudyProgrammes_Specialization, "name")
    descriptor = None
    for klass in StudyProgrammes_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_specialization_has_lengthInSemesters():
    assert hasattr(StudyProgrammes_Specialization, "lengthInSemesters")
    descriptor = None
    for klass in StudyProgrammes_Specialization.__mro__:
        if "lengthInSemesters" in klass.__dict__:
            descriptor = klass.__dict__["lengthInSemesters"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes_course_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes_Course)


def test_studyprogrammes_course_constructor_exists():
    assert callable(StudyProgrammes_Course.__init__)


def test_studyprogrammes_course_constructor_args():
    sig = inspect.signature(StudyProgrammes_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "availableSemesters" in params, "Missing parameter 'availableSemesters'"
    assert "credits" in params, "Missing parameter 'credits'"

def test_studyprogrammes_course_has_code():
    assert hasattr(StudyProgrammes_Course, "code")
    descriptor = None
    for klass in StudyProgrammes_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_course_has_name():
    assert hasattr(StudyProgrammes_Course, "name")
    descriptor = None
    for klass in StudyProgrammes_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_course_has_availableSemesters():
    assert hasattr(StudyProgrammes_Course, "availableSemesters")
    descriptor = None
    for klass in StudyProgrammes_Course.__mro__:
        if "availableSemesters" in klass.__dict__:
            descriptor = klass.__dict__["availableSemesters"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_course_has_credits():
    assert hasattr(StudyProgrammes_Course, "credits")
    descriptor = None
    for klass in StudyProgrammes_Course.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes_programme_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes_Programme)


def test_studyprogrammes_programme_constructor_exists():
    assert callable(StudyProgrammes_Programme.__init__)


def test_studyprogrammes_programme_constructor_args():
    sig = inspect.signature(StudyProgrammes_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "startYear" in params, "Missing parameter 'startYear'"
    assert "semestersBeforeSpecialization" in params, "Missing parameter 'semestersBeforeSpecialization'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"
    assert "totalNumberOfSemesters" in params, "Missing parameter 'totalNumberOfSemesters'"

def test_studyprogrammes_programme_has_startYear():
    assert hasattr(StudyProgrammes_Programme, "startYear")
    descriptor = None
    for klass in StudyProgrammes_Programme.__mro__:
        if "startYear" in klass.__dict__:
            descriptor = klass.__dict__["startYear"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_programme_has_semestersBeforeSpecialization():
    assert hasattr(StudyProgrammes_Programme, "semestersBeforeSpecialization")
    descriptor = None
    for klass in StudyProgrammes_Programme.__mro__:
        if "semestersBeforeSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["semestersBeforeSpecialization"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_programme_has_name():
    assert hasattr(StudyProgrammes_Programme, "name")
    descriptor = None
    for klass in StudyProgrammes_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_programme_has_code():
    assert hasattr(StudyProgrammes_Programme, "code")
    descriptor = None
    for klass in StudyProgrammes_Programme.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studyprogrammes_programme_has_totalNumberOfSemesters():
    assert hasattr(StudyProgrammes_Programme, "totalNumberOfSemesters")
    descriptor = None
    for klass in StudyProgrammes_Programme.__mro__:
        if "totalNumberOfSemesters" in klass.__dict__:
            descriptor = klass.__dict__["totalNumberOfSemesters"]
            break
    assert isinstance(descriptor, property)



def test_studyprogrammes_department_is_not_abstract():
    assert not inspect.isabstract(StudyProgrammes_Department)


def test_studyprogrammes_department_constructor_exists():
    assert callable(StudyProgrammes_Department.__init__)


def test_studyprogrammes_department_constructor_args():
    sig = inspect.signature(StudyProgrammes_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studyprogrammes_department_has_name():
    assert hasattr(StudyProgrammes_Department, "name")
    descriptor = None
    for klass in StudyProgrammes_Department.__mro__:
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
        "Spring",
        "Fall",
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
        "VA",
        "M1A",
        "M2A",
        "O",
        "NA",
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
StudyProgrammes_CourseAccess_strategy = st.builds(
    StudyProgrammes_CourseAccess,
    access=
        safe_text
)
StudyProgrammes_Semester_strategy = st.builds(
    StudyProgrammes_Semester,
    semesterSeason=
        safe_text,
    year=
        st.integers(),
    code=
        safe_text
)
StudyProgrammes_Specialization_strategy = st.builds(
    StudyProgrammes_Specialization,
    startSemester=
        st.integers(),
    name=
        safe_text,
    lengthInSemesters=
        st.integers()
)
StudyProgrammes_Course_strategy = st.builds(
    StudyProgrammes_Course,
    code=
        safe_text,
    name=
        safe_text,
    availableSemesters=
        safe_text,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StudyProgrammes_Programme_strategy = st.builds(
    StudyProgrammes_Programme,
    startYear=
        st.integers(),
    semestersBeforeSpecialization=
        st.integers(),
    name=
        safe_text,
    code=
        safe_text,
    totalNumberOfSemesters=
        st.integers()
)
StudyProgrammes_Department_strategy = st.builds(
    StudyProgrammes_Department,
    name=
        safe_text
)

@given(instance=StudyProgrammes_CourseAccess_strategy)
@settings(max_examples=50)
def test_studyprogrammes_courseaccess_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_CourseAccess)



@given(instance=StudyProgrammes_CourseAccess_strategy)
def test_studyprogrammes_courseaccess_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=StudyProgrammes_Semester_strategy)
@settings(max_examples=50)
def test_studyprogrammes_semester_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Semester)



@given(instance=StudyProgrammes_Semester_strategy)
def test_studyprogrammes_semester_semesterSeason_setter(instance):
    original = instance.semesterSeason
    instance.semesterSeason = original
    assert instance.semesterSeason == original



@given(instance=StudyProgrammes_Semester_strategy)
def test_studyprogrammes_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=StudyProgrammes_Semester_strategy)
def test_studyprogrammes_semester_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=StudyProgrammes_Specialization_strategy)
@settings(max_examples=50)
def test_studyprogrammes_specialization_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Specialization)



@given(instance=StudyProgrammes_Specialization_strategy)
def test_studyprogrammes_specialization_startSemester_setter(instance):
    original = instance.startSemester
    instance.startSemester = original
    assert instance.startSemester == original



@given(instance=StudyProgrammes_Specialization_strategy)
def test_studyprogrammes_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=StudyProgrammes_Specialization_strategy)
def test_studyprogrammes_specialization_lengthInSemesters_setter(instance):
    original = instance.lengthInSemesters
    instance.lengthInSemesters = original
    assert instance.lengthInSemesters == original

@given(instance=StudyProgrammes_Course_strategy)
@settings(max_examples=50)
def test_studyprogrammes_course_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Course)



@given(instance=StudyProgrammes_Course_strategy)
def test_studyprogrammes_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=StudyProgrammes_Course_strategy)
def test_studyprogrammes_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=StudyProgrammes_Course_strategy)
def test_studyprogrammes_course_availableSemesters_setter(instance):
    original = instance.availableSemesters
    instance.availableSemesters = original
    assert instance.availableSemesters == original



@given(instance=StudyProgrammes_Course_strategy)
def test_studyprogrammes_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=StudyProgrammes_Programme_strategy)
@settings(max_examples=50)
def test_studyprogrammes_programme_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Programme)



@given(instance=StudyProgrammes_Programme_strategy)
def test_studyprogrammes_programme_startYear_setter(instance):
    original = instance.startYear
    instance.startYear = original
    assert instance.startYear == original



@given(instance=StudyProgrammes_Programme_strategy)
def test_studyprogrammes_programme_semestersBeforeSpecialization_setter(instance):
    original = instance.semestersBeforeSpecialization
    instance.semestersBeforeSpecialization = original
    assert instance.semestersBeforeSpecialization == original



@given(instance=StudyProgrammes_Programme_strategy)
def test_studyprogrammes_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=StudyProgrammes_Programme_strategy)
def test_studyprogrammes_programme_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=StudyProgrammes_Programme_strategy)
def test_studyprogrammes_programme_totalNumberOfSemesters_setter(instance):
    original = instance.totalNumberOfSemesters
    instance.totalNumberOfSemesters = original
    assert instance.totalNumberOfSemesters == original

@given(instance=StudyProgrammes_Department_strategy)
@settings(max_examples=50)
def test_studyprogrammes_department_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Department)



@given(instance=StudyProgrammes_Department_strategy)
def test_studyprogrammes_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

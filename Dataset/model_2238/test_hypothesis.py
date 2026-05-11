import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studies::StudyCourse,
    studies::StudyYear,
    studies::StudyInstance,
    studies::Semester,
    studies::Study,
    studies::Course,
    studies::University,
    studies::CourseInstance,
    SemesterCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studies::studycourse_is_not_abstract():
    assert not inspect.isabstract(studies::StudyCourse)


def test_studies::studycourse_constructor_exists():
    assert callable(studies::StudyCourse.__init__)


def test_studies::studycourse_constructor_args():
    sig = inspect.signature(studies::StudyCourse.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_studies::studycourse_has_mandatory():
    assert hasattr(studies::StudyCourse, "mandatory")
    descriptor = None
    for klass in studies::StudyCourse.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_studies::studyyear_is_not_abstract():
    assert not inspect.isabstract(studies::StudyYear)


def test_studies::studyyear_constructor_exists():
    assert callable(studies::StudyYear.__init__)


def test_studies::studyyear_constructor_args():
    sig = inspect.signature(studies::StudyYear.__init__)
    params = list(sig.parameters.keys())
    assert "programName" in params, "Missing parameter 'programName'"

def test_studies::studyyear_has_programName():
    assert hasattr(studies::StudyYear, "programName")
    descriptor = None
    for klass in studies::StudyYear.__mro__:
        if "programName" in klass.__dict__:
            descriptor = klass.__dict__["programName"]
            break
    assert isinstance(descriptor, property)



def test_studies::studyinstance_is_not_abstract():
    assert not inspect.isabstract(studies::StudyInstance)


def test_studies::studyinstance_constructor_exists():
    assert callable(studies::StudyInstance.__init__)


def test_studies::studyinstance_constructor_args():
    sig = inspect.signature(studies::StudyInstance.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_studies::studyinstance_has_year():
    assert hasattr(studies::StudyInstance, "year")
    descriptor = None
    for klass in studies::StudyInstance.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studies::semester_is_not_abstract():
    assert not inspect.isabstract(studies::Semester)


def test_studies::semester_constructor_exists():
    assert callable(studies::Semester.__init__)


def test_studies::semester_constructor_args():
    sig = inspect.signature(studies::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "studyYearSemester" in params, "Missing parameter 'studyYearSemester'"

def test_studies::semester_has_studyYearSemester():
    assert hasattr(studies::Semester, "studyYearSemester")
    descriptor = None
    for klass in studies::Semester.__mro__:
        if "studyYearSemester" in klass.__dict__:
            descriptor = klass.__dict__["studyYearSemester"]
            break
    assert isinstance(descriptor, property)



def test_studies::study_is_not_abstract():
    assert not inspect.isabstract(studies::Study)


def test_studies::study_constructor_exists():
    assert callable(studies::Study.__init__)


def test_studies::study_constructor_args():
    sig = inspect.signature(studies::Study.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_studies::study_has_name():
    assert hasattr(studies::Study, "name")
    descriptor = None
    for klass in studies::Study.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studies::study_has_code():
    assert hasattr(studies::Study, "code")
    descriptor = None
    for klass in studies::Study.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studies::course_is_not_abstract():
    assert not inspect.isabstract(studies::Course)


def test_studies::course_constructor_exists():
    assert callable(studies::Course.__init__)


def test_studies::course_constructor_args():
    sig = inspect.signature(studies::Course.__init__)
    params = list(sig.parameters.keys())
    assert "studyPoints" in params, "Missing parameter 'studyPoints'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_studies::course_has_studyPoints():
    assert hasattr(studies::Course, "studyPoints")
    descriptor = None
    for klass in studies::Course.__mro__:
        if "studyPoints" in klass.__dict__:
            descriptor = klass.__dict__["studyPoints"]
            break
    assert isinstance(descriptor, property)

def test_studies::course_has_name():
    assert hasattr(studies::Course, "name")
    descriptor = None
    for klass in studies::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studies::course_has_code():
    assert hasattr(studies::Course, "code")
    descriptor = None
    for klass in studies::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studies::university_is_not_abstract():
    assert not inspect.isabstract(studies::University)


def test_studies::university_constructor_exists():
    assert callable(studies::University.__init__)


def test_studies::university_constructor_args():
    sig = inspect.signature(studies::University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studies::university_has_name():
    assert hasattr(studies::University, "name")
    descriptor = None
    for klass in studies::University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studies::courseinstance_is_not_abstract():
    assert not inspect.isabstract(studies::CourseInstance)


def test_studies::courseinstance_constructor_exists():
    assert callable(studies::CourseInstance.__init__)


def test_studies::courseinstance_constructor_args():
    sig = inspect.signature(studies::CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"
    assert "year" in params, "Missing parameter 'year'"
    assert "instanceName" in params, "Missing parameter 'instanceName'"

def test_studies::courseinstance_has_semester():
    assert hasattr(studies::CourseInstance, "semester")
    descriptor = None
    for klass in studies::CourseInstance.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_studies::courseinstance_has_year():
    assert hasattr(studies::CourseInstance, "year")
    descriptor = None
    for klass in studies::CourseInstance.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studies::courseinstance_has_instanceName():
    assert hasattr(studies::CourseInstance, "instanceName")
    descriptor = None
    for klass in studies::CourseInstance.__mro__:
        if "instanceName" in klass.__dict__:
            descriptor = klass.__dict__["instanceName"]
            break
    assert isinstance(descriptor, property)

def test_semestercode_exists():
    # Check that the Enumeration exists
    assert SemesterCode is not None

def test_semestercode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterCode]
    expected_literals = [
        "Autumn",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterCode"


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
studies::StudyCourse_strategy = st.builds(
    studies::StudyCourse,
    mandatory=
        st.booleans()
)
studies::StudyYear_strategy = st.builds(
    studies::StudyYear,
    programName=
        safe_text
)
studies::StudyInstance_strategy = st.builds(
    studies::StudyInstance,
    year=
        st.integers()
)
studies::Semester_strategy = st.builds(
    studies::Semester,
    studyYearSemester=
        safe_text
)
studies::Study_strategy = st.builds(
    studies::Study,
    name=
        safe_text,
    code=
        safe_text
)
studies::Course_strategy = st.builds(
    studies::Course,
    studyPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    code=
        safe_text
)
studies::University_strategy = st.builds(
    studies::University,
    name=
        safe_text
)
studies::CourseInstance_strategy = st.builds(
    studies::CourseInstance,
    semester=
        safe_text,
    year=
        st.integers(),
    instanceName=
        safe_text
)

@given(instance=studies::StudyCourse_strategy)
@settings(max_examples=50)
def test_studies::studycourse_instantiation(instance):
    assert isinstance(instance, studies::StudyCourse)

@given(instance=studies::StudyCourse_strategy)
def test_studies::studycourse_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=studies::StudyCourse_strategy)
def test_studies::studycourse_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=studies::StudyYear_strategy)
@settings(max_examples=50)
def test_studies::studyyear_instantiation(instance):
    assert isinstance(instance, studies::StudyYear)

@given(instance=studies::StudyYear_strategy)
def test_studies::studyyear_programName_type(instance):
    assert isinstance(instance.programName, str)


@given(instance=studies::StudyYear_strategy)
def test_studies::studyyear_programName_setter(instance):
    original = instance.programName
    instance.programName = original
    assert instance.programName == original

@given(instance=studies::StudyInstance_strategy)
@settings(max_examples=50)
def test_studies::studyinstance_instantiation(instance):
    assert isinstance(instance, studies::StudyInstance)

@given(instance=studies::StudyInstance_strategy)
def test_studies::studyinstance_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studies::StudyInstance_strategy)
def test_studies::studyinstance_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studies::Semester_strategy)
@settings(max_examples=50)
def test_studies::semester_instantiation(instance):
    assert isinstance(instance, studies::Semester)

@given(instance=studies::Semester_strategy)
def test_studies::semester_studyYearSemester_type(instance):
    assert isinstance(instance.studyYearSemester, str)


@given(instance=studies::Semester_strategy)
def test_studies::semester_studyYearSemester_setter(instance):
    original = instance.studyYearSemester
    instance.studyYearSemester = original
    assert instance.studyYearSemester == original

@given(instance=studies::Study_strategy)
@settings(max_examples=50)
def test_studies::study_instantiation(instance):
    assert isinstance(instance, studies::Study)

@given(instance=studies::Study_strategy)
def test_studies::study_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studies::Study_strategy)
def test_studies::study_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studies::Study_strategy)
def test_studies::study_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studies::Study_strategy)
def test_studies::study_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studies::Course_strategy)
@settings(max_examples=50)
def test_studies::course_instantiation(instance):
    assert isinstance(instance, studies::Course)

@given(instance=studies::Course_strategy)
def test_studies::course_studyPoints_type(instance):
    assert isinstance(instance.studyPoints, float)


@given(instance=studies::Course_strategy)
def test_studies::course_studyPoints_setter(instance):
    original = instance.studyPoints
    instance.studyPoints = original
    assert instance.studyPoints == original

@given(instance=studies::Course_strategy)
def test_studies::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studies::Course_strategy)
def test_studies::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studies::Course_strategy)
def test_studies::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=studies::Course_strategy)
def test_studies::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studies::University_strategy)
@settings(max_examples=50)
def test_studies::university_instantiation(instance):
    assert isinstance(instance, studies::University)

@given(instance=studies::University_strategy)
def test_studies::university_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=studies::University_strategy)
def test_studies::university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studies::CourseInstance_strategy)
@settings(max_examples=50)
def test_studies::courseinstance_instantiation(instance):
    assert isinstance(instance, studies::CourseInstance)

@given(instance=studies::CourseInstance_strategy)
def test_studies::courseinstance_semester_type(instance):
    assert isinstance(instance.semester, str)


@given(instance=studies::CourseInstance_strategy)
def test_studies::courseinstance_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=studies::CourseInstance_strategy)
def test_studies::courseinstance_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studies::CourseInstance_strategy)
def test_studies::courseinstance_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studies::CourseInstance_strategy)
def test_studies::courseinstance_instanceName_type(instance):
    assert isinstance(instance.instanceName, str)


@given(instance=studies::CourseInstance_strategy)
def test_studies::courseinstance_instanceName_setter(instance):
    original = instance.instanceName
    instance.instanceName = original
    assert instance.instanceName == original

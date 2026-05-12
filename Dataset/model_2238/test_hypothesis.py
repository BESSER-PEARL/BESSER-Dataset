import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studies_StudyCourse,
    studies_StudyYear,
    studies_StudyInstance,
    studies_Semester,
    studies_Study,
    studies_Course,
    studies_University,
    studies_CourseInstance,
    SemesterCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studies_studycourse_is_not_abstract():
    assert not inspect.isabstract(studies_StudyCourse)


def test_studies_studycourse_constructor_exists():
    assert callable(studies_StudyCourse.__init__)


def test_studies_studycourse_constructor_args():
    sig = inspect.signature(studies_StudyCourse.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_studies_studycourse_has_mandatory():
    assert hasattr(studies_StudyCourse, "mandatory")
    descriptor = None
    for klass in studies_StudyCourse.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_studies_studyyear_is_not_abstract():
    assert not inspect.isabstract(studies_StudyYear)


def test_studies_studyyear_constructor_exists():
    assert callable(studies_StudyYear.__init__)


def test_studies_studyyear_constructor_args():
    sig = inspect.signature(studies_StudyYear.__init__)
    params = list(sig.parameters.keys())
    assert "programName" in params, "Missing parameter 'programName'"

def test_studies_studyyear_has_programName():
    assert hasattr(studies_StudyYear, "programName")
    descriptor = None
    for klass in studies_StudyYear.__mro__:
        if "programName" in klass.__dict__:
            descriptor = klass.__dict__["programName"]
            break
    assert isinstance(descriptor, property)



def test_studies_studyinstance_is_not_abstract():
    assert not inspect.isabstract(studies_StudyInstance)


def test_studies_studyinstance_constructor_exists():
    assert callable(studies_StudyInstance.__init__)


def test_studies_studyinstance_constructor_args():
    sig = inspect.signature(studies_StudyInstance.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_studies_studyinstance_has_year():
    assert hasattr(studies_StudyInstance, "year")
    descriptor = None
    for klass in studies_StudyInstance.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studies_semester_is_not_abstract():
    assert not inspect.isabstract(studies_Semester)


def test_studies_semester_constructor_exists():
    assert callable(studies_Semester.__init__)


def test_studies_semester_constructor_args():
    sig = inspect.signature(studies_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "studyYearSemester" in params, "Missing parameter 'studyYearSemester'"

def test_studies_semester_has_studyYearSemester():
    assert hasattr(studies_Semester, "studyYearSemester")
    descriptor = None
    for klass in studies_Semester.__mro__:
        if "studyYearSemester" in klass.__dict__:
            descriptor = klass.__dict__["studyYearSemester"]
            break
    assert isinstance(descriptor, property)



def test_studies_study_is_not_abstract():
    assert not inspect.isabstract(studies_Study)


def test_studies_study_constructor_exists():
    assert callable(studies_Study.__init__)


def test_studies_study_constructor_args():
    sig = inspect.signature(studies_Study.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_studies_study_has_code():
    assert hasattr(studies_Study, "code")
    descriptor = None
    for klass in studies_Study.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_studies_study_has_name():
    assert hasattr(studies_Study, "name")
    descriptor = None
    for klass in studies_Study.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studies_course_is_not_abstract():
    assert not inspect.isabstract(studies_Course)


def test_studies_course_constructor_exists():
    assert callable(studies_Course.__init__)


def test_studies_course_constructor_args():
    sig = inspect.signature(studies_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "studyPoints" in params, "Missing parameter 'studyPoints'"
    assert "code" in params, "Missing parameter 'code'"

def test_studies_course_has_name():
    assert hasattr(studies_Course, "name")
    descriptor = None
    for klass in studies_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_studies_course_has_studyPoints():
    assert hasattr(studies_Course, "studyPoints")
    descriptor = None
    for klass in studies_Course.__mro__:
        if "studyPoints" in klass.__dict__:
            descriptor = klass.__dict__["studyPoints"]
            break
    assert isinstance(descriptor, property)

def test_studies_course_has_code():
    assert hasattr(studies_Course, "code")
    descriptor = None
    for klass in studies_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_studies_university_is_not_abstract():
    assert not inspect.isabstract(studies_University)


def test_studies_university_constructor_exists():
    assert callable(studies_University.__init__)


def test_studies_university_constructor_args():
    sig = inspect.signature(studies_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_studies_university_has_name():
    assert hasattr(studies_University, "name")
    descriptor = None
    for klass in studies_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_studies_courseinstance_is_not_abstract():
    assert not inspect.isabstract(studies_CourseInstance)


def test_studies_courseinstance_constructor_exists():
    assert callable(studies_CourseInstance.__init__)


def test_studies_courseinstance_constructor_args():
    sig = inspect.signature(studies_CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "instanceName" in params, "Missing parameter 'instanceName'"
    assert "year" in params, "Missing parameter 'year'"
    assert "semester" in params, "Missing parameter 'semester'"

def test_studies_courseinstance_has_instanceName():
    assert hasattr(studies_CourseInstance, "instanceName")
    descriptor = None
    for klass in studies_CourseInstance.__mro__:
        if "instanceName" in klass.__dict__:
            descriptor = klass.__dict__["instanceName"]
            break
    assert isinstance(descriptor, property)

def test_studies_courseinstance_has_year():
    assert hasattr(studies_CourseInstance, "year")
    descriptor = None
    for klass in studies_CourseInstance.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_studies_courseinstance_has_semester():
    assert hasattr(studies_CourseInstance, "semester")
    descriptor = None
    for klass in studies_CourseInstance.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
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
studies_StudyCourse_strategy = st.builds(
    studies_StudyCourse,
    mandatory=
        st.booleans()
)
studies_StudyYear_strategy = st.builds(
    studies_StudyYear,
    programName=
        safe_text
)
studies_StudyInstance_strategy = st.builds(
    studies_StudyInstance,
    year=
        st.integers()
)
studies_Semester_strategy = st.builds(
    studies_Semester,
    studyYearSemester=
        safe_text
)
studies_Study_strategy = st.builds(
    studies_Study,
    code=
        safe_text,
    name=
        safe_text
)
studies_Course_strategy = st.builds(
    studies_Course,
    name=
        safe_text,
    studyPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text
)
studies_University_strategy = st.builds(
    studies_University,
    name=
        safe_text
)
studies_CourseInstance_strategy = st.builds(
    studies_CourseInstance,
    instanceName=
        safe_text,
    year=
        st.integers(),
    semester=
        safe_text
)

@given(instance=studies_StudyCourse_strategy)
@settings(max_examples=50)
def test_studies_studycourse_instantiation(instance):
    assert isinstance(instance, studies_StudyCourse)



@given(instance=studies_StudyCourse_strategy)
def test_studies_studycourse_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=studies_StudyYear_strategy)
@settings(max_examples=50)
def test_studies_studyyear_instantiation(instance):
    assert isinstance(instance, studies_StudyYear)



@given(instance=studies_StudyYear_strategy)
def test_studies_studyyear_programName_setter(instance):
    original = instance.programName
    instance.programName = original
    assert instance.programName == original

@given(instance=studies_StudyInstance_strategy)
@settings(max_examples=50)
def test_studies_studyinstance_instantiation(instance):
    assert isinstance(instance, studies_StudyInstance)



@given(instance=studies_StudyInstance_strategy)
def test_studies_studyinstance_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studies_Semester_strategy)
@settings(max_examples=50)
def test_studies_semester_instantiation(instance):
    assert isinstance(instance, studies_Semester)



@given(instance=studies_Semester_strategy)
def test_studies_semester_studyYearSemester_setter(instance):
    original = instance.studyYearSemester
    instance.studyYearSemester = original
    assert instance.studyYearSemester == original

@given(instance=studies_Study_strategy)
@settings(max_examples=50)
def test_studies_study_instantiation(instance):
    assert isinstance(instance, studies_Study)



@given(instance=studies_Study_strategy)
def test_studies_study_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=studies_Study_strategy)
def test_studies_study_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studies_Course_strategy)
@settings(max_examples=50)
def test_studies_course_instantiation(instance):
    assert isinstance(instance, studies_Course)



@given(instance=studies_Course_strategy)
def test_studies_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studies_Course_strategy)
def test_studies_course_studyPoints_setter(instance):
    original = instance.studyPoints
    instance.studyPoints = original
    assert instance.studyPoints == original



@given(instance=studies_Course_strategy)
def test_studies_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=studies_University_strategy)
@settings(max_examples=50)
def test_studies_university_instantiation(instance):
    assert isinstance(instance, studies_University)



@given(instance=studies_University_strategy)
def test_studies_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=studies_CourseInstance_strategy)
@settings(max_examples=50)
def test_studies_courseinstance_instantiation(instance):
    assert isinstance(instance, studies_CourseInstance)



@given(instance=studies_CourseInstance_strategy)
def test_studies_courseinstance_instanceName_setter(instance):
    original = instance.instanceName
    instance.instanceName = original
    assert instance.instanceName == original



@given(instance=studies_CourseInstance_strategy)
def test_studies_courseinstance_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=studies_CourseInstance_strategy)
def test_studies_courseinstance_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

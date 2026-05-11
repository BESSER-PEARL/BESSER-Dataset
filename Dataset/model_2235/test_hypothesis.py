import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    studyplan::Semester,
    studyplan::Course,
    studyplan::FieldOfStudy,
    studyplan::StudyPlan,
    studyplan::Specialization,
    studyplan::CourseGroup,
    SemesterType,
    CourseStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyplan::semester_is_not_abstract():
    assert not inspect.isabstract(studyplan::Semester)


def test_studyplan::semester_constructor_exists():
    assert callable(studyplan::Semester.__init__)


def test_studyplan::semester_constructor_args():
    sig = inspect.signature(studyplan::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterType" in params, "Missing parameter 'semesterType'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyplan::semester_has_semesterType():
    assert hasattr(studyplan::Semester, "semesterType")
    descriptor = None
    for klass in studyplan::Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::semester_has_year():
    assert hasattr(studyplan::Semester, "year")
    descriptor = None
    for klass in studyplan::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::course_is_not_abstract():
    assert not inspect.isabstract(studyplan::Course)


def test_studyplan::course_constructor_exists():
    assert callable(studyplan::Course.__init__)


def test_studyplan::course_constructor_args():
    sig = inspect.signature(studyplan::Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseCode" in params, "Missing parameter 'courseCode'"
    assert "credit" in params, "Missing parameter 'credit'"
    assert "status" in params, "Missing parameter 'status'"
    assert "courseName" in params, "Missing parameter 'courseName'"

def test_studyplan::course_has_courseCode():
    assert hasattr(studyplan::Course, "courseCode")
    descriptor = None
    for klass in studyplan::Course.__mro__:
        if "courseCode" in klass.__dict__:
            descriptor = klass.__dict__["courseCode"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_credit():
    assert hasattr(studyplan::Course, "credit")
    descriptor = None
    for klass in studyplan::Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_status():
    assert hasattr(studyplan::Course, "status")
    descriptor = None
    for klass in studyplan::Course.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::course_has_courseName():
    assert hasattr(studyplan::Course, "courseName")
    descriptor = None
    for klass in studyplan::Course.__mro__:
        if "courseName" in klass.__dict__:
            descriptor = klass.__dict__["courseName"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::fieldofstudy_is_not_abstract():
    assert not inspect.isabstract(studyplan::FieldOfStudy)


def test_studyplan::fieldofstudy_constructor_exists():
    assert callable(studyplan::FieldOfStudy.__init__)


def test_studyplan::fieldofstudy_constructor_args():
    sig = inspect.signature(studyplan::FieldOfStudy.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_studyplan::fieldofstudy_has_fieldName():
    assert hasattr(studyplan::FieldOfStudy, "fieldName")
    descriptor = None
    for klass in studyplan::FieldOfStudy.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::studyplan_is_not_abstract():
    assert not inspect.isabstract(studyplan::StudyPlan)


def test_studyplan::studyplan_constructor_exists():
    assert callable(studyplan::StudyPlan.__init__)


def test_studyplan::studyplan_constructor_args():
    sig = inspect.signature(studyplan::StudyPlan.__init__)
    params = list(sig.parameters.keys())
    assert "planName" in params, "Missing parameter 'planName'"

def test_studyplan::studyplan_has_planName():
    assert hasattr(studyplan::StudyPlan, "planName")
    descriptor = None
    for klass in studyplan::StudyPlan.__mro__:
        if "planName" in klass.__dict__:
            descriptor = klass.__dict__["planName"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::specialization_is_not_abstract():
    assert not inspect.isabstract(studyplan::Specialization)


def test_studyplan::specialization_constructor_exists():
    assert callable(studyplan::Specialization.__init__)


def test_studyplan::specialization_constructor_args():
    sig = inspect.signature(studyplan::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "specName" in params, "Missing parameter 'specName'"

def test_studyplan::specialization_has_specName():
    assert hasattr(studyplan::Specialization, "specName")
    descriptor = None
    for klass in studyplan::Specialization.__mro__:
        if "specName" in klass.__dict__:
            descriptor = klass.__dict__["specName"]
            break
    assert isinstance(descriptor, property)



def test_studyplan::coursegroup_is_not_abstract():
    assert not inspect.isabstract(studyplan::CourseGroup)


def test_studyplan::coursegroup_constructor_exists():
    assert callable(studyplan::CourseGroup.__init__)


def test_studyplan::coursegroup_constructor_args():
    sig = inspect.signature(studyplan::CourseGroup.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "courseStatus" in params, "Missing parameter 'courseStatus'"

def test_studyplan::coursegroup_has_group():
    assert hasattr(studyplan::CourseGroup, "group")
    descriptor = None
    for klass in studyplan::CourseGroup.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_studyplan::coursegroup_has_courseStatus():
    assert hasattr(studyplan::CourseGroup, "courseStatus")
    descriptor = None
    for klass in studyplan::CourseGroup.__mro__:
        if "courseStatus" in klass.__dict__:
            descriptor = klass.__dict__["courseStatus"]
            break
    assert isinstance(descriptor, property)

def test_semestertype_exists():
    # Check that the Enumeration exists
    assert SemesterType is not None

def test_semestertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterType]
    expected_literals = [
        "SPRING",
        "FALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterType"

def test_coursestatus_exists():
    # Check that the Enumeration exists
    assert CourseStatus is not None

def test_coursestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseStatus]
    expected_literals = [
        "MANDATORY",
        "ELECTIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseStatus"


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
studyplan::Semester_strategy = st.builds(
    studyplan::Semester,
    semesterType=
        safe_text,
    year=
        st.integers()
)
studyplan::Course_strategy = st.builds(
    studyplan::Course,
    courseCode=
        st.integers(),
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        safe_text,
    courseName=
        safe_text
)
studyplan::FieldOfStudy_strategy = st.builds(
    studyplan::FieldOfStudy,
    fieldName=
        safe_text
)
studyplan::StudyPlan_strategy = st.builds(
    studyplan::StudyPlan,
    planName=
        safe_text
)
studyplan::Specialization_strategy = st.builds(
    studyplan::Specialization,
    specName=
        safe_text
)
studyplan::CourseGroup_strategy = st.builds(
    studyplan::CourseGroup,
    group=
        safe_text,
    courseStatus=
        safe_text
)

@given(instance=studyplan::Semester_strategy)
@settings(max_examples=50)
def test_studyplan::semester_instantiation(instance):
    assert isinstance(instance, studyplan::Semester)

@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_semesterType_type(instance):
    assert isinstance(instance.semesterType, str)


@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original

@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=studyplan::Semester_strategy)
def test_studyplan::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyplan::Course_strategy)
@settings(max_examples=50)
def test_studyplan::course_instantiation(instance):
    assert isinstance(instance, studyplan::Course)

@given(instance=studyplan::Course_strategy)
def test_studyplan::course_courseCode_type(instance):
    assert isinstance(instance.courseCode, int)


@given(instance=studyplan::Course_strategy)
def test_studyplan::course_courseCode_setter(instance):
    original = instance.courseCode
    instance.courseCode = original
    assert instance.courseCode == original

@given(instance=studyplan::Course_strategy)
def test_studyplan::course_credit_type(instance):
    assert isinstance(instance.credit, float)


@given(instance=studyplan::Course_strategy)
def test_studyplan::course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original

@given(instance=studyplan::Course_strategy)
def test_studyplan::course_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=studyplan::Course_strategy)
def test_studyplan::course_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=studyplan::Course_strategy)
def test_studyplan::course_courseName_type(instance):
    assert isinstance(instance.courseName, str)


@given(instance=studyplan::Course_strategy)
def test_studyplan::course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original

@given(instance=studyplan::FieldOfStudy_strategy)
@settings(max_examples=50)
def test_studyplan::fieldofstudy_instantiation(instance):
    assert isinstance(instance, studyplan::FieldOfStudy)

@given(instance=studyplan::FieldOfStudy_strategy)
def test_studyplan::fieldofstudy_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=studyplan::FieldOfStudy_strategy)
def test_studyplan::fieldofstudy_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=studyplan::StudyPlan_strategy)
@settings(max_examples=50)
def test_studyplan::studyplan_instantiation(instance):
    assert isinstance(instance, studyplan::StudyPlan)

@given(instance=studyplan::StudyPlan_strategy)
def test_studyplan::studyplan_planName_type(instance):
    assert isinstance(instance.planName, str)


@given(instance=studyplan::StudyPlan_strategy)
def test_studyplan::studyplan_planName_setter(instance):
    original = instance.planName
    instance.planName = original
    assert instance.planName == original

@given(instance=studyplan::Specialization_strategy)
@settings(max_examples=50)
def test_studyplan::specialization_instantiation(instance):
    assert isinstance(instance, studyplan::Specialization)

@given(instance=studyplan::Specialization_strategy)
def test_studyplan::specialization_specName_type(instance):
    assert isinstance(instance.specName, str)


@given(instance=studyplan::Specialization_strategy)
def test_studyplan::specialization_specName_setter(instance):
    original = instance.specName
    instance.specName = original
    assert instance.specName == original

@given(instance=studyplan::CourseGroup_strategy)
@settings(max_examples=50)
def test_studyplan::coursegroup_instantiation(instance):
    assert isinstance(instance, studyplan::CourseGroup)

@given(instance=studyplan::CourseGroup_strategy)
def test_studyplan::coursegroup_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=studyplan::CourseGroup_strategy)
def test_studyplan::coursegroup_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=studyplan::CourseGroup_strategy)
def test_studyplan::coursegroup_courseStatus_type(instance):
    assert isinstance(instance.courseStatus, str)


@given(instance=studyplan::CourseGroup_strategy)
def test_studyplan::coursegroup_courseStatus_setter(instance):
    original = instance.courseStatus
    instance.courseStatus = original
    assert instance.courseStatus == original

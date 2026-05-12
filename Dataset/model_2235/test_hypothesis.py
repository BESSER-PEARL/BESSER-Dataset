import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    studyplan_Semester,
    studyplan_Course,
    studyplan_FieldOfStudy,
    studyplan_StudyPlan,
    studyplan_Specialization,
    studyplan_CourseGroup,
    CourseStatus,
    SemesterType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_studyplan_semester_is_not_abstract():
    assert not inspect.isabstract(studyplan_Semester)


def test_studyplan_semester_constructor_exists():
    assert callable(studyplan_Semester.__init__)


def test_studyplan_semester_constructor_args():
    sig = inspect.signature(studyplan_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterType" in params, "Missing parameter 'semesterType'"
    assert "year" in params, "Missing parameter 'year'"

def test_studyplan_semester_has_semesterType():
    assert hasattr(studyplan_Semester, "semesterType")
    descriptor = None
    for klass in studyplan_Semester.__mro__:
        if "semesterType" in klass.__dict__:
            descriptor = klass.__dict__["semesterType"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_semester_has_year():
    assert hasattr(studyplan_Semester, "year")
    descriptor = None
    for klass in studyplan_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_course_is_not_abstract():
    assert not inspect.isabstract(studyplan_Course)


def test_studyplan_course_constructor_exists():
    assert callable(studyplan_Course.__init__)


def test_studyplan_course_constructor_args():
    sig = inspect.signature(studyplan_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credit" in params, "Missing parameter 'credit'"
    assert "courseName" in params, "Missing parameter 'courseName'"
    assert "status" in params, "Missing parameter 'status'"
    assert "courseCode" in params, "Missing parameter 'courseCode'"

def test_studyplan_course_has_credit():
    assert hasattr(studyplan_Course, "credit")
    descriptor = None
    for klass in studyplan_Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_courseName():
    assert hasattr(studyplan_Course, "courseName")
    descriptor = None
    for klass in studyplan_Course.__mro__:
        if "courseName" in klass.__dict__:
            descriptor = klass.__dict__["courseName"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_status():
    assert hasattr(studyplan_Course, "status")
    descriptor = None
    for klass in studyplan_Course.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_course_has_courseCode():
    assert hasattr(studyplan_Course, "courseCode")
    descriptor = None
    for klass in studyplan_Course.__mro__:
        if "courseCode" in klass.__dict__:
            descriptor = klass.__dict__["courseCode"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_fieldofstudy_is_not_abstract():
    assert not inspect.isabstract(studyplan_FieldOfStudy)


def test_studyplan_fieldofstudy_constructor_exists():
    assert callable(studyplan_FieldOfStudy.__init__)


def test_studyplan_fieldofstudy_constructor_args():
    sig = inspect.signature(studyplan_FieldOfStudy.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_studyplan_fieldofstudy_has_fieldName():
    assert hasattr(studyplan_FieldOfStudy, "fieldName")
    descriptor = None
    for klass in studyplan_FieldOfStudy.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_studyplan_is_not_abstract():
    assert not inspect.isabstract(studyplan_StudyPlan)


def test_studyplan_studyplan_constructor_exists():
    assert callable(studyplan_StudyPlan.__init__)


def test_studyplan_studyplan_constructor_args():
    sig = inspect.signature(studyplan_StudyPlan.__init__)
    params = list(sig.parameters.keys())
    assert "planName" in params, "Missing parameter 'planName'"

def test_studyplan_studyplan_has_planName():
    assert hasattr(studyplan_StudyPlan, "planName")
    descriptor = None
    for klass in studyplan_StudyPlan.__mro__:
        if "planName" in klass.__dict__:
            descriptor = klass.__dict__["planName"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_specialization_is_not_abstract():
    assert not inspect.isabstract(studyplan_Specialization)


def test_studyplan_specialization_constructor_exists():
    assert callable(studyplan_Specialization.__init__)


def test_studyplan_specialization_constructor_args():
    sig = inspect.signature(studyplan_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "specName" in params, "Missing parameter 'specName'"

def test_studyplan_specialization_has_specName():
    assert hasattr(studyplan_Specialization, "specName")
    descriptor = None
    for klass in studyplan_Specialization.__mro__:
        if "specName" in klass.__dict__:
            descriptor = klass.__dict__["specName"]
            break
    assert isinstance(descriptor, property)



def test_studyplan_coursegroup_is_not_abstract():
    assert not inspect.isabstract(studyplan_CourseGroup)


def test_studyplan_coursegroup_constructor_exists():
    assert callable(studyplan_CourseGroup.__init__)


def test_studyplan_coursegroup_constructor_args():
    sig = inspect.signature(studyplan_CourseGroup.__init__)
    params = list(sig.parameters.keys())
    assert "courseStatus" in params, "Missing parameter 'courseStatus'"
    assert "group" in params, "Missing parameter 'group'"

def test_studyplan_coursegroup_has_courseStatus():
    assert hasattr(studyplan_CourseGroup, "courseStatus")
    descriptor = None
    for klass in studyplan_CourseGroup.__mro__:
        if "courseStatus" in klass.__dict__:
            descriptor = klass.__dict__["courseStatus"]
            break
    assert isinstance(descriptor, property)

def test_studyplan_coursegroup_has_group():
    assert hasattr(studyplan_CourseGroup, "group")
    descriptor = None
    for klass in studyplan_CourseGroup.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_coursestatus_exists():
    # Check that the Enumeration exists
    assert CourseStatus is not None

def test_coursestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseStatus]
    expected_literals = [
        "ELECTIVE",
        "MANDATORY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseStatus"

def test_semestertype_exists():
    # Check that the Enumeration exists
    assert SemesterType is not None

def test_semestertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterType]
    expected_literals = [
        "FALL",
        "SPRING",
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
studyplan_Semester_strategy = st.builds(
    studyplan_Semester,
    semesterType=
        safe_text,
    year=
        st.integers()
)
studyplan_Course_strategy = st.builds(
    studyplan_Course,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    courseName=
        safe_text,
    status=
        safe_text,
    courseCode=
        st.integers()
)
studyplan_FieldOfStudy_strategy = st.builds(
    studyplan_FieldOfStudy,
    fieldName=
        safe_text
)
studyplan_StudyPlan_strategy = st.builds(
    studyplan_StudyPlan,
    planName=
        safe_text
)
studyplan_Specialization_strategy = st.builds(
    studyplan_Specialization,
    specName=
        safe_text
)
studyplan_CourseGroup_strategy = st.builds(
    studyplan_CourseGroup,
    courseStatus=
        safe_text,
    group=
        safe_text
)

@given(instance=studyplan_Semester_strategy)
@settings(max_examples=50)
def test_studyplan_semester_instantiation(instance):
    assert isinstance(instance, studyplan_Semester)



@given(instance=studyplan_Semester_strategy)
def test_studyplan_semester_semesterType_setter(instance):
    original = instance.semesterType
    instance.semesterType = original
    assert instance.semesterType == original



@given(instance=studyplan_Semester_strategy)
def test_studyplan_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=studyplan_Course_strategy)
@settings(max_examples=50)
def test_studyplan_course_instantiation(instance):
    assert isinstance(instance, studyplan_Course)



@given(instance=studyplan_Course_strategy)
def test_studyplan_course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original



@given(instance=studyplan_Course_strategy)
def test_studyplan_course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original



@given(instance=studyplan_Course_strategy)
def test_studyplan_course_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=studyplan_Course_strategy)
def test_studyplan_course_courseCode_setter(instance):
    original = instance.courseCode
    instance.courseCode = original
    assert instance.courseCode == original

@given(instance=studyplan_FieldOfStudy_strategy)
@settings(max_examples=50)
def test_studyplan_fieldofstudy_instantiation(instance):
    assert isinstance(instance, studyplan_FieldOfStudy)



@given(instance=studyplan_FieldOfStudy_strategy)
def test_studyplan_fieldofstudy_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=studyplan_StudyPlan_strategy)
@settings(max_examples=50)
def test_studyplan_studyplan_instantiation(instance):
    assert isinstance(instance, studyplan_StudyPlan)



@given(instance=studyplan_StudyPlan_strategy)
def test_studyplan_studyplan_planName_setter(instance):
    original = instance.planName
    instance.planName = original
    assert instance.planName == original

@given(instance=studyplan_Specialization_strategy)
@settings(max_examples=50)
def test_studyplan_specialization_instantiation(instance):
    assert isinstance(instance, studyplan_Specialization)



@given(instance=studyplan_Specialization_strategy)
def test_studyplan_specialization_specName_setter(instance):
    original = instance.specName
    instance.specName = original
    assert instance.specName == original

@given(instance=studyplan_CourseGroup_strategy)
@settings(max_examples=50)
def test_studyplan_coursegroup_instantiation(instance):
    assert isinstance(instance, studyplan_CourseGroup)



@given(instance=studyplan_CourseGroup_strategy)
def test_studyplan_coursegroup_courseStatus_setter(instance):
    original = instance.courseStatus
    instance.courseStatus = original
    assert instance.courseStatus == original



@given(instance=studyplan_CourseGroup_strategy)
def test_studyplan_coursegroup_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

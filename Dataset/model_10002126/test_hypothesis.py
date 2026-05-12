import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Administrator,
    Course,
    Student,
    AcademicResult,
    Department,
    FacultyInfo,
    Portal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "administratorID" in params, "Missing parameter 'administratorID'"
    assert "name" in params, "Missing parameter 'name'"

def test_administrator_has_administratorID():
    assert hasattr(Administrator, "administratorID")
    descriptor = None
    for klass in Administrator.__mro__:
        if "administratorID" in klass.__dict__:
            descriptor = klass.__dict__["administratorID"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_name():
    assert hasattr(Administrator, "name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseName" in params, "Missing parameter 'courseName'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"

def test_course_has_courseName():
    assert hasattr(Course, "courseName")
    descriptor = None
    for klass in Course.__mro__:
        if "courseName" in klass.__dict__:
            descriptor = klass.__dict__["courseName"]
            break
    assert isinstance(descriptor, property)

def test_course_has_subjectCode():
    assert hasattr(Course, "subjectCode")
    descriptor = None
    for klass in Course.__mro__:
        if "subjectCode" in klass.__dict__:
            descriptor = klass.__dict__["subjectCode"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "scholarNo" in params, "Missing parameter 'scholarNo'"
    assert "branch" in params, "Missing parameter 'branch'"
    assert "semester" in params, "Missing parameter 'semester'"

def test_student_has_name():
    assert hasattr(Student, "name")
    descriptor = None
    for klass in Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_student_has_scholarNo():
    assert hasattr(Student, "scholarNo")
    descriptor = None
    for klass in Student.__mro__:
        if "scholarNo" in klass.__dict__:
            descriptor = klass.__dict__["scholarNo"]
            break
    assert isinstance(descriptor, property)

def test_student_has_branch():
    assert hasattr(Student, "branch")
    descriptor = None
    for klass in Student.__mro__:
        if "branch" in klass.__dict__:
            descriptor = klass.__dict__["branch"]
            break
    assert isinstance(descriptor, property)

def test_student_has_semester():
    assert hasattr(Student, "semester")
    descriptor = None
    for klass in Student.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_academicresult_is_not_abstract():
    assert not inspect.isabstract(AcademicResult)


def test_academicresult_constructor_exists():
    assert callable(AcademicResult.__init__)


def test_academicresult_constructor_args():
    sig = inspect.signature(AcademicResult.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"

def test_academicresult_has_semester():
    assert hasattr(AcademicResult, "semester")
    descriptor = None
    for klass in AcademicResult.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "course" in params, "Missing parameter 'course'"

def test_department_has_name():
    assert hasattr(Department, "name")
    descriptor = None
    for klass in Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_department_has_course():
    assert hasattr(Department, "course")
    descriptor = None
    for klass in Department.__mro__:
        if "course" in klass.__dict__:
            descriptor = klass.__dict__["course"]
            break
    assert isinstance(descriptor, property)



def test_facultyinfo_is_not_abstract():
    assert not inspect.isabstract(FacultyInfo)


def test_facultyinfo_constructor_exists():
    assert callable(FacultyInfo.__init__)


def test_facultyinfo_constructor_args():
    sig = inspect.signature(FacultyInfo.__init__)
    params = list(sig.parameters.keys())
    assert "department" in params, "Missing parameter 'department'"
    assert "facultyName" in params, "Missing parameter 'facultyName'"
    assert "facultyID" in params, "Missing parameter 'facultyID'"

def test_facultyinfo_has_department():
    assert hasattr(FacultyInfo, "department")
    descriptor = None
    for klass in FacultyInfo.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_facultyinfo_has_facultyName():
    assert hasattr(FacultyInfo, "facultyName")
    descriptor = None
    for klass in FacultyInfo.__mro__:
        if "facultyName" in klass.__dict__:
            descriptor = klass.__dict__["facultyName"]
            break
    assert isinstance(descriptor, property)

def test_facultyinfo_has_facultyID():
    assert hasattr(FacultyInfo, "facultyID")
    descriptor = None
    for klass in FacultyInfo.__mro__:
        if "facultyID" in klass.__dict__:
            descriptor = klass.__dict__["facultyID"]
            break
    assert isinstance(descriptor, property)



def test_portal_is_not_abstract():
    assert not inspect.isabstract(Portal)


def test_portal_constructor_exists():
    assert callable(Portal.__init__)


def test_portal_constructor_args():
    sig = inspect.signature(Portal.__init__)
    params = list(sig.parameters.keys())


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
Administrator_strategy = st.builds(
    Administrator,
    administratorID=
        st.integers(),
    name=
        safe_text
)
Course_strategy = st.builds(
    Course,
    courseName=
        safe_text,
    subjectCode=
        safe_text
)
Student_strategy = st.builds(
    Student,
    name=
        safe_text,
    scholarNo=
        st.integers(),
    branch=
        st.none(),
    semester=
        st.integers()
)
AcademicResult_strategy = st.builds(
    AcademicResult,
    semester=
        st.integers()
)
Department_strategy = st.builds(
    Department,
    name=
        safe_text,
    course=
        st.none()
)
FacultyInfo_strategy = st.builds(
    FacultyInfo,
    department=
        st.none(),
    facultyName=
        safe_text,
    facultyID=
        safe_text
)
Portal_strategy = st.builds(
    Portal,
)

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_administratorID_setter(instance):
    original = instance.administratorID
    instance.administratorID = original
    assert instance.administratorID == original



@given(instance=Administrator_strategy)
def test_administrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original



@given(instance=Course_strategy)
def test_course_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Student_strategy)
def test_student_scholarNo_setter(instance):
    original = instance.scholarNo
    instance.scholarNo = original
    assert instance.scholarNo == original



@given(instance=Student_strategy)
def test_student_branch_setter(instance):
    original = instance.branch
    instance.branch = original
    assert instance.branch == original



@given(instance=Student_strategy)
def test_student_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=AcademicResult_strategy)
@settings(max_examples=50)
def test_academicresult_instantiation(instance):
    assert isinstance(instance, AcademicResult)



@given(instance=AcademicResult_strategy)
def test_academicresult_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Department_strategy)
def test_department_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original

@given(instance=FacultyInfo_strategy)
@settings(max_examples=50)
def test_facultyinfo_instantiation(instance):
    assert isinstance(instance, FacultyInfo)



@given(instance=FacultyInfo_strategy)
def test_facultyinfo_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=FacultyInfo_strategy)
def test_facultyinfo_facultyName_setter(instance):
    original = instance.facultyName
    instance.facultyName = original
    assert instance.facultyName == original



@given(instance=FacultyInfo_strategy)
def test_facultyinfo_facultyID_setter(instance):
    original = instance.facultyID
    instance.facultyID = original
    assert instance.facultyID == original

@given(instance=Portal_strategy)
@settings(max_examples=50)
def test_portal_instantiation(instance):
    assert isinstance(instance, Portal)
